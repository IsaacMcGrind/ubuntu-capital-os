# Gap and Risk Register

Status: `ANALYSIS_IN_PROGRESS`

| Risk ID | Risk | Severity | Evidence Status | Mitigation | Owner |
|---|---|---|---|---|---|
| RSK-001 | Binding vs non-binding investment semantics unresolved | CRITICAL | UNKNOWN | Keep first slice explicitly non-binding until legal evidence resolves OQ-003 | Product + Legal |
| RSK-002 | Settlement and custody operating model absent | CRITICAL | UNKNOWN | Block settlement implementation pending OQ-004 and OQ-005 | Finance + Operations |
| RSK-003 | Internal role and permission boundaries unverified | CRITICAL | INFERRED | Implement role matrix and negative-path tests before sensitive features | Security + Ops |
| RSK-004 | Audit evidence model may be conflated with telemetry | HIGH | INFERRED | Separate business audit schema from operational monitoring | Compliance + Platform |
| RSK-005 | External provider contracts unresolved | HIGH | UNKNOWN | Record provider decisions and error contracts before integration coding | Architecture + Procurement |
| RSK-006 | Readiness-decision authority and execution-control contract undefined (`OQ-016`) | CRITICAL | UNKNOWN | Keep `NO_GO` effective for execution-authorising scope until controlling governance identifies the authorised approver and durable decision contract; require exact `WP-AZ-*` scope, non-waivable conditions, owners/dates/evidence, expiry/review triggers, residual-risk record, and auditable decision evidence before any `GO` or `CONDITIONAL_GO` can authorise work | Project Owner + Programme Governance |
