# 22. 成文一致性回查(2026-10-30)

依据:05-locked-calibers.md。核对对象:sources/release-detection-deep.zh.md、sources/release-detection-plain.zh.md。
URL 核对:deep 版「附:主要来源」逐条在 lines/、verdicts/、locked/ 中做子串检索;找不到的换成底稿实际使用的 URL。没有联网。

共修改 46 处:deep 正文 22 处、deep 来源 URL 11 处、plain 13 处。另列疑点 10 条(见第四节)。

## 一、deep 版正文

| # | 位置 | 原文 | 改为 | 依据 |
|---|---|---|---|---|
| 1 | §2 Microsoft 306 服务 | 由客户或工程师报告的那 3.3%,检测平均慢约 10.7 倍,缓解慢约 3.75 倍 | 那 3.3% 里,客户报告的事故检测平均耗时约为监控报告的 10.7 倍(工程师报告约 9.96 倍),缓解约为 3.75 倍 | L02-3(10.7× 只对应客户报告;工程师 9.96×;3.75× 只对应客户报告) |
| 2 | §2 三数不能排趋势 | GenAI 混合严重度 | GenAI 关键词识别(严重度未说明,推断为混合) | L02-4 修正记录(论文未说明严重度,须标为推测);R3-1 |
| 3 | §2 Ranganathan | 156 起高严重度事故中约 74% 在客户报告之前由探针告警 | 156 起 Sev2/2.5 事故中约 74% 在客户报告之前由健康探针或 DRI 流水线告警 | L02-5、R3-2(auto-detected 定义) |
| 4 | §3 表 GCP 主要缓解 | 约 2–3 小时(视口径) | 40 分钟–3 小时(视口径) | 锁定案例表 GCP 行(red-button 推完 40 分钟 / 1h59m / 3h00m);n=9 缓解中位计算中 GCP 取 40 或 119 |
| 5 | §3 表 AFD 10-09 主要缓解 | 约 5 小时 | 5h00m–8h10m(视口径) | 锁定案例表 AFD-09 行 |
| 6 | §3 止血是小时级 | 只有两案在 1 小时内止血 | 确定在 1 小时内止血的只有两案(另有两案视口径而定) | 锁定口径 n=9「主要缓解」:GCP、Fastly 视口径而定 |
| 7 | §3 客户先发现 | ……首个信号就是客户工单。【单源已核】 | 补「第 2 节里 Teams Sev≤2 事故有 29% 由外部客户报告,GenAI 服务 38.3% 由人报告」;标注改为【样本内计数单源已核;作为一般结论方向存争】 | L03-2(必须紧跟 Teams、GenAI、Atlassian 三项对照;分级) |
| 8 | §4 AFD 传播速度 | 客户配置约 5–10 分钟到全球 | 客户配置按「行业预期」约 5–10 分钟到全球 | L04-2 修正记录、L04-5(原文是行业预期,不是 AFD 自己的历史统计) |
| 9 | §4 六类盲区表第 2 类 | 部署后 24–72 小时才 OS 崩溃 | 补「(该案最终在 Canary 阶段被 Gandalf 检出)」 | S3 表第 2 类注意、L05-5 禁止写法(案例 III 不是漏报) |
| 10 | §4 六类盲区表第 4 类 | 22%(三个月窗口) | 22%(三个月窗口,仅一席核) | S3 使用约束、L07-4 |
| 11 | §4 六类盲区标注 | 【各例证单源已核;第六类为假设算例……】 | 补「第五类的低流量盲区机制为推断」 | S3 第 5 类分级、L06-9 |
| 12 | §5 Gandalf 控制面 | 数值上与「1 − 漏报/全部部署」吻合 | 数值上与「1 − 漏报/全部部署」、specificity、NPV 三者都吻合,分母无法判定 | L05-2(只列一种会暗示「分母就是全部部署」,属禁止写法) |
| 13 | §5 FBDetect 降噪 | 未经大量工程化过滤的异常检测,在生产里几乎全是噪声 | 在 Meta 的性能时间序列场景里,未经大量工程化过滤的异常检测几乎全是噪声 | L08-3 锁定表述限定场景;Part 2 适用域总警告 |
| 14 | §6 ServiceLab | 【单源已核】 | 【单源已核:仅一席核到原文】 | L08-8(代价数字只有 G08-R 核过) |
| 15 | §7 ICLR 2026 | 与一行代码的基线相当 | 与一行代码的基线没有显著差异 | G09-6(锁定措辞「无显著差异」) |
| 16 | §8 RCACopilot | 依赖每个团队手工构建的诊断 handler | 依赖 OCE 按告警类型手工构建的诊断 handler | G12-3 修正记录 |
| 17 | §8 Triangle | Microsoft Triangle 的 97%/91% | Microsoft Triangle 的「up to 97%」/「as much as 91%」 | G12-5 禁止写法(不带 up to) |
| 18 | §8 ITBench | GPT-4o 诊断 13.81%,去掉 trace 数据后 9.52% | GPT-4o 诊断 13.81%;开 trace 的场景组 18.10%、关 trace 的另一组 9.52%,两组是不同场景,只能说明方向 | G13-6、否决清单 Part 3 #21(trace 消融被降为只表方向) |
| 19 | §8 Grafana | 离线验证漏掉,上线后被监控发现 | 离线验证漏掉,上线后被发现(触发方式原文未明确) | G14-6(「由告警发起」未验证)、否决清单 Part 3 #28 |
| 20 | §9 检测 | 监控在 1–25 分钟内就看见了问题 | 首个检测信号在影响开始后 1–25 分钟内出现 | L03-1(含 GCP 分诊、CF-2026 engaged 等代理信号;3/9 发现来源未披露) |
| 21 | §9 检测 | Microsoft 的漏检里,超过四成是根本没有相关监控 | Microsoft 的漏检类修复项里,超过四成…… | L02-3 禁止写法(40%/30% 的单位是 repair item,不是事故) |
| 22 | §9 缓解 | 止血中位约 2–3 小时 | 止血中位约 1.8–3 小时 | 锁定口径 n=9 主要缓解、L03-3 |

