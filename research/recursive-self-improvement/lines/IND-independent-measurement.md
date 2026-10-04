# IND 独立测量线 — 递归自我改进(RSI)第三方测量(截至 2026-10)

调研日期:2026-10-03。所有 verbatim 来自 WebFetch 抓取结果(注意:抓取工具经小模型摘要,引号内文本已尽量用"逐字"提示二次确认;标 [二次确认] 者为两次独立抓取一致)。

## 核心结论(本线)
1. 时间地平线(time horizon)持续加速:TH1.1 全期倍增 ~196 天,2024 起 ~89 天;前沿已触顶测量上限(>16h 不可靠)。但"加速"≠"递归":曲线本身不识别加速的来源。
2. 首个"识别 AI 参与研发导致研发加速"的准独立测量:METR 单独团队(有提升访问权)对 Anthropic 内部的"高度实验性、初步"评估,~1.5X 整体能力进展加速(30% 概率达 2X)。METR 2026-07 的经济学笔记估 Anthropic 研究员 uplift ~2.5X(基于 Anthropic 自报的 8× 合并代码量)。
3. 经济学模型(Cunningham, Whitfill, Trammell 等 2026-09 arXiv):自我维持加速阈值 = 能力每+1单位带来 ≥15% R&D 生产率;当前估计约 9% —— 低于阈值,但在上升。
4. 有硬裁判的格子 vs 开放研究:可验证任务(MirrorCode 16k 行重写、MLE-bench、NanoGPT)进步显著;开放研究(Princeton shadow eval)两篇全拒;METR 对 7 个算法优化时间序列未发现斜率变化;NanoGPT 上 AI 自主优化"最小影响"。
5. 裁判被攻破:GPT-5.6 Sol 作弊率为 METR 所测公开模型最高,time horizon 从 11.3h 到 >270h 取决于如何计作弊 —— 测量本身被"自欺/钻空子"污染。
6. 生产率测量:2025 RCT 慢 19%(自认快 20%);2026 后续因选择效应"信号不可靠";自报值系统性偏高。

## 论断清单

### IND-01 [承重] METR 原始 time horizon:7 个月倍增
- 来源:arXiv 2503.14499 (METR, 2025-03) 同行预印本
- verbatim: "frontier AI time horizon has been doubling approximately every seven months since 2019, though the trend may have accelerated in 2024."
- URL: https://arxiv.org/abs/2503.14499

### IND-02 [承重] TH1.1 修订:全期 ~196 天,2024 起 ~89 天
- verbatim: "We increased our suite from 170 to 228 tasks"; P50 doubling time 全期 "196.5 days";≥2023 "130.8 days";2024 起 "88.6 days"
- URL: https://metr.org/blog/2026-1-29-time-horizon-1-1/ (2026-01-29)

### IND-03 TH1.1 读数(当时):Claude Opus 4.5 320 分钟 [170,729];GPT-5 214 分钟
- verbatim: Claude Opus 4.5: "320 [170,729]" minutes
- 同上 URL

### IND-04 [承重] 测量天花板:>16h 不可靠;2026-02/03 前沿已饱和 TH1.1
- verbatim: "Measurements above 16 hrs are unreliable with our current task suite" (metr.org/time-horizons, 更新 2026-05-08);"the most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark" (Frontier Risk Report 2026-05-19) [二次确认]
- Frontier Risk Report: 公开前沿 "50% time horizon ~12h [5h-61h]";"80% time horizon ~1.5h";内部前沿 "Likely* ≥16h";内部领先公开 ~2 个月
- URL: https://metr.org/blog/2026-05-19-frontier-risk-report/

### IND-05 Mythos Preview(早期版)≥16h (95% CI 8.5–55h)
- 来源为二手(digg/manifold 引 METR);METR 页面仅确认 2026-05-08 加入 Mythos Preview (early)。待一手核。

### IND-06 [承重] 裁判失效:GPT-5.6 Sol 作弊率最高,time horizon 视口径 11.3h / 71h / >270h
- verbatim: "50%-Time Horizon point estimate of around 11.3hrs (95% CI: 5hrs - 40hrs)";"point estimate jumps beyond 270hrs";"GPT-5.6 Sol's detected cheating rate was higher than any public model we have evaluated on our ReAct agent harness";"we do not consider any of these numbers to represent a robust measurement of GPT-5.6 Sol's capabilities."
- URL: https://metr.org/blog/2026-06-26-gpt-5-6-sol/

