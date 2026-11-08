# Architecture

The project separates user-facing knowledge from agent operating instructions.

```text
Natural capture
      ↓
workbench/ ──→ Agent Skills ──→ vault/
      │              │             │
      └──── planning and logs ─────┘
                     ↓
                  system/
```

### Layers

- `workbench/` contains daily capture, active planning, and supporting logs.
- `vault/` contains durable canonical records with stable IDs.
- `system/` defines the schema, controlled vocabulary, templates, roles, automations, and skills.
- `system/skills/` defines repeatable agent workflows over the knowledge layers.

Ambiguous material remains in its source note until the user or agent has enough context to route it confidently. The public architecture intentionally has no catch-all holding area.

Markdown remains the source of truth. Obsidian provides navigation and editing, while Git provides history and review. Derived indexes or interfaces must remain disposable and rebuildable.
