### CLAIM 1 — Bai/Philippon/Savov: price informativeness ROSE for S&P 500, but only at long horizons
- **Exact**: "price informativeness is 60% higher in 2010 than 1960 at the three-year horizon and 80% higher at the five-year horizon. The increase is also highly statistically significant. Price informativeness at the one-year horizon, which is smaller to begin with, shows only a modest increase." (verbatim, fetched PDF text)
- **Measure (numerator/denominator)**: informativeness = b(t,h) × σ_t(log M/A), from cross-sectional regression E(i,t+h)/A(i,t) = a + b·log(M(i,t)/A(i,t)) + c·(E(i,t)/A(i,t)) + sector dummies. I.e. predicted cross-sectional standard deviation of future earnings-to-assets explained by current market-cap-to-assets. Not an R², a *scaled* forecasting coefficient.
- **Population/window**: S&P 500 **nonfinancial** firms only; annual 1960–2014 (h=5 estimates end 2009); separate regression per year × horizon; Newey-West SE, 5 lags.
- **Decade regression cross-check**: "five-year price informativeness is about 50% higher in the 2000s than in the 1960s"; at h=1 decade dummies are "never larger than a quarter of the intercept, and often insignificant."
- **Robustness**: "There is no evidence of structural breaks anywhere in our sample, including the years 2000, 2001, and 2002" (Reg FD, decimalization, SOX).
- Source: Bai, Philippon, Savov, "Have financial markets become more informative?", *JFE* 122(3):625–654 (2016)
- Tier: [PEER-REVIEWED]
- URL: https://pages.stern.nyu.edu/~asavov/alexisavov/Alexi_Savov_files/BaiPhilipponSavov2016.pdf

### CLAIM 2 — BPS's own caveat: outside the S&P 500 informativeness DECLINES (buried in footnote 2)
- **Exact verbatim**: "Likely as a result of the compositional shift, price informativeness for firms beyond the S&P 500 appears to decline. Interestingly, the decline is concentrated at the short horizon… Above all, we view these results as motivating our focus on S&P 500 firms."
- **Caliber note**: this is *footnote 2* of the published paper, not a headline result. The authors attribute the decline to sample-composition change (citing Fama-French 2004), not to a real informativeness loss. The whole "markets got more informative" headline is therefore conditioned on a ~500-firm denominator out of a US listed universe that ran ~4,000–7,000 firms over the sample.
- Tier: [PEER-REVIEWED]
- URL: same as CLAIM 1

### CLAIM 3 — BPS: the decline outside the S&P 500 is entirely in LOW-institutional-ownership firms
- **Exact verbatim**: "Fig. 8 shows that this decline is entirely contained among firms with low institutional ownership… The differences are very large. Three-year price informativeness is three times larger for the high group than the low group. At the five-year horizon, it is 50% larger. The two groups are far enough apart that their price informativeness series never cross."
- **Population**: all CRSP/Compustat nonfinancial firms split at the *annual median* institutional share.
- **Caliber note**: this is a cross-sectional level gap, not a causal effect of institutional/passive ownership; institutional ownership is endogenous to firm size and liquidity.
- Tier: [PEER-REVIEWED]
- URL: same as CLAIM 1

### CLAIM 4 — Farboodi/Matray/Veldkamp/Venkateswaran: the divergence result (the direct rebuttal to BPS's headline)
- **Exact verbatim (abstract)**: "Large, growth stock prices increasingly reflect information about future firm earnings. This is the rise reflected in the previous studies. But over the same time period, the information content of small and value firm prices was flat or declining."
- **Body, verbatim**: "It shows that price informativeness has fallen over time for the market as a whole… In fact, over the past 50 years, this declining trend has eviscerated almost all of the information content in prices. This contrasts with S&P 500 firms… Consistent with their findings, we find that S&P 500 price informativeness rose."
- **Explicit on BPS**: "Bai, Philippon, and Savov (2016) is there. Their sample is S&P 500 firms. Those are large firms. For small firms, and for the entire sample, price informativeness declines."
- **Magnitude for large growth firms**: "the ability of prices to forecast future fundamentals has risen substantially, roughly six-fold."
- **Cross-sectional gap**: "moving from the lowest decile to the highest decile of size implies a 17-fold increase in price informativeness."
- **Population/window**: all US listed firms, 1962–2016 (last informativeness estimate 2010, because the measure needs 3–5y forward earnings). "Large" = 500 largest firms; "small" = the rest. Uses BPS's own measure plus a structural estimation.
- Source: NBER WP 26927 (April 2020); published *RFS* 35(7):3101–3138 (July 2022)
- Tier: [PEER-REVIEWED]
- URL: https://www.nber.org/system/files/working_papers/w26927/w26927.pdf

### CLAIM 5 — Coles/Heath/Ringgenberg (JFE 2022) published abstract: information production falls, informativeness does not
- **Verbatim published abstract**: "We empirically examine the effects of index investing using predictions derived from a Grossman-Stiglitz framework. An exogenous increase in index investing leads to lower information production as measured by Google searches, EDGAR views, and analyst reports, yet price informativeness remains unchanged. These findings are consistent with an equilibrium in which investors choose to gather private information whenever it is profitable. As index investing increases, there are fewer privately-informed active investors (so overall information production drops), but the mix of investors adjusts until the returns to active investing are unchanged. As a result, passive investing does not undermine price efficiency."
- **Cite**: *JFE* 145(3):665–683 (2022)
- Tier: [PEER-REVIEWED] (abstract retrieved from RePEc/EconPapers mirror, not the paywalled publisher page)
- URL: https://econpapers.repec.org/article/eeejfinec/v_3a145_3ay_3a2022_3ai_3a3_3ap_3a665-683.htm

