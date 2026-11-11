# R3 · R5-X 反证搜索席

靶子:spec 的活性、冻结和漂移测量(G30/G29 的 A17–A21、A29、M30,G21 的 M08)。核心承重数字有:spec 单提交率,即「spec 冻结率 76%」(A20,SpecMine 样本 speckit 76.4% / openspec 84.1%);spec 与代码同 PR 共变 80.5%(A21);本线自测中,装了 spec-kit 但没有功能 spec 的比例 28%,「spec 冻结、代码继续」18%(A18/A19);constitution 空模板 8/100(A17);CMU 访谈中多数人报告 spec 与代码分叉(A29);Uvik 合并代码与自身 spec 不符 7.9%(M08)。

今天复核了:
- arXiv 2608.25202(HTML 版,题为 "Spec-Driven Development as Prescribed and as Practiced")的 Finding 4、Finding 10、附录代码表和 Table(PR 层)
- arXiv 2610.07534v1 EPIC(VCU/OSU/CodeDay)全文 §3.1.2、§4.2.2
- arXiv 2511.12884v2 Agent READMEs(Kasetsart/NAIST/Queen's)PDF §4.2
- arXiv 2510.21413v4(Mohsenimofidi 等,MSR '26)§4.3
- arXiv 2606.15828v5(Santos 等,Configuration Smells)§V-C、§VI-E
- arXiv 2606.30689v1(Citation Discipline in SDD)PDF 方法节
- **本席独立再抽样**:GitHub code search `filename:constitution.md path:.specify/memory` 第 301–500 名,去重后 197 个仓库,与 A18 的 60 仓重合 0 个。全部 treeless clone 后用 git 复测(脚本见 scratchpad `r5x-scripts/m.sh`,原始输出 `r5x/out.tsv`)

没拿到:
- Hebig 等 MODELS 2016 的原文和作者幻灯片(rostock 镜像连接被重置),「73.33% UML 文件从未更新」只来自检索摘要
- Zampetti 2020 IST 全文,37% 只来自摘要
- Uvik 之外任何「合并代码 vs 自身 spec」一致性的独立测量(没搜到)
- 未读另一席的 R5 文件

## 一、发现

**X1 来源谱系:承重数字只有一条数据血统,没有第二个独立来源。**
- A20 的 76.4%/84.1% 来自 SpecMine 500 仓样本。
- 2608.25202 自己写「81.5% of spec files have a single recorded commit」(§Finding 4,基于从 SpecMine 抽的 266 仓)。
- PR 层写「81.2%」也「modify code in the same PR」(语料汇总表)。A21 是 80.5%。
- 这三组数字出自**同一团队(Agarwal/Vasilescu 等)、同一语料**。2608.25202 不能当作 A20/A21 的独立证实,只是同源的两种切法。
- A17–A19 是本线自测,只有一个团队、一次 best-match 抽样。M08 是厂商自测。

**X2 本席独立再抽样(换了数据,团队仍是本研究,所以不是独立团队)。** 样本是 code search 第 301–500 名的 197 个 spec-kit 仓库,2026-11-11 测量。

| 指标 | 原值(A18/A19/A20/A21) | 本席复测 | 判断 |
|---|---|---|---|
| 装了 `.specify` 但 `specs/*/spec.md` 为 0 | 17/60 = 28% | 34/197 = **17.3%** | 同向,幅度偏低 |
| 每仓功能 spec 数中位 | 2 | **1** | 同向 |
| spec.md 单提交率(按当前路径,`git rev-list --count HEAD -- f`) | SpecMine speckit 76.4% | 620/911 = **68.1%**;按仓聚类 bootstrap 95% CI [59.0%, 76.3%];仓内中位 100% | 同向;76% 落在 CI 上沿 |
| 「spec 冻结」(最后改 spec 后 ≥20 次非合并提交,且距仓库最后提交 ≥60 天) | 11/60 = 18.3% | 11/197 = **5.6%** | **数字不稳** |
| 替代口径:近 90 天仍活跃的仓中,spec 停更 ≥60 天 | (原样本复算 13/34 = 38%) | 19/78 = **24%** | 量级随口径变化大 |
| 近 90 天无提交(截止 2026-08-13) | 27% | 111/197 = **56%** | 样本越靠后越「死」 |
| 触及 `specs/` 的提交中,同时改了工具目录以外非 .md 文件的比例 | PR 层 80.5%(A21) | 提交层合并 2558/4159 = **61.5%**;仓中位 71% | 同向;提交层天然低于 PR 层,不可直接比 |

结论:
- 「多数 spec 写完不再改」「spec 提交多数与代码共变」两个方向在另一批样本上复现。
- **「spec 冻结 18%」不稳**。同一定义在另一批样本得 5.6%,换口径得 24–38%。原因是这个指标同时受仓库是否还活跃(≥20 次后续提交的门槛)影响,不宜承重。
- 28% 的空 spec 率在更深排名降到 17%,应写成区间「约 1/6–1/4」。

**X3 独立团队、独立数据的参照系:其他「写给 agent 或设计用」的工件。** 这些不是同一构念,只能作参照,不能当证实。
- Chatlatanagulchai 等(2511.12884v2 §4.2.3),2,303 个文件 / 1,925 仓,≥5 star:「a majority of Claude Code context files (67.0%) are modified in multiple commits」,Copilot 59.8%,Codex 59.4%。换算单提交率约 33–41%。
- Mohsenimofidi 等(MSR '26,2510.21413v4 §4.3):「155 AGENTS.md files … 77 (50%) of them had not been changed」。
- Santos 等(2606.15828v5 §VI-E):100 个热门 AGENTS.md 中 24 个只有一次提交(作者称这是 "Init Fossilization"),且这些项目并非休眠。
- Hebig 等 2016 GitHub UML:「73.33% UML files never updated」。这是二手材料,未回一手。
- 读法:SDD spec 的单提交率(68–84%)明显高于 agent 上下文文件(24–50%),和 UML 模型(约 73%)接近。这和「spec 是写一次的功能工件,而不是活文档」的解读同向。但 OpenSpec 的 archived 文件按流程设计就不再改,单提交率高部分源于工件角色。2608.25202 自己给出的分角色数据:OpenSpec capability spec 单提交 47.4%,archived change 95.4%。

**X4 独立团队的 SDD 仓库挖掘没有测活性。**
- EPIC(Claudino、Sarma、Damevski、Feng 等,2610.07534v1)独立挖掘了 114 个 SDD 仓(code search 2026-04-25,850 → 206 → 114)。
- 它只评 spec 质量与结果的关联(顶档 bug-fix 提交占 11.8%,底档 20.4%),全文没有 spec 修改次数、停更或共变的测量。grep "drift/stale/outdated/updated" 只命中背景段。
- 这是目前唯一独立于 CMU 的 SDD 仓库样本,但对 R5 只能记为「独立团队存在,未测此量」。

**X5 A29 访谈计数逐字核到,但同团队。**
- 附录代码表 "challenge: spec-code drift" 列出 P2、P5、P6、P7、P8、P10、P11、P12、P13、P14、P16、P18、P19、P21,共 **14/21**。
- 其中 "agent deviates during implementation" 8 人,"spec goes stale as code evolves" 7 人。
- Finding 10 原文:「Most participants reported that code and spec diverged, in two ways」;「Spec decay affects living specs」。
- 访谈数据和仓库数据来源不同,但作者与 SpecMine 相同。没找到独立团队的 SDD 访谈对 drift 的计数。EPIC 有 N=15 访谈,但未报告 drift 计数。

**X6 M08(Uvik 7.9%)没有独立测量。** 邻近构念都不可比:
- (a) 2608.25202 访谈中 implementation drift 8/21,定性。
- (b) Wang、Pradel、Liu(ICSE 2026,2503.15223):29.6% 的 plausible patch 与 oracle patch 行为不同。比较对象是参考补丁,不是 spec。
- (c) Constraint Decay(2605.06445):最强配置在全约束下 Pass@1 只有 8.3%,用测试判定。
- (d) Citation Discipline(2606.30689):TDR 测的是**人为注入**的幻觉检出率(§方法:「hallucinations deliberately injected」),不是自然发生率。单作者,作者即 traceSDD 提出者,有利益关联。
- (e) agent PR 描述与代码不一致中 "phantom changes" 占 45.4%(2601.04886),是描述 vs 代码,不是 spec vs 代码。

所以 7.9% 只能维持「厂商口径·单时点」。邻近测量普遍高得多,但构念不同,不构成矛盾,只提示 7.9% 依赖 Uvik 的判定口径(第二评审人工比对,且只看已合并工单)。

**X7 A17 空模板。**
- Round 2 X 已独立重抽 101–300 名:13/200。合计约 7%(21/300)。
- 2608.25202 的说法是「Half of Spec Kit's specs/ files keep the literal (mandatory) annotation」。这针对 spec.md 里的脚手架标注,不是 constitution 占位符,且同团队,不能合并引用。
- 本席未再测 constitution。

## 二、结局

**X 席:无独立测量。** SDD 专属的活性、冻结、漂移数字全部来自单一血统:SpecMine 和 2608.25202 是同一团队、同一语料;A17–A19 是本线自测;M08 是厂商。独立团队、独立数据只能提供**异构工件的同向参照**:agent 上下文文件单提交 24–50%,UML 约 73%,BDD 共演化约 37%,文档过时引用 28.9%。本席换样本复测后,两个方向成立(单提交 68% [59, 76],共变 61.5%,提交层);但「spec 冻结 18%」不稳,同定义得 5.6%,换口径得 24–38%。

| 角度 | 查询/来源 | 结果 |
|---|---|---|
| 独立团队的 SDD 仓库挖掘 | WebSearch「empirical study spec-driven development GitHub mining Kiro spec-kit」;EPIC 2610.07534v1 全文 | 有独立样本(114 仓),**未测**活性/冻结/共变 |
| 同团队论文自报数字 | 2608.25202 HTML:81.5% 单提交、81.2% 同 PR 改代码、OpenSpec 分角色 47.4%/84.2%/95.4% | 与 A20/A21 同向,**非独立**(同语料) |
| 换样本复测(本席) | code search 301–500 名,197 仓,git 复测 | 方向同向;冻结率不稳;空 spec 率 17% vs 28% |
| agent 上下文文件维护(独立团队) | 2511.12884v2、2510.21413v4、2606.15828v5 | 单提交 33–41% / 50% / 24%:spec 比上下文文件更「写一次」;异构参照 |
| 传统设计/规格工件 | Hebig 2016 UML(二手 73.33%);Zampetti 2020 BDD(摘要约 37% 共演化,spec 变更同时或晚于代码) | 同向参照,未回一手 |
| 文档过时 | Tan、Wagner、Treude EMSE 2024:28.9% 热门项目当前含过时引用,82.3% 历史上曾有 | 同向参照,构念不同 |
| spec 漂移专项测量 | WebSearch「spec drift / specification drift coding agents measurement spec-kit OpenSpec Kiro」 | **没搜到**;只有提案(Spec Growth Engine)和 goal-drift 类基准 |
| AIDev 等 agent PR 数据集中的 spec/文档共变 | WebSearch「AIDev documentation changes co-change」 | **没搜到**对口研究(只有 docs PR 作者比较、测试共变 DiD) |
| 合并代码 vs spec 一致率(对 M08) | Citation Discipline 2606.30689;SWE-bench PatchDiff 2503.15223;Constraint Decay 2605.06445;PR 描述不一致 2601.04886;WebSearch「scope creep agent PR percentage」 | **无可比独立测量**;邻近构念 8–45% 不可比;2606.30689 为注入实验且作者有利益关联 |
| 独立访谈中的 drift 计数(对 A29) | EPIC N=15 访谈全文 grep | 未报告 drift 计数;14/21 仅 CMU 一家 |
| constitution 空模板(对 A17) | Round 2 X 101–300 名复测;2608.25202「(mandatory) annotation」 | 前者同向(6.5%);后者构念不同、同团队 |

成文建议:
- 「spec 冻结率 76%」改写为:「SpecMine(CMU 同一团队的数据集与论文)显示约 3/4–4/5 的 spec 文件只有一次提交;本期换样本复测得 68%(95% CI 59–76%)」,分级「单源已核 + 现场核验(同向)」。
- 加一句参照系:agent 上下文文件只有约 1/4–1/2 是一次写成(三个独立团队),spec 更像一次性功能工件。
- 「spec 冻结 18%」不承重。
- M08 维持厂商口径,写明「无独立测量」。
- A29 写「CMU 访谈 14/21」,并注明与 SpecMine 同一团队。
