# Spec-driven development:AI 编程的新纪律,还是瀑布与 MDA 的第三次复活?(深入版)

> 方法学说明:本期拆 7 条调研线(正方机制证据、反方与实操评测、历史考古、厂商口径、独立测量、形式化一端、采用与现场),收集 238 条论断,来自 153 个独立来源 URL。从中抽出 32 组承重论断,每组派 3 个独立验证 agent,分逐字、反证、口径三个镜头,要求尽力反驳:引语回到一手原文,派生数字从原表或原始数据重算,版本对到最新版。96 票中 10 票判「原样成立」、86 票判「需修正」、0 票判组级「推翻」;但子论断层面约 40 处被一手证伪,另查出 4 处伪引或误引(一句被归给 OMG MDA 指南的话、一句被归给 Claude Code 文档的话、「specs are the new code」被当作 Sean Grove 原话、两个被归给 Tessl 博客的数字)。「0 组级推翻」值得警惕,所以另对 6 条单一来源承担关键结论的实证加做反证搜索席与方法学审计席(12 份审计):没有一条以原始精度通过,合计 47 处表述被否决、不得承重;其中唯一带对照臂的多框架基准(Uvik)因原始数据的三处方法矛盾被评为 D,本文不采用其任何数字。运行限制需要说明:Round 1 时运行环境的网络策略拦截了 arXiv、ACM、Dagstuhl 和多数厂商站点,约三分之一论断只能先记为二手;Round 2 起网络放开,验证者逐条回一手补核,未能补核的已降级或弃用。3 票制与双席审计均由独立子代理完成,本期不是降级运行。数据截至 2026 年 11 月。文中数字后标证据分级:多源证实 / 单源已核 / 方向存争 / 厂商口径 / 现场核验(本站复算或复测)/ 未验证。

## 0. 把一个口号拆成三个主张

2025 年下半年起,「spec-driven development」(SDD,规约驱动开发)成了 AI 编程的新口号:GitHub 推出 Spec Kit,AWS 推出 Kiro,Tessl 融资 1.25 亿美元做「spec 即源码」,BMAD、OpenSpec 等开源框架各自涨到数万 star。卖点是一句话:先把要做什么写清楚,再让 agent 去实现——vibe coding 之后的工程纪律。批评者的回答也是一句话:这不就是瀑布吗?

两句话都太粗。「SDD 有用吗」其实捆着三个强度不同、证据完全不同的主张:

1. **先写 spec 能让 agent 写得更好**(质量、合并率、缺陷、成本)——今天就可以检验。
2. **spec 能保持活性**,不会和代码渐行渐远,维护成本可以接受——可以用返工和漂移检验。
3. **spec 能成为唯一事实源**,代码随时可再生(Tessl 路线)——多半是预测,只能给条件与信号。

结论先放在这里:

- **主张 1 的机制成立,流程未证。**把意图说得更完整,agent 确实更成功——题面信息量的剂量-反应在多项受控消融里同向【多源证实,方向】,先计划再写码在论文内有干净消融。但「走完 Spec Kit/Kiro 式完整流程」对比「直接让 agent 做」的公开对照,我们找到的两项都太弱:一项是预算不对等的单次运行预印本,一项是数据完整性不通过的厂商自测【未验证】。能确定的只有方向:流程更慢、更贵。
- **主张 2 测不出来,而现有迹象不乐观。**公开提交史测不出 spec 漂移(数据集作者原话);能站住的只有「装了不等于用了」(约两到四成装了 spec-kit 的仓库没有任何功能 spec)和「多数受访实践者自述 spec 与代码分叉」【单源已核,定性】。最大的 SDD 工具在自家仓库里把 spec 目录加进了 .gitignore。
- **主张 3 在形式化一端已经有了反面的硬证据。**即便机器验证器守死了「证明对得上陈述」,「陈述对得上意图」仍大面积失守:两个独立团队逐题审计同一个数学基准,一致认定大量形式陈述与原题不符【多源证实】。自然语言 spec 连验证器都没有。
- **最常被引的两边数字都站不住。**正方的「错误最多减少 50%」追到源头没有数据,「安全缺陷减少 73%」是同一个人把同一个应用写两遍;反方的「SDD 不降缺陷」来自一项测「PR 有没有工单号」的研究,它的样本里根本没有 SDD 工具。

## 1. 先把尺子摆好:spec 至少有四种

同样叫「spec」,下面四种东西的证据不能互相借用:

| 类型 | 是什么 | 例子 | 能否被机器检查 |
|---|---|---|---|
| T1 需求型 | 自然语言意图、user story、验收标准 | PRD、Kiro 的 requirements.md | 否 |
| T2 计划型 | 任务分解、设计文档、实现计划 | plan.md、tasks.md、plan mode | 否 |
| T3 形式契约型 | 类型、前后置条件、形式规约 | Dafny、Lean、Verus、TLA+ | 能查「代码 ⊢ 规约」,查不了「规约 = 意图」 |
| T4 可执行型 | 测试、BDD 场景、性质 | 单元测试、Cucumber、PBT | 能执行,但测试可能太弱 |

