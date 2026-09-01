# Evidence-Grounded Use-Case Impact Analysis

## Problem addressed

The original repository monitor treated any changed textual occurrence of a `UC-*` identifier as evidence that the corresponding use case was materially affected. This created false positives when broad architecture, catalogue, traceability, mapping documents, or PR descriptions enumerated many or all use cases. A single cross-reference source could therefore make the report claim that all 41 use cases were affected and then emit the same generic impact text for each one.

That behaviour is useful for identifier discovery, but it is not a real change-impact assessment.

## New impact rule

A use case is counted as **materially impacted** only when the monitoring window contains direct, attributable evidence such as:

- the use-case ID in focused commit metadata or pull-request metadata that actually changed in the window;
- the use-case ID in a dedicated changed file path;
- the use-case ID in a bounded changed diff where the change is specific enough to attribute to the use case;
- a bounded default-branch or pull-request head state difference during a history-integrity event.

Broad-reference suppression is applied **per attributed source**. If one changed file, PR body, or commit message enumerates more than eight distinct use-case IDs, that source is treated as **broad cross-reference coverage** rather than automatically claiming that every referenced use case changed in delivery. A batch change that touches many independent use-case-specific files still records each directly affected use case because each file is evaluated independently.

PR titles remain direct metadata because they are short, explicit change labels. PR bodies are thresholded independently so templates, checklists, architecture summaries, or mapping descriptions cannot recreate an "all 41 impacted" result simply by listing the catalogue.

Review/conversation-comment-only IDs and unchanged-context IDs are not promoted to material impact when their provenance cannot be established.

## Pull-request checkpoint provenance

The monitor persists a small machine-readable `monitoring-output/state.json` snapshot inside the existing 7-day workflow artifact. The snapshot records the current head SHA, title, and body for every open pull request.

On the next successful run, that checkpoint allows the monitor to distinguish:

- a newly created PR;
- a PR merged during the monitoring window;
- commits that entered an existing PR since the previous successful monitor run, regardless of the commits' author/committer dates;
- a force-pushed or rewritten PR head;
- an in-window edit to an existing PR title or body; and
- review/comment-only activity that did not change structural PR evidence.

This avoids using commit timestamps as a proxy for when a commit entered a PR. It also avoids GitHub's list-PR-commits 250-commit cap: when an existing PR head changes, the monitor compares the prior checkpoint head SHA with the current head through local git ancestry and inspects exactly the new commit range.

If the previous state artifact is unavailable or expired, the monitor degrades conservatively: it does not replay an existing PR's historical title/body/diff as fresh material impact merely because the PR `updated_at` changed.

## Oversized-diff handling

For PR-head deltas and created/merged PR comparisons, use-case evidence is derived from locally fetched git objects and per-file diffs. The monitor therefore does not rely on GitHub's optional REST `patch` field, which can be omitted for oversized textual diffs. Missing REST patch text does not silently become "no use-case impact".

## Per-use-case analysis

For every materially impacted use case, Section 3 reports:

1. **Actual change** — whether the evidence is implementation, test/E2E, delivery evidence, architecture, requirement, governance/traceability, structured evidence, or documentation.
2. **Why the use case is included** — the direct signal that linked the change to the use case.
3. **Change source** — the exact commit or pull request responsible.
4. **Changed evidence** — only the repository paths attributed to that use-case signal.
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
- Broad files or metadata sources that enumerate many use cases are reported as cross-reference changes instead of inflating the material-impact count.
- Reviewer comments alone cannot manufacture a material use-case impact claim.
- History-rewrite evidence is attributed per changed file before change type is inferred.
- Existing PR metadata is material only when the checkpoint proves that title/body changed in the monitoring window.
- A commit is considered newly added to an existing PR by head ancestry against the previous monitor checkpoint, not by the commit's authored/committed timestamp.

## Why this improves Ubuntu Capital OS

This keeps the monitoring report aligned with the repository's evidence-first governance model. The report now distinguishes between:

- a use case being **mentioned**;
- a use case having **changed evidence**;
- a use case having **changed implementation**; and
- a use case being ready for a **delivery-status decision**.

The result is a more decision-useful report for project governance, contractor oversight, readiness assessment, and prioritisation.
