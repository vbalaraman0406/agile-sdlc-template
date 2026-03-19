---
name: security-enforcement
description: Banking-grade security enforcement rules. Always active. Prevents insecure code patterns in financial applications.
activation: always_on
---

# Security Enforcement Rules

These rules apply to ALL code changes in this project. No exceptions.

## FORBIDDEN PATTERNS
- Hardcoded API keys, passwords, tokens, or secrets in any file
- HTTP (non-TLS) calls to any financial or authentication endpoint
- Storing tokens, PII, or financial data in SharedPreferences or logs
- Local-only biometric authentication without server-side challenge-response
- Logout without server-side token revocation
- Unvalidated user input (amounts, memos, account IDs)
- Swagger endpoints with `permitAll()` in production profile
- Flat Docker bridge networks (services must be isolated)
- Kong admin API (:8001) exposed to containers or external network
- JWT validated only at Kong without Spring-side validation

## MANDATORY PATTERNS
- All credentials via `${ENV_VAR}` or Vault
- All write operations in Spring services must be `@Transactional`
- All financial operations must be idempotent
- All write operations must have structured audit logging
- Input validation on BOTH client AND server
- Rate limiting on login, token refresh, and payment endpoints
