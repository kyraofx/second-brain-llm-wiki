# Demo walkthrough

This scenario uses only the fictional records in `demo-vault/`.

### 1. Weekly planning

Prompt:

> Synchronize the demo week of February 1–7, 2026.

Expected behavior:

- Preserve all seven existing daily notes.
- Merge calendar entries, recurring schedule commitments, and weekday habits without duplicates.
- Keep the February 5–6 mentor call explicitly tentative.

### 2. Daily review

Prompt:

> Review the February 2 daily note idempotently.

Expected behavior:

- Roll the unfinished project task into February 3 without duplicating it.
- Route the transcription-provider Input to the established [[ai-meeting-assistant]] project.
- Update the project and Maya's dated interaction when supported.
- Synchronize supplied diet and activity details.
- Write a compact Summary.
- Preserve Diary byte-for-byte.

### 3. Fitness review

Prompt:

> Review the Diet Log and Activity Log for February 1–7, 2026.

Expected behavior:

- Report diet and activity data coverage separately.
- Ground observations in recorded dates.
- Treat missing information as unknown rather than failure.
- Avoid diagnoses, invented calorie estimates, and prescriptive medical advice.

### 4. Evidence

Show the Git diff, then run:

```bash
python3 scripts/validate_vault.py
```

The demonstration should distinguish the repository's working skills and automation contracts from the live schedules configured separately in OpenAI.
