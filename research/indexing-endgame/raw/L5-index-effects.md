### CLAIM 1
**Baseline index effect, first documentation (Shleifer)**
- Verbatim abstract: "Since September, 1976, stocks newly included into the Standard and Poor's 500 Index have earned a significant positive abnormal return at the announcement of the inclusion. This return does not disappear for at least ten days after the inclusion. The returns are positively related to measures of buying by index funds, consistent with the hypothesis that demand curves for stocks slope down."
- Source: Shleifer, A., "Do Demand Curves for Stocks Slope Down?", *Journal of Finance* 41(3), July 1986, pp. 579–590.
- Tier: [PEER-REVIEWED]
- Caliber notes: Abstract text retrieved from the publisher-deposited Crossref record (not a summarizer), so wording is exact. The abstract itself carries **no number**; the "~3%" figure universally attributed to Shleifer (1986) comes from secondary citation. Greenwood & Sammon characterise it as "approximately 3 percent"; the Fed's Anadu et al. characterise it as "a 3-4 percent boost". Population = NYSE/AMEX stocks added to S&P 500 from Sept 1976 (announcement dates first recorded then) to 1983. Denominator = the stock's own price (abnormal return), not an index.
- URL: https://api.crossref.org/works/10.1111/j.1540-6261.1986.tb04518.x

### CLAIM 2
**Baseline index effect, the reversal result (Harris & Gurel)**
- Verbatim abstract (final sentences): "The results are consistent with the price‐pressure hypothesis: immediately after an addition is announced, prices increase by more than 3 percent. This increase is nearly fully reversed after 2 weeks."
- Source: Harris, L. and E. Gurel, "Price and Volume Effects Associated with Changes in the S&P 500 List: New Evidence for the Existence of Price Pressures", *Journal of Finance* 41(4), Sept 1986, pp. 815–829.
- Tier: [PEER-REVIEWED]
- Caliber notes: Crossref publisher-deposited abstract, exact wording. Note the direct conflict with CLAIM 1 in the SAME journal volume-year: Harris–Gurel say the effect is **nearly fully reversed in 2 weeks** (temporary price pressure); Shleifer says it "does not disappear for at least ten days" (permanent, downward-sloping demand). The canonical "~3% index effect" therefore has two incompatible interpretations from birth. Window: "immediately after announcement" vs "+2 weeks"; sample = S&P 500 list changes, 1973–1983 period.
- URL: https://api.crossref.org/works/10.1111/j.1540-6261.1986.tb04550.x

### CLAIM 3
**Published headline of "The Disappearing Index Effect"**
- Verbatim published abstract: "The abnormal return associated with a stock being added to the S&P 500 has fallen from an average of 7.4% in the 1990s to less than 1% over the past decade. This has occurred despite a significant increase in the share of stock market assets linked to the index. A similar pattern has occurred for index deletions, with large negative abnormal returns during the 1990s but an average return of only 0.1% between 2010 and 2020. We investigate the drivers of this phenomenon and discuss implications for market efficiency. We document a similar decline in the index effect among other families of indices."
- Source: Greenwood, R. and M. Sammon, "The Disappearing Index Effect", *Journal of Finance* 80(2), April 2025, pp. 657–698. DOI 10.1111/jofi.13410.
- Tier: [PEER-REVIEWED]
- Caliber notes: Abstract via Crossref publisher deposit (Wiley returns HTTP 403 to direct fetch, so I could not read the published tables). Published calibers differ from every working-paper version — see CROSS-CALIBER ISSUES #1. Population = S&P 500 additions/deletions 1980–2020; "the past decade" = 2010–2020. Last clause is the load-bearing generalisation: the decline is not S&P-specific.
- URL: https://api.crossref.org/works/10.1111/jofi.13410 (record); paper: https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13410

### CLAIM 4
**Greenwood–Sammon Table 2: additions AND deletions by decade, with N and standard errors**
- Additions, mean **total** abnormal return (day before announcement → day after effective), robust SEs in parentheses: All 4.11% (0.003); 1980–1989 **3.42%** (0.003); 1990–1999 **7.25%** (0.008); 2000–2009 **5.14%** (0.007); 2010–2020 **0.804%** (0.005, not significant). Difference (2010–2020) − (2000–2009) = −4.3pp*** (0.009). N = 700 / 196 / 137 / 212 / 155.
  - Announcement component (t−1→t+1): 3.36% / 4.80% / 4.04% / **1.01%***. Effective-date component: 3.44% / 3.52% / 1.33% / **0.26%** (ns).
- Deletions, mean total abnormal return: All −8.20%; 1980–1989 **−4.64%**; 1990–1999 **−16.1%**; 2000–2009 **−12.4%**; 2010–2020 **−0.62%** (0.011, ns). Difference = +11.8pp*** (0.026). N = 267 / 39 / 56 / 85 / 87.
- Source: Greenwood & Sammon, "The Disappearing Index Effect", author's working-paper version (revised June 2023), Table 2.
- Tier: [PEER-REVIEWED] (working-paper version of a JF article)
- Caliber notes: Read from pdftotext of the author-hosted PDF — numbers are the table's own. Numerator = individual event abnormal return regressed on a constant per decade; denominator = the added/deleted stock's own price. **Deletion decade cells rest on 39–87 events**, so the 1990s −16.1% has a wide interval. Announcement + effective components do NOT sum to total (the paper says the gap is typically >6 days, so not all days fall in the ±1-day windows). The Dec 2022 NBER version reports raw *total returns* instead of abnormal returns with N = 684/263 and slightly different cells (7.59% for the 1990s, 5.21% for the 2000s).
- URL: https://marcosammon.com/images/greenwood_sammon.pdf ; NBER version: https://www.nber.org/system/files/working_papers/w30748/w30748.pdf

### CLAIM 5
**The puzzle stated as a quantity: demand shock grew, price impact fell**
- Verbatim: "We estimate that funds tracking the S&P 500 in the form of mutual funds or ETFs have grown from essentially zero in the 1980s to approximately 7 percent of market capitalization in recent years."
- Verbatim: "although index trackers now buy about 7-8% upon index addition, total institutional ownership barely moves around index changes. We interpret this as professional active investors providing liquidity to passive buyers and sellers."
- Also: "There is no apparent relationship between net purchases and the index inclusion effect, for either additions or deletions" (Figure 3, event-by-event regression of inclusion return on mechanical buying).
- Source: Greenwood & Sammon (revised June 2023).
- Tier: [PEER-REVIEWED]
- Caliber notes: The "7%" numerator = AUM of identified S&P 500-tracking mutual funds and ETFs; denominator = total US stock market capitalisation. The authors flag that this is a LOWER bound and cite Chinco–Sammon volume-based estimates as "even higher". The "7–8% bought upon addition" numerator = shares purchased by trackers; denominator = the added firm's shares outstanding. This is the cleanest single anti-bubble datapoint available: the mechanical demand shock is ~2× its 1990s size while the price response fell to zero.
- URL: https://marcosammon.com/images/greenwood_sammon.pdf

