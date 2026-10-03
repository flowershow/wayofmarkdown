"""Build round 5: the recommended direction (Way Into AI base, orange, with
Making Software's contents, guide sidebar, exploded figure and pixel #).

Fills {{KEYS}} in page.src.html from the opt4 sketches, the round-4 exploded
figure and the logo marks, and writes page.html.
"""
import re, pathlib
here = pathlib.Path(__file__).parent
brand = here.parent
opt4 = brand / "round-3/opt4"

sk = (opt4 / "sketches.html").read_text()
F = {m.group(1): m.group(2).strip() for m in re.finditer(r"<!--([A-Z_]+)-->\n(.*?)\n<!--/\1-->", sk, re.S)}
F["TWOVIEWS"] = (opt4 / "twoviews.svg").read_text()
F["ISO"] = (brand / "round-4/makingsoftware/iso.svg").read_text()

hash_svg = (brand / "hash-brush.svg").read_text()
F["HASH_SYMBOL"] = '<symbol id="hash" viewBox="-4 -4 108 108">' + "".join(re.findall(r"<path[^>]*>", hash_svg)) + "</symbol>"

# pixel # on an 8x8 grid: two columns, two rows, each one cell thick.
# Whole cells only, so it stays sharp at 16px (2px a cell) and 32px.
cells = {(x, y) for y in range(8) for x in (2, 5)} | {(x, y) for x in range(8) for y in (2, 5)}
rects = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for x, y in sorted(cells))
def pix(cls, px=None, seal=False):
    size = f' width="{px}" height="{px}"' if px else ""
    if seal:
        return (f'<svg class="{cls}" viewBox="-2 -2 12 12"{size} shape-rendering="crispEdges" aria-hidden="true">'
                f'<rect x="-2" y="-2" width="12" height="12" style="fill:var(--acc)"/><g style="fill:#fff">{rects}</g></svg>')
    return f'<svg class="{cls}" viewBox="0 0 8 8"{size} shape-rendering="crispEdges" aria-hidden="true"><g style="fill:var(--acc)">{rects}</g></svg>'
def brush(cls, px=None):
    size = f' width="{px}" height="{px}"' if px else ""
    return f'<svg class="{cls}" viewBox="0 0 100 100"{size} aria-hidden="true"><use href="#hash" width="100" height="100" style="fill:var(--ink)"/></svg>'

F["PIX"] = pix("mk")
F["SEAL"] = pix("mk", seal=True)
F["BRUSH"] = brush("mk")
for px in (32, 16):
    F[f"PIX_{px}"] = pix("fv", px)
    F[f"SEAL_{px}"] = pix("fv", px, seal=True)
    F[f"BRUSH_{px}"] = brush("fv", px)

src = (here / "page.src.html").read_text()
for k, v in F.items():
    src = src.replace("{{%s}}" % k, v)
assert "{{" not in src, re.findall(r"\{\{[A-Z_0-9]+\}\}", src)
(here / "page.html").write_text(src)
print("built page.html", len(src))
