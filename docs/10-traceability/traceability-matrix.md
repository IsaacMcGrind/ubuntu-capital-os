# Traceability Matrix

Status: `ANALYSIS_IN_PROGRESS`

| Trace ID | Source | Use Case | Implementation Evidence | Validation Evidence | Status |
|---|---|---|---|---|---|
| TRC-001 | SRC-001 | UC-OPP-001 | docs/09-delivery/implementation-coverage-gap-matrix.md | Pending targeted tests | PARTIAL |
| TRC-002 | SRC-003 | UC-IAM-001 | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/App.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/pages/Login.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/lib/session.ts` | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/test/auth-and-eoi.test.tsx` (unauthenticated redirect + authenticated access tests) | PARTIAL |
| TRC-003 | SRC-001 | UC-DD-001 | docs/04-use-cases/UC-DD-001.md | Pending NDA workflow validation | PARTIAL |
| TRC-004 | SRC-004 | UC-INV-001 | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/pages/DealDetail.tsx`, `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/lib/eoi.ts` | `/Users/officialnumbr10/Dev/ubuntu-capital-platform/src/test/auth-and-eoi.test.tsx` (validation-failure and duplicate-submission tests) | PARTIAL |
| TRC-005 | SRC-011 | UC-INT-003 | docs/02-architecture/azure-mvp-platform-decision.md | Pending runtime integration evidence | PARTIAL |

## Usage

This matrix is the required chain: source -> use case -> implementation -> validation -> status.
