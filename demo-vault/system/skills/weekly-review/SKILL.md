---
name: weekly-review
description: Build a demo weekly review from seven completed daily Summary blocks and Saturday's open tasks. Use when the user requests a weekly review for a specific Sunday-through-Saturday period.
---

# Weekly Review

Work only inside `demo-vault/`.

- Require a specific Sunday-through-Saturday period.
- Read only the seven daily `### Summary` blocks for aggregated sections.
- Copy every unchecked, nonblank Saturday To-do into the review's To-do section without moving it into Sunday.
- Count Work done, Project, People, and Event links by days mentioned.
- Rank food types by days mentioned. Average steps only across days with supplied numeric totals; count other activity by day.
- Describe the chronological Feeling flow in no more than three sentences.
- Sum Input counts by destination without repeating Input wording.
- Use `demo-vault/system/templates/weekly-review-template.md` and do not alter source daily notes.

Write the result to `demo-vault/workbench/shelf/weekly/YYYY-MM-DD-weekly-review.md`, using the Saturday period-end date in the filename.

Report missing daily Summaries rather than silently filling gaps. Run `python3 scripts/validate_vault.py` before finishing.
