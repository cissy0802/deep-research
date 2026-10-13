# 锁定口径 · Part 1(G01–G05)

文章:「AI 能力最终会趋同是真的吗」(截至 2026-10)。每组 3 票全部为 CORRECTED;三票冲突时取最严格修正,数字以有复算或逐字核对的那票为准,冲突处列出各票数字。背景吸收:04-verification-round3.md(R1 ECI 差距、R3 Arena 感知)中与本组相关的限定。

---

## G01 · 基准饱和:Ott 2022 / Epoch / Akhtar-Reuel 2026 / METR 时间视野

### (1) 锁定表述

- **Ott 等(Nature Communications 13:6793,2022;数据约截至 2021,仅 CV 与 NLP,属前 LLM 时代)**:作者整理了 3765 个基准(纳入分析的总数,每个至少有一条结果),发现相当一部分基准很快趋近饱和。其中只有部分基准有 ≥3 个时点的结果可以做趋势分析,见下方冲突说明。引言另有一句:近饱和基准上,模型性能差异的统计显著性"更难取得"。这是作者在引言中带引用的**动机性论述**,不是对 3765 个基准的实证发现。正文用词"sizable portion ... key domains such as NLP"比摘要弱,不要给出具体百分比。
- **Epoch(Anson Ho,"A Rosetta Stone for AI benchmarks",2025-12-02)**:"只有当模型处在中间区间、不太好也不太差时,才能比较它们。"这是 Epoch 构造 ECI、讨论基准区分度时的方法论前提,不是关于模型能力趋同的实证结论。下文紧接着说模型进步太快,停留在中间区间的时间很短。
- **Akhtar、Reuel 等(arXiv 2602.16763 v4,2026-08-06 修订;ICML 2026)**:在 60 个文本类语言模型基准中,有 29 个(48.3%,即"近半")的 Sindex≥0.7,作者归为高或极高饱和,其中 14 个≥0.9。饱和比例随基准年龄上升。"饱和"按作者自定义,指顶尖模型之间在统计上失去可靠区分力,不等于达到人类水平。阈值 Sindex≥0.7 和 top-k(k=5)压缩定义也都是论文自定的。专家策划的基准抗饱和性更好,但这是相关性证据,且是在控制年龄之后才出现的;作者承认年龄是混淆因素,无法判断方向。测试集公开与否未见显著差异,但对比组是公开 56 个对私有 4 个,检验力很弱,只能说"未发现显著差异",不能说"证明无关"。
- **METR(Kwa 等,arXiv 2503.14499 v4,2026-07-10;v4 标题已改为 "Measuring AI Ability to Complete Long Software Tasks")**:v4 第 3.2.1 节写道,模型的 80% 时间视野比 50% 短 4–6 倍(TH1.0 数据;80% 倍增期 204 天,50% 为 207 天)。v1/v2 写的是约 5 倍(80% 倍增期 213 天)。TH1.1 yaml 复算的 p50/p80 比中位为 5.34,范围 3.99–10.29(口径见 G03),上沿超出 4–6 倍,两版数据不能混用。附录指出,任何饱和 logistic 曲线的起始段都与指数极为相似;在没有放缓证据时,无法预测何时、甚至是否会趋平。这句话的语境是论证为何不用多参数曲线拟合"时间视野—发布日期"的趋势,不是在讨论基准饱和。
- Ott 和 Akhtar 的年代与对象不同:前者是约 2021 年的 CV/NLP SOTA,后者是 2025 年前后的 LLM 基准。合引时不能串成同一条实证序列。

### (2) 英文原文引语(逐字)

