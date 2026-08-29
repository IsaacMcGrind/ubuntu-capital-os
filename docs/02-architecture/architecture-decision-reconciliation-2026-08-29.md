# Ubuntu Capital OS — Architecture Decision Reconciliation

**Date:** 2026-08-29  
**Purpose:** reconcile the existing technology-neutral IAM/use-case architecture with the newly confirmed Azure MVP platform decision.

## Reconciliation outcome

The logical architecture remains authoritative for **business capability ownership**. `ARCH-ADR-001` now supplies the **MVP platform implementation choice** for cloud services.

These are compatible decisions rather than competing architectures.

## UC-IAM-001 reconciliation

`docs/02-architecture/use-cases/UC-IAM-001-sign-in-investor-portal.md` established these durable principles:

- authentication and investor eligibility are separate concerns;
- Identity & Access owns authenticated principal/session state;
- credentials should be handled through a standards-based identity-provider boundary rather than application-built password security;
- protected backend/API capabilities must validate authentication independently of frontend route guards;
- MFA capability is required in the production authentication architecture;
- business audit evidence remains distinct from operational telemetry.

Those principles remain accepted.

### Superseded part of IAM-D03

The original IAM-D03 statement included:

> Vendor selection remains deferred.

That implementation-choice clause is superseded by `ARCH-ADR-001` for the MVP.

The reconciled decision is:

> **IAM-D03-R1:** Use a standards-based identity-provider boundary rather than implementing credential/password authentication inside Ubuntu Capital OS. **Microsoft Entra External ID is the selected customer-identity platform for the MVP.** Detailed tenant configuration, user flows/policies, protocol settings, token/session handling and production enforcement remain delivery-design decisions subject to evidence gates.

This supersession does **not** change UC-IAM-001's implementation status. It remains `IN_DEVELOPMENT` until server-side authentication/session enforcement and E2E evidence exist.

## IAM-D08 reconciliation

IAM-D08 says no cloud provider, queueing platform, database technology or microservice topology is selected **from UC-IAM-001 alone**.

That remains correct. Azure was selected by the broader cloud/platform workstream and project-level `ARCH-ADR-001`, not derived from the IAM use case alone.

## HLA reconciliation

The high-level logical architecture intentionally states that its boxes do not imply Azure, AWS, GCP, microservices, serverless or a database topology.

That rule remains correct: the HLA is a logical view. The Azure decision is a separate deployment/platform mapping beneath it.

```text
System Boundary / HLA
        ↓
Capability ownership and business-state authority
        ↓
Use-case architecture
        ↓
ARCH-ADR-001 Azure MVP platform mapping
        ↓
Provisioned/deployed implementation
        ↓
E2E evidence
```

## Open decisions after reconciliation

The identity vendor is no longer open for the MVP, but these IAM implementation details remain unresolved until delivery proves them:

- Entra External ID tenant/application configuration;
- authentication protocol/configuration detail;
- token versus application-session strategy;
- session lifetime and revocation;
- MFA enforcement policy;
- account recovery;
- detailed sign-out/session-expiry behaviour;
- role/permission/data-scope model;
- jurisdiction-specific identity requirements.

Specialist providers for KYC/AML, e-signature, messaging, banking/settlement and other integrations remain open unless separately decided.

## Governance rule

Where an older architecture document contains a technology-selection statement that conflicts with a later accepted ADR, the logical principle remains unless explicitly superseded, while the later ADR controls the implementation-choice detail. The original document should be updated during its next substantive revision; until then this reconciliation record prevents the older deferred-vendor wording from being interpreted as the current project decision.
