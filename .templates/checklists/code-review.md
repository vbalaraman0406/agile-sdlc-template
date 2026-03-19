# Code Review — Phase [N]

## Review Summary

| User Story | Reviewer | Date | Status (PASS/FAIL) |
|------------|----------|------|--------------------|
|            |          |      |                    |

---

## Per-Story Review Checklist

### US-[PHASE]-[NUMBER]: [Title]

#### Functionality
- [ ] Code correctly implements the user story requirements
- [ ] All acceptance criteria are met
- [ ] Edge cases are handled
- [ ] Error handling is comprehensive and user-friendly

#### Code Quality
- [ ] Follows coding standards (AGENTS.md Section 8)
- [ ] No code smells or anti-patterns
- [ ] No duplicated code
- [ ] Functions are single-purpose and well-named
- [ ] Comments explain "why", not "what"

#### Security
- [ ] No hardcoded secrets or credentials
- [ ] Input validation is present on all entry points
- [ ] Output encoding is present (for UI rendering)
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (for web applications)
- [ ] CSRF protection (for web applications)
- [ ] Authentication/authorization checks are present and correct

#### Testing
- [ ] Unit tests cover happy path
- [ ] Unit tests cover error/edge cases
- [ ] Test coverage >= 80% for changed code
- [ ] Tests are deterministic (no flaky tests)

#### Performance
- [ ] No N+1 query problems
- [ ] No unnecessary re-renders (for UI frameworks)
- [ ] Large data sets handled with pagination/streaming
- [ ] No potential memory leaks

#### Documentation
- [ ] Public API/functions documented
- [ ] Complex logic has explanatory comments
- [ ] README updated if needed
- [ ] CHANGELOG updated

### GATE STATUS: [ ] PASSED  [ ] FAILED
