import re, pathlib
here=pathlib.Path(__file__).parent
sk=(here/"sketches.html").read_text()
F={m.group(1):m.group(2).strip() for m in re.finditer(r"<!--([A-Z_]+)-->\n(.*?)\n<!--/\1-->",sk,re.S)}
F["TWOVIEWS"]=(here/"twoviews.svg").read_text()
for src in here.glob("*.src.html"):
    out=src.read_text()
    for k,v in F.items(): out=out.replace("{{%s}}"%k,v)
    assert "{{" not in out, src
    (here/src.name.replace(".src.html",".html")).write_text(out); print("built",src.name)