- Ott(摘要,arXiv 版):"We curated data for 3765 benchmarks covering the entire domains of computer vision and natural language processing, and show that a large fraction of benchmarks quickly trended towards near-saturation"。发表版用现在时 "trends"。
- Ott(引言):"statistical significance of differences in model performance is more difficult to achieve"
- Ott(引言正文):"a sizable portion of novel benchmarks in key domains such as NLP quickly trended towards saturation"
- Epoch:"We can only compare models when they're in the middle — not too good and not too bad."(原文撇号为弯引号)
- Akhtar 等(摘要):"We find that nearly half of our benchmarks exhibit saturation, with rates increasing with age. Further, we find that resilience to saturation is impacted by expert-curation, not by public test data."
- Akhtar 等(正文):"Hiding test data does not appear to prevent saturation once benchmarks are widely adopted";"We find no statistically meaningful difference in Sindex between the two groups"
- Kwa 等 v4:"models' 80% time horizons are 4-6x shorter, suggesting that even models that sometimes succeed on difficult and diverse tasks cannot reliably perform tasks of moderate length"
- Kwa 等(附录):"the initial part of any saturating logistic function horizon ∼ a · σ(release date + d) looks very similar to an exponential, and without any evidence that AI horizon is leveling off (on our metric), it is essentially impossible to predict when or if it will plateau"。必须连同后半句一起引用。

### 冲突记录

- **Ott 3765 的领域拆分**:票 1 写 1318 NLP + 2447 CV,票 3 写 1318 CV + 2447 NLP,两票相反。锁定:**不写领域拆分**,只写总数 3765。
- **≥3 个时点的子集**:票 2 写 3765 个中有 1935 个(51%)有 ≥3 个时点;票 1 写"NLP 中仅 50% 有 ≥3 个时点"。锁定:写"其中只有约一半(票 2 复算为 1935 个,51%)有 ≥3 个时点、可做趋势分析",不写成"每个基准都有时序"。
- **Epoch 引语的语境**:票 1 认为是基准区分度,票 3 认为是 ECI 构造的方法论要求。两者不冲突,合并为"构造 ECI 时对基准区分度的方法论前提"。

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "Ott 等研究发现,饱和使统计显著性更难达到" | 这是引言中引用他人文献的动机论述,不是实证发现。只能写"Ott 等指出" |
| "3765 个基准都趋近饱和"/当作 LLM 基准 | 3765 是纳入总数,仅约一半有 ≥3 个时点;范围是 CV+NLP,截至约 2021 |
| 引用 Ott 早期版本的 1688 | 必须用发表版的 3765 |
| 给 Ott 的 "large fraction" 配具体百分比 | 原文没有百分比,正文用语更弱 |
| 把 Epoch "in the middle" 当作"模型能力趋同"的论据 | 它是基准区分度和 ECI 构造的前提 |
| "抗饱和取决于专家策划,而不是测试集是否公开"(作为因果结论) | 这是相关性;年龄混淆;私有基准仅 4 个,"无显著差异"不等于无影响 |
| 把 Akhtar 的"饱和"写成"达到人类水平" | 作者定义是顶尖模型统计不可分,并明言人类水平不等于饱和 |
| 不注版本地写 METR "4–6 倍" | 4–6x 只出现在 v4(TH1.0);v1/v2 是约 5 倍;TH1.1 复算是中位 5.34、上沿 10.29 |
| 只引 logistic 句的前半句,暗示"METR 承认会饱和或趋同" | 原文结论正好相反:没有放缓证据,无法预测何时、是否见顶 |
| 把 Ott 与 Akhtar 串成一条连续的实证序列 | 年代、对象、定义都不同 |

### (4) 证据分级

- 多源证实(三票均为多源证实,逐字核对 PDF):Ott 摘要与引言引语、Epoch 引语、Akhtar 29/60、Kwa v4 引语。
- 方向存争 / 弱:Akhtar 中"公开与否无影响"和"专家策划"两项(N=4、年龄混淆)。

### (5) 主要一手 URL

- https://arxiv.org/pdf/2203.04592 ;https://www.nature.com/articles/s41467-022-34591-0
- https://epoch.ai/blog/capabilities-index
- https://arxiv.org/pdf/2602.16763 (v4)
- https://arxiv.org/pdf/2503.14499 (v1/v2/v4)

---

## G02 · 文章自做的数学推导(logit 压缩 / 串联成功率 / Elo 胜率 / 倍增期换算)

### (1) 锁定表述

以下数字由三票分别用 Python 复算,全部复现。每条都必须明写前提。

