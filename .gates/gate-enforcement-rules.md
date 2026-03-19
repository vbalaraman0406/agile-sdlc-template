# Gate Enforcement Rules

> **FOR AI AGENTS**: These rules are non-negotiable. Read `gate-definitions.yaml` for the full list of gates and their applicability.

## Enforcement Protocol

1.  **Before starting any development in a phase**, the agent MUST read `gate-definitions.yaml` and identify which gates apply to the current phase type.

2.  **During development**, the agent MUST continuously check code against the applicable gates (e.g., running SAST checks mentally or via tools as code is written).

3.  **Before marking a phase as complete**, the agent MUST:
    a.  Execute or simulate every applicable gate.
    b.  Fill in the corresponding report template in the phase's `scan-results/` or `test-results/` directory.
    c.  Fill in the `gate-checklist.md` for the phase with PASS/FAIL status for each gate.

4.  **If any `blocking: true` gate has a status of FAIL**, the agent MUST NOT proceed to the next phase. It must fix the issues and re-run the gate until it passes.

5.  **The `max_severity_allowed` field** defines the highest severity finding that is acceptable. For example, `MEDIUM` means CRITICAL and HIGH findings MUST be resolved, but MEDIUM and LOW can be documented with a remediation plan.

## What "Running a Gate" Means for an AI Agent

AI agents may not have access to external scanning tools. In that case, the agent MUST perform a **thorough manual review** that simulates the scan. For example:

-   **SAST**: The agent reviews all source code for common vulnerability patterns (injection, XSS, insecure deserialization, etc.) and documents findings.
-   **DAST**: If the app is running locally, the agent tests endpoints for common vulnerabilities. If not, the agent documents which tests should be run and provides a plan.
-   **SCA**: The agent reviews `package.json`, `requirements.txt`, or equivalent dependency files and checks for known vulnerabilities using public databases (e.g., NVD, GitHub Advisories).
-   **Secrets Scan**: The agent searches all files for patterns resembling API keys, passwords, and tokens.

The key principle is: **the gate must be addressed, documented, and signed off, even if the scan is manual.**