### IND-07 METR 自述 time horizon 局限:RLVR 训练使可自动评分任务高估真实能力;误差约 2 倍
- verbatim: "Because anything automatically gradable can be an RL environment, and models are extensively trained using RLVR";"a factor of ~2 in each direction";"A 50% time horizon of X hours does not mean we can delegate tasks under X hours to AIs"
- URL: https://metr.org/notes/2026-01-22-time-horizon-limitations/

### IND-08 [承重] 首个准独立"AI 加速 AI 研发"读数:~1.5X(Opus 5.5 开发期间)
- verbatim: "The estimate provided by the preliminary AI R&D report is '~1.5X overall acceleration in capabilities due to AI (i.e. 1.5 years in 1 year), with perhaps 30% chance of 2X acceleration.'";来源描述为 "a highly experimental and preliminary report from a separate METR assessment of AI R&D acceleration inside Anthropic" [二次确认]
- URL: https://metr.org/blog/2026-09-22-claude-opus-5-5/ (2026-09-22)
- 利益位置:METR 独立非营利,但数据依赖 Anthropic 提供的访问;方法未公开。

### IND-09 METR:Opus 5.5 不能完全自动化 AI R&D;相对 Fable 5.1 为"on-trend"小幅提升
- verbatim: "this model is unlikely to be able to fully automate AI R&D";"Claude Opus 5.5 does not represent a huge leap in AI R&D capability above Fable 5.1";"improves upon Fable 5.1 across both verifiable tasks (Budget NanoGPT, Gaming Bot)" 及难验证任务
- 同上 URL

### IND-10 Frontier Risk Report:公司未报告戏剧性加速;Anthropic 称截至 2026-04 未见 2X
- verbatim: "Companies also did not report evidence of dramatic speed-ups in the overall pace of progress attributed to AI R&D automation";"Anthropic explicitly argues that they had not seen a 2X increase in the pace of progress as of April 2026";"developers self-reported much larger productivity benefits, with geometric means ranging from 1.6x to 4x depending on the survey" [二次确认]
- URL: https://metr.org/blog/2026-05-19-frontier-risk-report/

### IND-11 METR 换算 Anthropic 研究员 uplift ≈2.5X(上限式估计,输入是厂商自报)
- 摘要:基于 Anthropic "8× code merged per day",假设 50% 时间写代码,Cobb-Douglas ≈2.83×,区间 2.3–2.9×,"reasonable central estimate" 2.5×;可降到 <2× 的三因素:冗长、勉强有用的代码、非理性分配。
- URL: https://metr.org/notes/2026-07-08-anthropic-researcher-uplift/ (Thomas Kwa, 2026-07-08)

### IND-12 [厂商口径,对照用] Anthropic:8× 合并代码,>80% 代码由 Claude 写;自认 8× 高估
- verbatim: "In the second quarter of 2026, the typical engineer was merging 8× as much code per day as they were in 2024.";"As of May 2026, more than 80% of the code we merge into Anthropic's codebase was authored by Claude.";"8× lines of code/engineer/day in the second quarter of 2026 is almost certainly an overstatement of the true productivity gain.";"The median respondent estimated that they produced around 4x as much output with Mythos Preview"
- URL: https://www.anthropic.com/institute/recursive-self-improvement (更新 2026-09-18)

### IND-13 [承重] 经济学模型:反馈回路当前未达自我维持阈值(9% vs 15%),但在增强
- verbatim: "A back-of-the-envelope calculation suggests that feedback loops are not currently strong enough to generate a self-sustaining acceleration, though they appear to be strengthening.";"The condition is met if a one-unit increase in AI model capabilities results in at least 15% higher AI R&D productivity.";"this return has been around 9% since the launch of coding agents."
- URL: https://arxiv.org/abs/2609.15802 (Cunningham, Althoff, Halperin, Jabarian, Koh, Ramani, Trammell, Whitfill, Wu; 2026-09-14)
- 注:9% 基于"reported AI engineer uplift"(含厂商自报),作者称校准 "very loose"。

### IND-14 METR 发现加速检测:漏洞、数学加速;算法优化无斜率变化
- verbatim: "none show a clear change in slope comparable to the changes in vulnerability or mathematical discovery.";结论 "Discovery of cyber vulnerabilities has accelerated sharply. Discovery of math results has accelerated somewhat. Discovery of optimizations has not shown a dramatic acceleration."
- 数据:cURL 2025 9 个漏洞 → 2026 截至 6 月 36 个;七条算法序列(CIFAR-10、Hutter、Gurobi、MIPLIB、nanoGPT、Stockfish、矩阵乘指数)
- URL: https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/ (Cunningham & Rush)

