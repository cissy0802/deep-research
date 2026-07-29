export const meta = {
  name: 'longevity-evidence-round3',
  description: 'Round 3: dual-seat audit (contradiction search + methods audit with veto) on 6 single-source load-bearing empirics',
  phases: [{ title: 'Audit' }],
}

const SEAT = {
  type: 'object',
  additionalProperties: false,
  required: ['id', 'seat', 'ruling', 'findings', 'reasoning'],
  properties: {
    id: { type: 'string' },
    seat: { type: 'string', enum: ['contradiction-search', 'methods-audit'] },
    ruling: {
      type: 'string',
      enum: ['upgrade-multisource', 'single-source-verified', 'direction-contested', 'restricted-use', 'VETO'],
      description: 'upgrade-multisource = independent team + independent data measured the same thing in the same direction. single-source-verified = traceable to primary but still one source. direction-contested = an independent measurement points the other way. restricted-use = usable only with stated limits. VETO (methods-audit seat only) = may not bear weight in the article at all.',
    },
    findings: { type: 'array', items: { type: 'string' } },
    searchAngles: { type: 'array', items: { type: 'string', description: 'Contradiction seat: every angle you searched, INCLUDING the ones that returned nothing. The nulls are part of the record.' } },
    permittedUse: { type: 'string', description: 'Exactly what the article may say using this evidence, and what it may not say.' },
    reasoning: { type: 'string' },
  },
}

const CONTRA = `You occupy the CONTRADICTION-SEARCH SEAT for a deep-research article on longevity-intervention evidence. Today is 2026-07-28.

Your job is NOT to check whether the finding was reported correctly — a previous round already did that. Your job is to find out whether an INDEPENDENT TEAM using INDEPENDENT DATA has measured the same thing, and what they got. You are hunting for the second opinion that either corroborates or contradicts.

Do this:
1. Identify precisely what quantity is being claimed.
2. Search hard for independent measurements of that same quantity: other cohorts, other labs, other countries, other assay methods, later replications, meta-analyses, letters and technical comments. Check whether apparent corroborators are actually independent — shared authors, shared cohort, shared funder, or shared upstream dataset all break independence, and this is the single most common way a field fakes replication.
3. Record EVERY search angle you tried, including the ones that returned nothing. A documented absence is a finding.
4. Rule: upgrade-multisource / single-source-verified / direction-contested / restricted-use.

Use WebSearch and WebFetch (load via ToolSearch: "select:WebSearch,WebFetch"). Never fill a gap from memory. If a fetch returns a summarizer rendering rather than document text, do not treat any "quote" in it as verbatim — a previous run of this pipeline caught a summarizer fabricating quotes outright.

THE FINDING TO AUDIT:
`

const AUDIT = `You occupy the METHODS-AUDIT SEAT for a deep-research article on longevity-intervention evidence. Today is 2026-07-28. YOU HAVE VETO POWER: if you rule VETO, this number may not bear weight anywhere in the article.

You are a hostile peer reviewer. Assume the finding is an artifact and try to show it. Attack, in order:
1. Sample size and power. What is the actual N in the cell that produces the headline? Is it powered for the claim? What is the minimum detectable effect?
2. Inferential statistics. Is there any? Pre-specified or post-hoc? One- or two-sided? What confidence level? How many outcomes/subgroups/timepoints were examined, and was multiplicity handled? Is a null being reported as evidence of absence?
3. Selection and measurement. How were participants/animals/samples chosen? Any differential attrition, completers-only analysis, or informative censoring? Is the measurement instrument validated for this use?
4. Conflicts of interest and provenance. Who funded it, who supplied the product, who profits, who holds the patent. Is the "independent" replication actually independent?
5. Generalization. Does the population/species/dose/duration studied support the claim being drawn from it?

Rule: single-source-verified (survives audit as one source) / restricted-use (usable only within stated limits) / VETO (may not bear weight). State in permittedUse exactly what the article may and may not say.

Use WebSearch and WebFetch (load via ToolSearch: "select:WebSearch,WebFetch"). Reach the primary document. Do not fill gaps from memory.

THE FINDING TO AUDIT:
`

