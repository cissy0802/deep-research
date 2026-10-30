# R3 反证搜索：R2（GenAI 事故更多靠人发现）

检索日期：2026-10-30。审的是 R2：Yan et al. arXiv 2504.08865，以及 Ranganathan et al. arXiv 2511.07424。

## 结论：单源已核，而且带一个口径警告

- 两篇原文的数字都已逐字核对。
- 但这两篇都出自 Microsoft，用的是 Microsoft 内部的事故数据，所以不算独立的两个来源。
- 没找到任何其他公司或学术团队给出「ML/LLM 服务事故由谁发现」的量化比例。
- 独立来源只有两类定性证据，方向都支持 R2：Anthropic 和 OpenAI 公开的事故复盘。
- 另一篇 Microsoft 论文（Ganatra 2023）在两件事上和 R2 有张力：对照组的基线数字，以及「新服务」的定义。

---

## 一、原文核对

### Yan et al. 2504.08865 v2（HUST/UIUC/Microsoft 等，13 位作者）

- **Table I**：GenAI 事故 38.3% 由人报、61.7% 由 monitor 报；其他服务分别是 13.7% 和 86.3%。
- **「人」的定义**：原文是 "engineers and customers, instead of automated incident monitors"。也就是说，工程师内部报的也算「人报」，不等于「用户先发现」。
- **monitor 误报率**：GenAI 11.0%，其他服务 3.8%。人报的误报率是 6.6% 和 4.8%。
- **样本与口径**：
  - 时间是 2020-06 到 2024-02。
  - 只收 mitigated 或 resolved 的事故。
  - 判定 GenAI 相关，靠 Service 字段或标题关键词。
  - 对照组是「同时段、同标准、同数量」的其他事故，没说是哪些服务。
  - 绝对数被隐藏，只给归一化数值。
- **Table I 用的是哪个数据集**：原文没写明，大概率是全量、全严重度的通用数据集，不是高严重度子集。论文也没给按年份或按严重度拆分的人报比例。
- **作者自己给的解释**：
  - 45.9% 的 GenAI 服务还处在开发或 preview 阶段。
  - monitor 是从其他服务的框架改过来的。
  - 每 100 起 monitor 报的事故里，GenAI 只用到约 25.9 个不同的 monitor，其他服务是 74.4 个。
  - invalid inference（幻觉、答非所问）常由用户报告。
- **内部小矛盾**（不影响 R2，但说明这篇需要谨慎引用）：TTM 正文给的是 1.12 比 0.65，约 1.7 倍；Implications 一节写的是 1.83 倍。

### Ranganathan et al. 2511.07424（三位作者均为 Microsoft Redmond；另有 AIOps'26 workshop 版本）

- **auto-detected 的定义**："alerts fired by health probes/DRI pipelines before customer reporting"。
- **数字**：156 起里 115 起是自动检出，约 74%。剩下 41 起约 26%，原文只说 "not auto-detected"，没有标成客户报。
- **范围**：只看 Sev2 和 Sev2.5（129 + 27 起），时间是 2025 年 4–6 月，对象是一个没具名的 "hyperscale LLM serving system"。
- TTD 只给了定义，没给数值。TTM P75 是 4 月约 32 小时、5 月约 49 小时。

## 二、两篇 Microsoft 论文能不能直接比（38.3% 人报 vs 约 74% 自动）

不能直接比。两篇有五处口径不同：

| 维度 | Yan | Ranganathan |
|---|---|---|
| 时间 | 2020-06 – 2024-02 | 2025-04 – 06 |
| 严重度 | 大概率全严重度 | 只看 Sev2/2.5 |
| 对象 | 所有 GenAI 相关服务（训练、平台、推理） | 一个 LLM serving 系统 |
| 「非自动」的含义 | 工程师或客户手报 | 客户报告之前没有告警 |
| 规模 | 数十万起 | 156 起 |

如果硬拿来对照，约 26% 非自动比 38.3% 人报，方向一致，两者都远高于 Yan 对照组的 13.7%。但这个下降可能来自三种原因，没法区分：服务成熟了、只看高严重度、对象更窄。两篇不矛盾，也不能拿来算「一年进步了多少」。

## 三、独立来源搜索

### 1. 学术研究：用 status page 分析 LLM 服务事故

- **Chu, Talluri, Lu, Iosup（VU Amsterdam，arXiv 2501.12469，ICPE 2025）**：覆盖 OpenAI、Anthropic、Character.AI，数据截止 2024-08-31。
  - 计时从 "investigating" 状态开始，**没有测检测时间，也没测谁先发现**。
  - 原文明确说，分析用户上报数据 "outside the scope of this article"。
  - 只有一个案例给到了 onset：2024-04-10 ChatGPT 事故，故障约 17:30 开始，17:56 开始调查，差约 26 分钟。
  - 结论：不能证实 R2，也不能证伪。
- **FAILS（arXiv 2503.12185）**：同一类 status page 采集框架，指标是 MTTR 和 MTBF，没有检测来源这一维。（只看了摘要层面。）
- **IsDown、devtoollab 这类聚合站**：只数事故条数。devtoollab 自己也承认，条数反映的是发布 status 的政策，不是可靠性。没有用。

### 2. Microsoft 内部的通用云对照：Ganatra et al.「Detection Is Better Than Cure」（ESEC/FSE 2023）

