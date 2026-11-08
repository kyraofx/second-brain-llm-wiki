---
type: how-to
id: HOW00001
date: 2026-02-02
summary: "Run the synthetic weekly-planning workflow and verify its results."
areas:
  - technology
sensitivity: public
aliases: []
people: []
projects:
  - "[[ai-meeting-assistant]]"
---

# How to Run Weekly Planning

1. Start an agent session from the repository root.
2. Ask it to prepare February 1–7, 2026.
3. Confirm it reads [[calendar]], [[schedule]], and [[habits]].
4. Review the created daily notes and Git diff.
5. Run `python3 scripts/validate_vault.py` from the repository root.

The workflow is successful when existing content remains intact, missing notes are created, and every planning source is mapped without duplicates.
