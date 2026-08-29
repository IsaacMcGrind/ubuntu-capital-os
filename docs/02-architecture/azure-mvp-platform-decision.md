# Ubuntu Capital OS — Azure MVP Platform Decision

**Decision ID:** ARCH-ADR-001  
**Status:** CONFIRMED — project-owner direction  
**Decision date:** 2026-08-29  
**Scope:** MVP cloud hosting and platform-services layer  
**Does not replace:** the technology-neutral logical architecture, business-domain architecture, legal model, settlement model, or use-case evidence gates.

## Decision

Ubuntu Capital will use Microsoft Azure as the target cloud platform for the MVP cloud workstream.

The approved starting service set is:

| Platform concern | MVP target |
|---|---|
| React/Vite frontend hosting | Azure Static Web Apps |
| Customer identity and authentication | Microsoft Entra External ID |
| Backend/API compute | Azure Functions |
| Relational persistence where required by the platform data model | Azure SQL Database |
| Documents and generated files | Azure Blob Storage |
| Secrets/configuration protection | Azure Key Vault |
| Azure-to-Azure service identity | Managed Identity where supported |
| Application telemetry | Application Insights |
| Platform monitoring and alerts | Azure Monitor |
| Cost governance | Azure Cost Management budgets and alerts |
| Build/deployment automation | Existing CI/CD capability using GitHub Actions or Azure DevOps as delivery requires |

## Evidence basis

This decision reconciles:

- `contractors/HerLogicSolutions/azure-architecture.md`;
- `contractors/HerLogicSolutions/azure-mvp-cost-breakdown.md`;
- the technology-neutral logical boundary in `docs/02-architecture/high-level-logical-architecture-v0.1.md`;
- the priority architecture map in `docs/02-architecture/priority-use-case-architecture-map.md`;
- project-owner direction on 2026-08-29 that the infrastructure documented in the repository is the chosen implementation direction.

## What this decision changes

The repository no longer needs to treat the MVP cloud provider and core Azure platform-service categories as open implementation choices.

This converts the following from architecture-option analysis into delivery work:

- provision and configure the Azure resource baseline;
- connect the React/Vite frontend to Azure Static Web Apps;
- implement Entra External ID integration for UC-IAM-001/002/003;
- implement protected Azure Functions APIs;
- introduce Azure SQL persistence only where the authoritative data model requires relational storage;
- use Blob Storage for documents rather than storing document binaries in SQL;
- use Key Vault and Managed Identity for secrets/service authentication;
- instrument Application Insights and Azure Monitor;
- establish budgets/alerts before material consumption-based usage begins.

## What this decision does not prove

This architecture decision is **not implementation evidence**.

It does not prove that any Azure resource currently exists, is configured securely, is deployed, or is integrated with the current frontend implementation.

It does not change any use case to `COMPLETE`, `READY_FOR_E2E_TEST`, or `READY_FOR_ACCEPTANCE` without objective implementation and E2E evidence.

## Relationship to the logical architecture

The existing HLA remains valid because it intentionally separates logical capability ownership from deployment technology.

```text
Logical capability ownership
        |
        v
Ubuntu Capital application/domain architecture
        |
        v
Azure MVP platform-services implementation
        |
        +-- Static Web Apps
        +-- Entra External ID
        +-- Azure Functions
        +-- Azure SQL
        +-- Blob Storage
        +-- Key Vault / Managed Identity
        +-- Application Insights / Azure Monitor
```

The Azure layer implements infrastructure responsibilities. It must not become the authoritative owner of business facts such as eligibility, opportunity state, NDA state, investment state, settlement state, or holdings.

## Cost and complexity constraints

The MVP should remain consumption-first and low-cost:

- free/lowest suitable tiers where practical;
- no speculative premium capacity;
- one managed relational database initially where appropriate;
- no AKS, dedicated VMs, Redis, Service Bus, API Management, Front Door, premium networking, or multi-region topology until a measured requirement justifies them;
- controlled telemetry ingestion/retention;
- Azure budgets and alerts from the beginning;
- additional environments only when the delivery process requires them.

The cost target remains **as close to R0 as practical initially**, with spend increasing only when real usage, production, security, performance, resilience, or compliance requirements justify it.

## Implementation gates

The Azure foundation is considered `COMPONENT_COMPLETE` only when evidence exists for all applicable items below:

1. Azure resource inventory and ownership are recorded.
2. Environment/resource naming and access model are documented.
3. Frontend deploys successfully to Static Web Apps.
4. Entra External ID tenant/application configuration is evidenced.
5. Protected API requests are enforced server-side.
6. Azure Functions deploy and execute with correlation/telemetry.
7. Azure SQL schema/migration evidence exists where used.
8. Blob access is mediated by authorised backend logic where documents are involved.
9. Key Vault/Managed Identity removes secrets from client code and repository configuration.
10. Application Insights/Monitor show traceable request/failure telemetry.
11. Budget and cost alerts are configured.
12. CI/CD produces repeatable deployment evidence.

The Azure foundation cannot be treated as `COMPLETE` until E2E evidence proves the relevant business use case through the deployed environment.

## Remaining architecture decisions

Azure selection does **not** resolve these critical questions:

- KYC/AML provider and decision model;
- e-signature/NDA provider and legal evidence lifecycle;
- messaging provider/channel requirements;
- settlement/banking/custody model;
- investor eligibility/accreditation policy;
- investment legal meaning;
- ownership/SPV/nominee/fund model;
- portfolio valuation/performance rules;
- internal RBAC/segregation-of-duties model;
- retention/privacy requirements;
- production resilience/RTO/RPO requirements.

## Delivery consequence

Architecture readiness has materially improved because the cloud implementation path is now bounded. Delivery readiness has **not** advanced automatically: the current implementation evidence still shows a predominantly front-end prototype, with backend, persistence, access enforcement, integrations, audit, and E2E evidence incomplete or absent for most business use cases.