### CLAIM 6 — CHR information-production magnitudes (the three headline percentages)
- **Exact, from the authors' own summary post**: "Google search volume about the stock falls by 3.8%"; "EDGAR page views fall by 14.1%"; "the number of analyst reports about the stock falls by 10.8%."
- **Also from that post**: "a stock switching indexes is accompanied by *zero* change in price efficiency"; "Our estimates are statistically well-powered, meaning that there is a high probability that our tests could find an effect if there were an effect to be found"; "the average variance ratio across all stocks—a standard measure of price *in*efficiency—was unchanged."
- **Denominator context given in the same post**: "from 2007 to 2016 the fraction of the average U.S. stock owned by passive funds quintupled from 2% to over 11%."
- **Caliber note**: percentages are *per treatment* (Russell 1000→2000 switch), not per unit of passive ownership; the treatment itself moves passive ownership by well under 1 percentage point of market cap (see CLAIM 7). Scaling these to "passive went from 2%→50%" is not licensed by the design.
- Source: Coles, Heath, Ringgenberg, Harvard Law School Forum on Corporate Governance, 2022-08-15 (author-written summary of their own JFE paper)
- Tier: [PRACTITIONER] (author summary of a [PEER-REVIEWED] paper); quotes are verbatim strings returned by the fetch, but the fetch was summarizing — treat as [LIKELY-VERBATIM, not independently re-verified against the JFE PDF]
- URL: https://corpgov.law.harvard.edu/2022/08/15/on-index-investing/

### CLAIM 7 — CHR: the actual size of the exogenous treatment (crucial for interpreting the null)
- **Exact, from the working-paper version**: treatment effect on passive ownership = **0.54% of market capitalization**; pre-treatment imbalance on passive ownership "extremely small – 0.03% of market cap." Price effect ~"0.5% following their addition to the Russell 2000 index. The results imply that our sample of U.S. equities has a price elasticity of demand of approximately -0.26."
- **Design**: RD around the annual Russell 1000/2000 reconstitution cutoff; ±bandwidths around the 1000th-ranked stock; 15 balance tests run, one significant at 10% (as expected under the null).
- **Caliber note**: this is the exact number the whole "passive does not hurt price discovery" literature rests on. A ~0.5pp shift in passive ownership at the Russell cutoff is a *local, small* treatment. A precisely-estimated zero at 0.5pp is not evidence of a zero at 30pp.
- Source: Coles, Heath, Ringgenberg, "On Index Investing," working paper draft dated 2017-10-20
- Tier: [PEER-REVIEWED] (pre-publication draft of the JFE paper)
- URL: https://business.gwu.edu/sites/g/files/zaxdzs5326/files/downloads/Paper%20Ringgenberg.pdf

### CLAIM 8 — CHR working paper found LARGE weak-form efficiency damage that the published framing de-emphasizes
- **Exact verbatim, 2017 draft**: "we find strong evidence that a change in investor composition, from active investors to passive investors, leads to a degradation in weak-form price efficiency. Using variance ratio tests… we find that increased index investing is associated with prices that significantly deviate from a random walk model. Following their addition to the Russell 2000 index, stocks experience an increase in their variance ratios of approximately 30%."
- **Same draft, abstract verbatim**: "index investing introduces noise into stock prices, but does not impact long-term price efficiency or trading by arbitrageurs. Stocks with more index investors have prices that deviate more from a random walk and exhibit higher correlations with index price movements. However, these stocks have no difference in turnover, trading volume, or earnings response coefficients."
- **Also**: "We also find that index investing is associated with a sharp increase in volatility, consistent with… Ben-David, Franzoni, and Moussawi (2016)."
- **Caliber note**: the paper's null is about *semi-strong-form* efficiency (ERC, PEAD, Hou-Moskowitz). It affirmatively finds *weak-form* degradation (+30% variance ratios), higher volatility, and higher index comovement. The 2022 published abstract and the widely-cited "passive investing does not undermine price efficiency" line do not mention the +30% variance ratio. This is the single most-misquoted result in the whole debate.
- Tier: [PEER-REVIEWED] (pre-publication draft)
- URL: https://business.gwu.edu/sites/g/files/zaxdzs5326/files/downloads/Paper%20Ringgenberg.pdf

### CLAIM 9 — Sammon (Management Science 2025): headline decline in pre-earnings informativeness
- **Verbatim abstract**: "I show that passive ownership negatively affects the degree to which stock prices anticipate earnings announcements. Estimates across several research designs imply that the rise in passive ownership over the last 30 years has caused the amount of information incorporated into prices ahead of earnings announcements to decline by approximately 1/4th of its whole sample mean and 1/6th of its whole sample standard deviation."
- **Numerator/denominator**: "averaging the estimated effects across the four measures… a 15% increase in passive ownership (i.e., the value weighted increase in passive ownership over my sample)" → the 1/4 and 1/6 figures. So: driver = +15pp VW passive ownership, 1990→2019.
- **Population/window**: US common stocks (exchange codes 1–3) matched CRSP↔IBES, 1990–2019; N = 441,238 firm-earnings observations for |Ret| and |Ret|/SD; 148,864 for PJ.
- **Cite**: *Management Science* 71(6):4582–4598, June 2025 (online 2024-09-17), DOI 10.1287/mnsc.2023.00836
- Tier: [PEER-REVIEWED]
- URL: https://marcosammon.com/images/sammon_passive.pdf

