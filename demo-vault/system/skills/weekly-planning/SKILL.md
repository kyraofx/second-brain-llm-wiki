---
name: weekly-planning
description: Prepare a requested span of demo daily notes from the calendar, recurring schedule, and weekly habits. Use when planning or synchronizing a week in `demo-vault`.
---

# Weekly Planning

Work only inside `demo-vault/`.

1. Resolve the user's requested date range. If dates are missing, ask rather than inferring a real personal schedule.
2. Read `demo-vault/system/templates/daily-template.md` and create only missing target notes in `demo-vault/workbench/daily/`. Never overwrite an existing note.
3. Preserve current Plan and To-do content and avoid exact or meaningfully equivalent duplicates.
4. Add dated Events, Hangouts, and Other entries from `workbench/wall/planning/calendar.md` to the matching Plan as unchecked checkboxes. Preserve supplied time, location, and uncertainty.
5. Add recurring commitments from `schedule.md` to matching weekdays.
6. Add only the `### Weekly` items from `habits.md`, mapped to their stated weekdays. Do not copy the weekly count into the activity label.
7. Preserve the template's `#### Reminders` subsection without populating it unless the user explicitly supplies reminder text for the target period.

Do not modify planning source files, Diary, Workflow, Inputs, or Summary. Plan items are intentions and never evidence of completion.

Verify every target date, weekday mapping, tentative label, and duplicate check before reporting the synchronized range.
