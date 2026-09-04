# System Reconstruction Summary

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

Settlement mechanics, custody/ownership structure, vendors, cancellation rules, detailed permissions, tax-document production, data correction authority, readiness-decision authority (`OQ-016`), and several failure/recovery behaviours are unknown.

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
- Readiness-decision authority and controlled GO/CONDITIONAL_GO governance (`OQ-016`).

## 10. Critical Open Questions

Critical business, legal, regulatory, permissions, provider, operational and readiness-authority questions remain open. The canonical source is `docs/11-open-questions/open-questions.md`; this summary must not be used to infer that an unresolved question has been closed.

`OQ-016` is the canonical readiness-authority question: it asks who may issue an execution-authorising `GO` or `CONDITIONAL_GO` and what decision-control contract governs that authority. It remains `OPEN` and `CRITICAL`. A non-authorising `NO_GO` may still be recorded while `OQ-016` is open; resolving `OQ-016` is required before `GO` or `CONDITIONAL_GO` can carry execution authority.

## 11. Readiness Assessment

**Overall regulated-platform readiness: `PARTIALLY_READY`.**

The supplied context supports an investor-facing marketplace and portfolio model, but does not yet support faithful implementation of regulated onboarding, binding investment, settlement, custody, financial calculations, tax reporting, or operational authority.

**Architecture direction:** materially improved and usable with assumptions, but several architecture/security/NFR and ADR closures remain outstanding.

**Foundation Slice A execution:** `BLOCKED_BY_CONTEXT`.

The current pre-implementation decision is **`NO-GO FOR UNRESTRICTED IMPLEMENTATION`**. Canonical Phase 0–4 artifacts materially exist, but presence is not approval or completion. The current gate is defined by `AGENT.md`, controlling `plan.md`, `docs/09-delivery/foundation-slice-a-governance-reconciliation.md`, and `docs/09-delivery/pre-implementation-gate-reassessment-2026-09-03.md`. No execution-authorising `GO` or `CONDITIONAL_GO` can open the gate until readiness-decision authority under `OQ-016` is formally defined and the non-waivable integrity and substantive closure conditions are satisfied. A `NO_GO` finding may be recorded or refreshed immediately while blockers remain because it does not authorise execution.

**First business slice execution:** `BLOCKED_BY_CONTEXT`.

The discovery/non-binding-EOI concept remains the preferred first vertical slice, but it must not start merely because the concept is bounded or because reconstruction artifacts exist.

## 12. Recommended Next Action

Do **not** restart Phase 0 or recreate canonical artifacts that already exist. Execute the current residual-closure queue in `plan.md`:

1. validate existing Phase 0–4 outputs against phase exit criteria and `AGENT.md` integrity rules;
2. reconcile the **pre-start planned traceability** required for the proposed scope as `source -> use case -> backlog -> architecture/design (where applicable) -> planned implementation target -> planned test/validation target -> planned durable-evidence target -> planned tracker/status`, using stable repository-accessible IDs or targets and aligning `docs/10-traceability/traceability-matrix.md` with `docs/09-delivery/e2e-delivery-tracker.md`;
3. close or formally bound the business/legal, permissions, data-ownership/state, first-slice technical-contract, architecture/security/NFR and ADR gaps;
4. disposition the `docs/02-architecture/` canonical-structure exception;
5. resolve `OQ-016` by defining readiness-decision authority and the controlled decision contract in controlling governance;
6. while blockers remain, record or refresh a durable `NO_GO` outcome for the evaluated scope. Only after `OQ-016`, applicable planned pre-start traceability and other non-waivable closure conditions are satisfied may an execution-authorising `GO` or `CONDITIONAL_GO` be issued;
7. only after an effective authorised decision, begin the exact permitted Foundation work packages and capture objective implementation evidence in `docs/09-delivery/foundation-slice-a-evidence-register.md`;
8. during authorised delivery, progressively reconcile the **realised** chain as `source -> use case -> backlog -> architecture/design (where applicable) -> implementation evidence -> test/run evidence -> durable evidence -> validation/status`; missing required realised hops block status promotion, E2E readiness and acceptance rather than the earlier start decision.

No use case or `WP-AZ-*` package is promoted by this summary.