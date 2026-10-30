# Part 2 锁定论断：大厂发布检测器自评、canary 方法与局限、告警信任

> 研究题目：AI 能接住坏发布吗：离线验证漏掉的问题，上线后多快被发现
> 锁定日期：2026-10-30｜范围：G05、G06、G07、G08、G10 + R3 双席审计（R3-X 反证、R3-M 方法，方法席有否决权）
> **本文件是成文的唯一依据。** 文中没有出现的数字不得写进文章；出现在文末否决清单里的数字不得承重。

合并规则（已执行）：
- 三票（V 逐字席 / R 反证席 / K 口径席）不一致时，取最保守、最窄的口径，并在「修正记录」里注明分歧。
- 任何一票判为「核不到原文 / 未验证 / 只能证到未见」的数字，降为「未验证」。
- R3-M 否决的数字列入文末否决清单；R3-M 降级的数字按降级后的口径锁定。
- 证据分级五档：**多源证实**（两个以上独立来源同向）/ **单源已核**（一手原文逐字核过，单一来源）/ **方向存争**（席位之间对方向或口径有实质分歧）/ **厂商口径**（系统所有者自述，无方法或分母）/ **未验证**。
- 通用前提：本 part 所有大厂数字都出自系统所有者对自家生产系统的自评，没有第三方用生产数据复测过。凡未另注，引用时一律带上「某厂自评」。

术语口径：
- **TTD**：坏发布开始生效 → 被检测器判出的时间。
- **决策延迟 / 流水线延迟**：数据进入检测器 → 出判定的处理时间。它不是 TTD。
- **观测窗口 / bake time**：设计参数，规定检测器等多久。它不是实测的 TTD，也不是「问题多晚显现」的上界。

---

## G05 Microsoft Gandalf（NSDI 2020）

一手来源统一为：Li et al., "Gandalf: An Intelligent, End-To-End Analytics Service for Safe Deployment in Cloud-Scale Infrastructure", NSDI 2020, https://www.usenix.org/system/files/nsdi20-paper-li.pdf （作者 11 人中 10 人来自 Microsoft，自评自家 Azure Compute 生产系统）。辅助来源：Azure 博客 "Advancing safe deployment with AIOps—introducing Gandalf"（只有口径，无任何检出数字）。

### L05-1 数据面：155 个关键故障、precision「约 92%」、recall 100% 是代理口径
- **锁定表述**：Microsoft 自报，在论文所称的「8 个月」窗口（论文标注为 2018 年 1 月至 11 月，日历跨度与 8 个月不符，论文自身前后不一致）里，Gandalf 在 Azure Compute 数据面 rollout 的早期阶段「捕获了 155 个关键故障」，precision 作者报为 92.4%。这个 92.4% 无法从 155 重算（155 作分子或分母都凑不出 92.4% 的整数比），告警总数和误报数都未披露，所以只能写「约 92%，分母未披露」。155 是否全为真阳性，论文没有说明。论文所称的「100% recall」，操作定义是「观察期内没有 Sev0–2 高影响事故由坏发布引起」：漏报只有升级成 Sev0–2 事故才会被计入，分母未知。它应改述为「观察期内作者没有记录到由坏发布引起的 Sev0–2 事故」，不能当作召回率。
- **证据分级**：厂商口径（同行评审，但为系统所有者自评、单一窗口、无独立复测）。
- **主要一手来源**：Gandalf NSDI 2020，§6 与摘要，https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- **修正记录**：原稿写「8 个月、precision 92.4%、100% recall（以无 Sev0-2 为代理）」→ 现在写「论文自称 8 个月（日历跨度不符）、precision 约 92%（不可重算）、recall 100% 作废，只能改述为『未记录到由坏发布引起的 Sev0–2』」。分歧：K 席判 C01 HOLDS，V 席、R 席判 CORRECTED，取 CORRECTED；R3-M 否决「100% recall」作为召回数字，并把 92.4% 降为「约 92%」。「低影响漏报不在分母里」是调研员推论（V 席、R 席），成文要写成推论。
- **禁止写法**：「Gandalf 数据面 recall 100%」「零漏报」「8 个月内拦下 155 个坏发布」「precision 92.4%」（不加「约」和「分母未披露」）；不得自行把窗口换算成 10 个月或 11 个月。

### L05-2 控制面：按论文自给计数，标准 recall = 37/39 ≈ 94.9%；99.8% 的分母未说明
- **锁定表述**：论文称 Gandalf 对「1200+ 次」控制面区域级部署做了放行或停止的决策，共提交 39 个 incident，其中 2 个误报，另漏掉 2 个真问题。按这些计数：TP = 37，FP = 2，FN = 2，precision = 37/39 ≈ 94.9%，标准 recall = TP/(TP+FN) = 37/39 ≈ 94.9%（n = 39，Wilson 95% CI 约 83%–99%）。论文报告的「recall 99.8%」无法由标准 recall 定义得到，论文也没有给出计算式。数值上，它与「1 − 漏报/全部部署」≈ 1198/1200、specificity 1159/1161、NPV 1159/1161 都吻合（FP = FN = 2 时三者相同），所以它的分母无法判定。控制面的时间窗论文没有明确给出，不能套用数据面的 2018-01 至 2018-11。两个漏报的原因：一是日志不全，二是故障组件抛出通用 timeout 而不是特定错误。
- **证据分级**：计数为单源已核（厂商自评）；「99.8% 的定义」为未验证。
- **主要一手来源**：Gandalf NSDI 2020 §6，https://www.usenix.org/system/files/nsdi20-paper-li.pdf ；R3-M 审计重算（Wilson CI）。
- **修正记录**：原稿写「99.8% 与 (1200−2)/1200 吻合，疑似分母是全部部署」→ 现在写「标准 recall 37/39 ≈ 94.9%；99.8% 的分母未说明，与 1−FN/总部署、specificity、NPV 三者数值都吻合，无法判定」。分歧：R 席判 HOLDS，并认为「疑似全部部署」在算术上成立；V 席、K 席判 CORRECTED，指出那只是三种候选之一。取 CORRECTED。R3-M 否决 99.8% 作为 recall。
- **禁止写法**：「Gandalf 控制面 recall 99.8%」（不论是否加注，都不得把 99.8% 称作 recall）；「99.8% 的分母就是全部部署」；「控制面数据也来自 2018 年 1–11 月」。

### L05-3 「5 分钟 / 3 小时」是决策流水线延迟，不是 TTD
- **锁定表述**：Gandalf 有两层分析。流式层（speed layer）只看每次部署前后各 1 小时的故障信号，每次部署端到端约 5 分钟出决策；批处理层（batch layer）看 30 天窗口，约 3 小时出决策，用来捕获发布 1 小时之后才出现的潜伏故障。这两个数是数据处理加决策的流水线延迟。论文自己说，即使把流式层延迟压到 10 秒，Gandalf 仍要等证据积累。论文没有报告「坏发布生效 → 检出」的 TTD 分布；文中案例显示，故障信号可以在发布后 24–72 小时才出现（案例 III），也有「发布 32 小时以后才检出」的潜伏问题（Figure 8）。「Azure 多数灾难性问题在发布后 1 小时内出现」是作者断言，没有给比例。「部署总时长减半以上」（Figure 14）的对照对象是 Gandalf 之前「组件 watchdog 加大量人工邮件审批」的流程，衡量的是发布速度，不是检测速度。
- **证据分级**：单源已核（厂商自评）。
- **主要一手来源**：Gandalf NSDI 2020（§4–§6、Figure 8、Figure 14），https://www.usenix.org/system/files/nsdi20-paper-li.pdf ；30 天窗口另见 Azure 博客 "Advancing safe deployment with AIOps—introducing Gandalf"。
- **修正记录**：原稿写「TTD（从部署到 go/no-go）：流式约 5 分钟，批处理约 3 小时；只看部署前后 1 小时」→ 现在写「决策流水线延迟约 5 分钟 / 3 小时，不是 TTD；只看 ±1 小时的仅限流式层，批处理层看 30 天」。三席一致判 CORRECTED；R3-M 否决把 5 分钟当 TTD。
- **禁止写法**：「Gandalf 5 分钟发现坏发布」「Gandalf 的 TTD 是 5 分钟」「Gandalf 只看发布后 1 小时」「Gandalf 让检测速度快了一倍」。

### L05-4 99.2% 的分母是「被检出的可疑 rollout」，不是全部坏发布
- **锁定表述**：论文 §5.2 / Figure 15 显示，被 Gandalf 判为可疑的数据面 rollout 中，99.2% 在 Stage/Canary/Pilot 阶段被拦，0.8% 在生产早期被拦。分母是被检出的可疑 rollout（含误报），是以检出为条件的比例，不是对全部坏发布的拦截率。论文结论段把它改写成 "blocked 99.2% of the bad rollouts"，偷换了分母，这句不得引用。0.8% 与 155 构不成整数比，说明 Figure 15 的分母不是那 155 个关键故障，两组数不能互算。误报多集中在 Stage 和 Canary，原因是这些环境的故障信号噪声更大。潜伏问题会造成错误归责：一次 agent 更新误删了重要目录，后来客户的 GuestOS 更新碰到该目录触发故障，Gandalf 错怪了 GuestOS 部署。
- **证据分级**：单源已核（厂商自评）。
- **主要一手来源**：Gandalf NSDI 2020 §5.2、Figure 15、结论段，https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- **修正记录**：原稿写「分母 = 被检出的可疑 rollout」（正确）→ 现在补上「论文结论段措辞偷换了分母，不得引用；不能与 155 互算」。分歧：V 席、K 席判 HOLDS，R 席判 CORRECTED，取 CORRECTED；R3-M 降级为「已检出的问题中 99.2% 发生在生产前阶段」。
- **禁止写法**：「Gandalf 在进入生产前拦下 99.2% 的坏发布」；用 0.8% × 155 推算任何数字。

### L05-5 组件级 watchdog 的三类漏检，与测试—生产差异
- **锁定表述**：Microsoft 在论文动机部分写到，即使经过评审和充分测试，仍有 bug 会因测试环境与生产环境在集群规模、硬件 SKU、OS/库版本、不可预测的负载、复杂组件交互上的差异而漏到生产。Gandalf 之前的组件级 watchdog 会漏掉三类问题：局部轻微但跨集群或区域严重的问题；发布数小时后才出现的潜伏问题（如内存泄漏）；只在与其他组件交互时出现的问题（如跨组件 API 契约违背）。这是对 Gandalf 之前组件级 watchdog 的动机陈述，不是 Gandalf 自身的漏检分析。案例 III：一次网络 agent 的 rollout 升级了 NIC 固件和驱动，固件升级脚本漏掉了一个硬件版本，导致旧固件与新驱动冲突，部署后 24–72 小时 OS 才崩溃，Gandalf 在 Canary 阶段发出了 Sev2 告警。这是潜伏问题被检出的成功案例，n = 1。
- **证据分级**：单源已核（厂商自评、定性）。与 FBDetect、Configerator、AWS 合看后，「离线漏检的共性是环境差异、规模/负载、时间延迟、依赖交互」可升为多源证实（几家都是厂商自述）。
- **主要一手来源**：Gandalf NSDI 2020 §1–§2、案例 III，https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- **修正记录**：原稿把三类漏检写成一般性结论 → 现在写明是「Gandalf 之前组件级 watchdog 的漏检」，案例 III 是检出成功案例。D21 三席均判 HOLDS；C05、C11 因为其他细节判 CORRECTED。「与 FBDetect、Teams 构成共性」是跨源综合，要标为综合判断，不能当 Gandalf 的结论。
- **禁止写法**：「Gandalf 会漏掉跨组件问题」（这是对 watchdog 的描述）；「案例 III 是 Gandalf 漏报」。

