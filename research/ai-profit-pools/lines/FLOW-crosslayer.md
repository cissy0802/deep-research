# FLOW-crosslayer 跨层资金流与总量账(截至 2026-10)

状态:调研中

## A. 收入缺口测算

F1 Sequoia/Cahn $600B (2024-06-20, 从业者博客/VC) https://sequoiacap.com/article/ais-600b-question/
> "take Nvidia's run-rate revenue forecast and multiply it by 2x to reflect the total cost of AI data centers (GPUs are half of the total cost of ownership...). Then you multiply by 2x again, to reflect a 50% gross margin for the end-user of the GPU"
口径:NVDA 数据中心 run-rate ×4 = 需要的终端年收入;是"需求侧应得收入"推算,非实测。

F2 Sequoia/Cahn $840B (2025-06-17) https://sequoiacap.com/article/why-ai-labs-are-starting-to-look-like-sports-teams
> "AI's $600B Question is now roughly AI's $840B Question, assuming that Nvidia reaches something like $210B in run-rate data center revenue by year-end 2025."

F3 Bain 2025 Global Technology Report (2025-09-23, 分析机构) https://www.prnewswire.com/news-releases/2-trillion-in-new-revenue-needed-to-fund-ais-scaling-trend---bain--companys-6th-annual-global-technology-report-302563362.html ; https://www.bain.com/insights/how-can-we-meet-ais-insatiable-demand-for-compute-power-technology-report-2025/
> "Two trillion dollars in annual revenue is what's needed to fund computing power needed to meet anticipated AI demand by 2030."
> "Even with AI-related savings, the world is still $800 billion short to keep pace with demand."
> "$500 billion of annual capex corresponds to $2 trillion in annual revenue" (按云厂商可持续 capex/收入比)
口径:2030 年单年;$800B 缺口 = 假设全部本地 IT 预算上云 + 再投入 AI 节省(约 20% 相关预算)后仍不足的额度。

## B. 芯片层 NVIDIA(10-Q Q2 FY27,截至 2026-07-26,提交 2026-08-26,官方)
URL: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

F4 季度损益:Revenue $96,221M;Gross margin 75.0%;Operating income $63,734M;Net income $59,688M。数据中心 $89.0B (+117% YoY)。
> "Revenue was $96.2 billion, up 106% from a year ago and up 18% sequentially. Data Center revenue was $89.0 billion, up 117%..."

F5 投资收益进利润(循环融资回流到芯片层账面):
> "Gains from equity securities, net 7,771 2,247 23,707 2,073" (Q2 / Q2 去年 / H1 / H1 去年, $M)
> "Other income, net, primarily consists of realized or unrealized gains and losses from investments in non-marketable securities and publicly-held equity securities."
H1 FY27 税前利润 $141,410M 中 $24,140M 来自 Other income(约 17%),多为对客户/模型商的股权未实现收益。

F6 非上市股权持仓膨胀:非上市股权余额 $3,799M(2025-07)→ $47,898M(2026-07);H1 净增 $31,005M。
> "Equity investments – We committed to make certain equity investments in AI model makers, infrastructure financiers, and other private companies, subject to certain contingencies."  未来承诺:Equity investments $25B。
> "We had $ 3.3 billion of investments in infrastructure financiers accounted for using the equity method"

F7 为 OpenAI 担保(新,2026-08):
> "In August 2026, we entered into guarantees, capped at a total of $ 105 billion, to provide credit support on a land, power, and shell buildout with affiliates of SB Energy Corp. ... on behalf of a customer, an affiliate of OpenAI Group PBC (OpenAI), related to leases for approximately 4.25 gigawatts of IT load ... In exchange for the guarantees, the site will exclusively host NVIDIA AI infrastructure"
> "The guarantees terminate upon certain events, including OpenAI achieving a satisfactory credit rating"
> "We believe AI clouds and AI model makers have significant demand ... and currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity"
含义:芯片商用自身资产负债表为模型商的信用兜底——风险从模型层回流芯片层。

F8 间接客户 OpenAI:
> "We estimate that one AI research and deployment company contributed a meaningful amount of our revenue by purchasing cloud services from our customers"
F9 承诺:supply and capacity commitments 从 $119B 升至 $279B;总承诺 $366B(含 cloud service agreements $29B——NVIDIA 回租云算力)。

