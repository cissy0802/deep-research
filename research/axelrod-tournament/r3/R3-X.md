# R3-X 反证搜索席：2004 CEC / 2005 CIG 二十周年赛与 Southampton 合谋

最关键的发现：主办方自己的成绩页（prisoners-dilemma.com，Wayback 上有存档）还能打开，而且有全部 223 行的排名。下面每个数字都按这份表重新核过。

## 逐项裁决
| 子论断 | 裁决 | 依据 |
|---|---|---|
| 2004 共 223 个参赛 | **确认** | 主办方页："In total we had 223 entries"：19 个网页提交、195 个 Java 提交、9 个标准策略 |
| Southampton 报了 112 个（不是 60） | **确认 112，60 被推翻** | 成绩表里署名 "Gopal Ramchurn" 的正好 112 行（我自己数的）。Wired 和 IEEE Spectrum（Crick，2004-11）都写 60，两者都错 |
| 标准联赛（comp 1）前三全是 Southampton | **确认** | 1 StarSN 117,057；2 StarS 110,611；3 StarSL 110,511；4 GRIM 100,611；5 OTFT 100,604。TFT 排第 12，92,962 |
| 底部是自我牺牲的成员 | **基本确认，要加限定** | Southampton 成员排名从 1 一直分布到 216。最后 7 名（217–223）不是 Southampton 的 |
| 13% 差距 | **确认，但说的是 noisy 联赛** | Noise 联赛（comp 2，noise 0.1）：1 StarSN 93,962，2 Colm O'Riordan Mem1 83,049，比值 1.131，即 13.1%。League 1 对 GRIM 是 16.3%，对不上 |
| 2004 noisy 联赛也夺冠 | **冠军确认；"前三全是 Southampton" 被推翻** | Noise 联赛前三是：1 Southampton，2 O'Riordan（单打），3 Southampton CoordinateCDCSIAN。Slany 说 league 2 前三都是 STAR，和主办方表对不上 |
| 2005 每机构限 20 个 | **确认是实际执行的上限**（规则原文没找到） | CIG05 comp 1 共 192 个参赛，Kienreich、Au、Vytelingum、Li 四家各正好 20 个 |
| 2005 noisy 赛 Southampton 夺冠，多 5% | **冠军确认；5% 只核到一部分** | Comp 2 run 1：BWIN（Vytelingum）73,330，对第二名 IMM01（Jiawei Li）70,506，多 4.0%。只核了 run 1，Rogers 说的 "5%" 是 5 轮平均 |
| 2005 comp 1 冠军 CosaNostra，comp 4 冠军 APavlov | **确认** | Run 1：CNGF 100,905 第 1，IMM01 第 2，SWIN（Soton）第 4。Comp 4（50 个参赛）：APavlov 30,096，对 OTFT 29,554，多 1.8%。Slany 写 1.2%，可能是 5 轮平均 |
| "would have won with around 20" 是谁说的 | **是 Jennings，不是 Kendall** | Wired 原文在这句话前面有过渡句 "In Jennings' case, the real interest is agents."，转载页把这句弄丢了 |
| 识别序列 "five to 10 moves" | Wired 转述的 Jennings 原话。论文写的是 Hamming / [15,5] BCH，保留冲突 | |