const ITEMS = [
  { id: 'R1', label: 'NAD+ whole-blood non-decline', finding: `Trętowicz MM, Scantlebery AML, Schomakers BV, et al., "Human whole-blood NAD+ levels do not vary with age or lifestyle interventions", Nature Metabolism 2026;8(6):1282-1290, DOI 10.1038/s42255-026-01537-5, PMID 42135539, e-published 14 May 2026. 32 authors (Amsterdam UMC, Helsinki, Leiden, Valencia). Measured NAD+ by validated UHPLC-HRMS across seven independent human cohorts and reported that whole-blood NAD+ does not decline with age.

WHY IT IS LOAD-BEARING: the article intends to use this as the strongest single piece of evidence that the founding premise of the NAD+ supplement industry — "NAD+ declines with age, so replace it" — is not established in humans. If this paper cannot carry that weight, the article's NAD+ section loses its spine.

KNOWN ISSUES ALREADY FLAGGED, which you should not merely repeat but go beyond: (i) the paper's own abstract concedes the decline is "widely proposed" in blood AND TISSUES and then restricts its own evidence to whole blood, so it does not by itself refute a tissue-level decline; (ii) an October 2025 Nature Metabolism review often cited alongside it (Vinten et al.) shares five authors and its senior authorship (Janssens, Houtkooper) with this paper, so it is NOT independent corroboration; (iii) a larger in-vivo human brain 31P-MRS dataset exists (Cuenoud et al., Front Aging Neurosci 2020, n=50) reporting only "an inverted trend between age and NAD level".

CONTRADICTION SEAT: find independent measurements of age-related NAD+ levels in humans — other cohorts, other assay methods (enzymatic cycling vs LC-MS vs 31P-MRS), other tissues (muscle, liver, brain, skin, PBMC). Does an independent team with independent data find a decline or not? Establish the actual state of the evidence, in both directions.
METHODS SEAT: audit the seven cohorts (are they really independent? cross-sectional or longitudinal? age ranges? N per cohort? confounded by health status?), the assay, and whether "no decline" is a powered null or an underpowered one.` },

  { id: 'R2', label: 'RAPA-EX-01', finding: `RAPA-EX-01 (2026): a randomised, placebo-controlled trial of sirolimus 6 mg once weekly vs placebo for 13 weeks in 40 sedentary adults aged 65-85 (mean 72.2 y, 47.5% female), testing the "cycling hypothesis" that alternating mTORC1 inhibition enhances adaptation to exercise. Pre-specified primary endpoint: change in 30-second chair-stand repetitions at 13 weeks, ITT, ANCOVA adjusted for baseline performance, age stratum and sex. Result: adjusted mean difference (sirolimus - placebo) = -2.13 repetitions (95% CI -4.61 to 0.34; p = 0.089) — not statistically significant, and numerically FAVOURING PLACEBO. Safety: HbA1c rose in the sirolimus arm (+1.74 mmol/mol; 95% CI 0.20-3.27; p = 0.030).

WHY IT IS LOAD-BEARING: the article intends to use this as the first direct human test of the intermittent/low-dose rapamycin regimen that the entire off-label longevity community relies on — and to report that it came back null on its primary endpoint with an adverse metabolic signal. That is a strong claim resting on one small trial.

CONTRADICTION SEAT: find any other human trial of intermittent or weekly-dose rapamycin/sirolimus in a non-transplant, non-disease population with a functional or metabolic endpoint. Does anything corroborate or contradict the direction? Include PEARL (AgelessRx, 48 weeks, n=114 completers) and any 2025-2026 trials. Also search specifically for human evidence on whether intermittent dosing spares mTORC2 and therefore avoids immunosuppression/metabolic effects — the article believes there is NO human evidence for this central pharmacological premise, so try hard to refute that absence.
METHODS SEAT: n=40 over 13 weeks with a chair-stand primary. What effect size was this powered to detect? Is p=0.089 in the direction of harm being over-read? Is a single HbA1c contrast at one timepoint among many safety labs a multiplicity artifact? Who funded it? What does the trial's registration say the primary endpoint was, and does it match the publication?` },

  { id: 'R3', label: 'Keys 2022 metformin reversal', finding: `Keys MT, Thinggaard M, Larsen LA, Pedersen DA, Hallas J, Christensen K. "Reassessing the evidence of a survival advantage in Type 2 diabetes treated with metformin compared with controls without diabetes: a retrospective cohort study." Int J Epidemiol 2022;51(6):1886-1898 (PMID 36287641). Danish National Health Registers 1996-2012, singletons AND discordant twin pairs. Reported that metformin monotherapy vs no diabetes "was associated with increased mortality in both singletons (IRR = 1.52, 95% CI: 1.37, 1.68) and discordant twin pairs" — i.e. the opposite direction from Bannister et al. 2014, which is the founding study of the metformin-as-longevity-drug hypothesis.

The article also intends to use the "forensic" observation from Keys' Discussion that three of the four crude mortality cells replicate almost exactly across the two countries (metformin-matched non-diabetic controls 16.9 Denmark vs 15.2 UK; sulfonylurea-matched controls 28.4 vs 28.7; sulfonylurea-treated 49.0 vs 50.9), so the UK/Denmark disagreement localises to the metformin-treated cell rather than being a general country difference.

WHY IT IS LOAD-BEARING: the article's metformin section turns on the founding epidemiological claim having been reversed by an independent team with independent national data.

CONTRADICTION SEAT: has anyone replied to, rebutted, or replicated Keys? Are there independent target-trial emulations or national-register studies of the SAME comparison (metformin initiators vs matched non-diabetics, all-cause mortality)? Note that Shadyab/Kim et al. 2025 (Women's Health Initiative, HR 0.70 for death before age 90) is an ACTIVE-COMPARATOR study (metformin vs sulfonylurea) and therefore does not test the same contrast — establish clearly which studies test which contrast, because conflating them is exactly how this literature stays confused.
METHODS SEAT: audit Keys. Is the discordant-twin analysis powered? What is the N of twin pairs? Does the Danish design have its own immortal-time or prevalent-user problems? Is "increased mortality on metformin vs non-diabetics" itself confounded by simply having diabetes — i.e. is the comparison meaningful at all, in EITHER direction? That last question matters: if the whole metformin-vs-non-diabetic contrast is uninterpretable, the article should say so rather than treating Keys as the correct answer to Bannister's question.` },

  { id: 'R4', label: 'CALERIE DunedinPACE', finding: `Waziry R, Ryan CP, Corcoran DL, et al., Nature Aging 2023: post-hoc analysis of banked CALERIE-2 specimens, N=197 with DNA methylation data of 220 randomised. Eleven DNAm measures of aging were tested: ten epigenetic clocks (Horvath, Hannum, Horvath Skin & Blood, PhenoAge, GrimAge — each in original and principal-component form) plus DunedinPACE. ALL TEN CLOCKS WERE NULL in intention-to-treat at both 12 and 24 months. Only DunedinPACE moved: 12-month ITT d = -0.29 (95% CI -0.45, -0.13), p = 4.83E-04; 24-month d = -0.25 (95% CI -0.41, -0.09).

The paper's own Discussion contains the translation "the CALERIE treatment effect of 2-3% slower pace of aging corresponds to a reduction in mortality risk of as much as 10-15%, similar to the effect of smoking cessation" — in the authors' own voice, benchmarked against Anthonisen 2005 (Lung Health Study, a randomized trial).

Context that matters: CALERIE-2 prescribed 25% caloric restriction but delivered 11.9 ± 0.7% (a formal 2016 erratum corrected the earlier 11.7% figure), front-loaded as ~19.5% in the first 6 months and ~9.1% thereafter.

WHY IT IS LOAD-BEARING: this is the single most-cited human result in the entire caloric-restriction field and the article intends to present it as one significant measure out of eleven tested, in a post-hoc analysis, on an unvalidated surrogate.

CONTRADICTION SEAT: has any independent trial measured DunedinPACE (or any clock) as an outcome of a randomized caloric-restriction or fasting intervention? Are there independent analyses of the CALERIE specimens by other teams? Has anyone published a critique or re-analysis of this specific result? What happened to DunedinPACE in other RCTs of other interventions — does it move easily (which would make it a weak discriminator) or rarely?
METHODS SEAT: eleven measures tested, one significant. Was multiplicity controlled? Was DunedinPACE pre-registered as the analysis of interest or selected after? Note the paper's own taxonomy treats DunedinPACE separately from "clocks" — assess whether that separation is principled or convenient. Also audit the authors' mortality translation: is it legitimate to carry an observational cohort's DunedinPACE-mortality association onto a treatment-induced change in DunedinPACE? Rule on whether the article may state a mortality implication at all.` },

  { id: 'R5', label: 'ITP 2026 non-replication', finding: `The NIA Interventions Testing Program's Cohort 2022 report (Korstanje R, Strong R, Salmon AB, et al., GeroScience, PMID 41843349): eleven intervention ARMS built from eight distinct agents/combinations (astaxanthin, meclizine, mitoglitazone, pioglitazone, alpha-ketoglutarate, mifepristone, methotrexate, atorvastatin-telmisartan), and none significantly increased lifespan in either sex. Three agents previously reported BY THE ITP ITSELF as male lifespan extenders were re-tested and did not reproduce: astaxanthin (+12% male median, p=0.003, in the 2024 C2019 report), meclizine (+8% male median, p=0.03, same 2024 report, 800 ppm from 12 months), and mitoglitazone (+9%, p=0.015, in the 2025 C2021 report, 300 ppm from 7 months).

Important counter-framing already identified: the ITP itself frames this as dose/start-age sensitivity rather than failed replication — the abstract says the three "showed no benefit when administered at different doses or starting at later ages" and warns of "the challenges of translating promising initial findings into consistent lifespan benefits at other doses or with alternate starting ages". Mitoglitazone was the only one re-tested at its ORIGINAL dose (300 ppm) and still showed a numerically positive male effect (+7.75% median, p=0.176). Meclizine's high-dose arm produced the largest male median gain in the whole cohort (+9.23%) at p=0.396. In females, astaxanthin, late-start mitoglitazone and pioglitazone were associated with SIGNIFICANTLY REDUCED lifespan when pooling all three sites — but the ITP reanalysed after finding unusually long-lived control females at The Jackson Laboratory.

WHY IT IS LOAD-BEARING: the article intends to argue that even the field's gold-standard program does not consistently reproduce its own hits — which is a strong claim about the best evidence in the field, and the ITP's own framing partly resists it.

CONTRADICTION SEAT: find any independent (non-ITP) replication attempt of astaxanthin, meclizine or mitoglitazone lifespan effects in mice. Also establish the broader base rate: how often do ITP hits replicate within the ITP when re-tested? Are there other documented ITP self-non-replications (e.g. across doses or start ages) besides this cohort?
METHODS SEAT: are the C2022 arms individually powered to detect the original effect sizes (+8% to +12% male median)? If not, "no significant effect" is not evidence of absence, and the article's claim must be weakened accordingly — say so explicitly. Audit the JAX control-female anomaly and the reanalysis decision: was excluding a site post-hoc? Rule on exactly how strongly the article may state the non-replication.` },

  { id: 'R6', label: 'cross-tissue clock discordance', finding: `Apsley AT, Ye Q, Caspi A, et al., "Cross-tissue comparison of epigenetic aging clocks in humans", Aging Cell 2025, PMID 39780748, DOI 10.1111/acel.14451, PMC11984668. Table 2 ("Pairwise within-person differences in standard epigenetic clocks across tissue types") reports a GrimAge2 buccal-vs-dried-blood-spot within-person difference of 35.78 ± 0.68 years, p<0.001. Total analytic sample 83 individuals (the buccal-vs-DBS cell is a subset of pairs, not 83 pairs).

Crucial limit already identified: the effect is NOT general across tissues. In the same GrimAge2 row, DBS vs buffy coat is -1.11 ± 0.81 and non-significant, and DBS vs PBMC is only 5.16 ± 0.56. The tens-of-years discordance is confined to oral-vs-blood contrasts, i.e. it largely reflects applying blood-trained clocks out of their training tissue.

WHY IT IS LOAD-BEARING: the article intends to use this to argue that consumer "biological age" results are not comparable across vendors that sample different tissues, and more broadly that the measurement layer under every longevity claim is unstable.

CONTRADICTION SEAT: find independent cross-tissue clock comparisons (other cohorts, other clock sets, saliva vs blood). Does an independent team reproduce discordance of this magnitude for oral-vs-blood? Separately and importantly: is there ANY published head-to-head study that splits one person's sample across multiple COMMERCIAL direct-to-consumer biological-age vendors and reports the disagreement? The article believes no such study exists — try hard to refute that.
METHODS SEAT: audit the design (how many pairs per cell, paired or unpaired, ±SE or ±SD, multiplicity across a large clock×tissue table). Assess whether a blood-trained clock applied to buccal cells produces a *meaningful* discordance or merely a *predictable* one — and rule on whether the article may use this to say anything about consumer tests, given that vendors may use tissue-appropriate models. State exactly what may be claimed.` },
]

phase('Audit')

const results = await pipeline(
  ITEMS,
  (it) => parallel([
    () => agent(CONTRA + it.finding + `\n\nReturn with id "${it.id}" and seat "contradiction-search".`, {
      label: `${it.id}-contra:${it.label}`, phase: 'Audit', model: 'opus', schema: SEAT,
    }),
    () => agent(AUDIT + it.finding + `\n\nReturn with id "${it.id}" and seat "methods-audit".`, {
      label: `${it.id}-audit:${it.label}`, phase: 'Audit', model: 'opus', schema: SEAT,
    }),
  ]).then(seats => ({ id: it.id, label: it.label, seats: seats.filter(Boolean) }))
)

const ok = results.filter(Boolean)
log(`Round 3 complete: ${ok.length} items, ${ok.reduce((a, r) => a + r.seats.length, 0)} seats`)
return { items: ok }
