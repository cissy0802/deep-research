# CATCHUP-open-china — 开源与中国追赶(追赶速度的测量)

截至 2026-10-12 调研中。数据下载目录(非仓库):scratchpad/catchup/;自算脚本 scratchpad/catchup_scripts/gap3.py

## C1 Epoch 2026-05-29 Data Insight(官方一手,分析机构)
URL: https://epoch.ai/data-insights/open-closed-eci-gap (May 29, 2026, Jack Edwards & Luke Emberson)
- "Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of four months in the Epoch Capabilities Index (ECI), our aggregate measure of model capability. The average ECI gap was 8 points, similar to the gap between GPT-5 and GPT-5.5."
- 方法: "To calculate the average time gap, we proceed day by day over our analysis window, January 1, 2026, through May 28, 2026. For each day, we identify the open-weight model with the highest ECI score available by that date. We then compare that model to the historical state-of-the-art ECI frontier and ask: what is the most recent date on which the SOTA model was not significantly better than this open-weight model?"
- 判定阈值: "We treat the open-weight model as having plausibly caught up to a previous SOTA model if it outperforms that SOTA model in at least 5% of paired bootstrap samples."
- 敏感性: "This estimate would grow to six months if we required that the open-weight model's point estimate for ECI be strictly higher than the closed-weight model it is catching up to (instead of better in at least 5% of samples)."
- CI: "We find an average ECI gap of 8 points, with a 90% confidence interval of 7 to 11 units."
- 局限(两条都偏向低估差距): "evidence suggests that open-weight models tend to perform worse on private benchmarks compared to closed models, plausibly because they more aggressively hillclimb on public benchmarks. Second, we only include models with enough public benchmark coverage to assign an ECI. Leading closed labs do not always release their most capable models"

## C2 Epoch 2025-10-30 Data Insight
URL: https://epoch.ai/data-insights/open-weights-vs-closed-weights-models (Oct 30, 2025, Luke Emberson)
- "Frontier open-weight models lag behind the most capable models by an average of 3 months in the Epoch Capabilities Index (ECI) ... That corresponds to an average ECI gap of around 7 points, similar to the gap between o3 and GPT-5."
- "We find an average "horizontal" time gap of 3.5 months, with a 90% confidence interval of 1.1 to 5.3 months. Along the vertical dimension, we find an average gap of 7 ECI points, with a 90% confidence interval of 0 to 14 units."
- 窗口: 2023-01 至 2025-10;"the gap varies considerably over time, sometimes even closing completely. Until the release of o1-mini, Llama 3.1-405B was rated on par with the closed-source state-of-the-art model, Claude 3.5 Sonnet."
- 方法(与 2026 版不同:2025 版用两条包络线水平距离;2026 版逐日+bootstrap 配对)

## C3 自算:Epoch benchmark_data.zip(2026-10-13 版 ECI + 500 次 bootstrap)复刻
数据: https://epoch.ai/data/benchmark_data.zip -> epoch_capabilities_index/eci_scores.csv + eci_bootstraps.json
方法: 逐日;open = Accessibility group "Open weights" 中当日 ECI 点估计最高者;SOTA 前沿 = 任一模型创新高的序列;找开源模型在 >=5% 配对 bootstrap 中不低于的最近一个前沿模型 k,gap = t − (k 之后下一个前沿模型的发布日);ECI 纵向差 = 当日全体最高 ECI − 开源最高 ECI。
结果(时间差月 / ECI 点差):
- 2024H1 7.8 / 6.4;2024H2 1.7 / 5.3;2025H1 2.8 / 5.5;2025H2 4.1 / 6.1;2026H1 5.9 / 9.9;2026-07-01~10-12 4.6 / 7.6
- 同窗口 2026-01-01~05-28: 我算 5.9 月 / 9.8 点(Epoch 发布 4 月 / 8 点)— 差异来自 ECI 每次数据更新整体重拟合 + 我对"最近日期"的实现细节;严格点估计口径 7.0 月(Epoch: 6 月)。
- 2026-05-29~10-12: 5% 口径 4.95 月 / 8.4 点;严格口径 6.3 月。
- 月度: 2026-08 最窄(3.8 月 / 5.3 点,Kimi K3 2026-07-16 ECI 157.45 + DeepSeek V4 Pro 0813 155.31),9-10 月重新拉大(Claude Fable 5.1 164.7、GPT-6 Astra 166.45、Claude Opus 5.5 167.33 → 10 月 5.5 月 / 9.9 点)。
- 结论口径: 用同一方法同一数据版本,2025 年平均 3.4 月 / 5.8 点 → 2026 年至今约 5.4 月 / 8.9 点:两种"差距"定义都显示 2026 年比 2025 年更宽,但并非单调——呈锯齿(闭源大版本发布拉大,中国开源大版本 1-3 月内补回一部分)。

