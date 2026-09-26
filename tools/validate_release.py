#!/usr/bin/env python3
"""Validate the Portfolio Builder repository and portable plugin package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "issybi-portfolio-builder"
SKILL = PLUGIN / "skills" / "data-portfolio-builder"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "PORTFOLIO_BUILDER_LITE.md",
        ROOT / ".agents" / "plugins" / "marketplace.json",
        ROOT / "docs" / "PRIVACY.md",
        ROOT / "docs" / "TERMS.md",
        ROOT / "docs" / "SUPPORT.md",
        ROOT / "submission" / "listing.md",
        ROOT / "submission" / "starter-prompts.md",
        ROOT / "submission" / "test-cases.md",
        ROOT / "submission" / "release-notes.md",
        PLUGIN / "plugin.json",
        SKILL / "SKILL.md",
        SKILL / "references" / "planning-framework.md",
        SKILL / "references" / "project-modes.md",
    ]
    for path in required:
        require(path.is_file(), f"Missing required file: {path.relative_to(ROOT)}")

    manifest = load_json(PLUGIN / "plugin.json")
    require(
        manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "Unexpected plugin schema",
    )
    require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest.get("name", "")) is not None, "Plugin name must be kebab-case")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")) is not None, "Plugin version must use semantic versioning")

    interface = manifest["extensions"]["com.openai"]["interface"]
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        require(bool(interface.get(field)), f"Missing interface field: {field}")
    for field in ("composerIcon", "logo"):
        relative = interface[field]
        require(relative.startswith("./"), f"{field} must use a ./-relative path")
        require((PLUGIN / relative[2:]).is_file(), f"Missing asset referenced by {field}: {relative}")
    for relative in interface.get("screenshots", []):
        require(relative.startswith("./"), "Screenshot path must start with ./")
        require((PLUGIN / relative[2:]).is_file(), f"Missing screenshot: {relative}")

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    require(skill_text.startswith("---\nname: data-portfolio-builder\n"), "Skill front matter name is missing or changed")
    require("description:" in skill_text.split("---", 2)[1], "Skill front matter description is missing")
    for link in re.findall(r"\]\((references/[^)]+)\)", skill_text):
        require((SKILL / link).is_file(), f"Broken SKILL.md reference: {link}")

    tests = (ROOT / "submission" / "test-cases.md").read_text(encoding="utf-8")
    require(len(re.findall(r"^## Positive ", tests, flags=re.MULTILINE)) == 5, "Submission must contain exactly five positive tests")
    require(len(re.findall(r"^## Negative ", tests, flags=re.MULTILINE)) == 3, "Submission must contain exactly three negative tests")

    secret_patterns = {
        "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() in {".png", ".xlsx", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in secret_patterns.items():
            require(pattern.search(text) is None, f"Possible {label} found in {path.relative_to(ROOT)}")

    print("Release structure, manifest references, skill links, test counts, and secret scan passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, json.JSONDecodeError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

