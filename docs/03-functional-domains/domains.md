# Functional Domains

This domain map separates directly observed investor-facing capabilities from regulated, operational, and administrative capabilities that still require validation.

| Domain Code | Domain | Purpose | Evidence Status | Principal Sources |
|---|---|---|---|---|
| PUB | Public Experience | Explain the platform, establish trust, and convert visitors into prospective investors | CONFIRMED | SRC-001, SRC-002 |
| IAM | Identity and Access | Authenticate users, protect private routes, manage sessions and account access | INFERRED | SRC-003, SRC-004 |
| ONB | Investor Onboarding | Capture profile, eligibility, accreditation, KYC/AML, agreements, and suitability information | INFERRED | SRC-004 |
| OPP | Opportunity Discovery | Present trending, new, and categorised investment opportunities and support discovery | CONFIRMED | SRC-001 |
| DD | Due Diligence Access | Control access to confidential opportunity information, including NDA-dependent content | CONFIRMED for NDA action; remaining behaviour INFERRED | SRC-001, SRC-004 |
| INV | Investment Commitment | Capture, validate, approve, and track an investor's commitment to an opportunity | INFERRED | SRC-004 |
| SET | Funding and Settlement | Provide funding instructions, track incoming funds, reconcile settlement, and resolve exceptions | UNKNOWN | None |
| PORT | Portfolio Management | Show pending investments, holdings, performance, and activity | CONFIRMED for navigation; calculations INFERRED | SRC-001, SRC-004 |
| DOC | Documents and Tax Reporting | Make reports and tax documents available to authorised investors | CONFIRMED for navigation; generation workflow UNKNOWN | SRC-001 |
| NEWS | Portfolio News and Content | Deliver investor-relevant company, fund, event, and educational content | CONFIRMED | SRC-001 |
| EVENT | Events and Webinars | Present investor events and webinars | CONFIRMED for navigation | SRC-001 |
| NOTIFY | Notifications and Engagement | Notify users about opportunity, portfolio, document, or operational events | INFERRED | SRC-004 |
| REF | Referrals | Allow investors to refer other prospective investors | CONFIRMED for navigation | SRC-001 |
| PROFILE | Investor Profile | Manage personal, preference, suitability, and account information | CONFIRMED for navigation; fields UNKNOWN | SRC-001 |
| OPS | Operations and Support | Handle support, corrections, overrides, escalations, reconciliation, and exceptions | INFERRED | SRC-001, SRC-004 |
| ADMIN | Platform Administration | Manage opportunities, content, users, permissions, reference data, and platform configuration | INFERRED | SRC-004 |
| AUD | Audit, Compliance and Risk | Record decisions and events, enforce controls, support compliance and investigations | INFERRED | SRC-004 |
| REPORT | Management Reporting | Provide operational, investment, compliance, and business reporting | INFERRED | SRC-004 |
| INT | External Integrations | Connect identity, KYC/AML, e-signature, email, payments/banking, CRM, analytics, and reporting services | UNKNOWN vendors; INFERRED categories | SRC-004 |

## Boundary notes

- `OPP` concerns finding and understanding opportunities.
- `DD` concerns controlled access to confidential investment materials.
- `INV` ends when a commitment is accepted or otherwise reaches a terminal commitment state.
- `SET` concerns the actual funding and reconciliation lifecycle.
- `PORT` concerns post-commitment visibility, valuation, performance, and activity.
- `DOC` concerns investor-facing generated or uploaded documents.
- `ADMIN`, `OPS`, and `AUD` are separate because administrative configuration, operational intervention, and compliance evidence may have different permissions and accountability.
