#!/usr/bin/env python3
"""Read-only Ubuntu Capital OS repository monitor.

Produces a Markdown report for every run. It does not modify repository content.
Material-change reports are later surfaced by the workflow as GitHub Issues.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://api.github.com"
REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
RUN_ID = os.environ["GITHUB_RUN_ID"]
WORKSPACE = Path(os.environ.get("GITHUB_WORKSPACE", "."))
OUT_DIR = WORKSPACE / "monitoring-output"
OUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_PATH = OUT_DIR / "report.md"

DOMAIN_BENEFITS = {
    "PUB": "Investor acquisition and proposition clarity",
    "IAM": "Secure investor access and protection of private information",
    "ONB": "Investor conversion, eligibility and compliance readiness",
    "OPP": "Investment discovery and marketplace engagement",
    "DD": "Confidentiality control and investor due diligence",
    "INV": "Investor conversion into investment intent or commitment",
    "SET": "Accurate funding, reconciliation and financial control",
    "PORT": "Investor trust, transparency and retention",
    "DOC": "Investor reporting, tax support and administration",
    "NEWS": "Investor engagement and portfolio awareness",
    "EVENT": "Education and investor engagement",
    "PROFILE": "Accurate investor data and preference management",
    "REF": "Referral-led investor acquisition",
    "NOTIFY": "Timely investor action and reduced missed obligations",
    "OPS": "Operational support and controlled exception recovery",
    "ADMIN": "Controlled investment supply and platform administration",
    "AUD": "Traceability, compliance evidence and accountability",
    "REPORT": "Management visibility and compliance oversight",
    "INT": "Reliable external-service integration and operational scale",
}

AREA_RULES = [
    ("AGENT.md", "Governance"),
    ("plan.md", "Execution plan"),
    ("README.md", "Repository context"),
    ("docs/00-context", "Context and evidence"),
    ("docs/01-system-understanding", "System understanding"),
    ("docs/02-actors-and-permissions", "Actors and permissions"),
    ("docs/03-functional-domains", "Functional domains"),
    ("docs/04-use-cases", "Use cases"),
    ("docs/05-business-rules", "Business rules"),
    ("docs/06-journeys", "Journeys"),
    ("docs/07-state-models", "State models"),
    ("docs/08-integrations", "Integrations"),
    ("docs/09-delivery", "Delivery"),
    ("docs/10-traceability", "Traceability"),
    ("docs/11-open-questions", "Open questions"),
    ("docs/12-validation", "Validation"),
    ("docs/13-risks", "Risks"),
    ("contractors/80kDevelopers", "80K Developers contractor delivery"),
    ("schemas", "Schemas"),
    ("data", "Machine-readable data"),
    ("output", "Executive output"),
]


def api(path: str, params: dict | None = None):
    if params:
        path += ("&" if "?" in path else "?") + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        API + path,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ubuntu-capital-os-monitor",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {exc.code} for {path}: {body[:500]}") from exc


def parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def johannesburg_display(dt: datetime) -> str:
    # Africa/Johannesburg is UTC+02:00 year-round.
    return dt.astimezone(timezone(timedelta(hours=2))).strftime("%Y-%m-%d %H:%M SAST")


def prior_successful_run(now: datetime) -> tuple[datetime, str]:
    current = api(f"/repos/{REPO}/actions/runs/{RUN_ID}")
    workflow_id = current["workflow_id"]
    runs = api(
        f"/repos/{REPO}/actions/workflows/{workflow_id}/runs",
        {"branch": "master", "status": "success", "per_page": 20},
    ).get("workflow_runs", [])
    for run in runs:
        if str(run.get("id")) == str(RUN_ID):
            continue
        started = run.get("run_started_at") or run.get("created_at")
        if started:
            return parse_dt(started), f"previous successful workflow run #{run.get('run_number')}"
    return now - timedelta(hours=12), "first-run fallback: preceding 12 hours"


def paginate(path: str, params: dict | None = None, max_pages: int = 10):
    items = []
    params = dict(params or {})
    params.setdefault("per_page", 100)
    for page in range(1, max_pages + 1):
        params["page"] = page
        batch = api(path, params)
        if not isinstance(batch, list):
            break
        items.extend(batch)
        if len(batch) < params["per_page"]:
            break
    return items


def load_catalogue() -> tuple[dict[str, str], int | None, list[str]]:
    path = WORKSPACE / "docs/04-use-cases/use-case-catalogue.md"
    if not path.exists():
        return {}, None, ["Missing `docs/04-use-cases/use-case-catalogue.md`."]
    text = path.read_text(encoding="utf-8")
    catalogue = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*(UC-([A-Z]+)-\d+)\s*\|[^|]*\|\s*([^|]+?)\s*\|", line)
        if m:
            catalogue[m.group(1)] = m.group(3).strip()
    declared = None
    m = re.search(r"catalogue contains \*\*(\d+) use cases\*\*", text, re.I)
    if m:
        declared = int(m.group(1))
    issues = []
    if declared is not None and declared != len(catalogue):
        issues.append(f"Use-case count mismatch: catalogue declares {declared}, but {len(catalogue)} UC rows were parsed.")
    return catalogue, declared, issues


def integrity_checks(catalogue_count: int) -> list[tuple[str, str]]:
    checks = []
    required = ["AGENT.md", "plan.md", "README.md", "docs/04-use-cases/use-case-catalogue.md"]
    for rel in required:
        if not (WORKSPACE / rel).exists():
            checks.append(("HIGH", f"Required controlling/context file missing: `{rel}`."))

    plan = (WORKSPACE / "plan.md")
    if plan.exists():
        text = plan.read_text(encoding="utf-8")
        stale_counts = sorted({int(x) for x in re.findall(r"\b(\d+)-use-case\b", text)})
        for value in stale_counts:
            if value != catalogue_count:
                checks.append(("MEDIUM", f"`plan.md` references {value}-use-case while the parsed catalogue contains {catalogue_count}."))

    contractor_root = WORKSPACE / "contractors"
    if contractor_root.exists():
        names = [p.name for p in contractor_root.iterdir() if p.is_dir()]
        folded = defaultdict(list)
        for name in names:
            folded[name.lower()].append(name)
        for variants in folded.values():
            if len(variants) > 1:
                checks.append(("HIGH", f"Case-conflicting contractor directories exist: {', '.join(sorted(variants))}."))
    return checks


def area_for(path: str) -> str:
    for prefix, area in AREA_RULES:
        if path == prefix or path.startswith(prefix + "/"):
            return area
    return "Repository"


def collect_commit_activity(since: datetime):
    commits = paginate(
        f"/repos/{REPO}/commits",
        {"sha": "master", "since": since.isoformat().replace("+00:00", "Z")},
        max_pages=5,
    )
    results = []
    for c in commits:
        detail = api(f"/repos/{REPO}/commits/{c['sha']}")
        files = []
        patches = []
        for f in detail.get("files", []):
            files.append({
                "filename": f.get("filename"),
                "status": f.get("status"),
                "additions": f.get("additions", 0),
                "deletions": f.get("deletions", 0),
            })
            if f.get("patch"):
                patches.append(f["patch"])
        results.append({
            "sha": c["sha"],
            "short": c["sha"][:7],
            "message": c.get("commit", {}).get("message", "").splitlines()[0],
            "author": (c.get("author") or {}).get("login") or c.get("commit", {}).get("author", {}).get("name", "unknown"),
            "time": c.get("commit", {}).get("author", {}).get("date"),
            "files": files,
            "patch": "\n".join(patches),
        })
    return results


def collect_pr_activity(since: datetime):
    pulls = paginate(
        f"/repos/{REPO}/pulls",
        {"state": "all", "sort": "updated", "direction": "desc"},
        max_pages=3,
    )
    results = []
    for pr in pulls:
        updated = parse_dt(pr["updated_at"])
        if updated < since:
            continue
        files = paginate(f"/repos/{REPO}/pulls/{pr['number']}/files", max_pages=2)
        reviews = paginate(f"/repos/{REPO}/pulls/{pr['number']}/reviews", max_pages=2)
        review_comments = paginate(f"/repos/{REPO}/pulls/{pr['number']}/comments", max_pages=2)
        issue_comments = paginate(f"/repos/{REPO}/issues/{pr['number']}/comments", max_pages=2)
        recent_reviews = [r for r in reviews if r.get("submitted_at") and parse_dt(r["submitted_at"]) >= since]
        recent_review_comments = [r for r in review_comments if r.get("updated_at") and parse_dt(r["updated_at"]) >= since]
        recent_issue_comments = [r for r in issue_comments if r.get("updated_at") and parse_dt(r["updated_at"]) >= since]
        results.append({
            "number": pr["number"],
            "title": pr["title"],
            "state": pr["state"],
            "draft": pr.get("draft", False),
            "merged_at": pr.get("merged_at"),
            "updated_at": pr["updated_at"],
            "author": pr.get("user", {}).get("login", "unknown"),
            "files": [f.get("filename") for f in files],
            "patch": "\n".join(f.get("patch", "") for f in files if f.get("patch")),
            "reviews": len(recent_reviews),
            "review_comments": len(recent_review_comments),
            "issue_comments": len(recent_issue_comments),
        })
    return results


def affected_use_cases(catalogue: dict[str, str], commits, prs):
    ids = set()
    for item in commits + prs:
        ids.update(re.findall(r"UC-[A-Z]+-\d+", item.get("patch", "")))
        for filename in item.get("files", []):
            if isinstance(filename, dict):
                filename = filename.get("filename", "")
            ids.update(re.findall(r"UC-[A-Z]+-\d+", filename or ""))
    return sorted(uid for uid in ids if uid in catalogue)


def significance(commits, prs, integrity, use_cases) -> str:
    if any(level == "HIGH" for level, _ in integrity):
        return "HIGH"
    if use_cases or any(p.get("merged_at") for p in prs):
        return "HIGH"
    file_count = len({f["filename"] for c in commits for f in c["files"]})
    if prs or file_count >= 5:
        return "MEDIUM"
    return "LOW" if commits else "LOW"


def repository_health(integrity) -> str:
    if any(level == "HIGH" for level, _ in integrity):
        return "RED"
    if integrity:
        return "AMBER"
    return "GREEN"


def main():
    now = datetime.now(timezone.utc)
    since, checkpoint_reason = prior_successful_run(now)
    catalogue, declared_count, catalogue_issues = load_catalogue()
    integrity = [("MEDIUM", issue) for issue in catalogue_issues]
    integrity += integrity_checks(len(catalogue))

    commits = collect_commit_activity(since)
    prs = collect_pr_activity(since)
    use_cases = affected_use_cases(catalogue, commits, prs)

    all_files = sorted({
        f["filename"]
        for c in commits
        for f in c["files"]
        if f.get("filename")
    } | {
        f for p in prs for f in p["files"] if f
    })
    areas = sorted({area_for(f) for f in all_files})
    contractor_changes = [f for f in all_files if f.startswith("contractors/80kDevelopers/")]
    governance_changes = [f for f in all_files if f in {"AGENT.md", "plan.md", "README.md"} or f.startswith("docs/00-context/")]

    material_changes = bool(commits or prs or integrity)
    severity = significance(commits, prs, integrity, use_cases)
    health = repository_health(integrity)
    momentum = "NO_CHANGE"
    if material_changes:
        score = len(commits) + len(prs) + len(use_cases)
        momentum = "MAJOR" if score >= 12 else "STRONG" if score >= 7 else "MODERATE" if score >= 3 else "LOW"

    title_time = johannesburg_display(now).replace(":", "")
    report_title = f"Ubuntu Capital OS Change Report — {title_time}"

    lines = []
    lines.append("# Ubuntu Capital OS — Repository Change Report")
    lines.append("")
    lines.append(f"**Run time:** {johannesburg_display(now)}")
    lines.append(f"**Monitoring window:** {johannesburg_display(since)} → {johannesburg_display(now)} ({checkpoint_reason})")
    lines.append(f"**Repository:** `{REPO}`")
    lines.append("**Branch:** `master`")
    lines.append("")

    lines.append("## 1. Executive Summary")
    lines.append("")
    if not commits and not prs:
        lines.append("No material Ubuntu Capital OS repository commits or pull-request updates were detected during this monitoring window.")
    else:
        lines.append(f"Detected **{len(commits)} relevant commit(s)** and **{len(prs)} pull request(s) with activity** affecting **{len(all_files)} unique file(s)**.")
    lines.append(f"- Affected catalogued use cases detected from changed evidence: **{len(use_cases)}**")
    lines.append(f"- Integrity findings: **{len(integrity)}**")
    lines.append(f"- Overall significance: **{severity}**")
    if areas:
        lines.append(f"- Areas touched: {', '.join(areas)}")
    lines.append("")

    lines.append("## 2. Changes Detected")
    lines.append("")
    if commits:
        lines.append("### Commits")
        for c in commits:
            lines.append(f"- `{c['short']}` — **{c['message']}** — {c['author']} — {johannesburg_display(parse_dt(c['time'])) if c['time'] else 'time unavailable'}")
            for f in c["files"][:15]:
                lines.append(f"  - `{f['filename']}` ({f['status']}, +{f['additions']}/-{f['deletions']}) — {area_for(f['filename'])}")
            if len(c["files"]) > 15:
                lines.append(f"  - … {len(c['files']) - 15} additional file(s)")
    else:
        lines.append("No new commits on `master` were detected in the monitoring window.")
    lines.append("")
    if prs:
        lines.append("### Pull Requests")
        for p in prs:
            state = "MERGED" if p["merged_at"] else p["state"].upper()
            lines.append(f"- PR #{p['number']} — **{p['title']}** — {state} — updated {johannesburg_display(parse_dt(p['updated_at']))}")
            lines.append(f"  - Review activity: {p['reviews']} review(s), {p['review_comments']} inline review comment(s), {p['issue_comments']} conversation comment(s) in window")
            if p["files"]:
                lines.append("  - Files: " + ", ".join(f"`{f}`" for f in p["files"][:12]))
    else:
        lines.append("No pull requests changed state or received material activity in the monitoring window.")
    lines.append("")

    lines.append("## 3. Use-Case Impact")
    lines.append("")
    if use_cases:
        for uid in use_cases:
            domain = uid.split("-")[1]
            lines.append(f"### {uid} — {catalogue[uid]}")
            lines.append(f"- **Observed change:** repository patch or file path explicitly references `{uid}`.")
            lines.append("- **Evidence impact:** requires human review before changing `CONFIRMED` / `INFERRED` / `UNKNOWN` / `CONTRADICTED` classification.")
            lines.append("- **Delivery impact:** no automatic delivery-status change is made by this monitor.")
            lines.append(f"- **Business impact:** {DOMAIN_BENEFITS.get(domain, 'Potential effect on the relevant Ubuntu Capital business capability')}.")
            lines.append("- **Remaining gap:** validate the changed artefact against code, permissions, persistence, integrations, tests and E2E evidence where applicable.")
            lines.append("- **Recommended next action:** review the referenced change and update traceability/status only when objective evidence supports it.")
            lines.append("")
    else:
        lines.append("No catalogued use cases were materially and explicitly referenced by changed patches or filenames during this monitoring window.")
        lines.append("")

    lines.append("## 4. Implementation and Contractor Progress")
    lines.append("")
    if contractor_changes:
        lines.append("Changes were detected under `contractors/80kDevelopers/`:")
        for f in contractor_changes:
            lines.append(f"- `{f}`")
        lines.append("These changes are implementation-provenance evidence only; they do not automatically establish E2E use-case completion.")
    else:
        lines.append("No changes under `contractors/80kDevelopers/` were detected in this monitoring window.")
    lines.append("")

    lines.append("## 5. Governance and Evidence Changes")
    lines.append("")
    if governance_changes:
        for f in governance_changes:
            lines.append(f"- `{f}` changed and should be reviewed for downstream evidence, execution-plan or repository-context impact.")
    else:
        lines.append("No controlling-document or source-inventory changes were detected.")
    lines.append("")

    lines.append("## 6. Risks, Problems and Regressions")
    lines.append("")
    if integrity:
        for level, message in integrity:
            lines.append(f"- **{level}** — {message}")
    else:
        lines.append("No automated repository-integrity regression was detected by the monitor's current checks.")
    lines.append("")

    lines.append("## 7. Positive Progress")
    lines.append("")
    positives = []
    if commits:
        positives.append(f"{len(commits)} commit(s) progressed the repository during the window.")
    if any(p["merged_at"] for p in prs):
        positives.append("One or more pull requests were merged, moving reviewed work into the repository history.")
    if use_cases:
        positives.append(f"{len(use_cases)} use case(s) received directly traceable repository activity.")
    if not integrity:
        positives.append("Automated integrity checks found no count/casing/required-file regression.")
    if positives:
        for p in positives:
            lines.append(f"- {p}")
    else:
        lines.append("No specific positive-progress event was detected beyond repository stability during the monitoring window.")
    lines.append("")

    lines.append("## 8. Recommended Next Actions")
    lines.append("")
    recommendations = []
    for level, message in integrity:
        recommendations.append(("P1" if level == "HIGH" else "P2", f"Repair integrity finding: {message}", "Repository integrity", "Before the next delivery phase"))
    if use_cases:
        recommendations.append(("P1", "Review affected use cases and reconcile evidence/status without auto-promoting completion.", "Use-case catalogue / traceability", "Changed repository evidence"))
    if contractor_changes:
        recommendations.append(("P2", "Reconcile contractor evidence against the 41-use-case catalogue and E2E tracker.", "80K Developers contractor delivery", "Objective implementation evidence"))
    if prs:
        recommendations.append(("P2", "Review active PR findings and merge status for repository-impacting work.", "Pull requests", "PR review state"))
    if not recommendations:
        recommendations.append(("P3", "No intervention required; continue scheduled monitoring.", "Repository monitoring", "None"))
    for priority, action, area, dependency in recommendations:
        lines.append(f"- **{priority}** — {action} **Area:** {area}. **Dependency:** {dependency}.")
    lines.append("")

    lines.append("## 9. Change Ledger")
    lines.append("")
    lines.append("| Time | Commit / PR | Change | Area | Impact |")
    lines.append("|---|---|---|---|---|")
    for c in commits:
        time = johannesburg_display(parse_dt(c["time"])) if c["time"] else "Unknown"
        c_areas = sorted({area_for(f["filename"]) for f in c["files"]})
        lines.append(f"| {time} | `{c['short']}` | {c['message'].replace('|', '/')} | {', '.join(c_areas) or 'Repository'} | Repository change |")
    for p in prs:
        p_areas = sorted({area_for(f) for f in p["files"]})
        lines.append(f"| {johannesburg_display(parse_dt(p['updated_at']))} | PR #{p['number']} | {p['title'].replace('|', '/')} | {', '.join(p_areas) or 'Repository'} | PR activity |")
    if not commits and not prs:
        lines.append("| — | — | No commit or PR activity detected | Repository | No change |")
    lines.append("")

    lines.append("## 10. Overall Assessment")
    lines.append("")
    lines.append(f"**Repository health:** `{health}`")
    lines.append(f"**Implementation momentum:** `{momentum}`")
    lines.append(f"**Immediate intervention required:** `{'YES' if health == 'RED' else 'NO'}`")
    if health == "RED":
        lines.append("High-severity repository-integrity findings should be repaired before progressing delivery status.")
    elif health == "AMBER":
        lines.append("The repository remains usable, but identified integrity/evidence findings should be reconciled promptly.")
    else:
        lines.append("No automated integrity blocker was detected. Continue evidence-first review of any reported changes.")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as fh:
            fh.write(f"material_changes={'true' if material_changes else 'false'}\n")
            fh.write(f"report_title={report_title}\n")
            fh.write(f"report_path={REPORT_PATH}\n")
    print(f"Report written to {REPORT_PATH}")
    print(f"Material changes: {material_changes}; significance: {severity}; health: {health}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        REPORT_PATH.write_text(
            "# Ubuntu Capital OS — Repository Change Report\n\n"
            f"**Monitor failure:** `{type(exc).__name__}`\n\n"
            f"The scheduled monitor could not complete: {exc}\n",
            encoding="utf-8",
        )
        print(f"Monitor failed: {exc}", file=sys.stderr)
        raise
