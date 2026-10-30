# CANARY 线：渐进发布与自动 canary 分析（截至 2026 年 10 月）

调研员：CANARY 子线。三段分开：检测(TTD) / 定位(RCA) / 缓解(回滚)。MTTR 不作检测证据。
字段：论断 / 逐字原文 / URL / 日期 / 来源类型 / 承重 / 支持叙事

---

## C01 Gandalf 数据面：8 个月 155 个关键故障，precision 92.4%，「recall 100%」的定义是「没有高影响事故由坏发布引起」
- 论断：Azure Gandalf 在 2018-01 至 2018-11（8 个月）数据面 rollout 中早期捕获 155 个关键故障，precision 92.4%；所谓 100% recall 不是对照人工标注真值，而是以「无 Sev0-2 事故归因于坏发布」作为代理——即漏报只在酿成高影响事故时才被计入，低影响漏报不在分母里。阶段：检测+归因（属于 rollout 关联/归责，不是纯异常检测）。
- 原文："Overall, in an 8-month usage window from Jan. 2018 to Nov. 2018, Gandalf captured 155 critical failures at the early stage of the data-plane rollouts and achieved a precision of 92.4% with 100% recall (no high-impact incidents were caused by bad rollouts)."
- URL：https://www.usenix.org/system/files/nsdi20-paper-li.pdf （Li et al., NSDI 2020）
- 日期：2020-02
- 来源类型：同行评审（但作者均为 Microsoft，自评自家生产系统）
- 承重：是
- 叙事：支持「自动 canary 分析能拦坏发布」，但 recall 口径偏宽

## C02 Gandalf 控制面：1200+ 次 region 级部署，39 次告警 2 次误报、漏 2 次；「99.8% recall」疑似以全部部署为分母
- 论断：控制面 1200+ 次 region 级部署决策，Gandalf 提交 39 个 incident，其中 2 个误报（precision 37/39=94.9%），漏掉 2 个真问题。若按标准定义 recall = 37/(37+2) ≈ 94.9%；论文报告的 99.8% 与 (1200-2)/1200 吻合，疑似分母是全部部署而非全部坏部署——这是交叉口径问题。漏报原因：日志不全；故障组件抛通用 timeout 而非特定错误。
- 原文："For the control plane, Gandalf has made decisions for 1200+ region-level deployments. The precision is 94.9% and recall is 99.8%. Gandalf filed 39 incidents and only 2 of them are false alarms. Meanwhile, Gandalf automatically approved all other region-level deployments and only missed 2 true issues. One false negative occurred because of incomplete logs. The other was due to the faulty component throwing generic timeout exceptions instead of specific errors, which misled Gandalf."
- URL：https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- 日期：2020-02
- 来源类型：同行评审（Microsoft 自评）
- 承重：是
- 叙事：中性偏警示——数字漂亮但分母可疑；漏报源于可观测性缺口

## C03 Gandalf 检测时延：speed layer 约 5 分钟出决策，batch layer 约 3 小时；部署总时长减半以上
- 论断：TTD（从部署到 go/no-go 决策）：流式层约 5 分钟端到端，批处理层约 3 小时（用于潜伏问题）；只看部署前后 1 小时的故障信号，因为「多数灾难性问题在发布后 1 小时内出现」。部署总时长「减半以上」是相对 Gandalf 前人工邮件审批流程（Figure 14），不是检测速度。
- 原文："For each deployment, Gandalf can make decisions in about 5 minutes end-to-end on the speed layer, and in about 3 hours on the batch layer. Gandalf cuts the deployment time for the entire production fleet by more than half (Figure 14)." / "In Azure, most catastrophic issues happen within 1 hour after the rollout. Latent faults occurring after 1 hour will be captured by the batch layer later."
- URL：https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- 日期：2020-02
- 来源类型：同行评审（Microsoft 自评）
- 承重：是
- 叙事：支持「自动判定可在分钟级给出」，同时承认潜伏故障需小时级

## C04 Gandalf：99.2% 可疑 rollout 在进入生产前被拦（Stage/Canary/Pilot），误报集中在 Stage/Canary
- 论断：数据面被判可疑的 rollout 中 99.2% 在 Stage/Canary/Pilot 阶段被拦，0.8% 在生产早期被拦（分母=被检出的可疑 rollout，不是全部坏 rollout）。误报主要出现在 Stage 与 Canary，因为这些环境噪声更大；潜伏问题会导致错误归责（例：agent 更新误删目录，后来 GuestOS 更新触发故障，被错怪为 GuestOS）。
- 原文："We can see that almost all (99.2%) suspicious rollouts are blocked before reaching production. The rest (0.8%) is blocked in the early stage of production." / "The false positive rate in Stage and Canary is higher compared to other environments because there are higher levels of noisy failure signals in these environments. Latent issues may mislead the Gandalf service."
- URL：https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- 日期：2020-02
- 来源类型：同行评审（Microsoft 自评）
- 承重：是
- 叙事：正反兼有——拦截早，但 canary 环境噪声高、潜伏故障致误归责

