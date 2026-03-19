# Claude Code Instructions

## CORE RULES
1.  **Follow `AGENTS.md`**: The rules in `AGENTS.md` are your primary operational guide. Read it first.
2.  **Sequential Execution**: Complete all steps in a phase before moving to the next. Do not skip steps.
3.  **Single-Task Focus**: Work on one user story or bug at a time. Do not mix tasks.
4.  **Minimalism**: Write the simplest, cleanest code that satisfies the requirement. Avoid over-engineering.
5.  **NO HARDCODED SECRETS**: You are FORBIDDEN from writing code containing API keys, passwords, or tokens. Use environment variables or Vault.

## WORKFLOW
1.  **Understand**: Read the user story and clarify any ambiguities.
2.  **Plan**: Create a brief implementation plan.
3.  **Test**: Write a failing test that proves the bug or defines the new feature.
4.  **Implement**: Write the minimal code to make the test pass.
5.  **Scan**: Run the `/security-scan` workflow.
6.  **Refactor**: Clean up the code now that it works and is secure.
7.  **Document**: Update `state.md` with the completion status.
8.  **Commit**: Commit the changes with a conventional commit message.
