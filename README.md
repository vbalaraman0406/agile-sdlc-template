# Universal AI-Native Agile SDLC Project Template

> A framework for building production-grade applications with AI coding agents, enforcing enterprise-level quality, security, and process at every step.

---

## 1. The Problem: The Chaos of AI-Powered Development

AI coding agents (Google Antigravity IDE, Claude Code, Cursor, Windsurf, GitHub Copilot) are revolutionary. They generate code at incredible speed, but this speed often comes at a cost. Without a structured SDLC, projects become chaotic, inconsistent, and insecure. Agents forget instructions mid-session, skip security scans, and produce code that is difficult to maintain.

This template solves that problem by imposing a **strict, repeatable, and enforceable Agile SDLC process** on any AI coding agent.

## 2. Core Features

| Feature | Description |
|---|---|
| **Interactive Init Script** | Run `project-init.py`, answer 6 questions, and get a fully configured project scaffold in seconds. |
| **IDE-Aware Generation** | Automatically generates the correct instruction files for your chosen AI coding IDE (Antigravity, Claude Code, Cursor, Windsurf, Copilot, or Universal). |
| **Dynamic Phase Generation** | Define 3 to 10 Agile phases, and the script generates the entire structure with all required artifacts. |
| **14 Enforced Quality Gates** | Every phase requires passing a comprehensive checklist of 14 gates, from SAST/DAST to accessibility and performance testing. |
| **Multi-Stack Presets** | Comes with presets for common tech stacks (React/Node, Python/FastAPI, Flutter) or can be used in a tech-agnostic way. |
| **Comprehensive Templates** | Includes pre-built templates for user stories, architecture reviews, security reports, code reviews, and retrospectives. |

## 3. Supported AI Coding IDEs

The init script asks which IDE you are using and generates **only the files that IDE needs**, in the exact locations and formats it expects.

| IDE | Files Generated | How It Works |
|---|---|---|
| **Google Antigravity** | `GEMINI.md` + `AGENTS.md` + `.agents/rules/core-enforcement.md` + `.agents/rules/security-enforcement.md` | `GEMINI.md` is the highest-priority rule file. `.agents/rules/` files use "Always On" activation so they are injected into every conversation automatically. |
| **Claude Code** | `CLAUDE.md` + `AGENTS.md` | Claude Code reads `CLAUDE.md` as its primary instruction file and falls back to `AGENTS.md`. Both are generated. |
| **Cursor** | `.cursor/rules/core.mdc` + `.cursor/rules/security.mdc` + `AGENTS.md` | Cursor uses `.mdc` files in `.cursor/rules/` with scope-based activation (Always On, Auto Attached). `AGENTS.md` provides broader context. |
| **Windsurf** | `.windsurf/rules/core.md` + `AGENTS.md` | Windsurf reads rule files from `.windsurf/rules/` with activation modes. `AGENTS.md` provides broader context. |
| **GitHub Copilot** | `.github/copilot-instructions.md` + `.github/instructions/security.instructions.md` + `AGENTS.md` | Copilot reads from `.github/copilot-instructions.md` for project-wide rules and supports glob-scoped instruction files. |
| **Universal / Other** | `AGENTS.md` only | The Linux Foundation open standard, supported by 60,000+ projects. Works with Codex CLI, Aider, Continue.dev, OpenHands, and any agent that reads `AGENTS.md`. |

## 4. Getting Started

### Step 1: Download and Unzip

Download the `.zip` file for this project and unzip it, or clone the repository.

```bash
git clone https://github.com/vbalaraman0406/agile-sdlc-template.git
```

### Step 2: Run the Initialization Script

```bash
cd agile-sdlc-template
python3 project-init.py
```

The script will ask you **6 questions**:

| # | Question | Example Answer |
|---|----------|---------------|
| 1 | Project name | `my-banking-app` |
| 2 | Human-readable title | `My Banking App` |
| 3 | Brief description | `A mobile banking POC with biometric auth` |
| 4 | Application type | `2` (Mobile Application) |
| 5 | Technology stack | `3` (Flutter) |
| 6 | **AI Coding IDE** | `1` (Google Antigravity) |
| 7 | Number of phases | `6` |

