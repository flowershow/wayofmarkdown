---
title: "How to use Markdown in Telegram"
description: "Telegram supports markdown-style formatting in chats — bold, italic, code, spoilers — with quirks per platform, plus a full MarkdownV2 dialect for bots."
---

# How to use Markdown in Telegram

Telegram does markdown in two quite different places: typing in chats, and the bot API. Regular users get a workable subset; bot builders get a whole dialect with its own rulebook.

## Typing in chats

On desktop and mobile these work as you type (send to apply):

| You type | You get |
|---|---|
| `**bold**` | **bold** |
| `__italic__` | *italic* |
| `` `code` `` | `code` |
| ```` ```block``` ```` | code block |
| `~~strikethrough~~` | ~~strikethrough~~ |
| `\|\|spoiler\|\|` | tap-to-reveal spoiler |

Note the accent: double-underscore for *italic* (not single, like most apps), double-asterisk for bold. Exact support varies a little between Telegram Desktop, iOS and Android, and there's no heading/list/quote syntax; for structure you're back to plain text conventions. The selection toolbar (select text → Format) covers the same ground if syntax fails you.

## The bot API: MarkdownV2

Bots sending messages can use **MarkdownV2**, a stricter, richer dialect: `*bold*` (single asterisk this time; yes, different from the chat box, we don't make the rules), `_italic_`, `__underline__`, `~strikethrough~`, `||spoiler||`, inline links `[text](url)`, and code blocks with language hints. The catch: nearly every special character you *don't* mean as formatting must be escaped with `\`, which surprises every bot developer exactly once. If you're building bots that relay markdown content (from a feed, a repo, [an AI](markdown-in-chatgpt.md)), budget for an escaping step.

## The takeaway

Telegram is a solid mid-table citizen of [the markdown world](everywhere.md): real formatting via familiar syntax, its own accent, no structural elements. Fine for chat; not a place to *keep* writing. Draft anything that matters in [your own files](markdown-knowledge-bases.md) and paste it in; the conversion pain is mild, and [AI handles it](markdown-in-chatgpt.md) when it isn't.
