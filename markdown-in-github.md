---
title: "Markdown in GitHub — where markdown conquered the world"
description: "GitHub runs on markdown: READMEs, issues, pull requests, comments, wikis. GFM syntax — tables, task lists, alerts, mermaid diagrams — and how to use it well."
---

# Markdown in GitHub

If markdown has a spiritual home, it's GitHub. READMEs, issues, pull requests, comments, discussions, wikis, gists: all markdown. Every developer on earth writes it here daily, which is a big part of how markdown became [the default format of the internet](everywhere.md) -- and why every AI trained on the internet [speaks it fluently](markdown-in-chatgpt.md).

GitHub's dialect, **GitHub Flavored Markdown (GFM)**, is also the de facto standard the rest of the world copies. Learn it once, use it everywhere.

## The GFM essentials

All the [basics](basics.md) work: headings, bold, italic, links, images, quotes, code. GFM adds the good stuff:

| Feature | Syntax |
|---|---|
| Tables | `\| col \| col \|` (like this one) |
| Task lists | `- [ ] todo` / `- [x] done` -- interactive in issues! |
| Fenced code with highlighting | ```` ```python ```` |
| Strikethrough | `~~nope~~` |
| Mentions & references | `@person`, `#123` (issue), SHA -- all auto-link |
| Footnotes | `[^1]` |
| Alerts | `> [!NOTE]`, `> [!WARNING]` etc: styled callout boxes |
| Diagrams | ```` ```mermaid ```` renders actual flowcharts 🎉 |
| Collapsible sections | `<details><summary>Click</summary>...</details>` -- because [HTML works in markdown](markdown-websites.md) |

Task lists deserve a highlight: in issues and PRs they become live checkboxes, and GitHub counts progress ("3 of 7"). A markdown bullet list is suddenly a project tracker. This is [the markdown database pattern](markdown-database.md) hiding in plain sight.

## Where markdown shows up on GitHub

- **README.md**: renders automatically as a repo's front page. A repo of markdown plus a README is already a publication.
- **Any `.md` file**: rendered when browsed, editable in the web editor (press `.` in any repo for a full VS Code in the browser).
- **Issues, PRs, comments**: full GFM, with slash-command niceties and drag-and-drop images.
- **Your profile**: create a repo named after your username, and its README becomes your profile page.

## The bigger move

Once your writing lives in markdown on GitHub, it's one step from *rendered files in a repo* to *actual website*: that's exactly what [markdown-based websites](markdown-websites.md) are, and what this site is. And because a repo is versioned and reviewable, it's also the machinery behind [team wikis and handbooks](markdown-wikis.md).

Practical tips in the kb: [GitHub FAQs -- branches, commits, good practice](kb/github-tips.md). Never touched GitHub? The [onboarding path](learn/onboarding.md) assumes nothing.
