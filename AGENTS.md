# Editorial Avatar

- A purpose-driven portrait workflow with a ChatGPT prompt and Codex skill.
- Canonical instructions live in `skills/editorial-avatar/references/workflow.md`; keep `workflow.en.md` aligned as its English translation. `python3 scripts/build_prompt.py` regenerates both ChatGPT prompts. Codex reads the canonical Chinese workflow.
- Python helpers use the standard library. Run `python3 -m unittest discover -s tests -v`, `python3 scripts/build_prompt.py --check`, and `python3 scripts/check_package.py`.
- Docs: `npm ci && npm run build:docs`; README covers usage. SHOWCASE.md / SHOWCASE.en.md and VALIDATION.md / VALIDATION.en.md source the Chinese / English generated HTML pages; their gallery templates live in scripts/showcase.html / scripts/showcase.en.html. The landing pages index.html (EN) and zh.html (中文) are hand-authored and share assets/landing.css. Run `npm run check:docs` before committing docs changes.
- Preserve actual example prompts, ordered references, hashes and observed outcomes. Do not claim stable identity fidelity or superiority without a corresponding comparison.
- Never import private source photographs or local experiment history into this public package. New public examples require known provenance and permission to distribute.
- Current verification status and unresolved checks belong in `VALIDATION.md`, not in these instructions.
