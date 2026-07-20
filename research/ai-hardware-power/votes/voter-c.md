# 对抗验证 · 验证者 C 判决(#15 AI 硬件短缺与电力短缺)

> 方法:refute-by-default,逐组回一手/最接近一手的来源核对分子、分母、时间窗、限定语。检索时间 2026-07-20。
> 统计:HOLDS 8 组(G4、G5、G6、G7、G8、G9、G10、G11),修正 4 组(G1、G2、G3、G12),推翻 0 组。

## G1 三家内存厂 2026 产能售罄 —— 判决:修正

- **SK Hynix HOLDS**:2025-10 财报电话会称 HBM/DRAM/NAND 2026 年产能 "essentially sold out",多源一致;另有 SEC F-1/424B4 申报可回溯(2026 年 Q1 DRAM 份额 29.1%、HBM 56.4%)。
- **Micron HOLDS**:FY26 Q1 财报电话会 prepared remarks(官网 PDF):"completed agreements on price and volume for its entire calendar 2026 HBM supply, including HBM4"。口径限定 = HBM,与论断一致。
- **Samsung 需限定**:一手可回溯的表述是 **HBM 2026 全部售罄、2027 提前接单**(2025-10-30 电话会起,Q1 2026 电话会重申;HBM4 已量产、2026 HBM 销售额预计 3 倍+),外加"全行业短缺"警告——**没有查到 Samsung"整体产能售罄"的一手表述**。
- **修正前→后**:"三家 2026 年产能整体售罄" → "SK Hynix 全线(DRAM/NAND/HBM)售罄;Micron 2026 HBM 全部签约;Samsung HBM 售罄并警告全线短缺——'整体售罄'仅 SK Hynix 一家有一手表述"。
- URL:https://www.techspot.com/news/110058-sk-hynix-completely-sells-out-semiconductor-supply-ai.html · https://investors.micron.com/static-files/088991c5-a249-4f66-a0a6-258d9b66f3f9 · https://www.kedglobal.com/earnings/newsView/ked202510300005 · https://www.digitaltoday.co.kr/en/view/52267/samsung-electronics-says-all-hbm-capacity-sold-out-sees-2026-sales-tripling · https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm

## G2 TrendForce 价格链 + 消费端传导 —— 判决:修正(两处口径)