## C05 Gandalf 指出局部 watchdog 的盲区：局部轻全局重、潜伏（内存泄漏）、跨组件契约违背；Azure >20% rollout 持续 1000+ 分钟
- 论断：组件级 watchdog 漏掉三类：本地轻微但跨集群/区域严重的问题、发布数小时后才出现的潜伏问题（如内存泄漏）、只在与其他组件交互时出现的问题（跨组件 API 契约违背）。案例 III：网络 agent 在 Canary 中部署后 24–72 小时才 OS 崩溃。案例 I：CRP 团队凭经验认为告警无关，要求绕过 no-go，后续在 Pilot 再次 no-go 才确认回归——人会推翻正确的自动判定。
- 原文："They alone, however, are insufficient in catching production issues that are minor locally but severe globally across clusters and/or regions. They may also miss latent issues such as memory leaks that happen hours after a rollout. Additionally, a component-level watchdog may fail to catch issues that arise only when interacting with other components, e.g., cross-components API contract violations." / "OS crashed during 24 hours to 72 hours after the deployment"
- URL：https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- 日期：2020-02
- 来源类型：同行评审（Microsoft 自评）
- 承重：是（盲区分类）
- 叙事：canary 盲区

## C06 Google CAS：每天评估「数十万」次生产变更，覆盖二进制、配置、数据集
- 论断：Google 中心化 Canary Analysis Service 每天评估数十万次生产变更（不是每天数十万次部署被拦，而是评估次数），对象包括二进制、配置变更和数据集变更。CAS 是被动观察者，自身不做回滚；回滚/暂停由 rollout 工具执行。
- 原文："CAS is used to analyze new versions of binaries, configuration changes, data-set changes, and other production changes. CAS evaluates hundreds of thousands of production changes every day at Google." / "It is a purely passive observer: it never changes any part of the production system."
- URL：https://sre.google/static/pdf/canary_analysis.pdf （Davidovič & Beyer, "Canary Analysis Service", ACM Queue 16(1), 2018；queue.acm.org/detail.cfm?id=3194655 对脚本返回 403，读的是 sre.google 官方 PDF）
- 日期：2018-01/02
- 来源类型：官方一手（Google 工程师撰写，ACM Queue 编辑出版，非同行评审）
- 承重：是（规模）
- 叙事：支持「自动 canary 分析已是大厂标配」

## C07 Google CAS 方法：canary vs control 两组时间序列 + 统计函数 → PASS/FAIL；自动配置可跑「数十个」测试；用相对比较（如 t 检验「增幅不超过 5%」）
- 论断：判定 = canary 组与 control 组时间序列对比，统计检验（有 Student t 检验等，也有模仿人眼判断的自定义启发式）；自动配置时可能跑数十个参数不同的测试，并由 model server 学习「此类变更通常表现」，对「预期内失败」忽略。局限：纯相对比较，在指标通常为 0 或相对变化大但绝对量小时表现「极差」。
- 原文："Some tests (such as Student's t-test) have a clear statistical origin, while others contain custom heuristics that attempt to mimic how a human would evaluate two" / "If the user opts for autoconfiguration, however, the evaluator may run dozens of tests with various parameters" / "the tests being run are purely relative comparisons, such as having a t-test with null hypothesis that the metric didn't increase by more than 5 percent. While relative comparisons are easy to reason about, they behave extremely poorly if the provided time series value is typically zero, or if a large relative change occurs in absolute numbers too small to be important to the service owner."
- URL：https://sre.google/static/pdf/canary_analysis.pdf
- 日期：2018
- 来源类型：官方一手
- 承重：是（方法）
- 叙事：canary 统计学盲区（低流量/零值指标）；多重检验但未公开 FWER 控制

## C08 Google CAS 的「自适应」反噬：用户反复重试危险变更，CAS 会把风险行为学成新常态
- 论断：在线行为学习假设「坏行为罕见」；若用户反复重试一个真正危险的推送，CAS 最终会把它当作常态不再告警。另有「用户无视 canary 失败、推送坏版本」导致的事故，根源是对复杂自动化的不信任。
- 原文："Adaptive behavior poses a risk if a user keeps retrying a push when an anomaly is actually dangerous: CAS eventually starts treating this risky behavior as the new norm and no longer flags it as problematic." / "CAS is useful but far from perfect. It has experienced incidents when users disregarded a canary failure and pushed a broken release. User mistrust of complex automation is at the root of many of these issues."
- URL：https://sre.google/static/pdf/canary_analysis.pdf
- 日期：2018
- 来源类型：官方一手
- 承重：是（误报代价→信任侵蚀→真报被无视）
- 叙事：反方/误报代价

## C09 Google CAS 明说「无法量化影响」：不公布拦截率，改用 near-miss 分析
- 论断：Google 自己说「影响分析非常难」：无法知道被阻止的事故会有多大；考虑过故意放过一部分失败判定做 A/B，但认为信号不清，最终用「近失分析」（翻大型 postmortem 找 CAS 本可拦却没拦的）。即 Google 没有、也认为难以给出 canary 检出率/拦截价值的可靠数字。
- 原文："Impact analysis is very hard ... If CAS actually prevents an outage, how do you know the impact of the outage and, therefore, the impact of CAS?" / "They considered an A/B approach where failures of a subset of evaluations were ignored, passing them in order to measure impact. Given the many factors that influence the magnitude of an outage, however, this approach would not be expected to provide a clear signal." / "Ultimately, the team settled upon what they call nearmiss analysis: looking at large postmortems at Google and identifying outages that CAS could have prevented, but did not prevent."
- URL：https://sre.google/static/pdf/canary_analysis.pdf
- 日期：2018
- 来源类型：官方一手
- 承重：是（关键：最大规模部署方不公布检出率）
- 叙事：反方/证据缺口——「AI 拦下多少坏发布」在一手层面缺乏分母

