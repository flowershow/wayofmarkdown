---
title: "How to use Markdown in Slack — and why it's weird (mrkdwn)"
description: "Slack supports markdown-style formatting but with its own dialect called mrkdwn: single-asterisk bold, no headings, and a hidden setting you should know about."
---

# How to use Markdown in Slack (and why it's weird)

Slack does markdown. Sort of. Slack actually speaks its own dialect -- literally called **`mrkdwn`** in their docs, vowels sold separately -- and knowing where it differs will save you some mangled messages.

## The syntax

| You type | You get |
|---|---|
| `*bold*` | **bold** (single asterisks!) |
| `_italic_` | *italic* |
| `~strikethrough~` | ~~strikethrough~~ |
| `` `inline code` `` | `inline code` |
| ```` ``` ```` | code block (no syntax highlighting) |
| `> quote` | block quote |
| `- item` or `1. item` | lists |

## First: check your settings

Slack has a setting that changes everything: **Preferences → Advanced → "Format messages with markup"**. Switched on, your typed characters format on send, markdown-style. Switched off (the default for many), Slack gives you a WYSIWYG toolbar and *intercepts* some markdown as you type. If you live in markdown, turn it on -- Slack becomes much less annoying.

## The dialect traps

- **Single-asterisk bold** -- same trap as [WhatsApp](markdown-in-whatsapp.md). Paste standard `**bold**` into Slack and you get stray asterisks.
- **No headings.** `# Big point` just prints the hash. Convention: a bold line instead.
- **No markdown links.** `[text](url)` doesn't work in chat; paste URLs bare, or use the WYSIWYG link button. (Bots and apps *can* send `<url|text>` -- angle brackets, because why not.)
- **Code blocks don't highlight.** Fine for snippets, sad for anything long.

## Copying in and out

Pasting rendered rich text into Slack mostly converts okay. Pasting *raw* markdown gets you the bold trap and literal `#` characters. The fix, as ever, is [asking an AI to convert](markdown-in-chatgpt.md) -- "make this Slack-friendly" -- or keeping your canonical text in real markdown and translating at the edge.

That last bit is the actual lesson here: keep the source of truth in plain, standard markdown *you* own, and treat each app's dialect as an output format. Your docs shouldn't live in Slack anyway -- Slack is where things go to scroll away. A [markdown knowledge base](markdown-based.md) is where they should live.

More apps and their accents: [markdown everywhere](everywhere.md) 🌍
