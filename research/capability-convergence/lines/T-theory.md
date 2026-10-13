# T-theory 线(理论与数学)

截至 2026 年 10 月(调研日 2026-10-12)。原文逐字摘引为英文;自算部分写明数据与方法。
自算脚本输入:METR `benchmark_results_1_1.yaml`(https://metr.org/assets/benchmark_results_1_1.yaml)、Arena `lmarena-ai/leaderboard-dataset` text/full parquet(HF,最新发布日 2026-10-08)。

---

## A. 天花板效应与基准饱和

**T01** Ott et al.(同行评审,Nature Communications 2022;arXiv:2203.04592)整理 3765 个 CV/NLP 基准,发现大比例基准很快接近饱和。
> "We curated data for 3765 benchmarks covering the entire domains of computer vision and natural language processing, and show that a large fraction of benchmarks quickly trended towards near-saturation"
URL: https://arxiv.org/abs/2203.04592 · 立场:测量伪影 · 承重

**T02** Ott et al.:饱和基准若继续用会误导——真实进步反映不出来,模型差异更难达到统计显著。这正是"榜首挤在一起≠能力相等"的测量学根据。
> "they see continued use but become misleading measures: actual progress of model capabilities is not properly reflected, statistical significance of differences in model performance is more difficult to achieve"
URL 同上 · 测量伪影 · 承重

**T03** Ott et al. 聚类:1079 条 SOTA 轨迹(654 个基准)中,饱和/停滞簇 378 条("values close to the ceiling of all results are observed very soon");另有"停滞后突然爆发"簇 241 条——即 S 曲线和突发跃迁同时存在。
> "Cluster 2 (378 benchmarks), corresponds to the saturation/stagnation scenario."
口径注意:正文前文写的是"1079 metric trajectories of 654 benchmarks",簇 2 却标注"378 benchmarks",单位前后不一致。
URL 同上 · 中性

**T04** Kiela et al. 2021 Dynabench(NAACL 2021;arXiv:2104.14337):GLUE 一年内饱和;模型在基准上分数很高,却在简单的挑战样例上失败。
> "GLUE saturated within a year" / "contemporary models quickly achieve outstanding performance on benchmark tasks but nonetheless fail on simple challenge examples and falter in real-world scenarios"
URL: https://arxiv.org/abs/2104.14337 · 测量伪影

**T05** Epoch "A Rosetta Stone for AI benchmarks"(2025-12-02,Ho/Denain/Atanasov/Albanie/Shah):分数与能力之间呈 S 形关系,只有处在中段的模型才能拿来比较;多数基准饱和得太快,看不出长期趋势。这就是 IRT 式的天花板论证。
> "We can only compare models when they're in the middle — not too good and not too bad." / "Most benchmarks saturate too quickly to study long-run AI trends."
URL: https://epoch.ai/blog/capabilities-index · 分析机构/一手 · 测量伪影 · 承重

**T06** 自算(IRT/logistic 天花板推导):设两模型的能力差固定为 Δlogit = logit(0.7) − logit(0.5) = 0.847。基线 50% 时分差 20.0 pt;基线 90% 时 5.45 pt;95% 时 2.79 pt;97% 时 1.69 pt;99% 时 0.57 pt。能力差一点没变,分差却被压缩了 35 倍。换成错误率看:97% 对 98.7%,错误率之比是 2.3 倍。
方法:s = σ(θ − b),把同一个 Δθ 加在不同的基线 logit 上。 · 测量伪影 · 承重

**T07** Fluid Benchmarking(Hofmann et al.,COLM 2025,arXiv:2509.11106,AI2):同一道题的信息量取决于模型能力水平。
> "the relative value of benchmark items depends on an LM's capability level, suggesting that evaluation should adapt to each LM"
URL: https://arxiv.org/abs/2509.11106 · 测量伪影

**T08** Akhtar, Reuel et al.,ICML 2026(arXiv:2602.16763,v4 修订于 2026-08-06):60 个 LLM 基准里近一半已饱和,基准越老,饱和率越高;决定抗饱和能力的是专家策划,而不是测试集是否公开。
> "nearly half of our benchmarks exhibit saturation, with rates increasing with age" / "resilience to saturation is impacted by expert-curation, not by public test data"
URL: https://arxiv.org/abs/2602.16763 · 同行评审 · 测量伪影
口径:二手摘要称新老分组饱和率为 42.9% 对 54.5%,且作者说明差异不显著;本条只采用摘要里的原句。

**T09** Stanford HAI AI Index 2026 技术表现章:
> "Evaluations intended to be challenging for years are saturated in months" / "Top model performance is converging" / "shifting competitive pressure toward cost, reliability, and domain-specific performance"
URL: https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance · 分析机构 · 趋同叙事(且同时承认测量饱和)

## B. 可靠性复合与长任务

**T10** 自算:0.95^50 = 7.69%,0.99^50 = 60.50%,0.9^10 = 34.9%。按独立串联模型,50% 成功的步数上限为 H50 = ln0.5/ln p:p = 0.99 时 69 步,0.995 时 138 步,0.999 时 693 步。p→1 时 H ≈ −ln s/(1−p),所以两个模型的长度比约等于两者错误率之比:99% 对 99.5% 看上去只差 0.5 pt,能完成的任务长度却差 2 倍。 · 长任务分化 · 承重

**T11** Sinha et al. 2025(arXiv:2509.09677,预印本):短任务基准会制造"进步放缓"的错觉,单步准确率的微小提升会复合成可完成任务长度的指数级增长;此外存在 self-conditioning(上下文里已有自己的错误时更容易再犯错),这削弱了"步骤错误相互独立"的假设。
> "even marginal gains in single-step accuracy can compound into exponential improvements in the length of tasks a model can successfully complete" / "models become more likely to make mistakes when the context contains their errors from prior turns"
URL: https://arxiv.org/abs/2509.09677 · 长任务分化/测量伪影 · 承重

**T12** Ord 2025(arXiv:2505.05115,2025-05-08):恒定风险率模型下,50% 时长就是半衰期;T80 = ln0.8/ln0.5 · T50 = 0.322 · T50;任务时长翻倍,成功率平方。
> "a constant rate of failing during each minute a human would take to do the task" / "if you double the task duration, you square the success probability" / "an 80% time-horizon would be ln(0.8)/ln(0.5) = 0.322 times as long as the 50% time-horizon"
URL: https://arxiv.org/abs/2505.05115 · 长任务分化 · 承重

**T13** Ord 2025 的反证:人类的生存曲线明显优于恒定风险率,原因可能是人能纠正前面的错误,也可能只是不同能力的人混在一起造成的伪影。
> "this human survival curve seems to be noticeably better than a constant hazard rate" / "(e.g. that the humans were better at correcting earlier failed subtasks)"
URL 同上 · 中性(说明 p^n 模型的边界)

**T14** Ord 2026-02-04 自我修正(采纳 Hamilton 的 Weibull 再分析):AI 的风险率随任务推进而下降,形状参数 k≈0.6,人类约 0.37;各代模型 k 基本不变,进步来自尺度参数 λ。所以超过 50% 时长的任务,成功率比恒定风险率模型预测的好;短于 50% 时长的任务则更差。
> "AI agents probably don't have a constant hazard rate / half-life. Instead their hazard rates systematically decline as the task goes on." / "the human value of k is significantly lower, at about 0.37"
URL: https://tobyord.com/writing/hazard-rates-for-ai-agents-decline · 从业者/研究者博客 · 反 p^n 简化 · 承重

**T15** Kwa et al.(arXiv:2503.14499,v4 修订于 2026-07-10):拟合式为 p = σ((log h − log t)·β),作者自述类比 IRT;80% 时长比 50% 时长短 4–6 倍,倍增期 204 天对 207 天。
> "psuccess (agent, task) = σ((log hagent − log ttask ) · βagent )" / "models' 80% time horizons are 4-6x shorter, suggesting that even models that sometimes succeed on difficult and diverse tasks cannot reliably perform tasks of moderate length"
URL: https://arxiv.org/abs/2503.14499 · 官方/一手 · 长任务 · 承重
推导:T_p = h·((1−p)/p)^{1/β},所以 T50/T80 = 4^{1/β};两模型的 β 不同时,比值会随阈值变化。

**T16** Kwa et al. 关于 S 曲线的警告:饱和型 logistic 的前段看起来和指数几乎一样。
> "the initial part of any saturating logistic function horizon ∼ a · σ(release date + d) looks very similar to an exponential"
URL 同上 · 中性

**T17** 自算(METR TH1.1 yaml,2024 年后发布的 21 个模型):p50/p80 中位数 5.34(范围 4.0–10.3),明显高于恒定风险率预测的 3.11;折算的 Weibull k 中位数 0.68(0.49–0.82),与 Ord 修正后的 k≈0.6 一致。注意:METR 的 p80 是用 log-logistic 拟合推出来的,折算 k 只是映射,不是独立拟合。 · 测量/理论 · 承重

**T18** 自算(TH1.1 yaml):23 个模型上,TH1.1 平均分每高约 7.1 pt,p50 时长约翻一倍(OLS:log2 p50 对 average_score 回归)。配对比较如下。
- Opus 4.6 对 Gemini 3.1 Pro:分差 +1.8 pt,p50 比 1.87×,p80 比 0.78×(排名随阈值反转)。
- Mythos Preview(早期)对 Opus 4.6:+6.3 pt,p50 1.45×,p80 2.66×。
- Mythos 对 GPT-5.4:+10.9 pt,p50 3.06×,p80 3.45×。

结论:分差小可以对应可观的比值,但比值的方向和大小取决于阈值,而且 CI 极宽。 · 长任务分化(弱) · 承重

**T19** METR TH1.1 官方数据文件:Claude Mythos Preview(早期版)p50 = 17.41 h,95% CI 8.48–55.07 h,p80 = 3.10 h;Opus 4.6 p50 = 11.98 h [5.28, 60.56];2023 年以来倍增期 128.7 天 [104.4, 158.0];全时段拼接 187.8 天。"第三方称约 17 小时"与 METR 自己的数据文件一致(METR 公开表述为"至少 16 小时")。TH1.1 只有闭源模型,无法用它算开源对闭源的时长比。
URL: https://metr.org/assets/benchmark_results_1_1.yaml · 官方/一手 · 承重

**T20** METR 2026-03-20 笔记:任务集饱和后,结果对分析选择变敏感;修正一处正则化错误后,近期模型的 p50 最多下调 20%;logistic 对极易任务敏感,容易拟出平缓斜率;右尾没有约束;约 230 个任务覆盖 1 秒到 20+ 小时,没有任何任务超过 30 小时。
> "As METR's time horizon task suite saturates, the results are becoming more sensitive to analysis choices." / "decreased recent models' 50% time horizon results by up to 20%" / "the right hand tail of the curve is not meaningfully constrained"
URL: https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/ · 官方/一手 · 测量伪影 · 承重

**T21** METR 前沿风险报告(2026-05-19):最强智能体基本饱和了 TH1.1,16 小时以上测不准;内部前沿平均比公开前沿领先约 2 个月。
> "The most capable agents we evaluated essentially saturated our Time Horizon 1.1 benchmark" / "The TH 1.1 suite can't reliably measure time horizons above 16 hours" / "internal frontier on average ~2 months ahead of public frontier"
URL: https://metr.org/blog/2026-05-19-frontier-risk-report/ · 官方/一手 · 测量伪影 · 承重

## C. 三种"差距"的换算(自算推导)

**T22** 自算:设追平月数为 L、分差为 Δ、比值为 R。
- 在线性、不饱和的能力尺度上,L = Δ/v,v 为前沿每月增速。
- 在时长尺度上,L = D·log2 R,D 为倍增期。
- 取 D = 4.23 个月(TH1.1 自 2023 年以来),L = 4 个月对应 R≈1.93×;L = 3 个月对应 1.64×。
- 若 L 固定为 4 个月而前沿加速,D 从 7 个月降到 3.5 个月,R 就从 1.49× 升到 2.21×。

所以"追平月数不变"再加上"前沿加速",结果是"比值拉大";反过来,"分差不变"再加上"前沿加速",结果是"月数缩短"。三种定义可以同时给出相反方向。 · 中性 · 承重

**T23** Epoch 2026-05-29:2026 年以来开源平均落后约 4 个月、8 个 ECI 点(90% CI 7–11),此前约 3 个月。判定"已追平"的标准很宽松:在 ≥5% 的 bootstrap 样本中胜出即可。作者自己也承认估计可能低估差距,因为闭源实验室并不总是发布最强模型。按 T22 换算,8 点 ÷ 4 个月意味着前沿约 2 ECI 点/月(粗算)。
> "We find an average ECI gap of 8 points, with a 90% confidence interval of 7 to 11 units." / "Two factors mean that our estimate may tend to understate the true gap between open and closed models."
URL: https://epoch.ai/data-insights/open-closed-eci-gap · 分析机构 · 分化(轻度) · 承重

**T24** Epoch 2025-08-15:能在单张消费级 GPU 上跑的开源模型平均落后前沿 6–12 个月。按基准分:GPQA-Diamond 7.4 个月,MMLU-Pro 7.3,AA Intelligence Index 6.3,LM Arena Elo 12.4。量尺不同,落后月数相差近一倍;作者也提醒小模型可能针对基准做了优化。
URL: https://epoch.ai/data-insights/consumer-gpu-model-gap · 分析机构 · 测量伪影

## D. Elo / Bradley-Terry

**T25** 自算:BT/Elo 胜率 P = 1/(1+10^(−Δ/400))。10 分对应 51.4%,20 分 52.9%,29 分 54.2%,30 分 54.3%,49 分 57.0%,50 分 57.1%,100 分 64.0%,200 分 76.0%,400 分 90.9%。按 2SE 粗算两两样本量 n≈(1/(P−0.5))^2:要分辨 30 分约需 540 票,10 分约需 4800 票。榜首"挤"表示的是在该提示分布上胜率接近 50%,不等于各方面能力相等。 · 测量伪影 · 承重

**T26** Chatbot Arena 论文(Chiang et al. 2024,ICML,arXiv:2403.04132):排名基于 Bradley-Terry;附录 B 给出了排名不一定传递时的非参数 BT 扩展。
> "the statistical model of Bradley & Terry (1952)" / "a nonparametric extension of the Bradley-Terry (BT) model (Bradley & Terry, 1952) to the case where the ranking is not necessarily transitive"
URL: https://arxiv.org/abs/2403.04132 · 同行评审 · 中性

**T27** Leaderboard Illusion(Singh et al.,arXiv:2504.20879,2025-05):私下测试后择优发布(best-of-N)违反 BT 无偏抽样假设,模拟中测 10 个变体可让最高分抬高约 100 分。闭源模型被抽样更多:Google 和 OpenAI 各拿到约 19–20% 的数据,83 个开源模型合计约 29.7%。
> "testing just 10 variants yields a notable increase of approximately 100 points in the maximum score identified" / "proprietary closed models are sampled at higher rates"
URL: https://arxiv.org/abs/2504.20879 · 预印本(作者来自 Cohere,与该榜有竞争利益) · 测量伪影(闭源-开源 Elo 差可能被系统性放大) · 承重

**T28** 自算(Arena text,"overall"类别,不含风格控制;HF leaderboard-dataset):
- 第 1 名与第 10 名的分差:2024-06 为 73,2024-12 为 80,2025-06 为 92,2025-10 为 42,2026-01 为 38,2026-04 为 31,2026-07 为 32,2026-10-08 为 43(第 1 名 gemini-4-argon-high 1534±8.8)。
- 最强闭源对最强开源:2025-10 为 26 分,2026-01 为 35,2026-04 为 33,2026-07 为 38,2026-09-30 为 43,2026-10-08 为 42(对应胜率 56.0%,两者 CI 合成后粗估约 ±13)。最强开源为 mimo-v2.6-pro,排第 9。
- 结论:头部前 10 名在 2025 年中到年底被压缩到 30–45 分,之后没有继续收窄;闭源与开源的 Elo 差自 2025-10 起温和扩大,但幅度和 CI 同一量级。媒体"29 Elo"的口径(是否风格控制、日期)需由 Arena 线核对。 · 分化(轻度)/测量 · 承重

**T29** 自算"稀释模型":设比例 f 的提示对两模型没有区分度(各 50%),其余提示上真实胜率为 q,则观测胜率 P = 0.5f + q(1−f)。q = 0.75(191 Elo)、f = 0.8 时,P = 0.55,只有 35 Elo;f = 0.9 时只有 17 Elo。用户感知饱和(多数日常提示分不出高下)可以在能力差不变的情况下把 Elo 差压到很小。
反证:2026-10-08 在 Arena 子类别里,hard_prompts 的闭源-开源差为 36、expert 为 14、coding 为 16,都不比 overall 的 42 大;反倒是 multi_turn(70)和 creative_writing(65)更大。也就是说,在 Arena 内部,"难题类别差距更大"的预测没有得到支持(子类 CI 更宽)。 · 正反兼有 · 承重

**T30** AI Index 2026:"截至 2026 年 3 月,顶级闭源领先顶级开源 3.3%,2024 年 8 月为 0.5%"(1503 对 1454)。口径问题:Elo 是任意平移的区间尺度,拿绝对值算百分比没有意义。49 分 = 1503 − 1454,49/1503 = 3.26%;同样的差换算成胜率是 57.0%。
> "As of March 2026, the top closed model leads the top open model by 3.3%, up from 0.5% in August 2024."
URL: https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance · 分析机构 · 分化(且口径有误)

## E. 技术扩散与追赶 / 收益递增

**T31** Ho et al. 2024(arXiv:2403.05812,Epoch):达到固定性能阈值所需的算力约每 8 个月减半(95% CI 5–14 个月)。这是"模仿成本随时间下降"的量化基础。
> "the compute required to reach a set performance threshold has halved approximately every 8 months, with a 95% confidence interval of around 5 to 14 months"
URL: https://arxiv.org/abs/2403.05812 · 预印本/一手 · 趋同机制 · 承重

**T32** Scher(MIRI TGT,2025-12-24):用 2023–2025 数据估算"追赶型"算法进步约 60×/年(1.76 个数量级),按中位数为 16×;作者对下一年的预测约 20×,80% CI 为 2–200×,其中加权含主观成分。
> "1.76 orders of magnitude per year, or a ~60× improvement in compute efficiency" / "Looking at the median of the slopes yields 16× or a halving time of 2.9 months."
URL: https://techgov.intelligence.org/blog/catch-up-algorithmic-progress-might-actually-be-60x-per-year · 分析机构 · 趋同机制

**T33** Anthropic 2026-02-23(厂商自报,利益相关):蒸馏让竞争者能以很小比例的时间和成本获得能力,这是 Mansfield 式模仿成本的当代版本;三家实验室约 2.4 万个账号、1600 万+ 次交互;Anthropic 把对方的快速进步部分归因于蒸馏。
> "competitors can use it to acquire powerful capabilities from other labs in a fraction of the time, and at a fraction of the cost, that it would take to develop them independently"
URL: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks · 厂商自报 · 趋同机制(模仿)

**T34** Mansfield, Schwartz & Wagner 1981(Economic Journal 91(364):907-918):48 种产品(化工/制药/电子/机械)的模仿成本平均约为创新成本的 65%,时间约为 70%。只找到二手转述,原文未取得,待核。后续文献给出的模仿/创新成本比在 0.4–0.9 之间。
URL: https://ideas.repec.org/a/ecj/econjl/v91y1981i364p907-18.html · 同行评审(二手转述) · 趋同机制

**T35** Arthur 1989(Economic Journal 99(394):116-131):在收益递增下,偶然的历史事件可以把经济锁定到某条技术路径上。
> "the economy, over time, can become locked-in, by "random" historical events, to a technological path that is not necessarily efficient"
URL: https://ideas.repec.org/a/ecj/econjl/v99y1989i394p116-31.html · 同行评审 · 分化/赢家通吃

**T36** Korinek & Vipra(NBER w33139,2024-11;Economic Policy 2025):基础模型存在显著的规模经济和范围经济,可能导致市场趋向集中,并有"tipping"风险。
> "identifies significant economies of scale and scope" "that may create a tendency towards greater market concentration in the future"
URL: https://www.nber.org/papers/w33139 · 同行评审/工作论文 · 分化

---

## 口径问题清单
1. 百分比化的 Elo(AI Index 的 3.3%)没有意义;应换成胜率或 Elo 差。
2. Arena 存在 overall / style control / 子类别多套榜;媒体"29 Elo"需注明榜单、日期和 CI。我算的 overall 2026-10-08 为 42±~13。
3. METR 的 p50/p80 比值、配对时长比对阈值敏感,也对模型设定(logistic 对 Weibull、正则化)敏感,而 CI 跨好几倍;TH1.1 没有开源模型。
4. Mythos"17 小时"是 METR yaml 的点估计 17.41 h(CI 8.5–55 h),METR 的文字表述是"≥16 h",已越过 TH1.1 的可靠测量上限。
5. Epoch"4 个月"的判定标准(≥5% bootstrap 胜出即算追平)偏宽松,月数偏短;二手称严格占优时约 6 个月,私有基准上 8–10 个月,这两条一手原文未见。
6. 追平月数、分差、比值三者互相换算时依赖前沿速度(T22),前沿加速期结论可能反向。
7. Ott 文中"378"的单位(轨迹还是基准)前后不一致。
8. Mansfield 65%/70% 仅有二手来源。
9. Kwa et al. 有 v1–v4 多个版本,本文所引 207/204 天、4–6 倍出自 v4。
