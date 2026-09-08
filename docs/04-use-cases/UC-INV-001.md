# UC-INV-001 — Submit a non-binding expression of interest

## 1. Objective
Record a non-binding investor interest signal before any binding commitment workflow.

## 2. Evidence Classification
- Status: CONFIRMED

## 3. Source References
- ["SRC-004"]

## 4. Primary Actor
- Authenticated investor

## 5. Supporting Actors
- Opportunity operator / platform administrator (for status review and approval support)

## 6. Preconditions
- Investor is authenticated.
- Opportunity is visible and open.
- First-slice business rules are in force.

## 7. Trigger
- Actor initiates Submit a non-binding expression of interest.

## 8. Main Success Flow
1. Actor views an open opportunity.
2. Actor submits a non-binding expression of interest.
3. Platform validates authorization and required inputs.
4. Platform records the interest and sets the opportunity/investor state to pending interest.
5. Actor receives confirmation that the submission is non-binding.

## 9. Alternate Flows
- Investor revisits the opportunity and updates the expression of interest.
- Opportunity is closed or no longer available before submission is processed.

## 10. Exception Flows
- Validation failure.
- Unauthorized or insufficient role.
- Duplicate or conflicting EOI state.
- Integration/provider failure where relevant.

## 11. Postconditions
- A non-binding investor interest record is created and tracked as pending interest.

## 12. Business Rules
- See docs/05-business-rules/business-rules.md.
- First implementation slice treats investor submission as a non-binding EOI and does not create a binding obligation.

## 13. Data Entities
- Investor, opportunity, expression of interest, pending-interest state.

## 14. Integrations
- Integration dependencies are defined in docs/08-integrations/integration-catalogue.md.

## 15. Permissions
- Permissions are defined in docs/02-actors-and-permissions/permissions-matrix.md.

## 16. Audit Requirements
- Sensitive actions require structured business audit events.

## 17. Non-Functional Requirements
- Security, reliability, and observability controls must follow repository governance.

## 18. Dependencies
- Opportunity open, investor authentication, first-slice eligibility and access policy

## 19. Risks
- Risk classification: MEDIUM for first-slice MVP; binding commitment flows remain out of scope.

## 20. Assumptions and Unknowns
- The legal meaning of any future binding action remains open and deferred.

## 21. Acceptance Criteria
- Investor can submit a non-binding EOI from an authenticated session.
- The system records pending-interest status without implying a commitment.
- Success and failure paths are covered by tests.

## 22. E2E Completion Criteria
- End-to-end flow is validated in a deployed-like environment.

## 23. E2E Evidence Required
- Test run evidence.
- Traceability linkage.
- Audit/security evidence where applicable.
