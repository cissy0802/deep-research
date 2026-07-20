# 对抗验证 · Voter A(refute-by-default)

验证日期:2026-07-20。方法:每组回到一手来源(官方新闻稿/监管文件/财报电话会/原始报告)逐字核对分子、分母、时间窗、限定语。判决:HOLDS / 修正 / 推翻。

---

## G1 三家内存厂 2026 产能售罄 — 判决:修正

**核到的事实:**
- SK Hynix 3Q25 业绩发布(2025-10-29,官方新闻稿):"has secured customer demand across all DRAM and NAND products, including HBM, through next year"——即 DRAM/NAND/HBM 全线 2026 需求锁定,媒体口径"sold out"成立。✅
- Micron:2026 自然年 HBM 产出已全部签约(多年期合约),多家报道一致。✅
- Samsung:公司层面确认的是 **HBM(HBM4)产能售罄**、供给远低于需求、客户提前拉动 2027 需求(1Q26 财报会,EVP Jaejune Kim);"整个 2026 产出售罄/到 2027 售罄"来自**分析师**(KB 证券等)推断,非三星官方表述。⚠️

**修正:** "三家 2026 年产能整体售罄(公司口径)" → "SK Hynix 官方确认 DRAM/NAND/HBM 全线 2026 需求锁定;Micron 官方确认 2026 HBM 全部签约;Samsung 官方仅确认 HBM 售罄与供给严重短缺,'全线售罄'系分析师口径"。

**一手/最近源:**
- https://news.skhynix.com/sk-hynix-announces-3q25-financial-results/
- https://finance.yahoo.com/news/micron-sold-2026-hbm-us-231248051.html(转述财报会)
- https://www.alpha-sense.com/earnings/005930.kr(Samsung 1Q26 财报会摘要)

---

## G2 TrendForce 价格链与 PC BOM — 判决:修正(主体成立,两处口径问题)

**逐项核对:**
- TrendForce 2026-03-31 新闻稿:常规 DRAM 合约价 2Q26 **+58–63% QoQ**、NAND **+70–75% QoQ**。✅ 逐字吻合。
- 3Q26 预测(2026-07-03 新闻稿):常规 DRAM **+13–18% QoQ**(NAND +10–15%)。✅
- HP CFO Karen Parkhill(FY26 Q1 财报会,2026-02-25):内存+存储占 PC BOM "roughly 15%–18%" → "roughly 35% for the year"。✅
- **"+89–90% 是现货/特定型号口径" ❌**:实际上流传的 ~90% 是 TrendForce 自己 2026-02-02 新闻稿对 **1Q26 常规 DRAM 合约价**的上修(55–60% → **90–95% QoQ**,NAND 33–38%→55–60%)。这是**合约价口径、且是 1Q26 而非 2Q26**,并非现货/特定型号误读。
- **16GB DDR4 零售 $137→$207(+51%)未能复现**:检索 Tom's Hardware RAM 价格指数、TechPowerUp、Pangoly 等均未找到该组数字。可核实的替代数据点:32GB(2×16GB)DDR4 套条 2025-10 约 $60–90 → 2026-01 约 $150–180(Tom's Hardware);Corsair 32GB DDR4-3200 低点 $71.99 → $262.99(TechPowerUp)。

**修正:** ① "媒体流传的 +89–90% 是现货/特定型号口径" → "流传的 ~90% 实为 TrendForce 2026-02-02 对 1Q26 合约价的上修(90–95% QoQ),与 2Q26 的 58–63% 属不同季度,同为合约价口径";② $137→$207 无一手出处,建议删除或换用上述可核实数据点。

**一手 URL:**
- https://www.trendforce.com/presscenter/news/20260331-12995.html
- https://www.trendforce.com/presscenter/news/20260703-13134.html
- https://www.trendforce.com/presscenter/news/20260202-12911.html
- https://www.theregister.com/on-prem/2026/02/25/hp-says-memorys-contribution-to-pc-costs-has-doubled/4138346(HP 财报会转述,含逐字引语)
- https://www.techpowerup.com/345717/ddr4-prices-skyrocketing-amid-dram-shortage-crunch

---

## G3 CoWoS 绑定约束 — 判决:HOLDS(附来源混用警示)

**核到的事实:**
- TSMC CEO 魏哲家称 CoWoS "extremely tight and sold out through 2026"。✅
- TrendForce(2026-06-15 转述):TSMC 以约 **80%/年**扩产 CoWoS,供需缺口 2026 年内仅从 ~20% 收窄到 ~10%,仍不够。✅
- NVIDIA 份额:digitimes(2025-12-10)报 NVIDIA 锁定 2026–27 **过半**产能、年订约 **80–85 万片**;另一口径(TrendForce/Astute)为 ~59.5 万片 = 全球需求(~100 万片)的 **60%**。"60%+ 份额"与"80–85 万片"分属两套估算(分母分别为总需求 vs TSMC 产能),同引时应注明均为供应链报道、非官方数字。

