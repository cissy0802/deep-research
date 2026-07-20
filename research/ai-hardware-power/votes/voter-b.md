# 对抗验证 · 验证者 B 判决(#15 AI 硬件短缺与电力短缺)

> 方法:refute-by-default,逐组回一手来源(官方新闻稿 PDF、财报稿、TrendForce 原稿、ERCOT/PJM/DOE/IEA/LBNL/Grid Strategies 原文)逐字核对分子、分母、时间窗、限定语。独立运行,未见其他验证者结论。
> 汇总:HOLDS 7(G4/G5/G6/G8/G9/G10/G11),修正 5(G1/G2/G3/G7/G12),推翻 0。

---

## G1 三家内存厂 2026 产能售罄 —— 判决:修正

**依据:**
- SK Hynix:2025-10-29 Q3 财报口径,HBM/常规 DRAM/NAND 2026 全线售罄,多家独立媒体同向转述(TechSpot、Blocks & Files),且有 SEC F-1/424B4 申报在途可回溯。成立。
- Micron:2026 HBM 产出全部签约/售罄,出自财报电话会,多源转述一致(Yahoo Finance、Investing.com)。成立。
- Samsung:一手只支持 **2026 年 HBM(HBM4)供给售罄**——2025-10-30 财报会,存储 EVP Kim Jae-june:"We've significantly expanded our HBM production for next year… yet customer demand has already outpaced supply"(KED Global 转录)。**没有 Samsung 全线(DRAM/NAND)售罄的一手表述。**

**修正前→后:**"三家内存厂 2026 年产能整体售罄" → "SK Hynix 2026 DRAM/NAND/HBM 全线售罄;Micron 2026 HBM 全部签约;Samsung 为 2026 HBM(HBM4)口径售罄,非全线。'三家整体售罄'仅在 HBM 品类上成立"。

**一手/最近似一手 URL:**
- https://www.techspot.com/news/110058-sk-hynix-completely-sells-out-semiconductor-supply-ai.html
- https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm(SK Hynix 424B4)
- https://www.kedglobal.com/earnings/newsView/ked202510300005(Samsung 财报会转录)
- https://finance.yahoo.com/news/micron-sold-2026-hbm-us-231248051.html

---

## G2 TrendForce 价格链 + 消费端传导 —— 判决:修正(一处;主体成立)

**依据(逐字命中):**
- TrendForce 2026-03-31 原始新闻稿:"Conventional DRAM contract prices expected to rise 58–63% QoQ in 2Q26";"NAND Flash contract prices are expected to rise by 70–75% QoQ in 2Q26"。✓
- Q3 放缓:TrendForce 2026-07-03 原稿,3Q26 常规 DRAM 合约价 +13–18% QoQ、NAND +10–15%(另 2026-07-09 稿:server DRAM 13–18%,LTA 封顶涨幅)。✓
- 16GB DDR4 零售 $137→$207.1(+51%):wccftech 零售价追踪口径,单源媒体,方向可用、精度不承重。✓(降级注明)
- HP CFO Karen Parkhill(Q1 FY2026 电话会,2026-02 末):"memory and storage costs made up roughly 15% to 18% of our PC bill of materials, and we now currently estimate this to be roughly 35% for the year"。逐字命中(PC Gamer/The Register 独立同向)。✓

**推翻的子句:**"媒体流传的 +89-90% 是现货/特定型号口径"——**不成立**。TrendForce 2026-02-02 原稿显示 ~90% 是 **1Q26 常规 DRAM 合约价**上调后口径(55–60% 上修至 90–95%;PC DRAM >100%、server DRAM ~90%、LPDDR4X/5X ~90%,全部为合约价,非现货);而"+89%"未在 TrendForce 一手命中——官方 2026-05-14 稿 2Q26 LPDDR5X 为 **78–83%**,"up to 89%" 系媒体(wccftech)加工。

**修正前→后:**"+89-90% 是现货/特定型号口径" → "+90% 是 TrendForce 1Q26 常规 DRAM 合约价口径(90–95%,上一季度),+89% 无一手支撑(2Q26 LPDDR5X 官方为 78–83%)。防混引结论不变:任何 ~90% 数字都不可与 2Q26 常规 DRAM 合约价 +58–63% 混引"。

