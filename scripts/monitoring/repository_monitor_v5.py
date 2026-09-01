#!/usr/bin/env python3
"""Provenance-aware significance layer for Ubuntu Capital repository monitoring.

V5 keeps V4's checkpoint-aware use-case attribution but ensures PR discussion-only
activity cannot inherit the significance of an old merged PR. Structural PR
activity (created, merged, metadata/head delta) remains eligible for significance;
comment/review-only activity remains visible in the report without inflating the
overall assessment.
"""

from __future__ import annotations

import repository_monitor as base
import repository_monitor_v4 as v4


def material_prs(pull_requests):
    """Return PRs with structural activity established by V4 provenance."""
    result = []
    for pr in pull_requests:
        mode = pr.get("material_pr_activity")
        # Backward compatibility: when provenance metadata is unavailable because
        # an older collector is used, preserve the base monitor's behaviour.
        if mode is None:
            result.append(pr)
        elif mode in {"created", "merged", "checkpoint_delta"}:
            result.append(pr)
    return result


def provenance_significance(commits, pull_requests, integrity, known_use_cases, absent_use_cases) -> str:
    if any(level == "HIGH" for level, _ in integrity):
        return "HIGH"

    structural_prs = material_prs(pull_requests)
    if known_use_cases or absent_use_cases or any(pr.get("merged_at") for pr in structural_prs):
        return "HIGH"

    unique_files = {
        file_entry["filename"]
        for commit in commits
        for file_entry in commit["files"]
        if file_entry.get("filename")
    }
    if structural_prs or len(unique_files) >= 5:
        return "MEDIUM"
    return "LOW"


def main() -> None:
    base.significance = provenance_significance
    v4.main()


if __name__ == "__main__":
    main()
