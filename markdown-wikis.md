---
title: "Markdown-based Wikis & Team Handbooks"
description: "A shared wiki or handbook as markdown files in a git repo: editable by everyone, reviewed via pull requests, with full history for free."
---

# Markdown-based Wikis & Team Handbooks

> [!note]
> Short version for now -- full guide coming.

A wiki is shared, linked, evolving knowledge. The markdown-based version: files + `[[wiki-links]]` in a **git repository** -- which quietly gives you what wiki software has to build: history of every change, who changed what, proposing changes for review (pull requests), and rollback.

**The pattern**: a repo per wiki; index page per section; everyone edits via GitHub's web editor (zero install) or Obsidian locally ([tutorial](learn/tutorial-2.md)); changes to sensitive pages go through PRs ([tutorial](learn/tutorial-3.md)); publish with Flowershow so it reads like a website, not a repo.

This site is itself run this way, and it's how we onboard people at Life Itself -- there's a [step-by-step path](learn/onboarding.md) for team members who've never touched markdown or GitHub.

Related: [knowledge bases](markdown-knowledge-bases.md) · [docs sites](markdown-docs.md)
