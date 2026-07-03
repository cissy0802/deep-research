# When Writing Code Becomes Cheap: A Plain-Language Guide to the AI-Native Transformation

> This is the accessible edition of a longer essay. The deep-dive edition carries the full theoretical argument, every data source, and evidence grading; this one keeps the main line and says it plainly. All figures here were independently fact-checked — for sources, see the deep-dive edition.

## A strange thing is happening

Start with two sets of numbers that are both true and contradict each other.

In 2025, DORA — Google's long-running software engineering research program — surveyed nearly five thousand engineers: 90% use AI at work, and over 80% feel it has made them more productive. Yet the same research found, for the second year running, that **the more an organization adopts AI, the less stable its software delivery becomes** — unless it has solid automated testing, version control, and fast feedback loops.

Then there's the randomized controlled trial (the same method used to test new drugs). The research group METR recruited 16 veteran open-source maintainers and randomly assigned tasks on the large codebases they had maintained for years: half allowed to use AI, half not. The result: **tasks with AI took 19% longer on average.** The developers had predicted AI would make them 24% faster — and even after being measurably slowed down, they still believed they'd been sped up by 20%.

They felt faster. They were slower. And they couldn't tell.

That is the question this essay answers: **why does everyone feel faster with AI while organizations don't get faster — and get less stable?** The answer isn't complicated, but it changes almost every judgment about how "AI transformation" should be done.

## The cost didn't disappear — it moved

The total cost of software development splits roughly in two: the cost of **writing the code**, and the cost of **confirming the code is right** (reading it, reviewing it, testing it, integrating it, debugging it when it breaks).

For decades, writing was expensive, so the entire industry's way of organizing — team sizes, hiring bars, process design — was optimized around writing. AI has pushed the cost of writing toward zero, and many people assume total cost fell with it.

It didn't. **The cost moved from "writing it" to "confirming it's right."**

- Why were those 16 veteran developers slower? Screen recordings show their time shifting from writing code to prompting the AI, waiting for output, and then reviewing it line by line. In a complex codebase they knew well, writing was never the bottleneck — review was. AI made the non-bottleneck faster and the bottleneck more congested.
- An engineering-analytics company (Faros) analyzed telemetry from over ten thousand developers: heavy AI users merged nearly twice as many code changes — but each change was 1.5× bigger, review time rose 91%, and **the team's end-to-end delivery cycle didn't change at all.** Individual output piled up at the review stage and queued there.
- Why the instability? Change volume ballooned, but the "confirming" machinery — tests, staged rollouts, rollbacks — didn't get stronger with it, so errors slipped through. DORA's one-line summary is the best in the business: **AI doesn't fix a team; it amplifies what's already there.** Strong teams get stronger. Messy teams get messier.

This is the root of everything else in this essay: **organizational design in the AI era is a repositioning around the new bottleneck — verification.** Whoever internalizes that first won't waste their transformation.

## So what do the humans do?

Economists offer a useful frame (Agrawal, Gans & Goldfarb, the leading researchers on the economics of AI): treat AI as **a drop in the cost of prediction**. Writing code, autocompleting, executing — all essentially prediction work, and it keeps getting cheaper. **Judgment** — setting goals, setting standards, deciding what counts as good, accepting or rejecting the result — doesn't get cheaper. It gets *more* valuable precisely because prediction is now cheap.

Real-world data matches the frame. Anthropic analyzed hundreds of thousands of AI coding sessions: humans kept about 70% of the *planning* decisions and handed about 80% of the *execution* decisions to the AI. More striking: whether you can program barely affects your success rate at getting AI to produce working code (34% for coders, 29% for non-coders) — **what separates people is domain knowledge**. An expert who understands the business can direct the AI through a dozen correct steps with one instruction; someone without that knowledge can't steer it at all.

One extreme case pushed this to its limit. At Itaú, a heavily regulated Brazilian bank with old systems, a single engineer with 8 years of experience worked with a set of AI tools and delivered, in 3 sprints, a project scoped for a 4-person team over 6 sprints — with no quality discount (all integration tests passing, zero defects after launch). One case only, written up by the engineer himself, so don't generalize — but the retrospective is valuable: the speed didn't come from typing faster. It came from **collapsing what used to be days of back-and-forth between product, architecture, security, and QA into minutes of one person directing AI.** And every piece of rework in the project traced back to vague requirements and the old system's undocumented "unwritten rules."

So the scarcest person in the AI era is not "a programmer who can use AI." It is **someone who can articulate business knowledge into clear specifications and has the judgment to decide whether the output is acceptable.** If your hiring and promotion still price people by how fast they write code, you are pricing an asset in decline.

## Will companies get smaller?

"AI lets ten people do the work of a hundred — companies will shatter into tiny teams." That's the most popular prediction. The honest answer: **nobody knows, and the current evidence leans the other way.**

The flagship paper promoting the "firms will shrink" thesis doesn't survive scrutiny: no peer review, no empirical data at all, and its two authors founded a startup selling agent infrastructure — "companies will fragment" happens to be their product pitch. Meanwhile, peer-reviewed research in a top finance journal finds AI investment concentrating in **large** firms, making big companies bigger and industries more concentrated.

