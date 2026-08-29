#!/usr/bin/env python3
"""Provenance-safe impact analysis for Ubuntu Capital repository monitoring.

This version builds on repository_monitor_v2 but replaces the material-use-case
classifier so broad-reference thresholds are applied per attributed file and
metadata source, PR comment-only activity cannot replay stale PR evidence, full
commit messages are inspected, and history rewrites retain per-file attribution.
"""

from __future__ import annotations

import re

import repository_monitor as base
import repository_monitor_v2 as v2

ORIGINAL_COLLECT_PR_ACTIVITY = base.collect_pr_activity


def record_metadata_signals(
    item: dict,
    text: str,
    signal: str,
    *,
    always_direct: bool = False,
) -> set[str]:
    """Classify metadata IDs without letting broad metadata inflate impact counts."""
    ids = set(re.findall(base.USE_CASE_PATTERN, text or ""))
    if not ids:
        return set()

    if not always_direct and len(ids) > v2.BROAD_REFERENCE_THRESHOLD:
        v2.BROAD_REFERENCES.append(
            {
                "source": v2.source_label(item) + f" — broad {signal}",
                "files": [],
                "ids": sorted(ids),
            }
        )
        return set()

    for uid in sorted(ids):
        v2.add_direct_impact(uid, item, [], signal)
    return ids


def record_file_signals_per_file(item: dict, file_evidence: list[dict]) -> set[str]:
    """Apply broad-reference detection independently to each attributed file."""
    direct_ids: set[str] = set()
    for evidence in file_evidence:
        ids = set(evidence.get("ids", set()))
        paths = list(evidence.get("paths", []))
        if not ids:
            continue
        if len(ids) > v2.BROAD_REFERENCE_THRESHOLD:
            v2.BROAD_REFERENCES.append(
                {
                    "source": v2.source_label(item),
                    "files": sorted(path for path in paths if path),
                    "ids": sorted(ids),
                }
            )
            continue
        for uid in sorted(ids):
            v2.add_direct_impact(
                uid,
                item,
                paths,
                "changed path or diff line in attributed file",
            )
            direct_ids.add(uid)
    return direct_ids


def full_commit_message(item: dict) -> str:
    """Read the complete commit message so body-only UC IDs are not lost."""
    sha = item.get("sha")
    if not sha:
        return item.get("message") or ""
    try:
        return base.git("show", "-s", "--format=%B", sha).strip()
    except Exception:
        return item.get("message") or ""


def pr_structural_activity_in_window(number: int, since) -> dict:
    """Describe PR activity that materially changed during the monitoring window.

    GitHub advances PR `updated_at` for reviews and conversation comments. Those
    events must not replay an old title/body/full diff as new impact. We distinguish:
    - created: the PR itself is new, so title/body/full diff are in-window evidence;
    - merged: the PR entered the default branch, so its full diff is material now;
    - commits_only: only commits added in-window are material; historical PR metadata
      and earlier file changes are excluded;
    - none: review/comment-only or otherwise unverifiable PR activity.
    """
    detail = base.api(f"/repos/{base.REPO}/pulls/{number}")
    created_at = detail.get("created_at")
    merged_at = detail.get("merged_at")

    created = bool(created_at and base.parse_dt(created_at) >= since)
    merged = bool(merged_at and base.parse_dt(merged_at) >= since)

    recent_commit_shas: list[str] = []
    commits = base.paginate_list(f"/repos/{base.REPO}/pulls/{number}/commits")
    for commit in commits:
        commit_meta = commit.get("commit", {})
        timestamp = (
            commit_meta.get("committer", {}).get("date")
            or commit_meta.get("author", {}).get("date")
        )
        if timestamp and base.parse_dt(timestamp) >= since and commit.get("sha"):
            recent_commit_shas.append(commit["sha"])

    if created:
        mode = "created"
    elif merged:
        mode = "merged"
    elif recent_commit_shas:
        mode = "commits_only"
    else:
        mode = "none"

    return {
        "mode": mode,
        "recent_commit_shas": recent_commit_shas,
        "created": created,
        "merged": merged,
    }


def collect_pr_activity_with_window_provenance(since):
    """Annotate base PR activity with exact structural in-window provenance."""
    items = ORIGINAL_COLLECT_PR_ACTIVITY(since)
    for item in items:
        number = item.get("number")
        if not number:
            item["material_pr_activity"] = "none"
            item["material_pr_commit_shas"] = []
            continue
        try:
            activity = pr_structural_activity_in_window(number, since)
        except Exception as exc:
            # Evidence-first fallback: inability to prove structural PR activity
            # must not promote stale PR evidence to material impact.
            activity = {
                "mode": "none",
                "recent_commit_shas": [],
                "verification_error": type(exc).__name__,
            }
        item["material_pr_activity"] = activity.get("mode", "none")
        item["material_pr_commit_shas"] = activity.get("recent_commit_shas", [])
        if activity.get("verification_error"):
            item["material_pr_verification_error"] = activity["verification_error"]
    return items


def api_commit_evidence(sha: str) -> tuple[dict, list[dict]]:
    """Return full-message metadata and per-file changed evidence for one PR commit."""
    detail = base.api(f"/repos/{base.REPO}/commits/{sha}")
    commit_meta = detail.get("commit", {})
    message = commit_meta.get("message") or ""
    synthetic = {
        "sha": sha,
        "short": sha[:7],
        "message": message.splitlines()[0] if message else "PR commit",
        "files": [],
    }
    evidence: list[dict] = []
    for file_entry in detail.get("files", []):
        filename = file_entry.get("filename")
        previous = file_entry.get("previous_filename")
        paths = [path for path in (previous, filename) if path]
        ids = v2.ids_in_changed_lines(file_entry.get("patch") or "")
        for path in paths:
            ids.update(re.findall(base.USE_CASE_PATTERN, path))
        evidence.append({"paths": paths, "ids": ids})
    return {"item": synthetic, "message": message}, evidence


