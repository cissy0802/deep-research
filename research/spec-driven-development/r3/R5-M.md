# R3 · R5-M 方法学审计席(有否决权)

靶子:spec 活性 / 冻结 / 漂移的量化证据——ADOPT 自测克隆样本(A18 无功能 spec 28%、A19 spec 提交占比 7.4/11.6/20% 与「spec 冻结」18/15/5%)、SpecMine 样本计算(A20 单提交 76.4%/84.1%、A21 spec-PR 同改代码 80.5%)、arXiv 2608.25202 访谈「21 人中 14 人报告分歧」(A29/M30)、Uvik「合并代码与自身 spec 不符 7.9%」(M08)。

今天复核了:
- `adopt-measure/repo_metrics.tsv`(180 行)+ `scripts/one.sh`、`sm.py`、`{sk,kiro,os}.txt`:全量复算 + Wilson CI + bootstrap + 阈值敏感性。
- 用 `one.sh` 原样重克隆重跑 9 个仓库(sk 5 / kiro 2 / os 2,含 6 个被判「冻结」的仓),并附加 `--since-as-filter` 对照检查 `--since` 截断偏差。
- 新做对照基线:重克隆 sk + kiro 共 120 仓,用同一「冻结」定义测根目录 README(`r5m/base.sh`)。
- SpecMine 样本仓(specmine-official @ da606c8,2026-11-09):`pull_requests` / `pr_files` / `spec_files` / `spec_file_commits` parquet,DuckDB 2.0.0 重算;DATA_DICTIONARY.md 字段定义。
- arXiv 2608.25202v4 PDF 全文(pdftotext):§III 招募与编码、§III-C 仓库挖掘、§V、§VI Threats to Validity。
- Uvik 原始 CSV `data/uvik-sdd-benchmark-2026-results.csv`(300 行):`spec_drift` / `spec_deviations` / `noise_rerun` 字段。
- 脚本与中间结果:`/tmp/claude-0/-home-user-deep-research/000f24b9-fbee-5fa6-8bbb-c9de969fb25d/scratchpad/r5m/`(a.py 克隆样本复算、b.py/c.py/d.py SpecMine、base.sh/base.tsv README 基线)。

没拿到:SpecMine 全量 Zenodo 档(只有 500 仓样本,所以全量 PR 层的 81.2% 只能引论文原文,复算不了);论文复现包(shyamagarwal13/spec-paper-replication-package,没打开);Uvik 第二评审的身份、盲法和一致性数据(CSV 和页面都没给)。

## 一、发现

**F1 · 克隆样本复算一致,工具层面可复现(计算可复现性 = A)。** a.py 复算 A18/A19 全部数字:sk nspec=0 17/60、中位数 2/4/40;spec 提交占比中位数 0.074(n=59)/ 0.116 / 0.200;冻结 11/60、9/60、3/60。重克隆 9 仓重跑 `one.sh`,10 个字段与 tsv 逐字一致;只有 zod-schema-faker 因新提交多 1–2 次提交,openspec-cn 总提交 464→463(上游重写了历史)。`--since-as-filter` 和 `--since` 在 9/9 仓结果相同,没发现 rev-list 截断偏差。另有一个小怪癖:`--since="<日期>"` 不带时刻,git 会补成运行时的当日时刻,首日提交可能被漏计,只影响 tot/specc 的个位数。

**F2 · 精度:n=60 的区间很宽,不支持精确百分比和工具排序。** Wilson 95% CI:
- sk 无功能 spec:17/60 = 28.3%,[18.5, 40.8]%
- 冻结:sk 18.3% [10.6, 29.9];kiro 15.0% [8.1, 26.1];os 5.0% [1.7, 13.7]
- 近 3 个月无提交:sk 26.7% [17.1, 39.0];kiro 55.0–56.7% [42.5, 68.4];os 50.0% [37.7, 62.3]
- spec 提交占比中位数的 bootstrap 95%(5,000 次):sk [4.2, 12.6]%、kiro [7.4, 19.4]%、os [17.7, 23.1]%

冻结率 sk vs kiro:Fisher p=0.81。sk vs os:p=0.043,但这是没校正的结果,同时做了 3 对 × 多个指标的比较,而且两边计的目录不同(见 F4),所以不成立。

**F3 · 「冻结」对阈值极敏感,结果更像是阈值选出来的。** 同一份 sk 数据,只改两个阈值(spec 后提交数 A、间隔天数 G):
- A≥50 / G≥60:5/60(8.3%)
- A≥20 / G≥90:9/60(15%)
- 原定义 A≥20 / G≥60:11/60(18.3%)
- 间隔改按「距今」算:13/60(21.7%)
- A≥10 / G≥30:20/60(33.3%)
- A≥5 / G≥30:21/60(35%)

