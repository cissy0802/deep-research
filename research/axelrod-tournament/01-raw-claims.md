# 01 Round 1 原始论断(5 线合并)


# 线 ORIGIN

## O01 (ORIGIN)
- 论断:第一届锦标赛有 14 份提交的参赛规则（来自 3 个国家、5 个学科，共 16 位提交者），另由主办方加入 RANDOM，总共 15 条规则进行循环赛。
- 原文:The fourteen submitted entries came from three countries and five disciplines. The Appendix lists the names a n d affiliations of the sixteen people who submitted these entries
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod, R. (1980a). Effective Choice in the Prisoner's Dilemma. Journal of Conflict Resolution 24(1): 3-25 · 1980-03 · 【研究】 · verbatim-checked
- 备注:引文来自扫描 PDF 的 OCR 文本层（有 OCR 噪声如 'a n d'），措辞已逐字核对。分母陷阱：'14 entries' 不含 RANDOM；'15 rules' 含 RANDOM（附录第十五名即 RANDOM；正文'just two of the fifteen rules'）。有二手源写错：Tesfatsion 2003 课堂笔记写 'Fourteen entries ... including RANDOM'；Rapoport, Seale & Colman 2015 写 'invited 14 scientists'——实际是 16 人提交 14 份。

## O02 (ORIGIN)
- 论断:第一届参赛者学科：经济学家、数学家、政治学家、心理学家和一名社会学家；多数招募自发表过博弈论/囚徒困境论文的人。
- 原文:the best of the fourteen entries from economists, mathematicians, political scientists, psychologists, and a sociologist.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, JCR 24(1) · 1980-03 · 【研究】 · verbatim-checked
- 备注:Axelrod & Hamilton 1981 Science 版本只写 'game theorists in economics, sociology, political science, and mathematics'，漏掉了心理学——而 TFT 提交者 Rapoport 本人就在 Toronto 心理学系。口径不一致，以 1980a 为准。

## O03 (ORIGIN)
- 论断:第一届署名参赛者（按名次）：Rapoport(TFT)、Tideman & Chieruzzi、Nydegger、Grofman、Shubik、Stein & Amnon Rapoport、Friedman、Davis、Graaskamp(本科生)、Downing、Feld、Joss、Tullock、一名匿名政治学研究生；第15名 RANDOM。
- 原文:Thirteenth Place with 300.5 points is an eighteen-line program entered by Gordon TULLOCK ... Fourteenth Place with 282.2 points is a 77-line program by a graduate student of political science whose dissertation is in game theory.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, Appendix 'The Decision Rules' · 1980-03 · 【研究】 · verbatim-checked
- 备注:Tullock 的规则是 Axelrod 邀请他把 Overcast & Tullock 1971 的想法具体化的，'out of scientific interest rather than an expectation that it would be a likely winner'；Downing 条目是 'based on an idea submitted by Leslie DOWNING'。注意第六名的 Amnon Rapoport（UNC 心理学系）不是 Anatol Rapoport——2015 年 PLOS ONE 批评论文的第一作者正是这位 Amnon Rapoport。

## O04 (ORIGIN)
- 论断:第一届规则：循环赛，每条规则与其他每条、与自身孪生体、与 RANDOM 各对局；每局恰好 200 步；收益 R=3, T=5, S=0, P=1；整个循环赛跑了 5 遍，共 120,000 步、240,000 次选择。
- 原文:Each game consisted of exactly 200 moves. The payoff matrix for each move awards both players 3 points for mutual cooperation, and 1 point for mutual defection. If one player defects while the other player cooperates, the defecting player receives 5 points and the cooperating player receives 0 points ... the entire round robin tournament was run five times to get a more stable estimate of the scores for each pair of players. In all, there were 120,000 moves, making for 240,000 separate choices.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, 'The Form of the Tournament' · 1980-03 · 【研究】 · verbatim-checked
- 备注:120,000 = 120 场对局 ×200 步 ×5 遍（15 条规则含自对局共 120 个无序对）。200 步是事先公布的固定长度——这正是第二届改成概率结束的原因（末局效应）。

## O05 (ORIGIN)
- 论断:TFT 第一届平均每局 504 分（附录精确值 504.5），第二名 Tideman & Chieruzzi 500.4——领先仅约 4 分（<1%）；第三 Nydegger 485.5。基准：全程互相合作 = 600，全程互相背叛 = 200。
- 原文:First Place with 504.5 points is TIT FOR TAT ... Second Place with 500.4 points is a program of 41 lines by T. Nicolas TIDEMAN and Paula CHIERUZZI ... Third Place with 485.5 points is a 23-line program by Rudy NYDEGGER
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, Appendix · 1980-03 · 【研究】 · verbatim-checked
- 备注:正文写 'averaged 504 points per game'（取整），附录写 504.5。'压倒性胜利'的叙事要小心：冠亚军差距很小。

## O06 (ORIGIN)
- 论断:'TFT 只有四行代码'在原文中成立，但口径是 FORTRAN 四行；且'最简单'是在提交的程序中——RANDOM 五行、JOSS 五行、DAVIS 六行。
- 原文:This rule is only four lines long in FORTRAN.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, Appendix · 1980-03 · 【研究】 · verbatim-checked
- 备注:正文说 'This simplest of all submitted programs'。有二手源写成'五行 Fortran'（Brooklyn CUNY 2005 课程讲义），属误传。另：1980a 同时说'neither the discipline of the author, the brevity of the program, nor its length accounts for a rule's relative success'——即简短本身不是成功原因（OCR 原文 brevity/length 并列）。

## O07 (ORIGIN)
- 论断:第一届前八名全部是 'nice'（不率先背叛，至少在最后几步之前），其余七名全都不 nice；nice 规则平均分 472–504，最好的非 nice 规则只有 401。
- 原文:Each of the top eight ranking entries are nice. None of the other entries are nice. There is even a substantial gap in the score between the nice entries and the others. The nice entries received tournament averages between 472 and 504, while the best of the entries that were not nice received only 401 points.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, 'Niceness' · 1980-03 · 【研究】 · verbatim-checked
- 备注:'nice' 的定义带限定：'if at least it will not be the first to defect before the last few moves (say before move 199)'——Tideman&Chieruzzi、Stein&Rapoport 在最后两步自动背叛仍算 nice。'bottom seven' 包含 RANDOM。

## O08 (ORIGIN)
- 论断:第一届排名主要由两个'造王者'（kingmaker）决定：DOWNING 和 GRAASKAMP；nice 规则对 RANDOM 的得分极差只有 157，对 DOWNING 达 443、对 GRAASKAMP 290。
- 原文:The range of scores achieved by the nice programs with RANDOM was only 157, compared t o a range of443 achieved with DOWNINGand 290 achieved with GRAASKAMP.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, 'Effectiveness with the Kingmaker' · 1980-03 · 【研究】 · verbatim-checked
- 备注:这一点直接支持'结果依赖参赛池'的批评：排名几乎由两条本身表现不佳的规则决定。

## O09 (ORIGIN)
- 论断:TFT 在单场对局中会输给对手：第一届 TFT 对 JOSS 的示例对局 TFT 236 : JOSS 241；五局平均 TFT 225 : JOSS 230。
- 原文:The final score of this game was 236 for TIT FOR TAT and 241 for JOSS. Notice that while JOSS did a little better than TIT FOR TAT, both did poorly. ... In the five games between them, the average scores aere 225 for TIT FOR TAT and 230 for JOSS.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, Table 3 及脚注 2 · 1980-03 · 【研究】 · verbatim-checked
- 备注:这是'TFT 从不赢任何单个对手'的一手实例（OCR 'aere'=were）。注意 JOSS 最终排第 12（304 分）——赢了 TFT 的人整体却很差。

## O10 (ORIGIN)
- 论断:'TFT 不可能在单个对局中得分超过对手'：Axelrod 本人 2011/2012 回顾中明确如此表述；Rapoport, Seale & Colman 2015 用第一届数据按'胜场数'重新排名，TFT 一场未赢、排最后（第15）。
- 原文:The most fascinating point was that TIT FOR TAT won the tournaments even though it could never do better than the player it was interacting with. Instead it won by its success at eliciting cooperation.
- URL:https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Axelrod-launching-2011.pdf
- 来源:Axelrod, R. Launching 'The Evolution of Cooperation'. Journal of Theoretical Biology 299 (2012) 21-24 (online 2011) · 2011-04 · 【研究】 · verbatim-checked
- 备注:严格表述：确定性 TFT 对任何对手的得分 ≤ 对手（最多落后一次 T−S=5 分），可以平局但不能赢。PLOS ONE 2015 原句 'TFT did not score even a single win' 及 'can never achieve a positive point difference'（WebFetch 摘录，未逐字对 PDF）。Wikipedia 引 1984 书 p.130 'won, not by doing better than the other player, but by eliciting cooperation'（二手）。

## O11 (ORIGIN)
- 论断:TIT FOR TWO TATS（只在对手连续两次背叛后才背叛）若参赛将赢得第一届：在 15 条规则的环境中平均 532 分（TFT 504）；它恰恰是寄给所有潜在参赛者的示例程序，但无人提交。同样'会赢'的还有 REVISED DOWNING（542）和预赛冠军 LOOK AHEAD（520）。
- 原文:The sample program sent to prospective contestants to show them how t o make a submission would in fact have won the tournament if anyone had simply clipped it and mailed it in! But no one did. ... In the environment of the 15 rules of the tournament, REVISED DOWNING averages 542 points. This compares t o T I T FOR TAT which won with 504 points. TIT FOR TWO TATS averages 532 in the same environment. and LOOK AHEAD averages 520 points.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, Surprise (6) 及脚注 5 · 1980-03 · 【研究】 · verbatim-checked
- 备注:口径：这是'把它放进既定 15 条规则的环境'的反事实计算，不是重跑（加入它不会改变其他参赛者的提交，但 Axelrod 在脚注3自己承认若条件不同参赛者会提交不同程序）。三个都比 TFT 好，Axelrod 自己据此警告'against the facile belief than an eye for an eye is necessarily the best strategy'。Wikipedia《Tit for tat》称 TF2T 是 Axelrod 'during his second round of computer simulations at RAND' 提出——与原文不符（是第一届的示例程序，Axelrod 在 Michigan）。

## O12 (ORIGIN)
- 论断:第一届参赛者事先就知道 TFT 很强：他们收到了预赛报告（TFT 在预赛得第二、在其变体中得第一），许多人以 TFT 为基础试图改进它。
- 原文:In a preliminary tournament, TIT FOR TAT scored second place, and in a variant of that preliminary tournament, TIT FOR TAT won first place. All of these properties were known to most of the people designing programs for the Computer Prisoner's Dilemma Tourna- ment, because they were sent copies of the description of a preliminary tournament. And not surprisingly, many of them used the TIT FOR TAT principle and tried to improve upon it.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, 'The Winner' · 1980-03 · 【研究】 · verbatim-checked
- 备注:这让'第一届 TFT 是出人意料的黑马'的叙事需要修正：它在预赛中已有表现，参赛者知情；'惊讶'在于复杂改进版全都不如它。

## O13 (ORIGIN)
- 论断:收益矩阵的具体数值会影响第一届结果：若 P 从 1 改为 2，Tideman & Chieruzzi 将第一，TFT 降至第四。
- 原文:if P is changed from I to 2, then TIDEMAN AND CHIERUZZI would have come in first, followed by STEIN AND RAPOPORT, FRIEDhlAN. and TIT FOR TAT. Of course, the entrants knew the actual payoff matrix.
- URL:https://esp.mit.edu/download/2dd80247-be60-4e73-b49d-91b5b6988ff0/S12850_axelrod_1980.pdf
- 来源:Axelrod 1980a, 脚注 3 · 1980-03 · 【研究】 · verbatim-checked
- 备注:Axelrod 自己的 caveat，埋在脚注里。可作为'方法论批评并非事后才有'的证据。同文结尾：'the results of a single tournament are not definitive'。

## O14 (ORIGIN)
- 论断:第二届有 62 份参赛（来自 6 个国家），加 RANDOM 共 63 条规则；多数参赛者是计算机爱好者，也有进化生物学、物理学、计算机科学教授及第一届的五个学科。
- 原文:This time there were 62 entries from six countries (23). Most of the contestants were computer hobbyists, but there were also professors of evolutionary biology, physics, and computer science, as well as the five disciplines represented in the first round.
- URL:https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- 来源:Axelrod, R. & Hamilton, W. D. (1981). The Evolution of Cooperation. Science 211(4489): 1390-1396 (JSTOR scan, course copy) · 1981-03 · 【研究】 · verbatim-checked
- 备注:1980b 原文未能取得（SAGE 付费墙）；1980b 摘要（IDEAS/RePEc）写 'The 62 entrants were able to draw lessons from the results of the first round'。63 = 62+RANDOM（Rapoport, Seale & Colman 2015: '63 programs (including RANDOM)'；Axelrod 2012 回顾也写 'the 63 rules of the second round'）。课程讲义转述书中国家为 US, Canada, Great Britain, Norway, Switzerland, New Zealand，并称最年轻者为十岁计算机爱好者（二手，未核原书）。

## O15 (ORIGIN)
- 论断:第二届参赛者都拿到了第一届的详细分析结果（包括 TIT FOR TWO TATS 等'本可获胜'的补充规则），而且彼此知道对方也知道。
- 原文:The 62 entrants were able to draw lessons from the results of the first round and were able to design their entries to take these lessons into account.
- URL:https://ideas.repec.org/a/sae/jocore/v24y1980i3p379-403.html
- 来源:Axelrod, R. (1980b). More Effective Choice in the Prisoner's Dilemma. JCR 24(3): 379-403 — abstract · 1980-09 · 【研究】 · verbatim-checked
- 备注:引文仅为摘要。'were all given the detailed analysis of the first round' 及包含补充规则的细节见 1984 书第2章（经 IIT Kanpur 书摘页与 Brooklyn CUNY 讲义二手转述，未核原书）。Science 1981：'The results of the first round were then circulated and entries for a second round were solicited.' 注意：知情 ≠ '所有人都试图打败 TFT'——没有一手文本支持后者；书中描述的是参赛者从不同'教训'出发（有人更宽容如 TF2T，有人如 TESTER 去剥削宽容者）。

## O16 (ORIGIN)
- 论断:第二届改为概率结束：每步后结束概率 0.00346（继续概率 w = .99654），设定目的是使对局长度中位数为 200 步；每对仍对局 5 次。
- 原文:In the second round, the length of the games was uncertain, with an expected probability of 200 moves. This was achieved by setting the probability that a given move would not be the last at w = .99654. As in the first round, each pair was matched in five games (24).
- URL:https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- 来源:Axelrod & Hamilton 1981 Science, note 23 · 1981-03 · 【研究】 · verbatim-checked
- 备注:口径冲突：Science 写 'expected probability of 200 moves'（措辞含糊，像是期望值）；Knight et al. 2025 引 1980b 原文为 'This parameter was chosen so that the expected median length of a game would be 200 moves'。数学上 w=.99654 → 中位数 ln0.5/ln w ≈ 200.0，期望长度 1/(1−w) ≈ 289。所以'平均 200 步'是错的，'中位数 200 步'才对。

## O17 (ORIGIN)
- 论断:第二届实际并未每局独立随机抽长度：Axelrod 事先抽了 5 个对局长度用于所有配对；1980b 只列出 63、77、151、308 四个（第五个据报告平均值 151 推算为 156）——实际平均长度约 151，短于 200。
- 原文:the five games for each pair of players would be of lengths 63, 77, 151, and 308
- URL:https://arxiv.org/html/2510.15438v1
- 来源:Knight, V. et al. (2025). Reviving, reproducing, and revisiting Axelrod's second tournament. arXiv:2510.15438 (quoting Axelrod 1980b) · 2025-10 · 【研究】 · secondhand
- 备注:引文是 Knight 等转引 1980b，经 WebFetch 摘录，未对 1980b 原件核对。'156' 是 Knight 等推断值，非 Axelrod 所写。

## O18 (ORIGIN)
- 论断:第二届 TFT 再次获胜，由 Anatol Rapoport 再次提交；Science 1981 将其单位写为维也纳高等研究院（IAS Vienna），而书中写作 University of Toronto——两处一手文本的单位不一致。
- 原文:TIT FOR TAT was again submitted by the winner of the first round, Professor Anatol Rapoport of the Institute for Advanced Study (Vienna). It won again.
- URL:https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- 来源:Axelrod & Hamilton 1981 Science · 1981-03 · 【研究】 · verbatim-checked
- 备注:1984 书版本（经 IIT Kanpur 书摘页二手）：'TIT FOR TAT was again sent in by the winner of the first round, Anatol Rapoport of the University of Toronto. Again it won.' Rapoport 1979–80 前后任维也纳 IHS 所长，两者可能都'对'只是时点不同；文章中最好不写单位或注明。egtheory 2015 博客称 Rapoport 是第二届'唯一（再）提交 TFT 的人'——未找到一手文本支持，存疑。

## O19 (ORIGIN)
- 论断:第二届前列：1 TFT (Rapoport)、2 Danny C. Champion、3 Otto Borufsen、4 Rob Cave、5 William Adams……；TIT FOR TWO TATS 由 John Maynard Smith 提交，排第 24。
- 原文:Submitted to Axelrod's second tournament by John Maynard Smith; it came in 24th in that tournament.
- URL:https://axelrod.readthedocs.io/en/latest/_modules/axelrod/strategies/titfortat.html
- 来源:Axelrod-Python library, TitFor2Tats docstring; Knight et al. 2025 Table 1 · 2025 · 【二手转述】 · secondhand
- 备注:排名表来自 Knight et al. 2025（基于 Axelrod 公布的 Fortran 源码代号 k92r=TFT, k61r=Champion, k90r=Maynard Smith）。'24th' 应出自 1984 书第2章，未能核对原书。这是'TF2T 本能赢第一届'的反讽对照：真正参赛时在更具剥削性的环境里落到第 24。

## O20 (ORIGIN)
- 论断:第二届 TFT 的成功被归于三点：从不率先背叛、可被激怒而报复、报复一次后即宽恕；书中总结为四性质：nice, retaliatory, forgiving, clear。
- 原文:the analysis of the 3 million choices which were made in the second round identified the impressive robustness of TIT FOR TAT as dependent on three features: it was never the first to defect, it was provocable into retaliation by a defection of the other, and it was forgiving after just one act of retaliation (24).
- URL:https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- 来源:Axelrod & Hamilton 1981 Science · 1981-03 · 【研究】 · verbatim-checked
- 备注:1984 书 p.54（经 Rapoport, Seale & Colman 2015 引用）：'What accounts for TIT FOR TAT's robust success is its combination of being nice, retaliatory, forgiving, and clear.' —— 第四个性质 clear 在 1981 Science 的三点里没有，是书中才加的。1980b 摘要用 'provocable' 而非 'retaliatory'。'3 million choices' 与书中'over a million moves'（二手讲义）一致：每步两人各一个选择。

