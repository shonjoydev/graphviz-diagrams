"""
Render inline Graphviz blocks in Markdown files to SVG.

A block is rendered when its FIRST line is:   // graphviz: NAME
Output:  <folder of the .md file>/diagrams/NAME.svg

Works inside GitHub callouts (> [!NOTE]) too.
"""
import re
import subprocess
import sys
import pathlib

# Files / folders that are never scanned (they contain syntax examples only)
SKIP_FILES = {"README.md"}
SKIP_DIRS = {"docs", ".github", ".git", "node_modules"}

PATTERN = re.compile(r"```dot\n//\s*graphviz:\s*([\w-]+)[ \t]*\n(.*?)\n```", re.S)

errors = 0
rendered = 0

for md in sorted(pathlib.Path(".").rglob("*.md")):
    if md.name in SKIP_FILES or any(part in SKIP_DIRS for part in md.parts):
        continue

    text = md.read_text(encoding="utf-8")
    # Remove blockquote / callout prefixes ("> ") so fenced code inside them is found
    text = "\n".join(re.sub(r"^\s*>\s?", "", line) for line in text.splitlines())

    seen = set()
    for name, code in PATTERN.findall(text):
        if name in seen:
            print(f"ERROR: duplicate name '{name}' in {md}")
            errors += 1
            continue
        seen.add(name)

        out = md.parent / "diagrams" / f"{name}.svg"
        out.parent.mkdir(exist_ok=True)
        result = subprocess.run(
            ["dot", "-Tsvg", "-o", str(out)],
            input=code, text=True, capture_output=True,
        )
        if result.returncode != 0:
            print(f"ERROR: failed to render '{name}' from {md}\n{result.stderr}")
            errors += 1
        else:
            print(f"Rendered {out}  (from {md})")
            rendered += 1

print(f"Done: {rendered} rendered, {errors} errors")
sys.exit(1 if errors else 0)
