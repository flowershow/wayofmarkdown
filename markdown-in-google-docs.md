---
title: "How to use Markdown in Google Docs — enable, paste, export"
description: "Google Docs has real markdown support now: paste from markdown, copy as markdown, import and export .md files. How to switch it on, plus export quirks to know."
---

# How to use Markdown in Google Docs

Did you know that Google Docs has major markdown support? Most importantly (at least for me) you can copy and past from markdown -- this is great for moving content from or to systems that are markdown-native like GitHub, ChatGPT, Discourse, Obsidian etc etc.

**However, markdown support is disabled by default 🤯**. So you need to enable it ... here's how courtesy of the official instructions https://support.google.com/docs/answer/12014036?hl=en

<img width="968" alt="image" src="https://github.com/user-attachments/assets/9a0fea17-c672-43e0-b942-c31154e91988" />

## Enable Markdown Support

- On your computer, open a file in Google Docs, Google Slides, or Google Drawings.
- Go to **Tools and then Preferences**
- Check or uncheck the box next to "Enable Markdown”.

Wow, that was easy 😅

## Paste markdown into Google Docs

- Copy the Markdown content to your clipboard
- On your computer, open a document in Google Docs.
- Right-click and select Paste from Markdown. The Markdown will be converted to Google Docs content and be pasted.

## Copy Google Docs content as Markdown

- In Google Docs select the content you want to copy
- Right-click and select Copy as Markdown.

## You can also import and export markdown files

- Just download as markdown ...
- Or upload

However, frankly I prefer just copy/pasting markdown using the above techniques 99% of the time.

# Commentary

## 2025-01-15 - Rufus Pollock

I personally don't use markdown *in* google docs that much. But I use the import/export features a lot when collaborating with other folks. e.g. i draft something in obsidian or in a github issue (in markdown) and then i need to collaborate with others or make a fancier version so i need to transfer to google docs ... paste from markdown support in gdocs is then a god-send.

conversely i've worked with some colleague on a product idea or a task in google docs and now i want to transfer to issue tracker in e.g. github ... copy as markdown is super helpful.

I also often find that for relatively rich textual output prompting chatgpt to give me markdown output and then pasting in gdocs gives greater fidelity than copying and pasting directly from chatgpt (especially the native app).

## Appendix: full-export quirks (field notes)

I just did a full markdown export of a large document from Googles Docs (this [metacrisis paper](https://metacrisis.info/paper) to be precise).

I noticed a few interesting things:

### Anchor links

It outputted anchors like `{#synopsis}` e.g.:

```
# Synopsis {#synopsis}
```

And in context:

```md
# Synopsis {#synopsis}

Our world shows signs of multi-systemic breakdown. In this context, **polycrisis** names an *entanglement* of interconnected crises that affect one another \- ecological, political, cultural, technological. **Metacrisis**, by contrast, denotes foundational conditions that generate these crises. Just as symptoms signal an underlying illness, polycrisis points to metacrisis. While the reality of a global polycrisis is increasingly acknowledged, awareness of metacrisis is less common. 
```

This is the [[identifiers|Identifiers]] feature introduced by Pandoc.

### Images inlined

It outputs images at the end of the file as `data:...`. This is kind of cool but also kind of weird. I guess it is the one way to have a single page html file. I'd much prefer the export was more like the HTML option where i can either have single file version or with assets separate and what i get is a zip file i can unzip.

More apps: [markdown everywhere](everywhere.md) 🌍