## C10 Google CAS：好的健康指标「出奇地少」；喂全部指标效果差；canary 不能替代测试与监控
- 论断：弱相关指标导致结果差；只用少数关键指标效果「好得多」；单组件 canary 即便极端失常，对整体 SLO 的影响也可能很小，所以需要组件级指标。「完美准确」的 canary 配置会阻断可接受的变更、造成大量 toil。
- 原文："In practice, using weakly relevant metrics leads to poor results." / "Even if a canary of a single component misbehaves in the extreme, its impact on a service's overall SLO can be small." / "Attempts at hyper-accurate canary setups often fail because the rigid configuration causes too much toil during regular releases."
- URL：https://sre.google/static/pdf/canary_analysis.pdf
- 日期：2018
- 来源类型：官方一手
- 承重：中
- 叙事：误报代价/指标选择是瓶颈而非算法

## C11 Google SRE Workbook：多数事故由二进制或配置推送触发；测试环境非 100% 等同生产，部分缺陷必然进生产
- 论断：Google 经验中多数事故由二进制或配置推送触发（引其 postmortem 分析，原章未给百分比）；canary 是 A/B 测试；在真实流量到达前不可能发现所有发布相关缺陷。
- 原文："In Google's experience, a majority of incidents are triggered by binary or configuration pushes (see Results of Postmortem Analysis)." / "Even if your release pipeline is fully automated, you won't be able to detect all release-related defects until real traffic is hitting the service." / "Canarying is effectively an A/B testing process."
- URL：https://sre.google/workbook/canarying-releases/ （The Site Reliability Workbook, ch.16 "Canarying Releases", O'Reilly 2018）
- 日期：2018
- 来源类型：官方一手（书）
- 承重：是（前提）
- 叙事：中性前提

## C12 SRE Workbook 结构性盲区：低峰部署抓不到性能缺陷；5% canary × 20% 错误 = 全局 1%，可被淹没在噪声里；指标聚合窗口须 ≤ canary 时长
- 论断：(a) 性能缺陷通常只在高负载出现，低峰时段部署抓不到；(b) 5% canary 出 20% 错误，全局监控只看到 1% 错误率，可能与其他错误源无法区分——所以必须按 canary/control 分组看；(c) 只收到少量请求就结束 canary 不提供有用信号；(d) 「before/after」canary 受时间（工作日 vs 周末）噪声污染；(e) 持续部署（如每天 20 次）时 canary 必须短得多；建议同一时间只跑一个 canary。
- 原文："Performance defects typically manifest only under heavy load, so deploying at an off-peak time likely wouldn't trigger performance-related defects." / "Consider our earlier example of a canary deployment to 5% of the population that runs at a 20% error rate. Because monitoring likely looks at the system as a whole, it will detect an overall error rate of only 1%. Depending on the system, this signal might be indistinguishable from other sources of errors" / "If you deploy continuously (for example, 20 times in a day), your canary duration must be significantly shorter." / "Because time is one of the biggest sources of change in observed metrics, it is difficult to assess degradation of performance with before/after evaluation."
- URL：https://sre.google/workbook/canarying-releases/
- 日期：2018
- 来源类型：官方一手
- 承重：是（盲区）
- 叙事：canary 盲区/速度与检出的权衡

## C13 SRE Workbook：误报会让 canary 被关掉或被无视；before/after canary 检测更快但恢复时间未必更短
- 论断：噪声指标（如 CPU）导致 canary 时好时坏，结果是「被运维禁用或忽略」。检测快 ≠ 恢复快：before/after 方式「可能更快检测」，但总恢复时间与小 canary 相近——直接支持「TTD 与 MTTR 必须分开」。
- 原文："an increase in resource usage doesn't necessarily impact a service and may result in a flaky or noisy canary process. This can result in the canary process being disabled or ignored by operators, which can defeat the point of having a canary process in the first place." / "A before/after canary may detect the problem faster, but the overall time to recovery may still be quite substantial and similar to a smaller canary."
- URL：https://sre.google/workbook/canarying-releases/
- 日期：2018
- 来源类型：官方一手
- 承重：中
- 叙事：误报代价；检测≠恢复

## C14 Netflix/Google Kayenta：典型 canary = 约 1% 流量、canary 与新建 baseline 各约 3 台实例；聚合 0–100 分→success/marginal/failure
- 论断：Kayenta（2018-04 开源）典型配置：把约 1% 生产流量导给 canary 和一个新建 baseline（与生产同代码，用以消除启动效应），通常各 3 台实例；逐指标统计检验后按权重聚合为 0–100 分，success 放行、marginal 转人工、failure 回滚。规模口径为「预期年底每天数千次判定」（预期，非实测）。
- 原文："The basic idea is to route a small subset of production traffic, for example 1%, through a deployment that reflects the changes (the canary) and a newly deployed instance that has the same code and configuration as production (the baseline). ... Typically three instances are created each for baseline and canary, while production has multiple instances. Creating a new baseline helps minimize startup effects and limit the system variations between it and the canary." / "By the end of the year, we expect Kayenta to be making thousands of canary judgments per day."
- URL：https://cloud.google.com/blog/products/gcp/introducing-kayenta-an-open-automated-canary-analysis-tool-from-google-and-netflix （Netflix 原文 netflixtechblog 对脚本 403，取 Google Cloud 联合发布稿）
- 日期：2018-04-10
- 来源类型：官方一手（厂商博客；Google/Netflix 推开源工具，受益方为 Spinnaker/GCP 生态）
- 承重：是（规模参数）
- 叙事：canary 样本极小——3 vs 3 实例、1% 流量，统计功效天然有限

