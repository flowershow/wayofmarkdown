"""Render the default social card: docs/brand/og/default.html -> assets/og/default-2026-10.png.

Uses headless Chrome (macOS path below; set CHROME to override)."""
import os, pathlib, subprocess
root = pathlib.Path(__file__).resolve().parent.parent
chrome = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
src = root / "docs/brand/og/default.html"
out = root / "assets/og/default-2026-10.png"
subprocess.run([chrome, "--headless=new", "--hide-scrollbars", "--window-size=1200,630",
                "--virtual-time-budget=5000", "--allow-file-access-from-files",
                f"--screenshot={out}", src.as_uri()], check=True, capture_output=True)
print("wrote", out.relative_to(root))
