# 锁定口径 · Part 2(G06–G09)

> 文章:「AI 能力最终会趋同是真的吗」(截至 2026-10)。每组三票均为 CORRECTED。冲突处取最严格的修正;数字以有复算或逐字核对的那一票为准,冲突处标出各票的数字。背景审计 04-verification-round3.md(R1/R3)的限定已吸收进相关组。

---

## G06 · Arena 前沿头部分差(#1−#10 / 实验室去重 #1−#5)

**票型**:CORRECTED ×3(三票都是单源已核,用 HF 数据集各自复算)

### (1) 锁定表述

按 Arena 公开历史快照(HF `lmarena-ai/leaderboard-dataset`,风格控制文本榜 overall,每个自然月取最后一个快照)自算,第 1 名与第 10 名的分差如下:2024-12-30 为 75.3,2025-06-24 为 67.3,2025-12-30 为 41.7,2026-08-27 降到 18.7,2026-10-08 又回升到 31.4。

需要同时写明以下几点:
- **序列并不单调**。2025-10-17 只有 16.9,比 2026-08 的 18.7 还低;2025-09 为 28.2,2025-11 回升到 47.4。所以 2026-08 既不是历史最低点,也不能说成单调收敛。
- **月内波动很大**。2024-12 当月 7 个快照在 52.0–75.3 之间,75.3 恰好是当月最大值;2026-09 曾低至 12.8。按月区间看更稳健的说法是:分差从 2024 年末到 2025 年中的约 50–85,降到 2026 年中的约 17–30,2026-09 以后回升到约 31。
- **同一实验室挤占前十**。2026-08 的前十里有 6 个 Anthropic 变体,2026-10-08 有 7 个。#1−#10 收窄有一部分来自这种挤占,不全是跨实验室趋同,所以建议主用实验室去重序列。
- **实验室去重序列**(按 organization 保留各家最高分,再取第 1 与第 5 家之差):75.3(2024-12)→ 42.7(2025-12)→ 23.6(2026-08)→ 40.3(2026-10-08)。organization 标签有别名(Zhipu / Zhipu AI / zai 等),但在这几个时点不影响结果。
- **2026-10 的回升**来自 gemini-4-argon-high:1525.4,95% CI [1516.5, 1534.2],只有 4,892 票,领先第 2 名 claude-opus-5.5-high(1507.1 [1499.0, 1515.2],6,272 票)18.3 分。两者 CI 只是勉强不重叠,而且 #1 票数远少于老模型(6–8 万票),属于早期估计,分数可能回落。2026-08-27 的榜首 claude-fable-5(1507.48)只领先第 2 名 claude-opus-4-6-high(1504.83)2.65 分,两者 CI 重叠。
- **原始榜(无风格控制)**波动更大:2024-06 至 2025-06 的月末值在 40.6–92.0 之间,2025-10 以后在 21.6–57.4 之间,2026-10-08 为 42.6。
- **方法变更让跨年比较只能看方向**:2024-01-09 Elo 改为 Bradley-Terry;2025-05-16 风格控制设为默认并平移 offset(同一模型约 +60);2025-07-23 引入频率重加权(官方承认会加大方差、加宽 CI);2026-05-12 把 Battles in Direct 投票计入榜单(回填 3–5 月),并在 BT 中加入 `is_direct_battle` 与 `same_org_indicator` 两个特征。2025-07→09 的骤降(67→28)恰好跨过重加权上线,不能排除这是方法变更造成的伪收敛。风格控制序列从 2024-08-28 才开始,没有更早的基线。

### (2) 英文原文引语

