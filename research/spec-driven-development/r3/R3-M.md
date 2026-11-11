# R3 · R3-M 方法学审计席(有否决权)
靶子:Spec Kit Agents(Taghavi & Bhavani, arXiv 2604.05278v1)Table 1/2/4,即「完整 Spec Kit vs 直接实现:LLM 评审 3.51 vs 3.46;完成耗时 24.0 vs 14.4 分钟;人类盲审 Full 19 : Tie 33 : Full-Aug 8」(论断 P26 / M23,G05;Round 2 汇总 03 第 57、76 行把它定为「唯一直接的完整 SDD 流程 vs 直接实现受控对照」)。

今天复核了:
- arXiv 2604.05278v1 PDF(abs 页确认只有 v1,2026-04-07 提交;10 页),pdftotext 全文。逐句定位:摘要;§3.1 LLM-as-judge 段与排除规则;§3.4 Configurations / Budgets / Success criteria;§4.1;§4.2 + Table 1、Table 2;§4.3 Table 3;§4.4 Table 4;§4.5 Table 5;附录 A Table 6;附录 B.2 Table 7、B.4、B.5;附录 C。
- 亲手复算(脚本 scratchpad/r3m_calc.py):Table 1 的加权一致性、各仓库方向、人类偏好符号检验、功效/MDE、SWE-bench Lite 分母。
- 代码/数据可得性:arXiv abs 页(无代码链接)、`gh search repos "spec kit agents"`、网页检索论文标题 + 作者名。
- Round 2 的 G05 三票(Q/X/K)与 03-verification-round2.md。

没拿到:
- 每次运行的原始分数、每格的 n(哪些运行被计入质量)、完成率——论文没有发表,也找不到代码/数据仓库(B.4 列出了 config.yaml、experiments/features.yaml、experiment_runner.py、quality_evaluator.py,但全文和 abs 页都没有 URL;GitHub 检索没找到作者的仓库,同名的 siddjoshi/spec-kit-agents 早于论文,与论文无关)。
- 作者机构(PDF 没署;检索只找到 Taghavi 的个人主页,研究方向是计算机视觉/自动驾驶,与 Bhavani 的联系找不到)→ 利益冲突无法评估。
- 人类评审的人数、身份,以及 6 个任务是怎么挑的。

## 一、发现

**F1 · 3.51 vs 3.46 是两套预算、两组生存样本之间的比较,不是配对对照。**
- §3.4:"Baseline and Augmented runs use a 40-minute budget, while Full and Full-Augmented runs use a 90-minute budget. Runs exceeding these limits are terminated and marked as failures." 所以「SDD vs 直接实现」同时改了两件事:工作流和时间预算(90 vs 40 分钟)。两者混在一起,无法分开。
- §3.1:"Rate-limited runs are excluded from latency analyses but retained for quality reporting when a pull request artifact is available"。质量分只算有 PR 产出的运行,所以 Table 1 的每格都是条件于「这次运行产出了 PR」的均值。两族的失败机制不同:40 分钟超时砍掉的是慢任务,也就是难任务。这样 Baseline 留下来的样本会偏向容易的任务,两组均值不可比(生存偏倚,方向未知)。
- 论文没有给出每格的 n 和完成率(§3.1 说 "completion rates include such runs",但全文没有完成率表)。Table 4 透露:两种配置都完成的配对只有 **15/32**(Baseline–Aug)和 **16/32**(Full–Full-Aug),即约一半任务至少有一侧没完成。
- **复算(Table 1 加权一致性)**:§4.2 说 Overall 是 "feature-count-weighted average across repositories"。我枚举了所有总和为 32 的仓库任务数组合 (FastAPI, Airflow, Dexter, Plausible, Strapi),要求同一组权重同时复现四行 Overall(容差 0.01)。只有 13 组可行;能把四行全部精确舍入复现的只有 (6, 8, 7, **1**, 10),也就是 Plausible 只有 1 个任务。但 Table 6 列出了 pla-01/03/05 三个 Plausible 任务和 str-07,至少 3 个 Plausible、7 个 Strapi。在 Plausible ≥ 3 的约束下,没有任何一组权重能同时复现 Full = 3.51 和 Baseline = 3.46,例如 (5,8,7,3,9) 得出 Full = 3.517 → 3.52,(6,8,7,3,8) 得出 Full = 3.501 → 3.50。结论:各配置的有效权重(即计入质量的任务数)不同,或者表内数字有误。不管哪种情况,3.51 − 3.46 = 0.05 都不是同一批任务上的配对差。
  - 不加权的均值:Baseline 3.432、Full 3.488(差 +0.056);两种汇总方式下,差值都落在下一条的噪声带里。

