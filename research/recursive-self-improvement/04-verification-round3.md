# Round 3 · 单源承重实证双席审计


## R1-anthropic-26pct: Anthropic R&D Automation Index,即截至 2026-08 Claude 在 AL4「leads」级别承担模型研发工作的 26% — 反证搜索席
**判定**:降级为弱结论

**发现**:
搜索角度与结果:
1) 原文核对(anthropic.com/institute/measuring-pace-of-ai-development,2026-09-17 发布):确认 26%(截至 8 月)、2 月 <1%、7 月 20% 员工每周抽样、约 15,000 任务、judge 精确一致 59%(人-人 35%)、一级内 97%、使用 Epoch AI 的 AL 量表。需要修正或无法核实的几处:(a) 原文写的是 542 节点的树,其中 378 个是叶节点,文章只写「378 叶类」没错,但最好补上树的结构;(b) 正文全文检索不到 "interval/uncertainty/90%",所以「90% 区间约 21–33%」最多只在图里出现,我没法从文本核实;(c) 各月数值中,只有 5 月 12%、7 月 22% 被二手报道转述,3 月 1% 只出现在一条二手标题里("Up From 1% in March"),4 月 3%、6 月 14% 没找到任何文本佐证;(d)「3–6 月用冻结的 7 月篮子回溯评分」:原文的说法是评某个月时 rater agent 只能看到该月及以前的证据;做稳定性检验时,另外用 2026-01 的数据建了一棵替代树,拿来对照 2–7 月新出现的任务。原文没有用「回溯」这个词。机制的大意没写错,但措辞应该照原文改。
2) 独立复现:没找到。没有任何第三方用独立数据测过 Anthropic 内部的这个份额。原文自己也说外部评估员只是计划("plan to embed independent third-party evaluators"),不是已经做了的事。METR 以前只对其离线监控平台做过红队测试,没有核对过这个指数。
3) 二手报道(implicator、FourWeekMBA、miraflow、aistop.watch、betanews、resultsense 等):都只是转述同一份数据,不算复现。implicator 指出了几点方法问题:评分基本由 Claude 自己完成(研究 agent 加 Claude judge),有循环评估的嫌疑;judge 可能和被测模型犯同类错误;任务是事后从 Slack/文档里重建的;外部没人核对过。
4) LessWrong(Alvin Ånestrand,2026-09-22)做外推预测,用的也全是 Anthropic 自家数据。他提醒 AL3、AL4、AL5 是累积曲线,彼此不独立,看逐月的相对变化比看绝对值可靠。
5) 其他实验室有没有可比的独立测量:OpenAI 的「Research acceleration: the view inside OpenAI」(2026-09)报告,8 月中研究部门每个人类工作日对应 3.1 个 agent 工作日,6 月以前还不到 1:1;4–8 小时的成功任务中过半至少有一次人类介入。这是独立机构、独立数据,方向一致(2026 年夏天内部 agent 化急剧加速),但指标是运行时长,不是「AI 主导的人时份额」,不能当作对 26% 的数值复现。另外原页面返回 403,我是通过二手摘要读到的。Google DeepMind:没搜到任何内部份额数据。
6) METR(Frontier Risk Report,2026-05-19;技术人员调查):自报的提升 1.4–2x 或 1.6–4x;METR 自己的 RCT 用的是 2025 年底的公开 agent,只测到约 4–20% 的提升。他们提醒自报数据历史上一直偏高,并提到 Anthropic 自己说截至 2026 年 4 月没观察到 2 倍的进展速度。这是一条独立的、方向偏保守的证据,但时间更早、测的也不是同一个量,构不成直接矛盾。
7) Epoch AI 访谈(8 位研究员,较早)和 GovAI 的 Chan 等「Measuring AI R&D Automation」(arXiv 2603.03992)都是框架或预期,没有测量值。
8) 没搜到的方向:针对 26% 的正式学术反驳;Anthropic 员工的独立调查;用 PR 合并、算力等外部可观测代理指标对这条曲线做交叉验证;任何第三方审计。
方法学问题汇总:单一机构、单一数据源;测量工具就是被测对象(Claude 抽任务、Claude 评级);人-人一致率只有 35%,说明构念本身就很模糊;AL4 的门槛定义直接决定百分比;冻结的篮子会漏掉新出现的工作类型;没有公布可在文本中核实的不确定性区间;未来「re-version」可能会改写历史数值。

