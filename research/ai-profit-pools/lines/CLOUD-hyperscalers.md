# CLOUD-hyperscalers 调研线(截至 2026 年 10 月)

数据截点:微软 FY26 Q4(截至 2026-06-30,7/29 发布)+ 9 月 FY27 分部重述;Alphabet/Amazon/Meta 2026 Q2(截至 6/30,7 月下旬发布);Oracle FY27 Q1(截至 2026-08-31,9/10 发布)。
口径约定:财年 vs 日历年分开写;capex 区分"现金购置 PP&E"与"含融资租赁";run-rate 与确认收入分开;GAAP / non-GAAP 分开。
原始文件均从 sec.gov 直接抓取(curl,UA=research bot),引文为文件原文。电话会引语经 WebFetch 抽取(标"电话会转录")。

---

## A. 当下利润:云层是 AI 链条里少数"已在 GAAP 层面赚钱"的环节

**C01 AWS 经营利润率 39.4%,增速 37%(官方 8-K,2026-07-30)**
- "AWS segment sales increased 37% year-over-year to $42.2 billion." / "AWS segment operating income was $16.6 billion, compared with $10.2 billion in second quarter 2025."
- 补充表:AWS 经营利润率 Q2'25 32.9% → Q2'26 39.4%;TTM 36.8%。
- 口径警示(电话会转录,Olsavsky):利润率改善 "520 basis points if you exclude the derivative accounting gain"——10-Q 原文:"Technology and infrastructure costs in Q2 2026 include net unrealized gains for energy contracts that are subject to derivative accounting, primarily related to AWS." → 剔除能源衍生品未实现收益后约 38%。
- URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm ;10-Q https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm

**C02 Google Cloud 收入 +82%,经营利润率 35.6%(官方 8-K,2026-07-22)**
- "Google Cloud saw a meaningful acceleration in growth as revenues increased 82% to $24.8 billion"
- 分部经营利润:Google Cloud $2,826M → $8,814M(Q2'25→Q2'26)。电话会:"operating margin increased from 20.7% in the second quarter last year to 35.6%"
- 口径警示:(a) 10-Q:"in the second quarter of 2026, we began recognizing revenue from the sale of TPU systems"——82% 增速含首次 TPU 硬件销售(产品收入,非纯云服务);(b) "Alphabet-level activities ... primarily reflect expenses related to our shared AI research and development",Q2 为 -$5,789M,前沿模型研发成本未分摊进 Cloud 分部利润。
- URL: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm

**C03 微软首次披露 Azure 绝对额:FY26 $101.9B(官方 8-K 分部重述,2026-09)**
- 重述口径 Azure:FY26 $101,938M(FY25 $72,610M),Q4 FY26 $29,417M;重述口径增速 Q4 42%、FY 40%。
- 口径变化原文:"Azure has been updated to reflect the move of GitHub cloud and other developer cloud services as well as Security Copilot to Microsoft 365 cloud. Healthcare and Life Sciences cloud will move to the new Industry solutions cloud metric."
- 新分部 Agents and Infra FY26 收入 $268,127M、经营利润 $136,365M(50.9%)。
- FY27 Q1 指引:"Azure revenue Growth of 44% to 45% in constant currency"
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526380280/d291965dex991.htm

**C04 微软 Intelligent Cloud:毛利率下滑、经营利润率持平(8-K 分部表,自算)**
- Q4 FY26:收入 $39,306M、成本 $16,876M、经营利润 $15,955M → 毛利率 57.1%(Q4 FY25 60.4%);经营利润率 40.6%(上年同期 40.6%)。FY26 41.3% vs FY25 42.0%。
- 10-K:"Microsoft Cloud gross margin percentage decreased to 66% driven by continued investments in AI infrastructure and growing AI product usage"
- 电话会转录(Hood):"Microsoft Cloud gross margin percentage was better than expected at 65%, and down year-over-year"
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526323632/msft-ex99_1.htm ;10-K https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm

**C05 Oracle:OCI +121%,但云与软件分部直接利润率下滑(官方 8-K/10-Q,2026-09-10/11)**
- "Q1 Cloud Infra (IaaS) Revenue up 121% in USD & up 120% in constant currency to $7.4 billion."
- 10-Q 分部:Cloud and software 收入 $17,157M(+33%),费用 $6,235M(上年 $3,418M,+82%),Margin $9,358M → 直接利润率 54.5%(上年 59.6%)。注:"The margins reported reflect only the direct controllable costs"
- URL: https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-ex99_1.htm ;10-Q https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm

**C06 GPU 租赁毛利 14% 报道 vs Oracle 自报 30-40%(媒体转述/厂商自报,2025-10)**
- The Information(经 CNBC 转述,2025-10-07):内部文件显示截至 2025-08 的三个月 Nvidia 芯片租赁约 $900M 收入、毛利约 14%。
- Oracle 回应(2025-10 AI World/分析师会,Bloomberg 转述):一个 6 年合同总额 $60B 的 AI 基础设施项目毛利率 35%,区间 30-40%。
- 状态:两者均非 GAAP 披露,Oracle 10-Q 未分拆 OCI 毛利。
- URL: https://www.cnbc.com/2025/10/07/oracle-stock-nvidia-chip-margins.html ;https://news.bloomberglaw.com/artificial-intelligence/oracle-eases-ai-profit-fears-by-saying-margins-can-be-35-1

**C07 Meta:无云业务,AI 投入先压利润(官方 10-Q,2026-07-30)**
- "Income from operations for the second quarter of 2026 was $18.78 billion, a decrease of $1.67 billion, or 8% ... driven by higher costs and expenses ... infrastructure expenses related to our data centers, technical infrastructure, and third-party cloud services; legal-related costs; and third-party AI token costs."
- FoA 经营利润率 53% → 39%;收入 +28%,广告单价 +12%、展示 +14%。
- 意义:Meta 同时是云/代币的买家("third-party cloud services","third-party AI token costs")——AI 回报经广告体现,但当期利润层在被上游(云/模型)抽走。
- URL: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm

## B. "AI 收入"口径:各家都是 run-rate,定义不同

**C08 微软 "AI business" run-rate $37B(官方 8-K,2026-04-29)**
- Nadella:"Our AI business surpassed an annual revenue run rate of $37 billion, up 123% year-over-year."(2025-01 为 $13B)
- 口径:未定义 AI business 包含范围(Azure AI + Copilot 等),run-rate 非确认收入;FY26 Q4 起未再更新此数字(电话会只给 Copilot 3000 万付费席位)。
- URL: https://www.sec.gov/Archives/edgar/data/789019/000119312526191457/msft-ex99_1.htm

**C09 AWS "AI business" run-rate >$25B,芯片业务 run-rate >$25B(官方 8-K,2026-07-30)**
- "Exceeded a $25 billion annual revenue run rate for AWS's AI business, growing triple-digit percentages year-over-year." / "Exceeded a $25 billion annual revenue run rate for its chips business"
- 口径:AWS 整体年化 $169B,AI 占约 15%;"chips business" 含 Trainium/Graviton,与 AI 业务可能重叠。
- URL: 同 C01

**C10 Alphabet 不单独给"AI 收入"(官方 8-K)**——只给 token 量:"Gemini models now process 22 billion API tokens per minute"、Gemini App 9.5 亿 MAU;Google Cloud 增长归因 "enterprise AI Solutions and enterprise AI Infrastructure, as well as core GCP services"。口径不可与 MSFT/AWS 横比。

## C. 积压订单:规模巨大,但高度集中于两三家前沿实验室