**一手 URL:**
- https://www.trendforce.com/presscenter/news/20260331-12995.html
- https://www.trendforce.com/presscenter/news/20260202-12911.html
- https://www.trendforce.com/presscenter/news/20260703-13134.html
- https://www.trendforce.com/presscenter/news/20260709-13140.html
- https://www.trendforce.com/presscenter/news/20260514-13044.html
- https://www.pcgamer.com/hardware/memory/hp-warns-that-memory-now-makes-up-around-35-percent-of-the-cost-its-pcs-double-that-of-a-year-ago/

---

## G3 CoWoS 绑定约束 —— 判决:修正

**依据:**
- "CoWoS 2026 售罄"出自 TSMC CEO 口径(财报会),多家独立转述同向;"绑定约束在先进封装"为分析师共识,方向成立。✓
- "产能年增 ~80%":流通估算 2024→2025 约 37 万→67 万片(+81%)支持"~80%";但 2025→2026 为 67 万→约 100 万片(≈+50%),月产能 75–80k→120–130k WPM(≈+60%)。**"~80% 年增"只对 2025 成立,引用必须带年份。**
- **内部矛盾:**"NVIDIA 锁定 60%+ 份额"(TrendForce 口径:~60% ≈ 59.5 万片,总量 ~100 万片)与"2026 约 80-85 万片 wafer"(wccftech 一路口径)**不能同时成立**——80-85 万片对应 ~80-85% 份额。两路口径来自不同转述链。

**修正前→后:**"NVIDIA 锁定 60%+ 份额(2026 约 80-85 万片 wafer)" → "NVIDIA 份额 ~60%(TrendForce 估算,≈59.5 万片/总需求 ~100 万片);'80-85 万片'为另一路媒体口径,与 60% 不自洽,弃用或单列为存争数字。'年增 ~80%'限定为 2024→2025,2026 年增速约 +50%"。

**URL(均为分析师/媒体估算,无厂商一手数字——本组整体只能以'分析师口径'承重):**
- https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/
- https://www.astutegroup.com/news/industrial/advanced-packaging-demand-soars-nvidia-secures-60-of-cowos-capacity/
- https://www.digitimes.com/news/a20251210PD218/tsmc-cowos-capacity-nvidia-equipment.html
- https://www.cnbc.com/2026/04/08/tsmc-nvidia-advanced-packaging-intel.html

---

## G4 PJM 容量拍卖价格链 —— 判决:HOLDS

**依据(PJM 2026-07-14 新闻稿 PDF 全文逐字核):**
- "The price came in at the FERC-approved cap, $325/MW-day (UCAP)… a 2.5% decrease from the 2027/2028 Base Residual Auction cap of $333.44/MW-day" ✓
- "secured 138,318 MW of unforced capacity" ✓;"short of PJM's reliability requirement by 6,831 MW" ✓;"a shortfall of approximately 6,500 MW in the previous capacity auction (for the 2027/2028 Delivery Year)" ✓
- "This was the third consecutive auction with the price collar"(三次全部触顶:$329.17/$333.44/$325.00)✓
- 早期链条:2026/27 BRA 报告 "$329.17… an increase from $269.92";2025/26 BRA $269.92(自 2024/25 的 $28.92)——PJM 官方拍卖报告一手命中。✓
- CEO David Mills 原话:"demand for electricity continues to grow faster than electricity supply" ✓

**一手 URL:**
- https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf
- https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2026-2027/2026-2027-bra-report.pdf
- https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.pdf
- https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2025-releases/20251217-pjm-auction-procures-134479-mw-of-generation-resources.pdf

---

## G5 Monitoring Analytics 数据中心归因 —— 判决:HOLDS

