# BENCH-static-index — 静态基准饱和时序 + Stanford AI Index 统计

截至 2026-10-12 调研(进行中,边查边写)。

## A. Stanford AI Index 2025(一手 PDF 已下载核对)

PDF: https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf (2025-04)

- A1 Arena 第1 vs 第10 名:11.9% → 5.4%(Elo 分差占比,基于 Chatbot Arena)。原文:"the Elo score difference between the top and 10th-ranked model on the Chatbot Arena Leaderboard was 11.9%. By early 2025, this gap had narrowed to just 5.4%."
- A2 前两名:"the difference between the top two models shrank from 4.9% in 2023 to just 0.7% in 2024"(同段,Arena Elo 口径)。
- A3 开源 vs 闭源(Arena):"In early January 2024, the leading closed-weight model outperformed the top open-weight model by 8.04% on the Chatbot Arena Leaderboard. By February 2025, this gap had narrowed to 1.70%."
- A4 中美(基准口径,非 Arena):"At the end of 2023, performance gaps on benchmarks such as MMLU, MMMU, MATH, and HumanEval were 17.5, 13.5, 24.3, and 31.6 percentage points, respectively. By the end of 2024, these differences had narrowed substantially to just 0.3, 8.1, 1.6, and 3.7 percentage points."
- 口径注:"%" 是 Elo 分差 / Elo 分值,Elo 是相对尺度(加常数不变),用百分比表达几乎无意义;1.7% 约 ≈ 20-25 Elo。

## B. Stanford AI Index 2026(第2章 PDF 已下载核对)

PDF: https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_2_technical.pdf (2026-04)

- B1 开源差距重新打开:"The open model performance gap reopened in 2025 after briefly closing in 2024. As of March 2026, the top closed model leads the top open model by 3.3%, up from 0.5% in August 2024. Six of the top ten models on the Arena Leaderboard are now closed."
  - 正文却写 3.4%:"As of March 2026, the top closed-weight model, Claude Opus 4.6 (1,503), led the top open-weight model GLM‑5 (1,454) by 49 points (3.4%)."(报告内部 3.3 vs 3.4 不一致;49/1454=3.37%)
  - 2023-05:"GPT‑4‑0314 outperformed the top open-weight model (Vicuna‑13B) by 174 points (15.2%)";2024-08:"narrowed the gap to just 7 points (0.5%)"。
- B2 头部聚拢:"Top model performance is converging, with 4 companies now clustered within 25 Elo points ... As of March 2026, Anthropic (1,503), xAI (1,495), Google (1,494), OpenAI (1,481), Alibaba (1,449), and DeepSeek (1,424)"
- B3 Text Arena top15:"the top 15 models spanning roughly 46 points ... confidence intervals overlap for many models"
- B4 中美:"the top U.S. model (Claude Opus 4.6, 1,503) led the top Chinese model (Dola‑Seed‑2.0 Preview, 1,464) by 39 points (2.7%)";2025-02 DeepSeek-R1 落后 5 分(0.4%)。
- B5 饱和:"Evaluations intended to be challenging for years are saturated in months"
- B6 HLE:"In a single year, accuracy went from under 10% to 38.3%."
- B7 MMLU-Pro:"leading 15 models all scoring above 87% ... The overall spread between the top-ranked and 15th-ranked model is just over 4 percentage points";MMLU 上 GPT-4o vs GPT-4-Turbo 差 1%,MMLU-Pro 上 9%(饱和基准压缩分差的直接例证)。
- B8 GPQA Diamond:"In late 2024, OpenAI’s o3 was the first to exceed it with a score of 87.7%. In 2025, mean accuracy reached 93%"(人类专家基线 81.2%)。
- B9 ARC-AGI-2(2026-02 榜):"the spread between the highest and lowest scores in the figure is about 46% ... Gemini 3 Deep Think leads at 84.6%, followed by Gemini 3.1 Pro Preview at 77.1% and GPT-5.2 (Refine.) at 72.9%"——未饱和基准上 top15 分布宽得多。
- B10 SWE-bench Verified:"top models are tightly clustered in the low-to-mid 70s ... Claude 4.5 Opus (high reasoning) led at approximately 76.8%"(mini-SWE-agent-v2 统一脚手架)。
- B11 FrontierMath T4:"risen from near 0% to 31.3%, with GPT-5.2 Pro (Web App) leading by the end of 2025"
- B12 专业领域:"The performance of the top 15 models is separated by as little as 3 percentage points in each benchmark."
- B13 基准可靠性:"invalid question rates ranging from 2% on MMLU Math to 42% on GSM8K";Arena 排名"may partly reflect adaptation to the platform"。
- B14 Terminal-Bench 2.0:"increasing from 20% in February 2025 to 77.3% in early 2026"

