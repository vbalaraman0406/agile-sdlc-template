#!/usr/bin/env python3
"""
Agile SDLC Project Initialization Script
Generates a complete project scaffold with AI agent instructions,
phase directories, quality gates, and security scan templates.
"""

import os
import sys
import shutil

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install it with: pip3 install pyyaml")
    sys.exit(1)

from datetime import datetime

# --- Configuration ---

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))

STACK_PRESETS = {
    "1": {"id": "react-node", "name": "React + Node.js (Vite, Express)"},
    "2": {"id": "python-fastapi", "name": "Python + FastAPI"},
    "3": {"id": "flutter", "name": "Flutter (Mobile)"},
    "4": {"id": "generic", "name": "Generic / Tech-Agnostic"},
}

APP_TYPES = {
    "1": "Web Application",
    "2": "Mobile Application",
    "3": "API / Backend Service",
    "4": "Full-Stack Application",
}

IDE_PRESETS = {
    "1": {"id": "antigravity", "name": "Google Antigravity"},
    "2": {"id": "claude", "name": "Claude Code"},
    "3": {"id": "cursor", "name": "Cursor"},
    "4": {"id": "windsurf", "name": "Windsurf"},
    "5": {"id": "copilot", "name": "GitHub Copilot"},
    "6": {"id": "universal", "name": "Universal / Other (AGENTS.md only)"},
}

PHASE_CATALOG = [
    {"id": "discovery", "name": "Discovery & Research"},
    {"id": "architecture", "name": "Architecture & Setup"},
    {"id": "core-development", "name": "Core Feature Development (MVP)"},
    {"id": "feature-development", "name": "Iterative Feature Development"},
    {"id": "integration", "name": "Integration & API Linkage"},
    {"id": "security-hardening", "name": "Security Hardening & Audit"},
    {"id": "performance", "name": "Performance & Load Testing"},
    {"id": "uat", "name": "User Acceptance Testing (UAT)"},
    {"id": "staging", "name": "Staging & Pre-Release"},
    {"id": "release", "name": "Production Release & Monitoring"},
]

ALL_QUALITY_GATES = [
    "Architecture Review",
    "Code Review",
    "Unit Tests",
    "Integration Tests",
    "E2E Tests",
    "SAST",
    "DAST",
    "SCA",
    "SPA Security",
    "Secrets Scanning",
    "License Compliance",
    "Accessibility (a11y)",
    "IaC Scanning",
    "Performance Testing",
]


# --- Helper Functions ---

def print_header(title):
    print("\n" + "=" * 60)
    print("  " + title)
    print("=" * 60 + "\n")


def ask_question(prompt, options=None):
    print("> " + prompt)
    if options:
        for key, value in options.items():
            print("    [{}] {}".format(key, value))
    while True:
        choice = input("  Your choice: ").strip()
        if not options or choice in options:
            return choice
        print("  Invalid choice, please try again.")


def ask_text(prompt):
    print("> " + prompt)
    return input("  Your answer: ").strip()


def ask_number(prompt, min_val=1, max_val=10):
    while True:
        try:
            num = int(ask_text(prompt + " ({}-{})".format(min_val, max_val)))
            if min_val <= num <= max_val:
                return num
            else:
                print("  Please enter a number between {} and {}.".format(min_val, max_val))
        except ValueError:
            print("  Invalid input. Please enter a number.")


def build_phase_list(num_phases):
    """Build a sensible list of phases based on the requested count."""
    phases = []
    phases.append(PHASE_CATALOG[0])  # Discovery
    phases.append(PHASE_CATALOG[1])  # Architecture
    phases.append(PHASE_CATALOG[2])  # Core Dev

    middle_count = max(0, num_phases - 5)
    for i in range(middle_count):
        entry = dict(PHASE_CATALOG[3])  # Feature Dev copy
        if middle_count > 1:
            entry["name"] = "Feature Development Sprint {}".format(i + 1)
        phases.append(entry)

    if num_phases >= 6:
        phases.append(PHASE_CATALOG[4])  # Integration

    phases.append(PHASE_CATALOG[5])  # Security Hardening
    phases.append(PHASE_CATALOG[9])  # Release

    return phases[:num_phases]


def generate_ide_files(project_root, ide_id, config):
    """Generate IDE-specific instruction files based on the chosen IDE."""
    print("  Generating files for IDE: {}".format(IDE_PRESETS[ide_id]["name"]))

    # Always generate the generic AGENTS.md
    shutil.copy(
        os.path.join(TEMPLATE_DIR, ".templates/ide/generic/AGENTS.md"),
        os.path.join(project_root, "AGENTS.md")
    )

    if ide_id == "1": # Antigravity
        os.makedirs(os.path.join(project_root, ".agents/rules"), exist_ok=True)
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/antigravity/GEMINI.md"), os.path.join(project_root, "GEMINI.md"))
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/antigravity/core-enforcement.md"), os.path.join(project_root, ".agents/rules/core-enforcement.md"))
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/antigravity/security-enforcement.md"), os.path.join(project_root, ".agents/rules/security-enforcement.md"))
    elif ide_id == "2": # Claude Code
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/claude/CLAUDE.md"), os.path.join(project_root, "CLAUDE.md"))
    elif ide_id == "3": # Cursor
        os.makedirs(os.path.join(project_root, ".cursor/rules"), exist_ok=True)
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/cursor/core.mdc"), os.path.join(project_root, ".cursor/rules/core.mdc"))
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/cursor/security.mdc"), os.path.join(project_root, ".cursor/rules/security.mdc"))
    elif ide_id == "4": # Windsurf
        os.makedirs(os.path.join(project_root, ".windsurf/rules"), exist_ok=True)
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/windsurf/core.md"), os.path.join(project_root, ".windsurf/rules/core.md"))
    elif ide_id == "5": # Copilot
        os.makedirs(os.path.join(project_root, ".github/instructions"), exist_ok=True)
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/copilot/copilot-instructions.md"), os.path.join(project_root, ".github/copilot-instructions.md"))
        shutil.copy(os.path.join(TEMPLATE_DIR, ".templates/ide/copilot/security.instructions.md"), os.path.join(project_root, ".github/instructions/security.instructions.md"))

    print("  [OK] Generated IDE-specific instruction files.")


