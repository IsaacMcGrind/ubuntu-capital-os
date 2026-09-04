# Ubuntu Capital OS

Ubuntu Capital OS is the evidence-first system reconstruction and delivery repository for rebuilding an OurCrowd-inspired private-markets investment platform one end-to-end use case at a time.

## Current status

`PARTIALLY_READY`

Architecture readiness has materially improved: the repository now contains a system boundary, high-level logical architecture, priority use-case architecture map, detailed UC-IAM-001 architecture analysis, a Phase 1 MVP architecture Blueprint, and a confirmed Azure MVP cloud platform direction.

Application-source readiness cannot currently be established from reproducible repository evidence. Historical artifacts describe a predominantly React/Vite front-end prototype, but the inspected branch, commit SHA, run identity, and durable raw evidence were not recorded. Current source verification is therefore `BLOCKED_BY_CONTEXT`, and no use case is supported by objective end-to-end completion evidence in this repository.

## Ubuntu Capital implementation references

The OS records these project-owner-supplied references:

- **Live website reference:** https://80kdevelopers.com/ubuntucapital/
- **Stated implementation source repository:** https://github.com/HarleyJoker/ubuntu-capital-platform
- **Implementation provenance records:** `contractors/80kDevelopers/`

The connected ChatGPT GitHub application has not established current source access to `HarleyJoker/ubuntu-capital-platform`. The 41-use-case coverage matrix records a historical, partial mapping from a reported local inspection whose exact branch, commit SHA, run identity, and durable raw-evidence reference are missing. It is not current implementation-status evidence. Later architecture or infrastructure documentation does not refresh or validate that snapshot.

## Architecture and chosen MVP cloud platform

Technology-neutral architecture is recorded under `docs/02-architecture/` and remains authoritative for logical capability ownership and system boundaries.

The MVP cloud implementation direction is confirmed in `docs/02-architecture/azure-mvp-platform-decision.md`:

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

Azure Blob Storage remains part of the confirmed MVP platform decision, but it is intentionally outside Foundation Slice A (`WP-AZ-001` through `WP-AZ-008`). Blob implementation is deferred until a business slice actually requires controlled document or generated-file storage, such as due-diligence/data-room or investor-document delivery. This deferral does not reverse `ARCH-ADR-001` and does not imply Blob has already been implemented.

## Delivery position

The historical, unpinned coverage snapshot in `docs/09-delivery/implementation-coverage-gap-matrix.md` contains 41 row-level labels:

- **41 use cases mapped in the historical snapshot**
- **7 historical `COMPONENT_COMPLETE` labels** — reported UI/page-level evidence only
- **16 historical `IN_DEVELOPMENT` labels** — reported partial/prototype evidence
- **18 historical `READY_FOR_DEVELOPMENT` labels** — no substantive implementation evidence reported
- **0 `COMPLETE`** — no objective E2E-completion evidence is recorded

The first three counts describe only that unpinned snapshot; they must not be used as a current implementation-status roll-up until revision-pinned inspection and durable run evidence are recorded.

Foundation Slice A remains the planned Azure infrastructure package, documented in `docs/09-delivery/foundation-slice-a-execution-package.md` with evidence intended for `docs/09-delivery/foundation-slice-a-evidence-register.md`.

The repository materially advanced its canonical reconstruction outputs in commit `d2d6f7bfe90ef04ec846eb11308cf551977cd33d`: actors and permissions, detailed use-case specifications, business rules, journeys, state models, integration records, structured data, backlog/tracker/traceability/validation/risk artifacts and related schemas now exist in the canonical structure. Their existence removes the earlier claim that these directories or files were absent.

**Foundation implementation must still not be treated as authorised solely because those files now exist.** The remaining gate is evidence quality and exit-criteria reconciliation: approvals, unresolved legal/business rules, complete traceability, validation coverage, architecture/security/NFR decisions, architecture-tree disposition, and internal consistency must be assessed against `AGENT.md` and the controlling `plan.md`. The current reassessment is recorded in `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md`.

