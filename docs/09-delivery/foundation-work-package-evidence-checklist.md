# Foundation Work Package Evidence Checklist

Status: APPROVED_TO_START

This checklist defines the evidence required before each Foundation work package can be marked complete. Foundation work may begin under the approved-to-start gate, but each work package must still produce objective evidence before it is accepted.

## Rule of progression

- A work package is not complete because it is deployed; it is complete only when the required evidence is recorded.
- The business slice remains blocked until the Foundation evidence gate for the relevant work packages is satisfied.
- Temporary architecture exceptions remain tracked and are not treated as production evidence.
- Evidence must be exportable, reviewable, and linked to the relevant resource, tenant, subscription, or branch baseline.

## Summary table

| Work package | Scope | Evidence gate | Status before acceptance |
|---|---|---|---|
| WP-AZ-001 | Azure baseline | Required evidence captured and reviewed | Not complete without exports and approvals |
| WP-AZ-002 | Azure Static Web Apps | Deployment + smoke test + URL + revision evidence | Not complete without live deployment evidence |
| WP-AZ-003 | Microsoft Entra External ID | Auth flow + protected route validation + no credential leakage | Not complete without identity proof |
| WP-AZ-004 | Azure Functions API | Server-side auth + telemetry + health + denial checks | Not complete without API proof |
| WP-AZ-005 | Azure SQL | Secure connectivity + read/write proof + migrations | Not complete without persistence evidence |
| WP-AZ-006 | Key Vault + managed identity | Secret access + least privilege + runtime access | Not complete without secret-handling proof |
| WP-AZ-007 | Application Insights + Azure Monitor | Telemetry + correlation + alerts | Not complete without observability proof |
| WP-AZ-008 | Reproducible infrastructure + CI/CD | Provisioning evidence + workflow evidence + traceability | Not complete without repeatability evidence |

---

## WP-AZ-001 — Azure baseline

### Required evidence

- [ ] Approved subscription, tenant, region, and resource-group model recorded
- [ ] Resource group created in the approved environment
- [ ] Naming convention and mandatory tags recorded and applied
- [ ] Azure RBAC assignments exported for deployment owners and operators
- [ ] Budget object exported with monthly reset period and R250 amount
- [ ] Cost alert configuration exported with threshold records
- [ ] Deployment identity model recorded and approved
- [ ] Secret exposure scan result recorded and retained
- [ ] Resource inventory export retained as evidence
- [ ] Gate record updated to show WP-AZ-001 is complete

### Completion rule

This package is complete only after the exported evidence is reviewed and reconciled against the approved baseline model.

---

## WP-AZ-002 — Azure Static Web Apps

### Required evidence

- [ ] Source repository branch and commit recorded for deployment
- [ ] Clean production build succeeded
- [ ] Static Web App deployed successfully in Azure
- [ ] Live URL recorded and reachable
- [ ] Basic smoke test completed for landing page and core app paths
- [ ] Deployment revision or release identifier recorded
- [ ] Deployment logs retained as evidence
- [ ] Failure path defined and tested if the app is not reachable

### Completion rule

This package is complete only when the deployed frontend is reachable and the deployment can be traced to a known revision.

---

## WP-AZ-003 — Microsoft Entra External ID

### Required evidence

- [ ] External ID tenant or customer directory model documented
- [ ] User sign-in flow succeeds for a valid external user
- [ ] Invalid or unauthenticated access fails safely
- [ ] Redirects, tokens, and callback config recorded without secret exposure
- [ ] No production credentials embedded in frontend code
- [ ] Protected routes are enforced by backend or identity platform, not only client logic
- [ ] Sign-out and session expiry behavior recorded
- [ ] Test result documented for success and failure paths

### Completion rule

This package is complete only when a real authentication flow works and the failure path is safely denied.

---

## WP-AZ-004 — Azure Functions API foundation

### Required evidence

- [ ] Function App created and reachable
- [ ] Health endpoint verified
- [ ] Unauthenticated request to protected endpoint denied with safe error response
- [ ] Authenticated request resolves caller identity on the server side
- [ ] Role or claim checks recorded for protected actions
- [ ] Runtime logs retained for normal and failed requests
- [ ] App Insights or equivalent correlation identifiers recorded
- [ ] Secret or API keys are not stored in code or client-side assets

### Completion rule

This package is complete only when the API is protected by server-side validation and its runtime behavior is observable.

---

## WP-AZ-005 — Azure SQL persistence

### Required evidence

- [ ] SQL server and database created in the approved environment
- [ ] Private or least-privilege connectivity approach documented
- [ ] Database migration or schema creation result recorded
- [ ] Write/read operation succeeds for a test record
- [ ] Failure-path handling documented for database errors
- [ ] Access via managed identity or secure service principal is preferred over embedded credentials
- [ ] Database tags and ownership metadata recorded
- [ ] Audit or query log evidence retained for the test data path

### Completion rule

This package is complete only when the application can persist and retrieve data securely and the access pattern is documented.

---

## WP-AZ-006 — Key Vault and managed identity

### Required evidence

- [ ] Key Vault created and scoped to the correct workload
- [ ] Secrets stored in Key Vault instead of app code or config files
- [ ] Managed identity or workload identity assigned and documented
- [ ] Function App or app service can retrieve secrets without embedded credentials
- [ ] Least-privilege RBAC assignments exported
- [ ] Rotation or renewal ownership recorded
- [ ] Secret access failure path tested and documented
- [ ] Key Vault access logs retained or linked

### Completion rule

This package is complete only when secrets are handled through Key Vault and the runtime identity can access them without hardcoded secrets.

---

## WP-AZ-007 — Application Insights and Azure Monitor

### Required evidence

- [ ] Application Insights resource created and connected to the app
- [ ] Request telemetry captured from a test flow
- [ ] Dependency telemetry captured for database or API interactions
- [ ] Exception telemetry captured from a deliberately triggered failure path
- [ ] Availability or alert configuration documented
- [ ] Correlation identifiers preserved across calls
- [ ] Logs or telemetry exports checked for secret leakage
- [ ] Alert or diagnostic rule evidence retained

### Completion rule

This package is complete only when the app emits telemetry across normal and failure conditions and the data is safe to review.

---

## WP-AZ-008 — Reproducible infrastructure and CI/CD evidence

### Required evidence

- [ ] Infrastructure as code or equivalent version-controlled provisioning definition exists
- [ ] Deployment workflow or pipeline definition exists and is version-controlled
- [ ] Clean provision or reconcile process succeeds in the target environment
- [ ] Build and deployment workflow logs retained
- [ ] Reproducibility test recorded for environment recreation or redeploy
- [ ] Failed deployment validation is clearly defined and enforced
- [ ] Infrastructure and app revision identifiers are traceable to evidence
- [ ] Access review and environment ownership recorded

### Completion rule

This package is complete only when the environment can be reproduced or redeployed from version-controlled definitions with objective evidence.

---

## Evidence package summary for acceptance

Before the business slice is released, the following must exist as a complete set:

- [ ] Foundation gate approval recorded
- [ ] Work package evidence captured for WP-AZ-001 to WP-AZ-008
- [ ] Evidence register updated with the final result for each package
- [ ] Temporary architecture exceptions tracked and scheduled for closure
- [ ] Business slice remains blocked until Foundation evidence is accepted

## Final gate note

The Foundation gate authorises implementation to begin, but it does not authorise business-slice completion. Business-slice completion is allowed only after the Foundation evidence requirements above are satisfied and the evidence is reviewed against the approved Azure baseline.
