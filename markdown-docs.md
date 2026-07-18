---
title: "Markdown-based Documentation Sites"
description: "Docs-as-code: product and project documentation as markdown files in the repo, published as a site. The pattern every serious dev tool uses, and how to have it."
---

# Markdown-based Docs

Look at the documentation of any tool you respect: Stripe, React, pandoc, take your pick. Underneath, it's the same architecture every time: a folder of markdown in a repo, published as a site. The industry even has a name for it, **docs-as-code**, and it won so thoroughly in developer tooling that nobody argues about it anymore.

The interesting part is that the pattern isn't for developers. It's for anyone whose documentation keeps going stale, which is everyone.

## Why docs rot (and why this fixes it)

Docs rot when updating them lives in a different system from doing the work. The wiki nobody opens, the PDF nobody can edit, the Google Doc with "FINAL v3" in the name. Distance kills accuracy.

Docs-as-code closes the distance:

- **Docs live next to the thing they document.** Change the project, and the doc that describes it is sitting in the same repo, in the same editor, in the same commit.
- **Every contributor can edit them** like any other file, and "edit this page" links let readers propose fixes in one click.
- **Changes get reviewed** like everything else: a [pull request](learn/tutorial-3.md) for the docs is the same motion as for the work.
- **History is total.** When did this instruction change, and why? `git log` knows.

And the 2026 addition: [AI tools read and update markdown directly](markdown-in-chatgpt.md), so "update the docs to match this change" is now a sentence you type rather than a chore you defer.

## The pattern

```
docs/
  index.md          ← docs home
  getting-started/
  guides/
  reference/
```

A publisher renders the folder as a site: sidebar from the structure, search, clean URLs. Callouts, code blocks with highlighting, and [mermaid diagrams](basics.md) all come free with markdown. Need custom layout somewhere? [HTML works](markdown-websites.md).

## The tools

[Flowershow](https://flowershow.app) publishes a docs folder with sidebar navigation and full-text search, straight from the repo. The wider docs-as-code ecosystem: MkDocs (with the Material theme, a docs classic), Docusaurus, GitBook, mdBook for technical books. As ever, they all eat the same markdown folder, so the choice is reversible.

## Getting started

For a project's docs: make `docs/`, write `index.md` and one getting-started page, publish, then grow it one page per recurring question. For standalone documentation, the [website tutorial](learn/index.md) applies directly; a docs site is a website whose pages happen to be instructions.

Related: [wikis & handbooks](markdown-wikis.md) (the internal-facing sibling) · [websites](markdown-websites.md)
