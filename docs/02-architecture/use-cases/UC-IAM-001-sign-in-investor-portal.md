# UC-IAM-001 — Sign in to the Private Investor Portal

**Domain:** Identity and Access (IAM)  
**Primary Actor:** Registered Investor  
**Priority:** Critical  
**Architecture Status:** Complete — decisions accepted  
**Requirement Evidence:** INFERRED  
**Current Reproducible Implementation Verification:** BLOCKED_BY_CONTEXT  
**Historical Snapshot Label:** IN_DEVELOPMENT  
**Last Updated:** 2026-09-04

---

## 1. Purpose

UC-IAM-001 establishes trusted authenticated access to the Ubuntu Capital private investor portal.

The documented outcome is to establish an authorised session for a registered investor. This capability is foundational because personalised, confidential and restricted platform capabilities depend on trusted authentication.

This use case does **not** determine investor eligibility. Authentication and eligibility are separate concerns.

---

## 2. Source Basis

This analysis is based on the following project sources:

- `docs/04-use-cases/use-case-catalogue.md`
- `docs/03-functional-domains/domains.md`
- `docs/01-system-understanding/system-overview.md`
- `docs/11-open-questions/open-questions.md`
- `contractors/80kDevelopers/implementation-status.md`
- `docs/09-delivery/implementation-coverage-gap-matrix.md`
- `docs/09-delivery/prioritized-backlog-diff.md`
- Ubuntu Capital OS Priority Use Cases & Business Benefits report, 09 August 2026

Relevant source statements:

- UC-IAM-001 outcome: **Establish an authorised session**.
- IAM domain purpose: authenticate users, protect private routes, manage sessions and account access.
- The priority-use-case report states that sign-in protects private investor, opportunity and portfolio information.
- Repository artifacts report that an unpinned local snapshot contained login and MFA user-interface components.
- That historical inspection did not report a backend authentication service or enforced session-management implementation within the inspected snapshot.
- The implementation coverage matrix therefore preserves `IN_DEVELOPMENT` as a historical snapshot label only. Current reproducible implementation verification is `BLOCKED_BY_CONTEXT` because the source branch, commit SHA, run identity, and durable raw evidence are not recorded.

### Evidence interpretation

The source requirement for UC-IAM-001 remains `INFERRED`. Reported login/MFA screens in an unpinned snapshot support historical implementation intent, not current behaviour or the complete business capability.

The snapshot observations are historical/partial supporting evidence and do not override the documented requirement or accepted architecture decisions. They must not be promoted to current-state evidence until an authorised revision-pinned inspection and durable run record exist.

---

# 3. Architecture Analysis

## 3.1 Requirement

The system must allow a registered investor to authenticate and establish an authorised session before accessing protected investor functionality.

The system must:

- establish the identity of the caller;
- create or recognise an authenticated session;
- make authenticated identity available to protected platform capabilities;
- deny protected access when authentication cannot be established or validated;
- support downstream authorisation decisions without embedding investor eligibility into the sign-in process.

### Requirement boundary

Authentication answers:

> **Who is this user?**

Eligibility and business controls answer:

> **What may this authenticated user access or do?**

Eligibility must therefore not be re-evaluated as part of every authentication event unless a downstream policy specifically requires the current eligibility state.

---

## 3.2 Historical Snapshot Evidence and Current Verification Boundary

Repository artifacts report a local inspection of an implementation-repository snapshot, but the exact branch, commit SHA, run identity, and durable raw-evidence reference are not recorded. The observations below are therefore historical/partial only and cannot establish present implementation behaviour.

### Reported snapshot observations

The historical coverage review references:

- `src/pages/Login.tsx` — reported login user-interface surface;
- `src/pages/MfaVerify.tsx` — reported MFA verification user-interface surface.

The artifacts also report that the snapshot built successfully and passed its baseline tests. Those unpinned results may guide reinspection, but they do not confirm current repository health or UC-IAM-001 end-to-end behaviour.

### Not evidenced in the reported snapshot

The historical review did not report evidence of:

- a backend authentication service;
- server-side session establishment;
- server-side session validation;
- protected backend/API enforcement;
- persistent authentication/session state;
- authentication-provider integration;
- logout/session-expiry implementation sufficient to satisfy UC-IAM-003;
- audit-event persistence for authentication outcomes;
- backend negative-path tests proving protected access is denied to unauthenticated callers.

Absence from an unpinned historical snapshot is not proof of current absence. The coverage matrix preserves the following historical label:

> **IN_DEVELOPMENT — the reported snapshot contained login/MFA UI, while no backend auth service/session enforcement was reported.**

Current reproducible source verification is:

> **BLOCKED_BY_CONTEXT — inspected source revision and durable run evidence are missing.**

### Evidence interpretation