- **(a) logit 压缩**:假设两模型位于同一 logistic/IRT 刻度上,且相差一个固定的 logit 差。演示时**设定** Δlogit=0.847(=ln(7/3),恰好让 50% 变为 70%)。以**较弱模型的得分**为基线,基线为 50/90/95/99% 时,同一能力差只表现为 20.0/5.45/2.79/0.57 个百分点,前后压缩约 35 倍(35.1)。若改以较强模型的得分为基线,分差为 20.0/10.58/5.93/1.30pp,压缩约 15 倍(15.4)。20pp 是构造值,不是实测。题目难度异质时,压缩幅度会变化。
- **(b) 串联成功率(玩具模型)**:假设各步独立、难度相同、每步成功率恒定、一步错则整题失败。0.95^50≈7.7%(7.69%),0.99^50≈60.5%(60.50%)。50% 可完成步数 H50=ln0.5/ln p:p=0.99、0.995、0.999 时分别约 69、138、693 步。p→1 时 H50≈0.693/(1−p),所以错误率降为 1/k,可完成步数大约增加 k 倍。例如 0.995→0.999,错误率降 5 倍,长度增 5.01 倍。这只是近似,不是精确等式。该前提与实测相冲突:Ord 2026 发现风险率递减,Sinha 等发现每步准确率随步数下降(见 G03)。因此这一模型只能当作直觉或理想化估计。
- **(c) Elo/BT 胜率**:P=1/(1+10^(−Δ/400))。分差 10/20/30/49/100/200 分别对应单局胜率 51.4/52.9/54.3/57.0/64.0/76.0%(200 分实为 75.97%)。这是不计平局的 Bradley-Terry 两两偏好概率,不是基准准确率。对 Elo 绝对值取百分比没有意义。
- **(d) 倍增期换算**:设前沿时间视野的倍增期为 D 个月,则落后 L 个月对应的倍数 R=2^(L/D),即 L=D·log2R。取 D=4.23 个月(METR TH1.1 yaml 中 `doubling_time_in_days.from_2023_on` 的点估计 128.744 天,CI 104.4–158.0 天,约 3.4–5.2 个月),L=4 时 R≈1.93。固定 L=4,D 从 7 降到 3.5 个月时,R 从约 1.49 升到约 2.21。前提是倍增期恒定的纯指数增长,追赶者与领先者沿同一曲线;METR 自己说无法区分指数与饱和 logistic 的初段。D 的取值有三种口径,不能混用:TH1.1 from_2023_on 为 4.23 个月,TH1.1 all_time_stitched 为 187.8 天(约 6.2 个月),论文摘要头条为约 7 个月(自 2019 年起)。

### (2) 英文原文引语

无(纯数学推导)。

### 冲突记录

- **(b) 措辞**:票 1 写"长度比近似等于错误率之比",票 2 指出应为"错误率比的倒数",票 3 写"错误率反比"。取最严格:锁定为"错误率降为 1/k → 可完成步数约增 k 倍(H50≈0.693/(1−p))"。
- **证据级别**:票 3 标"单源已核"(无一手来源,纯数学),票 1、2 标"多源证实"。取严:**单源已核(自算复现)**。

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "35 倍压缩"不注基线 | 以较强模型为基线时只有 15.4 倍 |
| "观察到 20pp 差距" | 20pp 是由 Δ=0.847 倒推的构造值 |
| "长度比≈错误率比" | 方向写反或含糊,应为倒数关系 |
| 不声明独立恒定 p 就用 H50 或 0.95^50 推真实 agent | 与 Ord 2026、Sinha 等的实测冲突 |
| 把 Elo 分差换算成"能力差百分比",或对 Elo 绝对值取百分比 | BT 只是两两胜率,绝对值可任意平移 |
| D=4.23 不注来源和窗口,或与 6.2、7 个月混用 | 三个拟合窗口不同 |

### (4) 证据分级

单源已核(数学自算,三票复现)。D=4.23 回溯到 METR yaml,已核。

### (5) 主要一手 URL

- https://metr.org/assets/benchmark_results_1_1.yaml (doubling_time_in_days 字段)

---

## G03 · 风险率模型:Ord 2025 恒定风险率 → Ord 2026 撤回 / TH1.1 p50/p80 复算 / Sinha 等 ICLR 2026