### L05-6 人会推翻正确的自动 no-go（Gandalf 案例 I）
- **锁定表述**：在案例 I 中，CRP 团队凭以往经验认为 Gandalf 报出的故障与 CRP rollout 无关，release manager 据此直接要求绕过 no-go 决定。随后 rollout 推进到 Pilot，Gandalf 再次给出 no-go，经深入调查才确认是 CRP 的回归；hotfix 部署时，Pilot 区已有客户报告了相关问题。这说明自动停发布机制可以被人覆盖，而论文没有报告覆盖率。案例 n = 1，是作者挑选的案例。
- **证据分级**：单源已核（案例级，n = 1）。
- **主要一手来源**：Gandalf NSDI 2020 案例 I，https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- **修正记录**：原稿写「CRP 团队凭经验认为告警无关，要求绕过 no-go」→ 现在写「CRP 团队认为无关，**release manager** 要求绕过」。G05 与 G10 两次出现，六票中有五票判 CORRECTED（G05-K、G10-K 判 HOLDS 但同样要求改主语）。
- **禁止写法**：「CRP 团队要求绕过 no-go」「发布经理凭经验认为告警无关」；「Gandalf 的 no-go 常被推翻」（没有覆盖率数据）。

---

## G06 Google CAS / SRE Workbook / Kayenta / Spinnaker judge

### L06-1 CAS 每天「评估」数十万次生产变更；它只判定，不执行
- **锁定表述**：Google 自述，中心化的 Canary Analysis Service（CAS）每天评估数十万次生产变更，对象包括新版二进制、配置变更、数据集变更等。这是评估次数，不是拦截次数；原文没有给出其中失败、拦截或真坏变更的数量。CAS 是纯被动观察者，自己不改动生产系统；判定由 rollout 工具调用，暂停或回滚由 rollout 工具执行。「被 CAS 评估」不等于「所有变更都经过分阶段和 canary」：Google Cloud 2025-06-12 的事故中，触发故障的策略数据在数秒内复制到全球（见 L06-9）。
- **证据分级**：厂商口径（数量级为 Google 工程师自述，ACM Queue 非同行评审）。
- **主要一手来源**：Davidovič & Beyer, "Canary Analysis Service", ACM Queue 16(1), 2018，https://sre.google/static/pdf/canary_analysis.pdf
- **修正记录**：原稿与锁定一致。三席均判 HOLDS；R 席补充了「评估 ≠ 全部变更都分阶段」的限定。
- **禁止写法**：「Google 每天拦下数十万次变更」「CAS 自动回滚」「Google 所有变更都经过 canary」。

### L06-2 CAS 的判定方法：canary 与 control 对比，纯相对比较在零值和小绝对量上表现极差
- **锁定表述**：CAS 把 canary 组和 control 组的时间序列做对比。检验方法有的有明确统计来源（如 Student t 检验），有的是模仿人眼判断的自定义启发式；用户选自动配置时，评估器可能跑几十个参数不同的检验。model server 会学习某类变更的常态，coordinator 在给出总体结论时，会忽略那些被预测为常态失败的检验结果。原文承认，这些检验是纯相对比较（例如「指标增幅不超过 5%」的 t 检验），当指标通常为 0，或者相对变化大但绝对量小到服务方并不在意时，表现「极差」。
- **证据分级**：单源已核（Google 自述，定性）。
- **主要一手来源**：CAS，ACM Queue 2018，https://sre.google/static/pdf/canary_analysis.pdf
- **修正记录**：无实质修正（三席均判 HOLDS）。
- **禁止写法**：「CAS 用 t 检验判定」（只写一种方法）；把这段写成实测误报数据。

### L06-3 自适应学习会把危险行为常态化；用户会无视 canary 失败
- **锁定表述**：CAS 的在线行为学习假设坏行为很少见。如果用户在异常确实危险时反复重试推送，CAS 最终会把这种行为当成新常态，不再告警。原文紧接着说，随着自动化变得更成熟可靠，用户不那么倾向盲目重试，这一风险会减轻，也可以用离线流程补充。CAS 还出过用户无视 canary 失败、推送坏版本导致的事故，作者认为很多此类问题的根源是用户不信任复杂自动化。原文没有给出这类事故的数量。
- **证据分级**：单源已核（定性，无计数）。
- **主要一手来源**：CAS，ACM Queue 2018，https://sre.google/static/pdf/canary_analysis.pdf
- **修正记录**：原稿缺少缓解条件 → 现在补上「风险随自动化成熟而减轻」。分歧：G06 中 V 席、K 席判 HOLDS，R 席判 CORRECTED；G10 中 V 席、K 席判 HOLDS，R 席判 CORRECTED。取 CORRECTED。引用「不信任」时，要同时说明 CAS 原文对拦截价值有正面粗估（L06-4），不能只引负面。
- **禁止写法**：把「常态化」写成无条件的漏洞；「CAS 多次因用户无视而出事」（没有次数）。

### L06-4 CAS 的拦截价值：Google 只给了粗估「likely prevented hundreds」
- **锁定表述**：Google 没有公布 CAS 的检出率或拦截率，并明说精确的影响分析很难：如果 CAS 真的防住了一次故障，就没法知道那次故障本来有多大。团队考虑过故意放过一部分失败判定做 A/B，但认为影响故障大小的因素太多，得不到清晰信号，于是放弃；最终采用「近失分析」，即翻查 Google 的大型 postmortem，找出 CAS 本可拦住却没拦住的故障。在较同质的部门子集上分析，「发现了一些粗粒度信号」。论文结论给出的是**粗估**：影响分析显示，CAS「可能避免了数百起值得写 postmortem 的故障」，而不用 CAS 的团队 postmortem 率「明显更高」。两者都没有给分母、方法细节或置信区间；后者是用与不用 CAS 的团队之间的相关比较，用不用 CAS 不是随机分配的，存在团队自选择偏差。
- **证据分级**：厂商口径。
- **主要一手来源**：CAS，ACM Queue 2018（"Impact analysis" 一节与结论段），https://sre.google/static/pdf/canary_analysis.pdf
- **修正记录**：原稿写「Google 没有、也认为难以给出 canary 检出率或拦截价值的可靠数字」→ 现在写「Google 没有公布检出率；自评粗估『可能避免了数百起 postmortem 级故障』，不用 CAS 的团队 postmortem 率更高，无方法、无分母，有自选择偏差」。R 席、K 席判 CORRECTED（原稿与原文结论相反），V 席判 HOLDS，取 CORRECTED。
- **禁止写法**：「Google 承认无法量化 CAS 的价值」「Google 没给任何数字」；反过来也不得写「CAS 防住了数百起故障」（不加「自评」「粗估」「可能」）；「不用 CAS 的团队事故更多，说明 CAS 有效」（相关，不是因果）。

### L06-5 指标选择：弱相关指标效果差；「超精确」配置造成 toil
- **锁定表述**：Google 的经验是，使用弱相关指标会导致结果很差。除非做过同等细致的数据分析（Google 有些团队做过，并据此使用大量指标），只用少数关键指标效果要好得多。单个组件的 canary 即便严重失常，对整个服务 SLO 的影响也可能很小，所以需要组件级指标。追求「完美准确」的 canary 配置往往失败：僵硬的配置会阻断行为变化本属可接受的发布，在常规发布中造成大量 toil。
- **证据分级**：单源已核（Google 自述，定性）。
- **主要一手来源**：CAS，ACM Queue 2018，https://sre.google/static/pdf/canary_analysis.pdf
- **修正记录**：原稿写「只用少数关键指标效果好得多」→ 现在补上限定「除非做过同等细致的数据分析」。V 席判 CORRECTED，R 席、K 席判 HOLDS 但同样要求补限定，取 CORRECTED。
- **禁止写法**：「指标越少越好」（不带限定）。

### L06-6 SRE Workbook 的 canary 设计注意事项（示例与指南，不是实测）
- **锁定表述**：Google SRE Workbook 第 16 章列出几条设计约束。(a) 性能缺陷通常只在高负载下显现，在低峰期部署很可能触发不了。(b) 示例算术：canary 占 5% 流量、错误率 20%，看整体的监控只会看到 1% 的错误率，可能与其他错误源无法区分，所以必须把 canary 组和 control 组分开看。这是 workbook 用演示程序注入错误的示例，不是生产实测。(c) 对于请求多样、功能各异的系统，只收到少量请求就结束 canary 得不到有用信号；但对于「完全坏掉」这类关键问题，不需要很大的 canary 群体，请求越同质，所需流量越少。(d) 时间是观测指标变化的最大来源之一，before/after 式 canary 难以评估性能退化。(e) 持续部署时（例如每天 20 次）canary 时长必须短得多；Google 强烈建议同一时间只跑一个 canary。
- **证据分级**：厂商口径（指南与示例）。
- **主要一手来源**：Google SRE Workbook, "Canarying Releases"，https://sre.google/workbook/canarying-releases/
- **修正记录**：原稿写「只收到少量请求就结束 canary 不提供有用信号」→ 现在限定为「请求多样的系统」，并补上「严重故障小样本即可发现」。V 席、R 席判 CORRECTED，K 席判 HOLDS 但同样注明了限定，取 CORRECTED。
- **禁止写法**：「Google 数据显示 5% canary 的 20% 错误在全局只剩 1%」（这是示例算术）；「canary 流量太小一律无效」。

