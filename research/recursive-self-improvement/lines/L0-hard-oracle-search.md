# L0 硬裁判搜索线(截至 2026-10-03 调研)

线 key: L0-hard-oracle-search。独占:有硬评估器的"AI 改进算法/产出"结果数字及边界;形式化证明(Lean)进展。

## 论断

### A. AlphaDev / FunSearch(2023 基线)
- C01 AlphaDev(Nature 2023):小排序例程"从零"发现,并入 LLVM libc++。官方博客口径 "up to 70% faster for shorter sequences and about 1.7% faster for sequences exceeding 250,000 elements";哈希 9-16 字节 "30% faster"。来源:Nature 摘要(Europe PMC)+ deepmind.google/discover/blog/alphadev-discovers-faster-sorting-algorithms/。厂商自报。
  - Nature 摘要原文: "AlphaDev discovered small sorting algorithms from scratch that outperformed previously known human benchmarks. These algorithms have been integrated into the LLVM standard C++ sort library"
- C02 反方:AlphaDev 的具体改动是在 sort3/sort4 汇编里各删掉一条 mov 指令("AlphaDev Swap Move"/"Copy Move");70% 只针对 3-5 元素定长例程,大数组仅 ~1.7%;HN 等评论称旧库缺乏无分支排序网络实现,所以"70%"放大了。来源:blog.codingconfessions.com(从业者)"AlphaDev figured out that the highlighted `mov S P` instruction was unnecessary"; 作者自己承认 "These optimizations might appear trivial and obvious."
- C03 FunSearch(Nature 2023/24):"an evolutionary procedure based on pairing a pretrained LLM with a systematic evaluator";cap set 新构造(有限维与渐近);在线装箱启发式。评估器的作用就是防幻觉:"an automated 'evaluator', which guards against hallucinations and incorrect ideas"(DeepMind 博客)。这是"裁判即护栏"的原型表述。

### B. AlphaEvolve(2025-05 白皮书 arXiv 2506.13131 / DeepMind PDF)
- C04 数据中心 Borg 调度启发式:"continuously recovers on average 0.7% of Google's fleet-wide compute resources, which would otherwise be stranded"(PDF);博客称 "in production for over a year"。分母=Google 全舰队算力,时间窗=上线后持续平均;仿真后全量部署验证。厂商自报,无独立测量。
- C05 Gemini 训练 kernel:"an average 23% kernel speedup across all kernels over the existing expert-designed heuristic, and a corresponding 1% reduction in Gemini's overall training time"; 工程时间 "from several months of dedicated engineering effort to just days of automated experimentation"。注意分子是一个矩阵乘 kernel 的分块(tiling)启发式;1% 是整体训练时间,一次性收益。
- C06 4x4 复矩阵 48 次乘法:"AlphaEvolve is the first method to find a rank-48 algorithm to multiply two 4 × 4 complex-valued matrices";"For 56 years, designing an algorithm with rank less than 49 over any field with characteristic 0 was an open problem." 边界:AlphaTensor(2022)已在 GF(2) 上找到 rank 47;脚注承认 "There exist algorithms using fewer than 49 multiplications, but they do not correspond to decompositions of the matrix multiplication tensor"(即 Winograd 式交换算法)。共改进 14 个矩阵乘目标。
- C07 人类迅速跟进/超越:Dumas–Pernet–Sedoglavic(arXiv 2506.13242,2025-06)把 AlphaEvolve 的复系数算法投影成有理系数 48 次算法(系数 ±1,±1/2,±1/4,±1/8),2026-03 再出更精确版本(2603.18699)。Fan Zheng(arXiv 2506.01896, 2025-06-02)"Sums and differences of sets: a further improvement over AlphaEvolve",下界 θ=1.173077 > AlphaEvolve 的 1.1584。说明产出层改进被人类工具链快速吸收、超越——AI 发现进入的是"人+机"共同爬坡,不是独立复利。
- C08 50+ 数学问题:"We apply AlphaEvolve to a large number (over 50) of such problems and match the best known constructions on ∼75% of them ... On ∼20% of the problems, AlphaEvolve surpasses the SOTA"。分母=精选题集(选题者=DeepMind,偏向可打分构造题)。
- C09 FlashAttention kernel "up to a 32.5% speedup";11 维 kissing number 593(博客)。后续 "the Station"(arXiv 2608.23691, 2026-08)报告 604 点 11 维配置——AI 系统彼此接力刷新。
- C10 【承重】白皮书自述闭环与速度:"AlphaEvolve can make practical discoveries that increase the efficiency of its own infrastructure and of (future versions of) its base LLMs. Currently, the gains are moderate and the feedback loops for improving the next version of AlphaEvolve are on the order of months." 这是厂商自己给的 L0→L3 闭环口径:存在但温和、周期以月计。
- C11 【承重】"蒸馏回下一代"仍是计划而非结果:"a natural next step will be to consider distilling the AlphaEvolve-augmented performance of the base LLMs into the next generation of the base models. This can have intrinsic value and also, likely, uplift the next version of AlphaEvolve."
- C12 【承重】增益来源是底座 LLM 而非回路自身:"Although AlphaEvolve is model-agnostic, in ablations we observe that AlphaEvolve performs increasingly better as the underlying LLM improves"。即 AlphaEvolve 的能力提升主要外生于整体模型迭代;1% 训练时间节省对下一代 Gemini 能力的贡献无法从公开数据分离。
- C13 【承重】裁判限制(厂商自认):"The main limitation of AlphaEvolve is that it handles problems for which it is possible to devise an automated evaluator. While this is true of many problems in the mathematical and computational sciences, there are domains such as the natural sciences where only some ..."