## 证据摘录
- 主办方 CEC04 页面：http://web.archive.org/web/2010/http://www.prisoners-dilemma.com/results/cec04/cec04.html。原文："In total we had 223 entries… That is, we used the same entries as for competition 1… The noise factor was set to 0.1."
- League 1 全表：http://web.archive.org/web/20170522031559/http://www.prisoners-dilemma.com:80/results/cec04/ipd_cec04_full_run.html，日期 "Mon Jun 21 19:22:47 BST 2004"。页脚："Author: Jan Humble / Contact: Graham Kendall"。
- Noise 联赛表：http://web.archive.org/web/2010/http://www.prisoners-dilemma.com/results/cec04/ipd_cec04_noise.html。共 223 行，其中 Ramchurn 112 行。
- CIG05 成绩：http://web.archive.org/web/2010/http://www.prisoners-dilemma.com/results/cig05/cig05.html，分 comp 1/2/4 的 run 01 页面。页面原文："Each competition was run 5 times"。
- Wired 原文（Wendy M. Grossman，2004-10-13）：http://web.archive.org/web/20070208065046/http://www.wired.com:80/news/culture/0,1284,65317,00.html。相关原句："the Southampton team submitted 60 programs"；"In Jennings' case, the real interest is agents. 'What's interesting from our point of view,' he said, '...we had far too many -- we would have won with around 20.'"
- IEEE Spectrum（Camberley Crick，2004-11）：https://spectrum.ieee.org/a-new-way-out-of-the-prisoners-dilemma-cheat。原文 "entered a team of 60 software robots"。这是第二家写 60 的媒体，看起来和 Wired 同源，算不上独立佐证。
- 主办方 "Did they Cheat?" 页：http://web.archive.org/web/2008/http://www.prisoners-dilemma.com/cheating.html。原文："some of which acted as 'fall guys'"；CIG'05 "introduced another category where only a single entry is allowed"。页面把首届写成 "July 2003"，是笔误：成绩页日期是 2004-06-21，CEC'04 会期是 2004-06-19 到 23。
- Southampton 新闻稿（2004-10-07）：https://www.southampton.ac.uk/news/2004/10/team-wins-competition.page。没有给参赛数量，只强调 "in a noisy environment"。

## 搜索角度（含无结果）
1. Web 搜 "Southampton 60 entries Kendall around 20"：找到 thereitis 转载、Spectrum、ECS 612，没有新的数字来源。
2. 搜主办方章节 Chong/Humble/Kendall/Li/Yao ch.1：只拿到目录（econpapers、lingnan），正文没拿到，**无结果**。
3. Wayback 查 Wired 两种 URL：旧版 65317 命中，2025 年新版存档抓下来是空的。
4. Wayback 查 prisoners-dilemma.com：成绩页命中（CEC04 有 comp 1/2，CIG05 有 comp 1/2/4）。"revised rules.html" 和 results.html 都**没有存档**，所以 20 个上限的规则原文没找到。2004-12 和 2005-02 两版 competition.html 里也没有 20 上限的说法。
5. Southampton ECS news 612（web-archive.southampton.ac.uk）：同一份新闻稿，没有数字。
6. 没试的：Slashdot 04/10/14 讨论帖、Freedom-to-Tinker、New Scientist。主办方原始表已经能直接核对，这些优先级低。

## 文章可以放心写的句子
- 2004 年 CEC 的二十周年赛共有 223 个参赛程序，其中 112 个出自南安普顿团队，略多于一半（主办方成绩表；早期媒体报道写的是 60 个）。
- 在无噪声的标准联赛里，前三名 StarSN、StarS、StarSL 都是南安普顿的"主人"程序；第四名是 GRIM，TFT 排第 12。
- 在噪声为 0.1 的联赛里，南安普顿的领队又拿了第一，得分比第二名（一个独立参赛者）高约 13%。不过这次前三里有一个不是南安普顿的。
- "我们报得太多了，其实大约 20 个就能赢"，说这话的是南安普顿团队的 Nick Jennings（Wired，2004-10-13）。
- 2005 年 CIG 赛里，四个参赛团队都正好报了 20 个程序。噪声赛还是南安普顿夺冠，标准赛的冠军换成了 Kienreich 一方的 CosaNostra，限一人一个的赛道由 Jiawei Li 的 APavlov 夺冠。
- 不要写：60 个；"would have won with around 20" 是 Kendall 说的；noisy 联赛前三也全是南安普顿；20 个上限是规则原文（只能写"实际上每家都是 20 个"）。
