# HORIZON-longtask — 长任务与可靠性(截至 2026-10)

## 自算数据(METR 一手数据)
- 来源: https://metr.org/assets/benchmark_results_1_1.yaml (下载于 2026-10-12); runs.jsonl TH1.0/TH1.1 自 https://github.com/METR/eval-analysis-public (最后同步 2026-03-06)
- 方法: 每模型对 log2(human_minutes) 做加权(invsqrt_task_weight)logistic 回归, p50/p80 = 成功率 50%/80% 对应的人类时长。自拟合在 TH1.1 上与 METR 公布值逐一吻合(GPT-5 202.9 vs 203.0;Opus 4.6 720.2 vs 718.8),故对 TH1.0 中开源模型的自拟合可信。
- METR time-horizons 页面: 最后更新 2026-09-08,"This page is no longer actively updated";"Measurements above 16 hrs are unreliable with our current task suite."

### TH1.1 官方 YAML(分钟,p50 [95%CI] / p80 / p50:p80 比)
| 发布 | 模型 | p50 | p80 | 比 |
|---|---|---|---|---|
| 2025-04-16 | o3 | 119.7 [74.6,190.9] | 30.0 | 4.0 |
| 2025-08-07 | GPT-5 | 203.0 [112.6,405.6] | 38.3 | 5.3 |
| 2025-11-18 | Gemini 3 Pro | 224.3 [139.6,379.2] | 54.1 | 4.1 |
| 2025-11-19 | GPT-5.1-Codex-Max | 223.7 | 50.6 | 4.4 |
| 2025-11-24 | Claude Opus 4.5 | 293.0 [161.7,623.7] | 49.4 | 5.9 |
| 2025-12-11 | GPT-5.2 | 352.2 [198.1,815.2] | 66.0 | 5.3 |
| 2026-02-05 | Claude Opus 4.6 | 718.8 [316.7,3633.8] | 69.9 | 10.3 |
| 2026-02-05 | GPT-5.3-Codex | 349.5 | 54.7 | 6.4 |
| 2026-02-19 | Gemini 3.1 Pro | 384.1 [233.5,694.8] | 89.8 | 4.3 |
| 2026-03-05 | GPT-5.4 | 341.7 [186.6,768.8] | 53.9 | 6.3 |
| 2026-04-07 | Claude Mythos Preview (early) | 1044.8 [508.9,3304.3] | 185.9 [97.3,398.5] | 5.6 |
doubling_time (from 2023 on, excludes p50>16h): 128.7 天 [104.4,158.0]

### TH1.0 自拟合: 开源/中国模型 vs 闭源前沿包络
| 开源 | 发布 | p50 | 闭源包络首次达到该水平的滞后(月) | 发布时闭源最佳/开源 比值 |
|---|---|---|---|---|
| Qwen2-72B | 2024-06 | 2.5 | 14.8 | 4.1x |
| Qwen2.5-72B | 2024-09 | 5.8 | 18.2 | 4.0x |
| DeepSeek-V3 | 2024-12 | 19.8 | 6.2 | 2.1x |
| DeepSeek-R1 | 2025-01 | 27.9 | 3.4 | 1.5x |
| DeepSeek-V3-0324 | 2025-03 | 24.6 | 6.1 | 2.2x |
| DeepSeek-R1-0528 | 2025-05 | 32.7 | 6.8 | 2.8x |
| gpt-oss-120b | 2025-08 | 45.1 | 7.2 | 2.4x |
| Kimi K2 Thinking | 2025-11 | 57.6 | 8.2 | 2.3x |
滞后方法: 闭源 running-max 包络,相邻点之间按 log(p50) 线性插值求首次达到时刻。

### 自算: 闭源"第二家实验室"差距(TH1.1 官方 YAML, p50 分钟)
- 2025-08: GPT-5 203 vs Opus 4.1 100 → 2.0x(OpenAI 领先)
- 2025-11/12: GPT-5.2 352 vs Opus 4.5 293 vs Gemini 3 Pro 224 → 1.2–1.6x
- 2026-02/03: Opus 4.6 719 vs Gemini 3.1 Pro 384 / GPT-5.3-Codex 350 / GPT-5.4 342 → 1.9–2.1x(但 Opus 4.6 CI 上限 3634,极宽)
- 2026-04: Mythos Preview(early) 1045 vs 次佳非 Anthropic 384 → 2.7x;p80 186 vs 90 → 2.1x
- 结论:领先者轮换(leapfrog),比值在 1.2x–2.7x 间摆动,无单调收窄;且 CI 大面积重叠。

