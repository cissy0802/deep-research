# ORIGIN 线：原始锦标赛到底发生了什么

30 条论断，见 ORIGIN.json。1980a 全文（MIT ESP 公开 PDF 的 OCR 文本层）和 Science 1981 全文（JSTOR 扫描的课程副本）已逐字核对；**1980b 原文没拿到**（SAGE 付费墙），只有摘要和转引。

## 关键数字（一手已核）
- **第一届**：14 份参赛（16 人提交，3 国，5 个学科）+ RANDOM，共 15 条规则；每局固定 200 步；收益 3/5/0/1；循环赛跑 5 遍，共 120,000 步（1980a）。
- TFT 平均 **504.5**，亚军 Tideman & Chieruzzi **500.4**，只差约 4 分；季军 Nydegger 485.5。
- 前 8 名全是 nice，后 7 名（含 RANDOM）全不 nice；nice 规则得分在 472–504 之间，最好的非 nice 规则只有 401。
- TFT「only four lines long in FORTRAN」，是提交程序里最简单的一个。
- 排名主要由两个「造王者」DOWNING 和 GRAASKAMP 决定。
- **TIT FOR TWO TATS** 放进同样 15 条规则的环境里，平均 532 分，比 TFT 的 504 高。它就是寄给参赛者的示例程序，但没人提交。REVISED DOWNING（542）和 LOOK AHEAD（520）也都会赢。
- 收益改成 P=2 时，Tideman & Chieruzzi 夺冠，TFT 掉到第四（1980a 脚注 3）。
- **第二届**：62 份参赛，来自 6 国，加 RANDOM 共 63 条规则；大多数参赛者是计算机爱好者（Science 1981）。每步继续概率 w = .99654，每对打 5 局。
- Science 1981 的稳定性条件：w ≥ (T−R)/(T−P) 且 w ≥ (T−R)/(R−S)。代入 3/5/1/0 得 w ≥ 2/3。

## 流行说法核查
| 说法 | 结论 |
|---|---|
| TFT 只有 4 行代码 | **成立，但口径是 FORTRAN 4 行**。有课程讲义写成 5 行，是错的 |
| TFT 从不赢单个对手 | **成立**。一手实例：TFT 对 JOSS 236:241，5 局平均 225:230。Axelrod 2012：「could never do better than the player it was interacting with」 |
| 第一届 TFT 是无人预料的黑马 | **需修正**。参赛者收到过预赛报告，知道 TFT 在预赛得第二、在变体里得第一，很多人以它为基础去改 |
| TF2T 本可赢第一届 | 成立，但这是放进既定环境的反事实计算。第二届真参赛（Maynard Smith 提交，二手）只排第 24 |
| 第二届参赛者都想打败 TFT | **无一手依据**。一手只说他们拿到了第一届的分析，「draw lessons」 |
| 第二届平均 200 步 | **不对**。按 w 算，中位数≈200、期望≈289；实际用 5 个预抽长度，平均约 151 |
| 第一届 14 个参赛含 RANDOM / 14 位科学家 | **不对**。是 14 份 + RANDOM，16 个人 |
| TFT 是 ESS | Science 原文写的是「evolutionarily stable」，但只是不可被严格超越；书中改称 collectively stable。Boyd & Lorberbaum 1987 证明重复 PD 中没有纯策略是 ESS |
| 四性质 / 四建议 | 第 2 章 p.54：nice, retaliatory, forgiving, clear（二手引）。第 6 章：Don't be envious / Don't be the first to defect / Reciprocate both cooperation and defection / Don't be too clever（Wikiquote 二手）。这是两套不同表述。Science 1981 只列了三点（没有 clear） |
| TF2T 是 Axelrod 在 RAND 提出的（Wikipedia） | **错**。它是第一届的示例程序，Axelrod 当时在 Michigan |

## 来源之间的口径冲突
1. **生态模拟**：Science 1981 说 TFT「went to fixation」；1980b（转引 p.401）说到第 1000 代 TFT 占 14.5%，仍以每代 0.05% 增长；Binmore 说「a little more than 1/6」；Hoffmann 2000 说互惠合作者合计约 75%。
2. **Rapoport 第二届署名单位**：Science 写 IAS Vienna，书写 University of Toronto（书摘，二手）。
3. **第一届学科**：Science 漏掉了心理学，而 Rapoport 本人就在心理学系。
4. **第二届对局长度**：Science 写「expected probability of 200 moves」，1980b 写「expected median length」。
5. 第一届第 6 名 Stein & **Amnon** Rapoport 不是 Anatol。PLOS ONE 2015 批评论文的第一作者正是 Amnon Rapoport。

## Axelrod 自己的保留
- 1980a：「the results of a single tournament are not definitive」；结果依赖收益数值（脚注 3）。
- 2012 回顾：原赛没有选择层面的噪声，「I wish I had appreciated this basic flaw in simple reciprocity earlier」。

## 方法论批评
- Binmore 1998：TFT「not so very successful」；换参赛池就不稳健；核心结论 folk theorem 早已有之；Axelrod 列的性质里只有 retaliatory 是必要的。
- Rapoport, Seale & Colman 2015：两阶段赛制下 TFT 只赢 11%；按胜场数排名，TFT 排最后。
- Knight et al. 2025：精确结果无法复现；TFT 只在 63.3% 的种子下夺冠；亚军代码有变量未初始化的 bug。

## 没拿到的
- 1980b 全文：第二届 TFT 得分、6 个变体定义及「5/6」、14.5% 原句。
- 1984 书原文：archive.org 是借阅限制，Google Books API 配额为 0。
- APSR 1981 全文。
- Axelrod 的 umich 站点返回 403。

## 来源
- Axelrod 1980a, JCR 24(1):3-25 — https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- Axelrod 1980b 摘要 — https://ideas.repec.org/a/sae/jocore/v24y1980i3p379-403.html
- Axelrod & Hamilton 1981, Science 211:1390-96 — https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- Axelrod 2012, J. Theor. Biol. 299:21-24 — https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Axelrod-launching-2011.pdf
- Knight et al. 2025, arXiv:2510.15438 — https://arxiv.org/html/2510.15438v1
- Rapoport, Seale & Colman 2015, PLOS ONE — https://pmc.ncbi.nlm.nih.gov/articles/PMC4520619/
- Binmore 1998, JASSS 1(1) — https://jasss.soc.surrey.ac.uk/1/1/review1.html
- Hoffmann 2000, JASSS 3(2) — https://www.jasss.org/3/2/forum/1.html
- Axelrod-Python 文档 — https://axelrod.readthedocs.io/en/latest/_modules/axelrod/strategies/titfortat.html
- 二手：Wikiquote（Axelrod 1984）、Wikipedia（The Evolution of Cooperation）、Azhar 2005 CUNY 讲义、Tesfatsion 2003 讲义、egtheory 2015、IIT Kanpur 书摘页
