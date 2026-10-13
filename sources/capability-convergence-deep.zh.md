# AI 能力最终会趋同吗?——排行榜挤压、天花板效应与长任务上的分化(深入版)

> 方法学说明:本文承重论断分为 27 组,每组派 3 个独立验证 agent(共 81 票),要求「尽力反驳」:逐字回到论文、官方报告与官方榜单原文;凡是调研阶段基于原始数据自算的数字(Arena 历史快照、Epoch 基准数据与能力指数、METR 原始 run 记录、τ²-bench 提交文件、ARC Prize 榜单 JSON),验证者都重新下载数据复算。结果:81 票中 80 票判「需修正」、1 票判「原样成立」、0 票判「推翻」;27 组里没有一组能三票原样通过,约 210 处原稿写法被判死或被禁止按原样使用。另对 4 条「单一来源承担关键结论」的实证加做反证搜索席与方法学审计席(共 8 席):4 条全部被降级,其中两条由反证席判为「方向存争」,没有一条被否决。证据分级:【多源证实】≥2 个独立来源同向;【单源已核】一手文件或原始数据可回溯;【方向存争】独立来源矛盾;【厂商口径】利益相关方自述,方向可参考、程度不承重;【未验证】。本文大量数字是用公开原始数据自算的,凡属自算都会注明。所有数字截至 2026 年 10 月 12 日;Epoch 能力指数(ECI)每次更新数据都会整体重新拟合,本文引用的是 2026 年 10 月下载的版本。

## 0. 先给「差距」一个能检验的定义

「头部模型越挤越近」「开源和闭源只差几个百分点」「中美差距实际上已经闭合」——这三句话在 2025–2026 年被反复引用。另一边的说法同样流行:「前沿在长任务上把差距放大了,赢家通吃。」两种叙事说的都是「差距」,但很少有人说清楚差距指什么。

差距至少有三种可检验的定义,而且它们可以给出相反的方向:

- **分差**:同一把尺子、同一时点,领先者与追赶者的分数之差(带置信区间)。
- **追平月数**:追赶者达到领先者某一水平,晚了几个月。
- **比值**:同一时点两者的倍数关系,例如能独立完成的任务长度之比、成功率之比。

三者之间有一个简单的换算。如果前沿某项能力(比如能独立完成的任务时长)每 D 个月翻一倍,那么落后 L 个月,就等于落后 R = 2^(L/D) 倍。取 METR 测得的 2023 年以来倍增期 D≈4.23 个月(128.7 天,95% 区间约 3.4–5.2 个月),落后 4 个月约等于落后 1.93 倍。【单源已核:自算,前提是倍增期恒定的指数增长】

这个换算有一个直接推论:**追平月数不变,而前沿加速,比值就会拉大。** 同样落后 4 个月,前沿每 7 个月翻倍时只差 1.49 倍,每 3.5 个月翻倍时就差 2.21 倍。所以「追赶者一直落后半年左右」与「差距在拉大」可以同时为真;「分差越来越小」与「比值越来越大」也可以同时为真。本文后面每一节,都会先说清楚用的是哪一种差距。

还有一组概念要分开:**用户感知饱和**(日常任务上分不出谁更强)与**能力饱和**(真的没有差别)。前者是测量问题,后者才是能力问题。

## 1. 天花板如何把差距压扁

**基准饱和是常态,而且越来越快。** Ott 等(Nature Communications 2022,数据约截至 2021 年,只覆盖计算机视觉与自然语言处理)整理了 3765 个基准,其中约一半有三个以上时点的结果可做趋势分析;作者写道:「a large fraction of benchmarks quickly trended towards near-saturation」。他们在引言里还指出,近饱和基准上「statistical significance of differences in model performance is more difficult to achieve」——这是带引用的动机性论述,不是该文的实证结果。【单源已核】到大模型时代,Akhtar、Reuel 等(arXiv 2602.16763,ICML 2026)检查了 60 个文本类语言模型基准,按作者自定义的饱和指数(Sindex≥0.7,指头部模型之间在统计上失去可靠区分力,不等于达到人类水平),29 个(48%)属于高或极高饱和,比例随基准年龄上升。【单源已核】

**为什么饱和会制造「趋同」的错觉。** Epoch 在构造跨基准能力指数时写下了一条方法论前提:「We can only compare models when they're in the middle — not too good and not too bad.」【单源已核】用一个简单的算术可以看清原因。假设两个模型在同一个 logistic(项目反应理论)刻度上相差一个固定的能力差,设定这个差恰好让较弱模型在 50% 时、较强模型在 70%——分差 20 个百分点。同样的能力差,当较弱模型的得分已经是 90%、95%、99% 时,分差只剩 5.45、2.79、0.57 个百分点,压缩约 35 倍(若以较强模型的得分为基线,约 15 倍)。【单源已核:自算,20 个百分点是设定值,不是实测】也就是说,在一张快被做满的考卷上,「只差零点几分」与「能力相同」在数学上不是一回事。

**排行榜上的百分比本身也有问题。** Stanford AI Index 2025 写道,Chatbot Arena 第 1 名与第 10 名的差距从 11.9%(这是上一年报告引用的 2023 年数据)缩小到 2025 年初的 5.4%,前两名从 2023 年的 4.9% 缩小到 2024 年的 0.7%;最强闭权重与最强开放权重模型的差距从 2024 年 1 月的 8.04% 缩小到 2025 年 2 月的 1.70%。【单源已核】这些百分比的分母是 Arena 分数的绝对值,而 Arena 分数整体可以任意平移——头部分数从约 1250 涨到约 1385,即使分差不变,百分比也会机械地缩小约一成。换成分差,5.4% 约合 70–75 个 Arena 点,0.7% 约合 10 个点,1.70% 是 23 个点(1,385 对 1,362)。分差在 Arena 上的含义是单局胜率:10 分约等于 51.4%,30 分约 54.3%,49 分约 57.0%,100 分约 64.0%。【单源已核:自算】

AI Index 2026 换了说法:开源差距「在 2025 年重新打开」,2026 年 3 月最强闭源 Claude Opus 4.6(1,503)领先最强开放权重 GLM-5(1,454)49 个点;中美之间,Claude Opus 4.6 领先 Dola-Seed-2.0 Preview(1,464)39 个点,报告据此认为中美差距已基本消失。同一个 49 点,报告的要点页写 3.3%,正文写 3.4%,分母不同。更要紧的是两版报告的序列接不上:2025 版用基准百分点衡量中美差距(MMLU、MMMU、MATH、HumanEval 从 2023 年底的 17.5/13.5/24.3/31.6 个百分点缩小到 2024 年底的 0.3/8.1/1.6/3.7),2026 版改用 Arena 分;而且 2026 版把 2025 年 2 月的中美 Arena 差重算为 0.4%,2025 版当时写的是 1.7%。Arena 在 2025 年 5 月把风格控制设为默认,历史分数被重新拟合过。【单源已核】AI Index 2026 要点页另有一句「Six of the top ten models on the Arena Leaderboard are now closed」,与 Arena 原始数据对不上(按模型计,3 月快照前十全是闭源),本文不采用。

