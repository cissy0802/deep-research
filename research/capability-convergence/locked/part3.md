# 锁定口径 · Part 3(G10–G13)

> 文章:「AI 能力最终会趋同是真的吗」(截至 2026-10)。规则:三票冲突时取最严格的修正;数字以复算/逐字核对的那票为准,冲突处列出各票数字;不添加票外事实。背景吸收了 04-verification-round3.md 的 R1(ECI 差距扩大)与 R3(Arena)相关限定。

---

## G10 · Arena 上的开闭源差距(Code Arena WebDev + Agent Arena)

**票型**:CORRECTED ×3(三票均为单源已核,都下载 HF parquet 用 pandas 复算,数字全部复现)

### (1) 锁定表述

- **WebDev 闭源−开源**:用 Arena 公开数据集(HF `lmarena-ai/leaderboard-dataset`)自算,口径为 Code Arena WebDev overall 原始 BT 分(不是风格控制版),开源 = license 非 Proprietary。最强闭源与最强开源的分差,2025-11-26 为 122.8,2026-04-28 为 37.1,2026-08-30 为 14.7。
- **2026-07-26 单日快照**:Kimi K3 Max(1681.8,CI [1669.2,1694.4])的点估计比 Claude Opus 5 High(1673.4,CI [1658.9,1687.8])高 8.4,但两者 CI 重叠,统计上只能算**并列第一**。一两天后 Claude Opus 5 Max 上榜,反超 Kimi K3。
- **2026-09/10 重新拉开**:分差在 2026-09-30 为 160.0,2026-10-08 为 158.7,此时 kimi-k3-max 排第 14。这次拉开主要来自一个刚上榜、票数很少的模型 claude-opus-5.5-max:10-08 只有 2294 票,分数 1813.0,CI 约 ±15(1797.7–1828.4),上榜后分数一路回落(1826.7→1813.0)。如果不算它,次强闭源 claude-opus-5-max 1691.3 对 kimi-k3-max 1654.4,只差约 37。
- **#1−#10 分差**:2025-11-26 为 135.0,2026-04-28 为 80.8,2026-08-30 为 80.4,2026-10-08 为 139.5。但这几个快照的模型池从 21 个涨到 141 个,而且前 10 名里有同一模型的多个变体(thinking/max/high),**跨期不可比**,只能当作各时点的结构描述。
- **Agent Arena**(2026-06-04 上线):这个榜的分数是相对"均匀抽取组件"基线的 IPS 处理效应 τ̂,不是成功率。2026-10-12 的前 15 名全是闭源。#1 Claude Opus 5.5 (Max) τ̂=0.179 [0.137,0.221],最强开源 DeepSeek V4.1 Flash (Max) τ̂=0.033 [0.029,0.037],排第 16。点估计之比约 5.35,用 CI 端点算约 3.6–7.5。注意 Opus 5.5 (Max) 是当天新上榜的,观测量约 61 万,对手约 3194 万;同家族 High 档在 10-08 的比值是 3.78。这个比值**只能描述截至 10-12 的排名结构,不能读成"强几倍",也不能读成趋势**。

### (2) 英文原文引语(逐字)

