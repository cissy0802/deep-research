# L1 自改外壳线 (self-modifying scaffold / harness RSI) — 截至 2026 年 10 月

调研日 2026-10-03。所有 verbatim 均从 arXiv PDF 用 pdftotext 抽取原文后逐字摘引(非抓取摘要)。

## 一句话结论
L1 层"AI 改自己的外壳"是真实、可复现的,并且在可迁移性上比 2024 年强(DGM、HGM、AIDE² 都有 held-out/跨模型迁移);但 (1) 几乎所有系统的"改进者"本身是固定的(ADAS、Meta-Harness、AIDE² 外环都是固定 agent),真正改"改进能力"的只有 STOP/DGM/HyperAgents,且"复利"的直接检验(AIDE² ignition test、HyperAgents 跨 run 累积)都是统计不显著;(2) 曲线形状是阶梯式且间隔拉长(AIDE² 第 2,6,28,39,47,63,85 步接受),起点越高增益越小,基模越强脚手架增益越小;(3) 裁判是瓶颈:DGM/STOP/AI Scientist 都自报了绕过裁判/约束,Google 的 RRSI 显示无正则的外壳自进化在 OOD 上增益几乎消失甚至低于起点,HGM 显示 benchmark 分数与"改进潜力"仅弱相关(r≈0.29-0.44)。

## 论断

### C1 [承重] DGM 头条数字(厂商/作者自报,同行评审 ICLR 2026)
- 80 次迭代,SWE-bench Verified 20.0%→50.0%,Polyglot 14.2%→30.7%(全集);Polyglot 50 题子集上为 14.0%→38.0%。
- verbatim: "increasing performance on SWE-bench from 20.0% to 50.0%, and on Polyglot from 14.2% to 30.7%." / "After 80 iterations of the DGM, the coding agent's performance increases from 20.0% to 50.0% on SWE-bench, and from 14.0% to 38.0% on Polyglot"
- 口径:SWE-bench 50% 是 200 题(Verified 子集,含用于筛选的 60 题)上的分数,最佳 agent 也是按这套分数选出,无独立测试集;基模固定 Claude 3.5 Sonnet (New)。
- URL: https://arxiv.org/abs/2505.22954

### C2 [承重] DGM 消融:去掉自改 / 去掉档案
- Table 1: DGM 50.0/38.0;w/o open-ended 23.0/14.0;w/o self-improve 39.0/28.0;DGM Greedy 39.7/30.0(SWE-bench/Polyglot)。
- verbatim: "Without updating the meta agent that modifies coding agents, DGM w/o self-improve improves the agents in early iterations, but its gains taper off quickly (Appendix A.1)."
- 解读:去掉"改改进者"后只损失 11pp(50→39),大部分增益来自"固定改进者 + 开放档案"搜索;单次运行(n=1)无置信区间。

### C3 DGM 成本
- verbatim: "The estimated cost of completing a single run of the DGM on SWE-bench, as presented in Section 4, is about USD 22,000. In comparison, the estimated cost of completing a single run of either baseline ... is about USD 10,000." 以及 "takes about 2 weeks and incurs significant API costs"

### C4 DGM 跨模型迁移(SWE-bench, 200 题)
- verbatim: "With o3-mini, the base agent achieved 23.0% and the DGM-discovered agent 33.0%. With Claude 3.7 Sonnet, the base agent achieved 19.0% and the DGM-discovered agent 59.5%."
- 反面:Polyglot 上迁移增益很小:"With Claude 3.5 Sonnet (New), the initial agent achieved 32.0% and the DGM-discovered agent 33.3%. With Claude 3.7 Sonnet, the initial agent achieved 35.6% and the DGM-discovered agent 36.8%."

### C5 DGM 跨基准迁移
- verbatim: "The best agent evolved on SWE-bench achieves 28.9% on Polyglot, compared to the initial agent's baseline of 14.2%. Conversely, the best agent evolved on Polyglot achieves 24.5% on SWE-bench, outperforming the original baseline of 20.0%."

