#!/usr/bin/env python3
"""Check local Markdown links and the integrity of recorded image-generation inputs."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def check():
    errors = []
    for path in ROOT.rglob("*.md"):
        if any(part in ("node_modules", ".git", "build") for part in path.relative_to(ROOT).parts):
            continue
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            parsed = urlsplit(link.strip("<>"))
            if parsed.scheme or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"Broken or escaping link: {path.relative_to(ROOT)} -> {link}")
    manifest = json.loads((ROOT / "examples/manifest.json").read_text(encoding="utf-8"))
    for artifact in manifest["artifacts"]:
        path = (ROOT / artifact["path"]).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append(f"Missing or escaping artifact: {artifact['path']}")
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            errors.append(f"Changed artifact: {artifact['path']}")
    recorded = {entry["path"] for entry in manifest["artifacts"]}
    for run in manifest["runs"]:
        for name in [run["prompt"], run["output"]] + [ref["path"] for ref in run["inputs"]]:
            if name not in recorded:
                errors.append(f"Unrecorded run input/output: {name}")
    observations = json.loads((ROOT / "tests/chatgpt-observations.json").read_text(encoding="utf-8"))
    prompt = ROOT / observations["prompt_file"]
    if hashlib.sha256(prompt.read_bytes()).hexdigest() != observations["prompt_sha256"]:
        errors.append("ChatGPT prompt has changed since the recorded observations; update validation status")
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print(f"Local links and {len(recorded)} artifact hashes verified")


if __name__ == "__main__":
    check()