**可安全写入**:Anthropic 2026 年 9 月发布了自测的原型「R&D Automation Index」(借用 Epoch AI 的自动化等级量表)。按它的估计,截至 2026 年 8 月,Claude 在「主导」级(AL4,人类只设定目标、审查结果)完成的工作约占其模型研发人时的 26%,而 2 月还不到 1%;5 月约 12%,7 月约 22%。这些评级主要由 Claude 自己的研究 agent 和 judge 模型给出,judge 与员工的精确一致率为 59%,员工彼此之间只有 35%。目前没有任何独立机构用独立数据复现或核对过这个数字,Anthropic 也只说「计划」引入第三方评估员。它应被视为实验室的自我报告,而不是外部测量。旁证方面,OpenAI 同期独立披露,其研究部门的 agent 工作量在 2026 年夏天超过了人类工时(8 月中约 3.1:1),方向上一致,但指标不同,不能互相印证具体数值。METR 的独立 RCT 和调查则显示,截至 2026 年上半年,实测的生产率提升远小于自报。(不建议写入:4 月 3%、6 月 14% 和「90% 区间 21–33%」,这几项在原文文本和二手来源里都核实不到。)


## R1-anthropic-26pct:Anthropic 原型 R&D Automation Index,2026-08 Claude 处于 AL4「leads」的工作约占模型研发工作 26%,2 月 <1% 起逐月上升 — 方法学审计席(有否决权)
**判定**:降级为弱结论

**发现**:
一手原文:anthropic.com/institute/measuring-pace-of-ai-development,我抓取了三次。下面分「能核实的部分」和「方法学问题」两块。

【能核实的部分】
- 正文有:「prototype」这个定性;Claude「leads」约 26% 的 AI R&D 工作;「collaborates」及以上 >90%;没有 AL5(完全自主)。
- 选样:2026 年 7 月每周按部门随机抽 20% 员工。
- 任务提取:由 Claude 研究 agent 读 Slack 和内部文档,抽出约 15,000 个任务,组成 542 个节点、378 个叶类的任务树,并冻结。
- judge 一致性:与员工精确一致 59%,人与人之间 35%,相差一级以内 97%。
- 回溯规则:评某个月时,只允许看该月及以前的证据。
- 原文另做了一个对照:用 1 月数据建一个替代篮子,结果显示「novel 任务」没有增加。

【正文核不到的部分】
- 「90% 区间约 21–33%」:正文中找不到 interval、bootstrap、uncertainty 等任何不确定性表述。如果这个区间存在,只可能在图里,我无法核实。在文本层面,它不得作为原文给出的数字引用。
- 2 月 <1% 之后的各月值(3 月 1%、4 月 3%、5 月 12%、6 月 14%、7 月 22%):正文没有,只有图中的曲线。这些是读图得到的数,不是原文报告值。
- 发布日期:页面没有写明。「2026-09」这个日期来源不明。页面只写测量时点为 August 2026。

【方法学问题】
1. 循环论证,而且是本研究最大的问题。抽任务的是 Claude agent,给每个任务判 AL 等级的也是 Claude judge,被测对象还是 Claude 自己。原文没有说明 judge 是哪个模型或版本,也没有说明它是否在给自己或后继模型打分。原文自己也承认「the automation ratings depend on the judge model」。
2. judge 的验证很薄。59% 的精确一致听上去高于人与人的 35%,但人与人只有 35% 恰好说明这套 AL 量表的信度很低。至于「相差一级内 97%」,对 AL4 这条边界几乎没有区分力:AL3 和 AL4 彼此正好相差一级,误差可以直接决定 26% 这个数。另外,验证人数、评分条数、怎么选出验证者、是否覆盖各月,全都没有披露。
3. 加权口径被误述了。审稿稿里写的「人时加权」并不是真实工时。原文的做法是:每人每周 1 个单位,平均分给他做过的每个任务。原文自称「crude approximation」。所以 26% 是「人·周等分权重下的份额」,不是工时占比。口径的敏感性没有报告。
4. 回溯评分有偏差。3–6 月(连同 2 月)用的是 7 月冻结的任务篮子,把 7 月的任务分类套到早期月份上。即便证据按时间截断,打分的 judge 依然是后来的模型,带着后来的分类框架。早期月份的 Slack 痕迹稀疏,也可能系统性压低早期值,从而人为放大上升斜率。月度曲线的陡升(<1% 到 26%)恰恰最容易受这种偏差影响。
5. 测量效度存疑。数据只来自 Slack 和文档的文字痕迹,没有提到 IDE 或 agent 日志之类的直接观测。员工在 Slack 里谈论「Claude 干了 X」的倾向本身会随时间变化,也会受内部文化影响。
6. 推断统计缺失。正文没有标准误、区间或抽样设计效应,也没有用独立样本复现。
7. 利益冲突和外部审查。这是开发方测自己产品的数字,且直接关系到自家叙事:展示 AI 研发加速,同时彰显安全治理。没有外部审计,没有同行评审,也没有公开数据或代码。原文自己也提到各家开发者都会倾向于「draw the line generously」。
8. 只有单一来源、单一机构。数字没法外推到「前沿实验室整体」或「RSI 的进度」。AL4 的定义是 Claude 在人监督下完成大部分任务,本身也不等于自我改进闭环。

