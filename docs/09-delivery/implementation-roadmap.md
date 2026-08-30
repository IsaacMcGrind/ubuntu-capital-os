# Ubuntu Capital OS — Implementation Roadmap

**Current programme status:** `PARTIALLY_READY`  
**Architecture readiness:** `READY_WITH_ASSUMPTIONS` for MVP cloud implementation  
**Cloud platform:** Azure MVP direction confirmed by `ARCH-ADR-001`  
**Production readiness:** `NOT_READY`

This roadmap separates faithful system reconstruction, Azure platform enablement, business-capability delivery and later production hardening. No production investment transaction should be released until critical legal, compliance, settlement, custody, ownership and permission questions are resolved.

`plan.md` remains the controlling implementation sequence. This roadmap is subordinate to it. Foundation Slice A may proceed as documented **parallel infrastructure work** where the work is reversible and does not invent regulated business behaviour, but it does not close or bypass plan-required reconstruction, permissions, rules, journey/state, integration, backlog, tracker, traceability, validation or risk outputs. The post-merge repository-level interpretation is recorded in `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`.

## Phase 0 — Context and Architecture Baseline

**Status:** `ANALYSIS_IN_PROGRESS` — materially advanced.

**Included work:** source inventory, terminology, actors, permissions, system boundary, logical architecture, architecture decisions, evidence register, open questions, testing/evidence strategy and implementation coverage.

**Completed/materially advanced:**
- system boundary view;
- high-level logical architecture v0.1;
- priority use-case architecture map;
- UC-IAM-001 detailed architecture analysis;
- 41-use-case implementation coverage matrix;
- Azure cloud architecture and MVP cost baseline;
- evidence-grounded repository monitoring.

**Remaining gate:** reconcile repository structure/traceability, close critical architecture/open-question dependencies, and preserve the distinction between architecture selection and implementation evidence.

## Phase 1A — Azure MVP Platform Foundation

**Status:** `READY_FOR_DEVELOPMENT`.

**Primary delivery plan:** `docs/09-delivery/azure-mvp-platform-delivery-plan.md`.  
**Execution package:** `docs/09-delivery/foundation-slice-a-execution-package.md`.  
**Evidence register:** `docs/09-delivery/foundation-slice-a-evidence-register.md`.  
**Governance reconciliation:** `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`.

Foundation Slice A is explicitly documented as `WP-AZ-001` through `WP-AZ-008`. The execution package defines implementation tasks, acceptance criteria, evidence gates, ownership/authority boundaries, environment expectations and handoff conditions. The evidence register is the canonical working record for Foundation Slice A implementation proof. No Azure implementation completion is claimed until those gates are satisfied.

Foundation Slice A is a parallel platform workstream rather than evidence that earlier `plan.md` phases are complete. Programme-level Foundation completion and progression into the first business vertical slice additionally require the material first-slice repository-integrity outputs identified in the governance reconciliation to be present and consistent.

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

**Exit criteria:** the technical Foundation Slice A work packages reach their objective `COMPONENT_COMPLETE` evidence gates, and the programme-level Foundation status is not promoted until the material repository-integrity gate in `foundation-slice-a-governance-reconciliation.md` also reconciles. No business use case becomes `COMPLETE` from Foundation completion.

## Phase 1B — Foundational Business Capabilities

**Included use cases:** UC-IAM-001, foundational parts of UC-ADMIN-003 and UC-AUD-001.

**Current status:** UC-IAM-001 remains `IN_DEVELOPMENT`; administration and audit foundations remain `READY_FOR_DEVELOPMENT` in the recorded implementation matrix.

**Business outcome:** authorised users can enter a protected investor workspace.

**Technical outcome:** Entra External ID integration, authenticated principal/session/token validation, protected API enforcement, role/data-scope enforcement, shared validation/error handling and business audit foundations.

**Required evidence:** positive/negative access tests, session/token tests, audit records, deployment reference and security review.

Operational telemetry produced by Foundation `WP-AZ-007` does not satisfy `UC-AUD-001`. Business audit evidence remains separately governed and is required for the first EOI slice under `WP-AZ-011`.

## Phase 2 — First Complete Vertical Slice: Discover and Express Interest

**Status:** `READY_FOR_DEVELOPMENT` only after the usable Phase 1A/1B technical dependencies and the material first-slice repository-integrity prerequisites reconcile.

**Included use cases:** UC-OPP-001, UC-OPP-002, UC-OPP-003 and a deliberately non-binding subset of UC-INV-001.

