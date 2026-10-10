---
title: "Plan: October 2026 marketing push"
publish: false
---

# Way of Markdown — October push (draft)

Status: draft for Rufus to approve (10 Oct 2026). Moved from `rufuspollock/marketing` (cross-initiative coordination; roadmap `docs/plans/2026-10-10-marketing-roadmap.md` there). Builds on [[marketing]] (personas, SEO as the main engine, community launches for spikes).

## Aim

Follow up August's spike while the topic is warm, in communities that have **not** seen the Markdown Database Pattern yet, and start capturing readers.

Measure: sessions from each post (UTM-tagged), sign-ups once the form is live, Reddit upvotes and comments. Baseline: August week 3.1K users; HN 1,455 sessions.

## What we know going in

- HN is hit or miss. Rufus's HN submissions: 168 and 51 points for two; 1–10 for the other four. The Google Docs `.md` news has already been submitted four times this week by others and got 2–4 points each, so **not HN for that one**.
- The pattern essay has only been on HN and dev.to. Reddit (r/ObsidianMD, r/PKMS, r/Markdown, r/selfhosted) is unused, and the site plan names it as the PKM audience's home.
- There is **no sign-up form** on the site yet (see Beads here). The site plan deferred one "until there's traffic worth capturing"; August suggests that point has passed.

## Pieces, in order

| # | Piece | Status | Where | Who posts |
|---|---|---|---|---|
| 1 | The Markdown Database Pattern (existing essay) | live | r/ObsidianMD, r/PKMS (text post, own summary, link at end) | assistant or Rufus |
| 2 | Google Docs opens `.md` natively (log, 5 Oct) | live | r/Markdown, r/gsuite; Bluesky; refresh `/markdown-in-google-docs` for search | assistant; agent drafts the page refresh |
| 3 | **New follow-up**: "Query your Obsidian vault with SQL" (MarkdownDB walkthrough of the pattern) | to write | HN (new URL, Rufus's account), dev.to, r/ObsidianMD a week after #1 | Rufus or assistant on HN |

Piece 3 is the one with HN potential: a hands-on "do it in five minutes" follow-up to a post HN already liked. Outline: the problem in two lines → link to the pattern → install MarkdownDB → index a vault → three queries people actually want (tasks due this week, notes by tag since date, orphan notes) → limits → Obsidian Bases as the no-code route. Draft in `wayofmarkdown/drafts/`. Before writing, check what MarkdownDB actually supports today, and use only queries it can run.

Sequence: sign-up live → #1 and #2 in week 1 (two different days) → #3 the week after → review.

## Draft posts

All links get UTM tags: `?utm_source=<platform>&utm_medium=social&utm_campaign=wom-2026-10`.

**#1 r/ObsidianMD** (check the sub's self-promotion rules first; post as a discussion, not a bare link)

> **Title:** Your vault is already a database: the "markdown database pattern"
>
> I've been writing up a pattern I've used for years: treat a folder of markdown files as a database. Each file is a record, frontmatter fields are columns, folders are tables, and tags, links and tasks are relations.
>
> Obsidian Bases is a no-code version of exactly this, and Dataview got there earlier. The point of naming it as a pattern is that it doesn't depend on any one tool: the same vault can be queried by Bases, by a script, or by SQL.
>
> Write-up with the full mapping, limits (not for millions of records, not for heavy relational data) and tools: https://wayofmarkdown.com/markdown-database?utm_source=reddit&utm_medium=social&utm_campaign=wom-2026-10
>
> Curious how people here structure frontmatter for this: one schema per folder, or loose?

**#1 r/PKMS**: same body; title: *"File over app, applied to data: the markdown database pattern"*.

**#2 r/Markdown**

> **Title:** Google Docs now opens and edits .md files without converting them
>
> Rolled out from 5 Oct: Drive previews `.md`, Docs opens it in "Markdown Mode", you can comment and collaborate, and the file stays markdown. Lost in round-trip: smart chips, colours, highlights, alignment.
>
> Notes, links to Google's announcement and the limits: https://wayofmarkdown.com/logs/2026-10-05-google-docs-opens-md-files?utm_source=reddit&utm_medium=social&utm_campaign=wom-2026-10

**#2 Bluesky** (personal account, once its app password exists)

> Google Docs now opens .md files natively. No import, no conversion: the file stays markdown, and you can comment and share it like any Doc. Google says plainly it's about AI agents. What works and what gets lost: [link]

## Open for Rufus

- Approve pieces 1–3 and the order. Who posts on Reddit: the assistant, from which account?
- Sign-up: which tool (Brevo shared list is the default) and does Flowershow support an embedded form? (see Beads here)
- Piece 3: Rufus writes it, or agent drafts in his voice for a final pass?
