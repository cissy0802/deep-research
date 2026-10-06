# PHYS-neocloud-power — 算力租赁与电力/数据中心层(截至 2026 年 10 月)

调研日 2026-10-05。来源分级:官方=SEC 原文/公司新闻稿;指数=Silicon Data 等独立指数(仍为商业机构自报方法论)。

## A. CoreWeave(neocloud 代表)

P1 [官方 SEC 8-K EX-99.1, 2026-08-11] Q2 2026(截至 2026-06-30)收入 $2,575M(去年同期 $1,212M);GAAP 经营亏损 $(49)M;净利息支出 $(640)M;GAAP 净亏损 $(626)M;non-GAAP Adjusted EBITDA $1,510M(59%);Adjusted operating income $128M(5%,去年同期 16%)。
原文: "Revenue $ 2,575 $ 1,212 Operating expenses 2,624 1,193 Operating income (loss) $ (49) $ 19 ... Interest expense, net $ (640) $ (267) Net loss $ (626) $ (290)"
URL: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm
口径注:59% EBITDA 与 -2% GAAP 经营利润之差 = 折旧摊销 $1,393M(单季,占收入 54%)+SBC。利息 $640M ≈ 收入 25%。"带杠杆的折旧套利"在财报结构中直接可见。

P2 [官方 SEC 8-K, 2026-08-11] 资产负债表 2026-06-30:recourse debt current 6,235 + non-current 25,170;non-recourse current 1,278 + non-current 2,385 → 有息债务合计约 $35.1B;另经营租赁负债 $16.3B;股东权益仅 $5.0B;累计亏损 $(4.0)B。H1 2026 资本开支 $14.1B vs 经营现金流 $3.66B。
原文: "Recourse debt, non-current 25,170 14,608 Non-recourse debt, non-current 2,385 57" ; "Purchase of property and equipment ... (6,422) (2,453) (14,117) (3,860)"

P3 [官方 SEC 8-K, 2026-08-11] 收入积压(backlog)约 $104B,另有早 Q3 >$25B 新签未计入;10-Q 中 RPO $103.7B,41% 在 24 个月内确认,其余到第 78 个月。口径:承诺额,非落地;"subject to the satisfaction of delivery and availability of service requirements"。
原文 10-Q: "As of June 30, 2026, the Company had $ 103.7 billion of unsatisfied RPO, of which 41 % was expected to be recognized over the initial 24 months ending June 30, 2028"
URL: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm

P4 [官方 10-Q / 10-K] 客户集中度:2025 全年 Microsoft 占 67%;Q2 2026 前三大客户分别 36%/26%/10%(Q2 2025 最大客户 71%)。OpenAI 承诺约 $6.5B(至 2031-05)等多笔;Meta 2026-03 新增最高约 $21.0B;Jane Street 约 $6.0B。
原文 10-K: "We recognized an aggregate of approximately 67% of our revenue from our top customer, Microsoft, for the year ended December 31, 2025."
原文 10-Q: "We recognized an aggregate of approximately 36%, 26%, and 10% of our revenue from our top three customers for the three months ended June 30, 2026"
URL 10-K: https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm

P5 [官方 10-K] 技术设备(GPU)折旧年限 6 年(2023 年起由 5 年延长至 6 年);承诺合同通常 1-6 年 take-or-pay。
原文: "Effective January 1, 2023, the Company changed its estimate of the useful life for its computing equipment utilized in data centers from five to six years"
含义:若 GPU 经济寿命 < 6 年(租价跌速快于直线折旧),账面利润被高估;反之 take-or-pay 合同覆盖期决定回收风险。

## B. GPU 租价时序(独立指数 = 商业机构自报方法论)

P6 [指数/Silicon Data 博客, 2026-01-09] 历史区间:H100 云租价从 2024 年初约 $8/h 跌到 2025 年末 $1.50-3.00/h;2025-12-09 基线 $2.00/h → 2026-01-06 $2.20/h。
原文: "H100 cloud rates plummeted from around $8/hr in early 2024 to the $1.50-$3.00/hr range by late 2025"
URL: https://www.silicondata.com/blog/h100-price-spike