After that pre-implementation gate is formally satisfied with a recorded `GO` or explicitly scoped `CONDITIONAL_GO`, Foundation Slice A may be executed. The first business vertical slice—authenticated opportunity discovery plus a **non-binding expression of interest**—must not start or advance through `WP-AZ-009` to `WP-AZ-012` until Foundation evidence and the separate first-slice integrity prerequisites both reconcile.

## Controlling documents

- `AGENT.md` defines how autonomous agents and contributors must operate.
- `plan.md` is the single controlling execution plan and canonical repository-structure definition.
- Documents under `docs/` are reconstruction, architecture and delivery outputs. They must not compete with `plan.md` as execution instructions.
- `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` remains a live compatibility gate reference because several Foundation delivery artifacts point to it; it is **not sufficient by itself** to authorise implementation and now explicitly delegates current readiness evaluation to the 2026-09-03 reassessment.
- `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md` is the current Foundation readiness reconciliation and requires closure/disposition of ADR, security, privacy, NFR, traceability, validation, business/legal and structure items plus a formal `GO`, `CONDITIONAL_GO`, or `NO_GO` decision.
- `contractors/` records implementation provenance and contractor delivery evidence. It does not replace use-case, traceability, testing, or E2E evidence under `docs/`.

## Repository structure and integrity note

`plan.md` remains the canonical structure definition. The repository now contains the plan-defined canonical actors-and-permissions outputs under `docs/02-actors-and-permissions/`.

The working architecture tree under `docs/02-architecture/` is an **explicit unresolved structure exception**: it is actively used and contains material architecture evidence, but it is not currently declared in the canonical required-output tree in `plan.md`. That exception must be formally dispositioned before the repository-integrity gate is closed—either by amending the canonical contract to include the architecture tree or by recording an approved exception that is consistent with `AGENT.md` and the controlling plan. Its existence must not be silently treated as canonical reconciliation.

Other plan-required reconstruction, validation, traceability and machine-readable outputs also now exist. Presence is not equivalent to approval or completion: several remain `ANALYSIS_IN_PROGRESS`, contain `INFERRED`/`UNKNOWN` evidence, or have incomplete traceability and validation closure. Those substantive gaps—not the prior directory-absence claim—are what continue to govern Foundation readiness.

Key active areas include:

- `docs/00-context` — source inventory, terminology and boundary context
- `docs/01-system-understanding` — system purpose, evidence and assumptions
- `docs/02-actors-and-permissions` — canonical actors and permissions evidence
- `docs/02-architecture` — working system/logical architecture, Blueprint and architecture decisions; explicit structure exception pending disposition
- `docs/03-functional-domains` — domains and capability map
- `docs/04-use-cases` — master catalogue and detailed specifications
- `docs/05-business-rules` — business-rule register
- `docs/06-journeys` — end-to-end journey models
- `docs/07-state-models` — lifecycle/state models
- `docs/08-integrations` — integration catalogue
- `docs/09-delivery` — implementation analysis, roadmap, coverage, backlog, tracker, Foundation execution/evidence, governance reconciliation and monitoring
- `docs/10-traceability` — source/use-case/implementation/test/evidence traceability
- `docs/11-open-questions` — unresolved questions
- `docs/12-validation` — validation planning
- `docs/13-risks` — risk/gap register
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

Foundation operational telemetry under `WP-AZ-007` is not equivalent to business audit evidence. Business audit for the first EOI slice remains separately gated under `WP-AZ-011` and `UC-AUD-001`.

## Integrity policy

Counts, links, IDs, evidence classifications, directory names, implementation claims and required outputs must reconcile across the repository. A contributor or agent must repair inconsistencies before progressing to implementation or claiming a status that depends on those inconsistencies being resolved.

The source base is still insufficient to reproduce regulated investment execution faithfully. Critical remaining evidence priorities include onboarding/eligibility rules, KYC/AML integration, NDA lifecycle, investment legal meaning, settlement/custody/reconciliation, portfolio valuation, approved internal permissions, business audit/reporting, retention/privacy, operational recovery, and measurable security/NFR targets.
