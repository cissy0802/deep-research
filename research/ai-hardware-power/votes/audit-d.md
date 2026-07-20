# Round 3 审计 D:反证搜索席 + 方法学审计席(有否决权)

审计对象:#15 期 6 组单源承重实证。日期:2026-07-20。
方法:每组先做主动反证搜索(记录全部角度,含无果),再做敌意方法学审计,最后判决。

---

## S1 账单归因(Pepco DC +$21/月、西马里兰 +$18、俄亥俄 ~$16;约半数归因 PJM 容量价)

### 反证搜索角度
1. Pepco DC + "$21" + PJM capacity + CUB → 命中 DC 官方消费者代表 OPC-DC 文件
2. Maryland OPC + Potomac Edison + capacity charge → 命中马里兰州 OPC 官方 factsheet
3. Ohio + "$16" + capacity auction + AEP → 命中 IEEFA 报告与 AEP Ohio 自己的公告
4. 尝试找 CUB 作为俄亥俄 $16 的原始出处 → 无果:$16 的原始出处是 IEEFA,不是 CUB(仓库归因需修正)
5. 未做:直接调取 Pepco/Exelon 2025 年费率公告原文(但 AEP Ohio 官方博客已覆盖公用事业侧口径)

### 找到的独立证据
- **DC(独立于 CUB,政府法定机构)**:DC Office of People's Counsel 2025-05-22 新闻稿:2025-06 起平均月账单约 +$20;OPC 估算其中 **$10/月(约一半)归因容量价格暴涨**。配套有 OPC 委托 Synapse Energy Economics 的报告《Drivers of PJM's Capacity Market Price Surge》(opc-dc.gov)。媒体独立复述:Washington Informer 给出 **$20.81** 的精确数;51st.news 亦独立报道。→ 与"$21/月、约半数归因容量价"高度吻合,且是**独立团队(OPC-DC/Synapse)+独立计算**。
- **马里兰(州政府法定机构)**:Maryland OPC 2025-06-12 官方 factsheet:2025/26 容量市场账单影响 **Potomac Edison(西马里兰)$18.00/月**、Pepco-MD $14.00/月;Utility Dive 独立报道"马里兰用户最高面临 24% 账单上涨"。注意:马里兰的传导时点不是 6 月——Pepco-MD 从 8 月账单、Potomac Edison 从 10 月账单开始,分摊到 2025 秋与 2026 春。
- **俄亥俄**:$16/月出自 **IEEFA** 报告("capacity prices estimated to increase the average residential bill by about $16/month in Ohio")。公用事业自己的口径:AEP Ohio 官方博客称 1,000 kWh 月用量客户 2025-06 起该项费用约 **+$27/月**;第三方(electricityplans 等)给出容量成本 ≈ +2¢/kWh、账单 +10-15%。即俄亥俄各家口径在 $16-27 之间,差异来自用电量假设与是否含其他费率变动;IEEFA 的 $16 处于**保守端**,方向无争议。

### 方法学审计
- 样本/口径:三个数字用电量假设不统一(DC 的"平均用户"与俄亥俄 1,000 kWh 不同),跨州横向比较时应注明。
- 归因方法:OPC-DC 的"约半数归因容量价"有 Synapse 委托报告支撑,是费率结构分解而非回归归因——这是合理口径,但应表述为"费率分解"而非因果推断。
- 利益冲突:CUB/OPC 是消费者倡导方,有夸大动机;但本案中**公用事业自己的数字(AEP Ohio $27)比倡导组织的更高**,反向 COI 检验通过。
- 归因错误:仓库把三个数字统一归到"CUB 等消费者组织"——实际 DC 是 OPC-DC(法定政府机构)+Synapse,马里兰是州 OPC,俄亥俄是 IEEFA。CUB 只是伊利诺伊/转述侧。

### 判决:**升级多源证实(DC、马里兰);俄亥俄单源已核可承重(限制)**
- DC $21(OPC-DC 口径 ~$20/$20.81)与"约半数归因容量价"($10/月,OPC-DC/Synapse):多源证实,可承重。
- 西马里兰 $18(= Potomac Edison,马里兰州 OPC 官方 factsheet):多源证实,可承重,但须修正传导时点(10 月起,非 6 月)。
- 俄亥俄 ~$16:承重时注明"IEEFA 估算;AEP Ohio 官方口径在 1,000 kWh 假设下约 $27,各口径 $16-27"。
- 行文修正:来源归因应改为"各州法定消费者代表(OPC)与 IEEFA/CUB 等",不是单一 CUB。

