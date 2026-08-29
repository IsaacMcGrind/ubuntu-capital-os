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


def pr_has_structural_activity_in_window(number: int, since) -> tuple[bool, list[str]]:
    """Return whether the PR itself changed in-window, excluding comment-only updates.

    GitHub's PR `updated_at` advances for reviews and conversation comments. Those
    updates must not cause an old title/body/fileset to be reclassified as fresh
    material evidence. We therefore require an in-window create/merge event or an
    in-window PR commit before PR metadata/file evidence is eligible for impact.
    """
    detail = base.api(f"/repos/{base.REPO}/pulls/{number}")
    reasons: list[str] = []

    created_at = detail.get("created_at")
    if created_at and base.parse_dt(created_at) >= since:
        reasons.append("PR created in monitoring window")

    merged_at = detail.get("merged_at")
    if merged_at and base.parse_dt(merged_at) >= since:
        reasons.append("PR merged in monitoring window")

    commits = base.paginate_list(f"/repos/{base.REPO}/pulls/{number}/commits")
    for commit in commits:
        commit_meta = commit.get("commit", {})
        timestamp = (
            commit_meta.get("committer", {}).get("date")
            or commit_meta.get("author", {}).get("date")
        )
        if timestamp and base.parse_dt(timestamp) >= since:
            reasons.append("PR commit recorded in monitoring window")
            break

    return bool(reasons), reasons


def collect_pr_activity_with_window_provenance(since):
    """Annotate base PR activity with whether material PR evidence changed in-window."""
    items = ORIGINAL_COLLECT_PR_ACTIVITY(since)
    for item in items:
        number = item.get("number")
        if not number:
            item["material_pr_activity"] = False
            item["material_pr_activity_reasons"] = []
            continue
        try:
            material, reasons = pr_has_structural_activity_in_window(number, since)
        except Exception as exc:
            # Evidence-first fallback: an inability to prove structural PR activity
            # must not promote stale PR evidence to material impact.
            material = False
            reasons = [f"structural PR activity could not be verified: {type(exc).__name__}"]
        item["material_pr_activity"] = material
        item["material_pr_activity_reasons"] = reasons
    return items


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
        metadata_ids = record_metadata_signals(
            item,
            message,
            "commit metadata",
        )
        all_direct_ids.update(metadata_ids)

        file_evidence = v2.commit_file_evidence(item)
        observed_file_ids = {
            uid for evidence in file_evidence for uid in set(evidence.get("ids", set()))
        }
        direct_file_ids = record_file_signals_per_file(item, file_evidence)
        all_direct_ids.update(direct_file_ids)

        # Never promote unattributed residual commit IDs. The hardened base collector
        # may retain IDs from a broad source that was intentionally suppressed here.
        # Per-file patches are re-read in full above, and the complete commit message
        # is inspected separately, so any remaining IDs lack safe provenance.
        residual = (
            set(item.get("use_case_ids", []))
            - observed_metadata_ids
            - observed_file_ids
        )
        if residual:
            v2.BROAD_REFERENCES.append(
                {
                    "source": v2.source_label(item) + " — unattributed commit references",
                    "files": [],
                    "ids": sorted(residual),
                }
            )

    for item in pull_requests:
        if not item.get("material_pr_activity", False):
            # The PR was returned because something such as a review/comment changed
            # its updated_at. Do not replay historical title/body/file evidence.
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

        body, file_evidence = v2.pr_details_and_file_evidence(item)

        # A focused PR title is an intentional direct label only when the PR itself
        # had structural in-window activity. The body is thresholded independently.
        title_ids = record_metadata_signals(
            item,
            item.get("title") or "",
            "PR title metadata",
            always_direct=True,
        )
        body_ids = record_metadata_signals(
            item,
            body,
            "PR body metadata",
        )
        metadata_ids = title_ids | body_ids
        all_direct_ids.update(metadata_ids)

        direct_file_ids = record_file_signals_per_file(item, file_evidence)
        all_direct_ids.update(direct_file_ids)

        # Do NOT promote residual PR collector IDs. The base collector also scans
        # review/conversation comments and may see unchanged-context identifiers.
        residual = set(item.get("use_case_ids", [])) - metadata_ids - direct_file_ids
        if residual:
            v2.BROAD_REFERENCES.append(
                {
                    "source": v2.source_label(item) + " — unattributed PR references",
                    "files": [],
                    "ids": sorted(residual),
                }
            )

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