P7 [从业者/分析机构 SemiAnalysis, 2026-04-02] H100 一年期合约租价从 2025-10 低点 $1.70 升至 2026-03 $2.35(+~40%);认为更高租价延长 GPU 经济寿命;"GPU rental pricing is more likely to continue rising than falling"。
原文: "H100 1-year GPU rental contract pricing has shot up almost 40% from a low of $1.70/hr/GPU in October 2025 to $2.35/hr/GPU by March 2026."
原文: "higher rental rates extend the economic useful life of existing GPUs"
URL: https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity

P8 [指数/Silicon Data, 2026-10-05] SDH100RT(neocloud H100)当日 $2.81/GPU-h,7 日 +2.9%;2026-03 H100 hyperscaler 指数约 $7.43-7.52/h(几乎不动),neocloud $2.43-2.63/h;B200 指数 2026-03-30 为 5.48(年初 4.40,3 月均值 $5.09/h)。
原文: "As of Oct 5, 2026 ... 2.81 USD / GPU-hour"; B200 "stood at an index value of 5.48" on March 30, 2026
URL: https://www.silicondata.com/products/silicon-index/h100 ; https://www.silicondata.com/blog/b200-rental-price-march-2026-update
口径注:hyperscaler 挂牌价 ~$7.5 vs neocloud ~$2.5-2.8,3 倍价差 = 品牌/生态溢价(或挂牌价≠成交价)。

P9 [媒体转述/Seoul Economic Daily 引 Ornn 交易平台, 2026-09-22] H100 小时租价一个月内 +21.9%,$2.69 → $3.28,约为 H200 的 70%;韩国 Vessl AI 将 H100 从 $2.39 提到 $2.98。
URL: https://en.sedaily.com/finance/2026/09/22/h100-rental-prices-jump-22-percent-in-a-month-as-gpu
判断:2023→2025 跌约 75-80% 支持"算力商品化";但 2025-10 起反弹 40-90%,说明 2026 年处于供给紧张期,租金暂回流到持有存量 GPU 的一方(含 neocloud)。周期性而非单调下跌。

## C. 电力层(公用事业/IPP)

P10 [官方 PJM 新闻稿, 2026-07-14] 2028/29 容量拍卖以 FERC 批准上限 $325/MW-day 出清(上一年 $333.44,亦为上限),低于可靠性标准 6,831 MW;总额约 $16.4B;明确提到数据中心大负荷进入负荷预测。连续三次拍卖撞上限。
原文: "The price came in at the FERC-approved cap, $325/MW-day (UCAP) for the entire PJM footprint"
URL: https://www.prnewswire.com/news-releases/pjm-capacity-auction-procures-138-318-mw-of-generation-resources-as-work-continues-to-address-growing-electricity-demand-302825613.html
口径注:上限(collar)由监管设定——说明电力稀缺租金的天花板是政治/监管决定的,不是市场决定的。2027/28 若无上限将出清在约 $530/MW-day(RTO Insider/Modo 等报道)。

P11 [官方 SEC 8-K, Vistra, 2026-08-07] Q2 2026 Ongoing Ops Adjusted EBITDA $1,767M(+31% YoY,去年 $1,349M);East(PJM)段 $642M vs $418M;驱动为"higher realized energy and capacity prices";GAAP 净利 $305M。2026 指引 $6.8-7.6B。同时宣布与 KKR/KIA/NVIDIA 成立 Helix Digital Infrastructure,Vistra 出资至多 $1.0B——发电商向下游数据中心延伸。
原文: "Ongoing Operations Adjusted EBITDA for the second quarter 2026 increased by $418 million compared to the second quarter 2025, driven primarily by higher realized energy and capacity prices"
URL: https://www.sec.gov/Archives/edgar/data/1692819/000169281926000017/vistra-20260630xearningsre.htm

