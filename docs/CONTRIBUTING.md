# Contributing to RGIG V4

Thank you for helping build the universal AGI/LLM benchmark!

## How to Add a New Field (H–Z)
1. Copy `fields/fieldG.py` as a template (or use `fields/contrib/` for drafts).
2. Implement:
   - `get_prompt()`: Returns the field's prompt template.
   - `get_audit_schema()`: Returns the audit schema (dict).
   - `check_response()`: Validates/scoring logic.
   - `DEMO`: Example dict for demo/batch mode.
3. Add your field to `cmd/rgig.py`'s `FIELD_MODULES` and `DEMO_RESPONSES`.
4. Add a sample log to `/examples/`.
5. Submit a PR with a short description and test run.

## Test Tasks & Peer Review
- Add demo/test data to your field module's `DEMO`.
- Use Tab UI or CLI to generate and export a run bundle.
- Invite reviewers for peer review and consensus.

## Roadmap & Community
- See [main.tex] and [guidance.tex] for the full roadmap.
- Join the Discord or GitHub Discussions for feature requests.
- All contributions are welcome: fields, UI, docs, tests, cloud, peer review.

## Coding Style
- Python 3.10+, type hints preferred.
- Keep modules <100 lines if possible.
- Use JSON/YAML for logs and audits.

## License
Apache 2.0 — open, remixable, and future-proof.

# Contributors

- Project Lead: Your Name Here
- Core Devs: ...
- Community: Add your name here via PR if you contribute a field, test, doc, or feature!

To add yourself, submit a PR updating this section. All contributors will be credited in launch announcements and docs.

See /docs/launch.md for launch checklist and recognition steps. 