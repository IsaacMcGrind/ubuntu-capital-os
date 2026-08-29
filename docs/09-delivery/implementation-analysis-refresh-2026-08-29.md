# Ubuntu Capital OS — Implementation Analysis Refresh

**Assessment date:** 2026-08-29  
**Overall status:** `PARTIALLY_READY`  
**Architecture readiness:** materially improved  
**Implementation readiness:** unchanged at business-capability level unless new implementation evidence is added  
**Production readiness:** not ready

## 1. Executive assessment

Ubuntu Capital OS now has a materially clearer target architecture and a bounded MVP cloud implementation path.

The repository contains:

- a technology-neutral system boundary and high-level logical architecture;
- a priority use-case-to-architecture map;
- a detailed UC-IAM-001 architecture analysis;
- a 41-use-case implementation coverage matrix based on previously inspected implementation evidence;
- a chosen Azure MVP cloud direction covering frontend hosting, identity, backend compute, relational persistence, document storage, secrets, observability and cost governance;
- a twice-daily evidence-grounded repository monitoring capability.

This improves **implementation decision readiness**, but it does not prove that the corresponding platform capabilities have been implemented.

The recorded implementation evidence still describes the application as predominantly a React/Vite frontend prototype with UI coverage across many investor journeys and limited/no verified backend business capability for authentication, persistence, regulated onboarding, investment state, settlement, administration, audit, reporting and external integrations.

## 2. Evidence boundary for this refresh

This refresh is grounded in repository evidence currently available in `ubuntu-capital-os`.

Primary evidence:

- `docs/02-architecture/system-boundary-view.md`
- `docs/02-architecture/high-level-logical-architecture-v0.1.md`
- `docs/02-architecture/priority-use-case-architecture-map.md`
- `docs/02-architecture/use-cases/UC-IAM-001-sign-in-investor-portal.md`
- `contractors/HerLogicSolutions/azure-architecture.md`
- `contractors/HerLogicSolutions/azure-mvp-cost-breakdown.md`
- `docs/09-delivery/implementation-coverage-gap-matrix.md`
- `docs/09-delivery/implementation-roadmap.md`
- `docs/09-delivery/prioritized-backlog-diff.md`
- `docs/11-open-questions/open-questions.md`

No new direct source-code inspection of `HarleyJoker/ubuntu-capital-platform` was performed as part of this refresh. Therefore existing implementation statuses are preserved unless the OS repository itself contains stronger delivery evidence.

## 3. What has materially changed

### 3.1 Logical architecture is now established

The logical architecture defines authoritative capability ownership for:

- Identity & Access;
- Investor Onboarding & Eligibility;
- Opportunity Management;
- Confidentiality & Due Diligence;
- Investment Intent / Commitment;
- Funding & Settlement;
- Portfolio Management;
- Investor Documents;
- Notifications;
- Administration, Audit & Evidence, and Management Reporting.

This reduces ambiguity around where business state belongs and prevents implementation components from becoming accidental owners of business decisions.

### 3.2 MVP cloud platform is now selected

The Azure MVP platform decision establishes the following target implementation path:

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
- CI/CD using the existing GitHub/Azure delivery capability.

This closes the cloud-provider/platform-service selection gap for the MVP without changing the technology-neutral logical capability boundaries.

### 3.3 Monitoring and governance are stronger

The repository monitor is now evidence-grounded and designed to distinguish direct material change from broad use-case references. This improves repository governance and reduces false progress claims.

## 4. Current implementation position

The current recorded matrix remains the authoritative implementation coverage view for the 41 use cases until stronger code/E2E evidence is added.

### Coverage summary

The counts below are derived from the row-level statuses in `implementation-coverage-gap-matrix.md`.

| Status | Count | Interpretation |
|---|---:|---|
| `COMPONENT_COMPLETE` | 7 | UI/page-level component evidence only; not E2E business completion |
| `IN_DEVELOPMENT` | 16 | Partial/prototype implementation evidence exists |
| `READY_FOR_DEVELOPMENT` | 18 | No substantive implementation evidence recorded |
| `COMPLETE` | 0 | No use case has objective E2E completion evidence |

### Readiness interpretation