- **HOLDS(逐字核对原稿)**:TrendForce 2026-03-31 新闻稿:2Q26 常规 DRAM 合约价 +58-63% QoQ、NAND +70-75% QoQ ✓;2026-07-03 新闻稿:3Q26 常规 DRAM +13-18%(NAND +10-15%),动因=消费端触及承受力上限+高基数 ✓;CSP 签 LTA 锁供给 ✓。
- **修正 1("+89-90% 是现货口径")**:89% 的一手口径是 **mobile LPDDR5X 特定型号的合约价**(96Gb/12GB 模组 $77.1→$145.9,2Q26 +89% QoQ,TrendForce 系报道),**不是现货**;另一个流传的 "90-95%" 是 TrendForce 自己的 **1Q26 常规 DRAM 合约价实录**(创纪录)。→ 修正为:"89% = LPDDR5X 特定型号合约口径;90-95% = 1Q26 常规 DRAM 合约实绩;两者都不是 2Q26 常规 DRAM 合约口径,不可混引"。
- **HP CFO HOLDS(补时间窗)**:HP FY26 Q1 电话会(2026-02-25/26),CFO Karen Parkhill:内存(含存储)占 PC BOM 从上季 15-18% 升至 ~35%,单季成本 ~+100%。多源逐字一致。
- **修正 2(16GB DDR4 $137→$207)**:未能回溯到该组数字的一手(Tom's Hardware 价格指数付费墙内)。方向性证据反而更强:16GB DDR4 芯片现货一年 $3.20→~$74(+2,200%,2026-07 首现回落 5%)。→ 建议:$137→$207(+51%) 若无法补出处(具体 kit + 时间窗),用可回溯的现货/零售序列替代。
- URL:https://www.trendforce.com/presscenter/news/20260331-12995.html · https://www.trendforce.com/presscenter/news/20260703-13134.html · https://en.sedaily.com/finance/2026/06/23/mobile-dram-prices-seen-surging-89-percent-as-consumer · https://www.tomshardware.com/pc-components/dram/dram-and-nand-contract-prices-to-climb-again-in-q2 · https://www.tomshardware.com/tech-industry/hp-says-memory-costs-doubled-to-35-percent-of-pc-build-materials-in-one-quarter · https://www.tomshardware.com/tech-industry/ddr4-spot-prices-fall-for-first-time-in-nearly-a-year-as-chinese-channel-inventory-clears

## G3 CoWoS 绑定约束 —— 判决:修正(wafer 数与增速)

- **HOLDS**:2026 CoWoS 售罄(TSMC CEO 魏哲家 2026-06-04 股东会 "extremely tight and sold out through 2026",二级转述一致;TrendForce 2026-04-30 新闻稿确认短缺自 2023 持续);NVIDIA 锁定 ~60% 份额 ✓(Morgan Stanley/TrendForce 口径)。
- **修正 1(wafer 数)**:主流估算是 **NVIDIA 2026 年 ~59.5 万片**(占全球总需求 ~100 万片的 60%;其中 TSMC ~51 万片,余 Amkor/ASE),"80-85 万片"仅见于个别 outlier 来源。→ "2026 约 80-85 万片" → "~59.5 万片(占 ~100 万片总需求的 60%;Broadcom 15 万/AMD 10.5 万)"。若保留 80-85 万,必须注明是少数派估算且与 60% 份额自相矛盾(80-85 万/100 万 = 80-85%)。
- **修正 2(增速)**:"产能年增 ~80%" 对应的是 **2025 年**(需求 37 万→67 万片,+81%);2026 年为 67 万→100 万(+49%),TSMC 官方口径是"到 2027 年扩产 60%+"。→ 需加年份限定。
- URL:https://eu.36kr.com/en/p/3580962946874242 · https://www.trendforce.com/presscenter/news/20260430-13028.html · https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026 · https://www.digitimes.com/news/a20251210PD218/tsmc-cowos-capacity-nvidia-equipment.html

## G4 PJM 容量拍卖价格链 —— 判决:HOLDS

- 2028/29 BRA(2026-07-14 公布):清算价 $325/MW-day 触 FERC 上限、连续第三次;采购 138,318 MW(UCAP);距可靠性要求缺 **6,831 MW**(上次 ~6,500 MW)——与 PJM Inside Lines/新闻稿逐项一致。负责人引语"Demand for electricity continues to grow faster than electricity supply"(PJM President David Mills)。
- 价格链 $28.92(2024/25)→$269.92(2025/26)→$329.17(2026/27)→$333.44(2027/28,record)与 PJM 历次公告及多家独立复述一致(modo/JEPIC:$325 较上次 $333.44 微降 ~2.5%)。
- URL:https://insidelines.pjm.com/pjm-capacity-auction-procures-138318-mw-of-generation-resources-as-work-continues-to-address-growing-electricity-demand/ · https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf · https://modoenergy.com/research/en/pjm-capacity-auction-2028-2029-reliability-price-cap-elcc

## G5 Monitoring Analytics 数据中心归因 —— 判决:HOLDS

- 报告 2026-01-05 发布(周一),两家独立媒体逐字一致:2027/28 拍卖数据中心负荷占容量成本 **40%($6.5B/$16.4B)**,其中 **$6.2B** 来自未建成但可能在 2027-06-01 前投运的数据中心;近三次 BRA 累计,超出存量的数据中心预测负荷贡献 **$21.3B(占 $47.2B 的 45%)**;IMM 明确"数据中心负荷增长是近期容量市场状况的首要原因"。
- 注:我经由 Bloomberg/Utility Dive 交叉,不是 Monitoring Analytics PDF 本体;数字两家逐字一致,判 HOLDS,建议成文引 IMM 报告原件(monitoringanalytics.com)。
- URL:https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/ · https://www.bloomberg.com/news/articles/2026-01-05/data-centers-added-6-5-billion-to-secure-power-for-big-us-grid

## G6 ERCOT 大负荷队列 —— 判决:HOLDS

- ~410 GW(87% 数据中心,2026-04/05 官方口径,RTO Insider 报道 + ERCOT 2026-04-01 参议院听证材料存在于 ercot.com);2026 年中 438 GW(Utility Dive "nearly 90%",另源 "nearly 89%");2026 Q1 单季新增 198 GW ✓;Oncor 区 259 GW;系统历史峰值 ~85 GW ✓(队列 ≈ 峰值 5 倍)。
- 小限定:438 GW 语境是 PUCT 批准大负荷互联新规("Batch Zero")报道,"~90%" 实为 89-90%。
- URL:https://www.rtoinsider.com/129421-ercot-large-load-requests-soar-again/ · https://www.utilitydive.com/news/texas-facing-438-gw-queue-approves-initial-large-load-interconnection-pro/823367/ · https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf

## G7 GE Vernova Q1 2026 —— 判决:HOLDS(一处标注)

- 燃机设备 backlog+slot reservation 83→**100 GW**,年底目标 ≥**110 GW** ✓;Q1 签 21 GW(19 GW slot reservation + 2 GW 直接订单)✓;Strazik 逐字:"about 10 GW of turbine production capacity remaining through 2030",并"continue to expect to take on orders for 2031 and beyond" ✓;新单价格逐字:"10% to 20% growth in price on new bidding and winning activity … relative to … the backlog in the fourth quarter of last year" ✓;电气化订单 +86%(organic)、backlog $25B→$42.4B ✓。
- 标注:"三大 OEM lead time 最长 8 年"是行业/媒体综合口径(7-8 年;Mitsubishi 售罄至 2028、Siemens 纪录 backlog),非任一 OEM 一手表述——按行业多源引用,不当作 GE Vernova 电话会内容。
- URL:https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-hits-100-gw-as-prices-rise/818332/ · https://www.gevernova.com/news/press-releases/ge-vernova-reports-first-quarter-2026-financial · https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm · https://sustainablepowernews.com/gas-turbine-backlog-crisis-orders-double-as-buyers-face-5-year-wait-times/

## G8 核电时间表 —— 判决:HOLDS(一处时效标注)

- Crane(前三里岛一号):835 MWe ✓;微软 20 年 PPA(2024-09 宣布)✓;DOE LPO **$10 亿贷款 2025-11-18 完成交割**(本届政府首个"条件承诺+交割同步"项目)✓;重启从 2028 提前至 2027(提前约一年)✓。时效风险:2026 年上半年 Constellation 为保住 2027 时间表向 FERC 申诉互联问题,裁决预计 2026 年 6-7 月——成文时应复查最新状态。
- Google-Kairos:首堆 2030、至 2035 共 500 MW(最多 7 台)✓。Amazon-X-energy/Energy Northwest:初期 4 堆 320 MWe(可扩至 960 MWe)、2039 年前 5 GW ✓("2030 年代早期"为项目方口径)。截至检索,美国无商业 SMR 并网 ✓(未见任何并网报道)。
- URL:https://www.ans.org/news/article-7570/crane-restart-boosted-by-1b-lpo-loan/ · https://www.ans.org/news/article-8026/ferc-decision-on-crane-restart-coming-in-june-or-july-constellation-execs-say/ · https://www.kairospower.com/updates/google-and-kairos-power-partner-to-deploy-500-mw-of-clean-electricity-generation/ · https://www.powermag.com/amazon-backs-massive-nuclear-smr-deployment-5-gw-with-x-energy-agreements-with-energy-northwest-dominion/

## G9 IEA / LBNL / 历史前科 —— 判决:HOLDS

- IEA《Energy and AI》官网页面逐字核对:Base Case 2030 全球数据中心 **945 TWh**、占全球用电 **"just under 3%"**、2024-30 年均 ~15%;美 **+240 TWh(+130%)**/中 **+175 TWh(+170%)**/欧 **+45 TWh(+70%)**;2035 情景:Lift-Off **~1,700 TWh(~4.4%)**/ High Efficiency **~970 TWh(~2.6%)**/ Headwinds **~700 TWh(<2%)**。全部 ✓(注:欧洲原文是 "more than 45 TWh")。
- LBNL 2024(DOE 委托):2023 年 176 TWh / 4.4%,2028 年 325-580 TWh / 6.7-12% —— 与公开报告口径一致(多源引用无矛盾;本轮未逐页回 PDF)。
- 历史前科(Mills 1999 被 Koomey 拆穿、2007 EPA 高估、2010-2018 平台期 = Masanet et al. Science 2020)为文献共识,多源无矛盾。
- URL:https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai · https://www.iea.org/reports/energy-and-ai/executive-summary · https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf

## G10 Google 测量 —— 判决:HOLDS

- 2025-08 Google Cloud 博客 + arXiv:2508.15734:Gemini Apps **中位文本 prompt 0.24 Wh**(0.26 ml 水、0.03 gCO2e);12 个月内中位 prompt 能耗降 **33×**、碳 **44×** ✓。口径限定(中位、纯文本、含 idle/host/PUE 开销、不含图像视频训练)与论断一致。
- 总量对照:2025 环境报告:2024 年排放 ~11.5 MtCO2e,较 2019 基线 **+51%**("+~50%" ✓);数据中心用电"过去四年翻倍"(2020→2024)、2024 年同比 +27% ✓。
- URL:https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference · https://arxiv.org/abs/2508.15734 · https://blog.google/company-news/outreach-and-initiatives/sustainability/environmental-report-2025/ · https://www.rcrwireless.com/20250704/ai-infrastructure/data-center-energy

## G11 Nadella BG2 逐字引语 —— 判决:HOLDS

- 多家独立媒体逐字一致:"The biggest issue we are now having is not a compute glut, but it's power … you may actually have a bunch of chips sitting in inventory that I can't plug in … It's not a supply issue of chips; it's actually the fact that I don't have warm shells to plug into." ✓
- 时间窗:BG2 播客(与 Sam Altman 同场)2025-10-31 前后发布,媒体集中报道 2025-11-01~03;"2025-11" 可用,建议写"2025 年 10 月底/11 月初"。旁证:微软 CFO Amy Hood 同期财报电话会称约束在"space or power"而非芯片。
- URL:https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-ceo-says-the-company-doesnt-have-enough-electricity-to-install-all-the-ai-gpus-in-its-inventory-you-may-actually-have-a-bunch-of-chips-sitting-in-inventory-that-i-cant-plug-in · https://www.datacenterdynamics.com/en/news/microsoft-has-ai-gpus-sitting-in-inventory-because-it-lacks-the-power-necessary-to-install-them/ · https://techcrunch.com/2025/11/03/altman-and-nadella-need-more-power-for-ai-but-theyre-not-sure-how-much/

## G12 NERC / Grid Strategies / 账单 —— 判决:修正(归属错置 + 两个账单数未回溯)

- **修正(归属)**:"5 年峰值 +166 GW(~90 GW 数据中心)"**不是 NERC 的数字**,是 **Grid Strategies《National Load Growth Report 2025》对公用事业 FERC Form 714 申报的加总**(166 GW 五年峰值增长,其中 ~90 GW 数据中心、~30 GW 制造业;2022 年同口径仅 24 GW)。NERC 2025 LTRA(2025-12 发布)的口径是:**十年夏季峰值 +224 GW、较 2025 年峰值 +24%**(Grid Strategies 的 LTRA Review 转述 NERC "到 2030 年 +160 GW")。→ 修正前:"NERC:5 年 +166 GW" → 修正后:"公用事业申报加总(Grid Strategies 汇编):5 年 +166 GW(~90 GW 数据中心);NERC LTRA:十年峰值 +24%(+224 GW)"。
- **HOLDS(反驳侧)**:Grid Strategies 同一报告即为批评方:公用事业数据中心负荷预测**可能高估达 40%**(高载荷因子、跨州重复申请);独立追踪(Cleanview 等)**2029-2030 实际投运 ~60-65 GW** vs 申报 ~90 GW ✓。
- **账单(部分核实)**:Pepco(DC)自 2025-06 平均 **+$21/月**,其中 **~$10 归因容量价**(≈"约半数")✓(51st/当地报道)。**西马里兰 +$18、俄亥俄 ~$16 未能回溯到一手**:可查到的是马里兰 OPC 报告"APS 区(西马里兰)账单 +24%"、AEP Ohio 2025-06 总涨幅 ~$27/月——两个具体数字维持【单源·倡导组织】降级,或补 CUB/OPC 原件后再承重。
- URL:https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf · https://www.instituteforenergyresearch.org/the-grid/u-s-peak-load-growth-to-soar-principally-due-to-data-centers/ · https://www.utilitydive.com/news/nerc-10-year-peak-demand-forecast-jumps-24-on-new-data-center-loads/810955/ · https://www.utilitydive.com/news/nerc-overstates-reliability-risks-ltra-grid-strategies/814292/ · https://gridstrategiesllc.com/wp-content/uploads/FINAL-2025-LTRA-Review.pdf · https://51st.news/dc-electricity-bill-high-pepco/ · https://www.utilitydive.com/news/maryland-bge-pepco-electricity-bill-pjm-capacity-auction-opc-ratepayer/724319/