P12 [官方 SEC 8-K, Talen, 2026-08-05] Q2 2026 Adjusted EBITDA $374M(去年 $90M);GAAP 归母净亏损 $(92)M(未实现衍生品损失+利息);2026 指引上调到 $2,025-2,225M;在 2028/29 PJM 拍卖以 $325/MWd 出清 >10 GW。
原文: "Adjusted EBITDA increased by $284 million primarily due to increases in energy and other revenues and capacity revenues"
URL: https://www.sec.gov/Archives/edgar/data/1622536/000162253626000065/a20260805q22026earningsrel.htm

P13 [官方 SEC 8-K, Constellation, 2026-08-06] Q2 2026 GAAP EPS $1.42(去年 $2.67),Adjusted Operating EPS $2.55(去年 $1.91);全年指引上调至 $11.50-12.50;新签 920 MW 核电长期 PPA,期限 15-20 年,2029-2032 起供;Crane(原三里岛 1 号机,微软 PPA)获 FERC CIR 转移豁免与 NRC 燃料许可,目标 2027 重启。
原文: "These agreements are for 15-20 years in duration and are set to begin in 2029 through 2032."
URL: https://www.sec.gov/Archives/edgar/data/1868275/000186827526000097/ceg-20260806991.htm
口径注:PPA 价格公司均不披露;只有卖方/媒体估计。

P14 [媒体转述 Jefferies 估算, 2024-09] 微软-Crane(三里岛)20 年固定价 PPA,Jefferies 估约 $110-115/MWh(远高于 PJM 批发电价),双方均未披露价格。
URL: https://tech.yahoo.com/business/articles/microsoft-may-pay-constellation-premium-223049148.html
口径:分析机构估算,非官方。

## D. 电力设备(燃气轮机/电网)

P15 [官方 SEC 8-K, GE Vernova, 2026-07-22] Q2 2026 订单 $24.2B(有机 +88%);燃气设备积压+槽位预订从 100 GW 增至 116 GW(53 GW 积压 + 63 GW slot reservation),预计年底 ≥125 GW;产能 2026 Q3 达 20 GW/年、2028 年 24 GW、2030 年 30 GW;总 backlog $176B。Power 段 EBITDA 率 18.8%(去年 16.4%);公司整体 Adjusted EBITDA 率 11.3%,GAAP 净利率 5.8%。订单增长"driven by higher volume and price"。
原文: "Gas Power equipment backlog and slot reservation agreements grew from 100 to 116 GW; now anticipate reaching at least 125 GW by year-end 2026"
原文: "Orders of $16.7 billion increased + 134% organically, primarily from strength in Gas Power equipment, driven by higher volume and price"
URL: https://www.sec.gov/Archives/edgar/data/1996810/000199681026000147/gevpressrelease2q26.htm
口径注:slot reservation 是"预订槽位"不是确定订单(承诺 vs 落地);积压按年产能 20-24 GW 计 ≈ 5 年排队——定价权真实,但利润率(11-19%)远低于 NVIDIA 级别;GEV 在主动扩产(2030 年 30 GW),约束在被拆解。

## E. 数据中心 REIT

P16 [官方 SEC 8-K, Digital Realty, 2026-07-23] Q2 2026 收入 $1.9B(+29% YoY);续约租金 cash +25.4%、GAAP +32.0%(创纪录);已签未起租 backlog $1.9B(100% 口径)/ $1.4B(DLR 份额);7 月签两笔超大规模租约年化 GAAP 基租 $410M;Core FFO 指引上调至 $8.15-8.20。
原文: "Rental rates on renewal leases signed during the second quarter of 2026 increased 25.4% on a cash basis and 32.0% on a GAAP basis."
URL: https://www.sec.gov/Archives/edgar/data/1297996/000110465926086270/dlr-20260723xex99d1.htm
口径注:>1MW(超大规模)续约 cash 价差 66.7%,0-1MW 仅 5.2%(媒体转述电话会/补充材料,未在 SEC 原文核对)——稀缺租金集中在"已通电的大块容量",即电力接入是被定价的东西。

