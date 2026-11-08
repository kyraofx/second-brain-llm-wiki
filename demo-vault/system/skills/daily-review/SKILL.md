---
name: daily-review
description: Review a specified demo daily note by rolling tasks, routing Inputs, updating supported records and logs, and writing Summary. Use when the user requests daily review, daily close, or daily summarization.
---

# Daily Review

Work only inside `demo-vault/`. Read `demo-vault/system/schema.md` before editing.

- Require a specific target date and leave a missing target untouched.
- Sunday through Friday, copy each unchecked nonblank To-do into the next calendar day's To-do without duplicates. On Saturday, leave unchecked tasks for Weekly Review.
- Route each nonblank Input to an established planning destination when the intended destination is clear. Preserve the original Input and append its destination link. When routing remains ambiguous, preserve the Input in place and report the unresolved decision.
- Treat Diary as immutable user writing. Never edit, correct, append to, reformat, or insert links into Diary.
- Build Summary from Workflow and Diary only. Use this order when supported: Work done, Project, Diet, Activity, Feeling, People, Event, Input. Omit empty categories and never infer completion from Plan, To-do, Reminders, or Inputs.
- Update an established canonical record instead of creating a duplicate. New durable records require the next unused type-prefixed ID.
- Synchronize only explicitly supplied diet and activity details into the corresponding logs. Never estimate.
- Replace only the content beneath the target note's `### Summary` heading.

Verify task rollover, routed links, Summary order, unique IDs, logs, and unchanged Diary text. Run `python3 scripts/validate_vault.py` before finishing.
