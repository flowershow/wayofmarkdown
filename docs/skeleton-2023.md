---
publish: false
---

# Site Skeleton (condensed, 2023)

#### Home Page
- Welcome to Makeitmarkdown!
- What is Markdown?
	- lightweight markup language used to format text (break this down + give examples)
	- Differences with WYSIWYG editors
- Why use Markdown?
	- Simple and intuitive
	- Portable and compatible
	- Flexible and extensible
	- Platform-independent
- The MOGF approach
	- An approach for working with Markdown to publish content on the web
	- Components (besides Markdown):
		- GitHub - version control for collaborating on web pages
		- Obsidian - Markdown-based note-taking software that syncs with GitHub for offline editing; extended version of Markdown; adding multiple files at once
		- Flowershow - converting Markdown files into websites; Obsidian-compatible
- About this guide
	- Guides you through basics of creating a website using the MOGF approach
	- By the end, you will be able to:
		- Create a website from scratch using Markdown and Flowershow
		- Edit your Flowershow website locally on your computer using Obsidian
		- Collaborate with others on your website project
		- Customise your website locally and preview your changes locally
- Let's get started!

#### Tutorial series
- Tutorial 1: Create a website from scratch using Markdown and Flowershow
	- Recap (of basics above)
	- What you'll learn
	- Prerequisites
	- Setting up a website
	- Editing a page on your website
	- Add a simple Markdown-based page
	- What's next?
- Tutorial 2: Edit your Flowershow website locally on your computer using Obsidian
	- Recap
	- What you'll learn
	- Prerequisites
	- Clone the GitHub repository on your computer
	- Edit your site in Obsidian
	- Save and publish your changes
	- What's next?
- Tutorial 3: Collaborating with others on your website project
	- Recap
	- What you'll learn
	- Create a new branch
	- Make changes in the new branch
	- Create a pull request (PR)
	- Review and merge a pull request
	- Resolving conflicts
	- What's next?
- Tutorial 4: Customising your website locally and previewing your changes locally
	- Recap
	- What you'll learn
	- Previewing the site locally
	- Changing the site title and description
	- Configuring the title, description and navbar
	- Integrating with Google Analytics
	- Customising the Tailwind theme
	- Congratulations! Where to go from here


# Skeleton (full version)
## Home page

Welcome to Make it Markdown! Here you can learn how to build markdown-based websites, docs, knowledgebases and more – and why a markdown-based approach is awesome 🦸‍♀️

### What is Markdown?

