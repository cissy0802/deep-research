# AI Reviews the Code — Who Reviews the AI? (Plain-Language Edition)

> This is the condensed version of the deep-dive essay of the same name. The deep dive has the full argument chain, every data source, and evidence grading; this version keeps the main line and says it plainly. The key numbers have been independently fact-checked (data as of July 2026).

## The one-sentence answer

AI writes code faster and faster, and the humans who check that code can't keep up — that problem is real. The industry's prescription is "buy another AI to check the code." That medicine **genuinely works in narrow settings, but in exactly the places where you need it most, it's more like nesting dolls**: an error-prone AI checking another error-prone AI — and the two are making increasingly similar errors.

## Why checking code became the bottleneck

First, is the demand real? AI has sped up the writing of code, but every line still has to be confirmed correct by someone before it ships — that step is called code review. Three unrelated data sources point the same way:

- The number of code submissions (PRs) merged on GitHub each month is up 23% year over year — the flood is here;
- A telemetry firm monitoring 22,000 engineers found that in periods of heaviest AI use, the median time to review a PR was **up 441%** from the low period, PRs merged with no review at all were up 31%, and incidents per PR were up 243% (this is the vendor's own monitoring data, not a strict experiment — but two other firms' data points the same way);
- Google's own paper says it in black and white: during internal AI-driven code migrations, "The bottleneck in the process was the speed at which engineers could review the changes. We purposefully limited the number of changes we generate every week to avoid overwhelming reviewers."

Fast to write, slow to check, traffic jammed at the checkpoint — the diagnosis holds. The problem is the prescription.

## Why you can't just trust the sellers' report cards

How do AI code review tools prove they work? They publish report cards. But those report cards follow one rule: **whoever runs the exam comes first.** By early 2026, at least six vendors had published their own evaluation benchmarks, and the publisher ranked #1 in every single one. One vendor's tool "catches 82% of bugs" on its own exam; a competitor re-tested it on the same five codebases and it scored 45; on a third company's exam, **roughly 5 out of every 6 of its comments pointed at things that weren't real bugs at all**. Same tool, three exams, three wildly different grades.

Then an independent research lab finally launched a leaderboard with no dog in the fight. Within about a month, three vendors each published a blog post declaring "we're #1" — one on the composite score, one on a single sub-metric, and one using a special lab-preview version to take first place (its actual shipping product ranked fourth).

The trick here was actually solved by science sixty years ago: **saying "we catch X% of bugs" without saying "and here's how many false alarms we raise" is meaningless** — turn any detector's sensitivity up and it will "catch more bugs," at the cost of drowning you in false alarms. And false alarms are the most expensive thing in code review, because they burn the one resource engineers are already short on: attention. Next time you see "we catch X% of bugs," ask one question: what's the false-alarm rate? If they won't say, grade it as a fail.

## How is it going for the companies using it on themselves?

The really valuable data comes from companies that use AI code review on their own code and honestly publish the funnel.

**Google**: AI-suggested edits ended up resolving **7.5%** of all human reviewer comments. Not 75% — 7.5%. And Google's paper admits that every metric they can measure is only an "easier-to-measure proxy" for productivity; how many real bugs the AI caught, nobody can measure.

**Meta**: their code-fixing AI scores **68** on their own curated exam; in real production, the share of its fixes that engineers actually accepted was **19.75%**. Between the offline score and real-world value lies a full order of magnitude. The same paper has an even more telling experiment: Meta showed AI-generated fix suggestions to code reviewers — and reviews got **5.5% slower** (statistically significant). The AI's output had itself become a new burden on the reviewer. The fix? Not a better model. They **hid the AI's suggestions from reviewers**.

**Independent research** fills in the other side: comments from open-source AI review tools led to actual code changes only **0.9% to 19.2%** of the time, versus 60% for human review comments. And when someone ran four leading tools in parallel on the same 146 real PRs, **93.4% of the issues were flagged by exactly one tool, and zero issues were flagged by all four** (the author works at one of the four vendors — noted — but the data is open-source and checkable). Four "inspectors" with almost no agreement on what counts as a problem: what they produce looks less like verification and more like opinions.

## Where exactly the nesting dolls are

The deepest problem isn't that these tools aren't good enough yet. It's structural.

First, **the AI inspector invents bugs**. OpenAI trained a model specifically to critique code (CriticGPT). The positive results are real: its critiques were preferred over human contractors' in 63% of comparisons, and human-plus-AI teams reviewed more thoroughly than humans alone while hallucinating less than the AI alone. But in the same paper's abstract, the authors wrote one devastating sentence: the bugs the AI critic hallucinates "could mislead humans into making mistakes they might have otherwise avoided." The inspector is not a neutral filter — it injects new errors into the process.

Second, **AIs are making increasingly similar mistakes**. Using a second AI to check the first assumes their blind spots differ. But a 2025 study found the opposite trend: the more capable models get, the **more similar** their errors become. When the AI that writes the code and the AI that checks it share blind spots, stacking more layers of checking still misses the same bugs. That's the mathematically precise meaning of "nesting dolls": layer inside layer, same pattern painted on every one.