### L06-7 噪声 canary 会被禁用；检测更快不等于恢复更快
- **锁定表述**：Workbook 指出，资源用量上升不一定影响服务，如果拿它做判据，canary 会时好时坏、噪声很大，最后被运维禁用或无视，canary 也就失去意义。Workbook 还论证，before/after 式 canary 也许能更快发现问题，但总恢复时间可能仍然可观，与小 canary 相近。这是指南中的推理（原文用的是 "may"），不是实测；可以写作「Google 指南的论证」。它支持「TTD 与恢复时间要分开看」。Google Cloud 2025-06-12 事故提供了同向事例：SRE 2 分钟内开始分诊、10 分钟内定位根因，但部分区域完全恢复用了约 2 小时 40 分钟。
- **证据分级**：厂商口径（Workbook 论证 + GCP 事故报告，都是 Google 自家材料）。
- **主要一手来源**：SRE Workbook "Canarying Releases"，https://sre.google/workbook/canarying-releases/ ；Google Cloud 事故报告 2025-06-12，https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW （仅 R 席核过原文）
- **修正记录**：原稿写「直接支持 TTD 与 MTTR 必须分开」→ 现在写「Google 指南的论证，非实测」。分歧：R 席拟借 GCP 事故升为多源证实，K 席定为厂商论证；两者都是 Google 自家材料，取保守的厂商口径。
- **禁止写法**：「Google 数据显示 before/after 检测更快但恢复不更快」。

### L06-8 Kayenta：1% 流量是举例，「每天数千次判定」是 2018 年的预期
- **锁定表述**：Google 与 Netflix 于 2018-04-10 联合发布开源的自动 canary 分析工具 Kayenta。基本思路是把一小部分生产流量（原文举例 1%）分别导给 canary 和一个新建的 baseline。baseline 与生产代码和配置相同，用来消除启动效应、缩小与 canary 的系统差异。通常各建 3 台实例。逐指标做统计检验后按权重聚合成 0–100 分：success 放行；marginal「可以」触发人工审批路径，是否转人工取决于配置；failure 触发回滚。「到年底预计每天做数千次 canary 判定」是 2018 年 4 月对当年年底的**预期**，不是实测。这篇发布稿的署名作者是 Google 的产品营销与 PM。
- **证据分级**：厂商口径（营销博客加预期值）。
- **主要一手来源**：Google Cloud Blog, "Introducing Kayenta"，https://cloud.google.com/blog/products/gcp/introducing-kayenta-an-open-automated-canary-analysis-tool-from-google-and-netflix
- **修正记录**：原稿写「典型配置约 1% 流量；marginal 转人工」→ 现在写「1% 是举例；marginal 是否转人工取决于配置」。V 席判 CORRECTED，R 席、K 席判 HOLDS 但同样做了小修，取 CORRECTED。
- **禁止写法**：「Kayenta 典型用 1% 流量」「Kayenta 每天做数千次判定」（不加「预期」）；「marginal 一律转人工」。

### L06-9 Spinnaker/Kayenta judge：低流量路径无数据默认不扣分；置信区间宽时大幅退化仍可判 Pass
- **锁定表述**：当前 Spinnaker 文档描述的默认 NetflixACAJudge 对每个指标单独做 Mann-Whitney U 检验，98% 置信度是硬编码常量，不可配置。一个指标被判为 High 或 Low 需要同时满足三个条件：98% 置信区间完全落在容差带之外；效应量超过 allowedIncrease/allowedDecrease 阈值；方向是被关注的方向。缺失数据的处理：默认情况下，canary 期间没有数据的指标被归为 Nodata，「不扣分也不加分」，但如果 ≥50% 的指标为 Nodata，整次判定失败；只有设置 `mustHaveData: true`，缺数据才计为失败；`nanStrategy: replace` 是把缺失值补成 0 再比较，canary 与 baseline 都为 0 时通常判 Pass，不能当作补救手段。所以「低流量路径上的错误指标在 canary 期间无数据会被放过」只限于少数指标缺数据的情况，这一机制说明是调研员的推断，文档本身没有这样表述。文档的官方示例 C 中，延迟上升 23%，超过了 allowedIncrease 1.2，但由于置信区间宽，仍判 Pass（文档原话说效应量阈值是「次级闸门」）。该页没有出现多重比较校正的说明，这只能证到「未见」，不能证明「没有」。文档没有版本日期，不能据此断定 2018 年 Kayenta 的行为也是如此。
- **证据分级**：单源已核（开源项目文档）；「低流量盲区的工具机制」属推断。
- **主要一手来源**：Spinnaker 文档 "How canary judgment works"，https://spinnaker.io/docs/guides/user/canary/judge/
- **修正记录**：原稿写「需 98% 置信且置信区间落在容差带之外；除非配置 mustHaveData/nanStrategy=replace」→ 现在写「需同时满足三个条件；只有 mustHaveData 会计失败，replace 补 0 通常判 Pass；≥50% Nodata 时整体失败」。V 席、K 席判 CORRECTED，R 席判 HOLDS，取 CORRECTED。
- **禁止写法**：「设 nanStrategy=replace 就能堵住低流量盲区」「Kayenta 没做多重比较校正」（只能写「文档未见说明」）；「Kayenta 2018 年就是这样判的」。

### L06-10 Google Cloud 2025-06-12：canary 只能验证被流量执行到的代码路径
- **锁定表述**：据 Google Cloud 的事故报告，出问题的代码变更经历过逐区域 rollout，但故障代码路径需要一次策略变更才会触发，所以在 rollout 期间从未被执行。之后触发它的策略元数据在数秒内复制到全球。这是一起单一事件，可以写作：「canary 和渐进发布只能验证被流量执行到的路径；不分阶段的数据或策略变更会绕过 canary」。
- **证据分级**：单源已核（一手事故报告；本 part 中只有 G06 的 R 席核过原文）。
- **主要一手来源**：Google Cloud Service Health 事故报告，2025-06-12，https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW
- **修正记录**：原稿没有这一条 → 由 G06-R 反证席补入。
- **禁止写法**：「Google 的 canary 失效了」（canary 本身按设计工作，只是代码路径没被执行）；把单一事件写成频率结论。

---

## G07 Netflix 序贯检验、Facebook Configerator 与持续部署、Azure/AWS 渐进发布

### L07-1 Netflix：canary 中反复「偷看」会让误报失控，序贯检验控制的是单个检验的误报
- **锁定表述**：Netflix 的作者指出，canary 中常见的做法是对累积数据反复跑固定样本量（fixed-n）检验。每多跑一次，I 类错误的概率就上升一点，误报增多会增加人工干预、降低交付节奏。他们提出基于 Howard & Ramdas 置信序列的序贯检验，可以连续监控同时严格控制 I 类错误，并给出检验停止时间和最大样本量的上界。这一控制针对的是单个检验。Lindon（Netflix）2026 年在 ERCIM News 上的署名文章泛论说，一次 canary 可能同时监控上百个指标，多重检验校正「不可避免」。所以单指标的误报控制不能直接推出整次 canary 的误报率受控。
- **证据分级**：单源已核（同行评审，Netflix 作者自评）。
- **主要一手来源**：Lindon, Sanden, Shirikian, "Rapid Regression Detection in Software Deployments through Sequential Testing", KDD 2022，https://arxiv.org/pdf/2205.14762v2 ；ERCIM News 145（2026-07-02）Lindon 署名文章（仅 G07 的 R 席检到）。
- **修正记录**：原稿与锁定一致，补上「单检验 ≠ 整次 canary」的限定（R 席）。三席均判 HOLDS。
- **禁止写法**：「序贯检验让 canary 误报可控」（不区分单检验和整次 canary）。

### L07-2 Netflix 两个案例：11.08 秒与约 65 秒（n = 2，自选，高事件率指标）
- **锁定表述**：Netflix 论文给出两个真实 canary 案例。案例一：一个软件 bug 让多种设备播放失败，以 SPS（成功起播事件）到达间隔为对象的序贯 p 值在 11.08 秒跌破 0.01。案例二：PlayDelay 性能回归约 65 秒跌破 0.01，阻止了该候选版本进入生产。计时起点是 canary 测试开始，不是坏代码上线到用户受影响。两个都是作者挑选的成功案例，指标都是高事件率的核心指标；论文没有给漏报率，也没有全量部署统计。论文自己承认，数据到达很慢的计数指标（如冷门设备的 SPS）需要更久才能拒绝原假设，长时间 canary 中平稳性假设很可能被违反，I 类错误保证会退化到什么程度并不清楚。论文说 fixed-n 方法「需要 30 分钟以上」，这是作者断言，没有给对比实验。
- **证据分级**：厂商口径（案例为作者自选；数字本身单源已核）。
- **主要一手来源**：Netflix KDD 2022，Figure 2、Figure 4、Discussion，https://arxiv.org/pdf/2205.14762v2
- **修正记录**：原稿写「n = 2，不能外推为一般 TTD」（正确）→ 现在补上「低频指标更慢、平稳性假设可能失效、计时起点是 canary 开始、30 分钟是作者断言」。R 席判 CORRECTED，V 席、K 席判 HOLDS，取 CORRECTED。
- **禁止写法**：「Netflix 能在 11 秒内发现坏发布」「序贯检验把 TTD 降到秒级」（不加 n = 2 和适用条件）；「fixed-n 要 30 分钟」（写成事实）。

### L07-3 Facebook Configerator：分阶段 canary，约 10 分钟是测试运行时长，不是 TTD
- **锁定表述**：Facebook 的配置变更自动 canary 按 spec 分阶段进行，例如阶段 1 在 20 台服务器上测，阶段 2 在有数千台服务器的完整集群上测。判据可以是「新配置服务器的 CTR 比仍用旧配置的服务器低不超过 x%」。成功案例：一次代码错过了 release cut，五天后才提交新的 schema 配置，canary 把那 20 台服务器的错误日志与其余生产服务器对比，发现 log spew（错误日志快速增长），中止了 rollout，避免了一次宕机。原文中「自动 canary 测试约需 10 分钟」是用来说明 Configerator 的提交延迟不关键，指的是 canary 测试本身的运行时长。它只能说明「在 canary 中会显现的问题，大约 10 分钟内判定」，对逃逸到生产的问题没有任何说明。
- **证据分级**：单源已核（同行评审，Facebook 作者自评）。
- **主要一手来源**：Tang et al., "Holistic Configuration Management at Facebook", SOSP 2015，https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf
- **修正记录**：原稿写「自动 canary 约需 10 分钟（TTD 量级）」→ 现在写「canary 测试运行时长约 10 分钟，不是 TTD」。R 席、K 席判 CORRECTED，V 席判 HOLDS 但同样锁定为测试时长，取 CORRECTED。
- **禁止写法**：「Facebook 10 分钟发现坏配置」「canary 的 TTD 是 10 分钟」。