- Agent Arena 方法论博客对 τ 的定义:"Typically, we take Q to be a uniform distribution over components"
- 同一博客:"We compute the per-signal leaderboards separately, then average them at the end"
- HF 数据集 README:"IPS scores";"score: IPS score (τ̂)";数据起点 "its release on June 4, 2026"
- changelog 关于回填:"will be available in our public HuggingFace datasets soon"

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "2026-07-26 Kimi K3 登顶、开源领先 8.4" | CI 重叠,统计上只是并列;这个状态只在单个快照里出现。反超日期和分数两票有出入:票 1 说 07-27 claude-opus-5-max 以 1725.3 上榜、差距翻成 +43.7;票 2 说 07-28 以 1711.9 上位、当时 1278 票。所以只写"一两天后被反超",不写具体日期和分数 |
| "#1−#10 从 135 压到 80 又扩到 139.5" 当作"挤压后再扩散"的证据 | 模型池 21→141,前 10 含同模型变体,不同池子的分差不可比(三票一致) |
| 不加限定地写"10 月闭源−开源约 160,开源全面落后" | 主要由一个约 2.3k 票、CI ±15、分数还在回落的模型驱动;去掉它只差约 37(票 2、票 3) |
| τ̂ 比值时序 3.43→1.14→2.20→3.42→5.35 当作开闭源差距趋势 | 三票一致判死。基线随模型池漂移:同一模型 Kimi K3 (Max) 的 τ̂ 从 0.105(08-12)降到 0.042(10-02);分母模型换过 5 次(GLM 5.1→GLM 5.2→Kimi K3→Hy4 preview→DeepSeek V4.1 Flash);09-08 模型数从 59 降到 43;09-05 前后观测量从 2.59M 骤降到 0.50M,changelog 里找不到说明;两个接近 0 的数相除本身就不稳定 |
| "闭源强 5.35 倍" / 把 τ̂ 比值当成功率之比 | τ̂ 是相对基线的处理效应,而且是各信号子榜的平均;CI 端点比值区间 3.6–7.5 |
| "Agent Arena 09-30/10-12 总榜方法论改版" | changelog 里 09-30 改的是 Steerability 信号,10-12 是 Bash Recovery→Bash Reliability,都属于信号子榜;方法博客另有一条 10/1/26 methodology update(票 2)。这些改动可能经由平均传导到总分,但回填尚未发布,不能说成"总榜改版"。正确写法:"9 月底到 10 月中信号定义有多次改动" |

**背景限定**(来自 round3 R3/R1,文本榜,非 WebDev):Arena 文本风格控制总榜上的开闭源 Elo 差,用 HF 数据每月末自算,2025-04 到 12 月在 29–62,2026 年在 19–49,2026-10 为 37,看不出扩大趋势。媒体"0→29 Elo 扩大"的说法起点挑在 2025-01 DeepSeek-R1 那一个月。所以不要用 Arena 文本榜去论证"差距扩大"。

### (4) 证据分级

- WebDev 与 Agent 各快照数字:**单源已核**(三票独立复算一致)
- "Kimi K3 07-26 统计并列第一":单源已核
- "10 月分差拉大":单源已核,但**由单个低票模型驱动**,按**方向存争**处理
- τ̂ 比值趋势:**判死**,只能描述单个快照

### (5) 主要一手 URL

- https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset(webdev/full-00000-of-00001.parquet、agent/full-00000-of-00001.parquet、README.md)
- https://arena.ai/blog/agent-arena-methodology/
- https://arena.ai/blog/leaderboard-changelog/(2026-09-30、2026-10-12 条目)

---

## G11 · Epoch 官方的开闭源时间差(4 个月 / 3 个月 / 5–22 个月)

**票型**:CORRECTED ×3(三票均为单源已核,curl 原文逐字核对)

### (1) 锁定表述

- Epoch 2026-05-29 的 Data Insight(作者 Jack Edwards、Luke Emberson)估计:在 **2026-01-01 至 2026-05-28** 窗口内,最强开源权重模型按 ECI 平均落后前沿闭源模型**约 4 个月**。追平的判定标准是开源模型在至少 5% 的配对 bootstrap 样本中超过当时的 SOTA;如果要求开源的点估计严格更高,则为 **6 个月**。平均 ECI 差 **8 点(90% CI 7–11)**。注意这个 90% CI 只属于 ECI 点差,4 个月本身没有给 CI。
- Epoch 自己指出这一估计**可能低估**真实差距,原因有两条:开源模型在私有基准上表现更差,可能因为它们更积极地刷公开基准;闭源实验室也不总发布自家最强模型。
- Epoch 原话是这个差距比它 2025-10 那篇"略大"(slightly larger)。那篇的口径是 **2023-01 至 2025-10 的多年平均**:标题写约 3 个月,正文是 3.5 个月(90% CI 1.1–5.3),ECI 差 7 点(90% CI 0–14)。两版的方法和窗口都不同:2025 版在整段可画线的 ECI 区间上取水平距离,把"差异不显著"算作追平;2026 版按天计算,用 5% 配对 bootstrap 判定。旧版的 CI 已经覆盖 4 个月,所以"变大"在统计上不成立,只能写"Epoch 称略大"。
- 2024-11-04 的 Epoch 报告(Cottier et al.)说开源落后 5–22 个月。这是基于 4 个基准、13 个单基准滞后值的 90% 区间(最大 25 个月),报告的中心结论约 1 年,而且不是 ECI 口径,**不能和 3 个月、4 个月串成一条时间序列**。
- 补充(票 2 用 2026-10 数据算出):2025 年末的开源纪录模型,追平月数已达 6.7 个月(Kimi K2 Thinking)和 7.5 个月(DeepSeek-V3.2)。

