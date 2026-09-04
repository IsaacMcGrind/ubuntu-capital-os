# Ubuntu Capital OS — Pre-Implementation Gate Reassessment

**Status:** `ANALYSIS_IN_PROGRESS`  
**Assessment date:** 2026-09-03  
**Evidence baseline:** current `master` through merged PR #24  
**Controlling documents:** `AGENT.md`, `plan.md`  
**Current Foundation gate:** this reassessment plus `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` and a formal readiness decision  
**Supersedes for current-state reporting:** the stale assumption that canonical Phase 0–4 outputs are absent

## 1. Purpose

This reassessment reconciles the 2026-08-30 Foundation governance finding against the newer repository state created by commit `d2d6f7bfe90ef04ec846eb11308cf551977cd33d` and the subsequently merged Phase 1 MVP Blueprint / Solution Architecture readiness material.

The earlier governance finding correctly blocked Foundation execution because required Phase 0–4 outputs and repository-integrity conditions did not reconcile at that time. Since then, the repository has materially advanced. The current gate must therefore be based on the quality, approval and internal consistency of the artifacts that now exist—not on an outdated assertion that those directories or files are missing.

Any Foundation delivery artifact that still points to `docs/09-delivery/foundation-slice-a-governance-reconciliation.md` must be read through that document's compatibility rule: the older checklist is necessary but not sufficient, and this reassessment plus an effective formal readiness decision are mandatory before Foundation implementation starts or advances.

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

## 3. Reassessed gate position

The evidence classification below applies to the **repository-state finding**, not to the underlying business rule or regulated behaviour. Each row is `CONFIRMED` because the stated current position is directly supported by repository artifacts, open-question/risk records, delivery evidence registers, or the current Solution Architecture audit. Where the underlying product behaviour remains inferred or unknown, this reassessment does not promote it to confirmed.

| Gate area | Current position | Evidence classification | Reason |
|---|---|---|---|
| Canonical file/directory presence | `MATERIALLY_RECONCILED` | `CONFIRMED` | The previously missing actors/permissions and other Phase 0–4 outputs now exist. |
| Architecture-tree disposition | `NOT_SATISFIED` | `CONFIRMED` | `docs/02-architecture/` is an active working architecture tree but is not declared in the canonical required-output tree in `plan.md`; this exception must be formally accepted/dispositioned or the canonical contract amended. |
| Actor and permission definition | `PARTIAL` | `CONFIRMED` | Artifacts exist, but several roles/permissions remain `INFERRED` or `UNKNOWN` and are not production approvals. |
| Use-case specification | `PARTIAL` | `CONFIRMED` | Detailed files and structured data exist, but regulated/business semantics remain unresolved in several areas. |
| Journeys/state/integration models | `PARTIAL` | `CONFIRMED` | Models exist; several transitions/providers/rules remain inferred or unknown. |
| Backlog/tracker/traceability | `PARTIAL` | `CONFIRMED` | Artifacts exist, but the required source -> use case -> backlog -> implementation -> test -> evidence chain is incomplete; the current matrix contains only partial chains. |
| Validation/evidence | `PARTIAL` | `CONFIRMED` | Validation artifacts exist, but security, persistence, integration and deployed E2E evidence remain incomplete. |
| Architecture/security/NFR decisions | `NOT_SATISFIED` | `CONFIRMED` | Threat model, privacy/retention, availability/performance, RTO/RPO, recovery, cost guardrails and several ADRs remain unresolved. |
| First-slice technical contracts | `NOT_SATISFIED` | `CONFIRMED` | The Solution Architecture audit still requires completion of the first-slice API, error, audit, persistence and integration contracts before Foundation implementation. |
| Azure Foundation evidence | `NOT_STARTED` | `CONFIRMED` | `WP-AZ-001` through `WP-AZ-008` still have 0 of 8 objective evidence gates satisfied. |
| Business/legal readiness for first slice | `NOT_SATISFIED` | `CONFIRMED` | EOI meaning, eligibility/jurisdiction, NDA policy, operator authority and data ownership remain open. |
| Readiness-decision authority | `NOT_SATISFIED` | `CONFIRMED` | The repository does not yet define which approved role/person may issue an execution-authorising `GO` or `CONDITIONAL_GO`, so no such decision can currently open the gate. |

## 4. Current Foundation decision

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
8. reconcile the required traceability chain for the applicable Foundation/first-slice scope as **source -> use case -> backlog -> architecture/design (where applicable) -> implementation -> test -> durable evidence -> validation/status**, with stable IDs and repository-accessible evidence. No `Pending` required hop may be treated as a complete chain;
9. demonstrate that structured data/schema validation, links, IDs, counts, open-question/risk references and status values reconcile;
10. define, in the controlling governance, the approving authority and decision-control contract for any execution-authorising readiness decision;
11. record a formal Architecture / Pre-Implementation Readiness Review outcome of `GO`, `CONDITIONAL_GO`, or `NO_GO` only after the decision-control contract below is satisfied.

