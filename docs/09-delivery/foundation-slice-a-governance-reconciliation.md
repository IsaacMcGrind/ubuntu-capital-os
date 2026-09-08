# Ubuntu Capital OS — Foundation Slice A Governance Reconciliation

> **Current Foundation decision — 2026-09-07:** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001`. The execution gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. This authorises governed start only; implementation, completion, business-use-case and production claims remain evidence-gated. Source: `SRC-020`.

**Status:** `ANALYSIS_IN_PROGRESS`  
**Evidence classification:** `CONFIRMED`  
**Assessment date:** 2026-08-30  
**Related merged PR:** #18 — Foundation Slice A execution package  
**Controlling documents:** `AGENT.md`, `plan.md`  
**Related delivery artifacts:** `docs/09-delivery/implementation-roadmap.md`, `docs/09-delivery/azure-mvp-platform-delivery-plan.md`, `docs/09-delivery/foundation-slice-a-execution-package.md`, `docs/09-delivery/foundation-slice-a-evidence-register.md`
**Effective revalidated decision:** `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md` (`GO-2026-09-05-FSA-001`); effective execution gate: `OPEN_FOR_AUTHORISED_EXECUTION`

## Current applicability and compatibility rule

This document remains a compatibility start-gate reference because several live Foundation delivery artifacts point to it. It must **not** be interpreted as a self-contained current authorisation test.

For any live reference to this document from the Foundation execution package, Azure delivery plan, implementation roadmap, or related delivery artifact, the current gate is the combined test formed by:

1. this governance reconciliation;
2. `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md`;
3. the current `AGENT.md` and controlling `plan.md`; and
4. a new or explicitly revalidated execution-authorising `GO` or scoped `CONDITIONAL_GO`, recorded by the defined readiness authority only after the controlling prerequisites reconcile.

Satisfying only the 2026-08-30 checklist is **necessary but not sufficient** to start or advance `WP-AZ-001` through `WP-AZ-008`. The 2026-09-03 reassessment adds the current ADR, security, privacy, NFR, traceability, validation, business/legal, architecture-structure, readiness-authority, and formal-readiness-decision requirements. Those requirements were accepted as reconciled in the project-owner formal review recorded by `SRC-020`. Foundation execution is now authorised, while implementation status and completion remain evidence-gated.

The traceability terms in this document use the current two-stage model from `plan.md` and the reassessment: **planned pre-start traceability** is required before an execution-authorising decision; **realised implementation/test/durable-evidence traceability** is produced only after authorised delivery begins and governs later status promotion and acceptance. No retained wording in this compatibility document may be read as requiring post-build evidence before the start decision.

## 2026-09-05 execution amendment

`GO-2026-09-05-FSA-001` is the current execution authority for `WP-AZ-001` through `WP-AZ-008` after the project-owner formal review recorded by `SRC-020`. The effective gate is `OPEN_FOR_AUTHORISED_EXECUTION`: historical undefined-authority, open-`OQ-016`, and interim pending-revalidation wording is superseded. Evidence gates and all non-waivable boundaries remain in force.

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
- **planned pre-start traceability** for the proposed scope as `source -> use case -> backlog -> architecture/design (where applicable) -> planned implementation target -> planned test/validation target -> planned durable-evidence target -> planned tracker/status`, with stable repository-accessible IDs or targets;
- open-question and risk linkage;
- required schemas and structured data outputs;
- canonical directory/output gaps identified by `plan.md` and `AGENT.md`;
- reconciliation of links, IDs, counts, evidence classifications, and required files.

The exact controlling test is not whether a document can be drafted around a missing artifact. The test is whether the repository satisfies the applicable `AGENT.md` validation rules and the Phase 0–4 exit criteria in `plan.md` sufficiently to permit implementation progression.

The current interpretation of that test is maintained in `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md`; if the two documents appear to differ, the newer reassessment governs current-state readiness reporting without overriding `AGENT.md` or `plan.md`.

After authorised Foundation delivery starts, the applicable planned targets must be progressively reconciled with **realised delivery traceability** as `source -> use case -> backlog -> architecture/design (where applicable) -> implementation evidence -> test/run evidence -> durable evidence -> validation/status`. Missing required realised hops block the affected status promotion, `COMPONENT_COMPLETE`, E2E readiness, or acceptance; they are not prerequisites for the earlier start decision.

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
- planned pre-start traceability for any not-yet-authorised first-slice scope, using the same stable planned chain defined in Section 3;
- validation coverage for success and mandatory negative paths;
- open-question and risk reconciliation for anything that could invalidate the non-binding interpretation.

The Phase 5 foundational capability gate additionally requires objective evidence for the shared product capabilities that the first vertical slice depends on, including:

- application shell and route structure;
- authentication and session handling;
- role and permission enforcement;
- investor profile identity baseline;
- shared validation and safe error handling;
- protected API bootstrap/authorization probe and non-business test data;
- business audit-event framework, distinct from operational telemetry;
- structured logging and correlation IDs;
- persistence migrations;
- test harness and CI quality gates;
- environment configuration and secrets strategy.

Before Phase 6 business-slice work starts, the Phase 5 exit evidence must show that an authorised test investor can authenticate, establish a server-validated session, and call a protected bootstrap/authorization test surface; unauthenticated, insufficient-role, and cross-user access are denied and tested; and failures produce safe errors with traceable logs. The opportunity read model, seed/test data, access policy enforcement, and permitted catalogue API remain `WP-AZ-009` deliverables and are not Phase 5 exit prerequisites. A partially reconciled subset of the shared Phase 5 capabilities is not sufficient to start `WP-AZ-009` through `WP-AZ-012`.

Once first-slice execution is authorised and begins, realised implementation, test/run, durable-evidence and validation/status links are required for delivery-status promotion and acceptance in accordance with `plan.md` and `docs/10-traceability/traceability-matrix.md`.

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
- the first business vertical slice cannot reach `READY_FOR_ACCEPTANCE` without deployed E2E evidence and reconciled realised traceability;
- regulated settlement remains outside the first slice and blocked by unresolved legal/financial operating-model evidence;
- no Foundation package may start from this document alone; the current reassessment and an effective execution-authorising readiness decision are also mandatory;
- `NO_GO` may be recorded immediately while blockers remain; it does not authorise implementation and does not require the blockers or readiness-authority question to be closed first.

## 8. Dependency-aware next sequence

The active sequence is:

1. Apply `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md` to the current repository baseline and close or disposition its residual ADR, security, privacy, NFR, business/legal, planned-traceability, validation, and repository-structure items.
2. Preserve the closed `OQ-016` authority outcome and the effective formal revalidation recorded on 2026-09-07.
3. Begin the permitted `WP-AZ-001` through `WP-AZ-008` scope in governed dependency order and populate `docs/09-delivery/foundation-slice-a-evidence-register.md` with objective implementation evidence.
4. During authorised Foundation delivery, reconcile realised implementation/test-run/durable-evidence/status links against the planned chain; do not promote a package while a required realised hop is missing.
5. Reconcile all Foundation evidence gates; do not infer business-use-case completion from infrastructure completion.
6. Complete and evidence the `plan.md` Phase 5 shared foundational product capabilities and its exit criteria, including role/permission enforcement, protected API bootstrap/authorization testing, shared validation/error handling, business audit-event framework, persistence/observability foundations, and test harness/quality gates. Do not require the `WP-AZ-009` opportunity catalogue/API as an input to its own start gate.
7. Confirm the separate first-business-slice start gate is fully satisfied.
8. Only then start or advance `WP-AZ-009` through `WP-AZ-012` as Phase 6 business-slice work.
9. Complete first-slice business-audit evidence and deployed E2E acceptance evidence before considering `READY_FOR_ACCEPTANCE`.

## 9. Definition of reconciliation complete

This governance reconciliation may move beyond `ANALYSIS_IN_PROGRESS` only when:

- the repository no longer relies on a parallel-work interpretation that conflicts with the controlling integrity rules;
- required pre-implementation outputs and **planned pre-start traceability** are reconciled before Foundation implementation starts;
- after all controlling prerequisites reconcile, the defined readiness authority records a new or explicitly revalidated execution-authorising `GO` or scoped `CONDITIONAL_GO` before any Foundation work starts;
- the `docs/02-architecture/` structure exception has been formally dispositioned or the canonical structure has been amended;
- Blob Storage is explicitly selected-but-deferred rather than silently omitted;
- operational telemetry is distinguished from business audit evidence;
- no Foundation or use-case status is promoted because documentation exists;
- after execution starts, required realised implementation/test/durable-evidence/status traceability is reconciled before the affected status promotion or acceptance;
- `WP-AZ-009` through `WP-AZ-012` are explicitly blocked from starting or advancing until both the first-slice integrity prerequisites and the controlling Phase 5 foundational product-capability exit criteria reconcile.
