---
applyTo: "**/*.dart,**/*.kt,**/*.java"
---

# Security Rules

## FORBIDDEN PATTERNS
- Hardcoded API keys, passwords, tokens, or secrets in any file
- HTTP (non-TLS) calls to any financial or authentication endpoint
- Storing tokens, PII, or financial data in SharedPreferences or logs
- Local-only biometric authentication without server-side challenge-response
- Logout without server-side token revocation
- Unvalidated user input (amounts, memos, account IDs)

## MANDATORY PATTERNS
- All credentials via `${ENV_VAR}` or Vault
- All write operations in Spring services must be `@Transactional`
- All financial operations must be idempotent
- Input validation on BOTH client AND server