### CLAIM 10 — Sammon: the four measures and their exact cross-sectional magnitudes
- **Measures**: |Ret| (abs. market-adjusted earnings-day return); |Ret|/SD (same, scaled by 22-day pre-announcement return SD); PJ (Weller 2018 price-jump ratio = share of total move that happens *after* the release); IVD (Kelly et al. implied-vol difference for options spanning the announcement). Higher = *less* pre-announcement informativeness.
- **OLS, 90th vs 10th percentile of passive ownership in 2019 (27% vs 3%, i.e. a 24pp gap)**:
  - |Ret|: +152 bps, vs whole-sample mean 476 bps and SD 621 bps (≈1/3 of mean)
  - |Ret|/SD: +1.062, vs mean 1.999 and SD 2.579 (≈1/2 of mean, ≈2/5 of SD)
  - PJ: +0.0595, vs mean 0.395 and SD 0.479 (≈1/6 of mean)
  - IVD: +0.0268, vs mean 0.057 and SD 0.113 (≈slightly less than half the mean)
  - Coefficients: 0.0635\*\*\* (0.007); 4.425\*\*\* (0.384); 0.248\*\*\* (0.060)
- **Aggregate time-series (not causal)**: 1990→2019, mean |Ret| 2%→4%; |Ret|/SD "just above 1"→"about 3.5"; PJ 0.2→0.5; IVD 0.02→0.05. Passive share 0%→~15% VW over the same window.
- Tier: [PEER-REVIEWED]
- URL: https://marcosammon.com/images/sammon_passive.pdf

### CLAIM 11 — Sammon: the IV estimates, and why they matter for the CHR comparison
- **Instruments**: (i) Russell 1000→2000 rebalancing, using CHR's own May-market-cap proxy method ("I correctly predict Russell 1000/2000 index membership for 99.24% of stocks"); 724 treated firms, 618 control firms. (ii) S&P 500 additions.
- **Exact IV coefficients (Russell panel, N=33,293; first-stage F = 222.7)**: |Ret| 0.16\*\*\* (0.037); |Ret|/SD 11.68\*\*\* (2.352); PJ 0.90\*\* (0.417); IVD 0.36\*\*\* (0.088).
- **Verbatim**: "across all four measures, the IV estimates are 2.5-4 times as large as the OLS estimates." S&P 500 panel: "point estimates are larger in magnitude than the cross-sectional regression estimates by a factor of about 3-4."
- **Sammon's own argument against reverse causality (verbatim)**: "in the presence of the reverse causality described above, we would expect the OLS estimates to be biased upward in magnitude. The fact that the IV estimates are larger… suggest that the latter are not materially biased by these endogeneity concerns."
- **Caliber note**: IV estimates have a LATE interpretation at the Russell cutoff — same population as CHR's null. Sammon's own design also uses CHR's control-group construction and CHR's fixed-effect structure ("Following Coles et al. (2022), all three equations include firm-by-cohort fixed effects").
- Tier: [PEER-REVIEWED]
- URL: https://marcosammon.com/images/sammon_passive.pdf

### CLAIM 12 — How Sammon reconciles with CHR: he doesn't dispute them, he changes the measurement window
- **Verbatim**: "there have been mixed empirical results on the relationship between passive ownership and price informativeness. Part of this is due to the fact that, because information is hard to measure, prior work has relied on model-based measures of price informativeness… Using earnings announcements as a laboratory, I sidestep the need for a model-based measure."
- **Verbatim, on why the literature disagrees**: "passive ownership may increase informativeness about systematic information while decreasing the incorporation of idiosyncratic information (Bhattacharya and O'Hara (2018), Cong et al. (2020), Antoniou et al. (2020), Glosten et al. (2021))."
- **Verbatim, his own contribution**: "The contribution of my paper is to use earnings announcements as a laboratory to study not just the effect of passive ownership on price informativeness, but also how passive ownership affects *when* information is incorporated into prices."
- He classifies CHR under "papers which document no relationship" and notes: "relative to these papers, my estimated effects are large, but I would like to highlight that, with one exception, none of these papers are focused on the effect of passive ownership on pre-earnings announcement price informativeness."
- **Reconciliation reading**: CHR measure *long-run/semi-strong* efficiency (PEAD, ERC, anomaly mispricing) and find zero; Sammon measures *timing of information arrival relative to a known news date* and finds decline. Both can be true: prices end up right, they just get there later and more of the adjustment happens on the announcement itself.
- Tier: [PEER-REVIEWED]
- URL: https://marcosammon.com/images/sammon_passive.pdf

