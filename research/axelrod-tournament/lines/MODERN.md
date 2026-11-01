# MODERN 线 · 后续赛事与 TFT 的命运（摘要）

30 条论断，见 MODERN.json。下文 V = 逐字核对过，S = 二手/媒体。

## 1. 20 周年赛（CEC'04 / CIG'05）
- 规则改了两处：加了 noise；允许一人报多个程序（V，Rogers et al. 2007 TCS）。
- **Southampton 参赛规模，口径冲突**：
  - Wired（2004-10-13，Grossman）：223 个参赛程序，Southampton 报了 60 个，拿下前三（S，通过转载页读到）。
  - 论文：2004 年报了 4 队 × 28 = **112** 个（V，Rogers TCS）。
  - 对手 Slany & Kienreich 也写 STAR 组有 112 个成员，占 223 的一半多（V）。
  - 两篇一手论文一致，"60" 应视为媒体口径，暂不承重。
- **2004 league 1 前三**：StarSN 117,057、StarS 110,611、StarSL 110,511，全是 Southampton。第 4 名 GRIM 100,611，第 5 名 OmegaTFT 100,604。原版 TFT 不在前 10（V，Slany 表 8.1a）。
- **13% 对不上**：Rogers 说队长"比第二名的竞争者多 13%"，但和 league 1 的表算不上：比 GRIM 多 16.3%，比队友 StarS 多 5.8%。可能指 noisy 联赛，待核。
- **识别机制**：
  - Wired 的说法是开局"5 到 10 步"的已知序列。
  - 论文里是二进制 code word：2004 年用 Hamming code，2005 年用 [15,5] BCH，也就是 15 步，比 Wired 说的长。
  - 识别后分 master/slave，slave 牺牲自己，成了"榜底一堆彻底失败者"（Wired 原话；具体多少个垫底没有数字）。
- **限额后还灵不灵**：
  - 2005 年每个机构限报 20 个。Southampton 在 noisy 赛照样夺冠，平均 5 轮比第二名多 5%；无噪声赛前四里有三个是各家团队的成员（V）。
  - 2005 league 4 每队只准报 1 个（50 个参赛）：冠军是 APavlov（Jiawei Li），第二是 OmegaTFT，差 1.2%（V，Slany）。
  - Wired 引一位组织者（似是 Kendall，待核）："we would have won with around 20"（S）。
- 2005 league 1 有 192 个参赛，Slany 自家的 CosaNostra（1 个 Godfather + 20 个 Hitmen）夺冠（V，竞争方自述）。
- Shalizi 批评：slave 没有动机留在合谋里，这套安排不是演化稳定的（V，博客评论）。

## 2. Axelrod-Python
- **期刊纠错**：Knight et al. 2016 发在 **JORS**（4:e35），不是 PLoS ONE。策略数在各版本、各节里不一致（136 / 135 / 129 / 139），只能写"约 130-140"（V）。
- **Harper et al. 2017**（PLoS ONE e0188046），176 个策略，标准赛与 5% noise 赛各跑 5 万次（V）：
  - 标准赛前 11 名全是训练出来的策略（EvolvedLookerUp2_2_2 最差也排第 8），之后依次是 DBS、Winner12、Fool Me Once、OmegaTFT。
  - TFT "never wins a tournament"，也一场 match 都不赢。论文正文没给 TFT 的中位名次，只在 Fig 9 里有分布。
  - noisy 赛：DBS 从没掉出前二，75% 的时候拿第一。
  - 结论：复杂策略可以很强（与"不要太聪明"相反），但 "The best strategies are nice"。
  - 注意：所谓 "reinforcement learning" 其实是演化算法加 PSO。
- **现行常设赛**（v4.13.1，2024-10-30；236 个策略，200 回合 × 100 次重复）：
  - 标准赛：TFT 排第 **82/236**，冠军 EvolvedLookerUp2_2_2，前 10 全是训练策略。Gradual 第 15，Grudger 第 40，Defector 第 232（V，CSV）。
  - 5% noise 赛：TFT 排第 **61/236**，冠军 Evolved ANN 5 Noise 05，第二 DBS（V）。

## 3. Glynatsi, Knight & Harper 2024
- **期刊纠错**：发在 **PLoS Comput Biol** 20(12):e1012644，不是 Sci Rep。
- 设置：195 个策略，四类赛制（标准 / noisy / 概率结束 / 两者叠加），每次随机抽参赛规模 N∈[3,195]、回合数等参数。
- 总数 45,600 = 11,400 × 4。但同篇另一处写 11,420，自相矛盾（V）。
- 主要结论：
  - 没有一个策略能通吃所有环境。
  - Axelrod 的建议被改写成：有点嫉妒、"在无噪声或长对局时 nice"、短对局要可激怒、有噪声时要宽容、可以聪明、合作率向群体均值看齐。
  - 赢家有一点类 ZD 的敲诈倾向，但比真正的 ZD 弱得多。
  - 往届冠军在大对手池里不再排进前列；标准赛前 15 里有 10 个是 Harper 2017 训练出来的策略。
  - Gradual 的中位名次总体好于 TFT，但在 noisy 和概率结束赛里不是。

## 4. Rapoport, Seale & Colman 2015（PLoS ONE e0134128）
- 用 Axelrod 首届赛公布的分数表，算遍 15 个程序分 3 组的全部 756,756 种两阶段赛：TFT 只赢 11.0%，T&C 赢 30.0%，S&R 赢 24.8%。
- 只让前 8 个 nice 程序循环赛：TFT 和另外三个并列垫底。
- 改按对局胜场计：TFT 0 胜，排最后。积分排名和胜场排名的 ρ = −.103；2004 年 223 个参赛的数据里 ρ = −.45（V）。
- 他们说 2004 赛"有噪声"，Slany 说 league 1 是标准规则，两边说法不一。
- 换 payoff 矩阵会怎样，只是推测，没有做新模拟。

## 5. Gradual（Beaufils et al. 1996，ALife V）
- 原文服务器拒绝连接，未读到。"胜过 TFT"目前只来自摘要片段（S）。
- 后来的独立佐证：Glynatsi 2024（标准赛 Gradual 好于 TFT），现行常设赛 Gradual 第 15、TFT 第 82。

## 没拿到的
- 组织者写的第 1 章（World Scientific，403）。
- 原始赛事官网 prisoners-dilemma.com：Wayback 下线。
- wired.com 原文：被拒，只能读转载。
- Southampton ECS news 612：403。
- Gradual 原论文：连不上。
- Freedom-to-Tinker 那篇"TFT 高于 Southampton 平均分"的文章：没打开。
