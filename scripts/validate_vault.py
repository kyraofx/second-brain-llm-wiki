#!/usr/bin/env python3
"""Validate structural and public-safety invariants in the demo vault."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VAULT_ROOT = REPO_ROOT / "demo-vault"
DURABLE_ROOT = VAULT_ROOT / "vault"
DAILY_ROOT = VAULT_ROOT / "workbench" / "daily"

ID_RE = re.compile(r"^[A-Z]{3}\d{5}$")
FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
DAILY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
ABSOLUTE_PATH_PATTERNS = (
    re.compile(r"/Users/[^/\s]+"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+"),
    re.compile(r"file://"),
)

TYPE_PREFIX = {
    "concept": "CON",
    "conversation": "CVO",
    "project": "PRJ",
    "person": "PER",
    "event": "EVE",
    "how-to": "HOW",
    "organization": "ORG",
    "place": "PLC",
    "podcast": "POD",
    "tool": "TOL",
    "video": "VID",
}

DAILY_HEADINGS = (
    "### Plan",
    "### To-do",
    "#### Reminders",
    "### Workflow",
    "### Inputs",
    "### Diary",
    "### Summary",
)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([a-z][a-z0-9-]*):\s*(.*)$", line)
        if match:
            result[match.group(1)] = match.group(2).strip().strip('"')
    return result


def main() -> int:
    errors: list[str] = []
    markdown_files = sorted(REPO_ROOT.rglob("*.md"))
    vault_markdown = sorted(VAULT_ROOT.rglob("*.md"))
    stems: dict[str, list[Path]] = defaultdict(list)
    ids: dict[str, Path] = {}

    for path in vault_markdown:
        stems[path.stem].append(path)

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(REPO_ROOT)
        for pattern in ABSOLUTE_PATH_PATTERNS:
            if pattern.search(text):
                errors.append(f"{relative}: contains a machine-specific absolute path")
                break

    for path in sorted(DURABLE_ROOT.rglob("*.md")):
        relative = path.relative_to(REPO_ROOT)
        if not FILENAME_RE.fullmatch(path.name):
            errors.append(f"{relative}: filename is not lowercase kebab-case")

        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        record_type = meta.get("type", "")
        record_id = meta.get("id", "")

        if record_type not in TYPE_PREFIX:
            errors.append(f"{relative}: unsupported or missing type")
        if not ID_RE.fullmatch(record_id):
            errors.append(f"{relative}: missing or invalid permanent ID")
        elif record_id in ids:
            errors.append(
                f"{relative}: duplicate ID {record_id} also used by "
                f"{ids[record_id].relative_to(REPO_ROOT)}"
            )
        else:
            ids[record_id] = path

        expected_prefix = TYPE_PREFIX.get(record_type)
        if expected_prefix and not record_id.startswith(expected_prefix):
            errors.append(f"{relative}: {record_id} does not match type {record_type}")
        if meta.get("sensitivity") != "public":
            errors.append(f"{relative}: populated demo records must be public")

    for path in sorted(DAILY_ROOT.glob("*.md")):
        relative = path.relative_to(REPO_ROOT)
        if not DAILY_RE.fullmatch(path.name):
            errors.append(f"{relative}: daily filename must be YYYY-MM-DD.md")
        text = path.read_text(encoding="utf-8")
        positions = [text.find(heading) for heading in DAILY_HEADINGS]
        if any(position < 0 for position in positions):
            errors.append(f"{relative}: missing one or more canonical daily headings")
        elif positions != sorted(positions):
            errors.append(f"{relative}: daily headings are out of order")

    for path in vault_markdown:
        if "templates" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(REPO_ROOT)
        for target in WIKILINK_RE.findall(text):
            normalized = Path(target.strip()).name
            if normalized not in stems:
                errors.append(f"{relative}: broken wikilink [[{target}]]")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Validation passed: {len(vault_markdown)} vault Markdown files, "
        f"{len(ids)} durable IDs, {len(list(DAILY_ROOT.glob('*.md')))} daily notes."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