---

## S2 "互联申请量是实际建成量的 5-10 倍"

### 反证搜索角度
1. 精确短语 "5 to 10 times" + data center interconnection → 溯源成功
2. Utility Dive 原文定位 → 找到原始报道与具名专家
3. LBNL / Grid Strategies 是否有系统性测量(load 侧)→ **无果**:LBNL Queued Up 只测发电侧队列
4. Koomey / EPRI / Brattle "conversion rate" 系统测量 → 找到 EPRI 2024-09 调查(方向性支撑,非直接测量)
5. 学术侧:arXiv "Best Practices for Large Load Interconnections"(2026)→ 定性支撑(负荷互联无正式队列、投机申请门槛极低),无倍数测量

### 找到的独立证据
- **原始出处(具名)**:Utility Dive《A fraction of proposed data centers will get built. Utilities are wising up.》,发言人 **Astrid Atkinson**,Camus Energy 联合创始人/CEO(前 Google 软件工程高级总监)。原话:"Conservatively, you're seeing five to 10 times more interconnection requests than data centers actually being built."
- **不存在系统性测量**。LBNL Queued Up(2025 版)是发电侧:队列 2,290 GW ≈ 现役机组 2 倍、历史建成率低(仅 ~13-20% 达 COD)——只能类比,不能直接支撑负荷侧倍数。
- **方向性独立支撑**:①EPRI 2024-09 调查:数据中心申请占现有峰荷 ≥50% 的公用事业,预期五年内实际落地不超过峰荷的 ~35%;②ERCOT 长期负荷预测方法(2025-04 官方文件):对新数据中心申请统一打 **49.8% 折扣**+180 天延迟;③ERCOT 队列自身结构:410 GW 申请 vs 5.8 GW 已通电(见 S3)——若 2030 实际落地在 40-80 GW 量级,倒推比值恰在 5-10 倍区间。

### 方法学审计
- 这是**单一从业者的口头量级估计**,无样本、无口径定义("申请"按项目数还是 MW?"建成"以何时点截止?)、无可复算程序。"Conservatively"表明连发言者本人都视其为下界猜测。
- COI:Camus 卖电网优化软件,渲染"队列失灵"与其产品叙事同向,轻度利益相关。
- 但多条独立硬数据(EPRI 调查、ERCOT 49.8% 折扣、ERCOT 队列阶段构成)与该量级**方向一致**,说明它不是凭空捏造,而是行业内经验共识的口语化。

### 判决:**限制使用**
- 不得写成"专家估计申请量为建成量的 5-10 倍"这种测量化表述。
- 允许的用法:作为量级示意,且必须具名+定性:"Camus Energy CEO Astrid Atkinson(前 Google)的经验估计——目前没有任何系统性测量;方向与 EPRI 调查(落地 ≤35%)和 ERCOT 官方预测折扣(新数据中心申请打 49.8% 折)一致"。
- 若文章承重点是"幽灵需求存在且巨大",应改用 S3 的 ERCOT 阶段构成数据承重,本条降为佐证。

---

## S3 ERCOT 大负荷队列 438 GW(~90% 数据中心)与 2026-04 的 410 GW/87%

### 反证搜索角度
1. ERCOT 438 GW 官方文件 → 命中 ERCOT Trending Topic(2026-06-18)与 Utility Dive PUCT 报道
2. 410 GW/87% 官方原文 → **已获取并通读 ERCOT 2026-04-01 参议院听证会正式简报 PDF 全文**(ercot.com/files/docs/2026/04/01/)
3. 队列定义/阶段构成 → PDF 第 3 页有完整分阶段表格(下详)
4. RTO Insider 410 GW 报道 → 付费墙,未获全文(无碍,已有官方原文)
5. ERCOT March TAC Report PDF → 解析失败(无碍)
6. ERCOT 预测口径 vs 队列口径 → 命中 2025-04 长期负荷预测方法文件 + PUCT Project 58480/58481 规则

### 找到的官方原文(2026-04-01 参议院听证会,Pablo Vegas 署名)
- 原文:"ERCOT is tracking approximately **410 GW** of Large Loads seeking interconnection of which **~87%** are data centers."(截至 2026-03-26:总计 **410,618 MW**,数据中心 87.6% = 355,830 MW)
- **关键表格(按 2030 年口径的阶段构成)**:
  - No Studies Submitted(连研究都未提交):**293,651 MW = 71.5%**
  - Under ERCOT Review:86,605 MW
  - Planning Studies Approved:21,343 MW
  - Approved-to-Energize 但未运行:3,241 MW
  - **Observed Energized(实际已通电):仅 5,778 MW = 1.4%**
