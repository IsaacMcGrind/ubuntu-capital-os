#!/usr/bin/env python3
"""Read-only Ubuntu Capital OS repository monitor.

The monitor produces a Markdown report for every run. It does not modify
repository content. Commit inspection is performed locally from the checked-out
repository to avoid one REST call per commit. Pull-request API calls are limited
to PRs updated inside the monitoring window.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
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
DEFAULT_BRANCH = os.environ.get("DEFAULT_BRANCH", "").strip()
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


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=WORKSPACE,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout


def parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def johannesburg_display(dt: datetime) -> str:
    return dt.astimezone(timezone(timedelta(hours=2))).strftime("%Y-%m-%d %H:%M SAST")


def repository_default_branch() -> str:
    if DEFAULT_BRANCH:
        return DEFAULT_BRANCH
    repo = api(f"/repos/{REPO}")
    branch = repo.get("default_branch")
    if not branch:
        raise RuntimeError("GitHub repository metadata did not include a default branch.")
    return branch


def prior_successful_run(now: datetime, branch: str) -> tuple[datetime, str]:
    current = api(f"/repos/{REPO}/actions/runs/{RUN_ID}")
    workflow_id = current["workflow_id"]
    runs = api(
        f"/repos/{REPO}/actions/workflows/{workflow_id}/runs",
        {"branch": branch, "status": "completed", "per_page": 30},
    ).get("workflow_runs", [])
    for run in runs:
        if str(run.get("id")) == str(RUN_ID):
            continue
        if run.get("conclusion") != "success":
            continue
        started = run.get("run_started_at") or run.get("created_at")
        if started:
            return parse_dt(started), f"previous successful workflow run #{run.get('run_number')}"
    return now - timedelta(hours=12), "first-run fallback: preceding 12 hours"


def load_catalogue() -> tuple[dict[str, str], int | None, list[str]]:
    path = WORKSPACE / "docs/04-use-cases/use-case-catalogue.md"
    if not path.exists():
        return {}, None, ["Missing `docs/04-use-cases/use-case-catalogue.md`."]
    text = path.read_text(encoding="utf-8")
    catalogue: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*(UC-([A-Z]+)-\d+)\s*\|[^|]*\|\s*([^|]+?)\s*\|", line)
        if m:
            catalogue[m.group(1)] = m.group(3).strip()
    declared = None
    m = re.search(r"catalogue contains \*\*(\d+) use cases\*\*", text, re.I)
    if m:
        declared = int(m.group(1))
    issues: list[str] = []
    if declared is not None and declared != len(catalogue):
        issues.append(
            f"Use-case count mismatch: catalogue declares {declared}, but {len(catalogue)} UC rows were parsed."
        )
    return catalogue, declared, issues


def integrity_checks(catalogue_count: int) -> list[tuple[str, str]]:
    checks: list[tuple[str, str]] = []
    required = ["AGENT.md", "plan.md", "README.md", "docs/04-use-cases/use-case-catalogue.md"]
    for rel in required:
        if not (WORKSPACE / rel).exists():
            checks.append(("HIGH", f"Required controlling/context file missing: `{rel}`."))

    plan = WORKSPACE / "plan.md"
    if plan.exists():
        text = plan.read_text(encoding="utf-8")
        stale_counts = sorted({int(x) for x in re.findall(r"\b(\d+)-use-case\b", text)})
        for value in stale_counts:
            if value != catalogue_count:
                checks.append(
                    ("MEDIUM", f"`plan.md` references {value}-use-case while the parsed catalogue contains {catalogue_count}.")
                )

    contractor_root = WORKSPACE / "contractors"
    if contractor_root.exists():
        folded: dict[str, list[str]] = defaultdict(list)
        for item in contractor_root.iterdir():
            if item.is_dir():
                folded[item.name.lower()].append(item.name)
        for variants in folded.values():
            if len(variants) > 1:
                checks.append(("HIGH", f"Case-conflicting contractor directories exist: {', '.join(sorted(variants))}."))
    return checks


def area_for(path: str) -> str:
    for prefix, area in AREA_RULES:
        if path == prefix or path.startswith(prefix + "/"):
            return area
    return "Repository"


def collect_commit_activity(since: datetime, branch: str):
    since_iso = since.isoformat().replace("+00:00", "Z")
    raw = git(
        "log",
        branch,
        f"--since={since_iso}",
        "--format=%H%x1f%an%x1f%aI%x1f%s",
        "--no-merges",
    )
    results = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        sha, author, timestamp, message = line.split("\x1f", 3)
        status_raw = git("diff-tree", "--root", "--no-commit-id", "--name-status", "-r", sha)
        files = []
        for row in status_raw.splitlines():
            if not row.strip():
                continue
            parts = row.split("\t")
            status = parts[0]
            filename = parts[-1]
            files.append({"filename": filename, "status": status})
        # Local patch extraction avoids REST expansion per commit. Cap each patch so
        # a pathological commit cannot exhaust runner memory.
        patch = git("show", "--format=", "--unified=0", "--no-ext-diff", sha)
        if len(patch) > 200_000:
            patch = patch[:200_000] + "\n[patch truncated by monitor]"
        results.append(
            {
                "sha": sha,
                "short": sha[:7],
                "message": message,
                "author": author,
                "time": timestamp,
                "files": files,
                "patch": patch,
            }
        )
    return results


def recent_pull_requests(since: datetime, max_pages: int = 5, max_recent: int = 50):
    """Fetch only PRs updated in-window, stopping when sorted results become old."""
    recent = []
    for page in range(1, max_pages + 1):
        batch = api(
            f"/repos/{REPO}/pulls",
            {
                "state": "all",
                "sort": "updated",
                "direction": "desc",
                "per_page": 50,
                "page": page,
            },
        )
        if not batch:
            break
        reached_old = False
        for pr in batch:
            if parse_dt(pr["updated_at"]) < since:
                reached_old = True
                break
            recent.append(pr)
            if len(recent) >= max_recent:
                return recent
        if reached_old or len(batch) < 50:
            break
    return recent


def one_page(path: str):
    data = api(path, {"per_page": 100, "page": 1})
    return data if isinstance(data, list) else []


def collect_pr_activity(since: datetime):
    results = []
    for pr in recent_pull_requests(since):
        number = pr["number"]
        files = one_page(f"/repos/{REPO}/pulls/{number}/files")
        reviews = one_page(f"/repos/{REPO}/pulls/{number}/reviews")
        review_comments = one_page(f"/repos/{REPO}/pulls/{number}/comments")
        issue_comments = one_page(f"/repos/{REPO}/issues/{number}/comments")

        recent_reviews = [
            r for r in reviews if r.get("submitted_at") and parse_dt(r["submitted_at"]) >= since
        ]
        recent_review_comments = [
            r for r in review_comments if r.get("updated_at") and parse_dt(r["updated_at"]) >= since
        ]
        recent_issue_comments = [
            r for r in issue_comments if r.get("updated_at") and parse_dt(r["updated_at"]) >= since
        ]

        patch = "\n".join(f.get("patch", "") for f in files if f.get("patch"))
        if len(patch) > 200_000:
            patch = patch[:200_000] + "\n[PR patch truncated by monitor]"

        results.append(
            {
                "number": number,
                "title": pr["title"],
                "state": pr["state"],
                "draft": pr.get("draft", False),
                "merged_at": pr.get("merged_at"),
                "updated_at": pr["updated_at"],
                "author": pr.get("user", {}).get("login", "unknown"),
                "files": [f.get("filename") for f in files if f.get("filename")],
                "patch": patch,
                "reviews": len(recent_reviews),
                "review_comments": len(recent_review_comments),
                "issue_comments": len(recent_issue_comments),
            }
        )
    return results


def affected_use_cases(catalogue: dict[str, str], commits, prs):
    ids = set()
    for item in commits + prs:
        ids.update(re.findall(r"UC-[A-Z]+-\d+", item.get("patch", "")))
        ids.update(re.findall(r"UC-[A-Z]+-\d+", item.get("message", "")))
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
    unique_files = {f["filename"] for c in commits for f in c["files"]}
    if prs or len(unique_files) >= 5:
        return "MEDIUM"
    return "LOW"


def repository_health(integrity) -> str:
    if any(level == "HIGH" for level, _ in integrity):
        return "RED"
    if integrity:
        return "AMBER"
    return "GREEN"


def set_output(name: str, value: str) -> None:
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"{name}={value}\n")


def main() -> None:
    now = datetime.now(timezone.utc)
    branch = repository_default_branch()
    since, checkpoint_reason = prior_successful_run(now, branch)
    catalogue, _, catalogue_issues = load_catalogue()
    integrity = [("MEDIUM", issue) for issue in catalogue_issues]
    integrity += integrity_checks(len(catalogue))

    commits = collect_commit_activity(since, branch)
    prs = collect_pr_activity(since)
    use_cases = affected_use_cases(catalogue, commits, prs)

    all_files = sorted(
        {f["filename"] for c in commits for f in c["files"] if f.get("filename")}
        | {f for p in prs for f in p["files"] if f}
    )
    areas = sorted({area_for(f) for f in all_files})
    contractor_changes = [f for f in all_files if f.startswith("contractors/80kDevelopers/")]
    governance_changes = [
        f
        for f in all_files
        if f in {"AGENT.md", "plan.md", "README.md"} or f.startswith("docs/00-context/")
    ]

    severity = significance(commits, prs, integrity, use_cases)
    health = repository_health(integrity)
    score = len(commits) + len(prs) + len(use_cases)
    momentum = (
        "NO_CHANGE"
        if score == 0
        else "MAJOR"
        if score >= 12
        else "STRONG"
        if score >= 7
        else "MODERATE"
        if score >= 3
        else "LOW"
    )

    report_title = f"Ubuntu Capital OS Change Report — {johannesburg_display(now)}"
    set_output("report_title", report_title)

    lines: list[str] = [
        "# Ubuntu Capital OS — Repository Change Report",
        "",
        f"**Run time:** {johannesburg_display(now)}",
        f"**Monitoring window:** {johannesburg_display(since)} → {johannesburg_display(now)} ({checkpoint_reason})",
        f"**Repository:** `{REPO}`",
        f"**Branch:** `{branch}`",
        "",
        "## 1. Executive Summary",
        "",
    ]

    if not commits and not prs:
        lines.append("No material Ubuntu Capital OS repository changes were detected during this monitoring window.")
    else:
        lines.append(
            f"Detected **{len(commits)} relevant commit(s)** and **{len(prs)} pull request(s) with activity** affecting **{len(all_files)} unique file(s)**."
        )
    lines.extend(
        [
            f"- Affected catalogued use cases: **{len(use_cases)}**",
            f"- Overall significance: **{severity}**",
            f"- Areas touched: {', '.join(areas) if areas else 'None'}",
            "",
            "## 2. Changes Detected",
            "",
        ]
    )

    if commits:
        lines.append("### Commits")
        lines.append("")
        for c in commits:
            lines.append(
                f"- `{c['short']}` — **{c['message']}** — {c['author']} — {c['time']} — {len(c['files'])} file(s)"
            )
    else:
        lines.append("No commits were detected in the monitoring window.")

    lines.append("")
    if prs:
        lines.append("### Pull Requests")
        lines.append("")
        for pr in prs:
            state = "MERGED" if pr.get("merged_at") else pr["state"].upper()
            lines.append(
                f"- PR #{pr['number']} — **{pr['title']}** — {state} — {pr['author']} — reviews: {pr['reviews']}, review comments: {pr['review_comments']}, conversation comments: {pr['issue_comments']}"
            )
    else:
        lines.append("No pull-request activity was detected in the monitoring window.")

    lines.extend(["", "## 3. Use-Case Impact", ""])
    if use_cases:
        for uid in use_cases:
            domain = uid.split("-")[1]
            lines.extend(
                [
                    f"### {uid} — {catalogue[uid]}",
                    f"- **Observed change:** explicit use-case ID appears in changed repository evidence.",
                    f"- **Business impact:** {DOMAIN_BENEFITS.get(domain, 'Requires business-impact review')}.",
                    "- **Evidence impact:** review the changed evidence before changing `CONFIRMED`, `INFERRED`, `UNKNOWN`, or `CONTRADICTED` classification.",
                    "- **Delivery impact:** no status is changed automatically by this monitor.",
                    "- **Remaining gap:** verify E2E evidence before treating the use case as complete.",
                    "",
                ]
            )
    else:
        lines.append("No catalogued use cases were materially affected during this monitoring window.")

    lines.extend(["", "## 4. Implementation and Contractor Progress", ""])
    if contractor_changes:
        lines.append("Changes were detected under `contractors/80kDevelopers/`:")
        for path in contractor_changes:
            lines.append(f"- `{path}`")
        lines.append("Review contractor provenance against implementation and E2E evidence before changing delivery status.")
    else:
        lines.append("No contractor-delivery files changed during this window.")

    lines.extend(["", "## 5. Governance and Evidence Changes", ""])
    if governance_changes:
        for path in governance_changes:
            lines.append(f"- `{path}` changed; verify execution instructions and evidence references remain consistent.")
    else:
        lines.append("No controlling governance or context files changed.")

    lines.extend(["", "## 6. Risks, Problems and Regressions", ""])
    if integrity:
        for level, issue in integrity:
            lines.append(f"- **{level}** — {issue}")
    else:
        lines.append("No selected repository-integrity regressions were detected.")

    lines.extend(["", "## 7. Positive Progress", ""])
    if commits or prs:
        lines.append("- Repository activity occurred and has been captured in the monitoring ledger.")
        if use_cases:
            lines.append(f"- {len(use_cases)} use case(s) received explicit changed evidence for review.")
        if contractor_changes:
            lines.append("- 80K Developers contractor-delivery evidence progressed.")
    else:
        lines.append("- Repository remained stable during this monitoring window.")

    lines.extend(["", "## 8. Recommended Next Actions", ""])
    priority = 1
    for level, issue in integrity:
        lines.append(f"{priority}. **{level}** — Repair integrity issue: {issue}")
        priority += 1
    if use_cases:
        lines.append(f"{priority}. Review changed evidence for: {', '.join(use_cases)} and update statuses only if objective E2E evidence supports it.")
        priority += 1
    if contractor_changes:
        lines.append(f"{priority}. Reconcile contractor changes against the 41-use-case catalogue and current implementation status.")
        priority += 1
    if priority == 1:
        lines.append("1. No immediate remediation required; continue scheduled monitoring.")

    lines.extend(["", "## 9. Change Ledger", "", "| Time | Commit / PR | Change | Area | Impact |", "|---|---|---|---|---|"])
    for c in commits:
        area = ", ".join(sorted({area_for(f["filename"]) for f in c["files"]})) or "Repository"
        lines.append(f"| {c['time']} | `{c['short']}` | {c['message'].replace('|', '/')} | {area} | Review |")
    for pr in prs:
        area = ", ".join(sorted({area_for(f) for f in pr["files"]})) or "Repository"
        lines.append(f"| {pr['updated_at']} | PR #{pr['number']} | {pr['title'].replace('|', '/')} | {area} | Review |")
    if not commits and not prs:
        lines.append("| — | — | No material change | Repository | None |")

    intervention = "YES" if health == "RED" or severity == "HIGH" else "NO"
    lines.extend(
        [
            "",
            "## 10. Overall Assessment",
            "",
            f"**Repository health:** `{health}`",
            f"**Implementation momentum:** `{momentum}`",
            f"**Immediate intervention required:** `{intervention}`",
            "",
            "The monitor is read-only. All status, evidence-classification, contractor-record, and implementation changes require human-reviewed repository updates.",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
