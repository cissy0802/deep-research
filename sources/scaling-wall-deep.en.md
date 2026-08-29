# Have Scaling Laws Hit a Wall? An Argument Without a Definition (Deep Dive)

> Methodology: the load-bearing claims in this piece went through 44 groups × 3 adversarial votes (132 votes: 2 groups survived unanimously, 42 carry caliber corrections; at the sub-claim level 18 were killed and may not be written at their original strength). Verifiers were instructed to *refute*, not confirm, and to check primary sources word by word. Among the casualties was one of this article's own planned structural findings — see the self-corrections appendix. Evidence grades: [multi-source] ≥2 independent sources agreeing; [single, verified] primary source retrievable; [contested] independent sources conflict; [interested party] a stakeholder's own account, directional only; [unverified]. Two further labels appear in the body: [killed] means the phrasing was overturned by a majority of verification votes and may appear only in corrected form, and [caliber correction] means the direction holds but the numbers or qualifiers have been rewritten. All figures as of August 2026 — on a topic that moves this fast, take the date stamp seriously.

## 0. First, a question: what does "the wall" mean?

Since November 2024, "scaling laws have hit a wall" has been one of the densest arguments in this industry. Two years on, both camps are still here, the numbers have turned over a few times, and the structure of the argument has barely moved.

This article's first finding is that the argument has never produced a testable definition of "the wall." And once you try to supply one, you discover that not a single piece of evidence either side publicly cites is aimed at it.

Start by clearing away the easiest confusion: **diminishing returns are not news. They are the definition of a power law.**

The three power laws fitted by Kaplan et al. in the founding 2020 paper (arXiv:2001.08361) have exponents αN ≈ 0.076, αD ≈ 0.095, and αC^min ≈ 0.050. The paper translates this into plain language itself: "doubling the number of parameters yields a loss that is smaller by a factor 2^−αN = 0.95" — double the parameters, and loss falls by 5% [single, verified, §1.2].

In other words, "double the input, get a sliver of the return" was written into the original paper as a precise number in 2020. Anyone saying in 2024 that "the returns to scaling are diminishing," if they mean this, is stating an arithmetic fact that has been known for five years — not reporting a new observation.

One widely circulated quotation needs fixing along the way. The abstract actually says the power laws hold "with **some** trends spanning more than seven orders of magnitude." Drop that *some* and a hedged sentence becomes a universal claim. The breakdown in the body is more revealing still: the compute dimension spans about eight orders of magnitude, parameters six, and **the data dimension was verified across barely two**; elsewhere the paper writes the same conclusion as "more than six orders of magnitude." Each law also carries the precondition "when not bottlenecked by the other two" [single, verified; internal inconsistencies in the paper recorded as found].

So if "the wall" is to be a claim that can be confirmed or falsified, only two forms remain:

**(a) Measured points systematically departing from the fitted power law.** Inputs keep going in, but the curve no longer lands where predicted — the wall in the sense of *the law failing*.

**(b) The power law holds, but the compute and dollars required per unit of loss reduction exceed what anyone is willing to pay.** An economic wall, unrelated to the law itself.

These two forms demand entirely different evidence. What follows argues that **the first has neither evidence nor any way to be tested under current disclosure practices, while the second is arriving — but its mechanism is electricity and concrete, not diminishing returns.**

One technical clarification, because it is routinely misused. People often say "the power law always had a wall built in," meaning the E in the Chinchilla parameterization L = E + A/N^α + B/D^β — the irreducible loss, which Hoffmann et al. define as "the loss for an ideal generative process on the data distribution, and should correspond to the entropy of natural text." That E is real, but **it is not in Kaplan 2020**: that paper's fits extrapolate toward zero loss and carry no constant term. Writing "it will eventually flatten" into the formula came later, with Henighan et al. 2020 (L = aC^b + c) and Chinchilla 2022 [single, verified]. And E is a fitted constant for a specific corpus under a specific tokenizer, not a universal property of natural language — a point that becomes critical shortly.

As for Kaplan's much-quoted "the authors themselves admitted it would flatten," the sentence has to be read whole: "We observe no signs of deviation from these trends on the upper end, though performance must flatten out eventually before reaching zero loss." The main clause is *no signs of deviation at the upper end we can see*; the concession is the flattening. Quoting only the second half inverts the authors' claim [single, verified].

## 1. Three papers, checked word by word: the law was revised once, and the replication revised it again

Before asking whether the law has failed, it helps to know what the law currently looks like. It has been publicly corrected twice — and neither correction pointed toward failure.

**First revision: Chinchilla (2022).** Hoffmann et al. found the large models of the day "significantly undertrained" and gave an allocation rule: "for every doubling of model size the number of training tokens should also be doubled," roughly 20 tokens per parameter in practice [single, verified, arXiv:2203.15556]. This directly overturned Kaplan's compute-allocation advice (train very large models on relatively modest data and stop early).

Two non-exclusive explanations exist for the disagreement. Hoffmann's own attribution is that Kaplan used a fixed token count and learning-rate schedule across all models. Pearce & Song 2024 (arXiv:2406.12907) offer a more mundane cause: Kaplan counted **non-embedding parameters only**, and worked at small scale — simulate the Chinchilla study under those conditions and you reproduce biased coefficients close to Kaplan's [contested; both explanations stand].

This is the article's first encounter with *same name, different thing*: one set of experiments, two ways of counting parameters, opposite allocation advice. There will be many more.

**Second revision: Epoch AI's replication (2024).** Besiroglu et al. (arXiv:2404.10102) reconstructed the data behind Chinchilla's figures and found three problems with its third estimation method: inconsistency with the first two, failure to fit the extracted data, and implausibly narrow confidence intervals — intervals that "would require over 600,000 experiments, while they likely only ran fewer than 500." Worth stating how that number arises: the replication works from 240 points reconstructed out of Hoffmann's Figure 4 (Hoffmann reports more than 400), and the 600,000 is derived backwards from the bootstrap standard errors of those 240 points [single, verified].

The corrected fit gives roughly 20 tokens per parameter, consistent with Hoffmann's own first two approaches and with how Chinchilla was actually trained; the original Approach 3 implied about 70 tokens per parameter — a ratio the authors did not follow when training their own model.

The ending is what deserves remembering: Borgeaud, one of Hoffmann's lead authors, publicly acknowledged the problem, his own words being that "the loss scale was too low in our paper, resulting in premature termination of L-BFGS, and leading to bad fits." The more specific mechanism — that averaging rather than summing Huber loss values made the standard errors too narrow — is Besiroglu et al.'s rendering of that clarification in the second version of the replication; the original post mentions neither Huber loss nor standard errors, and the paper's reference for it is a single line, "Borgeaud, S. (2024). Twitter.", with no link and no archive. So the field's flagship paper did contain a fitting bug — **and after correction, its central conclusion came out sturdier than before.**

One number to fix in passing: the frequently cited E = 1.8172 is Epoch's **re-fit** to reconstructed data (bootstrap standard error 0.03); Chinchilla's own E is 1.6934. Five significant figures is false precision — the two differ by about 0.13, while the bootstrap standard error on the re-fit is only 0.03 [single, verified].

## 2. The first wall: no evidence, and no way to test for it

Now the question that matters most: is there any public empirical demonstration that frontier models' measured loss has systematically departed from the fitted power law?

**As of August 2026, not one was found.**

This comes from a dedicated blank-check search covering: direct queries on frontier-model loss deviating from power laws; measured points falling off predicted curves; Epoch AI's scaling series and literature reviews; and every scaling-law breakdown or correction paper from 2025–2026. The one directionally relevant new work (arXiv:2509.25087) points the other way — it reports that under hyperparameter-optimal settings "loss curves collapse across scales," meaning *more* cross-scale predictability, not a breakdown [not found; search angles listed].