## F. Nebius(neocloud 第二样本)

P17 [官方/公司股东信, 2026-08-12] Q2 2026 集团收入 $582.3M(+454%);AI cloud 收入 $575M;ARR $3.0B(口径:季末月 AI cloud 收入 ×12,run-rate 非确认收入);集团 Adjusted EBITDA $236.2M(41%),AI cloud 段 49.7%;GAAP 净亏损约 $(190)M(媒体转述);Q2 capex 约 $5.7B;2026 指引收入 $3.0-3.4B、ARR $7-9B。
URL: https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf

P18 [官方/公司股东信, 2026-08-12] 单位经济:Q2 四笔大单平均 TCV >$1B,"yield of $20-25 million per megawatt";70% 合同含预付款,覆盖 50-60% 对应 capex;回收期从 2-3 年降到 1 年 10 个月;短期(3-6 个月)合约与首次拍卖看到 $40-50M/MW 定价机会;"We could sell our entire 2027 capacity on these terms today."
原文: "the expected payback period for the associated capex and related operating costs for Q2 deals is 1 year and 10 months, down from our two-to-three year payback period previously."
判断:2026 年供给紧张下,neocloud 有真实议价权(预付款+提价);这是周期顶部特征,还是结构性,取决于 2027-28 产能释放。

P19 [官方/公司股东信, 2026-08-12] 会计口径变化:服务器/网络设备折旧年限从 4 年延长到 5 年(2026 起);D&A 占收入从 72% 降至 45%(部分来自会计年限变化,非纯经营改善)。
原文: "We use a five-year useful life for our server and network equipment based on usage patterns and current utilization commitments, up from the four-year useful life used prior to 2026."
口径注:与 CoreWeave(6 年)、Amazon(部分服务器 6→5 年,2025)、Meta(延长到 5.5 年)对照——同一资产,各家年限方向相反,利润率可比性差。

P20 [官方 SEC 10-K, Amazon FY2025] 2025-01-01 起部分服务器与网络设备年限 6 年 → 5 年,原因是 AI/ML 技术迭代加速;2025 年折旧因此增加约 $1.4B(媒体转述数额;原文句确认)。
原文: "Effective January 1, 2025 we changed our estimate of the useful lives of a subset of our servers and networking equipment from six years to five years . The shorter useful lives are due to the increased pace of technology development, particularly in the area of artificial intelligence and machine learning."
URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm

## G. 超大规模云对 neocloud 的定位

P21 [官方访谈/Dwarkesh Podcast, 2025-11-12] Nadella:不想做"一家模型公司的托管商";不想被某一代硬件的大规模部署套牢;愿意从 neocloud 租入(lease / build-to-suit / GPUs-as-a-service)。
原文: "it didn't make sense for us to go be a hoster for one model company with limited time horizon RPO"
原文: "I didn't want to get stuck with massive scale of one generation."
原文: "we will take leases, we will take build-to-suit , we'll even take GPUs-as-a-service where we don't have capacity"
URL: https://www.dwarkesh.com/p/satya-nadella-2
判断:超大规模云主动把"单代 GPU 折旧风险 + 单一客户集中风险"外包给 neocloud——neocloud 承担的是被转移出来的风险,其报酬应理解为风险溢价而非稀缺租金。

## H. 电网接入与幽灵需求(反证)

P22 [同行评审级政府实验室/LBNL Queued Up 2026 版, 2026] 截至 2025 年底排队发电+储能约 2,061 GW(较 2024 降 10%,2023 峰值近 2,600 GW);2025 年撤回 >750 GW;2025 年投运项目从申请到投运中位数 >5 年;2000-2020 申请容量仅 13% 投运、75% 撤回。
URL: https://emp.lbl.gov/publications/queued-2026-edition-characteristics (数字经搜索摘要,官网 403 未逐字核)
含义:供给侧建设周期 5 年+,支持"电网接入是持久稀缺点"。