**依据:**报告为 Monitoring Analytics 2026-01-05《Analysis of the 2027/2028 RPM Base Residual Auction – Part A》。三个数字全部命中独立转述(Utility Dive + Bloomberg 双源同向):
- 数据中心占 2027/28 拍卖容量成本 40%($6.5B / $16.4B)✓
- 其中 ~$6.2B 来自尚未建成、但可能在 2027/28 交付年上线的数据中心 ✓
- 近三次基础拍卖:超出存量的数据中心预测负荷贡献 $21.3B,占 $47.2B 清算成本的 45% ✓(限定语"beyond existing data centers"与声称一致)
- MM 原话:"Data center load growth is the primary reason for recent and expected capacity market conditions…" ✓

**URL:**
- https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/
- https://www.bloomberg.com/news/articles/2026-01-05/data-centers-added-6-5-billion-to-secure-power-for-big-us-grid
- https://www.monitoringanalytics.com/reports/Reports/2025/IMM_Analysis_of_the_20262027_RPM_Base_Residual_Auction_Part_A_20251001.pdf(同系列上一期 Part A,佐证报告体例;2026-01-05 版同站可检索)

---

## G6 ERCOT 大负荷队列 —— 判决:HOLDS(附小注)

**依据(ERCOT 一手 PDF 逐字核):**
- 2026-04-01 ERCOT CEO Pablo Vegas 参议院听证材料:"ERCOT is tracking approximately 410 GW of Large Loads seeking interconnection of which ~87% are data centers"(数据截至 2026-03-26)✓
- 2026 年中 438 GW、~90% 数据中心:Utility Dive 转 ERCOT/PUCT("large users totaling more than 438,000 MW… nearly 90% from data centers")✓
- Q1 2026 单季新增 198 GW:Ascend Analytics("198 GW of large load applied for interconnection in the first quarter of 2026 alone")——独立二手,单源,建议标注来源。✓(降级注明)
- 历史峰值:ERCOT 官方纪录 85,508 MW(2023-08),2025 夏峰 83.9 GW——"~85 GW"成立。✓

**小注:**"2026-04 官方 ~410 GW"的数据日期是 3 月 26 日、4 月 1 日呈报,建议写"2026-03 末/04 初"。

**一手 URL:**
- https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf
- https://www.utilitydive.com/news/texas-facing-438-gw-queue-approves-initial-large-load-interconnection-pro/823367/
- https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access
- https://www.ercot.com/static-assets/data/news/content/a-peak-demand/all-time-records.htm

---

## G7 GE Vernova Q1 2026 —— 判决:修正

**依据(GEV 官方新闻稿 + 电话会转述逐字核):**
- **口径错误:**GEV 一手原文:"**Gas Power equipment backlog and slot reservation agreements** grew from 83 to 100 GW"——100 GW 与 83 GW 都是 **backlog+slot reservation 合并口径**,不是"签约 backlog";110 GW 年底目标同口径("now anticipate reaching at least 110 GW by year-end 2026")。
- Strazik 原话命中:"about 10 GW of turbine production capacity remaining through 2030 and continue[s] to expect to take on orders for 2031 and beyond" ✓
- 价格命中:"10% to 20% growth in price on new bidding and winning activity today relative to where we were in the backlog in the fourth quarter of last year" ✓(注意限定:相对去年 Q4 backlog,非"环比涨价")
- 电气化:订单 +86%(organic YoY,$7.1B,book-to-bill ~2.5),backlog $25B→$42.4B ✓;Q1 新签燃机 21 GW(19 GW 入 slot reservation、2 GW 直接入 order)——进一步证明合并口径。
- 三大 OEM lead time 最长 7-8 年:IEEFA 2025-10 报告 + 行业多源("planning according to seven to eight-year timelines")✓

**修正前→后:**"燃机签约 backlog 100 GW(上季 83 GW),年底目标 110 GW(含 slot reservation)" → "燃机设备 backlog+slot reservation 合并口径 100 GW(2025 年底 83 GW,同口径),年底目标 ≥110 GW(同口径);其中 Q1 新签 21 GW 里 19 GW 是 slot reservation 而非签约订单"。

**一手 URL:**
- https://www.gevernova.com/news/press-releases/ge-vernova-reports-first-quarter-2026-financial
- https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm(8-K)
- https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-hits-100-gw-as-prices-rise/818332/(电话会引语)
- https://ieefa.org/sites/default/files/2025-10/IEEFA%20Report_Global%20gas%20turbine%20shortages%20add%20to%20LNG%20challenges%20in%20Vietnam%20and%20the%20Philippines_October2025.pdf

