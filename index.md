---
title: "The Way of Markdown. Own the source. Compose with anything."
description: "Websites, knowledge bases, blogs, even a Notion replacement — built from plain text files you own, with tools you can swap anytime. Markdown is quietly everywhere; here's the way to make it work for you."
layout: plain
showHero: false
---

<main class="wom-home mx-auto w-full max-w-6xl px-5 py-12 sm:px-8 sm:py-16 lg:px-10 lg:py-20">
  <section class="mx-auto flex max-w-4xl flex-col items-center text-center">
    <h1 class="m-0 text-4xl font-medium leading-none tracking-tight text-stone-800 dark:text-stone-100 sm:text-6xl lg:text-7xl">The Way of Markdown</h1>
    <div class="mt-6 w-full max-w-xl sm:mt-8" style="aspect-ratio:16/9;">
      <video class="block h-full w-full" src="/assets/way-of-markdown.mp4" autoplay muted loop playsinline aria-label="A figure in profile, written in Markdown punctuation, performing a tai chi movement"></video>
    </div>
    <p class="mt-5 text-2xl font-medium leading-tight text-stone-700 dark:text-stone-200 sm:text-3xl">Own the source. Compose with anything.</p>
    <p class="mt-6 max-w-3xl text-lg leading-8 text-stone-600 dark:text-stone-300 sm:text-xl">Websites, knowledge bases, blogs, even a Notion replacement — built from plain text files you own, with tools you can swap anytime. Markdown is quietly everywhere; here's the way to make it work for you.</p>
    <div class="mt-8 flex w-full flex-col justify-center gap-3 sm:w-auto sm:flex-row">
      <a class="rounded-xl border border-green-600 bg-green-600 px-6 py-3 text-base font-bold text-white no-underline shadow-sm transition hover:border-green-700 hover:bg-green-700 sm:text-lg" href="/roadmap">Start the roadmap 🗺️</a>
      <a class="rounded-xl border border-green-600 px-6 py-3 text-base font-semibold text-stone-700 no-underline transition hover:bg-green-50 dark:text-stone-100 dark:hover:bg-green-950 sm:text-lg" href="/basics">New here? Markdown in 10 minutes</a>
    </div>
  </section>

  <section class="mt-16 border-t border-stone-200 pt-12 dark:border-stone-700 sm:mt-20 sm:pt-16" aria-labelledby="source-and-output">
    <h2 id="source-and-output" class="sr-only">Markdown source and rendered output</h2>
    <div class="grid items-stretch gap-5 lg:grid-cols-2">
      <div class="min-w-0 overflow-hidden rounded-2xl border border-stone-300 bg-white/40 dark:border-stone-700 dark:bg-stone-900/30">
        <div class="border-b border-stone-300 px-5 py-3 font-mono text-sm leading-6 text-stone-500 dark:border-stone-700 dark:text-stone-400">notes/reading-list.md — plain text, yours forever</div>
        <pre class="m-0 overflow-x-auto bg-transparent p-5 text-sm leading-7 text-stone-800 dark:text-stone-100 sm:p-6 sm:text-base"><code>&#35; My reading list

Books I &#42;&#42;actually&#42;&#42; finished:

&#124; Book &#124; Year &#124; Done &#124;
&#124;&#45;&#45;&#45;&#45;&#45;&#45;&#124;&#45;&#45;&#45;&#45;&#45;&#45;&#124;&#45;&#45;&#45;&#45;&#45;&#45;&#124;
&#124; The Dispossessed &#124; 1974 &#124; ☐ &#124;
&#124; File over app &#124; 2023 &#124; ☑ &#124;

&#96;&#96;&#96;mermaid
graph LR
  A[write] &#45;&#45;&gt; B[store] &#45;&#45;&gt; C[publish]
&#96;&#96;&#96;

