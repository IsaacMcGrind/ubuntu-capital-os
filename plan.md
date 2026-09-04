# Ubuntu Capital OS Execution Plan

## 1. Purpose

This plan converts the OurCrowd reference analysis and the Enterprise System Reconstruction prompt into an ordered, evidence-first execution programme for rebuilding Ubuntu Capital OS use case by use case.

The plan is the controlling implementation sequence for developers and autonomous coding agents. `AGENT.md` defines how the agent works; this file defines what must be produced, in what order, and what evidence is required before progressing.

## 2. Operating Rules

1. Execute phases in order unless a documented dependency permits parallel work.
2. Classify every requirement as `CONFIRMED`, `INFERRED`, `UNKNOWN`, or `CONTRADICTED`.
3. Do not implement inferred regulated or financial behaviour as fact without an explicit assumption record.
4. Deliver vertical slices through UI, API, persistence, security, audit, tests, and evidence.
5. Never mark a use case complete because code exists.
6. Keep reconstruction requirements separate from future enhancements.
7. Update the catalogue, backlog, tracker, traceability matrix, open questions, and summary after every completed phase.
8. Record current implementation and contractor delivery evidence under `contractors/` without treating implementation provenance as proof of E2E completion.

## 3. Required Repository Outputs

The execution must create and maintain:

```text
AGENT.md
plan.md
README.md

docs/
  00-context/
    source-inventory.md
    terminology.md
    system-boundary.md
  01-system-understanding/
    assumptions-and-evidence.md
    system-overview.md
  02-actors-and-permissions/
    actors.md
    permissions-matrix.md
  03-functional-domains/
    domains.md
    capability-map.md
  04-use-cases/
    use-case-catalogue.md
    UC-<DOMAIN>-<NUMBER>.md
  05-business-rules/
    business-rules.md
  06-journeys/
    journeys.md
    JRN-<NUMBER>.md
  07-state-models/
    state-models.md
  08-integrations/
    integration-catalogue.md
  09-delivery/
    implementation-roadmap.md
    backlog.md
    backlog.json
    e2e-delivery-tracker.md
  10-traceability/
    traceability-matrix.md
  11-open-questions/
    open-questions.md
  12-validation/
    validation-plan.md
  13-risks/
    gap-and-risk-register.md

contractors/
  80kDevelopers/
    README.md
    implementation-status.md
  Corefinity/
    README.md
    implementation-status.md
  HerLogicSolutions/
    README.md
    implementation-status.md

schemas/
  use-case.schema.json
  backlog-item.schema.json
  journey.schema.json
  state-model.schema.json
  integration.schema.json

data/
  use-cases.json
  backlog.json
  journeys.json
  state-models.json
  integrations.json

output/
  system-reconstruction-summary.md
```

The required-output tree is the canonical maintenance contract. File presence does not by itself satisfy a phase exit criterion. As of the 2026-09-03 reassessment, the canonical Phase 0–4 directories and major structured outputs materially exist; remaining work is therefore primarily validation, approval, reconciliation and gap closure rather than recreating those outputs from scratch.

The working `docs/02-architecture/` tree is an explicit structure exception because it is actively used but not declared in the canonical tree above. It must be formally dispositioned before the repository-integrity gate can close.

## 4. Phase 0 — Context and Architecture Baseline

### Objective
Establish a reliable baseline before implementation begins.

### Work Items

- Inventory all supplied screenshots, HTML, URLs, prompts, reports, and repository material.
- Record current implementation URLs, source repositories, contractor provenance, and repository-access constraints.
- Create system terminology and separate observed OurCrowd wording from Ubuntu Capital naming.
- Define public, authenticated investor, operational, administrative, and external-system boundaries.
- Document current evidence classifications and contradictions.
- Identify environments required for local, test, staging, and production.
- Define target architecture only where needed to support vertical slices.
- Establish testing, logging, audit, and evidence-capture conventions.

### Deliverables

- `docs/00-context/source-inventory.md`
- `docs/00-context/terminology.md`
- `docs/00-context/system-boundary.md`
- `contractors/80kDevelopers/README.md`
- `contractors/80kDevelopers/implementation-status.md`
- `contractors/Corefinity/README.md`
- `contractors/Corefinity/implementation-status.md`
- `contractors/HerLogicSolutions/README.md`
- `contractors/HerLogicSolutions/implementation-status.md`
- completed evidence register
- architecture decision log or baseline section

### Exit Criteria

- Every supplied source has a stable source ID.
- Current implementation and contractor provenance are recorded without overstating completion.
- Product boundaries and unknowns are explicit.
- No critical contradiction is hidden.
- The first vertical slice can be described without inventing binding investment behaviour.