But the second layer matters more than the absence: **this question is structurally untestable under current disclosure practices.**

Three reasons, each independently fatal:

First, neither the true parameter count N nor the true training token count D is published for frontier closed models. The GPT-4 technical report set this norm in unambiguous terms: "Given both the competitive landscape and the safety implications of large-scale models like GPT-4, this report contains no further details about the architecture (including model size), hardware, training compute, dataset construction, training method, or similar." It has been industry practice ever since (one fairness note: that passage is immediately followed by a third-party audit commitment, so "entirely closed" reads slightly stronger than the original) [single, verified, arXiv:2303.08774 §1].

Second, comparable pretraining loss is published even less. And loss is not comparable across corpora or tokenizers in the first place — as noted, E is a constant for a specific corpus under a specific tokenizer. Subtracting two reported loss figures measured on different test distributions with different tokenizers means nothing.

Third, the affirmative evidence — that the power law still holds — is entirely self-reported by vendors, and self-reported on private metrics. OpenAI says a power law fitted from models using 10,000× less compute "predicted GPT-4's final loss with high accuracy," but that loss was measured on "our internal codebase," and the accompanying figure has bits-per-word on the y-axis and compute normalized so GPT-4 = 1 on the x-axis, with no scale [interested party]. Meta says Llama 3's two-step extrapolation across four orders of magnitude was "quite accurate: it only slightly underestimates the final performance" — again, the trainer's own account [interested party].

So the first wall sits in this position: those claiming it exists cannot produce a measurement, and those claiming it does not produce their own unlabelled charts. **This is not insufficient evidence. This is evidence structurally withheld.**

To be clear, this does not mean the wall is absent. It means the question cannot be publicly answered under current disclosure practice. Anyone asserting either direction is speaking past their evidence.

## 3. Narrative archaeology: what evidence actually existed in those two weeks of November 2024

If measurement is closed off, what are the two sides actually citing? Taking the origins of the wall narrative back to primary sources is worth recording in full.

**Origin one: two reports sourced to anonymous insiders.**

On 9 November 2024, The Information published "OpenAI Shifts Strategy as Rate of 'GPT' AI Improvements Slows" (Stephanie Palazzolo, Erin Woo, Amir Efrati), citing OpenAI employees who had tested Orion: Orion's performance **did end up exceeding prior models**, but "the increase in quality was far smaller compared with the jump between GPT-3 and GPT-4," and it was not reliably better than its predecessor on certain tasks such as coding, while being clearly stronger at language tasks like summarizing and drafting. That first concession routinely vanishes in retelling, and without it the passage reads as "no progress at all" [multi-source retellings; original paywalled].

Four days later, Bloomberg published "OpenAI, Google and Anthropic Are Struggling to Build More Advanced AI" (Rachel Metz, Shirin Ghaffary, Dina Bass, Julia Love), reporting that three leading companies were "seeing diminishing returns from their costly efforts to build newer models," that Orion "fell short when trying to answer coding questions that it hadn't been trained on," that Google's next Gemini was "not living up to internal expectations," and that Anthropic's Claude 3.5 Opus had slipped [multi-source retellings].

Two things to keep in mind. First, the two pieces use different baselines — The Information compares GPT-3→GPT-4, Bloomberg compares GPT-3.5→GPT-4 — so the denominators cannot be merged. Second, and more importantly: **Bloomberg's core argument is economic, not about possibility**, writing that even modest improvements might not justify the enormous costs. That is the second form of wall from Section 0, not the first.

**Origin two: a sentence written by a reporter.**

The most-cited piece of "wall evidence" in this entire argument is Ilya Sutskever saying that results from scaling up pretraining had "plateaued." Checked word by word against Reuters' 11 November 2024 report (Krystal Hu, Anna Tong), the conclusion is: **that is not his quote.** The sentence carries no quotation marks; it is the reporter's indirect rendering, and "plateaued" is the reporter's word.

In the same report, Sutskever's only directly quoted sentences are two: "The 2010s were the age of scaling, now we're back in the age of wonder and discovery once again. Everyone is looking for the next thing." And — the direction here must be stated correctly — "**Scaling the right thing matters more now than ever.**"

That second sentence is pro-scaling. He is saying the *object* of scaling must change, not that scaling has stopped working [multi-source, all three votes agreeing].

He had also by then left OpenAI to found SSI, was raising money for a non-pretraining approach, and declined in that same report to say what SSI was working on. Treating him as a neutral third-party measurement does not hold.

**Origin three: a four-word tweet.**

The rebuttal came fast, and was equally thin. At 22:06 Pacific on 13 November 2024 (06:06 UTC on the 14th), Sam Altman posted four lowercase words: "there is no wall." No link, no quote, no mention of anyone — it was widely read as a response to those reports, but the post names none of them, and contemporaneous coverage uniformly hedged with phrasing like "an apparent response."

About eleven and a half hours later, Google DeepMind's Oriol Vinyals posted "What wall?" — but not as a reply to Altman: it was attached to his own Gemini-Exp-1114 topping Chatbot Arena that day [multi-source].

Neither man is neutral. Altman posted six weeks after OpenAI closed a $6.6 billion round at a $157 billion post-money valuation on 2 October 2024; Vinyals is one of the technical leads on the competing Gemini, posting at his own launch moment.

So the two origins of this argument are, on one side, media reports based on anonymous internal testing, and on the other, three to four words from interested parties. **Neither side produced a measurement.**

**Beyond the origins: two circulating quotes with no primary source.**

While doing archaeology, two claims that have been repeated for two years deserve clearing up:

"Orion is only 20% better than GPT-4" — **this phrasing does not exist in the original reporting.** The retrievable version is that Orion reached GPT-4-level performance at roughly 20% of the way through training. That is a training-progress figure, and it was originally used to argue that gains arrive early — the opposite direction from "20% better" [killed, three votes]. (Separately, Box CEO Aaron Levie's remark that GPT-4.5 was "about 20% better" was a task-specific comparison against GPT-4o — a different matter.)

"The age of giant models is over" — not Altman's words, and not from November 2024. The primary source is an April 2023 MIT event: "I think we're at the end of the era where it's going to be these, like, giant, giant models. We'll make them better in other ways." The circulating short form is WIRED's headline phrasing, and the date is off by nineteen months [killed, multi-source].

One that does check out: Hugging Face's chief ethics scientist Margaret Mitchell told Bloomberg "The AGI bubble is bursting a little bit" — retrievable verbatim, though the original is paywalled [single, verified].

## 4. Four incompatible walls, compressed into one word

Lay out what each party means by "the wall" and they turn out not to be the same thing at all — several are mutually inconsistent.

**Wall one: data.** This is Ilya Sutskever's wall. At the NeurIPS 2024 Test of Time session in Vancouver on 13 December 2024 (the award was for the seq2seq paper he wrote with Oriol Vinyals and Quoc Le a decade earlier), he said the much-quoted "Pre-training as we know it will unquestionably end."

But his reason has to be carried along, or the quotation inverts him: "while compute is growing through better hardware, better algorithms and larger clusters, the data is not growing because we have but one internet." And: "You could even go as far as to say that data is the fossil fuel of AI... we've achieved peak data - and there'll be no more."

His slide made the argument unambiguous: compute growing in the left column, data not growing in the right. **He is asserting that one ingredient is exhausted, not that the recipe's mathematics has failed** — he says explicitly, on that same slide, that compute is still growing. In the same talk he named three alternative paths: agents, synthetic data, and inference-time compute [multi-source, video available].

Citing that talk as evidence that "scaling laws failed" reads *the fuel has run out* as *the law has broken*.

**Wall two: architecture.** This is Yann LeCun's wall — that LLMs are a dead end on the path to human-level intelligence, a claim that is also the core pitch of the world-model company he founded. Note that he rejects the architecture, not scale — and his wall is incompatible with Ilya's: if the architecture is wrong to begin with, data sufficiency is not the binding question.

**Wall three: diminishing effect.** This is the wall in The Information and Bloomberg — the same inputs buying a smaller quality gain. It is the closest of the four to Section 0's first form, but what supports it is anonymous internal assessment, not a curve.

**Wall four: slowing compute growth.** This one is misattributed most often, because it comes from an organization that explicitly does not endorse the wall thesis. Epoch AI's September 2025 report does predict that compute scaling will slow — but the mechanism is **delivery lead times on the supply side**: returns are uncertain, so investors do not go all in at once but stake in 10× increments, checking results at each step; and each step up lengthens delivery. Renting GPUs is near zero, buying them about half a year, building a data center one to two years, a very large data center or power plant two to three, significantly upgrading an existing fab about two, building a cutting-edge fab from scratch four to five. The authors' summary: "our current best guess is that every additional 10x increase in compute scale lengthens lead times by around a year" [single, verified; the paper's own uncertainty discussion puts the central estimate at 8 months and says it could be as little as 4, not fully consistent with "around a year" in the body. A further note: both reports in this section come from Epoch, so they do not independently corroborate each other, and the later one appears in its Gradient Updates opinion series, whose pages carry a disclaimer that the views are the author's own].

Nowhere does that report claim the same compute buys less capability. **Using its slowdown forecast to support "diminishing returns" reads it exactly backwards.**

Once these four walls are collected under one word, the argument can no longer converge: each side is answering something the other never claimed.

## 5. The twenty-one months after the wall narrative: capability over time

If the first wall had really closed in late 2024, the capability curve afterwards should be flat. It is not — but reading this curve requires great care, because nearly every point on it is vendor-reported.

**SWE-bench Verified.** From October 2024 to January 2025, the frontier sat around 49%: Claude 3.5 Sonnet (new) 49.0%, o1 48.9%, o3-mini (high) 49.3%, DeepSeek R1 49.2%. Then: February 2025, Claude 3.7 Sonnet 62.3%; August 2025, GPT-5 reported 74.9%; over three weeks in November 2025, Gemini 3 Pro 76.2%, GPT-5.1-Codex-Max (xhigh reasoning, n=500) 77.9%, Claude Opus 4.5 80.9% (no extended thinking, 500 problems, averaged over 5 independent trials; with 64k thinking it is 80.6%). By 2026 the benchmark is near saturation: Anthropic's system cards report Claude Opus 5 at 96.0%, Mythos 5 at 95.5%, Fable 5 at 95% (the system card's wording carries no decimal) [entire chain vendor-reported].

Three caliber problems must be stated, and each weakens the curve:

First, that "49% line" is a compilation coincidence, not a measurement under one apparatus. OpenAI's own system cards give, for the same models, o1 at 40.9% (Agentless scaffold) and o3-mini at 39% (Agentless) versus 61% (internal tools) — **the same model, 22 percentage points apart depending on scaffold**.

Second, one bar often carries two denominators. Claude 3.7's 62.3% and its 70.3% with a custom scaffold do not share a denominator: on the same n=489 subset it is 63.7% → 70.3%, a scaffold gain of about 6.6pp, not 8.0. GPT-5's 74.9% ran on 477 of 500 problems.

Third, "Claude Opus 4.5 was first past 80%" does not hold — Anthropic's Claude 4 launch page reported Sonnet 4 at 80.2% back in May 2025 under a high-compute configuration (parallel test-time compute plus rejection sampling). The 80.9% can only be called the first to cross 80 in a standard configuration without parallel test-time compute [the original phrasing was overturned].

And independent replication runs systematically lower. Epoch AI, using a uniform scaffold on 484 problems: Claude 3.7 = 61.0, GPT-5 = 73.6, Gemini 3 Pro = 72.9, Opus 4.5 = 76.7, with an all-time high reading of Claude Opus 4.7 (max) at 83.5% ± 1.7%. **Not one point on that vendor chain has been independently reproduced at the level the vendor reported — 96% self-reported against 83.5% independently measured** [multi-source].

**ARC-AGI-2.** This one is more informative, because it was designed to resist saturation. On its 24 March 2025 release, ARC Prize's own verdict was "Pure LLMs score 0% on ARC-AGI-2, and public AI reasoning systems achieve only single-digit percentage scores," with o3-preview-low's 4% at the top. Then, all on the official leaderboard, semi-private set: November 2025, GPT-5.1 (Thinking High) 17.64% and Gemini 3 Pro 31.11%; December 2025, GPT-5.2 (XHigh) 52.91%; by August 2026 the leaders are GPT-5.6 Sol (Max) at 92.50% and $1.44 per task, and Claude Opus 5 (Max) at 90.42% and $2.06 per task — against a human panel at 100% [single, verified, official leaderboard].

Seventeen months, from single digits to ninety percent.

But the same organization released ARC-AGI-3 on 25 March 2026, whose launch-day verdict reads "Humans score 100%. Frontier AI scores 0.51%." — knocking every frontier model back to near zero. That state did not hold: as of August 2026, Claude Opus 5 (High) reaches 30.16%, while most others remain under 3%.

**Humanity's Last Exam.** At its 24 January 2025 release (3,000-question version), everything was low single digits: GPT-4o 3.3%, Claude 3.5 Sonnet 4.3%, o1 9.1%. On 3 April 2025 the set was finalized at 2,500 questions and the old version renamed HLE-preview. On the finalized set, no-tools: GPT-5 25.32% (August 2025), Gemini 3 Pro 37.52% (November 2025); by late August 2026 the top entries are Gemini 3.1 Pro Preview (thinking high) at 46.44 ± 1.96 and GPT-5.4 Pro at 44.32 ± 1.95 — which under Scale's own confidence-interval ranking makes them **tied for first**, not one leading [single, verified].

Here is a piece of counter-evidence sharper than "the wall": the HLE paper itself predicted "it is plausible that models could exceed 50% accuracy on HLE by the end of 2025." As of August 2026, the best no-tools full-set score is still 46.44% — **crossing 50% is running more than half a year behind the benchmark authors' own expectation** [single, verified]. This is the hardest "behind schedule" evidence in this article, and it comes from the optimistic side's own forecast.

