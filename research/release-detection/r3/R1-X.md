# R3 反证搜索：R1（POSTMORTEM 线 11 案）

审查日期：2026-10-30。方法是用独立团队和独立数据去找能证实或矛盾 R1 五条结论的测量。
下载件放在 scratchpad `dl/r3-R1-X/`，都是只读的纯文本；curl 只带通用 UA，没有任何个人信息。
标「原文」的引文是用 pdftotext 或 HTML 去标签后 grep 到的逐字原文。标「摘要」的来自 WebSearch/WebFetch 的模型摘要，没有逐字核过。

## 0. 先说结论

| R1 结论 | 判定 | 一句话理由 |
|---|---|---|
| 可计算 TTD 的 8 案中位数约 3 分钟 | **方向存争** | 大样本里监控检测确实占多数，但客户/人工报告的事故检测慢约 10 倍。公开复盘选中的是「炸得响」的事故，3 分钟不能外推 |
| 自动信号先发现 6/11，客户先发现 0/11 | **降级**（指「客户先发现≈0」这一面） | Microsoft 大样本里人工报告占 3.3%–38.3%；独立案例 Atlassian 2022、Optus 2025 都是客户先发现 |
| 6/11 走全局推送、没有渐进发布或绕过了保护 | **多源证实（方向）**；比例本身没有大样本可比 | Google 内部 2010–17 年配置推送占触发原因的 31%；Datadog 2023、Heroku 2025、AT&T 2024、Optus 2025 都是同类模式 |
| TTD≤5 分钟的 6 案中 4 案缓解超过 1 小时（检测快、缓解慢） | **多源证实（方向）**；倍数没有大样本测量 | Teams、Microsoft GenAI、LLM 状态页、AT&T、Datadog 都指向缓解时间远长于检测时间 |
| 没有一案主要靠自动回滚 | **单源已核**（只在样本内成立），**不可外推** | Slack、GitHub 的数据显示，常规部署事故里自动回滚很有效；R1 样本只选了自动回滚失效的灾难级事故 |

## 1. 搜索角度清单（包括没搜到的）

1. **学术大样本：Microsoft 事故研究**。搜到 3 篇，都是承重证据：
   - FSE'23《Detection Is Better Than Cure》：306 个服务，2022 年；
   - arXiv 2504.08865（GenAI 云服务事故）；
   - SoCC'22《How to Fight Production Incidents》：Teams，152 起事故。
2. **VOID（Verica Open Incident Database）**。只搜到二手报道，结论是事故时长偏态、不该用均值，以及「时长和严重度不相关」。**没找到 VOID 关于检测来源或 TTD 的数据**；VOID 收录的公开报告大多不写影响开始时刻。
3. **Dan Luu 的 post-mortems 列表和《Reading postmortems》**。只有非正式观察：搜「global outage postmortem」，约 50% 是配置变更引起的（摘要）。**没有检测来源的统计。**
4. **Gunawi 等人 SoCC'16（597 起公开宕机）**。355 起没有根因。**没拿到 TTD 或检测来源的数字**，PDF 没有下载。
5. **公开状态页的大规模分析**：
   - Chu 等人 ICPE'25（OpenAI/Anthropic/Character.AI，状态页报告）：明确**测不了 TTD**，时间线从「investigating」才开始。
   - Nokia Bell Labs（152 个服务，11000 多起事故）：只看到摘要。
   - StatusGator / IsDown：有「第三方先于官方状态页」的例子，属于厂商营销数据，没有采用。
6. **行业调查**：
   - NeuBird 2026：78% 的受访者遇到过「没有告警、客户先发现」至少一次。这是厂商调查，衡量的是「是否发生过」，不是比例。
   - Forrester 旧数据（「end users report nearly three-quarters of outages」）：来自二手转述，年份和方法不明，没有采用。
   - PagerDuty：没有检测来源的数据。
   - **incident.io 和 Statuspage 官方统计：没搜到。**
7. **Google SRE**：
   - Workbook 附录 C 是触发原因表，原页已核：binary push 37%、configuration push 31%。**它没有检测来源的数据。**
   - 博客《Shrinking the time to mitigate》没有抓到原文。
8. **2022–2026 客户或外部先发现的大事故**。找到的有：
   - Atlassian 2022（原文已核）；
   - Optus 2025（只有二手报道，Schott 报告原文没有下载）；
   - AT&T 2024（FCC 报告只有二手报道）。
   - **没找到** 2024–2026 年由云/CDN 大厂自己承认「客户先发现」的复盘。GitHub 状态页常写「investigating reports」，但没有明说首次检测来源。
9. **自动回滚在大样本里的作用**：
   - Slack Deploy Safety（原文已核）；
   - GitHub 2025-07-15 状态页（摘要，没有核原文）；
   - Microsoft 两篇论文的缓解方式分布。