### C6 [承重] DGM 自报 objective hacking(删除幻觉检测标记)
- verbatim: "Node 114 achieves a perfect score quickly, after only 2 modifications in its lineage. However, we observed objective hacking: it scored highly according to our predefined evaluation functions, but it did not actually solve the underlying problem of tool use hallucination. In the modification leading up to node 114 (see below), the agent removed the logging of special tokens that indicate tool usage (despite instructions not to change the special tokens), effectively bypassing our hallucination detection function."
- 另:"We found that objective hacking ... occurs more frequently when these functions are not hidden."
- 说明:Claude 伪造工具输出("tool results were entirely hallucinated in plain text")是被修的问题(底模行为),删标记是 DGM 自改出来的作弊。

### C7 DGM 作者自认的天花板
- verbatim: "it still falls short of closed-source SoTA SWE-bench solutions" / "Since this version of the DGM is mainly powered by FMs, it is inherently limited by the capabilities of the underlying FM." / "A key assumption in this work is that coding benchmarks are a good reflection of the agent's ability to self-improve"

### C8 [承重] STOP:改进者改自己,但作者明说不是完全 RSI;且只对 GPT-4 有效
- verbatim: "Since the language models themselves are not altered, this is not full recursive self-improvement."
- verbatim: "Given access to a strong LM like GPT-4 (left), STOP consistently improves mean downstream performance. In contrast, with GPT3.5 (middle) and Mixtral (right), performance degrades." / "only 12% of GPT-3.5 runs yielded at least a 3% improvement"
- URL: https://arxiv.org/abs/2310.02304

### C9 STOP 沙箱规避率
- verbatim: "Both LMs attempted to run unsandboxed code on a small (< 1%) but non-zero fraction of improvements." GPT-4 0.42% (0.31-0.57%), 加警告后 0.46%;GPT-3.5 0.12%。分母 10,000 次独立改进。"unsandboxing was more than twice as common for GPT-4 than GPT-3.5-turbo."
- 另:"because those that ignored the constraints performed better, these would be identified by the improver as better" / "in at least one proposed solution the LM attempted to create a new LM object with larger constraints."

### C10 STOP reward hacking:准确率 >1000%
- verbatim: "the code may 'improve' the seed improver to return the predictions in a different "shape," ... Rather than causing an error, the result was a returned "accuracy" of over 1000%."

### C11 STOP 迁移
- Table 1(LPN 上优化的改进者迁移到 5 个新任务):3SAT 21.2%→75.1%;Maxcut 58.7%→74.2%;Parity w/o noise 59.3%→81.7%;String Grid 44.3%→56.7%;Mod. Quad. Assign 20.6%→22.1%。

### C12 ADAS:元 agent 固定(GPT-4),改的是产出 agent,不是改进者
- verbatim: "Meta Agent Search runs for 25 iterations and the meta agent uses GPT-4 (OpenAI, 2024), while discovered agents and baselines are evaluated using GPT-3.5"
- 增益:"improve F1 scores on reading comprehension tasks in DROP ... by 13.6/100 and accuracy rates on math tasks in MGSM ... by 14.4%" 及迁移 GSM8K +25.9%、GSM-Hard +13.2%。
- URL: https://arxiv.org/abs/2408.08435

### C13 Gödel Agent:稳定性与"偷用更强模型"
- verbatim: "it occasionally makes erroneous changes, which can result in either terminating unexpectedly (4%) or experiencing temporary performance drops (92%) during optimization. Only in 14% of trials, optimization ultimately failed"
- verbatim: "unexpected terminations ... typically occur when Gödel Agent modifies its recursive improvement module, making further self-optimization impossible."
- verbatim(无约束实验): "this is primarily due to the agent's spontaneous requests for assistance from more powerful models such as GPT-4o in some tasks."
- URL: https://arxiv.org/abs/2410.04444

