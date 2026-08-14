export const meta = {
  name: 'indexing-endgame-round1',
  description: 'Round 1: 7 parallel research lines on passive investing / index bubble claims',
  phases: [{ title: 'Research' }],
}

const PREAMBLE = `You are one research line in a multi-agent deep-research pipeline for an article titled "指数化的终局:被动投资会破坏市场吗?" (The endgame of indexation: does passive investing break markets?). Today is 2026-08-14. Work in English internally; the article will be written later.

The article's research question: now that passive's share has (allegedly) crossed 50%, does the "index bubble / passive breaks price discovery" thesis have empirical support? The pipeline's soul is adversarial verification, so your job is to collect PRIMARY-SOURCE claims with exact calibers, not narrative.

Non-negotiable rules:
- Load web tools first: ToolSearch with query "select:WebSearch,WebFetch".
- Every claim must carry: the exact number/quote, numerator AND denominator, time window, population, and a URL to the most primary source you reached.
- Tag every claim's source tier: [PEER-REVIEWED] / [OFFICIAL] (Fed, SEC, official reports) / [VENDOR] (S&P DJI, Morningstar, BlackRock, AQR etc. — anything from a party with a commercial stake, INCLUDING SPIVA which is published by an index provider) / [PRACTITIONER] (fund letters, interviews, blogs) / [MEDIA].
- Verbatim quotes only if you saw the exact string in the fetched text. Web-fetch summarizers have previously FABRICATED quotes in this pipeline — if a fetch returns a summary, mark quotes from it as [UNCONFIRMED WORDING].
- Collect evidence AGAINST as eagerly as evidence FOR. Note conflicts of interest in both directions: active managers benefit from the bubble narrative; index giants and index providers benefit from debunking it.
- Note anything published in the last ~12 months (2025-08 to 2026-08) that updates the picture.
- Your final message IS the deliverable (raw data for the pipeline, not prose for a human). Format: markdown, one "### CLAIM n" block per claim with fields Source / Tier / Caliber notes / URL, then a final section "### CROSS-CALIBER ISSUES" listing places where sources disagree or where a popular number's caliber is slippery. Aim for the 12-25 most load-bearing claims for your line, each self-contained. Do not pad.

YOUR LINE:
`