P23 [官方 ERCOT 市场通知, 2026-08-03] 德州州长 Abbott 指令对数据中心大负荷先做"verification",ERCOT 暂停 Batch Zero 分类通知;媒体/律所报道 Batch Zero 有 204 个项目 66.4 GW 有条件纳入基荷、158 个 127.9 GW 为研究负荷,审计预计 2026-12-10 左右结束。
原文: "Governor Greg Abbott directing ERCOT to conduct a verification process before advancing any data center Large Loads through the interconnection process."
URL: https://www.ercot.com/services/comm/mkt_notices/M-A080326-01 ; https://www.hklaw.com/en/insights/publications/2026/08/texas-gov-abbott-directs-data-center-audit
含义:双刃——既确认需求申请中有大量投机(幽灵需求),也说明接入权本身成为被政治分配的稀缺资产。

P24 [媒体转述/Utility Dive, 2025-05-15] Camus Energy CEO:投机性接入申请是实际建成数据中心的 5-10 倍;Dominion、Appalachian Power 提议大负荷电价类别,须支付合同需量的至少 60%/80%(take-or-pay 化)。
原文: "Conservatively, you're seeing five to 10 times more interconnection requests than data centers actually being built."
URL: https://www.utilitydive.com/news/a-fraction-of-proposed-data-centers-will-get-built-utilities-are-wising-up/748214/
含义:受监管公用事业把需求风险转回给数据中心方——受监管层拿的是监管回报(资产基数增长),不是稀缺租金。

## I. CoreWeave 电话会(2026-08-11,FactSet 修订逐字稿,公司 IR 发布)

P25 [官方/电话会逐字稿] 定价:新一代(Blackwell/Vera Rubin)定价与利润率创新高,旧代定价"at or above where it was years ago";7 月全 SKU 提价约 25%,并转嫁零部件涨价;刚签一份 A100(2020 年发布)合同延续到 2029。
原文: "Pricing and margins for our Blackwell and Vera Rubin SKUs are setting new highs while pricing for prior generation SKUs is at or above where it was years ago."
原文: "our July pricing changes, which included an approximately 25% increase across SKUs in response to the current demand environment"
原文: "we recently signed an A100 contract that extends into 2029 at an attractive price. As a reminder, this SKU was introduced in 2020."
URL: https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CRWV-US-CORRECTED-TRANSCRIPT-CoreWeave-Q2-2026-Earnings-Call-11August2026.pdf
含义:A100 跑 9 年 → 支持 6 年折旧不激进;但这是厂商自证,且发生在供给紧张周期。

P26 [官方/电话会逐字稿] 指引:Q3 收入 $3.45-3.6B;Q3 调整后经营利润 $200-260M;Q3 利息支出 $860-940M(> 调整后经营利润 3 倍以上);2026 全年收入 $12.4-13.2B、调整后经营利润 $0.96-1.15B、capex $35-39B;年底 run-rate $18.5-19.5B;年底活跃电力 >1.85 GW。
原文: "Q3 interest expense is expected to be in the range of $860 million to $940 million, reflecting the growth in our debt balance to finance our accelerating deployments."
原文: "we now expect 2026 CapEx in the range of $35 billion to $39 billion"
判断:全年 capex ≈ 收入 3 倍;利息 > 调整后经营利润——即便在提价 25% 的卖方市场,股东层面仍无 GAAP 利润;利润流向债权人(利息)、NVIDIA(设备)、电力/地产(租赁)。

