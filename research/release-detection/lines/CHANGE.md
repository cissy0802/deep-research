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
