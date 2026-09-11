# Ubuntu Capital OS — Foundation Slice A Execution Package

> **Current Foundation decision — 2026-09-07:** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001`. The scope gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. This approves the bounded scope for assignment; technical start also requires a durable Project Manager contractor/package/path assignment. Implementation, completion, business-use-case and production claims remain evidence-gated. Source: `SRC-020`.

**Status:** `READY_FOR_DEVELOPMENT`  
**Scope gate:** `OPEN_FOR_AUTHORISED_EXECUTION`; `GO-2026-09-05-FSA-001` was revalidated on 2026-09-07  
**Contractor start gate:** `BLOCKED_PENDING_ASSIGNMENT`; no exact executor/package/path assignment is recorded  
**Execution scope:** `WP-AZ-001` through `WP-AZ-008`  
**Architecture decision:** `ARCH-ADR-001`  
**Parent delivery plan:** `docs/09-delivery/azure-mvp-platform-delivery-plan.md`  
**Programme roadmap:** `docs/09-delivery/implementation-roadmap.md`  
**Governance reconciliation:** `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`  
**Current readiness decision:** `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`

## 1. Purpose

This package converts the approved Azure MVP platform direction into the bounded, currently authorised, evidence-gated Foundation Slice A delivery package.

Its purpose is to establish the smallest secure, deployable, observable and cost-governed Azure platform shell required before Ubuntu Capital implements the first complete business vertical slice.

Foundation Slice A does **not** make any Ubuntu Capital business use case `COMPLETE`. Its exit target is infrastructure/platform evidence sufficient to support the first business slice:

> authenticated investor discovers an opportunity and submits a **non-binding expression of interest**.

### Hard start gate

`GO-2026-09-05-FSA-001` records the exact Foundation scope authority. The project owner completed the formal post-prerequisite readiness review on 2026-09-07, but that scope-level GO does not assign an executor. No technical contractor may begin until the Project Manager records the contractor, exact package subset, authorised repository paths or bounded contractor subdirectory, evidence purpose, and applicable external implementation/resource scope.

`AGENT.md` and `plan.md` remain controlling. The 2026-08-30 governance reconciliation remains part of the compatibility chain, and `SRC-020` records that the controlling prerequisites reconciled and `GO-2026-09-05-FSA-001` became effective for the exact `WP-AZ-001` through `WP-AZ-008` Azure DEV/MVP scope on 2026-09-07. A material baseline, scope, risk, or non-waivable evidence change requires renewed readiness review; status promotion remains evidence-gated.

## 2. Governing evidence rules

The following rules are controlling:

1. `GO-2026-09-05-FSA-001` is the effective bounded scope authority for `WP-AZ-001` through `WP-AZ-008` after the 2026-09-07 formal review. Implementation may begin only after a durable Project Manager assignment identifies the executor, exact package subset, authorised paths, evidence purpose, and external implementation/resource scope.
2. Architecture selection is not implementation evidence.
3. A work package advances only when its evidence gate is satisfied.
4. No use case becomes `COMPLETE` without objective E2E evidence.
5. Secrets, credentials, tokens and sensitive payloads must not be committed to the repository or exposed to client code.
6. Every deployment result must be traceable to the repository revision that produced it.
7. Technical contractors store repository-hosted first-pass evidence only in their contractor folders. After merge as provenance, the 80K Developers Project Manager workstream separately assesses it and, when accepted, links it in `docs/09-delivery/foundation-slice-a-evidence-register.md` through a distinct `PROJECT_MANAGER_GOVERNANCE` change.
8. Any unresolved contradiction in ownership, status, IDs, evidence or environment configuration must be reconciled before progression.
9. Production-grade regulated transaction capability is outside this slice.
10. Foundation infrastructure must be reproducible from version-controlled provisioning definitions; manually configured Azure state alone cannot satisfy `WP-AZ-008` or the Foundation exit gate.
11. Foundation completion does not automatically authorise `WP-AZ-009` through `WP-AZ-012`; their separate first-business-slice start gate — including the controlling `plan.md` Phase 5 foundational product-capability exit criteria — must also be satisfied.

## 3. Foundation Slice A target architecture

```text
React / Vite frontend
        |
        v
Azure Static Web Apps
        |
        v
Microsoft Entra External ID
        |
        v
Protected Azure Functions API
        |
        +--> Azure SQL Database
        |
        +--> Azure Key Vault / Managed Identity
        |
        +--> Application Insights / Azure Monitor

