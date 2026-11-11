# R3 · R3-X 反证搜索席
靶子:Spec Kit Agents(Taghavi & Bhavani, arXiv 2604.05278v1)Table 1/Table 4——"完整 Spec Kit 流程 vs 直接实现"LLM 评审 3.51 vs 3.46(1–5)、完成耗时 24.0 vs 14.4 分钟;Table 2 人类盲审 Full 19 / Tie 33 / Full-Aug 8。Round 2 成文口径称其为"**唯一**直接的完整 SDD vs 直接实现受控对照"(03-verification-round2.md 第 76 行)。论断 ID:P26 / M23(G05)。

今天复核了:
- arXiv 2604.05278v1 PDF(pdftotext;Table 1 第 186–193 行、Table 4 第 195–200 行、§3.4 第 126、209 行)
- 仓库内 `data/uvik-sdd-benchmark-2026-results.csv`(300 行;本席独立复算 Spec Kit 臂 vs no_spec 臂)
- arXiv 2602.02584v1(Marri, Constitutional SDD)§5.3 Table 3
- arXiv 2608.23616v4(Fawcett, Rebuild Dossier)§4.8、§4.9、§4.15 及 v4 勘误页
- arXiv 2605.01160v1(Farrag, Productivity-Reliability Paradox)§7.4
- arXiv 2611.05094v1(Abdo & Brom, Gated SDD audit-trail)Table 1
- arXiv 2609.09671v1(Hartman/Databricks, Consort)摘要与 §评估设计
- arXiv 2606.04967v1(Macedo, From Prompt to Process)摘要
- arXiv 2609.00252v1、2610.07534v1、2608.20341v1(均为概念/工件评分/框架报告,无对照,扫读确认)
- InfoQ, Nitin Garg, "When Spec-Driven Development Pays off"(2026-09-10)全文 HTML
- Instil, Matthew Wilson, "Spec-driven development is dead, long live plan mode"(2026-06-19)全文 HTML
- Asana, "Spec-driven development: The Good Parts"(.md 版)
- XB Software 博客 "AI in legacy systems: spec-driven development"
- DEV, Incomplete Developer, "OpenSpec … Failed My Experiment"(2026-04-01)
- Vunvulea Radu 博客 "I compared spec kit with and without extensions"(2026-03-26)
- RusDyn/planman README(raw.githubusercontent.com)

没拿到:
- Uvik 网页原文(本席只用仓库内 CSV;页面口径由 R2 席处理)
- Garg 所称 GAISS 2026 论文正文/预印本(只读到 InfoQ 文章本身)
- Prezi "We Tried Spec-Driven Development So You Don't Have To"(Instil 引用;检索未找到原文)
- arXiv 2609.20804(Harness Design 实证研究)、AgentModernize 2605.17535 正文——只有检索摘要,未下载核对,下文仅作角度记录、不作证据
- Spec Kit Agents 的任何独立复现或引用论文(检索 0 结果)

## 一、发现

**F1. "唯一"表述不成立:Uvik 基准就是第二个同构对照(独立团队、独立数据)。**
Uvik CSV 中 `arm=spec_kit` 与 `arm=no_spec` 各 50 张同一批工单(`noise_rerun=0`),两臂都是 `agent=claude-code`、`model=claude-sonnet-5`(CSV `agent`/`model` 列;仅 Kiro 臂用自有 agent),no_spec 臂 `spec_minutes` 全为 0。这在设计上就是"完整 Spec Kit 流程 vs 直接让 agent 实现",与 Spec Kit Agents Table 1 的 Full vs Baseline 同构,而且作者团队和任务集都不同。本席复算(python3 -I,csv+statistics,McNemar 精确双侧):
- 合并:Spec Kit 40/50 vs no_spec 36/50;不一致对 8(仅 SK 合并)vs 4(仅 NS 合并),McNemar 精确 p=0.388——质量差异不显著
- 每合并工单评审缺陷:0.57 vs 0.86(分母为各自合并集合,幸存者构成不同)
- 总耗时:中位 44 vs 31 分钟,均值 45.2 vs 31.2;配对比值中位 1.44×,50 张中 47 张 Spec Kit 更慢;合计 2,260 vs 1,560 分钟 = 1.45×
- 中位成本 $2.69 vs $1.75
**方向与靶子一致**:质量差异小且不显著,时间约 +45%(靶子是 +67%)。注意:Uvik 在本仓库归【厂商】口径,R2 靶子另有 M 席审计;它若被否决,本条只剩"存在第二个同构设计"这一事实,数值不承重。