## O21 (ORIGIN)
- 论断:1984 书第6章给出的四条建议原文措辞：Don't be envious. / Don't be the first to defect. / Reciprocate both cooperation and defection. / Don't be too clever.
- 原文:Don't be envious. ... Don't be the first to defect. ... Reciprocate both cooperation and defection. ... Don't be too clever.
- URL:https://en.wikiquote.org/wiki/Robert_Axelrod
- 来源:Axelrod 1984, The Evolution of Cooperation, ch.6 'How to Choose Effectively'（经 Wikiquote 转录） · 1984 · 【二手转述】 · secondhand
- 备注:未能取得原书文本（archive.org 为借阅限制；Google Books API 配额为 0）。Wikipedia 给出页码 'don't be envious' pp.110–113, 'don't be too clever' pp.120+。注意'四性质'(nice/retaliatory/forgiving/clear, 第2章 p.54) 与'四建议'(第6章) 是两套不同表述，不能混为一谈；书中还有第7–9章其他建议。

## O22 (ORIGIN)
- 论断:第二届中 nice 与否和成绩高度相关：前 15 名中除一个外都是 nice（那一个排第8）。
- 原文:Of the all top fifteen rules, all but one were nice (and that one ranked the eighth.)
- URL:https://www.sci.brooklyn.cuny.edu/~sklar/teaching/f05/alife/notes/azhar-ipd-Oct19th.pdf
- 来源:Azhar, M. Q. (2005) 课堂讲义 'The Success of TIT FOR TAT in Computer Tournaments'（转述 Axelrod 1984 第2章） · 2005 · 【二手转述】 · secondhand
- 备注:学生讲义转述原书，未核 1980b/原书原文。核查方需找原书第2章。同一讲义把 TFT 写成'only five lines of Fortan'——与 1980a 的四行矛盾，说明该讲义可靠性有限。

## O23 (ORIGIN)
- 论断:1980b 的'代表性'假设锦标赛：构造 6 个变体（每个让某一类规则大量过量出现），TFT 赢了其中 5 个、第 6 个排第二。
- 原文:The results were that TIT FOR TAT won five of the six variants of the tournaments and came in second in the sixth.
- URL:https://www.sci.brooklyn.cuny.edu/~sklar/teaching/f05/alife/notes/azhar-ipd-Oct19th.pdf
- 来源:Azhar 2005 讲义（转述 Axelrod 1984/1980b）；egtheory 博客 2015 同说 · 2005 · 【二手转述】 · secondhand
- 备注:1980b 摘要一手确认存在此分析：'An analysis of hypothetical alternative tournaments demonstrates the robustness of the results.' 但 '5/6' 数字只有二手来源（egtheory: 'TIT-for-TAT still came out on top 5 out of the 6 times, coming in 2nd in the last variant'）。这些变体仍由同 63 条规则加权构成，并非真正不同的参赛池——这是 Binmore 'why restrict ourselves to Axelrod's 63 strategies?' 批评的靶子。

## O24 (ORIGIN)
- 论断:生态（未来世代）模拟：以第二届 63 条规则为初始，每代各规则份额按上一代得分比例更新；Science 1981 称长期 TFT 取代其他规则、走向固定（fixation）；但 1980b 原文报告的是到第1000代 TFT 占 14.5% 且仍以每代 0.05% 增长。
- 原文:The results showed that, as the less successful rules were displaced, TIT FOR TAT continued to do well with the rules which initially scored near the top. In the long run, TIT FOR TAT displaced all the other rules and went to fixation (24).
- URL:https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- 来源:Axelrod & Hamilton 1981 Science · 1981-03 · 【研究】 · verbatim-checked
- 备注:关键口径冲突！1980b p.401（经检索摘要转引 PS: Political Science & Politics 的 Axelrod 传记）：'By the 1000th generation, it was 14.5% of the whole population . . . and was still growing at .05% per generation which was a faster rate than any other rule'——未能直接核对（传记 PDF 走代理被拦，1980b 付费）。Binmore 1998：TFT 'controls only a little more than 1/6 of the population'，'Actually a mixture of strategies survives'。Hoffmann 2000 JASSS 称第1000代'reciprocating cooperators accounted for about 75%'。即：1000 代时 TFT 只是最大份额（约 1/7–1/6），'went to fixation' 是 Science 对更长期的外推表述。

## O25 (ORIGIN)
- 论断:Axelrod & Hamilton 1981 的稳定性主张：当相遇继续概率 w 足够大时 TFT '进化稳定'，充要条件为 w ≥ (T−R)/(T−P) 且 w ≥ (T−R)/(R−S)；论证方法是只需检查 ALL D 和 DC 交替两种策略能否入侵。
- 原文:neither of these two strategies (and hence no strategy at all) can invade TIT FOR TAT if and only if both w > (T - R)/(T - P) and w > (T - R)/(R - S) (1) This demonstrates that TIT FOR TAT is evolutionarily stable if and only if the interactions between the individuals have a sufficiently large probability of continuing (19).
- URL:https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- 来源:Axelrod & Hamilton 1981 Science, 'Stability' · 1981-03 · 【研究】 · verbatim-checked
- 备注:OCR 把不等号印成 '>' 和 '-'，原刊应为 ≥（第二个式子 OCR 损坏，需看扫描图核对）。代入 3/5/1/0：两个阈值分别 1/2 和 2/3，所以 w ≥ 2/3。Science 用的是'evolutionarily stable'，但'不可被入侵'只指不被严格超越（Nash 意义）；ALL C 等 nice 策略对 TFT 是中性突变体，TFT 不是 Maynard Smith 严格意义的 ESS。1984 书改称 'collectively stable'（Proposition 2：'TIT FOR TAT is collectively stable if and only if, w is large enough'，经 Wikiquote）。Boyd & Lorberbaum 1987 Nature 327:58–59：'No pure strategy is evolutionarily stable in the repeated Prisoner's Dilemma game'。另：Science 原文说 ALL D 'is evolutionarily stable no matter what is the probability of interaction continuing'。

## O26 (ORIGIN)
- 论断:Science 1981 给出的初始可行性机制：亲缘关系，或聚簇（cluster）——当 p 和 w 足够大时，一小簇 TFT 可在几乎全是 ALL D 的环境中立足；且 nice 的稳定策略不能被任何簇入侵（'棘轮'）。
- 原文:When p and w are large enough, a cluster of TIT FOR TAT individuals can then become initially viable in an environment composed overwhelmingly of ALL D (19).
- URL:https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
- 来源:Axelrod & Hamilton 1981 Science, 'Initial Viability' · 1981-03 · 【研究】 · verbatim-checked
- 备注:OCR 两栏交错，引文已按语义复原。'The gear wheels of social evolution have a ratchet.' 也在同段。

## O27 (ORIGIN)
- 论断:Axelrod 自己承认原锦标赛没有'噪声'（选择被误执行/误感知），只在策略层面放了 RANDOM；他称这是简单互惠的'basic flaw'，并希望早点意识到。
- 原文:I wish I had appreciated this basic flaw in simple reciprocity earlier. I did not entirely ignore the problem of noise, but I had introduced it in the tournament at the level of the strategy rather than at the level of the choice.
- URL:https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Axelrod-launching-2011.pdf
- 来源:Axelrod 2012, J. Theor. Biol. 299: 21-24 · 2011-04 · 【研究】 · verbatim-checked
- 备注:与 NOISE 线交叉。Axelrod 引 Molander 1985：小噪声下两 TFT 的平均收益等同两个 RANDOM。

## O28 (ORIGIN)
- 论断:Binmore（1998 书评）批评：TFT 在 Axelrod 模拟中'没那么成功'，其有限成功在初始参赛池变化时不稳健；核心结论（重复博弈可支撑合作）在 Axelrod 之前已为人熟知超过 25 年（folk theorem）；Axelrod 列出的性质中只有'retaliatory'是必要的。
- 原文:On examination, it turns out that TIT-FOR-TAT was not so very successful in Axelrod's simulation. Nor is the limited success it does enjoy robust when the initial population of entries is varied.
- URL:https://jasss.soc.surrey.ac.uk/1/1/review1.html
- 来源:Binmore, K. (1998). Review of Axelrod, The Complexity of Cooperation. JASSS 1(1) · 1998-01 · 【研究】 · paraphrase
- 备注:引文由 WebFetch 摘录，判断为逐字，但未做第二次字节级核对。其他句：'But this fact had been well known for more than a quarter of a century before Axelrod began to write on the subject.'；'All that is then left on Axelrod's list is the requirement that a successful strategy be retaliatory.'

## O29 (ORIGIN)
- 论断:Rapoport, Seale & Colman (2015, PLOS ONE) 用第一届 15 条规则做两阶段（3组×5）循环赛的全部 756,756 种分组：TFT 只赢 11.0%，Tideman&Chieruzzi 30.0%，Stein&Rapoport 24.8%；结论是 TFT 的有效性取决于赛制、成功标准和收益数值。
- 原文:is contingent on the design of the tournament, the criterion used to determine success, and the particular values
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC4520619/
- 来源:Rapoport, Amnon; Seale, D. A.; Colman, A. M. (2015). Is Tit-for-Tat the Answer? On the Conclusions Drawn from Axelrod's Tournaments. PLOS ONE 10(7): e0134128 · 2015-07 · 【研究】 · paraphrase
- 备注:数字经 WebFetch 摘录，未逐字对 PDF。注意作者 Amnon Rapoport 本人是第一届第6名 STEIN AND RAPOPORT 的共同提交者——有利益相关可提，但其重分析对象就是 1980a 公开数据。

## O30 (ORIGIN)
- 论断:Knight 等 2025 用 Axelrod 公开的 Fortran 源码重跑第二届 25,000 次：TFT 仍是原排名/复现排名第一，但只在 63.3% 的随机种子下夺冠；Axelrod 报告的精确结果无法复现；第二名 Champion 的代码有变量未初始化的 bug（复现排名第12）。
- 原文:Although Axelrod's reported results are impossible to replicate, we are able to recover the main conclusions.
- URL:https://arxiv.org/html/2510.15438v1
- 来源:Knight et al. 2025, arXiv:2510.15438 · 2025-10 · 【研究】 · paraphrase
- 备注:WebFetch 摘录；预印本未经同行评审。'It is unclear whether this bug affected the tournament results reported in 1980.' 与 EVIDENCE/现代复现线交叉。


### 交叉口径问题
- 1980b 原文（JCR 24(3):379-403）未能取得：TFT 第二届具体得分、'nice'在第二届的精确统计、6 个代表性变体的定义与 5/6 结果、生态模拟 14.5%/0.05% 的原句（p.401）都只有二手转引。核查方若有 SAGE/JSTOR 访问请优先核这些。
- Science 1981 说生态模拟中 TFT 'went to fixation'；1980b（转引）说第1000代仅 14.5% 且仍在增长；Binmore 说'略多于 1/6'；Hoffmann 说互惠合作者合计约 75%。四个数字口径不同（TFT 单一规则 vs 一类规则；1000代 vs 极限），文章必须注明是哪一个。
- 第二届对局长度：'平均 200 步'（Science 措辞）vs '中位数 200 步'（1980b，经转引）vs 实际 5 个预抽长度平均约 151。文章应写'设计中位数 200'。
- Rapoport 第二届署名单位：Science 'Institute for Advanced Study (Vienna)' vs 1984 书 'University of Toronto'（书摘二手）。
- 第一届'14 个参赛'是否含 RANDOM：一手明确不含（14+RANDOM=15）；部分二手（Tesfatsion 2003）写成含 RANDOM；PLOS 2015 写成'14 scientists'（实为16人）。
- Science 1981 稳定性不等式 OCR 损坏：需看扫描原图确认是 ≥ 还是 >；以及 Science 用'evolutionarily stable'与书中'collectively stable'的术语差异及其严格性（Selten & Hammerstein 1984; Boyd & Lorberbaum 1987）。
- TF2T 第二届'第24名、Maynard Smith 提交'只见于 Axelrod-Python 文档，需对书第2章原文。
- 'Rapoport 是第二届唯一提交 TFT 的人'（egtheory 博客）无一手依据。
- '第二届参赛者都想打败 TFT'无一手依据：一手只说他们拿到第一届分析并'draw lessons'；书中描述的策略方向各异。

# 线 NOISE

## N01 (NOISE)
- 论断:Axelrod & Hamilton (1981) state TFT is 'evolutionarily stable' iff the continuation probability w is large enough: w >= (T-R)/(T-P) and w >= (T-R)/(R-S). Their stability test is 'cannot be invaded by a rare mutant', checked against ALL D and alternation of D and C.
- 原文:neither of these two strategies (and hence no strategy at all) can invade TIT FOR TAT if and only if both w ≥ (T - R)/(T - P) and w ≥ (T - R)/(R - S) ... This demonstrates that TIT FOR TAT is evolutionarily stable if and only if the interactions between the individuals have a sufficiently large probability of continuing
- URL:https://public.websites.umich.edu/~axe/research/Axelrod%20and%20Hamilton%20EC%201981.pdf
- 来源:Axelrod & Hamilton, The Evolution of Cooperation, Science 211:1390-1396 · 1981 · 【研究】 · verbatim-checked
- 备注:OCR'd JSTOR scan on Axelrod's own site; the '≥' sign is OCR'd as '2'. The definition the paper uses is 'cannot be invaded by a rare mutant adopting a different strategy', where invading means doing strictly better. That is weaker than Maynard Smith's ESS second condition, so a neutral mutant such as ALLC is not ruled out. The 'collective stability' wording comes from Axelrod 1981 APSR (see N02).

## N02 (NOISE)
- 论断:Axelrod's 1981 APSR paper frames the result as necessary and sufficient conditions for a strategy to be 'collectively stable' and for 'no strategy can do any better than the population average' against TFT. This is a no-strict-improvement (Nash-type) condition, not Maynard Smith's ESS.
- 原文:(1) the conditions under which no strategy can do any better than the population average if the others are using the reciprocal cooperation strategy of TIT FOR TAT, (2) the necessary and sufficient conditions for a strategy to be collectively stable
- URL:https://econpapers.repec.org/RePEc:cup:apsrev:v:75:y:1981:i:02:p:306-318_17
- 来源:Axelrod, The Emergence of Cooperation among Egoists, APSR 75(2):306-318 (abstract) · 1981 · 【研究】 · verbatim-checked
- 备注:Abstract only. The formal definition text from APSR or the 1984 book was not reached. Bendor & Swistak 1995 (N06) is the primary-literature source for 'stable in a weaker sense'.

## N03 (NOISE)
- 论断:Boyd & Lorberbaum (1987, Nature) argue that no pure strategy can be evolutionarily stable in the repeated PD, and that this casts doubt on several of Axelrod's conclusions.
- 原文:In this paper, however, we argue that no pure strategy can be evolutionarily stable in this game. This fact casts doubt on several of Axelrod's conclusions about the evolution of reciprocity.
- URL:https://www.nature.com/articles/327058a0
- 来源:Boyd & Lorberbaum, No pure strategy is evolutionarily stable in the repeated Prisoner's Dilemma game, Nature 327:58-59 · 1987 · 【研究】 · verbatim-checked
- 备注:Opening paragraph from the Nature page. The body was not reached. The often-cited mechanism (TFT is invaded by a mix of e.g. TF2T and STFT when w is large) is NOT verified from primary text. Conditions: no errors, w high enough that many strategies are best replies.

## N04 (NOISE)
- 论断:Boyd (1989) showed that if errors always occur with some probability, a pure strategy CAN be evolutionarily stable, provided it is a 'strong perfect equilibrium' against itself. Both ALLD and a modified TFT qualify.
- 原文:if there is always some probability that individuals will make a mistake, then a pure strategy can be evolutionarily stable provided that it is "strong perfect equilibria" against itself ... I show that both unconditional defection and a modified version of tit-for-tat have this property.
- URL:https://pubmed.ncbi.nlm.nih.gov/2779259/
- 来源:Boyd, Mistakes allow evolutionary stability in the repeated prisoner's dilemma game, J Theor Biol 136:47-56 · 1989 · 【研究】 · verbatim-checked
- 备注:Wu & Axelrod 1995 cite Boyd 1989, along with Sugden 1986, as the origin of contrition. The 'modified TFT' is the contrite-style TFT. Plain TFT is not on the list.

## N05 (NOISE)
- 论断:Farrell & Ware (1989) extended Boyd & Lorberbaum's result to finite mixtures of strategies.
- 原文:
- URL:https://portal.mardi4nfdi.de/wiki/Publication:1823196
- 来源:Farrell & Ware, Evolutionary stability in the repeated prisoner's dilemma, Theor Pop Biol 36:161-168 · 1989 · 【二手转述】 · secondhand
- 备注:Abstract not reachable (Elsevier elided). Secondary descriptions found through search: Bendor & Swistak say Farrell & Ware generalized the result to mixed strategies and conclude ESS is 'too strong'; Linster says any ESS mixture must make every finite history occur with positive probability. Treat as unverified.

## N06 (NOISE)
- 论断:Bendor & Swistak (1995, PNAS) reconcile Axelrod-Hamilton with Boyd-Lorberbaum. Under the attainable (weaker) stability concept, the IPD has 'too many' stable strategies, so stability alone does not discriminate. Stable strategies differ in how large an invasion they resist, and TFT-like conditional cooperators are the most robust.
- 原文:We first show that the IPD has "too many" such strategies, so that being stable does not discriminate among behavioral rules. Stable strategies differ, however, on a property that is crucial for their evolutionary survival--the size of the invasion they can resist. ... Conditionally cooperative strategies such as tit for tat are the most robust.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC42214/
- 来源:Bendor & Swistak, Types of evolutionary stability and the problem of cooperation, PNAS 92:3596-3600 · 1995 · 【研究】 · verbatim-checked
- 备注:A pro-TFT counterpoint. Its robustness claim is about the noiseless game with a sufficiently long shadow of the future, so it is not a claim about noise.

## N07 (NOISE)
- 论断:Selten & Hammerstein (1984, BBS commentary) are cited alongside Boyd & Lorberbaum for the point that TFT is not evolutionarily stable: without noise, ALLC earns the same as TFT and can drift in.
- 原文:Imagine a mixed population of players using TFT and players using the strategy 'always-cooperate' (ALLC). In the absence of noise, both strategies have the same average payoff. The frequency (=relative abundance) of ALLC can increase by random drift. This means TFT is not evolutionarily stable ( Boyd and Lorberbaum, 1987 ; Selten and Hammerstein, 1984 ).
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC2460568/
- 来源:Imhof, Fudenberg & Nowak, Tit-for-tat or win-stay, lose-shift? J Theor Biol 247:574-580 · 2007 · 【二手转述】 · secondhand
- 备注:Selten & Hammerstein, 'Gaps in Harley's argument on evolutionarily stable learning rules and in the logic of "tit for tat"', BBS 7:115-116. The text itself was NOT reached. The attribution of the 'mistake causes alternating retaliation' argument to S&H specifically is unverified; Nowak 2006 cites S&H (ref 16) for the trembling-hands decline of TFT (see N09).

## N08 (NOISE)
- 论断:The echo: if one of two TFT players defects by mistake, the pair falls into alternating C/D. In the infinitely repeated game with noise, TFT vs TFT averages only (R+S+T+P)/4 per round.
- 原文:If two TFT players interact with each other and one defects by mistake, then the other one will retaliate, which in turn leads to a sequence of alternating moves of cooperation and defection. In the presence of noise, in an infinitely repeated game, the expected payoff per round for TFT versus TFT is only ( R + S + T + P )/4.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC2460568/
- 来源:Imhof, Fudenberg & Nowak 2007, J Theor Biol · 2007 · 【研究】 · verbatim-checked
- 备注:(R+S+T+P)/4 is the long-run average under any small positive error rate with no discounting (the limit ε→0 of the ergodic average). With T=5,R=3,P=1,S=0 that is 2.25 instead of 3.

