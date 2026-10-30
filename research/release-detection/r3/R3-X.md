# R3-X 反证搜索：发布检测器的定量检出率是否「几乎全部来自 2015–2020 年系统所有者自评、无独立复测」

日期：2026-10-30｜席位：Round 3 反证搜索

## 结论：降级（原句要改写，核心方向成立）

「主要定量证据是系统所有者自评」这个方向成立：没有找到任何第三方拿到 Gandalf、FBDetect、Kayenta 或 CAS 的生产数据去复测检出率。但原句有三处不成立，必须改写：

1. **年代错误**：FBDetect 是 SOSP 2024 的论文，不属于 2015–2020；2021–2026 年还有 Slack（2025-10）、Atoms/CloudKitchens（2025-11）、SCELM（2025）等新的自报数字。
2. **「没有独立复测」说得太绝对**：SCELM（南开/清华/中科院自动化所，2025 年 arXiv 2507.09315）在三份第三方数据集上把 Gandalf 等五个方法重新实现成基线并报告了 F1。这是独立团队对**算法**的复测，只是没有复测**生产系统**。
3. **承重数字本身有内部问题**：原文自己算出的数字对不上，下文第 1 节第 1 条和第 2 条给出了细节。

## 一、对承重实证的核查（读了原文 PDF）

### 1. Gandalf（NSDI 2020）控制面的 recall 99.8% 与原文给的计数对不上
原文 §6：控制面「decisions for 1200+ region-level deployments. The precision is 94.9% and recall is 99.8%. Gandalf filed 39 incidents and only 2 of them are false alarms … only missed 2 true issues」。
- 按原文计数：TP = 37，FP = 2，FN = 2。precision = 37/39 = 94.9%，与原文一致；但 recall 按标准定义应为 37/(37+2) = **94.9%**，不是 99.8%。
- 99.8% 大约等于 (1200−2)/1200，看起来是用「全部决策」做的分母，更接近 accuracy 或 specificity，而不是 recall。
- 成文时如果引用「控制面 recall 99.8%」，应该写成「论文报告 99.8%，但按其给出的计数（漏 2 / 抓 37）算标准 recall 约 95%」，或者干脆只引用计数。
- 数据面的「100% recall」是代理定义（原文：「no high-impact incidents were caused by bad rollouts」），时间窗为 2018 年 1–11 月，共捕获 155 次 critical failure。brief 对此的描述准确。

### 2. FBDetect（SOSP 2024）的召回率是假设出来的，不是测出来的
- 0.005% 级回归检测、一个月 217 条报告、70 条有人确认，其中 49 真 / 21 假（另有 123 条标为 resolved、24 条无人处理），brief 的这些描述都准确。
- 与 Yahoo EGADS 对比时，原文写的是「Since FBDetect has almost no false negatives … **we assume its false negative rate is zero**」。也就是说，召回率是假设值，不是测量值。
- 与 EGADS 的对比由 Meta 自己的团队完成，用的是 Meta 的数据，标签也是自己人工标注（107 条阳性中 76 真 / 31 假）。
- 原文还给了一个有用的反衬数字：普通 change-point 算法在他们的环境里误报率为 99.7%。

### 3. Google CAS
research.google 的论文页只给出「hundreds of thousands of production changes per day」的评估量，没有拦截率。brief 的描述准确，本轮没有新发现。

## 二、搜索角度与结果（含没搜到的）

