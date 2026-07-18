---
title: "How to use Markdown in Reddit"
description: "Reddit has supported markdown for over a decade: bold, links, lists, tables, spoilers, superscript. How to switch to Markdown mode and the syntax that works."
---

# How to use Markdown in Reddit

Reddit is one of markdown's oldest homes: comments and posts have spoken it since the late 2000s, long before it was fashionable. (Fitting, given Reddit co-founder Aaron Swartz helped create markdown itself.)

## Switching to markdown mode

The modern editor defaults to a rich-text toolbar ("fancy pants editor", genuinely its name). For real markdown, look for **"Markdown Editor"** in the top-right of the comment/post box and click to switch. Old-school `old.reddit.com` is markdown-only, which is one reason power users never left.

## The syntax

| You type | You get |
|---|---|
| `**bold**` / `*italic*` | **bold** / *italic* |
| `~~strikethrough~~` | ~~strikethrough~~ |
| `[text](url)` | proper links -- yes, real markdown links in a chat-adjacent app! |
| `- item` / `1. item` | lists (nest with 4 spaces) |
| `> quote` | block quote |
| `` `code` `` / 4-space indent | inline code / code block |
| `# heading` | headings (posts especially) |
| `\|col\|col\|` | tables (supported in posts and comments) |
| `>!spoiler!<` | click-to-reveal spoiler (Reddit-only) |
| `^superscript` or `^(multi word)` | superscript (Reddit-only, beloved of ^tiny ^jokes) |

That's a generous implementation: proper links, tables *and* headings put Reddit ahead of [WhatsApp](markdown-in-whatsapp.md), [Slack](markdown-in-slack.md) and most chat tools.

## Quirks

- New-editor code blocks use fences in Markdown mode, but old.reddit only reliably renders 4-space indents. When in doubt, indent.
- Nested quoting plus lists can render differently between old and new Reddit. Preview before posting anything elaborate.
- No images inline via markdown syntax in comments on most subreddits; upload or link instead.

## The workflow point

Because Reddit speaks standard-ish markdown, drafts move freely: write a long post in [Obsidian](markdown-in-obsidian.md), keep it in your [knowledge base](markdown-knowledge-bases.md), paste it in. Get an [AI to tighten it](markdown-in-chatgpt.md) on the way. Your best comments and posts can live in *your* files, not just in Reddit's archive -- which, as with [every platform](everywhere.md), is the difference between writing you own and writing you've lent out.
