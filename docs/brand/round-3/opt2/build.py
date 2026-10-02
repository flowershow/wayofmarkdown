import re, pathlib
here=pathlib.Path(__file__).parent
figs=(here/"figs.html").read_text()
F={m.group(1):m.group(2).strip() for m in re.finditer(r"<!--(FIG\d)-->\n(.*?)\n<!--/\1-->",figs,re.S)}
F["TABLEFIG"]=(here/"tablefig.svg").read_text()
# recolour: blue -> orange, grid -> light grey, serif labels -> Inter
def rc(v): return v.replace("#2449d8","#ff5a00").replace("#c9d2f0","#e4e4e4").replace("Source Serif 4,serif","Inter,sans-serif")
for src in here.glob("*.src.html"):
    out=src.read_text()
    for k,v in F.items(): out=out.replace("{{%s}}"%k,rc(v))
    assert "{{" not in out, src
    (here/src.name.replace(".src.html",".html")).write_text(out); print("built",src.name)