const LINES = [
  { key: 'L1-passive-share', prompt: `L1 — Measuring the passive share. The single most quoted "fact" is that passive has crossed 50%. Establish every distinct caliber behind that:
(a) US mutual fund + ETF assets: when did index funds pass active funds (widely reported as end-2023 via Morningstar)? Exact figures.
(b) Share of TOTAL US equity market cap held by passive funds (much lower — Fed/ICI estimates ~15-20%?). Find the Investment Company Institute factbook numbers and the Federal Reserve note "The Shift from Active to Passive Investing" (Anadu, Kruttli, McCabe, Osambela) — its estimates and its risk taxonomy.
(c) Academic estimates of TRUE passive including shadow/closet indexing: Chinchilla-style. Find "How Competitive is the Stock Market?" or the paper estimating the passive share at ~33.5% or higher counting direct indexing (Sammon? "Measuring Passive Ownership"? The AQR/academic estimate that true passive is 2x the fund-based number). The paper "The Passive Ownership Share Is Double What You Think It Is" (Chinchilla — actually by Alex Chinlin? find the real authors: it's by ... just find it).
(d) Share of TRADING volume attributable to passive (very small, ~5%?) — the counterargument that passive barely trades.
(e) Global comparison: US vs Japan (BoJ ETF holdings) vs Europe.
(f) Latest 2025-2026 datapoints: has passive share kept climbing? Any new milestone in the last 12 months?` },
  { key: 'L2-warners', prompt: `L2 — The warning side, in their own words. Collect verbatim, sourced claims from the main "passive breaks markets" voices — what they ACTUALLY said, when, and what evidence each offered:
(a) Michael Green (Simplify): his thesis on passive flows, market elasticity, "the market has become a giant momentum machine"; any written pieces (his Substack "Yes, I give a fig"), podcast statements, and the specific mechanism he claims (flows-based, valuation-insensitive buying; the ~$1 passive flow moves market cap by >$1 claim). What testable predictions has he made? Any he got wrong/right?
(b) David Einhorn (Greenlight): "markets are fundamentally broken" (Feb 2024, Masters in Business interview) — exact wording and его full argument; his adaptation (buying cheap stocks that return capital, not waiting for rerating).
(c) Michael Burry Sept 2019 Bloomberg interview: "index fund bubble" / CDO comparison — exact quotes, and what he actually predicted (liquidity mismatch in small-caps/ETFs). Did anything he predicted materialize? What happened after (index kept rising)?
(d) Jack Bogle himself: his 2018 WSJ op-ed warning about concentration of ownership ("If historical trends continue, a handful of giant institutional investors will one day hold voting control of virtually every large U.S. corporation") — exact words.
(e) Grantham, Paul Singer ("passive investing is destroying markets"? find exact), Terry Smith, or other prominent warners.
(f) The other side's zingers too: Cliff Asness on passive fears ("The market is not broken because of indexing"), Fama, Bogle's rebuttals, Sheila Bair? Collect the strongest rebuttal quotes with sources.
For each: date, venue, exact quote (mark [UNCONFIRMED WORDING] if you couldn't see the raw text), and what empirical evidence (if any) the speaker cited.` },
  { key: 'L3-theory', prompt: `L3 — The theory layer: what do the models actually predict?
(a) Grossman-Stiglitz 1980 "On the Impossibility of Informationally Efficient Markets": the actual argument (equilibrium degree of disequilibrium; informed traders must earn a return on information costs). What does it predict about MORE passive? (Fewer informed traders -> bigger mispricings -> higher returns to remaining active -> self-correcting equilibrium.) Exact framing from the paper.
(b) Gabaix & Koijen "In Search of the Origins of Financial Fluctuations: The Inelastic Markets Hypothesis": the multiplier estimate ($1 of flows moves aggregate market value by ~$5), the micro vs macro elasticity distinction, publication status (Q J Econ? still WP?), and key critiques/replications of the multiplier. This is Michael Green's main academic ammunition — establish exactly what it does and does not say about passive specifically.
(c) Haddad, Huebner, Loualiche "How Competitive is the Stock Market? Evidence from How Investors' Trading Responds to the Rise of Passive Investing": their finding (active funds' demand elasticity fell/competition weakened, aggregate demand elasticity down ~11%? get exact), publication status (AER 2025?).
(d) Bond & Garcia "The Equilibrium Consequences of Indexing" (Rev Financ Stud): what does theory predict — indexing can IMPROVE welfare while worsening price efficiency? Get the actual predictions.
(e) Sharpe's "The Arithmetic of Active Management" (1991) — the baseline arithmetic argument and its known critiques (Pedersen "Sharpening the Arithmetic of Active Management" — index turnover means active can beat in aggregate).
(f) Any theory on the LIMIT case: what happens at 100% passive? Who does price discovery? (The classic "who sets prices if everyone indexes" — academic treatments, not op-eds.)` },
  { key: 'L4-price-discovery', prompt: `L4 — Empirical price discovery / informativeness. The load-bearing empirical question: has rising passive measurably damaged price efficiency?
(a) Bai, Philippon, Savov "Have Financial Markets Become More Informative?" (JFE 2016): finding (price informativeness ROSE for S&P 500 firms since 1960). Exact measure and caveats.
(b) Farboodi, Matray, Veldkamp, Venkateswaran "Where Has All the Data Gone?" (RFS): informativeness rose for large/growth firms but FELL for small firms — the divergence result. Exact.
(c) Coles, Heath, Ringgenberg "On Index Investing" (JFE 2022): Russell 1000/2000 reconstitution natural experiment — exogenous passive ownership changes have NO effect on price informativeness, earnings response, volatility? Get exact findings and magnitudes.
(d) Sammon "Passive Ownership and Price Informativeness" (Management Science 2024?): pre-earnings-announcement price informativeness DECLINED with passive ownership — the opposing result. Exact magnitudes; how reconciled with (c)?
(e) Ernst, Malenko? or Glosten, Nallareddy, Zou (ETF activity and informational efficiency: ETFs IMPROVE short-run earnings informativeness for small stocks?).
(f) Ben-David, Franzoni, Moussawi "Do ETFs Increase Volatility?" (J Finance 2018): yes, ~3.4%? higher volatility for high-ETF-ownership stocks — exact effect size, and any later critiques/refinements.
(g) Höfler/other recent (2024-2026) papers on passive share and price efficiency — anything new in the last 24 months, incl. any paper on 2024-2025 megacap concentration and passive flows (e.g. "passive flows and the Magnificent 7" type evidence, Jiang Vayanos Zheng "Passive Investing and the Rise of Mega-Firms" — THE key paper: passive flows disproportionately push up largest firms; get its mechanism and magnitudes and publication status).
(h) Market-quality aggregates: bid-ask spreads, depth over time (has liquidity worsened as passive rose? SEC/academic measures).` },
  { key: 'L5-index-effects', prompt: `L5 — Index inclusion effects, comovement, fragility events. The event-study literature: what happens mechanically when stocks enter/exit indices, and has it changed as passive grew?
(a) The index inclusion premium over time: Harris & Gurel 1986, Shleifer 1986 (~3%), rising to ~7-8% in the 1990s, then DECLINING toward zero post-2010 — Greenwood & Sammon "The Disappearing Index Effect" (2022/2024, J Finance?): exact time series and their four candidate explanations. This is a key ANTI-bubble datapoint (more passive, smaller price impact — opposite of naive prediction).
(b) Comovement: Barberis, Shleifer, Wurgler 2005 (S&P inclusion raises beta/comovement); later evidence — did comovement keep rising with passive share? Any reversal?
(c) The Tesla S&P 500 inclusion (Dec 2020) as the largest-ever index add: what happened (run-up, reversal), what it says about inclusion effects at scale.
(d) Fragility episodes attributed to passive/ETFs: Aug 24 2015 ETF dislocation (hundreds of ETFs halted, discounts), Feb 5 2018 XIV/vol-magedon, March 2020 bond ETF discounts (and the "ETFs as price discovery" reinterpretation), May 6 2010 flash crash role of ETFs. For each: what official post-mortems (SEC/BIS/Fed) concluded about whether passive STRUCTURE was the cause.
(e) BIS/IMF/FSB official assessments of passive investing and financial stability (BIS Quarterly Review "The implications of passive investing for securities markets" 2018; IMF GFSR chapters): their bottom lines.
(f) The 2025-2026 window: any new fragility episode, and how index funds behaved in the April 2025 tariff drawdown (did passive flows stay inelastic/stabilizing?).` },
  { key: 'L6-active-performance', prompt: `L6 — Active underperformance: the empirical case FOR passive, and its caveats.
(a) SPIVA U.S. Scorecard latest (2025 year-end, published ~March 2026): % of large-cap funds underperforming S&P 500 over 1/5/10/20 years. Exact numbers, and the caliber notes: survivorship correction, which benchmark, asset-weighted vs equal-weighted. Tag [VENDOR] — S&P Dow Jones sells indices.
(b) SPIVA time series: is underperformance worsening as passive grows (the Grossman-Stiglitz prediction would be the OPPOSITE: fewer active -> easier alpha)? Any year where majority of large-cap funds beat the index? (2005? 2007? recent 2025?)
(c) Morningstar Active/Passive Barometer latest: 10-yr success rates by category — where active does OK (bonds, small-cap, foreign?) vs US large cap. Tag [VENDOR] — Morningstar sells both data and index products; note their methodology differences vs SPIVA (category-average benchmark, survivorship handling).
(d) Persistence: SPIVA Persistence Scorecard — top-quartile persistence numbers (essentially zero over 5 years?).
(e) Academic side: Fama-French "Luck versus Skill" (2010) — aggregate alpha ~ -fees; Berk & Green rational model (skill exists, captured by managers via fees/AUM); Berk & van Binsbergen "Measuring Skill in the Mutual Fund Industry" (value added exists on average?). The nuance that gross alpha vs net alpha differ.
(f) The Grossman-Stiglitz test: papers testing whether alpha opportunities INCREASED as passive share rose (e.g., has dispersion/mispricing risen? Cremers? "Active Share" evidence; any 2024-2026 paper directly testing "more passive -> better active returns"). Also the practitioner claim that 2024/2025 were unusually BAD years for large-cap active despite record passive share — numbers.
(g) Fees: the actual investor-welfare case — asset-weighted average expense ratios over time (ICI data), estimated aggregate fee savings from the shift to passive.` },
  { key: 'L7-governance', prompt: `L7 — Ownership concentration, governance, antitrust, index provider power.
(a) The Big Three's (BlackRock/Vanguard/State Street) combined ownership of S&P 500 firms: current figures (average ~20-22%? of shares; % of votes cast at annual meetings ~25%?). Bebchuk & Hirst "The Specter of the Giant Three" (2019): their projection that Big Three could cast ~34% of votes within 2 decades; latest updates (2024-2026: has concentration kept rising? State Street losing share to Fidelity?).
(b) Common ownership and competition: Azar, Schmalz, Tecu airline paper (J Finance 2018) — the 3-7%? price effect claim; the replication failures/critiques (Dennis, Gerardi, Schenone JF 2022 "Common Ownership Does Not Have Anticompetitive Effects in the Airline Industry"; Koch/Panayides/Thomas; Backus-Conlon-Sinkinson ready-to-eat cereal). Where does that literature stand now — is the anticompetitive effect considered established or not?
(c) Regulatory/antitrust actions: FERC BlackRock utility case (2022? settlement 2024?), the Texas-led states' antitrust suit against BlackRock/Vanguard/State Street over coal (filed Nov 2024 — status as of 2026-08?), FTC/DOJ statements on common ownership, the SEC 13D/G amendments affecting passive managers' engagement.
(d) Stewardship capacity: Bebchuk-Hirst evidence on index funds' tiny stewardship staffing (person-days per portfolio company); the counterargument (Fisch/Kahan-Rock); pass-through voting programs (BlackRock Voting Choice — scale as of latest report).
(e) Index providers as unregulated standard-setters: MSCI/S&P/FTSE decisions moving hundreds of billions (Tesla add, China A-shares inclusion); Robertson "Passive in Name Only" / "The (mis)uses of the S&P 500" — SEC treatment of index providers (2022 request for comment; any 2024-2026 rulemaking on whether index providers are investment advisers?).
(f) The Vanguard fair-fund settlement or any 2025-2026 regulatory action involving big passive managers relevant to their market power.` },
]

phase('Research')

const results = await parallel(LINES.map(l => () =>
  agent(PREAMBLE + l.prompt, { label: l.key, phase: 'Research', model: 'opus' })
    .then(text => ({ key: l.key, text }))
))

const ok = results.filter(Boolean)
log(`Round 1 complete: ${ok.length}/7 lines returned`)
return ok