【判定理由】
不否决:数字确实出自原文,原文也披露了部分验证数据和局限,可以作为「Anthropic 自报的原型估计」引用。
但不可承重:这是一套自评、用模型判模型、回溯打分、加权粗糙、没有不确定性量化、没有外部验证的单一来源度量。文章里任何「RSI 已进展到某程度」的核心论断都不得以它为主要支撑。21–33% 这个区间和各月具体数值不得写成原文数据。

**可安全写入**:Anthropic 在 2026 年发布了一个自称「原型」的 R&D Automation Index。按其自报,2026 年 8 月 Claude 在其内部模型研发工作中「主导」(AL4:人类监督下端到端完成大部分任务)的份额约为 26%,完全自主(AL5)的工作为零;其图示显示这一比例从 2026 年 2 月的不足 1% 升上来。需要注意以下几点:该数字由 Claude agent 从员工 Slack 和文档中提取任务、再由 Claude judge 评级得出;权重是按人·周把份额平均分给各任务的粗略近似,并非实际工时;早期月份是用 7 月冻结的任务篮子回溯评分的;judge 与员工的精确一致率为 59%(员工之间仅 35%);原文没有给出置信区间,也没有经过外部审计。因此,它只能视为一家实验室对自身的初步估计,不能当作 AI 研发自动化程度的独立测量。


## R2-aeci-onetime-jump — 反证搜索席
**判定**:降级为弱结论

**发现**:
Independence check: all three cards (Mythos Preview 2026-04-07, Fable/Mythos 5.1 2026-09-01, Opus 5.5 2026-09-22) come from the same organization, use the same internal AECI fork, and refit the same data. They are one source, not three replications. I found no independent team that refit AECI or reproduced the jump-versus-slope test, and none could, because AECI scores are measured internally and not published.

Search angles and what each found:

1) Epoch's public ECI (independent team, but AECI is a fork of the same method and shares part of the benchmark pool, so it is only partly independent). The data insight "ECI frontier trend" (2026-09-01) puts the frontier since the reasoning era at about 14 points/yr, close to Anthropic's pre-breakpoint 14.4/yr. Mid-2026 models (Opus 5 161.59, GPT-5.6 Sol 161.06, Kimi K3 157.33) sit near the trend line with no new discontinuity. A third-party aggregator snippet gives Opus 5.5 at 167.3 and Fable 5.1 at 164.8 on public ECI as of 2026-10-02; I did not check these numbers against Epoch's own pages. Weak confirmation, in direction only, that the slope has not doubled. Key gap: I found no public ECI score for Mythos Preview or Mythos 5.1, so no independent data can test whether a jump happened at Mythos at all. Benjamin Todd's secondhand claim that external ECI shows Mythos "on trend" has no traceable source.

2) Epoch, "Have AI capabilities accelerated?" (Denain & Barry, 2026-04-16). Using 8 model families and cross-validation, the best model was "reasoning models show a one-off jump plus a roughly 2-3x faster trend". That concerns the 2024 reasoning breakpoint, not Mythos. Its relevance is structural: an independent team found that a jump and a slope change can coexist and that it is not either-or, which cuts against framing "one jump vs compounding growth" as two mutually exclusive options. Their own caveat: the acceleration is concentrated in verifiable domains (math and code), and one of the four metrics (WeirdML) showed no acceleration.

3) Kedrosky, "The AI Re-Acceleration That Wasn't" (2026-09-02/03, using Epoch ECI data). A piecewise model over the full sample, controlling for developer and model family, found no significant breakpoint (p=0.615; slope-change CI -8.4 to +23.4/yr). He attributes apparent acceleration to fitting frontier points only, choosing the breakpoint by hand, and ignoring variance collapse. This rebuts the 2024 breakpoint, not Mythos, but AECI's slope ratio uses exactly that method (frontier only, chosen breakpoint). So the CI of 1.20-1.82 for 1.53x is probably underestimated, and every slope-ratio figure, including 1.86-4.3x, rests on this fragile method.

4) METR (independent team, independent tasks). Early Mythos Preview measured a 50% horizon of at least 16h (95% CI 8.5-55h), which METR itself says is at the upper end of what its suite can measure (only 5 of 228 tasks are 16h or longer). METR's TH1.1 puts the post-2024 doubling time at about 89-105 days. I found no time-series analysis of the Mythos family or Opus 5.5 that could separate a jump from a slope change. Ceiling effects mean METR cannot currently confirm or refute the claim.

