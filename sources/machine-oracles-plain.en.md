# Can AI Find Real Bugs? First Ask Who the Judge Is (Plain-Language Edition)

> This is the condensed edition of the deep dive of the same name. Every key number has been independently checked; for the full arguments and sources, read the deep dive.

## A forty-year-old problem everyone suddenly touches

Software testing has an old nemesis: a program produces a result — **who decides whether that result is correct?** The thing that rules on correctness is called an *oracle* — the judge. The hard part of testing was never making the program run; it's writing down what "ran correctly" even means. A 2015 authoritative survey audited three decades of research and concluded: automating the judge is the least-solved link in all of test automation.

Then AI arrived. AI can write tests, write rules, write assertions, report vulnerabilities — it looks like the judge problem is about to be brute-forced. This essay lays software's judges out as a map and settles accounts cell by cell: **who is each cell's judge? Can it be sweet-talked? And are AI's scores real once it enters?**

The shape of the answer up front: AI's report card depends strictly on **which seat it takes** in the verification pipeline. It can be the **worker** (generating test inputs), the **drafter** (proposing rules and specs, filtered by an independent mechanism), or the **judge** (ruling directly). In the first two seats, the wins are real money. In the third seat, nearly every independent re-check shrinks the numbers.

## Where the judge is most incorruptible, AI's scores are hardest

**Math proofs.** A proof checker cannot be persuaded; wrong is wrong. AI provers surged to 88–90% within a year (under a multiple-attempts-per-problem scope), with one lovely detail: letting the model read the checker's error messages and retry lifted the score from 88.1% to 90.4% — **the more incorruptible the judge, the more freely AI can grind through trial and error.**

**Crash detection.** Google let AI write fuzzing probes for open-source projects, with the verdict entirely in the crash detector's hands: coverage rose automatically across 272 projects, and 26 new vulnerabilities surfaced in projects already tested for hundreds of thousands of hours — including one in OpenSSL that, by Google's judgment, had likely been hiding for twenty years, unreachable by human-written probes.

**Big Tech's test factory.** Meta had AI mass-produce unit tests behind a row of machine gates: doesn't compile — discarded; flaky across five runs — discarded; adds no coverage — discarded. In the end, 73% of the improvement suggestions were accepted into production by engineers. Later they went further: have AI inject artificial bugs into the code first, then have AI write tests that catch them — grading the exam by "can it kill the planted bugs," another machine gate.

Note what these share: **AI never once sat as judge.** Every verdict came from proof checkers, crashes, compilers, execution. AI was just capacity.

## The moment AI takes the bench, the numbers start shrinking

The other side is just as clear, and not a one-off:

- A famous "AI writes test assertions" tool once claimed 30 exclusively found bugs; two independent teams re-checked: nearly half its assertions were false alarms, and after fixing a leak in the evaluation setup, true precision was **0.38%**.
- AI judging whether code has vulnerabilities: 68% F1 on the lenient old exam; on a decontaminated, strictly split new exam, **3%** — GPT-4 on the strictest paired questions performed "no better than a random guess." Rename a variable and it flips its verdict 17% of the time.
- A vendor advertised "AI triage agrees with security researchers 96% of the time"; the fine print: on false-positive calls — exactly where triage is needed — agreement was 41%. On an independent benchmark, the best AI triage managed 16.9% precision.
- The cleanest controlled contrast: let AI propose database testing rules, but have a **mathematical prover** certify them before duty — 20 bug reports, 0 false alarms. Same system, prover swapped for GPT-5 as judge — 20 reports, **all false alarms**. The reason is humble: the AI judge's per-call error rate was only about 5%, but real bugs in mature databases are so rare that a few wrong calls drown the few true ones. **A judge can be only slightly wrong, and the reports can be entirely wrong.**

One more mechanical bad news: when AI writes test assertions, it aligns not with the code in front of it but with "how this kind of code usually behaves" from its training. One study modified code and had AI regenerate tests on the spot: 99% of the failing tests were actually asserting the old behavior. So AI tests make good **regression locks** (keep the status quo from breaking) and bad **correctness judges** (decide whether the status quo was ever right).

## One AI output, two judges, two fates

In 2024–2026, open-source security staged a natural experiment.

The same "AI-found security issues": plugged into a **crash detector**, the output was 26 real vulnerabilities and a twenty-year-old CVE. Dumped onto **human maintainers** for triage, the output was a disaster — about 20% of curl's 2025 security reports were AI garbage, under 5% were real, each report burned three or four of a seven-person team for half an hour to three hours apiece, and in early 2026 curl shut down its seven-year bug bounty. The Linux kernel security list went from two or three reports a week to ten, the increase "only AI slop."