## C15 Kayenta 判定细节：逐指标 Mann-Whitney U，98% 置信；缺数据（Nodata）的指标被排除、不扣分，≥50% 指标 Nodata 才自动失败
- 论断：每个指标单独做 Mann-Whitney U 检验，需 98% 置信且置信区间落在容差带之外才判 High/Low；Nodata 指标「不扣分也不加分」——低流量路径上的错误指标若 canary 期间没有数据，默认不会拉低分数（除非配置 mustHaveData/nanStrategy=replace）。这是低流量路径盲区在工具层面的具体机制。多指标逐个检验未见多重比较校正说明。
- 原文："The judge needs to be 98% confident there's a real difference before flagging a metric" / "The Mann-Whitney U test is a nonparametric test that compares two distributions." / "Nodata : Metric is excluded from group score calculations (doesn't hurt or help the score), but counts toward the 50% NODATA threshold." / "50% NODATA rule : If 50% or more of all metrics are classified as Nodata"
- URL：https://spinnaker.io/docs/guides/user/canary/judge/
- 日期：访问 2026-10-30（文档无明确版本日期）
- 来源类型：官方一手（开源项目文档）
- 承重：中
- 叙事：canary 统计盲区（低流量/缺数据被静默放过）

## C16 Netflix 序贯检验（KDD 2022）：反复「偷看」固定样本检验会膨胀 I 类错误、制造误报；改用 anytime-valid 序贯检验
- 论断：Netflix 指出 canary 中常见的「peeking」（对累积数据反复跑固定 n 检验）使 I 类错误失控，误报增加人工干预、降低交付节奏；提出基于 Howard & Ramdas 置信序列的序贯检验，可连续监控同时严格控制误报概率，并给出测试时长上界（便于算最大样本量）。
- 原文："The problem with this practice is a lack of control over type I errors. One wants to apply the test frequently, to detect regressions as soon as possible, but the probability of making a type I error with a fixed-n test increases with each usage [1]. We posit that canary tests should always have a strict type I error guarantee. Otherwise, the experiment would be unreliable, producing many false alerts which can increase manual intervention and reduce delivery cadence."
- URL：https://arxiv.org/pdf/2205.14762v2 （Lindon, Sanden, Shirikian, "Rapid Regression Detection in Software Deployments through Sequential Testing", KDD 2022, DOI 10.1145/3534678.3539099）
- 日期：2022-05（arXiv）/ 2022-08（KDD）
- 来源类型：同行评审（Netflix 作者，案例为自家）
- 承重：是（统计方法）
- 叙事：误报代价与「快检测 vs 误报」权衡的统计学正解

## C17 Netflix 序贯检验案例 TTD：播放失败 bug 11.08 秒、PlayDelay 回归约 65 秒（α=0.01）——仅 2 个精选案例
- 论断：两个真实 canary 案例：一个客户端 bug 导致多设备播放失败，SPS（成功起播事件）计数的序贯 p 值在 11.08 秒跌破 0.01；PlayDelay 回归约 65 秒跌破 0.01，并阻止该候选版本进入生产。口径：n=2 个作者挑选的成功案例，大流量核心指标；无漏报率、无全量部署统计，不能外推为一般 TTD。
- 原文："The left axis of figure 4 shows the sequential p-value, which falls below α = 0.01 in a mere 11.08 seconds." / "The p-value falls below 0.01 after approximately 65 seconds." / "the sequential methodology successfully detected a performance regression in PlayDelay and prevented the release candidate from reaching the production environment."
- URL：https://arxiv.org/pdf/2205.14762v2
- 日期：2022
- 来源类型：同行评审（Netflix 自评，案例研究）
- 承重：是（但样本 n=2，须标注）
- 叙事：支持「大流量核心指标上检测可到秒级」；不支持一般化

## C18 Meta Configerator：配置 canary 分阶段（先 20 台，再上千台的整集群），约 10 分钟；成功拦截案例 = 20 台服务器上的错误日志暴涨
- 论断：Facebook 配置变更的自动 canary 按 spec 分阶段：例如阶段 1 测 20 台、阶段 2 整个集群数千台；判据如「新配置服务器 CTR 不低于旧配置 x%」。自动 canary 约需 10 分钟（TTD 量级）。案例：代码与配置 schema 不同步，canary 在 20 台上对比其余生产服务器的错误日志，发现 log spew，中止 rollout、避免宕机。
- 原文："For example, in phase 1, test on 20 servers; in phase 2, test in a full cluster with thousands of servers." / "It compared the error logs of those 20 servers with those of the rest of the production servers, and detected a log spew, i.e., rapid growth of error logs. It aborted the rollout and prevented an outage." / "latency is less critical for Configerator, because automated canary tests take about ten minutes anyway."
- URL：https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf （Tang et al., "Holistic Configuration Management at Facebook", SOSP 2015）
- 日期：2015-10
- 来源类型：同行评审（Facebook 作者自评）
- 承重：是
- 叙事：支持「配置 canary 可在分钟级拦截」

## C19 Meta Configerator 盲区：小规模 canary 抓不到负载问题（罕见代码路径打爆后端存储，全站部署后才暴露）；人把真报当误报覆盖
- 论断：(a) 配置把移动端请求导向一条罕见代码路径、压垮数据存储，canary 当时只在少量服务器上测，规模不足以引发负载问题，全站部署后延迟才显现——之后才加了「数千台整集群」阶段；(b) 另一例：canary 因实例崩溃拒绝配置，工程师认定「一定是 canary 误报」并覆盖，结果更多崩溃（配置本身正确，但触发新代码路径上的竞态 bug）。
- 原文："At that time, automated canary tests did not catch the problem, because the testing was done on a limited number of servers and the small scale testing was insufficient to cause any load issue. The latency increase became evident only after the config was deployed site wide." / "'It must be a false positive of the canary tool!' She overrode the tool's rejection and deployed the config, which caused more crashes." / "Enhancing automated canary tests is a never ending battle"
- URL：https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf
- 日期：2015-10
- 来源类型：同行评审（Facebook 自评）
- 承重：是（盲区：规模相关；信任：真报被覆盖）
- 叙事：canary 盲区 + 误报文化的反噬

