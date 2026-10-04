# 线 T:理论与"复利"定义(截至 2026-10-03)

所有 verbatim 均为实际读到的原文(PDF 经 pdftotext 抽取或页面 curl 后字符串核对);标 [WF] 的是 WebFetch 摘要转述、未逐字核对。

## A. 原始出处

T1 Good 1965/66 原句(languagelog PDF Good1964.pdf, p.33):
"Let an ultraintelligent machine be defined as a machine that can far surpass all the intellectual activities of any man however clever. Since the design of machines is one of these intellectual activities, an ultraintelligent machine could design even better machines; there would then unquestionably be an "intelligence explosion," and the intelligence of man would be left far behind ... Thus the first ultraintelligent machine is the last invention that man need ever make, provided that the machine is docile enough to tell us how to keep it under control."
URL: https://languagelog.ldc.upenn.edu/myl/Good1964.pdf  — 注意:Good 的"unquestionably"没有处理递减回报;Cunningham et al. 2026 与 Davidson et al. 2026 都明确反驳这一步。

T2 Schmidhuber Gödel Machine (arXiv cs/0309048):
"such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful ... We show that such a self-rewrite is globally optimal - no local maxima! - since the code first had to prove that it is not useful to continue the proof search for alternative self-rewrites."
→ 裁判=形式证明。URL: https://arxiv.org/abs/cs/0309048

T3 Darwin Gödel Machine (Zhang, Hu, Lu, Lange, Clune 2025, arXiv 2505.22954):
"Unfortunately, proving that most changes are net beneficial is impossible in practice. We introduce the Darwin Gödel Machine (DGM), a self-improving system that iteratively modifies its own code ... and empirically validates each change using coding benchmarks." SWE-bench 20.0%→50.0%, Polyglot 14.2%→30.7%.
→ 把"证明裁判"换成"基准裁判":直接支持"瓶颈在 oracle"假说。

T4 Bostrom 2014 (经 LessWrong 读书会转录,非原书直接核对):
"Rate of change in intelligence = Optimization power/Recalcitrance" ;crossover = 进一步改进主要由系统自身行动驱动的点。
URL: https://www.lesswrong.com/posts/GT8uvxBjidrmM3MCv/superintelligence-6-intelligence-explosion-kinetics

T5 Yudkowsky 2013 Intelligence Explosion Microeconomics (MIRI):
"I identify the key issue as returns on cognitive reinvestment—the ability to invest more computing power, faster computers, or improved cognitive algorithms to yield cognitive labor which produces larger brains, faster brains, or better mind designs." ;并提议 "formalize return on investment curves, so that each stance can formally state which possible microfoundations they hold to be falsified by historical observations."
URL: https://intelligence.org/files/IEM.pdf

T6 Chalmers 2010 "proportionality thesis"(consc.net/papers/singularity.pdf):
"it holds that increases in intelligence (or increases of a certain sort) always lead to proportionate increases in the capacity to design intelligent systems ... It might fail because there are points of diminishing returns: perhaps beyond a certain point, a 10% increase in intelligence yields only a 5% increase at the next generation, which yields only a 2.5% increase at the next generation, and so on. It might fail because intelligence does not correlate well with design capacity"
→ 这是"每轮增益是否递增"的最早可检验表述(几何衰减 = 收敛,不爆炸)。

## B. 经济学参数:r、σ、β

T7 Bloom, Jones, Van Reenen, Webb (AER 2020): "The number of researchers required today to achieve the famous doubling of computer chip density is more than 18 times larger than the number required in the early 1970s." 正文:研究生产率年均降 6.8%。

T8 Besiroglu, Erdil, Ho (Epoch, 2024-05-17):Stockfish r ≈ 0.83 (SE 0.15);其他领域中位 r>1 但不显著;"we do not believe the current empirical data provides strong evidence for the possibility of a software singularity." [WF 摘要,0.83/0.15 与 NBER 文中引用一致]
URL: https://epoch.ai/blog/do-the-returns-to-software-rnd-point-towards-a-singularity

T9 Davidson & Houlden (Forethought, 2025):定义 "r gives the number of times software doubles for each time the cumulative work on software R&D doubles";"our best guess for r should perhaps be ~1-4, though with high uncertainty";控硬件后 "we might reduce our best-guess estimate of r to ~0.5-2";硬件 r 历史 ~7、GPU 2006–2022 ~5;结论 "at least decently likely that an SIE would occur if hardware were held constant ... though we can't be confident either way."
URL: https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion

T10 Davidson & Houlden "How quick and big":"the software intelligence explosion will probably (~60%) compress >3 years of AI progress into <1 year, but is somewhat unlikely (~20%) to compress >10 years into <1 year." 同文:"Erdil & Barnett (2025) express scepticism about an software intelligence explosion lasting for more than one order of magnitude of algorithmic progress."
URL: https://www.forethought.org/research/how-quick-and-big-would-a-software-intelligence-explosion-be