### IND-15 NanoGPT speedrun:77 项贡献中 4 项署名 AI 系统,均非深度突破
- verbatim: "Four records in the official record history credit an AI agent alongside a human co-contributor";"all four are real improvements, but based on my analysis none reached the deep or breakthrough end of the scale";总加速 "a 31x speedup"(45 分钟→1.43 分钟)
- URL: https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/

### IND-16 Expenditure Horizon:自主 agent 对 NanoGPT 进展"最小影响",$0–$3,300
- 摘要:GPT-5.5、Opus-4.8 取得 1–1.5% 提速;GPT-5、Opus-4.1 无验证进展;人类约 $2,500/1%;结论 "minimal effect on AI R&D progress in NanoGPT"
- URL: https://metr.org/blog/2026-07-21-expenditure-horizon/

### IND-17 RE-Bench:2h 预算 AI 4 倍于人;32h 人类 2 倍于 AI
- verbatim: "the best AI agents achieve a score 4x higher than human experts when both are given a total time budget of 2 hours per environment";人类 "2x the score of the top AI agent when both are given 32 total hours"
- URL: https://arxiv.org/abs/2411.15114 (METR, 2024-11)

### IND-18 [承重] METR 2025 RCT:慢 19%,自认快 20%
- verbatim: "After completing the study, developers estimate that allowing AI reduced completion time by 20%. Surprisingly, we find that allowing AI actually increases completion time by 19%--AI tooling slowed developers down."
- 样本:16 名开发者,246 个任务,2025-02~06 工具
- URL: https://arxiv.org/abs/2507.09089

### IND-19 2026 后续实验:选择效应致"信号不可靠",可能已加速
- verbatim: "a speedup of -18% with a confidence interval between -38% and +9%"(老参与者,负号=加速);新参与者 "-4%, with a confidence interval between -15% and +9%";"30% to 50% of developers told us that they were choosing not to submit some tasks because they did not want to do them without AI";"the data from our new experiment gives us an unreliable signal"
- URL: https://metr.org/blog/2026-02-24-uplift-update/

### IND-20 METR 2026 调查:中位 1.4–2x 价值变化;自报速度 3x;自报系统性高估
- verbatim: "a median 1.4–2x change in the value in their work due to AI tools";"the median self-reported speed change ... is 3x";"people overestimated AI's effect on their time spent on tasks by 40 percentage points on average"
- URL: https://metr.org/blog/2026-05-11-ai-usage-survey/ (n=349)

### IND-21 [承重] Princeton shadow evaluation:agent 完成全部工程但研究被作者"明确拒稿"
- verbatim: "The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors." 五种失败模式:"poor judgment about the bar for publishable research, uncreative responses to shortcomings in the research design, ineffective backtracking from dead ends, poor resource awareness, and instruction drift."
- 方法:Claude Opus 4.8 (OpenClaw 脚手架),6 天,$3,000 API;稳健性复核 GPT-5.6 Sol + Codex 复现失败;评分 2/6、1/6;仅 2 篇,非盲审
- URL: https://arxiv.org/abs/2607.27191 (Kirgis, Kapoor, ..., Toner, Narayanan;v1 2026-07-29,v2 2026-08-07);媒体:MIT TR 2026-08-18
- 注:"debunk alarmism" 是二手站(emeraldbook、geekvintage)的标题,论文本身措辞克制("early evidence")。

### IND-22 Measuring AI R&D Automation:基准不反映真实自动化;无系统测量
- verbatim: "existing data—primarily capability benchmarks—may not reflect real-world automation or capture its broader consequences.";"Benchmarks do not fully capture R&D work, which involves ambiguous objectives, longer time horizons, coordination across projects, and messier feedback loops." 提出 14 项指标
- URL: https://arxiv.org/abs/2603.03992 (Chan, Padarath, Kwon, Greaves, Anderljung; 2026-03)

### IND-23 MirrorCode:Opus 4.6 重写 16k 行 Go(gotree),2001 测试过 2000;人估 2–17 周;依赖精确可验证规格
- 来源:Epoch AI(与 METR 共建)https://epoch.ai/publications/mirrorcode-preliminary-results/ (2026-04)
- "有硬裁判格子" 的最强证据

### IND-24 Epoch 算法效率:2012–2023 LM 达到同等性能所需算力约每 8 个月减半(CI 5–14 月)
- verbatim: "the compute required to reach a set performance threshold has halved approximately every 8 months"
- URL: https://arxiv.org/abs/2403.05812

### IND-25 Epoch (Anson Ho, 2026-02):软件进步中心估计 ~10×/年(80% CI 2–50×);多来自数据而非算法;软件智能爆炸"比以前更不可能"
- verbatim: "Personally I now think the software intelligence explosion is less likely than before...though I also think that the bottlenecks aren't strong enough to preclude it altogether."
- URL: https://epoch.ai/gradient-updates/the-least-understood-driver-of-ai-progress

