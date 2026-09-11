# 80K Developers — Ubuntu Capital Implementation Context

## Purpose

This directory records the implementation work attributed to 80K Developers and the evidence available to Ubuntu Capital OS about the currently deployed platform.

It is an implementation-provenance record. It does not replace the evidence-first reconstruction documents under `docs/` and it does not by itself prove end-to-end completion of any use case.

## Submission contract

**Project role:** Under `SRC-021`, 80K Developers (Pty) Ltd is the appointed Project Manager contractor. Thembinkosi Mtsweni is the responsible human Project Manager and final project-owner decision authority.

80K Developers must declare one capacity in every PR:

- `PROJECT_MANAGER_GOVERNANCE` for an explicitly authorised canonical reconciliation or management decision; or
- `CONTRACTOR_TECHNICAL_EVIDENCE` for implementation, coding or other technical evidence.

Technical evidence from 80K Developers cannot self-accept, self-promote status or inherit management authority from the organization name. In `CONTRACTOR_TECHNICAL_EVIDENCE` capacity, all repository-hosted first-pass evidence must remain under `contractors/80kDevelopers/`; approved external raw evidence must be represented by a sanitised stable reference here, and canonical governance/status artifacts must not be changed in the same PR. Every PR must complete the project-owner-approved `.github/pull_request_template.md` (`SRC-021`); reviewers must verify the cited decision/context reference and authorised paths.

The canonical rules are `AGENT.md` and `plan.md`.

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
| Production readiness | CONFIRMED | BLOCKED_BY_CONTEXT | Bounded Azure DEV/MVP Foundation execution is authorised under `GO-2026-09-05-FSA-001`; unrestricted and production implementation remain `NO-GO` because complete E2E, security, integration, settlement, audit, and operational acceptance evidence has not been established. |

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