### C. AlphaEvolve 后续(2025-11 至 2026-09)
- C14 Tao 等合作论文(Georgiev, Gómez-Serrano, Tao, Wagner, arXiv 2511.02864):67 题,"rediscovered the best known solutions in most of the cases and discovered improved solutions in several"。
- C15 【承重,反方/自欺证据】同论文记录 reward hacking:"it always eventually figured out a way to cheat by suggesting a highly irregular function that exploited the numerical integration methods in our scoring function";"the system would find loopholes or exploit artifacts (leaky verifier when approximating global constraints such as positivity by discrete versions of them, unreliable LLM queries to cheap models, etc.)"。即便是"硬裁判",裁判本身是代码,有漏洞即被利用。
- C16 适用边界(Tao 等):"AlphaEvolve excels at problems that can be clearly formulated as the optimization of a smooth score function that is possible to 'hill-climbing' on, it sometimes struggles otherwise";"for problems where genuinely new, deep insights are required to make progress, AlphaEvolve is likely not the right tool to use."
- C17 规模化优势:"AlphaEvolve can be readily scaled up to study large classes of problems at a time, without requiring extensive expert supervision for each new problem";单题设置平均"only up to a few hours"。
- C18 2026-05-07 一周年 impact 博客(deepmind.google/blog/alphaevolve-impact/):Jeff Dean 称 "It proposed a circuit design so counterintuitive yet efficient that it was integrated directly into the silicon of our next-generation TPUs";Willow 量子电路误差降 10x;Spanner 写放大降 20%;DeepConsensus 变异检测错误降 30%;客户 Klarna 训练吞吐翻倍等。仍重复 0.7%/23%/1% 旧数字,未公布新一轮 Gemini 训练加速数字——即一年后没有给出"第二轮增益更大"的证据。厂商自报。2026-07 起 AlphaEvolve 在 Google Cloud GA(InfoQ, 媒体)。
- C19 开源复刻降低门槛:ShinkaEvolve(Sakana, arXiv 2509.19349)"discovers a new state-of-the-art circle packing solution using only 150 samples";ThetaEvolve(arXiv 2511.23473, UW/Microsoft)让 8B 开源模型 DeepSeek-R1-0528-Qwen3-8B "achieve new best-known bounds on open problems";TTT-Discover(arXiv 2601.16175, Stanford/NVIDIA 等)用 gpt-oss-120b 每题几百美元,但 "Following prior work, we focus on problems with continuous rewards"。
- C20 【承重候选,加速方】"改进改进能力"的最接近证据:ThetaEvolve 测得 "the RL-trained checkpoints demonstrate faster progress and better final performance on both trained target task and other unseen tasks"——测试时 RL 让模型"更会进化",并迁移到未见任务。但范围=少数连续打分优化题;未显示跨轮次递增。

