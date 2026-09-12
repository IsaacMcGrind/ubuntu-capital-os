# Ubuntu Capital OS — Pre-Implementation Gate Reassessment

**Status:** `ANALYSIS_IN_PROGRESS` with post-baseline amendments (historical baseline; superseded as current execution decision)  
**Original assessment date:** 2026-09-03  
**Original evidence baseline:** `master` through merged PR #24 at merge commit `2a44d3622d1e410e3eca82d6f21be3bea3ecf8d3`  
**Post-baseline amendment date:** 2026-09-04  
**Post-baseline amendment branch:** `fix/reconcile-current-repository-status` (PR #27)  
**Post-baseline evidence commit:** `2148ac6b36fde26a427c741e7b59ecc82ef6fbce`  
**Amendment scope:** the current findings and execution sequence incorporate PR #27's readiness-authority control (`OQ-016`), linked risk (`RSK-006`), planned-versus-realised traceability model, pre-start E2E criterion, Phase 5/Phase 6 handoff, and reconciled live delivery entry points. The original PR #24 baseline remains preserved as the starting snapshot rather than being represented as containing those later controls.  
**Controlling documents:** `AGENT.md`, `plan.md`  
**Current Foundation gate at assessment time:** this reassessment plus `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` and a formal readiness decision  
**Superseded by effective revalidated decision:** `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md` (`GO-2026-09-05-FSA-001`) for current execution authority
**Supersedes for current-state reporting:** the stale assumption that canonical Phase 0–4 outputs are absent

## 1. Purpose

This reassessment reconciles the 2026-08-30 Foundation governance finding against the newer repository state created by commit `d2d6f7bfe90ef04ec846eb11308cf551977cd33d` and the subsequently merged Phase 1 MVP Blueprint / Solution Architecture readiness material.

The earlier governance finding correctly blocked Foundation execution because required Phase 0–4 outputs and repository-integrity conditions did not reconcile at that time. Since then, the repository has materially advanced. The current gate must therefore be based on the quality, approval and internal consistency of the artifacts that now exist—not on an outdated assertion that those directories or files are missing.

Any Foundation delivery artifact that still points to `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` must be read through that document's compatibility rule: the older checklist is necessary but not sufficient, and this reassessment plus an effective formal readiness decision are mandatory before Foundation implementation starts or advances.

## 1.1 Current status amendment — 2026-09-07

Thembinkosi Mtsweni, as Ubuntu Capital project owner and final approving authority, completed the formal post-prerequisite readiness review and explicitly revalidated `GO-2026-09-05-FSA-001`. `OQ-016` is closed, readiness-decision authority is defined, and the scope gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. Contractors may self-select and begin in-scope work without assignment or a Project Manager pre-start record. Source: `SRC-020`.

For current execution decisions, this amendment supersedes the historical `OQ-016`-open, authority-`UNKNOWN`, effective-`NO_GO`, and pre-revalidation statements retained in Sections 3, 4 and 4.1. Those statements remain dated assessment history and must not be treated as current blockers. The revalidated GO defines the bounded scope without allocating work: all eight implementation evidence gates remain unsatisfied, contractor start is `OPEN_FOR_SELF_SELECTION`, package status remains `READY_FOR_DEVELOPMENT` until start evidence is accepted and canonically reconciled, `WP-AZ-009` through `WP-AZ-012` remain separately blocked, and production remains unauthorised.

`SRC-021` subsequently establishes the ongoing management/evidence workflow: technical contractors keep repository-hosted first-pass evidence in their contractor folders; contractor evidence merges as provenance only; and the 80K Developers Project Manager workstream separately assesses accepted evidence and reconciles canonical records through a distinct `PROJECT_MANAGER_GOVERNANCE` PR. The same governance amendment adds the existing `docs/02-architecture/` tree to the canonical `plan.md` contract, resolving the former structure exception without treating its contents as approved or complete. It also distinguishes the scope-level GO from each contractor's later evidence-PR declaration; no work-allocation record is required.

## 2. Current repository-output presence

The following plan-required outputs are now present in the repository and must no longer be described as absent:

- `docs/02-actors-and-permissions/actors.md`
- `docs/02-actors-and-permissions/permissions-matrix.md`
- `docs/03-functional-domains/capability-map.md`
- detailed `docs/04-use-cases/UC-*.md` specifications
- `docs/05-business-rules/business-rules.md`
- `docs/06-journeys/` journey artifacts
- `docs/07-state-models/state-models.md`
- `docs/08-integrations/integration-catalogue.md`
- `docs/09-delivery/backlog.md`
- `docs/09-delivery/backlog.json`
- `docs/09-delivery/e2e-delivery-tracker.md`
- `docs/10-traceability/traceability-matrix.md`
- `docs/12-validation/validation-plan.md`
- `docs/13-risks/gap-and-risk-register.md`
- `schemas/` for the structured reconstruction artifacts
- `data/use-cases.json`
- `data/backlog.json`
- `data/journeys.json`
- `data/state-models.json`
- `data/integrations.json`

The presence of these outputs is evidence of reconstruction progress only. It is not itself evidence that the relevant phase exit criteria are satisfied.

## 3. Historical reassessed gate position at the 2026-09-03 baseline

The evidence classification below applies to the **repository-state finding**, not to the underlying business rule or regulated behaviour. Each row is `CONFIRMED` because the stated current position is directly supported by repository artifacts, open-question/risk records, delivery evidence registers, or the current Solution Architecture audit. Where the underlying product behaviour remains inferred or unknown, this reassessment does not promote it to confirmed.

| Gate area | Current position | Evidence classification | Reason |
|---|---|---|---|
| Canonical file/directory presence | `MATERIALLY_RECONCILED` | `CONFIRMED` | The previously missing actors/permissions and other Phase 0–4 outputs now exist. |
| Architecture-tree disposition | `NOT_SATISFIED` | `CONFIRMED` | `docs/02-architecture/` is an active working architecture tree but is not declared in the canonical required-output tree in `plan.md`; this exception must be formally accepted/dispositioned or the canonical contract amended. |
| Actor and permission definition | `PARTIAL` | `CONFIRMED` | Artifacts exist, but several roles/permissions remain `INFERRED` or `UNKNOWN` and are not production approvals. |
| Use-case specification | `PARTIAL` | `CONFIRMED` | Detailed files and structured data exist, but regulated/business semantics remain unresolved in several areas. |
| Journeys/state/integration models | `PARTIAL` | `CONFIRMED` | Models exist; several transitions/providers/rules remain inferred or unknown. |
| Backlog/tracker/traceability | `PARTIAL` | `CONFIRMED` | Artifacts exist. Pre-start traceability must identify stable planned links from source/use case through backlog, design, planned implementation, planned validation/test, planned evidence target and tracker/status; actual implementation/test-run/durable-evidence links are populated only after authorised delivery begins. |
| Validation/evidence | `PARTIAL` | `CONFIRMED` | Validation artifacts exist, but security, persistence, integration and deployed E2E evidence remain incomplete. |
| Architecture/security/NFR decisions | `NOT_SATISFIED` | `CONFIRMED` | Threat model, privacy/retention, availability/performance, RTO/RPO, recovery, cost guardrails and several ADRs remain unresolved. |
| First-slice technical contracts | `NOT_SATISFIED` | `CONFIRMED` | The Solution Architecture audit still requires completion of the first-slice API, error, audit, persistence and integration contracts before Foundation implementation. |
| Azure Foundation evidence | `NOT_STARTED` | `CONFIRMED` | `WP-AZ-001` through `WP-AZ-008` still have 0 of 8 objective evidence gates satisfied. |
| Business/legal readiness for first slice | `NOT_SATISFIED` | `CONFIRMED` | EOI meaning, eligibility/jurisdiction, NDA policy, operator authority and data ownership remain open. |
| Readiness-decision authority | `NOT_SATISFIED` | `CONFIRMED` | Canonical open question `OQ-016` remains open: the repository does not yet define which approved role/person may issue an execution-authorising `GO` or `CONDITIONAL_GO`, so no such decision can currently open the gate. |

## 4. Historical Foundation decision at the 2026-09-03 baseline

**Decision: `NO-GO FOR UNRESTRICTED IMPLEMENTATION`**

This is not because the canonical repository outputs are missing. It is because several required exit criteria remain incomplete, inconsistent or unapproved.

The gate is therefore narrowed from a broad "missing repository structure" blocker to the following substantive closure set:

1. formally disposition the `docs/02-architecture/` structure exception by either amending the canonical `plan.md` tree or explicitly recording an approved exception that does not conflict with `AGENT.md`;
2. approve or explicitly disposition actor/role/permission rules required by the Foundation and first slice;
3. close or formally bound the unresolved EOI, jurisdiction/eligibility, NDA and operator-authority decisions that could invalidate the first-slice interpretation;
4. complete logical data ownership and authoritative state-transition decisions for the first slice;
5. complete the required threat model, authorization design, privacy/retention position and measurable NFR baseline;
6. complete the first-slice API, error, audit, persistence and integration contracts required by the Solution Architecture P0 closure set;
7. complete the minimum ADR set identified by the Solution Architecture readiness audit;
8. before a readiness decision can authorise implementation, reconcile **planned pre-start traceability** for the proposed scope as `source -> use case -> backlog -> architecture/design (where applicable) -> planned implementation target -> planned test/validation -> planned durable-evidence target -> planned tracker/status`. Every planned hop must have a stable repository-accessible ID or target. The start gate does **not** require implementation, test-run, deployment or durable evidence that can only be produced after authorised execution begins;
9. after authorised implementation begins, progressively replace the planned targets with **realised delivery traceability** as `source -> use case -> backlog -> architecture/design (where applicable) -> implementation evidence -> test/run evidence -> durable evidence -> validation/status`, and do not promote the affected work package or use case while a required realised hop remains `Pending`;
10. demonstrate that structured data/schema validation, links, IDs, counts, open-question/risk references and status values reconcile;
11. resolve canonical open question `OQ-016` by defining, in the controlling governance, the approving authority and decision-control contract for any execution-authorising readiness decision;
12. a formal readiness review may record `NO_GO` immediately whenever blockers, integrity failures, partial required planned traceability, or undefined readiness authority remain. An execution-authorising `GO` or `CONDITIONAL_GO` may be issued only after the decision-control contract, required **planned pre-start** traceability, and every other non-waivable closure condition applicable to that scope are satisfied.

A readiness review **must not issue `GO` or `CONDITIONAL_GO` for a scope whose required planned pre-start traceability is partial**. It must also **not** require post-build implementation/test/deployment/durable-evidence records as a prerequisite to starting the very work that will produce them. A general reference to `backlog.json`, an undefined future test, or an E2E tracker row without stable planned targets does not satisfy the pre-start closure condition. Once execution begins, the stricter realised traceability and evidence rules govern status promotion and acceptance.

A `NO_GO` outcome is different: it is a non-authorising blocked-state finding and may be recorded or refreshed as soon as unresolved blockers are identified. Recording `NO_GO` does not require those blockers to be closed first and does not depend on resolving `OQ-016`; `OQ-016` must be resolved before `GO` or `CONDITIONAL_GO` can carry execution authority.

### 4.1 Historical readiness-authority finding and continuing `CONDITIONAL_GO` controls

**Historical authority status at this assessment baseline: `UNKNOWN` (`OQ-016`) — superseded for current execution by `SRC-020` and `SRC-021`.** At the 2026-09-03 baseline no repository artifact identified an approved execution-authorising role/person, so `GO` and `CONDITIONAL_GO` could not then open the Foundation gate. The current bounded authority is recorded by the 2026-09-07 project-owner revalidation and the subsequent management model; the non-waivable decision controls below continue to apply to future or changed scope.

Before a future `CONDITIONAL_GO` can authorise any Foundation work, the controlling governance must identify the approving authority and the decision record must include all of the following:

- decision ID, date, approver identity/role and evidence of that authority;
- exact authorised work-package scope (`WP-AZ-*` IDs) and environment;
- every open condition, residual risk and dependency relevant to that scope;
- named owner and due date for each condition;
- explicit evidence required to close each condition;
- expiry/review date or trigger that automatically returns the scope to `BLOCKED_BY_CONTEXT` if conditions are not closed;
- explicit statement that no unlisted work package is authorised;
- links to the evidence/register entries supporting the decision.

A `CONDITIONAL_GO` **cannot waive or override** any `AGENT.md` repository-integrity stop condition. In particular, it cannot authorise progression while there are broken/missing controlling links, unreconciled required outputs, schema-validation failures, duplicate/conflicting canonical IDs or directories, broken required **planned pre-start traceability**, unsupported `CONFIRMED` claims, or unresolved contradictions material to the authorised scope. It also cannot waive unresolved legal/regulatory/business semantics that determine whether the proposed implementation behaviour is valid. Any such condition keeps the affected scope `BLOCKED_BY_CONTEXT` and requires `NO_GO` for that scope until repaired.

`NO_GO` does not grant execution authority and therefore does not require the execution-authorising authority defined by `OQ-016` to already be resolved. A readiness assessment or review may durably record `NO_GO` with its date, evaluated scope, blocking reasons and supporting evidence while `OQ-016` itself remains open.

## 5. What is no longer a blocker

The following statements are obsolete and must not be used as current blockers:

- that `docs/02-actors-and-permissions/` is missing;
- that actors and permissions have not been produced at all;
- that journeys and state models have not been created at all;
- that integration, validation, backlog, tracker, traceability or structured-data artifacts are entirely absent;
- that the immediate queue should recreate those artifacts from scratch.

Those artifacts may still require completion, approval, correction or validation. The work is now **reconciliation and closure**, not initial creation.

At this historical baseline, the `docs/02-architecture/` relationship was an unresolved structural exception. The current `plan.md` now includes the existing architecture tree under the project-owner-authorised `SRC-021` amendment, so that structural blocker is resolved; substantive architecture evidence and approval gaps remain governed separately.

## 6. Current execution sequence

Completed prerequisite: the project-owner review recorded by `SRC-020` accepted the bounded Foundation prerequisite reconciliation, closed `OQ-016`, and revalidated `GO-2026-09-05-FSA-001` on 2026-09-07. Reopen readiness only for a material baseline, scope, risk, or non-waivable evidence change.

1. Contractors self-select and begin any `WP-AZ-001` through `WP-AZ-008` subset in governed dependency order without assignment or a Project Manager pre-start record.
2. The contractor's evidence PR documents the submitting contractor, selected package/path scope, evidence purpose, and applicable external implementation/resource scope.
3. Each technical contractor records objective, sanitised, revision-pinned first-pass evidence only under its applicable contractor folder; approved external raw evidence is represented by a sanitised stable reference there.
4. Review and merge contractor evidence as provenance only.
5. The 80K Developers Project Manager workstream separately assesses merged evidence and, when accepted, reconciles the canonical Foundation evidence register, realised chain, and status through a distinct `PROJECT_MANAGER_GOVERNANCE` PR.
6. Required realised hops govern status promotion, `COMPONENT_COMPLETE`, E2E readiness, and acceptance rather than the already-completed bounded start decision.
7. Keep `WP-AZ-009` through `WP-AZ-012` blocked until Foundation evidence and the separate Phase 5 / first-business-slice gate are satisfied.

## 7. Status boundary

This reassessment does not:

- claim Azure resources are provisioned;
- promote any `WP-AZ-*` work package;
- mark any use case `COMPLETE`;
- convert inferred permissions or regulated behaviour into confirmed facts;
- silently treat the architecture-tree exception as resolved;
- define an approving authority where the repository currently has none;
- allow a conditional decision to waive `AGENT.md` integrity failures;
- require blockers to be closed before a non-authorising `NO_GO` can be recorded;
- require post-build implementation/test/evidence as a prerequisite to starting authorised work;
- override `AGENT.md` or `plan.md`.

It corrects the repository's current-state reporting so that the remaining block is based on **substantive readiness evidence, explicit structural disposition, controlled decision authority and non-waivable integrity requirements**, not stale file-presence assumptions.