## C4 METR 一手:开源在 time horizon 上的落后(METR 已评开源模型极少)
- METR 2025-06-27 https://metr.org/evaluations/deepseek-qwen-report/ : "We found that the level of autonomous capabilities of mid-2025 DeepSeek models is similar to the level of capabilities of frontier models from late 2024." 限制: "We spent roughly one workday eliciting the capabilities of each model, which is less than the time we spent on some previous models."
- METR 2025-02-12 https://metr.org/evaluations/deepseek-v3-report/ : "Overall, the performance of open-weight models on our tasks is on par with state-of-the-art models from 6 months ago, whereas they had previously lagged significantly further behind."
- 自算(Epoch zip 中 metr_time_horizons_external.csv,METR TH 数据镜像): TH50 分钟
  - DeepSeek-R1 (2025-01-20) 27 min [CI 13–51] vs o1 (2024-12-17) 39 → 比值 0.69
  - DeepSeek-R1-0528 (2025-05-28) 31 vs o3 (2025-04-16) 120 → 0.26
  - Kimi K2 Thinking (2025-11-06) 54 [25–98] vs GPT-5 high (2025-08-07) 203 → 0.27;闭源首次达到 54 min 是 Claude 3.7 Sonnet (2025-02-24, 56-60) → 追平月数约 8.4 月
  - 闭源顶点 Claude Mythos Preview (early, 2026-04-07) TH50 1044.8 min ≈ 17.4 h,CI 508.9–3304.3 min;TH80 185.9 min
  - 结论: time horizon 比值从 R1 时期 ~0.7 降到 ~0.27;METR 之后未再公开评测 2026 年开源旗舰(Kimi K2.5/K3、GLM-5.x、DeepSeek V4)→ 长任务维度上开源追赶缺少独立测量(覆盖缺口本身是口径问题)。

