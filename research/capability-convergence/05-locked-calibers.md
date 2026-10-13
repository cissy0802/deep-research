# 05 · 锁定口径(成文唯一依据)

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

# 锁定口径 · Part 4(G14–G18)

> 文章:「AI 能力最终会趋同是真的吗」(截至 2026-10)。每组三票均为 CORRECTED;冲突处取最严格修正。G18 已吸收 04-verification-round3.md 中 R2-metr-open-lag 双席审计(counter:方向存争;method:降级为弱结论)的限定。

---

## G14 · 基准饱和速度、OpenAI 停报 SWE-bench Verified、厂商主打基准迁移、AA 指数换题

### (1) 锁定表述

- **饱和速度**:口径为 Epoch 数据扣随机基线后归一化,n=(s−baseline)/(1−baseline),以首个归一化分 ≥80% 的模型发布日计。
  - GPQA Diamond(2023-11 发布)约 19 个月,2025-06 由 Gemini 2.5 Pro 达到,原始 85.29%,归一化 0.804,只多一题过线。
  - SWE-bench Verified(2024-08)约 20 个月,2026-04 由 Claude Opus 4.7(max)达到,83.5%。这是 Epoch 独立复测口径;厂商自报更早,约 2025-11 Claude Opus 4.5 自报约 80.9%,即约 15 个月。
  - ARC-AGI-2(2025-03)约 11 个月,2026-02-12 由 Gemini 3 Deep Think 达到,84.6%。若不计 Deep Think,则是 2026-03 的 GPT-5.4 Pro(83.3%)。
  - Terminal-Bench 2.0(2025-11 发布)约 3 个月后,2026-02-19 由 Gemini 3.1 Pro + 第三方 agent TongAgents 首破 80%(80.2%)。这是"模型 + 第三方 harness"组合的成绩。
  - HLE(2025-01)到 2026-09:GPT-6 Astra 原始分 54.8%,扣 4.8% 随机基线后归一化 52.5%,首次过半。
- **OpenAI 停报 SWE-bench Verified(2026-02-23)**:
  - OpenAI 审计了 o3 在 64 次独立运行中未能稳定解出的 138 道题,其中 59.4% 在测试设计或题面上有实质问题。
  - 所有受测前沿模型在部分题目上能复现 gold patch(人写的参考修复)或题面原文细节。对应小节涉及 GPT-5.2、Claude Opus 4.5、Gemini 3 Flash。
  - OpenAI 因此停报该基准,建议其他开发者也停报,并建议改报 SWE-bench Pro。
  - 后续(仅票 1,二手报道 + 页面摘要,未逐字核):2026-07 OpenAI 审计 SWE-bench Pro,估计约 30% 任务有问题。"撤回推荐"一说未核实。
- **厂商主打基准迁移**:
  - Claude Opus 5.5 发布页(2026-09-22)的基准表列出 Terminal-Bench 4.0 66.4%、FrontierCode v1.1 (Main) 54.4%、CursorBench 4.0 57.8%、GDPval-AA v2.1 1846、AutomationBench 40.0%、HLE 67.7%(with tools),均为厂商自报。FrontierCode 由 AA 独立测得 52.2%。
  - 全文不出现 MMLU、GPQA、SWE-bench、AIME、GSM8K。
  - 对比:Claude 3 发布页(2024-03)主打 MMLU、GPQA、GSM8K。
- **AA 智能指数换题**:
  - v4.0(2026-01)移除 MMLU-Pro、LiveCodeBench、AIME 2025。
  - v4.2(2026-09)移除 GPQA Diamond。v4.2 公告(2026-09-04)称 GPQA Diamond "has now been saturated"。版本史本身对两次移除都未写理由;GPQA 仍作为独立评测继续跑。
  - 另有 v4.1 移除 IFBench,v4.3 用 Terminal-Bench 4.0 替换 TB 2.1。现行版本为 v4.3.2(2026-09)。

### (2) 英文原文引语(逐字)

- OpenAI:"We conducted an audit of 138 SWE-bench Verified problems that OpenAI o3 did not consistently solve over 64 independent runs"
- OpenAI:"We found that 59.4% of the 138 problems contained material issues in test design and/or problem description"
- OpenAI:"all frontier models we tested were able to reproduce the original, human-written bug fix used as the ground-truth reference, known as the gold patch, or verbatim problem statement specifics for certain tasks"
- OpenAI:"This is why we have stopped reporting SWE-bench Verified scores, and we recommend that other model developers do so too"
- OpenAI:"Until we have those, OpenAI recommends reporting results for SWE-bench Pro."
- Claude 3 页面:"undergraduate level expert knowledge (MMLU), graduate level expert reasoning (GPQA), basic mathematics (GSM8K)"
- AA 版本史:"Removed MMLU-Pro, LiveCodeBench, AIME 2025 from Intelligence Index"(v4.0);"Removed GPQA Diamond from the Intelligence Index"(v4.2)
- AA v4.2 公告:"GPQA Diamond, an exceptional scientific reasoning evaluation that has now been saturated"(仅票 1 引用)
- AA:"We still run it on new model releases and report it as a standalone evaluation"(GPQA)

### (3) 判死 / 禁用清单

1. 原稿"Terminal-Bench(2025-05)→2026-02,约 9 个月":判死。2025-05-19 是 TB 1.0 的发布日,而分数全部来自 TB 2.0 榜(2025-11 发布)。正确说法是约 3 个月,且为 agent 组合成绩。
2. 原稿"ARC-AGI-2 于 2026-03 达标,约 12 个月":判死。首个达标是 2026-02 的 Gemini 3 Deep Think,约 11 个月。
3. 原稿"GPT-5.2 64 次运行稳定失败的 138 题":判死。跑 64 次的是 o3,原文是"未能稳定解出",不是"稳定失败"。GPT-5.2 出现在另一处:它解出了 31 道被认定几乎不可能解出的题。
4. 原稿"主流模型能凭记忆复现修复"(不加限定):禁用。必须带原文限定 "for certain tasks",并写明是 gold patch 或题面原文。
5. 原稿"HLE 约 52.5%"(不注口径):禁用。必须注明是归一化值,原始分为 54.8%。
6. 原稿"AA 因饱和移除 MMLU-Pro 等(v4.0)":禁用。v4.0 版本史未写理由;只有 v4.2 移除 GPQA 时在公告里写了 saturated。
7. "SWE-bench Verified 20 个月"不注口径:禁用。须注明是 Epoch 独立复测;厂商自报约 15 个月。

### (4) 证据分级

- 单源已核:Epoch 复算的饱和月数;Opus 5.5 页面内容;AA 版本史。
- 多源证实:OpenAI 停报的原文、数字与日期,三票逐字一致。
- 厂商口径:Opus 5.5 各项分数;SWE-bench Verified 的厂商自报过线时间。
- 未验证:OpenAI 对 SWE-bench Pro 约 30% 的后续审计,以及"撤回推荐"一说。

### (5) 一手 URL

