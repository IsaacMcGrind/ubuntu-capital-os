# Ubuntu Capital OS — Azure MVP Platform Delivery Plan

**Status:** `READY_FOR_DEVELOPMENT`  
**Architecture decision:** `ARCH-ADR-001`  
**Purpose:** convert the chosen Azure MVP platform direction into evidence-gated delivery work without treating infrastructure selection as implementation completion.

## 1. Delivery objective

Build the smallest secure Azure foundation capable of supporting the first complete Ubuntu Capital vertical slice:

> authenticated investor discovers an opportunity and submits a **non-binding expression of interest**.

The foundation must prove deployability, authentication, protected backend execution, persistence, secrets handling, telemetry, and cost governance before regulated or financial workflows are expanded.

## 2. Delivery sequence

| Order | Work package | Primary Azure capability | Main use-case dependency | Target status after evidence |
|---:|---|---|---|---|
| 1 | Azure subscription/resource baseline | Resource groups, RBAC, Cost Management | Cross-cutting | `COMPONENT_COMPLETE` |
| 2 | Frontend deployment | Static Web Apps | UC-PUB-001, UC-IAM-001 | `COMPONENT_COMPLETE` |
| 3 | Customer identity foundation | Entra External ID | UC-IAM-001/002/003 | `IN_DEVELOPMENT` |
| 4 | Protected API foundation | Azure Functions | IAM + all protected use cases | `COMPONENT_COMPLETE` |
| 5 | Persistence foundation | Azure SQL | ONB, OPP, INV, PORT, ADMIN, AUD | `COMPONENT_COMPLETE` |
| 6 | Secrets/service identity | Key Vault + Managed Identity | Cross-cutting | `COMPONENT_COMPLETE` |
| 7 | Observability | Application Insights + Azure Monitor | AUD/OPS and all runtime flows | `COMPONENT_COMPLETE` |
| 8 | CI/CD deployment evidence | GitHub Actions/Azure DevOps | Cross-cutting | `COMPONENT_COMPLETE` |
| 9 | Opportunity read model/API | Functions + SQL | UC-OPP-001/002/003 | `IN_DEVELOPMENT` |
| 10 | Non-binding EOI workflow | Functions + SQL | UC-INV-001 | `IN_DEVELOPMENT` |
| 11 | Audit evidence for first slice | SQL/storage + telemetry separation | UC-AUD-001 | `IN_DEVELOPMENT` |
| 12 | E2E acceptance evidence | deployed Azure environment | first vertical slice | `READY_FOR_ACCEPTANCE` |

Each sequence item has a one-to-one work-package ID below. Evidence must be recorded against the matching ID so that delivery cannot be skipped or attributed to the wrong package.

## 3. Work-package evidence gates

### WP-AZ-001 — Azure baseline

**Deliverables**
- resource-group/environment model;
- naming/tagging convention;
- RBAC ownership;
- budget and cost alerts;
- deployment identity/service connection.

**Evidence gate**
- resource inventory screenshot/export or CLI output;
- budget configuration evidence;
- no production secrets in repository/client code.

### WP-AZ-002 — Static Web Apps frontend

**Deliverables**
- React/Vite build deployed to Static Web Apps;
- environment configuration separated from source;
- deployment linked to CI/CD.

**Evidence gate**
- successful build/deploy run;
- reachable Azure-hosted URL;
- smoke test of core routes.

### WP-AZ-003 — Entra External ID

**Deliverables**
- customer identity tenant/configuration;
- Ubuntu Capital app registration/configuration;
- sign-in path integrated with frontend;
- server-side token/principal validation design.

**Evidence gate**
- valid test investor can authenticate;
- invalid/unauthenticated access fails;
- protected API cannot rely on frontend route protection alone;
- no credential handling is implemented directly in Ubuntu Capital application code.

### WP-AZ-004 — Azure Functions API foundation

**Deliverables**
- versioned API structure;
- correlation ID/error contract;
- authentication enforcement middleware/pattern;
- health endpoint;
- deployment pipeline.

**Evidence gate**
- unauthenticated protected request returns safe denial;
- authenticated request resolves the caller identity server-side;
- application failure appears in telemetry with correlation data.

### WP-AZ-005 — Azure SQL persistence

**Deliverables**
- initial relational schema aligned to accepted logical ownership;
- migration strategy;
- secure connection through managed configuration/identity where practical;
- repository/service abstraction sufficient for first slice.

**Evidence gate**
- migration output;
- integration test writing/reading a non-financial test record;
- database is not used for document binaries or telemetry logs;
- business state ownership remains explicit.

### WP-AZ-006 — Key Vault and Managed Identity

**Deliverables**
- Key Vault for required secrets/configuration;
- Managed Identity for supported Azure resource access;
- least-privilege access assignments.

**Evidence gate**
- no secret exposed to client code;
- deployed Function can access required resource without embedded credential;
- access assignments are documented.

### WP-AZ-007 — Application Insights and Azure Monitor

**Deliverables**
- request, dependency, exception and availability telemetry;
- alerts for material runtime failures;
- minimal-retention/cost-conscious configuration.

