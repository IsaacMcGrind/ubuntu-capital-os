# Azure Architecture for ubuntu-capital-platform

## Current Project State
- Frontend is a React + Vite single-page application.
- UI routes and screens exist for key business flows (authentication, onboarding, opportunities, portfolio, reports, notifications).
- Backend services and persistent data layer are not yet implemented.

## Scope
Defining the **Azure cloud architecture** for the Ubuntu Capital platform.

Determine how the platform can be hosted, secured, operated, monitored, deployed, and scaled within Microsoft Azure while keeping the initial cloud footprint simple and cost-effective.

This is **not the authoritative full-system architecture for the Ubuntu Capital platform**.

### This md file Covers
- Frontend cloud hosting.
- Backend cloud compute.
- Cloud identity and authentication infrastructure.
- Managed database infrastructure.
- Object and document storage.
- Secrets and configuration management.
- Service-to-service authentication.
- Observability and application monitoring.
- Azure resource organisation.
- Environment strategy.
- CI/CD deployment into Azure.
- Cost control and FinOps.
- Cloud scalability and resilience.
- Future Azure infrastructure capabilities.

### This md file Does Not Define
- The complete platform architecture.
- Application/domain architecture.
- Complete business workflow architecture.
- Detailed domain boundaries.
- The authoritative data model.
- Complete API design.
- Complete integration architecture.
- Business rules.
- Investment lifecycle design.
- Full security architecture beyond the Azure cloud layer.
- Other system-wide architecture decisions owned by the broader platform architecture.

Where the Azure architecture depends on one of these decisions, the cloud implementation should align with the authoritative platform architecture rather than redefine it.

The Azure architecture acts as the **cloud infrastructure and platform-services layer** supporting the wider Ubuntu Capital architecture.

## Why Azure Is a Good Fit
- Fast delivery with managed services and low ops overhead.
- Strong built-in security model (identity, secrets management, HTTPS by default).
- Easy path from MVP to scale without early overengineering.
- Cost-efficient entry point with serverless/consumption tiers.
- Intentional Azure skills development: the cloud workstream provides a real, production-oriented environment for expanding practical Azure capability while solving genuine platform requirements

## Azure Cloud Skills Development Objective

This Azure architecture workstream will be used deliberately to help **HerLogic Solutions strengthen and expand its practical Microsoft Azure capability**.

The objective is to learn through the implementation of real cloud requirements rather than through isolated demonstrations. The learning objective applies specifically to the **Azure cloud layer** and must not replace or override the broader platform architecture.

### Existing Experience

HerLogic Solutions already has practical exposure to:
- CI/CD pipelines and automated deployments.
- Azure Web Apps / Azure App Service.
- Azure Functions.
- Basic Microsoft Entra concepts and authentication.

### Skills to Strengthen Through This Project

This workstream can progressively deepen practical experience in:
- Azure Static Web Apps.
- Microsoft Entra External ID.
- Token-based authentication and API protection.
- Roles, scopes, authorization, and MFA concepts.
- Azure SQL Database.
- Azure Blob Storage.
- Azure Key Vault.
- Managed Identities.
- Application Insights.
- Azure Monitor.
- Azure Cost Management and FinOps.
- Azure resource organisation and environment management.
- Cloud security and least-privilege access.
- Serverless architecture.
- Azure networking concepts as required.
- Azure Service Bus when asynchronous workloads justify it.
- API Management when integration or governance requirements justify it.
- Azure Front Door and resilience patterns when scale or business continuity requirements justify them.

### Learn Through Real Platform Requirements

| Platform Cloud Requirement | Azure Learning Opportunity |
| Host the React frontend | Azure Static Web Apps |
| Deploy backend APIs | Azure Functions |
| Authenticate platform users | Microsoft Entra External ID |
| Protect APIs | Entra tokens, roles, scopes, authorization |
| Provide managed relational data infrastructure | Azure SQL Database |
| Store documents and reports | Azure Blob Storage |
| Protect secrets and configuration | Azure Key Vault |
| Authenticate Azure resources | Managed Identity |
| Investigate application failures | Application Insights |
| Monitor availability and platform health | Azure Monitor |
| Control cloud spend | Azure Cost Management |
| Automate releases | CI/CD |