**F2. 靶子自身的耗时比较跨了两个不同的配对子集(补充 R2)。**
2604.05278v1 Table 4 第 199–200 行:"Baseline vs. Augmented 14.4 / 15.5 / +1.1 / 15"、"Full vs. Full-Augmented 24.0 / 37.2 / +13.2 / 16"。14.4 来自 n=15 的 Baseline–Augmented 配对子集,24.0 来自 n=16 的 Full–Full-Aug 配对子集;论文**没有**直接报告 Baseline vs Full 的配对耗时。"24.0 vs 14.4(约 1.7×)"是本仓库把两张子表拼起来的结果,成文须写明"跨子集、非配对",或只写"约 1.5–1.7×"并以 Uvik 的 1.45× 作方向佐证。另外两者的预算不同(40 vs 90 分钟,R2 已记)。

**F3. Garg(InfoQ 2026-09)生成侧实验:方向存争,且指出混杂变量。**
InfoQ 原文(本席抓取全文):生成侧实验有 direct generation / chain-of-thought(先推理不写 spec)/ 单 prompt "spec-then-code" / 分阶段(先写 SPEC.md 再新开一步实现)四臂。逐字:"one arm asked the model for 'a specification, then the code' in a single prompt. That was indistinguishable from just asking for code directly. Both landed at 23.8 percent on a weak model. A staged arm … nearly doubled the pass rate to forty-five percent … (This trend of p≈0.18 at n=4 carries a second-pass confound discussed below)";以及 "fifty-nine percent (just write code) to ninety-five percent (reason first) to ninety-two percent (spec first), with spec-versus-reasoning not significant"。
- 独立团队、独立任务;但这是提示层级的 spec 产物,不是 Spec Kit 全流程,且 n=4、p≈0.18,作者自称"preliminary and directional"。
- 对靶子的意义:(a) 弱模型+复杂任务上分阶段 spec 方向为正(不显著),与靶子的"几乎无差"方向不同——属**方向存争**;(b) 简单任务上的 spec 增益几乎全被"先推理"对照吃掉,说明 Spec Kit Agents 的 Baseline(无推理对照)与 Full 的差异本身也混杂了"额外思考/额外 token"。
- 审阅侧(Table 2,5 名审阅者,配对 Wilcoxon):recall 0.525 vs 0.518(p=0.69),耗时 48.4 vs 26.7 分钟(p=0.043)。这是"审阅者有/无 spec",不是"实现时有/无 SDD",不对靶。

**F4. Rebuild Dossier(Fawcett,独立研究者,2608.23616v4):spec 流水线 vs 单 prompt,打平到落败。**
§4.8:弱模型(Haiku)上 Madeline 应用,单 prompt 与 spec-plus-rails 各 3 次,全部 7/7 可见 + 1/1 留出——"rebuild-dossier's full apparatus did not outperform giving the same weak-tier model direct source access and a single prompt"。§4.9:catchandtrade 应用上 spec-plus-rails "loses to single-prompt"(纪律维度,3 vs 3)。§4.15:同模型单次成本,单 prompt 17.4 分钟 / 488,055 输出 token,dossier 18.8 分钟 / 123,286 输出 token,另有约 36 分钟零 token 的抽取步骤。
- 方向与靶子一致(spec 流程没赢直接做),但任务是"从抽取的 spec 重建应用",单 prompt 臂可以读到真实源码,与 SDD 新功能开发不同构;n=3/臂;v4 勘误页自承"mechanically enforced"等表述错误。只能作旁证。

