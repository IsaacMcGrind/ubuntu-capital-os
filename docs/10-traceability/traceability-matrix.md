# Traceability Matrix

> **Current Foundation decision — 2026-09-07:** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001`. The scope gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. Contractors may self-select and begin work inside that project boundary without assignment or a Project Manager pre-start record; implementation, evidence acceptance, canonical status, completion, business-use-case and production claims remain evidence-gated. Source: `SRC-020`.

Status: `IN_DEVELOPMENT`

Effective revalidated decision: `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md` (`GO-2026-09-05-FSA-001`). Effective scope gate: `OPEN_FOR_AUTHORISED_EXECUTION`; the formal project-owner review is recorded by `SRC-020`, and contractor work allocation is not used.

Ubuntu Capital OS uses two related but distinct traceability chains so the pre-implementation readiness gate does not require evidence that can only exist after authorised delivery begins.

### Pre-start planned traceability

Before a `GO` or explicitly scoped `CONDITIONAL_GO` can authorise implementation, the proposed scope must have stable planned links for:

`source -> use case -> backlog -> architecture/design (where applicable) -> planned implementation target -> planned test/validation target -> planned durable-evidence target -> planned tracker/status`

A readiness decision evaluates this **planned** chain. Missing realised implementation, test-run, deployment or durable-evidence records do not by themselves block a pre-start decision because those records are produced during authorised execution.

### Post-start realised traceability

After authorised execution begins, the applicable planned targets must progressively be replaced or reconciled with realised delivery evidence:

`source -> use case -> backlog -> architecture/design (where applicable) -> implementation evidence -> test/run evidence -> durable evidence -> validation/status`

Missing required realised hops block status promotion, `COMPONENT_COMPLETE`, E2E readiness and acceptance. They do not retroactively make the pre-start decision circular.

## Pre-start planned traceability register

| Trace ID | Source | Use Case | Backlog Target | Architecture / Design | Planned Implementation Target | Planned Test / Validation Target | Planned Durable-Evidence Target | Planned Tracker / Status Target | Readiness Trace Status |
|---|---|---|---|---|---|---|---|---|---|
| TRC-001 | SRC-001 | UC-OPP-001 | `BL-OPP-001` in `docs/09-delivery/backlog.json` and `data/backlog.json` | `docs/02-architecture/priority-use-case-architecture-map.md` | `WP-AZ-009` in `docs/09-delivery/azure-mvp-platform-delivery-plan.md` | `docs/12-validation/validation-plan.md` (use-case verification + E2E walkthrough layer) and `WP-AZ-012` evidence gate | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-OPP-001` with realised evidence links added during `WP-AZ-012` | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-OPP-001` | COMPLETE |
| TRC-002 | SRC-003 | UC-IAM-001 | `BL-IAM-001` in `docs/09-delivery/backlog.json` and `data/backlog.json` | `docs/02-architecture/use-cases/UC-IAM-001-sign-in-investor-portal.md` | `WP-AZ-003` and `WP-AZ-004` in `docs/09-delivery/azure-mvp-platform-delivery-plan.md` | `docs/12-validation/validation-plan.md` (security/authorization checks) and `WP-AZ-012` evidence gate | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-IAM-001` with realised evidence links added during `WP-AZ-012` | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-IAM-001` | COMPLETE |
| TRC-003 | SRC-001 | UC-DD-001 | `BL-DD-001` in `docs/09-delivery/backlog.json` and `data/backlog.json` | `docs/04-use-cases/UC-DD-001.md` plus DD architecture/state artifacts | `WP-AZ-009` follow-on scope in `docs/09-delivery/azure-mvp-platform-delivery-plan.md` after Foundation and first-slice gate | `docs/12-validation/validation-plan.md` (use-case verification + security checks) | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-DD-001` with realised evidence links added when DD enters active execution scope | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-DD-001` | COMPLETE |
| TRC-004 | SRC-004 | UC-INV-001 | `BL-INV-001` in `docs/09-delivery/backlog.json` and `data/backlog.json` | `docs/04-use-cases/UC-INV-001.md` plus first-slice delivery artifacts | `WP-AZ-010` and `WP-AZ-011` in `docs/09-delivery/azure-mvp-platform-delivery-plan.md` | `docs/12-validation/validation-plan.md` (success/failure-path verification) and `WP-AZ-012` evidence gate | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-INV-001` with realised evidence links added during `WP-AZ-012` | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-INV-001` | COMPLETE |
| TRC-005 | SRC-011 | UC-INT-003 | `BL-INT-003` in `docs/09-delivery/backlog.json` and `data/backlog.json` | `docs/02-architecture/azure-mvp-platform-decision.md` | `WP-AZ-004` platform integration foundation and `WP-AZ-009` onward integration scope in `docs/09-delivery/azure-mvp-platform-delivery-plan.md` | `docs/12-validation/validation-plan.md` (integration/security checks) and `WP-AZ-012` where first-slice integration applies | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-INT-003` with realised evidence links added during relevant execution scope | `docs/09-delivery/e2e-delivery-tracker.md` row `UC-INT-003` | COMPLETE |

