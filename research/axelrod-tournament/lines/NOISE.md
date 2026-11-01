# NOISE 线:理论如何改写 TFT 故事(摘要)

完整论断见 NOISE.json(N01–N30)。来源类型都是一手原文：摘要、作者版 PDF 或 PMC 全文；例外是 N05/N07/N22，这三条属二手转述。

## 1. 稳定性之争(无噪声)
- **Axelrod & Hamilton 1981**:TFT「evolutionarily stable」当且仅当 w ≥ (T−R)/(T−P) 且 w ≥ (T−R)/(R−S)。这里的「稳定」指 TFT 不能被一个**严格更好**的突变者入侵，属于 Nash 型条件，比 Maynard Smith ESS 弱，因为它允许 ALLC 这类中性漂移。APSR 1981 摘要把它叫作「collectively stable」。(N01, N02)
- **Boyd & Lorberbaum 1987**(Nature):在重复 PD 里没有任何纯策略是 ESS，作者据此认为 Axelrod 的若干结论可疑。正文没拿到，具体入侵构造未核实。(N03)
- **Boyd 1989**:只要错误概率始终为正，纯策略就可以是 ESS，前提是它对自己构成「strong perfect equilibrium」。满足条件的有 ALLD 和改良版 TFT(即 contrite 型)，普通 TFT 不在其列。(N04)
- **Bendor & Swistak 1995**:两派结论并不矛盾。按可达到的稳定概念，稳定策略「太多」，稳定本身没有区分力；但按能抵御的入侵规模算，TFT 类条件合作者最稳健。这一条是挺 TFT 的反方声音。(N06)
- Farrell & Ware 1989 把结论推广到有限混合策略(仅二手转述);Selten & Hammerstein 1984 原文未见，后人引用他们的是「ALLC 中性漂移，所以 TFT 非 ESS」这一点。(N05, N07)

## 2. 噪声下的 TFT 回声
- 两个 TFT 中一方误背叛后，双方陷入 C/D 交替，长期平均收益只有 (R+S+T+P)/4。按标准收益是 2.25,低于互相合作的 3。见 Imhof et al. 2007。(N08)
- Molander 1985 的摘要原话是:TFT「performance deteriorates drastically at arbitrarily low noise levels」,办法是加入「some unconditional generosity」,而且不会因此被剥削。Wu & Axelrod 转述:任意噪声下，两个 TFT 的长期收益等于两个 RANDOM。(N10, N11)

## 3. 慷慨度公式与 GTFT
- 不折扣(δ=1)时，若 p=1 且 q < q\* = min{1−(T−R)/(R−S), (R−P)/(T−P)},该策略就是「partner」。按标准 5/3/1/0 收益算,q\* = 1/3。这个公式逐字出自 Hilbe et al. 2018 的提交版，他们把它归功于 Molander。在 donation game 中，公式退化为 1−c/b,与 Nowak 2006 一致。(N12, N13)
- **Nowak & Sigmund 1992**:少量 TFT 是互惠起步的必要条件，但它「only paves the way for a more generous strategy. TFT is the pivot, rather than the aim」。演化出的 q≈1/3 目前只有二手来源。(N14, N15)

## 4. Pavlov / WSLS
- **Nowak & Sigmund 1993**:在带突变和选择的概率策略异质群体中，Pavlov 意外胜出。它的两个优势是能纠错，并且能剥削 ALLC,从而防止 ALLC 漂移把 ALLD 招进来。摘要措辞带保留:「seems to be more robust」。具体模拟参数未拿到。(N16)
- **WSLS 的弱点**:相互背叛后它会回到合作，因此 ALLD 能交替拿到 T 和 P。Wu & Axelrod 脚注给出条件:当 w < (T−R)/(R−P) 时，一直背叛就划算;按 5/3/1/0 收益，任何 w<1 都满足。Hilbe 给出 WSLS 成为 partner 的条件:δ > (T−R)/(R−P),比 TFT 的条件更严;δ→1 时这要求 2R > T+P。(N17)
- Kraines & Kraines 1989 最早提出「Pavlov」这个名字，但他们的 Pavlov 是渐进学习的自动机，不完全等同于确定性的 WSLS。Fudenberg & Maskin 1990 证明:在有限复杂度策略中、带错误的条件下,WSLS 是 ES,TFT 不是。这一点只有二手转述。(N21, N22)
- 博弈形式也有影响：理论上 Pavlov 只在同时行动时胜出，交替行动时 GTFT 更好;人类实验结果见 Wedekind & Milinski 1996。(N29)

