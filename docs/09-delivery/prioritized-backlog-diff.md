# Prioritized Backlog Diff (Matrix Translation)

Status: `ANALYSIS_IN_PROGRESS`

This pass translates the historical, partial snapshot labels in `docs/09-delivery/implementation-coverage-gap-matrix.md` into backlog-ready work proposals. The source snapshot is unpinned, so its labels are planning inputs only—not current implementation statuses. Acceptance checks remain proposed future evidence gates and must be reconciled against an authorised revision-pinned inspection before execution or status promotion.

Tracker-ready payloads generated from this diff:

- `docs/09-delivery/backlog.json`
- `data/backlog.json`

Priority order for this pass:

1. Critical domains first: IAM, ONB, INV, SET, ADMIN, AUD, INT
2. Remaining domains next: DD, OPP, PORT, DOC, PROFILE, NOTIFY, OPS, REPORT, PUB, NEWS, EVENT, REF

Legend:

- `ADD`: New backlog item must be created.
- `EXPAND`: Existing UI/prototype work must be expanded into full vertical implementation.
- `SEQUENCE`: Dependency/order adjustment required.

## Critical Domain Backlog Diff

| Priority | Use Case ID | Historical Snapshot Gap Label | Backlog Diff | Backlog Item ID | Concrete Acceptance Checks |
|---|---|---|---|---|---|
| P0 | UC-IAM-001 | IN_DEVELOPMENT | EXPAND | BL-IAM-001 | Successful login creates server session; invalid credentials rejected with audit event; protected routes deny unauthenticated requests. |
| P0 | UC-IAM-002 | IN_DEVELOPMENT | ADD | BL-IAM-002 | Password reset token issued, expires, and is single-use; reset email delivery is logged; invalid/expired token path covered by tests. |
| P0 | UC-IAM-003 | READY_FOR_DEVELOPMENT | ADD | BL-IAM-003 | Explicit logout invalidates session server-side; idle/absolute timeout enforced; timed-out session redirected and audited. |
| P0 | UC-ONB-001 | IN_DEVELOPMENT | EXPAND | BL-ONB-001 | Signup persists investor account; duplicate email blocked; registration emits auditable account-created event. |
| P0 | UC-ONB-002 | IN_DEVELOPMENT | EXPAND | BL-ONB-002 | Onboarding step data persists and resumes; required fields validated per step; submit transitions investor to review state. |
| P0 | UC-ONB-003 | IN_DEVELOPMENT | ADD | BL-ONB-003 | KYC/AML decision states stored (`approved`, `pending`, `rejected`); provider failure/retry path handled; decision changes are audited. |
| P0 | UC-INV-001 | IN_DEVELOPMENT | EXPAND | BL-INV-001 | Express-interest endpoint enforces eligibility and opportunity status; duplicate submissions are idempotent; non-binding vs binding state explicit. |
| P0 | UC-INV-002 | IN_DEVELOPMENT | EXPAND | BL-INV-002 | Pending commitment lifecycle transitions are persisted; operator decision path captured with reason codes; state transition tests pass. |
| P0 | UC-INV-003 | READY_FOR_DEVELOPMENT | ADD | BL-INV-003 | Withdrawal window/policy enforced; unauthorized cancellation blocked; cancellation action recorded in audit/event history. |
| P0 | UC-SET-001 | READY_FOR_DEVELOPMENT | ADD | BL-SET-001 | Funding instructions generated only for accepted commitments; instructions are immutable/versioned; delivery event captured. |
| P0 | UC-SET-002 | READY_FOR_DEVELOPMENT | ADD | BL-SET-002 | Incoming funds matched to commitment references; unmatched/partial funds flagged; reconciliation reports include resolved/unresolved totals. |
| P0 | UC-SET-003 | READY_FOR_DEVELOPMENT | ADD | BL-SET-003 | Settlement exception queue supports assign/escalate/resolve; maker-checker required for manual overrides; exception SLA metrics logged. |
| P0 | UC-ADMIN-001 | READY_FOR_DEVELOPMENT | ADD | BL-ADMIN-001 | Admin can create draft opportunity and publish only after compliance approval; publish event appears in audit feed; investors see published deal only after status transition. |
| P0 | UC-ADMIN-002 | READY_FOR_DEVELOPMENT | ADD | BL-ADMIN-002 | Admin can pause/close/archive opportunities with reason; closed opportunities block new commitments; lifecycle actions are audit-logged. |
| P0 | UC-ADMIN-003 | READY_FOR_DEVELOPMENT | ADD | BL-ADMIN-003 | Role assignment enforces least privilege; scoped data access verified by negative tests; permission changes produce immutable audit records. |
| P0 | UC-ADMIN-004 | READY_FOR_DEVELOPMENT | ADD | BL-ADMIN-004 | Reference data/content edits require authorized role; changes are versioned; dependent UI reflects updates without manual code edits. |
| P0 | UC-AUD-001 | READY_FOR_DEVELOPMENT | ADD | BL-AUD-001 | Sensitive actions emit structured audit events with actor/time/resource/outcome; audit records are queryable; tamper attempt detection path defined. |
| P0 | UC-AUD-002 | READY_FOR_DEVELOPMENT | ADD | BL-AUD-002 | Compliance/security investigation case can be opened and linked to events; evidence chain is preserved; investigation status transitions are tracked. |
| P0 | UC-INT-001 | READY_FOR_DEVELOPMENT | ADD | BL-INT-001 | Identity/KYC provider contract implemented with timeout/retry logic; provider response mapped to onboarding states; integration failures observable in logs. |
| P0 | UC-INT-002 | READY_FOR_DEVELOPMENT | ADD | BL-INT-002 | E-sign workflow creates agreement envelope, captures signed artifact, and stores reference; unsigned/expired agreements block restricted access. |
| P0 | UC-INT-003 | READY_FOR_DEVELOPMENT | ADD | BL-INT-003 | Notification provider sends templated messages; delivery/bounce status captured; critical notification retries follow policy. |
| P0 | UC-INT-004 | READY_FOR_DEVELOPMENT | ADD | BL-INT-004 | Banking/payment integration exchanges settlement references; duplicate callback handling is idempotent; reconciliation mismatch triggers exception flow. |

