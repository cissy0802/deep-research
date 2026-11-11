# R3 · R6-M 方法学审计席(有否决权)

靶子:形式基准题面错位率这组承重数字(G25;F01–F07)。具体是 ProofNet-Verified 的 205(含 195)/367 与 ProofNet# 99/367、根因分布(F02)、miniF2F-v2「逾半错位」与 40→70(F04)、miniF2F-v2 Table 2 自动判官 97.5% vs 人工 62.7%(F05)、Faults 398/399(F07)。

今天复核了:
- ProofNet-Verified 仓库完整 git 历史(github.com/marcusm117/ProofNet-Verified,HEAD b7ca411,2026-11-07;9 个 commit,首个 fad8a96 是 2026-07-24)。读了 `error_taxonomy/{proofnet,proofnet#}/results.jsonl` 与 `summary.md`(367+367 条逐题标签)、首个 commit 里的 per_file 标签(用来比对版本漂移)、`data/proofnet/proofnet_lean4-6deae98.jsonl` 与 `proofnet-4.28.jsonl`(被审对象的来源)、`data/archive/proofnet-verified_gt-4.28.zip`(367 个证明文件)。
- ICML 2026 poster 82611 摘要(icml.cc,可取);NeurIPS 2026 poster 139101 摘要(neurips.cc/virtual/2026/loc/sydney/poster/139101,可取)。
- miniF2F_v2 仓库 README(HEAD 905eca8)与 arXiv 2511.03108v1 全文 PDF(19 页;§3–4、Table 2/3、附录 H)。
- Faults arXiv 2606.29493 全文 PDF(Table 4、§4.1、Table 10)。

没拿到:
- OpenReview 上 Ground False 的 PDF(l0dHSybfie / 5c0RSYyIWW;api2.openreview.net 返回 403 challenge)。所以论文正文里的标注协议(几人标注、LLM 判官的型号与提示、人机分歧怎么裁决、有没有一致性系数)拿不到。
- 本机没有 Lean/elan,106 个否命题证明**没有编译验证**,只核了它们在文件里存在、结构完整。
- `proofnet_lean4-6deae98` 对应哪个上游仓库、哪个 commit(github.com 的 commit 页被代理 403)。
- miniF2F-v2 人工评审的人数与一致性(论文里只写了 "Lean experts")。

## 一、发现

**M1 · ProofNet 计数可以从逐题数据精确复算(正面)。**
`error_taxonomy/proofnet/results.jsonl` 共 367 条。q2_faithfulness 的分布:faithful 162、stronger 75、weaker 54、incomparable 66、nl_ambiguous 9、nl_wrong 1。所以不忠实 = 75+54+66 = 195,另有 NL 源问题 10,合计 205,和 README 一致。ProofNet# 是 faithful 268 / 不忠实 39+19+32 = 90 / NL 源 9,合计 99,也一致。q4 根因计数与 README Root Cause 表逐项一致。

