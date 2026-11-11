# ADOPT 线 · 采用与实践现场(Round 1)

> 35 条论断(A01–A35)。本会话网络只放行 GitHub API / raw / git clone 与包仓库;survey.stackoverflow.co、stackoverflow.blog、jetbrains、dora/services.google.com、github.blog、thoughtworks、arxiv、HN/algolia、各博客均 403。**因此调查与话语场条目全部是 `secondhand`(WebSearch 摘要),GitHub 侧普查是本线一手自测(verbatim-checked,可复跑)。**测量日 2026-11-11 UTC。

## 1. 开发者调查:没有一个大调查问过"spec/plan-first"
- **阴性结论(需一手复核)**:SO 2025/2026、JetBrains 2025、DORA 2025、Octoverse 2025 的可得摘要里都没有 spec-driven / plan-first 题项(A01–A08)。叙事里的"SDD 已成主流"没有调查数字撑腰。
- 唯一沾边的题项方向相反:SO 2025(n=49,009)中 **69% 不打算用 AI 做项目规划**(A01)。这是"让 AI 规划",不是"人写 spec 给 agent",不可互换。
- agent 使用本身口径混乱:SO 2025 同一调查有 31% 在用 / 23% 至少每周 / 52% 不用或只用简单工具三种说法(A02);2026 主调查"AI agents or automated workflows"26.2% vs 4 月脉冲调查 59%(A03/A04)。2026 主调查样本量摘要报约 16,664,较 2025 骤降,待核。
- DORA 2025 的 7 项能力里有"小批量工作"(A07)——与"大块前置 spec"在方向上相反(本线推论,不是报告结论)。
- 调查方利益:JetBrains、Google Cloud(DORA)、GitHub 都卖 AI 编码工具,标【厂商】。

## 2. GitHub 普查:装了多少、用了多少(计文件 vs 计项目)
可复跑查询(遗留 REST code search,默认分支、非 fork、公开仓;total_count 为估计值):

| 查询 | total_count(文件) | 前 100 条的不同仓数 |
|---|---:|---:|
| `filename:constitution.md path:.specify/memory`(spec-kit) | 14,176 | 100 |
| `filename:requirements.md path:.kiro/specs`(Kiro) | 38,336 | 76 |
| `filename:design.md path:.kiro/specs` | 41,408 | 76 |
| `filename:project.md path:openspec`(OpenSpec) | 2,368 | 100 |
| `path:.bmad-core`(BMAD) | 3,680 | **16** |
| `filename:tessl.json` | 285 | 84 |
| 对照 `filename:AGENTS.md` / `CLAUDE.md` / `.cursorrules` | 1,247,232 / 1,028,096 / 30,976 | — |

- **口径陷阱**:`path:.kiro filename:tasks.md` 也返回 38,336,与 requirements.md 完全相同 → total_count 疑似分桶,**只能当数量级**(A11)。Kiro/BMAD 文件数≫项目数。
- **项目级交叉**:SpecMine v1.0(CMU,2026-07 快照)全量普查 **470,795 个 spec / 73,030 仓**(17 个工具/路径桶),Kiro **98,574 工件 / 12,910 仓**(A14)。与代码搜索推算的 Kiro 约 1 万仓同量级。语料长尾:仅 1.3% 仓 ≥100 star,92% spec 首提交于 2026(A15)。
- **star ≠ 安装**:spec-kit 149,227 star vs ~14k 个 constitution,约 10:1(A16)。topic `spec-driven-development` 2,949 仓且逐季翻倍(A28),但这是造工具的供给侧。
- 规模感:spec-kit 足迹约为 AGENTS.md 文件数的 1.1%(A13)——"给 agent 写上下文文件"远比"走 SDD 流程"普遍。