### (1) 锁定表述

- **Ord 2025(arXiv 2505.05115,仅 v1,2025-05-08,预印本)**:在 Kwa 等的研究工程任务套件内,Ord 提出恒定风险率模型,即人类做该任务的每一分钟里 AI 都以恒定速率失败。由此得出经验法则:任务时长翻倍,成功率取平方;T80=ln0.8/ln0.5≈0.322·T50(复算 0.3219)。论文中 Kwa 对 Claude 3.7 Sonnet 的估计比值为 0.25(TH1.0),Ord 称其与 0.322 接近且在误差范围内。但 TH1.1 yaml 中该模型的 p50/p80 比为 4.99。作者自己说明,这个模型是否更普遍适用"未知"。
- **Ord 2026-02-04 博文已撤回上述假设**:AI 智能体大概不是恒定风险率,风险率随任务推进系统性下降。Weibull 分析由 **Gus Hamilton** 完成,Ord 转述并背书:各模型的 k 集中在约 0.6,人类约 0.37,每个模型的 k 都显著低于 1;模型进步主要体现在 λ 上,k 变化很小。k<1 意味着,长于 50% 视野的任务,成功率好于恒定风险模型的预测;短于 50% 视野的则更差。Hamilton 同时发现 METR 的 log-logistic 拟合略优于 Weibull,两者在 99% 可靠性视野上相差约 20 倍。Ord 只是"slightly favour" Weibull,并称 99% 视野"deeply uncertain"。Hamilton 的初步结果早于 METR 加入 Opus 4.5 数据。
- **TH1.1 yaml 复算(METR-Horizon-v1.1,共 26 个带 p50/p80 的模型;本次下载含截至 2026-04 的模型)**:2024-01-01 起发布(含 2024 年)的 21 个模型,p50/p80 比中位 5.34(5.337),范围 3.99–10.29。最大值来自 Claude Opus 4.6(718.8/69.9),最小值来自 o3(119.7/30.0)。恒定风险率的预测是 3.11(ln0.5/ln0.8=3.106),实测更高。用两个分位点反推 Weibull,k=ln3.106/ln(比值),中位约 0.68(0.677),逐模型 0.49–0.82。若只看 2025 年起的 14 个模型,中位比 5.15,k 约 0.69。剔除 p50 超过 16 小时的 Mythos 后,20 个模型中位比 5.32,结果稳健。限定:METR 的 p80 来自 log-logistic 拟合,所以这个 k 只是"两点映射",不是 Weibull 直接拟合,与 Hamilton 的约 0.6 **不是同一个量**。0.68 与 0.6 的差距既不能读成矛盾,也不能读成确认,只是方向一致(k<1)。p80 的置信区间很宽;最大比值靠近任务套件上限,不稳。yaml 会随 METR 更新漂移。
- **Sinha 等("The Illusion of Diminishing Returns",arXiv 2509.09677 v3,2026-03-13;已作为 ICLR 2026 会议论文发表)**:短任务基准可能制造"进步放缓"的错觉,因为单步准确率的微小提升,会复合成可完成任务长度的指数级提升。这是在恒定单步准确率近似下的算术推论。实验任务是人为构造的受控执行任务(显式给出知识与计划),不是对开放式智能体工作的实测。论文自己还发现两点:每步准确率随步数下降;存在 self-conditioning,即上下文中含有自身先前错误时更容易再出错,单靠放大模型规模不能消除,thinking 可以缓解。Sinha 的 self-conditioning("错误引发更多错误")与 Ord 2026 的"风险率随任务推进下降"是**不同机制**,不可混用。

### (2) 英文原文引语(逐字)