**Evidence gate**
- test request trace;
- test exception trace;
- alert or alert-rule evidence;
- telemetry contains no credentials/tokens/sensitive payloads.

### WP-AZ-008 — CI/CD deployment evidence

**Deliverables**
- repeatable build, test and deployment workflow for the selected Azure MVP resources;
- environment-specific configuration handled outside committed secrets;
- deployment result linked to the repository revision that produced it;
- failure path that prevents a failed build/test from being treated as a successful deployment.

**Evidence gate**
- successful workflow run with build/test/deploy steps;
- failed validation demonstrably blocks deployment;
- deployed revision can be traced back to a commit/PR;
- deployment credentials use an approved service identity/connection and are not committed to the repository.

### WP-AZ-009 — Opportunity API

**Deliverables**
- canonical opportunity read model;
- server-side filtering/sorting contract where required;
- access policy enforcement;
- seed/test data separate from production source-of-truth assumptions.

**Evidence gate**
- UC-OPP-001/002/003 API tests;
- unavailable/restricted opportunity test;
- traceable request-to-data evidence.

### WP-AZ-010 — Non-binding expression of interest

**Deliverables**
- EOI endpoint/workflow;
- validation;
- idempotency/duplicate protection;
- persisted status;
- authorised operator read access;
- audit event.

**Evidence gate**
- valid EOI succeeds;
- duplicate/repeated action is safely handled;
- unauthorised user is denied;
- invalid input is rejected;
- database failure is safely surfaced/recoverable;
- action remains explicitly non-binding.

### WP-AZ-011 — Audit evidence for first slice

**Deliverables**
- business audit events for authentication-sensitive and EOI actions;
- actor, action, resource, timestamp, outcome and correlation references;
- separation between business audit evidence and operational telemetry;
- authorised review/query path for the captured audit records.

**Evidence gate**
- successful and denied first-slice actions create the required audit records;
- records can be correlated to the originating request without exposing credentials/tokens;
- audit evidence persists independently of transient application logs;
- authorised reviewer can retrieve the relevant evidence for the acceptance scenario.

### WP-AZ-012 — E2E acceptance evidence

**Deliverables**
- deployed-environment E2E scenario for the first vertical slice;
- positive and mandatory negative-path test evidence;
- traceability links from use case to implementation, deployment, test and evidence artifacts;
- acceptance package suitable for a human readiness decision.

**Evidence gate**
- authorised investor can authenticate, discover permitted opportunity data and submit a non-binding EOI end to end;
- unauthorised, duplicate, invalid, unavailable-opportunity and backend-failure scenarios are evidenced;
- persistence, audit, telemetry and deployment references reconcile to the tested revision;
- no unresolved critical question invalidates the non-binding first-slice interpretation;
- evidence is linked into the delivery tracker/traceability model before `READY_FOR_ACCEPTANCE` is considered.

## 4. Deferred services

Do not add the following until a measured/validated requirement exists:

- AKS;
- dedicated VMs;
- Premium Functions;
- large App Service plans;
- Service Bus;
- Redis;
- API Management;
- Front Door;
- premium networking/private endpoints everywhere;
- multi-region deployment;
- geo-redundant storage.

## 5. Environment strategy

MVP baseline:

```text
LOCAL DEVELOPMENT
      -> AZURE DEV/MVP
      -> PRODUCTION when production controls are justified
```

Additional QA/SIT/UAT/staging environments are introduced only when the delivery and approval model requires them.

## 6. Delivery roles and ownership

The repository currently records distinct responsibilities:

- Ubuntu Capital OS: authoritative requirements, architecture boundaries, evidence gates and delivery status;
- 80K Developers implementation evidence: current application/prototype delivery provenance;
- HerLogic Solutions: Azure cloud architecture/cost workstream and practical Azure implementation learning path;
- Corefinity: architecture-analysis contribution provenance where recorded.

Contractor provenance does not grant independent authority to change business/legal requirements or mark use cases complete.

## 7. First-slice exit criteria

The first business slice may move to `READY_FOR_ACCEPTANCE` only when all of the following are evidenced in the deployed target environment:

1. authorised test investor authenticates through the selected identity architecture;
2. protected API rejects unauthenticated access;
3. investor can obtain permitted opportunity catalogue/detail data from the backend;
4. investor can submit a non-binding EOI;
5. EOI is persisted with stable status and duplicate protection;
6. operator access is authorised and scoped;
7. audit evidence is created;
8. runtime requests/failures are observable;
9. automated tests cover positive and mandatory negative paths;
10. CI/CD deployment reference exists;
11. no unresolved critical question invalidates the non-binding interpretation;
12. captured E2E evidence is linked into the delivery tracker/traceability model.

## 8. Next action

Start with **WP-AZ-001 through WP-AZ-008** as Foundation Slice A, then implement **WP-AZ-009 and WP-AZ-010** as the first business vertical slice. Complete **WP-AZ-011 and WP-AZ-012** before the slice is considered for `READY_FOR_ACCEPTANCE`.