- 数据集 README:"On January 9, 2024, the rating system was updated from Elo to Bradley-Terry";"On May 16, 2025, style control was made the default ... offset was adjusted";"On July 23, 2025, frequency-based re-weighting was implemented"
- Arena Leaderboard Changelog(2026-05-12 条目):"we added a corresponding feature to the model: is_direct_battle and same_org_indicator"

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| 「原始榜 #1−#10 在 2024-06 至 2025-06 为 73–92」 | 三票复算都是 40.6–92.0(2024-07 为 40.6,2024-08 为 56.9,2025-02 为 52.7) |
| 「原始榜 2025-10 起为 31–43」 | 三票复算都是 21.6–57.4(2025-11 为 57.4,2026-02 为 49.9,2026-08 为 21.6);只有 2026-10-08 的 42.6≈43 成立 |
| 「Arena README 记录了 2026-05-12 BT 加入 same_org 特征」 | README 只记了 3 条(2024-01-09、2025-05-16、2025-07-23);same_org 出自 arena.ai Leaderboard Changelog,而且只针对 Direct 对战投票的同组织偏差,不是全局特征 |
| 把 2026-08 的 18.7 说成历史最低或单调收敛的终点 | 2025-10-17 是 16.9,2026-09 曾到 12.8,2026-10 又回到 31.4 |
| 把跨年分差变化当作同一把尺子下的精确幅度 | 期间有重加权、票源变化和新特征,只能当方向性证据 |
| 「2026-08 领先 2.7 分」不带 CI | 两者 CI 重叠(票 2),应注明 |

**数字冲突**:#1 与 #2 的 CI 间隙,票 1 写 1.3,票 2 写约 1,票 3 写约 1.4;按 1516.548 − 1515.18 计算约为 1.4,可以写成「约 1 分多」。

### (4) 证据分级

**单源已核**(单一数据集,三票独立复算一致)。跨年下降的**幅度**受方法变更影响,只能算**方向性**证据。

### (5) 主要一手 URL

- https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset(`text_style_control/full-00000-of-00001.parquet`、`text/full-00000-of-00001.parquet`、`README.md`)
- https://arena.ai/blog/leaderboard-changelog/

---

## G07 · Arena 闭源第一 − 开源第一的差距

**票型**:CORRECTED ×3(单源已核)

### (1) 锁定表述

口径:Arena 风格控制文本榜 overall,逐快照计算「闭源最高 rating − 开源最高 rating」。开源指 **license 非空且不是 Proprietary**,这个范围包括 Kimi K3 的非商用许可和 Llama 社区许可。

- **年度最小 / 中位 / 最大**:2024 年(2024-08-28 起,22 个快照)为 10.7 / 48.8 / 75.9;2025 年(85 个快照)为 2.7 / 43.0 / 70.4;2026 年(81 个快照,截至 10-08)为 17.7 / 35.1 / 57.7。
- **最强开源模型名次的年度中位数**:8 → 7 → 16。2026 年的 16 有一部分是推理档位重复条目(如 opus-4-6 与 opus-4-6-high)撑大的,去重后约为第 13,不能直接和 2024、2025 年比。
- **登顶情况**:开源模型从未登上风格控制榜第一。原始榜上,2024 年以来只有 DeepSeek-R1 在 2025-01-24 至 02-27 的 11 个快照里反超,领先 3.7–9.1 分。同一时期在风格控制榜上,R1 始终排第 2,差距缩到 2.7–6.7,从未归零。
- **2026-10-08 的差距取决于口径,两种都要交代**:不设票数门槛时为 37.3(闭源第一 gemini-4-argon-high 只有 4,892 票);只看 ≥1 万票的闭源模型时为 16.3(claude-opus-4-6-high 1504.4,79,415 票,对 kimi-k3-max 1488.1,30,351 票)。同一门槛下各月最后快照为:08-27 18.7、09-30 17.5、10-08 16.3。这三个数的变化都在 CI 之内,而且门槛只加在闭源一侧,所以**不构成收窄趋势**。
- **媒体说的「29 分」**出自原始榜(非风格控制)的 2026-08-27 / 09-01 快照,数值为 28.7(claude-opus-5-max 1504.75 / 1504.96 对 kimi-k3-max 1476.06–1476.3)。风格控制榜同期在约 17.7–20.9 之间(08 月底约 18.4–18.7),里面没有 29。文章若引用 29,必须注明是原始榜。发稿前一天(09-02)claude-fable-5.1-max 上榜后,原始榜差距已经是 37.7。
- **Arena 官方 2026-05-07 X 帖**说领先约 +30 分,相当于第 1 名和约第 18 名的距离。数据对得上:风格控制榜 05-06 差 32.1、最强开源 glm-5.1 排第 18;05-07 差 31.7、排第 19;05-14 差 29.3、排第 18。原始榜同日为 31.8 / 第 12,所以这条帖子用的是风格控制口径。

### (2) 英文原文引语

