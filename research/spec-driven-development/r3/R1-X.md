# R3 · R1-X 反证搜索席
靶子:Hill(ESEM 2026, LIPIcs 394 art. 84)「开源 PR 中的规格工件(实为 issue/ticket 引用)与缺陷、返工无关」——H1 匹配后 14.7% vs 15.2%(−0.6pp, p=0.133)、H2 作者内 +1.2pp / 匹配后 +0.5pp(p=0.146)、H3/H4 质量 p=0.164/0.860、H5 p=0.997(C01–C16、M29)。本席任务:找**独立团队 + 独立数据**对同一构念(PR/提交是否关联需求工件 × 缺陷/返工)的证实或矛盾测量。

今天复核了:
- Dagstuhl 正式版 PDF(drops.dagstuhl.de/…/LIPIcs.ESEM.2026.84.pdf,pdftotext)与作者仓库 esem-latex/main.tex、references.bib(raw.githubusercontent.com,main 分支)
- Rempel & Mäder, "Preventing Defects: The Impact of Requirements Traceability Completeness on Software Quality", IEEE TSE 43(8):777–797, DOI 10.1109/TSE.2016.2622264(OpenAlex 摘要全文)
- Pirouzkhah, Wurzel Gonçalves, Bacchelli, "The Value of Effective Pull Request Description", MSR 2026, arXiv 2602.14611(PDF 全文,Table 2/Table 4)
- Herbold et al., "Problems with SZZ and Features…", arXiv 1911.08938(EMSE,PDF 全文 §5.3)
- Mund, Femmer, Méndez Fernández, Eckhardt, ESEM 2015, arXiv 1702.07656(PDF 全文);Femmer et al., JSS 2017, arXiv 1611.08847(PDF 全文)——即 Hill 用来声称「前人发现效应弱、本研究在更大规模上证实」的两篇
- Khatib, Mathews, Nagappan, Nie, Zimmermann, "What Makes a Good Bug Report for an AI Agent?", arXiv 2607.07593(arXiv API 摘要)
- Agarwal et al., arXiv 2608.25202(SpecMine,摘要);Alenezi arXiv 2607.16680(摘要);Yoshioka et al. arXiv 2601.18749、Mazloomzadeh et al. arXiv 2607.21832(AIDev 研究,摘要)
- brennhill/delivery-gap-research issues 页(唯一 issue #1);github/spec-kit issue #3357 与 Discussion #3373
- WebSearch:critique / response / replication / reanalysis 多组查询

没拿到:
- Rempel & Mäder 全文(IEEE Xplore 418、ResearchGate/db-thueringen 不可达)——效应量(IRR)、项目选样细节未核,只用摘要口径
- Bird et al. FSE 2009 原文(只见 Nguyen/Adams/Hassan WCRE 2010 的二手转述)
- OpenAlex 被引列表、Semantic Scholar 引用检索(两 API 当日配额耗尽 429);OpenAlex 单条查询显示 Hill 论文 cited_by_count=0(当日快照)
- GitHub API 对作者仓库的 forks/提交历史(会话权限拒绝);只读了 HTML issues 页
- Zenodo 复现包记录(未尝试,Round 2 已记 API 无返回)

## 一、发现

**F1 无独立复现、复跑或批评。** 多组 WebSearch(标题全名;"Hill" + critique/response/reanalysis/replication;"spec-driven development" + empirical/defects/replication 2026,extended 模式)只返回论文本身、SSRN 版、二手博客转述与 Uvik benchmark。OpenAlex 记录 W7220422325 cited_by_count=0。作者仓库 issues 页仅 1 个 issue(#1,Sandy4321,2026-07-05,问「Co-authored-by: Copilot 是否意味着使用了 Spec Kit」),非复跑。

**F2 厂商未回应以数据。** github/spec-kit issue #3357(同一用户,2026-07-05,标题「[Bug]: Brenn Hill paper claimed that spec kit is not useful」)次日被锁定并由维护者 mnriem 转为 Discussion #3373;该 Discussion「Replies: 0 comments」「1 participant」。即:利益相关方没有发布任何反证数据。这不是证实,只是「无人反驳」。

**F3 最接近构念的独立测量方向相反,且 Hill 未引用。** Rempel & Mäder(TSE 2017,独立团队 TU Ilmenau,24 个中大型开源项目,多层 Poisson 回归)摘要原文:"We found that the degree of traceability completeness for three of the studied activities significantly affects software quality, which we quantified as defect rate. Our results provide for the first time empirical evidence that more complete traceability decreases the expected defect rate in the developed software."
- 构念对照:Rempel 的处理变量是**项目级**「需求→代码追踪链接完整度」(四类活动),Hill 是 **PR 级**「是否带 issue/ticket 引用」。二者都在测「代码变更是否挂在需求工件上」,是现有文献里最接近 H1 的独立测量。
- 不同处:Rempel 是 n=24 的项目级(生态型)比较,未做任务难度/适应证混杂的 PR 内控制;Hill 的核心论点恰是原始关联被适应证混杂主导——两者结论矛盾可由分析层级不同解释,不能直接判谁对。
- 引用检查:main.tex 与 references.bib 中 "rempel" / "traceab" 命中 0;正式版 PDF 同样 0。Hill 的「Requirements Engineering and Defect Prevention」节(正式版 p.84:3,第 96–98 行)未讨论这一反向证据。
- 效应量未核(全文未拿到);搜索片段中出现的 2.3%/10.3% 无法归属,**不得引用**。

**F4 Hill 用来铺垫「前人也只见弱效应」的两篇引文不测代码缺陷。** 正式版 p.84:3:"Mund et al. [15] found only weak evidence across two studies, and Femmer et al. [10] found that the relationship between requirements smells and downstream defects was context-dependent. Our study confirms this pattern at larger scale."
- Mund 2015(1702.07656):研究一为问卷(SRS 使用情况,Kendall τ 相关),研究二为学生受控实验,结局是**系统测试用例质量**而非代码缺陷;实验结论原文 "we conclude that, to a large extent, defects can propagate through the engineering process, even when people are briefed about the correct requirements"——即语义类 SRS 缺陷**确实**向下游传播,「only weak evidence」是选择性概括。
- Femmer 2017(1611.08847):评估需求坏味检测的精度/召回(摘要:precision 59%、recall 82%),全文无「下游缺陷」测量(grep "downstream" 0 命中);"context-specific" 指的是坏味的相关性判断。
- 含义:「本研究在更大规模上证实了既有模式」没有独立前序测量作支撑;Hill 的零结果在文献中是**孤立**的,不是对既有共识的复现。

**F5 独立证实 Hill 的「适应证混杂」机制的一半,另一半方向不一。** Pirouzkhah et al.(MSR 2026,独立团队 UZH,80K PR / 156 项目)Table 4「Link to Related Issue(s)」的提交时预测因子:正向 "PR includes test (1.29)"、"# of open PRs in project (1.24)"、"Project age (1.22)";负向 "Diff size (0.93)"、"Contrib's daily workload (0.97)"、"# of contrib's previous PRs (0.99)"。摘要:"PR descriptions are also more common in mature projects and complex changes, suggesting they are written when most useful rather than as a formality."
- 与 Hill 一致:写描述/挂 issue 不是随机的,与变更性质和作者经验相关(Hill:spec'd 作者先前提交中位数 64 vs 116;Pirouzkhah:先前 PR 数为负向预测,OR 0.99,幅度很小)。
- 与 Hill 不一致:Pirouzkhah 的 Link 元素与**diff 大小负相关**(OR 0.93),而 Hill 报 spec'd PR 新增行数 1.8×。「挂 issue 的是更大的活」在独立数据上不成立;整体描述(Purpose)才随 diff 增大(OR 1.41)。即「开发者给最难的活写 spec」的机制在 issue 链接这一具体工件上不是普遍规律,Hill 的 1.8× 可能部分来自其 spec'd 判定混入的模板/描述段与仓库构成。
- 结局变量:Pirouzkhah Table 2 中 Link 对合并决定(controlled OR 1.091,未标显著)、PR 重开(controlled OR 0.958,未标显著)均无可检效应——与 Hill 的「零」方向一致,但这是评审结局,**不是缺陷/返工**,只能算邻近旁证。

**F6 独立证实 Hill 处理变量的噪声通道(Round 2 发现的模板占位符/裸 #N 问题)。** Herbold et al.(1911.08938 §5.3,38 个 Apache 项目):"the broken links are due to links to pull requests on Github, which have the pattern #<NUMBER>… links to pull requests were the most frequent reason for additional links in general. Commonly used numbers were also problematic"。Hill 的 spec'd 判定中 #N 触发 11,348 例(Round 1 C02 复跑),是同类启发式。独立文献证明「#N = issue 引用」在开源仓库里系统性产生假链接——支持 Round 2「误判约 14%、偏向零」的判断,并说明误判不止于模板占位符,还包括指向其他 PR 的 #N(本席未在 master-prs.csv 上量化这一子通道)。

**F7 agent 侧的独立测量测的是另一个结局,不能用来反驳或证实 Hill。** Khatib et al.(2607.07593,Waterloo/MSR,433 个 SWE-bench Verified issue × 87 个修复 agent + SWE-bench Pro 消融):"fix suggestions, reproduction scripts, repository source code, and localization info are associated with higher resolution likelihood, while longer reports are associated with lower odds… some qualities long emphasized for human readers… contribute little or even correlate with lower success." 这说明**issue 内容的特定成分**影响 agent 解题率(T1 规格的「内容」效应),与 Hill H3/H4「LLM 打分的形式完整度不预测缺陷」不冲突,甚至互补:形式完整 ≠ 有用成分。但结局为基准解题率、非合并后缺陷,不是独立复现。AIDev 系列(2601.18749、2607.21832)摘要未见以 issue 链接/规格为处理变量的缺陷分析。

**F8 SDD 工具本身的独立外部数据仍无缺陷测量。** SpecMine(2608.25202,CMU,独立)只有访谈自报("reported more reliable agent behavior alongside greater planning and review costs"),无缺陷/返工测量;Alenezi(2607.16680)的「73% security defect reduction」是转引 Marri(Hill 已指出单项目、同一开发者先后实现)。Uvik benchmark(R2 靶子,厂商口径)与 Spec Kit Agents(R3 靶子)测的是 agent 基准上的工具工作流,与 Hill 的 OSS PR 观察构念不同,不构成对同一结论的独立证实或矛盾。

## 二、结局

**无独立测量**(针对 Hill 的同一构念:PR 级 issue/ticket 引用 × SZZ 缺陷 / 关键词返工)。邻近构念上有一项**独立矛盾**(Rempel & Mäder 2017:项目级需求追踪完整度 ↔ 更低缺陷率,Hill 未引用),一项**部分独立证实**(Pirouzkhah 2026:issue 链接与评审结局无可检效应、写描述非随机;但 issue 链接与 diff 大小负相关,与 Hill 的 1.8× 机制不一致),一项**测量噪声的独立证实**(Herbold:#N 假链接)。

| 角度 | 查询/来源 | 结果 |
|---|---|---|
| 直接复现/复跑 Hill 数据 | WebSearch 标题全名 + replication/reanalysis;作者仓库 issues;OpenAlex 被引 | 无;仓库 1 个非复跑 issue;cited_by=0 |
| 学术批评/评论 | WebSearch "Hill" + critique/response;"delivery gap" | 无;仅博客转述 |
| 厂商反驳 | github/spec-kit #3357 → Discussion #3373 | 被锁并转讨论,0 回复,无数据 |
| 同构念独立测量:需求追踪 ↔ 缺陷 | Rempel & Mäder TSE 2017(OpenAlex 摘要) | **矛盾**:追踪越完整缺陷率越低(24 项目,项目级);全文与效应量未拿到;Hill 未引用 |
| PR 级 issue 链接 ↔ 缺陷(GitHub) | WebSearch "linked issue" / "linked to issues" defect / bug-introducing 多组 | 未找到任何以 PR/提交是否挂 issue 为处理变量、缺陷为结局的独立研究 |
| PR 描述/issue 链接 ↔ 评审结局 | Pirouzkhah MSR 2026(全文 Table 2/4) | 部分证实:Link 对合并、重开无可检效应;写描述随复杂度/成熟度;Link 与 diff 大小负相关(与 Hill 1.8× 不一致) |
| 处理变量测量效度 | Herbold 1911.08938 §5.3;Bird 2009(二手) | 证实噪声:#N 常为指向 PR 的假链接;链接样本有偏(Bird 细节未核) |
| 需求质量 ↔ 下游缺陷(Hill 的文献铺垫) | Mund 2015、Femmer 2017 全文 | 两篇均不测代码缺陷;Mund 实验结论是 SRS 缺陷「to a large extent」向下游传播——Hill 的「only weak evidence」概括失真 |
| 需求质量研究综述 | WebSearch Frattini 2023/2024 | 综述称该领域多未连结到下游活动影响;无可用效应量 |
| agent 侧 issue 内容 ↔ 解题 | Khatib et al. 2607.07593 | 结局不同(基准解题率);显示特定内容成分有效、篇幅负相关;不复现也不反驳 Hill |
| AIDev agent PR 研究 | 2601.18749、2607.21832、2602.09185 等摘要 | 未见以规格/issue 链接为处理变量的缺陷分析 |
| SDD 工具实际使用的结局 | SpecMine 2608.25202;Alenezi 2607.16680 | 仅访谈自报或转引单项目 73%;无独立缺陷测量 |
| 引用图谱(被引/施引) | OpenAlex works / Semantic Scholar API | 429 配额耗尽,未完成;仅单条记录 cited_by=0 |

成文建议(供汇总):
- Hill 的零结果须写作「**单源**、无独立复现」;不得写「与既有研究一致」——Hill 的文献铺垫(Mund/Femmer)不测代码缺陷,而最接近的独立测量(Rempel & Mäder)方向相反。
- 可写:「另一项独立研究(24 个开源项目、项目级)发现需求追踪越完整缺陷率越低,与 Hill 的 PR 级零结果方向相反;两者分析层级与混杂控制不同,无法直接裁决」→ 分级:**方向存争**(对「需求工件挂钩 ↔ 缺陷」这一更宽命题)。
- 对 Hill 的窄命题(119 个 OSS 仓库内 PR 级工单引用与缺陷/返工无关),本席无独立证据可升级或降级,维持 **单源已核**(其分析是否承重由 M 席决定)。
- 「适应证混杂」机制:可引 Pirouzkhah 说明「写描述/挂 issue 非随机」,但不得用其支持「挂 issue 的是更大的活」(独立数据为负相关)。
