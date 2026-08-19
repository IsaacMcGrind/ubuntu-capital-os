#!/usr/bin/env python3
"""Read-only Ubuntu Capital OS repository monitor."""

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
USE_CASE_PATTERN = r"UC-[A-Z]+-\d+"

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
    request = urllib.request.Request(
        API + path,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ubuntu-capital-os-monitor",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
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


def git_exists(revision: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{revision}^{{commit}}"],
        cwd=WORKSPACE,
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def ensure_commit_available(revision: str) -> bool:
    """Fetch a prior workflow head that may be unreachable after a force-push."""
    if git_exists(revision):
        return True
    subprocess.run(
        ["git", "fetch", "--no-tags", "origin", revision],
        cwd=WORKSPACE,
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return git_exists(revision)


def git_is_ancestor(ancestor: str, descendant: str) -> bool:
    result = subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        cwd=WORKSPACE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def git_merge_base(left: str, right: str) -> str | None:
    result = subprocess.run(
        ["git", "merge-base", left, right],
        cwd=WORKSPACE,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return result.stdout.strip() if result.returncode == 0 else None


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


def paginate_list(path: str, params: dict | None = None, *, max_pages: int | None = None):
    """Read all list pages; max_pages is used only for documented endpoint caps."""
    items = []
    base = dict(params or {})
    per_page = min(int(base.pop("per_page", 100)), 100)
    page = 1
    while True:
        if max_pages is not None and page > max_pages:
            break
        query = dict(base)
        query.update({"per_page": per_page, "page": page})
        batch = api(path, query)
        if not isinstance(batch, list):
            raise RuntimeError(f"Expected list response while paginating {path}.")
        items.extend(batch)
        if len(batch) < per_page:
            break
        page += 1
    return items


def prior_successful_run(now: datetime, branch: str) -> tuple[datetime, str, str | None]:
    """Find the real prior successful run and preserve its branch head SHA."""
    current = api(f"/repos/{REPO}/actions/runs/{RUN_ID}")
    workflow_id = current["workflow_id"]
    path = f"/repos/{REPO}/actions/workflows/{workflow_id}/runs"
    page = 1
    while True:
        data = api(
            path,
            {"branch": branch, "status": "completed", "per_page": 100, "page": page},
        )
        runs = data.get("workflow_runs", []) if isinstance(data, dict) else []
        if not runs:
            break
        for run in runs:
            if str(run.get("id")) == str(RUN_ID) or run.get("conclusion") != "success":
                continue
            started = run.get("run_started_at") or run.get("created_at")
            if started:
                return (
                    parse_dt(started),
                    f"previous successful workflow run #{run.get('run_number')}",
                    run.get("head_sha"),
                )
        if len(runs) < 100:
            break
        page += 1
    return now - timedelta(hours=12), "first-run fallback: preceding 12 hours", None


def load_catalogue() -> tuple[dict[str, str], int | None, list[str]]:
    path = WORKSPACE / "docs/04-use-cases/use-case-catalogue.md"
    if not path.exists():
        return {}, None, ["Missing `docs/04-use-cases/use-case-catalogue.md`."]
    text = path.read_text(encoding="utf-8")
    catalogue: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"\|\s*(UC-([A-Z]+)-\d+)\s*\|[^|]*\|\s*([^|]+?)\s*\|", line)
        if match:
            catalogue[match.group(1)] = match.group(3).strip()
    declared = None
    match = re.search(r"catalogue contains \*\*(\d+) use cases\*\*", text, re.I)
    if match:
        declared = int(match.group(1))
    issues: list[str] = []
    if declared is not None and declared != len(catalogue):
        issues.append(
            f"Use-case count mismatch: catalogue declares {declared}, but {len(catalogue)} UC rows were parsed."
        )
    return catalogue, declared, issues


def integrity_checks(catalogue_count: int) -> list[tuple[str, str]]:
    checks: list[tuple[str, str]] = []
    required = ["AGENT.md", "plan.md", "README.md", "docs/04-use-cases/use-case-catalogue.md"]
    for relative in required:
        if not (WORKSPACE / relative).exists():
            checks.append(("HIGH", f"Required controlling/context file missing: `{relative}`."))

    plan = WORKSPACE / "plan.md"
    if plan.exists():
        text = plan.read_text(encoding="utf-8")
        for value in sorted({int(x) for x in re.findall(r"\b(\d+)-use-case\b", text)}):
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


def parse_name_status(status_raw: str) -> list[dict[str, str]]:
    files = []
    for row in status_raw.splitlines():
        if not row.strip():
            continue
        parts = row.split("\t")
        status = parts[0]
        entry = {"filename": parts[-1], "status": status}
        if status.startswith("R") and len(parts) >= 3:
            entry["previous_filename"] = parts[-2]
        files.append(entry)
    return files


def first_parent(sha: str) -> str | None:
    """Return the first parent so merge diffs match their first-parent patch."""
    parts = git("rev-list", "--parents", "-n", "1", sha).strip().split()
    return parts[1] if len(parts) > 1 else None


def commit_files_and_patch(sha: str) -> tuple[list[dict[str, str]], str]:
    """Collect paths and patch against the same first-parent comparison."""
    parent = first_parent(sha)
    if parent:
        status_raw = git("diff", "--name-status", "-M", "--no-ext-diff", parent, sha)
        patch = git("diff", "--format=", "--unified=0", "--no-ext-diff", parent, sha)
    else:
        status_raw = git("diff-tree", "--root", "--no-commit-id", "--name-status", "-M", "-r", sha)
        patch = git("show", "--format=", "--unified=0", "--no-ext-diff", sha)
    return parse_name_status(status_raw), patch


def collect_commit_activity(since: datetime, branch: str, previous_head_sha: str | None):
    """Collect activity and make default-branch rewrites explicit integrity evidence."""
    rewrite = None
    previous_head_available = bool(previous_head_sha) and ensure_commit_available(previous_head_sha)
    if previous_head_sha and previous_head_available:
        if git_is_ancestor(previous_head_sha, branch):
            revision = f"{previous_head_sha}..{branch}"
        else:
            merge_base = git_merge_base(previous_head_sha, branch)
            current_head_sha = git("rev-parse", branch).strip()
            revision = f"{merge_base}..{branch}" if merge_base else branch
            status_raw = git("diff", "--name-status", "-M", "--no-ext-diff", previous_head_sha, current_head_sha)
            full_patch = git("diff", "--format=", "--unified=0", "--no-ext-diff", previous_head_sha, current_head_sha)
            files = parse_name_status(status_raw)
            use_case_ids = set(re.findall(USE_CASE_PATTERN, full_patch))
            for file_entry in files:
                use_case_ids.update(re.findall(USE_CASE_PATTERN, file_entry.get("filename", "")))
                use_case_ids.update(re.findall(USE_CASE_PATTERN, file_entry.get("previous_filename", "")))
            rewrite = {
                "kind": "diverged",
                "previous_head": previous_head_sha,
                "current_head": current_head_sha,
                "merge_base": merge_base,
                "files": files,
                "use_case_ids": sorted(use_case_ids),
            }
        raw = git("log", revision, "--format=%H%x1f%an%x1f%aI%x1f%s", "--reverse")
    else:
        since_iso = since.isoformat().replace("+00:00", "Z")
        raw = git("log", branch, f"--since={since_iso}", "--format=%H%x1f%an%x1f%aI%x1f%s", "--reverse")
        if previous_head_sha:
            rewrite = {
                "kind": "previous_head_unavailable",
                "previous_head": previous_head_sha,
                "current_head": git("rev-parse", branch).strip(),
                "merge_base": None,
                "files": [],
                "use_case_ids": [],
            }

    results = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        sha, author, timestamp, message = line.split("\x1f", 3)
        files, full_patch = commit_files_and_patch(sha)
        use_case_ids = set(re.findall(USE_CASE_PATTERN, full_patch))
        use_case_ids.update(re.findall(USE_CASE_PATTERN, message))
        for file_entry in files:
            use_case_ids.update(re.findall(USE_CASE_PATTERN, file_entry.get("filename", "")))
            use_case_ids.update(re.findall(USE_CASE_PATTERN, file_entry.get("previous_filename", "")))

        patch = full_patch
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
                "use_case_ids": sorted(use_case_ids),
            }
        )
    return results, rewrite


def recent_pull_requests(since: datetime):
    """Fetch every PR updated in-window, stopping only at the actual time boundary."""
    recent = []
    page = 1
    while True:
        batch = api(
            f"/repos/{REPO}/pulls",
            {"state": "all", "sort": "updated", "direction": "desc", "per_page": 100, "page": page},
        )
        if not isinstance(batch, list) or not batch:
            break
        for pull_request in batch:
            if parse_dt(pull_request["updated_at"]) < since:
                return recent
            recent.append(pull_request)
        if len(batch) < 100:
            break
        page += 1
    return recent


def collect_pr_activity(since: datetime):
    results = []
    for pull_request in recent_pull_requests(since):
        number = pull_request["number"]
        files = paginate_list(f"/repos/{REPO}/pulls/{number}/files", max_pages=30)
        reviews = paginate_list(f"/repos/{REPO}/pulls/{number}/reviews")
        review_comments = paginate_list(f"/repos/{REPO}/pulls/{number}/comments")
        issue_comments = paginate_list(f"/repos/{REPO}/issues/{number}/comments")

        recent_reviews = [
            review
            for review in reviews
            if review.get("submitted_at") and parse_dt(review["submitted_at"]) >= since
        ]
        recent_review_comments = [
            comment
            for comment in review_comments
            if comment.get("updated_at") and parse_dt(comment["updated_at"]) >= since
        ]
        recent_issue_comments = [
            comment
            for comment in issue_comments
            if comment.get("updated_at") and parse_dt(comment["updated_at"]) >= since
        ]

        # Seed identifiers from PR metadata before inspecting textual patches. This
        # captures binary/generated-file PRs whose use-case ID exists only in title/body.
        use_case_ids = set(re.findall(USE_CASE_PATTERN, pull_request.get("title") or ""))
        use_case_ids.update(re.findall(USE_CASE_PATTERN, pull_request.get("body") or ""))
        for review in recent_reviews:
            use_case_ids.update(re.findall(USE_CASE_PATTERN, review.get("body") or ""))
        for comment in recent_review_comments + recent_issue_comments:
            use_case_ids.update(re.findall(USE_CASE_PATTERN, comment.get("body") or ""))

        file_paths = []
        patch_parts = []
        patch_size = 0
        patch_truncated = False
        for file_entry in files:
            filename = file_entry.get("filename")
            previous_filename = file_entry.get("previous_filename")
            if filename:
                file_paths.append(filename)
                use_case_ids.update(re.findall(USE_CASE_PATTERN, filename))
            if previous_filename:
                file_paths.append(previous_filename)
                use_case_ids.update(re.findall(USE_CASE_PATTERN, previous_filename))

            part = file_entry.get("patch", "")
            if not part:
                continue
            # Extract identifiers from the complete available patch before display truncation.
            use_case_ids.update(re.findall(USE_CASE_PATTERN, part))
            remaining = 200_000 - patch_size
            if remaining > 0:
                patch_parts.append(part[:remaining])
                patch_size += len(patch_parts[-1])
                if len(part) > remaining:
                    patch_truncated = True
            else:
                patch_truncated = True

        patch = "\n".join(patch_parts)
        if patch_truncated:
            patch += "\n[PR patch truncated by monitor]"

        results.append(
            {
                "number": number,
                "title": pull_request["title"],
                "state": pull_request["state"],
                "draft": pull_request.get("draft", False),
                "merged_at": pull_request.get("merged_at"),
                "updated_at": pull_request["updated_at"],
                "author": pull_request.get("user", {}).get("login", "unknown"),
                "files": sorted(set(file_paths)),
                "patch": patch,
                "use_case_ids": sorted(use_case_ids),
                "reviews": len(recent_reviews),
                "review_comments": len(recent_review_comments),
                "issue_comments": len(recent_issue_comments),
            }
        )
    return results


def changed_use_case_ids(commits, pull_requests, rewrite=None) -> set[str]:
    ids: set[str] = set()
    for item in commits + pull_requests:
        ids.update(item.get("use_case_ids", []))
        ids.update(re.findall(USE_CASE_PATTERN, item.get("patch", "")))
        ids.update(re.findall(USE_CASE_PATTERN, item.get("message", "")))
        ids.update(re.findall(USE_CASE_PATTERN, item.get("title", "")))
        ids.update(re.findall(USE_CASE_PATTERN, item.get("body", "")))
        for filename in item.get("files", []):
            if isinstance(filename, dict):
                ids.update(re.findall(USE_CASE_PATTERN, filename.get("filename", "")))
                ids.update(re.findall(USE_CASE_PATTERN, filename.get("previous_filename", "")))
            else:
                ids.update(re.findall(USE_CASE_PATTERN, filename or ""))
    if rewrite:
        ids.update(rewrite.get("use_case_ids", []))
    return ids


def classify_use_case_changes(catalogue: dict[str, str], commits, pull_requests, rewrite=None):
    changed = changed_use_case_ids(commits, pull_requests, rewrite)
    known = sorted(uid for uid in changed if uid in catalogue)
    absent = sorted(uid for uid in changed if uid not in catalogue)
    return known, absent


def significance(commits, pull_requests, integrity, known_use_cases, absent_use_cases) -> str:
    if any(level == "HIGH" for level, _ in integrity):
        return "HIGH"
    if known_use_cases or absent_use_cases or any(pr.get("merged_at") for pr in pull_requests):
        return "HIGH"
    unique_files = {file_entry["filename"] for commit in commits for file_entry in commit["files"]}
    return "MEDIUM" if pull_requests or len(unique_files) >= 5 else "LOW"


def repository_health(integrity) -> str:
    if any(level == "HIGH" for level, _ in integrity):
        return "RED"
    return "AMBER" if integrity else "GREEN"


def set_output(name: str, value: str) -> None:
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"{name}={value}\n")