## C20 Meta：3 个月高影响事故中 16% 与配置管理相关；其中 22% 是「合法配置触发代码 bug」
- 论断：Facebook 人工分析某 3 个月内高影响事故，16% 与配置管理相关，其余以软件 bug 为主；配置相关事故中 Type I 常见错误 42%、Type II 微妙错误（负载、故障诱发、蝴蝶效应）36%、Type III 合法配置暴露代码 bug 22%。口径：时间窗 3 个月（未给具体年份，论文 2015），分母=高影响事故数（未给绝对数）。
- 原文："we manually analyzed the high-impact incidents during a three-month period. We found that 16% of the incidents were related to configuration management, while the rest were dominated by software bugs." / "Type I: common config errors 42% / Type II: subtle config errors 36% / Type III: valid config changes exposing code bugs 22%" / "Type II errors are harder to anticipate ahead of time, e.g., load-related issues, failure-induced issues, or butterfly effects."
- URL：https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf
- 日期：2015-10
- 来源类型：同行评审（Facebook 自评）
- 承重：中（分母未披露）
- 叙事：漏网问题共性（负载/交互/代码-配置耦合）

## C21 Azure SDP 官方：canary 区域→pilot→逐区→区域对；强制 bake time；「有意牺牲速度」换信号积累
- 论断：Azure 安全部署策略由中央声明式策略决定速度（而非开发者），含强制健康信号和各阶段强制 bake time，理由是让变更暴露在完整负载周期（早上企业用户、晚上游戏用户、长期 VM 创建）。官方明说部署工具「有意牺牲速度」。无拦截数量。紧急情况可加速（安全补丁）。
- 原文："These exceptions are very rare, in general our deployment tools and processes intentionally sacrifice velocity to maximize the chance for signals to build up and scenarios and workflows to be exercised at scale, thus creating the opportunity to discover issues at the smallest possible scale of impact." / "The reason to have software sitting and baking for different periods of time across each phase is to make sure to expose the change to a full spectrum of load on that service."
- URL：https://azure.microsoft.com/en-us/blog/advancing-safe-deployment-practices/ （Mark Russinovich 署名系列，正文作者 Cristina del Amo Casado）
- 日期：2020-02-05
- 来源类型：官方一手（厂商博客）
- 承重：是（渐进发布的速度成本为官方自认）
- 叙事：反方/成本——检出能力靠时间换

## C22 Google Cloud 2025-06-12：二进制按区域逐步发布了两周，但出错代码路径在 rollout 中「从未被执行」；触发它的策略数据数秒内全球复制
- 论断：典型「canary 结构性盲区」双重叠加：(1) 2025-05-29 的 Service Control 新代码经区域逐步发布，但故障路径需特定策略变更才触发，rollout 期间从未执行，且无 feature flag；(2) 6-12 一条含空字段的策略写入区域 Spanner，因配额管理是全局的，数秒内全球复制，全球同时 crash loop。三段时间：SRE 2 分钟内开始分诊（检测）、10 分钟内定位根因（RCA）、约 25 分钟 red-button 就绪、40 分钟完成推送（缓解开始），us-central1 因羊群效应约 2h40m 才完全恢复。整改：全局复制数据须增量传播。
- 原文："This code change and binary release went through our region by region rollout, but the code path that failed was never exercised during this rollout due to needing a policy change that would trigger the code." / "Given the global nature of quota management, this metadata was replicated globally within seconds." / "Within 2 minutes, our Site Reliability Engineering team was triaging the incident. Within 10 minutes, the root cause was identified and the red-button (to disable the serving path) was being put in place. The red-button was ready to roll out ~25 minutes from the start of the incident. Within 40 minutes of the incident, the red-button rollout was completed" / "data replication needs to be propagated incrementally with sufficient time to validate and detect issues."
- URL：https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW
- 日期：2025-06-13（事故报告）
- 来源类型：官方一手（事故报告）
- 承重：是（盲区 + 三段分时样例）
- 叙事：canary 盲区（休眠代码路径 + 全局数据推送）；检测快不等于影响小

## C23 Cloudflare 2025-11-18：自动测试 3 分钟检出，但确信根因花了约 2 小时（先误判为 DDoS），主影响 3 小时后才解除——瓶颈在定位不在检测
- 论断：数据库权限变更 11:05 部署，11:28 影响开始，11:31 首个自动测试检出（TTD≈3 分钟），11:35 建事故会议；团队先怀疑超大规模 DDoS、调查 Workers KV，13:37 才确信是 Bot Management 配置文件（RCA≈2 小时），14:24 停止新文件生成传播，14:30 主影响解除，17:06 全部恢复。该特征文件每几分钟生成一次并推送全网（设计上为快速应对机器人），且好坏文件交替生成（集群部分升级），使症状忽好忽坏、更难定位。
- 原文："The first automated test detected the issue at 11:31 and manual investigation started at 11:32. The incident call was created at 11:35." / "After we initially wrongly suspected the symptoms we were seeing were caused by a hyper-scale DDoS attack, we correctly identified the core issue" / "every five minutes there was a chance of either a good or a bad set of configuration files being generated and rapidly propagated across the network." / "13:37 ... We were confident that the Bot Management configuration file was the trigger for the incident."
- URL：https://blog.cloudflare.com/18-november-2025-outage/
- 日期：2025-11-18
- 来源类型：官方一手（事故复盘）
- 承重：是（三段分时：检测分钟级，定位小时级）
- 叙事：支持「检测不是瓶颈，RCA/缓解才是」；全局配置推送是 canary 盲区

