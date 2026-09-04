# Ubuntu Capital OS — Foundation Slice A Evidence Register

**Scope:** `WP-AZ-001` through `WP-AZ-008`  
**Delivery package status:** `IN_DEVELOPMENT`  
**Execution gate:** `AUTHORISED_GO` via `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`  
**Execution package:** `docs/09-delivery/foundation-slice-a-execution-package.md`  
**Governance reconciliation:** `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`  
**Current readiness decision:** `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`

The 2026-08-30 governance reconciliation remains part of the controlling compatibility chain. Foundation execution is now authorised for `WP-AZ-001` through `WP-AZ-008` under `GO-2026-09-05-FSA-001` with scope and condition controls defined in `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`.

## Evidence handling rules

- Do not record passwords, client secrets, bearer tokens, private keys or full connection strings.
- Redact subscription, tenant, application or resource identifiers where disclosure is not required for project traceability.
- Every record must state exactly what the evidence proves and what it does **not** prove.
- Evidence classification must use `CONFIRMED`, `INFERRED`, `UNKNOWN` or `CONTRADICTED`.
- Architecture/design documents are not implementation evidence unless the record explicitly says the evidence only proves design intent.
- External evidence links must be stable enough for an authorised project reviewer to retrieve later.
- Foundation execution is authorised only for the exact scope in `GO-2026-09-05-FSA-001`; no unlisted work package is authorised by this register.
- Capture objective realised implementation, test/run, deployment and operational evidence here as it is produced. Evidence capture documents authorised work; it does not by itself promote delivery status.
- After the start gate is satisfied, a work package cannot move to `COMPONENT_COMPLETE` until its required evidence gate is reconciled here or in an explicitly linked canonical evidence artifact and the governed status transition is recorded.
- `WP-AZ-008` requires version-controlled infrastructure provisioning/reconciliation evidence; manual Azure configuration alone cannot satisfy the Foundation reproducibility gate.

## Register

| Evidence ID | Work package | Evidence type | Reference / location | Captured date | Owner | Classification | Proves | Does not prove | Review status |
|---|---|---|---|---|---|---|---|---|---|
| FSA-EV-000 | WP-AZ-001 to WP-AZ-008 | Readiness decision evidence | `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md` | 2026-09-05 | Project Owner | `CONFIRMED` | Foundation execution gate is open for the authorised scope in AZURE DEV/MVP | Completion of any work-package evidence gate or any business use-case completion | ACCEPTED |
| FSA-EV-001 | WP-AZ-001 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Azure resource baseline evidence | Provisioning, RBAC or cost controls | OPEN |
| FSA-EV-002 | WP-AZ-002 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Static Web Apps deployment evidence | Successful deployment | OPEN |
| FSA-EV-003 | WP-AZ-003 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Entra External ID evidence | Authentication integration | OPEN |
| FSA-EV-004 | WP-AZ-004 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for protected Functions API evidence | Server-side access enforcement | OPEN |
| FSA-EV-005 | WP-AZ-005 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Azure SQL evidence | Persistence implementation | OPEN |
| FSA-EV-006 | WP-AZ-006 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Key Vault/Managed Identity evidence | Runtime secret/service-identity integration | OPEN |
| FSA-EV-007 | WP-AZ-007 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Application Insights/Azure Monitor evidence | Runtime observability or business audit | OPEN |
| FSA-EV-008 | WP-AZ-008 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for reproducible infrastructure + CI/CD evidence | Infrastructure reconstruction/reconciliation or repeatable gated deployment | OPEN |

## Work-package evidence checklist

The checklists below become executable evidence gates only after the current Foundation start gate is satisfied by the controlling governance chain and formal readiness decision.

### WP-AZ-001 — Azure baseline

Required before `COMPONENT_COMPLETE`:
- [ ] resource inventory/export/CLI evidence;
- [ ] resource-group/environment model;
- [ ] RBAC ownership evidence;
- [ ] naming/tagging evidence;
- [ ] Azure Cost Management budget evidence;
- [ ] cost-alert evidence;
- [ ] deployment identity/service connection approach documented;
- [ ] secrets exposure check.

### WP-AZ-002 — Static Web Apps frontend

Required before `COMPONENT_COMPLETE`:
- [ ] successful clean build;
- [ ] successful Azure deployment;
- [ ] Azure-hosted URL;
- [ ] route smoke tests;
- [ ] deployed commit SHA/PR reference;
- [ ] environment configuration separation verified.

