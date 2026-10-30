# POSTMORTEM 线:公开复盘一手(截至 2026 年 10 月)

调研日期:2026-10-30。数据只取公司官方复盘/状态页 PIR/提交国会的书面证词原文；媒体与第三方汇总只用作找线索,不进表。
取证方式:Bash curl(通用 UA,不带任何个人信息)把原文下载到 scratchpad,转成纯文本后 grep 逐字摘引。**下面所有带引号的英文都是原文逐字摘录**,没有经过 WebFetch 摘要模型。
时区:一律换算成 UTC。原文用 PDT 的(Google、AWS)按 UTC-7 换算,并在旁边保留原文时刻。
「派生」标记的区间是我用原文时刻做减法算出来的,原文里没有这个数字。
引文核验:本文所有英文引文都已用脚本对下载的原文做了子串比对,全部命中。时间线表格的单元格之间用 " / " 连接,比对时按单元格拆开逐个核对。JSON 文件在 lines/POSTMORTEM.json,包含 11 个 case 和 22 条 claim。

## 0. 案例总表

TTD = 影响开始 → 第一个检测信号;RCA = 影响开始 → 定位到原因;MIT = 影响开始 → 主要缓解完成 / 全部结束。这三列都是派生值。

| # | 案例 | 触发变更类型 | 渐进发布/canary(原文) | 影响开始 UTC | 首次检测 UTC / 来源 | 定位 UTC | 缓解开始 → 完成 UTC | 自动回滚 | TTD | RCA | MIT(主要/全部) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CrowdStrike Channel File 291,2024-07-19 | 数据/内容文件(Rapid Response Content) | 无。事后才承诺「staggered deployment … starting with a canary」 | 未披露(更新发布于 04:09) | 未披露 / 未披露 | 未披露 | 回滚(revert)05:27;主机恢复未披露 | 否(人工 revert) | 未披露 | 未披露 | 发布→revert 78 分钟;主机恢复未披露 |
| 2 | Google Cloud Service Control,2025-06-12 | 代码二进制(05-29 上线,潜伏)+ 策略数据推送触发 | 代码「went through our region by region rollout」,但出问题的路径没被执行;策略数据「replicated globally within seconds」 | 17:49(10:49 PDT) | ≤~17:51「SRE team was triaging」/ 来源未明说 | ≤~17:59(「Within 10 minutes」) | red-button 约 18:14 就绪,约 18:29 推完;除 us-central1 外 19:48 恢复;20:49 结束 | 否(人工 red-button) | ≤2 分钟 | ≤10 分钟 | ~40 分钟开始恢复 / 2h59m |
| 3 | Cloudflare WAF 正则,2019-07-02 | 配置/规则(WAF Managed Rules) | 无。「SOP allowed … globally into production without a staged rollout」 | ~13:42(自动部署开始;原文没有单独写影响时刻) | 13:45 PagerDuty / 自动(外部合成测试) | 14:00 | global terminate 14:07 → 14:09 流量恢复;14:52 修复后重新启用 | 否(人工 global kill) | ~3 分钟 | ~18 分钟 | 27 分钟 |
| 4 | Fastly,2021-06-08 | 代码二进制(05-12 部署,潜伏)+ 客户合法配置触发 | 未披露 | 09:47 | 09:48 / 自动(Fastly monitoring) | 10:27(找到触发的客户配置) | 10:36 开始恢复 → 11:00 多数恢复 → 12:35 缓解;17:25 开始部署修复 | 否(禁用该配置) | 1 分钟 | 40 分钟 | 2h48m |
| 5 | Meta 骨干网 BGP,2021-10-04 | 基础设施操作(维护命令;审计工具 bug 没拦住) | 不适用 / 未披露 | 未披露 | 未披露 | 未披露 | 未披露(工程师到机房现场处理) | 否 | 未披露 | 未披露 | 未披露 |
| 6 | AWS us-east-1 DynamoDB DNS,2025-10-20 | 基础设施自动化的潜伏竞态(没有人发起变更) | 不适用 | 06:48(10-19 11:48 PM PDT) | 未披露(「immediately engaged」);NLB 次生故障 13:52 由监控检测到 | 07:38(12:38 AM PDT) | 08:15 临时缓解 → 09:25 DNS 恢复 → 09:40 DynamoDB 恢复;21:20 整体结束 | 否;事后在全球停用这套自动化 | 未披露(次生 NLB:82 分钟) | 50 分钟 | 2h52m / 14h32m |
| 7 | Azure Front Door QNBQ-5W8,2025-10-09 | 基础设施操作(人工清理时绕过保护系统) | 控制面「in line with our safe deployment practices」;保护系统先拦住了,随后「temporarily bypassed it」 | 07:50 | 08:13 / 自动(telemetry) | 09:04 | 09:08 开始重启 → 12:50 可用性恢复 → 16:00 宣布缓解 | 部分:自动重启 + 人工干预 | 23 分钟 | 74 分钟 | 5h00m / 8h10m |
| 8 | Azure Front Door YKYN-BWZ,2025-10-29 | 数据/配置(客户配置生成的元数据)+ 数据面潜伏 bug | 有多阶段 + 健康门控;崩溃是异步的(约 5 分钟后才出现),所以拿着健康信号过了闸,LKG 也被污染 | 15:41 | 15:43 保护系统自动冻结配置;15:48 监控告警 / 自动 | 16:15(调查聚焦到配置变更) | 17:10 开始人工改 LKG → 17:40 部署 → 18:30 开始恢复 → 次日 00:05 缓解 | 自动冻结有;自动回滚到 LKG **没用上**(LKG 已被污染) | 2 分钟(冻结)/ 7 分钟(告警) | 34 分钟 | 8h24m |
| 9 | Cloudflare bot 特征文件,2025-11-18 | 数据库权限变更 → 生成的数据/特征文件 | 数据库变更是逐步推的;特征文件「propagated to all the machines」,每 5 分钟生成一次 | 11:28(表格)/ 11:20(正文) | 11:31 / 自动(automated test) | 13:37 才确认是 Bot Management 文件(一度误判为 DDoS) | 14:24 停止生成和传播 → 14:30 主要恢复 → 17:06 全部恢复 | 否(人工换回旧文件) | 3 分钟(按 11:28) | ~2h09m | 3h02m / 5h38m |
| 10 | Cloudflare FL1 WAF killswitch,2025-12-05 | 配置(全局配置系统) | 第一个变更走了渐进发布;第二个变更走的系统「does not perform gradual rollouts」 | 08:47 | 08:50 / 自动(Automated alerts) | 未单列(「identified shortly after」) | 09:11 revert → 09:12 结束 | 否(人工 revert) | 3 分钟 | 未披露 | 25 分钟 |
| 11 | Cloudflare BYOIP,2026-02-20 | 代码二进制(Addressing API 发布里的子任务 bug) | 「applied iteratively and not instantaneously」,所以只有 25% 的 BYOIP 前缀受影响 | 17:56(表格)/ 17:48(正文) | 18:13「engaged for failures on one.one.one.one」/ 来源未明说(看到的是 1.1.1.1 故障) | 18:46 | 19:11 开始缓解 → 23:03 结束 | 否(人工终止子任务 + 人工恢复) | 17 分钟 | 50 分钟 | 5h07m |