---

## G8 核电时间表 —— 判决:HOLDS(附小注)

**依据:**
- Crane(前三里岛 1 号):835 MW ✓;微软 20 年 PPA、2024-09 签 ✓(Constellation 2024-09-20 公告);DOE LPO $10 亿贷款 2025-11 financial close(首例条件承诺与交割同步)✓;重启从 2028 提前至 2027(Constellation CEO Dominguez)✓。
- Google-Kairos:2024-10 Master Plant Development Agreement,500 MW 到 2035;首堆 = TVA 田纳西 Hermes 2(50 MWe),2030 年运营 ✓。
- Amazon-X-energy:2024-10-16 ~$5 亿 C-1 轮领投;初期 320 MW(Cascade,Energy Northwest,4×Xe-100),"construction by end of decade, operations targeted to start in the 2030s";目标 2039 年前 >5 GW ✓。
- 美国目前无商业 SMR 并网:成立(Hermes 系示范堆在建,无商业 SMR 发电并网)。

**小注:**"初期 ~320 MW **2030 年代早期**投运"中"早期"是项目方/媒体推断,官方表述为"2030s"——建议写"2030 年代(官方口径),业界预期偏早期"。

**一手 URL:**
- https://www.energy.gov/edf/crane-restart
- https://www.constellationenergy.com/about/locations/crane-clean-energy-center.html
- https://www.kairospower.com/updates/google-kairos-power-tva-collaborate-to-meet-americas-growing-energy-needs
- https://blog.google/company-news/outreach-and-initiatives/sustainability/google-kairos-power-nuclear-energy-agreement/
- https://x-energy.com/news/amazon-invests-in-x-energy-to-support-advanced-small-modular-nuclear-reactors-and-expand-carbon-free-power/

---

## G9 IEA / LBNL / 历史前科 —— 判决:HOLDS

**依据(IEA 官方页面逐字命中):**
- "global electricity consumption for data centres is projected to double to reach around 945 TWh by 2030 in the Base Case… representing just under 3% of total global electricity consumption in 2030" ✓
- 美 "+around 240 TWh (up 130%)"、中 "+around 175 TWh (up 170%)"、欧 "+more than 45 TWh (up 70%)" ✓
- 2035 情景:Lift-Off "exceeding the 1 700 TWh mark"、High Efficiency "around 970 TWh"、Headwinds "plateau… at around 700 TWh" ✓
- LBNL/DOE:"data centers consumed about 4.4% of total U.S. electricity in 2023"(176 TWh,自 2014 年 58 TWh)、"325 to 580 TWh by 2028"(6.7–12%)✓
- 历史前科:①Forbes 1999(Huber/Mills)称互联网 8%/全部计算机 13%、将达一半——Koomey 等(LBNL-46509 及后续)拆穿:2000 年互联网 <1%、全部计算机 ~3%;②2007 EPA 报告预测远超实际(Koomey 2011:2005–2010 增速远低于预测);③Masanet et al., Science 2020:2010–2018 全球数据中心用电仅 +6%(~205 TWh,约占全球 1%),算力/应用 +550%。✓("2020 实际 1-2%"为美国口径近似,方向成立)

**一手 URL:**
- https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
- https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf
- https://www.science.org/doi/10.1126/science.aba3758
- https://eta-publications.lbl.gov/sites/default/files/lbnl-46509.pdf

---

## G10 Google 效率测量 vs 总量 —— 判决:HOLDS

**依据:**
- Google Cloud 官方博客(2025-08)+ arXiv 2508.15734:中位 Gemini Apps 文本 prompt 0.24 Wh、0.03 gCO2e;12 个月窗口(2024-05→2025-05)能耗 33×、碳 44× 改善。口径限定(中位、纯文本、不含训练/图像/视频)与声称一致。✓
- 总量:Google 2025 环境报告口径——数据中心用电 2020→2024 翻倍;2024 排放 11.5 Mt,较 2019 +51%("+~50%"成立)。✓

