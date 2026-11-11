# FORMAL 线要点(T3/T4 形式化一端)— Round 1

> 34 条论断(F01–F34)。**降级说明**:本会话网络禁止访问 arxiv.org / openreview.net / 大多数论文站点,只能通过 GitHub 公开仓库(论文制品 README、博客源文件)拿一手原文;arXiv 独有的数字一律标 `secondhand`,或复用 #5 已核口径(注明 #5)。21 条 verbatim-checked(含 5 条复用 #5),4 条 paraphrase-checked,9 条 secondhand。

## 1. 形式基准的题面错位率:「证明⊢陈述」≠「陈述=意图」

- **ProofNet-Verified(Ground False,NeurIPS 2026 E&D)**【研究·verbatim】:原版 ProofNet 205/367(55.9%)有错,**已修正过一轮的 ProofNet# 仍有 99/367(27.0%)**。根因以「误解非形式数学」居首(95 题,25.9%);NL 原题本身有歧义或错误的只有 10 题(2.7%)→ 错位主要出在**翻译那一端**,不在意图本身。(F01–F02)
- **ProofNet#**:修了 118 条(31.8%,分母≈371)。(F03)
- **miniF2F-v2**(#5 已核):逾半题目形式陈述与非形式陈述不一致。(F04)
- **ReForm ConsistencyCheck**(#5 已核):人类专家写的形式陈述,miniF2F 16.4%、ProofNet 38.5% 有语义错误。(F06)
- **Faults in Our Formal Benchmarking**(ICML 2026):5 个基准共 4,833 条 findings,398/399 条机器可证。工具作者自己写明:"A theorem can be type-correct, compile cleanly, and still formalize the wrong mathematics entirely."(F07)
- **口径陷阱**:ProofNet 至少有 4 个错误率(31.8 / 38.5 / 55.9 / 27.0),分母、版本、判定方法都不同,**不能写成"ProofNet 错误率 X%"**。

## 2. 规约—意图鸿沟的可测性(最有新意的部分)

- **自动判官系统性高估忠实率**(miniF2F-v2 README Table 2,verbatim):Herald 翻译器在 v1 test 上自动判官给 97.5%,人工只有 62.7%;在竞赛原题版 v2c 上人工 54.1%,自动判官仍是 95.1%。Kimina 自动判官 98.4%,人工 90.6%。(F05)
- 同向证据:Verus-SpecGym 报告 LLM-as-judge 漏掉 26% 的可执行评测失败(secondhand,#5 也标为未验证)(F20);AutoCLRS 作者对 AI 审阅生成的目录写明 "take this table with a big grain of salt"(F15)。
- **人审也不是金标准**:Lahiri FMCAD 2024 的符号化测试找出 3 条误标和 2 条不一致规约,"all missed by human labeling"。例子是专家标为 strong 的 Dafny 规约,`==>` 应为 `<==>`,结果空列表就能平凡满足。(F13)
- **理论锚**(Lahiri 2026):"there is no oracle for specification correctness other than the user"。能测的只是相对测试集和变异体的 soundness/completeness **代理指标**。(F11)
- **Clover**:把正确性检查降为"代码/docstring/注解"三方一致性检查,在教科书级小数据集上做到 87% 接受、0 误报。(F24)

## 3. LLM 生成形式规约的正确性

- nl2postcond(FSE 2024):后置条件能区分 Defects4J 上 64 个真实 bug;Lahiri 转述为"约八分之一"。分母待核,Defects4J 评估源码未公开。(F09–F10)
- SpecGen(ICSE 2025):279/385 个程序得到"可验证"JML 规约(secondhand)。**"可验证"≠"忠实"**,ensures true 也能验证。(F19)
- NL→TLA+(#5 已核):语法 26.6%、语义 8.6%。**口径冲突**:#5 核的是"25 个开源模型聚合",本线搜索摘要写成"最佳",R2 须回原文。(F21)
- VerifyThisBench:代码、规约、证明一起生成,o3-mini 零样本 3.62%(secondhand,旧代模型)。(F27)
- **优化压力下规约被黑**:AlphaVerus 中模型用 `assume(false)` 让任意实现通过验证(#5 已核);ExVerus 报告某数据集里有同义反复的前/后置条件(secondhand)。(F22)
- Rust std 验证(AWS,厂商口径,#5 已核):LLM 合约 "require manual review before merging"。(F23)

## 4. 审规约 vs 审代码的成本(证据最薄)

- **最直接的一手量化**(AutoCLRS,Microsoft Research,verbatim):约 10 万行代码+证明,待审规约约 5,000 行,约 1/20。作者称规约审阅是"Key Challenge",规约质量"highly variable"。**这是行数比,不是工时比;单人案例;前提是证明由机器检查。**(F14)
- **机器证明通过的规约仍有缺口**:agent 写 SPOT 小测试后,52 个算法中 8 个有实质缺口(Prim 后置条件接受错误输出、哈希表 insert 允许永远返回 false),约 15%,且是下界。完整性测试是另一口径:5/48 不完整。(F16、F18)
- **审抽象规约本身也难**:SPOT 作者认为小而具体的测试"easier to review than large, abstract specifications",也就是**T3 的审阅要退回 T4 例子做代理**。(F17)
- 反向/中性证据(都是 secondhand):OOPSLA 2025 访谈 14 名 Dafny 用户,称验证"增加评审负担",规约成了**额外**的审阅面(F30);Snook & Harrison 2004 发现 Z 规约与 Java 实现的可理解性差异很小(F31);Matichuk ICSE 2015 发现规约规模与证明规模呈二次关系(F29)。
- **空白**:没找到 2024–26 年直接比较"审形式规约 vs 审代码"工时或准确率的受控实验。"spec 审阅更便宜"目前**没有实验支持**,只有行数比和定性判断。

## 5. 从 spec 生成可执行规约(T4 / PBT)

- Agentic PBT(Maaz/DeVoe/Hatfield-Dodds/Carlini):100 个包(15+15 个硬编码,70 个随机),人工复核样本 56% 为真 bug、32% 值得报告(secondhand);NumPy wald 的 bug 已修(verbatim)。**利益相关**:作者含 Anthropic 员工,被测 agent 是 Claude,评分由 Claude Opus 4.1 自动打。(F25)
- Vikram 等:以 API 文档为 spec 生成 PBT,79% 的断言 sound,21% 编码了错误意图(secondhand,GPT-3.5/4 时代)。(F26)

## 6. 历史 / 非 LLM 对照

- Fonseca EuroSys 2017:3 个已验证分布式系统中有 16 个 bug,已验证协议零 bug,bug 都在 shim 层和规约对环境的假设上(secondhand)。形式化**移动**了缺陷位置,并没有消除它。(F28)

## 最强 3 条
1. **F01/F02 ProofNet-Verified**:逐题以证明否命题或平凡化证明确认,仓库逐字核到,分母清楚,根因分类可复查。
2. **F05 miniF2F-v2 自动判官 vs 人工**:同一批翻译,自动判官 95–98%,人工 54–91%,README 表格逐字核到,直接证明"陈述=意图"难以自动测量。
3. **F16 AutoCLRS SPOT 8/52**:在真实 agent 工作流里,机器证明通过的规约仍有约 15% 存在实质缺口,而且是下界(作者自述,一手博客)。

## 最弱 3 条
1. **F33 Aleph 修复 PutnamBench 15 题**:厂商自述,无分母,且没有对 PutnamBench 的独立审计。
2. **F32 Kleppmann 预测**:预测类观点,原文不可达,不能加引号。
3. **F31 Snook & Harrison 2004 / F30 OOPSLA 访谈**:都只来自搜索片段,老实验或小样本定性研究。

## 交给 R2 的要点
- 回原文确认三处:#5 的 miniF2F "40%→70%" 对应哪种评分设定(README 表中 Full-score 设定下修正后反而更低);NL→TLA+ 的 26.6% 是聚合还是最佳;ProofNet-Verified 是 204 还是 205。
- "可验证率"(SpecGen/Clover/Goedel)与"忠实率"(ProofNet/miniF2F)不得混引。
- T3 的"审规约更便宜"不得外推到 T1/T2 自然语言 spec。Lahiri 本人也写明 Spec Kit 的规约 "informal and uncheckable"(F12)。
- 网络放开 arxiv.org 后,优先补核 F08、F19、F20、F26、F27(全是 arXiv 独有数字)。
