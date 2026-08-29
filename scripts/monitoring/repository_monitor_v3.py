#!/usr/bin/env python3
"""Provenance-safe impact analysis for Ubuntu Capital repository monitoring.

This version builds on repository_monitor_v2 but replaces the material-use-case
classifier so broad-reference thresholds are applied per attributed file and
metadata source, PR comment-only IDs are never promoted to material impact, and
history rewrites retain per-file attribution.
"""

from __future__ import annotations

import re

import repository_monitor as base
import repository_monitor_v2 as v2


def record_metadata_signals(
    item: dict,
    text: str,
    signal: str,
    *,
    always_direct: bool = False,
) -> set[str]:
    """Classify metadata IDs without letting broad metadata inflate impact counts.

    Short, focused metadata is useful direct evidence. A PR body or commit message
    that enumerates many use cases is instead treated as cross-reference coverage,
    matching the same safeguard applied to broad changed files.
    """
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
        metadata_ids = record_metadata_signals(
            item,
            item.get("message") or "",
            "commit metadata",
        )
        all_direct_ids.update(metadata_ids)

        direct_file_ids = record_file_signals_per_file(item, v2.commit_file_evidence(item))
        all_direct_ids.update(direct_file_ids)

        # The base collector scans the complete pre-truncation patch. Preserve only
        # residual commit IDs because commit provenance is limited to message/patch/path;
        # do not assign unrelated paths when exact attribution is unavailable.
        residual = set(item.get("use_case_ids", [])) - metadata_ids - direct_file_ids
        if residual:
            if len(residual) <= v2.BROAD_REFERENCE_THRESHOLD:
                for uid in sorted(residual):
                    v2.add_direct_impact(
                        uid,
                        item,
                        [],
                        "complete pre-truncation commit patch evidence; exact path unavailable",
                    )
                    all_direct_ids.add(uid)
            else:
                v2.BROAD_REFERENCES.append(
                    {
                        "source": v2.source_label(item) + " — broad unattributed commit references",
                        "files": [],
                        "ids": sorted(residual),
                    }
                )

    for item in pull_requests:
        body, file_evidence = v2.pr_details_and_file_evidence(item)

        # A focused PR title is always intentional direct metadata. The body is
        # thresholded independently because templates/mapping descriptions often
        # enumerate many use cases without materially changing each one.
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
        # Without provenance, these are reference-only evidence, not material impact.
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
            # Aggregate rewrite IDs without a file-level source are kept visible for
            # human reconciliation but are not promoted to material delivery impact.
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
    # v2 handles rendering and delivery-matrix enrichment; this version replaces only
    # the classifier used by v2.main() before the base monitor runs.
    v2.material_use_case_changes = material_use_case_changes
    v2.main()


if __name__ == "__main__":
    main()
