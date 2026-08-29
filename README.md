# Ubuntu Capital OS

Ubuntu Capital OS is the evidence-first system reconstruction and delivery repository for rebuilding an OurCrowd-inspired private-markets investment platform one end-to-end use case at a time.

## Current status

`PARTIALLY_READY`

Architecture readiness has materially improved: the repository now contains a system boundary, high-level logical architecture, priority use-case architecture map, detailed UC-IAM-001 architecture analysis, and a confirmed Azure MVP cloud platform direction.

Implementation readiness remains lower than architecture readiness. The current recorded implementation evidence still describes a predominantly React/Vite front-end prototype with no use case yet supported by objective end-to-end completion evidence.

## Current Ubuntu Capital implementation

The current implementation tracked by the OS is:

- **Live website:** https://80kdevelopers.com/ubuntucapital/
- **Implementation source repository:** https://github.com/HarleyJoker/ubuntu-capital-platform
- **Implementation provenance:** `contractors/80kDevelopers/`

The connected ChatGPT GitHub application cannot directly inspect `HarleyJoker/ubuntu-capital-platform`. The current 41-use-case implementation coverage matrix is therefore treated as recorded implementation evidence from the prior inspection captured in this OS repository. No new source-code inspection is implied by later architecture or infrastructure documentation.

## Architecture and chosen MVP cloud platform

Technology-neutral architecture is recorded under `docs/02-architecture/` and remains authoritative for logical capability ownership and system boundaries.

The MVP cloud implementation direction is now confirmed in `docs/02-architecture/azure-mvp-platform-decision.md`:

- Azure Static Web Apps — React/Vite frontend hosting
- Microsoft Entra External ID — customer identity/authentication
- Azure Functions — backend/API compute
- Azure SQL Database — relational persistence where required
- Azure Blob Storage — documents/generated files
- Azure Key Vault — secrets/configuration
- Managed Identity — Azure service-to-service identity where supported
- Application Insights + Azure Monitor — telemetry, health and alerting
- Azure Cost Management — budgets and cost governance
- GitHub Actions or Azure DevOps — repeatable CI/CD as delivery requires

This is a target architecture decision, not proof that these Azure resources are already deployed or integrated.

## Delivery position

The recorded implementation coverage is derived from the 41 row-level statuses in `docs/09-delivery/implementation-coverage-gap-matrix.md`:

- **41 use cases mapped**
- **7 `COMPONENT_COMPLETE`** — UI/page-level only
- **16 `IN_DEVELOPMENT`** — partial/prototype evidence
- **18 `READY_FOR_DEVELOPMENT`** — no substantive implementation evidence
- **0 `COMPLETE`**

The recommended next delivery step is the Azure foundation slice documented in `docs/09-delivery/azure-mvp-platform-delivery-plan.md`, followed by the first complete business vertical slice: authenticated opportunity discovery plus a **non-binding expression of interest**.

## Controlling documents

- `AGENT.md` defines how autonomous agents and contributors must operate.
- `plan.md` is the single controlling execution plan and canonical repository-structure definition.
- Documents under `docs/` are reconstruction, architecture and delivery outputs. They must not compete with `plan.md` as execution instructions.
- `contractors/` records implementation provenance and contractor delivery evidence. It does not replace use-case, traceability, testing, or E2E evidence under `docs/`.

## Repository structure and integrity note

`plan.md` remains the canonical structure definition. The repository currently contains `docs/02-architecture/`, while the plan-defined canonical `docs/02-actors-and-permissions/` phase is currently missing from the repository. The architecture tree is therefore an explicit structure exception that must be reconciled deliberately; it must not be read as if the canonical actors-and-permissions directory already exists or has been replaced.

Key active areas include:

- `docs/00-context` — source inventory, terminology and boundary context
- `docs/01-system-understanding` — system purpose, evidence and assumptions
- `docs/02-architecture` — working system/logical architecture and architecture decisions
- `docs/03-functional-domains` — domains and capability map
- `docs/04-use-cases` — master catalogue and detailed specifications
- `docs/09-delivery` — implementation analysis, roadmap, coverage, backlog and monitoring
- `docs/11-open-questions` — unresolved questions
- `contractors/80kDevelopers` — implementation evidence/provenance
- `contractors/HerLogicSolutions` — Azure cloud architecture/cost workstream evidence
- `contractors/Corefinity` — architecture contribution provenance where recorded
- `schemas`, `data`, `output` — structured evidence, machine-readable artifacts and summaries

## Evidence policy

Every material finding uses one of:

- `CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONTRADICTED`

A `CONFIRMED` classification requires direct supplied evidence. Every non-confirmed finding must state the uncertainty, impact, evidence needed and validation method.

Architecture selection does not promote delivery status. A use case can become `COMPLETE` only when its required vertical-slice and E2E evidence exists.

## Integrity policy

Counts, links, IDs, evidence classifications, directory names, implementation claims and required outputs must reconcile across the repository. A contributor or agent must repair inconsistencies before progressing to the next phase.

The source base is still insufficient to reproduce regulated investment execution faithfully. Critical remaining evidence priorities include onboarding/eligibility rules, KYC/AML integration, NDA lifecycle, investment legal meaning, settlement/custody/reconciliation, portfolio valuation, internal permissions, audit/reporting, retention/privacy, and operational recovery.