5) Third-party reviews (same data, interpretation only, not replication). Zvi (2026-09-23) says Opus 5.5 is on the shifted Mythos-level trend, not the old Opus trend, and asks whether that still counts as on trend, answering "basically no". This is a disagreement over framing, not new data. Ånestrand (LessWrong, 2026-05-07) works from Anthropic's numbers (15.7 to 67.4/yr = 4.28x) and warns that Anthropic may over-optimize its internal benchmarks, inflating AECI relative to Epoch's external ECI. He also notes Opus 4.7 fell back onto the pre-Mythos trend line, but that is still Anthropic's data. Lifland (2026-04-08) restates the 2-4x slope figure and the attribution to human research, adding nothing independent.

6) Searched without results: any independent refit or replication of AECI; Epoch public-ECI scores for Mythos Preview or 5.1; METR post-Mythos trend analysis; comparable jump tests from other labs (OpenAI/GDM system cards); academic papers testing the Mythos breakpoint. Search turned up arXiv 2607.12125 and 2607.16112 (titles only, not read) and nothing that directly tests this. I could not open the Opus 5.5 PDF (over 10MB), so the verbatim quotes (+5.9, 99/100, 14.4→22.2, 1.53x [1.20-1.82]) were not checked in this seat against the original text. Search snippets matched the cards on refit AECI, "on trend with the Mythos models", and no further slope change.

Methodological problems:
(a) The refit shift is about as large as the jump. One search snippet attributed to the Fable 5.1 card gives Mythos 5.1 AECI 161.98 (95% CI 158.20-169.00). The Opus 5.5 card has Opus 5.5 at 169.36, "1.24 above Mythos 5.1", which implies Mythos 5.1 was refit to about 168.1, roughly 6 points higher, about the same size as the +5.9 one-time jump. This needs checking against the original PDF. If it holds, the jump estimate is the same order of magnitude as refit noise.
(b) "Better in 99 of 100" only tests robustness to dropping benchmarks. It does not cover choice of breakpoint, frontier-only fitting, or model selection, which are the dimensions Kedrosky criticizes.
(c) After the breakpoint there are only about 5 months and a few frontier points. Jump plus unchanged slope versus a steeper slope is weakly identified on such a short window, and both readings "have not doubled", which matches the card's own "under either reading".
(d) The claim that the jump came from human research without significant AI help is one the card itself is "least able to substantiate publicly"; no outside party can verify it.
(e) Epoch's independent finding of "one jump plus 2-3x slope" shows the two hypotheses can coexist. The article should not present them as mutually exclusive.

**可安全写入**:Anthropic's own internal capability index (AECI, a fork of Epoch ECI) shows Mythos Preview clearly above the earlier trend; depending on the breakpoint, the slope ratio was put at 1.86-4.3x. In its two subsequent system cards Anthropic leans toward a different reading: a one-time upward shift of the trend line, not a continued steepening. The Opus 5.5 card gives the breakpoint-model slope as roughly 14→22 points/yr (about 1.5x) and states that under either reading the slope has not doubled. This is Anthropic's self-assessment on its own internal data and has not been independently replicated. The jump itself is the part Anthropic says it is least able to substantiate publicly, and absolute AECI values shift with each refit. Independent evidence leans the same way but does not settle it: on Epoch's public ECI, 2026 frontier models roughly sit on the reasoning-era trend of about 14 points/yr, but there is no public score for the Mythos models, so the jump itself cannot be checked independently; METR's long-task measurements have hit their ceiling and cannot tell the two readings apart; and independent analyses have shown that this kind of frontier-only, chosen-breakpoint slope comparison is statistically fragile. The safe claim is therefore: Anthropic's own data do not support the AI research loop already compounding (no slope doubling has been observed), but whether it was a one-time jump or a modest acceleration cannot yet be distinguished statistically, and the two are not mutually exclusive.


## R2-aeci-onetime-jump:Anthropic 系统卡 AECI 斜率分析,用来支撑「Anthropic 自己的数据更支持一次跃升,而非复利递增」 — 方法学审计席(有否决权)
**判定**:降级为弱结论

**发现**:
【核对的原文】我从 anthropic.com CDN 下载三份系统卡原 PDF,用 pdftotext 转成文本后逐段读过。三份是:Mythos Preview 卡(2.3.6 节,含 4 月 14 日修订说明)、Fable/Mythos 5.1 卡(2.3.4.2 节和 2.3.5 节)、Opus 5.5 卡(2.3.1 至 2.3.7 节)。待审实证里的引语全部逐字吻合,数字也都能在原文找到:1.86×–4.3×;+5.9;14.4→22.2/年;1.53×(1.20–1.82);99/100;历史斜率 14.75(13.2–17.1)。问题不在引文准确,在于这些数据能不能撑起「一次跃升而非复利」这个推断。