**一手/最近源:**
- https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/
- https://www.digitimes.com/news/a20251210PD218/tsmc-cowos-capacity-nvidia-equipment.html
- https://www.astutegroup.com/news/industrial/advanced-packaging-demand-soars-nvidia-secures-60-of-cowos-capacity/

---

## G4 PJM 容量拍卖价格链 — 判决:HOLDS

**逐项核对(全部为 PJM 官方口径):**
- 2028/29 BRA(2026-07-14 公布):RTO 出清 **$325.00/MW-day**,触 FERC 批准的上限;采购 **138,318 MW**(138,317.8 UCAP);距可靠性要求缺 **6,831 MW**(6,831.3);PJM 官方称上次(2027/28)缺口"approximately 6,500 MW";**连续第三次触上限**("third consecutive auction operating at the price cap")。✅
- 2027/28 BRA(2025-12-17 公布):全域出清 **$333.44/MW-day**,为 FERC 批准上限;采购 134,479 MW。✅
- 2026/27 BRA:$329.17(触当时价格上限);2025/26 BRA:$269.92;2024/25 BRA:$28.92(公认历史数,PJM 2024-07 新闻稿)。✅

**一手 URL:**
- https://insidelines.pjm.com/pjm-capacity-auction-procures-138318-mw-of-generation-resources-as-work-continues-to-address-growing-electricity-demand/
- https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf
- https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2027-2028/2027-2028-bra-report.pdf
- https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2025-releases/20251217-pjm-auction-procures-134479-mw-of-generation-resources.pdf

---

## G5 Monitoring Analytics 数据中心占容量成本 — 判决:HOLDS

**核到的事实(IMM 2026-01-05 报告,针对 2027/28 BRA):**
- 数据中心负荷占容量成本 **$6.5B / $16.4B = 40%**;其中约 **$6.2B** 来自尚未建成的数据中心。✅
- 近三次拍卖:超出存量负荷的数据中心预测贡献 **$21.3B,占 $47.2B 出清容量成本的 45%**。✅
- IMM 原话:"The extreme uncertainty in the load forecasts based on uncertainty about the addition of large data center loads is also unique and unprecedented."

**一手/最近源:**
- https://www.utilitydive.com/news/data-centers-pjm-capacity-auction/808951/(2026-01-07,直接引用 IMM 报告)
- https://www.monitoringanalytics.com/reports/Reports/(IMM 报告库;2027/28 BRA 分析)

---

## G6 ERCOT 大负荷队列 — 判决:HOLDS

**逐项核对:**
- 2026-04-01:队列超 **410 GW**(RTO Insider 报道 Oncor 批量申请推高;约 87% 为数据中心)。✅
- 2026 年中(PUCT 批准新规时):**438 GW**(438,000+ MW),**近 90%** 为数据中心(Utility Dive,2026-06)。✅
- **1Q26 单季新申请 198 GW**(Ascend Analytics 汇总 ERCOT 数据;另 86 GW 在审 ≈ 当前系统峰值)。✅
- 对照:ERCOT 历史峰值 ~85.5 GW(2023-08 纪录,"roughly equal to the current size of ERCOT's peak load" 佐证 ~85–86 GW 量级)。✅
- 时间线自洽:2025-12 约 233 GW(>70% 数据中心)→ 2026-04 410 GW → 年中 438 GW。

**一手/最近源:**
- https://www.rtoinsider.com/129421-ercot-large-load-requests-soar-again/
- https://www.utilitydive.com/news/texas-facing-438-gw-queue-approves-initial-large-load-interconnection-pro/823367/
- https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf(ERCOT 官方参议院听证材料)
- https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access

---

## G7 GE Vernova Q1 2026 — 判决:HOLDS(一处子项未能独立核实)

**逐项核对(Q1 2026 财报,2026-04-22):**
- 燃机签约 backlog **100 GW**(2025 年底为 **83 GW**,+17 GW)。✅
- 年底目标:backlog+slot reservation 合计 **至少 110 GW**。✅
- Strazik:2030 年前剩余产能 **约 10 GW**,"continue to expect to take on orders for 2031 and beyond"。✅ 与论断表述一致。
- 新订单报价较 Q4 2025 backlog 费率 **+10–20%**("10% to 20% growth in price on new bidding and winning")。✅
- 电气化业务:订单有机增长 **+86%**,backlog **$25B → $42.4B**;单季数据中心电气化订单 $2.4B 超 2025 全年。✅
- ⚠️ "三大 OEM lead time 最长 8 年":未在本次核查的一手材料中找到"8 年"表述(GE Vernova 自身口径为排产至 2030 年基本满、开始接 2031+ 订单,即 ~5–6 年;"8 年"若指全行业个别机型排至 2033–34,需补出处)。建议补注来源或降格为"排期已至 2030 年代初"。

