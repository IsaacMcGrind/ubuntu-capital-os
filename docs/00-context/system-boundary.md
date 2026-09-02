# System Boundary

Status: `ANALYSIS_IN_PROGRESS`

This canonical boundary summary links the reconstruction plan to the architecture baseline.

## Boundary statement

Ubuntu Capital OS includes investor and operator experiences, domain logic, controlled data state, permissions, business audit evidence, and integration adapters. External providers remain outside the boundary and must not become authoritative for Ubuntu Capital business state.

The first implementation slice is intentionally narrow: it covers public opportunity discovery, authenticated investor access, and a non-binding Expression of Interest (EOI) signal with a pending-interest status. It excludes binding commitments, settlement, custody, funds handling, and broader regulated/compliance flows until legal and product approval resolves the business model.

## Inside boundary

- Public and authenticated user experiences
- Identity/access decisions and role enforcement
- Opportunity discovery and visibility controls
- NDA/access grants and restricted-content decisions
- Non-binding EOI submission and pending-interest status
- Audience and operator management for the first slice
- Portfolio, reports/documents metadata, notifications
- Administration, support, audit, and management reporting

## Outside boundary

- Binding investment commitments or subscriptions
- Settlement, custody, funds movement, or reconciliation flows
- KYC/AML provider execution for broader regulated onboarding
- Banking/payment rails and escrow operations
- E-signature provider for legal execution workflows
- External messaging channels
- Third-party analytics and CRM systems beyond the first-slice MVP

## Authoritative references

- docs/02-architecture/system-boundary-view.md
- docs/02-architecture/high-level-logical-architecture-v0.1.md
- docs/03-functional-domains/domains.md
