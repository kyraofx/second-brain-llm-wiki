# Second-brain schema

`demo-vault/` is a synthetic example vault. Markdown is the source of truth.

| Area | Purpose |
|---|---|
| `workbench/` | Daily capture, active work, planning, and logs |
| `vault/` | Durable canonical records |
| `system/` | Schema, vocabulary, and templates |

### Authority and preservation

- Preserve source wording, uncertainty, and attribution.
- Distinguish user statements, sourced facts, and agent synthesis.
- Diary text is immutable to the agent.
- Unknown values stay blank or are omitted; never invent metadata to fill a template.
- Use one canonical note per durable identity and update it instead of creating a duplicate.
- Preserve ambiguous material in its source note and surface the unresolved routing decision. Do not create a catch-all holding area.

### Names and IDs

- New filenames use lowercase kebab-case. Daily filenames use `YYYY-MM-DD.md`.
- Durable records use permanent type-prefixed IDs followed by five digits.
- IDs advance within their type and are never reused.

| Record | Prefix |
|---|---|
| Concept | `CON` |
| Conversation | `CVO` |
| Event | `EVE` |
| How-to | `HOW` |
| Organization | `ORG` |
| Person | `PER` |
| Place | `PLC` |
| Podcast | `POD` |
| Project | `PRJ` |
| Tool | `TOL` |
| Video | `VID` |

### Daily notes

Daily notes contain Plan, To-do, Reminders, Workflow, Inputs, Diary, and Summary.

- Plan and To-do use Markdown checkboxes.
- Reminders are plain bullets and are not tasks or Summary evidence.
- Workflow records work actually performed.
- Inputs preserve free-form captures and may receive routing links.
- Diary remains byte-for-byte user-authored.
- Summary is compact, evidence-based, and ordered: Work done, Project, Diet, Activity, Feeling, People, Event, Input.

### Public-demo constraint

Every populated record in this repository uses fictional data and `sensitivity: public`. Private or restricted records belong in a separate, non-public system.

### System resources

- `system/templates/` defines visible starting structures for records.
- `system/agents/` documents the Vault Manager and Fitness Advisor, their responsibilities, and their boundaries. These notes are descriptive and do not activate a running agent.
- `system/skills/` contains the executable workflows used by compatible agents.
- `system/automations/` documents the triggers, inputs, and outputs used by OpenAI scheduled automations. Live schedules are configured in OpenAI and are not stored in the vault.
- Repository-level `AGENTS.md` contains project-wide policy and points agents to the workflows in `system/skills/`.