### CLAIM 13 — Glosten/Nallareddy/Zou: ETFs IMPROVE short-run informational efficiency (evidence against the bubble thesis)
- **Verbatim abstract**: "This paper investigates the effect of exchange-traded funds' (ETFs') activity on the short-run informational efficiency of their underlying securities. We find that ETF activity increases short-run informational efficiency for stocks with weak information environments. The increase in informational efficiency results from the timely incorporation of systematic earnings information. In contrast, we find no such effect for stocks with stronger information environments. ETF activity increases return comovement, and this increase is partly attributable to the timely incorporation of systematic earnings information. Further, ETF activity is associated with an attenuation of postearnings-announcement drift and an increase in active share lending."
- **Cite**: *Management Science* 67(1):22–47 (Jan 2021; online 2020-04-27)
- **Caliber note**: the improvement is specifically in *systematic* (market/sector-level) earnings information, and specifically for *weak information environment* (small, low-coverage) stocks. It says nothing about firm-specific/idiosyncratic informativeness — which is exactly what Höfler et al. find falls (CLAIM 18). These two results are compatible: ETFs move systematic info in faster and idiosyncratic info in slower.
- Tier: [PEER-REVIEWED]
- URL: https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2019.3427

### CLAIM 14 — Ben-David/Franzoni/Moussawi: ETF ownership raises volatility — the real number is 16%, not 3.4%
- **Verbatim abstract**: "We estimate that an increase of one standard deviation in ETF ownership is associated with an increase of 16% in daily stock volatility."
- **Unpacked, verbatim from body**: "In Column (1), a one standard deviation increase in stock ownership for S&P 500 stocks (1.44%) is associated with a 20 bps increase in daily volatility, which represents 16% of a standard deviation of the dependent variable."
- **Intraday**: "For S&P 500 stocks, a one standard deviation change in ETF ownership is associated with a 19% standard deviation increase in intraday volatility."
- **Attenuation for small stocks, verbatim**: "Extending the universe to smaller stocks (Column (4)), the effect is diluted, amounting to about 5% of a standard deviation."
- **CRITICAL CALIBER TRAP**: "16%" is **16% of one standard deviation of the volatility variable**, per one standard deviation of ETF ownership (=1.44pp of market cap). It is NOT "volatility is 16% higher." It is 20 basis points of daily volatility. The commonly-cited "3.4%" figure does not appear as a volatility effect anywhere in the paper — 3.4 bps in the text is the *ETF creation-unit fee*.
- **Cite**: *Journal of Finance* 73(6):2471–2535 (2018); NBER WP 20071 text used here
- Tier: [PEER-REVIEWED]
- URL: https://www.nber.org/system/files/working_papers/w20071/w20071.pdf

### CLAIM 15 — BDFM: their own evidence that the extra volatility is NOISE, not price discovery
- **Verbatim**: "we measure the impact of ETFs on the mean-reverting component of stock prices. Using intraday variance ratios as in O'Hara and Ye (2011), we show that price efficiency deteriorates for stocks with higher ETF ownership at the fifteen second frequency, which captures the investment horizon of ETF arbitrageurs. At the daily frequency, ETF flows trigger price reversals… In sum, ETFs appear to inflate the mean-reverting component of stock prices which suggests a deterioration in price efficiency, both intraday and at the daily frequency."
- **RD confirmation, verbatim**: "for the set of switchers to the Russell 2000, variance ratios are increasing in ETF ownership, which suggests that that price efficiency actually decreases after inclusion."
- **First stage caliber**: "top Russell 2000 members have ETF ownership larger by, on average, about 45 bps than bottom Russell 1000 stocks." The authors explicitly say they prefer the non-RD magnitudes: "we prefer to emphasize the magnitudes from the prior tables as they are more general and more conservative."
- Tier: [PEER-REVIEWED]
- URL: https://www.nber.org/system/files/working_papers/w20071/w20071.pdf

### CLAIM 16 — Jiang/Vayanos/Zheng: THE megacap paper — mechanism and exact magnitudes
- **Verbatim abstract**: "Flows into passive funds disproportionately raise the stock prices of the economy's largest firms, and especially those large firms in high demand by noise traders. Because of this effect, the aggregate market can rise even when flows are entirely due to investors switching from active to passive funds. Intuitively, passive flows increase the idiosyncratic risk of large firms in high demand, which discourages investors from correcting the flows' effects on prices. Consistent with our theory, prices and idiosyncratic volatilities of the largest S&P500 firms rise the most following flows into that index."
- **Mechanism (not the standard story)**: information is *symmetric* in their model, and the effect arises even when the index contains all firms. So it is NOT a Grossman-Stiglitz price-informativeness channel and NOT an index-addition channel. It is a risk-amplification loop: passive flows raise large-firm idiosyncratic volatility → arbitrageurs demand more compensation to lean against it → mispricing persists.
- **Exact magnitudes (1 SD increase in PassiveFlow_SP500 → quarterly excess return over the index)**: top 10 firms +0.687%; top 50 +0.528% (t 3.65–4.19; +0.557% equal-weighted); top 100 +0.303%; top 150 +0.208%; top 200 +0.145%. Monotone in size.
- **Cumulative, verbatim**: "the cumulative effect of PassiveFlow_SP500 on the excess return on the value-weighted top-50 firm portfolio is 0.528% × (0.05%/0.09%) × 99 = 29.04%. According to this estimate, the rise in passive investing over the past 25 years caused a firm that was in the top 50 of the S&P500 index during the entire period to rise by 29% more than the index."
- **Population/window**: S&P 500 sample 1996Q2–2020Q4 (99 quarters); S&P 600 sample 2001Q4–2020Q4. Passive flow = quarterly ratio of S&P500 index fund net assets to index market cap (mean 0.05%, SD 0.09%). ETF sample limited to SPY, IVV, VOO (plain-vanilla only).
- **Publication status**: NBER WP 28253 (Dec 2020) → published *Review of Financial Studies* 38(12):3461–3496 (2025). PDF version used here dated 2025-06-19.
- Tier: [PEER-REVIEWED]
- URL: https://personal.lse.ac.uk/vayanos/Papers/PIRMF_RFSf.pdf