## C24 Cloudflare：两次 2025 大事故的共同点是配置「数秒内全球传播」，绕过了二进制发布才有的渐进门禁；2026-05 宣称配置已全面改为健康门控部署（Snapstone）
- 论断：Cloudflare 自承二进制有「员工流量→免费用户→逐步扩大，检出异常无人工自动回滚」的门禁，但配置变更（含其内部团队的）通过 Quicksilver 数秒内到达 90% 服务器，未经门禁；11-18（约 2h10m）与 12-05（28% 应用约 25 分钟）两次事故均如此。2026-05-01 称已建 Snapstone，将渐进发布+实时健康监控+自动回滚默认用于配置，并称同类变更「会在早期阶段被检出，只影响小比例流量」——此为反事实自述，无实测检出数据。
- 原文："Our ability to deploy configuration changes globally within seconds was the core commonality across the two incidents. In both events, a wrong configuration took down our network in seconds." / "When a user creates a new DNS record, or creates a new security rule, it reaches 90% of servers on the network within seconds." / "if the same Bot Management change that caused the failure in November were to roll out now, the system would detect the failure in an early stage of the deployment, before it had affected anything more than a small percentage of traffic."
- URL：https://blog.cloudflare.com/fail-small-resilience-plan/ （2025-12-19）；https://blog.cloudflare.com/code-orange-fail-small-complete/ （2026-05-01）
- 日期：2025-12-19 / 2026-05-01
- 来源类型：官方一手（厂商博客；后者的效果宣称为厂商口径）
- 承重：是（盲区实证）；效果宣称不承重
- 叙事：canary 盲区（配置/数据推送不走门禁）；2026 趋势是把配置纳入渐进发布

## C25 Facebook/OANDA 持续部署（ICSE 2016）：部署频率增长时，严重故障数几乎不随之增长（关键/中/低三档趋势斜率 0.0004/0.0013/0.0061）
- 论断：以 Facebook 每月部署数为横轴、按严重度的生产故障数为纵轴，关键故障趋势线斜率 0.0004、中等 0.0013、低 0.0061（每多一次部署，故障数增量），即严重故障增长远慢于部署增长。代价：2009-01 至 2010-07 生产率激增期间以热修复数衡量的质量下降，随后质量改进「以部分生产率为代价」。口径：Facebook 内部 SEV 数据，作者含 Facebook 员工；相关非因果；未单独度量 canary/发布后检测的贡献。
- 原文："The number of critical and medium priority failures grow significantly slower than the number of deployments per month, with trendline slopes of 0.0004, 0.0013, and 0.0061, respectively; and this despite the growth in size and complexity of the product." / "Efforts to improve quality then came at the expense of some productivity."
- URL：https://www.eecg.toronto.edu/~stumm/Papers/Savor-ICSE16.pdf （Savor, Douglas, Gentili, Williams, Beck, Stumm, ICSE-C 2016）
- 日期：2016-05
- 来源类型：同行评审（行业 track，作者含公司员工）
- 承重：中
- 叙事：反方之反方——小步快发不必然更多事故；质量与速度确有权衡

## C26 Savor 2016：逐次变更的小幅资源回退在单次发布中「看起来合理」，累积起来巨大（死于千刀）——单次 canary 的结构性盲区
- 论断：持续部署中每次更新的资源占用增量很小，单次看不显著，但累积可观；论文给的假设例：每次 +0.05% CPU、每周 100 次，一年 CPU +260%。注意这是假设算例，不是实测。对 canary 的含义：低于最小可检测效应（MDE）的单次回退，逐次 canary 检验永远看不见，需要跨版本长期基线。
- 原文："continuous deployment can suffer from a 'death by a thousand cuts,' because release decisions are decentralized to individual developers rather than having a central coordinating body as in the waterfall model." / "Consider a hypothetical example where a set of updates each consume an additional 0.05% of CPU. ... having 100 such releases per week (for example) means that CPU utilization would increase by 260% within a year."
- URL：https://www.eecg.toronto.edu/~stumm/Papers/Savor-ICSE16.pdf
- 日期：2016-05
- 来源类型：同行评审（行业 track）
- 承重：中（假设算例，勿当实测）
- 叙事：canary 盲区（低于 MDE 的累积回退）

## C27 SCWarn（FSE 2021）：某大型商业银行约 50.4% 事故由坏变更引起；多模态检测 F1 0.95，MTTD 降 20.4%–60.7%
- 论断：学术+银行合作研究：基于一家大型商业银行数据，约 50.4% 的事故由坏变更（代码缺陷、配置错误、资源争用、软件版本）引起；SCWarn 在两个数据集上平均 F1 0.95，MTTD 相对基线方法降低 20.4%–60.7%。口径：MTTD 降幅是相对其他算法基线（非相对线上人工流程）；两个数据集含注入/历史坏变更；单一机构样本。
- 原文："Our quantitative analyses indicate that about 50.4% of incidents are caused by bad changes, mainly because of code defect, configuration error, resource contention, and software version." / "achieving 0.95 F1-score on average and reducing MTTD (mean time to detect) by 20.4%∼60.7%."
- URL：https://doi.org/10.1145/3468264.3468543 （Zhao et al., ESEC/FSE 2021；摘要经 OpenAlex 逆排索引还原，全文闭源未读）
- 日期：2021-08
- 来源类型：同行评审（摘要层核验，正文未读）
- 承重：中（降级：未读正文，基线定义未核）
- 叙事：支持「算法可缩短检测」，但幅度口径是算法间比较

