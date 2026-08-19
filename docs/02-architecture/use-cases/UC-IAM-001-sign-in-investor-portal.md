# UC-IAM-001 — Sign in to the Private Investor Portal

**Domain:** Identity and Access (IAM)  
**Primary Actor:** Registered Investor  
**Priority:** Critical  
**Architecture Status:** Complete — decisions accepted  
**Evidence Status:** Inferred  
**Last Updated:** 2026-08-19

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
- Ubuntu Capital OS Priority Use Cases & Business Benefits report, 09 August 2026

Relevant source statements:

- UC-IAM-001 outcome: **Establish an authorised session**.
- IAM domain purpose: authenticate users, protect private routes, manage sessions and account access.
- The priority-use-case report states that sign-in protects private investor, opportunity and portfolio information.
- Current implementation evidence does not yet verify the authentication mechanism, session lifecycle, route/API enforcement, MFA, audit trail or related security controls.

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

## 3.2 Current State

The Ubuntu Capital OS documentation defines an Identity and Access domain responsible for authentication, protected routes and sessions, but this capability is currently classified as **INFERRED**.

The contractor implementation register confirms that a deployed Ubuntu Capital web experience exists. However, the contractor source repository has not yet been inspectable through the connected GitHub context, so the implementation of UC-IAM-001 has not been verified end-to-end.

The following remain unverified in the current implementation:

- authentication provider;
- credential mechanism;
- session/token model;
- MFA capability;
- session expiry and revocation;
- logout behaviour;
- API-level protection;
- brute-force and rate-limit controls;
- audit and security-event capture.

The current repository therefore provides **insufficient implementation evidence** to claim this use case complete.

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

### Requirement → Current State → Target Architecture → Gap

**Requirement**  
A registered investor must be able to establish a trusted authorised session.

**Current State**  
IAM capability exists in the documented architecture, but the implementation cannot yet be verified end-to-end.

**Target Architecture**  
A defined Identity and Access boundary owns authentication, session state and authenticated identity, while downstream domains own business eligibility and authorisation facts.

**Gap**  
The implementation must be verified or completed for:

- authentication-provider integration;
- session lifecycle;
- protected route and API enforcement;
- authenticated identity propagation;
- security controls;
- audit/security telemetry;
- IAM-to-business-domain contracts.

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

| Decision ID | Decision | Status |
|---|---|---|
| IAM-D01 | Authentication and investor eligibility remain separate concerns. Login establishes identity/session and does not re-run or own eligibility determination. | Accepted |
| IAM-D02 | Identity & Access is authoritative for authenticated principal and session state. Investor Onboarding & Eligibility is authoritative for eligibility/compliance state. | Accepted |
| IAM-D03 | Use a standards-based identity-provider boundary rather than implementing credential/password authentication inside Ubuntu Capital OS. Vendor selection remains deferred. | Accepted |
| IAM-D04 | Protected backend/API capabilities must independently validate authentication and required business permissions. Frontend route protection alone is insufficient. | Accepted |
| IAM-D05 | Authentication/access events feed Audit & Evidence, while operational security telemetry and formal business audit evidence remain logically distinct concerns. | Accepted |
| IAM-D06 | MFA capability must be supported in the production authentication architecture. Whether MFA is mandatory for every investor remains a later policy/security decision. | Accepted |
| IAM-D07 | UC-IAM-001 establishes sessions. Account recovery and detailed session termination remain primarily within UC-IAM-002 and UC-IAM-003. | Accepted |
| IAM-D08 | No microservice topology, queueing platform, cloud provider or database technology is selected from this use case alone. | Accepted |

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

## Architecture Outcome

UC-IAM-001 establishes the platform authentication boundary.

The accepted architectural principle is:

> **Authentication establishes who the user is. Eligibility and downstream business domains determine what that authenticated user may access or do.**