## 二、deep 版「附:主要来源」URL

| # | 文献 | 原 URL | 改为 | 依据 |
|---|---|---|---|---|
| 23 | DORA 指标说明 | https://dora.dev/guides/dora-metrics-four-keys/ | https://dora.dev/insights/dora-metrics-history/ | 底稿无原 URL;L15-1 使用后者 |
| 24 | Ghosh 等 SoCC'22 | https://dl.acm.org/doi/10.1145/3542929.3563482 | https://www.microsoft.com/en-us/research/wp-content/uploads/2022/09/3542929.3563482.pdf | 底稿只有 DOI 文本与微软 PDF;L02-1 |
| 25 | Ganatra 等 ESEC/FSE'23 | https://dl.acm.org/doi/10.1145/3611643.3613898 | https://jonathanmace.github.io/papers/ganatra2023detection.pdf | 底稿无此 DOI;L02-3、R3-3 |
| 26 | Ranganathan 等 | https://arxiv.org/abs/2511.07424 | https://arxiv.org/pdf/2511.07424 | 底稿用 pdf/html 形式;L02-5 |
| 27 | Azure 复盘 | https://azure.status.microsoft/status/history/(泛首页) | 拆为 YKYN-BWZ 与 QNBQ-5W8 两个 PIR 具体链接 | L03-5、L04-2 |
| 28 | Kayenta | https://netflixtechblog.com/automated-canary-analysis-at-netflix-with-kayenta-3260bc7acc69 | https://cloud.google.com/blog/products/gcp/introducing-kayenta-an-open-automated-canary-analysis-tool-from-google-and-netflix | 底稿无 Netflix 博客具体 URL;L06-8 用 Google Cloud 发布稿 |
| 29 | TSB-AD | https://arxiv.org/abs/2412.10599 | NeurIPS 2024 proceedings PDF(c3f3c690…) | 底稿无 arXiv 号;G09-5「以 proceedings 版为准」 |
| 30 | Opprentice IMC'15 | https://conferences.sigcomm.org/imc/2015/papers/p211.pdf | http://conferences2.sigcomm.org/imc/2015/papers/p211.pdf | 底稿实际 URL;L10-1 |
| 31 | OpenRCA | https://openreview.net/forum?id=M4qNIzQYpd | ICLR 2025 proceedings PDF(d29b8d53…) | 底稿无 openreview id;G13-2 |
| 32 | AWS DevOps Agent GA | https://aws.amazon.com/blogs/aws/(泛首页) | https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/ | G14-1、G14-2 |
| 33 | Grafana 案例 | https://grafana.com/blog/(泛首页) | https://grafana.com/blog/a-tale-of-two-incident-responses-how-our-ai-assist-helped-us-find-the-cause-3-5x-faster/ | G14-6 |