## C. NVIDIA–OpenAI $100B 落地情况
F10 2026-02-27 OpenAI 融资 $110B(后 3/31 收于 $122B、投后 $852B):Amazon 至多 $50B、NVIDIA $30B、SoftBank $30B(TechCrunch,媒体转述)https://techcrunch.com/2026/02/27/openai-raises-110b-in-one-of-the-largest-private-funding-rounds-in-history/
> "$35 billion of Amazon's investment could be contingent on the company either achieving AGI or making its IPO by the end of the year" ; OpenAI 承诺消耗 ≥2GW Trainium、AWS 合作扩 $100B;"a significant portion of the dollar amount comes in the form of services rather than cash"
F11 Huang 2026-03-04 摩根士丹利 TMT 会议(媒体转述,Reuters/Yahoo)https://finance.yahoo.com/news/nvidia-not-able-invest-100-185513816.html :$100B "probably not in the cards";对 Anthropic 的 $10B "probably will be the last"。
结论:2025-09 的 "up to $100B" LOI 落地为 $30B 股权 + 2026-08 的 $105B 上限租约担保(形式从股权转为信用担保)。

## D. AMD–OpenAI(10-Q 截至 2026-06-27,官方)https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm
F12 > "In October 2025 and February 2026, we entered into multi-year agreements with OpenAI OpCo, LLC (OpenAI) and Meta Platforms, Inc. (Meta), respectively, under which each customer intends to deploy up to 6 gigawatts of AMD data center GPUs"
> "As of June 27, 2026, no warrant shares had vested or become exercisable, and the warrants had no impact on the Condensed Consolidated Financial Statements"
(每家 1.6 亿股、行权价 $0.01 的认股权,按采购里程碑+股价门槛归属)

## E. Oracle(10-Q 截至 2026-08-31,官方)https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm ;新闻稿 https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/orcl-ex99_1.htm
F13 > "Remaining performance obligations were $ 664 billion as of August 31, 2026 , of which we expect to recognize approximately 13 % as revenues over the next twelve months"
对照:当季总收入 $19,345M;资本开支 $28,499M;FCF −$5,396M(non-GAAP)。
F14 > "we received $ 11.4 billion of prepayments from customers that included a significant financing component" ——经营现金流 $23.1B 中含此预付款。
> "Oracle booked more than $30 billion of additional AI cloud contracts in Q1 ... Based on the structuring of those new contracts, the Company confirms there is no incremental impact on its plans to raise capital."
> "Oracle successfully completed the sale of $20 billion of common stock ... through an At-the-Market (ATM) equity program"
F15 > "we had $ 288 billion of additional lease commitments, substantially all related to data center arrangements, that are generally expected to commence between the second quarter of fiscal 2027 and fiscal 2029 and for terms of fifteen to nineteen years that were not reflected on our condensed consolidated balance sheets"

## F. CoreWeave(10-Q 截至 2026-06-30,官方)https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
F16 Q2 2026:收入 $2,575M;经营亏损 $(49)M;净利息费用 $(640)M;净亏损 $(626)M。RPO $103.7B(41% 在 24 个月内确认)。
> "As of June 30, 2026, the Company had $ 103.7 billion of unsatisfied RPO"
> "In January 2026, we entered into a securities purchase agreement with NVIDIA Corporation for a private placement of approximately 23 million shares of our Class A common stock at a purchase price of $87.20 per share, for aggregate gross proceeds of $2.0 billion."
> 客户集中:Customer A 36%(Q2 2026,去年同期 71%),Customer B 26%;"Other significant customers include Microsoft and OpenAI"
> Meta 2026-03 订单 "up to approximately $21.0 billion";OpenAI 2025-09 订单 "up to approximately $6.5 billion through May 31, 2031"
> 债务:存量高息票据 9.250%/9.000%/9.750%/9.625%/8.500%(2026-09-22 8-K 列举);2026-09 新发 2.875% 可转债。
含义:GPU 云中间层当季收入翻倍但经营利润为负、利息吞掉利润——利润没有停在"新云"层。

