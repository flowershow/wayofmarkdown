---
title: "Naming: The Way of Markdown"
publish: false
---

# Naming decision: The Way of Markdown

**Decision (2026-07):** the project/site is named **The Way of Markdown** (domain/repo: `wayofmarkdown`). "Markdown is Awesome" survives as landing-page energy (headline/tagline territory), not as the brand.

## Options considered

- **markdownmanifesto.com** — ideological/reformist. Strong positioning but narrows the site to polemic; awkward home for tutorials; slightly combative.
- **markdownisawesome.com** — evangelical/accessible. Maximum optionality (guides, demos, tools, community), immediately clear, but lightweight — little gravitas, and doesn't carry the "philosophy of openness" thread.
- **thewayofmarkdown.com** — practice/craft tradition. Distinctive, memorable, suggests depth and discipline. Risks: can drift into mysticism if not grounded in strong technical material; weaker keyword-intent match; more abstract.

## How the decision was reached

Worked through in [this ChatGPT thread](https://chatgpt.com/share/6a5ac1f3-54c4-83eb-a0d3-d0941c9b4592) (2026). Key moves:

1. Initial recommendation was *markdownisawesome* on pure optionality grounds.
2. Clarifying the site's primary job: a **practical guide with an edge** — not "civilizational infrastructure", but a philosophy of openness/portability demonstrated through practice ("infrastructure evangelism through demonstration").
3. That identity maps to a **practice tradition** ("craft ethos"), and of the three names, *The Way of Markdown* is the one that matches a practice tradition — the other two match an evangelical movement (*is awesome*) or a reformist one (*manifesto*).

## Sense check (Claude, 2026-07-18)

The choice is sound, with conditions:

- **The logic holds.** The thread's early lean toward *markdownisawesome* was based on optionality; once the identity was clarified as "practical craft with a philosophical spine", *Way of Markdown* is the honest name for that. "Way of X" has good precedent in developer-craft culture (*The Tao of Programming*, *Zen of Python*) — it reads as craft, not mysticism, **provided the content stays overwhelmingly practical**.
- **Distinctiveness beats descriptiveness here.** "Markdown is awesome"-style names are generic and undifferentiated; *The Way of Markdown* is ownable and memorable, and it uniquely accommodates both the tutorials and the why/philosophy essays under one identity.
- **SEO concern is real but minor.** Brand-name keyword match matters far less than page-level content; the guides/reference pages carry the search intent ("markdown in google docs", etc.). Mitigation: strong descriptive page titles, and optionally keep `markdownisawesome.com` as a redirect.
- **Guardrails:** keep the tone practical and specific; the "Way" framing earns its keep through exemplars and working material, not proclamations. Avoid manifesto-speak on the landing page.

## Implications

- Site title / nav title: "The Way of Markdown" (config.json).
- Landing page: can keep an energetic headline (e.g. "Markdown is awesome — here's the way to use it everywhere").
- Older names ("Make it Markdown", "Markdown is Awesome") in content should be cleaned up during v0.1 polish.