**M2 · 「可证伪」这个硬核子集有机器证书(正面,最强的一块)。**
ProofNet 里 q3_provability=false 的有 106 条:不忠实且为假 104 条(incomparable 48 + stronger 56),NL 源 2 条。我用正则 `theorem \S*_neg : ¬ (type_of% @…)` 扫了 `proofnet-verified_gt-4.28.zip` 的 367 个文件:**106/106 个 false 标签都有对应的否命题定理**,没有一个 false 标签缺证书,也没有证书落在非 false 条目上。每个文件里剩下的 `sorry` 只出现在被驳倒的那条原陈述上(107 个文件,其中 106 个是 false,另 1 个是 independent 的 #150)。104 个不忠实且为假的条目里,只有 1 个的否命题证明用了 `native_decide`(会绕过内核检查)。
- 限定:我没有编译这些证明。
- 104/367 = 28.3%,Wilson 95% CI [24.0, 33.2]。这个数和 ICML 摘要的 "104 (28%) are mathematically false" 精确吻合。
- ProofNet# 中不忠实且为假的有 59 条(16.1%,CI [12.7, 20.2]),其中 57 条在 ProofNet 中同样为假。

**M3 · 「不忠实但不假」这一块(约 91–100 条)属于判断性标注,协议没有公开。**
NeurIPS 和 ICML 两份摘要都写,修正版基准是 "produced by a semi-automated pipeline combining Lean provability checks, an LLM faithfulness judge, and human review"。README 第 5 条说的是对**修正版**做 "human reviewers and an AI agent until they reach a consensus"。README 和仓库都没有给标注人数、Cohen κ 之类的一致性系数,也没给 LLM 判官的单独精度。
- 逐题 reasoning 是 Q1–Q4 固定模板,ProofNet 不忠实条目的说明中位长度 946 字符。这与「代理先写、人工复核」的做法相符,但不能证明就是这么做的。
- 值得注意的是:文章拿来论证「LLM 判官不可靠」的工具,本身也用在了这份审计里。不过,假阳性要先过人工复核,假阴性只会让计数偏低,所以 205 更像一个下界式的计数,而不是夸大。

**M4 · 「错误」是相对审计者自己的修正版来定义的(循环依赖)。**
两份 summary.md 都写 "Compared against golden ground truth `proofnet_verified/`"。ProofNet# 的 268 个 faithful 里,有 266 个的 reasoning 只有一句 "ProofNet# formalization matches the corrected ground truth."。ProofNet 的 faithful 里,有 98 个是 "Original and corrected formalizations are identical"。
- 所以 99/367 的严格含义是:「PNV 团队改动了、并且判为不等价的 ProofNet# 条目数」。
- Poiroux 团队(ProofNet# 作者)和 PNV 团队在约 90 条上判断不同。这本身说明「忠实性」的人类专家判定在团队之间分歧不小,这一点对 PNV 自己的非证伪类标签同样适用。

**M5 · 版本漂移:README 数字和根因标签三个月内变过。**
- 首个 commit fad8a96(2026-07-24)的 README 写的是:"**204/367 (55.6%)** errors in ProofNet and **97/367 (26.4%)** errors in ProofNet#",其中 Unfaithful 194 / ProofNet# 88。
- 9c40e80(2026-10-25,commit message "fix unfaithful 311 …")之后改成 205 / 99。
- 我对比了两版的逐题标签:
  - 错/非错的翻转:ProofNet 只有 1 条(#311,faithful→weaker),ProofNet# 2 条(#205、#311)。总量很稳。
  - **根因标签不稳**:在两版都判为错误的条目里,ProofNet 有 14/204(6.9%)换了根因,ProofNet# 有 16/97(16.5%)换了根因。
  - 「adding_extra_case」这一类(9 条)被整类撤销;Misunderstanding of Lean 从 10 变成 16;ProofNet# 的 Misunderstanding of Mathlib 从 31 变成 24,Missing premise 从 3 变成 6。
- 结论:根因百分比(F02 里的 25.9%、8.4% 等)是最主观、最不稳的一个维度,不能精确承重。
- 第 2 轮 X 票把会议摘要的 204 称为「定版」,这个说法是错的。仓库首版的 204 = 194+9+1。按现行数据,ICML 的拆分「104 假 + 100 不假但不忠实 = 204」只有一种对得上的方式:把 9 条 NL 歧义算作不忠实、把 1 条 NL 错误排除(104 + 91 + 9 = 204)。这是我的重构,没有论文正文可以确认。两个「204」可能出自不同的口径组合。

**M6 · 被审对象不是 Azerbayev 的 Lean 3 原版。**
README 写的是「ProofNet」那一列,实际审的是 `data/proofnet/proofnet-4.28`。我拿它和 `proofnet_lean4-6deae98.jsonl`(某个公开 Lean 4 移植版,toolchain v4.20.0)比对:规范化之后 **356/367 条陈述逐字相同**,只有 11 条有差异,其中 3 条被判错。所以 PNV 升级到 4.28 时自己引入的错误可以忽略。但这个数字衡量的是「一个公开 Lean 4 移植版」,不是 Lean 3 原版。Root Cause 里的 Lean/Mathlib 误用(44 条)里可能有一部分是移植错误。Faults 把 ProofNet 版本漂移列为一种缺陷类型(其 Figure 4),也说明「ProofNet 原版」这个说法本身有歧义。

**M7 · 抽样误差不是主要风险。**
ProofNet 是全集普查,367/367,不是抽样,所以 CI 只反映「同一过程重来一遍」的不确定性:205/367 的 CI 是 [50.7, 60.9],99/367 是 [22.7, 31.7]。真正的风险在 M3–M5 说的测量效度,也就是标签由谁、按什么标准判定。

**M8 · miniF2F-v2 Table 2 的「LLM 判官系统性高估」被同一论文自己推翻。**
- arXiv 2511.03108 正文 Table 3(@1 设定)里,LLM 判 vs 人工判:
  - Herald v1 test 49.6% vs 55.3%
  - **Kimina v1 test 58.6% vs 88.1%**
  - Kimina v2s test 54.5% vs 79.5%
  - Herald v2s valid 50.4% vs 48.0%
- 正文原话:"Here, the opposite pattern appears: the LLM evaluator assigns lower accuracies than the human evaluator."
- 也就是说,@1 时 LLM 判官**低估**,最多 29.5pp;@128 时**高估** 7.8–41.0pp。方向随采样预算翻转,所以「系统性高估」不成立。能成立的写法是「LLM 判官与专家判定偏差大、方向不稳定」。
- @128 的对比对象也不对等。正文原话:"For the @128 setting, human evaluation is performed only on the first translation that successfully passes the Lean compiler, rather than on all 128 translations"。而 LLM 列的口径(是 128 条里有任意一条通过,还是只看同一条)正文没写清楚;§4 开头又写 "human review of the outputs of Herald @128 that LLM has marked as 97% correct"。两种读法下,97.5% 和 62.7% 的含义不同(一种是两套标准各自的通过率,另一种近似「判官精度约 64%」)。
- 判官也被作者换过:正文 "we used Deepseek-V3 … instead of Deepseek-V2.5",所以它不是 Herald 原论文发表时的那个判官。
- 人工评审人数与一致性未报告;作者之一来自 Huawei Hong Kong Research Center,数据集「funded by the company where the authors work」(数据卡,第 910 行)。
- 论文内部小不一致:§4 说人工复核后是 "66%",和 Table 2 任何一格都不相等(v1 两列均值约 66.2%);正文说 Kimina "78% to 88%",和 Table 2 的人工 75.4–91.0% 也对不上。
- 分母复算:62.7% = 153/244,97.5% = 238/244,54.1% = 132/244,和 244 题的 test split 一致。62.7% 的 CI 是 [56.5, 68.5]。

**M9 · miniF2F「逾半错位」把「简化」和「错误」混在一起。**
- 摘要原话:"discrepancies between the formal and informal statements for more than half of the problems"。
- 附录 H(第 2357–2360 行)原话:"the majority of the problems … are simplified and do not reflect the intended difficulty … approximately 40% of formal statements across both sets contained an error"。
- miniF2F 原设计就把答案写进形式陈述,「简化」大部分来自这一点,不是错误。所以「逾半」≠「逾半有错」;错误口径约 40%,而且是从图 4 读出来的近似值,没有精确计数。
- 「40%→70%」只在 Olympiad 设定下成立;在 Full score 设定下修正版反而更低(Kimina+Goedel-V2 test:77.5 → 74.2)。第 2 轮 K 票已经指出这一点,我复核成立。

**M10 · Faults 的 398/399 是信号计数,不是错题数;和 PNV 的 104 不能相除。**
- Table 4 的 Total 行是 "10,318 4,833 398 … 199(Axiom)";正文写的是 "4,833 findings and 399"。398 和 399 是论文内部不一致。
- Proven 列里 ProverBench 占 208,其中 Axiom 199 条,也就是说 398 条里有一半是同一个基准的公理问题。
- 表注原话:"forks, ports, and splits are counted separately and not deduplicated"。
- §4.1:静态告警的真阳性率只有 42/55 = 76%(作者自己标注的 55 例,Table 10)。
- 静态检查在 ProofNet 上只给出了 5 个 Proven(deepseek 移植版,371 题),PNV 在另一个移植版上证伪了 104 个。两者版本不同、证书类别不同,**不能**写成「静态检查只抓到 5%」。只能说静态检查只覆盖少数机械类别,远少于语义审计的发现。

**M11 · 利益冲突(标准学术型,不构成否决)。**
PNV、miniF2F-v2、Faults 的作者都在发布修正版基准或检查工具,都有动机把前作的错误率报得高一些。PNV 还同时推广自己的 autoformalization 方法(Divide and Abstract,ICLR 2026),而摘要里说等价性指标「penalize faithful models more」,这条结论对他们的方法有利。但 PNV 的硬核数字由否命题证明支撑,可以独立复查,这削弱了上述动机对硬核数字的影响。

## 二、结局

**评级:B**(核心可承重,但必须换成硬核口径并带版本;几条衍生表述否决)。分项:
- PNV 的「可证伪」计数:B+
- PNV 的总错误数:B−
- 根因分布:D
- miniF2F Table 2 的数字:B;它推出的「系统性高估」结论:D
- Faults 计数:B;把它当错误率用:D

**否决清单(不得承重):**
- **V1** 「LLM 判官对『陈述=意图』系统性高估 8–41pp」以及任何「LLM 判官高估」的单向表述(F05)。同一论文 @1 设定下方向相反(Kimina v1 test LLM 58.6% vs 人工 88.1%);@128 的对比对象不对等;判官被作者改过(DeepSeek-V3);人工评审人数/一致性未报告。拿它与 Verus-SpecGym 26% 漏判并称「同向」的说法也一并否决。
- **V2** F02 的根因百分比精确值(25.9%、8.4%、7.6%、4.9%、4.4%、1.9%)。三个月内 14/204 条换过根因,一个类别被整类撤销,也没有一致性数据。只保留「195 vs 10:错几乎全在翻译端,题面本身有问题的只有约 10 题」。这个比例跨版本稳定(194/10 → 195/10)。
- **V3** 不带版本的「ProofNet 错误率 55.9%」或「定版 204」。必须写「仓库 2026-10 版 205/367;2026-07 首版与会议摘要为 204」。ProofNet# 同理(97 → 99)。
- **V4** 「ProofNet 原版」或「Lean 3 原版」有 X% 错。被审对象是一个公开 Lean 4 移植版。
- **V5** 「miniF2F 逾半题目有错」。「逾半」含简化;错误口径约 40%,而且是图上的读数。
- **V6** 「398 道题有错」、任何由 398/4,833 算出的错误率,以及「静态检查只抓到 5%」。
- **V7** 「40%→70%」不带 Olympiad/no-score 设定限定。

**可承重的最强写法:**
> 在 ProofNet 的一个公开 Lean 4 移植版(367 道证明题)上,An、Min 等逐题审计,发现 104 道(28%)的「标准答案」形式陈述其实是**假命题**:他们为每一道都写了 Lean 否命题证明,放在仓库里可以复查。另有约 90–100 道虽然不假但与题意不符,合计约 56%(204–205 道,随版本)。就连已经修过一轮的 ProofNet#,仍有 59 道(16%)可被证伪、99 道(27%)被判有问题。错误几乎全出在把数学意思翻译成 Lean 的那一步,题面本身有问题的只有约 10 道。Poiroux 等(118/371,31.8%)和 ReForm(38.5%)用不同的版本和判定标准,得出了同方向的结论。在 miniF2F 上,LLM 自动判官与 Lean 专家的判定相差可达数十个百分点,而且偏差方向随采样设定翻转(@128 高估、@1 低估)。也就是说,自动忠实性判官目前不能代替人工。

**证据分级建议:**
- 「ProofNet 类形式基准有约四分之一到一半的形式陈述与题意不符」:**多源证实**(PNV / Poiroux / ReForm 三个团队,方向一致,数值不可并列)。
- 104/367 可证伪、ProofNet# 59/367 可证伪:**单源已核**(逐题数据复算吻合、证书存在;本席未编译)。
- 205/367、99/367 总错误:**单源已核(带版本,仓库 README 2026-10 口径)**,非证伪部分的标注协议未公开。
- 根因分布:**未验证**(只作定性描述:翻译端远多于题面端)。
- miniF2F Table 2 的各格数字:**单源已核**;「LLM 判官高估」:**方向存争**(同源内部翻转)。
- miniF2F「逾半不一致 / 约 40% 有错」:**单源已核**(带口径)。
- Faults 4,833 / 398:**单源已核(信号计数,不是错误率)**。

复算脚本要点(scratchpad,未入库):
- 用 `json` 读两版 results.jsonl 与首个 commit 的 per_file 标签,对 (q1, q2, q3) 做交叉计数和逐题 diff。
- 用正则扫 gt zip 里的 `_neg : ¬ (type_of% …)` 和 `sorry`,与 false 标签做集合比对。
- 规范化(去空白、定理名、`:= by sorry`)后比对移植版与 4.28 版陈述。
- Wilson 95% 区间。