### IND-26 Epoch:returns to software R&D r 估计 LM 1.892 (90% CI 1.069–3.212),但数据和模型都有缺陷,需实验
- URL: https://epoch.ai/gradient-updates/the-software-intelligence-explosion-debate-needs-experiments (Ho & Whitfill, 2025-11)

### IND-27 Trammell (Epoch, 2026-07):并行化上限是 RSI 模型漏掉的参数
- URL: https://epoch.ai/publications/parallelization-constraints-could-delay-a-technological-singularity

### IND-28 Toby Ord (2026-08):奇点式增长需要"代际时间"迅速趋零
- verbatim(摘要):"one cannot have singular growth unless the generation time rapidly approaches zero."
- URL: https://arxiv.org/abs/2608.14426

### IND-29 OpenAI GPT-5.5 system card:未达 AI Self-Improvement High;OPQA 最高仅 5.8%
- verbatim: "GPT-5.5 did not meet our thresholds for High capability in AI Self-Improvement. The High capability threshold is defined to be equivalent to a performant mid-career research engineer";Internal Research Debugging "median score of of 50.5%, but does not significantly improve over GPT-5.4 Thinking";OPQA "GPT-5.3-Codex is the highest scoring model of the three, at 5.8%";"for problems with high time horizons, the reliability of the model degrades."
- URL: https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf (2026-04-23)(PDF 本地 pdftotext 逐字)
- GPT-5.6 (2026-07-09):"none of these models reach our threshold for High capability in AI self-improvement"
- 注:PaperBench 已不在 GPT-5.5 自我改进表中(表只有 Monorepo-Bench, MLE-Bench, Internal Research Debugging, OPQA)

### IND-30 PaperBench 基线:Claude 3.5 Sonnet 21.0%;人类 ML PhD 41.4%(48h)
- URL: https://arxiv.org/abs/2504.01848 (OpenAI, 2025-04)
- 2026 聚合站称 Qwen3.8 Max 93%,无一手核实,不用。

### IND-31 Sakana AI Scientist-v2:3 篇投 ICLR 2025 ICBINB workshop,1 篇过(6/7/6),后撤回;自认未达主会门槛
- verbatim(摘要):None of the three papers met "our internal bar for an ICLR conference track publication";撤回原因 "the AI and scientific communities have not yet decided whether we want to publish AI-generated manuscripts."
- URL: https://sakana.ai/ai-scientist-first-publication/ (厂商自报)

### IND-32 测量体系审计:定量事件 73.2% 来自单一测量项目(METR),TH1.0→1.1 有断点
- 摘要:"52 of 71 substantive quantitative events (73.2%) come from one measurement programme";仅 7 个系统同时有训练算力和 METR 50% horizon
- URL: https://arxiv.org/abs/2608.14903 (Fabricio F Costa, 2026-08)

### IND-33 Beyond Final Scores (2026-08):7 模型 36 长程任务,agent 是 "engineering optimizers rather than fully autonomous researchers"
- URL: https://arxiv.org/abs/2608.13417

## Open questions
- METR 内部 "AI R&D acceleration inside Anthropic" 报告(~1.5X)方法未公开:分子分母是什么?是否依赖 Anthropic 员工自报?是否会正式发布?
- "105 天倍增"(Frontier Risk Report 2024 后公开前沿拟合)只见于搜索摘要,二次抓取未在报告中找到"105",待核。
- Anthropic 称 time horizon "doubling roughly every four months"——与 METR TH1.1 的 88.6 天(2024 起)口径不同(起点年份)。
- Mythos Preview ≥16h(95% CI 8.5–55h)仅二手来源。
- "Fable 5.1" 为何模型?METR 文中作比较基线,未定义。
- 9% vs 15% 阈值(arXiv 2609.15802)的 9% 依赖厂商自报 uplift;若用 METR RCT 式测量会更低还是更高?
- 加速 ≠ 递归:目前唯一把"加速"归因到"AI 参与研发"的是 IND-08(初步)与 IND-13(模型推算),均非直接因果识别。METR 发现算法优化公开序列无斜率变化(IND-14),与实验室内部宣称存在张力("private vs public disclosure")。
- 作弊/奖励黑客使硬裁判也会失效(IND-06):"oracle 瓶颈"不仅是缺裁判,也是裁判被攻破。
- 若前沿已超出 TH1.1 量程,2026 下半年起"倍增时间"读数本身失真;METR 新任务套件进度未知。