## Realised delivery evidence register

The entries below are recorded implementation/test evidence where repository history already contains it. They do **not** satisfy the pre-start planned chain by themselves and they do not imply current implementation authorisation or completion.

| Trace ID | Realised Implementation Evidence | Realised Test / Run Evidence | Realised Durable Evidence | Realised Delivery Status |
|---|---|---|---|---|
| TRC-001 | `docs/09-delivery/implementation-coverage-gap-matrix.md` | Pending targeted opportunity runtime tests | Pending objective evidence record / E2E linkage | PARTIAL |
| TRC-002 | Historical local references: `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/App.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/pages/Login.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/lib/session.ts` | Historical local reference: `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/test/auth-and-eoi.test.tsx` (unauthenticated redirect + authenticated access tests) | Pending durable repository-accessible record linking revision/run evidence to the E2E tracker | PARTIAL |
| TRC-003 | `docs/04-use-cases/UC-DD-001.md` only; no complete runtime implementation evidence | Pending NDA workflow validation | Pending NDA lifecycle / access-control evidence record | PARTIAL |
| TRC-004 | Historical local references: `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/pages/DealDetail.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/lib/eoi.ts` | Historical local reference: `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/test/auth-and-eoi.test.tsx` (validation-failure and duplicate-submission tests) | Pending backend/persistence/audit/deployed-E2E evidence record | PARTIAL |
| TRC-005 | No runtime integration evidence recorded | Pending runtime integration tests | Pending provider/runtime evidence record | PARTIAL |

## Usage and gate rules

1. **Readiness uses the planned chain.** Every applicable proposed scope must have stable source, use-case, backlog, architecture/design where applicable, planned implementation, planned test/validation, planned durable-evidence and planned tracker/status targets before that trace chain can support a readiness decision.
2. A general backlog-file reference, undefined future test, generic evidence placeholder or unlinked E2E tracker row is not sufficient. Critical scope must reconcile to stable repository-accessible IDs or targets.
3. `Pending` in a required **planned pre-start** hop keeps the readiness trace `PARTIAL` and prevents `GO` or `CONDITIONAL_GO` from claiming that planned traceability is closed for that scope.
4. `Pending` in a **realised post-start** implementation, test/run or durable-evidence hop does **not** prevent a pre-start readiness decision for work that has not yet been authorised. After execution starts, however, those missing realised hops block the affected delivery-status promotion, E2E readiness and acceptance.
5. Historical local implementation/test paths are supporting evidence only until represented by durable repository-accessible evidence with revision/run identity. They must not be used to infer current completion or to bypass the readiness gate.
6. `docs/09-delivery/e2e-delivery-tracker.md` must point to the same stable planned IDs/targets before start and then reconcile to the realised implementation/test/evidence/status references during delivery; it cannot substitute for a missing traceability hop.
7. This matrix does not by itself change project boundaries, accept evidence, or promote status. The effective scope gate is governed by `AGENT.md`, controlling `plan.md`, and the applicable project-owner decision controls. `GO-2026-09-05-FSA-001` was explicitly revalidated on 2026-09-07 and is current authority for its bounded Foundation scope. Contractors may self-select and begin work within it without assignment or a Project Manager pre-start record; realised traceability remains mandatory as execution progresses.