## 5. Phase 1 — Actors, Permissions, Domains, and Core Models

### Objective
Define who acts, what authority they possess, and which capabilities the platform contains.

### Work Items

- Identify guest visitor, applicant investor, authorised investor, investment operations user, compliance reviewer, opportunity manager, reporting user, support user, platform administrator, and external services where supported.
- Produce the permissions matrix for create/read/update/delete/approve/admin/report/override access.
- Define functional domains and stable codes.
- Build the hierarchical capability map.
- Identify core entities and lifecycle candidates.

### Deliverables

- `docs/02-actors-and-permissions/actors.md`
- `docs/02-actors-and-permissions/permissions-matrix.md`
- `docs/03-functional-domains/capability-map.md`
- updated domain document

### Exit Criteria

- No use case has an undefined primary actor.
- Administrative access is separated from legal or business approval authority.
- Cross-tenant and unauthorised access risks are documented.

## 6. Phase 2 — Complete Use-Case Discovery and Specification

### Objective
Convert the current catalogue into a complete, structured reconstruction specification.

### Work Items

- Review the current 41-use-case catalogue for duplicates, gaps, and oversized cases.
- Populate every required master-catalogue field.
- Create one Markdown specification per use case using the exact 23-section template.
- Perform mandatory exception analysis for every relevant use case.
- Extract business rules into stable rule IDs.
- Create valid `data/use-cases.json` conforming to the schema.

### Priority Order

1. Authentication and session management
2. Investor profile and eligibility/onboarding boundaries
3. Opportunity discovery and opportunity detail
4. NDA/due-diligence access
5. Expression of interest or non-binding commitment
6. Pending activity and status tracking
7. Holdings and portfolio views
8. Performance and reporting
9. Documents and tax records
10. Notifications, support, administration, audit, and operations

### Deliverables

- complete master catalogue
- individual `UC-*.md` files
- `docs/05-business-rules/business-rules.md`
- `data/use-cases.json`

### Exit Criteria

- Every use case has evidence status, source references, permissions, audit events, failure paths, acceptance criteria, and E2E completion evidence.
- Critical unknowns remain visible and are linked to open questions.
- JSON validates against Draft 2020-12 schema.

## 7. Phase 3 — Journeys, States, Integrations, and Validation Design

### Objective
Connect individual use cases into end-to-end behaviour.

### Work Items

- Model major investor and operator journeys.
- Define lifecycle states and transition rules for investor account, opportunity, NDA, expression of interest, investment/commitment, document, notification, and support case where evidence supports them.
- Catalogue all known and inferred integrations.
- Define idempotency, retry, timeout, reconciliation, and failure handling requirements without assuming synchronous behaviour.
- Create a risk-ordered validation plan for all inferred and unknown behaviour.

### Minimum Journeys

- `JRN-001`: Visitor becomes an authenticated platform user
- `JRN-002`: Investor discovers and evaluates an opportunity
- `JRN-003`: Investor signs an NDA and accesses controlled material
- `JRN-004`: Investor submits a non-binding expression of interest
- `JRN-005`: Investor monitors pending activity and portfolio information
- `JRN-006`: Investor obtains reports and documents
- `JRN-007`: Operator publishes and manages an opportunity
- `JRN-008`: Support or operations resolves a failed or exceptional process

### Deliverables

- journey catalogue and Mermaid diagrams
- state models and Mermaid diagrams
- integration catalogue
- validation plan
- JSON schemas and validated data for journeys, states, and integrations

### Exit Criteria

- Journey decision points and recovery routes are explicit.
- State transitions are internally consistent.
- Every inferred integration has a proposed verification method.

## 8. Phase 4 — Development Backlog and Traceability

### Objective
Create a development-ready, dependency-aware implementation system.

### Work Items

- Convert use cases into Initiative → Epic → Feature → User Story → Technical/Test Task hierarchy.
- Add business value, acceptance criteria, dependencies, risk, discipline, evidence, and status to every item.
- Build the E2E delivery tracker.
- Build complete **pre-start planned traceability** for the proposed implementation scope using `source -> use case -> backlog -> architecture/design (where applicable) -> planned implementation target -> planned test/validation -> planned durable-evidence target -> planned tracker/status`.
- Define how those planned targets will be replaced by realised implementation, test/run and durable-evidence references after authorised execution begins.
- Generate and validate `backlog.json`.

### Deliverables

- `docs/09-delivery/backlog.md`
- `docs/09-delivery/backlog.json`
- `docs/09-delivery/e2e-delivery-tracker.md`
- `docs/10-traceability/traceability-matrix.md`
- backlog schema and validated JSON

