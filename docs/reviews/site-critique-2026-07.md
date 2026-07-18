---
title: "Site critique — July 2026"
publish: false
---

# The Way of Markdown: a hard look (2026-07-18)

Written as requested: product owner + content strategist + marketer + guide-builder hats on, reviewing the site as it stands today (~70 pages, visual roadmap, blog, launch kit staged). Verdict up front: **the content skeleton is genuinely strong — coherent thesis, honest voice, unusual breadth for its age. What it lacks is almost everything *around* the words: visual identity, proof, interactivity, trust signals, and feedback loops.** It currently reads like an excellent manuscript, not yet like a place.

Scores by lens (5 = world-class):

| Lens | Score | One-line diagnosis |
|---|---|---|
| Thesis & IA | 4.5 | Clear, differentiated, well-structured; kb/guides seam is the one wrinkle |
| Writing & voice | 4 | Distinctive and honest; a few pages still read samey in rhythm |
| Visual identity | 1.5 | Default theme, emoji favicon, zero images, no OG cards |
| Show-don't-tell | 2 | Guides assert; almost nothing is *shown* (screenshots, demos, live examples) |
| Learner experience | 3 | Roadmap is a real asset; but no playground, no progress, tutorial 3–4 debt on the spine |
| Trust & authorship | 2 | No about page, no bylines, no "who is behind this" anywhere |
| Discovery (SEO/tech) | 3 | Good titles/slugs/llms.txt; missing OG images, RSS, Search Console, analytics |
| Engagement loops | 1.5 | No comments, no email capture, no reason to return except willpower |

## 1. Visual identity — the biggest gap

We are a site *about* how markdown+HTML can look great, wearing a default theme. That's a credibility problem, not just an aesthetic one.

- **Own a palette.** The roadmap accidentally created one: its green/amber/grey status language. Adopt green as the brand accent deliberately (links, buttons, callouts) via `custom.css` — Flowershow exposes theme variables in cascade layers, so this is an afternoon, not a redesign.
- **A wordmark.** Even just "**way**of**markdown**" set in a good mono/sans pair, plus a real favicon (the 🚀 emoji reads generic). A `#`- or `¶`-based mark is on-message and easy.
- **OG/social card images.** Every share of every page currently renders as a bare link. One templated card (title on brand background — generatable per page by script, our data→SVG pattern again) would multiply social CTR. This matters *before* launch, not after.
- **Illustration system.** Not stock art: a consistent, minimal diagram style (we already have it in the roadmap SVG) reused as small per-guide heros. Generated, versioned, themeable — the markdown way, applied to art direction.

## 2. Show, don't tell

The guides argue well and demonstrate almost nothing. Highest-impact fixes:

- **Screenshots in the money guides**: the Notion escape guide should *show* an exported vault open in Obsidian and a Bases table; the websites guide should show a repo next to the rendered site. 6–8 annotated screenshots would transform the four flagship guides.
- **Live worked examples.** We tell people "publish a catalog" — we should *link one*: a demo site (books catalog, tiny garden) built with the tutorials, linked as "see the result". The site itself is our only current exhibit.
- **A raw-markdown button.** "This whole site is markdown" is our proof point — surface it: a "view the markdown for this page" link (the repo edit link exists but is framed as editing, not as proof). Cheap, on-message, delightful.
- **Before/after moments**: the landing page's best possible visual is raw markdown on the left morphing into a rendered page on the right. Even a static two-panel does work; an animated one (CSS or a small gif) is a hook.

## 3. Learner experience