P27 [官方 SEC 8-K 2025-09 / 媒体转述] NVIDIA 与 CoreWeave 签约:NVIDIA 承诺购买 CoreWeave 未售出的剩余容量至 2032-04-13,初始价值 $6.3B;NVIDIA 同时是股东与供应商。
URL: https://www.rcrwireless.com/20250916/ai-infrastructure/nvidia-cloud (媒体转述 8-K)
含义:芯片商为 neocloud 的需求兜底 = 上游用资产负债表"买"渠道;neocloud 的部分风险实际由 NVIDIA 承担,也说明 neocloud 更像 NVIDIA 的分销/融资通道。

## J. 电力在 AI 总成本中的份额(关键反证)

P28 [研究机构/Epoch AI, 2026-05-14] 1 GW AI 数据中心(全 GB200 NVL72):前期 capex $38B,年 opex $0.9B;年化 TCO $8.5B,其中服务器 $5B(60%),能源仅 $0.6B/年(约 7%,电价 8.34 美分/kWh);IT 寿命 3 年→年化 $12B,7 年→$7B。
原文: "Servers dominate this cost at $5 billion per year, or 60% of the total"
URL: https://epoch.ai/data-insights/ai-datacenter-cost-breakdown
含义(承重):电费本身只占 AI TCO 的个位数百分比——电力层的"稀缺租金"即使电价翻倍,也只吃掉 TCO 的 ~7 个百分点;电力的议价力来自"能不能接入/多快接入"(时间价值),而非电价。真正的利润池仍在服务器(NVIDIA)。GPU 寿命假设对 TCO 的影响(±40%)远大于电价。

## K. 电价的政治天花板

P29 [官方/宾州州长办公室, 2026-01-16] Shapiro 争取联邦支持将 PJM 价格上限延长两次拍卖,称为 13 州 6,700 万用户节省约 $27B;要求把长期合约成本分摊给"未自带电源"的数据中心和新大用户。
原文: "Allocate the cost of those long-term contracts to data centers and new large users that have not brought their own power"
URL: https://www.pa.gov/governor/newsroom/2026-press-releases/gov-shapiro-secures-federal-support-to-extend-pjm-price-cap
含义:电力稀缺租金被政治封顶 + 成本被定向转嫁给数据中心 → IPP 的上行有上限,但"自带电源(BYOG)"的数据中心更值钱 → 租金向"拥有已接入电源的场地"(powered land)集中。PJM 容量价从 2024/25 的 $28.92/MW-day 涨到约 $329/MW-day(IEEFA 等转述),约 11 倍。

P30 [厂商自报/Crusoe 新闻稿, 2026-09-17] Crusoe Series F $3.9B,投后估值 $30.9B(NVIDIA 等参投);TCV >$140B;毛签约容量 6 GW+,已交付运营 1 GW;Abilene(OpenAI/Stargate)为主要项目。
URL: https://www.crusoe.ai/resources/newsroom/crusoe-announces-series-f-funding
口径:非上市厂商自报,TCV 为承诺额。

P31 [媒体转述, 2025-2026] Lambda:截至 2025-09 财年收入 >$5.2 亿、亏损 $1.75 亿;NVIDIA 以 $1.5B 租回 18,000 张自家 GPU(4 年),成为 Lambda 最大客户;Microsoft 多年数十亿美元协议。
URL: https://www.datacenterdynamics.com/en/news/nvidia-signs-15bn-deal-to-lease-its-gpus-back-from-lambda-report/ ; https://research.contrary.com/company/lambda
口径:媒体转述,非审计。含义同 P27:NVIDIA 同时是供应商、股东、客户——循环融资。

P32 [厂商自报/Talen 2025-06 投资者材料,经媒体转述] Talen-AWS 修订 PPA:至 2042 年最多 1,920 MW,表前(front-of-the-meter)模式;合同期总收入约 $18B,满量后年收入至多 $1.4B,2028 起年 2% 递增,最迟 2032 满量。
URL: https://electroneconomics.substack.com/p/talens-amazon-contract-carries-10 ; Talen 10-K https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm
推算(本线自算):$1.4B ÷ (1.92 GW × 8,760h ≈ 16.8 TWh) ≈ $83/MWh(按 100% 出力;按核电 ~93% 容量因子 ≈ $90/MWh)——与 Jefferies 对微软-Crane 的 $110-115/MWh 估计同一量级,约为批发电价的 1.5-2.5 倍。即核电 PPA 有溢价但不是 NVIDIA 式的倍数级租金。

