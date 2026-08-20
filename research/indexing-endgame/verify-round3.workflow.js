export const meta = {
  name: 'indexing-endgame-round3',
  description: 'Round 3: dual-seat audits (counter-evidence + methodology veto) on 4 single-source load-bearing empirics',
  phases: [{ title: 'Audit' }],
}

const VERDICT = {
  type: 'object',
  additionalProperties: false,
  required: ['itemId', 'seat', 'verdict', 'reasoning', 'searchAngles'],
  properties: {
    itemId: { type: 'string' },
    seat: { type: 'string', enum: ['COUNTER_EVIDENCE', 'METHOD_AUDIT'] },
    verdict: { type: 'string', enum: ['UPGRADE_MULTISOURCE', 'SINGLE_SOURCE_OK', 'RESTRICTED_USE', 'DIRECTION_CONTESTED', 'VETO'] },
    reasoning: { type: 'string', description: 'Full findings. For COUNTER_EVIDENCE: every independent measurement found (team, data, direction) and every angle searched that returned nothing. For METHOD_AUDIT: the hostile referee report — sample, identification, inference, COI, robustness.' },
    searchAngles: { type: 'array', items: { type: 'string' }, description: 'All search angles tried, including dead ends' },
    usageConditions: { type: 'array', items: { type: 'string' }, description: 'If RESTRICTED_USE: exact conditions under which the article may still use the number' },
  },
}

const PREAMBLE = `You are one seat of a two-seat audit on a SINGLE-SOURCE load-bearing empirical claim in a deep-research article about whether passive investing is breaking markets. Today is 2026-08-15. The claim has already survived 3-vote verbatim verification (Round 2) — your job is NOT to re-check transcription. Load tools first: ToolSearch with query "select:WebSearch,WebFetch". Local primary-text extracts live in /private/tmp/claude-502/-Users-cissychen-design/0f8bdcde-3464-42f4-af17-1552808c31d6/scratchpad/ (run ls).

SEAT DEFINITIONS:
- COUNTER_EVIDENCE seat: hunt for INDEPENDENT measurements — different team AND different data — that confirm or contradict the finding's direction and magnitude. Record every angle you searched, including the ones that returned nothing. Verdict UPGRADE_MULTISOURCE if >=1 genuinely independent same-direction measurement exists; DIRECTION_CONTESTED if independent measurements point the other way; SINGLE_SOURCE_OK if you find nothing either way after a thorough hunt.
- METHOD_AUDIT seat: hostile referee with VETO power. Attack: sample size and window, identification strategy, inference (SEs, multiple testing, extrapolation), construct validity, version drift, author incentives. VETO means the number must NOT be load-bearing in the article (may only appear as a weak/disputed claim). RESTRICTED_USE means it can be used only under conditions you enumerate.

Return via the structured schema. Be specific; name papers with authors, venue, year.

ITEM TO AUDIT:
`

