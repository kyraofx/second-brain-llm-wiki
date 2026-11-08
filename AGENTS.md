# Repository instructions

## Project

This repository is a synthetic, portable reference implementation of an agent-operated second brain. Markdown is the source of truth. `demo-vault/` is both the example dataset and an Obsidian-compatible vault.

## Boundaries

- Keep every example fictional and safe for public release. Never add real personal records, credentials, local usernames, home-directory paths, or private-vault exports.
- Preserve user-authored Diary text exactly. Agent synthesis belongs only in designated generated sections or canonical records.
- Use repository-relative paths. Do not introduce machine-specific absolute paths.
- Planned or tentative material must not be represented as completed or confirmed.
- Treat `demo-vault/system/agents/` as descriptive role documentation, not active runtime configuration.
- Treat `demo-vault/system/automations/` as scheduling contracts. A specification is not active merely because its file exists.

## Workflows

- For preparing daily notes from planning sources, use `$weekly-planning` from `demo-vault/system/skills/weekly-planning/SKILL.md`.
- For reviewing or closing a daily note, use `$daily-review` from `demo-vault/system/skills/daily-review/SKILL.md`.
- For producing a seven-day review, use `$weekly-review` from `demo-vault/system/skills/weekly-review/SKILL.md`.
- For reviewing diet and activity logs, use `$fitness-review` from `demo-vault/system/skills/fitness-review/SKILL.md`.

## Verification

Run `python3 scripts/validate_vault.py` after changes to the demo vault, templates, links, metadata, or skills. Fix failures caused by the requested work before finishing.
