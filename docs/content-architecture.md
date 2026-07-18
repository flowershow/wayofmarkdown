---
title: "Decision: evergreen KB + dates + blog stream"
publish: false
---

# Content architecture: dated posts vs wiki KB

**Decision (2026-07-18): both, with distinct jobs.** The knowledge-base/guide layer stays evergreen and canonical; every page shows a visible last-updated date; a lightweight blog stream sits on top for announcements, essays and pointers. Implementation tracked in the blog/changelog issue (see epic #46).

## The question

Rufus: people like blog-post presentation — a date tells them when something was published and gives a natural structure, whereas a wiki/KB feels a bit random and placeless. Should the site be dated posts or a wiki?

## The reasoning

Decompose what readers actually get from the blog format:

1. a **trust signal** ("this was true as of May 2023")
2. a **sense of place** in a chronological stream
3. an implicit promise the **site is alive**

What they don't get is maintainability. Dated posts psychologically resist editing — they're "published", so they quietly go stale. Cautionary tale from our own history: the portaljs catalog post still teaching Dataview years after Obsidian Bases superseded it.

For this site, guides and spokes must stay wiki-style evergreen: "how to use markdown in Google Docs" needs one canonical URL that accumulates SEO authority and gets corrected in place. Dated posts would fragment that authority and institutionalise staleness.

But the blog format's psychological benefits can be captured cheaply:

- **Visible dates on evergreen pages** — created/updated in frontmatter, shown on the page. Trust signal without the staleness trap; also a freshness signal for SEO.
- **A thin `blog/` stream** — announcements, dated essays, "new guide:" pointer posts (two paragraphs pointing into the evergreen layer is fine). Gives the site a pulse, and gives launches something fresh to link: an HN/Reddit submission pointing at a dated post reads better than one pointing at a wiki page. The stream advertises the garden.

This is Caulfield's garden-and-stream distinction, applied to ourselves — fitting, since our [[../markdown-digital-gardens|digital gardens guide]] teaches exactly this. The site should practice what it preaches: garden (guides) + stream (blog).

## Consequences

- Evergreen pages: keep slugs undated, maintain in place, show dates.
- New long-form essays may debut as dated blog posts *and* live on as evergreen pages when they mature — the manifesto and markdown-database essay pattern.
- Changelog-ish updates ("Everywhere list gained four new apps") are blog material, not new pages.
