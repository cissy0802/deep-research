# R3 · R4-X 反证搜索席
靶子:TiCoder(Fakhoury et al., TSE 2024 / arXiv 2404.10100)用户研究数字(正确判断 0.40→0.84 p=0.001;NASA-TLX 认知负荷 45.46→28.00/29.52;耗时不显著)与标题数字「平均绝对提升 45.97%(v2 摘要)/45.73%(正文)/38.43%(v1)」。论断 ID:G03 · P14、P15、P16、P17(P19 为其二次转述)。

今天复核了:
- arXiv 2404.10100 v1、v2 PDF(pdftotext -layout;v2 Table III 第 486–515 行,Table IV 第 675–697 行);Smfakhoury/TiCoder-project(README + TiCoder.pdf,浅克隆);**microsoft/TiCoder 官方代码仓**(HEAD 3362f00,2025-05-16;README、TRANSPARENCY.md、src/compute_metrics.py);gsakkas.github.io 的 ticoder_icse_2024.pdf(与 v1 逐字节相同)。
- 独立团队:Ferdowsi, Huang, James, Polikarpova, Lerner(UCSD),*Validating AI-Generated Code with Live Programming*,CHI 2024,arXiv 2306.09541(全文 PDF);Mu, Shi, Wang 等(中科院软件所/北航/York/华为),*ClarifyGPT*,arXiv 2310.10996v1(全文 PDF);Yuan, Lu, Wu, Jin, Wu(香港大学),*Guiding Human Validation of LLM-Generated Code via Verifiable Literate Programming*(VLP),arXiv 2607.02333v1(全文 PDF,Fig. 4/5 以 200dpi 渲染读数);Mathews & Nagappan(Waterloo)TGen,已由 R2 取得,本席未重复。
- Semantic Scholar 引用表(arXiv:2404.10100 的 179 篇施引文献,标题逐条筛);抽查 8 篇施引全文(2607.02333、2607.17927、2610.01769、2604.21505、2608.12355、2609.12012、2610.02952、2601.03878),看有无复跑/复现或数字转引。

没拿到:
- TiCoder 用户研究的逐人逐任务原始数据(两个作者仓库与官方代码仓均未提供;官方仓也不含 Table IV 所用的 100 代码 + 50 测试缓存,无法复跑基准)。
- ICSE 2024 海报两页版(ACM Companion pp. 390–391;conf.researchr.org 本会话不可达,dl.acm.org 未试)。同一团队,即便取得也不算独立。
- Zhang et al. UIST 2020 *Interactive Program Synthesis by Augmented Examples*(正则合成领域、示例消歧用户研究,12 人):web.eecs.umich.edu 不可达,只有搜索摘要,**不作证据**。
- Semantic Scholar 详情接口 429 限流;施引文献只按标题筛,未逐篇读全文(179 篇中读了 8 篇)。

## 一、发现

**F1 TiCoder 用户研究:没有找到任何独立复现或重做。** 原文作者全部来自 Microsoft Research 及合作者。179 篇施引文献按标题筛查,没有一篇对"测试驱动的意图确认能让人更准确地判断 AI 代码"做同设计的用户实验。抽查的 8 篇只在相关工作里提到 TiCoder,没有一篇转引 0.40/0.84 或 45.97%。"15 professional developers / p<0.001"的转述只出现在作者本人的博客和 arXiv 2603.17150 中(R2 已查),没有扩散到第三方论文。

**F2 最接近的独立用户研究(Ferdowsi et al., CHI 2024, UCSD, NSF 2107397 资助)方向一致,但没有达到显著。** 实验干预是"执行式验证"(Live Programming 实时显示运行值),不是"测试确认",所以只算相邻机制。设计为组间,共 17 人(LP 8 / No-LP 9),每组有 2 个 Fixed-Prompt 任务(Bigram、Pandas),每题 5 个候选,其中 Pandas 有 2 个正确。
- 验证成功率:6 次失败全部出在 No-LP 组(Bigram 3 次过度信任、Pandas 3 次信任不足),但"the overall between-group difference was not significant (p = .206 for both tasks)"(PDF p.4,§5.1)。本席用 Fisher 精确检验复算 Bigram 的 8/8 vs 6/9,双侧 p = 0.2059,与原文一致。
- 认知负荷:只在 Pandas 任务上显著(NASA-TLX 五项中四项显著,mental p=.039、performance p=.048、effort p=.015、frustration p=.0004),Bigram 无显著差异(§5.3)。
- 耗时与信心:组间都不显著(§5.1 脚注 3)。
- 对照 TiCoder:两项研究的方向相同(给用户可执行的行为证据 → 更少误判、负荷更低),但 Ferdowsi 的准确率效应不显著,负荷效应依任务而定。它**不能独立证实"约翻倍"这个幅度**,只能说"方向上有一项小样本独立研究支持,但没有达到统计显著"。