### Exit Criteria

- Every backlog item traces to at least one use case.
- Every critical use case has frontend, backend, database, security, tests, deployment, documentation, and evidence work represented.
- Every applicable critical **planned pre-start** trace chain has stable source, use-case, backlog, architecture/design where applicable, planned implementation, planned test/validation, planned durable-evidence and planned tracker/status references. A missing required planned hop keeps the chain incomplete.
- Post-build implementation/test-run/durable evidence is **not** required to exit this pre-implementation phase because it can only be produced after authorised execution. Those realised hops become mandatory for later status promotion and acceptance.
- The E2E tracker reconciles to the same stable planned IDs and targets rather than substituting for missing planned traceability.
- The tracker uses only approved status values.

## 9. Phase 5 — Foundational Product Capabilities

### Objective
Implement only the shared capabilities needed by the first vertical slice.

### Included Capabilities

- application shell and route structure
- authentication and session handling
- role and permission enforcement
- investor profile identity baseline
- shared validation and error contract
- opportunity read model and seed data
- audit event framework
- structured logging and correlation IDs
- persistence migrations
- test harness and CI quality gates
- environment configuration and secrets strategy

### Evidence Required

- unit and integration test output
- unauthorised and insufficient-role tests
- database migration evidence
- audit records
- API request/response samples
- deployment/build reference
- realised traceability replacing the applicable planned Phase 4 targets with implementation, test/run and durable-evidence references

### Exit Criteria

- An authorised test investor can authenticate and securely load a permitted opportunity catalogue.
- Cross-user access is denied and tested.
- Failures produce safe errors and traceable logs.
- Required realised traceability for completed work reconciles from source/use case/backlog through implementation, test/run, durable evidence and status.

## 10. Phase 6 — First Complete Vertical Slice

### Selected Slice

**Discover an opportunity and submit a non-binding expression of interest.**

This slice is deliberately non-binding until investment settlement, accreditation, legal, ownership, custody, payment, and jurisdiction rules are confirmed.

### End-to-End Flow

1. User authenticates.
2. System verifies access to investor opportunities.
3. User browses and filters opportunities.
4. User opens opportunity detail.
5. User submits an expression of interest with valid input.
6. System prevents duplicate/repeated submissions according to documented rules.
7. System persists the expression and status.
8. System creates audit events.
9. System presents confirmation and pending state.
10. Notification behaviour runs or is reliably simulated.
11. Operator can read the submitted interest only if authorised.

### Mandatory Failure Scenarios

- invalid or missing amount/details
- unauthorised user
- insufficient role
- expired or unavailable opportunity
- duplicate submission
- browser refresh/repeated action
- database failure
- notification failure
- session expiry
- stale opportunity data
- concurrency conflict

### Exit Criteria

- UI, API, database, security, audit, notification/simulation, automated tests, deployment, and captured E2E evidence are complete.
- No unresolved critical question invalidates the interpretation of the slice.
- Realised source/use-case/backlog/implementation/test/durable-evidence/status traceability reconciles.
- Tracker status reaches `READY_FOR_ACCEPTANCE`, then `COMPLETE` only after acceptance evidence.

## 11. Phase 7 — Core Business Journeys

### Objective
Implement the primary investor experience after the architecture has been proven.

### Sequence

1. Opportunity search, sorting, filters, themes, and asset classes
2. Opportunity detail and controlled-document access
3. NDA lifecycle
4. Pending activities/status tracking
5. Holdings views
6. Portfolio performance views
7. News and personalised content
8. Reports and tax/document retrieval
9. Profile and preference management
10. Events, webinars, referrals, and contact/support where supported

### Exit Criteria per Journey

- related use cases are implemented as vertical slices
- alternate and exception paths are proven
- data state transitions are verified
- accessibility and responsive behaviour are tested
- operational recovery is documented

## 12. Phase 8 — Production Integrations

### Objective
Replace simulations with validated production-grade integrations.

### Candidate Integrations Requiring Validation

- identity/email verification
- MFA
- KYC/AML/accreditation
- e-signature/NDA
- email and push notifications
- CRM
- document storage and generation
- payment or wire instruction processing
- fund administration/custody
- analytics
- valuation and portfolio reporting

### Exit Criteria

- provider and protocol are confirmed
- authentication and secrets are secure
- timeouts, retries, idempotency, reconciliation, alerts, and manual recovery are tested
- integration logs and evidence are available

## 13. Phase 9 — Administration, Operations, Reporting, and Compliance