### CLAIM 17 — JVZ: the idiosyncratic-volatility result and the placebo that makes the paper credible
- **Verbatim**: "A one-standard-deviation increase in PassiveFlow_SP500 is associated with an increase in idiosyncratic volatility by 1.86% (=20.63 × 0.09%) for firms outside the top 50, and this effect approximately doubles to 3.60% (=(19.32 + 20.63) × 0.09%) for firms in the top 50. Moreover, the incremental effect for large firms is statistically significant while the effect for other firms is not."
- **Placebo (verbatim)**: "the relationship between passive flows and excess returns on large stocks in the S&P600 is statistically insignificant." I.e. being the largest stock *in an index* does nothing; you must be among the largest in the *economy*. This is the cleanest discriminating test in the paper.
- **Idio vol definition**: quarterly SD of daily residual returns from the Fama-French three-factor model, all S&P 500 stocks.
- **Author's own caveat, verbatim**: "the 30% estimate concerns a contemporaneous effect of passive flows, which can partly mean-revert" — and the estimated 29% is "larger than in our calibration" (their model's own calibration produces at most ~4%).
- Tier: [PEER-REVIEWED]
- URL: https://personal.lse.ac.uk/vayanos/Papers/PIRMF_RFSf.pdf

### CLAIM 18 — Höfler/Schlag/Schmeling (2025): the most recent and most damaging market-quality result
- **Verbatim abstract**: "We show that an increase in passive exchange-traded fund (ETF) ownership leads to stronger and more persistent return reversals. Exploiting exogenous changes due to index reconstitutions, we further show that more passive ownership causes higher bid-ask spreads, more exposure to aggregate liquidity shocks, more idiosyncratic volatility and higher tail risk. We examine potential drivers of these results and show that higher passive ETF ownership reduces the importance of firm-specific information for returns but increases the importance of transitory noise and a firm's exposure to market-wide sentiment shocks."
- **Exact magnitudes (1 SD increase in instrumented passive ETF ownership)**: bid-ask spread +0.9 SD; liquidity beta (Pástor-Stambaugh) +0.9 SD; short-term-reversal-factor exposure +0.7 SD; left/right tail risk +19.2 / +19.4 percentage points; return variance +12.8 percentage points ("essentially replicates the result of Ben-David et al. (2018)"; "would mean to go from an average volatility of around 31% to about 47% annually"); noise share of variance +6.4pp (vs unconditional 15%); firm-specific information share −9pp; private firm-specific information −14.5pp (t = −4.3), public firm-specific slightly positive (t = 1.9).
- **Scaling given by authors, verbatim**: "a one standard deviation increase in passive ETF ownership (≈ 7 percentage points relative to an average of 9%), raises the variance share of noise by about 6 percentage points but decreases the share of firm-specific information by 9 percentage points."
- **Population/window**: all US common stocks NYSE/AMEX/NASDAQ, June 1997–Dec 2021 (stock-month panel); Russell 1000/2000 reconstitutions 2000–2020 for the IV. Avg passive ETF ownership rose to >10% of market cap by end-2021. Baseline variance decomposition: firm-specific info 65%, noise 20.5%.
- **Why this is the sharpest test**: it uses the SAME Russell reconstitution instrument as CHR (whose null is the pro-passive keystone) but over a much longer sample and with liquidity/variance-decomposition outcomes rather than PEAD/ERC — and finds large, significant damage.
- Source: Höfler, Schlag, Schmeling, "Passive Investing and Market Quality," dated 2025-03-24 (first version 2023-06-15); presented AFA 2025; SSRN 4567751
- Tier: [PEER-REVIEWED] (working paper, AFA-presented, not yet in a journal as of this search)
- URL: https://static1.squarespace.com/static/6310c0b9bb63a25599f4418c/t/68595d778232420d745297ba/1750687096033/Hoefler_PassiveInvesting_Plato2025.pdf

### CLAIM 19 — Ringgenberg congressional testimony, June 2026: the CHR author's own current framing
- **Verbatim**: "My research with Jeffrey Coles and Davidson Heath (Coles, Heath, and Ringgenberg, 2022) examines the consequences of the rise of passive ownership for stock price efficiency. We document that greater passive ownership is associated with a reduction in information production, however, we show that overall price efficiency has not significantly changed in recent years because active investors continue to gather information whenever it is profitable."
- **Verbatim, on the balance**: "Importantly, none of this means that passive investing is harmful to society in net. The benefits of low-cost, diversified investment vehicles for ordinary Americans are large and well-documented. But it does underscore that active investors provide a public service by keeping prices informative…"
- **Verbatim, acknowledging the other side**: "Several papers argue that the rise of index investing may distort prices and impact price efficiency and information production, including Wurgler (2011), Bond and Garcia (2022), and Haddad, Huebner, and Loualiche (2025)."
- **Context**: Subcommittee on Capital Markets, House Financial Services, hearing "From Wall Street to Main Street: The Future of How America Invests," 2026-06-25. Ringgenberg discloses: "I am a co-founder and past President of the Four Corners Center for Research on Index Investments, and I have served as an expert witness on matters related to my research."
- **Newest published-in-last-12-months item on this line.**
- Tier: [OFFICIAL] (congressional testimony; author disclosed potential COI)
- URL: https://docs.house.gov/meetings/BA/BA16/20260625/119401/HHRG-119-BA16-Wstate-RinggenbergM-20260625.pdf