### CLAIM 6
**Migrations: the mechanism that hollows out the average**
- Verbatim: "From the 1990s to the present day, migrations went from about 40% of additions to over 80% and this trend toward more migrations is mirrored among S&P 500 index deletions."
- By decade: "for direct additions, the index inclusion effect was 10.5% in the late 90s, 8.6% in the 2000s, and 5.3% in the 2010s… For migrations, the index inclusion effect was 6.4% in the late 1990s and 2.7% in the 2000s. By the 2010s, this effect became negative, at -1.8%."
- Deletions: "For direct deletions, the index removal effect was -11.9% in the late 1990s, -13.4% in the 2000s and -5.3% in the 2010s. For deletions which are also migrations, the index removal effect was -16 basis points in the late 1990s, -4.1% in the 2000s, and 62 basis points in the 2010s."
- Also verbatim, speculative: "it seems possible that one of the reasons for an increased percentage of index migrations is that the S&P 500 index committee has sought to minimize large price impact associated with rebalancing trades."
- Source: Greenwood & Sammon (revised June 2023), Section on explanation 3.
- Tier: [PEER-REVIEWED]
- Caliber notes: "Migration" = stock simultaneously enters S&P 500 and leaves S&P MidCap, so forced buying by 500-trackers is netted against forced selling by MidCap-trackers. The 5.3% figure for direct additions in the 2010s is explicitly stated by the authors to be **driven by Tesla**. This is the single most important caveat on "the index effect disappeared": on a direct-addition subsample the effect is still ~5% (Tesla-inflated) and the aggregate near-zero is partly an artifact of a compositional shift toward net-zero-demand events.
- URL: https://marcosammon.com/images/greenwood_sammon.pdf

