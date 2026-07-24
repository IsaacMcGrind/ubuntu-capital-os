# System Reconstruction Summary

## 1. System Purpose

Ubuntu Capital OS is being modelled as a private-market investment platform inspired by the supplied reference system. The visible product enables investors to discover investment opportunities and navigate portfolio areas including pending investments, holdings, performance, activity, reports, and tax documents. A complete production reconstruction would also require regulated onboarding, controlled due diligence, commitment, settlement, administration, compliance, support, and recovery capabilities that are not yet fully evidenced.

## 2. Context Reviewed

- Public and authenticated reference-platform screenshots.
- Public and portfolio URLs supplied by the user.
- User-supplied app/website reverse-engineering report.
- Enterprise System Reconstruction and Use-Case Discovery Agent prompt.
- Existing evidence-first files already committed to this repository.

The strongest evidence concerns visible investor-facing navigation and discovery. Backend rules, financial calculations, internal operations, vendors, and regulatory workflows remain incomplete.

## 3. Identified Actors

Current actor candidates include prospective investor, registered investor, eligible investor, NDA-authorised investor, support operator, opportunity administrator, access administrator, compliance actor, finance/settlement operator, management reporter, scheduled process, and external identity, agreement, messaging, and financial-service providers.

Most internal actor boundaries remain `INFERRED` or `UNKNOWN` pending an approved role and authority matrix.

## 4. Functional Domains

PUB, IAM, ONB, OPP, DD, INV, SET, PORT, DOC, NEWS, EVENT, NOTIFY, REF, PROFILE, OPS, ADMIN, AUD, REPORT, and INT.

## 5. Use-Case Count

The initial master catalogue contains **41 use cases**.

### Confirmed

Direct evidence supports the public platform proposition, visible opportunity cards and categories, the presence of an NDA action, portfolio-area navigation, news content, events navigation, profile navigation, referral navigation, and a contact/support entry point.

### Inferred

Authentication, registration, filtering and sorting behaviour, opportunity-detail behaviour, KYC/AML, accreditation, commitment processing, notifications, administration, audit, management reporting, and several external integration categories are inferred from the platform model, visible affordances, or supplied analytical report.

### Unknown

Settlement mechanics, custody/ownership structure, vendors, cancellation rules, detailed permissions, tax-document production, data correction authority, and several failure/recovery behaviours are unknown.

### Contradicted

No direct contradiction is currently supported. Architectural guesses in the earlier report are treated as inferences rather than facts.

## 6. Critical End-to-End Journeys

1. Visitor learns about the platform and becomes a prospective investor.
2. Prospective investor registers, completes eligibility onboarding, and receives an approved or remediated status.
3. Eligible investor discovers and evaluates an opportunity.
4. Investor signs an NDA and accesses controlled due-diligence content.
5. Investor submits and resolves an investment commitment.
6. Accepted investor receives instructions, funds the transaction, and the platform reconciles settlement.
7. Investor views holdings, performance, activity, reports, and tax documents.
8. Operators publish opportunities, support investors, correct exceptions under control, and produce audit/compliance evidence.

## 7. Recommended First Vertical Slice

Build **Discover an Opportunity and Submit a Non-Binding Expression of Interest**.

This slice should include protected access, catalogue UI and API, an explicitly assumed filtering/detail experience pending evidence, interest submission, persistence, duplicate handling, validation, role enforcement, audit events, operational visibility, automated tests, E2E acceptance tests, and deployment evidence.

It deliberately avoids presenting an expression of interest as a binding investment before legal, compliance, settlement, and ownership rules are confirmed.

## 8. Implementation Phases

0. Context and architecture baseline.
1. Identity, access, audit, and shared foundations.
2. Opportunity discovery plus non-binding interest vertical slice.
3. Investor onboarding and controlled due diligence.
4. Investment commitment and core integrations.
5. Funding, settlement, reconciliation, and exception recovery.
6. Portfolio, documents, administration, content, and support.
7. Reporting, compliance, security, resilience, and production hardening.

## 9. Highest-Risk Gaps

- Jurisdiction and regulatory scope.
- Investor eligibility and accreditation rules.
- Legal effect of the investment action.
- Custody, SPV, nominee, fund, or direct-ownership model.
- Funding, safeguarding, reconciliation, and refund mechanics.
- Performance and valuation formulas.
- Internal roles, authority, data scope, overrides, and maker-checker controls.
- Tax-document generation and approval.
- Privacy, retention, deletion, and evidence obligations.

## 10. Critical Open Questions

The open-question register currently contains 15 questions. OQ-001 through OQ-005, OQ-008, OQ-009, OQ-012, and OQ-015 are critical blockers for a production-regulated platform.

## 11. Readiness Assessment

**Overall regulated-platform readiness: `PARTIALLY_READY`.**

The supplied context supports an investor-facing marketplace and portfolio model, but does not yet support faithful implementation of regulated onboarding, binding investment, settlement, custody, financial calculations, tax reporting, or operational authority.

**Discovery-prototype readiness: `READY_WITH_ASSUMPTIONS`.**

A non-binding opportunity-discovery and expression-of-interest slice can proceed while clearly labelling filtering and detail behaviour as assumptions until direct evidence is captured.

## 12. Recommended Next Action

Execute `plan.md` from Phase 0, complete the canonical actor and permission outputs, and collect targeted evidence for opportunity filters, detail pages, onboarding, NDA completion, commitment, and settlement before promoting those behaviours to `CONFIRMED`.