(案例 12 原计划是 Meta 2021-10-04 的定量版,但官方两篇文章都没有任何时间戳,所以只保留为案例 5 的定性记录。最终是 11 条结构化记录。)

---

## 1. 逐案原文摘引

### 案例 1:CrowdStrike Falcon Channel File 291(2024-07-19)
来源:
- PIR:https://www.crowdstrike.com/blog/falcon-content-update-preliminary-post-incident-report/
- 技术说明:https://www.crowdstrike.com/blog/falcon-update-for-windows-hosts-technical-details/
- RCA PDF:https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf
- 国会书面证词(Meyers,2024-09-24):https://homeland.house.gov/wp-content/uploads/2024/09/2024-09-24-HRG-CIP-Testimony-Meyers.pdf

逐字摘引:
- 变更时刻:"On Friday, July 19, 2024 at 04:09 UTC, as part of regular operations, CrowdStrike released a content configuration update for the Windows sensor to gather telemetry on possible novel threat techniques."(PIR)
- 回滚时刻:"The defect in the content update was reverted on Friday, July 19, 2024 at 05:27 UTC."(PIR)
- 受影响窗口:"Systems running Falcon sensor for Windows 7.11 and above that downloaded the updated configuration from 04:09 UTC to 05:27 UTC – were susceptible to a system crash."(技术说明)
- 为什么校验没拦住:"Due to a bug in the Content Validator, one of the two Template Instances passed validation despite containing problematic content data."(PIR)
- 是否渐进发布:当时没有。整改项写的是 "Implement a staggered deployment strategy for Rapid Response Content in which updates are gradually deployed to larger portions of the sensor base, starting with a canary deployment."(PIR)。RCA 写的是 "Findings: Each Template Instance should be deployed in a staged rollout."
- 对比:同一份 PIR 说 Sensor Content 走的是 "a staged sensor rollout process that starts with dogfooding internally"。也就是说,**代码走了分阶段发布,内容/配置没走**。
- 检测时刻与发现来源:PIR、技术说明、RCA、国会证词里都**未披露**。证词只写了 "leading affected sensors to malfunction until the problematic configurations were replaced."

