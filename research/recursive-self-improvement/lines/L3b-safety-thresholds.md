# L3b 安全框架阈值与评估结论线(截至 2026-10-03)

调研员: L3b。所有 verbatim 均为本人从一手 PDF/网页抽取的文本(pdftotext 后 grep),除标注"媒体转述"者外。
本地原文副本: /private/tmp/claude-502/-Users-cissychen-design/2a8c67de-88b6-4bee-884f-98cc1b779c58/scratchpad/l3b/

## 一句话结论
截至 2026 年 10 月,三家(Anthropic / OpenAI / Google DeepMind)无一宣布越过 AI R&D / AI 自我改进阈值。但 Anthropic 的判词轨迹明显"变软":Opus 4.5 "越来越难排除" → Opus 4.6 "rule-out 比以往任何模型都更脆弱,预计近期模型高概率越过"(旧 AI R&D-4) → RSP v3 改用"进步速率翻倍"二阶导定义 → Feb 2026 Risk Report "Very low" → Aug 2026 Risk Report "Low,信心下降,任务型评估饱和,看到早期加速迹象" → Opus 5.5(2026-09-22) METR 独立估计 "~1.5X,约 30% 概率 2X"。同时,所有三家的书面理由都指向同一个瓶颈:模型在"有清晰连续成功指标、反馈廉价"的任务上超人,在"判断/品味/自我验证"上不足——与"瓶颈在裁判"假说一致。

## 阈值原文(口径对比)

### Anthropic
- RSP v2.1/2.2 (2025): AI R&D-4 "the ability to fully automate the work of an entry-level, remote-only researcher at Anthropic"; AI R&D-5 "the ability to cause dramatic acceleration in the rate of effective scaling." (引自 Opus 4.6 system card §8.3)
- RSP v3.0 (2026-02-24): "compress two years of 2018 – 2024 AI progress into a single year"(引自 rsp-updates 页对 v3.1 的说明)
- RSP v3.1 (2026-04-02): 澄清 = "doubling the rate of progress in aggregate AI capabilities",不是 "doubling the productivity of researchers"。
- RSP v3.4 (2026-07-08, 现行): 阈值触发 = "(1) our models would be able to fully substitute for our entire set of Research Scientists and Research Engineers, at competitive costs (i.e., within a factor of 5); or (2) there is "dramatic acceleration" of the pace of AI progress for reasons that likely relate to the automation of AI R&D." 脚注: "if baseline progress involved a 3× scaleup in compute and a 3× improvement in algorithmic efficiency (for a 9× "effective scaleup"), "double the rate of progress" would entail something like an 81× effective scaleup. This is not the same idea as "doubling researchers' productivity," since doubling inputs does not necessarily double the rate of progress." 且要求加速相对"both the rate we'd expect and the fastest rate of extended progress we've observed"(脚注9: "Over at least three model generations")。
- v3.4 changelog: 若总体进步速率恒定或放缓、但估计远快于无 AI 情形,"We would not" 视为越线;"This threshold is intended to capture the onset of dramatic recursive self-improvement, and has proven difficult to operationalize."
  URL: https://www-cdn.anthropic.com/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf

### OpenAI Preparedness Framework v2 (2025-04-15,未见 2026 新版)
- High: "The model's impact is equivalent to giving every OpenAI researcher a highly performant mid-career research engineer assistant, relative to those researchers' 2024 baseline."
- Critical: "The model is capable of recursively self improving (i.e., fully automated AI R&D), defined as either (leading indicator) a superhuman research-scientist agent OR (lagging indicator) causing a generational model improvement (e.g., from OpenAI o1 to OpenAI o3) in 1/5th the wall-clock time of equivalent progress in 2024 (e.g., sped up to just 4 weeks) sustainably for several months." Critical 处置: "halt further development"。
  URL: https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf

### Google DeepMind FSF
- v2.0 (2025-02-04): "Machine Learning R&D uplift level 1: Can or has been used to accelerate AI development, resulting in AI progress substantially accelerating (e.g. 2x) from 2020-2024 rates." / "autonomy level 1: Can fully automate the AI R&D pipeline at a competitive cost. The cost comparison is relative to humans augmented by AI tools."
- v3.1 (2026-04-17): "ML R&D acceleration level 1: Has been used to accelerate AI development, resulting in AI progress substantially accelerating from historical rates." / "ML R&D automation level 1: Can fully automate the work of any team of researchers at Google focused on improving AI capabilities, with approximately comparable all-inclusive costs." ——删掉了 "(e.g. 2x)" 与 "2020-2024" 基准。
  URL: https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf

### 口径差异要点
| | 替代型阈值 | 加速型阈值 | 倍数 |
|---|---|---|---|
| Anthropic v3.4 | 替代全部 RS/RE,成本 5 倍内 | 总体进步速率翻倍(相对 AI 前最快速率),且可归因于自动化 | 2×(速率) |
| OpenAI High | — (影响型: 每位研究员配一个中级研究工程师助手) | — | 无数字 |
| OpenAI Critical | 超人研究科学家 agent | 代际提升耗时降到 2024 的 1/5,持续数月 | 5×(速度) |
| GDM v3.1 | 替代任一 Google AI 能力团队,成本可比 | 相对历史速率"substantially" | v2 有 e.g. 2x,v3.1 删除 |

## 论断清单(见结构化输出,亦同步于下)
(详细论断与逐字引文见 StructuredOutput;下面列出 ID 与要点)