## C5 自算:Epoch 基准中心(2026-10 版)各基准 开源最佳 vs 同日闭源最佳
(脚本 bench2.py;开/闭源由 model_metadata.accessibility 判定;"同日"= 闭源发布日 <= 开源模型发布日)
| 基准 | 最佳开源(日期) | 分数 | 同日最佳闭源 | 比值 | 当前闭源最佳 |
|---|---|---|---|---|---|
| GPQA Diamond | Kimi K3 (2026-07-16) | 0.931 | GPT-5.4 Pro 0.946 | 0.98 | GPT-6 Astra 0.958 |
| SWE-bench Verified (Epoch 跑) | GLM-5.2 (2026-06-16) | 0.787 | Claude Opus 4.7 0.835 | 0.94 | 0.835 |
| DeepSWE | Kimi K3 | 0.685 | GPT-5.6 Sol 0.727 | 0.94 | GPT-6 Astra 0.741 |
| OSWorld | Kimi K2.5 (2026-01-27) | 63.3 | Claude Opus 4.5 66.3 | 0.95 | Sonnet 4.6 72.1 |
| FrontierMath T1-3 | Kimi K3 | 0.722 | GPT-5.6 Sol 0.891 | 0.81 | GPT-6.1 Sol 0.937 |
| PostTrainBench | Kimi K3 | 0.320 | Claude Fable 5 0.418 | 0.76 | 0.418 |
| APEX-Agents | GLM-5.3-Flash (2026-08-20) | 0.528 | Gemini 3.7 Flash 0.678 | 0.78 | Gemini 4 Argon 0.822 |
| Vending-Bench 2 ($) | GLM-5.2 | 8314 | Claude Opus 4.7 10937 | 0.76 | GPT-6 Astra 15515 |
| Terminal-Bench 2.0 | GLM-5 (2026-02-11) | 0.524 | Claude Opus 4.6 0.798 | 0.66 | GPT-5.5 0.847 |
| HLE | Kimi K2.5 | 0.244 | Gemini 3 Pro 0.375 | 0.65 | GPT-6 Astra 0.548 |
| FrontierSWE | Kimi K3 | 0.259 | Claude Fable 5 0.470 | 0.55 | GPT-6 Astra 0.655 |
| METR TH50 | Kimi K2 Thinking (2025-11) | 54 min | GPT-5 203 | 0.27 | Mythos 1045 |
- 规律:饱和/知识型基准(GPQA、SWE-bench Verified)比值 0.94–0.98;长程/agentic/前沿数学(FrontierSWE、Terminal-Bench、HLE、METR)比值 0.27–0.66。
- 覆盖警示:很多开源新模型未在 Terminal-Bench/HLE/METR 上被收录(最新开源条目停在 2026-01/02),新基准(FrontierSWE)只收录 2026-06 后的闭源模型 → "追平月数"在新基准上被人为压短(如 FrontierSWE 算出 1.2 月,只是因为更早的闭源模型没测)。

## C6 NIST CAISI(美国商务部下属政府机构;利益位置:执行"AI Action Plan",任务含评估"adversary AI",新闻稿由商务部长做政治定调)
### 2025-09-30 DeepSeek 评估 PDF https://www.nist.gov/document/caisi-evaluation-deepseek-ai-models-report
- "The best U.S. model outperforms the best DeepSeek model (DeepSeek V3.1) across almost every benchmark. The gap is largest for software engineering and cyber tasks, where the best U.S. model solves 20-80% more tasks than the best DeepSeek model."(新闻稿版本写作 "over 20% more tasks" —— 同机构两个口径)
- 表 3.1(%): CVE-Bench GPT-5 65.6 / Opus4 66.7 / V3.1 36.7;Cybench 73.5 / V3.1 40;CTF-Archive 50.6 / 28.2;SWE-bench Verified Opus4 66.7 / V3.1 54.8;Breakpoint 98.0 / 78.5;MMLU-Pro Opus4 90.2 / V3.1 89.0;GPQA GPT-5 86.9 / R1-0528 81.3;HLE 26.6 / 13.6
- 规律:知识类(MMLU-Pro)差 1 个点,agentic 网络安全差近一倍。
- 部长定调(新闻稿): "The report is clear that American AI dominates, with DeepSeek trailing far behind."
### 2026-05-01 DeepSeek V4 Pro https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
- "CAISI evaluations indicate that DeepSeek V4's capabilities lag behind the frontier by about 8 months"
- 厂商口径 vs 独立: "According to DeepSeek's data, DeepSeek V4 is about as capable as Opus 4.6 and GPT-5.4, which were released about 2 months ago. However, CAISI's evaluations, which include non-public benchmarks, indicate that DeepSeek V4 performs similarly to GPT-5, which was released about 8 months ago"
- "As shown in Figure 1, the U.S. capability frontier tends to lead the PRC frontier by roughly 8 months."
- 表: PortBench(非公开) GPT-5.5 78% / Opus 4.6 60% / V4 Pro 44%;CTF-Archive-Diamond 71/46/32;ARC-AGI-2 semi-private 79/63/46;GPQA 96/91/90;OTIS-AIME 100/92/97;IRT Elo 1260±28 / 999±27 / 800±28(GPT-5.4 mini 749)
- 规律再现:数学/GPQA 几乎持平甚至反超 Opus 4.6,非公开 agentic(PortBench)与网络安全差距大。
### 2026-07-17 GLM-5.2 https://www.nist.gov/news-events/news/2026/07/caisi-assessment-zais-glm-52
- "GLM-5.2's overall capabilities are similar to that of GPT-5.2, released in December 2025. GLM-5.2's cyber capabilities are similar to that of Opus 4.6, released in February 2026."(GLM-5.2 2026-06-16 发布 → 综合约 6 个月、网络安全约 4 个月)
### 2026-07-23 UK AISI/CAISI Kimi K3 网络安全 https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities
- "on average, Kimi K3 reached step 17 of this 32-step attack path, while the most cyber-capable U.S. models reached 28.5 steps on average."
- "Kimi K3 achieved ACE on 0/41 samples, whereas the most cyber-capable models achieved ACE on 20/41 samples on average"
- 注意: "U.S. closed-weight models were evaluated with system-level safeguards disabled"
### 2026-09-17 GLM-5.3 网络安全 https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities
- "GLM-5.3 lags the capability level of the U.S. frontier by about four months in an aggregate measure of performance across CAISI cyber benchmarks"
- 但任务级比值:SEC-Bench Pro 40.4% vs U.S. best 90.2%;ExploitGym 9.4% vs 44.4%;OSS-Fuzz(私有)7.7% vs 23.2%;ExploitBench 61.1% vs 100%。
- 口径: "This blog post does not compare to models that have been developed but not yet released, which could have stronger capabilities." "U.S. frontier best" 含 "trusted-access releases"
- 关键口径冲突示例:同一时点"追平月数≈4 个月"与"成功率比值≈0.2–0.45"同时成立——前沿每月改进快,所以数月滞后=数倍成功率差。

