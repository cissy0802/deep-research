# The "95% of AI Pilots Fail" Physical: Anatomy of a Viral Number, and the Real Base Rate of Enterprise AI (Deep Dive)

> The load-bearing claims in this essay went through 34 claim groups × 3 adversarial votes (102 votes: 34/34 survived, 0 overturned, 11 groups amended), with 4 single-source empirical groups additionally facing a contradiction-search seat and a methods-audit seat (8 verdicts: one universal negative downgraded, one "two-firm standoff" framing overturned by independent evidence and rewritten, one causal claim split and downgraded, one self-reported figure barred from standing next to RCTs). Counter-evidence stays in; citations carry their measurement definitions.

## 0. Two days, one sentence, a hundred billion dollars

On August 18, 2025, Fortune published a story headlined "MIT report: 95% of generative AI pilots at companies are failing." The next day, AI stocks pulled back: Nvidia fell 3.5%, Arm 3.8%, and Palantir plunged (Gizmodo recorded nearly −9%, Fortune nearly −10%). Several financial outlets tied the selloff to this "MIT report" — usually alongside a second trigger: Sam Altman had said that same week that investors as a whole were overexcited about AI. Gil Luria, an analyst at D.A. Davidson, offered a third reading: "This is really just the pendulum swinging back" — valuations were stretched, and this was mean reversion. No event study has ever apportioned the drop among those sentences; the attribution is narrative, not measurement.

Only one fact is certain: from that week on, "95% of enterprise AI pilots fail" became the most-cited statistic in the industry. It shows up in board decks, sell-side notes, and vendor marketing pages, and it is alive today.

The report is MIT Project NANDA's *The GenAI Divide: State of AI in Business 2025* — 26 pages, version v0.1, self-described as "Preliminary Findings." This essay does three things: dissects the report word by word; traces the number's year of mutation and the interests behind it; and then answers the better question — **what is the real failure rate of enterprise AI, and what does "failure rate" even measure?**

