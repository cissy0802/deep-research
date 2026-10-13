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
