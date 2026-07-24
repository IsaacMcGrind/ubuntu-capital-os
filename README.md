# Ubuntu Capital OS

Ubuntu Capital OS is the evidence-first system reconstruction and delivery repository for rebuilding an OurCrowd-inspired private-markets investment platform one end-to-end use case at a time.

## Current status

`PARTIALLY_READY`

The initial repository baseline captures the supplied screenshots, public routes, authenticated portfolio route, reverse-engineering report, and the enterprise reconstruction protocol. Material behaviour that was not directly evidenced is explicitly classified as `INFERRED` or `UNKNOWN`.

## Repository structure

- `docs/01-system-understanding` — system purpose, evidence, assumptions, glossary
- `docs/02-actors-and-access` — actor model and initial permissions
- `docs/03-functional-domains` — domains and capability map
- `docs/04-use-cases` — master catalogue and structured JSON
- `docs/05-user-journeys` — end-to-end journeys and diagrams
- `docs/06-state-models` — lifecycle models
- `docs/07-integrations` — integration catalogue and flows
- `docs/08-architecture` — system context, dependencies, data flow
- `docs/09-delivery` — roadmap, E2E tracker, backlog
- `docs/10-quality` — acceptance, traceability, gaps, risks
- `docs/11-open-questions` — unresolved questions and validation plan
- `schemas` — JSON schemas for structured outputs
- `output` — executive summary and machine-readable reconstruction report

## Evidence policy

Every material finding uses one of:

- `CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONTRADICTED`

The current source base is insufficient to reproduce regulated investment execution faithfully. The next evidence priority is direct observation of onboarding, accreditation/KYC, opportunity detail, NDA, commitment, settlement, portfolio update, reporting, administration, and failure recovery behaviour.