# --- Main Logic ---

def main():
    print_header("Agile SDLC Project Initialization Script")
    print("This script will guide you through creating a new project scaffold.")
    print("The generated project will be ready for AI coding agents to use.\n")

    # Step 1: Project Details
    print_header("Step 1: Project Details")
    project_name = ask_text("Enter the project name (e.g., my-awesome-app):")
    project_title = ask_text("Enter a human-readable project title (e.g., My Awesome App):")
    project_description = ask_text("Enter a brief project description:")

    # Step 2: Application Type
    print_header("Step 2: Application Type")
    app_type_choice = ask_question("What type of application are you building?", {k: v for k, v in APP_TYPES.items()})
    app_type = APP_TYPES[app_type_choice]

    # Step 3: Technology Stack
    print_header("Step 3: Technology Stack")
    stack_options = {k: v["name"] for k, v in STACK_PRESETS.items()}
    stack_choice = ask_question("Choose a technology stack preset:", stack_options)
    tech_stack = STACK_PRESETS[stack_choice]

    # Step 4: AI Coding IDE
    print_header("Step 4: AI Coding IDE")
    ide_options = {k: v["name"] for k, v in IDE_PRESETS.items()}
    ide_choice = ask_question("Which AI Coding IDE will you be using?", ide_options)
    ide_preset = IDE_PRESETS[ide_choice]

    # Step 5: Number of Phases
    print_header("Step 5: Project Phases")
    num_phases = ask_number("How many phases (sprints) will this project have?", 3, 10)

    print("\nConfiguring the project phases...")
    final_phases = build_phase_list(num_phases)
    for i, p in enumerate(final_phases):
        print("  Phase {}: {}".format(i + 1, p["name"]))

    # Build config dict
    config = {
        "project": {
            "name": project_name,
            "title": project_title,
            "description": project_description,
            "type": app_type,
            "initialized_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },
        "stack": {
            "id": tech_stack["id"],
            "name": tech_stack["name"],
        },
        "ide": {
            "id": ide_preset["id"],
            "name": ide_preset["name"],
        },
        "agile": {
            "total_phases": num_phases,
            "phases": [
                {"id": i + 1, "type": p["id"], "name": p["name"], "status": "PENDING"}
                for i, p in enumerate(final_phases)
            ],
        },
        "quality_gates": list(ALL_QUALITY_GATES),
    }

    # Step 6: Generate Project Scaffold
    print_header("Step 6: Generating Project Scaffold")
    project_root = os.path.join(os.getcwd(), project_name)

    if os.path.exists(project_root):
        print("Error: Directory 	'{}' already exists. Aborting.".format(project_root))
        return

    try:
        # Copy the entire template directory, ignoring the IDE templates
        shutil.copytree(
            TEMPLATE_DIR,
            project_root,
            ignore=shutil.ignore_patterns("*.pyc", "__pycache__", ".templates/ide")
        )
        print("  [OK] Copied base template files to {}/".format(project_name))

        # Generate IDE-specific files
        generate_ide_files(project_root, ide_choice, config)

        # Write the project-config.yaml file
        config_path = os.path.join(project_root, "project-config.yaml")
        with open(config_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        print("  [OK] Created project-config.yaml")

        # Create phase directories
        phases_dir = os.path.join(project_root, "phases")
        os.makedirs(phases_dir, exist_ok=True)

        phase_list = config["agile"]["phases"]
        for i, phase in enumerate(phase_list):
            p_type = phase["type"]
            p_name = phase["name"]
            p_num = str(i + 1).zfill(2)
            dir_name = "phase-{}-{}".format(p_num, p_type)
            phase_path = os.path.join(phases_dir, dir_name)
            os.makedirs(phase_path, exist_ok=True)

            for subdir in ["user-stories", "test-results", "scan-results"]:
                os.makedirs(os.path.join(phase_path, subdir), exist_ok=True)

            with open(os.path.join(phase_path, "PHASE.md"), "w") as f:
                f.write("# Phase {}: {}\n\n## Goals\n- \n\n## Acceptance Criteria\n- \n".format(i + 1, p_name))

            with open(os.path.join(phase_path, "gate-checklist.md"), "w") as f:
                gate_lines = ["- [ ] {}".format(g) for g in ALL_QUALITY_GATES]
                f.write("# Gate Checklist for Phase {}\n\n{}\n".format(i + 1, "\n".join(gate_lines)))

        print("  [OK] Created {} phase directories with all artifacts".format(len(phase_list)))

        # Create src, tests, docs directories
        for d in ["src", "tests", "docs/architecture", "docs/api", "docs/retrospectives"]:
            os.makedirs(os.path.join(project_root, d), exist_ok=True)
        print("  [OK] Created src/, tests/, docs/ directories")

        print("\n" + "-" * 60)
        print("Project 	'{}' created successfully!".format(project_name))
        print("Next steps:")
        print("1. cd {}".format(project_name))
        print("2. Open the project in your chosen AI coding IDE.")
        print("3. The agent should automatically pick up the generated instruction files.")
        print("-" * 60)

    except Exception as e:
        print("\nAn error occurred: {}".format(e))
        if os.path.exists(project_root):
            print("Cleaning up partially created project...")
            shutil.rmtree(project_root)

if __name__ == "__main__":
    main()