### Guiding Principle

Use real Ubuntu Capital cloud requirements to deepen HerLogic Solutions' Azure capability without introducing unnecessary infrastructure purely for learning purposes.

The cloud architecture should remain cost-effective, maintainable, secure, production-oriented, and aligned with the authoritative wider platform architecture.

## Recommended Simple Cloud Architecture

| Component | Purpose | Suggested Tier/SKU |
|---|---|---|
| Azure Static Web Apps | Host the React frontend with global delivery and SSL | Start with the lowest suitable/free tier where practical |
| Microsoft Entra External ID | Customer sign-up, sign-in, MFA, token-based auth | Pay-as-you-go / low-volume starting configuration |
| Azure Functions | Backend API compute defined by the platform architecture | Consumption-based plan |
| Azure SQL Database | Managed relational data infrastructure where required by the platform data architecture | Serverless / lowest suitable configuration |
| Azure Blob Storage | Documents and report file storage | Hot tier (as needed) |
| Azure Key Vault | Secrets and configuration protection | Standard |
| Application Insights + Azure Monitor | Telemetry, tracing, alerts, health monitoring | Basic/minimal setup |

## Architecture Flow (High-Level)
At the Azure cloud layer, the expected high-level flow would be:

1. User accesses the frontend hosted on Azure Static Web Apps.
2. User authenticates via Entra External ID.
3. Frontend calls protected backend APIs hosted on Azure compute being Azure Functions, in accordance with the platform architecture.
4. Backend services access the managed relational data platform where required.
5. Backend services issue secure upload/download access for Blob Storage when needed.

## Feature to Azure Service Mapping

The following mapping describes **cloud-service responsibilities only**.

- Login, signup, MFA: Entra External ID + token validation in APIs.
- Application APIs: Azure Functions.
- Relational business data: Azure SQL where the wider data architecture determines relational persistence is appropriate.
- Notifications: Start with the simplest platform-defined implementation; Azure Communication Services or asynchronous services may be introduced later where requirements justify them.
- Document/report handling: Blob Storage with short-lived signed access generated by the backend where appropriate.
- Secrets/configuration: Azure Key Vault.
- Monitoring and observability: Application Insights + Azure Monitor.

## Keep It Non-Complex: Phased Delivery
### Phase 1 (MVP / Learning Foundation)
- Azure Static Web Apps.
- Azure Functions where suitable for the platform-defined backend components.
- Azure SQL Database where required by the authoritative data architecture.
- Entra External ID.
- Application Insights.
- Azure Key Vault where secrets/configuration require central protection.
- Azure Cost Management budgets and alerts.

The objective in Phase 1 is to use the **smallest practical Azure footprint** while giving HerLogic Solutions hands-on experience across hosting, serverless compute, identity, managed data, security, observability, deployment, and cost management.

Other phases will identified on a later stage.

## Cost-Control Baseline
- Start with free, consumption-based, serverless, or the lowest suitable Azure tiers where practical.
- Avoid always-on or premium services during the early stage unless a real requirement justifies them.
- Enable budgets and cost alerts in Azure Cost Management from the beginning.
- Keep telemetry volume and retention intentionally controlled.
- Keep development resources materially smaller than production resources.
- Delay Service Bus, Redis, API Management, Front Door, multi-region deployment, and other advanced services until evidence justifies them.
- Scale only when usage, performance, resilience, compliance, or business requirements justify upgrades.

## Decision Summary

For this cloud workstream, the simplest effective Azure architecture is expected to begin with:
- Static Web Apps for frontend hosting.
- Azure Functions for backend services.
- Azure SQL for managed relational data where required.
- Entra External ID for customer identity.
- Blob Storage for documents.
- Key Vault for cloud security.
- Application Insights + Azure Monitor for operations.
- Azure Cost Management for cost governance.

This gives the project a clean MVP cloud path and a low-friction scale path later, while maintaining a clear boundary between the Azure cloud architecture and the broader Ubuntu Capital platform architecture.

It also gives **HerLogic Solutions a structured, real-world Azure upskilling path**, building from existing experience with CI/CD, Azure Web Apps, Azure Functions, and basic Entra knowledge toward stronger capability in Azure identity, data, storage, observability, security, FinOps, networking, integration, and resilience.