CI/CD -> repeatable build/test/deploy -> Azure DEV/MVP
Infrastructure as code -> recreate/reconcile Foundation resources
Cost Management -> budgets / alerts / ownership
```

Azure Blob Storage remains selected by `ARCH-ADR-001` but is intentionally deferred outside Foundation Slice A until a business slice requires controlled document or generated-file storage.

## 4. Environment model

The initial execution model is intentionally small:

```text
LOCAL DEVELOPMENT
      -> AZURE DEV/MVP
      -> PRODUCTION only after production controls are justified
```

After the start gate is satisfied, the Azure DEV/MVP environment is the evidence environment for Foundation Slice A.

Additional QA, SIT, UAT or staging environments must not be introduced unless the delivery/approval model creates a measurable requirement for them.

## 5. Ownership and authority

### 80K Developers — Project Manager contractor

Under `SRC-021`, owns the accountable project-management workstream for:

- authoritative requirements and use-case status reconciliation;
- architecture-boundary and approved-decision maintenance;
- evidence-gate assessment;
- delivery readiness, priority and acceptance recommendations;
- traceability and integrity reconciliation;
- subsequent-work recommendations for Thembinkosi Mtsweni's human decision.

Thembinkosi Mtsweni is the responsible human Project Manager and final project-owner decision authority.

### HerLogic Solutions — technical Azure contractor

Recorded scope:

- Azure platform implementation workstream after the governance start gate is satisfied;
- practical Azure delivery and sanitised evidence capture;
- Azure cost-governance implementation;
- cloud deployment support within approved architecture.

HerLogic Solutions does not independently authorise execution, accept its own evidence, change legal/business rules, waive repository-integrity gates, promote canonical status or authorise subsequent work.

### Corefinity — technical architecture-analysis contractor

May provide architecture-analysis evidence within assigned scope. Its contribution is supporting evidence, not independent architecture adoption or project authority.

### 80K Developers — technical capacity

When 80K Developers performs application, integration, deployment or other implementation work, it uses `CONTRACTOR_TECHNICAL_EVIDENCE` capacity and is subject to the same evidence-only review as other contractors. Its technical work cannot self-promote status.

## 6. Execution sequence

The Foundation scope gate for the bounded `WP-AZ-001` through `WP-AZ-008` Azure DEV/MVP scope was satisfied by the project-owner revalidation recorded on 2026-09-07 (`SRC-020`). The execution sequence remains blocked until the Project Manager records an exact contractor/package/path assignment. Once assigned, it may execute only within that subset and dependency order; it does not authorise production or `WP-AZ-009` through `WP-AZ-012`.

| Order | Work package | Delivery objective | Target status after evidence | Primary dependency |
|---:|---|---|---|---|
| 1 | `WP-AZ-001` | Azure baseline | `COMPONENT_COMPLETE` | Foundation start gate |
| 2 | `WP-AZ-002` | Static Web Apps frontend | `COMPONENT_COMPLETE` | WP-AZ-001 |
| 3 | `WP-AZ-003` | Entra External ID foundation | `COMPONENT_COMPLETE` | WP-AZ-001/002 |
| 4 | `WP-AZ-004` | Protected Functions API | `COMPONENT_COMPLETE` | WP-AZ-003 |
| 5 | `WP-AZ-005` | Azure SQL persistence | `COMPONENT_COMPLETE` | WP-AZ-004 |
| 6 | `WP-AZ-006` | Key Vault + Managed Identity | `COMPONENT_COMPLETE` | WP-AZ-001/004/005 |
| 7 | `WP-AZ-007` | Application Insights + Azure Monitor | `COMPONENT_COMPLETE` | WP-AZ-004 |
| 8 | `WP-AZ-008` | Reproducible infrastructure + CI/CD deployment evidence | `COMPONENT_COMPLETE` | all Foundation resources and deployment targets |

`WP-AZ-003` work-package completion is distinct from the broader `UC-IAM-001` use-case status. The identity foundation may reach `COMPONENT_COMPLETE` when its own evidence gate is satisfied. `UC-IAM-001` retains an `IN_DEVELOPMENT` historical snapshot label for traceability, while current reproducible verification remains `BLOCKED_BY_CONTEXT` until protected backend enforcement, application integration and later E2E evidence reconcile.

Once the start gate is satisfied, work packages may overlap only where their stated dependencies and evidence integrity allow it.

## 7. Work-package execution cards

### WP-AZ-001 — Azure subscription and resource baseline

**Objective**  
Create a controlled Azure DEV/MVP baseline with explicit ownership, cost governance and deployment identity.

**Implementation tasks**
- confirm subscription and tenant to be used for the MVP;
- define resource-group model;
- define naming convention;
- define required tags such as environment, owner, system and cost centre/project;
- document RBAC ownership;
- configure Azure Cost Management budget and alert thresholds;
- define deployment identity/service connection strategy;
- record region selection and rationale;
- record resources that are intentionally not provisioned yet.

**Acceptance criteria**
- Azure DEV/MVP ownership is explicit;
- resource naming and tagging is documented and consistently applied;
- budget/alerts exist;
- deployment identity is separate from personal credentials where practical;
- no production secret exists in repository/client code.

**Required evidence**
- resource inventory export, screenshot or CLI output;
- subscription/resource-group identifiers with secrets redacted;
- RBAC summary;
- budget and alert evidence;
- naming/tagging record.

### WP-AZ-002 — Static Web Apps frontend deployment

**Objective**  
Deploy the current React/Vite application to an Azure-hosted DEV/MVP endpoint.

**Implementation tasks**
- confirm frontend build command/output directory;
- provision/configure Static Web Apps;
- separate runtime/environment configuration from source secrets;
- connect deployment to CI/CD;
- verify required application routes load correctly;
- document deployment URL and revision.

**Acceptance criteria**
- build succeeds from a clean checkout;
- deployment is repeatable;
- Azure-hosted URL is reachable;
- core public/authentication-entry routes pass smoke tests;
- deployed revision is traceable to commit/PR.

**Required evidence**
- successful workflow/build output;
- deployment URL;
- route smoke-test results;
- deployed commit SHA.

### WP-AZ-003 — Microsoft Entra External ID foundation

**Objective**  
Establish the selected customer identity foundation for Ubuntu Capital investor authentication.

**Implementation tasks**
- configure the selected Entra External ID tenant/customer identity setup;
- configure Ubuntu Capital application registration/settings;
- integrate the frontend sign-in path;
- define token/principal validation expectations for the backend;
- document redirect/origin configuration;
- define test identities and negative-path scenarios without storing credentials in repository files.

**Acceptance criteria**
- valid test investor can authenticate;
- invalid/unauthenticated flow fails safely;
- authentication is not treated as complete based only on frontend route protection;
- credential handling is delegated to the selected identity platform;
- configuration and tests required by this identity-foundation package are reproducible and documented.

**Required evidence**
- redacted configuration evidence;
- successful sign-in test result;
- failed/unauthenticated test result;
- identity-to-backend validation contract.

### WP-AZ-004 — Protected Azure Functions API foundation

**Objective**  
Create a backend execution boundary that enforces authentication server-side.

**Implementation tasks**
- establish versioned API structure;
- implement authentication/principal validation pattern;
- define standard error contract;
- implement correlation/request ID pattern;
- add health endpoint;
- add deployment configuration;
- add positive and negative API tests.

**Acceptance criteria**
- unauthenticated protected request is denied;
- authenticated request resolves caller identity server-side;
- errors are safe and traceable;
- runtime failures can be correlated to telemetry;
- API is deployable through the selected delivery process.

**Required evidence**
- API test results;
- denial response evidence;
- authenticated identity resolution evidence;
- health endpoint evidence;
- deployment reference.

### WP-AZ-005 — Azure SQL persistence foundation

**Objective**  
Create the minimum relational persistence capability required by later business slices.

**Implementation tasks**
- confirm first-slice data ownership boundaries;
- create initial schema/migrations;
- define migration execution process;
- configure secure application connectivity;
- implement minimal repository/service abstraction;
- add persistence integration tests;
- keep document binaries and operational telemetry out of the business relational store.

**Acceptance criteria**
- migration can be executed repeatably;
- test record can be written/read through application path;
- connection secrets are not embedded in client/repository code;
- business state ownership is documented.

**Required evidence**
- migration output;
- integration-test result;
- schema/version reference;
- redacted connectivity/configuration evidence.

### WP-AZ-006 — Key Vault and Managed Identity

**Objective**  
Remove embedded infrastructure credentials and establish least-privilege service identity.

**Implementation tasks**
- identify secrets/configuration requiring protected storage;
- configure Key Vault;
- configure Managed Identity where supported;
- assign least-privilege access;
- remove/deprecate embedded connection credentials;
- document access ownership and rotation/recovery expectations.

**Acceptance criteria**
- no required backend secret is exposed to client code;
- deployed backend can access required Azure resource without embedded credential where supported;
- access assignments are documented and reviewable.

**Required evidence**
- redacted Key Vault inventory;
- identity/access assignment evidence;
- successful runtime access evidence;
- repository secret-scan/manual verification result where available.

### WP-AZ-007 — Application Insights and Azure Monitor

**Objective**  
Make the DEV/MVP platform observable without logging sensitive data.

**Implementation tasks**
- configure request/dependency/exception telemetry;
- configure availability/smoke monitoring where justified;
- define minimum alerts for runtime failure;
- configure retention/cost-conscious settings;
- confirm token/credential/sensitive payload exclusion;
- document correlation between API requests and telemetry.

**Acceptance criteria**
- successful request trace is visible;
- test exception trace is visible;
- at least one material alert rule is evidenced;
- sensitive authentication material is not logged;
- telemetry can be correlated to application requests.

**Required evidence**
- request trace;
- exception trace;
- alert-rule evidence;
- telemetry redaction/safety verification.

**Scope rule**
- this package proves operational observability only;
- it does not satisfy `UC-AUD-001`, the `plan.md` Phase 5 business audit-event framework, or the business-audit evidence requirements of `WP-AZ-011`.

### WP-AZ-008 — Reproducible infrastructure and CI/CD deployment evidence

**Objective**  
Make Foundation Slice A reproducible from source control rather than dependent on manually reconstructed Azure state.

**Implementation tasks**
- define the Foundation Azure resources in version-controlled infrastructure-as-code or equivalent declarative provisioning definitions;
- include the resource-group baseline and all Foundation resources/configuration owned by `WP-AZ-001` and `WP-AZ-002` through `WP-AZ-007` that are reasonably automatable;
- implement a repeatable provisioning/reconciliation workflow that can create a clean DEV/MVP foundation or reconcile drift against the declared state;
- implement repeatable application build/test/deploy workflow;
- ensure failed infrastructure validation or failed application build/test prevents successful deployment classification;
- isolate environment configuration from committed secrets;
- use approved service identity/connection;
- record deployed revision and infrastructure-definition revision;
- document rollback/recovery approach appropriate for MVP scope.

**Acceptance criteria**
- version-controlled provisioning definitions exist for the Foundation Azure resources;
- an authorised contributor can provision a clean DEV/MVP foundation or reconcile an existing one from those definitions without relying on undocumented portal-only steps;
- infrastructure validation/plan and application build/test/deploy workflow evidence exists;
- intentionally failed infrastructure or application validation demonstrates deployment blocking;
- deployed application and provisioned infrastructure map to repository revisions;
- deployment credentials are not committed;
- any unavoidable manual Azure steps are explicitly documented, justified and cannot represent material untracked Foundation state.

**Required evidence**
- infrastructure-as-code/declarative provisioning path and revision;
- successful clean provision or reconciliation run reference;
- infrastructure validation/plan output with sensitive identifiers redacted where required;
- successful application workflow run link/reference;
- failed/blocking infrastructure or application workflow evidence;
- deployed application SHA/version and infrastructure-definition revision;
- service identity/connection evidence with secrets redacted;
- operational deployment and reconstruction notes.

## 8. Cross-cutting acceptance controls

Foundation Slice A cannot begin until its current readiness start gate is satisfied, and cannot be declared `COMPONENT_COMPLETE` as a whole unless:

- the formal readiness decision authorizes the applicable Foundation work;
- all eight work-package evidence records exist;
- all eight work packages individually satisfy their `COMPONENT_COMPLETE` evidence gates;
- no work package is advanced solely from design intent;
- deployment and identity configuration are reproducible/documented;
- Foundation Azure resources can be created or reconciled from version-controlled provisioning definitions, with any unavoidable manual steps explicitly documented and justified;
- cost governance is active;
- unauthenticated backend access is denied;
- persistence has objective integration evidence;
- secret handling and service identity are evidenced;
- runtime telemetry and failure visibility are evidenced;
- CI/CD maps deployed application and infrastructure state to source revisions;
- no unresolved critical repository-integrity contradiction remains.

## 9. Evidence storage and traceability contract

Technical contractors first record all repository-hosted factual, sanitised, revision-pinned evidence under their existing `contractors/<contractor>/` directory and do not modify canonical governance/status artifacts in the same PR. After review and merge as provenance, the 80K Developers Project Manager workstream separately assesses the merged evidence and, when accepted, reconciles metadata and stable references into:

`docs/09-delivery/foundation-slice-a-evidence-register.md`

The register must include a stable repository path or external URL, date captured, owner, related work-package ID, evidence classification, and what the evidence proves and does not prove. It should link to contractor evidence rather than duplicate sensitive or bulky raw material.

Sensitive Azure values must be redacted. Neither contractor folders nor the evidence register may contain passwords, client secrets, bearer tokens, connection strings, private keys or unnecessary infrastructure identifiers.

## 10. Status transition model

Default recorded status for `WP-AZ-001` through `WP-AZ-008` remains `READY_FOR_DEVELOPMENT` unless stronger evidence already exists and is reconciled into this repository.

The 2026-09-07 project-owner review completed the bounded start decision, so an authorised package may transition to `IN_DEVELOPMENT` only when objective start evidence is accepted through a separate `PROJECT_MANAGER_GOVERNANCE` reconciliation. No package may transition to `COMPONENT_COMPLETE` until its full evidence gate is accepted.

After those prerequisites reconcile, allowed transitions are:

```text
READY_FOR_DEVELOPMENT
        -> IN_DEVELOPMENT
        -> COMPONENT_COMPLETE
