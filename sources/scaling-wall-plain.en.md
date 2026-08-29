# "Has AI Hit a Wall?" — Two Years of Arguing, and Neither Side Produced a Measurement (Plain-Language Edition)

> The load-bearing claims here went through 44 groups × 3 adversarial votes, with verifiers instructed to *refute*. One of this article's own planned conclusions was killed and replaced — see the note at the end. All figures as of August 2026.

## First, a question: what does "the wall" mean?

Since November 2024, "AI has hit a wall" has been the hottest argument in this industry. Two years on, both sides are exactly where they started.

The first thing worth saying is that this argument never produced a testable definition of "the wall." And once you try to supply one, you find that nothing either side offers is aimed at it.

Start by clearing away the biggest misunderstanding.

"Double the input, get less back" is not a discovery from 2024. It is what the scaling-law formula means. The founding 2020 paper spelled it out in plain arithmetic: **double the parameters, and loss falls by 5%.**

So anyone saying in 2024 that "the returns to scaling are diminishing," if that is what they mean, is reporting arithmetic that has been printed in a paper for five years — not a new observation.

If "the wall" is going to be a claim that can be confirmed or refuted, only two possibilities remain:

**One: the law has failed** — inputs keep going in, but results no longer land where the formula predicts.

**Two: the law still works, but nobody can afford it** — each additional increment costs more electricity and money than anyone is willing to pay.

These require entirely different evidence. And the conclusion here is: **the first has neither evidence nor any way to be checked; the second is arriving, but what is jamming it is electricity and concrete, not shrinking returns.**

## The first wall: no evidence, and no way to look

The finding first: **as of August 2026, no public study can be found showing that frontier models' measured results have departed from the line the formula predicts.**

This was searched for deliberately — from several angles, including every 2025–2026 paper claiming problems with scaling laws. The one relevant new study points the other way: it finds that with well-tuned settings, curves at different scales line up *more* neatly, not less.

But the second layer matters more than the absence: **this cannot be checked at all.**

Three reasons, each fatal on its own.

First, how many parameters frontier models have and how much data they used are not published. The GPT-4 technical report set this norm, stating that given the competitive landscape and safety implications, it contains no further details about architecture (including model size), hardware, training compute, dataset construction, or training method. It became industry practice.

Second, the core metric you would need for comparison is published even less. And that metric is not directly comparable across different corpora or different ways of splitting text — two models' reported numbers, if not measured under identical conditions, cannot meaningfully be subtracted.

Third, the affirmative evidence — that the formula still works — is entirely vendor self-reported, and reported on private metrics. OpenAI says it accurately predicted GPT-4's performance from models using 10,000× less compute, but that metric was measured on "our internal codebase," and the accompanying chart has no scale at all. Meta's claim about Llama 3 is likewise its own account.

So the first wall sits here: **those saying there is a wall cannot produce a measurement, and those saying there isn't produce their own charts without scales. This is not insufficient evidence; this is evidence withheld.**

To be clear, this does not mean the wall is absent. It means that under current disclosure habits, the question cannot be publicly answered. Anyone asserting either direction is speaking past their evidence.

## What each side actually produced in those two weeks

If measurement is closed off, what are they citing? Taking the origins of the wall thesis back to the originals is worth recording.

**Origin one: two reports from anonymous sources.** On 9 November 2024, The Information cited OpenAI employees who had tested a new model codenamed Orion: it **did outperform its predecessors**, but by far less than the jump from GPT-3 to GPT-4. That first concession routinely disappears in retelling, and without it the passage reads as "no progress." Four days later Bloomberg reported three companies struggling at once.

One point gets missed: **Bloomberg's core argument is about arithmetic, not impossibility** — it wrote that even modest improvements might not justify the enormous costs. That is the second kind of wall, not the first.

**Origin two: a sentence written by a reporter.** The most-cited "wall evidence" in this whole argument is Ilya Sutskever saying pretraining results had "plateaued."

Checked word by word against the Reuters original: **he did not say it.** The sentence carries no quotation marks; it is the reporter's paraphrase, and "plateaued" is the reporter's word.

In that same piece, only two sentences are actually in quotation marks. One: "The 2010s were the age of scaling, now we're back in the age of wonder and discovery once again." The other — note the direction — "**Scaling the right thing matters more now than ever.**"

That second one is pro-scaling. He is saying the *target* of scaling should change, not that scaling has stopped working.