- Ord 2025:"if you double the task duration, you square the success probability"
- Ord 2025:"This constant hazard rate model would predict that the time horizon for an 80% success rate is about ⅓ of the time horizon for a 50% success rate"
- Ord 2025:"an 80% time-horizon would be ln(0.8)/ln(0.5) = 0.322 times as long as the 50% time-horizon. Kwa et al. estimate the 80% time-horizon for Claude 3.7 Sonnet to be 0.25 as long, which is close to this theoretical estimate and within the margin of error"
- Ord 2026-02-04:"Contrary to my earlier hypothesis, AI agents probably don't have a constant hazard rate / half-life. Instead their hazard rates systematically decline as the task goes on."
- Ord 2026-02-04:"the AI agents mainly have a k of about 0.6, while the human value of k is significantly lower, at about 0.37"
- Sinha 等(摘要):"short-task benchmarks may give an illusion of slowing progress, as even marginal gains in single-step accuracy can compound into exponential improvements in the length of tasks a model can successfully complete"
- Sinha 等(摘要):"we observe a self-conditioning effect -- models become more likely to make mistakes when the context contains their errors from prior turns. Self-conditioning does not reduce by just scaling the model size. But, we find that thinking mitigates self-conditioning"
- Sinha 等:"the per-step accuracy of models degrades as the number of steps increases"

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| 把 Ord 2025 的恒定风险率、"翻倍即平方"当作现行结论 | Ord 2026-02-04 已亲口撤回("Contrary to my earlier hypothesis")。引用 2025 版时必须同时引 2026 版 |
| "Ord 发现 k≈0.6" | 拟合是 Gus Hamilton 做的,Ord 只是转述 |
| 不提 log-logistic 略优,就把 k≈0.6 当作定论 | 两种拟合在 99% 视野上相差约 20 倍,Ord 只是 slightly favour |
| "2024 年后发布的 21 个模型" | 应写"2024-01-01 起(含 2024 年)发布的 21 个";严格从 2025 年起只有 14 个(中位 5.15) |
| "TH1.1 复算的 k≈0.68 证实 / 反驳了 Hamilton 的 0.6" | 一个是两点映射,一个是直接拟合,不是同一个量,只能说方向一致 |
| 把 METR "4–6x"(TH1.0 v4)与 TH1.1 的中位 5.34 / 上沿 10.3 混成一个区间 | 数据版本不同 |
| 把 Sinha 等称为"预印本" | 已是 ICLR 2026 会议论文 |
| 只引 Sinha 的"指数级提升",当作对真实 agent 的实测 | 这是恒定 p 下的算术;任务是合成执行任务;论文自己发现每步准确率在衰减 |
| 把 self-conditioning 与递减风险率当成同一现象 | 机制不同 |

### (4) 证据分级

- 多源证实 / 单源已核:Ord 2025 与 2026 的引语(逐字);TH1.1 复算(三票独立复现 5.34 / 3.99–10.29 / 0.677);Sinha 的发表状态与引语。票 1 定级"单源已核",票 2、3 定级"多源证实",取严为**单源已核**。
- 方向存争:k 的具体数值与尾部含义(Weibull 与 log-logistic 之争未决)。
- 未验证:NeurIPS 2026 投稿 "On the estimation and validity of AI time horizons—a statistical look at the METR plot" 质疑 METR 的拟合假设。只做了摘要级检索,未读全文,只能当作"存在质疑"的线索,不能引作结论。2026-08 至 10 月未检索到 METR 官方对 p80/p50 的修订。

### (5) 主要一手 URL

- https://arxiv.org/pdf/2505.05115
- https://www.tobyord.com/writing/hazard-rates-for-ai-agents-decline
- https://metr.org/assets/benchmark_results_1_1.yaml
- https://arxiv.org/pdf/2509.09677 (v3)

---

## G04 · Stanford AI Index 2025:Arena 头部收敛 / 开闭源差 / 中美差

### (1) 锁定表述