口径提醒:常被引用的「78 分钟」是 04:09 发布 → 05:27 revert 的间隔,不是 TTD,也不是恢复时间。蓝屏主机需要逐台人工修复,恢复时长官方没有给数字。

### 案例 2:Google Cloud Service Control(2025-06-12)
来源:https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW(Incident Report,发布于 2025-06-13 16:45 PDT)
- 代码变更与发布方式:"On May 29, 2025, a new feature was added to Service Control for additional quota policy checks. This code change and binary release went through our region by region rollout, but the code path that failed was never exercised during this rollout due to needing a policy change that would trigger the code."
- 没有 feature flag:"The issue with this change was that it did not have appropriate error handling nor was it feature flag protected." 以及 "If this had been flag protected, the issue would have been caught in staging."
- 数据触发,全球复制:"On June 12, 2025 at ~10:45am PDT, a policy change was inserted into the regional Spanner tables that Service Control uses for policies. Given the global nature of quota management, this metadata was replicated globally within seconds."
- 检测、定位、缓解:"Within 2 minutes, our Site Reliability Engineering team was triaging the incident. Within 10 minutes, the root cause was identified and the red-button (to disable the serving path) was being put in place. The red-button was ready to roll out ~25 minutes from the start of the incident. Within 40 minutes of the incident, the red-button rollout was completed, and we started seeing recovery across regions, starting with the smaller ones first."
- 长尾:"It took up to ~2h 40 mins to fully resolve in us-central-1 as we throttled task creation …"
- 摘要时刻:"Incident Start: 12 June, 2025 10:49" / "All regions except us-central1 mitigated: 12 June, 2025 12:48" / "Incident End: 12 June, 2025 13:49"(原文注明 "All Times US/Pacific")
- 对外沟通:"We posted our first incident report to Cloud Service Health about ~1h after the start of the crashes, due to the Cloud Service Health infrastructure being down due to this outage."
- 教训:"data replication needs to be propagated incrementally with sufficient time to validate and detect issues." 以及 "We will enforce all changes to critical binaries to be feature flag protected and disabled by default."
- 发现来源:原文只写了 SRE 两分钟内开始分诊,**没有说是自动告警触发的**。