- **Frontend experience:** meaningful prototype coverage exists.
- **Backend/API layer:** not sufficiently evidenced for the core business journeys.
- **Persistence:** not sufficiently evidenced for regulated or transactional business state.
- **Authentication/session enforcement:** UI exists; enforceable backend capability remains incomplete in recorded evidence.
- **KYC/AML/accreditation:** not implemented beyond placeholder/onboarding representation.
- **NDA/restricted due diligence:** trigger exists; enforceable lifecycle/access state remains incomplete.
- **Expression of interest / investment workflow:** UI affordance exists; backend lifecycle/persistence is incomplete.
- **Settlement/reconciliation:** not implemented in recorded evidence.
- **Portfolio:** screens exist, but holdings/valuation ownership and calculation provenance are not production-evidenced.
- **Documents:** UI exists; secure document service/generation/retrieval auditing is incomplete.
- **Administration/RBAC:** not implemented in recorded evidence.
- **Audit:** no complete auditable event pipeline is recorded.
- **Reporting/compliance:** not implemented in recorded evidence.
- **External integrations:** KYC, e-signature, messaging and banking/payment providers remain unresolved/unimplemented.

## 5. Architecture-to-implementation gap

The principal gap is no longer "what cloud should we use?". The principal gap is now **turning the accepted logical architecture and Azure platform decision into secure, traceable vertical slices**.

| Architecture capability | Target platform direction | Current implementation evidence | Delivery gap |
|---|---|---|---|
| Identity & Access | Entra External ID + protected Azure Functions | Login/MFA UI | Provider integration, token/session validation, server-side enforcement, negative-path tests, audit |
| Investor Onboarding & Eligibility | Functions + SQL + external KYC/AML integration | Multi-step onboarding UI | Persistence, rules, workflow state, provider integration, compliance decisions |
| Opportunity Management | Functions + SQL, Static Web Apps consumer | Opportunity UI/static local data | Canonical API/data source, admin publishing, lifecycle controls, access policy |
| Confidentiality & DD | Functions + SQL/Blob + e-sign provider when selected | NDA/data-room affordance | NDA state model, signature evidence, access grant, protected documents, revocation/expiry |
| Investment Intent | Functions + SQL | Express-interest UI | Non-binding EOI workflow, idempotency, persistence, status, policy checks, audit |
| Settlement | Functions + SQL + banking/payment integration | No substantive evidence | Full operating model, provider, reconciliation, exceptions, maker-checker, audit |
| Portfolio | Functions + SQL | Static/mock holdings/performance UI | Ownership model, ledger/source, valuation rules, calculations, reconciliation |
| Documents | Blob + Functions + SQL metadata | Reports/download UI | Authorised file service, generation/upload, retention, access logs |
| Notifications | Functions + provider TBD | Preference UI | trigger catalogue, persistence, delivery integration, delivery evidence |
| Administration | Protected admin APIs/UI | no substantive admin capability | RBAC admin, opportunity lifecycle, reference data, controlled operations |
| Audit & Reporting | SQL/storage + Application Insights/Azure Monitor for operational telemetry | no business audit pipeline | immutable/material event model, retention, review/reporting interfaces |

## 6. Azure foundation implementation status

The Azure service selection is `CONFIRMED` as target architecture. The Azure foundation workstream is consistently `READY_FOR_DEVELOPMENT`: the target and evidence gates are defined, but no Azure provisioning/deployment evidence has yet been recorded. Absence of deployment evidence is an evidence gap, not a separate `NOT_ANALYSED` delivery status.

| Azure capability | Target | Current delivery status | Evidence required |
|---|---|---|---|
| Static Web Apps | frontend hosting | `READY_FOR_DEVELOPMENT` | resource/deployment URL, build/deploy run, environment configuration |
| Entra External ID | customer authentication | `READY_FOR_DEVELOPMENT` | tenant/app config, user flow/policy, token validation, protected API test |
| Azure Functions | backend/API compute | `READY_FOR_DEVELOPMENT` | deployed functions, API contract, auth enforcement, telemetry |
| Azure SQL | relational persistence | `READY_FOR_DEVELOPMENT` | logical data mapping, schema/migrations, secure connection, CRUD/integration tests |
| Blob Storage | document storage | `READY_FOR_DEVELOPMENT` | container/access design, authorised upload/download evidence, retention approach |
| Key Vault | secrets/config | `READY_FOR_DEVELOPMENT` | vault, access policy/RBAC, secret references, no secrets in client/repo |
| Managed Identity | service authentication | `READY_FOR_DEVELOPMENT` | enabled identities and successful resource access without embedded credentials |
| Application Insights | telemetry | `READY_FOR_DEVELOPMENT` | request/dependency/exception traces and correlation evidence |
| Azure Monitor | alerts/health | `READY_FOR_DEVELOPMENT` | dashboard/alerts and failure-test evidence |
| Cost Management | budgets/alerts | `READY_FOR_DEVELOPMENT` | budget threshold and notification evidence |
| CI/CD | repeatable deployment | partial capability exists historically | build/test/deploy pipeline for the selected Azure resources |

