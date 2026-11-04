# R3 · R3-X 反证搜索席
靶子:R3「失业伤害中有一大块来自社会规范与身份而非不工作本身」——子论断 (a) HKS 退休切换 6.12→6.47(J28);(b) Clark 2003 周围失业越多伤害越小(J25);(c) 规范强度放大痛苦(J27);相关 J26、J10。

今天复核了:HKS SOEPpaper 399 全文(DIW PDF,pdftotext,表 1/表 2/表 4);OpenAlex/RePEc/Crossref 按 DOI 取摘要 ~30 篇;OpenAlex 引用追踪 `cites:` HKS EJ 2014(W3121931488)与 Oesch & Lipps 2013(W3123927510),合计 289 条施引文献逐条筛题。
没拿到:Powdthavee 2007(南非,SIR 80:629,doi 10.1007/s11205-006-0013-z,无摘要、Springer 有 bot 挑战未绕)、Shields/Wheatley Price/Wooden 2009(HILDA,无摘要)、Torche & Daviss 2024(美国)、Wetzel et al. 2015、Clark & Lepinteur 2026 摘要;BHPS/UKHLS/HILDA/SHP 的「失业→退休」研究在引用追踪里**一篇没出现**。本轮 WebSearch 配额已被共享预算耗尽(首次调用即拒),未用搜索引擎绕行,只做了 DOI 直取与引用追踪。

## 一、发现
**(a) 退休身份切换——独立复现成立,但有三个限定**
1. HKS 原文核对:表 1 长期失业者 6.12→6.47(n=696),就业者 7.17→7.16(n=2,115);收入 1,208→1,283 欧(+6%,非"不变"但接近)。**表 2:效应只在男性显著**(男 0.409***,女 0.032 不显著;合计 0.245**)。表 4:最后一段失业**之前**两组已差 6.31 vs 7.29——作者自承退休后残差可能来自既有个体差异而非失业。
2. **独立团队+独立数据**:Ponomarenko, Leist, Chauvel 2017(Ageing & Society,doi 10.1017/s0144686x17000976),SHARE 多国一阶差分:失业者退休时生活满意度上升,"mainly a catching-up effect";控制选择后仍显著;从非经济活动退休无变化。→ 方向证实,跨国。
3. 同数据独立团队:Schmälzle, Wetzel, Huxhold 2018(Soc Sci Res,doi 10.1016/j.ssresearch.2018.10.006,SOEP,前后各 10 年):失业者退休**短期上升,但长期轨迹更负**;从就业退休者短期不变、长期更好。→ 「身份红利」可能是短期的。
4. HKS 本组 2019(Demography,doi 10.1007/s13524-019-00778-2):非自愿失业在退休后留下疤痕,超出养老金损失所能解释。→ 切换身份不清零伤害。

**(b) 地区失业率缓冲——方向冲突,且度量本身被质疑**
- 支持:Gathergood 2013(Health Econ,doi 10.1002/hec.2831,BHPS+IV)"largely mitigated by local labour market conditions"(与 Clark 同数据,不同团队);Uğur & Durak 2025(土耳其 19.6 万观测)描述性规范"modestly alleviate",主要在短期失业者。
- 反对/无效:Oesch & Lipps 2013(SOEP+SHP,FE)无缓冲;Chadi 2014(Empirical Econ,SOEP)"even more hurtful when regional unemployment is higher",仅自感领救济受污名者有规范效应;Hajdu & Hajdu 2023(Kyklos,doi 10.1111/kykl.12357,ESS 8 波,区域斜率 FE)**高失业区失业者满意度劣势更大**,并明说"unemployment rate does not reflect the social norm to work";Heggebø & Elstad 2017(ESR,EU-SILC 25 国)仅弱倾向,主要是失业人群构成变化。
- 重解读:Clark, Knabe, Rätzel 2010(Labour Econ,SOEP)能复现标准结果,但真正的分界是就业安全感而非就业/失业;Buffel et al. 2016(WES,SHARE)地区失业率更像劳动市场指标而非规范。

**(c) 规范/身份直接测量——多数支持,有关键反例**
- 支持:Roex & Rözer 2017(SIR,doi 10.1007/s11205-017-1723-0,WVS/EVS+ESS)规范强国失业男性更痛,长期失业者尤甚;Günther, Conradi, Hetschko 2025(Labour Econ,doi 10.1016/j.labeco.2025.102752)东德社会化女性失业更痛(自然实验,身份由制度塑造);Longhi et al. 2023(SJPE,UKHLS 事件研究)工作认同强的男性损失更大;Sage 2018(EVS)工作伦理弱者满意度更高。
- 反对:Stam et al. 2016(WES,doi 10.1177/0950017014564602,45 国 EVS 直接规范测量)"unemployed … unaffected by the social norm to work";退休者的规范效应控 GDP 后消失。Tomova, Lawes, Hetschko, Schöb 2026(J Wellbeing Econ,德国 app 面板)工作态度既不缓冲也不放大失业伤害。

## 二、结局:**存争(分拆裁决)**
- (a) 退休切换:**升级为多源证实**(SOEP + SHARE 多国),但须带"部分追赶、男性为主、长期可能回落"三限定。
- (b) Clark 2003 地区缓冲:**降级**,不得承重。独立数据(ESS、EU-SILC、SHP、SOEP)多数不复现或反向;支持者集中在 BHPS。
- (c) 规范强度放大痛苦:**存争**,跨国直接测量一正一反;个体层身份(认同、社会化)证据较一致。
- 综合:"规范/身份是失业伤害中可变的一块"站得住;"**一大块**"的量级无可靠独立估计。

## 三、成文时可以怎么写 / 不得怎么写
可以:"德国与欧洲多国数据都显示,长期失业者一旦被重新归类为'退休者',满意度回升一截,但只追回部分差距,且主要见于男性";"失业之痛部分取决于社会如何看待不工作——个人的工作认同与成长环境会改变它的大小"。
不得:"周围人都失业就不那么痛"(作为一般规律);"失业伤害大部分来自规范";以 6.47 vs 7.2 的差距直接归因于"不工作本身"(HKS 表 4 显示差距部分先于失业存在);把地区失业率(最高十几个百分点)或退休(老年、有养老金、有期限)外推为"全社会不再需要劳动"的直接证据——只能作类比,并明说类比的边界。