### L07-4 Facebook Configerator：小规模 canary 压不出负载问题；合法配置暴露代码 bug，工程师推翻了 canary
- **锁定表述**：Facebook 在同一篇论文里给了两个反例。(a) 一次配置把移动端请求导向一条罕见代码路径，压垮了后端数据存储。当时自动 canary 只在少量服务器上测，规模不足以引发负载问题，全站部署后延迟上升才显现；此后 Facebook 增加了「在一个集群的数千台服务器上测」的 canary 阶段。(b) canary 因实例崩溃拒绝了一次配置变更，工程师认定「一定是 canary 工具误报」，推翻拒绝并部署，结果引发更多崩溃，随即回滚。配置本身是正确的，但它让应用走上了一条新代码路径，触发了一个隐蔽的竞态 bug。作者称加强自动 canary 是「一场永无止境的战斗」。两例都是 n = 1 的作者叙述。同文作者人工分析了三个月的高影响事故，其中 16% 与配置管理有关；在配置相关事故中，「合法配置暴露代码 bug」一类占 22%。这组比例只有 G07 的 R 席核过，且只覆盖一个三个月窗口。
- **证据分级**：单源已核（案例级；16%/22% 为单席核对）。
- **主要一手来源**：Tang et al., SOSP 2015，https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf
- **修正记录**：原稿（CHANGE:C10）URL 写「同 C09」，在本组无法解析，会被误引成 CAS 论文 → 现在统一写 SOSP 2015 Tang et al.。CHANGE:C10 由 V 席判 CORRECTED（元数据）；C19 三席均判 HOLDS。
- **禁止写法**：把 CHANGE:C10 的来源写成 CAS 或「同 C09」；「22% 的事故是 canary 误判」（22% 是配置相关事故中的一类，且不等于 canary 误判）。

### L07-5 Azure 安全部署：中央策略强制 bake time，有意牺牲速度，没有拦截数字
- **锁定表述**：Azure 的安全部署由中央声明式策略和流程（而不是开发者）决定软件推出的速度，包含强制的健康信号和每个阶段强制的 bake time。理由是让变更经历该服务完整的负载谱：早上的企业用户、晚上的游戏用户、长时间运行的 VM 创建等。Azure 明说其部署工具和流程「有意牺牲速度」，让信号有时间积累、场景在规模上被走到，以便在影响最小的阶段发现问题；只有在少数紧急情况下（如发布安全更新）才会加速。文章没有给出任何拦截数量或误回滚率。署名为 Mark Russinovich，正文作者为 Cristina del Amo Casado，2020-02-05 发布。
- **证据分级**：厂商口径（博客，无数字）。
- **主要一手来源**：Azure Blog, "Advancing safe deployment practices"，https://azure.microsoft.com/en-us/blog/advancing-safe-deployment-practices/
- **修正记录**：无实质修正（三席均判 HOLDS）。R 席提出 Azure Front Door 2025-10-29 事件可作旁证，但 PIR 原文没有抓到、只有二手报道，按规则列为未验证，见否决与降级清单。
- **禁止写法**：「Azure 的安全部署拦下了 X% 坏发布」；用 2025-10 AFD 事件做承重论据。

### L07-6 Facebook 持续部署：严重故障增长远慢于部署增长（相关，非因果）
- **锁定表述**：Savor 等人（作者含 Facebook 员工）用 Facebook 内部数据，以每月部署数为横轴、按严重度分级的每月生产故障数为纵轴拟合趋势线：critical、medium、low 三级的斜率依次为 0.0004、0.0013、0.0061。按 0.0004 粗算，大约每月多 2500 次部署才多 1 起 critical 故障。原文没有给出截距和拟合优度，原句三个斜率配两个类别名，有语病，但上下文支持按三级理解。作者据此提出 critical 问题数量与部署次数几乎无关。代价是：在约 2009 年 1 月至 2010 年 7 月的生产率激增期，以热修复数为代理的质量下降，此后提升质量「以部分生产率为代价」。这是相关不是因果，没有单独度量 canary 或发布后检测的贡献。论文内部图号不一致，成文不要引图号。
- **证据分级**：单源已核（ICSE 行业 track，作者含公司员工）。
- **主要一手来源**：Savor, Douglas, Gentili, Williams, Beck, Stumm, "Continuous Deployment at Facebook and OANDA", ICSE-C 2016，https://www.eecg.toronto.edu/~stumm/Papers/Savor-ICSE16.pdf
- **修正记录**：无实质修正（三席均判 HOLDS）；补上斜率单位与「不引图号」。
- **禁止写法**：「部署越多事故越少」「canary 让 Facebook 的严重故障不随部署增长」（因果化，且没有拆出检测的贡献）。

### L07-7 MDE 以下的累积回退：260% 是线性假设算例，「单次 canary 看不见」是推论
- **锁定表述**：Savor 等人指出，持续部署可能遭遇「千刀万剐」：发布决策下放给各个开发者，没有中央协调。论文的**假设**算例是：每次更新多占 0.05% CPU，每周 100 次这样的发布，一年后 CPU 用量增加 260%（线性累加，0.05% × 100 × 52）。这是假设，不是实测；论文中关于 Facebook 如何解决的那句话在 PDF 中被截断，原文不可考。由此推出的结论是：单次 canary 的样本量决定了它的最小可检测效应（MDE），低于 MDE 的单次回退在逐次 canary 中**可能**不显著，需要舰队级或跨版本的长期检测来兜底。这一推论不在 Savor 原文中，原文没有提 canary 或 MDE。Meta FBDetect 在 FrontFaaS 上以 0.005%（子程序级 gCPU）为检测阈值、TOCS 扩展版专门处理「渐变回归」，说明这类增量对舰队级长窗口检测器未必不可见。
- **证据分级**：算例为单源已核（假设）；「单次 canary 看不见」的推论为未验证（K 席），R 席认为方向存争、与 FBDetect 合看可升级，取保守的未验证。
- **主要一手来源**：Savor et al., ICSE-C 2016，https://www.eecg.toronto.edu/~stumm/Papers/Savor-ICSE16.pdf ；佐证见 L08-1、L08-9。
- **修正记录**：原稿写「低于 MDE 的单次回退，逐次 canary 检验永远看不见」→ 现在写「单次 canary 可能看不见（推论，非原文），舰队级长期检测可兜底」。K 席判 CORRECTED，V 席、R 席判 HOLDS 但都要求标为推论，取 CORRECTED。
- **禁止写法**：「Facebook 一年 CPU 涨了 260%」「0.05% 的回退永远检测不到」；改成复利算法（≈13 倍）。

### L07-8 AWS 的 bake time 是设计参数，不是「问题多晚显现」的实测或上界
- **锁定表述**：AWS Builders' Library（Clare Liguori，2020-06-18）描述，其流水线在每个生产阶段之后设置 bake time，持续监控高严重度聚合告警，捕捉「慢燃型」影响。典型流水线的默认值是：每个 one-box 阶段后至少等 1 小时，第一个区域 wave 后至少等 12 小时，后续每个 wave 等 2–4 小时，全区域部署约需 4–5 个工作日；此外还要求积累足够的数据点（原文举例：Create API 至少收到 100 次请求）。大型或关键服务会更保守。原文把这些时长写成「扩大影响的风险」与「交付速度」之间的权衡，不是对影响显现时延的测量，更不是上界：bake 结束后才显现的问题依然存在。它反映 AWS 预期部分影响要到小时级才显现。AWS 也承认，one-box 通常最多承接约 10% 的流量，它引入的问题可能触发不了服务级的高严重度回滚告警，所以另设只看 one-box 的局部指标。文章没有任何检出率或误回滚率数字。
- **证据分级**：厂商口径。
- **主要一手来源**：AWS Builders' Library, "Automating safe, hands-off deployments"，https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/
- **修正记录**：原稿写「等于用设计参数给出了坏发布影响可能多晚才显现的厂商经验上界（小时到天级）」→ 现在写「风险与速度权衡下的设计参数，不是实测，也不是上界」。R 席、K 席判 CORRECTED，V 席判 HOLDS，取 CORRECTED。
- **禁止写法**：「AWS 的经验是坏发布最晚 12 小时内显现」「bake time 是 TTD 上界」。

---

## G08 Meta FBDetect / ServiceLab / TOCS 扩展版

一手来源：FBDetect，SOSP 2024，https://tangchq74.github.io/FBDetect-SOSP24.pdf （DOI 10.1145/3694715.3695977，15 位作者全部挂 Meta）；ServiceLab，OSDI 2024，https://www.usenix.org/system/files/osdi24-chow.pdf ；TOCS 扩展版，https://yangwang83.github.io/papers/tinyregression-tocs.pdf （DOI 10.1145/3785504）。三篇都是 Meta 自评。

**适用域总警告（R3-M）**：FBDetect 检测的是资源效率回归（CPU、吞吐、延迟、内存），主要后果是浪费服务器，不是用户可见的故障。拿它支撑「坏发布多快被发现」时，必须说明这是性能/资源类回归，存在题目错配。

### L08-1 0.005% 是超大舰队上的子程序级 gCPU 绝对阈值，不可外推到小服务
- **锁定表述**：Meta 自报，FBDetect 监控约 80 万条时间序列（吞吐、延迟、CPU、内存等），在数百个服务中检测由代码或配置变更引起的性能回归，最小能检出 0.005% 的回归。0.005% 是 FrontFaaS「小回归档」配置的检测阈值，指占全服务 CPU 的**绝对份额**变化，在子程序级检出（例如来自占 0.1% CPU 的子程序时，子程序内的相对变化是 5%）。实际检出的回归，中位数约 0.04%（Table 4：P10 = 0.010%，P50 = 0.043%）。这一灵敏度依赖 50 万台以上服务器和子程序级栈采样；同一篇论文里，只有 16 台服务器的 Invoicer 服务只能做到 0.5%，还需要每秒采样和 1 天窗口。所以它不能外推到中小服务。
- **证据分级**：单源已核（Meta 自评）。
- **主要一手来源**：FBDetect SOSP 2024，摘要、Table 1、Table 4，https://tangchq74.github.io/FBDetect-SOSP24.pdf
- **修正记录**：原稿与锁定一致；补上「检出中位数约 0.04%」（K 席）与「16 台服务只能做到 0.5%」（R3-M 降级理由）。三席均判 HOLDS；R3-M 降级为「只在超大舰队的 CPU 效率回归上成立」。
- **禁止写法**：「FBDetect 能检出 0.005% 的错误率或可用性下降」「中小团队也能做到 0.005% 级检测」「FBDetect 一般能抓到 0.005% 的回归」（这是阈值，不是典型检出值）。

### L08-2 FBDetect 是周期批处理；论文没有 TTD 分布，只能由窗口配置推设计量级
- **锁定表述**：FBDetect 按周期批处理运行，不是实时。FrontFaaS 同时跑两档：大回归档阈值 3%，每 30 分钟重跑一次，分析窗口 3 小时；小回归档阈值 0.005%，每 2 小时重跑一次，历史窗口 10 天，分析窗口 4 小时，延长窗口 6 小时。AdServing 长期档阈值 0.1%，每天跑一次，历史窗口 16 天，分析窗口 9 天。论文明说，阈值越小，越要等更久收集数据；延长 went-away 窗口能减少误报，但会推迟检测，这一权衡是开放问题。论文中未见 TTD 分布（只能证到「未见」）。若要写检测时延，只能写「由窗口配置推得的设计量级」：大回归为小时级，0.005% 小回归约 10 小时以上（推算，非实测）。
- **证据分级**：窗口配置为单源已核；「论文没有 TTD 分布」为未验证（V 席只能证到未见）；时延量级是推算。
- **主要一手来源**：FBDetect SOSP 2024 Table 1，https://tangchq74.github.io/FBDetect-SOSP24.pdf
- **修正记录**：原稿只写了 0.005% 档 → 现在补上 3% / 30 分钟的快档，避免读者以为 FBDetect 一律按小时到天的粒度检测。R 席判 CORRECTED，V 席、K 席判 HOLDS，取 CORRECTED。
- **禁止写法**：「FBDetect 实时检测」「FBDetect 的 TTD 是 X 小时」（写成实测）；「FBDetect 一律要等十几小时」。

