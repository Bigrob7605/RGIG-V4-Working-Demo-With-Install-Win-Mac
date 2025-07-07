# RGIG V4 Quickstart

## 1. Install
- Python 3.10+ (Windows/Mac/Linux)
- pip install -r requirements.txt
- (Optional) Docker: `docker pull bigrob7605/rgig:latest`
- Node.js (for Tab UI): `npm install` in /tab-ui/

## 2. Doctor & Setup
- `rgig doctor` — checks your system, suggests fixes
- `rgig quickstart` — generates config for your environment (Mini/Normal/Advanced/Max/Cloud/Tab)

## 3. Run a Benchmark
- CLI: `rgig run --path=mini --fields=A,B --model=api`
- Tab Mode: `rgig tab-mode` (then open browser at http://localhost:8080)
- Cloud: `rgig cloud launch` (see /docker/ or Colab)

## 4. Peer Review & Audit
- **Tab UI Peer Review Tab 2.0:** Assign reviewers, enter scores/comments, see consensus and outliers, export consensus logs for transparency.
- Review YAML/JSON logs in /examples/
- Use Tab Mode or CLI to invite reviewers
- Export a run bundle for sharing or audit

## 5. Screenshots & Video
- See `/docs/screenshots/` and `/docs/video/` for onboarding and marketing assets.
- Use these in your own docs, blog, or social posts.

## 6. Community Launch
- Share on Twitter, Discord, and GitHub Discussions.
- Open issues for "field H–Z" ideas and feature requests.
- Blog/tutorial: See `/docs/` for ready-to-share guides.

## 7. Auto-Upgrade & Field Import
- Drop new field modules into `/fields/` or `/fields/contrib/` for instant expansion.
- No code changes needed—just import and run.

## 8. CI/CD Integration
- All PRs are tested and linted via GitHub Actions.
- See `/tests/` for sample test cases and CI config.

## 9. More
- [Field Reference](../fields/)
- [Tab UI](../tab-ui/)
- [Docker/Cloud Setup](../docker/)
- [Examples & Logs](../examples/)
- [Contributing](CONTRIBUTING.md) 