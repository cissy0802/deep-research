# "95% of AI Pilots Fail"? The Number Can't Even Stand On Its Own Report (Plain-Language Edition)

> This is the condensed edition of the deep dive of the same name. Every key number has been independently verified; for the full arguments and sources, read the deep dive.

## The sentence that spooked the market

On August 18, 2025, Fortune ran a story: "MIT report: 95% of generative AI pilots at companies are failing." The next day AI stocks pulled back — Nvidia down 3.5%, Palantir down nearly 9%. From that week on, "95% of AI pilots fail" became the most-quoted number in the industry: in boardrooms, in analyst notes, and in the mouth of every salesperson with an AI solution to sell.

This essay went and read the original report word by word, then traced every stop in the number's year of circulation. The verdict up front: **the number can't even stand on its own report — but behind it sits a real question worth answering properly.**

## What the report actually says

The report is *The GenAI Divide*, from MIT's Project NANDA group — 26 pages, version v0.1, self-labeled "Preliminary Findings." Taken apart, four things never make the headlines:

**First, the "95%" is three mismatched statements in one report.** The opening says "95% of organizations are getting zero return." The only 5% with an actual data chart refers to a funnel for custom enterprise AI tools: 60% of organizations looked into them, 20% piloted, 5% reached production. "Didn't reach production" and "zero return" are different things: a company whose custom tool died may be saving real money with ChatGPT — which is exactly what the report itself measured (see the fourth point). Also: 80% of organizations in that funnel never piloted at all, so most of the "pilots" in "95% of pilots fail" never happened; among companies that actually piloted, the success rate is one in four.

**Second, "success" is defined as "someone said nice things."** Verbatim from the report: success means users or executives "have remarked" that the tool caused a marked and sustained productivity or P&L impact. Not financial data — whether someone said so in an interview. The appendix carries a second, different definition (measurable KPIs within six months); the two don't match. The report itself concedes the figures are only "directionally accurate" and that the six-month window may understate success.

**Third, the sample is startlingly small.** Interviews with 52 organizations, plus 153 questionnaires collected on the floor of four industry conferences. That's it. And the report's "Reviewers" line lists its own fourth author — reviewing himself.

**Fourth, the report contains data pointing the opposite way, which nobody quotes.** At 90% of the companies surveyed, workers were using personal AI tools for work — "almost every single person used an LLM," in the report's words — and that shadow use "often delivers better ROI than formal initiatives." General-purpose chatbots showed a pilot-to-implementation rate around 83% — a success story. The same report supports "AI is failing everywhere" or "AI is everywhere," depending on which sentence you clip.

## The number mutated on its way out the door

Rumors usually take several hops to distort. This one didn't need them — **the first story changed it**. The report said "95% of organizations getting zero return"; Fortune's headline said "95% of pilots are failing." The report's sample was 52 interviews + 153 questionnaires; Fortune printed "150 interviews and a survey of 350 employees" — numbers that don't exist in the public report, copied by dozens of outlets, and never corrected by any of them a year later.

After that, the standard script: qualifiers shed one by one, until "95% of generative AI pilots (with no measurable P&L impact within six months)" became "95% of AI projects fail"; the pedigree climbed too, from "a NANDA project team's preliminary findings" to "an MIT report" to "MIT Media Lab research." By 2026 the content farms had even bred a sourceless hybrid: "90% of enterprise AI implementations fail."

## What the authors sell

Project NANDA builds AI-agent infrastructure. The report's diagnosis: pilots fail because the tools can't learn; the cure is agentic AI with memory and adaptation — which is what NANDA is building. The report's own text twice lists its protocol as the solution infrastructure, and the conclusion advises companies to "start partnering with vendors." The 80,000 Hours post-mortem put it plainly: all four authors are developing or selling the class of frameworks the report recommends, under the MIT brand, with no conflict-of-interest disclosure.

The critics were many and on the record: Wharton professor Kevin Werbach publicly demanded NANDA "release the full supporting data. If not, it should retract the report." A year on, the response: zero. No data, no correction, no sequel — and the MIT Media Lab group's own publications page doesn't list the report.

One more mirror: that same year, MIT had another viral study pointing the opposite way — "AI accelerates materials discovery," endorsed by top economists, cited in Congress — until MIT itself declared it had "no confidence" in the data and asked for it to be withdrawn (critics allege fabrication). The year's two most viral "MIT numbers," one bearish and one bullish, both failed the physical. **An institution's brand guarantees nothing about method — good news needs an autopsy exactly as much as bad news.**

## How "90% succeed" and "90% fail" share the front page

Between 2024 and 2026 you could read all of these at once: a Microsoft-commissioned study saying every $1 returns $3.7, with only 1% of respondents reporting no ROI; PwC surveying 4,454 CEOs and finding 56% got neither revenue nor cost gains from AI in the past year; Wharton finding nearly three-quarters of executives "see positive ROI"; McKinsey finding only ~6% of firms can attribute a meaningful profit impact to AI.

