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
| SRC-008 | `HarleyJoker/ubuntu-capital-platform` (`https://github.com/HarleyJoker/ubuntu-capital-platform`) | Current implementation source repository | Identifies the repository stated to contain the current Ubuntu Capital implementation | CONFIRMED | Repository identity and sharing status were supplied by the project owner. The implementation has now been inspected directly in the local environment. |
| SRC-009 | GitHub connector access attempt for `HarleyJoker/ubuntu-capital-platform` | Access evidence | Confirms that the connected ChatGPT GitHub app could not inspect the implementation repository during the current attempt | CONFIRMED | The attempt returned `404 Not Found`. This is an access/context blocker, not evidence of a contradiction in the implementation repository itself. |
| SRC-010 | Direct inspection of the implementation repository | Implementation source code | Confirms the implementation is a static React/Vite investor portal with route-based navigation and in-memory mock opportunities data | CONFIRMED | Direct repository inspection established that the app renders the public and portfolio flows in the browser without a backend service layer or persisted data store. |
| SRC-011 | Project-owner Azure MVP direction recorded 2026-08-29 | Decision evidence | Confirms Microsoft Azure and the documented Azure MVP infrastructure direction as the selected project-level cloud implementation direction | CONFIRMED | This is the approval evidence used by `ARCH-ADR-001`; it confirms the platform direction but does not prove that any Azure resource has been provisioned or deployed. |
| SRC-012 | `contractors/HerLogicSolutions/azure-architecture.md` | Contractor architecture evidence | Supports the proposed Azure cloud architecture and platform-service composition for the Ubuntu Capital MVP workstream | CONFIRMED | The document itself is confirmed source evidence; its architecture content supports the decision but does not independently confer project-level approval or implementation completion. |
| SRC-013 | `contractors/HerLogicSolutions/azure-mvp-cost-breakdown.md` | Contractor cost/architecture evidence | Supports MVP Azure cost assumptions, low-cost service choices, and cost-governance direction | CONFIRMED | The document itself is confirmed source evidence; actual Azure spend and provisioned tiers require runtime/account evidence. |

## Current Implementation Evidence Boundary

The existence of the deployed Ubuntu Capital website and the stated implementation repository are now part of the reconstruction context. They do **not** yet prove which of the 41 catalogued use cases are fully implemented, partially implemented, simulated, or absent.

Direct code inspection of the implementation repository confirms a front-end portal with route-based pages for discovery, dashboard, onboarding, opportunities, portfolio, reports, and investor/account flows. The repository contains mock opportunity data and UI state, but no evidence of a backend API, database, authentication service, payment or settlement engine, or persisted investor records. This is a materially important constraint: the implementation appears to be a design/marketing/prototype layer, not a complete regulated-investment platform.

The failed connector access attempt is recorded as `CONFIRMED` access evidence with delivery status `BLOCKED_BY_CONTEXT`. It must not be classified as `CONTRADICTED`, because no incompatible source descriptions have been established.

Use-case-level coverage is now partially established through direct repository inspection and remains non-final until route walkthrough evidence is reconciled with backend, persistence, and operational behavior.

## Next Validation Actions

1. Walk the live website against the master use-case catalogue and reconcile any mismatch with local code evidence.
2. Validate whether any backend/API/persistence components exist outside the currently inspected front-end repository.
3. Update the E2E delivery tracker with approved statuses based on objective evidence for each use case.
4. Record route-level walkthrough evidence, code references, and test outputs before promoting any use case status.
5. Prioritize implementation gaps in settlement, admin, audit, reporting, and external integrations.
6. Reconcile the coverage gap matrix with backlog and traceability outputs.