## G. Microsoft(10-K FY26 截至 2026-06-30,官方)https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
F17 > "For fiscal year 2026, we recorded revenue from commercial arrangements with OpenAI, inclusive of revenue-sharing payments, of $ 24.1 billion, and accounts receivable from OpenAI as of June 30, 2026 was $ 6.0 billion. We have made total funding commitments of $ 13.0 billion related to our investment, of which $ 11.9 billion has been funded"
F18 > "Other income (expense), net included $6.5 billion of net gains ... from investments in OpenAI ... The net gains recorded for fiscal year 2026 primarily relate to the dilution gain from the OpenAI Recapitalization." (FY25 为 $4.8B 净亏损)
F19 > "Commercial remaining performance obligation increased 84% to $678 billion." ; "Microsoft Cloud gross margin percentage decreased to 66% driven by continued investments in AI infrastructure"; 资本开支(Additions to property and equipment)$115,948M;未起租数据中心租约 $329.1B。
F20 2025-10 重组(MSFT 10-Q 2025-09-30):"OpenAI has contracted to purchase an incremental $ 250 billion of Azure services, and Microsoft will no longer have a right of first refusal" https://www.sec.gov/Archives/edgar/data/789019/000119312525256321/msft-20250930.htm
F21 2026-04-27 再修订(微软官方博客)https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/
> "Revenue share payments from OpenAI to Microsoft continue through 2030, independent of OpenAI's technology progress, at the same percentage but subject to a total cap." ; "Microsoft will no longer pay a revenue share to OpenAI." ; "Microsoft's license will now be non-exclusive."

## H. Amazon(10-Q 截至 2026-06-30,官方)https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
F22 Q2 2026:经营利润 $27,461M;Other income $53,415M;税前 $80,857M。
> "The upward adjustments relating to equity investments in private companies of $ 50.5 billion in Q2 2026 ... reflect observable changes in prices, primarily from our nonvoting preferred stock in Anthropic."
F23 Anthropic:2023Q3–2025Q4 投 $8.0B 可转债;2026Q2 再投 $10B(Series G $5B + Series H $5B);另设 ≤$20B 融资额度,"as we reach certain delivery milestones of compute capacity ... amounts under this facility are made available for Anthropic to draw"——融资额度直接挂钩算力交付。
> "In Q2 2026, AWS and Anthropic announced an expansion of the strategic collaboration and existing multi-year commitment by more than $ 100.0 billion over 10.0 years, which includes contractual obligations related to the performance of AWS chips."
F24 OpenAI:> "In Q1 2026, AWS and OpenAI Group PBC (“OpenAI”) announced an expansion of the existing $ 38.0 billion multi-year commitment ... by $ 100.0 billion over 8.0 years"; Amazon 投 $15.0B Series C + $35.0B 承诺额,"Subsequent to June 30, 2026, we funded the remaining Commitment Amount of $21.3 billion"(即 $50B 已全部落地)。
F25 AWS 未确认承诺 "approximately $ 496 billion as of June 30, 2026";H1 资本开支 $98.4B。

## I. Alphabet(10-Q 截至 2026-06-30,官方)https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
F26 > "OI&E of $98.0 billion for the three months ended June 30, 2026 included net gains on equity securities of $99.0 billion, primarily related to unrealized gains in our equity securities portfolio from SpaceX and a private company."  经营利润 $40,770M vs 税前 $138,753M。
> "we had $ 519.5 billion of remaining performance obligations (“revenue backlog”), of which $ 513.9 billion related to Google Cloud"; 非上市股权 $124.3B。H1 资本开支 $80.6B。
("a private company" 未具名;Anthropic 为高度可能但未经该文件证实——标注推断)

## J. 收入缺口测算的 2026 更新
F27 Cahn "AI's $1.5T Question"(2026-07-08,Substack,从业者/VC)https://dcahn.substack.com/p/ais-15t-question
> "Take Nvidia's projected Q4 run-rate data center revenue x 2 (to reflect total data center CapEx, including non-chip expenses) x 2 (to reflect a 50% margin across the hyperscaler and the AI product company). This analysis arrives at the lifetime end-customer revenue requirement for a single year of CapEx."
> "if you wanted to know the total required revenue for today's AI buildout (cumulatively) since ChatGPT, you'd add up the numbers and arrive at roughly $3T of lifetime required revenue thus far."
> "most forecasts have 2026 hyperscaler data center CapEx in the $750B ballpark"
口径警示:$1.5T = 单一年(2026)capex 对应的"终身"终端收入需求,不是年收入;$3T = ChatGPT 以来累计。媒体(TechCrunch 2026-07-09 等)常写成"需要 $3T 收入来证明 2026 投入"——口径错误。
注意:"50% margin across the hyperscaler and the AI product company" 是把云+模型/应用合并当作一层的假设毛利。

