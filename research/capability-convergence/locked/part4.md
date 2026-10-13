# 锁定口径 · Part 4(G14–G18)

> 文章:「AI 能力最终会趋同是真的吗」(截至 2026-10)。每组三票均为 CORRECTED;冲突处取最严格修正。G18 已吸收 04-verification-round3.md 中 R2-metr-open-lag 双席审计(counter:方向存争;method:降级为弱结论)的限定。

---

## G14 · 基准饱和速度、OpenAI 停报 SWE-bench Verified、厂商主打基准迁移、AA 指数换题

### (1) 锁定表述

- **饱和速度**:口径为 Epoch 数据扣随机基线后归一化,n=(s−baseline)/(1−baseline),以首个归一化分 ≥80% 的模型发布日计。
  - GPQA Diamond(2023-11 发布)约 19 个月,2025-06 由 Gemini 2.5 Pro 达到,原始 85.29%,归一化 0.804,只多一题过线。
  - SWE-bench Verified(2024-08)约 20 个月,2026-04 由 Claude Opus 4.7(max)达到,83.5%。这是 Epoch 独立复测口径;厂商自报更早,约 2025-11 Claude Opus 4.5 自报约 80.9%,即约 15 个月。
  - ARC-AGI-2(2025-03)约 11 个月,2026-02-12 由 Gemini 3 Deep Think 达到,84.6%。若不计 Deep Think,则是 2026-03 的 GPT-5.4 Pro(83.3%)。
  - Terminal-Bench 2.0(2025-11 发布)约 3 个月后,2026-02-19 由 Gemini 3.1 Pro + 第三方 agent TongAgents 首破 80%(80.2%)。这是"模型 + 第三方 harness"组合的成绩。
  - HLE(2025-01)到 2026-09:GPT-6 Astra 原始分 54.8%,扣 4.8% 随机基线后归一化 52.5%,首次过半。
- **OpenAI 停报 SWE-bench Verified(2026-02-23)**:
  - OpenAI 审计了 o3 在 64 次独立运行中未能稳定解出的 138 道题,其中 59.4% 在测试设计或题面上有实质问题。
  - 所有受测前沿模型在部分题目上能复现 gold patch(人写的参考修复)或题面原文细节。对应小节涉及 GPT-5.2、Claude Opus 4.5、Gemini 3 Flash。
  - OpenAI 因此停报该基准,建议其他开发者也停报,并建议改报 SWE-bench Pro。
  - 后续(仅票 1,二手报道 + 页面摘要,未逐字核):2026-07 OpenAI 审计 SWE-bench Pro,估计约 30% 任务有问题。"撤回推荐"一说未核实。
- **厂商主打基准迁移**:
  - Claude Opus 5.5 发布页(2026-09-22)的基准表列出 Terminal-Bench 4.0 66.4%、FrontierCode v1.1 (Main) 54.4%、CursorBench 4.0 57.8%、GDPval-AA v2.1 1846、AutomationBench 40.0%、HLE 67.7%(with tools),均为厂商自报。FrontierCode 由 AA 独立测得 52.2%。
  - 全文不出现 MMLU、GPQA、SWE-bench、AIME、GSM8K。
  - 对比:Claude 3 发布页(2024-03)主打 MMLU、GPQA、GSM8K。
- **AA 智能指数换题**:
  - v4.0(2026-01)移除 MMLU-Pro、LiveCodeBench、AIME 2025。
  - v4.2(2026-09)移除 GPQA Diamond。v4.2 公告(2026-09-04)称 GPQA Diamond "has now been saturated"。版本史本身对两次移除都未写理由;GPQA 仍作为独立评测继续跑。
  - 另有 v4.1 移除 IFBench,v4.3 用 Terminal-Bench 4.0 替换 TB 2.1。现行版本为 v4.3.2(2026-09)。

### (2) 英文原文引语(逐字)

