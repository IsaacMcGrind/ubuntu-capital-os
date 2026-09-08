# Architecture Exception Disposition

**Status:** `PENDING_APPROVAL`  
**Exception ID:** AE-001  
**Scope:** Foundation Slice A and first business slice  
**Policy:** This exception is temporary and must be closed before WP-AZ-003 / WP-AZ-004 and business-slice acceptance.

## 1. Exception summary

The current repository uses client-side route gating and browser localStorage for identity/session state and expression-of-interest persistence. This is acceptable only as a prototype or design-time behavior and must not be treated as production authentication, authorisation, or persistence evidence.

Relevant evidence:

- [src/App.tsx](src/App.tsx#L35-L66)
- [src/lib/session.ts](src/lib/session.ts#L1-L42)
- [src/lib/eoi.ts](src/lib/eoi.ts#L1-L43)
- [src/pages/Login.tsx](src/pages/Login.tsx#L11-L67)
- [src/pages/DealDetail.tsx](src/pages/DealDetail.tsx#L29-L60)

## 2. Exception reason

This is a known temporary architecture exception because the project is still in early Foundation and business-slice readiness work. The repository does not yet provide the required backend identity enforcement, server-side auth, Azure SQL persistence, Key Vault, or managed identities that the attached Azure delivery plan requires before the first investor vertical slice can be accepted.

## 3. Temporary disposition

The exception is allowed only under the following conditions:

1. It remains clearly documented as a design-time limitation and not a production control.
2. It is not used as evidence that the investor auth model is complete.
3. It must be superseded by Entra External ID + Azure Functions backend enforcement before business-slice completion.
4. Any deployment or acceptance evidence must explicitly state that the protection is provisional and not final.

## 4. Closure requirement

This exception closes when:

- WP-AZ-003 has objective evidence for the Entra External ID foundation;
- WP-AZ-004 proves unauthenticated requests are denied server-side;
- WP-AZ-005 proves persistence is in Azure SQL or approved equivalent backend storage;
- WP-AZ-006 proves Key Vault and managed identity are active; and
- the first business slice has complete acceptance evidence.

## 5. Current business-slice control

The business slice remains blocked until the Foundation evidence gates are satisfied. This exception does not authorize any production protected workflow, identity claim, or EOI persistence beyond local prototype behavior.
