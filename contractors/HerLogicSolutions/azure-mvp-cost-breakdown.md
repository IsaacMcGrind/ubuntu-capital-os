 # Ubuntu Capital MVP — Azure Cost Breakdown

## Purpose

This document defines the expected Azure cost profile for the **Ubuntu Capital MVP**.

The objective is to keep the initial cloud architecture as cost-effective as possible while still using real Microsoft Azure services for hosting, identity, backend compute, data, storage, security, monitoring, and CI/CD.

This document does **not** assume a fixed number of MVP users. Costs should instead be managed according to actual platform usage, data volume, authentication activity, API execution, telemetry, storage, and deployment activity.

> **Important:** Azure pricing, free grants, regional availability, and service limits can change.

---

# Cost Strategy

The MVP should follow these principles:

1. Use free Azure tiers and allowances where eligible.
2. Prefer consumption-based services over always-on infrastructure.
3. Start with the smallest practical resource configuration.
4. Avoid premium services unless there is a real requirement.
5. Keep development environments smaller than production.
6. Set budgets and alerts from the beginning.
7. Measure actual usage before scaling.
8. Add architectural complexity only when justified by real requirements.

The MVP cost target should therefore be:

> **As close to R0 as practical at the start, with spend increasing only when real usage or production requirements justify it.**

---

# Service-by-Service Cost Breakdown

| Azure Component | Recommended MVP Configuration | Expected MVP Cost Position | Main Cost Driver |
|---|---|---:|---|
| Azure Static Web Apps | Free Plan initially | **R0** | Upgrade only if Standard features are required |
| CI/CD | GitHub Actions / Azure DevOps within free allowance | **R0 to low** | Build minutes and pipeline frequency |
| Microsoft Entra External ID | Core External ID capabilities | **R0 at low-to-moderate MVP usage** | Monthly active users and premium features |
| Azure Functions | Consumption-based plan | **R0 to low** | Execution count, execution duration, memory |
| Azure SQL Database | Free offer or smallest suitable serverless configuration | **R0 to moderate** | Compute, storage, query activity |
| Azure Blob Storage | Standard LRS, Hot tier as needed | **Very low** | File volume, transactions, downloads |
| Azure Key Vault | Standard | **Very low** | Secret/key operations |
| Application Insights | Minimal telemetry | **R0 to low** | Data ingestion and retention |
| Azure Monitor | Basic monitoring and alerts | **R0 to low** | Logs and metrics volume |
| Azure Cost Management | Budgets and alerts | **R0** | No direct cost for basic cost governance |

---

# 1. Azure Static Web Apps

## Purpose

Hosts the React + Vite frontend.

## Recommended MVP configuration

- Free Plan.
- Built-in HTTPS/TLS.
- GitHub or Azure DevOps deployment integration.
- Custom domain only when required.
- Minimal staging environments.

## Expected MVP cost

**Target: R0/month**

The Free Plan should be sufficient during the early MVP stage unless the platform requires features only available on Standard.

## Potential cost triggers

Upgrade may become necessary if the platform requires:

- higher quotas;
- production SLA;
- advanced networking;
- private endpoints;
- additional staging capacity;
- advanced authentication features.

---

# 2. CI/CD

## Purpose

Automates build, testing, and deployment of the frontend and backend.

Example:

```text
Developer
   │
   ▼
Git push / Pull Request
   │
   ▼
Build
   │
   ├── Tests
   │
   ▼
Deploy Frontend
   │
   ▼
Deploy Azure Functions
```

## Recommended MVP configuration

- Use existing GitHub or Azure DevOps integration.
- Keep workflows lightweight.
- Trigger deployments only when necessary.
- Avoid unnecessary repeated build jobs.

## Expected MVP cost

**Target: R0 to very low**

Cost depends mainly on build minutes and runner usage.

---

# 3. Microsoft Entra External ID

## Purpose

Handles platform identity and authentication.

Potential MVP capabilities:

- sign-up;
- sign-in;
- token-based authentication;
- protected APIs;
- roles and scopes;
- MFA where required.

## Expected MVP cost

**Target: R0 at normal MVP scale**

External ID is designed to support substantial user volumes before identity cost becomes a meaningful concern.

## Potential cost triggers

- very large monthly active user volume;
- SMS-based MFA;
- premium identity capabilities;
- advanced identity governance.

---

# 4. Azure Functions

## Purpose

Provides serverless backend compute.

Typical responsibilities may include:

- API endpoints;
- authentication/token validation;
- platform business logic;
- database operations;
- document access coordination;
- background processing where appropriate.

## Recommended MVP configuration

- Consumption-based plan.
- No Premium plan.
- No always-on capacity unless needed.
- Keep functions short and efficient.

## Expected MVP cost

**Target: R0 to low**

For an early MVP, Azure Functions should generally remain inexpensive because charges are based on actual execution.

## Main cost drivers

- number of executions;
- memory allocated;
- execution duration;
- always-ready capacity;
- premium hosting.

---

# 5. Azure SQL Database

## Purpose

Provides managed relational data storage where required by the wider platform architecture.

## Recommended MVP configuration

Use:

- the Azure SQL free offer where eligible; or
- the smallest suitable serverless configuration.

Avoid multiple databases unless the broader architecture genuinely requires them.

## Expected MVP cost

**Target: R0 to moderate**

Azure SQL is likely to become one of the biggest paid Azure components as the platform grows.

## Main cost drivers

- compute;
- database size;
- query volume;
- reporting workload;
- concurrent usage;
- indexes;
- backup/storage requirements.

## Cost-control principles