- OpenAI:"We conducted an audit of 138 SWE-bench Verified problems that OpenAI o3 did not consistently solve over 64 independent runs"
- OpenAI:"We found that 59.4% of the 138 problems contained material issues in test design and/or problem description"
- OpenAI:"all frontier models we tested were able to reproduce the original, human-written bug fix used as the ground-truth reference, known as the gold patch, or verbatim problem statement specifics for certain tasks"
- OpenAI:"This is why we have stopped reporting SWE-bench Verified scores, and we recommend that other model developers do so too"
- OpenAI:"Until we have those, OpenAI recommends reporting results for SWE-bench Pro."
- Claude 3 页面:"undergraduate level expert knowledge (MMLU), graduate level expert reasoning (GPQA), basic mathematics (GSM8K)"
- AA 版本史:"Removed MMLU-Pro, LiveCodeBench, AIME 2025 from Intelligence Index"(v4.0);"Removed GPQA Diamond from the Intelligence Index"(v4.2)
- AA v4.2 公告:"GPQA Diamond, an exceptional scientific reasoning evaluation that has now been saturated"(仅票 1 引用)
- AA:"We still run it on new model releases and report it as a standalone evaluation"(GPQA)

### (3) 判死 / 禁用清单

1. 原稿"Terminal-Bench(2025-05)→2026-02,约 9 个月":判死。2025-05-19 是 TB 1.0 的发布日,而分数全部来自 TB 2.0 榜(2025-11 发布)。正确说法是约 3 个月,且为 agent 组合成绩。
2. 原稿"ARC-AGI-2 于 2026-03 达标,约 12 个月":判死。首个达标是 2026-02 的 Gemini 3 Deep Think,约 11 个月。
3. 原稿"GPT-5.2 64 次运行稳定失败的 138 题":判死。跑 64 次的是 o3,原文是"未能稳定解出",不是"稳定失败"。GPT-5.2 出现在另一处:它解出了 31 道被认定几乎不可能解出的题。
4. 原稿"主流模型能凭记忆复现修复"(不加限定):禁用。必须带原文限定 "for certain tasks",并写明是 gold patch 或题面原文。
5. 原稿"HLE 约 52.5%"(不注口径):禁用。必须注明是归一化值,原始分为 54.8%。
6. 原稿"AA 因饱和移除 MMLU-Pro 等(v4.0)":禁用。v4.0 版本史未写理由;只有 v4.2 移除 GPQA 时在公告里写了 saturated。
7. "SWE-bench Verified 20 个月"不注口径:禁用。须注明是 Epoch 独立复测;厂商自报约 15 个月。

### (4) 证据分级

- 单源已核:Epoch 复算的饱和月数;Opus 5.5 页面内容;AA 版本史。
- 多源证实:OpenAI 停报的原文、数字与日期,三票逐字一致。
- 厂商口径:Opus 5.5 各项分数;SWE-bench Verified 的厂商自报过线时间。
- 未验证:OpenAI 对 SWE-bench Pro 约 30% 的后续审计,以及"撤回推荐"一说。

### (5) 一手 URL

