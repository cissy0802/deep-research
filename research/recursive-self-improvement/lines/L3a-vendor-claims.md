# L3a 厂商口径线 — "AI 参与 AI 研发"的厂商自述数字(截至 2026-10-03)

> 纪律:verbatim 均为实际读到的原文。Anthropic 两篇 Institute 文章、OpenAI 9/6 博文通过浏览器全文抓取逐字核对;Opus 5.5 system card 由 PDF pdftotext 抽取逐字核对。媒体转述的标"媒体转述"。

## A. Anthropic

### A1. Dario Amodei 2025-03-10 CFR 预测(一手:CFR 活动实录)
- 原话:"we are not far from the world—I think we'll be there in three to six months—where AI is writing 90 percent of the code. And then in twelve months, we may be in a world where AI is writing essentially all of the code."
- URL: https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic
- 口径:无分子分母;"the code"未指 Anthropic 内部还是全行业。同场附加限定:程序员仍需 specify conditions / overall app 设计。

### A2. Amodei 2025-10 Dreamforce 自称兑现(媒体转述)
- "Six months ago, I made this prediction that in six months, 90% of code would be written by AI models. But within Anthropic and within a number of companies that we work with, that is absolutely true."
- URL: https://officechai.com/ai/my-prediction-of-ai-writing-90-of-code-is-already-true-at-anthropic-anthropic-ceo-dario-amodei/ (转述,未找到官方实录)
- 被问是否全公司 90% 时承认"因团队而异"。

### A3. "When AI builds itself"(Anthropic Institute, Favaro & Clark, 2026-06-05;9/18 更新)
URL: https://www.anthropic.com/institute/recursive-self-improvement
- ">80%":"As of May 2026, more than 80% of the code we merge into Anthropic's codebase was authored by Claude." 基线:"Before Claude Code launched in research preview in February 2025, this number was in the low single digits."
- 分子/分母(脚注3):"Our >80% figure measures the share of lines merged to production that can be attributed to Claude. This is a more conservative measurement in two ways: our attribution pipeline has gaps, and the lines not attributed to Claude include auto-generated code and other artifacts that were not hand-written by humans either."
- 同脚注:"Anthropic leadership have publicly estimated that 90% or more of our code is written by Claude, including scripts and experimental code." → 90% 与 80% 是两个口径(含脚本/实验代码 vs 合并到生产的可归因行数)。
- 8x:"In the second quarter of 2026, the typical engineer was merging 8× as much code per day as they were in 2024." 自承:"8× lines of code/engineer/day in the second quarter of 2026 is almost certainly an overstatement of the true productivity gain."
- 内部调查 4x:"In a March 2026 poll of 130 employees from across Anthropic research teams, the median respondent estimated that they produced around 4x as much output with Mythos Preview..." + "We expect that the true degree of uplift in March was somewhat lower." 脚注引 METR:developer estimates ... can be overestimated。
- 训练代码加速任务:"In May 2025, Claude Opus 4 averaged a ~3x speedup over the starting code. By April 2026, Claude Mythos Preview was achieving ~52x." 脚注:"it should not be read as a real-world training speedup."  任务特性:"The goal and the success metrics are fixed in advance" ——硬裁判格子。
- 开放研究(弱到强监督):"Two human researchers, over about a week, recovered roughly 23% of that gap; the agents recovered 97% over 800 cumulative hours and used roughly $18,000 in compute." 限定:"the result didn't transfer cleanly to production-scale models, and humans still chose the problem and created the scoring rubric."
- 研究判断:"our best model in November 2025 (Opus 4.5) beat the human choice 51% of the time; in April 2026 (Mythos Preview), this grew to 64%." 样本 n=129 选的是人类走偏的时刻;对照组(人类本就走对的 127 个时刻)模型只在 ~20% 胜出;裁判是另一个 Claude。
- 开放任务成功率:"On the most open-ended tasks, Claude's success rate reached 76% in May 2026, up 50 percentage points in six months." 裁判:"Session success is determined by a Claude judge"。
- 瓶颈:"large performance gaps persist when it comes to Claude exercising judgement in choosing goals in both engineering and research."
- 复利论断:"Even if we suppose that Claude never achieves good research taste, a conservative reading of our evidence still implies compounding acceleration."
- Amdahl:"as we've begun to push more code around the organization, human code review has become a new bottleneck."
- "We are not there yet, and recursive self-improvement is not inevitable."

