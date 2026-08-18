# 80K Developers — Ubuntu Capital Implementation Context

## Purpose

This directory records the implementation work attributed to 80K Developers and the evidence available to Ubuntu Capital OS about the currently deployed platform.

It is an implementation-provenance record. It does not replace the evidence-first reconstruction documents under `docs/` and it does not by itself prove end-to-end completion of any use case.

## Current Implementation

- **Implemented website:** https://80kdevelopers.com/ubuntucapital/
- **Implementation source repository:** https://github.com/HarleyJoker/ubuntu-capital-platform
- **Repository owner:** `HarleyJoker`
- **Repository stated as shared with the Ubuntu Capital project owner:** Yes, based on user-provided project evidence.
- **Current ChatGPT GitHub connector access:** No. The connector returned `404 Not Found` when attempting to access `HarleyJoker/ubuntu-capital-platform`.

## What Has Been Done

Based on the current evidence supplied to Ubuntu Capital OS:

1. A Ubuntu Capital website implementation has been deployed at `https://80kdevelopers.com/ubuntucapital/`.
2. The implementation code is stated to reside in `HarleyJoker/ubuntu-capital-platform`.
3. The repository has been shared with the project owner on GitHub.
4. The current connected ChatGPT GitHub application cannot yet inspect that repository.
5. No claim is made yet about which of the 41 catalogued use cases are fully implemented, partially implemented, mocked, or absent.

## Evidence Classification

| Item | Classification | Reason |
|---|---|---|
| Deployed Ubuntu Capital website URL | CONFIRMED | Directly supplied as the current implemented website by the project owner. |
| Implementation repository URL | CONFIRMED | Directly supplied as the repository containing the implementation. |
| Repository shared with project owner | CONFIRMED | Directly stated by the project owner. |
| ChatGPT connector can inspect implementation repository | CONTRADICTED | Access attempt returned `404 Not Found`. |
| Exact implemented use-case coverage | UNKNOWN | Code and end-to-end website behaviour have not yet been inspected against the catalogue. |
| Production readiness | UNKNOWN | No complete E2E, security, integration, settlement, audit, or operational evidence has yet been mapped. |

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
