# Evidence-Grounded Use-Case Impact Analysis

## Problem addressed

The original repository monitor treated any changed textual occurrence of a `UC-*` identifier as evidence that the corresponding use case was materially affected. This created false positives when broad architecture, catalogue, traceability, or mapping documents enumerated many or all use cases. A single cross-reference document could therefore make the report claim that all 41 use cases were affected and then emit the same generic impact text for each one.

That behaviour is useful for identifier discovery, but it is not a real change-impact assessment.

## New impact rule

A use case is counted as **materially impacted** only when the monitoring window contains direct evidence such as:

- the use-case ID in a commit message or pull-request title/body;
- the use-case ID in a dedicated changed file path;
- the use-case ID in a bounded changed diff where the change is specific enough to attribute to the use case;
- a bounded default-branch state difference during a history-integrity event.

When a changed diff contains more than eight distinct use-case IDs, the monitor treats that as **broad cross-reference coverage** rather than automatically claiming that every referenced use case changed in delivery. Those references remain visible in the report, but are separated from material impact.

## Per-use-case analysis

For every materially impacted use case, Section 3 now reports:

1. **Actual change** — whether the evidence is implementation, test/E2E, delivery evidence, architecture, requirement, governance/traceability, structured evidence, or documentation.
2. **Why the use case is included** — the direct signal that linked the change to the use case.
3. **Change source** — the exact commit or pull request responsible.
4. **Changed evidence** — the affected repository paths.
5. **Business consequence** — the domain-level business outcome plus the consequence of the specific change type.
6. **Current delivery position** — read from `docs/09-delivery/implementation-coverage-gap-matrix.md` where available.
7. **Delivery impact** — what the observed change can and cannot justify about delivery progression.
8. **Known gap** — the current implementation gap from the coverage matrix.
9. **Next evidence gate** — the next verification step already defined for that use case.

## Interpretation rules

- Architecture or documentation changes do **not** imply implementation completion.
- Delivery-evidence changes do **not** automatically promote delivery status.
- Requirement changes trigger implementation/test reconciliation, not automatic progress.
- Implementation or test changes may represent delivery progression, but status still requires objective evidence gates.
- Broad documents that enumerate many use cases are reported as cross-reference changes instead of inflating the material-impact count.

## Why this improves Ubuntu Capital OS

This keeps the monitoring report aligned with the repository's evidence-first governance model. The report now distinguishes between:

- a use case being **mentioned**;
- a use case having **changed evidence**;
- a use case having **changed implementation**; and
- a use case being ready for a **delivery-status decision**.

The result is a more decision-useful report for project governance, contractor oversight, readiness assessment, and prioritisation.
