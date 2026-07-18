---
title: "Plan: product, users & marketing"
publish: false
---

# Product, users & marketing plan

Created 2026-07-18. Status: **draft for review**. Companion: [[content-map]] (which this plan's priorities feed).

## 1. What is the product?

The Way of Markdown is a **content/authority product**, not a tool: the reference site for the markdown-based way of working. Its jobs, in order of traffic volume:

1. **Answer a task query** — "how do I use markdown in Google Docs/WhatsApp/Slack?" (most visitors, arriving via search, one page, in and out)
2. **Guide an escape** — "how do I replace Notion / build a knowledge base / publish my notes without lock-in?" (fewer visitors, much higher engagement)
3. **Articulate the philosophy** — manifesto, essays; the linkable, shareable identity layer
4. **Feed the ecosystem** — quietly route builders to tools, Flowershow among them (secondary, per Rufus 2026-07-18: don't go on about Flowershow)

Strategic value beyond itself: SEO/authority asset for the ecosystem, a movement focal point ("X ❤️ Markdown"), long-term funnel and credibility for Flowershow/Datopian/Rufus — without being branded as such.

## 2. Who are the users?

| Persona | Who | They want | They find us via | We serve them with |
|---|---|---|---|---|
| **Searcher** | Anyone with a markdown task, often non-technical | Quick answer | Google/AI answers ("markdown in X") | Markdown-in-X articles + hub |
| **Escaper** | Sophisticated non-dev tired of Notion/Evernote/CMS lock-in | A credible path out | "notion alternative markdown", essays, word of mouth | Use-case guides, markdown-database pattern |
| **PKM enthusiast** | Obsidian/digital-garden crowd | Patterns, validation, new tricks | Reddit (r/ObsidianMD, r/PKMS), HN, newsletters | Essays, guides, interviews |
| **Builder** | Devs & tool-makers in the markdown ecosystem | A flag to rally to; reference material | HN, GitHub, each other | Manifesto, badges, interviews, reference |
| **Team lead** | Small org adopting markdown workflows (orig. Life Itself use case) | A curriculum to point people at | The above people recommending it | Learn track end-to-end |

The **Searcher** funds the site with traffic and authority; the **Escaper + PKM enthusiast** are the real audience for the mission; the **Builder** supplies backlinks and legitimacy. Content priorities should serve Searcher volume first (SEO base), mission audience second, always with a next-step link from the former to the latter.

## 3. Discovery: how they find us

### SEO (primary engine)
- **Hub & spoke**: "Markdown Everywhere" hub page → per-app "How to use Markdown in X" articles. Each spoke targets a real query ("discord markdown", "whatsapp formatting markdown", "markdown in google docs"). Long-tail, high-intent, mostly weak competition (official docs + thin listicles).
- **Escape queries**: "notion alternative markdown", "markdown knowledge base", "plain text second brain" — use-case guides.
- Title/meta discipline: descriptive, query-matching page titles (brand carries no keywords — by design, see [[../naming]]).
- Basics: sitemap, Search Console from day one, internal linking hub↔spokes, one topic per page.

### AI answer engines (the 2026 twist)
People increasingly ask ChatGPT/Claude instead of Google. Plays: be the cleanest, most-citable source (structured headings, direct answers up top); add `llms.txt`; the site *being* markdown is itself the pitch — make raw .md easily accessible. On-message and nearly free.

### Communities & launches (episodic spikes)
- **HN**: essays are the ammunition — The Markdown Database Pattern is very HN-shaped; the manifesto is a launch moment (post when the site has ~15–20 solid pages so the click-through sticks).
- **Reddit**: r/ObsidianMD, r/Markdown, r/PKMS, r/selfhosted — genuine participation + occasional links (by hand, Rufus).
- **X/Mastodon/Bluesky**: the "name and shame holdouts" table and "did you know X speaks markdown" make good posts.

### Ecosystem & link-building (compounding)
- **"X ❤️ Markdown" badges** (from inbox #45): tools/communities embed the badge, links back to the manifesto. Cheap, on-brand, viral-ish.
- **awesome-markdown lists & tool docs**: PR the site into relevant lists; get referenced from tool READMEs we review kindly.
- **Interview series** (Rufus's idea — the strongest play): each interview = unique content + the guest's audience + a backlink. Target list, roughly in order of fit × reachability:
  1. **Steph Ango (kepano)**, Obsidian CEO — "file over app" is literally our thesis
  2. **John MacFarlane** — pandoc/CommonMark, the ecosystem's quiet giant
  3. **Titus Wormer** — unified/remark, powers half the markdown web
  4. Stripe **Markdoc** team; **iA Writer** (Oliver Reichenstein); **Typora**; **Zettlr** (Hendrik Erz); Blot; into.md/Turndown authors
  5. Long shot: **John Gruber**
  Written Q&A first (low friction), podcast later if it works.

### Explicitly later
Newsletter (add a signup once there's traffic worth capturing), paid anything, programmatic SEO at scale.

## 4. Division of labour

**Claude sets up / drafts:** content map + articles (in Rufus's voice — #58), hub page, titles/meta/sitemap/llms.txt, badge assets + embed snippet, interview target dossiers + question sets + outreach email drafts, awesome-list PR candidates, HN/Reddit post drafts, Search Console setup instructions, metrics reporting.

**Rufus does by hand:** sending outreach and doing interviews, posting to HN/Reddit/X under his own name, personal-network seeding, final voice pass on flagship prose.

## 5. Sequence & metrics

1. **Now → content base**: ship the P1 content map ([[content-map]]) — hub + ~8 spokes + basics + 2 use-case guides. Meanwhile: Search Console, sitemap, llms.txt.
2. **Launch moment**: manifesto revised in Rufus's voice (#58) → HN + communities + badges live.
3. **Compound**: interview series starts; steady 1–2 articles/week; quarterly content-map refresh from Search Console query data.

Metrics that matter: indexed pages, search impressions/clicks (Search Console), referring domains, HN/Reddit post reception, and later: newsletter signups. Vanity to ignore: total pageviews early on.
