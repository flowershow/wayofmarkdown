---
title: "How to publish a Markdown file online — the fastest ways"
description: "You have a markdown file; you want it on the web as a page someone can read. The fastest routes, from ten seconds to a full site."
---

# How to publish a Markdown file online

The humblest job in this whole site: you have *one markdown file* (a note, a report, an essay, meeting minutes) and you want it on the web where someone can read it. No site, no fuss.

## Route 1: GitHub renders it for free (~1 min)

Any `.md` file in a GitHub repo displays as a formatted page. Create a repo (or use any you have), add the file, share the link. A repo whose README *is* the document is a perfectly respectable single-page publication — half the internet's project pages work exactly this way. Gists do the same for even less ceremony: [gist.github.com](https://gist.github.com), paste, save, share.

Good: free, instant, versioned. Less good: it looks like GitHub, not like a page of yours.

## Route 2: an actual page with Flowershow (~5 min)

Point [Flowershow](https://cloud.flowershow.app) at a repo containing your file and you get a real, clean web page on a real URL, and every edit you push updates it. One file today; if you ever add a second, congratulations, you're accidentally [building a website](markdown-websites.md), which is rather the idea. There's also the [CLI route](https://www.youtube.com/watch?v=E9z0zLewoAM): publish a file from your terminal in one command.

## Route 3: paste-and-go services (~10 sec)

Various paste-to-page services will turn markdown into a shareable page in seconds with zero accounts. Handy for throwaways; just remember the trade: your document now lives at someone else's mercy, with none of the ownership this site keeps banging on about. For anything you'd mind losing, use routes 1–2, where the source stays in your hands.

## The point behind the howto

Notice what you *didn't* do in any of these: convert the document. The markdown file is simultaneously your source, your archive and your publication — readable raw, rendered pretty, and still yours afterwards. That's the smallest possible demonstration of [the whole way of markdown](why.md), and the on-ramp to [everything else you can build](markdown-based.md).