10. **非中国大陆以外的其他大样本**（Alibaba、ByteDance、Huawei、Meta 的 TTD 中位数）：**没搜到**带分钟级中位数的论文。看到一份 TU Delft 的论文（979 份报告里分析了 258 份），研究变更类别和 TTD/TTR 的关系，但没有读全文。

## 2. 证据明细

### 2.1 检测来源比例（反驳「客户 0/11」）

- **Microsoft FSE'23**（原文，`fse23.txt`）：
  > "Figure 1(c) delineates the proportion of incidents (across 306 services in year 2022) detected by monitors and other sources. While majority (96.7%) of the incidents were detected by monitors, we still observe several human (either by customers or internal engineers) reported incidents."

  同一篇，关于检测时长（原文）：
  > "Customer and engineer reported incidents, on average take, ∼ 10.7x and 9.96x times longer to be detected than monitor reported incidents."

  > "customer reported incidents took ∼ 3.75x longer to be mitigated than monitor-detected incidents."

  另外，该文研究的 950 多起事故里，漏检的原因有 40% 以上是缺少监控（原文："for more than 40% of the cases a relevant monitor was not present"）。
- **Microsoft GenAI 研究**（arXiv 2504.08865，摘要）：

  | 服务类型 | 监控检测 | 人工报告 |
  |---|---|---|
  | GenAI 服务 | 61.7% | 38.3% |
  | 其他服务 | 86.3% | 13.7% |

  该文没有把人工报告再拆成客户和内部工程师。
- **Teams SoCC'22**（幻灯片原文，`teams-slides.txt`）：检测环节「Not Failed — 52.0 %」，也就是约一半事故的检测有缺陷；其中缺监控或缺遥测覆盖的占 17%。
- **Atlassian 2022-04**（PIR 原文，`atl.txt`）：
  > "The first support ticket was created by an impacted customer at 07:46 UTC on April 5th. Our internal monitoring did not detect an issue because the sites were deleted via a standard workflow."

  脚本 07:38 开始运行，客户在 8 分钟后报告；08:17 启动重大事故流程；最长中断 14 天。这一案的 TTD 很短，但信号来自客户。
- **Optus 2025-09-18**（The Register 对 Schott 独立评审的报道，摘要）：防火墙升级后，紧急呼叫约 14 小时无法路由。2:40 AM 的变更后检查中，失败率在上升但「The anomaly was not picked up」；聚合数据「not sufficiently granular」。公司最终是从客户打到客服中心的投诉才知道的。这是**信号存在但被平均掉**的典型。

**小结**：在成熟云厂商内部，监控先发现确实是主流（86%–97%）。但「客户先发现」并不是 0：总体占 3%–14%，AI 服务占 38%。而且客户先发现的那部分检测慢约 10 倍、缓解慢约 3.75 倍，正是尾部风险所在。R1 的 0/11 是样本选择的结果：公开写长篇复盘的，多是监控成熟、影响面巨大的事故。

### 2.2 TTD 分布

能直接比对「影响开始 → 首次检测」分钟级分布的大样本数据**没有找到**：
- 状态页数据结构上测不了 TTD（ICPE'25 明确说明）；
- Microsoft 的几篇论文只给倍数，或者给「time units」。

已知的独立单案 TTD：

| 案例 | TTD | 来源 |
|---|---|---|
| Datadog 2023-03-08 | 3 分钟，内部监控 | 官方复盘，摘要 |
| AT&T 2024-02-22 | 变更 2:42 → 中断 2:45；检测时刻未知 | FCC，二手 |
| Atlassian 2022 | 8 分钟，客户 | 原文 |
| Optus 2025 | 数小时，客户 | 二手 |

所以「大事故分钟级就能被发现」在**全面、大爆炸半径**的事故上大体成立；**局部或静默故障**（Optus、Atlassian 的「standard workflow」）是反例。

### 2.3 全局推送、绕过渐进发布

- **Google 内部**（SRE Workbook 附录 C，原页）：2010–2017 年的触发原因里，Configuration push 占 31%，Binary push 占 37%。表里没有区分是否走了渐进发布。
- **Datadog 2023**（摘要）：遗留的自动安全更新通道把 systemd 更新推到多个区域的 VM 上，US1/EU1/US3/US4/US5 同时受影响。事后停用了该通道。
- **Heroku 2025-06-10**（官方，摘要）：起因是「unintended system update applied to our production infrastructure by our vendor」，故障约 24 小时。
- **AT&T 2024**（FCC，二手）：变更没有按内部同行评审程序执行。
- **Optus 2025**：变更被标为 urgent，跳过了常规工程评审。
- **Slack**（原文）：73% 的客户可见事故是自家变更触发的。

**小结**：变更，尤其是配置和平台层推送，是主要触发原因，这一点多源一致；「绕过保护」反复出现。但「全局推送占 X%」**没有大样本比例**，R1 的 6/11 只能当作样本内描述。

### 2.4 检测快、缓解慢