【方法学问题,逐条】
1. 样本量和检验力严重不足。Mythos Preview(2026-04-07)之后只有 5 个数据点(Mythos Preview、Mythos 5、Opus 5、Mythos 5.1、Opus 5.5),时间跨度约 0.46 年。按 14.7/年和 22.2/年两种斜率推算,这段窗口内两条线最多只差约 3.5 AECI 点。同一张卡给的前沿模型 global 误差带是 8–12 点,local 误差带是 2–5 点,窗口太短,两种模型很难区分。Mythos Preview 卡自己也说趋势线「only observes a small number of datapoints」。
2. 「99/100 更优」不能当成独立证据读。100 次 bootstrap 只对基准做重采样(每次去掉 20% 基准),模型和时间点都没有重采样。卡里又写明各前沿模型在不同重采样之间「correlate at r = 0.97 to 1.00」,一起移动。所以 99/100 反映的是结论对基准篮子不敏感,不能算作两种时间趋势假设的统计检验。
3. 「better fit」的判据没有公开。两个模型的自由参数个数不同:断点模型要拟合断点位置和新斜率,跳升模型要拟合跳升幅度。卡里没说比的是似然、残差,还是 AIC/BIC 这类带复杂度惩罚的指标。另外,跳升位置是事后、按已知结果钉在 Mythos Preview 上的,属于看过数据再定假设。断点模型拟合出的断点又落在 2025 年 9 月,早于 Mythos Preview,两个模型讲的其实不是同一件事。
4. 口径漂移,研究者自由度大。每张卡都更换基准篮子并重拟合:338 个基准/525 个模型变成 374 个/732 个,还加了「新的困难内部评估」并修正错误。前沿模型在重拟合后整体上移 4.1–6.1 点,例如 Mythos 5.1 从 162.0 变成 168.12。这和 5.1 卡里「shifts are well within our reported error bars」的说法有张力。Mythos Preview 卡自承「最大的不确定性在于基准选择」,不同的合理选择可以放大或压低 Mythos Preview 的分数。另外,4 月的 1.86–4.3× 和 9 月的 1.53× 不是同一个量下修:前者是在三个指定断点上做两段线性拟合,后者是拟合出的断点加新篮子,不能读成「同一指标从 4.3× 降到 1.53×」。
5. 自评与循环。AECI 主要由不公开的内部基准驱动,内外部分数之间的衔接点也「sparse」,外部无法复算。METR 的「continues the AECI trend」依据的是 Anthropic 在问卷和访谈中提供的信息,不是独立测量。我在本项目的独立测量线(IND)里没有找到用 Epoch 公开 ECI 做的独立复算。
6. 利益冲突。RSP 用 2× 斜率作为阈值,越线就触发义务,而评分、拟合、选断点、选篮子、下结论都由同一家公司完成。
7. 「跃升由人类研究带来」这一归因无法核实。依据是内部访谈,原文自称「least able to substantiate publicly」,细节只给了外部审查方。
8. 测量效度。AECI 衡量的是基准上的能力水平,不是研发速度。RSI 的复利效应可能先出现在研究产出和效率上,不一定马上反映到基准指数。前沿区域基准稀缺(多数基准难度低于 Mythos Preview),顶部被压缩,可能低估斜率。5.1 卡还承认内部指标「subject to some lag」,很难测到最近的加速。
9. 推断越界。就算一次跳升模型拟合得更好,能得出的也只是「到 2026 年 9 月为止,在 AECI 上没有观测到斜率翻倍」,推不出「不是复利」。跳升模型本身也保留了约 14.7/年的基线斜率,而 5.1 卡说内部 AI 使用是「maintaining the current rate」的关键因素之一。也就是说,AI 对维持现有速度的贡献,本来就不在这个检验能看到的范围内。
10. 原文语气本身就有保留:5.1 卡用的是「suggests」;Opus 5.5 卡写的是「we do not interpret」,还写了「one already observed for the Mythos models」,即承认 Mythos 那次有过斜率变化。

【可以承重的部分】三份卡的引语和数字准确;这是厂商唯一公开的、带区间的量化序列;「两种读法下斜率都没到 2×」在厂商自己的口径内成立,1.82 的上限低于 2。

