# Is It Really Better to Write a Spec First and Then Let AI Write the Code? (Plain-Language Edition)

> This is the plain-language edition, written for people who don't write code, or who have only just started using AI to write code. For the source of every number, the original quotes and the strength of the evidence, see the [deep dive](https://hub.cissychen.com/deep-research/spec-driven-development-deep.en.html). All figures are as of November 2026.

## First, what is this piece asking?

Lots of people now use AI to write programs. The earliest approach was "say whatever comes to mind" and let the AI guess as it writes, which came to be called vibe coding. Since 2025 a new approach has caught on: **first write up what you want built as a detailed instruction document (a spec), then have the AI write the code by following it.** This is called "spec-driven development." GitHub, Amazon (AWS) and quite a few startups have all launched dedicated tools for it.

Supporters say: AI programming finally has some rules. Critics say: isn't this just the "waterfall development" of decades ago—lock down the documents first, then start building—under a new name?

There are really three questions wrapped up in this:

1. If you write a spec first, does the AI produce something better?
2. Once the spec is written, will it gradually drift out of step with the code?
3. In the future, could you change only the spec and have the AI regenerate the code automatically?

## 1. Spelling out what you want first really does make AI write better

**There is solid evidence for this.** Several groups of researchers have run the same kind of experiment: for the same task, the more complete the instructions given to the AI, the more it gets right; strip the instructions away bit by bit and the success rate drops bit by bit; add them back and it rises again. Having the AI list a plan before writing code helps too.

But there are two caveats:

- **The stronger the model, the smaller this benefit.** Older models from 2023 gained a lot from "plan first"; today's strong models gain much less.
- **The cost is not small.** In one 2026 study, having the AI write a spec before writing code passed a few more percentage points of tests, but cost anywhere from half again to more than double the money.

## 2. But there's no evidence that "running the full process with a dedicated tool" is better

This is the crux. What those experiments show is that "**stating your intent clearly**" helps—not that "**following some spec tool's seven-step process**" helps. The real comparison should be: given the same information, which is better—writing it as one clear paragraph and handing it straight to the AI, or going through the whole Spec Kit process?

The two comparisons of this kind that we found both fail to hold up under scrutiny:

- One is a paper that hasn't been formally published. The two sides were given different amounts of time (90 minutes for one, 40 minutes for the other), and only the finished attempts were scored, so the two scores can't be compared. It shows only one thing: **running the full process is slower.**
- The other is a test run by an outsourcing company itself, and it has spread widely online. We recalculated its published raw data line by line and found that dozens of rows described as a "re-run by different people" were in fact the first round's data with some edits; the way costs were calculated was also inconsistent. **We use none of its numbers.**

Several experienced engineers have tried it themselves, and their impressions agree: to fix one small bug, the tool generated 16 acceptance criteria, "like using a sledgehammer to crack a nut"; one tech lead said that without this process he was "around ten times faster", and the code the process produced was no better either.

## 3. Will the spec gradually drift out of step with the code?

**Yes—and right now we can't even measure how much accurately.**

- The biggest spec tool, GitHub Spec Kit, says in its documentation that "Specifications stay in sync with code because they generate it." Yet in its own code repository, it has set the spec folders to be ignored by version control, so they are never saved.
- The complaint this tool's users raise most often: **once written, the specs are hard to change and can't keep up with changes to features.**
- One research team interviewed 21 people using this method, and most said their specs and code had fallen out of step.
- In public data, roughly 20% to 40% of projects that installed this tool have never written a single formal spec.
- Some people have removed it from their projects, for a typical reason: "a reviewed, confirmed issue *is* the specification," and the process tools "were carrying cost without carrying work."

This is a lot like the UML diagramming tools of twenty years ago: a survey of 50 developers back then found not one who was using them fully; most drew a sketch to think things through and then threw it away.

## 4. Change only the spec and have the code generated automatically—can that work?

**Mathematics has already tried it for us, and the results aren't encouraging.**

Mathematicians write proofs in a language that a computer can check line by line. The computer can guarantee that "the proof is correct," but it can't guarantee that "the statement being proved is the statement you originally meant to prove." Two independent teams went through the same set of math problems one by one and found that **a large number of problems had been translated into statements with a different meaning**; across all the problems, more than a quarter had been translated into statements that can be proved false. The computer still "correctly" finished the proofs.

Software is the same. Microsoft researchers had AI write specs, code and proofs for more than 50 classic algorithms, and every one passed the computer's checks; on closer inspection, the specs themselves had holes for 8 of the algorithms—for example, letting a wrong answer through. Another study found that **an empty program that does nothing and just replies "OK" can pass every test written from the spec.**

Specs written in everyday language don't even have the "computer checks the proof" step. So for "just change the spec," there's no workable path in sight today. The company that pushed this hardest (Tessl) no longer says so on its current homepage.

## 5. The most-quoted numbers on both sides don't hold up

- Supporters often say "research shows up to 50% fewer errors": traced back to the source, the article being cited contains no data at all.
- Supporters also say "73% fewer security vulnerabilities": that was one person writing the same program twice.
- Critics often say "research proves specs don't reduce bugs": what that study actually measured was "whether a code change had a task number attached," and the classifier it used was faulty, misclassifying about 14% of the samples.
- The slogan "specs are the new code" is often attributed to a researcher at OpenAI. He didn't say it; it's the web address of the talk's page.
- "Fixing an error costs $1 at the requirements stage and $100 after launch": this comes from a chart about large projects in the 1970s whose original data was never made public; for small projects the difference is only two to four times.

There's also a historical joke: the 1970 paper treated as the origin of "waterfall development" never uses the word "waterfall" anywhere in it. The author actually considered going straight through in one pass "risky and invites failure," and his prescription was **to write more documentation**—even more than today's spec tools ask for.

## 6. Who is doing the talking

- The companies selling the tools (GitHub, Amazon, Tessl) have never published controlled experiments showing their own tools make code better. Amazon's pricing, on the other hand, admits it costs more: requests run through the spec process, once over the allowance, cost 5 times as much per request as ordinary ones.
- These companies themselves also say: small changes don't need to go through the whole process.
- Among the people online defending and criticizing this method, there are interested parties on both sides: some work at companies selling the tools, and some draw their examples from their own products.

## The things that matter most

1. **Spelling out what you want really does make AI write better**—but the benefit is shrinking, and the cost is not small.
2. **There's no reliable evidence that a "dedicated spec-tool process" beats "one clearly written paragraph"**; what is certain is that it's slower and more expensive.
3. **Specs drift out of step with code**, and today we can't even measure it accurately; the biggest tool doesn't even save its own specs.
4. **"Change only the spec and have the code generated automatically" has already hit a wall in mathematics**: a computer can check whether a proof is right, but not whether the problem statement is right.
5. **The popular numbers on both sides don't stand up**; when you hear "research shows," first ask: what did it measure, and who did it?
6. **The most likely ending looks like UML**: people keep the habit of "think it through first and write it down," and drop the heavy tools and processes.
