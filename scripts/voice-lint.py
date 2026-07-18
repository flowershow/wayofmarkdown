#!/usr/bin/env python3
"""Voice lint for wayofmarkdown content.

Mechanical checks from the write-like-me skill (banned words, AI anti-patterns,
dash density). A clean pass is a floor, not a guarantee of voice - see
.claude/skills/write-like-me/references/voice-profile.md.

Usage: python3 scripts/voice-lint.py [files-or-globs...]   (default: all site *.md)
Exit code 1 if any file has findings.
"""
import glob
import re
import sys

BANNED_WORDS = [
    r"\bdelve", r"\brealm\b", r"\btapestr", r"\bleverag(e|ing)\b", r"\butili[sz]e",
    r"\bfacilitat", r"\bendeavou?r\b", r"\bseamless", r"\bempower", r"\bstakeholder",
    r"game.chang", r"cutting.edge", r"revolutioni[sz]", r"\btransformative\b",
    r"paradigm shift", r"\bsynerg", r"\belevate\b", r"\bsupercharge",
    r"In today'?s \w+ (world|landscape|environment|era|age)",
    r"[Ll]et'?s (dive|unpack)", r"[Aa]t the end of the day",
    r"[Ii]t'?s (important|worth) (to note|noting)", r"\bIn summary\b", r"[Aa]s we'?ve seen",
    r"\bgold ?mine\b", r"\btreasure trove\b", r"\bunlock(s|ed|ing)? the\b",
]

BANNED_PATTERNS = [
    # negation flips: "It's not X -- it's Y" / "isn't about X. It's about Y"
    (r"(?i)(it|this|that)('s| is)( really| actually)? not [^.\n]{2,60}[.;,]?\s*[-–—]*\s*(it|this|that)('s| is)",
     "negation flip (It's not X - it's Y)"),
    (r"(?i)n[o']t (just |really |only )?about [^.\n]{2,60}\.\s*It'?s about", "negation flip (not about X. It's about Y)"),
    # unearned profundity / false buildup
    (r"(?i)\band that changes everything\b", "unearned profundity"),
    (r"(?i)\bsomething shifted\b", "unearned profundity"),
    (r"\?\s*It'?s simpler than", "false buildup"),
    (r"(?i)\bhere'?s the (thing|secret|kicker)\b", "false buildup"),
    # rhetorical question as transition
    (r"(?i)but what does (this|that) (really )?mean\?", "rhetorical-question transition"),
]

DASH_DENSITY_LIMIT = 1.6  # em/spaced dashes per 100 words


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)  # frontmatter
    return text


def lint_file(path):
    findings = []
    raw = open(path).read()
    text = strip_code(raw)
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if "voice-lint-ok" in line:
            continue
        for pat in BANNED_WORDS:
            if re.search(pat, line):
                findings.append((i, f"banned word/phrase: {pat}", line.strip()[:80]))
        for pat, label in BANNED_PATTERNS:
            if re.search(pat, line):
                findings.append((i, label, line.strip()[:80]))
    prose = "\n".join(l for l in lines if not re.match(r"\s*[-*|>#]", l))
    words = len(re.findall(r"\w+", prose))
    dashes = len(re.findall(r"—|–| -- | - (?=\w)", prose))
    if words > 150 and dashes / words * 100 > DASH_DENSITY_LIMIT:
        findings.append((0, f"dash density {dashes / words * 100:.1f}/100w (limit {DASH_DENSITY_LIMIT})", ""))
    return findings


def main():
    args = sys.argv[1:]
    if args:
        files = []
        for a in args:
            files.extend(glob.glob(a, recursive=True))
    else:
        files = [f for f in glob.glob("**/*.md", recursive=True)
                 if not f.startswith((".", "docs/", "node_modules"))]
    total = 0
    for f in sorted(files):
        findings = lint_file(f)
        if findings:
            total += len(findings)
            print(f"\n{f}")
            for line_no, label, excerpt in findings:
                loc = f":{line_no}" if line_no else ""
                print(f"  {loc:>5}  {label}" + (f"  | {excerpt}" if excerpt else ""))
    print(f"\n{len(files)} files checked, {total} findings")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