- 438 GW:2026 年中口径,出自 ERCOT 官方 Trending Topic 文件(2026-06-18)及 PUCT Batch Zero 决定的报道,"近 90% 数据中心"。与 410→438 的时间线一致(Q1 2026 单季涌入潮延续)。
- **仓库数字勘误**:C4 写"2026 Q1 单季新增申请 198 GW"。官方 PDF 第 4 页该图中 **"198"是申请件数(项目数)**,不是 GW(图注同系列数字 53/7/11/…/76/48 均为件数;多家转述也作 "198 new applications")。该季度对应柱高(Requested Load Amount)约 175-190 GW——量级碰巧接近,但口径是错的,不得写"198 GW"。
- 队列定义:含所有 ≥ 大负荷门槛、经 TSP 提交给 ERCOT 追踪的互联请求,**不要求签约、不要求交费、不要求场地控制**(这正是 PUCT 2026-03 起用 Project 58480/58481 补的洞:此后只有签署互联协议+每 MW $50,000 财务担保的负荷才计入官方大负荷预测)。跨 TSP 重复申请未去重(Oncor 一家 259 GW);得州 SB6 要求披露重复申请,侧面证明官方承认队列含重复。

### 方法学审计
- 两个数字都真实存在于 ERCOT 官方文件,行政记录性质,数字本身无可挑剔。
- 但"队列"是**申请登记簿而非需求预测**:71.5% 连研究都没提交、仅 1.4% 已通电;ERCOT 自己的规划预测对其打约五折(49.8%)并从 2027 起只认签约负荷。任何把 438 GW 当作"未来需求"的用法都是口径滥用;仓库 C4 恰恰把它用作"幽灵需求(申请≠建设)的最硬证据"——这个用法与官方口径完全自洽,且阶段构成表让论证更硬。

### 判决:**单源已核可承重(官方行政数据;附两项强制限制)**
1. 引用时必须带阶段构成(71.5% 未提交研究、已通电仅 5.8 GW),防止读者把队列读成需求;
2. **勘误否决一个子数字**:"Q1 2026 新增 198 GW"不得使用——应写"Q1 2026 单季新增 198 件申请(对应约 175-190 GW 请求量)"或只写件数。

---

## S4 "HBM 占 DRAM 晶圆产能 ~23%"(tech-insider 转述)

### 反证搜索角度
1. TrendForce + HBM wafer share → 命中 TrendForce 官方新闻稿(2026-06-02)
2. Omdia / Counterpoint 独立估算 → 命中 Counterpoint(经 DRAMWatch 汇编);Omdia 直接数字**无果**
3. tech-insider 原文定位 → 确认其为低质聚合站,数字疑似转抄 Counterpoint

### 找到的独立证据
- **TrendForce(官方新闻稿,2026-06-02)**:前三大厂商 HBM **晶圆投入(wafer input)**占 DRAM 总晶圆投入比例:2025 年底 ~18%、**2026 年底 ~22%**、2027 年底 ~30%;对应 **bit 供给占比仅 8%/9%/13%**(HBM 每 Gb 耗 ~3 倍晶圆,HBM4 恶化至 ~4 倍)。
- **Counterpoint Research(经 DRAMWatch 引用)**:HBM 2026 年消耗 DRAM 晶圆 **23%**(2025 年 19%)。
- 两家独立机构给出 22-23%(2026),互相印证;"~23%"落在区间内。

### 方法学审计
- tech-insider 本身不可作为来源(聚合站,无原始方法);但数字可溯源到两家独立第三方研究机构且相互一致。
- 口径陷阱有三,承重时必须写清:①是**晶圆投入占比**,不是 bit 占比(bit 只有 ~9%)——混用会把 HBM 的产能挤占效应夸大 2.5 倍或低估 2.5 倍;②TrendForce 口径限"前三大供应商"(≈全球 HBM 产能全部,但分母是三家的 DRAM 晶圆,不含 CXMT 等);③时点是"2026 年(底)",不是当前存量。

### 判决:**升级多源证实(附口径限制)**
- 允许承重,但引用源必须换成 TrendForce(22%,2026 年底,前三大厂)与 Counterpoint(23%,2026),弃用 tech-insider;必须注明"晶圆投入占比,对应 bit 占比仅 ~9%"。

