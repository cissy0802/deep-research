# Round 2 判决与锁定口径(V1–V26 已定案;V27–V32 补跑中)

96 票制:32 组 × 3 票,refute-by-default。原始票据全文存 `r2-votes-partial.json`。
本文件是**成文时的锁定口径清单**:每组给判决 + 必须执行的修正。三处 summarizer 编造已捕获(Chabakauri-Rytchkov 假引语、GK「三分之一」、Hartley-Gerding 假模型描述)——一切引语以逐字读到为准。

## 判决速览(V1–V26)

- HOLDS:V10(G-S 逐字)、V11(2H+1 小修)
- CORRECTED:V1–V9, V12–V26(其余全部)
- OVERTURNED:0(但多组内有子项被推翻,见下)

---

## V1 基金资产口径(被动过半的日期)
- $13.29T/$13.23T:Morningstar 正文没有这对数字(在图里),可引来源=CNBC 2024-01-18 引 Morningstar Direct。写法:「Morningstar 数据、CNBC 报道」。
- Morningstar 分类:index vs active(主动 ETF 算主动);不要用 CNBC 的「ETF+被动基金」措辞(那会把主动 ETF 算进被动)。
- 排除项:货币基金 **+ funds of funds**(后者是与 ICI 口径差异的来源)、CIT、separate accounts。
- 2019 股基交叉:写「截至 2019-08-31(9 月 13 日发布,初步数据)」,用 Morningstar 自己的 50.15%/49.85%、差距约 $250 亿;$4.27T/$4.25T 对可用但差距别写 $20bn。
- YE2025:Morningstar 报告自相矛盾——p1「55%」、p5「over 55%」、图标签 $19.42T/$16.02T=54.8%。$16.02T 不加波浪号。
- ICI 口径:YE2023 指数基金占长线基金 48% → **ICI 定义下过半是 2024**(51%);YE2025 = 52%($19.1T/$36.6T;Fact Book 与 Research Perspective 一个说 $19.1T 一个说 $19.3T,内部不一致)。SSGA「2024」无脚注,但在 ICI 定义下成立——交叉年份取决于口径,2023(Morningstar)与 2024(ICI)都对。
- ICI 月度 2026-06:53.7%(印在表里,分母 $40.7T 与 Fact Book $36.6T 不是同一序列,别连成一条线);URL 会漂移,引「ICI, Active and Index Investing, June 2026(2026-07-31 发布)」。
- Morningstar PDF 有坏字模:pdftotext 会吞 3/6/8/A/N/F/O——别用文本提取核对该 PDF。

## V2 市值口径
- ICI 19%(YE2025):分子=**指数型国内股票** MF+ETF(排除全球基金的美股部分),分母=WFE 美股市值;序列非单调(2019 16→2020 15)。
- Vanguard 23%(2024-12-31):全球基金的美股配置/CRSP 总市场;必须带 Vanguard 自己的脚注 2(承认 Chinco-Sammon 替代估计、自限于基金资产)。
- Fed 14%(2020-03):必须带 Fed 自己的下一句——「aggregate passive share…is still larger」引 BlackRock 2017 全球 18% 估计。三个小数字全部自我声明为下界。
- Fed 四通道:不能写「没有涉及价格的通道」——通道 4 是「估值、波动率与联动」,且论文第 4 节有指数纳入估值分析;正确写法:四通道里没有一条叫「价格发现/指数泡沫」。
- 90% 集中度:是「自 2004 年平均约 90%」,脚注里的数字。
- 引用:FEDS 2018-060r1(2020-05-15 稿),发表版 Financial Analysts Journal 76(4) 2020。

## V3 Chinco-Sammon
- 33.5% 用的是**全天**成交量(DailyVolume),不是收盘量。五个代理(2021):33.50 全天 / 28.65 扣日均量 / 24.62 16:00 后 / 22.53 收盘价成交 / **13.31 仅收盘竞价**。诚实低端是 13.31%(±1.96),**与 ICI 16% 统计不可区分**——最严口径下「翻倍」不成立。作者自己承认全天口径可能高估 2–5pp。
- 38.5% 与 11% 是同一笔 $2.25T 的两种互斥处理:合法对比 = 33.5 vs 11 或 38.5 vs 16;同用=重复计算。
- 自家 apples-to-apples 基准:若所有被动都是指数基金,该方法会得 ~6%(不是 16%)——对照 33.5% 是 5.6×。
- 2000 年 13.39%(SE±1.35pp,插值权重、序列非单调:2008 25.31/2009 31.85);2.5× vs 约 5×(别写 5.3×)。
- 版本漂移:2022 稿 37.8%(三指数、收盘窗、自称下界)→ 发表 32.19%(五指数、全天)——指数更多+量更宽反而更小,是方法修订。
- 收敛结论必须带作者自己的限定:「To be clear: index inclusion does affect prices. The effect just does not come by way of passive rebalancing demand on reconstitution days.」
- 别写「作者承认把被迫交易的主动管理人算进被动」——他们提出并**驳回**了这一异议;他们承认的是把 closet indexer 算进被动。
- 引用:JFE 157 (July 2024) 103860;S&P MidCap 400(不是 S&P 400)。

## V4 成交量口径
- Vanguard 1.2%:分母 Cboe 总量;排除清单(ETF 二级、衍生品、专户)出自 Vanguard 给 II 的声明,不是 PDF 本身。「active 2-5%」是 2006–2024 区间,2024 点值约 2%。份额掩盖量级:总量 $38T→$153T,指数基金交易额约涨 16×。
- ICI 28%:**全部 ETF**(含主动/杠杆);分母含场外;2022 峰 32% 归因于波动性对冲,其后回落而被动仍在涨——序列不跟被动走。
- SSGA:8.40% 是 2018-01 以来**期间平均**,15.39% 是 2025-12 单月;SSGA 自己说主动管理人迁往收盘也在推高 MOC。无被动占比数字。
- Green 64%:是我们对 20+8+36 的求和,II 未印 64%;36%「被动做市」无一手来源、与 20% 概念上可重复计算。Vanguard「<5%」是改了分子分母的构造,与 28% 不同尺度。
- 框架:这些不是同一量的四个估计,是四个不同对象;泡沫论需要 28%/15% 框架、辩方需要 1.2%,双方都不报对方的数。