### Step 3: Open in Your AI Coding IDE

The script generates a new directory (e.g., `my-banking-app/`). Open it in your chosen IDE. The agent will automatically detect and load the generated instruction files.

**For Google Antigravity users:** Also copy `GEMINI.md` to your global location for cross-workspace enforcement:

```bash
mkdir -p ~/.gemini
cp my-banking-app/GEMINI.md ~/.gemini/GEMINI.md
```

## 5. Generated Project Structure

After running the init script with **Google Antigravity** selected and **5 phases**, you get:

```
my-banking-app/
├── GEMINI.md                          ← Antigravity: highest-priority rules
├── AGENTS.md                          ← Universal: auto-loaded by all IDEs
├── .agents/
│   └── rules/
│       ├── core-enforcement.md        ← Antigravity: "Always On" workspace rule
│       └── security-enforcement.md    ← Antigravity: "Always On" workspace rule
├── project-config.yaml                ← Machine-readable project configuration
├── phase-tracker.yaml                 ← Phase progress tracker
├── phases/
│   ├── phase-01-discovery/
│   │   ├── PHASE.md
│   │   ├── gate-checklist.md          ← 14 quality gates to pass
│   │   ├── user-stories/
│   │   ├── scan-results/              ← SAST, DAST, SCA, SPA reports
│   │   └── test-results/              ← Unit, integration, E2E, perf reports
│   ├── phase-02-architecture/
│   ├── phase-03-core-development/
│   ├── phase-04-security-hardening/
│   └── phase-05-release/
├── src/
├── tests/
├── docs/
│   ├── architecture/
│   ├── api/
│   └── retrospectives/
├── .templates/                        ← Template library (user stories, reviews, etc.)
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

If you had selected **Cursor** instead, the root would contain `.cursor/rules/core.mdc` and `.cursor/rules/security.mdc` instead of `GEMINI.md` and `.agents/rules/`.

## 6. The 14 Quality Gates

Every phase includes a `gate-checklist.md` with these mandatory checkpoints:

| # | Gate | Description |
|---|------|-------------|
| 1 | Architecture Review | Design validation against SOLID, scalability, and security principles |
| 2 | Code Review | AI-assisted and manual peer review checklist |
| 3 | Unit Tests | Per-feature unit test coverage gates |
| 4 | Integration Tests | Cross-component and service testing |
| 5 | E2E Tests | End-to-end user flow testing |
| 6 | SAST | Static Application Security Testing (code-level vulnerabilities) |
| 7 | DAST | Dynamic Application Security Testing (runtime scanning) |
| 8 | SCA | Software Composition Analysis (dependency vulnerabilities) |
| 9 | SPA Security | CSP, XSS, CORS, and client-side security review |
| 10 | Secrets Scanning | Detect hardcoded API keys, passwords, and tokens |
| 11 | License Compliance | Open-source license risk analysis |
| 12 | Accessibility (a11y) | WCAG compliance checks |
| 13 | IaC Scanning | Infrastructure-as-Code misconfiguration detection |
| 14 | Performance Testing | Stress testing and benchmarks |

## 7. Tips for Strict Rule Enforcement

If your AI agent keeps "forgetting" rules, use these proven techniques:

**For Google Antigravity:**
1. Copy `GEMINI.md` to `~/.gemini/GEMINI.md` (global enforcement)
2. Set **Artifact Review Policy** to "Request Review" in Settings
3. Set **Terminal Command Auto Execution** to "Request Review" in Settings
4. Always use **Planning mode** (not Fast) for feature work
5. Train persistent **Knowledge Items** by telling the agent: "Remember this permanently: [rule]"

**For Claude Code:**
1. Keep `CLAUDE.md` under 300 lines (LLM instruction limit)
2. Use subdirectory `CLAUDE.md` files for scoped rules

**For Cursor:**
1. Use `.cursor/rules/` with `always_on` scope for critical rules
2. Use `auto_attach` scope with file glob patterns for language-specific rules

**For All IDEs:**
1. If the agent drifts, paste: "STOP. Re-read AGENTS.md right now. Report which rules you are violating."
2. Keep instruction files concise and imperative (commands, not suggestions)
3. Use numbered rules, not prose paragraphs

## 8. License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
