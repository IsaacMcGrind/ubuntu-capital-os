# Ubuntu Capital OS — Implementation Roadmap

**Current programme status:** `PARTIALLY_READY`  
**Architecture readiness:** `READY_WITH_ASSUMPTIONS` for MVP cloud implementation  
**Cloud platform:** Azure MVP direction confirmed by `ARCH-ADR-001`  
**Production readiness:** `NOT_READY`

This roadmap separates faithful system reconstruction, Azure platform enablement, business-capability delivery and later production hardening. No production investment transaction should be released until critical legal, compliance, settlement, custody, ownership and permission questions are resolved.

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

**Primary artifact:** `docs/09-delivery/azure-mvp-platform-delivery-plan.md`.

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

**Business outcome:** establish a deployable, authenticated, observable and cost-governed platform shell that can support the first complete business vertical slice.

**Technical outcome:** repeatable frontend deployment, server-side authentication enforcement, protected API foundation, persistence baseline, secrets/service identity, telemetry and cost controls.

**Required evidence:** resource inventory, deployment URL, successful CI/CD run, valid/invalid authentication tests, protected API denial test, SQL migration/integration evidence, Key Vault/Managed Identity evidence, telemetry traces and budget alerts.

**Exit criteria:** Foundation Slice A reaches `COMPONENT_COMPLETE` without claiming any business use case `COMPLETE`.

## Phase 1B — Foundational Business Capabilities

**Included use cases:** UC-IAM-001, foundational parts of UC-ADMIN-003 and UC-AUD-001.

**Current status:** UC-IAM-001 remains `IN_DEVELOPMENT`; administration and audit foundations remain `READY_FOR_DEVELOPMENT` in the recorded implementation matrix.

**Business outcome:** authorised users can enter a protected investor workspace.

**Technical outcome:** Entra External ID integration, authenticated principal/session/token validation, protected API enforcement, role/data-scope enforcement, shared validation/error handling and business audit foundations.

**Required evidence:** positive/negative access tests, session/token tests, audit records, deployment reference and security review.

## Phase 2 — First Complete Vertical Slice: Discover and Express Interest

**Status:** `READY_FOR_DEVELOPMENT` after Phase 1A/1B dependencies are usable.

**Included use cases:** UC-OPP-001, UC-OPP-002, UC-OPP-003 and a deliberately non-binding subset of UC-INV-001.

**Business outcome:** an authorised investor can discover a published opportunity, inspect its details and submit a traceable non-binding expression of interest without moving money.

**Technical outcome:** investor UI, protected catalogue API, persistence, policy enforcement, audit, telemetry, automated tests and E2E acceptance work together in the deployed Azure environment.

**Exit criteria:** valid, invalid, duplicate, unauthorised, unavailable-opportunity, stale-data and system-failure scenarios pass with captured evidence.

## Phase 3 — Controlled Due Diligence and Investor Onboarding

**Included use cases:** UC-ONB-001 to UC-ONB-003, UC-DD-001, UC-DD-002, UC-PROFILE-001, UC-INT-001 and UC-INT-002 where validated.

**Business outcome:** prospective investors can become eligible and receive controlled access to restricted deal material.

**Technical outcome:** persisted onboarding state, eligibility rules, KYC/AML integration, compliance review, NDA/e-sign evidence, Blob-backed restricted document access, expiry/revocation and notifications.

**Exit criteria:** legal/compliance owners approve rules; external-provider behaviour is confirmed; access-leakage and recovery tests pass.

## Phase 4 — Investment Commitment and Communications

**Included use cases:** UC-INV-001 to UC-INV-003, UC-INT-003 and related notification capability.

**Business outcome:** eligible investors can submit and manage investment intent under approved legal rules.

**Technical outcome:** commitment/EOI lifecycle, approvals, idempotency, limits, retries, notifications, audit and operational recovery.

**Exit criteria:** binding/non-binding interpretation is explicit and approved; all critical states and exception paths are validated.

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
| Azure resource deployment | `READY_FOR_DEVELOPMENT` | target selected; deployment evidence not yet recorded |
| Current application implementation | `PARTIALLY_READY` | meaningful UI prototype; backend/business capability incomplete |
| 41-use-case delivery | 0 `COMPLETE` | no objective E2E-complete use case yet |
| First non-binding EOI slice | `READY_FOR_DEVELOPMENT` after foundation | preferred next vertical slice |
| Regulated settlement platform | `PARTIALLY_READY` / blocked | critical legal, custody, settlement and integration evidence missing |
| Production | `NOT_READY` | production hardening and acceptance not satisfied |

## Active delivery artifacts

- `docs/09-delivery/implementation-analysis-refresh-2026-08-29.md` — architecture-aware status analysis.
- `docs/09-delivery/implementation-coverage-gap-matrix.md` — 41-use-case implementation evidence/status baseline.
- `docs/09-delivery/azure-mvp-platform-delivery-plan.md` — Azure foundation implementation/evidence gates.
- `docs/09-delivery/prioritized-backlog-diff.md` — existing implementation-gap-to-backlog translation.
- `docs/02-architecture/azure-mvp-platform-decision.md` — confirmed Azure target decision.

## Immediate execution queue

1. Provision and evidence the Azure MVP resource/cost-governance baseline.
2. Deploy the current React/Vite application to Azure Static Web Apps through repeatable CI/CD.
3. Integrate Microsoft Entra External ID for UC-IAM-001 and implement protected Azure Functions API validation.
4. Establish Azure SQL persistence, Key Vault/Managed Identity and App Insights/Monitor foundations.
5. Implement the opportunity read API and non-binding EOI vertical slice.
6. Capture automated/E2E evidence and update the coverage matrix/tracker/traceability.
7. Progress onboarding, NDA, integrations and later regulated journeys only as their critical questions are resolved.
