---
title: "Markdown-based Documentation Sites"
description: "Product and project docs as markdown files: the pattern every serious dev tool already uses, and how to have it too."
---

# Markdown-based Docs

> [!note]
> Short version for now -- full guide coming.

Every serious developer tool documents itself the same way: a `docs/` folder of markdown in the project repo, published as a site. Docs-as-code -- versioned with the code it documents, edited in PRs, "edit this page" links for readers.

**The pattern**: `docs/` folder; sidebar from folder structure; a publisher on top (Flowershow, MkDocs, Docusaurus, GitBook...). Search, navigation and theming come from the tool; the content stays portable markdown.

**Why it wins**: docs rot when updating them is a separate system from doing the work. When the docs live next to the code/project and every contributor can edit them like any other file, they stay closer to true. Plus [AI can read and update them directly](markdown-in-chatgpt.md).

Related: [websites](markdown-websites.md) · [wikis](markdown-wikis.md)
