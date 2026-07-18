---
name: write-like-me
description: Polish and rewrite AI-generated or drafted text to match a specific person's voice and writing style. Use when the user wants output to sound like them (or a specified voice) rather than generic AI. Loaded on demand at the writing/polishing stage, not at conversation start.
metadata:
  author: soundlikeme
  version: "0.1"
---

# Write Like Me

You are rewriting or polishing text to match a specific voice. Follow these layers in order:

## Step 1: Load the Voice Profile

Check for a voice profile in one of these locations (in priority order):

1. A file the user points you to
2. `references/voice-profile.md` in this skill directory
3. If no profile exists, tell the user: "No voice profile found. Either provide one, or use the `voice-extractor` skill to generate one from writing samples."

Read the voice profile before proceeding.

## Step 2: Apply Concise Writing Rules

Regardless of the voice profile, apply these baseline rules. They override the voice profile if there is a conflict. (Based on Strunk & White's *Elements of Style* -- for the full original rules, see `references/elements-of-style.md` if available, or install from [github.com/obra/the-elements-of-style](https://github.com/obra/the-elements-of-style).)

1. **Omit needless words.** Every word must earn its place. Cut filler phrases entirely.
   - "in order to" -> "to"
   - "the question as to whether" -> "whether"
   - "he is a man who" -> "he"
   - "the reason why is that" -> "because"

2. **Use concrete, specific language.** Vague claims hide weak thinking. Pin things down.
   - Bad: "Significant revenue growth was achieved across multiple segments."
   - Good: "Revenue grew 30% in Q3, driven by enterprise sales."

3. **Prefer active voice.** Active voice is shorter and clearer. Use passive only when the actor is unknown or irrelevant.
   - Bad: "The feature was shipped by the team after testing was completed."
   - Good: "The team shipped the feature after testing."

4. **Lead with the point.** State your conclusion, then support it. Don't make the reader wait.
   - Bad: "After careful analysis of the data and consideration of several factors, we concluded that..."
   - Good: "We should cancel the project. The data shows..."

5. **Put statements in positive form.** Say what something *is*, not what it *isn't*. Negatives are harder to parse.
   - Bad: "He was not very often on time."
   - Good: "He usually came late."

6. **One idea per sentence.** If a sentence carries two ideas, split it. If a paragraph drifts to a second topic, break it.

7. **Don't hedge unless genuinely uncertain.** Hedging weakens everything around it.
   - Bad: "This may potentially have an impact on performance."
   - Good: "This slows performance." (Or if uncertain: "I'm not sure whether this affects performance.")

8. **Use plain words.** Fancy synonyms don't make you sound smarter.
   - "use" not "utilise" / "help" not "facilitate" / "method" not "methodology" / "start" not "commence" / "about" not "with regard to"

9. **Cut qualifiers.** "Very", "really", "quite", "somewhat", "fairly" almost always weaken. Remove them and see if the sentence is better. It usually is.

10. **Vary sentence length for rhythm.** Default to short. Use a longer sentence occasionally to carry a complex idea, then follow it with a short one. This creates pace.

11. **Place emphatic words at the end.** The end of a sentence carries the most weight.
    - Weak: "Failure was, in the end, the result."
    - Strong: "In the end, the result was failure."

12. **No filler transitions.** "Furthermore", "Moreover", "Indeed", "Additionally", "It's important to note that" -- cut these. If the next sentence follows logically, it doesn't need a signpost.

## Step 3: Ban AI Anti-Patterns

Never use these in the output. If they appear in the draft, replace them.

**Banned words/phrases:**
- delve, realm, tapestry, landscape (metaphorical), leverage (as verb), utilise, facilitate, endeavour
- "In today's [adjective] world/landscape/environment"
- "Let's dive in", "Let's unpack this"
- "At the end of the day"
- "Revolutionise", "game-changer", "cutting-edge", "innovative" (unless literally describing an innovation)
- "It's important to note that..."
- "Transformative", "paradigm shift", "synergy"

**Banned structural patterns:**
- Snappy triads: "Fast, efficient, and reliable." (Don't string three adjectives for rhetorical effect)
- Negation flips: "It's not X -- it's Y." / "No X, no Y, just Z."
- Unearned profundity: "Something shifted." / "And that changes everything."
- Rhetorical questions as transitions: "But what does this really mean?"
- False build-ups: "The solution? It's simpler than you think."
- Ending with inspirational calls-to-action unless the user asked for one
- Summarising what was just said: "In summary..." / "As we've seen..."

## Step 4: Rewrite

With the voice profile, conciseness rules, and anti-patterns all loaded:

1. Read the draft text the user wants polished
2. Rewrite it to match the voice profile while applying all rules above
3. Keep the same structure and ideas -- don't add or remove points unless the user asks
4. Present the rewritten version
5. If you changed the structure or emphasis significantly, briefly note what you changed and why

## Notes

- This skill is for the **polish/rewrite step**, not for initial drafting. The user will have already generated or dictated content.
- Keep the rewritten output roughly the same length or shorter. Never inflate.
- When in doubt between matching the voice profile and following the conciseness rules, prefer conciseness. Good writing is the floor; voice is the layer on top.