- 以下均为 Stanford AI Index 2025 第 2 章 Highlights 的报告原口径,印刷页 86 / PDF 第 87 页。
- **Arena 头部挤压**:据 2024 版 AI Index(2023 年数据,由 2025 版转述),Chatbot Arena 第 1 名与第 10 名相差 11.9%,到 2025 年初缩小到 5.4%。前两名的差距从 2023 年的 4.9% 降到 2024 年的 0.7%。这几个百分比都是"点差 ÷ 较低模型的 Arena 绝对分"。BT/Elo 分数可以整体任意平移,所以这些百分比只能看方向,不能当作幅度,应改用点差:5.4% 约合 70–75 个 Arena 点,0.7% 约合 10 个点(点数换算见冲突记录)。11.9% 与 5.4% 来自不同报告年份的测量,不是同一方法下的连续序列。
- **闭权重 vs 开放权重**:2024 年 1 月,最强闭权重模型领先最强开放权重模型 8.04%;到 2025 年 2 月降至 1.70%。正文写作 8.0%/1.7%。2025 年 2 月对应 1,385 对 1,362,即 23 个点,23/1362=1.69%。口径是 open-weight,不是"开源",报告脚注 4 自己区分了两者。
- **中美(基准准确率,百分点)**:中美最强模型在 MMLU/MMMU/MATH/HumanEval 上的差距,从 2023 年底的 17.5/13.5/24.3/31.6 个百分点缩小到 2024 年底的 0.3/8.1/1.6/3.7 个百分点。
- **中美(Arena 口径)**:同一报告第 97 页另给出 Arena 口径的中美差,2024 年 1 月为 9.3%,2025 年 2 月为 1.7%。这一序列与上面的 pp 序列不是同一个量尺,不可混用。
- **跨版本漂移**:AI Index 2026 把 2025 年 2 月的中美 Arena 差重算为 0.4%(DeepSeek-R1 1,400 对 o1 1,405,相差 5 点),与 2025 版的 1.7% 对不上。原因是榜单经过风格控制和重新拟合,历史序列被改写。

### (2) 英文原文引语(逐字,印刷页 86;印刷页 14 的 Top Takeaways 版本没有 "just",用词是 "margins")

- "the Elo score difference between the top and 10th-ranked model on the Chatbot Arena Leaderboard was 11.9%. By early 2025, this gap had narrowed to just 5.4%. Likewise, the difference between the top two models shrank from 4.9% in 2023 to just 0.7% in 2024."
- "In early January 2024, the leading closed-weight model outperformed the top open-weight model by 8.04% on the Chatbot Arena Leaderboard. By February 2025, this gap had narrowed to 1.70%."
- "At the end of 2023, performance gaps on benchmarks such as MMLU, MMMU, MATH, and HumanEval were 17.5, 13.5, 24.3, and 31.6 percentage points, respectively. By the end of 2024, these differences had narrowed substantially to just 0.3, 8.1, 1.6, and 3.7 percentage points."
- (p.97)"the top U.S. model outperformed the best Chinese model by 9.3% in January 2024. By February 2025 ... 1.7%"

### 冲突记录

- **5.4% 换算成点数**:票 1 用 Fig 2.2.7 估算为 70/1304≈5.4%;票 2 自算 2024-12-30 风格控制榜 #1−#10 为 75.3 点(原始榜 79.8 点);票 3 取 2025-01-28 原始榜 #1−#10 为 72.7 点(约 73 点)。锁定写"约 70–75 个 Arena 点",不写单一精确值。
- **页码**:三票一致。Highlights 印刷页 86(PDF 87);Top Takeaways 印刷页 14;正文开闭源在 95(图在 96),中美在 97,前沿收敛在 100 和 107。

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "差距收敛了 55%"或把 11.9%→5.4% 当作幅度 | 分母是可任意平移的绝对分,百分比没有尺度意义。头部绝对分从约 1250 升到约 1385,即使点差不变,百分比也会机械性地缩小约 10% |
| 把 11.9% 当作 2025 版自测 | 原文明说 "According to last year's AI Index",是 2023 年的数据 |
| 写"开源 vs 闭源" | 报告口径是 open-weight vs closed-weight |
| 把中美 pp 序列与 Arena % 序列(或 2026 版的 2.7%)拼成一条时间序列 | 量尺不同 |
| 跨 2025、2026 两版报告拼接同一时点的数字(如 2025-02 中美差的 1.7% 与 0.4%) | 历史序列被重算,存在版本漂移 |
| 叫 "Elo" 而不注明 | Arena 已改用 BT;沿用报告原词时须注明是原口径 |

### (4) 证据分级

单源已核:三票逐字核对 AI Index 2025 PDF,分母以 Fig 2.1.34 复算。这些数字是报告自己的口径,不是独立测量。

