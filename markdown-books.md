---
title: "Markdown-based Books & Long-form Writing"
description: "Write your book in markdown and publish to anything — PDF, EPUB, print, web — via pandoc. One source, every format."
---

# Markdown-based Books & Long-form

> [!note]
> Short version for now -- full guide coming.

Books are where proprietary formats hurt most: a decade of Word-file archaeology, or an InDesign project only one person can open. The markdown-based way: a chapter per file, and **pandoc** -- the universal document converter -- turns the folder into PDF, EPUB, DOCX, LaTeX, HTML... one source, every output.

**The pattern**: `chapters/01-beginning.md` onward; a metadata file for title/author; pandoc (or tools built on it) for output; git for the priceless part -- real version history of a manuscript, and branches for experiments.

Whole books, theses and O'Reilly titles ship this way. Serialize it to the web as you write with a [markdown website](markdown-websites.md), then compile the same files into the book.
