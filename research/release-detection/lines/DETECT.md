# DETECT 线:生产回归与异常检测(截至 2026 年 10 月)

调研线负责范围:检测器本身的性能数据 + 对其评测方法的批评。只谈「检测(TTD)」段;RCA/缓解段的数字仅在标注时出现,不得当检测证据。

来源类型缩写:PR=同行评审;OF=官方一手(公司工程博客/官方报告);VS=厂商自报;PB=从业者博客;MD=媒体转述;AN=分析机构。
叙事:A=「AI/自动检测能接住坏发布」;B=「被高估/有盲区」;N=中性口径信息。

---

## D01 FBDetect 的 0.005% 是 CPU(gCPU)性能回归,不是正确性故障
- 论断:Meta FBDetect(SOSP 2024,Meta 作者自评)号称能在生产噪声中检出小至 0.005% 的回归;检测对象是吞吐、延迟、CPU、内存等**性能/资源**时间序列(约 80 万条),原因限定为代码或配置变更。0.005% 是 FrontFaaS 平台**子程序级 gCPU 绝对变化阈值**(Table 1 "FrontFaaS (small)" Δthreshold=0.005%),不是对错误率/可用性故障的检出能力。
- 原文:"catching regressions as small as 0.005% in noisy production environments. FBDetect monitors around 800,000 time series covering various types of metrics (e.g., throughput, latency, CPU and memory usage) to detect regressions caused by code or configuration changes in hundreds of services"
- URL:https://tangchq74.github.io/FBDetect-SOSP24.pdf (DOI 10.1145/3694715.3695977)
- 日期:2024-11(SOSP '24)
- 来源类型:PR(但作者全部来自 Meta,系统自评)
- 承重:是
- 叙事:A(能力)+ N(口径:性能而非正确性)

## D02 FBDetect 的检测延迟以「小时」计,且越小的回归等得越久
- 论断:FBDetect 是周期批处理,不是实时。FrontFaaS 小回归档(0.005%)每 2 小时重跑一次,分析窗口 4 小时 + 延长窗口 6 小时;AdServing 长期档每天跑一次、分析窗口 9 天。论文明言越小的阈值需要等待更久收集数据,并承认延长 went-away 窗口能减少误报但会推迟检测——TTD 与误报是显式权衡。论文**没有**报告 TTD 分布。
- 原文:Table 1 行 "FrontFaaS (small) 0.005% 2 hours 10 days 4 hours 6 hours"(列:Detection Threshold / Re-run Interval / Historical / Analysis / Extended Window);"this would delay the timeliness of regression detection. This trade-off is challenging and requires future research."
- URL:同 D01
- 日期:2024-11
- 来源类型:PR(Meta 自评)
- 承重:是(TTD 口径)
- 叙事:B(检测非即时)/N

## D03 FBDetect 原始 change point 99.7% 是瞬态假象;过滤三到四个数量级
- 论断:FrontFaaS 一个月短期检测原始产生 396 万个 change point;went-away 检测器滤掉 99.7%;全流程后只剩约 1/18857。论文称典型 change-point 算法在其环境下误报率会达 99.7%。即:**未经大量工程化过滤的异常检测在生产中几乎全是噪声**。
- 原文:"typical change-point detection algorithms [3] would result in a 99.7% false positive rate in our environment." / "Running the short-term regression detection algorithm for FrontFaaS detects 3.96 million change points." / "FBDetect reduces the number of performance anomalies that developers need to investigate by three to four orders of magnitude"
- URL:同 D01
- 日期:2024-11
- 来源类型:PR(Meta 自评)
- 承重:是(底率/误报)
- 叙事:B(原始检测器噪声)+ A(工程化过滤有效)

## D04 FBDetect 的「低误报」是在 32% 有标注的子集上外推的
- 论断:一个月内 FrontFaaS 报告 217 条回归;开发者明确确认的只有 70 条(49 真 / 21 假,即确认子集精度 70%);123 条标「resolved」无真值;24 条无人处理。「每 13 年才遇一次误报」是假设 49:21 比例推广到全部 217 条后按人头摊的结果。21 个误报中 15 个是 cost shift。
- 原文:"Among the 217 regressions reported by FBDetect, developers explicitly confirmed either true regressions or false positives for only 70 of them, marked another 123 as resolved, and did not act on the remaining 24. Among the 70 confirmed cases, 49 are true regressions and 21 are false positives. Assuming the same ratio (49:21) holds for the 217 reported regressions, a FrontFaaS developer would only need to investigate one false-positive regression approximately once every 13 years."
- URL:同 D01
- 日期:2024-11
- 来源类型:PR(Meta 自评)
- 承重:是
- 叙事:B(精度仅约 70%;「13 年一次」是摊薄指标)

## D05 FBDetect 的「几乎零漏报」以 4 起事故为真值,且其中 2 起检出了没人处理、1 起因指标未导出
- 论断:漏报评估以 FrontFaaS 2023 全年 4 起性能事故为 ground truth:2 起 FBDetect 检出但开发者未及时处理;1 起因开发者未把回归指标导出给 FBDetect(埋点缺口);1 起与变更无关。三年全站事故中找到 1 起由 FBDetect 漏报导致(cost-shift 检测器误滤,致某大服务 0.015% 错误率)。作者自己承认这不代表不漏小回归,只代表漏掉的没被注意到。与 EGADS 对比时「假设 FBDetect 漏报率为 0」。
- 原文:"Among the four performance incidents, two were detected by FBDetect but were not acted upon by developers in time. The third incident occurred because the developer did not configure the regressed metric to be exported to FBDetect" / "this does not imply that FBDetect never misses regressions larger than 0.005% for FrontFaaS; it only means that the missed regressions are not significant enough to be noticed by developers." / "we assume its false negative rate is zero."
- URL:同 D01
- 日期:2024-11
- 来源类型:PR(Meta 自评)
- 承重:是(检出≠处置;埋点缺口)
- 叙事:B

## D06 对照:通用异常检测(EGADS)在同一数据上要么误报压不住、要么漏 84%
- 论断:在 107 条 FBDetect 报警序列(人工复核 76 真 31 假)+ 约 3.5 万条无报警序列上,FBDetect 误报率 31/(35K+31)=0.00088(该集合上的 precision = 76/107 ≈ 71%)。Yahoo EGADS 三种算法中只有一种能满足作者设定的可用门槛(FPR<0.02),但漏报率 0.84。
- 原文:"FBDetect’s false positive rate is 31/(35K+31)=0.00088." / "only “EGADS algorithm 1” can meet this false positive rate, but at the cost of a 0.84 false negative rate, meaning it would miss 84% of true regressions."
- URL:同 D01
- 日期:2024-11
- 来源类型:PR(Meta 自评,对手是 2015 年开源基线)
- 承重:中
- 叙事:A(专用系统 >> 通用算法)/B(通用 AD 不可直接用)

## D07 FBDetect 的 RCA 成功率 35%(与检测分开)
- 论断(RCA 段,不是检测):一个月 217 条回归中 FBDetect 给出根因候选 75 条,71 条被确认(真因在 top-3);整体 75/217=35%,开发者人工仅补到 37%;作者经二次分析估计算法真实失败率约 22%。
- 原文:"While the success rate of FBDetect’s root cause analysis seems mediocre (75/217=35%), even developers’ manual efforts could only marginally improve it to (75+6)/217=37%."
- URL:同 D01
- 日期:2024-11
- 来源类型:PR(Meta 自评)
- 承重:中(给 RCA 线参考)
- 叙事:N

## D08 ServiceLab:Meta 发布前性能测试阈值 0.01%,但承认「有些问题会漏到生产」
- 论断:ServiceLab(OSDI 2024)在发布前回放生产流量做性能测试,FrontFaaS 上整体 CPU 回归 0.01% 即报警;FrontFaaS 中位检出回归 0.14%。FBDetect 论文明言发布前测试必要但有问题会漏过,因为难以精确复制生产环境,且检测极小回归需要只有生产舰队才能提供的样本量——这是「staging 漏掉什么」的一手解释(对性能类)。
- 原文(ServiceLab):"If a code change causes even just a 0.01% regression in the platform’s overall CPU usage, an alarm is raised." / "the median regression detected by ServiceLab for our large serverless platform, running on more than half a million machines, is only 0.14%."
  原文(FBDetect):"While pre-production performance testing [14, 25, 67] is necessary, some issues may slip through due to the difficulty of precisely replicating complex production environments in testing. Additionally, catching tiny regressions requires a massive amount of performance data samples, which are more feasible to gather from a large production fleet than a small test environment."
- URL:https://www.usenix.org/system/files/osdi24-chow.pdf ;同 D01
- 日期:2024-07(OSDI '24);2024-11
- 来源类型:PR(Meta 自评)
- 承重:是
- 叙事:N/B(离线漏检的结构性原因)

## D09 Kim et al. AAAI 2022:point-adjust 让随机分数成为 SOTA
- 论断:多数 TAD 论文用 point adjustment(PA:异常段内命中一点即算整段命中)。在 SWaT/WADI/MSL/SMAP 四个基准上,均匀随机分数的 F1-PA(0.969/0.965/0.931/0.961)超过所有 7 个已发表深度方法;去掉 PA 后随机分数 F1 仅 0.08–0.23。未训练的随机初始化模型在无 PA 时也与现有方法相当。
- 原文:"the PA protocol has a great possibility of overestimating the detection performance; that is, even a random anomaly score can easily turn into a state-of-the-art TAD method." / "we question the potential of existing TAD methods by showing that an untrained model obtains comparable detection performance to the existing methods even when PA is forbidden."
- URL:https://arxiv.org/abs/2109.05257 ;https://ojs.aaai.org/index.php/AAAI/article/view/20680
- 日期:2022-02(AAAI-22;arXiv v2 2022-01-04)
- 来源类型:PR
- 承重:是
- 叙事:B

## D10 Wu & Keogh:Yahoo 基准 86.1% 序列可用「一行代码」解决
- 论断:主流基准(Yahoo、Numenta、NASA、OMNI)多数样本有四类缺陷:平凡性、异常密度不现实、标签错误、run-to-failure 偏置。Yahoo 基准 367 条序列中 316 条(86.1%)可被一行简单规则解决。作者认为近年进展「可能是幻觉」。
- 原文:"The majority of the individual exemplars in these datasets suffer from one or more of four flaws." / "much of the apparent progress in recent years may be illusionary." / "316 out of 367 (86.1%) can be easily solved with a one-liner."
- URL:https://arxiv.org/abs/2009.13807 (IEEE TKDE 2023 正式版)
- 日期:arXiv 2020-09;IEEE TKDE vol.35 no.3 (2023), pp.2421–, DOI 10.1109/TKDE.2021.3112126(在线 2021-09)
- 来源类型:PR
- 承重:是
- 叙事:B

## D11 Microsoft SR-CNN(KDD 2019):生产数据 F1 仅约 0.5,且用延迟版 point-adjust
- 论断:SR-CNN 在 Microsoft 内部数据(372 条日粒度业务 KPI,随机抽取,客户/编辑人工标注)上 F1=0.537(冷启动)/0.507(测试集),precision 0.468/0.441;公开 KPI 集 F1 0.73–0.77。评测采用「段内任一点在延迟 k 内命中即整段算对」的协议(k=7 分钟级/3 小时级/1 日级)——即带延迟上限的 PA。摘要中「F1 提升超 20%」是相对基线的提升,不是绝对水平。该服务每天处理 400 万+ 条时间序列。
- 原文:"If any point in an anomaly segment can be detected by the algorithm, and the delay of this point is no more than k from the start point of the anomaly segment, we say this segment is detected correctly." / "Especially, the F 1 -score is improved by more than 20% on Microsoft production data." / Table 2 "SR-CNN 0.732 0.811 0.667 ... 0.537 0.468 0.630"
- URL:https://arxiv.org/abs/1906.03821
- 日期:2019-08(KDD '19)
- 来源类型:PR(Microsoft 自评)
- 承重:是
- 叙事:B(生产上 precision 不到一半)

## D12 Donut(WWW 2018):F 0.75–0.9 是「最佳阈值 + point-adjust」在 3 条阿里 KPI 上
- 论断:Donut 报告的 F-score 0.75–0.9 是对每个测试集枚举所有阈值取最优(best F-score,事后最优阈值)并使用 point-adjust 协议,数据为某全球大厂(阿里)18 条业务 KPI 中选出的 3 条(A/B/C)。这两个选择都系统性抬高分数(见 D09)。
- 原文:"its best F-scores range from 0.75 to 0.9 for the studied KPIs from a top global Internet company." / "The best F-score indicates the best possible performance of a model on a particular testing set, given an optimal global threshold." / "if any point in an anomaly segment in the ground truth can be detected by a chosen threshold, we say this segment is detected correctly, and all points in this segment are treated as if they can be detected by this threshold."
- URL:https://arxiv.org/abs/1802.03903
- 日期:2018-04(WWW '18)
- 来源类型:PR(清华 + 阿里)
- 承重:是
- 叙事:B

## D13 TSB-AD(NeurIPS 2024):40 种算法统一评测,简单/统计方法常常更好
- 论断:Liu & Paparrizos 在 1070 条人工精筛序列(40 个数据集)、40 种算法(统计/神经网络/基础模型)上统一调参评测,推荐 VUS-PR 作为最可靠指标;结论挑战「先进神经网络更优」的常识,简单架构与统计方法往往更好;神经网络仅在多变量、基础模型仅在点异常上有潜力。
- 原文:"Our findings challenge the conventional wisdom regarding the superiority of advanced neural network architectures, revealing that simpler architectures and statistical methods often yield better performance."
- URL:https://proceedings.neurips.cc/paper_files/paper/2024/file/c3f3c690b7a99fba16d0efd35cb83b2c-Paper-Datasets_and_Benchmarks_Track.pdf
- 日期:2024-12(NeurIPS 2024 D&B)
- 来源类型:PR
- 承重:是
- 叙事:B

## D14 ICML 2024 立场论文:SOTA 深度 TAD 模型实际上在学线性映射
- 论断:Sarfraz 等(KIT + Mercedes-Benz)论证 TAD 研究受困于有缺陷的指标和不一致的基准,复杂度带来的提升很小;简单基线(传感器量程偏离、L2 范数、最近邻距离、PCA 重建误差)持平或更好。
- 原文(arXiv 摘要片段,经 WebFetch 截取,需人工二次核对):"the revelation that state-of-the-art deep anomaly detection models effectively learn linear mappings" / added complexity "offers very little improvement"
- URL:https://arxiv.org/abs/2405.02678
- 日期:2024-05(v1)/ICML 2024
- 来源类型:PR(position paper)
- 承重:中
- 叙事:B

## D15 2025–2026 续篇:时序基础模型与 LLM 也没跳出「一行代码」基线
- 论断:ICLR 2026 论文测试 MOMENT、Chronos、TimesFM、Time-MoE、TSPulse 五个时序基础模型族,其异常检测表现与两个一行代码基线相当;核心假设「异常更难重建/预测」对这些模型并不成立。NeurIPS 2025 论文指出将 LLM 用于 TSAD 的近期尝试成效有限,常常不如简单方法。
- 原文:"anomalies are not consistently harder to reconstruct or forecast."(ICLR 2026, Zhu, Carpentier, Verbeke)/ "Recent efforts to apply Large Language Models (LLMs) to time-series anomaly detection (TSAD) have yielded limited success, often performing worse than even simple methods."(NeurIPS 2025, Park et al.)
- URL:https://iclr.cc/virtual/2026/poster/10010437 (OpenReview https://openreview.net/forum?id=H27kvyG4qf);https://proceedings.nips.cc/paper_files/paper/2025/hash/950a34c7b107111570077078e1b5b8ef-Abstract-Conference.html
- 日期:2026-04(ICLR 2026);2025-12(NeurIPS 2025)
- 来源类型:PR
- 承重:是(「AI 检测」的最新反证)
- 叙事:B

## D16 批评并未改变实践:2025 年 Microsoft 的 LLM 检测论文仍用 PA 类指标、仍在 KPI/Yahoo 上评
- 论断:Argos(UW + Microsoft Research,2025-01)用 LLM 自动生成检测规则,报告在内部数据上 F1 提升 28.3%;但主评测指标是 Event-F1 PA(带 point adjustment 的事件级 F1,比逐点 PA 温和,因其把段外每点都计为 FP),基准仍是 Wu & Keogh 批评过的 KPI 与 Yahoo;内部数据来自一个 AI 训练平台的 20 个硬件指标。
- 原文:"In ARGOS, we use Event-F1 PA as the primary evaluation method for calculating the F1 score metric." / "significant 28.3% F1 score improvement on our internal dataset."
- URL:https://arxiv.org/abs/2501.14170
- 日期:2025-01-24(arXiv v1)
- 来源类型:PR 预印本(Microsoft 作者自评)
- 承重:中
- 叙事:B(评测习惯延续)

## D17 Microsoft Teams 高严重度事故:只有约 55% 由自动监控发现,29% 由外部用户/客户报告
- 论断:Ghosh 等(SoCC 2022 最佳论文)分析 Microsoft Teams 约 152 起 Sev0–2 事故(有完整 postmortem 者):约 55% 由自动 watchdog 检出;其余 45% 中 29% 由外部用户或客户报告、10% 由 Microsoft 内部伙伴团队发现、6% 由本服务团队自己发现。约 17% 的事故缺监控或缺遥测覆盖(No Monitors 8.6% + Telemetry Coverage 8.6%),这类检测时间显著更长;无监控的事故中 70% 根因是代码 bug。
- 原文:"we observe that about 55% of the incidents were detected by the automated watchdogs." / "Among other 45% incidents, 29% incidents are reported by the external users or customers, and 10% are identified by the partner teams within Microsoft." / "Finding#7: ≈17% of incidents either lacked monitors or telemetry coverage, both of which result in significant detection delays." / "Finding#11: 70% of incidents with no monitors were root caused to code bugs, i.e., it is inherently difficult to monitor regressions introduced due to code changes. ⇒ For code changes, we should improve testing rather than relying on monitoring."
- URL:https://www.microsoft.com/en-us/research/wp-content/uploads/2022/09/3542929.3563482.pdf (DOI 10.1145/3542929.3563482)
- 日期:2022-11(SoCC '22)
- 来源类型:PR(Microsoft 自研)
- 承重:是(埋点缺口 + 客户先发现比例)
- 叙事:B
- 注:「29%」的分母存在歧义——原文句式为「其余 45% 中 29%」,结合 55+29+10+6=100 应理解为占全部事故的 29%。样本仅一个产品、仅高严重度。

## D18 Microsoft 全公司口径:96.7% 事故由监控检出,但「漏检」的一年近千条修复项中 >40% 是根本没有相关监控
- 论断:Ganatra 等(ESEC/FSE 2023 industry)对 Microsoft 306 个服务 2022 年事故统计:96.7% 由监控检出(其余为客户或内部工程师报告)。对 2022 年 973 条与监控相关的 postmortem 修复项(人工标 200 条 + 伪标签,伪标签准确率 72.9%)分析:漏检中 >40% 是没有相关监控,30% 是监控逻辑错误或缺信号/遥测;27% 的漏检事故导致 outage 或客户影响。论文把「被 OCE 调查比例 <10%」的监控定义为不可行动。
- 原文:"While majority (96.7%) of the incidents were detected by monitors, we still observe several human (either by customers or internal engineers) reported incidents." / "We observe that for more than 40% of the cases a relevant monitor was not present, whereas for 30% of the cases, existing monitors have either incorrect logic set up or missing appropriate signals or telemetry data." / "We observe that a significant portion (27%) of these miss-detected incidents lead to outages or customer impacts." / "We assume that a monitor is non-actionable if less than 10% of its generated incidents are investigated by OCEs."
- URL:https://jonathanmace.github.io/papers/ganatra2023detection.pdf ;https://www.microsoft.com/en-us/research/?p=990273
- 日期:2023-12(ESEC/FSE '23)
- 来源类型:PR(Microsoft 自研)
- 承重:是
- 叙事:A(绝大多数事故由监控先发现)+ B(漏检主因是没埋点)
- 注:96.7% 的分母是全部严重度事故(含大量监控自动生成的低严重度事故),与 D17 的高严重度 55% 口径不可直接比较。

## D19 GenAI 服务:38.3% 事故由人发现(其他服务 13.7%),监控误报率 11.0%(其他 3.8%)
- 论断:Yan 等(HUST/UIUC/Microsoft,2025)基于 Microsoft IcM 四年数据比较 GenAI 云服务与其他服务:GenAI 事故人报比例 38.3% vs 其他 13.7%;监控检出事故中误报率 11.0% vs 3.8%。作者解释:45.9% 的 GenAI 服务仍在开发/预览期,监控沿用旧框架不贴合新场景(如推理质量下降多由用户报告)。
- 原文:"GenAI cloud services experience a higher rate of incidents detected by humans (38.3%) compared to other services (13.7%) rather than automated monitors. Also, there is a higher false alarm rate for GenAI (11.0%) versus other services (3.8%)"
- URL:https://arxiv.org/abs/2504.08865 (v2 2025-08-14)
- 日期:2025-04(v1)/2025-08(v2)
- 来源类型:PR 预印本(Microsoft 合作)
- 承重:是(新型故障=新盲区;且是 2025 最新数据)
- 叙事:B
- 注:13.7% 是「其他服务」在同一时间窗、同标准下的对照组,与 D18 的 3.3%、D17 的 45% 都是不同样本/严重度口径。

## D20 Microsoft Gandalf:部署安全检测 precision 92.4–94.9%,但 recall 的分母是「高影响事故」而非全部坏发布
- 论断:Gandalf(NSDI 2020,Azure)关联故障信号与正在进行的发布,决定放行/停止。2018-01 至 2018-11 数据面捕获 155 个关键故障,precision 92.4%、recall 100%——recall 的定义是「没有 Sev0–2 高影响事故由坏发布引起」;控制面 1200+ 次区域级部署 precision 94.9%、recall 99.8%(报 39 起、2 起误报、漏 2 起;漏报原因:日志不全、组件抛泛化超时)。检测延迟:流式层约 5 分钟、批处理层约 3 小时;存在发布后 24–72 小时才出现的潜伏问题(有案例在发布 32 小时后检出)。误报集中在 Stage/Canary 环境。
- 原文:"It achieves 92.4% precision and 100% recall (no high-impact service outages in Azure Compute were caused by bad rollouts) for data-plane rollouts. For control-plane rollouts, Gandalf achieves 94.9% precision and 99.8% recall." / "Gandalf can make decisions in about 5 minutes end-to-end on the speed layer, and in about 3 hours on the batch layer." / "Gandalf filed 39 incidents and only 2 of them are false alarms."
- URL:https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- 日期:2020-02(NSDI '20)
- 来源类型:PR(Microsoft 自评)
- 承重:是(反方最强证据之一)
- 叙事:A(大厂检测器有效)+ N(recall 口径)
- 注:与 canary/回滚线可能重叠;本线只取检测指标。

## D21 Gandalf 对「测试漏掉什么」的一手归因
- 论断:Azure 认为即使经过评审与充分测试,仍有 bug 因测试与生产在集群规模、硬件 SKU、OS/库版本、不可预测负载、复杂组件交互上的差异而漏过;且有内存泄漏等发布数小时后才出现的潜伏问题。与 FBDetect(D08)、Teams 研究(D17 Finding#11)共同构成「离线漏检的共性」:环境差异、规模/负载、时间延迟、依赖交互。
- 原文:"some bugs could remain uncaught due to the discrepancies between testing and production environment in cluster size, hardware SKU (stock keeping unit), OS/library versions, unpredictable workloads, complex component interactions, etc."
- URL:同 D20
- 日期:2020-02
- 来源类型:PR(Microsoft)
- 承重:中
- 叙事:N

## D22 Walmart AIDR:MTTD 减少「7 分钟以上」,但覆盖 63% 重大事故、无基线 MTTD
- 论断:Walmart(ASPLOS'24 AIOps workshop)3 个月验证期,3000+ 模型服务 25+ 团队,覆盖 63% 重大事故,MTTD 减少 7 分钟以上;4 个案例客户中 3 个为 100% 事故覆盖(分母分别仅 4/3/3 起),Operations 团队仅 56%(27/48)、MTTD 减 7.2 分钟、噪声降 91%(相对非 AIDR 告警)。论文未给出基线 MTTD,故无法换算相对缩短比例。单模型权衡:XGBoost recall 96% 但 precision 10%;ARIMA precision 98% 但 recall 53%。
- 原文:"covering 63% of major incidents and reducing the mean-time-to-detect (MTTD) by more than 7 minutes." / "While an XGBoost classifier yields a superior recall of 96%, it severely suffers from a low precision of 10%. In contrast, a regression-based next-time-point-prediction model ARIMA yields an impressive precision of 98% while it suffers from a low recall of 53%."
- URL:https://arxiv.org/abs/2404.16887
- 日期:2024-04
- 来源类型:PR(workshop,Walmart 自评)
- 承重:是(为数不多的检测段前后对比)
- 叙事:A(有前后对比)+ B(样本小、无基线)

## D23 SCWarn:作者报 F1 0.95、MTTD 降 20.4–60.7%;第三方复现 F1 0.45–0.73
- 论断:SCWarn(FSE 2021,基于某大型商业银行数据)识别坏软件变更,摘要报平均 F1 0.95、MTTD 降低 20.4%–60.7%。在 AnoFusion(KDD 2023)的两个微服务故障注入数据集上复现,SCWarn precision/recall/F1 为 0.547/0.425/0.447 与 0.633/0.891/0.734。说明作者自有数据上的数字不迁移。
- 原文:"achieving 0.95 F1-score on average and reducing MTTD (mean time to detect) by 20.4%∼60.7%."(SCWarn 摘要)/ AnoFusion Table 3 行 "SCWarn [46] ✓ ✓ 0.547 0.425 0.447 0.633 0.891 0.734"
- URL:https://2021.esec-fse.org/details/fse-2021-papers/97/Identifying-Bad-Software-Changes-via-Multimodal-Anomaly-Detection-for-Online-Service- (DOI 10.1145/3468264.3468543);https://arxiv.org/abs/2305.18985
- 日期:2021-08;2023-08
- 来源类型:PR(两者均为学术 + 业界合作;AnoFusion 为竞品方法作者,有利益)
- 承重:中
- 叙事:B
- 注:AnoFusion 也用 best F1(最优阈值),复现数字同样偏乐观。

## D24 运维人员自己接受的精度门槛只有 0.66
- 论断:Opprentice(IMC 2015,清华 + 百度)合作的运维人员给出的可接受准确率偏好是 recall ≥ 0.66 且 precision ≥ 0.66——即愿意接受约 1/3 告警为误报、1/3 异常被漏。论文称该值来自运维用其他检测器的经验,且精度与召回常相冲突。
- 原文:"the operators we worked with specified “recall ≥ 0.66 and precision ≥ 0.66” as the accuracy preference" / "As anomalies are relatively few in the data, it is difficult for those detectors to achieve both high recall and precision."
- URL:http://conferences2.sigcomm.org/imc/2015/papers/p211.pdf
- 日期:2015-10(IMC '15)
- 来源类型:PR
- 承重:中
- 叙事:N/B

## D25 Google SRE:每个 page 都应可行动;频繁 page 会让人忽略真告警
- 论断:Google SRE 书「Monitoring Distributed Systems」把告警疲劳定性为可靠性风险:page 太频繁时值班者会怀疑、略读甚至忽略告警,真 page 可能被噪声掩盖。该书为原则陈述,未给出可行动告警比例实测。
- 原文:"Every page should be actionable." / "When pages occur too frequently, employees second-guess, skim, or even ignore incoming alerts"
- URL:https://sre.google/sre-book/monitoring-distributed-systems/
- 日期:2016(O'Reilly 出版;在线版持续更新)
- 来源类型:OF(从业者原则,非实测)
- 承重:否
- 叙事:B

## D26 底率自算:低底率下高精度检测器也会被误报淹没
- 论断(自算示例,非引用数据):设每天 1000 次发布,坏发布率 1%(10 次),检测器 TPR 95%、每次发布误报率 FPR 2% → 真报 9.5、误报 19.8,precision = 9.5/29.3 ≈ 32%;FPR 降到 0.5% → 误报 4.95,precision ≈ 66%(恰好是 D24 运维门槛);FPR 0.1% → precision ≈ 91%。若每次发布同时看 100 个独立指标、每个指标单独 FPR 0.1%,则每次发布至少一个误报的概率 = 1−0.999^100 ≈ 9.5%,整体 precision 跌回 ≈ 9.5/(9.5+94) ≈ 9%。实证对照:FBDetect FrontFaaS 一个月原始 change point 396 万,最终报 217 条(D03/D04)——生产检测器的主要工程量在压误报,而不是提高灵敏度。
- 原文:无(自算;FBDetect 数字见 D03)
- URL:—
- 日期:2026-10(本线自算)
- 来源类型:自算
- 承重:中(说明性)
- 叙事:B

## D27 「检出 ≠ 处置」:被检出的回归也会因无人行动变成事故
- 论断:FBDetect 一个月 217 条报告中 24 条无人处理(11%);2023 年 FrontFaaS 4 起性能事故中 2 起已被检出但未被及时处理。Gandalf 案例中,发布经理基于经验认为告警无关而忽略,后被确认为真回归。说明检测段的效果上限受告警信任与处置链路约束——TTD 缩短不自动转化为影响缩短。
- 原文:"did not act on the remaining 24." / "two were detected by FBDetect but were not acted upon by developers in time."
- URL:https://tangchq74.github.io/FBDetect-SOSP24.pdf
- 日期:2024-11
- 来源类型:PR(Meta)
- 承重:中
- 叙事:B

## D28 Meta 2024 年中起把发布前测试与生产检测串成闭环(TOCS 2025)
- 论断:FBDetect + ServiceLab 的 TOCS 扩展版(2025-12)称,自 2024 年中起用 ServiceLab 持续跑基准、喂给 FBDetect 检测,再由 ServiceLab 对嫌疑变更二分定位;渐变回归一次可能有 5000–20000 个嫌疑变更。称节省「数万台机器」(厂商口径,无误报/延迟新数据)。论文也承认发布前测试固有局限:有缺陷的代码或配置变更会漏到生产。
- 原文:"pre-production testing cannot fully reproduce the scale and complexity of the production system. As a result, some buggy code or config changes slip through." / "Typically, FBDetect can report 5,000 to 20,000 changes as suspected for one gradual change."
- URL:https://yangwang83.github.io/papers/tinyregression-tocs.pdf (DOI 10.1145/3785504)
- 日期:2025-12(ACM TOCS)
- 来源类型:PR(Meta 自评;节省数字为厂商口径)
- 承重:中
- 叙事:A/N

---

## 未找到 / 证据缺口(记录搜索角度)
- LinkedIn ThirdEye、Uber uVitals:官方博客只描述机制(反馈回路、分组降噪),未找到带分母的 precision/recall 或前后 TTD 数字。
- Google:未找到公开的生产异常检测器 precision/TTD 实测;SRE 书只有原则。
- 「可行动告警占比」的同行评审实测:未找到 2024–2026 年 IT 运维的一手数据;医疗报警研究(PICU 13% 可行动)与厂商报告(「<18% 被处理」)口径不可迁移,未收。Huawei Cloud 告警反模式论文(DSN 2022, arXiv 2204.09670)只有 18 人问卷百分比,未收为承重。
- 「AI 把 TTD 缩短多少」:带基线的前后对比极少——只有 Walmart(+7 分钟,无基线)、SCWarn(20.4–60.7%,作者自有银行数据)。没有找到 LLM 检测器在生产中的 TTD 前后对比。

## 交叉口径问题
1. 「检出率」三种分母混用:FBDetect 以 4 起已记录事故为真值(D05);Gandalf 以「无 Sev0–2 由坏发布引起」为 recall(D20);学术基准以人工标注段为真值且常用 PA(D09/D12)。三者不可横比。
2. 「监控检出比例」三套口径:Teams 高严重度 55%(D17)、Microsoft 全服务全严重度 96.7%(D18)、GenAI 对照组 86.3%(D19)。严重度越高,人报比例越高——引用时必须带严重度与服务范围。
3. FBDetect 的 0.005% 是 gCPU 子程序级绝对阈值(性能回归),不能当作「能检出 0.005% 错误率的正确性故障」;其唯一已知漏报导致的是 0.015% 错误率(D05)。
4. FBDetect 的「13 年一次误报」是 per-developer 摊薄指标;按报告计,确认子集 precision ≈ 70%(49/70),EGADS 对比集 ≈ 71%(76/107)。
5. TTD 证据稀缺且多为「检测器运行周期/窗口」而非实测分布:FBDetect 小时级窗口(D02)、Gandalf 5 分钟/3 小时(D20);Walmart、SCWarn 报 MTTD 差值但无基线或分母小。Teams 研究的 TTD 为归一化值(中位数=1),无绝对时间。
6. 「F1 提升 20%/28.3%」(SR-CNN、Argos)是相对提升,绝对 F1 在生产数据上约 0.5(D11)。
7. Donut/AnoFusion 的「best F1」= 测试集上事后最优阈值,部署时不可得;与固定阈值 F1 不可比。
8. MTTR/MTTM 不得混作检测证据:FBDetect RCA 35%(D07)属定位段;Gandalf「部署时间减半」属发布速度,不是 TTD。
9. 时间新鲜度:2025–2026 年的新证据主要是批评性(D15、D16、D19);支持性生产数字(Gandalf 2018 数据、FBDetect 2023 数据)都较旧。