**可安全写入**:Anthropic 用来追踪自家进展的内部能力指数 AECI(Epoch ECI 的内部 fork,主要由不公开的内部基准驱动),给出的数字一直在变。4 月的 Mythos Preview 卡写道:「On the current pipeline, the slope ratio lands between 1.86× and 4.3× depending on the choice of breakpoint」,并称误差棒「quite large」。卡里把这次上弯归因于没有 AI 显著帮助的人类研究,同时承认这是「least able to substantiate publicly」的一环。9 月 1 日的 Fable/Mythos 5.1 卡说,近期模型的证据「suggests」那是一次把趋势线整体上移的一次性跳升。9 月 22 日的 Opus 5.5 卡换了基准篮子、重新拟合,做了两种假设对比:一种是在 Mythos Preview 处一次性跳升 +5.9 点、斜率不变;另一种是斜率在 2025 年 9 月从 14.4/年升到 22.2/年(1.53×,95% 区间 1.20–1.82)。在 100 次各去掉 20% 基准的重拟合中,前一种有 99 次拟合更好,卡里的结论是「under either reading the slope has not doubled」。需要注意几点:这是厂商对自己的打分,外部无法复算;每张卡重拟合后绝对值都会变,不能跨卡比较;Mythos Preview 之后只有约 5 个模型、不到半年,统计上很难区分「一次跳升」和「斜率温和上升」;99/100 反映的是换一批基准结论不变,不是对时间趋势的统计检验。所以这组数据最多说明:按 Anthropic 自己的指标和口径,截至 2026 年 9 月还没看到 RSP 所说的 2× 持续加速。它不足以证明进展「不是复利」。


## R3-cunningham-9pct:Cunningham 等(Elasticity Institute,METR 资助,arXiv 2609.15802)的结论"约 9%/ECI,低于 15% 阈值 → 当前未处于自持加速" — 反证搜索席
**判定**:降级为弱结论

**发现**:
一、原文核对(已下载 arXiv PDF 全文逐段核)
- 阈值推导(§4.1):条件是 [g_A/g_R]·ε_R,C·ε_C,A > 1。原文取 g_A = g_R = ln3,所以第一项等于 1;ε_C,A ≈ 6.5,来自 Epoch 跨模型数据,做 ECI 对 log(训练算力)的回归斜率。由此得 ε_R,C > 1/6.5 ≈ 0.15。所以 15% 不是测出来的值,是由两项校准假设推出来的:
  (a) g_R = ln3 刻意没计入推理算力的增长。原文自己引了 OpenAI 的说法:半年内内部编码推理占研究算力的份额涨了 100 倍。如果 g_R 实际更大,阈值会更高。
  (b) g_A 用的是 2024 年的估计。原文也承认算法进步存在 scale-bias,所以 ε_C,A 可能和 ε_C,T 不相等。
- 9% 的算法:Opus 4.8 比 Claude 3.7 Sonnet(2025-02,随 Claude Code 一起发布)高 16 个 ECI 点;起点 uplift 假设约 1×(原文引 Becker 2025 的负效应为依据);终点用 Mythos Preview 系统卡里员工调查给出的 4×;4^(1/16) ≈ 1.09。原文写的是"very likely to be an overestimate, but even if it were true"。也就是说,原文自己把 9% 当作上界式的论证,不是点估计。
- 方法学问题:
  ① 4× 来自 Slack 上的自愿投票,130 人回答,取几何均值,问的是相对"零 AI"的自评 uplift。这是 Anthropic 一家机构的单一数据。
  ② 调查对象是 Mythos Preview(2026-04),但 ECI 终点用的是 Opus 4.8,两者的模型和时间点不一致。另外,Anthropic 系统卡里的 ECI 混用了内部基准,和公开 ECI 不能直接比。
  ③ 单位不严格:阈值 0.15 是对数弹性,9% 是百分比;换成对数口径是 ln4/16 ≈ 8.7%,结论方向不变。
  ④ 原文明说员工劳动 uplift 大于研发产出的弹性,因为劳动只占研发投入的一部分。拿劳动 uplift 直接去比 ε_R,C 是偏高的,这一点对"低于阈值"的结论有利。
  ⑤ 16 个 ECI 点上的平均值会掩盖近期的加速。原文自己也说弹性"likely increasing"。