## C28 SCELM（arXiv 2025-07，LLM+CoT）：坏变更检测 F1 0.925–1.000；但 D1 数据集极小（10% 抽样=2 个案例）；「解决时间降 90%」来自运维人员反馈，属 MTTR 口径
- 论断：南开/清华/腾讯等的 LLM 框架在三个工业数据集（yunzhanghu、kontrast、bytedance）上坏变更检测 F1 分别 1.000/0.942/0.925，基线 SCWarn/Kontrast/Lumos/Funnel/Gandalf 平均 F1 0.87–0.89。警示：D1 案例数极少（文中称抽 10% 只有 2 个案例，推知约 20 个）；上线效果「检测几乎所有错误变更」「解决时间降 90%」来源为 OCE 反馈，且是 time to resolution（MTTR 类），不能当检测速度证据；预印本未经同行评审。
- 原文："SCELM demonstrated outstanding detection capability, achieving F1-scores of 1.000, 0.942, and 0.925 on datasets D1, D2, and D3, respectively. By comparison, baseline methods SCWarn, Kontrast, Lumos, Funnel, and Gandalf had average F1-scores of 0.8935, 0.888, 0.868, 0.869, and 0.8685" / "This is attributed to the small number of cases in D1—sampling 10% results in only two cases" / "Feedback from Operations and Cloud Engineers (OCEs) indicates that SCELM is capable of detecting nearly all erroneous changes ... Compared to traditional manual analysis, SCELM has reduced the time to resolution for erroneous changes by 90%"
- URL：https://arxiv.org/pdf/2507.09315
- 日期：2025-07-12
- 来源类型：预印本（学术+企业，未同行评审）
- 承重：否（作为「LLM 时代数字口径薄弱」的样例）
- 叙事：AI 乐观叙事的典型证据形态——小样本 F1 + MTTR 混淆

## C29 从业者（Headout, 2025-04）：自动 canary 回滚误报从每周 5 次降到每周 1 次；低 RPM 服务与只路由到 canary 的 API 是误报残余来源
- 论断：一家 40+ 微服务的中型公司用 Argo Rollouts 做自动回滚；最初用「总错误率 vs 前一小时」固定阈值，被与部署同时的垃圾流量攻击、错误日志配置等干扰导致误回滚；改为 canary 与 stable 的错误差后，误回滚由每周 5 次降到 1 次。分母（每周部署数）未披露，无法换算误回滚率。
- 原文："Transitioning from a total error rate metric to evaluating error differences has reduced false positive rollbacks from five per week to just one." / "Although it's challenging to eliminate false positives entirely due to edge cases such as low RPM service errors or specific failing APIs being routed exclusively to canary pods"
- URL：https://backstage.headout.com/canary-deployment-with-automated-rollback/
- 日期：2025-04-11
- 来源类型：从业者博客
- 承重：否（单家、无分母）
- 叙事：误报代价真实存在；公开「误回滚率」几乎无大厂数字

## C30 Azure Front Door 2025-10-29：不兼容配置**经过了分阶段健康门控**仍全球传播——故障是异步延迟触发的，各阶段健康检查全部通过，且把坏配置写进了「last known good」快照
- 论断：AFD 配置管线有 pre-canary→canary→逐波扩展、每阶段健康门控（ConfigShield），历史上 5–10 分钟完成全球；10-29 的不兼容元数据因数据面故障是异步的（FlatBuffers 异步释放时的引用计数潜伏 bug），rollout 期间健康检查全部通过，配置全球传播并更新了 LKG 快照，回滚目标也被污染。10-09 另一事故：保护系统起初拦住了，但工程师手动清理操作绕过了保护层（人工覆盖自动拦截，影响欧洲约 6%、非洲约 16%）。AFD 服务代码本身走 2–3 周 SDP，但官方承认潜伏 bug 可躲过 SDP，直到特定流量/配置组合触发。整改：强制同步处理、增加阶段与 bake time、目标 <10 分钟自动恢复。
- 原文："Because the failure mode in the data-plane was asynchronous, the health checks validations embedded in our protection systems were all passed during the rollout. The incompatible customer configuration metadata successfully propagated globally through a staged rollout and also updated the 'last known good' (LKG) snapshot." / "A manual cleanup of stuck tenant metadata bypassed our configuration protection layer, allowing incompatible metadata to propagate beyond our canary edge sites." / "Azure Front Door follows a safe deployment practice (SDP) process to roll out newer versions of management, control or data plane over a period of approximately 2-3 weeks. ... However, latent bugs that escape pre-validation and SDP rollout can remain undetected until a specific combination of customer traffic patterns or configuration changes trigger the issue."
- URL：https://techcommunity.microsoft.com/blog/azurenetworkingblog/-/4479416 （"Azure Front Door: Implementing lessons learned following October outages", Tiwari/Srivastava/Chawla）
- 日期：2025-12-18
- 来源类型：官方一手（厂商工程博客）
- 承重：是（盲区：异步/延迟故障 > 阶段观察窗；人工绕过；回滚目标被污染）
- 叙事：canary 盲区——「有渐进发布」不等于「能拦住」

