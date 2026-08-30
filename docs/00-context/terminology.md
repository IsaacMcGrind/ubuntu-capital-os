# Terminology

Status: `ANALYSIS_IN_PROGRESS`

This glossary separates observed reference terms from Ubuntu Capital reconstruction terminology.

| Term ID | Term | Definition | Evidence Status | Source |
|---|---|---|---|---|
| TERM-001 | Prospective investor | Visitor evaluating whether to register. | CONFIRMED | SRC-001 |
| TERM-002 | Registered investor | Authenticated user with private-portal access intent. | INFERRED | SRC-003, SRC-004 |
| TERM-003 | Eligible investor | Investor passing required compliance and suitability checks. | INFERRED | SRC-004 |
| TERM-004 | Opportunity | Investable item presented in discovery cards/detail views. | CONFIRMED | SRC-001 |
| TERM-005 | Due-diligence material | Restricted documents/content behind NDA or access control. | INFERRED | SRC-001, SRC-004 |
| TERM-006 | Expression of interest (EOI) | Non-binding statement of investor intent used in first slice. | INFERRED | plan.md |
| TERM-007 | Commitment | Binding or semi-binding investment instruction; legal effect unresolved. | UNKNOWN | OQ-003 |
| TERM-008 | Pending investment | Investment-intent state awaiting completion/decision. | CONFIRMED for navigation, lifecycle INFERRED | SRC-001, SRC-004 |
| TERM-009 | Holding | Post-settlement owned position shown in portfolio views. | CONFIRMED for navigation, ownership semantics UNKNOWN | SRC-001, OQ-005 |
| TERM-010 | Audit event | Immutable business event used for compliance and investigations. | INFERRED | SRC-004 |
| TERM-011 | Operational telemetry | Runtime diagnostics/metrics/logs for platform operations. | CONFIRMED as architecture target, implementation UNKNOWN | docs/09-delivery/foundation-slice-a-governance-reconciliation.md |

## Notes

1. Terms marked `INFERRED` or `UNKNOWN` must not be treated as legal or implementation facts without additional evidence.
2. Use `Expression of interest` wording in first-slice artefacts until OQ-003 resolves binding semantics.
