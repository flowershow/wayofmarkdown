"""Render the site's logo and homepage sketches as standalone SVG files.

Sources live in docs/brand/ (not published); outputs go to assets/logo/ and
assets/sketches/ (published). Re-run after changing a source:

    python3 scripts/build-site-art.py

The logo is the brush # (docs/brand/hash-brush.svg) cut out of an orange seal,
round 5 option D. It is a placeholder until the logo thread decides
(docs/plans/2026-10-03-logo-brief.md). The sketches are served as <img>, so
page CSS can't reach them: colours and fonts are baked in here.
"""
import re, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
brand = root / "docs/brand"
ACC, TEXT = "#ff5a00", "#cc4400"
TINT, TINT2 = "#ffefe6", "#ffd6c0"  # orange at ~12% and ~26% on white
MONO = "'IBM Plex Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SERIF = "Newsreader,'Iowan Old Style',Charter,Georgia,serif"

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print("wrote", path.relative_to(root))

# --- logo: brush # in an orange seal ---
paths = "".join(re.findall(r"<path[^>]*>", (brand / "hash-brush.svg").read_text()))
seal = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="The Way of Markdown">'
        f'<rect width="100" height="100" fill="{ACC}"/>'
        f'<svg x="12" y="12" width="76" height="76" viewBox="-4 -4 108 108" fill="#fff">{paths}</svg></svg>\n')
write(root / "assets/logo/seal.svg", seal)

# --- sketches ---
sk = (brand / "round-3/opt4/sketches.html").read_text()
S = {m.group(1): m.group(2).strip() for m in re.finditer(r"<!--([A-Z_]+)-->\n(.*?)\n<!--/\1-->", sk, re.S)}
S["TWOVIEWS"] = (brand / "round-3/opt4/twoviews.svg").read_text().strip()
S["ISO"] = (brand / "round-4/makingsoftware/iso.svg").read_text().strip()

ISO_CSS = f"""
.side{{fill:{TINT2};stroke:{ACC};stroke-width:1}}
.pl,.top{{fill:#fff;fill-opacity:.94;stroke:{ACC};stroke-width:1.2}}
.base{{fill:{TINT};stroke:{ACC};stroke-width:1.2}}
.tint{{fill:{TINT};stroke:{ACC};stroke-width:1}}
.ln{{stroke:{ACC};stroke-width:1.4;stroke-linecap:round}}
.ln.soft{{stroke-opacity:.55}}
.node{{fill:{TINT};stroke:{ACC};stroke-width:1.2}}
.guide{{stroke:{ACC};stroke-width:1;stroke-dasharray:5 5;opacity:.7}}
.lead{{stroke:{ACC};stroke-width:1}}
.arr{{fill:{ACC}}}
.on{{fill:{TEXT};font-family:{MONO}}}
.lab{{fill:{TEXT};font-family:{MONO};font-size:10px;letter-spacing:.08em}}
"""

def standalone(svg, css=""):
    svg = svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
    svg = svg.replace("#ffd3bb", TINT2).replace("#ffe6d6", TINT)
    svg = re.sub(r'font-family="JetBrains Mono[^"]*"', f'font-family="{MONO}"', svg)
    svg = re.sub(r'font-family="Inter[^"]*"', f'font-family="{SERIF}"', svg)
    if css:
        svg = re.sub(r"(<svg[^>]*>)", lambda m: m.group(1) + f"<style>{css}</style>", svg, count=1)
    return svg + "\n"

for key, name in [("ISO", "inside-a-markdown-file"), ("TWOVIEWS", "one-file-two-views"), ("FORCES", "two-forces")]:
    write(root / f"assets/sketches/{name}.svg", standalone(S[key], ISO_CSS if key == "ISO" else ""))
