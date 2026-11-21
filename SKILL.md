---
name: human-voice
description: Use when writing or rewriting anything that goes out in the owner's name (captions, posts, site copy, bios, emails, application essays and statements). Asks the owner three questions, builds the text from their answers word for word, never invents a detail, and runs a checker for the patterns that make text read as machine-written.
---

# Human voice

Text written for someone reads as machine-written for one main reason: the model makes up sentences the person never
said (a sunrise, a mom, a "journey"). Polishing the style doesn't fix it. Humanizer prompts and repos that only
rewrite style still get flagged; what worked in a side-by-side test was making the model ask the person three
questions and use the answers word for word. This skill is that method, plus a checker.

## When to use
Any public or outgoing text in the owner's name: social captions, posts, site copy and project blurbs, bios, emails
and letters they send, application essays and statements (where AI policy allows any help at all; see below).
Not for internal notes, specs, commit messages or replies to the owner.

## Steps
1. **Start from a draft or a brief.** If there's a draft (yours, theirs, another tool's), keep it as the thing to
   rewrite. If there's only a brief, write a plain fact list, not prose.
2. **Cut.** Delete every line another AI would also write: openers, scene-setting, morals, "in a world where",
   summaries of what was just said. Delete every detail the owner didn't give you or that isn't in their files.
3. **Ask exactly three questions**, in one message, before writing anything final. Ask for the things only they
   know: what actually happened, why they made it, a concrete detail (a material, a mistake, a number, who it's
   for), how they'd say it to a friend. Short questions, no options to pick from (options put words in their mouth).
4. **Build from their answers word for word.** Their phrases go in as written. Fix spelling and grammar only. Don't
   add a single sentence they didn't say; joining words and the facts already in the brief (names, dates, sizes,
   prices) are the only additions.
5. **Check.** Run `python3 scripts/voice_check.py <file>` (or pipe the text in). Fix every hit, then run it again.
6. **Show the owner the text and which words were theirs.** They approve it before it goes out.

The owner may skip the questions ("just write it"). Then write the shortest plain version from facts on file,
run the checker, and say which lines are yours so they can swap in their own words.

## Banned patterns (the checker catches most)
- Em dashes, and en dashes used as dashes. Use a full stop or a comma.
- Lists of three ("bold, timeless and handmade"), and three-beat sentences.
- "X for Y" and "not X, but Y" swaps ("trading spreadsheets for sourdough", "it's not a chair, it's a statement").
- Stock words: delve, tapestry, testament, journey, elevate, seamless, curated, unleash, vibrant, realm, crafted with
  care, labor of love, more than just, whether you're, in today's world, let's dive in.
- Invented scenes or people: sunrises, family members, "I remember the first time" unless the owner said it.
- Closing morals, rhetorical questions, emoji strings, hashtags inside sentences.

## The prompt (to paste into any chat model, e.g. when offloading)
```
Rewrite this so it sounds like me, not AI.
1. Delete any line another AI would also write.
2. No lists of three. No "X for Y" swaps. No em dashes.
3. Never invent a detail. Ask me 3 questions first.
4. Use my answers word for word. Fix only grammar. Don't add a single sentence I didn't say.
[paste the draft here]
```

## Rules
- Never fake the owner's voice where it isn't allowed. Many schools and some publications forbid AI-written text:
  give questions, outlines and line edits only, and the owner writes the prose.
- Never invent a fact, quote, client, award or number to make text sound real.
- The checker is a floor, not a pass mark. A clean run doesn't mean it sounds like them; their own words do.
- Don't promise text will pass an AI detector. The point is that it says what they'd say.

## Excuses that don't count
| The excuse | What to do instead |
|---|---|
| "I know enough about the project to fill in the story" | Ask the three questions. Facts on file are fine; the story is theirs. |
| "One small invented detail makes it vivid" | That detail is exactly what reads as fake. Cut it or ask for a real one. |
| "Their answer is clunky, I'll smooth it" | Fix grammar only. Clunky and theirs beats smooth and generic. |
| "The checker passed, so it's done" | Read it aloud as them. Then show them. |
| "They're busy, I'll skip the questions" | Ask once, in one message. Skip only when they say to. |

## Keep this skill improving
When a piece of text gets rejected as "doesn't sound like me", or a new tell turns up, add it (dated) to
`references/tells.md`, add a pattern to `scripts/voice_check.py` if a regex can catch it, and publish with the
skills publish script. No private data.