二、搜索角度和结果
1. 有没有独立团队对本文的复核或批评?Ramez Naam,2026-09-27 博客,作者与本文无关联。他用 Epoch 估计的 Stockfish 研究回报 0.83 修正参数,把阈值抬到约 19%/ECI;又用 OpenAI 的数据(他引为每研究员实验数约 1.6×,配约 16 个 ECI 点)算出约 2–3%/ECI,和阈值差 5–10 倍。数据来自另一家实验室,而且是日志数据,不是自评,所以算独立方向的佐证。但"1.6×"这个乘数我在 OpenAI 报告的二手转述里没找到原值:转述只说 2026-08 达到历史最高,没给倍数;OpenAI 原文页面返回 403,无法核验。Naam 的计算未经同行评议,"每研究员实验数"也不等于研发生产率。另外,AI Weekly 那篇只是复述原文,不算独立来源。
2. 有没有对 4× 本身的独立质疑?Ryan Greenblatt,LessWrong,2026-04-11:他自估 Mythos 带来的串行劳动加速约 1.55×(AI Futures 转述的私下估计为 1.7×);引 Dario 2 月的说法"15-20% total factor speedup";并指出 Opus 4.6 的内部调查结果是 2.52×。METR 调查(Becker,2026-05,n=349)得到自评中位数 1.4–2×。代入原文同一公式(16 个 ECI 点)算出:1.4× 约 2.1%,1.55× 约 2.8%,1.7× 约 3.4%,2× 约 4.4%,2.52× 约 5.9%,全部低于 9%。要达到 15% 阈值,16 个点上需要约 9.4× 的 uplift(对数口径约 11×);按 19% 阈值则需要约 16×。目前没有任何独立来源报告过这个量级。
3. 有没有其他机构对研发倍率的估计?AI Futures Project,2026-08-16:Daniel 给的当前编码 uplift 中位数约 2×;他们判断走势是指数而不是超指数。AI 2027 Tracker 认为 1.5× 研发倍率处于"emerging"状态。OpenAI 2026-09 的报告:agent 工作日与人类工作日之比为 3.1:1,但报告自称这些指标"hard to interpret",没有给出研发加速倍数。
4. 有没有和"低于阈值"相矛盾的量化?没有找到任何独立测量认为当前已经超过阈值。但有一个潜在的反向风险:AI Futures 转述 Anthropic 的调查在 7 个月里从 1.25× 升到 4×。如果只看这个近期窗口的 ECI 增量,每点弹性可能明显高于 9%,甚至接近阈值。我没有找到这个窗口的可比 ECI 增量,所以无法量化,只能列为未核实的风险。这一点和原文"appear to be strengthening"的判断一致。
5. 有没有其他理论框架?Burtsev(arXiv 2609.00137)提出 R_AI 再生数,指出系统可能在加速可见之前就已越过临界,而且跨组织共享可以让整个生态自持,即使单个机构不自持。这是理论,没有测量,只能提醒"单实验室口径可能低估"。Forethought(Eth & Davidson)估计软件研发回报 r 中位数 1.2(范围 0.4–3.6),但前提是 AI 研发已被完全自动化,和"当前部分自动化下的弹性"不是同一个问题,不能直接拿来对照。
6. 没搜到的:针对 9% 或 15% 的同行评议回应;任何用实验室内部日志直接估算 ε_R,C 的独立研究;Opus 4.8 和 Mythos 在公开 ECI 上的可比分数;OpenAI 报告里的原始实验数倍数。同一机构 Elasticity Institute 的后续文章 "How to Measure RSI"(2026-09-23)不算独立来源。

三、结论
方向("目前低于自持阈值")有多个独立来源佐证:Greenblatt、METR 调查、AI Futures、Naam 用 OpenAI 数据的推算,给出的数值全部更低,也没有找到反例。但"9%"这个具体数字不能单独承重:它是原文自己承认偏高的上界式粗算,依赖单一机构的自愿投票,模型和 ECI 也对不上;"15%"是靠两项强假设校准出来的阈值,换成别的合理参数会落在 15–19% 或更高。所以不应把它写成"最直接的量化读数",应改写为"一个偏向上界的粗算,即使用最乐观的数也低于阈值"。

**可安全写入**:Cunningham 等(2026-09,Elasticity Institute,METR 资助)做过一个粗算。在他们的模型里,能力每提高 1 个 ECI 点,AI 研发生产率至少要提高约 15%,才能形成自持加速;这个阈值依赖他们对算法进步速度、研发投入增速等参数的校准。他们拿 Anthropic 员工自愿投票自报的约 4× 提效(作者自己认为这个数"很可能高估")摊到约 16 个 ECI 点上,得到每点约 9%,仍低于阈值。这个 9% 应读作偏向上界的估计,不是测量值:用其他更低的独立估计代入同一算法,例如 METR 调查的 1.4–2×、Greenblatt 估计的约 1.55–1.7×,每点只有约 2–4%;要达到阈值,uplift 大约要到 9–11×,目前没有独立来源报告过这个量级。因此可以说"现有证据普遍指向当前未达自持加速",但不宜把"9% < 15%"当作精确读数。还要补一句:作者和其他观察者都指出这个回报在上升,而跨 16 个 ECI 点的平均值可能掩盖了近期更快的增长。


## R3-cunningham-9pct — 方法学审计席
**判定**:降级为弱结论

