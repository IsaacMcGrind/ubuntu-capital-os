# System Reconstruction Summary

> **Current Foundation decision — 2026-09-07:** Thembinkosi Mtsweni completed the formal post-prerequisite readiness review and revalidated `GO-2026-09-05-FSA-001`. The scope gate for `WP-AZ-001` through `WP-AZ-008` is `OPEN_FOR_AUTHORISED_EXECUTION` in Azure DEV/MVP. This approves the bounded scope for assignment; technical start also requires a durable Project Manager contractor/package/path assignment. Implementation, completion, business-use-case and production claims remain evidence-gated. Source: `SRC-020`.

## 1. System Purpose

Ubuntu Capital OS is being modelled as a private-market investment platform inspired by the supplied reference system. The visible product enables investors to discover investment opportunities and navigate portfolio areas including pending investments, holdings, performance, activity, reports, and tax documents. A complete production reconstruction would also require regulated onboarding, controlled due diligence, commitment, settlement, administration, compliance, support, and recovery capabilities that are not yet fully evidenced.

## 2. Context Reviewed

- Public and authenticated reference-platform screenshots.
- Public and portfolio URLs supplied by the user.
- User-supplied app/website reverse-engineering report.
- Enterprise System Reconstruction and Use-Case Discovery Agent prompt.
- Existing evidence-first files already committed to this repository.
- Current canonical Phase 0–4 reconstruction outputs, delivery controls, and Solution Architecture readiness material.

The strongest evidence concerns visible investor-facing navigation and discovery. Backend rules, financial calculations, internal operations, vendors, and regulatory workflows remain incomplete.

## 3. Identified Actors

Current actor candidates include prospective investor, registered investor, eligible investor, NDA-authorised investor, support operator, opportunity administrator, access administrator, compliance actor, finance/settlement operator, management reporter, scheduled process, and external identity, agreement, messaging, and financial-service providers.

Canonical actor and permission artifacts now exist, but several internal actor boundaries and permissions remain `INFERRED` or `UNKNOWN` pending approved authority and access rules.

## 4. Functional Domains

PUB, IAM, ONB, OPP, DD, INV, SET, PORT, DOC, NEWS, EVENT, NOTIFY, REF, PROFILE, OPS, ADMIN, AUD, REPORT, and INT.

## 5. Use-Case Count

The master catalogue contains **41 use cases**.

### Confirmed

Direct evidence supports the public platform proposition, visible opportunity cards and categories, the presence of an NDA action, portfolio-area navigation, news content, events navigation, profile navigation, referral navigation, and a contact/support entry point.

### Inferred

Authentication, registration, filtering and sorting behaviour, opportunity-detail behaviour, KYC/AML, accreditation, commitment processing, notifications, administration, audit, management reporting, and several external integration categories are inferred from the platform model, visible affordances, or supplied analytical report.

### Unknown

Settlement mechanics, custody/ownership structure, vendors, cancellation rules, detailed permissions, tax-document production, data correction authority, and several failure/recovery behaviours are unknown. Readiness-decision authority is now defined and `OQ-016` is closed.

### Contradicted

No direct contradiction is currently supported. Architectural guesses in the earlier report are treated as inferences rather than facts.

## 6. Critical End-to-End Journeys

1. Visitor learns about the platform and becomes a prospective investor.
2. Prospective investor registers, completes eligibility onboarding, and receives an approved or remediated status.
3. Eligible investor discovers and evaluates an opportunity.
4. Investor signs an NDA and accesses controlled due-diligence content.
5. Investor submits and resolves an investment commitment or non-binding expression of interest according to the approved product/legal model.
6. Accepted investor receives instructions, funds the transaction, and the platform reconciles settlement only after the regulated operating model is confirmed.
7. Investor views holdings, performance, activity, reports, and tax documents.
8. Operators publish opportunities, support investors, correct exceptions under control, and produce audit/compliance evidence.

## 7. Recommended First Vertical Slice

The selected first business slice remains **Discover an Opportunity and Submit a Non-Binding Expression of Interest**.

This slice should include protected access, catalogue UI and API, an explicitly assumed filtering/detail experience pending evidence, interest submission, persistence, duplicate handling, validation, role enforcement, business audit events, operational visibility, automated tests, E2E acceptance tests, and deployment evidence.

It deliberately avoids presenting an expression of interest as a binding investment before legal, compliance, settlement, and ownership rules are confirmed.

**Selection of this slice is not authorization to execute it.** `WP-AZ-009` through `WP-AZ-012` remain `BLOCKED_BY_CONTEXT` until Foundation evidence, the controlling `plan.md` Phase 5 foundational capabilities/exit criteria, and the separate first-slice integrity gate all reconcile.

## 8. Implementation Phases