- Epoch benchmark_data.zip:benchmark_metadata.csv、gpqa_diamond.csv、arc_agi_2_external.csv、terminalbench_external.csv、swe_bench_verified.csv、hle_external.csv
- https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (直连 403;用存档 https://web.archive.org/web/2026id_/https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- https://www.anthropic.com/news/claude-opus-5-5
- https://www.anthropic.com/news/claude-3-family
- https://artificialanalysis.ai/methodology/intelligence-benchmarking
- https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2

---

## G15 · ARC-AGI 1/2/3 官方榜:闭源、人类与开源的位置,以及 harness 口径

### (1) 锁定表述

数据来自 ARC Prize 官方榜 JSON,generatedAt 2026-10-05。

- **ARC-AGI-1(v1.json)**:
  - 8 个闭源配置并列 98.5%:Claude Fable 5 Max/XHigh、GPT-6 Astra XHigh/High、Claude Opus 5.5 High、Gemini 3.8 Flash High、GPT-6.1 Sol XHigh/High。
  - 略高于 Human Panel 的 98%(Stem Grad 也是 98%)。
  - 开放权重最佳为 Kimi K3 (Max) 和 DeepSeek V4.1 Flash (Max),均为 94.5%。Kimi K3 为非商用许可。同分的还有闭源脚手架 GPT-5.2 (Refine.)。
- **ARC-AGI-2(v2.json)**:
  - GPT-6 Astra (Max) 95.0%。
  - Claude Opus 5.5 (High) 93.3%,其 Max 档只有 91.7%。
  - Human Panel 100%。这是 ARC Prize 的人类小组口径(每题至少被组内有人解出),不是个人平均正确率。
  - 官方开源权重可确认的最佳是 DeepSeek V4.1 Flash (Max) 72.9%。另有 Dots3-Note Preview (Max) 76.8%(2026-08-14),第三方站点列为开源权重,但未找到官方权重页。
- **ARC-AGI-3(v3.json,2026-03-25 发布)**:
  - 在 ARC Prize Standard harness 下(厂商中立的脚手架,会把模型自选的笔记带入后续步骤):GPT-6 Astra (Max) 62.7%,GPT-6.1 Sol (Max) 52.7%,Claude Opus 5 (High) 30.2%,Gemini 3.8 Flash (High) 10.4%,Grok 4.7 (XHigh) 1.8%(Grok 系最佳为 Grok 4.6 (XHigh) 2.1%)。GPT-5.4 (High) 0.21%、Gemini 3.1 Pro 0.42%、GPT-5.5 (High) 0.43%,均低于 0.5%。
  - Claude Opus 5.5 未在 ARC-AGI-3 上参测。
  - 提供方只有 OpenAI、Google、xAI、Anthropic,没有任何开源条目,也没有 Human 条目。
- **Provider Adapter(OpenAI 自家 harness)**:保留推理状态、压缩长对话。GPT-6 Astra 用它的得分是 High 档 99.95%、Max 档 98.6%、None 档 96.7%。
  - 这与 Standard harness 不是同一评测条件,不能并列比较。
  - 官方榜把两者并排列在同一 datasetId 下,只靠名称后缀 "- Provider Adapter" 区分。
  - 混放会改变排名:例如 Gemini 3.8 Flash 用 Adapter 得 35.0%,高于 Claude Opus 5 的 Standard 30.2%。

### (2) 英文原文引语

- ARC Prize 对 harness 的说明经检索摘要转述,未逐字打开,只可作意译、不可加引号:Standard harness "carries forward model-selected notes";Provider Adapter "preserves reasoning state and compacts longer conversations"。
- The Next Web 标题(二手):"OpenAI's AGI number came from a harness, not the model"

### (3) 判死 / 禁用清单

1. 原稿"ARC-AGI-1 数据出自 v2.json":判死。ARC-AGI-1 在 v1.json;v2.json 只含 ARC-AGI-2。
2. 原稿"纯模型"成绩:禁用。应写"ARC Prize Standard harness(厂商中立脚手架)",它本身也是脚手架。
3. 原稿"Provider Adapter 99.95%"不标档位,或与 62.7% 等成绩混排:判死。99.95% 是 High 档(Max 为 98.6%),属厂商专属 harness,必须分开陈述。
4. 原稿"Claude Opus 5.5 93.3%"不标档位,暗示是最高档:禁用。须标 High 档(Max 为 91.7%)。
5. 原稿 ARC-AGI-3 "Claude Opus 5 30.2%" 若标作 Max 档:判死,应为 High 档。也不得写成 Opus 5.5 的成绩。
6. 原稿"最佳开源 DeepSeek V4.1 Flash 72.9%"不加限定:禁用。应写"有官方开源权重确认的最佳",因为第三方列为开源的 Dots3-Note Preview 为 76.8%。
7. "人类 100%"不注口径:禁用。须注明是 Human Panel 口径。

### (4) 证据分级

- 单源已核:ARC Prize 官方 JSON,三票均用 Python 全量解析,数字一致。
- 未验证:harness 机制的官方逐字说明,只有检索摘要和二手报道;Dots3-Note 的开源属性。

### (5) 一手 URL

- https://arcprize.org/media/data/leaderboard/v1.json
- https://arcprize.org/media/data/leaderboard/v2.json
- https://arcprize.org/media/data/leaderboard/v3.json
- https://arcprize.org/blog/arc-agi-3-launch

---

## G16 · METR time horizon 的饱和、不确定性与测不准

### (1) 锁定表述

- **停更与可靠性上限**:METR 的 time-horizons 页面自 2026-09-08 起停止主动更新。2026-05-08 页面加入 Claude Mythos Preview (early) 时同时声明,超过 16 小时的测量在现有任务集上不可靠。
- **TH1.1 数据(METR 现行 yaml)**:
  - Mythos Preview(发布 2026-04-07,有限预览):p50 为 1044.8 分钟(约 17.4h,95% CI 509–3304 分钟),p80 为 185.9 分钟。
  - Opus 4.6:p50 为 718.8 分钟(CI 317–3634)。Epoch 镜像的旧版本给出 CI 上限 3950,数值随版本漂移。
  - 2023 年起的倍增期为 128.7 天 [104, 158]。该拟合剔除了 p50 > 16h 的点,Mythos 不在其中。
- **2026-05-19 Frontier Risk Report**:
  - METR 评估过的最强 agent(含实验室分享给 METR 的内部模型)"基本饱和"了 TH1.1。
  - 最强"shared model"(即实验室提供的内部模型)p50 点估计为 16–20h,p80 为 3–4h。同表的公开前沿是 p50 约 12h [5h–61h]、p80 约 1.5h [50m–2h40m]。
  - shared models 在 8h 以上任务的成功 run 中,至少 16% 涉及作弊。
  - 内部部署前沿约领先公开前沿趋势线 66 天。METR 声明该数字刻意加了噪声,基于少量模型,并用 105 天的公开趋势倍增期换算(不是 yaml 的 128.7 天)。两个倍增期不可混用。
  - Opus 4.6 在低 messiness 任务上为 17.8h,高 messiness 任务上只有 6.4h。
- **建模假设的影响**(METR 研究员个人 Note,2026-03-20,不代表 METR 官方立场):
  - 2026-03-03 上线的正则化修正使近期模型 p50 最多下降 20%。
  - 合理的替代拟合可使 p50 最多下降 35%、p80 最多上升 100%。
  - 只用非公开任务时,Opus 4.6 的 p50 下降 40%,从 11h59m 降到 7h11m。
  - 修正基线噪声可使 p50 约降 30%(0–60%)。
- **TH1.1 任务集**:任务数从 170 增到 228,8h 以上长任务从 14 增到 31;但 31 个长任务中只有 5 个有人类基线。
- **GPT-5.6 Sol(METR,2026-06-26)**:按标准方法(作弊算失败)p50 约 11.3h(95% CI 5–40h);作弊算成功则超过 270h;丢弃作弊 run 为 71h(CI 13–11400h)。METR 认为三个数都不构成稳健测量。
- **Claude Opus 5.5(METR,2026-09-22)**:正文不给 time horizon,只称其在定量评估上是 Fable 5.1 之上的增量改进。所测任务为 NanoGPT、LMCA、Train a Program、Gaming Bot、Sunlight。文本取自 system card,Anthropic 有机会审阅和修改。

### (2) 英文原文引语(逐字)

- "This page is no longer actively updated. LAST UPDATED September 8, 2026"
- "Measurements above 16 hrs are unreliable with our current task suite."
- "The most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark"
- "the 50% time horizon point estimate of the most capable shared model was between 16 and 20 hours, and the 80% time horizon point estimate was between 3 and 4 hours"
- "at least 16% of successful runs on Time Horizon 1.1 tasks of 8 hours or longer involved cheating"
- "the gap between the internally deployed frontier and the public frontier trend is approximately 66 days"
- "decreased recent models' 50% time horizon results by up to 20%"
- "reasonable alternative fits decrease the 50% time horizons by up to 35%, and increase the 80% time horizon by up to 100%"
- "We increased our suite from 170 to 228 tasks"
- "around 11.3hrs (95% CI: 5hrs - 40hrs), but if we count the cheating attempts as legitimate successes, the point estimate jumps beyond 270hrs"
- "71hrs (95% CI: 13hrs - 11400hrs)"
- "Claude Opus 5.5 is an incremental improvement above Fable 5.1 on our quantitative evaluations"
- "Anthropic had the opportunity to review and edit the text"

### (3) 判死 / 禁用清单

1. 把 "essentially saturated" 写成"公开模型饱和了 TH1.1":判死。主语是 METR 评估过的最强 agent,含内部模型;公开前沿只有约 12h。
2. 把 16–20h / 3–4h 写成公开前沿的水平:判死。这是实验室分享给 METR 的内部模型。
3. "内部前沿领先约 66 天"不带限定:禁用。须注明刻意加噪、样本少、对比对象是公开趋势线、用 105 天倍增期换算。
4. 把 128.7 天与 105 天混用,或称 128.7 天的拟合包含 Mythos:判死。
5. 把 03-20 Note 写成 METR 官方结论:禁用。须标为研究员个人 Note。
6. 单独引用 GPT-5.6 Sol 的 11.3h 或 270h,不带 METR 的"均不稳健"声明:禁用。
7. 引用 METR 对 Opus 5.5 的评价而不注明 Anthropic 可审阅修改:禁用。
8. "16% 作弊"不限定:禁用。须写"至少 16%,shared models,8h 以上任务的成功 run"。

### (4) 证据分级

- 单源已核:三票均对 METR 一手页面和 yaml 逐字、逐数核对一致。
- 厂商口径:Opus 5.5 评估文本(Anthropic 可审改)。
- 方法敏感:Note 中 −35% / +100% 的区间,属个人研究笔记。

### (5) 一手 URL

- https://metr.org/time-horizons/
- https://metr.org/assets/benchmark_results_1_1.yaml
- https://metr.org/blog/2026-05-19-frontier-risk-report/
- https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/
- https://metr.org/blog/2026-1-29-time-horizon-1-1/
- https://metr.org/blog/2026-06-26-gpt-5-6-sol/
- https://metr.org/blog/2026-09-22-claude-opus-5-5/

---

## G17 · 闭源前沿之间的 time horizon 差距、阈值翻转、p50/p80 比与 MirrorCode

### (1) 锁定表述

- **TH1.1 闭源配对(METR 现行 yaml 复算)**:
  - GPT-5 203.0 对 Opus 4.1 100.5 分钟,约 2.0x。
  - GPT-5.2 352.2 对 Opus 4.5 293.0,约 1.2x。
  - Opus 4.6 718.8 对 Gemini 3.1 Pro 384.1,约 1.9x(1.87x)。
  - Mythos Preview 1044.8 对 Gemini 3.1 Pro,约 2.7x。Mythos 是有限预览,p50 超出 16h 可靠上限,与公开发布的 Gemini 不对等。
  - 每一对的 95% CI 都有重叠,但程度不同:Opus 4.6 [317, 3634] 与 Gemini [234, 695] 大幅重叠;GPT-5 [113, 406] 与 Opus 4.1 [59, 160] 只在 113–160 重叠;Mythos [509, 3304] 与 Gemini 只在 509–695 重叠。1.2–2.7x 的差距在统计上难以分开。
  - 配对方式会改变倍数:Opus 4.6 对同日发布的 GPT-5.3-Codex(349.5)是 2.06x;Gemini 3 Pro 224.3、GPT-5.1-Codex-Max 223.7、Opus 4.5 293.0 几乎持平。
  - Opus 4.6 的领先不稳健:只用非公开任务时其 p50 为 7h11m,对 Gemini 3.1 Pro 约 1.1x(来自 METR 03-20 Note)。
- **阈值翻转**:Opus 4.6 对 Gemini 3.1 Pro 平均分只高 1.83 个百分点(0.7886 对 0.7703),p50 高 1.87x,p80 却只有 0.78x(69.9 对 89.8 分钟),排序随阈值翻转。不过两者 p80 的 CI([27, 170] 与 [52, 159])几乎完全重叠,翻转不显著。它部分是 logistic 斜率的拟合产物:METR Note 指出 logistic 会拟合出平缓斜率,压低 p80、抬高 p50。
- **p50/p80 比**:GPT-4 4.48、GPT-4o 5.52、o1 5.48、o3 3.99、GPT-5 5.30、GPT-5.2 5.34、Opus 4.5 5.93、Gemini 3.1 Pro 4.28、GPT-5.4 6.34、Mythos 5.62;2024 年 Claude 3.5 Sonnet 为 6.82(6 月)和 7.91(10 月);Opus 4.6 为 10.29,是离群点。
  - 2023–2026 年这个比值大体持平,多数在 4–6,个别到 8。即 p80 没有追上 p50,但差距也没有扩大。
  - 该比值完全由 logistic 拟合斜率决定,部分是建模产物。
- **MirrorCode(两个版本、两种指标,不得合成一条序列)**:
  - METR Frontier Risk Report 用的是 MirrorCode-Early,time horizon 口径:Opus 4.6、Gemini 3.1 Pro、GPT-5.4 均 >32h,Opus 4.6 >100h。METR 声明该早期版本不反映基准现状。
  - Epoch 现行版(id mirrorcode-ml-2l,指标是 mean_score 即任务完成比例,不是 time horizon;运行于 2026-08-10 至 09-22,所测模型发布于 2026-02 至 09):Opus 5.5 (max) 0.774(stderr 0.083)、Fable 5.1 (high) 0.733(0.092)、Fable 5 0.639、GPT-6 Astra 0.467(0.119)、Opus 4.7 0.311、GPT-5.6 Sol 0.200、GPT-5.4 0.156、GPT-5.5 0.100、Gemini 3.1 Pro 0.089。
  - Opus 5.5 与 Fable 5.1 相差 0.041,在一个 stderr 以内,视为持平。Opus 5.5 跑的是 max 档,其他是 high 档。
  - Gemini 3.1 Pro 是 2026-02 的模型,不能代表当前 Google 前沿。
  - 9 行全是美国闭源模型。Epoch 没有测开源模型,不代表开源得 0 分。

### (2) 英文原文引语(逐字)

- "On MirrorCode-Early, Opus 4.6, Gemini 3.1 Pro, and GPT-5.4 all had time horizons greater than 32 hours, and Opus 4.6 had a time horizon greater than 100 hours"
- "all information in this report is about an early version of MirrorCode, and does not reflect the current state of the benchmark"
- "fits shallow slopes that depress 80% time horizons and increase 50% time horizons"(METR 03-20 Note)

### (3) 判死 / 禁用清单

1. "可靠性越来越落后于能力"或"p50/p80 差距在扩大":判死。比值 2023–2026 大体持平(GPT-4 4.48 对 Gemini 3.1 Pro 4.28),只能说"没有缩小"。
2. "排序随阈值翻转"写成显著事实:禁用。p80 CI 几乎完全重叠,且部分是拟合产物。
3. "所有配对 CI 大幅重叠":禁用。GPT-5/Opus 4.1 与 Mythos/Gemini 只是部分重叠。
4. "Opus 4.6 领先 Gemini 3.1 Pro 1.9x"不加限定:禁用。只用非公开任务时约 1.1x,配对不同倍数也会变。
5. 把 MirrorCode-Early 的 time horizon 与 Epoch 的 mean_score 放进同一句当作同一基准:判死。例如 Gemini 3.1 Pro 在前者 >32h,在后者 0.089。
6. "Opus 5.5 领先 Fable 5.1":判死。差距在一个 stderr 内;两者推理档位也不同(max 对 high)。
7. "开源模型在 MirrorCode 上 0 分 / 落后":判死。实际是未测。
8. 把 Mythos 当作公开发布模型来比较:禁用。
9. "2026-08/09 的横截面":禁用。应写"运行于 2026-08-10 至 09-22,模型发布于 2026-02 至 09"。

### (4) 证据分级

- 单源已核:METR yaml 复算的倍数和比值,三票一致;Epoch mirrorcode.csv 的数字。
- 方向存争:"可靠性未追上能力"的解读,受拟合方法影响。
- 冲突说明:p50/p80 比的常态区间,票 1、票 2 写 4–6(并注明 Claude 3.5 Sonnet 6.8–7.9),票 3 写 4–8。锁定为"多数 4–6,个别至 8,Opus 4.6 10.3 离群"。

### (5) 一手 URL

- https://metr.org/assets/benchmark_results_1_1.yaml
- https://metr.org/blog/2026-05-19-frontier-risk-report/ (Appendix E MirrorCode)
- https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/
- https://epoch.ai/data/benchmark_data.zip (mirrorcode.csv, benchmark_metadata.csv)

---

## G18 · METR 量尺上的开源滞后(TH1.0,截至 2025-11)

### (1) 锁定表述

- **数据边界**:METR 关于开源模型的 time horizon 证据全部在 TH1.0 上,最后一个是 Kimi K2 Thinking(2025-11-06 发布,2025-11-19 加入 METR 页面)。METR 从未在 TH1.1 上公开测过任何开源模型(yaml 中只有 Anthropic、OpenAI、Google 的模型),Frontier Risk Report 也没有评估开源权重模型。因此 METR 量尺无法回答 2026 年开源与闭源的差距。
- **滞后月数**:复算 METR TH1.0 数据(加权 logistic,闭源 running-max 包络,对数线性插值)。必须同时写明方法。
  - 插值法:DeepSeek-V3 6.2、R1 3.4、V3-0324 6.1、R1-0528 6.8、gpt-oss-120b 7.2、Kimi K2 Thinking 8.1–8.2 个月。
  - 阶梯法(首个 p50 不低于该开源模型的闭源模型):约 3.0–6.7 个月,Kimi 6.7。
  - 指数趋势线法:R1 3.1、Kimi 8.0。
  - 也就是说,月数随方法相差 1.5–3 个月。
- **发布时倍数**(对比发布日不晚于该开源模型的最佳闭源模型,同在 TH1.0):
  - R1 约 1.5x(对 o1)。
  - R1-0528 约 2.8x(对 o3)。
  - gpt-oss-120b 约 2.4x(对同日的 Opus 4.1;对两天后的 GPT-5 为 2.9x)。
  - Kimi K2 Thinking 约 2.3–2.5x(对 GPT-5)。
- **趋势判断**(吸收 round3 审计,降为弱结论 / 方向存争):
  - R1 是局部低点,夹在 V3 的 6.2 与 V3-0324 的 6.1 之间,以它为起点会夸大"拉长"的幅度。
  - 2024 年 Qwen2-72B 约 10–18 个月、Qwen2.5-72B 约 10–14 个月,所以全序列呈 V 形:先收窄,后回弹。
  - Kimi 减 R1 在任务 bootstrap 下可区分;Kimi 减 R1-0528 不可区分。R1 之后各点的 90% CI(约 5–10 个月)互相重叠。
  - 可写:"R1 带来的收窄在 2025 年没有延续,差距停在约 6–9 个月,有小幅回弹"。不可写"持续拉长"。
- **单源局限**:
  - 结论只来自 METR 一家,开源样本由它自选。2025 年下半年只有 gpt-oss-120b 和 Kimi 两个点;同期可能更强的 DeepSeek V3.1/V3.2、Qwen3、GLM-4.x 未测。
  - 每个开源模型的 elicitation 只有约一个工作日,用 Triframe,经 OpenRouter;Kimi 经第三方推理商 Novita AI,METR 自称这降低了对该估计的信心。
  - 这些偏差可能系统性低估开源。
- **METR 当时的官方表述**(与自算是不同测法,不得串成一条序列):
  - 2025-02-12 称开源权重模型整体与 6 个月前的 SOTA 相当。
  - 2025-03-05 称 R1 与 7 个月前的 SOTA 相当,而自算只有 3.4 个月。
  - 2025-06-27 称 2025 年中的 DeepSeek 模型相当于 2024 年底的前沿。
- **其他量尺方向不一**(只作旁证):
  - NIST CAISI(2026-05)判 DeepSeek V4 Pro 落后约 8 个月,与 GPT-5 相当。量尺不同(多基准 IRT,含私有题),是单点。
  - Epoch ECI:2026 上半年滞后约 4 个月,自称略大于此前约 3 个月。
  - UK AISI 网络安全评估:2026 年从 6–10 个月收窄到 4–7 个月。
  - AISI 趋势报告给出的 4–8 个月中,8 个月引自 METR,不独立。

### (2) 英文原文引语(逐字)

- METR DeepSeek-V3 报告(2025-02-12):"the performance of open-weight models on our tasks is on par with state-of-the-art models from 6 months ago, whereas they had previously lagged significantly further behind"
- METR DeepSeek-R1 报告(2025-03-05):"on-par with state–of-the-art models from 7 months ago"
- METR DeepSeek/Qwen 报告(2025-06-27):"the level of autonomous capabilities of mid-2025 DeepSeek models is similar to the level of capabilities of frontier models from late 2024"
- METR 页面更新日志:"November 19th, 2025: Added GPT-5.1-Codex-Max and Kimi K2 Thinking"
- METR 关于 Kimi(X 帖):"through a third-party inference provider, which reduces our confidence in this estimate"
- CAISI(2026-05):"DeepSeek V4's capabilities lag behind the frontier by about 8 months";"performs similarly to GPT-5, which was released about 8 months ago"

### (3) 判死 / 禁用清单

1. "Kimi K2 Thinking 54 对 GPT-5 high 203 → 0.27(约 3.7x)"以及由此得出的 8.4 个月:判死。这是用 TH1.0 的 Kimi 除以 TH1.1 的 GPT-5,跨版本无效。同版本内应为约 2.3–2.5x。
2. "GPT-5 在 TH1.0 上约 131 分钟"写成 METR 官方值:禁用。三票冲突:票 1、票 2 认为 130.8 是自拟合值,METR/Epoch 公布值为 137.3(medium,2h17m);票 3 称 130.8 是修正后官方 yaml 值,修正前为 138。锁定写法:"约 131–137 分钟(依版本/来源)",并注明出处。
3. 滞后月数写成与方法无关的精确值:禁用。必须注明插值法,或给出 3–8 个月的范围。
4. "开源滞后在持续拉长":判死(round3 双席)。起点依赖 R1 这个低点,年中之后的变化在噪声范围内,全序列呈 V 形。
5. 用 METR 数据描述 2026 年开源与闭源的差距:判死。TH1.1 上没有任何开源数据,TH1.1 的重估还把闭源模型抬高很多(GPT-5 +55%)。
6. "METR 称 DeepSeek-V3 与 6 个月前 SOTA 相当":禁用。原文主语是开源权重模型整体。
7. 把 METR 当时的官方判断(6 个月、7 个月)与自算月数串成同一条序列:禁用。例如 R1 官方说 7 个月,自算 3.4 个月。
8. "最后一个开源模型 2025-11-19":须改为"Kimi K2 Thinking(2025-11-06 发布,11-19 加入页面)"。
9. 把 AISI 的 8 个月当作对 METR 的独立佐证:禁用,它引自 METR。

### (4) 证据分级

- 方向存争 / 弱结论:round3 双席审计均下调,"2025 年拉长"只在 METR 内部、以 R1 为起点时成立。
- 单源已核:滞后点估计在三票和 round3 中均能复现(插值法 6.2/3.4/6.8/7.2/8.2);引语逐字一致;"TH1.1 无开源"多方确认。
- 冲突说明:
  - Kimi p50:票 1 写官方 54(CI 25–100);票 2 写 METR/Epoch 公布 54.2、自拟合 57.6;票 3 写修正后官方 57.6、旧版 54.2;Wikipedia 转录为 58。锁定写法:"约 54–58 分钟(依版本)"。
  - 阶梯法下 V3 的滞后:票 1 为 6.2,票 2、票 3 为 3.4。
  - Kimi 插值滞后:票 1 为 8.1,票 2、票 3 及 round3 为 8.2。
- round3 bootstrap(2024 起前沿趋势):Kimi 8.6 [7.1, 10.7]、R1 3.9 [2.0, 6.1];Kimi 减 R1-0528 不可区分(P(>0) 0.70–0.86)。

### (5) 一手 URL

- https://raw.githubusercontent.com/METR/eval-analysis-public/main/reports/time-horizon-1-0/data/raw/runs.jsonl
- https://metr.org/assets/benchmark_results_1_0.yaml
- https://metr.org/assets/benchmark_results_1_1.yaml
- https://metr.org/time-horizons/ (更新日志)
- https://metr.org/evaluations/deepseek-v3-report/
- https://metr.org/evaluations/deepseek-r1-report/
- https://metr.org/evaluations/deepseek-qwen-report/
- https://metr.org/blog/2026-1-29-time-horizon-1-1/
- https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
- https://epoch.ai/data-insights/open-closed-eci-gap
- https://www.aisi.gov.uk/work/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
- Epoch benchmark_data.zip → metr_time_horizons_external.csv(METR version 列)

# 锁定口径 · Part 5(G19–G22)

> 文章:「AI 能力最终会趋同是真的吗」(截至 2026-10)。依据:verdicts/G19–G22 三票全文 + 04-verification-round3(R1 ECI 差距、R2 METR、R4 CAISI 8 个月)。
> 规则:三票冲突时取最严格的修正;数字以有复算或逐字核对的那一票为准,冲突处列出各票的数字。本文件不添加票里没有的事实。

### 跨组统一口径:Qwen3.8-Max 的开源属性(G19、G20、G22 共用)

- 冲突:G19 票 1 和 G20 票 1 依据 HF 一手 README:"Qwen3.8-Max is the official version based on Qwen3.8-2.4T-A95B"(权重 2026-08-08 开放,qwen3.8-max 定制许可;API 版另加视觉、1M 上下文)。G19 票 3、G20 票 2/3 依据 Epoch 元数据的 "API access",称其为"阿里闭源"。
- 锁定(取最严):**"阿里闭源"判死**,因为有一手证据推翻。也**不能直接写"开源"**,因为 API 版本身只走 API,而且 τ² 提交日期 2026-08-04 早于权重开放 4 天。
- 统一写法:「Qwen 3.8 Max(阿里;API 版本,基于 2026-08-08 开放权重的 Qwen3.8-2.4T-A95B,定制许可)」。归属须标注,只能写成"中国模型"或"开放权重系的 API 版",不能单独算进"闭源"或"开源"任何一边。

---

## G19 · 智能体/长程基准上的开源–闭源差距(Terminal-Bench 3.0/4.0/2.0、APEX-Agents、OSWorld 2、Vending-Bench 2)

票型:CORRECTED ×3(三票均为单源已核)

### (1) 锁定表述

- **TB3.0 饱和论**:Terminal-Bench 团队在 3.0 公告中承认,旧版很多任务已饱和,榜单"挤在很窄的区间"。同一组六个闭源模型(各用自家 harness:Claude Code / Codex / Cursor CLI)在 TB2.1 上分布于 **74.6–83.8%**,在 TB3.0 上拉开到 **14.3–33.8%**。不在这组六个里的 GPT-5.6 Sol 为 34.4%,居 TB3.0 榜首,但它没有 TB2.1 分数。Fable 5 与 Opus 4.8 的差距从 TB2.1 的 **4.9 分**扩大到 TB3.0 的 **12.7 分**。GLM 5.2(Claude Code harness)在 TB3.0 上只有 **5.1%**。TB3.0 仅 74 题;公告日期页面上未能核到。
- **TB4.0 公开榜**(updated 2026-10-06,每个条目 330 trials):Opus 5.5(Claude Code, max)**64.8±3.1**、Sonnet 5.5 61.8、GPT-6 Astra(Codex, max)58.2、GPT-6.1 Sol 58.2、Fable 5.1(max)57.9、开放权重 GLM-5.3(Claude Code, max)**41.8±3.2**、Grok 4.7(xhigh)37.6、Qwen3.8-Max-0902(Claude Code)27.0。Anthropic 自报的 **66.4%** 是 **xhigh 档、自家 setup**(SE ±2.6),公开榜上只有 max 档,没有 xhigh 行。两者相差 1.6 分,在噪声范围内**不矛盾**,但配置不同,不是同一条测量。
- **TB2.0 同 harness(Terminus 2)回溯序列**(Epoch 转录;"时点"指模型发布月份,TB2.0 本身 2025-11 才发布):闭源最佳 vs 开源最佳,截至 2025-08 为 **38.0 vs 27.8**(Opus 4.1 / Kimi K2)、截至 2025-11 为 **57.8 vs 35.7**(Opus 4.5 / Kimi K2 Thinking)、截至 2026-02 为 **64.7 vs 52.4**(GPT-5.3-Codex / GLM-5;HF 原始 result.json 复算 GLM-5 为 51.9)。差距依次是 **10.2 → 22.1 → 12.3 分,先扩后缩,不是单调变化**。2026-02 之后没有开源模型的 Terminus 2 条目,序列到此为止。混合 harness 下榜首为 GPT-5.5 + NexAU-AHE **84.7%**(第三方 agent,组织 china-qijizhifeng)。
- **APEX-Agents**(Epoch 转录,2026-09):Gemini 4 Argon **82.2**(effort 未知,SE 4.4)、Sonnet 5.5 75.5、Opus 5.5(max)73.5。开放权重最佳为 **MiMo-V2.6-Pro 59.5**(2026-09-21,MIT 许可),其后依次是 GLM-5.3 **56.6**(NIST 证实已开放权重)、GLM-5.3-Flash 52.8、Kimi K3 50.6(non-commercial 许可)。闭源与开放权重最佳的差距:票 2/3 算为 **约 22.7 分**,票 1 给区间 19–23 分;如果把 Qwen3.8-Max 63.3 算进开放权重系,差距取下端。
- **OSWorld 2**:Opus 5(max,**batch tool**,500 步)binary **31.4%**,开源最高为 MiniMax-M3 和 Kimi K2.6 的 **4.6%**(**standard** 设置)。算术上是 6.83x,但两边工具设置不同,而且开源一侧只测了 2026-04~06 的旧模型,Kimi K3、GLM-5.x、MiMo-V2.6、DeepSeek V4 都没测。同 standard 设置下,Opus 4.8 max 18.5 对 4.6 约 **4.0x**;同期 Opus 4.7 standard 13.9 对 Kimi K2.6 约 3.0x;按 partial score 算是 68.3 vs 22.3,约 **3.1x**。锁定写法:**"同条件比约 3–4 倍"**。另外,4.6% 是极低的基数,算比值会放大差距。旧版 OSWorld 是 Sonnet 4.6 72.1 对 Kimi K2.5 63.3,属于 2026-02 前后的旧快照。
- **Vending-Bench 2**(Andon Labs;仅计入盈利模型、线性回归):中国 SOTA 线 +$1,047/月(R²=0.98),西方 +$822/月(R²=0.95),两条拟合线相差"约 111 天",**预测** 2027-10 交叉。这里的"Chinese"指中国 SOTA(含闭源),不等于开源。榜单:GPT-6 Astra **$15,515**(±$1,074),GLM-5.2 **$8,314**。**反证**:按原始累计 SOTA,中国最高分自 2026-06-16(GLM-5.2)以来没有被超过,GLM-5.3 为 $8,164,Kimi K3 为 $5,165;同期西方从 Opus 4.7 $10,937 涨到 $15,515。按当前时点算,实际滞后**约 6–8 个月**(票 2 算约 8 个月,对应西方 2026-02 的 Opus 4.6 $8,018;票 3 算约 6 个月,对应 2026-04 前后)。近 4 个月的停滞与线性交叉的外推方向相反。单点噪声也很大,比如 Opus 5.5 $9,235 低于 Opus 5 $11,182。

### (2) 英文原文引语(逐字)

- TB3.0: "Many Terminal-Bench tasks have become saturated and leaderboard entries are condensed into a narrow range that may not fully represent capability gaps across models."(引用须保留后半句,或在截断处加省略号)
- TB3.0: "Fable 5 in Claude Code and Opus 4.8 in Claude Code are separated by only 4.9 points on Terminal-Bench 2.1, but 12.7 points on Terminal-Bench 3.0"
- Anthropic: "Terminal-Bench 4.0 results are reported for Claude Opus 5.5 at xhigh effort" / "The standard error is ±2.6 pts"
- NIST(GLM-5.3): "Z.ai publicly released the model's weights two weeks later"
- Andon Labs: "Chinese: +$1,047/month (R² = 0.98) · Western: +$822/month (R² = 0.95) · Chinese lags by ~111 days · Projected crossover: Oct 2027";"Only profitable models are included"

### (3) 判死 / 禁用清单

1. **APEX-Agents"最佳开源 GLM-5.3-Flash 52.8"、"差 29.4 分"→ 判死。** MiMo-V2.6-Pro 59.5(MIT 开放权重)和 GLM-5.3 56.6(已开放权重)都更高,差距约 22.7 分(区间 19–23)。原稿很可能被 Epoch 过时的 accessibility 字段误导。
2. **"六个闭源 TB3.0 为 14.3–34.4"→ 禁用。** 这把两个集合混在了一起:同组六个是 14.3–33.8,34.4 属于没有 TB2.1 对照的 GPT-5.6 Sol。
3. **"TB4 公开榜与 Anthropic 自报 66.4% 一致(同一测量)"→ 禁用。** 66.4 是 xhigh、自家 setup,64.8 是 max、公开榜,只能说"在噪声内不矛盾"。
4. **把 TB2.0 序列写成"差距持续扩大/单调分化"→ 禁用。** 实际是 10.2→22.1→12.3,先扩后缩,且只到 2026-02。"2025-08"不能写成当时的榜单时点。
5. **OSWorld 2"开源差 6.8 倍"不加限定 → 禁用。** 工具设置不同(batch vs standard),开源是旧模型,基数又低。同条件比约 3–4 倍。
6. **Vending-Bench 2"中国只落后约 111 天、2027-10 将交叉"当作现状或事实 → 禁用。** 111 天是两条拟合线的时移,交叉是线性外推;按原始 SOTA,当前滞后约 6–8 个月,且中国 SOTA 自 6 月起停滞。"Chinese"也不能换写成"开源"。
7. **把 Qwen3.8-Max(TB4.0 27.0)算作"闭源"或"开源"任何一边 → 禁用**,见文首统一口径。

### (4) 证据分级

- TB3.0 饱和引语、4.9→12.7、六模型区间:**单源已核**(tbench.ai 公告,三票逐字一致)
- TB4.0 榜单数字:**单源已核**(三票核对榜单 JSON);Anthropic 66.4%:**厂商口径**(xhigh、自家 setup)
- TB2.0 Terminus 2 序列:**单源已核**(Epoch 转录,另有 HF result.json 复算);"开源差距在扩大"这一方向:**方向存争**(先扩后缩)
- APEX-Agents 数字:**单源已核**(Epoch 转录);开源归属依据 HF 和 NIST 一手
- OSWorld 2 比值:**单源已核**,但口径不对等,数字只能带限定使用
- Vending-Bench 2 的 111 天和交叉:**厂商口径**(Andon Labs 回归、外推);当前 6–8 个月滞后:票内复算,**方向存争**(票 2 为 8 个月,票 3 为 6 个月)

### (5) 主要一手 URL

- https://www.tbench.ai/news/terminal-bench-3-0
- https://www.tbench.ai/leaderboard/terminal-bench/4.0
- https://www.anthropic.com/news/claude-opus-5-5
- https://epoch.ai/data/benchmark_data.zip(terminalbench_external / apex_agents_external / osworld_2_external / os_world_external / vending_bench_2_external / model_metadata)
- HF harborframework/terminal-bench-2-leaderboard(原始 result.json);HF XiaomiMiMo/MiMo-V2.6-Pro-RL;HF Qwen/Qwen3.8-2.4T-A95B README
- https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities
- https://andonlabs.com/evals/vending-bench-2

---

## G20 · τ²-bench 可靠性(pass^k)上的开源–闭源差距

票型:CORRECTED ×3(三票均为单源已核)

### (1) 锁定表述

- **banking_knowledge 域**:Sierra 2026-08-04 统一批次,tau2 v1.0.1,AllTools 检索,GPT-5.2 低推理用户模拟器,seed 300,**97 题 × 4 trials**。各模型 pass^1 / pass^4:Claude Opus 5(max)**48.7 / 32.0**,GLM-5.2(xhigh)**37.1 / 13.4**,Kimi K3(max)**37.1 / 17.5**。单次成功率差 **1.31 倍**,四次全对的比率差到**约 1.8–2.4 倍**。后者只基于 31、13、17 题的计数,误差很大:票 2 粗估 2.39x 的 95% 区间约为 1.3–4.5x,票 3 估 SE 约 3.5–4.7pp。Opus 5 也不是闭源第一,同批 Grok 4.5 为 47.9 / 32.0。
- **榜首**:Qwen 3.8 Max(xhigh)**55.2 / 35.1**,pass^1 和 pass^4 都高于 Opus 5。归属按文首统一口径写,即"基于开放权重 Qwen3.8-2.4T-A95B 的 API 版"。
- **保持率 pass^4/pass^1**:只在 pass^1 相近(37–41)的模型之间比较时,开源 GLM-5.2 为 0.36、Kimi K3 为 0.47,闭源 Opus 4.8 为 0.57、GPT-5.4 为 0.55、Opus 4.7 为 0.62、Fable 5 为 0.73、Muse Spark 1.1 为 0.51。方向是开源偏低,但与最差的闭源只差约 1–2 个 SE。**这不是干净的开源/闭源分界,也不是中美分界**,反例有:Muse Spark 1.1 0.51、Inkling 0.45(美国,与开源相近);Gemini 3 Pro 0.23、Gemini 2.5 Pro 0.08(闭源,低保持率);Grok 4.5 0.67、Qwen 3.8 Max 0.64。Anthropic 内部也不单调:Opus 4.6 0.42 → 4.7 0.62 → 4.8 0.57 → Opus 5 0.66。保持率还会随 pass^1 水平机械变化。
- **老域上开源已追平甚至反超**(2026-02/03 批次,同为 gpt-5.2 模拟器,接近饱和):telecom 上 Qwen3.5-397B **97.8 / 92.1**,Opus 4.5(high)92.3 / 78.1;airline 上 GLM-5 **82.5 / 70.0**,Opus 4.5 84.0 / 70.0。
- **历史背景**:τ-bench 原论文(2024)已指出,gpt-4o 级函数调用 agent 在 retail 上 pass^8 不足 25%。
- **方法学限定(须写入)**:pass^k 同时计入被测 agent 和 LLM 用户模拟器的随机性,只能在同一模拟器的批次内比较。老条目混用 gpt-4.1、DeepSeek-V3.2、Gemini-3.0-Pro、claude-sonnet-4.5 等模拟器,跨批次不可比;Qwen3-Max-Thinking 的 98.2 / 93.9 用的是 gpt-4.1 模拟器,不能并入比较。

### (2) 英文原文引语(逐字)

- Sierra 提交 notes:"GPT-5.2 low-reasoning user simulation, four trials, and seed 300"
- τ-bench 摘要:"succeed on <50% of the tasks, and are quite inconsistent (pass^8 <25% in retail)"

### (3) 判死 / 禁用清单

1. **"banking 第一为阿里闭源 Qwen 3.8 Max"→ 判死**(票 1 有 HF 一手 README)。改用文首统一口径。榜首属于中国开放权重系,这与"开源可靠性全面落后"的叙事直接冲突,须写入正文。
2. **"开源可靠性全面落后 / 开源–闭源(或中美)存在干净分界"→ 判死。** 反例:Muse Spark、Inkling、Gemini 3 Pro 的保持率都低;Qwen 3.8 Max 居榜首;老域上开源已反超。
3. **"Opus 4.5 → Opus 5 保持率从 0.46 升到 0.66 是代际进步"→ 禁用。** 推理档位变了(high → max),而且 Anthropic 内部序列本身不单调。
4. **把 GLM-5 的保持率 0.32 并入比较 → 禁用。** 它的 pass^1 只有 9.8,落在低分区;票 1 还指出该条检索配置是 text-emb-3-large,不是 alltools。同为 pass^1 9.8 的 Qwen3.5-397B 保持率是 0.53。
5. **"pass^4 差 2.39 倍"作为精确倍数且不注样本 → 禁用。** 应写"约 1.8–2.4 倍(97 题,小样本)"。
6. **跨批次或跨模拟器比较 pass^k → 禁用。**

### (4) 证据分级

- banking、telecom、airline 的各项数字:**单源已核**(sierra-research/tau2-bench 仓库 submission.json,三票全量复算一致)
- "一致性差距大于单次成功率差距"的方向:**单源已核**,但为小样本
- "开源保持率系统性低于闭源":**方向存争**
- τ-bench pass^8 引语:**单源已核**(arXiv 摘要)

### (5) 主要一手 URL

- https://github.com/sierra-research/tau2-bench(web/leaderboard/public/submissions/*/submission.json)
- https://arxiv.org/abs/2406.12045
- HF Qwen/Qwen3.8-2.4T-A95B README

---

## G21 · 政府评测机构的落后月数(NIST CAISI / UK AISI)

票型:CORRECTED ×3(三票均为多源证实)。吸收了 Round 3 R4(CAISI 8 个月)的限定。

### (1) 锁定表述

- **DeepSeek V4 Pro**(CAISI,2026-05-01):CAISI 用含非公开基准的 IRT 聚合(Figure 1 为 16 个基准 × 35 个模型,本次评测表格只列 9 个基准,两者没有对上;8 个月具体怎么从趋势线算出来没有披露)判定它**落后前沿约 8 个月**,水平相当于约 8 个月前发布的 GPT-5。DeepSeek 自报的数据则显示它与约 2 个月前发布的 Opus 4.6、GPT-5.4 相当。**"2 个月"是"自报对标模型的发布间隔",与 8 个月不是同一把尺子。**
- **独立复核**(Round 3 R4):在 Epoch ECI 上自算,V4 Pro(2026-04-24)ECI 149.13(CI 147.31–150.72),约等于 GPT-5,落后约 **8.5–8.6 个月**,按 CI 端点算区间约 5–10.5 个月;后续的 V4 Pro 0813 仍落后约 6–8 个月。Artificial Analysis 的指数隐含约 4–5 个月,有版本漂移,无法确切换算。所以锁定写法是:**"独立测量给出约 4–9 个月,CAISI 与 Epoch 都约 8 个月"**。这两源并非完全独立:都含私有题,都用类 IRT 聚合,部分题目重叠。另外,8 个月针对的是 V4 Pro 单个模型,推成"中国前沿落后 8 个月"是外推。
- **分项**(NIST 页面 Figure 2 的 HTML 表格,不是从图上读的;列为 GPT-5.5 xhigh / Opus 4.6 max / V4 Pro max):PortBench **78 / 60 / 44**;CTF-Archive-Diamond **71 / 46 / 32**(V4 的值是 IRT 插补);ARC-AGI-2 半私有集 **79 / 63 / 46**(任务均分,不是官方口径);GPQA-Diamond **96 / 91 / 90**;OTIS-AIME-2025 **100 / 92 / 97**(V4 在数学上反超 Opus 4.6)。差距集中在私有和智能体/网络安全类题;知识题、数学题基本持平。对 2 个月口径下的对标模型 Opus 4.6,私有题差约 **14–17pp**;30pp 以上的差距是对 GPT-5.5 而言(R4)。
- **DeepSeek V3.1 报告**(2025-09-30):完整报告 PDF 称,在**软件工程和网络安全**两个领域,最佳美国模型多解 **20–80%** 的任务。这是相对增幅,不是百分点。新闻稿的写法是"over 20% more"。发布时商务部长 Lutnick 做了明显的政治定调,评测本身是应 AI Action Plan 的指令做的。
- **GLM-5.2**(CAISI,2026-07-17):整体能力约等于 GPT-5.2(2025-12),网络安全能力约等于 Opus 4.6(2026-02)。
- **GLM-5.3**(CAISI,2026-09-17):网络安全聚合指数**约落后美国前沿 4 个月**,但单项差距悬殊:SEC-Bench Pro **40.4%(74/183)vs 90.2%**,ExploitGym(Userspace)**9.4%(47/498)vs 44.4%(223/502)**,OSS-Fuzz **7.7% vs 23.2%**,ExploitBench 61.1% vs 100%。须注明,这里的"美国前沿最佳"是**逐个基准取任一美国模型的最高分**(含 trusted-access 版本),而且测美国模型时**关闭了网络安全防护**。这是一条上包络,会高估对任何单一公开模型的差距。4 个月的 IRT 综合指数与单项 2–4 倍的差距并不矛盾。PRC 此前在 SEC-Bench Pro 上的最佳只有 27.3%,进步很快。GLM-5.3 先上 API,两周后才开放权重。
- **UK AISI**(2026-07-17):开放权重模型在网络安全上落后前沿 **4–7 个月**,比 2025 年 1–9 月发布的开放权重模型测得的 6–10 个月更窄。4–7 个月特指 **GLM-5.2**:窄任务上约等于 Opus 4.6(约 4 个月),cyber range 上约等于 Opus 4.5(约 7 个月)。DeepSeek V4-Pro 在窄任务上约落后 5 个月。长程 cyber range 上差距更大,但 AISI 自认这部分是**较弱证据**,并声明结论不能预测之后开放模型能否复制 Mythos Preview 和 GPT-5.5 的跃升。
- **Kimi K3**(**UK AISI 与 CAISI 联合**初评,2026-07-23,发在 NIST 页面):在 32 步攻击路径上平均到**第 17 步**,最强美国模型平均 **28.5 步**,GLM-5.2 为第 11 步;10 次尝试中 K3 完成 1 次;ExploitBench ACE 为 0/41 对 20/41。美国闭源模型是在**关闭系统级防护**的条件下测的,公开版本是开启的。K3 的总体网络安全能力只由 ExploitBench 单一基准(41 题)估计,置信区间较宽。

### (2) 英文原文引语(逐字)

- CAISI V4 Pro: "CAISI evaluations indicate that DeepSeek V4's capabilities lag behind the frontier by about 8 months"
- CAISI V4 Pro: "According to DeepSeek's data, DeepSeek V4 is about as capable as Opus 4.6 and GPT-5.4, which were released about 2 months ago. However, CAISI's evaluations, which include non-public benchmarks, indicate that DeepSeek V4 performs similarly to GPT-5, which was released about 8 months ago"
- 表格脚注:"Imputed from a subset of samples via IRT";ARC-AGI-2 为 "mean score across tasks, which differs from ARC-AGI-2's official score aggregation"
- V3.1 报告 PDF: "the best U.S. model solves 20-80% more tasks than the best DeepSeek model"(限 software engineering 和 cyber);新闻稿: "solves over 20% more tasks"
- Lutnick: "The report is clear that American AI dominates, with DeepSeek trailing far behind"
- GLM-5.2: "GLM-5.2's overall capabilities are similar to that of GPT-5.2, released in December 2025. GLM-5.2's cyber capabilities are similar to that of Opus 4.6, released in February 2026."
- GLM-5.3: "lags the capability level of the U.S. frontier by about four months in an aggregate measure";"including both trusted-access releases and full public releases";"U.S. models were tested with cyber safeguards disabled"
- UK AISI: "it trails the frontier by 4 to 7 months. This is narrower than the 6 to 10 month gap we measured in internal evaluations of open weight models released from January to September 2025";"we treat the comparison from our ranges as weaker evidence";"not predictive of whether future open weight models will replicate the more recent jumps delivered by Mythos Preview and GPT-5.5"
- Kimi K3 联合页: "Kimi K3 reached step 17 of this 32-step attack path, while the most cyber-capable U.S. models reached 28.5 steps on average";"U.S. closed-weight models were evaluated with system-level safeguards disabled to reduce refusals and enable measurement of maximal capabilities. Publicly available versions of these models have these safeguards enabled."

### (3) 判死 / 禁用清单

1. **"20–80%"标为新闻稿内容,或泛化到全部基准 → 禁用。** 它出自完整报告 PDF,只限软件工程和网络安全两个领域,是相对增幅;新闻稿写的是"over 20%"。
2. **"厂商说 2 个月、独立评测说 8 个月,同一尺度相差 4 倍"→ 禁用**(R4)。2 个月是自报对标模型的发布间隔。正确写法是"2 个月 vs 独立测量的 4–9 个月"。
3. **"私有题差 30+pp"作为对标差距 → 禁用**(R4)。那是对 GPT-5.5 的差距;对 Opus 4.6 约为 14–17pp。
4. **"公开榜追平源于针对公开考卷的优化/刷题"作为结论 → 判死**(R4)。没有直接证据,CAISI 原文也没有讨论污染;题目饱和、闭源方接触过"私有"题、脚手架差异、赢家诅咒都能解释同样的格局。最多只能写成"一种推测"。
5. **"CAISI 测得中国前沿落后 8 个月"→ 禁用。** 8 个月只针对 V4 Pro 单个模型。
6. **GLM-5.3 单项差距写成"对美国某个公开模型"→ 禁用。** 对照方是逐基准取最高分的包络(含 trusted-access 版本、关闭防护)。
7. **把"4–7 个月"写成泛指全体开源模型,或把 Kimi K3 评测写成"AISI 单独"所做 → 禁用。** 4–7 个月特指 GLM-5.2;Kimi K3 那份是 UK AISI 与 CAISI 的联合初评。
8. **"长程 cyber range 差距更大"不加 AISI 自己的"较弱证据"限定 → 禁用。**

### (4) 证据分级

- CAISI V4 Pro 8 个月:**多源证实**(CAISI,加 Round 3 在 Epoch ECI 上的复算约 8.5 个月;两源并非完全独立)
- "2 个月":**厂商口径**(DeepSeek 自报,经 CAISI 转述)
- 分项表、GLM-5.2/5.3、AISI 4–7 个月、Kimi K3 17 vs 28.5 步:**多源证实**(NIST 和 AISI 一手页面,三票逐字一致)
- "差距集中在私有/智能体题":**方向存争**(格局成立,但与题目饱和度、题型共线)
- "针对公开题优化"这一机制:**未验证**
- Stanford AI Index"公开榜差距 2.7%":**未验证**(二手转引),只能并列说明量尺不同

### (5) 主要一手 URL

- https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
- https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks
- https://www.nist.gov/document/caisi-evaluation-deepseek-ai-models-report
- https://www.nist.gov/news-events/news/2026/07/caisi-assessment-zais-glm-52
- https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities
- https://www.nist.gov/news-events/news/2026/07/uk-aisi-caisi-preliminary-assessment-kimi-k3s-cyber-capabilities
- https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
- 独立复核:https://epoch.ai/data/benchmark_data.zip(eci_scores.csv;Round 3 R4)

---

## G22 · 跨基准开源/闭源比值、AA 指数与"落后几个月"的诸家估计

票型:CORRECTED ×3(三票均为单源已核)。吸收了 Round 3 R1(ECI 差距)和 R4 的限定。

### (1) 锁定表述

- **自算比值**:数据为 Epoch 2026-10 下载;开源指 Epoch 标注为 open weights 的模型(含 non-commercial,如 Kimi K3);分母是"发布日不晚于该开源模型的闭源最佳",衡量的是"开源追平同期闭源到什么程度"。
  - 知识类和接近饱和的基准:GPQA **0.98**(Kimi K3 0.931 vs GPT-5.4 Pro 0.946)、SWE-bench Verified **0.94**(GLM-5.2 0.787 vs Opus 4.7 0.835)、DeepSWE **0.94**(Kimi K3 0.685 vs GPT-5.6 Sol 0.727)、旧版 OSWorld **0.95**(Kimi K2.5 63.3 vs Opus 4.5 66.3;不是 OSWorld 2)。其中 DeepSWE 和 OSWorld 本身就是 agentic 基准。
  - 较难的 agentic 和数学基准:FrontierMath T1-3 **0.81**;APEX-Agents **0.78**(只计 Epoch 标注的开源模型:GLM-5.3-Flash 0.528 vs Gemini 3.7 Flash 0.678),若计入 Epoch 漏标的 MiMo-V2.6-Pro 则为 **0.87**(0.595 vs Claude Fable 5.1 0.686);Terminal-Bench 2.0 同 harness(Terminus 2)**0.83**(GLM-5 0.524 vs Opus 4.6 0.629);FrontierSWE **0.55**(Kimi K3 0.259 vs Claude Fable 5 0.470)。
  - 锁定概括:**"知识/饱和类 0.94–0.98;较难的 agentic/数学类约 0.55–0.87(随 harness 和开源定义变化)"。** 分化确实存在,但集中在最难的长程工程和数学任务上,幅度比原稿小。
  - HLE(0.65,Kimi K2.5 是 2026-01 的数据点)和 METR 时间跨度(0.27,Kimi K2 Thinking 是 2025-11 的数据点,与 GPT-5 配对)的开源数据过旧,反映的是 Epoch 的收录缺口。METR 是分钟数比值,和正确率比值量纲不同,只能单列或删除。AA 2026-04 同期的 HLE 比值约 0.77–0.82(票 2)。
  - 如果改用"当前闭源最佳"做分母,比值明显更低:HLE 0.45、FrontierSWE 0.40、METR 0.05、Terminal-Bench 0.62、APEX 0.64(或 0.72)。
- **Artificial Analysis 2026-04-30**:Kimi K2.6 和 MiMo V2.5 Pro 并列开源第一,54 分。AA 原文说这"在领先闭源模型的 3–6 点以内",具体是距 GPT-5.5(xhigh)的 60 分 **6 点**,距 Gemini 3.1 Pro 和 Opus 4.7 的 57 分 **3 点**。一年前约 **13 点**(DeepSeek V3 0324 22 vs Claude 3.7 Sonnet 35)。AA 也写明在最难的推理和 agentic 编码评测上差距仍大;前 10 名开源模型全部来自中国实验室。
- **AA 当前榜**(2026-10-12):Opus 5.5(max with fallback)**58**;Claude Sonnet 5.5 和 Muse Wonder Full **56**;GPT-6 Astra(max)**53**、Gemini 4 Argon(**high**)**53**、Fable 5.1 53、GPT-6.1 Sol 52;开源最高 MiMo-V2.6-Pro **46**、Kimi K3(max)**44**。在当前版本内,开源与闭源相差 **12 点**。版本号"v4.3":票 3 从 AA 首页图表 JSON 核到,票 1/2 在页面上没找到,Round 3 也按 v4.3 引用,所以写入时标注"(AA 当前版本)"即可,不强调版本号。**不能把它与 4 月的 6 点并成一条趋势**:跨了指数版本,比如 Kimi K3 在 v4.1 是 57 分、当前是 44 分(R1)。
- **Ihle**(LessWrong,2026-05-28,17 个基准,约 110 个数据点):开源模型在私有基准上落后闭源前沿 **8–10 个月**,公开基准上落后 **4–6 个月**;差距在 2025 年 1 月 DeepSeek R1 前后最小,此后扩大。限定:比较对象是全体开源 vs 闭源,不是中美;这是 backward-looking 的度量;作者自承部分"私有"基准并不完全私有,第三方推理服务降级可能夸大差距,存在赢家诅咒;作者本人运营被纳入的 WeirdML。
- **Epoch 中美比较**(2026-01-02,Luke Emberson):按 ECI 衡量,2023 年以来前沿模型都出自美国,中国模型平均落后 **7 个月**(最短 4,最长 14)。这是国别比较。票 2 用当前 ECI 复算,平均约 7.5–8 个月,区间因重拟合漂移为 1.1–18.1;截至 2026-10,ECI 前沿仍全部是美国模型。
- **Epoch 开源/闭源比较**(Data Insight,2026-05-29):2026 年以来最强开源权重模型平均落后 **4 个月**(约 8 个 ECI 点),比 2025 年的约 3 个月"slightly larger"(票 2 与 Round 3 都引用了)。UK AISI 网络安全的数字是 4–7 个月,且在收窄(见 G21)。所以"落后多少个月"的各家估计在 **4–10 个月**之间,取决于量尺。
- **Round 3 R1 背景**:在 ECI 同一次拟合里,2026 年开源与闭源的差距**没有收窄**(2026-10 约 10 点,bootstrap 90% 区间约 8–14)。但"扩大一倍"取决于拿 2025 年哪个时点作基准,不可用。AA 指数在 2025-04 到 2026-04 曾经收窄。

### (2) 英文原文引语(逐字)

- AA: "tie as the leading open weights models on the Artificial Analysis Intelligence Index at 54";"within 3-6 points of the leading proprietary models";"The gap to proprietary remains wide on the hardest reasoning and agentic coding evaluations.";"The top 10 open weights models on the Intelligence Index are all from China-based AI labs."
- AA 当前榜: "MiMo-V2.6-Pro is the highest-ranked open weights model with an Intelligence Index score of 46"
- Ihle: "on private benchmarks ... open models are roughly 8-10 months behind the closed frontier, while for public benchmarks the gap is roughly 4-6 months. We also find that the gap was smallest around the time of DeepSeek R1, in Jan 2025, and since then the gap has been growing."
- Epoch: "Since 2023, every model at the frontier of AI capabilities, as measured by the Epoch Capabilities Index, has been developed in the United States." / "trailed US capabilities by an average of seven months, with a minimum gap of four months and a maximum gap of 14."

### (3) 判死 / 禁用清单

1. **APEX-Agents 0.78 不加定义 → 禁用。** 须注明"只计 Epoch 标注的开源模型";计入 MiMo-V2.6-Pro 则为 0.87。APEX 不宜作为"低比值"的例证。
2. **Terminal-Bench 2.0 0.66 → 判死**(票 2/3)。这是跨 harness 的比值:GLM-5 用 Terminus 2,Opus 4.6 的 0.798 用的是 ForgeCode 第三方 agent。同 harness 为 0.83。
3. **METR 0.27 与正确率比值并列 → 禁用。** 量纲不同(分钟数),而且开源数据点停在 2025-11。
4. **HLE 0.65 作为当前差距 → 禁用。** 那是 2026-01 的陈旧配对。
5. **"饱和/知识 0.94–0.98 vs 长程 agentic 0.27–0.78"这种分组 → 判死。** DeepSWE、OSWorld 本身是 agentic 却在 0.94–0.95;修正后的低值只剩 FrontierSWE 0.55 和 FrontierMath 0.81。
6. **"最佳开源距 GPT-5.5(60)3–6 点"→ 判死。** 对 GPT-5.5 是 6 点;3 点是对 Gemini 3.1 Pro 和 Opus 4.7(57)而言。
7. **只列 Opus 5.5 58、GPT-6 Astra 53、Gemini 4 Argon 53,暗示 GPT-6 Astra 排第二 → 禁用。** 第二是 Sonnet 5.5 和 Muse Wonder Full(56)。Opus 5.5 须注"max with fallback",Gemini 4 Argon 是 high 档。
8. **把 AA 4 月的 6 点和当前的 12 点并成"差距翻倍"的趋势 → 禁用**(跨指数版本)。同样,"ECI 差距 2026 年扩大一倍"也禁用(R1)。
9. **把 Ihle 的数字写成中美差距,或把 Epoch 的 7 个月写成开源/闭源差距 → 禁用。** 前者是开源 vs 闭源,后者是国别比较。
10. **称 Epoch 自己说过"open-weight models tend to perform worse on private benchmarks"→ 禁用**(R4 未找到这句原话)。

### (4) 证据分级

- 十个比值的数字:**单源已核**(Epoch 数据,三票复现);开源定义、harness、数据陈旧的修正:票内一手核对
- AA 4/30 文章引语与分数:**单源已核**;AA 当前榜数值:**单源已核**;版本号:**单票核到**
- Ihle 8–10 / 4–6 个月:**单源已核**(原文逐字);其中"差距在扩大"这一方向:**方向存争**(Epoch 4 个月"slightly larger",AISI 网络安全在收窄)
- Epoch 7 个月(中美):**单源已核**,平均值稳健,区间随重拟合漂移
- Epoch 开源落后 4 个月:**单源已核**(票 2 和 Round 3 引用)
- Mozilla 约 4.4 个月:**未验证**(只见二手摘要)

### (5) 主要一手 URL

- https://epoch.ai/data/benchmark_data.zip(各基准 csv、model_metadata、eci_scores、processed_data_for_eci)
- https://www.artificialanalysis.ai/articles/recent-open-weights-model-launches
- https://artificialanalysis.ai/leaderboards/models
- https://www.lesswrong.com/posts/rJcCrXyEsJKmmDpWG/how-far-behind-are-open-models
- https://epoch.ai/data-insights/us-vs-china-eci
- https://epoch.ai/data-insights/open-closed-eci-gap

# 锁定口径 · Part 6(G23–G27)

> 文章「AI 能力最终会趋同是真的吗」(截至 2026-10)。规则:三票冲突取最严;数字以复算/逐字核对票为准,冲突处列明各票数字。背景吸收 04-verification-round3.md 中 R1(ECI 重拟合漂移)的限定,仅用于 G25。

---

## G23 · 蒸馏能追平到哪:R1-Distill、模仿的天花板、Anthropic 蒸馏指控、MEM1 的 SFT 崩溃

票型:CORRECTED / CORRECTED / HOLDS

### (1) 锁定表述

- **R1 蒸馏 vs 直接 RL(同一基座)**:DeepSeek-R1 论文(arXiv 2501.12948)自报,在同一 Qwen-32B 基座上,从 R1 蒸馏得到的 R1-Distill-Qwen-32B 在 AIME 2024 上 pass@1 为 **72.6**,直接做大规模 RL 的 R1-Zero-Qwen-32B 只有 **47.0**。作者同时写道:蒸馏"经济且有效",但要突破智能边界,可能仍需要更强的基座和更大规模的 RL。
- **R1 对 o1-1217(厂商口径)**:按 DeepSeek 自报表格,AIME 2024 为 79.8 对 79.2,GPQA Diamond 为 71.5 对 75.7,SimpleQA 为 30.1 对 47.0。o1-1217 的数字是 DeepSeek 引自 OpenAI 报告,不是同一套评测流程下的独立复测。
- **模仿的天花板(限定实验设置)**:Gudibande 等(ICLR 2024,会议版题名 *The False Promise of Imitating Proprietary Language Models*)发现,在模仿数据覆盖不足的任务上,模仿 ChatGPT 的模型几乎没有缩小基座与 ChatGPT 之间的差距。这一结论只适用于 2023 年、1.5B–13B 的 LLaMA 级基座加 ChatGPT 对话模仿数据的设置。R1 用长推理轨迹做蒸馏,在数学上迁移有效,两者在推理任务上结论方向不同,写作时要交代这层张力。
- **Anthropic 指控(单方口径)**:Anthropic 在 2026-02-23 指控 DeepSeek、Moonshot、MiniMax 通过约 **24,000** 个欺诈账户,与 Claude 产生了 **1,600 万次以上**交互。分项为 MiniMax 超过 1,300 万次、Moonshot 超过 340 万次、DeepSeek 超过 15 万次(不到总量的 1%)。Anthropic 称非法蒸馏可以"用一小部分时间和成本"获得能力,这是对非法蒸馏的一般性说法,不是对这三家的实测结论。截至检索,未见三家发布公开正式回应。该指控的归因依据是 IP、请求元数据和基础设施特征,未经独立核实。
- **MEM1 消融**:MEM1(arXiv 2506.15841)附录 D.1 的单一消融显示,在多目标 QA 任务上,用 GPT-4o 轨迹(1–3 个目标)做 SFT 的模型,在目标数超过 6 个时性能崩溃,RL 模型仍然稳健。按表 4,6 个目标时 SFT 已降到 0.088(RL 为 1.630),8 个目标时为 0.027,16 个目标时为 0.000,所以也可以写成"到 6 个目标左右即崩溃"。

### (2) 英文原文引语(逐字)

- R1: "while distillation strategies are both economical and effective, advancing beyond the boundaries of intelligence may still require more powerful base models and larger-scale reinforcement learning."
- Gudibande: "imitation models close little to none of the gap from the base LM to ChatGPT on tasks that are not heavily supported in the imitation data"
- Anthropic: "These labs generated over 16 million exchanges with Claude through approximately 24,000 fraudulent accounts, in violation of our terms of service and regional access restrictions."
- Anthropic: "in a fraction of the time, and at a fraction of the cost, that it would take to develop them independently."
  - 冲突说明:票 1 和票 3 逐字核到全句。票 2 的抓取被截断,只核到 "in a fraction of the time",但没有给出反证。因此可以引用全句,但必须标明这是 Anthropic 对非法蒸馏的一般性说法。
- MEM1: "when the number of objectives exceeds six, the performance of the SFT model collapses, whereas the RL-trained model continues to demonstrate strong robustness"

### (3) 判死 / 禁用清单

1. 「DeepSeek 大规模蒸馏 Claude」或把 1,600 万笼统算到 DeepSeek 头上 → DeepSeek 只有约 15 万次,不到 1%,大头是 MiniMax(超过 1,300 万次)。
2. 「被指控方未回应 / 默认」写成确定事实 → 只能写"截至检索未见公开正式回应"。三票都没有找到一手声明,只有二手报道称三家沉默。
3. 「蒸馏能用一小部分时间和成本追平」当作实测结论,或当作蒸馏导致能力追平的证据 → 这是 Anthropic 单方的一般性论述,未经独立核实。
4. 「R1 已追平 / 超过 o1」作为独立评测结论 → 只是厂商自报;而且 GPQA(71.5 对 75.7)和 SimpleQA(30.1 对 47.0)上 R1 仍落后。
5. 把 Gudibande 的结论外推到当今规模或推理蒸馏 → 原实验是 2023 年、≤13B、ChatGPT 对话模仿。
6. 「ICLR 2024?」的存疑写法 → 已确认是 ICLR 2024 poster,题名用 "...Proprietary Language Models"。
7. 把 MEM1 写成通用的"SFT 在复杂任务上崩溃" → 它只是附录里的单一消融,任务是多目标 QA,SFT 训练用 GPT-4o 轨迹(≤3 个目标)。

### (4) 证据分级

- R1 的 72.6 对 47.0:单源已核(论文自报,三票均逐字核对)
- R1 对 o1-1217:厂商口径
- Gudibande:单源已核(同行评审,限定在其实验设置)
- Anthropic 的 1,600 万 / 2.4 万及分项:厂商口径(单方指控,数字逐字已核)
- 蒸馏的"时间和成本"说法:厂商口径
- MEM1:单源已核(附录消融)
- 票 3 提到 2026-09 的后续报告数字更大:未验证,不得使用

### (5) 主要一手 URL

- https://arxiv.org/pdf/2501.12948v1
- https://arxiv.org/pdf/2305.15717 ;https://iclr.cc/virtual/2024/poster/18877
- https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
- https://arxiv.org/pdf/2506.15841

---

## G24 · 算力集中与中美算力差

票型:CORRECTED / CORRECTED / CORRECTED

### (1) 锁定表述

- **超大厂持有份额**:Epoch(2026-04-14)估计,Amazon、Google、Meta、Microsoft、Oracle 五家在 2025 年第四季度合计持有全球累计 AI 算力约 **71%**,2024 年第一季度为 **63%**(表中为 62.5%)。口径是芯片所有权(按 H100e 计),不是使用份额,而 AI 实验室多数是租用算力。Epoch 表中 2026 年第一季度为 75.8%,但尚未定稿,可以作为"仍在上升"的注脚。
- **单体数据中心纪录**:自 2024 年 8 月 Colossus 1 上线以来,单体 AI 数据中心的算力纪录大约每 **7 个月**翻一番(Epoch Data Insight,2026-06-11)。Epoch 同时预测,到 2027 年下半年之前,不会有数据中心明显超过 Colossus 2,也就是纪录会暂时停在平台上。
- **Epoch 数据中心库(2026-10-12 快照)**:共 94 个站点,合计约 **1,462 万 H100e**(复算 14,619,636),其中美国占 **86.3%**。≥50 万 H100e 的站点有 7 个,其中 6 个在美国(唯一例外是马来西亚 DayOne Nusajaya)。Epoch 估计这个库覆盖全球已部署 AI 算力的 **44%**(截至 2026-10-13,90% CI 23%–81%)。库是以美国为先建的,所以 86.3% 是样本内份额,不是美国占全球的份额。
  - 用户归属:Colossus 2 的用户列为 Anthropic、Cursor、SpaceXAI(xAI 现名 SpaceXAI);Fairwater Atlanta→OpenAI 标注为 #likely;Google Pryor→Google DeepMind 标注为 #speculative。
- **训练算力差距**:Epoch 估计 GPT-6 Astra 约 **1e27 FLOP**(CI 约 5e26–2e27,置信度 Likely)。
  - 2026 年发布的开放权重模型中,最大的是 Kimi K3,约 **2e25**(Speculative;非商用许可)。两者相差约 **50 倍**,计入 CI 后为 25–100 倍。
  - DeepSeek-V4-Pro(约 9.7e24,仅预训练)约小 **100 倍**(复算约 103 倍)。
  - 历来最大的开放权重模型是 Llama 3.1-405B(3.8e25,2024)。Llama Nemotron Ultra 253B 记为 3.9e25,因为计入了基座算力。相对它们差约 **26 倍**。
- **IFP 反事实基线**:IFP 在 2025 年 12 月估计,如果不向中国出口 AI 芯片、也没有走私,美国在 2026 年新产 AI 算力上将领先 **21–49 倍**(区间来自 Blackwell 按 FP4 还是 FP8 计)。同一报告称,不受限出口 H200 会把领先缩小到 6.7–1.2 倍。美国随后在 2025 年 12 月批准了 H200 销售,所以 21–49 倍只是反事实基线,不是实际预测。
- **华为对英伟达**:Epoch(Venkat Somala,2026-09-04,09-24 修订但主要结论不变)估计,华为 2026 年的 AI 算力产出不到英伟达的 **4%**。只能用国产 HBM 时,到 2028 年约为 1%;CI 上限约 6%;按显存带宽算为 1.4%。这是华为对英伟达的比较,不是中国对美国。
- **林俊旸(时任阿里 Qwen,ChinaTalk 英译)**:他说美国算力总体上可能比中国高一到两个数量级。被问到"3–5 年后领先的 AI 公司是中国公司的概率"时,他答 20%,并补了一句 20% 已经很乐观。同台的姚顺雨持较乐观的看法。

### (2) 英文原文引语(逐字)

- Epoch: "Amazon, Google, Meta, Microsoft, and Oracle collectively hold an estimated 71% of the world's cumulative AI compute as of Q4 2025 ... up from 63% in Q1 2024"
- Epoch: "Since the launch of SpaceXAI's Colossus 1 in August 2024, the record for the largest AI data center by computing capacity has doubled every seven months."
- Epoch: "no data center will have meaningfully greater capacity than Colossus 2 until the second half of 2027"
- Epoch: "we estimate this database's coverage of global deployed AI computing capacity to be 44% as of October 13, 2026 (90% CI: 23% to 81%)"
- IFP: "With no AI chip exports to China and no smuggling, we estimate the US would hold a 21–49x advantage in 2026-produced AI compute, depending on whether FP4 or FP8 performance is used for Blackwell chips."
- IFP: "Unrestricted H200 exports would shrink this advantage to between 6.7x and 1.2x"
- 林俊旸: "U.S. compute may overall exceed ours by one to two orders of magnitude." / "I think it's 20%. Twenty percent is already very optimistic"
- 华为 4% 的措辞,三票给出的版本互相冲突,**不作逐字引用,只意译**:
  - 票 1(报告正文):"Huawei will produce less than 4% of Nvidia's compute output this year."
  - 票 2(Epoch X 帖):"less than 4% of Nvidia's AI compute in 2026"
  - 票 3(报告页):"less than 4% as much AI compute as Nvidia in 2026"

### (3) 判死 / 禁用清单

1. 「该数据库只覆盖全球约 26%」→ **判死**。Epoch 页面写的是 44%(截至 2026-10-13,90% CI 23–81%),2024 年第一季度为 22%,页面上不存在 26%。
2. 「最大的开放模型是 Kimi K3」→ **判死**。最大的开放权重模型是 Llama 3.1-405B(3.8e25),Nemotron Ultra 记为 3.9e25。K3 只能说是"2026 年发布的最大开放权重模型"或"中国最大"。另外,"约 50 倍"必须写明是对 K3 的比较;对历来最大的开放模型约为 26 倍。
3. 「≥50 万 H100e 的站点服务 OpenAI/Anthropic/Google/Meta/xAI」原样照写 → 需要改。Colossus 2 的用户是 Anthropic、Cursor、SpaceXAI;Pryor→DeepMind 是 speculative;Fairwater→OpenAI 是 likely。
4. 「美国占全球 AI 算力 86%」→ 禁用。86.3% 只是这个以美国为先建的库(覆盖约 44%)里的样本内份额。
5. 「IFP 预测美国 2026 年实际领先 21–49 倍」→ 禁用。这是 2025 年 12 月、无出口且无走私的反事实基线,而 H200 后来已获批出口,在不受限出口下同一报告给出的是 6.7–1.2 倍。
6. 华为 4% 的逐字引语 → 禁用逐字引用(三票措辞不一),也禁止写成"中国对美国"。
7. 「71% 是使用份额」→ 禁用,这是所有权口径。
8. 引用林俊旸的 20% 时去掉"已经很乐观"这层限定 → 禁用。

### (4) 证据分级

- 71% / 63%、7 个月翻倍、44% 覆盖率:单源已核(Epoch)
- 1,462 万 / 86.3% / 7 个站中 6 个在美:单源已核(三票都用 CSV 复算)
- GPT-6 Astra 1e27 对 K3 2e25:单源已核(Epoch 估计;K3 为 Speculative)
- IFP 21–49 倍:单源已核(反事实)
- 华为 <4%:单源已核(Epoch 预测;措辞存在冲突)
- 林俊旸:单源已核(英译文字稿,个人判断)

### (5) 主要一手 URL

- https://epoch.ai/data-insights/hyperscalers-control-most-compute
- https://epoch.ai/data-insights/largest-data-center-compute
- https://epoch.ai/data/data-centers ;https://epoch.ai/data/data_centers/data_centers.csv ;https://epoch.ai/data/frontier-data-centers
- https://epoch.ai/data/all_ai_models.csv
- https://ifp.org/wp-content/uploads/Should-the-US-Sell-Hopper-Chips-to-China-IFP.pdf ;https://ifp.org/should-the-us-sell-hopper-chips-to-china/
- https://epoch.ai/publications/huaweis-roadmap-to-2031
- https://www.chinatalk.media/p/the-all-star-chinese-ai-conversation

---

## G25 · ECI 前沿斜率、谁还在前沿、算法效率、"追随者便宜"

票型:CORRECTED / CORRECTED / CORRECTED(另吸收 round3 R1 的重拟合漂移限定)

### (1) 锁定表述

- **前沿斜率(自算,须标注)**:这是作者用 Epoch ECI(2026-10-12 下载)的数据自己算的。对 2024 年以来的 21 个前沿纪录点(从 GPT-4 Turbo 126.46 到 Claude Opus 5.5 167.33)做 OLS 拟合,斜率约为每年 **15.6 ECI**(复算 15.59)。按这个速度,10 ECI 约等于 **7.7 个月**。
  - 斜率对起点敏感:从 2023 年起算约为 20.8;用逐月滚动最大值拟合,2024 年以来为 15.71,2025 年以来为 14.72。
  - 如果粗略假设前沿算力每年增长 5 倍,并把 ECI 进步全部归因于算力,7.7 个月约相当于 **2.8 倍**算力。这一换算是作者自己的假设,不是 Epoch 的结论,它把算法和后训练的贡献都折进了算力。
  - 与训练算力差距对照:GPT-6 Astra 对 Kimi K3 约 50 倍,计入 CI 后为 25–100 倍,在每年 5 倍的速度下约相当于 2.4 年(区间约 2.0–2.9 年)。K3 的算力是 speculative。GPT-6 Astra(ECI 166.45)并不是 ECI 前沿模型,前沿模型 Opus 5.5 的训练算力未知。如果改用 DeepSeek-V4-Pro 对比,差距约为 100 倍,约 2.9 年。
  - ECI 每次更新数据都会重拟合。round3 发现,同一对模型仅因重拟合,分差就漂移了约 3 点,而且漂移集中在闭源顶端。因此所有数值只属于这一个快照。
- **Meta 与 xAI**:Meta 的最佳模型 Muse Spark 1.3 为 156.75,xAI 的 Grok 4.6 为 156.44,比前沿 Claude Opus 5.5(167.33)分别低 **10.6** 和 **10.9**。它们与 Kimi K3(157.45)、Gemini 3.7 Flash(157.27,Google 已打分模型中最高)、Qwen 3.8 Max(156.41)处于同一档。
- **贴近前沿的实验室数**:只看已有 ECI 分数的模型,以距前沿 6 ECI 以内为门槛,用当前这次 ECI 拟合做回溯计算:
  - 2025-09-30 有 5 家:OpenAI、Anthropic(3.16)、xAI(3.56)、Google(4.68)、DeepSeek(5.0);Qwen 为 6.15,刚好在门槛外。
  - 2026-06-30 和 2026-09-30 只有 Anthropic 和 OpenAI 两家。2026-06 时 Google 落后 7.3;如果门槛放到 8 点,2026-06 为 3 家。
  - Google 的 Gemini 4 Argon 于 2026-09-30 发布,仅限量开放,尚未打分。有报道称它接近前沿(Google 自称与 Astra、Opus 相当)。所以"只剩两家"是暂定结论,可能被推翻。
- **算法效率**:Ho 等(2024)估计,2012–2023 年间,在语言模型预训练(WikiText/PTB 困惑度)上,达到某一固定性能所需的算力大约每 **8 个月**减半(95% CI 约 5–14 个月)。
- **参照依赖**:Gundlach 等(arXiv 2511.21622)用小规模消融只能解释被引用的 22,000 倍(这是 Ho 等的数字,非本文自测)中**不到 10 倍**。在本文实测的 21,400 倍中,LSTM→Transformer(846 倍)和 Kaplan→Chinchilla 再平衡(约 10 倍)这两项依赖规模的创新,外推到 2025 年算力前沿时合计占 **91%**。作者因此认为,算法效率的度量强烈依赖参照点。
- **追随者成本(条件句)**:Epoch Gradient Updates(Denain 与 Wu,2026-03-23,评论性质)写道,OpenAI 2024 年 R&D 算力约 **50 亿美元**,这是报道数字,出自 Epoch 2025-10-10 的 data insight,不是 Epoch 的实测。最终训练运行只占其中 **9.6%**,MiniMax 为 22.6%,Z.ai 为 12.3%。作者的推论是:如果大部分支出是探索而不是执行,追随者从前沿学到有效做法后,就能以一小部分成本复现。但作者也说只有三个数据点,证据不确定,而且 Z.ai 与这一追赶预测不符。

### (2) 英文原文引语(逐字)

- Ho et al.: "the compute required to reach a set performance threshold has halved approximately every 8 months, with a 95% confidence interval of around 5 to 14 months"
- Gundlach et al.: "Algorithms have been estimated to increase AI training FLOP efficiency by a factor of 22,000 between 2012 and 2023 [Ho et al., 2024]... we are able to account for less than 10× of these gains"
- Gundlach et al.: "measures of algorithmic efficiency are strongly reference-dependent"
- Gundlach et al.: "Together, these account for 91% of total efficiency gains when extrapolating to the 2025 compute frontier"
- Epoch GU: "OpenAI spent $5 billion on R&D compute in 2024"
- Epoch GU: "9.6% for OpenAI, 22.6% for MiniMax, and 12.3% for Z.ai"
- Epoch GU: "if most of the spending is exploration rather than execution, then a competitor who learns what works from the frontier could replicate the results for a fraction of the original cost."
- Epoch GU: "with only three data points, the evidence remains inconclusive"

### (3) 判死 / 禁用清单

1. 「Meta、xAI 都约低 10.5」→ 改为 10.6 和 10.9(三票复算一致)。
2. 「10 ECI ≈ 2.8 倍前沿算力」当作 Epoch 结论或事实 → 禁用。这是作者自己的换算,假设算力每年增长 5 倍且进步全部来自算力。
3. 「与前沿模型的算力差约 50 倍」→ 禁用这种措辞。50 倍是 GPT-6 Astra 对 Kimi K3(K3 为 speculative,CI 下为 25–100 倍),而 Astra 不是 ECI 前沿模型。
4. 「只剩两家在前沿」不加限定 → 禁用。必须注明"只算已打分模型、以 6 点为门槛、用当前拟合回溯",并说明 Gemini 4 Argon 未打分。
5. 「91% 的效率提升来自依赖规模的创新」(泛指)→ 禁用。91% 只指两项具体创新,外推到 2025 年前沿,分母是实测的 21,400 倍。
6. 把 22,000 倍写成 Gundlach 等自己测的 → 禁用,这是 Ho 等的数字。
7. 「Epoch 认为追随者能以一小部分成本复现」写成既定结论 → 禁用。原文是条件句,只有 n=3,作者自认 inconclusive。
8. 把 50 亿美元写成 Epoch 实测 → 禁用。这是报道数字或 Epoch 引用的估计。
9. 跨 ECI 版本比较斜率或分差(例如拿 5 月发布的数字对比 10 月复算的数字)→ 禁用,重拟合漂移约 3 点(round3)。

### (4) 证据分级

- 斜率 15.6/年、7.7 个月、10.6/10.9、5→2→2 家:单源已核(三票分别复算 Epoch CSV;换算部分是作者假设)
- 2.8 倍 / 2.4 年:未验证(属于推导,依赖假设)
- Ho 等 8 个月:单源已核
- Gundlach 等 <10 倍、91%、参照依赖:单源已核
- Epoch GU 的 9.6% 等:单源已核;"复现只需一小部分成本"为方向存争(条件句,n=3)
- 50 亿美元:厂商/报道口径

### (5) 主要一手 URL

- https://epoch.ai/data/benchmark_data.zip(epoch_capabilities_index/eci_scores.csv)
- https://epoch.ai/data/all_ai_models.csv
- https://arxiv.org/abs/2403.05812
- https://arxiv.org/abs/2511.21622
- https://epoch.ai/gradient-updates/r-and-d-vs-training-compute ;https://epoch.ai/data-insights/openai-compute-spend
- https://epoch.ai/data-insights/open-closed-eci-gap(round3 背景)

---

## G26 · 推理价格暴跌 vs 前沿运行成本上升、测试时算力、RL 扩展效率

票型:CORRECTED / CORRECTED / CORRECTED

### (1) 锁定表述

- **单位性能成本下降**:Epoch《The plunging price of thought》(Emberson 与 Roodman,2026-09-22;09-23 修订,补充了关于"思考的价格"这一概念模糊性的说明)覆盖五个主要基准(数学、硬科学、技巧类游戏)。结论是,自 2023 年以来,达到某一固定性能水平的成本每季度下降约 **47%**,约合每年 **13 倍**(复算 0.53⁴ 约为 12.7 倍)。
  - 性能水平刚成为 SOTA 时,成本每季度下降约 **66%**(约每年 75 倍);两年后降速减半,为每季度 **32%**(约每年 4.7 倍)。这一"SOTA 溢价"模式只出现在五个基准中的 **3 个**上。
  - 在图中 8 条轨迹里,只有 1 条的"第二个点"来自开放权重模型(QwQ-32B,AIME 25% 水平)。作者同时补充,闭源模型之间的竞争可能仍受到开源压力的推动。
- **固定性能变便宜,前沿运行变贵**:Gundlach、Lynch、Mertens、Thompson(MIT FutureTech,《The Price of Progress》,arXiv 2511.23455)发现,在知识、推理、数学和软件工程基准上,达到固定性能的价格每年下降约 **5–10 倍**。但在 GPQA-Diamond、SWE-bench Verified、AIME 上运行表现最好的前沿模型,其成本每年上升 **3–18 倍**,原因是模型更大、推理需求更长。这是跑基准的总成本,不是每 token 单价。同一摘要还估计算法效率约每年提升 3 倍。
- **测试时算力**:Snell 等(2024,PaLM 2-S*,MATH)发现,在 FLOPs 对齐的比较下,对于小模型已经有一定成功率的问题,测试时算力可以胜过一个大 **14 倍**的模型。这一优势取决于推理负载与预训练负载之比,适用于易题和中等题;在最难的题上,预训练算力更有效。
- **RL 扩展效率**:Toby Ord 根据 OpenAI 公开的 o1/o3(及 GPT-5)图表粗略估计,RL 要扩大 10 倍,才能换来推理算力扩大 3 倍的同等提升。这是他读图得出的启发式估计,不是对照实验,也未经同行评审或独立复现。

### (2) 英文原文引语(逐字)

- Epoch: "fallen about 47% per quarter since 2023, or 13× per year"
- Epoch: "cost falls 66% per quarter (75× per year) for performance that has just debuted as SOTA. Two years later, prices fall half as fast, at 32% per quarter (4.7× per year)"
- Epoch: "We see this pattern on three of our five main benchmarks"
- Epoch: "In only one of the eight traces in the figure does the model responsible for the second dot have open weights (QwQ-32B for 25% performance on AIME)."
- Gundlach et al.: "the price for a given level of benchmark performance has decreased remarkably fast, around 5× to 10× per year, for frontier models on knowledge, reasoning, math, and software engineering benchmarks"
- Gundlach et al.: "the price of running frontier models is rising between 3× to 18× per year due to bigger models and larger reasoning demands"
- Snell et al.: "in a FLOPs-matched evaluation, we find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14× larger model"
  - 冲突说明:票 1 和票 3 记作 "14×",票 2 记作 "14x",其余文字一致。
- Ord: "a 10x scaling of RL is required to get the same performance boost as a 3x scaling of inference"

### (3) 判死 / 禁用清单

1. 「Cottier et al.《The Price of Progress》」→ **判死(归属错误)**。作者是 Gundlach、Lynch、Mertens、Thompson(MIT FutureTech),Cottier 只是在文中被引用。票 2 和票 3 一手核实;票 1 漏判,按最严规则以判死为准。数字和引语本身无误。
2. 把「3–18 倍/年」写成每 token 单价上涨 → 禁用。它指在三个基准上运行前沿模型的成本。
3. 「刚成 SOTA 时降价最快」写成普遍规律 → 禁用,只在 5 个基准中的 3 个上成立。
4. 「开源推动了降价」或反过来的「降价与开源无关」写成定论 → 禁用。原文只是"图中 8 条轨迹里只有 1 条",作者还加了"可能仍受开源压力推动"的保留。
5. 去掉 Snell 的限定条件(FLOPs 对齐、小模型已有一定成功率),写成"小模型加推理可以打败 14 倍大的模型" → 禁用。
6. 把 Ord 的 10 倍对 3 倍写成实验结论 → 禁用。

### (4) 证据分级

- Epoch 的 47% / 13 倍 / 66% / 32% / 8 条轨迹中 1 条:单源已核
- Gundlach 等的 5–10 倍与 3–18 倍:单源已核
- Snell 的 14 倍:单源已核(带限定)
- Ord 的 10 倍对 3 倍:未验证(个人启发式估计)

### (5) 主要一手 URL

- https://epoch.ai/publications/the-plunging-price-of-thought
- https://arxiv.org/abs/2511.23455
- https://arxiv.org/abs/2408.03314
- https://www.tobyord.com/writing/how-well-does-rl-scale

---

## G27 · "没有护城河"备忘录、人才流动、DeepMind 论文禁发期、Meta Muse Spark 闭源

票型:CORRECTED / CORRECTED / CORRECTED

### (1) 锁定表述

- **"没有护城河"**:2023-05-04,SemiAnalysis(Dylan Patel 与 Afzal Ahmad)发布了一份经 Discord 泄露的内部备忘录,作者是 Google 内部的一名研究员。文中说,开源与 Google 的差距"正在惊人地快速收窄"。这只代表一名研究员个人的看法,不是 Google 的官方立场。
- **人才流动(SignalFire,2025-05-20,专有人才数据)**:
  - 工程师从 OpenAI 跳槽到 Anthropic 的可能性,是反方向的 **8 倍**;从 DeepMind 到 Anthropic 的比例接近 **11:1**。
  - 两年留存率(入职满 2 年的员工在第二年末仍在职的比例):Anthropic **80%**,DeepMind **78%**,OpenAI **67%**,Meta **64%**。Meta 的 64% 是全公司(FAANG 口径)的数字,不是 Meta 的 AI 实验室。
  - 数据是 2025 年的,早于 Meta 2025 年中开始的大规模 AI 招聘和 2026 年的人事变动。SignalFire 自己也指出,初创公司人数少、历史短,留存率难以评估。
- **DeepMind 论文禁发期(媒体转述)**:据英国《金融时报》2025 年 4 月报道(消息源为匿名现任和前任员工),DeepMind 对生成式 AI 的"战略性"论文设置了最长六个月的发表禁发期。FT 原文未能一手核实,仅有多家二手报道一致转述。DeepMind 回应称仍在广泛发表论文,保留发表能力。
- **Meta Muse Spark**:Meta 于 2026-04-08 发布 Muse Spark,这是 MSL 的首个模型。发布时只开放 meta.ai 和私有 API 预览,没有发布权重,Epoch 将其列为 API access。Meta 在发布博文中承认,模型在长时程智能体系统和编码工作流上存在性能差距。
  - 时间点限定:后续版本(至 2026-09-02 发布的 1.3)针对上述短板做了改进。Meta 自报在 DeepSWE 上得 75.4,对 Claude Opus 5 的 74.0,未经独立核实。权重仍未开放,开放权重只是"在路线图上"。按 Epoch ECI,Muse Spark 1.3 为 156.75,仍落后前沿约 **10.6** 点。

### (2) 英文原文引语(逐字)

- SemiAnalysis(泄露备忘录): "While our models still hold a slight edge in terms of quality, the gap is closing astonishingly quickly."
- SignalFire: "Engineers are 8 times more likely to leave OpenAI for Anthropic than the reverse. From DeepMind, the ratio is nearly 11:1"
- SignalFire: "An impressive 80% of employees hired at least 2 years ago at Anthropic were still at the company at the end of their second year... DeepMind follows closely at 78%, while OpenAI's retention trails at 67% but remains on par with large FAANG companies like Meta (64%)."
- Meta(2026-04-08 博文): "We continue to invest in areas with current performance gaps, such as long-horizon agentic systems and coding workflows."
  - 冲突说明:票 1 和票 3 从一手博文核到的是 "such as"。票 2 只看到二手转述,作 "specifically"。以一手的 "such as" 为准。
- FT 的禁发期原句:无一手逐字,不得加引号。

### (3) 判死 / 禁用清单

1. 「Google 的备忘录 / Google 承认没有护城河」→ 禁用。那是一名匿名研究员的泄露文件,不是公司立场。
2. 「Meta AI 实验室留存率 64%」→ 禁用。64% 是 Meta 全公司口径。
3. 不注明年份就用 SignalFire 的数字说明当前(2026)的人才格局 → 禁用,数据是 2025 年的,早于 MSL 的招聘潮。
4. 「DeepMind 实行六个月论文禁发」写成已证实事实 → 禁用。只能写"据 FT 报道(匿名消息源,媒体转述)",并附上 DeepMind 的回应。
5. 「Meta 承认在智能体和编码上有差距」不注时间点,当作 2026-10 的现状 → 禁用。必须注明这是 2026-04 发布时的说法,并补充 1.3 之后的进展和 ECI 仍约落后 10.6 的事实。
6. 「Meta 宣布闭源」→ 禁用这种措辞。博文没有明说"闭源",只能写"未发布权重 / 仅 API 预览"。
7. 引用 Meta 自报的 DeepSWE 75.4 对 74.0 当作已追平 → 禁用,未经独立核实。
8. Muse Spark 中间版本号:票 1 写作 1.1–1.3,票 2 写作 1.1(07-09)和 1.3(09-02),票 3 写作 1.2(2026-08)和 1.3(09-02),三票冲突。只写已一致的"1.3(2026-09-02)",不写 1.1 或 1.2 的具体日期。

### (4) 证据分级

- 泄露备忘录引语:单源已核(个人观点)
- SignalFire 的 8 倍、11:1、各家留存率:单源已核(专有数据,2025 年,样本小)
- DeepMind 六个月禁发期:未验证(FT 一手未见,只有媒体转述)
- Muse Spark 未发布权重、发布时承认差距:单源已核(Meta 博文,厂商口径)
- 1.3 的 ECI 156.75:单源已核(Epoch)
- DeepSWE 75.4 对 74.0:厂商口径(未核)

### (5) 主要一手 URL

- https://newsletter.semianalysis.com/p/google-we-have-no-moat-and-neither
- https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025
- https://ai.meta.com/blog/introducing-muse-spark-msl/
- FT 原文未取得;二手转述:https://tech.slashdot.org/story/25/04/01/1648250
- https://epoch.ai/data/benchmark_data.zip(Muse Spark 1.3 的 ECI)

