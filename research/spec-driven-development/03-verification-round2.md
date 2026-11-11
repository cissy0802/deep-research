# 03 Round 2 · 3 票对抗验证判决(32 组 × Q/X/K = 96 票)

镜头:Q 逐字(回一手逐字核引语与数字)/ X 反证(勘误、更新版本、独立矛盾测量)/ K 口径(复算、混口径、外推缺口、利益相关)。3 镜头 × 4 批(B1 G01–G08 / B2 G09–G16 / B3 G17–G24 / B4 G25–G32)= 12 个独立子代理,互不可见,refute-by-default。网络在 Round 2 开始前改为不受限(Round 1 为受限运行,见 STATE)。逐票原文见 verdicts/。

| 组 | 主题 | Q 逐字 | X 反证 | K 口径 |
|---|---|---|---|---|
| G01 | LLM 计划先行(T2):Self-planning、MapCoder、Self-collaboration、SCoT、PlanSearch | 修正 | 修正 | 修正 |
| G02 | 需求澄清(T1):ClarifyGPT、Ambig-SWE、HumanEvalComm、Ask or Assume | 修正 | 修正 | 修正 |
| G03 | TiCoder 与测试入提示(T4) | 修正 | 修正 | HOLDS |
| G04 | 意图形式化 vs SDD:Lahiri、nl2postcond、Dafny 规约评估 | 修正 | 修正 | 修正 |
| G05 | 仓库级计划/流程:CodePlan、Spec Kit Agents、SWE-RPG、Google 规约驱动测试 | 修正 | 修正 | 修正 |
| G06 | Hill ESEM 2026:设计、处理变量、选样与评审轨迹 | 修正 | 修正 | 修正 |
| G07 | Hill ESEM 2026:H1–H5 结果、版本差与勘误 | HOLDS | 修正 | 修正 |
| G08 | SDD 文献引用链与转述失真 | 修正 | 修正 | 修正 |
| G09 | Böckeler 实操评测(Kiro/spec-kit/Tessl) | HOLDS | 修正 | 修正 |
| G10 | Eberhardt(Scott Logic)与 Zaninotto(Marmelab)实操 | 修正 | 修正 | 修正 |
| G11 | Spec Kit 用户 issue、幽灵完成、小型试点与成本断言 | 修正 | 修正 | 修正 |
| G12 | Royce 1970 原文与「waterfall」一词考古 | 修正 | 修正 | 修正 |
| G13 | 专家论证:Brooks、Parnas、Dijkstra、Knuth | 修正 | HOLDS | HOLDS |
| G14 | Boehm 缺陷成本曲线与其溯源/反证 | 修正 | 修正 | 修正 |
| G15 | UML/MDA/CASE 采用与衰落 | 修正 | 修正 | 修正 |
| G16 | BDD 与 TDD 证据 | 修正 | HOLDS | 修正 |
| G17 | Spec Kit 厂商口径与自家 dogfooding | 修正 | HOLDS | 修正 |
| G18 | OpenSpec、BMAD 与各家 plan mode | 修正 | 修正 | 修正 |
| G19 | AWS Kiro:发布、用量、定价与客户案例 | 修正 | 修正 | 修正 |
| G20 | Tessl、Grove「新代码」演讲与 Thoughtworks Radar | 修正 | 修正 | 修正 |
| G21 | Uvik SDD benchmark | 修正 | 修正 | 修正 |
| G22 | 单人对照、Rebuild Dossier 与门控流程个案 | 修正 | 修正 | 修正 |
| G23 | 规约完整度的受控消融 | 修正 | 修正 | 修正 |
| G24 | #14/#0 已核口径的迁移 | HOLDS | 修正 | 修正 |
| G25 | Autoformalization 忠实率与形式基准题面错位 | 修正 | 修正 | 修正 |
| G26 | LLM 生成形式规约:AutoCLRS、SpecGen、Verus、TLA+、Clover | 修正 | 修正 | 修正 |
| G27 | PBT、规约审阅成本与形式验证中的规约缺陷 | 修正 | 修正 | 修正 |
| G28 | 开发者调查(SO/JetBrains/DORA/Octoverse) | 修正 | 修正 | 修正 |
| G29 | GitHub 足迹与 SpecMine 普查 | 修正 | 修正 | 修正 |
| G30 | 装了≠用了:constitution 空模板、spec 活性与冻结 | 修正 | HOLDS | HOLDS |
| G31 | 弃用 PR 与弃用理由 | 修正 | 修正 | 修正 |
| G32 | 企业案例与话语场 | 修正 | 修正 | 修正 |

