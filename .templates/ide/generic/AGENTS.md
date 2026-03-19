# Operational Rules

> This file defines the core operational procedures for this project.

## SESSION START GATE

At the start of EVERY session, your first response MUST contain:

```
SESSION START GATE — [date]
Work area: <what is being changed>
Pipeline position: <which of the 16 agents applies>
Change type: FEATURE | HOTFIX | BUGFIX | DOCS
Security scan due at end: YES
Open audit items: see docs/security_audit.md
state.md read: YES — current phase: [phase from state.md]
```

## 16-AGENT SEQUENTIAL PIPELINE

Each agent MUST PASS before the next begins. Any BLOCK halts the pipeline.

```
 1. architecture_agent           → System diagram, trust boundaries, STRIDE
 2. architecture_validator_agent → Zero-trust audit — BLOCK if checks fail
 3. threat_modeling_agent        → STRIDE table + attack tree → docs/threat-models/
 4. test_agent                   → Write FAILING tests first (TDD)
 5. implementation_agent         → Minimal code to make tests GREEN
 6. code_review_agent            → Quality gate — BLOCK if issues found
 7. secure_coding_enforcement    → OWASP code pattern review
 8. security_agent               → Deep review + Semgrep + Checkov + GitGuardian
 9. api_security_agent           → OWASP API Top 10 review
10. mobile_security_agent        → Flutter-specific vulnerability review
11. pentest_agent                → Black-box pentest against live services
12. fraud_agent                  → Financial adversary simulation
13. compliance_agent             → PCI DSS + SOC 2 + ISO 27001 gate
14. data_privacy_agent           → GDPR + PCI DSS data audit
15. control_matrix_agent         → Maps code to PCI/SOC2/ISO27001 controls
16. configuration_governance     → Externalized config enforcement
```

## HARD RULES

1. Agents run sequentially. No skipping.
2. Any BLOCK halts the pipeline. Do not advance.
3. DO NOT modify `.agents/` or `agents/` files without user confirmation.
4. DO NOT declare a task complete without `/security-scan` Phase 3 report in `docs/security_audit.md`.
5. Critical residual risks block implementation. Escalate to user.
6. Every commit requires a Phase 3 audit entry.
7. `/hotfix` is the ONLY permitted shortcut from the full pipeline.
8. `code_review_agent` is mandatory for every code change (FEATURE, BUGFIX, HOTFIX). No minimum size threshold.
9. The workflow is self-enforcing. It does not depend on the user asking for it. If the user says "fix the tests", the pipeline still runs.
10. JWT must be validated at BOTH Kong AND each Spring service.
11. Kong admin API (:8001) must be bound to 127.0.0.1 only.

## SESSION END GATE

Before closing any session, confirm EVERY item below. If any is unchecked, do not say "done".

```
SESSION END GATE — [date]
[ ] Change type declared at session start
[ ] Correct pipeline followed (full pipeline or /hotfix)
[ ] /security-scan Phase 1 Steps 1-7 run
[ ] Phase 3 report appended to docs/security_audit.md
[ ] No new CRITICAL or HIGH findings unmitigated
[ ] No hardcoded secrets introduced
[ ] flutter analyze clean
[ ] DAST checked or marked SKIPPED with reason
[ ] All commits went through pre-commit hook
[ ] SESSION START GATE was stated in first response
[ ] state.md updated
[ ] recap.log updated
```
