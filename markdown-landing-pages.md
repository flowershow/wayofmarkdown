---
title: "Markdown-based Landing Pages"
description: "A landing page — hero, pitch, call to action — from a markdown file, using the HTML-in-markdown superpower. Yes, really."
---

# Markdown-based Landing Pages

A landing page is the most design-heavy page most people ever need: a hero, a pitch, maybe a signup. Surely *this* is where markdown taps out and you need a website builder?

No. And this page is the demo of why. A landing page is 90% content (headline, pitch, proof, call to action) and 10% layout. Markdown handles the 90%; [inline HTML handles the 10%](markdown-websites.md), right in the same file:

<div style="text-align:center; border:2px solid #22c55e; border-radius:16px; padding:2.5rem 1.5rem; margin:1.5rem 0;">
  <div style="font-size:1.8rem; font-weight:800;">Your headline goes here 🚀</div>
  <p style="max-width:34rem; margin:0.8rem auto;">One sentence that says what this is and why the visitor should care. Below it, the one thing you want them to do.</p>
  <a href="/markdown-websites" style="display:inline-block; border:2px solid currentColor; border-radius:10px; padding:0.6rem 1.4rem; font-weight:700; text-decoration:none;">The call to action →</a>
</div>

That hero is a `<div>` in this markdown file. With Tailwind available (Flowershow supports it) you can go considerably fancier (columns, gradients, the lot), and [AI writes this HTML happily](markdown-in-chatgpt.md) if you describe what you want.

## The anatomy, in markdown terms

1. **Hero** — HTML block (above)
2. **The pitch** — plain markdown: short paragraphs, bold where it counts
3. **Proof** — a features list, logos, a quote as a blockquote
4. **Call to action again** — people scroll; ask twice
5. **Signup** — Flowershow supports form embeds; or link out to your form of choice

One file. Versioned, editable anywhere, no site-builder subscription, and when you outgrow one page you're already [building a website](markdown-websites.md).

The 2023 mind-map that seeded this site listed "I want to put a landing page on the web" as one of the five things people actually come wanting. It took us until now to write the page. Sorry, past selves. See also the [single-document version](publish-markdown.md) for the even simpler cousin.