def rewrite_file_evidence(rewrite: dict) -> list[dict]:
    """Derive UC evidence per rewritten path instead of sharing aggregate IDs."""
    previous = rewrite.get("previous_head")
    current = rewrite.get("current_head")
    if not previous or not current:
        return []

    evidence: list[dict] = []
    for file_entry in rewrite.get("files", []):
        filename = file_entry.get("filename")
        previous_filename = file_entry.get("previous_filename")
        paths = [path for path in (previous_filename, filename) if path]
        if not paths:
            continue
        try:
            patch = base.git(
                "diff",
                "--format=",
                "--unified=0",
                "--no-ext-diff",
                previous,
                current,
                "--",
                *paths,
            )
        except Exception:
            patch = ""
        ids = v2.ids_in_changed_lines(patch)
        for path in paths:
            ids.update(re.findall(base.USE_CASE_PATTERN, path))
        evidence.append({"paths": paths, "ids": ids})
    return evidence


def material_use_case_changes(catalogue: dict[str, str], commits, pull_requests, rewrite=None):
    """Return materially impacted use cases using provenance-safe attribution."""
    v2.IMPACT_RECORDS.clear()
    v2.BROAD_REFERENCES.clear()
    v2.ABSENT_DIRECT_IDS.clear()

    all_direct_ids: set[str] = set()

    for item in commits:
        message = full_commit_message(item)
        observed_metadata_ids = set(re.findall(base.USE_CASE_PATTERN, message))
        metadata_ids = record_metadata_signals(item, message, "commit metadata")
        all_direct_ids.update(metadata_ids)

        file_evidence = v2.commit_file_evidence(item)
        observed_file_ids = {
            uid for evidence in file_evidence for uid in set(evidence.get("ids", set()))
        }
        direct_file_ids = record_file_signals_per_file(item, file_evidence)
        all_direct_ids.update(direct_file_ids)

        # Never promote unattributed residual commit IDs. The hardened base collector
        # may retain IDs from a broad source that was intentionally suppressed here.
        residual = set(item.get("use_case_ids", [])) - observed_metadata_ids - observed_file_ids
        if residual:
            v2.BROAD_REFERENCES.append(
                {
                    "source": v2.source_label(item) + " — unattributed commit references",
                    "files": [],
                    "ids": sorted(residual),
                }
            )

    for item in pull_requests:
        mode = item.get("material_pr_activity", "none")

        if mode == "none":
            residual = set(item.get("use_case_ids", []))
            if residual:
                v2.BROAD_REFERENCES.append(
                    {
                        "source": v2.source_label(item) + " — comment/review-only window activity",
                        "files": [],
                        "ids": sorted(residual),
                    }
                )
            continue

        if mode in {"created", "merged"}:
            # Creation makes the complete proposed change new evidence; merge makes
            # the complete PR materially enter the default branch in this window.
            body, file_evidence = v2.pr_details_and_file_evidence(item)
            title_ids = record_metadata_signals(
                item,
                item.get("title") or "",
                "PR title metadata",
                always_direct=True,
            )
            body_ids = record_metadata_signals(item, body, "PR body metadata")
            metadata_ids = title_ids | body_ids
            all_direct_ids.update(metadata_ids)

            direct_file_ids = record_file_signals_per_file(item, file_evidence)
            all_direct_ids.update(direct_file_ids)

            residual = set(item.get("use_case_ids", [])) - metadata_ids - direct_file_ids
            if residual:
                v2.BROAD_REFERENCES.append(
                    {
                        "source": v2.source_label(item) + " — unattributed PR references",
                        "files": [],
                        "ids": sorted(residual),
                    }
                )
            continue

        # For an existing open PR with only new commits in-window, inspect exactly
        # those commits. Do not replay the PR's historical title/body/full file diff.
        if mode == "commits_only":
            for sha in item.get("material_pr_commit_shas", []):
                commit_info, file_evidence = api_commit_evidence(sha)
                commit_item = commit_info["item"]
                message = commit_info["message"]
                metadata_ids = record_metadata_signals(
                    commit_item,
                    message,
                    "in-window PR commit metadata",
                )
                all_direct_ids.update(metadata_ids)
                direct_file_ids = record_file_signals_per_file(commit_item, file_evidence)
                all_direct_ids.update(direct_file_ids)
            continue

    if rewrite:
        synthetic = {
            "number": "history",
            "title": f"default-branch {rewrite.get('kind', 'rewrite')}",
            "files": rewrite.get("files", []),
        }
        direct_rewrite_ids = record_file_signals_per_file(
            synthetic, rewrite_file_evidence(rewrite)
        )
        all_direct_ids.update(direct_rewrite_ids)

        residual_rewrite = set(rewrite.get("use_case_ids", [])) - direct_rewrite_ids
        if residual_rewrite:
            v2.BROAD_REFERENCES.append(
                {
                    "source": f"default-branch {rewrite.get('kind', 'rewrite')} — unattributed state references",
                    "files": [],
                    "ids": sorted(residual_rewrite),
                }
            )

    known = sorted(uid for uid in all_direct_ids if uid in catalogue)
    absent = sorted(uid for uid in all_direct_ids if uid not in catalogue)
    v2.ABSENT_DIRECT_IDS.extend(absent)
    return known, absent


def main() -> None:
    # V3 owns provenance qualification; V2 still owns rendering and matrix enrichment.
    base.collect_pr_activity = collect_pr_activity_with_window_provenance
    v2.material_use_case_changes = material_use_case_changes
    v2.main()


if __name__ == "__main__":
    main()
