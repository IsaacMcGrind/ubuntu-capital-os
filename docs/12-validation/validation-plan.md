# Validation Plan

Status: `ANALYSIS_IN_PROGRESS`

## Validation layers

1. Structural repository validation (required files, link integrity, ID consistency).
2. Schema validation for JSON artifacts in data/ and docs/09-delivery.
3. Use-case verification checks for success and failure paths.
4. Security/authorization checks for protected workflows.
5. E2E walkthrough evidence for status promotion.

## Current executable checks

- JSON parse validation with jq for backlog/schema files.
- Required-file inventory comparison against plan.md.
- Local implementation repo baseline checks (2026-08-31):
	- `npm run lint` in `/Users/officialnumbr10/Dev/ubuntu-capital-platform` (0 errors, 8 warnings)
	- `npm test` in `/Users/officialnumbr10/Dev/ubuntu-capital-platform` (passed)
	- `npm run build` in `/Users/officialnumbr10/Dev/ubuntu-capital-platform` (passed)

- Local implementation repo verification rerun (2026-08-31):
	- `npm run lint` in `/Users/officialnumbr10/Dev/ubuntu-capital-platform` (0 errors, 8 warnings; unchanged)
	- `npm test` in `/Users/officialnumbr10/Dev/ubuntu-capital-platform` (passed; `2` files, `6` tests)
	- `npm run build` in `/Users/officialnumbr10/Dev/ubuntu-capital-platform` (passed; non-blocking warnings unchanged)

- Step-2 verification coverage added (2026-08-31):
	- session-required route behavior (`/myportfolio/*` redirect for unauthenticated access)
	- unauthorized-access denial for guarded portfolio route entry
	- EOI validation failure checks (empty and below-minimum amount)
	- EOI duplicate-submission protection for same deal ID

## Observed verification limitations

- Current lint output includes `react-refresh/only-export-components` warnings in shared UI files.
- Build output includes non-blocking warnings for large JS chunk size and Browserslist data staleness.
- Current tests validate limited UI rendering behavior and do not yet provide business-flow, authorization-boundary, persistence, or E2E coverage for critical use cases.

## Planned checks

- Automated markdown link checker.
- Schema-driven validation for journeys, state models, integrations.
- E2E test evidence package per critical use case.
