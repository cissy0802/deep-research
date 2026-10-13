# LOCKIN-compute — 输入侧锁定(算力/资本/RL/人才)

截至 2026-10-12 调研。原始数据: Epoch AI all_ai_models.csv (下载于 2026-10-12, 3626 行, 最新发布日期 2026-09-30)。

## 自算 C1: Epoch 数据库中 >=1e25 / >=1e26 FLOP 模型
方法: curl https://epoch.ai/data/all_ai_models.csv, 过滤 Training compute (FLOP) >= 阈值。
- >=1e25: 25 个 (2023:4, 2024:6, 2025:9, 2026:6); >=1e26: 仅 4 个 (Grok 3 3.5e26, GPT-4.5 3.8e26, Grok 4 5e26 speculative, GPT-6 Astra 1e27 likely, 2026-09-03)。
- 口径问题: 2026 年 Anthropic/Google/OpenAI 大部分前沿模型(Claude Opus 5/5.5, Gemini 3.x/4, GPT-5.5/5.6)训练算力字段为空 —— 闭源不披露, 计数严重低估前沿; 中国开源模型因披露 active params/tokens 反而有估计。
- GPT-6 Astra 注释原文: "trained on at least 100,000 GB200s in Abilene, Texas ... This suggests around 1e27 FLOP ... yielding a CI of ~[5e26, 2e27] FLOP."
- 最大开源权重估计: Kimi K3 2.0e25 (speculative, 2026-07-16), DeepSeek-V4-Pro 9.7e24 (2026-04-24), Qwen3.8-2.4T-A95B 无估计。=> 最大闭源(已估) / 最大开源(已估) ≈ 1e27/2e25 ≈ 50× (粗略, 区间 25-100×)。

## 自算 C2: Epoch Frontier Data Centers (https://epoch.ai/data/data_centers/data_centers.csv, 下载 2026-10-12, 94 站点)
- 当前合计 ~14.6M H100e; 国家: 美国 86.3%, 马来西亚 8.8%(含 ByteDance MY06), 中国 2.2%(仅 4 站点:VNET乌兰察布/华为和林格尔/华为芜湖/阿里张北)。
- 按 owner: Google 25%, Meta 17%, 未知 12%, Microsoft 11.5%, SpaceXAI 9.6%, Amazon 9.3%, CoreWeave 5%, Oracle 4%。
- 按 user(多用户均分): Meta 2.49M, Google DeepMind 2.32M, OpenAI 2.13M, Anthropic 1.86M, Microsoft 0.85M, SpaceXAI 0.38M, Cursor 0.37M, ByteDance 0.34M, Tencent 0.08M, Alibaba 0.03M。
- >=500k H100e 单站: Colossus 2 (1.11M, 946MW, users Anthropic/Cursor/SpaceXAI), MS Fairwater Atlanta 0.77M, Anthropic-Amazon New Carlisle 0.69M, Google Pryor 0.64M, DayOne Nusajaya(马来西亚) 0.58M, Meta Prometheus 0.54M, Stargate Abilene 0.51M。
- 口径问题: Epoch 靠卫星+许可证, 中国覆盖率显著偏低; 但前沿单站 >=500k H100e 的"玩家"约 5-6 家美国实验室, 是锁定信号。

## 自算 C3: Epoch GPU clusters (旧数据集, 截止 2025-07): 最大集群按首运营年 2022 7.9k → 2023 14.4k → 2024 100k → 2025 276k H100e; 存量美国 79.5%, 中国 7.0%。