---

## S5 SemiAnalysis 对"2026 美国数据中心一半被取消"的反驳

### 反证搜索角度
1. SemiAnalysis 原文 → 命中《Stop Saying Half of 2026 US Datacenter Capacity Is Canceled》(newsletter.semianalysis.com)
2. Bloomberg/Sightline 原始口径 → 命中多家转述(Bloomberg 原文付费墙未获全文):~12-16 GW 计划 vs 4-5 GW 在建,30-50% 延期或有取消风险;溯源至 Bloomberg 2026-04-01《America's AI Build-Out Hinges on Chinese Electrical Parts》
3. 独立追踪商横向对比(Baxtel/DC Byte/Synergy)→ Baxtel、DC Byte 直接数字无果;命中 ITK Research 的横向对比(下详)+ Synergy(在营口径)
4. "在建"口径的机构间离散度 → 关键发现

### 找到的独立证据
- **SemiAnalysis 自述**(原文确认):6 个月内其北美超大规模自建年底 2026 预测仅动 ~1%、托管(colocation)<5%;卫星视觉模型显示仅前两家超大规模自建在建即 >5 GW,未计第三方开发商的多个 GW 级在建项目。
- **Bloomberg/Sightline 口径**(转述一致):~12 GW(一说 12-16 GW)计划 2026 上线,仅 4-5 GW 在建,30-50% 延期或取消风险;归因变压器/开关柜短缺与电网瓶颈。注意各转述在 4 GW vs 5 GW、"取消" vs "延期或有风险"上不一致——二手放大链本身就是失真源。
- **关键独立发现(ITK Research 横向对比)**:"在建"口径机构间差 4 倍——Cushman & Wakefield / datacenterHawk 口径北美在建 ~25.3 GW(H2 2025,含自建与 behind-the-meter AI factory),而 **CBRE 同期口径仅 5,994 MW**(仅主要托管市场)。Sightline 的"5 GW 在建"接近 CBRE 窄口径;SemiAnalysis 的">5 GW 仅两家自建"与 C&W 宽口径相容。**两边的分歧大部分是口径分歧,不是事实分歧。**
- ITK 同时记录:相对原计划的缺口从 2026 年初 ~7.5 GW 扩大到年中 ~10.5 GW——真实延误存在且在扩大,支持 F1 的"两者可同真"裁决。

### 方法学审计
- SemiAnalysis 的 "~1%" 是**其自有专有模型的自我修订幅度**,外界不可复算,等于"我们没改口"的自我背书——证据等级低。">5 GW 在建"基于卫星影像,原则上可第三方复核,证据等级较高。
- COI 双向:SemiAnalysis 卖数据中心数据产品(反驳"取消潮"符合其商业叙事);Sightline Climate 同样卖气候/基建情报(渲染瓶颈同样符合其叙事)。COI 对冲,不构成单边否决理由。
- Bloomberg 侧的原始弱点:分母是"公告(announced)容量",其中大量本来就是无场地/无融资/无互联协议的早期公告——"取消一半"的分母偏差是 SemiAnalysis 指控的核心,且与 S2/S3 的幽灵需求证据一致。

### 判决:**限制使用**
- "~1%"只能作为**具名归因的当事方反驳**("SemiAnalysis 称其自有预测仅动 ~1%"),不得作为独立事实承重,必须同句披露 COI。
- ">5 GW 两家在建"可承重(卫星方法+与 C&W 25 GW 宽口径相容),标注方法。
- 文章承重的应是口径分解结论本身:"公告容量大量蒸发(本来就是幽灵)+在建容量大体推进但延误扩大(7.5→10.5 GW 缺口)"——这一结论现为多源(SemiAnalysis、ITK、C&W/CBRE 口径对比)支撑。

---

## S6 内存短缺持续时间的分析师口径(UBS vs "Bloomberg Intelligence")

### 反证搜索角度
1. UBS DRAM "2028" 原文 → 命中多家独立转述(wccftech、Digital Citizen、Yahoo Finance、BigGo);UBS 原始报告为客户报告,不公开(预期内)
2. UBS 口径演变 → 命中 SMBOM 早前转述"UBS:短缺持续到 2027 Q1"——说明"至少到 2028 Q2"是其**上调后**的口径
3. "Bloomberg Intelligence" memory 2026 见顶 → 命中 24/7 Wall St. 等,但溯源后发现归属可疑
4. Shuli Ren 身份核验 → 命中 Bloomberg 原文专栏列表,确认其为 **Bloomberg Opinion 专栏作家**(非 Bloomberg Intelligence 分析师)
5. 搜索真正的 Bloomberg Intelligence 内存供需研究 → **无果**(未找到 BI 署名的"2026 Q2 见顶"研究)