### WP-AZ-003 — Entra External ID

Required before `COMPONENT_COMPLETE` for the **work package**:
- [ ] customer identity configuration evidence;
- [ ] frontend sign-in integration evidence;
- [ ] successful valid-investor sign-in test;
- [ ] invalid/unauthenticated test;
- [ ] backend token/principal validation contract;
- [ ] confirmation application code does not handle user credentials directly.

`WP-AZ-003` completion does not by itself make `UC-IAM-001` complete; the broader authentication use case remains governed by protected backend enforcement and E2E evidence.

### WP-AZ-004 — Protected Azure Functions API

Required before `COMPONENT_COMPLETE`:
- [ ] versioned API deployment evidence;
- [ ] unauthenticated denial test;
- [ ] authenticated principal resolution test;
- [ ] safe error/correlation contract evidence;
- [ ] health endpoint evidence;
- [ ] runtime failure telemetry reference.

### WP-AZ-005 — Azure SQL persistence

Required before `COMPONENT_COMPLETE`:
- [ ] schema/migration evidence;
- [ ] repeatable migration execution;
- [ ] write/read integration test;
- [ ] secure connectivity evidence;
- [ ] business-state ownership documented;
- [ ] verification that document binaries/telemetry are not incorrectly stored as business relational state.

### WP-AZ-006 — Key Vault and Managed Identity

Required before `COMPONENT_COMPLETE`:
- [ ] Key Vault inventory with sensitive values redacted;
- [ ] Managed Identity evidence where supported;
- [ ] least-privilege access assignment evidence;
- [ ] deployed runtime access test;
- [ ] confirmation that client/repository code contains no required backend secrets.

### WP-AZ-007 — Application Insights and Azure Monitor

Required before `COMPONENT_COMPLETE`:
- [ ] successful request trace;
- [ ] dependency trace where applicable;
- [ ] exception trace;
- [ ] material alert-rule evidence;
- [ ] telemetry retention/cost configuration;
- [ ] sensitive-data logging review.

`WP-AZ-007` proves operational observability only. It does not satisfy `UC-AUD-001` and does not replace the business-audit evidence required by `WP-AZ-011`.

### WP-AZ-008 — Reproducible infrastructure and CI/CD deployment evidence

Required before `COMPONENT_COMPLETE`:
- [ ] version-controlled infrastructure-as-code or equivalent declarative provisioning definitions for Foundation resources;
- [ ] successful clean provision or reconciliation run for the Azure DEV/MVP Foundation;
- [ ] infrastructure validation/plan evidence;
- [ ] successful application build/test/deploy workflow run;
- [ ] failed infrastructure or application validation shown to block deployment;
- [ ] deployed application revision traceability;
- [ ] infrastructure-definition revision traceability;
- [ ] approved service identity/connection evidence;
- [ ] no committed deployment credential;
- [ ] deployment, reconstruction/reconciliation and rollback operational notes;
- [ ] any unavoidable manual Azure steps explicitly documented and justified.

## Foundation Slice A acceptance summary

| Work package | Recorded delivery status | Execution gate | Evidence gate satisfied? | Evidence IDs | Notes |
|---|---|---|---:|---|---|
| WP-AZ-001 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-001 | Authorised to start and record realised evidence |
| WP-AZ-002 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-002 | Authorised to start and record realised evidence |
| WP-AZ-003 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-003 | UC-IAM-001 remains independently governed for use-case completion |
| WP-AZ-004 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-004 | Authorised to start and record realised evidence |
| WP-AZ-005 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-005 | Authorised to start and record realised evidence |
| WP-AZ-006 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-006 | Authorised to start and record realised evidence |
| WP-AZ-007 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-007 | Operational telemetry scope remains distinct from business audit scope |
| WP-AZ-008 | `IN_DEVELOPMENT` | `AUTHORISED_GO` | No | FSA-EV-008 | Reproducibility/CI-CD evidence required before completion |

**Foundation Slice A package:** `IN_DEVELOPMENT`.  
**Foundation Slice A execution gate:** `AUTHORISED_GO` via `GO-2026-09-05-FSA-001` — `WP-AZ-001` through `WP-AZ-008` may start and advance within authorised scope, and progress must be recorded here with objective realised evidence. No infrastructure implementation completion is claimed.
