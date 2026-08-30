# Ubuntu Capital OS — Foundation Slice A Governance Reconciliation

**Status:** `ANALYSIS_IN_PROGRESS`  
**Evidence classification:** `CONFIRMED`  
**Assessment date:** 2026-08-30  
**Related merged PR:** #18 — Foundation Slice A execution package  
**Controlling documents:** `AGENT.md`, `plan.md`  
**Related delivery artifacts:** `docs/09-delivery/implementation-roadmap.md`, `docs/09-delivery/azure-mvp-platform-delivery-plan.md`, `docs/09-delivery/foundation-slice-a-execution-package.md`, `docs/09-delivery/foundation-slice-a-evidence-register.md`

## 1. Purpose

This document records the post-merge repository-level review of Foundation Slice A against the full Ubuntu Capital OS governance context.

It exists to prevent the Foundation execution package from being interpreted as permission to bypass earlier evidence, traceability, canonical-output, or phase-exit requirements in `plan.md` and `AGENT.md`.

## 2. Review conclusion

The Foundation Slice A package is internally coherent as a future infrastructure execution package for `WP-AZ-001` through `WP-AZ-008`.

However, the wider repository still contains known reconstruction and canonical-structure gaps. `plan.md` remains the controlling execution plan, and `AGENT.md` requires progression to stop when required outputs, links, counts, traceability, or other integrity conditions do not reconcile.

Accordingly, **Foundation Slice A implementation must not start or advance while those prerequisite repository outputs remain materially incomplete or inconsistent**. The Foundation package may be maintained as planning documentation, but its work-package statuses must remain unchanged until the controlling prerequisites are reconciled.

No parallel-execution exception is created by this document. Any future exception to the ordered plan would need to be explicitly dependency-based and recorded in the controlling plan without conflicting with `AGENT.md` integrity rules.

## 3. Foundation execution prerequisite

Before `WP-AZ-001` through `WP-AZ-008` may begin or advance, the repository must reconcile the controlling Phase 0 through Phase 4 outputs and validation rules that precede implementation.

This includes, at minimum:

- canonical actor and permissions outputs;
- complete use-case specifications and business rules required by the planned first slice;
- journeys and state models;
- integration catalogue and validation design;
- development backlog and machine-readable backlog outputs;
- E2E delivery tracker;
- source-to-use-case-to-implementation-to-test/evidence traceability;
- open-question and risk linkage;
- required schemas and structured data outputs;
- canonical directory/output gaps identified by `plan.md` and `AGENT.md`;
- reconciliation of links, IDs, counts, evidence classifications, and required files.

The exact controlling test is not whether a document can be drafted around a missing artifact. The test is whether the repository satisfies the applicable `AGENT.md` validation rules and the Phase 0–4 exit criteria in `plan.md` sufficiently to permit implementation progression.

## 4. First-business-slice start gate

`WP-AZ-009`, `WP-AZ-010`, `WP-AZ-011`, and `WP-AZ-012` must not **start, advance, or be promoted** until all of the following are true:

1. Foundation Slice A (`WP-AZ-001` through `WP-AZ-008`) has satisfied its own objective evidence gates;
2. all plan-required outputs material to the first business slice are present and internally consistent; and
3. the `plan.md` Phase 5 foundational product capabilities and exit criteria required by Phase 6 are complete and evidenced before the business slice starts.

The first-slice integrity set includes:

- actor and permissions evidence for authenticated investor and authorised operator access;
- first-slice business rules and explicit non-binding EOI assumptions;
- first-slice journey and relevant state model;
- integration records for identity and any external dependencies used by the slice;
- backlog entries representing frontend, backend, persistence, security, audit, tests, deployment, documentation, and evidence work;
- E2E delivery tracking;
- source-to-use-case-to-implementation-to-test/evidence traceability;
- validation coverage for success and mandatory negative paths;
- open-question and risk reconciliation for anything that could invalidate the non-binding interpretation.

The Phase 5 foundational capability gate additionally requires objective evidence for the shared product capabilities that the first vertical slice depends on, including:

- application shell and route structure;
- authentication and session handling;
- role and permission enforcement;
- investor profile identity baseline;
- shared validation and safe error handling;
- opportunity read model/seed-data foundation required by the selected slice;
- business audit-event framework, distinct from operational telemetry;
- structured logging and correlation IDs;
- persistence migrations;
- test harness and CI quality gates;
- environment configuration and secrets strategy.

