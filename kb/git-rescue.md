---
title: "Git rescue: undo, unstage, and fix merge conflicts"
description: "I committed the wrong thing, I can't push, there's a merge conflict — calm fixes for the git situations every markdown-site editor eventually hits."
---

# Git rescue 🚑

The three situations that scare every newcomer to a markdown workflow, and the calm way out of each. First, the golden rule: **in git, almost nothing is ever lost.** Commits are snapshots; the scary messages are git being thorough, not your work being gone.

## "I staged / committed something I didn't mean to"

**Staged but not committed** (ticked the wrong file in GitHub Desktop): just untick it. That's unstaging. Nothing happened yet.

**Committed but not pushed**: in GitHub Desktop, right-click the commit → *Undo commit*. Your changes come back as ordinary edits; fix and recommit. (Command line: `git reset --soft HEAD~1`.)

**Committed *and* pushed**: don't try to rewrite history on a shared branch — make a new commit that reverses the old one. GitHub Desktop: right-click the commit → *Revert changes in commit*. This is the polite, safe fix, and nobody will think less of you; revert commits are everywhere in professional projects.

## "There's a merge conflict" 😱

Two people edited the same lines; git wants a human to choose. The file now contains both versions between markers:

```
<<<<<<< HEAD
your version of the line
=======
their version of the line
>>>>>>> main
```

The fix is genuinely this: open the file, decide what the text should say (yours, theirs, or a blend), **delete the marker lines**, save, commit. That's the whole procedure. On a markdown site the conflicts are prose, so *you* are perfectly qualified to resolve them — no developer needed.

Prevention: [pull](glossary.md) before you start editing, keep PRs small, and don't leave branches sitting for weeks.

## "I'm just completely stuck"

The nuclear option that's almost never wrong on a content repo: copy your changed file(s) somewhere safe (your desktop is fine), delete your local copy of the repo, [clone](glossary.md) it fresh, paste your changes back in, commit, push. Inelegant? Slightly. Effective? Completely. Every developer has done it; they just don't mention it.

And the modern option: [AI tools read git](../markdown-in-chatgpt.md) — describe your situation to Claude Code or similar in plain words ("I committed to the wrong branch") and let it drive. Untangling git states is exactly the kind of thing they're good at.

Terms unfamiliar? [The glossary](glossary.md). Never seen a PR? [Tutorial 3](../learn/tutorial-3.md).