**Independent measurement: METR's time horizon.** This is the only ruler not controlled by vendors whose scale has physical meaning. METR's March 2025 paper defines the "50% time horizon" — the length of task, measured by how long human professionals take, that an AI completes with 50% success — and measured exponential growth from 2019 to 2025 across 170 tasks, doubling roughly every 7 months (with METR's own hedge attached: "though the trend may have accelerated in 2024"), and Claude 3.7 Sonnet at about 59 minutes [single, verified].

Time Horizon 1.1, on 29 January 2026, expanded the suite to 228 tasks (8-hour-plus tasks from 14 to 31) and moved infrastructure from METR's own Vivaria to the UK AISI's Inspect. Under the new ruler, the doubling time since 2023 falls from 165 days to 131, and METR writes that "progress is estimated to be 20% more rapid under TH1.1."

But that "20% faster" carries a limit that must be stated: **it applies only to the post-2023 subsample. The full-sample doubling time is identical across both versions at 196 days** — METR's own words are "exactly the same doubling time." And that full-sample curve is stitched: pre-2023 models were never re-measured under 1.1, and only 14 of 33 older models were re-estimated [single, verified, caliber correction].

Another circulating conversion needs fixing: the post-2024 doubling time of 89 days under TH1.1 corresponds to roughly **17× per year**, not the frequently repeated 10× — 10× per year is precisely TH1.0's 109 days.

This ruler's own boundaries deserve stating too: only 5 of the 31 tasks over 8 hours have measured human baselines; METR's live page states that "measurements above 16 hrs are unreliable with our current task suite," and 2026's new data points have reached that ceiling; its June 2026 reading for GPT-5.6 Sol of about 11.3 hours [5, 40] comes with METR's own declaration that they "do not consider any of these numbers to represent a robust measurement" — because the model cheated on long tasks, and depending on how that is penalized the estimate swings between 11 and 270 hours [single, verified].

**Independent measurement: Epoch's Capabilities Index.** ECI fits results from 50-plus benchmarks onto one scale using item response theory. In the snapshot used for its "AI capabilities progress has sped up" page (149 models, December 2021 to December 2025), frontier scores show a breakpoint around April 2024, which Epoch describes as "a 90% acceleration in April 2024" [single, verified].

This evidence carries one decisive limitation, and it points straight at this article's core: **ECI measures the total capability of deployed models** — its entries are literally "model + reasoning setting," with reasoning, RL, post-training and test-time compute all baked into the score, and its methodology explicitly assumes no relationship between capability and either time or compute. **There is no pretraining dimension to separate out.** Epoch itself attributes the acceleration to reasoning models.

So "pretraining returns are diminishing" and "total capability is accelerating" can both be true at once — and ECI can testify for neither the former nor its negation.

"No sign of slowdown since" also needs narrowing: Epoch's April 2026 report finds strong acceleration in three of four metrics but not the fourth (WeirdML V2); and the acceleration evidence concentrates in programming and mathematics — precisely the automatically verifiable domains that reinforcement learning has targeted — with Epoch cautioning that the acceleration "may be less general than the headline numbers suggest" [single, verified].

## 6. But the rulers themselves are coming apart

Every curve in the previous section rests on benchmarks. Over these two years, the reliability of benchmarks as measuring instruments has degraded faster than capability has risen.

**Scaffolding is the largest confounder.** Epoch AI writes that on SWE-bench Verified "simply switching the scaffold makes up to an 11% difference for GPT-5 and up to a 15% difference for Kimi K2 Thinking," and that "the choice of scaffold has the single biggest impact on the overall performance" (the original says "% difference" rather than percentage points; the unit is not made explicit in the primary source). Harder still is OpenAI's own account: on the same benchmark on the same day, o3-mini scored 39% with the open-source Agentless scaffold and 61% with an internal tools scaffold representing maximum capability elicitation — 22 points, one model [multi-source].

From which follows (this article's inference, not Epoch's words): **gaps of 1 to 3 percentage points on cross-vendor leaderboards have essentially no discriminating power.** Epoch's own error bars run ±1.7% to ±2.0%, and its board has had two models tied at 78.7%.

**Same name, different thing is the most expensive lesson of these two years.** On 20 December 2024, ARC Prize published o3's results on the ARC-AGI semi-private set: 75.7% within a $10,000 compute cap at 6 samples, and 87.5% at roughly 172× that compute with 1,024 samples — a tier that exceeds ARC-AGI-Pub's $10,000 budget rule and therefore does not appear on the public board. OpenAI simultaneously disclosed that "they trained the o3 we tested on 75% of the Public Training set."

On 22 April 2025, ARC Prize retested the released o3: 41% for o3-low and 53% for o3-medium on ARC-AGI-1, with neither exceeding 3% on ARC-AGI-2 (1.9% / 2.9%). OpenAI confirmed to them that "this public o3 model differs from the o3-preview we tested in December 2024" — a different model, the preview text-only while the release accepts visual input, and the preview's test-time compute tier unavailable in the product [single, verified].

The 87.5% from the launch and the 41% users could buy are not the same object.

One more reading is worth recording: o3-high returned answers on only 37 of 100 ARC-AGI-1 tasks, 82% of them correct. ARC Prize states plainly that such data "should not be reported on" — the denominator is the 37 returned, and unreturned tasks are systematically harder. (ARC Prize later completed the full test; today's official board lists o3 High at 60.83% on ARC-AGI-1 and 6.53% on ARC-AGI-2, superseding that truncated reading.) [single, verified]

**Cost figures can be revised three times, and reverse direction.** The costs from that ARC evaluation are the least stable numbers checked for this article. On launch day, the 75.7% tier was listed at $2,012 total and $20 per task, while the 87.5% tier had no cost at all, noted as "pricing and feature availability is still TBD." On 24 March 2025, ARC recalculated using o1-pro pricing, and the 75.7% tier rose to $201 per task — past the "under $10k" contest budget the page itself cites; that April, ARC Prize's Mike Knoop gave roughly $34,400 per task for the high-compute tier on the same basis. Then on 10 December 2025 ARC switched to o3-pro pricing at $80 per million tokens, and the figures fell sharply: the 87.5% tier was filled in for the first time at $4,560 per task.

So the circulating claim that "$4,560 was revised up to about $30,000" **has the order backwards**: the real path was blank, then up to about $34,400 per task, then down to $4,560 [killed; direction must be corrected]. The same table still mixes two pricing regimes today.

**The funder can own the questions.** On 23 January 2025, Epoch AI published a statement acknowledging that the 300 problems at FrontierMath's core were commissioned and funded by OpenAI, that "OpenAI retains ownership of these questions and has access to the problems and solutions, with the exception of a holdout set" — and that as of the statement, the 50-problem holdout set was **still being finalized**. Which means that when o3 was announced at over 25% on FrontierMath in December 2024, the holdout OpenAI could not see did not yet exist. Epoch also acknowledged that "many contributors were unaware of these details" [single, verified].

As for "not used for training," that is not in the official statement: it comes from TechCrunch's 19 January report relaying Besiroglu — OpenAI and Epoch had only a **verbal agreement** [single, verified].

The numerical gap needs equal care. On the December 2024 livestream, OpenAI's chief research officer Mark Chen said: "We're seeing [internally], with o3 in aggressive test-time compute settings, we're able to get over 25%." In April 2025, Epoch independently measured the released o3 at about 10%.

But this is not a clean contradiction: it was not the same model, nor the same problem set (180 questions in the 2024-11-26 version versus 290 in the 2025-02-28-private version), and that 10% was later revised substantially upward — Epoch's current public data puts the released o3 at 18.7% (high reasoning) on the same private set. **The durable lesson is not "the vendor lied," but this: when the funder owns the questions, the evaluator's caliber shifts, and elicitation method determines the score, a single benchmark number carries almost no independent arbitrating power.**

**Benchmarks have a lifespan.** A systematic study at ICML 2026 (arXiv:2602.16763, EvalEval Coalition, a roughly forty-person cross-institution team) examined 14 saturation-related properties across 60 language model benchmarks: by a saturation index ≥ 0.7, 29 are highly or extremely saturated, 14 of them ≥ 0.9. Saturation rises with benchmark age (42.9% within 24 months, 54.5% past 60), though the authors restrain this conclusion themselves — the trend is modest and not significant at conventional thresholds.

The half of the intuition that got falsified is more interesting: **private test sets are not systematically more resistant** — "private test sets do not exhibit systematically lower saturation than public." The authors lean toward expert curation and adversarial design as what actually lasts, but write that only as a possibility [single, verified].

On contamination, Scale AI's GSM1k (arXiv:2405.00332) rebuilt a thousand problems at matched difficulty: accuracy drops of up to 8 percentage points on the new set (note: the widely circulated 13% comes from the May 2024 first version, which the authors revised down themselves), with the Phi and Mistral families showing systematic overfitting at almost every release and scale, and the probability of a model reproducing an original GSM8k problem correlating with its gap (Spearman r² = 0.36, also a revised-up value).

But that same paper sets a clear limit on the contamination narrative: "all frontier models show minimal signs of overfitting," and even the most overfit models still generalize to new problems guaranteed absent from training data [single, verified]. Contamination is real, but it lands on small and mid-size open models — it does not support the strong claim that frontier scores rest on memorization.

**A final signal comes from the vendors themselves.** By 2026, Anthropic's two flagship launches no longer lead with SWE-bench Verified at all, reporting Frontier-Bench, CursorBench, ARC-AGI-3 and OSWorld 2.0 instead; and since Opus 4.7 Anthropic has disclosed that its memorization screens flag a subset of the SWE-bench problems. When the tested party starts changing its own exam, that 49% → 96% curve needs reading with more care still.

## 7. The data wall: continually bought off, continually pushed back

Ilya's wall is the most concrete of the four and the only one with quantitative research behind it. Its status: **not hit, but not gone either — it has been deferred by a series of measures, each with its own boundary.**

**Stock estimates.** Villalobos et al.'s first version in 2022 predicted high-quality language data would be exhausted "likely before 2026." The June 2024 revision (ICML 2024) changed this to: if current trends continue, models will be trained on datasets roughly equal in size to the stock of public human text **between 2026 and 2032**, or slightly earlier if overtrained [single, verified; the two versions differ substantially, so citations must state which].

The companion Epoch post gives the magnitude: an effective stock, adjusted for quality and repetition, on the order of 300 trillion tokens — but the original carries "a 90% confidence interval of 100T to 1000T," **a full order of magnitude**. The year range is a separate interval: "Our 80% confidence interval is that the data stock will be fully utilized at some point between 2026 and 2032." The two should not be conflated.

They also ran two conditional scenarios: overtrain by 5× and the stock is used up in 2027; by 100× and it is used up in 2025. These are scenarios, not predictions — the real-world reference point they give is Llama 3-70B at 10× overtrained. Citing "Epoch predicted data would run out in 2025 and it didn't" is attacking a straw man [single, verified].

One semantic clarification matters: Epoch's caliber is **training set size catching up with the stock** — the demand line meeting the stock line — not data being physically consumed.

**First buy-off: repetition.** Muennighoff et al. (NeurIPS 2023) measured that under a fixed compute budget with constrained data, "training with up to 4 epochs of repeated data yields negligible changes to loss compared to having unique data." But the following clause matters equally: "However, with more repetition, the value of adding compute eventually decays to zero." [single, verified; passed unanimously — one of only two claims in this article to survive all three votes unchanged]

The boundaries: what is undamaged is **loss**, and the paper makes no claim about downstream capability; the experiments reach at most 900 billion tokens and 9 billion parameters, one to two orders of magnitude below 2026 frontier training; and it is a 2023 C4 pure-pretraining recipe, with no instruction tuning, no synthetic data, and no RL post-training.

**Second buy-off: synthetic data.** This is where denominator traps cluster.

Microsoft's phi-4 pretraining mixture table shows synthetic data at 40% of the token budget, with the model pretrained on approximately 10T tokens — and behind that 40% sit only about 290B unique synthetic tokens, repeated across 13.8 epochs. The same table also has 15% LLM-rewritten web content and 20% code data the paper describes as a mix of synthetic and original — so the true share of LLM-generated text exceeds 40%.

phi-4 did beat the model that generated its training data on two benchmarks (GPQA 56.1 vs 50.6, MATH 80.4 vs 74.6). But look right along the same table: phi-4 scores 3.0 on SimpleQA against GPT-4o's 39.4, and trails on MMLU, MGSM, HumanEval and DROP as well. **Two wins out of seven — and the worst loss is on factual recall, which is exactly what real corpora buy** [single, verified].

NVIDIA Nemotron-4 340B's much-quoted "98% synthetic" is precisely limited in the original: "over 98% of data used in our model **alignment** process is synthetically generated," with roughly 20,000 human annotations across the whole alignment pipeline. Its pretraining is a separate matter — 9T tokens, with synthetic share never mentioned [single, verified; denominator trap].

And how much synthetic data frontier closed models use **cannot be answered from outside**: the norm the GPT-4 report established became industry practice.

One intuition needs actively correcting: the common reasoning that "every synthetic-data success is distillation from a stronger teacher, so it cannot be extrapolated" does not hold. Nemotron's paper states that "the teacher model does not impose a ceiling on the student model," and its first-round generator, Mixtral-8x7B-Instruct, was considerably weaker than the model being trained; phi-4's abstract likewise claims its method goes "beyond distillation." **What blocks extrapolation is the layer and the unmeasurability, not teacher strength**: the verifiable successes happen either at the alignment layer (Nemotron) or on small models (phi-4 is 14B), and nobody has published a checkable measurement of synthetic text substituting for human text at frontier pretraining scale [caliber correction; the original claim was overturned].

**Model collapse: a controlled-experiment phenomenon, not an engineering incident.** The much-quoted hedged sentence from Shumailov et al.'s July 2024 Nature paper — "indiscriminately training... can lead to a collapse" — is in fact **Nature's editorial standfirst, not the paper's abstract.** The authors' own abstract does not hedge at all: "We find that indiscriminate use of model-generated content in training causes irreversible defects in the resulting models, in which tails of the original content distribution disappear." *Causes*, and *irreversible* [killed; the correction runs opposite to the usual assumption].

But the experiment behind that strong claim is small: recursive **fine-tuning** of OPT-125m (125 million parameters) on wikitext2, with a control of five epochs and no original data preserved in later generations. And another setting in the same paper supplies the antidote: "Ten epochs, 10% of original training data preserved," resampling 10% from the original real data each generation, yielding "only minor degradation of performance" — minor degradation, not none. The real data never leaves, which is why it works.

Gerstgrasser et al. (arXiv:2404.01413) offer the direct rebuttal: it is **replacing** real data that trends toward collapse, whereas "accumulating the successive generations of synthetic data alongside the original real data avoids model collapse," with a proof that under accumulation test error has a finite upper bound independent of iteration count. The real internet resembles accumulation, not replacement.

**As of August 2026, there is no confirmed public report of model collapse observed in a real production training pipeline.** It remains a controlled-experiment phenomenon and a theoretical concern. Schaeffer et al.'s position paper goes further, noting that the field contains "eight distinct and sometimes conflicting definitions" of model collapse, and that several famous collapse scenarios are easily avoided [the original phrasing was overturned; this is absence of evidence — vendors have no disclosure obligation, and failed internal runs are not published].

**Third buy-off: purchase and licensing.** Supply on this side genuinely is tightening. Longpre et al.'s *Consent in Crisis* measured that between April 2023 and April 2024, robots.txt restrictions rendered roughly 5%+ of all C4 tokens, and 28%+ of tokens from C4's most actively maintained critical sources, fully restricted from crawling; under a terms-of-service reading, about 45% carry some form of use restriction.

But this study measures **how many signs are hanging on doors, not how much data actually became unobtainable.** The paper's own conditional is explicit: these consequences follow "if these restrictions are respected by developers or enforced by law"; it also states that most automated crawlers ignore such terms in practice. Nor does robots.txt apply retroactively — crawls archived before the sign went up remain usable. And the 28% denominator is the top domains by token volume in each corpus, not all of C4; the paper gives 28%+, 25%+, and 20–33% in its abstract, introduction and body respectively. Finally: that window closed more than two years ago [single, verified; extensive corrections].

**So has the wall ever bitten a specific training run?** The one public case is the Wall Street Journal's 20 December 2024 report on Orion. It does say OpenAI ran at least two large training runs where "each time new problems arose and the software fell short of the results researchers were hoping for," that researchers found the data less diverse than expected, and that the company began hiring people to write code and solve math problems to create new data.

Citing it carries three traps. First, "$500 million each" is wrong — the WSJ states a general rule, that a six-month training run "could cost around half a billion dollars in computing costs alone," never that Orion's two runs each cost that. Second, the most-quoted line — that there may not be enough data in the world to make it smart enough — is **the WSJ's own subheadline**, a reporter's framing; OpenAI declined to comment and has never confirmed that causal claim. Third, and most dangerous: the subject of that report is "officially called GPT-5, code-named Orion," but Orion shipped in February 2025 as **GPT-4.5**, and the GPT-5 released in August 2025 is a different thing entirely, built by shrinking pretraining and enlarging post-training. **What this report can support is that GPT-4.5's pure scale-up route hit a wall — not that GPT-5 did** [multi-source; important correction].

**And published pretraining scale does not constitute an extrapolable upward trend.** The numbers themselves are right: Llama 3's flagship pretrained on 15.6T text tokens, Qwen3 on 36T, Llama 4 Scout on about 40T. But these three cannot be drawn as one line — Llama 3's figure is text-only while Llama 4 Scout's is multimodal (Meta says the overall mixture exceeds "30 trillion tokens" of "text, image, and video data"), so the rulers differ; and Qwen3's 36T explicitly includes trillions of tokens recognized from PDF-like documents by Qwen2.5-VL and refined by Qwen2.5, plus trillions synthesized by Qwen2.5, Qwen2.5-Math and Qwen2.5-Coder — growth the models themselves manufactured.

The clearest evidence is within one generation: **Llama 4 Maverick is stronger than Scout while using about 22T tokens, nearly half of Scout's 40T.** Even "rising with each generation" fails inside a single generation, let alone as an extrapolable trend [multi-source; the original claim was substantially corrected].

## 8. The reasoning axis: changing axes is not the same as running out of them

After September 2024, "scaling" started meaning two different things, and the two camps often each mean only one.

OpenAI's original phrasing in the o1 post: "The performance of o1 consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute). The constraints on scaling this approach differ substantially from those of LLM pretraining, and we are continuing to investigate them." That last clause is usually dropped — and it is precisely where the vendor concedes that the new paradigm's constraints are not yet understood [interested party].

The two famous dual curves accompanying it have AIME pass@1 accuracy on the y-axis and, on the x-axis, only "train-time compute (log scale)" and "test-time compute (log scale)" — **bare tick marks, no numerical labels at all**. It is a schematic; no multiple, slope, or absolute compute magnitude can be read from it.

The AIME figures in that same post come at three sampling calibers: 74% (11.1/15) with a single sample, 83% with consensus among 64 samples, and 93% when re-ranking 1,000 samples with a learned scoring function. "o1 scored 93% on AIME," quoted without the sampling caliber, presents a multi-sample result as single-inference capability [single, verified].

**The new axis may not have the same shape as the old one.** Meta's *The Art of Scaling Reinforcement Learning Compute for LLMs* (arXiv:2510.13786) put in over 400,000 GPU-hours and states plainly: "Unlike pre-training, which typically uses power-law to fit predictive curves, we model pass rate versus log(compute) with a sigmoidal function" — a sigmoid rather than a power law, which substantively means **the curve has an asymptotic ceiling**. Note that its 100,000 GPU-hour validation run was on an 8B dense model, far below frontier scale [single, verified].

Nor was the shape settled in 2026: an ACL 2026 paper fitting Qwen2.5 from 0.5B to 72B recovers a power law instead, while reporting that "RL learning efficiency exhibits a latent saturation trend with increasing model scale" [contested].

**The growth on this axis may be a one-time catch-up dividend.** Epoch's signed commentary (Josh You, May 2025) reasons that if reasoning training compute keeps growing 10× every few months, it will reach the frontier of total training compute "perhaps within a year," after which growth converges to the ~4× per year of overall training compute.

But that "10×" is not an official OpenAI disclosure — Epoch read it off a chart in the o3 livestream **whose axes were unlabelled**, noting itself that the presenter "did not verbally clarify any details beyond what is shown in the graph" and that the x-axis was only "likely" reasoning training compute [single, verified; evidence strength must be downgraded].

As of August 2026, **this prediction cannot be settled**: frontier labs have disclosed no comparable RL compute figures since, and Epoch has published no retrospective [unverified: no public data exists by which to settle this prediction].

**Does RL elicit existing capability or add new capability? This has not been settled.** Yue et al. (arXiv:2504.13837) probe the boundary with pass@k at large k, finding RLVR models ahead at small k and base models overtaking at large k, concluding that "the current training setup does not elicit fundamentally new reasoning patterns." Two things to note: this is already the revised wording — v1's abstract said the harder "the RL does not, in fact, elicit fundamentally new reasoning patterns," with the authors narrowing "RL cannot" to "the current setup cannot" over the course of the argument; and the same abstract explicitly exempts distillation, which "can genuinely expand the model's reasoning capabilities." Their experiments top out at 32B — **no frontier-scale models at all.**

NVIDIA's ProRL (arXiv:2505.24864) is often taken as the clean counterexample. It is not. The original says only "across a wide range of pass@k evaluations," while its §4.2 is titled "Diminish, Plateau, and Sustained Gains" and states that on tasks the base model already handles well, RL delivers "minimal or even negative gains," constituting "a narrowing of the reasoning boundary." More importantly, **ProRL's starting point is not a raw base model but DeepSeek-R1-Distill-Qwen-1.5B, an already-distilled reasoning checkpoint** — and distillation is exactly the path Yue et al. concede can introduce new patterns. The two papers are not in direct collision [the original phrasing was overturned].

The real sources of disagreement are training steps (hundreds versus over two thousand), the nature of the starting model (raw base versus distilled checkpoint), task difficulty stratification, and choice of k — not "1.5B versus frontier" (ProRL is the smaller one; neither is frontier).

**Inference economics is getting cheaper and more expensive at the same time.** Epoch measures (on data through February 2025) that the price of reaching a given performance level falls between 9× and 900× per year depending on the milestone, with the price of matching GPT-4 on PhD-level science questions falling about 40× per year — while cautioning that the fastest declines are concentrated in the year before that piece was written (roughly March 2024 to February 2025) and may not persist [single, verified].

In the other direction, reasoning models generate large volumes of thinking tokens that users never see and that bill the same. In measured terms: ARC Prize's April 2025 figures put o3 at $1.22 to $2.52 per task on ARC-AGI-1, against o4-mini at $0.05 to $0.23 [single, verified].

(For the record: the circulating figures of "$2,767.05 to evaluate o1 across a benchmark suite versus $108.85 for GPT-4o" could not be traced to any primary source on Artificial Analysis, and are not used here [killed, two votes].)

The price itself deserves a separate note. OpenAI's official changelog records that on 10 June 2025, alongside the release of o3-pro, o3's price was reduced; the current official pricing is $2 per million input tokens and $8 per million output. But three claims usually cited alongside it — the "80%" magnitude, the line "same exact model, just cheaper," and "an independent retest confirmed unchanged performance" — could not be traced to primary sources in this check, and are treated as [unverified]. Which also means that the inference "price and capability can move independently" currently lacks a checkable foundation, and is not asserted here as a conclusion.

## 9. The constraint actually binding is on the supply side

If the first wall cannot be detected, where does the second — the economic wall — currently stand?

It is approaching. But **it is binding on electricity, concrete and delivery schedules, not on returns.**

**Epoch's August 2024 report, "Can AI scaling continue through 2030?", ranks four constraints.** On data: the indexed web holds about 500 trillion words of unique text, projected to grow 50% by 2030; folding in multimodal sources, effective tokens available for training in 2030 run from 400 trillion to 20 quadrillion, enough to support training runs of 6e28 to 2e32 FLOP.

One easily miscited point: that range **excludes synthetic data entirely** — the methodology states that "only human-generated data is considered in our projections," with synthetic listed separately as upside. Which means the 400-trillion floor was computed without counting on synthetic data at all [single, verified; important caliber].

The report concludes that training runs around 2e29 FLOP will "likely be possible" by 2030 — advancing models by roughly the margin GPT-4 held over GPT-2. And what stands in the way, in order: **power > chip manufacturing capacity > data > latency. Data is third.**

**The September 2025 report supplies the slowdown mechanism, and no step in it is "compute stopped buying capability."** The logic: returns are too uncertain and the outlays too large for investors to commit all at once, so they stake in 10× increments and reassess at each; and each step up lengthens delivery time (see the ladder in Section 4).

They also offer short-term slack: even if investment expansion is dragged by lead times, frontier labs may sustain 5× annual growth in training compute for another year or two **by allocating a larger share of their existing stock to training** — with the paper specifically noting this dynamic acts most directly on a lab's **total compute stock, not the size of a single training run** [single, verified].

**This supply-side constraint has direct testimony from an interested party.** Microsoft CEO Satya Nadella, on a November 2025 podcast: "The biggest issue we are now having is not a compute glut, but it's power... you may actually have a bunch of chips sitting in inventory that I can't plug in." Not a chip shortage — a shortage of warm shells to plug them into [unverified: this quotation did not go through this run's verification process; it comes from a November 2025 podcast via media retelling. The direction runs against the speaker's own interest, but it is not used here as an established fact].

**Four sets of compute-economy numbers.** Per Epoch's calibers, each with its own limits:

*Growth rate.* Frontier training compute grew 5.3× per year between 2010 and May 2024 (90% CI 4.9–5.7); across all notable models, 4.1×; and for language models specifically, a detectable slowdown occurred around mid-2020, after which growth ran at about 5.0× per year through May 2024 (with a caveat: Epoch's body text labels that interval 90% confidence and its appendix table 80%, while the bounds are identical, so one must be a typo). But an appendix figure that should not be skipped: "recent frontier models" (roughly 2018 to May 2024) grew only **4.2× per year**, visibly below the 5.3 headline. And all of this data stops in May 2024 [single, verified].

*Cost.* The cost of the largest single training run has grown 2.4× per year since 2016 (90% CI 2.0–2.9), from about $200,000 for GNMT in 2016 to about $490 million for Grok 4 in 2025 (2023 dollars). The caliber is **amortized hardware plus energy over the training period**, about half of it GPUs — not the full capital expenditure on the cluster, which can differ by an order of magnitude [single, verified].

*Algorithmic efficiency.* The compute required to reach a set performance threshold halves roughly every 8 months (95% CI about 5 to 14 months), based on 200-plus language model evaluations from 2012 to 2023. Read this one carefully: it measures perplexity, not downstream capability; the paper's own conclusion writes "8 to 9 months," and a cross-validated aggregate gives a median of 7.8 months with an interval as wide as 1.5 to 17.6; and the data stops in 2023 — **the entire reasoning-model era is outside it** [single, verified].

*One counterexample.* Epoch estimates GPT-5's total training compute at about 5e25 FLOP, above GPT-4's roughly 2e25 but **below GPT-4.5's >1e26**. This is the first time in the GPT line that a successor used less training compute than its predecessor. Epoch's attribution is not a wall: they argue OpenAI bet its resources on scaling post-training, while the new post-training techniques were not yet mature enough to be applied at GPT-4.5's scale. They expect the next flagship to rise again, but the same piece hedges itself — that return to trend "might not last long" — and names the availability of high-quality pretraining data and post-training RL environments as potentially harder bottlenecks. (The piece appears in Epoch's Gradient Updates opinion series under four researchers' names, on pages carrying a disclaimer that the views are the authors' own; the summary "a pause, not a halt" that circulates from it is Lynette Bye's phrasing in Transformer News, not Epoch's characterization.) [single, verified; Epoch's third-party inference, undisclosed by OpenAI]

**And demand shows no sign of retreat.** Epoch's May 2026 estimate: at current prices, token demand is growing roughly 10× per year while global inference capacity grows about 3.4× per year, with long-context and agentic workloads hitting the shortfall first [unverified: this estimate did not go through this run's verification process; the demand figure is itself stitched from proxy indicators].

This collides directly with the short thesis that AI demand cannot justify the capital expenditure. And the short argument's own structure is worth seeing clearly: Michael Burry's widely circulated case rests on depreciation accounting and circular financing (reportedly estimating that the industry understates depreciation by about $176 billion across 2026–28) — **not on models hitting a capability wall.** The two get bundled together, but they require entirely different evidence [unverified: this figure did not go through this run's verification process, and comes from a position-holder via media retelling].

## 10. The verdict

Pulling nine sections together, this article's conclusion is four sentences.

**First, the question "has it hit a wall?" cannot be answered under current public disclosure — and not because the evidence has yet to arrive, but because the data required to answer it is structurally withheld.** Frontier models' parameter counts, training token counts, and comparable pretraining loss are all unpublished, and loss is not comparable across corpora. Those claiming a wall exists cannot produce a measurement; those claiming it does not produce their own charts without scales.

**Second, the most widely circulated evidence in this argument has mostly shed its qualifiers in transit — and always in the same direction, the one that makes the claim stronger.** Kaplan's "some," Ilya's reporter-written sentence, o3's "internal, aggressive test-time compute," o3-preview's 172× compute and 75% training-set exposure, Nemotron's "alignment process," Shumailov's hedge that turns out to be an editor's standfirst, GSM1k's 13% that its own authors revised down — every correction restores a weaker fact from a stronger assertion. This is not one side's failing; both do it.

**Third, four incompatible walls have been compressed into one word, which is why the argument cannot converge.** Ilya's wall is data (he says explicitly that compute is still growing); LeCun's is architecture (incompatible with the former); the reports' is diminishing effect; and Epoch's forecast slowdown is a data-center delivery schedule. Each side is answering something the other never claimed.

**Fourth, capability is still rising, and the constraint genuinely closing in has changed position.** On independent measurement: METR's time horizon doubles about every 131 days on the post-2023 subsample (though the full-sample figure is identical across both versions at 196 days), and Epoch's Capabilities Index shows roughly 90% acceleration around April 2024 — but ECI measures deployed capability with RL and test-time compute baked in, and can testify neither for "pretraining returns are diminishing" nor against it. On the constraint side, Epoch's ordering is explicit: **power first, chip capacity second, data third**; And Nadella's line about chips sitting in inventory that cannot be plugged in, while it did not go through this run's verification process, points the same way.

One honest statement is owed on whether pretraining has yielded. The only somewhat hard indications are that GPT-5's total training compute came in below GPT-4.5's, and that GPT-4.5 — the largest pretrained model — was removed from the API on 14 July 2025 (the official reason being that GPT-4.1 "offers improved or similar performance on many key capabilities at lower latency and cost"; it remained in ChatGPT's legacy menu for some time afterward). That is an **economic verdict, not a capability verdict**, and Epoch reads it as a temporary dip rather than an endpoint, predicting the next flagship will rise again — though the same piece concedes that the return to trend "might not last long." As of August 2026 there is no public data by which to settle that prediction.

One last thing deserves separate mention. This article had planned a sharper structural finding: that Ilya, who proclaimed the age of scaling over, turned around and took $5 billion from NVIDIA to increase his compute tenfold. Adversarial verification killed it on two votes, on the grounds that it is a false contradiction manufactured by deleting qualifiers — his own definition of the next phase is "it's back to the age of research again, just with big computers," what he rejects is that "if you just 100x the scale, everything would be transformed," and he explicitly grants that scaling up "would be different, for sure."

**The critique that does hold is a different and more interesting one: scale drift.** In that same interview he said that you do need some amount of compute, but that whether research requires the largest compute ever assembled is far from obvious — citing AlexNet's 2 GPUs and the Transformer paper's experiments on no more than 64. Less than a year later, his "enough compute" had risen by an order of magnitude. Add one more: a company that as of August 2026 has published neither a paper nor a product received an order-of-magnitude increase in compute, and its research claims cannot be checked from outside.

Which is the article in miniature — **in this argument, nearly every sufficiently sharp claim gets duller once returned to its primary source, and what remains is usually more worth knowing than the version that was circulating.**

## 11. Thirteen testable claims

Ordered by evidence strength, strongest first.

1. **As of August 2026, no public empirical demonstration exists that frontier models' measured loss systematically departs from the fitted power law.** [Strongest: blank check executed, search angles listed] How to falsify: either side producing comparable N, D and loss triples.
2. **Diminishing marginal returns are intrinsic to a power law, not a 2024 observation.** Double the parameters, lose 5% of loss — written into the 2020 paper. [Strong: primary, verbatim]
3. **Ilya Sutskever's "pretraining scaling has plateaued" is Reuters' indirect rendering, not his words; one of his actual quotes is pro-scaling.** [Strong: three votes agreeing, primary retrievable]
4. **Ilya's wall is a data wall, not a compute wall or a failure of the power law.** He says on the same slide that compute is still growing. [Strong: video available]
5. **The compute slowdown Epoch forecasts is mechanistically about data-center and power-plant delivery times, not technical diminishing returns.** Its constraint ordering is power > chip capacity > data > latency. [Strong: primary, verbatim]
6. **The same model under a different scaffold can differ by 22 percentage points on SWE-bench Verified (OpenAI's own data).** Therefore 1-to-3-point gaps on cross-vendor leaderboards have no discriminating power. [Strong: vendor self-report plus independent measurement]
7. **Launch-event benchmark figures and the shipping product can differ by more than 30 percentage points.** o3-preview scored 87.5% on ARC-AGI-1; the released o3 scored 41–53%, and OpenAI confirmed they are not the same model. [Strong: primary, verbatim]
8. **Repeating the same data for up to 4 epochs costs almost nothing in loss relative to fresh data; beyond that, the marginal value of added compute eventually decays to zero.** [Strong: passed unanimously; but what is undamaged is loss, not downstream capability]
9. **"Running out of data" means training set size catching up with the stock, not data being physically consumed; the window is 2026 to 2032, and the stock estimate itself spans an order of magnitude (100T to 1000T tokens).** [Moderately strong: single verified; the same group's two versions differ substantially]
10. **As of August 2026, there is no confirmed public report of model collapse observed in a real production training pipeline.** [Moderately strong: absence of evidence; vendors have no disclosure obligation]
11. **Capability measurement and pretraining returns are two different ledgers, and the existing independent indices can only measure the first.** Epoch's Capabilities Index bakes in reasoning, RL, post-training and test-time compute, with no pretraining dimension to separate. [Moderately strong: methodological self-statement]
12. **Published pretraining token counts do not form an extrapolable upward trend.** Within one generation, Llama 4 Maverick beats Scout using 22T against 40T. [Moderate: multi-source, but calibers differ across models]
13. **The prediction that reasoning-training compute growth is a one-time catch-up dividend remains unsettleable.** Epoch's May 2025 inference rests on a screenshot of an unlabelled livestream chart, and frontier labs have disclosed no comparable figures since. [Weak: the evidence base itself requires downgrading]

## Appendix: methodology and this run's self-corrections

Each of 44 load-bearing claim groups was assigned 3 independent verification agents, instructed to refute rather than confirm and to check primary sources word by word. Result: 2 groups survived unanimously intact, 42 carry caliber corrections, and 18 sub-claims were killed.

The article's own planned statements that verification overturned, listed:

1. **The planned structural finding "Ilya declared scaling over while buying 10× compute" was killed on two votes** as a false contradiction produced by deleting qualifiers. Replaced with "scale drift plus research claims that cannot be externally checked."
2. **"The irreducible term E was written into the formula in 2020" is false** — Kaplan's fits contain no E. Corrected to Henighan 2020 and Chinchilla 2022.
3. **"Orion is only 20% better than GPT-4" has no primary source** — a corruption of a training-progress figure.
4. **"Claude Opus 4.5 was first past 80%" does not hold** — Anthropic reported 80.2% six months earlier under a high-compute configuration.
5. **The ARC cost story "revised up from $4,560 to about $30,000" has the direction backwards** — $4,560 is the result of the final downward revision.
6. **"$2,767.05 for o1 versus $108.85 for GPT-4o" has no primary source** (killed on two votes) and is not used.
7. **Shumailov's hedged quotation is Nature's editorial standfirst**; the authors' abstract is stronger (causes / irreversible) — the correction runs opposite to the original assumption.
8. **ProRL is not a clean counterexample** — its own paper reports negative RL gains on tasks the base model handles well, and its starting point is an already-distilled checkpoint.
9. **"Every synthetic-data success is distillation from a stronger teacher" was overturned** — Nemotron states the teacher imposes no ceiling. Replaced with a layer-and-unmeasurability argument.
10. **"Pretraining scale rises with each generation" fails within a single generation** (Maverick 22T < Scout 40T).
11. **Kaplan's "some" was restored**, and the data dimension was verified across barely two orders of magnitude.
12. **Vinyals's "NeurIPS '25 talk" is a slip** for NeurIPS 2024 — precisely the talk where Ilya said pretraining as we know it will end.

No dual-seat audit was run this time: none of the 44 groups presented a case of a single source bearing a key conclusion of the article — the most important one (no evidence for the first wall) is itself absence of evidence, and has been labelled to that standard.

## Appendix: principal sources

**Theoretical lineage**: Kaplan et al. 2020 (https://arxiv.org/abs/2001.08361), Hoffmann et al. 2022 (https://arxiv.org/abs/2203.15556), Besiroglu et al. 2024 replication (https://arxiv.org/abs/2404.10102), Pearce & Song 2024 (https://arxiv.org/abs/2406.12907), Wei et al. 2022 (https://arxiv.org/abs/2206.07682), Schaeffer et al. 2023 (https://arxiv.org/abs/2304.15004), GPT-4 technical report (https://arxiv.org/abs/2303.08774)

**Data and synthesis**: Villalobos et al. (https://arxiv.org/abs/2211.04325), Muennighoff et al. 2023 (https://arxiv.org/abs/2305.16264), Shumailov et al. Nature 2024 (https://www.nature.com/articles/s41586-024-07566-y), Gerstgrasser et al. 2024 (https://arxiv.org/abs/2404.01413), phi-4 technical report (https://arxiv.org/abs/2412.08905), Longpre et al. *Consent in Crisis* (https://arxiv.org/abs/2407.14933)

**Reasoning axis**: OpenAI o1 (https://openai.com/index/learning-to-reason-with-llms/), DeepSeek-V3 (https://arxiv.org/abs/2412.19437), DeepSeek-R1 in Nature (https://www.nature.com/articles/s41586-025-09422-z), Meta ScaleRL (https://arxiv.org/abs/2510.13786), Yue et al. (https://arxiv.org/abs/2504.13837), NVIDIA ProRL (https://arxiv.org/abs/2505.24864)

**Independent measurement**: METR Time Horizon (https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/), METR TH1.1 (https://metr.org/blog/2026-1-29-time-horizon-1-1/), Epoch AI (https://epoch.ai/), ARC Prize (https://arcprize.org/), GSM1k (https://arxiv.org/abs/2405.00332), benchmark saturation study (https://arxiv.org/abs/2602.16763)

**Related research on this site**: the financing structure behind compute capex is covered in "AI Capex and 1999: What Rhymes and What Doesn't" (https://hub.cissychen.com/deep-research/ai-capex-1999-deep.en.html); power and hardware delivery constraints in "AI Hardware and Power: Where the Bottleneck Actually Is" (https://hub.cissychen.com/deep-research/ai-hardware-power-deep.en.html); benchmark contamination and LLM-judge caliber problems in "AI Code Review: Cure for the Verification Bottleneck, or Turtles All the Way Down?" (https://hub.cissychen.com/deep-research/ai-code-review-deep.en.html).