### 案例 3:Cloudflare WAF 正则 CPU 耗尽(2019-07-02)
来源:https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/(原文 "All times in this blog are UTC.")
- 变更:"With the tests passing, TeamCity automatically began deploying the change at 13:42."
- 检测与来源:"Three minutes later the first PagerDuty page went out indicating a fault with the WAF. This was a synthetic test that checks the functionality of the WAF (we have hundreds of such tests) from outside Cloudflare …"
- 误判:"In the initial moments of the outage there was speculation it was an attack of some type we'd never seen before."
- 定位:"At 14:00 the WAF was identified as the component causing the problem and an attack dismissed as a possibility."
- 缓解:"Eventually, a team member executed the global WAF termination at 14:07 and by 14:09 traffic levels and CPU were back to expected levels worldwide."
- 修复:"At 14:52 we were 100% satisfied that we understood the cause and had a fix in place and the WAF was re-enabled globally."
- 绕过渐进发布:"The SOP allowed a non-emergency rule change to go globally into production without a staged rollout." 原文还说 "by design, the WAF doesn't use this process because of the need to respond rapidly to threats."(这里的「this process」指 DOG/PIG/Canary)
- 测试漏掉的东西:"What it didn't do was test for runaway CPU utilization by the WAF"
- 告警教训:"The first alert for the global traffic drop took too long to fire."
- 工具依赖:"we couldn't get to other internal services like Jira or the build system."

### 案例 4:Fastly(2021-06-08)
来源:https://www.fastly.com/blog/summary-of-june-8-outage(原文 "all times are in UTC")
- 潜伏代码:"On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances."
- 触发:"Early June 8, a customer pushed a valid configuration change that included the specific circumstances that triggered the bug, which caused 85% of our network to return errors."
- 时间线:"09:47 Initial onset of global disruption" / "09:48 Global disruption identified by Fastly monitoring" / "09:58 Status post is published" / "10:27 Fastly Engineering identified the customer configuration" / "10:36 Impacted services began to recover" / "11:00 Majority of services recovered" / "12:35 Incident mitigated" / "17:25 Bug fix deployment began"
- 摘要:"We detected the disruption within one minute, then identified and isolated the cause, and disabled the configuration. Within 49 minutes, 95% of our network was operating as normal."
- 教训:"We'll figure out why we didn't detect the bug during our software quality assurance and testing processes."
- 客户配置变更的时刻:未披露。05-12 那次软件部署有没有走 canary:未披露。

### 案例 5:Meta/Facebook 骨干网(2021-10-04)
来源:
- https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/
- https://engineering.fb.com/2021/10/04/networking-traffic/outage/

两篇摘引:
- 触发:"During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintentionally took down all the connections in our backbone network"
- 防护失效:"Our systems are designed to audit commands like these to prevent mistakes like this, but a bug in that audit tool prevented it from properly stopping the command."
- 定位受阻:"the total loss of DNS broke many of the internal tools we'd normally use to investigate and resolve outages like this."
- 缓解:"we sent engineers onsite to the data centers to have them debug the issue and restart the systems."
- 恢复时的冲击:"Individual data centers were reporting dips in power usage in the range of tens of megawatts"

**两篇官方文章都没有任何时间戳。** 影响开始、检测、定位、缓解时刻全部未披露。媒体常引的「约 6 小时」不是来自这两篇原文,所以不进表。