- Arena X 帖(id 2052455463573426452,created_at 2026-05-07T18:28:09Z;**仅票 1 取得全文**):"Today, the proprietary lead is about +30 points. It separates #1 from roughly #18 on the current leaderboard.";"The remaining gap is small in points, but still large in rank";"at its narrowest was almost closed entirely"
- cryptobriefing(2026-09-03,三票逐字):"As of September 2026, the gap ... has ballooned to 29 Elo points";"Claude Opus 5 Max sits at a rating of 1505";"by the largest margin in nearly two years";另有 "The Elo rating gap ... hit zero" / "From zero in January 2025"

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| 开源定义写成「license≠Proprietary」 | 字面照算会把 license 为空的 gpt-5.4-high / gpt-5.4 误算成开源,2026 年中位变成 34.1,04-02 那一期的差距从 48.3 掉到 18.7;应写「license 非空且非 Proprietary」 |
| 「原始榜只有 R1 登顶」(不加时限) | 数据集 2023-05 至 2023-11 的快照里也有开源第一(vicuna、wizardlm),原因是这些快照缺 GPT-4 / Claude。必须加「2024 年以来」(票 3 认为「2023-12 以来」也成立) |
| 媒体「近两年最大差距」 | 原始榜 2026 年就有 59.6(票 3 定位在 2026-02-09,票 1 说是 1 月)、51.1(03-31)、41.9(08-03)、38.3(07-27);2025 年最大 54.0 |
| 媒体「扩大到 / ballooned 到 29」 | 方向也不对:原始榜 7 月下旬是约 38,28.7 接近 2026 年的低位 |
| 媒体「2025-01 差距归零 / 从零起步」 | 原始榜上是 R1 反超(差距为 −3.7 至 −9.1),风格控制榜最小 2.7、没有反超,两种都不是「归零」;以这个月为起点属于挑点(R1 审计) |
| 「8→10 月差距收窄到 16.3」 | 只在「闭源设 ≥1 万票门槛」这种非对称口径下成立,而且三个月的变化在 CI 之内。不设门槛是 37.3(09-30 起都在 36.8 以上);7 月下旬到 8 月初,两种口径给出的趋势相反(不限票 22,限票 38) |
| 只写 16.3、不写 37.3 | 两种口径必须同时报 |
| 「29 来自风格控制榜」 | 风格控制榜同期没有 29;29 是原始榜的数 |

**冲突**:X 帖引语只有票 1 通过 cdn.syndication.twimg.com 和 api.fxtwitter.com 取得全文并逐字核对;票 2、票 3 没取到原帖,标为【未验证】,但两票都没有反证,而且都确认数据层面吻合。锁定为「单源已核」,引用时注明来源是 Arena 官方 X 帖。

### (4) 证据分级

- 年度差距和名次:**单源已核**(单一数据集,三票复算一致)
- 29 分的来源判定:**单源已核**
- X 帖引语:**单源已核**(仅一票取得原文,属当事方口径)
- 媒体的「近两年最大 / 归零」:**判死**

### (5) 主要一手 URL

- https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset(text_style_control / text 全量 parquet)
- https://cryptobriefing.com/arena-ai-frontier-open-weight-model-gap-widens/(2026-09-03)
- Arena 官方 X 帖 status id 2052455463573426452(2026-05-07)

---

## G08 · 前沿区间 Arena 偏好榜与 Epoch ECI 能力排序脱钩

**票型**:CORRECTED ×3(单源已核)。另有 Round 3 R3 审计(counter 与 method 两席)判为「降级为弱结论」,其限定已吸收如下。

### (1) 锁定表述

把 2026-10-08 的 Arena 风格控制总榜和 Epoch ECI(2026-10 下载版)按模型名对齐,共 111 个模型:

- **全样本** Spearman 为 0.95(0.947)。这个数有一部分是不同代际模型之间的时间跨度抬高的:只看 2025-06 以后发布的 70 个模型,降到 0.81;只看 2026 年发布的 55 个,约为 0.72(R3 审计)。
- **ECI 前 30 名**为 0.19,**ECI 前 15 名约为 0**(−0.025)。区间很宽:票 2 的 bootstrap 95% CI 为前 15 名约 −0.60 至 0.53、前 30 名约 −0.14 至 0.48;R3 审计按模型重抽样的 90% CI 为 [−0.52, 0.44]。所以「≈0」只是点估计,要报区间。这个结果对选样方式敏感:按 Arena 而不是按 ECI 选前 15 名,Spearman 约为 0.45–0.54;在全体 ECI 模型里取前 15 再与 Arena 取交集(n=12),是 0.27。
- **不能只用全距限制来解释**。在同一批 ECI 前 15 名模型里,各能力基准两两之间的 Spearman 中位数仍有 0.69(171 对,IQR 0.55–0.79),与 Epoch 自己公布的跨类别中位数 0.68 吻合;单单 Arena 和它们脱钩。去掉风格控制(原始榜)后脱钩反而更明显(前 15 名 −0.07)。
- **但 Arena 并没有失去区分力**(R3 审计)。在前 15 名内,Arena 的秩可靠度约 0.96,头部分差约 51 Elo,CI 平均宽约 11.5;105 对模型里有 39 对 CI 不重叠。它只是按另一种标准排序。
- **可以写的结论**:在前沿区间,偏好榜排序与 ECI 排序基本不相关,偏好榜已不能当作能力的代理指标。原因可能是「用户在日常提示上分不出差别」,也可能是「两者测的构念不同」(对话体验、风格、速度、说服力),还可能是「变体择优和榜单机制压缩了头部」。现有数据区分不了这三种解释。这是用公开数据自算的结果,不是 Arena 或 Epoch 的官方结论。
- **例证**:ECI 把 Opus 5.5(167.33 [164.06, 171.68])排在 Opus 4.6(155.24 [153.36, 157.28])之上 12 分,把 GPT-6.1 Sol(166.09 [162.89, 170.63])排在 Kimi K3(157.45 [155.15, 160.03])之上 8.6 分,两组的 90% CI 都不重叠。Arena 上,claude-opus-5.5-high 为 1507.08 [1498.97, 1515.18](6,272 票,第 2),claude-opus-4-6-high 为 1504.36 [1500.97, 1507.74](79,415 票,第 3),差 2.7 Elo,实际打平。kimi-k3-max 为 1488.08 [1483.39, 1492.77](第 16),gpt-6.1-sol-max 为 1483.72 [1474.56, 1492.88](只有 4,512 票,第 21),差 4.4 Elo,z≈0.8,也是打平。所以只能说「Arena 分不出,而 ECI 拉开且 CI 不重叠」。Opus 4.6 选的是哪一档必须写明:无档位的 claude-opus-4-6 为 1497.73(第 7),它和 Opus 5.5 差 9.3 Elo,z≈3.5,统计上显著。
- **分类目**(2026-10-08 风格控制榜,#1−#10 / 闭源−开源,不设票数门槛):overall 31.4 / 37.3,hard_prompts 33.9 / 33.9,coding 22.4 / 22.4,math 24.5 / 26.6,expert 16.3 / 17.0。只有 coding、math、expert 比 overall 更挤,而且类目内 #1 的 CI 半宽为 coding ±17.2、math ±34.8、expert ±9.4,分差基本落在噪声里。hard_prompts(33.9)比 overall(31.4)还略大,其余类目更宽:multi_turn 55.1 / 53.3,longer_query 40.4 / 40.8,instruction_following 35.8 / 41.1,creative_writing 36.0 / 58.9。前十里有同族推理档位的重复条目,会压缩 #1−#10。
- **Vision**:原始 Vision 榜(2026-10-09)#1−#10 为 10.9,闭源−开源 27.9,最强开源排第 23;风格控制 Vision 榜的 #1−#10 为 15.1。引用时要标明是哪个版本。

### (2) 英文原文引语

无。

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| 「偏好榜在前沿区间已不反映能力差异」/「失去区分能力」 | Arena 头部秩可靠度约 0.96,39/105 对可分,它在区分,只是维度不同;应降为「前沿区间偏好排序与 ECI 排序基本不相关」 |
| 「困难类目都没有把前沿拉开」 | hard_prompts(33.9)> overall(31.4),multi_turn 55.1、longer_query 40.4 更宽;只对 coding、math、expert 成立,而且落在 CI 内 |
| 「Kimi K3 排在 GPT-6.1 Sol 之上」作为倒挂证据 | 两者 CI 大幅重叠,差 4.4 Elo,z≈0.8,Sol 只有 4,512 票,属于打平 |
| 「Opus 4.6 与 Opus 5.5 CI 重叠,所以分不出」(不注明档位) | 用基础版 1497.7 时差 9.3 Elo,z≈3.5,显著;只有用 -high 版(1504.4)时差 2.7 才打平。「CI 重叠=无差别」本身也是统计误读 |
| 「全体 0.95 → 前沿 ≈0」的强对比 | 0.95 被时间跨度抬高,2026 年发布的模型只有约 0.72 |
| 「前沿 ≈0」不带区间 | n=15,95% CI 约 −0.6 至 0.5,要报区间 |
| 「用户感知饱和」作为确定的归因 | 没有经过识别,只能和「构念不同」「变体择优压缩头部」并列,作为几种可能解释之一 |
| 「Vision 前十只差 10.9」不注明榜单 | 10.9 是原始 Vision 榜,风格控制 Vision 榜是 15.1 |
| 闭源−开源 37.3 与 G07 的 16.3 混用 | 37.3 不设门槛,16.3 是闭源 ≥1 万票的门槛口径,全文要统一 |

**匹配口径**:111 个模型里只有 48 个是精确匹配。规则不一致在于:只要有完全同名的条目就不再看 -high 变体(Opus 4.6、4.7、4.8 都受影响),另外有一处 flash-lite 错配。改为所有变体一致取最高分后,前 15 名为 −0.08、前 30 名为 0.18;取最低分时为 −0.025 / 0.235。量级不变。ECI 每次重拟合都会漂移,必须注明是 2026-10 下载版。

### (4) 证据分级

- 「前沿区间 Arena 与 ECI 脱钩」这一描述层:**单源已核**(同一份 Epoch 数据加同一份 Arena 数据的内部稳健性检验,没有独立团队复核;R3 判为弱结论、有限承重)
- 因果解释:**未验证**

### (5) 主要一手 URL

- https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset(text_style_control / text / vision / vision_style_control full parquet,2026-10-08 与 10-09 快照)
- https://epoch.ai/data/benchmark_data.zip(epoch_capabilities_index/eci_scores.csv、processed_data_for_eci.csv,2026-10 下载版)
- https://epoch.ai/data-insights/benchmark-correlations(跨类别中位数 0.68,以及时间跨度会抬高相关的警告;R3 审计引用)

---

## G09 · 《The Leaderboard Illusion》与 Arena 的回应

**票型**:CORRECTED ×3(三票都是多源证实:论文 v1、v2 原文加 Arena 回应原文)

### (1) 锁定表述

Singh 等人的《The Leaderboard Illusion》(arXiv 2504.20879;**引用 v2,2025-05-12**;arXiv 上只有 v1 2025-04-29 和 v2 两个版本)。第一作者、通讯作者和资深作者(Fadaee、Hooker)来自 Cohere Labs / Cohere,合作者来自 Princeton、Stanford、Waterloo、MIT、AI2、UW。Cohere 本身是在 Arena 上参赛的模型提供方,论文自己披露作者提交过 command-r、aya 等模型,并说研究由这段经历驱动;Arena 则称曾帮 Cohere 评测过 9 个预发布模型。**双方都是利益相关方。**

论文的主要发现:

- Meta 在 Llama-4 发布前私测了 27 个文本模型变体(正文另说视觉榜还有 16 个)。
- 按各厂商模型的对战场次份额估计(统计期 2024-01 至 2025-04),Google 和 OpenAI 分别拿到约 19.2% 和 20.4% 的 Arena 数据,83 个开权重模型合计约 29.7%。v2 正文另给出:41 个完全开源模型合计 8.9%,专有厂商合计 61.4%。
- 243 个公开模型中,有 205 个被「静默下线」(对照官方列出的 47 个),其中 64% 是开权重或完全开源模型(v1 为 66%)。「静默下线」是作者自定的代理指标:2025-03-03 至 04-23 期间平均对战 ≤10 场就算,不是 Arena 的下线记录。
- 私测择优带来的分数抬升,论文前后说法不一。v1 全文都是「10 个变体约 +100」。v2 正文和附录 I 改成「20 个变体约 +50」,但 v2 的一处要点总结仍是「10 个变体约 +100」,大概率是修订时漏改。附录 I 还给出:变体完全相同时(N=50、n=3000)偏差约 17.7;变体有真实差异时(σtrue=20)约 56。

Arena 在 2025-05-09 发布回应(2025-06-13 更新):
- 按它自己的模拟,有限数据下 50 次测试、3,000 票后的增益只有约 +11 Elo,并会随新数据归零。这是 Arena 在 BT 假设下的模拟,属当事方口径,不是独立复测。
- 「最好的模型不论来自哪家都会被上采样。」
- 官方统计里开放模型占 40.9%。这个数反驳的是 v1 中「41 个完全开源模型只占 8.8%」的说法,和论文的 29.7%(开权重模型的对战份额)不是同一指标。v2 的开权重 29.7% 加完全开源 8.9%,合计约 38.6%,已经和 40.9% 接近,所以不能把两者写成对立。

### (2) 英文原文引语

论文(v2):
- "At an extreme, we identify 27 private LLM variants tested by Meta in the lead-up to the Llama-4 release."(摘要,v1、v2 一致)
- "Providers like Google and OpenAI have received an estimated 19.2% and 20.4% of all data on the arena, respectively. In contrast, a combined 83 open-weight models have only received an estimated 29.7% of the total data."(摘要)
- "out of 243 public models, 205 have been silently deprecated"
- "Among the models that are silently deprecated, 64% are open-weight or fully open-source"
- v2 要点框 / 要点句:"testing just 10 variants yields a notable increase of approximately 100 points in the maximum score identified"
- v2 正文:"testing just 20 variants yields a notable increase of approximately 50 points";附录 I:"a lift of 50 when 20 non-identical private variants are tested"

Arena 回应:
- "around +11 Elo after 50 tests and 3000 votes"
- "The best models, regardless of provider, are upsampled to improve the user experience"
- "Official Chatbot Arena stats (published 2025/4/27) show Open Models at 40.9%"
- 回应中逐字点名过的论点:"Claim: Pre-release testing can boost Arena Score by 100+ points"

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| 「论文摘要说 10 个变体约 +100 分」 | 三票都确认这句不在摘要里。具体位置有分歧:票 1、票 2 定位在 v2 第 3 节「Section Findings」要点框,票 3 定位在第 1 节引言的贡献要点。锁定写法是「v2 的要点总结(非摘要)仍写 10→100,v2 正文和附录 I 已改为 20→50」。内部不一致属实,但只存在于 v2 |
| 「静默下线的 64% 是开源模型」 | 原文是「开权重或完全开源」;64% 是 v2 的数字,v1 为 66% |
| 把 Arena 的 40.9% 与论文的 29.7% 并列对立 | 指标不同(在榜占比 vs 对战数据份额),而且 40.9% 反驳的是 v1 的 8.8%;v2 口径合计约 38.6%,已经接近 40.9%,并列属于版本错配 |
| 份额数字不带「estimated」,不注明统计期 | 原文用的是 estimated,口径是对战场次份额,统计期 2024-01 至 2025-04 |
| 把「205/243 静默下线」写成 Arena 的官方下线记录 | 这是作者自定的代理指标 |
| 把 +11 Elo 写成独立结论 | 这是 Arena 自己的模拟,属当事方口径;论文附录给出的同类估计是 17.7(变体相同)到约 56(变体有真实差异) |
| 只写作者来自 Cohere、不提利益相关(或只提一方) | Cohere 是参赛方,Arena 是被批评方,两边都要披露 |

### (4) 证据分级

- 论文数字与引语:**多源证实**(v1、v2 原文,三票逐字核对)
- 论文的结论本身:属**利益相关方的研究口径**
- Arena 的 +11 Elo、40.9%、上采样说法:**厂商口径**(逐字属实,但属当事方自述)

### (5) 主要一手 URL

- https://arxiv.org/abs/2504.20879(摘要与版本记录)
- https://arxiv.org/pdf/2504.20879v1
- https://arxiv.org/pdf/2504.20879v2(页脚 "arXiv:2504.20879v2 [cs.AI] 12 May 2025")
- https://arena.ai/blog/our-response(Published 2025-05-09,Last updated 2025-06-13)