He had also left OpenAI to found a new company, was raising money for a route that does not rely on pretraining, and declined in that same piece to say what he was working on.

**Origin three: a four-word tweet.** The rebuttal came fast and was equally thin. In mid-November 2024, Sam Altman posted four words: "there is no wall." No link, no target, no argument. He posted six weeks after OpenAI closed a $6.6 billion round at a $157 billion valuation.

Eleven and a half hours later, Google DeepMind's Oriol Vinyals posted "What wall?" — but not as a reply to Altman; it was attached to his own model topping a leaderboard that day.

**So the two origins of this argument are anonymous internal testing on one side and three or four words from interested parties on the other. Neither produced a measurement.**

Two claims that have circulated for two years, cleared up in passing:

"Orion is only 20% better than GPT-4" — **that sentence is not in the original reporting.** The retrievable version is that Orion reached GPT-4's level about 20% of the way through training. That is training progress, not improvement, and it was originally used to argue that gains arrive early and the rest won't catch up — the opposite direction.

"The age of giant models is over" — not Altman's words, and not from 2024. The primary source is an April 2023 remark at MIT, and the circulating phrase is a magazine headline. The date is off by a year and a half.

## Four different walls, stuffed into one word

Lay out what each party means by "the wall" and they are not the same thing — several are mutually contradictory.

**Wall one: data.** This is Ilya's. In December 2024 he said at an award talk that "pre-training as we know it will unquestionably end," but the reason has to come along: compute keeps growing through better hardware, better algorithms and larger clusters, while data does not, "because we have but one internet." He called data the fossil fuel of AI, already at peak.

His slide made it unmistakable: compute growing in the left column, data not growing in the right. **He is saying one ingredient has run out, not that the recipe's math is wrong** — he says on that same slide that compute is still growing. In the same talk he named three ways forward: agents, synthetic data, and inference-time compute.

Citing that talk as proof that "scaling laws failed" reads *out of fuel* as *engine broken*.

**Wall two: architecture.** This is Yann LeCun's — that large language models cannot reach human-level intelligence at all, which is also the founding pitch of his new company. He rejects the route, not the scale — and **this wall is incompatible with Ilya's**: if the route is wrong to begin with, data sufficiency is not the question.

**Wall three: diminishing effect.** This is the wall in those two reports. It is the closest to the first kind above, but what supports it is anonymous internal assessment, not a curve.

**Wall four: slowing compute growth.** This one is misattributed most often, because it comes from a research group that explicitly does not endorse the wall thesis. Epoch AI does forecast a slowdown in compute expansion — but the mechanism is **that things cannot be built fast enough**: renting GPUs takes almost no time, buying them about half a year, building a data center one to two years, a very large data center or power plant two to three, and a cutting-edge chip fab from scratch four to five. Their conclusion: every additional 10× in compute scale adds roughly a year of lead time.

Nowhere does that report say the same compute buys less capability. **Using it to support "diminishing returns" reads it exactly backwards.**

Once four walls go into one word, the argument cannot produce a result: each side is answering something the other never said.

## Did capability actually rise these two years?

Yes. But read the curve carefully, because nearly every point is vendor-reported.

Take the coding benchmark the industry cites most, SWE-bench: the frontier sat around 49% in late 2024, reached 62% in February 2025, 75% in August, 81% in November (in a configuration with no extended thinking, averaged over five runs), and by 2026 vendors report 96%.

Three problems must be stated:

First, that "49% line" is a coincidence of different vendors' numbers plotted on one chart, not a measurement under one apparatus. **The same model with a different set of surrounding tools can score 22 percentage points apart** — that is from OpenAI's own system card.

Second, "first past 80%" does not hold: Anthropic reported 80.2% half a year earlier, just with a more compute-hungry configuration.

Third, and most importantly: **independent replication comes in systematically lower.** Epoch AI, using a uniform toolchain on the same problems, measures an all-time high of 83.5% where vendors report 96%. Not one point on that curve has been independently reproduced at the level claimed.

**Even problem sets built specifically to resist saturation are being solved fast.** ARC-AGI-2, released in March 2025, had pure language models at zero and the strongest reasoning systems in single digits. By August 2026 the leader is at 92.5% — humans are at 100%. Seventeen months, from single digits to ninety percent.

But the same organization released a new generation in March 2026, whose launch-day verdict was: "Humans score 100%. Frontier AI scores 0.51%." Everything knocked back to near zero. That did not hold either — by August one model reached 30%.