### A4. R&D Automation Index(Anthropic Institute, 2026-09-17,Favaro & Wright)
URL: https://www.anthropic.com/institute/measuring-pace-of-ai-development
- 结论原文:"As of August 2026, Claude is not operating fully autonomously for any measured subset of AI R&D work. Claude "leads" 26% of Anthropic's AI R&D work. The share of work at or above "AI collaborates" is above 90%."
- "lead" 定义(Epoch AI AL 量表):"In AL4, AI "leads": it can complete most of the task end-to-end from a high-level prompt, while the human supervises." AL3:"it can do large chunks of work under close human direction." 脚注:AL4 下 "Claude wouldn't deploy the fix" ——人做最终 ship 决定。
- 分母:2026 年 7 月每周随机抽各部门 20% 员工,Claude 研究 agent 读其 Slack/文档 → ~15,000 任务 → 542 节点树/378 叶;"we used the amount of person-time dedicated to that task as a proxy"(人时加权);"Each person gets one unit of weight per week, split evenly across the tasks they worked on that week." 打分:"An independent Claude judge then read the resulting evidence and assigned one of six automation levels"。
- 验证:"model-versus-human exact agreement was 59%, human-versus-human was 35%), and model and human ratings were within one level of each other 97% of the time." 自承:"we're using our own models to evaluate our systems, which could mean that the "judge" model could make the same kinds of errors as the model it is checking." "There remains real room for disagreement on borderline cases, such as where exactly "AI collaborates" ends and "AI leads" begins."
- 冻结篮子:"it does not, on its own, tell us whether new kinds of work are appearing that humans have shifted onto."
- 监控:"approximately 30,000 agents doing research and engineering work at Anthropic at any one time in our most-used internal platform"; "over a billion decisions ... August 2026 ... 0.002% of them (about 1 in 47,000) were blocked"。
- 算力:"about 6% of compute that went to AI R&D was allocated toward safety, and about 12% of compute that went to AI-driven AI R&D was allocated toward safety."(一周快照 7/13-7/20)
- 第三方:"We plan to embed independent third-party evaluators" ——尚未发生。
- "<1% in February 2026" 正文无此句(媒体普遍引用,可能来自图表);CSER 工作论文写作 "1% to 26% between March and August 2026" —— 口径不一致待核。

### A5. Claude Opus 5.5 System Card(2026-09-22)——厂商自己的"没有显著加速"判定
URL: https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf
- 阈值定义:"either (1) our models would be able to fully substitute for our entire set of Research Scientists and Research Engineers, at competitive costs (within a factor of five); or (2) there is "dramatic acceleration" of the pace of AI progress..."
- "our internal measures of AI-driven research acceleration ... do not show a sustained AI-attributable 2× acceleration in the pace of our progress, though some of these measures have moved"
- AECI:"the trend-break hypothesis yields a slope change from 14.4 to 22.2 points per year, with the fitted break in September 2025 and a 1.53x increase (95% range 1.20 to 1.82). The first hypothesis fits the data better, but under either reading the slope has not doubled." 一次性跳跃模型 "is a better fit to the data in 99 of 100 resampled fits"。
- CoBench 2.1:Opus 5.5 55.8%(vs Mythos 5.1 53.4%, Opus 5 53.2%),"p ≈ 0.2";替代研究员阈值 ≥85%。
- 不再跑自动 R&D 任务:"Recent models have crossed the highest human baselines for many of the automated task-based AI R&D evaluations ... results on such tasks are no longer a significant component of our ... capability threshold determinations." (饱和 = 格子内裁判失效)
- 定性短板:"internal users report that it mostly tests incremental ideas and prefers less ambitious hypotheses"; "has checked a plan against requirements it wrote itself rather than against the people the plan was designed to support"; 头号 flagged 行为 "asserting unverified inferences as established fact"。
- METR(外部,经 Anthropic 转载):"~1.5X overall acceleration in capabilities due to AI (i.e. 1.5 years in 1 year), with perhaps 30% chance of 2X acceleration." 但 METR 公开团队 "was not able to share the supporting evidence"; "the data we have is insufficient for distinguishing consistent, accelerating, or decelerating rates of improvement"; "full automation of AI R&D will require large improvements in foresight, prediction, creating one's own feedback loops ..."
- RSI 安全措施:"We have deployed safeguards on Claude Opus 5.5 for a narrow set of capabilities related to developing frontier LLMs, such as kernel development on certain ML accelerators"。