### L08-3 降噪漏斗：396 万个 change point → 约 210 条；99.7% 有两种含义
- **锁定表述**：FrontFaaS 短期检测一个月原始检出 396 万个 change point。went-away 检测器这一步就过滤掉约 99.7%（剩 1/365）；经过全部过滤步骤后，短期检测列只剩约 1/18857，约 210 条（全流程过滤率约 99.995%）。月度报告的 217 条是整个 FrontFaaS 的数字（含长期检测），与 210 不是同一行，不要并成一条漏斗。论文另一处说，典型的 change-point 算法在他们的环境里会有 99.7% 的误报率。这是两个不同语境里的 99.7%，不得混用。其他工作负载的累计过滤比例在 1/30 到 1/5240 之间。这些都是降噪比例，不是准确率。可以得出的结论是：在 Meta 的性能时间序列场景里，未经大量工程化过滤的异常检测几乎全是噪声。
- **证据分级**：单源已核（Meta 自评）。
- **主要一手来源**：FBDetect SOSP 2024 Table 3 与正文，https://tangchq74.github.io/FBDetect-SOSP24.pdf ；TOCS 扩展版 Table 3。
- **修正记录**：原稿写「396 万 → 全流程后约 1/18857，对应 217 条」→ 现在写「1/18857 只对应短期检测列（≈210 条），217 是另一口径」。K 席判 CORRECTED，V 席、R 席判 HOLDS 但同样注明了 210 与 217 的差异，取 CORRECTED。R3-M 降级 99.7% 为「降噪量级」。
- **禁止写法**：「FBDetect 过滤掉 99.7% 的误报」「FBDetect 准确率 99.7%」「396 万 → 217」。

### L08-4 精度：开发者确认的 70 条中 49 真 21 假（≈70%）；「每 13 年一次误报」作废
- **锁定表述**：一个月里 FrontFaaS 共报 217 条回归，开发者只对 70 条给出了明确的真假确认：49 条为真，21 条为误报，确认子集 precision = 49/70 = 70.0%（Wilson 95% CI 约 58.5%–79.5%）。另有 123 条被标为「resolved」，没有真值；24 条无人处理。确认率只有 70/217 ≈ 32%，存在选择偏差。若对 217 条全量取极值，precision 落在 22.6%（未确认的全为假）到 90.3%（未确认的全为真）之间。在 EGADS 对比集上，独立人工复核得到 76/107 ≈ 71.0%（见 L08-6），与 70% 数值相近、互相印证，但那是另一个集合。21 条误报中有 15 条源自 cost shift。论文中「一个 FrontFaaS 开发者大约每 13 年才遇到一次误报」是按 49:21 外推到全部 217 条后，再按约 1 万名开发者人头摊薄得到的，衡量的是单个开发者被打扰的频率，组织越大数字越好看，不是检测器的误报率。
- **证据分级**：单源已核（Meta 自评；70% 为可核子集）。
- **主要一手来源**：FBDetect SOSP 2024 §评估，https://tangchq74.github.io/FBDetect-SOSP24.pdf ；R3-M 审计重算（CI 与极值界）。
- **修正记录**：原稿写「确认子集精度 70%；13 年是假设比例推广后按人头摊」（正确）→ 现在补上 CI、全量极值界，并把「13 年」整体否决、不得作为检测质量证据。三席均判 HOLDS；R3-M 否决「13 年」以及任何「近乎零误报」的说法。
- **禁止写法**：「FBDetect 每 13 年才误报一次」「FBDetect 几乎没有误报」「FBDetect precision 70%」（不加「确认子集」）。

### L08-5 漏报评估：4 起事故作真值，结构性不完整；2 起检出但没拦住
- **锁定表述**：FBDetect 的漏报评估以 2023 年全年 FrontFaaS 的 4 起性能事故为真值：2 起被 FBDetect 检出，但开发者没有及时处理；1 起是因为开发者没有把出现回归的指标导出给 FBDetect（作者算作「不归它管」）；1 起是容量管理问题，与代码或配置变更无关。作者由此称 FBDetect「没有漏掉它应该抓的」。有效样本只有 2 起，2/2 检出（Wilson 95% CI 约 34%–100%）；如果把未导出指标的那起计入分母，就是 2/3。作者自己承认，这不代表 FrontFaaS 上不会漏掉大于 0.005% 的回归，只代表漏掉的回归没大到被开发者注意到；漏报真值来自「被注意到的事故」，结构上看不到小回归的漏报。作者另称，在三年的全站事故中只找到 1 起由 FBDetect 漏报导致的事故（cost-shift 检测器误滤了一个回归，致某大服务出现 0.015% 错误率），检索方法未给出，属轶事级。这组数据不能当召回证据，但它是「检出不等于拦下」的正面证据：可归因的 2 起都被检出，也都没有被及时处理。
- **证据分级**：单源已核（Meta 自评，n = 4 / 2）。
- **主要一手来源**：FBDetect SOSP 2024 §漏报评估，https://tangchq74.github.io/FBDetect-SOSP24.pdf
- **修正记录**：原稿与锁定一致；补上「可归因 2/2 检出、0/2 及时拦下」以及 CI。三席均判 HOLDS；R3-M 否决把它当作 recall 证据，并把三年 1 起降为轶事。
- **禁止写法**：「FBDetect 没有漏报」「FBDetect recall 100%」「三年只漏一次」（不加「作者自查，方法未给」）。

### L08-6 与 Yahoo EGADS 的对比：真值部分由 FBDetect 自己定义
- **锁定表述**：Meta 构造了一个测试集：随机抽 107 条 FBDetect 报了回归的时间序列（人工复核为 76 真 31 假，precision ≈ 71%），加上约 3.5 万条 FBDetect 没报回归的序列。这 3.5 万条没有逐条独立标注，被直接当作真阴性；FBDetect 的漏报率被「假设为 0」。在此设定下，FBDetect 的误报率为 31/(35K+31) ≈ 0.00088。作者设定的可用门槛是 FPR < 760/(35K+31) ≈ 0.02（760 = 10 × 76，意思是误报超过真阳性 10 倍、九成调查白费即不可用）。Yahoo EGADS（2015 年开源基线）三种算法中只有算法 1 能满足这个门槛，代价是漏报率 0.84，而它被判漏报的就是 FBDetect 报出并经人工确认的那 76 条。整个对比以 FBDetect 自身输出为参照系，构造上对 FBDetect 有利。
- **证据分级**：方向存争（R 席认为评估设计偏向自身；V 席判 HOLDS，K 席判 CORRECTED）。
- **主要一手来源**：FBDetect SOSP 2024，Figure 8 与对比段，https://tangchq74.github.io/FBDetect-SOSP24.pdf
- **修正记录**：原稿写「FBDetect 误报率 0.00088；EGADS 只有一种能满足门槛但漏报 0.84」→ 现在写「测试集按 FBDetect 自身判定抽样，3.5 万条阴性未独立标注，FBDetect 漏报率是假设的 0；对比在构造上偏向 FBDetect」。R 席、K 席判 CORRECTED，取 CORRECTED。R3-M 否决「FBDetect 漏报率为 0」。
- **禁止写法**：「FBDetect 误报率只有 0.088%」（不加参照系说明）；「FBDetect 漏报为 0，而 EGADS 漏掉 84%」。

### L08-7 根因定位（属于定位，不是检测）：建议 75 条，确认 71 条
- **锁定表述**：同一个月 217 条回归中，FBDetect 为 75 条给出了根因候选，其中 71 条经开发者确认正确（真因在前三个候选中），按确认数算约 33%（71/217）；论文以「给出建议数」作分子，报告为 75/217 ≈ 35%，开发者人工补救后也只到 (75+6)/217 ≈ 37%。作者另对一批**不在**同一时间窗内的 61 条未定位案例做了二次分析，在「两个时期失败率相同」「排除 11 条未导出指标的变更」两个假设下，估计算法的真实失败率约 22%。
- **证据分级**：单源已核（Meta 自评；22% 为作者估计）。
- **主要一手来源**：FBDetect SOSP 2024 §根因分析，https://tangchq74.github.io/FBDetect-SOSP24.pdf
- **修正记录**：原稿写「75 条，71 条被确认；整体 35%」→ 现在写「按确认数约 33%，论文报 35%；22% 来自另一时间窗、基于假设」。K 席判 CORRECTED，V 席、R 席判 HOLDS，取 CORRECTED。
- **禁止写法**：把根因定位成功率写成检测成功率；「FBDetect 真实失败率 22%」（不加「作者估计、另一批样本」）。

### L08-8 ServiceLab：发布前测试有效，但覆盖有限、误报可观
- **锁定表述**：Meta 的 ServiceLab 在发布前回放生产流量做性能测试，平台整体 CPU 回归达到 0.01% 就报警；五年来真阳性回归幅度的中位数是 0.14%（p90 为 1.7%，p99 为 38.7%）。代价方面：ServiceLab 只对约 23% 的 FrontFaaS 变更跑了实验；被测变更中 0.3%（5,560 次）报了回归，其中 57% 为真、15% 为假、28% 未知，按比例外推误报约 21%（「符合预期」的变化被计为真阳性）；A/A 实验中，p50、p90、p99 指标的误报率分别为 0.6%、40%、64%。原文还说，开发者如果频繁收到误报工单，很可能会无视它们。FBDetect 论文明说，发布前性能测试必要，但因为难以精确复制复杂的生产环境，有些问题会漏过；检测极小回归需要海量样本，只有大规模生产舰队才收集得到。注意：ServiceLab 的 0.01% 是平台总体 CPU（发布前），FBDetect 的 0.005% 是子程序级 gCPU 绝对变化（生产），不是同一指标。
- **证据分级**：单源已核（Meta 自评；23%、21%、A/A 误报率等「代价」数字只有 G08 的 R 席核过）。
- **主要一手来源**：Chow et al., ServiceLab, OSDI 2024，https://www.usenix.org/system/files/osdi24-chow.pdf ；FBDetect SOSP 2024，https://tangchq74.github.io/FBDetect-SOSP24.pdf
- **修正记录**：原稿只写了 ServiceLab 的灵敏度 → 现在必须同时写出覆盖率与误报代价（R 席），并注明两个百分比不是同一指标（K 席）。三席均判 HOLDS。
- **禁止写法**：「发布前测 0.01%、发布后测 0.005%，所以生产检测更灵敏」；只写 0.01% 灵敏度而不写 23% 覆盖率和误报。

