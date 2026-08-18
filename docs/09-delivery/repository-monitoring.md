# Ubuntu Capital OS — Scheduled Repository Monitoring

## Purpose

This capability monitors `IsaacMcGrind/ubuntu-capital-os` twice daily and produces an evidence-first repository change report without modifying product or reconstruction content.

## Schedule

The workflow runs at:

- `00:00` Africa/Johannesburg
- `12:00` Africa/Johannesburg

It also supports manual execution through `workflow_dispatch`.

Workflow: `.github/workflows/ubuntu-capital-repository-monitor.yml`

## Monitoring Window

The monitor determines the previous successful run of the same workflow through the GitHub Actions API.

- Normal run: previous successful run → current run.
- First run: preceding 12 hours.

No repository checkpoint file is required, so the monitoring mechanism does not create self-generated checkpoint commits.

## Sources Inspected

The monitor uses the GitHub repository and API to inspect:

- commits on `master`;
- files added, modified, removed or renamed in those commits;
- pull requests updated during the monitoring window;
- recent PR reviews and review comments;
- changed file paths and available patches;
- the current use-case catalogue;
- controlling documents and repository-integrity conditions;
- contractor records under `contractors/80kDevelopers/`.

## Report Outputs

Every run creates `monitoring-output/report.md` inside the runner.

The report is:

1. appended to the GitHub Actions job summary;
2. uploaded as a workflow artifact with 90-day retention;
3. published as a GitHub Issue when new commit or pull-request activity is detected.

No issue is created merely because a pre-existing integrity finding still exists. Such findings remain visible in the job summary and artifact until resolved.

## Report Structure

The report contains:

1. Executive Summary
2. Changes Detected
3. Use-Case Impact
4. Implementation and Contractor Progress
5. Governance and Evidence Changes
6. Risks, Problems and Regressions
7. Positive Progress
8. Recommended Next Actions
9. Change Ledger
10. Overall Assessment

## Evidence Policy

The monitor follows Ubuntu Capital OS evidence discipline:

- `CONFIRMED`
- `INFERRED`
- `UNKNOWN`
- `CONTRADICTED`

It does not automatically promote a use case or delivery status. A code, documentation, UI or contractor change is treated as evidence requiring reconciliation rather than proof of end-to-end completion.

## Integrity Checks

The initial automated checks include:

- presence of `AGENT.md`, `plan.md`, `README.md`, and the master use-case catalogue;
- reconciliation between the declared use-case count and parsed use-case rows;
- stale `N-use-case` references in `plan.md` that conflict with the current catalogue;
- case-conflicting contractor directory names.

These checks are intentionally conservative. They do not replace human review or the broader traceability/validation requirements in `AGENT.md` and `plan.md`.

## Permissions

The scheduled workflow is read-only with respect to repository content.

Granted workflow permissions:

- `contents: read`
- `actions: read`
- `pull-requests: read`
- `issues: write`

`issues: write` is used only to publish material-change reports.

The workflow does not:

- modify product or OS files;
- merge or close pull requests;
- change branches;
- resolve reviews;
- update evidence classifications;
- update use-case delivery status.

## Operational Notes

Scheduled workflows execute from the latest commit on the default branch. Therefore this monitoring workflow becomes active on its schedule only after the workflow file is merged into `master`.

The workflow can be manually run from the GitHub Actions UI after it exists on the default branch.
