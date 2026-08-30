# Capability Map

Status: `ANALYSIS_IN_PROGRESS`

```mermaid
flowchart TB
  subgraph Investor_Facing
    PUB[Public Experience]
    IAM[Identity and Access]
    OPP[Opportunity Discovery]
    DD[Due Diligence Access]
    INV[Expression of Interest / Commitment]
    PORT[Portfolio Views]
    DOC[Reports and Tax Documents]
    NEWS[News and Events]
    PROFILE[Profile and Preferences]
  end

  subgraph Operational
    ONB[Onboarding and Eligibility]
    SET[Funding and Settlement]
    NOTIFY[Notifications]
    OPS[Operations and Support]
    ADMIN[Administration]
    AUD[Audit and Compliance]
    REPORT[Management Reporting]
  end

  subgraph External
    INT[Integration Adapters]
  end

  IAM --> OPP
  OPP --> DD
  DD --> INV
  INV --> SET
  SET --> PORT
  ONB --> IAM
  NOTIFY --> Investor_Facing
  AUD --> Operational
  REPORT --> Operational
  INT --> Operational
```

## Domain dependency notes

- IAM and AUD are cross-cutting prerequisites for sensitive workflows.
- SET and INT remain blocked by unresolved legal and provider evidence.
- Foundation and first-slice sequencing is governed by docs/09-delivery/foundation-slice-a-governance-reconciliation.md.