### (2) 英文原文引语(逐字)

- "Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of four months"
- "We find an average ECI gap of 8 points, with a 90% confidence interval of 7 to 11 units"
- "if it outperforms that SOTA model in at least 5% of paired bootstrap samples"
- "This estimate would grow to six months if we required that the open-weight model's point estimate for ECI be strictly higher"
- "Two factors mean that our estimate may tend to understate the true gap"
- "open-weight models tend to perform worse on private benchmarks compared to closed models, plausibly because they more aggressively hillclimb on public benchmarks"
- "Leading closed labs do not always release their most capable models, for safety, commercial, or competitive reasons"
- "slightly larger than the one we identified in our October 2025 Data Insight, which found that open models lagged by an average of three months between January 2023 and October 2025"
- 2025-10-30 页:"average "horizontal" time gap of 3.5 months, with a 90% confidence interval of 1.1 to 5.3 months ... average gap of 7 ECI points, with a 90% confidence interval of 0 to 14 units"
- 2024-11-04 报告:"the best open large language models (LLMs) have lagged the best closed LLMs by 5 to 22 months";"90% confidence interval (CI) over all 13 lag values, which is 5 to 22 months"

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "高于 2025 年底的约 3 个月" | 三票一致判死。3 个月是 2023-01 至 2025-10 的多年平均,不是 2025 年底那个时点的差距;Epoch 原话只说 slightly larger |
| "差距从 3.5 个月扩大到 4 个月"(当作同口径趋势) | 方法和窗口都不同,而且旧版 CI 1.1–5.3 覆盖 4,不构成扩大证据 |
| "落后 5–22 个月"与 3、4 个月并列成时间序列 | 13 个单基准滞后值的 90% 区间,中心约 1 年,不是 ECI 口径 |
| "4 个月(90% CI 7–11)" | 7–11 是 ECI 点差的 CI,月数没有给 CI |

### (4) 证据分级

- 引语和数字:**单源已核**(逐字)
- "差距略大于 2025":**机构口径**(Epoch 自述),同源、不独立(round3 R1/R2 也这样判);统计上不显著

### (5) 主要一手 URL

- https://epoch.ai/data-insights/open-closed-eci-gap(2026-05-29)
- https://epoch.ai/data-insights/open-weights-vs-closed-weights-models(2025-10-30)
- https://epoch.ai/blog/open-models-report(2024-11-04)

---

## G12 · 用 Epoch 2026-10 版 ECI 数据自算的开闭源差距

**票型**:CORRECTED ×3(三票均为单源已核,都用 eci_scores.csv 和 eci_bootstraps.json 自算)。月数复刻有冲突:票 1、票 3 复现了 5.9/7.0,票 2 没有复现。按最严格规则处理。

### (1) 锁定表述