0. Context and architecture baseline.
1. Actors, permissions, domains, and core models.
2. Complete use-case discovery and specification.
3. Journeys, states, integrations, and validation design.
4. Development backlog and traceability.
5. Foundational product capabilities.
6. First complete non-binding EOI vertical slice.
7. Core business journeys.
8. Production integrations.
9. Administration, operations, reporting, and compliance.
10. Production hardening.

The controlling phase sequence is defined in `plan.md`.

## 9. Highest-Risk Gaps

- Jurisdiction and regulatory scope.
- Investor eligibility and accreditation rules.
- Legal effect of the investment action / EOI.
- Custody, SPV, nominee, fund, or direct-ownership model.
- Funding, safeguarding, reconciliation, and refund mechanics.
- Performance and valuation formulas.
- Internal roles, authority, data scope, overrides, and maker-checker controls.
- Logical data ownership and authoritative first-slice state transitions.
- First-slice API, error, audit, persistence, and integration contracts.
- Threat model, authorization design, privacy/retention, measurable NFRs, recovery and cost guardrails.
- Tax-document generation and approval.
- Continued enforcement of the now-defined readiness-decision authority and controlled GO/CONDITIONAL_GO governance (`OQ-016`, closed).

## 10. Critical Open Questions

Critical business, legal, regulatory, permissions, provider, operational and readiness-authority questions remain open. The canonical source is `docs/11-open-questions/open-questions.md`; this summary must not be used to infer that an unresolved question has been closed.

`OQ-016` is closed. The authority model and decision-control contract are recorded in `docs/09-delivery/foundation-slice-a-go-decision-2026-09-05.md`; its bounded GO was formally revalidated and made effective on 2026-09-07. Future decisions must retain explicit scope, non-waivable conditions, evidence links and residual-risk controls.

## 11. Readiness Assessment

**Overall regulated-platform readiness: `PARTIALLY_READY`.**

The supplied context supports an investor-facing marketplace and portfolio model, but does not yet support faithful implementation of regulated onboarding, binding investment, settlement, custody, financial calculations, tax reporting, or operational authority.

**Architecture direction:** materially improved and usable with assumptions, but several architecture/security/NFR and ADR closures remain outstanding.

**Foundation Slice A:** scope gate `OPEN_FOR_AUTHORISED_EXECUTION` for `WP-AZ-001` through `WP-AZ-008`; contractor start `BLOCKED_PENDING_ASSIGNMENT`; package status `READY_FOR_DEVELOPMENT`; 0 of 8 objective evidence gates satisfied.

The effective decision is `GO-2026-09-05-FSA-001`, limited to Foundation work packages `WP-AZ-001` through `WP-AZ-008` in Azure DEV/MVP. It authorises the bounded scope but does not assign an executor or prove implementation: the Foundation evidence register still records 0 of 8 objective evidence gates satisfied. No business use case is promoted by this decision, and `WP-AZ-009` through `WP-AZ-012` remain blocked by their separate gates.

**First business slice execution:** `BLOCKED_BY_CONTEXT`.

The discovery/non-binding-EOI concept remains the preferred first vertical slice, but it must not start merely because the concept is bounded or because reconstruction artifacts exist.

## 12. Recommended Next Action

Do **not** restart Phase 0 or recreate canonical artifacts that already exist. `SRC-020` records completion of the bounded Foundation prerequisite review and revalidation of `GO-2026-09-05-FSA-001`; reopen it only for a material baseline, scope, risk, or non-waivable evidence change.

Execute the current queue in `plan.md`:

1. require the Project Manager to record the contractor, exact permitted `WP-AZ-001` through `WP-AZ-008` subset, authorised repository paths or bounded contractor subdirectory, evidence purpose, and applicable external implementation/resource scope;
2. allow the assigned contractor to begin only that exact subset in governed dependency order; source-dependent packages still require a pinned application branch and commit;
3. require each technical contractor to capture objective, sanitised, revision-pinned first-pass implementation, test/run, deployment, and operational evidence only under its applicable `contractors/<contractor>/` folder;
4. review and merge contractor evidence as provenance only;
5. require the 80K Developers Project Manager workstream to separately assess merged evidence and, when accepted, link it into `docs/09-delivery/foundation-slice-a-evidence-register.md`, maintain realised traceability, and record any status change through a distinct `PROJECT_MANAGER_GOVERNANCE` PR;
6. repair the repository-monitor path/import regression in a separate focused change and validate the repaired workflow at a pinned commit;
7. keep `WP-AZ-009` through `WP-AZ-012` blocked until Foundation evidence, Phase 5 shared-capability exit criteria, and first-slice integrity requirements reconcile.

No use case or `WP-AZ-*` package is promoted by this summary.

## 13. Current Implementation Assessment

The current revision-pinned implementation assessment is `docs/09-delivery/implementation-analysis-refresh-2026-09-05.md`, based on OS commit `e1bbbe2fa5bcb3570271ac3bdbcba5b3072ad256`.
