# Assumptions and Evidence Register

## Source inventory

| Source ID | Source Type | Name | Scope | Reliability | Important Content | Limitations |
|---|---|---|---|---|---|---|
| SRC-001 | Screenshot set | Public and authenticated OurCrowd screens | Investor-facing UI | High for visible UI only | Navigation, opportunity cards, asset classes, news, portfolio sections, NDA action | Does not prove backend rules, permissions, calculations or integrations |
| SRC-002 | URL | `https://www.ourcrowd.com/` | Public website route | Medium | Confirms public platform location | No captured route crawl in this reconstruction |
| SRC-003 | URL | `https://www.ourcrowd.com/myportfolio/home` | Authenticated portfolio route | High for route naming | Confirms portfolio-home route pattern | Authentication and route guards were not observed directly |
| SRC-004 | User-supplied report | App / Website Reverse-Engineering Report | Product and architecture interpretation | Medium | Personas, pages, likely data model, workflows and rebuild stack | Contains assumptions and must not be treated as direct evidence |
| SRC-005 | Execution prompt | Enterprise System Reconstruction and Use-Case Discovery Agent | Required analytical method and repository outputs | High for project process | Evidence classifications, stages, schemas, backlog and traceability requirements | Describes method rather than target-system behaviour |
| SRC-006 | Repository | `IsaacMcGrind/ubuntu-capital-os` | Target reconstruction repository | High | Empty baseline repository with `master` branch at start | Contains no pre-existing product implementation or evidence |

## Classification rules

- `CONFIRMED`: directly visible or explicitly supplied.
- `INFERRED`: reasonably implied but not verified.
- `UNKNOWN`: insufficient evidence.
- `CONTRADICTED`: incompatible source descriptions.

## Material findings

| Finding | Status | Sources | Why it matters | Verification required |
|---|---|---|---|---|
| The platform has a public website and authenticated portfolio area | CONFIRMED | SRC-001, SRC-002, SRC-003 | Establishes public/private product boundary | Observe unauthenticated route behaviour and login redirect |
| Investors can browse opportunity cards and categories | CONFIRMED | SRC-001 | Core discovery capability | Inspect opportunity detail and filters |
| Portfolio navigation includes pending, performance, holdings, reports/tax docs and activities | CONFIRMED | SRC-001 | Defines core investor-management domains | Open each section and record states and data |
| An NDA action exists for at least one opportunity | CONFIRMED | SRC-001 | Indicates controlled due-diligence access | Execute NDA path and inspect legal/e-signature behaviour |
| The system verifies investor accreditation and performs KYC/AML | INFERRED | SRC-004 | Regulated-platform reconstruction depends on it | Observe onboarding, inspect forms, policies, API traffic and support material |
| Investors can make binding commitments and settle funds digitally | INFERRED | SRC-004 | Central revenue workflow | Execute test investment in a safe environment or obtain workflow documentation |
| Portfolio performance is calculated from valuations, cash flows and exits | INFERRED | SRC-001, SRC-004 | Determines financial correctness | Inspect displayed calculations, reports and source data |
| Administrators can create and manage opportunities | INFERRED | SRC-004 | Required operational capability | Inspect admin tooling or interview operators |
| Internal roles have unrestricted authority | UNKNOWN | None | Avoids unsafe permission assumptions | Obtain role matrix and access tests |
| Payment provider, KYC provider and e-signature vendor | UNKNOWN | None | Integration design cannot be finalised | Inspect network traffic, contracts or configuration |

## Contradictions

No direct contradictions are presently supported by the supplied evidence. The prior report includes implementation guesses; these are classified as inferred rather than contradictions.

## Faithful reconstruction versus improvement

The current repository records observed behaviour separately from recommendations. A design choice that appears preferable must not replace reference behaviour unless it is documented as a future enhancement.
