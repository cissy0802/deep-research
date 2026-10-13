# Are AI Models Really Becoming Alike? The Leaderboards Say "Close Enough," the Hard Tests Say "Not Even Close" (Plain-Language Edition)

> This is the plain-language edition, written for people who don't follow model leaderboards. For the source of every number, the original quotes and the strength of the evidence, see the [deep dive](https://hub.cissychen.com/deep-research/capability-convergence-deep.en.html). All figures are as of October 12, 2026.

## First, what does "gap" mean

Two claims have both been popular over the past two years. One says: the top few AI models are crowding ever closer together, free open models are "only a few percentage points" behind the most expensive closed ones, and the US–China gap has "effectively closed" — so AI will end up an ordinary commodity anyone can use. The other says: on complex tasks that take hours of continuous work, the strongest models are pulling further ahead, and the winner takes all.

Both claims are about the "gap," but there are at least three ways to measure a gap:

- **Score gap**: on the same test, how many points apart two takers are.
- **Months behind**: how many more months the trailing side needs to reach where the leader is now.
- **Multiple**: for example, the leader can finish an 8-hour job on its own, while the follower can only manage 3 hours.

These three measures can give opposite answers. An example: if the length of work the strongest model can do doubles every four-plus months, then "4 months behind" equals "nearly 2 times apart." The faster the strongest model improves, the larger the multiple behind the same "4 months." So "followers have always been only about half a year behind" and "the gap is widening" can both be true at once.

## Why tests make everyone look the same

**When a test is close to maxed out, score gaps get squashed.** Picture a 100-point exam: two students with a real difference in ability score 50 and 70, a 20-point gap; with the same difference in ability, on a much easier exam, one scores 99 and the other 99.6 — a 0.6-point gap that looks like "the same." Their abilities didn't converge; the exam got too easy. Researchers noticed long ago that AI tests are being maxed out faster and faster: a test of graduate-level science questions took about 19 months to reach 80%; some later hard tests took only a year, some only 3 months.

**The widely cited "a few percentage points apart" is computed the wrong way.** Stanford's annual AI report says the gap between the No. 1 and No. 10 models on a leaderboard shrank from 11.9% to 5.4%. That percentage divides the "score gap" by "the score itself" — but scores on this kind of leaderboard can be shifted up or down as a whole at will, like switching temperature from Celsius to Fahrenheit, which changes every percentage. In actual points, 5.4% is roughly 70-odd points; and on this kind of leaderboard, a 49-point gap means the leader wins about 57% of head-to-head matchups.

**Both the test makers and the test takers are switching tests.** In February 2026, OpenAI announced it would stop reporting scores on a well-known coding test: it examined 138 problems its own model o3 did not consistently solve over 64 runs and found about 60% of them were flawed, and top models from every company could "recite" the reference answers to some problems. When Anthropic released a new model in September, it listed a new batch of tests; not one of the old tests everyone reported a few years ago appeared.

## Leaderboards: scores bunch up, but the ranking no longer tracks ability

**The most famous leaderboard is a public vote.** You ask a question, two anonymous models each answer, and you pick the better one. By this vote, the score gap between No. 1 and No. 10 fell from about 75 points at the end of 2024 to under 20 points in August 2026, then went back to about 31 points in October — the crowding is real, but it wasn't a straight line down. The leaderboard also changed its scoring method several times in this period, so comparisons across years only show the general direction.

**The news item "the open–closed gap widened to 29 points, the largest in nearly two years" is wrong in three places.** The 29 points come from the raw version of the leaderboard, without "style correction"; on the same day, the version the site showed by default had a gap of only about 18 to 21 points; earlier in 2026 the gap had been over 50 points; and the so-called "gap dropped to zero in January 2025" was in fact DeepSeek-R1, open-sourced that month, briefly pulling ahead. Only by picking the month when open models did best as the starting point can you tell a story of "widening."

**The leaderboard itself is biased, too.** One study (by authors from a company that competes on the board; the leaderboard operator is the party being criticized) found that some companies privately tested more than twenty versions before releasing a new model and published only the best one; big companies also received far more vote data than open models. By each side's own estimates, biases like these can inflate scores by about 10 to 50-odd points — roughly as large as the current gaps among the top models.

**The key finding: among the very top group, the public-vote ranking has almost nothing to do with the ranking by actual ability.** We compared the leaderboard against a capability index that combines dozens of tests: across all hundred-plus models, the two agree closely; but looking only at the 15 most capable, their rankings are almost uncorrelated. And for those same 15 models, cross-checked on other tests, the rankings still agree closely. For example, the capability index rates Anthropic's new model from September 2026 well ahead of its old model from February, yet the public vote (comparing the high-reasoning versions of both) can't tell the two apart.