**F2 · 差值 0.05 远小于这个设计能检出的最小效应;作者没有检验它。**
- 论文唯一的统计检验是 Full vs Full-Aug(§4.2 "On the paired subset of completed tasks … Wilcoxon signed-rank, p < 0.05",没给确切 p、效应量和 CI)。Baseline vs Full 没有任何检验,论文也没有把它作为一个对比来报告(§4.4 明确说 "latency is compared only within each budget family",§1 也说 "we interpret latency within each budget family rather than across families")。所以「SDD vs 直接实现」是我们(R1/R2)自己从表里拼出来的对比,作者并没有主张它。
- 复算功效:配对 n = 32,假设配对差的 SD 为 0.3 / 0.5 / 0.7(1–5 分,四维平均的 LLM 评审;论文没报 SD),95% CI 半宽为 ±0.10 / ±0.17 / ±0.24,80% 功效的最小可检效应(MDE)为 0.15 / 0.25 / 0.35。如果按实际完成配对 n ≈ 16 计,MDE 为 0.21 / 0.35 / 0.49。**0.05 ≪ MDE**:这既不能说明「没差别」(没做等价检验),也不能说明「有差别」。
- 每次运行只跑一遍(4 种配置 × 32 任务 = 128 次),没有重复,也没报 judge 的重测信度。

**F3 · 各仓库方向不一致,异质性远大于总效应。** Full − Baseline 按仓库:FastAPI −0.11、Airflow **−0.40**、Dexter +0.25、Plausible +0.18、Strapi +0.36(Table 1)。5 个仓库里有 2 个直接实现得分更高,单仓库的波动(±0.4)是总差值(0.05)的 8 倍。所以「质量无差」的说法也过强,准确的说法是「总分接近,但仓库间方向相反」。

**F4 · 24.0 vs 14.4 分钟(约 1.67×)不能作为跨族的效应量。**
- 两个数来自 Table 4 的两行**不同配对子集**:14.4 是 Baseline 在 Baseline–Aug 共同完成的 15 对中的均值,24.0 是 Full 在 Full–Full-Aug 共同完成的 16 对中的均值。两个任务集不同,而且作者明确不做跨族比较(引文见 F2)。
- 删失阈值不同:只统计完成的运行,而 Baseline 超过 40 分钟就判失败,Full 的上限是 90 分钟。所以 Baseline 的耗时分布在 40 分钟处被截断。即使工作流本身不慢,这种截断也会人为拉大比值。
- 方向(Spec Kit 全流程耗时更长,多出 Specify/Plan/Tasks 三个阶段)在机制上成立;但「+67%」「约 1.7 倍」这个量级不能承重。

**F5 · 人类盲审 19:8 和 SDD vs 直接实现无关,本身也不显著。**
- Table 2 比较的是 **Full vs Full-Aug**,有无钩子,两边都走完整 Spec Kit 流程;不涉及 Baseline。
- 复算:去掉平局后 19 vs 8,双侧精确符号检验 **p = 0.052**,而这是把 60 票当成独立样本算的。实际上票按 **6 个任务**聚集,平均每任务 10 票,评审人数未知,有效样本远小于 27,真实 p 会明显更大。6 个任务只取「两种配置都成功完成」的配对子集,怎么从中挑出来没有说明。
- 33/60(55%)为平局。最多只能写成「人类评审没有复现 LLM 评审给出的 +0.15」;Round 2 的「人类反而偏好无钩子版」「与 LLM 评审方向相反」把一个不显著、有聚集的计数写成了方向性结论,需要降级。§3.1 说人类评审用 "the same rubric",但 Table 2 只给偏好票,没有 1–5 分,无法和 LLM 评审直接对比。

**F6 · 测量效度:主结局是单一 LLM 评审,没有校准。**
- 评审模型是 Claude Opus 4.6(§3.3/§4.1),四维 1–5 分取平均;没报 judge 和人类的一致性、judge 的重测方差,也没报四个分项。附录 Table 7 把这个 judge 的 "LLM-as-judge model ID" 写成 "20250501",与 Opus 4.6 的发布时间对不上(该日期早于 Claude 4 系列),属于版本标注错误或口径不清。
- 生成模型是 MiniMax-M2.5,通过 Claude Code CLI 2.1.50 路由到 "Anthropic-compatible endpoint"(§3.3)。这是单一模型、非原生 harness,结果能否外推到其他 agent/模型没有检验。
- "99.7–100% test compatibility" 只出现在摘要和正文里,没有表,也没有分母(F1 说过,这只在有 PR 的运行上可能成立)。

