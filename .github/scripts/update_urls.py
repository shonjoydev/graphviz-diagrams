"""
Keeps Graphviz image URLs in sync with inline dot code in Markdown files.

A ```dot block is rendered when its FIRST line is:   // graphviz: NAME
The script maintains one line in the same file:      [NAME]: https://kroki.io/graphviz/svg/...
and your image line uses it:                         ![alt][NAME]

No .dot or .svg files are created.
"""
import base64
import pathlib
import re
import sys
import zlib

# Self-hosting Kroki? Change this, e.g. "http://localhost:8000/graphviz/svg/"
KROKI_BASE = "https://kroki.io/graphviz/svg/"
SKIP_DIRS = {".github", ".git", "node_modules"}

BLOCK = re.compile(r"```dot\n//\s*graphviz:\s*([\w-]+)[ \t]*\n(.*?)\n```", re.S)


def encode(code):
    return base64.urlsafe_b64encode(zlib.compress(code.encode("utf-8"), 9)).decode("ascii")


def decode(token):
    token += "=" * (-len(token) % 4)
    return zlib.decompress(base64.urlsafe_b64decode(token)).decode("utf-8")


changed, errors = 0, 0

for md in sorted(pathlib.Path(".").rglob("*.md")):
    if any(part in SKIP_DIRS for part in md.parts):
        continue

    original = md.read_text(encoding="utf-8")
    # Ignore blockquote / callout prefixes ("> ") so blocks inside callouts work too
    stripped = "\n".join(re.sub(r"^\s*>\s?", "", ln) for ln in original.splitlines())

    text, seen = original, set()
    for name, code in BLOCK.findall(stripped):
        if name in seen:
            print(f"ERROR: duplicate name '{name}' in {md}")
            errors += 1
            continue
        seen.add(name)

        code = code.strip("\n") + "\n"
        ref = re.compile(rf"^\[{re.escape(name)}\]:[ \t]*(\S+)[ \t]*$", re.M)
        found = ref.search(text)

        if found:
            base, _, frag = found.group(1).partition("#")
            frag = ("#" + frag) if frag else ""
            try:
                if decode(base.rsplit("/", 1)[-1]) == code:
                    print(f"Up to date: {name} ({md})")
                    continue
            except Exception:
                pass
            line = f"[{name}]: {KROKI_BASE}{encode(code)}{frag}"
            text = text[: found.start()] + line + text[found.end():]
            print(f"Updated:    {name} ({md})")
        else:
            frag = "#gh-light-mode-only" if name.endswith("-light") else \
                   "#gh-dark-mode-only" if name.endswith("-dark") else ""
            text = text.rstrip("\n") + f"\n\n[{name}]: {KROKI_BASE}{encode(code)}{frag}\n"
            print(f"Added:      {name} ({md})")

    if text != original:
        md.write_text(text, encoding="utf-8")
        changed += 1

print(f"Done: {changed} file(s) changed, {errors} error(s)")
sys.exit(1 if errors else 0)