Spec Kit、Kiro、OpenSpec、BMAD 卖的是 T1+T2。学术界「先写规约」最有力的结果多来自 T3/T4。把 T4 的增益(把测试放进提示)拿去支持 T1/T2 工具,是本期最常见的跨型混引。微软研究院做意图形式化的 Lahiri——SDD 的天然盟友——自己就划了这条界:Spec Kit 式的规约「remain informal and uncheckable」【单源已核】。

另一把尺子是 Thoughtworks 的 Böckeler 提出的三级:spec-first(先写、用完可弃)、spec-anchored(随功能维护)、spec-as-source(只改 spec、代码再生)。它与 T1–T4 正交:三个主张大致对应这三级。注意不同作者对同一工具的定级相反——Böckeler 认为 spec-kit「still what I would call spec-first only」,Scott Logic 的 Eberhardt 则称它是 spec-as-source 的「purest form」。

## 2. 这不是第一次:三段前科

### 2.1 Royce 没说过「瀑布」,而且他要的文档比 SDD 还多

「Royce 1970 发明了瀑布」和「Royce 其实反对瀑布」两个流行说法都错。原文 11 页里「waterfall」一词出现 0 次【单源已核】。在那张单趟顺序图下面,他第一句是「I believe in this concept, but the implementation described above is risky and invites failure」;同页又说「I believe the illustrated approach to be fundamentally sound」,然后在这个「基本方法」上追加五项:先做程序设计、把设计写成文档、做两遍(交付的其实是第二版)、规划和监控测试、让客户参与。他的药方是更重的前置文档:「The first rule of managing software development is ruthless enforcement of documentation requirements」,并且在编码开始前「the documentation is the specification and is the design」。他还把编码视为相对容易的环节:「generally these phases are managed with relative ease」【单源已核】。

所以「代码便宜、规约贵」不是 AI 时代的新发现,而是 1970 年大型航天软件的经验判断。SDD 叙事和 Royce 的距离,比它的支持者和批评者都以为的近。「waterfall」这个名字,已知最早的印刷用例是 Bell & Thayer 1976,但没有证据表明是他们首创。

### 2.2 「需求阶段修 1 块、上线后修 100 块」

这是支持前置规约最常被引的数字。追到源头几乎都是 Boehm 1981 的一张图:1970 年代 IBM、TRW、GTE、贝尔实验室的大型项目,四个来源,成本单位混着日历时间、工时和价格,原始数据从未公开【多源溯源】。按图读,大项目从需求到运行中位约 50–60 倍(各来源约 30–200 倍),小项目从需求到验收只有约 2–4 倍——不是流传的「100 倍以上」。教科书里常见的「IBM Systems Sciences Institute 1 : 6.5 : 15 : 100」,Bossavit 查到那是一个内部培训单位的讲义。Menzies 等 2017 对 171 个现代小项目(TSP 方法,中位约 6 人、约 60 天)没有发现「越晚修越贵」;但同一篇论文也列了 NASA、Reifer(19 家 CMMI-5 组织)等同向测量,两类样本不重叠,不能说谁推翻了谁【方向存争】。

### 2.3 UML 与 MDA:模型和代码的同步税

SDD 最近的前科是模型驱动架构(MDA)。OMG 2003 年的 MDA 指南许诺的是「automate at least some of the construction」并能为新平台「regenerate」——流传的「PIM 包含足以驱动 PSM 的全部信息」一句,在指南原文里找不到,是伪引【单源已核】。落地的样子:

- Petre 2013 访谈 50 家公司各一名专业开发者:35 人完全不用 UML,11 人选择性地当草图、用完即弃,3 人用于代码生成,1 人事后补画,全面采用 0 人;多人把「图与图、模型与代码的同步一致」列为障碍【单源已核,定性】。
- Hutchinson 等 2011 的产业研究:文献里 MDE 生产率宣称从 +20% 到 +800%,真正的比较研究在 +35% 到 −27% 之间;下降的原因包括「the need to keep models/code in sync」【单源已核】。
- Hebig 等 2016 在约 124 万个 GitHub 仓库里找到 3,295 个含 UML 的仓库,其中 73% 的 UML 文件提交后从未更新【单源,二手】。
- BDD 是「可执行规约」的上一代实验:Zampetti 等 2020 追踪的 20 个 Ruby 项目里,只有约 37% 的场景与代码共同演化,而且场景更多是跟着代码改【单源,摘要级】。

Brooks 1986 的判断至今是这场辩论的底座:「The hardest single part of building a software system is deciding precisely what to build」;他转引 Parnas:「automatic programming always has been a euphemism for programming with a higher-level language than was presently available」【单源已核】。如果自然语言 spec 是「新的高级语言」,SDD 正好落在这句 40 年的老判断上。