### 找到的独立证据
- **UBS 口径真实存在**,多家独立转述一致:DRAM **供不应求至少持续到 2028 Q2**;需求年增 36.2% vs 供给 19.3%;2027 年供需缺口达创纪录的 17 个百分点;"30 年未见"。限定语:"at least through Q2 2028"(下界表述)。注意这是从早前"到 2027 Q1"**上调**而来的动态口径。
- **"Bloomberg Intelligence"归属错误**:"2026 Q2 见顶、2028 可能过剩"的实际出处是 **Shuli Ren,Bloomberg Opinion 专栏作家**(前投行人士),见其 2026-07-05《Michael Burry Is Right About Memory Chipmakers》、2026-07-07、2026-07-15(CXMT)系列专栏。24/7 Wall St. 转述时误标为"Bloomberg Intelligence's Shuli Ren",仓库沿袭了这一错误。原文限定语是软的:"likely peaked"、"could tip into oversupply by 2028"。
- 语境校准:分析师光谱上,UBS 处于多头端但非孤例(Jefferies 看涨价到 2027;Blocks & Files 报道"supercycle 到 2028";TechPowerUp:厂商自己预期短缺 2028 年底结束);Ren 的"2028 过剩"押注 CXMT 产能与经典周期逻辑,属光谱的空头端,同样非孤例(Michael Burry 同向)。

### 方法学审计
- UBS:卖方研究,原始报告不可得,依赖二手转述——但四家以上独立转述数字一致(36.2%/19.3%/17pp/Q2 2028),转述失真风险低。卖方看多内存股与其投行业务无直接可见 COI,但需保留"卖方研究"标签。
- "Bloomberg Intelligence"标签:**机构归属错误**。BI 是 Bloomberg 的研究部门,Opinion 是个人评论专栏——证据等级差一级(机构研究 vs 专栏观点)。以"Bloomberg Intelligence"之名承重会虚增该反方观点的权威性。

### 判决:**UBS 单源已核可承重(标注卖方研究+"至少"下界+口径曾上调);"Bloomberg Intelligence"口径否决——按现表述不得承重**
- 否决理由:机构归属错误。修正后可用:改为"Bloomberg Opinion 专栏作家 Shuli Ren(2026-07)认为短缺'很可能已于 2026 Q2 见顶',2028 '可能'转向过剩(押注 CXMT 扩产)"——作为具名个人观点与 UBS 对置,A6 的"分歧在 2028"框架仍然成立,但反方一侧的权威等级需降格。

---

## 判决汇总表

| 组 | 判决 | 关键动作 |
|---|---|---|
| S1 | DC/MD 升级多源证实;俄亥俄单源可承重(限) | 归因改为 OPC-DC/Synapse、MD OPC、IEEFA;MD 时点修正 |
| S2 | 限制使用 | 具名 Atkinson+"无系统测量";承重改用 ERCOT 阶段数据 |
| S3 | 单源已核可承重(官方行政数据,限) | 必须附阶段构成;**"198 GW"勘误为"198 件申请"** |
| S4 | 升级多源证实(限) | 换源 TrendForce 22%/Counterpoint 23%;注明晶圆≠bit(bit 仅 ~9%) |
| S5 | 限制使用 | "~1%"仅具名归因+COI 披露;">5 GW"可承重;口径分解结论已多源 |
| S6 | UBS 可承重(限);"BI"口径**否决** | "Bloomberg Intelligence"改"Bloomberg Opinion 专栏 Shuli Ren" |

主要来源:opc-dc.gov(2025-05 新闻稿+Synapse 报告)、opc.maryland.gov(2025-06-12 factsheet)、ieefa.org、aepohiowire.com、utilitydive.com(748214)、ercot.com(2026-04-01 参议院听证 PDF、2026-06-18 Trending Topic)、trendforce.com(2026-06-02 新闻稿)、dramwatch.com(Counterpoint)、newsletter.semianalysis.com、itkservices3.com、bloomberg.com/opinion(Shuli Ren 2026-07 系列)、wccftech/digitalcitizen/yahoo(UBS 转述)、smbom.com(UBS 早前口径)。