F28 Bain 第 7 份 Global Technology Report(2026-09-29,分析机构)https://www.bain.com/about/media-center/press-releases/2026/global-ai-market-could-hit-$6-trillion-annually-by-2031-through-unlocking-value-and-innovation--bain--cos-7th-global-technology-report/ ; https://www.bain.com/insights/new-innovation-is-required-to-fund-ais-6-trillion-buildout-technology-report-2026/
> "funding AI's insatiable compute demand would require $6 trillion in annual revenue by 2031"
> "By 2031, annual spending on AI infrastructure could reach $1.5 trillion ... If we assume that capital expenditures amount to about 25% of industry revenue ... sustaining this level of investment would require an AI market approaching $6 trillion annually."
> "Consumer AI ... and enterprise AI ... could total between $1.2 trillion and $1.8 trillion in revenue." ; "the remaining $4.2 trillion of new revenue"
对比 2025 版:2030 年 $500B/yr capex → $2T 收入、缺口 $800B;2026 版:2031 年 $1.5T/yr capex → $6T、缺口约 $4.2T。一年内缺口估算 ×5。

F29 JPMorgan(2025-11,分析机构,媒体转述 Tom's Hardware)https://www.tomshardware.com/tech-industry/artificial-intelligence/usd650-billion-in-annual-revenue-required-to-deliver-10-percent-return-on-ai-buildout-investment-j-p-morgan-claims-equivalent-to-usd35-payment-from-every-iphone-user-or-usd180-from-every-netflix-subscriber-in-perpetuity
约 $650B/年永续收入才能让 2030 前 AI 投资获 10% 回报;全球 AI/数据中心 capex 至 2030 约 $5T+。

F30 Morgan Stanley(2025-07,分析机构)https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Research_Bridging-Data-Center-Gap.pdf (PDF 未能抓取,数据来自转述)
2028 年前全球数据中心 capex 约 $2.9T(硬件 $1.6T、基建 $1.3T);超大厂自有现金流覆盖约 $1.4T,融资缺口约 $1.5T,其中私募信贷约 $800B。

## K. 各层收入/毛利美元额的第三方估算
F31 Apoorv Agrawal "The Economics of Generative AI: Two Years Later"(2026-04-01,从业者博客)https://tailwinds.substack.com/p/the-economics-of-generative-ai-two
生态总收入约 $435B:半导体约 $300B(69%)、基础设施约 $75B(17%)、应用约 $60B(14%);毛利:半导体约 $225B(~73% GM)、基础设施约 $40B(~55%)、应用约 $20B(~33%)。
> "Semis capture 79% of all gross profit dollars in the AI ecosystem"
> "the semi layer added ~$225B vs ~$55B for apps"
口径:作者自建数据表、非审计;"应用层"含 OpenAI/Anthropic(约 $45B 年化,run-rate 口径)。属当下利润分布,非长期落点。

## L. 前沿实验室(非上市,厂商自报/媒体转述)
F32 Anthropic 官方(2026-04-06)https://www.anthropic.com/news/google-broadcom-partnership-compute
> "Our run-rate revenue has now surpassed $30 billion—up from approximately $9 billion at the end of 2025"
F33 Anthropic 投资人更新(2026-08-17,媒体转述 Bloomberg/CNBC/Yahoo)https://finance.yahoo.com/technology/ai/articles/anthropic-revenue-run-rate-hits-111710007.html :run-rate 7 月底超 $65B;Q2 初步收入超 $11.5B(去年同期 $787M);"positive adjusted operating income for the quarter"(调整后口径)。
F34 OpenAI(媒体转述,The Information/TNW 2026-09-19)https://thenextweb.com/news/openai-856bn-compute-vs-600bn-reset-burn-improved :2 月对投资人称 2030 前算力支出约 $600B(此前 Altman 称 $1.4T 承诺);7 月推介材料为 $856B;2026–2030 负自由现金流 $278B;2026 收入约 $36B,2030 目标 $350B。Q1 2026 收入 $5.7B、烧钱 $3.7B(The Information)。
> 关键机制(TNW 概括):支出上调而烧钱下降,因为 NVIDIA、Oracle、SB Energy 等合作方用自己资产负债表承接了基建融资。
F35 Google–Anthropic(2026-04-24,TechCrunch 媒体转述)https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/ :先投 $10B(估值 $350B),达标再投 $30B;Google Cloud 未来五年新增 5GW。
F36 Anthropic–Microsoft–NVIDIA(2025-11-18,官方)https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships :Anthropic 承诺购买 $30B Azure 算力;NVIDIA 至多投 $10B、微软至多 $5B;初始至多 1GW Grace Blackwell/Vera Rubin。

## M. 芯片层"商品化互补品"
F37 NVIDIA 8-K(2026-09-03)收购 Hugging Face 约 $11.9B https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm
> "Demand for open-source foundation models and applications based on them promotes the use of our products worldwide and sustains the Hugging Face platform."
F38 NVIDIA 8-K(2026-08-17)SB Energy 残值担保 https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm
> "NVIDIA’s aggregate payment obligation is cumulatively capped at $105 billion for its initial commitment" ; "OpenAI has agreed to reimburse and indemnify NVIDIA for any and all amounts actually paid by NVIDIA to the Lessor"

## N. NVIDIA Q2 FY27 电话会(2026-08-26,FactSet 修订逐字稿,官方 IR 托管)https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf
F39 Kress:
> "First, we've invested nearly $50 billion in the frontier AI labs."
> "we recently announced partnerships with six of the world's leading infrastructure capital providers; Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR, to establish financing platforms that will raise over $500 billion of third-party capital."
> "OpenAI's existing and planned commitments represent approximately 12 gigawatts of NVIDIA Compute. For another frontier AI lab, we will provide selective credit enhancement for nearly 2 gigawatts of compute."
> "We recognize the scale of this support, and we know some will call this circular financing. We see it differently."
> "we expect demand from the AI labs for which we expect to leverage our balance sheet to contribute toward roughly a quarter of our business next year."
F40 新云收入分成结构:
> "NVIDIA provides a take-or-pay commitment on a portion of the facility's capacity, a minimum revenue guarantee that gives lenders the confidence to underwrite the project, and in exchange, we share in a portion of the neoclouds revenue earned above that floor. ... In this model, we get paid twice, once on the hardware sale and again through the share of rental revenue"
F41 分析师 Vivek Arya(BofA):把 CFO 评论里的承诺与担保加总 "I get to a number of about $500 billion or so ... over the next several years";并指出 OpenAI 与 Anthropic 都在做自研芯片(OpenAI "Jalapeño")。
Huang:"the only regret that I have is that I didn't invest more and sooner."

## O. 2026 年取消/缩减(媒体转述)
F42 Bloomberg 2026-03-06:Oracle 与 OpenAI 终止 Abilene 旗舰园区扩建计划(原 1.2GW 扩至约 2GW),原因融资谈判拖延、OpenAI 需求预测变动 https://www.bloomberg.com/news/articles/2026-03-06/oracle-and-openai-end-plans-to-expand-flagship-data-center ;另有报道 OpenAI 实际放弃自建 Stargate、改为租赁算力,由合作方承担直接投资风险 https://finance.yahoo.com/sectors/technology/articles/openai-effectively-abandoned-first-party-160031027.html
F43 NVIDIA $100B LOI(2025-09)→ 2026-01-31 WSJ 报暂停 → 2026-02 落地 $30B 股权 → 2026-08 改以 $105B 上限租约担保方式支持(F7/F38)。

状态:完成(2026-10-05)

## P. Oracle–OpenAI 原始口径
F44 Oracle 8-K(2025-06-30,官方)https://www.sec.gov/Archives/edgar/data/1341439/000119312525152035/d136779d8k.htm
> "we signed multiple large cloud services agreements including one that is expected to contribute more than $30 billion in annual revenue starting in FY28." ; "Amounts ultimately recognized from the contract noted above may vary"
注:"$300B/5 年"与"OpenAI 为对手方"来自 WSJ 等媒体及 OpenAI 4.5GW 公告,Oracle 文件本身未点名 OpenAI、未给 $300B 总额。