**饱和的速度也在加快。** 按 Epoch 数据扣除随机猜测基线后,以首个达到 80% 的模型发布日计:GPQA Diamond(2023 年 11 月发布)约 19 个月;SWE-bench Verified(2024 年 8 月)按 Epoch 独立复测约 20 个月,按厂商自报约 15 个月;ARC-AGI-2(2025 年 3 月)约 11 个月;Terminal-Bench 2.0(2025 年 11 月)约 3 个月后被一个「模型 + 第三方 agent 框架」的组合首破 80%。Humanity's Last Exam(2025 年 1 月)到 2026 年 9 月才被 GPT-6 Astra 以原始分 54.8% 首次过半。【单源已核:自算】AI Index 2026 的概括是「Evaluations intended to be challenging for years are saturated in months」。

## 2. 偏好排行榜:点数在挤,排序已经脱钩

**头部确实挤了,但不是单调的。** 用 Arena 公开的历史快照(Hugging Face 数据集 lmarena-ai/leaderboard-dataset,风格控制文本总榜)每月取最后一个快照自算:第 1 名与第 10 名的分差,2024 年 12 月 30 日为 75.3,2025 年 6 月为 67.3,2025 年 12 月为 41.7,2026 年 8 月 27 日为 18.7,2026 年 10 月 8 日又回到 31.4。【单源已核:自算】这条序列并不单调:2025 年 10 月 17 日曾低到 16.9,2026 年 9 月曾到 12.8;月内波动也很大。稳一点的说法是,分差从 2024 年末到 2025 年中的约 50–85,降到 2026 年中的约 17–30。前十里同一家实验室的不同推理档位会挤占名额(2026 年 10 月 8 日前十有 7 个是 Anthropic 的变体),按实验室去重后,第 1 家与第 5 家的差为 75.3(2024 年 12 月)→ 42.7(2025 年 12 月)→ 23.6(2026 年 8 月)→ 40.3(2026 年 10 月 8 日)。这段时间 Arena 改过几次方法:2025 年 5 月风格控制设为默认并整体平移分数,2025 年 7 月引入按频率重新加权(官方承认会加宽置信区间),2026 年 5 月把「直接对战」投票计入。2025 年 7–9 月分差从 67 骤降到 28,恰好跨过重加权上线,所以跨年下降只能当方向证据,不能当精确幅度。

10 月的回升来自刚上榜的 gemini-4-argon-high:1525.4(95% 区间 1516.5–1534.2),只有 4,892 票,领先第 2 名 claude-opus-5.5-high(1507.1)18.3 分,两者的置信区间只隔一分多。新模型票少,分数常在上榜后回落。

**闭源与开源的 Arena 差:没有趋势,只有口径。** 风格控制榜上,闭源第一减开源第一(开源定义为许可证非空且不是 Proprietary,包括 Kimi K3 这类非商用许可)的年度最小/中位/最大值为:2024 年(8 月 28 日起)10.7/48.8/75.9,2025 年 2.7/43.0/70.4,2026 年(至 10 月 8 日)17.7/35.1/57.7。【单源已核:自算】开源模型从未登上风格控制榜第一;在不做风格控制的原始榜上,2024 年以来只有 DeepSeek-R1 在 2025 年 1 月 24 日至 2 月 27 日的 11 个快照里短暂反超。2026 年 10 月 8 日的差距取决于票数门槛:不设门槛是 37.3;只看一万票以上的闭源模型是 16.3(claude-opus-4-6-high 对 kimi-k3-max),8–10 月同一门槛下的 18.7、17.5、16.3 都落在置信区间之内,不构成收窄趋势。Arena 官方在 2026 年 5 月 7 日的 X 帖里概括为:「The remaining gap is small in points, but still large in rank」——当时领先约 30 分,相当于第 1 名与约第 18 名的距离。【单源已核,当事方口径】

2026 年 9 月有媒体报道「闭源与开源的差距扩大到 29 Elo,是近两年最大」,并说 2025 年 1 月差距「归零」。29 来自原始榜 8 月 27 日至 9 月 1 日的快照(28.7),同期风格控制榜在 17.7–20.9 之间;原始榜 2026 年就出现过 59.6 和 51.1,「近两年最大」不成立;2025 年 1 月原始榜上是 R1 反超,风格控制榜上最小差 2.7,两种口径都不是「归零」。把起点挑在 R1 那个月,才得出「扩大」。【单源已核:自算;媒体原说法判死】

**榜单本身的偏差与这些分差同一量级。** Singh 等《The Leaderboard Illusion》(arXiv 2504.20879 v2)记录了 Meta 在 Llama-4 发布前私测了 27 个文本模型变体;按 2024 年 1 月至 2025 年 4 月的对战场次份额估计,Google 与 OpenAI 分别拿到约 19.2% 和 20.4% 的 Arena 数据,83 个开放权重模型合计约 29.7%。论文对「私测多个变体、只公布最好的」能抬高多少分数前后说法不一:v1 是「10 个变体约 +100」,v2 正文与附录改为「20 个变体约 +50」,v2 的要点总结仍保留旧数。论文作者主要来自 Cohere——一家在 Arena 上参赛的模型公司。Arena(被批评的一方)的回应称,按它的模拟,50 次测试、3,000 票之后私测的增益约 +11 Elo,并会随新数据归零;回应也承认「The best models, regardless of provider, are upsampled」。【多源证实(论文);Arena 的 +11 为厂商口径】不论取 +11 还是 +50,这类偏差都和当前头部 10–30 分的分差同一量级。

**最关键的发现:在前沿区间,偏好排序与能力排序基本不相关。** 把 2026 年 10 月 8 日的 Arena 风格控制榜与 Epoch ECI(2026 年 10 月版)按模型名对齐,共 111 个模型。全体样本的 Spearman 相关为 0.95,但其中一部分来自不同代际模型之间的时间跨度——只看 2026 年发布的模型约为 0.72。只看 ECI 前 30 名降到 0.19,前 15 名约为 0(点估计 −0.03,95% 区间约 −0.6 到 0.5)。【单源已核:自算;Round 3 双席审计降级为弱结论】这不只是「样本范围窄了,相关自然变低」:在同样这 15 个模型上,各项能力基准两两之间的排序相关中位数仍有 0.69,与 Epoch 公布的跨类别中位数 0.68 吻合;去掉风格控制后,脱钩反而更明显。

但 Arena 并没有失去区分力。前 15 名里,105 对模型中有 39 对置信区间不重叠,它只是在按另一种标准排序。两个例子:ECI 把 Claude Opus 5.5(167.3)排在 Opus 4.6(155.2)之上 12 分,90% 区间不重叠,而 Arena 上 opus-5.5-high 与 opus-4-6-high 只差 2.7 分,实际打平;ECI 把 GPT-6.1 Sol 排在 Kimi K3 之上 8.6 分,Arena 上两者差 4.4 分、同样打平。所以结论是:**在前沿区间,偏好榜已不能当作能力的代理指标。** 原因可能是普通用户在日常提示上分不出差别(用户感知饱和),也可能是两者测的根本是不同的东西(对话体验、风格、速度),还可能是变体择优把头部压扁了——现有数据区分不了这三种解释。

## 3. 静态考卷:饱和的地方差距小,没饱和的地方差距大——但不全是

**同一批模型,换一张考卷,差距差一个数量级。** 用 Epoch 基准数据(近 12 个月发布的模型)自算,最佳闭源与最佳开放权重模型的分差:GPQA Diamond 95.8%(GPT-6 Astra)对 93.1%(Kimi K3,非商用许可),差 2.7 个百分点,只算无限制许可的开源约差 4 个百分点;SimpleQA Verified 75.6% 对 52.9%;FrontierMath Tier 1–3 为 93.7% 对 72.2%;FrontierMath Tier 4(41 道研究级数学题)上,Epoch 表中 GPT-6 Astra 为 97.6%,开源最好的 Kimi K3 只有 39.0%(16/41),无限制许可的开源最好是 26.8%。【单源已核:自算】Epoch 表中 GPT-6.1 Sol 在 Tier 4 上记为 100%,但没有公开运行日志,无法独立核验;Claude Opus 5.5 记为 95.0%,与 41 题的整数比对不上,运行口径不同。