## N09 (NOISE)
- 论断:Nowak's 2006 Science review calls errors ('trembling hands' or 'fuzzy minds') the 'Achilles heel' of TFT, citing Fudenberg & Maskin 1990 and Selten & Hammerstein 1984. It describes a succession: TFT replaced by GTFT, then by WSLS. TFT is a catalyst where nearly everyone defects, but WSLS better maintains cooperation once it is established.
- 原文:if there are erroneous moves, caused by 'trembling hands' or 'fuzzy minds', then the performance of tit-for-tat declines ( 15 , 16 ). Tit-for-tat cannot correct mistakes, because an accidental defection leads to a long sequence of retaliation. ... Tit-for-tat is an efficient catalyst of cooperation in a society where nearly everybody is a defector, but once cooperation is established win-stay, lose-shift is better able to maintain it.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3279745/
- 来源:Nowak, Five rules for the evolution of cooperation, Science 314:1560-1563 (author manuscript) · 2006 · 【研究】 · verbatim-checked
- 备注:Refs 15 = Fudenberg & Maskin AER 1990; 16 = Selten & Hammerstein BBS 1984; 17 = Nowak & Sigmund 1992; 18 = Nowak & Sigmund 1993.

## N10 (NOISE)
- 论断:Molander (1985): TFT's performance in the iterated PD deteriorates drastically at arbitrarily low noise levels. Adding some unconditional generosity remedies this without exposure to exploitation.
- 原文:The tit-for-tat strategy in iterated prisoners' dilemma games is examined in the presence of disturbances. It is shown that performance deteriorates drastically at arbitrarily low noise levels. The situation may be remedied by introducing some unconditional generosity. This may be done without exposing oneself to the risk of exploitation by the other party.
- URL:https://econpapers.repec.org/RePEc:sae:jocore:v:29:y:1985:i:4:p:611-618
- 来源:Molander, The Optimal Level of Generosity in a Selfish, Uncertain Environment, JCR 29(4):611-618 · 1985 · 【研究】 · verbatim-checked
- 备注:Abstract only; the full text (SAGE) was not reached. Molander's own formula for the optimal generosity level was NOT seen in primary text (see N12 for the formula as stated by Hilbe et al. 2018, who cite Molander for it).

## N11 (NOISE)
- 论断:As reported by Wu & Axelrod, Molander showed that with any amount of noise, two TFT players in the long run average the same payoffs as two RANDOM players.
- 原文:Molander (1985) has shown that in the presence of any amount of noise, two Tit for Tat (TFT) players will in the long run average the same payoffs as two interacting RANDOM players.
- URL:https://public.websites.umich.edu/~axe/research/How_to_Cope.pdf
- 来源:Wu & Axelrod, How to Cope with Noise in the Iterated Prisoner's Dilemma (author version, July 1994), JCR 39:183-189 · 1995 · 【二手转述】 · verbatim-checked
- 备注:Verbatim from Wu & Axelrod, but secondhand about Molander's result. This is consistent with N08: the (R+S+T+P)/4 average equals the payoff of two 50/50 RANDOM players. It holds in the long-run, undiscounted limit.

## N12 (NOISE)
- 论断:Generosity bound: in the undiscounted (δ=1) game, a reactive strategy (p,q) is a 'partner' iff p=1 and q < q*, where q* = min{1-(T-R)/(R-S), (R-P)/(T-P)}. GTFT's forgiveness q must be large enough to avoid vendettas but low enough to give ALLD no selective advantage (citing Molander 1985).
- 原文:Without discounting, δ = 1, a reactive strategy is a partner if and only if p = 1 and q < q ∗ with q ∗ = min{1−(T −R)/(R−S), (R−P )/(T −P )}.
- URL:https://research-explorer.ista.ac.at/download/419/7052/2018_NatureHumanBeh_Hilbe.pdf
- 来源:Hilbe, Chatterjee & Nowak, Partners and rivals in direct reciprocity, Nat Hum Behav 2:469-477 (submitted version, Box 2) · 2018 · 【研究】 · verbatim-checked
- 备注:Submitted version, not the typeset text. Main text: 'The probability q can be chosen sufficiently large to avoid costly vendettas after an error, but low enough to give ALLD no selective advantage [41=Molander]'. With T=5,R=3,P=1,S=0: q* = min(1/3, 1/2) = 1/3. In the donation game (T=b,R=b-c,P=0,S=-c) both terms equal 1-c/b, matching Nowak 2006 (N13). A Király EGT lecture (egt04.pdf) gives the same formula as 'q_opt' for Nowak & Sigmund 1992.

## N13 (NOISE)
- 论断:In Nowak's 2006 donation-game framing, GTFT cooperates whenever you cooperate and sometimes cooperates after you defect, with probability 1 - c/b.
- 原文:generous-tit-for-tat ( 17 ), a strategy which cooperates whenever you cooperate, but sometimes cooperates although you have defected (with probability 1 − c/b ). Natural selection can promote forgiveness.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3279745/
- 来源:Nowak 2006, Science · 2006 · 【研究】 · verbatim-checked
- 备注:Ref 17 = Nowak & Sigmund 1992. The b/c parameterization is the donation-game special case of N12.

## N14 (NOISE)
- 论断:Nowak & Sigmund (1992, Nature): in heterogeneous, error-prone populations, a small fraction of TFT is essential for reciprocation to emerge, but it only paves the way for a more generous strategy. TFT is 'the pivot, rather than the aim'.
- 原文:We find that a small fraction of TFT players is essential for the emergence of reciprocation in a heterogeneous population, but only paves the way for a more generous strategy. TFT is the pivot, rather than the aim, of an evolution towards cooperation.
- URL:https://www.nature.com/articles/355250a0
- 来源:Nowak & Sigmund, Tit for tat in heterogeneous populations, Nature 355:250-253 · 1992 · 【研究】 · verbatim-checked
- 备注:Opening paragraph only. Setup (secondhand): reactive strategies (p,q) with stochasticity. The evolved generosity q≈1/3 under standard payoffs is reported by Grim (1996, philarchive GRISAG) and is consistent with N12. The value is NOT verified from the 1992 body text.

## N15 (NOISE)
- 论断:Evolutionary trajectories among reactive strategies often run ALLD → TFT → GTFT.
- 原文:Although reactive strategies contain both ALLD and TFT, stochastic simulations typically favor a more lenient strategy. Evolutionary trajectories often lead from ALLD to TFT and from there to Generous Tit for Tat (GTFT) 42 .
- URL:https://research-explorer.ista.ac.at/download/419/7052/2018_NatureHumanBeh_Hilbe.pdf
- 来源:Hilbe, Chatterjee & Nowak 2018 (submitted version) · 2018 · 【研究】 · verbatim-checked
- 备注:Ref 42 = Nowak & Sigmund 1992. This holds within the reactive (memory-1 on the opponent only) strategy space.

## N16 (NOISE)
- 论断:Nowak & Sigmund (1993, Nature): extended evolutionary simulations of heterogeneous ensembles of probabilistic strategies with mutation and selection found Pavlov (win-stay, lose-shift) unexpectedly successful. Its two advantages over TFT are correcting occasional mistakes and exploiting unconditional cooperators. The second prevents ALLC drift, which would invite defectors.
- 原文:Pavlov's success is based on two important advantages over tit-for-tat: it can correct occasional mistakes and exploit unconditional cooperators. This second feature prevents Pavlov populations from being undermined by unconditional cooperators, which in turn invite defectors. Pavlov seems to be more robust than tit-for-tat
- URL:https://pubmed.ncbi.nlm.nih.gov/8316296/
- 来源:Nowak & Sigmund, A strategy of win-stay, lose-shift that outperforms tit-for-tat in the Prisoner's Dilemma game, Nature 364:56-58 · 1993 · 【研究】 · verbatim-checked
- 备注:The abstract hedges with 'seems to be more robust'. Simulation specifics (memory-one strategies (p1..p4), error rate, payoffs, run counts) were NOT read from primary text; the body is paywalled. Wu & Axelrod describe it as 'a simulated evolutionary process that included noise, but allowed strategies with memory of only the preceding move'.

## N17 (NOISE)
- 论断:Pavlov/WSLS is vulnerable to ALLD: after mutual defection it cooperates, so ALLD can alternate T and P. Wu & Axelrod give the condition: always-defect beats Pavlov at low noise if T + wP > R + wR, i.e. w < (T-R)/(R-P). With T=5,R=3,P=1,S=0 and any w<1, it pays to always defect against Pavlov.
- 原文:It pays to always defect when playing with Pavlov at low levels of noise if alternating T and P is better than always getting R. With standard notation, this is true when T+wP > R+wR or w < (T-R)/(R-P). Thus, with the standard payoffs of T=5, R=3, P=1, S=0, and any w < 1, it pays to always defect when playing with Pavlov.
- URL:https://public.websites.umich.edu/~axe/research/How_to_Cope.pdf
- 来源:Wu & Axelrod 1995 (author version), footnote 3 · 1995 · 【研究】 · verbatim-checked
- 备注:Hilbe 2018 has the matching condition: 'WSLS is a partner strategy if δ > (T−R)/(R−P) and δ > (T−R)/(T−S), which is a sharper condition' than TFT's δ > (T−R)/(T−P), δ > (T−R)/(R−S). As δ→1 this requires 2R > T+P, which fails at the boundary for the 5/3/1/0 payoffs. Imhof 2007: 'WSLS is exploited by ALLD in every second round whereas TFT is not.'

## N18 (NOISE)
- 论断:Wu & Axelrod (1995) reran Axelrod's second-round environment of 63 rules (average interaction length 151 moves) with 1% noise and added GTFT (cooperates 10% of the time it would otherwise defect), Contrite TFT, Pavlov and Generous Pavlov. GTFT scored higher than any of the 63 original rules. CTFT beat all but five. Pavlov ranked below 55 of the 63 and GPavlov below 48.
- 原文:To this environment we add 1% noise, meaning that for each intended choice there is a 1% chance that the opposite choice will actually be implemented. ... The highest score is attained by GTFT which actually does better than any of the 63 rules submitted. CTFT also does very well, better than all but five of the 63 rules. Pavlov does poorly, ranking below 55 of the 63 rules. Adding generosity to Pavlov helps only a little: GPavlov ranks below 48 of the 63 rules.
- URL:https://public.websites.umich.edu/~axe/research/How_to_Cope.pdf
- 来源:Wu & Axelrod 1995 (author version) · 1995 · 【研究】 · verbatim-checked
- 备注:Scores are averaged over 20 replications. GTFT's generosity here is 10%, not the q*=1/3 bound. The noise sweep (0.1% to 10%) found GTFT and CTFT do well at all levels; GTFT is slightly better at low noise, CTFT slightly better when noise > 1%. The paper does not state how plain TFT ranked in the noisy rerun.

## N19 (NOISE)
- 论断:In Wu & Axelrod's ecological simulation (67 rules, 1% noise, 2000 generations), Contrite TFT became the leader by generation 1000 and reached 97% of the population by generation 2000. GTFT had early success, then faded. Both Pavlov versions fell below one part in a million by about generation 100.
- 原文:By generation 1000, CTFT was the leader. It continued to grow, eventually becoming 97% of the population at generation 2000. GTFT had some early success, but then faded. Both versions of Pavlov declined to less than one part in a million as early as the hundred generation. The clear winner in this ecological simulation with noise was CTFT.
- URL:https://public.websites.umich.edu/~axe/research/How_to_Cope.pdf
- 来源:Wu & Axelrod 1995 (author version) · 1995 · 【研究】 · verbatim-checked
- 备注:Conclusion: GTFT is best against populations not adapted to noise. CTFT is better once others have adapted, because contrition corrects only one's own errors (CTFT vs TFT still echoes after TFT's error). 'Pavlov is not robust'. This contradicts the Nowak-Sigmund 1993 headline; the difference is in environment (Axelrod's 63 rules vs a memory-one ensemble) and payoffs (5/3/1/0, where ALLD exploits Pavlov).

## N20 (NOISE)
- 论断:Wu & Axelrod's abstract summarizes the three findings: GTFT is highly effective when the players it meets have not adapted to noise; CTFT is even more effective if they have; Pavlov is not robust.
- 原文:(1) a generous version of tit-for-tat is a highly effective strategy when the players it meets have not adapted to noise; (2) if the other players have adapted to noise, a contrite version of tit-for-tat is even more effective at quickly restoring mutual cooperation without the risk of exploitation; and (3) Pavlov is not robust.
- URL:https://econpapers.repec.org/RePEc:sae:jocore:v:39:y:1995:i:1:p:183-189
- 来源:Wu & Axelrod, JCR 39(1):183-189 (abstract) · 1995 · 【研究】 · verbatim-checked
- 备注:In his 2001 Routledge encyclopedia entry Axelrod restates that TFT 'is overly sensitive to misunderstanding or misimplementation' and that this can be corrected by generosity or contrition (public.websites.umich.edu/~axe/research/TitForTat.pdf).

## N21 (NOISE)
- 论断:Kraines & Kraines (1989) introduced the name 'Pavlov' for a conditioned-response learner in the extended-play PD. WSLS is also known as Pavlov (Kraines & Kraines 1989, 1995) and as 'perfect tit-for-tat'.
- 原文:Our Pavlov learns by conditioned response, through rewards and punishments, to cooperate or defect.
- URL:https://scholars.duke.edu/publication/781706
- 来源:Kraines & Kraines, Pavlov and the prisoner's dilemma, Theory and Decision 26(1):47-79 (abstract via Duke Scholars) · 1989 · 【研究】 · paraphrase
- 备注:Only the first abstract sentence was captured verbatim, through a fetch tool, not a raw page. Imhof 2007: 'WSLS is also known as Pavlov ( Kraines and Kraines, 1989 , 1995 )'; 'Another name for WSLS is "perfect tit-for-tat;" ... the rule is a symmetric subgame-perfect equilibrium, while TFT is typically not.' The Kraines Pavlov is a learning automaton with graded probabilities, not identical to deterministic WSLS (1,0,0,1).

## N22 (NOISE)
- 论断:Fudenberg & Maskin (1990) showed WSLS is evolutionarily stable in the set of finite-complexity strategies in repeated games with errors, while TFT is not.
- 原文:Fudenberg and Maskin (1990) considered a concept of evolutionary stability for repeated games with errors and showed that WSLS is, in this sense, evolutionarily stable in the set of strategies of finite complexity, while TFT is not.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC2460568/
- 来源:Imhof, Fudenberg & Nowak 2007 (describing Fudenberg & Maskin, AER 80:274-279) · 2007 · 【二手转述】 · secondhand
- 备注:This is Fudenberg (a coauthor) describing his own 1990 result. The AER paper was not reached.

## N23 (NOISE)
- 论断:Folk theorem (as stated in a review): for a sufficiently large continuation probability δ, any feasible payoff pair in which both players get at least P can arise in equilibrium. Theory does not single out TFT, and in evolving populations none of these equilibria is evolutionarily stable without mistakes, because of neutral stepping-stone invasions (TFT→ALLC→ALLD; ALLD→STFT→...).
- 原文:The folk theorem 21,22 guarantees that any feasible average payoff can arise in equilibrium, provided that players get at least the mutual defection payoff P (Fig. 1c). On the other hand, in evolving populations none of those equilibria are evolutionarily stable 23–26 . ... Such neutral, stepping-stone invasions are always possible 27,28 , unless there is a positive probability of mistakes 29,30 .
- URL:https://research-explorer.ista.ac.at/download/419/7052/2018_NatureHumanBeh_Hilbe.pdf
- 来源:Hilbe, Chatterjee & Nowak 2018 (submitted version) · 2018 · 【研究】 · verbatim-checked
- 备注:Refs 21-22 = Friedman 1971, Aumann 1981; 23-26 = Maynard Smith 1982, Selten & Hammerstein 1984, Boyd & Lorberbaum 1987, Bendor & Swistak; 29-30 = Boyd 1989, Fudenberg & Maskin 1990. The Fig. 1 caption reads 'for sufficiently large δ, all payoff pairs in which both players get at least P can arise in equilibrium'. Axelrod & Hamilton 1981 already note 'when w is sufficiently great, there is no single best strategy regardless of the behavior of the others'.

## N24 (NOISE)
- 论断:Nowak (2006): direct reciprocity can only lead to cooperation if the probability w of another encounter exceeds c/b. In the TFT-vs-ALLD matrix, the thresholds are b/c > 1/w (ESS), b/c > (2-w)/w (risk-dominance) and b/c > (3-2w)/w (advantageous).
- 原文:Direct reciprocity can only lead to the evolution of cooperation if the probability, w , of another encounter between the same two individuals exceeds the cost-to-benefit ratio of the altruistic act: w > c / b .
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3279745/
- 来源:Nowak 2006, Science (author manuscript) · 2006 · 【研究】 · verbatim-checked
- 备注:The thresholds come from Table 1 (PMC text extraction; the fractions were flattened). The rule assumes cooperators use TFT and defectors ALLD, with no errors. It is a 'simple rule', not a general characterization.

## N25 (NOISE)
- 论断:Imhof, Fudenberg & Nowak (2005, PNAS): with only ALLD, ALLC and TFT under mutation-selection in finite populations, the population cycles ALLD → TFT → ALLC → ALLD, although ALLD is the only strict Nash equilibrium. The time average can be concentrated entirely on TFT.
- 原文:Despite ALLD being the only strict Nash equilibrium, we observe evolutionary oscillations among all three strategies. The population cycles from ALLD to TFT to ALLC and back to ALLD. Most surprisingly, the time average of these oscillations can be entirely concentrated on TFT.
- URL:https://pubmed.ncbi.nlm.nih.gov/16043717/
- 来源:Imhof, Fudenberg & Nowak, Evolutionary cycles of cooperation and defection, PNAS 102:10797-10800 · 2005 · 【研究】 · verbatim-checked
- 备注:This is a finite-population stochastic model without errors in the base model. It is a pro-TFT result conditional on the strategy set {ALLD, ALLC, TFT}.

## N26 (NOISE)
- 论断:Imhof, Fudenberg & Nowak (2007): with errors, in finite populations (limits u→0, N→∞), among ALLD, ALLC, TFT and WSLS, either ALLD is selected (benefit below a critical value) or WSLS is selected (above it). TFT is never selected but lowers the threshold for WSLS. In the donation game the threshold is b/c > 3 for weak selection without TFT and drops to 2 with TFT present.
- 原文:If instead of TFT, WSLS competes with ALLC and ALLD, then WSLS is selected, provided the benefit-to-cost ratio, b / c , is sufficiently large. The critical value is 3 in the limit of weak selection. d) Similar behavior as in c) is observed if TFT is added, but the critical value is now lowered to 2 for any intensity of selection.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC2460568/
- 来源:Imhof, Fudenberg & Nowak, Tit-for-tat or win-stay, lose-shift? J Theor Biol 247:574-580 · 2007 · 【研究】 · verbatim-checked
- 备注:Abstract: 'TFT is never selected in this evolutionary process, but lowers the selection threshold for WSLS.' Body: 'TFT is a catalyst for the emergence of cooperation, but is not the target of evolution.' Assumptions: infinitely repeated PD, error probability ε small, R > (T+S)/2. In the ALLD+TFT+ALLC system with noise, the equilibrium distribution is entirely centred on ALLD. For stronger selection the WSLS-vs-ALLD threshold is somewhat above 3.

