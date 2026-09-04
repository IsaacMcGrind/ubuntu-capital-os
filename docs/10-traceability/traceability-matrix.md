# Traceability Matrix

Status: `ANALYSIS_IN_PROGRESS`

The governed chain required by `AGENT.md` is **source -> use case -> backlog -> implementation -> test -> evidence -> status**. Architecture and validation artifacts may provide additional intermediate context, but they do not replace the required backlog, test, or durable evidence hops.

| Trace ID | Source | Use Case | Backlog | Architecture / Design | Implementation Evidence | Test Evidence | Durable Evidence Record | Status |
|---|---|---|---|---|---|---|---|---|
| TRC-001 | SRC-001 | UC-OPP-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/02-architecture/priority-use-case-architecture-map.md` | `docs/09-delivery/implementation-coverage-gap-matrix.md` | Pending targeted opportunity tests | Pending objective evidence record / E2E tracker linkage | PARTIAL |
| TRC-002 | SRC-003 | UC-IAM-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/02-architecture/use-cases/UC-IAM-001-sign-in-investor-portal.md` | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/App.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/pages/Login.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/lib/session.ts` | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/test/auth-and-eoi.test.tsx` (unauthenticated redirect + authenticated access tests) | Pending durable repository evidence record linking test/run/revision to the E2E tracker | PARTIAL |
| TRC-003 | SRC-001 | UC-DD-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/04-use-cases/UC-DD-001.md` plus relevant DD architecture/state artifacts | `docs/04-use-cases/UC-DD-001.md` only; no complete runtime implementation evidence | Pending NDA workflow validation | Pending NDA lifecycle / access-control evidence record | PARTIAL |
| TRC-004 | SRC-004 | UC-INV-001 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | relevant EOI architecture/state and first-slice delivery artifacts | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/pages/DealDetail.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/lib/eoi.ts` | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/test/auth-and-eoi.test.tsx` (validation-failure and duplicate-submission tests) | Pending backend/persistence/audit/deployed-E2E evidence record | PARTIAL |
| TRC-005 | SRC-011 | UC-INT-003 | `docs/09-delivery/backlog.json` / `data/backlog.json` — related use-case coverage must be reconciled to a stable backlog item ID | `docs/02-architecture/azure-mvp-platform-decision.md` | No runtime integration evidence recorded | Pending runtime integration tests | Pending provider/runtime evidence record | PARTIAL |

## Usage and completion rule

1. Every applicable trace chain must include a stable source ID, use-case ID, backlog item ID, implementation reference, test reference, durable evidence reference, and governed status before the chain can be treated as complete.
2. A general backlog file reference is **not** sufficient for completion; the readiness closure must reconcile each critical use case to specific stable backlog item IDs.
3. Local implementation/test paths are historical evidence references only until they are represented by durable repository-accessible evidence with revision/run identity.
4. `Pending` in any required hop keeps the chain `PARTIAL` and prevents a readiness decision from claiming complete traceability for that scope.
5. `docs/09-delivery/e2e-delivery-tracker.md` must reconcile to the same use case, backlog, test, evidence, and status chain rather than acting as a substitute for missing evidence.