## 7. Delivery status by programme phase

### Phase 0 — Context and architecture baseline

**Status:** `ANALYSIS_IN_PROGRESS` / materially advanced.

Completed or materially advanced:

- system boundary;
- logical architecture;
- priority architecture map;
- Azure MVP cloud direction;
- cost baseline;
- implementation coverage matrix;
- repository monitoring.

Still required:

- reconcile architecture directory placement with the canonical `plan.md` repository structure;
- formalise remaining architecture decisions and open-question ownership;
- ensure source inventory/traceability includes the Azure decision and related evidence.

### Phase 1 — Foundational capabilities

**Status:** `IN_DEVELOPMENT` at UI level; Azure foundation workstream `READY_FOR_DEVELOPMENT`; backend foundation not proven.

Priority implementation sequence:

1. Azure resource/environment baseline.
2. Static Web Apps deployment of the current frontend.
3. Entra External ID integration.
4. Azure Functions API foundation.
5. server-side authentication/authorisation enforcement.
6. Azure SQL persistence foundation.
7. audit-event model and persistence.
8. Key Vault/Managed Identity.
9. Application Insights/Azure Monitor.
10. automated build/test/deploy evidence.

### Phase 2 — First complete vertical slice

**Status:** `READY_FOR_DEVELOPMENT` once Phase 1 access/persistence controls are usable.

Target slice remains:

> authenticated investor discovers an opportunity and submits a **non-binding expression of interest**.

Settlement remains outside this first slice.

### Phases 3–7

**Status:** predominantly `READY_FOR_DEVELOPMENT` / blocked by unresolved legal, compliance, data and integration decisions.

## 8. Critical blockers

The highest-impact unresolved blockers remain:

1. supported investor jurisdictions;
2. eligibility/accreditation rules;
3. legal meaning of investment action;
4. settlement/custody/reconciliation model;
5. legal ownership structure;
6. opportunity lifecycle rules;
7. NDA lifecycle and e-signature evidence;
8. portfolio valuation/performance formulae;
9. internal roles/permissions/segregation of duties;
10. external KYC/e-signature/messaging/banking providers;
11. retention/privacy requirements;
12. controlled correction/override rules.

Azure selection does not resolve these business/legal operating-model questions.

## 9. Immediate delivery recommendation

The next delivery objective should be **Foundation Slice A — deployable authenticated platform shell**.

Definition:

```text
React/Vite frontend
    -> Azure Static Web Apps
    -> Entra External ID
    -> protected Azure Functions API
    -> Azure SQL persistence baseline
    -> Key Vault / Managed Identity
    -> Application Insights / Azure Monitor
    -> CI/CD evidence
```

Acceptance evidence should prove:

- deployment is repeatable;
- a test investor can sign in;
- an unauthenticated request to a protected API fails closed;
- authenticated identity is available server-side;
- a protected API can read/write a non-financial test record to Azure SQL;
- secrets are not exposed to the browser/repository;
- requests and failures are traceable in telemetry;
- cost budget/alerts exist.

Only after this foundation is proven should the team complete the first business vertical slice across opportunity discovery and non-binding EOI.

## 10. Status conclusion

**Architecture:** `READY_WITH_ASSUMPTIONS` for MVP cloud implementation.  
**Cloud platform selection:** `CONFIRMED`.  
**Azure foundation workstream:** `READY_FOR_DEVELOPMENT`; deployment evidence not yet recorded.  
**Application implementation:** `PARTIALLY_READY` / prototype-heavy.  
**First vertical slice:** `READY_FOR_DEVELOPMENT` after foundation dependencies.  
**Regulated investment platform:** `PARTIALLY_READY`; critical business/legal/integration questions remain open.  
**Production:** `NOT_READY`.

No current evidence justifies changing any use case to `COMPLETE`.
