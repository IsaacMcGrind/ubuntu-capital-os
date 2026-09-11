# Ubuntu Capital OS — Azure MVP Platform Delivery Plan

> **Current Foundation decision — 2026-09-07:** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001`. The execution gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. This authorises governed start only; implementation, completion, business-use-case and production claims remain evidence-gated. Source: `SRC-020`.

**Status:** `READY_FOR_DEVELOPMENT`  
**Architecture decision:** `ARCH-ADR-001`  
**Purpose:** convert the chosen Azure MVP platform direction into evidence-gated delivery work without treating infrastructure selection as implementation completion.

## 1. Delivery objective

Build the smallest secure Azure foundation capable of supporting the first complete Ubuntu Capital vertical slice:

> authenticated investor discovers an opportunity and submits a **non-binding expression of interest**.

The foundation must prove deployability, authentication, protected backend execution, persistence, secrets handling, telemetry, cost governance and reproducible infrastructure before regulated or financial workflows are expanded.

### Governance boundary and start gate

`plan.md` remains the controlling implementation sequence. This Azure plan is a subordinate delivery plan and does not replace or close plan-required reconstruction outputs.

`GO-2026-09-05-FSA-001` is the effective bounded authority for `WP-AZ-001` through `WP-AZ-008` after the 2026-09-07 formal project-owner review. The governance chain remains `AGENT.md`, `plan.md`, and `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`; execution must follow governed dependency order, and all status promotions remain evidence-gated.

## 2. Delivery sequence

The sequence below is executable for the exact Foundation Slice A scope authorised by the project-owner revalidation of `GO-2026-09-05-FSA-001` on 2026-09-07 (`SRC-020`). It does not authorise production, broader scope, or `WP-AZ-009` through `WP-AZ-012`; material baseline, scope, risk, or non-waivable evidence changes require renewed readiness review.

| Order | Work package | Primary Azure capability | Main use-case dependency | Target status after evidence |
|---:|---|---|---|---|
| 1 | Azure subscription/resource baseline | Resource groups, RBAC, Cost Management | Cross-cutting | `COMPONENT_COMPLETE` |
| 2 | Frontend deployment | Static Web Apps | UC-PUB-001, UC-IAM-001 | `COMPONENT_COMPLETE` |
| 3 | Customer identity foundation | Entra External ID | UC-IAM-001/002/003 | `COMPONENT_COMPLETE` |
| 4 | Protected API foundation | Azure Functions | IAM + all protected use cases | `COMPONENT_COMPLETE` |
| 5 | Persistence foundation | Azure SQL | ONB, OPP, INV, PORT, ADMIN, AUD | `COMPONENT_COMPLETE` |
| 6 | Secrets/service identity | Key Vault + Managed Identity | Cross-cutting | `COMPONENT_COMPLETE` |
| 7 | Observability | Application Insights + Azure Monitor | AUD/OPS and all runtime flows | `COMPONENT_COMPLETE` |
| 8 | Reproducible infrastructure + CI/CD deployment evidence | IaC/declarative provisioning + GitHub Actions/Azure DevOps | Cross-cutting | `COMPONENT_COMPLETE` |
| 9 | Opportunity read model/API | Functions + SQL | UC-OPP-001/002/003 | `IN_DEVELOPMENT` |
| 10 | Non-binding EOI workflow | Functions + SQL | UC-INV-001 | `IN_DEVELOPMENT` |
| 11 | Audit evidence for first slice | SQL/storage + telemetry separation | UC-AUD-001 | `IN_DEVELOPMENT` |
| 12 | E2E acceptance evidence | deployed Azure environment | first vertical slice | `READY_FOR_ACCEPTANCE` |

Each sequence item has a one-to-one work-package ID below. Evidence must be recorded against the matching ID so that delivery cannot be skipped or attributed to the wrong package.

`WP-AZ-003` work-package completion is distinct from the broader `UC-IAM-001` use-case status. The Entra External ID foundation can become `COMPONENT_COMPLETE` when its own package evidence gate is satisfied. `UC-IAM-001` retains an `IN_DEVELOPMENT` historical snapshot label for traceability, while current reproducible verification remains `BLOCKED_BY_CONTEXT` until backend enforcement, application integration and E2E evidence are complete.

Azure Blob Storage remains selected by `ARCH-ADR-001` for documents/generated files but is intentionally not a Foundation Slice A work package. It is deferred until a business slice requires controlled document or generated-file storage; its omission from `WP-AZ-001` through `WP-AZ-008` is not a reversal of the architecture decision and is not implementation evidence.

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
- no credential handling is implemented directly in Ubuntu Capital application code;
- identity-foundation configuration and tests are reproducible and documented.

**Work-package status rule**
- when the current Foundation start gate has been satisfied, the formal readiness decision authorizes the work, and the evidence above is present, `WP-AZ-003` may reach `COMPONENT_COMPLETE`;
- this does **not** by itself move `UC-IAM-001` to `COMPLETE`.

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

**Scope rule**
- `WP-AZ-007` proves operational observability only;
- it does not satisfy `UC-AUD-001` business-audit requirements or replace the Phase 5 business audit-event framework or `WP-AZ-011` slice audit evidence.

### WP-AZ-008 — Reproducible infrastructure and CI/CD deployment evidence

**Deliverables**
- version-controlled infrastructure-as-code or equivalent declarative provisioning definitions for Foundation Slice A resources that are reasonably automatable;
- repeatable provisioning/reconciliation workflow capable of creating a clean DEV/MVP foundation or reconciling drift against declared state;
- repeatable application build, test and deployment workflow;
- environment-specific configuration handled outside committed secrets;
- deployment result linked to the application revision and infrastructure-definition revision that produced it;
- failure paths that prevent failed infrastructure validation, build or test from being treated as a successful deployment;
- documented and justified manual Azure steps where automation is not practical, with no material untracked Foundation state.

**Evidence gate**
- version-controlled provisioning definitions exist for Foundation resources;
- successful clean provision or reconciliation run is evidenced;
- infrastructure validation/plan output is recorded with sensitive values redacted where required;
- successful application workflow run contains build/test/deploy steps;
- failed infrastructure or application validation demonstrably blocks deployment;
- deployed application and infrastructure state can be traced back to repository revisions;
- deployment credentials use an approved service identity/connection and are not committed to the repository;
- reconstruction/operational notes are recorded for any unavoidable manual step.

### WP-AZ-009 — Opportunity API

**Start prerequisite**  
Do not start or advance this package until Foundation Slice A is evidenced, the current readiness position and formal readiness conditions permit progression, the full first-business-slice integrity gate in `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` and `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md` is satisfied, and the `plan.md` Phase 5 **shared** foundational product capabilities and exit criteria required by Phase 6 are complete and evidenced. Phase 5 does not require the catalogue/API produced by this package; `WP-AZ-009` is the Phase 6 delivery unit that implements that business capability after the shared-capability handoff.

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

**Start prerequisite**  
Do not start or advance this package until Foundation Slice A is evidenced, the current readiness position and formal readiness conditions permit progression, the full first-business-slice integrity gate is satisfied, and the `plan.md` Phase 5 foundational product capabilities and exit criteria required by Phase 6 are complete and evidenced.

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

**Start prerequisite**  
Do not start or advance this package until Foundation Slice A is evidenced, the current readiness position and formal readiness conditions permit progression, the full first-business-slice integrity gate is satisfied, and the `plan.md` Phase 5 foundational product capabilities and exit criteria — including the shared business audit-event framework — are complete and evidenced.

**Deliverables**
- concrete business audit events for authentication-sensitive and EOI actions produced through the pre-existing Phase 5 audit-event framework;
- actor, action, resource, timestamp, outcome and correlation references;
- separation between business audit evidence and operational telemetry;
- authorised review/query path for the captured audit records.

**Evidence gate**
- successful and denied first-slice actions create the required audit records;
- records can be correlated to the originating request without exposing credentials/tokens;
- audit evidence persists independently of transient application logs;
- authorised reviewer can retrieve the relevant evidence for the acceptance scenario.

### WP-AZ-012 — E2E acceptance evidence

**Start prerequisite**  
Do not start or advance this package until Foundation Slice A is evidenced, the current readiness position and formal readiness conditions permit progression, the full first-business-slice integrity gate is satisfied, and the `plan.md` Phase 5 foundational product capabilities and exit criteria required by Phase 6 are complete and evidenced.

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

## 4. Foundation Slice A completion rule

Foundation Slice A consists of `WP-AZ-001` through `WP-AZ-008`.

Foundation execution can begin only after the current pre-implementation gate is satisfied and a formal `GO` or explicitly scoped `CONDITIONAL_GO` authorizes the applicable work. After that, Foundation Slice A as a whole may be described as `COMPONENT_COMPLETE` only when:

1. every Foundation work package has satisfied its own evidence gate and reached `COMPONENT_COMPLETE`;
2. `WP-AZ-003` identity-foundation completion is not confused with completion of `UC-IAM-001`;
3. the Azure Foundation can be recreated or reconciled from version-controlled provisioning definitions plus explicitly documented unavoidable manual steps;
4. application deployment is repeatable and blocked by failed infrastructure validation, build or test;
5. the resulting infrastructure/application revisions and evidence references reconcile in `docs/09-delivery/foundation-slice-a-evidence-register.md`.

This completion rule does not promote any business use case to `COMPLETE` and does not by itself authorize `WP-AZ-009` through `WP-AZ-012`; their separate start gate and the controlling Phase 5 foundational product-capability exit criteria must also be satisfied.

## 5. Deferred services and scoped deferrals

Azure Blob Storage is a **selected-but-deferred capability**, not an unselected service. Its implementation is deferred from Foundation Slice A until a business slice requires document/generated-file storage and can define the necessary access, retention and evidence rules.

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

## 6. Environment strategy

MVP baseline:

```text
LOCAL DEVELOPMENT
      -> AZURE DEV/MVP
      -> PRODUCTION when production controls are justified
