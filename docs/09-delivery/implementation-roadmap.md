# Ubuntu Capital OS — Implementation Roadmap

> **Current Foundation decision — 2026-09-07:** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001`. The execution gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. This authorises governed start only; implementation, completion, business-use-case and production claims remain evidence-gated. Source: `SRC-020`.

**Current programme status:** `PARTIALLY_READY`  
**Architecture readiness:** `READY_WITH_ASSUMPTIONS` for MVP cloud implementation  
**Cloud platform:** Azure MVP direction confirmed by `ARCH-ADR-001`  
**Production readiness:** `NOT_READY`

This roadmap separates faithful system reconstruction, Azure platform enablement, business-capability delivery and later production hardening. No production investment transaction should be released until critical legal, compliance, settlement, custody, ownership and permission questions are resolved.

`plan.md` remains the controlling implementation sequence. This roadmap is subordinate to it. The major canonical Phase 0 through Phase 4 outputs now materially exist. Foundation Slice A's bounded scope is recorded in `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`, and progression is `OPEN_FOR_AUTHORISED_EXECUTION` after the 2026-09-07 formal review, while downstream business-slice progression remains separately gated by validation, approval, traceability reconciliation, architecture/security/NFR closure, structure-exception disposition, and scope-specific readiness controls.

## Phase 0 — Context and Architecture Baseline

**Status:** `ANALYSIS_IN_PROGRESS` — materially advanced.

**Included work:** source inventory, terminology, actors, permissions, system boundary, logical architecture, architecture decisions, evidence register, open questions, testing/evidence strategy and implementation coverage.

**Completed/materially advanced:**
- system boundary view;
- high-level logical architecture v0.1;
- priority use-case architecture map;
- UC-IAM-001 detailed architecture analysis;
- historical 41-use-case implementation coverage matrix from an unpinned reported snapshot;
- Azure cloud architecture and MVP cost baseline;
- evidence-grounded repository monitoring;
- canonical actors/permissions, business rules, journeys, state models, integrations, backlog/tracker/traceability/validation/risk artifacts and structured data materially present.

**Remaining gate:** validate the existing Phase 0 through Phase 4 outputs against `AGENT.md` and `plan.md`; disposition the `docs/02-architecture/` structure exception; and reconcile business/legal, architecture, security, NFR, planned traceability, schema, link, ID, count, evidence-classification, open-question and risk gaps. A non-authorising `NO_GO` may be recorded or refreshed at any point while blockers remain. An execution-authorising `GO` or explicitly scoped `CONDITIONAL_GO` may be recorded only after all applicable non-waivable closure and readiness-authority requirements reconcile.

## Phase 1A — Azure MVP Platform Foundation

**Status:** `READY_FOR_DEVELOPMENT` for `WP-AZ-001` through `WP-AZ-008`; execution gate `OPEN_FOR_AUTHORISED_EXECUTION`; no realised start evidence is recorded.

**Primary delivery plan:** `docs/09-delivery/azure-mvp-platform-delivery-plan.md`.  
**Execution package:** `docs/09-delivery/foundation-slice-a-execution-package.md`.  
**Evidence register:** `docs/09-delivery/foundation-slice-a-evidence-register.md`.  
**Governance reconciliation:** `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`.  
**Current readiness decision:** `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`.

Foundation Slice A is documented as `WP-AZ-001` through `WP-AZ-008`. The package defines implementation tasks, acceptance criteria, evidence gates, ownership/authority boundaries, environment expectations and handoff conditions. `GO-2026-09-05-FSA-001` records that exact scope and authority and was revalidated by the project owner on 2026-09-07. Execution may begin in governed dependency order. The older governance reconciliation remains a required compatibility reference and does not override current decision scope controls.

**Chosen platform services:**
- Azure Static Web Apps;
- Microsoft Entra External ID;
- Azure Functions;
- Azure SQL Database where relational persistence is appropriate;
- Azure Blob Storage;
- Azure Key Vault;
- Managed Identity;
- Application Insights;
- Azure Monitor;
- Azure Cost Management;
- CI/CD through GitHub Actions or Azure DevOps as delivery requires.

Azure Blob Storage is part of the confirmed target service set but is intentionally deferred outside `WP-AZ-001` through `WP-AZ-008`. It becomes implementation work when a business slice requires controlled document/generated-file storage; Foundation Slice A does not claim Blob implementation evidence.

**Business outcome:** establish a deployable, authenticated, observable and cost-governed platform shell that can support the first complete business vertical slice.

**Technical outcome:** repeatable frontend deployment, server-side authentication enforcement, protected API foundation, persistence baseline, secrets/service identity, telemetry and cost controls.

**Required evidence:** resource inventory, deployment URL, successful CI/CD run, valid/invalid authentication tests, protected API denial test, SQL migration/integration evidence, Key Vault/Managed Identity evidence, telemetry traces and budget alerts.

**Start gate status:** satisfied by the formal project-owner review recorded on 2026-09-07. `GO-2026-09-05-FSA-001` is effective for its bounded scope; implementation completion and all status promotion remain evidence-gated.

**Exit criteria:** after the start gate is satisfied and execution begins, every Foundation work package must meet its objective evidence gate before Foundation Slice A as a whole can be described as `COMPONENT_COMPLETE`. No business use case becomes `COMPLETE` from Foundation completion.

## Phase 1B — Foundational Business Capabilities

**Included use cases:** UC-IAM-001, foundational parts of UC-ADMIN-003 and UC-AUD-001.

**Historical snapshot labels:** UC-IAM-001 was recorded as `IN_DEVELOPMENT`; administration and audit foundations were recorded as `READY_FOR_DEVELOPMENT`. Those labels come from an unpinned reported snapshot and are not current delivery assertions. Current reproducible application-source verification remains `BLOCKED_BY_CONTEXT` pending an authorised revision-pinned inspection and durable run evidence.

**Business outcome:** authorised users can enter a protected investor workspace.

**Technical outcome:** Entra External ID integration, authenticated principal/session/token validation, protected API enforcement, role/data-scope enforcement, shared validation/error handling and business audit foundations.

**Required evidence:** positive/negative access tests, session/token tests, audit records, deployment reference and security review.

Operational telemetry produced by Foundation `WP-AZ-007` does not satisfy `UC-AUD-001`. Business audit evidence remains separately governed and is required for the first EOI slice under `WP-AZ-011`.

## Phase 2 — First Complete Vertical Slice: Discover and Express Interest

**Status:** `BLOCKED_BY_CONTEXT` until the Foundation and first-slice start gates reconcile.

**Included use cases:** UC-OPP-001, UC-OPP-002, UC-OPP-003 and a deliberately non-binding subset of UC-INV-001.

**Business outcome:** an authorised investor can discover a published opportunity, inspect its details and submit a traceable non-binding expression of interest without moving money.

**Technical outcome:** investor UI, protected catalogue API, persistence, policy enforcement, audit, telemetry, automated tests and E2E acceptance work together in the deployed Azure environment.

**Start gate:** `WP-AZ-009`, `WP-AZ-010`, `WP-AZ-011`, and `WP-AZ-012` must not start, advance, or be promoted until Foundation Slice A has satisfied its evidence gates, the current readiness decision still permits progression, all plan-required outputs material to the first business slice are internally consistent, and the controlling `plan.md` Phase 5 foundational product capabilities and exit criteria required before Phase 6 are complete and evidenced.

**Repository-integrity prerequisite:** actor/permission evidence, first-slice business rules, journey/state definitions, relevant integration records, backlog coverage, E2E tracker, planned pre-start traceability, validation coverage, open-question/risk reconciliation and other plan-required artifacts material to this slice must exist and be internally consistent.

**Exit criteria:** valid, invalid, duplicate, unauthorised, unavailable-opportunity, stale-data and system-failure scenarios pass with captured evidence; realised traceability and E2E records reconcile; no unresolved critical question invalidates the explicitly non-binding interpretation.

## Phase 3 — Controlled Due Diligence and Investor Onboarding

**Included use cases:** UC-ONB-001 to UC-ONB-003, UC-DD-001, UC-DD-002 and UC-PROFILE-001.

**Business outcome:** prospective investors can progress through onboarding and controlled due-diligence preparation while the external-integration work required for KYC/AML and e-signature is delivered under Phase 4.

**Technical outcome:** persisted onboarding state, eligibility rules, compliance-review state, NDA/data-room state models, Blob-backed restricted document access, expiry/revocation and notification hooks. Phase 3 cannot exit until its required Phase 4 external-integration dependencies are proven.

**Exit criteria:** legal/compliance owners approve rules; required external-provider dependencies are complete; access-leakage and recovery tests pass.

## Phase 4 — External Integrations, Investment Commitment and Communications

**Included use cases:** UC-INT-001, UC-INT-002, UC-INT-003, UC-INV-001 to UC-INV-003 and related notification capability.

**Business outcome:** validated external identity/agreement/messaging integrations support eligibility, due diligence and investment-intent workflows under approved legal rules.

**Technical outcome:** KYC/AML provider integration, e-signature evidence, commitment/EOI lifecycle, approvals, idempotency, limits, retries, notifications, audit and operational recovery.

**Exit criteria:** provider behaviour is validated; binding/non-binding interpretation is explicit and approved; all critical states and exception paths are validated.

## Phase 5 — Funding, Settlement and Reconciliation

**Included use cases:** UC-SET-001 to UC-SET-003 and UC-INT-004.

**Current status:** blocked by critical operating-model evidence.

**Business outcome:** accepted commitments can be funded, matched, reconciled and resolved safely.

**Technical outcome:** settlement instructions, immutable references, payment/banking integration, partial/duplicate/late/reversed payment handling, reconciliation, maker-checker controls, monitoring and recovery.

**Exit criteria:** banking/custody/client-money model, refunds, chargebacks and reconciliation ownership are confirmed; failure simulations pass.

## Phase 6 — Portfolio, Documents, Administration and Support

**Included use cases:** UC-PORT-001 to UC-PORT-004, UC-DOC-001, UC-NEWS-001, UC-EVENT-001, UC-REF-001, UC-OPS-001, UC-OPS-002, UC-ADMIN-001 to UC-ADMIN-004.

**Business outcome:** investors can manage their post-investment relationship while authorised teams operate the platform.

**Technical outcome:** holdings, valuation/performance calculations, activity, Blob-backed document access, content, opportunity administration, support tooling, controlled corrections and role enforcement.

**Exit criteria:** ownership/valuation rules reconcile to approved examples; document access and operational overrides are auditable.

## Phase 7 — Reporting, Compliance and Production Hardening

**Included use cases:** UC-AUD-001, UC-AUD-002, UC-REPORT-001, UC-NOTIFY-001 and cross-cutting hardening.

**Business outcome:** management, compliance, operations and investors can rely on a secure and supportable production service.

**Technical outcome:** business audit/reporting, retention, privacy, observability, backup/recovery, resilience, performance, security-event response, runbooks and failure simulation.

**Azure scale rule:** advanced services such as Service Bus, Redis, API Management, Front Door, premium networking and multi-region deployment are introduced only when measured requirements justify them.

**Exit criteria:** production readiness review passes; critical open questions are closed; E2E evidence is complete; recovery objectives are demonstrated.

## Programme status snapshot

| Area | Status | Meaning |
|---|---|---|
| Logical architecture | `READY_WITH_ASSUMPTIONS` | capability boundaries are usable; critical legal/business unknowns remain |
| Azure MVP platform selection | `CONFIRMED` | cloud provider/core MVP services selected; this is evidence classification, not delivery completion |
| Azure resource deployment | `READY_FOR_DEVELOPMENT` | execution is authorised by the revalidated bounded GO; no realised start or deployment evidence is recorded |
| Current application-source verification | `BLOCKED_BY_CONTEXT` | stated repository identity is known, but the latest source revision and runtime behaviour are not reproducibly verified |
| Historical unpinned application snapshot | `PARTIALLY_READY` (historical label only) | reported UI prototype observations cannot be promoted to current status without revision-pinned evidence |
| 41-use-case delivery | 0 `COMPLETE` | no objective E2E-complete use case is recorded |
| First non-binding EOI slice | `BLOCKED_BY_CONTEXT` | WP-AZ-009..012 cannot start or advance until Foundation + Phase 5 + first-slice integrity gates reconcile |
| Regulated settlement capability | `BLOCKED_BY_CONTEXT` | current implementation is unverified and critical legal, custody, settlement, and integration evidence is missing |
| Production | `NOT_READY` | production hardening and acceptance not satisfied |

## Active delivery artifacts

- `docs/09-delivery/implementation-analysis-refresh-2026-09-05.md` — current revision-pinned implementation assessment at OS evidence commit `e1bbbe2fa5bcb3570271ac3bdbcba5b3072ad256`.
- `docs/09-delivery/implementation-analysis-refresh-2026-08-29.md` — historical architecture-aware status snapshot; `HISTORICAL_SNAPSHOT` / `NON_EXECUTABLE`, not an execution authority.
- `docs/09-delivery/implementation-coverage-gap-matrix.md` — historical/partial 41-use-case snapshot mapping; not a current implementation-status baseline until revision-pinned evidence is recorded.
- `docs/09-delivery/azure-mvp-platform-delivery-plan.md` — Azure foundation implementation/evidence gates.
- `docs/09-delivery/foundation-slice-a-execution-package.md` — active execution/acceptance/evidence package for the bounded `WP-AZ-001` through `WP-AZ-008` scope; execution is authorised.
- `docs/09-delivery/foundation-slice-a-evidence-register.md` — Project-Manager-owned canonical Foundation Slice A evidence checklist and traceability register; technical contractors submit first-pass evidence under their applicable contractor folders.
- `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` — compatibility/governance chain for Foundation start gates.
- `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md` — current repository-state reassessment and residual closure set that must feed the formal readiness decision.
- `docs/09-delivery/prioritized-backlog-diff.md` — existing implementation-gap-to-backlog translation.
- `docs/02-architecture/azure-mvp-platform-decision.md` — confirmed Azure target decision.

## Immediate execution queue

The queue follows the controlling `plan.md`. Existing canonical outputs were accepted as reconciled by the project owner during the formal review recorded on 2026-09-07. `GO-2026-09-05-FSA-001` is the effective bounded authority; the next executable action is governed Foundation delivery.

Completed prerequisites—preserve rather than repeat: the project-owner review recorded by `SRC-020` accepted the Phase 0–4/residual-gap, P0/architecture/security/NFR, planned-traceability, live-artifact, readiness-authority and decision prerequisites for the bounded Foundation scope and revalidated `GO-2026-09-05-FSA-001` on 2026-09-07. Reopen that decision only for a material baseline, scope, risk, or non-waivable evidence change.

1. Begin only the authorised `WP-AZ-001` through `WP-AZ-008` scope in governed dependency order; source-dependent packages still require a pinned application branch and commit.
2. Each technical contractor captures objective, sanitised, revision-pinned first-pass evidence only under its applicable `contractors/<contractor>/` folder; approved external raw evidence is represented by a sanitised stable reference there.
3. Review and merge contractor evidence as provenance only; merge is not acceptance or status promotion.
4. The 80K Developers Project Manager workstream separately assesses merged evidence and, when accepted, reconciles it into the canonical Foundation evidence register, realised traceability, E2E tracker, and status records through a distinct `PROJECT_MANAGER_GOVERNANCE` PR.
5. A required realised `Pending` hop blocks status promotion, `COMPONENT_COMPLETE`, E2E readiness or acceptance; it does not invalidate the already-completed bounded start decision unless it reveals a material non-waivable contradiction.
6. Keep `WP-AZ-009` through `WP-AZ-012` blocked until Foundation evidence, the controlling Phase 5 capabilities/exit criteria, and the first-slice integrity gate all reconcile.
7. Progress Blob-backed document capabilities, onboarding, NDA, specialist integrations and later regulated journeys only as their actual use-case dependencies and critical questions are resolved.
