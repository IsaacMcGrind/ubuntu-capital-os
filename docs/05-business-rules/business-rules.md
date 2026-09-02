# Business Rules Register

Status: `ANALYSIS_IN_PROGRESS`

| Rule ID | Rule | Evidence Status | Related Use Cases | Notes |
|---|---|---|---|---|
| BR-001 | Only authenticated users may access private investor routes. | INFERRED | UC-IAM-001, UC-OPP-001 | Must be verified with backend/session evidence. |
| BR-002 | Opportunity visibility is controlled by investor access status. | INFERRED | UC-OPP-001 to UC-OPP-003 | Requires policy and role evidence. |
| BR-003 | Restricted due-diligence content requires explicit NDA/access grant. | INFERRED | UC-DD-001, UC-DD-002 | Trigger confirmed; lifecycle unverified. |
| BR-004 | First implementation slice treats investor submission as a non-binding EOI and does not create a binding commitment or funding obligation. | CONFIRMED | UC-INV-001, UC-INV-002 | Controlled by plan.md Phase 6; legal and product approval remains required before any binding flow. |
| BR-005 | Duplicate EOI submissions must be prevented or safely deduplicated. | INFERRED | UC-INV-001, UC-INV-002 | Requires idempotency and concurrency tests. |
| BR-006 | Sensitive actions must emit structured business audit events. | INFERRED | UC-AUD-001 and sensitive UC-* | Distinct from operational telemetry. |
| BR-007 | Settlement actions require immutable references and reconciliation controls. | UNKNOWN | UC-SET-001 to UC-SET-003 | Blocked by OQ-004. |
| BR-008 | Role changes and privileged overrides require least-privilege governance. | INFERRED | UC-ADMIN-003, UC-OPS-002 | Maker-checker requirement unresolved. |
| BR-009 | Investor-facing documents require authorization and retrieval audit evidence. | INFERRED | UC-DOC-001 | Storage and retention design pending. |
| BR-010 | Non-confirmed requirements must include uncertainty and validation method. | CONFIRMED | All UC-* | Required by AGENT.md. |
