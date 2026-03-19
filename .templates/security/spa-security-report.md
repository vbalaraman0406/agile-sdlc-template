## SPA Security Report — Phase [N]

### Date: [date]

### CSP Review
- [ ] Content-Security-Policy header configured
- [ ] No `unsafe-inline` in `script-src`
- [ ] No `unsafe-eval` in `script-src`
- [ ] `report-uri` / `report-to` configured

### XSS Prevention
- [ ] All user input is sanitized/encoded before rendering
- [ ] No use of `innerHTML`/`dangerouslySetInnerHTML` with user-controlled data
- [ ] DOM-based XSS vectors reviewed and mitigated

### Client-Side Storage
- [ ] No sensitive data (tokens, PII) in `localStorage`
- [ ] No sensitive data in `sessionStorage`
- [ ] Cookies have `Secure`, `HttpOnly`, and `SameSite=Strict` flags

### Authentication & Session
- [ ] Tokens are stored securely (e.g., in-memory with secure cookie for refresh token)
- [ ] Token refresh mechanism is secure
- [ ] Logout properly invalidates all client-side and server-side sessions/tokens

### CORS
- [ ] CORS `Access-Control-Allow-Origin` is restrictive (no wildcard `*` in production)
- [ ] `Access-Control-Allow-Credentials` is not used with a wildcard origin

### Findings
| Category | Issue | Severity | Status | Remediation |
|----------|-------|----------|--------|-------------|
|          |       |          |        |             |

### GATE STATUS: [ ] PASSED  [ ] FAILED