## V5 Burry
- 引语按 Bloomberg 注明「lightly edited and condensed」处理;采访 2019-09-03(email),发表 09-04。
- 1,049(<$5m)⊃456(<$1m),嵌套非并列;266 是 S&P 500 里过半 <$150m。
- 他自己写了「However, I just don't know what the timeline will be」——「无时间表」有出处;机制他有指(衍生品/伪匹配的不可解仓)。
- S&P 500:2,937.78(2019-09-04)→ 7,798.99(2026-08-13 收盘新高),**价格口径 +165.5%**(不含股息);盘中高点 7,816.70。
- Scion:SEC IAPD 注销生效 2025-11-10(CRD 167772);2025-03 AUM $155m(2019 年约 $340m——警告发出时就是小基金)。
- Substack:michaeljburry.substack.com(带 j),2025-11-23 首发,$379/年;主题以 AI/超大规模资本开支折旧为主,自述范围更广;79 篇无一谈指数化——2019 论点未在本周期重申(但多数付费墙内,收窄表述)。
- acquirersmultiple.com 版本被注入赌博广告链接+伪造归因,不可用作来源。
- 新反证来源:Elm Wealth(Haghani & White, 2019-10-04)当时即反驳其自我拆台(若被动压低小盘,正是主动的机会)。

## V6 Einhorn
- 「fundamentally broken」等引语✓(机器转写字面可靠);同一采访里的让步(4-5×PE+回购、「机会好于以往」)✓。
- 「a bit of a broken market」出处是 **CNBC Delivering Alpha 2024-11-13**(不是 Robin Hood 会议)。
- 他把框架归功于 Green(II)——非独立佐证。

## V7 Green(本期最大修正组)
- **83% 不在正式预印本里**:Green-Krishnan-**Sturm**《A Model for Passive That Breaks the Market》(SSRN 6438678,2026-03-27 挂出,未发表)摘要写的是 **~65% 波动率或急升、90% 三次方速度**。83% 只是 2026-01-20 播客口径。
- 时间线自相矛盾:54%+4pp/年 → 83% 需 7.25 年,5 年只到 74%。
- Apple/CarMax 年化对不上:0.167%/日×252≈42%(简单)/52%(复利),他说 23%;CarMax 0.06%/日→~15%,他说 6%。且模型高估后他当场用基本面消解——无拒绝域。实测:AAPL 2025 全年 +8.6%,比他的模型预测低 ~14pp。
- Vanguard 流入:Morningstar 2025 实数 $240bn(iShares $366bn 才是第一);$350bn 是 Green 的旧数,须归他。
- GK 引用:Green 说「between five and eight」,GK 原文是「about $5 (our estimates are between $3 and $8)」+稳健性 3.5–8;点估计族 5.28(1.10)/7.08(1.86)/7.69(2.32)/10.93(2.64);5.9 是推导值无 SE。GK 全文对被动指数化只有一处转述 De Long 1990;至今未过审(方法论文 GIV 已发 JPE 2024)。
- Andrew Lo 75–80%:找不到任何 Lo 一手文献——只能写「Green 自称复现 Lo」。
- PPA/QDIA 并不要求默认进被动(他说 401k 被迫默认被动是错的)。
- Tier1 Alpha:他自己的公告(yesigiveafig.com,2026-08-09)「leaving Simplify…to found Tier1 Alpha Asset Management, where I will serve as CEO and CIO」;Tier1 Alpha 研究公司此前已存在。
- 「intentionally misleading」用了两次:先对 Vanguard 成交量图(Fig 6),再对 mid-cap 持仓图(REIT/行业指数构成异议)。
- 转写日期 2026-01-20。

## V8 Bogle
- 2018 WSJ:治理集中论、零价格发现主张、结尾为指数基金辩护+引 Coates「Amen」✓。
- 2017:「chaos, catastrophe」与「It's zero」同段相邻✓,但「I'm not concerned about it」隔约 100 词,写「同一回答稍后」;「75% 也不危险」是**记者转述**非直接引语。
- Asness 脚注 40「I made it up」✓(asness.txt)。

## V9 Terry Smith
- Expansión 采访:**2025-11-03**(Roberto Casado);西语原文,英文是译文(Fundsmith 自家挂「TRANSLATION FROM SPANISH」);「>50% assets / <10% funds」的分母切换是 Smith 本人的(西语原文如此)。
- 2026-07 信(fundsmith.co.uk 一手已核):-2.9% = T Class Acc GBP 净值(午间定价)vs MSCI World £ Net(美收盘)+11.2%,14.1pp 是信自己的数;基金声明不对标基准。周转率:正文 51%、附录 51.8%(别写 52%);对照 FY2025 12.7%、FY2024 3.2%。
- 「momentum 30 年新高」= 信里一张 Bloomberg 图(MSCI US Momentum QoQ vs MSCI US QoQ,1995 年起、美国、季度环比差)——是 Smith 对图的转述,非可核验统计。
- 他的被动占比八个月漂移:>50%(2025-11)→ >60%(2026-07 信),均无出处;信里还有「Cboe:主动占交易 80%→10%」无法溯源、「S&P 五个月跌 57%」(实为 2007-10→2009-03 约 17 个月)、「跑赢 24%」实为 24pp 且等权含存活偏差;UK 数据转引自 Simon Evan-Cook 的 Substack。
- 信在 7/10–8/3 间原址重发过(文字修订,数字未变)。
- 对冲框架:信同时说「We have no desire to hug the index」+五大 detractor 是个股选择(LVMH/Zoetis/IDEXX/Microsoft/Coloplast)——归因张力如实写。

## V10 Grossman-Stiglitz(HOLDS ×3)
- 全部逐字确认。要点保持:λ 是内生输出;不存在均衡的极限结果由噪音→0 驱动(误用警告);Conjecture 7 是薄市场(成交量)主张;「更被动→主动更好赚」是对等式条件的换质位推理,论文未写出。