- **点估计前沿**(Epoch 2026-10 版数据,开源/闭源按 Accessibility group 划分):截至 2026-10-12,最强闭源 Claude Opus 5.5(2026-09-22)ECI 167.3(90% CI 164.1–171.7),最强开源权重 Kimi K3(2026-07-16,Epoch 标为 Open weights (non-commercial))157.5(90% CI 155.2–160.0)。相差约 **9.9 点**,90% CI 不重叠。
- **季末分差**(同一次拟合):2025-03 5.2、2025-06 6.1、2025-09 5.0、2025-12 9.1、2026-03 10.9、2026-06 10.3、2026-09 9.9。分差是**锯齿状**的:4 月末到 5 月为 11.0,Kimi K3 发布后的 2026-07/08 回落到 5.3(和 2025-10 的 5.3 相当),2026-09/10 又回到 9.9。
- **更稳的写法用时间平均**(round3 R1):逐日平均分差,2025 全年 5.78,2026 年至今 9.09,约 1.57 倍。同一次拟合内的 bootstrap 给出的增幅是 +3.45 点(90% 区间 1.9–5.3)。这个区间只反映拟合内的抽样噪声,不反映重拟合漂移和基准选择的不确定性。
- **年增量**(以 10 月末为年界,最后一段到 2026-10-12,不足 12 个月):闭源前沿 +9.9、+14.5、+17.1;开源前沿 +11.9、+16.0、+12.4。点差变大主要是因为**闭源前沿加速**,不是开源放慢。月数滞后大致持平,"点差 ≈ 月数滞后 × 闭源斜率"(round3 R1)。
- **逐模型追平月数**必须标口径:
  - 严格点估计口径(开源纪录模型发布日 − 闭源首个点估计不低于它的日期):Kimi K2.5 5.7、GLM-5.1 8.0、Kimi K2.6 5.0(票 3 为 5.1)、GLM-5.2 6.9、Kimi K3 4.4 个月,范围 4.4–8.0,逐模型平均约 6.0。
  - Epoch 的 5% bootstrap 口径(票 3):分别为 5.7、4.6、4.3、6.2、2.8,范围 2.8–6.2。
  - 季末严格口径从 2024-12 的 3.6 到 2026-09 的 6.9,但中间不单调(3.6、3.4、6.4、5.5、8.5、7.8、7.4……6.9,2025-12 的 8.5 是峰值);同一序列在 5% 口径下是 0.5→5.3。
- **复刻 Epoch 2026-01-01 至 05-28 窗口**:垂直差约 **9.8 点**,三票一致,结果稳健。时间差**只给区间**,因为各票数字不同:
  - 5% 口径:票 1、票 3 为 5.9 个月;票 2 两种实现为 6.4–7.4 个月。
  - 严格口径:票 1、票 3 为 7.0 个月;票 2 为 7.6–8.5 个月。
  - 锁定写法:"用 10 月数据复刻,约 6–7 个月(严格口径约 7–8.5 个月)、约 9.8 点"。月数对实现细节敏感,约 ±1.5 个月。
- **重拟合漂移**:同一对模型,Epoch 5 月页面内嵌的 ECI 是 GPT-5.5 Pro 159.35、Kimi K2.6 151.60;10 月版分别是 162.07、151.05。2026-05 的点差在 6 月版拟合下是 7.74,在 10 月版下是 11.02,漂了约 3 点,和所说的"扩大"同一量级。2025 年的点几乎不动(2025-10:5.02 对 5.28)。所以 **10 月复刻值高于 Epoch 5 月发布的 4 个月/8 点,只能说明数据版本不同,不能当作差距扩大的证据**;方法复刻偏差和数据漂移也无法分离。
- **月度锯齿只用 ECI 点差表述**:2026-08 为 5.3 点(Claude Opus 5 162.78 对 Kimi K3 157.45),2026-10 为 9.9 点。
- 量尺注意:GPT-5=150、Claude 3.5 Sonnet=130 是 ECI 定标锚点,GPT-5 的 150.0 是定义值,不是测量值。2026 年所有前沿模型都在最高锚点之上 7–17 点,顶端的点距是否等距没有验证过(round3 R1)。

### (2) 英文原文引语