### 案例 6:AWS us-east-1 DynamoDB DNS(2025-10-19/20)
来源:https://aws.amazon.com/message/101925/
- 总时段:"While the event started at 11:48 PM PDT on October 19 and ended at 2:20 PM PDT on October 20, there were three distinct periods of impact"
- 根因类型:"The root cause of this issue was a latent race condition in the DynamoDB DNS management system that resulted in an incorrect empty DNS record for the service's regional endpoint"
- 检测、定位、缓解:"Engineering teams for impacted AWS services were immediately engaged and began to investigate. By 12:38 AM on October 20, our engineers had identified DynamoDB's DNS state as the source of the outage. By 1:15 AM, the temporary mitigations … By 2:25 AM, all DNS information was restored"
- 自愈失败:"the system was left in an inconsistent state that prevented subsequent plan updates from being applied by any DNS Enactors. This situation ultimately required manual operator intervention to correct."
- 次生故障的检测:"Our monitoring systems detected this at 6:52 AM",对应 "Between 5:30 AM and 2:09 PM PDT on October 20 some customers experienced increased connection errors on their NLBs"
- 恢复中的拥塞崩溃:"DWFM had entered a state of congestive collapse … Since this situation had no established operational recovery procedure"
- 教训:"We have already disabled the DynamoDB DNS Planner and the DNS Enactor automation worldwide."
- 首次检测的来源:**未披露**("immediately engaged" 没有说明是怎么知道的)。
- 这不是一次发布事故。它是自动化系统自身的潜伏竞态,放进来是作对照组。

### 案例 7:Azure Front Door QNBQ-5W8(2025-10-09)
来源:https://azure.status.microsoft/en-us/status/history/?trackingId=QNBQ-5W8
- 缺陷的来源:"a software defect in the latest version of the AFD control plane which had been rolled out six weeks prior to the incident, in line with our safe deployment practices."
- 保护系统曾经拦住过:"Our automated protection layer intercepted this in early update stages and prevented this metadata from propagating any further to the data plane, thereby averting any customer impact at that time."
- 绕过保护:"we temporarily bypassed it to allow the cleanup of the tenant configuration to proceed. By bypassing the protection system, the erroneous metadata was inadvertently able to propagate to later stages"
- 时间线:"07:30 UTC … The cleanup operation was initiated." / "07:50 UTC … Initial customer impact began" / "08:13 UTC … Our telemetry detected resource availability loss across multiple AFD edge sites." / "09:04 UTC … We identified that the crashes were due to the previously identified data plane bug." / "09:08 UTC … Automated restarts began …" / "12:50 UTC … Availability for AFD fully recovered" / "16:00 UTC … we declared the incident as mitigated"
- 教训:"We have hardened our standard operating procedures, to ensure that the configuration protection system is not bypassed for any operation."

### 案例 8:Azure Front Door YKYN-BWZ(2025-10-29)
来源:https://azure.status.microsoft/en-us/status/history/?trackingId=YKYN-BWZ
- 测试漏掉了什么:"This defect escaped detection due to a gap in our pre-production validation, since not all features are validated across different control plane build versions."
- 渐进发布与健康门控:"Azure Front Door employs multiple deployment stages, and a configuration protection system … advances only after receiving positive health signals from the data plane." 以及 "The configuration protection system waits for approximately a minute between each stage, completing on an average within 5-10 minutes globally."
- **canary 为什么没拦住**:"Our configuration propagation monitoring continued to receive healthy signals – although the problematic metadata was present, it had not caused any issues. Because the data plane crash surfaced asynchronously, after approximately five minutes, the configuration passed through the protection safeguards and propagated to later stages."
- 自动回滚的基线被污染:"Since the incompatible customer configuration metadata was deployed successfully to the majority of fleet with positive health signal, the LKG was also updated with this configuration." 以及 "Since the latest 'last known good' (LKG) version was updated with the conflicting metadata, we chose not to revert to it."
- 检测:"The issue started at 15:41 UTC and was detected by monitoring at 15:48 UTC, prompting our investigation. By 15:43 UTC the configuration protection system activated … and automatically blocked all new and in-flight configuration changes from being deployed worldwide."
- 时间线:"15:35 UTC … Corrupt metadata first introduced" / "16:15 UTC … Focus of the investigation became examining AFD configuration changes." / "17:10 UTC … Began updating the 'last known good' LKG configuration to remove problematic configurations manually." / "17:40 UTC … Initiated the deployment of our updated 'last known good' configuration." / "18:30 UTC … AFD DNS servers recovered" / "00:05 UTC on 30 October 2025 – AFD impact confirmed mitigated for customers"
- 教训:增加「'pre-canary' stage」和「extending the bake time」;"improvements to the data plane recovery time from approximately 4.5 hours to approximately one hour"