### L08-9 TOCS 扩展版：ServiceLab 漏报率约 32%（以 FBDetect 为参照）；「数万台机器」是反事实
- **锁定表述**：FBDetect 与 ServiceLab 的 TOCS 合并扩展版（2025 年；PDF 内只见 2025-03 收稿、2025-08 修订，出版月份未核）称，自 2024 年中起，Meta 用 ServiceLab 持续跑基准、把结果喂给 FBDetect 检测，再由 ServiceLab 对嫌疑变更做二分定位。这条流水线的场景是 PyTorch/ML 训练（TorchBench 等，案例是 GPU 内存和延迟问题），不是 FrontFaaS 的 Web 服务。渐变回归一次可能有 5,000–20,000 个嫌疑变更，突变回归则直接取最近的变更。论文称这「帮我们抓到了本会耗费 Meta 数万台机器的回归」，是反事实估算，不是实测节省量。TOCS 版还新增了 ServiceLab 的漏报率估计：以 FBDetect 报出、可归因到变更、但 ServiceLab 漏掉的 2,038 个变更为分子，漏报率约 32%。作者附了两条 caveat：无法归因到变更的回归没有计入；FBDetect 本身不保证准确。TOCS 同时把 ServiceLab 的 precision 改报为 79.4%、每次变更的误报率约 0.014%。论文承认，发布前测试受测试资源所限，无法完全复现生产的规模与复杂度，有缺陷的代码或配置变更会漏到生产。FBDetect 部分的评估数字与 SOSP 版完全相同，没有新数据。
- **证据分级**：厂商口径（「数万台机器」与 32% 漏报率均为 Meta 自评；32%、79.4% 只有 G08 的 R 席核过）。
- **主要一手来源**：TOCS 扩展版，https://yangwang83.github.io/papers/tinyregression-tocs.pdf （DOI 10.1145/3785504）
- **修正记录**：原稿写「2025-12；节省数万台机器；无误报/延迟新数据」→ 现在写「2025（出版月份未核）；『本会耗费』数万台机器，是反事实；新增 ServiceLab 漏报率约 32%；场景是 ML 训练」。V 席、R 席判 CORRECTED，K 席判 HOLDS（但同样要求改日期），取 CORRECTED。
- **禁止写法**：「Meta 节省了数万台机器」「TOCS 2025-12」；「ServiceLab 漏掉 32% 的回归」（不加「以 FBDetect 为参照、附 caveat」）；把二分定位流水线写成 Web 服务场景。

---

## G10 低底率、告警信任与人工推翻

### L10-1 Opprentice 的 0.66/0.66 是一个运维团队对点级 KPI 异常检测的偏好
- **锁定表述**：在 Opprentice（IMC 2015，清华与百度等）中，与作者合作的运维人员（百度搜索）把「recall ≥ 0.66 且 precision ≥ 0.66」作为准确率偏好，这组数值来自他们以往使用其他检测器的经验，在论文中作为 Opprentice 的量化目标。这里的 precision 和 recall 定义在 KPI 时间序列的**异常数据点或异常窗口**上，对象是搜索引擎的 PV、慢响应数、响应时间等 KPI，不是发布级的放行或停止判定。论文明说偏好因场景而异：忙碌的运维更在意 precision，收入类 KPI 更在意 recall。论文还说，异常在数据中相对稀少，检测器很难同时做到高 recall 和高 precision，两者常常冲突。
- **证据分级**：单源已核。
- **主要一手来源**：Liu et al., "Opprentice: Towards Practical and Automatic Anomaly Detection Through Machine Learning", IMC 2015，http://conferences2.sigcomm.org/imc/2015/papers/p211.pdf
- **修正记录**：原稿写「即愿意接受约 1/3 告警为误报、1/3 异常被漏」→ 现在写「一家合作运维团队对点级 KPI 异常检测的目标值，不是发布级门槛，也不是行业标准」。V 席判 CORRECTED，R 席、K 席判 HOLDS 但同样要求限定适用面，取 CORRECTED。
- **禁止写法**：「业界可接受 1/3 的告警是误报」「发布检测的行业门槛是 0.66」。

### L10-2 底率算例（自算假设，不是实测）
- **锁定表述**：下面是假设性算例，用来说明「坏发布本身很少时，误报率决定告警可信度」。假设每天 1000 次发布，坏发布率 1%（10 次坏、990 次好），检测器对坏发布的检出率（TPR）为 95%，即每天真报 9.5 次；误报只发生在 990 次好发布上。
  - 每次发布误报率（FPR）2%：误报 19.8 次，precision = 9.5/29.3 ≈ 32%。
  - FPR 0.5%：误报 4.95 次，precision ≈ 66%。
  - FPR 0.1%：误报 0.99 次，precision ≈ 91%。
  - 每次发布同时看 100 个指标、每个指标 FPR 0.1%，**并假设各指标相互独立**：每次好发布至少一个指标误报的概率 = 1 − 0.999^100 ≈ 9.5%，误报约 94 次，precision ≈ 9%。真实指标高度相关，整体误报率会低于这个数，所以它是独立性假设下的上界式示意；多指标「任一报警即判坏」时 TPR 也会高于 95%，但对结论影响很小。
  
  结论是方向性的：底率低时，precision 主要由 FPR 决定。对性能回归来说，1% 的底率可能还偏宽松（ServiceLab 被测变更中只有 0.3% 报了回归，见 L08-8），底率越低，同样 FPR 下 precision 越差，结论方向不变而且更强。「生产检测器的主要工程量在压误报」可以引 FBDetect 的降噪漏斗作同向佐证：FrontFaaS 短期检测一个月 396 万个 change point 被过滤到约 210 条（L08-3），以及 ServiceLab A/A 实验中 p90、p99 指标误报率 40%、64%（L08-8）。但这两个都是性能时间序列场景，单位是 change point 或指标，不是「发布」，不能当发布级底率的实证。FPR 0.5% 对应的 66%，只能说「数值上与 Opprentice 合作运维给出的点级目标相近（单位不同，仅作直观参照）」。
- **证据分级**：自算（算术已三席重算无误）；方向有多源支撑（FBDetect、ServiceLab 同向）；不是实证。
- **主要一手来源**：本线自算；佐证见 FBDetect SOSP 2024（https://tangchq74.github.io/FBDetect-SOSP24.pdf）、ServiceLab OSDI 2024（https://www.usenix.org/system/files/osdi24-chow.pdf）。
- **修正记录**：原稿写「FPR 0.5% → precision ≈ 66%（恰好是 D24 运维门槛）；100 个独立指标 ≈ 9%；实证对照 396 万 → 217」→ 现在写「数值相近、单位不同；100 指标结果建立在独立性假设上，是上界式示意；漏斗写作 396 万 → 约 210（短期列），单位不是发布」。三席均判 CORRECTED。
- **禁止写法**：「precision 66% 恰好等于运维门槛」或任何把 66% 与 Opprentice 0.66 画等号的写法；「看 100 个指标会让 precision 掉到 9%」（不加独立性假设）；把算例写成实测；「396 万 → 217」。

### L10-3 检出不等于处置：FBDetect 有 2 起检出未处理，Gandalf 有 1 起人工推翻
- **锁定表述**：Meta 自报，FBDetect 一个月 217 条报告中有 24 条无人处理（约 11%）。这 24 条真假未知；按确认子集 49:21 的比例，其中约三成可能是误报，所以只能写「11% 的报告无人响应」，不能写「11% 的真回归被忽视」。更硬的证据是：2023 年 FrontFaaS 的 4 起性能事故中，有 2 起已被 FBDetect 检出，但开发者没有及时处理（L08-5）。这是处置链路的失败，不是检测失败。Microsoft 的 Gandalf 案例 I 中，CRP 团队认为告警无关，release manager 要求绕过 no-go，直到 Pilot 再次 no-go 才确认是回归（L05-6），这是人工推翻自动判定。Google 也写到，CAS 出过用户无视 canary 失败、推送坏版本的事故（L06-3）；Facebook Configerator 的工程师推翻过 canary 的拒绝，但随即回滚止损（L07-4）。由此可以推出：检测端的效果上限受告警信任和处置链路约束，缩短 TTD 不会自动转化为缩短影响。这一推论有 Google Cloud 2025-06-12 的事例同向支撑（2 分钟开始分诊、10 分钟定位根因，部分区域完全恢复约 2 小时 40 分钟）。各案例都是 n 很小的厂商自述。
- **证据分级**：各数字为单源已核；「检出 ≠ 处置」这一方向为多源证实（Meta、Microsoft、Google、Facebook 各自的一手材料同向，但都是厂商自述，都是个案级）。K 席把结论定为推论，R 席定为多源证实；方向上无人反对，取「多源证实（厂商个案）」，并在成文时标明是综合判断。
- **主要一手来源**：FBDetect SOSP 2024，https://tangchq74.github.io/FBDetect-SOSP24.pdf ；Gandalf NSDI 2020，https://www.usenix.org/system/files/nsdi20-paper-li.pdf ；CAS ACM Queue 2018，https://sre.google/static/pdf/canary_analysis.pdf ；Configerator SOSP 2015，https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf ；GCP 事故报告，https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW
- **修正记录**：原稿写「24 条无人处理；发布经理基于经验认为告警无关而忽略」→ 现在写「24 条真假未知，只能写 11% 无人响应；CRP 团队认为无关，release manager 要求绕过」。三席均判 CORRECTED。
- **禁止写法**：「FBDetect 11% 的真回归被忽视」「发布经理凭经验忽略了告警」；「大厂 canary 判定经常被推翻」（没有任何公开的推翻率）。

### L10-4 Headout：误回滚从每周 5 次降到 1 次（n = 1，无分母）
- **锁定表述**：Headout 的工程博客（2025-04-11）称，他们有 40 多个微服务，用 Argo Rollouts 做自动回滚。最初的判据是「总错误率与前一小时比较、固定阈值」，会被与部署同时发生的垃圾流量攻击、配置错误的错误日志等干扰，造成误回滚。改为比较 canary 与 stable 的错误差（前提是流量均匀）之后，误回滚从每周 5 次降到每周 1 次。残余误报来自低 RPM 服务的错误，以及只被路由到 canary pod 的特定失败 API。每周部署数没有披露，无法换算成误回滚率。同一篇博客还自称「识别缺陷发布 100%」，依据是拦下了 3 次有缺陷的生产发布，同样没有分母，漏报靠「没注意到」来认定。这是一家公司的从业者轶事。
- **证据分级**：单源已核（从业者博客，n = 1 家公司，检出口径 n = 3）。
- **主要一手来源**：Headout, "Canary Deployment with Automated Rollback"，https://backstage.headout.com/canary-deployment-with-automated-rollback/
- **修正记录**：原稿写「一家中型公司……误回滚由每周 5 次降到 1 次」→ 现在去掉「中型公司」（原文只说 40+ 微服务），补上「流量均匀」前提和「100% = 3/3、无分母」。R 席判 CORRECTED，V 席、K 席判 HOLDS（K 席同样补了 3/3），取 CORRECTED。
- **禁止写法**：「Headout 误回滚率降低 80%」「Headout 检出率 100%」；「中型公司」。