**Here is a piece of counter-evidence sharper than "the wall."** Another problem set, billed as humanity's last exam, came with a paper predicting models might exceed 50% by the end of 2025. As of August 2026, the best no-tools score is still 46.44 — **crossing 50 is running more than half a year behind the question-setters' own expectation.** This is the hardest "behind schedule" evidence here, and it comes from the optimistic side's own forecast.

**The one ruler not held by vendors** is METR's "time horizon": how long a task takes a human, where the AI can finish it half the time. Its measured progress is exponential, doubling roughly every seven months. After a revised version in January 2026, the doubling time since 2023 fell from 165 days to 131, which METR describes as progress being 20% faster than previously estimated.

But that "20% faster" applies only to the stretch after 2023. **Across the full dataset, the old and new versions give exactly the same doubling time: 196 days.**

## The rulers themselves are breaking

Every curve above rests on benchmarks. And over these two years, benchmarks have lost reliability as instruments faster than capability has risen.

**The same name can be two different things.** In December 2024, ARC Prize reported that o3 scored 75.7% on its problem set, and 87.5% with roughly 172× the compute. OpenAI simultaneously disclosed that the o3 tested had been trained on 75% of that benchmark's public training set.

In April 2025, the same organization retested the released o3: 41% to 53%. OpenAI confirmed that **the shipping version is not the same model as the one tested**, and that the compute tier used back then is not available in the product.

The 87.5% from the launch and the 41% you can buy are not the same thing.