## C7 DeepSeek-R1 作为追赶标志(arXiv 2501.12948v1, 2025-01-22;后经 Nature 2025 发表——同行评审版待核)
- 厂商口径: "DeepSeek-R1 achieves performance comparable to OpenAI-o1-1217 on reasoning tasks."
- 自报表 4(R1 vs o1-1217): AIME24 79.8 vs 79.2;MATH-500 97.3 vs 96.4;Codeforces 2029 vs 2061;GPQA 71.5 vs 75.7;SWE Verified 49.2 vs 48.9;Aider-Polyglot 53.3 vs 61.7;SimpleQA 30.1 vs 47.0。o1 分数取自 OpenAI 官方报告("Since accessing the OpenAI-o1-1217 API is challenging in mainland China, we report its performance based on official reports")
- 时间差: o1-preview 2024-09-12 → R1 2025-01-20 约 4 个月;o1-1217 → R1 约 1 个月。
- 自承短板: "large-scale RL has not been applied extensively in software engineering tasks. As a result, DeepSeek-R1 has not demonstrated a huge improvement over DeepSeek-V3 on software engineering benchmarks."
- 独立复测(METR TH50): R1 27 min vs o1 39 min;Epoch ECI 自算 2025-01 时间差约 1.0 月、2025-02 ECI 差 2.9 点 → R1 时期为近三年开源/闭源差距最小窗口之一(另一个是 2024-08 Llama 3.1-405B)。