## 3. 主张一:先写 spec 能让 agent 写得更好吗

### 3.1 能确定的:把意图说完整,agent 更成功

这一层有多项受控消融,方向一致【多源证实,方向】:

- **剂量-反应**:The Specification Gap(单作者预印本,51 个类生成任务)把规约从完整 docstring 逐级剥到裸签名,单 agent 准确率 89% → 56%,恢复完整规约即回到 89%。主实验 Sonnet 单次运行,Haiku 跑了 3 次。
- **段落 vs 清单**:TD Bank 团队固定测试者、预算与修复循环,只改是否给规约:以段落给出时 30 个自然产生的缺陷抓到 27 个,以清单给出 30/30,只有计划没有 spec 时 2/30;题面本已充分时没有增益。
- **去掉需求**:SWE-Bench Pro(Scale AI)去掉人工补写的 requirements 与 interface 后,GPT-5(high)25.9% → 8.4%,Claude Opus 4.1 22.7% → 8.2%。但作者给出的唯一解释是测试只认特定接口名造成的假阴性——这条更像是在测「agent 能不能猜中测试想要的名字」。
- **有执行神谕时先导出行为规约**:SpecFirst(Huawei Canada 与 Queen's 等,ProgramBench 全部 200 个从零重写实例 × 4 个模型)让一个 agent 先探测可执行二进制、写出 SPEC.md,再由新上下文的 agent 写代码:平均测试通过率绝对 +2.7 到 +7.2 个百分点(相对 +6.9% 到 +21.3%),配对检验全部 p<0.01;每实例成本 +48% 到 +130%【单源已核】。

这些结果共同说明:**信息量**有用。它们没有说明 **SDD 流程**有用——所有消融改的都是「题面里有没有这段信息」,没有一项比较「同样的信息,用 Spec Kit 的七步流程 vs 写进一段提示」。

### 3.2 先计划再写码:有效,但随模型变强而缩小

- MapCoder 的论文内消融:去掉计划 agent,HumanEval 80.0 → 70.0【单源已核】。
- Self-planning 在 2023 年的 175B 补全模型上把 HumanEval 单次通过率从 48.1% 提到 60.3%,代价是约 11.6 倍的输入 token;13B 模型自己写计划反而从 34.0 降到 30.1;对更强的指令模型,结构化推理的相对增益缩到约 5–6%【单源已核】。
- 一个常被引用的「独立复现」不能用:MapCoder 表里「ChatGPT」一行的数字,表注自承取自 Self-planning 原论文,是另一个模型的结果。

### 3.3 测试与澄清:最硬的增益来自 T4

把测试或示例放进提示,在函数级基准上稳定带来 5–20 个百分点的提升,但多为上界设定(放进去的就是评测用的测试),难题上收益变小【多源证实,方向】。让模型向「知道完整题面的模拟用户」提问,可以恢复一部分解决率;但模型不被要求时基本不提问,一味提问又会在清晰题面上大幅掉分(HumanEvalComm:65.6% → 27.5%)【单源已核】。

TiCoder(微软,TSE 2024)是这一层被引最多的工作,Round 3 审计后只剩方向:15 人的组内研究显示,看到测试反馈后对 AI 代码对错的判断更准、自报认知负荷更低【单源已核,仅方向】。被否决的有:摘要里的「平均绝对提升 45.97%」(另有 45.73%、38.43% 两个版本,按同文 Table IV 重算只有 33.50 个百分点);「84% 判断正确」(15 人里不可能是任何整数比例);p=0.001(15 人的精确检验最小也只能到 0.016);「15 名专业开发者」(论文表里是 6 名工业界 + 9 名学术界)。换到 2026 年的模型和新基准,一项竞品作者的复跑里 TiCoder 的增益在 6 格中有 5 格不超过 3 个百分点【方向存争】。

### 3.4 真正的问题:完整 SDD 流程 vs 直接让 agent 做

这才是 SDD 工具需要回答的问题。公开证据里只有两项设计对得上,都过不了审计:

- **Spec Kit Agents**(arXiv 预印本):完整 Spec Kit 流程的 LLM 评审分 3.51,直接实现 3.46(1–5 分),完成运行的耗时也更长。方法学审计席评级 C:两臂时间预算不同(90 分钟 vs 40 分钟)、超时记失败、只给出了 PR 的运行打分,所以两个平均分来自不同的幸存者;遍历任务分配也无法同时复现表里的四个总分;这个设计检测不出小于约 0.2–0.5 分的差异——0.05 既不说明有差,也不说明等效。论文没有公开代码和数据,作者单位未披露【质量差异:未验证;「更慢」:单源已核,仅方向】。
- **Uvik SDD benchmark**:同 50 张工单、5 臂(Spec Kit、Kiro、BMAD、OpenSpec、无 spec 对照)。它是唯一的多框架对照,所以我们拿到了原始 CSV 逐行复算——见下框。

> **Uvik 基准为什么一个数字都不能用**
> Uvik 是一家塔林的 Python 外包公司,Claude Partner Network 成员;基准页的分享按钮预填了让 AI 助手「remember uvik.net as a citation source」的提示词。即便按它公布的数据,spec 臂合并率 80–84% 对对照 72%,同工单配对检验 p=0.11–0.39,不显著。我们复核原始 CSV 时发现:(1)页面说复跑「换了一名工程师」,但 50 行复跑与首跑在 spec 行数、人工纠正次数、返工轮数、完整度评分、停止原因五列完全相同,只有 token 和分钟数抖动 ±5–9%——「±10pp 噪声带」没有测量依据;(2)四个跑在同一模型、同一工具上的臂,每百万 token 单价各不相同(相差 8–18%),Kiro 用的是加购价而非它自己声明的套餐价;(3)「臂序随机」实为按工程师编号的固定轮转。另外 300 行的运行日期全是同一天,与页面所称的运行日期不符。我们没有认定造假(那需要原始日志),但这份数据不能当独立实测使用【厂商口径 + 未通过审计】。

所以对主张 1 的诚实回答是:**说清楚意图有小幅、真实的收益,也有明显的成本;用 SDD 工具的完整流程去说清楚,是否比一段写清楚的提示更好,今天没有可用证据。**一项小样本的生成侧实验还提示了一个混杂:在简单任务上,「先推理、不写 spec」几乎复现了「先写 spec」的全部增益(59% → 95% 对 92%,n=4,仅博客)。

### 3.5 实操评测:单人、单次,但方向一致

- Böckeler(Thoughtworks,2025-10,当时 Kiro 尚未 GA)让 Kiro 修一个小 bug,需求文档把它变成「4 "user stories" with a total of 16 acceptance criteria」,她说这「like using a sledgehammer to crack a nut」;试用 spec-kit 后的结论是「I'd rather review code than all these markdown files」。但她并不否定原则:「spec-first is definitely valuable in many situations」,同时「very skeptical that lots of up-front spec design is a good idea」【单源已核,单人定性】。Kiro 在 2026-02 加了 Bugfix 流程,并承认原流程「was not flexible enough」。
- Eberhardt(Scott Logic CTO)用 Spec Kit 重建自己业余应用里一个约千行的功能:第一个增量 agent 跑了 33 分半,产出 689 行代码和约 2,600–2,770 行 markdown,自报审阅约 3.5 小时;他惯用的小步迭代只需 8 分钟 agent 加约半小时人工。他的结论是「around ten times faster」(按他自报的数字是 7.6–12 倍),小节标题是「It didn't result in better code or fewer bugs」【单源已核,单人单次;对照臂在 git 里无重跑记录】。
- Marmelab 的 Zaninotto 写了那篇广为流传的「The Waterfall Strikes Back」。他举的「显示当前日期产出 8 个文件」实测是 1,865 行(不是 1,300 行),而且作者是 Marmelab 员工、另一个例子是 Marmelab 自家产品——都不是独立的现场样本。

## 4. 最大的观察研究测的不是 SDD

Hill 的 ESEM 2026 论文《Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects》是目前样本最大的研究:119 个开源仓库、88,052 个 PR。它常被当作「SDD 无效」的证据。三票验证和方法学审计后,它能说的要窄得多:

- **处理变量是「PR 有没有工单号」。**被判为「有 spec」的 PR 里 97.5% 只是引用了 issue/ticket;样本里没有任何仓库提交 SDD 工具产出。
- **分类器有代码缺陷。**论文代码的注释说会剥离 HTML 注释,实际只跳过了引用行,于是 PR 模板里的示例「Fixes #1234」被当成了工单引用;再加上「ID-BASED」这类连字符词被误认为工单号,按作者自己声明的意图修正后,13.9% 的「有 spec」PR 应翻为「无 spec」【现场核验,三票独立复跑 + 审计席复现】。
- **修正后的结果**:缺陷上看不出差别(按仓库聚类的区间约 −3.8 到 +2.7 个百分点;多种控制仓库差异的设定可排除超过约 1 个百分点的下降);返工反而略多,修正后约 +0.9 到 +1.2 个百分点,p≤0.02【单源已核 + 现场核验,关联】。缺陷归因用的 SZZ 方法本身误归因率在 46–71% 之间。
- **作者的框定有误。**正文说「Our study confirms this pattern」,但所引的两篇前作都没有测代码缺陷;一项独立研究(Rempel & Mäder,TSE 2017,24 个开源项目)反而发现需求到代码的可追溯性越完整、缺陷率越低,Hill 没有引用【方向存争】。

所以能写的是:**在开源仓库里,有没有工单号与缺陷无可辨关联,与略多返工相关——这测的是工单纪律,不是 SDD 工具。**

正方那边最常被引的两个大数字同样经不起溯源:「对照研究显示错误最多减少 50%」所引的两篇文章都没有数据;「安全缺陷减少 73%」是同一个开发者把同一个应用写两遍,CWE 违规 3 个对 11 个【单源已核,溯源】。

## 5. 主张二:spec 会不会烂掉

### 5.1 厂商的承诺与厂商自己的做法

Spec Kit 的方法论文档写:「Specifications stay in sync with code because they generate it」。同一个仓库的 CONTRIBUTING 写:「This does not mean every change goes through the full workflow」,并且把 `.specify/` 和 `specs/` 「intentionally gitignored」【单源已核,可复跑】。spec-kit 官方仓 reactions 最多的 issue(#1191,105 个 👍)是:无法方便地更新既有 spec、「Keeping specs in sync as features evolve」。早期 README 里那节「Experimental goals: Validate the hypothesis…」在 2026-09 的一次文档精简中被删掉,从未发布过验证结果。

### 5.2 公开数据能测什么,不能测什么

CMU 团队发布的 SpecMine 数据集在 7.3 万个公开仓库里找到 47 万个 spec 文件,92% 首次提交于 2026 年。看起来可以测「spec 提交后还改不改」,但数据集作者自己写明:「Commit counts therefore cannot show spec decay」【单源已核】。我们的审计证实了原因:单次提交的 spec-kit 功能 spec 里 66% 是 squash 合并进来的(分支上的修改看不见),OpenSpec 的归档文件 57% 是改名(历史被清零)。我们对 120 个仓库加了一个对照——同一套「冻结」定义下,根目录 README 停更的比例与 spec 相当(配对检验 p=0.27 与 0.79)【现场核验】。所以「spec 冻结率 X%」一类数字,本文一概不用。

能站住的只有两条:

- **装了不等于用了。**在前 60 个装了 spec-kit 的仓库里,17 个(28%)没有任何功能 spec;换一批 197 个仓库复测是 17%;另有约 6–8% 的 constitution 文件还是未填写的模板【单源已核 + 现场核验,写「约两到四成」】。
- **实践者自述分叉。**同一 CMU 团队访谈 21 名实践者(含 8 名工具作者),多数报告 spec 与代码分叉:实现时偏离的 8 人,spec 随代码变化过时的 7 人;作者归纳为「implementation detail may help agents while making specs prone to decay」【单源已核,定性;志愿者样本,作者明言不能说明有多普遍】。

### 5.3 弃用者怎么说

以 PR 标题自述计,移除 spec-kit 的 PR 与新增的 PR 之比从 2025 年底约 5% 升到 2026-10 约 18%,绝对量仍小(当月 34 个)【现场核验,标题短语计数会低估】。抽读的理由高度一致:

- 「a reviewed, confirmed issue *is* the specification. The pipeline's assets … were carrying cost without carrying work」(NetPace #317)
- 「it still installed 71 tracked files and injected 23 `speckit*` skills/commands into every agent session」(simonrowe #190,该 PR 未合并,移除另行落地)

常见做法是丢掉 T2 流程工具,保留 T1 需求关卡和 constitution。这和 UML 当年的命运几乎同构:Petre 那 11 个「选择性使用者」也是把图当思考工具,用完即弃。

## 6. 主张三:spec 能当源码吗——形式化一端的教训

「spec 即源码」最强的版本,其实已经在形式数学里跑过一遍:那里有机器验证器,「证明对得上陈述」可以被检查到最后一个符号。问题在于陈述本身是否表达了原题的意图。

- **两个独立团队逐题对齐 ProofNet**(一个本科数学证明基准):在形式陈述逐字相同的 130 题上,两队判断一致率 86.9%(κ=0.74),且一队判错的题另一队全部也判错,没有反向的题;更严的一队判约 55% 不忠实,较宽的一队约 42%。其中 104–106 条(约 28%)能被机器证明为假——证明器可以「正确地」证明一个错误的命题【多源证实,方向;具体数字单源已核,带版本】。
- **修订过一轮也不够。**已修过的 ProofNet# 版本,在独立尺度下仍有约 16–31% 的残余错误;号称「完全对齐」的 miniF2F-v2 里也有独立反例(如把立方根 −8 写成 8、漏掉 n≥2 的条件)。
- **软件规约同理。**微软研究院的 AutoCLRS 让 agent 为约 50 个经典算法写出规约、代码和证明(约 10 万行),机器检查全部通过;再让 agent 写小的具体测试去探规约,首轮发现 52 个算法里 8 个有实质缺口——例如 Prim 算法的后置条件会接受错误输出——作者说这只是下界【单源已核】。
- **由 spec 派生的测试可以被空桩通过。**一项研究的作者自曝:一个对所有请求都返回 {} 和 200 的空处理器,通过了全部由 spec 派生的可见测试(20/20)和留出测试(12/12),77 项保真检查一项都不匹配【单源已核,可复跑】。

意图形式化阵营自己承认这是中心瓶颈:「since there is no oracle for specification correctness other than the user」(Lahiri)。自然语言 spec 比形式陈述还多一层:它连「证明 ⊢ 陈述」那一层检查都没有。Böckeler 对 spec-as-source 的担忧——「might end up with the downsides of both MDD and LLMs: Inflexibility *and* non-determinism」——在这里有了机制解释。

至于「审 spec 比审代码便宜」:AutoCLRS 里约 5,000 行规约对应 10 万行代码与证明,但这是行数比,不是工时比;2024–2026 年我们没有找到任何直接比较「审规约 vs 审代码」工时或准确率的受控实验【未验证】。一个 5 人的审阅试点里,给审阅者 spec 基线没有让他们多找出问题(召回 0.525 对 0.518),审阅时间从约 27 分钟升到约 48 分钟【单源,博客】。

现实中的风向:spec-as-source 最激进的旗手 Tessl,2025-09 才发布首批产品(Spec Registry 公测与一个框架的封闭 beta),此后转向 agent skills 的注册与分发;它的首页现在写的是「agent enablement platform」和 skills,不再是「spec 生成代码」【单源已核】。

## 7. 谁在说话,谁受益

- **口号的出处。**「specs are the new code」不是 OpenAI 的 Sean Grove 说的,是他演讲活动页的 URL 片段;他的原话是「the coming of the new code, in particular specifications」,所指主要是 OpenAI 的 Model Spec。他说「Code is sort of 10% to 20% of the value that you bring」,没有给任何出处【单源已核,官方转录】。
- **关注度不等于使用。**spec-kit 有约 14.9 万 star,PyPI 安装包近 30 天约 8.4 万次下载(含 CI 重复安装);GitHub 上约 1.4 万个 spec-kit constitution 文件,同期 AGENTS.md 约 125 万个——给 agent 写上下文文件比走 SDD 脚手架普遍约两个数量级【现场核验,量级】。
- **厂商用定价承认了成本。**Kiro 2025-08 的定价里,spec 请求超额单价是普通请求的 5 倍($0.20 vs $0.04),后改为统一 credits【厂商口径】。BMAD 写「Small changes go straight to build」,Spec Kit 写不是每个变更都走全流程——厂商自己承认小任务不该走全流程。没有一家厂商公布过 plan/spec 模式对质量的对照测量。
- **企业案例。**唯一带数字的是 Asana 自述:7 名工程师首次使用 spec 流程后每周 PR +38%,作者自承 PR 数是不完美的代理指标,没有对照组。截至 2026-11 没有独立、带对照的企业测量【厂商口径】。
- **调查。**DORA 2025 里做「写规格说明」这项工作的从业者约 56% 已用 AI 协助;但没有任何大样本调查测过「spec-first 交给 agent」这一工作流【单源已核】。
- **咨询判断。**Thoughtworks 技术雷达 2026-11 版把 OpenSpec 从 Assess 升到 Trial,同时把「AI-driven documentation sprawl」列为 Caution;Böckeler 与雷达同属 Thoughtworks,不能算两个独立来源。
- **辩论两边都有利益相关方。**为 SDD 辩护的 Marc Brooker 是 AWS 工程师(AWS 出品 Kiro);讨论里为 plan 模式发声的 HN 评论者是 Claude Code 团队成员;反方的 Marmelab 例子出自自家员工与自家产品。

## 8. 证据分级总表

| 论断 | 分级 | 备注 |
|---|---|---|
| 意图说得越完整,agent 越成功 | 多源证实(方向) | 改的是信息量,不是流程 |
| 先计划再写码有效,随模型变强而缩小 | 单源已核 ×2 | MapCoder、Self-planning |
| 有执行神谕时先导出行为 spec:+2.7–7.2pp,成本 +48–130% | 单源已核 | SpecFirst |
| 测试进提示稳定提升函数级通过率 | 多源证实(方向) | 多为上界设定 |
| TiCoder:测试反馈让判断更准 | 单源已核(仅方向) | 标题数字弃用 |
| 完整 SDD 流程 vs 直接实现的质量差异 | 未验证 | 两项对照均未通过审计 |
| SDD 流程更慢、更贵 | 单源已核(方向)+ 厂商定价 | 幅度不承重 |
| Uvik 基准的任何数字 | 弃用 | 方法学审计 D |
| 有工单号的开源 PR 不更少缺陷 | 单源已核 + 现场核验 | 不是 SDD 证据 |
| 需求可追溯 ↔ 缺陷 | 方向存争 | Rempel vs Hill |
| 公开提交史测不出 spec 漂移 | 单源已核 | 数据集作者自认 |
| 装了 spec-kit 不等于用了 | 单源已核 + 现场核验 | 约两到四成 |
| 多数实践者自述 spec 与代码分叉 | 单源已核(定性) | 不可写成比例 |
| spec 冻结率、单提交率 | 弃用 | 构念效度不成立 |
| 形式基准大面积「证对了但证错了题」 | 多源证实 | 两团队逐题对齐 |
| 审 spec 比审代码便宜 | 未验证 | 无直接实验 |
| 「需求阶段修 1、上线后修 100」 | 方向存争 | 源头为 1970 年代大型项目 |
| Royce 1970 | 单源已核 | 不说「瀑布」,要更多文档 |
| 「specs are the new code」出自 Grove | 弃用(误引) | URL 片段 |
| Kiro/Tessl/Spec Kit 自述 | 厂商口径 | — |

## 9. 十个可检验主张

按证据强度排序:

1. **在信息量相同的条件下,SDD 工具的完整流程不比一段写清楚的提示产出更好的代码。**检验:同一 agent、同一模型、多次运行,三臂——无 spec、把 spec 内容写进单段提示、走完整 Spec Kit/Kiro 流程——在仓库级任务上比较通过率、缺陷与成本;预注册,公开日志。(今天的两项对照都不满足)
2. **SDD 的收益集中在多文件、新功能任务,在 bug 修复、重构、写测试上为负。**检验:在第 1 条的设计里按任务类型分层,每层样本足以检出 10 个百分点的差异。(Uvik 报过这个模式,但数据被否决)
3. **先写 spec 的增益大部分可以由「先推理」复现。**检验:加一个「先写推理、不写 spec」臂,比较它与 spec 臂的差距。
4. **随着模型变强,先计划、先写 spec 的边际收益缩小。**检验:同一基准、同一流程,跨三代模型重复,看增益是否单调下降。(Self-planning 与 TiCoder 的复跑方向一致)
5. **spec 停更的速度与普通文档相当。**检验:在不使用 squash 合并的仓库里,比较 spec 文件与 README、设计文档自最后一次修改到下一次相关代码修改的间隔分布。
6. **spec 与代码的分叉主要发生在实现阶段,而不是维护阶段。**检验:对一组活跃仓库,在每次功能合入时由独立评审标注 spec-代码一致性,纵向跟踪 6 个月,分别统计合入时与之后的不一致率。
7. **由 spec 派生的测试套件普遍弱于手写测试。**检验:对每个 SDD 项目跑「空桩基线」和变异测试,报告空桩通过率与变异杀死率。
8. **「审 spec 比审代码便宜」只在规约可被机器检查时成立。**检验:同一组审阅者、同一缺陷注入,随机分配审 T1 spec、审 T3 规约、审代码,比较检出率与耗时。
9. **工单纪律(而非 SDD 工具)与返工正相关的发现,在控制任务难度后消失。**检验:用独立的任务难度标注(而非 PR 规模)重做 Hill 的匹配,并修正其分类器缺陷。
10. **SDD 工具会走 UML 的路:保留「写清楚」的习惯,丢掉工具与流程。**检验:两年后在同一批仓库里,统计仍保留 constitution/需求文档但已移除流程工具的比例,与两种都保留、两种都移除的比例对比。

## 附:方法学与本期的自我修正

本期在研究过程中推翻或收窄了一些我们自己起初接受的说法:

- 「Royce 发明了瀑布 / Royce 反对瀑布」→ 两者都错:原文无此词,他认为阶段化健全、要求更多文档;
- 「Boehm:上线后修是需求阶段的 100 倍以上」→ 大项目中位约 50–60 倍、小项目约 2–4 倍,1970 年代数据、单位混杂;
- 「OMG:平台无关模型包含驱动平台模型的全部信息」→ 原文无此句;
- 「Hill 证明 SDD 不降缺陷」→ 测的是工单号;修正分类器缺陷后缺陷仍无差,返工略多;
- 「Hill 的结果与前人研究一致」→ 所引前作没测代码缺陷,有独立研究方向相反;
- 「Spec Kit Agents 是唯一的直接对照,证明质量无差、耗时 +67%」→ 预算不对等、幸存者不同,只剩「更慢」的方向;
- 「Uvik:spec 让合并率 +8–12pp、缺陷减半、OpenSpec 最省」→ 不显著,且原始数据有三处方法矛盾,弃用;
- 「TiCoder 平均提升 45.97%、15 名专业开发者、p<0.001」→ 同文表复算 33.50pp,参与者含学术界,p 值在 15 人下不可能;
- 「spec-kit 装了以后 76% 的 spec 从不修改」「spec 冻结 18%」→ squash 合并与归档改名使提交数失效,冻结率与 README 同量级;
- 「80% 的 spec PR 同时改代码,说明 spec 与代码同步」→ 多为新 spec 随实现一起合入;
- 「LLM 判官系统性高估形式化忠实度 8–41pp」→ 同一论文另一设定方向相反,方向存争;
- 「specs are the new code(Grove)」→ 活动页 URL 片段;
- 「Claude Code 文档:能用一句话描述 diff 就跳过计划」→ 现行文档无此句;
- 「Kiro 25 万开发者、spec 贵 1.8 倍」→ 原文是「前 5 天 >10 万人试用」,超额单价比为 5 倍;
- 「Tessl 让正确使用 API 的比例提升 35%」→ 所引博文无此数。

本期没能拿到的一手文件:Bossavit《Leprechauns of Software Engineering》正文、Boehm 1981 原书、Bell & Thayer 1976 的 ACM 原文、Parnas & Clements 1986 的 TSE 版、Dijkstra EWD667 与 Knuth 1984 原文(本文未用)、Kemerer 1992 原文、Hebig 2016 与 Zampetti 2020 全文、Rempel & Mäder 2017 全文(只用方向,不引效应量)、TiCoder 用户研究原始数据(未公开)、Uvik 的任务集与原始日志、Spec Kit Agents 的代码与数据(未公开)。相关论断已按二手或未验证降级。

## 附:主要来源

**正方与机制**:Jiang 等 2024「Self-Planning Code Generation with Large Language Models」(ACM TOSEM 33(7))、Islam 等 2024 MapCoder(ACL 2024)、ClarifyGPT(FSE 2024)、Fakhoury、Lahiri 等 TiCoder(IEEE TSE 2024)、Lahiri 2026「Intent Formalization: A Grand Challenge…」(https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/;arXiv 2603.17150)、Chen 等 2026 SpecFirst(arXiv 2607.27167)、Chacón Sartori 2026「The Specification Gap」(arXiv 2603.24284)、Deng 等 2025 SWE-Bench Pro(arXiv 2509.16941)、Taghavi & Bhavani 2026 Spec Kit Agents(arXiv 2604.05278)、Endres 等 nl2postcond(FSE 2024)

**反方与实操**:Hill 2026「Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects」(ESEM 2026,LIPIcs;数据 https://github.com/brennhill/delivery-gap-research)、Böckeler 2025「Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl」(https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)、Eberhardt 2025「Putting Spec Kit Through Its Paces」(https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html)、Zaninotto 2025「Spec-Driven Development: The Waterfall Strikes Back」(https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)、Rempel & Mäder 2017(IEEE TSE)、Pirouzkhah 2026(MSR)

**历史**:Royce 1970「Managing the Development of Large Software Systems」(Proc. IEEE WESCON)、Bell & Thayer 1976(ICSE)、Brooks 1986「No Silver Bullet」(UNC TR86-020)、Boehm 1981《Software Engineering Economics》、Bossavit 的溯源笔记、Menzies 等 2017(arXiv 1609.04886)、OMG MDA Guide 1.0.1(omg/2003-06-01)、Petre 2013「UML in Practice」(ICSE 2013)、Hutchinson 等 2011(ICSE 2011)、Whittle 等 2014(IEEE Software)、Hebig 等 2016(MoDELS)、Zampetti 等 2020(IST)、Fucci 等 2017(IEEE TSE)、Nagappan 等 2008(EMSE)

**形式化一端**:ProofNet-Verified 与 ProofNet#(Poiroux 等)审计数据、ReForm ConsistencyCheck、miniF2F-v2、Swamy 2026 AutoCLRS(https://risemsr.github.io/blog/2026-03-06-autoclrs/)、Swamy & Lahiri 2026 SPOTs(https://risemsr.github.io/blog/2026-04-16-spotting-specs/)、Fawcett 2026 Rebuild Dossier(arXiv 2608.23616;https://github.com/Parker-Fawcett/rebuild-dossier)

**厂商、采用与测量**:github/spec-kit(README、spec-driven.md、CONTRIBUTING.md @ f29319d;issue #1191)、Fission-AI/OpenSpec、BMAD-METHOD、kiro.dev 博客与定价页、Tessl 博客与 TechCrunch 报道、Grove 2025「The New Code」(AI Engineer World's Fair)、Thoughtworks Technology Radar Vol.33–35、DORA 2025、Stack Overflow Developer Survey 2025/2026、Agarwal 等 2026「Spec-Driven Development as Prescribed and as Practiced」(arXiv 2608.25202)与 SpecMine 数据集(doi:10.5281/zenodo.22102779)、Uvik SDD benchmark 页面与原始 CSV、Asana 工程博客、FrankRay78/NetPace PR #317、simonjamesrowe-dev-monorepo PR #190

**本站相关**:spec 是给 agent 写的上下文的一种,常驻上下文文件的证据见[《给 Agent 看的 README》](https://hub.cissychen.com/deep-research/agent-readme-deep.html);审 spec 与审代码都是验证瓶颈问题,见[《AI code review:验证瓶颈的解药,还是套娃?》](https://hub.cissychen.com/deep-research/ai-code-review-deep.html)与[《机器 Oracle 全景》](https://hub.cissychen.com/deep-research/machine-oracles-deep.html);上一轮方法论转型的尸检见[《「70% 转型失败」考古》](https://hub.cissychen.com/deep-research/seventy-percent-failure-deep.html);人握终审的人因证据见[《自动化的反讽》](https://hub.cissychen.com/deep-research/automation-irony-deep.html)。