T11 Ho & Whitfill (Epoch Gradient Updates, 2025-11-14):前沿实验室 2022-11 后 g_K≈1.3, g_L≈0.85, g_A≈1.1(以 e 为底);ε_K≈0.67(计算份额 0.59–0.75 取均值);"all our estimates of λ/β should be cut by a factor of three, which puts them all below 1."(Cobb-Douglas 计算瓶颈调整)
URL: https://epoch.ai/gradient-updates/the-software-intelligence-explosion-debate-needs-experiments

T12 Whitfill & Wu (arXiv 2507.23181):4 家实验室(OpenAI, DeepMind, Anthropic, DeepSeek)2014–2024 面板;基线 CES σ=2.58(替代),"frontier experiments" 规格 σ=−0.10(强互补)。[WF 摘要,数字与多处二手一致]

T13 Erdil & Barnett (Epoch 2025-03-21):"If the two inputs are indeed complementary, any software-driven acceleration could only last until we become bottlenecked on compute and end up having to do the physical work of obtaining more GPUs"; 私营 R&D 仅占美国 TFP 增长 "0.2%/yr ... compared to around 0.8%/yr of total TFP growth" (1988–2022)。
URL: https://epoch.ai/gradient-updates/most-ai-value-will-come-from-broad-automation-not-from-r-d

T14 Erdil (Epoch 2025-04-26):"Software R&D in AI seems bottlenecked by experimental compute and data as well as cognitive research effort. If we were to simply scale up cognitive effort by many orders of magnitude while leaving other factors mostly untouched, these bottlenecks would probably become binding and any potential singularity would fizzle out."
URL: https://epoch.ai/gradient-updates/the-case-for-multi-decade-ai-timelines

T15 Davidson, Halperin, Houlden, Korinek, NBER w35155 (2026-10 版):explosion condition 校准 "fY + 1 · fS + 5 · fH + 0.53 · fA > 1";β_A=3.1(Bloom), β_H=0.2, r_S=1(Erdil et al. 2024 保守取值);"13% automation across all sectors is sufficient ... 17% suffices when only software and hardware research are automated";"automating software in isolation is approximately at the knife-edge";"fully automating software research plus 5% automation elsewhere generates a singularity within six years"(作者称 "a stylized exercise rather than a forecast")。Ho & Whitfill 直接估 r_S 1.2–1.8。
URL: https://basilhalperin.com/papers/singularities.pdf ;利益:Korinek 署名 "Anthropic Institute",Davidson 属 Forethought。

## C. 2026 新进展(8–10 月)

T16 Chan, Mindermann et al. (22 作者含 OpenAI Pachocki、Anthropic Clark、Hinton、Bengio;GovAI Frontier AI WP 2/2026, 2026-09-28):
"Using historical data on AI progress, Ho and Whitfill [28] find central estimates of r between 1.2 and 1.9 across three subfields of AI research. Though uncertainty is substantial, these results suggest radical acceleration after full automation: if r stayed at these levels and no other bottlenecks emerged, the pace of AI progress would increase tenfold within about 1.5 years, at which point a year's worth of progress at today's pace would take about five weeks."
脚注 6:90% CI (0.727–2.094), (0.380–2.708), (1.069–3.212)。
附录:"ω = 1.40 and ε = 1.01 ... each doubling of A multiplies the growth rate by 2^0.39 ≈ 1.31, so each subsequent doubling takes (1/2)^0.39 ≈ 76% as long as the last." 首个翻倍取 4.5 个月(训练效率)。
自我批评:"Existing estimates of r come from a period of rapid compute scaling ... Such confounding would bias estimates of r upward: in a regime of fixed or slowly growing compute, r would be lower than historical data suggest." 脚注 4:"we only consider increases in labor ... This means the value of r is lower than if we considered increases in all inputs"。脚注 5:"r must eventually drop below 1"。
"Productivity gains from AI R&D automation have not yet reached the threshold needed to trigger an intelligence explosion, but gains from newer systems are likely approaching that threshold [37]."
计算:"The limited available data suggest that a software-driven intelligence explosion is not possible if such experiments require proportionally more compute as frontier training runs grow [29]."
URL: https://www.governance.ai/research-paper/what-if-automating-ai-r-d-triggers-an-intelligence-explosion (PDF: casp.ac 链接)
注意:Ho & Whitfill 1.2–1.9 是"未扣计算瓶颈"的数;同作者扣 ε_K 后 <1(T11)。

T17 Cunningham, Althoff, Halperin, Jabarian, Koh, Ramani, Trammell, Whitfill, Wu "The Economics of Recursive Self-Improvement"(Elasticity Institute/METR, arXiv 2609.15802, 2026-09-14;METR note 2026-07-22):
定义 "Self-sustaining acceleration: When AI systems are sufficient for accelerating progress in AI capabilities without any growth in exogenous inputs (human labor, training compute, etc.)";"Intelligence explosion: When AI capabilities go to infinity in finite time."
条件:ε_A,A > 1(净回路弹性之积>1)。校准:"the condition is met if a one-unit increase in AI model capabilities results in at least 15% higher AI R&D productivity. A rough back-of-the-envelope calculation based on reported AI engineer uplift suggests this return has been around 9% since the launch of coding agents. This number is below the model-implied threshold, suggesting we are not experiencing a self-sustaining acceleration." 9% 来自 Mythos Preview 系统卡自报 4X uplift("very likely to be an overestimate")。ε_C,A≈6.5;"ε R,C . We have almost no evidence for this parameter"。
Narrow vs broad:"AI systems improve narrowly at optimizing AI R&D benchmarks without improving at broader economically valuable tasks."
专家/超级预测者 2025-08:三倍有效算力增速至 2029 概率 20%/8%。

