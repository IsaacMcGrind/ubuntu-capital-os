# Ubuntu Capital OS — Foundation Slice A Evidence Register

> **Current Foundation decision — 2026-09-07:** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001`. The scope gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. This approves the bounded scope for contractor self-selection; it does not allocate work. Implementation, completion, business-use-case and production claims remain evidence-gated. Source: `SRC-020`.

**Scope:** `WP-AZ-001` through `WP-AZ-008`  
**Delivery package status:** `READY_FOR_DEVELOPMENT`  
**Scope gate:** `OPEN_FOR_AUTHORISED_EXECUTION`; `GO-2026-09-05-FSA-001` was revalidated on 2026-09-07  
**Contractor start mode:** `OPEN_FOR_SELF_SELECTION`; no contractor selection declaration is recorded yet  
**Execution package:** `docs/09-delivery/foundation-slice-a-execution-package.md`  
**Governance reconciliation:** `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`  
**Current readiness decision:** `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`

The 2026-08-30 governance reconciliation remains part of the controlling compatibility chain. `GO-2026-09-05-FSA-001` is effective for `WP-AZ-001` through `WP-AZ-008` after the 2026-09-07 project-owner formal review. No realised execution evidence is recorded. The work packages remain `READY_FOR_DEVELOPMENT`; contractors may self-select work; each PR must declare its exact package/path scope, and status may change only after objective start evidence is accepted and canonically reconciled through a separate `PROJECT_MANAGER_GOVERNANCE` change.

## Evidence handling rules

- Under `SRC-021`, a `CONTRACTOR_TECHNICAL_EVIDENCE` PR must keep every repository-hosted first-pass evidence file under the submitting contractor's existing `contractors/<contractor>/` directory and must not modify this canonical register or another canonical governance/status artifact. Approved external raw evidence is represented by a sanitised stable reference in the contractor folder. 80K Developers (Pty) Ltd is the appointed Project Manager contractor; Thembinkosi Mtsweni is the responsible human Project Manager and final project-owner decision authority. After merge, the 80K Developers Project Manager workstream separately assesses the contractor evidence and reconciles accepted references into this register through a distinct `PROJECT_MANAGER_GOVERNANCE` update.
- Contractor evidence does not approve execution, change this register's review status, promote a work package, declare completion, redefine a gate, or authorise subsequent work.
- Do not record passwords, client secrets, bearer tokens, private keys or full connection strings.
- Redact subscription, tenant, application or resource identifiers where disclosure is not required for project traceability.
- Every record must state exactly what the evidence proves and what it does **not** prove.
- Evidence classification must use `CONFIRMED`, `INFERRED`, `UNKNOWN` or `CONTRADICTED`.
- Architecture/design documents are not implementation evidence unless the record explicitly says the evidence only proves design intent.
- External evidence links must be stable enough for an authorised project reviewer to retrieve later.
- The formal post-prerequisite review revalidated `GO-2026-09-05-FSA-001` on 2026-09-07. The scope-level GO applies only to that decision's exact scope; contractors may self-select work within it and must declare their exact package/path scope and evidence purpose in the PR. This register records accepted evidence references and does not broaden authority.
- After a contractor evidence PR is reviewed and merged as provenance, the 80K Developers Project Manager workstream separately assesses it. Only when accepted may its objective implementation, test/run, deployment and operational metadata or stable reference be recorded here through a distinct `PROJECT_MANAGER_GOVERNANCE` change. This reconciliation does not by itself promote delivery status.
- After the start gate is satisfied, a work package cannot move to `COMPONENT_COMPLETE` until its required evidence gate is reconciled here or in an explicitly linked canonical evidence artifact and the governed status transition is recorded.
- `WP-AZ-008` requires version-controlled infrastructure provisioning/reconciliation evidence; manual Azure configuration alone cannot satisfy the Foundation reproducibility gate.

## Register

| Evidence ID | Work package | Evidence type | Reference / location | Captured date | Owner | Classification | Proves | Does not prove | Review status |
|---|---|---|---|---|---|---|---|---|---|
| FSA-EV-000 | WP-AZ-001 to WP-AZ-008 | Readiness decision evidence | `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md` | 2026-09-05 | Project Owner | `CONFIRMED` | Records the bounded Foundation scope and decision authority as of 2026-09-05 | Post-reconciliation permission to start, completion of any work-package evidence gate, or any business use-case completion | ACCEPTED |
| FSA-EV-001 | WP-AZ-001 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Azure resource baseline evidence | Provisioning, RBAC or cost controls | OPEN |
| FSA-EV-002 | WP-AZ-002 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Static Web Apps deployment evidence | Successful deployment | OPEN |
| FSA-EV-003 | WP-AZ-003 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Entra External ID evidence | Authentication integration | OPEN |
| FSA-EV-004 | WP-AZ-004 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for protected Functions API evidence | Server-side access enforcement | OPEN |
| FSA-EV-005 | WP-AZ-005 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Azure SQL evidence | Persistence implementation | OPEN |
| FSA-EV-006 | WP-AZ-006 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Key Vault/Managed Identity evidence | Runtime secret/service-identity integration | OPEN |
| FSA-EV-007 | WP-AZ-007 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for Application Insights/Azure Monitor evidence | Runtime observability or business audit | OPEN |
| FSA-EV-008 | WP-AZ-008 | Planned evidence placeholder | Pending | Pending | Pending | `UNKNOWN` | Nothing yet; placeholder for reproducible infrastructure + CI/CD evidence | Infrastructure reconstruction/reconciliation or repeatable gated deployment | OPEN |

## Work-package evidence checklist

The checklists below became executable for the bounded `WP-AZ-001` through `WP-AZ-008` Azure DEV/MVP scope when the project owner formally revalidated `GO-2026-09-05-FSA-001` on 2026-09-07 (`SRC-020`). They do not authorise broader scope or status promotion.

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
- [ ] least-privilege access evidence;
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

| Work package | Recorded delivery status | Contractor start mode | Evidence gate satisfied? | Evidence IDs | Notes |
|---|---|---|---:|---|---|
| WP-AZ-001 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-001 | Scope available for self-selection; no accepted start evidence |
| WP-AZ-002 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-002 | Scope available for self-selection; no accepted start evidence |
| WP-AZ-003 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-003 | Scope available for self-selection; no accepted start evidence; UC-IAM-001 remains independently governed |
| WP-AZ-004 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-004 | Scope available for self-selection; no accepted start evidence |
| WP-AZ-005 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-005 | Scope available for self-selection; no accepted start evidence |
| WP-AZ-006 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-006 | Scope available for self-selection; no accepted start evidence |
| WP-AZ-007 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-007 | Scope available for self-selection; no accepted start evidence; telemetry remains distinct from business audit |
| WP-AZ-008 | `READY_FOR_DEVELOPMENT` | `OPEN_FOR_SELF_SELECTION` | No | FSA-EV-008 | Scope available for self-selection; no accepted start evidence; reproducibility evidence remains required |

**Foundation Slice A package:** `READY_FOR_DEVELOPMENT`.  
**Foundation Slice A scope gate:** `OPEN_FOR_AUTHORISED_EXECUTION` — `GO-2026-09-05-FSA-001` was revalidated by the project owner on 2026-09-07 for `WP-AZ-001` through `WP-AZ-008`. **Contractor start mode:** `OPEN_FOR_SELF_SELECTION`. The packages remain `READY_FOR_DEVELOPMENT`; objective start evidence must be accepted and canonically reconciled before transition. All eight evidence gates remain unsatisfied, and no infrastructure implementation completion is claimed.