**一手/最近源:**
- https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm(8-K 新闻稿)
- https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-hits-100-gw-as-prices-rise/818332/(含财报会逐字引语)

---

## G8 核电时间表 — 判决:HOLDS

**逐项核对:**
- Crane Clean Energy Center(原三里岛 1 号):**835 MW**;Microsoft **20 年 PPA**(2024-09 签署);DOE **$10 亿贷款**(2025-11 关闭);重启目标由 2028 提前至 **2027**。✅ 全部与 Constellation/DOE 官方一致。
- Google–Kairos(2024-10 主开发协议):首堆 **2030** 年并网,**500 MW** 到 **2035**。✅(Kairos 官方稿)
- Amazon–X-energy(2024-10):与 Energy Northwest 初期 **4 台 ~320 MWe**(可扩至 960 MWe),目标 2030 年代早期;整体目标 **5 GW 到 2039**("largest commercial deployment target of SMRs to date")。✅
- 美国目前无商业 SMR 并网:✅ 截至 2026 年,西方尚无商业运行 SMR;NRC 2026 年才预期发出首批商业 SMR 建设许可决定;北美唯一在建 SMR 在加拿大(Darlington BWRX-300)。

**一手/最近源:**
- https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html
- https://www.energy.gov/edf/crane-restart(DOE $1B 贷款)
- https://www.kairospower.com/updates/google-and-kairos-power-partner-to-deploy-500-mw-of-clean-electricity-generation
- https://www.powermag.com/amazon-backs-massive-nuclear-smr-deployment-5-gw-with-x-energy-agreements-with-energy-northwest-dominion/
- https://smrintel.com/state-of-smr-2026/

---

## G9 IEA / LBNL / 历史前科 — 判决:HOLDS

**逐项核对(IEA《Energy and AI》官方页面,逐字):**
- Base Case 2030:全球数据中心 **~945 TWh**,"just under 3%" 全球用电占比。✅
- 区域(至 2030):美国 "increases by around **240 TWh (up 130%)**";中国 "around **175 TWh (up 170%)**";欧洲 "grows by more than **45 TWh (up 70%)**"。✅ 逐字吻合。
- 2035 情景:Lift-Off "exceeding the **1 700 TWh** mark"(4.4%);High Efficiency "around **970 TWh**";Headwinds "at around **700 TWh**"(<2%)。✅
- LBNL 2024《美国数据中心能耗报告》:2023 年 **176 TWh(4.4%)**;2028 预测 **325–580 TWh(6.7–12%)**。✅ 与报告一致(本组为公开报告标准数字)。
- 历史前科:1999 年 Forbes/Mills"互联网将吃掉半数电力"被 Koomey 等系统性证伪(实际 2020 年前后数据中心占比 ~1–2%);2007 EPA 预测远超实际;2010–2018 全球数据中心用电基本持平(Masanet/Koomey, Science 2020)。✅ 学术共识,无需修正。

**一手 URL:**
- https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
- https://iea.blob.core.windows.net/assets/86ed1178-4d77-45ac-ab38-28e849f3b93f/EnergyandAI.pdf
- LBNL:https://eta.lbl.gov/publications/united-states-data-center-energy(2024 US Data Center Energy Usage Report)

---

## G10 Google Gemini 能耗测量 — 判决:HOLDS

**逐项核对:**
- Google 技术论文(arXiv:2508.15734,2025-08-21)+ Google Cloud 官方博客:中位 Gemini Apps 文本 prompt **0.24 Wh**(0.03 gCO2e、0.26 mL 水);过去 12 个月单位能耗降 **33×**、单位碳足迹降 **44×**。✅ 逐字吻合。
- Google 2025 环境报告:2024 年排放较 2019 基线 **+51%**(论断"+~50%"成立);电力消耗"doubled over the past four years"(即自 2020 翻倍,数据中心用电 2024 年同比 +27%)。✅
- 论断中"单位效率大增 vs 总量翻倍"的对照关系与一手材料一致。

**一手 URL:**
- https://arxiv.org/abs/2508.15734
- https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
- https://www.smartenergydecisions.com/wp-content/uploads/2025/07/google-2025-environmental-report-1.pdf

---

## G11 Nadella BG2 引语 — 判决:HOLDS

**核到的逐字记录(BG2 Pod,与 Sam Altman 同场,2025-10/11 播出,媒体 2025-11 初广泛转录):**
> "The biggest issue we are now having is not a compute glut, but it's power – it's sort of the ability to get the builds done fast enough close to power. So, if you can't do that, you may actually have a bunch of chips sitting in inventory that I can't plug in. In fact, that is my problem today. It's not a supply issue of chips; it's actually the fact that I don't have warm shells to plug into."