**合计:10 HOLDS / 86 修正 / 0 组级推翻。** 0 组级推翻不代表论断干净——推翻全部发生在子论断层,且多处承重数字被降级或禁写(见下)。Round 1 的 86 条 secondhand 中,各镜头合计约 267 条次补核升级为 verbatim(三镜头间大量重叠,按条目去重约百余条)。

## 伪引用(按红线处理)
- **H27** OMG MDA Guide「PIM … contains enough information to drive one or more PSMs」:Q/K/X 三票独立确认 omg/2003-06-01 全文 0 命中 → 伪引用;改用原件 §2.2.12/§2.2.15/§3.7 措辞(「automate at least some of the construction… regenerate for the new infrastructure」),原件无「唯一事实源」说法。
- **V30** Claude Code「If you could describe the diff in one sentence, skip the plan」:现行文档全站 grep 0 命中、Wayback 不可达 → 禁作逐字引用(现版文档反而推荐「访谈 → SPEC.md → 新会话实现」)。
- **V26**「specs are the new code」不是 Grove 原话(活动页 URL slug);最接近原句「the coming of the new code, in particular specifications」(ai.engineer 官方转录已核)。V28 结尾句补「test against the model」。
- **M31** Tessl「约 35%」「Bowser 57%→93%」在所引博文中找不到 → 推翻;同文 1.17X / 1.2X 自相矛盾,测的是 rubric 打分的 abstraction adherence。