### Objective
Make the platform operable, supportable, and auditable.

### Work Items

- opportunity administration
- user and access support
- compliance review queues where validated
- manual intervention and correction workflows
- document/report administration
- notification administration
- activity and audit review
- operational dashboards and reconciliation
- retention and access review

### Exit Criteria

- support staff can identify and recover failed processes without unsafe database edits
- overrides require explicit authority and audit evidence
- reports reconcile to source records

## 14. Phase 10 — Production Hardening

### Work Items

- threat modelling and penetration testing
- tenant and object-level authorisation tests
- performance and load testing
- backup and recovery drills
- dependency failure simulation
- observability dashboards and alerts
- privacy, retention, and compliance validation
- accessibility review
- operational runbooks
- disaster recovery and business continuity

### Exit Criteria

- critical security findings are resolved
- recovery objectives are tested
- performance targets are measured
- all critical use cases have objective E2E evidence
- production readiness is formally approved

## 15. Immediate Execution Queue

The current queue must use the artifacts that already exist. Do not recreate canonical Phase 0–4 outputs merely because an older status document described them as absent.

Execute these tasks next, in order:

1. Validate the existing Phase 0–4 outputs against the applicable phase exit criteria and `AGENT.md` integrity rules, using `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md` as the current reconciliation point.
2. Produce a residual-gaps list that distinguishes `PRESENT_AND_ACCEPTABLE`, `PRESENT_BUT_PARTIAL`, `PRESENT_BUT_INCONSISTENT`, and `MISSING` so that already completed reconstruction work is not reopened unnecessarily.
3. Gain repository access to `HarleyJoker/ubuntu-capital-platform` and refresh the implementation inventory when access becomes available; until then, preserve the current recorded implementation evidence boundary.
4. Close the remaining P0 business/legal decisions required for the Foundation and first slice: EOI meaning, jurisdiction/eligibility, NDA policy, operator authority, logical data ownership, and authoritative state transitions.
5. Close the remaining architecture/security/NFR readiness items identified by the current Solution Architecture audit, including threat model, authorization design, privacy/retention, measurable availability/performance/recovery/cost targets, the first-slice API/error/audit/persistence/integration contracts, and the minimum ADR set.
6. Reconcile the **pre-start planned traceability chain** for the proposed Foundation/first-slice scope as `source -> use case -> backlog -> architecture/design (where applicable) -> planned implementation target -> planned test/validation -> planned durable-evidence target -> planned tracker/status`. Update `docs/10-traceability/traceability-matrix.md` and `docs/09-delivery/e2e-delivery-tracker.md` to the same stable planned IDs/targets, and verify schemas, structured data, links, IDs, counts, statuses, open-question references, and risk references. Do not require implementation/test-run/deployment/durable evidence that can only be produced after authorised execution starts.
7. Reconcile `output/system-reconstruction-summary.md`, `README.md`, the implementation roadmap and all live delivery/gate artifacts with the same current readiness position; no summary may state that the business slice can proceed while Foundation/Phase 5 gates remain blocked.
8. Define and record the readiness-decision approving authority and decision-control contract. Until authority exists, `GO` and `CONDITIONAL_GO` cannot open the gate and `NO_GO` remains effective.
9. Run and record a formal pre-implementation readiness review with an explicit `GO`, `CONDITIONAL_GO`, or `NO_GO` decision only after all non-waivable integrity conditions and required **planned pre-start** traceability hops for the proposed scope reconcile.
10. Only if an effective authorised decision permits execution, begin the exact permitted subset of `WP-AZ-001` through `WP-AZ-008` and capture objective evidence in `docs/09-delivery/foundation-slice-a-evidence-register.md`.
11. During authorised delivery, replace planned targets progressively with realised `implementation -> test/run -> durable evidence -> validation/status` references. A missing required realised hop blocks work-package/use-case status promotion and acceptance, not the pre-start decision itself.
12. Keep `WP-AZ-009` through `WP-AZ-012` blocked until Foundation evidence and the separate Phase 5 / first-business-slice gate are satisfied.
13. Continue regulated onboarding, NDA, settlement, custody, portfolio and production-hardening work only as their own evidence and dependency gates are satisfied.

## 16. Agent Completion Protocol

At the end of each execution cycle, the agent must report:

- files created or updated;
- use cases progressed;
- evidence classifications changed;
- contractor implementation evidence added or reconciled;
- open questions added or resolved;
- tests or schema validations executed;
- current blockers;
- tracker status changes;
- next dependency-aware action.

The agent must commit related changes atomically with a descriptive message and use a focused pull request for each coherent change set.