其余 URL 均能在 lines/ 或 locked/ 中原样检出。Google CAS 的 queue.acm.org/detail.cfm?id=3194655 在 lines/CANARY.md 中以无协议头的形式出现,保留未改(locked 用的是 https://sre.google/static/pdf/canary_analysis.pdf,同一篇文章)。

## 三、plain 版

| # | 位置 | 原文 | 改为 | 依据 |
|---|---|---|---|---|
| 34 | 坏发布从哪来 | Facebook 某三个月里约 16% | Facebook 某三个月的严重事故里,与配置管理有关的约 16% | L01-4(16% 是配置管理相关,不是「改动引起」) |
| 35 | 谁先发现 | 漏掉的情况里,四成以上是「根本没装相关监控」 | 漏检之后定下的改进项里,四成以上…… | L02-3(单位是修复项) |
| 36 | 谁先发现·结论 | 越严重、越新的服务,靠人发现的比例越高 | 在严重事故和新类型的服务上,靠人发现的比例不小 | G02 组级禁令(不同口径不能连成趋势) |
| 37 | 公开大事故 | 9 份由坏发布引起的大事故 | 9 份由变更引起的大事故 | L03-2(n=9 为「由变更引发」;AFD-09 是人工操作、Fastly 是潜伏代码) |
| 38 | 公开大事故 | 止血中位数约 2 到 3 小时 | 约 1.8 到 3 小时 | 锁定口径 n=9 主要缓解 |
| 39 | 发现了也不一定有人信 | 团队觉得「肯定跟我们无关」,硬是绕过去了 | 相关团队认为告警跟这次发布无关,发布负责人就要求绕了过去 | L05-6(绕过由 release manager 提出;原引号句非原文) |
| 40 | 实验室分数 | 完全随机乱猜……只剩 0.1 到 0.2 分;八成多的题目简单到一行公式就能解 | 补「在四个常用数据集上」「约」;一行公式补「参数是逐题对着答案调出来的」 | G09-1(SMD 为反例)、G09-2 禁止写法 |
| 41 | 找原因 | 「至少找对一个出问题的服务」的宽松标准能到 76% | 11 个前沿模型……平均 76% | G13-4(76% 是 11 模型平均) |
| 42 | Grafana | 上线后监控发现了 | 上线后才发现 | G14-6(触发方式未验证) |
| 43 | 最要紧 #1 | 大事故的「发现」已经很快了,通常几分钟 | 公开复盘里的大事故,「发现」已经很快了,中位数几分钟 | L03-1 禁止写法、Part 1 否决 #4(总体推断被否) |
| 44 | 最要紧 #3 | 最贵的几次事故都出在这里 | 我们核对的 9 起大事故里,5 起出在这类不分阶段的通道上 | L04-1(5/9;「最贵」无依据) |
| 45 | 怎么检验 | 越严重、越新的服务越靠人发现 | 严重事故和新服务更多靠人发现 | G02 组级禁令 |
| 46 | 附·被推翻 | 改成「止血中位约 2 到 3 小时」 | 约 1.8 到 3 小时 | L03-3 |

(编号连续计,实际修改 46 处:deep 正文 22、URL 11、plain 13。)

## 四、疑点(判断有问题但未改)

1. **标点风格**:委托要求「中文全角逗号句号」,但两份稿件和 sources/ 下所有 zh 稿都用半角逗号「,」、半角问号,只有句号是全角。为与全仓库一致,改动处沿用半角逗号。是否要全仓统一换全角,需要委托方决定。
2. **deep §3 末句**「它回答不了安静的回归要多久才被发现——那恰恰是第 2 节里客户报告、检测慢 10 倍的那部分」:把 Ganatra 的「客户报告事故」等同于「安静回归」是推论,锁定里没有这层对应。
3. **deep §9 缓解段**「最长的那几次,是因为回滚基线已被污染,或者坏数据已经在几秒内复制到全球」:最长的 AFD-29(LKG 污染)、GCP(全球复制)成立,但 AFD-09(8h10m,人工绕过)和 CF-2026(5h+,逐步施加)不属于这两类,归因偏宽。
4. **Slack 90%**(deep §3、plain 公开大事故节):「引入自动回滚后……下降 90%」读起来带因果;L03-4 允许引用,LR3-2 禁止「用自动回滚把事故减少了 90%」。现写法说的是客户影响小时数、标了厂商口径,未改;如要更稳,可补「2024-02 至 2025-01,无因果设计」。
5. **deep §5「在 2018 年的一个窗口里」**:L05-1/D4 要求写「论文自称 8 个月(标注 2018-01 至 2018-11,日历跨度不符)」。现写法回避了 8 个月,没有违反禁止写法,未改。
6. **deep §6「噪声大的 canary 会被运维禁用或无视」**放在「Google: CAS」条下、标【单源已核:定性】;这句其实出自 SRE Workbook(L06-7),分级为厂商口径。
7. **「严格口径两成到五成」**(deep §8、§9、主张 6;plain):照搬成文要点,但同节的 OpenRCA 1.0 严格口径 11.34%、复测 3.9–12.5% 都低于两成,区间下限与正文数字不完全自洽。
8. **plain「Google 说它的金丝雀分析系统『可能避免了数百起事故』」**:原文是「数百起值得写 postmortem 的故障」,易读版略去了限定,未改。
9. **方法学前言统计**:396 / 234 / 162 与 05 的逐条重数一致,但 STATE.md 运行日志记的是 397 / 231 / 166,两处底稿不一致;文章按 05 写,未改。
10. **deep §4「配置变更通过 Quicksilver 在数秒内到达约 90% 的服务器」**:Quicksilver 出现在 lines/CANARY 和 G04 判决里,但锁定表述只写「新建 DNS 记录或安全规则会在数秒内到达 90% 的服务器」,不是泛指全部配置变更,范围可能偏宽。