**F3 独立团队用模拟用户复跑 TiCoder 基准,在新基准和新模型上增益很小,部分为负。** VLP(香港大学,arXiv 2607.02333v1,2026-07,预印本)把 TiCoder 作为基线,按官方 GitHub 仓库实现。模拟器拿到参考实现作为 oracle,对"TiCoder 生成的 5 个候选测试"给出 pass/fail(相当于 PassFail 模式,Table IV)。Fig. 4(p.8)的柱上数值如下(Default → TiCoder):
  | 模型 | BCB-All | BCB-Hard | QCE-Full |
  |---|---|---|---|
  | DeepSeek V4 Flash | 48.1 → 51.1(+3.0) | 30.4 → 30.4(0.0) | 28.7 → 51.4(+22.7) |
  | GPT-5.4 | 49.9 → 52.5(+2.6) | 30.4 → 31.8(+1.4) | 73.2 → 68.0(**−5.2**) |
  - 对照原文 Table IV:三个对话模型 PassFail m=5 的增幅为 13.3–19.8 pp,全部 14 组的 Output m=5 平均为 33.50 pp。到了 BigCodeBench 这类依赖库、带隐藏要求的任务上,6 个格子中有 5 个增幅在 −5.2 到 +3.0 pp 之间,只有 QCE/DeepSeek 一格达到 +22.7。
  - 真人部分:VLP 另有 8 人真人研究(2 人试点,另有 GPT-5.4,8 个此前未被解出的任务)。TiCoder 的满意度在五项中有三项最低或并列最低(bug finding 3.3、low effort 2.1、understanding 2.4、confidence 3.1、overall 3.1,Fig. 5)。passed-checks 曲线只能从图上粗读,本席不报具体数字。
  - 限定:(a) VLP 作者是竞争方法的提出者,利益方向与 TiCoder 相反;(b) 交互次数 m 没有写明,"5 个候选测试"可能对应 m≤5;(c) 基准、模型、年代都与原文不同,所以这是**外推性矛盾**,不是对 MBPP/HumanEval 原数字的直接推翻;(d) 预印本,未经同行评审;数值由本席从渲染图上读出,柱顶标签清晰可读。

**F4 另一个独立团队用真人回答澄清问题,在 MBPP 上的增益约为 TiCoder 理想化上界的一半到三分之二。** ClarifyGPT(arXiv 2310.10996v1)让 10 名非作者参与者回答澄清问题(每题 3 人作答后取平均),GPT-4 在 MBPP-sanitized 上 70.96 → 80.80,MBPP-ET 上 51.52 → 60.19(Table 2,第 544–547 行)。注意:原文"an increase of 13.87%"是**相对**提升(80.80/70.96 = 1.1387),绝对提升只有 **+9.84 pp / +8.67 pp**。机制是澄清问题而不是测试,而且参与者能看到题目自带的单元测试。对比 TiCoder 理想用户(GPT-4-32k MBPP PassFail m=1 +14.43,m=5 +16.57;Output m=5 +18.66):方向一致,但真人在环的增幅更小,符合原文自己说的"oracle 是上界"。

**F5 标题数字:没有任何独立来源复现 45.97%/45.73%/38.43%,作者方也没有更正。**
- 官方代码仓 microsoft/TiCoder 的 TRANSPARENCY.md 第 41 行原样写着"an average absolute improvement of 45.97% in the pass@1 code generation accuracy for both datasets and across all LLMs within 5 user interactions"。旧仓 Smfakhoury/TiCoder-project 的 README 仍写 38.43%。两个仓库都没有勘误。以"TiCoder 45.97 erratum/correction/critique"检索,无结果。
- compute_metrics.py 只计算单次运行的 pass@k、pruned pass@k,没有"跨模型平均绝对提升"的汇总代码,无法据此确定标题数字的口径。
- 本席穷举复算 v2 Table IV(14 行全部解析):7 个模型的全部 127 个子集 × 10 个 m 列 × {绝对, 相对},看哪种组合能得到 45.97/45.73/38.43(容差 ±0.06)。只命中 6 个零散组合,例如"GPT-4-32k + GPT-4-turbo + code-davinci-002 + text-davinci-003 的 PassFail m=2 **相对**提升 = 45.95",没有一个对应有原则的口径(m=5、Output、绝对提升、全部或四个旧模型)。有原则的口径都与 R2 一致:全部 14 组 Output m=5 = 33.50 pp,旧模型 8 组 = 43.94 pp,PassFail m=5 = 26.33 pp,对话模型 6 组 Output m=5 = 19.58 pp。
- 结论:标题数字既不能从同文复现,也没有外部来源支撑,不能承重。

