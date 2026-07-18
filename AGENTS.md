# AGENTS.md — instructions for AI agents working on this repo

This repo is **The Way of Markdown** (https://wayofmarkdown.com): a content site teaching the markdown-based way of working, published with Flowershow. The markdown in this repo *is* the site. Owner: Rufus Pollock (@rufuspollock).

## Orient yourself (read in this order)

1. `docs/vision.md` — what this project actually is (core insight: nobody cares about markdown per se; the ecosystem and use cases are the point; Flowershow stays secondary)
2. `docs/plans/` — current version plan (with work log), content map, marketing plan
3. GitHub issues — the canonical task tracker (see Workflow below)

## Workflow

- **Tracking lives in GitHub issues**: a version epic (currently #46) links sub-issues per big item; loose ideas go to the inbox issue (#45). Close sub-issues with a "what happened" writeup — they double as the project's history.
- **Act first, review later.** Rufus delegates fully: proceed without asking for anything reversible, and append a short comment per work session to the review log issue (#57) listing judgment calls, prose worth a skim, and unverified fact-claims. Ask first only for irreversible or outward-facing steps (deleting things you can't restore, posting/emailing as Rufus, anything touching other repos or services).
- **Commit and push to `main`** in logical chunks with prefixed messages (`content:`, `docs:`, `voice:`, `seo:`, `launch:`). Pushing deploys the site (usually live within ~1–2 minutes). After significant pushes, spot-check live URLs.
- Also update the narrative log in the current `docs/plans/v*.md` when a session changes project state.

## Voice — this is the crucial one

Published prose must sound like Rufus, not like AI. This is a hard requirement (issue #58).

1. **Load the `write-like-me` skill** (`.claude/skills/write-like-me/`) before drafting or editing any published page. Its voice profile (`references/voice-profile.md`) defines the voice; its rules ban the AI register (negation flips, snappy triads, "delve", inspirational wrap-ups, em-dash tics).
2. **Run `python3 scripts/voice-lint.py`** before committing prose. It must pass (suppress genuine false positives inline with `<!-- voice-lint-ok: reason -->`). The lint is the floor, not the voice: after it passes, read a paragraph aloud — if it sounds like a keynote, rewrite it.
3. **When Rufus has a draft, start from it and edit lightly.** Never rewrite his text into polished-AI register; keep his phrasings, jokes and asides. His originals: `docs/manifesto/draft-2026-01.md`, `markdown-database.md`, rufuspollock.com.

## Content conventions

- **Structure**: mostly-flat top level with SEO slugs. Guides: `markdown-<x>.md` (index: `markdown-based.md`). Per-app articles: `markdown-in-<x>.md` (hub: `everywhere.md`). Tutorials and howtos: `learn/`. Notes/tools/workflows: `kb/`. Philosophy: `why.md`, `manifesto.md`.
- **Every published page** gets frontmatter `title` and `description` (descriptive and query-matching — the brand name carries no SEO weight, the page titles do).
- **Spoke articles** lead with the answer (syntax table up top), cover quirks honestly, and end with one link deeper into the site. Hub and spokes must link both ways.
- **Guides** follow: what is X → the markdown-based pattern → tools (Flowershow appears as *a* publishing option, never the headline) → walkthrough. Be honest about limits; it's a signature of the voice and the site.
- **Videos**: embed as HTML `<iframe>` (allowed — and on-message, since "markdown supports HTML" is a core lesson). Index: `videos.md`.
- **New page slugs are permanent** — they become URLs. Think before naming; renames need redirects.

## Publishing mechanics

- Flowershow publishes everything except: paths in `contentExclude` in `config.json` (currently `.claude/`, `docs/`, `scripts/`, README/AGENTS/CLAUDE) and pages with `publish: false` frontmatter. **Anything else you create will appear on the public site** — internal material goes in `docs/`.
- `config.json` must stay valid JSON (`python3 -c "import json; json.load(open('config.json'))"`).
- `llms.txt` exists for AI answer engines — extend it when major pages are added.

## Checks before ending a work session

```bash
python3 scripts/voice-lint.py    # voice/anti-pattern lint — must pass
python3 scripts/link-check.py    # wikilinks + relative links — must pass
```

Plus: valid config.json if touched, and live-URL spot-checks after deploy.

## Repo map

```
index.md, why.md, manifesto.md      site core
basics.md, everywhere.md            syntax primer; markdown-in-X hub
markdown-based.md, markdown-*.md    guides section
markdown-in-*.md                    per-app articles
learn/                              tutorials, howtos, onboarding path
kb/                                 knowledge-base notes
videos.md, llms.txt                 media index; AI-engine manifest
docs/                               internal: vision, naming, plans, launch kit, manifesto sources (NOT published)
scripts/                            voice-lint.py, link-check.py
.claude/skills/write-like-me/       voice skill + profile
```

`CLAUDE.md` is a symlink to this file so Claude Code loads it automatically; keep the two as one.