**Cost figures can be revised three times, and reverse direction.** For that evaluation, the high-compute tier had no cost listed at all on launch day, marked "pricing TBD." In spring 2025 ARC recalculated under one price list, and the high-compute tier was at one point estimated at roughly $34,400 per task (a figure from ARC Prize's Mike Knoop, via media retelling). A December 2025 recalculation under another brought it down to $4,560. So the circulating claim that "$4,560 was revised up to $30,000" **has the order backwards** — $4,560 is the result of the final downward revision.

**The funder can own the questions.** For one hard mathematics benchmark, its maintainer acknowledged in January 2025 that the core 300 problems were commissioned and funded by OpenAI, that OpenAI owns them and can see both problems and solutions (a holdout set excepted) — and that as of the statement, **the holdout set was still being finalized.** Which means that when OpenAI announced weeks earlier that its model scored over 25% on this set, the portion whose answers it could not see did not yet exist. As for "not used for training," that was a verbal agreement.

An independent retest of the released model later gave about 10%. But that is not a clean contradiction: it was not the same model, nor the same problem set, and the 10% was later revised up to 18.7%.

**The real lesson is not "the vendor lied," but this: when the funder owns the questions, the evaluator's caliber shifts, and how you ask determines the score, a single benchmark number carries almost no independent arbitrating power.**

**Benchmarks have a lifespan.** A 2026 systematic study of 60 benchmarks found nearly half saturated to the point of no longer separating models. And the intuition it falsified is more interesting: **hiding the questions does not help** — private test sets are not more resistant to saturation than public ones.

**A final signal comes from the vendors.** By 2026, Anthropic's two flagship launches no longer lead with that coding benchmark at all, using others instead; and it discloses that its internal memorization screens flag a subset of that benchmark's problems. **When the party being examined starts changing its own exam, that 49%-to-96% curve needs reading with more care.**

## The data wall: bought off all the way, and pushed back

Ilya's wall is the most concrete of the four and the only one with quantitative research behind it. Its current state: **not hit, not gone — deferred by a series of measures, each with its own limits.**

**How much stock is left?** A widely cited study predicted in 2022 that high-quality language data would likely run out before 2026; its 2024 revision changed this to: on current trends, models will train on datasets comparable to the total stock of public human text **between 2026 and 2032.**

The companion estimate puts the magnitude at about 300 trillion tokens — but the original range must come along: **100 trillion to 1,000 trillion, a full order of magnitude.**

One clarification: "running out" here means **training consumption catching up with the stock**, not data being physically used up.

**First measure: reuse it.** One study measured that with compute held fixed, repeating the same data up to 4 times costs almost nothing in quality versus fresh data. But the second half of that sentence matters as much: **repeat beyond that, and the value of adding compute eventually decays to zero.** This is one of only two claims in this piece that survived all three votes unchanged.

**Second measure: have models make the data.** This is where the traps cluster.

Microsoft's phi-4 used 40% synthetic data and did beat the stronger model that generated its data on two tests. But look right along the same table: on a test of factual recall, phi-4 scores 3.0 against its teacher's 39.4, and it trails on four others too. **Two wins out of seven — and the worst loss is factual recall, which is exactly what real text buys.**

That much-quoted "98% synthetic data" is precisely limited in the original: **the 98% refers to the alignment stage, not pretraining.** Completely different denominators.

And how much synthetic data frontier closed models use **cannot be known from outside**.

One common explanation needs correcting: people say every synthetic-data success is distillation from a stronger teacher and therefore cannot be extrapolated. That reasoning fails — NVIDIA's paper states that the teacher does not impose a ceiling on the student, and its first-round data generator was weaker than the model being trained. **What blocks extrapolation is the layer and the unmeasurability, not teacher strength**: the verifiable successes happen either at the alignment stage or on small models.

**What about models degrading from eating their own output?** The famous Nature paper's much-quoted hedged sentence — that indiscriminate training "can lead to" collapse — is in fact **the journal editor's standfirst, not the paper's abstract.** The authors' own abstract does not hedge at all, using "causes" and "irreversible."

But the experiment behind that strong claim is small: recursive fine-tuning of a 125-million-parameter model on a small corpus, with a control that preserves no original data in later generations. And another setting in the same paper supplies the antidote: resample 10% of the original real data into every generation, and you get only minor degradation. The real data never leaves, which is why it works.

Another group offers the direct rebuttal: **it is *replacing* real data that causes collapse; *accumulating* does not** — and the real internet is closer to accumulation.

**As of August 2026, there is no confirmed public report of model collapse observed in real production training.** It remains a laboratory phenomenon, not an incident that has happened. (To be precise: this is absence of evidence — vendors have no obligation to disclose, and failed internal runs are not published.)

**Has the wall ever bitten a specific training run?** The one public case is the Wall Street Journal's December 2024 report on Orion. Citing it carries three traps:

First, "$500 million each" is wrong — the report states a general rule, that a six-month run could cost around half a billion in compute alone, not that Orion's two runs each did.

Second, the most-quoted line — that there may not be enough data in the world to make it smart enough — is **the paper's own subheadline**, a reporter's framing; OpenAI never confirmed it.

Third, the fatal one: the model in that report shipped in February 2025 as **GPT-4.5**, and the GPT-5 released in August 2025 is a different thing entirely. **What that report supports is that GPT-4.5's pure scale-up route hit a wall — not that GPT-5 did.**

**One counterintuitive note: published training-data sizes are not a line you can extrapolate.** The numbers are right — 15 trillion, 36 trillion, 40 trillion, rising. But the rulers differ (some text-only, some including images and video), and part of that "growth" is data the models manufactured themselves. The clearest evidence is within one generation: **Llama 4's Maverick beats Scout while using 22 trillion against Scout's 40 trillion, nearly half as much.**

## Changing axes is not the same as running out of axes

After September 2024, "scaling" started meaning two things, and each camp often means only one.

OpenAI's original wording about o1 was that performance keeps improving with more reinforcement learning and more thinking time — and then, in a clause usually dropped, **"the constraints on scaling this approach differ substantially from those of LLM pretraining, and we are continuing to investigate them."** The vendor is conceding that the new paradigm's limits are not yet understood.

The two famous curves accompanying it have only "compute (log scale)" on the x-axis, **with no numerical labels at all**. It is a schematic; no multiple and no absolute magnitude can be read from it.

The AIME math scores in that same post come at three levels: 74% answering once, 83% voting across 64 attempts, 93% sampling 1,000 times and picking one. "o1 scored 93" without the sampling method presents many attempts as one attempt's ability.

**The new axis may not have the old one's shape.** A Meta study using over 400,000 GPU-hours states plainly that unlike pretraining, which typically fits power laws, they model reinforcement learning's compute-performance relationship with an **S-shaped curve** — and an S-curve means **there is a ceiling.** Note that its validation ran on an 8-billion-parameter model, far below frontier scale.

**Does reinforcement learning draw out existing ability or create new ability? Unsettled.** One side probes the boundary with heavy sampling and finds base models catching up when sampled enough, concluding that current training does not elicit fundamentally new reasoning patterns; the other side (NVIDIA) counters with results from much longer training.

But that counter is not clean: NVIDIA's own paper states that on tasks the base model already handles well, reinforcement learning delivers minimal or even negative gains; and **its starting point is not a raw base model but one already distilled from a reasoning model** — and distillation is precisely the path the other side concedes can introduce new patterns. The two papers are not in direct collision.

**Inference is getting cheaper and more expensive at once.** The price of reaching a given level falls somewhere between 9× and 900× per year (on data through February 2025, with the fastest declines concentrated in the year before that). In the other direction, reasoning models generate large volumes of thinking you never see, and it bills the same.

The price itself is worth a note: OpenAI's official changelog records that on 10 June 2025, alongside the release of o3-pro, o3's price was reduced. But three claims usually cited with it — the "80%" magnitude, the line "same exact model, just cheaper," and "an independent retest confirmed performance unchanged" — could not be traced to primary sources in this check, so this article does not draw conclusions from them.

## What is actually jamming is on the supply side

If the first wall cannot be detected, where does the second — the unaffordable one — stand?

It is approaching. But **what is jamming is electricity, concrete and delivery schedules, not returns.**

Epoch AI's 2024 report ranked four constraints and concluded that by 2030, advancing models by a large margin — comparable to GPT-4's margin over GPT-2 — is **likely achievable**. And the obstacles, in order: **power > chip manufacturing capacity > data > latency. Data is third.**

(One easily miscited point: that report's data estimate **excludes synthetic data entirely**, listing it separately as upside.)

This constraint has a much-quoted piece of testimony from an interested party: Microsoft's CEO said in November 2025 that the biggest issue now is not a compute glut but power — "you may actually have a bunch of chips sitting in inventory that I can't plug in." Not a chip shortage, but a shortage of rooms with power. (This quotation did not go through this run's verification process; it comes from a podcast via media retelling, so it is used here only as a side observation.)

A few numbers worth keeping:

- Frontier training compute has grown about 5× per year over the past decade-plus, but counting only recent frontier models since 2018 it is **4.2× per year**, below the headline figure — and that dataset stops in May 2024.
- The cost of the largest single training run grows about 2.4× per year, from roughly $200,000 in 2016 to about $490 million in 2025. Note the caliber: **amortized hardware plus electricity**, not the full cost of building the cluster, which can differ by an order of magnitude.
- Algorithmic efficiency is also improving: the compute needed for a given result halves roughly every 8 months. But that data stops in 2023 — **the entire reasoning-model era is outside it.**
- A counterexample: Epoch estimates GPT-5's total training compute came in **below** GPT-4.5's, the first time in the GPT line that a successor used less. Epoch's attribution is not a wall: they argue OpenAI bet its resources on scaling post-training, while the new techniques were not yet mature enough to apply at GPT-4.5's scale. They predict the next generation will rise again, but the same piece discounts itself — the return to growth "might not last long" — and names the availability of high-quality pretraining data as a potentially harder bottleneck. (In passing: the summary "a pause, not a halt" that circulates from this comes from a technology newsletter, not from Epoch.)

**And demand shows no retreat.** Epoch's May 2026 estimate: at current prices, token demand grows roughly 10× per year while global inference capacity grows about 3.4×, with long-context and agentic workloads hitting the shortfall first. (This estimate likewise did not go through this run's verification process, and the demand figure is itself stitched together from proxy indicators.)

Worth seeing clearly in passing: the widely circulated short thesis rests on depreciation accounting and circular financing, **not on models hitting a capability wall.** The two get bundled together but require entirely different evidence.

## The things that matter most

**This question currently cannot be answered, and not because the evidence hasn't arrived.** Frontier models' parameter counts, data volumes and comparable core metrics are all unpublished. Those claiming a wall cannot produce a measurement; those denying it produce their own unlabelled charts. Anyone asserting either direction is speaking past their evidence.

**The most widely circulated evidence has mostly shed its qualifiers in transit, always in the same direction — the one that makes the claim stronger.** Kaplan's "some," Ilya's reporter-written sentence, o3's "internal, aggressive configuration," the "98% synthetic" that turns out to be the alignment stage, the Nature hedge that turns out to be an editor's line — every correction restores a weaker fact from a stronger assertion. This is not one side's failing; both do it.

**Four different walls got stuffed into one word, which is why it cannot be settled.** Data, architecture, diminishing effect, delivery schedules — each side is answering something the other never said.

**Capability is still rising, but the constraint genuinely closing in has moved from the returns side to the supply side.** Power first, chips second, data third.

**When you meet any "AI has/hasn't hit a wall" number, ask four things:** Is this vendor-reported or independently measured? Which surrounding toolchain produced it? Is the model in that launch demo the same one I can buy? And has this number been revised since?

## How to check the judgments in this article

Ordered from most to least confident:

1. **As of August 2026, no public study shows frontier models' measured results departing from the predicted line.** How to refute: either side producing parameter counts, data volumes and the core metric under one consistent caliber.
2. **Diminishing returns are a property of the formula, not a 2024 discovery.** Double the parameters, gain 5% — written into the 2020 paper.
3. **Ilya's "pretraining has plateaued" was written by a reporter, not by him**; one of his actual quoted sentences supports continued scaling.
4. **Ilya's wall is data, not compute, and not the formula failing.** He says on the same slide that compute is still growing.
5. **The compute slowdown Epoch forecasts is about data centers and power plants not being buildable fast enough, not about shrinking returns.** Their constraint order: power, chips, data, latency.
6. **The same model with a different toolchain can score 22 percentage points apart on the coding benchmark** (OpenAI's own data). So one-to-three-point gaps on leaderboards mean nothing.
7. **Launch-demo scores and shipping products can differ by more than 30 percentage points.** The o3 demo scored 87.5% on one problem set; the released version 41% to 53% — and OpenAI confirmed they are not the same model.
8. **Repeating the same data up to 4 times costs almost nothing; beyond that, added compute's value eventually decays to zero.** (Note: what is undamaged is the training metric, not downstream capability.)
9. **"Running out of data" means consumption catching up with stock, not data being physically exhausted**; the window is 2026 to 2032, and the stock estimate itself spans an order of magnitude.
10. **As of August 2026, no confirmed public report exists of model collapse observed in real production training.** (Absence of evidence — vendors need not disclose.)
11. **Capability measurement and pretraining returns are two ledgers, and existing independent indices only measure the first.** They bake reasoning, reinforcement learning and post-training together, with no pretraining dimension to separate out.
12. **Published training-data sizes are not an extrapolable upward line.** Within one generation, Llama 4's Maverick beats Scout on 22 trillion against 40 trillion.
13. **The prediction that reasoning-training's fast growth is a one-time dividend cannot be settled.** Its basis is a screenshot of an unlabelled livestream chart, and frontier labs have disclosed no comparable figures since.

**What to watch.** Three things would change the judgments here:

First, **any lab publishing parameter counts, data volumes and the core metric under one caliber** — that would make the first wall checkable for the first time, and it is also the least likely to happen.

Second, **a bend in the slope of METR's ruler.** It is the only one not held by vendors whose scale has physical meaning; if it bends, that is a real signal rather than another benchmark saturating.

Third, **power loosening or locking up.** Since the binding constraint has moved to electricity, what sets the pace over the next two years is grid connections and data-center delivery, not papers.

## A note on where this article was itself overturned

Adversarial verification killed one of this article's planned conclusions, along with several statements. The important one:

**The plan was to write that Ilya, having proclaimed the age of scaling over, turned around and took $5 billion from NVIDIA to increase his compute tenfold.** Two votes judged this a false contradiction manufactured by deleting qualifiers — his own definition of the next phase is "it's back to the age of research again, just with big computers," what he rejects is that scaling the current recipe 100× would transform everything, and he explicitly grants that scaling up "would be different, for sure."

**The critique that does hold is different and more interesting: scale drift.** In that same interview he said you do need some amount of compute, but that whether research requires the largest compute ever assembled is far from obvious — citing AlexNet's 2 GPUs and the Transformer paper's experiments on no more than 64. Less than a year later, his "enough compute" had risen by an order of magnitude. And one more: a company that as of August 2026 has published neither a paper nor a product received an order-of-magnitude increase in compute, and its research claims cannot be checked from outside.

Also overturned: "Orion is only 20% better than GPT-4" has no source; "first past 80%" does not hold; the ARC cost story runs the opposite direction from the circulating version; "$2,767 to evaluate o1" cannot be traced; the Nature hedge is an editor's standfirst and the authors' own wording is stronger; NVIDIA's paper is not a clean counterexample; and "every synthetic-data success is distillation from a stronger teacher" does not hold either.

**Which is the article in miniature: in this argument, nearly every sufficiently sharp claim gets duller once returned to its source — and what remains is usually more worth knowing than the version that was circulating.**