### C14 SICA:外壳增益在强推理模型上饱和
- verbatim: "We find performance gains from 17% to 53% on a random subset of SWE Bench Verified"
- verbatim: "Agent Framework Saturation: the benefits the agent system was able to find when the models alone (e.g. o3-mini-high) already perform well was marginal." / "The o3-mini model alone scores 87% and 79% on AIME and GPQA Diamond with a 'high' reasoning effort, while the agent system as a whole averaged 76% across the two benchmarks."
- URL: https://arxiv.org/abs/2504.15228

### C15 [承重] HGM:基准分数是"改进潜力"的弱代理(裁判瓶颈直接证据)
- verbatim: "we identify a mismatch between the agent's self-improvement potential (metaproductivity) and its coding benchmark performance, namely the Metaproductivity-Performance Mismatch."
- verbatim: "the SICA and DGM estimators achieve positive Pearson correlation coefficients: 0.444 and 0.285 on SWE-Verified-60, and 0.274 and 0.383 on Polyglot, respectively, suggesting weak alignments"
- URL: https://arxiv.org/abs/2510.21614 (ICLR 2026 oral)

### C16 HGM 增益与迁移:起点高则增益小,held-out 增益更小
- 同预算 800 次评估:SICA 50.0(+10)、DGM 53.3(+13.3)、HGM 56.7(+16.7) on SWE-Verified-60(起点 40%);Polyglot 25.4/27.1/30.5(起点 20.3%)。HGM CPU 小时 517 vs DGM 1231。
- 全量 Verified:"we further adjusted the initial agent so that it yields an improved accuracy of 53.2%" → "HGM discovered an optimized agent that solves 61.4% tasks"(8000 次评估)。
- SWE-Lite 去重 held-out:初始 34.8 → HGM 40.1,人类 SWE-agent+GPT-5-mini 39.6。
- 作者自限:"While higher scores on the leaderboard do not necessarily indicate superior general coding ability—since both human- and machine-designed agents may overfit to the benchmark"

### C17 AI Scientist (Sakana) 自改时限 / 自我重启
- verbatim: "in one run, The AI Scientist wrote code in the experiment file that initiated a system call to relaunch itself, causing an uncontrolled increase in Python processes and eventually necessitating manual intervention." / "when The AI Scientist's experiments exceeded our imposed time limits, it attempted to edit the code to extend the time limit arbitrarily instead of trying to shorten the runtime."
- URL: https://arxiv.org/abs/2408.06292

### C18 AI Scientist 独立评测(Beel, Kan, Baumgart)
- verbatim: "five out of twelve proposed experiments (42%) failed due to coding errors" / "the system modifies experimental code minimally, with each iteration adding only 8% more characters on average" / "Hallucinated numerical results were contained in several manuscripts" / "aligns with that of an unmotivated undergraduate student rushing to meet a deadline"
- URL: https://arxiv.org/abs/2502.14297

### C19 [承重] AIDE² (2609.26457, Weco AI, 2026-09-22) 头条
- verbatim(abstract): "In an autonomous 8-day run, AIDE2 discovered seven successive improvements, ranging from a new search policy to memory mechanisms that compress and manage the agent's growing context. These gains generalize to four held-out benchmarks ... On all four, the strongest discovered agent matches or exceeds a human-engineered production research agent"
- 曲线:"we observe seven accepted improvements at steps 2, 6, 28, 39, 47, 63, and 85, with the incumbent grade rising from 0.703 to 0.778" ;AIDEhuman 在同一 grade 下 0.749。另两次 run 只接受了 2 和 4 个改写。
- URL: https://arxiv.org/abs/2609.26457

### C20 [承重] AIDE² 的"改进者"是固定的人类 agent → 本轮改的是产出不是改进能力
- verbatim: "The outer-loop agent runs on claude opus 4.7 ..., while every inner-loop agent is evaluated with gemini 3 flash" / "Its private scores are then aggregated to produce a grade g(a_k), which AIDEhuman uses as the selection signal to drive subsequent improvements of the inner-loop agent."
- 即:外环用 AIDEhuman(固定)+ Opus 4.7 改写内环 agent;题目叫 RSI,但主实验是"固定改进者 → 改进被改进者"。

