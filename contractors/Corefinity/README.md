# Corefinity — Ubuntu Capital Contribution Provenance

This directory records Corefinity architecture-analysis contribution provenance for Ubuntu Capital OS.

Corefinity contribution evidence is supporting project evidence only. It does not replace the authoritative requirements, architecture boundaries, evidence gates, delivery tracker, or human approval rules defined by Ubuntu Capital OS.

## Submission contract

**Project role:** Corefinity is a technical contractor whose recorded scope is architecture-analysis contribution evidence. Under `SRC-021`, it is not the Project Manager and does not independently authorise execution, gates, canonical status, completion, architecture adoption or further work.

Corefinity PRs use capacity `CONTRACTOR_TECHNICAL_EVIDENCE`, remain within an explicitly assigned work package, keep every repository-hosted first-pass evidence file under `contractors/Corefinity/`, and complete the project-owner-approved `.github/pull_request_template.md` (`SRC-021`). Approved external raw evidence must be represented by a sanitised stable reference in this folder; canonical governance/status artifacts must not be changed in the same PR. Architecture-analysis provenance may support an 80K Developers Project Manager decision but does not become that decision.

The canonical rules are `AGENT.md` and `plan.md`.

## Current evidence boundary

- `SRC-017` records the project-owner confirmation that GitHub account `kg-m3` is the Corefinity contractor identity for this project.
- Architecture-analysis contributions are referenced in Ubuntu Capital OS architecture and delivery documentation where recorded.
- `contribution-log.md` records repository-observable contributor attribution, including the confirmed `kg-m3` architecture contribution merged through PR #11.
- `new.md` is an existing historical placeholder and is not delivery evidence by itself.
- No independent product, backend, deployment, infrastructure, or end-to-end implementation completion is established merely by the existence of this contractor directory.

## Governance

Corefinity does not have independent authority through this repository to:

- change legal or business requirements;
- change evidence classifications without supporting evidence;
- mark a use case `COMPLETE`;
- approve production readiness;
- redefine contractor or project authority.

See `contribution-log.md` for confirmed contributor/artifact provenance and `implementation-status.md` for the currently recorded contribution status.
