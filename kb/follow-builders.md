---
title: Follow Builders, Not Influencers — AI builders digest
description: "A daily/weekly digest that tracks top AI builders on X and YouTube, remixes their content into summaries. Set up in two minutes with Claude Code or OpenClaw. No API keys needed."
---

# Follow Builders, Not Influencers

**([github.com/zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders))**

An AI-powered digest that tracks the top builders in AI — researchers, founders, PMs, and engineers who are actually building things — and delivers curated summaries of what they're saying.

**Philosophy:** Follow people who build products and have original opinions, not influencers who regurgitate information.

## What you get

A daily or weekly digest delivered to your preferred messaging app (Telegram, Discord, WhatsApp, etc.) with:

- Summaries of new podcast episodes from top AI podcasts
- Key posts and insights from 26 curated AI builders on X/Twitter
- Full articles from official AI company blogs (Anthropic Engineering, Claude Blog)
- Links to all original content
- Available in English, Chinese, or bilingual

## Default sources

**Podcasts (6):** Latent Space, Training Data, No Priors, White House AI, Tough Things, Equity

**X/Twitter builders (26):** Including Andrej Karpathy, Dylan Patel, Bloomberg AI, Zvi Mowshowitz, Catherine Wood, etc.

**Official blogs (2):** Anthropic Engineering, Claude Blog

## Quick start

**Claude Code:**

```bash
git clone https://github.com/zarazhangrui/follow-builders.git ~/.claude/skills/follow-builders
cd ~/.claude/skills/follow-builders/scripts && npm install
```

Then tell your agent: "set up follow builders" or invoke `/follow-builders`. The agent walks you through setup conversationally — no config files to edit.

**OpenClaw:**

```bash
git clone https://github.com/zarazhangrui/follow-builders.git ~/skills/follow-builders
cd ~/skills/follow-builders/scripts && npm install
```

## What the agent will ask you

- How often you want your digest (daily or weekly) and what time
- What language you prefer
- How you want it delivered (Telegram, email, or in-chat)

No API keys needed — all content is fetched centrally. Your first digest arrives immediately after setup.

## Customizing the summaries

The skill uses plain-English prompt files to control how content is summarized. You can:

- **Through conversation (recommended):** Tell your agent what you want — "Make summaries more concise," "Focus on actionable insights," "Use a more casual tone."
- **Direct editing (power users):** Edit the files in the `prompts/` folder — `summarize-podcast.md`, `summarize-tweets.md`, `summarize-blogs.md`, `digest-intro.md`, `translate.md`. Plain English instructions, not code. Changes take effect on the next digest.

## How it works

1. A central feed is updated daily with the latest content from all sources (blog articles via web scraping, YouTube transcripts via Supadata, X/Twitter via official API)
2. Your agent fetches the feed — one HTTP request, no API keys
3. Your agent remixes the raw content into a digestible summary using your preferences
4. The digest is delivered to your messaging app (or shown in-chat)

## Privacy

- No API keys are sent anywhere — all content is fetched centrally
- If you use Telegram/email delivery, those keys are stored locally in `~/.follow-builders/.env`
- The skill only reads public content (public blog posts, public YouTube videos, public X posts)
- Your configuration, preferences, and reading history stay on your machine

## License

MIT

## See also

- [`kb/ai-editing.md`](../kb/ai-editing) — Using AI to edit Markdown notes in Obsidian (Claude Code, Codex)
- [`kb/cursor-obsidian.md`](../kb/cursor-obsidian) — Using Cursor with Obsidian