这篇和 R2 同属 Microsoft，所以**不独立**，但它提供了对照基线和成熟度维度，PDF 全文已读。

- **基线**：306 个服务、2022 全年，**96.7% 的事故由 monitor 检出**。这和 Yan 对照组的 86.3%（人报 13.7%）有明显差距。可能是服务集合、严重度或时间窗不同造成的。这说明 Yan 的对照基线本身随口径变化很大，「13.7%」不能当成「成熟云服务」的普适值。
- **漏检原因**：约 950 起漏检事故里，40% 以上是缺 monitor，30% 是 monitor 逻辑错误或缺信号；27% 的漏检事故造成了 outage 或客户影响。
- **成熟度**：preview 阶段的服务，coverage 问题占比在所有生命周期阶段里最高。这支持「新服务覆盖跟不上」。但 In Development 阶段的服务完全没有 coverage 类问题，而 buggy monitor 的比例随服务成熟而**上升**。所以成熟度和检测质量不是简单的单调关系。这是本轮唯一接近「反例」的证据，但它比的是漏检原因的构成，不是检出率。

### 3. 独立公司的公开复盘（定性，方向支持 R2）

- **Anthropic 2025-09 复盘**（三个 bug，2025-08 到 09）：
  - 先有用户报告，早期报告和正常的反馈波动分不开。
  - 原文："The evaluations we ran simply didn't capture the degradation users were reporting"。
  - 上下文路由 bug 从 8 月 5 日引入，到 9 月 4 日才部署修复，约一个月。
  - 改进措施里包括在生产环境上做持续质量评估。
- **OpenAI GPT-4o sycophancy（2025-04-25 上线）**：
  - OpenAI 原帖返回 403，以下信息来自搜索摘要和二手转述，没有逐字核对。
  - 当时没有专门针对 sycophancy 的部署评估；部分专家测试者觉得 "felt off"，但没拦住上线。
  - 问题是上线后由用户和社交媒体暴露的，几天内回滚。
- 这两例都是**质量类退化**，正好对应 Yan 说的 invalid inference 常由用户报告。但它们是个案，不是比例。

### 4. 搜了但没找到的

- **Google**：Papasian & Underwood《How ML Breaks》（OpML 2020）、McGlohon（SREcon21）。只有根因分类，比如约 30% 的 postmortem 是「ML 固有」的，没有检测来源的统计。
- **Meta、阿里、字节、华为**：没找到 LLM 或 ML 推理服务事故按检测来源分的公开统计。公开的多是训练集群故障研究，那里的故障天然靠自动检测，和这个问题不对口，所以没深追。
- **Microsoft Teams 研究**（Ghosh et al., SoCC 2022「How to Fight Production Incidents?」）：只拿到二手摘要，约 17% 的事故缺 monitor 或遥测覆盖。不是 ML 服务，原文没核。
- **厂商调查**：Neubird 2026，1000 多名 SRE，自报 78% 遇到过「没有告警、客户先发现」的事故。这是自报的经历，不是事故比例，也不针对 ML，不可用。
- **反例**（新服务检测率不比成熟服务差）：没找到直接的量化反例。唯一沾边的就是上面 Ganatra 的生命周期构成分析。

## 四、成文时可以怎么说、不能怎么说

**可以说：**
- 「Microsoft 研究者分析自家四年的事故记录后发现，GenAI 相关事故里约 38% 是由人（工程师或客户）而不是监控报出来的，其他云服务只有约 14%。监控触发的告警里，GenAI 的误报率约 11%，其他服务不到 4%。」
- 「作者给的解释是：近半 GenAI 服务还在开发或 preview 阶段，监控是从老服务的框架改过来的，幻觉这类质量问题很难用传统指标捕捉。」
- 「Microsoft 另一个团队 2025 年对一个 LLM 推理服务的研究里，高严重度事故约四分之三在客户报告前就有告警，说明覆盖在追。但两篇口径不同，不能直接相减算进步幅度。」
- 用 Anthropic 和 OpenAI 的复盘做**案例**：质量退化先被用户感知，离线评估没抓到。

**不能说：**
- 不能说「多项研究表明」或「业界普遍」。量化证据只有 Microsoft 一家的数据。
- 不能说「38% 是用户先发现的」。这个「人」包括内部工程师。
- 不能说「LLM 服务的检出率从 62% 升到 74%」或类似的趋势表述。两篇口径不可比。
- 不能把 13.7% 当成「成熟服务」的普适基线。同公司的 Ganatra 给的是 3.3%，基线随口径摆动很大。
- 不能把 status page 研究（Chu et al.）当作检测时间的证据。它的计时从 investigating 开始。
- 「新服务监控跟不上」作为机制解释可以写，但要标成作者的解释或 Ganatra 的 preview 发现。目前没有一项研究直接按服务成熟度对比过检出率。

## 来源
- https://arxiv.org/html/2504.08865v2
- https://arxiv.org/html/2511.07424
- https://arxiv.org/html/2501.12469v1
- https://jonathanmace.github.io/papers/ganatra2023detection.pdf（ESEC/FSE '23）
- https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
- https://openai.com/index/expanding-on-sycophancy/（403，二手摘要）
- https://www.usenix.org/conference/opml20/presentation/papasian
- https://www.microsoft.com/en-us/research/?p=881646（Teams 研究，二手）
