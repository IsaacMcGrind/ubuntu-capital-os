# UC-PORT-001 — View pending investments

## 1. Objective
Understand investments awaiting completion or resolution

## 2. Evidence Classification
- Status: CONFIRMED

## 3. Source References
- ["SRC-001"]

## 4. Primary Actor
- Investor

## 5. Supporting Actors
- To be confirmed from actor matrix.

## 6. Preconditions
- Required dependencies and access policies are satisfied.

## 7. Trigger
- Actor initiates View pending investments.

## 8. Main Success Flow
1. Actor starts the use case.
2. Platform validates authorization and input.
3. Platform processes request and persists state where required.
4. Actor receives outcome and status.

## 9. Alternate Flows
- Alternate channel or optional decision path may apply.

## 10. Exception Flows
- Validation failure.
- Unauthorized or insufficient role.
- Integration/provider failure where relevant.

## 11. Postconditions
- Use-case state transition is recorded consistently.

## 12. Business Rules
- See docs/05-business-rules/business-rules.md.

## 13. Data Entities
- Domain entities to be finalized via state and integration analysis.

## 14. Integrations
- Integration dependencies are defined in docs/08-integrations/integration-catalogue.md.

## 15. Permissions
- Permissions are defined in docs/02-actors-and-permissions/permissions-matrix.md.

## 16. Audit Requirements
- Sensitive actions require structured business audit events.

## 17. Non-Functional Requirements
- Security, reliability, and observability controls must follow repository governance.

## 18. Dependencies
- IAM, investment records

## 19. Risks
- Risk classification: HIGH

## 20. Assumptions and Unknowns
- Evidence-driven assumptions remain open until validated.

## 21. Acceptance Criteria
- Behavior is implemented, reachable, and policy-compliant.
- Success and failure paths are covered by tests.

## 22. E2E Completion Criteria
- End-to-end flow is validated in deployed-like environment.

## 23. E2E Evidence Required
- Test run evidence.
- Traceability linkage.
- Audit/security evidence where applicable.
