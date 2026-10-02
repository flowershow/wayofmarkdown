#!/usr/bin/env python3
"""Inline shared figures from figs.html into *.src.html -> *.html"""
import re, pathlib
here = pathlib.Path(__file__).parent
figs = (here/"figs.html").read_text()
F = {m.group(1): m.group(2).strip() for m in re.finditer(r"<!--(FIG\d)-->\n(.*?)\n<!--/\1-->", figs, re.S)}
for src in here.glob("*.src.html"):
    out = src.read_text()
    for k, v in F.items(): out = out.replace("{{%s}}" % k, v)
    assert "{{" not in out, src
    (here/src.name.replace(".src.html", ".html")).write_text(out)
    print("built", src.name)