## C. OpenAI 弃用 SWE-bench Verified(2026-02-23)
- 一手 https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (curl/WebFetch 均 403,未能逐字核)。
- 媒体转述(decrypt):审计 "138 tasks that GPT-5.2 consistently failed across 64 independent runs" → "59.4% of those tasks are broken";GPT-5.2/Claude Opus 4.5/Gemini 3 Flash 可凭记忆复现原修复;建议改报 SWE-bench Pro。
- 口径问题:The Decoder 写成 "at least 59.4 percent of the benchmark's tasks are flawed"——是 138 道最难题子集的 59.4%,不是全集。

## D. Epoch Benchmarking Hub 原始数据自算(下载 https://epoch.ai/data/benchmark_data.zip,引用版本 2026-10)
方法:eci_scores.csv 给每模型 ECI、90% CI、Accessibility group(Open/Closed weights)、国家;processed_data_for_eci.csv 为扣随机基线后归一化分数(核对:HLE 原始 54.8% → (0.548-0.048)/0.952=52.5%)。各基准 CSV 有 Epoch 自跑分数+stderr。

### D1 ECI 开源 vs 闭源前沿(自算,"截至 t 已发布模型"的最佳)
| 时点 | 最佳闭源 | 最佳开源 | ECI 差 |
|---|---|---|---|
| 2024-07 | Claude 3.5 Sonnet 130.0 | Qwen2-72B 125.3 | 4.7 |
| 2025-04 | Gemini 2.5 Pro 144.2 | DeepSeek-R1 139.0 | 5.2 |
| 2025-10 | GPT-5 150.0 | DeepSeek-V3.2-Exp 145.0 | 5.0 |
| 2026-01 | GPT-5.2 Pro 155.4 | DeepSeek-V3.2 146.3 | 9.1 |
| 2026-04 | GPT-5.4 Pro 158.9 | Kimi K2.5 148.0 | 10.9 |
| 2026-07 | GPT-5.5 Pro 162.1 | GLM-5.2 151.8 | 10.3 |
| 2026-10-12 | Claude Opus 5.5 167.3 (CI 164.1-171.7) | Kimi K3 157.5 (CI 155.2-160.0) | 9.9(CI 不重叠) |
- 开源"新纪录"发布时的追平月数(开源模型发布日 − 首个达到同 ECI 的闭源模型发布日):2025 年 1.1–5.5 月;2026 年 Kimi K2.5 5.7、GLM-5.1 8.0、Kimi K2.6 5.0、GLM-5.2 6.9、Kimi K3 4.4 月。发布时 ECI 差 2026 年 4.6–10.3。
- 中美(ECI,自算):2025-04 5.2 → 2026-10 9.9(最佳中国模型 Kimi K3);与 AI Index 2026 用 Arena 得出的"2.7% 实际已闭合"方向不同。
- 对照 Epoch 官方 2026-05-29 Data Insight:"Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of four months";"The average ECI gap was 8 points, similar to the gap between GPT-5 and GPT-5.5."(https://epoch.ai/data-insights/open-closed-eci-gap)

### D2 同一批模型(2025-10-12 至 2026-10-12 发布)在饱和 vs 未饱和基准上的分差(Epoch 自跑原始分)
| 基准 | 最佳闭源 | 最佳开源 | 分差 pp | 状态 |
|---|---|---|---|---|
| OTIS Mock AIME 24-25 | 100(多个) | 98.6 DeepSeek V4 Pro 0813 | ~1.4 | 饱和 |
| GPQA Diamond | 95.8±1.4 GPT-6 Astra | 93.1±1.5 Kimi K3 | 2.7 | 饱和 |
| SWE-bench Verified | 83.5±1.7 Opus 4.7 (2026-04) | 78.7±1.9 GLM-5.2 | 4.8 | 饱和/被弃用(Epoch 未跑 2026-07 后新模型) |
| FrontierMath T1-3 v2 | 93.7±1.4 GPT-6.1 Sol | 72.2 Kimi K3 | 21.5 | 头部近饱和 |
| SimpleQA Verified | 75.6±1.4 GPT-6 Astra | 52.9 DeepSeek V4 Pro 0813 | 22.7 | 未饱和 |
| ARC-AGI-2 | 95.0 GPT-6 Astra | 61.4 DeepSeek V4 Flash 0731 | 33.6 | 头部近饱和 |
| FrontierMath T4 v2 (41 题) | 100 GPT-6.1 Sol;97.6±2.4 GPT-6 Astra | 39.0 Kimi K3 | ~61 | 头部近饱和 |
| HLE (external) | 54.8±1.9 GPT-6 Astra | 24.4 Kimi K2.5(Epoch 无更新开源条目) | 30(覆盖不全) | 未饱和 |
- top1 − top10(同一年 cohort,归一化分):GPQA 2.4pp、ARC-AGI-1 2.0、OTIS AIME 0.0、SWE-V 6.8 vs FM-T4v2 26.8、HLE 21.4、Terminal-Bench 21.6、Mystery Game Puzzles 35.3、Remote Labor Index 19.6。
- 解读注意:pp 分差受 S 曲线位置支配——基准在陡峭段时同样的"落后 N 月"会表现为很大的 pp 差;饱和段则压成 ~0。FM-T4v2/ARC-AGI-2 上 30–60pp 的差距主要是头部在 2026 年中快速冲顶、开源停在 40-60% 段。

### D3 饱和时序(Epoch 数据,归一化后首个达阈值模型的发布日)
| 基准 | 发布 | ≥50% | ≥80% | ≥90% | 当前最高(归一化) |
|---|---|---|---|---|---|
| GPQA Diamond | 2023-11 | 2024-12 | 2025-06 | 2025-11 | 94.4 |
| MATH L5 | 2021-03 | 2024-05 | 2024-09 | 2024-12 | 98.1 |
| OTIS Mock AIME | 2024-12 | 2024-12 | 2025-04 | 2025-08 | 100 |
| SWE-bench Verified | 2024-08 | 2025-02 | 2026-04 | – | 83.5 |
| ARC-AGI-1 | 2019-11 | 2025-04 | 2025-11 | 2025-12 | 98.5 |
| ARC-AGI-2 | 2025-03 | 2025-12 | 2026-03 | 2026-07 | 95.0 |
| Terminal-Bench | 2025-05 | 2025-11 | 2026-02 | – | 84.7 |
| FrontierMath T1-3 v2 | (v2 2026-06) | 2025-08 | 2026-03 | 2026-09 | 93.7 |
| FrontierMath T4 v2 | (v2 2026-06) | 2026-03 | 2026-06 | 2026-06 | 100 |
| HLE | 2025-01 | 2026-09 | – | – | 52.5 |
| OSWorld 2.0 | 2026-06 | – | – | – | 31.4 |
| Remote Labor Index | 2025-10 | – | – | – | 20.8 |
| GDPval(Epoch 收录) | 2025-09 | – | – | – | 49.7 |
- 从发布到 ≥80%:GPQA ~19 月;ARC-AGI-2 ~12 月;Terminal-Bench ~9 月;SWE-V ~20 月;HLE 20 月仍 ~52%。

### D4 ECI 方法论(一手)
- https://epoch.ai/data/eci-documentation/methodology:"performance(m,b) = σ(α_b [C_m − D_b])";"Higher α_b values correspond to “steeper” benchmarks ... These benchmarks tend to saturate quickly";"We report 90% bootstrap confidence intervals"。
- https://epoch.ai/benchmarks/eci:"When scores are near 0% and 100%, benchmarks aren't very good at telling which model is more capable.";"giving more weight to the benchmarks that carry the most signal";锚定 "Claude 3.5 Sonnet = 130 and GPT-5 = 150";"there is no maximum achievable ECI"。
- 饱和处理是隐式的(logistic 在 0/100% 处梯度趋零,信息量低),未见显式降权/剔除规则;benchmark_metadata.csv 有 random_baseline、score_ceiling、superseded_by(如 FrontierMath 旧版被 v2 取代)字段。
- 论文:Ho et al., "A Rosetta Stone for AI Benchmarks", arXiv:2512.00193 (2025-11-28):"Most AI benchmarks saturate within years or even months after they are introduced."

### D5 同一基准上闭源−开源分差的时序:倒 U 形(自算,Epoch processed 归一化分;"截至该日已发布模型"中两组最佳之差,pp)
| 基准 | 24-07 | 25-01 | 25-07 | 26-01 | 26-04 | 26-07 | 26-10 |
|---|---|---|---|---|---|---|---|
| GPQA Diamond | 17.7 | 27.0 | 12.0 | 11.2 | 9.0 | 3.7 | 3.5 |
| OTIS Mock AIME | 2.5 | 57.6 | 17.8 | 7.2 | 5.6 | 3.3 | 1.4 |
| ARC-AGI-1 | – | – | 39.6 | 33.5 | 32.7 | 21.5 | 4.0 |
| ARC-AGI-2 | – | – | 7.3 | 50.1 | 71.5 | 66.4 | 33.6 |
| FrontierMath T1-3 v2 | – | – | – | – | 51.2 | 28.5 | 21.5 |
| FrontierMath T4 v2 | – | – | – | – | – | 60.9 | 61.0 |
| Terminal-Bench | – | – | – | 29.9 | 29.4 | 32.3 | 32.3 |
| SimpleQA Verified | – | – | – | 26.4 | 33.1 | 26.5 | 22.7 |
| Chess Puzzles | 1.1 | 10.6 | 34.7 | 30.5 | 40.6 | 40.0 | 26.3 |
| DeepSWE | – | – | – | – | – | 26.1 | 5.6 |
- 规律:分差在基准"起飞段"放大(闭源先爬坡),在闭源触顶后被天花板压缩(ARC-AGI-1 39.6→4.0;AIME 57.6→1.4;GPQA 27→3.5)。"饱和基准上的小分差"大部分是天花板压缩,不是追赶者真追平同等能力。
- 反例:未饱和基准上也有小分差——DeepSWE(头部 74%)Δ5.6、FrontierCode(头部 55%)Δ10.5、PostTrainBench Δ9.8、CL-bench Δ8.6(D2 cohort 表)。即"未饱和→大分差"不是普遍定律。
- 口径:用模型发布日排时间;Epoch 评测时间可能晚于发布;开源样本覆盖不均(如 HLE 开源最新条目仅到 Kimi K2.5;Terminal-Bench 开源最佳停在 52%)。

## E. ARC-AGI 官方榜单原始 JSON(https://arcprize.org/media/data/leaderboard/v1|v2|v3.json,generatedAt 2026-10-05)
- ARC-AGI-1 (Semi-Private):多家并列 98.5%(Claude Fable 5、GPT-6 Astra、Claude Opus 5.5、Gemini 3.8 Flash、GPT-6.1 Sol),Human Panel 98%;最佳开源 Kimi K3 94.5、DeepSeek V4.1 Flash 94.5。→ 完全饱和、超人类面板。
- ARC-AGI-2 (Semi-Private):GPT-6 Astra (Max) 95.0%、GPT-6.1 Sol 94.2、Claude Opus 5.5 93.3;Human Panel 100%;最佳开源 DeepSeek V4.1 Flash (Max) 72.9%(差 ~22pp)。ARC-AGI-2 2025-03 发布,头部 18 个月到 ~95%。
- ARC-AGI-3(2026-03-25 发布的交互式环境):纯模型(非 adapter)GPT-6 Astra (Max) 62.7%、GPT-6.1 Sol (Max) 52.7、Claude Opus 5 (High) 30.2、Gemini 3.8 Flash (High) 10.4、Grok 4.7 1.8;2026 上半年 GPT-5.4 0.21%、Gemini 3.1 Pro 0.42%、GPT-5.5 0.43%。"Provider Adapter harness" 条目 GPT-6 Astra 99.95%、GPT-6.1 Sol 96.4%(脚手架口径,不可与纯模型比)。榜单无开源模型条目。→ 在最新未饱和基准上,头部之间也高度分化(62.7 vs 30.2 vs 10.4 vs 1.8)。
- 媒体(decrypt 2026-03)报 ARC-AGI-3 发布时 Gemini 3.1 Pro 0.37%、GPT-5.4 0.26%、Opus 4.6 0.25%,人类 100%。

## F. 基准原始论文:发布时的分数(一手 arXiv)
- MMLU(arXiv 2009.03300, 2020-09-07):"the very largest GPT-3 model improves over random chance by almost 20 percentage points on average"。
- GPQA(arXiv 2311.12022, 2023-11-20):"experts ... reach 65% accuracy (74% when discounting clear mistakes ...)";"our strongest GPT-4 based baseline achieving 39% accuracy"。
- FrontierMath(arXiv 2411.04872, 2024-11-07):"Current state-of-the-art AI models solve under 2% of problems"。
- HLE(arXiv 2501.14249, 2025-01-24):"LLMs now achieve over 90% accuracy on popular benchmarks like MMLU";发布时 SOTA 8.80%(AI Index 2025 原文 "the top system scores just 8.80%")。
- AI Index 2025:"The saturation of traditional AI benchmarks like MMLU, GSM8K, and HumanEval ... Humanity’s Last Exam ... top system scores just 8.80%; FrontierMath ... solve only 2% of problems"。

## G. 厂商头条基准迁移(一手发布页)
- Claude 3(2024-03-04,anthropic.com/news/claude-3-family):正文点名 "MMLU", "GPQA", "GSM8K"。
- Claude Opus 4.5(2025-11-24):"state-of-the-art on tests of real-world software engineering"(SWE-bench),表下列 SWE-bench Multilingual, Aider Polyglot, BrowseComp-Plus, Vending-Bench;无 MMLU/GPQA。
- Claude Opus 5.5(2026-09-22,anthropic.com/news/claude-opus-5-5):表格 Terminal-Bench 4.0 66.4%、FrontierCode v1.1 54.4%、CursorBench 4.0、GDPval-AA v2.1 1846、AutomationBench 40.0%、HLE 67.7% with tools、Terminal-Bench-Science、OSWorld 2.1、Chartography;MMLU/GPQA/SWE-bench Verified/AIME 均不出现。(厂商口径)
- OpenAI 2026-02-23 弃 SWE-bench Verified 改推 SWE-bench Pro(见 C)。
- Artificial Analysis Intelligence Index 版本史(https://artificialanalysis.ai/methodology/intelligence-benchmarking):v2.1(2025-08)"Removed MATH-500","Removed AIME 2024";v4.0(2026-01)"Removed MMLU-Pro, LiveCodeBench, AIME 2025 from Intelligence Index",新增 GDPval-AA/AA-Omniscience/CritPt;v4.2(2026-09)"Removed GPQA Diamond from the Intelligence Index";v4.1 "Adjusted category weights to further emphasize agentic tasks: Agents (34%)…";v4.3.2 现 10 项:AA-Briefcase, GDPval-AA, AutomationBench-AA, Terminal-Bench 4.0, SciCode, AA-LCR, AA-Omniscience, HLE, GDP.pdf, CritPt。注:版本史未写明"因饱和"移除。

### D6 ECI 年增速(自算,"截至日已发布"最佳)
| 窗口 | 闭源前沿 ΔECI | 开源前沿 ΔECI |
|---|---|---|
| 2023-10→2024-10 | +9.9 | +11.9 |
| 2024-10→2025-10 | +14.5 | +16.0 |
| 2025-10→2026-10 | +17.1 | +12.4 |
- 最近一年闭源前沿加速、开源前沿增速放缓 → ECI 分差由 ~5 扩到 ~10;按 2026 年闭源年增 ~17 点换算,10 点 ≈ 7 个月进度(与追平月数 4.4–8 月一致)。

## H. 其他测量质量证据
- MMLU 标签错误(arXiv 2406.04127, 2024-06-06):"We estimate that 6.49% of MMLU questions contain errors";Virology "57% of the analysed questions ... contain errors"。→ MMLU 顶分 ~90% 已贴近噪声天花板。
- HLE 标签争议(FutureHouse 2025-07-23,https://www.futurehouse.org/research/hle-exam,从业者/研究机构博客):文本类化学/生物题约 29±3.7% 答案与文献冲突;HLE 团队复核子集约 18% 有问题。→ 未饱和基准也有天花板<100%。
- 基准饱和系统研究(arXiv 2602.16763, 2026-02-18,ICML 2026):"nearly half of our benchmarks exhibit saturation, with rates increasing with age";"resilience to saturation is impacted by expert-curation, not by public test data"。
- "Benchmark Ceiling"(arXiv 2607.01254, 2026-06):"discriminating signal concentrates in the hardest benchmark items"。
- Scale SWE-bench Pro 公开集榜(labs.scale.com,未标更新日,条目停在 Muse Spark 1.1/GPT-5.4 时代):第1 Muse Spark 1.1 61.50±3.10,GPT-5.4 59.10±3.56;CI ±3.6 → 相邻名次多数统计不可分;开源最佳 qwen3-coder-480b 38.70±3.55(且开源条目陈旧)。

## I. 口径问题清单
1. AI Index 的 "%" = Elo 分差 / Elo 绝对值;Elo 可平移,百分比不具尺度意义;1.7%/3.3% 应回写为 ~20/49 Elo 点。
2. AI Index 2026 报告内部 3.3%(highlights)vs 3.4%(正文 49 点)不一致。
3. AI Index 中美差距 2025 版是基准 pp(MMLU 等),2026 版换成 Arena Elo——口径切换使"差距闭合"的时间序列不可直接衔接;Epoch ECI 自算同期中美差 ~9.9 点,方向相反。
4. GPQA 人类基线:原论文专家 65%(剔除明显错误后 74%),AI Index 2026 用 "expert human validator baseline of 81.2%"。
5. AI Index 2026 "SWE-bench Verified ... close to 100% in 2025" 是相对人类基线缩放值,不是原始解题率(原始 ~77-80%)。
6. OpenAI SWE-V 审计 59.4% 是"138 道 GPT-5.2 稳定失败题"子集的比例,媒体误写为全集比例。
7. ARC-AGI-3 "Provider Adapter harness" 分数(99.95%)与纯模型分数(62.7%)混在同一榜单;厂商宣传 99.9% 为脚手架口径。
8. HLE:无工具(Epoch external 54.8%)vs with tools(Anthropic 67.7%, 厂商口径)不可比。
9. Epoch processed 分数已扣随机基线归一化,与原始准确率不同(HLE 54.8→52.5)。
10. pp 分差强烈依赖基准在 S 曲线上的位置:同等时间滞后在起飞段显示为大 pp 差、在饱和段显示为近零差。
