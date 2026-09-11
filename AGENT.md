# Ubuntu Capital OS — System Reconstruction Agent

## Mission

Reconstruct the supplied reference investment platform into an evidence-first, traceable functional model for Ubuntu Capital. Execute the stages in `plan.md` in order and save every durable output in this repository.

## Governing principle

The agent's objective is not to speculate about an ideal platform. Its objective is to reconstruct the supplied reference system faithfully from evidence, make uncertainty explicit, and produce an implementation-ready specification without silently converting assumptions into facts.

## Mandatory operating rules

1. Read `AGENT.md` first, then read and execute `plan.md` sequentially.
2. Treat supplied screenshots, documents, observations, and repository evidence as authoritative.
3. Classify every material finding as `CONFIRMED`, `INFERRED`, `UNKNOWN`, or `CONTRADICTED`.
4. Do not present inferred behaviour as confirmed.
5. For every non-confirmed finding, record uncertainty, impact, evidence needed, and validation method.
6. Keep faithful reconstruction requirements separate from future Ubuntu Capital improvements.
7. Model business outcomes as use cases, not individual screens, buttons, endpoints, tables, or components.
8. Deliver complete vertical slices covering UI, API/service, domain rules, persistence, access control, integrations, validation, audit, monitoring, automated tests, E2E tests, failure handling, deployment evidence, and documentation where applicable.
9. Do not mark a use case `COMPLETE` unless its E2E completion evidence is present.
10. Preserve stable IDs for sources, actors, domains, requirements, business rules, use cases, journeys, entities, integrations, backlog items, questions, risks, tests, and evidence.
11. Do not overwrite unrelated files.
12. Validate JSON against the schemas in `/schemas` before treating an output as complete.
13. Use the canonical repository structure defined in `plan.md`; do not create parallel or renamed directory trees.
14. If counts, links, IDs, evidence status, or required outputs do not reconcile, stop progression and repair the inconsistency before continuing.
15. Repository change policy: after required canonical outputs are present, all further updates must modify existing files only. Do not create new files unless explicitly approved by the project owner for a specific purpose. `SRC-021` explicitly approves the creation and continuing use of `.github/pull_request_template.md` as the mandatory PR-governance control. It also permits a new evidence file inside an existing contractor folder only when the Project Manager assignment identifies its exact path or bounded contractor subdirectory and evidence purpose; neither approval creates a general new-file or canonical-artifact exception.

## Delivery authority and contractor evidence boundary

Under `SRC-021`, 80K Developers (Pty) Ltd is the appointed Project Manager contractor and accountable project-management workstream. Thembinkosi Mtsweni is the responsible human Project Manager and final project-owner decision authority working through that management arrangement. In that capacity, Thembinkosi Mtsweni holds the sole repository authority for interpreting or accepting contractor evidence, changing canonical Ubuntu Capital OS delivery status, changing priorities, approving gates, and authorising subsequent work.

Within this Ubuntu Capital OS repository:

1. Contractors and coders execute only the work package and path scope assigned by the Project Manager.
2. A `CONTRACTOR_TECHNICAL_EVIDENCE` submission must keep every repository-hosted first-pass evidence file under the submitting contractor's existing `contractors/<contractor>/` directory. It must not create or modify canonical governance, status, decision, register, tracker, traceability, roadmap, plan, or summary artifacts. Sensitive or bulky raw evidence may remain in an approved external store, but the contractor folder must contain the sanitised, stable reference and evidence description.
3. A contractor evidence submission may state work performed, dates, responsible contributor, commands or procedures used, revision-pinned references, validation executed and results, limitations, unfinished work, dependencies, blockers, and decisions required.
4. A contractor evidence submission must not approve or authorise work, create or reinterpret a project gate, change canonical project or work-package status, declare a use case or work package complete, make an architecture/business/legal decision for Ubuntu Capital, broaden assigned scope, or present unsupported implementation claims as current fact.
5. Contractor evidence is an input to governance, not a governance decision. Merging contractor evidence does not promote status or approve further work.
6. Automated reviewers and agents may assess evidence quality, completeness, traceability, security, contradictions, and alignment. Their labels and recommendations are analytical only; they do not approve, accept, reject, merge, or change project status.
7. After a contractor evidence PR is reviewed and merged as provenance, the Project Manager separately assesses the merged evidence. Only evidence accepted through an explicitly identified `PROJECT_MANAGER_GOVERNANCE` change may be linked into canonical OS artifacts or support a status, priority, gate, or subsequent-work decision.
8. 80K Developers may operate in two explicitly separated capacities: Project Manager contractor and implementation/coding contractor. When submitting implementation or technical delivery evidence, 80K Developers is subject to the same evidence-only rules and review as every other contractor. A canonical governance change is Project-Manager-owned only when its purpose and authority are explicitly identified; organizational identity alone does not convert a technical evidence submission into a governance decision.
9. Every PR must complete the project-owner-approved `.github/pull_request_template.md` (`SRC-021`) with submitting organization, declared capacity, responsible human, work-package IDs, assignment/decision reference, authorised paths, evidence references, validation, what the evidence proves/does not prove, and a sensitive-information check. Missing or unverifiable authority metadata makes the PR `Unverified` or `Changes required`.
10. If a contractor PR crosses this boundary, classify it as `Changes required` until project-level decisions and status changes are removed or explicitly moved into an 80K-Developers-Project-Manager-owned governance change.

The governed workflow is:

`Project Manager assigns work -> contractor implements -> contractor records sanitised evidence in its contractor folder -> evidence PR is reviewed -> evidence PR is merged as provenance only -> Project Manager separately assesses the merged evidence -> accepted evidence is reconciled through a PROJECT_MANAGER_GOVERNANCE change -> Thembinkosi Mtsweni decides status, priority, gates, and next work`.

## Evidence classifications

- `CONFIRMED`: directly supported by supplied evidence.
- `INFERRED`: reasonably implied but not verified.
- `UNKNOWN`: evidence is insufficient.
- `CONTRADICTED`: available sources are incompatible.

## Execution order

1. Context inventory
2. System understanding
3. Actors and permissions
4. Functional domains
5. Master use-case catalogue
6. Detailed use-case specifications
7. User journeys
8. Entity state models
9. Integrations and dependencies
10. Delivery roadmap and backlog
11. Quality, traceability, gaps, risks, and validation
12. Final summary and self-review

## Status values

`NOT_ANALYSED`, `ANALYSIS_IN_PROGRESS`, `BLOCKED_BY_CONTEXT`, `READY_FOR_DEVELOPMENT`, `IN_DEVELOPMENT`, `COMPONENT_COMPLETE`, `READY_FOR_E2E_TEST`, `E2E_TESTING`, `FAILED_E2E_TEST`, `READY_FOR_ACCEPTANCE`, `COMPLETE`, `DEFERRED`.

## Repository validation rules

The agent must not treat a phase as complete while any of the following is true:

- a Markdown link points to a missing file;
- a referenced controlling document does not exist;
- use-case, actor, workflow, phase, question, risk, test, or evidence counts differ across outputs;
- duplicate or conflicting canonical directories exist;
- a `CONFIRMED` statement lacks direct evidence;
- a non-confirmed finding lacks uncertainty details;
- required JSON fields are missing or schema validation fails;
- stable IDs are duplicated, skipped without explanation, or silently changed;
- traceability from source to use case, backlog, test, and evidence is broken;
- required output files from `plan.md` are missing.

## Required repository outputs

Follow the canonical repository structure documented in `plan.md`. When new evidence arrives, update the source inventory first, then propagate traceable changes through requirements, rules, use cases, journeys, backlog, tests, open questions, and summaries.