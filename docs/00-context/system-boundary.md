# System Boundary

Status: `ANALYSIS_IN_PROGRESS`

This canonical boundary summary links the reconstruction plan to the architecture baseline.

## Boundary statement

Ubuntu Capital OS includes investor and operator experiences, domain logic, controlled data state, permissions, business audit evidence, and integration adapters. External providers remain outside the boundary and must not become authoritative for Ubuntu Capital business state.

## Inside boundary

- Public and authenticated user experiences
- Identity/access decisions and role enforcement
- Opportunity lifecycle and visibility controls
- NDA/access grants and restricted-content decisions
- EOI/commitment lifecycle state
- Settlement state, exception handling, and reconciliation records
- Portfolio, reports/documents metadata, notifications
- Administration, support, audit, and management reporting

## Outside boundary

- KYC/AML provider execution
- Banking/payment rails
- E-signature provider
- External messaging channels
- Third-party analytics and CRM systems

## Authoritative references

- docs/02-architecture/system-boundary-view.md
- docs/02-architecture/high-level-logical-architecture-v0.1.md
- docs/03-functional-domains/domains.md