### 案例 9:Cloudflare Bot Management 特征文件(2025-11-18)
来源:https://blog.cloudflare.com/18-november-2025-outage/(原文 "all times in this blog are UTC")
- 正文写的影响开始:"On 18 November 2025 at 11:20 UTC … Cloudflare's network began experiencing significant failures"
- 表格写的影响开始:"11:28 / Impact starts. / Deployment reaches customer environments, first errors observed on customer HTTP traffic."
- 变更:"11:05 / Normal. / Database access control change deployed."
- 检测:"The first automated test detected the issue at 11:31 and manual investigation started at 11:32. The incident call was created at 11:35."
- 误判:"After we initially wrongly suspected the symptoms we were seeing were caused by a hyper-scale DDoS attack"
- 间歇性干扰诊断:"every five minutes there was a chance of either a good or a bad set of configuration files being generated and rapidly propagated across the network."
- 定位与缓解:"13:37 / Work focused on rollback of the Bot Management configuration file to a last-known-good version." / "14:24 / Stopped creation and propagation of new Bot Management configuration files." / "14:30 / Main impact resolved." / "17:06 / All services resolved. Impact ends."
- 教训:"Hardening ingestion of Cloudflare-generated configuration files in the same way we would for user-generated input" 以及 "Enabling more global kill switches for features"

### 案例 10:Cloudflare FL1 WAF(2025-12-05)
来源:https://blog.cloudflare.com/5-december-2025-outage/
- 两个变更,只有第一个走了渐进发布:"This first change was being rolled out using our gradual deployment system." 以及 "This second change of turning off our WAF testing tool was implemented using our global configuration system. This system does not perform gradual rollouts, but rather propagates changes within seconds to the entire fleet of servers in our network"
- 时间线:"08:47 / INCIDENT start / Configuration change deployed and propagated to the network" / "08:48 / Full impact" / "08:50 / INCIDENT declared / Automated alerts" / "09:11 / Change reverted" / "09:12 / INCIDENT end"
- 教训:"data used for rapid threat response and general configuration needs to have the same safety and blast mitigation features. This includes health validation and quick rollback capabilities"
- 和 11-18 的共性(原文自己说的):"In both cases, a deployment to help mitigate a security issue for our customers propagated to our entire network and led to errors for nearly all of our customer base."

### 案例 11:Cloudflare BYOIP 前缀撤销(2026-02-20)
来源:https://blog.cloudflare.com/cloudflare-outage-february-20-2026/
- 正文写的开始时刻:"On February 20, 2026, at 17:48 UTC, Cloudflare experienced a service outage"
- 时间线:"2026-02-05 21:53 / Code merged into system" / "2026-02-20 17:46 / Code deployed into system" / "2026-02-20 17:56 / Impact Start" / "2026-02-20 18:13 / Cloudflare engaged / Cloudflare engaged for failures on one.one.one.one" / "2026-02-20 18:18 / Internal incident declared" / "2026-02-20 18:21 / Addressing API team paged" / "2026-02-20 18:46 / Issue identified / Broken sub-process terminated by an engineer" / "2026-02-20 19:11 / Mitigation begins" / "2026-02-20 23:03 / … IMPACT ENDS"
- 渐进发布限制了爆炸半径:"This incident did not impact all BYOIP customers because the configuration change was applied iteratively and not instantaneously across all BYOIP customers."
- staging 为什么没发现:"Our staging environment contains data that matches Production as closely as possible, but was not sufficient in this case and the mock data we relied on to simulate what would occur was insufficient." 以及 "testing did not cover a scenario where the task-runner service would independently execute changes to user data without explicit input."
- 教训:"We will improve our monitoring to detect when changes are happening too fast or too broadly … This will form a type of circuit breaker"

---

## 2. 跨案例论断(编号;口径写在每条后面)

