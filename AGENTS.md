# Editorial Avatar

- A purpose-driven portrait workflow with a ChatGPT prompt and Codex skill.
- Shared instructions live in `skills/editorial-avatar/references/workflow.md`; regenerate `prompts/chatgpt.md` with `python3 scripts/build_prompt.py`.
- Python helpers use the standard library. Run `python3 -m unittest discover -s tests -v`, `python3 scripts/build_prompt.py --check`, and `python3 scripts/check_package.py`.
- Docs: `npm ci && npm run build:docs`; README covers usage; SHOWCASE.md is the showcase.html content source; VALIDATION.md is the validation source. showcase.html and validation.html are generated; the layout template lives in scripts/showcase.html. The landing pages index.html (EN) and zh.html (中文) are hand-authored and share assets/landing.css. Run `npm run check:docs` before committing docs changes.
- Preserve actual example prompts, ordered references, hashes and observed outcomes. Do not claim stable identity fidelity or superiority without a corresponding comparison.
- Never import private source photographs or local experiment history into this public package. New public examples require known provenance and permission to distribute.
- Current verification status and unresolved checks belong in `VALIDATION.md`, not in these instructions.