## C8 蒸馏
- Gudibande et al. 2023 (arXiv 2305.15717, ICLR 2024): "imitation models close little to none of the gap from the base LM to ChatGPT on tasks that are not heavily supported in the imitation data. We show that these performance discrepancies may slip past human raters because imitation models are adept at mimicking ChatGPT's style but not its factuality."
- DeepSeek-R1 论文 §4.1: "distilling more powerful models into smaller ones yields excellent results, whereas smaller models relying on the large-scale RL mentioned in this paper require enormous computational power and may not even achieve the performance of distillation. Second, while distillation strategies are both economical and effective, advancing beyond the boundaries of intelligence may still require more powerful base models and larger-scale reinforcement learning." 表 6: R1-Distill-Qwen-32B AIME24 72.6 vs R1-Zero-Qwen-32B(纯 RL)47.0。
- 长程/agent 上蒸馏(SFT)较弱的证据:
  - MEM1 (arXiv 2506.15841v2, 2025-07): "the SFT model consistently underperforms compared to its RL counterpart ... when the number of objectives exceeds six, the performance of the SFT model collapses, whereas the RL-trained model continues to demonstrate strong robustness"
  - PivotRL (NVIDIA, arXiv 2603.21383, 2026-03): "While supervised fine-tuning (SFT) is compute efficient, it often suffers from out-of-domain (OOD) degradation. Conversely, end-to-end reinforcement learning (E2E RL) preserves OOD capabilities, but incurs high compute costs"
- 厂商指控(厂商口径,利益相关:支持出口管制):
  - Anthropic 2026-02-23 https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks : "These labs generated over 16 million exchanges with Claude through approximately 24,000 fraudulent accounts"; "Each campaign targeted Claude's most differentiated capabilities: agentic reasoning, tool use, and coding."; "In reality, these advancements depend in significant part on capabilities extracted from American models"(未提供量化证据说明"significant part")
  - OpenAI 2026-02-12 致众议院中国特别委员会备忘录(仅媒体转述,Reuters/Bloomberg): 称 DeepSeek "ongoing efforts to free-ride on the capabilities developed by OpenAI and other U.S. frontier labs"

## C9 Stanford AI Index 2026(官方一手报告,2026-04)https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- "The U.S.-China AI model performance gap has effectively closed. ... In February 2025, DeepSeek-R1 briefly matched the top U.S. model. As of March 2026, the top U.S. model leads by 2.7%"
- "In February 2025, DeepSeek‑R1 (1,400) trailed the leading U.S. model (o1‑2024‑12‑17, 1,405) by just 5 Arena points (0.4%). As of March 2026, the top U.S. model (Claude Opus 4.6, 1,503) led the top Chinese model (Dola‑Seed‑2.0 Preview, 1,464) by 39 points (2.7%)."
- 开/闭源: "In May 2023, the leading closed-weight model (GPT‑4‑0314) outperformed the top open-weight model (Vicuna‑13B) by 174 points (15.2%) ... narrowed the gap to just 7 points (0.5%) by August 2024. Over the past year, that trend reversed ... As of March 2026, the top closed-weight model, Claude Opus 4.6 (1,503), led the top open-weight model GLM‑5 (1,454) by 49 points (3.4%)."
- 口径问题: "%"= Elo 差 / 对手 Elo 分,Elo 是区间尺度,百分比无意义;39 Elo ≈ 头部胜率 55.6%,49 Elo ≈ 57.0%(自算 1/(1+10^(-Δ/400)))。且数据源 = Arena 偏好投票。

## C10 自算:Arena 官方历史快照(HF lmarena-ai/leaderboard-dataset,text_style_control,overall,截至 2026-10-08;license != Proprietary 视为开源)
- 每月末快照 闭源第一 vs 开源第一 Elo 差: 2024-08 39;2025-01 6.2(R1);2025-02 2.8;2025-06 53.8;2025-10 29.2;2025-11 61.6(Gemini 3 Pro);2026-03 48.5;2026-05 28.3;2026-07 21.8(Kimi K3 上榜);2026-08 18.7;2026-09-01 18.4;2026-09-13 20.9;2026-09-30 起 36.8(Gemini 4 Argon high 1525,仅 4,942 票,预览)
- 要求 >=10,000 票时: 2026-08 18.7、2026-09 17.5、2026-10 16.3(最窄自 2025-02 以来)
- 2026-10-08 最新榜: Kimi K3 max 1488 排第 16,高于 GPT-6.1 Sol max(1484,第 21)、GPT-5.6 Sol(1485);Claude Opus 4.6 high(2026-02)1504 仍排第 3,与 Claude Opus 5.5 high(1507)CI 重叠。→ Arena 文本榜在前沿已基本不区分 2026 年内的能力代差(Epoch ECI: Opus 4.6 155.2 vs Opus 5.5 167.3;GPT-6.1 Sol 166.1 vs Kimi K3 157.5)。这是"用户感知饱和"的直接证据。
- 媒体称"Arena 2026-09 闭源 vs 开源差距扩大到 29 Elo"——官方快照不支持该数字:9 月大部分快照约 18–21,9-30 起因 Gemini 4 Argon 预览上榜变为约 37;29 无对应快照(可能源自 BenchLM 等第三方聚合,未核实)。
- Arena Agent 榜(2026-10-12,score 指标,会话数见数据): 前 15 名全部闭源;最佳开源 DeepSeek V4.1 Flash 0.033(第 16)vs Claude Opus 5.5 Max 0.179、GPT 6.1 Sol 0.138;Kimi K3 0.030。同一平台:文本榜开源追到前沿 20 Elo 内,agent 榜开源仅为头部分数的约 1/5。