const ITEMS = [
  { id: 'R3A', label: 'Chinco-Sammon 33.5%', claim: `Chinco & Sammon (JFE 157, July 2024): total US passive ownership was ~33.5% of market cap in 2021 (vs 16% for index funds alone), measured from reconstitution-day total volume across five indexes; proxy family runs 13.31% (closing-auction-only) to 38.5% (adding Vanguard CRSP assets). The article uses this as its central "the true passive share is far above the fund-based number" measurement.
Counter-evidence angles to try: (a) any independent estimate of total/shadow passive share (e.g., BlackRock 2017 ~18% of global equity; Bank of England; academic closet-indexing literature — Cremers-Ferreira-Matos-Starks holdings-based; ICI rebuttals; S&P DJI indexed-assets survey $13T-to-S&P500-alone ≈ 21% of US cap — is that independent corroboration?); (b) any critique or replication of the reconstitution-volume method since 2024.
Method-audit angles: the method counts ALL reconstitution-day volume as passive rebalancing; five-index coverage; interpolated pre-2009 weights; the 13.31%-vs-16% statistical indistinguishability the authors concede; version drift 37.8→33.5.` },
  { id: 'R3B', label: 'HHL 11% inelasticity', claim: `Haddad, Huebner & Loualiche (AER 115(3) 2025): the rise of passive investing over ~2001-2020 made aggregate demand for individual stocks 11% more inelastic (pass-through 0.33 x 32% log-drop in active share); strategic competition offsets two-thirds. The article uses this as its best-identified causal magnitude for "passive changed how prices respond to trading."
Counter-evidence angles: independent estimates of rising demand inelasticity or its absence — van der Beck (JFE 2026) short-vs-long-run elasticities; Koijen-Yogo demand-system literature; Behmaram 2026 (stock-level passive ownership and elasticity, 40% less elastic, index additions -12%); Gabaix-Koijen macro multiplier; any paper contesting the Koijen-Yogo demand-system identification (Fuchs-Fukuda-Neuhann 2025?).
Method-audit angles: 13F quarterly holdings identify elasticities only under strong assumptions; elasticity-based active/passive classification (passive = KY elasticity < 0.06) is model-defined, not observed; the counterfactual holds other trends fixed; version drift 15%→11% with chi 2.15→2.97; the 11% rests on the broad measure (19→41% of market cap) not the fund-based one (6.3%).` },
  { id: 'R3C', label: 'Sammon pre-announcement informativeness', claim: `Sammon (Management Science 71(6) 2025): pre-earnings-announcement price informativeness declined 1990-2019 and is causally linked to passive ownership (OLS headline: 15% more passive ownership -> pre-announcement informativeness falls by ~1/4 of its mean; IV 2.5-4x larger; reduced form weak). The article uses this as the strongest evidence that SOME price-discovery channel measurably deteriorated.
Counter-evidence angles: independent teams/data on pre-announcement information: Weller (RFS 2018) "Does Algorithmic Trading Reduce Information Acquisition?" uses the same price-jump ratio — what does it attribute the trend to?; Bennett-Stulz-Wang GPIN result (S&P additions); Kacperczyk-Nosal-Sundaresan same price-jump measure opposite sign; Glosten-Nallareddy-Zou ETF improves systematic-info efficiency; Israeli-Lee-Sridharan (2017) ETF ownership worsens information environment; Hu-Liang (JAAF 2026) passive improves ERC via disclosure; earnings-announcement-timing literature (more info released AT announcements over time — Beaver et al: announcement informativeness RISING for reasons unrelated to passive).
Method-audit angles: |Ret| rising could reflect MORE information content of announcements (earnings becoming more informative) rather than less pre-announcement discovery — the measures cannot separate "less anticipation" from "bigger surprises/more disclosure at announcement"; confounds: Reg FD (2000), insider-trading enforcement, 8-K expansion, guidance practices; reduced form "almost always insignificant"; value-weighting shrinks |Ret| coefficient; sample ends 2019.` },
  { id: 'R3D', label: 'JVZ megacap gradient', claim: `Jiang, Vayanos & Zheng (RFS 38(12) 2025): flows into S&P500 index funds disproportionately raise the largest stocks' prices (one-SD PassiveFlow: top-10 +0.687%/qtr, monotone down to top-200 +0.145% ns), with linear-extrapolated cumulative top-50 effect of 29% over 1996-2020 vs their own calibration's 0-4%. The article uses this as the best-credentialed evidence that passive flows distort the relative price of megacaps (the "passive inflates the Mag 7" mechanism).
Counter-evidence angles: independent evidence on passive flows and large-stock relative pricing: Vanguard's mid-cap-ownership rebuttal (index funds' proportional ownership is highest in MID-caps — does that contradict?); Haddad et al Figure 3 (large firms lower elasticity — corroborates?); Chinco-Sammon reconstitution non-effect; Greenwood-Sammon; any 2025-26 paper on concentration and passive (Goldman/GMO practitioner estimates; the "passive did not cause concentration" literature — e.g., research attributing concentration to earnings concentration); international evidence (Japan BoJ ETF distortions literature — Charoenwong/Morck/Wiwattanakantang on BoJ purchases and stock prices as a natural experiment of price-insensitive buying).
Method-audit angles: PassiveFlow is a contemporaneous ownership-share change partly built from prices (mechanical correlation risk); 99 quarterly observations, R^2 0.05-0.21; the 29% is the authors' own linear cumulation of a coefficient they say partly mean-reverts, 7x their calibration; the narrow passive measure (4.95% of index cap); placebo has lower power; gradient loses significance by top-200.` },
]

phase('Audit')

const results = await pipeline(
  ITEMS,
  (it) => parallel(['COUNTER_EVIDENCE', 'METHOD_AUDIT'].map(seat => () =>
    agent(PREAMBLE + it.claim + `\n\nYou hold the ${seat} seat for itemId "${it.id}". Work independently.`, {
      label: `${it.id}:${seat === 'COUNTER_EVIDENCE' ? 'counter' : 'audit'}:${it.label}`,
      phase: 'Audit',
      model: 'opus',
      schema: VERDICT,
    })
  )).then(seats => ({ item: it.id, label: it.label, seats: seats.filter(Boolean) }))
)

const ok = results.filter(Boolean)
log(`Round 3 complete: ${ok.length} items, ${ok.reduce((a, r) => a + r.seats.length, 0)} seats`)
return { items: ok }