**F6 内部一致性(不是独立证据,附给 M 席参考):NASA-TLX 总分与分项只有两组对得上。** 按"心理需求 + 压力 + 节奏 + (20 − 信心) + 努力"(即 5 题 0–20 分加总为 0–100,信心反向计分)复算 Table III:A2 = 27.95(表中 28.00),A3 = 29.47(表中 29.52),两组都在舍入误差内;**A1 = 46.39,表中为 45.46,差 0.93**,超出舍入范围。v1 与 v2 的 Table III 数字相同,两版都没有说明。这使"45.46 → 28.00"中对照组的数值出现小的内部不一致(方向不受影响)。另:R2 K 镜头指出的 1/25 分母异常(0.84、0.64 不能写成 k/15),本席没有找到任何外部材料能解释。

## 二、结局

**X 席结局:用户研究(P14/P15)= 无独立测量;标题数字(P17)及大规模增益的外推(P16)= 独立矛盾(外推方向)。**
- 用户研究:找不到对同一干预的独立重做。唯一相邻的独立研究(Ferdowsi CHI 2024,n=17)方向一致但不显著,不能证实"0.40 → 0.84"的幅度,也不能证实"负荷普遍下降"(只有 1/2 任务显著)。
- 基准增益:独立团队复跑(VLP 2026,模拟 oracle 用户、BigCodeBench/QCE、2026 年模型)得到 TiCoder 增益 −5.2 到 +22.7 pp,6 格中 5 格 ≤ +3 pp,与"平均绝对提升 ~46 pp"以及原文对话模型的 13–20 pp 都相去甚远。独立的真人澄清研究(ClarifyGPT)在 MBPP 上为 +9.8 pp,低于 TiCoder 的 oracle 上界。
- 标题数字 45.97/45.73/38.43:没有任何外部复现,穷举也无法从同文表格得到;作者在官方仓库中继续沿用,没有更正。

搜索角度表:
| 角度 | 查询/来源 | 结果 |
|---|---|---|
| 1 TiCoder 用户研究的直接复现 | WebSearch "TiCoder replication user study…";S2 引用表 179 篇标题筛 | 无 |
| 2 施引文献复跑 TiCoder 作基线 | S2 引用表 → 抽查 8 篇全文 grep | **命中 VLP 2607.02333**(F3);其余只在相关工作中提及 |
| 3 相邻机制的独立用户研究(执行/示例辅助验证 AI 代码) | WebSearch "Validating AI-Generated Code with Live Programming";"user study generated test cases help developers verify…";"CHI user study input-output examples disambiguate…" | Ferdowsi CHI 2024(F2,方向一致,不显著);Tang et al. 眼动研究 2405.16081(n=28,没有测试干预,不适用) |
| 4 真人在环的意图澄清对 pass@1 的独立测量 | ClarifyGPT 2310.10996 全文 | +9.84 pp(GPT-4,MBPP-sanitized,真人,F4) |
| 5 测试入提示的独立测量(P18 相关) | Mathews & Nagappan TGen(R2 已取得) | 同向 +3~13 pp(不重复) |
| 6 标题数字的来源与更正 | microsoft/TiCoder TRANSPARENCY.md、compute_metrics.py;TiCoder-project README;WebSearch "TiCoder … erratum/45.97/38.43" | 45.97 沿用,无更正、无汇总脚本(F5) |
| 7 标题数字的口径反推 | 穷举 127 个子集 × 10 列 × 绝对/相对 | 无有原则的匹配(F5) |
| 8 同团队早期版本(非独立,用于口径追溯) | arXiv 2208.05950v2(没有用户研究,摘要 22.49%);ICSE 2024 海报(researchr 不可达) | 无新信息 |
| 9 示例消歧的跨领域旁证(正则合成) | UIST 2020 Zhang et al.;Vaithilingam/Pu/Glassman 2023 | 只有搜索摘要,主机不可达,**未作证据** |
| 10 二次转述扩散 | 8 篇施引全文 grep "45.9/38.4/professional developers" | 无第三方转引 |

证据分级建议(供成文):
- 0.40 → 0.84、45.46 → 28.00:**单源已核**(一手可回溯),没有独立测量;对照组 TLX 总分与分项有 0.93 的内部差,写法上只保留方向(正确判断率约翻倍、自报负荷下降、耗时不显著),并带上 n=15、每人每条件 1 题、作者为方法提出方。
- "在函数级基准上,oracle 用户确认测试能显著提高 pass@1":原文 Table IV 属**单源已核**(上界)。外推到更难或依赖库的任务属**方向存争**(VLP 独立复跑 −5~+3 pp 为主)。
- 45.97%/45.73%/38.43%:**弃用**(不可复现,也没有独立支撑)。