无。本组是自算结果。Epoch 官方引语见 G11。

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "复刻 Epoch 方法得 5.9 个月 / 严格 7.0"(单一月数) | 票 2 用两种合理实现得到宽松 6.4–7.4、严格 7.6–8.5,只有 9.8 点能复现。按最严格规则,月数只给区间 |
| "8 月 3.8 个月、10 月 5.5 个月"(月度月数) | 票 2 未能复现(8 月 4.4–5.4,10 月 4.4–7.1);票 3 也指出这是 5% 口径,严格口径下 8 月约 5.4。月度锯齿只用点差 |
| "2026 年平均 5.4 个月" vs "5.9 个月"作为两个并列结论,且不注明窗口 | 票 1、票 3:5.4 对应 2026-01-01 至 10-12,5.9 对应 01-01 至 05-28,是窗口不同;票 2:两个数都不在可复现范围(逐模型平均 6.0,逐日平均 6.4–7.4)。必须写窗口,并且只给区间 |
| 拿 10 月复刻的 9.8 点 / 约 6 个月对比 Epoch 5 月的 8 点 / 4 个月,论证"差距扩大" | 跨数据版本比较无效:重拟合本身让同一对模型的分差漂移约 3 点(round3 R1、票 2) |
| "2025-10 差 5.0" | 只在 2025-09-30 到 10-06 成立;10-07 GPT-5 Pro 发布后,10 月末是 5.3 |
| "2026-04 差 10.9" | 10.9 是 03-31 或 4 月初的值;4 月内在 7.9–11.0 之间波动,4 月末是 11.0 |
| 季末严格口径 3.6→6.9 写成"稳定扩大" | 序列不单调,2025-12 的 8.5 是峰值 |
| 同一段落混用严格口径和 5% 口径的月数 | 两种口径差距很大,例如 Kimi K3 是 4.4 对 2.8 |
| "2026 年分差比 2025 年扩大约一倍" / 用 9–11 点做快照对比 | round3 R1:"翻倍"取决于选哪个 2025 基准点(2025 年内在 3–9 之间来回)、快照时点(2026-08 和 2025 一样)和拟合版本;时间平均只有约 1.57 倍,6 月版拟合下约 1.3–1.6 倍 |

### (4) 证据分级

- 点估计、CI、季末序列、年增量、逐模型严格口径月数:**单源已核**(三票复现)
- "在 ECI 上 2026 年差距没有收窄":**单源已核**,并有多源同向支撑(round3:Epoch、AA 2026 下半年、Arena 持平、CAISI 水平证据)
- "差距扩大(点数)":**方向存争**。只有 ECI 单源支持;AA 2025-04→2026-04 是从 13 收窄到 6(round3 R1)
- 复刻月数:**未验证到单一值**,只给区间

### (5) 主要一手 URL

- https://epoch.ai/data/benchmark_data.zip(2026-10 版:epoch_capabilities_index/eci_scores.csv 274 行、eci_bootstraps.json 500 个 bootstrap、ci_level=0.9)
- https://epoch.ai/data-insights/open-closed-eci-gap(用来比对 5 月版内嵌的 ECI 表)

---

## G13 · 分基准的开闭源差距(饱和 vs 未饱和、倒 U、代理型基准)

**票型**:CORRECTED ×3(三票均为单源已核,都用 Epoch 2026-10 benchmark_data.zip 复算)。共同口径:窗口取发布日 ≥2025-10-12;开源 = model_metadata.accessibility 以 "Open weights" 开头(含 non-commercial 的 Kimi K3)。

### (1) 锁定表述

- **GPQA Diamond(已饱和)**:最佳闭源 GPT-6 Astra 95.8% 对最佳开源权重 Kimi K3 93.1%(非商用许可),差 2.7pp。只算无限制开源时两票数字不同:票 2、票 3 是 GLM-5.2 91.9%,差 3.9pp;票 1 是 DeepSeek V4 Pro 0813 91.7%,差 4.1pp。写"约 4pp"。前几名闭源之间的差距在误差以内。
- **FrontierMath Tier 4 v2(41 题,未饱和)**:
  - GPT-6.1 Sol 在 Epoch 表中记为 100%,stderr 为 0,没有公开日志,无法独立核验;票 2 指出分不清是 41/41 还是 40/40。
  - GPT-6 Astra 97.6%(medium 档正好是 40/41)。
  - Claude Opus 5.5 在 Epoch 表中记为 95.0%,但这个数不是 41 题的整数比,用 stderr 反推,票 1 得 n≈29,票 3 得 n≈28,票 2 认为是 38/40。所以必须注明运行口径不同。
  - 最佳开源 Kimi K3 39.0%(16/41,非商用权重);只算无限制开源,最佳是 26.8%(DeepSeek V4 Pro 0813 / V4.1 Flash)。
  - 最佳中国模型是闭源的 Qwen3.8 Max 46.3%(19/41),这是 08 月版;0902 版降到 34.1%。
  - 发布日没有对齐:GPT-6.1 Sol 是 2026-09-29,Kimi K3 是 2026-07-16。