```

A work package must not skip directly to `COMPONENT_COMPLETE` without its evidence gate.

Work-package status and business use-case status are evaluated independently. In particular, `WP-AZ-003` may be `COMPONENT_COMPLETE` while `UC-IAM-001` retains only its historical `IN_DEVELOPMENT` snapshot label; current reproducible verification remains `BLOCKED_BY_CONTEXT` until the wider authentication use-case evidence is satisfied.

## 11. Handoff to the first business vertical slice

Foundation completion is necessary but not sufficient for handoff.

`WP-AZ-009`, `WP-AZ-010`, `WP-AZ-011`, and `WP-AZ-012` must not start or advance until:

1. Foundation Slice A evidence has been accepted;
2. the current readiness position and any formal readiness conditions still permit progression;
3. the full first-business-slice integrity gate in `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` and `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md` is satisfied, including permissions, rules, journey/state, integrations, backlog, E2E tracker, traceability, validation, and open-question/risk reconciliation; and
4. the `plan.md` Phase 5 foundational product capabilities and Phase 5 exit criteria required before Phase 6 are complete and objectively evidenced.

The Phase 5 prerequisite includes only the shared capabilities needed by the slice: authentication/session handling, role and permission enforcement, investor identity baseline, shared validation/safe error handling, protected API bootstrap/authorization testing, business audit-event framework, structured logging/correlation, persistence migrations, test harness/CI quality gates, and environment/secrets strategy. Its exit evidence must show that an authorised test investor can authenticate, establish a server-validated session, and call a protected bootstrap/authorization test surface; unauthenticated, insufficient-role, and cross-user access must be denied and tested; and failures must produce safe errors with traceable logs. The opportunity read model, seed/test data, access policy enforcement, and permitted catalogue API are owned by `WP-AZ-009` after this handoff and are not Phase 5 exit prerequisites.

Only after all conditions are true may the Phase 6 first slice proceed:

- `WP-AZ-009` — Opportunity API;
- `WP-AZ-010` — non-binding expression of interest;
- `WP-AZ-011` — concrete business-audit evidence produced through the established audit-event framework;
- `WP-AZ-012` — deployed E2E acceptance evidence.

The intended first E2E journey remains:

> authenticated investor -> permitted opportunity discovery/detail -> non-binding EOI -> persisted status -> audit + telemetry -> acceptance evidence.

## 12. Definition of done for this execution package

This documentation package is complete when:

1. execution scope `WP-AZ-001` to `WP-AZ-008` is explicit;
2. every package has objective tasks, acceptance criteria and evidence requirements;
3. ownership and authority boundaries are recorded;
4. environment and deployment expectations are recorded;
5. evidence storage and redaction rules are recorded;
6. roadmap and parent delivery-plan references reconcile;
7. Foundation reproducibility requirements are explicit and version-controlled infrastructure reconstruction is required before Foundation completion;
8. the current pre-implementation hard start gate explicitly includes the 2026-09-03 reassessment and formal readiness decision, and prevents work-package status progression while that gate remains blocked;
9. the separate first-business-slice gate explicitly blocks `WP-AZ-009` through `WP-AZ-012` from starting or advancing until the first-slice integrity prerequisites and the controlling `plan.md` Phase 5 foundational product-capability exit criteria reconcile;
10. no claim is made that Azure resources are already implemented without evidence.