## V11 GP + Bond-García + Chabakauri-Rytchkov(2 HOLDS + 1 小修)
- GP:被动成本下降→无效率上升尤其宏观 = **Proposition 7**;信息成本下降→下降尤其宏观 = **Proposition 6**(摘要枚举的 (4)(5) 与命题号不同,引用时说「摘要第 (4)/(5) 条结论」或命题号,别混);「25 年两力并存净预测模糊」是本文综合,须归本文;GP 自己把两趋势排成先后(信息成本 80-90 年代、被动成本 2000 年代)。Pedersen AQR COI 披露✓。
- Bond-García:参与=战略互补、自我强化、welfare 上升✓(RFS 2022;引文出自 2019 WP 稿)。
- C-R:标题《Asset pricing with index investing》;模型中指数化**降低**市场波动率、无信息量主张✓。

## V12 HHL
- 81.4%→59.5% 是**个股市值中主动投资者持有的份额**(弹性分类、跨股中位数),不是 13F AUM;13F 覆盖约 80% 美股市值、无法区分同一机构内的主动/被动。
- 发表版:χ=2.97(SE 0.47)、pass-through 33%、抵消 2/3、效应 11%、$2.5→$2.8;WP:χ≈2.15、60%、15%(摘要)/13%(正文自算)——WP 自相矛盾。别写「评审改小」(无证据),写版本演变即可。
- 「32%」是 log 变化(ln(59/81));简单比例是 27%。
- 观察到的总弹性下降 0.41→0.27(≈34%),被动只解释其中 11%——其余归主动投资者自身弹性变化。
- 词汇陷阱:HHL 自称「aggregate elasticity」=单只股票上跨投资者聚合,仍是微观对象;脚注 37 明确与 GK 宏观对象区分。
- 二手引用错误实例:T. Rowe Price 2024-08(15%+「markets」);UCLA Anderson Review(15%/50%)。Apollo 2024-11 已用对 2.97/33%/11%。窄口径(被动基金市值份额)对应 6.3%(发表)/8%(WP)。

## V13 乘数文献(重组该节)
- **三篇不构成一个「转向」**:KRY=静态均衡对比(2020 年已流传,RES 91(4) 2024 发表),贡献是「价格效应大(14% 截面重定价,非市场水平)、信息量效应小(仅 BPS 度量,标准化系数 0.049)」;不撤回非弹性——价格效应大恰恰支持非弹性。
- van der Beck:**已发表 JFE 184 (2026) 104337**;股票层面乘数短期 ~3 → 长期 ~1(摘要 3×,导言 4×,写 3-4×);是**微观**对象(自称 GK 标量乘数的 cross-sectional pendant)——「GK 5-7→长期 2」的映射必须删除或明确标注为本文自算且对象错配。其短期 3 本身已低于 GK 宏观 5-7。
- GK 自己的 Figure 4:累计冲击 4 个季度内「fairly stable」——总量层面「transitory」叙事的反证;但置信区间随 horizon 变宽。
- Hartley-Gerding:**不可达**(SSRN 403,无镜像)——只能引 Hartley 2025-06-10 公开帖子原话(短期可非弹性、长期弹性、乘数不如文献说的高或持久);未过审、零引用;Hartley 本人是该文献的公开批评者(利益方)。summarizer 编造警告(第 3 起)。
- Fuchs-Fukuda-Neuhann 2025 对需求系统估计的方法学批评存在,可作脚注。

## V14 BPS + FMVV
- BPS 度量:b×σ 的**平方根**口径(σ 是 log(M/A) 的截面 SD,不是盈利的);60%/80% 是趋势回归(1960→2014;导言写 2010——论文自身端点不一致,安全写法「1960–2014 样本上 60%(3 年)/80%(5 年)」);marginal R² 同向上升(别写「不用 R²」)。
- footnote 2 必须带后半句:「decline is concentrated at the short horizon, so again there is relative improvement at the long end」。
- 前史:FRBNY SR 578(2012-10)已结论「stable」;NBER WP 19728(2013-12)同;发表版反转,footnote 7 自述(通胀调整是消除 70 年代的向上偏差)。
- FMVV:「eviscerated」只在 WP、指**整个市场**非小盘;发表版(RFS 2022)数字:S&P 500 5 年期 +70%、非 S&P -80%,且整块降级到附录 E 并自带免责声明(reduced-form 难解释);上升仅限**大盘且高成长**;成员身份:趋势=规模效应非指数效应(稳健),水平效应两个检验方向相反(别说「membership 无作用」)。
- **样本止于 2010**——早于被动主升浪,不能用于裁决其后。
- Dávila-Parlatore(RFS 2025/2026)正面攻击 BPS 度量(不能分离信息聚合与基本面波动)。scratchpad 的 fmvv.txt/farboodi.txt 都是 WP 版。

