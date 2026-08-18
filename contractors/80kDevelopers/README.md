# 80K Developers — Ubuntu Capital Implementation Context

## Purpose

This directory records the implementation work attributed to 80K Developers and the evidence available to Ubuntu Capital OS about the currently deployed platform.

It is an implementation-provenance record. It does not replace the evidence-first reconstruction documents under `docs/` and it does not by itself prove end-to-end completion of any use case.

## Current Implementation

- **Implemented website:** https://80kdevelopers.com/ubuntucapital/
- **Implementation source repository:** https://github.com/HarleyJoker/ubuntu-capital-platform
- **Repository owner:** `HarleyJoker`
- **Repository stated as shared with the Ubuntu Capital project owner:** Yes, based on user-provided project evidence.
- **Current ChatGPT GitHub connector access:** Blocked. The connector returned `404 Not Found` when attempting to access `HarleyJoker/ubuntu-capital-platform`.

## What Has Been Done

Based on the current evidence supplied to Ubuntu Capital OS:

1. An Ubuntu Capital website implementation has been deployed at `https://80kdevelopers.com/ubuntucapital/`.
2. The implementation code is stated to reside in `HarleyJoker/ubuntu-capital-platform`.
3. The repository has been shared with the project owner on GitHub.
4. The current connected ChatGPT GitHub application cannot yet inspect that repository.
5. No claim is made yet about which of the 41 catalogued use cases are fully implemented, partially implemented, mocked, or absent.

## Evidence Classification

| Item | Classification | Delivery Status | Reason |
|---|---|---|---|
| Deployed Ubuntu Capital website URL | CONFIRMED | COMPONENT_COMPLETE | Directly supplied as the current implemented website by the project owner. |
| Implementation repository URL | CONFIRMED | COMPONENT_COMPLETE | Directly supplied as the repository containing the implementation. |
| Repository shared with project owner | CONFIRMED | COMPONENT_COMPLETE | Directly stated by the project owner. |
| ChatGPT connector access attempt | CONFIRMED | BLOCKED_BY_CONTEXT | The access attempt returned `404 Not Found`; this confirms only that the connector could not inspect the repository during this attempt. |
| Exact implemented use-case coverage | UNKNOWN | NOT_ANALYSED | Code and end-to-end website behaviour have not yet been inspected against the catalogue. |
| Production readiness | UNKNOWN | NOT_ANALYSED | No complete E2E, security, integration, settlement, audit, or operational evidence has yet been mapped. |

The connector failure is **not** classified as `CONTRADICTED`. A `404 Not Found` does not establish incompatible source descriptions; it establishes a current access/context blocker.

## Required Reconciliation Once Repository Access Is Available

When `HarleyJoker/ubuntu-capital-platform` becomes accessible, the next review must:

1. Read the implementation repository instructions and project documentation.
2. Inventory the technology stack and application architecture.
3. Identify routes, pages, components, services, APIs, databases, external integrations, and deployment configuration.
4. Map implementation evidence to every relevant Ubuntu Capital OS use-case ID.
5. Identify features implemented outside the current 41-use-case catalogue and classify them before adding new use cases.
6. Update the E2E delivery tracker using objective implementation evidence.
7. Separate visual/UI completion from full business-process completion.
8. Record missing regulated, financial, security, audit, support, and recovery behaviour as gaps rather than silently treating the website as complete.

See `implementation-status.md` for the current contractor delivery snapshot.