**Business outcome:** an authorised investor can discover a published opportunity, inspect its details and submit a traceable non-binding expression of interest without moving money.

**Technical outcome:** investor UI, protected catalogue API, persistence, policy enforcement, audit, telemetry, automated tests and E2E acceptance work together in the deployed Azure environment.

**Repository-integrity prerequisite:** actor/permission evidence, first-slice business rules, journey/state definitions, relevant integration records, backlog coverage, E2E tracker, source-to-evidence traceability, validation coverage, open-question/risk reconciliation and other plan-required artifacts material to this slice must exist and be internally consistent.

**Exit criteria:** valid, invalid, duplicate, unauthorised, unavailable-opportunity, stale-data and system-failure scenarios pass with captured evidence; traceability and E2E records reconcile; no unresolved critical question invalidates the explicitly non-binding interpretation.

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
| Azure MVP platform selection | `CONFIRMED` | cloud provider/core MVP services selected |
| Azure resource deployment | `READY_FOR_DEVELOPMENT` | Foundation Slice A is defined as parallel infrastructure work; deployment evidence not yet recorded |
| Current application implementation | `PARTIALLY_READY` | meaningful UI prototype; backend/business capability incomplete |
| 41-use-case delivery | 0 `COMPLETE` | no objective E2E-complete use case yet |
| First non-binding EOI slice | `READY_FOR_DEVELOPMENT` after technical + integrity prerequisites | preferred next vertical slice, but cannot bypass plan-required evidence |
| Regulated settlement platform | `PARTIALLY_READY` / blocked | critical legal, custody, settlement and integration evidence missing |
| Production | `NOT_READY` | production hardening and acceptance not satisfied |

## Active delivery artifacts

- `docs/09-delivery/implementation-analysis-refresh-2026-08-29.md` — architecture-aware status analysis.
- `docs/09-delivery/implementation-coverage-gap-matrix.md` — 41-use-case implementation evidence/status baseline.
- `docs/09-delivery/azure-mvp-platform-delivery-plan.md` — Azure foundation implementation/evidence gates.
- `docs/09-delivery/foundation-slice-a-execution-package.md` — executable `WP-AZ-001` through `WP-AZ-008` task/acceptance/evidence package.
- `docs/09-delivery/foundation-slice-a-evidence-register.md` — Foundation Slice A evidence checklist and traceability register.
- `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` — post-merge full-repository reconciliation of Foundation work against `AGENT.md` and `plan.md`.
- `docs/09-delivery/prioritized-backlog-diff.md` — existing implementation-gap-to-backlog translation.
- `docs/02-architecture/azure-mvp-platform-decision.md` — confirmed Azure target decision.

## Immediate execution queue

The queue below must be read together with the controlling `plan.md`; it is a dependency-aware infrastructure/business-delivery subqueue, not a declaration that earlier required reconstruction outputs are complete.

1. Reconcile the plan-required first-slice repository-integrity outputs that are still missing or incomplete, especially actors/permissions, business rules, journey/state, relevant integration/validation records, backlog/tracker/traceability and risk/open-question linkage.
2. In parallel, execute `WP-AZ-001`: provision and evidence the Azure MVP resource/cost-governance baseline.
3. Execute `WP-AZ-002`: deploy the current React/Vite application to Azure Static Web Apps through repeatable CI/CD.
4. Execute `WP-AZ-003` and `WP-AZ-004`: integrate Microsoft Entra External ID for UC-IAM-001 and implement protected Azure Functions API validation.
5. Execute `WP-AZ-005` through `WP-AZ-007`: establish Azure SQL persistence, Key Vault/Managed Identity and Application Insights/Azure Monitor foundations.
6. Execute `WP-AZ-008`: prove version-controlled Foundation infrastructure reconstruction/reconciliation, gated CI/CD and source-to-deployment traceability.
7. Reconcile Foundation Slice A technical evidence with the repository-integrity gate in `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`; do not promote programme-level Foundation completion before both reconcile.
8. Implement the opportunity read API and non-binding EOI vertical slice (`WP-AZ-009`/`WP-AZ-010`) only against approved first-slice requirements and traceability.
9. Capture business-audit and E2E evidence (`WP-AZ-011`/`WP-AZ-012`) and update the coverage matrix/tracker/traceability before considering `READY_FOR_ACCEPTANCE`.
10. Progress Blob-backed document capabilities, onboarding, NDA, specialist integrations and later regulated journeys only as their actual use-case dependencies and critical questions are resolved.
