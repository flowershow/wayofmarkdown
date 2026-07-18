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

**Team onboarding path** (direct Rufus use case, 2026-07-18: Life Itself newcomers who don't know markdown and need to end up using GitHub + markdown knowledge bases): a single "start here, work through in order" page sequencing basics → tutorial 1 (publish) → tutorial 2 (Obsidian + GitHub Desktop) → KB practices (catalog howto, wiki-links) → collaboration (tutorial 3 when done). Mostly curation of existing material; gaps become new tutorials. Likely absorbs legacy issue #1 (editor guide epic).

## B2. Markdown-based X — a section in its own right (Rufus 2026-07-18)

Elevated from "use-case guides": for *every* X people build with proprietary tools, an entry — stub first, detailed guide over time. Format per entry: what is X (intro for someone who's never named the concept) → the markdown-based pattern → tools out there (Flowershow shows up naturally for publishing; Obsidian for PKM; etc.) → worked walkthrough (deep guides only).

Brainstormed list (slug = SEO: top-level `/markdown-<x>` pages, flat per our IA preference):

| X | Status / notes |
|---|---|
| **Websites** | FLAGSHIP, multi-part, almost a guide-in-itself. Must include **"markdown supports HTML"** as a core part (Rufus: major, underexplained; video Qquv0Qq7luE = editing HTML site with AI). Flowershow features a lot here. Absorbs/reframes MOGF tutorials + legacy #12. |
| **Blogs** | video 0NGvcuXTris (blog listing in 30s) |
| **Knowledge bases / second brain / PKM** | videos CsCVOFn3bMc (Obsidian+PARA), HwkO14-nTwk (AI+git+Obsidian) |
| **Notion replacement** | flagship escape guide; Bases video 0_qr_qQVkxk |
| **Wikis** (team wiki / handbook) | |
| **Docs** (product/project documentation) | |
| **Databases / catalogs** | ✅ essay + catalog howto; unify |
| **Digital gardens** | import digital-garden.md (#50) |
| **Journals / daily notes** | |
| **Bookmarking / web clipping** | video d-Vte5vJCl0 |
| **Books & long-form** | pandoc |
| **Slides / presentations** | Marp, reveal.js — P3 |
| **Forms/CVs/letters** | P3, maybe |
| **A single page/document** | from coggle "5 core areas" (#62): the humblest on-ramp — "put one note/report/article on the web". P2, small page, big funnel value |
| **A landing page** | from coggle: hero, CTA, signup; showcases HTML-in-markdown. P2 |

Also from the coggle mining ([[../coggle-distilled]]): **kb/glossary** (git/GitHub terms for non-devs, question-phrased) and a **git-rescue howto** (unstage/uncommit/merge-conflicts — the newcomer fear trio).

From Rufus 2026-07-18 (roadmap review session):

- **Pluggable markdown** — dedicated entry on fenced ```-blocks as markdown's *plugin system* (mermaid, dataview/Bases, embedded languages): "you can embed entire other tools". Currently only touched in the manifesto's superpowers section. P1-adjacent — it's a distinctive idea we can own.
- **"Why markdown is awesome" — visual one-pager** — the format's core magic (simple/human-readable, plain text, AI-native, pluggable/extensible) presented *visually and concisely*; distinct from why.md (which argues the approach). Candidate landing-page material.
- **Landing-page engagement** (parked, location TBD): tiny manifesto + visual (roadmap slice or the awesome one-pager) as the hook.

## B3. Videos (Rufus 2026-07-18)

@flowershowapp channel reviewed (15 videos; ~10 markdown-general). Plan: a `/videos` section page listing the markdown-relevant ones grouped by topic, **plus** embedded on the relevant guide pages (iframe embeds — which itself demos "markdown supports HTML" 😎). Product-only videos (What is Flowershow, error-syncing, sidebar) stay out.

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