### (5) 主要一手 URL

- https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf

---

## G05 · Stanford AI Index 2026(截至 2026-03):开闭源差重开 / 四家 25 分内 / 中美 39 分 / 评测数月饱和

### (1) 锁定表述

- **数据口径**:AI Index 2026 技术章(印刷页 71–95)使用 2026 年 3 月导出的 Arena 历史榜(Public,Style Control On)。所列分数是 BT 分,报告沿用了 "Elo" 一词。下面每个数字都只是 **2026 年 3 月的快照**。
- **开闭源差**:最强闭权重模型 Claude Opus 4.6(1,503)领先最强开放权重模型 GLM-5(1,454)**49 个 Arena 点**;2024 年 8 月同口径只差 7 点。报告 Highlights 写 3.3%(以领先方 1,503 为分母),正文写 3.4%(以落后方 1,454 为分母),同一个分差用了不同分母,属于内部不一致。文章统一写 49 点,不要并列两个百分比。
- **四家头部**:Anthropic 1,503、xAI 1,495、Google 1,494、OpenAI 1,481,四家相差在 25 点以内(复算 22 点;按 2026-03-11 快照为 22.6 点)。口径是按实验室各取最高模型。报告混用了不同日期的快照:Google 在 02-26 快照为 1,500,在 03-31 快照为 1,494。p.78 还说"去年报告前四名跨度约 97 点",但两版用的是不同的榜单口径(LMSYS 榜对风格控制榜),97→25 不是同口径比较。
- **中美**:美国最强模型 Claude Opus 4.6(1,503)领先中国最强模型 Dola-Seed-2.0 Preview(1,464)**39 个点**。报告写 2.7%,以落后方为分母。这个数字只能接 2025 版的 Arena 口径序列(9.3%→1.7%),不能接基准 pp 序列。但 2026 版把 2025 年 2 月重算为 0.4%(5 点),与 2025 版的 1.7% 矛盾,所以跨版本连线也不成立。2025-05-16 起风格控制成为默认,并平移了 offset。
- **评测饱和**:AI Index 写道,本打算难住多年的评测几个月就饱和了(这是定性措辞)。HLE 一年内(2024→2025)从不到 10% 升到 38.3%,这是 AI Index 图表采用的值(来源 lastexam.ai),未注明工具档位或 harness,不可写成"当前最高分"。MMLU 上只差 1% 的 GPT-4o 与 GPT-4-Turbo,在 MMLU-Pro 上拉开到 9%。这是 AI Index 转述的 2024 年 MMLU-Pro 论文旧例,不是 2026 年的新测量。
- **时点限定(票 2,HF lmarena-ai/leaderboard-dataset 2026-08 至 10 月数据)**:到 2026-10-08,风格控制榜按实验室去重后,前四家为 Google 1525.4、Anthropic 1507.1、Meta 1494.2、Moonshot 1488.1,跨度 37.3 点,Google 单独领先约 18 点,成员也变了(xAI 跌出前 8,OpenAI 排第 5)。模型层级的前十全部是 Proprietary。开放权重头名 kimi-k3-max 与闭源头名相差 37.3 点;2026-08-27 时是 18.7 点,几周内来回摆动。所以 3 月的"25 分内"不能写成持续趋势。
- **背景限定(吸收 round3 R3 与 R1)**:前沿区间的 Arena 分差小,不等于"能力趋同"或"榜单失去区分力"。2026-10 风格控制榜上,Arena 自排前 15 名的分差为 37 点,105 对模型中有 39 对的 95% 置信区间不重叠;按 ECI 选出的前 15 名,分差为 51 点,置信区间平均宽度约 11.5。但在 ECI 前 15 名内,Arena 与 ECI 的相关接近 0(n=15,区间很宽),说明在前沿,偏好榜和能力指数测的已不是同一样东西。round3 R1 记录了二手说法"Arena 开闭源差从 0 扩大到 29 Elo",未核实,不可引用。

### (2) 英文原文引语(逐字)