**C11 微软商业 RPO $678B,剔除 OpenAI 仅 +25%(官方 8-K + 电话会转录)**
- 8-K:"commercial remaining performance obligation increased 84% to $678 billion."
- 电话会:"RPO increased 25% when excluding OpenAI." / "All sequential commercial RPO growth was driven by commitments from customers outside of frontier model companies."
- 10-K:约 30% 在未来 12 个月确认。

**C12 微软 FY26 来自 OpenAI 的收入 $24.1B(官方 10-K 关联方披露)**
- "For fiscal year 2026, we recorded revenue from commercial arrangements with OpenAI, inclusive of revenue-sharing payments, of $ 24.1 billion, and accounts receivable from OpenAI as of June 30, 2026 was $ 6.0 billion."
- 规模:约占微软总收入 7.3%;若主要落在 Azure,相当于 Azure FY26 的约 1/4(推算,口径不同,需谨慎)。
- 持股:"an approximate 25 % interest on an as-converted basis"。

**C13 Google Cloud 积压 $514B,口径于 2026Q1 放宽(官方 10-Q)**
- "As of June 30, 2026, we had $ 519.5 billion of remaining performance obligations ('revenue backlog'), of which $ 513.9 billion related to Google Cloud ... We expect to recognize just over 50 % of the revenue backlog as revenues over the next 24 months"
- 口径警示:"In the first quarter of 2026, we elected to change our reporting of revenue backlog to also include contracts with an original expected term of one year or less."
- 电话会转录:CFO 未披露其中 TPU 销售协议占比;"the vast majority of the revenues from these agreements will be realized in 2027"(指 TPU system sales)。
- URL: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm

**C14 AWS 积压 $496B,含 OpenAI +$100B、Anthropic +>$100B(官方 10-Q)**
- "those commitments not yet recognized were approximately $ 496 billion as of June 30, 2026. The weighted-average remaining life of our long-term contracts is 6.4 years."
- "In Q1 2026, AWS and OpenAI Group PBC ('OpenAI') announced an expansion of the existing $ 38.0 billion multi-year commitment ... by $ 100.0 billion over 8.0 years ... In Q2 2026, AWS and Anthropic announced an expansion ... by more than $ 100.0 billion over 10.0 years"

**C15 Oracle RPO $664B,仅 13% 在 12 个月内确认(官方 10-Q)**
- "Remaining performance obligations were $ 664 billion as of August 31, 2026 , of which we expect to recognize approximately 13 % as revenues over the next twelve months , 37 % over the subsequent month 13 to month 36 , 34 % over the subsequent month 37 to month 60"
- 10-K 风险因素:"In certain OCI offerings, we are more concentrated among a number of large customers, which could increase these risks."(10-K/10-Q 均未点名 OpenAI)
- 新签:"Oracle booked more than $30 billion of additional AI cloud contracts in Q1"

## D. capex 与自由现金流:2026 年四家合计指引约 $7000 亿+

**C16 微软:FY26 现金 capex $115.9B,占 OCF 63%;CY2026 指引约 $175B(官方 8-K + 电话会)**
- 现金流量表:Additions to property and equipment FY26 $115,948M(FY25 $64,551M);Net cash from operations $182,935M(FY25 $136,162M)→ 现金 FCF ≈ $67.0B(FY25 ≈ $71.6B)。
- 电话会:"Capital expenditures were $41 billion"(Q4,含融资租赁);"Roughly two thirds of our capex was for short-lived assets, primarily CPUs and GPUs"
- CY2026:"our calendar year 2026 CapEx investment expectations remain unchanged. However, the shift from finance to operating leases adjusts our expectation to approximately $175 billion"(此前约 $190B——口径变化而非削减)。
- 10-K:未起租租赁 "$ 329.1 billion","will commence between fiscal year 2027 and fiscal year 2033"。

