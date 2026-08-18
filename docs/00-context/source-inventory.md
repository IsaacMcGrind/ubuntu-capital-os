# Source Inventory

Status: `ANALYSIS_IN_PROGRESS`

This inventory records source material used to reconstruct and validate Ubuntu Capital OS. New evidence must be added here before it is propagated into use cases, journeys, delivery tracking, or implementation claims.

| Source ID | Source | Type | What It Supports | Evidence Status | Notes |
|---|---|---|---|---|---|
| SRC-001 | OurCrowd public website (`https://www.ourcrowd.com/`) | Reference platform | Public investment-platform proposition and reference experience | CONFIRMED | Original reconstruction reference named in the repository baseline. |
| SRC-002 | OurCrowd authenticated portfolio route (`https://www.ourcrowd.com/myportfolio/home`) | Reference platform | Authenticated investor-portal context | CONFIRMED | Access and detailed behaviour remain subject to supplied screenshots and observations. |
| SRC-003 | Supplied OurCrowd screenshots and reverse-engineering material | User-supplied evidence | Visible opportunity cards, navigation, news, portfolio areas, and NDA trigger | CONFIRMED | Individual detailed flows remain `INFERRED` or `UNKNOWN` where not directly observed. |
| SRC-004 | Ubuntu Capital implemented website (`https://80kdevelopers.com/ubuntucapital/`) | Current implementation | Confirms that a current Ubuntu Capital website implementation has been deployed | CONFIRMED | Confirmed from user-provided project evidence. Automated fetch was not available in the current session, so feature-level behaviour has not yet been independently validated. |
| SRC-005 | `HarleyJoker/ubuntu-capital-platform` (`https://github.com/HarleyJoker/ubuntu-capital-platform`) | Current implementation source repository | Identifies the repository stated to contain the current Ubuntu Capital implementation | CONFIRMED | Repository path and sharing status were provided by the user. Current ChatGPT GitHub connector returned `404 Not Found`, so source code and feature coverage are not yet inspectable. |

## Current Implementation Evidence Boundary

The existence of the deployed Ubuntu Capital website and the stated implementation repository are now part of the reconstruction context. They do **not** yet prove which of the 41 catalogued use cases are fully implemented, partially implemented, simulated, or absent.

Until the implementation repository becomes accessible and the live website is walked through use case by use case, implementation coverage must remain `UNKNOWN` unless supported by direct evidence.

## Next Validation Actions

1. Grant the connected GitHub application access to `HarleyJoker/ubuntu-capital-platform`.
2. Inspect the repository structure, routes, components, APIs, persistence, integrations, tests, and deployment configuration.
3. Walk the live website against the master use-case catalogue.
4. Map each observed implementation to the relevant use-case ID.
5. Update the E2E delivery tracker with `NOT_ANALYSED`, `IN_DEVELOPMENT`, `COMPONENT_COMPLETE`, `READY_FOR_E2E_TEST`, or other approved statuses based on objective evidence.
6. Record code references, screenshots, API evidence, database evidence, logs, and test results before marking any use case `COMPLETE`.