&#62; Plain text never goes out of fashion.</code></pre>
      </div>
      <div class="overflow-hidden rounded-2xl border border-green-500 bg-white/40 dark:bg-stone-900/30">
        <div class="border-b border-green-400 px-5 py-3 font-mono text-sm leading-6 text-green-600 dark:text-green-400">the same file, rendered — by any tool, today or in 2046</div>
        <div class="p-5 sm:p-6">
          <h3 class="m-0 text-3xl font-bold text-stone-800 dark:text-stone-100">My reading list</h3>
          <p class="mt-4 text-lg text-stone-700 dark:text-stone-200">Books I <strong>actually</strong> finished:</p>
          <div class="mt-5 overflow-x-auto">
            <table class="w-full border-collapse text-left text-base text-stone-700 dark:text-stone-200">
              <thead><tr class="border-b-2 border-stone-300 dark:border-stone-600"><th class="px-2 py-2">Book</th><th class="px-2 py-2">Year</th><th class="px-2 py-2">Done</th></tr></thead>
              <tbody>
                <tr class="border-b border-stone-200 dark:border-stone-700"><td class="px-2 py-2">The Dispossessed</td><td class="px-2 py-2">1974</td><td class="px-2 py-2">☐</td></tr>
                <tr><td class="px-2 py-2">File over app</td><td class="px-2 py-2">2023</td><td class="px-2 py-2">☑</td></tr>
              </tbody>
            </table>
          </div>
          <div class="mt-6 flex flex-wrap items-center gap-2 text-sm text-stone-600 dark:text-stone-300">
            <span class="rounded-md border border-green-500 px-3 py-1">write</span><span aria-hidden="true">→</span>
            <span class="rounded-md border border-green-500 px-3 py-1">store</span><span aria-hidden="true">→</span>
            <span class="rounded-md border border-green-500 px-3 py-1">publish</span>
          </div>
          <blockquote class="mt-6 border-l-4 border-green-500 pl-5 text-xl italic leading-8 text-stone-600 dark:text-stone-300">Plain text never goes out of fashion.</blockquote>
        </div>
      </div>
    </div>
    <p class="mx-auto mt-8 max-w-3xl text-center text-lg italic leading-8 text-stone-600 dark:text-stone-300">Tables, task lists, diagrams — all still plain text. That's the whole trick, and it goes remarkably far.</p>
    <p class="mt-6 text-center"><a href="/playground.html" class="inline-block rounded-xl bg-green-600 px-7 py-3 text-lg font-bold text-white no-underline shadow-md shadow-green-600/20 transition hover:bg-green-700">🎮 Try it yourself in the playground</a></p>
  </section>

  <section class="mx-auto mt-20 max-w-3xl sm:mt-24" aria-labelledby="why-markdown-wins">
    <h2 id="why-markdown-wins" class="text-3xl font-bold tracking-tight text-stone-800 dark:text-stone-100 sm:text-4xl">Why markdown wins</h2>
    <p class="mt-5 text-lg leading-8 text-stone-700 dark:text-stone-300">The whole syntax takes <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/basics">ten minutes</a> to learn, and then it's <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/why">yours</a>: plain files on your disk, still readable in fifty years, which is more than your .docx files can promise (<a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/timeline">the history</a> is instructive here). The rest of the world has quietly agreed. <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/markdown-in-chatgpt">Every AI speaks markdown</a>, <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/everywhere">most of the apps you already use</a> handle it, and you can put diagrams, databases and whole tools <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/pluggable-markdown">inside three backticks</a>.</p>
  </section>

  <section class="mt-20 sm:mt-24" aria-labelledby="what-will-you-build">
    <div class="mx-auto max-w-3xl text-center">
      <h2 id="what-will-you-build" class="text-3xl font-bold tracking-tight text-stone-800 dark:text-stone-100 sm:text-4xl">What will you build?</h2>
      <p class="mt-5 text-lg leading-8 text-stone-700 dark:text-stone-300">Nobody cares about markdown, the same way nobody cares about ASCII. You care about the thing you want to make — and there's a guide for each:</p>
    </div>
    <div class="mt-9 grid grid-cols-2 gap-3 sm:grid-cols-4 sm:gap-4">
      <a href="/markdown-websites" class="rounded-xl border border-stone-300 p-4 text-center font-bold text-stone-800 no-underline transition hover:border-green-500 hover:shadow-md dark:border-stone-700 dark:text-stone-100 dark:hover:border-green-500">🌐 Website</a>
      <a href="/markdown-knowledge-bases" class="rounded-xl border border-stone-300 p-4 text-center font-bold text-stone-800 no-underline transition hover:border-green-500 hover:shadow-md dark:border-stone-700 dark:text-stone-100 dark:hover:border-green-500">🧠 Knowledge base</a>
      <a href="/markdown-notion-alternative" class="rounded-xl border border-stone-300 p-4 text-center font-bold text-stone-800 no-underline transition hover:border-green-500 hover:shadow-md dark:border-stone-700 dark:text-stone-100 dark:hover:border-green-500">🚪 Notion escape</a>
      <a href="/markdown-blogs" class="rounded-xl border border-stone-300 p-4 text-center font-bold text-stone-800 no-underline transition hover:border-green-500 hover:shadow-md dark:border-stone-700 dark:text-stone-100 dark:hover:border-green-500">✍️ Blog</a>
      <a href="/markdown-databases" class="rounded-xl border border-stone-300 p-4 text-center font-bold text-stone-800 no-underline transition hover:border-green-500 hover:shadow-md dark:border-stone-700 dark:text-stone-100 dark:hover:border-green-500">🗃️ Database</a>
      <a href="/markdown-wikis" class="rounded-xl border border-stone-300 p-4 text-center font-bold text-stone-800 no-underline transition hover:border-green-500 hover:shadow-md dark:border-stone-700 dark:text-stone-100 dark:hover:border-green-500">👥 Team wiki</a>
      <a href="/markdown-digital-gardens" class="rounded-xl border border-stone-300 p-4 text-center font-bold text-stone-800 no-underline transition hover:border-green-500 hover:shadow-md dark:border-stone-700 dark:text-stone-100 dark:hover:border-green-500">🌱 Garden</a>
      <a href="/markdown-based" class="rounded-xl border border-green-500 bg-green-50 p-4 text-center font-bold text-green-800 no-underline transition hover:bg-green-100 hover:shadow-md dark:bg-green-950 dark:text-green-300 dark:hover:bg-green-900">✨ All guides</a>
    </div>
  </section>

  <section class="mt-20 sm:mt-24" aria-labelledby="start-here">
    <div class="mx-auto max-w-3xl text-center">
      <h2 id="start-here" class="text-3xl font-bold tracking-tight text-stone-800 dark:text-stone-100 sm:text-4xl">Start here</h2>
      <p class="mt-5 text-lg leading-8 text-stone-700 dark:text-stone-300">There are two ways in, and they walk the same path:</p>
    </div>
    <div class="mt-9 grid gap-5 md:grid-cols-2">
      <article class="rounded-2xl border border-stone-300 p-6 dark:border-stone-700 sm:p-8">
        <h3 class="text-xl font-bold text-stone-800 dark:text-stone-100">🚀 “I want to publish something”</h3>
        <p class="mt-4 text-base leading-7 text-stone-700 dark:text-stone-300">A website, a blog, a page on the web. <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/roadmap">The roadmap</a> starts at the syntax and has you live by step ②, today. Prefer working straight through? <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/learn">The tutorial series</a> goes from zero to a published site.</p>
      </article>
      <article class="rounded-2xl border border-stone-300 p-6 dark:border-stone-700 sm:p-8">
        <h3 class="text-xl font-bold text-stone-800 dark:text-stone-100">📝 “I want better notes”</h3>
        <p class="mt-4 text-base leading-7 text-stone-700 dark:text-stone-300">A knowledge base, a second brain, published later or never. Start the same way, then <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/learn/howtos/create-a-simple-catalog-of-anything">build a catalog of anything</a> and read <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/markdown-database">the pattern behind it</a>.</p>
      </article>
    </div>
    <p class="mx-auto mt-9 max-w-3xl text-center text-base leading-7 text-stone-600 dark:text-stone-300">Never touched markdown? <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/basics">The basics</a> take ten minutes, or <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/playground.html">try it live</a> right now. Onboarding a team? The <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/learn/onboarding">step-by-step path</a> sequences the whole thing with checkpoints. Already fluent — go poke around the <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/kb">reference shelf</a>, the <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/videos">videos</a>, the <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/kb/canon">canon</a> or the <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/blog">blog</a>.</p>
  </section>

  <footer class="mt-20 border-t border-stone-200 pt-8 text-center text-sm italic leading-6 text-stone-500 dark:border-stone-700 dark:text-stone-400 sm:mt-24">
    Made by <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/about">Rufus Pollock</a> and <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="https://datopian.com/">folks at Datopian</a>, as markdown files <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="https://github.com/flowershow/wayofmarkdown">in the open</a>. This page is itself markdown with a little HTML in it — <a class="text-green-700 underline decoration-green-600/40 underline-offset-4 dark:text-green-400" href="/markdown-websites">which is rather the point</a>.
  </footer>
</main>