取值范围是 8–35%,宽了 4 倍。按「距今」算时 kiro 15/60 > sk 13/60,工具排序直接翻转。阈值没有预注册,是 Round 1 事后选的。

**F4 · 测量效度:分母、截尾、误判、目录口径都有问题。**
- (a)分母混入了没有 spec 的仓。sk 的 60 仓里有 14 仓 `lastspec` 为空;只看有 spec 记录的 46 仓,冻结率是 11/46 = 23.9%。再排除「工具装上到仓库最后一次提交不足 60 天、按定义根本不可能被判冻结」的仓:sk 11/34 = 32% [19, 49];kiro 9/30 = 30%;os 3/44 = 7%。kiro 有 30/60 的仓工具龄不足 60 天,右截尾很重。
- (b)误判。sk 用的路径是 `specs` 目录,不是 spec-kit 的功能 spec。DeeCode-inc/tanstack-query-chrome-devtools 的 nspec=0,但根目录有一个叫 `specs` 的文件(`git log --name-status`:`A specs`、`M specs`),被计成了「冻结」。另有 2 个 nspec=0 的仓也命中了 `specs` 路径。sk 冻结 11 例里至少 1 例是假阳性。
- (c)目录口径不同。sk 计 `specs/`,kiro 计 `.kiro/specs`,os 计整个 `openspec/`(含 AGENTS.md、project.md,以及 change→archive 流程强制产生的移动)。所以「OpenSpec 更活 / 更少冻结」不能比。
- (d)样本被工具自家仓和演示仓污染。os 样本里有 openspec-cn/openspec,是 OpenSpec 本体的中文镜像,463 次提交里 216 次改 spec。kiro 样本里有 kiro-project-template、getting-started-with-kiro、flappy-kiro、Kiro-InteractionKit 等模板或教程仓。sk 样本里有 Spec-Kit-VS-Code、ai-genius-s4-ep2-speckit。
- (e)冻结例里有一部分其实是「只用过一次」:arrows.app、vibego、strata、SlimBook、open-bridge、roxas、zod-schema-faker 都是 specc=1。这是「试了一次就不用了」还是「spec 停更、代码继续」,用提交计数分不出来。

**F5 · 没有基线的「冻结率」无法解读:spec 并不比 README 冻结得更多(新测)。** 对同样 120 仓按同一定义测根目录 README(该处最后一次修改后 ≥20 次提交、且间隔 ≥60 天):
- sk:README 冻结 6/60(10%),spec 冻结 11/60;两者都冻结 2 仓。配对比较只有 spec 冻结 9 仓、只有 README 冻结 4 仓,精确 McNemar p=0.27。
- kiro:README 冻结 7/60(12%),spec 冻结 9/60;不一致对 8:6,p=0.79。

也就是说,「spec 停更、代码继续」跟普通文档停更是同一量级,没有证据显示 spec 有额外的腐坏。这个对照在 Round 1/2 里没有人做过。

**F6 · A20「单提交 = 创建后从未修改」的构念不成立,SpecMine 作者自己也这么说。**
- 论文 v4 §VI-B 原文:「Commit counts understate revision. The histories we retrieved do not follow renames, so a file moved to a new path loses the commits made before the move. OpenSpec's archive step moves every completed change in this way. Squashed or rebased commits also merge several edits into one. Conversely, a recorded revision may only fix a typo. Commit counts therefore cannot show spec decay, which would require checking whether the behavior a spec describes changed while the spec did not.」§V 也写了「recovering design history from version control can be lossy when files are renamed or commits are squashed」。
- 本席在数据里核实了这两条(d.py):
  - squash 合并:单提交的 speckit feature spec 共 1,373 个,其中 66.1% 的首提交标题以 `(#N)` 结尾,是典型的 GitHub squash 合并。spec 在 feature 分支上改过多少次,在默认分支上都看不见。
  - 重命名:单提交的 openspec archived spec 共 14,213 个,其中 56.9% 的首提交信息含「archive」,也就是归档时移动路径、历史被清零。openspec 的 84.1% 里 66%(14,708/22,132)是 archived 角色,这个数主要由流程机制决定。
  - 年龄截尾:按首提交距爬取截止日 2026-07-11 分层,speckit 单提交率是 <30 天 90.9%、≥180 天 66.5%(n=200);openspec 是 92.2% → 75.0%(n=571)。合并口径的 76.4% 被新文件抬高了约 10pp。
  - 另:`file_total_commits` 与 `spec_file_commits` 的行数 28,583/28,583 完全一致,数据内部自洽,问题出在构念上,不在数据质量。