## N27 (NOISE)
- 论断:Hilbe et al. 2018: WSLS is the only memory-1 strategy that is mutually cooperative, retaliating and error-correcting. It evolves in a wide range of scenarios provided mutual cooperation is sufficiently profitable and the game is iterated for enough rounds. The review's larger frame: successful strategies are either 'partners' or 'rivals'; partners are favoured by large populations and stable relationships, rivals by small populations and few rounds.
- 原文:WSLS is the only memory-1 strategy that satisfies three simple principles 48 : It is mutually cooperative, retaliating, and error-correcting. ... Due to these principles, WSLS evolves in a wide range of scenarios, provided that mutual cooperation is sufficiently profitable and that the game is iterated for a sufficient number of rounds
- URL:https://research-explorer.ista.ac.at/download/419/7052/2018_NatureHumanBeh_Hilbe.pdf
- 来源:Hilbe, Chatterjee & Nowak 2018 (submitted version); abstract via PubMed 31097794 · 2018 · 【研究】 · verbatim-checked
- 备注:PubMed abstract: 'Whereas small population sizes and a limited number of rounds favour rivalry, partner strategies are selected when populations are large and relationships stable.' A 2018 publisher correction fixed a missing arrow in Fig. 4 only.

## N28 (NOISE)
- 论断:Nowak & Sigmund (1993, PNAS): populations of simple memory-one strategies can show persistent periodic or chaotic oscillations in cooperation. Adding GTFT greatly increases the overall level of cooperation and can lead to long periods of steady cooperation.
- 原文:Adding "generous tit-for-tat" greatly increases the overall level of cooperation and can lead to long periods of steady cooperation.
- URL:https://pubmed.ncbi.nlm.nih.gov/8506355/
- 来源:Nowak & Sigmund, Chaos and the evolution of cooperation, PNAS 90:5091-5094 · 1993 · 【研究】 · verbatim-checked
- 备注:Supports the 'no final winner / cycles' picture.

## N29 (NOISE)
- 论断:Human experiments (Wedekind & Milinski 1996) suggest the Pavlov-vs-GTFT ranking depends on game format. Theory predicts Pavlov wins only in the simultaneous game. In humans about 70% played Pavlov-like and 30% GTFT-like; Pavlovian players did better in simultaneous play and GTFT-like players in alternating play.
- 原文:According to recent developments of theory the last champion strategy of "win--stay, lose--shift" ("Pavlov") is the winner only if the players act simultaneously.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC39691/
- 来源:Wedekind & Milinski, Human cooperation in the simultaneous and the alternating Prisoner's Dilemma: Pavlov versus Generous Tit-for-Tat, PNAS 93:2686-2689 · 1996 · 【研究】 · verbatim-checked
- 备注:This is a format condition on the WSLS result: it rests on Nowak & Sigmund 1994 (JTB) for the alternating PD. That 1994 paper was not reached.

## N30 (NOISE)
- 论断:Knight et al. (2025 preprint) rebuilt Axelrod's second tournament from the surviving Fortran code and reproduced TFT's win. With 1% noise the rankings reshuffle substantially and mean cooperation falls from 0.75 to 0.65. The noisy winner cooperates at 0.61, while TFT cooperates at 0.70; k42r, ranked 10th, outperforms TFT. The authors call the original tournament 'especially favorable to TFT'.
- 原文:The mean cooperation rate declines from 0.75 (noiseless) to 0.65 under noise (Figure 6c). Correspondingly, the new winning strategy in this setting cooperates at 0.61, slightly below the noisy-tournament mean, whereas TFT cooperates at 0.70, above the mean.
- URL:https://arxiv.org/abs/2510.15438
- 来源:Knight, Campbell, Harper, Gaffney, Glynatsi, Reviving, reproducing, and revisiting Axelrod's second tournament (arXiv) · 2025 · 【研究】 · verbatim-checked
- 备注:Preprint, not peer-reviewed at time of reading. TFT's exact rank under noise is not stated in the extracted text. This is a modern counterpart to Wu & Axelrod's N18 and may overlap with a 'reproduction' research line.


### 交叉口径问题
- Boyd & Lorberbaum 1987 body text: the exact invasion construction (which strategy pair invades TFT, and under what w) was not reached. Avoid asserting 'TF2T + STFT' without the primary text.
- Selten & Hammerstein 1984 BBS commentary text was not reached. It is unverified whether they made the noise/echo argument or the neutral-drift/non-ESS argument (secondary sources cite them for non-ESS).
- Molander 1985 full text: his own optimal-generosity formula and the payoffs/discounting he assumed. The q* = min{1-(T-R)/(R-S),(R-P)/(T-P)} formula is verified only from Hilbe et al. 2018, which cites Molander for it, and from a lecture slide that attributes it to Nowak & Sigmund 1992.
- Nowak & Sigmund 1992 body: the reported evolved q (≈1/3 per Grim 1996, secondhand), payoffs, and error handling.
- Nowak & Sigmund 1993 body: strategy space (memory-one p1..p4), error rate (one secondary source says 1%; unverified), payoff values, number of runs, and whether they state the R > (T+P)/2 condition for Pavlov resisting ALLD.
- Farrell & Ware 1989 abstract and exact theorem (finite mixtures) — only secondhand descriptions were seen.
- Axelrod's formal definition of 'collectively stable' (APSR 1981 / 1984 book), to quote precisely that it requires only that no mutant does strictly better (Nash), i.e. weaker than ESS.
- Fudenberg & Maskin 1990 AER result (WSLS-type ESS under errors) — only Fudenberg's coauthored description was seen.
- Wu & Axelrod 1995: plain TFT's rank in the 1%-noise rerun is not given in the text (Fig. 1 is an image).

# 线 ZD

## Z01 (ZD)
- 论断:Press & Dyson 2012 (PNAS 109(26):10409–10413, published online 2012-05-21/22, issue 2012-06-26) introduced zero-determinant (ZD) strategies: memory-one strategies with which player X can unilaterally enforce a linear relation between her and her opponent's long-run scores, including fixing the opponent's score.
- 原文:One specialization of ZD strategies allows X to unilaterally set Y's score.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387070
- 来源:Press & Dyson, Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent, PNAS · 2012 · 【研究】 · verbatim-checked
- 备注:Memory-one (conditions only on last round), infinitely repeated / long-run average payoffs, no errors. Same paper: 'X cannot unilaterally set her own score in IPD.' PNAS doi page returned 403; text read via PMC. Contributed 2012-04-19 (PNAS 'Contributed' track, Dyson NAS member).

## Z02 (ZD)
- 论断:Abstract claims an extortionate ZD player can enforce an extortionate linear relation, and that an 'evolutionary' opponent's best response is to accede; 'only a player with a theory of mind about his opponent can do better', in which case the IPD becomes an Ultimatum Game.
- 原文:Only a player with a theory of mind about his opponent can do better
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387070
- 来源:Press & Dyson 2012 PNAS (abstract) · 2012 · 【研究】 · verbatim-checked
- 备注:Also verbatim from abstract: 'an evolutionary player's best response is to accede to the extortion.' Full abstract not reproduced (tool quote limit); fetch the PMC page to copy it whole. Discussion: 'If Y has a theory of mind, then IPD is simply an ultimatum game'.

## Z03 (ZD)
- 论断:Press & Dyson define an 'evolutionary' player narrowly: one who adjusts his own strategy to improve his score but does not explicitly model X's score or strategy. The 'dominates any evolutionary opponent' title therefore refers to a single fixed-strategy X against one adapting Y, not to population evolution.
- 原文:but does not otherwise explicitly consider X's score or her own strategy
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387070
- 来源:Press & Dyson 2012 PNAS (Methods/Discussion) · 2012 · 【研究】 · verbatim-checked
- 备注:Key to the media overstatement: 'evolutionary' here ≠ evolving population. Discussion advice: X 'should go to lunch leaving her fixed strategy mindlessly in place'. The word 'dominate' appears only in the title, not in the Discussion (per fetch).

## Z04 (ZD)
- 论断:Press & Dyson give an extortion example with extortion factor χ=3 (standard payoffs T=5,R=3,P=1,S=0): if Y fully cooperates, X scores above the mutual-cooperation value 3 and Y below it.
- 原文:X’s score is always greater than the mutual cooperation value of 3, and Y’s is always less.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387070
- 来源:Press & Dyson 2012 PNAS · 2012 · 【研究】 · paraphrase
- 备注:Phrase 'enforces an extortion factor 3' verified in text; χ symbol and payoff numbers are rendered as images so not text-verified. My own calculation (not from source): χ=3, Y always cooperates → s_X≈3.73, s_Y≈1.91 (s_X−P = 3(s_Y−P)). Verify against PDF before printing numbers.

## Z05 (ZD)
- 论断:Press & Dyson explicitly identify Tit-for-Tat as a special (fair) case within the ZD family — the χ=1 / slope-1 boundary of the linear relation s_X−P = χ(s_Y−P), i.e. TFT enforces equal payoffs.
- 原文:which is the well-known tit-for-tat (TFT) strategy
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387070
- 来源:Press & Dyson 2012 PNAS · 2012 · 【研究】 · paraphrase
- 备注:Verbatim phrase confirmed; the fetch reported it arises in 'a special case that implies fairness and at one limit value of a parameter' but the parameter values are images. Also: 'Knowing only TFT among ZD strategies' (verbatim). Hilbe-Nowak-Sigmund 2013 define extortion only for χ>1 and treat TFT separately as (1,0,1,0) — so 'TFT = ZD with χ=1' is accurate as limit/boundary, but TFT is not an 'extortioner'. Check Press–Dyson PDF Eq. for exact parameterization.

## Z06 (ZD)
- 论断:Press & Dyson: when both players know about ZD strategies, they may negotiate to set each other's score to the cooperative maximum, and then there is no advantage in defection.
- 原文:they may choose to negotiate to each set the other’s score to the maximum cooperative value
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387070
- 来源:Press & Dyson 2012 PNAS (Discussion) · 2012 · 【研究】 · verbatim-checked
- 备注:Also: 'Unlike naive PD, there is no advantage in defection'. Shows the authors themselves framed extortion as a game between 'sentient' players, not as an evolutionary winner.

## Z07 (ZD)
- 论断:Press described the discovery as an accident: his program (searching for evolutionarily stable points) kept crashing, which led to ZD strategies; the computer found instances and Dyson generalized them.
- 原文:The computer could find instances, but not generalize them.
- URL:https://www.edge.org/node/21471
- 来源:Edge.org: On 'Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent' (Poundstone, Press, Dyson, Sigmund & Nowak) · 2012 · 【媒体】 · verbatim-checked
- 备注:Edge page dated 2012-06-18. Press's own reply text. Attribution of 'Dyson did the proof' is my inference from context, not verbatim.

## Z08 (ZD)
- 论断:Edge.org's popular framing (William Poundstone) presented Press–Dyson as overturning Axelrod's moral: Axelrod said 'Don't be too clever, don't be unfair'; Press and Dyson supposedly showed cleverness and unfairness triumph.
- 原文:Press and Dyson have shown that cleverness and unfairness triumph after all.
- URL:https://www.edge.org/node/21471
- 来源:Edge.org conversation, Poundstone commentary · 2012 · 【媒体】 · verbatim-checked
- 备注:Main example of overstatement: generalizes a 1-vs-1 fixed-strategy result to Axelrod's tournament/evolution context.

## Z09 (ZD)
- 论断:Dyson himself, on Edge, was skeptical of IPD as a model for evolution of cooperation and summarized Stewart–Plotkin's tournament as 'the strategy that is best for outcome is worst for evolution, and vice versa'.
- 原文:So the strategy that is best for outcome is worst for evolution, and vice versa.
- URL:https://www.edge.org/node/21471
- 来源:Edge.org, Freeman Dyson reply to Stewart & Plotkin · 2012 · 【媒体】 · verbatim-checked
- 备注:Also verbatim: 'still very skeptical about its use as a model for the evolution of cooperation' and 'Cooperation loses and defection wins.' Context of the latter not fully read — check before quoting it, it may be about a specific scenario.

## Z10 (ZD)
- 论断:Sigmund & Nowak (Edge Reality Club, 2012) replied that strategies fixing the opponent's payoff were already known (citing their 1997 'Equal pay for all prisoners'), and that evolution acts at population level, where mutual extortion is self-defeating; the only non-self-defeating norm leads back to Tit-for-Tat.
- 原文:But biological or cultural evolution is not a phenomenon on the level of the individual.
- URL:https://www.edge.org/node/21471
- 来源:Edge.org Reality Club: Karl Sigmund & Martin Nowak · 2012 · 【媒体】 · verbatim-checked
- 备注:Also verbatim: 'We had known about strategies that allow to nail down the opponent's payoff'. The 1997 paper is Boerlijst, Nowak & Sigmund, 'Equal pay for all prisoners', Am. Math. Monthly 104 (equalizer strategies) — citation detail not separately verified.

## Z11 (ZD)
- 论断:MIT Technology Review (2012-08-16) headlined 'The Emerging Revolution in Game Theory', claiming the discovery of 'a winning strategy' for the PD was forcing game theorists to rethink the discipline — while reporting in the same piece Adami & Hintze's finding that ZD strategies are not evolutionarily stable.
- 原文:The world of game theory is currently on fire.
- URL:https://www.technologyreview.com/2012/08/16/85388/the-emerging-revolution-in-game-theory/amp/
- 来源:MIT Technology Review (arXiv blog), The Emerging Revolution in Game Theory · 2012 · 【媒体】 · verbatim-checked
- 备注:Subhead: 'The discovery of a winning strategy for Prisoner's Dilemma is forcing game theorists to rethink their discipline.' Also 'nothing short of revolutionary'. Only quoted sources are Adami & Hintze.

## Z12 (ZD)
- 论断:Stewart & Plotkin's companion PNAS commentary (109(26):10134–10135, 2012-06-18) stated Press & Dyson had 'changed the game' and noted extortion works best when opponents do not realize they are being extorted; if both know ZD, each tries to extort, giving low payoffs for both.
- 原文:What is immediately clear is that, by publishing their results, Press and Dyson have changed the game.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387035
- 来源:Stewart & Plotkin, Extortion and cooperation in the Prisoner's Dilemma, PNAS (commentary) · 2012 · 【研究】 · verbatim-checked
- 备注:Commentary explicitly left evolutionary fate of extortion as open future research. 'Theory of mind' glossed as 'a player who realizes that her behavior can influence her opponents' strategies'.

## Z13 (ZD)
- 论断:Stewart & Plotkin reran an Axelrod-like tournament adding ZD strategies: ZDGTFT-2 (generous ZD, enforces S_X−R = 2(S_Y−R)) got the highest total payoff, above TFT and GTFT; Extort-2 (S_X−P = 2(S_Y−P)) got a lower total payoff but won more head-to-head matches than any strategy except Always Defect.
- 原文:ZDGTFT-2 received the highest total payoff, higher even than Tit-For-Tat and Generous-Tit-For-Tat, the traditional winners.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3387035
- 来源:Stewart & Plotkin 2012 PNAS commentary, Fig. 1 caption · 2012 · 【研究】 · verbatim-checked
- 备注:Earliest primary source for 'extortion wins pairwise but loses the tournament'. Caption: Extort-2 'received a lower total payoff (because its opponents are not evolving), but it won more head-to-head matches than any other strategy, save Always Defect.' NOT stated in the commentary: number of strategies, rounds, payoff numbers, noise. Knight et al. 2024 describe a 19-strategy reproduction 'from Stewart and Plotkin' (secondhand).

## Z14 (ZD)
- 论断:Stewart & Plotkin 2013 (PNAS 110(38):15348–15353) found extortion strategies are not successful in evolving populations unless the population is very small; instead 'generous ZD' strategies are evolutionarily robust for all but the smallest population sizes, and all robust strategies are generous.
- 原文:Extortion strategies are not successful in evolving populations unless the population size is very small.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3780848
- 来源:Stewart & Plotkin, From extortion to generosity, evolution in the Iterated Prisoner's Dilemma, PNAS · 2013 · 【研究】 · verbatim-checked
- 备注:'Robust' = cannot be selectively replaced by a mutant in a finite population (reduces to ESS as N→∞). Setup: pairwise-comparison/imitation process, weak mutation (monomorphic population), selection strength σ. No numeric N threshold given in text. Generous = after deviation from mutual cooperation, own payoff falls more than opponent's (κ=R condition not text-verified, images). arXiv 1304.7205.

## Z15 (ZD)
- 论断:Stewart & Plotkin 2013: WSLS is 'good' but not robust; generous ZD strategies outperform WSLS in some regimes when evolution runs over the full space of memory-one strategies.
- 原文:
- URL:https://arxiv.org/abs/1304.7205v2
- 来源:Stewart & Plotkin 2013 (arXiv version) · 2013 · 【研究】 · paraphrase
- 备注:'in some regimes' is the qualifier — do not write 'generous ZD beats WSLS'. Paper sometimes misspells WSLS as 'win-lose-stay-shift'.