This shows that at the very top, the public vote is no longer measuring "who is more capable." It may be that the questions ordinary users ask day to day are too easy to tell them apart; it may be that the vote was measuring something else all along, such as conversational style or speed; or it may be that the practice of choosing which versions go on the board has flattened the top — the existing data cannot tell which.

## Switch to hard tests nobody has maxed out, and the gap appears — but not always

**Same models, different test, and the gap can differ by an order of magnitude.** On the nearly maxed-out graduate science test, the best closed model scores 95.8% and the best open model 93.1%, just 2.7 points apart. On a test of research-level math problems, the best closed model reaches 97.6% and the best open model only 39%. On a test of obscure factual questions it is 75.6% versus 52.9%.

**On a new test, the gap often widens first, then gets pushed back down by the ceiling.** On one abstract-reasoning test, closed models surged ahead when it first came out and open models couldn't keep up, with the gap reaching about 60 to 70 points at one point; once closed models neared a perfect score, open models caught up and the gap shrank back to 4 points. So whenever you see "the gap is shrinking" on any test, first ask: how far is this test from a perfect score?

**But on tests that aren't maxed out, the gap can also be small.** On a software-engineering test with a standardized testing method, open models still trailed by 26 points at the end of June 2026; when Moonshot AI released Kimi K3 (open weights under a non-commercial licence) in mid-July, the gap shrank to 4 points within a day. On another coding test run with a uniform method, the best closed model scores 52% and the best open model 45%. Catching up sometimes isn't a gradual narrowing but a single release jumping ahead.

## Composite scores: the gap didn't shrink in 2026, but "doubled" is wrong

The research organization Epoch combines dozens of tests into a capability index. Its official estimate in May 2026 was: the best open models trail closed ones by about 4 months on average. Epoch itself cautions that this may understate the gap — open models tend to do worse on non-public tests, and closed companies don't necessarily release their strongest models.

Calculating it ourselves with October data: the best closed and best open models are about 10 points apart; the average gap across 2025 was about 6 points, and so far in 2026 it averages about 9. But this can't be stated as "the gap doubled," for three reasons: the 2025 gap itself bounced between 3 and 9 points, so the conclusion depends on which day you pick as the starting point; the index is recomputed as a whole every time new data is added, and recomputation alone can move the gap between the same pair of models by about 3 points; and another organization's composite index showed "the gap narrowing" between April 2025 and April 2026. Only one statement holds up: **the gap did not shrink in 2026.** And the extra gap comes mainly from the closed frontier running faster, not from open models slowing down.

## Long tasks: where it matters most, the ruler ran out first

**Why long tasks magnify the gap.** Take a job that requires 50 consecutive steps, where one wrong step ruins everything: a model with a 95% per-step success rate has only about an 8% chance of completing the whole thing; one with 99% has about 60%. A gap of just 4 percentage points per step becomes nearly 8 times on the whole job. Reality isn't this extreme — one analysis found that AI's error rate actually falls as it gets further into a task, so this calculation is on the pessimistic side — but the direction is right.

**The ruler built specifically to measure "how long a job it can do on its own" broke down in 2026.** The research organization METR sets a task's length by "how long a human expert would take," and looks at how long a job AI can finish with a 50% success rate. By May 2026, the strongest models had exceeded this ruler's range: METR itself states that measurements above 16 hours are unreliable, and the strongest model measured about 17 hours, with an error range of 8.5 to 55 hours. Worse is cheating: for internal models labs provided to METR, of the "successes" on tasks over 8 hours, at least 16% were the model exploiting a loophole. For another model, counting cheating as failure gives about 11 hours; counting it as success gives over 270 hours; METR itself says none of these numbers is a robust measurement. METR stopped updating this page in September, and the new version of the ruler has never measured any open model.

**What the old version of the ruler does show: open models' catch-up stalled at a bit over half a year in 2025.** When DeepSeek-R1 was released it trailed by only about 3-plus months, the closest it has come; the open models after it trailed by about 6 to 9 months. For 2026 open models, this ruler is blank.

**Getting it right once and getting it right four times show different gaps.** In a test simulating bank customer service, the model attempts each question 4 times: the share of questions Anthropic's model gets right on one try is 1.3 times the open model's, but the share it gets right "all 4 times" is about 1.8 to 2.4 times the open model's. In other words, the gap in "reliability" is larger than the gap in "capability." But this is just one test with fewer than 100 questions, and the top of this test's board happens to be Alibaba's Qwen 3.8 Max (a version based on an open-weight model); on some older question types, open models have already caught up or even pulled ahead.

