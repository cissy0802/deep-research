# 22. Round 1 原始论断(5 线合并)


---

# CHANGE 线:变更与事故的基本事实(截至 2026 年 10 月)

研究总题:AI 能接住坏发布吗。本线独占产出:「事故从哪来、谁发现的」基础数据。
三段严格区分:检测(TTD)/ 定位(RCA)/ 缓解。MTTR 不作检测速度证据。

来源类型:同行评审 / 官方一手 / 厂商自报 / 从业者博客 / 媒体转述 / 分析机构

---

## C01 Google SRE 书「约 70% outage 来自线上系统变更」
- 论断:Google SRE 书第 1 章 Introduction「Change Management」小节称约 70% 的 outage 由线上系统变更引起。原文**不给分子分母、时间窗或数据来源**,是经验断言(rule of thumb 级)。同章另有一句更弱的定性表述「most outages are caused by some kind of change」,且把「a new type of user traffic」也算作 change——即书中的「change」比「代码/配置推送」宽。
- 原文:"SRE has found that roughly 70% of outages are due to changes in a live system." / "Because most outages are caused by some kind of change—a new configuration, a new feature launch, or a new type of user traffic—the two teams' goals are fundamentally in tension."
- URL:https://sre.google/sre-book/introduction/
- 日期:2016(O'Reilly 出版;在线版持续可访问,2026-10-30 抓取核对)
- 来源类型:官方一手(无数据口径)
- 承重:是
- 叙事:支持「变更是主因」,但口径缺失

## C02 Google SRE Workbook 附录 C:2010–2017 触发因素分布
- 论断:Google 基于「过去七年数千份 postmortem 抽样」统计 top 8 outage 触发因素:binary push 37%、configuration push 31%,合计 68%(这是 70% 说法最接近的可追溯数据);其余 user behavior change 9%、processing pipeline 6%、service provider change 5%、performance decay 5%、capacity management 5%、hardware 2%。口径:分母为「sample of thousands of postmortems」(非全部事故,只含写了 postmortem 的事故,有选择偏差);是「trigger」不是「root cause」;只列 top 8。同附录 root-cause 分类中 Software 41.35%、Development process failure 20.23%、Complex system behaviors 16.90%、Deployment planning 6.74%、Network failure 2.75%。
- 原文:"Table C-1 shows the breakdown of our top eight triggers for outages, based on a sample of thousands of postmortems over the last seven years." / "Table C-1. Top eight outage triggers, 2010–2017 … Binary push 37% … Configuration push 31% … User behavior change 9% … Processing pipeline 6% … Service provider change 5% … Performance decay 5% … Capacity management 5% … Hardware 2%"
- URL:https://sre.google/workbook/postmortem-analysis/
- 日期:2018(The Site Reliability Workbook)
- 来源类型:官方一手(厂商内部数据,但非营销语境)
- 承重:是(70% 说法的唯一可追溯数据锚点)
- 叙事:支持「变更是主因」;同时注意配置推送(31%)与代码推送(37%)量级相当

## C03 Google Workbook 第 16 章 Canarying:多数事故由二进制或配置推送触发
- 论断:Workbook 金丝雀章节以定性方式复述附录 C,并指出 canary 能发现「单测、压测等测试框架看不到」的问题——即测试漏网问题需真实流量才暴露。
- 原文:"In Google's experience, a majority of incidents are triggered by binary or configuration pushes (see Results of Postmortem Analysis)." / "Introducing the change to actual production traffic also enables us to identify problems that might not be visible in testing frameworks like unit testing or load testing, which are often more artificial."
- URL:https://sre.google/workbook/canarying-releases/
- 日期:2018
- 来源类型:官方一手
- 承重:否(辅证)
- 叙事:支持变更主因 + 支持「离线测试有结构性盲区」

## C04 Microsoft Teams 152 起高严重度事故:只有约 55% 由自动监控发现,29% 由外部用户/客户报告
- 论断:Ghosh et al.(SoCC'22 Best Paper)分析 Microsoft Teams 一个 12 个月窗口内 152 起高严重度(Sev 0/1/2)事故:约 55% 由自动 watchdog 检出;其余 45% 中,29% 由外部用户/客户报告、10% 由微软内部伙伴团队发现、6% 由服务团队自己发现。口径:分母 152 起;已过滤约 35% 缺乏详细根因/缓解描述的事故(选择偏差);单一服务(Teams);作者明言可能不可推广。
- 原文:"we observe that about 55% of the incidents were detected by the automated watchdogs. … Among other 45% incidents, 29% incidents are reported by the external users or customers, and 10% are identified by the partner teams within Microsoft. The remaining 6% incidents are detected by the Microsoft-Teams's service team itself."
- URL:https://www.microsoft.com/en-us/research/wp-content/uploads/2022/09/3542929.3563482.pdf
- 日期:2022-11(SoCC'22)
- 来源类型:同行评审(作者为微软研究员,自家数据)
- 承重:是(「谁发现的」核心数字)
- 叙事:反对「监控/AIOps 已能接住大多数问题」——即便在顶级云厂商,近半高严重度事故不是监控先发现的

## C05 同上:代码 bug 类事故检测最慢,无监控事故 70% 根因为代码 bug
- 论断:同一研究发现代码 bug 与依赖故障的 TTD 显著高于其他根因;约 17% 事故缺监控或缺 telemetry;没有监控覆盖的事故中 70% 根因是代码 bug,作者结论是「对代码变更应加强测试而非依赖监控」。TTD 只给出**归一化**值(以全部事故中位数为 1)、去掉 10% 离群,未给绝对分钟数。
- 原文:"Finding#5: The time-to-detect code bugs and dependency failures is significantly higher than other root causes, indicating inherent difficulties in monitoring such incidents." / "Finding#7: ≈17% of incidents either lacked monitors or telemetry coverage, both of which result in significant detection delays." / "Finding#11: 70% of incidents with no monitors were root caused to code bugs, i.e., it is inherently difficult to monitor regressions introduced due to code changes. ⇒ For code changes, we should improve testing rather than relying on monitoring."
- URL:同 C04
- 日期:2022-11
- 来源类型:同行评审
- 承重:是
- 叙事:反对「上线后检测可兜底代码回归」;支持「代码类坏变更是检测盲区」

## C06 同上:根因分布——代码/配置 bug 仅 40%,60% 为基础设施、部署、依赖
- 论断:152 起事故根因:Code Bug 27.0%、Dependency Failure 16.4%、Infrastructure 15.8%、Deployment Error 13.2%、Config Bug 12.5%、Database/Network 10.5%、Auth Failure 4.6%。「部署错误」中 55% 是证书管理(过期/错证书)。缓解:近 80% 事故无需改代码/配置即被缓解,回滚是主流;47% 配置 bug 用回滚缓解。注意:这是「根因」分类,不是「触发」分类,与 Google 附录 C 的 trigger 口径不可直接比较;且很多「依赖故障」本身是伙伴团队的变更(External code change 占依赖故障 28%)。
- 原文:"Finding#1: While 40% incidents were root caused to code or configuration bugs, a majority (60%) were caused due to non-code related issues in infrastructure, deployment, and service dependencies." / "Finding#2: Although 40% incidents were caused by code/configuration bugs, nearly 80% of incidents were mitigated without a code or configuration fix."
- URL:同 C04
- 日期:2022-11
- 来源类型:同行评审
- 承重:是(反方:非代码原因占多数)
- 叙事:部分反对「代码/配置变更是主因」;但「变更」广义(含部署操作、伙伴变更)仍占大头——取决于口径

## C07 Microsoft GenAI 云服务事故(2025):人工报告比例 38.3% vs 其他服务 13.7%;监控误报率 11.0% vs 3.8%
- 论断:Yan et al.(Microsoft + 高校,arXiv 2504.08865v2,2025-08)分析微软近四年 GenAI 相关事故(全量「数十万」条用于检测类型统计;深度分析只取高严重度子集):GenAI 事故 38.3% 由人(工程师/客户)报告、61.7% 由监控发现;对照组其他云服务人工报告仅 13.7%(监控 86.3%)。监控发现的事故中「误报」比例 GenAI 11.0%、其他 3.8%。口径:「false alarm」= 缓解步骤被标为 False Alarm 的事故占比(事后人工标注),不是告警级误报率;对照组「same number of other incidents」抽样。注意与 C04(Teams 高严重度,监控仅 55%)口径不同——这里很可能含大量低严重度事故,监控占比天然更高。
- 原文:"GenAI cloud services experience a higher rate of incidents detected by humans (38.3%) compared to other services (13.7%) rather than automated monitors. Also, there is a higher false alarm rate for GenAI (11.0%) versus other services (3.8%)"
- URL:https://arxiv.org/pdf/2504.08865
- 日期:2025-04 首版,v2 2025-08-14
- 来源类型:同行评审前预印本(作者含微软员工,自家数据)
- 承重:是(最新的「谁发现」数据;新型服务监控更差)
- 叙事:反对「监控已成熟」——新类型服务(GenAI)人工发现比例近 4 成;同时给出误报代价的一个基线

## C08 Gunawi et al. SoCC'16「Why Does the Cloud Stop Computing?」:597 次公开 outage,升级(UPGRADE)是最大已知根因之一(16%),配置 10%
- 论断:分析 32 个互联网服务 2009–2015 年的 1247 篇新闻与公开复盘、597 起非计划 outage。355 起(59%)根因未知;在已知根因标签中 UPGRADE 16%、NETWORK 15%、BUGS 15%、CONFIG 10%、LOAD 9%、CROSS(跨服务依赖)8%、POWER 6%、SECURITY 5%、HUMAN 4%、STORAGE 4%、SERVER 3%、NATURAL DISASTER 3%、HARDWARE 1%。口径:分母为「已知根因」标签计数(一起事故可多标签),样本来自**公开报道**(偏向大而显眼的 outage,非内部全量);「UPGRADE」含硬件升级与软件更新。作者指出开发者测试过升级,但推送到全生态时仍失败。
- 原文:"We analyzed 1247 headline news and public post-mortem reports that detail 597 unplanned outages that occurred within a 7-year span from 2009 to 2015." / "Table 3 shows that UPGRADE is one of the largest root causes (16%)." / "355 outages (out of the total 597) have UNKNOWN root causes. Among the outages with reported root causes, UPGRADE, NETWORK, and BUGS are three most popular root causes, followed by CONFIG and LOAD."
- URL:https://ucare.cs.uchicago.edu/pdf/socc16-cos.pdf
- 日期:2016-10(SoCC'16)
- 来源类型:同行评审(学术方,数据来自公开报道)
- 承重:是(独立于厂商的外部视角)
- 叙事:中性偏反方——按公开 outage 计,升级+配置合计约 26%,远低于 70%;但大量「未知根因」和多标签使比较不稳

## C09 Facebook(Tang et al. SOSP'15):三个月高影响事故中 16% 与配置管理有关,其余以软件 bug 为主
- 论断:Facebook 人工分析三个月窗口的高影响事故,16% 与配置管理相关,其余主要是软件 bug。配置相关事故内部:Type I 常见配置错误(拼写、越界、引错集群)42%、Type II 微妙配置错误(负载相关、故障诱发、蝴蝶效应)36%、Type III 合法配置变更暴露代码 bug 22%。口径:窗口仅 3 个月,未给事故总数;「配置相关」≠「变更触发」(软件 bug 事故大部分也是经代码发布进入生产的,但论文未按触发统计)。
- 原文:"we manually analyzed the high-impact incidents during a three-month period. We found that 16% of the incidents were related to configuration management, while the rest were dominated by software bugs." / "Type I: common config errors 42% / Type II: subtle config errors 36% / Type III: valid config changes exposing code bugs 22%"
- URL:https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/printable/008-tang.pdf
- 日期:2015-10(SOSP'15)
- 来源类型:同行评审(作者为 Facebook 员工,自家数据)
- 承重:是(配置 vs 代码占比的一个锚点)
- 叙事:对「配置推送是事故大头」的反例——在 FB 这个窗口里配置相关仅 16%,与 Google 附录 C 的 31% 差距大

## C10 Facebook 自动 canary 的三个真实案例:拦截成功、被工程师当误报覆盖、因规模太小漏掉负载问题
- 论断:同论文给出自动 canary 的正反案例:(a) 新配置先推 20 台机器,与其余生产机器比对错误日志,检测到 log spew 后中止发布,避免了 outage;(b) canary 因崩溃拒绝了一次配置变更,工程师认定是误报而强行覆盖,导致更多崩溃后回滚——配置本身正确,但触发了新代码路径上的竞态 bug;(c) 一次配置错误把移动请求导向罕见路径、压垮后端存储,小规模 canary 没有足够负载暴露问题,全站部署后才显现,此后加了「数千台服务器、集群级」canary 阶段。这是「canary 漏掉什么」与「误报信任代价」的一手质性证据。
- 原文:"It compared the error logs of those 20 servers with those of the rest of the production servers, and detected a log spew, i.e., rapid growth of error logs. It aborted the rollout and prevented an outage." / "'It must be a false positive of the canary tool!' She overrode the tool's rejection and deployed the config, which caused more crashes." / "At that time, automated canary tests did not catch the problem, because the testing was done on a limited number of servers and the small scale testing was insufficient to cause any load issue."
- URL:同 C09
- 日期:2015-10
- 来源类型:同行评审
- 承重:否(质性案例,但对「canary 漏网共性:规模相关/负载相关」承重)
- 叙事:双向——canary 有效,但规模依赖型问题会漏,且人对告警的不信任会抵消检测

## C11 Azure Gandalf(NSDI'20):测试-生产差异导致漏网;部分坏发布影响在数小时到数天后才显现;「100% recall」的定义很窄
- 论断:(a)漏网共性:微软指出即使充分测试,bug 仍因测试与生产在集群规模、硬件 SKU、OS/库版本、不可预测负载、复杂组件交互上的差异而漏到生产;组件级 watchdog 会漏「局部轻微、全局严重」的问题、几小时后才出现的潜伏问题(如内存泄漏)、跨组件 API 契约破坏。案例:一次 NIC 固件/驱动升级的问题在部署后 24–72 小时才引发 OS 崩溃;另一例潜伏问题部署后 >32 小时才检测到。(b)指标口径:Gandalf 自报数据面 precision 92.4%、recall 100%,但 recall 的定义是「没有 Sev0-2 高影响事故由坏 rollout 引起」——即以「漏到高影响事故的坏发布」为漏报,不是以全部坏发布为分母;控制面 1200+ 次区域级部署中提了 39 个事故、2 个误报、漏 2 个。窗口 2018-01 至 2018-11(8 个月),Azure Compute。
- 原文:"some bugs could remain uncaught due to the discrepancies between testing and production environment in cluster size, hardware SKU (stock keeping unit), OS/library versions, unpredictable workloads, complex component interactions, etc." / "They may also miss latent issues such as memory leaks that happen hours after a rollout." / "It achieves 92.4% precision and 100% recall (no high-impact service outages in Azure Compute were caused by bad rollouts) for dataplane rollouts." / "Gandalf filed 39 incidents and only 2 of them are false alarms. Meanwhile, Gandalf automatically approved all other region-level deployments and only missed 2 true issues."
- URL:https://www.usenix.org/system/files/nsdi20-paper-li.pdf
- 日期:2020-02(NSDI'20)
- 来源类型:同行评审(作者为微软员工,系统自评,厂商受益)
- 承重:是(漏网共性 + 「recall」口径警示);检出率数字归 canary 线,本线只用其口径
- 叙事:支持「生产期检测能接住坏发布」,但 recall 口径偏宽松;同时证明 TTD 在潜伏问题上以小时/天计

## C12 DORA 2023 把 MTTR 改为「失败部署恢复时间」,理由正是 MTTR 混入了非变更故障
- 论断:DORA 官方回顾:2023 年把 MTTR / time to restore service 改名并重定义为 failed deployment recovery time,原因是旧定义不区分「软件变更引发的故障」与「外部因素(如数据中心停电)引发的故障」。2024 年新增第五个指标 deployment rework rate;当前五指标分组中,失败部署恢复时间被归入「throughput」因子,change fail rate 与 rework rate 归入「instability」。注意:这一指标仍是「恢复」时间(覆盖检测+定位+缓解全程),不是检测时间。
- 原文:"In 2023, DORA made a significant adjustment to the stability metrics. The metric historically known as 'mean time to recover (MTTR)' or 'time to restore service' was renamed and redefined as failed deployment recovery time. The reasoning was specific: previous definitions did not distinguish between a failure initiated by a software change and a failure caused by external factors, such as a data center outage."
- URL:https://dora.dev/insights/dora-metrics-history/
- 日期:页面 last updated 2026-01-02
- 来源类型:官方一手(Google Cloud 运营的 DORA 项目)
- 承重:是(口径)
- 叙事:中性;为「MTTR 不能当检测速度证据」提供官方依据

## C13 DORA 2024 绩效分档:变更失败率 5%(elite)到 40%(low);失败部署恢复时间 <1 小时到 1 周–1 月
- 论断:Accelerate State of DevOps 2024 的聚类:Elite(占受访者 19%)变更失败率 5%、失败部署恢复 <1 小时;High(22%)20%、<1 天;Medium(35%)10%、<1 天;Low(25%)40%、1 周–1 月。口径:**问卷自报**(非系统测量),聚类用原四指标;High 档 CFR(20%)反而高于 Medium(10%),说明档位是多指标聚类结果而非 CFR 单调排序。定义:只有「落地到生产、终端用户可感知」的问题才算 change failure;在通往生产路上被拦下的变更算「部署流程成功检出错误」。→ 这意味着被 canary 拦下的坏发布是否计入 CFR,取决于 canary 是否已对用户可见,口径模糊。
- 原文:"Change fail rate: the percentage of deployments that cause failures in production, requiring hotfixes or rollbacks." / "Elite … 5% … Less than one hour … 19% (18-20%)" / "Low … 40% … Between one week and one month … 25% (23-26%)" / "We consider a deployment to be a change failure only if it causes an issue after landing in production, where it can be experienced by end users. In contrast, a change that is stopped on its way to production is a successful demonstration of the deployment process's ability to detect errors."
- URL:https://services.google.com/fh/files/misc/2024_final_dora_report.pdf
- 日期:2024-10
- 来源类型:分析机构/官方一手(Google Cloud 赞助的问卷研究;Google 作为云与 DevOps 工具厂商间接受益)
- 承重:是(变更失败基线)
- 叙事:中性;提供「多大比例的部署是坏发布」的唯一行业级(问卷)基线

## C14 DORA 2025:不再给 elite/high/medium/low 四档,改为原始分布 + 7 类团队原型;CFR 中位落在 8–16% 档
- 论断:State of AI-assisted Software Development 2025 不再沿用四档聚类基准,而给出问卷原始分布,并以七类团队原型(cluster)替代。变更失败率分布:0–2% 8.5%、2–4% 8.1%、4–8% 19.6%、8–16% 26%、16–32% 19.5%、32–64% 12.5%、>64% 5.9%——即约 38% 受访者自报 CFR ≥16%,中位数落在 8–16% 档。失败部署恢复时间:<1 小时 21.3%、<1 天 35.3%、1 天–1 周 28%、1 周–1 月 9.4%、1–6 月 4.9%、>6 月 1%。口径:问卷自报;问题措辞「generally take to restore service」,是恢复全程不是检测;CFR 题干把 fix forward/patch 也算作 remediation。
- 原文:"Approximately what percentage of changes to production or releases to users result in degraded service (for example, lead to service impairment or service outage) and subsequently require remediation (for example, require a hotfix, rollback, fix forward or patch), if at all?" / "0%-2% 8.5% … 4%-8% 19.6% … 8%-16% 26% … 16%-32% 19.5% … 32%-64% 12.5% … >64% 5.9%" / "How long does it generally take to restore service after a change to production or release to users results in degraded service … Less than one hour 21.3% … Less than one day 35.3% … Between one day and one week 28%"
- URL:https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf (落地页 https://dora.dev/research/2025/dora-report/)
- 日期:2025-09/10(报告版本 v.2025.2)
- 来源类型:分析机构/官方一手(Google Cloud 主办,GitHub、GitLab 等为研究伙伴——工具厂商受益于「AI+平台工程」叙事)
- 承重:是(最新的行业级 CFR 与恢复时间基线)
- 叙事:中性;但提醒「坏发布」并非罕见——超过三分之一团队自报 ≥16% 的变更需补救

## C15 DORA 2025:AI 采用提升吞吐,但仍增加交付不稳定性
- 论断:DORA 2025 的贝叶斯模型估计,AI 采用与软件交付吞吐正相关(相对 2024 是转变),但仍与「软件交付不稳定性」(CFR + rework rate)正相关;报告解释为团队为速度适配,但底层系统尚未进化到能安全管理 AI 加速的开发。口径:问卷横截面,89% credible interval,标准化效应量很小(图中量级约 ±0.1)。这与本研究「AI 在发布后检测能否接住坏发布」相关:上游 AI 编码可能抬高了坏发布输入率。
- 原文:"AI adoption now improves software delivery throughput, a key shift from last year. However, it still increases delivery instability. This suggests that while teams are adapting for speed, their underlying systems have not yet evolved to safely manage AI-accelerated development."
- URL:同 C14
- 日期:2025
- 来源类型:分析机构/官方一手(Google 同时是 AI 编码工具厂商)
- 承重:否(背景)
- 叙事:反对「AI 让发布更安全」的单向叙事;强调需要发布后兜底

## C16 Google《Incident Metrics in SRE》(Davidovič 2021):即使事故真的缩短 10%,MTTR 往往看不出来
- 论断:Google SRE Štěpán Davidovič 用三家公司公开事故数据做 Monte Carlo:假设某产品让每起事故时长缩短 10%,MTTR 差值仍有 38%(A)、40%(B)、20%(C)的概率为负;反过来,产品什么都不做时也有 19%/23%/10% 的概率看到 ≥30 分钟的 MTTR「改善」。结论:MTTR/MTTM 不适合做决策或趋势分析。同报告的事故时间线模型把「首次产品影响 → 检测(运维意识到)→ 缓解 → 恢复」分开,MTTR 定义为恢复时刻减首次影响时刻——即 MTTR 天然包含 TTD 与 RCA、缓解。→ 对本研究的含义:任何「AI 把 MTTR/TTD 降低 X%」的厂商数字,若基于前后对比的均值且样本小,统计上可能是噪声。
- 原文:"In this report, we use a simple Monte Carlo simulation process … to demonstrate that these statistics are poorly suited for decision making or trend analysis in the context of production incidents." / "Even though in the simulation the improvement always worked, 38% of the simulations had the MTTR difference fall below zero for Company A, 40% for Company B, and 20% for Company C." / "there's a 19% chance that there is a half-hour improvement (or better) of MTTR in Company A (and 23% for Company B, and 10% for Company C)…even though in this simulation, you did not change anything about the incidents." / "Detection: When the system's operator becomes aware of the ongoing problem"
- URL:https://sre.google/resources/practices-and-processes/incident-metrics-in-sre/ (PDF:https://sre.google/pdf/IncidentMeticsInSre.pdf)
- 日期:2021-03(O'Reilly report)
- 来源类型:官方一手(Google SRE,方法论报告)
- 承重:是(评估「AI 缩短检测时间」声明的统计基础)
- 叙事:反对用 MTTR 前后对比证明 AIOps 有效

## C17 VOID 2022 报告:事故时长正偏态、多数 <2 小时、时长与严重度无相关,建议弃用 MTTR
- 论断:VOID(Verica Open Incident Database,2022 年底第二份报告,据报道近 1 万起公开事故、近 600 家公司)认为事故时长数据正偏态、多数在两小时内解决,均值类指标不可靠;未发现事故时长与严重度相关;主张「本就不该用单一平均数代表复杂社会技术系统的可靠性」。口径:来自公开事故报告(状态页、博客等),时长多为报告中自述或推算;本条逐字引文经 InfoQ 转述(VOID 原 PDF 现需邮件订阅获取,未能直接下载核对)。
- 原文:"The additional data in the report reinforced the notion that incident duration data is positively skewed as most incidents resolve in under two hours." / (报告原文,经 InfoQ 引用)"We never should have used a single averaged number to try to measure or represent the reliability of complex sociotechnical systems." / "One of the newer findings in the report is that there is no correlation detected between incident duration and incident severity."
- URL:https://www.infoq.com/articles/incident-metrics-void/ (原报告页 https://www.thevoid.community/report)
- 日期:2022-12(报告);InfoQ 报道 2023
- 来源类型:媒体转述(底层为从业者研究机构报告;Verica 当时是混沌工程厂商)
- 承重:否(支持 C16 的定性结论)
- 叙事:反对 MTTR 作为改进证据

## C18 Allspaw(SREcon24):「事故没有客观的开始时间」,并反讽「变更是事故主因」
- 论断:John Allspaw 在 SREcon24 Americas 讲稿中列出「我们以为知道但其实不对」的条目:事故没有客观的开始/结束时间、严重度总是可协商的分类;并把 Wu et al. ICSE-SEIP 2023「变更是诱发事故的主要原因之一」改写为「变更也是解决事故的主要原因之一」「以及事故没有发生的主要原因之一」;质疑「检测→动员→诊断→解决→学习」线性序列是否代表多数真实事故。→ 对 TTD 的直接含义:TTD 起点(影响开始)本身是事后建构的,跨组织不可比。
- 原文:"There is no objective start time of an incident" / "There is no objective end time of an incident" / "Severity is always a negotiable classification" / (原引)"Change is one of the leading causes that induce incidents." → (改写)"Change is one of the leading causes of resolving incidents." / "Is this how all incidents play out? Is this how most incidents play out?"
- URL:https://www.usenix.org/system/files/srecon24americas_slides-allspaw.pdf
- 日期:2024-03(SREcon24 Americas)
- 来源类型:从业者(Adaptive Capacity Labs 创始人;前 Etsy CTO)
- 承重:是(TTD 口径的根本性质疑)
- 叙事:反对「变更=坏」的单向叙事;反对线性阶段模型被当作可精确测量

## C19 Richard Cook《How Complex Systems Fail》:根因归因从根本上是错的;变更引入新的失效形式
- 论断:Cook(1998/2000)的条目被 SRE 社区广泛引用:复杂系统总携带潜伏缺陷;事后把事故归于单一「根因」从根本上是错的,事故需要多个各自不充分的因素共同作用;变更(尤其新技术)为消除高频低后果故障,常引入低频高后果的新失效路径。→ 含义:「X% 事故由变更引起」是把多因素事故压成单一触发标签的统计,Google 附录 C 明确区分了 trigger 与 root cause。
- 原文:"Post-accident attribution to a 'root cause' is fundamentally wrong." / "Because overt failure requires multiple faults, there is no isolated 'cause' of an accident." / "Change introduces new forms of failure." / "When new technologies are used to eliminate well understood system failures or to gain high precision performance they often introduce new pathways to large scale, catastrophic failures."
- URL:https://how.complexsystems.fail/
- 日期:1998(原文,Cognitive Technologies Laboratory, University of Chicago);在线版持续
- 来源类型:从业者/学术经典(非同行评审短文)
- 承重:否(框架)
- 叙事:双向——支持「变更带来风险」,但反对把事故单一归因于某次变更;也提示 AI 检测作为「新技术」本身可能引入新失效

## C20 Microsoft LLM 推理服务(2025-04 至 06,156 起 Sev2/2.5):约 74% 在客户报告前被自动检出;LLM 辅助 DRI 工具改善分诊但多数情况仍需人决策
- 论断:Ranganathan et al.(Microsoft,arXiv 2511.07424,2025-10)分析 2025 年 4–6 月 156 起高严重度(Sev 2 / 2.5)LLM 推理事故:115 起(≈74%)为「auto-detected」(定义:health probe / DRI 流水线在客户报告之前触发告警),其余非自动检出;≈60% 为推理引擎故障,≈16% 模型配置故障(header 配置错误、无效输出),≈4% 运维类故障且常与 rollout 窗口重合;低流量 endpoint、阈值过宽导致检测延迟。LLM 辅助工具(ICM Analyzer、DRI Copilot)「改善分诊、减少人工劳动,但多数情况下未消除人工决策」。口径:单一服务族、3 个月窗口、排除 Sev3+;非同行评审。
- 原文:"We define auto-detected as alerts fired by health probes/DRI pipelines before customer reporting. As observed in Figure 5, across the 156 incidents, 115 were auto-detected (≈74%), and the rest were still not auto-detected." / "LLM assisted DRI tooling (ICM Analyzer, DRI Copilot) and enrichment pipelines improved triage and reduced manual toil, but did not eliminate the need for human decisions in most cases." / "Gaps in observability (low-traffic endpoints, permissive thresholds) and traffic routing (imbalances) delayed detection and prolonged impact."
- URL:https://arxiv.org/pdf/2511.07424
- 日期:2025-10-17(v1)
- 来源类型:预印本(作者均为微软员工,自家数据)
- 承重:是(2025 年最新「谁发现」数字;与 C04 的 55%、C07 的 61.7% 构成区间)
- 叙事:中性——监控检出率较 2022 Teams 研究高,但仍约四分之一高严重度事故非自动发现;AI 工具作用在分诊(定位段)而非检测

## C21 AWS Builders' Library:用「烘焙时间」显式承认部分坏发布影响不会立刻显现;one-box 流量太小触发不了服务级告警
- 论断:Amazon 官方说明其流水线在每个生产阶段后设 bake time 持续监控高严重度聚合告警以捕捉「slow burning impact」;典型流水线 one-box 后至少等 1 小时、第一个区域 wave 后至少 12 小时、后续 wave 各 2–4 小时,全区域部署约 4–5 个工作日;并要求等到足够数据点(如 ≥100 次 Create API 请求)。另承认 one-box 只服务小比例流量,其问题可能触发不了服务级高严重度回滚告警,因此另设 one-box 局部指标。→ 这等于用设计参数给出了「坏发布影响可能多晚才显现」的厂商经验上界(小时到天级),也是「canary 漏网共性:低流量/慢燃型」的一手描述。无检出率数字。
- 原文:"Sometimes a negative impact caused by a deployment is not readily apparent." / "A typical pipeline waits at least one hour after each one-box stage, at least 12 hours after the first regional wave, and at least two to four hours after each of the rest of the regional waves" / "A one-box stage serves a small percentage of overall traffic, so issues introduced by a one-box deployment might not trigger the service's high-severity rollback alarm." / "During off-hours, it takes longer to engage the oncall engineer than during the day"
- URL:https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/
- 日期:2020(Clare Liguori;2026-10-30 抓取仍在线)
- 来源类型:官方一手(厂商工程博客,宣传自身实践)
- 承重:否(质性 + 设计参数)
- 叙事:支持「自动 canary + 自动回滚是主流防线」,同时承认慢燃/低流量问题需要长时间窗

## C22 Azure CTO Russinovich:除小而常见的硬件故障外,Azure 可靠性问题的首要原因是「变更」
- 论断:Azure 官方博客明确把「变更」列为除常见小硬件故障外的首要可靠性问题来源,但**未给比例**;并描述安全部署框架:渐进发布 + 持续健康信号 + 强制 bake time,「只要没有负面信号就继续部署」,用于发现「测试中未暴露」的影响;提到用机器学习做故障关联与异常检测(即 Gandalf)。
- 原文:"What is the primary cause of service reliability issues that we see in Azure, other than small but common hardware failures? Change." / "we roll out the change in a gradual manner and measure health signals continuously, so that we can detect in relative isolation if there is any unexpected impact associated with the change that did not surface during testing."
- URL:https://azure.microsoft.com/en-us/blog/advancing-safe-deployment-practices/
- 日期:2020-02(Mark Russinovich)
- 来源类型:官方一手(厂商博客,无数据)
- 承重:否(定性;微软版「70%」只有定性)
- 叙事:支持「变更是主因」;注意它显式把高频硬件故障排除在外

## C23 Google Cloud 2025-06-12 全球事故:代码经逐区域发布但故障路径未被触发;两周后一条全球秒级复制的策略数据变更引爆;检测 2 分钟、定位 10 分钟、主体缓解约 2 小时、全部结束 3 小时
- 论断:官方事故报告:2025-05-29 Service Control 新增配额检查功能,无错误处理、无 feature flag;该二进制「经过逐区域发布,但故障代码路径在发布期间从未被执行」,因为需要一条策略变更才会触发。06-12 10:45 PDT 一条含空字段的策略写入 Spanner,「数秒内全球复制」,触发空指针导致全球 crash loop。时间线清楚分三段:2 分钟内 SRE 开始分诊(检测)、10 分钟内定位根因(RCA)、约 25 分钟 red-button 就绪、40 分钟内 red-button 推完、除 us-central1 外 12:48 缓解,us-central1 因 herd effect 恢复更久,事件 13:49 结束(时长 3 小时)。这是「staging/canary 漏掉什么」的典型:**休眠代码路径 + 绕过分阶段发布的全局数据/配置推送**。
- 原文:"This code change and binary release went through our region by region rollout, but the code path that failed was never exercised during this rollout due to needing a policy change that would trigger the code." / "Given the global nature of quota management, this metadata was replicated globally within seconds." / "Within 2 minutes, our Site Reliability Engineering team was triaging the incident. Within 10 minutes, the root cause was identified and the red-button (to disable the serving path) was being put in place." / "Incident Start: 12 June, 2025 10:49 All regions except us-central1 mitigated: 12 June, 2025 12:48 Incident End: 12 June, 2025 13:49 Duration: 3 hours"
- URL:https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW
- 日期:2025-06(事故报告)
- 来源类型:官方一手(事故复盘)
- 承重:是(检测快 ≠ 恢复快的反例;canary 漏网共性)
- 叙事:反对「快速检测即可止损」——检测 2 分钟,但全球同步推送使影响在检测前已全面扩散;支持「数据/配置推送是 canary 盲区」

## C24 Cloudflare 2025-11-18:数据库权限变更 → 机器生成的特征文件翻倍 → 全网传播;3 分钟自动检出,但先误判为 DDoS,约 2 小时后才锁定配置文件
- 论断:官方复盘时间线:11:05 数据库访问控制变更部署;11:28 影响开始;11:31 首个自动化测试检出问题,11:32 人工调查,11:35 建事故会;11:32–13:05 团队调查 Workers KV 等表象并尝试流量调度;团队一度误认为是超大规模 DDoS;13:37 才确信 Bot Management 配置文件是触发源;14:24 停止该文件生成与传播;14:30 主要影响解除;17:06 全部恢复。文件每 5 分钟由逐步升级中的 ClickHouse 集群生成,好坏文件交替,系统反复「恢复-失败」,加剧误判。→ 三段分离的典型:检测(TTD)≈3 分钟;定位约 2 小时以上;缓解在定位后数分钟。坏变更是**内部生成的配置/数据文件**,未走代码发布的分阶段流程;整改项包括「把 Cloudflare 自己生成的配置文件当作用户输入一样加固」与更多全局 kill switch。
- 原文:"11:05 Normal. Database access control change deployed. 11:28 Impact starts. … The first automated test detected the issue at 11:31 and manual investigation started at 11:32. The incident call was created at 11:35." / "After we initially wrongly suspected the symptoms we were seeing were caused by a hyper-scale DDoS attack, we correctly identified the core issue" / "This fluctuation made it unclear what was happening as the entire system would recover and then fail again as sometimes good, sometimes bad configuration files were distributed to our network." / "Hardening ingestion of Cloudflare-generated configuration files in the same way we would for user-generated input"
- URL:https://blog.cloudflare.com/18-november-2025-outage/
- 日期:2025-11-18
- 来源类型:官方一手(事故复盘)
- 承重:是(「检测不是瓶颈,定位才是」的一手证据)
- 叙事:反对「更快的检测=更快止损」;支持「配置/数据推送是 canary 盲区」;对 LLM-RCA 叙事是双刃——正是定位段耗时最长

## C25 CrowdStrike 2024-07-19 Channel File 291:内容(配置类)更新通过了 Content Validator 但未分阶段发布;整改即补 canary + ring + bake-in
- 论断:官方 RCA:新 Template Instance 首次对第 21 个输入字段使用非通配匹配,Content Validator 基于「21 个输入」的错误预期放行,而解释器只提供 20 个值 → 越界读 → 系统崩溃;测试中该字段一直是通配符,未覆盖非通配情形。RCA 明确发现「每个 Template Instance 应分阶段发布」,整改为 canary 测试后逐环推广并设 bake-in 遥测。→ 漏网共性:**验证器与运行时的契约不一致 + 测试只覆盖过去用过的输入形态 + 快速内容通道绕过分阶段发布**。
- 原文:"The Content Validator evaluated the new Template Instances, but based its assessment on the expectation that the IPC Template Type would be provided with 21 inputs." / "the lack of a specific test for non-wildcard matching criteria in the 21st field" / "Findings: Each Template Instance should be deployed in a staged rollout." / "New Template Instances that have passed canary testing are to be successively promoted to wider deployment rings or rolled back if problems are detected."
- URL:https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf
- 日期:2024-08-06
- 来源类型:官方一手(事故 RCA)
- 承重:是(配置/内容推送绕过 canary 的标志性案例)
- 叙事:支持「离线验证有结构盲区」;支持「问题不在于 AI 检测不够快,而在于没有分阶段暴露面可供检测」

## C26 Uptime Institute 2025(反方/口径对照):在「数据中心运营者」口径下,电力仍是最主要原因;IT 与网络问题占 2024 年有影响 outage 的 23%,其上升归因于变更管理与误配置
- 论断:Uptime Institute 2025 年度 outage 分析(新闻稿):IT 与网络问题在 2024 年上升到有影响 outage 的 23%,「很可能」源于复杂度上升带来的变更管理与误配置问题;人为错误相关 outage 中 85% 源于不按程序操作或程序本身缺陷;九年公开报道 outage 中约三分之二归于第三方 IT/数据中心服务商。另据多家媒体转述,同报告调查中 54% 受访者称最近一次重大 outage 原因是电力(未在新闻稿中逐字核到,标为媒体转述)。口径:问卷 + 公开报道,面向数据中心/基础设施运营者,不是软件服务事故;「change management」定义未公开(付费报告)。
- 原文:"Outages from IT and networking issues increased in 2024, totaling 23% of impactful outages." / "This rise is likely caused by increased IT and network complexity, leading to issues with change management and misconfigurations." / "Of these incidents, 85% stem from staff failing to follow procedures or from flaws in the processes and procedures themselves."
- URL:https://uptimeinstitute.com/about-ui/press-releases/uptime-announces-annual-outage-analysis-report-2025
- 日期:2025-05
- 来源类型:分析机构(付费报告的新闻稿;Uptime 卖咨询与认证)
- 承重:否(反方口径对照)
- 叙事:反方——「变更是主因」依赖于你统计的是哪一层(软件服务 vs 数据中心物理层);在物理层,电力是主因

## C27 Liu et al. HotOS'19(Azure):软件 bug 约占高严重度事故近 40%,硬件故障 <5%;bug 类中数据格式不一致 21%(多由更新引起)、故障检测/处理缺陷 31%
- 论断:研究 Azure 多服务「数百起」高严重度事故,软件 bug 是最常见原因(close to 40%);对其中 112 起 bug 事故深挖:组件故障检测与处理错误 31%、不同组件/版本间数据格式假设不一致 21%(其中约 60% 涉及消息接口、40% 涉及文件;「多数情况下由未充分考虑各方数据格式假设的软件更新触发」)、时序 bug 13%、常量值错误 7%;硬件故障导致的事故比例 <5%。作者坦言:微软已用工具在上线前消除大量 bug 类型,所以「配置项写错」类事故样本很少——即**生产事故分布是被离线验证过滤后的残差分布**。
- 原文:"identified software bugs as the most common cause of cloud incidents (close to 40%). We then did an in-depth study of all the 112 high-severity production incidents that are caused by software bugs." / "(1) incorrect or missing detection and handling of component failures (31 %) and (2) inconsistent data-format assumptions held by different software components or versions (21 %)." / "In most cases, these bugs are triggered by software updates that fail to fully consider the data-format assumptions held by all stakeholders." / "we observed the percentage of incidents caused by hardware failures to be significantly smaller (less than 5%) than those in non-cloud systems"
- URL:https://people.cs.uchicago.edu/~shanlu/paper/hotos19_azure.pdf (MSR 页 https://www.microsoft.com/en-us/research/?p=610323)
- 日期:2019-05(HotOS'19)
- 来源类型:同行评审(workshop;作者含微软研究员)
- 承重:是(「漏网的是什么」:跨版本/跨组件契约)
- 叙事:支持「离线测试漏掉的是跨组件契约与故障处理路径」;硬件占比低,支持软件/变更为主

## C28 某大型商业银行(Zhao et al. FSE'21,SCWarn):约 50.4% 事故由坏变更引起;作者自报的检测方法把 MTTD 降低 20.4%–60.7%
- 论断:清华等与一家大型商业银行合作的实证研究称约 50.4% 的事故由坏变更引起(主要为代码缺陷、配置错误、资源争用、软件版本);当时的坏变更检测实践难以处理变更涉及的异构多源数据。作者提出的多模态异常检测方法 SCWarn 在两个数据集上平均 F1 0.95,并把 MTTD 降低 20.4%–60.7%。口径:50.4% 的分母为该银行研究窗口内的事故(摘要未给总数与窗口);MTTD 降幅是在**已知坏变更数据集**上与基线方法比较,不是线上前后对比,且属作者自评。
- 原文:"Our quantitative analyses indicate that about 50.4% of incidents are caused by bad changes, mainly because of code defect, configuration error, resource contention, and software version." / "achieving 0.95 F1-score on average and reducing MTTD (mean time to detect) by 20.4%∼60.7%."
- URL:https://2021.esec-fse.org/details/fse-2021-papers/97/Identifying-Bad-Software-Changes-via-Multimodal-Anomaly-Detection-for-Online-Service- (DOI 10.1145/3468264.3468543)
- 日期:2021-08(ESEC/FSE'21)
- 来源类型:同行评审(学术方 + 企业数据)
- 承重:是(非互联网大厂的变更占比锚点;也是「AI 缩短检测时间」少有的 TTD 口径数字)
- 叙事:支持「变更约占一半」;检测改进数字属于「已知回归集合」口径,需打折

## C29 「70%」的引用链:2026 年同行评审论文仍直接引用 SRE 书该句作为事实依据
- 论断:ING 银行与 TU Delft 的 ICSE-SEIP 2026 论文在引言中写「据 Google 报告,其线上系统约 70% outage 由此类变更引起」,引用 Beyer et al. 2016(SRE 书)——即 C01 那句无口径的经验断言,在十年后仍作为学术论文的事实前提流通。同一论文自身数据显示:引发事故的变更在全部变更中「很少」,导致规则与模型精度都很低、存在告警疲劳风险(基线规则召回 56%)。
- 原文:"A significant portion of incidents stem from IT changes, which involve additions, modifications, or deletions to existing IT applications [19]. As reported by Google [7], roughly 70% of outages in its live systems are due to such changes." / "Due to the low amount of incident-inducing changes present in the data, all models inevitably exhibit low precision. This can create operational challenges, most notably alert fatigue"
- URL:https://arxiv.org/pdf/2604.13462
- 日期:2026-04-15(ICSE-SEIP '26)
- 来源类型:同行评审(企业 + 高校)
- 承重:是(70% 的传播链证据;也是「事前风险预测误报代价」的口径)
- 叙事:揭示主流叙事的证据基础薄弱;同时说明「坏变更是稀有事件」→ 任何检测器都面临基率问题导致的低精度

---

## 小结:本线的基础事实区间(截至 2026 年 10 月)

| 问题 | 数据点 | 来源 |
|---|---|---|
| 变更(代码+配置推送)触发占比 | 68%(binary 37% + config 31%,2010–2017,Google postmortem 抽样) | C02 |
| 「变更」引起占比(其他口径) | 银行 ~50.4%(C28);FB 配置相关 16%(C09);Azure bug 近 40%(C27);Teams 代码+配置 bug 40%(C06);公开 outage 升级+配置 ~26%(C08) | |
| 自动监控先发现的比例 | Teams 高严重度 ~55%(2022);GenAI 61.7% / 其他服务 86.3%(2025,含低严重度);LLM 推理 Sev2 ~74%(2025) | C04/C07/C20 |
| 客户/外部报告比例 | Teams 29%;GenAI 人工报告 38.3% | C04/C07 |
| 行业变更失败率 | DORA 2025 中位落在 8–16% 档,~38% 团队 ≥16%(问卷自报) | C14 |
| 典型检测 vs 定位时间 | GCP 2025-06:检测 2 分钟 / 定位 10 分钟 / 主体缓解 ~2 小时;Cloudflare 2025-11:检测 3 分钟 / 定位 ~2 小时+ | C23/C24 |
| 慢燃/潜伏问题时间尺度 | 数小时至 24–72 小时(Gandalf);AWS bake 1h/12h/2–4h,全球 4–5 工作日 | C11/C21 |

## 交叉口径问题(供合稿时核对)

1. **「70%」没有原始口径**。SRE 书第 1 章原句无分子分母;唯一可追溯数据是 Workbook 附录 C 的 68%(binary 37% + config 31%),它是「top 8 triggers」在「数千份 postmortem 样本」中的占比,且是 trigger 不是 root cause。引用 70% 时应改引附录 C 并注明口径。C29 显示 2026 年的同行评审论文仍直接引 70%。
2. **Trigger vs root cause 不可混比**。Google(C02)是触发分类;Ghosh(C06)、Liu(C27)、Gunawi(C08)、Tang(C09)是根因分类。代码 bug 作为根因的事故大多也是经代码推送触发的,所以「变更占比」在 trigger 口径下天然高于 root-cause 口径。Ghosh 的「60% 非代码」中,依赖故障里 28% 是伙伴团队的变更、部署错误 55% 是证书——按 trigger 口径很多仍是「变更」。
3. **严重度过滤决定「谁发现」比例**。Teams(C04)只看 Sev0–2 且过滤掉 35% 信息不全的事故 → 监控 55%;GenAI 研究(C07)的检测类型统计用的是全量「数十万」事故(含低严重度)→ 监控 61.7%/86.3%;LLM 推理(C20)只看 Sev2/2.5 → 74%。三者不可直接排趋势。
4. **「自动检出」定义不一**。C20 定义为「客户报告前由 probe/DRI 流水线告警」;C04 为「由 automated watchdog 检出」;都没有说明告警是否先于影响开始多久——即「自动检出」不等于「影响扩散前检出」。
5. **TTD 起点无客观定义**(C18 Allspaw;C16 用「first product impact」)。Ghosh 只给归一化 TTD。厂商的「TTD 缩短 X%」通常以告警时间减「影响开始」,而影响开始由事后复盘人工认定。
6. **MTTR/恢复时间混合三段**。DORA 的 failed deployment recovery time(C12–C14)、VOID 的 duration(C17)都覆盖检测+定位+缓解;C23/C24 的单案时间线显示检测只占几分钟,定位与缓解占数小时——用这些指标论证「AI 加速检测」是错配。
7. **小样本前后对比的统计噪声**(C16):真实 10% 改善在 MTTR 上有 20–40% 概率表现为变差;无改善也有 10–23% 概率显示 ≥30 分钟改善。厂商「MTTR/MTTD 降 X%」若无对照组与置信区间,应视为不可证伪。
8. **DORA 是问卷自报**,且 2024 年 High 档 CFR(20%)高于 Medium 档(10%);2025 年取消四档改为分布 + 七原型——跨年「elite 比例」不可比。DORA 定义中被拦在生产前的变更不算失败,canary 已对部分用户可见时是否计入,定义未说清。
9. **「误报率」口径不同**。C07 的 11.0%/3.8% 是「被标为 False Alarm 的事故占监控检出事故的比例」(事故级);Gandalf(C11)的 precision 92.4%/94.9% 是「拦截的发布中真坏的比例」(发布级);C29 是事前风险预测的模型精度。三者均不是告警级误报率。
10. **Gandalf「100% recall」**的分母是「造成 Sev0–2 高影响事故的坏发布」,不是全部坏发布;且为系统作者自评。
11. **公开 outage 样本偏差**:Gunawi(C08)、VOID(C17)、Uptime 公开报道部分(C26)只覆盖被公开报道的事故,偏向大而显眼者,59% 根因未知(C08)。
12. **层级口径**:Uptime(C26)面向数据中心物理层,电力为主因;Google/微软研究面向软件服务层,硬件 2%(C02)/ <5%(C27)。「变更是主因」只在软件服务层成立。
13. **未能核实的数字**(勿引用):第三方博客称「Google 70% / Baidu 54%」与某 IEEE 研究 231 起变更事故、蚂蚁集团 ICSE-SEIP'23 研究 161 起变更事故的具体发现——蚂蚁论文全文在 IEEE 付费墙后,本线未能读到原文。VOID 2022 原 PDF 需订阅,C17 引文经 InfoQ 转述。Uptime「54% 电力」来自媒体转述。

---

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

---

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

---

# 调研线 RCA:LLM 根因分析与 agentic SRE —— 宣称 vs 独立测量

截至 2026 年 10 月(调研日 2026-10-30)。来源分级:同行评审 / 官方一手 / 厂商自报(厂商口径)/ 从业者博客 / 媒体转述 / 分析机构。
"承重" = 若此条错,主文叙事会变。"叙事":A = AI 显著缩短发布后定位/检测;B = 宣称被口径放大 / 独立测量远低;C = 中性/口径说明。

---

## L1. Meta AI 辅助根因:42% 是 top-5、回放、限 web monorepo、限"代码变更"候选
- 论断:Meta 的 42% 是**回放评估(backtesting)**,分母为与 web monorepo 相关的**历史 investigation**,只用"调查创建时可用的信息",判定为**根因落在 top-5 候选代码变更中**;不是 top-1,不是全部事件,不是线上实测。模型为微调的 Llama 2 7B,先用启发式检索把候选从数千缩到数百。
- 原文:"Based on exhaustive backtesting, with historical investigations and the information available at their start, 42% of these investigations had the root cause in the top five suggested code changes." / "Our testing has shown this new system achieves 42% accuracy in identifying root causes for investigations at their creation time related to our web monorepo." / "The biggest lever to achieving 42% accuracy was fine-tuning a Llama 2 (7B) model using historical investigations for which we knew the underlying root cause."
- URL:https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/
- 日期:2024-06-24
- 来源类型:官方一手(工程博客,非同行评审)
- 承重:是
- 叙事:C/B(常被转述为"42% 准确率",省略 top-5 与回放)

## L2. Meta 自认风险:可能误导工程师,用置信度过滤"牺牲覆盖换精度"
- 论断:Meta 承认 AI 根因可能给出错误根因误导工程师,并对低置信答案不展示——意味着 42% 之外还有一个未公开的"覆盖率"(展示了多少 investigation)维度。
- 原文:"it can reduce effort and time needed to root cause an investigation significantly, but it can potentially suggest wrong root causes and mislead engineers." / "We also rely on confidence measurement methodologies to detect low confidence answers and avoid recommending them to the users – sacrificing reach in favor of precision."
- URL:同 L1
- 日期:2024-06-24
- 来源类型:官方一手
- 承重:中
- 叙事:B

## L3. Microsoft Ahmed et al. (ICSE 2023):4 万+ 事件上用词汇/语义相似度评估,人评正确性 2.28–3.16 / 5
- 论断:该研究在 Microsoft 40,000+ 事件上微调 GPT-3.x 生成根因与缓解文本,自动指标是 BLEU/ROUGE 等文本相似度,不是"是否找对根因";对 50 个近期事件的事故 owner 人评中,OpenAI 模型正确性评分 2.28–3.16(1–5 分),>70% owner 打 3 分及以上。这是"生成一段像样的根因描述",不是定位准确率。
- 原文:"We do a rigorous study at Microsoft, on more than 40,000 incidents and compare several large language models in zero-shot, fine-tuned and multi-task setting using semantic and lexical metrics." / "Though the correctness score of the OpenAI models ranges from 2.28 to 3.16, several OCEs pointed out that the models recommend beneficial root causes and mitigation plans." / "More than 70% of incident owners gave three or above for the recommendations of the models."
- URL:https://arxiv.org/abs/2301.03797
- 日期:2023-01(ICSE 2023)
- 来源类型:同行评审(作者为 Microsoft 员工/实习生)
- 承重:中
- 叙事:C

## L4. RCACopilot (EuroSys 2024):"RCA accuracy up to 0.766" 实为单服务、653 事件、根因**类别**分类的 Micro-F1
- 论断:常被引的 0.766 是 Microsoft Transport(邮件)服务一年 653 个事件上预测"根因类别"的 Micro-F1(Macro-F1 仅 0.533);且依赖每个团队手工构建的诊断 handler。24.96% 的事件属于新根因类别。直接用 GPT-4 prompt 的 Micro-F1 仅 0.026。
- 原文:"Our evaluation demonstrates that RCACopilot achieves RCA accuracy up to 0.766." / "RCACopilot achieves 0.766 and 0.533 for Micro-F1 and Macro-F1 separately when predicting the root cause category of cloud incidents" / "We collect a one-year dataset of 653 incidents from Microsoft's Transport service" / "incidents with a new root cause category account for 24.96% (163 among 653) of all incidents."
- URL:https://arxiv.org/abs/2305.15778
- 日期:2023-05 预印 / EuroSys 2024
- 来源类型:同行评审(Microsoft 自家系统)
- 承重:是
- 叙事:B(摘要用 "accuracy" 一词,正文是类别 F1)

## L5. RCACopilot 部署的是"诊断信息收集"模块(4 年、30+ 团队),根因预测只在单服务推出
- 论断:长期大规模部署的是自动化收集诊断信息(非 LLM 根因);LLM 根因预测模块仅 "rolled out in the Transport service"。
- 原文:"We have successfully deployed RCACopilot's diagnostic information collection module across over 30 teams within Microsoft, where it has been in active use for over four years." / "The root cause prediction module has also been rolled out in the Transport service."
- URL:https://arxiv.org/abs/2305.15778
- 日期:2024(EuroSys 2024)
- 来源类型:同行评审
- 承重:中
- 叙事:B

## L6. AIOpsLab (MLSys 2025, Microsoft):受控故障注入,RCA 任务最佳 45.45%,缓解 54.55%;检测任务 LLM 69–100%
- 论断:在 Microsoft 自建的 Kubernetes 微服务故障注入基准(48 个问题)上,GPT-4 等 agent 的 RCA 准确率 9.09%–45.45%,缓解 0%–54.55%;检测(二元判断有无故障)69.23%–100%,定位 top-1 30.77%–61.54%。传统非 LLM 方法(MKSMC 检测 15.38%,PDiagnose 定位 15.38%)更差。样本量小(每类十余题),非真实生产事件;"检测"为给定已注入故障环境下的二元问答,无误报率/真实流量。
- 原文:"FLASH achieves the highest accuracy among all agents. Although GPT-3.5-TURBO completes the tasks the fastest, it has the lowest accuracy at 15.25%." / "The detection task, being a binary choice question, should be the simplest task ... However, as shown in Table 4(a), only FLASH answers all the detection problems correctly." / "The RCA and mitigation tasks prove to be the most challenging for the agents." / Table 4(c): "GPT-4-W-SHELL 40.90% ... REACT 45.45% ... FLASH 36.36%"
- URL:https://arxiv.org/abs/2501.06706
- 日期:2025-01(MLSys 2025)
- 来源类型:同行评审(Microsoft 自建基准,自家 agent FLASH 参评)
- 承重:是(唯一同时测检测/定位/RCA/缓解四段的基准)
- 叙事:B/C

## L7. OpenRCA (ICLR 2025):335 个真实系统故障,最佳 Claude 3.5 + RCA-agent 仅 11.34%
- 论断:OpenRCA 335 个故障(来自三套企业系统,68GB 遥测),要求根因要素(时间、组件、原因)全部正确才计分;最佳 Claude 3.5 Sonnet + RCA-agent 11.34% 全对,17.31% 部分对;纯 prompt 最佳 Gemini 1.5 Pro 7.16%。无人类 SRE 基线。
- 原文:"Even with the specially designed RCA-agent, the best-performing model, Claude 3.5, solved only 11.34% failure cases." / "OpenRCA includes 335 failures from three enterprise software systems, along with over 68 GB of telemetry data (logs, metrics, and traces)." / "current models can only handle the simplest cases."
- URL:https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf
- 日期:2025(ICLR 2025)
- 来源类型:同行评审(Microsoft + CUHK)
- 承重:是
- 叙事:B

## L8. Anthropic 在 Opus 4.6 发布页把 OpenRCA 当卖点;聚合站转录 34.9%(待核)
- 论断:到 2026 年,模型厂商开始在发布页报告 OpenRCA,口径为"全部根因要素匹配才得 1 分"、"在基准作者 harness 上跑、已提交官方验证"。第三方聚合站 llm-stats 记录 Opus 4.6 为 0.349,标注 "Self-reported",未验证。即从 11.34%(2024 末)到 ~35%(2026-02)提升约 3 倍,但仍是三分之一。
- 原文(Anthropic):"Opus 4.6 excels at diagnosing complex software failures." / "For each failure case in OpenRCA, Claude receives 1 point if all generated root-cause elements match the ground-truth ones, and 0 points if any mismatch is identified. ... The benchmark was run on the benchmark author's harness, graded using their official methodology, and has been submitted for official verification."(llm-stats:"0.349",验证状态 "Self-reported1" / "StatusUnverified")
- URL:https://www.anthropic.com/news/claude-opus-4-6 ;https://llm-stats.com/benchmarks/openrca
- 日期:2026-02(发布页);llm-stats 访问于 2026-10-30
- 来源类型:厂商自报(数字在图表中,本调研未能从页面文本直接读到 34.9,经聚合站转录)
- 承重:中
- 叙事:A(进步)/ 需验证

## L9. OpenRCA 2.0(2026-06):11 个前沿模型精确根因集合平均仅 20.7%;"定位到服务"76.0%,但有因果链支撑的只 61.5%
- 论断:OpenRCA 2.0(500 例,故障注入 + 逐步因果标注)显示,"至少找对一个根因服务"(宽松)与"精确根因集合"(严格)差距巨大(76.0% vs 20.7%),且相当部分"找对"没有被验证过的传播路径支撑——"未落地的诊断(ungrounded diagnosis)"。说明宽松口径会大幅高估可信度。
- 原文:"Across 11 frontier LLMs, recovering the exact root-cause set succeeds in only 20.7% of cases on average." / "agents identify at least one correct root-cause service in 76.0% of cases, but ground that service in a verified causal propagation path to the observed symptom in only 61.5%. Outcome-only evaluation hides this failure mode"
- URL:https://arxiv.org/abs/2606.27154
- 日期:2026-06-25
- 来源类型:预印本(未同行评审)
- 承重:是(口径敏感性的最好例证)
- 叙事:B

## L10. 对 OpenRCA 的 1,675 次 agent 运行失败分析:幻觉式数据解读跨模型普遍存在
- 论断:2026 年一项过程级分析在 OpenRCA 上跑 5 个模型共 1,675 次,发现最常见失败是"幻觉式数据解读"和"探索不完整",且不随模型能力档位消失;仅靠 prompt 工程无法消除。
- 原文:"the most prevalent pitfalls, notably hallucinated data interpretation and incomplete exploration, persist across all models regardless of capability tier, indicating that these failures originate from the shared agent architecture rather than from individual model limitations." / "prompt engineering alone cannot resolve the dominant pitfalls"
- URL:https://arxiv.org/abs/2602.09937
- 日期:2026-02-10
- 来源类型:预印本
- 承重:中
- 叙事:B

## L11. OpenRCA 上的规则挖掘:Full Score 14.10 → 35.90(留出 cloudbed),结论仅限 OpenRCA
- 论断:2026-07 预印本显示,在 OpenRCA 某留出子系统上,从审计报告挖出的规则把 Full Score 从 14.10 提到 35.90(人工规则 24.36),但作者明言挖掘依赖标签、结果特定于 OpenRCA——说明基准分数对"程序/领域知识注入"高度敏感,也提示过拟合基准的风险。
- 原文:"Rules mined from the audit reports of one Market cloudbed raise Full Score on a held-out cloudbed from 14.10 to 35.90, surviving correction for multiple testing, against 24.36 for manual rules" / "Mining is label-supervised, and all results are specific to OpenRCA."
- URL:https://arxiv.org/abs/2607.13548
- 日期:2026-07-15
- 来源类型:预印本
- 承重:否
- 叙事:C

## L12. 基准作者自身的反方:Traversal 称 OpenRCA "不是根因分析"
- 论断:AI SRE 厂商 Traversal 批评 OpenRCA 只考"有界静态遥测上的模式匹配",部分故障根本无法从遥测中恢复、因果归属本身有歧义——即低分不一定代表生产能力,但也意味着高分不代表生产能力。(注意:批评者是厂商,受益于"基准不代表我们"的叙事;页面无日期)
- 原文:"OpenRCA evaluates pattern matching over bounded, static telemetry artifacts." / "The fault is not recoverable from the telemetry." / "selecting a labeled answer is not the same as performing root cause analysis."
- URL:https://www.traversal.com/blog/openrca-isnt-root-cause-analysis-why-that-matters
- 日期:未标注(约 2026)
- 来源类型:厂商(从业者博客)
- 承重:否
- 叙事:C(基准效度之争,双刃)

## L13. ITBench(IBM,ICML 2025):真实环境 SRE 场景,GPT-4o 诊断 pass@1 仅 13.81%,去掉 trace 降至 9.52%
- 论断:IBM ITBench 在 42 个 SRE 场景(Kubernetes 故障注入)、每场景每模型 10 次运行上,最佳 GPT-4o 诊断 pass@1 13.81%,缓解 11.43%;去掉 trace 后诊断 9.52%、缓解 2.86%——可观测性数据的完备度直接决定 AI 定位能力。
- 原文:"agents powered by state-of-the-art models resolve only 13.8% of SRE scenarios, 25.2% of CISO scenarios, and 0% of FinOps scenarios." / "GPT-4o consistently outperforms the other models, achieving the highest pass@1 scores for diagnosis (13.81%) and mitigation (11.43%)" / "GPT-4o's pass@1 in diagnosis falls from 13.81% with traces to 9.52% without them, and mitigation plummets to 2.86%."
- URL:https://arxiv.org/abs/2502.05352
- 日期:2025-02(ICML 2025 / PMLR 267)
- 来源类型:同行评审(IBM 自建基准)
- 承重:是
- 叙事:B

## L14. ITBench-AA(Artificial Analysis × IBM,2026-05):前沿模型根因识别仍 < 50%,最佳 47%
- 论断:2026-05 的 SRE 排行榜(59 个任务,含 19 个留出任务),评分为"全召回下的精度"(漏掉任一真根因即 0 分);Claude Opus 4.7 47%、GPT-5.5 46%、Qwen3.7 Max 42%;无人类基线;更长的 agent 运行不带来更高分。
- 原文:"Claude Opus 4.7 (Adaptive Reasoning, Max Effort) leads at 47%, followed by GPT-5.5 (xhigh) at 46% and Qwen3.7 Max at 42%" / "Scoring uses average precision at full recall." / "if a model misses any of the ground-truth root causes, it scores 0.0 for that repeat."
- URL:https://artificialanalysis.ai/articles/itbench-aa-launch
- 日期:2026-05-27
- 来源类型:分析机构(与基准方 IBM 合作;经 WebFetch 摘录,未二次逐字核对)
- 承重:是(最新 SOTA)
- 叙事:B(进步但仍不过半)

## L15. Microsoft Ahmed 系后续:ReAct agent 在 100 个抽样事故上人工标注约 34–38 个"正确",检索基线错误答案中 49% 为幻觉
- 论断:Microsoft 团队(Roy et al. 2024)对 100 个抽样生产事故人工标注:检索基线/CoT/ReAct 正确数 38/38/34;检索基线的错误预测中 49% 属幻觉(编造"已重启集群"等未发生的处置),ReAct 降到 6%,但代价是更多"证据不足"拒答(39 例)。
- 原文:"26% (10/38) of the correct predictions made by the RB (k=10) contain hallucinations, while it is < 1% for CoT and ReAct S+Q BM25. Similarly, 49% (29/59) of the RB (k=10)'s incorrect predictions are hallucinations, dropping to 18% (11/59) for CoT and 6%(4/63) for ReAct. Overall, ReAct has the highest precision among the 3, but this comes at the cost of lower overall accuracy." / "we randomly sample 100 incidents from the evaluation set"
- URL:https://arxiv.org/abs/2403.04123
- 日期:2024-03
- 来源类型:预印本 / 工业论文(Microsoft)
- 承重:中
- 叙事:B

## L16. Microsoft Triangle(ASE 2025):"准确率最高 97%、TTE 最多降 91%"是分团队最好值,且是**分派(triage)**不是根因
- 论断:Triangle 解决的是"事故该派给哪个团队",指标是 Time to Engage(TTE);97% 与 91% 均为 "up to",来自不同团队(91% TTE 降幅来自分派准确率最低 82% 的 Team B)。属于检测之后、定位之前的一段。
- 原文:"TRIANGLE significantly improved incident triage accuracy (up to 97%) and reduced Time to Engage (TTE) by as much as 91%" / "Team B experiences the most dramatic impact, with a 91% reduction in TTE." / "While Team B's accuracy is slightly lower at 82%"
- URL:https://conf.researchr.org/details/ase-2025/ase-2025-papers/22/Triangle-Empowering-Incident-Triage-with-Multi-Agent
- 日期:2025(ASE 2025)
- 来源类型:同行评审(Microsoft 自家生产系统)
- 承重:中
- 叙事:A(分派段确有加速)/ C(口径)

## L17. Azure 博客:Triangle 本地分派 6 个团队生产、"agents achieving 90% accuracy",单一团队 TTM 降 38%
- 论断:Microsoft 官方博客(2025-03)称本地分派系统 2024 年中起在 Azure 生产,至 2025-01 有 6 个团队上线;"90% 准确率"(分派接受/拒绝判断)与"一个团队 TTM 降 38%"——TTM 是缓解时间,混合多段,且只有一个团队。
- 原文:"The Local Triage system has been in production in Azure since mid-2024. As of Jan 2025, 6 teams are in production with over 15 teams in the process of onboarding. The initial results are promising, with agents achieving 90% accuracy and one team saw a reduction in their TTM of 38%"
- URL:https://azure.microsoft.com/en-us/blog/optimizing-incident-management-with-aiops-using-the-triangle-system/
- 日期:2025-03-06
- 来源类型:官方一手(厂商口径)
- 承重:中
- 叙事:A/C

## L18. Meta DrP(2025-12):**非 LLM** 的代码化排障手册平台,MTTR 平均改善 20%;LLM 集成仍是"进行中"
- 论断:Meta 自己大规模生产的自动排障平台 DrP(2000+ analyzer、300+ 团队、日均 5 万次分析、5 年生产)靠代码化 playbook + 统计/ML(维度分析、异常检测、代码/配置变更排序),不是 LLM;MTTR 平均改善 20%,深度接入(≥10 个 analyzer)的团队 50–80%。MTTR 的定义是"解决时间戳 − 检测时间戳",**不含检测时间**;对比为用/不用 DrP 的事件(观察性,存在选择偏差)。论文称 LLM 库集成是 ongoing work。
- 原文:"Overall, the average MTTR improvement over the period of study was 20%." / "Teams that onboarded DrP more comprehensively, with at least 10 analyzers, achieved substantially higher MTTR reductions ranging from 50% to 80%." / "aggregating the mean time difference between resolution and detection timestamps" / "We are also actively looking into integrating LLM based libraries into the DrP SDK as part of ongoing work."
- URL:https://arxiv.org/abs/2512.04250 ;https://engineering.fb.com/2025/12/19/data-infrastructure/drp-metas-root-cause-analysis-platform-at-scale/
- 日期:2025-12
- 来源类型:官方一手 / 预印本(Meta 自评)
- 承重:是(大厂最扎实的生产数据来自非 LLM 自动化;且明确 MTTR 不含 TTD)
- 叙事:B/C

## L19. AWS DevOps Agent GA:"up to 75% lower MTTR、80% faster investigations、94% root cause accuracy"——预览期客户与伙伴自报,无方法学
- 论断:AWS GA 博客(2026-03-31)的三个数字来源为"预览期客户与伙伴报告",均为 "up to"/未给分母、事件集合、评判者;94% 准确率未说明 top-k 或谁判定。博客中的客户案例为单次事故:20–30 分钟 vs"估计" 1–2 小时人工。
- 原文:"In preview, customers and partners using AWS DevOps Agent report up to 75% lower MTTR, 80% faster investigations, and 94% root cause accuracy, enabling 3–5x faster incident resolution." / "The full investigation wrapped in 20–30 minutes, roughly a 75% reduction compared to the 1–2 hours it would have taken manually."
- URL:https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/
- 日期:2026-03-31
- 来源类型:厂商自报(厂商口径;AWS 按 agent-秒计费,受益于"更多自动调查")
- 承重:是(最常被引的"94%")
- 叙事:A(宣称)/ 需验证

## L20. LLM 调查由告警触发:AI SRE 普遍位于"检测之后"
- 论断:AWS DevOps Agent 的客户描述与集成说明显示,调查由 CloudWatch 高严重度告警或 PagerDuty 告警**自动触发**——即检测仍由传统监控/阈值/异常检测完成,LLM 缩短的是之后的定位段(TTD 不变)。Datadog 文档同样以"monitor alert 上的 Bits 分析"为入口。
- 原文:"We've integrated AWS DevOps Agent directly into our incident response process, where it automatically triggers investigations on high-severity CloudWatch alarms" / "PagerDuty: Native integration for automatic incident response triggered by PagerDuty alerts"
- URL:https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/
- 日期:2026-03-31
- 来源类型:官方一手(客户引语经厂商发布)
- 承重:是(TTD vs RCA 区分的直接证据)
- 叙事:C

## L21. Azure SRE Agent GA:"1,300+ agents、35,000+ incidents mitigated、20,000+ 工程小时"——产量指标,无准确率
- 论断:Microsoft 内部使用数据以"部署数/缓解事故数/节省工时"呈现,未给根因准确率、误判率、分母(总事故数)或 TTD/TTM 分段;"mitigated"含义未定义。(另有二手来源称 50,000+ 小时,与 GA 帖不一致,未采用)
- 原文:"Microsoft runs Azure SRE Agent across its own services — 1,300+ agents deployed, 35,000+ incidents mitigated, and over 20,000 engineering hours saved."
- URL:https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-general-availability-for-the-azure-sre-agent/4500682
- 日期:2026-03-10
- 来源类型:厂商自报
- 承重:中
- 叙事:A(规模)/ B(无质量口径)

## L22. Datadog Bits AI SRE:内部"真实事故基准"存在但不公开数字;官方承认早期版本把对的线索总结成错的根因
- 论断:Datadog 称用跨数百团队标注的真实事故构建基准并"显著改进",但正文未给出准确率数字;2026-03 版本口径是"约 2 倍快、3–4 分钟完成调查"(速度,不是准确率)。工程博客坦承一个失败模式:12 次工具调用中有一次找到真根因,但被上游噪声信号带偏,最终输出错误根因。
- 原文:"We worked across hundreds of teams at Datadog to collect and label real incidents and used them to create a benchmark dataset of test scenarios." / "One of the tool calls correctly pinpointed the root cause. But because other tool responses included suspicious signals like critical application errors in an upstream service, the summarization prompt returned an incorrect root cause." / "Bits Investigation can complete investigations about 2 times faster than before—in approximately 3-4 minutes, depending on complexity." / "The result is an agent that's more accurate on internal benchmarks and approximately twice as fast."
- URL:https://www.datadoghq.com/blog/building-bits-ai-sre/ ;https://www.datadoghq.com/blog/bits-ai-sre-deeper-reasoning/
- 日期:2026-01-12;2026-03-05
- 来源类型:厂商(官方工程博客)
- 承重:中
- 叙事:B/C

## L23. Traversal:单一 Fortune 100 客户 "82% RCA accuracy in under 5 minutes",跨客户 "around a 40% reduction in MTTR"
- 论断:厂商口径;82% 来自单一金融客户,未说明分母、top-k、评判者;40% 是 MTTR(混合多段)。Traversal 同时是 OpenRCA 批评者(L12)。
- 原文:"a Fortune 100 financial-services customer saw over 82% RCA accuracy in under 5 minutes, and across enterprise clients, Traversal has driven around a 40% reduction in MTTR."
- URL:https://www.traversal.com/blog/ai-sre-accuracy-and-speed
- 日期:约 2026(页面未标日期)
- 来源类型:厂商自报
- 承重:否
- 叙事:A(宣称)

## L24. Resolve AI × Salesforce:MTTR 降 ~60%,但"调查时间"只降 ~30%——MTTR 改善大于定位改善,说明 MTTR 混入了其他段
- 论断:同一客户页上,"调查时间 ~30% 降低"小于"MTTR ~60% 降低",告警分诊 "~70% 更快"。如果 AI 的作用主要在定位,MTTR 的更大降幅必然来自其他因素(分诊、协调、修复流程或基线变化)——是 MTTR 不能当定位/检测证据的现成例子。首页另称 "5x faster MTTR"、"cutting downtime by up to 80%"。
- 原文:"MTTR reduction ~60% Alert triage ~70% faster Investigation time ~30% reduction" / "~60% reduction in mean time to resolve ( MTTR )" / "Drives reliability with 5x faster MTTR"
- URL:https://resolve.ai/customers/salesforce ;https://resolve.ai/
- 日期:访问于 2026-10-30
- 来源类型:厂商自报
- 承重:中(口径论证)
- 叙事:B/C

## L25. Cleric:58% 告警"无需工程师即关闭"(Cleric 自判),51% 已解决事故采用其修复;并宣称做"发布后变更验证"
- 论断:Cleric 首页三个自有指标均为自评口径:"No action needed" 由 Cleric 自己判定(经 WebFetch 读取到的脚注,未经 curl 复核),工程师评分为可选打分。它把产品定位延伸到发布后检测("检查每个变更……在成为事故前修复回归"),但未给出回归检出率、误报率或检出时间——这是 LLM 进入"检测段"的宣称,无测量。自动关闭告警若误判,即为漏检代价。
- 原文:"58% Alerts Closed Without an Engineer 51% Resolutions That Applied Cleric's Fix 4.08/5 Average Engineer Rating" / "Cleric checks each change in production and fixes any regressions before they become incidents."
- URL:https://cleric.ai/
- 日期:访问于 2026-10-30(统计窗口称 2026 年 5–10 月)
- 来源类型:厂商自报
- 承重:中(唯一明确宣称 LLM 做发布后检测的样本)
- 叙事:A(宣称)/ B(自判口径)

## L26. Grafana:单一内部事故轶事——AI 8 分钟找到根因,比 on-call 早 20 分钟
- 论断:标题"3.5x faster"来自一个事故;且 AI 是在告警触发、人类已开始排查后并行启动。属 n=1 轶事。
- 原文:"Eight minutes later, it found the root cause, 20 minutes before our on-call team came to the same conclusion."
- URL:https://grafana.com/blog/a-tale-of-two-incident-responses-how-our-ai-assist-helped-us-find-the-cause-3-5x-faster/
- 日期:2026-01-29
- 来源类型:厂商(从业者博客)
- 承重:否
- 叙事:A(轶事)

## L27. 厂商自己给买家的评估建议:用 5–10 个已结事故回放——行业评估样本量的现实
- 论断:incident.io 建议买家用 precision/recall 做历史回放,但样本仅 "5-10 closed incidents";说明大多数"客户自测准确率"背后的样本量可能极小。
- 原文:"Run historical incidents with known root causes through the system to measure AI accuracy. Select test incidents: Choose 5-10 closed incidents where you definitively know the root cause."
- URL:https://incident.io/blog/ai-root-cause-analysis-accuracy-testing-guide
- 日期:2026-02-20
- 来源类型:厂商(从业者博客)
- 承重:否
- 叙事:B/C

## L28. Google Gemini Cloud Assist investigations:仍为 Preview,官方文档承认结果不确定、无准确率
- 论断:Google 未公布准确率;文档明言同一调查重跑结果会不同(LLM 概率性 + 云状态变化),且 2026-04 后限 Premium Support 用户。
- 原文:"Investigations are subject to the general limitations of AI technology. Investigation runs are dynamic, which means re-running the same investigation can produce results with small differences." / "the probabilistic nature of output from large-language models such as Gemini"
- URL:https://docs.cloud.google.com/cloud-assist/investigations
- 日期:访问于 2026-10-30
- 来源类型:官方一手
- 承重:否
- 叙事:B/C

## L29. 信任差距:PagerDuty 赞助调研中 59% IT 决策者 vs 37% 开发者预期 AI 让停机/恢复改善 >20%
- 论断:注意这不是"信任"问题本身,而是对改善幅度 >20% 的预期;来源为 PagerDuty 赞助的 The New Stack 文章(利益相关)。
- 原文:"Research indicates that 59% of IT decision-makers expect AI to improve downtime and recovery performance by more than 20%. However, developers appear not to share the same enthusiasm, with only 37% agreeing."
- URL:https://thenewstack.io/fix-developer-burnout-outages/
- 日期:2026-04-21
- 来源类型:媒体转述(厂商赞助内容)
- 承重:否
- 叙事:B

---

## 交叉口径问题(供验证阶段)

1. **top-k 不一致**:Meta 42% = top-5 候选变更命中;AIOpsLab 定位报 Acc@1 与 Acc@3;OpenRCA/ITBench-AA = 全部要素/全部根因命中才计分;AWS 94%、Traversal 82% 未说明 top-k。不可横比。
2. **分母类型**:回放历史事件(Meta、Ahmed、RCACopilot、Roy)vs 故障注入基准(AIOpsLab、ITBench、OpenRCA 2.0)vs 客户自报生产事件(AWS、Traversal、Resolve)vs 厂商自判(Cleric "No action needed")。
3. **"accuracy" 一词偷换**:RCACopilot "accuracy up to 0.766" 实为类别分类 Micro-F1;Ahmed 用 BLEU/人评 1–5 分;Triangle 97% 为分派准确率而非根因。
4. **严格 vs 宽松判定差距巨大**:OpenRCA 2.0 同一批模型 20.7%(精确根因集)vs 76.0%(至少一个正确服务)vs 61.5%(有因果链)。任何宣称都应追问用的是哪档。
5. **MTTR ≠ 定位 ≠ 检测**:DrP 明确 MTTR = 解决 − 检测时间戳(不含 TTD);Resolve/Salesforce MTTR 降幅(60%)大于调查时间降幅(30%);Triangle 的 TTE、Azure 博客的 TTM 各是不同段。没有任何一个厂商/论文给出 LLM 缩短 TTD 的实测。
6. **LLM 是否参与检测**:证据仅有 (a) AIOpsLab 的二元检测题(故障已注入、样本十余题、无误报率);(b) Cleric 的"变更验证"宣称(无数字)。生产中 AWS/Datadog/PagerDuty 的调查均由告警触发。
7. **基准分数的时间线**:OpenRCA 11.34%(Claude 3.5,2024 末)→ ~34.9%(Opus 4.6,2026-02,厂商自报、聚合站转录、"已提交官方验证"但截至访问仍 Unverified);ITBench 13.81%(GPT-4o,2025)→ 47%(Opus 4.7,ITBench-AA,2026-05,评分规则不同)。不同版本/评分规则不可连成趋势线而不加说明。
8. **人类基线缺失**:OpenRCA、ITBench、ITBench-AA、AIOpsLab 均无人类 SRE 基线;"AI 比人快多少"只有厂商轶事(Grafana n=1、AWS 单案"估计 1–2 小时")。
9. **覆盖率(reach)隐藏**:Meta 用置信度过滤低置信答案、ReAct 更多"证据不足"拒答——准确率提升可能以覆盖率下降换取,厂商均不报覆盖率。
10. **利益相关**:Microsoft 自建 AIOpsLab/OpenRCA 并让自家 agent 参评;IBM 自建 ITBench;Anthropic 自报 OpenRCA;Traversal 既批评 OpenRCA 又卖产品;PagerDuty 赞助信任调研。

---

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
