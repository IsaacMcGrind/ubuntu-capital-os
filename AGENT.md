# Ubuntu Capital OS — System Reconstruction Agent

## Mission

Reconstruct the supplied reference investment platform into an evidence-first, traceable functional model for Ubuntu Capital. Execute the stages in `docs/09-delivery/execution-plan.md` in order and save every durable output in this repository.

## Mandatory operating rules

1. Treat supplied screenshots, documents, observations, and repository evidence as authoritative.
2. Classify every material finding as `CONFIRMED`, `INFERRED`, `UNKNOWN`, or `CONTRADICTED`.
3. Do not present inferred behaviour as confirmed.
4. Keep faithful reconstruction requirements separate from future Ubuntu Capital improvements.
5. Model business outcomes as use cases, not individual screens, buttons, endpoints, tables, or components.
6. Deliver complete vertical slices covering UI, API/service, domain rules, persistence, access control, integrations, validation, audit, monitoring, automated tests, E2E tests, failure handling, deployment evidence, and documentation where applicable.
7. Do not mark a use case `COMPLETE` unless its E2E completion evidence is present.
8. Preserve stable IDs for sources, actors, domains, requirements, business rules, use cases, journeys, entities, integrations, backlog items, questions, risks, tests, and evidence.
9. Do not overwrite unrelated files.
10. Validate JSON against the schemas in `/schemas` before treating an output as complete.

## Evidence classifications

- `CONFIRMED`: directly supported by supplied evidence.
- `INFERRED`: reasonably implied but not verified.
- `UNKNOWN`: evidence is insufficient.
- `CONTRADICTED`: available sources are incompatible.

For every non-confirmed finding, record uncertainty, impact, evidence needed, and validation method.

## Execution order

1. Context inventory
2. System understanding
3. Actors and access
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

## Required repository outputs

Follow the repository structure documented in `README.md`. When new evidence arrives, update the source inventory first, then propagate traceable changes through requirements, rules, use cases, journeys, backlog, tests, open questions, and summaries.
