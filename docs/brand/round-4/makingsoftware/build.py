"""Assemble ms.html from ms.src.html, the round-3 opt4 sketches and iso.svg."""
import re, pathlib, subprocess
here = pathlib.Path(__file__).parent
opt4 = here.parent.parent / "round-3" / "opt4"
subprocess.run(["python3", str(here / "iso.py")], check=True)
sk = (opt4 / "sketches.html").read_text()
F = {m.group(1): m.group(2).strip() for m in re.finditer(r"<!--([A-Z_]+)-->\n(.*?)\n<!--/\1-->", sk, re.S)}
F["TWOVIEWS"] = (opt4 / "twoviews.svg").read_text()
F["ISO"] = (here / "iso.svg").read_text()
out = (here / "ms.src.html").read_text()
for k, v in F.items(): out = out.replace("{{%s}}" % k, v)
assert "{{" not in out
(here / "ms.html").write_text(out); print("built ms.html", len(out))
