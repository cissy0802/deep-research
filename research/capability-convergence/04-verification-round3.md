# Round 3 · 单源承重实证双席审计

## R1-eci-gap-widening · counter → **降级为弱结论**

**可用表述**:在 Epoch ECI 同一次拟合里,开源与闭源前沿的分差从 2025 年多数时点的约 3–7 点(年中约 5–6),在 2025 年底升到约 9 点,并在整个 2026 年停在约 10 点(2026-10:Claude Opus 5.5 167.3 对 Kimi K3 157.5,bootstrap 90% 区间约 8–14)。追平时滞约 4–7 个月,比 2025 年持平或略长。也就是说,在跨基准合成量尺上,2026 年差距没有收窄。Arena 偏好榜同期大致持平,美国 CAISI 用含非公开基准的评测判 DeepSeek V4 约落后 8 个月,都不支持"已追平"。但"扩大约一倍"取决于拿 2025 年哪个时点作基准;Epoch 各版本重拟合本身就会让同一对模型的分差漂移约 3 点;Artificial Analysis 的指数显示 2025-04 到 2026-04 曾经收窄(13→6),到 2026 年秋才又拉开到约 12(且跨了指数版本)。所以只能说"没有收窄、近一年稳定在较高水平",不宜说"翻倍"。"差距只剩几个百分点"的印象主要来自饱和考卷和偏好榜。

**理由**:一、复算(benchmark_data.zip 用 python zipfile 解压,系统 unzip 报 CRC 错;eci_scores.csv 共 274 个模型;eci_bootstraps.json 有 500 个样本,capability_samples 已是 ECI 量尺)。
点估计能复现:2026-10 Opus 5.5 167.33 对 Kimi K3 157.45,差 9.88。
按"每个 bootstrap 样本各取闭源最大、开源最大"算前沿分差(中位数,90% CI):
- 2025-01:3.0(1.7–4.4)
- 2025-04:7.3(5.0–9.7)
- 2025-06:6.5(4.6–9.1)
- 2025-09:5.2(3.0–7.2)
- 2025-12:8.9(7.0–11.8)
- 2026-03:10.9(9.0–14.3)
- 2026-06:10.7(8.4–13.9)
- 2026-10-12:10.3(7.9–13.6)
结论:分差在一次拟合之内确实变大了。2025-09 与 2026 的 CI 不重叠,所以"差距没有收窄"在 ECI 里站得住。但"约一倍"要看取哪个时点:2025 年内本身就在 3–9 之间来回;2025-04 已是 7.3,2025-12 已是 8.9。抬升主要发生在 2025 年第四季度,2026 年全年停在约 10 点上下。说成"2026 相对 2025 翻倍",基本是拿 2025 年中做基准。

二、稳健性:
1)剔除 Pro、高算力变体:2025-12 降到 7.0,2026-03 降到 9.4,2026-10 不变(10.25)。方向不变。
2)闭源一侧是否计入中国模型:结果不变,前沿全是美国实验室。开源只算中国模型:结果也不变,开源前沿本来就全是中国模型。
3)Google 最新 Pro 级未打分(Gemini 3.1 Pro 之后只有 Flash 系列):只可能让闭源前沿更高、差距更大,不会翻转方向。
4)Epoch 开源覆盖不全:Artificial Analysis v4.3 的开源第一名 MiMo-V2.6-Pro 不在 ECI 里(AA 上 46 对 K3 的 44),可能让分差略缩,但幅度应在 1–2 点量级,属推测。
5)追平月数(当前开源最强达到的水平,闭源最早何时达到):2025 年各节点 1.1–7.5 个月,2026 年 4.4–6.9 个月。大致持平或略增,与 Epoch 官方的 3→4 个月同向。

三、重拟合漂移:Epoch 5 月 Data Insight 表里,GPT-5.5 Pro 是 159.35、Kimi K2.6 是 151.60;10 月版里分别是 162.07 和 151.05。同一对模型,仅因重拟合分差就漂了约 +3.2 点,和文章所说的"扩大"同一量级。所以跨版本比较(5 月发布的 8 点对 10 月复算的 9.8 点)不能当作变大的证据。只有同一次拟合里比较才有效;同版本内上述趋势仍然成立。bootstrap 不覆盖"选哪些基准"带来的不确定性。

四、ECI 是否偏向闭源:ECI 大量用私有或保留集(FrontierMath 私有、ARC-AGI、ProofBench 等)。Epoch 与 WhatLLM 都指出,开源模型常针对公开基准刷分,公开考卷会让开源显得更近。CAISI 用含非公开基准的评测,判 DeepSeek V4 落后约 8 个月,比 ECI 显示的更远。所以 ECI 不太可能是"偏向闭源而人为拉大差距"的来源。覆盖度上并不对称:Opus 5.5 只有 17 个基准,K3 有 21 个,这不利于闭源一侧。没有做去掉某类基准后重拟合的测试。

五、独立来源:
- Artificial Analysis 官方 2026-04-30 文:差距约 13 点(2025-04)缩到 6 点(2026-04),上半段是收窄,与文章相反。v4.3 下到 2026-09/10,Opus 5.5 58 对 MiMo 46,差 12;同版本更早一期是 7。下半段又在变大,但这主要由 Opus 5.5 一次发布带动,还夹着版本切换(K3 在 v4.1 是 57,在 v4.3 是 44)。
- Arena(用 lmarena HF 数据自算,风格控制总榜,每月取最后一期):2025-03 到 12 月在 29–62 Elo,2026 年在 19–49,2026-10 为 37。无扩大趋势,平且噪声大。媒体"0→29 Elo"的起点是 2025 年 1 月 DeepSeek-R1 那一个月,属挑点。
- CAISI 对 DeepSeek V4:约落后 8 个月。只有一个时点,不给趋势,但支持"没追平"。
- Epoch 官方 3→4 个月:同一机构同一数据,不算独立来源。
总结:"没有收窄"有多源同向支撑(Epoch,AA 的 2026 下半年,Arena 平,CAISI 的水平证据);"2026 年分差扩大约一倍"只有 ECI 单源,而且对基准时点敏感,AA 的 2025→2026 上半段还给出了反向证据。

**method_issues**:
- 分差是不是"翻倍",几乎完全取决于 2025 年基准点:2025-01 为 3.0,04 为 7.3,09 为 5.2,12 为 8.9。抬升集中在 2025 年第四季度,2026 年全年平台在约 10。
- 跨版本比较无效:同一对模型因 ECI 重拟合漂移约 3 点,和所称扩大幅度同量级。只能在单一版本内比较。
- bootstrap CI 只反映这次拟合的抽样不确定性,不反映选哪些基准、锚点(Claude 3.5 Sonnet=130,GPT-5=150)和重拟合带来的不确定性。
- 前沿用 max 统计量,容易被单次发布(如 Opus 5.5、GPT-5.x Pro)带动,呈阶梯状。剔除 Pro 变体会让 2025-12、2026-03 的分差小 1.5–2 点,但 2026-10 不变。
- 覆盖度不对称:Google 新 Pro 级未打分(会让分差变大);MiMo-V2.6-Pro 等开源模型未纳入(可能缩小 1–2 点);Opus 5.5 只有 17 个基准,K3 有 21 个。
- ECI 偏重私有或保留集,如果有偏,更可能是让开源少吃"刷公开榜"的红利,而不是人为偏向闭源。没做去掉某类基准后的重拟合测试。
- "Accessibility group" 有一类 Other(例如托管版 Qwen),我按非开源处理,对前沿结果无影响。
- Artificial Analysis 跨版本(v4.1→v4.3)重标度幅度很大,不能把版本间的点差直接拿来比趋势。