论断引语为忠实节选(省略号处为"get the builds done fast enough close to power"一句),无断章取义。✅

**一手/最近源:**
- https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-ceo-says-the-company-doesnt-have-enough-electricity-to-install-all-the-ai-gpus-in-its-inventory-you-may-actually-have-a-bunch-of-chips-sitting-in-inventory-that-i-cant-plug-in
- https://techcrunch.com/2025/11/03/altman-and-nadella-need-more-power-for-ai-but-theyre-not-sure-how-much/
- 原始视频:BG2 Pod(YouTube),Nadella & Altman 专场

---

## G12 NERC / Grid Strategies / 账单 — 判决:修正(两处归属错误)

**逐项核对:**
- **❌ 归属错误一:"NERC:5 年峰值 +166 GW(~90 GW 数据中心)"**——166 GW/90 GW 出自 **Grid Strategies《National Load Growth Report 2025》**(汇总公用事业 FERC 申报:5 年峰值预测由 2022 年的 24 GW 升至 2025 年的 166 GW,其中数据中心 ~90 GW、制造业 ~30 GW),**不是 NERC 数字**。
- NERC 2025 LTRA(2026-01 发布):**10 年**夏季峰值 **+24%**(**+224 GW**;冬季 +246 GW),数据中心为主要驱动。✅(论断"十年峰值 +24%"正确,但应与 166 GW 分开归属)
- Grid Strategies 反驳口径:公用事业申报的数据中心负荷可能高估 **达 40%**;独立追踪显示 2029–30 实际落地约 **60–65 GW**(vs 申报的 ~90 GW)。✅
- **❌ 归属/数字问题二(账单):**
  - 西马里兰 **+$18/月**:✅ 但口径是 **Maryland OPC(People's Counsel)** 对 Potomac Edison 的测算(2024 容量拍卖影响),非 CUB。
  - "Pepco(DC)+$21/月":未能复现。OPC 同一报告口径:**BGE +$21/月,Pepco(MD)/SMECO +$14/月**。$21 对应的是 BGE 而非 Pepco。
  - "俄亥俄 ~$16":未能复现。可核实口径:AEP Ohio 2025-06 起平均月账单约 **+$27**(Price to Compare +36%,主要归因容量价暴涨与数据中心需求)。
- "约半数归因容量价"的定量拆分亦未找到一手支撑。

**修正:** ① 166 GW/90 GW 归属 Grid Strategies 2025 报告(公用事业申报汇总),NERC 仅保留"十年 +24%(224 GW)";② 账单改为:Maryland OPC 口径 BGE +$21、Potomac Edison(西马里兰)+$18、Pepco/SMECO +$14;俄亥俄用 AEP Ohio ~+$27/月(2025-06)或删除。

**一手 URL:**
- https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf
- https://www.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf
- https://www.utilitydive.com/news/nerc-10-year-peak-demand-forecast-jumps-24-on-new-data-center-loads/810955/
- https://gridstrategiesllc.com/forecasting-for-large-loads/
- https://opc.maryland.gov/Portals/0/Files/Publications/RMR%20Bill%20and%20Rates%20Impact%20Report_2024-08-14%20Final.pdf(Maryland OPC 账单影响报告)
- https://electricityplans.com/ohio-capacity-cost-increase-2025/

---

## 总表

| 组 | 判决 | 要点 |
|---|---|---|
| G1 | 修正 | Samsung"整体售罄"系分析师口径,非官方 |
| G2 | 修正 | ~90% 实为 TrendForce 1Q26 合约价上修(90–95%);$137→$207 无出处 |
| G3 | HOLDS | 附警示:60% 份额与 80–85 万片分属两套供应链估算 |
| G4 | HOLDS | 价格链、138,318 MW、6,831 vs ~6,500 MW、三连触顶全部吻合 |
| G5 | HOLDS | $6.5B/$16.4B=40%、$6.2B 未建成、$21.3B/$47.2B=45% 全吻合 |
| G6 | HOLDS | 410→438 GW、87%→~90%、Q1 198 GW、峰值 ~85 GW 吻合 |
| G7 | HOLDS | 100→110 GW、10 GW 剩余、+10–20%、+86%、$42.4B 吻合;"8 年 lead time"未独立核实 |
| G8 | HOLDS | Crane/Kairos/X-energy/无商业 SMR 并网全部吻合 |
| G9 | HOLDS | IEA/LBNL 数字逐字吻合;历史前科为学术共识 |
| G10 | HOLDS | 0.24 Wh、33×/44×、+51%、四年翻倍全部吻合 |
| G11 | HOLDS | 引语逐字吻合,省略号无断章 |
| G12 | 修正 | 166 GW/90 GW 应归属 Grid Strategies 而非 NERC;账单 $21 属 BGE、俄亥俄 $16 未证实 |
