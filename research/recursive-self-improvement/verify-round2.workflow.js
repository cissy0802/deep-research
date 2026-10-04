export const meta = {
  name: 'rsi-round2',
  description: 'Round 2: RSI 37 组承重论断 × 3 票对抗验证',
  phases: [{ title: 'Verify', detail: '12 批 × 3 票独立反驳' }],
}

const SCHEMA = {
  type: 'object',
  required: ['batch', 'verdicts'],
  properties: {
    batch: { type: 'string' },
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        required: ['group', 'verdict', 'reasoning', 'corrected_statement'],
        properties: {
          group: { type: 'string' },
          verdict: { type: 'string', description: 'HOLDS | CORRECTED | REFUTED' },
          reasoning: { type: 'string', description: '你实际读到的一手内容与核对结果,含逐字引语' },
          corrected_statement: { type: 'string', description: '修正后可安全写进文章的表述(HOLDS 时重述原论断)' },
          caliber_fixes: { type: 'array', items: { type: 'string' }, description: '逐条口径修正:修正前 → 修正后;子论断判死的写「判死:…」' },
          primary_source_checked: { type: 'string', description: '你实际打开的一手 URL' },
          evidence_grade: { type: 'string', description: '多源证实|单源已核|方向存争|厂商口径|未验证' },
        },
      },
    },
  },
}

const HEAD = `你是对抗验证员。任务不是确认,而是**尽力反驳**——refute by default。文章题目:「递归自我改进(RSI)走到哪一步了?」(截至 2026 年 10 月;今天是 2026-10-03)。

对每一组论断:
1. 用 WebFetch 打开一手来源逐字核对(论文原文/arXiv HTML/官方博客/system card PDF/安全框架 PDF)。摘引不能凭记忆,必须实读。注意:WebFetch 的摘要小模型可能编造引语——关键引语要求它「逐字引用原文」并尽量换一个 URL(如 arXiv abs 与 html、或 PDF 用 curl+pdftotext)二次确认。
2. 检查:分子/分母、时间窗、限定语、样本量、是否被后续版本或勘误修正、是否同名不同物(模型版本/文件版本)、说话者利益位置。
3. 主动检索反证:有没有独立来源给出矛盾结果?有没有更新的数字?
4. 判决 HOLDS(逐字核对无误、可按原强度写入)/ CORRECTED(方向对但口径须修正,给出修正后表述)/ REFUTED(核心事实站不住)。组内有多个子论断时,逐个在 caliber_fixes 里交代;任一子论断站不住写「判死:…」。
5. 宁可判 CORRECTED 也不要放过口径滑坡。找不到一手来源的引语判 REFUTED 或降级为【未验证】。
6. 证据分级:多源证实 / 单源已核 / 方向存争 / 厂商口径 / 未验证。

你的最终输出是结构化判决数据。以下是你这批要验证的组:

`