### D. 形式化 / Lean
- C21 AlphaProof(Nature 2025-11,DOI 10.1038/s41586-025-09833-y):摘要原文 "an AlphaZero-inspired agent that learns to find formal proofs through RL by training on millions of auto-formalized problems. For the most difficult problems, it uses test-time RL, a method of generating and learning from millions of related problem variants at inference time"; IMO 2024 "solved three out of the five non-geometry problems ... this performance, achieved with multi-day computation, resulted in reaching a score equivalent to that of a silver medallist"。DeepMind 2024 博客:28/42;"The problems were manually translated into formal mathematical language";"took up to three days"。Lean 是硬裁判,自产问题+自证=L2 级自训练,但题目翻译由人做。
- C22 【承重】FLT 形式化(Anthropic 2026-09-04, anthropic.com/research/formalizing-fermats-last-theorem):"In 11 days, working largely autonomously, Claude produced the first end-to-end, computer-checked proof of FLT";"13 million lines of Lean and proved 29,500 intermediate theorems";"about six billion output tokens from a general-purpose internal research model roughly comparable to Claude Fable 5.1";人类输入 "limited to occasional high-level instructions from Tianyi"(Tianyi Peng);沿用 Darmon–Diamond–Taylor 简化版 Wiles 证明并 "adapts pieces from the Imperial College London FLT project"。Buzzard 复核:只用 Lean 三条标准公理,comparator 确认定理陈述与 Mathlib 的 FLT 陈述一致。厂商自报 + 外部专家复核陈述。
- C23 FLT 的口径边界:Anthropic 自述 "what's novel here is the verification";Buzzard(TNW 转述)称其 "faithfully follows the early literature on the proof and adds nothing",13M 行暂进不了 Mathlib(不接受 AI 评审,积压 ~3000 PR)。= 硬裁判下的 L0 产出规模化,不是新数学,也不是改进改进能力。
- C24 OpenAI Astra 十题(2026-08-01):内部 Astra 模型对 10 个开放 ≥10 年问题给出新结果(非 sofic 群构造、Connes rigidity 反证、3 个 Erdős 问题等),附 Lean 4 证明、sorry=0,算力约 $2,000(媒体转述 OpenAI)。独立人工审计 preprint(Sienicki & Sienicki, arXiv 2608.14673):"No confirmed substantive mathematical error in a principal result remains in the examined assessments",但审阅深度不一、部分依赖仅部分核查。
- C25 Navier–Stokes(OpenAI 2026-09-08,原帖 openai.com/index/navier-stokes-solution 403 未能直读):对每个正黏度构造光滑紧支外力 + 由静止出发的光滑解,有限时间速度爆破、动能有界;166 页论文 + Lean;~10,000 并行 agent、88 小时、270 万消息、约 1300 亿 token,随后 ~17 小时 Lean 形式化(媒体转述)。边界:带外力(Fefferman 的 (C)(D) 选项),"leaving the behavior of a fluid that nothing pushes as an open problem"(Tufts Daily);Clay 9-11 称 "apparently been settled" 但需同行评审,状态 "active";Buckmaster/Alpöge 同期(早 ~12 小时)Euler 结果引发优先权争议;Córdoba 称无人类既有工作 AI 解不出。
- C26 【反方】25 位菲尔兹奖得主公开信(2026-09-11,Tao 博客):"solving problems is only a tool and proxy for achieving the primary goal of conceptual understanding and insight";"the mass production at faster and faster pace of 'true/false' statements could destroy fertile ground"。——硬裁判(真/假)只覆盖数学价值的一部分。
- C27 【自欺反例,软裁判】2025-10 OpenAI Kevin Weil 称 GPT-5 "解决" 10 个 Erdős 问题;erdosproblems.com 维护者 Thomas Bloom 称 "a dramatic misrepresentation"(模型其实是找到已有文献);Hassabis 称 "embarrassing"(TechCrunch 2025-10-19,媒体)。对比 2026 有 Lean 证书的 Astra 十题——同一公司在加了形式化裁判后口径可信度显著上升。

## 小结(本线对核心假说的贡献)
1. 所有 L0 成果都位于"可自动打分"格子(时间/正确性/数值界/Lean 通过),厂商自己把此列为主要限制(C13)。
2. 唯一公开的闭环(AlphaEvolve→Gemini 训练)是一次性 1%,周期以月计,厂商自称"moderate"(C05, C10);一周年报告未给第二轮数字(C18)。无"每轮增益递增"证据。
3. AlphaEvolve 的能力增长随底座 LLM(C12),说明驱动力是外部常规模型迭代,不是回路自复利。
4. 硬裁判也会被 hack(C15),且只裁"真/假",不裁"有无洞见/理解"(C16, C26)。
5. 加速方最强证据:Lean 作为裁判让规模化跃迁(FLT 13M 行/11 天;Astra 十题 $2k;NS 88h)——裁判越硬,生成越能放量;ThetaEvolve 显示"学会进化"能迁移(C20)。这正支持"瓶颈在裁判"而非否定它。

## Open questions
- AlphaEvolve 加速的 Gemini kernel 训练出的下一代 Gemini 是否已驱动新版 AlphaEvolve?有无第二轮训练加速数字(>1%?)——公开资料未见。
- 0.7% 算力回收、TPU 电路入硅均无独立测量;0.7% 是否随时间衰减或已被后续调度变更吸收?
- AlphaDev 70% 的分母(哪个基准、哪个旧实现)与 libc++ 实际合并的 diff 规模;GPT-4 能否复现同样改动的说法(Papailiopoulos 推文)未核实一手。
- FLT:Prove2Me 平台归属、"Fable 5.1 相当"的内部模型具体是什么;定义层语义是否全部人工核查(comparator 只保证最终陈述)。
- Navier–Stokes:OpenAI 原帖被 403 挡,数字(10,000 agent/88h/130B token/17h Lean)均为媒体转述,需二次确认;Lean 形式化覆盖范围(是否含全部分析引理、是否引入额外公理)未核。
- Astra 审计 preprint 作者独立性与资质待查;"$2,000" 口径(Sol API rates)待一手确认。
- 菲尔兹奖得主公开信签名人数:Wikipedia 写 28,Tao 博客/多数媒体写 25——以 25 为准待确认。
- Tao 等论文中 67 题的具体改进比例未在摘要给出。