## 外部一手(已核)
- Epoch Data Insight 2026-06-11 (Ben Cottier) https://epoch.ai/data-insights/largest-data-center-compute : 最大单体数据中心算力纪录约每 7 个月翻倍(~3.3×/年, 模拟区间 2.3-5.1×); "no data center will have meaningfully greater capacity than Colossus 2 until the second half of 2027"; 数据集约覆盖全球 AI 算力 26% (截至 2026-03-31), 偏美国。注意与 CSV 当前值不一致(Insight 称 Meta Prometheus 7.6e5 H100e @2026-05-28; CSV 当前 5.36e5)。
- Epoch trends dashboard (Updated Feb. 5, 2026) https://epoch.ai/data/trends : "Training compute for frontier language models has been growing at 5× per year since 2020"; "The cost to train frontier language models has increased by 3.5×/year since 2020"; "The total computing power of the stock of AI chips is growing at a rate of 3.4×/year."
- Epoch model counts (2025-05-30) https://epoch.ai/tools/model-counts : "Model counts rapidly grow from 10 above 1e26 FLOP by 2026, to over 200 by 2030." 首个 >1e26 为 Grok-3 (2025-02)。
- Ho et al. 2024 arXiv:2403.05812: "the compute required to reach a set performance threshold has halved approximately every 8 months" (95% CI 5-14 months)。
- Gundlach et al. (MIT FutureTech) arXiv:2511.21622 (ICML 2026): 小规模消融只解释 <10×(文献再 <10×), 远小于 22,000×; "measures of algorithmic efficiency are strongly reference-dependent"; Transformer 与 Chinchilla 再平衡两项尺度依赖创新占外推到 2025 前沿时 91% 效率增益 → 算法进步偏向大算力玩家(反"追赶者靠效率追平"叙事)。
- Toby Ord 2025-10-20 https://tobyord.com/writing/how-well-does-rl-scale : "a 10x scaling of RL is required to get the same performance boost as a 3x scaling of inference"。(从业者博客)
- Epoch (Venkat Somala) "Will Huawei catch up to Nvidia by 2030?" 2026-09-04/更新 09-24 https://epoch.ai/publications/huaweis-roadmap-to-2031 : "Huawei will produce less than 4% of Nvidia's compute output this year."; Ascend 950 约 H100 一半性能; "HBM is the key bottleneck"。
- IFP (Khan, Burga, Fist, Adamson) 2025-12-07 H200 memo: "With no AI chip exports to China and no smuggling, we estimate the US would hold a 21–49x advantage in 2026-produced AI compute"; 无限制 H200 出口 → 6.7x-1.2x; 中国 AI 芯片产量 "only 1–4% of US production in 2025 and 1–2% in 2026"。
- Epoch Data Insight 2026-01-02 https://epoch.ai/data-insights/us-vs-china-eci : 中国模型 ECI 平均落后 7 个月(min 4, max 14); "Since 2023, every model at the frontier of AI capabilities ... has been developed in the United States."
- Epoch Data Insight 2026-05-29 https://epoch.ai/data-insights/open-closed-eci-gap : "Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of four months"; "The average ECI gap was 8 points, similar to the gap between GPT-5 and GPT-5.5."
- Anthropic 2026-02-23 https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks : DeepSeek/Moonshot/MiniMax "16 million exchanges with Claude through approximately 24,000 fraudulent accounts"; "competitors can use it to acquire powerful capabilities from other labs in a fraction of the time"; "Distillation attacks therefore reinforce the rationale for export controls." (厂商自报, 被指控方未回应)
- NIST CAISI 2026-05 https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro : DeepSeek V4 Pro 约落后美国前沿 8 个月(与 GPT-5 相当); 方法受批评(含私有基准)。

## 自算 C4: Epoch ECI (https://epoch.ai/data/eci_scores.csv, 下载 2026-10-12, 274 模型, 最新 2026-09-29)
方法: 每季度末取已发布模型的 ECI 最大值为前沿; 最佳开源=Accessibility group=Open weights 最大值; "追平月数"=季度末 - 前沿首次达到该开源分数的日期。
| 季度末 | 前沿 | 最佳开源 | 分差 | 追平月数(季末口径) | 前沿 6 分内的机构数 |
| 2024-12 | o1 141.9 | DeepSeek-V3 132.3 | 9.6 | 3.6 | 1 |
| 2025-03 | Gemini 2.5 Pro 144.2 | DeepSeek-R1 139.0 | 5.2 | 3.4 | 4 |
| 2025-06 | o3-pro 147.4 | R1-0528 141.3 | 6.1 | 6.4 | 3 |
| 2025-09 | GPT-5 150.0 | V3.2-Exp 145.0 | 5.0 | 5.5 | 5 (OpenAI/Anthropic/xAI/GDM/DeepSeek) |
| 2025-12 | GPT-5.2 Pro 155.4 | V3.2 146.3 | 9.1 | 8.5 | 3 |
| 2026-03 | GPT-5.4 Pro 158.9 | Kimi K2.5 148.0 | 10.9 | 7.8 | 3 |
| 2026-06 | GPT-5.5 Pro 162.1 | GLM-5.2 151.8 | 10.3 | 7.4 | 2 (OpenAI, Anthropic) |
| 2026-09 | Claude Opus 5.5 167.3 (CI 164.1-171.7) | Kimi K3 157.5 (CI 155.2-160.0) | 9.9 | 6.9 (发布时口径 4.4) | 2 (Anthropic 167.3, OpenAI 166.4) |
- 输入≠输出: Meta (按 user 拥有最多前沿数据中心算力 ~2.5M H100e) 最佳 Muse Spark 1.3 = 156.75; SpaceXAI/xAI (Colossus 2 owner) 最佳 Grok 4.6 = 156.44; 均比前沿低 ~10.5 分, 与最佳中国开源 Kimi K3 (157.45) 同档。=> 算力是必要非充分条件。
- 口径问题: Google 最新 Pro 级(Gemini 4 Argon, 2026-09-30 limited access)未被 ECI 打分, Google 2026-02 后仅有 Flash 打分 → "2 家"可能低估; ECI 分差非线性; 季末口径 vs 发布时口径相差 2-3 个月。