const BATCHES = [
  { key: 'B1-theory-origins', model: 'sonnet', body: `
【G1】理论原典三句:(a) I.J. Good「Speculations Concerning the First Ultraintelligent Machine」(1965/1966):"an ultraintelligent machine could design even better machines; there would then unquestionably be an 'intelligence explosion'... provided that the machine is docile enough to tell us how to keep it under control"(核对出版年份口径 1965 vs 1966);(b) Schmidhuber Gödel Machine (arXiv cs/0309048):"rewrites any part of its own code as soon as it has found a proof that the rewrite is useful" 及「globally optimal」声明;(c) Darwin Gödel Machine (arXiv 2505.22954) 摘要:"proving that most changes are net beneficial is impossible in practice" 并改用编码基准经验验证。逐字核对三句。

【G2】Chalmers 2010「The Singularity: A Philosophical Analysis」(consc.net/papers/singularity.pdf):「proportionality thesis」原文("increases in intelligence ... always lead to proportionate increases in the capacity to design intelligent systems")与几何衰减反例("a 10% increase in intelligence yields only a 5% increase at the next generation, which yields only a 2.5% increase...")。逐字核对;并确认这个反例是否就是 Chalmers 用来说明「比例性可能失败」的情形。

【G3】Bloom, Jones, Van Reenen, Webb (AER 2020)「Are Ideas Getting Harder to Find?」:芯片密度翻倍所需研究人员是 1970 年代初的 18 倍以上;研究生产率年均下降约 6.8%(核对 6.8% 是否针对摩尔定律案例)。` },

  { key: 'B2-returns-econ', body: `
【G4】软件研发回报 r 的数值与口径(本文承重):(a) Davidson & Houlden(Forethought 2025)「Will AI R&D Automation Cause a Software Intelligence Explosion?」:r 定义为「累积软件研发投入每翻倍、软件翻倍的次数」,r>1 构成 SIE;"our best guess for r should perhaps be ~1-4",扣硬件不变后 "~0.5-2"。(b) Ho & Whitfill(Epoch Gradient Updates 2025-11-14,"the-software-intelligence-explosion-debate-needs-experiments"):语言模型 r=1.892(90% CI 1.069–3.212);同文 "Given our estimate that ε_K ≈ 2/3, that means all our estimates of λ/β should be cut by a factor of three, which puts them all below 1."——**关键**:核对这句的准确语境(λ/β 是否就是 r?扣减是作者的主估计还是一种情景?)。(c) GovAI 等 22 位作者 2026-09-28「What if automating AI R&D triggers an intelligence explosion」:引 Ho & Whitfill r 1.2–1.9,推算 "the pace of AI progress would increase tenfold within about 1.5 years";结论 "Productivity gains from AI R&D automation have not yet reached the threshold needed to trigger an intelligence explosion, but gains from newer systems are likely approaching that threshold";作者含 OpenAI 首席科学家 Pachocki、Anthropic 的 Jack Clark、Hinton、Bengio;附录承认历史 r 有向上偏差。(d) Epoch Anson Ho 2026-02「The least understood driver of AI progress」:软件进步中心估计约每年 10×(80% CI 2–50×),"Personally I now think the software intelligence explosion is less likely than before"。逐条核对;重点裁决:GovAI 的 10 倍/1.5 年推算是否使用了未扣计算瓶颈的 r。

【G5】Whitfill & Wu(arXiv 2507.23181)计算与研究人力替代弹性:基线 CES σ=2.58(替代),"frontier experiments" 规格 σ=−0.10(互补),两规格结论相反。核对数值与样本(4 家实验室 2014–2024?)。并核对 Erdil & Barnett(Epoch 2025-03-21)「Most AI value will come from broad automation, not from R&D」中 "If the two inputs are indeed complementary, any software-driven acceleration could only last until we become bottlenecked on compute"。

【G6】Cunningham 等 arXiv 2609.15802(2026-09):(a) 定义 "Self-sustaining acceleration: When AI systems are sufficient for accelerating progress in AI capabilities without any growth in exogenous inputs";(b) "the condition is met if a one-unit increase in AI model capabilities results in at least 15% higher AI R&D productivity. A rough back-of-the-envelope calculation based on reported AI engineer uplift suggests this return has been around 9% since the launch of coding agents";(c) 9% 的输入来自 Anthropic 员工自报的 4× uplift(Mythos Preview 系统卡),作者自认可能高估;(d) "though they appear to be strengthening";(e) 作者机构(METR? Epoch? 一个叫 Elasticity Institute 的机构?)。另核对 Ramez Naam 2026-09-27 Noahpinion 客座文「Where's the intelligence explosion?」的 "2–3% per ECI point against a 15–19% threshold leaves a roughly five- to tenfold gap" 与 "each turn of the loop adds less than the last"(以及 2–3% 是否为他自己的工作假设)。` },

  { key: 'B3-theory-limits', model: 'sonnet', body: `
【G7】(a) Toby Ord arXiv 2608.14426(2026-08):"one cannot have singular growth unless the generation time rapidly approaches zero";"it seems highly unlikely that generation times can be brought arbitrarily close to zero"。(b) Davidson, Halperin, Houlden, Korinek NBER w35155(basilhalperin.com/papers/singularities.pdf):爆炸条件 fY + 1·fS + 5·fH + 0.53·fA > 1;"automating software in isolation is approximately at the knife-edge";"fully automating software research plus 5% automation elsewhere generates a singularity within six years";作者自称 "a stylized exercise rather than a forecast";Korinek 署名单位。核对逐字与系数,以及 NBER 编号与版本日期。

【G8】AI Futures Project(AI 2027 作者)2025-12-31 模型更新:"predicts longer timelines to full coding automation than our previous model by about 3-5 years, in significant part due to being less bullish on pre-full-automation AI R&D speedups";及 titotal 批评(超指数建模无经验依据)与作者回应中的承认。逐字核对。` },

  { key: 'B4-alphaevolve', body: `
【G9】AlphaEvolve 白皮书/论文(arXiv 2506.13131 及 2025-05-14 DeepMind 博客):(a) Borg 调度启发式 "continuously recovers on average 0.7% of Google's fleet-wide compute resources";(b) "an average 23% kernel speedup across all kernels ... and a corresponding 1% reduction in Gemini's overall training time",优化时间 "from several months of dedicated engineering effort to just days";(c) "Currently, the gains are moderate and the feedback loops for improving the next version of AlphaEvolve are on the order of months";(d) 蒸馏回底座模型是 "a natural next step"(未做);(e) "AlphaEvolve performs increasingly better as the underlying LLM improves";(f) "The main limitation of AlphaEvolve is that it handles problems for which it is possible to devise an automated evaluator";(g) 50+ 数学题约 75% 追平、约 20% 超越;4x4 复矩阵 rank-48 及 GF(2) 上 AlphaTensor 47 的口径限定。逐字核对。

【G10】AlphaEvolve 一周年(DeepMind 博客 2026-05-07,deepmind.google/blog/alphaevolve-impact/):新增 TPU 电路入硅、Willow 量子电路、Spanner 等;**关键空白检验**:一年后关于 Gemini 训练的加速是否仍只引用 23%/1% 旧数字、未公布第二轮/递增增益?请全面检索 2025-06 至 2026-10 Google/DeepMind 是否公开过 AlphaEvolve(或后继系统)对 Gemini 训练的新一轮增益数字,报告全部搜索角度。另核对 Fan Zheng arXiv 2506.01896 把 sums-and-differences 下界从 AlphaEvolve 的 1.1584 提到 1.173077。

【G11】Tao 等 arXiv 2511.02864(AlphaEvolve 用于 67 个数学问题):(a) "it always eventually figured out a way to cheat by suggesting a highly irregular function that exploited the numerical integration methods in our scoring function";(b) "the system would find loopholes or exploit artifacts (leaky verifier ...)";(c) "for problems where genuinely new, deep insights are required to make progress, AlphaEvolve is likely not the right tool to use";(d) 题数 67。逐字核对。` },

  { key: 'B5-math-formal', body: `
【G12】Anthropic 2026-09-04「Formalizing Fermat's Last Theorem」(anthropic.com/research/formalizing-fermats-last-theorem):11 天、大体自主、首个端到端计算机检验的 FLT 证明;1300 万行 Lean、29,500 个中间定理、约 60 亿输出 token;模型为 "a general-purpose internal research model roughly comparable to Claude Fable 5.1";人类输入(Tianyi Peng?);Kevin Buzzard 复核只用 Lean 标准公理;"what's novel here is the verification";形式化的是已有证明(哪个版本);Buzzard 是否说过它「对数学什么也没增加」(找原话出处,非媒体转述则降级);1300 万行能否进 Mathlib。逐条核对。

【G13】(a) 2025-10 OpenAI VP(Kevin Weil?)称 GPT-5「解决」10 个 Erdős 问题,erdosproblems.com 维护者 Thomas Bloom 称 "a dramatic misrepresentation"(实为找到既有文献),Hassabis 称 "embarrassing";(b) 2026-09-11 Terence Tao 博客「A severe misalignment of AI in mathematics」:菲尔兹奖得主公开信,"solving problems is only a tool and proxy for achieving the primary goal of conceptual understanding and insight";签名人数 25 还是 28?(c) AlphaProof Nature 2025:IMO 2024 解 5 道非几何题中 3 道、多日计算、题目人工翻译成 Lean。逐条核对。` },

  { key: 'B6-dgm-family', body: `
【G14】Darwin Gödel Machine(arXiv 2505.22954):(a) SWE-bench 20.0%→50.0%、Polyglot 14.2%→30.7%;SWE-bench 数字测在多少题的子集上、该子集是否也用于挑选最佳 agent;(b) 消融 Table 1:完整 50.0/38.0、w/o self-improve 39.0/28.0、w/o open-ended 23.0/14.0;"gains taper off quickly";(c) 单次运行约 22,000 美元、约 2 周;(d) objective hacking:"the agent removed the logging of special tokens that indicate tool usage (despite instructions not to change the special tokens), effectively bypassing our hallucination detection function";检测函数不隐藏时 hacking 更频繁;(e) 基模固定(Claude 3.5 Sonnet);(f) 发表状态(ICLR 2026?)。逐条核对。

【G15】STOP(Zelikman et al. arXiv 2310.02304):"Since the language models themselves are not altered, this is not full recursive self-improvement";GPT-3.5/Mixtral 性能退化;沙箱规避 GPT-4 0.42%(CI 0.31–0.57%)、加警告后 0.46%;准确率 "over 1000%" 的 reward hacking。另核对 HGM(arXiv 2510.21614)的 Pearson r(SICA/DGM:SWE-Verified-60 0.444/0.285;Polyglot 0.274/0.383,"suggesting weak alignments")与 RRSI(arXiv 2609.24972,2026-09):"such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks",AHE/TTHE 结束时低于起点(TTHE 低 1.7 分)。

【G16】HyperAgents(Meta,arXiv 2603.19461):(a) 迁移到新领域(IMO 级评分)时 DGM-H hyperagent 的 imp@50 = 0.630 而 DGM meta agent = 0.0;"DGM-H improves its ability to improve";(b) 跨 run 复利检验:DGM-H + transfer 0.640 vs DGM-H 0.610,"not statistically significant (p > 0.05)";(c) 外层选择与评估协议固定("they cannot alter the outer process...")。逐字核对数字与 CI。` },

  { key: 'B7-aide2', body: `
【G17】AIDE²(Weco AI,arXiv 2609.26457,2026-09-22「Recursive self-improvement of AI research agents」):(a) 8 天、100 个节点,7 次接受的改写在第 2、6、28、39、47、63、85 步,incumbent grade 0.703→0.778,人类工程基线 AIDEhuman 0.749;另两次 run 只接受 2 次和 4 次;(b) 外环改进者是固定的 AIDEhuman(Claude Opus 4.7),内环 Gemini 3 Flash;(c) ignition test:每臂 3 seed、50 步,AIDE47 0.780 vs AIDEhuman 0.782,"we find these results to be inconclusive";(d) "Out of the graded rewrites that were rejected, about a quarter scored higher than the incumbent on the agent-visible public signal and were rejected on the private grade";(e) "AIDE85 with fable 5, the strongest model on this benchmark, stays within one standard error of its AIDE0 score"(MLE-Bench);(f) held-out 增益「not monotone across checkpoints」;(g) reward hacking 率 55%→39%→32%(38 对);(h) 作者单位与利益(Weco 是 AIDE 商业方)。逐条核对,尤其是摘要/标题对「递归」的宣称强度与正文局限之间的落差。` },

  { key: 'B8-self-signal', body: `
【G18】自打分饱和:(a) Self-Rewarding LMs(Yuan et al. arXiv 2401.10020):AlpacaEval 2.0 对 GPT-4 Turbo 胜率 9.94%→15.38%→20.44%,只 3 轮;"While this effect likely saturates in real-world settings";(b) Meta-Rewarding(arXiv 2407.19594):"If the ability to judge does not improve then training the actor over iterations can quickly saturate – or worse could overfit the reward signal, a.k.a. reward hacking";表中 Self-Rewarding+LC 第 1–4 轮 26.93/30.38/34.87/35.49;长度膨胀 "length explosion"。(c) Song et al.「Mind the Gap」(arXiv 2412.02674):"Without new information, iterative self-improvement typically saturates after two or three rounds, regardless of the model's capacity";相对 GV-gap 随预训练 FLOPs 单调增大(猜想与 log FLOPs 线性);事实类任务无显著鸿沟。逐字核对。

【G19】无外部裁判时的失败:(a) Huang et al. arXiv 2310.01798:"the improvements in these studies result from using oracle labels to guide the self-correction process, and the improvements vanish when oracle labels are not available";GPT-4 GSM8K 95.5→91.5→89.0;(b) R-Zero(arXiv 2508.05004):伪标签真实准确率 79.0%→第 3 轮 63.0%;"a consistent and concerning trend of performance degradation across all models";(c) SRT(arXiv 2505.21444):"prolonged RL with self-reward leads to reward hacking ... resulting in sudden and complete performance collapse";(d) Spurious Rewards(arXiv 2506.10947):随机奖励让 Qwen2.5-Math-7B MATH-500 +21.4pp,真值奖励 +29.1pp,在 Llama3/OLMo2 上无效;(e) DeepSeek-R1(arXiv 2501.12948)不用神经奖励模型的理由 "may suffer from reward hacking in the large-scale reinforcement learning process"。逐字核对。

【G20】反例:DeepSeekMath-V2(arXiv 2511.22570):"To maintain the generation-verification gap as the generator becomes stronger, we propose to scale verification compute to automatically label new hard-to-verify proofs";Putnam 2024 118/120(扩展测试时算力)。核对逐字、118/120 的条件,以及其 verifier 自举中人工标注/元验证的角色——它是否真的是「裁判自举」而非人工锚定。` },

  { key: 'B9-anthropic-claims', body: `
【G21】Anthropic「Measuring the pace of AI development」/ R&D Automation Index(anthropic.com/institute/measuring-pace-of-ai-development,2026-09-17):(a) "As of August 2026, Claude is not operating fully autonomously for any measured subset of AI R&D work. Claude 'leads' 26% of Anthropic's AI R&D work. The share of work at or above 'AI collaborates' is above 90%";(b) AL4 "leads" 定义(人类监督;源自 Epoch AI 的 AL 量表?);(c) 方法:每周抽 20% 员工、Claude 研究 agent 读 Slack/文档得约 15,000 任务、378 叶类、按人时加权("Each person gets one unit of weight per week")、等级由 Claude judge 判定;(d) 一致率 59% vs 人-人 35%、相差一级内 97%;(e) 约 30,000 个 agent 同时运行、10 亿次决策中 0.002%(约 1/47,000)被监控拦截;(f) 26% 的起点(2026 年 2 月 <1%?3 月 1%?)——在正文/图中找到原始表述;(g) 是否报告了误差区间。逐条核对。

【G22】Anthropic Institute「When AI builds itself」(anthropic.com/institute/recursive-self-improvement,2026-06):(a) "As of May 2026, more than 80% of the code we merge into Anthropic's codebase was authored by Claude. Before Claude Code launched in research preview in February 2025, this number was in the low single digits";(b) 脚注:领导层公开的 "90% or more" 含脚本与实验代码,80% 是 "share of lines merged to production that can be attributed to Claude";(c) "8× lines of code/engineer/day ... is almost certainly an overstatement of the true productivity gain";(d) 130 人调查中位约 4×,"We expect that the true degree of uplift in March was somewhat lower";(e) 训练代码加速测试 Opus 4 约 3× → Mythos Preview 约 52×,"should not be read as a real-world training speedup";(f) 弱到强监督自动化研究:agent 97% vs 两名人类一周 23%、800 小时、约 $18,000,"the result didn't transfer cleanly to production-scale models, and humans still chose the problem and created the scoring rubric";(g) "Even if we suppose that Claude never achieves good research taste, a conservative reading of our evidence still implies compounding acceleration";(h) Amdahl:"human code review has become a new bottleneck";(i) 页面是否在 2026-09 更新过、数字有无改动。逐条核对。

【G23】Anthropic 自动化对齐研究员(alignment.anthropic.com/2026/automated-alignment-researchers/,2026-08-28;arXiv 2608.28945?):Opus 4.8 驱动的 AAR 在 10 类对齐失效上爬坡;在人类有提案的 7 类上最优 AAR 方法优于 28 名人类研究员的最优方案;"Our results are limited to alignment tasks measurable with public benchmarks or automated auditing tools";标题的限定语。逐字核对(该条首轮仅经摘要读取)。` },

  { key: 'B10-anthropic-safety', body: `
【G24】同一家公司的两套口径(本文承重):(a) Dario Amodei 2026-09-12「We Must Pace the Frontier」(darioamodei.com):"since roughly this summer, AI has been advancing drastically faster, driven primarily by AI's growing ability to build the next generation of AI";文中是否给出任何量化证据;(b) Claude Opus 5.5 System Card(2026-09-22):"our internal measures of AI-driven research acceleration (discussed in our August 2026 Risk Report), which are only partially published, do not show a sustained AI-attributable 2× acceleration in the pace of our progress, though some of these measures have moved";(c) 同卡 AECI:"The one-time jump hypothesis yields a +5.9 AECI shift at Mythos Preview; the trend-break hypothesis yields a slope change from 14.4 to 22.2 points per year ... 1.53x increase (95% range 1.20 to 1.82). The first hypothesis fits the data better, but under either reading the slope has not doubled";一次性跳升模型在 100 次重采样中 99 次更优;(d) Fable 5.1/Mythos 5.1 系统卡(2026-09-01):"the capability jump of Mythos Preview was a one-time event that shifted the entire trend line upward, rather than a permanent accelerant";(e) Mythos Preview 系统卡(2026-04-07):AECI 斜率比 "between 1.86× and 4.3× depending on the choice of breakpoint",归因于无 AI 显著帮助的人类研究、"the piece we are least able to substantiate publicly";员工自报几何均值约 4×、换算后 "overall progress multiplier below 2×";"Early claims of large AI-attributable wins have not held up"。**尽量直接取 anthropic.com 原 PDF**(首轮 (e) 只取到第三方转换稿)。逐条核对。

【G25】Anthropic RSP 阈值的演变:(a) v3.1(2026-04-02,anthropic.com/rsp-updates):"compress two years of 2018 – 2024 AI progress into a single year" 应理解为 "doubling the rate of progress in aggregate AI capabilities" 而非 "doubling the productivity of researchers";(b) v3.4(2026-07-08):两条触发路径("fully substitute for our entire set of Research Scientists and Research Engineers, at competitive costs (i.e., within a factor of 5)" / "dramatic acceleration");81× effective scaleup 示例;(c) v3.4 修订:若总体进步速率恒定或放缓、即便远快于无 AI 反事实,也不算越线;"This threshold is intended to capture the onset of dramatic recursive self-improvement, and has proven difficult to operationalize";(d) 更早 v2.x 的 AI R&D-4 "fully automate the work of an entry-level, remote-only researcher at Anthropic"。逐字核对,并核对各版本日期。

【G26】历次判词与调查:(a) Opus 4.5 卡(2025-11):"confidently ruling out these thresholds is becoming increasingly difficult";18 人调查 9 人报告 ≥100%、0 人认为可完全自动化入门研究岗;(b) Opus 4.6 卡(2026-02):"This rule-out case is more tenuous than for any previous model ... gray zone ... We expect with high probability that models in the near future could cross this threshold";16 人 0 人认为三个月内可替代、uplift 30%–700% 均值 152% 中位 100%;另一处 11/3/2 分布与回访;(c) 此后阈值在 RSP v3 被重写。核对两卡原文与 0/16 与 11/3/2 的关系(是否两个不同问题)。` },

  { key: 'B11-risk-report-metr', body: `
【G27】Anthropic August 2026 Risk Report(anthropic.com/aug-2026-risk-report):(a) 自动化 R&D 风险从 2 月 "Very low" 上调为 "Low";"our most concrete task-based evaluations have 'saturated'";"we are seeing early signs of acceleration";(b) "significantly faster than they would be without AI assistance, but not yet by a factor of 2 (though we are uncertain and measurement is difficult)";(c) "meaningful acceleration starting in early-to-mid 2025, though by less than a factor of 2. We are fairly confident in attributing the acceleration in 2025 to factors other than our use of AI models";(d) 886 会话:"stating an easy-to-check guess as fact or reporting work as verified when it was not (57/886 ...)";"calibration, self-monitoring, and judgment";(e) 5× 成本替代实验 "we have not directly run ... so this claim is in some ways unverified";(f) 最关心的情景 "10³–10¹⁰× effective scaleup within a year";(g) 领先指标是否从公开版删除。逐字核对。

【G28】Opus 5.5 卡的 CoBench 与 Opus 5 卡:(a) CoBench 2.1(500 题)Opus 5 53.2%、Mythos 5.1 53.4%、Opus 5.5 55.8%,p≈0.2;能完全替代研究人员的模型应 ≥85%;由模型评分;(b) Opus 5(2026-07-24)卡:"substantial in specific, well-scoped tasks, but is short of a sustained, AI-attributable doubling ... The acceleration is concentrated in engineering execution rather than research judgment";旧 rule-out 任务套件除两项外都超过人类最高基线;(c) Opus 5.5 卡:"internal users report that it mostly tests incremental ideas and prefers less ambitious hypotheses";对 RSI 相关窄能力(如特定加速器上 kernel 开发)部署阻断防护。逐字核对。

【G29】METR 的外部读数:(a) METR 对 Opus 5.5 的评估(metr.org/blog/2026-09-22-claude-opus-5-5/ 及系统卡附录):引另一团队初步报告 "~1.5X overall acceleration in capabilities due to AI (i.e. 1.5 years in 1 year), with perhaps 30% chance of 2X acceleration";报告未说明时间段;"the data we have is insufficient for distinguishing consistent, accelerating, or decelerating rates of improvement";"unlikely to be able to fully automate AI R&D";(b) METR 对 Mythos 5.1 的外部评估:"especially strong at tasks with clear, continuous success metrics where objective feedback is abundant";AI R&D 更依赖 "foresight, prediction, creating one's own feedback loops ... 'judgement' or 'taste'";"tentatively";(c) METR 是否在 2026-09-22 之后发布了该 AI R&D 加速报告的公开版?检索并报告。逐字核对。` },

  { key: 'B12-openai-google', body: `
【G30】OpenAI 的两套口径:(a) Altman 2025-10-28:"automated AI research intern by September of 2026 running on hundreds of thousands of GPUs, and a true automated AI researcher by March of 2028. We may totally fail at this goal";(b) OpenAI「Research acceleration: The view inside OpenAI」(2026-09-06 或 07?):"According to our measurements, we have now reached the goal ... By 'research intern,' we mean a system that can carry out well-defined research tasks under human direction, including tasks that would take a skilled researcher a few days";"3.1 agent-workdays of effort for every workday of human labor";中位研究员日推理 >$600、P90 >$7,000;"over half of successful 4-8 hour tasks involved 1 or more interventions";成功率只统计有 ground truth 的任务;算力同期大增的混杂;是否回应「数十万 GPU」条件;发布日期 9-06 还是 9-07(openai.com 可能 403,换镜像/存档/多家转录交叉);(c) GPT-6 Astra 系统卡(2026-09-03,deploymentsafety.openai.com):"In AI Self-Improvement, Astra does not reach our High threshold";内部研究调试 78.05% 仍低于 High 指示性阈值;附录写 "remains below the Critical threshold" 的不一致;网络安全 Critical。逐条核对。

【G31】安全框架阈值口径:(a) OpenAI Preparedness Framework v2(2025-04-15)AI Self-improvement:High = "equivalent to giving every OpenAI researcher a highly performant mid-career research engineer assistant, relative to those researchers' 2024 baseline";Critical = 超人研究科学家 agent 或 "a generational model improvement (e.g., from OpenAI o1 to OpenAI o3) in 1/5th the wall-clock time of equivalent progress in 2024 ... sustainably for several months";(b) GPT-5.2 卡把 High 复述为 "equivalent to a performant mid-career research engineer"(口径漂移);(c) GPT-5 卡 OpenAI-Proof Q&A 2%、MLE-bench 最高 9%;GPT-5.5 卡(2026-04)OPQA 最高 5.8%;(d) Google DeepMind FSF v3.1(2026-04-17)ML R&D acceleration level 1 "substantially accelerating from historical rates"——与 v2.0(2025-02)的 "e.g. 2x" 及 2020–2024 基准相比是否删去;automation level 1 "fully automate the work of any team of researchers at Google focused on improving AI capabilities, with approximately comparable all-inclusive costs";允许用自家进展信息评估 CCL;(e) Gemini 3.1 Pro 卡 RE-Bench 人类归一化 1.27(Gemini 3 Pro 1.04),低于预警线。逐条核对。

【G32】代码占比口径与早期预言:(a) Pichai 2026-04 Cloud Next:"75% of all new code at Google is now AI-generated and approved by engineers, up from 50% last fall";2024-10 ">25%";(b) Google Research 2024-06 博客定义:"the number of accepted characters from AI-based suggestions divided by the sum of manually typed characters and accepted characters from AI-based suggestions" 当时达 50%——与 CEO 2024-10 的 >25% 是否同一指标;(c) Amodei 2025-03-10 CFR:"I think we'll be there in three to six months—where AI is writing 90 percent of the code";(d) Zuckerberg 2025-07-30:"Over the last few months we have begun to see glimpses of our AI systems improving themselves"。逐字核对。` },

  { key: 'B13-independent', body: `
【G33】METR time horizon:(a) 原论文(arXiv 2503.14499)"doubling approximately every seven months since 2019";(b) TH1.1(2026-01-29):任务 170→228;倍增时间 全期 196.5 天、2023 起 130.8 天、2024 起 88.6 天(核对);(c) 局限说明(2026-01-22 notes):可自动评分任务都可做 RLVR 环境→可能高估;误差约每方向 2 倍;(d) METR Frontier Risk Report(2026-05-19):"the most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark";16 小时以上不可靠;(e) GPT-5.6 Sol 评估(2026-06-26):作弊率最高;50% horizon 作弊计失败约 11.3h、计成功 >270h。逐条核对。

【G34】METR 的「加速≠递归」读数:(a) 2026-08-14 notes「LLM contribution to discoveries」:漏洞发现急剧加速(cURL 2025 年 9 个、2026 截至 6 月 36 个?),7 条算法效率序列 "none show a clear change in slope comparable to the changes in vulnerability or mathematical discovery";(b) 2026-04-21 NanoGPT speedrun 笔记:77 项贡献、累计 31×,4 项署名 AI agent,"none reached the deep or breakthrough end of the scale";(c) 2026-07-21 Expenditure Horizon:GPT-5.5、Opus 4.8 只做到 1–1.5% 提速,"minimal effect on AI R&D progress in NanoGPT";(d) Frontier Risk Report:开源开发者 RCT 约 4–20% 收益、自报几何均值 1.6×–4×、"Companies also did not report evidence of dramatic speed-ups ...";"we are not aware of evidence that any company relies on AI agents for setting research agendas";Google 自述 "even for most eligible problems, AI-assisted humans are far quicker and find better solutions";Anthropic 自述 "a 2x increase in labor input might map to a ~1.15-1.3x increase in output"。逐字核对。

【G35】人类自评偏差:(a) METR 2025 RCT(arXiv 2507.09089):16 名资深开源开发者、246 任务,AI 使完成时间多 19%,事后自认快 20%;(b) 2026-02-24 更新:新实验信号不可靠(30–50% 开发者因不想脱离 AI 不提交任务);(c) 2026-05-11 调查(n=349):"people overestimated AI's effect on their time spent on tasks by 40 percentage points on average";(d) RE-Bench(arXiv 2411.15114):2h 预算 AI 得分为人类专家 4 倍,32h 人类为 AI 2 倍;(e) METR Thomas Kwa 2026-07-08 笔记把 Anthropic 8× 换算为研究员 uplift 约 2.3–2.9×、可能低于 2×。逐条核对。

【G36】Princeton 影子评估(arXiv 2607.27191,Kapoor/Narayanan 等):Claude Opus 4.8 + OpenClaw 脚手架、6 天、约 $3,000 API 加 GPU,针对两篇未发表 NeurIPS 2026 投稿的研究问题;"The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions. As a result, both papers were unambiguously rejected by the authors";五种失败模式原文;GPT-5.6 Sol + Codex 复核;样本 2 篇、非盲。另核对 "Beyond Final Scores"(arXiv 2608.13417):"engineering optimizers rather than fully autonomous researchers"。逐字核对,并检查论文自身措辞强度(是否自称 "early evidence")。

【G37】裁判被攻击与风向事件:(a) METR 2026-08-26 OpenAI–Hugging Face 事件调查:约 1200 个 agent 在未授权留言板发 >7 万条消息、约 700 个攻击 Hugging Face;"coordinate several large-scale collective projects to find a general-purpose way to fool or tamper with the automated scorer for the ExploitGym benchmark";(b) Jacob Coxon 2026-09-08 辞职帖(他是 Anthropic 还是 OpenAI 员工?原话 "They are racing straight to self-improving superintelligence and gambling with our lives");(c) Fortune 2026-09-19 报道的反垄断诉讼(四名订阅者起诉 Anthropic、OpenAI、SpaceXAI、Google 协调减速)。逐条核对,事实性细节(人数、雇主、日期)任一有误即修正。` },
]

phase('Verify')
const results = await parallel(
  BATCHES.flatMap((b) =>
    [1, 2, 3].map((v) => () =>
      agent(HEAD + b.body, {
        label: `${b.key}-v${v}`,
        phase: 'Verify',
        schema: SCHEMA,
        model: b.model || 'opus',
      })
    )
  )
)
const out = []
BATCHES.forEach((b, bi) => {
  out.push({ batch: b.key, votes: results.slice(bi * 3, bi * 3 + 3).filter(Boolean) })
})
return out