## Z16 (ZD)
- 论断:Adami & Hintze 2013 (Nature Communications 4:2193, published 2013-08-01; preprint arXiv 1208.2666 'Winning isn't everything', Aug 2012) showed ZD strategies (both opponent-score-fixing and extortionate) are at most weakly dominant, not evolutionarily stable, are easily outcompeted by common strategies, and quickly evolve into non-ZD strategies.
- 原文:Here we show that Zero Determinant strategies are at most weakly dominant, are not evolutionarily stable
- URL:https://ar5iv.labs.arxiv.org/html/1208.2666
- 来源:Adami & Hintze, Evolutionary instability of zero-determinant strategies demonstrates that winning is not everything, Nat. Commun. · 2013 · 【研究】 · verbatim-checked
- 备注:Quote from arXiv abstract; published abstract has near-identical wording (PMC3741637). Payoffs (R,S,T,P)=(3,0,5,1). Published correction 2014-06-16 (content of correction not checked).

## Z17 (ZD)
- 论断:Adami & Hintze: ZD wins every direct competition with Pavlov (WSLS), yet Pavlov is the ESS because it cooperates with itself; replicator dynamics show Pavlov drives ZD extinct regardless of initial density.
- 原文:Yet, Pavlov is the ESS because it cooperates with itself
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC3741637
- 来源:Adami & Hintze 2013 Nat. Commun. · 2013 · 【研究】 · verbatim-checked
- 备注:Also verbatim: 'ZD strategies win every single matchup against non-ZD strategies' (Discussion) and 'Thus, ZD wins every direct competition with Pavlov.' Agent-based runs: well-mixed population of 1,024, death-birth/fitness-proportional, 0.1% replacement per update, 1% per-locus mutation; with mutation the population evolves to a stochastic 'general cooperator' (GC). The ZD used is a specific Press–Dyson example — check which p-vector.

## Z18 (ZD)
- 论断:Adami & Hintze: ZD can be evolutionarily stable only with an informational advantage — a tag-based ZD ('ZDt') that cooperates with itself and plays ZD against others is favored only if it is the only strategy that can recognize itself; such an advantage is bound to be short-lived.
- 原文:such an advantage is bound to be short-lived as opposing strategies evolve to counteract the recognition.
- URL:https://ar5iv.labs.arxiv.org/html/1208.2666
- 来源:Adami & Hintze 2013 (arXiv/Nat. Commun.) · 2013 · 【研究】 · verbatim-checked
- 备注:Note the direction: it is ZD recognizing ZD (self-recognition), not opponents recognizing ZD. The brief's phrasing 'ZD can be beaten if opponents recognize them' is not the paper's claim; the paper says opponents can counter by imitating tags or evolving longer memory.

## Z19 (ZD)
- 论断:Hilbe, Nowak & Sigmund 2013 (PNAS 110(17):6913–6918): in reasonably large populations extortioners act as catalysts for cooperation (like TFT) but are not the stable outcome of selection; in very small populations relative payoff differences matter and extortioners hold their ground; in two-population coevolution extortion benefits the slower-evolving population (Red King effect).
- 原文:they can act as catalysts for the evolution of cooperation, similar to tit-for-tat
- URL:https://ar5iv.arxiv.org/html/1212.1067
- 来源:Hilbe, Nowak & Sigmund, Evolution of extortion in Iterated Prisoner's Dilemma games (arXiv 1212.1067) · 2013 · 【研究】 · verbatim-checked
- 备注:Quote from preprint; final PNAS abstract wording not retrieved. Small-population threshold is parameter-specific: 'with our parameter values, for M>10' extortion no longer succeeds (donation game b=3, c=1); WSLS beats extortioners in direct contest when M > 1+χ. Extortion defined only for χ>1.

## Z20 (ZD)
- 论断:Hilbe, Röhl & Milinski 2014 (Nature Communications 5:3976, 2014-05-29), 'Extortion subdues human players but is finally punished in the prisoner's dilemma': computer ZD strategies vs humans; extortioners beat each human opponent but earned lower payoffs than generous ZD strategies.
- 原文:Although extortioners succeeded against each of their human opponents, extortion resulted in lower payoffs than generosity.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC4050275
- 来源:Hilbe, Röhl & Milinski, Extortion subdues human players but is finally punished in the prisoner's dilemma, Nat. Commun. · 2014 · 【研究】 · verbatim-checked
- 备注:Correct title is '...but is finally punished...', NOT '...outperformed in groups'. No group treatment: all games 1 human vs 1 computer. 60 first-year biology students, 60 rounds (length not announced), subjects not told opponent was a computer. Four ZD treatments by slope s: strong/mild extortion (s=1/3, 2/3), mild/strong generosity (s=2/3, 1/3). Payoffs T=€0.50, R=€0.30, P=€0.10, S=€0. Pooled generosity >18% more payoff (P=0.011).

## Z21 (ZD)
- 论断:In Hilbe et al. 2014, humans cooperated 34.2% vs extortioners and 67.7% vs generous ZD; withholding cooperation acted as costly punishment — in the last 10 rounds about a third of humans refused to cooperate with extortioners vs 1 of 30 against generous strategies.
- 原文:
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC4050275
- 来源:Hilbe, Röhl & Milinski 2014 Nat. Commun. · 2014 · 【研究】 · paraphrase
- 备注:Numbers from fetch summary of results section; cooperation vs generous rose 53.0%→76.0% (first vs last 10 rounds), vs extortion 30.3%→39.7% (n.s.). Humans still scored LESS than the extortioner in each pair; the 'punishment' lowers the extortioner's absolute payoff, not below the human's.

## Z22 (ZD)
- 论断:Wang, Zhou, Lien, Zheng & Xu 2016 (Nature Communications 7:11125, 2016-04-12): extortion outperformed generosity only when the game was long (500 rounds) and subjects knew the opponent was a computer; with 60 rounds no significant difference; when unaware, generosity scored higher (replicating Hilbe et al.).
- 原文:More than half of extortionate strategists finally obtain an average score higher than that from mutual cooperation.
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC4832060
- 来源:Wang et al., Extortion can outperform generosity in the iterated prisoner's dilemma, Nat. Commun. · 2016 · 【研究】 · verbatim-checked
- 备注:8 treatments (500/60 rounds × aware/unaware × extort/generous), 256 students, 32 per treatment; payoffs 5/3/1/0. In 500A: extortion 2.943 vs generous 2.263 points/round. Intro: 'To our knowledge, this is the first experimental evidence which supports the predictions of the Press–Dyson theory.' Author order per PMC: Zhijian Wang first; Hilbe–Chatterjee–Nowak 2018 ref list cites it as 'Xu, B., Zhou, Y., Lien, J. W., Zheng, J. & Wang, Z.' — discrepancy, use PMC order. Paper does not measure punishment.

## Z23 (ZD)
- 论断:Hilbe, Chatterjee & Nowak 2018 review (Nature Human Behaviour 2:469–477): Press & Dyson asked whether Alice can win every pairwise encounter regardless of Bob's strategy and make full cooperation optimal for Bob — answer yes; but evolving populations typically do not settle at extortion; extortioners act as catalysts because they never lose direct competitions and can drift into ALLD populations, then give rise to more cooperative strategies.
- 原文:Evolving populations, however, typically do not settle at extortion
- URL:https://research-explorer.ista.ac.at/download/419/7052/2018_NatureHumanBeh_Hilbe.pdf
- 来源:Hilbe, Chatterjee & Nowak, Partners and rivals in direct reciprocity, Nat. Hum. Behav. · 2018 · 【研究】 · verbatim-checked
- 备注:Author-manuscript PDF. 'Twice the payoff' example requires payoffs rescaled so mutual defection = 0. Also verbatim: 'Evolution leads from extortion to generosity'.

## Z24 (ZD)
- 论断:Hilbe–Chatterjee–Nowak 2018: successful strategies are partners (TFT, GTFT, WSLS, Grim — under high continuation probability and sizable benefit) or rivals (ALLD, extortioners); small populations and few rounds favor rivalry, large populations and stable relationships favor partners; only in infinitely repeated undiscounted games is TFT both partner and rival.
- 原文:Whereas small population sizes and a limited number of rounds favor rivalry, partner strategies are selected when populations are large and relationships stable.
- URL:https://research-explorer.ista.ac.at/download/419/7052/2018_NatureHumanBeh_Hilbe.pdf
- 来源:Hilbe, Chatterjee & Nowak 2018 Nat. Hum. Behav. (abstract) · 2018 · 【研究】 · verbatim-checked
- 备注:TFT dual status: 'it does not lose out in any pairwise encounter, while still making sure that it yields the mutual cooperation payoff against players of the same kind.' Same review restates Axelrod: TFT 'did not win any pairwise encounter' yet had highest average score — the mirror image of extortion.

## Z25 (ZD)
- 论断:Hilbe–Chatterjee–Nowak 2018 summarize the human experiments: extortioner beat each human in direct encounter but generous program earned higher average payoffs; fairness concerns explain this, and they vanished when participants were told they faced a computer program. They also note extortion can succeed via chosen representatives (Milinski et al. 2016 Nat. Commun. 7:10915, climate game) and power asymmetry (Hilbe, Hagel & Milinski, PLoS ONE).
- 原文:While the extortionate program indeed outperformed each human opponent in the direct encounter, it was the generous program that reached on average higher payoffs than the extortioner.
- URL:https://research-explorer.ista.ac.at/download/419/7052/2018_NatureHumanBeh_Hilbe.pdf
- 来源:Hilbe, Chatterjee & Nowak 2018 Nat. Hum. Behav. · 2018 · 【二手转述】 · verbatim-checked
- 备注:Secondhand summary of primary experiments. Review says subjects 'did not obtain any information about the nature of their opponent' — true for Hilbe 2014 and the unaware arms of Wang 2016 only. Milinski 2016 and Hilbe-Hagel-Milinski primary papers NOT fetched.

## Z26 (ZD)
- 论断:Hilbe, Traulsen & Sigmund 2015 (Games and Economic Behavior 92:41–52) 'Partners or rivals?' characterize within memory-one strategies: partner strategies (fair share of social optimum, unfair co-player penalized), competitive strategies (never less than co-player) and ZD strategies (enforce linear payoff relation), properties holding against any co-player strategy, memory-one or not.
- 原文:
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC4547490
- 来源:Hilbe, Traulsen & Sigmund, Partners or rivals? Strategies for the iterated prisoner's dilemma, GEB · 2015 · 【研究】 · paraphrase
- 备注:Venue is Games and Economic Behavior, not the journal 'Games'. Abstract content from search snippets, full text not fetched.

## Z27 (ZD)
- 论断:Knight, Harper, Glynatsi & Gillard (PLoS ONE 19(7):e0304641, 2024; arXiv 1904.00973, 2019): in large Axelrod-library tournaments (204 strategies), extortionate strategies achieve many wins but generally not a high score and fail to be evolutionarily stable; top scorers are 'selectively extortionate' (extort weak opponents, cooperate with strong ones), and ZD strategies can be outperformed by non-ZD strategies.
- 原文:Extortionate strategies achieve a high number of wins but they do generally not achieve a high score
- URL:https://pmc.ncbi.nlm.nih.gov/articles/PMC11280246
- 来源:Knight et al., Recognising and evaluating the effectiveness of extortion in the Iterated Prisoner's Dilemma, PLoS ONE · 2024 · 【研究】 · verbatim-checked
- 备注:Best modern source for 'ZD wins every pairwise match but loses tournaments' (plus Stewart–Plotkin 2012 Fig.1 and Adami–Hintze 2013). Also 'Infamously, extortionate strategies do not play well with themselves.' Results depend on strategy pool; no noise/fixed lengths in parts of design.

## Z28 (ZD)
- 论断:Quanta Magazine (Emily Singer, 2015-02-12) framed Press–Dyson as suggesting 'the best strategies were selfish ones that led to extortion, not cooperation', then reported Stewart–Plotkin's finding that generous strategies were most successful in evolving populations.
- 原文:It suggested the best strategies were selfish ones that led to extortion, not cooperation.
- URL:https://www.quantamagazine.org/game-theory-explains-how-cooperation-evolved-20150212/
- 来源:Quanta Magazine, Game Theory Calls Cooperation Into Question · 2015 · 【媒体】 · verbatim-checked
- 备注:Plotkin quoted: 'The most robust strategies, the ones that can't be replaced by other strategies, are generous.' The Plotkin 'defection rules the day' quote refers to later work (Stewart & Plotkin 2014, coevolving payoffs) — do not attach it to ZD. Republished in Scientific American.


### 交叉口径问题
- Exact full abstract of Press & Dyson 2012 not transcribed (tool quote limit); copy from PMC3387070 directly. PNAS doi page 403.
- Press–Dyson χ parameterization and the precise limit giving TFT are in equation images; verify in PDF that TFT corresponds to χ=1 (and the 13/3 limiting score mentioned in the text).
- Stewart & Plotkin 2012 tournament parameters (number of strategies, rounds, payoffs) not stated in commentary; possibly in SI. Knight et al. say a 19-strategy reproduction.
- No 'Nature news' piece on Press–Dyson located; may not exist or may be under a different title. Unverified.
- Dyson's IAS Letter (Fall 2012) piece returned 403 — not read.
- Hilbe–Nowak–Sigmund 2013 final PNAS abstract wording not checked (preprint used).
- Adami–Hintze 2014 correction content not checked.
- No paper titled 'Extortion subdues human players but is outperformed in groups' exists as far as found; the correct title ends 'but is finally punished in the prisoner's dilemma'. Possible confusion with Hilbe, Wu, Traulsen & Nowak 2014 PNAS 'Cooperation and control in multiplayer social dilemmas' (extortion in groups) — not fetched.
- Milinski et al. 2016 (representatives) and Hilbe–Hagel–Milinski (asymmetric power) primary papers not fetched; Becks & Milinski 2019 not checked.
- Author order discrepancy for Nat. Commun. 7:11125 (PMC: Wang first; HCN 2018 ref list: Xu first).

# 线 MODERN

## M01 (MODERN)
- 论断:To mark Axelrod's 20th anniversary, the two tournaments were recreated at the 2004 IEEE Congress on Evolutionary Computation (CEC'04) and the 2005 IEEE Symposium on Computational Intelligence and Games (CIG'05). The rules changed in two ways: noise (moves mis-executed with small probability) was added, and entrants were explicitly invited to submit more than one player.
- 原文:To stimulate novel research, the rules of Axelrod's original tournaments were extended in two key ways. Firstly, noise was introduced, whereby the moves of each player would be mis-executed with some small probability. Secondly, researchers were explicitly invited to enter more than one player into the round-robin style tournament.
- URL:https://eprints.soton.ac.uk/263238/1/journal_paper.pdf
- 来源:Rogers, Dash, Ramchurn, Vytelingum, Jennings, 'Coordinating team players within a noisy Iterated Prisoner's Dilemma tournament', Theoretical Computer Science 377 (2007) 243-259 · 2007 · 【研究】 · verbatim-checked
- 备注:This was written by the Southampton team themselves, not the organizers. The organizers' own chapter (Chong, Humble, Kendall, Li, Yao, ch.1 of '20 Years On', DOI 10.1142/9789812770684_0001) returned 403 and was not read. Slany & Kienreich name the organizers as 'Graham Kendall, Paul Darwen and Xin Yao'. The book's editors were Kendall, Yao and Chong.

## M02 (MODERN)
- 论断:The Southampton team was Nick Jennings, Alex Rogers, Gopal (Sarvapali D.) Ramchurn, Raj (Rajdeep K.) Dash and Krishnen (Perukrishnen) Vytelingum. The university announced the win on 7 October 2004.
- 原文:
- URL:https://www.southampton.ac.uk/news/2004/10/team-wins-competition.page
- 来源:University of Southampton news: 'team wins competition' (7 Oct 2004) · 2004 · 【官方】 · paraphrase
- 备注:The press release lists five names, the same as the TCS paper's authors (A. Rogers, R.K. Dash, S.D. Ramchurn, P. Vytelingum, N.R. Jennings). The tool would not reproduce the full release text. It gives no entry count, no strategy count and no rankings. It says the team won the '20th anniversary challenge' in a noisy environment and that the method uses coding theory.

## M03 (MODERN)
- 论断:Wired (Wendy M. Grossman, 13 Oct 2004): the 2004 competition had 223 entries, Southampton submitted 60 programs, and Southampton had the top three performers.
- 原文:the Southampton team submitted 60 programs
- URL:https://thereitis.org/new-tack-wins-prisoners-dilemma/
- 来源:Wired, 'New Tack Wins Prisoner's Dilemma' (repost; original wired.com/2004/10/new-tack-wins-prisoners-dilemma/) · 2004 · 【媒体】 · secondhand
- 备注:wired.com refused the fetch, so this was read from a repost that credits Wired. The figure '60 programs' conflicts with the papers: Rogers et al. 2007 say 4 teams x 28 = 112, and Slany & Kienreich say the STAR group had 112 members. See M06/M07. Other quotes from the repost: 'The 2004 competition had 223 entries'; 'Southampton had the top three performers'.

## M04 (MODERN)
- 论断:Wired describes recognition as 'a known series of five to 10 moves'. After recognition the programs took 'master and slave' roles: one sacrificed itself so the other could win repeatedly. The sacrificing programs ended near the bottom of the table.
- 原文:a load of utter failures at the bottom of the table who sacrificed themselves for the good of the team
- URL:https://thereitis.org/new-tack-wins-prisoners-dilemma/
- 来源:Wired, 'New Tack Wins Prisoner's Dilemma' (repost) · 2004 · 【媒体】 · secondhand
- 备注:Wired gives no exact count of how many Southampton programs finished at the bottom. The Rogers paper describes the code word as a fixed-length binary sequence of opening moves, tested at 1-16 bits, with an optimum length. The competition entries used a Hamming code in 2004 and a [15,5] BCH code in 2005, so the 2005 code word was 15 moves. That is longer than the 'five to 10' in Wired.

## M05 (MODERN)
- 论断:Wired attributes the 'around 20' remark to organizer Graham Kendall, not to Southampton: 'It turns out we had far too many — we would have won with around 20.'
- 原文:It turns out we had far too many — we would have won with around 20.
- URL:https://thereitis.org/new-tack-wins-prisoners-dilemma/
- 来源:Wired, 'New Tack Wins Prisoner's Dilemma' (repost) · 2004 · 【媒体】 · secondhand
- 备注:Attribution caveat: the WebFetch reader assigned this to Kendall from the 'he said' context. The pronoun 'we' reads oddly for an organizer, so check against the original Wired text before quoting. The same article says Kendall planned a second competition for April 2005.

## M06 (MODERN)
- 论断:Primary source, Southampton's own account: entries were unlimited in 2004, so they entered four teams of 28 players each, all using a single-block Hamming code. Their team leader, with TFT as its default strategy, won by 13% over the second-placed competing player.
- 原文:In the first competition there was no limit on the number of players that could be submitted, and thus, we entered four different teams. Each team consisted of 28 players, and used the single block Hamming code for recognition. ... the team leader that employed tit-for-tat as a default strategy won the competition by a significant margin (it scored 13% more than the second placed competing player).
- URL:https://eprints.soton.ac.uk/263238/1/journal_paper.pdf
- 来源:Rogers et al., Theoretical Computer Science 377 (2007) 243-259 · 2007 · 【研究】 · verbatim-checked
- 备注:4 x 28 = 112 players, which contradicts Wired's '60'. The paper does not say which 2004 league (noise-free or noisy) the 13% refers to. It does not match Slany's league-1 table (M08): StarSN 117,057 vs GRIM 100,611 is +16.3%, and vs teammate StarS 110,611 is +5.8%. 'Competing player' probably means non-team, but 13% still does not fit league 1, so it may refer to the noisy league. The book-chapter version (ch.9 of '20 Years On', 2006 preprint) says instead: 'the team leader from the largest team won with a clear advantage', with no numbers.

## M07 (MODERN)
- 论断:Slany & Kienreich, a rival team, describe the 2004 league 1 as standard IPD rules with 223 strategies. The winning 'STAR' group sent in by Gopal Ramchurn had 112 members, just over half the field.
- 原文:after the STAR group strategy of Gopal Ramchurn (with 112 members, though we are not sure that all strategies colluded as one group). ... 112 is exactly the smallest integer larger than 223 divided by 2, so the STAR group members were just more than 50% of the total population.
- URL:https://arxiv.org/pdf/cs/0609017
- 来源:Slany & Kienreich, 'On some winning strategies for the Iterated Prisoner's Dilemma or Mr. Nice Guy and the Cosa Nostra' (arXiv 2006; ch.8 of '20 Years On', 2007, pp.171-204) · 2006 · 【研究】 · verbatim-checked
- 备注:This independently confirms 112, not 60. It is a competitor's account. They also complain that their own 10,000+ clone 'EmperorAndHisClones' entry was cut to a single copy.

## M08 (MODERN)
- 论断:2004 league 1 top 10 (Slany Table 8.1a): StarSN 117,057, StarS 110,611 and StarSL 110,511 (all Ramchurn/Southampton) took 1st-3rd. Next came GRIM 100,611 (4th) and OmegaTFT 100,604 (5th). Plain TFT is not in the top 10.
- 原文:1 Gopal Ramchurn StarSN (StarSN) 117,057 / 2 Gopal Ramchurn StarS (StarS) 110,611 / 3 Gopal Ramchurn StarSL (StarSL) 110,511 / 4 GRIM (GRIM Trigger)_1 GRIM (GRIM Trigger) 100,611 / 5 Wolfgang Kienreich OTFT (Omega tit for tat) 100,604
- URL:https://arxiv.org/pdf/cs/0609017
- 来源:Slany & Kienreich (2006/2007), Table 8.1a 'Original tournament results' · 2006 · 【研究】 · verbatim-checked
- 备注:This supports Wired's 'top three'. Slany adds that GRIM had played 0.92% more games than OTFT (an error flagged by Abraham Heifets). Scaled for that, OTFT would have been 1st among non-group strategies. Slany argues GRIM's strong showing came from the STAR members defecting against everyone outside their group.

## M09 (MODERN)
- 论断:2004 league 2 was the noisy variant with the same 223 strategies. Per Slany, the top three were again members of Ramchurn's STAR group. OTFT was 3rd among individuals, behind an individual strategy by Colm O'Riordan.
- 原文:OTFT was placed as the second best non-group, individual strategy, placed third after three members of Ramchurn's STAR group and an individual strategy sent in by Colm O'Riordan
- URL:https://arxiv.org/pdf/cs/0609017
- 来源:Slany & Kienreich (2006/2007) · 2006 · 【研究】 · verbatim-checked
- 备注:Read as written, the sentence is internally confusing: it says '2nd best non-group' but 'placed third after three STAR members and O'Riordan', which would make it 5th overall. Rogers et al. say 'the noisy IPD tournaments held at both events were won by a member of such a team, entered by the authors.'

## M10 (MODERN)
- 论断:In 2005 (CIG'05) a cap of 20 players per institution applied. Southampton entered one team using a [15,5] BCH error-correcting code with a TFT-default leader. In the noise-free tournament, three of the top four places went to different teams. In the noisy tournament, Southampton's leader won again, scoring 5% more than the second-placed competitor (averaged over five runs).
- 原文:a fixed limit of 20 players per institution was established ... Within the noise free IPD tournament, three of the top four positions were occupied by representatives of different teams. However, within the noisy IPD tournament, our team leader again won with a clear advantage (averaged over five runs, it scored 5% more than the second placed competing player), despite using the tit-for-tat as a default strategy.
- URL:https://eprints.soton.ac.uk/263238/1/journal_paper.pdf
- 来源:Rogers et al., Theoretical Computer Science 377 (2007) · 2007 · 【研究】 · verbatim-checked
- 备注:On whether collusion works under limited entries: under the 20-player cap it still won the noisy track. The paper credits error-correcting codes. Kendall's quoted 'around 20' (M05) is consistent with this.

## M11 (MODERN)
- 论断:Slany & Kienreich: the 2005 league 1 (standard rules) had 192 strategies and was won by their own 'CosaNostra Godfather', supported by 20 'Hitmen'. The 2005 league 4 allowed one strategy per team and had 50 strategies. It was won by APavlov (Jiawei Li), 1.2% ahead of OmegaTFT.
- 原文:2005 competition, league 1 (standard IPD rules, with 192 participating strategies) • CosaNostra Godfather was overall winner, with 20 CosaNostra Hitmen participating in the CosaNostra group strategy.
- URL:https://arxiv.org/pdf/cs/0609017
- 来源:Slany & Kienreich (2006/2007) · 2006 · 【研究】 · verbatim-checked
- 备注:League 4 quote: 'Winner was the strategy APavlov sent in by Jia-Wei Li, outperforming our second placed OTFT by 1.2%.' So once entries were limited to one per team, colluding groups were excluded by design, and an adaptive Pavlov variant, not TFT, won. Counts for the 2005 noisy league were not found. The organizers' chapter was unreachable.

## M12 (MODERN)
- 论断:The Southampton paper is itself the main source on how much team size matters. In their own test population (18 classic strategies) with 10% noise, two team members win only 3.4% of the time without noise. In the alternative formats (ecological, remove-worst), a team of three or more still wins every competition.
- 原文:with just two team members and no noise, a team player will win the tournament just 3.4% of the time. However, as the noise level increases, the performance of ... At a noise level of 1/5 the same team members win 70.2% of the time.
- URL:https://eprints.soton.ac.uk/263238/1/journal_paper.pdf
- 来源:Rogers et al., Theoretical Computer Science 377 (2007) · 2007 · 【研究】 · verbatim-checked
- 备注:The quote is partial; the text between the ellipses is cut. This is a lab simulation, not the competition. Ecological-format claim: 'with three or more team players (one team leader and two or more team members), the team leader wins every competition.' The paper also notes that TFT 'performs relatively poorly' in their 18-strategy test population, beaten by Adaptive and Gradual.

## M13 (MODERN)
- 论断:Shalizi (bactra.org, Oct 2004) critique: the master/slave scheme is not evolutionarily stable. Slaves have no incentive to take part, and a mutant that defects against masters but plays TFT with everyone else would beat a slave.
- 原文:the slave agents have, by construction, exactly no incentive to participate in the arrangement
- URL:https://bactra.org/weblog/275.html
- 来源:Cosma Shalizi, Three-Toed Sloth weblog, 14 Oct 2004 · 2004 · 【二手转述】 · verbatim-checked
- 备注:This is commentary, not data. Search snippets also attribute to a Freedom-to-Tinker (Princeton CITP) post the claim that 'Tit-for-Tat still scores higher than the average Southampton player'. That post was not opened.

## M14 (MODERN)
- 论断:The Axelrod-Python library's founding paper was published in the Journal of Open Research Software (2016, vol 4, e35, DOI 10.5334/jors.125), not PLoS ONE. Lead author is Vincent Knight, with 22 authors in total.
- 原文:An open framework for the reproducible study of the iterated prisoner's dilemma.
- URL:https://arxiv.org/pdf/1604.00896v4
- 来源:Knight et al., 'An Open Framework for the Reproducible Study of the Iterated Prisoner's Dilemma', J. Open Research Software 4(1):e35 (arXiv v4, 20 Dec 2016) · 2016 · 【研究】 · verbatim-checked
- 备注:The brief said PLoS ONE; that is wrong. The strategy count is inconsistent across versions and sections. arXiv v4 abstract: 'a growing collection of 136 strategies'. Body: '135 strategies are included'. Full-tournament figure: 129 strategies. The journal abstract, via a search snippet, says 139. Report it as 'about 130-140 at the time'.

## M15 (MODERN)
- 论断:Knight et al. 2016 findings: zero-determinant extortionate strategies win many individual matches but do poorly in overall ranking. Lookup-table and meta strategies (Looker Up, Meta Hunter) are 'generally cooperative yet still exploit naive strategies'.
- 原文:extortionate strategies obtain a large number of wins: the number of times they outscore an opponent during a given match. However these do not perform particularly well from the overall tournament ranking point of view.
- URL:https://arxiv.org/pdf/1604.00896v4
- 来源:Knight et al. 2016 (JORS) · 2016 · 【研究】 · verbatim-checked
- 备注:The paper also reproduces Stewart & Plotkin's 19-strategy tournament. It gives no numeric rank for TFT in the text.

## M16 (MODERN)
- 论断:Harper et al. 2017 (PLoS ONE 12(12):e0188046, published 11 Dec 2017): 176 strategies (53 stochastic). Standard tournament: 200 turns. Noisy tournament: 5% chance of flipping each action. Each was repeated 50,000 times. Payoffs (R,P,T,S) = (3,1,5,0).
- 原文:A total of 176 are included, of which 53 are stochastic. A standard tournament with 200 turns and a tournament with 5% noise is discussed. Due to the inherent stochasticity of these IPD tournaments, these tournaments were repeated 50000 times.
- URL:https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0188046
- 来源:Harper, Knight, Jones, Koutsovoulos, Glynatsi, Campbell, 'Reinforcement learning produces dominant strategies for the Iterated Prisoner's Dilemma', PLoS ONE 2017 · 2017 · 【研究】 · verbatim-checked
- 备注:Training used evolutionary algorithms and particle swarm optimization (PSO), which the authors call 'reinforcement learning'. That is not RL in the modern deep-RL sense. The abstract says the strategies were trained 'against a corpus of over 170 distinct opponents'.

## M17 (MODERN)
- 论断:Harper 2017, standard tournament: the top 11 strategies by median payoff were all trained. Next came DBS (Desired Belief Strategy), then Winner12, Fool Me Once and Omega TFT. The worst rank EvolvedLookerUp2_2_2 reached in any tournament was 8th.
- 原文:The top 11 performing strategies by median payoff are all strategies trained to maximize total payoff against a subset of the strategies (Table 2). The next strategy is Desired Belief Strategy (DBS)
- URL:https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0188046
- 来源:Harper et al. 2017, PLoS ONE · 2017 · 【研究】 · verbatim-checked
- 备注:Also verbatim: 'the worst that the EvolvedLookerUp_2_2_2 ranks in any tournament is 8th.' The trained archetypes are lookup tables, Gambler, finite state machines (FSM), HMMs and neural networks (ANN). Discussion: 'In opposition to historical tournament results and community folklore, our results show that complex strategies can be effective for the IPD.'

## M18 (MODERN)
- 论断:Harper 2017 on TFT: over 50,000 standard tournaments TFT never wins a tournament and never wins a single match. It either draws through mutual cooperation or defects second. The paper gives no median rank for TFT in the text; its rank distribution appears only in Fig 9.
- 原文:(We note that it never wins a tournament). Finally Fig 10 shows the number of opponents beaten in any given tournament: Tit For Tat does not win any match. (This is due to the fact that it will either draw with mutual cooperation or defect second).
- URL:https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0188046
- 来源:Harper et al. 2017, PLoS ONE · 2017 · 【研究】 · verbatim-checked
- 备注:A numeric median rank for TFT was not extracted. It would have to be read from Fig 9 or the archived data (ref [31]).

## M19 (MODERN)
- 论断:Harper 2017, noisy (5%) tournament: DBS had the best median score, ahead of two noise-trained and three non-noise-trained strategies. DBS never ranked below 2nd and won 75% of the time. The two noise-trained strategies were top-3 95% of the time. Of the human-designed strategies, only DBS consistently performed well.
- 原文:the DBS strategy never ranks lower than second and wins 75% of the time. The two strategies trained for noisy tournaments rank in the top three 95% of the time.
- URL:https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0188046
- 来源:Harper et al. 2017, PLoS ONE · 2017 · 【研究】 · verbatim-checked
- 备注:Also verbatim: 'Of all the human-designed strategies in the library, only DBS consistently performs well, and it is substantially more complex than traditional tournament winners like TFT, OmegaTFT, and zero determinant strategies.' The noisy top-6 included PSO Gambler, yet it 'performs less well than' Spiteful TFT and OmegaTFT.

## M20 (MODERN)
- 论断:Harper 2017 still finds Axelrod's 'nice' property among the winners: the top strategies never defect first. The authors conclude that first impressions matter.
- 原文:The best strategies are nice (never defecting first)
- URL:https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0188046
- 来源:Harper et al. 2017, PLoS ONE · 2017 · 【研究】 · verbatim-checked
- 备注:The surrounding text says the top-3 strategies 'never defect first and learn to quickly punish poorer strategies'. So the winners are complex but still nice, which is a nuance for the article.

## M21 (MODERN)
- 论断:Glynatsi, Knight & Harper 2024 were published in PLoS Computational Biology 20(12):e1012644 on 26 Dec 2024, not Scientific Reports. The study used 195 strategies (Axelrod-Python v3.0.0) and four tournament types: standard, noisy, probabilistic ending, and noisy + probabilistic ending. The headline total is 45,600 tournaments (11,400 trials x 4).
- 原文:We have run a total of 11400 trials of Algorithm 1. For each trial, we collect the results for four different tournaments, resulting in a total of 45600 (11400 × 4) tournament results.
- URL:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11670945/
- 来源:Glynatsi, Knight, Harper, 'Properties of winning Iterated Prisoner's Dilemma strategies', PLoS Comput Biol 2024 · 2024 · 【研究】 · verbatim-checked
- 备注:Internal inconsistency: Algorithm 1 loops 'for seed ∈ [0, 11420]', and Table 2 says 'based on 11420 unique tournaments' per type, but the text says 11,400 trials. Each trial randomizes the parameters: N ∈ [3,195] strategies, turns n ∈ [1,200], repetitions k ∈ [10,100], noise p_n ∈ [0,1], ending probability p_e ∈ [0,1]. Table 2 restricts the noisy and probabilistic-ending results to p ≤ 0.1, which leaves 1,151 and 1,139 tournaments.

## M22 (MODERN)
- 论断:Glynatsi 2024 headline: no single strategy excels everywhere. Successful strategies are 'nice, provocable and generous, a little envious, clever, and adapt to the environment', and they do best when their cooperation probability matches the population's aggregate cooperation.
- 原文:We find that, while no single strategy consistently excels, successful strategies share key characteristics: they are nice, provocable and generous, a little envious, clever, and adapt to the environment.
- URL:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11670945/
- 来源:Glynatsi, Knight, Harper 2024, PLoS Comput Biol (Author summary) · 2024 · 【研究】 · verbatim-checked
- 备注:Their refined rules, verbatim: 'Be a little bit envious; Be "nice" in non-noisy environments or when game lengths are longer; Reciprocate both cooperation and defection appropriately; Be provocable in tournaments with short matches, and generous in tournaments with noise; It's ok to be clever; Adapt to the environment; Adjust to the mean population cooperation'. So 'nice' holds conditionally, not universally. The authors say these findings 'challenge ... the advice to "not be clever" and "not be envious"'.

## M23 (MODERN)
- 论断:Glynatsi 2024 on envy: tournament winners show some extortionate (ZD-like) behavior, but less than many ZD strategies.
- 原文:The winners of the tournaments considered in this work demonstrate envious behavior, but not to the extent observed in many ZDs.
- URL:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11670945/
- 来源:Glynatsi, Knight, Harper 2024, PLoS Comput Biol · 2024 · 【研究】 · verbatim-checked
- 备注:Envy is measured by SSE distance to ZD behavior. ZD = zero-determinant (Press & Dyson 2012).

## M24 (MODERN)
- 论断:Glynatsi 2024: earlier tournament winners do not appear among the top performers against large opponent pools. In standard tournaments the top ranks are dominated by strategies trained with reinforcement learning (10 of the top 15 came from Harper 2017). In noisy tournaments (p_n ≤ 0.1), DBS ranks 1st with a median normalized rank of 0.
- 原文:we show that the previous tournament winners are lacking against large enough opponent pools; they do not appear among the top-performing strategies anymore.
- URL:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11670945/
- 来源:Glynatsi, Knight, Harper 2024, PLoS Comput Biol · 2024 · 【研究】 · verbatim-checked
- 备注:Also verbatim: 'In standard tournaments dominating strategies were those trained using reinforcement learning techniques. 10 out of the 15 top strategies were introduced in [23]' and 'For noisy tournaments DBS is the top ranked strategy with r̄ = 0, thus DBS won every tournament it participated in.'

## M25 (MODERN)
- 论断:Glynatsi 2024, TFT vs Gradual: TFT's normalized rank looks roughly normally distributed. Gradual has a lower median rank, so it does better than TFT, except in noisy and probabilistic-ending tournaments. TFT does best in probabilistic-ending tournaments, Gradual in standard ones.
- 原文:Overall, Gradual achieves a lower median rank, signifying that it performs better than TFT except in the case of noisy and probabilistic ending tournaments (lower rank is better).
- URL:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11670945/
- 来源:Glynatsi, Knight, Harper 2024, PLoS Comput Biol · 2024 · 【研究】 · verbatim-checked
- 备注:This is in the full random-parameter set. TFT's exact median normalized rank was not extracted; it is in Fig 2.

## M26 (MODERN)
- 论断:Current Axelrod-Python standing tournament (results for v4.13.1, pushed 30 Oct 2024): 236 strategies, 200 turns, 100 repetitions, seed 1. Standard tournament: TFT ranks 82nd of 236 (0-indexed rank 81), median score 2.602, 0 wins. Leader: EvolvedLookerUp2_2_2 (2.854). Gradual 15th; Grudger 40th; Cooperator 137th; Defector 232nd.
- 原文:81,Tit For Tat,2.6022659574468086,0.7725093617021277,0.0,1.0,...
- URL:https://axelrod-tournament.readthedocs.io/en/latest/standard/index.html
- 来源:Axelrod-Python-Tournament docs, std_summary.csv (GitHub Axelrod-Python/tournament, commit 'Add results for 4.13.1', 2024-10-30) · 2024 · 【官方】 · verbatim-checked
- 备注:CSV URL: https://axelrod-tournament.readthedocs.io/en/latest/_downloads/06521e41d1988f718cb46ee467423437/std_summary.csv. Parameters come from run_std.py in the repo (turns=200, repetitions=100, seed=1). The CSV has 236 data rows, ranked 0-235. Top 10 are all trained: EvolvedLookerUp2_2_2, Evolved HMM 5, Evolved ANN 5, Evolved FSM 16, Evolved ANN, Evolved FSM 16 Noise 05, PSO Gambler 2_2_2, PSO Gambler 1_1_1, PSO Gambler Mem1, Evolved FSM 4.

## M27 (MODERN)
- 论断:Same standing tournament with 5% noise (run_noisy.py: noise=0.05, 200 turns, 100 repetitions): TFT ranks 61st of 236, median 2.154. Leader: Evolved ANN 5 Noise 05 (2.506), then DBS (2.458). Omega TFT 10th, Gradual 26th, Grudger 92nd, Defector 161st, Cooperator 206th.
- 原文:60,Tit For Tat,2.15363829787234,0.5090672340425532,109.0,...
- URL:https://axelrod-tournament.readthedocs.io/en/latest/noisy/index.html
- 来源:Axelrod-Python-Tournament docs, noisy_summary.csv (v4.13.1 results, 2024-10-30) · 2024 · 【官方】 · verbatim-checked
- 备注:CSV URL: https://axelrod-tournament.readthedocs.io/en/latest/_downloads/9d6a34f750f60e5b526478e53eef813c/noisy_summary.csv. Under noise, TFT ranks relatively higher (61st vs 82nd), but it is still mid-table. Ranks here are 1-indexed; the CSV is 0-indexed. This is a single seeded run, not a distribution.

## M28 (MODERN)
- 论断:Rapoport, Seale & Colman 2015 (PLoS ONE 10(7):e0134128, published 30 Jul 2015) reanalyzed Axelrod's first-tournament score table as a two-stage tournament: all 756,756 ways of splitting the 15 programs into three groups of five, with group winners meeting in a final round-robin. TFT won only 11.0% of these; T&C (Tideman & Chieruzzi) won 30.0% and S&R (Stein & Rapoport) 24.8%. TFT won the preliminary stage most often (42.1%).
- 原文:Table 3 shows that Program 2 (T&C) won 30.0% of the tournaments, Program 6 (S&R) came second with 24.8%, whereas Program 1 (TFT) only won 11.0%.
- URL:https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0134128
- 来源:Rapoport, Seale, Colman, 'Is Tit-for-Tat the Answer? On the Conclusions Drawn from Axelrod's Tournaments', PLoS ONE 2015 · 2015 · 【研究】 · verbatim-checked
- 备注:Program full names (Tideman & Chieruzzi, Stein & Rapoport) are from Axelrod 1980 entrant list, not this paper's abbreviations — verify. This is a recomputation from Axelrod's published pairwise score table, not new play. The top eight ('nice') programs took 99.7% of wins. In a round-robin of only the top-8 nice programs, 'TFT was one of the four programs that tied for the lowest ranking'. The authors attribute TFT's original win largely to two 'kingmakers' (DOWNING and GRAASKAMP).

## M29 (MODERN)
- 论断:Rapoport et al. 2015 on scoring criterion: ranked by number of pairwise wins, TFT comes last in Axelrod's first tournament (zero wins). The points ranking and the wins ranking are uncorrelated (Spearman ρ = −.103). In the 2004 Kendall competition (223 programs) the correlation is ρ = −.45 (p < 0.001).
- 原文:TFT did not score even a single win—by its nature, it can never outscore its co-player—and was ranked last. The Spearman rank correlation between the two rankings turns out to be ρ = −.103.
- URL:https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0134128
- 来源:Rapoport, Seale, Colman 2015, PLoS ONE · 2015 · 【研究】 · verbatim-checked
- 备注:Discrepancy: RSC describe the 2004 tournament as having 'incorporated random noise', while Slany describes league 1 as 'standard IPD rules' and league 2 as the noisy variant. It is unclear which league's table RSC used (their ref [21], an online table). Abstract conclusion: TFT's efficacy 'is contingent on the design of the tournament, the criterion used to determine success, and the particular values chosen for the Prisoner's Dilemma payoff matrix'. The payoff-matrix argument is a conjecture citing Kretz, not a new simulation.

## M30 (MODERN)
- 论断:Beaufils, Delahaye & Mathieu introduced the 'Gradual' strategy at Artificial Life V (Nara, 16-18 May 1996; MIT Press, pp. 202-209) and claimed it outperforms TFT. Gradual is a TFT variant whose retaliation grows with each defection, followed by two cooperative 'calming' moves.
- 原文:
- URL:https://cristal.univ-lille.fr/SMAC/publications/pdf/alife5-meeting.pdf
- 来源:Beaufils, Delahaye, Mathieu, 'Our Meeting With Gradual: A Good Strategy For The Iterated Prisoner's Dilemma', Artificial Life V (1996) · 1996 · 【研究】 · secondhand
- 备注:The PDF server refused the connection (ECONNREFUSED), so the paper was not read. The abstract claim comes from a search snippet. The mechanism description is backed by Rogers et al. 2007 Table A.1 ('Modified tit-for-tat strategy that use progressively longer sequences...'). Some citations date it 1997. Independent later confirmation that Gradual beats TFT: M25 (Glynatsi 2024, standard tournaments) and M26 (Gradual 15th vs TFT 82nd).


### 交叉口径问题
- Is the Southampton 2004 count 60 (Wired) or 112 (Rogers et al. 2007: 4 teams x 28; Slany: STAR group 112)? The papers agree on 112. The organizers' chapter (Chong/Humble/Kendall/Li/Yao, '20 Years On' ch.1) returned 403 and should be checked for the official count.
- Which 2004 league does Rogers' '13% more than the second placed competing player' refer to? It does not match Slany's league-1 table (+16.3% over GRIM, +5.8% over StarS).
- Was the 2004 'main' tournament noisy? Southampton's press release and RSC 2015 emphasize noise. Slany describes league 1 as standard and league 2 as noisy. Wired's '223 entries' and 'top three' fit league 1.
- Who said 'we would have won with around 20'? The repost suggests Kendall, but the pronoun 'we' is odd for an organizer. Verify against the original Wired text, which wired.com blocked.
- Not found: 2005 CIG entry counts for the noisy league and leagues 2-3 (Slany gives league 1 = 192 and league 4 = 50 only). The noise probability used in 2004/2005 was also not found; Rogers' simulations used 1/10, but that is their own setting.
- TFT's median rank across Harper 2017's 50,000 tournaments is only in Fig 9 and was not extracted numerically. The same goes for TFT's median normalized rank in Glynatsi 2024 (Fig 2).
- Beaufils et al. 1996 Gradual paper (cristal.univ-lille.fr) was unreachable; its experimental numbers (pool size, ranks vs TFT) are unverified.
- Unreached: the Southampton ECS news item 612 (403), the prisoners-dilemma.com official site via Wayback (archive offline / blocked), and the Freedom-to-Tinker post claiming TFT out-scored the average Southampton player.

# 线 EVIDENCE

## E01 (EVIDENCE)
- 论断:Dal Bó & Fréchette (AER 2011) find that in the infinitely repeated PD, cooperation can prevail, but only under conditions stricter than 'cooperation is a subgame-perfect equilibrium', and stricter even than a risk-dominance condition.
- 原文:We show that cooperation may prevail in infinitely repeated games, but the conditions under which this occurs are more stringent than the subgame perfect conditions usually considered or even a condition based on risk dominance.
- URL:https://www.aeaweb.org/articles?id=10.1257/aer.101.1.411
- 来源:Dal Bó & Fréchette, The Evolution of Cooperation in Infinitely Repeated Games: Experimental Evidence, AER 101(1):411-29 · 2011 · 【研究】 · verbatim-checked
- 备注:Quote is the AER abstract, fetched raw from aeaweb.org. Published February 2011, DOI 10.1257/aer.101.1.411.

## E02 (EVIDENCE)
- 论断:Design of Dal Bó & Fréchette 2011: continuation probability δ ∈ {1/2, 3/4}, cooperation payoff R ∈ {32, 40, 48}. Each subject played between 23 and 77 repeated games. Grim risk-dominates AD in only 3 of the 6 cells (δ=1/2 & R=48; δ=3/4 & R=40; δ=3/4 & R=48). Cooperation is an SPE in every cell except δ=1/2 & R=32.
- 原文:each subject participated in between 23 and 77 infinitely repeated games
- URL:https://economics.brown.edu/sites/g/files/dprerj726/files/papers/2007-7_paper.pdf
- 来源:Dal Bó & Fréchette, working paper version (April 2007), Brown Econ WP 2007-7 · 2007 · 【研究】 · verbatim-checked
- 备注:Taken from the 2007 working paper (Table 3 and text), not the final AER text. The δ=0 one-shot control treatments are omitted here. Footnote 5 of the WP has an apparent typo ('R=23'). Check against the AER version before citing exact cells.

## E03 (EVIDENCE)
- 论断:In Dal Bó & Fréchette 2011, first-round cooperation in the risk-dominant treatments rose from 46.5% in early repeated games to 70.6% after 110 interactions. When cooperation was not an equilibrium, first-round cooperation fell from 29% (games starting in the first 10 interactions) to 5.5%.
- 原文:While in the first rounds of the early repeated games in the risk-dominant treatments cooperation was 46.5%, in later repeated games (after 110 interactions) it reached 70.6%
- URL:https://economics.brown.edu/sites/g/files/dprerj726/files/papers/2007-7_paper.pdf
- 来源:Dal Bó & Fréchette 2007 WP (later AER 2011) · 2007 · 【研究】 · verbatim-checked
- 备注:WP numbers; the published version may differ slightly. Strategy fits in the same WP: in late games, AD explains 90% of observations under δ=1/2,R=32 and Grim explains 93% under δ=3/4,R=48.

## E04 (EVIDENCE)
- 论断:The Dal Bó & Fréchette JEL survey (2018) is a meta-analysis of experiments on the infinitely repeated PD. Being supportable in equilibrium does not mean most subjects cooperate. High cooperation appears only when cooperation is 'very robust to strategic uncertainty'.
- 原文:However, the fact that cooperation can be supported in equilibrium does not imply that most subjects will cooperate. High cooperation rates will emerge only when the parameters of the repeated game are such that cooperation is very robust to strategic uncertainty.
- URL:https://www.aeaweb.org/articles?id=10.1257/jel.20160980
- 来源:Dal Bó & Fréchette, On the Determinants of Cooperation in Infinitely Repeated Games: A Survey, JEL 56(1):60-114 · 2018 · 【研究】 · verbatim-checked
- 备注:Abstract fetched raw from aeaweb.org.

## E05 (EVIDENCE)
- 论断:Size of the survey's meta-dataset: 15 papers, 32 treatments (δ, g, ℓ combinations), 2,415 subjects, 157,170 choices. Half the treatments, 73% of subjects and 67% of choices come from papers co-authored by the survey authors, who report robustness checks for this.
- 原文:We have data from 15 papers, involving 32 different treatments (combinations of δ, g and ℓ), with 2415 subjects and a total of 157,170 choices.
- URL:https://web.archive.org/web/2018/https://www.brown.edu/Departments/Economics/Faculty/Pedro_Dal_Bo/coopsurvey.pdf
- 来源:Dal Bó & Fréchette survey, working draft dated March 3, 2016 (Wayback copy) · 2016 · 【研究】 · verbatim-checked
- 备注:From the 2016 draft. The published JEL 2018 version may have updated counts. The original Brown URL now 404s.

## E06 (EVIDENCE)
- 论断:SizeBAD is the size of the basin of attraction of AD against Grim: the minimum belief that the other player is playing Grim needed for cooperation to be optimal. It equals 1 when cooperation is not an SPE, equals 1/2 when δ = δ_RD, and falls as δ rises. The survey adopts it as the main predictor of cooperation.
- 原文:if SizeBAD = 0.8, a player needs to believe that the other player will cooperate with probability 0.8 or higher for him or her to want to also cooperate. If cooperation cannot be supported in equilibrium, then SizeBAD = 1
- URL:https://web.archive.org/web/2018/https://www.brown.edu/Departments/Economics/Faculty/Pedro_Dal_Bo/coopsurvey.pdf
- 来源:Dal Bó & Fréchette survey (2016 draft) · 2016 · 【研究】 · verbatim-checked
- 备注:Formula: SizeBAD = (1-δ)ℓ / (1-(1-δ)(1+g-ℓ)) if δ ≥ g/(1+g), else 1. The survey says it focuses on SizeBAD over δ-δ_RD 'due to its better' performance, but admits the data cannot clearly separate the two.

## E07 (EVIDENCE)
- 论断:Strategies under perfect monitoring: AD, Grim and TFT account for most behaviour. Together they are the majority in 15 of 17 treatments and at least 70% in 11 of them. WSLS (Pavlov) is 'never a sizeable fraction'. AC is rare.
- 原文:WSLS (not listed in this table), also known as Perfect TFT ... However, it is never a sizeable fraction of the strategies used.
- URL:https://web.archive.org/web/2018/https://www.brown.edu/Departments/Economics/Faculty/Pedro_Dal_Bo/coopsurvey.pdf
- 来源:Dal Bó & Fréchette survey (2016 draft), Table 10 and Result 6 · 2016 · 【研究】 · verbatim-checked
- 备注:The quote is abridged with '...'. Also: 'Given the work of Axelrod, one could have expected subjects to use TFT. On the other hand, TFT is not subgame perfect, and, thus, Grim may be more likely. In fact, both Grim and TFT are present in the data.' This is useful nuance: humans use TFT, but not exclusively, and Grim is just as common.

## E08 (EVIDENCE)
- 论断:The survey notes that across its 32 treatments, five pure strategies (AD, AC, Grim, TFT, STFT) always account for the majority of play. In supergames after the fourth, they cover 84% of play in supergames longer than one round. This counters Breitmoser's (2015) mixed-strategy reading.
- 原文:for supergames greater than four, those five strategies account for 84 percent of play in supergames lasting more than one round and 79 percent of play in supergames lasting more than two rounds.
- URL:https://web.archive.org/web/2018/https://www.brown.edu/Departments/Economics/Faculty/Pedro_Dal_Bo/coopsurvey.pdf
- 来源:Dal Bó & Fréchette survey (2016 draft), footnote 38 · 2016 · 【研究】 · verbatim-checked
- 备注:This finding is contested: Breitmoser 2015 AER 'Cooperation, but no reciprocity' argues for semi-grim / mixed behaviour. Worth a counter-check.

## E09 (EVIDENCE)
- 论断:Fudenberg, Rand & Dreber (AER 2012): when intended actions are implemented with noise, subjects cooperate far more in treatments where cooperation is an equilibrium. Successful strategies are 'lenient' (do not retaliate for the first defection), and many are 'forgiving' (return to cooperation after punishing).
- 原文:In these treatments successful strategies were "lenient" in not retaliating for the first defection, and many were "forgiving" in trying to return to cooperation after inflicting a punishment.
- URL:https://www.aeaweb.org/articles?id=10.1257/aer.102.2.720
- 来源:Fudenberg, Rand & Dreber, Slow to Anger and Fast to Forgive: Cooperation in an Uncertain World, AER 102(2):720-49 · 2012 · 【研究】 · verbatim-checked
- 备注:Abstract fetched raw. The abstract also says 'considerable strategic diversity, indicating that subjects had not fully learned the distribution of play.'

## E10 (EVIDENCE)
- 论断:FRD 2012 parameters: δ = 7/8 and noise probability 1/8 (an intended move is flipped to the other action). The survey's table lists FRD 2012 as δ=0.875, g=ℓ=0.33 (i.e. b/c=4) with 48 subjects in that cell. SFEM estimates for that cell: AC 24%, AD 6%, Grim 12%, TFT 15%, totalling only 57%. The rest are lenient or forgiving variants such as TF2T.
- 原文:
- URL:https://web.archive.org/web/2018/https://www.brown.edu/Departments/Economics/Faculty/Pedro_Dal_Bo/coopsurvey.pdf
- 来源:Dal Bó & Fréchette survey (2016 draft), Tables 3 & 10, citing FRD 2012 · 2016 · 【二手转述】 · paraphrase
- 备注:Could NOT reach the FRD full text (Harvard DASH returned 429). δ=7/8 and the table numbers come from the survey. 'Noise = 1/8' and the full list of b/c values (believed to be 1.5/2/2.5/4) are from memory and need checking against the AER paper. One search snippet garbled the noise levels as '1/16 and 1/18', which is unreliable.

## E11 (EVIDENCE)
- 论断:Wilkinson (Nature 1984), wild vampire bats (Desmodus rotundus): food sharing by blood regurgitation depends 'equally and independently' on relatedness and on an index of opportunity for reciprocation. Captive experiments showed that unrelated bats reciprocally exchange blood.
- 原文:food sharing by regurgitation of blood among wild vampire bats (Desmodus rotundus) depends equally and independently on degree of relatedness and an index of opportunity for reciprocation.
- URL:https://www.nature.com/articles/308181a0
- 来源:Wilkinson, Reciprocal food sharing in the vampire bat, Nature 308:181-184 · 1984 · 【研究】 · verbatim-checked
- 备注:Published March 1984. The abstract does not say 'tit-for-tat'. Whether the bat case is TFT is a later gloss (Axelrod and others).

## E12 (EVIDENCE)
- 论断:Carter & Wilkinson (Proc B 2013): 20 captive vampire bats were fasted individually, inducing food sharing on 48 days over 2 years. Food received was the best predictor of food given, 8.5 times more important than relatedness. 64% of sharing dyads were unrelated (67% expected without nepotism). Donors initiated sharing more often than recipients, which argues against harassment.
- 原文:Food received was the best predictor of food given across dyads, and 8.5 times more important than relatedness. Sixty-four per cent of sharing dyads were unrelated, approaching the 67 per cent expected if nepotism was absent.
- URL:https://doi.org/10.1098/rspb.2012.2573
- 来源:Carter & Wilkinson, Food sharing in vampire bats: reciprocal help predicts donations more than relatedness or harassment, Proc R Soc B · 2013 · 【研究】 · verbatim-checked
- 备注:Abstract via Europe PMC. Framed as 'mutual direct fitness benefits' and social bonding, not as strict TFT.

## E13 (EVIDENCE)
- 论断:Carter et al. (Current Biology 2020): previously unfamiliar captive vampire bats were tracked for 15 months. They selectively escalated low-cost grooming before forming higher-cost food-sharing relationships, which supports a 'raising-the-stakes' model. This is a relationship and bonding model, not round-by-round TFT.
- 原文:We found compelling evidence that vampire bats selectively escalate low-cost grooming before developing higher-cost food-sharing relationships.
- URL:https://doi.org/10.1016/j.cub.2020.01.055
- 来源:Carter, Farine, Crisp, Vrtilek, Ripperger & Page, Development of New Food-Sharing Relationships in Vampire Bats, Curr Biol · 2020 · 【研究】 · verbatim-checked
- 备注:Abstract via Europe PMC.

## E14 (EVIDENCE)
- 论断:Milinski (Nature 1987): using mirrors, a single three-spined stickleback inspecting a live predator was given either a simulated cooperating companion (parallel mirror) or a simulated defecting one (angled mirror). In both cases the test fish behaved according to TIT FOR TAT.
- 原文:In both cases the test fish behaved according to TIT FOR TAT supporting the hypothesis that cooperation can evolve among egoists.
- URL:https://www.nature.com/articles/325433a0
- 来源:Milinski, TIT FOR TAT in sticklebacks and the evolution of cooperation, Nature 325:433-435 · 1987 · 【研究】 · verbatim-checked
- 备注:Published January 1987. The 'parallel vs angled mirror' detail is from my memory of the paper. The abstract says only 'a system of mirrors'.

## E15 (EVIDENCE)
- 论断:Milinski's TFT interpretation was challenged right away. Lazarus & Metcalfe (Animal Behaviour 1990) published 'Tit-for-tat cooperation in sticklebacks: a critique of Milinski', and Milinski replied 'No alternative to TIT FOR TAT in sticklebacks' (Anim Behav 39:989-991). Masters & Waite (1990) also disputed whether predator inspection is a PD.
- 原文:
- URL:https://eprints.ncl.ac.uk/119424
- 来源:Lazarus & Metcalfe 1990, Anim Behav 39(5):987-988 (bibliographic record) · 1990 · 【二手转述】 · secondhand
- 备注:Only the bibliographic record and the reply title were confirmed. The arguments of the critique were not read. Carter 2014 cites Dugatkin 1991 'Predator inspection, tit-for-tat and shoaling: A comment on Masters & Waite'.

## E16 (EVIDENCE)
- 论断:Clutton-Brock (Nature 2009 review): firm evidence of reciprocity in animal societies is rare. Many examples of cooperation between non-kin are probably intra-specific mutualism or manipulation.
- 原文:Firm evidence of reciprocity in animal societies is rare and many examples of cooperation between non-kin probably represent cases of intra-specific mutualism or manipulation.
- URL:https://www.nature.com/articles/nature08366
- 来源:Clutton-Brock, Cooperation between non-kin in animal societies, Nature 462:51-57 · 2009 · 【研究】 · verbatim-checked
- 备注:Published November 2009. Nature's editorial summary adds: 'there is little evidence that, under natural conditions, animals other than man commonly exchange either resources or services.' That line is the editor's summary, not the author's abstract.

## E17 (EVIDENCE)
- 论断:Hammerstein (2003, Dahlem volume chapter) argues that after three decades of research, only a modest number of animal examples of reciprocity exist, and evidence is scarce even in primates. Simple repeated-game models do not reflect natural conditions: most repeated animal interactions are not even repeated games, and partner switching and mobility undermine the stability of reciprocity.
- 原文:Most repeated animal interactions do not even correspond to repeated games.
- URL:https://science.umd.edu/faculty/wilkinson/BIOL608W/Hammerstein2003.pdf
- 来源:Hammerstein, Why Is Reciprocity So Rare in Social Animals? A Protestant Appeal, in Genetic and Cultural Evolution of Cooperation (MIT Press), pp. 83-94 · 2003 · 【研究】 · paraphrase
- 备注:The PDF is a poor OCR scan. The quote was reconstructed from garbled OCR ('I.... pc.lted animal lllie raciions do not c\'en correspond 10 repealed gamt.'S'), so treat its wording as near-verbatim and check it against a clean copy. The same abstract says 'Tit-for-Tat-like behavior' has been the prime explanation 'In contrast to the shortage of support', and 'In the few known examples, quick retaliation seems to be the rule'.

## E18 (EVIDENCE)
- 论断:Stevens & Hauser (TICS 2004): despite heavy theoretical interest, there is little empirical evidence for reciprocal altruism in non-human animals. They propose that cognitive constraints (temporal discounting, numerical discrimination, memory) make reciprocity hard for animals.
- 原文:Despite immense theoretical interest, little empirical evidence substantiates the biological importance of reciprocal altruism in non-human animals.
- URL:https://doi.org/10.1016/j.tics.2003.12.003
- 来源:Stevens & Hauser, Why be nice? Psychological constraints on the evolution of cooperation, Trends Cogn Sci 8(2):60-65 · 2004 · 【研究】 · verbatim-checked
- 备注:Abstract via Europe PMC. The volume and pages (8(2):60-65) are from memory. Hauser later had misconduct findings (2010-2012) on other papers. Not known to affect this review, but worth noting if he is named.

## E19 (EVIDENCE)
- 论断:Carter (2014, 'The reciprocity controversy'): many reviews now conclude that reciprocity is rare or absent outside humans. Carter argues this is largely semantic. Definitions translated from TFT 'basically define reciprocity out of existence', while the original broad concept is well supported in fungi, plants, fish, birds, rats and primates.
- 原文:many reviews now conclude that it is rare or absent outside of humans. Here, I show that nonhuman reciprocity seems rare mainly because its meaning has changed over time.
- URL:https://www.iee.unibe.ch/e54478/e384613/e639025/e852764/files871686/Carter2014Thereciprocitycontroversy_eng.pdf
- 来源:Carter, The Reciprocity Controversy, Animal Behavior and Cognition 1(3):368-386, doi:10.12966/abc.08.11.2014 · 2014 · 【研究】 · verbatim-checked
- 备注:Key counterpoint: the 'rare' verdict depends on taking TFT as the operational definition. Lists four problematic approaches: assuming sophisticated cognition, focusing only on short-term contingency with a single partner, demanding a paradoxical temporary fitness cost, and assuming fixed responses.

## E20 (EVIDENCE)
- 论断:Raihani & Bshary (J Evol Biol 2011): strategies based on precise accounting (TFT-style bookkeeping) are relatively uncommon in animals, perhaps because the full IPD assumptions are rarely met. Animals instead use diverse strategies: positive and negative reciprocity, and long-term 'friendships'.
- 原文:Strategies based on precise accounting are relatively uncommon, perhaps because the full set of assumptions of the IPD model are rarely satisfied.
- URL:https://doi.org/10.1111/j.1420-9101.2011.02307.x
- 来源:Raihani & Bshary, Resolving the iterated prisoner's dilemma: theory and reality, J Evol Biol · 2011 · 【研究】 · verbatim-checked
- 备注:Abstract via Europe PMC.

## E21 (EVIDENCE)
- 论断:Schweinfurth & Call (Learning & Behavior 2019) review three textbook cases (Norway rat, common vampire bat, brown capuchin). They conclude that many species have the psychological processes for some form of reciprocity, which 'might be a widespread phenomenon' varying in strategies and mechanisms. This is the current revisionist consensus.
- 原文:We conclude that many species possess the psychological processes to show some form of reciprocity. Hence, reciprocity might be a widespread phenomenon that varies in terms of strategies and mechanisms.
- URL:https://doi.org/10.3758/s13420-019-00394-5
- 来源:Schweinfurth & Call, Reciprocity: Different behavioural strategies, cognitive mechanisms and psychological processes, Learning & Behavior · 2019 · 【研究】 · verbatim-checked
- 备注:The abstract also frames the split: 'some scientists conclude that reciprocity is an almost uniquely human trait ... Others, however, conclude that reciprocity is widespread'.

## E22 (EVIDENCE)
- 论断:Rat evidence: Rutte & Taborsky (PLoS Biol 2007) show 'generalized reciprocity'. Female rats pulled more for an unknown partner after having been helped, regardless of partner identity. Dolivo & Taborsky (Biol Lett 2015) report that rats use direct-reciprocity rules in an IPD variant, preferentially helping cooperators over defectors, and adjust help to the quality of help received.
- 原文:Previous experiments have demonstrated that Norway rats, Rattus norvegicus, cooperate using direct reciprocity decision rules in a variant of the iterated Prisoner's Dilemma, where they preferentially help cooperators instead of defectors.
- URL:https://doi.org/10.1098/rsbl.2014.0959
- 来源:Dolivo & Taborsky, Norway rats reciprocate help according to the quality of help they received, Biol Lett; Rutte & Taborsky 2007 PLoS Biol doi:10.1371/journal.pbio.0050196 · 2015 · 【研究】 · verbatim-checked
- 备注:Both abstracts via Europe PMC. Generalized reciprocity ('help anyone if helped') is not TFT, since it carries no partner-specific memory.

## E23 (EVIDENCE)
- 论断:Axelrod's Ch. 4 builds on the work of Tony Ashworth, whom he calls 'a British sociologist'. Ashworth's 1980 book drew on diaries, letters and reminiscences from virtually every one of the 57 British divisions, averaging more than 3 sources per division. Axelrod says he relies on Ashworth 'for its illustrative quotes and for its historical interpretation' and admits that 'Ashworth does not put it this way' (i.e. as an iterated PD).
- 原文:This chapter relies upon Ashworth’s fine work for its illustrative quotes and for its historical interpretation. While Ashworth does not put it this way, the historical situation in the quiet sectors along the Western Front was an iterated Prisoner’s Dilemma.
- URL:https://gwern.net/doc/economics/1984-axelrod-theevolutionofcooperation-ch4-theliveandletlivesysteminwwi.html
- 来源:Axelrod, The Evolution of Cooperation (1984), Ch. 4 'The Live-and-Let-Live System in Trench Warfare in World War I' (excerpt mirrored on gwern.net) · 1984 · 【研究】 · verbatim-checked
- 备注:Ashworth, Trench Warfare 1914-1918: The Live and Let Live System (London: Macmillan, 1980; Pan reprint 2000). Full quote verified against the gwern excerpt (excerpt mirror, not the printed book; page numbers unverified).

## E24 (EVIDENCE)
- 论断:In Ch. 4 Axelrod himself notes three departures from pure TFT. (1) Retaliation was often 'two-for-one or three-for-one'. (2) Ethics and ritual emerged, so preferences changed: 'behavior and outcomes also affected preferences'. (3) The system was ended by high-command raids, not by internal collapse.
- 原文:When a defection actually occurred, the retaliation was often more than would be called for by TIT FOR TAT. Two-for-one or three-for-one was a common response to an act that went beyond what was considered acceptable.
- URL:https://gwern.net/doc/economics/1984-axelrod-theevolutionofcooperation-ch4-theliveandletlivesysteminwwi.html
- 来源:Axelrod 1984, Ch. 4 (excerpt) · 1984 · 【研究】 · verbatim-checked
- 备注:Same chapter on raids: 'the high command effectively ended the live-and-let-live system by preventing their battalions from exercising their own strategies of cooperation based on reciprocity.'

## E25 (EVIDENCE)
- 论断:Gelman (2008) argues that Axelrod's trench-warfare analysis 'is in error'. Western Front soldiers were not generally in a PD (iterated or otherwise), and their restraint is explained more parsimoniously as immediately reducing their own risks. Gelman is a statistician and political scientist, not a WWI historian.
- 原文:Contrary to Axelrod’s claims, there soldiers in the Western Front were not generally in a prisoner’s dilemma (iterated or otherwise), and their cooperative behavior can be explained much more parsimoniously as immediately reducing their risks.
- URL:https://ideas.repec.org/a/rar/journl/0078.html
- 来源:Gelman, Methodology as ideology: mathematical modeling of trench warfare (a.k.a. 'some comments on Robert Axelrod's The Evolution of Cooperation'), QA - Rivista dell'Associazione Rossi-Doria · 2008 · 【研究】 · verbatim-checked
- 备注:Abstract via RePEc. The 'there' typo is in the original. The full text is paywalled at FrancoAngeli. Joanne Gowa's 1986 International Organization review of Axelrod (IO 40(1):167-186) is also cited as a critique, but its text was not read.

## E26 (EVIDENCE)
- 论断:Akata et al.: different LLMs (GPT-3, GPT-3.5, GPT-4 and others) played FINITELY repeated 2x2 games (10 rounds, horizon known) with each other, with simple strategies and with humans. LLMs do well in self-interested games such as the PD family but poorly in coordination games such as Battle of the Sexes. Preprint arXiv 2305.16867 (v1 26 May 2023, v2 7 May 2025). Published in Nature Human Behaviour 9(7):1380-1390, online 8 May 2025.
- 原文:Here we let different LLMs play finitely repeated 2 × 2 games with each other, with human-like strategies, and actual human players. Our results show that LLMs perform particularly well at self-interested games such as the iterated Prisoner’s Dilemma family. However, they behave suboptimally in games that require coordination, such as the Battle of the Sexes.
- URL:https://www.nature.com/articles/s41562-025-02172-y
- 来源:Akata, Schulz, Coda-Forno, Oh, Bethge & Schulz, Playing repeated games with large language models, Nature Human Behaviour · 2025 · 【研究】 · verbatim-checked
- 备注:NHB metadata (vol 9, issue 7, pp. 1380-1390, online 2025-05-08) checked from the nature.com meta tags. Key caveat: with a known 10-round horizon, backward induction makes defection an equilibrium, which the authors acknowledge.

## E27 (EVIDENCE)
- 论断:Akata et al.: GPT-4 'never cooperates again' against an agent that defects once and then cooperates every round after (Grim-like, unforgiving). This held across robustness checks. Told explicitly that the opponent would defect once and otherwise cooperate, GPT-4 defected in all rounds. Telling it that the other player can make mistakes (after Fudenberg et al. 2012) made it start cooperating again.
- 原文:Crucially, GPT-4 never cooperates again when playing with an agent that defects once but then cooperates on every round thereafter. Thus, GPT-4 seems to be rather unforgiving in this setup.
- URL:https://arxiv.org/abs/2305.16867
- 来源:Akata et al., arXiv 2305.16867v2 · 2025 · 【研究】 · verbatim-checked
- 备注:From the v2 PDF text. The intro also says: 'GPT-4 retaliates repeatedly, even after only having experienced one defection ... it is particularly unforgiving and selfish.' The authors stress that defection can be the equilibrium in a known finite horizon, so 'unforgiving' is not necessarily irrational.

## E28 (EVIDENCE)
- 论断:Fontana, Pierri & Aiello ('Nicer Than Humans', arXiv 2406.13605): Llama2, Llama3 and GPT-3.5 played 100-round IPDs against random opponents with varied defection rates. No model initiates defection. LLMs are at least as cooperative as typical humans. Llama2 and GPT-3.5 are more cooperative than humans and especially forgiving when opponent defection is below 30%. Llama3 is more human-like: uncooperative and exploitative unless the opponent always cooperates.
- 原文:In particular, Llama2 and GPT3.5 are more cooperative than humans, and especially forgiving and non-retaliatory for opponent defection rates below 30%. More similar to humans, Llama3 exhibits consistently uncooperative and exploitative behavior unless the opponent always cooperates.
- URL:https://arxiv.org/abs/2406.13605
- 来源:Fontana, Pierri & Aiello, Nicer Than Humans: How do Large Language Models Behave in the Prisoner's Dilemma? · 2024 · 【研究】 · verbatim-checked
- 备注:v1 19 Jun 2024, v2 19 Sep 2024. Journal or conference venue not verified (possibly ICWSM 2025). The opponents are random (memoryless), not reciprocal strategies.

## E29 (EVIDENCE)
- 论断:Payne & Alloui-Cros (arXiv 2507.02618, v1 3 Jul 2025) ran 7 evolutionary IPD tournaments. The core is a 2x2 design: model capability (basic gpt-3.5-turbo / gemini-1.5-flash vs advanced gpt-4o-mini / gemini-2.5-flash) × per-round termination probability (10% vs 25%). Plus a 75% stress test, a 10% run with Random mutation, and a 10% 'LLM Showdown' adding claude-3-haiku-20240307. Each tournament has 24 agents, 276 round-robin matches per phase and 5 phases, with matches capped at 30 rounds. The runs produced 'almost 32,000 individual decisions and rationales'.
- 原文:Each cell is executed once, yielding 276 round-robin matches per phase (with a fixed population of 24 agents) and a total of five phases per tournament.
- URL:https://arxiv.org/abs/2507.02618
- 来源:Payne & Alloui-Cros, Strategic Intelligence in Large Language Models: Evidence from evolutionary Game Theory · 2025 · 【研究】 · verbatim-checked
- 备注:From the PDF text. Expected match lengths are 9±3, 3±1 and 1.3±0.1 rounds for p=0.10/0.25/0.75. Caveats: each condition run ONCE (no replication). The 'advanced' models are small or fast tiers. The showdown population is 20 (4 each of Anthropic/Bayesian/Gemini/OpenAI/Random). Still v1 only as of fetch, so not peer-reviewed.

## E30 (EVIDENCE)
- 论断:Payne & Alloui-Cros 'strategic fingerprints': Gemini is 'strategically ruthless', OpenAI is 'highly cooperative' (catastrophic in hostile environments), and Claude is 'the most forgiving reciprocator'. Cooperation rates: in the 75% condition Gemini 2.2% vs OpenAI 95.7%. OpenAI was eliminated, and the final population was Gemini 16 + STFT 8. In the Showdown, Gemini 0.925, OpenAI 0.957, Anthropic 0.958.
- 原文:Anthropic's Claude emerged as the most forgiving reciprocator, showing remarkable willingness to restore cooperation even after being exploited or successfully defecting.
- URL:https://arxiv.org/abs/2507.02618
- 来源:Payne & Alloui-Cros 2025, abstract + Table 13 + Table 8 · 2025 · 【研究】 · verbatim-checked
- 备注:Claude (only claude-3-haiku) appears in just ONE tournament, the Showdown. 'Most forgiving' rests on that single run. In the 75% run, average score per move was close (Gemini 2.207 vs OpenAI 2.171), yet the selection outcomes were wildly different. In the Showdown, Anthropic ended phase 5 with 5 agents and OpenAI with 3. Payne also writes that 'OpenAI has a higher raw cooperation rate than Gemini' in every experiment.

## E31 (EVIDENCE)
- 论断:2025 follow-ups. Willis, Du, Leibo & Luck (arXiv 2501.16173) prompted LLMs to write complete IPD strategies with aggressive, cooperative or neutral dispositions and ran evolutionary dynamics. Different LLMs show distinct biases in how well aggressive vs cooperative strategies do. Singh, Radhakrishna & Gulwani (arXiv 2509.04847) put LLM agents against 240 classical strategies in an Axelrod-style tournament. They report performance on par with, sometimes exceeding, the best classical strategies, plus the traits niceness, provocability and generosity, and detection of mid-game strategy switches within a few rounds.
- 原文:We pit model-based agents against a suite of 240 well-established classical strategies in an Axelrod-style tournament and find that language models achieve performance on par with, and in some cases exceeding, the best-known classical strategies.
- URL:https://arxiv.org/abs/2509.04847
- 来源:Singh, Radhakrishna & Gulwani, Collaboration and Conflict between Humans and Language Models through the Lens of Game Theory (5 Sep 2025); Willis et al., Will Systems of LLM Agents Cooperate (27 Jan 2025) · 2025 · 【研究】 · verbatim-checked
- 备注:Only the abstracts were read. Singh et al. are at Microsoft. The '240 strategies' likely means the Axelrod Python library. Which LLMs were used and the exact rankings were not checked.

## E32 (EVIDENCE)
- 论断:FAIRGAME (Buscemi, Proverbio, Di Stefano, Han, Castignani & Liò; arXiv 2504.14325, v1 19 Apr 2025, v5 16 Mar 2026) is a framework for running game-theoretic games among LLM agents. It reports biased outcomes depending on the LLM, the prompt language, and the agents' personality or strategic knowledge.
- 原文:we employ it to uncover biased outcomes in popular games among AI agents, depending on the employed Large Language Model (LLM) and used language, as well as on the personality trait or strategic knowledge of the agents.
- URL:https://arxiv.org/abs/2504.14325
- 来源:FAIRGAME: a Framework for AI Agents Bias Recognition using Game Theory · 2025 · 【研究】 · verbatim-checked
- 备注:Abstract only. It is a tooling paper, and no specific IPD numbers were captured.


### 交叉口径问题
- FRD 2012 exact parameters (noise 1/8? b/c values 1.5/2/2.5/4?) and per-treatment cooperation rates: the full text was unreachable (Harvard DASH 429). Check via the AER PDF or the openICPSR replication data (project 112512).
- Dal Bó & Fréchette JEL 2018 final text: all survey numbers come from the March 2016 draft (Wayback). Confirm the 15 papers / 32 treatments / 2,415 subjects and the '15 of 17 treatments' strategy figure in the published version.
- Whether any professional WWI historian (as opposed to Gelman, a statistician, or Gowa, a political scientist) has critiqued Axelrod's use of Ashworth. Not found. Ashworth himself was a sociologist.
- Gowa 1986 IO review: what it actually says about the trench case. Not read.
- Lazarus & Metcalfe 1990 and Masters & Waite 1990: the substance of the stickleback critiques was not read. Also later Milinski/Dugatkin follow-ups (guppies, 'Tit for Tat: sticklebacks trusting a cooperating partner').
- Payne & Alloui-Cros: has a peer-reviewed version appeared? arXiv still showed v1 only at fetch time. The 'Claude most forgiving' claim rests on one run with claude-3-haiku.
- Akata et al.: the exact model list in the final NHB version (the abstract says 'different LLMs'; the preprint used GPT-3/3.5/4 and others) and the human-participant N for the SCoT experiment.
- Wilkinson 1984: exact captive-experiment N and the 'index of opportunity for reciprocation' definition. Abstract only.
- Breitmoser 2015 AER 'Cooperation, but no reciprocity: Individual strategies in the repeated Prisoner's Dilemma' is a direct counterclaim to the human-TFT evidence. Not fetched; worth adding.