**C17 Alphabet:2026 capex 指引 $195-205B;Q2 自由现金流转负;发股融资(官方 8-K)**
- Q2'26 购置 PP&E $44,924M,OCF $39,069M,FCF -$5,855M;TTM FCF $53,273M。2025 全年 capex $91,447M / OCF $164,713M(55.5%)。
- 电话会转录:"We are updating our full-year 2026 CapEx guidance range to $195 billion-$205 billion, up from our previous estimate of $180 billion-$190 billion." / "we continue to expect our CapEx to increase significantly in 2027"
- 2026-06-01 8-K:"Alphabet Announces Proposed $80 Billion Equity Capital Raise to Expand AI Infrastructure and Compute"(含 Berkshire $10B 定增);Q2 实际 "aggregate net proceeds of $49.6 billion",另发债净额 $20.3B。
- URL: https://www.sec.gov/Archives/edgar/data/1652044/000119312526257724/d83560dex991.htm

**C18 Amazon:2026 现金 capex 约 $220B;TTM 自由现金流 -$7.6B(官方 8-K + 电话会)**
- "Free cash flow decreased to an outflow of $7.6 billion for the trailing twelve months, driven primarily by a year-over-year increase of $66.1 billion in purchases of property and equipment ... This increase primarily reflects investments in artificial intelligence."
- TTM 净 capex $169,007M vs OCF $161,403M(105%)。2025 全年净 capex $128,320M / OCF $139,514M,FCF $11,194M。
- 电话会转录(Jassy):"We now believe we will spend approximately $220 billion in cash CapEx in 2026." / "Even at that amount, we will still not have enough capacity to meet all the demand we have in 2026."

**C19 Meta:2026 capex(含融资租赁本金)$130-145B;Q2 FCF $0.78B(官方 8-K)**
- "We anticipate 2026 capital expenditures, including principal payments on finance leases, to be in the range of $130-145 billion, narrowed from our prior outlook of $125-145 billion."
- Q2:OCF $31,862M,购置 PP&E $30,116M,融资租赁本金 $962M → FCF $784M(上年同期 $8,549M)。2025 全年 FCF $43,585M。
- 10-Q:未起租租赁 "approximately $ 278.99 billion",7 月再签 "approximately $ 68 billion"。
- URL: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm

**C20 Oracle:FY26 FCF -$23.7B,FY27 Q1 再 -$5.4B,靠 ATM 发股与举债(官方 10-K/10-Q)**
- FY26(截至 2026-05-31):OCF $31,977M,capex $55,663M,FCF -$23,686M。
- FY27 Q1:OCF $23,103M,capex $28,499M,FCF -$5,396M;"During the first quarter ended August 31, 2026, we fully utilized the" $20B ATM。非流动借款 $117.7B。
- URL: 10-K https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm

## E. 折旧年限:会计杠杆有多大

**C21 微软 2022 年服务器 4→6 年,FY23 经营利润 +$3.7B(官方 10-K FY22)**
- "we determined we should increase the estimated useful lives of both server and network equipment from four years to six years ... it is estimated this change will increase our fiscal year 2023 operating income by $3.7 billion."
- FY26 10-K 写法:"servers and network equipment, two to six years"。
- FY27 起数据中心/办公楼 15→25 年(电话会转录):"This change affects only the timing of future depreciation and is expected to have a minimal benefit to FY27 operating income."——主要影响是 capex 统计口径(融资租赁→经营租赁)。
- URL: https://www.sec.gov/Archives/edgar/data/789019/000156459022026876/msft-10k_20220630.htm

**C22 Alphabet 2023 年服务器 4→6 年(官方 10-K 2022)**
- "adjusted the estimated useful life of our servers from four years to six years and the estimated useful life of certain network equipment from five years to six years . This change in accounting estimate is effective beginning in fiscal year 2023."
- 此后未再变更;H1'26 折旧 $13,586M(H1'25 $9,485M,+43%)。
- URL: https://www.sec.gov/Archives/edgar/data/1652044/000165204423000016/goog-20221231.htm

