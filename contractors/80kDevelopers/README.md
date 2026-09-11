# 80K Developers — Ubuntu Capital Implementation Context

## Purpose

This directory records the implementation work attributed to 80K Developers and the evidence available to Ubuntu Capital OS about the currently deployed platform.

It is an implementation-provenance record. It does not replace the evidence-first reconstruction documents under `docs/` and it does not by itself prove end-to-end completion of any use case.

## Submission contract

Within this Ubuntu Capital OS repository, this contractor workstream records factual, sanitised implementation evidence only. 80K Developers (Pty) Ltd is the appointed Project Manager contractor and accountable project-management workstream. Thembinkosi Mtsweni is the responsible human Project Manager and project-owner decision authority acting for 80K Developers; in that capacity, he retains authority to interpret and accept evidence, update canonical OS artifacts and delivery status, set priorities, approve gates, and authorise subsequent work.

80K Developers may also perform implementation or coding work. When it does, the resulting submission remains evidence-only and must not self-accept, self-promote status or rely on 80K's Project Manager appointment to bypass review. An 80K Developers change exercises Project Manager authority only when it is explicitly identified as Project-Manager-owned governance work and is kept separate from technical evidence capture.

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

## Current Implementation

- **Implemented website:** https://80kdevelopers.com/ubuntucapital/
- **Implementation source repository:** https://github.com/HarleyJoker/ubuntu-capital-platform
- **Repository owner:** `HarleyJoker`
- **Repository stated as shared with the Ubuntu Capital project owner:** Yes, based on user-provided project evidence.
- **Historical ChatGPT GitHub connector access attempt:** Blocked at the recorded attempt; the connector returned `404 Not Found` for `HarleyJoker/ubuntu-capital-platform`.
- **Recorded inspection position:** A local-workspace inspection and 41-use-case reconciliation were reported, but the inspected source branch, commit SHA, run identity, and durable raw evidence reference are not recorded. Treat the mapped coverage as historical/partial evidence, not as current reproducible source verification.

## What Has Been Done

Based on the current evidence supplied to Ubuntu Capital OS:

1. An Ubuntu Capital website implementation has been deployed at `https://80kdevelopers.com/ubuntucapital/`.
2. The implementation code is stated to reside in `HarleyJoker/ubuntu-capital-platform`.
3. The repository has been shared with the project owner on GitHub.
4. A historical ChatGPT GitHub connector attempt returned `404 Not Found`; that result is retained only as access-attempt evidence.
5. A local-workspace inspection and reconciliation against all 41 catalogued use cases were reported in repository artifacts.
6. Because the inspected source revision and durable run evidence are not pinned, those coverage records are historical/partial evidence only; they do not establish the current `ubuntu-capital-platform` head or mark any use case `COMPLETE`.

## Evidence Classification

| Item | Classification | Delivery Status | Reason |
|---|---|---|---|
| Deployed Ubuntu Capital website URL | CONFIRMED | COMPONENT_COMPLETE | Directly supplied as the current implemented website by the project owner. |
| Implementation repository URL | CONFIRMED | COMPONENT_COMPLETE | Directly supplied as the repository containing the implementation. |
| Repository shared with project owner | CONFIRMED | COMPONENT_COMPLETE | Directly stated by the project owner. |
| Historical ChatGPT connector access attempt | CONFIRMED | BLOCKED_BY_CONTEXT | The recorded attempt returned `404 Not Found`; this classifies that access path and time only, not the later local inspection. |
| Exact source revision and durable inspection run | UNKNOWN | BLOCKED_BY_CONTEXT | The inspected branch/commit SHA and durable run/evidence reference are absent, so the local inspection cannot be reproduced or treated as current source verification. |
| Existence of 41-use-case coverage artifacts | CONFIRMED | ANALYSIS_IN_PROGRESS | Coverage artifacts exist and distinguish UI/prototype, partial, missing, and E2E-unproven behaviour; their source-revision provenance remains incomplete. |
| Production readiness | CONFIRMED | BLOCKED_BY_CONTEXT | The current repository gate remains `NO-GO FOR UNRESTRICTED IMPLEMENTATION`; no complete E2E, security, integration, settlement, audit, or operational acceptance evidence has been established. |

The connector failure is **not** classified as `CONTRADICTED`. A `404 Not Found` does not establish incompatible source descriptions; it establishes an access/context blocker for that recorded attempt. The later reported local inspection is separate historical evidence, but it remains non-reproducible until its exact source revision and durable run record are added.

## Remaining Reconciliation and Evidence Work

The current source state is not verified by a durable pinned inspection. The next authorised review of `HarleyJoker/ubuntu-capital-platform` must:

1. Record the exact source branch and commit SHA, inspection date/run identity, and durable evidence reference before treating the resulting coverage as current or reproducible.
2. Refresh the technology-stack and application-architecture inventory.
3. Identify routes, pages, components, services, APIs, databases, external integrations, and deployment configuration.
4. Map implementation evidence to every relevant Ubuntu Capital OS use-case ID.
5. Identify features implemented outside the current 41-use-case catalogue and classify them before adding new use cases.
6. Update the E2E delivery tracker using objective implementation evidence.
7. Separate visual/UI completion from full business-process completion.
8. Record missing regulated, financial, security, audit, support, and recovery behaviour as gaps rather than silently treating the website as complete.

See `implementation-status.md` for the current contractor delivery snapshot.
