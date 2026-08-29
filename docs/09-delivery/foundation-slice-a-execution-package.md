# Ubuntu Capital OS — Foundation Slice A Execution Package

**Status:** `READY_FOR_DEVELOPMENT`  
**Execution scope:** `WP-AZ-001` through `WP-AZ-008`  
**Architecture decision:** `ARCH-ADR-001`  
**Parent delivery plan:** `docs/09-delivery/azure-mvp-platform-delivery-plan.md`  
**Programme roadmap:** `docs/09-delivery/implementation-roadmap.md`

## 1. Purpose

This package converts the approved Azure MVP platform direction into an executable, evidence-gated Foundation Slice A delivery package.

Its purpose is to establish the smallest secure, deployable, observable and cost-governed Azure platform shell required before Ubuntu Capital implements the first complete business vertical slice.

Foundation Slice A does **not** make any Ubuntu Capital business use case `COMPLETE`. Its exit target is infrastructure/platform evidence sufficient to support the first business slice:

> authenticated investor discovers an opportunity and submits a **non-binding expression of interest**.

## 2. Governing evidence rules

The following rules are controlling:

1. Architecture selection is not implementation evidence.
2. A work package advances only when its evidence gate is satisfied.
3. No use case becomes `COMPLETE` without objective E2E evidence.
4. Secrets, credentials, tokens and sensitive payloads must not be committed to the repository or exposed to client code.
5. Every deployment result must be traceable to the repository revision that produced it.
6. Evidence must be stored or linked in the Foundation Slice A evidence register.
7. Any unresolved contradiction in ownership, status, IDs, evidence or environment configuration must be reconciled before progression.
8. Production-grade regulated transaction capability is outside this slice.

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
Cost Management -> budgets / alerts / ownership
```

## 4. Environment model

The initial execution model is intentionally small:

```text
LOCAL DEVELOPMENT
      -> AZURE DEV/MVP
      -> PRODUCTION only after production controls are justified
```

The Azure DEV/MVP environment is the evidence environment for Foundation Slice A.

Additional QA, SIT, UAT or staging environments must not be introduced unless the delivery/approval model creates a measurable requirement for them.

## 5. Ownership and authority

### Ubuntu Capital OS

Owns:
- authoritative requirements and use-case status;
- architecture boundaries and approved decisions;
- evidence gates;
- delivery readiness and acceptance decisions;
- traceability and integrity reconciliation.

### HerLogic Solutions

Recorded scope:
- Azure platform implementation workstream;
- practical Azure delivery and evidence capture;
- Azure cost-governance implementation;
- cloud deployment support within approved architecture.

HerLogic Solutions does **not** have authority to change legal/business rules or mark Ubuntu Capital use cases complete.

### 80K Developers / implementation contributors

May provide application, integration, deployment and implementation evidence according to the approved work packages and repository governance.

## 6. Execution sequence

| Order | Work package | Delivery objective | Target status after evidence | Primary dependency |
|---:|---|---|---|---|
| 1 | `WP-AZ-001` | Azure baseline | `COMPONENT_COMPLETE` | none |
| 2 | `WP-AZ-002` | Static Web Apps frontend | `COMPONENT_COMPLETE` | WP-AZ-001 |
| 3 | `WP-AZ-003` | Entra External ID | `IN_DEVELOPMENT` | WP-AZ-001/002 |
| 4 | `WP-AZ-004` | Protected Functions API | `COMPONENT_COMPLETE` | WP-AZ-003 |
| 5 | `WP-AZ-005` | Azure SQL persistence | `COMPONENT_COMPLETE` | WP-AZ-004 |
| 6 | `WP-AZ-006` | Key Vault + Managed Identity | `COMPONENT_COMPLETE` | WP-AZ-001/004/005 |
| 7 | `WP-AZ-007` | Application Insights + Azure Monitor | `COMPONENT_COMPLETE` | WP-AZ-004 |
| 8 | `WP-AZ-008` | CI/CD deployment evidence | `COMPONENT_COMPLETE` | all deployment targets used by the slice |

The sequence may overlap where technically safe, but evidence gates must still reconcile before Foundation Slice A is considered complete.

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
- credential handling is delegated to the selected identity platform.

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

### WP-AZ-008 — CI/CD deployment evidence

**Objective**  
Make Foundation Slice A reproducible from source control rather than manually reconstructed Azure state.

**Implementation tasks**
- implement repeatable build/test/deploy workflow;
- ensure failed build/test prevents successful deployment classification;
- isolate environment configuration from committed secrets;
- use approved service identity/connection;
- record deployed revision;
- document rollback/recovery approach appropriate for MVP scope.

**Acceptance criteria**
- successful build/test/deploy workflow run exists;
- intentionally failed validation demonstrates deployment blocking;
- deployed revision maps to commit/PR;
- deployment credentials are not committed;
- another authorised contributor can understand the deployment process from repository documentation.

**Required evidence**
- successful workflow run link/reference;
- failed/blocking workflow evidence;
- deployed SHA/version;
- service identity/connection evidence with secrets redacted;
- operational deployment notes.

## 8. Cross-cutting acceptance controls

Foundation Slice A cannot be declared `COMPONENT_COMPLETE` as a whole unless:

- all eight work-package evidence records exist;
- no work package is advanced solely from design intent;
- deployment and identity configuration are reproducible/documented;
- cost governance is active;
- unauthenticated backend access is denied;
- persistence has objective integration evidence;
- secret handling and service identity are evidenced;
- runtime telemetry and failure visibility are evidenced;
- CI/CD maps deployed state to source revision;
- no unresolved critical repository-integrity contradiction remains.

## 9. Evidence storage and traceability contract

Evidence metadata is recorded in:

`docs/09-delivery/foundation-slice-a-evidence-register.md`

Where evidence lives outside this repository, the register must include a stable reference or URL, date captured, owner, related work-package ID, evidence classification and what the evidence proves.

Sensitive Azure values must be redacted. The evidence register must not contain passwords, client secrets, bearer tokens, connection strings or private keys.

## 10. Status transition model

Default starting status for `WP-AZ-001` through `WP-AZ-008` is `READY_FOR_DEVELOPMENT` unless stronger implementation evidence already exists and is reconciled into this repository.

Recommended transitions:

```text
READY_FOR_DEVELOPMENT
        -> IN_DEVELOPMENT
        -> COMPONENT_COMPLETE
```

A work package must not skip directly to `COMPONENT_COMPLETE` without its evidence gate.

Foundation Slice A completion does not advance the first business vertical slice to `COMPLETE`; it only establishes the platform prerequisites for `WP-AZ-009` onward.

## 11. Handoff to the first business vertical slice

After Foundation Slice A evidence is accepted, proceed to:

- `WP-AZ-009` — Opportunity API;
- `WP-AZ-010` — non-binding expression of interest;
- `WP-AZ-011` — business audit evidence;
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
7. no claim is made that Azure resources are already implemented without evidence.