**C23 Meta 2025 年延长至 5.5 年,2025 年少计折旧 $2.92B(官方 10-K 2025)**
- "an increase in the estimated useful lives of most servers and network assets to 5.5 years, effective January 1, 2025 ... the financial impact of this change in estimate included a reduction in depreciation expense of $ 2.92 billion and an increase in net income of $ 2.59 billion, or $ 1.00 per diluted share, for the year ended December 31, 2025."
- URL: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm

**C24 Amazon 反向缩短 6→5 年,并提前报废(官方 10-K 2024/2025)——反证"都在拉长"**
- 10-K 2024:"changing the useful lives of a subset of our servers and networking equipment, effective January 1, 2025, from six years to five years" / "We recorded approximately $ 920 million of accelerated depreciation ... related to these decisions" / "due to an increased pace of technology development, particularly in the area of artificial intelligence and machine learning."
- 10-K 2025 实际影响:"an increase in depreciation and amortization expense of $ 1.4 billion and a reduction in net income of $ 1.0 billion"
- 前一次(2024)5→6 年曾带来 "a reduction in depreciation and amortization expense of $ 3.2 billion"。
- URL: https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm ;https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm

**C25 Oracle 服务器 6 年(官方 10-Q)**:"Comprised primarily of servers and networking equipment with estimated useful life of six years";季度折旧 $3.2B(上年同期 $1.4B)。

**C26 Burry:2026-2028 少计折旧 $176B(从业者/投资人,2025-11,媒体转述)**
- "Understating depreciation by extending useful life of assets artificially boosts earnings - one of the more common frauds of the modern era."(X 帖)
- 估算:Oracle 2028 年利润高估 26.9%,Meta 20.8%(Investing.com 转述)。
- 反驳/对照:Amazon 自己缩短到 5 年(C24);老一代 A100 仍在出租(市场观察,非一手);Nadella 本人:"I didn't want to go get stuck for four or five years of depreciation on one generation"(Dwarkesh 播客,2025-11)——承认技术代际风险,但用分批采购而非缩短年限应对。
- URL: https://www.investing.com/news/stock-market-news/michael-burry-warns-of-176-billion-depreciation-understatement-by-tech-giants-4346876 ;https://www.dwarkesh.com/p/satya-nadella-2

## F. 云厂商如何从模型层"分账":收入分成 + 股权重估

**C27 微软-OpenAI:约 27% 股权、$250B 增量 Azure 承诺、放弃 ROFR(官方博客,2025-10-28)**
- "Microsoft holds an investment in OpenAI Group PBC valued at approximately $135 billion, representing roughly 27 percent on an as-converted diluted basis" / "OpenAI has contracted to purchase an incremental $250B of Azure services" / "Microsoft will no longer have a right of first refusal to be OpenAI's compute provider"
- 2026-04-27 再修订(媒体转述):OpenAI 向微软的约 20% 收入分成持续至 2030 但设总额上限;微软对 OpenAI IP 许可变为非独占;OpenAI 可在任何云提供产品。
- URL: https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/ ;https://www.cnbc.com/2026/04/27/openai-microsoft-partnership-revenue-cap.html

**C28 微软 OpenAI 权益法:FY25 亏 $4.8B → FY26 赚 $6.5B(稀释收益)(官方 10-K)**
- "Other income (expense), net included $6.5 billion of net gains and $4.8 billion of net losses for fiscal years 2026 and 2025, respectively, from investments in OpenAI ... The net gains recorded for fiscal year 2026 primarily relate to the dilution gain from the OpenAI Recapitalization."
- 另:Q4 FY26 "a $3.2 billion gain from our investment in Anthropic"(8-K)。
- 微软 non-GAAP 剔除 OpenAI 影响:FY26 净利 GAAP $133.7B vs non-GAAP $128.8B。

