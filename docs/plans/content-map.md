---
title: "Plan: content map"
publish: false
---

# Content map

Created 2026-07-18. Status: **draft for review**. Priorities follow [[marketing]] (Searcher volume first, escape/use-case guides second, philosophy as the linkable layer). Voice: per #58, draft in Rufus's register, not AI-polish.

Reorientation (Rufus 2026-07-18): markdown + its ecosystem is the headline; Flowershow appears *inside* guides as the publish step, not as the story. Existing MOGF tutorials stay as-is for now.

## A. Markdown Everywhere — hub + "Markdown in X" series

**Hub page** (`everywhere.md`, nav item): logo grid of apps that speak markdown, tiered — *Full support* / *Partial/quirky* / *Name and shame* (Apple Notes desktop 👀). Each logo links to its article. Doubles as the shareable "look how far markdown has spread" artifact.

Spoke articles — format: how to enable/use, what's supported, quirks & limits, copy-in/copy-out tricks, next-step link. ✅ = exists in kb (fold into series, maybe expand).

P1 (high search volume × weak competition × we can write today):
1. WhatsApp — huge "whatsapp formatting" volume; markdown-ish syntax
2. Discord — big; markdown subset + code blocks
3. Slack — good story: "mrkdwn", the quirky dialect
4. Google Docs ✅ (expand: tips + export quirks note ✅)
5. Notion — import/export angle, doubles as escape-hatch article
6. ChatGPT / Claude / AI chats — "why does AI output markdown" + how to use it
7. Obsidian — the PKM flagship; gateway to use-case guides
8. Apple Notes ✅ / iPad Notes ✅ (merge into one "Apple and markdown" saga — good name-and-shame material)

P2: GitHub (competitive but table-stakes), Reddit, Telegram, Substack, Gmail/Google Chat, Confluence, MS Teams, Word (Copilot markdown), Bear, iA Writer, Craft, VS Code, Linear, Jira. Plus converter-intent pages: "Google Docs → markdown" ✅-ish, "HTML → markdown" (Turndown ✅, into.md ✅), "Word/docx → markdown" (pandoc).

## B. Learn — basics + the markdown-based way

**Basics** (Searcher + Team lead):
- `basics.md` ✅ — already ≈ the Datopian playbook intro (same text; diff & merge its extra links). Improve into a proper standalone tutorial: examples, try-it prompts, cheatsheet section.
- Later (P3, competitive with markdownguide.org): per-syntax reference pages (tables, links, images, footnotes…). Only if Search Console shows appetite.

**Use-case guides — "How to X with markdown"** (Escaper; the site's real point). Format: what you get, the pattern, tools (Flowershow as *a* publish option), worked example.

P1:
1. **Replace Notion with markdown** — flagship escape guide; pattern = files + frontmatter + views (Obsidian Bases etc.); links markdown-database essay
2. **Build a knowledge base / second brain** — Obsidian-centric, publishing optional

P2: 3. Make a website ✅ (MOGF tutorials, reframed as one guide entry) · 4. Small database/catalog ✅ (catalog howto + pattern essay, unify) · 5. Blog · 6. Digital garden (import digital-garden.md from flowershow notes/, #50) · 7. Docs site · 8. Team wiki/handbook · 9. Journal/daily notes · 10. Books & long-form (pandoc).

## C. Why / essays (Builder + PKM; the linkable layer)

- Manifesto ✅ — revise into Rufus's voice (#58) before any launch push
- Why markdown-based ✅ — voice pass
- The Markdown Database Pattern ✅ — HN candidate as-is
- P2 imports/new: PKM-wave essay (flowershow notes/, #50), digital gardens, "Markdown is eating the world", History of markdown + timeline (inbox #45)
- Interview series lands here or in own section (see [[marketing]] §3)

## D. Site chrome to support all this

- Nav gains **Everywhere**; kb "Markdown in Apps" section becomes the series (kb keeps tools/workflows/reference)
- Hub↔spoke internal linking; every spoke ends with one next step (usually a use-case guide)
- `llms.txt` + sitemap + Search Console (see [[marketing]])

## Priority queue (proposed build order)

| # | Item | Section |
|---|---|---|
| 1 | Everywhere hub page (logo grid + tiers) | A |
| 2–6 | WhatsApp, Discord, Slack, Notion, AI-chats articles | A |
| 7 | Apple Notes saga (merge ✅s) + Obsidian article | A |
| 8 | basics.md upgrade | B |
| 9 | Replace-Notion guide | B |
| 10 | Knowledge-base guide | B |
| 11 | Manifesto voice revision (#58) | C |
| 12 | llms.txt, sitemap, Search Console | D |

Then: launch moment (HN etc., per [[marketing]] §5), then P2 by observed demand.
