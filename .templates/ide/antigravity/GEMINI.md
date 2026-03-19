# CRITICAL RULES — READ BEFORE ANY ACTION

You MUST follow every rule in this file. Violating any rule is a session failure.

## RULE 1: SESSION START
At the start of EVERY session, execute the `/start` workflow. No other action is permitted first.

## RULE 2: STATE AWARENESS
Read `state.md` before any work. Update `state.md` after completing any task.

## RULE 3: NO HARDCODED SECRETS
You are FORBIDDEN from writing code containing API keys, passwords, or tokens. Use environment variables or Vault.

## RULE 4: NO BLIND CODING
You are FORBIDDEN from writing feature code without first creating a plan and getting user approval.

## RULE 5: VERIFY BEFORE REFERENCING
You are FORBIDDEN from assuming files exist. Run `ls` or `cat` to verify before referencing any file.

## RULE 6: PHASE GATES
You are FORBIDDEN from advancing to the next phase until all checks in the current phase are complete and documented in `state.md`.

## RULE 7: MANDATORY SECURITY SCAN
Run `/security-scan` after every code change and before every commit. No exceptions.

## RULE 8: NO PERSONA
You are a tool. Execute tasks efficiently. Do not role-play or adopt a persona.

## RULE 9: PLANNING MODE
For every new feature or user story, use Planning mode. Create an Implementation Plan artifact FIRST. Do not write code until the plan is approved.

## RULE 10: SELF-CHECK
Before responding to ANY user message, silently verify: "Am I about to violate any rule in this file?" If yes, stop and correct yourself before responding.

## CONTEXT HIERARCHY
1. **This file** (`GEMINI.md`): Your constitution. Highest priority.
2. **`AGENTS.md`** (project root): Operational rules. Read after this file.
3. **`.agents/rules/`**: Workspace rules. Always On rules are auto-applied.
4. **`.agents/skills/`** and **`.agents/workflows/`**: On-demand. Read only when a task requires them.
5. **`state.md`**: Your memory. Read and write constantly.

## REFERENCE FILES
For the full 16-agent pipeline, banking security rules, and workflow details, read `AGENTS.md` via: @AGENTS.md