## C11 Artificial Analysis(分析机构,自跑基准)
- 2026-04-30 https://artificialanalysis.ai/articles/recent-open-weights-model-launches : "This places the best open weights models within 3-6 points of the leading proprietary models: OpenAI's GPT-5.5 (xhigh) at 60 ... just one year ago the highest-scoring open weights model was DeepSeek V3 0324 which achieved 22 on the Intelligence Index, and was ~13 points below the highest-scoring proprietary model, Claude 3.7 Sonnet (Reasoning) at 35."
- 同文反向: "The gap to proprietary remains wide on the hardest reasoning and agentic coding evaluations. ... On CritPt (Research-level Physics) they score 4-12%, vs 27% for GPT-5.5 (xhigh). On TerminalBench Hard (Agentic Coding & Terminal Use) they score 43-46%, vs 61% for GPT-5.5 (xhigh)"
- "The top 10 open weights models on the Intelligence Index are all from China-based AI labs."
- 2026-10-12 模型页(Intelligence Index v4.3): Claude Opus 5.5 (Max) 58;GPT-6 Astra (Max) 53;Gemini 4 Argon (high) 53(2026-09-30 文);最佳开源 MiMo-V2.6-Pro 46;Kimi K3 (Max) 44;DeepSeek V4.1 Flash (Max) 39 → 分差 12 点、比值 0.79(4 月为 6 点、0.90;但指数版本已更换 v4.x→v4.3,跨版本不可直接比)。
- FrontierCode 1.1(Cognition 私有任务,AA 统一 harness,2026-10-12): "Claude Opus 5.5 (max with fallback) leads at 52% ... MiMo-V2.6-Pro is the leading open weights model at 45%, followed by DeepSeek V4.1 Flash (max) and Kimi K3 (max) at 44%";"nine models from six labs score between 43% and 52%" → 在这个"可合并代码"私有基准上开源比值 0.87,差距不大(反例:并非所有 agentic 基准都拉开)。

## C12 METR time horizon 页(官方)https://metr.org/time-horizons/
- 更新日志: "May 8th, 2026: Added Claude Mythos Preview (early) and notice that "Measurements above 16 hrs are unreliable with our current task suite."" ;"September 8th, 2026: Clarified that this page is no longer actively updated."
- Epoch 镜像数据: Mythos Preview (early) TH50 1044.78 min ≈ 17.4 h(CI 508.9–3304.3 min ≈ 8.5–55 h),TH80 185.9 min。
- 对本线的含义: METR TH1.1 中最后一个被测的开源模型是 Kimi K2 Thinking(2025-11,54 min);2026 年开源旗舰无 METR 时长测量,且该页面已停更 → "长任务维度开源是否追上"在 METR 口径下无法回答,只能靠 CAISI/AISI/Epoch 其他 agentic 基准间接推断。