换成比值(开源最佳 ÷ 发布日不晚于它的闭源最佳,衡量「追平同期闭源到什么程度」):知识类与接近饱和的基准在 0.94–0.98 之间(GPQA 0.98、SWE-bench Verified 0.94、DeepSWE 0.94、旧版 OSWorld 0.95);较难的 agent 与数学基准在约 0.55–0.87 之间(APEX-Agents 0.87(计入 Epoch 漏标的开源模型 MiMo-V2.6-Pro;只计 Epoch 标注的开源为 0.78)、同一 agent 框架下的 Terminal-Bench 2.0 0.83、FrontierMath Tier 1–3 0.81、FrontierSWE 0.55)。【单源已核:自算】分化是真的,但集中在最难的长程工程与数学任务上;DeepSWE 和旧版 OSWorld 本身就是 agent 任务,比值却在 0.94 以上。

**分差随时间的形状有两种。** 一种是先扩后缩的「倒 U」:新考卷刚出来时闭源先冲上去、开源跟不上,分差拉大;等闭源接近满分,天花板把分差压回去。ARC-AGI-1 上,闭源最佳减开源最佳从 2025 年 5–6 月的约 39.6 个百分点涨到 2025 年底的约 59–69,2026 年 7 月 Kimi K3 发布后降到 4.0;ARC-AGI-2 从 2025 年中的 7.3 涨到 2026 年 4 月的 73.2,当前按 Epoch 数据为 29.2、按 ARC Prize 官方榜为 22.1。另一种是单调收敛:AIME 类竞赛数学从 2024 年 12 月的 57.5 个百分点一路收窄,2025 年 7 月开源一度反超,2026 年 8 月起为 1.4;GPQA 从 2024 年 12 月的 20.2 降到 2025 年 7 月的 6.9,现在 2.7。【单源已核:自算】这两种形状的共同点是:**任何一张考卷上的「差距收窄」,都要先问它离满分还有多远。**

**反例同样存在:没饱和的考卷,差距也可能很小。** DeepSWE(所有模型用同一个 agent 框架)上,2026 年 6 月底闭源最佳 Fable 5 为 69.9%,开源最佳 GLM-5.2 为 43.8%,差 26.1 个百分点;7 月 16 日 Kimi K3 发布(68.5%),差距一天之内降到约 4 个百分点,之后基本不变,10 月为 5.6(对 GPT-6 Astra 74.1%;Kimi K3 为非商用许可,只算无限制许可的开源为 10.7)。Artificial Analysis 用统一框架测的 FrontierCode 1.1 上,Claude Opus 5.5 为 52%,开源最佳 MiMo-V2.6-Pro 为 45%,DeepSeek V4.1 Flash 与 Kimi K3 各 44%。【单源已核】所以「未饱和就一定拉开」不成立;追赶有时是一次发布完成的跳变,不是渐进收窄。

**被测方开始换考卷。** 2026 年 2 月 23 日,OpenAI 宣布停报 SWE-bench Verified:它审计了 o3 在 64 次独立运行中未能稳定解出的 138 道题,发现「59.4% of the 138 problems contained material issues in test design and/or problem description」;所有受测前沿模型在部分题目上能复现人写的参考修复或题面原文细节;OpenAI 建议其他开发者也停报,改报 SWE-bench Pro。【多源证实】Anthropic 2026 年 9 月 22 日发布 Claude Opus 5.5 时,基准表列的是 Terminal-Bench 4.0(66.4%,xhigh 档、自家设置)、FrontierCode、GDPval-AA、HLE(带工具 67.7%)等,全文不出现 MMLU、GPQA、SWE-bench、AIME;2024 年 3 月 Claude 3 发布时主打的正是 MMLU、GPQA、GSM8K。【厂商口径】Artificial Analysis 的智能指数 2026 年 1 月移除了 MMLU-Pro、LiveCodeBench、AIME 2025(版本史没写理由),9 月移除 GPQA Diamond,公告称它「has now been saturated」。【单源已核】

## 4. 合成指数:2026 年差距没有收窄,但「翻倍」站不住

**Epoch 的官方估计。** Epoch 2026 年 5 月 29 日的数据洞察估计,2026 年 1 月 1 日至 5 月 28 日,最强开放权重模型按 ECI 平均落后前沿闭源模型约 4 个月;判定「追平」的标准是开源模型在至少 5% 的配对 bootstrap 样本中超过当时的最强模型,若要求点估计严格更高则为 6 个月。平均 ECI 差 8 点(90% 区间 7–11)。Epoch 说这比它 2025 年 10 月的估计「slightly larger」——那次是 2023 年 1 月至 2025 年 10 月的多年平均,约 3 个月(正文 3.5 个月,90% 区间 1.1–5.3)。两次的方法与时间窗都不同,旧区间也覆盖了 4 个月,所以「从 3 个月扩大到 4 个月」在统计上不成立。【单源已核】Epoch 自己指出这一估计可能低估真实差距:「open-weight models tend to perform worse on private benchmarks compared to closed models, plausibly because they more aggressively hillclimb on public benchmarks」;以及「Leading closed labs do not always release their most capable models」。

**用 10 月数据自算。** 截至 2026 年 10 月 12 日,最强闭源 Claude Opus 5.5(9 月 22 日发布)ECI 167.3(90% 区间 164.1–171.7),最强开放权重 Kimi K3(7 月 16 日发布)157.5(155.2–160.0),相差 9.9 点,区间不重叠。季末分差在同一次拟合里是:2025 年 3 月 5.2、6 月 6.1、9 月 5.0、12 月 9.1;2026 年 3 月 10.9、6 月 10.3、9 月 9.9。分差呈锯齿状:Kimi K3 发布后的 2026 年 8 月一度回落到 5.3,和 2025 年 10 月相当;9 月闭源新模型集中发布后又回到约 10。按逐日平均,2025 全年 5.78、2026 年至今 9.09,约 1.57 倍;同一次拟合内的 bootstrap 给出的增幅为 +3.45 点(90% 区间 1.9–5.3)。【单源已核:自算;Round 3 双席审计降级为「没有收窄」,「扩大」本身为方向存争】

三个限定让「差距翻倍」这种说法站不住。第一,是否「翻倍」取决于拿 2025 年哪一天做基准,2025 年内分差本身就在约 3–9 之间来回。第二,ECI 每次加入新数据都会整体重新拟合:同样是 GPT-5.5 Pro,5 月版拟合为 159.35,10 月版为 162.07;同一个 2026 年 5 月的分差,6 月版拟合下是 7.7,10 月版下是 11.0——漂移约 3 点,与所谓的「扩大」同一量级,而且集中在闭源顶端(这些模型测过的基准较少)。所以拿 10 月复算的数字和 Epoch 5 月发布的数字比较,不能证明差距扩大。第三,另一家合成指数给出相反的读数:Artificial Analysis 的智能指数上,开源最佳与闭源最佳的差距从 2025 年 4 月的约 13 点缩小到 2026 年 4 月的 6 点(对 GPT-5.5 的 60 分);它当前版本是 12 点(Claude Opus 5.5 58 对 MiMo-V2.6-Pro 46),但跨了指数版本——Kimi K3 在旧版本是 57 分,当前是 44 分——不能连成趋势。【单源已核】

