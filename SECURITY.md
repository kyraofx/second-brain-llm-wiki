# Security and privacy

This repository must contain synthetic demonstration material only.

### Reporting

If you find a credential, personal identifier, private record, or machine-specific path, do not reproduce it in a public issue. Contact the repository owner privately and identify the affected path with the minimum necessary detail.

### Maintainer rules

- Never copy a live personal vault into this repository.
- Never commit secrets, API keys, access tokens, private logs, or agent memory.
- Build examples from fictional records with `sensitivity: public`.
- Run `python3 scripts/validate_vault.py` before every release.
- Review the complete Git history—not only the current working tree—before publication.