### CLAIM 20 — FCA-commissioned literature survey (July 2025): the regulator-facing bottom line is "unsettled"
- **Verbatim**: "Overall, our understanding of the research suggests that passive investing increases the volatility of returns, though this is not equivalent to saying that volatilities have been rising over time. On the other hand, the literature has not settled on the question of passive investing's impact of price efficiency with many influential articles arguing for no impact at all."
- **Verbatim, conclusions section**: "empirical studies offer mixed evidence: some find that passive investing reduces price informativeness or leads to higher price impact, while others, using different methodologies or focusing on cross-sectional effects, report no significant impact on overall price efficiency… Overall, while passive investing is linked to heightened volatility, its precise influence on market efficiency remains an open question."
- **Key aggregate-trend fact it reports (verbatim)**: "Easley et al. (2021) point out that a simple measure of investor activeness based on the cross-sectional standard deviation of stock turnover is largely flat between 2000 and 2017. Similarly, aggregate measures of price informativeness show no sign of a trend during this period (see their Fig. 13.)."
- **Calibration magnitude it reports (verbatim)**: "Calibrations in Jiang et al. (2020) suggest that a large shift in active:passive investing (from a 90:10 split to a 40:60 split) increases the volatilities of mid- and large market capitalization stocks by between 0 - 6% (from an annual volatility of 11.13 to 11.84)."
- **Conflicting structural results it flags (verbatim)**: "[Haddad et al.] argue that the rise of passive investing has led to larger price impact and volatility and has lowered price informativeness. In a competing paper, Koijen et al. (2024) use a similar modelling approach but arrive at the conclusion that the large shift to passive investing did not influence price informativeness as, on average, capital did not flow to less-informed investors."
- **Provenance**: Allard, Farkas, Pedio, Rubio, Tonks (University of Bristol Business School), "A Survey of the Consequences of Passive Investment Funds for Financial Markets," Report for the Financial Conduct Authority, 2025-07-08. Disclosed: "independent research commissioned by the Financial Conducts Authority who are not responsible for any of the views expressed"; thanks Dimitri Vayanos among commenters.
- Tier: [OFFICIAL] (regulator-commissioned; academically authored, independence disclosed)
- URL: https://www.bristol.ac.uk/media-library/sites/business-school/documents/passive-investment-fca-report.pdf

### CLAIM 21 — Greenwood & Sammon: the index effect has VANISHED as indexation rose — a major fact against naive flow-pressure stories
- **Verbatim (NBER WP version)**: "The abnormal return associated with a stock being added to the S&P 500 has fallen from an average of 3.4% in the 1980s and 7.6% in the 1990s to 0.8% over the past decade. This has occurred despite [a rise in] index [assets]. A similar pattern has occurred for index deletions, with large negative abnormal returns on average during the 1980s and 1990s, but only -0.6% between 2010 and 2020."
- **Deletion series verbatim**: "The average effect of being removed from the S&P 500 was -4.6% in the 1980s, -16.6% in the 1990s, -12.3% from 2000-2009, and -0.6% from 2010-2020. Again, the average return in the past decade is not statistically [significant]."
- **Mechanisms they identify**: (i) trading costs fell "considerably since the early 1990s"; (ii) migrations from S&P MidCap rose "from about 40% of additions to over 80%," and by the late 2010s "direct additions had returns of 2.2%, while migrations had returns of -2.3%"; (iii) index changes became more predictable/pre-traded; (iv) more liquidity supply at the reconstitution — "in the 1990s… 15% of total volume occurred on the effective date, while in the 2010s that number increased to almost 30%."
- **Cite**: NBER WP 30748 (Dec 2022) → *Journal of Finance* 80(2):657–698 (April 2025)
- **CALIBER CONFLICT**: the NBER draft says 3.4% (1980s) / 7.6% (1990s) / 0.8% (last decade) and −0.6% for deletions; secondary summaries of the *published JF* abstract report 7.4% (1990s) / 0.3% (last decade) / 0.1% for deletions. I could not retrieve the published JF abstract directly (Wiley 403). **Do not cite the JF numbers without re-verifying against the published paper.**
- Tier: [PEER-REVIEWED]
- URL: https://www.nber.org/system/files/working_papers/w30748/w30748.pdf

### CLAIM 22 — Choi (2026): the leading recent reconciliation — passive helps efficiency ONLY where active ownership is already high
- **Reported findings**: using annual Russell 1000/2000 reconstitutions as an instrument for passive ownership, instrumented increases in passive holdings produce "economically large improvements in price efficiency—lower intraday pricing errors, weaker return autocorrelation, and faster information incorporation—in firms with substantial active ownership, but have negligible effects where active ownership is limited." The complementarity is "specific to active ownership: it is not replicated when conditioning on analyst coverage, trading activity, or institutional breadth, and only the active ownership interaction retains significance when all proxies are nested simultaneously." Consistent with an information-intermediation channel: "analyst coverage increases, forecast dispersion declines, and post-earnings-announcement drift attenuates exclusively in high-active-ownership firms."
- **Publication status**: Youngmin Choi, "The Conditional Price Efficiency of Passive Investing," SSRN 5480703, reported as April 2026. Working paper, not peer-reviewed.
- **Why load-bearing**: this is the sharpest candidate mechanism for the whole L4 contradiction — the level of passive share is the wrong X variable; what matters is the *remaining stock of active capital*. It also implies a threshold/nonlinearity that every linear study in this literature is misspecified for.
- **[UNCONFIRMED WORDING]** — SSRN returned HTTP 403; all quoted strings above come from a search-engine summary, not from fetched paper text. Must be re-verified before quoting.
- Tier: [PEER-REVIEWED] (working paper, unrefereed)
- URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5480703