**independent_measurements**:
- Epoch ECI 自算(epoch.ai/data/benchmark_data.zip,2026-10 版):前沿分差 2025-09 为 5.2 [3.0–7.2],2025-12 为 8.9,2026-03 为 10.9,2026-10 为 10.3 [7.9–13.6]。同向,但 2025 年内波动 3–9。
- Epoch Data Insight(https://epoch.ai/data-insights/open-closed-eci-gap,2026-05-29):2026 年以来平均落后 4 个月、8 ECI 点;2025-10 版为 3 个月。同向(略扩大),但同源、不独立。
- Epoch 5 月版对 10 月版:GPT-5.5 Pro 159.35→162.07,Kimi K2.6 151.60→151.05,单对分差因重拟合漂移约 +3.2 点。这是方法学警示。
- Artificial Analysis 官方(https://www.artificialanalysis.ai/articles/recent-open-weights-model-launches,2026-04-30):约 13 点(2025-04,DeepSeek V3 0324 22 对 Claude 3.7 Sonnet 35)→6 点(GPT-5.5 60 对 Kimi K2.6、MiMo V2.5 Pro 54)。反向:2025→2026 上半年在收窄。
- Artificial Analysis v4.3(https://artificialanalysis.ai/models/open-source 与 https://rits.shanghai.nyu.edu/ai/claude-opus-5-5-takes-the-top-spot-on-artificial-analysis-at-58/,2026-09/10):Opus 5.5 58 对 MiMo-V2.6-Pro 46,差 12,更早为 7。同向(2026 下半年扩大),但 K3 在 v4.1 为 57、在 v4.3 为 44,版本切换是混杂因素。
- WhatLLM(https://whatllm.org/blog/open-source-vs-proprietary-llms-2026,2026-07,AA 数据):智能指数差 11.3,但 Coding 差 5.4、Agentic 差 4.3、GPQA 差 2。因子指数不同,差距从小到大不等。
- Arena 自算(HF lmarena-ai/leaderboard-dataset text,风格控制总榜,每月取末期):2025-04 至 12 月为 57/53/54/43/35/32/29/62/51 Elo,2026-01 至 10 月为 38/48/49/34/28/35/22/19/37/37。不同向:无扩大趋势,平且噪声大。
- 媒体引 Arena(https://cryptobriefing.com/arena-ai-frontier-open-weight-model-gap-widens/):2025-01 为 0,2026-09 为 29 Elo,称在扩大。起点挑在 R1 那个月,复算不支持趋势。
- CAISI/NIST(https://nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro,2026-05):用含非公开基准评测,DeepSeek V4 Pro 相当于 GPT-5,约落后 8 个月。支持没追平,无趋势。
- UK AISI 与 CAISI 对 Kimi K3 的网络安全评测(https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities):exploit 32.2% 对美国前沿 76.2%。只测网络安全、条件不对等,只作旁证。

**search_angles**:
- Epoch 原始数据复算:点估计分差、bootstrap 前沿分差时间序列、剔除 Pro 变体、按国别、只看中国开源、追平月数
- Epoch 5 月 Data Insight 表与 10 月 CSV 对同一模型对比(查重拟合漂移)
- Artificial Analysis 官方开源模型发布文(2026-04)、v4.3 开源页、模型排行榜
- Artificial Analysis 二手报道(rits.shanghai.nyu、pasqualepillitteri 两个页面都抓取失败 socket hang up,只读到搜索摘要,59.7 对 65.7 的说法无法核实)
- Arena:媒体"0→29 Elo"报道,以及用 HF 数据集每月复算风格控制榜和原始总榜
- CAISI/NIST 对 DeepSeek V4 Pro 的评测;UK AISI 与 CAISI 对 Kimi K3 的网络安全评测
- LiveBench:没找到一手的整体榜分差,只有聚合站的分项排名,无法使用
- Scale SEAL 开源对闭源分析:没搜到
- Ihle 开源闭源差距分析:没搜到
- Mozilla State of Open Source AI 2026(二手摘要称 2026-03 Arena 差 3.3 点,没核一手)
- The Decoder 报道开源模型达到 4 个月前的网络安全前沿水平(只看标题,与约 4 个月时滞一致,没深读)
- WhatLLM 用 AA 数据的分项指数差距

## R1-eci-gap-widening · method → **降级为弱结论**

**可用表述**:On Epoch's cross-benchmark composite ECI, the gap between open and closed models did not narrow in 2026. Averaged by time, the gap between the best closed and best open model went from about 6 points in 2025 to about 9 points in 2026 (Oct 2026 version). On the June-version fit the increase is smaller, at about 1.3–1.5x, and the gap swings sharply each time a major open model ships: it fell back to the 2025 level of about 5 points right after Kimi K3. In months, open models still trail by about 4–8 months, with no clear trend. The widening in points mainly reflects the closed frontier speeding up, not open models slowing down. This is a finding from a single composite scale. Its hardest benchmarks are mostly run on closed models, and other composite indices disagree: Artificial Analysis reports the gap narrowing to about 4–6 points. So the safest version is "the gap has not closed by the hardest measures", not "the gap doubled".

**理由**:I downloaded epoch.ai/data/benchmark_data.zip (Oct 2026, 274 models) and recomputed. I also pulled the Wayback snapshot of the same zip from 2026-06-10 to check refit drift directly. Findings:

(1) The R1 numbers reproduce. Running-max closed minus open on 2026-10-12 is 167.33 - 157.45 = 9.88. Annual gains reproduce too: closed +14.46 then +17.05, open +16.00 then +12.45.

(2) The gap is a sawtooth, so a snapshot comparison is unreliable. Month-end gaps: 2025-10 = 5.28; 2026-04/05 = 11.02; 2026-07/08 = 5.33 (right after Kimi K3), which is the same level as 2025; 2026-09/10 = 9.88. The "9–11" figure is partly an artifact of measuring 2.5 months after the last open-frontier jump. Daily time-averaged gaps are more robust: calendar 2025 = 5.78 (range 2.9–9.6), 2026 YTD = 9.09 (range 4.6–11.0), a factor of about 1.57. That is a widening, but not "about double".

(3) The within-fit bootstrap (eci_bootstraps.json, 500 samples, rescaled to the 130/150 anchors; this reproduces the official medians and CIs) gives an increase in time-averaged gap of +3.45 points, 90% interval [1.9, 5.3], P(>0) = 1.0. The snapshot difference (2026-10 vs 2025-10) is +4.4 [0.8, 7.9]. This only covers benchmark-sampling noise within one fit, not refit drift or coverage bias.

(4) Refit drift is real and concentrated at the closed top end. For the same models, the June fit gives GPT-5.5 Pro 159.35; the Oct fit gives 162.07 (+2.7). Kimi K2.6 went 151.60 to 151.05. So the 2026-05 gap was 7.74 in the June fit and 11.02 in the Oct fit, and the 2026-03 gap was 9.5 vs 10.9. 2025 points barely move: 2025-10 is 5.02 vs 5.28, 2025-06 is 5.93 vs 6.13. Mean per-model drift is only -0.4 (closed) and -0.3 (open), but top-end models scored on few benchmarks (GPT-5.5 Pro has only 10) get pulled up as new hard benchmarks are added. About 1.5–3.3 points of the 2026 gap therefore depends on the fit version. On the June fit, 2026 H1 still sits at about 7.7–9.5 against about 5–6 in 2025, so the direction survives but the size shrinks to about 1.3–1.6x. That matches Epoch's own May figure (about 8 points / about 4 months, vs about 3 months in Oct 2025). Also, every top model is extrapolated more than 10 points above the GPT-5 = 150 anchor, so whether points are equally spaced at the top is unverified.

(5) In months, the lag is roughly flat, and the latest point is short. Lag of each new open-frontier record behind the first closed model to reach that level: 2025 values were 1.1, 4.3, 5.3, 3.8, 5.5, 6.7, 7.5. 2026 values were 5.7, 8.0, 5.0, 6.9, then 4.4 for Kimi K3 (shortest of 2026). Excluding Chinese closed models (Qwen Max, GLM-5.3) gives identical results, because the closed frontier is always a US model. A wider point gap with a flat month lag is mostly a mechanical result of the closed frontier speeding up (+17/yr): gap in points ≈ lag × slope. That means "not narrowing" holds in months, but "widened" is a unit-of-measure claim, not a structural fact.

(6) Coverage and selection bias. For models released in 2026, the median number of benchmarks is 15 for closed and 10 for open. Coverage is lopsided: FrontierMath T4 v2 81% closed vs 36% open, ARC-AGI 60/32, Furniture Assembly 52/7, SimpleQA Verified 81/43. Frontier pairs are reasonably matched (K3 has 21 benchmarks, Opus 5.5 has 17), but on their 15 shared benchmarks the gap is driven by Furniture Assembly (+0.70), FrontierMath T4 (+0.56), Mystery Game Puzzles (+0.50) and FrontierSWE (+0.37). These are Epoch in-house or partner benchmarks, and FrontierMath was funded by OpenAI, which has access to most of the problems. Meanwhile GPQA (-0.03) and AIME (+0.03) are saturated and close to tied. The scale really is weighted toward hard tasks that closed labs run and that are more aligned with them. That is both its value (less contamination) and a potential bias. I did not refit IRT with benchmarks left out, so the size of this effect is unquantified. Unscored Google Pro-tier models would only push the closed frontier up, making the gap bias conservative. Missing open models (e.g., no DeepSeek V4.1 Pro) would bias the gap upward. These two risks point in opposite directions.

(7) Independent indices are mixed. Epoch's official figure (Data Insight, 2026-05-29) is a 4-month lag, slightly up from 3 months in 2025, so same direction but small. CAISI/NIST put DeepSeek V4 Pro about 8 months behind (Apr 2026). That is a lag level, not a trend, and its method is also IRT with private benchmarks, so it is not fully independent. Arena reportedly widened from 0 to 29 Elo (secondhand, unverified), same direction. Artificial Analysis Intelligence Index, per secondhand reports, narrowed from 13 points a year ago to 6 points in Sep 2026 (Fable 5.1 65.7 vs K3 59.7), and AA's own July statement put it at 4 points. That is the opposite direction. LiveBench, Ihle and Scale: nothing found. The article attributes the "gap is only a few points" impression to "saturated exams and preference leaderboards", but by these reports the preference leaderboard (Arena) actually shows widening, and the narrowing impression comes mainly from AA's composite index. That attribution has to be corrected.

Conclusion: "On ECI, the gap did not narrow in 2026" survives all the sensitivity checks (time-averaging, bootstrap, June fit, excluding Chinese closed models), so it can carry weight with caveats. "Roughly doubled" depends on the snapshot date (2026-08 equals 2025) and on the fit version (about 1.5–3 points of drift), so it cannot carry weight. Across indices the direction is contested (AA says narrowing). Verdict: downgrade to a weak conclusion. Not vetoed.

**method_issues**:
- Snapshot sensitivity: the ECI gap is a sawtooth. It was 5.33 in 2026-07/08 (same as 2025-10's 5.28), 11.02 in 2026-04/05 and 9.88 in 2026-10. '9–11 points' is cherry-picked timing 2.5 months after the last open-frontier jump. The time-averaged figure (5.78 → 9.09, about 1.57x) should be used instead.
- Refit drift is concentrated at the closed top end: GPT-5.5 Pro moved from 159.35 in the 2026-06 Wayback-snapshot fit to 162.07 in the Oct fit. That puts the 2026-05 gap at 7.74 vs 11.02, while 2025 points barely move (5.02 vs 5.28). About 1.5–3.3 points of the 2026 gap depends on the fit version.
- Scale extrapolation: anchors are Claude 3.5 Sonnet = 130 and GPT-5 = 150, and all 2026 frontier models sit 7–17 points above the top anchor. Whether points are equally spaced at the top is unverified, so 'doubled in points' is not necessarily a doubling in capability.
- Unit-of-measure confound: gap in points ≈ month lag × closed-frontier slope. The month lag is roughly flat (2025: 1.1–7.5 months; 2026: 5.7, 8.0, 5.0, 6.9, 4.4, with Kimi K3 at 4.4 the shortest of 2026). The point widening mostly comes from the closed side's slope rising from +14.5 to +17.1.
- Benchmark coverage is asymmetric: for 2026 models the median benchmark count is 15 closed vs 10 open. Coverage of FrontierMath T4 is 81% vs 36%, ARC-AGI 60% vs 32%, Furniture Assembly 52% vs 7%. The frontier pair (K3 with 21, Opus 5.5 with 17) is reasonably matched, but GPT-5.5 Pro has only 10 benchmarks, so it has wide CIs and drifts easily.
- The gap is driven by a few hard benchmarks: on the 15 shared with Opus 5.5 vs K3, Furniture Assembly is +0.70, FrontierMath T4 +0.56, Mystery Game Puzzles +0.50, FrontierSWE +0.37, while GPQA (-0.03) and AIME (+0.03) are close to tied. These benchmarks are Epoch in-house or partner tests. FrontierMath was funded by OpenAI, which has access to most of the problems, a potential conflict of interest and closed-side bias. I did not refit IRT with benchmarks left out, so the size of this effect is unquantified.
- Coverage-bias directions conflict: unscored Google Pro-tier models would only push the closed frontier up (biasing the gap estimate down). Possibly missing open models, e.g. no DeepSeek V4.1 Pro score, would bias it up. The two cancel to an unknown degree.
- Excluding Chinese closed models (Qwen 3.8 Max, GLM-5.3) does not change the results at all, because the closed frontier is always a US model. Moving them into the 'open' group is not a valid definition. Changing the open/closed definition has no effect on the direction.
- The bootstrap only covers within-fit noise: increase in time-averaged gap +3.45 [1.9, 5.3] at 90%, P > 0 = 1.0; snapshot difference +4.4 [0.8, 7.9], P > 0 = 0.986. It does not cover refit drift or benchmark-selection uncertainty.
- The article's causal attribution is wrong: it blames the 'gap is only a few points' impression on saturated exams and preference leaderboards, but Arena reportedly shows widening (0 → 29 Elo). The narrowing impression mainly comes from Artificial Analysis's composite index (13 → 6 points, secondhand).

**independent_measurements**:
- Epoch Data Insight https://epoch.ai/data-insights/open-closed-eci-gap (2026-05-29): open models trailed by an average of 4 months in 2026, vs about 3 months in Oct 2025, and an average of about 8 ECI points. Same direction, but a small change (same data source, not independent).
- My recomputation on the Wayback 2026-06-10 snapshot of epoch.ai/data/benchmark_data.zip (June fit): 2025-10 gap 5.02, 2025-12 7.72, 2026-03 9.50, 2026-05 7.74. Same direction, but about 1.5–3 points smaller than the Oct fit.
- CAISI/NIST https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro : DeepSeek V4 Pro about 8 months behind the frontier, roughly at GPT-5 level (Apr 2026). This is a lag level, not a trend, so it cannot test 'widening'. The method is also IRT with private benchmarks, so it is not fully independent.
- UK AISI + CAISI Kimi K3 cyber assessment https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities : ExploitBench 32.2% vs 76.2% for top US models. Cyber only, and preliminary.
- Artificial Analysis Intelligence Index (secondhand, https://pasqualepillitteri.it/en/news/14684/open-source-gap-artificial-analysis , https://latent.space/p/ainews-much-ado-about-open-weights , AA 2026-04 https://www.artificialanalysis.ai/articles/recent-open-weights-model-launches): about 6 points in Apr 2026; about 4 points after K3 in Jul; about 6 points in Sep (65.7 vs 59.7), vs 13 points a year earlier. Opposite direction (narrowing). Index versions are not comparable.
- Arena (secondhand, https://cryptobriefing.com/arena-ai-frontier-open-weight-model-gap-widens/): frontier vs open gap went from 0 in Jan 2025 to 29 Elo in Sep 2026. Same direction (widening), unverified against Arena itself.
- LiveBench / Ihle / Scale: no 2026 open-vs-closed trend analysis found.

**search_angles**:
- Recompute the frontier gap at monthly snapshots plus daily time-averages from Epoch eci_scores.csv (Oct 2026 version)
- Bootstrap from eci_bootstraps.json (500 samples, rescaled to anchors) for the uncertainty of the gap and its yearly difference
- Wayback 2026-06-10 snapshot of benchmark_data.zip: compare same-model ECI under the June vs Oct fits (refit drift)
- Catch-up lag of each open-frontier record behind the first closed model to reach that level, with and without Chinese closed models
- Benchmark coverage of open vs closed models (processed_data_for_eci.csv) and benchmark-level contributions for frontier pairs
- Change in open/closed definition (Other group / Chinese closed models): no effect on direction
- Artificial Analysis open vs proprietary gap 2026 (found only secondhand reports, opposite direction)
- CAISI DeepSeek V4 Pro / Kimi K3 evaluations (lag level, cyber-only)
- Epoch Data Insight open-closed-eci-gap (official 4 months / 8 points)
- Arena open-weight gap (secondhand 29 Elo)
- LiveBench / Ihle / Scale open-vs-closed trend in 2026 (nothing found)
- Leave-one-benchmark-out IRT refit (not done: needs Epoch's fitting code, so the size of benchmark-selection bias is unquantified)

## R2-metr-open-lag · counter → **方向存争**

**可用表述**:按 METR TH1.0 原始数据复算,2025 年开源模型追平闭源前沿的滞后有拉长迹象:2024 年底到 2025 年初的 DeepSeek V3/R1 约 3–6 个月,2025 年 11 月的 Kimi K2 Thinking 约 8 个月(按任务重抽样,90% 区间约 7–11 个月)。DeepSeek-R1 的 3.4 个月是个偏低的点;改以 V3 为起点,增幅只有约 2–3 个月;年中以后的变化落在误差范围内。这些数字来自单一评测方,每个模型的调优投入约一个工作日,部分模型还是经第三方推理商测的,可能系统性低估开源。其他量尺方向不一:Epoch ECI 显示 2026 年上半年滞后从约 3 个月微增到约 4 个月;英国 AISI 的网络安全评估则显示 2026 年从 6–10 个月收窄到 4–7 个月。METR 在 2026 年没有测过任何开源模型,长任务量尺上开源 2026 年的位置目前是空白。

**理由**:一、复算(数据 metr runs10.jsonl,TH1.0 runs;脚本 /private/tmp/claude-502/-Users-cissychen-design/1d6c6872-cb3a-41af-9b1a-b757938b5350/scratchpad/r2s/lag.py、sens.py、lag2.py)。每个模型做加权 logistic 拟合求 p50,权重用 invsqrt_task_weight。滞后定义:闭源前沿包络(取历史最高值,对数线性插值)到达该开源模型 p50 的日期,与开源模型发布日之差。点估计完全复现:V3 6.2、R1 3.4、V3-0324 6.1、R1-0528 6.8、gpt-oss-120b 7.2、Kimi K2 Thinking 8.2 个月。另一种算法拿闭源前沿做指数趋势线(倍增期约 134 天),结果相近:R1 3.1、R1-0528 6.3、gpt-oss 6.5、Kimi 8.0。所以数字稳健,不取决于用哪种算法。

二、统计可区分性。按 task family 做配对 bootstrap(B=200–300),每轮闭源包络也一起重拟,因此包络本身的不确定性已计入。
- 单模型滞后 90% CI:R1 2.4–7.1,R1-0528 5.4–11.3,gpt-oss 5.3–9.9,Kimi 6.7–11.1,区间宽且互相重叠。
- Kimi 减 R1:中位 4.4 个月,90% CI 1.8–7.9,P(差≤0)≈0.01。在任务抽样意义上可区分。
- Kimi 减 V3(2024-12):中位 2.9,90% CI 0.9–5.6,也可区分。
- Kimi 减 R1-0528:中位 1.4,90% CI −2.0 到 4.1,P(差≤0)≈0.20,不可区分。
- 注意:bootstrap 只覆盖任务抽样噪声,没覆盖 run 内随机性、发布日的选取、elicitation/provider 差异,真实不确定性更大。

三、R1 是不是选样造成的异常点:部分是。R1 是 2025 年初的低点:比它早一个月的 V3 滞后 6.2,晚两个月的 V3-0324 滞后 6.1。"从 3.4 拉长到 8.2"拿 R1 当起点,夸大了幅度。拟合滞后随时间的斜率:6 个开源模型全用是 +3.9 个月/年;去掉 R1 是 +2.45;只看推理模型 R1-0528、gpt-oss、Kimi 是 +3.1。方向(变长)在去掉 R1 后仍在,幅度从"翻倍多"降到"约 2 个月"。年中以后(R1-0528 到 Kimi)的变化统计上不可区分。

四、elicitation 偏差。METR 的 DeepSeek/Qwen 报告写明每个模型只花"roughly one workday"做 elicitation,用 Triframe 脚手架、走 OpenRouter,并承认可能存在更好的脚手架。Kimi K2 Thinking 在 METR 表中标注"inference via Novita AI",走的是第三方推理商。第三方部署质量参差,可能压低分数。这些偏差全部朝一个方向:低估开源、拉长滞后。不过闭源模型同样走 METR 的标准流程,偏差大小未知,没法定量修正。这是系统性风险,不是证伪。

五、独立量尺对照(反证与佐证):
1. Epoch ECI:2023-01 到 2025-10 平均滞后约 3 个月;2026-01-01 到 05-28 约 4 个月(8 ECI 点,90% CI 7–11),Epoch 自称比之前"slightly larger"。方向同向(略变长),幅度比 METR 小得多,而且是综合指数,不是长任务量尺。
2. UK AISI Frontier AI Trends Report(2025-12):开源闭源差距"过去两年在收窄",现为 4–8 个月。但其中的 8 个月引用的就是 METR,不独立。
3. AISI 网络安全专项:从 2025 年多数时间的 6–10 个月收窄到 GLM-5.2 / DeepSeek V4-Pro 的 4–7 个月。方向相反,而且时段是 2026,正好落在 METR 空白期。
4. CAISI 评估 DeepSeek V4 Pro(2026-04 测、05 发布):约 8 个月,与 GPT-5 相当。水平高,但只是一个点,没有趋势。有人质疑其选样(用 IRT 加两套私有题集,只留 GPT-5.4 mini 作对照)。
5. Terminal-Bench 2.x:只找到厂商自报、harness 各异的分数,算不出干净的月份滞后。任务方给的"同 harness 约 3 个月"本席没能独立找到一手来源。
6. Arena:2026-09 报道说 Elo 差距扩大到 29 分。来源是二手报道,模型名未核实,也不是长任务量尺。
7. Vending-Bench(111 天)、APEX-Agents(约 5 个月):本席未独立复核,只作背景。

六、METR 2026 年是否空白:Wikipedia 转录的 METR 表里,2026 年条目只有 Opus 4.6、GPT-5.3-Codex、Gemini 3.1 Pro、GPT-5.4、Mythos Preview、GPT-5.6 等闭源模型。开源模型全是 TH1.0 数值,TH1.1 yaml 里也没有开源模型。"2026 年这一量尺对开源是空白"成立。

综合:"在 METR 量尺上 2025 年开源滞后变长"这个方向,在 METR 内部算稳健:换趋势定义、去掉 R1 都成立,对 V3 和 R1 的差也可区分。但幅度主要靠 R1 这个低点撑着;只看年中以后是噪声级。而且它是单一评测方、低 elicitation、经第三方推理商测出来的。同时期其他量尺里,只有 Epoch 同向但幅度小;AISI cyber 2026 和 AISI 总报告给的是收窄。所以没法升级为多源证实,应写成"METR 量尺上 2025 年呈拉长迹象,其他量尺方向不一"。

**method_issues**:
- 样本小:有滞后可算的开源模型只有 6 个(Qwen2.5-72B 低于包络起点,算不出),推理型开源只有 4 个
- 单模型滞后的 90% CI 宽 4–6 个月,互相重叠;Kimi 对 R1/V3 的差在任务 bootstrap 下可区分,对 R1-0528 不可区分(P≤0≈0.20)
- 选样:R1(3.4)夹在 V3(6.2)和 V3-0324(6.1)之间,是低点;拿它当起点夸大了增幅。斜率从 +3.9 个月/年(含 R1)降到 +2.45(去掉 R1)
- bootstrap 只覆盖任务抽样噪声,没覆盖 run 随机性、发布日认定、provider 和 elicitation 差异,真实不确定性更大
- elicitation 不对称:METR 对开源约一个工作日、统一用 Triframe;Kimi 经 Novita 第三方推理。偏差朝一个方向(低估开源、拉长滞后),但幅度没法量化
- 滞后的定义依赖闭源包络插值。Kimi 的 p50(57.6 分钟)由 Claude 3.7 Sonnet(55.3 分钟,2025-02)一点决定,对单个闭源点敏感
- AISI 趋势报告的 8 个月引自 METR,不能当独立佐证;Terminal-Bench 只有厂商自报、harness 各异的数字,没有一手同 harness 月份滞后
- 独立量尺的时段大多在 2026(AISI cyber、Epoch 2026H1、CAISI),METR 自算在 2025。时段不重叠,严格说不能直接比

**independent_measurements**:
- https://epoch.ai/data-insights/open-closed-eci-gap — Epoch ECI 开源滞后:2023-01 到 2025-10 平均约 3 个月;2026-01 到 05-28 约 4 个月(8 ECI 点,90% CI 7–11),自称 slightly larger。方向同向(略变长),幅度远小于 METR 自算
- https://www.aisi.gov.uk/work/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber — AISI 网络安全专项:2025 年多数时间 6–10 个月,收窄到 GLM-5.2/DeepSeek V4-Pro 的 4–7 个月。方向相反(收窄),时段为 2026
- https://aisi.gov.uk/frontier-ai-trends-report — AISI 趋势报告(2025-12):差距过去两年在收窄,现为 4–8 个月。方向相反,但 8 个月引自 METR,不独立
- https://nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro — CAISI:DeepSeek V4 Pro 约落后 8 个月(≈GPT-5)。水平与 Kimi 的 8.2 一致,单点无趋势,方法有争议(IRT、私有题集)
- https://metr.org/evaluations/deepseek-qwen-report/ — METR 官方:mid-2025 DeepSeek ≈ late-2024 前沿;每模型 elicitation 约一个工作日、Triframe、走 OpenRouter;自认可能有更好的脚手架。与自算同向,同一来源
- https://en.wikipedia.org/wiki/METR — METR 表转录:开源模型只有 TH1.0 数值(Kimi K2 Thinking 58 分钟,inference via Novita AI);2026 年条目全是闭源,证实空白
- https://cryptobriefing.com/arena-ai-frontier-open-weight-model-gap-widens/ — Arena Elo 差距扩大到 29 分(2026-09,二手报道,未核实)。同向但量尺不同
- 本席复算 METR runs10.jsonl:点估计完全复现(R1 3.4 / R1-0528 6.8 / gpt-oss 7.2 / Kimi 8.2);趋势线法 3.1/6.3/6.5/8.0;配对 bootstrap Kimi−R1 中位 4.4 [1.8, 7.9],Kimi−V3 2.9 [0.9, 5.6],Kimi−R1-0528 1.4 [−2.0, 4.1]

**search_angles**:
- Epoch AI open-weight lag frontier months 2026 → 找到 ECI data insight(3→4 个月)
- Epoch open-closed-eci-gap 全文后半段 → 确认 2023–2025 约 3 个月、2026H1 约 4 个月,slightly larger
- METR time horizon 开源模型 Kimi/DeepSeek/gpt-oss → 找到 Wikipedia 表与 deepseek-qwen 报告;gpt-oss 无单独报告
- METR deepseek-qwen 报告 → elicitation 一个工作日、Triframe、OpenRouter
- Wikipedia METR 表的开源与 2026 条目 → 2026 无开源,开源只有 TH1.0
- METR Kimi K2 Thinking Novita 说明 → 没搜到 METR 对第三方推理影响的说明(无结果)
- CAISI DeepSeek/Kimi 评估 → 只有 DeepSeek V4 Pro 约 8 个月;CAISI 没有 Kimi 评估(无结果)
- AISI Frontier AI Trends open/closed gap cyber → 趋势报告 4–8 个月收窄(8 个月引自 METR)、cyber 6–10 收窄到 4–7
- Terminal-Bench 2.0 开源与闭源月份差 → 没有一手同 harness 月份滞后,只有厂商自报 2.1 分数(无可用结果)
- Arena 开源与闭源 Elo 差距 2026 → 二手报道 29 Elo 扩大(未核实)
- 未搜:Vending-Bench、APEX-Agents 的开源滞后(任务已给数字,本席未独立复核)
- 本地复算:METR TH1.0 runs 加权 logistic、包络法和趋势线法、按 task family 配对 bootstrap、去掉 R1 的敏感性

## R2-metr-open-lag · method → **降级为弱结论**

**可用表述**:在 METR 的 time horizon 量尺(TH1.0)上,2025 年测过的几款开源模型(DeepSeek-R1-0528、gpt-oss-120b、Kimi K2 Thinking)落后闭源前沿约 6–9 个月(自算,bootstrap 90% CI 大致落在 5–12 个月)。这比 DeepSeek-R1 发布时约 3–5 个月的最窄点宽,但没有回到 2024 年 Qwen 时期的 10–18 个月。也就是说,R1 带来的收窄在 2025 年没有延续,差距停在半年以上,并有小幅回弹。这一结论只来自 METR 一家机构、少数几款由它挑选的开源模型,而且 METR 对开源模型的调优投入有限。Terminal-Bench、AISI 等其他长程量尺多数给出 3–8 个月且部分在收窄,方向并不一致。2026 年起 METR 的新版量尺(TH1.1)没有测过任何开源模型,因此这把尺子对 2026 年的开源与闭源差距无法回答。

**理由**:复算用 METR TH1.0 的 runs10.jsonl(41,629 条 run),逐模型拟合 logistic(成功率对 log2 人类耗时),得到 p50;再对闭源 SOTA 包络做 log-线性前沿趋势,滞后 = 开源发布日减去趋势线达到同一 p50 的日期。用 2024 年起的趋势时复现出原数:R1 3.5、R1-0528 6.6、gpt-oss 6.7、Kimi 8.2 个月,所以数字本身没有算错。问题出在用它们承重的叙述上。

(1) 统计可区分性。按 task family 做 200 次配对 bootstrap:Kimi 减 R1 的 90% CI 为 [2.5, 7.4] 个月(2024 起趋势)或 [0.9, 6.9](2023 起),P(>0) 为 0.98 到 0.99,所以单看 8.2 对 3.4 是可区分的。但去掉 R1 后:Kimi 减 R1-0528 是 [-1.0, 3.6],P 为 0.86;2023 起趋势下是 [-2.5, 3.3],P 为 0.70,都不可区分。R1 之后 4 个点的 90% CI 互相重叠(约 5–10 个月)。

(2) R1 是局部最低点,有选样问题。同一条曲线上 2024 年的 Qwen2-72B 滞后约 10–18 个月、Qwen2.5-72B 约 10–14、DeepSeek-V3 约 5–7。整个序列是 V 形或"先收窄后回弹",不是单调拉长。"2025 年内在拉长"只在以 R1 为起点时成立;起点挪到 V3(2024-12),Kimi 减 V3 的 P 为 0.85 到 0.97,对设定敏感。

(3) 方法敏感性。改用阶梯法(第一款 p50 不低于该开源模型的闭源 SOTA)得到 R1 1.5–3.0、Kimi 6.7,方向不变但幅度更小。趋势起点(2019、2023、2024)和权重(invsqrt、equal、无权重)只让 Kimi 在 7.9–8.6 之间、R1 在 3.1–5.6 之间移动。另外,滞后的绝对数完全取决于"前沿"怎么定义,Opus 4.5 在 2025-11 跳到约 247 分钟,高出趋势线。

(4) 覆盖偏差。开源样本只有 METR 挑选的 8 个,2025 年下半年只有 gpt-oss-120b 和 Kimi K2 Thinking 两个点。当时可能更强的开源模型(DeepSeek V3.1/V3.2、Qwen3 系、GLM-4.x 等)没有测,"最强开源"可能被低估,滞后被高估。

(5) Elicitation 与脚手架。原始 runs 显示开源模型和 Opus 4.5 用 flock-public 脚手架,GPT-5 用 flock-secret。开源模型致命错误比例偏高(R1 189/1346,约 14%;Kimi 77/1006)。METR 自述对开源约一个工作日的 elicitation,系统性低估开源的可能真实存在,但大小无法量化。错误率在开源模型间是下降的,这一项不会制造"拉长"的假象,但会抬高整体滞后水平。

(6) Kimi 的 run 数较少(1006 条,4 小时以上任务 147 条),长任务端的 CI 主要靠少数成功样本。

(7) 外部一致性。其他长程量尺给出约 3–8 个月,其中 AISI cyber 从 6–10 收窄到 4–7,Terminal-Bench 同 harness 约 3 个月,方向和"拉长"不一致或相反。所以"最直接的量尺显示拉长"是单机构、单量尺、依赖起点的结果,不宜作为趋势结论承重。

(8) 后半句"2026 年对开源是空白"属实:TH1.1 的结果文件里只有闭源模型(包括 Gemini 3/3.1、GPT-5.x、Opus 4.6、Mythos preview),2026 年的 METR 文章也没有开源 time horizon。

结论:不否决,但"在拉长"必须降级为"R1 之后没有继续收窄,稳定在约 6–9 个月,且有回弹迹象",并且要标明单一来源、起点依赖和覆盖偏差。

**method_issues**:
- 起点依赖:'拉长'以 DeepSeek-R1 这一局部最低点为基准。2024 年 Qwen2-72B 和 Qwen2.5-72B 的滞后约 10–18 个月,全序列呈 V 形;起点换成 V3 或 R1-0528,差异的显著性下降或消失(Kimi 减 R1-0528 的 P(>0) 只有 0.70–0.86)
- 样本量:2025 年下半年只有 gpt-oss-120b 和 Kimi K2 Thinking 两个开源点;R1 之后 4 个点的 90% CI(约 5–10 个月)互相重叠,无法确立单调趋势
- 覆盖与选样:METR 只测了自选的开源模型,同期可能更强的 DeepSeek V3.1/V3.2、Qwen3、GLM-4.x 等没有测,'最强开源'可能被低估、滞后被高估
- Elicitation 不对称:原始 runs 显示开源模型用 flock-public 脚手架,GPT-5 用 flock-secret;开源模型致命错误比例较高(R1 约 14%);METR 对开源约一个工作日的调优,可能系统性抬高滞后水平
- 前沿定义敏感:趋势法得到 Kimi 7.9–8.6、R1 3.1–5.6 个月;阶梯法得到 Kimi 6.7、R1 1.5–3.0 个月;Opus 4.5 高出趋势线,用实际 SOTA 还是趋势线会改变数值
- Kimi 只有 1006 条 run,4 小时以上任务 147 条,长任务端靠少量成功样本(11 次)
- 单一机构、单一量尺(METR 既定义任务又挑选模型),与 AISI cyber(收窄)、Terminal-Bench(约 3 个月)等外部量尺方向不一致
- 版本漂移:TH1.0 与 TH1.1 任务集不同,TH1.1 没有开源数据,2025 年的结论不能外推到 2026 年

**independent_measurements**:
- 自算复现(METR runs10.jsonl,family bootstrap B=200,2024 起前沿趋势):R1 3.9 [2.0, 6.1]、R1-0528 6.9 [4.7, 10.3]、gpt-oss 7.1 [5.4, 10.1]、Kimi 8.6 [7.1, 10.7] 个月;Kimi 减 R1 为 [2.5, 7.4],P=0.99,与原论断同向
- 自算(2023 起前沿趋势):R1 5.5 [2.9, 8.5]、Kimi 9.0 [7.2, 11.6];Kimi 减 R1-0528 为 [-2.5, 3.3],P=0.70,R1 之后的'继续拉长'不成立
- 自算:Qwen2-72B(2024-06)约 12–18 个月、Qwen2.5-72B(2024-09)约 10–14 个月、DeepSeek-V3(2024-12)约 5–7 个月。2024 到 2025 的长期趋势是收窄后回弹,不是持续拉长
- METR TH1.1 的 benchmark_results_1_1.yaml 模型列表里没有任何开源模型,'2026 空白'同向确认
- 任务方提供的外部量尺:Terminal-Bench 同 harness 约 3 个月、AISI cyber 从 6–10 收窄到 4–7 个月、Vending-Bench 约 111 天、APEX-Agents 约 5 个月、CAISI 约 8 个月。水平相近(3–8 个月),但多数没有显示拉长,部分显示收窄,方向不一致

**search_angles**:
- 下载 METR TH1.0 runs 自行拟合 p50 并复现滞后(成功复现 3.4/6.8/7.2/8.2 的量级)
- 三种任务权重(invsqrt、equal、无)的敏感性
- 前沿定义:2019、2023、2024 起的趋势线,以及阶梯法 SOTA
- task-family 配对 bootstrap,检验差值显著性
- 去掉 R1 和改换起点(V3、R1-0528、Qwen 系)的敏感性
- 原始 runs 里的脚手架、致命错误率、长任务样本量(elicitation 不对称)
- TH1.1 结果文件是否有开源模型(没有)
- METR 2026 年博客和笔记里是否有开源 time horizon(只找到对 CAISI DeepSeek V4 Pro 评估的引用,没有 METR 自测数据)
- 没有独立搜索 2025 年下半年其他开源模型是否被第三方用 METR 任务集测过(未找到,未查)

## R3-arena-perception · counter → **降级为弱结论**

**可用表述**:把 2026 年 10 月的 Arena 风格控制榜和 Epoch ECI 对齐看:在全部 111 个模型上两者高度一致(Spearman 0.95);但只看 ECI 前 15 名时,相关降到约 0。这不是"范围窄了相关自然变低"造成的:在同样这 15 个模型里,各项能力基准彼此的排序相关中位数仍有 0.69,脱钩的只有 Arena。换不换风格控制、名称匹配怎么做,结论都不变。不过 Arena 在头部并没有失去分辨力:前 15 名里约四成的模型对,置信区间互不重叠。它只是按另一种标准排序,几款 Flash 级模型会排在旗舰之前。所以更稳妥的说法是:在前沿区间,偏好排行榜已经不能当作能力的代理指标。至于原因是用户在日常提示上分不出来,还是在奖励风格、速度、说服力或刷榜带来的过拟合,现有数据还区分不了。

**理由**:一、复算与匹配误差(arena/corr.py 与 ctrl.py,工作目录在 scratchpad/arena)。111 / 0.947 / −0.025 / 0.192 四个数都能原样复现。匹配方面:前 15 名里只有 1 个模型的名字和 ECI 完全一致,其余 14 个都靠前缀匹配到带 -high/-max/-xhigh 后缀的变体。"多个变体取最高分"在前 15 名里只影响 Claude Opus 5 一个模型(两个变体差 0.7 分),改取最低分后前 15 名仍是 −0.025,前 30 名从 0.192 变成 0.235。只看精确匹配时,111 个里剩 48 个,相关 0.911。所以匹配方式不改变结论。不过匹配规则前后不一致:Opus 4.6 精确匹配到不带后缀的版本(1497.7),而它的 -high 变体是 1504.4;其他模型拿的却是推理加档变体。这只是小瑕疵,但文章如果点名 Opus 4.6,应注明用的是哪个变体。

二、范围受限对照(核心检验)。同样取 ECI 前 15 名,在 Epoch processed_data 里两两计算各能力基准之间的 Spearman:共 171 对,中位数 0.69(四分位 0.55 到 0.79),低于 0.2 的只占 7%。前 30 名共 232 对,中位数 0.65。另外,按综合分选样会产生 Berkson 效应,把成分之间的相关往下压,所以 0.69 只会偏保守。反观 Arena 和单个基准在前 15 名内的相关:FrontierMath −0.04 和 −0.14,GPQA −0.34,OTIS 0.00,APEX-Agents 0.41,DTBench 0.54,整体中位数大约 0.15。结论是:范围受限不能把"≈0"解释掉。在同一窄范围里,能力量尺彼此仍然高度一致,只有 Arena 脱钩。这一层描述性发现经得起检验。

三、风格控制。用 raw 榜(不做风格控制)重算,前 15 名 −0.075,前 30 名 0.054,111 个全体 0.914。风格控制不改变结论。

四、"失去区分能力 / 用户感知饱和"这层机制解释有反证。Arena overall 按 Arena 自己排出的前 15 名,分差 37 分;105 对模型中有 39 对的 95% 置信区间不重叠。按 ECI 选出的前 15 名,Arena 分差 51 分,置信区间宽度中位数约 10。hard_prompts 类目里 46/105 对可分。也就是说,Arena 在前沿仍然能把模型分开,只是排出的顺序和能力量尺几乎正交:Gemini 3.7/3.8 Flash、Muse Spark 1.3 排在 GPT-6 Sol、GPT-6.1 Sol 之上。这更像"偏好测的是另一个维度"(风格、速度、说服力、刷榜过拟合),而不是"用户分不出来"。只有 expert 和 math 是 0/105 可分(分差 22 和 28),但这两个类目票数少、置信区间宽,零可分既可能是感知饱和,也可能只是样本量不够,目前无法区分。文章用的两个具体例子也要降调:Kimi K3 是 1488 [1483, 1493],GPT-6.1 Sol 是 1484 [1475, 1493],置信区间重叠,"K3 排在 GPT-6.1 Sol 之上"在统计上不显著。Opus 4.6-high 是 1504 [1501, 1508],Opus 5.5 是 1507 [1499, 1515],置信区间重叠这一点成立。

五、独立文献。没有找到哪个独立团队专门测过"前沿区间内 Arena 与能力基准的相关"。能找到的旁证有四条,都只能支持描述层,不能支持"感知饱和"这个机制:
(a) LMSYS 自己的 Arena-Hard 博客:Spearman 不惩罚头部错排,把置信区间考虑进去后,MT-Bench 与 Arena 的一致性从 91.3% 掉到 22.6%。这是头部排序一致性很脆弱的方法学先例。
(b) The Leaderboard Illusion(arXiv 2504.20879,NeurIPS 2025):私下测试多个变体、各家拿到的数据量不均、对 Arena 分布过拟合。这给出了一个和"感知饱和"竞争的解释,即 Arena 测的是 Arena 特有的东西。
(c) LessWrong 上 Baybar 2025-09 的帖子:前沿模型的 Elo 系统性高于算力/时间趋势线,作者推测 Elo 奖励的是说服力。
(d) arXiv 2608.29843(质量调整价格指数):在 69 个模型的全范围上,它的指数和 Arena 相关,|ρ|≈0.70。这只与全范围高相关同向,不涉及头部。
此外,arXiv 2605.18840 只分析了 SWE-bench 与 GPQA 两项基准的耦合,不涉及 Arena。

综合判断:"前沿区间 Arena 与能力量尺脱钩"这条描述性结论,经范围受限对照、匹配敏感性和风格控制三项检验都成立。但这些都是同一份 Epoch 数据集上的内部稳健性检验,算不上独立团队的多源证实,在这一层只能维持单源。文章真正承重的是"失去区分能力、反映用户感知饱和"这个机制判断,它与 39/105 对可分、分差远大于置信区间这两组数据相冲突,替代解释(测的是不同维度、刷榜过拟合)至少一样有力。所以结论整体降级为弱结论,需要改写措辞。

**method_issues**:
- 名称匹配:前 15 名中 14 个靠前缀匹配到推理档变体,只有 1 个精确匹配;Opus 4.6 精确匹配到无后缀版本(1497.7),而非 -high(1504.4),变体选取规则前后不一致。对相关系数影响很小(取最高/最低变体:前 15 名均为 −0.025,前 30 名 0.192/0.235)
- 范围受限:已用同一 top-15 集合里基准两两相关做对照(中位数 0.69),可排除"≈0 是范围受限的数学产物"。但 ECI 本身由这些基准合成,ECI 与单个基准的相关偏高,不可直接比较;基准两两相关才是干净对照,且 Berkson 效应使它偏保守
- n=15 时 Spearman 的抽样误差很大(约 ±0.5),−0.025 与 0.15 甚至 0.3 统计上难以区分。应表述为"接近零、远低于能力量尺之间的相关",不宜写成精确的 −0.025
- 从"相关≈0"推到"失去区分能力"是推断跳跃:Arena 头部 39/105 对置信区间可分,分差远大于置信区间,说明它在区分,只是维度不同
- 从"困难类目分差不比 overall 大"推到"用户感知饱和":expert/math 零可分很可能源于票数少、置信区间宽,无法与饱和区分;hard_prompts 可分对数(46)反而多于 overall(39)
- "用户感知饱和"与竞争解释(风格残差、速度、说服力、Leaderboard Illusion 所述的私测与过拟合)在现有数据中无法区分,缺少针对性检验(如控制回答长度和延迟的盲测、专家标注的正确性)
- 独立性:所有对照都基于同一份 Epoch 数据和同一份 Arena 数据,属于内部稳健性检验,不构成独立团队的多源证实

**independent_measurements**:
- 自算对照(同一 Epoch 数据集,非独立团队):ECI 前 15 名内能力基准两两 Spearman 中位数 0.69(171 对,IQR 0.55–0.79),前 30 名 0.65(232 对)。说明范围受限不能把相关压到约 0;与 R3 中 Arena 约 0 的结果方向一致,支持"Arena 在头部脱钩"
- 自算:ECI 前 15 名内 Arena 与单个基准的 ρ:FrontierMath T1-3 −0.14,T4 −0.04,GPQA −0.34,OTIS 0.00,ARC-AGI-2 0.15,APEX-Agents 0.41,DTBench 0.54。中位数约 0.15,与 R3 同向
- 自算:raw 榜(无风格控制)前 15 名 ρ=−0.075,前 30 名 0.054,全体 0.914。风格控制不改变结论,与 R3 同向
- 自算:Arena overall 前 15 名分差 37 分,39/105 对置信区间不重叠;hard_prompts 46/105;coding 11/105;expert 0/105;math 0/105。与"失去区分能力"的说法反向(expert/math 除外)
- 自算:Kimi K3 1488 [1483,1493] 与 GPT-6.1 Sol 1484 [1475,1493] 置信区间重叠,"K3 高于 GPT-6.1 Sol"不显著;Opus 4.6-high 1504 [1501,1508] 与 Opus 5.5 1507 [1499,1515] 重叠,这一点成立
- https://lmsys.org/blog/2024-04-19-arena-hard:Arena-Hard 与 Arena 的 Spearman 为 94.1%,但计入置信区间后 MT-Bench 一致性从 91.3% 降到 22.6%。独立测量,方法学上支持"头部排序一致性脆弱"
- https://arxiv.org/abs/2504.20879(The Leaderboard Illusion):私测变体、数据分配不均,arena 数据进 SFT 可使 ArenaHard 胜率从 23.5% 升到 49.9%。支持"Arena 测的不是一般能力",但给出的机制与"感知饱和"相竞争
- https://www.lesswrong.com/posts/jrDgzQv5YZsjudcPg/what-is-lmarena-actually-measuring:前沿模型 Elo 系统性高于 log-FLOP/时间趋势(如 Gemini 2.5 Pro 高约 71 分),作者推测奖励说服力。与"Arena 偏离能力"同向,与"饱和"的解释不同
- https://arxiv.org/pdf/2608.29843:质量调整指数与 LMArena 在 69 个模型的全范围上 |ρ|=0.70,与 Epoch 指数 0.93(有共享输入)。只与全范围高相关同向,无头部数据
- https://arxiv.org/abs/2605.18840:只做 SWE-bench 与 GPQA 两基准的耦合(r=0.72,34 个模型),不涉及 Arena,无关

**search_angles**:
- Chatbot Arena 与基准在前沿/头部区间的 Spearman 相关(找到 LMSYS Arena-Hard 博客、Auto-Arena、MixEval 等,多为 2024 年中低端模型样本,没有前沿头部专项研究)
- The Leaderboard Illusion(找到,arXiv 2504.20879,NeurIPS 2025)
- Epoch AI 关于 LMArena 与 ECI 相关的分析(没找到 Epoch 官方直接分析;找到 benchmark-correlations data insight 与 LessWrong 帖子)
- LMArena 风格控制博客及风格对排名的影响(找到 lmsys/arena.ai style-control 博客:长度是主效应)
- 人类偏好榜饱和、用户分不出前沿模型(2026)(没找到直接检验"用户分不出"的研究;arXiv 2605.18840 只涉及 SWE/GPQA,与 Arena 无关;其余为 SEO 博客)
- AI Revealed Preferences arXiv 2608.26178(与主题无关:研究模型自身偏好)
- LMArena Expert/职业类目与 Artificial Analysis Intelligence Index 的相关(没找到量化研究)
- 质量调整价格指数论文 arXiv 2608.29843 中 LMArena 的相关(找到全范围 |ρ|=0.70)
- 自算:名称匹配敏感性(最高/最低变体、仅精确匹配)
- 自算:范围受限对照(top-15/top-30 中能力基准两两相关 vs Arena 与基准的相关)
- 自算:raw 榜与风格控制榜对比
- 自算:Arena 各类目头部置信区间可分对数,以及 Kimi K3/GPT-6.1 Sol、Opus 4.6/5.5 置信区间核对

## R3-arena-perception · method → **降级为弱结论**

**可用表述**:把 2026-10-08 的 Arena 风格控制榜与 Epoch ECI(2026-10)按模型名对上,得到 111 个模型。全样本 Spearman 约为 0.95,其中部分来自不同代际模型之间的时间差;只看 2026 年发布的模型约为 0.72。在 ECI 前 15 名内,相关跌到 −0.1 到 0.3 之间(n=15,不确定度很大),Arena 分数对 ECI 的斜率从约 6 Elo/点降到接近 0。这种脱钩不能简单归因于"头部样本范围太窄":在同一批前沿模型里,其他独立基准两两之间的相关中位数仍约为 0.7;去掉风格控制后,脱钩反而更明显。但 Arena 并没有失去区分能力,它在头部仍能把模型稳定地排开(约 50 Elo 的分差,远大于置信区间),只是排序依据的不再是综合能力指数所衡量的东西。比较合理的读法是:在前沿区间,偏好榜和能力指数测的已经不是同一样东西。"普通用户在日常提示上感觉不到能力差异"是可能的解释之一,但现有数据没法把它和另外两种解释分开:一是两者测的构念不同(对话体验、编码、指令遵循等),二是厂商提交多个变体再择优上榜、把头部分数压缩了。所以这条只能作为背景观察,不能用来证明"能力在收敛"或"能力没在收敛"。

**理由**:数据:我重新下载了 Epoch 的 benchmark_data.zip(eci_scores、eci_bootstraps 和 processed_data_for_eci),用的是 Arena HF 数据集 2026-10-08 的 text_style_control 与 text 两份 parquet,脚本在 scratchpad/audit/a1–a5.py。复算结果与 R3 完全一致:111 / 0.947 / 0.192 / −0.025。

(1) 名称匹配误差。把规则从"多变体取最高分"换成取均值或最低分,前 15 名仍为 −0.025,前 30 名在 0.19 到 0.24 之间。原规则有一处不一致:只要有完全同名的条目就不再看 -high 变体,Opus 4.6、4.7、4.8 都受影响。改成对所有变体一致地取最高分,并剔除 flash-lite 这个错配后,前 15 名为 −0.08,前 30 名为 0.18。只用完全同名匹配时(n=48),前 15 名是 0.72,但那 15 个模型 ECI 偏低,不是同一个前沿集合,不能拿来比。另一个敏感点是"前 15"怎么定义:如果取全体 ECI 模型的前 15 再去和 Arena 交集(n=12),相关是 0.27。所以 "≈0" 这个点估计不稳,但始终在 0 到 0.3 之间。结论:匹配误差改变不了量级。

(2) 范围受限。这一点不能把发现解释掉,反而让发现更硬,理由有三。第一,零假设模拟:假定全样本的线性关系(斜率 6.3 Elo/ECI 点,残差 SD 37)在前沿同样成立,前 15 名的 Spearman 中位数应为 0.55(90% 区间 0.16–0.80),观测值落在这个分布以下的概率约 0.01;前 30 名的期望是 0.55,观测值 0.19,概率约 0.007。第二,斜率塌缩:前 15 名内斜率只有 0.13,前 30 名 0.80,而 ECI 后 81 名为 6.7。第三,对照独立量尺:同样在 ECI 前 15 名内,171 对基准两两相关的中位数为 0.69(IQR 0.55–0.79),与 Epoch 自己公布的跨类别中位数 0.68 吻合。可见范围受限本身并不会把相关压到 0。只有 GPQA 这类已饱和的基准表现得像 Arena(与 ECI 相关 0.35,与 Arena 相关 −0.47)。但这个推断不确定度很大:n=15 时按模型重抽样,90% 区间是 [−0.52, 0.44]。

(3) 风格控制。去掉风格控制(原始 text 榜)后,前 15 名为 −0.07,前 30 名为 0.05,脱钩更严重。所以结论不是风格控制制造出来的。不过风格控制把 ECI 前 15 模型在 Arena 上的分差从约 120 Elo 压到了 51,说明原始榜头部的分差大半是文风带来的。

(4) 致命问题在"失去区分能力"这个措辞和"用户感知饱和"这个归因。用 Arena 的 CI 注入噪声重抽样,前 15 名内 Arena 自身的秩可靠度约 0.96(ECI 约 0.94)。前 15 名 Arena 分差 51 Elo,95% CI 平均宽度只有 11.5。也就是说 Arena 在前沿依然能稳定地把模型排开,只是排的维度和 ECI 不同,所以不是"失去区分能力"。分类目看也是这样:coding 前 15 名相关 0.45,instruction_following 0.32,expert 0.26,hard_prompts 0.01,multi_turn −0.37。逐个基准看,Arena 与 FrontierCode(0.63)、LMCA(0.67)、DTBench(0.69)、ProofBench(0.59)仍有中等相关,与 FrontierMath(0.06–0.20)和 GPQA(−0.47)几乎无关或负相关。这更像"偏好榜在前沿测的是另一种构念(对话体验、编码与指令遵循)",而不是"用户分不出来"。数据本身没法区分"感知饱和"和"构念不同"这两种解释;Arena 没有对照实验(比如盲测专家能否辨别),"用户感知饱和"属于未经检验的归因。

(5) 例证逐条核对。
- Opus 4.6 与 Opus 5.5 CI 重叠:基础版 claude-opus-4-6 为 1497.7 [1494.4, 1501.0],Opus 5.5-high 为 1507.1 [1499.0, 1515.2]。两个 CI 只重叠约 2 分,差值 9.3 Elo,差值的 z≈3.5,统计上显著。"CI 重叠所以分不出"是一个常见的统计误读。改用 opus-4-6-high(1504.4)后差值只有 2.7 Elo,才真正打平,但胜率差约 51% 对 49%。正文应写成"差距 ≤9 Elo,约 51% 胜率",不要写"CI 重叠"。
- Kimi K3 排在 GPT-6.1 Sol 之上:4.4 Elo,z≈0.8。这是打平,不是倒挂,不能当作"排反了"的证据。
- 困难类目头部分差不比 overall 大:成立。第 1 名减第 10 名,overall 31,hard_prompts 34,expert 16,coding 22;但 expert 和 coding 的 CI 更宽(23 和 15)。

(6) 选样与利益冲突。前 15 名里多数是 -max/-high 推理档位的变体,而 ECI 各基准的评测档位不一定相同,存在构念错配。Arena 允许厂商提交、私测多个变体,外部研究("The Leaderboard Illusion",Singh 等,2025;未在本会话重新核读)指出这会抬高、压缩头部分数。也就是说,头部压缩有一部分可能是榜单机制造成的,不全是用户感知。另外,全样本的 0.947 本身被时间跨度抬高了(Epoch 的 benchmark-correlations 数据洞察明确警告过这一点):只看 2026 年发布的 55 个模型,Spearman 降到 0.72。所以"全体 0.95 → 前沿 ≈0"这个对比,前一半有夸大。

(7) 独立研究。我没有找到直接测量"Arena 与 ECI 或综合能力指数在前沿区间相关性"的同行评议研究(检索 2 次)。已有工作(SMART filtering arXiv 2410.20245、Chatbot Arena Estimate NAACL 2025)都把 Arena 当作效标,而不是检验它在前沿的效度。所以这是单一数据集上的自算,没有升级为多源的条件。

裁定:实证层面"前沿区间 Arena 排序与 ECI 脱钩"经得起匹配方式、风格控制和范围受限三项检验,可以留作有限承重(n=15、区间宽、单数据集)。"失去区分能力"与事实不符(Arena 内部排序稳定)。"用户感知饱和而非能力收敛"的因果归因没有被识别,必须降级为几种解释之一,并与"构念不同"、"变体择优与榜单机制压缩头部"并列。

**method_issues**:
- 小样本:前 15 名 n=15,按模型重抽样的 90% CI 为 [−0.52, 0.44];'≈0' 只是点估计,应报区间
- 前 15 名的定义不稳:在匹配后的模型里取前 15 得 −0.025;在全体 ECI 模型里取前 15 再与 Arena 交集(n=12)得 0.27
- 匹配规则不一致:只要有完全同名条目就不再看 -high 变体(Opus 4.6/4.7/4.8 等);Gemini 3.5 Flash 错配了 flash-lite。修正后前 15 名为 −0.08、前 30 名为 0.18,量级不变
- 'CI 重叠'被误读为'无差别':Opus 4.6 基础版与 Opus 5.5 差 9.3 Elo,z≈3.5,显著;改用 4.6-high 才打平(差 2.7 Elo)
- Kimi K3 高于 GPT-6.1 Sol 只有 4.4 Elo,z≈0.8,属于打平,不能作'倒挂'证据
- 措辞与数据矛盾:Arena 在前 15 名内的秩可靠度约 0.96,头部分差约 51 Elo,CI 宽约 11.5,有区分能力,只是与 ECI 不同轴
- 因果归因未识别:'用户感知饱和'、'构念不同'(Arena 与 FrontierCode/LMCA/DTBench 相关约 0.6–0.7,与 FrontierMath/GPQA 约 0 或为负)、'变体择优与榜单机制压缩头部'三种解释无法用这些数据区分
- 构念错配:Arena 上是 -max/-high 等推理档位变体,ECI 各基准的评测档位未必一致
- 全样本 0.947 受时间跨度抬高(Epoch 自己有警告);只看 2026 年发布的模型降到 0.72,'0.95 → 0' 的反差被夸大
- 利益冲突与机制偏差:Arena 允许厂商私测、择优发布变体(Leaderboard Illusion 2025),可能人为压缩头部
- 单一数据集自算,没有独立研究复核前沿区间的 Arena 与能力指数相关
- 肯定性发现:范围受限不能解释结果。线性零模型下前 15 名期望 Spearman 约 0.55(P≈0.01);同一前 15 名内基准两两相关中位数 0.69;风格控制不制造结果(原始榜前 15 名 −0.07)

**independent_measurements**:
- 本地复算(Epoch eci_scores.csv 2026-10 + Arena text_style_control 2026-10-08):全体 n=111 Spearman 0.947,前 30 名 0.192,前 15 名 −0.025,与 R3 一致
- 同上,原始 text 榜(无风格控制):全体 0.914,前 30 名 0.05,前 15 名 −0.07(同向,更强)
- Epoch processed_data_for_eci,ECI 前 15 名内 171 对基准两两 Spearman 中位数 0.69(IQR 0.55–0.79)。这说明范围受限不会把相关压到 0,与 R3 的推断方向一致,但削弱了'≈0 只是范围受限伪影'这一反驳
- Epoch 数据洞察 https://epoch.ai/data-insights/benchmark-correlations:前沿模型跨类别基准相关中位数 0.68,并警告时间跨度会抬高相关(与本地 0.69 吻合;支持对全样本 0.947 打折)
- Arena 分类目前 15 名 vs ECI:coding 0.45、instruction_following 0.32、expert 0.26、hard_prompts 0.01、multi_turn −0.37(方向不一致,部分反驳'全面失去区分')
- Arena 与 ECI 各分量基准在前 15 名内:FrontierCode 0.63、LMCA 0.67、DTBench 0.69、ProofBench 0.59、FrontierMath T1-3 0.06、GPQA −0.47(更支持'构念不同',而非'用户分不出')
- SMART filtering(arXiv 2410.20245)与 Chatbot Arena Estimate(NAACL 2025 industry)把 Arena 当效标,不涉及前沿区间效度,不能作为独立证据
- LessWrong《what is lmarena actually measuring》https://www.lesswrong.com/posts/jrDgzQv5YZsjudcPg/what-is-lmarena-actually-measuring(只看到搜索结果,未读正文,不承重)

**search_angles**:
- 重算匹配:多变体取最大 / 均值 / 最小、只用完全同名匹配、所有变体一致取最大并剔除 lite
- 前 15 名定义:在匹配后模型中取前 15,vs 在全体 ECI 中取前 15 再交集
- 范围受限零模型:在实际 ECI 分布上按全样本斜率加残差噪声做模拟
- 对照独立量尺:ECI 前 15/30 名内各基准两两相关、各基准与 Arena 的相关
- 测量信度:用 ECI 500 次 bootstrap 和 Arena CI 噪声估算两者在前 15 名内的秩可靠度
- 风格控制 vs 原始 text 榜
- 分类目(hard_prompts/expert/coding/math/IF/longer_query/multi_turn/creative)的前 15 名相关和头部分差
- 具体例证 CI 与差值 z 检验(Opus 4.6/4.6-high vs 5.5;Kimi K3 vs GPT-6.1 Sol)
- 时间跨度混杂:只看 2026 年发布的模型
- 确认 ECI 成分里不含 Arena(独立性成立)
- Web:Arena Elo 与基准在前沿区间相关或饱和的研究(没找到直接研究)
- Web:Epoch ECI 与 LMArena 相关(没找到;只有 Epoch 基准相关性数据洞察)
- 没搜到也没核读:The Leaderboard Illusion 正文、LiveBench 论文中 Arena 相关表、Arena 官方关于前沿区分度的博客

## R4-caisi-8months · counter → **方向存争**

**可用表述**:DeepSeek 自报 V4 Pro 只比美国前沿落后约 2 个月;独立测量给出的落后幅度在 4–9 个月之间。美国政府机构 NIST CAISI 估计约 8 个月,Epoch AI 的能力指数复算约 8.5 个月(95% 区间约 5–10 个月,水平相当于 GPT-5),Artificial Analysis 的综合指数约 4–5 个月。差距主要出现在非公开题上:在接近满分的公开题(GPQA、AIME 类数学)上 V4 Pro 与美国模型持平,在 Epoch 的私有数学题 FrontierMath 和 CAISI 的私有智能体/网络安全题上明显落后。独立研究者 Ihle 跨 17 个基准统计,开源模型在私有基准上落后 8–10 个月,在公开基准上落后 4–6 个月。这个模式和"针对公开考卷做了优化"的说法相符,但目前没有直接证据。题目饱和、闭源实验室接触过部分"私有"题、评测脚手架不同,也都能解释同样的结果。另外,CAISI 的私有基准无法复现,而且它是按美国 AI 行动计划来评测中国模型的。

**理由**:一、"约 8 个月"这个数,在一个独立的一手数据集上得到证实。我用 Epoch benchmark_data.zip 里的 eci_scores.csv 复算:DeepSeek-V4-Pro(2026-04-24)ECI = 149.13,95% CI 为 147.31–150.72。美国前沿第一次超过 149.13 的模型是 GPT-5(2025-08-07,ECI 150.0),也就是落后约 8.5 个月;同档的美国模型还有 GPT-5.1(149.64)和 GPT-5.4 Mini(148.84)。按 CI 两端算,区间约 5–10 个月(下端对应 o3-pro 2025-06 的 147.42,上端对应 Gemini 3 Pro 2025-11 的 152.92)。后续的 V4 Pro 0813(2026-08-13)ECI = 155.31,约等于 GPT-5.2 Pro(2025-12,155.4)和 Opus 4.6(2026-02,155.24),仍落后约 6–8 个月。Epoch ECI 对 V4 Pro 用了 15 个基准,数据大多来自第三方或 Epoch 自跑,不是 DeepSeek 自报,所以和 CAISI 算是两个独立组织、两套方法。不过两边的题有重叠(GPQA、OTIS-AIME、SWE-bench Verified),而且 ECI 也含私有题 FrontierMath,不能算完全独立的数据。
二、另一个独立聚合给出的是中间值。Artificial Analysis 在发布时给 V4 Pro(Max)打 52 分(Index v4.0),已经高于 GPT-5.2 xhigh(2025-12 发布,50–51 分;这个分数来自二手报道 The Decoder 和 iThome)。按这个指数算,落后约 4–5 个月,低于 8 个月、高于 2 个月。Epoch 自己的 data insight 说 2026 年最强开源权重模型平均落后封闭前沿 4 个月,但那里比的是"开源前沿"(Kimi K2.6 的 ECI 151.6),不是 DeepSeek 本身。Epoch 另有一条 data insight:2023 年以来中国模型平均落后约 7 个月(区间 4–14 个月)。所以"8 个月"是 DeepSeek V4 Pro 单个模型的数,不等于"PRC 前沿"。按 ECI,V4 Pro 发布时不是最强的中国模型,CAISI 说"美国前沿 tends to lead PRC frontier by ~8 months",这个说法有外推成分。
三、"私有题差距大、公开题差距小"这个模式,有独立证据支持,而且是一手可复算的。在 Epoch 的数据里,V4 Pro 在饱和的公开题上与美国模型持平甚至略高:GPQA 0.879(Opus 4.6 为 0.874),OTIS 0.967(Opus 4.6 为 0.944)。但在 Epoch 私有题 FrontierMath 上明显落后:Tier 1–3 为 0.453(GPT-5 为 0.554,Opus 4.6 为 0.66,GPT-5.4 为 0.786),Tier 4 为 0.024(GPT-5 为 0.22)。Ihle 的 WeirdML 上 V4 Pro 为 0.489,GPT-5 为 0.607。Håvard Tveit Ihle 在 LessWrong(2026-05-28)用 17 个基准、约 110 个数据点、主要基于 Epoch 数据做了分析:私有基准上开源模型落后 8–10 个月,公开基准上落后 4–6 个月。任务里提到的 Epoch 自述"open-weight models tend to perform worse on private benchmarks",我没有在 Epoch 的出版物里找到原话。目前最接近的证据基础就是 Ihle 这篇第三方分析,数据主要来自 Epoch 的 Benchmarking Hub。
四、"针对性优化公开考卷"没有直接证据,只是推测。CAISI 原文没有指控 contamination 或针对性优化,只说两个基准是 held-out。它还复现了 DeepSeek 自报的 GPQA 成绩(90%),说明这一项没有虚高。Ihle 把"train to the test、过滤不彻底"列为可能解释,同时写明了反向混杂。至少有四种同样能解释这个模式的机制:
(a) 天花板压缩:饱和题本来就拉不开差距;
(b) 闭源一方接触过"私有"题,比如 OpenAI 资助并接触过 FrontierMath,ARC-AGI-2 半私有集也对 API 方暴露过,这会放大差距;
(c) 脚手架、token 预算、第三方推理服务降级(CAISI 自己承认它测的 SWE-bench 分数低于其他评测方);
(d) 赢家诅咒偏差。
五、CAISI 的利益位置和透明度。CAISI 是按 AI Action Plan 的指令评测 PRC 模型的机构;上一份 DeepSeek 报告(2025-09)发布时,商务部长 Lutnick 公开做了政治定调。PortBench 和 CTF-Archive-Diamond 是 CAISI 自建的非公开基准,V4 Pro 的网络安全分数还是用 IRT 插补出来的,完整方法文档尚未发布。正文里一处说 16 个基准、35 个模型,表里只列了 9 个基准,两者没有对上。成本对比只剩 GPT-5.4 mini 一个美国模型。Decrypt 的批评主要来自一位化名开发者,质量不高。但 Epoch 的独立复算削弱了"8 个月是政治产物"这一怀疑。
六、"2 个月"这一端只有 DeepSeek 自报,本质是厂商挑选的比较;独立评测给出 4–5 个月(AA)到 8.5 个月(Epoch)。所以"厂商自报 vs 独立评测相差数倍"这个说法,数字上站得住,但应写成"2 个月 vs 独立测量的 4–9 个月",不能只写 8 个月。
结论:"约 8 个月"可以升级为两源支持(CAISI 加我在 Epoch ECI 上的复算),"私有题差距大于公开题"也有 Ihle 和 Epoch 原始数据两个独立来源。但 AA 给出 4–5 个月,说明落后幅度取决于指数的构成;"差额来自针对公开考卷的优化"这一因果解释没有直接证据,还有至少四个同样合理的替代解释。整条承重结论判为"方向存争":数值部分升级,机制部分必须降级为推测。

**method_issues**:
- CAISI 私有基准(PortBench、CTF-Archive-Diamond)不可复现;V4 Pro 的网络安全分数是用 IRT 从部分样本插补的;完整方法文档尚未发布
- CAISI 原文自相矛盾:一处说 16 个基准、35 个模型,表格只列 9 个基准;'8 个月'怎么从趋势线算出来的没有给细节
- 利益位置:CAISI 执行 AI Action Plan 下'评测 PRC 前沿模型'的指令,2025 年那份报告发布时商务部长 Lutnick 公开做了政治定调;成本对比只留下 GPT-5.4 mini 一个美国模型
- '2 个月'不是独立测量,只是 DeepSeek 自报加 CAISI 的转述;拿它和独立测量比较,本身就是拿厂商挑选的比较当基线
- '8 个月'针对的是 DeepSeek V4 Pro 这一个模型;按 Epoch ECI,同期 Kimi K2.6 更强,所以推成'PRC 前沿落后 8 个月'是外推
- CAISI 自己承认它测的 SWE-bench 低于其他评测方(system prompt、脚手架、token 预算不同),说明独立评测的数字也依赖评测配置
- '私有题'的混杂:OpenAI 资助并接触过 FrontierMath,ARC-AGI-2 半私有集对 API 方有暴露。闭源一方可能见过题,会放大差距,这和'开源方针对公开题优化'是两回事
- 天花板效应:GPQA、AIME 类题接近满分,区分度低,持平可能只是饱和压缩,不一定是刷题
- Epoch ECI 和 CAISI 在 GPQA、OTIS、SWE-bench 上题目重叠,也都使用类 IRT 的聚合,两源并非完全独立
- Ihle 的分析里,数据点取舍由 Claude Opus 4.7 判定再加人工覆盖;存在赢家诅咒偏差;早期数据有自报成分
- Artificial Analysis 指数版本漂移:V4 Pro 在 v4.0 是 52 分,在 v4.1/4.1.1 是 44–45 分,跨版本不能比;GPT-5.2 的 v4.0 分数来自二手报道

**independent_measurements**:
- Epoch ECI 自算(https://epoch.ai/data/benchmark_data.zip,eci_scores.csv):DeepSeek-V4-Pro 2026-04-24 ECI 149.13(CI 147.31–150.72),约等于 GPT-5(2025-08-07,150.0)和 GPT-5.1(149.64),落后约 8.5 个月(CI 区间约 5–10 个月)。与 CAISI 的 8 个月、约等于 GPT-5 同向,高度一致
- Epoch ECI 自算:DeepSeek V4 Pro 0813(2026-08-13)ECI 155.31,约等于 GPT-5.2 Pro(2025-12,155.4)和 Opus 4.6(2026-02,155.24),落后约 6–8 个月。与 8 个月量级同向
- Epoch processed_data_for_eci.csv 分项:V4 Pro 在 GPQA 0.879(Opus 4.6 为 0.874)和 OTIS 0.967(Opus 4.6 为 0.944)上持平;FrontierMath T1–3 私有集 0.453(GPT-5 0.554、Opus 4.6 0.66、GPT-5.4 0.786),T4 私有集 0.024(GPT-5 0.22);WeirdML 0.489(GPT-5 0.607)。'公开饱和题持平、私有难题差距大'与 CAISI 同向
- Artificial Analysis(https://www.artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash):V4 Pro(Max)Index v4.0 得 52 分,同期 GPT-5.5 60、Opus/Gemini 3.1 Pro 57;GPT-5.2 xhigh(2025-12)约 50–51 分(二手:The Decoder、iThome)。隐含落后约 4–5 个月,介于 2 和 8 个月之间,部分矛盾
- Ihle, LessWrong 2026-05-28(https://www.lesswrong.com/posts/rJcCrXyEsJKmmDpWG/how-far-behind-are-open-models):17 个基准,开源模型在私有基准上落后 8–10 个月、公开基准上落后 4–6 个月。与'差额集中在私有题'同向;作者自承部分'私有'题并不完全私有,并有赢家诅咒偏差
- Epoch data insight(https://epoch.ai/data-insights/open-closed-eci-gap):2026 年以来最强开源权重模型平均落后 4 个月(ECI 差约 8 分)。针对的是开源前沿(Kimi K2.6),不是 DeepSeek V4 Pro,口径不同,提示'8 个月'不能外推为'中国/开源前沿'
- Epoch data insight(https://epoch.ai/data-insights/us-vs-china-eci):2023 年以来中国模型平均落后 7 个月(4–14 个月)。量级与 8 个月同向
- CAISI 原文(https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro):CAISI 复现了 DeepSeek 自报的 GPQA 90%,说明公开题自报没有虚高;原文没有任何关于针对性优化或污染的直接证据
- Stanford AI Index 2026(经 Decrypt 转引):公开 Arena 排行榜上中美差距 2.7%。测量对象不同(偏好 Elo),方向与'几乎追平'同向,但不能和月数直接对比

**search_angles**:
- NIST CAISI DeepSeek V4 Pro 评测原文(已读:方法、分项表、caveats)
- CAISI 方法批评(Decrypt;批评者主要是化名开发者 Ex0bit,质量低)
- CAISI 与 AI Action Plan、Lutnick 政治定调(找到 2025 年报告时的 Lutnick 表态)
- Epoch ECI 原始数据下载并自算 V4 Pro 与美国前沿的时间差(成功,结果约 8.5 个月)
- Epoch processed_data_for_eci.csv:V4 Pro 分项和数据来源(成功)
- Epoch 模型页 deepseek-v4-pro / v4-pro-0813(ECI 149 / 155)
- Epoch 'open-weight models perform worse on private benchmarks' 原话出处(没找到 Epoch 一手表述;最接近的是 Ihle 在 LessWrong 上基于 Epoch 数据的分析)
- Epoch data insight:开源与封闭 ECI 差距(2026 年平均 4 个月)、中美 ECI 差距(平均 7 个月)
- Artificial Analysis V4 Pro 发布文章和模型页(52 分 / 44–45 分,有版本漂移)
- Artificial Analysis Index v4.0 中 GPT-5.2 / Opus 4.5 / Gemini 3 Pro 的分数(只找到二手报道)
- Ihle 'How far behind are open models'(LessWrong,2026-05-28)
- UK AISI 对 DeepSeek V4 Pro 的评测(没搜到)
- Scale SEAL 排行榜上的 DeepSeek V4 Pro(没搜到)
- LMArena HF 数据集 lmarena-ai/leaderboard-dataset text/overall 中 DeepSeek V4 的评分(datasets-server 返回 504 或索引加载中,没取到数据)
- DeepSeek 自报与独立复现的对比(CAISI 复现了 GPQA 90%,说明这一项无虚高)
- 关于 DeepSeek 针对公开基准优化或污染的直接证据(没找到;只有 Ihle 的推测)
- BenchLM 对 V4 Pro 0813 给出的另一个 ECI 估计 141.37(第三方站点,口径不明,未采信)

## R4-caisi-8months · method → **降级为弱结论**

**可用表述**:对 DeepSeek V4 Pro(2026-04),两家独立评测的结论相近:Epoch 能力指数 149(95% CI 147–151)约等于 2025-08 的 GPT-5,落后美国前沿约 8.6 个月(按 CI 端点算是 5–10 个月);NIST CAISI 估计约 8 个月。DeepSeek 自称与约 2 个月前发布的 Opus 4.6、GPT-5.4 持平,不过这是"对标模型发布间隔",和前两者不是同一把尺子。分项上,在已接近饱和的公开题(GPQA、AIME、SWE-bench Verified)上,V4 Pro 与同代美国模型基本持平;在未公开或智能体、网络安全类题(PortBench、CTF、ARC-AGI-2 半私有集)上,它比 Opus 4.6 低约 15 个百分点,比 GPT-5.5 低 30 多个百分点。独立分析(Ihle 2026)同样发现开源模型在私有基准上的差距约是公开基准的两倍(8–10 个月 vs 4–6 个月)。这提示公开榜单可能高估了追赶速度。但这个差额也和题目饱和度、任务类型重合,"针对公开考卷做了优化"目前只是推测,还没有直接证据。

**理由**:这条论断拆成三部分,结论各不相同。

(A)"独立评测给出约 8 个月":可以升级为多源。我下载了 Epoch benchmark_data.zip 并复算(epoch_capabilities_index/eci_scores.csv,当前版本)。DeepSeek-V4-Pro(2026-04-24)的 ECI 为 149.13,CI 147.31–150.72。美国模型最早达到 ≥149.13 的是 GPT-5(150.0,2025-08-07;它也是 ECI 的锚点),滞后约 8.6 个月。拿 CI 端点做敏感性检验:下界 147.3 对应 o3-pro(2025-06-10),约 10.5 个月;上界 150.7 对应 Gemini 3 Pro(2025-11-18),约 5.2 个月。所以区间是 5–10.5 个月,2 个月落在区间之外。后续版本 V4 Pro 0813 的 ECI 为 155.3,约等于 GPT-5.2 Pro(2025-12),仍落后约 8 个月,说明换版本、换时点结论都稳定。Ihle(LessWrong,2026-05-28,17 个基准约 110 个数据点)按阈值穿越法独立估算:开源模型在私有基准上落后 8–10 个月,在公开基准上落后 4–6 个月。CAISI 的 8 个月和 Epoch 的 8.6 个月由不同机构用不同基准集算出,方向和量级一致,所以 CAISI 的利益冲突不足以推翻这个数字。不过有两点限制:ECI 本身也纳入了 FrontierMath 私有集、Chess Puzzles 等私有或半私有题,所以 Epoch 和 CAISI 在"含私有题"这一点上并不完全独立;Ihle 的数据也大量取自 Epoch hub。Artificial Analysis 的数据比较含糊:发布时 V4 Pro 为 52,GPT-5.5 为 60;旧版 v4.0 的 Opus 4.6 分数和它不同版本、不可直接比,只能说 AA 的结果介于两者之间,没有核实出确切的月数。

(B)"2 个月":这不是一个测出来的差距。CAISI 原文的意思是 DeepSeek 自称与 Opus 4.6、GPT-5.4 持平,而这两款发布约 2 个月。这是用"自称对标模型的发布时间"做的代理,口径与 8 个月不同。"相差数倍"这个对比可以写,但必须注明 2 个月是"自报对标模型的发布间隔",而不是同一指标算出的差距。

(C)"差额集中在私有/智能体题,公开追平部分来自针对性优化":
- 分项格局成立。CAISI 表里,V4 Pro 对 Opus 4.6:公开题 SWE-V -5、GPQA -1、FrontierScience +2、AIME +5、PUMaC +1、SMT +2,基本持平;私有或半私有题 CTF -14(而且这一项是 IRT 插补值)、PortBench -16、ARC-AGI-2 半私有 -17。
- 文章写的"30+pp"是对 GPT-5.5 的差距(CTF -39、PortBench -34、ARC -33)。GPT-5.5 并不是 2 个月口径下的对标模型,对标 Opus 4.6 时只差约 15pp,30+pp 有夸大。
- 我在 Epoch 数据里复现了同样的格局:V4 Pro 对 GPT-5.2,GPQA、AIME、DTBench、SWE-V 持平或略高,SimpleQA 还高 10pp;但 FrontierMath T1-3 私有 -22pp、T4 私有 -29pp、Chess -31pp。
- 问题在于"私有"和"未饱和、长程、智能体型"这几个属性高度共线。公开题大多已饱和(AIME、PUMaC、SMT 在 90–100%),天花板压缩会机械地缩小差距。WeirdML 是公开基准,但没有饱和,DS 对 GPT-5.2 落后 23pp。这说明题目难度和类型本身就能解释相当一部分差额,不一定要用"针对公开考卷优化"来解释。
- 我没有找到任何直接证据,证明 DeepSeek 对公开基准做了针对性训练或存在污染。CAISI 正文没有讨论污染,只称 PortBench 和 ARC 半私有集"held-out、uncontaminated";Ihle 明说过拟合只是从 public/private 差距反推出来的"suggestion";Epoch 2024 年的 open-models report 并没有任务描述里那句"open-weight models tend to perform worse on private benchmarks",它只给了 GSM1k 落后 6–10 个月这一个私有题例子。那句话的出处没有找到,不能当作 Epoch 的自述来引用。

(D)CAISI 的方法透明度:PortBench 是 CAISI 自建、不公开;CTF-Archive-Diamond 上 V4 的分数是插补的;ARC-AGI-2 半私有集已对部分第三方暴露;用的是 1PL IRT,域内、域间等权,这个权重选择会直接决定结论;正文说"9 个基准",图 1 又写"16 个基准、35 个模型",两者对不上;8 个月具体怎么从趋势线算出来没有披露,详细方法说明只说"稍后发布";SWE-V 的分数也系统性偏低。利益位置方面,NIST 页面本身没提 AI Action Plan 或商务部长,但 CAISI 的使命设定(评估对手国 AI)属于结构性立场,需要在文中注明。DeepSeek 的自报同样有利益冲突,所以两边都不是中立来源。好在 Epoch 的独立复算对上了量级,削弱了"8 个月是政治数字"的疑虑。

总评:"独立口径约 8 个月、厂商口径约 2 个月"可以承重,但要讲清两者口径不同。"差额集中在私有/智能体题"可以作为观察来写,但要标明与饱和度、题型混杂,而且 30+pp 要改成对 Opus 4.6 约 15pp。"公开追平来自针对性优化"只是推测,没有直接证据,不能承重。整句按原文表述降级。

**method_issues**:
- '2 个月 vs 8 个月'口径不同:2 个月是 DeepSeek 自称对标模型(Opus 4.6/GPT-5.4)的发布间隔,8 个月是 IRT 综合分配合前沿趋势线的估算,两者并非同一指标下的'相差数倍'
- '私有题差 30+pp'取自对 GPT-5.5 的比较;对 2 个月口径下的对标模型 Opus 4.6,私有题差距约 14–17pp,有夸大
- 混杂:CAISI 的私有题同时是智能体/网络安全/长程题且未饱和,公开题多已饱和(AIME/PUMaC/SMT 90–100%),天花板压缩会机械缩小差距;'私有性'的效应无法与'题型/难度'分离。Epoch 数据中公开但未饱和的 WeirdML 同样差 23pp
- '针对性优化公开考卷'没有直接证据(没有污染检测、改写题对照或 held-out 同分布对照),CAISI 正文未讨论污染,Ihle 自述只是推测
- CAISI 方法透明度不足:PortBench 自建且不公开、不可复现;CTF-Archive-Diamond 上 V4 的分数为 IRT 插补值;ARC-AGI-2 半私有集已部分暴露;正文 9 个基准与图 1 的 16 个基准/35 个模型对不上;8 个月的具体计算未披露,详细方法说明'稍后发布';SWE-V 分数系统性偏低(脚手架/预算差异)
- IRT 1PL 加域内、域间等权是关键的建模选择:5 个域等权会放大网络安全(仅 CTF+PortBench)的权重,换权重结论可能移动,而 CAISI 未给出敏感性分析
- 利益冲突:CAISI 的使命是评估对手国 AI(结构性立场),NIST 页面本身未提 Action Plan;DeepSeek 自报同样有利益冲突。好在 Epoch 的独立复算量级一致,削弱了'政治数字'的疑虑
- Epoch ECI 也纳入私有题(FrontierMath 私有集、Chess Puzzles、Mystery Game),与 CAISI 在'含私有题'上不完全独立;Ihle 的数据也主要来自 Epoch hub,三个来源存在共同数据依赖
- 数据版本漂移:ECI 随新模型加入会重新拟合,V4 Pro 发布时的排名(24/212)与现在(52/249)不同;本次复算基于 2026-10 版本

**independent_measurements**:
- Epoch ECI 自算(https://epoch.ai/data/benchmark_data.zip, eci_scores.csv 当前版本):DeepSeek-V4-Pro 149.13 [147.31,150.72] @2026-04-24;首个达到的美国模型是 GPT-5 150.0 @2025-08-07,约 8.6 个月;CI 敏感性 5.2–10.5 个月。与 CAISI 的 8 个月同向,与'2 个月'反向
- Epoch ECI 0813 版本:V4 Pro 0813 155.31,约等于 GPT-5.2 Pro 155.4 @2025-12-11,约 8 个月。差距稳定,同向 8 个月
- Epoch processed_data_for_eci.csv 分项:V4 Pro 对 GPT-5.2,GPQA -0.7pp、AIME +0.6、SWE-V +3.9、SimpleQA +9.9;FrontierMath T1-3 私有 -22、T4 私有 -29、Chess -31、WeirdML(公开,未饱和)-23。'饱和公开题持平、私有/难题大差'这一格局同向,但 WeirdML 显示公开的未饱和题同样差距大
- Ihle, LessWrong 2026-05-28 https://www.lesswrong.com/posts/rJcCrXyEsJKmmDpWG/how-far-behind-are-open-models:开源整体在私有基准上落后 8–10 个月,公开基准 4–6 个月。针对开源整体而非 V4 Pro 单模型;数据大量来自 Epoch,并非完全独立;作者明说过拟合是推测
- Artificial Analysis(https://www.artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash):发布时 V4 Pro 52,GPT-5.5 约 60。与 Opus 4.6 的分数指数版本不一致,无法换算成月数,方向不定
- NIST CAISI https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro:IRT Elo V4 Pro 800±28,GPT-5.4 mini 749,Opus 4.6 999,GPT-5.5 1260。'2 个月'来自 DeepSeek 自称对标模型的发布时间
- Epoch open-models report(2024-11-04)https://epoch.ai/blog/open-models-report:未找到'open-weight models tend to perform worse on private benchmarks'原句;只有私有 GSM1k 上开源落后 6–10 个月一例,不能当作 2026 年的 Epoch 自述

**search_angles**:
- NIST CAISI DeepSeek V4 Pro 原文:基准清单、IRT、per-benchmark 表、'2 个月'的口径(已核)
- Decrypt 等媒体对 CAISI 方法的批评(已核:私有不可复现、IRT 相对分、成本对比只保留 GPT-5.4 mini)
- 下载 Epoch benchmark_data.zip 复算 V4 Pro 的 ECI 月差及 CI 敏感性(已做)
- Epoch 分项:V4 Pro 对 GPT-5、GPT-5.2、Gemini 3 Pro、GPT-5.5、o3,按公开/私有拆开(已做)
- V4 Pro 0813 版本的 ECI 月差,检验版本稳定性(已做)
- Epoch 原句'open-weight models tend to perform worse on private benchmarks'的出处(没找到原句;2024 报告无此表述)
- Ihle LessWrong 关于开源模型私有/公开差距的分析(已核,过拟合属推测)
- Artificial Analysis 上 V4 Pro 对 Opus 4.6/GPT-5 的指数(只找到 52 对 GPT-5.5 约 60;版本不一,未能换算月数)
- UK AISI、Scale SEAL 对 DeepSeek V4 Pro 的独立评测(未搜到公开数值)
- DeepSeek V4 污染、针对公开基准训练的直接证据(未搜到)
- LMArena HF 数据集与 METR 时间视界数据(本论断未用到,未下载)
