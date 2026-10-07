---
title: "Google Docs now opens and edits .md files natively"
description: "Since 5 Oct 2026 Google Drive previews .md files and Docs edits, comments on and shares them without converting. The file stays markdown."
date: 2026-10-05
authors: ["rufus"]
---

# Google Docs now opens and edits .md files natively

This is a big one. Google Drive now renders `.md` files, and Google Docs opens them, edits them and lets you comment and collaborate, all **without converting them into a Google Doc**. The file stays a `.md` file in your Drive. 🎉

Until now Docs could paste and export markdown ([how-to](/markdown-in-google-docs)), but a `.md` file had to be imported, which converted it, and you lost the plain file. Now the markdown file is the document.

- **Announcement**: [Google Workspace Updates, 5 Oct 2026](https://workspaceupdates.googleblog.com/2026/10/preview-edit-and-collaborate-on-Markdown-files-natively-across-Drive-and-Docs.html)
- **Help page**: [View and edit Markdown (.md) files in Google Docs](https://support.google.com/docs/answer/18289341?hl=en)
- **Thread**: [Chandu Thota](https://x.com/ChanduThota/status/2107195115441946850), who leads engineering for Google Workspace

## What you get

- **Drive**: right-click a `.md` file → *Open with* → *Preview*. You can flip between the raw markdown and the rendered view (clickable links, proper tables).
- **Docs**: double-click a `.md` file and it opens in "Markdown Mode", with an `.md` tag next to the title. Edit in the normal Docs editor, add comments, share it, work on it together in real time.
- **Rollout**: all Workspace customers and personal Google accounts, rolling out gradually from 5 October (up to 15 days). No setting to switch on.

## Why it matters: AI

Google is explicit that this is about AI. The announcement pitches markdown as the format LLMs use for structured content, and says editing `.md` in Docs lets "both users and agents" collaborate without anyone writing raw syntax or converting files. Chandu Thota's thread puts it more plainly:

> Markdown has become the common language between humans and AI agents - specs, plans, READMEs, tables, task lists, generated docs - so much of this starts as .md.

and the friction it removes: "no import/export loops, fewer broken formats". <!-- voice-lint-ok: direct quote -->

That's exactly the gap I kept hitting. I draft in markdown (or an agent does), then someone wants to comment, so it goes into a Google Doc, and now there are two versions and the markdown one is stale. Now the agent writes the `.md`, the humans comment on that same file in Docs, and the agent can read it straight back.

## The limits

Docs can do more than markdown can express, so some things don't survive when you edit a `.md` file (per the help page):

- smart chips turn into plain text or links
- HTML formatting becomes plain text
- font colours, highlights and text alignment are dropped

Version history will get you back the original. I haven't tested how it handles frontmatter, wikilinks or footnotes yet; reports welcome.

More on markdown and Google Docs: [How to use Markdown in Google Docs](/markdown-in-google-docs).