### CLAIM 23 — Hu & Liang (2026): a channel by which passive ownership IMPROVES efficiency
- **Reported findings**: using firm additions to the S&P 500 as an exogenous shock, increases in passive institutional ownership lead to greater firm disclosure, with higher earnings response coefficients (ERC) and weaker post-earnings-announcement drift (PEAD) among firms with greater passive institutional ownership; the argued channel is that passive ownership promotes corporate disclosure, which facilitates the incorporation of public information into prices.
- **Cite**: Jingxin Hu and Lihong Liang, "Passive Institutional Ownership and the Informational Efficiency of Stock Prices," *Journal of Accounting, Auditing & Finance* (SAGE), 2026.
- **Note the tension**: this uses the same outcome variables (ERC, PEAD) on which CHR found *zero*, and finds *improvement*. Same family of outcomes, three different signs across three papers (CHR zero, Sammon negative on a different window, Hu-Liang positive).
- **[UNCONFIRMED WORDING]** — the SAGE page fetch failed (socket closed); the above is from a search-engine summary. Sample period, N, and magnitudes NOT obtained. Re-verify before use.
- Tier: [PEER-REVIEWED]
- URL: https://journals.sagepub.com/doi/10.1177/0148558X261435231

### CLAIM 24 — The strongest practitioner statement of the harm thesis, with a disclosed and severe conflict of interest
- **Verbatim abstract**: "The rise of passive investing has had a significant impact on financial markets in the last three decades, especially on its contribution to higher asset-price volatility, reduced liquidity, and possible contribution to heightened market concentration… this paper illustrates how passive investors, who primarily track major indices, have contributed to reduced price elasticity and market responsiveness, which, in turn, have led to amplified price movements, decreased liquidity, potential macroeconomic inefficiencies, and a disproportionate concentration of market influence in a few dominant stocks, such as the so-called 'Magnificent Seven.'"
- **Its own headline denominator (verbatim)**: "Passive investing has grown significantly over the past three decades, accounting for 50% of total equity investing in mutual funds and ETFs globally today." Data as of July 2024. Note the denominator is *mutual funds and ETFs*, not the whole market.
- **CONFLICT OF INTEREST, both directions**: co-authored by Torsten Sløk, Chief Economist of **Apollo Global Management** — a private-markets/alternatives firm whose commercial interest is in persuading allocators that public markets are structurally broken. This is the mirror image of the index-provider COI. Treat every claim in it as advocacy.
- Source: von Moltke & Sløk, "Assessing the Impact of Passive Investing over Time," Apollo Academy, November 2024
- Tier: [VENDOR]
- URL: https://www.apolloacademy.com/wp-content/uploads/2024/11/Passive-Investing-Paper-vF-112224_STAMPED.pdf

---

### CROSS-CALIBER ISSUES

**1. "Price informativeness rose since 1960" is true of ~500 firms and false of the market.** BPS's 60%/80% figures are for **S&P 500 nonfinancial firms only**. FMVV, using BPS's own measure on the full CRSP universe, find the market-wide trend has "eviscerated almost all of the information content in prices." Both are correct; they have different denominators. Anyone citing BPS as "markets got more informative, so passive is fine" is silently swapping the denominator. Conversely, FMVV's small-firm decline runs 1962–2010 and therefore **predates the passive surge**, so it cannot be attributed to passive without further work — BPS explicitly attribute the outside-S&P-500 decline to *sample composition*, not information.

**2. CHR's null is the load-bearing pro-passive result, and it is much narrower than its reputation.** The exogenous treatment is a **0.54pp shift in passive ownership** at the Russell 1000/2000 cutoff. The paper finds zero on *semi-strong-form* measures (ERC, PEAD, Hou-Moskowitz) but affirmatively finds **+30% variance ratios**, higher volatility, and higher index comovement — i.e. weak-form degradation. The published abstract's closing line, "passive investing does not undermine price efficiency," is not supported by the variance-ratio result in the same paper. The authors' own summary post uses "the average variance ratio *across all stocks*… was unchanged," which is an unconditional time-series statement about the market, not the RD treatment effect — two different objects presented adjacently.

**3. Sammon vs CHR is not a contradiction; it is a window mismatch — but this is under-argued in both papers.** CHR ask "does the price end up right?" Sammon asks "how much of the adjustment happens *before* the announcement?" Sammon uses CHR's own Russell control-group construction and gets a large negative effect on his measures; CHR get a precisely-estimated zero on theirs. Nobody has run both sets of outcomes on the same sample with the same design. The reconciliation ("passive delays idiosyncratic info while leaving eventual accuracy intact") is plausible and is what Sammon gestures at, but it is an inference, not a demonstrated result.