**But the story has a second act.** In 2026, after curl resumed taking reports, the confirmation rate didn't fall — it recovered and overshot its historical level (15–16%), with nearly every report using AI to some degree; kernel reports climbed to 5–10 a day, mostly correct, and the new problem became mass duplication — prompting Torvalds to change the rules: AI-found bugs are treated as public, must come with a **runnable reproducer**, ideally a patch — pushing the burden of proof back onto the submitter, demanding something a machine can verify.

The two acts together are the whole essay in miniature: **whether the judge is incorruptible decides whether the same AI output is an asset or a burden; and whether human judges drown depends on incentives and tool generations.**

## Don't deify the incorruptible judge either

Three honest caveats, to keep the conclusion from being overused:

**First: the judge may be incorruptible while the exam questions are wrong.** A proof checker only guarantees "the proof follows from the statement," not "the statement says what you meant." The most popular formal-math exam was found to have over half its problems mismatched against the original questions; even human experts' handwritten formal specs contain semantic errors 16–38% of the time; ask an LLM to translate plain-language requirements into the spec language TLA+, and semantic correctness is 8.6%. One model even learned to slip "assume false" into specs, letting any implementation pass verification. **In the AI era, verification risk is moving up from "proof written wrong" to "question set wrong."**

**Second: AI's gains must be compared against strong baselines, not against nothing.** A dumb, AI-free mutation tool out-benched a star AI fuzzing tool in same-bench re-tests; an AI-free database testing framework found 196 bugs on its own. Several published "AI gains" lost to "the control group was weak."

**Third: machine gates are necessary, not sufficient.** Uber uses AI to fix data races; some fixes that passed the "re-run a thousand times, no recurrence" gate were still rejected as incorrect by human review. Above all the machine gates, the human final say can't yet be retired.

## How to check this essay's judgments

Eleven testable claims, hardest evidence first:

1. **In cells with incorruptible judges, AI gains have hard numbers** — 26 vulnerabilities, a twenty-year CVE, proof completion 88→90, Meta's 73% acceptance — all verdicts from machines or maintainers, none from AI self-grading.
2. **With AI on the bench, numbers shrink under independent re-checks** — 0.38%, 3%, 16.9%, 20/20 false alarms: five independent bodies of evidence, one direction.
3. **Risk has moved up to the question-setting layer**: verifiers can't vouch for the questions — half the formal exam mismatched, human specs wrong 16–38% of the time, AI-written TLA+ semantically right only 8.6%.
4. **AI gains must beat strong non-AI baselines** — a dumb tool out-benching a star AI tool has already happened.
5. **The premise behind "have several AIs check each other" was experimentally rejected** (shared mistakes at 3.7× the independence assumption) — though three-version voting still cut failures to roughly a third; decay, not zero.
6. **The "kill planted bugs" gate is cheap, effective, and industrialized — but its scores can also be inflated by data contamination** (about 10 points), just less easily maxed out than coverage.
7. **AI assertions anchor 99% to old behavior from training**; the current ceiling for proactively catching unknown bugs is 16–30%.
8. **AI as drafter delivers real gains, but the leftover human burden doesn't vanish** — drafting got cheap; adjudication got no cheaper.
9. **Human judges drowning in AI reports is real, but uneven and reversible** — curl closed its bounty then overshot its old confirmation rate; the kernel went from "only slop" to "mostly correct but duplicated."
10. **AI is still absent from the concurrency-bug cell**, for a structural reason: the biggest AI fuzzing pipeline never plugged in the race detector.
11. **Neither direction of "AI code is wrecking production" has passed independent re-checking** — the negative narrative (rising code churn) got contradicted by a re-test too.

Worth watching: whether the AI fuzzing pipeline replicates its record once the race detector is plugged in; whether the kernel's "attach a patch" rule tames the duplication flood; and whether the next product claiming "AI as judge" dares publish independently re-tested false-alarm numbers.

## What matters most

1. **Evaluating any "AI finds bugs / AI reviews" product, the first question is always: who is the judge?** Verdicts from compilers, test execution, crashes, provers — trust the numbers. Verdicts from the AI itself or its cousins — discount heavily first.
2. **Give AI capacity an independent gate, not another AI.** Compile, execute, cover, kill planted bugs, re-run a thousand times — these gates are cheap, mechanical, unpersuadable. They are the real leverage of the AI era.
3. **Use AI-written tests as regression insurance, not as certificates of correctness.** They can lock in the status quo; they cannot tell you whether the status quo was right.
4. **Beware evaluations sold on "coverage" and "agreement rates"**: coverage saturates easily, and agreement's bulk may come from the easy half of the task. Look at the false-alarm side, the kill rate, the independent re-tests.
5. **If you're on the drowning side** (maintainer, reviewer, security team), borrow the kernel's fix: push the burden of proof back — demand machine-verifiable artifacts, a runnable reproducer, a patch that passes tests.
6. **Software is lucky: it owns a whole cabinet of unpersuadable mechanical judges.** Wire AI's capacity into them — don't let AI replace them.

*For the full arguments, every source, and the counter-evidence, read the deep dive.*