- (印刷页 71,Highlights)"The open model performance gap reopened in 2025 after briefly closing in 2024. As of March 2026, the top closed model leads the top open model by 3.3%, up from 0.5% in August 2024. Six of the top ten models on the Arena Leaderboard are now closed." 最后一句已判死,见下文,不可当作事实引用。
- (p.76)"Claude Opus 4.6 (1,503), led the top open-weight model GLM‑5 (1,454) by 49 points (3.4%)"
- (p.71)"Top model performance is converging, with 4 companies now clustered within 25 Elo points";(p.78)"the top four models are separated by fewer than 25 points"
- (p.77)"the top U.S. model (Claude Opus 4.6, 1,503) led the top Chinese model (Dola‑Seed‑2.0 Preview, 1,464) by 39 points (2.7%)"
- (p.71)"Evaluations intended to be challenging for years are saturated in months"
- (p.81)"GPT-4o and GPT-4-Turbo appeared to have a 1% gap on standard MMLU, but on MMLU-Pro the spread widens to 9%"
- (p.95)"In a single year, accuracy went from under 10% to 38.3%"

### 冲突记录

- **"前十中六个闭源"**:票 1 认为模型层级复算为 10/10 闭源,按实验室去重(02-26 快照)才是 6/10;票 2 认为是 3 月的状态,需加时点,而 10 月已是 10/10;票 3 认为模型层级为 10/10,实验室去重(2026-03)为 7/10,两种口径都对不上 6/10。取最严:**判死**。
- **四家跨度**:票 1 复算 22 点(混用快照),票 3 复算 22.6 点(2026-03-11 快照)。两者都支持"25 点以内"。
- **页码**:三票一致。Highlights 印刷页 71;开闭源 76;中美 77;收敛 78;MMLU-Pro 81;HLE 95。

### (3) 判死 / 禁用清单

| 原稿说法 | 为何不能用 |
|---|---|
| "Arena 前十中有六个是闭源模型" | 与 Arena 原始数据不符:模型层级 3 月快照为 10/10 闭源;实验室去重后,不同快照为 6/10 或 7/10,口径不定。10 月模型层级仍为 10/10。不引用;若一定要引,须注明"AI Index 原文如此,与 Arena 数据不符" |
| 并列写 3.3% 和 3.4%,或任选其一当作幅度 | 同一个 49 点差用了两种分母;百分比的分母可任意平移 |
| 0.5%(2024-08)→3.3%(2026-03)与 2025 版 8.04%→1.70% 拼成一条曲线 | 2026 版用风格控制历史榜重算过,与 2025 版不是同一序列 |
| "四家头部持续收敛在 25 分内" | 这是 2026-03 的快照;到 10-08 跨度为 37.3 点,Google 领先约 18 点 |
| "去年 97 点 → 今年 25 点" | 跨版本、跨榜单口径 |
| 中美 2.7% 接 2025 版的 pp 序列(0.3/8.1/1.6/3.7) | 量尺不同;而且 2025-02 被重算为 0.4%,与 1.7% 矛盾 |
| "MMLU-Pro 拉开 9%"作为 2026 年新发现 | 2024 年 MMLU-Pro 论文的旧例 |
| "HLE 当前最高 38.3%" | 只是 AI Index 截止时采用的值,harness 未注明,2026 年内更新的分数未核 |
| "Arena 头部分差小 → 用户分不出 / 能力已趋同" | round3 R3:头部 39/105 对置信区间可分,Arena 与能力指数在前沿脱钩;"感知饱和"只是几种解释之一 |
| "Arena 开闭源差 0→29 Elo" | 二手说法,未核实 |

### (4) 证据分级

- 单源已核:三票逐字核对 AI Index 2026 PDF,并对照 HF lmarena-ai/leaderboard-dataset 的 text_style_control 快照,49、22/22.6、39 点均吻合。这些数字是报告口径。
- 已判死:"Six of the top ten"。
- 方向存争:开闭源差、头部跨度的趋势,几周内来回摆动,结论依赖快照。
- 弱结论(round3):用 Arena 头部压缩推断能力趋同。

### (5) 主要一手 URL

- https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_2_technical.pdf
- https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset (text_style_control/full parquet,2026-02-26、03-11、03-16、03-31、08-27、10-08 快照)