**F7 · 报告精度的旁证:SWE-bench Lite 的百分比在 n = 300 下不可能出现。** §4.5 说的是 "a standard benchmark of 300 real-world software engineering issues",但 56.5% 和 58.2% 都不是 k/300 能得到的(k/300 只能取 56.33/56.67、58.00/58.33)。按一位小数,最大的可行分母是 **299**(169/299、174/299),也就是实际评估集和声明不符,而论文没有披露。这条不是 R3 的靶子,但说明全文的分母报告不可靠,应该一并降低对 Table 1/4 表内数字的信任。

**F8 · 可复现性与利益冲突。** 没有公开代码、数据和每次运行的结果(见「没拿到」);只有 v1,没有勘误;作者机构未披露,COI 无法评估。系统本身是作者的产品(Spec Kit Agents),论文的主张(+0.15)是有利于自家设计的方向;而我们关心的 Baseline vs Full 对比恰恰是作者没主张、也没检验的,因此不存在作者为这条对比刻意调参的动机。这一点略微有利于它作为「无显著收益」的旁证,但不能弥补 F1–F3 的问题。

## 二、结局

**M 席评级:C**(一手可回溯,表内数字定位无误;但对照有混淆——预算差加生存样本;没有检验,功效不足;没有重复;单一 LLM 评审;加权不能复现;无代码/数据;分母报告有误)。它不能作为「SDD 对质量无影响」的承重证据,只能当「目前唯一公开、但设计无力回答该问题的数据点」。

**否决清单(不得承重)**
- **V1**:「完整 Spec Kit vs 直接实现,质量 3.51 vs 3.46,**质量无差** / 唯一的直接受控对照证明 SDD 不提升质量」。理由:F1(预算混淆、生存样本、加权不可复现)、F2(没检验,0.05 ≪ MDE ≈ 0.15–0.5)、F3(仓库间方向相反)。可以列出数字,但不能把结论压在「无差」上。
- **V2**:「耗时 24.0 vs 14.4 分钟,**+67% / 约 1.7 倍**」作为 SDD 的时间成本量级。理由:F4(不同配对子集、40 vs 90 分钟的删失阈值不同、作者明确不做跨族比较)。
- **V3**:「人类盲审反而偏好无钩子版本 / 与 LLM 评审方向相反」,以及任何把 19:8 用于 SDD vs 直接实现的表述。理由:F5(比较对象是有无钩子;p = 0.052 还是在忽略聚集的情况下;n = 6 任务;选样不明)。
- **V4**:「+0.15 证明上下文钩子(或 SDD)提升质量」作为承重结论。理由:p < 0.05 只在完成配对子集上、没报确切 p 和 CI、单一 LLM 评审、人类评审没复现(F2/F5/F6)。(Round 2 已禁止写成 SDD 收益,这里进一步禁止它作为「钩子有效」的承重。)
- **V5**:「测试兼容 99.7–100%」作为质量保证。没有表、没有分母,只在有 PR 的运行上(F6)。
- (Round 2 已有的禁令维持:SWE-bench Lite 56.5→58.2 不是 SDD 证据。F7 另外发现它的分母和声明的 300 不符。)

**可承重的最强写法**
> 唯一公开把「走完整 Spec Kit 流程」和「直接让 agent 实现」放在同一批仓库任务上的实验(Spec Kit Agents,arXiv 2604.05278,单一生成模型 MiniMax-M2.5、单次运行、Claude Opus 4.6 评审),两者的 LLM 评审分接近(3.51 vs 3.46,满分 5),5 个仓库里有 2 个直接实现得分更高。作者没有检验这个差,两组的时间预算也不同(90 vs 40 分钟),只计入产出了 PR 的运行;按 32 个任务、单次运行的规模,这个实验检不出 0.2 分以下的差异。它说明「没看到 SDD 带来可测的质量提升」,不能说明「SDD 没用」。Spec Kit 全流程的完成时间更长(完成样本中约 24 vs 14 分钟,但两组任务子集和超时上限都不同,倍数不可靠)。给流程加上仓库探测钩子后,LLM 评审再高 0.15,但 6 个任务、60 票的人类盲评有 33 票是平局,没有复现这个提升。

**证据分级建议**
- 「Table 1 数字本身(3.46/3.50/3.51/3.66)」:**单源已核**(一手定位无误)。
- 「完整 Spec Kit vs 直接实现的质量差」:**未验证**。单源、没检验、有混淆;成文时只能作为弱旁证,并标明「作者未检验、预算不同」。
- 「SDD 流程更耗时」(方向):**单源已核**(方向);量级 1.7× **不承重**。
- 「人类评审未复现钩子增益」:**单源已核**(计数准确);「人类偏好相反」:**未验证**。
- 整条靶子在全文论证中的权重:从「唯一直接受控对照(承重)」降为「唯一公开数据点,设计不足以回答(弱结论)」。