What's useful isn't picking a side — it's two indicators you can watch in your own organization: does your **per-change verification cost** grow linearly with change volume, or faster? If verification keeps getting cheaper, small-team futures have a chance; if verification stays your most expensive step, scale keeps winning. Anyone who claims to know the direction today is selling certainty beyond the evidence.

## If you run systems that must not fail

BigQuery-class infrastructure, payment rails, core banking — tens of millions of lines of code, decades of history, enormous request volumes, front-page news when they break. Nearly every AI transformation article these organizations read was written from a startup context, and **the startup playbook is not just useless to you — it's dangerous.**

**Why dangerous? One true story suffices.** On August 1, 2012, the market-maker Knight Capital deployed new code to only 7 of its 8 servers. The unpatched server activated a piece of code that had been retired for eight years but never deleted. In 45 minutes the firm lost over $460 million; within a year it lost its independence. Note the detail: before the market opened, the system had sent 97 error emails — but those emails "were not designed to be system alerts," and nobody read them. Now imagine AI generating code at ten times your current speed, in an organization where nobody deletes dead code and nobody owns the alerts. Legacy systems + high-velocity change + weak verification is the recipe for disaster; AI is an accelerant.

**Why unprofitable? The experiment above is the evidence.** METR's "19% slower with AI" result came from exactly this setting: senior engineers, million-line mature codebases, strict quality bars — **not exotic lab conditions; your organization's everyday reality.** The reason is plain: the hardest part of an old system is its unwritten rules — historical fixes for edge cases, undocumented behavioral dependencies, house conventions — precisely what an AI trained on public code knows least. And no, stuffing the whole codebase into a bigger context window doesn't work: measurements show model performance *degrades* as input grows, and oceans of similar-looking code act as interference.

**So where do you start? One task category has verified success records from multiple companies on giant legacy codebases: large-scale migrations and upgrades.** Old pattern to new pattern, test-framework replacement, language version upgrades — work that is tedious, universally avoided, and — crucially — **machine-checkable** (does it compile? do the tests pass?). Real numbers: Google used AI for code migrations with roughly three-quarters of the changes AI-generated and project time cut in half, restarting migrations that had been shelved for years; Airbnb moved 3,500 test files to a new framework — estimated at 1.5 engineer-years, done in 6 weeks.

And these companies' methods are strikingly consistent — copy them directly:

1. **AI only handles the middle**: deterministic tools find what to change, AI drafts the change, compilers and tests deliver the verdict — the AI never owns the merge decision.
2. **AI code goes through the same review and the same test gates as human code.** No express lane.
3. **Throttle by review capacity**: Google explicitly recorded slowing down AI generation because the bottleneck was how fast humans could review. Generation capacity is abundant; verification capacity is the valve.

The counter-example is just as real: in 2018, the UK bank TSB switched 5 million customers to a new system in one shot. Online banking collapsed, phishing fraud spiked 70-fold, total costs passed £300 million, and the regulator later fined the bank nearly £50 million. **Big-bang rewrites remain a death trap in the AI era.** AI didn't change the old rule — small steps, each verifiable, always reversible. It just made the most laborious part of the incremental path ten times cheaper.

Three steps for these organizations: **practice on migration tasks first** (building your own AI telemetry baseline as you go) → **guardrails before scale** (tests, staged rollout, rollback, review tooling — the "confirming" infrastructure comes first) → **treat verification capacity as a first-class asset** to invest in and measure — and set one rule: judge AI's benefit only by delivery data, never by gut feel. Remember the 40-percentage-point perception gap.

## How to actually drive the transformation

Four organizational rules, each backed by decades of management research:

1. **Transformation is hard because organizations are rational, not stupid.** A mature organization handed AI will instinctively use it to do the same things faster, rather than redesign how the work is done — a pattern confirmed again and again in innovation research. The consequence is marginal gains, while the real opportunity goes to someone else.
2. **Give the transformation its own walled garden.** Asking one team to protect delivery *and* reinvent the way it works fails. Spin up a separate small unit with different goals, incentives, and processes; let it redesign the work around AI's new cost structure; spread what works.
3. **Don't invert the sequence: fix the foundations, then scale AI.** AI amplifies what you already are. A team with shaky testing and release discipline that adopts AI first will harvest instability, then lose its second chance when trust collapses. For teams with solid fundamentals, AI's dividend compounds.
4. **The real bottleneck is the executive layer.** Whether engineers adopt tools was never the hard part (one experiment found 30–40% never touched a free, management-endorsed tool — time fixes that). The hard part is the decisions only leadership can make: moving investment from generation capacity to verification infrastructure, and repricing talent from execution to judgment.

## Three things to remember

1. **Faster individuals ≠ a faster organization.** The cost moved from writing code to confirming it's right; without upgrading verification, AI just helps you produce problems faster.
2. **Trust data, not feel.** The senior engineers slowed down by AI were convinced it sped them up. Evaluate AI with delivery cycle time, change failure rate, and review latency.
3. **Legacy organizations: enter through migrations, guardrails before scale.** It is the only path with real success records from multiple major companies — and the big-bang rewrite is still a death trap.

*For the full arguments, every source, and the counter-evidence, read the deep-dive edition: "When Code Becomes Cheap: Theory and Evidence for the AI-Native Transformation of Software Organizations."*