## V15 CHR
- **-14.1% 是论文自己导言的数字**,与自己 Table IV 的 -24.8 log points(205→159/日,-22%)不一致——这是论文内部矛盾,不是引用者错(我们原稿的指控须反转)。
- into-R2000:EDGAR 与分析师报告都只 p<0.10;Google SVI 两个方向都不显著(摘要过强)。out-of-R2000 更有力(EDGAR +20.3**、分析师 +14.3***)。
- 正效应表:idio vol 最弱(+0.064*,t=1.7;且该列定义是**总**日波动率);turnover +12.1%***;short interest +1.9pp(≈相对 +19%)。
- AVR 数字标注:4 天下带(-0.017/SD 0.413/MDES±0.068);8 天下带另有一组。
- Figure 5:被动指数**基金**持股占市值 2%→11%,VR 1.16→1.10。
- **版本反转**:2017-10 稿结论相反(「index investing introduces noise」、VR 恶化约 30%)——发表版是修订后结果;引用一律标 2022。
- LATE 声明须带作者的反向限定(「model's predictions hold for any feasible level」)。
- 首阶段幅度多口径:1.5pp(结果节均值;分带 +1.81/-1.16)/导言写「约 2%」——引 1.5pp 归结果节。
- 优先引 Table IV 的 log-point 数(-24.8/-10.8;+20.3/+14.3),导言的百分数不稳定;-10.8 是分析师报告降幅,+14.3 是反向面板的升幅(没有 -14.3)。
- 补强:Ringgenberg 2026-06-25 国会证词重申结论未撤回;其个人页预告《A note on Russell-based methodologies》(未验证)——若发布可能影响整个 Russell 设计文献。

## V16 Sammon
- 「CHR 显示信息 2 天内完全入价、无 drift」**错**:CHR 发现样本平均存在显著 PEAD(BetaPEAD 4.3%,SE 0.6%),零的是指数化的**处理效应**。
- 「timing 和解」出自 Sammon 2023-03 稿、针对 BPS/Dávila-Parlatore,不是针对 CHR;发表稿只把 CHR 列为「无关系」文献。写法:两者确有张力,timing 是 Sammon 提出过的和解思路,本文采纳并标注为本文的综合。
- reduced form 弱点用附录原话:「almost always insignificant」+一个工具「consistently insignificant」。
- IVD 序列 1996 起(OptionMetrics);Figure 1 是 value-weighted 序列而 476bp 均值是 equal-weighted;152bp 是 pooled panel(1990–2019)系数应用于 2019 分位差。
- 引用:Management Science 71(6) 2025, 4582–4598;网上 PDF 是 2023-10 WP;2023-03 稿是几乎另一篇论文(不同度量、16% headline)。
- 他的 Passive 度量只含显性指数基金(脚注 16 自认漏 shadow indexing)——15% 别当真实被动份额(Chinco-Sammon 33.5% 是他自己的姊妹篇)。
- KNS 用同一 price-jump 度量得反号,Sammon 脚注 8 以 shock 污染回应——如实呈现。

## V17 BDFM(未决项已裁决)
- **发表版 JF 摘要没有 16%**;headline 是「risk premium of up to 56 basis points monthly」。16% 的口径错误**源于作者自己的 WP 摘要**(NBER 页至今如此)——发表时被删掉,这本身是更有意思的事实。
- 16% = 20bps ≈ 均值 2.08% 的 **10%**(16% 是对 SD 1.29pp);仅 S&P 500 股票(SD 1.44pp);R3000 稀释到 5% of SD。
- 发表版主识别是 Russell RDD,作者 2019 note 自述幅度「about 31% of a standard deviation」。
- **45% 反转→约 55% 永久的说法必须删**:发表版(数据到 2015)Internet Appendix 写「the price impact of flows is fully reversed」、半衰期约 10 天。
- 效率恶化「both intraday and at the daily frequency」(15 秒 + 5 天 VR),别写只有微结构。
- 这是 ETF 论文:指数共同基金系数小一个数量级。
- Semantic Scholar 在发表 DOI 下挂 WP 摘要——来源陷阱。

## V18 JVZ(1 HOLDS + 2 修)
- 超额收益=**相对指数**;样本 1996Q2–2020Q4(99 季);placebo 是 S&P600 前 60 只、系数为负不显著、样本更短(77 季)——是低功效未拒绝,不是证明为零。
- 29%(论文亦写 30%,同一数)是作者的线性外推(同期关联、可部分均值回归);模型对应物 0–4%(对象是 size group 5 vs 3-5 均值、且校准用了大得多的被动迁移)。
- 被动度量很窄:S&P500 跟踪 MF+3 只 ETF,2020 年累计仅 4.95% 指数市值。
- 理论亦有总量含义(纯主动→被动切换也抬升总市场,校准 1.47-1.68%)+噪音交易者失价加剧——别写成纯相对主张;但**不是信息通道**(information symmetric),不能当价格发现证据。
- idio vol:只有 top-50 交互项显著(t=2.53),非 top-50 主效应 t=1.21 别报 +1.86%。
- 引用:RFS 38(12) 2025, 3461–3496, doi 10.1093/rfs/hhaf085;NBER WP 无 size ladder 与 29%,不可混引。

## V19 Greenwood-Sammon(大修组)
- **用发表版 Table 1**:additions 3.42(80s)/7.39(90s)/5.16(00s)/0.83(2010s, ns);deletions -4.64/-16.11/-12.39/**-0.62(ns)**;deletion N=39/56/85/87。7.25/5.14/0.804 是 2023-06 WP 的 Table 2。
- 摘要的「deletions +0.1%」与自己的表(-0.62%)矛盾——摘要错误,非版本符号翻转;另有 DASH/HBS 元数据「0.3%」变体摘要流传。以表为准。
- migrations:发表版「~50% of additions → over 70%」且 additions 份额大致平稳(90s 69.07%→2010s 63.40%);**暴涨的是 deletions 的 migration 份额 5.88%→87.36%**(WP 的「40%→80%」已废)。
- 流动性提供者:**不是主动共同基金**(其净需求≈0),是 13F/S12 之外的机构(对冲基金/养老金/捐赠基金);零售亦被排除。
- direct additions 2010s = **5.4%**;Tesla 公告至生效 +53.35%;ex-Tesla 2020 平均 -3bp✓。
- 2020 中位数:trackers 买 7.53% 股本,机构持股仅 **+0.65%**(WP 的 -0.75% 已被发表版符号反转);全样本均值 3.04%。
- 结论归因:migrations + 市场流动性供给能力上升(Lo 适应性市场),predictability 角色小;McLean-Pontiff 只是类比——别当 headline 解释。
- BSW 优先权限于 additions(1997–2017),Preston & Soe 2021 记录了双向。
- **2025 复活实证(已核)**:COIN 公告次日 2025-05-13 +23.97%(市调 ~23.3%;公告至生效 +27.4%);HOOD +15.83%、APP +11.59%(2025-09-08)。三例都是 direct additions、样本外、无同行评审重估——qualify 而非推翻「消失」结论。

## V20 Comovement
- BSW 0.326/-0.319 是 1976–2000 全样本日频双变量;分期双变量 0.286/0.357。
- CSW 2001–2012:**原始 beta 仍升**(S&P +0.071 显著、非 S&P +0.075),差分 -0.004(t=-0.14)——写「升幅不再超额」;样本止 2012,别说覆盖其后被动主升。
- BIS 0.45→0.52 是原始相关性无对照(2000-01–2017-09);ECB +0.005/1pp 是面板 FE(IV 只是稳健性)、含 AR(1) 的短期系数,「10pp→+0.05」是本文外推须标注。
- Anadu Table 4 的「declined significantly since 2001」是对 CSW 的转述,且正文说证据 mixed(Kamara-Lou-Sadka、Bolla 等 beta 上行)。
- **新反证(必须收录)**:DeCoste, Global Finance Journal 65 (2025)——fuzzy RDD 发现长期显著正超额联动,称 CSW 的零是新老成员异质性所致;另 Liao-Coakley-Kellard (IRFA 2022) 分解出 beta 套利者反向力。**联动文献未定案**,按方向存争写。

## V21 脆弱性事件
- 伞形结论收窄为:「没有官方尸检把这些事件归因于**被动持有份额的增长或指数基金资金流**」;监管方确实归因于 **ETF 交易/套利层**的机制(2010「one of the reasons」+订单簿薄;2015 关联性且 SEC 明示不作因果结论)。
- 可验证的负面事实:SEC 2015 note 全文零次出现 passive/index fund/indexing;2010 报告的「passive」仅指被动做单。
- 事件数:五个(含 2025-04)或「四个经典+一个近例」。
- 2018:BIS「a key factor」于午后 VIX spike(非全日抛售的原因);$4bn 是「select」四只产品;「非代表性」句在 Graph A1 脚注。
- 2020-03:BIS 两面都写(套利受阻 + 「arguably」运行威慑);「price discovery」是 BlackRock 语言;BlackRock deck 标注:Madhavan, EII Global Research,FIMSAC 2020-10-05 第三方材料。Fed FSR 引语必须含「arising from poor performance」。
- 2015 数字:SPX -5.2%(max decline)vs SPY 开盘 -5.2%、9:35 低点 -7.8%、收盘 -4.2%;327 vs 315 两处计数并存,用 SEC 自己的百分比别自算。
- 2025-04:BIS 说 retail 非 institutions 买入;75% 反弹归因非关税消息是 VAR 分解,别与投资者类型混。2010 报告的触发叙事需注 Sarao 起诉补充。

## V22 SPIVA
- MY2025(一手,数据至 2025-06-30):1 年 72.61(=截至 6/30 的 12 个月)/5 年 86.91/10 年 85.98/15 年 88.29/20 年 91.03;All Domestic vs **S&P Composite 1500** 20 年 93.81;风险调整 10 年 94.39。
- Exhibit 1 = 2001–2024 共 24 个整年 + H1 2025;跑赢多数年:2005(49,舍入边缘)/2007(45)/2009(48,舍入边缘);趋势:OLS +0.235pp/年、r²=0.025,半样本均值 62.8→67.1——「基本平坦、微弱上漂」。
- 存活分解(15 年,1,033 只):50.05pp 未存活 + 38.24pp 存活但输 + 11.71pp 存活且赢;存活者中仅 23.4% 跑赢。别写「死于跑输」——死亡基金生前是否跑输正是争点。
- YE2025 全部二手(79%、fourth-worst 是 S&P 自家 YE 文本用语,媒体引号只包 79% 句);H1 54%「best year since 2022」与全年 79%「fourth-worst」同年反转必须并列呈现;S&P 自家归因是大盘集中度(且 2025 年内 top-5 贡献从 78% 线性降到 11%——集中度下降的年份主动反而第四差,内伤)。
- EW -1.96pp vs AW -1.25pp(20 年,年化净额,非 alpha)。

## V23 Morningstar Barometer(twist 反转)
- **同类对比下 SPIVA 更狠**:SPIVA Large-Cap Core 10 年 96.57% 跑输(3.4% 成功)vs Morningstar Large Blend 8.1%;Morningstar 自家同类聚合是 p.6「Just 10% survived and beat over the decade」。「修正 costless benchmark 反而更狠」必须删——投资净费基准使门槛**更低**(CFR:81→73%),Morningstar 的被动组合 14.5% ≤ 指数 ~14.8%。
- 方法学自相矛盾:asset-weighted(定义+takeaways)vs equal-weighted(下一段+附录 C)——引 asset-weighted 并注明报告不一致。
- Morningstar 全文未提 SPIVA——对比是本文的分析,须如此标注。
- 数字确认:21% 10 年、38%/37%(1 年全体/美股)、8.1/3.6/20.3、EM 29.1、Corp bond 52.2(但 2025 单年 4.4——单年是噪音)、9,248 只/$26T≈67% 美国**基金市场**。
- 保留反向亮点:「过去 10 年,平均美元投资在 20 类中 17 类跑赢平均基金」;最便宜五分位 31% vs 最贵 15%。

## V24 Persistence(1 票已到,2 票补跑中——暂按此稿)
- 0.39% 基线是本文自算(S&P 只印 6.25% 两种 null);零 vs 期望 2 只:P(0)≈13.5%,与随机完全一致——「zero」不是超随机信号。
- 死亡不对称(YE2024 精确值):Q4 24.89% vs Q1 6.81%(国内股票,n=470/quartile;固收 30.00 vs 10.00);风格漂移近对称(28.72 vs 25.11)。
- 0.46%(YE2025)只可归 VettaFi/Advisor Perspectives 2026-05-08 二手;YE2025 据二手另有:2023 top-quartile 短期持续 28.9%(vs null 6.25%)、小盘 2.4% 非零——「not a single fund」对 YE2025 cohort 不成立。别混 vintages。

## V25 IAA/Ptak(2 票已到)
- 92.04→55.31 是 12 类平均;All Domestic 20 年是 94.11→77.56;摘要 79%→56% 是 All Domestic 1 年(2024)。三个口径别串。
- 71.34%/92.04% 标「作者复现基线」;S&P 自家发表值 92.66%/76.00%。复现在美股匹配到 0.6pp、固收差 ~7pp——Ptak 最强点即在此:IG intermediate 类 37pp 改善的近 1/5 是复现误差(61.33→54.34→23.91),**该表述限于该类**。
- 「supported by」IAA Active Managers Council(IAA 的主动管理倡导部门);Cremers「independent director/advisor」保留 independent;S&P 曾付 Cremers 团队 $15,000(SPIVA 奖二等)——双向 COI 都写。CFMS 2016 结论是「explicit indexing improves competition」,别称 pro-active。
- Ptak:高收益普查是 Morningstar 类别代理(他自己说没有 SPIVA 数据);2,844/4,518 是总基金月(headcount 效应),每只 88.9 vs 98.2 个月(1.10×)——「活得近两倍久」失实;其文内日期/口径自相矛盾(正文 2004 vs 图注 2014,以正文为准);他披露了 Barometer;死基金=失败是定义分歧非实证驳倒。
- S&P 无方法学回应文档(仅公关声明);论文仍未发表(md5 与 5/4 稿一致)。

## V26 G-S 收益率检验(1 票已到)
- PST:IndustrySize=主动美股**共同基金** AUM/市值(1979 2.4%→2008 峰 18.6%→2011 16.8%),别叫 active share;40bp=主样本(1993–2011)OLS-FE,扩样本(1979–2011,含主样本)~20bp。**必须披露 CFR 交锋**:Adams-Hayunga-Mansi (CFR 2022) 称 post-2001 工业层面规模不经济消失(168 条错误观测);PST+Zhu 同期回应(robust regression 确认原结论)——外推「主动缩水应抬升 alpha」须带此未决注。
- FF2010:样本 1984-01–2006-09;H&L 批评针对**截面 bootstrap**(个体基金层),不动摇总量 VW alpha;补 H&L 原话「in our simulation」与其建议(修正实现而非推翻);KTWW 反向过度拒绝。
- BvB $3.2m 是**时间加权**(按存续期数加权)非 AUM 加权;无权重截面均值 $0.14m/月;中位数负、57% 为负✓。
- CFMS 系数是 Panel B(country of sale);Panel A 不显著、经由指数化成本通道。
- Unterberg:全部二手(SSRN 2026-06-19 挂出、6-29 修订、68 页、未过审、全文没人读过);「符号翻转」只在 Morningstar 总结第 6 条——要么明确归 Morningstar 转述、要么删;奖项按作者页「Brattle Group PhD Candidate Award, WFA 2026」(Green 的「Two Sigma Award」说法与之冲突);机制自述是需求/价格压力而非技能衰退,不是 G-S 信息效率证据。

---

## V24 Persistence(×3 CORRECTED)
- 0.39% 基线是本文自算(S&P 只印 6.25%);Poisson(2) 下 P(0)=13.5%——「zero」在随机零假设内毫不异常;top-half 存活调整后 null≈5.7%。
- 死亡不对称:Report 5(国内股票,2014-19 排名→2019-24 观察,n=470/quartile):Q4 24.89% vs Q1 6.81%;各类别不一;风格漂移近对称(25.11 vs 28.72)且体量更大;Report 11 是固收(30.00 vs 10.00)。**同时**:CFR 指出 Report 5 是对同行排名非对基准,死亡≠输给基准。
- **0.46%(YE2025)判死不得刊出**:一手不可达、唯一二手是疑似机器生成 FAQ、另一二手读同表得 0.00%、且 0.46% 出现在我们喂给搜索的查询里(回声污染)。YE2025 只可写「据二手读表:除小盘外全部类别归零」并标二手。
- 反向证据必须收录:YE2024 Report 5 显示 5 年期 top-quartile 留存 54.76%(vs 随机 25%)——长窗口的「无持续性」不适用于五年期同行排名;小盘 2022-12 仍 0.79%。
- Report 2 是等权基金计数;分母是 2020-12 cohort(512/1021 等)。

## V25 IAA/Ptak(×3 CORRECTED)
- 「1/5 是复现误差」限于 investment-grade intermediate(61.33→54.34→23.91);固收类整体 71.34→37.09(34.25pp),且 71.34 是**作者复现值**(SPIVA 自印 76.00——复现在固收整体差 4.66pp,Ptak 的批评适用于整条固收线)。
- 口径阶梯:92.04/92.66/55.31 = 12 类等权平均;All Domestic 20 年 = 94.11→77.56;摘要 79%→56% = All Domestic 1 年(2024,56.49)。三层不可互串;55% 是论文自己印的两个数字里更有利的那个。
- 「supported by」IAA Active Managers Council(IAA=注册投顾总会,AMC 是其主动管理倡导部门);Cremers「independent」保留;SPIVA 奖=2014 年第三届二等奖 $15,000,获奖论文结论是「显性指数化改善行业竞争」(**亲指数化**——讽刺点是 S&P 奖励过他,不是奖励反指数化)。
- Ptak:**承认第三项调整**(基准改投资净费被动基金——Barometer 已做 2/3 项:基准+资产加权);他守的是死亡=失败与等权两项;41% 的死亡 HY 基金生前跑赢(部分支持 CFR);2,844/4,518 是总月数(headcount 效应,每只 88.9 vs 98.2,1.10×);其文正文 2004 vs 图注 2014(以正文为准);8.3 年 vs 加总隐含 7.9 年不调和。
- S&P 的正面回应存在(WealthManagement 引):SPIVA 测「基金比例 vs 市场基准」因为检验的主张是 beat the market——范围之争非方法让步。CFR 未发表。

## V26 G-S 收益率检验(×3 CORRECTED)
- BvB $3.2m/年 = **按存续期数加权**(时间加权)非 AUM 加权;无权重均值 $0.14m/月;median -$20k/月、57.01% 为负✓;作者自注 t 值高估(跨基金相关+超峰);BvB 的 VW gross alpha ≈+80bp/年(对 Vanguard 基金基准)与 FF +13bp(对因子)**不同基准不可并列**;FF 净 VW -0.81~-1.00(t -2.5~-3.0)才是「alpha=-fees」的支撑。
- PST:论文框架是 Berk-Green 规模递减,不引 G-S——「G-S 检验」的联结是本文的,须标注;IndustrySize=主动美股共同基金 AUM/CRSP 总市值(排除对冲基金/主动 ETF/专户);40bp=主样本(1993-2011)FE 谱(t=-3.60),无 FE 约一半且勉强显著;扩样本加时间趋势后 t=-1.72 不稳健;样本止 2011-12,post-2010 推断是本文外推且需另证主动份额确实下降;**CFR 交锋必须披露**(AHM 2022 vs PSTZ 2022 robust 确认)。
- CFMS:Panel B(country of sale)才显著;净四因子 alpha;2002-2010(同样早于被动主升);在样本均值 Active Share 0.705 处组合边际效应≈0——「指数化多→alpha 高」只对贴基准基金成立;机制是竞争纪律(费用/努力)非错价机会。
- Unterberg:一切数字归 Swedroe/Morningstar(2026-08)转述;作者摘要只可证「四因子 alpha 降约 1pp + Active Share 关系反转」;「行业层符号翻转」只在 Morningstar 转述第 6 条——归转述或删;奖项两说(WFA 程序册 Two Sigma / 本人页 Brattle)——写「WFA 2026 获奖论文」即可;机制自述为需求/价格压力**否认技能衰退**,不是 G-S 信息效率证据;Reuter-Zitzewitz(RoF 2021)RD 发现基金层规模效应≈0,若涉基金层须一并注。

## V27 费用(2 HOLDS + 1 修)
- 全部数字✓(1996 起点是图标签口径,如引注明)。
- 「无累计节费一手来源」**被推翻**:Vanguard《50 years, 50 facts》给出 25 年累计省费约 **$570bn**(厂商反事实口径:假设指数投资者原本付主动费率)——存在但是[厂商口径],引用须带构造。

## V28 Bebchuk-Hirst(×3 CORRECTED)
- 投票份额:25.4% mean 系 **2017** 年会(不是 2018);median 24.2%;R3000 mean 22.0%;wedge 解释用 2017 年非三巨头投票率 68%(73% 是 2008-17 均值、只用于投影假设)。
- 投影:**复合**(几何)外推 0.84%/年(非线性);34.3%(2028)/40.8%(2038)=投票;27.6/33.4=**所有权**投影且同出 2019 论文——「2022 下修」不存在,2022 原样重印并辩护。34.3 是三个基期口径里最高(5 年基期 28.4、20 年基期 27.2)。
- 2022 内部矛盾是三重:24.9%(1552/1569 页,fn118 却引 Table 2)vs Table 2 的 27.5(sum of rounded medians)vs 正文 27.6;21.9% 是**三个中位数之和**;别把 20.5%(2017 mean)与 21.9%(2021 sum-of-medians)接成增长序列——一致口径中位序列 19.5%(2017)→21.9%(2021)。
- **平台化**:2022 Table 1 中位合计 21.5(2019)/21.1(2020)/21.9(2021)——投影要求 2028 达 27.6,增长停滞未被作者处理;引投影必须并呈平台化。
- Figure 1 标题「index funds」但底层是 13F 全持仓(含主动;index 占比 BLK 66%/V 74%/SSGA 79%)。
- 「<4 person-days/$1bn」是 BlackRock 专属(SSGA/Vanguard <2);2022 版重述漏了分母,别引那句。
- Kahan-Rock 重写:比较基准是基金**自身的经济所有者**(基金投资者),称 B&H 的假想集中股东基准为「category mistake」;他们并不否认 45/21/12 数字且承认 B&H 在自身条件下的点。
- S&C 18.7% = 「collectively owned 18.7% of all shares」(aggregate,非 value-weighted 修饰);88% 亦见 CamberView 2017/K&E 2019——行业通说,更支持「rank stat 非控制」的警告。
- 最新一手:BIS Annual Report 2025(日历年,12-31 数据):Voting Choice 合格 $3.76T/总指数股票 $7.7T、enrolled ~$885bn;BAIS 13 人→BlackRock stewardship 合计 ~73+;与年中 Spotlight($3.3T/$784bn/$6.9T,6-30)是不同报告期,不可混用。

## V29 Common ownership(×3 CORRECTED)
- **「Azar & Vives 反方综述」不存在**——镜像 COI 综述= Schmalz, ARFE 10 (2018) 413-448 及 ASt 自己的 Antitrust Bulletin 66(1) 2021 方法学辩护。Azar & Vives ECGI 827/2022 是实证论文,且其发现是**三巨头共同持股与更低机票价相关**(非三巨头股东才与高价相关)——放进正文反而是妙料。
- GLS 已发表:Annual Review of Financial Economics 16 (2024) 89-114(怀疑方已过审;Atlanta Fed URL 死链);引语必须带范围限定(「Across the newest papers employing the most credible identification techniques…However, further research is necessary」)。
- ASt 数字锚定 2017 IESE WP/发表版:3-7% 面板、10-12% BGI-IV(pooled;分期系数多不显著;ASt 自称「may be 10-12%」)、~0.5% 直接效应;JF 摘要唯一数字是浓度「10 倍于门槛」;ASt 在 Refutation 中自认面板估计**不主张因果**。
- DGS:敏感于 investor control 度量+破产假设;三个 placebo;发表版用 HHI∆ 记号。
- 更多批评线:Egland et al.(SSRN 3463231,Analysis Group,COI 在怀疑侧)、Kennedy-O'Brien-Song-Waehrer 2017(结构模型)。BCS tunneling 归谬自带「对 control weights 敏感」警告(反而强化归谬用途)。
- 交锋 Refutation(亦 CESifo 9937/ECGI 837)与 Surrebuttal 均未过审✓。

## V30 2025-26 治理事件(×3 CORRECTED)
- Texas v. BlackRock:2025-08-01 是**部分准许部分驳回**(Counts I-XVII、XXI 存活;XVIII-XX 驳回;消费者保护限四州);「a close call」专指circumstantial conspiracy pleading;operative 是 2025-01-16 修正诉状(13 州);Vanguard 和解 = 2026-02-25/26、11 州、$29.5m;§4.1 是**总量 50% 门槛**(非「任一基金过半美股」);承诺至 2032-06。
- **删「listen-only」**(仅 summarizer 出现);BlackRock 于 2025-02-20/21(Reuters)恢复,写「一周内、2 月下旬」;其自述是「highlighting our role as a passive investor at the start of each engagement」。
- 拆分:每家**两队**(BIS/BAIS——BAIS 2025-01-01 已存在,早于 2026 叙事;Vanguard VCM/VPM;SSGA AST+可选 SSS);「<5%」是 Innisfree 的概率式措辞非设计上限——EDGAR 实测:Vanguard 是(Macy's 4.96/4.94)、BlackRock 否(NETSTREIT 13.9%);拆分高度不对称(BIS≈90% AUM、VCM≈75%);**Innisfree 实测「两队常平行投票」**(推翻「尚无证据」);Cooley:VCM/VPM 美国政策除覆盖基金外「identical」。「统一票仓失效」降级为「法律形式分拆、行为尚未分化」。
- Engagement:同类比 1,950 公司/12,700+ 公司 ≈15%;但同报告另一口径「~70% of the value of clients' equity assets engaged」——两个都给;BIS 数字仅覆盖 Benchmark Policies(约 3/4 AUM)。
- Vanguard 参与率:82,000 人是 8 基金/$264bn 期的数;~10M 合格是 2025-05 扩容后的前瞻数——0.8% 混期;Vanguard 自家口径:直接经纪客户参与率≈10%、资产口径 $9bn/$264bn=3.4%。写明分母。
- FTC/DOJ SoI:明确不就 acquisition-only 理论表态——双向都不许过度解读✓。

## V31 指数编制商(×3 CORRECTED)
- IA-6050:**2025-04-21 正式从 Unified Agenda 撤下**(RIN 3235-AM95,「Completed Actions」)——写「问了、然后正式撤回」,别写「不了了之」;2025-06 的 14 项撤回是另一批(它未到 proposal 阶段);2026 议程(2026-07-03/07)无此项。
- $5.0bn = **全行业** 2021 指数收入(SEC 脚注引 FT/Burton-Taylor),前三家 >2/3 ≈ $3.4bn;3.05M 指数 = IIA 2020 survey;fn44 自引 Kasch-Sarkar 反方——RFC 本身不是 SEC 对指数效应的背书。
- An-Benetton-Song(JFE 149(3) 2023, 407-433):发表措辞「over one-third of ETF **expense ratios**」(31.4%→35.7%,2010→2019);「improving competition…reduces expense ratios by **up to** 30%」= 完全竞争基准(9.3→6.5bp,作者自称 unlikely);**进入反事实显示新低价编制商几乎不动费率**(市场自愈失败,引 Morningstar Open Indexes 佐证);现实情形约 6%/13%;估计基于 ~10% 自愿披露子样本(选择偏差自认);HHI 3,294 = 2010-2019 月度均值、美股 ETF 市场。
- Molk-Robertson:1.7-7.5% 是 **round-trip**(单边 0.85-3.75%),mean 2.9%/median 1.8%,仅五只 >$100bn 基金;$61.5bn = $30.7bn 单边×2,其中五大基金占 ~$52bn;删「≈0.5%」(对 S&P 500 基金资产是 ~2-3%;0.5% 用错分母);98.9% 基金季 <20% active share——**不支持**「巨型基金暗地主动」强读法;flow 检验作者自称仅 smell test。
- RA Tesla:$94bn 与 $78bn 矛盾在**同一句**($4.6T×1.69%=$77.7bn,$94bn 无支撑);$147bn(endnote 算术对)vs $154bn(正文);$4.6T 是 **YE2019** 基数套 2020-12 事件;41bp=假设组合六个月收益差(RA 自称 cost——纠正其标签);RA 无 COI 披露段(写「未披露的商业利益」);PDF 已迁 rafi.com;两次再生成 PDF 未改错。

## V32 BoJ/监管注意力/FCA(2 HOLDS + 1 修)
- **「¥110 万亿 unsourced」被推翻**:Nikkei 2026-06-07 报道 BOJ ETF 市值超 ¥110tn、超 TSE Prime 8%(AI/半导体行情推高);序列 ~¥70-80tn(2025-09)→¥95tn(Nikkei Asia 2026-02-10)→>¥110tn(2026-06)是市值升值的一致轨迹。写「Nikkei 报道口径」。
- Fed 2026-05 FSR 零提及✓;FCA/Bristol 判词逐字✓;BoJ 声明逐字✓、~330bn/年账面、Ueda「more than 100 years」✓。

---

## Round 2 总盘点(96 票)
- 组级:V10 全票 HOLDS;V11/V27/V32 多数 HOLDS(含小修);其余 28 组 CORRECTED;0 组整体推翻。
- 子项级判死/不得刊出:0.46% persistence(YE2025)、「45% 反转→55% 永久」(BDFM WP 旧数)、「listen-only mode」、「Azar & Vives 综述」、「40%→80% migrations」、「~50pp 死于跑输」读法、JVZ 非 top-50 vol 主效应、my「Morningstar 修正后更狠」、「M≈5-7→长期 2」映射、「0.5% of index assets」。
- 本文自身论证被验证反转的(写进正文):①「-14.1% 是引用者误引」→实为 CHR 论文内部矛盾;②「Morningstar 修正 costless benchmark 反而更狠」→同类对比 SPIVA 更狠、投资净费基准更宽松;③「主动共同基金提供纳入流动性」→其净需求≈0,提供者是对冲基金/养老金/捐赠基金;④「migrations 从 40% 升到 80%」→additions 份额平稳,暴涨的是 deletions;⑤「BoJ ¥110tn 无来源」→Nikkei 有报道;⑥「三巨头拆分后无投票行为证据」→Innisfree 实测平行投票;⑦「无累计节费一手来源」→Vanguard $570bn 存在(厂商口径);⑧「2022 下修投影」→不存在。
