"""Build the round-4 brief: Way Into AI's design for The Way of Markdown.

Pulls the opt4 sketches (recoloured at runtime by CSS so they follow the
accent switcher) and the brush hash, fills {{KEYS}} in page.src.html and
writes page.html.
"""
import re, pathlib
here = pathlib.Path(__file__).parent
brand = here.parent.parent
opt4 = brand / "round-3/opt4"

sk = (opt4 / "sketches.html").read_text()
F = {m.group(1): m.group(2).strip() for m in re.finditer(r"<!--([A-Z_]+)-->\n(.*?)\n<!--/\1-->", sk, re.S)}
F["TWOVIEWS"] = (opt4 / "twoviews.svg").read_text()

hash_svg = (brand / "hash-brush.svg").read_text()
paths = "".join(re.findall(r"<path[^>]*>", hash_svg))
F["HASH_SYMBOL"] = f'<symbol id="hash" viewBox="-4 -4 108 108">{paths}</symbol>'

INK = "fill:var(--ink)"
ACC = "fill:var(--acc)"
LOGOS = {
    "a": f'<use href="#hash" width="100" height="100" style="{INK}"/>',
    "b": f'<use href="#hash" width="100" height="100" style="{ACC}"/>',
    "c": f'<rect width="100" height="100" rx="8" style="{ACC}"/><use href="#hash" x="13" y="13" width="74" height="74" style="fill:#fff"/>',
    "d": '<path d="M63 8.5 A43 43 0 1 1 29 13.5" fill="none" stroke-width="7" stroke-linecap="round" style="stroke:var(--acc)"/>'
         f'<use href="#hash" x="24" y="24" width="52" height="52" style="{INK}"/>',
    "e": f'<use href="#hash" x="0" y="12" width="74" height="74" style="{INK}"/><rect class="caret" x="80" y="24" width="13" height="52" style="{ACC}"/>',
    "f": f'<use href="#hash" width="100" height="100" style="{INK}"/><circle cx="49.5" cy="51" r="7" style="{ACC}"/>',
}
for k, body in LOGOS.items():
    K = k.upper()
    F[f"LOGO_{K}"] = f'<svg viewBox="0 0 100 100" aria-hidden="true">{body}</svg>'
    for px in (48, 32, 16):
        F[f"LOGO_{K}_{px}"] = f'<svg viewBox="0 0 100 100" width="{px}" height="{px}" aria-hidden="true">{body}</svg>'
# the nav carries all six; the switcher shows one
F["LOGO_A_NAV"] = "".join(f'<svg class="l{k}" viewBox="0 0 100 100" aria-hidden="true">{b}</svg>' for k, b in LOGOS.items())

src = (here / "page.src.html").read_text()
for k, v in F.items():
    src = src.replace("{{%s}}" % k, v)
assert "{{" not in src, re.findall(r"\{\{[A-Z_]+\}\}", src)
(here / "page.html").write_text(src)
print("built page.html", len(src))
