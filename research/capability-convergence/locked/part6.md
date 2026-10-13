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
