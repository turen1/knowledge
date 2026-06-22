# -*- coding: utf-8 -*-
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"


def main() -> int:
    errors = []

    required = [
        ROOT / "AGENTS.md",
        WIKI / "index.md",
        WIKI / "profile.md",
        WIKI / "preferences.md",
        WIKI / "projects.md",
        WIKI / "workflows.md",
        WIKI / "tools.md",
        WIKI / "timeline.md",
        WIKI / "open-questions.md",
        WIKI / "provenance.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    raw_files = list(RAW.rglob("*.md"))
    if not raw_files:
        errors.append("raw/ has no markdown sources")

    wiki_files = list(WIKI.rglob("*.md"))
    wiki_names = {p.stem for p in wiki_files}
    for path in wiki_files:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[\[([^\]]+)\]\]", text):
            target_name = target.split("#", 1)[0].strip()
            if target_name and target_name not in wiki_names:
                errors.append(f"broken wiki link in {path.relative_to(ROOT)}: [[{target}]]")
        if path.name not in {"index.md", "open-questions.md", "provenance.md"}:
            if "来源：" not in text and "来源：" not in text.replace("`", ""):
                errors.append(f"wiki page lacks source markers: {path.relative_to(ROOT)}")

    if errors:
        print("Knowledge base audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Knowledge base audit passed.")
    print(f"raw files: {len(raw_files)}")
    print(f"wiki files: {len(wiki_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