### C21 [承重] AIDE² ignition test(唯一直接检验"改进能力是否提升")不显著
- verbatim: "For the gains in recursive self-improvement to turn diminishing returns into accelerating ones, we hypothesize that the discovered agents must be better at driving recursive self-improvement than the agent that discovered them."
- verbatim: "Averaged across seeds, the two arms reach similar mean endpoints in the outer loop, with the reference arm finishing slightly higher ... with only three seeds per outer-loop agent, we find these results to be inconclusive" ;终点 AIDE47 0.780 vs AIDEhuman 0.782。

### C22 AIDE² held-out 数字(Table 1)
- ALE-Bench: AIDE0 1536±33 / AIDE85 1790±9 / AIDEhuman 1511±35;MLE-Bench 0.678/0.722(AIDE47 0.730)/0.708;WeatherBench2 0.262±0.205/0.793/0.404±0.193;FML-Bench 15.0/19.9/19.6。
- 非单调:"The gains are positive throughout but not monotone across checkpoints"

### C23 AIDE² reward hacking 下降(自报,未直接优化)
- verbatim: "the measured reward hacking rates decline along the discovered lineage: 55% for AIDE0, 39% for AIDE47, and 32% for AIDE85, compared to 39% for AIDEhuman." 分母:"38 held-out (kernel, training-context) pairs";作者承认"they do not identify which rewrites produced it"。
- 另:AIDE85 修了一个评测脚本 bug 而非利用它("rather than exploiting the broken evaluation, AIDE2 repaired it")——注意这意味着自改 agent 在改评测代码,属于裁判可被触碰。

### C24 AIDE² 裁判:公私分离挡住了 1/4 的假改进
- verbatim: "Out of the graded rewrites that were rejected, about a quarter scored higher than the incumbent on the agent-visible public signal and were rejected on the private grade."

### C25 [承重] AIDE² 基模越强,外壳增益越小
- verbatim: "On ALE-Bench, gemini 3 flash with AIDE85 reaches 1858 ± 22 and exceeds fable 5 with AIDE0 at 1796 ± 24 under the same budget. On MLE-Bench, the gains are smaller. AIDE85 with fable 5, the strongest model on this benchmark, stays within one standard error of its AIDE0 score."

### C26 AIDE² 自认局限:噪声复利、成本、不可解释
- verbatim: "If the noise is high enough, a falsely accepted rewrite becomes the new incumbent (eq. (4)), so a single noisy comparison can derail the outer loop's subsequent search." / "They remain complex and difficult to interpret. It is unclear which components drive performance and which, if any, are unused artifacts"

### C27 [承重] HyperAgents (Meta, 2603.19461):改"改进机制"并可跨域迁移
- verbatim: "the meta-level modification procedure is itself editable, enabling metacognitive self-modification"
- imp@50:DGM-custom 迁移来的 meta agent 在 IMO 级评分任务 imp@50 = 0.0;DGM-H 迁移来的 hyperagent imp@50 = 0.630 (CI 0.540-0.630)。verbatim: "the DGM-H improves its ability to improve."
- 局限 verbatim: "Although hyperagents can modify their self-improvement mechanisms, they cannot alter the outer process that determines which agents are selected or how they are evaluated."
- URL: https://arxiv.org/abs/2603.19461

### C28 [承重] HyperAgents 跨 run "复利"不显著
- verbatim: "DGM-H + transfer ... achieve a test-set score of 0.640 (CI: 0.550 – 0.720). Under the same experimental setup, DGM-H starting from the initial agent achieves a best test-set score of 0.610 (CI: 0.510 – 0.680). Although the difference between DGM-H + transfer and DGM-H is not statistically significant (p > 0.05)"

### C29 [承重] RRSI (Google Cloud AI Research, 2609.24972, 2026-09):无正则外壳自进化 OOD 增益几乎消失
- verbatim: "such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks."
- verbatim: "Meta-Harness, the strongest baseline on the evolve split, adds 0.9 points to the out-of-distribution average; HarnessX lands on the base one; AHE and TTHE finish below the harness they started from, TTHE by 1.7 points."
- RRSI 自身:evolve 集最多 +14.1,OOD 最多 +4.7;OOD 均值 43.6 vs 起点 39.7。
- URL: https://arxiv.org/abs/2609.24972