**一手 URL:**
- https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
- https://arxiv.org/abs/2508.15734
- https://blog.google/company-news/outreach-and-initiatives/sustainability/environmental-report-2025/

---

## G11 Nadella BG2 引语 —— 判决:HOLDS(日期小注)

**依据:**多家独立转录逐字一致(Tom's Hardware、DCD、TechSpot):
"The biggest issue we are now having is not a compute glut, but it's power – it's sort of the ability to get the builds done fast enough close to power. So, if you can't do that, you may actually have a bunch of chips sitting in inventory that I can't plug in. In fact, that is my problem today. It's not a supply issue of chips; it's actually the fact that I don't have warm shells to plug into."
声称的省略号拼接忠实原意,无断章。✓
**小注:**播客发布于 2025-10-31/11-01,媒体报道 2025-11-03;标"2025-11"可接受,精确可写"2025-10-31 发布"。另:微软 CFO Amy Hood 在 FY26Q1 电话会有同向表述(空间/电力而非芯片是约束),可作第二锚点。

**URL:**
- https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-ceo-says-the-company-doesnt-have-enough-electricity-to-install-all-the-ai-gpus-in-its-inventory-you-may-actually-have-a-bunch-of-chips-sitting-in-inventory-that-i-cant-plug-in
- https://www.datacenterdynamics.com/en/news/microsoft-has-ai-gpus-sitting-in-inventory-because-it-lacks-the-power-necessary-to-install-them/

---

## G12 NERC vs Grid Strategies + 账单 —— 判决:修正

**依据:**
- **归因错误:**"5 年峰值 +166 GW(~90 GW 数据中心)"不是 NERC 的数字。一手为 Grid Strategies《National Load Growth Report 2025》(Wilson et al., 2025-11/12):对公用事业 **FERC 申报**的汇总——"the planning areas now anticipate 166 GW in load growth"、五年预测三年间从 24 GW 增至 166 GW(6 倍)、"Of the 166 GW of forecast peak load growth, roughly 90 GW are linked to data centers"。NERC 2025 LTRA(2026-01 发布)自身口径:2030 年前 ~160 GW(含 90 GW 数据中心,系公用事业申报滚汇),十年夏季峰值 +24%(Utility Dive 转 NERC)。
- 40% 高估:GS 报告原文:"FERC-submitted load forecasts collectively overstate data center-driven load growth by about 40%"(90 GW 中约 25 GW,亦即 ~65 GW 更可信)✓
- 60–65 GW:GS《Review of NERC's 2025 LTRA》(2026-03-05,受 Earthjustice/NRDC/Sierra Club/EDF 委托——注意委托方立场):"Scheduled by 2029 ~60 GW"、"Projection based on chip shipments ~65 GW"(TD Cowen)vs "Aggregated utility forecast ~90 GW" ✓
- 账单:Pepco(DC)2025-06 起平均 +$21/月、约半数归因容量价;西马里兰 +$18/月;俄亥俄 ~$16/月——消费者组织/OPC 对费率文件的计算,多家媒体转述同向,数字本身未独立复算(维持"倡导组织口径"分级)。✓

**修正前→后:**"NERC:5 年峰值 +166 GW(~90 GW 数据中心)、十年峰值 +24%" → "Grid Strategies 汇总公用事业 FERC 申报:5 年峰值 +166 GW(~90 GW 数据中心,~55%);NERC 2025 LTRA:2030 年前 ~160 GW(含 90 GW 数据中心)、十年夏季峰值 +24%。两者同根(都源自公用事业申报),Grid Strategies 的 40% 高估批评同时打向两个数字"。

**一手 URL:**
- https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf
- https://gridstrategiesllc.com/wp-content/uploads/FINAL-2025-LTRA-Review.pdf
- https://www.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf
- https://www.utilitydive.com/news/nerc-10-year-peak-demand-forecast-jumps-24-on-new-data-center-loads/810955/
- https://www.utilitydive.com/news/nerc-overstates-reliability-risks-ltra-grid-strategies/814292/