## L. 横向对照:同一季度各层利润量级

P33 [官方 SEC 8-K, NVIDIA, 2026-08-26] Q2 FY27(截至 2026-07-26)收入 $96.2B,数据中心 $89.0B;GAAP 毛利率 75.0%;GAAP 经营利润 $63.7B;GAAP 净利 $59.7B。
原文: "For the quarter, GAAP and non-GAAP gross margins were both 75.0%."
URL: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm
对照(本线自算,口径混杂仅示量级):同期(日历 Q2 2026)本线覆盖公司——Vistra adj. EBITDA $1.77B、Talen adj. EBITDA $0.37B、GE Vernova 净利 $0.6B、CoreWeave GAAP 经营亏损 $(0.05)B / 净亏 $(0.63)B、Nebius 净亏约 $(0.19)B、Digital Realty 收入 $1.9B——加总的 EBITDA 量级不到 NVIDIA 单季 GAAP 经营利润的 1/10。当下利润池:芯片 >> 电力/设备 > 数据中心地产 > neocloud(股东层面为负)。

---
## 综合判断(本线)

1. neocloud 的商业模式在财报上就是"带杠杆的折旧套利":CoreWeave Q2 2026 Adj. EBITDA 59% → 折旧吃掉 54% 收入 → 利息吃掉 25% → GAAP 净亏 24%;Q3 利息指引 $0.86-0.94B > 调整后经营利润 $0.20-0.26B。即使在 2026 年卖方市场(提价 25%、A100 续约到 2029、Nebius 回收期缩至 22 个月),股东层面仍未见 GAAP 利润。价值被债权人、NVIDIA(设备 75% 毛利)、电力/地产(租赁)分走。
2. GPU 租价不是单调下跌:2024 初 ~$8 → 2025-10 低点 ~$1.70(-80%,商品化证据)→ 2026-09/10 $2.8-3.3(反弹 60-90%,短缺证据)。周期性强,意味着 neocloud 是高 beta 资产;租价上行期折旧年限被上调(Nebius 4→5、CoreWeave 6 年),下行期会反噬。
3. 超大规模云主动把"单代折旧 + 单客户集中"风险外包给 neocloud(Nadella 原话),NVIDIA 以兜底/回租/入股支撑 neocloud——neocloud 更像上游的融资与分销通道,议价权有限。
4. 电力层:IPP 利润确实在涨(Vistra +31%、Talen 4 倍、CEG 上调指引),主要来自 PJM 容量价约 11 倍上涨;但(a)容量价被监管上限封住且连续三年撞顶,政治明确要求数据中心自担成本;(b)电费只占 AI TCO 约 7%,电力卖方能拿到的是"接入时间"的稀缺租金,金额规模远小于芯片层;(c)幽灵需求(申请是实建的 5-10 倍、ERCOT 暂停审计)意味着需求侧被高估。
5. 最持久的稀缺点更可能是"已通电、已接入的场地与容量"(powered land / energized capacity):DLR >1MW 续约价差 66.7%、Nebius/CoreWeave 都在囤合同电力(5 GW / 3.7 GW)、Vistra 向下游成立 Helix。供给弹性:燃气轮机 ~5 年排队但 GEV 在扩产(20→30 GW/年),并网中位数 >5 年——比芯片(年级别)慢,所以稀缺持续更久;但单位租金被监管与 TCO 占比双重压低。结论:电力层 = 持久但"薄"的利润池;neocloud = 薄且带杠杆;芯片 = 当下最厚。
