# RGIG V4 — Reality Grade Intelligence Gauntlet

**The one tool to test them all.**

RGIG V4 is the universal, modular, idiot-proof AGI/LLM benchmarking suite. Run it anywhere: Windows, Mac, Linux, browser tab, or the cloud. Benchmark any model—API, local, or browser LLMs (ChatGPT, Claude, Gemini, etc.).

## Features
- Modular CLI and Tab Mode (browser)
- One-command cloud launch (Docker, Colab, AWS/GCP/Azure)
- Peer review, audit, and consensus tools
- Pluggable fields (A–G, H–Z coming)
- YAML/JSON logs, checksummed for transparency

## Quickstart
1. **Install**
   - Python 3.10+, pip, Docker (optional), Node (for Tab UI)
   - Or just use the all-in-one Docker image
2. **Run**
   - `rgig doctor` — check your setup
   - `rgig quickstart` — generate config
   - `rgig run --path=mini --fields=A,B` — run a test
   - `rgig tab-mode` — launch browser UI for ChatGPT/Claude/Gemini
   - `rgig cloud launch` — start a cloud instance
3. **Review**
   - Peer review, merge, and export results

## Docs
- [Quickstart Guide](docs/quickstart.md)
- [Field Reference](fields/)
- [Tab UI](tab-ui/)
- [Docker/Cloud Setup](docker/)
- [Examples & Logs](examples/)
- [Contributing](docs/CONTRIBUTING.md)

## License
Apache 2.0 — open, remixable, and future-proof.

# Launch Checklist

- [ ] Test all fields (A–G) in CLI and Tab UI (single, batch, demo)
- [ ] Verify Peer Review tab: assign reviewers, export consensus logs, outlier detection
- [ ] Confirm CLI/Tab UI export/import match
- [ ] Test on desktop, mobile, tablet
- [ ] Try demo data, screenshots, onboarding flow
- [ ] Validate error handling and field import/auto-upgrade
- [ ] Follow README/Quickstart from fresh clone
- [ ] Check /docs/screenshots/ and /docs/video/ rendering
- [ ] Remove obsolete files, confirm /examples/, /tests/, /docker/
- [ ] Check CI/CD (GitHub Actions) triggers/tests
- [ ] Run setup.sh (Linux/Mac) or setup.bat (Windows) for easy install
- [ ] For Tab UI: just open tab-ui/index.html in your browser
- [ ] Credit all contributors in /docs/CONTRIBUTING.md
- [ ] Announce launch!  

See /docs/launch.md for full details. 