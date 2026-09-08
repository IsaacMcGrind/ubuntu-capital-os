# Validation Plan

Status: `ANALYSIS_IN_PROGRESS`

## Validation layers

1. Structural repository validation (required files, link integrity, ID consistency).
2. Schema validation for JSON artifacts in data/ and docs/09-delivery.
3. Use-case verification checks for success and failure paths.
4. Security/authorization checks for protected workflows.
5. E2E walkthrough evidence for status promotion.

## Repository-executable validation checks

- JSON parse validation with `jq` for backlog/schema files.
- Required-file inventory comparison against `plan.md`.

These checks apply to this Ubuntu Capital OS repository. They do not verify the current contents or runtime behaviour of `HarleyJoker/ubuntu-capital-platform`.

## Reported historical implementation checks

Repository artifacts record the following results for a local snapshot on 2026-08-31. The exact source branch, commit SHA, run identity, and durable raw-evidence reference are `UNKNOWN`, so every result in this section is historical/partial supporting evidence only.

- Reported local path: `/Users/officialnumbr10/Dev/ubuntu-capital-platform`
- Reported baseline checks:
	- `npm run lint` (0 errors, 8 warnings)
	- `npm test` (passed)
	- `npm run build` (passed)
- Reported verification rerun:
	- `npm run lint` (0 errors, 8 warnings; reportedly unchanged)
	- `npm test` (passed; `2` files, `6` tests)
	- `npm run build` (passed; non-blocking warnings reportedly unchanged)
- Reported Step-2 test coverage:
	- session-required route behavior (`/myportfolio/*` redirect for unauthenticated access)
	- unauthorized-access denial for guarded portfolio route entry
	- EOI validation failure checks (empty and below-minimum amount)
	- EOI duplicate-submission protection for the same deal ID

## Historical verification limitations and current boundary

- The reported lint warnings concerned `react-refresh/only-export-components` in shared UI files.
- The reported build warnings concerned large JS chunk size and Browserslist data staleness.
- The reported tests covered limited UI behaviour and did not establish business-flow, authorization-boundary, persistence, or E2E completion for critical use cases.
- None of these observations confirms current codebase health or current implementation behaviour. An authorised revision-pinned inspection and durable run record are required before they can be refreshed as current verification evidence.

## Planned checks

- Automated markdown link checker.
- Schema-driven validation for journeys, state models, integrations.
- E2E test evidence package per critical use case.