Third, **counting on humans as the final gate is a plan that was sentenced to death in 1983**. Forty years of human-factors research concluded: asking a person to watch an automated system that's right most of the time, just to catch its rare mistakes, gives "the human monitor an impossible task"; the complacency and over-trust that automation induces "cannot be prevented by training or instructions." A 2026 eye-tracking experiment confirmed it: tell reviewers "this code was written by an AI" and they stare at it longer — **but review it no more thoroughly**. And the most realistic picture comes from large-scale observation of AI-generated PRs: **most AI-written PRs get no human review at all, and where "someone" does review them, that someone is usually another AI.**

## So when does it actually work?

Flip the evidence over and AI code review genuinely pays off when three conditions hold at once:

1. **A referee that isn't an AI has the final say.** Why did Google's migration projects succeed? Because every AI change had to pass the compiler, pass the tests, and go through exactly the same review pipeline as human code — the AI was one stage of an assembly line, not the judge. High test coverage and uniform changes (code migrations, dependency upgrades) are where the evidence for AI review is most solid.
2. **False alarms are taken seriously.** The production systems that survive share one trait: they crush false positives first and brag about catch rates second. ByteDance added a dedicated filter layer before humans see anything; GitHub's tool learned to say nothing at all in 29% of reviews. The cautionary tale is the tool that hands you one real bug buried in 20 speculative guesses — and that description comes not from a critic but from Greptile CEO Daksh Gupta, in his own essay "There is an AI code review bubble" (February 2026) — Greptile being one of the vendors that ranks first on its own benchmark.
3. **Humans keep the final verdict, and the layer is cheap.** Cloudflare's home-built system runs 130,000+ reviews a month at an average $1.19 each. As a cheap *extra* layer stacked on top of human review, that's almost a guaranteed win — **as long as it stays an extra layer and doesn't quietly replace the human one**.

Flip all three conditions — core business logic with no tests underneath, AI writing and AI reviewing, humans just clicking approve — and you have the standard portrait of the nesting dolls.

One honest footnote: in two years of boom, this industry **has not run a single randomized controlled trial** showing AI code review works — and not one named company has published a postmortem titled "why we turned our AI reviewer off." Rigorous evidence is missing in both directions.

## What to do

**If you're deciding whether to adopt it for your team**: pick which repos go first by whether tests and type systems have your back, not by the vendor demo; in procurement, only accept catch-rate and false-alarm-rate as a pair — a one-sided number is a fail; during the pilot, sample the AI's comments yourself and count how many actually get acted on, then compare with the public numbers in this essay.

**If you're the engineer being buried in AI comments**: trusting everything and ignoring everything are both losing moves. The workable middle: triage by category — handle high-confidence classes (compile errors, clear API misuse) by default, bulk-downgrade the speculative classes (style opinions, "possible" concurrency issues), and spot-check the downgraded pile now and then. Two red lines: don't treat "tests pass" as proof of correctness, especially when the AI wrote the tests too; and don't let yourself become a reviewer who only reads AI summaries — the ability to read code with your own eyes is exactly the skill that holds its value in the AI era.

**If you're building these tools**: the first vendor to publish its false-alarm rate on its own benchmark page — with a note saying "this benchmark is run by a contestant" — will collect, for free, the trust the whole industry is currently bleeding.

## How to check whether this essay is right

The whole argument reduces to eight claims, ordered from hardest to softest evidence:

1. **The verification bottleneck is real and worsening** — AI-written code keeps growing while human review capacity doesn't.
2. **Vendor-run benchmarks don't count as evidence**: six vendors ran their own, six ranked first; the same tool's score varies 3.7× across benchmarks.
3. **Discount offline scores by an order of magnitude before believing production value** (Meta: 68% offline → 19.75% in production).
4. **AI output adds a new verification burden on reviewers** — Meta's experiment showed reviews slowing significantly, fixed only by hiding the AI's identity.
5. **The independence of "AI verifying AI" doesn't hold**: the stronger the models, the more alike their errors; a model grading its own homework collapses.
6. **"Humans will catch it" is not a reliable backstop** — forty years of human-factors research: automation complacency cannot be trained away.
7. **In narrow settings it genuinely works**: an independent test oracle, controlled false positives, humans holding the final call — remove any one and it slides toward turtles.
8. **The industry has never run a single randomized controlled trial, and there is no named failure post-mortem** — every conclusion here, including this essay's, should stay revisable.

Worth watching: which way the first RCT points; whether the share of PRs merged with zero review keeps climbing or gets governed back; whether an independent evaluation protocol emerges that vendors can't harvest.

## The things that matter most

1. **The verification bottleneck is real, but "buy another AI" is not automatically the answer.** Demand for checking code is exploding, while the AI checkers invent problems of their own and increasingly make the same mistakes as the AI writers.
2. **Always demand paired numbers.** A report card that says "catches X% of bugs" without a false-alarm rate was ruled invalid by science sixty years ago; "whoever runs the exam comes first" is this industry's current normal.
3. **Divide demo scores by ten before talking.** An order of magnitude separates offline benchmarks from production: Meta's own model scored 68% offline and 19.75% actually applied in production. When evaluating tools, only production adoption rates count — never the demo.
4. **"A human is still in the loop" is not a safety statement.** Forty years of human-factors research is blunt: automation complacency cannot be trained or reminded away. Measure real gatekeeping quality — like the share of PRs merged with zero review — instead of assuming people stay vigilant.
5. **The right role for AI review is "a cheap extra layer," not "the layer that replaces people."** With tests underneath, false alarms under control, and humans holding the final verdict, it's medicine. Remove any one of the three, and it starts sliding toward nesting dolls.
