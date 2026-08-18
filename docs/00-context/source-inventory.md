# Source Inventory

Status: `ANALYSIS_IN_PROGRESS`

This inventory records source material used to reconstruct and validate Ubuntu Capital OS. New evidence must be added here before it is propagated into use cases, journeys, delivery tracking, or implementation claims.

The established `SRC-001`–`SRC-006` identifiers are preserved exactly because they are already referenced elsewhere in the repository. New implementation evidence is appended using new source IDs.

| Source ID | Source | Type | What It Supports | Evidence Status | Notes |
|---|---|---|---|---|---|
| SRC-001 | Supplied OurCrowd screenshot set | Screenshot set | Visible investor-facing UI, navigation, opportunity cards, asset classes, news, portfolio sections, and NDA action | CONFIRMED | High reliability for visible UI only; does not prove backend rules, permissions, calculations, or integrations. |
| SRC-002 | OurCrowd public website (`https://www.ourcrowd.com/`) | URL / reference platform | Confirms public platform location and reference experience | CONFIRMED | No complete route crawl has yet been recorded in this reconstruction. |
| SRC-003 | OurCrowd authenticated portfolio route (`https://www.ourcrowd.com/myportfolio/home`) | URL / reference platform | Confirms authenticated portfolio-home route pattern | CONFIRMED | Authentication and route guards were not directly observed. |
| SRC-004 | App / Website Reverse-Engineering Report | User-supplied report | Product interpretation, personas, likely workflows, architecture, pages, and data-model hypotheses | INFERRED SUPPORT | Contains assumptions and must not be treated as direct behavioural evidence. |
| SRC-005 | Enterprise System Reconstruction and Use-Case Discovery Agent prompt | Execution prompt | Defines the reconstruction method, evidence classifications, schemas, backlog, traceability, and required outputs | CONFIRMED | Governs project process rather than target-system behaviour. |
| SRC-006 | `IsaacMcGrind/ubuntu-capital-os` | Repository | Ubuntu Capital OS reconstruction repository and project baseline | CONFIRMED | At project start it contained no product implementation; it now contains reconstruction and delivery artefacts. |
| SRC-007 | Ubuntu Capital implemented website (`https://80kdevelopers.com/ubuntucapital/`) | Current implementation | Confirms that a current Ubuntu Capital website implementation has been deployed | CONFIRMED | User-provided implementation evidence. Feature-level and E2E behaviour are not yet reconciled against the 41-use-case catalogue. |
| SRC-008 | `HarleyJoker/ubuntu-capital-platform` (`https://github.com/HarleyJoker/ubuntu-capital-platform`) | Current implementation source repository | Identifies the repository stated to contain the current Ubuntu Capital implementation | CONFIRMED | Repository identity and sharing status were supplied by the project owner. Source contents are not yet inspectable through the connected ChatGPT GitHub app. |
| SRC-009 | GitHub connector access attempt for `HarleyJoker/ubuntu-capital-platform` | Access evidence | Confirms that the connected ChatGPT GitHub app could not inspect the implementation repository during the current attempt | CONFIRMED | The attempt returned `404 Not Found`. This is an access/context blocker, not evidence of a contradiction in the implementation repository itself. |

## Current Implementation Evidence Boundary

The existence of the deployed Ubuntu Capital website and the stated implementation repository are now part of the reconstruction context. They do **not** yet prove which of the 41 catalogued use cases are fully implemented, partially implemented, simulated, or absent.

The failed connector access attempt is recorded as `CONFIRMED` access evidence with delivery status `BLOCKED_BY_CONTEXT`. It must not be classified as `CONTRADICTED`, because no incompatible source descriptions have been established.

Until the implementation repository becomes accessible and the live website is walked through use case by use case, implementation coverage remains `UNKNOWN` unless supported by direct evidence.

## Next Validation Actions

1. Grant the connected GitHub application access to `HarleyJoker/ubuntu-capital-platform`.
2. Inspect the repository structure, routes, components, APIs, persistence, integrations, tests, and deployment configuration.
3. Walk the live website against the master use-case catalogue.
4. Map each observed implementation to the relevant use-case ID.
5. Update the E2E delivery tracker with `NOT_ANALYSED`, `IN_DEVELOPMENT`, `COMPONENT_COMPLETE`, `READY_FOR_E2E_TEST`, or other approved statuses based on objective evidence.
6. Record code references, screenshots, API evidence, database evidence, logs, and test results before marking any use case `COMPLETE`.