```text
Historical unpinned snapshot
----------------------------
Login UI                 REPORTED
MFA UI                   REPORTED
Authentication backend  NOT EVIDENCED IN SNAPSHOT
Session enforcement     NOT EVIDENCED IN SNAPSHOT
API protection          NOT EVIDENCED IN SNAPSHOT
Auth audit persistence  NOT EVIDENCED IN SNAPSHOT
E2E auth validation     NOT EVIDENCED IN SNAPSHOT

Current reproducible verification
---------------------------------
Source revision          UNKNOWN
Durable run evidence     UNKNOWN
Implementation status   BLOCKED_BY_CONTEXT
```

These snapshot observations support architecture-gap and validation planning. They do not prove whether the documented outcome—an authorised session—is currently established and enforced end to end.

---

## 3.3 Target Architecture

Identity and Access becomes the authoritative platform capability for:

- authentication;
- authenticated principal resolution;
- session establishment;
- session validation;
- authentication security controls;
- authentication context exposed to downstream capabilities.

Identity and Access does **not** own:

- investor eligibility;
- KYC/AML status;
- accreditation status;
- NDA access state;
- opportunity lifecycle state;
- investment state.

These remain owned by their corresponding business domains.

### Logical flow

```text
Registered Investor
        |
        v
Investor Experience
        |
        v
Identity & Access
  - authenticate
  - establish session
  - resolve investor identity
        |
        | AuthenticatedIdentity
        v
Protected Capability
        |
        +--> consult eligibility/business state where required
        |
        v
Allow or deny requested action
```

### Core identity contract

The platform should expose an authenticated identity context conceptually containing:

```text
AuthenticatedIdentity
---------------------
subjectId
investorId / accountId
sessionId
authenticationTime
authenticationStrength
```

It should not carry authoritative business-state claims such as:

```text
eligible
accredited
ndaAccepted
mayInvest
```

unless those claims are explicitly derived from and governed by the authoritative business domain.

---

## 3.4 Gap

### Requirement → Historical Snapshot Boundary → Target Architecture → Gap

**Requirement**  
A registered investor must be able to establish a trusted authorised session.

**Historical Snapshot / Current Verification Boundary**  
An unpinned reported snapshot described login and MFA user-interface components and did not evidence the backend authentication, session enforcement, persistence, API protection, or audit capability required for the end-to-end outcome. Because the source revision and durable run are unknown, those observations do not establish current implementation behaviour; current reproducible verification remains `BLOCKED_BY_CONTEXT`.

**Target Architecture**  
A defined Identity and Access boundary owns authentication, session state and authenticated identity, while downstream domains own business eligibility and authorisation facts.

**Gap**  
The implementation must add or verify:

- standards-based authentication-provider integration;
- server-side session establishment and validation;
- protected route and backend/API enforcement;
- authenticated identity propagation to protected capabilities;
- authentication failure and negative-path handling;
- audit/security event capture and persistence;
- IAM-to-business-domain identity contracts;
- automated validation proving valid login succeeds and unauthenticated/invalid access fails closed.

### Delivery evidence gate

The current delivery backlog defines the following concrete acceptance direction for UC-IAM-001:

- successful login creates a server-recognised session;
- invalid credentials are rejected;
- protected routes reject unauthenticated requests;
- relevant authentication outcomes produce audit evidence.

These are future delivery/verification criteria derived from the historical gap analysis and target architecture. They refine how the target can be proven without converting the unpinned snapshot into current implementation evidence or changing the accepted business boundary of this use case.

---

# 4. Technical Architecture Direction

The architecture should use a standards-based identity-provider boundary rather than implement password and credential security directly inside Ubuntu Capital OS.

Vendor selection is intentionally deferred.

Conceptually:

```text
Investor Browser
      |
      v
External Identity Provider
  - credentials
  - authentication factors
  - authentication protocol
      |
      | identity assertion / token
      v
Ubuntu Capital OS
Identity & Access Layer
  - validate identity
  - establish application context
  - enforce authentication
      |
      v
Business Capabilities
```

Authentication remains synchronous in the user journey. Queues or asynchronous processing are not required in the sign-in critical path.

Secondary security analytics, notifications or audit enrichment may be processed asynchronously if later justified.

---

# 5. Production and NFR Considerations

## Security

The target implementation should support:

- TLS for authentication and session traffic;
- secure credential handling by the identity provider;
- secure token/session storage;
- API/backend authentication enforcement;
- rate limiting and brute-force protection;
- MFA capability;
- session expiry and revocation;
- least-privilege access controls;
- prevention of embedded credentials or secrets in client code;
- secure handling of authentication failures.

## Reliability

Authentication validation must fail closed.

If identity cannot be trusted, protected access must not be granted.

The public experience should remain independently available where possible even if private authentication services are degraded.

## Observability

At minimum, monitor:

- successful sign-ins;
- failed sign-ins;
- repeated authentication failures;
- token/session validation failures;
- denied protected requests;
- unusual access patterns;
- identity-provider availability.

## Audit

Material authentication and access events should preserve enough evidence to determine:

- who acted;
- what occurred;
- when it occurred;
- which account/session was involved;
- whether the action succeeded or failed;
- the reason or event category where appropriate.

Authentication secrets, passwords and sensitive token contents must never be written to logs.

---

# 6. Related Use Cases

UC-IAM-001 is foundational to:

- `UC-ONB-001` — Register as a prospective investor
- `UC-ONB-002` — Complete investor profile and eligibility onboarding
- `UC-ONB-003` — Verify investor identity and compliance status
- `UC-OPP-001` — Browse visible investment opportunities
- `UC-DD-001` — Initiate an NDA action
- `UC-DD-002` — Access confidential due-diligence materials
- `UC-INV-001` — Submit an investment commitment / expression of interest
- `UC-PORT-*` — Portfolio capabilities
- `UC-DOC-001` — Reports and tax documents
- `UC-ADMIN-003` — Manage users, roles and permissions
- `UC-AUD-001` — Record and review audit events

### Key relationship

```text
UC-IAM-001
Authentication
     |
     v
Who is this?
     |
     +--> Onboarding / Eligibility
     |      Are they eligible?
     |
     +--> Due Diligence
     |      May they see this?
     |
     +--> Investment
            May they perform this action?
```

---

# 7. Accepted Architecture Decisions

The reported historical snapshot evidence does not contradict any previously accepted architecture decision. Because the snapshot is unpinned, it is not current implementation verification.

| Decision ID | Decision | Status |
|---|---|---|
| IAM-D01 | Authentication and investor eligibility remain separate concerns. Login establishes identity/session and does not re-run or own eligibility determination. | Accepted — reaffirmed |
| IAM-D02 | Identity & Access is authoritative for authenticated principal and session state. Investor Onboarding & Eligibility is authoritative for eligibility/compliance state. | Accepted — reaffirmed |
| IAM-D03 | Use a standards-based identity-provider boundary rather than implementing credential/password authentication inside Ubuntu Capital OS. Vendor selection remains deferred. | Accepted — reaffirmed |
| IAM-D04 | Protected backend/API capabilities must independently validate authentication and required business permissions. Frontend route protection alone is insufficient. | Accepted — reaffirmed; historically reported UI-only evidence supports reinspection priorities |
| IAM-D05 | Authentication/access events feed Audit & Evidence, while operational security telemetry and formal business audit evidence remain logically distinct concerns. | Accepted — reaffirmed |
| IAM-D06 | MFA capability must be supported in the production authentication architecture. Whether MFA is mandatory for every investor remains a later policy/security decision. | Accepted — reaffirmed; historically reported MFA UI does not establish current behaviour |
| IAM-D07 | UC-IAM-001 establishes sessions. Account recovery and detailed session termination remain primarily within UC-IAM-002 and UC-IAM-003. | Accepted — reaffirmed |
| IAM-D08 | No microservice topology, queueing platform, cloud provider or database technology is selected from this use case alone. | Accepted — reaffirmed |

---

# 8. HLA Impact

**Classification:** HLA clarification — no new capability required.

The High-Level Architecture already contains both:

- Identity & Access;
- Investor Onboarding & Eligibility.

UC-IAM-001 clarifies the ownership boundary:

```text
Identity & Access owns
----------------------
Authentication
Session state
Authenticated identity

Investor Onboarding & Eligibility owns
---------------------------------------
Eligibility
KYC/AML status
Accreditation / compliance status

Protected business capability combines
--------------------------------------
Authenticated identity
+
Required business-domain controls
```

The historical snapshot evidence does not require a structural HLA change. It supports the planned validation of a possible gap between reported front-end authentication screens and an enforceable IAM capability; current implementation state remains unverified.

This clarification should be inherited by all subsequent use-case analyses.

---

# 9. Deferred Decisions / Open Items

The following remain intentionally unresolved:

- identity provider/vendor;
- authentication protocol implementation detail;
- token versus server-side session mechanism;
- session lifetime;
- MFA enforcement policy;
- account recovery mechanism;
- detailed session termination rules;
- role and permission model;
- jurisdiction-specific authentication or identity requirements.

These should be resolved by the use cases or architecture decisions that own those concerns.

---

## Historical Evidence Outcome and Current Verification

The historical snapshot record informs validation priorities; it does not change the accepted target architecture or establish current implementation state.

Repository artifacts report login and MFA interfaces in an unpinned snapshot, while backend authentication and an enforceable session boundary were not evidenced in that snapshot. The exact source revision and durable run record remain `UNKNOWN`, so current reproducible implementation verification is `BLOCKED_BY_CONTEXT`.

The architectural principle remains:

> **Authentication establishes who the user is. Eligibility and downstream business domains determine what that authenticated user may access or do.**

UC-IAM-001 remains architecturally complete as an analysis. `IN_DEVELOPMENT` is retained only as a historical snapshot label; no current delivery status may be asserted until revision-pinned evidence exists, and eventual completion still requires the authorised-session outcome to be implemented and verified end to end.