## C13 Epoch 2024 开源报告(分析机构)https://epoch.ai/blog/open-models-report (Cottier et al., 2024-11)
- "In terms of benchmark performance, the best open large language models (LLMs) have lagged the best closed LLMs by 5 to 22 months."
- "In terms of training compute, the largest open models have lagged behind the largest closed models by about 15 months."
- "Training data contamination and "cramming for the leaderboard" may also contribute to higher scores."
- 预测: "Based on the trend in Meta's open Llama models, we expect the lag between the best open and closed models to shorten next year." —— 事后:2025 年 Epoch ECI 滞后确实缩到约 3 个月,但开源领军者从 Meta 换成中国实验室(Meta 2026 年转向闭源 Muse Spark 系列)。
- 时序汇总(滞后月数,不同方法不可严格比): 2024-11 报告 5–22 月(单基准)/15 月(算力) → 2025-02 METR "6 months"(agent) → 2025-06 METR"mid-2025 ≈ late 2024"(约 6–9 月,agent) → 2025-10 Epoch 3.5 月(ECI) → 2026-05 Epoch 4 月(ECI)/ CAISI 8 月(IRT,含私有基准) → 2026-07 CAISI GLM-5.2 ≈ GPT-5.2(约 6 月) → 2026-09 CAISI GLM-5.3 网络安全约 4 月。

## C14 从业者博客:公开 vs 私有基准上的开源滞后
- Håvard Tveit Ihle, "How far behind are open models?", LessWrong 2026-05-28 https://www.lesswrong.com/posts/rJcCrXyEsJKmmDpWG/how-far-behind-are-open-models (约 17 基准,多数取自 Epoch 基准中心)
- "open models are roughly 8-10 months behind the closed frontier"(私有基准);"for public benchmarks the gap is roughly 4-6 months"
- "the gap was smallest around the time of DeepSeek R1, in Jan 2025, and since then the gap has been growing."
- 自承偏差: "This methodology does have a winner's-curse bias.";"several of the "private" benchmarks not being fully private";第三方托管可能降低开源表现。
- 与 CAISI V4 Pro 的"厂商自报≈2 个月 vs CAISI 含私有基准≈8 个月"方向一致。

## 本线小结(截至 2026 年 10 月)
1. 综合指数口径(Epoch ECI)开源滞后:2024 年 5–22 月(单基准)→ 2025 年约 3–3.5 月(最窄在 R1 时 ~1 月)→ 2026 年约 4 月(Epoch 官方)/ 我用 2026-10 数据复算 5–6 月;8 月 Kimi K3 + DeepSeek V4 Pro 0813 把差距压到 3.8 月/5.3 点,9 月 GPT-6/Claude Opus 5.5 又拉回 ~5.5 月/~10 点。锯齿形,2026 均值宽于 2025。
2. 用户偏好口径(Arena 文本)几乎收敛:2026-08~10 开源第一与闭源第一差 16–21 Elo(高票数口径),胜率约 52–53%;且 Arena 已不能区分 Opus 4.6 与 Opus 5.5 → 这是用户感知饱和,不是能力收敛。
3. 政府/私有基准口径(CAISI)滞后更长:DeepSeek V4 Pro 约 8 月(自报 2 月);GLM-5.2 约 6 月;GLM-5.3 网络安全约 4 月(但任务成功率仅前沿的 0.2–0.45)。
4. 长程/agent 维度:同时点比值 0.27(METR TH)、0.55(FrontierSWE)、0.66(Terminal-Bench)、0.78(APEX-Agents)vs GPQA 0.98、SWE-bench Verified 0.94;Arena Agent 榜开源最好仅为头部 1/5。但并非全部:FrontierCode(私有)0.87,DeepSWE 0.94。
5. 蒸馏:能快速搬运可验证的短推理(R1-Distill),学术证据显示 SFT/模仿在长程与分布外泛化上弱(Gudibande 2023;MEM1;PivotRL);厂商指控(Anthropic 16M 交互、OpenAI 备忘录)有利益立场且未量化贡献。
