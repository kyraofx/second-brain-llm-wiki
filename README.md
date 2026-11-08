# Second Brain / LLM Wiki

> **Version 1.0.0** — a private-review portfolio demonstration of an agent-operated personal knowledge system.

I built this project to explore a simple question: what happens when a second brain is designed for both a person and an AI agent from the beginning?

The result is an Obsidian-compatible Markdown vault where agents can plan a week, review daily notes, maintain connected records, and create weekly summaries through clear `SKILL.md` workflows. OpenAI scheduled automations decide when the main workflows run, while Git and a deterministic validator make every change inspectable.

> [!IMPORTANT]
> **Portfolio demonstration only.** This repository is a curated example of how my system works. It is not a starter kit, reusable vault, distributable product, or supported base for forks. The dataset is entirely fictional.

## What I built

- A Markdown knowledge system with typed YAML metadata and permanent record IDs
- A **Vault Manager** agent that coordinates planning, review, and vault maintenance
- A **Fitness Advisor** agent that reviews recorded diet and activity data without inventing missing details
- Four scoped Agent Skills: Weekly Planning, Daily Review, Weekly Review, and Fitness Review
- Three recurring workflow contracts triggered by OpenAI scheduled automations
- An Obsidian-compatible interface without required community plugins
- A dependency-free Python validator and GitHub Actions workflow for structural checks

## How it works

```text
Natural daily capture
        ↓
   Vault Manager
        ↓
   Agent Skills ─────→ connected records
        ↓                    ↓
daily and weekly notes ← planning + logs
        ↓
 validation + Git history
```

I keep the source material human-readable. The agent works through small, explicit skills instead of one large prompt, and each workflow defines what it may read, what it may change, and what it must preserve. For example, Daily Review can roll unfinished tasks and write a Summary, but it cannot rewrite the Diary.

## System components

| Component | Responsibility |
|---|---|
| Vault Manager | Coordinates supported workflows and protects the vault's structure |
| Fitness Advisor | Reviews Diet and Activity logs with evidence-linked, non-medical feedback |
| Weekly Planning | Builds seven daily plans from calendar events, recurring schedules, and habits |
| Daily Review | Rolls tasks, routes inputs, updates records and logs, and writes the daily Summary |
| Weekly Review | Synthesizes seven daily Summaries and Saturday's unfinished tasks |
| Fitness Review | Finds patterns in a requested Diet and Activity log period |
| OpenAI automations | Trigger Weekly Planning, Daily Review, and Weekly Review on their schedules |
| Validator | Checks IDs, metadata, links, privacy rules, daily structure, and path portability |

The live OpenAI schedules are external configuration, so this repository documents the automation contracts without exposing account-specific settings.

## Demonstration dataset

The fictional demo covers one complete week: **February 1–7, 2026**. It contains seven daily notes, a weekly review, Diet and Activity logs, 13 templates, and 14 connected records built around a fictional AI Meeting Assistant project.

The point is not the fictional project itself. The dataset shows how information moves through the system—from planning, to daily capture, to canonical records, to a weekly review—without copying anything from my private vault.

## Repository layout

```text
.
├── AGENTS.md                  # Repository-wide agent policy
├── demo-vault/               # Obsidian-compatible synthetic vault
│   ├── system/
│   │   ├── agents/           # Vault Manager and Fitness Advisor
│   │   ├── automations/      # OpenAI automation contracts
│   │   ├── skills/           # Executable SKILL.md workflows
│   │   └── templates/        # Reusable note structures
│   ├── vault/                # Connected canonical records
│   └── workbench/            # Daily notes, planning, reviews, and logs
├── docs/                     # Architecture, privacy, and demo notes
├── scripts/                  # Deterministic validation
└── .github/workflows/        # Continuous integration
```

## Review the demo

The fastest path through the project is:

1. Read [`AGENTS.md`](AGENTS.md) for the repository rules.
2. Open [`demo-vault/system/agents/vault-manager.md`](demo-vault/system/agents/vault-manager.md) to see the main agent's role.
3. Inspect [`demo-vault/system/skills/`](demo-vault/system/skills/) to see how the workflows are scoped.
4. Compare the seven notes in [`demo-vault/workbench/daily/`](demo-vault/workbench/daily/) with the final [`weekly review`](demo-vault/workbench/shelf/weekly/2026-02-07-weekly-review.md).
5. Read [`docs/demo.md`](docs/demo.md) for the complete walkthrough.
6. Run the validator:

```bash
python3 scripts/validate_vault.py
```

## Technical decisions

- **Markdown is the source of truth.** The system remains readable without Obsidian or an AI interface.
- **Skills are narrow and inspectable.** Each `SKILL.md` defines one workflow and its boundaries.
- **Records use permanent IDs.** Filenames can change without changing record identity.
- **Original writing is preserved.** Agent-generated summaries are separated from Diary text.
- **Automations and skills are separate.** A skill defines how work is done; the OpenAI automation determines when it runs.
- **Validation is deterministic.** Structural checks do not depend on an LLM.
- **The portfolio demo is synthetic.** No private-vault content, credentials, or machine-specific paths are included.

## Current boundaries

- OpenAI automation schedules are configured outside this repository.
- The validator checks structural rules, not the quality of an agent's judgment.
- Obsidian is optional; no community plugins are required.
- This portfolio demonstration is not licensed for reuse, redistribution, or adaptation.
