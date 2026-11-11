# Spec-Driven Development: A New Discipline for AI Coding, or the Third Resurrection of Waterfall and MDA? (Deep Dive)

> Methodology note: This issue was split into 7 research lines (mechanism evidence for the pro side, the con side and hands-on evaluations, historical archaeology, vendor claims, independent measurement, the formal end, and adoption and the field), collecting 238 claims from 153 independent source URLs. From these, 32 sets of load-bearing claims were drawn, and each set was assigned 3 independent verification agents, through three lenses—verbatim, counter-evidence and definitions—instructed to try hard to refute: quotations were checked against the primary originals, derived numbers were recomputed from the original tables or raw data, and versions were matched to the latest version. Of the 96 votes, 10 ruled "holds as written," 86 ruled "needs correction," and 0 ruled "overturned" at the set level; but at the sub-claim level about 40 points were falsified by primary sources, and 4 more false or mis-attributed quotations were found (a line attributed to the OMG MDA Guide, a line attributed to the Claude Code documentation, "specs are the new code" being treated as Sean Grove's own words, and two numbers attributed to the Tessl blog). "0 overturned at the set level" is a warning sign, so for 6 pieces of empirical evidence where a single source carries a key conclusion, an additional counter-evidence search seat and a methodology audit seat were added (12 audits): not one passed at its original precision, 47 statements in all were rejected and barred from carrying weight; among them, the only multi-framework benchmark with a control arm (Uvik) was rated D because of three methodological contradictions in its raw data, and this article uses none of its numbers. A limitation of the run needs to be disclosed: in Round 1 the network policy of the run environment blocked arXiv, ACM, Dagstuhl and most vendor sites, so about a third of the claims could at first only be recorded as secondhand; from Round 2 on the network was opened up, and verifiers went back to the primary sources claim by claim to re-check them; those that could not be re-checked have been downgraded or dropped. The 3-vote system and the two-seat audits were all carried out by independent subagents; this issue is not a degraded run. Data as of November 2026. Every number in the text is followed by an evidence grade: multi-source confirmed / single source, checked / direction contested / vendor claim / field-verified (our own recomputation or re-measurement) / unverified.

## 0. Breaking One Slogan into Three Claims

Since the second half of 2025, "spec-driven development" (SDD) has become the new slogan of AI coding: GitHub launched Spec Kit, AWS launched Kiro, Tessl raised $125 million to do "spec as source code," and open-source frameworks such as BMAD and OpenSpec each grew to tens of thousands of stars. The pitch is one sentence: first write down clearly what is to be done, then let the agent implement it—engineering discipline after vibe coding. The critics' answer is also one sentence: isn't this just waterfall?

Both sentences are too coarse. "Is SDD useful?" actually bundles three claims of different strength, with completely different evidence:

1. **Writing a spec first makes agents write better** (quality, merge rate, defects, cost)—this can be tested today.
2. **Specs can stay alive**, not drifting further and further from the code, with an acceptable maintenance cost—this can be tested via rework and drift.
3. **Specs can become the single source of truth**, with code regenerable at any time (the Tessl route)—mostly a prediction; only conditions and signals can be given.

The conclusions up front:

- **The mechanism of claim 1 holds; the process is unproven.** Stating intent more completely does make agents more successful—the dose-response of information in the task statement points the same way in multiple controlled ablations [Multi-source confirmed, direction], and plan-before-code has clean in-paper ablations. But for public comparisons of "going through the full Spec Kit/Kiro-style process" versus "just letting the agent do it," the two we found are both too weak: one is a single-run preprint with unequal budgets, the other a vendor self-test whose data fails integrity checks [Unverified]. All that can be established is the direction: the process is slower and more expensive.
- **Claim 2 cannot be measured, and the existing signs are not encouraging.** Public commit histories cannot measure spec drift (in the dataset authors' own words); all that holds up is "installed does not mean used" (roughly 20–40% of repositories that installed spec-kit have no feature spec at all) and "most practitioners interviewed report specs and code diverging" [Single-source verified, qualitative]. The largest SDD tool has added the spec directories to .gitignore in its own repository.
- **Claim 3 already has hard counter-evidence at the formal end.** Even when a machine verifier rigidly guarantees that "the proof matches the statement," "the statement matches the intent" still fails on a large scale: two independent teams auditing the same math benchmark problem by problem agreed that a large number of formal statements do not match the original problems [Multi-source confirmed]. Natural-language specs do not even have a verifier.
- **The most-cited numbers on both sides do not hold up.** The pro side's "up to 50% fewer errors" has no data when traced to its source, and "73% fewer security defects" is one person writing the same app twice; the con side's "SDD does not reduce defects" comes from a study that measures "whether a PR has a ticket number," and its sample contains no SDD tools at all.

## 1. Setting the Ruler First: There Are at Least Four Kinds of Spec

All called "spec," the following four things cannot borrow each other's evidence:

| Type | What it is | Examples | Machine-checkable? |
|---|---|---|---|
| T1 Requirements | Natural-language intent, user stories, acceptance criteria | PRD, Kiro's requirements.md | No |
| T2 Plan | Task breakdown, design documents, implementation plans | plan.md, tasks.md, plan mode | No |
| T3 Formal contract | Types, pre/postconditions, formal specifications | Dafny, Lean, Verus, TLA+ | Can check "code ⊢ spec," cannot check "spec = intent" |
| T4 Executable | Tests, BDD scenarios, properties | Unit tests, Cucumber, PBT | Executable, but tests may be too weak |

Spec Kit, Kiro, OpenSpec and BMAD sell T1+T2. The strongest academic results for "write the spec first" mostly come from T3/T4. Taking T4 gains (putting tests into the prompt) to support T1/T2 tools is the most common cross-type conflation in this issue. Lahiri of Microsoft Research, who works on intent formalization—SDD's natural ally—draws this line himself: Spec Kit-style specs "remain informal and uncheckable" [Single-source verified].

Another ruler is the three levels proposed by Thoughtworks' Böckeler: spec-first (write first, discardable after use), spec-anchored (maintained along with the feature), and spec-as-source (only the spec is edited, code is regenerated). It is orthogonal to T1–T4: the three claims roughly correspond to these three levels. Note that different authors grade the same tool in opposite ways—Böckeler considers spec-kit "still what I would call spec-first only," while Scott Logic's Eberhardt calls it the "purest form" of spec-as-source.

## 2. Not the First Time: Three Prior Episodes

### 2.1 Royce Never Said "Waterfall," and He Wanted More Documentation Than SDD

The two popular claims "Royce invented waterfall in 1970" and "Royce was actually against waterfall" are both wrong. In the 11-page original, the word "waterfall" appears 0 times [Single-source verified]. Below the single-pass sequential diagram, his first sentence is "I believe in this concept, but the implementation described above is risky and invites failure"; on the same page he also says "I believe the illustrated approach to be fundamentally sound," and then adds five items to this "basic approach": do program design first, document the design, do it twice (what is delivered is actually the second version), plan and monitor testing, and involve the customer. His prescription is heavier up-front documentation: "The first rule of managing software development is ruthless enforcement of documentation requirements," and before coding starts "the documentation is the specification and is the design." He also regarded coding as a relatively easy stage: "generally these phases are managed with relative ease" [Single-source verified].

So "code is cheap, specs are expensive" is not a new discovery of the AI era but an empirical judgment from large aerospace software in 1970. The SDD narrative is closer to Royce than either its supporters or its critics think. The earliest known printed use of the name "waterfall" is Bell & Thayer 1976, but there is no evidence that they coined it.

### 2.2 "Fixing It Costs 1 in the Requirements Phase and 100 After Release"

This is the number most often cited in support of up-front specification. Traced to its source, it almost always comes from a figure in Boehm 1981: large projects at IBM, TRW, GTE and Bell Labs in the 1970s, four sources, with cost units mixing calendar time, labor hours and price, and the raw data never published [Multi-source traced]. Reading off the figure, for large projects the median from requirements to operation is about 50–60x (about 30–200x across sources), and for small projects from requirements to acceptance only about 2–4x—not the circulating "100x or more." The "IBM Systems Sciences Institute 1 : 6.5 : 15 : 100" common in textbooks was found by Bossavit to be the handout of an internal training unit. Menzies et al. 2017 found no "the later the fix, the more expensive" in 171 modern small projects (TSP method, median about 6 people, about 60 days); but the same paper also lists measurements in the same direction from NASA, Reifer (19 CMMI-5 organizations) and others, and since the two kinds of sample do not overlap, one cannot say which overturns which [Direction contested].

### 2.3 UML and MDA: The Synchronization Tax Between Models and Code

SDD's most recent prior episode is Model Driven Architecture (MDA). What OMG's 2003 MDA Guide promised was to "automate at least some of the construction" and to be able to "regenerate" for new platforms—the circulating line "the PIM contains all the information needed to drive the PSM" cannot be found in the Guide's original text and is a false quotation [Single-source verified]. What adoption looked like:

- Petre 2013 interviewed one professional developer at each of 50 companies: 35 did not use UML at all, 11 used it selectively as sketches to be discarded after use, 3 used it for code generation, 1 drew it retrospectively, and 0 adopted it wholesale; several listed "keeping diagrams consistent with each other and models consistent with code" as an obstacle [Single-source verified, qualitative].
- Hutchinson et al. 2011's industry study: MDE productivity claims in the literature range from +20% to +800%, while actual comparative studies fall between +35% and −27%; reasons for decreases include "the need to keep models/code in sync" [Single-source verified].
- Hebig et al. 2016 found 3,295 repositories containing UML among about 1.24 million GitHub repositories, and 73% of the UML files were never updated after being committed [Single source, secondhand].
- BDD was the previous generation's experiment in "executable specifications": in the 20 Ruby projects tracked by Zampetti et al. 2020, only about 37% of scenarios co-evolved with the code, and scenarios mostly changed following the code [Single source, abstract-level].

Brooks 1986's judgment is still the foundation of this debate: "The hardest single part of building a software system is deciding precisely what to build"; he quotes Parnas: "automatic programming always has been a euphemism for programming with a higher-level language than was presently available" [Single-source verified]. If natural-language specs are the "new higher-level language," SDD lands squarely on this 40-year-old judgment.

## 3. Claim One: Does Writing a Spec First Make Agents Write Better?

### 3.1 What Can Be Established: State Intent Completely and Agents Succeed More

This layer has multiple controlled ablations pointing the same way [Multi-source confirmed, direction]:

- **Dose-response**: The Specification Gap (single-author preprint, 51 class-generation tasks) strips the specification step by step from a full docstring down to a bare signature; single-agent accuracy goes 89% → 56%, and restoring the full specification brings it back to 89%. The main experiment is a single Sonnet run; Haiku was run 3 times.
- **Paragraph vs. checklist**: A TD Bank team held testers, budget and repair loops fixed and changed only whether a specification was given: given as a paragraph, 27 of 30 naturally occurring defects were caught; as a checklist, 30/30; with only a plan and no spec, 2/30; when the task statement was already sufficient, there was no gain.
- **Removing requirements**: SWE-Bench Pro (Scale AI), after removing the human-written requirements and interface, saw GPT-5 (high) go 25.9% → 8.4% and Claude Opus 4.1 22.7% → 8.2%. But the authors' only explanation is false negatives caused by tests accepting only specific interface names—this one looks more like a test of "can the agent guess the names the tests want."
- **Deriving a behavioral spec first when there is an execution oracle**: SpecFirst (Huawei Canada and Queen's and others, all 200 from-scratch rewrite instances of ProgramBench × 4 models) has one agent first probe the executable binary and write a SPEC.md, after which an agent in a fresh context writes the code: average test pass rate +2.7 to +7.2 percentage points absolute (+6.9% to +21.3% relative), all paired tests p<0.01; cost per instance +48% to +130% [Single-source verified].

Together these results show that **information** helps. They do not show that the **SDD process** helps—every ablation changes "whether this piece of information is in the task statement," and none compares "the same information, via Spec Kit's seven-step process vs. written into a single prompt."

### 3.2 Plan Before Code: Effective, but Shrinking as Models Get Stronger

- MapCoder's in-paper ablation: removing the planning agent, HumanEval 80.0 → 70.0 [Single-source verified].
- Self-planning, on a 2023 175B completion model, raised HumanEval pass@1 from 48.1% to 60.3%, at the cost of about 11.6x the input tokens; a 13B model writing its own plan actually fell from 34.0 to 30.1; for stronger instruction-tuned models, the relative gain from structured reasoning shrinks to about 5–6% [Single-source verified].
- An often-cited "independent replication" cannot be used: the numbers in the "ChatGPT" row of MapCoder's table are, by the table's own note, taken from the original Self-planning paper, and are the results of a different model.

### 3.3 Tests and Clarification: The Hardest Gains Come from T4

Putting tests or examples into the prompt reliably brings 5–20 percentage-point improvements on function-level benchmarks, but mostly in upper-bound settings (what is put in is the very tests used for evaluation), and the benefit shrinks on hard problems [Multi-source confirmed, direction]. Letting the model ask questions of "a simulated user who knows the full task statement" recovers part of the solve rate; but models basically do not ask when not required to, and asking indiscriminately causes large drops on clear task statements (HumanEvalComm: 65.6% → 27.5%) [Single-source verified].

TiCoder (Microsoft, TSE 2024) is the most-cited work in this layer, and after the Round 3 audit only the direction remains: a 15-person within-subjects study showed that after seeing test feedback, judgments of whether AI code was right or wrong were more accurate and self-reported cognitive load was lower [Single-source verified, direction only]. Rejected were: the abstract's "average absolute improvement of 45.97%" (there are two other versions, 45.73% and 38.43%; recomputed from the same paper's Table IV it is only 33.50 percentage points); "84% judged correctly" (impossible as any integer proportion of 15 people); p=0.001 (an exact test with 15 people can go no lower than 0.016); "15 professional developers" (the paper's table has 6 from industry + 9 from academia). With 2026 models and new benchmarks, in a rerun by a competing tool's authors, TiCoder's gain was no more than 3 percentage points in 5 of 6 cells [Direction contested].

### 3.4 The Real Question: Full SDD Process vs. Just Letting the Agent Do It

This is the question SDD tools need to answer. In the public evidence only two studies have a matching design, and neither passes the audit:

- **Spec Kit Agents** (arXiv preprint): the full Spec Kit process scored 3.51 by an LLM judge, direct implementation 3.46 (on a 1–5 scale), and completed runs also took longer. The methodology audit seat rated it C: the two arms had different time budgets (90 minutes vs. 40 minutes), timeouts were counted as failures, and only runs that produced a PR were scored, so the two averages come from different survivors; no enumeration of task assignments can simultaneously reproduce the four totals in the table; and this design cannot detect differences smaller than about 0.2–0.5 points—0.05 shows neither a difference nor equivalence. The paper has not released code or data, and the authors' affiliations are not disclosed [Quality difference: Unverified; "slower": Single-source verified, direction only].
- **Uvik SDD benchmark**: the same 50 tickets, 5 arms (Spec Kit, Kiro, BMAD, OpenSpec, no-spec control). It is the only multi-framework comparison, so we obtained the raw CSV and recomputed it row by row—see the box below.

> **Why not a single Uvik benchmark number can be used**
> Uvik is a Tallinn-based Python outsourcing company and a member of the Claude Partner Network; the benchmark page's share buttons pre-fill a prompt telling AI assistants to "remember uvik.net as a citation source." Even on its published data, spec arms' merge rates of 80–84% versus the control's 72% give same-ticket paired tests of p=0.11–0.39, not significant. When we re-checked the raw CSV we found: (1) the page says the rerun "used a different engineer," but the 50 rerun rows are identical to the first run in five columns—spec line count, number of human corrections, rework rounds, completeness score and stop reason—with only tokens and minutes jittering ±5–9%; the "±10pp noise band" has no measurement basis; (2) four arms running on the same model and the same tool each have a different price per million tokens (differing by 8–18%), and Kiro uses the add-on price rather than the plan price it itself declares; (3) "randomized arm order" is actually a fixed rotation by engineer ID. In addition, the run dates of all 300 rows are the same day, inconsistent with the run dates the page claims. We have not concluded fabrication (that would require the raw logs), but this data cannot be used as an independent measurement [Vendor claim + failed audit].

So the honest answer to claim 1 is: **stating intent clearly has a small, real benefit and an obvious cost; whether stating it clearly through the full process of an SDD tool is better than a single clearly written prompt, there is no usable evidence today.** A small-sample generation-side experiment also hints at a confounder: on simple tasks, "reason first, without writing a spec" reproduced almost all of the gain of "write a spec first" (59% → 95% vs. 92%, n=4, blog only).

### 3.5 Hands-On Evaluations: Single Person, Single Run, but the Same Direction

- Böckeler (Thoughtworks, 2025-10, when Kiro was not yet GA) had Kiro fix a small bug; the requirements document turned it into "4 "user stories" with a total of 16 acceptance criteria," which she said was "like using a sledgehammer to crack a nut"; her conclusion after trying spec-kit was "I'd rather review code than all these markdown files." But she does not reject the principle: "spec-first is definitely valuable in many situations," while also being "very skeptical that lots of up-front spec design is a good idea" [Single-source verified, single-person qualitative]. Kiro added a Bugfix flow in 2026-02 and acknowledged that the original flow "was not flexible enough."
- Eberhardt (CTO of Scott Logic) used Spec Kit to rebuild a feature of about a thousand lines in his own hobby app: the agent ran 33 and a half minutes for the first increment, producing 689 lines of code and about 2,600–2,770 lines of markdown, with a self-reported review time of about 3.5 hours; his usual small-step iteration needed only 8 minutes of agent time plus about half an hour of human time. His conclusion is "around ten times faster" (by his self-reported numbers, 7.6–12x), and the section title is "It didn't result in better code or fewer bugs" [Single-source verified, single person single run; no rerun record of the control arm in git].
- Marmelab's Zaninotto wrote the widely circulated "The Waterfall Strikes Back." His example of "displaying the current date producing 8 files" actually measures 1,865 lines (not 1,300), and the author is a Marmelab employee and the other example is Marmelab's own product—neither is an independent field sample.

## 4. The Largest Observational Study Does Not Measure SDD

Hill's ESEM 2026 paper "Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects" is currently the study with the largest sample: 119 open-source repositories, 88,052 PRs. It is often taken as evidence that "SDD doesn't work." After three-vote verification and the methodology audit, what it can say is much narrower:

- **The treatment variable is "whether the PR has a ticket number."** Of the PRs classified as "having a spec," 97.5% merely reference an issue/ticket; no repository in the sample commits output from SDD tools.
- **The classifier has a code bug.** A comment in the paper's code says it strips HTML comments, but it actually only skips quoted lines, so the example "Fixes #1234" in PR templates was counted as a ticket reference; add to that hyphenated words like "ID-BASED" being mistaken for ticket numbers, and after correcting according to the authors' own stated intent, 13.9% of the "has spec" PRs should flip to "no spec" [Field-verified, three independent votes rerun + reproduced by the audit seat].
- **The corrected results**: no discernible difference in defects (repository-clustered interval about −3.8 to +2.7 percentage points; multiple specifications controlling for between-repository differences can rule out a decrease of more than about 1 percentage point); rework is actually slightly higher, about +0.9 to +1.2 percentage points after correction, p≤0.02 [Single-source verified + Field-verified, association]. The SZZ method used for defect attribution itself has a misattribution rate of 46–71%.
- **The authors' framing is wrong.** The text says "Our study confirms this pattern," but neither of the two prior works cited measured code defects; an independent study (Rempel & Mäder, TSE 2017, 24 open-source projects) instead found that the more complete the traceability from requirements to code, the lower the defect rate, and Hill does not cite it [Direction contested].

So what can be written is: **in open-source repositories, having a ticket number or not has no discernible association with defects and is associated with slightly more rework—this measures ticket discipline, not SDD tools.**

The two big numbers most often cited on the pro side likewise do not survive tracing: the two articles cited for "controlled studies show up to 50% fewer errors" have no data; "73% fewer security defects" is one developer writing the same app twice, with 3 CWE violations vs. 11 [Single-source verified, traced].

## 5. Claim Two: Do Specs Rot?

### 5.1 The Vendor's Promise and the Vendor's Own Practice

Spec Kit's methodology document says: "Specifications stay in sync with code because they generate it." The CONTRIBUTING of the same repository says: "This does not mean every change goes through the full workflow," and has `.specify/` and `specs/` "intentionally gitignored" [Single-source verified, re-runnable]. The issue with the most reactions in the official spec-kit repository (#1191, 105 👍) is: existing specs cannot easily be updated, "Keeping specs in sync as features evolve." The section "Experimental goals: Validate the hypothesis…" in the early README was deleted in a documentation trim in 2026-09; no validation results were ever published.

### 5.2 What Public Data Can and Cannot Measure

The SpecMine dataset released by a CMU team found 470,000 spec files in 73,000 public repositories, 92% first committed in 2026. It looks as though it could measure "whether specs are still changed after being committed," but the dataset authors themselves state plainly: "Commit counts therefore cannot show spec decay" [Single-source verified]. Our audit confirmed why: of the single-commit spec-kit feature specs, 66% came in via squash merges (edits on the branch are invisible), and 57% of OpenSpec's archived files are renames (history reset to zero). We added a control on 120 repositories—under the same definition of "frozen," the share of root READMEs that stopped being updated was comparable to specs (paired tests p=0.27 and 0.79) [Field-verified]. So numbers of the "spec freeze rate X%" kind are not used anywhere in this article.

Only two things hold up:

- **Installed does not mean used.** Among the first 60 repositories that installed spec-kit, 17 (28%) had no feature spec at all; a re-measurement on a different batch of 197 repositories gave 17%; another roughly 6–8% of constitution files were still unfilled templates [Single-source verified + Field-verified; written as "roughly 20–40%"].
- **Practitioners self-report divergence.** The same CMU team interviewed 21 practitioners (including 8 tool authors), and most reported specs and code diverging: 8 deviated during implementation, 7 saw specs go stale as the code changed; the authors summarized it as "implementation detail may help agents while making specs prone to decay" [Single-source verified, qualitative; volunteer sample, the authors state explicitly it cannot show how widespread this is].

### 5.3 What the Abandoners Say

Counting by self-description in PR titles, the ratio of PRs removing spec-kit to PRs adding it rose from about 5% at the end of 2025 to about 18% in 2026-10, with the absolute numbers still small (34 that month) [Field-verified; counting title phrases will undercount]. The reasons in the sampled PRs are highly consistent:

- "a reviewed, confirmed issue *is* the specification. The pipeline's assets … were carrying cost without carrying work" (NetPace #317)
- "it still installed 71 tracked files and injected 23 `speckit*` skills/commands into every agent session" (simonrowe #190; this PR was not merged, and the removal landed separately)

The common practice is to throw away the T2 process tooling and keep the T1 requirements gate and the constitution. This is almost isomorphic to UML's fate back then: Petre's 11 "selective users" also treated diagrams as thinking tools, discarded after use.

## 6. Claim Three: Can Specs Serve as Source Code?—Lessons from the Formal End

The strongest version of "spec as source code" has in fact already been run once in formal mathematics: there are machine verifiers there, and "the proof matches the statement" can be checked down to the last symbol. The problem is whether the statement itself expresses the intent of the original problem.

- **Two independent teams aligned ProofNet problem by problem** (an undergraduate math proof benchmark): on the 130 problems whose formal statements are verbatim identical, the two teams' judgments agreed 86.9% of the time (κ=0.74), and every problem one team judged wrong the other team also judged wrong, with no problems the other way round; the stricter team judged about 55% unfaithful, the more lenient team about 42%. Of these, 104–106 statements (about 28%) can be machine-proven false—the prover can "correctly" prove a wrong proposition [Multi-source confirmed, direction; specific numbers Single-source verified, with version].
- **One round of revision is not enough.** The already-revised ProofNet# version still has about 16–31% residual errors on an independent scale; miniF2F-v2, billed as "fully aligned," also has independent counterexamples (such as writing the cube root of −8 as 8, or omitting the condition n≥2).
- **Software specifications are the same.** Microsoft Research's AutoCLRS had agents write specifications, code and proofs for about 50 classic algorithms (about 100,000 lines), all passing machine checks; it then had agents write small concrete tests to probe the specifications, and the first round found substantive gaps in 8 of 52 algorithms—for example, the postcondition for Prim's algorithm accepts wrong output—and the authors say this is only a lower bound [Single-source verified].
- **Tests derived from a spec can be passed by an empty stub.** The authors of one study disclosed of their own work: an empty handler returning {} and 200 to every request passed all visible spec-derived tests (20/20) and held-out tests (12/12), while not one of 77 fidelity checks matched [Single-source verified, re-runnable].

The intent-formalization camp itself acknowledges this is the central bottleneck: "since there is no oracle for specification correctness other than the user" (Lahiri). Natural-language specs have one more layer than formal statements: they do not even have the "proof ⊢ statement" layer of checking. Böckeler's worry about spec-as-source—that it "might end up with the downsides of both MDD and LLMs: Inflexibility *and* non-determinism"—gets a mechanistic explanation here.

As for "reviewing specs is cheaper than reviewing code": in AutoCLRS about 5,000 lines of specification correspond to 100,000 lines of code and proofs, but this is a line ratio, not a labor-hour ratio; for 2024–2026 we found no controlled experiment directly comparing the labor hours or accuracy of "reviewing specs vs. reviewing code" [Unverified]. In a 5-person review pilot, giving reviewers a spec baseline did not make them find more problems (recall 0.525 vs. 0.518), and review time rose from about 27 minutes to about 48 minutes [Single source, blog].

The actual direction of the wind: Tessl, the most radical standard-bearer of spec-as-source, only released its first products in 2025-09 (a public beta of the Spec Registry and a closed beta of a framework), and has since pivoted to registering and distributing agent skills; its home page now says "agent enablement platform" and skills, no longer "specs generating code" [Single-source verified].

## 7. Who Is Talking, Who Benefits

- **The origin of the slogan.** "specs are the new code" was not said by OpenAI's Sean Grove; it is a URL fragment of his talk's event page. His actual words are "the coming of the new code, in particular specifications," referring mainly to OpenAI's Model Spec. He said "Code is sort of 10% to 20% of the value that you bring," without giving any source [Single-source verified, official transcript].
- **Attention does not equal use.** spec-kit has about 149,000 stars, and the PyPI package about 84,000 downloads in the last 30 days (including repeated CI installs); there are about 14,000 spec-kit constitution files on GitHub, against about 1.25 million AGENTS.md files in the same period—writing context files for agents is about two orders of magnitude more common than using SDD scaffolding [Field-verified, order of magnitude].
- **Vendors have acknowledged the cost through pricing.** In Kiro's 2025-08 pricing, the overage price for spec requests was 5 times that of ordinary requests ($0.20 vs. $0.04), later changed to unified credits [Vendor claim]. BMAD writes "Small changes go straight to build," and Spec Kit writes that not every change goes through the full process—the vendors themselves acknowledge that small tasks should not go through the full process. No vendor has published a controlled measurement of the effect of plan/spec modes on quality.
- **Enterprise cases.** The only one with numbers is Asana's self-report: after 7 engineers used a spec process for the first time, weekly PRs were +38%; the author acknowledges that PR count is an imperfect proxy, and there is no control group. As of 2026-11 there is no independent, controlled enterprise measurement [Vendor claim].
- **Surveys.** In DORA 2025, about 56% of practitioners who do the task of "writing specifications" already use AI assistance; but no large-sample survey has measured the workflow of "spec-first, handed to an agent" [Single-source verified].
- **Consulting judgments.** The 2026-11 edition of the Thoughtworks Technology Radar moved OpenSpec from Assess to Trial, while listing "AI-driven documentation sprawl" as Caution; Böckeler and the Radar both belong to Thoughtworks and cannot be counted as two independent sources.
- **Both sides of the debate have interested parties.** Marc Brooker, who defends SDD, is an AWS engineer (AWS makes Kiro); the HN commenter speaking up for plan mode in the discussion is a member of the Claude Code team; the con side's Marmelab examples come from its own employees and its own products.

## 8. Summary Table of Evidence Grades

| Claim | Grade | Note |
|---|---|---|
| The more completely intent is stated, the more successful the agent | Multi-source confirmed (direction) | What changes is information, not process |
| Plan before code is effective, shrinking as models get stronger | Single-source verified ×2 | MapCoder, Self-planning |
| Deriving a behavioral spec first when there is an execution oracle: +2.7–7.2pp, cost +48–130% | Single-source verified | SpecFirst |
| Tests in the prompt reliably raise function-level pass rates | Multi-source confirmed (direction) | Mostly upper-bound settings |
| TiCoder: test feedback makes judgments more accurate | Single-source verified (direction only) | Headline numbers dropped |
| Quality difference between the full SDD process and direct implementation | Unverified | Neither comparison passed the audit |
| The SDD process is slower and more expensive | Single-source verified (direction) + vendor pricing | Magnitude not load-bearing |
| Any number from the Uvik benchmark | Dropped | Methodology audit D |
| Open-source PRs with ticket numbers do not have fewer defects | Single-source verified + Field-verified | Not SDD evidence |
| Requirements traceability ↔ defects | Direction contested | Rempel vs. Hill |
| Public commit histories cannot measure spec drift | Single-source verified | Acknowledged by the dataset authors |
| Installing spec-kit does not mean using it | Single-source verified + Field-verified | Roughly 20–40% |
| Most practitioners self-report specs and code diverging | Single-source verified (qualitative) | Cannot be written as a proportion |
| Spec freeze rate, single-commit rate | Dropped | Construct validity does not hold |
| Formal benchmarks widely "proved correctly, but proved the wrong problem" | Multi-source confirmed | Two teams aligned problem by problem |
| Reviewing specs is cheaper than reviewing code | Unverified | No direct experiment |
| "Fix costs 1 in requirements, 100 after release" | Direction contested | Source is 1970s large projects |
| Royce 1970 | Single-source verified | Does not say "waterfall," wants more documentation |
| "specs are the new code" comes from Grove | Dropped (misquotation) | URL fragment |
| Kiro/Tessl/Spec Kit self-descriptions | Vendor claim | — |

## 9. Ten Testable Claims

Ordered by strength of evidence:

1. **Given the same information, the full process of an SDD tool does not produce better code than a single clearly written prompt.** Test: same agent, same model, multiple runs, three arms—no spec, the spec's content written into a single prompt, and the full Spec Kit/Kiro process—comparing pass rate, defects and cost on repository-level tasks; preregistered, with public logs. (Neither of today's two comparisons meets this)
2. **SDD's benefits are concentrated in multi-file, new-feature tasks, and are negative for bug fixes, refactoring and writing tests.** Test: in the design of claim 1, stratify by task type, with enough samples in each stratum to detect a 10-percentage-point difference. (Uvik reported this pattern, but its data was rejected)
3. **Most of the gain from writing a spec first can be reproduced by "reasoning first."** Test: add a "write reasoning first, no spec" arm and compare its gap with the spec arm.
4. **As models get stronger, the marginal benefit of planning first and writing a spec first shrinks.** Test: same benchmark, same process, repeated across three generations of models, to see whether the gain declines monotonically. (The reruns of Self-planning and TiCoder point the same way)
5. **Specs stop being updated at about the same rate as ordinary documentation.** Test: in repositories that do not use squash merges, compare the distribution of intervals from the last modification of spec files and of READMEs and design documents to the next related code modification.
6. **Divergence between spec and code happens mainly in the implementation phase, not the maintenance phase.** Test: for a set of active repositories, have independent reviewers annotate spec-code consistency at each feature merge, track longitudinally for 6 months, and separately count the inconsistency rate at merge time and afterwards.
7. **Test suites derived from specs are generally weaker than hand-written tests.** Test: for each SDD project, run an "empty-stub baseline" and mutation testing, reporting the empty-stub pass rate and the mutation kill rate.
8. **"Reviewing specs is cheaper than reviewing code" holds only when the specification is machine-checkable.** Test: the same group of reviewers, the same defect injection, randomly assigned to review a T1 spec, a T3 specification, or code, comparing detection rate and time taken.
9. **The finding that ticket discipline (rather than SDD tools) correlates positively with rework disappears after controlling for task difficulty.** Test: redo Hill's matching using independent task-difficulty annotations (rather than PR size), and fix its classifier bug.
10. **SDD tools will go the way of UML: keeping the habit of "writing things down clearly," dropping the tools and the process.** Test: two years from now, in the same set of repositories, count the share that still keep constitution/requirements documents but have removed the process tooling, compared with the shares that keep both and that remove both.

## Appendix: Methodology and This Issue's Self-Corrections

In the course of the research, this issue overturned or narrowed some claims we ourselves had initially accepted:

- "Royce invented waterfall / Royce opposed waterfall" → both wrong: the word is not in the original, and he considered phasing sound and asked for more documentation;
- "Boehm: fixing after release costs 100x or more than in the requirements phase" → median about 50–60x for large projects, about 2–4x for small projects, 1970s data, mixed units;
- "OMG: the platform-independent model contains all the information needed to drive the platform model" → this sentence is not in the original;
- "Hill proved SDD does not reduce defects" → it measured ticket numbers; after fixing the classifier bug, defects still show no difference, and rework is slightly higher;
- "Hill's results are consistent with prior research" → the cited prior works did not measure code defects, and an independent study points the opposite way;
- "Spec Kit Agents is the only direct comparison, proving no quality difference and +67% time" → unequal budgets and different survivors; only the direction "slower" remains;
- "Uvik: specs raise merge rate +8–12pp, halve defects, OpenSpec is cheapest" → not significant, and the raw data has three methodological contradictions; dropped;
- "TiCoder average improvement 45.97%, 15 professional developers, p<0.001" → 33.50pp recomputed from the same paper's table, participants include academics, and the p-value is impossible with 15 people;
- "76% of specs are never modified after installing spec-kit," "18% of specs frozen" → squash merges and archive renames invalidate commit counts, and the freeze rate is of the same order as READMEs;
- "80% of spec PRs also change code, showing specs and code are in sync" → mostly new specs merged together with the implementation;
- "LLM judges systematically overestimate formalization faithfulness by 8–41pp" → another setting in the same paper points the opposite way; direction contested;
- "specs are the new code (Grove)" → URL fragment of the event page;
- "Claude Code docs: skip planning if you can describe the diff in one sentence" → the current documentation has no such sentence;
- "Kiro 250,000 developers, specs cost 1.8x" → the original says ">100,000 people tried it in the first 5 days," and the overage price ratio is 5x;
- "Tessl raises the share of correct API usage by 35%" → the cited blog post has no such number.

Primary documents this issue could not obtain: the text of Bossavit's *Leprechauns of Software Engineering*, Boehm 1981's original book, the ACM original of Bell & Thayer 1976, the TSE version of Parnas & Clements 1986, the originals of Dijkstra EWD667 and Knuth 1984 (not used in this article), the Kemerer 1992 original, the full texts of Hebig 2016 and Zampetti 2020, the full text of Rempel & Mäder 2017 (direction only used, effect sizes not cited), the raw data of the TiCoder user study (not released), Uvik's task set and raw logs, and the code and data of Spec Kit Agents (not released). The related claims have been downgraded to secondhand or unverified.

## Appendix: Main Sources

**Pro side and mechanisms**: Jiang et al. 2024 "Self-Planning Code Generation with Large Language Models" (ACM TOSEM 33(7)), Islam et al. 2024 MapCoder (ACL 2024), ClarifyGPT (FSE 2024), Fakhoury, Lahiri et al. TiCoder (IEEE TSE 2024), Lahiri 2026 "Intent Formalization: A Grand Challenge…" (https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/; arXiv 2603.17150), Chen et al. 2026 SpecFirst (arXiv 2607.27167), Chacón Sartori 2026 "The Specification Gap" (arXiv 2603.24284), Deng et al. 2025 SWE-Bench Pro (arXiv 2509.16941), Taghavi & Bhavani 2026 Spec Kit Agents (arXiv 2604.05278), Endres et al. nl2postcond (FSE 2024)

**Con side and hands-on**: Hill 2026 "Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects" (ESEM 2026, LIPIcs; data https://github.com/brennhill/delivery-gap-research), Böckeler 2025 "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl" (https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html), Eberhardt 2025 "Putting Spec Kit Through Its Paces" (https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html), Zaninotto 2025 "Spec-Driven Development: The Waterfall Strikes Back" (https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html), Rempel & Mäder 2017 (IEEE TSE), Pirouzkhah 2026 (MSR)

**History**: Royce 1970 "Managing the Development of Large Software Systems" (Proc. IEEE WESCON), Bell & Thayer 1976 (ICSE), Brooks 1986 "No Silver Bullet" (UNC TR86-020), Boehm 1981 *Software Engineering Economics*, Bossavit's tracing notes, Menzies et al. 2017 (arXiv 1609.04886), OMG MDA Guide 1.0.1 (omg/2003-06-01), Petre 2013 "UML in Practice" (ICSE 2013), Hutchinson et al. 2011 (ICSE 2011), Whittle et al. 2014 (IEEE Software), Hebig et al. 2016 (MoDELS), Zampetti et al. 2020 (IST), Fucci et al. 2017 (IEEE TSE), Nagappan et al. 2008 (EMSE)

**The formal end**: ProofNet-Verified and ProofNet# (Poiroux et al.) audit data, ReForm ConsistencyCheck, miniF2F-v2, Swamy 2026 AutoCLRS (https://risemsr.github.io/blog/2026-03-06-autoclrs/), Swamy & Lahiri 2026 SPOTs (https://risemsr.github.io/blog/2026-04-16-spotting-specs/), Fawcett 2026 Rebuild Dossier (arXiv 2608.23616; https://github.com/Parker-Fawcett/rebuild-dossier)

**Vendors, adoption and measurement**: github/spec-kit (README, spec-driven.md, CONTRIBUTING.md @ f29319d; issue #1191), Fission-AI/OpenSpec, BMAD-METHOD, kiro.dev blog and pricing page, Tessl blog and TechCrunch coverage, Grove 2025 "The New Code" (AI Engineer World's Fair), Thoughtworks Technology Radar Vol.33–35, DORA 2025, Stack Overflow Developer Survey 2025/2026, Agarwal et al. 2026 "Spec-Driven Development as Prescribed and as Practiced" (arXiv 2608.25202) and the SpecMine dataset (doi:10.5281/zenodo.22102779), Uvik SDD benchmark page and raw CSV, Asana engineering blog, FrankRay78/NetPace PR #317, simonjamesrowe-dev-monorepo PR #190

**Related on this site**: specs are one kind of context written for agents; for the evidence on persistent context files, see ["The README for Agents: Are Context Files Infrastructure or Cargo Cult?"](https://hub.cissychen.com/deep-research/agent-readme-deep.en.html); reviewing specs and reviewing code are both verification-bottleneck problems, see ["AI Code Review: Cure for the Verification Bottleneck, or Turtles All the Way Down?"](https://hub.cissychen.com/deep-research/ai-code-review-deep.en.html) and ["The Machine-Judge Atlas: How Much Can LLMs Scale Software's Oracles?"](https://hub.cissychen.com/deep-research/machine-oracles-deep.en.html); for a post-mortem of the last wave of methodology transformation, see ["The '70% of Transformations Fail' Autopsy: Can the Last Wave's Post-Mortems Predict AI-Native?"](https://hub.cissychen.com/deep-research/seventy-percent-failure-deep.en.html); for the human-factors evidence on humans holding the final veto, see ["The Ironies of Automation: The Better the AI, the Faster the Human Veto Decays?"](https://hub.cissychen.com/deep-research/automation-irony-deep.en.html).
