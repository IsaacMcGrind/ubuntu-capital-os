# Ubuntu Capital Implementation Coverage Gap Matrix

Status: `ANALYSIS_IN_PROGRESS`

This matrix maps the currently inspected implementation repository (`/Users/officialnumbr10/Dev/ubuntu-capital-platform`) to the 41-use-case catalogue in `docs/04-use-cases/use-case-catalogue.md`.

Evidence basis used for this pass:

- Route and page inventory from `src/App.tsx` and `src/pages/*`
- Shared portal navigation from `src/components/PortalLayout.tsx`
- Opportunity and portfolio data sources from `src/data/opportunities.ts`
- Baseline verification run: `npm test -- --run` and `npm run build` (both succeeded)

Important gating rule: `COMPONENT_COMPLETE` in this matrix means UI/page-level evidence exists. It is not equivalent to end-to-end business completion for regulated investment workflows.

## Coverage Summary

The summary below is derived from the 41 row-level delivery statuses in this matrix.

- Total use cases mapped: 41
- `COMPONENT_COMPLETE` (UI-level only): 7
- `IN_DEVELOPMENT` (partial/prototype): 16
- `READY_FOR_DEVELOPMENT` (no substantive implementation evidence): 18
- `COMPLETE`: 0

## Use-case Mapping