- [Markdown](https://en.wikipedia.org/wiki/Markdown) is a lightweight markup language used to format text
- In WYSIWYG editors (e.g. Word), you click buttons to format text and the changes are immediately visible; in markdown you add syntax to the text to indicate how it should be formatted, e.g. `**xxx**` to indicate bold

### Why use Markdown? 

- **Markdown is simple and intuitive** - don't need to learn a lot of tags and commands, just use symbols to create headings, links, etc.
- **Markdown is portable and compatible** - files with markdown-formatted text can be opened and edited with virtually any text editor or application that supports plain text (which isn't the case with e.g. Word, which locks content into a proprietary file format). This means:
	- You can use it for everything (websites, documents, notes, knowledgebases, catalogs, books, technical documentation...)
	- Can share files with others without compatibility issues
- **Markdown is flexible and extensible** - you can customise Markdown to suit your needs.  There are different 'flavours' or extensions of Markdown that add more features or functionality (e.g. CommonMark and GFM)
	- **Markdown is platform-independent** - you can use it on any device running any operating system

([source 1](https://www.markdownguide.org/getting-started/), [source 2](https://www.linkedin.com/pulse/intro-markdown-benefits-drawbacks-sully-vickers))

### The MOGF approach

- In this guide we set out an approach for working with Markdown to publish content on the web that we term MOGF (Markdown + Obsidian + Git(Hub) + Flowershow)
- This combination or "stack" of tools is free and easy to use, and provides a number of advantages
- **[GitHub](https://github.com/)** is a web-based interface that uses [Git](https://git-scm.com/), the open source version control software that lets multiple people make separate changes to web pages at the same time. ([source](https://digital.gov/resources/an-introduction-github/))
- **[Obsidian](https://obsidian.md/)** is a note-taking software that operates on Markdown files 
	- It previews formatted text
	- Supports an extended version of Markdown that includes majority of elements from CommonMark and GFM, while also introducing its own unique features, like [wiki-links](https://help.obsidian.md/Linking+notes+and+files/Internal+links) or [callouts](https://help.obsidian.md/Editing+and+formatting/Callouts).
	-  Using Obsidian gets around some of the limitations of using GitHub UI:
		- Offline editing
		- GitHub UI will only preview GitHub Flavoured Markdown. And while it's a majority of Markdown you would write, it won't be able to render Obsidian-only (or Flowershow-only) syntax elements, like callouts, wiki-links or inline table of contents
		- It also doesn't allow you to make changes (or to add) multiple files at once
- **[Flowershow](https://flowershow.app/)** is an open-source tool for easily converting markdown files into a website
		- Flowershow template is Obsidian-compatible, meaning it supports (or aims to support) all of the Obsidian Markdown features

### About this guide
- This series of tutorials will guide you through the basics of creating a website using the MOGF approach
- By the end, you will be able to:
	- Create a website from scratch using Markdown and Flowershow
	- Edit your Flowershow website locally on your computer using Obsidian
	- Collaborate with others on your website project
	- Customise your website locally and preview your changes locally
- Let's get started! ['Start Now' button below]

## Tutorial 1: Create a website from scratch using Markdown and Flowershow

### 1. Introduction

- This is a tutorial for creating a website in markdown and published in Flowershow
- What you'll have by the end of this tutorial:
	- a working markdown-based website powered by Flowershow
	- be able to edit the text and add pages, all from an online interface without installing anything
- Screenshot of what the final result will look like

### 2. Prerequisites

- A GitHub account

### 3. Setting up a website

- Navigate to your Github account and create a new repository
- Give your repository a name
- Sign in to cloud.flowershow.app and create a new site (select repo created in step above)
- See your published website!

### 4. Editing a page on your website

- Navigate to the repository of your website on GitHub
- Navigate to the "content" folder
- Edit the "index.md" file
- Save your changes
- See your site getting rebuilt
- Preview your site after changes

### 5. Add a simple Markdown-based page
- Navigate to the "content" folder in your website's repository
- Create new file
- Write the content of the file
- Save your changes
- Preview your site after changes

### 6. What's next?
- Limitations of editing on GitHub UI - no offline working, adding multiple files, previewing markdown elements
- Using Obsidian to edit content locally on computer gets around these limitations

## Tutorial 2: Edit your Flowershow website locally on your computer using Obsidian

### 1. Introduction
- Recap - we have a markdown-based website on Flowershow which we have edited on GitHub
- Advantages of editing locally with Obsidian (see subsection 6 above)
- This tutorial walks you through editing website locally. By the end, you will learn how to:
	- clone repo on your computer
	- edit content with Obsidian
	- commit changes locally and push them back to the GitHub repo

### 2. Prerequisites
- A GitHub account
- Obsidian installed
- GitHub Desktop installed
- Tutorial 1 complete

### 3. Clone the GitHub repository on your computer
- Open GitHub Desktop app
- Click on "Clone a Repository from the Internet…"
- Select the repository you want to clone
- Choose where your repository should be saved
- Click "Clone" and wait for the process to complete

### 4. Edit your site in Obsidian
- Open Obsidian
- Open your repository's /content folder as vault
- Edit your site's content

### 5. Save and publish your changes
- Navigate to GitHub Desktop app
- Commit your changes
- Push your changes to the remote repository
- See updated site live!

### 6. What's next?
- What happens if more than one person want to make changes to the site?
- In next tutorial, we will learn how to create a new branch of the repository locally and then merge changes with the web version

## Tutorial 3: Collaborating with others on your website project

### 1. Introduction
- Recap
- In this tutorial, we will guide you through collaborating with others on the same website project using GitHub.
- By the end of this tutorial, you will:
	- Understand what a branch is and how to create one.
	- Understand what a pull request (PR) is and how to create one.
	- Learn how to review and merge a PR.
	- Know how to resolve conflicts if they arise.
	- Collaborate with others using GitHub, following best practices.

### 2. Create a new branch
- Navigate to your site's repository on GitHub
- Click on the 'Branch' dropdown menu, type a new branch name and press Enter
- Yay! You've created a new branch!

### 3. Make changes in the new branch
- Switch to the new branch in GitHub Desktop
- Open the /content folder of the repository in Obsidian
- Edit the about page
- Commit the changes in GitHub Desktop app and push them to the remote repository on GitHub

### 4. Create a pull request (PR)
- Go back to your site's repository on GitHub
- Click on 'New pull request'
- Select your branch from the dropdown menu
- Write a brief description of your changes, then click on 'Create pull request'
- Yay! Your changes are ready to be reviewed! 

### 5. Review and merge a pull request
- Navigate to the 'Pull requests' tab in your repository
- Open the newly created pull request
- Review the changes, add comments if necessary
- If everything is in order, click 'Merge pull request', then 'Confirm merge'
- Yay! You've merged your changes into the main branch!

### 6. Resolving conflicts
-  In case of conflicts between your changes and those on the main branch, GitHub will alert you
- Follow the on-screen instructions to resolve the conflicts and merge your changes

### 7. What's next?


## Tutorial 4: Customising your website locally and previewing your changes locally

### 1. Introduction

In this tutorial, we will dive into the more technical aspects of website customisation, but this time, everything will be done locally. You'll learn how to preview your site on your own machine before pushing changes to the live site, ensuring everything looks and works exactly as you want.

By the end of this tutorial, you will:

- Understand how to preview your site locally.
- Know how to change your website's title and description.
- Learn how to customise your website's appearance using Tailwind themes.
- Understand how to configure the navbar, navigation links, and logo.
- Learn how to integrate Google Analytics into your website.
- Be aware of additional customisation options for deeper customisation.

### 2. Previewing the site locally

- Navigate to your website's repository directory on your computer using command line
- Install the site's dependencies
- Start the local development server
- Visit the local address displayed in your command line. Yay! You can now preview your changes locally, live! 🎉

### 3. Changing the site title and description

- Perfect! You've personalised your site's title and description! 🎉

### 4. Configuring the title, description and navbar

- Open the `content/config.mjs` file in your code editor
- Edit the `title` and `description` fields
- Edit the fields in the `navbar` field to customise your navbar's title and logo. Then, add navigation links to `navLinks` field (these will be displayed in the navbar). Save and refresh your local site to see the changes.

### 5. Integrating with Google Analytics

- Still in the `content/config.mjs` file, navigate to the `analytics` field
- Enter your Google Analytics tracking ID, save and refresh your local site to ensure it's integrated correctly
- Excellent! Your website is now integrated with Google Analytics! 🎉

### 6. Customising the Tailwind theme

- Open `tailwind.config.js` file in your code editor
- Change the light and dark theme colours and fonts to your liking, save and refresh your local site to see the changes
- Awesome! Your website now has a new look! 🎉

When you're happy with all your changes, use GitHub Desktop to commit your changes and push them back to your GitHub repository.

In addition to these topics, the full tutorial shows you what other customisations options are available and where to find information on these.