### A6. 自动对齐研究员 AAR(Anthropic Alignment Science, 2026-08-28)
URL: https://alignment.anthropic.com/2026/automated-alignment-researchers/ ; PDF https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf ; arXiv 2608.28945
- 标题限定 "Well-Characterized";TL;DR:"Automating alignment research on well-characterized failures may be practical in the near term."
- 局限:"Our results are limited to alignment tasks measurable with public benchmarks or automated auditing tools"; "These evaluations are also only proxies for deployment misalignment"; 不覆盖 "open-ended, hard-to-supervise research"。
- 规模:10 类失效(sycophancy/jailbreak/prompt injection/power seeking/deception/hallucination/social bias/privacy/reward hacking/concealing uncertainty),每次 "about 30 minutes on one H200 GPU";对比 28 名人类安全研究员,在人类提出方案的 7 类上 "The best AAR method closes more of the safety headroom than the best human idea"。
- (经 WebFetch 摘要获取,未逐字二次确认 PDF;建议终稿前复核)

### A7. 2026-09-12 Amodei《We Must Pace the Frontier》
URL: https://darioamodei.com/post/we-must-pace-the-frontier
- "since roughly this summer, AI has been advancing drastically faster, driven primarily by AI's growing ability to build the next generation of AI."
- 文中无量化证据(WebFetch 摘要判断)。与 10 天后 system card "slope has not doubled"/"no sustained 2×" 存在张力。

## B. OpenAI

### B1. Altman 2025-10-28 目标(X 帖,一手)
- "We have set internal goals of having an automated AI research intern by September of 2026 running on hundreds of thousands of GPUs, and a true automated AI researcher by March of 2028. We may totally fail at this goal..."
- URL: https://x.com/sama/status/1983584366547829073 (搜索结果标题文本)

### B2. 2026-09-06《Research acceleration: The view inside OpenAI》(浏览器全文抓取)
URL: https://openai.com/index/research-acceleration-view-inside-openai/
- "According to our measurements, we have now reached the goal, announced last fall, of having an automated research intern by September of this year. By "research intern," we mean a system that can carry out well-defined research tasks under human direction, including tasks that would take a skilled researcher a few days."
- 3.1:"as of mid-August, in total, the research organization uses 3.1 agent-workdays of effort for every workday of human labor." —— 分子是 agent 运行时(按 8h 折算),不是产出;"Before June 2026, total agent runtime across the research organization was still below that of total human labor."
- token:"the median researcher was integrating agents daily into their work, using more than $600 per day of inference at API prices. The 90th percentile user ... more than $7,000 of tokens per day."
- 干预:"agents still require significant human steering to be successful, especially as task complexity rises. In the last 6 months, over half of successful 4-8 hour tasks involved 1 or more interventions." 成功率只统计 "tasks we can find a ground truth outcome for"。
- 规划占比:"High-level planning still remains a minimal fraction of agent output tokens."
- 自承解释难:"AI research is a complex process with many potential bottlenecks, so the overall pace of progress likely won't keep pace with these specific metrics." "These data points are relatively easy to measure, but can be hard to interpret. As automation progresses, the tasks which are least automatable will take on a larger share of researcher effort..."
- 混杂:"This is correlated with increased Codex adoption, though we note that our available compute has also grown significantly since 2025."
- 人的角色:"People still set our research priorities, judge which ideas and results to pursue, and decide whether to scale, pause, or deploy systems."
- RSI 立场:"We do not yet know how to safely get all the way to aligned, full RSI."
- Hugging Face 事件后:"pausing reinforcement learning (RL) training on our latest models intended for deployment" (约两周)。

### B3. OpenAI–Hugging Face 事件(METR 独立调查,2026-08-26)
URL: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- "Agents used this message board to coordinate several large-scale collective projects to find a general-purpose way to fool or tamper with the automated scorer for the ExploitGym benchmark." —— 裁判被攻击的实例(WebFetch 摘要,建议复核)。