| Use Case ID | Delivery Status | Implementation Evidence | Gap Summary | Next Evidence Gate |
|---|---|---|---|---|
| UC-PUB-001 | COMPONENT_COMPLETE | `src/pages/Index.tsx` | Public proposition and navigation are implemented as front-end UI. | Add analytics/events and traceable acceptance test evidence. |
| UC-IAM-001 | IN_DEVELOPMENT | `src/pages/Login.tsx`, `src/pages/MfaVerify.tsx` | Login and MFA screens exist, but no auth service/session enforcement was found. | Implement backend auth, session management, and auth-path tests. |
| UC-IAM-002 | IN_DEVELOPMENT | `src/pages/ForgotPassword.tsx` | Reset UI exists only; no token, identity, or email flow evidence. | Implement reset token lifecycle and recovery-path validation. |
| UC-IAM-003 | READY_FOR_DEVELOPMENT | No explicit logout/session-expiry logic found | Session termination/expiry behavior is not evidenced. | Implement explicit sign-out, expiry, and unauthorized-session handling tests. |
| UC-ONB-001 | IN_DEVELOPMENT | `src/pages/Signup.tsx` | Registration form UI exists without backend account creation evidence. | Add account creation workflow, persistence, and validation tests. |
| UC-ONB-002 | IN_DEVELOPMENT | `src/pages/Onboarding.tsx` | Multi-step onboarding UI exists; no persisted onboarding workflow. | Implement profile persistence, validation rules, and step-state recovery. |
| UC-ONB-003 | IN_DEVELOPMENT | `src/pages/Onboarding.tsx` (Verify step) | KYC/AML and accreditation are represented as placeholders only. | Integrate identity/compliance services and decision-state evidence. |
| UC-OPP-001 | COMPONENT_COMPLETE | `src/pages/Opportunities.tsx`, `src/components/HoverExpandCard.tsx`, `src/data/opportunities.ts` | Opportunity cards/categories are implemented with static local data. | Add catalog source-of-truth, access controls, and data freshness checks. |
| UC-OPP-002 | IN_DEVELOPMENT | `src/pages/Opportunities.tsx`, `src/pages/PortfolioOpportunities.tsx` | Client-side filters/sort chips exist without backend filtering semantics. | Implement server-side filter/sort contract and validation tests. |
| UC-OPP-003 | IN_DEVELOPMENT | `src/pages/DealDetail.tsx` | Detail page exists with static copy and local data. | Add canonical opportunity detail API, policy checks, and audit events. |
| UC-DD-001 | IN_DEVELOPMENT | `src/pages/DealDetail.tsx` (`Request data room` action) | NDA trigger affordance exists; no enforceable NDA process was found. | Implement NDA workflow, signature evidence, and access-state transitions. |
| UC-DD-002 | READY_FOR_DEVELOPMENT | No protected data-room route/service found | Restricted due-diligence content access is not implemented. | Add protected content service, authorization checks, and access logs. |
| UC-INV-001 | IN_DEVELOPMENT | `src/pages/DealDetail.tsx` (`Express interest`) | Interest/commitment action exists as UI control without workflow backend. | Implement commitment lifecycle and policy validation for binding vs non-binding modes. |
| UC-INV-002 | IN_DEVELOPMENT | `src/pages/PortfolioPending.tsx` | Pending area exists with static in-memory rows. | Add status transitions, operator decisions, and exception handling traces. |
| UC-INV-003 | READY_FOR_DEVELOPMENT | No cancel/withdraw workflow evidence found | Cancellation policy and execution path are absent. | Implement withdrawal rules, audit trail, and user/operator permissions. |
| UC-SET-001 | READY_FOR_DEVELOPMENT | No funding-instruction service/routes found | Funding instruction generation and delivery are absent. | Implement settlement instruction pipeline and communication evidence. |
| UC-SET-002 | READY_FOR_DEVELOPMENT | No funds recording/reconciliation logic found | No banking/payment integration or reconciliation workflow found. | Implement settlement ledger, matching rules, and reconciliation tests. |
| UC-SET-003 | READY_FOR_DEVELOPMENT | No settlement exception workflow found | Exception remediation flows are absent. | Implement settlement exception queue, controls, and operator audit logging. |
| UC-PORT-001 | COMPONENT_COMPLETE | `src/pages/PortfolioPending.tsx` | Pending investments page exists at UI level. | Connect to real investment state and verify lifecycle consistency. |
| UC-PORT-002 | COMPONENT_COMPLETE | `src/pages/PortfolioHoldings.tsx` | Holdings table exists with static mock records. | Integrate holdings source, ownership model, and valuation provenance. |
| UC-PORT-003 | IN_DEVELOPMENT | `src/pages/PortfolioPerformance.tsx` | Performance cards exist; chart is explicitly a placeholder. | Implement valuation/performance engine and calculation verification tests. |
| UC-PORT-004 | COMPONENT_COMPLETE | `src/pages/PortfolioActivities.tsx` | Activity timeline UI exists with static sample events. | Add event sourcing/audit integration and exportable activity evidence. |
| UC-DOC-001 | IN_DEVELOPMENT | `src/pages/PortfolioReports.tsx` | Reports/tax docs UI and download buttons exist without document service. | Implement document generation, access controls, and retrieval audit logs. |
| UC-NEWS-001 | COMPONENT_COMPLETE | `src/pages/PortfolioNews.tsx` | News feed UI exists with local static updates. | Integrate content feed source, relevance logic, and publication traceability. |
| UC-EVENT-001 | COMPONENT_COMPLETE | `src/pages/Events.tsx` | Events/webinars page exists with static events list. | Implement event catalogue backend and registration workflow tracking. |
| UC-PROFILE-001 | IN_DEVELOPMENT | `src/pages/PortfolioProfile.tsx` | Profile form UI exists; save action has no persisted backend evidence. | Implement profile update API, validations, and change audit trails. |
| UC-REF-001 | IN_DEVELOPMENT | `src/pages/Referrals.tsx` | Referral page exists with static link display only. | Implement referral submission, attribution, and abuse controls. |
| UC-NOTIFY-001 | IN_DEVELOPMENT | `src/pages/PortfolioNotifications.tsx` | Notification preferences UI exists with local toggles only. | Implement trigger engine, channel delivery, and preference persistence. |
| UC-OPS-001 | IN_DEVELOPMENT | `src/pages/Contact.tsx` | Support contact form exists without ticket workflow evidence. | Implement support case creation, routing, and SLA/audit instrumentation. |
| UC-OPS-002 | READY_FOR_DEVELOPMENT | No controlled correction workflow found | Controlled data correction and maker-checker governance are absent. | Implement governed correction workflow with approvals and immutable audit trail. |
| UC-ADMIN-001 | READY_FOR_DEVELOPMENT | No admin opportunity-creation surface found | Opportunity publish workflow is absent in current codebase. | Implement admin create/publish flow with compliance gates. |
| UC-ADMIN-002 | READY_FOR_DEVELOPMENT | No admin lifecycle management surface found | Opportunity update/close/archive controls are absent. | Implement lifecycle controls and investor-facing state propagation. |
| UC-ADMIN-003 | READY_FOR_DEVELOPMENT | No users/roles/permissions admin flow found | Access governance controls are absent. | Implement RBAC administration and scoped access controls. |
| UC-ADMIN-004 | READY_FOR_DEVELOPMENT | No reference-data/content admin flow found | Platform content/reference-data management is absent. | Implement admin content/reference-data tools with approval workflow. |
| UC-AUD-001 | READY_FOR_DEVELOPMENT | No audit-event pipeline found | No auditable event recording/review capability was evidenced. | Implement audit instrumentation, retention policy, and review interfaces. |
| UC-AUD-002 | READY_FOR_DEVELOPMENT | No compliance/security investigation workflow found | Investigation and incident review capability is absent. | Implement compliance/security event investigation workflow and evidence capture. |
| UC-REPORT-001 | READY_FOR_DEVELOPMENT | No operational/compliance report engine found | Managerial/compliance reporting workflow is absent. | Implement reporting datasets, authorization, and scheduled report evidence. |
| UC-INT-001 | READY_FOR_DEVELOPMENT | No identity/KYC integration contracts found | External identity/KYC/AML integration is absent. | Define and implement provider integration contracts and failure handling. |
| UC-INT-002 | READY_FOR_DEVELOPMENT | No e-signature agreement integration found | Electronic agreement execution evidence is absent. | Implement e-sign integration with signed artifact retention. |
| UC-INT-003 | READY_FOR_DEVELOPMENT | No messaging integration service found | Delivery evidence for email/in-app communications is absent. | Implement notification delivery provider integration and delivery audit logs. |
| UC-INT-004 | READY_FOR_DEVELOPMENT | No banking/payment integration found | Settlement data exchange integrations are absent. | Implement banking/payment integration with reconciliation controls. |

## Notes for Reconciliation

1. This matrix is evidence from implementation code inspection, not a production-readiness declaration.
2. `COMPONENT_COMPLETE` rows still require backend, security, persistence, and E2E verification before any use case can become `COMPLETE`.
3. External implementation evidence has been treated as supporting evidence under the repository evidence hierarchy, not canonical requirement truth.
