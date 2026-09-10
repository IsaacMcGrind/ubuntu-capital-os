# WP-AZ-001 Azure Baseline Findings (Ubuntu Capital Platform)

Status date: 2026-09-03  
Repository: ubuntu-capital-platform  
Branch: feature/update_navigation_bar_size_and_UI_wording

## 1. Objective Alignment

WP-AZ-001 requires baseline Azure governance and evidence before it can be marked `COMPONENT_COMPLETE`:

- Resource inventory/export/CLI evidence
- Resource-group/environment model
- RBAC ownership evidence
- Naming/tagging evidence
- Azure Cost Management budget evidence
- Cost-alert evidence
- Deployment identity/service connection approach documented
- Secrets exposure check

## 2. Current Project Findings

### 2.1 Application and architecture state

- The repository is currently a frontend-only React + Vite application.
- There is no backend API implementation in this repo yet.
- There are no Infrastructure as Code files currently present (no Bicep/Terraform in this workspace).
- There are no CI workflow files currently present in this workspace.

### 2.2 Authentication and protected route behavior

- Route protection is currently client-side only via local session checks in app routing.
- Login currently creates a local session record, not an external identity session.

Code references:

- [src/App.tsx](src/App.tsx#L35)
- [src/lib/session.ts](src/lib/session.ts#L1)
- [src/lib/session.ts](src/lib/session.ts#L21)
- [src/lib/session.ts](src/lib/session.ts#L35)
- [src/pages/Login.tsx](src/pages/Login.tsx#L25)

### 2.3 EOI persistence behavior

- Expression of interest state is currently persisted in browser localStorage.

Code references:

- [src/lib/eoi.ts](src/lib/eoi.ts#L1)
- [src/lib/eoi.ts](src/lib/eoi.ts#L25)
- [src/lib/eoi.ts](src/lib/eoi.ts#L29)

### 2.4 Secrets and environment signals

- No `.env*` files were found in this workspace scan.
- No obvious hardcoded credential patterns were found in the inspected artifacts.
- `.gitignore` currently covers OS-level artifacts (macOS/Windows); it does not include dependency/build output ignores (e.g., `node_modules/`, `dist/`).

Code references:

- [.gitignore](.gitignore#L10)
- [.gitignore](.gitignore#L11)

## 3. Gap Analysis Against WP-AZ-001

The following are not yet implemented in this repo and must be produced as evidence artifacts:

1. Resource inventory/export/CLI outputs
2. Resource-group/environment baseline model (documented)
3. RBAC assignment evidence for ownership and deployment identity
4. Naming/tagging policy and proof of tag application
5. Cost Management budget object and thresholds
6. Cost-alert notification evidence
7. Deployment identity/service connection design record
8. Repeatable secrets exposure scan evidence

## 4. Required Deliverables for Completion

To close WP-AZ-001, produce and retain the following artifacts.

### 4.1 Documentation artifacts

- `docs/09-delivery/wp-az-001-baseline-model.md`
  - Subscription scope and region choice
  - Resource-group/environment model
  - Naming standard
  - Mandatory tags
  - RBAC matrix
  - Budget and alert policy
- `docs/09-delivery/wp-az-001-deployment-identity-approach.md`
  - Identity type (recommended: federated OIDC workload identity)
  - Scope/roles
  - Service connection boundaries
  - Secret handling approach

### 4.2 Evidence artifacts

Create folder: `evidence/wp-az-001/`

Required files (minimum):

- `resource-groups.json`
- `resources.json`
- `resource-summary-table.txt`
- `resource-tags.json`
- `rbac-rg-ucp-dev.json` (or equivalent RG scope)
- `budget-rg-ucp-dev.json` (or equivalent budget scope)
- `cost-alert-config.json` (or budget payload showing notification thresholds)
- `secrets-scan.txt`
- `gate-check.md` (start-gate confirmation note)

## 5. Suggested Baseline Azure Model (MVP)

This is a practical starting model for WP-AZ-001 only:

- Resource groups:
  - `rg-ucp-dev`
  - `rg-ucp-shared`
- Region:
  - `southafricanorth` (or approved target region)
- Tags (minimum):
  - `org=ubuntu-capital`
  - `workload=platform`
  - `environment=dev|shared`
  - `owner=<team-or-person>`
  - `costCenter=<code>`
  - `managedBy=iac`
  - `dataClass=internal`
- Deployment identity:
  - user-assigned managed identity or app registration with federated credential for CI/CD
- RBAC:
  - least privilege for deployment identity (typically Contributor at dev RG scope)
  - constrained human ownership assignments with evidence export

## 6. Implementation Steps (Execution Order)

1. Confirm governance start gate is satisfied per controlling delivery plan.
2. Create and approve baseline model document and naming/tagging policy.
3. Provision baseline resource groups with mandatory tags.
4. Create deployment identity and assign scoped RBAC roles.
5. Configure monthly budget and 50/80/100 alert thresholds.
6. Export inventory, RBAC, budget, and alert configuration evidence files.
7. Run and store secrets exposure scan evidence.
8. Reconcile checklist and mark WP-AZ-001 complete only after all evidence is present.

## 7. Example Azure CLI Command Set (Adapt Values)

```bash
az account show --output table

az group create --name rg-ucp-dev --location southafricanorth --tags org=ubuntu-capital workload=platform environment=dev managedBy=iac
az group create --name rg-ucp-shared --location southafricanorth --tags org=ubuntu-capital workload=platform environment=shared managedBy=iac

az identity create --name id-ucp-deploy-dev --resource-group rg-ucp-dev

az role assignment create --assignee <principalId-or-appId> --role Contributor --scope /subscriptions/<subscriptionId>/resourceGroups/rg-ucp-dev
az role assignment list --scope /subscriptions/<subscriptionId>/resourceGroups/rg-ucp-dev --output json > evidence/wp-az-001/rbac-rg-ucp-dev.json

az group list --output json > evidence/wp-az-001/resource-groups.json
az resource list --output json > evidence/wp-az-001/resources.json
az resource list --output table > evidence/wp-az-001/resource-summary-table.txt
az resource list --query "[].{name:name,resourceGroup:resourceGroup,tags:tags}" --output json > evidence/wp-az-001/resource-tags.json
```

Note: Budget/notification command syntax can vary across Azure CLI versions. Validate with `az consumption budget --help` in your environment and export the resulting budget object JSON as evidence.

## 8. Important Constraints

- WP-AZ-001 completion does not imply IAM use-case completion.
- WP-AZ-001 completion does not authorize WP-AZ-009 through WP-AZ-012 by itself.
- Evidence must be objective, exportable, and traceable to subscription/RG scope.

## 9. Conclusion

The project has a strong frontend baseline, but WP-AZ-001 is currently missing all Azure governance/evidence artifacts required for `COMPONENT_COMPLETE`. The fastest path is to complete the baseline model docs, provision minimal Azure baseline resources, and capture evidence exports into `evidence/wp-az-001/`.