A readiness review **must not issue `GO` or `CONDITIONAL_GO` for a scope whose required traceability chain is still partial**. A general reference to `backlog.json`, a local test path without durable run/revision evidence, or an E2E tracker row without the underlying evidence does not satisfy this closure condition.

### 4.1 Readiness decision authority and `CONDITIONAL_GO` controls

**Current authority status: `UNKNOWN`.** No current repository artifact identifies an approved role or person with authority to issue an execution-authorising `GO` or `CONDITIONAL_GO`. Therefore, until that authority is explicitly recorded in controlling governance, `GO` and `CONDITIONAL_GO` are reporting labels only and **must not open the Foundation execution gate**. `NO_GO` remains the effective current decision.

Before a future `CONDITIONAL_GO` can authorise any Foundation work, the controlling governance must identify the approving authority and the decision record must include all of the following:

- decision ID, date, approver identity/role and evidence of that authority;
- exact authorised work-package scope (`WP-AZ-*` IDs) and environment;
- every open condition, residual risk and dependency relevant to that scope;
- named owner and due date for each condition;
- explicit evidence required to close each condition;
- expiry/review date or trigger that automatically returns the scope to `BLOCKED_BY_CONTEXT` if conditions are not closed;
- explicit statement that no unlisted work package is authorised;
- links to the evidence/register entries supporting the decision.

A `CONDITIONAL_GO` **cannot waive or override** any `AGENT.md` repository-integrity stop condition. In particular, it cannot authorise progression while there are broken/missing controlling links, unreconciled required outputs, schema-validation failures, duplicate/conflicting canonical IDs or directories, broken required traceability, unsupported `CONFIRMED` claims, or unresolved contradictions material to the authorised scope. It also cannot waive unresolved legal/regulatory/business semantics that determine whether the proposed implementation behaviour is valid. Any such condition keeps the affected scope `BLOCKED_BY_CONTEXT` and requires `NO_GO` for that scope until repaired.

## 5. What is no longer a blocker

The following statements are obsolete and must not be used as current blockers:

- that `docs/02-actors-and-permissions/` is missing;
- that actors and permissions have not been produced at all;
- that journeys and state models have not been created at all;
- that integration, validation, backlog, tracker, traceability or structured-data artifacts are entirely absent;
- that the immediate queue should recreate those artifacts from scratch.

Those artifacts may still require completion, approval, correction or validation. The work is now **reconciliation and closure**, not initial creation.

The `docs/02-architecture/` issue is different: the directory exists and is actively used, but its relationship to the canonical tree remains an explicit structural exception requiring disposition before the integrity gate can be closed.

## 6. Current execution sequence

1. Validate the existing Phase 0–4 artifacts against their `plan.md` exit criteria and `AGENT.md` integrity rules.
2. Produce an explicit residual-gaps register from that validation; do not reopen work that is already present and internally consistent.
3. Disposition the `docs/02-architecture/` canonical-structure exception.
4. Close the P0 business/legal/security/NFR, first-slice technical-contract and ADR gaps identified by the current Solution Architecture audit.
5. Reconcile **source -> use case -> backlog -> architecture/design (where applicable) -> implementation -> test -> durable evidence -> validation/status** for Foundation-relevant and first-slice-relevant scope, and update `docs/10-traceability/traceability-matrix.md` plus `docs/09-delivery/e2e-delivery-tracker.md` so both point to the same stable IDs and evidence.
6. Define and record the readiness-decision approving authority and decision-control contract.
7. Record the formal pre-implementation gate decision only after the required traceability and other closure conditions are satisfied.
8. Only after an effective `GO`, or a `CONDITIONAL_GO` that satisfies Section 4.1 without waiving any integrity stop condition, begin only the authorised Foundation work packages and capture objective evidence in `docs/09-delivery/foundation-slice-a-evidence-register.md`.
9. Keep `WP-AZ-009` through `WP-AZ-012` blocked until Foundation evidence and the separate Phase 5 / first-business-slice gate are satisfied.

## 7. Status boundary

This reassessment does not:

- claim Azure resources are provisioned;
- promote any `WP-AZ-*` work package;
- mark any use case `COMPLETE`;
- convert inferred permissions or regulated behaviour into confirmed facts;
- silently treat the architecture-tree exception as resolved;
- define an approving authority where the repository currently has none;
- allow a conditional decision to waive `AGENT.md` integrity failures;
- override `AGENT.md` or `plan.md`.

It corrects the repository's current-state reporting so that the remaining block is based on **substantive readiness evidence, explicit structural disposition, controlled decision authority and non-waivable integrity requirements**, not stale file-presence assumptions.