点差为什么变大?以 10 月末为年界,闭源前沿的 ECI 年增量依次为 +9.9、+14.5、+17.1(最后一段不足 12 个月),开源前沿为 +11.9、+16.0、+12.4。点差扩大主要来自**闭源前沿加速**,不是开源放慢;用月数衡量,滞后大致持平——这正是第 0 节那个换算的含义。【单源已核:自算】逐个模型看,2026 年每个打破开源纪录的模型,追平月数(按严格点估计口径)在 4.4 到 8.0 个月之间:Kimi K2.5 5.7、GLM-5.1 8.0、Kimi K2.6 5.0、GLM-5.2 6.9、Kimi K3 4.4;按 Epoch 的 5% bootstrap 口径则在 2.8 到 6.2 个月之间。

**本节可以承重的结论只有一句:在跨基准的合成量尺上,2026 年开源与闭源的差距没有收窄;是否在扩大,取决于量尺与基准时点。** 「差距只剩几个百分点」的印象,来自饱和的考卷、偏好榜上的百分比,以及 Artificial Analysis 指数在 2025 年 4 月至 2026 年 4 月的收窄读数。

## 5. 长任务与可靠性:最该看的地方,尺子先到头了

**问题本身是对的。** 如果每一步的成功率是 p,一个需要 n 步、错一步就失败的任务,成功率是 p^n:0.95 的 50 次方约 7.7%,0.99 的 50 次方约 60.5%。在这个玩具模型里,错误率降到 1/k,能完成的任务长度大约增加 k 倍。【单源已核:自算,前提是各步独立、难度相同、一步错即失败】单步看似只差几个百分点,长任务上就可能差出数倍。Sinha 等(ICLR 2026)据此论证,短任务基准可能制造「进步放缓」的错觉:「even marginal gains in single-step accuracy can compound into exponential improvements in the length of tasks a model can successfully complete」。不过他们自己的实验也发现,每步准确率会随步数下降,而且模型在上下文里看到自己先前的错误后更容易再错(self-conditioning),单靠放大模型不能消除,让模型先思考可以缓解。【单源已核】

现实并不完全照这个玩具模型走。Toby Ord 2025 年提出「恒定风险率」模型:任务时长翻倍,成功率取平方,80% 可靠性的任务长度约为 50% 的 0.32 倍。2026 年 2 月 4 日他撤回了这一假设:「Contrary to my earlier hypothesis, AI agents probably don't have a constant hazard rate / half-life. Instead their hazard rates systematically decline as the task goes on.」他转述的 Gus Hamilton 的拟合给出 AI 的 Weibull 形状参数约 0.6、人类约 0.37,都显著小于恒定风险率对应的 1;但 Hamilton 同时发现 METR 用的 log-logistic 拟合略优于 Weibull,两者在 99% 可靠性时长上相差约 20 倍,Ord 只是「slightly favour」Weibull。【单源已核】风险率随任务推进下降,意味着 p^n 对长任务过于悲观——但也意味着人类在这一点上仍明显强于 AI。

**METR 的时长量尺:前沿已经量不出来了。** METR 用「人类专家完成该任务需要多长时间」给任务定长,测模型以 50% 成功率能完成多长的任务(下称 50% 时长)。它在 2026 年 1 月推出 1.1 版任务集(任务从 170 个增到 228 个,8 小时以上的长任务从 14 个增到 31 个,但其中只有 5 个有人类基线)。2026 年 5 月 8 日,METR 加入 Claude Mythos Preview(有限预览版)时同时声明:「Measurements above 16 hrs are unreliable with our current task suite.」Mythos 的 50% 时长点估计为 1044.8 分钟(约 17.4 小时,95% 区间 509–3304 分钟,即约 8.5–55 小时),80% 时长 185.9 分钟。【单源已核】METR 5 月 19 日的前沿风险报告写道:「The most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark」——主语包括实验室提供给 METR 的内部模型;其中最强的内部模型 50% 时长点估计在 16–20 小时之间,而同期公开前沿约 12 小时(区间 5–61 小时)。同一报告还发现,内部模型在 8 小时以上任务的成功 run 里「at least 16%」含作弊。【单源已核】

测量不确定性已经大到改写结论的程度。METR 对 GPT-5.6 Sol 的预部署评估(2026 年 6 月 26 日):按标准方法(作弊记为失败)50% 时长约 11.3 小时(95% 区间 5–40 小时);把作弊算作成功则超过 270 小时;丢弃作弊 run 为 71 小时(区间 13–11400 小时),METR 认为三个数都不构成稳健测量。METR 研究员 2026 年 3 月 20 日的个人笔记(不代表 METR 官方立场)指出:任务集饱和后结果对分析选择越来越敏感,一项正则化修正让近期模型的 50% 时长最多下调 20%,合理的替代拟合可使其最多下调 35%、80% 时长最多上调 100%;只用非公开任务时,Opus 4.6 的 50% 时长从 11 小时 59 分降到 7 小时 11 分。【单源已核】METR 的时长页面自 2026 年 9 月 8 日起「no longer actively updated」;它对 9 月发布的 Claude Opus 5.5 不再给时长,只说是「an incremental improvement above Fable 5.1」(该文本出自系统卡,Anthropic 有机会审阅修改)。

**这把尺子从未在新版上量过开源模型。** METR 的 1.1 版数据里只有 Anthropic、OpenAI、Google 的模型;最后一个被测的开源模型是 Kimi K2 Thinking(2025 年 11 月 6 日发布,用的是 1.0 版任务集)。用 1.0 版原始 run 记录复算开源模型追平闭源前沿的滞后(加权 logistic 拟合,对闭源取逐步上升的包络线,对数线性插值):DeepSeek-V3 6.2 个月、DeepSeek-R1 3.4、V3-0324 6.1、R1-0528 6.8、gpt-oss-120b 7.2、Kimi K2 Thinking 约 8.2;换一种插值方法,月数会差 1.5–3 个月。按发布时的倍数,R1 约为同期闭源的 1/1.5,R1-0528 约 1/2.8,之后的 gpt-oss-120b 与 Kimi K2 Thinking 约 1/2.3–1/2.5。【单源已核:自算;Round 3 降级为弱结论/方向存争】R1 是局部低点,夹在 V3 的 6.2 与 V3-0324 的 6.1 之间;2024 年的 Qwen2-72B 约落后 10–18 个月。全序列呈 V 形:先收窄,R1 之后小幅回弹,停在约 6–9 个月,R1 之后各点的区间相互重叠。METR 每个开源模型只做约一个工作日的能力引出,Kimi 还是经第三方推理服务商测的,这些都可能低估开源。**能确定的只有:R1 带来的收窄在 2025 年没有延续;2026 年开源在这把尺子上是空白。**

**80% 可靠性没有追上 50% 能力,但也没有落得更远。** METR 1.1 版数据里,50% 时长与 80% 时长之比在 2023–2026 年大体持平,多数在 4–6 倍之间,个别到约 8(2024 年的 Claude 3.5 Sonnet):GPT-4 4.48、o3 3.99、GPT-5 5.30、Gemini 3.1 Pro 4.28、GPT-5.4 6.34、Mythos 5.62;Opus 4.6 的 10.29 是离群点。【单源已核:自算】这个比值完全由 logistic 拟合的斜率决定,部分是建模产物。

