# Weekly Planning Automation

### Purpose

Prepare a requested span of daily notes from the calendar, recurring schedule, and weekly habits.

### Operational source

- Skill: `system/skills/weekly-planning/SKILL.md`
- Invocation: `$weekly-planning`
- Daily template: `system/templates/daily-template.md`

### Trigger

- OpenAI scheduled automation
- Runs once before the upcoming Sunday-through-Saturday planning period and supplies its date range to `$weekly-planning`

### Inputs

- Explicit target date range
- Calendar, schedule, Weekly habits, and existing target notes

### Output

- Missing daily notes created from the template
- Existing Plan and To-do content preserved
- Planning sources synchronized without duplicates

### Status

Active automation contract. The recurring schedule is configured in OpenAI and intentionally stored outside this demonstration repository.
