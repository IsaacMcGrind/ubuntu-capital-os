# Ubuntu Capital OS — Foundation Slice A Readiness Decision

Decision ID: GO-2026-09-05-FSA-001  
Decision date: 2026-09-05  
Decision outcome: GO  
Decision status: REVALIDATED_EFFECTIVE  
Authorised scope: WP-AZ-001 through WP-AZ-008 (Foundation Slice A only)  
Authorised environment: AZURE DEV/MVP  
Effective scope gate: OPEN_FOR_AUTHORISED_EXECUTION  
Revalidation date: 2026-09-07  
Revalidation evidence: SRC-020  
Management-authority and evidence-workflow amendment: SRC-021 (effective 2026-09-11)  
Supersession scope: replaces the interim `CLOSED_PENDING_REVALIDATION` state while retaining every non-waivable condition and scope boundary below

## 1. Authority model

The Ubuntu Capital project owner is the final execution-authorising authority. Under `SRC-021`, 80K Developers (Pty) Ltd is the appointed Project Manager contractor and accountable project-management workstream, with Thembinkosi Mtsweni as the responsible human Project Manager and final project-owner decision authority.

HerLogic Solutions and Corefinity may self-select work and contribute technical delivery or analysis evidence within the approved scope. They do not independently approve a gate, promote canonical status, accept their own evidence, change priorities or authorise subsequent work.

The Ubuntu Capital project owner approved this bounded GO on 2026-09-05. On 2026-09-07, Thembinkosi Mtsweni completed the formal post-prerequisite readiness review, validated the prerequisite reconciliation, and explicitly confirmed that the Foundation work is ready to begin. This decision remains revalidated and effective. The `SRC-021` authority amendment governs future evidence acceptance and further-work decisions without retroactively invalidating this GO.

## 1.1 Formal post-prerequisite revalidation

Decision: `GO` revalidated and effective.  
Scope position: `WP-AZ-001` through `WP-AZ-008` are approved for governed execution within Azure DEV/MVP. Contractors may self-select work within the approved scope and must declare the executor, exact package subset, authorised paths or bounded contractor subdirectory, evidence purpose, and applicable external implementation/resource scope in the PR. This decision does not allocate work.  
Evidence boundary: the decision authorises execution but does not claim that execution has started, that Azure resources exist, or that any implementation evidence gate is satisfied. Package status remains `READY_FOR_DEVELOPMENT` until objective start evidence is accepted and canonically reconciled through a separate `PROJECT_MANAGER_GOVERNANCE` change.

## 2. Conditions and boundaries

The following conditions are non-waivable:

1. Scope remains strictly WP-AZ-001 through WP-AZ-008.
2. Before contractor execution begins, the Project Manager must record the executor, exact package subset, authorised paths or bounded contractor subdirectory, evidence purpose, and applicable external implementation/resource scope.
3. Status promotion still requires objective evidence gates per work package.
4. No business use case may be marked COMPLETE from Foundation work alone.
5. Secrets, credentials, and tokens must not be committed to repository artifacts.
6. Required traceability links must be maintained from source/use case/backlog/design to implementation, tests, and durable evidence as execution progresses.
7. Any critical contradiction discovered during execution triggers immediate pause and governance review.

## 3. Required execution recording

Execution recording uses two governed stages:

1. The technical contractor records factual, sanitised, revision-pinned work evidence in its existing `contractors/<contractor>/` directory.
2. After review and merge as provenance, the 80K Developers Project Manager workstream separately assesses that evidence and, only when accepted, updates or links it through a distinct `PROJECT_MANAGER_GOVERNANCE` change in:
   - `docs/09-delivery/foundation-slice-a-evidence-register.md`;
   - `docs/10-traceability/traceability-matrix.md`;
   - `docs/09-delivery/e2e-delivery-tracker.md` where use-case progression is affected.

A contractor evidence merge does not itself accept evidence, promote status or authorise further work. Canonical records should reference the contractor evidence rather than duplicate sensitive or bulky raw material.

## 4. Residual risk statement

This revalidated GO authorises the bounded Foundation scope but does not allocate work. Execution may begin in governed dependency order only after a durable contractor self-selection declaration is recorded, with objective evidence submitted as it is produced and accepted separately before canonical reconciliation. It does not remove existing business/legal unknowns outside Foundation scope, prove implementation completion, authorise production, or authorise `WP-AZ-009` through `WP-AZ-012`.
