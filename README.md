# Ubuntu Capital OS

Ubuntu Capital OS is the evidence-first system reconstruction and delivery repository for rebuilding an OurCrowd-inspired private-markets investment platform one end-to-end use case at a time.

## Current status

`PARTIALLY_READY`

The repository baseline captures the supplied reference-platform evidence, reverse-engineering material, the 41-use-case catalogue, the execution protocol, and the current Ubuntu Capital implementation references. Material behaviour that has not been directly evidenced remains explicitly classified as `INFERRED` or `UNKNOWN`.

## Current Ubuntu Capital implementation

The current implementation supplied by the project owner is now tracked as part of the OS context:

- **Live website:** https://80kdevelopers.com/ubuntucapital/
- **Implementation source repository:** https://github.com/HarleyJoker/ubuntu-capital-platform
- **Implementation provenance:** `contractors/80kdevelopers/`

The connected ChatGPT GitHub application cannot currently inspect `HarleyJoker/ubuntu-capital-platform`; the access attempt returned `404 Not Found`. Therefore the existence of the deployed website is recorded as implementation progress, while exact use-case coverage remains unverified until the codebase and live flows can be reconciled against the 41-use-case catalogue.

## Controlling documents

- `AGENT.md` defines how autonomous agents and contributors must operate.
- `plan.md` is the single controlling execution plan and canonical repository-structure definition.
- Documents under `docs/` are reconstruction and delivery outputs. They must not compete with `plan.md` as execution instructions.
- `contractors/` records implementation provenance and contractor delivery evidence. It does not replace use-case, traceability, testing, or E2E evidence under `docs/`.

## Canonical repository structure

- `docs/00-context` — source inventory, terminology, and system boundary
- `docs/01-system-understanding` — system purpose, evidence, and assumptions
- `docs/02-actors-and-permissions` — actors, roles, authority, and permissions matrix
- `docs/03-functional-domains` — domains and capability map
- `docs/04-use-cases` — master catalogue and detailed specifications
- `docs/05-business-rules` — extracted rules and controls
- `docs/06-journeys` — end-to-end journeys and diagrams
- `docs/07-state-models` — lifecycle and transition models
- `docs/08-integrations` — integration catalogue and dependency behaviour
- `docs/09-delivery` — implementation roadmap, backlog, and E2E tracker
- `docs/10-traceability` — source-to-requirement-to-test-to-evidence traceability
- `docs/11-open-questions` — unresolved questions
- `docs/12-validation` — validation plan for inferred and unknown behaviour
- `docs/13-risks` — gap and risk register
- `contractors/80kdevelopers` — current 80K Developers implementation references, provenance, and delivery-status evidence
- `schemas` — JSON schemas for structured outputs
- `data` — machine-readable reconstruction artefacts
- `output` — executive reconstruction summaries

## Evidence policy

Every material finding uses one of:

- `CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONTRADICTED`

A `CONFIRMED` classification requires direct supplied evidence. Every non-confirmed finding must state the uncertainty, impact, evidence needed, and validation method.

## Integrity policy

Counts, links, IDs, evidence classifications, directory names, implementation claims, and required outputs must reconcile across the repository. A contributor or agent must repair inconsistencies before progressing to the next phase.

The source base is still insufficient to reproduce regulated investment execution faithfully. The next evidence priority is to gain access to the current implementation repository, walk the deployed website against the 41 use cases, and directly validate onboarding, accreditation/KYC, opportunity detail, NDA, commitment, settlement, portfolio update, reporting, administration, security, testing, and failure-recovery behaviour.