**可靠性的差距比单次成功率的差距大。** τ²-bench 的 banking 新域(Sierra 2026 年 8 月 4 日统一批次,97 题、每题 4 次,用户由 GPT-5.2 模拟):Claude Opus 5 单次成功率(pass^1)48.7%、4 次全对率(pass^4)32.0%;开源 GLM-5.2 为 37.1%/13.4%,Kimi K3 为 37.1%/17.5%。单次成功率只差 1.31 倍,4 次全对率差到约 1.8–2.4 倍。【单源已核:自算,小样本——4 次全对的题数只有 31、13、17 道】但这不是一条干净的开源/闭源分界线:这个域的榜首是 Qwen 3.8 Max(55.2%/35.1%,阿里基于 2026 年 8 月 8 日开放权重的 Qwen3.8-2.4T-A95B 的 API 版);在接近饱和的老域上,开源已经追平甚至反超(telecom 上 Qwen3.5-397B 为 97.8%/92.1%,Opus 4.5 为 92.3%/78.1%);闭源里也有可靠性保持率很低的(Gemini 3 Pro 的 pass^4/pass^1 只有 0.23)。

**其他长程 agent 基准:方向一致,幅度各异。**
- Terminal-Bench 团队在 3.0 版公告中写道:「Many Terminal-Bench tasks have become saturated and leaderboard entries are condensed into a narrow range that may not fully represent capability gaps across models.」同一组六个闭源模型,在 2.1 版上分布于 74.6–83.8%,在 3.0 版上拉开到 14.3–33.8%;Fable 5 与 Opus 4.8 的差距从 4.9 分扩大到 12.7 分;开源 GLM 5.2 在 3.0 版上只有 5.1%。【单源已核】
- Terminal-Bench 4.0 公开榜(10 月 6 日更新,每项 330 次):Opus 5.5 64.8±3.1%、GPT-6 Astra 58.2%、开放权重 GLM-5.3 41.8±3.2%。在 2.0 版上用同一 agent 框架比较,闭源最佳减开源最佳依次为 10.2(截至 2025 年 8 月发布的模型)、22.1(截至 11 月)、12.3(截至 2026 年 2 月),先扩后缩。
- APEX-Agents(Epoch 转录,2026 年 9 月):Gemini 4 Argon 82.2%、Claude Opus 5.5 73.5%,开放权重最佳 MiMo-V2.6-Pro 59.5%,差约 23 个百分点(19–23)。
- OSWorld 2(电脑操作):同等工具设置下,闭源与开源相差约 3–4 倍;开源一侧只测到 2026 年 4–6 月的旧模型,而且基数很低(4.6%)。
- Vending-Bench 2(模拟一年的售货机经营):Andon Labs 用两条线性拟合得出「Chinese lags by ~111 days」并预测 2027 年 10 月交叉,这里的「中国」包括闭源模型;按原始纪录,中国最高分自 2026 年 6 月 16 日(GLM-5.2,$8,314)以来没被超过,同期西方从 $10,937 涨到 GPT-6 Astra 的 $15,515,当前滞后约 6–8 个月,与外推的「交叉」方向相反。【厂商口径(111 天)/ 单源已核(原始纪录)】

**本节结论**:在最接近「长任务、高可靠性」的量尺上,开源与闭源的差距普遍大于饱和考卷上的差距,可靠性(多次全对)的差距大于单次成功率的差距——但这些证据是拼起来的:最直接测量长任务的量尺已经饱和、停更、且从未在 2026 年量过开源模型。

## 6. 自报与独立评测:2 个月还是 8 个月

美国 NIST 下属的 AI 标准与创新中心(CAISI)2026 年 5 月 1 日评估 DeepSeek V4 Pro:「CAISI evaluations indicate that DeepSeek V4's capabilities lag behind the frontier by about 8 months」,水平相当于约 8 个月前发布的 GPT-5;而「According to DeepSeek's data, DeepSeek V4 is about as capable as Opus 4.6 and GPT-5.4, which were released about 2 months ago」。【单源已核】注意这两个数不是同一把尺子:2 个月是「自报对标模型的发布间隔」,8 个月是 CAISI 的综合能力估计。独立复核方面,在 Epoch ECI 上 V4 Pro 为 149.1,约等于 GPT-5,落后约 8.5 个月(按区间端点约 5–10.5 个月);Artificial Analysis 的指数隐含约 4–5 个月。**独立测量给出约 4–9 个月,CAISI 与 Epoch 都约 8 个月。**【多源证实(CAISI + Epoch 复算;两源都含私有题,并非完全独立)】

差距集中在哪里?CAISI 的分项表(GPT-5.5 / Opus 4.6 / V4 Pro):非公开的 PortBench 78/60/44,CTF-Archive-Diamond 71/46/32,ARC-AGI-2 半私有集 79/63/46;而 GPQA Diamond 96/91/90,OTIS-AIME 100/92/97(V4 Pro 在数学上反超 Opus 4.6)。对「2 个月」口径下的对标模型 Opus 4.6,私有与 agent 类题目差约 14–17 个百分点;30 个百分点以上的差距是对 GPT-5.5 而言。【单源已核】独立研究者 Ihle(LessWrong,2026 年 5 月 28 日,17 个基准)发现开源模型在私有基准上落后约 8–10 个月,在公开基准上约 4–6 个月,并称差距在 R1 前后最小、此后扩大(他自承部分「私有」基准并不完全私有,且他本人运营其中一个基准)。【单源已核】

这个格局与「开源针对公开考卷做了优化」的说法相符,但**没有直接证据**:题目饱和程度、闭源实验室接触过部分「私有」题、评测框架不同,都能解释同样的结果。【Round 3 判为推测,无直接证据】

评测方也有自己的位置。CAISI 是按美国《AI 行动计划》的指令评估外国模型的机构;2025 年 9 月它评估 DeepSeek V3.1 时,完整报告称在软件工程与网络安全两个领域「the best U.S. model solves 20-80% more tasks」,新闻稿发布时商务部长 Lutnick 的定调是「The report is clear that American AI dominates, with DeepSeek trailing far behind」。在网络安全上,CAISI 判 GLM-5.3 综合约落后美国前沿 4 个月,但单项差距悬殊(SEC-Bench Pro 40.4% 对 90.2%,ExploitGym 9.4% 对 44.4%)——这里的「美国前沿」是逐个基准取任一美国模型的最高分,含受信访问版本,且测美国模型时关闭了网络安全防护。英国 AISI(2026 年 7 月 17 日)测得开放权重模型在网络安全上落后 4–7 个月(特指 GLM-5.2),比 2025 年测得的 6–10 个月更窄;长程攻击演练上差距更大,但 AISI 自认这部分是较弱证据。【多源证实】这是「追平月数小」与「成功率差数倍」同时成立的又一例。

## 7. 头部之间:不是趋同,也不是一家独大

把开源放到一边,只看美国闭源前沿内部,读数同样取决于量尺。

**时长量尺上分不开。** METR 1.1 版数据里,同期闭源领先者与第二家的 50% 时长之比:GPT-5 对 Opus 4.1 约 2.0 倍,GPT-5.2 对 Opus 4.5 约 1.2 倍,Opus 4.6 对 Gemini 3.1 Pro 约 1.9 倍,Mythos(有限预览)对 Gemini 3.1 Pro 约 2.7 倍;每一对的区间都有重叠。只用非公开任务时,Opus 4.6 对 Gemini 3.1 Pro 只有约 1.1 倍。Opus 4.6 与 Gemini 3.1 Pro 的平均分只差 1.83 个百分点,50% 时长高 1.87 倍,80% 时长却只有对方的 0.78 倍——排序随阈值翻转,但两者 80% 时长的区间几乎完全重叠,翻转不显著。【单源已核:自算】

