---
name: fitness-review
description: Review the demo Diet Log and Activity Log for a specified date range and provide evidence-linked, non-medical feedback. Use when the user requests a fitness, diet, or activity-log review.
---

# Fitness Review

Work only with the synthetic logs in `demo-vault/workbench/shelf/logs/`.

1. Require a specific date range. Read the Diet Log and Activity Log entries within that range; do not inspect unrelated daily notes or records.
2. Report data coverage separately for diet and activity. Missing entries mean unknown, not failure.
3. Summarize only recorded patterns. Cite the supporting dates near each material observation.
4. Organize the response as:
   - Data coverage
   - Activity patterns
   - Diet patterns
   - What appears to be working
   - One to three practical experiments
   - Important uncertainties or questions
5. Keep feedback supportive and non-medical. Do not diagnose, prescribe treatment, moralize food, or estimate calories, nutrients, portions, exertion, or weight change from missing data.
6. Do not present a short period as a long-term trend. When individualized medical or nutritional assessment is needed, recommend an appropriate qualified professional.

This workflow is read-only unless the user separately requests a specific log correction or another write.