## 子论断推翻(数字/事实被一手证伪)
- **H18** Boehm 曲线读图:「5–9」是纵轴读数非倍数;小项目需求→验收约 2–4×;大项目需求→运行中位约 50–60×、各源约 30–200×,不是「100× 以上」。
- **H01** Royce 所「相信的概念」是相邻步骤可迭代的阶段化,不是单趟;**H09** Bell & Thayer Fig.1 是其自家 MIL-STD 阶段图,不对应 Royce Fig.2;**H10** 改用期刊终稿措辞。
- **H21** Menzies 样本改用作者汇总表口径(团队中位 6、最多 36;工期中位约 61 天)。**H22**「延迟问题效应无独立证据」禁写:同文列 Stecklein/NASA、Reifer(19 家 CMMI-5)、Willis 同向测量。
- **C29** Zaninotto「8 文件 1,300 行」→ 实测 1,865 行;作者为 Marmelab 员工(提交邮箱 @marmelab.com),Kiro 例为 Marmelab 自家 Atomic CRM,均非独立现场样本。
- **C26/C27** Eberhardt「约十倍」按其自报数为 7.6×–12.1×;对照臂在 git 无重跑痕迹;C25 分步数字自相矛盾(Tasks 节误复制 Plan 节),仅四个总计可引。
- **C33** 「幽灵完成无发生率数据/反复遇到」推翻:工具 README 自报约 3/830(~0.36%),作者论证其罕见且静默。**C32** 「较温和评论者」注释推翻。
- **C18** Round 1「Hill 失真 Eberhardt」推翻:Eberhardt 自有小节标题「It didn't result in better code or fewer bugs」,Hill 仅夸大 buggy 程度。
- **C16** 「Grafana 排除 Spec Kit 目录」推翻:规则为 `.specs`,不匹配 `.specify/` 与 `specs/`。
- **P26/M23** 「Spec Kit Agents 无 SDD vs 无 spec 对照」推翻:Table 1 含完整 Spec Kit vs 直接实现,LLM 评审 3.51 vs 3.46(1–5),完成耗时 24.0 vs 14.4 分钟;+0.15 仅为有无 grounding hooks 之差,盲审人类反而偏好无 hooks 版(19:8,33 平);SWE-bench Lite +1.7pp 两侧均无 spec 工件,禁作 SDD 证据。
- **P31** 61.20% 是不确定性感知单代理脚手架,不是基线(无交互基线 54.80%,简单交互基线 70.4%)。**P29** 58% vs 59% 为同一论文摘要与引言自相矛盾,不是两个来源。**P24** PlanSearch 77.0/60.6/41.4 来自三个模型,同模型(Claude 3.5 Sonnet)pass@200 55.6→77.0。**P09** SCoT MBPP 最大增益 12.48%(表)非 12.31%(正文)。
- **F10/P21** nl2postcond「抓住约八分之一真实 bug」是 2 模型 × 2 提示 × 10 样本的并集上界(64/525=12.2%);最佳单配置 GPT-4 47/525(9%)且提示含 buggy code;仅自然语言约 1/15;博客所称「CodeLlama」实为 StarChat。**F13** FMCAD 工具只覆盖 64/153 条 spec,无一致性统计。
- **P27/M20** Google「+9.8pp」只在 detect@5(5 次任一检出)显著;单次 +4.2pp、p=0.31,token +38%。
- **F27** VerifyThisBench「XS 变体通过率略升」推翻(o3-mini 3.62%→2.24%);任务数论文自相矛盾。**F26** 模型为 GPT-4/Gemini-1.5-Pro/Claude-3-Opus,非 GPT-3.5 时代;摘要更严厉的口径为仅 21% 性质得到正确 PBT。**F28** Fonseca 16 bug:11 shim 层、3 验证工具、2 规约 → 「bug 集中在规约假设」推翻。**F01** 「205 条错误形式陈述」措辞推翻:205 含 10 条非形式源问题,真正不忠实的形式陈述 195/367(53.1%);同行评审摘要口径 204/367(56%)。**F21** 26.6% 与 8.6% 来自不同提示策略(FS 173/650 vs Progressive 56/650),不是同一聚合。**F20** 26% = 单一判官(gpt5.3-codex)判自写 spec 的 49/191。
- **A03** SO 2026 样本 30,903(169 国),非约 16,664。**A07/A01/A04** 「主要调查无 spec/规划题项」推翻:DORA 2025 Figure 21「Creating specifications 56%」「Analyzing requirements 49%」;SO 2026「写工单/需求/计划」27.8% 在用 AI、30.5% 不用也不打算;A04 是 68%「偏好」单 agent 而非 69%「使用」。A02 各数为同一题(n=31,877)切片,可互换算。
- **A27** 「#442 第二多」推翻(实为 #1213,66 👍);#1191 已于 2026-04-08 关闭(同日社区 Spec Refine 扩展上线)。**A25/A26** 非已完成弃用(#190 未合并而移除另行落地;ketcher #11517 仍开)。**A35** HN 评论者 yodon 立场被转述反了(本人喜欢 SpecKit)。**A33** Nadeem 被断章:plan mode「给 agent 的精确指令」用途过时,「帮人理解」用途更重要。
- **M30** arXiv 2608.25202 题名为「Spec-Driven Development as Prescribed and as Practiced」(作者含 Macvean),SpecMine 为其数据集名;5,992 是行数,去重 5,979 PR。
- **V18** Kiro 用量:原文「前 5 天 >10 万人试用」「自 preview 以来 >25 万」;「第一周」「前三个月」口径推翻,「3 亿次请求」一手找不到。**V19** 「spec 贵 1.8 倍」推翻:按官方超额价 spec $0.20 vs vibe $0.04 = 5×;且按 Kiro 定义,写 spec 文档计 vibe request,spec request 只计执行 tasks——两者非同一计量单位。**V34** 「Spec Kit 仍在 Assess」推翻:Radar Vol.35(2026-11)未收录 Spec Kit,OpenSpec 由 Assess 升 Trial,「AI-driven documentation sprawl」列 Caution。**V15** BMAD 全称(「Breakthrough Method of…」,仅见 CHANGELOG)与「名称为商标」推翻。**V22** $750M 估值在 TechCrunch 正文,非「文内更新/未披露」。
- **M26** Rebuild Dossier「hook 机械强制 spec」:作者 v4 勘误自承所发布 hook 在 2026-09-22 前从未生效,撤回 "mechanically enforced"。**M28** 「零缺陷上线」推翻为「约 30 个会话未观察到 bug」(作者自观察)。**M24** 论文主结论为结构化 spec 整体显著有益;「6 中 3 最优」比的是配置非模型,且最结构化配置仅 9/30 组合最优、「签名 + 自然语言」11/30。**M17** 退化作者归因于测试只认特定接口名(验证器假阴性),非「需求让 agent 更正确」的证据。**M21** 27/30 是段落形式 spec;清单形式 30/30,强基线 18/30;任务作者自建并刻意挑欠规约。**M22** 对最强基线(Claude Code)仅 +2–15pp;「13.17%」为 18 个对比的均值。**M19** Sonnet 单次运行、仅 Haiku 跑 3 次。**M33** 增益来自定位覆盖,补丁精度恒定(p=0.119),「SDD 有效成分是反馈环」推翻。**M03** 假设性 McNemar p≈0.031 推翻(真实配对 p=0.109–0.39)。