**F7 · A21「80.5% 同改代码」用错了条件方向,而且大半是工作流本身的机械结果。**
- (a)这是选在结局上的样本。PR 层只收「触及 spec 的 PR」,而且 `is_merged` 全为 1,只有已合并的 PR。它给的是 P(改代码 | 改了 spec)。漂移需要的是反方向 P(改了 spec | 改代码),这个 PR 层给不出来。本线 A19 测的正好是反方向:中位只有 7–20% 的提交碰 spec。
- (b)拆开看 spec 文件的变更状态(pr_files.change_status,以 5,335 个工具×PR 行计):
  - 只新增 spec:2,869(54%),其中 83% 同改代码。这是「新功能 spec 与实现同一个 PR 合入」,是 spec-kit 按分支开发的机械结果,不是维护。
  - 既新增又修改:1,193,同改代码 89.5%。
  - 只修改已有 spec:1,155,同改代码 70.7%。
  - 未触及 spec.md:117。
  - 「修改已有 spec 且同改代码」约 1,885 / 5,335 ≈ 35%。这才是比较接近「spec 跟着代码更新」的口径。
- (c)聚类:229 仓,每仓 PR 数中位 10、最多 327(elastic/terraform-provider-elasticstack),前 12 仓占 34% 的 PR。各仓同改率差异很大,中位 0.94,liqiongyu/agentpack 只有 0.035(170 PR)。按仓聚类 bootstrap 的 95% CI 是 [73.4, 86.2]%,不是点值 80.5%。
- (d)Round 1 备注「共变可能只是勾 tasks.md」在这里不适用:`is_spec` 只标 spec.md(全部被修改或新增的 spec 文件 basename 都是 spec.md/SPEC.md),tasks.md 走的是 `n_md_files`,`is_code` 对 md/json/yaml 全为 0。
- (e)论文 §III-C 原文给出全量口径:「5,979 PRs from 581 repositories, and 81.2% of these PRs also modify code」。80.5% 是样本复算,成文应改引论文的 81.2%(全量)。但它和 A20、A29 出自同一团队、同一数据,不能算两个来源。

**F8 · A29 的 14/21 是定性自述,不是患病率。** 论文 §III-B 原文:「Each source was first coded by one author, and we did not measure inter-rater agreement」。§VI-C 原文:「they are likely more engaged with SDD than practitioners generally. Their accounts show which practices exist but not how common the practices are.」样本是 LinkedIn、Reddit、GitHub 招募来的志愿者,8/21 是工具作者,也没有对照。另外,§IV 写明了三种 spec 维护实践(living spec / 累积变更记录 / 实现后丢弃),而且 Spec Kit「leaves the choice between the two to the team」。这意味着功能 spec 冻结可以是一种合法的实践,进一步否定「冻结 = 漂移」。同文还有一个可承重的普查口径(§III-C):「29.9% of named-tool repositories above the star threshold have at most one spec commit」,样本比本线 n=60 大,方向和 A18 相同,但仍是提交计数。

**F9 · M08 Uvik 7.9%:单时点、单评审、无信度数据,还有一个新的数据红旗。**
- 主运行(noise_rerun=0)里 spec 臂合并 164 次、`spec_drift`=1 共 13 次:7.9%,Wilson [4.7, 13.1]%。把 39 次复跑也算进去是 13/203 = 6.4%。
- `spec_drift` 等价于 `spec_deviations`≥1(交叉表 (0,0)=190、(1,1)=7、(1,2)=6),是同一次判定,不是独立的第二个测量。
- 分臂:SK 5/40、Kiro 2/41、BMAD 5/41、OS 1/42。四臂异质性 χ²=4.46(df=3,p≈0.22);SK vs OS 的 Fisher p=0.10。分臂排序不成立。
- 新红旗:复跑选的 10 个工单(T06/T09/T16/T19/T26/T29/T36/T39/T46/T49,尾号都是 6 或 9,是确定性选取)和 12 个出现过 drift 的工单零重合。按超几何算,随机选出零重合的概率约 0.046。复跑 0/39 drift;如果真实率是 7.9%,观察到 0/39 的概率约 0.040。结果是 drift 判定的重测信度完全没有被观测到。同期复跑中的 review_defects 在 18 对里有差异,说明评审本身有噪声,而 drift 恰好全部落在没复跑的工单上。
- 页面原文自限:「does not measure the long-term value of a living spec across many changes」。