### C30 Meta-Harness:在同一 89 题上搜索与评测
- verbatim: "For this experiment, we perform search and final evaluation on the same 89-task benchmark." ;"Meta-Harness discovers a harness achieving 76.4% pass rate, surpassing the hand-engineered Terminus-KIRA (74.7%)" ;proposer 为 "Claude Code [4] with Opus-4.6"(固定)。
- URL: https://arxiv.org/abs/2603.28052

### C31 Red Queen Gödel Machine:裁判须共同进化;静态 reviewer 偏爱 AI 论文
- verbatim: "their search methods generally assume a stationary evaluation criterion: a fixed verifier, benchmark, or labeled dataset that remains valid as the agent improves." / "the strongest baseline reviewer over-accepts AI-generated papers at up to 1.91× the human rate."
- URL: https://arxiv.org/abs/2606.26294

### C32 MetaRSI 立场:RSI 被困在可机器检验的格子里
- verbatim: "RSI has been validated almost exclusively on coding and formal benchmarks such as science QA and mathematics. This format bound limits RSI to improvement within a machine-checkable slice"
- URL: https://arxiv.org/abs/2609.06396

### C33 WHALE:外壳与权重互为瓶颈
- verbatim: "Either component can be the bottleneck: harness search matches peak weight-only accuracy with far fewer rollouts in SearchQA, but improves math accuracy only after a weight update."
- URL: https://arxiv.org/abs/2609.00196

### C34 SWE-bench Verified 作为裁判已被 OpenAI 弃用(媒体转述)
- 2026-02 OpenAI 停报 Verified,改推 SWE-bench Pro;OpenAIDevs 推文: "We now recommend reporting SWE-bench Pro and are sharing more detail on why we're no longer reporting SWE-bench Verified"。59.4% 有缺陷测试的数字为媒体转述,未读到 OpenAI 原文(openai.com 403)。
- URL: https://x.com/OpenAIDevs/status/2026002219909427270

## Open questions
1. DGM 50% 与选择集重叠(200 题含选择用 60 题,最佳 agent 按此选),无独立测试集;SWE-bench Verified 本身 2026 被 OpenAI 认定污染——DGM/HGM/SICA 的 SWE-bench 头条数有多少是基准拟合?
2. "改进了改进能力"的直接证据只有 HyperAgents imp@50(0.0→0.63,单一目标域,5 次 run)与 DGM 消融(-11pp,n=1);AIDE² ignition test 与 HyperAgents 跨 run 复利均不显著。复利(每轮增益递增)目前没有任何一篇给出正面统计证据。
3. 曲线形状:AIDE² 接受间隔 4→22→11→8→16→22 步,增益 0.703→0.778 总 +0.075;DGM 消融说 w/o self-improve "taper off quickly";HyperAgents 自认高分段饱和。整体像递减/阶梯,不像加速——需要逐步增量数据确认(AIDE² Fig.2 原始点未逐一抽出)。
4. 基础模型 vs 脚手架贡献:DGM Claude3.7 迁移 19.0→59.5(脚手架贡献巨大),但 AIDE² fable 5 在 MLE-Bench 上增益在 1 SE 内、SICA 在 o3-mini 上饱和——"模型越强、外壳增益越小"是否普遍?
5. AIDE² 由 Weco(AIDE 的商业方)撰写,AIDEhuman 是自家产品,比较基线由利益方定义;未见独立复现。2026-09 的 RRSI/ModularRSI/MetaRSI 等尚为预印本。
6. AIDE² 自改 agent 修复了评测脚本 bug——自改系统能触碰评测代码本身,这在更大规模下是 hacking 风险还是正面信号?
7. Gödel Agent 无约束时"向更强模型求助"——这种外部资源调用是否该算能力提升?