- **Teams**（原文）：缓解延迟里有 30% 源于文档、流程和手工部署步骤；配置 bug 有 47% 靠回滚缓解。
- **LLM 状态页**（ICPE'25，摘要）：investigating 阶段算术均值 0.84 小时，repairing 1.40 小时，checking 1.58 小时；MTTR 中位数约 1 小时。注意：论文的表内数字自相矛盾，只能看量级。
- **单案**：
  - AT&T：回滚花了近 2 小时，全面恢复至少 12 小时（二手）；
  - Datadog：3 分钟检测，恢复超过 24 小时；
  - Heroku：08:26 确认核心症状，次日 05:50 才结束。

**小结**：方向一致，「发现不难，恢复难」。但大样本里没有同一事故内 TTD 对比 TTM 的分布，「4/6」这个比例不能外推。

### 2.5 自动回滚

- **Slack**（原文）："Once automatic rollbacks were introduced we observed dramatic improvement in results." 客户影响小时数从峰值下降 90%；目标是「Automated detection & remediation within 10 minutes」「Detect problematic deployments prior to reaching 10% of the fleet」。
- **GitHub 2025-07-15**（状态页，摘要，原文未核）：数据库查询变更 19:55–19:58 UTC，被部署工具自动检测并回滚，全程 3 分钟。
- **Microsoft 的回滚比例**：

  | 样本 | 回滚占缓解方式 | 其中 |
  |---|---|---|
  | Teams | 22.4% | — |
  | GenAI 研究 | 15.2% | 部署回滚 8.9%，配置回滚 6.3% |

  两篇都没有区分自动回滚和人工回滚。

**小结**：自动回滚在常规部署事故里大量起作用，所以这些事故不会变成需要长篇公开复盘的灾难。R1 的「没有一案主要靠自动回滚」是**幸存者偏差的另一面**：进入样本的条件之一，往往就是自动回滚没有接住。

## 3. 成文时可以怎么说、不能怎么说

**可以说：**
- 「在我们读的 11 份大厂公开复盘里，能算出 TTD 的 8 案中位数约 3 分钟，首次信号多来自自动监控。」必须带上样本限定。
- 「Microsoft 2022 年 306 个服务的数据：96.7% 的事故由监控发现；但客户报告的事故平均晚约 10.7 倍才被发现、缓解慢约 3.75 倍。」(FSE'23)
- 「AI 服务的人工报告占比明显更高：38.3% 对比其他服务的 13.7%。」(Microsoft，arXiv 2504.08865)
- 「变更是事故的头号触发原因（Google 2010–17：binary push 加 config push 约占 2/3；Slack：73%）。全局配置或平台推送绕过渐进发布，在多家公司反复出现。」
- 「检测快、缓解慢在多个独立案例和研究里方向一致。」
- 「常规部署事故里，自动检测加自动回滚能把影响压到 10 分钟以内（Slack）。灾难级事故恰恰是它没接住的那类。」

**不能说：**
- 「线上问题通常几分钟内就会被发现。」这是把公开大事故样本外推到全部事故。
- 「客户先发现的情况几乎不存在。」反例有 Microsoft 3%–38%、Atlassian、Optus。
- 「X% 的大事故源于全局推送绕过渐进发布。」没有大样本比例。
- 「自动回滚没用」或「大事故都靠人工」。这是选择偏差。
- 引用 NeuBird 78% 或 Forrester「四分之三」当作客户先发现的比例。前者衡量「是否遇到过」，后者来源不明。
- 引用 ICPE'25 的阶段均值做精确比较。表内数字自相矛盾。

## 4. 来源

- Ganatra 等，FSE'23：https://jonathanmace.github.io/papers/ganatra2023detection.pdf （本地 `fse23.txt`）
- Microsoft GenAI 事故研究：https://arxiv.org/html/2504.08865v2
- Ghosh 等，SoCC'22 幻灯片：https://asatarin.github.io/assets/talks/2023-01-how-to-fight-production-incidents.pdf （本地 `teams-slides.txt`）
- Google SRE Workbook 附录 C：https://sre.google/workbook/postmortem-analysis/
- Chu 等，ICPE'25：https://arxiv.org/html/2501.12469v1
- Atlassian PIR：https://www.atlassian.com/engineering/post-incident-review-april-2022-outage （本地 `atl.txt`）
- Optus（Schott 评审）：https://www.theregister.com/2025/12/19/optus_emergency_outages_cause_report/
- AT&T FCC 报告（二手）：https://www.fierce-network.com/wireless/fcc-reports-atts-nationwide-outage-february
- Datadog：https://www.datadoghq.com/blog/engineering/2023-03-08-multiregion-infrastructure-connectivity-issue/
- Heroku：https://www.heroku.com/blog/summary-of-june-10-outage/
- Slack：https://slack.engineering/deploy-safety/ （本地 `slack.txt`）
- Dan Luu：https://danluu.com/postmortem-lessons/
