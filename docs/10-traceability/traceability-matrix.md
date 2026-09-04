# Traceability Matrix

Status: `ANALYSIS_IN_PROGRESS`

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
| TRC-001 | SRC-001 | UC-OPP-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/02-architecture/priority-use-case-architecture-map.md` | Protected opportunity catalogue implementation target must be linked to a stable repository path/work item before readiness closure | Targeted opportunity success/access/error validation must be linked to a stable test/validation target | Objective delivery/E2E evidence target must be linked to a stable evidence ID/path | `docs/09-delivery/e2e-delivery-tracker.md` — stable planned row/status target required | PARTIAL |
| TRC-002 | SRC-003 | UC-IAM-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/02-architecture/use-cases/UC-IAM-001-sign-in-investor-portal.md` | Entra/protected-session implementation target must be linked to a stable repository path/work item before readiness closure | Authentication, token/session and negative-access validation target must be linked to a stable test/validation ID/path | Foundation/identity evidence target must be linked to a stable evidence ID/path | `docs/09-delivery/e2e-delivery-tracker.md` — stable planned row/status target required | PARTIAL |
| TRC-003 | SRC-001 | UC-DD-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/04-use-cases/UC-DD-001.md` plus relevant DD architecture/state artifacts | NDA/access-control implementation target must be linked to a stable repository path/work item before readiness closure | NDA lifecycle/access validation target must be linked to a stable test/validation ID/path | NDA lifecycle/access-control evidence target must be linked to a stable evidence ID/path | `docs/09-delivery/e2e-delivery-tracker.md` — stable planned row/status target required | PARTIAL |
| TRC-004 | SRC-004 | UC-INV-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | relevant EOI architecture/state and first-slice delivery artifacts | Non-binding EOI API/persistence/audit implementation target must be linked to a stable repository path/work item before readiness closure | Valid/invalid/duplicate/unauthorised/failure-path validation targets must be linked to stable test/validation IDs/paths | Backend/persistence/audit/deployed-E2E evidence targets must be linked to stable evidence IDs/paths | `docs/09-delivery/e2e-delivery-tracker.md` — stable planned row/status target required | PARTIAL |
| TRC-005 | SRC-011 | UC-INT-003 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/02-architecture/azure-mvp-platform-decision.md` | Messaging integration implementation target must be linked to a stable repository path/work item before readiness closure | Runtime integration/failure-path validation target must be linked to a stable test/validation ID/path | Provider/runtime evidence target must be linked to a stable evidence ID/path | `docs/09-delivery/e2e-delivery-tracker.md` — stable planned row/status target required | PARTIAL |

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
7. This matrix does not authorise implementation. The effective execution decision remains governed by `AGENT.md`, controlling `plan.md`, `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md`, and the applicable readiness-decision controls.
