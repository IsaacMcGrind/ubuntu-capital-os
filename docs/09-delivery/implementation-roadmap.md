# Implementation Roadmap

This roadmap separates a faithful reconstruction programme from later Ubuntu Capital enhancements. No production investment transaction should be released until critical legal, compliance, settlement, custody, and permission questions are resolved.

## Phase 0 — Context and Architecture Baseline

**Included work:** source inventory, glossary, actors, permissions, system boundary, entities, environments, evidence register, open questions, JSON schemas, testing and evidence strategy.

**Business outcome:** stakeholders share a traceable understanding of the target system.

**Technical outcome:** repository conventions, IDs, schemas, architecture decision process, and E2E evidence standards exist.

**Exit criteria:** critical source gaps are registered; no inferred behaviour is labelled confirmed; first slice is approved.

## Phase 1 — Foundational Capabilities

**Included use cases:** UC-IAM-001, foundational parts of UC-ADMIN-003 and UC-AUD-001.

**Business outcome:** authorised users can enter a protected investor workspace.

**Technical outcome:** identity, session controls, route protection, role/data-scope enforcement, shared validation, error handling, configuration, and audit foundations.

**Required evidence:** positive/negative access tests, session tests, audit records, deployment reference, security review.

## Phase 2 — First Complete Vertical Slice: Discover and Express Interest

**Included use cases:** UC-OPP-001, UC-OPP-002, UC-OPP-003 and a deliberately non-binding interest-capture subset of UC-INV-001.

**Business outcome:** an authorised investor can discover a published opportunity, inspect its details, and submit a traceable expression of interest without moving money.

**Technical outcome:** investor UI, catalogue API, domain validation, persistence, access enforcement, audit, operational visibility, automated tests, and E2E acceptance work together.

**Why this slice:** it proves the core marketplace architecture while avoiding unsupported assumptions about regulated commitment and settlement behaviour.

**Exit criteria:** opportunity discovery and interest submission pass valid, invalid, duplicate, unauthorised, unavailable-opportunity, and system-failure scenarios with evidence.

## Phase 3 — Controlled Due Diligence and Investor Onboarding

**Included use cases:** UC-ONB-001 to UC-ONB-003, UC-DD-001, UC-DD-002, UC-PROFILE-001.

**Business outcome:** prospective investors can become eligible and receive controlled access to restricted deal material.

**Technical outcome:** onboarding states, document capture, eligibility rules, compliance review, agreement evidence, restricted document access, expiry/revocation, and notifications.

**Exit criteria:** compliance and legal owners approve rules; inferred integration behaviour is verified; access leakage tests pass.

## Phase 4 — Investment Commitment and External Integrations

**Included use cases:** UC-INV-001 to UC-INV-003, UC-INT-001 to UC-INT-003.

**Business outcome:** eligible investors can submit and manage commitments under approved business and legal rules.

**Technical outcome:** commitment lifecycle, approvals, idempotency, limits, retries, agreement execution, notifications, audit, and operational recovery.

**Exit criteria:** binding/non-binding status is explicit; all critical states and exception paths are validated against approved reference behaviour.

## Phase 5 — Funding, Settlement, and Reconciliation

**Included use cases:** UC-SET-001 to UC-SET-003 and UC-INT-004.

**Business outcome:** accepted commitments can be funded, matched, reconciled, and resolved safely.

**Technical outcome:** settlement instructions, immutable references, partial/duplicate/late/reversed payment handling, reconciliation, manual controls, maker-checker approval, monitoring, and recovery.

**Exit criteria:** payment/banking model, custody responsibilities, segregation, refunds, chargebacks, and reconciliation ownership are confirmed; failure simulations pass.

## Phase 6 — Portfolio, Documents, Administration, and Support

**Included use cases:** UC-PORT-001 to UC-PORT-004, UC-DOC-001, UC-NEWS-001, UC-EVENT-001, UC-REF-001, UC-OPS-001, UC-OPS-002, UC-ADMIN-001 to UC-ADMIN-004.

**Business outcome:** investors can manage their post-investment relationship while authorised teams operate the platform.

**Technical outcome:** holdings, valuations, performance calculations, activity, document access, content, opportunity lifecycle administration, support tooling, controlled corrections, and role enforcement.

**Exit criteria:** valuation and performance rules reconcile to approved examples; document access and operational overrides are auditable.

## Phase 7 — Reporting, Compliance, and Production Hardening

**Included use cases:** UC-AUD-001, UC-AUD-002, UC-REPORT-001, UC-NOTIFY-001 and cross-cutting hardening.

**Business outcome:** management, compliance, operations, and investors can rely on a secure and supportable production service.

**Technical outcome:** reporting, retention, observability, backup/recovery, resilience, performance, privacy, security-event response, operational documentation, and failure simulation.

**Exit criteria:** production readiness review passes; critical open questions are closed; E2E evidence is complete; recovery objectives are demonstrated.

## Programme gate

Current readiness is `READY_WITH_ASSUMPTIONS` for a discovery-and-interest prototype, but `PARTIALLY_READY` for a regulated production investment platform because onboarding, compliance, commitment, settlement, custody, valuation, internal permissions, and integration details remain incompletely evidenced.

## Backlog translation artifact

Use `docs/09-delivery/prioritized-backlog-diff.md` as the direct matrix-to-backlog translation for the current implementation gap pass.

- It prioritizes critical domains first: IAM, ONB, INV, SET, ADMIN, AUD, INT.
- It maps each use-case gap row to concrete backlog item IDs and acceptance checks.
- It includes dependency-first sequencing deltas for implementation order.