- **FrontierMath Tier 1–3 v2**:93.7(GPT-6.1 Sol / GPT-6 Astra)对 72.2(Kimi K3);中国最佳是闭源 Qwen3.8 Max 74.7。
- **SimpleQA Verified**:75.6(GPT-6 Astra)对 52.9(DeepSeek V4 Pro 0813);中国最佳是闭源 Qwen3.7 Max 55.8。
- **趋势形状**(每月月末累计前沿,即截至当月的闭源最佳 − 开源最佳):
  - **ARC-AGI-1(倒 U 成立)**:2025-05/06 约 39.6pp(o3 60.8 − R1-0528 21.2);2025-07 Grok 4 发布后 45.5;2025 年底达峰,两票数字不同(票 1:2025-11 58.8;票 3:2025-12 69.3),写"2025 年底约 59–69pp";2026-07 Kimi K3 发布后降到 4.0pp(Fable 5 98.5 对 Kimi K3 94.5),此后一直是这个值。
  - **ARC-AGI-2(倒 U 成立)**:2025-05/06 为 7.3pp;2026-04 为 73.2pp(GPT-5.5 xhigh 85.0 − Kimi K2.5 11.8);当前值取决于数据源:Epoch 数据 29.2pp(95.0 − GLM-5.3-Flash 65.8);ARC Prize 官方 v2.json 22.1pp(对 DeepSeek V4.1 Flash 72.9);如果把第三方列为开源权重的 Dots3-Note Preview(76.8)算进来是 18.2pp。
  - **AIME(OTIS mock)和 GPQA 不是倒 U**:都是从 2024-12 的高点单调收敛。AIME 2024-12 为 57.5pp,2025-07 开源已经反超(票 2 −1.9、票 3 −2.2,Qwen3-235B-Thinking-2507 86.7 高于闭源),2026-08 起为 1.4pp。GPQA 原始分差 2024-12 为 20.2pp,2025-07 为 6.9pp,现在 2.7pp。
- **DeepSWE**(所有行都用同一个 mini-swe-agent harness):2026-06 底是 Fable 5 69.9 对 GLM-5.2 43.8,差 26.1pp;2026-07-16 Kimi K3 发布(68.5),当天降到约 4.2pp,7 月底 5.1pp,2026-10 是 GPT-6 Astra 74.1 对 68.5,差 5.6pp。差距是**一次发布就缩小**的,此后基本不变。限定:只算无限制开源(GLM-5.3-Flash 63.4)时差 10.7pp;DeepSWE 上开源只有 5 个条目,没有 DeepSeek。
- **FrontierCode 1.1(Artificial Analysis 统一 Stirrup harness,2026-10-12)**:Claude Opus 5.5 52%(榜单精确值 52.2%),最佳开源权重 MiMo-V2.6-Pro 45%,DeepSeek V4.1 Flash (max) 和 Kimi K3 (max) 各 44%。**不能**和 Anthropic 自报的 54.4%,或 Epoch/Cognition 口径的 Opus 5.5 54.6(claude-code harness)对 Kimi K3 44.2(mini-swe-agent harness)、差约 10.5pp 的数字混用。
- **HLE**:只能写"Epoch 对开源覆盖不全"。近 12 个月共 18 行,开源只有 Kimi K2.5(2026-01)24.4,对 GPT-6 Astra 54.8,两者发布相隔约 7 个月,**不作为分差证据**。

### (2) 英文原文引语(逐字)

