---
title: "Markdown-based Books & Long-form Writing"
description: "Write your book as markdown chapters and publish to everything — PDF, EPUB, print, web — with pandoc and friends. One source, every format, full git history."
---

# Markdown-based Books & Long-form

Books are where proprietary formats hurt most. A decade-old manuscript is a Word-file archaeology dig; an InDesign project opens for exactly one person on exactly one machine. Meanwhile the actual content of a book is the thing markdown handles best: structured prose.

The markdown-based way: a chapter per file, and a converter that turns the folder into every format a book needs.

## The pattern

```
book/
  metadata.yaml        ← title, author, ISBN...
  01-in-the-beginning.md
  02-the-pattern.md
  ...
```

**[pandoc](https://pandoc.org)** is the engine: the universal document converter, turning that folder into PDF (via LaTeX, so it looks properly typeset), EPUB, DOCX for the editor who insists, HTML, and dozens more. One source, every output. Real books ship this way, from O'Reilly titles to PhD theses.

The command is honestly this short:

```bash
pandoc metadata.yaml 0*.md -o book.epub
```

## Why git changes book-writing

Version control sounds like a programmer concern until you've written anything long:

- **Real history**: every draft of every chapter, forever, with the reasons in the commit messages. No `final-FINAL-v3.docx`.
- **Branches for experiments**: try the restructure; keep the old order intact; merge whichever wins.
- **Diffs**: see exactly what changed between drafts, paragraph by paragraph.
- **Collaboration with an editor** via [pull requests](learn/tutorial-3.md): comments anchored to lines, suggestions you accept or reject, all tracked.

Plus everything else in the ecosystem: write in [Obsidian](markdown-in-obsidian.md), let [AI tools](markdown-in-chatgpt.md) critique structure across the whole manuscript at once (a folder of markdown is something an AI can actually *read whole*), and keep research notes wiki-linked next to chapters in the same [knowledge base](markdown-knowledge-bases.md).

## Tool variations

- **Quarto**: pandoc with batteries, great for technical and academic books with executable code
- **mdBook**: what Rust uses for its documentation books; lovely web output
- **Leanpub**: publishes and *sells* books straight from markdown
- **Serialize as you write**: publish chapters to the web with a [markdown website](markdown-websites.md), gather readers before the book exists, then compile the same files into the final artifact

## Starting

Don't set up the toolchain first; that's procrastination with extra steps. Write chapter files in any editor until the writing has momentum, then add `metadata.yaml` and a pandoc command in an afternoon. The files you wrote on day one need no conversion, because they were already the source of truth. That's [the whole idea](manifesto.md) 🚀