| # | 角度 | 结果 |
|---|---|---|
| 1 | 拿 Gandalf 当基线的第三方论文 | **找到**：SCELM（arXiv 2507.09315，Sun/Kuang/…/Dan Pei，另有一位腾讯作者）。ECD 任务在 yunzhanghu、kontrast、bytedance 三份数据集上的平均 F1：SCWarn 0.8935、Kontrast 0.888、Lumos 0.868、Funnel 0.869、**Gandalf 0.8685**，SCELM 自己为 0.925–1.000。**质量警告**：arXiv 版的 §5.1 实验设置只有占位条目（「Baseline Approach / Evaluation Metric」后面没有内容），没有说明 Gandalf 是怎么重新实现的、F1 按什么粒度算；作者也是竞品方。FSE 2025 版的主页（weihuakuang.github.io）只提到两份微服务数据集，没有点名 Gandalf。 |
| 2 | SCWarn（FSE 2021，清华裴丹组）的基线 | 原文报告平均 F1 0.95；HADES（arXiv 2207.02918）复测 SCWarn 时得到约 0.78–0.95。这是对**算法**的独立复测，并且显示复测值低于原作者自报。我没有核实 SCWarn 是否用 Gandalf 做了基线。 |
| 3 | Kontrast 原论文 | 没搜到原文（只在 SCELM 中作为基线和数据集名出现）。 |
| 4 | FBDetect 的独立复现 | **没有**。引用 FBDetect 的 MobileUPReg（arXiv 2509.16864）只是相关工作，没有复测。TinyRegression（TOCS）仍是 Meta 自己的论文。 |
| 5 | Kayenta / 自动 canary 分析的第三方误报率评测 | **没有**。只有 Netflix 自家的 KDD 2022 序贯检验论文（arXiv 2205.14762，两个案例研究，没有拦截率）和从业者演讲里的定性说法。 |
| 6 | 2021–2026 年其他公司带分母的数字 | **自报有，带分母的拦截率或误回滚率没有**。Slack「Deploy Safety」（2025-10-07）：73% 的面向客户事故由变更触发；2024 年 4 月引入自动回滚后，客户影响小时数从 2024 年 2 月到 2025 年 1 月下降 90%。这是结果指标，没有回滚次数、误回滚数或检出率。Atoms（原 CloudKitchens，2025-11-06）：超过 80% 的发布走 canary，2025 年第三季度拦下 1,100 多次坏发布，但没有总发布数；FP/FN 有跟踪，没有公布。Headout（博客）：误回滚从每周 5 次降到 1 次，抓到 3 次坏发布，同样没有分母。Uber、LinkedIn、Netflix、Shopify、Spotify、阿里、字节、腾讯：没有搜到公开的检出率或误回滚率（只有字节作为 SCELM 数据集来源出现）。 |
| 7 | 业界调查中的自动回滚采用率和效果 | **没有**。Perforce 2026 State of DevOps（820 人）把自动回滚当作成熟度特征，摘要里没有百分比；theCUBE 2025 的片段不可读；DORA 只有 change failure rate，不衡量检测器。 |
| 8 | 变更与事故关联的独立复测 | **找到**：Kapel, Cruz, Spinellis, van Deursen「On the Difficulty of Identifying Incident-Inducing Changes」，ICSE-SEIP 2024。这是学术团队在一家企业里复现已有的变更–事故关联方法，结论是历史数据上的评估与实地观察显著不一致，对无标签变更做关联时误报更多。PDF 下载超时，没有拿到具体数字；工业方是不是 ING 也未证实。这项工作针对的是事后归因，不是发布闸门，但它是「自评偏乐观」最接近的独立证据。 |
| 9 | ISSRE 2023「How to Manage Change-Induced Incidents?」（231 起事故） | 只拿到书目信息，没有拿到检测相关的数字。 |
| 10 | Google 2021–2026 的新数字（Prodspec、safe rollout） | 没有。 |

## 三、成文时可以怎么说 / 不能怎么说

**可以说：**
- 「公开的发布检测器检出率，几乎都来自系统所有者对自家生产系统的自评（Microsoft Gandalf 2020、Meta FBDetect 2024），我们没有找到任何第三方拿生产数据复测过。」
- 「这些自评的『召回率』都是代理或假设：Gandalf 把『没有发生由坏发布引起的 Sev0-2 事故』当作 100% recall；FBDetect 直接假设漏报率为零。」
- 「学术界在别家数据上重新实现 Gandalf 时，F1 约 0.87（SCELM 2025，竞品作者、实验细节不全）。这说明它在别处并非『百分之百』，但这个数字本身也不够硬。」
- 「2024–2025 年 Slack、Atoms 等公司公布的是结果指标（客户影响时长下降 90%、一个季度拦下 1,100 多次坏发布），都没有分母，也没有公布误回滚率。」

**不能说：**
- 「定量数据几乎全来自 2015–2020 年」：FBDetect 是 2024 年，Slack、Atoms 是 2025 年。
- 「完全没有独立复测」：算法层面有 SCELM 和 HADES 这类第三方基线复测，事后归因层面有 Kapel 2024。应改为「没有对生产系统的独立复测」。
- 「Gandalf 控制面 recall 99.8%」：不能不加说明地照搬，按原文计数算是约 95%。
- 「FBDetect 召回率接近 100%」：原文是假设，不是测量。
- 任何「业界自动回滚采用率 X%」的说法：没有找到可靠的调查数据。

## 来源
- Gandalf PDF：https://web.eecs.umich.edu/~ryanph/paper/gandalf-nsdi20.pdf（§6，本地文本见 scratchpad/dl/r3-R3-X/gandalf/g.txt）
- FBDetect PDF：https://tangchq74.github.io/FBDetect-SOSP24.pdf（False positive 段落与 EGADS 对比段落）
- SCELM：https://arxiv.org/abs/2507.09315；FSE 版主页：https://weihuakuang.github.io/publication/2025-03-FSE2025-SCELM
- HADES：https://arxiv.org/pdf/2207.02918；SCWarn：https://2021.esec-fse.org/details/fse-2021-papers/97/
- Kapel et al. ICSE-SEIP 2024：https://luiscruz.github.io/publications/2024-04-kapel-incident-inducing.html（DOI 10.1145/3639477.3639755）
- Netflix 序贯检验：https://arxiv.org/abs/2205.14762
- Google CAS：https://research.google/pubs/canary-analysis-service/
- Slack Deploy Safety：https://slack.engineering/deploy-safety/
- Atoms/CloudKitchens：https://techblog.atoms.co/p/deployment-confidence-in-era-of-ai
- Headout：https://backstage.headout.com/canary-deployment-with-automated-rollback/
- ISSRE 2023 change-induced incidents：https://researchr.org/publication/ZhaoJTZWWJLW23