## Remaining Gap Alignment Backlog Diff

| Priority | Use Case ID | Historical Snapshot Gap Label | Backlog Diff | Backlog Item ID | Concrete Acceptance Checks |
|---|---|---|---|---|---|
| P1 | UC-DD-001 | IN_DEVELOPMENT | EXPAND | BL-DD-001 | NDA initiation persists request and status; signer identity bound to account; completed NDA grants controlled data-room eligibility. |
| P1 | UC-DD-002 | READY_FOR_DEVELOPMENT | ADD | BL-DD-002 | Restricted documents available only to NDA-authorized users; revoked/expired access denied; access/download events audited. |
| P1 | UC-OPP-001 | COMPONENT_COMPLETE | EXPAND | BL-OPP-001 | Opportunity cards sourced from backend catalogue; eligibility and visibility rules enforced; stale/inactive opportunities excluded. |
| P1 | UC-OPP-002 | IN_DEVELOPMENT | EXPAND | BL-OPP-002 | Server-side filter and sort contract supports sector/status/location fields; invalid filter values rejected; query behavior covered by tests. |
| P1 | UC-OPP-003 | IN_DEVELOPMENT | EXPAND | BL-OPP-003 | Detail page served from canonical API; unavailable/deprecated opportunity returns correct error state; detail-view action is traceable. |
| P1 | UC-PORT-001 | COMPONENT_COMPLETE | EXPAND | BL-PORT-001 | Pending view reflects live commitment states; status counts reconcile with commitment records; unauthorized data access blocked. |
| P1 | UC-PORT-002 | COMPONENT_COMPLETE | EXPAND | BL-PORT-002 | Holdings sourced from settled positions; asset metadata and ownership model are explicit; values reconcile with valuation source. |
| P1 | UC-PORT-003 | IN_DEVELOPMENT | EXPAND | BL-PORT-003 | Performance calculations defined and tested against known fixtures; chart uses real time-series data; recalculation events are traceable. |
| P1 | UC-PORT-004 | COMPONENT_COMPLETE | EXPAND | BL-PORT-004 | Activity timeline generated from auditable events; filters/search supported; export output matches underlying event history. |
| P1 | UC-DOC-001 | IN_DEVELOPMENT | EXPAND | BL-DOC-001 | Reports and tax docs generated with versioning; download authorization enforced; document access is logged per user/action. |
| P1 | UC-PROFILE-001 | IN_DEVELOPMENT | EXPAND | BL-PROFILE-001 | Profile updates persist with validation; sensitive fields have change controls; profile change history is queryable. |
| P1 | UC-NOTIFY-001 | IN_DEVELOPMENT | EXPAND | BL-NOTIFY-001 | Notification preference updates persist; event triggers respect preferences; high-priority alerts bypass opt-out only when policy permits. |
| P1 | UC-OPS-001 | IN_DEVELOPMENT | EXPAND | BL-OPS-001 | Contact form creates support ticket with owner/priority; SLA timers start on creation; ticket lifecycle events are auditable. |
| P1 | UC-OPS-002 | READY_FOR_DEVELOPMENT | ADD | BL-OPS-002 | Controlled correction requires authorization and reason; before/after values retained; approval workflow enforced for high-risk changes. |
| P1 | UC-REPORT-001 | READY_FOR_DEVELOPMENT | ADD | BL-REPORT-001 | Operational/compliance reports generated from authoritative stores; role-based report access enforced; schedule/manual runs both logged. |
| P2 | UC-PUB-001 | COMPONENT_COMPLETE | EXPAND | BL-PUB-001 | Public page instrumentation captures funnel events; legal/regulatory disclaimers are versioned; page content updates follow governance rules. |
| P2 | UC-NEWS-001 | COMPONENT_COMPLETE | EXPAND | BL-NEWS-001 | News feed content sourced from managed catalogue; investor personalization rules applied; content publication has audit trail. |
| P2 | UC-EVENT-001 | COMPONENT_COMPLETE | EXPAND | BL-EVENT-001 | Event registration persists attendance intent; reminders trigger from schedule; cancellation/no-show paths are handled. |
| P2 | UC-REF-001 | IN_DEVELOPMENT | EXPAND | BL-REF-001 | Referral links are unique and attributable; referral submissions validated and persisted; anti-abuse checks applied. |

## Sequencing Diff (Dependency-First)

1. `SEQUENCE-001`: Move BL-AUD-001 ahead of BL-SET-* and BL-ADMIN-* so all sensitive workflows emit standardized audit events from day one.
2. `SEQUENCE-002`: Deliver BL-IAM-001, BL-IAM-003 before onboarding/commitment work to avoid unsecured state transitions.
3. `SEQUENCE-003`: Deliver BL-INT-001 and BL-ONB-003 before BL-DD-* and BL-INV-* where eligibility gates are required.
4. `SEQUENCE-004`: Deliver BL-SET-001 before BL-SET-002 and BL-SET-003 to establish canonical funding references first.
5. `SEQUENCE-005`: Deliver BL-ADMIN-003 before BL-ADMIN-001/002/004 to ensure governance controls exist before admin tooling expands.

## Definition-of-Done Gate for Each Backlog Item

A backlog item from this diff can only move to `READY_FOR_E2E_TEST` when all are true:

1. Linked use-case IDs are explicit in the item.
2. Acceptance checks above are implemented and testable.
3. Positive and negative path tests exist.
4. Audit and access-control expectations are verified where applicable.
5. Traceability links are updated in delivery and evidence docs.
