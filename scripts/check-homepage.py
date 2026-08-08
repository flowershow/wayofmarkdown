#!/usr/bin/env python3
"""Check the homepage's structural contract.

This is deliberately a source check: Flowershow owns the outer document, while
index.md owns the plain-layout page inside it.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
source = (ROOT / "index.md").read_text()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


frontmatter = source.split("---", 2)[1]
check(re.search(r"^layout:\s*plain\s*$", frontmatter, re.M) is not None,
      "index.md must use layout: plain")
check('class="wom-hero"' not in source,
      "the old wom-hero wrapper must be removed")

title = source.index("<h1")
title_end = source.index("</h1>", title)
mark = source.index('src="/hero-mark.html"')
lede = source.index("Own the source. Compose with anything.", mark)
check(title < title_end < mark < lede,
      "the animated mark must sit immediately between the title and lede")

for heading in ("Why markdown wins", "What will you build?", "Start here"):
    check(heading in source, f"homepage section missing: {heading}")

for destination in (
    "/roadmap", "/basics", "/playground.html", "/markdown-websites",
    "/markdown-knowledge-bases", "/markdown-notion-alternative",
    "/markdown-blogs", "/markdown-databases", "/markdown-wikis",
    "/markdown-digital-gardens", "/markdown-based",
):
    check(f'href="{destination}"' in source,
          f"homepage destination missing: {destination}")

check('w-full max-w-6xl' in source,
      "homepage must have one max-w-6xl page shell")
check('class="wom-home mx-auto w-full max-w-6xl' in source,
      "homepage shell must carry its compatibility hook")
check('</div>\n\n      <div class="overflow-hidden' not in source,
      "nested demo cards must remain in one raw-HTML block")

styles = (ROOT / "custom.css").read_text()
check("#mdxpage .wom-home h1" in styles,
      "plain homepage must override Flowershow's hidden first h1")

print("homepage structure: ok")
