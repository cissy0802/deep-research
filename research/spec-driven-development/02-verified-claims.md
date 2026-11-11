# 02 承重论断 · 验证结论 · 证据分级(成文唯一依据)

分级词表:**多源证实**(≥2 独立来源同向)/ **单源已核**(一手可回溯)/ **方向存争**(独立来源矛盾)/ **厂商口径**(利益相关方自述)/ **现场核验**(本站复算或复测)/ **未验证** / **弃用**。依据:03(Round 2,96 票)+ 04(Round 3,12 份审计,47 项否决)。凡与 Round 3 冲突的 Round 2 写法,以 Round 3 为准。

## A. 主张 1:先写 spec 能提升 agent 产出吗

| # | 可承重写法 | 分级 | 关键限定 / 禁写 |
|---|---|---|---|
| A1 | 题面/规约信息量越完整,agent 越成功:The Specification Gap 逐级剥离规约,单 agent 89%→56%,恢复完整规约回到 89%;TD Bank 段落 spec 27/30、清单 30/30、只有计划无 spec 2/30;SWE-Bench Pro 去掉 requirements+interface 后 GPT-5(high)25.9%→8.4% | 多源证实(方向;机制=信息量) | 都是**改题面信息量**,不是 SDD 流程;单作者/单团队、主实验单次运行;SWE-Bench Pro 作者把退化唯一归因于测试只认特定接口名的假阴性;题面本已充分时无增益(TD Bank) |
| A2 | 先计划再写码在论文内有干净消融:MapCoder 去掉计划 agent HumanEval 80.0→70.0;Self-planning 在 2023 年 175B 补全模型上 48.1→60.3%(单次贪心,token 约 11.6×);对更强指令模型增益缩到约 5–6% | 多源同向(单源已核 ×2) | 禁写 MapCoder「ChatGPT」行(表注自承取自 Jiang et al.);PlanSearch 77.0/60.6/41.4 是三个模型;13B 模型自写计划反降 34.0→30.1 |
| A3 | 有执行神谕时先导出行为 spec 再写码:SpecFirst(Huawei/Queen's,ProgramBench 200 实例 × 4 模型)通过率绝对 +2.7 到 +7.2pp(相对 +6.9–21.3%),配对 Wilcoxon 全部 p<0.01;成本 +48–130% | 单源已核(主线程回一手) | spec 由 agent 探测可执行二进制得到(有执行反馈),不是人写 PRD;作者为方法提出者;似单次运行 |
| A4 | 测试/示例(T4)进入提示稳定提升函数级通过率(5–20pp,多为上界设定),难题上收益变小 | 多源证实(方向) | TiCoder Table V 测试入提示有泄漏;ClarifyGPT 真人实验参与者看过测试(T1 混入 T4) |
| A5 | 澄清问题:向「持有完整题面的模拟用户」提问可恢复部分解决率;但模型不被要求时基本不提问,一味提问在清晰题面上大幅掉分(HumanEvalComm 65.6%→27.5%) | 单源已核 ×多 | 模拟用户 = 理想化上界;Ambig-SWE「最高 74%」= 最弱模型相对值 |
| A6 | TiCoder 用户研究:15 人组内,看到测试反馈后对 AI 代码对错判断更准、自报负荷更低 | 单源已核(**仅方向**) | **弃用**:标题「平均绝对提升 45.97%/45.73%/38.43%」(同文 Table IV 复算 33.50pp)、「84% 判断正确」(n=15 下不可能为 k/15)、p=0.001(n=15 精确检验最小 0.016)、「15 名专业开发者」(6 工业 + 9 学术)、「不省时」(功效不足);作者为方法提出方 |
| A7 | TiCoder 式交互增益在新模型新基准上大多缩到 ≤3pp(VLP,2026 年模型,6 格中 5 格) | 方向存争 | VLP 为竞品作者、未同行评审、读图值 |
| A8 | **完整 SDD 流程 vs 直接实现**的公开对照都太弱,无法回答问题:Spec Kit Agents(预印本)LLM 评审 3.51 vs 3.46、完成运行时间更长;Uvik 同设计但被否决 | 未验证(质量差异);单源已核(仅「SDD 更慢」方向) | **禁写**「3.51 vs 3.46 证明质量无差」「+67%/1.7×」「人类偏好与判官相反」「+0.15 证明 hooks 有效」;两臂时间预算 90 vs 40 分钟、幸存者不同、MDE 0.2–0.5;无代码/数据、作者单位未披露 |
| A9 | 生成侧小样本:先推理(无 spec)几乎复现先写 spec 的增益(59%→95% vs 92%) | 单源(博客,未见论文) | n=4、双模型;只作「额外推理是混杂」的提示,不承重 |
| A10 | 更好的指导文件让 agent 更常找到该改的文件,但每个 patch 的精度不变(约 59%,p=0.119)——spec 若作用于此,解决的是「改哪」不是「改对」 | 单源已核(#14 已核,Shepard & Albrecht) | 是可检验假说,不是结论;「SDD 有效成分是反馈环」推翻 |
| A11 | #14 已核:常驻上下文文件无一致成功率提升;成本方向存争(AGENTbench +20–23% vs Lulla −28.64%) | 方向存争 | AGENTbench 已出 v3(CTXBENCH,结论软化 + 显著性检验)——#14 需另行修正,本文只引 v3 口径「不普遍提升」 |
| A12 | METR 2025 RCT 只迁移方法学教训「自评≠测量」 | 单源已核(#0 已核) | 2026-02 更新(回访者 −18%、新招募 −4%,METR 自评受选择影响)→ 不得把「慢 19%」写成现状 |

## B. 主张 2:spec 能保持活性、不与代码漂移吗

| # | 可承重写法 | 分级 | 关键限定 / 禁写 |
|---|---|---|---|
| B1 | **公开提交史测不出 spec 漂移**——数据集作者原文「Commit counts therefore cannot show spec decay」 | 单源已核 | — |
| B2 | 多数受访实践者自述 spec 与代码分叉(21 人访谈,其中实现时偏离 8 人、spec 随代码过时 7 人);作者另述「implementation detail may help agents while making specs prone to decay」 | 单源已核(定性) | **禁写成比例**(志愿者样本、单人编码、作者原话「not how common」);与 SpecMine 同组 |
| B3 | 装了≠用了:前 60 个装了 spec-kit 的仓库 17 个(28%)无任何功能 spec;换样本 197 仓为 17%;论文另报 29.9% 的仓至多一次 spec 提交;constitution 空模板 8/100、13/200 | 单源已核 + 现场核验 | 非随机样本;写「约两到四成」 |
| B4 | spec 停更与 README 停更同量级(McNemar p=0.27/0.79) | 现场核验(R5-M) | 「冻结率 18/15/5%」「三工具排序」**禁写**(阈值敏感 8–35%、右截尾、换样本 5.6%) |
| B5 | spec PR 多同改代码,但多为新 spec 随实现一起合入(54%);修改已有 spec 且同改代码约 35% | 现场核验 | 「80.5% 共变 = 同步证据」**禁写**(条件方向反、只含已合并 PR);「单提交 76%/84%」**弃用**(squash 66%、归档改名 57%) |
| B6 | Spec Kit 自家仓库把 `.specify/` 与 `specs/` 加进 .gitignore,CONTRIBUTING 写「not every change goes through the full workflow」;同一工具文档写「Specifications stay in sync with code because they generate it」 | 单源已核(厂商自述反向事实,可复跑 @ f29319d) | — |
| B7 | spec-kit 官方仓 reactions 最多的 issue(#1191,105 👍)是「无法方便地更新既有 spec / 随功能演化保持同步」;2026-04-08 以社区扩展关闭 | 单源已核 | 「#442 第二」推翻(实为 #1213) |
| B8 | 弃用理由集中在「承担成本不承担工作」:NetPace #317「a reviewed, confirmed issue *is* the specification」;simonrowe #190「71 tracked files … 23 `speckit*` skills/commands into every agent session」;移除/新增 PR 标题比约 5%→18%(当月 34 个) | 单源已核(引语)/ 现场核验(计数) | #190 未合并、ketcher #11517 仍开 → 不写「已弃用」;标题短语计数严重低估 |
| B9 | 历史前科:Petre 2013 50 名开发者 0 人全面采用 UML、35 人不用、同步一致性为障碍;Hutchinson 2011「the need to keep models/code in sync」;Hebig 2016 GitHub UML 文件 73.33% 从未更新;Zampetti 2020 BDD 场景与代码仅约 37% 共演化、spec 变更同时或晚于代码 | 多源同向(类比) | Hebig、Zampetti 部分为摘要/二手;只作类比,不作 SDD 漂移率 |
| B10 | Uvik「7.9% spec 不一致」 | 弃用 | 13/164、单时点、判定重测信度未观测、厂商被否决 |

## C. 主张 3:spec 能成为唯一事实源、代码可再生吗

| # | 可承重写法 | 分级 | 关键限定 / 禁写 |
|---|---|---|---|
| C1 | 即便有机器验证器守住「证明 ⊢ 陈述」,「陈述 = 意图」仍大面积失守:两个独立团队逐题对齐 ProofNet(130 题逐字相同,一致率 86.9%,κ=0.74,无反向题),更严的一方约 55%、较宽的一方约 42% 判为不忠实;104–106/367(约 28%)能被机器证明为假;修订过一轮的 ProofNet# 在独立尺度下仍有约 16–31% 残余错误 | **多源证实**(方向)/ 单源已核(具体数) | 带版本(205/99 现版,204/97 首版);被审为 Lean 4 移植版;根因百分比**未验证**;「LLM 判官系统性高估 8–41pp」**禁写**(方向存争);miniF2F「逾半错位」禁写(约 40%,含设计内「简化」);Faults 398 只作下限 |
| C2 | T3 一端多个独立团队:机器能查「证明 ⊢ 规约」,查不了「规约 = 意图」——AutoCLRS 机器已证明通过的 agent 规约里 52 个算法有 8 个存在实质缺口(如 Prim 后置条件接受错误输出),作者说这只是下界;约 5,000 行规约对 10 万行代码与证明(行数比) | 多源同向 | 行数比不是工时比;「审 spec 比审代码便宜」**没有**直接对照实验(未验证) |
| C3 | 意图形式化阵营自己划界:Lahiri「since there is no oracle for specification correctness other than the user」;Spec Kit 式 spec「remain informal and uncheckable」 | 单源已核 | — |
| C4 | spec 派生测试会被空桩通过:一个对所有请求返回 {} 与 200 的 handler 通过全部可见(20/20)与留出(12/12)测试,77 项保真检查 0 项匹配 | 单源已核(作者自曝,可复跑) | — |
| C5 | spec-as-source 旗手 Tessl:2025-09 才发布(原称 2025 初)、2026-01 起转向 skills registry / 「agent enablement platform」,spec 生成代码引擎从未 GA;TechCrunch 正文 $750M 估值 | 单源已核 / 厂商口径 | Tessl「35%」「57%→93%」**伪引**;1.17×/1.2× 自相矛盾 |
| C6 | Böckeler(Thoughtworks)对 spec-as-source:「might end up with the downsides of both MDD and LLMs: Inflexibility *and* non-determinism」 | 单源已核(单人定性) | Thoughtworks Radar 与 Böckeler 同公司,非两个独立来源 |

## D. 历史考古

| # | 可承重写法 | 分级 | 关键限定 / 禁写 |
|---|---|---|---|
| D1 | Royce 1970 原文 0 次出现「waterfall」;单趟实施「is risky and invites failure」,但「fundamentally sound」,药方是更多前置文档(「ruthless enforcement of documentation requirements」「the documentation is the specification and is the design」)+ 做两遍 + 客户参与;编码「managed with relative ease」 | 单源已核(PDF 文本层 + 页图;Bossavit 独立同读) | 禁写「Royce 发明/反对瀑布」;「1500 页」单引禁写(扫描损坏);Bell & Thayer 是已知最早印刷用例,非首创 |
| D2 | Brooks 1986「The hardest single part of building a software system is deciding precisely what to build」;转引 Parnas「automatic programming always has been a euphemism for programming with a higher-level language than was presently available」 | 单源已核(UNC TR86-020) | Parnas 句须注「经 Brooks 转引」 |
| D3 | 「需求阶段修 1 块、上线后修 100 块」源头几乎都追到 Boehm 1981 一张图:1970 年代大型项目、四个来源、单位混杂、无原始数据;大项目需求→运行中位约 50–60×(各源 30–200×),小项目约 2–4×;「IBM Systems Sciences Institute」是内部培训单位;Menzies 2017 对 171 个 TSP 小项目未见延迟效应,但同文列有 NASA/Reifer/Willis 同向测量 | 多源(溯源)/ 方向存争(效应) | 「100× 以上」「5–9×」推翻;「Menzies 推翻 Boehm」禁写(样本不重叠);「无独立证据」禁写 |
| D4 | MDA/MDE:OMG MDA Guide 原文是「automate at least some of the construction… regenerate for the new infrastructure」;MDE 生产率宣称 +20% 到 +800%,比较研究 +35% 到 −27%;Whittle 等:收益多来自被迫把架构写清楚 | 单源已核 | 「PIM contains enough information to drive PSMs」**伪引**;Kemerer 70/25/5 **禁写** |
| D5 | TDD:Fucci 2017 测试先写或后写无重要差异(要紧的是小步匀速);Nagappan 2008 四团队非随机缺陷密度下降 | 单源已核 | Bissi 76%/88% 禁写;三种 TDD 证据口径不可合并 |

## E. 厂商口径、采用与话语

| # | 可承重写法 | 分级 | 关键限定 / 禁写 |
|---|---|---|---|
| E1 | 「specs are the new code」不是 Grove 原话(活动页 URL slug);原句「the coming of the new code, in particular specifications」;「Code is sort of 10% to 20% of the value」无出处;「code itself is actually a lossy projection from the specification」 | 单源已核(官方转录) | Grove 的 spec 主要指 OpenAI Model Spec |
| E2 | Spec Kit 早期 README「Experimental goals: Validate the hypothesis…」,2026-09-15 精简 commit 删除,从未发布验证结果;spec-driven.md 唯一量化对比是虚构示例(约 12 小时 vs 15 分钟,只计生成) | 单源已核 / 厂商口径 | — |
| E3 | 关注度 vs 安装:spec-kit 149k star,PyPI specify-cli 近 30 天约 8.4 万下载;OpenSpec npm 422 万/30 天、BMAD 8.9 万;GitHub 上约 1.4 万个 spec-kit constitution 文件 vs 约 125 万个 AGENTS.md;SpecMine 7.3 万公开仓 47 万 spec 文件,92% 首次提交于 2026 年 | 现场核验 / 单源已核 | 下载含 CI 重复拉取;code search total_count 只作量级(非单调);文件≠项目 |
| E4 | Kiro:前 5 天 >10 万人试用(AWS 自述);2025-08 定价 spec 请求超额 $0.20 vs vibe $0.04(5×),按 Kiro 定义写 spec 文档计 vibe、spec request 只计执行 tasks;后改统一 credits;2026-02 新增 Bugfix spec,Kiro 自认原流程「was not flexible enough」 | 厂商口径 | 「25 万」「3 亿次」「spec 贵 1.8 倍」禁写;PKFARE「60×」须带下沿 30× |
| E5 | 厂商自己承认小任务不该走全流程:Spec Kit CONTRIBUTING、BMAD「Small changes go straight to build」;Cursor「significantly improve the code」无数据 | 单源已核 / 厂商口径 | Claude Code「describe the diff in one sentence, skip the plan」**禁作引语**(现行文档无);现行文档推荐「访谈 → SPEC.md → 新会话实现」 |
| E6 | Thoughtworks Radar:SDD 2025-11 Assess、Spec Kit 2026-04 Assess(当前版均未保留)、OpenSpec 2026-04 Assess → 2026-11 Trial;Vol.35 把「AI-driven documentation sprawl」列 Caution | 单源已核(咨询专家判断) | 与 Böckeler 同公司 |
| E7 | 调查:DORA 2025「Creating specifications」56%、「Analyzing requirements」49%(做这项工作者中依赖 AI);SO 2026「写工单/需求/计划」27.8% 在用 AI、30.5% 不用也不打算;没有大样本调查测「spec-first 交给 agent」这一工作流 | 单源已核 / 厂商口径(调查方) | JetBrains「13%」禁写;SO 2026 样本 30,903 |
| E8 | 企业报告:唯一带数字的是 Asana 自述(7 名工程师、每周 PR +38%,作者自承 PR 数是不完美代理、无对照);截至 2026-11 未见独立带对照的企业测量 | 厂商口径 | Rackspace「52 周→3 周」禁写 |
| E9 | 话语中的利益相关:Marc Brooker(AWS)辩护;HN 评论者 bcherny(Anthropic,Claude Code);Zaninotto 的例子为 Marmelab 员工/自家产品;Uvik 为 Claude Partner Network 成员 | 单源已核 | Brooker 只写「AWS 工程师」 |

## F. 大样本观察研究(Hill ESEM 2026)

| # | 可承重写法 | 分级 | 关键限定 / 禁写 |
|---|---|---|---|
| F1 | 119 个开源仓库、88,052 个 PR:PR 是否关联工单/issue 与缺陷无可辨关联(仓库聚类 CI 约 [−3.8, +2.7]pp;多种控制仓库设定可排除 >约 1pp 的下降),与略多返工相关(修正分类器缺陷后 +0.9 到 +1.2pp,p≤0.02) | 单源已核 + 现场核验(关联) | 测的是「有没有工单号」(97.5%),样本零 SDD 工具产出 → **不是 SDD 证据**;分类器缺陷致 13.9% 误判;SZZ 误归因 46–71%;事后选样、停止规则=零结果稳定;单作者无利益声明;SSRN 版头条相反 |
| F2 | 「需求可追溯 ↔ 缺陷」:Rempel & Mäder(TSE 2017)同向有益 vs Hill 零 | 方向存争 | Hill「Our study confirms this pattern」不成立 |
| F3 | SDD 文献最常被引的两个大数字:「错误最多减少 50%」追到源头无数据;「安全缺陷减少 73%」= 同一开发者写两遍、3 vs 11 个 CWE 违规 | 单源已核(溯源) | 禁作 SDD 有效证据 |

## G. 实操评测(单人定性)

| # | 可承重写法 | 分级 | 关键限定 / 禁写 |
|---|---|---|---|
| G1 | Böckeler(2025-10,Kiro 未 GA):小 bug 变「4 "user stories" with a total of 16 acceptance criteria」「like using a sledgehammer to crack a nut」;「I'd rather review code than all these markdown files」;但「spec-first is definitely valuable in many situations」,且「very skeptical that lots of up-front spec design is a good idea」 | 单源已核(单人单次定性) | 须带日期;Kiro 2026-02 已加 Bugfix 流程 |
| G2 | Eberhardt(Scott Logic CTO):Spec Kit 第一增量 agent 33m30、689 行代码、约 2,600–2,770 行 markdown、自报审阅 3.5 小时;惯用小步迭代 8 分钟 agent + 约半小时;「around ten times faster」(按其自报数字 7.6–12×);小节标题「It didn't result in better code or fewer bugs」 | 单源已核(单人单次) | 对照臂 git 无重跑痕迹;分步数字自相矛盾,只引总计 |
| G3 | Zaninotto(Marmelab):「8 文件」实测 1,865 行;例子出自 Marmelab 员工与自家 Atomic CRM | 单源已核 | 「1,300 行」推翻;「80% 时间在读」不作数据 |
| G4 | Garg(InfoQ)5 人审阅试点:有 spec 基线召回不变(0.525 vs 0.518)、81% 发现可指到条款(无基线 0%)、审阅 48 vs 27 分钟 | 单源(博客) | 测的是人工审阅;n=5 |
| G5 | 幽灵完成:工具作者自报约 3/830(~0.36%),罕见且静默 | 单源已核 | — |

## H. 弃用 / 不得承重的数字总表
Uvik 全部效应与成本数字(R2-M 评级 D);Spec Kit Agents 全部比较数字(R3-M C);TiCoder 标题数字与 0.84/p=0.001;冻结率与单提交率;7.9% 漂移;LLM 判官高估;ProofNet 根因百分比;Tessl 35%/57→93%;Kiro 25 万/3 亿/1.8 倍;JetBrains 13%;Rackspace;Kemerer 70/25/5;Bissi;Piskala 50%;Marri 73%(作有效证据);OMG/Claude Code/Grove 三处伪引或误引。
