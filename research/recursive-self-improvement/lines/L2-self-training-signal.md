# L2 自产训练信号线(截至 2026 年 10 月)

调研日期 2026-10-03。所有 verbatim 均取自 arXiv API 原始摘要 / arXiv HTML 全文 / Nature 页面 / Kimi K2 PDF(pdftotext),经 grep 实读,非记忆。

## 总判断(一句话)
没有外部硬裁判时,自产信号(自打分 / 多数投票 / 自信度 / 自判)普遍呈"先升后平或先升后崩":Self-Rewarding/Meta-Rewarding 3-4 轮内每轮增益不递增;Mind the Gap 测得 GV-gap 2-3 轮归零且与模型规模无关;R-Zero 伪标签准确率 79%→63%(第 3 轮);SRT/RLIF 长训全崩。能持续往上走的方案几乎都靠"把裁判接到外部":代码执行器(Absolute Zero)、规则可验证奖励(R1-Zero)、语料锚定(SPICE/SCOPE)、外部验证算力扩充的 verifier(DeepSeekMath-V2)、用 RLVR 信号校准 self-critic(Kimi K2)。唯一偏正面的规模信号:相对 GV-gap 随预训练 FLOPs 单调增(Song et al.)——即"单轮可自改的余量"随规模变大,但"多轮复利"未被观察到。

## 论断

### A. 方法谱系与裁判来源(中性定义)
1. **STaR (Zelikman 2022, arXiv 2203.14465)** — 裁判 = 数据集正确答案(外部标签)。"fine-tune on all the rationales that ultimately yielded correct answers; repeat." https://arxiv.org/abs/2203.14465 [同行评审 NeurIPS]
2. **ReST-EM (Singh et al. 2023, 2312.06585)** — 仅在有标量反馈(可验证)任务上:"we explore whether we can go beyond human data on tasks where we have access to scalar feedback, for example, on math problems where one can verify correctness" ;"(3) repeat this process a few times"。https://arxiv.org/abs/2312.06585 [Google DeepMind,厂商论文]
3. **Constitutional AI (Anthropic 2022, 2212.08073)** — RLAIF:"The only human oversight is provided through a list of rules or principles"。人类锚点退到宪法层。https://arxiv.org/abs/2212.08073 [厂商论文]
4. **DeepSeek-R1-Zero (2501.12948 v1)** — 刻意不用神经奖励模型:"We do not apply the outcome or process neural reward model in developing DeepSeek-R1-Zero, because we find that the neural reward model may suffer from reward hacking in the large-scale reinforcement learning process"。https://arxiv.org/html/2501.12948v1 [厂商自报] **承重**
5. **Absolute Zero (Zhao et al. 2025, 2505.03335)** — 零外部数据,但裁判=代码执行器:"using a code executor to both validate proposed code reasoning tasks and verify answers, serving as an unified source of verifiable reward"。https://arxiv.org/abs/2505.03335 [学术]
6. **Kimi K2 (Moonshot 2025, 2507.20534)** — 生产级 self-critic 由 RLVR 信号闭环校准:"During RL training, the critic model is refined using verifiable signals. On-policy rollouts generated from verifiable-reward prompts are used to continuously update the critic"。https://arxiv.org/pdf/2507.20534 [厂商自报] **承重候选**

### B. 自打分迭代:增益与饱和
7. **Self-Rewarding (Yuan et al. 2024, 2401.10020)** AlpacaEval 2.0 胜率(对 GPT-4 Turbo,GPT-4 评判):"from 9.94% in Iteration 1, to 15.38% in Iteration 2, to 20.44% in Iteration 3"。每轮增量 +5.44 → +5.06pp,不递增;只跑 3 轮;评判是外部 GPT-4 代理。https://arxiv.org/html/2401.10020v3 **承重**
8. 同文作者自承:"While this effect likely saturates in real-world settings"。奖励能力 pairwise accuracy 78.7%→80.4%→81.7%(+1.7,+1.3)。
9. **Meta-Rewarding (Wu et al. 2024, 2407.19594)** 诊断:"existing methods have primarily focused on improving model responses rather than judgment capabilities, resulting in rapid saturation during iterative training";"If the ability to judge does not improve then training the actor over iterations can quickly saturate – or worse could overfit the reward signal, a.k.a. reward hacking." https://arxiv.org/html/2407.19594v2 **承重(直接支持"瓶颈在裁判")**
10. Meta-Rewarding 表格(Llama-3-8B-Instruct,AlpacaEval 2 LC):Self-Rewarding+LC iter1-4 = 26.93/30.38/34.87/35.49(第4轮 +0.62);Meta-Rewarding = 27.85/32.66/35.45/39.44(+4.81/+2.79/+3.99,不单调递增)。Arena-Hard:Self-Rewarding iter3→4 = 28.2%→27.3%(下降);Meta-Rewarding 25.1/27.4/27.6/29.1。
11. 长度偏置放大:"this leads to length explosion where responses get longer with each iteration. This is due to the length-bias of the judge"。
12. **自偏好偏置 (Panickssery et al. 2024, 2404.13076)**:"we discover a linear correlation between self-recognition capability and the strength of self-preference bias"。https://arxiv.org/abs/2404.13076 [学术/NeurIPS]

