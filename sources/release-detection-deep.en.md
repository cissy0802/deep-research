# Can AI Catch Bad Releases? What Offline Checks Miss, and How Fast It Gets Found in Production (Deep Dive)

> Methodology note: This issue was split into 5 research lines (incident sources, progressive delivery and canaries, production regression detection, LLM root-cause analysis, public incident postmortems), collecting 140 claims. From these, 15 sets of load-bearing claims were drawn, and each set was assigned 3 independent verification agents, through three lenses—verbatim, counter-evidence and definitions—instructed to try hard to refute; every quotation was substring-matched against the primary original, and every derived number was recomputed. Of the 45 votes, 44 ruled "needs correction," 1 ruled "holds as written," and 0 ruled "overturned"; at the sub-claim level there were 396 rulings in total: 234 "holds as written," 162 "needs correction," 0 "overturned." "0 overturned" is itself a warning sign, so for 3 pieces of empirical evidence where a single source carries a key conclusion, an additional counter-evidence search seat and a methodology audit seat were added (6 audits in total): all 3 were downgraded, and 4 numbers among them were rejected and barred from carrying weight (Gandalf control-plane recall 99.8%, Gandalf data-plane recall 100%, FBDetect's "one false positive every 13 years," and Walmart's MTTD reduction). Because of token costs, this issue is one size smaller than a standard run: 5 research lines, 15 sets of load-bearing claims. Data as of October 2026. Every number in the text is followed by an evidence grade: Multi-source confirmed / Single-source verified / Direction contested / Vendor-reported / Unverified.

## 0. First, Split an Incident into Three Segments

The phrase "AI can catch bad releases" hides three different things. After a bad release goes live, three stretches of time must pass before it counts as "caught":

- **Detection (TTD)**: from the start of impact (or from when the change takes effect) until a person or a system realizes something is wrong.
- **Localization (RCA)**: from realizing something is wrong to confirming which change and which component.
- **Mitigation**: from confirming the cause to the impact stopping (rollback, flipping a switch, swapping back the old file).

The industry's most common metric, MTTR, blends these three segments into one number. In 2023 DORA renamed MTTR "failed deployment recovery time," counting only failures caused by software changes, but it still measures the whole recovery, not detection. 【Single-source verified】 Meta's automated troubleshooting platform DrP reports "an average 20% improvement in MTTR," and its MTTR is defined as "resolution timestamp minus detection timestamp"—which by construction excludes the detection segment. 【Single-source verified】 So wherever this piece mentions "reducing MTTR by X%," it cannot be read as "bad releases were found faster."

Even looking at just one number, the mean is fragile. Google SRE Štěpán Davidovič ran a Monte Carlo on incident data from three companies: assuming a tool genuinely shortens every incident by 10%, the before-and-after MTTR difference still has a 20%–40% probability of being negative; conversely, doing nothing at all still has a 10%–23% probability of showing an "improvement" of more than 30 minutes. 【Single-source verified】 The VOID report argues that incident durations are positively skewed and that reliability should not be measured by a single mean. 【Vendor-reported: Verica was a chaos engineering vendor at the time】 John Allspaw goes further: incidents have no objective start or end time in the first place. 【Single-source verified: practitioner's view】 This means the starting point of TTD is itself constructed after the fact; any "down from X minutes to Y minutes" must first ask how the starting point was defined.

The eight sections below unfold along these three segments, followed by a verdict.

## 1. Where Bad Releases Come From: An Archaeology of "70%"

"About 70% of incidents come from changes" is the most cited number in this field. It comes from the "Change Management" passage of Chapter 1 of the Google SRE book (2016); the original gives no numerator, denominator or time window, and no data source—it is an assertion from experience. The same chapter also counts a "new type of user traffic" as a change, so the book's "change" is far broader than code or configuration pushes. 【Single-source verified】

The closest thing to traceable data is Appendix C of the SRE Workbook two years later: sampling from thousands of postmortems from 2010–2017 and tallying the top eight categories of outage triggers, binary push accounts for 37% and configuration push for 31%, 68% combined. But these eight categories add up to exactly 100%—**68% is the share within the top eight trigger categories, not the share of all outages**; the true share is ≤68%, exact value unknown. Moreover, it counts triggers, not root causes; the sample includes only incidents that had a postmortem written. 【Single-source verified: Google internal data】

Switch rulers, and the numbers diverge widely:

- Public-reporting basis: Gunawi et al. (SoCC'16) analyzed 597 unplanned outages at 32 internet services from 2009–2015, 59.5% with unknown root cause; converted to a share of all incidents, upgrades account for about 9%, and upgrades plus configuration about 15%. 【Single-source verified】
- Facebook: Tang et al. (SOSP'15) manually analyzed high-impact incidents in a certain three-month window; 16% were related to configuration management. 【Single-source verified: the company's own data】
- A large commercial bank: the SCWarn paper (ESEC/FSE'21, authors include an AIOps vendor) states that about 50.4% of incidents were caused by bad changes; denominator and window not disclosed. 【Single-source verified: abstract level only】

These numbers have mutually different denominators; they cannot be merged into one range and can only be listed separately. What holds up is the direction: **changes are one of the main triggers of incidents**. 【Multi-source confirmed: direction】 And that 70% is still being quoted verbatim ten years later—the ICSE-SEIP 2026 paper by ING and TU Delft writes "about 70% according to Google" in its introduction, and elsewhere in the body it has already drifted to "up to 70%." 【Single-source verified】

Also remember Richard Cook's warning: incidents require multiple factors, each insufficient on its own, acting together; attributing them after the fact to a single "root cause" is itself wrong. 【Single-source verified: argumentative classic】 "X% come from changes" is a statistic that compresses multi-factor incidents into a single trigger label.

## 2. Who Finds It First: Monitoring, or People

If bad releases are mostly caught by automated monitoring within minutes, then "can AI catch them" is mainly a localization question; if a substantial share relies on customer reports, detection itself is the gap. The answer the data gives depends on which layer you look at:

- **Microsoft, 306 services, all incidents in 2022 (any severity)**: 96.7% were detected by monitoring. But among the 3.3% reported by customers or engineers, the average detection time for customer-reported incidents was about 10.7 times that of monitor-reported ones (engineer-reported about 9.96 times), and mitigation about 3.75 times. Among the repair items for missed detections, more than 40% were "no relevant monitoring at all," and 30% were faulty monitoring logic or missing signals. 【Single-source verified: Ganatra et al. ESEC/FSE'23; 10.7× and 3.75× verified against the original by only one seat】
- **Microsoft Teams, 152 Sev 0–2 incidents over one year**: about 55% were detected by automated watchdogs; 29% were reported by external users or customers, 10% found by internal Microsoft partner teams, 6% found by the service team itself. About 17% of incidents lacked monitoring or telemetry. 【Single-source verified: Ghosh et al. SoCC'22, single service, about 35% of incidents without complete postmortems filtered out】
- **Microsoft GenAI-related incidents (2020-06 to 2024-02)**: 38.3% were reported by people (engineers or customers), versus 13.7% for comparison services; among monitor-reported incidents, those later labeled False Alarm were 11.0% for GenAI and 3.8% for the comparison group. The authors attribute this to nearly half of GenAI services being in development or preview, with monitoring carried over from old frameworks. 【Single-source verified: non-peer-reviewed preprint; downgraded in Round 3—no confidence intervals, preview-stage confounding not stratified, no detection latency data】

These three numbers **cannot be lined up as a trend**: their denominators are all severities, high severity, and GenAI keyword identification (severity not stated, inferred to be mixed) respectively. Another Microsoft preprint states that of 156 Sev2/2.5 incidents at an LLM inference service in April–June 2025, about 74% were alerted by health probes or the DRI pipeline before customer reports 【Single-source verified】, but it differs from the 38.3% in time, scope and definition, and both come from the same incident database—not an independent replication. Note also that "reported by people" includes internal engineers and is not the same as "users found it first."

What can be said: **on high-severity incidents and new types of services, the share found by people is not small, and the part found by people falls precisely in the slowest tail of detection.** 【Single-source verified: all Microsoft data】 Outside Microsoft, we found no quantified share of "who detected the incident." The only independent evidence is qualitative cases, for example Anthropic's 2025-09 postmortem: the quality degradation was first perceived by users, and offline evaluation did not catch it. 【Single-source verified: qualitative case】

## 3. The Clocks in Public Postmortems: Detection in Minutes, Mitigation in Hours

Public postmortems are the only material in which the complete timeline is visible. We checked 11 official postmortems case by case, excluding two not caused by releases (AWS 2025-10 was a latent race condition in an automation system, Meta 2021 was an operational command), leaving 9 cases:

| Case | Trigger | Progressive delivery? | Impact→detection | Detection source | Main mitigation |
|---|---|---|---|---|---|
| CrowdStrike 2024-07 | Content file | No (this content channel was not staged) | Not disclosed | Not disclosed | Release→manual revert 78 minutes (not TTD) |
| Google Cloud 2025-06 | Latent code + policy data | Code released region by region, but the failing path was never executed; policy data replicated globally within seconds | ≤2 minutes (SRE began triage, proxy) | Not disclosed | 40 minutes–3 hours (depending on basis) |
| Cloudflare 2019-07 | WAF rule | No | 3 minutes | Automated (external synthetic tests) | 27 minutes |
| Fastly 2021-06 | Latent code + legitimate customer configuration | Not disclosed | 1 minute | Automated | 49 minutes–2h48m (depending on basis) |
| Azure Front Door 2025-10-09 | Manual cleanup bypassed protection system | Protection existed, bypassed manually | 23 minutes | Automated (telemetry) | 5h00m–8h10m (depending on basis) |
| Azure Front Door 2025-10-29 | Customer configuration + latent data-plane bug | Yes, multi-stage + health gating, still penetrated | 2 or 7 minutes | Automated | 2h49m–8h24m (depending on basis) |
| Cloudflare 2025-11-18 | Database permission change → feature file | Feature file generated every 5 minutes and rapidly propagated network-wide | 3–11 minutes | Automated (automated tests) | About 3 hours |
| Cloudflare 2025-12-05 | Global configuration | No | 3 minutes | Automated | 25 minutes |
| Cloudflare 2026-02-20 | Code | Applied gradually | ≤17–25 minutes (proxy upper bound) | Not stated explicitly | About 5 hours |

【Vendor-reported: each case is the primary original text of the official postmortem; for Cloudflare 2025-11-18 and 2026-02-20, the start of impact is written inconsistently between the body text and the table of each postmortem, so both values are listed】

The locked-in findings from this:

- **Detection is on the scale of minutes.** For the 8 computable cases, from the start of impact to the first detection signal, the range is 1–25 minutes, median 3–5 minutes (depending on two self-contradictory starting points in the originals); measured from the moment of the change, the median is about 8–13 minutes. 【Vendor-reported; downgraded in Round 3】
- **Mitigation is on the scale of hours.** The median of main mitigation is about 1.8–3 hours, tens of times longer than detection. Only two cases definitely stopped the bleeding within 1 hour (two more depend on the basis), and both used a ready-made global switch or a direct revert. 【Multi-source confirmed in direction; the specific multiple is Vendor-reported】
- **Localization varies the most.** Google 10 minutes, Cloudflare 2019 18 minutes, Azure Front Door 10-29 34 minutes, Fastly 40 minutes, while Cloudflare 2025-11-18 took about 2 hours—the team first thought it was a hyperscale DDoS; good and bad feature files were generated alternately, and the system repeatedly cycled "recover—fail." 【Single-source verified】
- **Not one case stopped the damage mainly through automatic rollback.** Azure Front Door 10-29 automatically froze propagation, but the rollback baseline (last known good) had already been contaminated by the bad configuration, so it could only be rewritten manually. 【Single-source verified: within sample】

The last point is the easiest to misread. Both Round 3 auditors pointed out that this sample was **selected by outcome**: all are loud global failures, with Cloudflare accounting for four cases. Bad releases caught by automatic rollback do not get written up as big public postmortems. Slack states that after introducing automatic rollback in April 2024, customer-impact hours fell by 90% (a before-and-after comparison of 2024-02 to 2025-01, with no causal design); Cloudflare states that its binary releases can roll back automatically without human intervention. 【Vendor-reported: no rollback counts or false-rollback counts】 Bias in the opposite direction exists too: no case in the sample says in its original text that "customers found it first" (6 cases are explicitly automated signals, 3 not disclosed), but in Atlassian's 2022-04 incident, the first signal was a customer ticket; in Section 2, 29% of Teams Sev≤2 incidents were reported by external customers, and 38.3% of GenAI service incidents were reported by people. 【In-sample count Single-source verified; as a general conclusion Direction contested】

So the question this table can answer is narrow: **loud big failures are seen within minutes, and then take hours to stop.** It cannot answer how long quiet regressions take to be found. The incidents in Section 2 reported by customers, with detection about 10 times slower, are almost invisible in this kind of public postmortem.

## 4. What Canaries Can't See

Progressive delivery and canaries are the main mechanism for "post-release detection." Google puts it bluntly: even if the release pipeline is fully automated, it is impossible to detect all release-related defects before real traffic hits the service; a canary is essentially an A/B test. 【Single-source verified】 The question is what this A/B test cannot see.

**The first structural gap: configuration and data travel through a different, faster channel.** Primary materials from at least four vendors show an asymmetry between the release cadence of code and that of configuration/data:

- Cloudflare states that its binaries have a gate of "employee traffic → free users → gradual expansion, with automatic rollback on detected anomalies," but configuration changes such as newly created DNS records and security rules reach about 90% of servers within seconds via Quicksilver, without passing through the gate; both the 2025-11-18 and 2025-12-05 incidents occurred on this side. 【Single-source verified】
- Google Cloud 2025-06: code was released region by region, but the policy data that triggered the failure was "replicated globally within seconds." 【Single-source verified】
- CrowdStrike: one of the findings of the official RCA is that "each Template Instance should be deployed in a staged rollout," implying that this content channel was not staged at the time. 【Single-source verified】
- Microsoft Azure Front Door: service code takes about 2–3 weeks, while customer configuration reaches the globe in about 5–10 minutes per "industry expectations"—both incidents occurred in the customer-configuration category. 【Unverified: one seat could not re-check the original; the direction is supported by remediation items】

Of the 9 cases, 5 involved configuration/data/content channels that were global or unstaged by design, and 1 involved manually bypassing a protection gate. 【Multi-source confirmed in direction; 5/9 is Vendor-reported】 The fastest category of change is exactly the canary's blind spot.

**But going through progressive delivery doesn't prevent incidents either.** Three verified ways of penetrating it:

1. **The failing path needs another change to trigger it.** Google Cloud's bad code was "never executed" during the region-by-region rollout, and was triggered 14 days later by a policy with an empty field. 【Single-source verified】
2. **Asynchronous, delayed onset.** Azure Front Door 10-29's configuration crashed asynchronously about 5 minutes after being delivered, having already passed health gating; the configuration was pushed globally, and even the rollback baseline was updated to the bad one. 【Single-source verified】
3. **A human overrode the automated judgment.** Azure Front Door 10-09's protection system initially blocked it; a manual cleanup operation bypassed it. 【Single-source verified】

Taking all vendors' materials together, the canary's structural blind spots can be grouped into six categories (this is this study's synthesized classification, not one given by any single source; each category has only individual cases, no proportions):

| Blind spot | Mechanism | Primary example |
|---|---|---|
| Insufficient scale or load | The canary is small or in off-peak hours, and cannot surface problems that appear only at full volume | Facebook: a configuration routed mobile requests to a rare path and overwhelmed storage; a small-scale canary did not expose it, and a cluster-level stage of thousands of machines was added afterward |
| Latency / time delay | The problem appears after the observation window ends | Microsoft: NIC firmware conflicting with a driver, OS crash only 24–72 hours after deployment (this case was ultimately detected by Gandalf at the Canary stage) |
| Unexecuted paths and unstaged data changes | The canary only validates paths that traffic actually reaches | Google Cloud 2025-06 |
| Cross-component interaction | The change itself is correct but triggers a bug elsewhere | Facebook: a legitimate configuration triggered a race-condition bug on a new code path, accounting for 22% of its configuration-related high-impact incidents (three-month window, verified by only one seat) |
| Low-traffic paths / missing data | Low-frequency paths have too few samples or no data, and the statistical judgment lets them through | Spinnaker/Kayenta by default judge metrics with no data during the canary as Nodata, with no penalty |
| Cumulative regression below the single-run MDE | Each one is below the minimum detectable effect, accumulating into a big problem | Hypothetical example: +0.05% CPU each time, 100 times a week, +260% in a year |

【Each example Single-source verified; the low-traffic blind-spot mechanism in the fifth category is an inference; the sixth category is a hypothetical example, and "a single canary can't see it" is an Unverified inference】

What offline validation misses also has something in common: **legitimate but never-before-seen input shapes, triggering latent code paths.** Google Cloud's empty-field policy, Fastly's legitimate customer configuration, CrowdStrike's 21st field using a non-wildcard match for the first time (the Content Validator approved it based on 21 inputs, while the interpreter supplied only 20 values). How long the bad code lay dormant in production before being triggered: Google Cloud 14 days, Fastly 27 days, and CrowdStrike's template type about 5 months. 【Single-source verified: case by case】 Tests and canaries both test "inputs that have already been seen."

## 5. Big-Tech Detectors' Report Cards

The affirmative evidence for "AI can catch bad releases" comes almost entirely from big companies' papers on their own systems. Sent back to the originals, the numbers are all narrower than the versions in circulation.

**Microsoft Gandalf (NSDI 2020, Azure's release safety analysis service).**
- Data plane: in a 2018 window it "caught 155 critical failures," with precision reported as 92.4%. This ratio cannot be recomputed from 155; neither the total number of alerts nor the number of false positives is disclosed, so it can only be written as "about 92%, denominator not disclosed." The paper's operational definition of "recall 100%" is "no Sev0–2 incident was caused by a bad release"—only misses that turned into high-severity incidents were counted. 【Rejected in Round 3: proxy ground truth, barred from carrying weight】
- Control plane: more than 1,200 region-level deployments, 39 incidents filed, 2 false positives, 2 misses. By standard definitions, precision and recall are both 37/39 ≈ 94.9% (Wilson 95% interval about 83%–99%). The paper's reported "recall 99.8%" cannot be obtained from the standard definition; numerically it matches all three of "1 − misses/all deployments," specificity and NPV, so the denominator cannot be determined. 【99.8% rejected in Round 3; 94.9% is Single-source verified, vendor self-assessment】
- "Decisions in about 5 minutes" is the streaming layer's data processing plus decision latency, not the time from a bad release taking effect to its detection. The paper reports no TTD distribution; in its cases, failure signals could appear 24–72 hours after release. 【Single-source verified】
- The paper's conclusion says it "blocked 99.2% of bad rollouts," but in the body the denominator of this ratio is "rollouts judged suspicious" (including false positives)—a ratio conditional on detection. 【Single-source verified: the conclusion's phrasing must not be cited】

**Meta FBDetect (SOSP 2024, production performance regression detection).**
- "Can detect 0.005% regressions": 0.005% is a threshold on a subroutine's absolute share of CPU across the whole service; the target is performance regressions, not correctness failures; it depends on a sample size of more than 500,000 servers. The median of regressions actually detected is about 0.04%. 【Single-source verified】
- It is periodic batch processing: the small-regression tier runs every 2 hours, with an analysis window of 4 hours. The smaller the threshold, the longer the wait. No TTD distribution was found in the paper. 【Single-source verified】
- In one month, FrontFaaS raw detection produced 3.96 million change points; after filtering, short-term detection was left with about 210. 【Single-source verified】 **In Meta's performance time-series setting, anomaly detection without heavy engineered filtering is almost all noise.**
- In one month 217 regressions were reported; of the 70 explicitly confirmed by developers, 49 were true and 21 false, precision ≈ 70% (95% interval about 58%–80%); the confirmation rate was only 32%, with selection bias. "One false positive only every 13 years" is the result of spreading across about 10,000 developers. 【70% Single-source verified; "13 years" rejected in Round 3】
- The miss evaluation used 4 performance incidents in 2023 as ground truth: 2 were detected but developers did not act in time, 1 was a metric not exported to FBDetect, and 1 was unrelated to changes. 【Single-source verified: n=4】

**Google Canary Analysis Service (CAS).** It "evaluates" hundreds of thousands of production changes every day—that is a count of evaluations, not of blocks. Google states plainly that precise impact analysis is hard: if CAS really prevented an outage, there is no way to know how big that outage would have been; the team considered deliberately letting a portion of failing verdicts through for an A/B test, but ultimately gave up. The paper offers only a rough estimate: CAS "likely prevented hundreds of postmortem-worthy outages." 【Vendor-reported: no denominator, no method】

**Other companies.** The numbers other companies made public in 2024–2025 are all outcome metrics without denominators: Slack's "90% drop in customer-impact hours" and Atoms' (formerly CloudKitchens) "blocked more than 1,100 bad releases in one quarter" have no total release count, false-rollback count or detection rate. 【Vendor-reported】 Walmart's "MTTD reduced by more than 7 minutes" comes from a general anomaly detection platform; the denominator of its 63% coverage is only 58 incidents from 4 case-study customers, with no MTTD baseline. 【Rejected in Round 3 as evidence of release detection】

The Round 3 counter-evidence seat concluded: **we found no third party that has re-tested Gandalf, FBDetect, Kayenta or CAS on production data.** The only external comparison comes from a preprint by a competitor's authors, which ran Gandalf as a baseline on someone else's data and got an average F1 of about 0.87, with experimental details missing. 【"No independent production re-test" is Multi-source confirmed; the external F1 is Unverified】 The industry has also never published a survey of block rates with denominators, false-rollback rates, or automatic-rollback adoption rates.

The claim that holds up: **big companies self-report few misses and moderate precision (about 70%–95%), but "recall" is always a proxy or an assumption, and detection is not the same as blocking.**

## 6. Low Base Rates: Detected, but Not Necessarily Believed

Why does a detector with 70% precision count as a good result in production? Because bad releases themselves are rare. An illustration of our own calculation (hypothetical, not measured): 1,000 releases a day, 1% bad, and the detector catches 95% of them.

- At a per-release false-positive rate of 2%, there are about 9.5 true alerts and 19.8 false alerts per day, alert precision about 32%;
- at a false-positive rate of 0.5%, precision about 66%;
- at a false-positive rate of 0.1%, precision about 91%.
- If each release simultaneously watches 100 metrics, each with a 0.1% false-positive rate, and the metrics are independent, the probability of at least one false positive per release is about 9.5% (it would be lower if the metrics are correlated, so this is an upper-bound-style illustration).

【Own calculation, recomputed by three seats without error; the direction is matched by primary materials from Meta and Google】 When the base rate is low, the false-positive rate determines whether alerts can be trusted. For performance regressions, the real base rate may be even lower—Meta's pre-release replay testing, ServiceLab, reported regressions on only 0.3% of tested changes, and in A/A experiments the false-positive rates for p90 and p99 metrics were 40% and 64% respectively. 【Single-source verified: verified against the original by only one seat】

The cost of false positives is not reading a few more alerts but the erosion of response. Primary materials contain four kinds of cases pointing the same way:

- Neither of the 2 incidents FBDetect detected was handled in time. 【Single-source verified】
- Gandalf gave a correct no-go; the team judged from experience that it was unrelated, and the release manager requested a bypass; advancing to the next stage produced another no-go, and only deeper investigation confirmed a regression, by which time customers had already reported it. 【Single-source verified: n=1】
- Facebook: a canary rejected a configuration change because of instance crashes; engineers concluded it "must be a canary false positive" and overrode it, which caused more crashes. 【Single-source verified】
- Google: CAS has had incidents where users ignored canary failures and pushed bad versions; on the other side, if users repeatedly retry a genuinely dangerous push, CAS's adaptive learning will eventually treat it as normal and stop alerting. 【Single-source verified: qualitative】 The Google SRE Workbook also notes that noisy canaries get disabled or ignored by operators. 【Vendor-reported: guidance argument】

**Detection is not the same as response.** 【Multi-source confirmed in direction: individual cases from four vendors, with no public statistics on human override rates】 Shortening TTD does not automatically shorten impact; the handoff between humans and machines is a bottleneck in its own right. This is consistent with the conclusion of this site's "The Ironies of Automation": the more reliable automation becomes, the harder it is for people, in the few critical moments, to judge whether it is right this time.

## 7. Why Offline Evaluations Are Systematically Inflated

If detection results on big companies' production data all need to be discounted, results on academic benchmarks need it even more. Time-series anomaly detection (the main method behind KPI alerts) has three known score-inflating mechanisms in evaluation:

- **Point-adjust (PA).** Most papers stipulate that hitting a single point within an anomalous segment counts as hitting the whole segment. Kim et al. (AAAI-22) found that on four datasets—SWaT, WADI, MSL, SMAP—uniformly random scores achieve an F1 of 0.93–0.97 under PA, higher than the 7 deep methods in the table; without PA, the random scores' F1 is only 0.11–0.23. All scores also use the post-hoc optimal threshold. 【Single-source verified; the direction has been widely accepted by subsequent work, no rebuttal found】
- **The benchmarks themselves.** Wu and Keogh (TKDE) found that 316 of the 367 series (86.1%) in the Yahoo benchmark can be solved by a one-line expression—the expression's parameters were searched series by series with the help of labels, but that precisely shows these problems are too easy. The authors argue that recent progress "may be illusory." 【Single-source verified】
- **New methods didn't win.** TSB-AD (1,070 carefully curated series, 40 algorithms) found that simple architectures and statistical methods are often better; an ICLR 2026 paper tested five families of time-series foundation models and found their anomaly detection performance not significantly different from a one-line-of-code baseline. 【Single-source verified】

Numbers from production confirm this: Microsoft's SR-CNN achieved an F1 of about 0.5 on its own 372 business KPIs, with precision 0.44–0.47, lower than all baselines. 【Single-source verified: Microsoft self-assessment】

Detectors specifically for "bad changes" are the same. SCWarn averaged an F1 of 0.95 on the authors' data, dropping to 0.45–0.73 on fault-injection tasks in follow-up papers from the same academic circle (a different task, so not an independent replication); a preprint using LLMs for bad-change detection reports F1 of 1.000/0.942/0.925, but its experimental setup section is only an outline. 【SCWarn Direction contested; LLM preprint Unverified】

**Offline detection scores cannot be taken as evidence that problems will be caught after going live.** 【Close to multi-source confirmed in direction】

## 8. LLMs Have Entered the Localization Segment, Not the Detection Segment

The hottest claim of 2025–2026 is the "AI SRE": having LLM agents investigate incidents and find root causes. Placing each vendor's materials into the "three segments," the conclusion is clear: **in public product workflows, investigations are mainly triggered by alerts, and some are initiated manually; LLMs are not responsible for first detecting anomalies.** 【Multi-source confirmed: AWS, Google, Datadog official primary sources】 The first step of AWS's example workflow is "a CloudWatch alarm fires"; the same AWS blog also contains a counterexample: an investigation where "nothing showed up on monitoring," and the team manually posted the problem to the agent. A few vendors claim to be doing proactive detection (for example, "check every change and fix regressions before they become incidents"), but give no detection rate, false-positive rate or lead time. 【Vendor-reported: claims only】 So "AI SRE shortened TTD" is currently an inference, not a measurement. 【Unverified】

In the localization segment, the commonly cited accuracy figures are almost all on lenient bases:

- **Meta 42%**: a replay evaluation, limited to historical investigations in the web monorepo, judged as the root cause falling within the **top-5** candidate code changes; the size and denominator of the replay set are not disclosed. Meta acknowledges that AI may give wrong root causes and that low-confidence answers are not shown, but the display rate is not disclosed. 【Vendor-reported】
- **Microsoft RCACopilot 0.766**: Micro-F1 (Macro-F1 0.533) for predicting the **root-cause category** on 653 incidents over one year in a single email service, relying on diagnostic handlers built manually by OCEs per alert type; 24.96% of incidents belonged to new categories. 【Single-source verified】
- **Microsoft Ahmed et al. (ICSE'23)**: the incident owner first picked the best of the model's 5 candidates before scoring; correctness scores were 2.28–3.16 (out of 5). 【Single-source verified】
- **Microsoft Triangle's "up to 97%" / "as much as 91%"**: these are routing accuracy and time-to-engage for "which team the incident is assigned to," not root-cause accuracy. 【Single-source verified: abstract-level basis】

Switch to independent benchmarks and strict bases, and the numbers fall to between 10% and 50%:

- **OpenRCA 1.0 (ICLR'25, 335 failures)**: a score is earned only if all requested root-cause elements are correct; the best in 2024 was 11.34%. Anthropic reported about 34.9% in a chart on its 2026-02 model release page, but the number is not in the page text, and third-party aggregator sites mark it "Self-reported / Unverified"; an independent 2026 study re-testing 2026 models within the same baseline framework got only 3.9%–12.5%. **These numbers cannot be connected into a "threefold progress" curve.** 【11.34% Single-source verified; 34.9% Unverified】
- **OpenRCA 2.0 (500 cases, preprint)**: averaged across 11 frontier models, "finding at least one root-cause service correctly" is 76.0%, of which only 61.5% is supported by a verified causal propagation path; the "exact root-cause set" is only 20.7%. 【Single-source verified】
- **IBM ITBench (42 Kubernetes failure scenarios)**: GPT-4o diagnosis 13.81%; 18.10% for the scenario group with traces on and 9.52% for another group with traces off—the two groups are different scenarios, so this shows only direction. The 2026 ITBench-AA leaderboard uses "precision at full recall" (missing any true root cause scores 0); as of 2026-10 the top is 56.2%. The two have different scoring rules and cannot be connected into a trend. 【Single-source verified】
- **Microsoft AIOpsLab (48 injected-failure problems)**: localization top-1 31%–62%, RCA 9%–45%, mitigation 0%–55%. 【Single-source verified: self-built benchmark, own agent among participants】

None of these benchmarks has a human SRE baseline.

Vendors' production numbers are even harder to interpret: AWS DevOps Agent's "94% root-cause accuracy" comes from "reports from preview customers and partners," with no denominator, event set or judge; Azure SRE Agent's "mitigated more than 35,000 incidents" does not define "mitigated"; Datadog has not published any accuracy figure, saying only that it is about 2 times faster than its own previous version. 【Vendor-reported】 Datadog's engineering blog does candidly admit a failure mode: in one of 12 tool calls the agent had already found the true root cause, but was led astray by noisy signals from an upstream service and output a wrong answer.

A complete n=1 case comes from Grafana (2026-01): a change ran fine in staging, passed CI and went through thorough code review, then broke the database after going live; most of the manual investigation time was spent on "confirming whether it was our deployment"; an AI assistant investigated in parallel in the background, found the root cause in 8 minutes, 20 minutes earlier than the on-call team. 【Vendor-reported: n=1】 This is exactly the typical path of this piece's question: missed by offline validation, found after going live (the original does not make clear how it was triggered), and AI accelerating localization.

## 9. Verdict

Back to the title. **"Can AI catch bad releases?" has to be answered as three questions.**

**Detection: loud bad releases don't need AI to catch them, and quiet bad releases aren't yet caught by AI either.** In big public incidents, the first detection signal appears within 1–25 minutes of the start of impact (median 3–5 minutes). 【Vendor-reported, sample selected by outcome】 The real detection gaps are in two other places: one is failures that were never instrumented—among Microsoft's repair items for missed detections, more than 40% were no relevant monitoring at all, and detection for the customer-reported portion is about 10 times slower 【Single-source verified】; the other is configuration and data channels that bypass progressive delivery, plus code paths that lie dormant for days to months before being triggered 【Multi-source confirmed: direction】. Statistical and ML detectors work inside big companies, but "recall" is a proxy, precision is between 70% and 95%, and no third party has re-tested them on production data. 【Single-source verified: vendor self-assessment】 LLMs are currently not in the detection segment.

**Localization: this is where AI is actually working; the gains may be real, but they have not been measured clearly.** In big public incidents, localization ranges from 10 minutes to about 2 hours, and the slowest one was a misdiagnosis (taking a bad configuration for a DDoS). Under strict bases LLMs can correctly identify about 10%–50% of root causes, higher under lenient bases; production numbers exist only as vendor reports.

**Mitigation: the bottleneck is here, and it is mainly not an AI problem.** The median time to stop the bleeding is about 1.8–3 hours, tens of times longer than detection. Those that stopped the bleeding within 30 minutes all relied on ready-made global switches and reverts; among the longest ones, in some the rollback baseline had already been contaminated by the bad configuration (Azure Front Door 10-29), in some the bad data had already replicated globally within seconds (Google Cloud), and there was also the long-tail repair after a manual bypass of protection (Azure Front Door 10-09).

So rather than asking "can AI find bad releases faster," the more useful questions are three engineering questions: **Do configuration and data go through progressive delivery? Can the rollback target be contaminated by the bad change? Is the false-positive rate of alerts low enough to be worth trusting?** None of these three needs AI, and the most expensive incidents in public postmortems lost precisely here.

This also means that any claim that "AI reduced MTTR by X%" should first answer: which segment was reduced? How was the starting point defined? What is the denominator? By the locked-in standards of this issue, we have not seen a single public number that can answer all three questions at once.

## 10. Ten Testable Claims

Ordered from strongest to weakest evidence.

1. **In public AI SRE product workflows, LLM investigations are triggered by alerts or manually, and are not responsible for first detecting anomalies.** 【Multi-source confirmed】 How to test: any vendor publishing the count, false-positive rate and lead time of "LLM found a bad release before the alert."
2. **The release cadences of code and of configuration/data are asymmetric, and big failures concentrate on the unstaged side.** 【Multi-source confirmed: direction】 How to test: whether similar global incidents decrease one year after retrofits such as Cloudflare Snapstone that "put configuration through progressive delivery too" go live.
3. **Offline anomaly detection scores are systematically higher than production performance.** 【Close to multi-source confirmed】 How to test: whether new methods can still consistently beat random scores and one-line baselines under protocols that use neither point-adjust nor post-hoc optimal thresholds.
4. **Detection is not the same as response.** 【Multi-source confirmed in direction: vendor case studies】 How to test: any company publishing the rate at which "automatic no-gos are overridden by humans," and the share of those overrides later proven wrong.
5. **In big public incidents, detection is on the scale of minutes and main mitigation on the scale of hours, differing by tens of times.** 【Multi-source confirmed in direction; numbers Vendor-reported】 How to test: whether, in big-company postmortems with complete timelines over the next 12 months, median TTD stays within 10 minutes and main mitigation stays above 1 hour.
6. **LLM root-cause analysis accuracy under strict bases is between 10% and 50%.** 【Single-source verified: multiple benchmarks】 How to test: whether the officially verified leaderboards of OpenRCA and ITBench-AA show results above 70% on strict bases, and whether human SRE baselines are added.
7. **The public precision of big companies' release detectors is 70%–95%, and there is no credible independent number for recall.** 【Single-source verified: vendor self-assessment】 How to test: a third party re-testing Gandalf, FBDetect or similar systems on production data.
8. **On high-severity incidents and new types of services, the share found by people is not low (Teams 29% reported externally, GenAI 38.3% reported by people).** 【Single-source verified: Microsoft only】 How to test: companies other than Microsoft publishing incident statistics broken down by detection source.
9. **Detection of customer-reported incidents is about an order of magnitude slower than of monitor-found ones.** 【Single-source verified: verified against the original by only one seat】 How to test: TTD distributions from other companies broken down by detection source.
10. **AI SRE products have shortened TTD.** 【Unverified: currently only claims】 How to test: any company publishing a before-and-after comparison split into the three segments of detection, localization and mitigation, with denominators and starting-point definitions.

**What to watch.** If any of four things happens, the judgments in this piece should change: first, **a vendor publishes the detection rate and false-positive rate of proactive LLM detection**—that would make LLMs entering the detection segment testable for the first time; second, **OpenRCA or ITBench gets an officially verified leaderboard with a human baseline**; third, **retrofits such as Cloudflare's "put configuration through progressive delivery too" get a before-and-after comparison**; fourth, **large-sample incident statistics broken down by detection source appear outside Microsoft**.

## Appendix: Methodology and This Issue's Self-Corrections

In this issue, each of the 15 sets of load-bearing claims was assigned 3 independent verification agents, through three lenses—verbatim, counter-evidence and definitions—instructed to try hard to refute. Of the 45 votes, 44 ruled "needs correction"; in addition, a two-seat audit was added for 3 single-source empirical claims, and all 3 were downgraded.

The most important original-draft phrasings overturned or rewritten by verification:

1. **"Google found that 68% of incidents come from pushes" was rewritten.** 68% is the share within the top eight trigger categories; the eight categories sum to exactly 100%, so it is not the share of all incidents.
2. **"Gandalf control-plane recall 99.8%" was rejected.** By the paper's own counts, standard recall is 37/39 ≈ 94.9%.
3. **"Gandalf data-plane recall 100%" was rejected.** This is a proxy definition of "no Sev0–2 incident was caused by a bad release."
4. **"FBDetect has a false positive only once every 13 years" was rejected.** This is a metric spread per developer head; precision on the verifiable subset is about 70%.
5. **"Among the 6 public-postmortem cases with TTD≤5 minutes, 4 took more than 1 hour to mitigate" was withdrawn.** The result changes with the anchor; changed to "main mitigation median about 1.8–3 hours."
6. **"In public postmortems, zero were found first by customers" was downgraded.** It holds only within the sample; 29% of Teams incidents were reported by external customers, and in Atlassian 2022 a customer ticket arrived first.
7. **"Not one case in the sample relied on automatic rollback, which shows automatic rollback doesn't work" was ruled a selection artifact.** Bad releases caught by automatic rollback don't get written up as big public postmortems.
8. **"OpenRCA progressed from 11% to 35%" was ruled dead.** The 35% is a self-reported number in a vendor chart; the independent re-test within the same framework is 3.9%–12.5%.
9. **"AI SRE products are all triggered by alerts" was rewritten.** Mainly triggered by alerts, with some initiated manually.
10. **"Walmart's AI detection covers 63% of major incidents and cut MTTD by 7 minutes" was rejected as evidence of release detection.** The denominator of the 63% is 58 incidents from 4 case-study customers, and there is no MTTD baseline.
11. **"Facebook's canary can detect within about 10 minutes" was rewritten.** The 10 minutes is the run duration of the canary test, not the detection time.
12. **"Gandalf detects bad releases in 5 minutes" was rewritten.** The 5 minutes is the decision pipeline latency; the paper reports no TTD distribution.

These corrections share a common direction: **nearly every number that made "detection is already fast, AI is already accurate" look stronger—near-perfect recall, a false positive once in decades, threefold progress, minute-level detection—became narrower once sent back to the original.** Where it narrowed was usually its denominator: counting only misses that turned into big incidents, looking only at confirmed reports, looking only at loud failures.

## Appendix: Main Sources

**Incident sources and measurement**: Google SRE book, Chapter 1 (https://sre.google/sre-book/introduction/), SRE Workbook Appendix C (https://sre.google/workbook/postmortem-analysis/), Gunawi et al. SoCC'16 (https://ucare.cs.uchicago.edu/pdf/socc16-cos.pdf), Tang et al. SOSP'15 (https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf), DORA metrics explainer (https://dora.dev/insights/dora-metrics-history/), Davidovič, "Incident Metrics in SRE" (https://sre.google/resources/practices-and-processes/incident-metrics-in-sre/), Cook, "How Complex Systems Fail" (https://how.complexsystems.fail/)

**Who finds it first**: Ghosh et al. SoCC'22 (https://www.microsoft.com/en-us/research/wp-content/uploads/2022/09/3542929.3563482.pdf), Ganatra et al. ESEC/FSE'23 (https://jonathanmace.github.io/papers/ganatra2023detection.pdf), Yan et al. (https://arxiv.org/abs/2504.08865), Ranganathan et al. (https://arxiv.org/pdf/2511.07424)

**Public postmortems**: CrowdStrike RCA (https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf), Google Cloud 2025-06-12 (https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW), Cloudflare 2025-11-18 (https://blog.cloudflare.com/18-november-2025-outage/), Cloudflare 2025-12-05 (https://blog.cloudflare.com/5-december-2025-outage/), Cloudflare 2019-07-02 (https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/), Fastly 2021-06-08 (https://www.fastly.com/blog/summary-of-june-8-outage), Azure Front Door PIR 2025-10-29 (https://azure.status.microsoft/en-us/status/history/?trackingId=YKYN-BWZ), Azure Front Door PIR 2025-10-09 (https://azure.status.microsoft/en-us/status/history/?trackingId=QNBQ-5W8)

**Progressive delivery and detectors**: Gandalf NSDI'20 (https://www.usenix.org/system/files/nsdi20-paper-li.pdf), Google CAS (https://queue.acm.org/detail.cfm?id=3194655), SRE Workbook, "Canarying Releases" (https://sre.google/workbook/canarying-releases/), Kayenta (https://cloud.google.com/blog/products/gcp/introducing-kayenta-an-open-automated-canary-analysis-tool-from-google-and-netflix), Spinnaker canary judge (https://spinnaker.io/docs/guides/user/canary/judge/), AWS Builders' Library (https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/), FBDetect SOSP'24 (https://tangchq74.github.io/FBDetect-SOSP24.pdf), Savor et al. ICSE'16 (https://www.eecg.toronto.edu/~stumm/Papers/Savor-ICSE16.pdf)

**Anomaly detection evaluation**: Kim et al. AAAI-22 (https://arxiv.org/abs/2109.05257), Wu & Keogh (https://arxiv.org/abs/2009.13807), TSB-AD (https://proceedings.neurips.cc/paper_files/paper/2024/file/c3f3c690b7a99fba16d0efd35cb83b2c-Paper-Datasets_and_Benchmarks_Track.pdf), SR-CNN KDD'19 (https://arxiv.org/abs/1906.03821), Opprentice IMC'15 (http://conferences2.sigcomm.org/imc/2015/papers/p211.pdf)

**Root-cause analysis**: Meta engineering blog (https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/), RCACopilot (https://arxiv.org/abs/2305.15778), Ahmed et al. ICSE'23 (https://arxiv.org/abs/2301.03797), OpenRCA (https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf), ITBench (https://arxiv.org/abs/2502.05352), AIOpsLab (https://arxiv.org/abs/2501.06706), AWS DevOps Agent GA (https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/), Grafana case study (https://grafana.com/blog/a-tale-of-two-incident-responses-how-our-ai-assist-helped-us-find-the-cause-3-5x-faster/)

**Related research on this site**: for the ceiling on the offline-validation side, see ["The Machine-Judge Atlas: How Much Can LLMs Scale Software's Oracles?"](https://hub.cissychen.com/deep-research/machine-oracles-deep.en.html), where Argus's low-base-rate mechanism is isomorphic to Section 6 of this piece; for humans overriding correct alerts, and the better the automation the harder it is for people to judge, see ["The Ironies of Automation: The Better the AI, the Faster the Human Veto Decays?"](https://hub.cissychen.com/deep-research/automation-irony-deep.en.html); for the pre-release verification bottleneck, see ["AI Code Review: Cure for the Verification Bottleneck, or Turtles All the Way Down?"](https://hub.cissychen.com/deep-research/ai-code-review-deep.en.html); for how organizations should be designed when failures outpace human reaction, see ["When Code Becomes Cheap: Theory and Evidence for the AI-Native Transformation of Software Organizations"](https://hub.cissychen.com/deep-research/ai-native-deep.en.html).