## 3. 装了 ≠ 用了 ≠ 保持活性(本线克隆样本 + SpecMine 样本)
- 100 个 constitution.md 抓原文:**8% 仍是未填写模板**(A17)。
- 克隆 60 个 spec-kit 仓:**28% 有 .specify/ 但 0 个功能 spec**;中位 2 个功能 spec;Kiro 中位 4,OpenSpec 中位 40 个 md(A18)。
- 活性(A19):工具加入后触及 spec 目录的提交中位占比 spec-kit 7.4% / Kiro 11.6% / OpenSpec 20%;"spec 冻结而代码继续 ≥20 次提交且 ≥60 天"占 18% / 15% / 5%;近 3 个月零提交的仓 27% / 57% / 50%(大量是一次性试用仓)。
- SpecMine 样本(按 star 精选,**作者明言不可估总体**):创建后从未修改的 spec 文件 speckit 76%、openspec 84%、living 角色 51%(A20);触及 spec 的 PR 中 80.5% 同时改代码(A21)。
- **解读警告**:"冻结"≠漂移。spec-first(用完即弃)用法下冻结是预期行为;要判漂移须看 spec 内容与代码是否一致——这一层只有 Agarwal et al.(A29,二手)触及:多数受访者报告分歧,实现细节越多越早腐坏。

## 4. 弃用信号
- 标题 `"remove spec kit"` 的 PR 共 158 条;月度 0(2025-09)→34(2026-10),同期 `"add spec kit"` 43→192,**移除/新增比约 5%→18%**(A22)。绝对量小、严重低估(多数移除不用此标题),且有批量尖峰(AstralDeep 一天 5 仓)。
- 其他:`remove speckit` 134、`remove kiro` 258(多为撤 CLI/IDE/认证问题,非弃 spec,A23)、`remove openspec` 606、`remove bmad` 133。
- **最有信息量的逐字理由**:
  - NetPace #317:"a reviewed, confirmed issue *is* the specification … were carrying cost without carrying work."(A24)
  - simonrowe #190:"still installed 71 tracked files and injected 23 `speckit*` skills/commands into every agent session."(A25,上下文税)
  - EPAM ketcher #11517:未使用的 OpenSpec 引用会误导 agent(A26)。
- **模式**:弃的是 T2 流程脚手架,留的是 T1(issue 验收标准)与 constitution 规则——弃用≠"spec 无用"。
- spec-kit 官方仓 reactions 第一的 issue(#1191,105 👍)就是"无法迭代更新既有 spec / 保持同步"(A27),主张 2(spec 活性)是工具自身头号痛点。

## 5. 企业案例:只有厂商与自述
- AWS/Kiro:PKFARE 5 周 10 万行上线、LMU 半天、Socure 2 天 vs 3 周(二手)——无基线、无对照(A31)。**Rackspace"52 周→3 周、+90%"未能定位一手,按疑似夸大处理,不得引用。**
- Asana 内部(7 人、524 PR、4 个月,前后对比):PR/周 +38%,revert 1.2% vs 1.66%(A30)——无对照、无推断统计,PR 数≠质量。
- **独立、带对照的企业报告:未找到**(A32)。

## 6. 2026 话语场(【媒体】,全部二手,引语未逐字核)
- 质疑:Zaninotto(Marmelab)"Waterfall Strikes Back";Kent Beck"Earn *And* Learn"(SDD 预设"终点线游戏");Ayman Nadeem"Plan mode is dead"(自家产品转向,有利益)。
- 辩护:Marc Brooker(**AWS,Kiro 出品方**)"isn't Waterfall:不是把设计提前,而是把设计提升";Roger Wong;Utsab Pant(过期 spec 比无 spec 更糟)。
- Thoughtworks Radar:SDD、Spec Kit、OpenSpec 均停留 **Assess**(A09)。
- HN 原帖不可达,具名作者缺失(A35)——验证阶段需补。

## 最强 / 最弱证据
- **最强**:A14(SpecMine 项目级普查,学术方,README 逐字)、A10/A18(可复跑 GitHub 普查与克隆样本,安装 vs 使用落差)、A24/A25(弃用理由逐字一手)。
- **最弱**:A31 Rackspace 数字(无一手)、A06 JetBrains AI Pulse(单个二手摘要)、A35 HN 转述(无原帖无作者)。

## 交叉口径要点(详见 JSON)
文件≠项目;total_count 分桶;安装≠使用≠效果;冻结≠漂移;SpecMine 样本不可估总体;调查"AI 做规划"≠"人写 spec";移除计数低估且非同质;厂商案例无基线;Agarwal et al. 与 SpecMine 同组非独立。
