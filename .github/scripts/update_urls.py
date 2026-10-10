"""
Keep Graphviz image URLs in sync with the inline dot code in Markdown files.

A block is processed when its FIRST line is:    // graphviz: NAME
For every block, the script maintains one link-reference line in the same file:

    [NAME]: https://kroki.io/graphviz/svg/<encoded diagram>#fragment

and your image line simply uses it:

    ![Weighted graph][NAME]

No .dot or .svg files are created. The diagram is rendered by a Kroki server
when the page is viewed. Works inside GitHub callouts (> [!NOTE]) too.
"""
import base64
import pathlib
import re
import sys
import zlib

# Change this if you self-host Kroki, e.g. "http://localhost:8000/graphviz/svg/"
KROKI_BASE = "https://kroki.io/graphviz/svg/"

# Files / folders that are never scanned (they contain syntax examples only)
SKIP_FILES = {"README.md"}
SKIP_DIRS = {"docs", ".github", ".git", "node_modules"}

BLOCK = re.compile(r"```dot\n//\s*graphviz:\s*([\w-]+)[ \t]*\n(.*?)\n```", re.S)


def encode(code: str) -> str:
    return base64.urlsafe_b64encode(zlib.compress(code.encode("utf-8"), 9)).decode("ascii")


def decode(token: str) -> str:
    token += "=" * (-len(token) % 4)
    return zlib.decompress(base64.urlsafe_b64decode(token)).decode("utf-8")


def default_fragment(name: str) -> str:
    if name.endswith("-light"):
        return "#gh-light-mode-only"
    if name.endswith("-dark"):
        return "#gh-dark-mode-only"
    return ""


changed_files = 0
errors = 0

for md in sorted(pathlib.Path(".").rglob("*.md")):
    if md.name in SKIP_FILES or any(part in SKIP_DIRS for part in md.parts):
        continue

    original = md.read_text(encoding="utf-8")
    # Strip blockquote / callout prefixes so fenced code inside callouts is found
    stripped = "\n".join(re.sub(r"^\s*>\s?", "", ln) for ln in original.splitlines())

    text = original
    seen = set()
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
            old_url = found.group(1)
            base, _, frag = old_url.partition("#")
            frag = ("#" + frag) if frag else ""
            try:
                if decode(base.rsplit("/", 1)[-1]) == code:
                    print(f"Up to date: {name}  ({md})")
                    continue
            except Exception:
                pass  # old URL unreadable, rebuild it
            new_line = f"[{name}]: {KROKI_BASE}{encode(code)}{frag}"
            text = text[: found.start()] + new_line + text[found.end():]
            print(f"Updated:    {name}  ({md})")
        else:
            new_line = f"[{name}]: {KROKI_BASE}{encode(code)}{default_fragment(name)}"
            text = text.rstrip("\n") + "\n\n" + new_line + "\n"
            print(f"Added:      {name}  ({md})")

    if text != original:
        md.write_text(text, encoding="utf-8")
        changed_files += 1

print(f"Done: {changed_files} file(s) changed, {errors} error(s)")
sys.exit(1 if errors else 0)