**F5. Planman(RusDyn,插件作者自测):plan mode 对直接实现零效应。**
README 第 248–256 行:同一 50 题 SWE-bench Verified 子集上,"Claude Code (baseline) 35/50 … No plan phase"、"Claude Code + plan mode 35/50 … Plan phase, no plugin"、"Claude Code + planman 37/50";"Plan mode alone has zero effect"。
- 这比较的是 plan mode 与直接实现,不是完整 SDD;作者是插件方(利益相关);n=50、单次;README 内部还有矛盾(第 241 行写基线 300/500=60.0%,第 258 行写 "Our baseline (71%)")。只能作"轻量计划同样无增益"的弱旁证。

**F6. 反方向的唯一"对照":Marri 2602.02584(n=1,不可承重)。**
§5.3 逐字:"implementing the same banking application requirements twice … Both implementations used the same AI assistant (Claude) and the same developer"。Table 3:CWE 违规 3 vs 11("73% reduction"),首个安全构建 4 天 vs 9 天("56% faster")。
- 方向与靶子相反(质量更好、速度更快),但只有一个项目、同一开发者先后做两遍、没有平衡顺序、只测安全维度,作者也是方法提出者;Hill(G06/G07)已指出此问题。不构成独立矛盾。

**F7. 其余角度:有前后对比或计划中的研究,但没有受控对照。**
- Farrag 2605.01160 §7.4:3 个团队、14 名工程师,前后各两个月(引入 Spec Kit 前/后);原文 "The objective was not to produce a controlled experiment",结果"qualitative and indicative"。
- Asana:7 名工程师、524 个 PR,看各人首次使用 /spec-driven 前后的变化;原文 "These comparisons weren't controlled"。而且这是自研工作流,对比对象也不是 plan mode 臂。
- Abdo & Brom 2611.05094 Table 1 说明:"None of the claims is comparative, because the study has no control condition."
- Consort 2609.09671:受控比较只是预注册的未来工作("claims we frame as a pre-registered, testable hypothesis"),作者为 Databricks 框架开发者。
- XB Software:单个遗留项目、自估"half the time it would have taken manually",另称"Spec Kit is overkill for tasks estimated at two days or less"——无对照臂,属厂商自述。
- DEV(OpenSpec vs Instructions.md):单人、单个 UI 任务、OpenSpec 跑了 2 次,没有计量——方向与靶子一致,但只是轶事。
- Instil(Wilson):"On the spec-kit projects I ran, the cost ran several multiples of the equiv[alent plan-mode]"、"roughly similar quality of output";没有数字。
- Vunvulea:Spec Kit 对比 Spec Kit+扩展(9.00 vs 7.19 自定义加权分),不是对比直接实现,不对靶。
- 检索摘要层(未下载核对):arXiv 2609.20804 称"计划"仅对弱模型(Nemotron-3 30B)在 SWE-Bench 上 +11.6pp,强模型主要是降成本;AgentModernize 2605.17535 称完整流水线在强模型上输给单 prompt。两者都是计划/流水线消融,不是 SDD,只记录为角度。

## 二、结局

**X 席:独立证实(仅方向;且"唯一对照"表述被推翻)**

