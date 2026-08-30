# Permissions Matrix

Status: `ANALYSIS_IN_PROGRESS`

Legend: `C` = Confirmed, `I` = Inferred, `U` = Unknown.

| Capability | Prospective | Registered | Eligible | Portfolio | Opp Admin | Access Admin | Compliance | Ops Support | Mgmt |
|---|---|---|---|---|---|---|---|---|---|
| View public content | C | C | C | C | C | C | C | C | C |
| Sign in / session establish | U | I | I | I | I | I | I | I | I |
| Browse opportunities | U | I | C | C | I | I | I | I | I |
| View opportunity detail | U | I | I | I | I | I | I | I | I |
| Request NDA / DD access | U | I | I | I | I | I | I | I | U |
| Submit EOI/commitment | U | U | I | I | U | U | U | U | U |
| View pending investments | U | I | I | C | U | U | U | I | U |
| View holdings/performance | U | U | I | C | U | U | U | U | I |
| Manage opportunities | U | U | U | U | I | U | I | I | U |
| Manage roles/permissions | U | U | U | U | U | I | I | U | U |
| Review audit evidence | U | U | U | U | U | I | I | I | I |

## Constraints

1. This matrix is not an approval artifact for production permissions.
2. Negative-path tests (unauthorized/insufficient scope) are mandatory before status promotion.