**4. Ben-David et al.'s "16%" is routinely mis-scaled.** It is 16% *of one standard deviation* of daily volatility, per one standard deviation (1.44pp) of ETF ownership — in levels, 20 basis points of daily volatility, for S&P 500 stocks. For the broader Russell 3000 it drops to ~5% of a SD. The "3.4%" figure circulating in the passive debate does not correspond to any volatility estimate in the paper (3.4 bps appears there as an ETF creation-unit fee). Any linear extrapolation from a 1.44pp ownership SD to today's 15–30pp passive shares is unlicensed.

**5. JVZ's 29% is a cumulative extrapolation from a contemporaneous quarterly coefficient, and the authors flag it.** 0.528% × (mean/SD ratio) × 99 quarters = 29.04%. The authors write that the estimate "is larger than in our calibration" (their model produces at most ~4%) and that it "concerns a contemporaneous effect of passive flows, which can partly mean-revert." Treat 29% as an upper bound, not a point estimate, and never as "passive inflated megacaps by 29%" without the mean-reversion caveat.

**6. Two Russell-cutoff IV papers, same instrument, opposite conclusions.** CHR (2022) and Höfler/Schlag/Schmeling (2025) both instrument passive ownership with Russell 1000/2000 reconstitutions. CHR find no efficiency effect; HSS find bid-ask spreads +0.9 SD, noise share +6.4pp, firm-specific information share −9pp (private firm-specific −14.5pp, t=−4.3). Differences: HSS use a much longer window (reconstitutions 2000–2020 vs CHR's shorter post-banding sample), measure passive *ETF* ownership specifically, and use liquidity/variance-decomposition outcomes rather than PEAD/ERC. This is the single most important unresolved empirical conflict on this line.

**7. "Passive helps small stocks" and "passive hurts firm-specific info" are the same finding seen from two sides.** Glosten/Nallareddy/Zou find ETFs improve short-run efficiency for weak-information-environment stocks — explicitly via *systematic* earnings information. HSS find passive ETF ownership *reduces* the firm-specific information share of return variance. Both can hold: ETFs speed up the arrival of market/sector-level information and slow down idiosyncratic information. A one-sentence "ETFs improve efficiency" citation of GNZ drops the word "systematic," which is doing all the work.

**8. The index-inclusion effect collapsed to zero exactly as indexation peaked.** Greenwood & Sammon show S&P 500 addition returns fell from 3.4%/7.6% (1980s/1990s) to 0.8% (2010s) and deletions from −16.6% to −0.6%. This is a direct empirical embarrassment for the simplest "passive flows mechanically distort prices" story and must be reconciled with JVZ's megacap flow-pressure result. Note the caliber conflict: the NBER draft reports 3.4%/7.6%/0.8% and −0.6%; secondary summaries of the published JF abstract report 7.4% and 0.3%/0.1%. **I could not retrieve the published JF text (Wiley 403) — the JF numbers are unverified.**

**9. Two structural-demand papers, same method, opposite answers.** Per the FCA survey: Haddad/Huebner/Loualiche conclude the rise of passive "has lowered price informativeness"; Koijen et al. (2024), using a similar demand-system approach, conclude it "did not influence price informativeness as, on average, capital did not flow to less-informed investors." Both are structural, both are calibrated to holdings data, and the disagreement is about a modelling assumption (who the marginal switcher is), not about a measurement. Do not cite either as decisive.

**10. There is no clean aggregate market-quality time series in this literature, and its absence is itself a finding.** Every credible price-efficiency result here is *cross-sectional and instrumented*, because the aggregate time series is confounded by decimalization, Reg FD, SOX, HFT, and the data revolution. The one aggregate claim I found reported is that a turnover-dispersion "activeness" measure and aggregate informativeness measures are "largely flat between 2000 and 2017" (Easley et al. 2021, via the FCA survey — **I did not verify this against the Easley paper itself; my search for it returned a different Easley et al. RFS paper**). Searches for an official SEC/DERA aggregate bid-ask-spread or depth series over the passive era returned only low-quality secondary sources. **Treat any "spreads have widened/narrowed as passive rose" claim in the article as unsourced until a primary series is obtained.** BPS also note the confound directly: they find no structural break at 2000/2001/2002.

**11. Conflicts of interest run hard in both directions on this line.** Apollo (private markets) publishes the strongest harm case — it sells the alternative. Index providers and the Big Three fund the debunking case. Notably, Ringgenberg — whose CHR null is the keystone pro-passive result — discloses in sworn congressional testimony that he "co-founded and [is] past President of the Four Corners Center for Research on Index Investments" and has "served as an expert witness." His testimony's framing is nonetheless balanced and concedes the information-production decline. Sammon (HBS) and Höfler/Schlag/Schmeling (Goethe/SAFE, DFG-funded) have no obvious commercial stake; JVZ disclose funding from the LSE Paul Woolley Centre, whose founding intellectual program is explicitly critical of index-linked investing — a mild COI in the harm direction.

**12. Nothing in this literature tests the 50%+ passive-share world.** Every causal estimate above is identified off treatments of 0.45–7 percentage points of ownership, mostly at the Russell 1000/2000 boundary, in samples ending 2019–2021. Choi's conditional result (efficiency gains only where active ownership remains substantial) implies the relationship is nonlinear in exactly the region nobody has data for. The honest empirical answer to "has passive broken price discovery at 50%" is that the identified estimates do not extrapolate there, in either direction.