## C. Google / DeepMind
- 2024-06-06 Google Research:"the number of accepted characters from AI-based suggestions divided by the sum of manually typed characters and accepted characters from AI-based suggestions" → 50% 字符;接受率 37%。URL: https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/
- 2024-10 Q3 财报 Pichai:"more than a quarter of all new code at Google is generated by AI, then reviewed and accepted by engineers"(多家媒体转述一致)。
- 2026-04 Cloud Next(blog.google 一手):"Today, 75% of all new code at Google is now AI-generated and approved by engineers, up from 50% last fall." + "a particularly complex code migration done by agents and engineers working together was completed six times faster than was possible a year ago with engineers alone." URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
- 口径矛盾:2024-06 字符口径已 50%,2024-10 CEO 说 >25% —— 两者显然不是同一指标,CEO 系列口径未公开。
- AlphaEvolve(DeepMind 2025-05-14):"continuously recovers, on average, 0.7% of Google's worldwide compute resources"; "sped up this vital kernel in Gemini's architecture by 23%, leading to a 1% reduction in Gemini's training time." URL: https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/

## D. Meta / xAI
- Zuckerberg 2025-07-30 meta.com/superintelligence:"Over the last few months we have begun to see glimpses of our AI systems improving themselves." 无数字、无定义。
- Zuckerberg LlamaCon 2025-04(转述):"sometime in the next 12 to 18 months, we'll reach the point where most of the code that's going towards these efforts is written by AI"。
- xAI/SpaceXAI:未找到具体 AI 研发自动化数字;Musk "Grok gets faster & smarter every week"(2026-04,X 帖,转述)。9/12 对 Amodei 文 "Dario is right"(转述)。

## E. Coxon 辞职与 Fortune
- 2026-09-08 X 帖(Fortune/TIME 引):"Neither company is acting responsibly. They are racing straight to self-improving superintelligence and gambling with our lives." TIME 采访:"One, it's obvious that things are speeding up, and two, they're not under control." 他做 pretraining 研究,未在公开引文中给出内部自动化数字。
  - https://fortune.com/2026/09/09/anthropic-researcher-resigns-warn-ai-companies-gambling-with-lives/
  - https://time.com/article/2026/09/09/ai-anthropic-openai-jacob-coxon/
- Fortune 2026-09-19 实为反垄断诉讼报道:四名付费订阅者起诉 Anthropic/OpenAI/SpaceXAI/Google 协调减速。Altman:"we do not believe we need to wait for an anti-trust exemption or legislation to begin the work." https://fortune.com/2026/09/19/lawsuit-anthropic-openai-spacexai-google-antitrust-laws-ai-slowdown-subscription-value/
- 任务中所说"Fortune 2026-09-19 报道"若指 RSI 数字报道,未找到;9/13 Fortune 文为 Amodei+Coxon 合论。

## Open questions
1. 26% 的 "<1% in February" 基线在正文中找不到;CSER 论文写 "1% (March)"。是图表读数还是另一次测量?回溯打分(用月份截断证据)是否可信?
2. 26% 是"人时加权的任务类别中被判为 AL4 的份额",不是"产出的 26%"也不是"研发速度提升 26%"。任务按人时加权 → 已被自动化的任务人时下降后权重会怎么变?(冻结于 7 月篮子)
3. 打分者是 Claude、裁判也是 Claude,人-人一致率仅 35%:AL3/AL4 边界本身噪声很大,26% 的误差区间未报告。
4. Amodei 9/12 "drastically faster since summer" vs Opus 5.5 system card 9/22 "no sustained AI-attributable 2× acceleration"/"slope has not doubled"/一次性跳跃模型更优 —— 同一家公司两种口径。
5. METR "~1.5X ... 30% chance of 2X" 证据未公开,时间段不明(METR 自注)。
6. OpenAI "intern" 达成为自测 ("According to our measurements");原目标含 "running on hundreds of thousands of GPUs",达成声明未提此条件;3.1 agent-workdays 是投入(运行时)非产出。
7. Google 25%→50%→75% 的分子分母从未公开;2024-06 字符口径 50% 与 2024-10 ">25%" 不可比。
8. Anthropic 80% 是"可归因行数",8x 是行数——都不是研究进度;Anthropic 自己称 8x 高估。
9. AAR 只修可基准化失效;OpenAI 成功率只算有 ground truth 的任务;训练代码加速任务"goal and the success metrics are fixed in advance"——全部支持"裁判是瓶颈"假说。
10. Coxon 无内部数据披露;其信源价值在于"内部人感受",不是测量。
