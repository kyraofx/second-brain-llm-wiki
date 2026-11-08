# Daily Review Automation

### Purpose

Close a specified daily note by handling task rollover, Input routing, supported record updates, factual logs, and Summary while preserving Diary exactly.

### Operational source

- Skill: `system/skills/daily-review/SKILL.md`
- Invocation: `$daily-review`
- Daily template: `system/templates/daily-template.md`

### Trigger

- OpenAI scheduled automation
- Runs once near the end of each local day and supplies that day's date to `$daily-review`

### Input

- Explicit target date

### Output

- Idempotent daily close with a compact evidence-based Summary

### Status

Active automation contract. The recurring schedule is configured in OpenAI and intentionally stored outside this demonstration repository.
