# Bad Code Shipped — Can AI Help Find It? Big Outages Are Spotted in Minutes; the Hard Part Is the Hours After (Plain-Language Edition)

> This is the plain-language edition, written for people who don't run live online services. For the source of every number, the original quotes and the strength of the evidence, see the [deep dive](https://hub.cissychen.com/deep-research/release-detection-deep.en.html). All figures are as of October 2026.

## First, what "catching" it means: three steps

Software companies ship new code and change settings every day. The one change that goes wrong and breaks the service is called a "bad release." Before shipping there are tests, staging environments and code review, but something always slips through. Once it slips through, three steps have to happen before it counts as "caught":

- **Spotting it**: a person or a system realizes something is wrong.
- **Finding the cause**: confirming which change, and which part, caused the problem.
- **Stopping the damage**: pulling the change back or flipping a switch off, so the service recovers.

The "mean time to repair" the industry likes to quote blends these three steps into a single number. So when a company says "AI cut our repair time in half," you have no way of knowing which step got shorter. This article looks at the three steps separately.

## Where bad releases come from: where "70% of incidents come from changes" came from

This line comes from a 2016 Google book on running online services; the original gives no data source—it's a rule of thumb. Two years later Google published a set of real statistics: among the top eight categories of incident triggers, pushing new code accounted for 37% and pushing new settings for 31%. But these eight categories add up to exactly 100%, so 68% is just "the share within the top eight," not the share of all incidents.

Count a different way, and the numbers are far apart: among publicly reported incidents, upgrade and configuration problems together are about 15%; among Facebook's serious incidents over one three-month period, about 16% were related to configuration management; at one large bank, about 50%. All that can be said is the direction: **changes are one of the main sources of incidents**. And that unsourced "70%" is still being quoted word for word in academic papers ten years later.

## Who spots it first: machines, or people

A few Microsoft papers give the most detailed data, but each looks at a different scope, so they can't be compared side by side:

- Across all incidents at 306 services, 96.7% were first spotted by monitoring systems. But the small remainder reported by customers or engineers was spotted about 10 times more slowly. Among the fixes decided on after a miss, more than 40% were "there was no relevant monitoring at all."
- Among a year of serious incidents at Teams, about 55% were first spotted by monitoring, and 29% were reported by outside customers.
- Among incidents related to generative AI, 38.3% were first reported by people (including internal engineers), versus only 13.7% for ordinary services. The authors think the reason is that nearly half of these services were still in preview, and monitoring hadn't caught up.

The conclusion: **for serious incidents and for new kinds of services, the share spotted by people is not small, and that is exactly the part that gets spotted most slowly.** All of this is data from Microsoft alone; no other company has published similar statistics.

## Big public outages: spotted in minutes, stopped in hours

We checked, one by one, 9 official post-incident reports on big outages caused by changes, involving CrowdStrike, Google Cloud, Cloudflare, Fastly, Microsoft Azure and others. The timelines are strikingly consistent:

- **Spotting it is fast.** From the start of trouble to the first alert: 1 to 25 minutes, with a median of 3 to 5 minutes, mostly spotted first by automatic monitoring.
- **Finding the cause varies a lot.** The fast ones took 10 minutes; the slow ones, more than two hours. In Cloudflare's November 2025 outage, the team first thought it was under a massive network attack, and only later discovered that an automatically generated configuration file had gone wrong.
- **Stopping the damage is slow.** The median is about 1.8 to 3 hours, dozens of times slower than spotting it. The two that were stopped within half an hour both used a ready-made global off switch or simply pulled the change back.
- **Not one was stopped by "automatic rollback."** One Microsoft outage did have automatic rollback, but the version it was supposed to roll back to had already been overwritten by the bad settings.

But be careful: these are all the biggest, noisiest outages that got public write-ups. Bad releases quietly caught by automatic rollback don't get written up publicly; Slack, for one, says that after it introduced automatic rollback, the time customers were affected fell by 90%. In the other direction, this list contains no case of "customers spotted it first," but other public incidents do. So this table shows only one thing: **loud big failures get noticed very quickly, and then take hours to stop.** How long quiet small problems take to be noticed, it can't tell us.

## What gradual rollouts can't see

When big companies ship new code, they usually give it to a small slice of users first and widen it step by step if nothing goes wrong. This is called a "gradual rollout" or "canary release." It is the main way bad releases get caught, but it has several built-in blind spots:

- **Settings and data take the express lane.** At several companies, code rolls out slowly, but settings are pushed worldwide in seconds. Two big Cloudflare outages, the Google Cloud one and the CrowdStrike one all went wrong in settings, data or content files.
- **Bad code can "lie in wait."** Google Cloud's bad code looked fine during the gradual rollout because the faulty part was never actually run; it was set off 14 days later by one unusual setting. At Fastly it lay in wait for 27 days, at CrowdStrike about 5 months.
- **Problems that show up late.** In one Microsoft case, a settings change crashed only 5 minutes after being sent out, after it had already passed the health checks.
- **People went around the safeguards.** In another Microsoft case, the protection system had actually blocked it; a manual operation got around it.
- Others: a small trial can't produce problems that only appear under full load; rarely used features have no data to look at during the trial; and a slowdown that's tiny each time, too small to measure once, adds up to a big problem over a year.

Pre-release tests and gradual rollouts both test "situations we've seen before." What slips through is often **input that's perfectly valid but has never been seen before**, which happens to set off a piece of bad code that had been buried for a long time.

## Big companies' detection systems: mark the grades down

When people say "AI can catch bad releases," the most cited evidence is papers Microsoft and Meta published about their own systems. Checked against the originals:

- Microsoft's Gandalf claims "100% recall" (it catches everything), but what that actually means is "no serious incident was caused by a bad release"—smaller misses aren't counted at all. Another claim of 99.8% recall works out to about 95% using the paper's own numbers.
- Meta's FBDetect claims it can spot a 0.005% performance slowdown. That number really is impressive, but it measures performance metrics like CPU usage, not service failures; and it takes data from more than 500,000 servers to pull off. Among the reports developers confirmed, about 70% were real problems. "A false alarm only once every 13 years" was calculated by spreading the alarms across about 10,000 engineers.
- Google says its canary analysis system "likely prevented hundreds of postmortem-worthy outages," but also admits it can't be counted precisely.

We found no outside party that has re-tested these systems on real production data. What can be said: **big companies themselves report few misses, with accuracy between 70% and 95%, but there is no reliable number for "how much they missed."**

## Spotted, but not necessarily believed

Bad releases are rare, and that makes "false alarms" a serious problem. An arithmetic example: 1,000 releases a day, 1% of them bad, and a detection system that catches 95% of those. If it raises a false alarm on 2% of good releases, only about a third of its alarms are real; only when the false-alarm rate drops to 0.1% are nine in ten real.

With too many false alarms, people stop believing them. Several companies' papers contain stories like these:

- Meta's system caught two problems that later turned into incidents, but nobody dealt with either in time.
- Microsoft's system correctly halted a release; the team involved decided the alarm had nothing to do with that release, and the person in charge of the release had it overridden.
- Facebook engineers decided it "must be a false alarm," overrode the automatic block, and caused even more crashes.
- Google says that noisy detection gets switched off outright by operators.

**Spotting it is not the same as dealing with it.** Making machines spot things faster does not automatically make incidents end faster.

## Why lab scores run high