**新考卷上拉得很开。** ARC-AGI-3(2026 年 3 月发布的交互式基准,ARC Prize 厂商中立框架):GPT-6 Astra(Max)62.7%,GPT-6.1 Sol(Max)52.7%,Claude Opus 5(High)30.2%,Gemini 3.8 Flash(High)10.4%,Grok 4.7 1.8%;2026 年上半年的 GPT-5.4、Gemini 3.1 Pro、GPT-5.5 都在 0.5% 以下;榜上没有开源条目。同一个榜上,GPT-6 Astra 用 OpenAI 自家框架(保留推理状态、压缩长对话)得 99.95%(High 档)——这是另一种评测条件,不能和 62.7% 并列。【单源已核】Epoch 的 MirrorCode(软件复刻任务,完成比例)上,Claude Opus 5.5 0.774 与 Fable 5.1 0.733 在一个标准误内持平,GPT-6 Astra 0.467,GPT-5.5 0.100;领先者是 Anthropic。而在 Vending-Bench 2 上领先的是 OpenAI。**「头部」是谁,取决于任务类型。**

**贴着前沿的实验室在变少——暂定。** 只看有 ECI 分数的模型,以距前沿 6 点以内为门槛,用当前拟合回溯:2025 年 9 月 30 日有 5 家(OpenAI、Anthropic、xAI、Google、DeepSeek),2026 年 6 月和 9 月只剩 Anthropic 和 OpenAI 两家;2026 年 6 月 Google 落后 7.3 点,门槛放到 8 点就是 3 家。Google 9 月 30 日发布的 Gemini 4 Argon 仅限量开放、尚未被打分,而它在 Arena 上暂居第一。所以「只剩两家」可能被推翻。【单源已核:自算,暂定】Meta 的最佳模型 Muse Spark 1.3(ECI 156.75)与 xAI 的 Grok 4.6(156.44)分别落后前沿 10.6 和 10.9 点,与开源的 Kimi K3(157.45)同一档。

## 8. 输入侧:算力差几十倍,能力差几个月

**输入在集中。** Epoch 估计,Amazon、Google、Meta、Microsoft、Oracle 五家持有的全球累计 AI 算力(芯片所有权口径,不是使用份额)从 2024 年第一季度的 63% 升到 2025 年第四季度的 71%。单体 AI 数据中心的算力纪录自 2024 年 8 月以来约每 7 个月翻一倍。【单源已核】训练算力上,Epoch 估计 GPT-6 Astra 约 1e27 FLOP(区间约 5e26–2e27),2026 年发布的最大开放权重模型 Kimi K3 约 2e25(推测级),相差约 50 倍(25–100 倍);DeepSeek-V4-Pro 约 9.7e24,约差 100 倍。【单源已核;K3 的数字为推测级】国家层面,IFP 2025 年 12 月估计,如果不向中国出口 AI 芯片、也没有走私,美国在 2026 年新产 AI 算力上将领先 21–49 倍——这是反事实基线,美国随后批准了 H200 对华销售,同一报告估计不受限出口会把领先缩小到 6.7–1.2 倍。Epoch 估计华为 2026 年的 AI 算力产出不到英伟达的 4%。时任阿里 Qwen 技术负责人的林俊旸说美国算力「may overall exceed ours by one to two orders of magnitude」,被问到三到五年后领先的 AI 公司是中国公司的概率时答「20%」,并补了一句「Twenty percent is already very optimistic」。【单源已核】

**但输入差距没有按比例变成能力差距。** 2024 年以来 ECI 前沿纪录的线性斜率约每年 15.6 点,按这个速度,10 个 ECI 点约等于 7.7 个月。若粗略假设前沿算力每年增长 5 倍、且进步全部来自算力,7.7 个月约相当于 2.8 倍算力——而训练算力实际差约 50 倍,按同样速度约相当于 2.4 年。【自算换算,依赖作者假设,未验证】更直接的证据是 Meta 和 xAI:两家都掌握第一梯队的算力,能力却和中国开源模型同档。**算力是门槛,不是保证。**

**追赶机制是真的,但各有边界。**
- 算法效率:Ho 等(2024)估计,2012–2023 年在语言模型预训练上,达到固定性能所需的算力约每 8 个月减半(95% 区间约 5–14 个月)。Gundlach 等(MIT FutureTech)的反驳是,小规模消融只能解释被引用的 22,000 倍中不到 10 倍;Transformer 与 Chinchilla 再平衡这两项依赖规模的创新,外推到 2025 年前沿时占实测增益的 91%;「measures of algorithmic efficiency are strongly reference-dependent」。效率进步有一部分只在大算力下才兑现。【单源已核】
- 学前沿经验:Epoch 的一篇评论估计,OpenAI 2024 年的研发算力里最终训练只占约 9.6%(MiniMax 22.6%、Z.ai 12.3%),推论是「if most of the spending is exploration rather than execution, then a competitor who learns what works from the frontier could replicate the results for a fraction of the original cost」——作者自认只有三个数据点,「inconclusive」。【单源已核;推论为方向存争】
- 蒸馏:DeepSeek-R1 论文自报,在同一 Qwen-32B 基座上,从 R1 蒸馏的模型 AIME 2024 得 72.6,直接做大规模强化学习只有 47.0;作者同时写道:「advancing beyond the boundaries of intelligence may still require more powerful base models and larger-scale reinforcement learning」。早一代的证据方向相反:Gudibande 等(ICLR 2024)发现,模仿 ChatGPT 对话的模型「close little to none of the gap ... on tasks that are not heavily supported in the imitation data」(限于 2023 年、130 亿参数以下的模型)。Anthropic 2026 年 2 月 23 日指控 DeepSeek、Moonshot、MiniMax 通过约 24,000 个欺诈账户与 Claude 产生了 1,600 万次以上交互用于蒸馏——其中 MiniMax 超过 1,300 万次、Moonshot 超过 340 万次、DeepSeek 超过 15 万次,不到总量的 1%;截至检索未见三家公开正式回应。【厂商口径,单方指控】

