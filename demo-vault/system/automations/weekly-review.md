# Weekly Review Automation

### Purpose

Synthesize a completed Sunday-through-Saturday period from seven daily Summary blocks and Saturday's open tasks.

### Operational source

- Skill: `system/skills/weekly-review/SKILL.md`
- Invocation: `$weekly-review`
- Review template: `system/templates/weekly-review-template.md`

### Trigger

- OpenAI scheduled automation
- Runs after the expected Saturday Daily Review window and supplies the completed Sunday-through-Saturday period to `$weekly-review`

### Inputs

- Explicit Sunday-through-Saturday period
- Seven daily Summary blocks
- Saturday's unchecked To-dos

### Output

- `workbench/shelf/weekly/YYYY-MM-DD-weekly-review.md`, dated with the Saturday period end

### Status

Active automation contract. The recurring schedule is configured in OpenAI and intentionally stored outside this demonstration repository.