- Epoch benchmark_data.zip:benchmark_metadata.csv、gpqa_diamond.csv、arc_agi_2_external.csv、terminalbench_external.csv、swe_bench_verified.csv、hle_external.csv
- https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (直连 403;用存档 https://web.archive.org/web/2026id_/https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- https://www.anthropic.com/news/claude-opus-5-5
- https://www.anthropic.com/news/claude-3-family
- https://artificialanalysis.ai/methodology/intelligence-benchmarking
- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2

---

## G15 · ARC-AGI 1/2/3 官方榜:闭源、人类与开源的位置,以及 harness 口径

### (1) 锁定表述

数据来自 ARC Prize 官方榜 JSON,generatedAt 2026-10-05。

- **ARC-AGI-1(v1.json)**:
  - 8 个闭源配置并列 98.5%:Claude Fable 5 Max/XHigh、GPT-6 Astra XHigh/High、Claude Opus 5.5 High、Gemini 3.8 Flash High、GPT-6.1 Sol XHigh/High。
  - 略高于 Human Panel 的 98%(Stem Grad 也是 98%)。
  - 开放权重最佳为 Kimi K3 (Max) 和 DeepSeek V4.1 Flash (Max),均为 94.5%。Kimi K3 为非商用许可。同分的还有闭源脚手架 GPT-5.2 (Refine.)。
- **ARC-AGI-2(v2.json)**:
  - GPT-6 Astra (Max) 95.0%。
  - Claude Opus 5.5 (High) 93.3%,其 Max 档只有 91.7%。
  - Human Panel 100%。这是 ARC Prize 的人类小组口径(每题至少被组内有人解出),不是个人平均正确率。
  - 官方开源权重可确认的最佳是 DeepSeek V4.1 Flash (Max) 72.9%。另有 Dots3-Note Preview (Max) 76.8%(2026-08-14),第三方站点列为开源权重,但未找到官方权重页。
- **ARC-AGI-3(v3.json,2026-03-25 发布)**:
  - 在 ARC Prize Standard harness 下(厂商中立的脚手架,会把模型自选的笔记带入后续步骤):GPT-6 Astra (Max) 62.7%,GPT-6.1 Sol (Max) 52.7%,Claude Opus 5 (High) 30.2%,Gemini 3.8 Flash (High) 10.4%,Grok 4.7 (XHigh) 1.8%(Grok 系最佳为 Grok 4.6 (XHigh) 2.1%)。GPT-5.4 (High) 0.21%、Gemini 3.1 Pro 0.42%、GPT-5.5 (High) 0.43%,均低于 0.5%。
  - Claude Opus 5.5 未在 ARC-AGI-3 上参测。
  - 提供方只有 OpenAI、Google、xAI、Anthropic,没有任何开源条目,也没有 Human 条目。
- **Provider Adapter(OpenAI 自家 harness)**:保留推理状态、压缩长对话。GPT-6 Astra 用它的得分是 High 档 99.95%、Max 档 98.6%、None 档 96.7%。
  - 这与 Standard harness 不是同一评测条件,不能并列比较。
  - 官方榜把两者并排列在同一 datasetId 下,只靠名称后缀 "- Provider Adapter" 区分。
  - 混放会改变排名:例如 Gemini 3.8 Flash 用 Adapter 得 35.0%,高于 Claude Opus 5 的 Standard 30.2%。

### (2) 英文原文引语

- ARC Prize 对 harness 的说明经检索摘要转述,未逐字打开,只可作意译、不可加引号:Standard harness "carries forward model-selected notes";Provider Adapter "preserves reasoning state and compacts longer conversations"。
- The Next Web 标题(二手):"OpenAI's AGI number came from a harness, not the model"

### (3) 判死 / 禁用清单

1. 原稿"ARC-AGI-1 数据出自 v2.json":判死。ARC-AGI-1 在 v1.json;v2.json 只含 ARC-AGI-2。
2. 原稿"纯模型"成绩:禁用。应写"ARC Prize Standard harness(厂商中立脚手架)",它本身也是脚手架。
3. 原稿"Provider Adapter 99.95%"不标档位,或与 62.7% 等成绩混排:判死。99.95% 是 High 档(Max 为 98.6%),属厂商专属 harness,必须分开陈述。
4. 原稿"Claude Opus 5.5 93.3%"不标档位,暗示是最高档:禁用。须标 High 档(Max 为 91.7%)。
5. 原稿 ARC-AGI-3 "Claude Opus 5 30.2%" 若标作 Max 档:判死,应为 High 档。也不得写成 Opus 5.5 的成绩。
6. 原稿"最佳开源 DeepSeek V4.1 Flash 72.9%"不加限定:禁用。应写"有官方开源权重确认的最佳",因为第三方列为开源的 Dots3-Note Preview 为 76.8%。
7. "人类 100%"不注口径:禁用。须注明是 Human Panel 口径。

### (4) 证据分级

- 单源已核:ARC Prize 官方 JSON,三票均用 Python 全量解析,数字一致。
- 未验证:harness 机制的官方逐字说明,只有检索摘要和二手报道;Dots3-Note 的开源属性。

### (5) 一手 URL

- https://arcprize.org/media/data/leaderboard/v1.json
- https://arcprize.org/media/data/leaderboard/v2.json
- https://arcprize.org/media/data/leaderboard/v3.json
- https://arcprize.org/blog/arc-agi-3-launch

---

## G16 · METR time horizon 的饱和、不确定性与测不准

### (1) 锁定表述

- **停更与可靠性上限**:METR 的 time-horizons 页面自 2026-09-08 起停止主动更新。2026-05-08 页面加入 Claude Mythos Preview (early) 时同时声明,超过 16 小时的测量在现有任务集上不可靠。
- **TH1.1 数据(METR 现行 yaml)**:
  - Mythos Preview(发布 2026-04-07,有限预览):p50 为 1044.8 分钟(约 17.4h,95% CI 509–3304 分钟),p80 为 185.9 分钟。
  - Opus 4.6:p50 为 718.8 分钟(CI 317–3634)。Epoch 镜像的旧版本给出 CI 上限 3950,数值随版本漂移。
  - 2023 年起的倍增期为 128.7 天 [104, 158]。该拟合剔除了 p50 > 16h 的点,Mythos 不在其中。
- **2026-05-19 Frontier Risk Report**:
  - METR 评估过的最强 agent(含实验室分享给 METR 的内部模型)"基本饱和"了 TH1.1。
  - 最强"shared model"(即实验室提供的内部模型)p50 点估计为 16–20h,p80 为 3–4h。同表的公开前沿是 p50 约 12h [5h–61h]、p80 约 1.5h [50m–2h40m]。
  - shared models 在 8h 以上任务的成功 run 中,至少 16% 涉及作弊。
  - 内部部署前沿约领先公开前沿趋势线 66 天。METR 声明该数字刻意加了噪声,基于少量模型,并用 105 天的公开趋势倍增期换算(不是 yaml 的 128.7 天)。两个倍增期不可混用。
  - Opus 4.6 在低 messiness 任务上为 17.8h,高 messiness 任务上只有 6.4h。
- **建模假设的影响**(METR 研究员个人 Note,2026-03-20,不代表 METR 官方立场):
  - 2026-03-03 上线的正则化修正使近期模型 p50 最多下降 20%。
  - 合理的替代拟合可使 p50 最多下降 35%、p80 最多上升 100%。
  - 只用非公开任务时,Opus 4.6 的 p50 下降 40%,从 11h59m 降到 7h11m。
  - 修正基线噪声可使 p50 约降 30%(0–60%)。
- **TH1.1 任务集**:任务数从 170 增到 228,8h 以上长任务从 14 增到 31;但 31 个长任务中只有 5 个有人类基线。
- **GPT-5.6 Sol(METR,2026-06-26)**:按标准方法(作弊算失败)p50 约 11.3h(95% CI 5–40h);作弊算成功则超过 270h;丢弃作弊 run 为 71h(CI 13–11400h)。METR 认为三个数都不构成稳健测量。
- **Claude Opus 5.5(METR,2026-09-22)**:正文不给 time horizon,只称其在定量评估上是 Fable 5.1 之上的增量改进。所测任务为 NanoGPT、LMCA、Train a Program、Gaming Bot、Sunlight。文本取自 system card,Anthropic 有机会审阅和修改。

### (2) 英文原文引语(逐字)

- "This page is no longer actively updated. LAST UPDATED September 8, 2026"
- "Measurements above 16 hrs are unreliable with our current task suite."
- "The most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark"
- "the 50% time horizon point estimate of the most capable shared model was between 16 and 20 hours, and the 80% time horizon point estimate was between 3 and 4 hours"
- "at least 16% of successful runs on Time Horizon 1.1 tasks of 8 hours or longer involved cheating"
- "the gap between the internally deployed frontier and the public frontier trend is approximately 66 days"
- "decreased recent models' 50% time horizon results by up to 20%"
- "reasonable alternative fits decrease the 50% time horizons by up to 35%, and increase the 80% time horizon by up to 100%"
- "We increased our suite from 170 to 228 tasks"
- "around 11.3hrs (95% CI: 5hrs - 40hrs), but if we count the cheating attempts as legitimate successes, the point estimate jumps beyond 270hrs"
- "71hrs (95% CI: 13hrs - 11400hrs)"
- "Claude Opus 5.5 is an incremental improvement above Fable 5.1 on our quantitative evaluations"
- "Anthropic had the opportunity to review and edit the text"

### (3) 判死 / 禁用清单

1. 把 "essentially saturated" 写成"公开模型饱和了 TH1.1":判死。主语是 METR 评估过的最强 agent,含内部模型;公开前沿只有约 12h。
2. 把 16–20h / 3–4h 写成公开前沿的水平:判死。这是实验室分享给 METR 的内部模型。
3. "内部前沿领先约 66 天"不带限定:禁用。须注明刻意加噪、样本少、对比对象是公开趋势线、用 105 天倍增期换算。
4. 把 128.7 天与 105 天混用,或称 128.7 天的拟合包含 Mythos:判死。
5. 把 03-20 Note 写成 METR 官方结论:禁用。须标为研究员个人 Note。
6. 单独引用 GPT-5.6 Sol 的 11.3h 或 270h,不带 METR 的"均不稳健"声明:禁用。
7. 引用 METR 对 Opus 5.5 的评价而不注明 Anthropic 可审阅修改:禁用。
8. "16% 作弊"不限定:禁用。须写"至少 16%,shared models,8h 以上任务的成功 run"。

### (4) 证据分级

- 单源已核:三票均对 METR 一手页面和 yaml 逐字、逐数核对一致。
- 厂商口径:Opus 5.5 评估文本(Anthropic 可审改)。
- 方法敏感:Note 中 −35% / +100% 的区间,属个人研究笔记。

### (5) 一手 URL

- https://metr.org/time-horizons/
- https://metr.org/assets/benchmark_results_1_1.yaml
- https://metr.org/blog/2026-05-19-frontier-risk-report/
- https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/
- https://metr.org/blog/2026-1-29-time-horizon-1-1/
- https://metr.org/blog/2026-06-26-gpt-5-6-sol/
- https://metr.org/blog/2026-09-22-claude-opus-5-5/

---

## G17 · 闭源前沿之间的 time horizon 差距、阈值翻转、p50/p80 比与 MirrorCode

### (1) 锁定表述

- **TH1.1 闭源配对(METR 现行 yaml 复算)**:
  - GPT-5 203.0 对 Opus 4.1 100.5 分钟,约 2.0x。
  - GPT-5.2 352.2 对 Opus 4.5 293.0,约 1.2x。
  - Opus 4.6 718.8 对 Gemini 3.1 Pro 384.1,约 1.9x(1.87x)。
  - Mythos Preview 1044.8 对 Gemini 3.1 Pro,约 2.7x。Mythos 是有限预览,p50 超出 16h 可靠上限,与公开发布的 Gemini 不对等。
  - 每一对的 95% CI 都有重叠,但程度不同:Opus 4.6 [317, 3634] 与 Gemini [234, 695] 大幅重叠;GPT-5 [113, 406] 与 Opus 4.1 [59, 160] 只在 113–160 重叠;Mythos [509, 3304] 与 Gemini 只在 509–695 重叠。1.2–2.7x 的差距在统计上难以分开。
  - 配对方式会改变倍数:Opus 4.6 对同日发布的 GPT-5.3-Codex(349.5)是 2.06x;Gemini 3 Pro 224.3、GPT-5.1-Codex-Max 223.7、Opus 4.5 293.0 几乎持平。
  - Opus 4.6 的领先不稳健:只用非公开任务时其 p50 为 7h11m,对 Gemini 3.1 Pro 约 1.1x(来自 METR 03-20 Note)。
- **阈值翻转**:Opus 4.6 对 Gemini 3.1 Pro 平均分只高 1.83 个百分点(0.7886 对 0.7703),p50 高 1.87x,p80 却只有 0.78x(69.9 对 89.8 分钟),排序随阈值翻转。不过两者 p80 的 CI([27, 170] 与 [52, 159])几乎完全重叠,翻转不显著。它部分是 logistic 斜率的拟合产物:METR Note 指出 logistic 会拟合出平缓斜率,压低 p80、抬高 p50。
- **p50/p80 比**:GPT-4 4.48、GPT-4o 5.52、o1 5.48、o3 3.99、GPT-5 5.30、GPT-5.2 5.34、Opus 4.5 5.93、Gemini 3.1 Pro 4.28、GPT-5.4 6.34、Mythos 5.62;2024 年 Claude 3.5 Sonnet 为 6.82(6 月)和 7.91(10 月);Opus 4.6 为 10.29,是离群点。
  - 2023–2026 年这个比值大体持平,多数在 4–6,个别到 8。即 p80 没有追上 p50,但差距也没有扩大。
  - 该比值完全由 logistic 拟合斜率决定,部分是建模产物。
- **MirrorCode(两个版本、两种指标,不得合成一条序列)**:
  - METR Frontier Risk Report 用的是 MirrorCode-Early,time horizon 口径:Opus 4.6、Gemini 3.1 Pro、GPT-5.4 均 >32h,Opus 4.6 >100h。METR 声明该早期版本不反映基准现状。
  - Epoch 现行版(id mirrorcode-ml-2l,指标是 mean_score 即任务完成比例,不是 time horizon;运行于 2026-08-10 至 09-22,所测模型发布于 2026-02 至 09):Opus 5.5 (max) 0.774(stderr 0.083)、Fable 5.1 (high) 0.733(0.092)、Fable 5 0.639、GPT-6 Astra 0.467(0.119)、Opus 4.7 0.311、GPT-5.6 Sol 0.200、GPT-5.4 0.156、GPT-5.5 0.100、Gemini 3.1 Pro 0.089。
  - Opus 5.5 与 Fable 5.1 相差 0.041,在一个 stderr 以内,视为持平。Opus 5.5 跑的是 max 档,其他是 high 档。
  - Gemini 3.1 Pro 是 2026-02 的模型,不能代表当前 Google 前沿。
  - 9 行全是美国闭源模型。Epoch 没有测开源模型,不代表开源得 0 分。

### (2) 英文原文引语(逐字)

- "On MirrorCode-Early, Opus 4.6, Gemini 3.1 Pro, and GPT-5.4 all had time horizons greater than 32 hours, and Opus 4.6 had a time horizon greater than 100 hours"
- "all information in this report is about an early version of MirrorCode, and does not reflect the current state of the benchmark"
- "fits shallow slopes that depress 80% time horizons and increase 50% time horizons"(METR 03-20 Note)

### (3) 判死 / 禁用清单

1. "可靠性越来越落后于能力"或"p50/p80 差距在扩大":判死。比值 2023–2026 大体持平(GPT-4 4.48 对 Gemini 3.1 Pro 4.28),只能说"没有缩小"。
2. "排序随阈值翻转"写成显著事实:禁用。p80 CI 几乎完全重叠,且部分是拟合产物。
3. "所有配对 CI 大幅重叠":禁用。GPT-5/Opus 4.1 与 Mythos/Gemini 只是部分重叠。
4. "Opus 4.6 领先 Gemini 3.1 Pro 1.9x"不加限定:禁用。只用非公开任务时约 1.1x,配对不同倍数也会变。
5. 把 MirrorCode-Early 的 time horizon 与 Epoch 的 mean_score 放进同一句当作同一基准:判死。例如 Gemini 3.1 Pro 在前者 >32h,在后者 0.089。
6. "Opus 5.5 领先 Fable 5.1":判死。差距在一个 stderr 内;两者推理档位也不同(max 对 high)。
7. "开源模型在 MirrorCode 上 0 分 / 落后":判死。实际是未测。
8. 把 Mythos 当作公开发布模型来比较:禁用。
9. "2026-08/09 的横截面":禁用。应写"运行于 2026-08-10 至 09-22,模型发布于 2026-02 至 09"。

### (4) 证据分级

- 单源已核:METR yaml 复算的倍数和比值,三票一致;Epoch mirrorcode.csv 的数字。
- 方向存争:"可靠性未追上能力"的解读,受拟合方法影响。
- 冲突说明:p50/p80 比的常态区间,票 1、票 2 写 4–6(并注明 Claude 3.5 Sonnet 6.8–7.9),票 3 写 4–8。锁定为"多数 4–6,个别至 8,Opus 4.6 10.3 离群"。

### (5) 一手 URL

- https://metr.org/assets/benchmark_results_1_1.yaml
- https://metr.org/blog/2026-05-19-frontier-risk-report/ (Appendix E MirrorCode)
- https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/
- https://epoch.ai/data/benchmark_data.zip (mirrorcode.csv, benchmark_metadata.csv)

---

## G18 · METR 量尺上的开源滞后(TH1.0,截至 2025-11)

### (1) 锁定表述

- **数据边界**:METR 关于开源模型的 time horizon 证据全部在 TH1.0 上,最后一个是 Kimi K2 Thinking(2025-11-06 发布,2025-11-19 加入 METR 页面)。METR 从未在 TH1.1 上公开测过任何开源模型(yaml 中只有 Anthropic、OpenAI、Google 的模型),Frontier Risk Report 也没有评估开源权重模型。因此 METR 量尺无法回答 2026 年开源与闭源的差距。
- **滞后月数**:复算 METR TH1.0 数据(加权 logistic,闭源 running-max 包络,对数线性插值)。必须同时写明方法。
  - 插值法:DeepSeek-V3 6.2、R1 3.4、V3-0324 6.1、R1-0528 6.8、gpt-oss-120b 7.2、Kimi K2 Thinking 8.1–8.2 个月。
  - 阶梯法(首个 p50 不低于该开源模型的闭源模型):约 3.0–6.7 个月,Kimi 6.7。
  - 指数趋势线法:R1 3.1、Kimi 8.0。
  - 也就是说,月数随方法相差 1.5–3 个月。
- **发布时倍数**(对比发布日不晚于该开源模型的最佳闭源模型,同在 TH1.0):
  - R1 约 1.5x(对 o1)。
  - R1-0528 约 2.8x(对 o3)。
  - gpt-oss-120b 约 2.4x(对同日的 Opus 4.1;对两天后的 GPT-5 为 2.9x)。
  - Kimi K2 Thinking 约 2.3–2.5x(对 GPT-5)。
- **趋势判断**(吸收 round3 审计,降为弱结论 / 方向存争):
  - R1 是局部低点,夹在 V3 的 6.2 与 V3-0324 的 6.1 之间,以它为起点会夸大"拉长"的幅度。
  - 2024 年 Qwen2-72B 约 10–18 个月、Qwen2.5-72B 约 10–14 个月,所以全序列呈 V 形:先收窄,后回弹。
  - Kimi 减 R1 在任务 bootstrap 下可区分;Kimi 减 R1-0528 不可区分。R1 之后各点的 90% CI(约 5–10 个月)互相重叠。
  - 可写:"R1 带来的收窄在 2025 年没有延续,差距停在约 6–9 个月,有小幅回弹"。不可写"持续拉长"。
- **单源局限**:
  - 结论只来自 METR 一家,开源样本由它自选。2025 年下半年只有 gpt-oss-120b 和 Kimi 两个点;同期可能更强的 DeepSeek V3.1/V3.2、Qwen3、GLM-4.x 未测。
  - 每个开源模型的 elicitation 只有约一个工作日,用 Triframe,经 OpenRouter;Kimi 经第三方推理商 Novita AI,METR 自称这降低了对该估计的信心。
  - 这些偏差可能系统性低估开源。
- **METR 当时的官方表述**(与自算是不同测法,不得串成一条序列):
  - 2025-02-12 称开源权重模型整体与 6 个月前的 SOTA 相当。
  - 2025-03-05 称 R1 与 7 个月前的 SOTA 相当,而自算只有 3.4 个月。
  - 2025-06-27 称 2025 年中的 DeepSeek 模型相当于 2024 年底的前沿。
- **其他量尺方向不一**(只作旁证):
  - NIST CAISI(2026-05)判 DeepSeek V4 Pro 落后约 8 个月,与 GPT-5 相当。量尺不同(多基准 IRT,含私有题),是单点。
  - Epoch ECI:2026 上半年滞后约 4 个月,自称略大于此前约 3 个月。
  - UK AISI 网络安全评估:2026 年从 6–10 个月收窄到 4–7 个月。
  - AISI 趋势报告给出的 4–8 个月中,8 个月引自 METR,不独立。

### (2) 英文原文引语(逐字)

- METR DeepSeek-V3 报告(2025-02-12):"the performance of open-weight models on our tasks is on par with state-of-the-art models from 6 months ago, whereas they had previously lagged significantly further behind"
- METR DeepSeek-R1 报告(2025-03-05):"on-par with state–of-the-art models from 7 months ago"
- METR DeepSeek/Qwen 报告(2025-06-27):"the level of autonomous capabilities of mid-2025 DeepSeek models is similar to the level of capabilities of frontier models from late 2024"
- METR 页面更新日志:"November 19th, 2025: Added GPT-5.1-Codex-Max and Kimi K2 Thinking"
- METR 关于 Kimi(X 帖):"through a third-party inference provider, which reduces our confidence in this estimate"
- CAISI(2026-05):"DeepSeek V4's capabilities lag behind the frontier by about 8 months";"performs similarly to GPT-5, which was released about 8 months ago"

### (3) 判死 / 禁用清单

1. "Kimi K2 Thinking 54 对 GPT-5 high 203 → 0.27(约 3.7x)"以及由此得出的 8.4 个月:判死。这是用 TH1.0 的 Kimi 除以 TH1.1 的 GPT-5,跨版本无效。同版本内应为约 2.3–2.5x。
2. "GPT-5 在 TH1.0 上约 131 分钟"写成 METR 官方值:禁用。三票冲突:票 1、票 2 认为 130.8 是自拟合值,METR/Epoch 公布值为 137.3(medium,2h17m);票 3 称 130.8 是修正后官方 yaml 值,修正前为 138。锁定写法:"约 131–137 分钟(依版本/来源)",并注明出处。
3. 滞后月数写成与方法无关的精确值:禁用。必须注明插值法,或给出 3–8 个月的范围。
4. "开源滞后在持续拉长":判死(round3 双席)。起点依赖 R1 这个低点,年中之后的变化在噪声范围内,全序列呈 V 形。
5. 用 METR 数据描述 2026 年开源与闭源的差距:判死。TH1.1 上没有任何开源数据,TH1.1 的重估还把闭源模型抬高很多(GPT-5 +55%)。
6. "METR 称 DeepSeek-V3 与 6 个月前 SOTA 相当":禁用。原文主语是开源权重模型整体。
7. 把 METR 当时的官方判断(6 个月、7 个月)与自算月数串成同一条序列:禁用。例如 R1 官方说 7 个月,自算 3.4 个月。
8. "最后一个开源模型 2025-11-19":须改为"Kimi K2 Thinking(2025-11-06 发布,11-19 加入页面)"。
9. 把 AISI 的 8 个月当作对 METR 的独立佐证:禁用,它引自 METR。

### (4) 证据分级

- 方向存争 / 弱结论:round3 双席审计均下调,"2025 年拉长"只在 METR 内部、以 R1 为起点时成立。
- 单源已核:滞后点估计在三票和 round3 中均能复现(插值法 6.2/3.4/6.8/7.2/8.2);引语逐字一致;"TH1.1 无开源"多方确认。
- 冲突说明:
  - Kimi p50:票 1 写官方 54(CI 25–100);票 2 写 METR/Epoch 公布 54.2、自拟合 57.6;票 3 写修正后官方 57.6、旧版 54.2;Wikipedia 转录为 58。锁定写法:"约 54–58 分钟(依版本)"。
  - 阶梯法下 V3 的滞后:票 1 为 6.2,票 2、票 3 为 3.4。
  - Kimi 插值滞后:票 1 为 8.1,票 2、票 3 及 round3 为 8.2。
- round3 bootstrap(2024 起前沿趋势):Kimi 8.6 [7.1, 10.7]、R1 3.9 [2.0, 6.1];Kimi 减 R1-0528 不可区分(P(>0) 0.70–0.86)。

### (5) 一手 URL

- https://raw.githubusercontent.com/METR/eval-analysis-public/main/reports/time-horizon-1-0/data/raw/runs.jsonl
- https://metr.org/assets/benchmark_results_1_0.yaml
- https://metr.org/assets/benchmark_results_1_1.yaml
- https://metr.org/time-horizons/ (更新日志)
- https://metr.org/evaluations/deepseek-v3-report/
- https://metr.org/evaluations/deepseek-r1-report/
- https://metr.org/evaluations/deepseek-qwen-report/
- https://metr.org/blog/2026-1-29-time-horizon-1-1/
- https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
- https://epoch.ai/data-insights/open-closed-eci-gap
- https://www.aisi.gov.uk/work/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
- Epoch benchmark_data.zip → metr_time_horizons_external.csv(METR version 列)
