#!/usr/bin/env python3
"""Check wikilinks and relative markdown links across published site content.

Usage: python3 scripts/link-check.py    (checks all site *.md; docs/, .claude/ excluded)
Exit code 1 if any link is broken. Code spans/fences are ignored.
"""
import glob
import os
import re
import sys


def main():
    mdfiles = [f for f in glob.glob("**/*.md", recursive=True)
               if not f.startswith((".", "docs/", "scripts/", "node_modules"))]
    names = set()
    for f in glob.glob("**/*", recursive=True):
        if os.path.isfile(f):
            names.add(os.path.splitext(os.path.basename(f))[0])
            names.add(os.path.basename(f))
    problems = []
    for f in mdfiles:
        text = open(f).read()
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for m in re.finditer(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", text):
            t = m.group(1).strip()
            base = os.path.basename(t)
            if base not in names and os.path.splitext(base)[0] not in names:
                problems.append((f, "wikilink", t))
        for m in re.finditer(r"(?<!\!)\[[^\]]*\]\(([^)#\s]+)\)", text):
            t = m.group(1)
            if t.startswith(("http", "mailto:", "/")):
                continue
            p = os.path.normpath(os.path.join(os.path.dirname(f), t))
            if not (os.path.exists(p) or os.path.exists(p + ".md")):
                problems.append((f, "rellink", t))
    for p in problems:
        print("%s  [%s]  %s" % p)
    print(f"{len(mdfiles)} files checked, {len(problems)} broken links")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