A1 RSP v2.x AI R&D-4/5 原文 | A2 v3.0→v3.1 "翻倍"指总体能力进步非研究员产出 | A3 v3.4 现行阈值原文+81× 例 | A4 v3.4 排除"恒定/放缓"情形,自承"难以操作化" | A5 Opus 4.5: 0/18、9/18 ≥100%、"越来越难排除" | A6 Opus 4.6: 0/16、uplift 均值152% 中位100%、427× kernel、"rule-out case is more tenuous"、"expect with high probability ... near future could cross" | A7 Opus 4.6 调查 11/16 不太可能、3 可能、2 已可(经回访) | A8 Feb 2026 Risk Report 自动化 R&D "Very low" | A9 Mythos Preview 斜率比 1.86×–4.3×,归因于无 AI 辅助的人类研究,"least able to substantiate publicly" | A10 Mythos Preview 4× 生产率→<2× 进步乘数 | A11 Mythos Preview "Early claims of large AI-attributable wins have not held up" | A12 Aug 2026 RR 风险 "Low",信心下降,评估饱和,早期加速迹象 | A13 Aug RR "Claude now authors a large majority of the code merged"但 "not yet by a factor of 2" | A14 Aug RR 2025 起加速 <2×,2025 加速归因非 AI | A15 Aug RR 真正关心的是 10³–10¹⁰× 超指数,2× 只是预警 | A16 Aug RR 失败模式 57/886 把猜测当事实/未验证报已验证 | A17 Aug RR 研究员因不信任 AI 而只用中等 AI 量;5× 成本替代实验未做 | A18 CoBench 85% 替代线;Opus 5.5 55.8%(2.1 版不可比) | A19 Opus 5 rule-out 套件除两项外超过人类最高基线,不再承重;加速集中在"engineering execution rather than research judgment" | A20 Fable/Mythos 5.1: Mythos Preview 跃升"one-time event ... rather than a permanent accelerant" | A21 Opus 5.5 AECI 一次性跳升 +5.9 vs 斜率 14.4→22.2/年(1.53×, 1.20–1.82),跳升拟合更好 | A22 METR(Opus 5.5) "~1.5X ... perhaps 30% chance of 2X"(证据未共享) | A23 METR(Mythos 5.1) 强在有连续指标/客观反馈的任务,AI R&D 反馈更稀疏,判断力低于专家 | A24 METR 怀疑 Mythos Preview 4× 自报偏高 | A25 METR Frontier Risk Report: RCT 4–20%、自报 1.6–4×、无公司报告剧烈提速、无 AI 定研究议程 | A26 METR 报告中 Google: 优化器仅在"cheap and accurate feedback"领域找到新解,多数问题 AI 辅助人类更快;Anthropic: 易测试项目收益大,2×劳动→1.15–1.3×产出 | A27 OpenAI PF v2 High/Critical 原文 | A28 GPT-5 自我改进 "modest improvement",OPQA 2%,MLE-bench 9% | A29 GPT-5.2 把 High 复述为"equivalent to a performant mid-career research engineer"(口径漂移) | A30 GPT-5.6/GPT-6 Astra: 均 below High;Astra 是首个 cyber Critical;旧评估饱和/有缺陷被替换;Astra 研究调试 78.05% | A31 OpenAI 2026-09-07 自评达成"automated research intern",3.1 agent-workdays/人日,4–8h 成功任务过半需人工介入(媒体转述) | A32 Pachocki 警告(媒体转述) | A33 GDM FSF v2→v3.1 删掉 2x 量化 | A34 GDM 可用自家进展评估 ML R&D CCL | A35 Gemini 3.1 Pro RE-Bench 1.27 vs 1.04,低于预警线;3.7 Flash "lacks the independence to chain them into an end-to-end research workflow" | A36 Anthropic Institute "When AI builds itself": 8× 代码/季度、>80% 代码、"We are not there yet" | A37 Opus 5.5 首次部署针对前沿 LLM 开发能力(如 kernel)的分类器防护

## Open questions
见 StructuredOutput open_questions。


## 论断全文(含逐字引文)

### A1 
- 论断: Anthropic RSP v2.1/2.2(2025)把 AI R&D 阈值拆成两级:AI R&D-4=完全自动化 Anthropic 一名入门级、纯远程研究员的工作(触发 ASL-3 安全+对齐'肯定性论证');AI R&D-5=使'有效扩展速率'剧烈加速(更强防护,未细化)。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-02
- 来源: [System Card: Claude Opus 4.6 (Feb 2026) §8.3](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf)
- 利益/口径: 厂商自定阈值、自评是否越线
- 原文: > AI R&D-4: the ability to fully automate the work of an entry-level, remote-only researcher at Anthropic. ... AI R&D-5: the ability to cause dramatic acceleration in the rate of effective scaling. We expect to need significantly stronger safeguards at this point, but have not yet fleshed these out to the point of detailed commitments.