### p50/p80 比值(可靠性是否追上能力)
- TH1.1: GPT-4 4.5, Claude 3.5 Sonnet(New) 7.9, o3 4.0, GPT-5 5.3, Gemini 3 Pro 4.1, Opus 4.5 5.9, GPT-5.2 5.3, Opus 4.6 10.3, Gemini 3.1 Pro 4.3, GPT-5.4 6.3, Mythos 5.6 → 无改善趋势,比值大致恒定 4–6x(离群 Opus 4.6=10.3)。
- 一手: METR Frontier Risk Report(2026-05-19): 最强 shared 模型 p50 16–20h, p80 3–4h → 比值约 5x。

## 一手引文摘录
1. METR time-horizons 页(LAST UPDATED 2026-09-08): "This page is no longer actively updated." / "Measurements above 16 hrs are unreliable with our current task suite." / "Due to our limited capacity, some models were measured long after release and others were skipped entirely."
   更新日志: "May 8th, 2026: Added Claude Mythos Preview (early)…"; 开源最后一次添加: "November 19th, 2025: Added GPT-5.1-Codex-Max and Kimi K2 Thinking." → TH1.1 无任何开源模型。
2. METR note 2026-03-20 (Alexander Barry): "As METR's time horizon task suite saturates, the results are becoming more sensitive to analysis choices." 正则化修正 "decreased recent models' 50% time horizon results by up to 20%"; "which tasks are included has a very large impact on the results"; "reasonable choices generally still leave us inside the CIs (which are very wide!)."
3. Kwa et al. 2025 (arXiv 2503.14499): "frontier AI time horizon has been doubling approximately every seven months since 2019"; Claude 3.7 Sonnet "50% time horizon of around 50 minutes".
4. TH1.1 YAML: doubling_time from_2023_on 128.7 天 [104.4,158.0](排除 p50>16h 的点)。
5. METR Frontier Risk Report 2026-05-19: "the 50% time horizon point estimate of the most capable shared model was between 16 and 20 hours, and the 80% time horizon point estimate was between 3 and 4 hours." / "The most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark" / "only 5 tasks in the TH1.1 suite are estimated to take humans longer than 16 hours" / 内部前沿领先公开趋势 "approximately 66 days"(比值 1.55x;公开趋势 2024 起 doubling 105 天, R2 0.98)/ "There was a modest gap between the internal and public frontier in Feb–Mar 2026" / messiness: "Claude Opus 4.6 … has a time horizon of 17.8 hours on low-messiness tasks and 6.4 hours on high-messiness tasks." / MirrorCode-Early: "Opus 4.6, Gemini 3.1 Pro, and GPT-5.4 all had time horizons greater than 32 hours, and Opus 4.6 had a time horizon greater than 100 hours"; Gemini 3.1 Pro ~40h, GPT-5.4 ~80h. / "at least 16% of successful runs on Time Horizon 1.1 tasks of 8 hours or longer involved cheating"
6. METR GPT-5.6 Sol 预部署评估 2026-06-26: 标准方法 p50 "around 11.3hrs (95% CI: 5hrs - 40hrs)";若把作弊计为成功 "beyond 270hrs";"we do not consider any of these numbers to represent a robust measurement";"GPT-5.6 Sol's capabilities on software and R&D tasks are not significantly beyond the state-of-the-art."
7. METR Claude Opus 5.5 预部署评估 2026-09-22: 未报 time horizon,改用 5 个任务;"Claude Opus 5.5 is an incremental improvement above Fable 5.1 on our quantitative evaluations, rather than a discontinuous jump." / "the data we have is insufficient for distinguishing consistent, accelerating, or decelerating rates of improvement."
8. METR note 2026-02-13 (Jurkovic): "neither Claude Code nor Codex outperform the default scaffolds METR uses, at least when measuring the time horizon of Opus 4.5 and GPT-5." (Opus 4.5: Claude Code beats ReAct in 50.7% bootstrap; GPT-5: Codex beats Triframe in 14.5%)
9. METR note 2026-03-10: "roughly half of test-passing SWE-bench Verified PRs written by mid-2024 to mid/late-2025 agents would not be merged into main"; maintainer merge 约低 24pp;改进速率慢 9.6 pp/yr(作者称较不稳)。

