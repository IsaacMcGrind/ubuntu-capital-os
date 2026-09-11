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
8. Record current implementation and contractor delivery evidence under `contractors/` without treating implementation provenance as proof of E2E completion, project approval, status promotion or authority to begin further work.

## 2.1 Contractor evidence and project-management workflow

Under `SRC-021`, 80K Developers (Pty) Ltd is the appointed Project Manager contractor and accountable project-management workstream. Thembinkosi Mtsweni is the responsible human Project Manager and final project-owner decision authority working through that management arrangement. In that capacity, Thembinkosi Mtsweni retains authority to interpret evidence, accept or reject delivery claims, update canonical Ubuntu Capital OS artifacts and statuses, set priorities, approve gates, and authorise subsequent work.

Contractors and coders must:

- execute only assigned work;
- keep all repository-hosted first-pass evidence under their existing `contractors/<contractor>/` directory; never modify canonical governance, status, decision, register, tracker, traceability, roadmap, plan, or summary artifacts in a `CONTRACTOR_TECHNICAL_EVIDENCE` change; use sanitised stable references in the contractor folder for approved external raw evidence;
- record what was performed, by whom and when, validation results, limitations, unfinished work, blockers, dependencies, and decisions required;
- avoid project-level approval, gate, status, completion, architecture, business, legal, or scope-authorisation statements.

Contractor evidence is not self-accepting. A merged evidence PR records provenance and observations only. It does not change a work package, use case, phase, gate, readiness, or completion state.

Because 80K Developers may act both as Project Manager contractor and as an implementation/coding contractor, every submission must identify which capacity applies. 80K technical evidence remains subject to the same evidence-only contract and review as other contractor evidence. Project-management authority applies only to explicitly identified Project-Manager-owned governance work; it is not inferred from the contributor organization.

Automated review may recommend `Candidate for human approval`, `Changes required`, `Blocked`, or `Unverified`, but those verdicts are analytical and cannot change repository authority or delivery status.

After a contractor evidence PR is reviewed and merged as provenance, the Project Manager separately assesses the merged evidence and performs a repository-wide impact analysis. Where evidence is accepted, canonical OS updates must be made through a separate, explicitly identified `PROJECT_MANAGER_GOVERNANCE` change. Only the Project Manager may approve the next assignment or status transition.

Required PR declaration:

Every PR must complete the project-owner-approved `.github/pull_request_template.md` (`SRC-021`) and provide:

- submitting organization and responsible human;
- declared capacity: `PROJECT_MANAGER_GOVERNANCE` or `CONTRACTOR_TECHNICAL_EVIDENCE`;
- assigned work-package IDs and assignment/decision source reference;
- authorised repository paths;
- revision-pinned evidence references;
- validation performed and results;
- what the evidence proves and does not prove;
- sensitive-information confirmation.

A declaration is not self-authorising. Reviewers must verify it against the cited source, decision, work package and path scope. Missing or unverifiable metadata makes the PR `Unverified` or `Changes required`.

Required sequence:

1. Project Manager assigns a bounded work package.
2. Contractor implements the assigned scope.
3. Contractor records sanitised evidence in the contractor folder.
4. The evidence PR is reviewed for factual support, reproducibility, safety, scope and role-boundary compliance.
5. A contractor evidence PR may be merged after the required review; merge records contractor provenance only and does not constitute Project Manager evidence acceptance or a canonical status change.
6. Project Manager separately assesses the merged evidence and analyses the integrated repository.
7. If evidence is accepted, the Project Manager updates canonical OS records through an explicitly identified `PROJECT_MANAGER_GOVERNANCE` change.
8. Thembinkosi Mtsweni decides priorities, status, gates and the next authorised work.

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

- Every use case has evidence status, source references, permissions, audit events, failure paths, acceptance criteria, **E2E completion criteria, and a stable planned E2E evidence target**. Actual E2E completion evidence is produced only after authorised implementation and is required for later status promotion and acceptance, not for the pre-implementation Phase 2 exit.
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
- protected API bootstrap/authorization probe and non-business test data
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

- An authorised test investor can authenticate, establish a server-validated session, and call a protected bootstrap/authorization test surface without receiving another user's data.
- Unauthenticated, insufficient-role, and cross-user access are denied and tested.
- Failures produce safe errors and traceable logs.
- Required realised traceability for completed work reconciles from source/use case/backlog through implementation, test/run, durable evidence and status.

`WP-AZ-009` owns the opportunity read model, seed/test data, access policy enforcement, and permitted catalogue API in Phase 6. Those catalogue outputs are not Phase 5 exit prerequisites; Phase 5 proves the shared authentication, authorization, validation, audit, persistence, observability, deployment, and test foundations that `WP-AZ-009` consumes.

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

Completed prerequisites—do not repeat them unless a material baseline, scope, or controlling-evidence change invalidates the 2026-09-07 decision:

1. **Completed:** Phase 0–4 output validation, residual-gap classification, material P0/architecture/security/NFR closure or bounding, planned pre-start traceability reconciliation, and live-artifact alignment were accepted through the formal project-owner review recorded by `SRC-020`.
2. **Completed:** readiness-decision authority is defined by `SRC-021`, `OQ-016` is closed, and Thembinkosi Mtsweni is the final project-owner decision authority.
3. **Completed:** the 2026-09-07 formal review revalidated `GO-2026-09-05-FSA-001`; `WP-AZ-001` through `WP-AZ-008` are `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. Re-run readiness only if material scope, baseline, risk, or non-waivable evidence changes.

Execute the current work next, in order:

1. Begin only the exact `WP-AZ-001` through `WP-AZ-008` scope authorised by `GO-2026-09-05-FSA-001`, in governed dependency order. Source-dependent work still requires a pinned application branch and commit.
2. Each technical contractor records objective, sanitised, revision-pinned first-pass evidence only under its applicable `contractors/<contractor>/` folder; approved external raw evidence is represented by a sanitised stable reference there.
3. Review and merge a contractor evidence PR as provenance only; merge does not accept evidence or change canonical status.
4. The 80K Developers Project Manager workstream separately assesses the merged evidence and, when accepted, links it into `docs/09-delivery/foundation-slice-a-evidence-register.md`, updates realised traceability and records any status change through a distinct `PROJECT_MANAGER_GOVERNANCE` PR.
5. A missing required realised hop blocks work-package/use-case status promotion and acceptance, not the already-completed bounded start decision.
6. Keep `WP-AZ-009` through `WP-AZ-012` blocked until Foundation evidence and the separate Phase 5 / first-business-slice gate are satisfied.
7. Continue regulated onboarding, NDA, settlement, custody, portfolio and production-hardening work only as their own evidence and dependency gates are satisfied.

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