```

Additional QA/SIT/UAT/staging environments are introduced only when the delivery and approval model requires them.

## 7. Delivery roles and ownership

Under `SRC-021`, the repository records distinct responsibilities:

- 80K Developers Project Manager capacity: accountable repository analysis, canonical requirements/architecture/evidence/status reconciliation, priority and gate recommendations;
- Thembinkosi Mtsweni: responsible human Project Manager and final project-owner decision authority;
- 80K Developers technical capacity: historical/partial application-prototype evidence and any explicitly assigned future implementation evidence, reviewed like other contractor evidence;
- HerLogic Solutions: technical Azure cloud architecture, cost and infrastructure-delivery evidence;
- Corefinity: technical architecture-analysis contribution evidence.

Technical contractor provenance does not grant independent authority to accept evidence, change business/legal requirements, adopt architecture, promote status, approve gates or authorise subsequent work.

## 8. First-slice start and exit criteria

`WP-AZ-009` through `WP-AZ-012` must not start or advance until:

1. Foundation Slice A has satisfied its evidence gates;
2. the current readiness decision continues to permit progression;
3. the first-slice outputs required by `plan.md` and the current reassessment reconcile, including actor/permission evidence, business rules, journey/state definitions, relevant integration/validation records, backlog/tracker/traceability, and risk/open-question linkage; and
4. the `plan.md` Phase 5 foundational product capabilities and exit criteria required before Phase 6 are complete and objectively evidenced.

The Phase 5 gate includes only the shared capabilities the first slice relies on: authentication/session handling, role/permission enforcement, investor identity baseline, shared validation and safe errors, protected API bootstrap/authorization testing, business audit-event framework, structured logging/correlation, persistence migrations, test harness/CI quality gates, and environment/secrets strategy. Before Phase 6 starts, evidence must show that an authorised test investor can authenticate, establish a server-validated session, and call a protected bootstrap/authorization test surface; unauthenticated, insufficient-role, and cross-user access must be denied and tested; and failures must produce safe errors with traceable logs. The opportunity read model, seed/test data, access policy enforcement, and permitted catalogue API are `WP-AZ-009` deliverables and are therefore not prerequisites for starting `WP-AZ-009`.

The first business slice may move to `READY_FOR_ACCEPTANCE` only when all of the following are evidenced in the deployed target environment:

1. authorised test investor authenticates through the selected identity architecture;
2. protected API rejects unauthenticated access;
3. investor can obtain permitted opportunity catalogue/detail data from the backend;
4. investor can submit a non-binding EOI;
5. EOI is persisted with stable status and duplicate protection;
6. operator access is authorised and scoped;
7. business audit evidence is created independently of operational telemetry through the established audit-event framework;
8. runtime requests/failures are observable;
9. automated tests cover positive and mandatory negative paths;
10. CI/CD deployment reference exists;
11. no unresolved critical question invalidates the non-binding interpretation;
12. captured E2E evidence is linked into the delivery tracker/traceability model.

## 9. Next action

1. Preserve the completed prerequisite reconciliation and effective 2026-09-07 revalidation of `GO-2026-09-05-FSA-001`; reopen it only for a material baseline, scope, risk, or non-waivable evidence change.
2. Execute only the permitted **WP-AZ-001 through WP-AZ-008** subset using `docs/09-delivery/foundation-slice-a-execution-package.md`; source-dependent packages require a pinned application branch and commit.
3. Require technical contractors to capture objective, sanitised and revision-pinned first-pass evidence only in their contractor folders as implementation/testing work is produced.
4. Review and merge technical evidence as provenance only.
5. Require the 80K Developers Project Manager workstream to separately assess merged evidence and, when accepted, link it into `docs/09-delivery/foundation-slice-a-evidence-register.md`, maintain planned-to-realised traceability, and reconcile status through a distinct `PROJECT_MANAGER_GOVERNANCE` PR only when each work-package evidence gate is satisfied.
6. Keep downstream scope controls in place: `WP-AZ-009` through `WP-AZ-012` remain blocked until Foundation evidence gates and first-slice start-gate prerequisites are satisfied.
7. If critical contradictions or non-waivable integrity failures emerge during execution, pause affected scope and issue a governance review update before status promotion.
8. Reconcile all Foundation evidence gates.
9. Complete and evidence the `plan.md` Phase 5 foundational product capabilities and its exit criteria.
10. Confirm the separate first-business-slice start gate is fully satisfied.
11. Only then start or advance **WP-AZ-009 through WP-AZ-012** as Phase 6 business-slice work.
12. Do not consider the first slice `READY_FOR_ACCEPTANCE` until its business-audit, E2E, tracker and traceability evidence reconciles.