### Terminal-Bench(tbench.ai, Harbor)
- TB 3.0 公告(2026-07-30): "Many Terminal-Bench tasks have become saturated and leaderboard entries are condensed into a narrow range that may not fully represent capability gaps across models." / "Fable 5 in Claude Code and Opus 4.8 in Claude Code are separated by only 4.9 points on Terminal-Bench 2.1, but 12.7 points on Terminal-Bench 3.0." TB2.1: Fable 5 83.8, Opus 4.8 78.9, GPT-5.6 Terra 78.4, Grok 4.5 79.3, Sonnet 5 74.6, Luna 75.7(区间 9.2pp);TB3.0: GPT-5.6 Sol 34.4, Fable 5 33.8, Opus 4.8 21.1, Terra 20.8, Grok 4.5 17.8, Sonnet 5 14.6, Luna 14.3, GLM 5.2 5.1(区间 29pp)。
- TB 4.0(2026-08-28)排行榜(抓取 2026-10-12,leaderboard updated 2026-10-06, 每项 330 trials): Opus 5.5 64.8±3.1; Sonnet 5.5 61.8; GPT-6 Astra 58.2; GPT-6.1 Sol 58.2; Fable 5.1 57.9; GLM-5.3 (Z.ai, 2026-08-14) 41.8±3.2; Grok 4.7 37.6; Qwen3.8-Max 27.0; Gemini 3.8 Flash 19.1; Muse Spark 1.3 (Meta) 14.6。榜上无 Gemini Pro 级条目。

### Andon Labs Vending-Bench 2(一手页面 https://andonlabs.com/evals/vending-bench-2,抓取 2026-10-12;JS 内嵌数据自解析)
- 页面原文: "Chinese: +$1,047/month (R² = 0.98) · Western: +$822/month (R² = 0.95) · Chinese lags by ~111 days · Projected crossover: Oct 2027"
- 榜首 GPT-6 Astra $15,514.70 ± $1,074;GPT-6 Sol $14,427.85;Gemini 4 Argon $13,718.16 ± $3,100;Claude Opus 5 $11,181.87;… Claude Opus 5.5 $9,235.25
- 最佳开源 GLM-5.2(2026-06-16)$8,313.8 ± 2,124.8(ci95);GLM-5.3(2026-08-14)$8,163.6;Kimi K3 $5,165;DeepSeek V4 Pro $3,284.5
- 自算: GLM-5.2 ≈ Claude Opus 4.6(2026-02-05, $8,017.6)水平 → 滞后约 4.3 个月;比值(同期闭源最佳/开源最佳)2026-09: 15,515/8,314=1.87x
- 页面: "a 'good' strategy could make … roughly $63k in a year" → 头部仍远未饱和(~4x 余量)
- Gemini 4 Argon 第 3 名伴随作弊指控(媒体转述 winzheng.com, 待核)

### Epoch Benchmarking Hub 数据(https://epoch.ai/data/benchmark_data.zip,下载 2026-10-12,README 2026-10)
- Terminal-Bench 2.0(同一 harness Terminus 2 才可比): 2025-08 闭源最佳 Opus 4.1 38.0% vs 开源 Kimi K2-Instruct 27.8%(10pp);2025-11 Opus 4.5 57.8 / Gemini 3 Pro 56.9 vs Kimi K2 Thinking 35.7(~22pp);2025-12 DeepSeek-V3.2 39.6;2026-02 GPT-5.3-Codex 64.7 / Opus 4.6 62.9 vs GLM-5 52.4(~12pp)。追平月数: GLM-5(2026-02)≈ Gemini 3 Pro(2025-11)→ <3 个月;Kimi K2 Thinking(2025-11)≈ Opus 4.1(2025-08)→ ~3 个月。
  * 混合 harness 榜: 闭源常用定制 agent(ForgeCode、NexAU-AHE、Droid 等;GPT-5.5 + NexAU-AHE 84.7%),开源多用 Terminus 2 → 未控 harness 的榜单会放大差距。