## 外部一手(续)
- Epoch Data Insight 2026-04-14 https://epoch.ai/data-insights/hyperscalers-control-most-compute : Amazon/Google/Meta/Microsoft/Oracle "collectively hold an estimated 71% of the world's cumulative AI compute as of Q4 2025" "up from 63% in Q1 2024"。(集中度上升 = 锁定信号)
- Epoch Gradient Updates (Josh You) 2026-05-20 https://epoch.ai/gradient-updates/frontier-labs-dont-use-most-ai-compute : 2025 年底 OpenAI ~1.7M H100e, Anthropic >1M, xAI 0.6-0.7M, Meta 总 ~2.3M; 五家前沿开发者合计 "probably still under half of the world total"。
- Epoch Gradient Updates (Denain & Wu) 2026-03-23 https://epoch.ai/gradient-updates/r-and-d-vs-training-compute : OpenAI 2024 R&D 算力 ~$5B, 最终训练 ~9.6%; MiniMax 22.6%, Z.ai 12.3%; "a competitor who learns what works from the frontier could replicate the results for a fraction of the original cost" (追随者优势 → 趋同力), 但三点数据不确定。
- Epoch Gradient Updates (Denain & Barber) 2026-01-12 https://epoch.ai/gradient-updates/state-of-rl-envs : 引 The Information "Anthropic had discussed spending over $1 billion on RL environments"; "compute spending will still dwarf RL environment spending"; "exclusive deals are roughly 4-5x more expensive"; 内部自建增多。
- Cursor 2026-03-26 https://cursor.com/en/blog/real-time-rl-for-composer : 用户交互实时 RL, "about five hours" 一轮; A/B: edit persists +2.28%, dissatisfied follow-up -3.13%; "real environments and real users, eliminating this source of modeling uncertainty"。(厂商自报; Composer 2.5 基于 Kimi K2.5 开源底座 → 使用数据飞轮不专属前沿实验室)
- Ege Erdil (Epoch) 2024-12-06 https://epoch.ai/gradient-updates/us-export-controls-china-ai : 出口管制给美国 "a hardware lead of around 4 years when it comes to training frontier models" 但 "essentially no lead when it comes to serving"。
- Snell et al. arXiv:2408.03314 (2024-08, ICLR 2025): "test-time compute can be used to outperform a 14x larger model" (FLOPs-matched, 仅在小模型有非平凡成功率的题上); 效果 "critically varies depending on the difficulty of the prompt"。
- Epoch (Emberson & Roodman) 2026-09-22 https://epoch.ai/publications/the-plunging-price-of-thought : 同等性能成本每季 -47% (13×/年) since 2023; SOTA 时 -66%/季, 两年后 -32%/季; "In only one of the eight traces in the figure does the model responsible for the second dot have open weights"。
- Gundlach? 否 —— "The Price of Progress" arXiv:2511.23455 (2025-11): 同等基准价格每年降 5-10×; 算法效率 ~3×/年; "the price of running frontier models is rising between 3× to 18× per year"。
- SignalFire 2025-05-20 https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025 : 两年留存 Anthropic 80%, DeepMind 78%, OpenAI 67%, Meta 64%; "Engineers are 8 times more likely to leave OpenAI for Anthropic than the reverse"; DeepMind→Anthropic ~11:1。(VC 分析机构)
- FT 2025-04 (媒体转述): DeepMind 对战略论文设 6 个月禁发期; 研究员 "I cannot imagine us putting out the transformer papers for general use now"。
- Google 内部备忘录 (SemiAnalysis 刊出 2023-05-04) https://newsletter.semianalysis.com/p/google-we-have-no-moat-and-neither : 标题 "We Have No Moat, And Neither Does OpenAI"; "the gap is closing astonishingly quickly"; "Large models aren't more capable in the long run if we can iterate faster on small models"。→ 2026 数据显示: 开源仍落后 4-7 个月且分差未收窄, 备忘录"小模型快迭代必胜"的预测未兑现, 但"开源紧随"成立。
- 资本开支(platformonomics 2026-07 汇总财报原话; 分析博客): Amazon "approximately $220 billion in cash CapEx in 2026"; Google "$195‑205 billion"; Meta "$130-145 billion"; Microsoft ~$175B(租赁口径调整, 原口径 $190B); 合计 >$735B。Goldman(经 Al Jazeera 2026-09-24 转述): 阿里/腾讯/百度/字节 2026 合计约 $102B vs 美国 hyperscaler ~$764B。

