# Grading the Evidence on Longevity Interventions: Rapamycin, Metformin, NAD+, Fasting (Deep Dive)

> Methodological note: the load-bearing claims in this article went through 34 groups × 3 adversarial votes (102 votes: 33 groups returned with caliber corrections, 1 group was overturned, 0 groups passed untouched), plus a contradiction-search seat and a methods-audit seat with veto power for each of 6 single-source load-bearing empirical findings (12 seats: 2 upgraded to multi-source, 1 ruled direction-contested, 9 restricted-use). Verification produced 90+ caliber corrections, three of which rewrote this article's intended argument outright — the overturned and restricted parts are in the body text, not buried in a footnote. Evidence grades: **[multi-source]** ≥2 independent sources agreeing; **[single-source verified]** traceable to primary text; **[direction contested]** independent sources disagree; **[interested-party caliber]** self-reported by someone with a stake, direction usable, magnitude not load-bearing; **[unverified]**. All figures as of July 2026. **This is an evidence review, not medical advice. Nothing here should be taken as a reason to use any drug; off-label use of prescription medication in particular requires a physician's assessment.**

## 0. First, a ruler: three tiers and four slippages

Arguments about longevity interventions almost never happen at the level of fact. Rapamycin really does extend mouse lifespan. Metformin's epidemiological starting point really was published. Caloric restriction really does improve metabolic markers. The argument is about **which tier those true things get moved to**.

So this article starts by fixing a ruler. Evidence for any longevity intervention can only sit in one of three tiers:

1. **Animal lifespan.** The animals live longer. This is the only tier where "lifespan" is measured directly.
2. **Human surrogate endpoints.** Something moved in a person — a blood marker, an epigenetic clock, muscle mass, insulin sensitivity.
3. **Human clinical outcomes.** People got sick less, became disabled less, lived longer.

The four star interventions sit in wildly different places on this ruler, and their fame has almost nothing to do with where they sit. More importantly, moving evidence up a tier does not require one bold leap. It requires four small, specific moves that almost always survive peer review:

- **Tier slippage.** Animal lifespan data is cited as human outcome data, with the two intervening tiers left empty.
- **Endpoint slippage.** Maximum lifespan is quoted as median lifespan, mean as median; a missed primary endpoint is replaced by a secondary endpoint or a subgroup; a within-group before-and-after change is presented as a between-group randomized contrast.
- **Dose slippage.** The prescribed dose is quoted as the achieved dose; the nominal milligrams as the milligrams actually absorbed.
- **Criterion slippage.** A pre-specified one-sided p<0.10, a 90% confidence interval, or an 80% posterior probability is read as if it were a conventional two-sided p<0.05.

The finding of this physical is that each of the four interventions has a signature number, and **all four signature numbers are products of one of those slippages**. That is not four independent lapses. It is what a field does systematically when it has no qualified endpoint.

One thing to say up front: criterion slippage runs both ways. It usually makes a positive result look stronger, but this article also caught it making a negative result look gentler (section 2.5). Different direction, same mechanism.

## 1. The only scoreboard: the NIA Interventions Testing Program

To grade evidence you need a scoreboard that serves nobody's position. This field happens to have one, and exactly one.

### 1.1 Why it counts as a gold standard

The National Institute on Aging's Interventions Testing Program (ITP) has run since 2004 and does three things that most published mouse lifespan work does not [multi-source, primary design papers]:

**The genetic background is not a single strain.** Every mouse is a UM-HET3 — a four-way cross bred from CByB6F1/J dams (BALB/cByJ × C57BL/6J) and C3D2F1/J sires (C3H/HeJ × DBA/2J), so no animal is inbred. That removes an entire class of objection: that an effect is just one strain's quirk. NIA's own phrasing is that these mice are "genetically heterogeneous, the equivalent of a large sibship" — each genotype unique, but still related individuals.

**Three sites run the same protocol in parallel.** The Jackson Laboratory, the University of Michigan, and UT Health San Antonio each run a copy. The design paper is admirably hedged about "identical": the SOPs only promise conditions "as uniform as possible," and it states plainly that "It is particularly challenging to provide uniform environmental conditions at independent institutions." That honesty matters, because the same paper quantifies the residue: across the three sites, control male median lifespan averaged 799 days with a range of 137 days — 17% of the mean.

**The power was calculated in advance, and it is not high.** The 2008 design specified 36 females and 44 males per site per arm (108 females and 132 males in total); males were over-represented "because of the expectation that some cages will have to be culled due to fighting"; the control group is twice the size of each experimental group. The power statement must be quoted in full: the 2017 program review says the protocol will "detect a 10% change in **mean** lifespan, in either sex, with 80% power, **pooling data from as few as two sites**." Mean lifespan, pooled across sites. Which implies something that recurs throughout this article: **by design, the ITP cannot resolve effects smaller than about 10%.**

One correction: 36/44 was the 2008 design, not current practice. Recent cohorts reported in 2024 ran 142–156 males and 132–144 females per arm pooled across the three sites. Quoting 36/44 in the present tense is wrong.

**Results are published regardless of outcome.** I expected to find no written policy on this; verification overturned that. NIA's ITP page, under the heading "Publication, Data Sharing, and Biospecimens," states: "All lifespan results, both positive and negative, are submitted for publication." [single-source verified, official page] A publication commitment in writing is rare in this field and deserves to be recorded as such.

Every ITP percentage has to be read against one denominator: across 3,690 control mice (six cohorts, start years 2004, 2005, 2006, 2007, 2009, 2010), female median lifespan was 887 days (95% CI 879–898) and male median 803 days (791–815). "A 20% male extension" means roughly 160 days added to an 803-day base.

### 1.2 The ledger: what passed, what did not

| Compound | ITP verdict |
|---|---|
| Rapamycin | Passed; largest effect, stable across doses, female-favouring |
| Acarbose | Passed; large in males, small in females |
| 17α-estradiol | Passed; males |
| Canagliflozin | Passed; males (female harm on late start) |
| Glycine | Passed, both sexes — but only 4–6% |
| **Metformin (alone)** | **Did not pass** |
| **Nicotinamide riboside (NR)** | **Did not pass** |
| **Fisetin** | **Did not pass** |
| Resveratrol, simvastatin | Did not pass |
| Urolithin A, taurine | **In testing, unreported** (2025 cohort) |

That last row deserves its own note. I intended to write that the ITP has never tested urolithin A or taurine. The verification seat overturned it directly: NIA's compounds-in-testing table (updated 2026-04-13) contains the rows "Urolithin A (Uro) | 2025 | 150 ppm | 7 mo | In Progress" and "Taurine (Tau) | 2025 | 6000 ppm | 7 mo | In Progress" [single-source verified, official table]. The correct statement is "no result has been reported," not "never tested" — a distinction that matters most for taurine, which is among the loudest longevity claims of recent years and whose verdict is on its way.

A trap worth recording, because it will cause misreporting: the abbreviation "UA" in the ITP data portal is **ursolic acid**, not urolithin A.

### 1.3 That "14%" is a maximum-lifespan figure

Rapamycin's signature number comes from Nature in 2009 [multi-source, primary]. The sentence reads:

> "On the basis of age at 90% mortality, rapamycin led to an increase of 14% for females and 9% for males."

Three qualifiers get dropped in everyday citation. This is **age at 90% mortality** — a maximum-lifespan measure, not median lifespan. Dosing began at **600 days of age**, already late life. And the 9%/13% pair from the same paper, widely quoted as medians, is introduced in the original as "Expressed as mean lifespan" — **mean**, not median. The paper reports no pooled median-lifespan percentage anywhere.

While drafting I made a more instructive error. I had written that 14% was "one of the smaller rapamycin effects in the ITP's own ledger." Two of three verifiers pointed out that this sentence commits the very slippage the paragraph is warning about — comparing a 90th-percentile figure against other studies' median figures. On its own metric, the 2009 result is not small. I changed it.

The authors' own hedge deserves quoting too:

> "Rapamycin may extend lifespan by postponing death from cancer, by retarding mechanisms of ageing, or both."

Extending lifespan is not the same as slowing aging. The original paper is more careful than its retellings.

### 1.4 Dose and sex: the same drug gives three different answers

Miller 2014's dose-response experiment (dosing from 9 months, median lifespan increase) [multi-source, primary]:

- 4.7 ppm: males +3% (p=0.19, **not significant**), females +16%
- 14 ppm: males +13%, females +21%
- 42 ppm: males +23%, females +26%

So "rapamycin extends mouse lifespan by X%" is meaningless without a dose and a start age: the lowest dose did essentially nothing in males. One technical correction: these p-values come from site-stratified log-rank tests on the entire survival distribution. They are not tests of a difference in medians.

Rapamycin is one of the few female-favouring hits in the ITP, and the paper's proposed explanation is higher female blood levels (7/16/80 ng/mL in females at 4.7/14/42 ppm versus 6/9/23 ng/mL in males). The paper hedges this itself ("perhaps reflecting sexual dimorphism in blood levels"), and its own data do not fully fit the prediction: at 4.7 ppm blood levels are nearly identical between sexes (6 versus 7 ng/mL), yet that is exactly the dose where the sex gap is largest. Presenting it as an established mechanism overstates it.

Nor can "rapamycin favours females" be written as a rule: in Strong 2020, one arm starting at 20 months was significant in **males** only (+11%, p=0.024) and null in females (+4%, p=0.15).

### 1.5 The scoreboard records harm too, and mostly in females