## C31 AFD：客户配置行业惯例 5–10 分钟全球生效；WAF/DDoS 平台数据每日更新走 SDP 并有 >12 小时 bake——速度与检出窗口的显式权衡
- 论断：同一平台对不同变更类型采取截然不同的传播速度：服务代码 2–3 周、平台安全数据 >12 小时 bake、客户配置 5–10 分钟全球。客户配置正是两次事故所在类别。说明「渐进发布」覆盖程度取决于变更类型，最快的那类（配置）恰是盲区。
- 原文："Updates to these datasets occur daily through multiple SDP stages with an extended bake time of over 12 hours to minimize the risk of global impact during rollout." / "Due to the nature of these changes, it is expected across the edge delivery / CDN industry to propagate these changes globally in 5-10 mins. Both outages stemmed from issues within this category."
- URL：https://techcommunity.microsoft.com/blog/azurenetworkingblog/-/4479416
- 日期：2025-12-18
- 来源类型：官方一手
- 承重：中
- 叙事：渐进发布速度成本/变更类型差异

## C32 CrowdStrike 2024-07 Channel File 291：内容（数据）更新当时不走分阶段发布；整改后才加 canary + 部署环 + bake-in
- 论断：官方 RCA 第 6 条发现「每个 Template Instance 都应分阶段发布」，整改为通过 canary 测试后逐环推广、每环有 bake-in 时间收集遥测——反推事发时 Rapid Response Content 未经分阶段 canary。另：Content Validator 有逻辑错误（离线验证漏网）。这是「数据/内容推送不按实例分批 → canary 结构性缺席」的标志性案例。
- 原文："Findings: Each Template Instance should be deployed in a staged rollout." / "New Template Instances that have passed canary testing are to be successively promoted to wider deployment rings or rolled back if problems are detected. ... Promoting a Template Instance to the next successive ring is followed by additional bake-in time, where telemetry is gathered to determine the overall impact"
- URL：https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf
- 日期：2024-08-06
- 来源类型：官方一手（事故 RCA）
- 承重：中（其他调研线可能已覆盖，此处只取「缺 canary」一点）
- 叙事：canary 盲区（内容/数据推送绕开渐进发布）

---

## 交叉口径问题

1. **Gandalf recall 定义不一**：数据面「100% recall」= 无 Sev0-2 事故归因于坏发布（代理指标，低影响漏报不计）；控制面「99.8% recall」与「39 告警/2 误报/漏 2」不自洽——按标准定义 recall=37/39≈94.9%，99.8% 疑似 (1200−2)/1200，即以全部部署为分母（更接近 specificity/accuracy）。引用时必须写明，或只引原始计数（39 告警、2 误报、2 漏报、1200+ 部署）。
2. **Gandalf 99.2%「生产前拦截」**分母是「被检出的可疑 rollout」，不是全部坏 rollout；不能读成「99.2% 坏发布在生产前被拦」。
3. **规模数字 ≠ 拦截数字**：Google CAS「每天数十万次评估」、Kayenta「预期每天数千次判定」都是评估次数；Google 明确表示无法可靠量化拦截价值（C09）。全线没有找到任何大厂公开「误回滚率（false rollback / 全部部署）」——唯一具体数字是从业者 Headout 的「每周 5→1 次」，且无分母（C29）。
4. **TTD 起点不一**：Gandalf「约 5 分钟」= 部署后数据到决策的流水线延迟；Netflix「11 秒/65 秒」= canary 开始到序贯 p<0.01；Configerator「约 10 分钟」= canary 阶段时长；Cloudflare「3 分钟」= 影响开始到首个自动测试告警；Google Cloud「2 分钟」= 事故开始到 SRE 分诊。不可并列成一个「AI 检测时间」。
5. **MTTR/解决时间被当作检测证据的风险**：SCELM「解决时间降 90%」（C28）、Gandalf「部署总时长减半」（C03，是审批流程提速，不是检测提速）都不是 TTD。Google SRE workbook 明确指出检测快不等于恢复快（C13）。
6. **算法 vs 基线的比较对象**：SCWarn「MTTD 降 20.4–60.7%」是相对其他算法，不是相对人工值班；SCELM F1 对比基线（含 Gandalf 复现）在小数据集上进行，D1 约 20 例。
7. **检测 vs 定位分段**：Cloudflare 11-18 检测 3 分钟、确信根因约 2 小时（中间误判 DDoS）；Google 6-12 检测 2 分钟、定位 10 分钟、缓解推送 40 分钟、完全恢复 2h40m。两案说明发布后检测已非瓶颈，定位与全局缓解才是——但这是两个案例，不是统计。
8. **「渐进发布存在」≠「渐进发布覆盖」**：AFD 10-29（异步故障通过健康门控）、Google 6-12（代码已逐区发布但路径未执行；数据秒级全局复制）、Cloudflare 11-18/12-05（配置秒级全局）、CrowdStrike 2024（内容不分阶段）。盲区共性：(a) 休眠代码路径需特定数据/配置触发；(b) 全局数据/配置推送；(c) 延迟/异步失败超过阶段观察窗；(d) 规模/负载相关（Configerator 罕见路径打爆存储）；(e) 低于单次 MDE 的累积回退（Savor 假设例）；(f) 人工覆盖自动判定（Configerator、Gandalf 案例 I、AFD 10-09、CAS 用户无视失败）。
9. **年代口径**：Gandalf（2018 数据）、CAS（2018）、Kayenta（2018）、Configerator（2014–2015 数据）都是 2015–2020 年的自评数字；2024–2026 的新增一手资料主要是事故复盘（定性+时间线），而非检出率统计。成文须标明「最新的定量检出率数据仍停留在 2018 年前后」。
10. **自评偏差**：Gandalf、CAS、Kayenta、Configerator、Savor、Netflix 序贯检验均为系统所有者自评；无独立第三方复现其生产检出率。