---

## 专项锁定（委托方指定的四个点）

### S1 Gandalf 控制面 recall
锁定为 **37/39 ≈ 94.9%**（按论文自给计数的标准 recall，n = 39，Wilson 95% CI 约 83%–99%）。论文报告的 99.8% 分母未说明，它与 1−FN/全部部署、specificity、NPV 三种算法的数值都吻合，无法判定；R3-M 已否决把它当 recall。详见 L05-2。

### S2 CAS「likely prevented hundreds」
锁定为：Google 自评粗估，CAS「可能避免了数百起值得写 postmortem 的故障」，不用 CAS 的团队 postmortem 率「明显更高」。无分母、无方法、无置信区间，后者存在团队自选择偏差；Google 同时承认精确的影响分析很难，并放弃了 A/B 方案。证据分级为厂商口径。既不能写「Google 没给数字」，也不能写「CAS 防住了数百起故障」。详见 L06-4。

### S3 canary 六类结构性盲区（每类一个一手例证）

| # | 盲区 | 机制 | 一手例证 | 证据分级 |
|---|---|---|---|---|
| 1 | **规模或负载不足** | canary 规模小、或在低峰期，压不出只在高负载或全局规模下出现的问题 | Facebook Configerator：一次配置把移动端请求导向罕见路径、压垮后端存储，小规模 canary 没有足够负载暴露问题，全站部署后延迟才显现，事后加了数千台的集群级阶段（Tang et al., SOSP 2015，https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf）。旁证：SRE Workbook 称性能缺陷通常只在高负载下显现 | 单源已核（n = 1） |
| 2 | **潜伏 / 时间延迟** | 问题在 canary 观测窗口结束后才显现 | Microsoft Gandalf 案例 III：NIC 固件与驱动冲突，部署后 24–72 小时 OS 才崩溃；另有发布 32 小时后才检出的潜伏问题（Li et al., NSDI 2020，https://www.usenix.org/system/files/nsdi20-paper-li.pdf）。注意：案例 III 本身被 Gandalf 在 Canary 阶段检出 | 单源已核 |
| 3 | **未被执行的代码路径，以及不分阶段的数据或策略变更** | canary 只验证被流量走到的路径；触发路径的数据变更不经过 canary | Google Cloud 2025-06-12：故障代码路径在逐区域 rollout 中「从未被执行」，触发它的策略元数据数秒内复制到全球（https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW） | 单源已核（单一事件，仅一席核过原文） |
| 4 | **跨组件交互 / 合法变更暴露既有 bug** | 变更本身正确，但触发了别处的 bug，或违反了跨组件契约 | Facebook Configerator：配置本身正确，但让应用走上新代码路径、触发竞态 bug；这一类占配置相关高影响事故的 22%（三个月窗口，仅一席核）（SOSP 2015，同上）。旁证：Gandalf 论文所列组件级 watchdog 漏掉「跨组件 API 契约违背」 | 单源已核（案例）；22% 为单席核对 |
| 5 | **低流量路径 / 数据缺失** | 低频路径在 canary 期间样本太少或没有数据，统计判定放行 | Spinnaker/Kayenta judge 文档：canary 期间无数据的指标默认判 Nodata、不扣分（https://spinnaker.io/docs/guides/user/canary/judge/）。旁证：AWS 承认 one-box 承接流量小，可能触发不了服务级告警；Netflix 承认冷门设备的计数指标检验更慢 | 单源已核（工具机制为推断） |
| 6 | **低于单次 MDE 的累积回退** | 每次增量都低于单次 canary 的最小可检测效应，逐次放行后累积成大问题 | Savor et al., ICSE-C 2016 的**假设**算例：每次 +0.05% CPU、每周 100 次，一年 +260%（线性）（https://www.eecg.toronto.edu/~stumm/Papers/Savor-ICSE16.pdf）。Meta 用舰队级 FBDetect 和 TOCS 的「渐变回归」检测来兜底，说明这一类需要跨版本的长期检测 | 例证为假设算例；「单次 canary 看不见」为未验证推论 |

使用约束：
- 这六类是由多个来源综合出来的分类，是本线的综合判断，不是任何单一来源给出的分类。成文要这样标注。
- 每类的例证都是个案（n = 1 或假设），不能据此给出各类所占比例。
- 唯一的比例型数字是 Configerator「合法配置暴露代码 bug 占配置相关事故 22%」，限 Facebook、三个月、仅一席核过，只能作为个案级比例引用。
- 另有两类与人和流程相关、不属于 canary 统计结构的失效，要另写：人工推翻正确判定（L05-6、L07-4）；自适应基线把危险行为常态化（L06-3）。workbook 的 5% × 20% = 1% 稀释示例说明的是「看整体的监控」的盲区，是要求 canary 分组对比的理由，不是 canary 本身的盲区。

### S4 底率算例的正确表述
见 L10-2。要点：(1) 全部是自算假设（1000 次/天、1% 坏发布率、TPR 95%、各档 FPR）；(2) 100 指标的 ≈9% 建立在**指标相互独立**的假设上，是上界式示意，真实指标相关时误报会低于这个数；(3) 66% 只能写「数值上与 Opprentice 合作运维的点级目标相近，单位不同，仅作直观参照」，**不得与 Opprentice 的 0.66 画等号**；(4) 方向结论是「底率低时 FPR 决定 precision」，对性能回归，真实底率可能更低（ServiceLab 0.3%），结论会更强。

---

## R3 横向锁定：大厂检测器自评的总体证据地位

### LR3-1 公开的发布检测器检出率几乎都是系统所有者自评，没有对生产系统的独立复测
- **锁定表述**：公开的发布检测器检出率，几乎都来自系统所有者对自家生产系统的自评，主要是 Microsoft Gandalf（NSDI 2020）和 Meta FBDetect（SOSP 2024）。我们没有找到任何第三方拿生产数据复测过 Gandalf、FBDetect、Kayenta 或 CAS。这些自评的「召回」都是代理或假设：Gandalf 把「没有由坏发布引起的 Sev0–2 事故」当作数据面 100% recall；FBDetect 在 EGADS 对比中直接假设自身漏报率为零，漏报评估只用了 4 起被注意到的事故。三篇（含 Walmart）都没有做推断统计（没有 CI、没有检验），小样本（39、70、2、4）配百分比，精度被夸大。时间窗都是作者自选的单一窗口，FN 真值都依赖「事后升级成事故」，会系统性低估漏报。在**算法**层面存在第三方复测：SCELM（arXiv 2507.09315，2025）在三份第三方数据集上把 Gandalf 重新实现成基线，平均 F1 约 0.87。但 SCELM 的作者是竞品方，arXiv 版的实验设置一节只有占位条目，没有说明 Gandalf 是怎么重新实现的。这个数字只能用来说明「Gandalf 的算法在别处并非百分之百」，本身不够硬。
- **证据分级**：「自评为主、无生产复测」为多源证实（R3-X、R3-M 两席独立得出，且与 G05、G08 各三票一致）；SCELM 的 F1 为未验证（单席检索，实验细节缺失，竞品作者）。
- **主要一手来源**：Gandalf，https://www.usenix.org/system/files/nsdi20-paper-li.pdf ；FBDetect，https://tangchq74.github.io/FBDetect-SOSP24.pdf ；SCELM，https://arxiv.org/abs/2507.09315
- **修正记录**：原稿写「主要定量证据几乎全来自 2015–2020 年、无独立复测」→ 现在写「几乎都是系统所有者自评（Gandalf 2020、FBDetect 2024），没有对生产系统的独立复测；算法层面有第三方基线复测，但质量不足以承重」。R3-X 判降级。
- **禁止写法**：「定量数据几乎全来自 2015–2020 年」（FBDetect 是 2024 年）；「完全没有独立复测」（应写「没有对生产系统的独立复测」）；「Gandalf 在第三方数据上 F1 0.87」（写成可靠数字）。

### LR3-2 大厂之外：2024–2025 年的公开数字都是结果指标，没有分母，也没有误回滚率
- **锁定表述**：R3-X 检索到的 2024–2025 年其他公司数字，都是没有分母的结果指标。Slack（2025-10-07）称 73% 面向客户的事故由变更触发，2024 年 4 月引入自动回滚后，客户影响小时数从 2024 年 2 月到 2025 年 1 月下降 90%，但没有回滚次数、误回滚数或检出率。Atoms（原 CloudKitchens，2025-11-06）称超过 80% 的发布走 canary，2025 年第三季度拦下 1,100 多次坏发布，但没有总发布数，FP/FN 有跟踪但没有公布。Uber、LinkedIn、Netflix、Shopify、Spotify、阿里、字节、腾讯都没有搜到公开的检出率或误回滚率。业界调查（DORA、Perforce 2026）没有自动回滚采用率或效果的百分比。
- **证据分级**：厂商口径（只有 R3-X 一席检索，未经三票逐字核对）。
- **主要一手来源**：Slack Deploy Safety，https://slack.engineering/deploy-safety/ ；Atoms，https://techblog.atoms.co/p/deployment-confidence-in-era-of-ai
- **修正记录**：本 part 原稿中没有这一条，由 R3-X 补入。
- **禁止写法**：「Slack 用自动回滚把事故减少了 90%」（下降的是客户影响小时数，没有分母，也没有因果设计）；「业界自动回滚采用率 X%」（没有可靠调查数据）。

---

## 否决与降级清单

### A. R3-M 否决（不得承重，不得出现在正文的论证链中）

