# CON 线:反方一手证据与对照实测(#25 spec-driven development)

> 35 条论断(C01–C35),见 `CON.json`。运行环境限制:drops.dagstuhl.de、arxiv.org、martinfowler.com 被会话网络策略拦截(curl CONNECT 403 / WebFetch ENOTFOUND)。替代路径:从 GitHub 拿作者的源仓库、博客源码仓库和独立网页剪藏,能核的数字都对照 git 历史或公开数据复跑。仍只有二手来源的条目(C34 Garg、C35 Instil)已降为 `secondhand`。

## 1. Hill(ESEM 2026)——唯一的大样本反证,也是单源承重候选

**来源路径**:作者公开仓库 `brennhill/delivery-gap-research`(commit a23d38a, 2026-07-27):camera-ready LaTeX `esem-latex/main.tex`、SSRN 预印本 PDF、`REVISION-PLAN.md`、`CORRECTIONS.md`、复现数据(CC-BY 4.0,Zenodo 10.5281/zenodo.19415187)。第三方读已发表 PDF 的转述(mattbutlerengineering/ai-tooling PR#731)与 tex 里的数字一致。

**设计**
- 观察性研究。119 个开源仓库,88,052 个非 bot 的已合并 PR(原始 100,247,剔除 bot 12,195),17 种语言,时间窗约 2025-04 至 2026-04。
- 5 条假设直接从 Spec Kit、Kiro、Copilot Academy 的宣传语推出。
- 估计方法分三层:混合比较、逻辑回归(规模控制 + 仓库 FE)、作者内 LPM(按作者聚类 SE)。另做 12 项稳健性检验,其中 PSM 是主估计。
- **缺陷** = 基本 SZZ(仅覆盖 103 个仓库,误归因率 46–71%)。
- **返工** = 30 天内出现文件重叠、且标题含 fix/revert 等关键词的后续 PR。
- **质量** = Claude Haiku 按 7 维量表打分。人工校验仅 38 例,ρ=0.42;其中「验收标准」维度 ρ=0.17。

**结果**:5 条假设全部不成立。
- H1:匹配后 −0.6pp,p=0.133(17,375 对)。
- H2:作者内 +1.2pp(p=0.001,方向是返工更多);匹配后 +0.5pp(p=0.146)。
- H3/H4:p=0.164 / 0.860。
- H5:交互项 p=0.997。
- 未调整时的正向关联(缺陷 OR 1.20)被解释为适应证混杂:人们给难活写 spec。

**最大的口径陷阱(成文必须照搬作者原话)**
1. 处理变量 97.5% 是 issue/ticket 引用。结构化需求段只有 24 个 PR。样本里**没有任何仓库提交过 SDD 工具产出**,作者原话是「SDD tool adoption itself remains untested」。所以只能写「开源 PR 中的规格工件与缺陷/返工无关」,**不能写「SDD 不降缺陷」**。
2. Grafana、Airflow、Spark 的 .gitignore 主动排除 `.specs` / `.kiro/`(C17,现场核验)。工具产出被刻意留在版本库之外,任何基于工件的测量都看不到它们。这一点对 ADOPT 线的仓库普查同样适用。
3. 抽样是目的性的,并富集了强规格实践的仓库。样本量没有预先设定:作者在未见效应时持续追加仓库,零结果稳定后才停止。全部是事后分析,未预注册。外部效度只限开源。
4. SSRN 预印本(2026-04)的头条是「spec'd PR 引入**更多**缺陷」。ESEM 终稿按审稿条件改成 PSM 主估计下的完全零结果。一位审稿人(#26A)建议拒稿,被元审稿推翻,最终有条件接收,发在 SEIP 轨道。两版不得混引。
5. 匹配估计没有报告 CI。H5 的 CI 是 ±0.10 log-churn,并不算紧。

**本线现场核验**(复跑 `master-prs.csv`)
- 非 bot 88,052 条,spec'd 24,298 条(27.6%),来源分解与论文表 2 逐项吻合。
- **新发现**:「项目 ticket ID」类 5,112 个 PR 中,至少 1,161 个匹配的是普通连字符词,不是工单号。例如 ID-BASED、LLM-GENERATED、CPU-ONLY、UUID-BASED,约占 spec'd 的 4.8%。这类误判大多是非差异性噪声,会把效应往零拉,与零结果同方向。它不足以翻转结论,但应交方法学审计席。
- 作者自己的勘误(C15)披露过一个 pandas `== True` 误用,漏掉了 11.5% 的评分 PR。透明度好,但说明分析管线出过真实的编码错误。

**利益**:作者署名「Independent Researcher」,无资助或 COI 声明。他的 GitHub 上有《The Delivery Gap》一书和 cost-per-accepted-change 指标项目,属于非财务的立场利益。就职 Delivery Hero 一说只来自二手(LinkedIn 搜索摘要),未核。

**转述失真**:Hill 在相关工作里说 Eberhardt 的 Spec Kit 产出是「buggy code」。原文说的是代码质量「just fine」,只有 1 个简单 bug,kartlog 提交显示修复为 +3/−2 行(C18)。Hill 对 Piskala「50%」引用链的拆解(C16)有价值,但本线没能回到 Piskala 原文,交验证阶段。

## 2. Böckeler(martinfowler.com,2025-10-15)

- 正文取自 3 份独立网页剪藏,关键句逐字一致;链接锚文本已去掉 markdown 标记。
- **「小 bug → 4 user stories / 16 acceptance criteria」逐字核实(C19)**。原文还说这「像用大锤砸坚果」,并引了一条凑数的 user story。
- 口径:单次运行,时间是 2025-10,Kiro 当时尚未 GA,没有墙钟或 token 数据。不得外推为 Kiro 现在的行为(新的 bugfix 流程交 VENDOR 线核)。
- spec-kit 部分:一个 3–5 点的棕地功能,markdown「repetitive… verbose and tedious」(C20)。她的结论是「I'd rather review code than all these markdown files」(C21)。agent 无视 research 笔记,把现有类重新生成了一遍(C22)。
- MDD 类比:担心 spec-as-source 落得「Inflexibility *and* non-determinism」(C23)。「MDD 从未普及」是她的亲历判断,不是数据,交 HIST 线。
- **常见误读**:她并不反对 spec-first,原话是「definitely valuable in many situations」(C24)。她批评的是重型工具流程和这个术语的语义稀释。

## 3. Scott Logic / Eberhardt(2025-11-26)——唯一带计时的实操

- 来源:ScottLogic/blog 源码仓库里的原文。我逐个提交核对了 ColinEberhardt/kartlog 的 git 历史。
- **实测了什么**:Spec Kit(Copilot + Sonnet 4.5)重建一个约 1,000 行的 CRUD 功能。第一增量:agent 33m30s,产出 689 行代码、2,577 行 md,自报审阅约 3.5h。其中 Plan 一步就是 2,067 行 md。迭代式做法:agent 8m,15m 代码审阅,9m 测试。作者自估「around ten times faster」。
- **git 核验**:删除 −1,069 行、spec +230、plan +2,067、实现 +689,均吻合。但原文的 Tasks 一节误抄了 Plan 的统计,实际是 +312 行。逐项相加是 2,770,对不上文中的 2,577。
- **对照不对称**:n=1,是自己的业余应用,而且是他已经写过的功能。审阅时间是自报。迭代臂的计时出处不明。按原文数字算,倍数在 7.6×(只算增量一)到 12×(两个增量)之间,「十倍」只能作为作者自估引用。
- 文章声称要列 token,实际没有列。
- 他自己留了余地:「I am simply just using it wrong」也有可能,而且他未必是目标用户(C28)。

## 4. Marmelab / Zaninotto(2025-11-12)——观点文,无测量

- 来源:HN 存档里的整页副本。
- 7 项缺陷清单(C29),以及「agent 把 verify 任务勾成完成却没写测试」(C30)。「80% 时间在读」是修辞,不得承重。
- **核验**:他引用的「8 files and 1,300 lines」出自 frequentito PR#42。specs 目录确实是 8 个文件,但新增行数是 **1,865**,不是 1,300。生产代码约 126 行。
- 利益:Zaninotto 是 Marmelab CEO,在推自家命名的「Natural Language Development」路线。他不卖 SDD 工具,但有替代方法论的品牌。他承认 SDD 适合从零起步的新项目(C31)。

## 5. 流程税 / token 的独立测量——几乎是空白

- 没有搜到任何多被试、受控的「SDD 工作流 vs plan-mode/迭代提示」墙钟或 token 对照实验。Uvik benchmark 归 MEASURE 线,属厂商口径。
- spec-kit issue #1492(C32):Pro 账户「不到一小时」触顶,单用户自报,没有计数。
- 仓库 issue 计数(按 issue 计,不按人计):含 token 的 164 条、overhead 32 条、verbose 22 条。
- 社区专门做了一个查「幽灵完成」的扩展(C33)。这只证明问题存在,不能说明发生频率。
- Garg 的 InfoQ 试点(n=5:有 spec 审阅 48 分钟 vs 只看代码 27 分钟,81% 的发现能对应到条款,发现率持平)和 Instil(「数倍成本」,无数字)都只有二手来源(C34、C35)。

## 最强 / 最弱

- **最强**:
  - C02/C03:Hill 的构念说明,外加本线复跑数据的核验。
  - C04:H1 匹配主估计。它有一手数据可复跑,但处理变量只是工单引用。
  - C26:Eberhardt 的 markdown 和代码行数,由 git 历史逐提交核实。
- **最弱**:
  - C34:Garg 试点,二手且 n=5。
  - C35:Instil,无数字。
  - C30 里的「80%」,以及 C27 的「十倍」:单人自估,对照不对称。

## 交验证阶段的重点

1. Hill 的匹配估计缺 CI;可选停止的影响;ticket 正则误报(≥1,161 例);返工启发式没有人工校验。
2. Hill 预印本和终稿头条不一致。
3. Eberhardt 原文的数字自相矛盾(Tasks 统计、markdown 合计)。
4. Marmelab 的行数口径对不上实测。
5. 回 arXiv 一手核对 Zietsman、Marri、Tufano、Smékal、SpecMine,以及 Piskala 的「50%」引用链。
