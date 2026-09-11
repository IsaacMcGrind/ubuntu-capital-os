# HerLogic Solutions — Ubuntu Capital Azure Workstream

This directory records HerLogic Solutions contribution provenance for the Ubuntu Capital Azure cloud architecture, cost, and infrastructure-delivery workstream.

## Submission contract

**Project role:** HerLogic Solutions is the technical Azure architecture, cost and infrastructure-delivery contractor. Under `SRC-021`, it is not the Project Manager and does not independently authorise execution, gates, canonical status, completion, architecture adoption or further work.

HerLogic Solutions PRs use capacity `CONTRACTOR_TECHNICAL_EVIDENCE`, remain within an explicitly assigned work package, keep every repository-hosted first-pass evidence file under `contractors/HerLogicSolutions/`, and complete the project-owner-approved `.github/pull_request_template.md` (`SRC-021`). Approved external raw evidence must be represented by a sanitised stable reference in this folder; canonical governance/status artifacts must not be changed in the same PR. They may record sanitised Azure work performed, revision-pinned evidence, validation, limitations, blockers, dependencies and decisions required from 80K Developers Project Manager workstream.

The canonical rules are `AGENT.md` and `plan.md`.

## Current evidence

The directory includes:

- `azure-architecture.md` — proposed Azure architecture and practical implementation/upskilling context;
- `azure-mvp-cost-breakdown.md` — MVP cost-control and service-cost evidence;
- `contribution-log.md` — contributor/artifact provenance for the Azure architecture and MVP cost-analysis commits plus the project-owner-confirmed contractor identity mapping;
- `implementation-status.md` — the current governed delivery assessment for this contractor workstream.

Project-level acceptance of the Azure MVP direction is recorded separately under `docs/02-architecture/azure-mvp-platform-decision.md`, and the evidence-gated delivery sequence is recorded under `docs/09-delivery/azure-mvp-platform-delivery-plan.md`.

## Confirmed contractor identity

`SRC-017` records the project-owner attestation that GitHub account `HarleyJoker` is associated with **HerLogic Solutions** as a contractor for Ubuntu Capital and that `mbuyanaledi@gmail.com` was supplied as that account/contact identity. The `HarleyJoker` account owns the current implementation repository `HarleyJoker/ubuntu-capital-platform`.

The repository also preserves the exact Git-object author/committer identity for the Azure architecture/cost commits as `mbuyazinaledi <mbuyazinaledi@gmail.com>` under `SRC-015`. Because the two email strings differ, the repository does not silently treat them as the same email alias/credential without separate evidence. This distinction preserves exact Git provenance while still recording the confirmed contractor affiliation supplied by the project owner.

## Evidence boundary

HerLogic Solutions' recorded architecture and cost contribution helps guide implementation, but it does not by itself prove that Azure resources are provisioned, configured, deployed, integrated, or tested.

Contractor contribution does not independently:

- change authoritative business or legal requirements;
- establish production readiness;
- mark Azure infrastructure `COMPONENT_COMPLETE` without deployment evidence;
- mark any Ubuntu Capital use case `COMPLETE`.

Use `contribution-log.md` for confirmed contributor/artifact provenance, `implementation-status.md` as the current contractor-workstream status record, and apply the evidence gates in `AGENT.md`, `plan.md`, delivery and traceability artifacts before changing status.