## 外部一手(再续)
- Epoch Data Insight (2025-08) https://epoch.ai/data-insights/consumer-gpu-model-gap : "Frontier AI performance becomes accessible on consumer hardware within a year" (单张消费级 GPU 可跑的开源模型平均落后 6-12 个月)。
- ChinaTalk 译 AGI-Next (2026-01-10, 刊 01-13) https://www.chinatalk.media/p/the-all-star-chinese-ai-conversation : 林俊旸 "U.S. compute may overall exceed ours by one to two orders of magnitude"; "just fulfilling delivery requirements already consumes the vast majority of our compute"; 3-5 年内领先者为中国公司概率 "I think it's 20%" "already very optimistic"。
- xAI Grok 4 博客 (2025-07-09) https://x.ai/blog/grok-4 : 在 200k GPU Colossus 上 "reinforcement learning at pretraining scale", "over an order of magnitude more compute than had been used previously"。(厂商自报) → 但 2026-09 Grok 4.7 ECI 153.5、Grok 4.6 156.4, 落后前沿 ~11-14 分: RL 规模化本身不是护城河。
- Altman 2025-10-28 直播 (媒体转述, Reuters/PYMNTS): ~30 GW、约 $1.4T 总拥有成本的算力承诺。Anthropic 2026-04 Google/Broadcom 多 GW TPU (Broadcom 披露 ~3.5GW 自 2027 起)。(媒体/厂商)
- Meta Muse Spark (2026-04-08) 首个 MSL 模型, 闭源; Meta 自承在 "long-horizon agentic systems and coding workflows" 存在差距 (媒体转述 Meta 博客)。

## 自算 C5: 输入差距 → 输出差距的换算
- ECI 前沿纪录 2024-01 起线性拟合斜率 ≈ 15.6 分/年 (21 个纪录点)。=> 10 分 ECI 差 ≈ 7.7 个月 ≈ 前沿训练算力增长(5×/年)下的 ~2.8× 算力。
- 而已估训练算力: 最大闭源 ~1e27 (GPT-6 Astra) vs 最大开源 ~2e25 (Kimi K3) ≈ 50× ≈ 前沿 2.4 年的算力增长; IFP: 2026 新增算力美/中 21-49×; 林俊旸: 1-2 个数量级。
- 结论: 输入侧差距(数十倍) 远大于输出侧差距(~8 个月/10 ECI 分), 追随者的"算力→能力转化率"高得多(蒸馏、复用前沿知识、R&D 只花 ~10% 在最终训练)。但输出侧差距在 2026 不再收窄(分差从 2025 的 ~5 分扩至 ~10 分; 前沿 6 分内机构从 3-5 家降至 2 家)。
- 口径: 训练算力仅指预训练估计, 不含 RL/R&D; GPT-6 Astra 为单点估计 CI 5e26-2e27; ECI 斜率对窗口敏感。

## 综合判断(本线)
1) 输入侧明确在集中: hyperscaler 份额 63%→71%; 单体数据中心纪录 ~3.3×/年; >=500k H100e 单站仅 5 家美国实验室可用; 中国新增算力约美国 1/20-1/50, 华为 <4% Nvidia。
2) 但输入集中并未 1:1 转为能力锁定: 算力第一梯队内部(Meta、xAI)能力落后前沿 ~10 分, 与中国开源同档 → 算力是门槛不是保证。
3) 2026 年出现"前沿两强化"迹象(Anthropic、OpenAI 领先其余 ≥6 ECI 分), 开源/中国差距以分差计扩大、以月数计稳定在 4-8 个月——"追平月数"稳定 + "分差"扩大 = 前沿加速而追随者同速跟进。
4) 反方力量真实存在: 同等性能成本 13×/年下降; 推理时计算让小模型在可解题上追平 14× 大模型; 前沿 R&D 90% 为探索成本, 追随者可省; 蒸馏(Anthropic 指控 1600 万次交互)。
5) 算法进步"每年 3×"可能被高估且偏大算力(Gundlach 2025): 削弱"追随者靠效率追平"论。
