---
title: "Git & GitHub glossary for non-developers"
description: "Repository, clone, commit, push, branch, fork, pull request, merge — every term you meet in a markdown workflow, explained in plain language."
---

# Git & GitHub glossary (for normal people)

Every term you'll meet working on a markdown-based site or wiki, in the order you'll meet them. No prior knowledge assumed — this is the companion to the [tutorials](../learn/index.md) and the [onboarding path](../learn/onboarding.md).

**Repository (repo)** — the project's folder, hosted on GitHub: all its files plus the complete history of every change ever made to them. Your website or wiki is one repo.

**git** — the version-control system underneath everything: the program that tracks changes to files over time. You mostly meet it through friendlier tools (GitHub's website, GitHub Desktop) rather than directly.

**GitHub** — a website that hosts git repositories and adds the social layer: accounts, access, reviewing, discussion. git is the engine; GitHub is the garage.

**Clone** — copy a repository from GitHub onto your computer, history included. You edit the local copy; the one on GitHub is the shared original.

**Commit** — save a snapshot of your changes, with a short message saying what you did ("fix typo on about page"). Think "save, with a note to your future self". Commits are why nothing is ever really lost.

**Push** — send your local commits up to GitHub so everyone (including the website build) gets them. Until you push, your changes exist only on your machine.

**Pull** — the reverse: fetch other people's commits from GitHub down to your copy. Do it before you start editing, and life has fewer [merge conflicts](git-rescue.md).

**Branch** — a temporary parallel version of the repo where you make changes without touching the main one. The main branch (usually called `main`) is what the live site is built from.

**Fork** — your own copy of *someone else's* repo, on your GitHub account. Like a branch, but across ownership boundaries — how you contribute to projects you don't have edit rights on.

**Pull request (PR)** — "here are my changes; please review and pull them into the main branch". The unit of collaboration: shows exactly what would change, hosts the discussion, and merges with a click when approved.

**Merge** — combine one branch's changes into another, usually via a PR. When two people changed the same lines, git asks a human to pick — that's a **merge conflict**, it's routine, and [the rescue guide](git-rescue.md) walks you through it.

**Stage** — mark which of your edited files go into the next commit. GitHub Desktop shows this as checkboxes; ticking them is staging.

**Remote / origin** — the copy of the repo that lives on GitHub (as opposed to the local one on your machine). "Origin" is just git's default nickname for it.

Terms in the wild: watch them all appear, in order, in [tutorial 2](../learn/tutorials/edit-a-website-locally.md) and [tutorial 3](../learn/tutorial-3.md).
