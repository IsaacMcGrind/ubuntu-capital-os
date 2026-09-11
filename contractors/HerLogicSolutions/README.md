# HerLogic Solutions — Ubuntu Capital Azure Workstream

This directory records HerLogic Solutions contribution provenance for the Ubuntu Capital Azure cloud architecture, cost, and infrastructure-delivery workstream.

## Submission contract

Within this Ubuntu Capital OS repository, this contractor workstream records factual, sanitised implementation evidence only. 80K Developers (Pty) Ltd is the appointed Project Manager contractor and accountable project-management workstream. Thembinkosi Mtsweni is the responsible human Project Manager and project-owner decision authority acting for 80K Developers; in that capacity, he retains authority to interpret and accept evidence, update canonical OS artifacts and delivery status, set priorities, approve gates, and authorise subsequent work.

An evidence submission may record:

- assigned work package and scope;
- work actually performed, responsible contributor and date;
- revision-pinned implementation or resource references where safe;
- commands or procedures used;
- validation executed and results;
- limitations, unfinished work, blockers and dependencies;
- decisions or clarification required from the Project Manager.

An evidence submission must not:

- approve or authorise work;
- create, replace or reinterpret a project gate;
- change canonical project, work-package or use-case status;
- declare a work package or use case complete;
- make an Ubuntu Capital architecture, business, legal or commercial decision;
- broaden the contractor's assigned scope;
- present unsupported or unpinned implementation observations as current fact.

Evidence must not expose secrets, credentials, tokens, private personal information, raw sensitive cloud exports or unnecessary infrastructure identifiers. Merging an evidence PR records evidence only; it does not promote status or authorise further work. The Project Manager performs repository-wide analysis and any canonical OS update separately after evidence is merged.

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
