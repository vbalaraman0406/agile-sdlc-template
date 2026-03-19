# Security Review — Phase [N]

## OWASP Top 10 Verification

| OWASP ID | Category | Status (Verified/N/A) | Notes |
|----------|----------|-----------------------|-------|
| A01 | Broken Access Control | | |
| A02 | Cryptographic Failures | | |
| A03 | Injection | | |
| A04 | Insecure Design | | |
| A05 | Security Misconfiguration | | |
| A06 | Vulnerable and Outdated Components | | |
| A07 | Identification and Authentication Failures | | |
| A08 | Software and Data Integrity Failures | | |
| A09 | Security Logging and Monitoring Failures | | |
| A10 | Server-Side Request Forgery (SSRF) | | |

## Data Protection

- [ ] PII is encrypted at rest
- [ ] PII is encrypted in transit (TLS 1.2+)
- [ ] Sensitive data is not written to logs
- [ ] Data retention policy is implemented or documented
- [ ] GDPR/CCPA compliance verified (if applicable)

## Authentication & Authorization

- [ ] Strong password policy enforced
- [ ] MFA supported (if applicable)
- [ ] Session management is secure (timeouts, invalidation)
- [ ] JWT tokens have appropriate expiry and are signed securely
- [ ] Role-based access control (RBAC) is implemented and tested

## API Security

- [ ] Rate limiting implemented on all public endpoints
- [ ] Input validation on all API endpoints
- [ ] CORS configured correctly (no wildcard in production)
- [ ] API versioning implemented
- [ ] Error responses do not leak internal details (stack traces, DB info)

## Findings

| ID | Category | Description | Severity | Status | Remediation |
|----|----------|-------------|----------|--------|-------------|
|    |          |             |          |        |             |

### GATE STATUS: [ ] PASSED  [ ] FAILED
