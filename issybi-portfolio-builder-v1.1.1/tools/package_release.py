#!/usr/bin/env python3
"""Build local source, skill and portable-plugin archives; does not publish/install."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "issybi-portfolio-builder"
SKILL = PLUGIN / "skills" / "data-portfolio-builder"

def archive(source, destination, prefix, exclude=()):
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as z:
        for item in sorted(source.rglob("*")):
            if item.is_symlink():
                raise ValueError(f"Symlinks are not packaged: {item}")
            rel = item.relative_to(source)
            if not item.is_file() or any(p in exclude for p in rel.parts):
                continue
            z.write(item, str(Path(prefix) / rel))
    with zipfile.ZipFile(destination) as z:
        if z.testzip() is not None:
            raise ValueError(f"Corrupt archive: {destination}")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT / "tools" / "validate_release.py")], check=True)
    version = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))["version"]
    out = args.output.resolve()
    if out.is_relative_to(ROOT) and out != ROOT / "dist":
        raise ValueError("Use dist/ or an output directory outside the repository")
    out.mkdir(parents=True, exist_ok=True)
    items = [
        (PLUGIN, out / f"issybi-portfolio-builder-plugin-v{version}.zip", PLUGIN.name, ("__pycache__",)),
        (SKILL, out / f"data-portfolio-builder-skill-v{version}.zip", SKILL.name, ("__pycache__",)),
        (ROOT, out / f"issybi-portfolio-builder-source-v{version}.zip", f"issybi-portfolio-builder-v{version}", (".git", "dist", "__pycache__")),
    ]
    hashes = {}
    for source, destination, prefix, exclude in items:
        archive(source, destination, prefix, exclude)
        hashes[destination.name] = hashlib.sha256(destination.read_bytes()).hexdigest()
        print(f"Built and CRC-checked: {destination.name}")
    (out / "SHA256SUMS.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