The ITP can detect shortened lifespan, and has. 16α-hydroxyestradiol raised male median lifespan 15% (p=0.0001) while causing a significant **7% decline** in females; late-start canagliflozin also showed female harm; a dedicated end-of-life necropsy study found no pathological explanation [single-source verified]. (The compound's name carries a trap: the original paper printed "hydroxyestriol," corrected to "hydroxyestradiol" by a 2025 erratum.)

In the 2026 C2022 report, the only result that survives multiplicity correction is also harm: pioglitazone reduced female median lifespan by 9.41% (p<0.0001 pooled across sites; −6.2%, p=0.0047 excluding The Jackson Laboratory) [single-source verified, primary].

One elegant mechanistic experiment explains half of the sex asymmetry: castrating male mice at 3 months abolished the male-specific metabolic response to both acarbose and 17α-estradiol [single-source verified].

### 1.6 On "even the gold standard can't replicate itself" — a sentence I cannot write

The 2026 C2022 report is tempting material: eleven intervention arms (built from eight compounds and combinations), none significantly extending lifespan; and astaxanthin, meclizine and mitoglitazone — three male hits the ITP itself reported in 2024 and 2025 — all failing to reach significance this time.

I was going to write that even this field's gold-standard program cannot replicate its own hits. The methods-audit seat struck it down, on two grounds, both correct.

**First, not one of the three was re-tested at its original dose-and-start-age combination.** Astaxanthin's original hit used a 4,000 ppm target dose (achieved roughly 46% of target) starting at 12 months; this round changed the dose or delayed the start. A negative result under changed conditions is not a failed replication; it is a different experiment.

**Second, these arms are not powered to detect the original effect sizes.** The original effects were +12%, +8% and +9% median gains — two of the three below the ITP's own 10% detection floor. At that power, "not significant" is not "not there." C2022's own Methods state: "P-values presented are nominal, i.e., they are not adjusted for multiple comparisons."

And the ITP's actual replication record is good, not bad. Strong 2022, verbatim [single-source verified]:

> "Five of the agents that increase lifespan (NDGA, aspirin, rapamycin, 17αE2, and acarbose) have been re-examined in later cohorts with different dosages and treatment durations. Of these, only aspirin did not replicate, although it was only tested at higher doses."

Counting canagliflozin, five of six re-examined hits replicated — aspirin the lone failure, and only at higher doses. So the correct story is not "the gold standard can't replicate itself" but a more useful stratification: **the large effects (rapamycin, acarbose, 17α-estradiol) replicate robustly, while the small hits in the 8–12% band sit on the power floor and are fragile enough that a modest change in dose or start age erases them.**

The strongest evidence for that stratification is what the ITP says about itself in print. The C2022 discussion puts chance on the table unprompted:

> "…were at or near the lower level of what is expected to be able to discover at 80% power, and none of them showed a change in the Wang-Allison statistic. Furthermore, the p-values are nominal, and chance effects can be expected in any series of studies for truly ineffective agents."

A program writing in its own journal article that its small hits may be chance carries more weight than any external criticism.

And the cleanest demonstration of boundary fragility is not in C2022 at all — it is inside C2021: forskolin, male median +8.3%, log-rank p=0.17, recorded as a miss; mitoglitazone, +8.7%, p=0.015, recorded as a hit [single-source verified]. Same cohort, same control group, nearly identical median gains, on opposite sides of p=0.05. The distance between a hit and a miss is sometimes 0.4 percentage points.

### 1.7 Combinations, and another caveat I got wrong

The largest effect the ITP has published is a combination: rapamycin 14.7 ppm plus acarbose 1000 ppm from 9 months, male median +34% and female +28% (both p<0.0001). I had attached the caveat "measured against non-concurrent controls." That is wrong — these figures use C2017's own concurrently randomized control group. The real caveat is more serious and more specific: C2017's control mice at the UT site were anomalously short-lived, the paper calls its own conclusions "tentative," and excluding that site brings the figures down to +29% male and +22% female.

Acarbose is also not the largest single-agent male effect (rapamycin at 42 ppm, +23%, is larger), and its +22% did not replicate at that magnitude: the same 1000 ppm dose started at 8 months gave +17%.

## 2. Rapamycin: the strongest animal evidence, the thinnest human evidence

Rapamycin's standing at the animal tier is the only uncontested thing among these four interventions. Its standing at the human tier is the opposite, and that contrast is the most important picture in this article.

### 2.1 That "20%" is not about rapamycin

The most widely circulated human evidence is that "rapamycin improved immune response in the elderly by 20%." Item by item [multi-source, primary]:

- The drug was **everolimus (RAD001)**, a rapalog, not rapamycin.
- 218 volunteers aged ≥65, nine centres in New Zealand and Australia, six weeks of dosing.
- The endpoint was the influenza vaccine haemagglutination-inhibition geometric mean titre ratio.
- The criterion was **two conditions jointly**, not p<0.05: in at least two of three vaccine strains, a ≥1.2-fold GMT increase relative to placebo **and** a posterior probability of at least 80%. This is a Bayesian design, and the paper says so.
- In the intention-to-treat population, seroconversion rates for the H3N2 and B strains rose numerically but did not reach statistical significance.

One fact favouring the study must be added, or this is quoting half the evidence: seroconversion against the heterologous A/H3N2 strain **was** significant in ITT (pooled drug arms 39% versus placebo 20%, P=0.007).

On adverse events, the rate of **treatment-related** adverse events was 41.5% (0.5 mg daily), 37.7% (5 mg weekly) and 50.9% (20 mg weekly) versus 20.3% on placebo — roughly double placebo, with mouth ulcers occurring even at the lowest dose.

### 2.2 The decisive human result is a failure

This product line reached phase 3. PROTECTOR 1 enrolled **1,024** participants aged ≥65 (non-smokers without COPD; 16 sites in New Zealand and 15 in Australia), missed its primary endpoint, and put the point estimate on the wrong side of 1 (OR 1.07) [multi-source, primary].

The phase 2b result that launched the programme is almost always quoted without one qualifier: OR 0.601, **90% confidence interval** 0.391–0.922. A 90% interval is a materially lower bar than the conventional 95%. And the phase 2b population was high-risk (asthma, type 2 diabetes, COPD, heart failure, current smokers) while phase 3 used a lower-risk population — a change **the FDA requested**, a fact stated in the trial's own publication, not only in outside commentary.

The timeline afterwards: failure announced 2019-11-15; merger agreement signed 2020-04-28; merger with Adicet Bio completed 2020-09-15. Within roughly ten months of the failure, the company was no longer an aging company. And the most experienced developer on this line, Joan Mannick, is now Chief Medical Officer at Altos Labs; TOR-101, the next-generation rapalog from the company she founded (Tornado Therapeutics), has still not entered humans.

### 2.3 PEARL: primary endpoint missed, positive finding resting on eight people

PEARL (NCT04488601) is the only randomized rapamycin trial in a healthy-aging population, and its sponsor, AgelessRx, is a telehealth company that **sells rapamycin**.

Its registered primary outcome was change in visceral fat by DXA. It was **not met**. The widely cited positive finding is lean tissue mass improvement in women on 10 mg/week (48-week mean difference 6.194, 95% CI 0.877–11.511, p=0.018), and it rests on **eight women** — the paper states n=8 for women in the 10 mg group, while the percentage in the same sentence (20%) implies seven, and the sponsor's own webinar says six. Three sources, three numbers; and the paper's own Results concede that "limited sample sizes and variability in individual response likely restricted the statistical interpretation of results." The analysis covers 114 completers against 129 registered enrollees. As of July 2026 the registry's hasResults flag is still No, despite a primary completion date of 2023-12-30 and journal publication in 2025.

One accusation I intended to make was stopped by verification: AgelessRx's public explainer does disclose the missed primary endpoint, stating that "Loss of visceral fat was one of the primary clinical endpoints for the PEARL trial" and that no statistically significant difference was found. This cannot be written as concealment.

### 2.4 Compounded rapamycin: a direction I had backwards

PEARL used compounded rapamycin capsules from Belmar Pharma Solutions (5 or 10 mg/week) and **did not measure blood levels**. A pharmacokinetic paper from the same group later reported 0.27 versus 0.87 ng/mL per milligram, i.e. compounded at 31% of the commercial product.

Three corrections to that chain. The PK study measured **tablets from Precision Compounding Pharmacy** — a different pharmacy and a different dosage form, in a paper that stresses compounding quality varies between pharmacies. It reports a **single-timepoint blood concentration ratio roughly 24 hours after dosing**, not bioavailability in the AUC sense; the authors state that measuring Cmax "was beyond the scope of the current study." And an independent HPLC assay found the compounded tablets contained about 26% less rapamycin per milligram, so a substantial part of the "low bioavailability" may be a content shortfall rather than absorption.

More importantly, I had the direction of use backwards. I assumed the community mostly takes compounded product, so trial doses understate real exposure. In AgelessRx's own observational database, only 12 of 316 users (3.8%) were on compounded rapamycin, while 79.7% used 6 mg of the commercial product. The dose gap exists; it runs the other way.

### 2.5 2026: the intermittent-dosing hypothesis was tested directly

The entire off-label rapamycin community rests on one pharmacological premise: once-weekly intermittent dosing inhibits mTORC1 while sparing mTORC2, thereby avoiding immunosuppression and metabolic side effects. There is **no direct human evidence** for this premise — confirmed by dedicated search.

In 2026 it got its first direct test. RAPA-EX-01 (ACTRN12624000790549) randomized 40 sedentary adults aged 65–85 one-to-one to sirolimus 6 mg weekly or placebo, on top of 13 weeks of structured exercise. The pre-specified primary endpoint was 30-second chair-stand repetitions [single-source verified, primary; restricted-use after dual-seat audit]:

- ITT adjusted between-group difference **−2.13 repetitions (95% CI −4.61 to 0.34; p=0.089)**, favouring placebo.
- The pre-specified complete-case analysis, −2.46 repetitions (p=0.045), and per-protocol analysis, −3.44 repetitions (p=0.007), were both **significant in favour of placebo**.
- HbA1c rose in the drug arm by 1.74 mmol/mol (95% CI 0.20–3.27; p=0.030).

Here is the reverse-direction criterion slippage promised in section 0, and the audit seat caught it for me: the trial's **protocol pre-specified α = 0.10**, while the publication reports 95% intervals and describes the primary endpoint as non-significant. On its own pre-specified threshold, the primary endpoint is significant in the direction favouring placebo. The public account makes a negative result look gentler than the protocol's own criterion does.

But the weight this trial can bear is limited, and the audit listed three restrictions this article accepts in full. It was powered for Cohen's d of 0.8–0.9 and describes itself as an exploratory feasibility study. Confidence intervals came from a wild bootstrap with only 999 replicates, giving p=0.089 a Monte Carlo band of roughly 0.071 to 0.107 — any phrasing about "just missing significance" is reading noise. The HbA1c finding sits within a panel of roughly 28 safety parameters (six of them nominally p<0.05), the paper states no multiplicity adjustment was made, and there were no pharmacodynamic measurements at all. Beyond that, the primary endpoint **is the training stimulus** — the placebo arm improved by 6.59 repetitions (+46%) over 13 weeks, a gain that looks more like learning than physiology for a bodyweight movement.

So the correct landing point is: **the intermittent-dosing hypothesis was tested head-on for the first time and was not supported, alongside an uncorrected metabolic signal.** Not "refuted," and not "no difference found."

Two independent pieces of context. PEARL itself found a significant HbA1c increase in males on 5 mg. And a 2025 independent mouse study (Elliehausen et al., Aging Cell) tested whether intermittent dosing is metabolically clean: both frequent and intermittent dosing impaired glucose tolerance and insulin sensitivity after weighted wheel-running, with intermittent dosing **reducing but not eliminating** the impairment. The "intermittent is clean" premise has been independently contradicted in mice and never supported in humans.

### 2.6 The hard endpoint is in dogs, and has not reported

A sentence I have to narrow: I intended to write that no human randomized trial of rapamycin has ever used a clinical outcome as its primary endpoint. That is false — a multiple system atrophy futility trial (NCT03589976, primary endpoint UMSARS score), a phase 3 trial in familial adenomatous polyposis (NCT06950385, primary endpoint disease progression), and 24-month phase 3 renal transplant trials in nearly 1,300 patients all exist. The correct statement has to pin the scope down: **in a healthy-aging population there is no randomized trial of rapamycin itself (sirolimus) with a clinical primary endpoint**, and none is registered as of July 2026. The rapalog line does have one — the everolimus/RTB101 programme in sections 2.1 and 2.2 used laboratory-confirmed respiratory infections as its endpoint. This has to stay consistent: having cited a systematic review whose scope is "rapamycin and its derivatives," I cannot then exclude the derivatives here.

The only anti-aging rapamycin trial with a hard primary endpoint is in companion dogs. TRIAD's own paper describes itself as "the first rigorous test of a pharmacologic intervention against biological aging with lifespan and healthspan metrics as endpoints to be performed outside of the laboratory in any species" — note "first against biological aging," not "the only trial in the rapamycin literature." Target enrollment is 580 dogs; published enrollment figures conflict (150 in the 2025 design paper, 210 in J Vet Sci 2025, and 158 "as of 2025" in GeroScience 2026), and no traceable 2026 figure exists. By design each dog receives 12 months of dosing followed by 24 months of monitoring, 36 months in total; the design paper publishes no completion or reporting date, so any specific readout year is an inference.

The total human evidence base can be summarized by one number: the most comprehensive systematic review screened 18,400 articles and included **19** studies — and its scope was rapamycin **and its rapalogs**, not rapamycin alone.

## 3. Metformin: the complete life history of an epidemiological artifact

This is the cleanest of the four cases, because it went the full distance: a number was born, cited for years, reversed by independent data, and then explained by a third dataset.

### 3.1 The origin: "diabetics outlive non-diabetics"

Bannister et al. 2014 used UK CPRD data (2000 to July 2013) to compare 78,241 incident type 2 diabetics on metformin monotherapy, 12,222 on sulphonylurea monotherapy, and 90,463 matched non-diabetic controls [multi-source, primary].

The conclusion cited for twelve years has this caliber: it is a roughly 15% **median survival time ratio** derived from a log-logistic accelerated failure time model, over a median follow-up of about 2.4 years. It is not an observation that people on metformin lived longer.

The paper states three things itself. It did not adjust for HbA1c, systolic blood pressure, total cholesterol, creatinine or BMI, because of "large proportions of missing data in controls" (not total absence). Its design censored patients 90 days after a regimen change, a rule applying to **both diabetic arms**, with each control censored at their matched case's censor date. And the authors named the asymmetry that diabetics receive lifestyle intervention and blood pressure and cholesterol monitoring while controls do not. To be precise: they listed this as a limitation but did not concede their result might be artifactual — they concluded the opposite.

The most telling detail is that the difference is not significant in the raw data: crude mortality 14.4 (metformin) versus 15.2 (matched controls) per 1,000 person-years, p=0.054, with the authors writing that the Kaplan-Meier curves "show that overall there was little discernible difference between metformin cases and non-diabetic controls." Funding was AstraZeneca and Bristol-Myers Squibb, with a BMS employee as co-author. The paper carries no retraction, erratum or expression of concern to this day.

### 3.2 The reversal, and a disagreement confined to one cell

Keys et al. 2022 ran the same comparison on Danish national registers (1996–2012): 7,842 metformin monotherapy initiators matched 1:1 to non-diabetic controls on birth year and sex. The result **reversed** — higher mortality among metformin initiators, IRR 1.52 (95% CI 1.37–1.68) unadjusted and 1.32 (1.16–1.50) adjusted [multi-source, primary; dual-seat audit: contradiction seat upgraded to multi-source].

What gives the reversal forensic value is that Keys placed their own crude mortality rates beside Bannister's. Three of four cells nearly coincide:

| Crude mortality per 1,000 person-years | Denmark | UK |
|---|---|---|
| Non-diabetic controls matched to metformin | 16.9 | 15.2 |
| Non-diabetic controls matched to sulfonylurea | 28.4 | 28.7 |
| Sulfonylurea-treated | 49.0 | 50.9 |
| **Metformin-treated** | **24.9** | **14.4** |

Two countries with different health systems, registries and demographics agree in three cells. That rules out "Denmark and the UK are simply different" and compresses the disagreement into the single remaining cell.

### 3.3 The third dataset does not just contradict — it explains

Stevenson-Hoare et al. 2023 repeated the comparison in the Welsh SAIL databank (1999–2018) at larger scale: 129,140 metformin-treated and 68,563 sulphonylurea-treated patients plus matched non-diabetic controls. Over a twenty-year horizon, the metformin group's survival time was **82%** of matched controls (survival time ratio 0.819) [multi-source, primary].

But its most valuable contribution is not another contradiction. The Welsh team re-ran the analysis across a range of simulated study windows and found that metformin's survival advantage over matched non-diabetic controls **does exist in the first three years and reverses after five**. Bannister's advantage can be reproduced in independent data — as an artifact of short follow-up. That is far stronger than "results disagree." It is a mechanistic explanation of an artifact.

### 3.4 All three papers actually agree on one thing

This literature looks chaotic but contains a stable conclusion: **metformin beats sulfonylurea.** Bannister reported markedly worse survival on sulphonylurea; Stevenson-Hoare states that "Metformin patients had better survival than sulphonylurea patients, controlling for age"; and Shadyab et al. 2025, using a new-user active-comparator target trial emulation in the Women's Health Initiative (438 propensity-matched women aged 60+), found HR 0.70 (95% CI 0.56–0.88) for death before age 90.

This has to be stated clearly, because Shadyab 2025 is being cited as restoring Bannister's conclusion. It does not: its comparator is **sulfonylurea**, not a non-diabetic population and not placebo. "One drug beats another glucose-lowering drug" and "a drug makes people outlive healthy people" are entirely different propositions.

Equally, Keys should not be treated as the right answer. The methods-audit seat listed its own directional biases: the twin limb rests on only about 172 exposed individuals and roughly 60% of pairs are dizygotic, so the claimed genetic control is sibling-level in most pairs; non-diabetic controls were censored at incident diabetes, which removes exactly the person-time in which a control's health is deteriorating and pushes the IRR upward; and co-twin control mortality runs about 40% below singleton control mortality with no explanation offered. The honest landing point is that Bannister's direction is unstable — and that the contrast "metformin-treated diabetics versus non-diabetics" may not be able to bear weight in either direction, because it mixes drug effect with having diabetes at all.

### 3.5 The randomized evidence: 21 years, nothing moved

There is one randomized dataset that sidesteps the observational quarrel. The Diabetes Prevention Program randomized 3,234 adults in 1996–99 — eligibility required elevated fasting glucose of 95–125 mg/dL **and** impaired glucose tolerance **and** overweight, with a mean age of 50.6 and mean BMI of 34, none of them diabetic — to placebo (n=1,082), metformin 850 mg twice daily (n=1,073), or intensive lifestyle (n=1,079). Its follow-on cohort, DPPOS, followed them for a median of about 21 years with 453 deaths (170 cancer, 131 cardiovascular) [single-source verified]:

> "Compared with placebo, metformin did not influence mortality from all causes (HR 0.99 [95% CI 0.79, 1.25]), cancer (HR 1.04 [95% CI 0.72, 1.52]), or cardiovascular disease (HR 1.08 [95% CI 0.70, 1.66])."

In the same cohort, metformin did reduce diabetes incidence. So this is a clean dissociation: effective on its own indication, and nothing downstream over twenty-one years.

Three qualifiers, without which I would be committing the error I criticize. Mortality was not a pre-specified primary endpoint of DPP or DPPOS and the trial was not powered for it; the all-cause confidence interval (0.79–1.25) is compatible with anything from a 21% reduction to a 25% increase — this is a **null result, not proof of no effect**. I had also written that this is "the exact population TAME proposes to treat," which is wrong: DPP's mean age was 50.6 with mean BMI 34, while TAME's design specifies ages 65–79. Finally, placebo dosing stopped in 2001 while the metformin arm continued unmasked, and participants in all arms who developed diabetes were frequently prescribed metformin by outside providers — the contrast was diluted, and the authors concede this was not fully controlled.

### 3.6 TAME: announced eleven years ago, not one participant enrolled

TAME (Targeting Aging with Metformin) was announced in 2015–2016 and is widely described as the trial that will make "aging" a registrable indication.

As of 28 July 2026, it has **no ClinicalTrials.gov registration** (checked with eight different query formulations), does not appear in the EU's EudraCT, and has never enrolled a participant [multi-source, registry primary plus official pages]. AFAR's own TAME page still describes it prospectively, with participants and donors listed under what is still needed.

The designer's own words are worth recording exactly. In August 2022 he told STAT News that he had been publicly predicting TAME's imminent start every year since roughly 2015. On 12 August 2025 he said:

> "I cannot give you a perfect update because it's now being handled within ARPA-H."

In the same interview he mentioned that Eli Lilly would run "a TAME-like study but with their GLP-1 agonist." To be precise: he frames TAME as a reusable template, not as being **replaced** by GLP-1 — "instead" was my drafting, not his word.

One byproduct is worth recording as a thermometer for this field's information hygiene: a website dated 2 March 2026 already reports TAME's "results" as fact, claiming a significant reduction in composite endpoint incidence. A trial that has never enrolled anyone already has reported results.

### 3.7 Evidence running the other way: it blunts exercise adaptation

Metformin has a layer of evidence that rarely appears alongside the benefit claims.

Konopka et al. 2019 randomized 53 adults (mean age 62) to metformin (titrated weekly to 2,000 mg/day, with eleven participants reduced to 1,500 mg/day for gastrointestinal discomfort) or placebo alongside aerobic training. Metformin attenuated the training-induced improvement in insulin sensitivity and "abolished the ~25% increase in maximal CI-linked respiration after AET during the ADP titration" [single-source verified]. Two necessary honesties: that abolished increase was itself p=0.07 and non-significant in the placebo arm; and the VO2max result routinely cited as significant was p=0.08.

Stronger still is the MASTERS trial: 109 participants randomized (55 placebo, 54 metformin) to progressive resistance training, where the investigators' **pre-specified hypothesis was that metformin would enhance** the response and they found the opposite. The relative-strength values were misprinted in the original publication; after a corrigendum they read placebo +18.9% versus metformin +14.8%, p=0.30.

Even the leading advocate accepts this point: in that August 2025 interview, Barzilai said people under 50 without diabetes should not take metformin, citing precisely the exercise interaction.

### 3.8 The misquoted monkey

The 2024 Cell study in cynomolgus monkeys travelled the world as "metformin delays aging in primates." Its caliber [single-source verified]: a self-described proof-of-concept Resource article; **male monkeys only**; aged 13–16 at start; **six treated animals**; 20 mg/kg/day; and the authors state in their limitations that they **did not assess survival**. The clocks used to score "age" were bespoke models trained de novo by the same laboratory on 36 of its own monkeys, never externally validated.

Barzilai publicly described it as "Aging was delayed by eight years on the transcriptomic level." Checked against the full text: the largest bulk transcriptAge values are Achilles tendon −5.31 years, then liver −4.14, bronchus −3.71, muscle −3.56, lung −3.40; the single largest figure anywhere in the paper is −6.86 years (microglia, single-nucleus). **There is no eight years.** In the same interview, describing his own centenarian-offspring proteomics, he said subjects were "on average, eight years younger on a proteomic level" — the eight years appears to have been carried over from a human dataset onto the monkeys.

## 4. NAD+: the premise itself does not hold

The first three interventions have at least one real animal lifespan signal. The NAD+ precursor line has a problem further upstream: **its major premise does not hold in humans.**

### 4.1 How thin the human evidence for an age-related decline is

An entire industry rests on one sentence: NAD+ declines with age, so replace it. The primary human evidence for that sentence is:

- **Skin.** Massudi et al. 2012, human pelvic non-sun-exposed skin biopsies, n=49 (including newborns), cross-sectional. The correlations are not weak: males r=−0.769 (p=0.0007), females r=−0.537 (p=0.01) [single-source verified].
- **Brain.** Zhu et al. 2015, occipital-lobe 31P-MRS, **seventeen people total**, in three bins (seven aged 21–26, four aged 33–36, six aged 59–68).

Both pillars have problems. The brain pillar has an independent, larger test whose incentives ran the other way: Cuenoud et al. 2020 (n=50, EPFL/Sherbrooke, funded by Nestlé with three Nestlé employees as authors) found only an inverted trend at p≈0.06 — **the larger, more recent study is the weaker one**, and an interest structure that should have favoured confirming a decline failed to push it over the line.

The skin pillar has a fake-replication problem of exactly the kind this article criticizes elsewhere: the two most-cited datasets supporting a human NAD+ decline — Massudi 2012 and Clement 2019 (plasma, LC-MS/MS) — **share an author, Nady Braidy, and the UNSW Sydney institutional cluster**. Citing both as "multiple studies show a decline" is the same independence failure this article charges elsewhere.

And the widely circulated "NAD+ falls by half by age 50" has no clean human primary source; it is a weld of a skin correlation, an n=17 spectroscopy study, and animal data.

### 4.2 2026: an underpowered null, but with independent corroboration

In May 2026, Nature Metabolism published a 32-author study (Amsterdam UMC, Helsinki, Leiden, Valencia) that measured NAD+ by validated UHPLC-HRMS across seven independent human cohorts and concluded that whole-blood NAD+ does not vary with age, challenging the utility of blood NAD+ as an aging biomarker [single-source verified; dual-seat audit: restricted-use].

The methods-audit seat was hard on it, and this article passes that on. The cohort purpose-built to test age is **n=20 (<30 years) versus n=20 (>60 years)**. The paper's own supplementary figure states that, given observed technical variability, only a true difference greater than 7 nmol/mL would have been detected with 80% power. There is no equivalence test anywhere; "remain remarkably stable with age" is a **failure to reject**, not a demonstration that the effect is negligible. The regression adjusts for sex only, while the authors separately show that the red-cell fraction drives the signal — and hematocrit is not in the model. And the largest age-relevant cohort of the seven is the Leiden Longevity Study, a family collection genetically enriched for exceptional survival, i.e. the population least likely to show an age-related decline.

But the contradiction-search seat brought back something more important: on blood specifically, this conclusion has genuine independent corroboration. Yang et al. 2022 (Frontiers in Endocrinology) measured n=1,518 healthy adults in China using an enzymatic cycling assay cross-validated against LC-MS/MS — different team, different country, different cohort, different chemistry, zero author overlap — and likewise found no consistent decline across the adult age range [multi-source]. An honest qualifier: Yang reports a significant sex interaction (p=0.003), with a small negative coefficient in men aged ≥60 and no trend in women, at a magnitude of roughly 6% of the male mean. An independent French team (Breton et al. 2020) reported the same sex asymmetry.

So there are two separate conclusions here, and they are not the same one: **"human whole-blood NAD+ does not decline appreciably with age" is now a multi-source conclusion; "human NAD+ does not decline with age" outruns the evidence — the tissue-level evidence points the other way, and the 2026 paper itself lists measuring only whole blood as its first limitation.**

Two gaps are worth recording. There has never been a meta-analysis or systematic review of NAD+ versus age in humans — the five meta-analyses that surface are all about supplementation trials. And there are no longitudinal data at all: **every** study above, on both sides, is cross-sectional. Nobody has followed the same people and measured their NAD+ twice.

### 4.3 It rises in blood and not in muscle

The pharmacokinetic conclusion is clean: oral precursors do raise circulating NAD+. The largest NR randomized trial (n=140 healthy overweight adults, 8 weeks) established a clear dose response, with whole-blood NAD+ up 22%, 51% and 142% [single-source verified]. The widely circulated "NR raises NAD+ 2.7-fold" is an **n=1** pilot in Trammell 2016, labelled as such in the paper; that study's controlled figure is PBMC NAD+ rising from about 12 to 18 µM after a single 1,000 mg dose (n=12).

But to produce any functional consequence it has to rise in the tissue doing the work. Elhassan et al. 2019 is the only NR trial to measure muscle NAD+ directly by biopsy in older people: 12 aged men, 1 g/day for 21 days, in a **crossover** design in which every participant received both drug and placebo. Muscle NAD+ **did not rise significantly** (210 versus 197 pmol/mg, p=0.22). The paper's title phrase "augments the NAD+ metabolome" refers to other metabolites, not NAD+ itself. Functional endpoints were likewise null: no difference in complex I- or complex II-mediated oxidative phosphorylation, and hand-grip strength of 32.5 kg (NR) versus 34.7 kg (placebo), p=0.96.

Here I had a piece of evidence pointing the wrong way in draft, which is worth recording. I treated Remie 2020 as a counterexample in which NR did raise muscle NAD+. On checking: Remie measured muscle NAD+ by two independent methods, enzymatic cycling (p=0.34) and mass spectrometry (p=0.91), and **neither rose**; the paper states "We confirmed that NR supplementation had no effect on skeletal muscle NAD+ content itself." It is not a counterexample; it is a **second-method replication** of the Elhassan null. What rose were downstream metabolites such as NAAD and methylnicotinamide. A third dataset, Dollerup 2020, doubled the dose to 2,000 mg/day and quadrupled the duration to 12 weeks, and still found no change in muscle NAD+ or mitochondrial function.

### 4.4 Functional endpoints: mostly null, but not unanimous

At the pooled level [multi-source]:

- Prokopidis et al. 2025 (10 RCTs; NMN 250–2000 mg/day for 3–24 weeks in six, NR 500–1000 mg/day for 3–12 weeks in four; mean ages 60.9–83) found **no effect** on skeletal muscle mass indices or strength.
- A meta-analysis of NMN on metabolic endpoints (8 RCTs, n=342) found no significant benefit.
- Damgaard and Treebak 2023, in Science Advances, assessed all **25** then-published human NR research articles and concluded the effects are few and clinically marginal and that the literature systematically overstates them.
- The most rigorous insulin-sensitivity test was null: 40 obese, insulin-resistant men, NR 2,000 mg/day for 12 weeks, hyperinsulinaemic-euglycaemic clamp, no effect.

But "unanimous" cannot be written: verification found two meta-analyses pointing the other way (Wang et al. 2025 on muscle endpoints, Zhang et al. 2026 on blood pressure). The honest phrasing is that **the mainstream direction is null while the pooled layer itself contains disagreement.**

The caliber of two signature numbers:

"NR lowers blood pressure by 9 mmHg" comes from Martens 2018 and is a **post-hoc exploratory subgroup** of a 24-completer crossover trial, about which the authors wrote that "no statistical inferences can be made"; the pre-specified whole-group results were null.

"NR improves walking in peripheral artery disease" (the NICE trial, n=90, 6 months) was judged positive against a **pre-specified one-sided p<0.10**. The ITT effect is +17.6 m on the six-minute walk. One caliber error of mine was corrected here: 20 m is not the minimal clinically important difference — the paper defines a small MCID of about 8 m and a **large** MCID of 20 m for PAD, so 17.6 m clears the small one and misses the large one. Also, only the NR-alone arm crossed the threshold; the NR-plus-resveratrol arm was null (+3.65 m, p=0.38).

### 4.5 Funding structure: vendor dependence, not one vendor

I had drafted that every large or landmark human NR trial carries ChromaDex money, product or equity ties. That universal quantifier was refuted: counterexamples include Norheim et al. 2024 in COPD (competitor Elysium Health supplied product and funded the methylation analyses) and NOPARK — 410 patients with early Parkinson's disease, NR 500 mg twice daily versus placebo for 52 weeks, led by Norwegian public hospitals with no industry collaborator on the registry record, completed 2025-06-17, and as of July 2026 neither published nor posted.

The accurate description is **vendor dependence rather than a single vendor**: ChromaDex (which sells Tru Niagen) and its competitor Elysium Health each sit on a long list of trials, and the Elysium line includes large studies such as NO-ALS (n=380) and NADAPT (n=330). Any defence of the form "this one wasn't ChromaDex-funded" does not solve the independence problem; it changes the vendor.

One detail deserves separate quotation: Martens 2018 declares "The authors declare no competing interests" in the same document that discloses ChromaDex supplied study pills, standards and partial funding.

### 4.6 The mouse verdict, and a possibly cheaper mechanism

NR's ITP verdict is in section 1.2: 1,000 ppm from 8 months, three sites, males p=0.252 (median −3%), females p=0.612 (0%). The mouse study supporting "NR extends lifespan" is a single work reporting about 5% with dosing from roughly 24 months (Zhang 2016), against the ITP's null.

And a 2026 head-to-head trial (65 healthy participants, **open-label**, 1,000 mg/day of NR, NMN or nicotinamide for 14 days) proposed a mechanism: gut microbiota convert NR and NMN into nicotinic acid, which then raises systemic NAD+ via the Preiss-Handler pathway [single-source verified]. If that holds, the expensive precursors are doing the work of cheap nicotinic acid. There are no clinical-endpoint data on this line, but it identifies a controlled trial that has never been run: NR or NMN head-to-head against plain nicotinic acid, on any clinical endpoint.

### 4.7 The signature NMN result: 13 versus 12, and the same lab could not replicate it

NMN's most famous clinical result is that 250 mg/day for 10 weeks improved muscle insulin sensitivity in postmenopausal women with prediabetes (Yoshino et al., Science 2021). Its size is 13 in the NMN arm and 12 on placebo.

Charles Brenner challenged it in Science on randomization grounds: baseline intrahepatic triglyceride was 6.3 ± 1.2% versus 14.8 ± 2.0% (P=0.003, means ± SEM). His stated reason has to be quoted precisely — I had drafted it as "liver fat itself depresses muscle insulin sensitivity," while his actual argument is:

> "Given that a target of NMN is liver fat clearance, this was not an effectively randomized trial."

The point is that NMN's own target is liver fat clearance, so the arms were not exchangeable with respect to the drug. Separately, that headline 25% is itself a **within-group** before-and-after change in the NMN arm.

The most important development was unearthed by verification: the same group ran a larger, longer, higher-dose repetition (NCT04571008; 28 randomized and 20 completing per arm, ≥16 weeks, 300 or 450 mg/day, prediabetic men and women), with results posted to the registry on 2026-03-11 — **it did not replicate.** The follow-up trial's standard deviations on that endpoint were enormous (roughly 90 on a mean change of about 15), which retrospectively shows how illusory the precision of the original 13-versus-12 result was.

## 5. Fasting and caloric restriction: the only intervention with long randomized trials

This is the only one of the four tested in multi-year randomized controlled trials in humans, which makes its evidence both the sturdiest and the most revealing about where this field's ceiling is.

### 5.1 CALERIE-2: registered primary endpoints and the actual dose

CALERIE-2 is the only long-term randomized caloric restriction trial in healthy non-obese humans. Two things have to be established first.

**The primary endpoints.** The registered primary outcomes were change in core body temperature and change in resting metabolic rate corrected for body composition, at 12 and 24 months. At 24 months both were null; RMR was met at 12 months (p=0.04). I had drafted "failed both primary endpoints," which is wrong — one of four registered primary outcome measures was met, at 12 months, at p=0.04. There is also a trap this article has to raise itself: the registry's posted results give p<0.001 and p<0.0001 on the **uncorrected** RMR caliber, which any reader checking the registry will see; the difference is exactly that the pre-specified endpoint was the body-composition-corrected one.

**The dose.** The prescription was 25% caloric restriction; the achieved figure was **11.9 ± 0.7%** (a formal 2016 erratum corrected a previously published 11.7%, so there is one value, not two independent estimates from two papers). And it was not flat: about 19.5% in the first six months and 9.1% on average across the remaining eighteen. So any sentence of the form "25% caloric restriction in humans produced X" describes an average dose of about 12%. This is the textbook case of dose slippage — and this time it is not the researchers' fault, it is the ceiling of human adherence.

Incidentally, the cardiometabolic improvements universally cited as the trial's payoff are labelled **exploratory outcomes** in the paper's own title (N=218, 2:1 randomization, two years).

### 5.2 What that "slower aging" result actually is

CALERIE's most famous result comes from Waziry et al.'s 2023 **post-hoc** analysis of banked specimens in Nature Aging (N=197 of 220 randomized). It tested eleven DNA methylation measures of aging: ten clocks (Horvath, Hannum, Horvath Skin & Blood, PhenoAge, GrimAge, each in original and principal-component form) plus DunedinPACE. All ten clocks were **null** in ITT at both 12 and 24 months. Only DunedinPACE moved: 12-month d = −0.29 (95% CI −0.45 to −0.13, p=4.83×10⁻⁴), 24-month d = −0.25 (−0.41 to −0.09).

I was going to write this up as a "one out of eleven" multiplicity problem. The methods-audit seat explicitly forbade that framing, on quantitative grounds this article accepts: the pace-versus-level distinction is principled. DunedinPACE's standard deviation is 0.09, so d = −0.29 means a pace of aging roughly 2.6% slower; the ten clocks measure a level in **years** (standard deviations of 2.76–5.04 years), and a one-year intervention mathematically cannot move those to detectability. In other words, DunedinPACE is the only measure that **could** have moved on this timescale, not one lucky draw in eleven. And the 12-month result survives Bonferroni correction across 22 tests on its own.

So this is a real effect that survives correction. The problem is what it gets converted into.

The paper's own discussion performs that conversion — which also corrects my draft, since I had assumed the media added it:

> "…the CALERIE treatment effect of 2-3% slower pace of aging corresponds to a reduction in mortality risk of as much as 10-15%, similar to the effect of smoking cessation"

Note that "as much as" is an upper bound, not a point estimate. And of the two sources cited for that conversion, one is DunedinPACE's own development paper, sharing a senior author with this one.

The contradiction-search seat then found independent data that directly undercuts the conversion. Norway's HUNT study measured DNA methylation twice in the same people eleven years apart and followed mortality to 2023, measuring exactly the quantity the conversion requires — **the association between change in DunedinPACE and all-cause mortality** — and found a null. Meanwhile the per-standard-deviation mortality hazard for DunedinPACE ranges from 1.23 to 1.99 across independent cohorts, a spread that cannot support a point conversion.

Two further things make the measure harder to lean on. DunedinPACE responded in 36% of 41 human interventional studies, statistically indistinguishable from GrimAge (38.1%) and PhenoAge (33.3%) — it belongs to the most easily moved class of markers. And **no independent team has ever measured DunedinPACE in an independent randomized caloric-restriction or fasting trial**; the closest, DIRECT PLUS (n=256, an 18-month randomized diet trial that measured seven clocks including DunedinPACE), concluded that "all interventions did not differ in terms of changes between mAge clocks."

[direction contested] is this article's grade: the effect stands within the original trial, but the bridge from it to health outcomes has been dismantled by independent data.

### 5.3 The cost side: real, small, and a cost of weight loss

CALERIE's own investigators reported that 24 months of roughly 12% caloric restriction caused significant bone mineral density loss at the lumbar spine, total hip and femoral neck (24-month absolute changes of −0.013, −0.017 and −0.015 g/cm², about 2%).

Four qualifiers are necessary, and dropping any one turns this into alarmism. The loss occurred **only at central sites** — the paper states that "BMD decreased at the central sites of the spine and hip but not at the peripheral site of the wrist or whole body." These were pre-specified **secondary** outcomes, not primary endpoints. The authors calculated the clinical meaning themselves: for a 50-year-old woman without other risk factors, a **less than 0.5%** increase in ten-year fracture risk. And they state it was "expected on the basis of the weight lost," consistent with people who lose the same weight by other means — not a toxicity specific to caloric restriction. The trial's companion safety analysis concluded that two years of caloric restriction at these levels "was safe and well tolerated."

On body composition, 71% of the weight lost was fat (so about 29% was not); an MRI substudy (n=43, achieved restriction 13.7%) reports that subcutaneous fat made up 68.4% of total tissue-volume loss in the CR group over 24 months, visceral fat 7.4% and intermuscular fat 2.2% — 78% summed, which is this article's own arithmetic and not a figure the paper states.

### 5.4 The monkey studies: the answer was what the controls ate

The two long-term primate studies were long treated as this field's great unresolved case, and the 2017 joint analysis resolved it. This is an excellent evidence-grading case study and worth getting exactly right.

**Wisconsin's 2009 conclusion rested on a chosen endpoint.** 37% (14/38) of control monkeys versus 13% (5/38) of restricted monkeys died of **age-related** causes (p=0.03); **all-cause mortality in the same paper was not significant** (p=0.16). Only after five more years of accrued deaths (2014) did it firm up: age-related mortality HR 2.89 (95% CI 1.34–6.25), P=0.007; all-cause HR 1.78 (1.04–3.04), P=0.037. The honest grade is that the result ultimately holds, but the 2009 announcement used a subset endpoint.

**The NIA study found no survival benefit at either onset age.** The young/adult-onset cohort had 86 monkeys (46 control, 40 restricted); the old-onset cohort had 35.

**The 2017 reconciliation points at the control group.** Both diets were about 60% carbohydrate by weight, but **sucrose was under 7% of total carbohydrate at NIA and 45% at Wisconsin**; NIA used a naturally sourced diet, Wisconsin a semi-purified one. Feeding differed too: NIA's control monkeys were not free-fed but given measured allotments based on National Research Council data "to provide approximate ad libitum intake… without overfeeding," while Wisconsin's controls were fed ad libitum.

In other words: how much of Wisconsin's restriction effect was the benefit of eating less, and how much was the benefit of not eating a 45%-sucrose semi-purified diet continuously, cannot be separated within that design.

The third factor, age at onset, cuts against restriction, but must be quoted completely: the 2017 paper notes that although Cox proportional hazard regression indicated the survival differences between young/adult control and restricted animals were not significant, the NIA young-onset restricted monkeys reached 80% mortality **before** the controls. Both halves count: the regression is non-significant, but the direction runs against restriction.

### 5.5 Time-restricted eating: calories or timing?

This is the section both camps most often get wrong.

**TREAT** (Lowe et al., JAMA Internal Medicine 2020): 141 randomized, 116 analyzed, 12 weeks, 16:8 ad libitum eating from 12:00 to 20:00. The primary weight outcome was **not significant**. The widely cited lean-mass alarm needs three corrections: appendicular lean mass fell 0.64 kg in the TRE group (95% CI −0.89 to −0.39, **within-group** P<0.001) and 0.17 kg in controls (P=0.16, not significant), while the **between-group** difference is −0.47 kg (95% CI −0.82 to −0.12), P=0.009. And "65% of the weight lost was lean mass" is computed inside an arm that lost only 1.70 kg total, in a trial whose primary weight outcome was null.

**TREATY** (New England Journal of Medicine 2022): 12 months, 139 adults with obesity, China. **Both arms were calorie-restricted** — 1,500–1,800 kcal/day for men and 1,200–1,500 kcal/day for women (not 1,500–1,800 for both, which was my drafting error). The 12-month net weight difference was −1.8 kg (95% CI −4.0 to 0.4, P=0.11). To be precise: this is "no difference detected," not "no difference" — the point estimate favours TRE and the interval is compatible with an advantage as large as 4 kg.

**The isocaloric test** (Maruthur et al. 2024): 41 adults with obesity plus prediabetes or diet-controlled diabetes, 12 weeks, with **meals provided** so calories were held constant — no benefit from TRE.

**The BMJ 2025 network meta-analysis** (99 randomized trials, 6,582 adults): versus ad libitum eating, alternate-day fasting gave −3.40 kg (95% CI −4.14 to −2.67, **high certainty**).

But "timing does not matter" cannot be written; verification supplied two counterexamples. Jamshed et al. 2022 (n=90, 14 weeks, **both arms energy-restricted**, early TRE 7:00–15:00 versus a ≥12-hour window) found early TRE lost 2.3 kg more (95% CI −3.7 to −0.9, P=0.002). Sutton et al. 2018, a eucaloric crossover with food provided, improved insulin sensitivity with no weight loss. And the BMJ meta-analysis itself shows alternate-day fasting beating continuous energy restriction by 1.29 kg (95% CI −1.99 to −0.59, moderate certainty).

So the precise landing point splits in two: **time-restricted eating's weight benefit in humans is essentially a benefit of eating fewer calories; but within the broader category of "fasting," alternate-day fasting has a small real advantage over continuous restriction, and early eating windows show a signal under isocaloric conditions.**

### 5.6 Hype in both directions: that "91%"

In 2024 a headline swept the world: an 8-hour eating window was associated with a 91% higher risk of cardiovascular death. Layer by layer [multi-source, primary]:

- **The 91% comes from the American Heart Association's press release**, not the scientific abstract. The conference abstract (Circulation 2024;149:AP192) reports HR 1.96 (95% CI 1.23–3.13).
- It was a **conference abstract**, not peer reviewed, pushed worldwide by press release.
- Exposure classification rested on **exactly two days** of 24-hour dietary recall — two for everyone, not a minimum — used to characterize a follow-up averaging about eight years.

It was published in full in 2025, and the numbers are not the circulating ones: n=19,831 NHANES adults (2003–2018) linked to the National Death Index through December 2019, with cardiovascular mortality **HR 2.35 (95% CI 1.39–3.98)**.

The direction here is the opposite of what most people expect, and it must be stated: peer review made the number **larger**, not smaller — from +91% in the press release to +135% in the published paper. Part of that shift is definitional rather than evidential, since the reference category narrowed from 12–16 hours to 12–14 hours. The lesson is not "the scary preprint headline was later debunked" but that **publishing ahead of peer review is the problem regardless of which way the number later moves**.

Hype runs the other way too. The fasting-mimicking diet's "2.5 years younger biological age" is a **within-group** before-and-after comparison inside the FMD arm, even though both parent trials had control arms; and the circulating "11 years younger" is not a measurement at all but a 20-year simulation assuming continued efficacy. The interests need full disclosure: the experimental diet was provided by L-Nutra, USC has licensed related intellectual property to L-Nutra and may receive royalties, and the corresponding authors hold equity.

### 5.7 An absence I got wrong

I had drafted: "No caloric restriction, fasting, or time-restricted-eating trial anywhere in the world has mortality or incident age-related disease as a primary endpoint." This group was **overturned 3/3** — the only overturned group of this issue.

The counterexamples: PREDIMED-Plus (ISRCTN89898870), whose intervention arm is an energy-restricted Mediterranean diet plus physical activity plus behavioural support, with a primary-prevention cardiovascular composite as its primary endpoint; and MeMeMe (NCT02960711, 1,600 randomized), whose registered primary outcome reads "Total incidence of age related chronic diseases." Verifiers also noted that my scan of 1,472 registry records failed to catch the Diabetes Prevention Program itself — which shows the search string under-detects, and under-detection is not proof of absence.

The corrected landing point still holds but must be narrowed: such hard-endpoint trials exist, but they are all **multi-component lifestyle** trials. Caloric restriction or eating timing as a **single variable**, with a hard clinical primary endpoint, still does not exist. The distinction matters — if PREDIMED-Plus succeeds, you cannot know whether the credit belongs to calories, the Mediterranean pattern, exercise, or behavioural support.

## 6. Why this field is condemned to surrogate endpoints

The previous five sections keep hitting the same wall: the human outcome tier is nearly empty. This section is about why, and about how loose the ruler used in its place is.

### 6.1 There is no "aging" indication

A 2025 scoping review screened 3,780 publications and found no established regulatory framework for drugs targeting aging in any jurisdiction, stating explicitly that the FDA, EMA and Health Canada do not classify aging as a disease [single-source verified].

One widely repeated claim needs to be named and rebutted: **no primary FDA document — letter, guidance, Federal Register notice, or advisory committee record — accepts a composite morbidity endpoint for an "aging" indication.** I searched for one and it does not exist. This has to be named because multiple peer-reviewed reviews assert in print that "the FDA has approved TAME" — including, as it happens, the same 2025 scoping review cited above for the absence of a framework, whose supporting citation (Barzilai 2016) never mentions the FDA. A false claim appearing in both the literature supporting it and the literature refuting it is itself a diagnosis of this field's citation hygiene.

While correcting absences: "nobody has calculated how large a human lifespan RCT would need to be" was also wrong. Espeland et al. published a dedicated quantitative design paper in J Gerontol A in 2017, and TAME's own design paper specifies 3,000 participants aged 65–79 across roughly 14 centres, with mortality inside the composite endpoint. The size has been calculated; nobody has funded it.

### 6.2 Epigenetic clocks: the same DNA gives different answers

The hottest surrogate is the epigenetic clock. Its reliability problems come in two kinds that must be kept apart, because they are different in nature.

**Technical noise.** Higgins-Chen et al. 2022 report that "technical noise produces deviations up to 9 years between replicates for six prominent epigenetic clocks." One caliber correction: that 9 years is the **worst case for one clock (PhenoAge) among 36 replicate pairs**, while median deviations across the six clocks are 0.9–2.4 years. Quoting the worst case as typical is exactly the slippage this article criticizes. And the paper sells the remedy: its principal-component clock method is licensed through Yale to a consumer biological-age testing company, the replicate datasets it used were supplied by that company, and the competing-interests statement says so.

**Tissue non-comparability.** Apsley et al. 2025 (83 individuals, 284 samples, five tissues) found that blood-trained clocks read on oral samples return a much older biological age for the same person at the same moment: GrimAge2 differs by roughly 36 years between buccal swab and dried blood spot — though that cell pools 36 children aged 9–14 with adults in one paired test, for a clock trained only on adults, so the magnitude should not be read as a general adult-population parameter.

But this **must** be stated alongside the other half of the same table or it misleads: **blood versus blood is essentially flat** — dried blood spot versus buffy coat is −1.11 ± 0.81 years, non-significant, and non-significant for all seven clocks tested. So this is not "biological-age measurement is unstable," it is a **highly consistent systematic bias**: take a blood-trained ruler to oral tissue and it is reliably far off. A systematic bias can be calibrated away; random noise cannot — the engineering implications are entirely different. One further trap: the error term the source table attaches to that ~36-year gap is a **standard error** (0.68 years), not a standard deviation, so it must not be read as everyone differing by 36 years give or take a year — the implied person-to-person spread is about 5 years. In the same table, Horvath's pan-tissue clock runs the opposite direction (buccal 8–11 years *younger* than blood).

The structural picture has independent replication: Bruellman et al. 2026, in an unrelated cohort (N=91), measured saliva against buffy coat and found PhenoAge +19.72, Horvath2 +16.41 and PCGrimAge +9.10 years (all p<0.001), with all seven clocks null for PBMC versus buffy coat [multi-source]. So **the direction and structure are multi-source; the magnitude is 9–20 years, not 36.**

What this does and does not license: it does not license "different vendors will report biological ages 36 years apart" — the vendors that sample oral tissue specifically do not apply blood-trained clocks to it (Tally Health's TallyAge derives from CheekAge, trained on 8,045 buccal samples; Elysium's Index is a saliva assay). What it licenses is: **biological ages derived from different tissues are not on a common scale and are not interchangeable; and no study has ever split one person's sample across multiple commercial vendors and published the disagreement.** That last is a clean gap and can be stated as one.

### 6.3 The circularity: the original is more interesting than its retelling

A criticism of this field circulates widely: because no intervention has been validated, biomarkers are built from the changes candidate interventions produce, and then used to evaluate those interventions.

In draft I attributed this to the Biomarkers of Aging Consortium's 2024 Nature Medicine paper. On checking, that paper contains no such passage — "geroprotector" appears zero times and there is no circularity discussion. The passage is in the consortium's 2023 Cell paper, and **the original's tone is the opposite of the retelling**:

> "Importantly, there exist many candidate biomarkers of aging and many proposed geroprotectors, and the accumulated evidence supporting either could be leveraged to validate the other"

The authors treat the relationship as an **opportunity for mutual validation**, not as a confession; a figure legend acknowledges it "may appear to have a circular relationship." Written faithfully, this is more interesting: the field knows perfectly well that it stands on a bootstrap, and has chosen to treat that as a method rather than a defect. As for validation in the regulatory sense — an intervention-induced change in the marker must predict the change in outcome — no clock meets it, and no aging, biological-age, healthspan, frailty or multimorbidity biomarker appears among FDA's formally qualified biomarkers or its Table of Surrogate Endpoints.

### 6.4 The trial landscape: seven in ten enroll under a hundred people

On 28 July 2026 I queried the ClinicalTrials.gov v2 API (query.cond=Aging, interventional studies) and got 3,076 studies; three verifiers independently reproduced the same number. Of these, 2,198 (71.5%) enroll no more than 100 participants and 1,373 (44.6%) no more than 50.

But verification supplied a correction more informative than those percentages: **this is not "the geroscience landscape."** query.cond is a synonym-expanded condition search; only 1,902 studies actually list Aging in the Condition field. And within the same result set, "skin aging" returns 429 studies, "facial aging" 368 and "wrinkle" 233 — far more than metformin at 23, rapamycin at 30, NAD at 35, taurine at 5 and senolytics at 4.

That contrast is itself a conclusion: in the registry sense, the bulk of "anti-aging clinical research" by count is cosmetic medicine, not geriatric medicine.

## 7. The commercial layer: where the money is, and where the claims are

### 7.1 The NMN regulatory reversal

In 2022 the FDA determined that NMN was excluded from the dietary supplement definition because it had first been investigated as a drug: the agency's letter states that NMN and the investigational drug MIB-626 "have the same chemical structure, as confirmed by FDA's review of the relevant INDs." MIB-626 belongs to Metro International Biotech.

On 29 September 2025 the FDA reversed that position. To be precise: docket FDA-2023-P-0872 contains exactly **one** response letter (document FDA-2023-P-0872-2754, addressed to Daniel Fabricant of the Natural Products Association and Gretchen DuBeau of ANH-USA), with a second same-day letter to the Council for Responsible Nutrition filed under a different docket. The verbatim conclusion:

> "FDA has reconsidered its position… and, in light of this change in interpretation, we have determined that NMN is not excluded from the dietary supplement definition."

On 2 December 2025 the FDA wrote to SyncoZymes and Inner Mongolia Kingdomway setting aside its 4 November 2022 superseding letters. (One detail worth mentioning: the 29 September letter's own date line is printed as "September 29, 2029"; a verifier rendered page one of the PDF as an image to confirm the typo is in the document itself, with the correct date established by the digital signature block.)

One phrasing I have to withdraw: I drafted that "both ends of the regulatory chain had commercial stakes." No primary document shows that any FDA decision-maker had a commercial stake, and the phrase reads as an insinuation of capture the record does not support. What can be said is that **commercial interests were arrayed on both sides of the dispute** — a company developing NMN as a drug on one side, trade associations wanting to sell it as a supplement on the other.

### 7.2 Every market figure comes from someone selling the report

Market-size estimates for NAD+ precursor supplements differ by roughly fivefold, and **every figure I could trace** was produced by a firm selling that report (priced $2,450–$4,490). Future Market Insights, for instance, gives $876.2 million for 2025 — note the scope is "NAD precursor supplements," not the broader "NAD+ supplements" or "longevity market." I could find no government, academic or independent estimate.

The wording discipline here is the same as elsewhere in this article: "every figure I could trace," not "every figure" — the latter is an unfalsifiable universal.

### 7.3 Advertising regulation did what peer review did not

On 21 May 2026 a National Advertising Review Board panel, in case #7487-346, recommended that Niagen Bioscience (formerly ChromaDex) discontinue or modify multiple advertising claims [single-source verified].

The decision contains a sentence that is the legal formalization of this entire article: the substantiation required depends on **the message conveyed to consumers**, not on what the advertiser's cited studies happen to say. That is the four slippages in legal form: a trial judged positive on a one-sided p<0.10 with an endpoint of +17.6 m on a six-minute walk may lawfully exist; rendering it as "clinically proven to support healthy aging" is another matter.

### 7.4 An "FDA milestone" is not approval — but this time the misreading wasn't the press's

Loyal (formerly Cellular Longevity, Inc.) received FDA Center for Veterinary Medicine acceptance of the "reasonable expectation of effectiveness" (RXE) section for its canine longevity drug LOY-002 on 26 February 2025. This is not approval: it is one of several technical sections in a conditional-approval application.

But two of the three accusations I had attached to this were refuted, and I record that plainly:

- I wrote that the company itself states this is not approval. **The announcement contains no such sentence**; the relevant content appears only in an FAQ (still under review, further section acceptances required).
- I wrote that press coverage routinely renders it as FDA approval. **No such example was found.** The Washington Post's headline was "Antiaging pill for dogs clears key FDA hurdle" — accurately, as a step.
- I wrote that the STAY trial's change from 1,000 to 1,300 dogs went unexplained. **It was explained, in advance**: a dedicated post on 14 April 2025 states "we've achieved our original enrollment goal of 1,000 dogs, and we're expanding the trial to include up to 1,300 dogs."

Two points of precision remain: 26 February 2025 is the date of the **company's announcement**, not a documented FDA action (FDA/CVM published nothing), and a milestone of the form "one technical section accepted" is intrinsically easy to misread. So this section's conclusion is not "the vendor is misleading people" but something more interesting: **a structurally misreadable regulatory milestone, which this time neither the company nor the press misrepresented.** Writing it up as a scandal would be me committing the error this article is about.

### 7.5 Three named individuals

When a person is themselves part of the story, anonymizing is discarding evidence.

**David Sinclair** resigned as president of the Academy for Health and Lifespan Research (a body of roughly 60 aging scientists) in March 2024, after a February 2024 press release from Animal Bioscience — a company he founded — claimed a supplement was proven to "reverse aging" in dogs. In the peer-reviewed version of that study, "improved cognitive function" rested on changes at three months in an **owner-completed questionnaire** (CCDR) at p=0.02, and the objective cognitive test did not corroborate it. A subjective, short-window surrogate endpoint became a species-level anti-aging claim.

**Bryan Johnson** said in a WIRED interview published 21 July 2025 that he was "so close to either shutting it down or selling it" — referring to his supplement company Blueprint — because the commercial business costs him credibility. A year later there is no confirmation of any sale or shutdown. The interesting part is where the split falls: Blueprint's product-page claims are scrupulously compliant structure/function statements carrying the FDA disclaimer, with **no lifespan claim**. The brand is compliant; the founder's public narrative is not.

**Nir Barzilai's** two calibers are recorded in section 3: describing the monkey study as showing eight years of transcriptomic delay (the paper's maximum is −6.86 years, and it never measured survival), and predicting TAME's imminent start annually since 2015. He is also the only advocate in this article who has publicly discouraged a population from taking the drug he champions (people under 50 without diabetes).

## 8. A structural finding: evidence strength runs roughly opposite to market size

Put the seven sections together and one pattern is not a coincidence.

**The compound with the largest, most dose-stable effect in the ITP is rapamycin.** It is a prescription drug with a boxed warning (for its approved organ-rejection indication at daily dosing), has essentially no retail market, circulates mainly through telehealth prescriptions and self-organized communities, and its total human evidence base is 19 studies plus one failed phase 3 in 1,024 people.

**The compound the ITP explicitly failed is nicotinamide riboside** (males p=0.252, females p=0.612). It has a retail market in the hundreds of millions of dollars, hundreds of brands, an entire consumer marketing apparatus, and a human trial chain funded or supplied almost entirely by two competing vendors.

The inversion has an unmysterious structural explanation: **what can be retailed at scale must be a supplement; a supplement legally cannot be a drug; and what actually works at the animal lifespan tier is usually a drug.** Under the US DSHEA framework, a supplement may make structure/function claims without premarket review provided it notifies FDA and carries the disclaimer, but may not make disease claims. So market size is determined not by effect size but by regulatory category. Rapamycin cannot be packaged into a capsule and sold to you not because its evidence is weak, but precisely because it is a drug.

This also explains why all four signature numbers are products of slippage. When no qualified endpoint exists (section 6) and market access depends on regulatory category rather than effect size (this section), the function of "evidence" degrades from deciding what to sell into decorating what is already being sold. The slippages are not individual researchers' moral failures; they are the predictable output of that incentive structure.

## 9. Eleven testable claims

Ordered by evidence strength, each with how to test it.

**1. [multi-source] Oral NR or NMN raises circulating NAD+ but does not raise NAD+ in resting skeletal muscle.** Three independent datasets agree (Elhassan 2019 crossover, p=0.22; Remie 2020, two methods, p=0.34/0.91; Dollerup 2020, double dose and quadruple duration, no change). Test: any new biopsy trial must report muscle NAD+ itself, not only downstream metabolites.

**2. [multi-source] Metformin failed to extend mouse lifespan on the ITP's pre-specified test.** Male median +7%, P=0.35; no female effect; the ITP's only metformin lifespan experiment. Test: the ITP re-testing at a higher dose or earlier start age and reporting the result.

**3. [multi-source] Bannister 2014's "survival advantage" is an artifact of short follow-up.** Two independent national registries reverse it (Denmark IRR 1.52; Wales STR 0.819), and the Welsh team reproduced the advantage inside a three-year window and showed it reverses after five. Test: any study claiming to restore the conclusion must use non-diabetic controls, not a sulfonylurea comparator.

**4. [multi-source] Time-restricted eating's weight benefit in humans comes essentially from reduced calorie intake, not timing.** An isocaloric fed-meals trial (Maruthur 2024) found no benefit; a 12-month trial with both arms calorie-restricted found a net difference of −1.8 kg (P=0.11). Test: any timing-effect claim must reproduce under provided-meal isocaloric conditions. Counter-evidence already exists (Jamshed 2022, early window, 2.3 kg more lost), so this claim is limited to time-restricted eating and does not cover all fasting modalities.

**5. [multi-source] Human whole-blood NAD+ does not decline appreciably with age.** Two independent teams, two countries, two chemistries agree (Trętowicz 2026, seven cohorts; Yang 2022, n=1,518). Test: any "NAD+ declines" claim must name the tissue — blood now has two independent nulls, and the tissue-level evidence points the other way.

**6. [single-source verified] The ITP's small hits in the 8–12% band sit on their own power floor.** The ITP itself lists chance as an explanation in the C2022 discussion, and C2021 contains a pair of nearly identical median gains landing on opposite sides of the threshold (+8.3%, p=0.17, a miss; +8.7%, p=0.015, a hit). Test: whether any sub-10% ITP hit survives an independent re-test at its original dose and start age.

**7. [single-source verified] TAME has never enrolled anyone.** No ClinicalTrials.gov registration, no EudraCT record, and annual predictions of imminent start since 2015. Test: an NCT number appearing with actual enrollment greater than zero.

**8. [single-source verified, dual-seat restricted] The once-weekly rapamycin hypothesis was not supported the first time it was tested head-on.** RAPA-EX-01's primary endpoint was −2.13 repetitions (p=0.089 against a protocol-specified α of 0.10), pre-specified complete-case and per-protocol analyses favoured placebo significantly, and HbA1c rose without multiplicity correction. Test: a replication powered at α=0.05 with pharmacodynamic measurements; and TRIAD's canine hard endpoint whenever it reports.

**9. [direction contested] CALERIE's DunedinPACE effect is real, but its conversion into mortality risk does not hold.** The effect survives Bonferroni correction; Norway's HUNT study measured change in DunedinPACE against all-cause mortality directly and found a null, and the per-SD mortality hazard ranges from 1.23 to 1.99 across independent cohorts. Test: any independent randomized caloric-restriction trial measuring DunedinPACE — there has not been one.

**10. [single-source verified] Epigenetic "biological age" is not interchangeable across tissues, but this is a calibratable systematic bias, not random noise.** Blood versus blood is essentially flat (all seven clocks null); oral versus blood differs by 9–20 years in two independent cohorts. Test: splitting one person's sample across multiple commercial vendors and publishing the spread — a study that does not exist.

**11. [single-source verified] "Aging" is not a registrable indication in any jurisdiction, and no clock has been validated as a surrogate endpoint in the regulatory sense.** Test: a trial showing that an intervention-induced change in a clock predicts the magnitude of change in an outcome; or an aging-related entry appearing on FDA's qualified biomarker list.

## Appendix: methodology and this issue's self-corrections

The most useful record from this issue is not how many caliber problems it found in other people's work, but how many the verification process found in this article's own drafts. The ones that changed the argument:

- **"The ITP cannot replicate its own hits"** → struck down by the methods-audit seat. None of the three earlier hits was re-tested at its original dose and start age, and the new arms lack power to detect the original effect sizes. Rewritten as a stratification by effect size (large effects robust, small effects fragile), using the ITP's own language about chance.
- **"CALERIE picked 1 of 11 measures"** → forbidden as evidence of cherry-picking. The dimensional difference between pace and level means only DunedinPACE could move within a year, and that result survives Bonferroni. Redirected to challenging the mortality conversion, with the independent HUNT null introduced.
- **"No CR/fasting trial has a hard primary endpoint"** → overturned 3/3 (PREDIMED-Plus, MeMeMe). Narrowed to "no single-variable caloric-restriction or eating-timing trial."
- **"The ITP has never tested urolithin A or taurine"** → overturned; both are in the 2025 cohort.
- **"No human rapamycin RCT has a clinical primary endpoint"** → overturned; narrowed to "not in a healthy-aging population."
- **"AgelessRx conceals PEARL's missed primary endpoint," "the press calls Loyal's RXE an approval," "Loyal never explained the STAY expansion"** → all three checked and found untrue; deleted.
- **"Remie 2020 is a counterexample where NR raised muscle NAD+"** → direction reversed; it is a second-method replication of the Elhassan null.
- **"Every large NR trial carries ChromaDex money"** → universal quantifier refuted; rewritten as vendor dependence rather than a single vendor.
- **"Both ends of the NMN regulatory chain had commercial stakes"** → withdrawn in favour of "both sides of the dispute had commercial interests."
- **The circularity passage was misattributed** → not in Moqri 2024 but in Cell 2023, and the original's tone is the opposite.

The overturned and restricted material stays in the body text, not as a gesture toward honesty but because it is the actual output of the method: an evidence review that reports only "I found other people's errors" is indistinguishable from one that does not check its own.

## Appendix: principal sources

**Animal lifespan tier**: Nadon et al., Age 2008 (ITP design); Nadon et al., eBioMedicine 2017; Cheng et al., Aging Cell 2019 (control baselines); Harrison et al., Nature 2009; Miller et al., J Gerontol A 2011; Miller et al., Aging Cell 2014; Strong et al., Aging Cell 2016 (metformin); Strong et al., Aging Cell 2020; Strong et al., Aging Cell 2022; Harrison et al., GeroScience 2024; Korstanje et al., GeroScience 2026 (C2022); Jiang et al., GeroScience 2024; Garratt et al., Aging Cell 2017 (castration); NIA ITP official pages and compounds-in-testing table.

**Rapamycin human tier**: Mannick et al., Sci Transl Med 2014; Mannick et al., Lancet Healthy Longev 2021 (PROTECTOR 1); Juricic Dzankic & Partridge, Lancet Healthy Longev 2021; Moel et al., Aging 2025 (PEARL); Stanfield et al., J Cachexia Sarcopenia Muscle 2026 (RAPA-EX-01); Elliehausen et al., Aging Cell 2025; the TRIAD design paper; Kaeberlein et al., GeroScience (user survey).

**Metformin**: Bannister et al., Diabetes Obes Metab 2014; Keys et al., Int J Epidemiol 2022; Stevenson-Hoare et al., BMC Public Health 2023; Shadyab et al., J Gerontol A 2025; Keys et al., Ageing Res Rev 2025; the DPPOS 21-year mortality analysis; Konopka et al. 2019; the MASTERS trial and its corrigendum; Yang et al., Cell 2024 (cynomolgus monkeys); Barzilai et al., Cell Metab 2016 (TAME design).

**NAD+**: Massudi et al., PLoS One 2012; Zhu et al., PNAS 2015; Cuenoud et al., Front Aging Neurosci 2020; Yang et al., Front Endocrinol 2022; Trętowicz et al., Nat Metab 2026; Vinten et al., Nat Metab 2025; Trammell et al. 2016; Elhassan et al., Cell Rep 2019; Remie et al. 2020; Dollerup et al., J Physiol 2020; Martens et al., Nat Commun 2018; Yoshino et al., Science 2021 and Brenner's technical comment; Prokopidis et al., J Cachexia Sarcopenia Muscle 2025; Damgaard & Treebak, Sci Adv 2023; the NICE trial; the NOPARK registry record.

**Caloric restriction and fasting**: Ravussin et al., J Gerontol A 2015 and its 2016 erratum; Kraus et al., Lancet Diabetes Endocrinol 2019; Villareal et al. 2016 (bone density); Romashkan et al., Oncotarget 2016; Waziry et al., Nat Aging 2023; Sun et al., Clin Epigenetics 2026 (HUNT); Yaskolka Meir et al., BMC Med 2023 (DIRECT PLUS); Colman et al., Science 2009 and Nat Commun 2014; Mattison et al., Nature 2012 and Nat Commun 2017; Lowe et al., JAMA Intern Med 2020 (TREAT); Liu et al., N Engl J Med 2022 (TREATY); Maruthur et al. 2024; Jamshed et al., JAMA Intern Med 2022; Sutton et al., Cell Metab 2018; the BMJ 2025 network meta-analysis; Circulation 2024;149:AP192 and its 2025 published version; Brandhorst et al., Nat Commun 2024 (FMD).

**Endpoints and regulation**: Higgins-Chen et al., Nat Aging 2022; Apsley et al., Aging Cell 2025; Bruellman et al., Epigenetics 2026; Moqri et al., Cell 2023 and Nat Med 2024; Espeland et al., J Gerontol A 2017; the 2025 gerotherapeutics regulatory scoping review; ClinicalTrials.gov v2 API queries (2026-07-28); FDA letters of 2025-09-29 and 2025-12-02 on NMN (dockets FDA-2023-P-0872, FDA-2022-S-0023); NARB case #7487-346.

---

**Related research on this site**: this article's evidence-grading method is the same one used in [The Evidence Grades of Learning Science: Which Methods Actually Work?](https://hub.cissychen.com/deep-research/learning-science-deep.en.html) — that one deals with educational interventions and runs into the same class of problem, where a headline number turns out to come from a pre-erratum version or a corrected value gets quoted as raw. On how a single number deforms as it travels, see [The "95% of AI Pilots Fail" Physical](https://hub.cissychen.com/deep-research/ninety-five-percent-deep.en.html); on the structure in which both camps' signature numbers take equal damage, see [Screen Time and Adolescent Mental Health](https://hub.cissychen.com/deep-research/screen-time-teens-deep.en.html).