T18 Ord "The Dynamics of Intelligence Explosions" (arXiv 2608.14426, 2026-08-14, rev 08-25):
"singular growth (towards a vertical asymptote) is harder to achieve than would be expected from recent economics-inspired modelling ... one cannot have singular growth unless the generation time rapidly approaches zero." "it seems highly unlikely that generation times can be brought arbitrarily close to zero." "Doubling time shrinking towards zero is a useful threshold for defining super-exponential growth, but it is only generation time that can set the threshold for singular growth."

T19 Burtsev "Recursive Criticality of AI Self-Improvement" (arXiv 2609.00137, 2026-08-31):R_AI(递归再生数)"When R_AI>1, the effects of improvements compound across development cycles ... A system can therefore enter a self-amplifying regime before acceleration becomes visible, while rapid progress can also occur without self-amplification." "improvements shared across organizations can make the overall research ecosystem self-amplifying even when no individual actor is."

T20 Naam (Noahpinion 2026-09-27, 怀疑方,从业者博客):"Inside OpenAI, though, the July research-task horizon at 80% success was roughly 15 minutes ... A four-hour benchmark horizon is about 16 times longer than OpenAI's research horizon." "I use 2–3% productivity gain per ECI point ... 2–3% per ECI point against a 15–19% threshold leaves a roughly five- to tenfold gap." "AI is helping build better AI. Under this estimate, though, each turn of the loop adds less than the last." ECI "What looked like acceleration now appears more consistent with a one-time jump." 芯片容量约 127 倍(三年余)。

T21 AI Futures Model Dec 2025 update (Lifland, Halstead, Kastner, Kokotajlo, 2025-12-31):"predicts longer timelines to full coding automation than our previous model by about 3-5 years, in significant part due to being less bullish on pre-full-automation AI R&D speedups";"To achieve a fast takeoff, there usually needs to be a feedback loop such that each successive doubling of AI capabilities takes less time than the last ... taste-only singularity"。
titotal 批评(经作者回应转述):"very little empirical validation of the model",超指数建模 "no empirical backing";AI 2027 作者承认超指数论证 underdeveloped。

## D. "复利 / R" 的可检验定义候选(本线独占产出)

1. 半内生 r(Davidson/Houlden;Ho/Whitfill):r = 软件翻倍数 / 累积研发投入翻倍数。r>1 → 每次翻倍所需时间递减。可检验量:相继翻倍时间比 (1/2)^(r−1);r=1.39 时 ≈0.76。观测指标:算法效率翻倍间隔是否在固定算力下缩短。
2. 回路弹性之积 ε_A,A>1(Cunningham et al.):可操作化为"每 +1 ECI,研发生产率 +≥15%"。现估 9%(厂商自报 uplift 上界)/ 2–3%(Naam)。这是"改进改进能力"(R)的直接测度,而非产出改进。
3. 世代增益比(Chalmers):第 n+1 代增益 / 第 n 代增益 >1? 10%→5%→2.5% 为收敛反例。
4. 世代时间(Ord):奇点需 T_n→0 足够快(Σ T_n 收敛);只看 doubling time 缩短不足以判定 singular。
5. R_AI(Burtsev):反馈强度 / 难度上升率;可在不可见加速前就 >1,也可快速进步而 <1——提醒"看到快"≠"在复利"。
6. 自持 vs 外生:必须控制外生投入(人力、训练算力)。Cunningham 定义要求"without any growth in exogenous inputs";否则投资驱动的加速会被误读为 RSI。

## Open questions
- Ho & Whitfill r:Gradient Updates 文给"语言模型 90% CI 超过 1",NBER 引 1.2–1.8,GovAI 引 1.2–1.9;同作者扣计算份额后全部 <1。哪一个是"正确口径"取决于 σ(2.58 vs −0.10),而 σ 本身两个规格相反。
- 9%/ECI 的分子来自 Anthropic 员工自报 4X uplift(Mythos Preview 系统卡),作者自己认为高估;METR 2025 RCT(Becker et al.)曾测得负效应。
- Anthropic "26% leads" 为自评(Claude 自己打分多),GovAI 论文直接引用;需 L3 线交叉。
- OpenAI 内部 80% 成功研究任务时长 ~15 分钟(Naam 引 7 月数据) vs METR 外部 ~4 小时:16 倍差距是否同口径?
- Forethought 两篇文章确切发布日期未核(约 2025 年 3 月 / 8 月)。
- Bostrom 原书引文为二手转录。