## 5. Wu & Axelrod 1995:真正「带噪重跑锦标赛」
- 实验环境是第二轮的 63 条规则，平均 151 步，噪声 1%,结果取 20 次重复的平均。GTFT(慷慨度 10%)得分高于全部 63 条原规则;CTFT 只排在 5 条之后;Pavlov 低于其中 55 条,GPavlov 低于 48 条。(N18)
- 噪声在 0.1%–10% 范围内变化时,GTFT 和 CTFT 始终表现好。噪声 ≤1% 时 GTFT 略优，噪声 >1% 时 CTFT 略优。论文**没有**给出普通 TFT 在带噪重跑中的名次。
- 生态模拟跑了 2000 代:CTFT 最终占 97%,GTFT 先涨后退，两种 Pavlov 在约 100 代内就跌到百万分之一以下。结论是 Pavlov「not robust」。(N19, N20)
- **与 Nowak-Sigmund 1993 的矛盾**:两者的环境不同，一边是 Axelrod 的 63 条人写规则，一边是记忆-1 概率策略系综;收益也不同,5/3/1/0 下 ALLD 能剥削 Pavlov。所以「WSLS 胜过 TFT」依赖具体条件，不是普遍结论。

## 6. 民间定理与有限群体
- 民间定理：只要 δ 足够大，任何双方都至少得到 P 的收益组合都可以是均衡，所以理论本身不会挑出 TFT。没有错误时，中性的踏脚石入侵(TFT→ALLC→ALLD)总是可能的。来源是 Hilbe 2018。(N23)
- Nowak 2006:直接互惠成立的条件是 w > c/b,前提是 TFT 对 ALLD、无错误。(N24)
- **Imhof et al. 2005**:有限群体中 ALLD→TFT→ALLC→ALLD 循环出现，时间平均可以完全集中在 TFT 上。这是在无噪声、三策略模型中挺 TFT 的结果。(N25)
- **Imhof et al. 2007**:带错误的四策略模型里,TFT「never selected」,但它能降低 WSLS 的门槛：弱选择下，没有 TFT 时门槛是 b/c>3,有 TFT 时降到 2。原话是「catalyst...not the target」。(N26)
- **Hilbe et al. 2018**:WSLS 是唯一同时满足「互相合作、会报复、能纠错」的记忆-1 策略，前提是合作收益够高、轮数够多。成功策略分 partners 和 rivals 两类：大群体、关系稳定时 partners 胜出，小群体、轮数少时 rivals 胜出。(N27)
- Knight et al. 2025(预印本)重建了第二轮锦标赛,TFT 依然胜出;加 1% 噪声后排名大洗牌，赢家合作率 0.61,TFT 为 0.70,k42r 超过了 TFT。(N30)

## 叙事要点
「TFT 被噪声打败」这个说法需要拆成三层:
1. 两个 TFT 相遇时会产生回声，这一点没有争议。
2. 带噪重跑 Axelrod 环境时，胜出的是**TFT 的变体**(GTFT、CTFT),不是 Pavlov。
3. 在演化模型里,WSLS 是否胜出取决于收益条件(2R>T+P 或 b/c 门槛)、同时还是交替行动、有没有 ALLD。

几篇论文对 TFT 的定位口径一致:TFT 是「催化剂/支点」,不是演化终点。

## 未拿到
- Boyd-Lorberbaum、Selten-Hammerstein、Molander、Farrell-Ware、Fudenberg-Maskin 的正文。
- NS1992、NS1993 的正文，包括模拟参数和 q≈1/3。
- Axelrod 对「collectively stable」的正式定义原文。