**C1 全局推送绕过 canary 是最常见的形态。** 11 案里,原文明确说触发变更走了「全局 / 几秒内全网 / 没有渐进发布」路径,或者绕过了保护系统的有 6 案:CrowdStrike、Google(策略数据)、CF-2019、CF-2025-11、CF-2025-12、AFD-10-09。另外 2 案的触发方式是全局性的,但原文没有用 rollout 的语言来描述:Meta 是全局命令,Fastly 是客户配置。
口径:分母是 11 个结构化案例。AWS 不算发布事故。Fastly 和 Meta 不计入那 6 案。

**C2 「代码走了渐进发布,配置/数据没走」反复出现。** CrowdStrike 的 Sensor Content 走分阶段,Rapid Response Content 没走。Cloudflare 2019 的软件走 DOG/PIG/Canary,WAF 规则按设计不走。Google 的二进制逐 region 发布,策略数据几秒内全球复制。Cloudflare 2025-12 的第一个变更走渐进,第二个走全局配置系统。
口径:4 案,都有原文直说。

**C3 已披露的 TTD 普遍是分钟级。** 能从原文时刻算出 TTD 的有 8 案:Fastly 1、Google ≤2、AFD-29 2(冻结)或 7(告警)、CF-2019 ~3、CF-11 3、CF-12 3、CF-2026 17、AFD-09 23,单位都是分钟。**中位数约 3 分钟。**
口径:「影响开始」用各家自己的定义。CF-11 和 CF-2026 的正文和表格对不上,改用正文时刻的话两者分别变成 11 和 25 分钟,中位数仍然是 3。CrowdStrike、Meta、AWS 主故障这 3 案未披露,不能当作 0 计入。

**C4 首次发现来源:原文明确是自动信号的 6 案;明确是客户报告的 0 案。** 6 案是 CF-2019(外部合成测试)、Fastly(monitoring)、AFD-09(telemetry)、AFD-29(保护系统自动冻结和监控告警)、CF-11(automated test)、CF-12(automated alerts)。Google 只写了「SRE … triaging」,CF-2026 只写了「engaged for failures on one.one.one.one」,两者都没说明来源。CrowdStrike、Meta、AWS 未披露。
口径:分母 11。选择偏差:厂商在复盘里更愿意写「监控 1 分钟发现」。没写发现来源本身就是一种信号。

**C5 检测快,但定位/缓解慢,这是主流形态。** TTD ≤5 分钟的 6 案里(Fastly、Google、AFD-29、CF-2019、CF-11、CF-12),有 4 案主要缓解超过 1 小时:Fastly 2h48m、Google ~3h、AFD-29 8h24m、CF-11 3h02m。只有 CF-2019(27 分钟)和 CF-12(25 分钟)在 1 小时内缓解,两者都靠现成的全局 kill switch 或直接 revert。
口径:派生值,「主要缓解」按各家口径。

**C6 11 案里,没有一案的主要缓解是靠自动回滚完成的。** 自动化做到的最多是「自动停止继续传播」(AFD-29 在 15:43 自动冻结)或「自动重启」(AFD-09)。AFD-29 本来设计了自动回滚到 LKG,但 LKG 已经被坏配置污染,只能人工编辑。Google、CF-2019、CF-11、CF-12、CF-2026、CrowdStrike 都是人工 revert、人工 red-button 或人工 kill switch。
口径:按原文对缓解动作的描述判断。

**C7 离线验证漏掉的问题有共性:都是「合法但没见过的输入形状」触发了潜伏代码路径,而且常常有时间延迟。** 输入形状包括:CrowdStrike 21 个字段 vs 20 个输入、Google 策略的空字段、CF-11 特征数超过 200、Fastly 的特定客户配置、AFD-29 跨控制面版本的元数据、CF-2026 的空字符串参数、CF-2019 正则回溯导致的 CPU 耗尽(测试只检查功能,不检查 CPU)。潜伏期:Google 14 天、Fastly 27 天、AFD-09 6 周、CF-2026 合并后 15 天,AFD-29 异步约 5 分钟后才崩。
口径:7 案原文有明确机制描述。潜伏天数由原文日期相减得到。