This is the second time this site has given a percentage a physical. The first was [The "70% of Transformations Fail" Autopsy](https://cissy0802.github.io/deep-research/seventy-percent-failure-deep.en.html), which closed by naming the next candidate zombie statistic to watch: "95% of AI pilots fail." Its number has come up.

## 1. Anatomy: what the report actually says

### 1.1 One sentence, three constructs

The birthplace of "95%" is the executive summary:

> "Despite $30–40 billion in enterprise investment into GenAI, this report uncovers a surprising result in that 95% of organizations are getting zero return. … Just 5% of integrated AI pilots are extracting millions in value, while the vast majority remain stuck with no measurable P&L impact."

Note the yardstick: **"95% of organizations getting zero return."** Yet the only 5% in the report that traces back to a data exhibit sits in Section 3.2 — a funnel for "embedded or task-specific GenAI tools" (custom enterprise tools): 60% of organizations investigated them, 20% reached pilots, 5% were successfully implemented. The comparison group, general-purpose LLM chatbots, runs 80% → 50% → 40%. The report then writes: "The 95% failure rate for enterprise AI solutions represents the clearest manifestation of the GenAI Divide."

Put the three side by side and you find **the same 95%/5% pair draped over three non-equivalent constructs**: ① 95% of organizations getting "zero return"; ② 5% of "integrated AI pilots" extracting millions; ③ 5% of task-specific tools reaching production in the funnel (whose base itself wobbles between "organizations" and "solutions"). These are not the same thing: a company whose custom tool never reached production is not a company with zero return — it may be saving real money with generic ChatGPT, which is exactly what the report measures elsewhere. The numerator quietly morphs from "did not reach production" into "zero return"; only through that rewrite do ① and ③ land on the same 95%.

That is precisely what Wharton professor Kevin Werbach caught. After reading the report multiple times, he wrote publicly:

> "There appears to be no further support for the 95% claim. … There is a 5% number in Section 3.2, for 'custom enterprise AI tools' being 'successfully implemented.' But that's much narrower. And successful deployment is defined as 'causing a marked and sustained productivity and/or P&L impact.' In other words, 'unsuccessful' explicitly does not mean 'zero returns.'"

A second conversion was exposed by the 80,000 Hours post-mortem: in the funnel, 80% of organizations **never piloted** a task-specific tool at all. Take "those who piloted" as the denominator and the success rate is 5/20 = 25%; most of the "pilots" in "95% of pilots fail" never happened.

### 1.2 Two definitions of "success," and "directionally accurate"

The Research Note on pages 6–7 defines success:

> "We define successfully implemented for task-specific GenAI tools as ones users or executives have remarked as causing a marked and sustained productivity and/or P&L impact"

— success is when someone **remarked** that impact was marked and sustained. An interview-impression yardstick, not a financial one. Appendix 8.2 supplies a second, different definition: "Success defined as deployment beyond pilot phase with measurable KPIs. ROI impact measured 6 months post-pilot." The two do not match; the report itself concedes "success definitions may differ across organizations," and states:

> "Research Limitations: These figures are directionally accurate based on individual interviews rather than official company reporting."

Plus a self-exemption almost nobody quotes: the six-month window "may be insufficient to fully assess 'successful deployment' for complex enterprise systems, potentially understating success rates." In other words, the number that erased a hundred billion dollars of market value is — by the report's own account — an interview-based, directionally-accurate preliminary estimate with a possibly-too-short window and a moving definition.

### 1.3 The sample: 52 + 153 + 300, reviewed by the fourth author

The NOTES page discloses the methodology: a desk review of 300+ publicly disclosed AI initiatives, structured interviews with representatives of 52 organizations, and survey responses from 153 senior leaders collected at four industry conferences. Research period: January–June 2025. The survey is a convenience sample gathered on conference floors, not a random draw; the appendix concedes "Selection bias possible."

Four authors are listed: Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari. The "Reviewers" line lists Pradyumna Chari and Project NANDA — Chari is the fourth author, reviewing himself. The report is not peer-reviewed, and access has been gated behind a Google Form from launch to this day; at the height of the frenzy, even journalists couldn't get the original, and mirror PDFs circulated via third-party sites. Rob Wiblin's verdict on the sample size at 80,000 Hours: "Flip one or two interviews the other way and you'd get a completely different headline."

### 1.4 The data in the report that points the other way

Buried under the headline is a set of measurements inside the report that run against the "AI is failing" narrative, and were almost never quoted:

- **The shadow AI economy**: "While only 40% of companies say they purchased an official LLM subscription, workers from over 90% of the companies we surveyed reported regular use of personal AI tools for work tasks. In fact, almost every single person used an LLM in some form for their work." The report even notes this shadow use "often delivers better ROI than formal initiatives."
- **The general-purpose funnel is a success story**: 80% → 50% → 40%, and elsewhere: "Generic LLM chatbots appear to show high pilot-to-implementation rates (~83%)."
- **Buying beats building roughly two to one** (~67% vs ~33% deployment) — immediately followed by the report's own caveat that "The correlation between external partnerships and success does not necessarily prove causation."

### 1.5 Numbers that disagree with each other

The report contradicts itself in at least three places: the executive summary counts 8 major sectors, the body counts 9; the share of AI budget captured by sales and marketing is "approximately 70 percent" in one passage and ~50% in another within the same section; personal AI use among knowledge workers is "over 40%" on one page and "almost every single person" at 90% of companies on another. A 26-page draft that cannot reconcile its own numbers became 2025's most-cited source of enterprise AI statistics.

## 2. Mutation: a number's first year

### 2.1 Mutated on arrival

Viral distortion is usually imagined as drift at the end of a long chain. Not here — **the first story changed the yardstick**. Fortune's headline turned "95% of organizations getting zero return" into "95% of pilots are failing"; its body copy described the methodology as "150 interviews with leaders, a survey of 350 employees, and an analysis of 300 public AI deployments." A full-text search of the only public version, v0.1, finds no 150 and no 350; the report's own account is 52 organizations interviewed and 153 senior leaders surveyed (whether some unpublished version contained those numbers cannot be verified). Fortune not only inflated the sample two- to three-fold — it turned "153 senior leaders" into "350 employees," drifting the respondents' identity too. Dozens of outlets copied the numbers; no correction has ever run, and many 2026 citations still carry Fortune's version.

### 2.2 The variant family

Nine variant classes are traceable along the chain. Highlights:

- **V0 (original)**: "95% of organizations are getting zero return."
- **V1 (Fortune's headline)**: 95% of pilots are failing — organizations become pilots, zero return becomes failing.
- **V3 (Entrepreneur)**: "Nearly 95% of Companies Saw Zero Return on In-House AI Investments" — an invented "in-house" qualifier, when the report actually found external partnerships succeed more.
- **V5/V6 (terminal generalization)**: "95% of Enterprise AI Fails" → "95% of AI projects fail" — every qualifier (generative, pilot, P&L, six months) shed.
- **V7 (institutional upgrade)**: an FT column rendered it as "Recent research led by Aditya Challapally at the MIT Media Lab" — a project team's preliminary report promoted, step by step, into MIT Media Lab research.
- **The 2026 hybrid generation**: long-tail content now carries a sourceless "90% of enterprise AI implementations fail" — 95% (NANDA) crossbred with 80% (RAND's borrowed estimate) in the content farms.

### 2.3 The control group: numbers routinely mixed with the 95%

"Failure-rate dashboard" articles line the 95% up with a family of other figures. Restored to their actual terms, one by one: **S&P Global 451**: "The share of companies abandoning most of their AI initiatives jumped to 42%, up from 17% last year" — the subject is companies, not projects (n=1,006, North America + Europe, fielded October–November 2024), and the same survey found the average organization scraps 46% of its PoCs before production. **Gartner**: "At least 30% of generative AI projects will be abandoned after proof of concept by the end of 2025" — a July 2024 prediction, future tense; in 2026 Gartner revised its own account to over 50% actual, while the articles that had cited the prediction as an accomplished statistic never went back to fix it. **RAND**: "By some estimates, more than 80 percent of AI projects fail" — an estimate RAND borrows in its opening; RAND's own work interviewed 65 practitioners to catalogue root causes, and measured no failure rate. **IBM**: "only 25% of AI initiatives have delivered expected ROI" — self-reports from 2,000 CEOs, project-level denominator, own-expectations yardstick. Five numbers, five denominators, all traded as one "AI failure rate."

### 2.4 The afterlife, 2026

As of July 2026: NANDA has published no sequel and no revision, the underlying data has never been released, the report still circulates as v0.1, the MIT Media Lab NANDA group's publications page does not list it, and there has been no retraction, no disclaimer, no author correction. The number itself is thriving — its most energetic citers are vendors with something to sell ("MIT says 95%…" as the opening line of data-governance and platform pitches), while a minority of citers (e.g., Pertama) retain the original qualifiers. The most systematic reckoning of 2026 came not from academia or MIT but from the 80,000 Hours podcast, whose verdict: "an opaque, conflicted, barely-scrutinised report managed to attract the MIT label, move markets and have a vast impact on global opinion about AI."

## 3. Interests: who wrote it, and what they sell

### 3.1 The prescription at the end of the diagnosis

Project NANDA stands for Networked Agents And Decentralized Architecture — an agent-protocol project founded at the MIT Media Lab by professor Ramesh Raskar, positioning itself as "TCP/IP for AI": agent registry, discovery, reputation, and payments infrastructure. The report's core thesis: GenAI pilots fail because the tools don't learn ("The core barrier to scaling is not infrastructure, regulation, or talent. It is learning"), and the cure is agentic AI with memory and adaptation. The report's own body twice lists NANDA alongside MCP and A2A as the infrastructure for that transition; §6.5 envisions agents that will "execute trustless transactions through blockchain-enabled smart contracts"; the concluding chapter advises enterprises to "start partnering with vendors."

The 80,000 Hours post-mortem says the quiet part: the four authors are "all either currently developing or trying to sell" the class of agentic frameworks the report recommends, and the report was "marketed under the MIT brand with no conflict of interest disclosure." The NOTES-page claim that anonymization exists to "prevent any perception of commercial advancement" coexists with the protocol's name appearing three times in the text.

### 3.2 Named critics, zero response

The critics' roster is long and on the record: Werbach demanded NANDA "release the full supporting data. If not, it should retract the report"; Paul Roetzer of the Marketing AI Institute called it "not a viable, statistically valid thing"; Oxford fellow Ajit Jaokar called it "a clever marketing gimmick"; Futuriom's chief analyst Raynovich called it "irresponsible and unfounded," countering with his firm's database of 130+ enterprise case studies. A year on, the response to all of it: zero.

### 3.3 MIT's other number

MIT produced two breakout enterprise-AI numbers in 2025. The other pointed the opposite way: a doctoral paper claiming AI accelerated materials discovery, endorsed by senior economists and cited in Congress — until May 16, 2025, when MIT's economics department publicly stated it had "no confidence in the provenance, reliability or validity of the data and has no confidence in the veracity of the research," requesting withdrawal from arXiv and from consideration at the QJE (critics allege fabrication; the paper was never published). Both of the year's most viral "MIT numbers" — one bearish, one bullish — failed the methods physical. The lesson is not "distrust MIT"; it is that **institutional branding carries no methodological guarantee, and positive findings need autopsies exactly as much as negative ones.**

## 4. The yardstick war: 90% success and 90% failure, simultaneously true

Lay out the major "enterprise AI returns" numbers of 2024–2026 and the two ends of the spectrum sit ninety percentage points apart. Restore each report's terms, and the machinery of the war becomes legible.

### 4.1 How the vendors' warm numbers are manufactured

**Microsoft/IDC's "$3.7x per $1"** (Nov 2024, the workhorse of Copilot marketing): underneath is a self-estimate multiple-choice question — "What would you estimate your organization's ROI is for every $1 spent on generative AI projects or initiatives?" — with answer buckets of 1x/2x/3x/4x/5x/5x+, "not sure" excluded from the denominator, and respondents who are themselves the people "responsible for bringing AI transformation to life" — grading their own projects. Only **1%** of the sample answered "No ROI." The companion claim that "top leaders realize 10.3x" is circular by construction: "Top leaders are 18% of the leaders who realize more than 5x return" — filter people by their returns, then announce that their returns are high.

**Google Cloud's "74% achieve ROI within the first year"** (Sept 2025): the denominator includes only companies with $10M+ revenue **that have already deployed generative AI** — the never-boarded and the boarded-then-quit are absent by construction. The report carries a coincidentally identical breadth metric: 74% see ROI on at least one use case (88% among early agentic adopters). One 74% is a time metric, the other a use-case metric; the marketing collapses them into one sentence. As for revenue: 56% self-report business growth, of whom 71% report higher revenue, of whom 53% estimate gains of 6–10% — multiply the nesting dolls and you get roughly a fifth of the full sample.

The vendor side has its dissenters: Anthropic's Economic Index reports usage structure and makes no return-multiple claims; AWS's adoption survey likewise avoids the ROI question. The multiple-asserters are precisely the two selling Copilot and cloud.

### 4.2 The consultancies' cold numbers, and the eerily convergent "elite few"

**McKinsey** (Nov 2025, n≈2,000): 88% of organizations use AI in at least one function, but "Meaningful enterprise-wide bottom-line impact from the use of AI continues to be rare" — about 39% attribute any enterprise-level EBIT impact to AI (most below 5%), and the "AI high performers" who both attribute ≥5% of EBIT to AI and self-assess significant value are about 6%.

**BCG** (Sept 2025, n=1,250): 5% of companies achieve AI value at scale; 60% report no material value. The methods section contains a rare self-disclosure: "Unless explicitly stated as realized…reported numbers reflect expected future impact. … responses may be subject to perception bias." — unless marked "realized," the numbers are **expectations**, with admitted perception bias.

**Deloitte** wears two faces: its Q4-2024 wave found nearly three-quarters of initiatives meeting or exceeding ROI expectations — asking each respondent only about their **most advanced** initiative, against their own expectations, with AI stakeholders as respondents; its 2025 Europe/Middle East study found only 6% achieve payback within a year, with typical payback of 2–4 years. Same firm, different question, warm to cold.

**IBM** (May 2025, 2,000 CEOs): only 25% of AI initiatives delivered expected ROI and 16% scaled enterprise-wide; in the same report, 85% of CEOs expect positive ROI by 2027, and 64% admit fear of falling behind drives investment "before they have a clear understanding of the value." Failure is present tense; success is permanently future tense.

**PwC** (Jan 2026, 4,454 CEOs, actual-results yardstick over the trailing year): "56% report neither increased revenue nor lower costs from AI over the past 12 months"; 22% say costs went up; only 12% achieved both revenue gains and cost reductions.

**Bain** (June 2026, 951 companies with $100M+ revenue, counting only firms that actually measured outcomes): "The technology worked. The value didn't arrive." 37% of companies set cost-reduction targets of 11–20%; among those that measured, nearly 40% landed at 0–10%. The sharpest finding is the funding structure: 44% of large enterprises cite **savings from prior automation programs** as the funding source for the next GenAI/agentic wave — savings Bain's analysis finds systematically underdelivered; and about 90% of those same companies are increasing their budgets again, this time for AI agents. Betting the next round with savings that never arrived is expectation rolled forward.

Note how the consulting side's "elite few" converges: BCG 5%, McKinsey 6%, Accenture 8% (front-runners), PwC 12%. That may be the true base rate; it also fits, perfectly, the "few succeed — you need help" narrative that sells transformation services. The two explanations are not mutually exclusive.

### 4.3 Whoever answers, owns the answer

Wharton and GBK's *Accountable Acceleration* (Oct 2025, n≈800 US enterprise decision-makers) was widely framed by the media as the counterweight to NANDA (the report and press release never name MIT; Wharton's Puntoni was plain in an interview: "Our definition is very different from the MIT report. Theirs is much more stringent."). It found nearly three-quarters of decision-makers "already see positive ROI." The operative words are perceptions and believe — a perception yardstick. And inside the same dataset lives the micro-mechanism of the whole war: **81% of VPs and above believe ROI is positive, versus 69% of mid-managers.** Twelve points of seniority gradient — and most surveys ask only the executives. S&P's sample includes mid-level staff, and its numbers run colder; KPMG's ~130-person quarterly panel swung agent deployment from 11% to 42% to 26% within a year. Who answers, and how you ask, is part of the measurement.

### 4.4 The ladder of yardsticks

Six dimensions explain nearly all of the war: **denominator** (projects / organizations / your best project / at least one use case), **yardstick** (self-estimated multiple < met own expectations < perceived positive ROI < measured revenue-or-cost results < EBIT attribution < marked P&L acceleration), **sample admission** (surveying only deployers = deleting the failed exits), **respondent seniority**, **time window**, and **self-report versus measurement**. Each notch of yardstick severity drops the "success rate" a tier: IDC's 99%-report-ROI → Deloitte's best-project 74% → Wharton's perceived 74% → IBM's project-level 25% → PwC's measured 12% → McKinsey's high-bar 6% → BCG's at-scale 5% ≈ NANDA's pilot-to-P&L 5%.

Once the ladder is visible, NANDA's position is clear: **its 5% is not an outlier at the strict end** — it sits in the same band as McKinsey's 6%, BCG's 5%, PwC's 12%. Its sin was never direction. It was reporting a single-digit-precision percentage from a 52-interview convenience sample, rewriting "no marked P&L impact" as "zero return," and letting the media promote that into "AI is failing." On the same ladder, Wharton's 74% and McKinsey's 6% do not contradict each other — they are different rulers; the "95% versus 74%, who's lying?" debate is itself a failure to read the rulers.

## 5. Independent measurement: three facts from official statistics and registry data

Step outside the vendor and consulting questionnaires, and the picture from official statistics and academic registry data compresses into three phrases: adopted fast, used shallow, used in hiding.

### 5.1 Adopted fast

The Bick–Blandin–Deming RPS surveys (US population-representative) find generative AI reached ~53% adult adoption in three years — faster at the same age than the PC or the internet; the November 2025 wave puts adult adoption at 54.6% and at-work use at 37.4%. Census BTOS (a sampling frame of ~1.2 million firms) has the firm-level curve rising from 3.7–3.8% in September 2023 to ~18% by end-2025 (employment-weighted ~32%) — but citing that official curve requires a footnote: **from November 2025 the question was widened from AI use "in producing goods or services" to use "in any business function,"** and both Census and the Fed acknowledge in writing that part of the later rise is measurement effect.

### 5.2 Used shallow

The same official data: among US firms that adopted AI, 57% use it in three or fewer business functions; among firms reporting task effects, about 66% use AI purely to augment rather than replace; roughly 2% of AI-using firms cut employment because of it (Census working paper, Nov 2025–Jan 2026 window). Euro area: ~71% of firms say they use AI (experimental use included), but the ECB's June 2026 assessment is that intense use is only about 7% — "The intensive use that drives transformation…remains rare." The payments lens agrees: paid AI adoption among Ramp's client firms crossed 50% in March 2026 (50.4%, from 35% a year earlier), yet by June the **median** firm's AI spend was $11.38 per employee per month, against $7,449 for the top 1% — "paid adoption above half" and "most firms spend almost nothing" are simultaneously true.

On the outcomes side, the best causal evidence also says "shallow": RPS respondents report AI-driven time savings equal to about 1.6% of total work hours. Denmark's population-wide administrative registers (Humlum & Vestergaard; 11 exposed occupations, ~25,000 workers × ~7,000 workplaces) deliver a precise zero on pay and hours — "precise null effects on earnings and recorded hours…ruling out effects larger than 2%" (measured two years after the launch of ChatGPT); adopters self-report saving about 3% of work hours, an order of magnitude below task-level RCTs (e.g., +15% in the QJE customer-support experiment). The March 2026 revision retitled the paper "Still Waters, Rapid Currents" and re-centered the explanation on "structure moves first, pay moves later": tasks are being reorganized, new AI-adjacent tasks are spreading, workers are drifting toward AI-related occupations — none of it yet visible in paychecks. The macro level points the same way: Goldman Sachs's own economists concluded in March 2026 that "We still do not find a meaningful relationship between productivity and AI adoption at the economy-wide level" (a house counterpoint to the firm's 2023 forecast that AI could lift global GDP 7% over a decade); the bright spot in their read — median gains around 30% in customer service and software development — comes from the self-reports of the few companies that volunteered quantified numbers on earnings calls, not from independent measurement; and by Goldman's count, about 1% of the S&P 500 has quantified AI's impact on earnings.

### 5.3 Used in hiding

A Fed note of April 2026 names the three official numbers that disagree at the same point in time: BTOS firm-level ~18%; RPS worker self-report ~41%; the Atlanta Fed SBU's employment-weighted rate around 78% (employment weighting approximates the share of the labor force working at firms that have adopted AI). One of the Fed's explanations is **information asymmetry between respondents**: employees use AI on personal accounts, and executives can't see it. The KPMG–University of Melbourne survey of 48,000 people in 47 countries supplies the mechanism: **57% of employees hide their AI use from employers and present AI output as their own**, and nearly half admit uploading sensitive material to public tools. NANDA's own 90% (personal use) versus 40% (official subscriptions) gap — methodologically its weakest number — points the same direction as the official data: **the firm-level statistic measures official deployment, not actual use.** "95% of pilots fail" and "everyone is using AI" therefore do not contradict each other: what fails is the P&L attribution of formal projects; what thrives is the shadow use no statistic captures.

## 6. Historical base rates: the 95% in a thirty-year lineage

"A high failure rate + an authoritative byline + seller-side distribution" was not invented for AI. The autopsies, one per specimen:

- **Standish CHAOS (from 1994, "only 16% of software projects succeed")** — the same company's data can swing between 5.8% and 94.2% "success" under its definitions, and the chairman conceded the figures should be treated as opinion. Full anatomy in [The "70% of Transformations Fail" Autopsy](https://cissy0802.github.io/deep-research/seventy-percent-failure-deep.en.html); not repeated here.
- **"85% of big-data projects fail" (2017)** — the entire evidentiary basis is one personal tweet by Gartner analyst Nick Heudecker ("closer to 85 percent"), since deleted; Gartner's formal prediction read "Through 2017, 60 percent of big-data projects will fail to go beyond piloting and experimentation and will be abandoned" (made in 2015, future tense). A deleted tweet was cited as "Gartner research" for nearly a decade.
- **"85% of AI projects fail" (2018)** — Gartner's sentence was "Through 2022, 85 percent of AI projects will deliver erroneous outcomes due to bias in data, algorithms or the teams responsible for managing them": a prediction that **bias would cause erroneous outcomes** (nearly a truism), mutated in circulation into a measured failure rate. Tom Davenport's verdict: it "actually has no data at all on what percentage of projects fail."
- **Cisco's "close to three-fourths of IoT projects are failing" (2017)** — its own data: 60% of initiatives stalled at PoC, and 26% of surveyed **companies** had ever had an IoT initiative they considered a complete success; the headline's 74% is 100 minus 26, with every not-completely-successful company booked as failing. By the completed-projects yardstick, about two-thirds were considered successes; and 64% of respondents said learnings from stalled or failed pilots accelerated their investment.
- **"Manufacturing is stuck in pilot purgatory" (2018–2021)** — the McKinsey-side numbers: 84% (2018, "companies working in IoT," via IndustryWeek's retelling), 56% (2019, manufacturers) / 74% (2020) — the latter two via LNS's citations, primaries unverified; rival LNS Research measured 13% (2019) and 7% (2021) and publicly called the narrative "fake news." Yet the high side has independent same-direction support (BCG: 71% not beyond pilot at scale; IDC: of every 33 AI pilots, 4 reach production; the WEF's 1,000+-site census: >70%; Capgemini: ~86%), while LNS's 7–13% is an isolated low value built on a narrower construct — it counts companies that ticked "stuck in pilot with unclear results" among their top-three challenges. Both sets of numbers are real; the gap is a **one-directional definitional mismatch**, not a measurement stalemate. What the pair proves is that the failure rate is a function of the question.
- **"80–90% of new products fail"** — Castellion & Markham 2013 (JPIM), reviewing the empirical literature since 1977: measured failure runs about 40% or lower; the 80–90% claim is an urban legend sustained for decades by argumentum ad populum and seller self-interest.

The lineage also contains a **verbatim twin**. Harvard Business School's Shikhar Ghosh studied 2,000+ venture-backed startups; the WSJ's 2012 rendering: "If failure is defined as failing to see the projected return on investment…then more than 95% of start-ups fail." The same companies fail at 30–40% by liquidation, 65–75% by capital-not-returned, 95% by projected-ROI — tighten the definition a notch and the number doubles. Drug development behaves identically: Phase I-to-approval success is 9.6% on BIO's method and 13.8% on Wong et al.'s path-by-path method — a 44% relative gap attributed mainly to methodology (the paper's own wording is "may be due to"), with the data windows and databases differing too. Nobody concludes from nine-in-ten failed candidates that "pharma doesn't work"; a high failure rate there is understood as **the shape of a funnel**, not a death sentence for the industry.

Directly measured, the base rate of outright IT project abandonment is far lower than the folklore: Sauer, Gemino & Reich's 412 UK projects showed 9.2% abandoned and about 67% delivering close to expectations; a meta-review of 28 surveys spans 6.87–31.1% abandonment. Flyvbjerg's 5,392-project database shows overruns and underruns "about equally frequent," median and mode near zero, mean about +80% — **a fat tail, not majority failure**.

Three conclusions fall out of the lineage. First, as a pilot-to-scale funnel number, 95% is unremarkable — it is verbatim-identical to the VC ROI yardstick and shape-identical to drugs, new products, big data, and IoT. Second, read as "AI projects are being wiped out," 95% contradicts every historical measurement — measured outright-abandonment has always run between one and three in ten. Third, and most important: **these failure-rate numbers almost never measure what they claim to measure** — they measure forecast bias (Standish), a bias prediction (Gartner's 85%), "not a complete success" (Cisco), self-selected definitions (LNS/McKinsey), a pass bar set at perfection (Ghosh's 95%). And why does debunking never kill them? Letrud & Hernes 2019 quantified it: among papers citing the debunking literature, 468 still affirmed the myth and only 40 rejected it — twelve to one. The debunkings became carriers.

## 7. Theory: four readings, four incompatible prescriptions

Your theoretical prior decides what you read the 95% as. Four frameworks, four readings, incompatible prescriptions.

### 7.1 The J-curve: this is what the bottom looks like

Brynjolfsson, Rock & Syverson's Productivity J-curve (AEJ: Macroeconomics 2021): general-purpose technologies demand massive intangible complementary investment (process redesign, data, training) that national accounts book as cost, not output, so a new GPT's early productivity is systematically underestimated and its harvest later overestimated. The key prediction, verbatim:

> "In fact, the more transformative the new technology, the more likely its productivity effects will initially be underestimated."

Under this frame, "95% with no measurable P&L impact" is the model's **defining prediction for the dip, not a counterexample**. The paper closes by inverting Solow: "in the future…we will see new technologies everywhere including the productivity statistics."

The mechanism has independent confirmation — with corrections: a KU Leuven team confirmed an intangibles-driven firm-level J-curve in Belgian B2B microdata, but sized the TFP underestimate at roughly 3% (against BRS's 15.9% headline) and found the bias concentrated in small, young firms — the opposite heterogeneity from the US evidence; international replication splits (present in Korea, absent in France and Japan). The most-cited "causal confirmation" is a Census working paper (CES-WP-25-27, April 2025, Brynjolfsson co-authoring): in US manufacturing microdata, the authors report causal evidence of J-curve-shaped returns, with short-run losses concentrated in older firms, about a third of which trace to abandonment of structured management practices. The methods-audit seat downgraded it on several counts: not peer-reviewed, built on confidential data others cannot re-run, identified by an instrumental variable whose exclusion restriction the authors concede can never be directly tested, with the upward arm resting on between-group comparisons of surviving firms; it measures **pre-2021 industrial and predictive AI, not GenAI**, in manufacturing only; and its J-curve reflects real production disruption ("rather than primarily mismeasurement") — the opposite pathology from BRS's measurement story. Same shape, different disease. An independent attempt on Statistics Canada microdata found no J-curve.

In February 2026 the standoff got its cleanest week: Brynjolfsson declared the US "transitioning out of this investment phase into a harvest phase" (basis: 2025 productivity growth of ~2.7%, nearly double the decade average), while a day earlier Apollo's chief economist Torsten Slok wrote "AI is everywhere except in the incoming macroeconomic data." Same macro data, opposite conclusions; the 2.7% carries no causal AI attribution. "Emerging from the dip" is, for now, a live dispute — not a fact.

### 7.2 Absorptive capacity: failure isn't random, and some never make it

Cohen & Levinthal 1990 (ASQ) define absorptive capacity as the "ability to recognize the value of new, external information, assimilate it, and apply it to commercial ends" — a function of prior related knowledge, produced as a **byproduct of doing your own R&D and operations; it cannot be bought**. The harshest prediction is lockout: a firm that stops investing in absorptive capacity in a fast-moving field "may never assimilate and exploit new information in that field, regardless of the value of that information."

This framework meets the NANDA report in one head-on collision. NANDA's diagnosis — "The core barrier to scaling is not infrastructure, regulation, or talent. It is learning." — reads, on its face, like absorptive capacity. But NANDA assigns the learning to **software** (tools should have memory and adapt), while the C&L tradition assigns it to the **organization** (prior knowledge, routines, gatekeepers); a full-text search of the report finds no "absorptive" anywhere. One word, two opposite purchase orders: buy tools that learn, or build an organization that learns. The report's authors sell the former. Bresnahan, Brynjolfsson & Hitt's classic three-way complementarity (QJE 2002) sides with the latter: IT's returns arrive only bundled with workplace reorganization and new products — technology alone doesn't pay. Under the absorptive-capacity reading, the 95% does not self-correct — failure concentrates in organizations lacking the prior stock, and some of them lock out permanently.

### 7.3 Acemoglu: the 95% may be the ceiling's shadow

Acemoglu 2024 (NBER w32487) computes AI's ten-year TFP gain at "no more than a 0.66%" — twice flagged by him as an **upper bound** — and below 0.53% after discounting hard tasks. The paper names its targets: far below Goldman's +7% global GDP and McKinsey's $17–26 trillion. His 2030 forecast: "most companies are going to be doing more or less the same things." On this reading, pilots failing to move P&L is **a small effect being measured correctly** — not an artifact, and ten years of waiting will not produce a J-shaped rebound; the high failure rate reflects limited economic value plus a wrong direction (too much automation, too little augmentation).

### 7.4 The electrification rhyme: 1900's own 95%

Paul David (AER P&P 1990), writing on the Solow paradox, planted the flag a century back: "In 1900, contemporary observers well might have remarked that the electric dynamos were to be seen 'everywhere but in the productivity statistics!'" (dynamos — generators). Electrification took roughly forty years from the first central power station (1880s) to visible manufacturing productivity (early 1920s); the proximate cause of delay was that still-serviceable old plants weren't worth demolishing — until the unit drive made single-story factories, optimized material flow, and flexible wiring possible, which in turn required "building up a cadre of experienced factory architects and electrical engineers" (David, drawing on Devine 1983). The bulk of the gains never came from cheaper power; they came from redesigned workflows — rhyming with today's survey finding that only 21% of organizations have redesigned theirs. Solow's sentence is from the New York Times Book Review of July 12, 1987 ("We'd Better Watch Out," p.36); thirteen years later, Oliner & Sichel 2000 ruled that IT use plus computer manufacturing together explain about two-thirds of the late-1990s productivity acceleration (~1 percentage point) — "information technology largely is the story." The last paradox closed its loop. But the ECB's Lane (March 2026) adds a modern correction: GPT diffusion has been speeding up in recent decades, so the forty-year benchmark may be systematically slow.

### 7.5 How four readings coexist

The frameworks split on two diagnostics: **does the failure self-correct** (J-curve and electrification: yes, once complements arrive; absorptive capacity: no — lockout; Acemoglu: no — the pool is shallow), and **where is the problem** (J-curve: measurement artifact; electrification: real but necessary reconstruction cost; absorptive capacity: organizational deficit; Acemoglu: a technology ceiling). They cannot all be right — the J-curve says the more transformative, the more underestimated early; Acemoglu says the early evidence overestimates the future (easy tasks come first) — but they can each be right about one layer: task-level gains are real (repeatedly replicated in RCTs), enterprise-level attribution is broadly absent (5–12% at strict yardsticks), and macro-level signal is so far missing (BLS, Fed, Goldman pointing the same way). Which framework wins is exactly the question of whether transmission across those three layers happens. Commentators have already run NANDA's number through these frames (Rasmus via Solow; Sequoia via the J-curve — note the VC's book); as of July 2026, no peer-reviewed paper has tested the 95% itself.

## 8. Verdict: the real base rate of enterprise AI

Back to the question this essay owes an answer: what is the base rate of transformation difficulty? The honest answer is layered:

| What you want to measure | Best available measurement | Number |
|---|---|---|
| Executives perceiving positive ROI | Wharton n≈800 (2025) | ~74% (VP+ 81%, mid-managers 69%) |
| Organizations self-reporting positive impact on some objective | S&P VotE (Oct 2025) | 70–76%, declining year over year |
| Initiatives meeting own expected ROI | IBM, 2,000 CEOs (2025) | 25% |
| Measured revenue gains + cost cuts, trailing 12 months | PwC, 4,454 CEOs (2026) | 12% |
| ≥5% enterprise EBIT attributed to AI, with significant value | McKinsey n≈2,000 (2025) | ~6% |
| Achieving AI value at scale | BCG n=1,250 (2025) | 5% |
| Custom-tool pilot → marked P&L (6-month window) | NANDA n=52+153 (2025) | 5% (weakest method) |
| Companies abandoning most AI initiatives | S&P n=1,006 (2025) | 42% (17% a year earlier) |
| Historical outright IT-project abandonment | 28 academic surveys | 7–31% |

Three judgments this essay is prepared to sign:

First, **the sentence "95% of organizations are getting zero return" does not hold** — the report's own success definition (short of "marked and sustained" ≠ zero), its own shadow-AI data (workers at 90% of companies using AI, which "often delivers better ROI"), and its own general-purpose funnel (~83% pilot-to-implementation) all refuse it. It is a narrow funnel statistic repackaged as a general verdict.

Second, **as a strict-yardstick funnel number, the 5% is directionally credible** — it converges with McKinsey's 6%, BCG's 5%, and PwC's 12% at the ladder's end, and matches the pilot-survival shape of VC, drugs, new products, and IoT. The true picture of enterprise AI is not "mass failure" but **concentration at the head**: a few organizations winning by hard standards, most using AI broadly and shallowly, and the outcome signal in official statistics doubly diluted by shadow use and lag.

Third, **in this industry, "failure rate" is rhetoric first and measurement second**. From Standish through the 85% tweet to the 95%, across thirty years, the producers of the numbers have almost always been sellers of the cure. When the next viral failure rate arrives, the same three questions apply: What is the denominator? What is the yardstick? What does the person telling you this sell?

## 9. Closing: twelve testable claims

Ordered from hardest to softest evidence; each with its check.

1. **The NANDA executive summary's sentence is "95% of organizations are getting zero return," while the report's only traceable 5% is the task-specific tool funnel (60→20→5)** — non-equivalent constructs; verifiable verbatim in the first-hand PDF. [Multi-source]
2. **The report's own sample is 52 organization interviews + 153 conference-surveyed senior leaders; Fortune's launch story said 150 interviews + 350 employees, numbers absent from the only public version v0.1, with no correction to date.** [Multi-source; "any version" unprovable, hence scoped to the public one]
3. **The report's "success" is an interview-remark yardstick ("users or executives have remarked…"), with a second, inconsistent KPI+6-month definition in the appendix; the report itself calls the figures only "directionally accurate."** [First-hand]
4. **The report carries an undisclosed interest structure**: the body twice lists NANDA as solution infrastructure, the conclusion advises "start partnering with vendors," and 80,000 Hours records all four authors developing or selling the recommended class of agentic frameworks. [Multi-source]
5. **As of July 2026: no sequel, no data release, no correction; the MIT Media Lab NANDA group's publications page does not list the report.** [Live-checked]
6. **Independent strict-yardstick measurements converge on 5–12%** (McKinsey ~6%, BCG 5%, PwC 12%, IBM 25% mid-band) while perception yardsticks converge on 70–80% (Wharton; S&P per-objective) — different instruments, and the yardstick ladder explains nearly the whole spectrum. [Consulting self-report, terms verified per report]
7. **Official statistics: fastest adoption on record, shallow use** — RPS 53% in three years; BTOS ~18% by end-2025 (including a question-widening effect); 57% of adopting firms confine AI to ≤3 functions; self-reported time savings ~1.6% of work hours; ECB intense use ~7%; Ramp median spend $11.38 per employee per month. [Official/independent]
8. **Danish registry data delivers a precise null on pay and hours (ruling out >2%), and macro productivity shows no AI-attributable signal** (BLS series, Fed, Goldman's own research pointing the same way). [Peer-reviewed track + official; multi-source]
9. **Shadow use systematically depresses the firm-level statistic**: at the same time point, BTOS 18% vs RPS workers 41% vs SBU employment-weighted ~78%; 57% of employees report hiding their AI use. [Official + large survey]
10. **The 95% has a verbatim twin**: by the "failed to see projected ROI" yardstick, "more than 95% of start-ups fail" (Ghosh/WSJ 2012); drugs, new products, big data, and IoT share the funnel shape — high pilot mortality is the normal form of experimental portfolios, not an AI disease. [Peer-reviewed + multi-source]
11. **Historical failure-rate numbers almost never measure what they claim**: the big-data 85% was a deleted tweet; the AI 85% a mutated bias prediction; Cisco's 74% counted "not a complete success" as failure; the pilot-purgatory gap is a one-directional definitional mismatch (high side independently multi-sourced, low side an isolated narrow construct). [Multi-source]
12. **The four theoretical readings (J-curve / absorptive capacity / Acemoglu's ceiling / electrification rhyme) give incompatible answers to "will the 95% self-correct"**; the Census J-curve causal evidence concerns last-generation industrial AI and carries methodological reservations — the GenAI-era test does not yet exist, and is the most watch-worthy empty cell of the next five years. [Theory + downgraded single source]

**What to watch**: whether NANDA ever releases its data or a sequel (two years of silence make it unlikely — but it is the only route to re-measuring the 95%); whether the BLS productivity revisions of 2026–27 show an AI-attributable acceleration (the adjudication point of Brynjolfsson vs. Slok); whether Gartner revises again after moving "at least 30%" to "over 50%"; whether Bain's "funding the next wave with savings that never arrived" structure produces its first named blowups in the 2027 budget cycle; and the next viral failure-rate number — on this lineage's cadence, it is already on its way.

## Appendix: principal sources

**Report and critiques**: NANDA *The GenAI Divide* v0.1 (mirror PDFs); Werbach's LinkedIn essay (via Futuriom); the 80,000 Hours post-mortem (2026-04-28); Futuriom; Pivot to AI; Marketing AI Institute; BankInfoSecurity (Jaokar / Furr & Shipilov / Narayanan roundup).
**Propagation chain**: Fortune 2025-08-18 and 08-21; The Register; Gizmodo; Axios; Entrepreneur; consultancy.uk; FT (via secondary quotation).
**Vendor/consulting yardsticks**: IDC×Microsoft 2024 InfoBrief; Google Cloud ROI of AI 2025; McKinsey State of AI 2025; BCG Widening AI Value Gap 2025 (incl. methods note); Deloitte Q4-2024 wave and 2025 AI ROI paradox; IBM CEO Study 2025; KPMG AI Pulse 2025 Q1–Q4; Accenture Front-Runners 2025; Wharton-GBK Accountable Acceleration 2025; PwC 29th Global CEO Survey 2026; Bain June 2026; S&P Global 451 VotE 2025-03/2025-10; Gartner's 2024 prediction and 2026 revision; RAND RRA2680-1.
**Independent measurement**: Census BTOS and CES-WP-26-25; Fed FEDS Notes 2026-04; Bick–Blandin–Deming (NBER w32966 and updates); Humlum & Vestergaard (NBER w33777, March 2026 revision); Brynjolfsson–Li–Raymond (QJE 2025); Otis et al. (Management Science); KPMG–Melbourne 2025; ECB SAFE 2025Q4 and June 2026 blog; UK ONS BICS; Ramp AI Index; Stanford AI Index 2026; Goldman Sachs March 2026 (via Fortune).
**Historical base rates**: Eveleens & Verhoef (IEEE Software 2010); Sauer/Gemino/Reich (CACM 2007); Flyvbjerg et al. (JMIS 2022; HBR 2011); Castellion & Markham (JPIM 2013); Wong/Siah/Lo (Biostatistics 2019); BIO 2016; Cisco 2017 press release; LNS Research; Ghosh (via WSJ/HBS 2012); Letrud & Hernes (PLoS ONE 2019); Davenport (IIA).
**Theory**: Brynjolfsson/Rock/Syverson (AEJ Macro 2021); Cohen & Levinthal (ASQ 1990); Bresnahan/Brynjolfsson/Hitt (QJE 2002); Solow (NYT Book Review, 1987-07-12); David (AER P&P 1990); Devine (JEH 1983, as quoted by David); Oliner & Sichel (2000); Acemoglu (NBER w32487 and Dec 2024 interview); McElheran et al. (Census CES-WP-25-27); Bijnens/Konings/Putseys (KU Leuven); Slok (Apollo, Feb 2026); ECB's Lane (March 2026).

*For the full arguments, every source, and the counter-evidence, this deep-dive edition is the reference; the plain-language edition is its compressed rewrite.*