**C29 Amazon Q2 税前其他收益 $53.4B,主要来自 Anthropic 估值上调(官方 8-K/10-Q)**
- 8-K:"Second quarter 2026 net income includes non-operating pre-tax other income of $53.4 billion, primarily from our investments in Anthropic."
- 10-Q:"The upward adjustments relating to equity investments in private companies of $ 50.5 billion in Q2 2026 and $ 62.8 billion for the six months ended June 30, 2026 reflect observable changes in prices, primarily from our nonvoting preferred stock in Anthropic."
- 对照:同季 AWS 经营利润 $16.6B——一季度的 Anthropic 账面重估收益是 AWS 经营利润的 3 倍。

**C30 Alphabet Q2 其他收益 $98.0B,主要为股权未实现收益(官方 8-K/10-Q)**
- 8-K:"Other income reflected a net gain of $98.0 billion, primarily the result of net unrealized gains on our equity securities."
- 10-Q:非上市股权(measurement alternative)Q2 未实现收益 $77,544M,"primarily consist of our investment in a private company"(未点名);另持有 SpaceX 股份 $80.0B + $14.1B。Q2 净利 $112.2B 中经营利润仅 $40.8B。

## G. 供给约束与议价权

**C31 三家都说"需求超过供给"(电话会转录)**
- 微软:"customer demand continues to exceed supply"(Azure 指引语境)
- Google:"we continue to be supply constrained"
- Amazon:见 C18
- Oracle 8-K:"Customer demand for AI Cloud Training and Inferencing Services continues to grow faster than supply."
- 解读:当下利润率在扩张期由稀缺支撑;稀缺解除后利润率走势是长期利润落点的关键变量(未证实)。

**C32 Bedrock 多模型货架(官方 8-K)**——"Added 10+ fully managed foundation models to Amazon Bedrock, including OpenAI's GPT-5.6, Anthropic's Claude Opus 5, Google DeepMind's Gemma 4, and SpaceXAI's Grok 4.3" / "customers spent more in Q2 than all prior quarters combined"。支持"云做模型货架、模型可替换"叙事;但未披露 Bedrock 收入额。

---

## 交叉口径问题(供验证阶段)
1. 财年错位:微软 FY26 = 2025-07~2026-06;Oracle FY26 = 2025-06~2026-05;其余为日历年。合计 capex 不能直接相加。
2. capex 口径:微软"$175B CY2026"含融资租赁、且因租赁类型转换下调;Amazon 用"现金 capex"及"净额(扣除处置与激励)";Meta 含融资租赁本金;Alphabet 为购置 PP&E。
3. 微软 Azure 9 月重述(移出 GitHub/Security Copilot/医疗云),新旧增速差 1pp;旧口径"Azure and other cloud services"不可与新"Azure"直接拼接。
4. Alphabet 积压 2026Q1 起纳入 1 年以内合同,同比不可比;Google Cloud Q2 增速含首次 TPU 硬件销售。
5. Google Cloud 分部利润不含 Alphabet-level 共享 AI 研发(Q2 -$5.8B);AWS/Azure 分部各自分摊方式不同。
6. AWS Q2 利润率含能源合同衍生品未实现收益(非现金),剔除后约 38%。
7. "AI 收入"全是 run-rate 且定义不一(MSFT AI business $37B / AWS AI $25B / Alphabet 不披露)。
8. 净利润层被模型公司股权重估扭曲:Amazon $50.5B(Anthropic)、Alphabet $77.5B(未点名私企)+SpaceX、微软 OpenAI 稀释收益 $6.5B——"云厂商赚了多少"必须用经营利润/分部利润口径,不用 GAAP 净利。
9. 积压/RPO 高度集中于 OpenAI、Anthropic 等少数实验室(MSFT ex-OpenAI RPO 仅 +25%);承诺额 ≠ 落地额,Oracle RPO 仅 13% 在 12 个月内确认。
10. Oracle 14% GPU 租赁毛利为 The Information 内部文件报道(2025-08 季度),35% 为 Oracle 自报合同全生命周期估算,口径不同。