**C8 canary 结构性看不见的东西有两类:一是延迟发作的故障,二是要等别的变更才会触发的代码路径。** AFD-29:健康信号在 crash 之前就放行了,而且把坏配置写进了 LKG。Google:"the code path that failed was never exercised during this rollout"。这两案都是走了渐进发布、仍然漏掉的反例。
口径:2 案原文直说。CF-2026 是「渐进发布有效限制了爆炸半径」的正例(25%)。

**C9 定位慢的常见原因:误判为攻击、间歇性症状、工具自身依赖故障设施。** 误判为攻击:CF-2019、CF-11。间歇性症状:CF-11 每 5 分钟好坏交替。工具依赖:Meta 的内部工具和带外网络断了,CF-2019 进不去 Jira 和构建系统,Google 的状态页本身挂了,AFD 的 Premier 客户无法开支持单。
口径:定性,均有原文。

**C10 缓解后的恢复长尾往往比检测加定位还长,主因是群体效应和积压。** Google us-central1 出现 herd effect,最长 ~2h40m。CF-11 先是 dashboard 登录积压,随后到 17:06 才恢复。AWS DWFM 出现「congestive collapse」,EC2 到 13:50 PDT 才恢复。AFD-29 重载配置加流量再平衡,原文说 "approximately 4.5 hours"。Meta 有数十兆瓦级的功耗回冲风险。
口径:5 案原文。

---

## 3. 交叉口径问题清单

1. **影响开始时刻,同一篇文章内部自相矛盾**:CF-2025-11-18 正文写 11:20,表格写 11:28;CF-2026-02-20 正文写 17:48,表格写 17:56。TTD 相差 8 分钟。建议主文用表格时刻,并脚注写明另一个。
2. **「78 分钟」常被误读**:它是 CrowdStrike 发布 → revert 的间隔,不是检测时间,也不是恢复时间。CrowdStrike 官方从未披露检测时刻、发现来源,也没有给主机恢复的时长。
3. **Google 的时间大多是相对表述**:「Within 2 minutes / 10 minutes / ~25 / 40 minutes」都是近似上界,「~10:45am」带约号。由此换算出的 UTC 时刻只能写成「约 / ≤」。
4. **「检测」的定义不一**:AFD-29 有两个时刻,15:43 保护系统自动冻结、15:48 监控告警触发人工调查,TTD 取 2 分钟还是 7 分钟要统一。Google 的「SRE triaging」也不等于告警时刻。
5. **「缓解」的定义不一**:AFD-09 可用性 12:50 恢复,但到 16:00 才宣布缓解(以延迟为准);Google 分「除 us-central1 外」和「结束」两个时刻;Cloudflare 分「主要影响解决」和「全部解决」。MTTR 不能直接横比。
6. **Meta 2021 没有官方时间戳**:媒体和第三方给出的约 6 小时以及 15:39 UTC 起始,都不是 Meta 原文,不能进数据表。
7. **AWS 不是发布事故**:它是自动化系统的潜伏竞态。如果主文统计「坏发布」,应把 AWS 从分母里剔除。剔除后分母是 10,C1 的 6/11 变成 6/10。
8. **发现来源存在选择偏差**:官方复盘只在发现得快时才倾向写来源。11 案里有 5 案来源不明或模糊,不能据此推出「自动告警占比 ≥55%」这类总体比例。
9. **样本偏差**:这些案例全部是大厂、全局性、公开写了复盘的事故。正好是 canary 被绕过、影响面巨大的那一类。它们不能代表「多数生产事故」的 TTD 分布(多数事故没有公开复盘)。
10. **Fastly 的触发时刻**:客户配置推送的具体时刻未披露,所以无法区分「变更 → 影响」的延迟。