Before Phase 6 business-slice work starts, the Phase 5 exit evidence must show that an authorised test investor can authenticate and securely load a permitted opportunity catalogue, cross-user access is denied and tested, and failures produce safe errors with traceable logs. A partially reconciled subset is not sufficient to start `WP-AZ-009` through `WP-AZ-012`.

## 5. Azure Blob Storage scope clarification

`ARCH-ADR-001` confirms Azure Blob Storage as the selected platform service for documents and generated files.

Blob Storage is **selected but intentionally deferred from Foundation Slice A (`WP-AZ-001` through `WP-AZ-008`)** because the Foundation objective does not require confidential-document or report storage to prove the authenticated platform shell.

Blob implementation belongs with the first use case that actually requires document storage or controlled document access, such as due-diligence/data-room or investor-document delivery. At that point the delivery package must define container/access design, authorised backend mediation, retention requirements, and evidence gates.

The absence of a Blob work package in Foundation Slice A must therefore not be interpreted as reversing `ARCH-ADR-001` or as evidence that Blob has been implemented.

## 6. Audit and telemetry scope clarification

Foundation Slice A `WP-AZ-007` covers **operational telemetry and monitoring** through Application Insights and Azure Monitor.

It does not satisfy the business-audit requirement for `UC-AUD-001`.

The shared business audit-event framework required by `plan.md` Phase 5 must exist and be evidenced before Phase 6 business-slice implementation starts. `WP-AZ-011` then captures and verifies the concrete business-audit evidence produced by the first EOI slice, including actor, action, resource, outcome, timestamp, correlation, persistence, authorised review, and separation from transient application logs.

## 7. Status and evidence rules

The following rules remain controlling:

- architecture selection is not implementation evidence;
- planning documentation does not advance work-package delivery status;
- `WP-AZ-001` through `WP-AZ-008` remain at their existing recorded statuses until the Foundation execution prerequisite is satisfied and implementation evidence exists;
- a work package reaches `COMPONENT_COMPLETE` only when its own evidence gate is satisfied;
- Foundation completion does not promote any business use case to `COMPLETE`;
- `WP-AZ-009` through `WP-AZ-012` cannot start or advance until the first-business-slice start gate, including the required Phase 5 foundational product-capability exit criteria, is satisfied;
- the first business vertical slice cannot reach `READY_FOR_ACCEPTANCE` without deployed E2E evidence and reconciled traceability;
- regulated settlement remains outside the first slice and blocked by unresolved legal/financial operating-model evidence.

## 8. Dependency-aware next sequence

The active sequence is:

1. Reconcile the Phase 0 through Phase 4 repository outputs and integrity conditions required by `AGENT.md` and `plan.md`.
2. Only after that gate is satisfied, execute `WP-AZ-001` through `WP-AZ-008` and populate `foundation-slice-a-evidence-register.md` with objective implementation evidence.
3. Reconcile all Foundation evidence gates; do not infer business-use-case completion from infrastructure completion.
4. Complete and evidence the `plan.md` Phase 5 foundational product capabilities and its exit criteria, including role/permission enforcement, shared validation/error handling, business audit-event framework, test harness/quality gates, and the authorised permitted-opportunity catalogue path.
5. Confirm the separate first-business-slice start gate is fully satisfied.
6. Only then start or advance `WP-AZ-009` through `WP-AZ-012` as Phase 6 business-slice work.
7. Complete first-slice business-audit evidence and deployed E2E acceptance evidence before considering `READY_FOR_ACCEPTANCE`.

## 9. Definition of reconciliation complete

This governance reconciliation may move beyond `ANALYSIS_IN_PROGRESS` only when:

- the repository no longer relies on a parallel-work interpretation that conflicts with the controlling integrity rules;
- required pre-implementation outputs are reconciled before Foundation implementation starts;
- Blob Storage is explicitly selected-but-deferred rather than silently omitted;
- operational telemetry is distinguished from business audit evidence;
- no Foundation or use-case status is promoted because documentation exists;
- `WP-AZ-009` through `WP-AZ-012` are explicitly blocked from starting or advancing until both the first-slice integrity prerequisites and the controlling Phase 5 foundational product-capability exit criteria reconcile.
