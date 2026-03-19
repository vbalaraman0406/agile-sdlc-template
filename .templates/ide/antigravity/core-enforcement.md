---
name: core-enforcement
description: Core SDLC enforcement rules. Always active. Ensures the agent follows the mandatory pipeline, security scans, and phase gates for every action.
activation: always_on
---

# Core Enforcement Rules

These rules are ALWAYS active and cannot be overridden.

## BEFORE EVERY RESPONSE
1. Verify you have run `/start` this session. If not, run it now.
2. Verify `state.md` is current. If not, read it now.

## BEFORE WRITING CODE
1. Confirm a plan or design document exists and is approved.
2. Write a failing test FIRST (TDD). Then write the implementation.

## AFTER WRITING CODE
1. Run `/security-scan` immediately.
2. Run `flutter analyze` (if Flutter) or equivalent linter.
3. Update `state.md` with what was changed.

## BEFORE COMMITTING
1. Verify `/security-scan` passed with no CRITICAL or HIGH findings.
2. Verify no hardcoded secrets exist (check Step 3 of security-scan).
3. Use conventional commit format: `type(scope): description`
4. Append a Phase 3 entry to `docs/security_audit.md`.

## BEFORE SAYING "DONE"
1. Complete the SESSION END GATE checklist (defined in AGENTS.md).
2. Update `state.md` with final status.
3. Append session summary to `recap.log`.