- **The playground gap.** Every good syntax-teaching site has a try-it box. `basics.md` ends with links to *other people's* interactive tutorials — traffic we hand away. A markdown live-preview playground is one `<textarea>` + a JS renderer; needs custom JS, so investigate Flowershow's script options (or an embedded iframe playground we host elsewhere). This is the single biggest missing feature for the Searcher/learner audience.
- **Tutorial 3–4 debt is now visible debt**: the roadmap shows amber on the spine (honest, good) — but it means our flagship path has a hole at exactly the "collaborate" step the Life Itself job story (JS1) needs. Finishing tutorial 3 properly is worth more than three new spokes.
- **Roadmap v2**: progress ticking (localStorage) would convert the map from picture to companion. Also: the map should probably *be* the landing page hero, cropped to stages ⓪–②.
- **Dead-end audit**: several kb notes (turndown, markdoc, identifiers) end without a next step; every page should end with exactly one suggested continuation.

## 4. Trust & authorship

- **No /about page.** Who runs this? Why should I trust it? One page: Rufus, the Life Itself/Datopian/Flowershow lineage, why this site exists, how it's made (repo link), contact. Also needed for Google E-E-A-T on a new domain.
- **Bylines & dates.** Essays and posts should carry visible author + date (blog posts have frontmatter; evergreen pages need the visible-updated treatment already logged in #45). An undated guide on a young domain reads as content-farm output — dates + bylines are the antidote.
- **Site footer** is default: should carry about / GitHub / blog / RSS / license (content license is actually undeclared — decide: CC-BY? on-brand and quotable).

## 5. Discovery mechanics

- **RSS for the blog** (Flowershow supports it) — table stakes for the audience we want; newsletter people subscribe via RSS-to-email themselves.
- **Analytics: nothing is measuring anything.** Flowershow supports GA4 and Umami. Umami fits the brand (privacy-respecting); needs a decision + account from Rufus. Without it, the whole marketing plan flies blind.
- **Search Console + sitemap** — already on the launch checklist; do not skip.
- **The kb/guides seam**: `kb/google-docs` (app guide) vs root `markdown-in-x` (app guides) is one genre in two homes with two URL patterns. Consolidate on `markdown-in-*` with redirects before the URLs age further.
- **Comparison pages** are the highest-intent SEO genre we have none of: "Obsidian vs Notion", "Flowershow vs Obsidian Publish", "markdown vs rich text". Two or three, honestly written (our honesty *is* the differentiator), would out-earn ten more spokes.

## 6. Engagement loops

- **Comments via Giscus** (GitHub Discussions; Flowershow-supported) on blog + essays: cheap community, and our audience has GitHub accounts by definition.
- **"X ❤️ Markdown" badges** (inbox): the only viral mechanic we've designed — build the badge + embed snippet page.
- **A tiny footer email capture** ("occasional dispatches") even before a newsletter exists — collecting intent early is free optionality. (Marketing plan says later; I'd move it earlier.)

## 7. Practice-what-we-preach audit

We preach gardens with backlinks: Flowershow supports backlinks display and a knowledge graph — **neither is enabled**. We preach dates; we show none. We preach "the ecosystem can reproduce anything" while our own blog index needed MDX (fine — but say so somewhere; it's an honest limits note). Turning on backlinks alone would make the site demo its own thesis.

## Top 10, prioritized (impact × effort)

1. **custom.css brand pass** — palette + typography ownership (S effort, L impact)
2. **/about page + footer + bylines** (S, L — trust)
3. **OG card images**, templated/generated (M, L — every future share pays)
4. **Screenshots for the 4 flagship guides** (M, L)
5. **Finish tutorial 3** (M, L — spine integrity, JS1)
6. **Analytics (Umami) + Search Console + RSS** (S, L — decision needed from Rufus)
7. **Raw-markdown "view source" framing + enable backlinks** (S, M — proof)
8. **Giscus comments on blog/essays** (S, M)
9. **kb→markdown-in-* consolidation with redirects** (S, M — do before URLs age)
10. **Markdown playground** (L, L — investigate JS options first; the one big feature bet)

Not prioritized but recorded: landing-page hero rework (pairs with 1+3), comparison pages (next content wave), badges, roadmap progress-ticking, demo example sites, email capture.