### C. 生成-验证鸿沟与轮次饱和
13. **Mind the Gap (Song et al. 2024, 2412.02674)** 规模正面:"a variant of the generation-verification gap scales monotonically with the model pre-training flops";"We conjecture that in this case, the relative gap is linear with respect to the log of the pre-training flops." https://arxiv.org/html/2412.02674v2 **承重**
14. 同文迭代负面:"Saturation Limit: Without new information, iterative self-improvement typically saturates after two or three rounds, regardless of the model's capacity." 以及 "GV-Gap saturates to 0 in handful rounds ... the saturation rate is independent from the model capacity ... the effective diversity degrades"。**承重**
15. 同文:Sudoku 上 "Only the 72B models can self-improve";事实类任务 "There is no significant generation-verification gap"。
16. 交叉改进:"The gap scales directly with the verifier's flops and inversely with the generator's flops."(=裁判必须比生成者强)
17. **Huang et al. 2023 (2310.01798, ICLR 2024)**:"LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." 表3:GPT-4 GSM8K 95.5→91.5→89.0;GPT-3.5 CommonSenseQA 75.8→38.1→41.8。先前改进 "result from using oracle labels ... and the improvements vanish when oracle labels are not available"。**承重**

### D. 无外部奖励的 RL:先升后崩
18. **R-Zero (Huang et al. 2025, ICLR 2026, 2508.05004)** 伪标签真准确率:"initially high at 79.0%, it systematically drops to 63.0% by the third iteration ... the Solver's majority vote becomes a less reliable source for ground truth." **承重**
19. 同文:"After multiple iterations, we observe a consistent and concerning trend of performance degradation across all models ... the larger the model, the later the onset of performance degradation" — 0.6B 第1轮见顶,4B 持续3轮后在 Step 60 骤降;"larger model capacity can delay the negative effects, it does not prevent them"。单模型版 Single-R-Zero "peaks after the very first iteration"。
20. **SRT (Shafayat et al. 2025, 2505.21444)**:"prolonged RL with self-reward leads to reward hacking where models learn to maximize training (pseudo-)reward, resulting in sudden and complete performance collapse";加大 KL 系数"does not mitigate reward hacking"。https://arxiv.org/abs/2505.21444
21. **No Free Lunch / RLIF (2506.17219)**:"when training progresses, performance degrades even below the model before training ... RLIF yields little improvement for instruction-tuned models"。
22. 反面:**Intuitor (2505.19590)** 自信度奖励 "matches GRPO's performance on mathematical benchmarks";**TTRL (2504.16084)** "boosts the pass@1 performance of Qwen-2.5-Math-7B by approximately 211% on the AIME 2024 with only unlabeled test data"(训练时长较短,且基于 Qwen-Math)。
23. **Spurious Rewards (Shao et al. 2025, 2506.10947)** 测量效度警告:随机奖励使 Qwen2.5-Math-7B MATH-500 "+21.4 percentage points ... nearly matching the 29.1-point gain from ground-truth rewards";对 Llama3/OLMo2 无效。**承重(方法学)**
24. **Rise-and-Collapse (2606.21090, 2026-06)**:即使是二值 CodeGrader 硬裁判,"pass@1 ... peaks within tens of gradient steps and then falls back, sometimes to near zero";"KL- and EWC-style constraints do not prevent it";"GRPO raises the floor but does not remove the cliff"。

### E. RLVR(硬裁判)是否扩展边界
25. **Yue et al. 2025 (2504.13837)**:"the base models achieve a higher pass@k score when k is large ... reasoning abilities originate from and are bounded by the base model";蒸馏 "can introduce new reasoning patterns"。**承重**
26. **ProRL (NVIDIA 2025, 2505.24864)** 反驳:"RL-trained models consistently outperform base models across a wide range of pass@k evaluations, including scenarios where base models fail entirely"(1.5B 模型)。
27. **PASS@(k,T) (2604.14877, 2026-04)**:"tool-use RL genuinely enlarges the capability boundary ... These results reconcile optimistic and pessimistic readings of RL for LLMs: both are correct, on different task types."
28. **Diversity Collapse as Overtraining (2606.15455, 2026-06)**:"restricting updates to problems with zero observed success lifts Pass@256 above the base model on difficult benchmarks";"a non-trivial fraction of initially unsolvable problems become solvable during standard RLVR training"。

