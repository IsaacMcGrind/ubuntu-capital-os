#!/usr/bin/env python3
"""Evidence-grounded reporting layer for the Ubuntu Capital repository monitor.

The base monitor remains responsible for repository/activity collection and integrity
checks. This layer narrows use-case impact to material evidence instead of treating
any textual UC-ID mention as a delivery impact, then replaces Section 3 with a
change-specific analysis grounded in changed files, commit/PR metadata and the
current implementation coverage gap matrix.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import repository_monitor as base

BROAD_REFERENCE_THRESHOLD = 8
IMPACT_RECORDS: dict[str, dict] = {}
BROAD_REFERENCES: list[dict] = []
ABSENT_DIRECT_IDS: list[str] = []


def changed_lines(patch: str) -> list[str]:
    return [
        line[1:]
        for line in (patch or "").splitlines()
        if (line.startswith("+") or line.startswith("-"))
        and not line.startswith("+++")
        and not line.startswith("---")
    ]


def normalize_paths(item: dict) -> list[str]:
    paths: set[str] = set()
    for value in item.get("files", []):
        if isinstance(value, dict):
            if value.get("filename"):
                paths.add(value["filename"])
            if value.get("previous_filename"):
                paths.add(value["previous_filename"])
        elif value:
            paths.add(value)
    return sorted(paths)


def source_label(item: dict) -> str:
    if item.get("short"):
        return f"commit `{item['short']}` — {item.get('message', '').strip()}"
    return f"PR #{item.get('number')} — {item.get('title', '').strip()}"


def classify_change_type(path: str) -> str:
    lower = path.lower()
    if any(token in lower for token in ("/test/", "/tests/", ".spec.", ".test.", "e2e")):
        return "TEST_EVIDENCE"
    if lower.startswith(("src/", "app/", "api/", "server/", "backend/", "frontend/", "infra/")):
        return "IMPLEMENTATION"
    if path.startswith("contractors/80kDevelopers/") or path.endswith("implementation-coverage-gap-matrix.md"):
        return "DELIVERY_EVIDENCE"
    if "architecture" in lower or path.startswith("docs/07-state-models/") or path.startswith("docs/08-integrations/"):
        return "ARCHITECTURE"
    if path.startswith("docs/04-use-cases/") or path.startswith("docs/05-business-rules/") or path.startswith("docs/06-journeys/"):
        return "REQUIREMENT"
    if path in {"AGENT.md", "plan.md"} or path.startswith("docs/00-context/") or path.startswith("docs/10-traceability/"):
        return "GOVERNANCE_EVIDENCE"
    if path.startswith("docs/") or path.endswith(".md"):
        return "DOCUMENTATION"
    if path.startswith(("data/", "schemas/")):
        return "STRUCTURED_EVIDENCE"
    return "REPOSITORY_CHANGE"


def load_delivery_matrix() -> dict[str, dict[str, str]]:
    path = Path(base.WORKSPACE) / "docs/09-delivery/implementation-coverage-gap-matrix.md"
    if not path.exists():
        return {}
    matrix: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| UC-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        uid, status, evidence, gap, next_gate = cells[:5]
        matrix[uid] = {
            "status": status,
            "evidence": evidence,
            "gap": gap,
            "next_gate": next_gate,
        }
    return matrix


def ensure_record(uid: str) -> dict:
    return IMPACT_RECORDS.setdefault(
        uid,
        {
            "sources": set(),
            "files": set(),
            "change_types": set(),
            "signals": set(),
        },
    )


def add_direct_impact(uid: str, item: dict, paths: list[str], signal: str) -> None:
    record = ensure_record(uid)
    record["sources"].add(source_label(item))
    record["files"].update(paths)
    record["signals"].add(signal)
    record["change_types"].update(classify_change_type(path) for path in paths)
    if not paths:
        record["change_types"].add("METADATA")


def material_use_case_changes(catalogue: dict[str, str], commits, pull_requests, rewrite=None):
    """Return only materially implicated use cases, not broad cross-reference mentions."""
    IMPACT_RECORDS.clear()
    BROAD_REFERENCES.clear()
    ABSENT_DIRECT_IDS.clear()

    all_direct_ids: set[str] = set()
    for item in commits + pull_requests:
        paths = normalize_paths(item)
        metadata = "\n".join(
            value or ""
            for value in (item.get("message"), item.get("title"), item.get("body"))
        )
        metadata_ids = set(re.findall(base.USE_CASE_PATTERN, metadata))
        path_ids = {
            uid
            for path in paths
            for uid in re.findall(base.USE_CASE_PATTERN, path)
        }
        line_ids = set(re.findall(base.USE_CASE_PATTERN, "\n".join(changed_lines(item.get("patch", "")))))

        direct_ids = metadata_ids | path_ids
        if len(line_ids) <= BROAD_REFERENCE_THRESHOLD:
            direct_ids |= line_ids
        elif line_ids:
            BROAD_REFERENCES.append(
                {
                    "source": source_label(item),
                    "files": paths,
                    "ids": sorted(line_ids),
                }
            )

        for uid in sorted(direct_ids):
            signal_parts = []
            if uid in metadata_ids:
                signal_parts.append("commit/PR metadata")
            if uid in path_ids:
                signal_parts.append("dedicated changed path")
            if uid in line_ids and len(line_ids) <= BROAD_REFERENCE_THRESHOLD:
                signal_parts.append("changed diff line")
            add_direct_impact(uid, item, paths, ", ".join(signal_parts) or "direct change evidence")
            all_direct_ids.add(uid)

    if rewrite:
        rewrite_ids = set(rewrite.get("use_case_ids", []))
        if 0 < len(rewrite_ids) <= BROAD_REFERENCE_THRESHOLD:
            synthetic = {
                "number": "history",
                "title": f"default-branch {rewrite.get('kind', 'rewrite')}",
                "files": rewrite.get("files", []),
            }
            paths = normalize_paths(synthetic)
            for uid in rewrite_ids:
                add_direct_impact(uid, synthetic, paths, "default-branch state difference")
                all_direct_ids.add(uid)
        elif rewrite_ids:
            BROAD_REFERENCES.append(
                {
                    "source": f"default-branch {rewrite.get('kind', 'rewrite')}",
                    "files": normalize_paths({"files": rewrite.get("files", [])}),
                    "ids": sorted(rewrite_ids),
                }
            )

    known = sorted(uid for uid in all_direct_ids if uid in catalogue)
    absent = sorted(uid for uid in all_direct_ids if uid not in catalogue)
    ABSENT_DIRECT_IDS.extend(absent)
    return known, absent


def change_meaning(change_types: set[str]) -> str:
    ordered = [
        ("IMPLEMENTATION", "implementation code changed"),
        ("TEST_EVIDENCE", "test or E2E evidence changed"),
        ("DELIVERY_EVIDENCE", "delivery/implementation evidence changed"),
        ("ARCHITECTURE", "architecture or integration design changed"),
        ("REQUIREMENT", "use-case, journey or business-rule definition changed"),
        ("GOVERNANCE_EVIDENCE", "governance or traceability evidence changed"),
        ("STRUCTURED_EVIDENCE", "structured evidence/schema changed"),
        ("DOCUMENTATION", "supporting documentation changed"),
        ("METADATA", "commit or PR metadata directly names the use case"),
        ("REPOSITORY_CHANGE", "repository evidence changed"),
    ]
    labels = [label for key, label in ordered if key in change_types]
    return "; ".join(labels) if labels else "direct repository evidence changed"


def delivery_implication(change_types: set[str], status: str) -> str:
    current = status or "not recorded in the implementation coverage matrix"
    if "IMPLEMENTATION" in change_types or "TEST_EVIDENCE" in change_types:
        return (
            f"Potential delivery progression from the current `{current}` position, but the monitor does not promote status automatically; "
            "the changed implementation/test evidence must satisfy the documented evidence gate first."
        )
    if "DELIVERY_EVIDENCE" in change_types:
        return (
            f"The evidence used to assess delivery changed while the current recorded position is `{current}`. "
            "Reconcile the matrix/status row against the underlying implementation before changing delivery state."
        )
    if "ARCHITECTURE" in change_types:
        return (
            f"Design clarity improved or changed, but this is not implementation completion. Current delivery position remains `{current}` unless implementation/E2E evidence also changed."
        )
    if "REQUIREMENT" in change_types:
        return (
            f"The expected behaviour or control definition changed. Current delivery position is `{current}`; implementation and tests should be checked for alignment with the revised requirement."
        )
    return f"No implementation progression is established by this evidence alone. Current recorded delivery position: `{current}`."


def business_consequence(uid: str, change_types: set[str]) -> str:
    domain = uid.split("-")[1]
    benefit = base.DOMAIN_BENEFITS.get(domain, "Business outcome requires review")
    if "IMPLEMENTATION" in change_types:
        suffix = "The change may alter executable platform behaviour and therefore deserves functional and regression validation."
    elif "ARCHITECTURE" in change_types:
        suffix = "The immediate effect is design/decision clarity rather than live investor behaviour."
    elif "REQUIREMENT" in change_types:
        suffix = "The primary risk is requirements-to-implementation drift if downstream delivery is not reconciled."
    elif "DELIVERY_EVIDENCE" in change_types:
        suffix = "The immediate value is more accurate delivery visibility and prioritisation, not proof of new production capability."
    else:
        suffix = "The change improves or alters project evidence; production behaviour is not assumed to have changed."
    return f"{benefit}. {suffix}"


def render_use_case_section(catalogue: dict[str, str]) -> str:
    matrix = load_delivery_matrix()
    lines = ["## 3. Use-Case Impact", ""]

    material_ids = sorted(uid for uid in IMPACT_RECORDS if uid in catalogue)
    if not material_ids:
        lines.append("No use case had direct material change evidence during this monitoring window.")
    else:
        lines.append(
            f"**Materially impacted use cases: {len(material_ids)}.** A use case appears here only when the change directly names it in commit/PR metadata, a dedicated path, or a bounded changed diff. Broad documents that merely enumerate many use cases are not treated as individual delivery impacts."
        )
        lines.append("")
        for uid in material_ids:
            record = IMPACT_RECORDS[uid]
            delivery = matrix.get(uid, {})
            paths = sorted(record["files"])
            sources = sorted(record["sources"])
            signals = sorted(record["signals"])
            types = set(record["change_types"])
            lines.extend(
                [
                    f"### {uid} — {catalogue[uid]}",
                    f"- **Actual change:** {change_meaning(types)}.",
                    f"- **Why this use case is included:** {'; '.join(signals)}.",
                    f"- **Change source:** {'; '.join(sources)}.",
                    f"- **Changed evidence:** {', '.join(f'`{path}`' for path in paths) if paths else 'PR/commit metadata only'}.",
                    f"- **Business consequence:** {business_consequence(uid, types)}",
                    f"- **Current delivery position:** `{delivery.get('status', 'UNKNOWN')}`.",
                    f"- **Delivery impact:** {delivery_implication(types, delivery.get('status', ''))}",
                    f"- **Known gap:** {delivery.get('gap', 'No use-case-specific gap was available in the implementation coverage matrix.')} ",
                    f"- **Next evidence gate:** {delivery.get('next_gate', 'Perform targeted implementation/E2E verification before changing status.')}",
                    "",
                ]
            )

    if BROAD_REFERENCES:
        lines.extend(["### Broad cross-reference changes (not counted as individual delivery impact)", ""])
        for ref in BROAD_REFERENCES:
            ids = ref["ids"]
            preview = ", ".join(ids[:6]) + (f" … +{len(ids) - 6} more" if len(ids) > 6 else "")
            files = ", ".join(f"`{path}`" for path in ref["files"][:5]) or "metadata/state comparison"
            lines.append(
                f"- **{ref['source']}** references **{len(ids)} use-case IDs** ({preview}) across {files}. This is treated as catalogue/architecture cross-reference coverage, not proof that all referenced use cases changed in delivery."
            )
        lines.append("")

    if ABSENT_DIRECT_IDS:
        lines.extend(["### Directly changed identifiers absent from the current catalogue", ""])
        for uid in ABSENT_DIRECT_IDS:
            lines.append(f"- `{uid}` — direct change evidence references this identifier, but it is absent from the current catalogue; reconcile removal, rename, or erroneous introduction.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def replace_section_three(report: str, catalogue: dict[str, str]) -> str:
    start = report.find("## 3. Use-Case Impact")
    end = report.find("## 4. Implementation and Contractor Progress")
    if start == -1 or end == -1 or end <= start:
        raise RuntimeError("Could not locate report Section 3 boundaries for impact enrichment.")
    return report[:start] + render_use_case_section(catalogue) + "\n" + report[end:]


def main() -> None:
    base.classify_use_case_changes = material_use_case_changes
    base.main()

    catalogue, _, _ = base.load_catalogue()
    report = base.REPORT_PATH.read_text(encoding="utf-8")
    base.REPORT_PATH.write_text(replace_section_three(report, catalogue), encoding="utf-8")


if __name__ == "__main__":
    main()