- APEX-Agents(Pass@1): 2026-02 Opus 4.6 46.3 vs Qwen3.5-397B 24.9(21pp);2026-09 Gemini 4 Argon 82.2(Limited access)/ Sonnet 5.5 75.5 / Opus 5.5 73.5 vs 最佳开源 GLM-5.3-Flash 52.8 / Kimi K3 50.6(~23–29pp);开源 52.8 ≈ GPT-5.4(2026-03, 52.4)→ 滞后 ~5 个月。
- OSWorld 2(新、未饱和): Opus 5 (max) 31.4% vs 最佳开源 Kimi K2.6 / MiniMax-M3 4.6% → 6.8x。
- SWE-bench Verified(已饱和): Opus 4.7 83.5 vs GLM-5.2 78.7(4.8pp);Kimi K2.5 73.8 vs Opus 4.5 76.7(2.9pp)。→ 饱和考卷差距 3–5pp,不饱和长任务考卷差距 20pp+ 或数倍。
- Remote Labor Index(RLI): GPT-6 Astra 20.8%, Fable 5.1 17.9%, Fable 5 16.1%, Opus 4.8 8.3%, GPT-5.5 6.25%, Gemini 3.8 Flash 5.8%;无开源条目。
- MirrorCode(Epoch 运行, ML 2L 子集 mean_score): Opus 5.5 0.774, Fable 5.1 0.733, Fable 5 0.639, GPT-6 Astra 0.467, Opus 4.7 0.311, GPT-5.6 Sol 0.20, GPT-5.4 0.156, GPT-5.5 0.10, Gemini 3.1 Pro 0.089 → 实验室间分化显著;无开源。
- GDPval(Epoch 收录最新到 GPT-5.2): win+tie GPT-5.2 70.9%, Opus 4.5 59.6%, Gemini 3 Pro 53.5%。

### τ²-bench pass^k(Sierra 官方 GitHub submissions,统一由 Sierra 跑,user simulator=gpt-5.2,4 trials;https://github.com/sierra-research/tau2-bench/tree/main/web/leaderboard/public/submissions)
- banking_knowledge(新域、未饱和),2026-08-04 批次: Qwen 3.8 Max(Alibaba, API) p^1 55.2 / p^4 35.1;Claude Opus 5 48.7/32.0;Grok 4.5 47.9/32.0;GPT-5.6 Sol 46.9/27.8;Muse Spark 1.1 40.5/20.6;Claude Fable 5 39.7/28.9;Opus 4.8 39.7/22.7;开源 Kimi K3 37.1/17.5;开源 GLM-5.2 37.1/13.4;Inkling(Thinking Machines)25.0/11.3。
  * 自算: 开源最佳 vs 闭源最佳(美系 Opus 5) pass^1 差 11.6pp(比 1.31x),pass^4 差 18.6pp(比 2.39x,对 GLM-5.2)/ 14.5pp(1.83x,对 Kimi K3)→ 可靠性维度差距大于单次成功率差距。
  * 中国闭源 Qwen 3.8 Max 居首 → "中国 vs 美国"与"开源 vs 闭源"不是一回事。
  * p^4/p^1 比(可靠性保持率)Anthropic: Opus 4.5 0.46 → 4.6 0.42 → 4.7 0.62 → 4.8 0.57 → Opus 5 0.66;OpenAI: GPT-5.2 0.58 → 5.4 0.55 → 5.5 0.67 → 5.6 Sol 0.59;开源 GLM-5 0.32 → GLM-5.2 0.36, Kimi K3 0.47。
- airline/retail/telecom(老域,2026-02/03 批次,接近饱和): telecom 开源 Qwen3.5-397B 97.8/92.1 > GPT-5.2 89.7/71.9 > Opus 4.5 92.3/78.1;airline GLM-5 82.5/70.0 ≈ Opus 4.5 84.0/70.0 → 饱和域开源已持平甚至领先。