def main() -> None:
    now = datetime.now(timezone.utc)
    branch = repository_default_branch()
    since, checkpoint_reason, previous_head_sha = prior_successful_run(now, branch)
    catalogue, _, catalogue_issues = load_catalogue()
    integrity = [("MEDIUM", issue) for issue in catalogue_issues] + integrity_checks(len(catalogue))

    commits, rewrite = collect_commit_activity(since, branch, previous_head_sha)
    pull_requests = collect_pr_activity(since)
    use_cases, absent_use_cases = classify_use_case_changes(catalogue, commits, pull_requests, rewrite)
    if rewrite:
        if rewrite["kind"] == "diverged":
            integrity.append(
                (
                    "HIGH",
                    "Default-branch history rewrite detected: previous successful head "
                    f"`{rewrite['previous_head']}` is not an ancestor of current head `{rewrite['current_head']}`. "
                    f"The monitor compared current state with the prior head and collected current-branch commits after merge base `{rewrite['merge_base'] or 'none'}`; "
                    "activity removed by the rewrite cannot be reconstructed from the current branch and requires human review.",
                )
            )
        else:
            integrity.append(
                (
                    "HIGH",
                    "Previous successful workflow head "
                    f"`{rewrite['previous_head']}` could not be fetched from `origin` or found in the checkout. "
                    "Default-branch continuity and state comparison cannot be verified; review for a force-push, object retention issue, or repository-access failure.",
                )
            )
    if absent_use_cases:
        integrity.append(
            (
                "MEDIUM",
                "Changed evidence references use-case ID(s) absent from the current catalogue: "
                + ", ".join(absent_use_cases)
                + ". Treat these as removed, renamed, or unknown identifiers until reconciled.",
            )
        )

    all_files = sorted(
        {file_entry["filename"] for commit in commits for file_entry in commit["files"] if file_entry.get("filename")}
        | {
            file_entry.get("previous_filename")
            for commit in commits
            for file_entry in commit["files"]
            if file_entry.get("previous_filename")
        }
        | {filename for pull_request in pull_requests for filename in pull_request["files"] if filename}
        | {
            file_entry.get("filename")
            for file_entry in (rewrite or {}).get("files", [])
            if file_entry.get("filename")
        }
        | {
            file_entry.get("previous_filename")
            for file_entry in (rewrite or {}).get("files", [])
            if file_entry.get("previous_filename")
        }
    )
    areas = sorted({area_for(filename) for filename in all_files})
    contractor_changes = [filename for filename in all_files if filename.startswith("contractors/80kDevelopers/")]
    governance_changes = [
        filename
        for filename in all_files
        if filename in {"AGENT.md", "plan.md", "README.md"} or filename.startswith("docs/00-context/")
    ]

    severity = significance(commits, pull_requests, integrity, use_cases, absent_use_cases)
    health = repository_health(integrity)
    score = len(commits) + len(pull_requests) + len(use_cases) + len(absent_use_cases) + int(bool(rewrite))
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
    set_output("reportable", "true" if commits or pull_requests or rewrite else "false")

    lines: list[str] = [
        "# Ubuntu Capital OS — Repository Change Report",
        "",
        f"**Run time:** {johannesburg_display(now)}",
        f"**Monitoring window:** {johannesburg_display(since)} → {johannesburg_display(now)} ({checkpoint_reason})",
        f"**Repository:** `{REPO}`",
        f"**Branch:** `{branch}`",
        f"**Previous successful head:** `{previous_head_sha}`" if previous_head_sha else "**Previous successful head:** unavailable (time fallback used)",
        "",
        "## 1. Executive Summary",
        "",
    ]
    if not commits and not pull_requests and not rewrite:
        lines.append("No material Ubuntu Capital OS repository changes were detected during this monitoring window.")
    else:
        lines.append(
            f"Detected **{len(commits)} relevant commit(s)** and **{len(pull_requests)} pull request(s) with activity** affecting **{len(all_files)} unique file(s)**."
        )
    lines.extend(
        [
            f"- Affected catalogued use cases: **{len(use_cases)}**",
            f"- Changed use-case IDs absent from current catalogue: **{len(absent_use_cases)}**",
            f"- Overall significance: **{severity}**",
            f"- Areas touched: {', '.join(areas) if areas else 'None'}",
            "",
            "## 2. Changes Detected",
            "",
        ]
    )

    if commits:
        lines.extend(["### Commits", ""])
        for commit in commits:
            lines.append(
                f"- `{commit['short']}` — **{commit['message']}** — {commit['author']} — {commit['time']} — {len(commit['files'])} file(s)"
            )
    else:
        lines.append("No commits were detected in the monitoring window.")

    if rewrite:
        lines.extend(
            [
                "",
                "### Default-branch history integrity event",
                "",
                f"- Previous successful head: `{rewrite['previous_head']}`",
                f"- Current head: `{rewrite['current_head']}`",
                f"- Event: `{rewrite['kind']}`",
                f"- Comparison base: `{rewrite['merge_base'] or 'none (unavailable or unrelated histories)'}`",
                f"- Current-state path differences captured: {len(rewrite['files'])}",
                "- **History integrity event:** YES",
                "- This is a **HIGH** integrity event. Review it before relying on the normal monitoring ledger.",
            ]
        )

    lines.append("")
    if pull_requests:
        lines.extend(["### Pull Requests", ""])
        for pull_request in pull_requests:
            state = "MERGED" if pull_request.get("merged_at") else pull_request["state"].upper()
            lines.append(
                f"- PR #{pull_request['number']} — **{pull_request['title']}** — {state} — {pull_request['author']} — reviews: {pull_request['reviews']}, review comments: {pull_request['review_comments']}, conversation comments: {pull_request['issue_comments']}"
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
                    "- **Observed change:** explicit use-case ID appears in changed repository evidence or PR metadata.",
                    f"- **Business impact:** {DOMAIN_BENEFITS.get(domain, 'Requires business-impact review')}.",
                    "- **Evidence impact:** review changed evidence before changing its evidence classification.",
                    "- **Delivery impact:** no status is changed automatically by this monitor.",
                    "- **Remaining gap:** verify E2E evidence before treating the use case as complete.",
                    "",
                ]
            )
    else:
        lines.append("No currently catalogued use cases were materially affected during this monitoring window.")

    if absent_use_cases:
        lines.extend(["", "### Changed identifiers absent from the current catalogue", ""])
        for uid in absent_use_cases:
            lines.append(
                f"- `{uid}` — changed evidence references this identifier, but it is absent from the post-change catalogue. Review whether it was removed, renamed, or introduced incorrectly."
            )

    lines.extend(["", "## 4. Implementation and Contractor Progress", ""])
    if contractor_changes:
        lines.append("Changes were detected under `contractors/80kDevelopers/`:")
        lines.extend(f"- `{path}`" for path in contractor_changes)
        lines.append("Review contractor provenance against implementation and E2E evidence before changing delivery status.")
    else:
        lines.append("No contractor-delivery files changed during this window.")

    lines.extend(["", "## 5. Governance and Evidence Changes", ""])
    if governance_changes:
        lines.extend(
            f"- `{path}` changed; verify execution instructions and evidence references remain consistent."
            for path in governance_changes
        )
    else:
        lines.append("No controlling governance or context files changed.")

    lines.extend(["", "## 6. Risks, Problems and Regressions", ""])
    if integrity:
        lines.extend(f"- **{level}** — {issue}" for level, issue in integrity)
    else:
        lines.append("No selected repository-integrity regressions were detected.")

    lines.extend(["", "## 7. Positive Progress", ""])
    if commits or pull_requests or rewrite:
        lines.append("- Repository activity occurred and has been captured in the monitoring ledger.")
        if use_cases:
            lines.append(f"- {len(use_cases)} current use case(s) received explicit changed evidence for review.")
        if contractor_changes:
            lines.append("- 80K Developers contractor-delivery evidence progressed.")
    else:
        lines.append("- Repository remained stable during this monitoring window.")

    lines.extend(["", "## 8. Recommended Next Actions", ""])
    priority = 1
    for level, issue in integrity:
        lines.append(f"{priority}. **{level}** — Repair or reconcile integrity issue: {issue}")
        priority += 1
    if use_cases:
        lines.append(
            f"{priority}. Review changed evidence for: {', '.join(use_cases)} and update statuses only if objective E2E evidence supports it."
        )
        priority += 1
    if contractor_changes:
        lines.append(
            f"{priority}. Reconcile contractor changes against the current use-case catalogue and implementation status."
        )
        priority += 1
    if priority == 1:
        lines.append("1. No immediate remediation required; continue scheduled monitoring.")

    lines.extend(
        [
            "",
            "## 9. Change Ledger",
            "",
            "| Time | Commit / PR | Change | Area | Impact |",
            "|---|---|---|---|---|",
        ]
    )
    for commit in commits:
        commit_paths = set()
        for file_entry in commit["files"]:
            if file_entry.get("filename"):
                commit_paths.add(file_entry["filename"])
            if file_entry.get("previous_filename"):
                commit_paths.add(file_entry["previous_filename"])
        area = ", ".join(sorted({area_for(path) for path in commit_paths})) or "Repository"
        lines.append(
            f"| {commit['time']} | `{commit['short']}` | {commit['message'].replace('|', '/')} | {area} | Review |"
        )
    for pull_request in pull_requests:
        area = ", ".join(sorted({area_for(path) for path in pull_request["files"]})) or "Repository"
        lines.append(
            f"| {pull_request['updated_at']} | PR #{pull_request['number']} | {pull_request['title'].replace('|', '/')} | {area} | Review |"
        )
    if rewrite:
        rewrite_area = ", ".join(
            sorted(
                {
                    area_for(path)
                    for file_entry in rewrite["files"]
                    for path in (file_entry.get("filename"), file_entry.get("previous_filename"))
                    if path
                }
            )
        ) or "Repository"
        lines.append(
            f"| {now.isoformat()} | History integrity | {rewrite['kind'].replace('_', ' ')} | {rewrite_area} | HIGH integrity review |"
        )
    if not commits and not pull_requests and not rewrite:
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
