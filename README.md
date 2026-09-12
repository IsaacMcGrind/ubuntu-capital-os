# Ubuntu Capital OS

Ubuntu Capital OS is the evidence-first system reconstruction and delivery repository for rebuilding an OurCrowd-inspired private-markets investment platform one end-to-end use case at a time.

## Current status

`PARTIALLY_READY`

Current revision-pinned assessment: `docs/09-delivery/implementation-analysis-refresh-2026-09-05.md` at OS evidence commit `e1bbbe2fa5bcb3570271ac3bdbcba5b3072ad256`.

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

Foundation Slice A remains the planned Azure infrastructure package documented in `docs/09-delivery/foundation-slice-a-execution-package.md`. Technical contractors submit first-pass evidence in their contractor folders; accepted evidence references are later maintained in `docs/09-delivery/foundation-slice-a-evidence-register.md` through a separate Project-Manager-owned governance change.

**Current Foundation decision (2026-09-07):** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001` for `WP-AZ-001` through `WP-AZ-008` in Azure DEV/MVP. That decision defines the bounded scope but does not allocate work. Contractors may self-select work and must declare their exact package/path scope and evidence purpose in the PR. The packages remain `READY_FOR_DEVELOPMENT` until objective start evidence is accepted and canonically reconciled through a separate `PROJECT_MANAGER_GOVERNANCE` change; 0 of 8 completion evidence gates are satisfied. Source: `SRC-020`.

The repository materially advanced its canonical reconstruction outputs in commit `d2d6f7bfe90ef04ec846eb11308cf551977cd33d`: actors and permissions, detailed use-case specifications, business rules, journeys, state models, integration records, structured data, backlog/tracker/traceability/validation/risk artifacts and related schemas now exist in the canonical structure. Their existence removes the earlier claim that these directories or files were absent.

**Foundation scope is authorised by the recorded project-owner decision, not by file presence alone.** Contractor work does not require assignment or a Project Manager pre-start record; the contractor's evidence PR must document the work it selected. Evidence quality, exit criteria, traceability, security, status promotion and completion remain governed by `AGENT.md`, the controlling `plan.md`, and the Foundation evidence register.

The pre-implementation scope gate was formally satisfied by the 2026-09-07 revalidation. A contractor may begin any self-selected Foundation Slice A work in governed dependency order without assignment or a Project Manager pre-start record. Its evidence PR must declare the selected package/path scope and evidence purpose. The first business vertical slice—authenticated opportunity discovery plus a **non-binding expression of interest**—must not start or advance through `WP-AZ-009` to `WP-AZ-012` until Foundation evidence and the separate first-slice integrity prerequisites both reconcile.

## Delivery authority and contractor evidence workflow

Under `SRC-021`, 80K Developers (Pty) Ltd is the appointed Project Manager contractor and accountable project-management workstream. Thembinkosi Mtsweni is the responsible human Project Manager and final project-owner decision authority working through that management arrangement. In that capacity, Thembinkosi Mtsweni interprets contractor evidence, updates canonical Ubuntu Capital OS status and priorities, and approves gates or project-boundary changes. Contractors self-select work without allocation and document their selected scope and evidence intent in each PR.

Contractors and coders record all repository-hosted first-pass delivery evidence only under their existing `contractors/<contractor>/` directory. A technical evidence PR must not modify canonical governance, status, decision, register, tracker, traceability, roadmap, plan, or summary artifacts. Approved external raw evidence is represented by a sanitised stable reference in the contractor folder. Contractor evidence may document work performed, validation, limitations, unfinished work, blockers and decisions needed; it must not redefine gates, change canonical status, declare completion, expand project boundaries, or make project-level architecture, business or legal decisions.

Automated reviews assess evidence and recommend action only. After an evidence PR is reviewed and merged as provenance, the 80K Developers Project Manager workstream separately assesses it and makes any justified canonical OS update through an explicitly identified `PROJECT_MANAGER_GOVERNANCE` change.

When 80K Developers performs coding or implementation work, its technical evidence is governed exactly like other contractor evidence. A submission must clearly identify whether it is an implementation-evidence contribution or an 80K-Developers-Project-Manager-owned governance change.

See `AGENT.md` for the mandatory authority boundary and `plan.md` for the complete governed workflow.

## Controlling documents

- `AGENT.md` defines how autonomous agents and contributors must operate.
- `plan.md` is the single controlling execution plan and canonical repository-structure definition.
- Documents under `docs/` are reconstruction, architecture and delivery outputs. They must not compete with `plan.md` as execution instructions.
- `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` remains a live compatibility reference; current authority is the effective decision in `foundation-slice-a-go-decision-2026-09-05.md` as revalidated on 2026-09-07.
- `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md` is the historical prerequisite reassessment that informed the now-completed formal readiness review.
- `contractors/` records implementation provenance and contractor delivery evidence. It does not replace use-case, traceability, testing, or E2E evidence under `docs/`.

## Repository structure and integrity note

`plan.md` remains the canonical structure definition. The repository now contains the plan-defined canonical actors-and-permissions outputs under `docs/02-actors-and-permissions/`.

The architecture tree under `docs/02-architecture/` is now explicitly included in the canonical required-output tree by the project-owner-authorised `plan.md` amendment under `SRC-021`. This resolves the former structural exception only; it does not approve the contents, close their evidence gaps, or promote delivery status.

Other plan-required reconstruction, validation, traceability and machine-readable outputs also now exist. Presence is not equivalent to approval or completion: several remain `ANALYSIS_IN_PROGRESS`, contain `INFERRED`/`UNKNOWN` evidence, or have incomplete traceability and validation closure. Those substantive gaps—not the prior directory-absence claim—continue to govern evidence-based status promotion, downstream business-slice readiness and production readiness.

Key active areas include:

- `docs/00-context` — source inventory, terminology and boundary context
- `docs/01-system-understanding` — system purpose, evidence and assumptions
- `docs/02-actors-and-permissions` — canonical actors and permissions evidence
- `docs/02-architecture` — canonical system/logical architecture, Blueprint and architecture-decision evidence; content remains evidence-gated
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