- AA FrontierCode 文章(2026-10-12),票 1、票 2 一致:"MiMo-V2.6-Pro is the leading open weights model at 45%, followed by DeepSeek V4.1 Flash (max) and Kimi K3 (max) at 44%"
- Opus 5.5 那一句两票引文不同,**不要当逐字引语用**,只写中文"Opus 5.5 以 52% 领先":
  - 票 1:"Claude Opus 5.5 (max with fallback) leads with an average score of 52%"
  - 票 2:"Claude Opus 5.5 (max with fallback) leads at 52%"

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "GPT-6.1 Sol 100%(41 题全对)" | 只是单次运行,没有公开日志,stderr=0 是公式结果;票 2 指出分不清 41/41 还是 40/40。只能写"Epoch 表记 100%" |
| "Opus 5.5 95.0%"当作干净的 41 题成绩 | 不是 k/41 的整数比,三票反推的分母都不是 41 |
| "最佳中国模型 Qwen3.8 Max 46.3%"不注版本 | 这是 08 月版;0902 版只有 34.1% |
| "HLE 54.8 vs 24.4"当作当前开闭源差距 | 开源只有 1 个模型,而且早 7 个月 |
| "ARC-AGI-1 2025-07 差 39.6pp" | 39.6 是 2025-05/06 的值,2025-07 是 45.5;中间峰值被漏写;4.0 从 2026-07 起就是这个值 |
| "AIME 57.6pp(2025-07)→1.4"作为倒 U | 票 2、票 3 判死。2025-07 实际是开源反超(−1.9 或 −2.2);57.5 出现在 2024-12;AIME 是单调收敛,不是倒 U |
| "GPQA 27.0→3.5" | 票 2、票 3 判死。任何时点都复算不出原始 27.0;票 1 指出 27.0≈20.2/0.75 是扣除随机基线后的归一化值,和其他基准的原始 pp 混在一起;现值是 2.7,不是 3.5 |
| "ARC-AGI-2 7.3→71.5(2026-04)→33.6" | 71.5 和 33.6 都不能用一致方法复算(33.6=95.0−61.4,漏了 GLM-5.3-Flash 和 V4.1 Flash);改用 73.2→29.2(Epoch)/ 22.1(ARC 官方) |
| "DeepSWE 2026-07 差 26.1pp → 2026-10 5.6pp" | 26.1 是 2026-06 底的值;差距在 7-16 一次发布后就收窄了,不是 7→10 月逐步收窄 |
| FrontierCode 混用 AA 52/45/44 与 Anthropic 自报 54.4、Cognition 54.6/44.2 | harness 和来源都不同,分差从约 7pp 到约 10.5pp 不等 |
| 不加限定的"开源"(Kimi K3 算开源) | Kimi K3 是 non-commercial 开源权重。必须注明;无限制口径下,GPQA 约 4pp,DeepSWE 10.7pp,FM T4 最佳 26.8% |

**票间冲突**:票 3 把 FrontierCode 的 AA 数字判为"找不到一手来源、降为未验证"。票 1、票 2 都 curl 了 AA 文章并逐字引用,票 1 还核对了 AA 榜单精确值 52.2%。票 3 的判定是"没找到",不是一手反证,所以保留 AA 数字,但证据等级标为"单源已核(2/3 票核到原文)",并且不用有分歧的那句引语。

### (4) 证据分级

- GPQA、FM T1–3、FM T4 中的 Kimi K3 / Qwen 数字、SimpleQA:**单源已核**(Epoch 数据,三票复现)
- FM T4 的 GPT-6.1 Sol 100%、Opus 5.5 95.0%:**厂商/数据表口径,未独立核验**
- ARC-AGI-1/2 倒 U:**单源已核**;ARC-AGI-2 的当前值**随数据源不同**(29.2 / 22.1 / 18.2)
- AIME/GPQA 单调收敛:单源已核
- DeepSWE:单源已核(harness 统一,但开源样本只有 5 个)
- FrontierCode AA 数字:**单源已核**(2/3 票核到原文,1 票未找到)
- HLE 分差:**禁用**

### (5) 主要一手 URL

- https://epoch.ai/data/benchmark_data.zip(gpqa_diamond.csv、frontiermath_tier_4_v2.csv、frontiermath_tiers_1_3_v2.csv、simpleqa_verified.csv、hle_external.csv、arc_agi_external.csv、arc_agi_2_external.csv、otis_mock_aime_2024_2025.csv、deepswe_external.csv、frontiercode_external.csv、model_metadata.csv)
- https://arcprize.org/media/data/leaderboard/v2.json(generatedAt 2026-10-05)、v1.json
- https://artificialanalysis.ai/articles/frontiercode
- https://artificialanalysis.ai/evaluations/frontiercode