**F10 · 独立性。** A20、A21、A29、M30 和论文的 81.2% 是同一团队(CMU+Google)、同一语料,算 1 个来源。ADOPT 克隆样本(A18/A19)的抽样框独立(GitHub code search best-match),但和 A20 一样用提交计数做代理,两者都栽在 F5/F6 指出的同一个构念缺陷上。所以二者同向不构成「多源证实」:它们共享的是同一种测量偏差,不是同一事实的两次独立观测。Uvik(M08)测的是另一个构念(单时点一致性),而且是厂商口径,不能和「冻结」互证。

## 二、结局

**M 席评级:C**(计算可复现性 A:克隆和 SpecMine 数字全部复现,9 仓重跑一致;但作为「spec 活性/漂移」的测量,构念效度不成立——没有基线、阈值事后选定、提交计数被 squash/rename 系统性扭曲,SpecMine 作者明文承认「Commit counts therefore cannot show spec decay」)。

**否决清单(不得承重)**
- **V1**:A19「spec 冻结 18%/15%/5%」作为 spec 腐坏、漂移或过时的证据。理由:同定义的 README 基线 10%/12%,配对 p=0.27/0.79;阈值敏感区间 8–35%,排序可翻转;有假阳性;右截尾。也禁止「spec 冻结率」写成任何精确百分比。
- **V2**:三工具活性或冻结排序(「OpenSpec 更活/更少冻结」「spec-kit 最易冻结」)。理由:计数目录不同;多重比较校正后不显著;os 样本含工具本体镜像仓。
- **V3**:A20「76.4%/84.1% 的 spec 创建后从未修改」及其任何「冻结」读法。理由:squash 66.1%、archive 改名 56.9%、年龄截尾约 10pp;作者在 §VI-B 原文否认提交计数能测 decay;README 明言样本不可估总体。
- **V4**:A21 / 论文 81.2% 作为「spec 与代码保持同步」「spec 是活的」「SDD 避免漂移」的证据。理由:条件方向反了,样本按结局选取且只含已合并 PR;54% 是新 spec 随实现同 PR 入库;修改已有 spec 且同改代码约 35%。
- **V5**:「21 人中 14 人报告分歧」写成比例或发生率(「三分之二的 SDD 实践者遭遇漂移」)。理由:志愿者样本、单人编码、无 IRR,作者原话「not how common」。
- **V6**:M08「7.9% 漂移率」,以及 Uvik 分臂不一致率排序。理由:单时点、单一第二评审、无信度;复跑零覆盖 drift 工单;厂商口径。
- **V7**:A18「28% 的 spec-kit 仓库没写过 spec」作为总体比率。理由:best-match 非随机抽样,CI 18–41%。

**可承重的最强写法**
> 公开仓库的提交史测不出 spec 漂移——数据集作者自己写明「Commit counts therefore cannot show spec decay」,因为 squash 和归档改名会抹掉修订史。能测到的是三件弱事实:(1)装了不等于持续用:CMU 普查里,超过星标阈值的命名工具仓库有 29.9% 至多只有一次 spec 提交;本期抽查 60 个 spec-kit 仓,17 个没有任何功能 spec(约两到四成)。(2)改 spec 的 PR 大多同时改代码(全量 5,979 个 PR 中 81.2%),但这多半是「新 spec 与实现一起合入」,改已有 spec 并同改代码的只约三分之一。所以它说明 spec 是跟着功能分支走的,不说明 spec 后来被维护。(3)「spec 停更、代码继续」的仓库比例与 README 停更同量级(约一到两成),没有证据显示 spec 腐坏得比普通文档快。漂移的直接证据只有两种:实践者自述(21 名志愿受访者中 14 人报告过分歧,定性)和一个厂商基准的单时点核对(13/164 个合并工单代码与自身 spec 不符,95% CI 约 5–13%)。两者都不是随时间的漂移率。

**证据分级建议**
- A18「装了≠用了」(17/60 写成「约两到四成」)+ 论文 29.9%:**单源已核**,方向可写,程度不承重。两者同为提交或文件计数口径,方向一致,但不升「多源证实」。
- A19「冻结」:**未验证**(作为漂移构念);如果要写,只能写「与 README 停更同量级」这一反向发现,标「现场核验 · 本期自测」。
- A20:**弃用**,或只作「提交计数不可用」的方法学注脚。
- A21 / 81.2%:**单源已核**(描述性:spec-PR 多同改代码),同时必须带「多为新 spec 与实现同入、改已有 spec 约 35%」;作为同步或活性证据则否决。
- A29 14/21:**单源已核**(定性自述存在分歧),不得量化为比例。
- M08 7.9%:**厂商口径**(单时点、单评审),只能带 CI 和「非随时间漂移」整体引用,分臂不承重。
- 「SDD 让 spec 保持活性 / 不漂移」或其反命题「spec 普遍腐坏」:**未验证**(当前公开数据没有任何一项测量能检验)。