| # | 被否决的数字或说法 | 否决理由 | 可替代写法 |
|---|---|---|---|
| V1 | Gandalf 控制面「recall 99.8%」 | 按自给计数，标准 recall = 37/39 ≈ 94.9%；99.8% 的分母被换成了全部部署，或者是 specificity/NPV | 「标准 recall 37/39 ≈ 94.9%（CI 约 83–99%）；论文报告的 99.8% 分母未说明」 |
| V2 | Gandalf 数据面「recall 100% / 零漏报」 | 代理真值（只把 Sev0–2 计为漏报），分母未知 | 「观察期内作者未记录到由坏发布引起的 Sev0–2 事故」 |
| V3 | 「Gandalf 5 分钟发现坏发布」/ 把 5 分钟当 TTD | 5 分钟是流式层的决策流水线延迟 | 「决策延迟约 5 分钟（流式）/ 3 小时（批处理）；检测窗口为小时级到天级」 |
| V4 | 「FBDetect 每 13 年一次误报」及任何「几乎无误报」的说法 | 按开发者人头摊薄的打扰频率，是规模的产物，不是误报率 | 「开发者确认的 70 条中 49 真 21 假（约 70%）」 |
| V5 | 「FBDetect 漏报率为 0」（EGADS 对比） | 原文写的是假设，不是测量 | 「对比中假设 FBDetect 漏报为 0」 |
| V6 | 以 FrontFaaS 4 起事故作为 FBDetect 的 recall 证据 | 有效 n = 2，真值结构性不完整 | 只能作为「检出 ≠ 拦下」的证据：2/2 检出，0/2 及时处理 |
| V7 | Walmart AIDR「MTTD 缩短 7 分钟以上」作为发布检测证据 | 只对应一个子案例（另一处写 14 分钟、7.2 分钟）；n、基线、方差都没有，无对照；是通用异常检测，不是发布检测；团队数 25 与约 30 前后不一致 | 最多作为「大厂 AIOps 自报 MTTD 缩短为分钟级」的轶事，不进入本题论证 |
| V8 | 「FBDetect 过滤掉 99.7% 的误报 / 准确率 99.7%」 | 99.7% 是 went-away 单步过滤率，或是典型 change-point 算法的误报率；全流程过滤率约 99.995%，都是降噪比例 | 「降噪：一个月 396 万个 change point 压到约 210 条（短期列）」 |
| V9 | 「大厂发布后检测有效，所以中小团队照搬也有效」 | 机制依赖海量样本和稳定基线；FBDetect 的 16 台服务只能做到 0.5% | 「不可外推到中小组织」 |

### B. 降级（可以引用，但必须用降级后的口径）

| # | 原数字或说法 | 降级后口径 | 来源 |
|---|---|---|---|
| D1 | Gandalf 数据面 precision 92.4% | 「约 92%，分母未披露，不可重算」 | R3-M |
| D2 | Gandalf 控制面 precision 94.9% | 必须附 n = 39 和 CI 83.1–98.6% | R3-M |
| D3 | Gandalf「99.2% 坏发布在进生产前被拦」 | 「已检出的可疑 rollout 中 99.2% 在生产前阶段被拦」 | R3-M，三席 |
| D4 | Gandalf「8 个月窗口」 | 「论文自称 8 个月（标注 2018-01 至 2018-11，日历跨度不符）」 | 三席，R3-M |
| D5 | FBDetect 0.005% | 只在 50 万台以上舰队的子程序级 CPU 效率回归上成立 | R3-M |
| D6 | FBDetect 三年全站只有 1 起漏报事故 | 轶事级，作者自查，检索方法未给 | R3-M |
| D7 | 「定量数据全来自 2015–2020，完全无独立复测」 | 「几乎都是自评，没有对生产系统的独立复测」 | R3-X |
| D8 | CAS「Google 没给拦截价值数字」 | 改为 S2 的粗估口径 | G06-R、G06-K |
| D9 | Configerator「约 10 分钟（TTD 量级）」 | 「canary 测试运行时长约 10 分钟，不是 TTD」 | G07-R、G07-K |
| D10 | AWS bake time 是「影响多晚显现的上界」 | 「风险与速度权衡下的设计参数」 | G07-R、G07-K |
| D11 | FBDetect TOCS「节省数万台机器」 | 「本会耗费数万台机器」（反事实，厂商口径） | G08-V |
| D12 | FBDetect 根因成功率 35% | 「建议 75 条，确认 71 条（约 33%）；论文报 35%」 | G08-K |
| D13 | Opprentice 0.66「运维门槛」 | 一家合作团队的点级 KPI 偏好 | G10 三席 |
| D14 | Headout「检出 100%」 | n = 3、无分母的自报 | G10-R、G10-K |

### C. 降为「未验证」（至少一票核不到原文，或只能证到「未见」）

| # | 内容 | 理由 |
|---|---|---|
| U1 | Gandalf 控制面 99.8% 的定义（分母） | G05-K：未验证；G05-V：口径推论未验证 |
| U2 | 「低于 MDE 的单次回退逐次 canary 看不见」 | G07-K：调研员推论，原文不在；R 席：方向存争 |
| U3 | 「FBDetect 论文没有 TTD 分布」 | G08-V：只能证到「未见」（三席都没找到，可写「论文未报告 TTD 分布」，不得写「论文证明无法测 TTD」） |
| U4 | TOCS 扩展版「2025-12」出版月份 | G08-K：PDF 内只见收稿与修订日期 |
| U5 | Azure Front Door 2025-10-29 中断：「保护机制被 bug 绕过」 | G05-R、G07-R：PIR 原文没有抓到，只有 InfoQ 二手报道；只能当「体系仍会漏」的旁证，不得用来反证 Gandalf 指标 |
| U6 | Kapel et al. ICSE-SEIP 2024（变更—事故关联的独立复现） | R3-X：PDF 下载超时，没有拿到具体数字，工业方身份未证实；只能写「有学术团队的复现报告称历史评估与实地观察显著不一致」，不得引数字 |
| U7 | ISSRE 2023「How to Manage Change-Induced Incidents?」 | R3-X：只拿到书目信息 |
| U8 | 告警忽略率：Splunk 2025「13% 故意忽略或压制告警」、NeuBird 2026「83% 偶尔忽略」 | G10-R：厂商问卷，原文未核 |
| U9 | Netflix 2024「Sequential A/B Testing Keeps the World Streaming」 | G07-R：正文未直接抓取，只见二手摘要 |
| U10 | SCELM 对 Gandalf 的 F1 0.8685 | R3-X：实验设置空缺，竞品作者 |
| U11 | HADES 复测 SCWarn F1 0.78–0.95 | R3-X：单席检索，且与本题（发布检测）只间接相关 |

---

## 统计

### 按判决文件逐票计数（15 份判决文件，41 条子论断 × 3 票 = 123 票）

| 组 | 子论断数 | V 席 H / C / R | R 席 H / C / R | K 席 H / C / R | 合计 H / C / R |
|---|---|---|---|---|---|
| G05 | 8 | 2 / 6 / 0 | 2 / 6 / 0 | 4 / 4 / 0 | 8 / 16 / 0 |
| G06 | 9 | 5 / 4 / 0 | 6 / 3 / 0 | 7 / 2 / 0 | 18 / 9 / 0 |
| G07 | 9 | 8 / 1 / 0 | 6 / 3 / 0 | 6 / 3 / 0 | 20 / 7 / 0 |
| G08 | 9 | 8 / 1 / 0 | 6 / 3 / 0 | 6 / 3 / 0 | 20 / 7 / 0 |
| G10 | 6 | 2 / 4 / 0 | 1 / 5 / 0 | 4 / 2 / 0 | 7 / 11 / 0 |
| **合计** | **41** | 25 / 16 / 0 | 21 / 20 / 0 | 27 / 14 / 0 | **73 / 50 / 0** |

（H = HOLDS，C = CORRECTED，R = REFUTED。G10 中的 C05、C08 分别与 G05、G06 重复，去重后为 39 条独立子论断。）

### 按保守合并后的子论断计数（任一票 CORRECTED 即记为 CORRECTED）

| 组 | HOLDS | CORRECTED | REFUTED |
|---|---|---|---|
| G05 | 1（D21） | 7 | 0 |
| G06 | 3（C06、C07、C13） | 6 | 0 |
| G07 | 4（C16、C19、C21、C25） | 5 | 0 |
| G08 | 4（D01、D04、D05、D08） | 5 | 0 |
| G10 | 0 | 6 | 0 |
| **合计** | **12** | **29** | **0** |

说明：三席判决中没有任何一条子论断被判 REFUTED。但 R3-M 在数字层面否决了 9 项（见否决清单 A），其中 V1–V6、V8 落在 G05、G08 的子论断之内；按「被否决的数字不得承重」，这些子论断以 CORRECTED 后的口径保留，被否决的数字本身作废。

---

## 成文要点

1. **大厂检测器「几乎不漏」的说法站不住，能站住的是「自报下漏报很少、精度中等」。** Gandalf 控制面按自给计数，precision 和 recall 都约 95%（n = 39）；FBDetect 在可核子集上 precision 约 70%。各家的「召回」都是代理或假设（只把酿成事故的漏报计入），没有第三方用生产数据复测。
   证据强度：数字为单源已核（厂商自评）；「无独立生产复测」为多源证实（R3 两席加 G05、G08 三席）。

2. **公开材料里几乎没有真正的 TTD（坏发布生效 → 被检出）分布。** 常被引用的「5 分钟」（Gandalf）、「11 秒 / 65 秒」（Netflix，n = 2）、「约 10 分钟」（Configerator）分别是决策流水线延迟、自选案例中从 canary 开始计的时间、canary 测试运行时长。AWS、Azure 的 bake time（1 到 12 小时，全区域 4–5 个工作日）是设计参数，它只说明厂商预期部分问题要到小时级才显现。潜伏问题的个案达到 24–72 小时。
   证据强度：单源已核加厂商口径（多家同向，但都是设计参数或个案，没有分布）。

3. **canary 有结构性盲区，统计功效之外还有六类结构问题。** 分别是：规模或负载不足、潜伏延迟、未被执行的路径与不分阶段的数据变更、跨组件交互、低流量与数据缺失、低于单次 MDE 的累积回退。每类都有一手个案；没有任何来源给出各类所占比例（唯一的比例是 Configerator 中 22%，属个案级）。Google 自己也承认，精确量化 canary 的拦截价值很难，只给了「可能避免数百起 postmortem 级故障」的粗估。
   证据强度：分类是本线综合；各例证为单源已核个案；第 6 类为假设算例加未验证推论。

4. **在低底率下，误报率决定告警能不能被信任，而误报直接侵蚀处置。** 自算示例（自算，非实测）：坏发布率 1% 时，每次发布的 FPR 从 0.1% 升到 2%，precision 从约 91% 降到约 32%。Meta 和 Google 的一手材料都表明，生产检测器的主要工程量在压误报（FBDetect 一个月 396 万个 change point 被压到约 210 条；ServiceLab A/A 实验中 p90/p99 指标误报 40%/64%；CAS 认为噪声大的 canary 会被禁用或无视）。
   证据强度：算例为自算；「压误报是主要工程量」有多源同向支撑（Meta、Google 自述），但都是性能或指标级口径，不是发布级实证。

5. **检出不等于处置。** FBDetect 在 2023 年可归因的 2 起事故都检出了，却都没有被及时处理；Gandalf 的正确 no-go 被 release manager 绕过；CAS 出过用户无视 canary 失败的事故；Google Cloud 2025-06 的事故 10 分钟定位根因，部分区域恢复却用了约 2 小时 40 分钟。缩短 TTD 不会自动缩短影响，人机交接是独立的瓶颈。
   证据强度：多源证实（四家厂商一手材料同向），但都是个案级（n 很小），没有任何公开的人工推翻率或「检出后未处置率」统计。