**发现**:
一手原文已读:arXiv 2609.15802 全文 PDF(提交日 2026-09-14),重点读了第 1 节摘要、第 3 节数据表和 4.1/4.2 节。
【事实核对:全部属实】作者 Cunningham(METR)、Althoff、Halperin、Jabarian、Koh、Ramani、Trammell(Stanford DEL 和 Epoch AI)、Whitfill(METR)、Wu,所有作者都挂 Elasticity Institute,论文声明"METR 提供行政与资金支持"。15% 阈值、16 个 ECI 点(Claude 3.7 Sonnet 到 Opus 4.8)、约 4X、约 9%、"very likely to be an overestimate"、摘要里的"not currently strong enough... though they appear to be strengthening",原文都有。算术也对:4^(1/16)-1=9.05%,按对数口径 ln4/16=8.7%。
【方法学问题】
1. 作者自己定性为粗算。原文用词是 "back-of-the-envelope" 和 "very rough calibration",还写明有 "high degree of uncertainty" 和 "model misspecification" 的可能。论文是没经过同行评审的预印本,这个数也只有这一个来源。
2. 分子(4X)是自报数据。来源是 Mythos Preview 系统卡里 Anthropic 员工的自评,样本量、题目措辞、抽样方式在本文里都查不到。来源方是利益相关方。作者在两处说它可能高估。METR 自己的调查(Becker 2026)给的是 1.4–2X;Becker et al. 2025 的 RCT 测出 AI 让工程生产率下降。分子换成 2X 得 4.3%,换成 1.4X 得 2.1%。
3. 构念错配。4X 是"工程师任务 uplift",而阈值针对的是 ε_R,C,即每增加一个 ECI 点、整体研发投入增加多少。作者自己承认,研究产出的弹性小于人类任务 uplift,因为劳动只是研发投入的一部分。另外 4X 是用 Mythos Preview 时报的,ECI 差值却按 Opus 4.8 算,模型对不上。基线还默认 2025-02 时 uplift≈1X(作者说当时"not conclusively larger than 0")。
4. 时间口径是最要紧的问题。9% 是 2025-02 到 2026 年间 16 个 ECI 点上的几何平均,读的是区间均值,不是当前的边际值。作者明说这个弹性"likely increasing",摘要也写"appear to be strengthening"。在弹性递增的情况下,均值低于阈值,推不出当前边际值也低于阈值。所以拿它当"当前未处于自持加速"的直接读数,逻辑上有缺口。
5. 阈值本身也不稳。15%≈1/6.5,前提有三个:(a) ε_C,A≈6.5,来自 Epoch 数据上 ECI 对 log(compute) 的跨模型回归,并假设 C=C(A×T) 对称、不存在规模偏置(作者在脚注 11 里暂时搁置了这个问题);(b) 回报项 gA/gR=ln3/ln3=1,而 gA 是 2024 年的估计;(c) gR 直接设为 ln3,作者自己说 gK 实际已经大增(GPT-5.6 发布时提到编码推理在研究算力中的占比 6 个月涨了 100 倍)。gR 变大会推高阈值,但这一项没有区间,也没做敏感性分析。阈值和读数都没有误差棒。
6. 作者自己写道 "We have almost no evidence for this parameter (ε_R,C)",也就是说,最关键的那个参数基本没有实证。
7. 利益冲突:METR 出资,两位作者是 METR 员工。ECI 是 Epoch 的产品,Trammell 隶属 Epoch。没看出系统性偏向某个结论,但这一点应该披露。
8. 有一点对文章有利,所以不建议否决:4X 很可能高估,构念错配也会让 9% 偏高,所以 9% 更接近区间均值的上界,"低于阈值"这个方向在该模型内部是稳的。真要达到 15%,16 个点内的 uplift 需要约 9.4X(复利口径)或约 11.7X(对数口径),和现有任何自报数都差得远。
【没搜到的】Mythos 系统卡里那次调查的样本量和题目原文(本次没读系统卡原件);ε_C,A=6.5 回归的置信区间(论文没给)。

**可安全写入**:Cunningham 等人(Elasticity Institute,METR 资助,2026 年 9 月预印本)做了一个模型推导:按 Epoch 能力指数(ECI)衡量,如果能力每提高 1 点,AI 研发生产率至少提高约 15%,反馈环就会进入自持加速。作者用 Anthropic 员工在 Mythos Preview 系统卡里自报的约 4 倍提效做了粗算:2025 年 2 月 Claude Code 上线以来,这一回报平均约 9%,低于阈值。作者自己指出,4 倍很可能高估;9% 是过去约 16 个 ECI 点的区间平均,不是当前值;阈值依赖多项未经检验的假设,关键参数"几乎没有实证"。他们的结论是,反馈环"目前还不足以自持,但似乎在增强"。所以,这个数字只能说明过去一段时间平均看尚未越过模型阈值,而且是粗略的。它不能证明当前不处于自持加速,也不能用来判断离越过阈值还有多远。(不得写成"已测得 RSI 回报为 9%",也不得把它当作文章结论的唯一量化依据。)
