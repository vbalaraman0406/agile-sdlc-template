# Phase [N]: [Phase Name]

## Phase Overview

**Type**: [Phase Type from project-config.yaml]
**Status**: PENDING
**Sprint Duration**: [from project-config.yaml]

## Goals

Describe the high-level goals for this phase. What should be accomplished by the end of this phase?

1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

## User Stories

The following user stories are assigned to this phase. Each story is detailed in the `user-stories/` directory.

| Story ID | Title | Priority | Story Points | Status |
|----------|-------|----------|--------------|--------|
| US-[N]-001 | | | | PENDING |
| US-[N]-002 | | | | PENDING |
| US-[N]-003 | | | | PENDING |

## Architecture Considerations

Describe any new components, services, or architectural changes introduced in this phase. A full architecture review must be completed in `architecture-review.md`.

## Dependencies

List any dependencies on other phases, external services, or team members.

| Dependency | Type (Internal/External) | Status | Notes |
|------------|--------------------------|--------|-------|
|            |                          |        |       |

## Quality Gates for This Phase

Refer to `gate-checklist.md` for the full checklist. The following gates are applicable to this phase:

| Gate | Applicable | Artifact |
|------|------------|----------|
| Architecture Review | Yes | `architecture-review.md` |
| Code Review | | `code-review.md` |
| Unit Tests | | `test-results/unit-test-report.md` |
| Integration Tests | | `test-results/integration-test-report.md` |
| E2E Tests | | `test-results/e2e-test-report.md` |
| SAST | | `scan-results/sast-report.md` |
| DAST | | `scan-results/dast-report.md` |
| SCA | | `scan-results/sca-report.md` |
| SPA Security | | `scan-results/spa-security-report.md` |
| Secrets Scan | | `scan-results/secrets-scan-report.md` |
| License Compliance | | `scan-results/license-compliance-report.md` |
| Accessibility | | `scan-results/accessibility-report.md` |
| IaC Scan | | `scan-results/iac-scan-report.md` |
| Performance Testing | | `test-results/performance-test-report.md` |

## Phase Completion Criteria

This phase is complete ONLY when:
1. All user stories are marked as DONE (see Definition of Done in AGENTS.md).
2. All applicable quality gates in `gate-checklist.md` are PASSED.
3. `phase-tracker.yaml` is updated to reflect COMPLETED status.
4. `CHANGELOG.md` is updated with a summary of this phase.
5. `retrospective.md` is filled in.