## 禁写清单(一手不可得或不承重)
- 厂商/二手数字:V30 原话、V18「3 亿次请求」、PKFARE「60×」不带下沿(用下沿为 30×)、A31 Rackspace「52 周→3 周」、A06 JetBrains「仅 13% 全 SDLC」、A07「+14 点」、M13 Medium token 数、M06「Kiro 最省钱」作效率证据(Kiro 成本 = credits × $0.04,其余臂按 API 价;Kiro token 比对照多 26%)。
- 学术:MapCoder「ChatGPT」行作独立复现(表注自承取自 Jiang et al.)、TiCoder「平均绝对提升 45.97%/45.73%/38.43%」(同文 Table IV 复算只有 33.50pp)、「15 名专业开发者,p<0.001」(含博士生)、HumanEvalComm 58%/59% 承重、Piskala「最多减少 50%」与 Marri 73%(n=1 项目)作 SDD 有效证据、Bissi 76%/88%、Kemerer 70/25/5、Snook & Harrison 结论(F31)、F30「评审负担增加」加引号、H05「1500 页」单引、H16「not important to its author」加引号、H15 第(1)句不注版本。
- 口径:Zaninotto「80% 时间在读」作测量、Wilson「十倍慢」作 Scott Logic 引语、「Most PRs predate agentic coding」(未测量)、AGENTbench「+20% 成本」作确定结论(#14 存档有 Lulla −28.64% 反向测量 → 方向存争)、METR「慢 19%」作现状(2026-02 更新:回访者 −18%、新招募 −4%,METR 自评受选择效应影响)、「Uvik ±10pp 噪声带由复跑测得」(50 次复跑 49 次一致)、「AWS 杰出工程师」(Brooker 自述 AWS 工程师)、「Kiro 登顶 HN」(仅 1,063 分可确认)、「EPAM/simonrowe 已弃用」、H31「27% 的项目在做 BDD」(只是框架存在,含 RSpec)。

## Round 2 新增的承重发现
1. **Hill 处理变量的系统性误判**(K/X/Q 三票独立复跑 master-prs.csv):连字符词误判 1,149–1,161 PR(≈4.8%)+ PR 模板占位 issue 号(ray `#1234` 993、vite `#123` 374、k8s `<kep-issue-number>` 317,另 litellm/pydantic/vllm 疑似)1,746–2,630 PR(7.2–10.8%),合计约 14%;集中于 5 个仓库,论文自述的模板过滤未拦住。偏向零效应。另:匹配估计无 CI,按 p 值反推缺陷约 [−1.4, +0.2]pp(相对约 9% 的缺陷下降无法排除),返工约 [−0.2, +1.2]pp(排除 >0.2pp 的返工收益)。勘误实有两条(第二条:1,015 个重分类 PR 仍留在 H3/H4,限定 spec'd 后 p=0.168/0.829,零结果不变);SSRN 版仍带未修正数字。
2. **Uvik 原始 CSV 获取并复算**(data/uvik-sdd-benchmark-2026-results.csv):配对 McNemar 最佳臂 OpenSpec 8:2 p=0.109,其余 0.27–0.39;数据完整性红旗——300 行 run_date 全为 2026-09-24(页面称运行 10-15、「Q4 2026」,若日期属实 5 人一天 217.7 工时)、Spec Kit 五类每类恰 8/10(p≈0.0025)、50 次复跑 49 次一致(推不出 ±10pp)、重跑工单首跑全合并;新增利益相关:Uvik 为 Claude Partner Network 成员、五臂均 claude-sonnet-5。
3. **唯一直接的「完整 SDD 流程 vs 直接实现」受控对照**(Spec Kit Agents Table 1):质量 3.51 vs 3.46(LLM 评审),耗时 24.0 vs 14.4 分钟——质量无差、时间 +67%。
4. **spec 漂移的独立证据**:CMU 2608.25202 访谈 14/21 报告 spec 与代码分叉(「Most participants reported that code and spec diverged」);Zampetti 2020 BDD 场景与代码仅约 37% 共演化、且 spec 变更同时或晚于代码;Hebig 2016 GitHub UML 文件 73.33% 从未更新;Petre/Hutchinson 的同步障碍。
5. **计划先行在论文内有干净消融**:MapCoder 去掉计划 agent HumanEval 80.0→70.0;但 InfoQ/Garg 小样本里 spec-first 92% 与 reason-first 95% 无显著差(n 很小),提示有效成分可能是「先想后写」而非文档本身。
6. **调查确有 spec 题项**:DORA 2025「Creating specifications」56%(做这项工作者中依赖 AI);SO 2026 写工单/需求/计划 27.8% 在用 AI。
7. **采用:装了≠用了**(G30 HOLDS,独立重抽样 13/200=6.5% 空模板);PyPI specify-cli 近 30 天约 8.4 万下载 vs 149k star;npm OpenSpec 422 万/30 天、BMAD 8.9 万;移除/新增 PR 比约 5%→17.8%。
8. **上游已发布研究的修订**(影响站内已发布 #14/#0):AGENTbench v3(2026-09,改名 CTXBENCH)结论软化为「不普遍提升」并补显著性(p=0.87/0.37),新增人写上下文文件优于 LLM 生成约 7%(p=0.038);METR 2026-02 更新。→ 已登记为独立修正任务,不在本期处理。

## 进入 Round 3 的单源承重实证(候选)
- R1 **Hill ESEM 2026**(唯一大样本 spec 工件 × 缺陷/返工观察研究;处理变量误判 ~14%、无 CI、事后选样、单作者)
- R2 **Uvik SDD benchmark**(唯一多臂 SDD 工具对照;数据完整性红旗、厂商利益)
- R3 **Spec Kit Agents Table 1**(唯一直接 SDD vs 直接实现;LLM 评审 vs 人类盲审方向相反)
- R4 **TiCoder 用户研究**(标题数字不可从同文表复现;均值为 1/25 倍数与 n=15 不符)
- R5 **ADOPT/SpecMine 活性与漂移测量**(spec 冻结率 76%、spec-code 共变 80.5%;本线自测 + 同组数据集与论文非独立)
- R6 **ProofNet-Verified / miniF2F-v2 错位率**(形式化端「陈述=意图」鸿沟的承重数字;205/204/195 多口径)
