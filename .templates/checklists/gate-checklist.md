# Gate Checklist for Phase [N]

> **MANDATORY**: All gates MUST be checked and passed before transitioning to the next phase.
> The AI agent MUST verify each item and provide evidence of completion.

## Phase Sign-Off

| Gate | Status (PASS/FAIL) | Evidence (Link to artifact) | Verified By (Agent/User) |
|------|--------------------|-----------------------------|--------------------------|
| **Architecture Review** | | `architecture-review.md` | |
| **Code Review** | | `code-review.md` | |
| **Unit Tests** | | `test-results/unit-test-report.md` | |
| **Integration Tests** | | `test-results/integration-test-report.md` | |
| **E2E Tests** | | `test-results/e2e-test-report.md` | |
| **SAST Scan** | | `scan-results/sast-report.md` | |
| **DAST Scan** | | `scan-results/dast-report.md` | |
| **SCA Scan** | | `scan-results/sca-report.md` | |
| **SPA Security Review** | | `scan-results/spa-security-report.md` | |
| **Secrets Scan** | | `scan-results/secrets-scan-report.md` | |
| **License Compliance** | | `scan-results/license-compliance-report.md` | |
| **Accessibility (a11y)** | | `scan-results/accessibility-report.md` | |
| **IaC Scan** | | `scan-results/iac-scan-report.md` | |
| **Performance Testing** | | `test-results/performance-test-report.md` | |

---

### Phase Status: [ ] PENDING [ ] PASSED [ ] FAILED

### Sign-Off Comments:


### Next Steps:
- If PASSED: Proceed to the next phase as defined in `project-config.yaml`.
- If FAILED: Create remediation tasks for all failed gates. DO NOT proceed.
