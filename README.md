# Ubuntu Capital OS

Ubuntu Capital OS is the evidence-first system reconstruction and delivery repository for rebuilding an OurCrowd-inspired private-markets investment platform one end-to-end use case at a time.

## Current status

`PARTIALLY_READY`

The initial repository baseline captures the supplied screenshots, public routes, authenticated portfolio route, reverse-engineering report, and enterprise reconstruction protocol. Material behaviour that was not directly evidenced is explicitly classified as `INFERRED` or `UNKNOWN`.

## Controlling documents

- `AGENT.md` defines how autonomous agents and contributors must operate.
- `plan.md` is the single controlling execution plan and canonical repository-structure definition.
- Documents under `docs/` are reconstruction and delivery outputs. They must not compete with `plan.md` as execution instructions.

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

Counts, links, IDs, evidence classifications, directory names, and required outputs must reconcile across the repository. A contributor or agent must repair inconsistencies before progressing to the next phase.

The current source base is insufficient to reproduce regulated investment execution faithfully. The next evidence priority is direct observation of onboarding, accreditation/KYC, opportunity detail, NDA, commitment, settlement, portfolio update, reporting, administration, and failure recovery behaviour.