### F. 合成数据崩溃
29. **Shumailov et al. Nature 2024**:"indiscriminate use of model-generated content in training causes irreversible defects in the resulting models, in which tails of the original content distribution disappear." https://www.nature.com/articles/s41586-024-07566-y
30. **Gerstgrasser et al. 2024 (2404.01413)**:"if data instead accumulate, the test error has a finite upper bound independent of the number of iterations, meaning model collapse no longer occurs." (避免崩溃 ≠ 带来提升)
31. **Strong Model Collapse (Dohmatob et al. 2024, 2410.04840, ICLR 2025)**:"even the smallest fraction of synthetic data (e.g., as little as 1% of the total training dataset) can still lead to model collapse";"larger models can amplify model collapse"(简化回归设定)。

### G. 2025-2026 前沿:把裁判/信息源接出去
32. **DeepSeekMath-V2 (2511.22570)**:"To maintain the generation-verification gap as the generator becomes stronger, we propose to scale verification compute to automatically label new hard-to-verify proofs, creating training data to further improve the verifier." Putnam 2024 118/120(scaled test-time compute)。[厂商自报] **承重候选(最强的"裁判也能自举"证据)**
33. **SPICE (Meta FAIR, 2510.24684)**:"Unlike existing ungrounded self-play methods that offer more limited benefits, SPICE achieves consistent gains across mathematical (+8.9%) and general reasoning (+9.8%)";"corpus grounding provides the rich, near-inexhaustible external signal necessary for sustained improvement"。
34. **ICML 2026 position (2603.02218)**:"many existing proposals are better understood as self-play and often plateau quickly. A central failure mode is that the loop synthesises more data without increasing learnable information for the next iteration." 同类:R-Few (2512.02472) "unguided self-evolving systems often plateau quickly or even degrade";SCOPE (2605.31433) "rubric generation quality is the bottleneck for self-judging"。
35. **Self-Play Pretraining with Zero Data (Cowsik, Dolev, Li, ..., Goodman, Levine; 2609.30063, 2026-09-24)**:生成器写程序由通用图灵机执行,学习者从零学;"Across several natural datasets, zero-shot loss exhibits predictable scaling in compute." —— 裁判/环境=图灵机(硬),proof-of-concept。
36. (补充)**Scaling Laws for Scalable Oversight (Engels et al. 2025, 2504.18530)**:嵌套监督在 Elo 差 400 时成功率 "13.5% for Mafia, 51.7% for Debate, 10.0% for Backdoor Code, and 9.4% for Wargames; these rates decline further when overseeing stronger systems"。

## Open questions
- "复利"的可检验定义:目前所有迭代自打分论文只跑 3-4 轮,每轮增益均不递增(7,10);没有任何一篇在无外部裁判下展示递增增益。是否存在超 5 轮的公开自打分实验?
- Song et al. 的"相对 gap 随 FLOPs 线性于 log"是 conjecture,模型最大到 72B 级、预训练 FLOPs 维度,未在 2025-26 前沿推理模型上复测;规模让单轮余量变大,但饱和轮数与规模无关——两者合起来指向"每代模型一次性收割,而非轮内复利"。
- R-Zero/SRT/TTRL/Intuitor/Spurious Rewards 多在 Qwen2.5(-Math) 上做,Spurious Rewards 显示 Qwen 对随机奖励也涨——无外部奖励方法的正面结果需在 Llama/OLMo 复验。
- DeepSeekMath-V2 的 verifier 扩展靠"scaled verification compute"自动标注,仍有元验证与人工抽查成分?论文正文需二次核实其人工参与比例。
- ReST-EM 正文据记忆有"多轮后 APPS 过拟合"结论,本次未实读,不入论断。
- 厂商生产管线(Kimi K2、R1)的 self-critic/RLAIF 占比与增益没有独立测量。
- arXiv 2601.05280(LLM 非 Solomonoff 归纳、"Singularity not near")摘要提及前沿厂商 "Fable and Astra",版本到 v6,来源可信度存疑,未采用。
- 搜索结果称 2026-09-03 发布 "GPT-6 Astra"、PostTrainBench 23% 等,属 L3/L4 线,未核实。
