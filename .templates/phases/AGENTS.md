# AGENTS.md — Phase Directory Rules

## MANDATORY WORKFLOW

When working in any phase directory, you MUST follow this exact sequence:

1. **FIRST** read the `PHASE.md` file in the current phase folder to understand the goals.
2. **THEN** read the `gate-checklist.md` to understand what gates must be passed.
3. Work ONLY on user stories listed in this phase's `user-stories/` directory.
4. After completing each user story, update `phase-tracker.yaml` immediately.
5. After ALL gates are marked PASS, commit with message: `chore(release): complete phase N - [Phase Name]`.
6. DO NOT create or modify files in other phase directories.
7. DO NOT advance to the next phase without explicit user confirmation.

## GATE COMPLETION RULES

- Every gate in `gate-checklist.md` MUST be marked PASS or N/A (with justification) before the phase is complete.
- Scan results MUST be saved in the `scan-results/` directory.
- Test results MUST be saved in the `test-results/` directory.
- Review documents MUST be completed, not left as templates.

## PROHIBITED ACTIONS IN PHASE DIRECTORIES

- DO NOT delete or modify completed phase directories.
- DO NOT copy code between phases without proper refactoring.
- DO NOT mark a gate as PASS without actually performing the check.