Nobody is lying. They're using **different rulers** — and each notch of strictness drops the "success rate" a tier:

- Ask "what would you estimate your ROI multiple is" (multiple choice, "not sure" excluded) → 99% have ROI;
- Ask only companies that already deployed AI whether ROI arrived within a year → 74%;
- Ask executives whether they *feel* ROI is positive → 74% (81% of VPs and above say yes; only 69% of middle managers — **whoever answers owns the answer**);
- Ask CEOs whether AI projects met their own expectations → 25%;
- Count actual, measured revenue gains plus cost cuts over 12 months → 12%;
- Require attributing a ≥5% profit impact to AI, plus self-assessed significant value → about 6%;
- Require "value at scale" → 5%.

See it now: **NANDA's 5% is not lonely at the strict end** — McKinsey's 6%, BCG's 5%, and PwC's 12% sit in the same band. Its sin wasn't direction. It was reporting a single-digit-precision number from 52 interviews, swapping "no marked P&L impact" for "zero return," and letting the media inflate that into "AI is failing."

And keep one pattern in mind: vendors selling AI produce warm numbers; consultancies selling AI transformation produce "only a few succeed — you need help" numbers. BCG's own methods note admits that unless marked "realized," its figures are respondents' **expectations**, subject to "perception bias."

## What the government data says: fast, shallow, and hidden

Step outside the vendor and consultant surveys, and the official statistics tell a three-word story.

**Fast.** Generative AI reached roughly 53% adult adoption in three years — faster than the PC or the internet at the same age.

**Shallow.** Among US firms that adopted AI, 57% use it in three or fewer functions; the European Central Bank says about seven in ten euro-area firms "use AI," but only about 7% use it intensely enough to drive transformation. The money tells the same story: corporate-card data shows over half of firms now pay for AI, but the **median** firm spends $11.38 per employee per month — a bit more than a coffee. On outcomes, the hardest evidence comes from Denmark: researchers combed the entire national payroll registry (25,000 of the most AI-exposed workers) and found AI chatbots' effect on wages and hours was a **precise zero** (ruling out anything above 2%). Users themselves report saving about 3% of their time — while controlled experiments on the same kinds of tasks (the method medicine uses to test new drugs) measure gains an order of magnitude larger. At the macro level, even Goldman Sachs admits it finds no meaningful relationship between productivity and AI adoption across the economy — despite its own 2023 forecast that AI could lift global GDP by 7%.

**Hidden.** At one point in time, three official numbers disagree: ask firms, 18% use AI; ask workers, 41%; weight by employment, 78% of the workforce sits in adopting firms. Why the spread? One big reason: employees use personal accounts, and the boss can't see it. A 47-country survey of 48,000 people found **57% of employees hide their AI use from their employer and present AI output as their own work**. So "95% of pilots fail" and "everyone is using AI" don't contradict each other: what fails is the formally chartered project; what thrives is the shadow use no statistic captures.

## It happens every time

A high failure rate plus an authoritative byline is a thirty-year-old recipe, one per generation:

- "Only 16% of software projects succeed" (Standish, 1994) — the same company's data can swing from 5.8% to 94.2% "success" under a different counting rule. We [took that apart last time](https://cissy0802.github.io/deep-research/seventy-percent-failure-plain.en.html).
- "85% of big-data projects fail" (2017) — the entire source is **one personal tweet by a Gartner analyst, since deleted**. It was cited as "Gartner research" for nearly a decade.
- "85% of AI projects fail" (2018) — Gartner's actual sentence was that 85% of AI projects would "deliver erroneous outcomes due to bias" (nearly a truism); circulation turned it into a failure rate.
- "Three-fourths of IoT projects are failing" (Cisco, 2017) — Cisco's own data showed about two-thirds of completed projects were considered successes; the 74% was manufactured by counting every company that didn't self-rate "complete success" as failing.
- And the best one: Harvard Business School studied 2,000+ venture-backed startups, and the Wall Street Journal's 2012 rendering was — **"If failure is defined as failing to see the projected return on investment… then more than 95% of start-ups fail."** The same companies fail at 30–40% by the liquidation yardstick. The 95% had an exact twin before AI existed, made with the same recipe: set the pass bar at perfection, and the failure rate is whatever you need.

New drugs make it from first human trials to approval about one time in ten, and nobody says "pharma doesn't work" — a high failure rate is **the shape of a funnel**, the normal form of every field that runs experiments. The thing to remember: **these failure-rate numbers almost never measure what they claim to measure.** And debunking doesn't help — one study counted papers citing the debunking literature and found them re-affirming the myth versus rejecting it at 12 to 1.

## Four theories, four readings

Economics offers four frameworks for "95% of pilots show no return," and their prescriptions conflict:

1. **The productivity J-curve**: a big technology's early investments (redesigning processes, building data, training people) all book as cost, not output, so "no measurable return" is what the transformation phase is supposed to look like — the bigger the technology, the deeper the dip. Ride it out. The theory's author declared in early 2026 that the US is "transitioning into a harvest phase"; the same week, another chief economist wrote "AI is everywhere except in the incoming macroeconomic data." Unresolved.
2. **Absorptive capacity**: a company's ability to digest new technology is a byproduct of doing the work itself — **it can't be bought**; firms that lack it don't fail by bad luck, and some never make it through. The sting: NANDA's report also says the problem is "learning" — but it means the **tools** should learn (so buy our agent framework), while this school means the **organization** must learn (so don't expect a purchase to fix it). One word, two opposite shopping lists.
3. **Acemoglu's ceiling**: maybe AI's near-term profit potential is simply small — his upper bound is under 0.66% of productivity over ten years. On this reading the 95% is not an artifact; it is **a small effect, measured correctly**, and ten years of waiting won't produce a rebound.
4. **The electrification precedent**: in 1900 you could honestly say "the dynamos are everywhere but in the productivity statistics" — electrification took forty years, until factories were redesigned and a new generation of engineers grew up. The gains never came from cheaper power; they came from rebuilt workflows — and today only about 21% of organizations have redesigned theirs.

Three facts hold at once: task-level gains are real (replicated in experiments), enterprise-level profit attribution is mostly absent (5–12% on strict rulers), and the macro signal hasn't arrived. The four theories are bets on whether transmission across those layers happens.

## How to check this essay's judgments

From hardest to softest evidence:

1. **"95% of organizations getting zero return" has no data support in the report** — the only traceable 5% is the custom-tool funnel, and "didn't reach production" ≠ "zero return." The PDF can be checked word by word.
2. **The sample is 52 interviews + 153 questionnaires; Fortune printed 150 + 350, numbers absent from the public report and never corrected.**
3. **"Success" means someone praised the tool in an interview, and the report itself calls its figures only "directionally accurate."**
4. **The authors sell the cure the report prescribes** (agentic AI frameworks), with no conflict disclosure; a year after being publicly asked to release the data or retract, the response is zero.
5. **Strict-yardstick independent measurements converge on 5–12%** (McKinsey ~6%, BCG 5%, PwC 12%) — NANDA's 5% isn't lonely in direction; what's lonely is its wording and its sample.
6. **Perception yardsticks run warm (~74% report positive ROI), and warmer with seniority** (VP+ 81% vs middle managers 69%).
7. **Official statistics: fastest adoption on record, mostly shallow use** (57% of adopting firms confine it to ≤3 functions; the median firm spends $11.38 per employee per month).
8. **Denmark's national payroll data: AI's effect on wages and hours is a precise zero** (ruling out >2%); no AI signal in macro productivity — even Goldman says so.
9. **57% of employees hide their AI use** — firm-level statistics are structurally undercounted; the failure narrative and the boom can both be true.
10. **The 95% has an exact twin**: by the "failed to meet projected ROI" yardstick, more than 95% of venture-backed startups "fail" — high pilot mortality is the normal shape of experimental portfolios, not an AI disease.
11. **Historical failure rates almost never measure what they claim**: the 85% was a deleted tweet; the other 85% a mutated bias prediction; the 74% counted "not a complete success" as failure.
12. **The four theories give opposite answers to "will the 95% fix itself"** — the most watch-worthy question of the next five years, and no peer-reviewed study has yet tested the number itself.

**What to watch**: whether NANDA ever releases its data (the only route to re-measuring the 95%); whether the 2026–27 US productivity revisions show an AI-attributable acceleration (the verdict point for the J-curve dispute); whether Gartner revises again after moving "at least 30% will be abandoned" to "over 50% were"; and the next viral failure-rate number — on this recipe's schedule, it's already on its way.

## The few things that matter most

1. **Next time you see "X% of AI projects fail," ask three questions: What's the denominator? How is "failure" defined? What does the person telling you this sell?** Those three questions dismantled the 70%, the 85%, and now the 95%.
2. **A success rate is a function of the ruler, not just the facts.** Self-estimates give 99% success; strict attribution gives 6%. Between them lies not a lie but six adjustable dials. Quote any number with its ruler attached.
3. **Keep two ledgers for your own AI projects**: one for "did it reach production" (the funnel ledger), one for "did it make or save money" (the profit ledger). NANDA's core error was collapsing the two into one.
4. **Mass pilot death is the normal form of an experimental portfolio.** Don't take it as a reason to panic, or to buy someone's cure — nine in ten drug candidates die and pharma still profits, by managing the funnel rather than abolishing failure.
5. **Your employees are almost certainly already using AI, and half of them are hiding it.** Before chartering another formal pilot, make the hidden users safe to come forward and compliant — the ROI buried in shadow use may beat your official projects, which is the most solid and least-quoted finding in that whole report.

*For the full arguments, every source, and the counter-evidence, read the deep dive.*
