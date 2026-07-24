# Master Use-Case Catalogue

The catalogue is evidence-first. `CONFIRMED` means the supplied material directly supports the stated capability. It does not confirm every rule, field, route, calculation, or technical implementation detail.

| Use Case ID | Domain | Use Case | Primary Actor | Outcome | Evidence | Priority | Dependencies |
|---|---|---|---|---|---|---|---|
| UC-PUB-001 | PUB | Learn about the investment platform | Prospective investor | Understand the proposition and decide whether to register | CONFIRMED | HIGH | None |
| UC-IAM-001 | IAM | Sign in to the private investor portal | Registered investor | Establish an authorised session | INFERRED | CRITICAL | Account exists |
| UC-IAM-002 | IAM | Recover account access | Registered investor | Regain access after credential or access failure | UNKNOWN | HIGH | Identity verification |
| UC-IAM-003 | IAM | End or expire an investor session | Investor / system | Prevent continued unauthorised access | UNKNOWN | HIGH | Active session |
| UC-ONB-001 | ONB | Register as a prospective investor | Prospective investor | Create an investor account and begin onboarding | INFERRED | CRITICAL | Public experience, IAM |
| UC-ONB-002 | ONB | Complete investor profile and eligibility onboarding | Prospective investor | Submit information needed to determine platform eligibility | INFERRED | CRITICAL | Registration |
| UC-ONB-003 | ONB | Verify investor identity and compliance status | Compliance actor / external service | Establish KYC/AML and accreditation status | INFERRED | CRITICAL | Profile submission, integrations |
| UC-OPP-001 | OPP | Browse visible investment opportunity cards and categories | Eligible investor | Discover available opportunity summaries shown by the reference interface | CONFIRMED | CRITICAL | IAM, access status |
| UC-OPP-002 | OPP | Filter and sort opportunities | Eligible investor | Narrow the opportunity set by investor-relevant criteria | INFERRED | HIGH | Opportunity catalogue |
| UC-OPP-003 | OPP | View an opportunity detail page | Eligible investor | Understand the opportunity, terms, status, and next action | INFERRED | CRITICAL | Opportunity available |
| UC-DD-001 | DD | Initiate an NDA action for an opportunity | Eligible investor | Begin the process required to access restricted opportunity content | CONFIRMED for trigger; flow INFERRED | HIGH | Opportunity, identity, agreement service |
| UC-DD-002 | DD | Access confidential due-diligence materials | NDA-authorised investor | Review restricted opportunity material | INFERRED | HIGH | Valid NDA/access grant |
| UC-INV-001 | INV | Submit an investment commitment | Eligible investor | Record an intention or binding commitment to invest | INFERRED | CRITICAL | Opportunity open, DD where required, eligibility |
| UC-INV-002 | INV | Review and resolve a pending investment | Investor / operations | Reach an accepted, rejected, cancelled, or remediated status | CONFIRMED for pending area; lifecycle INFERRED | CRITICAL | Commitment exists |
| UC-INV-003 | INV | Cancel or withdraw an investment request | Investor / authorised operator | Stop an eligible pending commitment | UNKNOWN | MEDIUM | Pending commitment, cancellation policy |
| UC-SET-001 | SET | Receive funding instructions | Accepted investor | Obtain approved settlement instructions | UNKNOWN | CRITICAL | Accepted commitment |
| UC-SET-002 | SET | Record and reconcile investor funds | Operations / banking integration | Match funds to the correct commitment | UNKNOWN | CRITICAL | Funding receipt, reference data |
| UC-SET-003 | SET | Resolve a settlement exception | Operations | Correct unmatched, partial, late, duplicate, or reversed funding | UNKNOWN | HIGH | Settlement exception |
| UC-PORT-001 | PORT | View pending investments | Investor | Understand investments awaiting completion or resolution | CONFIRMED for navigation | HIGH | IAM, investment records |
| UC-PORT-002 | PORT | View current holdings | Investor | See owned companies, funds, or alternative assets | CONFIRMED for navigation | CRITICAL | Completed investments |
| UC-PORT-003 | PORT | View portfolio performance | Investor | Understand portfolio value and performance | CONFIRMED for navigation; calculations INFERRED | CRITICAL | Holdings, valuations, cash flows |
| UC-PORT-004 | PORT | View portfolio activity history | Investor | Review material portfolio and account events | CONFIRMED for navigation | HIGH | Auditable events |
| UC-DOC-001 | DOC | View and download reports and tax documents | Investor | Obtain authorised portfolio and tax documentation | CONFIRMED for navigation; retrieval flow INFERRED | HIGH | Generated/uploaded documents |
| UC-NEWS-001 | NEWS | View portfolio and opportunity news content | Investor | Stay informed about investments and opportunities | CONFIRMED | MEDIUM | Content catalogue, preferences |
| UC-EVENT-001 | EVENT | Browse investment events and webinars | Investor | Discover relevant educational or engagement events | CONFIRMED for navigation | LOW | Event catalogue |
| UC-PROFILE-001 | PROFILE | View and maintain investor profile | Investor | Keep account and investor information current | CONFIRMED for navigation; fields INFERRED | HIGH | IAM |
| UC-REF-001 | REF | Refer a prospective investor | Investor | Submit a referral through the platform | CONFIRMED for navigation; workflow UNKNOWN | LOW | IAM |
| UC-NOTIFY-001 | NOTIFY | Receive material platform notifications | Investor | Be informed of required actions and significant events | INFERRED | HIGH | Event triggers, delivery channels |
| UC-OPS-001 | OPS | Respond to an investor support request | Support operator | Resolve an investor question or incident | CONFIRMED for contact path; workflow INFERRED | HIGH | Support channel, access controls |
| UC-OPS-002 | OPS | Correct investor or investment data under control | Authorised operator | Resolve verified data defects without compromising auditability | UNKNOWN | HIGH | Approval, audit, reason codes |
| UC-ADMIN-001 | ADMIN | Create and publish an investment opportunity | Opportunity administrator | Make a reviewed opportunity discoverable to eligible investors | INFERRED | CRITICAL | Permissions, content, compliance approval |
| UC-ADMIN-002 | ADMIN | Update, close, pause, or archive an opportunity | Opportunity administrator | Maintain opportunity lifecycle accurately | INFERRED | HIGH | Existing opportunity |
| UC-ADMIN-003 | ADMIN | Manage users, roles, permissions, and data scope | Access administrator | Enforce authorised access | INFERRED | CRITICAL | Governance model |
| UC-ADMIN-004 | ADMIN | Manage platform content and reference data | Administrator | Keep categories, sectors, themes, locations, events, and content current | INFERRED | MEDIUM | Admin permissions |
| UC-AUD-001 | AUD | Record and review audit events | Compliance / authorised operator | Establish traceability for sensitive and material actions | INFERRED | CRITICAL | Event instrumentation |
| UC-AUD-002 | AUD | Investigate a compliance or security event | Compliance / security actor | Determine facts, impact, and remediation | UNKNOWN | HIGH | Audit, logs, access evidence |
| UC-REPORT-001 | REPORT | Produce operational and compliance reports | Authorised manager | Monitor platform operations, risk, and regulatory obligations | INFERRED | HIGH | Source data, reporting permissions |
| UC-INT-001 | INT | Exchange identity or KYC/AML data with an external provider | Platform / provider | Verify investor status reliably | UNKNOWN vendor; capability INFERRED | CRITICAL | Integration contract |
| UC-INT-002 | INT | Execute or record electronic agreements | Platform / e-signature provider | Capture enforceable agreement evidence | UNKNOWN vendor; capability INFERRED | HIGH | Agreement templates |
| UC-INT-003 | INT | Deliver email or in-app communications | Platform / messaging provider | Notify actors and preserve delivery evidence | INFERRED | HIGH | Notification event |
| UC-INT-004 | INT | Exchange settlement data with banking or payment services | Platform / financial service | Support funding and reconciliation | UNKNOWN | CRITICAL | Banking/payment integration |

## Catalogue count

The catalogue contains **41 use cases**.

## Coverage observations

- Confirmed evidence is strongest for visible opportunity cards, categories, investor navigation, portfolio news, and the presence of an NDA trigger.
- Filtering, sorting, detail-page behaviour, regulated onboarding, commitment, settlement, administration, and operational recovery remain incompletely evidenced.
- The first implementation-ready slice must distinguish a demonstrable prototype from a production-regulated investment transaction.