- Use one database initially where appropriate.
- Avoid storing large documents in SQL.
- Store files in Blob Storage.
- Optimise queries before increasing compute.
- Keep indexes deliberate.
- Avoid using SQL as a telemetry/log store.
- Scale only when measured workload justifies it.

---

# 6. Azure Blob Storage

## Purpose

Stores platform files such as:

- reports;
- PDFs;
- uploaded documents;
- statements;
- images;
- generated files.

## Recommended MVP configuration

- Standard storage.
- LRS replication initially.
- Hot tier for regularly accessed files.
- Keep storage volumes small.

## Expected MVP cost

**Target: very low**

Blob Storage is generally one of the cheapest components in this architecture at MVP scale.

## Main cost drivers

- total storage volume;
- read/write operations;
- file downloads;
- outbound data transfer;
- replication option.

---

# 7. Azure Key Vault

## Purpose

Stores sensitive secrets and configuration.

Examples:

- external API keys;
- certificates;
- credentials;
- third-party secrets.

## Recommended MVP configuration

- Standard tier.
- Use Managed Identity wherever possible.
- Avoid excessive secret retrieval.

## Expected MVP cost

**Target: near R0 / very low**

Key Vault is a metered service, but at MVP scale operations should remain minimal.

## Cost-control principle

Prefer:

```text
Azure Function
      │
 Managed Identity
      │
      ▼
Azure SQL
```

over repeatedly retrieving credentials from Key Vault.

---

# Services to Avoid During the Initial MVP

Do not introduce these services unless a real requirement exists:

❌ Azure Kubernetes Service
❌ Dedicated Virtual Machines
❌ Premium Azure Functions
❌ Large App Service Plans
❌ Azure Front Door
❌ API Management
❌ Redis
❌ Service Bus
❌ Multi-region deployments
❌ Premium networking
❌ Geo-redundant storage
❌ Private endpoints everywhere
❌ Large always-on SQL capacity
```

These can be added later when scale, integration, performance, compliance, resilience, or governance requirements justify them.

---

# Environment Cost Strategy

Do not start with a full enterprise environment estate unless necessary.

Avoid initially:

```
DEV
QA
SIT
UAT
STAGING
PRE-PROD
PRODUCTION
```

A lean MVP environment model can be:

```
LOCAL DEVELOPMENT
        │
        ▼
AZURE DEV / MVP
        │
        ▼
PRODUCTION
```

Development resources should be smaller than production resources.

Additional environments should be added only when the delivery process requires them.

---

# MVP Monthly Cost Ranges

The following ranges are practical planning bands rather than guaranteed Azure invoices.

| MVP Stage | Expected Azure Cost Position |
|---|---:|
| Local development | **R0** |
| Very early hosted MVP | **R0 – R200/month** |
| Active MVP with regular testing and usage | **R200 – R1,000/month** |
| Growing beta / pre-production platform | **R1,000+ depending on workload** |

The primary variables will usually be:

- Azure SQL compute;
- monitoring/log ingestion;
- file storage and downloads;
- API usage;
- authentication volume;
- additional environments;
- premium networking or resilience services.

---

# Likely Cost Growth Order

As the MVP grows, Azure costs will typically increase in roughly this order:

```text
1. Azure SQL
       │
       ▼
2. Monitoring / telemetry
       │
       ▼
3. Backend compute
       │
       ▼
4. Storage / file transfer
       │
       ▼
5. Identity at larger scale
       │
       ▼
6. Advanced networking / resilience
```

This means Azure SQL and observability should receive the closest cost monitoring from the start.

---

# MVP Cost Governance Rules

1. **Free first**
   - Use eligible free Azure services and allowances.

2. **Consumption first**
   - Prefer usage-based billing over dedicated capacity.

3. **Start small**
   - Deploy the lowest practical SKU.

4. **One requirement, one justification**
   - Every paid Azure resource should solve a real problem.

5. **No speculative scale**
   - Do not provision for user volumes that do not yet exist.

6. **Measure before upgrading**
   - Use metrics to justify larger compute or storage.

7. **Keep files out of SQL**
   - Use Blob Storage for documents.

8. **Prefer Managed Identity**
   - Reduce stored secrets and Key Vault calls.

9. **Control telemetry**
   - Monitoring must not become a hidden cost driver.

10. **Review costs regularly**
    - Inspect Azure Cost Management as part of normal operations.

11. **Earn complexity**
    - Add Service Bus, Redis, API Management, Front Door, multi-region, and similar services only when required.

---

# Recommended MVP Cost Position

For the Ubuntu Capital MVP, the architecture should not be designed around a fixed user count.

Instead, it should be designed around:

```
LOW INITIAL CLOUD FOOTPRINT
          │
          ▼
FREE / CONSUMPTION SERVICES
          │
          ▼
REAL USAGE METRICS
          │
          ▼
RIGHT-SIZING
          │
          ▼
CONTROLLED SCALE
```

The goal is:

> **Keep the initial Azure footprint at R0 or very low cost where practical, then allow actual platform usage and production requirements to determine when additional spend is justified.**

---

# Final MVP Cost Summary

| Component | Initial MVP Position |
|---|---|
| Static Web Apps | Free |
| CI/CD | Free / low |
| Entra External ID | Free at normal MVP scale |
| Azure Functions | Free / low through consumption |
| Azure SQL | Free offer or smallest serverless configuration |
| Blob Storage | Very low |
| Key Vault | Very low |
| Application Insights | Free / low |
| Azure Monitor | Free / low |
| Azure Cost Management | Free |

A realistic cost-management approach is therefore:

> **R0 where possible, very low spend at initial MVP stage, and controlled increases only when usage, reliability, security, performance, or business requirements justify them.**