- 存在一个独立团队、独立数据的同构对照(Uvik:同一批 50 张工单,Spec Kit 对比 no-spec,同为 Claude Code + claude-sonnet-5)。方向与靶子一致:质量差异小且不显著(合并 40 vs 36,McNemar p=0.39),耗时约 ×1.45。但 Uvik 属厂商口径,数值由 R2 的 M 席裁决;证实的强度最多到"方向"。
- 非同构的旁证(Rebuild Dossier、Planman、Instil/DEV 轶事)都指向"走 spec/计划流程没赢直接做、成本更高"。没有找到任何受控的独立矛盾;Marri 的反方向结果是 n=1 的前后自比,不算数。
- Garg 生成侧给出了方向不同的弱信号(弱模型+复杂任务上分阶段 spec 23.8%→45%,n=4,p≈0.18),并指出"先推理"这一混杂变量。成文应写"方向存争的边缘条件",而不是"完全无效"。
- 成文必须改:删掉"唯一";耗时写成"约 1.5–1.7×(Spec Kit Agents 跨子集拼接;Uvik 配对 1.45×)";质量写成"两项独立对照都未见显著差异(LLM 评审 +0.05/5;人工合并率 +8pp,p=0.39)",并带上"厂商口径/单次运行"的限定。

| 角度 | 查询/来源 | 结果 |
|---|---|---|
| 同构对照:Spec Kit vs 无 spec,同模型同 harness | 仓库内 Uvik CSV,本席复算 | **找到**:40/50 vs 36/50(p=0.388),时间 1.45×;方向一致;厂商口径 |
| 靶子自身的独立复现/引用 | WebSearch "Spec Kit Agents" Taghavi Bhavani replication | 0 结果,只有聚合页 |
| 学术受控实验(SDD vs 直接实现) | WebSearch arXiv 2026 spec-driven controlled experiment;下载 2606.04967、2611.05094、2609.09671、2609.00252、2610.07534、2608.20341 | 全部无对照:综述/分类、审计日志(明确写无对照)、预注册未来工作、概念分析、工件评分 |
| 随机化/多被试研究 | WebSearch randomized developers with/without spec | 无;只有 2605.01160 前后对比(自称非受控)、2608.12440 单案例 |
| 提示层级 spec 优先 vs 直接生成 | InfoQ Garg 全文 | 找到:单 prompt spec 与直接生成持平 23.8%;分阶段 45%(n=4,p≈0.18);先推理对照吃掉简单任务上的增益——方向存争 |
| spec 流水线 vs 单 prompt(应用重建) | 2608.23616v4 §4.8/4.9/4.15 | 打平(3 vs 3)到落败;输出 token 约为 1/4;不同构 |
| plan mode vs 直接实现 | RusDyn/planman README | 35/50 = 35/50(plan mode 零效应);插件方自测,README 有内部矛盾 |
| 计划消融(SWE-bench 类) | WebSearch planning ablation SWE-bench | 仅检索摘要:2609.20804 计划只对弱模型 +11.6pp;未核原文 |
| 流水线 vs 单 prompt(遗留系统迁移) | WebSearch AgentModernize | 仅检索摘要:强模型上单 prompt 胜;v1/v2 口径不同;未核原文 |
| 反方向证据(SDD 更好/更快) | 2602.02584 §5.3 Table 3 | 同一开发者做两遍,n=1:CWE 3 vs 11、4 vs 9 天;不可承重 |
| 企业前后对比 | Asana .md;2605.01160 §7.4;XB Software | 都是前后对比或自估,作者自承非受控 |
| Kiro spec 模式 vs vibe 模式 | WebSearch Kiro spec vs vibe controlled | 无计量对比(RedMonk 只是定性走查,Kiro 账号文章无数字) |
| BMAD vs 普通 agent | WebSearch BMAD benchmark | 只回到 Uvik |
| 从业者 A/B | DEV OpenSpec;Instil;Scott Logic(已在库);Vunvulea | 单人轶事、无数字,或对比对象不对(Spec Kit 对比 Spec Kit+扩展) |
| Prezi "We Tried SDD…" | WebSearch 精确标题 | 未找到原文 |
| 靶子内部口径 | 2604.05278v1 Table 4 | 发现 24.0 与 14.4 来自不同配对子集(n=16 / n=15),不是直接配对 |