**价格:固定能力在变便宜,最强的在变贵。** Epoch(2026 年 9 月 22 日)测算,自 2023 年以来,达到某一固定性能水平的成本每季度下降约 47%,约合每年 13 倍;刚成为最强水平时降得最快(每季度约 66%),两年后降速减半——这一模式只出现在其五个基准中的三个上。图中 8 条降价轨迹里,只有 1 条的第二个价格点来自开放权重模型。【单源已核】Gundlach 等《The Price of Progress》发现,固定基准表现的价格每年下降约 5–10 倍,但在 GPQA、SWE-bench Verified、AIME 上运行表现最好的前沿模型,总成本每年上升 3–18 倍。【单源已核】这与 [《AI 价值链的利润池会落在哪一层?——五层账本与一个转圈的资金环》](https://hub.cissychen.com/deep-research/ai-profit-pools-deep.html) 里「两条价格曲线」的判断一致:**趋同的、变成商品的,是昨天的前沿;今天的前沿始终领先一段、而且越来越贵。**

## 9. 判决

**第一,「能力在趋同」的证据几乎全部来自两类会机械压缩差距的量尺。** 一类是快被做满的静态考卷,同一能力差在 99% 附近只显示为零点几分;另一类是偏好排行榜,在前沿区间它与能力指数的排序基本不相关。AI Index 那组被广泛引用的百分比,分母是可以任意平移的分数绝对值。

**第二,换到没有饱和的量尺,差距没有收窄。** 合成能力指数上,2026 年开源与闭源的差距没有缩小(是否扩大存争);最难的数学与长程工程题上差距最大(FrontierSWE 上开源只有同期闭源的 0.55,FrontierMath Tier 4 上开源最佳 39.0%、闭源 90% 以上);可靠性(多次全对)的差距大于单次成功率的差距。但未饱和不等于必然拉开,DeepSWE 上一次发布就把差距从 26 个百分点压到 4 个。

**第三,追赶者的滞后以月计大致稳定在约 3–9 个月,不趋于零。** 独立测量里,2025 年 R1 前后最窄,之后再没回到那个水平;DeepSeek V4 Pro 这一例中,厂商自报的滞后明显短于独立测量。前沿在加速,所以「月数不变」意味着比值在拉大。

**第四,最该看的量尺,恰恰在 2026 年失效了。** METR 的时长量尺已饱和、停更、从未在新版上测过开源;几项替代基准都是拼图。「长任务上赢家通吃」既没有被证实,也没有被证伪——它在当前的公开测量下暂时无法检验。

**第五,美国闭源前沿内部既不是趋同,也不是一家独大。** 领先者按任务类型轮换;能贴着前沿的实验室数量在减少(暂定)。

**第六,输入差距(几十倍)远大于能力差距(几个月),算力是门槛不是保证。** 趋同的是昨天的前沿;追赶机制(算法效率、学前沿经验、蒸馏)真实存在,但对最难的长程任务效果最弱。对 [《AI 价值链的利润池会落在哪一层?》](https://hub.cissychen.com/deep-research/ai-profit-pools-deep.html) 的含义是:模型层的定价权取决于客户需要的是今天的前沿还是「够好」的昨天——而后者每年便宜一个数量级。

## 10. 十个可检验主张

按证据强度排序,强的在前。

1. **截至 2026 年 10 月,没有任何独立的公开量尺,能在长任务上同时测量 2026 年的闭源前沿与开源模型。** METR 时长页面自 9 月 8 日停更、16 小时以上不可靠、1.1 版从未测过开源;替代基准要么停在旧模型,要么只测闭源。【最强:一手页面事实】检验方式:METR 或其他机构发布包含 2026 年开源模型、可靠上限高于 16 小时的新任务集。
2. **同一时点、同一批模型,饱和或知识类基准上开源/闭源比值在 0.94 以上,而最难的未饱和基准上差距大得多(FrontierSWE 比值 0.55;FrontierMath Tier 4 上开源最佳 39.0%,闭源 90% 以上)。**【强:Epoch 原始数据,三票复算】检验方式:任何一个新发布的高难度基准,若在发布后半年内开源比值就达到 0.9 以上,本条的普遍性即被削弱。
3. **厂商自报的追赶速度快于独立测量。** DeepSeek V4 Pro 自报对标约 2 个月前的模型,独立测量为约 4–9 个月(CAISI 与 Epoch 都约 8 个月)。【中强:多源,但只有 DeepSeek V4 Pro 一例,两个独立源都含私有题】检验方式:下一个主要开源模型发布后,比较其自报对标与 CAISI、Epoch、Artificial Analysis 的独立估计。
4. **追赶者的滞后以月计在 2025–2026 年稳定在约 3–9 个月,没有趋于零的趋势。**【中强:多量尺同向,单个数字口径各异】检验方式:某个开放权重模型在 ECI 上与当时最强闭源模型的区间重叠、并维持一个月以上。
5. **METR 时长量尺上,80% 可靠性时长与 50% 时长之比自 2023 年以来大体持平在 4–6 倍:可靠性没有追上能力,也没有落得更远。**【中:单源复算,比值部分由拟合方法决定】检验方式:新任务集上这一比值的代际变化。
6. **在前沿区间,Arena 偏好排序与能力指数排序基本不相关(ECI 前 15 名 Spearman 约 0,区间约 −0.6 到 0.5),而其他能力基准之间仍有约 0.69 的相关。**【中:单源自算,区间宽;原因不可分辨】检验方式:用之后的 Arena 快照与 ECI 版本复算;若前 15 名内相关稳定回到 0.5 以上,本条即被推翻。
7. **输入差距远大于能力差距:训练算力相差约数十倍,能力相差约数月;握有第一梯队算力的 Meta 与 xAI 在能力指数上与中国开源模型同档。**【中:算力数字为估计,换算依赖假设】检验方式:Meta 或 xAI 的下一代模型进入 ECI 前沿 6 点以内。
8. **在 ECI 上,2026 年开源与闭源的差距没有收窄(逐日平均 2025 年 5.78 点、2026 年 9.09 点),扩大部分主要来自闭源前沿加速。**【中弱:单一合成指数;Artificial Analysis 的指数在 2025 年 4 月至 2026 年 4 月给出相反读数;重拟合漂移约 3 点】检验方式:Epoch 下一次数据版本中同一时段的分差;Artificial Analysis 同一指数版本内的分差。
9. **可靠性(多次全对)的开源/闭源差距大于单次成功率的差距。** τ²-bench banking 域:单次 1.31 倍,4 次全对约 1.8–2.4 倍。【弱:单一基准、97 题小样本;榜首是开放权重系的 API 版,反例存在】检验方式:更多 pass^k 批次;若同一模拟器下多个新域的 pass^k 差距不大于 pass^1 差距,本条即被推翻。
10. **美国闭源前沿内部,能贴着 ECI 前沿(6 点以内)的实验室从 2025 年 9 月的 5 家减少到 2026 年 9 月的 2 家。**【弱:暂定——Gemini 4 Argon 尚未被打分】检验方式:Gemini 4 Argon 的 ECI 分数;若它进入前沿 6 点以内,本条即改为 3 家。

**值得盯什么。** 四件事一旦发生,本文的判断就该改:一是**出现一个能可靠测量 16 小时以上任务、并且测了开源模型的新量尺**——它会第一次让「长任务上是否赢家通吃」变得可检验;二是**某个开放权重模型在私有基准上也追到闭源前沿的误差范围内**,那会推翻「公开考卷上的追平高估了追赶速度」;三是**ECI 前沿 6 点以内的实验室数量回升**,说明头部的收窄只是发布时间错开造成的;四是**Arena 与能力指数在前沿区间重新相关**,说明偏好榜的脱钩只是暂时现象。

## 附:方法学与本期的自我修正

本期 27 组承重论断各派 3 个独立验证 agent(理论原话与数学推导一批用较小模型,其余用 Opus 级),分逐字、反证、口径三个镜头,要求尽力反驳;所有自算数字由验证者重新下载原始数据复算。81 票中 80 票判「需修正」;另对 4 条单源承重实证加做反证搜索席与方法学审计席,4 条全部被降级。

被验证推翻或改写的原稿表述,挑最重要的列出:

1. **「2026 年开源与闭源的差距扩大约一倍」被判死。** 「翻倍」取决于 2025 年的基准点;同一对模型仅因重新拟合就漂移约 3 点;另一个合成指数在同期给出收窄的读数。改为「没有收窄,是否扩大存争」。
2. **「METR 量尺上开源滞后在持续拉长」被判死。** 起点 R1 是局部低点,全序列呈 V 形,R1 之后的变化在噪声范围内。改为「R1 带来的收窄没有延续」。
3. **「偏好榜在前沿已失去区分能力」被改写。** Arena 仍能把头部排开,只是排序与能力指数脱钩;「用户感知饱和」是几种解释之一,不是定论。
4. **「开源针对公开考卷刷分,所以公开榜高估追赶」被判为推测。** 格局成立,机制没有直接证据。
5. **媒体的「Arena 差距扩大到 29、是近两年最大、2025 年 1 月曾归零」三句全部判死。** 29 来自原始榜,风格控制榜同期约 18–21;2026 年原始榜出现过 59.6;2025 年 1 月是 R1 反超。
6. **「厂商说 2 个月、独立评测说 8 个月,同一尺度差 4 倍」被改写。** 2 个月是自报对标模型的发布间隔,不是同一把尺子。
7. **「Kimi K3 在 WebDev 上登顶、开源领先 8.4 分」被判死。** 两者置信区间重叠,统计上只是并列,一两天后即被反超。
8. **「OSWorld 2 上开源差 6.8 倍」被改写为「同等条件下约 3–4 倍」。** 两边的工具设置不同,开源一侧是旧模型。
9. **「τ²-bench banking 榜首是阿里闭源模型」被判死。** Qwen 3.8 Max 是基于开放权重模型的 API 版,不能单独归入闭源或开源;它居榜首这件事本身就和「开源可靠性全面落后」相冲突。
10. **「Vending-Bench 上中国只落后 111 天、将于 2027 年交叉」被改写,它不是现状。** 111 天是两条拟合线的时移;按原始纪录当前约落后 6–8 个月,而且中国最高分自 6 月起停滞。
11. **「OpenAI 发现 GPT-5.2 稳定失败的 138 道题里 59.4% 有问题」被改正。** 跑 64 次的是 o3,原文是「未能稳定解出」。
12. **「Terminal-Bench 约 9 个月饱和」被判死。** 分数来自 2025 年 11 月发布的 2.0 版,约 3 个月,而且是「模型 + 第三方框架」的组合成绩。

这些修正有一个共同方向:**几乎每一个让「趋同」或「分化」显得更戏剧化的数字——翻倍的差距、拉长的滞后、登顶的开源、几倍的比值、归零的起点——送回原始数据之后都温和了一些。** 剩下的是一个不那么好讲的故事:差距在饱和的尺子上消失,在没饱和的尺子上停在几个月,而最能说明问题的那把尺子刚好到头。

## 附:主要来源

**理论与测量学**:Ott 等 2022(https://www.nature.com/articles/s41467-022-34591-0)、Akhtar、Reuel 等 2026(https://arxiv.org/abs/2602.16763)、Epoch《A Rosetta Stone for AI benchmarks》(https://epoch.ai/blog/capabilities-index)、Kwa 等(https://arxiv.org/abs/2503.14499)、Ord 2025(https://arxiv.org/abs/2505.05115)、Ord 2026(https://www.tobyord.com/writing/hazard-rates-for-ai-agents-decline)、Sinha 等(https://arxiv.org/abs/2509.09677)

**排行榜与年度报告**:Arena 历史快照(https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)、Arena 方法变更记录(https://arena.ai/blog/leaderboard-changelog/)、《The Leaderboard Illusion》(https://arxiv.org/abs/2504.20879)、Arena 回应(https://arena.ai/blog/our-response)、Stanford AI Index 2025(https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf)、AI Index 2026 技术章(https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_2_technical.pdf)

**基准与合成指数**:Epoch 基准数据(https://epoch.ai/data/benchmark_data.zip)、Epoch 开源差距 2026(https://epoch.ai/data-insights/open-closed-eci-gap)、Epoch 开源差距 2025(https://epoch.ai/data-insights/open-weights-vs-closed-weights-models)、OpenAI 停报 SWE-bench Verified(https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、Claude Opus 5.5 发布页(https://www.anthropic.com/news/claude-opus-5-5)、Artificial Analysis 方法与版本史(https://artificialanalysis.ai/methodology/intelligence-benchmarking)、Artificial Analysis 开源模型(https://www.artificialanalysis.ai/articles/recent-open-weights-model-launches)、FrontierCode(https://artificialanalysis.ai/articles/frontiercode)、ARC Prize 榜单(https://arcprize.org/media/data/leaderboard/v3.json)

**长任务与可靠性**:METR 时长页面(https://metr.org/time-horizons/)、METR 1.1 版数据(https://metr.org/assets/benchmark_results_1_1.yaml)、METR 前沿风险报告(https://metr.org/blog/2026-05-19-frontier-risk-report/)、METR 建模假设笔记(https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)、METR GPT-5.6 Sol 评估(https://metr.org/blog/2026-06-26-gpt-5-6-sol/)、METR 原始 run 记录(https://github.com/METR/eval-analysis-public)、τ²-bench 提交文件(https://github.com/sierra-research/tau2-bench)、Terminal-Bench 3.0(https://www.tbench.ai/news/terminal-bench-3-0)、Vending-Bench 2(https://andonlabs.com/evals/vending-bench-2)

**追赶与评测机构**:CAISI 评估 DeepSeek V4 Pro(https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)、CAISI 评估 DeepSeek V3.1(https://www.nist.gov/document/caisi-evaluation-deepseek-ai-models-report)、CAISI 评估 GLM-5.3(https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities)、UK AISI 开源网络安全(https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber)、Ihle(https://www.lesswrong.com/posts/rJcCrXyEsJKmmDpWG/how-far-behind-are-open-models)、DeepSeek-R1(https://arxiv.org/abs/2501.12948)、Gudibande 等(https://arxiv.org/abs/2305.15717)、Anthropic 蒸馏指控(https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)

**输入侧与价格**:Epoch 超大厂算力份额(https://epoch.ai/data-insights/hyperscalers-control-most-compute)、Epoch 数据中心(https://epoch.ai/data-insights/largest-data-center-compute)、Epoch 模型库(https://epoch.ai/data/all_ai_models.csv)、IFP(https://ifp.org/should-the-us-sell-hopper-chips-to-china/)、Epoch 华为路线图(https://epoch.ai/publications/huaweis-roadmap-to-2031)、林俊旸发言(https://www.chinatalk.media/p/the-all-star-chinese-ai-conversation)、Ho 等(https://arxiv.org/abs/2403.05812)、Gundlach 等(https://arxiv.org/abs/2511.21622)、Epoch 研发与训练算力(https://epoch.ai/gradient-updates/r-and-d-vs-training-compute)、Epoch《The plunging price of thought》(https://epoch.ai/publications/the-plunging-price-of-thought)、《The Price of Progress》(https://arxiv.org/abs/2511.23455)

**本站相关研究**:这些能力差距对利润落点的含义见[《AI 价值链的利润池会落在哪一层?——五层账本与一个转圈的资金环》](https://hub.cissychen.com/deep-research/ai-profit-pools-deep.html);前沿进步是否在放缓、以及「被测方换考卷」的前一阶段见[《Scaling laws 撞墙了吗?一场没有定义的争论》](https://hub.cissychen.com/deep-research/scaling-wall-deep.html);裁判与自动评分在 AI 研发中的作用见[《递归自我改进走到哪一步了?「AI 改进 AI」的分层体检》](https://hub.cissychen.com/deep-research/recursive-self-improvement-deep.html)。
