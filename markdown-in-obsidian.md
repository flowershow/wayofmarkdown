---
title: "Markdown in Obsidian — the app that is markdown"
description: "Obsidian doesn't 'support' markdown, it IS markdown: plain files on your disk with a beautiful editor on top. What it adds, and why that matters."
---

# Markdown in Obsidian

Most apps on [the everywhere list](everywhere.md) *support* markdown. Obsidian is different: it **is** markdown. There's no database, no cloud copy of your notes, no export step. An Obsidian "vault" is a folder of `.md` files on your disk, and the app is a beautiful editor pointed at them.

This distinction matters more than any feature. Quit Obsidian forever and your notes are still there, readable in anything. That's why it has become the trusted centre of the markdown world, and the editor we recommend throughout this site.

## What Obsidian gives you

- **Live preview**: write `**bold**` and see bold, while the file stays plain markdown underneath. Toggle source mode to see the raw text anytime.
- **`[[Wiki-links]]`**: type `[[` and link to any note, with autocomplete. The glue of [knowledge bases](markdown-knowledge-bases.md).
- **Backlinks and graph view**: every note shows what links *to* it; the graph shows your whole web of notes.
- **Properties (frontmatter)**: structured fields on any note, edited in a friendly panel, stored as plain YAML frontmatter in the file.
- **Bases**: database views (tables, cards, filters) over your notes' properties. This is [the markdown database pattern](markdown-database.md) with a native UI, and a fair chunk of a [Notion replacement](markdown-notion-alternative.md) on its own.
- **Canvas, templates, daily notes, and a few thousand plugins** for whatever's missing.

## The dialect notes

Obsidian speaks CommonMark plus GitHub-flavoured extensions, plus a few of its own that other tools may not render:

- `[[wiki-links]]` and `![[embeds]]` (transclusion: embed one note, or an image, inside another)
- `> [!note]` callouts (styled boxes; several types)
- `%%comments%%` that don't render

If your notes will also be published or read elsewhere, know which tools understand these. Flowershow renders wiki-links, embeds and callouts properly (much of this site uses them); plain CommonMark tools won't.

## Using it well

Start simple: a folder, some notes, links between them ([the 30-minute setup](markdown-knowledge-bases.md)). Add [git and GitHub](learn/howtos/publish-obsidian-vault-to-github.md) for history and sync. Point [an AI tool at the vault](kb/ai-editing.md) and let it tidy, link and draft with you. Publish the good parts [with Flowershow](https://www.youtube.com/watch?v=2jOYg0wCg1s), straight from inside Obsidian.

Sync between devices: Obsidian Sync is the paid official option and is good; git does it free with a little setup; iCloud/Dropbox work for the casual case. Files, remember. They go where files go.

The one caution: the plugin garden is deep and a certain kind of person (hello) loses a fortnight to configuring it. The notes are the point. Plain markdown plus links gets you 90% of the value 😎