### CLAIM 7
**The other four candidate explanations, with the authors' own verdicts**
- (1) Changing composition: "We quickly rule out that the effects we document are driven by changes in the characteristics of additions and deletions since the 1980s, although such shifts do account for some of the changes"; a Fama–French-style regression on volatility, volume and relative size "cannot fully account for changes".
- (2) Market-wide liquidity: "value-weighted average bid-ask spreads have fallen by a factor of about 10× between the early 1990s and the late 2010s"; but "These declines in trading costs, however, are not enough to fully explain the change in price impact, and moreover the timing of the decline in trading costs predates the disappearance of the index announcement effect."
- (4) Predictability / front-running: "We find mixed evidence to support this hypothesis. In recent years, a larger share of the total return leading up to the index change occurs before announcement… That said, which precise stocks get added are still difficult to predict."
- (5) Improved liquidity provision: "in the 1990s, in the month before and after the index change, 15% of total volume occurred on the effective date, while in the 2010s that number increased to almost 30%."
- Source: Greenwood & Sammon (Dec 2022 NBER version, Introduction).
- Tier: [PEER-REVIEWED]
- Caliber notes: There are **five** classes of explanation, not four (the brief's premise of "four candidate explanations" is wrong). The paper's own bottom line, verbatim: "In the 1980s, index changes were unanticipated, index funds were small, and there was mispricing in the market. As index funds grew larger, the mispricing deepened and turned into an opportunity. As a result, the market adjusted to take advantage of this opportunity… This worked to eliminate the anomaly on average, in spite of demand shocks that continued to grow in magnitude over the 2000s and 2010s." They frame it as McLean–Pontiff (2016) anomaly decay, i.e. arbitrage capital arriving — NOT as evidence that indexation is harmless in general.
- URL: https://www.nber.org/system/files/working_papers/w30748/w30748.pdf

### CLAIM 8
**Prior claim of precedence (avoid mis-crediting)**
- Verbatim: "Most closely related to our paper is Bennett, Stulz, and Wang (2022), who first noted the decline in the index inclusion effect, although their focus is on the real effects of index changes, and they study only additions to the S&P 500 between 1997-2017."
- Source: Greenwood & Sammon (Dec 2022 NBER version), Introduction.
- Tier: [PEER-REVIEWED]
- Caliber notes: The "disappearing index effect" finding is not original to Greenwood–Sammon; Bennett, Stulz & Wang documented the decline first on additions only, 1997–2017. Useful against the framing that a single 2022–2025 paper overturned the literature.
- URL: https://www.nber.org/system/files/working_papers/w30748/w30748.pdf

### CLAIM 9
**Comovement: the canonical pro-friction result (Barberis, Shleifer, Wurgler)**
- Verbatim: "While stocks added to the S&P during 1976–1987 experience an average increase in daily S&P beta of 0.067 after inclusion, the average increase in the 1988–2000 period is 0.214."
- Verbatim: "At the daily frequency, for example, S&P betas increase by 0.326 on average over the 1976–2000 period, while non-S&P betas fall by an average of 0.319." (bivariate specification)
- Verbatim (univariate, full sample): "In the full sample of additions, the mean increase in daily beta is 0.151".
- Source: Barberis, N., Shleifer, A., Wurgler, J., "Comovement", *Journal of Financial Economics* 75(2), 2005, pp. 283–317.
- Tier: [PEER-REVIEWED]
- Caliber notes: Sample = S&P 500 inclusions 22 Sept 1976 – 31 Dec 2000 and deletions 1 Jan 1979 – 31 Dec 2000; final sample **455 inclusions and 76 deletions** (daily/weekly); events after 31 Dec 1998 dropped for lack of post-event window. Pre/post estimation windows exclude the announcement and implementation months. Numerator = change in regression slope; denominator = none (beta is unitless). The authors' own framing is that the effect is "not only present but larger in more recent data" — i.e. as of 2005 the trend was UP with indexation, the exact opposite of the later index-effect trend.
- URL: https://pages.stern.nyu.edu/~jwurgler/papers/wurgler_barberis_shleifer.pdf

### CLAIM 10
**Comovement: the reversal / methodological demolition (Chen, Singal, Whitelaw)**
- Univariate difference-of-differences (Δβ_S&P500 − Δβ_nonS&P500) for S&P 500 additions, with t-stats and N:
  - 1976–1987: **+0.020** (t = 0.763), N = 197
  - 1988–2000: **+0.199** (t = 4.938), N = 269
  - 2001–2012: **−0.004** (t = −0.137), N = 214
  - 1976–2012: +0.083 (t = 4.080), N = 680
- Verbatim abstract: "We show that the bivariate regressions in this literature provide little information about the economic magnitude of excess comovement, with coefficients that are sensitive to unrelated factors. Using robust univariate regressions and matched control samples, almost all evidence of excess comovement disappears. In both examples, the stocks exhibit strong returns prior to the event, akin to momentum winners. We document that winner stocks exhibit increases in betas, generating much of the apparent excess comovement."
- Source: Chen, H., Singal, V., Whitelaw, R., "Comovement revisited", *Journal of Financial Economics* 121(3), 2016, pp. 624–644.
- Tier: [PEER-REVIEWED]
- Caliber notes: Pre-event window = one year ending the month before announcement; post-event = one year starting the month after the effective date. Dimson (1979) lead/lag correction applied; controls matched within size decile on trailing-12-month return. **This is the (b) answer: the comovement effect is statistically zero in 2001–2012, the decade when passive share grew fastest** — same directional result as the disappearing index effect, and it predates Greenwood–Sammon by six years.
- URL: https://pages.stern.nyu.edu/~rwhitela/papers/Comovement%20revisited%20JFE%202016.pdf

### CLAIM 11
**Central-bank replication that finds no permanent inclusion effect at all**
- Verbatim abstract: "We find that the firms included in the S&P 500 index are characterized by large increases in earnings, appreciation in market value, and positive price momentum in the period preceding their index inclusion. This strong preinclusion performance predicts 1) the permanent increase of market value and 2) the change in return comovement… Contrary to the consensus in the literature, our results indicate that – after accounting for the firms' extraordinary preinclusion performance – index inclusion has no permanent effect on value and comovement."
- Verbatim: "the results indicate the existence of temporary but no permanent value effect of S&P 500 index inclusion, consistent with the conclusions in Harris and Gurel (1986)."
- Source: Kasch, M. and Sarkar, A., "Is There an S&P 500 Index Effect?", Federal Reserve Bank of New York Staff Report No. 484, Feb 2011, revised Nov 2012.
- Tier: [OFFICIAL] (Fed staff report — but note: staff reports are explicitly not peer-reviewed and this one carries the standard disclaimer that views are the authors', not the FRBNY's)
- Caliber notes: Sample = additions Oct 1989 – Oct 2009; 562 additions in the raw window, **403 in the final sample** after excluding mergers/restructurings and requiring ≥60 daily returns in the ±15 months. Estimation windows [−12,−1] and [+4,+15] months relative to the announcement month. The authors explicitly decline to run BSW's bivariate spec, verbatim: "the correlation between S&P 500 and non-S&P 500 stock returns exceeds 93%. The concern regarding a multiple regression with highly correlated regressors is that its parameter estimates are likely to be regression artifacts."
- URL: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr484.pdf

### CLAIM 12
**BIS official pro-comovement estimate**
- Graph 3, "Inclusion in the S&P 500 increases correlation and improves liquidity": correlation of the stock's daily returns with the S&P 500 rises from **0.45** (t−200 to t−1) to **0.52** (t+1 to t+200). Trading volume rises (indexed 1.0 at t−200 to ~1.9 peak) and bid-ask spread falls from ~0.144% to ~0.096% of mid-price.
- Sample footnote, verbatim: "Sample based on 462 stocks joining the S&P 500 between January 2000 and September 2017. Stocks subject to mergers and acquisitions, stocks with poor data availability and those that have left the index during the first 30 days after the inclusion date are excluded."
- Also verbatim: "passive funds managed about $8 trillion or 20% of aggregate investment fund assets as of June 2017, up from 8% a decade earlier"; "ETFs' share of passive fund assets exceeded 40% in June 2017".
- Source: Sushko, V. and Turner, G., "The implications of passive investing for securities markets", *BIS Quarterly Review*, March 2018, pp. 113–131.
- Tier: [OFFICIAL] (BIS)
- Caliber notes: This is a **raw before/after comparison with no matched control and no control for pre-inclusion momentum** — precisely the design Chen–Singal–Whitelaw (CLAIM 10) and Kasch–Sarkar (CLAIM 11) show produces spurious comovement. Its sample window (2000–2017) overlaps CSW's null period. The passive-share figure has denominator = *global investment fund AUM*, not market capitalisation — not comparable to the "50% of US equity funds" figure the article's thesis turns on.
- URL: https://www.bis.org/publ/qtrpdf/r_qt1803j.pdf

### CLAIM 13
**BIS bottom line on passive and stability (the (e) answer, part 1)**
- Verbatim from the abstract: "A shift towards passive investing could affect securities markets in two key ways. First, it could result in higher correlation of returns and less security-specific price information. Second, it could affect aggregate investment fund flows and market price dynamics. In this context, active mutual funds exhibited persistent outflows in recent stress periods, whereas passive mutual fund flows were fairly stable. ETF flows were relatively volatile, although their link with underlying prices is less straightforward than for other fund types."
- Verbatim: "A key observation is that, despite their rapid growth, passive funds account for a relatively small fraction of outstanding securities."
- Verbatim on flows in stress: "passive mutual funds' flows were the least volatile, in both absolute and relative terms, compared with those of both ETFs and active mutual funds. On this basis, index mutual fund investors do not appear to 'rush for the exit' in times of stress." And: "active mutual funds exhibited the most persistent outflows across asset classes in all three episodes."
- Source: same BIS Quarterly Review March 2018 special feature.
- Tier: [OFFICIAL] (BIS)
- Caliber notes: The three stress episodes are named: "the 2013 taper tantrum (bond funds only); the 2015 bout of equity market turbulence (equity funds only); and the turbulence surrounding the 2016 US presidential election (bond funds and EME equity funds)." No 2020 or 2025 episode (paper predates them). BIS also flags the counterbalancing force verbatim: "At some point, greater anomalies in individual security prices would be expected to increase the gains from informed analysis and active trading, and thus spur more active investment strategies."
- URL: https://www.bis.org/publ/qtrpdf/r_qt1803j.pdf

### CLAIM 14
**ECB official estimate of the passive→comovement link (most recent official estimate)**
- Verbatim: "Between the first quarter of 2010 and the first quarter of 2024, a 1 percentage point increase in the passive ownership share of a euro area stock was associated with an increase of around 0.005 in the correlation coefficient with the EURO STOXX index."
- Verbatim footnote giving the base: "the average return correlation coefficient of a euro area stock with the EURO STOXX index between the first quarter of 2010 and the first quarter of 2024 is 0.50."
- Verbatim method note: "The estimate is based on a panel regression with stock and time fixed effects that regress correlation with the EURO STOXX index on the passive ownership share of constituent stocks, controlling for market capitalisation, liquidity, valuation and 1 autoregressive lag of the correlation coefficient… The results also hold in a two-step regression set-up, using index inclusion as an instrumental variable for passive ownership share."
- Verbatim conclusion: "These relationships could undermine the benefits of diversification for investors and reduce the ability of markets to absorb shocks, potentially leading to larger price volatility in the end."
- Also verbatim on liquidity clustering: "Passive funds avoid trading during a continuous trading session, preferring to trade at closing auctions… This is evidenced by a significantly larger share of closing auction volumes on index rebalancing days".
- Source: Dieckelmann, D., Siciliano, E., Sowiński, A., "Passive investing and its impact on return co-movement, market concentration and liquidity in euro area equity markets", box in ECB *Financial Stability Review*, November 2024.
- Tier: [OFFICIAL] (ECB)
- Caliber notes: All strings verified against the raw page HTML, not a summarizer. Population = EURO STOXX constituents (the index "captures 90% of euro area free-float market capitalisation"), NOT US. Economic size: a 10pp rise in a stock's passive ownership share maps to +0.05 on a base correlation of 0.50 — a ~10% relative increase. Uses index inclusion as the IV, which is exactly the instrument whose first stage (the price effect) has collapsed in the US per CLAIM 3–4. The box itself notes euro-area passive ownership "is still only half that of the United States".
- URL: https://www.ecb.europa.eu/press/financial-stability-publications/fsr/focus/2024/html/ecb.fsrbox202411_03~87408e7fb3.en.html

### CLAIM 15
**Federal Reserve staff survey: the scorecard, including its own "effects have declined" verdicts**
- Verbatim abstract: "We examine how this shift affects financial stability through its impacts on: (i) funds' liquidity and redemption risks, (ii) asset-market volatility, (iii) asset-management industry concentration, and (iv) comovement of asset returns and liquidity. Overall, the shift appears to be increasing some risks and reducing others. Some passive strategies amplify market volatility, and the shift has increased industry concentration, but it has diminished some liquidity and redemption risks. Finally, evidence is mixed on the links between indexing and comovement of asset returns and liquidity."
- Table 4, column "Evidence that active-to-passive shift has exacerbated?":
  - Valuation (inclusion effect): "For equities, valuation effects have declined significantly since 2000; for bonds, little research to date"
  - Comovement of returns: "For equities, comovement effects have declined significantly since 2001"
  - Comovement of liquidity: "Systematic liquidity associated with index investing has increased in recent years"
  - Liquidity: "Mixed: Liquidity declines for IG bonds and increases for HY bonds"
- Verbatim on the CSW evidence: "Chen, Singal, and Whitelaw (2016), who look more specifically at index-inclusion effects on return betas, do not find evidence of an upward trend in recent years. They report that adding a stock to the index had a smaller effect on its beta during the period from 2001 to 2012 than in the previous decade, even as indexing had become more common."
- Source: Anadu, K., Kruttli, M., McCabe, P., Osambela, E., "The Shift from Active to Passive Investing: Potential Risks to Financial Stability?", FEDS 2018-060r1, Board of Governors of the Federal Reserve System, 2018, revised 2020.
- Tier: [OFFICIAL] (Fed staff working paper; standard non-concurrence disclaimer)
- Caliber notes: This is the most balanced official scorecard available and it is **not** a passive-bubble endorsement: the two channels the bubble thesis needs (valuation effect, return comovement) are the two the Fed marks as declining. The channel it marks as worsening is *liquidity* commonality, which is a fragility argument, not a mispricing argument. Note their footnote that inclusion effects "may arise from activities other than passive (index) investing", specifically closet indexing.
- URL: https://www.federalreserve.gov/econres/feds/files/2018060r1pap.pdf (DOI 10.17016/FEDS.2018.060r1)

### CLAIM 16
**Tesla inclusion, academic calibers (the (c) answer, conservative measurement)**
- Verbatim: "Tesla was the largest ever firm added to the S&P 500 index, relative to the S&P 500's total market capitalization (over 2%). And, as mentioned above, in 2020 Tesla drove a positive overall average addition effect, experiencing a cumulative market-adjusted announcement return of 5.2% and implementation return of 4.5%."
- Verbatim: "Excluding Tesla, the average inclusion effect in 2020 was -3 basis points."
- Verbatim footnote caveat: "Another way that Tesla's addition was unusual is that there was a 32-day gap between the announcement of its addition and the implementation of the index change, while the typical gap is fewer than 10 days. So, the total cumulative market adjusted return to Tesla may also be high because other good news about Tesla was released between the announcement date and effective date."
- Table 1, 2020 row (12 additions): announcement 0.40%, effective 2.31%, total **5.49%**, post-event 0.64%.
- Source: Greenwood & Sammon (revised June 2023), Tables 1–2 and Section 2.1.
- Tier: [PEER-REVIEWED]
- Caliber notes: The 5.2% / 4.5% are ±1-day market-adjusted windows around announcement and effective date respectively. The 5.49% is the 12-addition 2020 average total return, essentially all of it Tesla. The authors themselves refuse to attribute the full run-up to index demand (32-day contaminated window). Population denominator for "over 2%" = S&P 500 total market cap.
- URL: https://marcosammon.com/images/greenwood_sammon.pdf

### CLAIM 17
**Tesla inclusion, practitioner calibers (the same event, 10× larger numbers)**
- Verbatim: "Index funds, ETFs, and other index strategies that track the S&P 500 needed to buy at least $78 billion of Tesla shares at the rebalance-date valuation. Closet indexers likely needed to buy a similar, if not larger, amount. From the announcement on November 17, 2020, of Tesla's addition to the index through the market close on December 18, 2020, one day before the rebalance date, TSLA soared 57%. Meanwhile, AIV tumbled 17%."
- Verbatim: "Over the 10 trading days prior to December 18 (excluding the December 18 value), the average dollar-volume traded was $33 billion. On December 18, the dollar-volume traded spiked to $154 billion, the equivalent of 23% of total Tesla shares outstanding."
- Reversal, verbatim footnote: "From December 18, 2020, to June 18, 2021, $100 invested in AIV grew to $160.20 and $100 invested in TSLA fell to $89.70. The relative return advantage is calculated as 160.20/89.70 = 78.6%."
- Cost claim, verbatim footnote: "TSLA entered the S&P 500 Index with a weight of 1.69% and AIV exited the index with an estimated weight of 0.012%. Over the period December 18, 2020, to June 18, 2021, the S&P 500 returned 13.16%. In contrast, a hypothetical portfolio that did not rebalance out of AIV and into TSLA would have earned 13.57% over the same period, outperforming the actual index by 41 bps."
- Source: Arnott, R., Kalesnik, V., Wu, L., "Revisiting Tesla's Addition to the S&P 500: What's the Cost, Before and After?", Research Affiliates, June 2021.
- Tier: [VENDOR] — **strong conflict of interest in the pro-bubble direction**: Research Affiliates' entire commercial franchise is non-cap-weighted ("fundamental") index construction, i.e. it is paid to demonstrate that cap-weighted indexing has hidden costs. The piece explicitly concludes: "These 'hidden' costs could be easily avoided with smarter index design".
- Caliber notes: The 41bp is NOT an index-effect estimate; it is a 6-month counterfactual-portfolio performance difference on ONE event pair, annualised nowhere and generalised freely. The 78.6% is a ratio of two terminal values (160.20/89.70), which is a peculiar definition of "relative return advantage" (arithmetic difference would be 70.5pp). Announcement date given as Nov 17 vs the S&P DJI release dated Nov 16 after the close. Their own valuation framing ("Tesla was more than 120 times more expensive than the traditional automakers" per car sold) is editorial, not an inclusion-effect measurement.
- URL: https://www.researchaffiliates.com/content/dam/ra/publications/pdf/832-revisiting-teslas-addition-to-the-sp500.pdf

### CLAIM 18
**24 August 2015: what actually happened to ETPs, per the SEC's own research note**
- "On August 24, 1,278 LULD halts were triggered in 471 securities." Breakdown: "there were 1,058 LULD halts in 327 ETPs (many halts were repeats in the same ETP), and 220 LULD halts in 144 non-ETPs."
- Verbatim, the counter-fact: "Although most of the 1,278 LULD trading halts on August 24 occurred in ETPs, 80% of ETPs did not experience a single LULD halt." And: "Most ETPs (859, 63.3% of total ETPs) experienced price declines of less than 10% -- a level that is generally consistent with the broad-market price declines on August 24 and therefore suggestive that they traded with little, if any, discount to the indices they were designed to track."
- Verbatim on the tail: "A minority of ETPs (19.2%), however, declined by 20% or more (compared to only 4.7% of Corporates)." For the 499 US Equity ETPs, "41.9% experienced an LULD halt and their mean percentage range for the day… was 19.2%."
- Verbatim idiosyncrasy: "SPY, for example, traded at a premium to its NAV until 9:37, while the next largest ETP – the iShares Core S&P 500 ('IVV') – traded at a substantial discount to the SPY, E-Mini, and SPY NAV until 9:43." And QQQ "traded at a substantial discount to its NAV until 9:37" despite all NASDAQ-100 constituents having opened at 9:30.
- Verbatim size-neutrality: "LULD trading pauses occurred in 20% of the 50 largest capitalization ETPs, and in 20% of the remaining 1,491 ETPs."
- Source: SEC Division of Trading and Markets, Office of Analytics and Research, "Research Note: Equity Market Volatility on August 24, 2015" (Dec 2015), 88 pp.
- Tier: [OFFICIAL] (SEC staff)
- Caliber notes: sec.gov returns 403 to default fetchers; retrieved with a declared User-Agent. Denominators: 1,541 ETPs in the halt analysis, 1,506 in the control-period table, 4,312 Corporates. The "hundreds of ETFs halted" popular claim is accurate on the numerator (327 ETPs) and misleading on the denominator (80% had zero halts, 63% tracked the market fine).
- URL: https://www.sec.gov/marketstructure/research/equity_market_volatility.pdf

### CLAIM 19
**24 August 2015: the SEC's causal diagnosis was market structure, not passive structure**
- Verbatim: "By 9:35, for example, the NYSE had opened 38% of its listed S&P 500 companies representing 53% of such companies' market capitalization. By 9:45, these figures increased to 86%… representing 91%."
- Verbatim: "The S&P 500 Index ('SPX'), as calculated and disseminated by S&P Dow Jones Indices LLP ('S&P DJI'), declined on August 24 by only 5.2% from its previous day's close. Until approximately 9:42, SPX remained substantially higher than the prices of the SPY (7.8% decline), E-Mini (7% decline), and the net asset value ('NAV') of SPY (8% decline…). S&P DJI generally uses last sale prices from only the primary listing market to calculate its equity indexes… The use of these previous day closing prices to calculate SPX in the opening minutes of August 24 likely caused its decline to be less than S&P 500 related products that reflected real-time trade prices."
- Verbatim: "Because the SPX did not decline by 7% (the first level trigger) on August 24, the market-wide circuit breakers… were not triggered on August 24."
- Verbatim on liquidity: "Quoted depth… was much lower in the opening minutes on August 24 than in control periods, particularly for Very Large Corporates (more than 70% reduction) and for ETPs (more than 90% reduction)."
- Verbatim on the best predictor: "A pre-August 24 metric with a particularly strong association with volatility is secondary market turnover rate – the ratio of average daily volume in the secondary market for an ETP to its shares outstanding. Large and Mid market capitalization US Equity ETPs with comparatively low secondary market turnover rates in a control period were much more likely to experience severe volatility".
- Source: same SEC research note.
- Tier: [OFFICIAL] (SEC staff)
- Caliber notes: This inverts the popular reading of 24 Aug 2015. The **index** (SPX, computed by the index provider from stale primary-market prints) was the mispriced object; SPY/E-mini/NAV were closer to real-time truth — and the stale index is why the market-wide circuit breaker failed to fire. The ETP dislocations track a *liquidity/turnover* characteristic of individual ETPs, not indexation. Note the S&P DJI conflict: the index provider's own calculation convention is implicated.
- URL: https://www.sec.gov/marketstructure/research/equity_market_volatility.pdf

### CLAIM 20
**6 May 2010 flash crash: ETFs disproportionately hit, but the mechanism was market-maker withdrawal**
- Verbatim: "during the 20 minute period between 2:40 p.m. and 3:00 p.m., over 20,000 trades (many based on retail-customer orders) across more than 300 separate securities, including many ETFs, were executed at prices 60% or more away from their 2:40 p.m. prices." Elsewhere quantified as "over 20,000 trades representing 5.5 million shares".
- Verbatim: "over two-thirds of the securities with broken trades were ETFs listed on NYSE Arca".
- Verbatim mechanism: "A large majority of ETF market makers with whom we spoke, and particularly those that value underlying stocks as part of their normal market making activities, paused their market making for considerable periods of time starting at about 2:45 p.m. on May 6. We believe this is one of the reasons equity-based ETFs were disproportionately affected by the extreme price volatilities of that afternoon. We further note that ETFs that do not derive their value from the prices of domestic equity securities were not disproportionately affected."
- Verbatim structural point: "they considered ETFs a 'professional's market,' where depth of book is more limited compared to individual stocks, and there are little, if any, resting retail orders far from the mid-quote."
- Source: CFTC/SEC Staff, "Findings Regarding the Market Events of May 6, 2010" (30 Sept 2010).
- Tier: [OFFICIAL] (joint SEC/CFTC staff)
- Caliber notes: The falsification test is inside the report: **non-domestic-equity ETFs were not disproportionately affected**, which rules out "ETF structure per se" and points at the specific dependency of equity-ETF market makers on underlying-stock price integrity. Numerator = securities with broken trades (>300); the two-thirds refers to *securities*, not share volume or dollar value. Separately, "Almost two-thirds of shares in cancelled trades were executed at prices of less than $1.00", i.e. stub-quote executions, so the 60%-away figure is largely a market-microstructure artifact.
- URL: https://www.cftc.gov/sites/default/files/idc/groups/public/@otherif/documents/ifdocs/staff-findings050610.pdf

### CLAIM 21
**5 February 2018 (XIV / "volmageddon"): BIS attributes it to leveraged/inverse vol ETPs AND explicitly declares them unrepresentative**
- Verbatim: "The assets of select leveraged and inverse volatility ETPs have expanded sharply over recent years, reaching about $4 billion at end-2017".
- Verbatim: "Even though the aggregate positions in these instruments are relatively small, systematic trading strategies of the issuers of leveraged and inverse volatility ETPs appear to have been a key factor behind the volatility spike that occurred on the afternoon of 5 February."
- Verbatim: "Transaction data show a spike in trading volume to 115,862 VIX futures contracts, or roughly one quarter of the entire market, and at highly inflated prices, within one minute at 16:08. The value of one of the inverse volatility ETPs, XIV, fell 84% and the product was subsequently terminated."
- Verbatim mechanism: "There were signs that other market participants began bidding up VIX futures prices at around 15:30 in anticipation of the end-of-day rebalancing by volatility ETPs… Due to the mechanical nature of the rebalancing, a higher VIX futures price necessitated even greater VIX futures purchases by the ETPs, creating a feedback loop."
- Verbatim scope limit (critical): "Neither the size nor the complex strategies of leveraged and inverse volatility ETPs are representative of the broader ETP market".
- Verbatim on XIV's termination trigger: "In the case of XIV, conditions of termination (called 'acceleration' in the prospectus) include a loss of 80% or more from previous daily indicative closing value."
- Source: BIS, "The equity market turbulence of 5 February – the role of exchange-traded volatility products", box in *BIS Quarterly Review*, March 2018.
- Tier: [OFFICIAL] (BIS)
- Caliber notes: All strings verified against raw page HTML. $4bn is the AUM of *select leveraged and inverse volatility* ETPs — roughly 0.1% of global ETP assets at the time. VIX futures market context, verbatim from the same feature: average daily volume rose "from 180,000 contracts daily average (2011) to 590,000 (2017)". This episode is routinely cited as "passive investing caused a crash"; the primary source says the culprits are daily-rebalancing leveraged derivatives products explicitly declared non-representative of ETPs, let alone of index funds.
- URL: https://www.bis.org/publ/qtrpdf/r_qt1803t.htm

### CLAIM 22
**March 2020 bond ETFs: BIS calibers on the dislocation and on baskets as a stabiliser**
- Verbatim: "bond ETFs have been growing steadily over the past few years and now manage more than $1.2 trillion of assets across the globe, compared with less than $10 billion in 2009."
- Verbatim: "Within days, steep discounts of share prices relative to NAV transformed into large premiums… In addition, the tracking error of bond ETFs increased to above 200 basis points for some funds in March–April 2020, much higher than the historical average of 0.7 bp in the sector. These facts indicated impediments to the functioning of the arbitrage mechanism for bond ETFs."
- Verbatim reinterpretation: "such a stabilisation mechanism was arguably in place during the March–April 2020 episode… when some ETFs traded at a discount while redeeming baskets that were more illiquid than the holdings."
- Verbatim on Treasuries: "The extraordinary dysfunction of the market for US Treasuries resulted in deep discounts for ETFs investing in these securities. These discounts subsided with the Federal Reserve's intervention on 23 March".
- Source: Shim, J.J. and Todorov, K., "The anatomy of bond ETF arbitrage", *BIS Quarterly Review*, March 2021.
- Tier: [OFFICIAL] (BIS)
- Caliber notes: "above 200 basis points" is a max-for-some-funds figure against a 0.7bp sector mean — a ~300× outlier ratio, so the two numbers should never be reported as a like-for-like comparison. BIS frames discounts as (partly) an *intentional* run-deterrent produced by basket selection, i.e. an argument that the ETF wrapper absorbed rather than transmitted the shock. Note the causality direction: the Treasury-ETF discounts were caused by Treasury market dysfunction, not the reverse.
- URL: https://www.bis.org/publ/qtrpdf/r_qt2103d.htm

### CLAIM 23
**Federal Reserve's own March-2020 read: the passive shift DAMPENS fire-sale risk**
- Verbatim: "One notable trend in the asset management industry over the past couple of decades is the shift from actively managed assets to passively managed mutual funds and ETFs. As investors in passive mutual funds tend to be less responsive to performance than those in active funds, this shift to passive investing might help reduce large redemptions arising from poor performance and, therefore, damp fire sale risks."
- Verbatim, the carve-out: "At the same time, some types of exchange-traded products (ETPs)—leveraged and inverse ETPs—have features that could cause strains in market liquidity… Because this pattern is well known by other market participants, there is the potential for 'front running,' or executing trades in anticipation of the rebalancing, leading to further liquidity strains."
- Verbatim March 2020 outflow calibers: "Both high-yield funds and bank loan funds experienced heightened outflows in March, reaching 4 percent and 14 percent of assets under management, respectively."
- Source: Board of Governors of the Federal Reserve System, *Financial Stability Report*, May 2020, Box "Vulnerabilities associated with the asset management industry" (p. 33 area).
- Tier: [OFFICIAL] (Fed, Board-level publication — higher standing than a staff working paper)
- Caliber notes: The 4% and 14% denominators are each fund category's own AUM; these are *active* categories (HY and bank-loan funds), so the largest March 2020 redemption pressures cited by the Fed came from actively managed vehicles. The Fed's structural verdict on passive is explicitly stabilising, with the destabilising label reserved for leveraged/inverse ETPs — the same carve-out BIS makes in CLAIM 21.
- URL: https://www.federalreserve.gov/publications/files/financial-stability-report-20200515.pdf

### CLAIM 24
**The "ETFs are price discovery" reinterpretation — and who authored it**
- Average absolute stated premium/discount to NAV, Jan–Feb 2020 vs Mar–Apr 2020: TLT 0.13% → 0.86%; **LQD 0.13% → 1.39%**; HYG 0.21% → 1.06%.
- Verbatim conclusions slide: "Bond ETFs serve as vehicles for efficient price discovery… Bond ETF prices showed large deviations from NAV. However, we believe these deviations were a function of price discovery coupled with NAV latency effects in a challenged liquidity environment." And: "We find no evidence supporting claims of 'wrong way' arbitrage."
- Verbatim test behind that last claim: "We regress bond ETF creation/redemption flows on the average intraday premium/discount to intrinsic value and add an interaction term for the crisis period. In no case are the coefficients negative. Accordingly, we find no evidence of wrong way arbitrage even in times of market stress." (Adj. R² reported as 0.455 / 0.336 / 0.158.)
- Verbatim on stale NAV: "Majority of bonds do not trade on a given day – NAV largely based on estimation. These dynamics are exacerbated during periods of volatility. The ETF price reflects an actionable trade on exchange."
- Source: "Pricing and Liquidity of Fixed Income ETFs in the Covid-19 Crisis of 2020", EII Global Research, as of July 2020; hosted on sec.gov for the SEC Fixed Income Market Structure Advisory Committee conference of 5 Oct 2020.
- Tier: [VENDOR] — **this is a BlackRock document** (internal doc ID ICRMH0920U-1319728; "Source: BlackRock" on every exhibit; "EII" = BlackRock's ETF and Index Investments group). Hosting on sec.gov does not make it an SEC finding. COI runs in the debunking direction: the world's largest ETF issuer is the party arguing that March-2020 bond ETF discounts were informative rather than a structural failure.
- Caliber notes: The comparison periods are two-month averages of *stated* (end-of-day) premium/discount, so the headline 1.39% understates intraday extremes reported elsewhere (>6–8% for some IG funds). The "no wrong-way arbitrage" test is a flow-on-premium regression with only a crisis interaction term — it tests sign, not magnitude, and it is the issuer's own specification on its own funds. Treat the *direction* of the price-discovery argument as corroborated by BIS (CLAIM 22) and by the SEC's independent Aug-2015 finding that the index, not the ETF, was stale (CLAIM 19); treat the *specific calibers* here as vendor-sourced.
- URL: https://www.sec.gov/spotlight/fixed-income-advisory-committee/100520-sec-conference-bond-etf-behavior-during-covid-volatility.pdf

### CLAIM 25
**April 2025 tariff drawdown: who bought the dip, per BIS (the (f) answer, official)**
- Verbatim: "in contrast with past episodes, retail investors, rather than institutional ones, bought into the rally."
- Verbatim: "Even as institutional investors withdrew from equity markets, retail investors were on net 'buyers of the dip', as visible from fund flows (Graph A2.C). These dynamics were somewhat unusual compared with past stress episodes (eg the GFC), when retail investors were net sellers and institutional investors were net buyers."
- Verbatim on the recovery's driver: "the market rebound through mid-May was mainly due to backtracking from the initial tariff shock… The protracted equity rally and compression in volatility from mid-May onwards were largely influenced by non-tariff-related news and developments."
- Source: BIS, "Understanding the swift market recovery after the April 2025 tariff shock", box in *BIS Quarterly Review*, September 2025.
- Tier: [OFFICIAL] (BIS) — published within the last 12 months
- Caliber notes: BIS says "retail", not "passive/index". The mapping retail→index-fund flows is an inference the pipeline must not smuggle in as BIS's finding, though it is the natural reading given retail's vehicle mix. No numbers are attached to the flow claim in the box text (the magnitude lives in Graph A2.C, which I could not read as text). This is the strongest official evidence for inelastic/stabilising passive-adjacent flows in the 2025–26 window, and it is directional-only.
- URL: https://www.bis.org/publ/qtrpdf/r_qt2509w.htm

### CLAIM 26
**Peer-reviewed pro-bubble mechanism with a stated magnitude (Jiang, Vayanos, Zheng)**
- Verbatim abstract: "We study how passive investing affects asset prices. Flows into passive funds disproportionately raise the stock prices of the economy's largest firms, and especially those large firms in high demand by noise traders. Because of this effect, the aggregate market can rise even when flows are entirely due to investors switching from active to passive funds… Consistent with our theory, prices and idiosyncratic volatilities of the largest S&P500 firms rise the most following flows into that index."
- Magnitudes: a one-standard-deviation rise in PassiveFlow(S&P500) is associated with higher quarterly excess returns of **+0.687% (top 10 firms), +0.528% (top 50), +0.303% (top 100), +0.208% (top 150), +0.145% (top 200)**; t-stats 2.46 / 3.66 / 3.02 / 2.28 / 1.64; N = 99 quarterly observations.
- Verbatim cumulative claim: "According to this estimate, the rise in passive investing over the past 25 years caused a firm that was in the top 50 of the S&P500 index during the entire period to rise by 29% more than the index."
- Source: Jiang, H., Vayanos, D., Zheng, L., "Passive Investing and the Rise of Mega-Firms", version dated 19 June 2025 (RFS-forthcoming manuscript; supersedes NBER WP 28253).
- Tier: [PEER-REVIEWED] (accepted/forthcoming; the June 2025 manuscript is the author-hosted version)
- Caliber notes: Sample = 1996Q2–2020Q4, 99 quarters; PassiveFlow mean 0.05% and SD 0.09% per quarter (denominator = index market cap). The 29% is arithmetic extrapolation: 0.528% × (0.05/0.09) × 99 = 29.04% — a linear, no-mean-reversion cumulation of a contemporaneous quarterly coefficient, and the authors themselves flag that "the 30% estimate concerns a contemporaneous effect of passive flows, which can partly mean-revert" and that it "is larger than in our calibration". Adjusted R² on the top-50 regressions is 0.049–0.210. This is the best-credentialed number for the bubble thesis in L5's territory, and it is a *relative* claim (top-50 vs index), not a claim about the index's absolute level.
- URL: https://personal.lse.ac.uk/vayanos/Papers/PIRMF_RFSf.pdf

### CLAIM 27
**Newest reconciliation: inclusion no longer moves price, but it does stiffen demand (2026 working paper)**
- Verbatim abstract: "Stocks with high passive ownership are 40% less elastic than low-passive stocks, and index additions are associated with discrete elasticity declines. In a partial-equilibrium counterfactual that freezes passive ownership at its 2000 level, estimated aggregate elasticity is 76% higher, with active investors partially offsetting the mechanical effect."
- Event study, Table 13: S&P 500 addition raises the Indexing Inclusion Ratio from 0.147 to 0.180, i.e. **+3.5pp (t = 28.64, N = 271 events, 2001–2023)**; stock-level price elasticity falls from **0.198 to 0.173, −2.4pp / −12% (t = −7.09, N = 153 events), with 75.2% of added stocks showing a decline.**
- Matched DiD: "Each S&P 500 addition is matched to a control stock from the same year with similar size (±0.5 log market equity) and the closest pre-event IXI. Across 138 matched" pairs.
- Source: Behmaram, P., "Indexing and the Elasticity of Stock Demand", working paper dated 1 April 2026, UQAM.
- Tier: NOT peer-reviewed — unpublished working paper by a single author. Closest available label: [PRACTITIONER]/preprint. Do not present as established.
- Caliber notes: Published within the last 4 months; directly relevant because it uses index addition as the identifying event and finds a *real, significant* inclusion effect on demand elasticity in 2001–2023 — the same period in which the price-level inclusion effect is zero. If it survives refereeing, it is the reconciliation the article needs: passive growth shows up in elasticity, not in event-day returns. Note the sample attrition 271→153 events for the elasticity panel, which the author addresses with a balance test (pre-event IXI p = 0.57, but dropped events are larger, p = 0.02). The paper's own framing figure: "the U.S. passive equity fund share rising from 3% in 1995 to over 55% in 2025" — denominator is US equity *fund* assets, not the market.
- URL: https://www.pouyabehmaram.com/papers/main_v16.pdf

---

### CROSS-CALIBER ISSUES

**1. "The Disappearing Index Effect" has three mutually inconsistent headline numbers across its own versions.**
- NBER WP 30748 (Dec 2022) abstract: additions fell "from an average of 3.4% in the 1980s and 7.6% in the 1990s to 0.8% over the past decade"; deletions "only -0.6% between 2010 and 2020".
- Author's revised version (June 2023) abstract: identical numbers but "0.8% over the **past two decades**" — almost certainly a typo, since its own Table 2 reports 5.14% for 2000–2009.
- Published JF 80(2) (April 2025) abstract: "from an average of **7.4%** in the 1990s to **less than 1%** over the past decade… an average return of **only 0.1%** between 2010 and 2020" for deletions.
- The 1990s additions figure moved 7.6% → 7.25% (abnormal-return table) → 7.4% (published abstract). The 2010–2020 deletions figure moved **−0.6% → +0.1%, a sign flip**. Wiley returns 403 so the published tables are unverified here. **Any article quoting "7.4%" and "−0.6%" together is mixing versions.** Safest citation: the published abstract's 7.4% / "less than 1%" / 0.1%, flagged as JF 2025.

**2. A web-search summarizer fabricated a Greenwood–Sammon number in this very session.** A WebSearch result summarising the Wiley abstract page reported "**0.3%** over the past decade" and "a similar decline… with only 0.3%"; the publisher-deposited abstract says "**less than 1%**". Do not use any GS caliber sourced from a search snippet.

**3. "The index effect disappeared" is an average of two offsetting halves.** In the 2010s, direct additions still earned **+5.3%** while migrations earned **−1.8%**, and migrations rose from ~40% to >80% of additions. Further, the 5.3% is Tesla-driven; excluding Tesla, 2020's average inclusion effect was **−3bp**. So there are at least three defensible statements — "the effect is zero", "the effect is ~5% for genuine additions", "the effect is negative once you drop one outlier" — all from the same table. Specify subsample every time.

**4. Total vs abnormal returns, and non-additive windows.** GS's Dec 2022 tables are raw total returns (N = 684 additions / 263 deletions); the revised tables are abnormal returns (N = 700 / 267). Announcement return is t−1→t+1 around announcement; effective return is t−1→t+1 around the effective date; total is day-before-announcement→day-after-effective. **Announcement + effective ≠ total** because the gap averages >6 days. Deletion decade cells rest on 39–87 events.

**5. Tesla: 5.2% and +57% are both correct and measure different things.** GS: +5.2% market-adjusted around the announcement, +4.5% around implementation, in a 32-day-gap event they explicitly warn is contaminated by non-index news. Research Affiliates: **+57%** raw from 17 Nov to the 18 Dec close. A third number, RA's **41bp**, is not an inclusion effect at all — it is a 6-month counterfactual index-portfolio return difference on one add/delete pair. And RA's headline "78.6%" is a ratio of terminal values (160.20/89.70), not an arithmetic return difference (which would be 70.5pp). Announcement date is given as 16 Nov (S&P DJI, after close) or 17 Nov (RA).

**6. Comovement: the famous number is the one the literature says is meaningless.** BSW's quotable "+0.326 S&P beta / −0.319 non-S&P beta" comes from the **bivariate** specification. Chen–Singal–Whitelaw's central methodological claim is that "the bivariate regressions in this literature provide little information about the economic magnitude of excess comovement", and the FRBNY staff report refuses to run the spec at all because the two regressors correlate >93%. The defensible univariate difference-of-differences is **+0.083 full sample, +0.199 in 1988–2000, and −0.004 (t = −0.14) in 2001–2012.** Popular retellings of "index inclusion raises beta" almost always quote 0.326.

**7. Two official bodies estimate the passive→comovement link with incompatible designs and get opposite-signed implications.** BIS 2018 (Graph 3): correlation 0.45 → 0.52, 462 stocks, 2000–2017 — raw before/after, no matched control, no pre-inclusion-momentum control, i.e. exactly the design CSW and Kasch–Sarkar show is confounded. ECB 2024: +0.005 per 1pp passive ownership, stock and time fixed effects plus an index-inclusion IV, Q1 2010–Q1 2024, euro area, base correlation 0.50. The ECB estimate is methodologically far stronger but (a) is euro-area, (b) instruments with index inclusion — whose first-stage price effect has collapsed in the US, and (c) implies only +0.05 correlation for a 10pp passive-share rise. The Fed's own 2018/2020 survey scores this channel as "**comovement effects have declined significantly since 2001**".

**8. "Passive share" denominators are not comparable across the official sources cited here.** BIS 2018: $8trn = **20% of global investment fund AUM** (June 2017). Greenwood–Sammon: ~**7% of US market capitalisation** in S&P-500-tracking funds/ETFs. Behmaram 2026: "**over 55%**" = US passive **equity fund** share, 2025. ECB: passive ownership share **of an individual stock**. A "passive crossed 50%" claim is only true on the narrowest of these denominators.

**9. No official post-mortem of any of the four fragility episodes attributes causation to index/passive structure.** 6 May 2010 → equity-ETF market makers pausing, with the falsification test in the report itself ("ETFs that do not derive their value from the prices of domestic equity securities were not disproportionately affected"). 24 Aug 2015 → NYSE manual opens, LULD bands, and a **stale index** (S&P DJI's primary-market-only calculation) that both mispriced SPX at −5.2% versus SPY at −7.8% and prevented the market-wide circuit breaker from firing; the best cross-sectional predictor of ETP damage was low secondary-market turnover, not indexation. 5 Feb 2018 → leveraged/inverse volatility ETPs, ~$4bn AUM, which BIS explicitly says are not "representative of the broader ETP market". March 2020 → bond-market illiquidity, with the Board-level Fed FSR saying the passive shift "might help reduce large redemptions… and therefore damp fire sale risks". **The popular fragility case depends on conflating ~$4bn of daily-rebalanced leveraged derivatives ETPs with multi-trillion-dollar index funds.** Note also that the same official sources do flag one genuinely worsening channel: liquidity commonality / closing-auction concentration (Fed Table 4; ECB 2024).

**10. Conflicts of interest, both directions, on the specific sources above.** Pro-bubble: Research Affiliates (CLAIM 17) sells non-cap-weighted indices and its conclusion is an ad for "smarter index design". Anti-bubble: the "bond ETFs are efficient price discovery / no wrong-way arbitrage" evidence set (CLAIM 24) is a **BlackRock** deck (doc ID ICRMH0920U-1319728) merely *hosted* on sec.gov — it must not be cited as an SEC finding. Third-party: **S&P DJI appears on both sides** — its index-calculation convention is implicated in the Aug 2015 circuit-breaker failure, GS speculate its committee may deliberately favour MidCap migrations "to minimize large price impact", and it is the publisher of SPIVA.

**11. Coverage gaps I could not close (do not let another line paper over these).**
- **IMF and IOSCO primary documents are unreachable**: imf.org returns 403 to both curl and WebFetch (GFSR April 2026 ch2, Oct 2025 text, and the GFSR landing page), and iosco.org 403s on IOSCOPD682. I therefore assert **no IMF, FSB or IOSCO claim**. Search summaries attributed to GFSR Oct 2022 ("increased herding and concentration… made market liquidity more vulnerable") and GFSR April 2026 ("passive mutual funds and ETFs show the greatest sensitivity within the investment fund sector to shifts in global risk") are **[UNCONFIRMED WORDING]** and must be re-fetched from an authenticated or browser path before use. Requested URLs: https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch2.pdf and https://www.iosco.org/library/pubdocs/pdf/IOSCOPD682.pdf
- **April 2025 flow calibers are unverified.** Morningstar's page 403s; ici.org 403s. Search-summary figures — active **−$82bn** vs passive **+$36bn** in April 2025; ~**$18bn** into US ETFs 3–7 April; "59 Morningstar Categories enduring outflows and just 40 gathering inflows"; Morningstar Global Markets Index **−11%** 3–8 April — are all **[UNCONFIRMED WORDING, VENDOR/MEDIA]**. Only the BIS Sept 2025 box (CLAIM 25) is safely citable, and it says "retail", not "passive".
- **A possible 2025 index-effect revival is unverified and worth a dedicated check.** Reports that Coinbase jumped ~**24% on its 12 May 2025 announcement** (effective 19 May) and Robinhood ~**7% after hours** (added 22 Sept 2025) come only from blogs/media. If the 24% figure holds against CRSP/exchange data, it is a single-event inclusion effect roughly 3× the 1990s decade average, in the decade the literature calls "zero" — the strongest available challenge to a naive reading of Greenwood–Sammon, whose sample **ends in 2020**. Nothing in the peer-reviewed record covers 2021–2026 index effects.
- **Greenwood–Sammon's other-index-families result** (published abstract: "We document a similar decline in the index effect among other families of indices") is asserted in the abstract but its Russell/MSCI calibers live in the published tables I could not read.