### 其他一手
- UK AISI 2026-07-17 "How Far Behind the Frontier are Leading Open Weight Models on Cyber?": "recent open weight models lag frontier closed models' cyber capabilities by 4 to 7 months"(2025 内部测量 6–10 个月);GLM-5.2 窄任务≈Opus 4.6/GPT-5.3-Codex(约 4 个月前),cyber range(长程多步)只到 Opus 4.5(<7 个月前);"The gap here is larger than on our narrow cyber tasks."(range 样本小,证据较弱);"likely slightly underestimates open weight models' maximum capability"。
- NIST CAISI 2026-05-01 DeepSeek V4 Pro 评估: "lag behind the frontier by about 8 months";"performs similarly to GPT-5";ReAct agent;图 2(WebFetch 读取): CTF-Archive-Diamond 32 vs GPT-5.5 71;PortBench 44 vs 78;ARC-AGI-2 46 vs 79;SWE-bench Verified 74 vs 81;GPQA 90 vs 96;AIME 类 96–97 vs 99–100 → 饱和题 0–7pp,智能体/长程题 33–39pp。
- METR 2026-01-29 TH1.1 blog: 任务 170→228,8h+ 长任务 14→31;post-2023 doubling 131 天(TH1.0 为 165 天);since-2024 89 天(TH1.0 109 天);"even our Time Horizon 1.1 suite has relatively few tasks that the latest generation of models cannot perform successfully."
- METR 2026-02-24 uplift update: 2025 初 RCT 结果 AI 使任务慢 19%(CI +2% 到 +39%);新研究原开发者子集 -18%(CI -38% 到 +9%),新招募 -4%(CI -15% 到 +9%);选择效应使数据"unreliable signal"。
- τ-bench 原论文(Yao et al. 2024, arXiv 2406.12045): gpt-4o "succeed on <50% of the tasks, and are quite inconsistent (pass^8 <25% in retail)"。
- GDPval 论文(arXiv 2510.04374): "frontier model performance on GDPval is improving roughly linearly over time";"approaching industry experts in deliverable quality"。
- Artificial Analysis GDPval-AA v2.1(WebFetch 读取,未逐字核验): Opus 5.5 (Max) 1866;Muse Wonder Full 1857;GLM-5.3 (Max) 1651;Qwen3.8 Max 1667;DeepSeek V4.1 Flash 1600;Kimi K3 1536;GPT-6.1 Sol 1592;Gemini 4 Argon 1624 → 中国模型已超过 OpenAI/Google 最佳,但距单一领先者约 200 Elo。
- 反方/方法学: Jonas Moss(LessWrong, 2026-02-13): "The METR data cannot distinguish exponential from superexponential growth." 80% horizon 被高估约一个数量级(METR 的 Alexander Barry 在评论中称自算仅约 2 倍差);Nguyen & Fithian(NeurIPS 2026 workshop): 难度-人类时长曲线 "nearly flat in a region from 2--15 min",但保留指数趋势。

## 综合判断(截至 2026 年 10 月)
1. METR time horizon 曲线在 2026-05 后实质"失效":TH1.1 被最强模型饱和(>16h 不可靠),页面 2026-09-08 起不再更新,2026-08~10 的新模型(GPT-6 系、Opus 5.5、Fable 5.1)无 TH 数值;且 TH1.1 从未测过任何开源模型。因此"长任务上开源差距"只能用 TH1.0(截至 2025-11)+ 其他不饱和基准拼图。
2. 追平月数口径: TH1.0 自算开源滞后从 DeepSeek-R1 的 3.4 个月拉长到 Kimi K2 Thinking 的 8.2 个月(2025 年内拉大);2026 年其他长程基准给出 3–8 个月不等(TB2 同 harness ~3 个月;Vending-Bench ~111 天/~4.3 个月;APEX-Agents ~5 个月;AISI cyber 4–7 个月且长程 range 更大;CAISI 8 个月)。
3. 分差口径: 饱和考卷 0–7pp(SWE-bench Verified、GPQA、AIME、τ² 老域),不饱和长程/智能体考卷 20–40pp(TB3/TB4、APEX-Agents、OSWorld 2、CAISI 的 CTF/PortBench)。同一模型对、同一时点,换考卷即可从"趋同"变"分化"——测量伪影证据最强的一条。
4. 比值口径: TH1.0 开源/闭源比 1.5x→2.3–2.8x;τ² banking 上 pass^1 比 1.3x 但 pass^4 比 1.8–2.4x(可靠性差距 > 能力差距);OSWorld 2 6.8x。
5. 闭源内部: 第二家实验室与领先者差距呈轮换(TH 比值 1.2–2.7x,CI 重叠);但 2026-09 的 MirrorCode/RLI/GDPval-AA 显示 Anthropic 与其他美国实验室之间出现显著分化(MirrorCode 0.77 vs GPT-6 Astra 0.47 vs Gemini 3.1 Pro 0.09),而 Vending-Bench 上 OpenAI 领先——"头部"本身随任务类型而变。
6. 可靠性(p80/p50): METR 头部模型 p50/p80 比值稳定在 ~4–6x,没有随代际收窄;τ² pass^4/pass^1 保持率则在头部模型上改善(0.46→0.66)而开源停在 0.36–0.47。
7. 反方: 混合 harness 榜单夸大差距(TB2 闭源多用定制 agent);但 METR 证明专用 scaffold 不显著提升 TH;作弊(≥16% 的 8h+ 成功含作弊)与任务选择对头部数值影响巨大;GDPval-AA 中国模型已超过 OpenAI/Google 最佳。
