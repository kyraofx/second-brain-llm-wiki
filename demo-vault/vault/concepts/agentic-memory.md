---
type: concept
id: CON00001
date: 2026-02-01
summary: "A synthetic concept note explaining how an agent can use explicit files as durable working context."
areas:
  - technology
sensitivity: public
aliases:
  - Agent Memory
people: []
projects:
  - "[[ai-meeting-assistant]]"
tools:
  - "[[obsidian]]"
---

# Agentic Memory
### What It Is
Durable context stored outside a model session so an agent can recover relevant rules, state, and history later.
### How It Works
The system keeps human-readable source files, loads only the context needed for a task, and writes supported changes back to canonical records.
### Core Components
- Stable source files
- Retrieval rules
- Provenance boundaries
- Update and validation workflows
### Examples and Applications
- Remembering project decisions across sessions
- Loading a person profile before recording a new interaction
- Reading recent summaries before preparing a weekly review
### Related Concepts and Tools
- [[obsidian]]
### Sources
- Synthetic explanation created for this public demonstration.