## What companies say, and what others measure

China's DeepSeek says its new model from April 2026 is as strong as a US model released about 2 months earlier. The US government's evaluation body says it is only on par with US models from about 8 months earlier; calculating on Epoch's capability index also gives about 8 months, and other independent measurements range from 4 to 9 months. The gap shows up mainly on non-public tests that require hands-on work; on public knowledge and math questions they are nearly even, and on math it even beats Anthropic's February model. One independent researcher tallied 17 tests and found open models trail by about 8 to 10 months on non-public tests and about 4 to 6 months on public ones.

This looks a lot like "open models trained for the public tests," but there is no direct evidence — public tests being easier to max out, and closed companies possibly having seen some of the "non-public" questions, could also explain the same result. Note as well that this US evaluation body assesses Chinese models in line with the US government's AI policy; when it evaluated DeepSeek's previous model in 2025, the US Commerce Secretary framed it as "American AI dominates."

## Among the leaders: who is ahead depends on the test

Even looking only at the few US closed-model companies, the answer depends on what is being tested. On "how long it can work on its own," the gaps among them are about as large as the measurement error. On a new interactive abstract-reasoning test released in 2026, OpenAI's strongest model scores 62.7%, the Anthropic model that was tested 30.2%, a Google model 10.4%, and xAI under 2%. On a test of "rewriting a piece of software exactly as it is," Anthropic leads; in a test simulating running a vending machine business for a year, OpenAI leads.

On the composite capability index, in September 2025 five companies were within 6 points of the top; by September 2026 only Anthropic and OpenAI remained — though Google's new model, released at the end of September, has not yet been scored, so this conclusion may change.

## Tens of times the compute, months of difference in ability

The compute used to train OpenAI's GPT-6 Astra is estimated at about 50 times that of Kimi K3, the largest open model released in 2026 (the K3 figure is speculative). Roughly, with frontier compute growing 5 times a year, that equals a gap of over two years — yet actual ability differs by only a few months. Meta and xAI both have first-tier compute, yet their ability sits in the same tier as Chinese open models. **Compute is a threshold, not a guarantee.**

The ways to catch up are real: algorithms are improving, and by an estimate for 2012–2023 the compute needed to reach a given level halves about every 8 months; latecomers may be able to skip the detours their predecessors had to explore (evidence for this is still thin); and they can train on the answers of strong models (this is called "distillation"). Anthropic accuses three Chinese companies of conducting more than 16 million conversations with its models through about 24,000 fake accounts in order to distill them — a one-sided accusation, in which the largest share was MiniMax (over 13 million), with DeepSeek accounting for less than 1%. But these methods work least well on the hardest long tasks; DeepSeek itself has written that going beyond the current level may still require a stronger base and larger-scale training.

**On price, AI at a given level gets about 13 times cheaper each year, yet getting work done with the strongest models keeps getting more expensive.** So what becomes an "ordinary commodity" is really yesterday's best; today's best always stays some distance ahead.

## What matters most

**"AI is becoming alike" is mainly an artifact of the rulers.** Nearly maxed-out tests squash the gap; the public-vote leaderboard no longer tracks actual ability at the very top; and the widely cited "a few percentage points apart" is computed the wrong way.

**Switch to hard tests that aren't maxed out, and the gap is still there; it did not shrink in 2026.** But "doubled" is wrong, and some hard tests get caught up with in a single release.

**Open models have consistently trailed by a few months, not trending toward zero.** Independent measurements mostly fall between 3 and 9 months; the catch-up speed companies report themselves — at least in DeepSeek's case — is much faster than what others measure.

**"Long tasks," the thing most worth watching, happen to be exactly what can no longer be measured.** "Winner takes all on long tasks" can currently be neither confirmed nor refuted.

**The gap in "reliability" is larger than the gap in "capability"** — but the evidence is still thin, and there are counterexamples.

**Among the top few companies, who is ahead depends on the test; the number of companies that can stay right behind the frontier is shrinking (tentative).**

**Tens of times the compute, only months of difference in ability.** What gets cheap and ordinary is yesterday's best; this bears on whether model makers can still make money.

## How to test this article's judgments

Ordered from most to least confident:

1. **There is currently no independent ruler that can measure both the strongest closed and open models of 2026 on long tasks.** How to overturn it: an organization launches a new test that can reliably measure tasks over 16 hours and has measured open models.
2. **For the same models, open models reach over 94% of closed models on nearly maxed-out tests, and fall far short on the hardest tests** (only 55% on a hard engineering test; 39% versus over 90% on a research-level math test). How to overturn it: open models reach over 90% on some newly released hard test within half a year.
3. **The catch-up speed companies report themselves is faster than independent measurements.** DeepSeek's self-reported comparison models were released only about 2 months before it; independent measurements say it trails by 4 to 9 months. How to overturn it: see whether self-reports and independent measurements match after the next major open model release.
4. **The number of months open models trail stayed steady at about 3 to 9 months in 2025–2026, not trending toward zero.** How to overturn it: some open model ties the strongest closed model on the composite capability index and holds it for more than a month.
5. **The length of work that can be done with "80% confidence" has stayed roughly at one-quarter to one-sixth of the length at "50% confidence," neither catching up nor falling further behind.** How to overturn it: see how this ratio changes in new tests.
6. **Among the very top group, the public-vote ranking and the ranking by actual ability are almost uncorrelated.** How to overturn it: recompute with data from the coming months and see whether the two become clearly correlated again.
7. **Tens of times the compute, only months of difference in ability; Meta and xAI, with first-tier compute, are not at the front in ability.** How to overturn it: Meta's or xAI's next model enters the front tier.
8. **On the composite capability index, the open–closed gap did not shrink in 2026, and the increase comes mainly from closed models running faster.** Confidence in this one is moderate: another organization's index gave the opposite reading for the same period. How to overturn it: look at Epoch's next recomputation and the other organization's numbers within a single version.
9. **The gap in "getting it right every time" is larger than the gap in "getting it right once."** Confidence in this one is weak: only one test, fewer than 100 questions. How to overturn it: in more tests of this kind, the two gaps turn out to be about the same size.
10. **The number of US companies that can stay right behind the frontier went from 5 to 2.** This one is tentative: Google's new model has not yet been scored. How to overturn it: Google's new model gets its score and enters the front tier.

**What to watch.** If any of four things happens, this article's judgments should be revised:

First, **a new ruler appears that can reliably measure long tasks and has measured open models** — only then can we really answer "is it winner-takes-all on long tasks."

Second, **some open model catches up to within the error range of closed models on non-public tests too** — that would overturn "public tests overstate the catch-up speed."

Third, **the number of companies right behind the frontier rises again** — showing that the thinning at the top was just staggered release timing.

Fourth, **the public vote and actual ability line up again at the very top** — showing that this decoupling was only temporary.

## Appendix: where this article was overturned

Review changed the original draft in many places. The most important:

- The original draft said "the open–closed gap doubled in 2026" — the conclusion depends on which day you pick as the starting point, index recomputation alone moves the gap by about 3 points, and another index gave the opposite reading. Changed to "did not shrink."
- The original draft said "on METR's ruler, open models are falling further and further behind" — the starting point, R1, happened to be open models' best showing, and looking back to 2024 they trailed by more. Changed to "the closing-in that R1 brought did not continue."
- The original draft said "at the top, the leaderboard can no longer tell who is stronger" — in fact it can still spread the models out; it just isn't ranking ability.
- The original draft said "open models gamed the public tests" — the pattern fits, but there is no direct evidence; it can only count as a conjecture.
- The original draft said "Moonshot AI's Kimi K3 topped the web-programming leaderboard" — the two error ranges overlap, so it only counts as a tie, and it was overtaken a day or two later.
- The original draft said "on a computer-use test, open models are nearly 7 times behind" — the two sides used different tool setups; under the same conditions it is about 3 to 4 times.
- The original draft said "the top of the bank customer-service test is Alibaba's closed model" — it is a version based on an open-weight model and can't simply be counted as closed.

**Nearly every number that made "becoming alike" or "pulling apart" look more dramatic became somewhat milder once sent back to the original data.** The conclusion that remains is less easy to tell: the gap vanishes on maxed-out rulers, holds at a few months on rulers that aren't maxed out, and the one ruler that could best settle the question has just run out.

For the full argument and sources, read the [deep dive](https://hub.cissychen.com/deep-research/capability-convergence-deep.en.html). Related plain-language editions on this site: ["Who Ends Up With the Money AI Makes? Are Model Makers Just Sewing Someone Else's Wedding Dress?"](https://hub.cissychen.com/deep-research/ai-profit-pools-plain.en.html), ["'Has AI Hit a Wall?' — Two Years of Arguing, and Neither Side Produced a Measurement"](https://hub.cissychen.com/deep-research/scaling-wall-plain.en.html).