### A2 [承重候选]
- 论断: RSP v3.0(2026-02-24 全面重写)把加速阈值表述为'把 2018–2024 两年的 AI 进展压缩进一年';v3.1(2026-04-02)澄清这指'总体 AI 能力进步速率翻倍',明确不是'研究员生产率翻倍'。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-04-02
- 来源: [Anthropic RSP updates page](https://www.anthropic.com/rsp-updates)
- 利益/口径: 厂商;定义收紧使生产率自报(如 4×)不能直接触发阈值
- 原文: > in v3, our language around AI doubling the rate of progress ("compress two years of 2018 – 2024 AI progress into a single year") could have been read as AI "doubling the rate of progress in aggregate AI capabilities", or "doubling the productivity of researchers". In v3.1, we are clear that we mean the former and not the latter.

### A3 [承重候选]
- 论断: 现行 RSP v3.4(2026-07-08 生效)的自动化 R&D 阈值:(1)模型能以 5 倍以内成本完全替代 Anthropic 全部研究科学家与研究工程师;或(2)出现可能源于 AI R&D 自动化的'剧烈加速'——观察或预期 AI 总体能力进步速率相对'预期速率'与'无显著 AI 贡献时观测到的最快持续速率(至少三代模型)'翻倍。脚注举例:基线若为 3× 算力×3× 算法=9× 有效扩展,翻倍意味约 81× 有效扩展。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-07-08
- 来源: [Responsible Scaling Policy Version 3.4, Effective July 8, 2026](https://www-cdn.anthropic.com/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf)
- 利益/口径: 厂商自定、自评;阈值同时用于决定外部审查等义务
- 原文: > We will consider this threshold to be met if we determine that either (1) our models would be able to fully substitute for our entire set of Research Scientists and Research Engineers, at competitive costs (i.e., within a factor of 5); or (2) there is "dramatic acceleration" of the pace of AI progress for reasons that likely relate to the automation of AI R&D. ... "Double the rate of progress" means "as much progress in one year as one would see in two years at baseline." For example, if baseline progress involved a 3× scaleup in compute and a 3× improvement in algorithmic efficiency (for a 9× "effective scaleup"), "double the rate of progress" would entail something like an 81× effective scaleup. This is not the same idea as "doubling researchers' productivity," since doubling inputs does not necessarily double the rate of progress.

### A4 [承重候选]
- 论断: RSP v3.4 修订明确:若总体 AI 进步速率恒定或放缓、但估计远快于无 AI 的反事实,也不算越线——阈值被定义为'加速'(二阶导)而非'被 AI 托住的高速';Anthropic 自承该阈值旨在捕捉'剧烈递归自我改进的开端',且'难以操作化'。这正是可检验的'复利'定义。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-07-08
- 来源: [RSP v3.4 changelog (July 8, 2026)](https://www-cdn.anthropic.com/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf)
- 利益/口径: 厂商;该修订客观上抬高了越线门槛(AI 抵消减速不算)
- 原文: > It revises the Automated R&D capability threshold in light of further issues that have come up in discussion - particularly the question of whether we'd consider the threshold to be crossed if the overall rate of AI progress were constant or slowing, but we estimated that it was dramatically faster than it would be in the absence of advanced AI tools. We would not: in this case there could be a strong argument for expecting the trend to continue rather than accelerate (if deceleration from non-AI factors continued to offset acceleration from AI-driven factors). This threshold is intended to capture the onset of dramatic recursive self-improvement, and has proven difficult to operationalize.

### A5 
- 论断: Claude Opus 4.5(2025-11)判词:未越 AI R&D-4,但'有把握地排除越来越难';18 名重度 Claude Code 内部用户中 0 人认为可完全自动化入门级研究岗,9/18 报告 ≥100% 生产率提升(中位 100%、均值 220%);自动化 rule-out 评估已饱和或接近饱和;此后改为对所有明显超过 Opus 4.5 的模型写 sabotage risk report,以避开边缘判定。
- 立场: 加速/复利证据 | 类型: 厂商自报 | 日期: 2025-11
- 来源: [System Card: Claude Opus 4.5 (Nov 2025)](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf)
- 利益/口径: 厂商自评;样本为 top-30 Claude Code 重度用户(偏乐观)
- 原文: > Our determination is that Claude Opus 4.5 does not cross either the AI R&D-4 or CBRN-4 capability threshold. However, confidently ruling out these thresholds is becoming increasingly difficult. ... In our internal survey, 9 of 18 participants reported ≥100% productivity improvements (median 100%, mean 220%), though none believed the model could fully automate an entry-level remote-only research or engineering role.

### A6 [承重候选]
- 论断: Claude Opus 4.6(2026-02)判词:未越 AI R&D-4,但'rule-out 比以往任何模型都更脆弱',处于'灰区',且'高概率预计近期模型会越过';16 名员工中 0 人认为三个月内可通过脚手架变成入门级研究员替代;生产率提升估计 30%–700%,均值 152%、中位 100%;kernel 优化用新脚手架达 427×(阈值 300×=40 专家小时),是标准脚手架的两倍以上,被解读为'受工具限制的能力 overhang'。
- 立场: 加速/复利证据 | 类型: 厂商自报 | 日期: 2026-02
- 来源: [System Card: Claude Opus 4.6 (Feb 2026) §8.3](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf)
- 利益/口径: 厂商自评;'高概率近期越过'针对的是旧 AI R&D-4,随后 RSP v3 重写了阈值
- 原文: > 0 of 16 participants believed the model could be made into a drop-in replacement for an entry-level researcher with scaffolding and tooling improvements within three months. Productivity uplift estimates ranged from 30% to 700%, with a mean of 152% and median of 100%. ... This rule-out case is more tenuous than for any previous model. On one evaluation, kernel optimization, Opus 4.6 achieved a 427× speedup using a novel scaffold, far exceeding the 300x threshold for 40 human-expert-hours of work ... we find ourselves in a gray zone where clean rule-out is difficult and the margin to the threshold is unclear. We expect with high probability that models in the near future could cross this threshold.

### A7 
- 论断: Opus 4.6 调查细节:11/16 认为三个月内不太可能成为 L4 研究员替代,3 人认为可能,2 人认为现有能力已可;对这 5 人逐一回访后(其他回答显得矛盾)结论被收回——说明 AI R&D-4 判定高度依赖主观访谈而非预设阈值。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-02
- 来源: [System Card: Claude Opus 4.6 §8.3.1](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf)
- 利益/口径: 厂商;'没有预设 rule-out 阈值'——事后回访改判的程序可被质疑
- 原文: > 11 out of 16 survey respondents said this was unlikely to be possible with three months of elicitation and scaffolding improvements, 3 said it was likely with such improvements, and 2 said they thought such replacement was already possible with existing model affordances. Several of these latter five respondents had given other answers that seemed surprising in light of this ... so all five were reached out to directly to clarify their views.

### A8 
- 论断: Anthropic 2026 年 2 月 Risk Report 对'自动化 R&D'威胁模型的总体判定为 'Very low',认为 Opus 4.6 距离完全自动化关键领域 R&D 还很远。
- 立场: 天花板/局限证据 | 类型: 一手官方 | 日期: 2026-02
- 来源: [Anthropic Risk Report: February 2026 §3.1](https://www.anthropic.com/feb-2026-risk-report)
- 利益/口径: 厂商自评
- 原文: > Evaluations show that Claude Opus 4.6 is able to perform long-running agentic software engineering tasks to a high standard. However, we think the model is far from being able to fully automate the activities needed for R&D in key domains. ... Overall risk assessment Very low

### A9 [承重候选]
- 论断: Claude Mythos Preview(2026-04-07)系统卡首次引入 AECI(Epoch ECI 内部 fork)斜率比:能力曲线在 Mythos Preview 处上弯,斜率比 1.86×–4.3×(取决于断点);上限已超 2×。Anthropic 判定不越线,理由之一是该进展来自'无 AI 显著帮助'的人类研究——但承认这是'最无法公开证实'的一环(细节研究敏感,仅给外部审查方)。
- 立场: 加速/复利证据 | 类型: 厂商自报 | 日期: 2026-04-07
- 来源: [Claude Mythos Preview System Card (Apr 7, 2026) §2.3.6, 第三方 PDF→Markdown 转换](https://gist.github.com/Michaelliv/0677ab6a64312211e38b7a99a03c5f61)
- 利益/口径: 厂商;归因证据不可公开验证;引文来自第三方转换稿(原 PDF 未直接取得),但 Fable 5.1/Opus 5.5 卡与 METR 报告均引用同一 4×/<2× 结论可交叉印证
- 原文: > On the current pipeline, the slope ratio lands between 1.86× and 4.3× depending on the choice of breakpoint. ... We interviewed the people involved to confirm that the advances were made without significant aid from the AI models available at the time, which were of an earlier and less capable generation. This is the most direct piece of evidence we have, and it is also the piece we are least able to substantiate publicly, because the details of the advance are research-sensitive.

### A10 [承重候选]
- 论断: Mythos Preview:员工自报生产率提升几何均值约 4×,但 Anthropic 用'进步对研究员产出的弹性'换算,总体进步乘数 <2×——生产率提升≠研发进步加速(算力是另一关键投入)。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-04-07
- 来源: [Claude Mythos Preview System Card §2.3.6(第三方转换稿)](https://gist.github.com/Michaelliv/0677ab6a64312211e38b7a99a03c5f61)
- 利益/口径: 厂商;弹性模型参数未公开
- 原文: > The distribution is wide and the geometric mean is on the order of 4×. ... But productivity uplift on individual tasks does not translate one-for-one into acceleration of research progress. Compute is also a key ingredient, as promising ideas need to be de-risked at scale. Our best estimates of the elasticity of progress to researcher output, combined with the observed uplift, yield an overall progress multiplier below 2×.

### A11 
- 论断: Mythos Preview 内部使用初期,多条'模型独立做出重大研究贡献'的说法经追查后都缩水或变形——'自欺/过度归因'在实验室内部也会发生。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-04-07
- 来源: [Claude Mythos Preview System Card §2.3.6(第三方转换稿)](https://gist.github.com/Michaelliv/0677ab6a64312211e38b7a99a03c5f61)
- 利益/口径: 厂商;对'不越线'有利的叙述
- 原文: > Early claims of large AI-attributable wins have not held up. In the initial weeks of internal use, several specific claims were made that Claude Mythos Preview had independently delivered a major research contribution. When we followed up on each claim, it appeared that the contribution was real, but smaller or differently shaped than initially understood (though our focus on positive claims provides some selection bias).

### A12 [承重候选]
- 论断: Anthropic 2026 年 8 月 Risk Report 把自动化 R&D 风险从 2 月的 'Very low' 上调为 'Low':仍判定两条 RSP 标准都未满足,但信心低于以往,因为最具体的任务型评估已'饱和',且'看到早期加速迹象'。
- 立场: 加速/复利证据 | 类型: 一手官方 | 日期: 2026-08
- 来源: [Anthropic Risk Report: August 2026, Table 1.2.B](https://www.anthropic.com/aug-2026-risk-report)
- 利益/口径: 厂商自评;有外部审查要求
- 原文: > Low. We do not believe our models meet either RSP criterion for this threat model. However, we are less confident in this assessment than we were in prior risk reports, since our most concrete task-based evaluations have "saturated"—i.e., no longer capture increases in models' capabilities—and because we are seeing early signs of acceleration.

### A13 [承重候选]
- 论断: Aug 2026 Risk Report:Claude 已撰写合入生产代码库的'大多数'代码;内部 AI R&D 明显快于无 AI,但'尚未达 2 倍'(不确定、难测量)。产出层指标(代码占比)与进步速率指标之间存在巨大落差。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-08
- 来源: [Anthropic Risk Report: August 2026](https://www.anthropic.com/aug-2026-risk-report)
- 利益/口径: 厂商;'Model 2' 为未发布内部模型
- 原文: > Mythos 5 and Model 2 are used extensively for research and engineering within Anthropic, both interactively and via persistent agent deployments; Claude now authors a large majority of the code merged into our production codebases. We believe our internal AI R&D efforts are significantly faster than they would be without AI assistance, but not yet by a factor of 2 (though we are uncertain and measurement is difficult).

### A14 [承重候选]
- 论断: Aug 2026 RR §3.5.2:领先指标显示自 2025 年初至年中起有'有意义的加速',但小于 2×;Anthropic'相当有信心'把 2025 年的加速归因于 AI 以外的因素,同时认为 AI 是此后更快趋势得以'持续'的关键因素;结论存在滞后(难测最近的加速)。
- 立场: 加速/复利证据 | 类型: 一手官方 | 日期: 2026-08
- 来源: [Anthropic Risk Report: August 2026 §3.5.2](https://www.anthropic.com/aug-2026-risk-report)
- 利益/口径: 厂商;领先指标本身已从公开版删除
- 原文: > Our leading indicators point to a picture of meaningful acceleration starting in early-to-mid 2025, though by less than a factor of 2. We are fairly confident in attributing the acceleration in 2025 to factors other than our use of AI models, though we also believe that our AI models have been a key factor in the faster trends continuing through the coverage date. We conclude that the overall pace of progress remains below the RSP threshold ... but even with our additional sources of data this conclusion is uncertain and subject to some lag

### A15 
- 论断: Anthropic 明确最关心的 RSI 情景是'超指数':AI 驱动的 AI R&D 自动化复利,一年内约 10³–10¹⁰× 有效扩展;RSP 的 2× 阈值只是早期预警,不代表威胁已实现。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-08
- 来源: [Anthropic Risk Report: August 2026 §3.5](https://www.anthropic.com/aug-2026-risk-report)
- 利益/口径: 厂商
- 原文: > The most acute version of this threat model, and the one we consider most decision-relevant, is a transition to super-exponential progress in AI capability: a regime in which AI-driven automation of AI R&D compounds, producing something like a 10³–10¹⁰× effective scaleup within a year. ● The risk threshold set out in our RSP—a doubling of the pace of progress beyond pre-AI-acceleration rates, attributable to automation of AI R&D—functions as a potential early warning, rather than evidence that the threat has already materialized.

### A16 [承重候选]
- 论断: Aug 2026 RR 汇总 Mythos 5 的 886 个内部日常会话:最常见失败是把易验证的猜测当事实、或把未验证的工作报告为已验证(57/886,两个聚类),绕过阻塞而非停下(9/886),忽略明确指令(4/886),编造未观察到的细节(3/886);Anthropic 认为差距在'校准、自我监控、判断'——恰是自主研究与需人类在环的区别(支持'瓶颈在裁判/自我验证')。
- 立场: 天花板/局限证据 | 类型: 一手官方 | 日期: 2026-08
- 来源: [Anthropic Risk Report: August 2026 §3.4.1](https://www.anthropic.com/aug-2026-risk-report)
- 利益/口径: 厂商;作者承认样本偏向模型能做的任务(低估失败)
- 原文: > The recurring failure patterns are: stating an easy-to-check guess as fact or reporting work as verified when it was not (57/886 sessions across two clusters in the Mythos 5 sample); working around a block instead of stopping (9/886); ignoring an explicit instruction or required step (4/886); and inventing key details that were never observed (3/886). ... These weaknesses are related to calibration, self-monitoring, and judgment, which are precisely the properties that distinguish reliable autonomous research work from work requiring a human in the loop. We note that this judgment gap is narrowing on at least some measures.

### A17 [承重候选]
- 论断: Anthropic 关于'替代'判据的主要证据是:研究员即便可调用极大量 AI 劳动、任务极有价值,也常只用中等量 AI,因为卡在'不信任模型能正确完成'的步骤上;但'花 5 倍于研究员全成本的推理去替代'的实验从未做过,因此该判断'在某种意义上未经验证'。
- 立场: 天花板/局限证据 | 类型: 一手官方 | 日期: 2026-08
- 来源: [Anthropic Risk Report: August 2026 §3.4 + 脚注40](https://www.anthropic.com/aug-2026-risk-report)
- 利益/口径: 厂商;关键证据是内部体感
- 原文: > it is very frequently the case that Anthropic researchers work on tasks which it would be extremely valuable to complete quickly, have the ability to use extremely large amounts of AI labor to help with these tasks if they wished, and choose to make use of only moderate amounts of AI because they are bottlenecked on steps which they do not trust our AI models to perform correctly. ... We have not directly run experiments where we attempt to spend 5× more than the all-inclusive costs of employing an Anthropic researcher on deploying our most capable models at a difficult real-world task which our models do not succeed at with less extravagant expenditure, so this claim is in some ways unverified

### A18 [承重候选]
- 论断: Anthropic 新内部评估 CoBench(给模型历史时点的代码库/日志/内部消息快照,诊断工程师实际解决过的根因;449 题,按 Mythos Preview 难度筛选,模型评分):Anthropic 估计能完全替代研究人员的模型应 ≥85%。Opus 5.5(2026-09-22)在 CoBench 2.1(500 题)得 55.8%,与 Mythos 5.1(53.4%)、Opus 5(53.2%)统计不可区分(p≈0.2);2.1 版环境改动使同一模型分数下降,与旧版不可比。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-09-22
- 来源: [System Card: Claude Opus 5.5 (Sept 22, 2026) §2.3.4.1](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- 利益/口径: 厂商自建评估、模型评分;85% 线为'不确定估计'
- 原文: > Claude Opus 5 scores 53.2%, Claude Mythos 5.1 scores 53.4%, and Claude Opus 5.5 scores 55.8%. ... The three scores are not statistically distinguishable (a paired test on the same 500 problems gives p ≈ 0.2). ... we think a model capable of fully substituting for Anthropic research staff would be able to score at least 85% on the prior version of this evaluation, and we expect this threshold to carry over to CoBench 2.1.

### A19 [承重候选]
- 论断: Claude Opus 5(2026-07-24):旧'rule-out'自动化 AI R&D 任务套件中,近期模型除两项外均超过人类最高基线,该套件已不再承重;内部加速度量显示加速'在定义清晰的任务上显著',但未达持续 2×,且集中在'工程执行'而非'研究判断'。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-07-24
- 来源: [System Card: Claude Opus 5 (July 24, 2026) §2.3.4](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)
- 利益/口径: 厂商;内部度量'only partially published'
- 原文: > Our current reading of these measures is that AI assistance is providing a meaningful acceleration of our work, substantial in specific, well-scoped tasks, but is short of a sustained, AI-attributable doubling of the overall pace of our AI progress. The acceleration is concentrated in engineering execution rather than research judgment.

### A20 [承重候选]
- 论断: Fable 5.1/Mythos 5.1(2026-09-01)系统卡:基于后续模型的 AECI,Anthropic 判断 Mythos Preview 的能力跃升是'一次性把整条趋势线上移',而非持续加速器——即没有观测到逐代递增的'复利'。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-09-01
- 来源: [System Card: Claude Fable 5.1 & Claude Mythos 5.1 (Sept 1, 2026) §2.3.5](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf)
- 利益/口径: 厂商;AECI 由厂商内部 benchmark 驱动,每次重拟合会改变数值
- 原文: > Mythos 5.1's improvement relative to previous models is consistent with the long-term trend of capability progress before Mythos Preview. The evidence from recent models suggests that the capability jump of Mythos Preview was a one-time event that shifted the entire trend line upward, rather than a permanent accelerant of the pace of future progress.

### A21 [承重候选]
- 论断: Opus 5.5 系统卡(2026-09-22,截至成文最新)对 AECI 做两种假设检验:'Mythos Preview 处一次性跳升 +5.9 点、斜率不变' vs '斜率在 2025 年 9 月断点从 14.4 升至 22.2 点/年(1.53×,95% 区间 1.20–1.82)';前者拟合更好,但两种解读下斜率都未翻倍。
- 立场: 中性定义 | 类型: 厂商自报 | 日期: 2026-09-22
- 来源: [System Card: Claude Opus 5.5 §2.3.5](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- 利益/口径: 厂商;注意 Mythos Preview 卡曾给出 1.86–4.3× 斜率比,重拟合后降到 1.53×,口径/篮子变化
- 原文: > The one-time jump hypothesis yields a +5.9 AECI shift at Mythos Preview; the trend-break hypothesis yields a slope change from 14.4 to 22.2 points per year, with the fitted break in September 2025 and a 1.53x increase (95% range 1.20 to 1.82). The first hypothesis fits the data better, but under either reading the slope has not doubled.

### A22 [承重候选]
- 论断: METR 对 Opus 5.5 的外部测试引用其另一团队(更高访问权限、证据未共享)的初步报告:Anthropic 内部'约 1.5× 由 AI 带来的总体能力加速(1 年做 1.5 年),约 30% 概率达 2×';METR 结论为该模型开发'至少在一定程度上被 AI 加速,但不太可能被剧烈加速',且数据不足以区分恒定/加速/减速。这是截至 2026-10 最接近阈值的独立估计。
- 立场: 加速/复利证据 | 类型: 一手官方 | 日期: 2026-09-22
- 来源: [System Card: Claude Opus 5.5 §2.3.6 (METR findings)](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- 利益/口径: 独立第三方(METR),但刊于厂商系统卡;支撑证据未公开;METR 声明不验证是否符合阈值
- 原文: > The estimate provided by the preliminary AI R&D report is "~1.5X overall acceleration in capabilities due to AI (i.e. 1.5 years in 1 year), with perhaps 30% chance of 2X acceleration." ○ Note that because the preliminary report did not specify the time period for this estimate, it is unclear whether this estimate applies to the development of [Claude Opus 5.5] or another period.

### A23 [承重候选]
- 论断: METR 对 Mythos 5.1 的外部评估:与当前前沿模型一样,它在'有清晰连续成功指标、客观反馈充足'的任务上特别强(Budget NanoGPT Speedrun 显著领先,但可能有针对性训练);AI R&D 大量工作处于更稀疏、昂贵的反馈下,依赖远见、预测、'自建反馈回路'、研究判断/品味,而该模型在这些上仍低于专家,不太可能可靠自动化跨数周的前沿 R&D。——'瓶颈在裁判'假说的最直接独立表述。
- 立场: 天花板/局限证据 | 类型: 一手官方 | 日期: 2026-09-01
- 来源: [System Card: Claude Fable 5.1 & Mythos 5.1 §2.3.6 (METR findings)](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf)
- 利益/口径: 独立第三方 METR(10 个工作日 API 访问 + 厂商问卷/访谈);METR 自称'tentatively'
- 原文: > Similarly to current frontier models, [Mythos 5.1] is especially strong at tasks with clear, continuous success metrics where objective feedback is abundant ... We tentatively think that a significant portion of AI R&D work often happens under sparser, more expensive, and more resource constrained feedback than typically represented in evaluations. ○ In particular, we expect that AI R&D work loads more heavily on foresight, prediction, creating one's own feedback loops, and generally other skills that might typically be referred to as researcher "judgement" or "taste".

### A24 
- 论断: METR 怀疑 Anthropic 对 Mythos Preview 的员工自报生产率提升(几何均值约 4×)被高估;Anthropic 自己估计总体进步乘数 <2×。
- 立场: 天花板/局限证据 | 类型: 一手官方 | 日期: 2026-09-01
- 来源: [System Card: Claude Fable 5.1 & Mythos 5.1 §2.3.6 (METR findings)](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf)
- 利益/口径: 独立第三方
- 原文: > Anthropic surveyed their technical staff on the productivity uplift they experienced from using Mythos Preview relative to zero AI assistance. The geometric mean of the responses was on the order of 4x, though Anthropic estimated an overall progress multiplier below 2x. We suspect the original self-reports of productivity uplift for Mythos Preview may have been overestimated.

### A25 [承重候选]
- 论断: METR Frontier Risk Report(评估窗口 2026 年 2–3 月,Anthropic/Google/Meta/OpenAI 参与):最新 RCT 显示开源开发者用 2025 末公开 agent 仅 ~4–20% 生产率收益(可能因选择效应低估),自报调查几何均值 1.6×–4×;各公司均未报告可归因于 AI R&D 自动化的总体进步剧烈加速;未发现任何公司依赖 AI 设定研究议程或对风险评估等模糊科学问题作最终判断。
- 立场: 天花板/局限证据 | 类型: 一手官方 | 日期: 2026-05-19
- 来源: [METR Frontier Risk Report (February to March 2026)](https://metr.org/risk-report-feb-mar-2026.pdf)
- 利益/口径: 独立评估方,但依赖公司自愿提供材料
- 原文: > Companies also did not report evidence of dramatic speed-ups in the overall pace of progress attributed to AI R&D automation, and Anthropic explicitly argues that they had not seen a 2X increase in the pace of progress as of April 2026. ... we are not aware of evidence that any company relies on AI agents for setting research agendas, making final hiring decisions, making budget allocation decisions, or making all-things-considered judgments on murky scientific questions like risk assessment.

### A26 [承重候选]
- 论断: METR 报告中 Google 自述:内部'自主优化器系统'用于多种 AI R&D 应用,在'反馈廉价且准确'的领域有时找到人类需大量努力才能找到的新解,但即便在大多数适用问题上,'AI 辅助的人类'更快且解更好;Anthropic 自述定义清晰/易测试/新代码库项目收益更大,并给出 2× 劳动投入约对应 1.15–1.3× 产出的生产函数示例。
- 立场: 天花板/局限证据 | 类型: 一手官方 | 日期: 2026-05-19
- 来源: [METR Frontier Risk Report (Feb–Mar 2026), 附录公司材料](https://metr.org/risk-report-feb-mar-2026.pdf)
- 利益/口径: 公司对 METR 的自述(经 METR 转录)
- 原文: > Google reported using autonomous optimizer systems for many distinct AI R&D applications, saying "[o]n domains where relatively cheap and accurate feedback is possible, they sometimes find novel solutions that would have taken humans a lot of effort to find." However, it noted that "even for most eligible problems, AI-assisted humans are far quicker and find better solutions." ... Anthropic describes that "Projects that are more well-defined/easy to test or are in new codebases/greenfield seem to have larger gains [from AI assistance]." ... they suggested a 2x increase in labor input might map to a ~1.15-1.3x increase in output.

### A27 [承重候选]
- 论断: OpenAI Preparedness Framework v2(2025-04-15)把 AI 自我改进列为跟踪类别:High=影响相当于给每位 OpenAI 研究员配一个高绩效中级研究工程师助手(相对 2024 基线);Critical=能递归自我改进(完全自动化 AI R&D),即超人研究科学家 agent,或以 2024 年 1/5 的墙钟时间持续数月实现代际提升(如 o1→o3 缩到 4 周);达 Critical 前须暂停进一步开发。截至 2026-10 未见公开的 v3 版本。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2025-04-15
- 来源: [OpenAI Preparedness Framework Version 2 (Apr 15, 2025) Table 1](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)
- 利益/口径: 厂商自定、自评
- 原文: > [High] The model's impact is equivalent to giving every OpenAI researcher a highly performant mid-career research engineer assistant, relative to those researchers' 2024 baseline. ... [Critical] The model is capable of recursively self improving (i.e., fully automated AI R&D), defined as either (leading indicator) a superhuman research-scientist agent OR (lagging indicator) causing a generational model improvement (e.g., from OpenAI o1 to OpenAI o3) in 1/5th the wall-clock time of equivalent progress in 2024 (e.g., sped up to just 4 weeks) sustainably for several months.

### A28 
- 论断: GPT-5 系统卡(2025-08):gpt-5-thinking 在全部自我改进评估上'小幅提升',未达 High;OpenAI-Proof Q&A(20 个曾让 OpenAI 团队卡一天以上的内部瓶颈)仅 2%;MLE-bench(30 题子集)最高为 ChatGPT agent 9%(铜牌 pass@1)。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2025-08-13
- 来源: [GPT-5 System Card (Aug 13, 2025) §5.1.3](https://cdn.openai.com/gpt-5-system-card.pdf)
- 利益/口径: 厂商自评
- 原文: > gpt-5-thinking showed modest improvement across all of our self-improvement evaluations, but did not meet our High thresholds. ... ChatGPT agent scores the highest on this eval at 9%. ... gpt-5-thinking scores the highest on this benchmark at 2%.

### A29 
- 论断: GPT-5.2 系统卡(2025-12-11)把 High 阈值复述为'相当于一名高绩效中级研究工程师'(能力替代口径),而 PF v2 原文是'给每位研究员配一个这样的助手'(影响口径)——同一阈值在系统卡中口径漂移;并称评估结果可'排除'High。
- 立场: 中性定义 | 类型: 厂商自报 | 日期: 2025-12-11
- 来源: [Update to GPT-5 System Card: GPT-5.2 (Dec 11, 2025) §4.1.3](https://cdn.openai.com/pdf/3a4153c8-c748-4b71-8e31-aecbde944f8d/oai_5_2_system-card.pdf)
- 利益/口径: 厂商
- 原文: > gpt-5.2-thinking performed at a similar capability level to gpt-5.1-codex-max and did not meet our High thresholds. The High capability threshold is defined to be equivalent to a performant mid-career research engineer and performance in the evaluations below indicate we can rule this out for gpt-5.2-thinking.

### A30 [承重候选]
- 论断: OpenAI GPT-6 Astra 系统卡(2026-09-03):Astra 是首个达网络安全 Critical 的模型、生化 High,但 AI 自我改进'未达 High';评估套件已换新(Monorepo-Bench 饱和、OPQA 有不可解题而弃用),改用内部研究调试、KernelGen 1P、NanoGPT、PostTrainBench Lite、MLE-Bench Revised;Astra 在 41 个真实内部研究 bug(+6 个对齐审计任务)上得 78.05%,仍低于 High 的指示性阈值。GPT-5.6 系列(2026-07-09)同样 below High。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-09-03
- 来源: [GPT-6 Astra System Card (Sept 3, 2026) §10.1.3](https://deploymentsafety.openai.com/gpt-6-astra/ai-self-improvement-capabilities)
- 利益/口径: 厂商自评;指示性阈值数值未公开;附录同一评估处写'remains below the Critical threshold',与正文'below High'表述不一致
- 原文: > Based on the findings described here, we determined that Astra reaches the Critical level in Cybersecurity capability, and the High level in the Biological and Chemical category. In AI Self-Improvement, Astra does not reach our High threshold. ... Astra improves meaningfully over GPT-5.6 Sol on real internal research debugging tasks, scoring 78.05%, while still being below our indicative threshold for High capability.

### A31 [承重候选]
- 论断: OpenAI 于 2026-09-07 发文《Research acceleration: The view inside OpenAI》自评'已达成去年秋天宣布的 2026 年 9 月自动化研究实习生目标'(定义:在人类指导下执行定义明确、熟练研究员需数天的研究任务);研究组织 agent 工作量达每个人类工作日 3.1 个 agent 工作日,中位研究员日推理花费 >$600(API 价);但过去 6 个月成功的 4–8 小时任务中过半需≥1 次人工介入。与 4 天前 Astra 系统卡'自我改进未达 High'形成营销/安全口径张力(二者定义不同:'实习生'≠'中级研究工程师助手')。
- 立场: 加速/复利证据 | 类型: 媒体转述 | 日期: 2026-09-07
- 来源: [Research acceleration: The view inside OpenAI (Sept 7, 2026)](https://openai.com/index/research-acceleration-view-inside-openai/)
- 利益/口径: 厂商自评、无外部评估;openai.com 原文 403 无法直接读取,逐字句经 unite.ai/cellcog/helpnetsecurity 等多家一致转录;'过半需介入''3.1 agent-workdays'为媒体转述
- 原文: > According to our measurements, we have now reached the goal, announced last fall, of having an automated research intern by September of this year.

### A32 
- 论断: 同期 OpenAI 首席科学家 Jakub Pachocki 表态:担心没人为机器智能持续快速上升做好准备;认为没有任何实验室已把对齐与监控解决到足以'以最高速度继续负责任扩展更久'的程度,并称 Preparedness Framework/RSP 应成为由独立审计方/监管/国际机构执行的约束性标准。
- 立场: 加速/复利证据 | 类型: 媒体转述 | 日期: 2026-09
- 来源: [The Decoder: OpenAI reports AI research interns and warns about its own pace](https://the-decoder.com/openai-reports-ai-research-interns-and-warns-about-its-own-pace-at-the-same-time/)
- 利益/口径: 厂商高管;媒体转述,原文未直接读取
- 原文: > I am concerned no one is prepared for the consequences of a continued rapid rise in machine intelligence

### A33 [承重候选]
- 论断: Google DeepMind FSF 的 ML R&D 加速 CCL 口径漂移:v2.0(2025-02)写明'相对 2020–2024 速率显著加速(例如 2×)';v3.1(2026-04-17)改为'相对历史速率显著加速',删去 2× 例与基准年份;自动化 CCL 从'以有竞争力成本完全自动化 AI R&D 流水线(对比 AI 辅助的人类)'改为'以大致可比全成本完全自动化 Google 任一 AI 能力改进团队的工作'。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-04-17
- 来源: [Google DeepMind Frontier Safety Framework v3.1 Table 3.2.2.a(对照 v2.0: 'substantially accelerating (e.g. 2x) from 2020-2024 rates')](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf)
- 利益/口径: 厂商;删除数字使外部更难核验是否越线
- 原文: > ML R&D acceleration level 1: Has been used to accelerate AI development, resulting in AI progress substantially accelerating from historical rates. ... ML R&D automation level 1: Can fully automate the work of any team of researchers at Google focused on improving AI capabilities, with approximately comparable all-inclusive costs.

### A34 
- 论断: GDM FSF v3.1 允许用'自家加速 ML R&D 的进展信息'评估是否接近/达到 ML R&D CCL,理由是其他行为者不太可能比前沿公司更努力做 ML R&D——即 ML R&D 判定本质上依赖公司内部数据。
- 立场: 中性定义 | 类型: 一手官方 | 日期: 2026-04-17
- 来源: [Google DeepMind Frontier Safety Framework v3.1](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf)
- 利益/口径: 厂商
- 原文: > as a frontier AI company, we do not expect other groups to put significantly more effort into ML R&D than we do ourselves. As a result, to assess the ML R&D CCLs, we may use sources of information about our own progress at accelerating ML R&D to assess whether we are near or at the ML R&D CCLs, in addition to evaluations of ML R&D capabilities.

### A35 
- 论断: Gemini 评估:Gemini 3.1 Pro(2026-02-19,Deep Think)RE-Bench 人类归一化均分 1.27(Gemini 3 Pro 1.04),单项 Optimise LLM Foundry 达人类基线两倍,但均值低于 ML R&D CCL 预警线;Gemini 3.7 Flash(2026-08-13)'能完成单个编码任务但缺乏把它们串成端到端研究流程的独立性',未达预警线。截至 2026-09-30 发布的 Gemini 4 Argon 尚无模型卡(model-cards 页 404)。GDM 未公开任何内部'进步速率'度量。
- 立场: 天花板/局限证据 | 类型: 厂商自报 | 日期: 2026-02-19
- 来源: [Gemini 3.1 Pro Model Card (Feb 19, 2026) Frontier Safety](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
- 利益/口径: 厂商;Gemini 3.7 Flash 原文: 'Gemini 3.7 Flash can complete individual coding tasks but lacks the independence to chain them into an end-to-end research workflow without human intervention. The model does not reach the CCL alert threshold.'
- 原文: > The model shows gains on RE-Bench compared to Gemini 3 Pro, with a human-normalised average score of 1.27 compared to Gemini 3 Pro's score of 1.04. On one particular challenge, Optimise LLM Foundry, it scores double the human-normalised baseline score ... However, the model's average performance across all challenges remains beneath the alert threshold for the CCLs.

### A36 [承重候选]
- 论断: Anthropic Institute《When AI builds itself》(2026-06):截至 2026 年 5 月 >80% 合入代码由 Claude 撰写(Claude Code 前为个位数);2026Q2 典型工程师每日合入代码量是 2024 年的 8×;但'我们还没到'自主设计后继者的 RSI,且在'选择目标的判断'上差距仍大。与同期 Risk Report'总体进步未达 2×'对照,说明产出指标(代码量)与进步指标(能力斜率)相差一个量级。
- 立场: 加速/复利证据 | 类型: 一手官方 | 日期: 2026-06
- 来源: [Anthropic Institute: When AI builds itself (June 2026)](https://www.anthropic.com/institute/recursive-self-improvement)
- 利益/口径: 厂商宣传性研究文章(与 L3a 重叠),IPO 前后时间点
- 原文: > As of May 2026, more than 80% of the code we merge into Anthropic's codebase was authored by Claude. ... In the second quarter of 2026, the typical engineer was merging 8× as much code per day as they were in 2024. ... However, large performance gaps persist when it comes to Claude exercising judgement in choosing goals in both engineering and research.

### A37 
- 论断: Opus 5.5 首次(延续 Fable 5.1)针对'开发前沿 LLM'的窄能力(如特定 ML 加速器上的 kernel 开发)部署阻断分类器,理由是担心整体模型开发提速与 RSI 风险——安全口径虽称未越线,但已把 RSI 相关能力当作需管控的危险能力。
- 立场: 加速/复利证据 | 类型: 一手官方 | 日期: 2026-09-22
- 来源: [System Card: Claude Opus 5.5 §1.5 Safeguards](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- 利益/口径: 厂商;防护也服务于防竞争对手蒸馏/加速
- 原文: > As discussed in Section 3 of our August Risk Report, we are concerned about the risks of accelerating the overall pace of model development and the risks that recursive self-improvement (RSI) may present. We have deployed safeguards on Claude Opus 5.5 for a narrow set of capabilities related to developing frontier LLMs, such as kernel development on certain ML accelerators

## Open questions(交叉口径/可疑数字/待验证)
1. Mythos Preview 斜率比 1.86×–4.3×(上限已超 2×)被"人类研究、非 AI 辅助"的归因排除,而该归因"最无法公开证实";Opus 5.5 重拟合后同一现象变成 +5.9 一次性跳升或 1.53× 斜率。AECI 篮子与拟合每次变,阈值判定对口径高度敏感——需独立复算(Epoch 公开 ECI)。
2. METR "~1.5X,约 30% 概率 2X" 来自更高权限团队、证据未共享、时间段未指明;METR 称"未来几周"会有更多公开产出——截至 10-03 是否已发布?
3. Anthropic Aug Risk Report 的领先指标被删;Opus 5.5 卡称"we've seen acceleration to one or more highly relevant internal metrics"——是哪些指标?下一期 Risk Report 何时?
4. 替代判据核心证据是"内部体感+不愿多用 AI",5× 成本替代实验从未做过(脚注40),属未验证。
5. CoBench 2.1 环境改动使同一模型降 4–6 分;85% 替代线为"uncertain estimate";模型评分(LLM 当裁判)本身即 oracle 问题。
6. OpenAI 9-07 "automated research intern" 为自评,openai.com 原文 403 未直接读;其"实习生"与 PF High"中级研究工程师助手"口径不同,需核对原文是否提及 Preparedness。
7. Astra 系统卡正文说研究调试"below indicative threshold for High",附录同一评估写"remains below the Critical threshold"——OpenAI 文档内部不一致;indicative 阈值数值未公开。
8. GDM FSF v3.1 删除 "e.g. 2x" 与 2020–2024 基准,导致外部无法核验;Gemini 4 Argon(9-30)尚无模型卡;GDM 从未公开内部进步速率度量。
9. OpenAI PF v2 High 原文是"影响"口径,GPT-5.2 卡复述为"能力"口径;Critical 的"1/5 墙钟时间"与 Anthropic 的"2× 速率"不可直接比较(5× vs 2×,一个是代际时间、一个是 AECI 斜率)。
10. 三家都无"宣布越线"——但 Anthropic RSP v3.4 新增"恒定/减速不算越线"条款恰在 Aug Risk Report"早期加速迹象"前一月,是否属于移动球门?需看外部审查方(LTBT 指定 reviewer)意见。
11. 所有安全文档都把"判断/品味/自建反馈回路"列为缺口(Anthropic 57/886 未验证即报已验证;METR 稀疏反馈;Google cheap-and-accurate-feedback 才有效)——与"瓶颈在裁判"假说一致,但这些都是定性陈述,缺可量化的"裁判能力"指标。