The anomaly-detection scores in academic papers rely on a few known ways of "padding the grade." The most typical one: if you happen to hit just one point in a stretch of abnormal data, you get credit for catching the whole stretch. Under this rule, on four commonly used datasets, completely random guessing beats seven deep-learning methods; remove the rule, and random guessing scores only about 0.1 to 0.2. In another commonly used test set, more than 80% of the problems can be solved with a one-line formula (the formula's settings were tuned problem by problem against the answers, but it still shows the problems are too easy). The latest large time-series AI models detect about as well as a single line of code.

So **high scores in papers cannot be taken as evidence that problems will be caught after going live.**

## Where AI is used now: finding the cause, not spotting the problem

The hottest product of 2025 to 2026 is the "AI operations engineer": having a large language model investigate incidents and find the cause. After reading each company's public descriptions, one thing is clear: **these products basically start investigating only after an alarm goes off, and some are started by hand; the AI is not responsible for spotting the problem in the first place.** A few vendors say they're working on "proactive detection," but haven't published any numbers.

At the finding-the-cause step, the commonly cited accuracy figures are all looser than they sound:

- Meta's 42% means the right answer appeared somewhere among the top 5 candidates the AI offered.
- Microsoft's 0.766 is about guessing "which category the problem belongs to" for one email service, not finding the specific cause.

Switch to independent tests that require a fully correct answer, and the scores drop to between 10% and 50%: on one public test, the best score in 2024 was about 11%; on another test that requires finding every cause, the leader in October 2026 is about 56%; 11 cutting-edge models averaged 76% under the loose standard of "find at least one broken service correctly," but only about 21% under the strict standard. The 35% that one model maker reported for itself appears only in a chart on its release page; independent research re-testing 2026 models the same way got only 4% to 13%. None of these tests has a score for human engineers to compare against.

Vendors' marketing numbers are even harder to judge: AWS says "94% root-cause accuracy," sourced to "feedback from preview customers," without saying how it was calculated. Grafana recorded a textbook case: a change passed staging, automated tests and code review, then broke the database after going live; an AI assistant found the cause in 8 minutes, 20 minutes ahead of the on-call team. This is the standard path of this article's question: **not caught before release, spotted after release, with AI helping find the cause faster.**

## What matters most

1. **For the big outages in public reports, "spotting it" is already fast—a median of a few minutes.** What's slow is finding the cause and stopping the damage, which takes hours.
2. **What really gets spotted slowly is the places with no monitoring, and the part customers notice first.** In Microsoft's data, this part is about 10 times slower.
3. **The most dangerous channel is settings and data.** Code rolls out slowly; settings are often pushed worldwide in seconds. Of the 9 big outages we checked, 5 happened on this kind of all-at-once channel.
4. **Big companies' detection-system grades are self-reported.** Accuracy is 70% to 95%; there's no reliable number for how much they miss, and nobody has re-tested them independently.
5. **Spotting it is not the same as dealing with it.** Once there are too many false alarms, people ignore or override the correct ones.
6. **AI operations products are used for "finding the cause," not for "spotting it."** Under strict standards they get it right 10% to 50% of the time, and vendors' numbers have no denominator.
7. When you see "AI cut repair time by X%," first ask three things: **Which step got shorter? When does the clock start? Compared with what?**

## How to test this article's judgments

- If a vendor publishes how often "AI spotted a bad release before the alarm did," along with its false-alarm rate, the judgment that "AI isn't responsible for spotting" will have to change.
- If, a year after Cloudflare and others launch their "put settings through gradual rollout too" overhauls, similar worldwide outages clearly drop, that confirms "the settings channel is the biggest blind spot."
- If a public test gets officially verified scores with human engineers for comparison, we'll be able to answer for the first time "how much better is AI than people at finding the cause."
- If companies other than Microsoft publish statistics on "who spotted the incident first," we can test "serious incidents and new services rely more on people to spot them."

## Appendix: where this article was overturned

Review changed the draft in many places. The most important ones:

- The draft said "Google found 68% of incidents come from pushes"—that's the share within the top eight triggers, not all incidents.
- The draft said "Microsoft's Gandalf has 99.8% recall"—using the paper's own numbers, it's about 95%.
- The draft said "Meta's system gives a false alarm only once in 13 years"—that's a figure spread across the number of engineers; among confirmed reports, about three in ten were false alarms.
- The draft said "of the big outages that were spotted fast, most took more than an hour to stop"—change when the clock starts and the conclusion changes, so it became "the median time to stop the damage is about 1.8 to 3 hours."
- The draft said "in public incidents, customers never spotted it first"—that holds only in the sample we chose; other incidents have such cases.
- The draft said "AI's cause-finding scores tripled in two years"—that high score was self-reported by a vendor; independent re-testing is far lower.
- The draft said "AI operations products are all triggered by alarms"—some are also started by hand.

**Nearly every number that made "spotting is already fast, AI is already accurate" look stronger got narrower once checked against the original.** Narrower where? Usually in the denominator: counting only misses that turned into big incidents, counting only reports that were confirmed, looking only at the noisiest failures.

For the full argument and sources, read the [deep dive](https://hub.cissychen.com/deep-research/release-detection-deep.en.html). Related plain-language editions on this site: ["Can AI Find Real Bugs? First Ask Who the Judge Is"](https://hub.cissychen.com/deep-research/machine-oracles-plain.en.html), ["The Better the AI, the Worse the Human? A Question Predicted 42 Years Ago"](https://hub.cissychen.com/deep-research/automation-irony-plain.en.html).
