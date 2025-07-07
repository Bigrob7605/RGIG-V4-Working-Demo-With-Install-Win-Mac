# RGIG V4 Launch Checklist

## 1. Full-System Testing (All Platforms)
- Tab UI: Test all fields (A–G) in single and batch mode
- Verify Peer Review tab: assign reviewers, enter scores/comments, export consensus logs
- Confirm export/import matches CLI output format
- Test responsiveness on desktop, mobile, tablet
- Try demo data, screenshots, and onboarding flow
- CLI: Run `python -m cmd.rgig --batch` and `python -m cmd.rgig --demo`
- Confirm all fields, audits, and exports work cleanly
- Validate error handling for missing/invalid input
- Field Import/Auto-Upgrade: Drop a new module in /fields/ or /fields/contrib/, confirm CLI and Tab UI autodetect
- Peer Review: Upload/export consensus logs, trigger outlier detection, confirm reviewer display
- Docs & Examples: Follow README and Quickstart from a fresh clone—flag any unclear or missing steps
- Check /docs/screenshots/ and /docs/video/ rendering in Markdown/docs

## 2. Cleanup
- Remove/archive obsolete files, test artifacts, placeholder modules
- Confirm /examples/, /tests/, /docker/ run as described in docs
- Double-check CI/CD (GitHub Actions) triggers and test matrix

## 3. Installer/Setup Scripts
- For Python/CLI: Use setup.sh (Linux/Mac) or setup.bat (Windows)
  - Creates venv, installs requirements, runs smoke test
  - Optional: one-liner install with pipx or python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
- For Tab UI: All HTML/JS/CSS is drag-and-drop—no build step
- Document in README: "Just open tab-ui/index.html in your browser."

## 4. Final Review
- Confirm all contributors are credited in /docs/CONTRIBUTING.md
- Review and finalize this checklist and /README.md
- Announce in your chosen channels: "RGIG V4 is live!"

## 5. Team/Community
- Work through this checklist step-by-step
- Report bugs, usability snags, or missing features as GitHub issues
- Clean up repo and commit any final tweaks before public launch
- Begin work on installer scripts once tests are 100% green

---

See README.md and /docs/quickstart.md for user steps. 