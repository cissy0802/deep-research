# 02a · 锁定口径清单 — 前半(G1–G35 + G-extra)

> 由 Round 2 前半 108 票(8 批 × 3 席 × 36 组)合并。三席不一致时取最严格者:任何一席发现的口径问题都成立,除非另一席明确指出该发现本身有误。
> **成文时必须逐条对照本文件,不得回退到 01 的原始表述。**
> 合并后判决:**HOLDS 3(G6、G8、G16)/ CORRECTED 31 / REFUTED 2(G24、G-extra)**。
> 凡标题带「⚠️」者(**G3、G14、G24、G35、G-extra**),至少一席判 REFUTED,必须读完「不得这样写」再动笔。
> **G-extra 是全票推翻后改写成的正面条目**——原论断「不存在非 BLS 作者的系统性量化评估」是事实错误;取而代之的 Stekler & Thomas(2005)误差指标组是全篇方法学脊柱的最强证据。
> 送 Round 3 双席审计:**21 条**(清单见文末)。

---

## [G1] BLS 2024–34 的 3.1% 就业增长被劳动力预测「锚定」,但不是数学恒等式

- **判决**:CORRECTED(2 CORRECTED / 1 HOLDS;无 REFUTED。取最严格的两席)
- **锁定表述**:
  - 据美国劳工统计局(BLS)就业预测项目新闻稿《Employment Projections — 2024–2034》(USDL-25-1324,2025 年 8 月 28 日 10:00 ET 发布)逐字:「Total employment is projected to increase to 175.2 million and grow 3.1 percent, which is slower than the 13.0-percent growth recorded over the 2014-24 decade.」;全经济体新增 5.2 million jobs。
  - 就业口径(EP Table 2.1,Employment by major industry sector,单位千):2014 = 150,436.3;2024 = 169,956.1;2034 = 175,167.9;2024–34 变动 +5,211.8,+3.1%;2014–24 +13.0%。EP Table 1.2「Total, all occupations / 00-0000」同样给出 169,956.1 → 175,167.9 / +5,211.8 / 3.1。
  - 劳动力口径(EP Table 3.1,Civilian labor force,「Total, 16 years and older」,单位千):2004 = 147,402;2014 = 155,922;2024 = 168,104;2034 = 173,454;2024–34 变动 +5,350,**+3.2%**;2014–24 **+7.8%**。
  - **机制的正确说法**:BLS 假设**目标年(2034)处于充分就业、劳动力市场出清**,因此目标年就业量≈预测劳动力减去摩擦性失业;3.1%(岗位)与 3.2%(人)之所以几乎相等,还额外依赖 BLS 对摩擦性失业率、多重兼职率与自雇比例大致不变的假设,并非模型强制的恒等式。BLS 技术注释逐字:「BLS also assumes that the economy will be at full employment in the projected year, with the labor market at equilibrium. That is, employment in the projected year will be roughly equivalent to the projected labor force minus a level of frictional unemployment (the relationship is not exact because labor force is a count of people, while employment is a count of jobs, and individual people can hold more than one job). BLS does not project an overall labor shortage or surplus because in the BLS projections data framework, labor supply (the labor force) and labor demand (employment) are linked – a projected increase in labor supply necessarily results in an increase in employment.」(BLS 原文此处用 en dash,非 em dash;属无害排版差异)
  - **承重的反证锚点(比原论断更有力,建议写进文章)**:上一个十年这两个口径实际相差 5.2 个百分点——劳动力 2014→2024 +7.8%,就业 +13.0%,岗位/劳动力人口之比由 0.966 升到 1.011;而 2024–34 预测中该比值被假设为几乎不变(1.011→1.010)。**「比值走平」正是这条预测的承重假设本身。** 另,BLS 自己的 2012–22 评估显示劳动力预测误差 0.5pp(预测 +5.5% vs 实际 +6.0%)对应的职业平均就业增速误差却是 2.4pp(10.8% vs 13.2%),两者不是一一映射。
  - 精度说明:5,211.8 / 169,956.1 = 3.07%;5,350 / 168,104 = 3.18%;BLS 各自四舍五入为 3.1% 与 3.2%,「基本等同」成立但相差 0.11pp。
- **证据分级**:多源证实(三席各自经 Wayback `id_` 原始快照或真实浏览器取到新闻稿、技术注释、EP Table 1.2/2.1/3.1 与官方评估页,逐格一致;bls.gov 对脚本/通用 UA 一律 Akamai 403)
- **数字定版**:
  - **就业总量口径统一用 EP Table 2.1 的 169,956.1 → 175,167.9(+5,211.8,+3.1%)**;劳动力用 Table 3.1 的 168,104 → 173,454(+5,350,+3.2%)。理由:两表分别是 BLS 对「岗位数」与「人数」的官方序列,新闻稿正文的 175.2 million / 5.2 million / 3.1 percent 即由前者取整而来。
  - **169,956.1(千个岗位,含自雇与第二职业)与 168,104(千人)口径不同,不可相减、不可互换**,只能并列比较增速。
- **不得这样写**:
  - ❌「这个 3.1% 在数学上基本等同于 BLS 自己的劳动力人口预测……**因为 BLS 模型强制令劳动供给=劳动需求**」——BLS 原文用的是 linked / necessarily results in,并在同一句括注里写明 the relationship is **not exact**;论断恰好省略了这条限定语。改用上面的「锚定 + 三项附加假设」表述。
  - ❌ 暗示「就业增速不可能超过劳动力增速」——2014→2024 就业 +13.0% 就远超劳动力 +7.8%,原因是 2014 年劳动力市场宽松。
  - ❌ 引 Technical Note 时只截「labor supply … are linked」那一句而不带前一句的 full-employment 假设与「not exact」括注。
- **利益相关**:无(BLS 官方统计)。但须注意 BLS 既是预测发布者也是评估者,见 G2。
- **待 Round 3**:否(三席一手逐格一致,属多源证实)

---

## [G2] BLS 自陈「方法不为捕捉极快技术变化而设计」的那篇 MLR 文章,是 BLS 评 BLS

- **判决**:CORRECTED(3/3 票 CORRECTED)
- **锁定表述**:
  - 出处须写全:Christine Machovec、Michael J. Rieley、Emily Rolen,《Incorporating AI impacts in BLS employment projections: **occupational case studies**》,*Monthly Labor Review*,U.S. Bureau of Labor Statistics,**2025 年 2 月**,DOI 10.21916/mlr.2025.1。**副标题不可省**——它限定了该文只是若干职业案例研究,不是全面方法论评估。
  - 引 MLR 那句必须补全整句:「**Although it is always possible that future developments will deviate from historical patterns,** BLS projection methods are not designed to capture extremely rapid technological change and, therefore, assume that the overall pace of technological change will be consistent with past experience.」另一句可独立引用:「The timing and scale of many potential impacts of GenAI are too uncertain to be reflected in BLS projections.」
  - 技术注释(USDL-25-1324)四句逐字可用:「The projections focus on long-term structural trends of the economy and do not try to anticipate future business cycle activity.」/「The projections are not intended to be a forecast of what the future will be but instead are a description of what would be expected to happen under these specific assumptions and circumstances.」(其后紧接一句原稿未引:「When these assumptions are not realized, actual values will differ from projections.」)/「In a future state where technology advances much more rapidly than it has historically, it is unlikely that historical relationships would hold, and therefore BLS projection methods are unlikely to yield reasonable results.」/「BLS methods could capture this, but BLS has no data on which to base these **differential productivity impacts**.」
  - **数码相机案例**:「EP projected that employment in the occupation would decline 23.6 percent from 2004 to 2014. Indeed, employment in the occupation started to fall precipitously in the early 2000s, declining from **a peak of 86,300 in 2004** to 28,800 in 2014, with a further decline to only 9,200 in 2023.」(职业为 photographic process workers and processing machine operators)。该文把它当作「研究驱动的主观调整成功案例」,但 86,300→28,800 实际是 **−66.6%**:**即便在技术路径清晰、已在数据中显现的最有利情形下,BLS 仍把降幅低估了约 3 倍。**
  - **卡车司机案例**:「Employment of **heavy and tractor-trailer truck drivers** was about 1.7 million in 2012 and had grown to over 2.2 million by 2023.」——口径限于重型及牵引挂车司机(SOC 53-3032),不含轻型/送货司机。
  - **评审性质(本条最重要的落点)**:MLR 的三步评审按其 For Authors 页逐字只适用于「All article submissions from **outside BLS** are subject to a rigorous, three-step review process.」;其 Step 2 的 peer review 审稿人也是「subject-matter experts **at BLS**」。三位作者均为 BLS 就业与失业统计办公室(Office of Employment and Unemployment Statistics)经济学家,即被评估项目自身的在编人员。**这是 BLS 雇员在 BLS 自办刊物上评价 BLS 方法,属自评,不可称「同行评审文献」。**
- **证据分级**:多源证实(三席分别经 Wayback `id_` 快照与浏览器直取,五段引语与两个案例数字逐字/逐格一致;For Authors 页与作者简介页二席取到一手)
- **不得这样写**:
  - ❌「卡车司机 2012 约 170 万 → 2023 逾 220 万」——必须加「heavy and tractor-trailer」限定。全口径卡车司机(含轻型送货)规模约为其两倍,不加限定会放大该案例的说服力。
  - ❌ 把「BLS projection methods are not designed to capture extremely rapid technological change」当独立引语——被切掉的前后半句正是 BLS 的自辩(「因此我们假定技术变化速度与历史一致」),单引会读成 BLS 承认方法失效。
  - ❌ 把「BLS has no data on which to base these differential productivity impacts」读成「BLS 承认对 AI 整体无数据」——该句仅限**分行业差异化**生产率影响;BLS 明确表示若生产率提速在各行业均匀,则对就业预测无影响。
  - ❌ 隐含「MLR 是官方刊物所以经同行评审」——见上,外部投稿评审流程不适用于 BLS 在编人员的本机构稿件。
  - ❌ 只引数码相机案例的「BLS 提前调低了预测」而不写实际跌幅 −66.6%——会让读者高估 BLS 捕捉技术冲击的能力,对准大学生是危险的乐观。
- **利益相关**:**明确存在**。发布方 BLS 即被评估方;三位作者是就业预测项目所属部门的在编经济学家;刊物为 BLS 自办。引用时必须随文标注「BLS 自评」。
- **待 Round 3**:否(五段引语三席各自逐字命中,评审制度页二席取到一手)

---

## ⚠️ [G3] BLS 方框「关注方向而非精确值」是软性提示;「从不发布情景区间」被推翻

- **判决**:CORRECTED(2 CORRECTED / **1 REFUTED**;方框主体三席一致 HOLDS,附加论断三席一致认定被证伪。第 3 席就此整条判 REFUTED,故标 ⚠️)
- **锁定表述**:
  - 方框逐字(USDL-25-1324 内嵌方框,标题「Interpreting the Employment Projections」;同一段文字亦原样出现在 EP FAQ「How accurate are BLS projections?」条目):「The Employment Projections (EP) program estimates specific values for projected employment levels and growth rates. However, this precision in the data does not account for the inherent uncertainty of predicting long-term changes in the labor market. Focusing on the direction and relative size of projected changes, rather than on the precise value estimates, **may** yield similar insights into employment trends and themes across occupations and industries.」
  - **必须补引方框第二段**(原稿以省略号截掉):「The EP program also conducts research on factors that are expected to affect employment, which may not be reflected in historical data, such as emerging technologies and new legislation. Adjustments based on this research are generally applied conservatively such as when there is convincing evidence for a long-term structural change.」——这一段是 BLS 的自辩,说明它确实做前瞻性调整、只是很保守。
  - **不确定性披露的正确表述**:「**现行**EP 十年期预测只发布单一情景的点估计,不附统计意义上的置信区间/预测区间;但 BLS 有发布情景区间的先例。」两条一手先例:
    - **疫情情景(最近一次)**:2021 年初 BLS 就 2019–29 预测另发布了两套 alternate projections——moderate impact 与 strong impact。MLR 2022-02《Expected pandemic-driven employment changes: a comparison of 2019–29 and 2020–30 projection sets》摘要逐字:「Because these projections did not reflect the potential long-term impacts of the coronavirus disease 2019 (COVID-19) pandemic, BLS developed alternate 2019–29 projections in early 2021, capturing those impacts for selected industries and occupations.」;用途逐字:「these scenarios sought to identify industries and occupations whose employment trajectories might be subject to higher levels of uncertainty because of the pandemic.」;BLS Career Outlook(2021,《Effects of the pandemic on projected employment in selected industries, 2019–29》)逐字:「The alternate sets of projections are not intended as precise estimates of employment change over the 2019–29 decade; instead, they identify industries in which employment is subject to the most pandemic-related uncertainty.」
    - **历史多档情景**:MLR 1983 年 11 月 Andreassen / Saunders / Su《Economic outlook for the 1990's: three scenarios for economic growth》逐字:「The new estimates consist of a moderate-growth case, and high-growth and low-growth alternatives」及「none of the three projections should be favored as the most likely… to examine the implications of a reasonable range of demand growth over the projection period」;MLR 1997 年 11 月(1996–2006 劳动力预测)逐字:「An alternative immigration scenario… BLS prepared an alternative labor force projection reflecting the high net immigration scenario from the Census Bureau」。到 MLR 1999-11《The U.S. economy to 2008》与 2001-11《Labor force projections to 2010》全文检索 low growth / high growth / alternative scenario 均零命中,只剩单一 moderate 方案。
- **证据分级**:方框主体=多源证实(三席逐字一字不差);「BLS 曾发布情景区间」=多源证实(疫情情景由二席各自取到 MLR 2022-02 / MLR 2021 / Career Outlook 三处一手;1980–90 年代多档情景由一席取到 PDF 全文一手)
- **数字定版**:不适用(本条无数字争议)。**时间口径定版**:统一写「**自 1990 年代末起,BLS 常规十年预测不再发布高/低增长替代方案;2021 年疫情期间曾为 2019–29 单独发布两套情景**」,不写「从不」。
- **不得这样写**:
  - ❌「BLS 自己劝读者**不要看精确数值**」——原文是「may yield similar insights」,软性提示,不是劝阻使用数值。
  - ❌「BLS 只发点估计,**从不**发布预测的置信区间或情景区间」——**「从不」是硬错误,三席一致认定被一手证据推翻**,第 3 席据此整条判 REFUTED。必须拆成两句:统计置信区间确实从不发布;情景区间发布过(2021 年疫情两套 + 1980–90 年代高/中/低三档)。
  - ❌ 只引方框第一段——会把 BLS 描绘成纯外推、比实际更「认怂」的模型,对读者不公。
- **利益相关**:无(BLS 官方文本),但同 G2:此处是 BLS 对自身预测精度的自我描述。
- **待 Round 3**:否(证伪所需的一手件由两席各自独立取到,方向一致)

---

## [G4] BLS 历次预测评估:误差方向会翻转,单向偏差断言都不成立

- **判决**:CORRECTED(3/3 票 CORRECTED)
- **锁定表述**:
  - **方向准确率必须标明分母,不可并列成一组「准确率」**:**86%** = 2014–24,22 个**大类职业组**(major occupational groups),逐字「BLS correctly projected whether an occupational group would grow or decline 86 percent of the time.」;**77%** = 2012–22,同为 22 个大类职业组,逐字同句式;**69%** = 2014–24,**16 个大类产业部门**(major industry sectors),逐字「BLS correctly projected which major industry sectors would grow and which would decline 69 percent of the time.」86% 与 77% 分母相同、仅轮次不同;69% 分母不同。
  - **增速低估是双轮一致的**:2014–24 职业平均增速 预测 6.5% vs 实际 **12.9%**;2012–22 预测 10.8% vs 实际 **13.2%**。
  - **57.9% 的完整口径**:2014–24 职业评估 Table 2「Detailed occupations, combined scorecard」公布的是 **Count of better score:BLS 475 / Naïve(occupational-share)345**;820 与 57.9% 系据此自行推算(475 ÷ 820 = 57.93%),**非 BLS 发布口径**。**必须同时给平衡信息**:同一张表的另一指标 Sum of absolute differences of employment shares 上 BLS 19.6 优于 Naïve 21.1,大类层面 BLS 13:9 胜出。可比性背景:820 是 BLS 对 SOC 2010→2018 做映射后纳入全部职业的结果;2012–22 那轮只保留 1:1 匹配的 748 个职业,BLS 胜出 432/748 = 57.8%——**两轮几乎相同**。
  - **参与率三组数字(引用时须注明是勘误后版本)**:MLR **2015 年 11 月**,Kathryn J. Byun、Richard Henderson、Mitra Toossi,《Evaluation of BLS employment, labor force and macroeconomic projections to 2006, 2008, and 2010》,**2015 年 12 月 10 日更正**。Figure 3C 逐格(base / projected / actual):1996–2006 = 66.8 / 67.6 / 66.2;1998–2008 = 67.1 / 67.6 / 66.0;2000–10 = 67.1 / 67.5 / 64.7。勘误逐字:「In figure 2B, several of the projected labor force participation rates for 1996–2006 and 2000–10 originally shown in the figure were somewhat lower than the rates BLS actually projected. In figure 3C, the base year labor force participation rate for 2000–10 was corrected to 67.1 instead of 67.2.」
  - **参与率高估 ≠ 劳动力规模高估(本条最容易写错的一处)**:同一篇评估逐字「BLS anticipated underprojections of population from the U.S. Census Bureau and offset them with slight adjustments to the BLS-projected labor force participation rates. **These adjustments resulted in accurate projections of the labor force for each of the three sets of projections to 2006, 2008, and 2010.**」Figure 3A 劳动力逐格(预测 / 实际,千人):1996–2006 = 148,847 / 151,428(**低估**);1998–2008 = 154,576 / 154,287(几乎打平);2000–10 = 157,721 / 153,889(高估)。真正被系统性高估的是**就业总量与商品生产部门**:逐字「overprojected the goods sectors by nearly 7 percent in 2006, more severely by 15.8 percent in 2008, and 33.4 percent in 2010」。
  - **制造业**逐字:「However, the magnitude of the decline in manufacturing was greatly underestimated.」及「The largest directional error was the belief, in all three sets of projections, that manufacturing had reached its trough and would stay nearly flat」。
  - **评估缺口(两处,须都写)**:① 2010–20 从未被评估——原句完整为「Due to the impact of the COVID-19 pandemic on data for 2020, BLS did not evaluate the 2010–20 projections. **BLS is in the process of evaluating previous evaluations.**」该句 2026-02-13 快照仍在评估首页(页面自注 Last Modified Date: August 29, 2024),但 **BLS 于 2026-04-10 改版后已整段删除**,现行首页只写「With the release of the 2014–24 Projections Evaluations, BLS did not evaluate the 2014–24 Labor Force Projections or the Macro Projections.」(同句亦见于 Methods of Projections Evaluation 页)。事实内核仍成立:评估目录中 2002–12 / 2004–14 / 2006–16 / 2008–18 / 2012–22 / 2014–24 一应俱全,唯独没有 2010–20。② **2014–24 这一轮 BLS 连劳动力预测与宏观预测的评估都没做**——意味着 G1 所依赖的「劳动力预测锚定就业」这一环,最近一轮根本没有被官方检验过。
- **证据分级**:多源证实(三个方向准确率、475/345、参与率与制造业引语三席各自逐字命中;Figure 3A/3C 逐格数据由二席分别经数据表与页面 Highcharts 对象独立读出)
- **数字定版**:
  - **57.9% 必须写成「475 / 345(合计 820),自行推算为 57.9%,非 BLS 口径」**,并紧跟 19.6 vs 21.1 与大类 13:9。理由:只写 57.9% 是单边取材,偏向不利于 BLS 的一侧,与本文的引用伦理自相矛盾。
  - **2014–24 的 12.9% 与 G1 的 13.0% 不得混用**:12.9% 是**各职业平均增长率**(对应预测 6.5%),13.0% 是**总就业增长率**,两者是不同测度,数值接近纯属巧合。
  - **2010–20 那句引语一律改引 Wayback 快照**(评估首页 2026-02-13 及更早快照),不得链现网。
- **不得这样写**:
  - ❌「1996–06 / 1998–2008 / 2000–10 三版**系统性高估**」不加限定——高估的是**劳动参与率、GDP 增速(2000–10 版)、非农就业与商品生产部门**;**劳动力人数三次都准**(其中 1996–2006 版还是低估)。不加限定地写「三版系统性高估」,本身就犯了本文要批判的那个错。
  - ❌ 把 86% / 77% / 69% 并列成一组「BLS 准确率」——69% 的分母是产业部门,不与前两者可比。
  - ❌「BLS 在细分职业层面只赢过 naïve model 57.9%(475/820)」而不说这是自算、也不给另一指标。
  - ❌ 引用参与率数字而不标「MLR 2015 年 11 月刊,2015-12-10 更正」与三位作者署名——勘误对象恰是本论断依赖的图。
  - ❌ 按现址链接「2010–20 从未被公开评估」那句——现行页面已删,读者点进去找不到。
- **利益相关**:BLS 评估 BLS(评估页与 MLR 评估文均由 BLS 出品),须与 G2 同样标注;但 2014–24 评估表中 BLS 输给 naïve 模型的项目被如实公布,自评仍具参考价值。
- **待 Round 3**:否(全部数字与引语三席各自回到一手并逐字/逐格一致)

---

## [G5] 跨 SOC 版次(2010→2018)的「预测 vs 实际」对照表:四行可全额承重,三行必须改写

- **判决**:CORRECTED(3/3 票 CORRECTED。第 2 席对其中 software developers **单行**判 REFUTED,但第 3 席明确指出该行不必 REFUTED——加总算术无误、论断方向不倒,仅误在偏保守一侧;故整条不标 ⚠️,而把该行的口径问题全额写入「不得这样写」)
- **锁定表述**:
  - **数据来源**:2014–24 预测值取自 BLS Projections Archive 的 `2014-24.zip`(9,823,242 字节)→ `2014-24/occupation.xlsx`,工作表「Table 1.2 Employment by detailed occupation, 2014 and projected 2024 (Numbers in thousands)」,**2010 SOC**;2024 实际值取自当期 `occupation.xlsx`(EP Table 1.2「Occupational projections, 2024–2034, and worker characteristics, 2024」),**2018 SOC**。可比性判定依据 OMB/SOCPC 官方《2010 to 2018 SOC crosswalk》(`soc_2010_to_2018_crosswalk.xlsx`,BLS 代 OMB 与 Standard Occupational Classification Policy Committee 发布,**2017 年 11 月**)。**三席逐格核对:原表全部数字无误。**
  - **【A 组:官方 crosswalk 证实严格一对一(两向唯一、无拆无并、无 (#)/(##) 标记),可全额承重】**(2014 实际 / 2024 预测(变动%) / 2024 实际(2014→2024 实际变动%),单位千人):
    - Computer programmers 15-1131→15-1251:328.6 / 302.2(−8.0%) / **121.2(−63.1%)** ——**全表最干净、最可承重的一行,「BLS 大幅低估崩塌」成立,不必弱化。**
    - Computer systems analysts 15-1121→15-1211:567.8 / 686.3(+20.9%) / 521.1(−8.2%)——**方向判反**。
    - Information security analysts 15-1122→15-1212:82.9 / 97.7(+17.9%) / 182.8(+120.5%)。
    - Network and computer systems administrators 15-1142→15-1244:382.6 / 412.8(+7.9%) / 331.5(−13.4%)——**方向判反**。
  - **【B 组:Software developers,必须双重加注】**
    - 口径注一:**2010 SOC 中不存在「Software developers」这一职业,2014–24 表里没有这一行**(全表 1,096 行,零命中)。1,114.0 与 1,300.7 是自行合成:15-1132 Software developers, applications(718.4 / 853.7)+ 15-1133 Software developers, systems software(395.6 / 447.0)。加总算术无误,但**必须标明为自行合成,不得写成 BLS 行**。
    - 口径注二:15-1132 与 15-1133 在 2018 SOC 中**同时**流向 15-1252(Software developers)**和**新设的 15-1253(Software quality assurance analysts and testers,2024 = 201.7),故 15-1252 是 2010 口径的真子集。同口径可比区间:下界 1,114.0→1,693.8 = **+52.0%**;上界 1,114.0→(1,693.8+201.7=1,895.5)= **+70.2%**。
  - **【C 组:Computer and mathematical occupations 15-0000,须加可比性脚注】**:4,068.3 / 4,599.7(+13.1%) / 5,416.7(约 +33%)。2018 SOC 对该大组边界双向都动过——**流入**:43-9011 Computer operators(2014 = 61.1)整体并入 15-1299;**流出**:15-1199 Computer occupations, all other(2014 = 233.0)的一部分划至 13-1082 Project Management Specialists。以 61.1 千做粗调,可比区间约 **+31% ~ +36%**。方向与量级站得住,但 +33.1% **不应作精确值书写**。全表穷举确认跨 15-0000 边界的条目仅此两条。
  - **【D 组:Data scientists 15-2051,不得用于增长论证】**:该码系 2018 SOC 新设,官方 crosswalk 中**唯一**来源是 2010 SOC 的 15-2099 Mathematical Science Occupations, All Other,而该码 2014 年只有 **1.8 千人**(其上级桶 15-2090 Miscellaneous mathematical science occupations 全部也只有 3.0 千)。故 2024 年的 **245.9 千几乎全部是重新分类/重新计量的产物**,不是从 1.8 千长出来的组织性增长。这一行**只能用来说明「2018 年 SOC 才承认这个职业」**。
  - **【E 组:原稿自列的两个踩坑点,三席复核属实,保留】**:(a) 15-1253 Software QA analysts and testers 2024 = 201.7,确为 2018 SOC 新设;(b) 15-1134 Web developers(2014 = 148.5)被拆为 15-1254 Web developers(86.0)+ 15-1255 Web and digital interface designers(128.9)= 214.9,单看前者会得出「腰斩」的错误结论;但 15-1255 同时还从 15-1199 取值,故 **214.9 是上界**。
  - **【F 组:BLS 自己的可比性警告,须随表引用】**:Projections Archive 页「Difficulties in comparing projections」逐字:「Changes to classifications can make it difficult to compare industries or occupations over time… these changes can result in comparability issues **which are not always obvious**.」及「Changes to methods can mean that certain estimates do not describe the same concepts or populations over time.」;2014–24 职业评估页逐字:「Changes in methodology and classifications in these programs and surveys result in challenges with evaluating occupational projections at a detailed level.」;MLR 2015 评估文更直接:「Evaluation of employment by occupation for these sets of projections was omitted entirely because of the revised classification system.」——**BLS 曾因分类改版整个放弃做职业层面的评估**。BLS 自己做 2014–24 评估时的处理逐字:「applied a mapping between the two SOC classification systems … aggregating employment from multiple occupations or applying ratios based on previous employment, depending on how the occupations were split or combined between the 2010 and 2018 SOC systems」。
  - **【G 组:一席额外发现,建议作反例点出】**:同两份文件里 Management occupations 2014 = 9,157.5(占比 6.1%)→ 2024 = 13,607.6(占比 8.0%),十年 +48.6%;Computer and information systems managers 2014 = 348.5 → 2024 = 667.1(+91%)。这种量级不可能是真实增长,是 SOC/OEWS 计量口径变化——**侧证跨版次的「预测 vs 实际」在细分层面普遍被口径污染**;而 BLS 自家评估表里 Management 恰是输给 naïve 模型最多的大类(BLS 2.17 vs Naïve 2.11)。
- **证据分级**:多源证实(三席各自下载 2014-24.zip 与当期 occupation.xlsx 逐格读出、并各自逐行读 OMB/SOCPC crosswalk;第 1、2 席另各自程序穷举了跨 15-0000 边界的映射,结果一致)。**G 组(Management 反例)为单席发现,未经第二席复核,标「单源已核」。**
- **数字定版**:
  - **Software developers 的实际增幅:文章写「至少 +52.0%(同口径可比区间 +52% ~ +70%)」,「实际增幅是预测的 3.1 倍」改为「至少 3.1 倍,上界约 4.2 倍」**(52.0/16.8 = 3.10;70.2/16.8 = 4.18)。理由:+52.0% 是把 15-1253 全部算作来自 15-1199 的下界假设,+70.2% 是全部算作来自 15-1132/33 的上界假设,真值必在其间;取下界当点估计方向不错但低报了自己的论点。
  - **15-0000 大组:写「约 +33%(非严格可比,可比区间约 +31%~+36%)」**,不写 +33.1%。理由:该组边界双向变动,+33.1% 是不同口径两端相减的结果。
  - **Web developers:写「148.5 → 214.9(合并 15-1254+15-1255),为上界」**,不得单引 86.0。
  - **Data scientists:不定版、不入增长表**——245.9 只能作分类史料使用。
- **不得这样写**:
  - ❌「Software developers 1,114.0 / 1,300.7(+16.8%)/ 1,693.8(+52.0%)——实际增幅是**预测的 3.1 倍**」——两处错:① 1,114.0 与 1,300.7 是自行合成的两行之和,不是 BLS 行(第 2 席就此单行判 REFUTED);② 1,693.8 与 2014 口径不等价,+52.0% 是下界而非点值。
  - ❌「Data scientists:2010 SOC 中不存在该代码,2024 实际 245.9」而不加限定——任何「数据科学家十年增长上百倍」的读法都是错的;把 245.9 当作「数据科学家岗位增长」呈现给准大学生是重大误导。
  - ❌「Computer and mathematical occupations +33.1%」作精确值——非严格同口径。
  - ❌ 单引 15-1254 Web developers 86.0 说「腰斩」——须合并 15-1255 后为 214.9(且为上界)。
  - ❌ 沿用采集者「对所有行都提示重大 SOC 断层风险」的笼统警告——**风险定位错了**:程序员、系统分析师、信息安全、网络管理员四行经官方 crosswalk 检验完全干净,对这四行的泛泛提示是多余的,反而会削弱本文最能承重的证据。
  - ❌ 不披露采集者原未做 crosswalk——该自陈应保留,并配 F 组 BLS 自己的警告。
- **利益相关**:无(BLS/OMB 官方分类与统计文件)。但须注意:分类变更的执行者与预测评估的执行者是同一机构。
- **待 Round 3**:**是**。理由:这是本批唯一一条**由验证者自行构造、且承重的量化对照表**(跨 SOC 版次的「预测 vs 实际」),BLS 自己都因分类改版而放弃过职业层面评估。需审计:① **方法学审计席**——复核 A 组四行「两向唯一」的判定是否穷尽(须独立重跑 crosswalk 的正向与反向扫描,确认无第三方 2010 码流入 15-1251/15-1211/15-1212/15-1244,并核实 (#)/(##) 标记语义;若任一行的一对一判定不成立,该行的「方向判反 / −63.1%」结论即不得承重);② 复核 B 组 +52%~+70.2% 区间的上下界假设是否穷尽(15-1253 的第三个来源 15-1199 未被量化分摊);③ 复核 C 组 +31%~+36% 粗调的算法(仅用 43-9011 的 61.1 千,未量化 15-1199→13-1082 的流出规模,而 13-1082 2024 年已达 1,046.3 千);④ **反证搜索席**——检索是否存在独立团队(学界/智库/OEWS 研究)已发布的 2010→2018 SOC 回溯可比序列,可用于交叉验证或替代本文自建的对照表;⑤ 复核 G 组 Management +48.6% 这一单席发现(目前无第二席核对)。**在 ①③ 未通过前,本表只能以「四行严格可比 + 三行加限定」的形式呈现,不得作为整表统计结论使用。**

---

## [G6] BLS 的「occupational openings」是十年年均流量、97.2% 来自分离而非新增岗位,且与 JOLTS 空缺是两个构念

- **判决**:HOLDS(3/3 票 HOLDS,无 CORRECTED、无 REFUTED)
- **锁定表述**:
  - 据美国劳工统计局(BLS)《Employment Projections》2024–34 vintage,`occupation.xlsx` 之 **Table 1.10**,表标题逐字为 "Table 1.10 Occupational separations and openings, projected 2024–34 (Employment in thousands)",openings 列表头逐字为 **"Occupational openings, 2024–34 annual average"**——**这是十年期的年均流量,不是任一时点的存量,也不是十年累计量**。
  - 该表 "Total, all occupations"(SOC 00-0000,Summary 行)逐格:2024 年就业 **169,956.1 千**;2034 年就业 **175,167.9 千**;十年净变化 **+5,211.8 千(+3.1%)**;年均 labor force exits **8,155.0 千**;年均 occupational transfers **10,187.1 千**;年均 total occupational separations **18,342.1 千**;年均 occupational openings **18,863.3 千**。换算:年均 openings 约 **1,886.33 万**,其中分离 **1,834.21 万**、净增 **52.12 万**。
  - 构成恒等式(不是近似,是定义):**openings = 年均 total separations + 十年净变化 ÷ 10**。复算 18,342.1 + 5,211.8/10 = 18,863.28 ≈ 18,863.3(表内四舍五入)。三席分别在全部 **832 条 "Line item" 明细职业**上逐行验证,残差全部 ≤0.1,最大偏差 0.000,**零例外**。故占比为:分离贡献 18,342.1/18,863.3 = 97.237% → **97.2%**;净增贡献 521.18/18,863.3 = 2.763% → **2.8%**。
  - openings 定义逐字(BLS,https://www.bls.gov/emp/documentation/separations.htm,Wayback 20260612174136):"To project occupational openings, the Bureau of Labor Statistics (BLS) calculates an estimate of separations caused by workers exiting the labor force, due to retirement or other reasons, and separations caused by workers transferring to different occupations. Projections of separations are combined with projections of employment change to determine occupational openings. **This estimate of openings does not count workers who change jobs but remain in the same occupation.**"——即**同职业换雇主不计入**。
  - 与 JOLTS 的区分逐字(BLS separations FAQ,https://www.bls.gov/emp/documentation/separations-faqs.htm):"The JOLTS job openings metric is a **stock measure** of the number of job openings, or positions that are open, not filled, on the last business day of a month. In contrast, occupational openings are projections of the number of positions that are created and filled on an **annual basis**… There is therefore **no way** to create an annual average metric of job openings from JOLTS that could be compared with the annual average number of occupational openings." 两个构念不可互换、不可相除、不可同图并置。
  - **必带的结构限定(三席各自独立提出,合并后为强制)**:18,342.1 千分离中,**occupational transfers 10,187.1 千(占分离 55.5%,占 openings 54.0%)、labor force exits 只有 8,155.0 千(占分离 44.5%,占 openings 43.2%)**。即所谓「补缺」的**多数是转去别的职业的在职者,不是退休腾位**。
  - **另一必带限定**:BLS 同一 FAQ 写明 "For declining occupations, **not all workers who separate need to be replaced**",且自述使用限度为 "projections of openings are best used to give a general sense of the scale of expected openings, especially in relation to other occupations"。
- **证据分级**:多源证实(三席各自独立取件、独立复算,832 行全量验证结果一致;定义句与 FAQ 句三席逐字命中同一 BLS 页面)
- **不得这样写**:
  - ❌「BLS 预测未来十年有 1,886 万个职位空缺」——漏掉「年均」。这是 2024–34 的**年均流量**,十年累计约 18.86 亿人次口径,两者差 10 倍。
  - ❌「97.2% 的 openings 是替补岗位/替补退休者」——两处错。一是严格表述只能是「**年均分离量相当于 openings 的 97.2%**」(衰退职业的负增长项已在总量里相抵,BLS 明说衰退职业的分离者并非都需要被替补);二是分离中 55.5% 是**职业间转移**,不是退休,写成「退休潮腾出岗位」是事实错误。
  - ❌ 把 EP 的 openings 与 JOLTS 的 job openings 相互印证、相除或并列成时间序列——BLS 自己写明二者「no way to compare」,一个是月末存量、一个是年度创造并填补的流量。
  - ❌「换工作也算一个 openings」——同职业换雇主**明确不计入**;只有跨职业转移与退出劳动力才计入。
- **利益相关**:无(联邦统计机构的公共数据产品)。但须注意 BLS 同时是本篇后文(G9、G-extra)的被评估方。
- **待 Round 3**:否(三席全量独立复算一致,属多源证实)

---

## [G7] openings 榜首 15 名中 13 个低于全职业中位薪、6 个(不是 5 个)在萎缩;BLS Career Outlook 那句引语只覆盖「无学历要求」一档

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - 排名口径:在 `occupation.xlsx` **Table 1.2 / Table 1.10 的 832 条 "Line item" 明细职业**内按 2024–34 年均 openings 降序排列(**不含 Summary 汇总行**,否则重复计数)。三席分别独立重排,前 15 名的职业、顺序与每一格数值全部一致。
  - 基准值:全职业 **2024 年 5 月中位年薪 $49,500**(Table 1.2 "Median annual wage, dollars, 2024[1]" 的 Total, all occupations 行)。脚注 [1] 逐字口径:数据来自 **OEWS(Occupational Employment and Wage Statistics)**,"Wage data cover **non-farm wage and salary workers** and do not cover the **self-employed**…"。此口径与 openings 的全岗位口径**略有错配**(openings 含自雇),属标准做法但必须写明。
  - 前 15 名(年均 openings 千人 / 2024 年中位年薪 / 分离占 openings 比):Fast food and counter workers 904.3 / $30,480 / 97.4%;Home health and personal care aides 765.8 / $34,900 / 90.3%;Retail salespersons 555.8 / $34,580 / 100.4%;Cashiers 542.6 / $31,190 / 105.8%;Stockers and order fillers 472.3 / $37,090 / 95.0%;Waiters and waitresses 456.7 / $33,760 / 100.4%;Laborers and freight, stock, and material movers, hand 384.3 / $38,940 / 98.9%;Janitors and cleaners 351.3 / $35,930 / 98.6%;Customer service representatives 341.7 / $42,830 / 104.5%;General and operations managers 308.7 / $102,950 / 94.7%;Office clerks, general 282.4 / $43,630 / 106.3%;Cooks, restaurant 250.7 / $36,830 / 91.3%;Heavy and tractor-trailer truck drivers 237.6 / $57,440 / 96.3%;Nursing assistants 204.1 / $39,530 / 98.4%;Secretaries and administrative assistants, except legal, medical, and executive 202.8 / $46,290 / 101.5%。
  - **15 个中 13 个低于 $49,500**,高于的只有 General and operations managers($102,950)与 Heavy and tractor-trailer truck drivers($57,440)。
  - **「分离占比 >100% ⟺ 该职业十年净就业萎缩」是严格恒等式,不是相关**:现行方法下 openings ≡ 年均 separations + 年均净变化,**无下限截断**(三席在全部 832 行上验过),故 sep/openings > 1 当且仅当净变化 < 0,充分且必要。
  - **前 15 名中 >100% 的是 6 个,不是 5 个**(十年净变化,千人):Retail salespersons 100.4% / **−19.6**;Cashiers 105.8% / **−313.6**;**Waiters and waitresses 100.4% / −16.3**(SOC 35-3031,2024=2,329.7 → 2034=2,313.5,−0.7%,年均 −1.63 千);Customer service representatives 104.5% / **−153.7**;Office clerks, general 106.3% / **−177.8**;Secretaries and administrative assistants 101.5% / **−30.8**。原表述漏了 Waiters,且原文自己的分行数据里已写明其为 100.4%,属**前后自相矛盾**。
  - **BLS Career Outlook 引语的正确射程**:该句出自 Elka Torpey《Education level and projected openings, 2024–34》,BLS Career Outlook,2025 年(https://www.bls.gov/careeroutlook/2025/article/education-level-and-openings-2024-34.htm,Wayback 20260612174813 / 20251121173416),逐字为 "Each of the occupations in **chart 1**, like most at **this education level**, had wages below the median for all occupations."。**chart 1 是「No formal educational credential」这一学历档内 openings 最多的前 10 个职业**(该档共 109 个职业,与按 Table 1.2 分组的计数吻合),同文前一段写明 "The occupations in chart 1 account for nearly **7 out of 10** openings projected at **this education level**"。**"this education level" 指的就是无学历要求档,不是全经济 openings 前 15 榜**。同文对 chart 2–5 给出的是相反结论,其中 chart 4、chart 5 的职业**每一个都高于**全职业中位薪。
  - 可用的改写版:「BLS 自己在按学历档拆分 openings 时承认:**无正规学历要求那一档**里 openings 最多的职业,几乎每一个都低于全职业中位薪。」全经济前 15 榜的「13/15 低于中位薪」是**本文自算**,须标注为自算,不得挂在 BLS 那句引语上。
- **证据分级**:多源证实(15 行逐格数值三席各自独立复算一致;恒等式三席各自在 832 行全量验证;引语三席逐字命中同一 Wayback 快照)
- **数字定版**:
  - 萎缩职业数 **定版为 6 个**(两席独立指出漏列 Waiters,第三席未提及但其列出的 Waiters 数值 100.4% 与之一致,无任何一席反对)。文章行文用「前 15 名里有 6 个正在萎缩」。
  - 低薪职业数 **定版为 13/15**,分母口径写明为「832 条明细职业中按年均 openings 排序的前 15 名」。
- **不得这样写**:
  - ❌ 把 "Each of the occupations in chart 1… had wages below the median for all occupations." 放在全经济前 15 榜之后——会被读成 BLS 承认整张 openings 榜低薪。BLS 承认的只是**无学历档**的头部职业低薪,该文对更高学历档给出相反结论。三席全部点名这一处。
  - ❌「retail、cashiers、customer service reps、office clerks、secretaries **五个**净减少」——漏了 Waiters and waitresses,实为六个。
  - ❌「低于全职业中位数」不写数值与口径——必须写「低于 **2024 年 5 月全职业中位年薪 $49,500(OEWS 口径,仅覆盖非农工资薪金雇员,不含自雇者)**」。
  - ❌ 把「13/15 低于中位薪」说成 BLS 的结论——那是本文在 Table 1.2/1.10 上自算的,BLS 未作此陈述。
  - ❌ 把「分离占比 >100%」说成「大致意味着」「往往意味着」——它在现行(2016–26 起)方法下是充要条件;但**在旧方法下不成立**(旧法对衰退职业把增长项截断为零,见 G9),跨 vintage 使用该判据是错的。
- **利益相关**:无
- **待 Round 3**:否(三席一致且均为一手全量复算)

---

## [G8] 按 BLS「入职典型学历」分档:三个学位档只占年均 openings 的 20.6%,却占十年净增的 58.0%;机制是分离率梯度

- **判决**:HOLDS(3/3 票 HOLDS,无 CORRECTED、无 REFUTED;三席均附口径注脚)
- **锁定表述**:
  - 方法口径:取 `occupation.xlsx` Table 1.2 的 **832 条 "Line item"**(排除 Summary 行),按第 13 列 **"Typical education needed for entry"** 分组加总。明细行合计 emp = 169,956.4 千、openings = 18,861.6 千、change = 5,210.7 千,与官方 Total 行 169,956.1 / 18,863.3 / 5,211.8 仅差四舍五入,**无覆盖缺口**。三席各自独立重算,八档数字逐个一致。
  - 2024–34 **年均 openings**(千人 / 占比,分母为明细行合计 18,861.6):High school diploma or equivalent 6,753.6 / 35.81%;No formal educational credential 6,287.8 / 33.34%;Bachelor's degree 3,333.5 / 17.67%;Postsecondary nondegree award 1,161.1 / 6.16%;Some college, no degree 440.2 / 2.33%;Associate's degree 332.3 / 1.76%;Master's degree 316.8 / 1.68%;Doctoral or professional degree 236.3 / 1.25%。
  - **三个学位档(Bachelor's + Master's + Doctoral/professional)合计年均 openings 3,886.6 千**,占 **20.61%**(明细行分母)或 **20.60%**(官方 Total 18,863.3 为分母)——两种分母均为 **20.6%**。
  - 同三档 **2024 年就业 42,469.6 + 3,828.8 + 4,511.3 = 50,809.7 千 = 29.90%**(官方 Total 169,956.1 为分母)。
  - 同三档 **2024–34 十年净增 2,378.5(Bachelor's,45.65%)+ 391.7(Master's,7.52%)+ 255.0(Doctoral,4.89%)= 3,025.2 千**,占 **58.05%**(官方 Total 5,211.8 为分母)/ **58.06%**(明细行合计 5,210.7 为分母)。
  - **Some college, no degree = −157.0 千(−3.0%),是八档中唯一净减少的一档**,其余七档全为正。
  - **机制(三席各自独立实算,成立且梯度单调)**:按档加权的年均 total occupational separations rate 为 Doctoral 4.67% < Master's 7.25% < Bachelor's 7.29% < Associate's 9.10% < Postsecondary nondegree 10.52% < Some college 10.83% < High school 10.96% < **No formal credential 15.47%**;拆开看 exit rate 2.72%→7.08%、transfer rate 1.96%→8.38%,**两个分量同向**。即学位档 openings 相对少,源于**低分离率**,不是源于岗位少。
  - **必带的字段限定**:"Typical education needed for entry" 是 **BLS 分析师指派给每个细类职业的属性**,不是在岗者的实际学历分布。定义逐字(https://www.bls.gov/emp/documentation/nem-definitions.htm,亦见 definitions.htm):"The Bureau of Labor Statistics (BLS) education and training classification system consists of three categories of information that **BLS analysts have assigned** to each detailed occupation… **Typical education needed for entry.** This category best describes the typical level of education that most workers need to enter the occupation. Occupations are assigned one of the following **eight** education levels…" BLS 另在 MLR《Employment trends by typical entry-level education requirement》(2017)明说该字段与劳动者实际受教育程度是不同概念。
- **证据分级**:多源证实(三席各自下载同一底件、各自分组重算,八档绝对值与占比逐个一致;分档职业计数另经 BLS Career Outlook 自述的 No formal credential 109 个 / High school 326 个独立佐证)
- **数字定版**:
  - **58.0% 定版使用官方 Total 5,211.8 千作分母(= 58.05%)**,并在文中写明分母是「published Total, all occupations 的十年净变化」。理由:全篇其他占比(20.6%、29.9%)均已用官方 Total 行作分母,统一分母可避免读者对不上账;用明细行合计 5,210.7 会得 58.06%→58.1%,差异不影响任何结论。
  - **20.6% 与 29.9% 亦定版使用官方 Total 行分母**(18,863.3 与 169,956.1)。
- **不得这样写**:
  - ❌「三个学位档只占 20.6% 的 openings,却拿走 58% 的**新增岗位**」——**58.0% 的分母是净增量**(已被衰退职业对冲后的余额 +5,211.8 千,其中已扣掉 Some college 的 −157.0),**不是新增岗位总量**。若改用「仅正增长之和 5,367.7 千」作分母,三学位档占 **56.4%**。并列 20.6% 与 58.0% 时必须写清两者说的是不同的东西。
  - ❌ 把「入职典型学历」说成「从业者的学历」或「岗位要求的学历门槛」——它是 BLS 分析师的指派属性,该限定语必须随数字出现。
  - ❌「学位档 openings 少 = 学位职业更稳定」只讲一面——同一组数字也意味着学位类职业相对其存量每年可进入的口子更窄,对求职者是双刃的(第 3 席点名)。
  - ❌ 混用分母而不声明——20.61%/20.60%、58.06%/58.05% 的差异全部来自明细行合计 vs 官方 Total 行,写作时须锁定一套。
- **利益相关**:无
- **待 Round 3**:否(三席独立复算一致)

---

## [G9] 2014–24 与 2016–26 两版 openings 不可比:46,506.9 是十年累计、18,981.5 是年均;年化后 4.08 倍跳升主要但非全部来自方法变更

- **判决**:CORRECTED(1/3 CORRECTED + 2/3 HOLDS;**取最严格者 CORRECTED**——两席判 HOLDS 的核验依据里同样写出了「不宜说成纯方法效应」「3.9 倍」这一处收紧,只是未升格为修正,无任一席反对该收紧)
- **锁定表述**:
  - 两版底件均为 BLS 官方归档 zip,经 Wayback 原始快照取得后解包内含的 `occupation.xlsx`:`https://www.bls.gov/emp/projections-archive/2014-24.zip`(9,823,242 字节)与 `2016-26.zip`(9,989,732 字节)。三席各自独立下载并逐格核对。
  - **2014–24 版**:Table 1.2 表头逐字为 **"Job openings due to growth and replacements, 2014-24"**(**无 "annual average" 字样,是十年合计**);"Total, all occupations" 行 = 2014 年就业 150,539.9 / 2024 年就业 160,328.8 / 十年变化 9,788.9(+6.5%)/ **openings 46,506.9 千**。
  - **2016–26 版**:表头逐字为 **"Occupational openings, 2016-26 annual average"**;Total 行 = 156,063.8 / 167,582.3 / 11,518.6(+7.4%)/ **openings 18,981.5 千**。
  - **46,506.9 确为十年累计而非年均**,两重独立证据:(a) 同一工作簿 Table 1.10 标题为 "Employment change, replacement needs, and job openings projected 2014-2024",Total 行的 "2014-24 Replacement rate" = 23.5(十年口径百分比)、"Replacement needs" = 35,326.0;(b) 46,506.9 / 150,539.9 = 30.9%,若当年均则等于每年 31% 的开口,与任何口径都不合。
  - 年化与倍数:46,506.9 / 10 = **4,650.69 千/年(约 465 万/年)**;18,981.5 / 4,650.69 = **4.08 倍**(三席分别得 4.081 / 4.081 / 4.082)。**若直接并列 46,506.9 与 18,981.5,会读成 −59% 的「腰斩」,这正是本条要拆穿的错觉。**
  - **BLS 自我判决逐字**(出处必须标 https://www.bls.gov/emp/documentation/replacements.htm,Wayback 20260613002033,页面 Last Modified Date: August 28, 2025):"BLS used a cohort-component method for estimating job openings due to replacement needs from the 1991 through the 2014–24 projections. **This method is no longer in use because BLS identified statistical and conceptual issues with the implementation of this method that compromised the accuracy and validity of the resulting estimates.**"
  - **BLS 另有一句更硬的不可比声明**(separations FAQ):"Published estimates from the 2014–24 projections and prior years **should not be compared** with the 2016–26 projections to estimate how the number of openings has changed over time."
  - **第三重不可比(论断原文未提,第 1、3 席各自挖出,须写进文章)**:**旧法把衰退职业的增长项截断为零**(openings = replacements + max(growth, 0)),**新法不截断**(openings = separations + growth,可为负)。实证:2014–24 表中 Chief executives 变化 = −4.1、replacements = 58.4、openings = 58.4(未扣减);全表 Σ(repl + max(chg,0)) = 46,506.4 ≈ 已公布的 46,506.9,而 Σrepl + Σchg 只有 45,114.9(差额约 1,392 即衰退职业未被扣减的降幅)。**这也意味着 G7 的「分离占比 >100% 即萎缩」判据只在新法下成立。**
  - **归因必须收紧**:两版基期不同(2014 vs 2016)、全职业就业基数不同(150,539.9 → 156,063.8,+3.7%)。**换成占就业比的口径,旧法 3.09%/年、新法 12.16%/年,可归因于方法变更的跳升约 3.9 倍**(三席分别得 3.94 / 3.9 / 3.9)。把 4.08 倍全部归因于方法变更略有高估,幅度约 4%。
  - 第三方对新 separations 法的态度(三席各自检索,结论一致):**未检索到任何针对新方法的公开学术质疑或独立量化评估**;检索到的第三方(Chmura Economics 2018-02-28《Occupational Separations: Components and Applications》、Minnesota DEED《New Separations Methodology》2018、Arkansas / Montana / 华盛顿州 ESD 等州级 LMI)均为**中性描述并独立佐证跳升幅度**。Chmura 逐字:"When the BLS switched from replacement rates to separation rates, it was quite a shock for many of us. On average, these rates measuring this type of labor demand **more than quadrupled**!" 华盛顿州 ESD 自 2017 年起改用本州自定的替代分离法而非直接套用 BLS 分离率,属实务层面的适用性保留。
- **证据分级**:多源证实(两版原始 xlsx 三席各自解包逐格核对;BLS 自陈句三席逐字命中同一页面);「无第三方学术质疑」一项为**多源未获(三席独立检索均无所获)**,写作时应表述为「未检索到」,不得表述为「不存在」
- **数字定版**:
  - **4.08 倍(水平口径)与 3.9 倍(占就业比口径)须并列呈现**,不得只取其一。文章主句用 **「同口径年化后约 4.1 倍」**,紧跟一句 **「其中可归因于方法变更的约 3.9 倍,余下约 4% 来自两版基期就业基数差异(150,539.9 → 156,063.8 千)」**。理由:全篇的论点是「口径变更被当成现实变化」,若自己在归因上不做同样的收紧,等于犯下所批评的错误。
  - **年化值定版为 4,650.69 千/年(约 465 万/年)**,须同时给出未年化的 46,506.9 千并标明「十年累计」。
  - 2016–26 的 18,981.5 千为准;**流传于某 NSF 补充表的 18,742.0 与一手不符,不得使用**(第 3 席点名)。
- **不得这样写**:
  - ❌ 直接并列 46,506.9 与 18,981.5 并称「openings 腰斩 59%」——两者时间口径不同(十年累计 vs 年均),这是本条要拆穿的错觉本身。
  - ❌「方法变更导致 openings 跳升 4.1 倍」不加限定——4.08 倍是两个不同期次、不同就业基数的水平比;纯方法效应约 3.9 倍。
  - ❌ 把 BLS 那段自我判决标注为出自 separations.htm 或 separations FAQ——separations.htm 上同一段前面多一句 "Before then,",separations-faqs.htm 上措辞不同("…BLS identified … and therefore developed the current separations method")。**逐字引用必须标 replacements.htm**。
  - ❌ 把旧法 23.5% 与新法的分离率直接比——旧法 23.5% 是**十年累计替换率**,新法约 11.0% 是**年均分离率**,周期口径不同。
  - ❌ 说两版差异「只是分离/替换算法不同」——增长项的处理也变了(旧法截断负增长,新法不截断),这是第三重不可比。
  - ❌ 写「学界质疑新分离法」——三席各自检索均**未找到**任何针对新方法的独立量化评估或统计学质疑。只能写「至今未见独立评估」,而这本身正是 G-extra 的论点。
- **利益相关**:BLS 既是方法变更的执行者,也是唯一对该变更作出判决的一方;其「旧法有统计与概念缺陷」的自陈同时也是其停用旧法的自我辩护。引用时须标明被评估方=评估方。
- **待 Round 3**:**是**。① 「未检索到对 2016–26 起新 separations/openings 方法的任何独立量化评估」是本文一个承重的**否定性主张**,须由反证搜索席穷尽搜索角度(州级 LMI 技术报告、AEA/JOLE/ILR Review、Urban Institute / Georgetown CEW、GAO 与 DOL OIG 审计)并记录全部未命中角度;② 旧法「截断负增长」的重算(Σ(repl+max(chg,0)) = 46,506.4 vs 已公布 46,506.9)目前只有一席做过全量验证,须第二席复算。

---

## ⚠️ [G-extra] 对 BLS 职业预测的独立系统性量化评估**确实存在**——文献薄、陈旧,但有两项非 BLS 作者的正式评估,且其误差指标是本篇方法学论证的最强证据

- **判决**:**REFUTED(3/3 票 REFUTED,全票推翻)**
- **被推翻的原表述**:「公开文献中基本不存在非 BLS 作者对 BLS 职业预测准确度的系统性量化评估」;「唯一找到的独立学者批评是 Peter Cappelli(NBER WP 20382, 2014)」。**两句都是事实错误**,三席各自独立找到并取得反证一手全文。
- **锁定表述(正面版,比原论断更强)**:
  - **对 BLS 职业预测准确度的独立系统性量化评估是存在的,而且它给出的数字比「没人评估过」这个说法有力得多:BLS 自己承认无法与外部预测对标,但外部学者绕过这一点、改用朴素外推模型作基准完成了评估——结论是大类层面尚可、细类层面失准到几乎无法用于个人专业选择。**
  - **反证一(主力)**:H.O. Stekler(乔治华盛顿大学经济系 research professor)与 Rupin Thomas,**《Evaluating BLS labor force, employment, and occupation projections for 2000》,*Monthly Labor Review*,2005 年 7 月,第 46–56 页**(全文 PDF:`https://www.bls.gov/opub/mlr/2005/07/art5full.pdf`,经 Wayback 原始快照 20260613045502 / 2020id_ 取得,11 页,三席中两席逐字读完全文)。作者栏逐字:"H.O. Stekler is a research professor in—and Rupin Thomas, a graduate of—the Department of Economics, George Washington University."——**两位作者均非 BLS 雇员**,论断自设的「非 BLS 作者」标准已被满足。评估对象为 **BLS 1988 年基年 → 2000 年目标年的职业预测**;方法包括 MAPE、dissimilarity index(结构误差分解)、Spearman 秩相关、预测/实际增长率的五分位转移表(原文 Table 7),并**以两个 naïve share 外推模型作基准**。
  - **反证二**:John H. Bishop 与 Shani Carter(康奈尔大学 New York State School of Industrial and Labor Relations),**《How Accurate Are Recent BLS Occupational Projections?》,*Monthly Labor Review*,1991 年 10 月**(经康奈尔 eCommons DSpace 取到原始 PDF:item `3afb9f5d-9a38-47be-8454-be64c770565f`,handle `https://hdl.handle.net/1813/75634`,bitstream `Bishop45_How_Accurate_Are_Recent.pdf`,7 页,`dc.date.issued=1991-10-01`)。作者栏逐字:"John H. Bishop is associate professor, and Shani Carter is a graduate student, New York State School of Industrial and Labor Relations, Cornell University." 正文自述:"This communication offers an evaluation of the accuracy of the BLS projections of employment growth in the 1980's by major occupational groups. It also considers the accuracy of earlier projections covering the 1960's and 1970's…" **BLS 编者按逐字**:"The Bureau is always receptive to **comment or criticism** of its data or methods in this or any other program. In that spirit, the following communication by John Bishop and Shani Carter comments on the Bureau's 1990 occupational projections."(此编者按本身就是 BLS 承认外部评估存在的一手证据。)其量化结论:BLS 系统性低估高技能职业增长——BLS 预测专业/技术/管理岗占 1988–2000 就业增长的 **44.5%**,该二人估 **70%**,而 1988-03 至 1991-03 的实际为 **87%**。
  - **同二人另有一篇独立文献**(与上文不是同一篇,不可混引):Bishop & Carter,《The Worsening Shortage of College-Graduate Workers》,***Educational Evaluation and Policy Analysis* 13(3), 1991, pp.221–246**,DOI `10.3102/01623737013003221`(经 OpenAlex 核实元数据)。
  - **两文均刊于 MLR(BLS 自家刊物),但作者均为外部学者**——这一点须在文章中主动交代,否则读者会质疑独立性;正确的表述是「BLS 自家刊物刊出的外部学者批评」,这反而使证据更强,不更弱。
  - **BLS 的自陈句(方向正确、可保留,但必须与「无独立评估」拆开)**,逐字:"An important way to evaluate any projection is to compare it against other, similar projections. This is not possible for occupational projections because there are **no comparable projections** which are not in some way derived from BLS projections."(出处 https://www.bls.gov/emp/evaluations/2014-2024-occupational.htm,Wayback 20260613063741;同句亦见 2012-2022、2006-2016、2002-2012 各 vintage 的评估页)。**该句说的是「不存在可与之对比的独立预测(projections)」,不是「不存在独立的评估(evaluations)」——前者成立,后者不成立,写作时必须拆开。** Stekler 独立复述了同一事实:"no other organization made projections of these variables. Consequently, there is no benchmark for judging the BLS forecasts."——**而他恰恰是在那篇仍然完成了评估(改用 naïve 基准)的文章里这么说的**,这个反差本身就是最好的一句论证。
  - **可安全承重的收窄版否定性主张**:「未检索到任何 **2005 年之后**的独立系统性量化评估,也未检索到对 **2016–26 起新 separations/openings 方法**的任何独立评估。」这一版三席均支持,且比原论断更精确、更不易被推翻。
- **数字定版(本条的方法学脊柱,逐个数字的完整口径)**:
  1. **338 个细类职业的 MAPE:未加权 45.2%、加权 15.0%**。出处 Stekler & Thomas, MLR 2005-07, pp.46–56;预测周期为 **BLS 1988 基年 → 2000 目标年**;样本为该次预测中可与实际对照的 **338 个 detailed(disaggregated)occupations**;加权口径为**按就业量加权**,未加权为 338 个职业的简单平均。**加权值(15.0%)远低于未加权值(45.2%),说明大误差集中在小职业**——这一句必须随数字出现,否则 45.2% 会被过度使用。**须补审的口径**:三席均未写明 MAPE 的分母究竟是「实际就业水平」还是「实际增长率」(百分比误差的基数),**该子项列入 Round 3 必审**;在补审前,文章只能写「原文报告的 338 个细类职业 MAPE 为未加权 45.2%、加权 15.0%」,**不得**改写成「BLS 对细类职业的就业预测平均偏离实际 45%」这类指定分母的说法。
  2. **9 个大类(major occupational groups)的 MAPE:未加权 5.86%、加权 5.29%;两个 naïve 外推模型的对应值为 13.8% / 11.8%**。同一篇、同一预测周期。摘要逐字:"in most cases, the accuracy of BLS projections were **comparable to** estimates from naïve extrapolated models"。方向判断在 9 个大类中判对 8 个(农业除外)。**该组数字对 BLS 有利,必须与 45.2% 并列呈现**——只引 45.2% 而不引 5.86% 是选择性引用。口径完整、可直接引用(仅第 1、2 席给出具体数值,第 3 席确认存在该表)。
  3. **「增长最快的 20 个职业」实际只有 6 个真的最快**。出处同为 Stekler & Thomas 对 **1988→2000** 那次预测的评估。**口径不完整**:仅第 1 席给出该数字,第 2、3 席未复核;「最快」的判定基准(按增长率还是增量?「实际最快 20 名」的名单如何界定?)三席均未写明。**该数字暂不可直接引用,列入 Round 3 必审**;若 Round 3 未能补齐口径,文章应改用第 4 项(Spearman)承重。
  4. **预测增速与实际增速的 Spearman 秩相关 = 0.43**。出处 Stekler & Thomas,原文逐字:"the projections for many occupations were clearly inaccurate and explains why the **Spearman rank correlation coefficient is only 0.43**"。相关的两组变量为 **338 个细类职业的预测增长率排序 vs 实际增长率排序**(即与第 1 项同一组 338 个职业,同一 1988→2000 预测周期),**不是 9 个大类那一组**。口径完整,**可直接引用**。配套可引的还有原文 Table 7 的预测/实际增长率五分位转移表。
  5. **Bishop & Carter 的 44.5% / 70% / 87%**:BLS 预测专业·技术·管理岗占 **1988–2000** 就业增长的 44.5%;Bishop & Carter 自估 70%;**1988 年 3 月至 1991 年 3 月**的实际值为 87%。注意最后一个是**三年期的实际值**,不是 1988–2000 全周期的实际值,不可写成「实际是 87%」而不标时间窗。仅第 3 席给出,**单席来源,列入 Round 3 复核**。
  6. **Bishop & Carter 的出处定版**:文章引「BLS 职业预测准确度评估」时,**引 MLR 1991 年 10 月那篇《How Accurate Are Recent BLS Occupational Projections?》**(第 1、3 席一手核到,含 BLS 编者按)。理由:它才是直接针对 BLS 预测准确度的评估,且满足「非 BLS 作者 + 系统性量化」双条件;EEPA 13(3) 那篇题为《The Worsening Shortage of College-Graduate Workers》,主题是学历劳动力短缺,**是另一篇文章,不得与 MLR 那篇混为一谈**(第 2 席只核到 EEPA 那篇,第 3 席指出两篇并存——取第 3 席的拆分)。
- **证据分级**:
  - 两项独立评估**存在**这一事实:**多源证实**(三席各自独立取到一手全文或原始 PDF;Stekler & Thomas 三席均取到全文,Bishop & Carter 第 1 席取到康奈尔 eCommons 原始 PDF、第 2 席经 OpenAlex 核到 EEPA 篇元数据、第 3 席经 Gale + eCommons 双路确认)。
  - 45.2% / 15.0% / 5.86% / 5.29% / 13.8% / 11.8% / 0.43:**单源已核**(单一论文,但一手 PDF 可回溯,三席中至少两席逐字读到)。
  - 「20 个里只有 6 个」与「44.5%/70%/87%」:**单席已核,待复核**。
  - Cappelli 已发表版是否保留该句:**未验证(UNVERIFIABLE)**,见下。
- **不得这样写**:
  - ❌「公开文献中基本不存在非 BLS 作者对 BLS 职业预测准确度的系统性量化评估」——**事实错误,3/3 席推翻**。至少有 Stekler & Thomas(2005)与 Bishop & Carter(1991)两项,均带正式误差指标与朴素模型基准,且全文可得。
  - ❌「唯一找到的独立学者批评是 Peter Cappelli」——同上,事实错误。
  - ❌ **把 Cappelli 那句当成「独立学者对 BLS 职业预测的批评」——这是移花接木,三席全部点名。** 原句逐字:"**Governments** do not have a particularly good record of forecasting where jobs will be years in advance, however, and students and their families would bear the costs when those forecasts are wrong."(NBER Working Paper 20382, August 2014,手稿第 49 页 / PDF 第 51 页,`https://www.nber.org/system/files/working_papers/w20382/w20382.pdf`,1,097,634 字节,67 页,两席逐字核对一字不差)。该句出现在**讨论佛罗里达州按雇主意愿调拨专业经费**的段落里,**主语是 "Governments" 泛指,上下文全文未点名也未引用 BLS Employment Projections**。
    - **改写后的正确射程(可直接用)**:「Cappelli 对**政府主导的「专业—岗位对口」式人力规划**提出过一般性批评:政府在提前数年预测岗位去向上纪录不佳,而预测出错的代价由学生和他们的家庭承担。」——**只能射向「政府的人力预测与据此调拨专业经费」这一类做法,不能射向 BLS EP 这一具体产品**。
  - ❌ 引 Cappelli 时标已发表版页码——已发表版为 Peter Cappelli, "Skill Gaps, Skill Shortages, and Skill Mismatches: Evidence and Arguments for the United States", *ILR Review* 68(2), March 2015, pp.251–290, DOI `10.1177/0019793914564961`,**封闭获取**。三席穷尽路径均未取到正文:SAGE 全文与 PDF 返 403;OpenAlex 显示 `is_oa=false`、`oa_status='closed'`、`any_repository_has_fulltext=false`、无 `pdf_url`;ResearchGate / PhilArchive 403;Wharton 站点该 PDF 404;Semantic Scholar 上的候选 PDF 实为**同题演讲幻灯片(26 页)**而非期刊正文;CRS R47059 只引书目不引该句。工作论文版(60 余页)到发表版(40 页)存在实质删减的可能。**该句只能引 NBER WP 20382(2014 年 8 月),并明确标注「工作论文版」。**
  - ❌ 把 BLS 那句 "no comparable projections" 当作「没有人评估过 BLS」的证据——它说的是**没有可对标的独立预测**,不是没有独立评估。Stekler 正是在承认前者的同一篇文章里、改用 naïve 基准完成了后者。两件事必须拆开。
  - ❌ 只引 338 个细类的 45.2% 而不引 9 个大类的 5.86%(及其 naïve 基准 13.8%)——那是选择性引用,且与本篇批评「选择性引用」的立场自相矛盾。**正确的一句话概括是:BLS 在大类层面的预测精度与朴素外推模型相当甚至更好,但在个人真正要选的那一级——细类职业——误差大到排序几乎失效(Spearman 0.43)。**
  - ❌ 说「BLS 从未被外部审计」「BLS 拒绝外部评估」——BLS 自家刊物 MLR 主动刊出了这两篇外部批评,并配了「always receptive to comment or criticism」的编者按。
- **利益相关**:
  - **两篇反证评估均刊于 MLR,即 BLS 自家刊物**——发表渠道受被评估方控制,须随引用标注;但作者机构(乔治华盛顿大学、康奈尔 ILR)独立,BLS 编者按亦明确将其定位为对本局方法的 comment/criticism。
  - **BLS 是被评估方本身**,其「不存在可比预测」的自陈同时也是其免于外部对标的理由。引用该句时宜配上 Stekler 的独立同向表述,不要单独使用。
  - Cappelli 版本问题不涉及利益相关,纯属付费墙可及性。
- **待 Round 3**:**是,本批优先级最高**。
  1. **反证搜索席**:确认「2005 年之后无独立系统性量化评估」这一否定性主张,记录全部搜索角度(International Journal of Forecasting、Journal of Forecasting、AEA 系列、ILR Review、Industrial Relations、州级 LMI 技术报告、GAO/DOL OIG 审计报告、Georgetown CEW、Urban Institute),包括未命中的角度。
  2. **方法学审计席**:回到 Stekler & Thomas 原文,**补齐 MAPE 的分母定义**(相对实际就业水平还是相对实际增长率)、**核实「20 个里只有 6 个」的判定基准与名单**、确认 Spearman 0.43 的样本确为那 338 个细类职业;并评估「以 naïve share 模型为基准」这一设计是否足以支撑「BLS 大类预测尚可」的结论。**「20 个里只有 6 个」在补齐口径前不得承重。**
  3. 复核 Bishop & Carter 的 44.5% / 70% / 87% 三个数字(单席来源),并确认 MLR 1991-10 篇与 EEPA 13(3) 篇确为两篇不同文章。

---

## [G10] 纽约联储分专业表 2024 ACS 版:数字与排名全对,但三处口径来源与限定语必须改写

- **判决**:CORRECTED(1 席 CORRECTED / 2 席 HOLDS;取最严格的 CORRECTED 席——两席 HOLDS 也在「不影响判决的补充」里独立记下了同样的 O*NET 归属与名义美元问题,三席实质同向)
- **锁定表述**:
  - 据纽约联储 *The Labor Market for Recent College Graduates* 交互页「Outcomes by Major」标签(**2026-02-04 发布,数据年为 2024 年 ACS**;来源行逐字为 "Source: U.S. Census Bureau, American Community Survey (IPUMS)."):CSV 共 75 行 = 1 表头 + **73 个专业 + 1 行 Overall**(Overall 不参与排名计算)。
  - **人群口径必须分两套写**:失业率与低就业率为 **22–27 岁、持学士及以上学位**(含硕博)的近期毕业生;**中位工资为「仅持学士学位」的全职工作者**;early career 22–27 岁,mid-career 35–45 岁;**全部数字排除在校生**(notes 逐字:"All figures exclude those currently enrolled in school.")。把「学士及以上」当整表统一口径是错的。
  - 关键格值(失业率 / 低就业率 / 早期中位薪 / 中期中位薪,三席各自独立下载同一 CSV 逐格一致):Computer Engineering 7.783 / 15.835 / $90,000 / $131,000;Computer Science 6.992 / 19.127 / $87,000 / $120,000;Nursing 2.147 / 12.781 / $70,000 / $87,000;Elementary Education 1.18 / 16.213 / $45,000 / $55,000;Biology 4.292 / 51.13 / $45,000 / $83,000;Psychology 4.985 / 48.291 / $45,000 / $72,000;Fine Arts 7.655 / 58.87 / $45,000 / $72,000;Economics 3.524 / 33.094 / $72,000 / $115,000;Finance 2.758 / 27.758 / $70,000 / $112,000;Overall 4.211 / 39.35 / $58,000 / $87,000。
  - 排名(73 个专业、剔除 Overall,三席复算一致):CS 失业率**倒数第 4 高**(高于它的仅 Anthropology 7.922、Computer Engineering 7.783、Fine Arts 7.655);CS 低就业率**第 9 低**;CS 早期中位薪**第 2 高**(仅次于 CE $90,000);Nursing 低就业率 12.781 为**全表最低(1/73)**。
  - **低就业率的分母是「在业」毕业生,失业者不在分母内**。此点站上未写明,须引方法论原文:Abel & Deitz, "Underemployment in the Early Careers of College Graduates over the Business Cycle," NBER WP 22654 / NY Fed Staff Report 749, p.6:"We measure the underemployment rate as the share of **employed** college graduates working in jobs that do not require a college degree."(另 Abel, Deitz & Su, "Are Recent College Graduates Finding Good Jobs?," *Current Issues in Economics and Finance* 20(1), 2014 同义:"We calculate the underemployment rate as the number of graduates underemployed divided by total graduates employed.")
  - 分专业表的 $ 数为**当年名义美元**:Outcomes by Major 的 notes **没有任何 constant-dollar 声明**,而同一交互的 Wages 标签页明写 "Annual wages are expressed in constant 2025 dollars"。故该列不可跨版本直接相减。
- **证据分级**:多源证实(三席各自直连下载 CSV 与 college-labor-chart-meta.json 逐格核对,数值与 notes 逐字一致;分母口径二席各自回到 NY Fed 一手方法论 PDF)
- **数字定版**:低就业判定阈值有两版——网站写 "50 percent or more",NY Fed 自定方法论(NBER WP 22654 / SR 749, p.6)写 "**more than 50 percent** of the respondents working in that occupation indicated that at least a bachelor's degree was necessary"。边界(恰好 50%)两处相反。**文章以网站版「50% 或以上」为准,并在括号内注明方法论原文为「超过 50%」**,理由:锁定的数据表是网站产出物,应用网站自述口径,但差异必须披露。
- **不得这样写**:
  - ❌「该(分专业)表注明其低就业判定依据 O*NET」——Outcomes by Major 标签的 notes **根本没有定义 underemployment**,其 source 行只写 ACS(IPUMS),**不提 O*NET**。"50 percent or more" 那句逐字出现在 **Underemployment 标签页**的 notes(source 行为 "Current Population Survey (IPUMS); U.S. Department of Labor, O*NET")。O*NET 适用于分专业表这一点只能靠页面 FAQ 搭桥("This analysis uses survey data from the U.S. Department of Labor's Occupational Information Network (O*NET) Education and Training Questionnaire…"),须写成「据该页 FAQ」。
  - ❌ 把分专业表的中位薪当作可比不变价、或与 Wages 标签页的数直接并列——分专业表是名义美元。反证:分专业表 Overall 早期中位薪 2022 年为 $50,000(若折 2025 年美元约 $55,000),而 CPS 口径 Wages 表 2022 年不变价中位数为 $57,216。
  - ❌ 把「仅学士」这个限定挂在失业率或低就业率上,或把「学士及以上」挂在工资列上——两列人群不同。这个错配在 Biology 上尤其致命:Biology 的研究生学位持有比例为 **63.98%**,即 $45,000 的早期中位薪只描述那约 36% 止步于学士的人,而 4.292% 的失业率覆盖全部学位层级。
  - ❌ 写「73 个专业」时把 Overall 也算进排名分母——CSV 有 74 行数据,Overall 是所有学士及以上毕业生的合并值,不是第 74 个专业。
  - ❌ 不标数据年份与更新状态(见 G12「不得这样写」末条的停更公告)。
- **利益相关**:无(联邦储备银行的公共数据产品)
- **待 Round 3**:否(三席独立下载同一份一手 CSV 并各自复算排名,结果完全一致,属多源证实)

---

## [G11] CS 四版时序(2021→2024 ACS):数字全对,但「同期」「不同向」「涨 11.5%」三处口径不成立

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - 四个版本逐格核实(发布日 / 数据年由各版 college-labor-chart-meta.json 的 releaseDateInfo 与 notes 一一确证,快照为 Wayback `id_` 原始字节):
    - **2023-02-10 发布 / 2021 ACS**:CS 4.8 / 19.1 / $73,000;CE 3.7;Overall 5.1(该版原始文件只保留 1 位小数)
    - **2024-02-22 发布 / 2022 ACS**:CS 4.267 / 16.654 / $78,000;CE 2.311;Overall 3.557
    - **2025-02-20 发布 / 2023 ACS**:CS 6.056 / 16.456 / $80,000;CE 7.538;Overall 3.640
    - **2026-02-04 发布 / 2024 ACS**:CS 6.992 / 19.127 / $87,000;CE 7.783;Overall 4.211
  - 四版 notes 的人群定义(ACS、22–27 岁、学士及以上、排除在校生;工资列为仅学士全职)逐字一致,**时序可比性成立**。CS 失业率两年 +2.725pp(6.992 − 4.267),写作「+2.7pp」正确。
  - **CS 早期中位薪:$78,000(2022)→ $80,000(2023)→ $87,000(2024),两年累计名义 +11.5%,未做通胀调整**;扣除 CPI-U 年均值 292.655(2022)→313.689(2024)的 +7.19% 后,**实际购买力涨幅约 +4%**。
  - **同期 Overall 早期中位薪 $50,000 → $58,000,名义 +16.0%——即 CS 起薪涨幅低于全体毕业生**。此对照必须与 +11.5% 同时出现。
  - **CS 低就业率不是「持续下降」**:2022→2023 为 16.654→16.456,仅 −0.198pp,远小于该表跨版本变动的中位绝对值 1.25pp,属噪声级;真正的转折在 2023→2024(16.456→19.127,+2.67pp)。且 **2021 版即为 19.1%——2024 年的 19.127% 不是新高,而是回到 2021 年水平,中间的 16.7%/16.5% 才是低谷**。
  - 可承重的合并表述:「若统一用 2022→2024 窗口,CS 的失业率与低就业率**同向恶化**,唯一逆向的是名义起薪;而名义起薪的涨幅还低于全体毕业生。」
- **证据分级**:多源证实(三席各自用 Wayback `id_` 快照取回同四版 CSV 并解压逐格比对,20 个格值全部一致;2026 版与 2026-07-24 直连线上文件本地 diff 为逐字节相同)
- **数字定版**:起薪涨幅 **+11.5%(名义)与约 +4%(实际)须并列呈现**,并明写「名义」二字。理由:分专业表无 constant-dollar 声明,+11.5% 与 +4.0% 对准大学生是两个量级的信号,取任一单值都会误导;CPI-U 折算为文章自算,须注明算法(BLS 序列 CUUR0000SA0 年均值)。
- **不得这样写**:
  - ❌「起薪**同期**从 $78k 涨到 $87k」——紧邻句讲的是 2022→2023,而 $78k→$87k 跨的是 2022→2024 两个数据年;2022→2023 起薪只从 $78,000 到 $80,000(+2.6%)。「同期」在此为时间窗混用。
  - ❌ 只给 +11.5% 不给 Overall 的 +16.0%——会让读者得出与数据相反的推论(以为 CS 起薪跑赢大盘)。
  - ❌「低就业率 2022→2023 **还在下降**」——−0.198pp 实质持平,不足以支撑带方向性的措辞。
  - ❌「三个指标不同向」被当作 2022→2024 的整体描述——只有混用不同时间窗才成立。
  - ❌ 只呈现 2022→2024 的低就业率上升而不提 2021 版的 19.1%——会让读者误以为在恶化到史无前例,实际是「先降后回」。
  - ❌ 对 2021 年(2023-02-10 版)那一行做 0.1pp 以下的精细比较——该版只有 1 位小数,存在 ±0.05pp 取整误差。
- **利益相关**:无(联邦储备银行公共数据 + BLS CPI)
- **待 Round 3**:否(四版一手快照三席均取得,数字交叉一致)

---

## [G12] CNBC 病毒式报道的传播链:数字全中,但标题版本、更正声明与「口径事故」的指控范围须改写

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - 报道:Jessica Dickler, CNBC,**首发 2025-05-16,更新 2025-06-05**。**存在两个标题**:页面 JSON-LD / og:title / h1 仍为《College majors with the best and worst job prospects — art history beats finance》(首发版,授权转载页保留),而更新后 CNBC 现行正文标题与 URL slug 为《College majors with the best and worst **employment** prospects — **philosophy now outranks finance**》。引用时必须写明「2025-06-05 更正版」并指出用的是哪一版标题,否则读者按标题搜不到。
  - **该文文末带更正声明,逐字:"Correction: This story has been updated to correct the data in a chart."** 即首发版图表数据是错的、事后被订正;而「病毒式传播」传的恰恰主要是那张图。
  - 文中数字与 **2025-02-20 发布 / 2023 ACS 版** CSV 逐个吻合(**仅对现行订正后正文成立,不可推及首发版图表**):CS 6.1%↔6.056、CE 7.5%↔7.538、art history 3%↔3.047、nutritional sciences 0.4%↔0.441(NY Fed 标签为 "Nutrition Sciences")、philosophy 3.2%↔3.180、finance 3.7%↔3.704、nursing 1.4%↔1.422、"median wages of $80,000"↔$80,000。
  - **口径事故的准确描述**:CNBC **明确写了**分专业数据的来源与年份——"The New York Fed's report was based on Census data from 2023"。未标注口径的是同版面那句 5.8%:原文只写 "the unemployment rate for recent college grads rose to 5.8% in March, up from 4.6% the same time a year ago, according to the Federal Reserve Bank of New York",**未说明它来自 CPS 月度序列、经季节调整 + 三月移动平均、参照期为 2025 年 3 月单月、且是全专业合计**。事故在于「两套调查并排而只有一套被标注」,不在于「未标年份」。
  - 两套口径确实不可并排:同为 2023 日历年,CPS 应届生失业率 12 个月均值为 4.377%,而 2023 ACS 的 Overall 只有 3.640%,相差 0.74pp。
  - **该 5.8% 与其同比基数 4.6% 都被回溯修订过**(CPS 序列做季调 + 三月移动平均,会随后续数据改写历史值):
    - 报道当时版(Wayback 20250501074651 / 20250602232905):2025-03 = **5.802**、2024-03 = **4.600**
    - 2025-08 存档版:5.710 / 4.542(另 2025-12 存档 5.720、2026-03 存档 5.724)
    - 现行版(meta releaseDateInfo "May 5, 2026, with 2026:Q1 data",2026-07-24 直连):**5.672 / 4.521**
    - 即那句话的**两个数字如今都不再成立**;同比升幅由 +1.2pp 变为 +1.15pp。
  - **时效**:6.056(2023 ACS)已被 6.992(2024 ACS,2026-02-04 发布)取代,CE 7.5%→7.783% 同理。**准确说法是「落后一个发布周期 / 一个数据年,描述的是 2023 年的劳动力市场」**。此外「CS 与 CE 起薪 $80,000、赚得最多」这句在 2023 ACS 版里其实是与 Chemical Engineering **三方并列** $80,000,到 2024 ACS 版已变为 CS $87,000 / CE $90,000——该句双重过期。
- **证据分级**:多源证实(三席均因 CNBC 直连 403 改用 NBC 授权转载版逐字读取,标题/署名/日期/更正声明一致;CPS 修订链三席分别用 Wayback CDX 列举快照后逐版取值,三个修订值全部命中)
- **数字定版**:**5.8% / 4.6% 与 5.672% / 4.521% 须并列呈现**,写作「CNBC 引用时的现行值为 5.8% vs 4.6%,截至 2026-07 的现行值已修订为 5.672% vs 4.521%」。理由:本条的论点正是「被引数字会被回溯修订」,只写任一端都会消掉论点本身。**「已过期两年」定版改为「落后一个发布周期(2023 数据年 → 2024 数据年)」**,理由:6.056 只被替换过一次,写「两年」是把数据年差与发布年差混算,夸大一个周期。
- **不得这样写**:
  - ❌「CNBC 未交代分专业数据的来源/年份」——它写了 "based on Census data from 2023"。指控写过头会被整句反驳。
  - ❌「CNBC 引用的数字逐个回对 2025-02-20 版 CSV 完全吻合」而不提更正声明——吻合的是**订正后正文**,传播最广的那张图是被订正掉的那版。
  - ❌ 只追 5.8% 的修订而不提 4.6% 也被改过——同一句的两端都已失效。
  - ❌ 用《…art history beats finance》做标题却不说明它是首发/转载版旧标题。
  - ❌ 引用 2025-10 之后的 CPS 月度值而不加数据质量警示——NY Fed 该页 2025-10-31 挂出停更公告("Due to the suspension of necessary data, The Labor Market for Recent College Graduates has not been updated as scheduled."),现行 Unemployment 注释写明 "October 2025 results are estimated due to missing data"。
- **利益相关**:CNBC 为商业媒体,该报道属流量型二手转述;NY Fed 数据本身无商业利益。
- **待 Round 3**:否(报道原文、四版 CPS 序列快照、分专业 CSV 三席均取得并逐格核对)

---

## [G13] EIG 的置信区间反驳:引语必须补回限定词,「稳定复现」的噪声论证不能只用一边

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - **引语必须逐字完整**(Connor O'Brien, "A viral chart on recent graduate unemployment is misleading," Economic Innovation Group / *Agglomerations*, 2025-08-13,datePublished 元数据 2025-08-13T10:30:58+00:00):"**In most cases,** the confidence intervals around these estimates of recent grad unemployment are so large that it makes no sense to use them to make firm conclusions about the returns to particular majors, **let alone use them to make policy decisions.**" 删去句首 "In most cases," 会把作者的「多数情况下」升格为全称判断,恰恰犯了作者批评的毛病;尾部截断须用省略号标出。
  - 区间三组逐字:CE "somewhere between four percent and 11 percent";physics "somewhere between two percent and 12 percent";public policy "from zero percent to 13 percent"。方法为 "Using special weights provided by the ACS"(重复权重)。
  - **EPOP 90% 不是 NY Fed 的 Computer Science 行**:EIG 为扩大样本改用 ACS 更粗的 "computer and information sciences" 大类(**该类下辖六个专业**),原句 "A full 90 percent of 22- to 27-year-olds who majored in those fields were employed in 2023",且作者自注该值 "**down more than one percent from 2022**"。两者不同口径,不可并排。
  - **时效边界(必须标注)**:该文发于 2025-08-13,可用数据只到 2023 ACS(作者原文:"the American Community Survey, which only extends through 2023");作者自陈 "Given the surge in layoffs from Big Tech firms in 2023 and 2024, it is likely that the job prospects for young graduates of computer and information science programs have worsened since the last ACS"。2026-02-04 发布的 2024 ACS 已把 CS 抬到 6.992%、CE 抬到 7.783%。故结尾那句 "Still, news of the much-anticipated implosion of the computer science graduate job market is greatly exaggerated, **at least for now**" 的 "for now" **已到期**,不能当作 2026 年的现成反驳。
  - **跨版本波动复算(2023 ACS → 2024 ACS,73 专业同名可配对,无缺失;三席各自 Python 复算一致)**:失业率变化的**中位绝对值 = 1.2520pp**;**|Δ| > 2pp 者恰为 20 个**(无恰好等于 2 的边界案例)。按 |Δ| 降序前 12 名逐格吻合:Early Childhood Education 1.298→6.593(+5.295)、Performing Arts 2.718→6.950(+4.232)、Nutrition Sciences 0.441→4.536(+4.095)、Environmental Studies 2.582→6.307(+3.725)、Art History 3.047→6.688(+3.641)、Medical Technicians 2.823→6.236(+3.413)、Public Policy and Law 5.513→2.237(−3.276)、Mechanical Engineering 1.529→4.364(+2.835)、Chemical Engineering 2.024→4.711(+2.687)、Business Analytics 2.392→5.034(+2.642)、Architecture 4.284→6.844(+2.560)、Foreign Language 4.040→1.579(−2.461);对照 CS +0.936pp、CE +0.245pp。
  - **「CS/CE 高失业率稳定复现」必须降级为**:「CS/CE 的当前高位只由**两次连续读数**支撑(CS 6.056→6.992、CE 7.538→7.783),且 **CE 这个高位本身诞生于一次单年跳变:2022 ACS 2.311% → 2023 ACS 7.538%,+5.23pp,是 2022→2023 全表第二大跳变**(仅次于 Aerospace Engineering 7.771→1.397,−6.37pp);CS 同期也跳了 4.267→6.056(+1.79pp),是那一年中位绝对变化 0.853pp 的两倍多。CE 四版时序为 3.7(2021)→ 2.311(2022)→ 7.538(2023)→ 7.783(2024)。且 EIG 给 CE 的 95% CI 为 4%–11%,7.538 与 7.783 同处一个区间内,『复现』在统计上不提供额外信息。」可承重的表述上限:**「CS/CE 连续两年读数偏高,但在样本噪声量级下尚不足以称为稳定趋势。」**
  - **「NY Fed 未公布样本量/标准误」须改为有界表述**:「NY Fed 在该表的公开发布渠道中均未提供样本量、标准误或置信区间——四份数据 CSV 无 N/SE 列(分专业表仅 6 列)、交互页 notes 与 FAQ 全文(14 问)grep 'sample size / standard error / margin of error / confidence interval' 零命中、可下载的 College-labor-data_historical.xlsx 全部 sharedStrings 无样本量字样;FAQ 指定的两篇方法论文献(NBER WP 22654 / Staff Report 749;*Current Issues* 20(1))亦未公布该网页表的专业级样本量。」
  - 补一条更硬的正面证据:NY Fed 自己的方法论原文做分专业分析时用的是 **13 个宽口径专业 + 2009–11 三年合并 ACS**("We classify recent college graduates as belonging to one of thirteen different undergraduate majors… for the 2009-11 period");网页版扩到 **73 个细分专业 + 单年 ACS**,这一扩展**从未配套发布过任何样本量、标准误或方法论说明**。
- **证据分级**:单源已核(EIG 的置信区间本身是**唯一**给该表做区间估计的来源,一手可回溯、三席各自抓取原文逐字一致,但无第二支独立团队复算);跨版本跳变复算部分为**多源证实**(三席各自下载两版 CSV 独立复算,中位值、计数与前 12 名清单全部一致)。
- **数字定版**:EPOP **90% 只能标为「ACS 'computer and information sciences' 大类(下辖六个专业)、2023 年、22–27 岁」**,不得写成 Computer Science 专业的数字,也不得与 NY Fed 表中 CS 的 6.992% 做算术互补(1 − 0.90 ≠ 失业率:EPOP 的分母是全体该专业毕业生而非劳动力)。中位绝对变化 **1.25pp 定版为 1.2520pp**(2023→2024 档);另需与 2022→2023 档的 **0.853pp** 区分,不得混用。
- **不得这样写**:
  - ❌ 引 "the confidence intervals…" 而删去句首 "In most cases," 与句尾 "let alone use them to make policy decisions."——把不确定性论证反过来说死。
  - ❌ 把 EIG 的 EPOP 90% 说成「NY Fed 表里 Computer Science 专业的就业率」——不同口径。
  - ❌ 拿 "greatly exaggerated, at least for now" 当 2026 年的现成反驳——其结论止于 2023 ACS,作者本人已预告会变差。
  - ❌「CS/CE 的高失业率**稳定复现**,而艺术史/营养学一年就翻车」——噪声论证只用在一边。CE 的高位正是同一种单年跳变的产物,只稳了两年;这与本条自己论证的「单年 ACS 噪声极大」自相矛盾。
  - ❌「NY Fed **从未**公布样本量或标准误」——无界否定命题,改用上面的有界渠道枚举写法。
- **利益相关**:**有,须随数字披露**。Economic Innovation Group 是华盛顿的政策倡导型机构(非中立统计机构),2015 年由 Sean Parker 与 John Lettieri、Steve Glickman 创办,启动资金约 1,500 万美元,出资方为科技投资人(Sean Parker、Ron Conway),长期主张扩大高技能移民 / H-1B;该文开篇即把争议框定为涉及 "the future of STEM education, the effects of AI on labor markets, and even high-skilled immigration"。「CS 就业市场没有崩塌」这一结论方向与其资助方与政策立场同向。作者 Connor O'Brien 为其研究人员。**这不否定其统计工作**(CI 复算方法本身正当,且有公开 GitHub 仓库可查),但引用时必须披露。
- **待 Round 3**:**是**。① EIG 的置信区间是本条唯一支撑「分专业失业率不可承重」的区间估计,属**单源承重实证 + 利益相关方**,需方法学审计席复核其重复权重(replicate weights)实现与区间宽度是否可复现,并评估其倡导立场对结论选择的影响;② 「NY Fed 未公布样本量/标准误」是否定命题,需反证搜索席检索是否存在未被三席覆盖的渠道(如 Liberty Street Economics 博文、NY Fed 研究简报、作者会议 slides、对媒体的书面回复)公布过该表的分专业 N 或 SE;③ 需检索是否有独立团队(非 EIG)用 ACS 微观数据对同一批专业做过区间估计,以把本条从单源已核升级。

---

## ⚠️ [G14] CEW《The Major Payoff》:CS 应届失业率 7.2% 成立,但对比基准、收入区间、失业率区间三处数字全错,且它与 NY Fed 不是独立测量

- **判决**:CORRECTED(3/3 票 CORRECTED;其中第 1 席对「应届失业率区间 1.3%–11%」这一子项单独判 REFUTED,故加 ⚠️)
- **锁定表述**:
  - 据乔治城大学教育与劳动力中心(Georgetown University Center on Education and the Workforce, CEW)《The Major Payoff: The Value of a Bachelor's Degree by Major》(Catherine Morris、Ban Cheah、Jeff Strohl,2025-10-15 发布,共 74 页,p.37):「unemployment among recent graduates with a bachelor's degree in computer science is **7.2 percent**, up from a low of **5.3 percent in 2014**」。脚注 66 说明两个窗口分别是 **ACS 2013–15 合并**与 **ACS 2021–23 合并**;CEW 的年份标签是三年合并的中点(方法论附录:「The unemployment rate for each year represents a pooled three-year average」,即「2022」=2021–23 合并、「2014」=2013–15 合并),**引用时不得当作单年**。
  - 「recent college graduates」= **22–26 岁**(NY Fed 同类指标为 22–27 岁,两者不可混用);「prime-age」= **25–54 岁**。
  - **computers, statistics, and mathematics 应届失业率 6.8%**,口径是 CEW 的 **detailed field(16 个之一)**,隶属 STEM broad field(8 个 broad field 之一),**不是「大类」,也不等于 CIP 11**。该 detailed field 下辖 computer science、computer engineering、computer and information systems、information sciences、applied mathematics、mathematics、statistics and decision science(报告 Table 3 列出 7 个专业;CEW 官方数据工具另含一个 other,合 8 个)。**computer engineering 单列在这个 detailed field 之内**,即 6.8% 已包含计算机工程。
  - 「6.8% 为 **STEM 内最高**」成立(Figure 13);但全部 16 个 detailed field 的应届失业率最高者是 **arts 8.9%**,最低是 **education 2.8%**。写「最高」必须带「STEM 内」限定。
  - **应届收入区间**(Figure 5/6,口径:ACS **2009–23 十五年合并**、**全职全年(full-time, full-year)**、**仅持学士学位(排除同时持研究生学位者)**、2024 年美元):最低 **$37,000(zoology)**,次低 counseling psychology $38,000、communication disorders sciences and services $39,000;最高 **$98,000(petroleum engineering)**,其后 chemical engineering $86,000、computer engineering $86,000、actuarial science $85,000、electrical engineering $84,000、**computer science $83,000(排第 6,不是第 1)**。
  - **$79,000(中位)/ $107,000(75 分位)**数值无误,但脚注 64 显示其为 ACS **2021–23 合并**,而报告绝大多数收入数字用 2009–23 合并 —— 同一报告内收入口径不统一,逐条标注方可引用。
  - **prime-age 溢价**:仅持学士的 25–54 岁全职全年劳动者中位收入 **$81,000**,较仅高中学历者高 **70%**(ACS 2009–23 合并、2024 年美元,脚注 7);若含同时持研究生学位者则为 **$88,000**(脚注 5)。对应失业率 **2.9% vs 6.2%** 是另一口径:ACS **2021–23 合并**、25–54 岁、劳动力口径(excludes those who are not in the labor force)、**不限全职**。收入与失业率不是同一时间窗,并列陈述必须分别标注。
  - **专业数**:方法论附录逐字「a total of **152 majors for prime-age workers and 142 majors for recent college graduates**」。凡应届口径的表述一律写 142。
  - **供给侧 159%**:Appendix Table C1(IPEDS Completions,学士层级),computers, statistics, and mathematics 由 2009 年 **53,499** 增至 2023 年 **138,755**,+159%,为 16 个 detailed field 中最快(次为 healthcare 109%)。**该系列用的是 CEW 自建专业分类,口径宽于 NCES CIP 11,与 G15 的表 325.35 序列不可互换、不可拼接。**
  - **关键定性(三席一致要求改写)**:CEW 与纽约联储用的是**同一套底层微观数据 —— Census Bureau American Community Survey(ACS)**。二者只是不同年龄窗、不同池化策略的切法差异,**不构成独立测量**。文章只能写成「同一数据源的不同切法给出同向结果,降低了单年抽样噪声的可能性」,**不得**写成「两个独立机构互证」。
- **证据分级**:单源已核(三席均取得同一份正文 PDF 并逐页核对;与 NY Fed 的关系为同源切片,不构成多源证实)
- **数字定版**:
  - **失业率起点:用 5.3%(2013–15 合并),涨幅写 +1.9pp,并必须同时披露 CEW 自身的内部冲突。** 理由:第 3 席查明 4.3% 来自 CEW 博客(「7.2 percent in 2021–23, up from 4.3 percent in 2013–15」),而报告正文 p.37 白纸黑字是 5.3%——**同一机构两份出版物对同一统计量给出互相矛盾的两个数**。定版取经同行编辑的报告正文,但因起点值存在机构内部冲突,该起点**不承重**:文章若要讲「翻倍恶化」的涨幅叙事,必须括注冲突;更稳妥的写法是只用 7.2% 的水平值,不用涨幅。用 4.3% 会把恶化幅度从 1.9pp 夸大到 2.9pp(近 50% 放大)。
  - **应届收入区间:$37,000(zoology)–$98,000(petroleum engineering),CS 为 $83,000。** 理由:三席均自报告 Figure 5/6 逐行核到;原稿的 $34,000–$86,000 出自 CEW 博客/在线工具,全文检索「$34,000」在报告正文零命中。
  - **应届失业率区间:只能写 2.8%(education)–8.9%(arts),16 个 detailed field。** 理由:CEW 不发布专业层级失业率(见下)。
- **不得这样写**:
  - ❌「CS 应届失业率 7.2%,对比 2013–15 的 **4.3%**」——报告正文是 5.3%;4.3% 只见于 CEW 博客,且第 1 席指出 4.3% 实为 2022 年 multi/interdisciplinary studies 的应届失业率(Figure 13),存在张冠李戴风险。
  - ❌⚠️「应届失业率区间 **1.3%(operations logistics and e-commerce)至 11%(film, video, and photographic arts)**」——第 1 席判 REFUTED,第 2、3 席同向。**CEW 根本不发布专业层级失业率**:脚注 8 逐字「Our analysis of the unemployment rate among bachelor's degree holders is aggregated at the **detailed field level** due to small sample sizes within some majors.」;官方失业率数据工具底层 JSON 字段只有 field / detailed_field,**无 major 字段**。这两个数只出现在 CEW 博客,与报告自陈的方法论直接抵触,且极可能是从 NY Fed 分专业表串味而来。**整条删除**;若坚持引用,必须写明「出自 CEW 博客/在线工具,与其报告方法论相抵触」。
  - ❌「应届收入区间 $34,000(communication disorders)至 **$86,000(computer science)**」——四个要素全错:最低是 zoology $37,000、communication disorders 是 $39,000、最高是 petroleum engineering $98,000、$86,000 属于 computer engineering 与 chemical engineering。把 $86,000 说成「computer science 且为区间上限」是双重错误。
  - ❌ 把「2021–23 三年窗口」套到收入数字上——失业率是 2021–23 合并(8 处),收入绝大多数是 2009–23 十五年合并(19 处)。
  - ❌ 引用任何收入数字而不写「**全职全年、仅持学士**」——报告作者 Ban Cheah 自己的引语已承认限定(「among those who do manage to land a job」);省略会实质性高估典型结果。
  - ❌ 称 computers/statistics/mathematics 为「**大类**」或等同 CIP 11——它是 16 个 detailed field 之一,与 NCES CIP 11 不是同一个东西;G14 的 159% 与 G15 的 CIP 11 序列**不得拼接或互相印证**。
  - ❌ 把 Table 3 中 computer engineering 旁的「**13%**」读成失业率——那是该专业占本 detailed field 应届人数的**份额**(computer science 42%、mathematics 14%)。
  - ❌ 写「**CEW 与 NY Fed 两个独立来源互证,削弱了样本噪声解释**」——同一份 ACS,不是独立测量;它能排除某一种切法的偶然,不能排除 ACS 自身的抽样与自报专业编码误差。
  - ❌「152 个专业」用于应届口径——应届只有 142 个。
- **利益相关**:**须标注**。CEW 是乔治城大学 McCourt 公共政策学院下属的研究与政策机构,立场明确亲学位(正文「the evidence overwhelmingly indicates that a bachelor's degree is a worthwhile investment in the long run」),自述使命为促进高等教育入学、完成与职业成功;本报告资助方为 **Lumina Foundation 与 Gates Foundation**,两家均以提高学位获得率为纲领。报告头条结论($81,000、+70% 溢价)与机构及资助方利益同向。
- **待 Round 3**:**是**。① 5.3% vs 4.3% 是同一机构报告正文与博客的公开矛盾,需方法学审计席判定哪一版可承重、以及 4.3% 是否确为 multi/interdisciplinary studies 串味;② 该 detailed field 下属专业数报告 Table 3 记 7 个、官方数据工具记 8 个(含 other),须核实以免写错「下辖 N 个专业」;③ 本条与 NY Fed 同源,不满足多源证实,凡压在其上的结论须降级为单源已核。

---

## [G15] NCES 表 325.35 全部数字无误,但第一轮「谷底」不是 1993-94 而是 1995-96 的五年平台,且数据科学并不在 CIP 11 内

- **判决**:CORRECTED(CORRECTED 2/3 · 第 1、3 席;HOLDS 1/3 · 第 2 席)。取最严格者:第 2 席未核 1995-96 一格(其自陈只比对到 1992-93,并称 8 个学位的差距「trivial」),第 1、3 席各自独立核到 1995-96 = 24,506 更低,**第 2 席未指出该发现有误,故该发现成立**。
- **锁定表述**:
  - 来源:NCES《Digest of Education Statistics 2023》Table 325.35「Degrees in computer and information sciences conferred by postsecondary institutions, by level of degree and sex of student: Academic years 1964-65 through 2021-22」(表格制备于 2023 年 11 月)。以下为学士学位授予数(both sexes),三席逐格核对一致。
  - **第一轮周期**:峰值 1985-86 = **42,337**(1984-85 = 39,121、1986-87 = 39,767,确为局部峰);随后跌入 **1991-92 至 1995-96 约 24,500 的五年谷底平台**(1991-92 = 24,821、1992-93 = 24,519、1993-94 = 24,527、1994-95 = 24,737、**1995-96 = 24,506 为最低点**);峰谷跌幅 **−42.1%**(以 24,527 计 −42.07%,以 24,506 计 −42.11%,两算法同为 −42.1%)。**复苏起点应记为 1996-97,不是 1994-95。**
  - **第二轮周期**:峰值 2003-04 = **59,488**(2002-03 = 57,433、2004-05 = 54,111);谷底 2008-09 = **37,992**(2007-08 = 38,523、2009-10 = 39,593,确为局部最小);跌幅 **−36.1%**(−36.13%)。
  - **第三轮上升**:2009-10 = 39,593、2013-14 = 55,271、2017-18 = 79,597、2019-20 = 97,054、2020-21 = 104,883、2021-22 = **108,503**。自 2009-10 起 **+174.0%**;自 2008-09 谷底起 **+185.6%(≈+186%)**。
  - **2021-22 为 provisional**:SOURCE 行逐字「Completions component, IPEDS Fall 2000 through Fall 2021 (final data) and **Fall 2022 (provisional data)**. (This table was prepared November 2023.)」
  - **两条比 provisional 更大的不确定性来源(必须一并标注)**:NOTE 行逐字「Data in this table are based on the **2020** Classification of Instructional Programs. **Some data have been revised from previously published figures.**」即 1964 年以来的整条长序列是用 2020 版 CIP **回溯重编**的,HEGIS 时代(1970-71 至 1985-86)到 IPEDS 时代的映射并不完美,跨版本 Digest 的同年数字会不一致。做「两轮完整蛛网」的跨四十年比较时必须披露这一分类断点。
  - **口径宽度问题成立**:CIP 11「Computer and Information Sciences and Support Services」范围远大于 computer science 本身,含 11.01 一般计算机与信息科学、11.0102 人工智能、11.0103 信息技术、11.04 信息科学、11.09 网络、11.10 信息技术管理与信息系统安全等。
  - **滞后期**:互联网泡沫破裂 2000 年 3 月 → 学位数峰值 2003-04 学年(2004 年春授予),约 4 年,算术无误。但因果读法必须写成**四年学制的学位管道延迟**:2003-04 的峰值人群是约 1999–2000 年入学、即在泡沫顶点或之前做出专业选择的那一届,不是对崩盘的反应;真正的行为反应(报考回落)要到 2004-05 起才在授予数上显现,而 −36.1% 的下滑正是从那里开始。对蛛网论证而言这一改写是加强而非削弱。
  - **无更新版可补**:dt24_325.35 与 dt25_325.35 均返回 HTTP 404(三席各自实测),2025 年 menu_tables 不含 325.x 章节表,d23 仍是该表最新版,最晚年份止于 2021-22。IPEDS Completions 原始数据本身已有 2022-23、2023-24,但未进入 Digest 该表。
- **证据分级**:多源证实(三席各自抓取同一原始 HTML 并解析全部 58 个学年行,数值与四项百分比复算全部一致)
- **数字定版**:
  - **第一轮谷底:写「1991-92 至 1995-96 的五年谷底平台,最低点 1995-96 年 24,506」,跌幅统一写 −42.1%。** 理由:两种算法同得 −42.1%,数字不受影响;但「1993-94 是谷」在事实层面错误(它只排第三低),且会把复苏起点提前两年、扭曲滞后期叙事。第 2 席认为 1993-94「是复苏前最后一年,可作谷标记」——该辩护建立在它没查到 1995-96 的基础上,不成立。
- **不得这样写**:
  - ❌「1993–94 年 24,527(**谷**,−42.1%)」——1993-94 不是最低点(1992-93 = 24,519、1995-96 = 24,506 均更低),它只排第三低。第一轮的底部是持续五年的平台而不是一个点,这直接影响滞后期与复苏起点的叙事。
  - ❌「第三轮上升可能部分反映 CIP 11 口径扩张(**数据科学等新专业被归入**)」——括号里的例子事实相反:CIP 2020 中 **Data Science = 30.70 / 30.7001、Data Analytics = 30.71,归在 CIP 30「Multi/Interdisciplinary Studies」之下,不在 CIP 11**,故数据科学学位**不**计入本表。口径宽度的警告成立且重要,但这个具体佐证必须删除。
  - ❌ 只标「2021-22 为 provisional」而不标「2020 CIP 回溯重编 + 部分数据经修订」——后者对四十年跨期比较的威胁更大。
  - ❌ 把「滞后 4 年」写成**市场信号传导延迟**或学生对崩盘的反应——它本质是四年学制的学位管道延迟。
  - ❌ 把本表序列与 G14 的 CEW 159%(2009→2023)拼接或互相印证——CEW 用的是自建的 computers/statistics/mathematics 分类,比 CIP 11 更宽,方向一致但数值不可替代。
- **利益相关**:无(NCES 官方统计)
- **待 Round 3**:否(三席独立逐格复算一致;两处修正均有一手原文与相邻年份数据支撑)

---

## [G16] BLS 2024–34 预测:软件开发者三处一手件逐字命中,但「合并组 +15%」与「单列 +15.8%」是两个口径,必须并列区分

- **判决**:HOLDS(3/3 票 HOLDS,无一席要求修正)
- **锁定表述**:
  - **A · OOH「Software Developers, Quality Assurance Analysts, and Testers」**(三个 SOC 的合并组,15-1252 + 15-1253)Quick Facts 逐字:2024 Median Pay **$131,450 per year / $63.20 per hour**;Number of Jobs, 2024 = **1,895,500**;Job Outlook, 2024–34 = **15% (Much faster than average)**;Employment Change, 2024–34 = **+287,900**。正文逐字:「Overall employment of software developers, quality assurance analysts, and testers is projected to grow 15 percent from 2024 to 2034, much faster than the average for all occupations.」「About **129,200 openings** for software developers, quality assurance analysts, and testers are projected each year, on average, over the decade.」
  - **同页 Pay 段的分职业中位数**(May 2024):software developers 单列 **$133,080**;QA analysts and testers 单列 **$102,610**。**$131,450 是合并组数**;若与「软件开发者单列」的增速配对,必须用 $133,080。
  - **B · OOH「Computer Programmers」**:2024 Median Pay **$98,670 per year / $47.44 per hour**;Number of Jobs, 2024 = **121,200**;Job Outlook, 2024–34 = **−6% (Decline)**;Employment Change = **−7,200**。逐字:「Despite declining employment, about **5,500 openings** for computer programmers are projected each year, on average, over the decade. **All of those openings** are expected to result from the need to replace workers who transfer to other occupations or exit the labor force, such as to retire.」
  - **C · Monthly Labor Review 2026 年 1 月《Industry and occupational employment projections overview and highlights, 2024–34》**逐字:「One occupation that stands to benefit from these trends is software developers. Not only are they projected to experience employment growth that is over 5 times faster than the all-occupation average (**15.8 percent**), but they are also projected to have the second-largest increase in employment of all occupations with **267,700 new jobs** added through 2034.」
  - **AI 双向表述同篇并存**(论断描述准确):利好句「The growing adoption of AI technologies, including generative AI tools, is another factor that will fuel strong job growth among computer and mathematical occupations.」;利空句(Highlights 段)「The growing adoption of AI technologies, including generative AI tools, and resulting productivity gains are expected to dampen labor demand in a variety of fields, such as sales, design, and administrative support.」
  - **口径区分(本条对文章最有用的一半)**:+15% / +287,900 / 1,895,500 属**三职业合并组**;+15.8% / +267,700 属 **software developers 单列(SOC 15-1252)**,OOH 同页 Job Outlook 图表把它四舍五入作 **16%**。两者算术自洽:267,700 ÷ 0.158 ≈ 1,694,000 的 2024 年开发者基数,余约 201,000 的 QA/testers 补足合并组的 1,895,500;**合并组增速略低于开发者单列,正因为最易被自动化的 QA/测试部分增长更慢**——这对「AI 与入门岗」的主题是实质性论据。
  - **OOH 图表的官方对照序列**:Software developers 16% / Software developers, quality assurance analysts, and testers 15% / Software quality assurance analysts and testers 10% / Computer occupations 9% / Total, all occupations 3%。
  - **全职业平均**:OOH 作 **3%**,MLR 精确值 **3.1%**(「Total employment is projected to grow 3.1 percent between 2024 and 2034, increasing from 170.0 million to 175.2 million」)。两处内部一致性校验通过:15.8 ÷ 3.1 = 5.1(「over 5 times faster」✓);计算机与数学类 10.1% ÷ 3.1 = 3.26(「over 3 times as fast」✓)。若文章保留一位小数,用 3.1%。
  - **必须向读者标注的性质**:这是 BLS 就业预测(EP)模型的**十年期建模基线**(2024 基年,2026 年初发布),不是实测就业,也不带误差区间;其职业配置结构主要外推自历史行业—职业矩阵,该轮发布时大多数 agentic coding 的采用数据尚不存在。BLS 在同一文件内对 AI 同时给出利好与利空,本身即表明模型未对 AI 冲击作单向假设。
  - **all / many 的区别须保留**:程序员是「**All** of those openings」来自替换需求;合并组的年均空缺表述不同,不可互换。
- **证据分级**:多源证实(三席分别取不同日期的 Wayback id_ 原始快照——2026-06-01 / 2026-07-05 / 2026-07-10 / 2026-07-14 / 2026-07-17——逐格逐字核对,三处一手件全部命中,无一处需修;bls.gov 对三席直连均 403)
- **不得这样写**:
  - ❌ 把 **+15%/+287,900** 与 **+15.8%/+267,700** 当同一个数或混用——前者是三职业合并组,后者是软件开发者单列。正确写法:「合并组 +15% / +287,900」与「软件开发者单列 +15.8%(OOH 图表作 16%)/ +267,700」并列,并注明全职业平均 MLR 为 3.1%、OOH 作 3%。
  - ❌ 把 **$131,450** 挂在「软件开发者」名下——那是含 QA/testers 的合并组中位数,开发者单列为 $133,080。
  - ❌ 把 BLS 预测写成**观测数据或有把握的预言**——须写明是十年期建模基线,且模型对 AI 冲击自陈双向。
  - ❌ 只引 MLR 的 AI 利好句而不引同篇的利空句(或反之)——两句同篇并存,单引任一句都是选择性引用。
  - ❌ 把程序员的「All of those openings」放宽成「many」,或把合并组的空缺来源说成「全部来自替补」。
- **利益相关**:无(BLS 官方统计与其官方期刊)
- **待 Round 3**:否(三席分别以不同快照独立逐字命中,属多源证实;唯一新增内容是口径澄清与建模性质标注,均有一手原文支撑)

---

## [G17] Indeed Hiring Lab:软件岗位广告仍比疫情前低约 27%(不是 30%),而「+15% 反弹」的基期恰是序列谷底且由厂商事件选定

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - 来源:Indeed Hiring Lab,Guillermo Gallacher,《AI and Job Postings: From Destruction to Creation》,2026-07-08 发布。
  - **逐字引语(三席均确认一字不差)**:「Even after the recent rise, software development job postings remain about 27.5% below their pre-pandemic level, while overall job postings are essentially the same as in February 2020.」
  - **水平值**:Software Development(total postings)指数(2020-02-01 = 100)**2026-06-30 = 73.47**,2026 年 6 月区间 72.33–73.62,即较疫情前基期低 **26.4%–27.7%**。文章自述 27.5%。
  - **反弹幅度**:文章原文两处均为「**almost** 15%」(Key points:「US software development job postings have grown by **almost 15%** since the launch of Claude Code in late February, 2025, while overall job postings fell by 7% over the same period.」),是「接近 15%」而非「达到 15%」。以当前公开数据版本重算同一区间:63.26(2025-02-24)→ 73.47(2026-06-30)= **+16.1%**;若延至最新观测 75.62(2026-07-17)= **+19.5%**;同期全部岗位为 −6.8% 至 −7.4%。
  - **⚠️ 基期是序列谷底,且由厂商事件选定(第 2 席认定为最重要的修正)**:文章图注逐字「indexed to 100 on **February 24, 2025, the launch of Claude Code**」。而 2025-02-24 的指数值 63.26 几乎就是整个 2025–26 窗口的最低点(月末值:2025-02 = 62.79、2025-03 = 62.57 为区间谷)。**从距历史低点一步之遥处起算,机械性地把反弹幅度最大化。**任何复用「+15%」的写法都必须同时说明基期即谷底,否则读者会把触底反弹误读为恢复健康——水平面仍比 2020 年低约 27%。文章自己也承认「correlation does not imply causation」与「there were, of course, many other factors influencing the market both then and now」。
  - **月末序列(Software Development, total postings,2020-02-01 = 100)**:2025-01 66.90 | 2025-02 62.79 | 2025-03 62.57 | 2025-04 63.27 | 2025-05 63.98 | 2025-06 65.56 | 2025-07 66.04 | 2025-08 65.25 | 2025-09 64.29 | 2025-10 65.90 | 2025-11 66.62 | 2025-12 67.31 | 2026-01 69.40 | 2026-02 70.87 | 2026-03 72.89 | 2026-04 72.61 | 2026-05 73.55 | 2026-06 73.47 | 2026-07-17 75.62(不完整月)。
  - **全部岗位 JPI**:**季调(SA)2026-06-30 = 100.96(四舍五入 101.0)**;**同日未季调(NSA)= 104.02**,差 3 个点,不标 SA/NSA 会被人拿反。2025-02-24 SA = 108.97;2026-07-08 SA = 101.18;2026-07-17 SA = 101.54。
  - **增量分解(必须带两个限定)**:图注逐字「senior roles account for **71% of the net increase** in US software development postings between May 2025 and May 2026, and **AI-related titles for 37%**, **with the two categories overlapping**.」即:① 是 **2025-05 至 2026-05 净增量(net increase)**的构成,不是存量结构;② **两类互相重叠,不能相加**。
  - **三个基期不可混在一句里**:27.5% 对 **2020-02-01 = 100**;+15% / −7% 对 **2025-02-24 = 100**;71% / 37% 是 **2025-05 至 2026-05 的净增量分解**。
  - **指数方法论**:「seasonally adjusted」与两个基期出自本文;**七日 trailing average** 出自 Hiring Lab 官方方法说明(job_postings_tracker README:February 1, 2020 = 100、seven-day trailing average、分地区与 sector 分别季调,2024 年 11 月起改用 Deutsche Bundesbank 日频季调法并**回溯修订历史数据**),**不出自本文,引用时不得挂在本文名下**。
  - **口径无法与 BLS 对齐**:Indeed 的「software development」是 **Indeed 自有的、基于标准化职位标题(normalized job titles)的 sector 分类**,不是 SOC/官方职业分类,**不能与 BLS 的 software developers 直接对齐**——这正是 G16 与 G17 可以同时为真的技术原因之一,应写明。
  - **文章自身最该被引的一句(对准大学生最不利、最不能被标题效应盖过)**:「This suggests demand is growing for experienced professionals who can work with AI, **not necessarily a broad-based recovery across all software roles**.」文章并引入「seniority-biased technological change」。
- **证据分级**:多源证实(三席各自直取文章一手 HTML 并逐字比对正文、Key points 与图注 alt-text;底层日频序列由三席分别从 Indeed Hiring Lab 官方公开仓库 job_postings_tracker 的 US/job_postings_by_sector_US.csv 与 US/aggregate_job_postings_US.csv 取得,关键值一致。FRED 序列 IHLIDXUSTPSOFTDEVE 对多席直连返回 403/000,已以其上游同源数据替代)
- **数字定版**:
  - **疫情前落差:文章原句逐字引用「about 27.5% below」,并括注「按 Hiring Lab 公开日频数据,2026-06-30 指数 73.47,实为低约 26.5%」。绝不写「约 30%」。** 理由:三席一致认定「≈73」与「低约 30%」在同一句里自相矛盾(73 就是低 27%);「约 30%」高估 2.5–3.5 个百分点且方向偏悲观,该序列上一次真的低约 30% 是 2026 年 1 月(69.40),已是半年前。
  - **反弹幅度:写「接近 15%(Hiring Lab 2026-07-08 口径)」,并注明数据截取日期与回溯修订。** 理由:文章原文是「almost 15%」,写成「+15%」是向上取整;而按当前数据版本重算同一区间为 +16.1%(至 2026-06-30)/ +19.5%(至 2026-07-17)。Indeed 会持续修订季调因子并回溯历史数据,**同一句「自 Claude Code 发布以来 +X%」在不同抓取时点会给出不同数字**,故必须锁定为「文章口径 + 引用日期」,不得当作固定事实。
  - **JPI = 101.0 定版为季调值(精确 100.96),并必须标注 SA;NSA 104.02 仅作对照。**
- **不得这样写**:
  - ❌「software development ≈ 73(较 2020-02 **低约 30%**)」——同一句内自相矛盾,且高估落差 2.5–3.5pp。
  - ❌「自 2025-02-24 起算 **+15%**」——原文是「almost 15%」;且**不披露基期就是序列谷底、且是某 AI 厂商的产品发布日**,等于把因果故事写进了测量本身。必须同时说明:这是从近乎历史低点起算的反弹,水平面仍比 2020 年低约 27%。
  - ❌ 把 **71% 与 37% 相加**或据此推出「其余 −8% 来自初级岗」——两类明确重叠,且都是**净增量**份额而非存量结构。
  - ❌ 把 27.5%、+15%/−7%、71%/37% 三组数字写在同一坐标系里——它们分属三个不同基期与时间窗。
  - ❌ 把「**七日滚动平均**」挂在本文名下——本文只写了 seasonally adjusted 与两个基期,该方法论出自 Hiring Lab 方法说明页,须分开引用。
  - ❌ 引 JPI 101.0 而不标**季调(SA)**——同日未季调为 104.02。
  - ❌ 把 Indeed 的 software development sector 与 **BLS software developers** 当作同一口径互证或互驳。
  - ❌ 让「软件岗位在回升」的标题效应盖过文章自己的结论——增长集中于资深岗与 AI 相关岗,作者明说「not necessarily a broad-based recovery across all software roles」。
- **利益相关**:**须标注,共四层**。(a) Indeed 是招聘广告平台,其商业利益在于「岗位广告数是有意义的劳动力市场信号」;指数仅覆盖 Indeed 自有岗位,平台份额漂移会污染指数,重复/过期/从未真实招聘的广告也计入;广告数下降亦可能只反映招聘方式变化。(b) **编辑框架问题**:把基期定在「Claude Code 发布日」并以此为叙事轴心,是作者选定的框架,不是自然实验;标题「From Destruction to Creation」是方向性判断,而底层水平数据(仍低于 2020 年约 27%)本身并不支持这一判断。(c) 该基期同时是序列谷底,框架与测量互相强化。(d) 文章的核心发现指向资深岗集中,对入门口最不利,不得被选择性省略。
- **待 Round 3**:**是**。① 该指数会被 Indeed 回溯修订(2024-11 起改用 Bundesbank 日频季调法并重算历史),同一口径在不同抓取时点给出 +15% / +16.1% / +19.5% 三个值,需方法学审计席判定文章引用应锁定哪一版本与哪一截取日;② 三席都是从同一上游(Hiring Lab 官方仓库/FRED 转载)取数,不构成独立测量,需反证搜索席寻找独立岗位广告数据(如 LinkUp、Lightcast、Revelio 等)对「软件岗位广告仍低于疫情前约 27%」与「资深岗主导反弹」两项作独立复核。

---

## [G18] Eloundou 等《GPTs are GPTs》:3%/49% 不在摘要里,Science 版是 3 页 Policy Forum,且 1.8%/46% 是真实下修

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - 一手件有两个不同版本,必须分开引:①工作论文 **Eloundou, Manning, Mishkin & Rock,《GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models》,arXiv:2303.10130,v5(2023-08 修订)——未过同行评审的预印本**;②期刊版 **《GPTs are GPTs: Labor market impact potential of LLMs》,Science 384(6702): 1306–1308,DOI 10.1126/science.adj0998,在线 2024-06-20 / 纸刊 2024-06-21——栏目为 Policy Forum(3 页政策短文,非完整研究论文,页面标注 "No access")**。
  - **arXiv v5 摘要**只给出两组数:β 口径的 **80% 的劳动者所在职业至少 10% 任务被暴露、19% 的劳动者所在职业过半任务被暴露**;以及**任务**口径的 "about 15% of all worker tasks" 与 "between 47 and 56% of all tasks"。**注意后者分母是任务,不是劳动者。**
  - **3% 与 49% 出自 arXiv v5 正文第 1 节 Introduction(PDF 第 2 页),不在任何一版摘要里**(v1/v3/v4/v5 摘要均已逐版核过)。原文:"Human assessments suggest that only 3% of U.S. workers have over half of their tasks exposed to LLMs when considering existing language and code capabilities without additional software or modalities. Accounting for other generative models and complementary technologies, our human estimates indicate that up to 49% of workers could have half or more of their tasks exposed to LLMs."
  - **Science 版摘要只有两个数**,逐字为:"we estimate that roughly 1.8% of jobs could have over half their tasks affected by LLMs with simple interfaces and general training. When accounting for current and likely future software developments that complement LLM capabilities, this share jumps to just over 46% of jobs." **Science 摘要中根本没有 80%/19%**。
  - **对应关系必须写准**:1.8%/46% 对应的是 arXiv 正文的 3%/49%(即 α50 与 ζ50 两个口径),**不是** 80%/19%(β 口径)的改写。分母也变了:arXiv 说 **workers**(就业加权),Science 说 **jobs**。
  - **同一研究还有第三套分母——未加权的职业层面**(arXiv §4.2):"human annotators determined that 2.3% of occupations are α50-exposed, 21.6% are β50-exposed, and 47.3% are ζ50-exposed"。故 3% / 2.3% / 1.8% 是三个不同分母下的数,面向准大学生必须点明。
  - **3%→1.8%、49%→46% 是真实下修,不是数据版本漂移**:两版都用 O*NET 27.2(arXiv 正文 "We use the O*NET 27.2 database (O*NET, 2023)";Science 参考文献 9 "O*NET, O*NET 27.2 Database")。
  - **构念定义(可原样承重)**:§3.3 "we define exposure as a measure of whether access to an LLM or LLM-powered system would reduce the time required for a human to perform a specific DWA or complete a task by at least 50 percent",rubric 中 E0 含 "while maintaining equivalent quality"。三指标 "(i) α, corresponding to E1... (ii) β, which is the sum of E1 and 0.5*E2... (iii) ζ, the sum of E1 and E2, an upper bound"。摘要 80%/19% 用的是 **β**(§4.1 逐字)。50% 阈值作者自陈 "Although this threshold is somewhat arbitrary, it was selected for ease of interpretation by annotators."
  - **标注档位实为四档而非三档**:E0/E1/E2/**E3**,E3(图像生成能力)在全部分析中并入 E2。原文:"we categorize access to image capabilities separately (E3) to facilitate annotation, though we combine E2 and E3 for all analyses."
  - **四处免责声明(逐字,可承重)**:①"We define exposure as a proxy for potential economic impact without distinguishing between labor-augmenting or labor-displacing effects.";②"This exposure measure reflects an estimate of the technical capacity to make human labor more efficient; however, social, economic, regulatory, and other determinants imply that technical feasibility does not guarantee labor productivity or automation outcomes.";③Table 4 **表题(caption,非脚注)**"...but it does not necessarily suggest that their tasks can be fully automated by these technologies.";④摘要末句 "We do not make predictions about the development or adoption timeline of such LLMs."——**第④句是 v4 才加入摘要的,v1/v3 摘要没有**。
  - **rubric、Table 2、四处免责全部只存在于 arXiv 工作论文中**,Science 那 3 页里没有。凡引"Eloundou et al. (2024)"的方法学细节者,实际引的都是预印本。
  - **传播机制(可承重)**:截至 2026-07-24,RePEc(ideas.repec.org/p/arx/papers/2303.10130.html)仍著录为 "Papers 2303.10130, arXiv.org, revised Aug 2023",**无 "Published in" 字段**;arXiv abs 页也无 journal-ref,只有自签 DOI 10.48550/arXiv.2303.10130。两大索引都没标记其已发表,这正是被取代的 80%/19% 至今仍被广泛转引的原因。
- **证据分级**:多源证实(三席各自下载 arXiv v5 PDF 并 pdftotext 逐字核对,数字与引语全部一致;Science 摘要由三席分别经 Wayback id_ 原始快照、Semantic Scholar 出版方馈送、GovAI 论文页三条独立路径取得,文本一致;书目由 Crossref、PubMed PMID 38900883、OpenAlex W4399848789 三方交叉确认)
- **数字定版**:
  - **文章主引 Science 版的 1.8% / 46%(jobs 口径)**,并注明"工作论文正文对应的是 3% / 49%(workers 口径),经期刊版下修"。理由:Science 版经同行评审、口径更晚、且下修是同一 O*NET 版本下的真实修订,引 3%/49% 而不说它已被下修属于引用被取代版本。
  - **80% / 19% 若要用,必须标明"这是 β 口径、出自未过审的 arXiv 工作论文摘要,期刊版摘要中没有这两个数"**。不得与 1.8%/46% 并置成"两个版本两套数字"。
  - **2.3% / 21.6% / 47.3%(未加权职业口径)须与 1.8%/46% 并列呈现**若文章要谈分母敏感性;定不下单值,因为分母定义不同,不是同一量的两个估计。
- **不得这样写**:
  - ❌「arXiv v5 **摘要**给出人工标注下"仅 3%""最多 49%"」——归属错误,这两个数在正文 Introduction,摘要里没有。三席一致点名,是本条最严重的错误。
  - ❌ 把摘要的 "15% of all worker tasks" / "47–56% of all tasks" 当成劳动者占比——分母是**任务**。
  - ❌ 暗示「80%/19% 在期刊版被改成 1.8%/46%」——两组数分属 β 与 α50/ζ50 三个不同口径,不构成同一数字的两版。
  - ❌ 把 Science 版称作「同一篇论文的正式版/完整研究论文」——它是 3 页 Policy Forum,方法学细节一概不在其中。
  - ❌ 写「Table 4 **脚注**」——是 Table 4 的**表题(caption)**。
  - ❌ 写「三档 E0/E1/E2」——标注时是四档,E3 被并入 E2。
  - ❌ 把 3%/2.3%/1.8% 混着用而不标分母(workers 加权 / occupations 未加权 / jobs)。
  - ❌ 引用该研究时不标「arXiv 版为**预印本、未过同行评审**」。
- **利益相关**:作者 4 人中 3 位署名 OpenAI / OpenResearch;暴露度评估由 OpenAI 内部人员与其对齐外包标注员完成(详见 G19)。研究方即模型开发方。
- **待 Round 3**:否(三席分别以互不相同的取证路径拿到 Science 摘要与书目,已构成多源证实)

---

## [G19] 暴露度标注的方法学缺陷:人机一致率、零重叠 top-5,以及作者自己的抗辩

- **判决**:CORRECTED(2/3 CORRECTED + 1 HOLDS;取最严格的 CORRECTED)
- **锁定表述**:
  - **人机一致性(arXiv v5 Table 2,六格逐格核实)**:GPT-4 Rubric 1 vs Human — α 一致率 80.8%/Pearson r=0.223;β 65.6%/r=0.591;ζ 82.1%/r=0.654。GPT-4 Rubric 2 vs Human — α 81.8%/r=0.221;β 65.6%/r=0.538;ζ 79.5%/r=0.589。故「人机一致率区间 65.6%–82.1%」「r 最低 0.221」均属实(0.221 出自 Rubric 2 的 α 行;论文自身分析用 Rubric 1,其 α 的 r=0.223)。表注:"In the paper we use GPT-4, Rubric 1." 模型自比(Rubric1 vs Rubric2)则高达 91.1%。
  - **标注者构成**:不是「全部由承包商标注」。原文 "The authors personally labeled a large sample of tasks and DWAs and enlisted experienced human annotators who have reviewed GPT-3, GPT-3.5 and GPT-4 outputs as part of OpenAI's alignment work (Ouyang et al., 2022)";脚注 5 给出分工:"The authors annotated DWAs that clearly required a high degree of physicality or manual dexterity, and the contracted annotators labeled the remaining activities..."。**正确写法:由 OpenAI 内部人员与其对齐外包标注员共同完成,无一人是对应职业的从业者;且作者亲自挑走了体力/手工类 DWA,这一分工本身即一处未被讨论的方向性偏差来源。**
  - **rubric 差异**:论文措辞是 "slight differences between the rubric presented to humans and the one used for GPT-4",且系刻意为之("This decision was made deliberately to guide the model towards reasonable labels without excessively influencing human annotators.")。**更值得写的是调参方向**:"We made slight modifications to the rubric (which was used as a 'prompt' to the model in this case) to enhance agreement with a set of human labels."——GPT-4 的 rubric 是**朝人类标签调过的**,这会机械抬高 Table 2 的一致率。另有一处更大的不可比:**人类标 DWA + 部分 task,GPT-4 标全部 task/occupation pair**,单位与覆盖面都不同。
  - **人类标注才是主结果**:"In this analysis, we present results from human annotators as our primary results."(此句是 G21 引用链批评的关键前提)
  - **四处作者自陈(逐字,可承重)**:①§3.4.1 "A fundamental limitation of our approach lies in the subjectivity of the labeling... However, this group is not occupationally diverse, potentially leading to biased judgments regarding LLMs' reliability and effectiveness in performing tasks within unfamiliar occupations.";②§3.4.2 "...we use multiple annotation sources, but none should be considered the definitive ground truth relative to the others.";③§3.4.3 "Human annotators were mostly unaware of the specific occupations mapped to each DWA during the labeling process.";④§3.4.3 "If indeed, the task-based breakdown is not a valid representation of how most work in an occupation is performed, our exposure analysis would largely be invalidated."
  - **86 vs 15**:Table 4 内嵌注 "Humans labeled 15 occupations as 'fully exposed.'" / "The model labeled 86 occupations as 'fully exposed.'",86/15=5.73,「5.7 倍」属实。**限定:这是 ζ 口径下 100% 暴露的职业计数。**
  - **top-5 名单零重叠**:Table 4 中 α、β、ζ 三组人机 top-5 **完全零重叠**(人工 α:Interpreters and Translators / Survey Researchers / Poets, Lyricists and Creative Writers / Animal Scientists / Public Relations Specialists;模型 α:Mathematicians / Correspondence Clerks / Blockchain Engineers / Court Reporters and Simultaneous Captioners / Proofreaders and Copy Markers)。**但只有 α、β 两对可承重**:ζ 那一对的 top-5 是从人工 15 个、模型 86 个并列 100% 的职业里任取五个,不重叠不构成分歧证据。
  - **Barbers 反直觉结果**:§4.1 "...yields some curious results (e.g. ranking Barbers as having reasonably high exposure)"。**限定:其语境是未按 O*NET "Importance" 加权导致的怪异结果,不是人机分歧的例证。**
  - **必须并列的作者抗辩(否则会高估缺陷的破坏力)**:同一 §3.4.2 结尾写 "Still, we observe a high degree of agreement between human ratings and GPT-4 ratings at the occupation level concerning overall exposure to LLM systems (see Table 2, Figure 2).";§3.4.3 称最大匹配法下 "the agreement remained relatively consistent"。
- **证据分级**:多源证实(三席各自 pdftotext 逐格核对 arXiv v5,Table 2 六格、86/15、四处引语、top-5 名单三席结果完全一致)
- **数字定版**:
  - **一致率写「65.6%–82.1%」、r 写「0.221–0.654」**,并注明两端分别来自哪一行(65.6% 与 r=0.591 是 β/Rubric 1;0.221 是 α/Rubric 2;论文自身分析用 Rubric 1,其 α 的 r=0.223)。理由:取单值会让读者以为只有一组比较;区间加行标注既准确又保留信息。
  - 若只引一个数以说明「机器标注不可替代人工」,**用 β 的 65.6% / r=0.591**——因为摘要的 80%/19% 正建立在 β 上,同口径最有说服力。
- **不得这样写**:
  - ❌「人工标注者是 OpenAI 自己的对齐标注承包商(非各职业从业者)」——漏掉作者本人也参与标注,且作者挑走了体力/手工类 DWA。改写为「OpenAI 内部人员 + 其对齐外包标注员共同完成,无一是对应职业从业者」。
  - ❌「GPT-4 用的 rubric 与人类用的**不是同一份**」而不给作者的 "slight" 自评——会让读者以为是两套完全不同的标准。正确的杀伤点是「rubric 被朝人类标签调过」与「标注单位不同(DWA vs task/occupation pair)」。
  - ❌「人机最高暴露职业名单**几乎**不重叠」——实为完全零重叠,「几乎」偏保守;但同时不得拿 ζ 那一对当证据。
  - ❌ 只引缺陷不引作者抗辩("a high degree of agreement... at the occupation level")——属选择性引用,会高估该缺陷的破坏力。
  - ❌ 把 Barbers 那句当成「人机分歧」的例子——原文语境是未加权导致的怪异结果。
  - ❌ 把 86 vs 15 说成泛指的「暴露职业数」——那是 ζ 口径下 100% 暴露的计数。
- **利益相关**:标注者全部来自 OpenAI 体系(作者本人 + OpenAI 对齐工作的外包标注员),评估对象是 OpenAI 自家模型的能力边界。属**研究方即利益方**,但方向不明确(高估或低估均有可能),不宜简单套用「厂商故而夸大」。
- **待 Round 3**:否(三席逐格独立核对一致,且全部证据均为可回溯的一手 PDF 文本)

---

## [G20] Anthropic Economic Index:automation 从未「越过 50%」,且多处限定语与稳健性检验被删

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - **首期(2025-02-10 公告《The Anthropic Economic Index》 + 配套论文 arXiv:2503.04761,v1 提交 2025-02-11,预印本)**:样本为 "approximately one million conversations with Claude (specifically, Free and Pro conversations on Claude.ai)",映射到 O*NET 的 "around 20,000 specific work-related tasks";摘要另称 "over four million Claude.ai conversations"——**这是跨各项分析的合计(聚类另用约 280 万条),100 万是任务映射分析自身的样本,两者不是「公告 vs 论文」的对举**。
  - 首期结论逐字:"~36% of occupations using AI for at least a quarter of their associated tasks";"only approximately 4% of jobs used AI for at least 75% of their tasks"(任务口径阈值定义:"Task usage is defined as occurrence across five or more unique user accounts and fifteen or more conversations");"57% of usage suggests augmentation of human capabilities (e.g., learning or iterating on an output) while 43% suggests automation (e.g., fulfilling a request with minimal human involvement)";Computer & Mathematical 类 "37.2% of all queries"(加写作类 10.3% ≈ 47.5%,故「近一半」成立)。
  - **首期两条决定性限制**:①**7 天快照**——论文 §4.1 "We use snapshots of Claude.ai Free and Pro conversations over 7-day periods";②**排除全部商业客户**——"the results shared in this paper exclude activity from business customers (i.e., Team, Enterprise, and all API customers)"。第②条直接决定了后来 Claude.ai 与 1P API 的对比**不是同一总体**。作者亦自陈 "While our data and methods face important limitations and only paint a picture of AI usage on a single platform..."。
  - **2025-09-15 报告**:"The share of directive conversations sampled from Claude.ai conversations jumped from 27% in V1 in late 2024 to 39% in V3.";"This is the first report where automation usage exceeds augmentation usage."——**是首次超过 augmentation,不是越过 50%**。脚注 4 给出绝对值:**49%(Sonnet 4 分类器)/ 45%(Sonnet 3.7 重跑)**;正文形容 Claude.ai 为 "the split between automation and augmentation is nearly even"、"about 50% for Claude.ai users"。六分类框架下存在「两者皆非」的对话,故 49% 可以在不过半的情况下超过 augmentation。
  - 同期 API 对比:"77% of API transcripts show automation patterns (especially full task delegation) versus just 12% for augmentation";"97% of tasks show automation-dominant patterns in API usage, compared to only 47% on Claude.ai"。
  - **跨期可比性:至少三条原因,且作者已做稳健性补救**。①分类器换代 + 作者补救(完整句):"We note that V3 uses Claude Sonnet 4 for classification, while V2 used Sonnet 3.7, which complicates direct comparison. To address this, we reran V3 data with Sonnet 3.7 and still found directive interactions rising significantly (though to a lower absolute level of 45% automation versus 49% with Sonnet 4). We also verified this trend is not driven by changes in task mix...";②**2026-03 报告改用 2019 年版 O*NET 任务分类(此前各期为 2010 年版),直接改变了分母本身**;③**每期都是 7 天快照**(2026-03 报告样本仅 2026-02-05 至 02-12 一周)。作者原话是 "complicates direct comparison",**不是「不可比」**。
  - **犹他州异常**:脚注 7 "When further investigating Utah's activity, we discovered a notable fraction of its usage appeared to be possibly associated with coordinated abuse.",但**同一脚注紧接着**:"However, we ran robustness checks and believe that this activity is not driving the results."
  - **2026-03-24《Learning curves》**:"augmentation in Claude.ai increased slightly... In Appendix Figure A.3, we show that automation decreased sharply in the 1P API data."
  - **2026-06-26《Cadences》**:"Our final linked sample consists of about 9,700 survey respondents."(随机抽 Claude 用户、剔除 session < 5 者,**与 2025-12 用 Anthropic Interviewer 访谈的约 81,000 人不是同一批**);"The Economic Index Survey is not representative of the general population.";"Computer and Mathematical occupations are the most heavily over-represented, making up roughly 30% of survey respondents—comparable to their share of Claude usage, but far above their 4% share of US employment."
  - **2026-03-05《Labor market impacts of AI》(Massenkoff & McCrory)**:"Computer Programmers are at the top, with 75% coverage"(部分媒体转引 74.5%,以官方页 75% 为准);"30% of workers have zero coverage, as their tasks appeared too infrequently in our data to meet the minimum threshold."——**零 coverage 的原因是数据里出现太少,不等于「不受影响」,该限定语必须一起引**;"For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage points... **although the relationship is slight. Interestingly, there is no such correlation using the Eloundou et al. measure alone.**";"We find no systematic increase in unemployment for highly exposed workers since late 2022";"The averaged estimate in the post-ChatGPT era is a 14% drop in the job finding rate compared to that in 2022 in the exposed occupations, **although this is just barely statistically significant. (There is no such decrease for workers older than 25.)**"。该 14% 指的是**月度求职成功率**(约 2%/月 降约 0.5pp),**不是就业率或失业率**。该报告于 2026-03-08 发过更正:"Corrected Figure 7, which incorrectly reversed the labels between top quartile and zero exposure group inflow rates."
- **证据分级**:**厂商口径**(厂商自有平台数据 + 厂商自有分类器 + 厂商自行发布,无第三方复核,样本仅覆盖自家平台)。核验层面为多源证实——三席分别以 curl 剥标签、WebFetch 原页、arXiv API/PDF 三条路径取得,引语逐字一致。**方向可参考、程度不承重。**
- **数字定版**:
  - **2025-09 的 automation 水平写「49%(Sonnet 4 分类器)/ 45%(Sonnet 3.7 重跑)」,并明写「首次超过 augmentation,但未过半」**。理由:两个数出自同一脚注、是同一量的两种分类器读数,必须成对出现才能显示作者已做稳健性检验;取任一单值都会丢掉这一信息。
  - **首期 automation/augmentation 用整数 43% / 57%**,可加注「Anthropic 官方数据集归一化后为 42.6% / 57.4%」。理由:42.6/57.4 已溯源成功(HuggingFace 官方数据集 release_2025_02_10/automation_vs_augmentation.csv:directive 22.5633 + feedback loop 12.0363 = 34.600;learning 18.9176 + task iteration 25.4765 + validation 2.3142 = 46.708;对已分类部分归一化得 42.6%/57.4%),**但它是对已分类子集重新归一化的结果,而公告页与论文正文一律用 43%/57%**。以出版口径为准,一位小数留作注脚。
  - **NP 式的「首次越过 50%」不存在,不存在定版问题——该阈值须整句删除。**
- **不得这样写**:
  - ❌「2025-09 报告显示 automation **首次越过 50%**」——**三席一致点名的实质性错误**。原报告从未这样说;它说的是首次**超过 augmentation**,绝对水平 49%/45%。把相对比较升级成绝对阈值,对准大学生是实打实的误导。
  - ❌「作者自陈跨期**不可比**」——原文是 "complicates direct comparison",且紧接着给出了 Sonnet 3.7 重跑与 task mix 检验两项补救。只引前半句等于删掉作者的稳健性检验。
  - ❌ 把跨期问题只归因于分类器换代——更硬的两条是 **O*NET 分类版本从 2010 版换到 2019 版(分母变了)** 与 **每期都是 7 天快照**。
  - ❌ 引犹他州句而不带 "However, we ran robustness checks and believe that this activity is not driving the results."——称其「自曝数据污染」属选择性引用。
  - ❌ 引「22–25 岁 job-finding rate 下降 14%」而删掉 "although this is just barely statistically significant" 与 "There is no such decrease for workers older than 25."——等于把一条边缘结果包装成事实。且必须写明它是**月度求职成功率**,不是失业率。
  - ❌ 引「每增 10pp coverage,BLS 增长预测降 0.6pp」而删掉 "although the relationship is slight" 与 "there is no such correlation using the Eloundou et al. measure alone."
  - ❌ 写「零 coverage 的 30% 劳动者不受 AI 影响」——原因是其任务在数据中出现太少,未达最低阈值。
  - ❌ 把「首期约 100 万条(配套论文 400 万+)」作为公告与论文的对举——100 万正是论文自身任务映射分析的样本。
  - ❌ 把 2026-06 的 9,700 人与 2025-12 的约 81,000 人混为同一批样本。
  - ❌ 把 Claude.ai 与 1P API 的对比说成同一总体的两个切面——首期明确排除了 Team/Enterprise/API 全部商业客户。
- **利益相关**:全部数据、分类器(Claude 给 Claude 的对话打标)、报告均出自 Anthropic 自身,样本仅覆盖自家平台,无第三方复核。**但此处的利益冲突方向是反直觉的**:公司研究部门 2026-03 的结论("no systematic increase in unemployment for highly exposed workers since late 2022")与本公司 CEO 的营销叙事相悖——Amodei 2025-05-28 对 Axios("Behind the Curtain: A white-collar bloodbath")称 AI 可能在 1–5 年内消灭半数入门级白领岗、失业率升至 10–20%;2026-07-24 Fortune 刊出报道称该分歧已公开化。故**不宜套用「厂商发布故而夸大」的怀疑框架**;真正的偏差风险在样本(仅自家平台、7 天快照、早期排除企业客户)而非动机。**同时,这一「相反」要降调**:公司报告的结论不是「影响有限」,而是「**迄今检测不到**」,且自陈可检测门槛约为 1 个百分点的差异失业率;一个是预测,一个是迄今未检出,不构成严格意义上的对立结论。
- **待 Round 3**:**是**。①Amodei 的 Axios 表态有一席因页面反爬(HTTP 403)未能逐字取得,系依多家二手报道一致复述记录,需反证搜索席取得逐字原文或改为二手转述并标注;②2026-07-24 Fortune 那篇「Anthropic 首席经济学家解释 CEO 为何错了」仅一席引到,需独立核实标题与内容;③2026-03 报告改用 2019 版 O*NET 这一条仅一席指出,需第二席回原页坐实,因为它是「跨期不可比」论证中最硬的一环。

---

## [G21] AI 暴露度构念的「假独立」引用链:范围要收窄,但链条比原论断更长

- **判决**:CORRECTED(2/3 CORRECTED + 1 HOLDS;取最严格的 CORRECTED)
- **锁定表述**:
  - **一手件**:①Brynjolfsson, Chandar & Chen,《Canaries in the Coal Mine?》,Stanford Digital Economy Lab,**2025-11-13 版**(封面日期 November 13, 2025)——**工作论文,未过同行评审**;②Iscenko & Curto Millet,《Looking for the Ladder: Is AI Impacting Entry-Level Jobs?》,Economic Innovation Group,**2026-01**——智库 note,非同行评审。
  - **Canaries 用了两套自变量**(§3.2 逐字):"The first uses exposure measures from Eloundou et al. (2024), who estimate AI exposure by O*NET task using ChatGPT validated with human labeling. They construct occupational exposure measures by aggregating the task data to the 2018 SOC code level. **We focus on the GPT-4 based β exposure measures from their paper.**";"The second approach we take uses generative AI usage data from the Anthropic Economic Index (Handa et al., 2025)... We use this as an estimate of whether AI usage for an occupation is primarily complementary or substitutable with labor."。合并方式:"We use a 2010 SOC code to 2018 SOC code crosswalk from the BLS to merge the exposure measures to the payroll data."(合并对象是 ADP **工资单就业微观数据**)。automation/augmentation 映射见脚注 14:"Directive and Feedback Loop conversations are considered Automative; Task Iteration, Learning, and Validation are considered Augmentative."
  - **EIG 用的是同一套 β,且系其自陈**(方法附注逐字):"We calculate AI exposure quintiles using the data and code provided in the replication package for Eloundou et al. (2024), using GPT-4 β scores and an equal weight scheme. **We understand this is the same basis for exposure calculations as was used in Brynjolfsson et al. (2025).**"——注意 "We understand" 是 **EIG 自己的推断**,非 Brynjolfsson 团队确认;且 EIG 明示用 "an equal weight scheme",与 Canaries 的聚合口径未必逐格相同。
  - **精确的「假独立」表述(必须按此收窄)**:「共享 Eloundou GPT-4 β 这一个构念的,是 **Canaries 与 EIG 这一对**,以及 **Anthropic 2026-03-05 劳动力市场报告的 coverage 测度**(其原文:'Task-level exposure estimates from Eloundou et al. (2023)... Eloundou et al.'s metric, β, scores tasks on a simple scale: 1... 0.5... 0')。**Anthropic Economic Index 的使用量数据本身在构造上与 Eloundou rubric 相互独立**;Canaries 的**结果变量**(ADP 工资单微观数据,数百万工人月度就业)也与二者完全无关,是真正独立的一手数据。因此这些研究共享的是**自变量/分组构念**,不是数据或结论:它们能互相印证的是『按这套暴露度分组后就业出现分化』,不能互相印证『这套暴露度衡量的确实是 AI 影响』。」
  - **传导链上最硬的一条**:Canaries 与 EIG 用的都是 **GPT-4 β**,而 Eloundou 论文自己写明 "In this analysis, we present results from human annotators as our primary results."——两篇下游研究采用的正是原作者不当作主结果的那一套机器标注(与人类 β 的一致率仅 65.6%、Pearson r=0.591,且把 86 个职业标为 fully exposed,是人工 15 个的 5.7 倍)。Canaries 将其描述为 "ChatGPT validated with human labeling",与原作者的主次关系是**倒置的**。
  - **一条比「假独立」更能承重的独立检验**:Anthropic 2026-03-05 报告同页写着 "Interestingly, there is no such correlation using the Eloundou et al. measure alone."——即 Eloundou β 单独使用时,与 BLS 2024–2034 就业增长预测**不相关**;那条 0.6pp 关系只存在于 Anthropic 自建的复合 coverage 指标(理论可行性 × 实际用量 × 自动化加权)。
  - **前趋势/安慰剂问题**(Robustness 章 "Longer Sample" 段,配 Figure A16):"A concern is that for the Eloundou et al. (2024) measures the most exposed quintile had slower employment growth starting around 2020. This is not the case for the Anthropic exposure measures, shown in Figures A17, A18, and A19."——**必须带上下文**:该段紧接在 "Figure A16 shows results when extending the balanced sample of firms to 2018. This reduces the sample size and makes the data somewhat noisier." 之后,**不是主样本结果**。
  - **低使用量分位的数据稀薄问题(方向别写反)**:脚注 17 逐字 "Occupations in the first two augmentation quintiles have very low Claude usage (0.01% and 0.09% of conversations **for the average occupation**, respectively), with a high share of conversations classified as neither automative nor augmentative. In contrast, occupations in the third through fifth quintiles average 0.47%, 0.39%, and 0.33%..."。即 0.01%/0.09% 属于 augmentation **最低**的两个五分位(最不具增强性的那一端),**不是最增强型分组**。问题性质是:被当作**对照/参照端**的那一组几乎没有数据支撑,整个 augmentation 梯度的低端是空的。automation 口径对照:最低组 0.05%、最高组 0.73%。作者补救:"Figures A9 and A10 show that automation and augmentation results are similar when dropping occupations with low overall Claude usage."
  - **版本必须标注**:EIG 那份 note 脚注 1 明说 "Our comments in this note were written about the original version of the 'Canaries' paper published on 26 August 2025.",而现行 Canaries 是 **2025-11-13 版**。三席均探测未见 2026 年更新版(Stanford 上传路径 404)。**即 EIG 的批评对象与现行版本不是同一份稿。**
- **证据分级**:多源证实(三席各自下载 Canaries 2025-11 版 PDF 与 EIG PDF 并 pdftotext 逐字检索,§3.2、脚注 14/17、Longer Sample 段、EIG 方法附注与脚注 1 三席结果一致);其中「Anthropic coverage 测度亦架在 Eloundou β 之上」为**单源已核**(仅一席回到 2026-03-05 页面逐字取得)
- **数字定版**:
  - **0.01% / 0.09% 必须连同 "for the average occupation" 这五个词一起引**,并与第三至五分位的 0.47% / 0.39% / 0.33% 并列。理由:脱离对照组时读者无从判断「稀薄」到什么程度;而丢掉 "for the average occupation" 会让人误以为是该分位全部职业的合计占比。
  - automation 口径的 0.05% / 0.73% 可选引,若引须与 augmentation 那组分开标明口径。
- **不得这样写**:
  - ❌「Canaries 的 augmentation **最低两个五分位…即最『增强型』分组样本极稀薄**」——**方向反了**。0.01%/0.09% 是最不具增强性的两组,是被当作对照端的那一侧。缺陷仍然严重,但描述必须反过来写。
  - ❌「三项研究整体共享同一套构念前提 / 彼此非独立」——推论过宽。Canaries 的结果变量(ADP 工资单)与 Anthropic Economic Index 的使用量数据在构造上都独立于 Eloundou rubric;共享的只是自变量/分组构念。
  - ❌ 把 Anthropic 2026-03-05 劳动力市场报告排除在链条之外——它的 coverage 测度本身就架在 Eloundou β 上,引用链实为 **Eloundou β → {Canaries 分组, EIG 反驳, Anthropic 自家位移风险测度}**,比原论断说的更长。
  - ❌ 引安慰剂/前趋势那句而不说它出自 "Longer Sample" 稳健性小节、作者同段自陈 "makes the data somewhat noisier"——会让该证据显得比原文更硬。
  - ❌ 把 EIG 的 "We understand this is the same basis..." 写成双方确认的事实——那是 EIG 的单方推断,且其用 "an equal weight scheme",聚合口径未必与 Canaries 逐格相同。
  - ❌ 不标注版本错位——EIG 批评的是 2025-08-26 初版,现行 Canaries 是 2025-11-13 版。
  - ❌ 引 Canaries 对 Eloundou 的描述 "ChatGPT validated with human labeling" 而不点明原作者以人工标注为主结果——这句把主次关系倒置了。
  - ❌ 把 Canaries / EIG 当作已发表研究——两者均为工作论文/智库 note,未过同行评审。
- **利益相关**:Canaries 的第二套自变量与 Anthropic 2026-03 报告的 coverage 均依赖 Anthropic 自有平台使用量数据(见 G20 的厂商口径判定);Eloundou β 出自 OpenAI 团队。**即整条引用链的两个构念源头分别是两家模型厂商**,链条中没有一个完全独立于厂商的暴露度测度。EIG 为独立智库,但其反驳复用了被批评方的同一构念。
- **待 Round 3**:**是**。①「Anthropic 2026-03-05 的 coverage 测度架在 Eloundou β 之上」只有一席回到原页逐字取得,是本条最关键的链条延长,需第二席独立坐实;②Canaries 是否存在 2026 年更新版,三席均以 404 为据(否定性证据),需反证搜索席从 SSRN/NBER/arXiv 等其他渠道复检,并确认 EIG 的批评是否已被新版回应。

---

## [G22] ⟨Canaries in the Coal Mine⟩ 的 16%:一个估计量、两次写法,且随数据窗口从 13% 漂到 16%

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED;三席均以一手 PDF 逐字比对)
- **锁定表述**:
  - 来源:Erik Brynjolfsson, Bharat Chandar, Ruyu Chen,《Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence》,**Stanford Digital Economy Lab / SIEPR 工作论文**,现行版**题名页日期 2025 年 11 月 13 日**(文件 CanariesintheCoalMine_Nov25.pdf);**未经同行评审、无期刊卷期页**,出版页标注 WORKING PAPER。引用时必须写「工作论文,未过审」。
  - **全文只有两个独立测量,不是三个**:
    - **口径 A(描述性,无任何控制)**:「for the highest two exposure quintiles employment for 22-25 year olds declined by **6%** between late 2022 and September 2025, while employment for workers aged 35-49 grew by **over 8%**」——分子分母是**最高两个**暴露五分位(不是单一最暴露五分位)、22–25 岁、2022 年末至 2025 年 9 月。
    - **口径 B(回归相对值)**:Poisson 事件研究,含 **firm-time + firm-quintile 固定效应**,基准组 = 暴露五分位 1(最低暴露),基准月 **2022 年 10 月**(方程 4.1 中 t = −1)。正文写「a **15 log point** decline in relative employment for the most AI-exposed quintiles compared to the least exposed quintile」;摘要/结论写 **16%**——「After conditioning on firm-time effects, young workers experienced a **16% relative employment decline** in the most exposed occupations.」exp(0.15)−1 ≈ 16.2%。**16% 与 15 log points 是同一个数,不可并列为两次独立测量。**
  - 摘要逐字:「Early-career workers (ages 22-25) in AI-exposed occupations experienced 16% relative employment declines, controlling for firm-level shocks」。
  - 年龄异质性逐字(取导言版,须标明出处):「Estimates for other age groups are **generally** much smaller in magnitude and not statistically significant.」(正文 §4.4 含 generally;引用时不得漏字)
  - 单职业描述值:「By September 2025, employment for software developers aged 22-25 declined **nearly 20%** compared to its peak in late 2022.」
  - **样本与分母(须自足写出)**:ADP 薪资数据;「ADP observes job titles for about **70%** of workers in its system. We exclude workers without a recorded job title.」;保留「companies that have employee earnings records for each month from **January 2021 through September 2025**」;结果为每月约 **350 万–500 万**在职劳动者记录(「records on 3.5 and 5 million workers each month for our main analysis sample」)。ADP 自陈偏差:「the distribution of firms using ADP services does not exactly match the distribution of firms across the broader US economy」,脚注 13 更硬——ADP「somewhat overrepresents firms in the **Northeast**」且「firms using ADP tend to **grow faster on average** than the typical firm in the US economy」。
  - **作者自设因果边界(须原样保留)**:「we caution that the facts we document may in part be influenced by factors other than generative AI. Taken as a whole, our results are consistent with the hypothesis that generative AI has begun to affect entry-level employment.」
  - **版本漂移(必须写进文章)**:初版**2025 年 8 月 26 日**,摘要逐字「early-career workers (ages 22-25) in the most AI-exposed occupations have experienced a **13 percent** relative decline in employment even after controlling for firm-level shocks」;现行版(2025-11-13)为 **16%**。漂移机制由作者本人 2026-02-09 博文自陈:「With the fixed-effect approach, the employment changes start later, but they are growing (**reaching about 16% by October 2025, vs 13% in our paper with data only through July**), and they have not shown a reversal.」→ **同一设定、数据窗口延长 + 效应本身在增长,不是换方法**。两处需注明的不整齐:① 博文说「by October 2025」而论文数据窗口截至 **2025 年 9 月**;② 截至 **2026-07-24**,斯坦福自家 **SIEPR 工作论文页摘要仍写「a 13 percent relative decline」**,而 Digital Economy Lab 的 PDF 与出版物页写 16%——**同一机构两个官网挂着两个互相矛盾的头条数字**。原 2025/08 路径的 PDF 现已直接返回 Nov25 文件(一席比对 MD5 一致),初版仅可从 Wayback id_ 快照取得。
  - **2026-02-09 后续博文:必须两面都写。** 让步只在**时点**上:「When we explore a more stringent approach to control for other factors, the employment decline is significant only after 2024.」(同文另有更清楚的写法,建议改引:「starts in 2024, not late 2022 or 2023」);在**利率渠道**上作者明确**不让步、是反驳**:「we find evidence that more AI-exposed jobs are actually **less** exposed to interest rates on average」「we do not find strong support for the hypothesis that interest rate changes explain the disproportionate decline」。
- **证据分级**:**单源已核**(三席各自 pdftotext 逐字命中,但承重数字只有 Stanford/ADP 这一个来源与一份**未过审工作论文**;版本漂移部分为多源证实——初版 Wayback 快照 + 作者博文 + SIEPR 页三处交叉)
- **数字定版**:
  - **文章主引 16%**,并**必须**同句写明:「= 15 log points,同一事件研究估计的两种写法;相对最低暴露五分位;含 firm-time 与 firm-quintile 固定效应;数据截至 2025 年 9 月」。理由:16% 是现行版摘要与结论的头条数字,也是 EIG 2026-01 正文改引的数字,是当前流通口径。
  - **13% 与 16% 须并列呈现**,写法固定为「工作论文初版(2025-08-26)13% → 现行版(2025-11-13)16%,同一设定、数据窗口由截至 7 月延至 9 月;作者自陈效应仍在增长;斯坦福 SIEPR 页至 2026-07 仍挂 13%」。**不得只写一个数字而不说版本。**
  - **6% 不与 16% 并列成序列**:6% 是最高两个五分位的描述性绝对变动,16% 是相对最低五分位的回归值,**分母与对照组都不同**。
- **不得这样写**:
  - ❌「论文给出三个不同口径的数字互相印证(6% / 16% / 15 log points)」——三席一致指认:16% 与 15 log points 是同一个估计量,这样写等于把同一个数**数了两次**,人为制造交叉印证。
  - ❌「22–25 岁在**最暴露职业**的就业下降 6%」——原文是**最高两个**暴露五分位。
  - ❌ 把「+6% 至 +9%」当作正文对照数——它只出现在**导言**(「compared to a 6-9% increase for older workers」);正文 Fact 2 的对照是 35–49 岁「grew by **over 8%**」。用「+6%~+9%」必须标明是导言口径。另注:「5-13%」那个区间是**按暴露五分位**、不是按年龄,不得混用。
  - ❌ 引「Estimates for other age groups are much smaller...」而漏掉 **generally**。
  - ❌ 把「more AI-exposed jobs are actually less exposed to interest rates」写成作者的**让步**——它是作者对 EIG 利率解释的**反驳**。让步只在时点一处。
  - ❌ 把基准写成笼统的「2022 年末」——事件研究基准月是 **2022 年 10 月**。
  - ❌「截至 2026 年 7 月 Fortune 等媒体仍在引 13%」——**三席无一独立核实**(两席明说未回到原文/配额耗尽)。要写「仍在流通的旧数字」,请改挂已核实的 **SIEPR 官网页**,不要挂媒体。
  - ❌ 以「研究显示/论文证明」的语气承载 16%——它出自**未过审工作论文**,且作者自设了「may in part be influenced by factors other than generative AI」的边界。
- **利益相关**:数据由 **ADP** 提供、经费由 **Stanford Digital Economy Lab** 支持(致谢逐字:「We are grateful to ADP for access to the data and the Stanford Digital Economy Lab for financial support」)。ADP 客户企业增长快于全美典型企业、东北部超配——**这是分母偏差,不只是「谁给的数据」**。
- **待 Round 3**:**是,且必须送双席审计。** 理由:16% 是本篇最承重的单源实证,来自**未过审工作论文**,且**数字本身在移动**(13→16),同一机构两个官网口径打架。
  - **方法学审计席(有否决权)**须审:① Poisson 事件研究设定(firm-time + firm-quintile 固定效应)是否足以排除企业层面需求冲击;② 以暴露五分位 1 为基准组的可比性(平行趋势);③ ADP 样本选择——仅保留 2021-01 至 2025-09 每月连续在册企业 + 剔除无职位名称的 30% 劳动者,两道筛选如何影响年轻雇员的进入/退出计数;④ 「16% 随数据窗口增长」是效应增长还是样本组成变化;⑤ 作者 2026-02 自陈的「显著性起点移到 2024 年」对原叙事(2022 年末起下滑)的削弱程度。
  - **反证搜索席**须搜:独立团队 + 独立数据对同一现象的测量(至少覆盖 Humlum & Vestergaard 丹麦行政数据、Yale Budget Lab CPS、EIG 职位广告),并记录**是否存在用非 ADP 美国微观数据复现 16% 的独立结果**(目前无一席找到)。

---

## [G23] EIG《Looking for the Ladder》:反方一手扎实,但「与 Canaries 同源」是推定、两个采用率不是同一指标

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED;三席均逐字全文比对,一席称「本批最扎实的一条」)
- **锁定表述**:
  - 来源全称:Zanna Iscenko & Fabien Curto Millet,《**Looking for the Ladder: Is AI Impacting Entry-Level Jobs?**》,**Economic Innovation Group(EIG),American Worker Project,2026 年 1 月**(政策简报,非同行评审)。
  - 数据口径逐字:「more than **238 million** US job postings (averaging ~**3.3 million** monthly) from **September 2019 to August 2025**... across **767** 6-digit SOC occupational categories and **21** 2-digit NAICS industry sectors.」——「**超过** 2.38 亿条」,是下限不是精确值。
  - 暴露度构造逐字:「We calculate AI exposure quintiles using the data and code provided in the replication package for **Eloundou et al. (2024)**, using **GPT-4 β scores** and an **equal weight scheme**. **We understand** this is the same basis for exposure calculations as was used in Brynjolfsson et al. (2025).」——**「同源」是 EIG 的推定,不是双方核实**。且一席指出可能不严格成立:Eloundou 原文脚注 6/7 的职业级聚合把 O*NET **core 任务权重设为 supplemental 的两倍**(「Core tasks are given twice the weight of supplemental tasks, and all weights sum to one」),只有部分图用等权;Canaries §3.2 则直接取用已发表的职业级 β 测度。→ 写作口径:「EIG 用 Eloundou 复现包的 GPT-4 β 重算五分位、采等权重,并自称推定与 Canaries 同源;但 Eloundou 主口径对 core 任务加倍加权,两者是否严格同一未经双方核实。」
  - 时点论证逐字:「vacancies for the highest AI exposure quintile of occupations peaked in **March–April 2022** and declined sharply throughout the remainder of the year」+「This hiring slowdown **predates any plausible generative AI effect by over six months**.」
  - 共线性逐字:「Approximately **38 percent** of workers in the most AI-exposed quintile are employed in these sectors, compared to **less than 2 percent** in the least-exposed quintile.」(基于 **2023 Census data**)
  - 资历检验逐字:「There is **no evidence** that job postings for junior roles within occupations most exposed to AI have declined more than postings for senior positions.」
  - 核心主张逐字:「The most plausible explanation is that the data patterns observed are not early warnings of large-scale technological displacement, but rather the predictable consequences of a classic macroeconomic shock: **the sharpest monetary policy tightening cycle in four decades**.」
  - 自设边界逐字:「All this being said, **absence of evidence is not the same as evidence of absence**.」
  - **企业采用率:两个数不是同一指标,必须拆开。** 2023 Q4:「fewer than **10 percent** of large businesses surveyed were even **planning** to use AI in the next six months」(计划采用);2025 Q3:「adoption by large businesses has only climbed to **12 percent**」(EIG 自己未点明是 planned 还是 current,**不要替它断言**)。**「大企业」= 250 人以上**(脚注 2:「The largest business category in the U.S. Census Bureau's **Business Trends and Outlook Survey** covers companies with **250+ employees**」)。**建议主引脚注 2 更硬的那个数**:「fewer than **6 percent** of businesses with 250 employees or more reported **using** AI technologies in the past two weeks for the production of goods and services」——实际使用 <6% 比计划 <10% 更承重。
  - **射程自限(必须写)**:脚注 1 逐字「Our comments in this note were written about the **original version** of the 'Canaries' paper published on **26 August 2025**... We understand that Brynjolfsson and co-authors are helpfully continuing to update their analysis based on feedback they received, including from us, and we link to the latest version of their paper.」而 EIG **正文引的头条数字已是 16%**:「Its headline finding is striking: a **16 percent** relative decline in employment for early-career workers (ages 22–25) in the most AI-exposed occupations」。→ 唯一正确的写法:**分析基于 8 月版(13%),正文引用数字已换成 11 月版的 16%,EIG 自陈未针对更新版重做分析。**
  - **必须补的独立反证(EIG 立论支点被两方打脸)**:EIG 全篇支点是「AI 暴露度 ≈ 利率敏感度」。① Brynjolfsson 等 2026-02-09 用 Zens et al.(2020)原数据得出「more AI-exposed jobs are actually **less** exposed to interest rates on average」(作者自辩,方向可参考);② 更值得引的是**第三方**:**Yale Budget Lab(2026-05-07)独立测得**「AI-exposed occupations are generally **less sensitive to the business cycle** than unexposed occupations」,并把这一点写进 Key Takeaways。→ 共线性(38% vs <2%)成立**不蕴含**「利率敏感度更高」。
- **证据分级**:**多源证实**(三席各自 pdftotext 全文逐字比对,引语与数字全部一字不差命中;署名与致谢名单三席一致)。其中「EIG 暴露度与 Canaries 是否同口径」为**方向存争**(EIG 自称推定、一席据 Eloundou 脚注提出反例)。
- **数字定版**:
  - **企业采用率:文章主引「实际使用 <6%(250+ 员工,2023 Q4,过去两周用于商品/服务生产)」**,并列注「同期计划未来六个月使用者 <10%;2025 Q3 采用率 12%(EIG 未标明是计划还是实际)」。理由:三席中两席点名脚注 2 的 <6% 是同一份 BTOS 里口径最硬、最不含意向成分的一个,且能避免「<10% → 12%」被误读成同一序列。
  - **职位广告量写「超过 2.38 亿条」**,不写「2.38 亿条」。理由:原文是 more than。
- **不得这样写**:
  - ❌「普查局数据显示到 2023 Q4 大企业中计划用 AI 的不到 10%,到 2025 Q3 也只升到 **12%**」——把**计划采用**与**实际采用**两个不同指标串成一条时间序列。三席全部点名。
  - ❌ 不定义「大企业」——必须写 **250 人以上(BTOS 最大分组)**。
  - ❌「EIG 与 Canaries 用**同一**暴露度基础」——原文是「We **understand** this is the same basis」,是推定;且 Eloundou 主口径对 core 任务加倍加权,与 EIG 的等权重方案未必等同。去掉 hedge 就是替 EIG 断言。
  - ❌「EIG 批的是 13% 那版,所以已经过时」——EIG 正文引的是 16%。也 ❌「EIG 逐条打的是 Nov25 版」——分析写于 8 月版。只能用上面那句三段式表述。
  - ❌ 把 EIG 的共线性发现直接当作「AI 暴露职业对利率更敏感」的证据——EIG 自己没证明这一步,且有两个来源(含独立第三方 Yale Budget Lab)测得**相反**方向。
  - ❌ 只说「由 Google 首席经济学家撰写」就带过利益相关(见下)。
- **利益相关**:**极重且必须随数字出现。** 署名逐字:「**Zanna Iscenko is AI & Economy Lead, Chief Economist's Team, Google; and Fabien Curto Millet is Chief Economist, Google.**」致谢逐字含 **Ruth Porat(Alphabet 总裁兼 CIO)、Kent Walker(Alphabet 总法律顾问)、James Manyika(Google SVP)** 三位 Google 高管,另有 David Autor、Diane Coyle、Mohamed El-Erian、Michael Spence 等(研究助理 Guillaume Aimard)。即:**「AI 没在杀入门级岗位」这一侧的厂商指纹比另一侧更深。** 旁证该报告已进入学术流通:Humlum & Vestergaard 2026-03 版参考文献已正式引用 Iscenko and Curto Millet (2026)。
  文本质量旁注(可用可不用):EIG 脚注 3 把 Daniel Rock 的名字印成「Daniel Rockloundou」。
- **待 Round 3**:**是(限一项)**。需**方法学审计席**判定:EIG 的「GPT-4 β + 等权重」五分位与 Canaries 所用的 Eloundou 职业级 β 测度**是否为同一暴露度排序**(可比对复现包的 core/supplemental 加权)。这决定文章能否说「两篇用同一把尺子量出相反结论」——这句话若不成立,整段对垒的叙事强度要下调。其余部分不需 Round 3(三席逐字全中)。

---

## ⚠️ [G24] 三份「反方证据」全部引错版本:Yale 日期与出处、H&V 已改题、Johnston & Makridis 三个系数全错

- **判决**:**REFUTED(2 CORRECTED / 1 REFUTED;第 3 席对 C 段判 REFUTED,第 2 席判 C 段 UNVERIFIABLE,第 1 席取得全文后逐条判错)**。三席方向一致:**原表述的三段证据没有一段可以按原样使用**;综合取最严格者,本条按 REFUTED 处理,原稿三段全部重写或删除。
- **锁定表述**:
  - 【A · Yale Budget Lab】**必须先解决出处冲突,再落笔。** 三席对该机构的出版物清单描述不一致:
    - 第 1 席称取得 **《Tracking the Impact of AI on the Labor Market》,题头「Published: April 16, 2026 / Updated: April 16, 2026」**(PDF 直取),并称四条引语与四个基准日期全部逐字命中。
    - 第 2、3 席均称 **Budget Lab AI 专题页不存在 2026-04-16 条目**;引语实际出自 **《Evaluating the Impact of AI on the Labor Market: Current State of Affairs》(Gimbel, Kinder, Kendall, Lee),2025 年 10 月 1 日**;第 3 席另称该报告已被 **2026-06-15 的交互式追踪器《Tracking the Impact of AI on the Labor Market》** 接替,且追踪器 Key Takeaways 已改写。
    - → **锁定处理:在 Round 3 定版前,文章不得标注该报告的具体日期。** 可确认为逐字属实的引语(三席交集):「While the occupational mix is changing more quickly than it has in the past, it is not a large difference and **predates the widespread introduction of AI** in the workforce.」/「Currently, measures of exposure, automation, and augmentation show **no sign of being related to changes in employment or unemployment**.」/「our analysis is **not predictive of the future**.」
    - 方法与基准可确认:**Duncan & Duncan 相异性指数 + 12 个月移动平均**,对照期 **1984–1989(PC)/ 1996–2002(互联网)/ 2016–2019(对照)/ AI baseline Nov 2022**;比较的年龄口径是**应届毕业生 20–24 岁 vs 25–34 岁**。
    - **应届生那处「异动」必须带原文自限**:原文对应处为「The dissimilarity has increased slightly faster in recent months than it did in a previous time period, which could be consistent with a recent paper from Brynjolfsson et al.... **It could also simply reflect a slowing labor market.** However, **our results should be interpreted with caution particularly given small sample sizes**.」以及「the dissimilarity between older and more recent college graduates **rarely deviates outside of the 30-33% range**」。
    - **Yale 手上更有承重力的那份必须用**:另一篇《What We Do and Don't Know About How AI is Affecting the Labor Market》(2026-05-06/07,Gimbel/Kendall/Nunn;第 1 席另引题为《AI Is Probably Not (Yet) the Reason for Labor Market Weakening》的同机构分析)采用 **synthetic difference-in-differences** 做正式因果识别:「The estimate is **close to zero and cannot be distinguished from it**, statistically speaking.」;失业率侧逐字「AI-exposed unemployment has risen somewhat more than unemployment of the comparison group, though the difference is **not statistically significant**」,全样本约 +0.5 个百分点、**16–34 岁**子样本更大,「both are statistically insignificant **as of the first quarter of 2026**」;年轻人结论逐字「finding **mixed evidence** of AI effects for this group... this is a much **broader group** than the early career subgroup」。
  - 【B · Humlum & Vestergaard】**现行版**:《**Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI**》,**2026 年 3 月 13 日**,**NBER Working Paper w33777**(Issue Date May 2025 / Revision Date March 2026),扉页注「previously circulated under the title 'Large Language Models, Small Labor Market Effects'」,状态 **Under Review(未过审)**。
    - 现摘要逐字:「using difference-in-differences, we estimate **precise null effects on earnings and recorded hours** at both the **worker and workplace levels**, ruling out effects **larger than 2%** two years after the launch of ChatGPT.」——**结果变量是 earnings 与 recorded hours(及职场层面),不是个人雇佣状态**。
    - 样本口径:2023 年 11–12 月与 2024 年 11–12 月两轮,每轮邀请 115,000 人、约 **25,000** 份有效问卷、**7,000** 家职场、**11** 个高暴露职业(丹麦)。
    - **early-career 章节在现行版 §3.4 + 附录 D.2**(2025-07 版确无,采集者未定位到是对的)。正确口径逐字:「While we **replicate the pattern of declining early-career employment** in exposed occupations in Denmark, our difference-in-differences analysis reveals that the declines are **not driven by firms adopting AI chatbots**.」「estimates precise enough to **rule out effects greater than a third of a percentage point**」;脚注 21 自算 AI 采用至多解释 **0.43×0.33 ≈ 0.14 个百分点**,而 2022-10 至 2024-12 入门级份额总降幅约 **0.6 个百分点**(约四分之一)。→ 这是**归因否定,不是现象否定**。
    - H&V 自己也写明这批下降「whose connection to generative AI is itself debated (Frank et al., 2026; **Iscenko and Curto Millet, 2026**)」。
  - 【C · Johnston & Makridis】**原稿三个系数全部作废。** 现行版:《**AI, Output, and Employment**》,Andrew C. Johnston(UT Austin)& Christos A. Makridis,**SSRN 5375017,posted 1 Aug 2025 / last revised 25 Mar 2026**;镜像版本 **CESifo Working Paper No. 12579,2026-03-25,55 页**(未过审)。
    - 现行摘要逐字:「A one standard deviation increase in exposure raises **output by 7%**, with effects emerging in **2021** when enterprise AI tools entered the market. Employment effects follow the same timing but **diverge by exposure type**: where AI likely requires human collaboration, **employment rises 4%**; where AI can perform tasks independently, **we find no significant employment effect**. Results are robust to state-by-year and industry-by-year fixed effects and suggest AI has caused a **decrease in the labor share of income**.」
    - 正文(第 1 席取得 ifo 镜像全文)§5.1 逐字:「raises **sector output** by roughly **10 percent** by the end of the sample」——10% 是**2024 年端点值**,不是全样本平均,且结果变量是**产出(BEA 实际增加值)**,不是生产率。§5.2 逐字:「By 2024, a one standard deviation increase in exposure is associated with a **4.8 percent increase in the wage bill** (p < 0.01), a **3.9 percent increase in employment** (p < 0.01), and a **2.6 percent increase in establishments** (p < 0.05).」——**4.8% 是工资总额(wage bill),不是工资**;作者自算个人层面(ACS)**小时工资仅 +1.0–1.1%**,并称「only about 29% of the AI-induced [output gains accrue to labor]」、劳动份额每标准差下降 5 个百分点。
    - 数据源:产出 **BEA**;就业与工资总额 **QCEW**(「covers over **95%** of all U.S. wage and salary jobs」);个人工资 **ACS**。
    - **效应始于 2021 年、早于 ChatGPT**(「effects emerging in 2021 when enterprise AI tools entered the market」)——这削弱它作为「生成式 AI 正面效应」的证据力,且**与 EIG 的时点论证同向**,不能只当 Canaries 的反方。
  - Canaries **脚注 9** 对该文的反驳引语**逐字无误可原样使用**(结尾还有「(Hampole et al., 2025)」),但它针对的是该文**旧版**结论,并置时必须说明。
- **证据分级**:
  - A:**单源已核 + 出处存疑**(引语逐字属实,但日期/出处三席不一致,一处「引语」两席查无实据)。Yale 的 SDID 结论为**单源已核**。
  - B:**单源已核**(丹麦行政数据 + 两轮调查,现行版三席逐字一致;未过审,**版本已改题、关键区间由 1% 放宽到 2%**)。
  - C:**方向存争 / 版本漂移严重**(第 1 席取得 CESifo 镜像全文,第 2 席全路径 403 判 UNVERIFIABLE,第 3 席据现行摘要判三系数作废;正文级系数仅一席取得)。
- **数字定版**:
  - **H&V 的精度区间定版为 2%**(「ruling out effects larger than **2%** two years after the launch of ChatGPT」,2026-03-13 版)。理由:1% 出自已被取代的 2025-07 稿;**版本更新使区间放宽一倍,这是实质性削弱,必须按现行版写**。
  - **H&V 的 early-career 精度定版为「rule out effects greater than a third of a percentage point」**(职场层面早期职业就业份额),并同时给出脚注 21 的 **0.14pp / 0.6pp ≈ 四分之一**这个可承重的量级。
  - **Johnston & Makridis 的产出效应定版为 7%**(现行摘要头条,全样本口径),**10% 只能作为「2024 年端点值、正文 §5.1」附注**。理由:摘要口径是作者自己选定的头条数,10% 是端点值,单引 10% 会系统性高估。
  - **就业效应须并列呈现,不得取合并值**:「需人机协作型暴露 **+4%**;AI 可独立完成型 **无显著就业效应**」;**3.9% 是合并值,仅可作为正文层面的括注**。
  - **「工资 +4.8%」作废,改为并列两条**:「工资总额(wage bill)+4.8%」与「个人层面小时工资 **+1.0–1.1%**(ACS),同时劳动收入份额下降(每标准差约 5 个百分点)」。理由:对准大学生读者,「工资涨 4.8%」与「小时工资涨 1% 且劳动份额下降」是**完全相反的两条建议**——三席中判得最严的一席称这是本批**最危险**的一处。
  - **A 段日期不定版**:两席称不存在 2026-04-16 版本、一席称直接取得该日期 PDF。→ **须并列呈现为「出处待定」,Round 3 前不写具体日期。**
- **不得这样写**:
  - ❌「Johnston & Makridis 发现 **生产率 +10%**」——双错:结果变量是**产出**不是生产率;10% 是 2024 年端点值,摘要头条是 **7%**。(产出 +10% 搭配就业 +3.9%,隐含劳动生产率约 +6%。)
  - ❌「**工资 +4.8%**」——4.8% 是**工资总额**。个人小时工资仅 +1.0–1.1%,且劳动份额在**下降**。这是全批最危险的一处口径错。
  - ❌「就业 **+3.9%**」不加区分地使用——现行摘要已按暴露类型拆分,**AI 可独立完成的类型无显著就业效应**。
  - ❌ 把该文当作「AI 对就业净正面」的单向反证——现行摘要同时报告**劳动收入份额下降**,且第 2 席另引摘要句「However, sectors where AI can **directly substitute** for human labor saw **employment reductions**」「Wage gains are concentrated among **younger and more educated** workers」。结论是**条件性**的。
  - ❌ 写「效应期为 2017–2024」——摘要称效应自 **2021 年**出现(企业级 AI 工具进入市场),**早于 ChatGPT**。
  - ❌「匹配 QCEW 官方全覆盖行政数据」——漏了 **BEA(产出)与 ACS(个人工资)**,三个数据源分属不同结果变量。
  - ❌「Humlum & Vestergaard 的置信区间可排除 **1%** 以上的效应」/ ❌ 引「Modest productivity gains (**3% time savings**)」/ ❌ 引「Our findings **challenge narratives of imminent disruption**」——三者**全部出自已被取代的 2025-07 稿**;现行版区间为 2%,3% 与该句均已从摘要删除(旧稿正文实为「average time savings amount to **2.8%** of work hours」),现行版结句为「Technological change reshapes work well before it surfaces in earnings or hours.」
  - ❌「H&V 发现 AI 对入门级岗位是**零效应**」——EIG 与 Canaries 的这个简写是**误述**。原文复现了入门级就业下降,零效应指的是「采用 AI 的职场 vs 未采用职场无差异」这一**渠道**。现象否定 ≠ 归因否定。
  - ❌「Yale Budget Lab 报告显示 2026Q1 青年失业率上升迹象统计不显著」挂在相异性指数那份报告上——**该报告没有任何青年失业率显著性检验**(两席全文 grep 确认)。该结论出自 Yale 的**另一篇 SDID 分析**,且口径是 **16–34 岁**、不是 22–25 岁,结论是「**混合证据**」而非「无效应」。
  - ❌「**唯一**异动」——原文是「The most notable difference」(最显著的差异)。且引用应届生异动时**必须**带上「could also simply reflect a slowing labor market」与「small sample sizes」两句自限。
  - ❌ 逐字引用「an uptick in the dissimilarity of occupational mix between older and younger college graduates, though this remains at the high end of the historical range」——**两席在 2025-10 报告与 2026-06 追踪器中均查无此句**。Round 3 定版前不得作为逐字引语使用。
  - ❌ 只引 Yale 的相异性指数(纯描述性)而不引其 **SDID 因果估计**——等于弃用 Yale 手上更有承重力的那份证据。
  - ❌ 把三份「反方」并列成一条统一战线——A 的现行版结论是「no sign of being related」但方法是描述性;B 是归因否定而非现象否定;C 的效应早于 ChatGPT 且伴随劳动份额下降。
- **利益相关**:Makridis 的 SSRN 挂靠含 **The Gallup Organization**;Johnston 现职 University of Texas at Austin。H&V 2026-03 版致谢同时感谢 **OpenAI Economic Research Conference** 与会者,并披露「Caspar Ringhof and **Claude Code (Opus 4.6)** provided excellent research assistance」。Yale Budget Lab 为大学附属政策机构,无直接厂商利益。**三篇均为未过审工作论文/政策简报。**
- **待 Round 3**:**是(本批优先级最高之一)**。
  - **反证搜索席**:① 确认 Yale Budget Lab 的出版物序列与准确日期(是否存在 2026-04-16 版《Tracking the Impact of AI on the Labor Market》,还是 2025-10-01 报告 + 2026-06-15 追踪器两件),并定位「high end of the historical range」那句的一手出处或判定其不存在;② 确认 Yale SDID 那篇的准确题名与日期(第 1 席与第 2/3 席给出的题名不同)。
  - **方法学审计席(有否决权)**:审 Johnston & Makridis 的正文级系数——目前**只有一席取得全文**(ifo/CESifo 镜像),另两席取不到,属单席孤证;须复核 §5.1/§5.2 的 7% vs 10%、4.8% wage bill、+1.0–1.1% 小时工资三组数字,并评估「效应始于 2021 年」对因果识别(DiD 处理时点)的影响。**未通过审计前,该文任何系数不得承重。**

---

## [G25] 三项研究测三个不同构念的对照表:结构成立,但四格口径必须重写

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - **表的骨架成立**:Eloundou et al.、Anthropic Economic Index、Canaries 三项研究回答**三个不同问题**,不能互为证据。核心附加论断「厂商在这场争论的**两端都有人**」**站得住**,且三席均认为可以写得更硬。
  - **Eloundou 那一格(利益相关)**:arXiv 2303.10130v5 扉页逐字「Tyna Eloundou¹, Sam Manning^{1,2}, Pamela Mishkin*¹, and Daniel Rock³ / ¹OpenAI ²OpenResearch ³University of Pennsylvania」→ **四位作者中三位署 OpenAI(Manning 兼 OpenResearch),第四作者 Daniel Rock 在宾夕法尼亚大学沃顿商学院,与 OpenAI 无隶属。** 写法定为这一句,比「主要作者为 OpenAI 员工」更抗质疑。
  - **Eloundou 那一格(测的是什么)**:Canaries 与 EIG 用的都是 **GPT-4 β**,而 **β = E1 + 0.5×E2**。E1 逐字:「using the described LLM via ChatGPT or the OpenAI playground can decrease the time required to complete the DWA or task **by at least half (50%)**」;E2 逐字:「access to the described LLM alone would **not** reduce the time... by at least half, but **additional software could be developed on top of the LLM** that could reduce the time... by at least half」;0.5 权重的用意逐字:「intended to account for exposure when deploying the technology via complementary tools and applications necessitates additional investment」。「同等质量」的定义逐字:「a third party, typically the recipient of the output, would not notice or care about LLM assistance」。→ 该格写法:「理论上、在同等质量下,直接用 LLM 能把耗时砍一半的任务(E1),**加上半权重的**『再造一层软件后才可能砍一半』的任务(E2)」。
  - **Eloundou 那一格(不能推出)**:摘要逐字「**We do not make predictions about the development or adoption timeline of such LLMs.**」;正文另有「technical feasibility does not guarantee labor productivity or automation outcomes」。
  - **Anthropic Index 那一格(分母,必须带版本)**:Canaries 用的是 **Handa et al. (2025)= Index V1**(arXiv 2503.04761,2025-02),口径逐字「over **four million** Claude.ai conversations」;观测单位逐字「The unit of observation is a **conversation** with Claude on Claude.ai, **not a user**, so it is possible that multiple conversations from the same user are included.」;且**只含 Claude.ai 免费版与 Pro 版,明确排除 API、Team、Enterprise**:「We also only analyze data from Claude.ai **Free and Pro plans**, rather than API, Team, or Enterprise users.」→ 该格写法:「Claude.ai 免费版 + Pro 版**消费级对话数**(约 400 万次),不含 API/团队/企业流量;不是劳动者数,不是工时。」**Canaries 的 Fact 3(自动化 vs 增强)整个建立在这份消费级对话样本上。**
  - **Anthropic 自陈的限定(必须补进「不能推出」格)**:「we don't argue that the uses in our dataset are a **representative sample** of AI use in general」;「We **can't know for certain whether someone using Claude for a task was completing a task for work**.」第三方佐证:Yale Budget Lab 独立评估后写「data from Claude usage alone is **not representative** of how workers across the economy are using AI chatbots and tools」。
  - **「automation 上升」必须标版本**:**V1(2024 年末)的结论恰恰是增强占多数——57% augmentation vs 43% automation**;「automation 上升」出自 **V3(2025-09)**:directive 类对话「jumped from **27% in V1 in late 2024 to 39% in V3**」,且「This is the **first report where automation usage exceeds augmentation usage**」;V3 侧口径 automation 企业 API 约 **77%**、Claude.ai 约 **50%**。**V3 已另加一套 1P API 数据**(2025 年 8 月随机抽取的 100 万条 API transcript,与 100 万条 Claude.ai 对话**分开统计**)→ 若表格要涵盖 V3,「单一厂商平台使用日志分布」应写成「单一厂商的 **Claude.ai 对话 + 其 1P API transcript,两套分别统计**」。
  - **Canaries 那一格(分母,须收紧)**:不是泛指「ADP 覆盖企业的在职人数」,而是「**有职位名称记录**(ADP 只对约 70% 的劳动者观测到职位名称,其余剔除)、全职、有正收入、70 岁以下、且所在企业 2021-01 至 2025-09 **每月**都在 ADP 的在职人数」,每月约 **350 万–500 万人**。
  - **Canaries 那一格(利益相关,须加重)**:致谢逐字「We are grateful to **ADP** for access to the data and the **Stanford Digital Economy Lab** for financial support」;更要紧的是脚注 13:ADP「somewhat **overrepresents firms in the Northeast**」且「firms using ADP tend to **grow faster on average** than the typical firm in the US economy」。→ 该格写法:「ADP 提供数据;且 ADP 客户企业增长快于全美典型企业、东北部超配。」
  - **Canaries 那一格(不能推出,须加一句)**:「且该估计**随数据窗口变动**(截至 2025-07 数据 13% → 截至 2025-10 数据 16%),作者本人 2026-02 更新后把显著性起点移到 2024 年」——**该测量本身仍在移动**,表格若呈现为三项已定型的测量会制造虚假确定性。
  - **「两端都有厂商」可以写得更硬**:高暴露度那端 = Eloundou et al. 四位作者中三位是 OpenAI;「automation 上升」那端 = Anthropic 用**自家日志 + 自家分类器**;「AI 没在杀入门级岗位」那端 = EIG 报告由 Google 首席经济学家 Fabien Curto Millet 与 Google 首席经济学家团队 AI & Economy Lead Zanna Iscenko 撰写,致谢含 Ruth Porat、Kent Walker、James Manyika。旁证:Humlum & Vestergaard 2026-03 版致谢同时感谢 OpenAI Economic Research Conference 与会者,并披露「**Claude Code (Opus 4.6)** provided excellent research assistance」。→ **「厂商=夸大 AI 影响」这条启发式不成立;最深的厂商指纹恰在「AI 没在杀入门级岗位」这一侧。**
- **证据分级**:**多源证实**(作者归属、β 定义、Index 口径、Canaries 分母四项三席各自回到一手 PDF/官方页逐字命中,无冲突)
- **数字定版**:
  - **Index 分母定版为 V1 的「约 400 万条 Claude.ai 免费版+Pro 版对话」**,因为 Canaries 引的就是 V1(Handa et al. 2025)。理由:表格要说明的是 Canaries **实际用了什么**。注:Anthropic 官方发布页另有「approximately **one million** conversations」的说法(指该次分析的抽样规模),与论文摘要的「over four million」并存——**引用时以论文摘要的 400 万为准并注明官方页另有 100 万口径**。
  - **automation/augmentation 须并列两版**:V1 = 43% automation / 57% augmentation;V3 = directive 由 27%→39%,首次 automation 超过 augmentation。**不得只写一版。**
- **不得这样写**:
  - ❌「利益相关:**全部作者为 OpenAI**」——**Daniel Rock 在宾大沃顿,不是 OpenAI**。三席全部点名。一席直言:把一位学界作者写成厂商员工,对一篇教读者查利益相关的文章是自伤。(原稿「OpenAI 员工为主要作者」的写法本身**是对的**,只是不够抗质疑;不要改成「全部」。)
  - ❌ 把 Eloundou 的 β 说成「LLM 能把任务耗时砍一半」——**β 里有一半权重是 E2**,即「再开发一层软件之后才可能砍一半」的假想任务。这个简化**正好放大了这套数据的确定性**。
  - ❌「Anthropic Index 主张 automation 上升」不标版本——V1(Canaries 所用)的结论是**增强占多数**,与此打架;「automation 上升」是 V3。
  - ❌ 把 Index 的分母写成「Claude 对话总数」而不写**只含免费版/Pro 版消费级流量、排除 API/Team/Enterprise**——会高估其代表性。
  - ❌ 把 Canaries 的分母写成「ADP 覆盖企业的在职人数」——漏掉了 70% 职位名称筛选与「每月连续在册企业」两道限制。
  - ❌ 把这张表呈现为三项**已定型**的测量——Canaries 的估计仍随数据窗口移动。
- **利益相关**:三项测量分别由 **OpenAI(3/4 作者)**、**Anthropic(自有数据 + 自有分类器)**、**ADP + Stanford Digital Economy Lab** 支撑;对垒的另一侧(EIG)由 **Google 首席经济学家团队**撰写。**这张表本身就是「谁在说话、谁受益」的示范,厂商指纹须逐格标注。**
- **待 Round 3**:否(四格口径三席各自回到一手件逐字核对且无冲突;唯一与 Round 3 有关的是 Canaries 16% 本身,已挂在 G22 名下)。

---

## [G26] 蛛网模型的三份底座:NAE 附录 D 是教科书推演而非计量估计,0.67 与 Freeman 的数字都不能承重

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED;三席对「附录 D 无任何统计估计」「Freeman 具体数字 UNVERIFIABLE」完全一致)
- **锁定表述**:
  - 美国国家工程院(NAE)《Understanding the Educational and Career Pathways of Engineers》(2018,National Academies Press)**Appendix D, pp.180–181**:全长仅两页、仅一张 Figure D-1、**通篇无数据表、无回归、无系数、无弹性、无任何统计估计**,措辞是 "the market is **likely** to stay at point b"。Figure D-1 自注 "Adapted with permission from https://policonomics.com/cobweb-model"(一个经济学科普博客)。**文章必须写明这是教科书式静态图解,不得让读者误以为是 NAE 的计量结论。**
  - 「四年」的准确口径:是**假定的学位培养期**,且带条件句——"about four years (**if supply is dependent on new US graduates entering the market**, not a surge in engineers from offshore)";配套原句 "With the drop in wages, there is likely to be talk of a 'glut' of engineers four years after complaints of 'shortages.'"
  - 「一年」的准确口径:是**供给量可被改变的最短滞后**,不是整个调整期。原文 "Since the expansion in 1990 of the number of **skilled immigrant temporary visas** permitted, immigration has allowed just such a short cut to the equilibrium. The number of engineers can be changed with **no more than a year's lag (the time to apply for the annual visa distribution)**, so the long-run supply curve is flatter: **the cycles are both faster and associated with smaller wage changes**." 注意:原文说的是 1990 年移民法扩容的「技术移民临时签证」,**不专指 H-1B**;且最后半句(波幅同时变小)是必须保留的限定语——只讲「周期变快」不讲「工资波动变小」会夸大蛛网对学生的威胁。
  - Long, Goldhaber & Huntington-Klein,"Do completed college majors respond to changes in wages?",*Economics of Education Review* **49: 1–14 (2015-12)**,DOI 10.1016/j.econedurev.2015.07.007(**非 .003**)。可承重的定性结论(摘要逐字):学位完成数 "most strongly related to wages observed **three years earlier**, when students were college freshmen";异质性原文为 "women, blacks, Hispanics, and students with **low test scores** are **less likely to respond** to wage changes"(应写「更不容易随工资变动而调整」,原文未给显著性检验措辞)。
  - 0.67 的准确口径(第 2 席经 Wayback 取得接受稿全文后逐字核到,第 1、3 席均未取到):它是**某 6 位 CIP 专业占全部学士学位之份额**对**该对口职业的相对工资**(该职业 CPS 周薪均值 ÷ 全职业周薪均值,**不是「工资溢价」**)滞后三年的弹性;**不是回归系数,论文未报告任何标准误**——原文由加权平均边际效应 0.014 在加权平均专业份额 2.07% 处换算而来:"a 0.1 increase in relative wages would increase this average major's share from 2.07% to 2.21%, **for an elasticity of 0.67**";脚注 29 明写 "These regression results are not shown, but are available from the authors"。同段 **R²=0.02**——三年前工资只解释学位产出变异约 2%。作者自评 "modest"。
  - 时间窗:摘要写 1982–2012,但数据节为 **IPEDS 学位 1987–2011、CPS 工资 1983–2012**,以后者为准。异质性数值(男 0.023 / 女 0.009;白 0.016、亚裔 0.019 vs 黑 **−0.006**、拉美裔 **−0.003**;高 SAT 0.020 / 低 SAT 0.004)来自**华盛顿州 ERDC 行政数据 2007–2012、8 所公立大学 58,511 名毕业生**,不是全国序列;是 **SAT 分数**,不是泛指「测验分数」。
  - Beffy, Fougère & Maurel,"Choosing the Field of Study in Postsecondary Education: Do Expected Earnings Matter?",*Review of Economics and Statistics* **94(1): 334–347(2012-02)**;数值取自工作论文版 IZA DP No. 4127(2009-04)p.19 逐字:"simulating a **10% increase** in the expected earnings for each major yields low elasticities of respectively **0.09 for sciences, 0.14 for humanities and social sciences, and finally 0.12 for law, economics and management"。作者定性:"These elasticities appear to be **very low**, which means that the choice of a major is mainly driven by **non-pecuniary factors**";并自设限定 "still significant and **quantitatively small**"——**统计显著、量级小,不是零反应**;效应非线性,收入上升 20% 时约为 1.9 倍(脚注 29)。数据为法国 CEREQ **Génération 92 + Génération 98** 两轮调查,三阶段结构模型,测的是「专业选择概率」对「预期收入」。
  - 书目(经 Crossref 一手核实):Ezekiel M., "The Cobweb Theorem", *QJE* **52(2), 1938,起页 255**,DOI 10.2307/1881734;Freeman R.B., "A Cobweb Model of the Supply and Starting Salary of New Engineers", *ILR Review* **29(2): 236–248, 1976**,DOI 10.1177/001979397602900204。**只能写「Freeman 1976 将蛛网模型应用于工程师起薪与供给」。**
- **证据分级**:
  - NAE 附录 D 逐字与「无统计估计」判定:**多源证实**(三席分别从 nap/nationalacademies 两条路径取得全文,逐字一致)。
  - Beffy 0.09/0.14/0.12:**多源证实**(三席均从 https://docs.iza.org/dp4127.pdf 取到并逐字比对);但**取自工作论文版**,REStat 2012 发表版正文三席均未取得。
  - 0.67 / 0.014 / R²=0.02 / 脚注 29:**单源已核**(仅第 2 席经 Wayback 取得 Elsevier 接受稿 PDF;第 1、3 席经 ScienceDirect、CEDR WP、nickchk.com、ERIC、OpenAlex 全部 403/404,判 UNVERIFIABLE)。
  - Freeman 本人的周期长度与弹性数值:**未验证**(ILR/SAGE 403、Unpaywall is_oa=false、JSTOR 付费墙;Freeman 1975 AER 物理学家论文在 Crossref 中亦检索不到条目)。
- **数字定版**:
  - **0.67 → 可用,但必须整句带口径**:「学位份额对对口职业相对工资的三年滞后弹性约 0.67(由边际效应 0.014 在平均份额 2.07% 处换算,论文未报告标准误,R²=0.02)」。理由:第 2 席已回到接受稿一手逐字核到该数与其换算过程,证据层级高于另两席的「取不到」;但因三席中仅一席取得,分级只能停在单源已核,且不得省略换算与 R² 这两个削弱性限定。
  - **Beffy 弹性 → 定版 0.09 / 0.14 / 0.12(工作论文版口径)**,并注明「发表版为 REStat 94(1):334–347, 2012;本文数值取自其前身 IZA DP 4127,发表版正文未取得,若有微调以发表版为准」。理由:三席一致逐字核到,是本条唯一三席共同持有的一手数值。
  - **Freeman 的周期长度与弹性 → 无版可定,一律不写。**
- **不得这样写**:
  - ❌「NAE 2018 年报告**指出** H-1B 扩张把调整期压缩到约一年」——三重错误:(1) 附录 D 是模型推演不是机构结论;(2)「一年」是签证申请滞后即供给可被改变的最短时间,不是整个调整期;(3) 原文说的是 1990 年扩容的「技术移民临时签证」,不专指 H-1B。
  - ❌ 引 NAE「周期变快」而**省略** "associated with smaller wage changes"——删掉后会把报告的中性结论改造成对学生的警告。
  - ❌ 把「四年」写成 NAE 测出来的经验周期——它是 "if supply is dependent on new US graduates" 条件下的程式化培养期假设。
  - ❌「完成学位数对**对口职业工资溢价**的弹性 0.67」——分子是学位**份额**,分母是**相对工资**(职业周薪 ÷ 全职业周薪),不是溢价。
  - ❌ 给 0.67 配「标准误」「显著性」——论文未报告,回归表 "are not shown"。
  - ❌ 把 0.67 与 Beffy 的 0.09–0.14 并列成「**美国有弹性 / 法国无弹性**」的跨国对照——**第 2 席标为「本条最重要的推翻」,且 Long 等人自己就否掉了这个对照**。原文 p.23:Beffy 的**百分点效应更大**(10% 工资上升带来 0.25/0.53/0.40 个百分点),Long 自己只有 0.14 个百分点;弹性反过来纯因 Beffy 用 3 个大类(基数份额大)而 Long 用 6 位 CIP(平均份额仅 2.07%)。原文 "We find a smaller percentage point effect, but a larger elasticity than Beffy et al. (2012)… since they are evaluating relationships using aggregated major groups that have larger initial shares… They characterize their results as 'quantitatively small even though they are statistically significant' (p. 342), **and we largely share this conclusion**." **要么换成同口径(百分点效应)对比,要么删除该对照。**
  - ❌ 把 Beffy 读成「学生对收入毫无反应」——原文是 significant but quantitatively small。
  - ❌ 把 Long 的异质性结论(黑、拉美裔系数为负)当成全国长序列结果——它来自华盛顿州 8 校 58,511 人的行政数据(2007–2012)。
  - ❌ 给 Freeman 安上任何周期长度或弹性数值;❌ 引 Freeman 1975 AER 物理学家论文(Crossref 无条目,未获一手证实)。
  - ❌ 把 Long 论文 DOI 写成 10.1016/j.econedurev.2015.07.**003**(正确为 .007);❌ 把 Beffy 发表版标题写成带连字符的版本(原题为 "Choosing the Field of Study in Postsecondary Education")。
- **利益相关**:无(NAE 为国家科学院系统;两篇学术论文无厂商资助披露被提及)。唯一需标注的是 NAE 附录 D 的示意图源自商业科普网站 policonomics.com。
- **待 Round 3**:**是**。① 0.67 及其换算过程仅第 2 席一席取得(Wayback 上的 Elsevier 接受稿),需反证搜索席独立复现同一 PDF 并核对 0.014 / 2.07% / R²=0.02 / 脚注 29 四处;若无法复现,0.67 必须降级为「未经一手核对」或改用纯定性表述。② Beffy 数值取自工作论文版,需确认 REStat 2012 发表版正文的三个弹性是否有修订。③ Freeman 1976 全文若能取得,须补其周期长度与弹性;取不到则维持「不得写任何数字」。

---

## [G27] 法学院 2010–2013 塌方与 2025 反弹:三处硬错误,且 57.0%/10.1% 的证据层级只到「Wayback 上的 ABA 原始 PDF」

- **判决**:CORRECTED(3/3 票 CORRECTED;第 1、2 席 confidence=high,第 3 席 confidence=medium 且对多项判 UNVERIFIABLE)
- **锁定表述**:
  - **【硬错误必改】2025 年秋 1L 不是「约 38,000」**。ABA《2025 Standard 509 Information Report Data Overview》(2025-12-15 发布):Fall 2025 **Total First Year Enrollees 42,817**(较 2024 年 39,689,**+7.9%**),Total JD1 Cohort(含所有 1L)**43,721(+7.6%)**;Fall 2025 总 JD 在读 **120,039**(较 2024 年 115,410,+4.0%)。LSAC 官方博文(2026-04-08,Elizabeth Bodamer)逐字:"legal education welcomed its **largest first-year class since 2012**, an 8% increase over the 2024 incoming class"。**约 38,000 是 Fall 2023 前后的水平。此错方向性地削弱了文章立论——真实数据比原稿更强:下一轮扩张已落到入学端,不只在申请端。**
  - 「总 JD 在读较 2010 峰值低 18.6%」成立:120,039 / 147,525 = 81.4%,即 **−18.6%**(该式同时反证 2010 峰值 147,525)。
  - **1L 峰值应写 52,488,不是 52,404**:ABA 官方历史表《ABA Approved Law School Enrollment and Degrees Awarded Data 1963–2013》(enrollment_degrees_awarded.xls),2010–2011 学年 First Year Enrollment = **52,488**,Total J.D. Enrollment = **147,525**。
  - **申请件数应写 604,300 → 385,800,不是 602,300 → 385,400**:LSAC "Archive: 2000-2015 ABA End-of-Year Summaries",Fall 2010 申请人 87,900 / 申请件 **604,300**;Fall 2013 申请人 59,400 / 申请件 **385,800**;LSAC 自注 "Volumes are rounded to the nearest hundred",故 602,300/385,400 不可能是 LSAC 发布值。降幅 −36.2%,「三年 −36%」✓。
  - LSAT **171,514 人次** ✓:LSAC 表名即 "Total LSATs Administered—Counts & Percent Increases by Admin & Year",测试年度 2009–2010 合计 171,514(+13.3%),为该序列历史峰值。「人次」用词准确。
  - **2013 秋 1L 必须选定一个序列**:ABA 官方历史表 2013–2014 学年 First Year Enrollment = **40,802**,2012–2013 = 44,481,**YoY = −8.3%**;−10.8% 只有把 **39,675**(ABA 另一口径的 first-year class / matriculants)配上 44,481 才算得出;「回到 1977 年水平」的对照基准(该表 1977–1978 为 39,676)属于 39,675 那一支序列。**两支不得混用。**
  - **2013 届就业(论断 B)**:ABA 2013 年官方汇总表,Class of 2013 **Bar Passage Required 长期全职 26,653 = 57.0%**、**JD Advantage 长期全职 4,715 = 10.1%**;Class of 2012 为 26,066 = 56.2%、4,387 = 9.5%。**分母是 Total Graduates 46,776 全部毕业生**(表头 "%age of Total Grads"),不是「就业状态已知」的 45,695。测量时点由 ABA 2014 年表脚注坐实:"class of 2013 employment statistics **as of February 15th, 2014**";页眉写明 **"(9 months following graduation)"**。
  - **2025 届就业(论断 C)**:ABA Class of 2025 表,"EMPLOYMENT OUTCOMES **AS OF MARCH 16, 2026**";Bar Admission Required/Anticipated 长期全职 **29,928**、JD Advantage 长期全职 **1,815**;Total Graduates **36,206**(2024 为 38,937,**−2,731,−7.0%**);Total Employed 33,294(92.0%)。**ABA 自己发布的百分比是 89.9% 与 5.5%,分母是「已就业毕业生 33,294」**;82.7% / 5.0% / 87.7% 是以 36,206 为分母的**自算值**。ABA 2026-04 新闻稿逐字:"**31,743 or 87.7%** of the 2025 graduates of the **195 law schools**…were employed in full-time, long-term Bar Admission Required/Anticipated or J.D. Advantage jobs"(29,928+1,815=31,743 自洽)。**ABA 同时把类别名由 "Bar Passage Required" 改成了 "Bar Admission Required/Anticipated"。**
  - **三重不可比(拿 57.0% 与 82.7% 相减时必须全部写出)**:① 测量窗口不同——2013 届是毕业后 **9 个月**(2014-02-15),2025 届是毕业后 **10 个月**(2026-03-16);② 分母口径不同——ABA 2025 年表已把百分比分母改为「已就业毕业生」;③ 类别命名与全集不同——ABA 82.7%/87.7% 覆盖 **195 所(含波多黎各 3 所)**,Muller 的 **82.5%** 明写 "excluding Puerto Rico's three law schools"。
  - **Muller 口径(论断 D)**:Derek Muller, Excess of Democracy, 2026-04-23,逐字 "These are **ten-month figures from March 15, 2026**"、"a placement rate of **82.5%**, even as raw job totals **declined by around 2000 positions** year over year"、"Outcomes improved, but only because the Class of 2025 was **materially smaller** than the Class of 2024";大所条 "they **declined by 7%** year over year" 指的是 **101+ 律师事务所的岗位同比降幅**。毕业班规模的 **−7.0%** 出自 **ABA 表自身**("Total Graduates 36,206 / 38,937 / -2,731 (-7.0%)")。两个 7% 数值巧合,来源不同。
  - **LSAC 早期读数(论断 E)**:LSAC 博文(2025-10-13,Sudha Setty)逐字——"the total number of applicants is currently **up 33 percent**. Applications are **up 27 percent**"(基准为 as of early October),三处限定语 "this is **extremely early data**, and it should be viewed as **broadly directional at best**"、"we typically have only about **15 percent** of the total number of applicants and applications we expect to see by the end of the cycle"。**季末读数须另引 LSAC 2026-04-08 博文:全季申请人 "more than 76,000…highest volume of applicants since 2011 and an 18% increase"。**
  - **LSAC 自设的跨期不可比警告(拿 2010/2013 与 2026 周期对比时必引)**:LSAC 存档页逐字 "Data starting in **2016** include applicants for all terms and do not include deferrals; therefore, **archived data are not comparable to current data**."
- **证据分级**:
  - 2025 年 1L 42,817 / 总 JD 120,039、Class of 2025 与 Class of 2013 各计数、ABA 历史表 52,488/40,802/44,481:**多源证实**(第 1、2 席分别经 Wayback id_ 原始快照与检索层独立取得同一批 ABA 一手件,数值逐格一致)。
  - **57.0% / 10.1%:单源已核,但证据层级须写清——它停在「Wayback 存档的 ABA 官方原始 PDF(2014-07-02 快照)」这一层,不是 ABA 现役站点,也不是媒体转述。** 第 1、2 席均直接读到该 PDF 的逐行数字与页眉;第 3 席因 americanbar.org 全站 403、abarequireddisclosures.org 为 JS 空壳、web.archive.org 被其工具策略禁访、timetravel DNS 失效,**本轮判 UNVERIFIABLE,其唯一旁证是 Muller 文中对 "the Class of 2012's 56% placement rate" 的二手转述**。故:**并非「三席都只拿到媒体转述层级」——两席已回到一手 PDF;但因第三席无法独立复现,仍不能升为多源证实。**
  - LSAC 2025-10-13 三处限定语与 +33%/+27%:**多源证实**(第 1、2 席逐字取得;第 3 席未定位到该博文)。
  - 「到 2026-04 已超 75,000 人 / 此前四年平均约 59,000」:**未验证**(report.lsac.org/VolumeSummary.aspx 为 Power BI 动态报表,三席均抓不到;LSAC 2026-04-08 博文给出的是 "more than 76,000",与 75,000 不是同一表述)。
  - 「56% 招生官认为政治是主因」:**未验证**(三席一致确认不在 LSAC 该博文中)。
  - LawHub 口径断裂声明:**未验证**(三席均未在一手页面取得)。
- **数字定版**:
  - **2025 年秋 1L → 定版 42,817(+7.9%,ABA 2025 Standard 509 Data Overview)**;若须强调「最大一届」,配 LSAC 2026-04-08 的 "largest first-year class since 2012"。理由:ABA 官方发布件,两席独立取得。原稿 38,000 直接删除。
  - **1L 峰值 → 定版 52,488(2010–2011 学年,ABA 官方历史表)**,弃用 52,404。
  - **申请件数 → 定版 604,300 → 385,800(LSAC 存档表)**,弃用 602,300 / 385,400(与 LSAC「四舍五入到百」的自注不相容)。
  - **2013 秋 1L → 定版 40,802 / YoY −8.3%(ABA 官方历史表)**;若文章要保留「回到 1977 年水平」的修辞,必须改写为「按 ABA 另一支 first-year class 序列计为 39,675,与 1977–1978 的 39,676 相当」,并明说是另一口径。理由:统一到有官方历史表可查的那支序列,修辞让位于口径一致。
  - **2025 届 BPR 安置率 → 须并列呈现**:主用 **ABA 官方发布的 89.9%(分母=已就业毕业生 33,294)**,同时给出**以全部毕业生 36,206 为分母的 82.7%**,并注明 **Muller 剔除波多黎各三校后为 82.5%**。理由:三个数分属三种全集/分母,三席在此不一致(第 3 席甚至指 82.7% 无法回溯),取任何单值都会丢掉「ABA 中途改了分母」这一本文最想讲的口径教训。**若文章要与 2013 届的 57.0% 做时序对比,只能用同分母的 82.7%,且必须同时挂上三重不可比。**
  - **−7.0% → 定版为「毕业班规模同比 −7.0%,出处是 ABA Class of 2025 表自身」**;Muller 的 7% 单独写作「101+ 律师事务所岗位同比 −7%」。
  - **申请增幅 → 须并列呈现并各自标时点**:「2025-10(全季约 15% 进度)申请人 +33%、申请件 +27%」与「2024-25 全季申请人超 76,000、同比 +18%、为 2011 年以来最高」是两个时点的两组数,不得合并。
- **不得这样写**:
  - ❌「2025 年 1L 稳定在约 38,000」——硬错误,实为 42,817;且方向相反,会把「已起跳」写成「已回稳态」。
  - ❌「1L 峰值 52,404」「申请件数 602,300 / 385,400」——非官方发布值。
  - ❌「2013 秋 1L 跌至不足 40,000,较 2012 再跌 10.8%,回到 1977 年水平」——**混用两支序列**:−10.8% 需用 39,675 配 44,481,而「不足 40,000」与 ABA 历史表的 40,802 冲突。
  - ❌ 把 57.0% → 82.7% 直接相减说成「修复幅度」而不写三重不可比(9 个月 vs 10 个月、分母改口径、195 校含/不含波多黎各)——会**系统性高估修复幅度**。
  - ❌ 把 82.7% / 5% / 87.7% 说成「ABA 发布值」——ABA 发布的是 89.9% 与 5.5%(分母为已就业毕业生),82.7% 是自算。
  - ❌ 把 2025 届类别写成 "Bar Passage Required"——ABA 已改名为 "Bar Admission Required/Anticipated",跨年比较时这本身就是口径变更的一部分。
  - ❌ 把「毕业班规模 −7.0%」归给 Muller——那是 ABA 表的数;Muller 的 7% 是大所岗位跌幅。**第 3 席点名此处为「最严重」:把分子端跌幅误当分母端缩幅,会让「修复来自分母缩小」的论证凭空多出一个不存在的量化支撑。**
  - ❌ 把 2025-10 的三处限定语(extremely early / 约 15% / broadly directional)扣在 2026-04 的季末数字上——**算术上不可能成立**(季末不可能仍只占 15%)。
  - ❌ 写「到 2026-04 已有超 75,000 人申请、此前四年平均约 59,000」而不标来源——三席均未取得一手;LSAC 官方说法是 "more than 76,000…an 18% increase"。**该句应改用 LSAC 原文或删除。**
  - ❌ 写「56% 招生官认为政治是主因」——不在 LSAC 该博文中,三席均未定位到出处,**补源否则删**。
  - ❌ 把 LSAC 的归因简化为「政治+经济」——第 2 席指出博文 "What May Be Driving These Numbers?" 一节的**首要解释是结构性/时序性的**:"More law schools are now offering **early decision** programs and emphasizing **rolling admissions**, which may be creating a larger early surge in applications";政治/经济环境出现在另一节 "The Value of Legal Education",讲的是「为何现在很多人对法律教育有兴趣」,不是对早期激增的归因。
  - ❌ 直引 LawHub 那句口径断裂声明——三席均未取得一手。改述为「ABA 官方历史表止于 2013–2014 学年,之后为逐年 xlsx,序列需自行拼接」。
  - ❌ 把 171,514(施测人次)、604,300(申请件)、87,900(申请人)、52,488(1L 入学)、147,525(总在读)五种口径并排而不带单位标签——第 3 席特别提醒,读者会把「人次」与「件」当成同类量。
  - ❌ 拿 2010/2013 的 LSAC 存档数与 2026 周期数直接连线——LSAC 自己声明 2016 年起口径变更、"not comparable to current data"。
- **利益相关**:ABA 是法学院认证机构,其就业统计口径由自身制定并在 2025 年发生分母变更(由「全部毕业生」改为「已就业毕业生」),该变更方向对法学院有利,引用时须随数字标注。LSAC 是 LSAT 出题方与申请平台运营方,申请量增长与其商业利益同向,其「周期强劲」类博文属**机构口径**,方向可参考、程度不承重。Derek Muller 是独立法学教授(Notre Dame),其博客为二次分析,但方法披露充分。
- **待 Round 3**:**是,且这是本批次最必须送审的一条。**
  - ① **57.0% / 10.1% 必须送反证搜索席**:证据层级目前停在「Wayback 存档的 ABA 原始 PDF」,两席取得、一席因 web.archive.org 被禁访完全无法复现。需第三方独立路径(如 abarequireddisclosures.org 的年度汇总下载、ABA 现役站点镜像、或 NALP《Jobs & JD's: Employment and Salary of New Law Graduates, Class of 2013》作为独立机构交叉源)复核 26,653/46,776 = 57.0% 与 4,715/46,776 = 10.1%。**若无法取得第二条独立路径,成文中必须标注「据 ABA 2013 年官方汇总表(经 Internet Archive 存档件核对)」,不得省略存档层级。**
  - ② 「超 75,000 人申请 / 前四年平均约 59,000」与「56% 招生官认为政治是主因」两处**必须补源或删除**,需反证搜索席检索 LSAC Current Volume Summary 的静态导出或 ABA/NALP 二次统计。
  - ③ 2013 秋 1L 的 40,802 与 39,675 两支序列,需方法学审计席确认 ABA 两套定义(First Year Enrollment vs first-year class/matriculants)的差异来源,并裁定「回到 1977 年水平」这一修辞是否可保留。

---

## [G28] NIH ACD 2012 报告:引语与页码全对,但「26% 是 2012 年读数」是必须改的四年时效虚增

- **判决**:CORRECTED(3/3 票 CORRECTED,confidence 均为 high;三席对「终点是 2008 不是 2012」完全一致)
- **锁定表述**:
  - 一手件:NIH Advisory Committee to the Director《Biomedical Research Workforce Working Group Report》,**2012 年 6 月**(封面日期 2012-06-14,共同主席 Shirley Tilghman / Sally Rockey),157 页,https://acd.od.nih.gov/documents/reports/Biomedical_research_wgreport.pdf 。**版本提示**:附录 F 载有 "Participants in **June 21, 2012** meeting",流通版本晚于封面日期,引用时写「2012 年 6 月」较稳妥。
  - **【必改】终身教职比例的终点年份是 2008,不是 2012**。p.7 逐字:"Although the vast majority of people holding biomedical PhDs are employed (i.e. **unemployment is very low**), the proportion of PhDs that move into **tenured or tenure-track** faculty positions has declined from **~34 percent in 1993 to ~26 percent today**." 报告自陈其数据源 SDR 的缺陷,p.17:"the data are reported with a significant lag (**the most recent data available to the committee were from 2008**)";p.23 再述:"data from the SDR…**extends only through 2008**. Therefore, much of the information presented below about career outcomes does not take into account the past four years (including the recent recession)."(对应 Figure 12 区间为 1993–2008。)**正确写法:「从 1993 年约 34% 降至约 26%(报告原文作 today,但其底层 SDR 数据止于 2008 年,即该 26% 实为 2008 年读数,不含 2008–2012 衰退期影响)」。**
  - **类别口径**:是 "**tenured or tenure-track** faculty positions",即**已获终身教职 + 终身轨合计**,不只是「终身轨」。
  - **【建议替换,更贴题】** 第 3 席发现报告 p.23 有一个比 34%/26% 更直接的「对口率」证据:"across science and engineering PhD fields **60-80%** of graduates report that they are employed in occupations that are **closely related to their PhD field**. However, the percent in biomedical sciences **decreased between 1997 and 2008 from 70% to just below 59%**. Other fields do not show a decrease of this magnitude." **这才是「失业率不动、对口率塌方」的教科书级证据,应与 p.7 的 "unemployment is very low" 直接并置。**
  - 其余引语逐字与页码三席全部命中,可原样使用:
    - p.17:"The steep increase in the number of biomedical PhDs awarded began in **2004**, just after the end of the **doubling of the NIH budget (1999-2003)**. Given a **5-7 year training period**, this illustrates a close relationship between the size of the NIH budget and the number of biomedical PhD slots."
    - p.10(执行摘要,p.38 正文重复):"This creates a system in which a large number of future scientists are being produced each year, **well in excess of the number of research-oriented jobs** in academia, government and industry."
    - p.14:"As described later in this report, the data gathered by the ACD working group **do not indicate such growth in employment opportunities**. Rather, the numbers of positions available for biomedical PhDs that take advantage of their long training are **less than** the number of PhDs produced each year."
    - p.15(1998 年 NRC):"a study published by the National Research Council in 1998, **Trends in the Early Careers of Life Scientists**, chaired by Shirley Tilghman…The study concluded that the level of PhD production in 1998 **exceeded the availability of jobs**…The 1998 committee recommended **restraint in future growth** in the number of graduate students…It is notable that this report was released **just before the doubling of the NIH budget**, which may have affected the perception of the urgency of its recommendations."
  - **2011 年 NRC(Chalkley)报告的结论必须写全**:p.14 原文为该研究基于 "low unemployment rates of biomedical and behavioral scientists and models that predicted substantial growth in scientific employment opportunities over the next decade",结论是 NRSA 岗位数 "is adequate **and should remain at the same level in biomedicine and should be increased in behavioral sciences**"。报告全名《Research Training in the Biomedical, Behavioral, and Clinical Research Sciences》(p.75 脚注 58),主持人 Roger Chalkley(Vanderbilt)。**只写「够用」会漏掉「行为科学应增加」这一半。**
  - **SDR 的两条自陈缺陷(p.17,必写)**:"It **does not include information on foreign-trained doctorates** (an increasing share of the biomedical workforce), and the data are reported with a significant lag (the most recent data available to the committee were from 2008).";p.42 另补:GSS/SED/SDR 三大数据源 "omit large portions of the **postdoctoral** population",SDR 与 SED 仅含美国本土培养博士。
  - **补充数据(p.8,p.28 重复,三席逐字命中)**:"For PhDs graduating in **2001**, the median age for biomedical scientists was **32** and the median age for starting a tenure track position was **37**; comparable ages for chemistry doctorates were **30 and 33**.";"average starting salaries in **fiscal year 2011** for biomedical assistant professors were approximately **$68,000** compared to **$69,000 for chemistry**, **$79,000 for clinical and health fields** and **over $100,000 for economists**"。**薪酬数据源为 Oklahoma State University 对公立研究型院校的薪酬调查,不是 NIH 自采,引用必须注明。** 第 3 席建议:化学 $69,000 这个对照比经济学 $100,000 更能说明问题——同为自然科学、训练期更短,起薪却几乎一样。
- **证据分级**:**多源证实**(三席各自下载同一份 PDF,其中两席用 pdftotext -layout 全文抽取并按页脚 "Final Report N" 逐页定位页码,所有引语与页码三席一致);其中**关于 1998 年 NRC 与 2011 年 NRC 两份报告的一切内容为「单源已核 · 转引」**——三席均未取得这两份报告原文(1998 报告 NAP catalog record 6244 可达但全文需登录;2011 报告 grants.nih.gov PDF 未验证)。
- **数字定版**:
  - **26% 的时点 → 定版为「约 2008 年(报告原文作 today)」**。理由:报告自身在 p.17 与 p.23 两处明说底层 SDR 止于 2008,标成 2012 等于凭空多给四年时效,对准大学生是实质误导。
  - 对口率 → 定版 **70% → just below 59%(1997–2008,生物医学)**,并给出 S&E 全体的 60–80% 作背景。
- **不得这样写**:
  - ❌「终身教职轨道比例从 1993 年约 34% 降至 **2012 年**约 26%」——报告原文是 today,底层数据止于 2008;**三席全部点名此处**,第 1 席直言「把终点写成 2012 会把这条数据凭空拉近四年」。
  - ❌ 写成「**终身轨**比例」——原文是 "tenured **or** tenure-track",含已获终身教职者。
  - ❌ 引 34%/26% 而不同时交代 SDR 的两条自陈缺陷(不含外国培养博士、滞后至 2008)——这两条正是本案例「用对口率而非失业率」口径教训的一部分。
  - ❌ 把 2011 年 NRC 报告的结论写成单纯「NRSA 岗位够用」——原文还有「行为科学应增加」。
  - ❌ 把 $68,000 等起薪写成 NIH 数据——出自 Oklahoma State University 对公立研究机构的薪酬调查。
  - ❌ 把关于 1998 年 NRC 与 2011 年 NRC 的表述写成对两份报告原文的直接引用——**三席均未取得原文**,必须统一写「据 NIH ACD 2012 年报告转述」。
  - ❌ 只引经济学 $100,000 作对照而略去化学 $69,000——后者更能说明训练期与起薪脱钩。
- **利益相关**:该报告由 NIH 自身的顾问委员会出具,**是对 NIH 自家资助体系(预算倍增期扩招、NRSA 岗位规模)的自我检讨**——属「机构自证不利」类文本,可信度方向上偏强,但其政策建议部分仍是 NIH 内部立场,引用建议时须注明。共同主席 Shirley Tilghman 同时是 1998 年 NRC 报告的主持人,两份报告结论同向,**存在同一作者跨报告自我印证的问题,写「1998 年就警告过、2012 年再次警告」时应披露主持人是同一人**。
- **待 Round 3**:**是(轻度)**。1998 年 NRC《Trends in the Early Careers of Life Scientists》与 2011 年 NRC《Research Training in the Biomedical, Behavioral, and Clinical Research Sciences》两份报告原文三席均未取得,需反证搜索席尝试 NAP 全文(record 6244)与 grants.nih.gov PDF;**若仍取不到,成文中凡涉及这两份报告的表述一律写成「据 2012 年 NIH ACD 报告转述」,不得升级为直接引用。** 2012 报告本身无需再审(三席逐字逐页一致)。

---

## [G29] 石油工程学位崩塌:2,615 是行业自愿问卷数而非普查数,且官方序列在三席之间未能定于一

- **判决**:CORRECTED(3/3 票 CORRECTED;第 1、2 席 confidence=high,第 3 席 confidence=medium。**无 REFUTED,但第 1、2 席均以官方数据反证了原稿的两个具体数字,第 3 席则完全未能取得官方序列**)
- **锁定表述**:
  - **【调查主体与口径,本条最必须写清的一件事】** 2,615(2017 年峰值)、894(2022)、655/660(2023)、约 500(2024)、「开设院校 35 → 20 所」这一整组数字,来自 **Lloyd Heinze(Texas Tech University, Bob L. Herd Department of Petroleum Engineering)主持的年度自愿问卷调查**,经 SPE 会刊 *Journal of Petroleum Technology*(JPT)报道;**它不是 IPEDS/NCES 的联邦普查,而是各石油工程系自报的抽样统计,应答项目数逐年浮动**。第 3 席特别指出一处内在矛盾:**「2023 年仅 25 个项目回应」与「开设院校从 35 降到 20」两个数放在一起本身就不自洽(回应数 25 > 在办院校数 20)**,必须在文章中讲明,否则「降 75–81%」这个耸动区间会被当成普查结论。**注:「2023 年仅 25 个项目回应」本身第 2 席明确报告未能在一手件中核到。**
  - **JPT 2023-12-01 原文的准确表述**(Stephen Rassenfoss,《More Students Going Into Petroleum Engineering Programs as Research Work Tilts to Alternative Energy》):"**660 seniors expected to graduate** this year, down from a **peak of 2,615 in 2017**";"that number will drop to **572 in 2025** based on the number of juniors"。**即 660/572 是「预期毕业的大四/大三在读人数」,不是已授予学位数;原稿的「2024 年约 500」在该文中不存在。**
  - **2,550 的来源**:另一篇 JPT 文《Petroleum Engineering Enrollment Projected to Drop Sharply》称 "record-high **2,550** bachelor of science degrees awarded in petroleum engineering in 2017"。**2,615 与 2,550 不是两个口径的两个版本,而是同一 Heinze 调查在不同 JPT 报道中的两个说法。**
  - **官方 IPEDS 序列(CIP 14.2501,学士,first majors,全美)——两席取得但彼此错开一年,见「数字定版」**:
    - 第 1 席(直接下载 NCES 原始 C20XX_A.zip,筛 CIPCODE 前缀 14.25 / AWLEVEL=5 / MAJORNUM=1 求和 CTOTALT):2008 **521**、2009 690、2010 779、2011 1,030、2012 1,068、2013 1,130、2014 1,406、2015 1,688、2016 1,984、2017 **2,124**、**2018 2,151(峰值)**、2019 1,703、2020 1,123、2021 830、2022 **745**、2023 **623**、2024 **488**。
    - 第 2 席(Urban Institute Education Data API 镜像):2008 **690**、2009 779、2010 1,018、2011 1,068、2012 1,130、2013 1,406、2014 1,688、2015 1,984、2016 **2,124**、**2017 2,151(峰值)**、2018 1,703、2019 1,123、2020 1,123、2021 830、2022 **745**。第 2 席自陈 2019 与 2020 同为 1,123 可疑,建议用 NCES 原始文件复核;2023/2024 该 API 返回 500。
    - **两序列数值完全相同,整体错开一年**——第 1 席按「IPEDS 年份 = 学年结束年(2018 = 2017–18 学年)」标注。
  - **降幅**:以第 1 席口径,488 / 2,151 = **−77.3%**,落在原稿「75–81%」区间内;以第 2 席口径,745 / 2,151(2017)= **−65.4%**(该口径下 2023/2024 数据缺失)。
  - **【被官方数据反证】「开设院校从 35 所降至 20 所」方向相反**:IPEDS 中「当年至少授出 1 个石油工程学士学位」的机构数为 2008 年 **17 所** → 2017 年 22 所 → 2018 年 23 所 → 2022 年 **25 所**,一路上升(两席结论一致)。35→20 只可能是 Heinze 问卷中「设有项目 / 回应问卷」的口径,与「授予学位的机构数」不是一回事。
  - **油价(论断 B)**:FRED 日频 DCOILWTICO / DCOILBRENTEU——WTI **2014 年 6 月月均 $105.79**(月内最高 107.95),**2016-01-20 低见 $26.68**(全周期最低为 2016-02-11 的 $26.19);Brent 2016-01-20 为 $26.01。105.79 → 26.68 = **−74.8%**,「跌逾 70%」✓。
  - **滞后期**:油价 2014-06 见顶 → 学位峰值 **2017 学年(第 2 席口径,约三年)或 2018 学年(第 1 席口径,约三年半到四年)**。**该滞后是业内经验拟合,不是发表的计量估计——这一限定语必须留在正文,不能只放脚注。**
  - **JPT 专家讨论(论断 C)——逐字成立,但性质与时点必须写清**:《History Matching of Petroleum Engineering Graduation Rates》(Stephen Rassenfoss,**2022-03-01**),是 JPT 对**四位学者邮件讨论的新闻报道,属专家意见,不是研究**;其历史拟合数据覆盖约 **1940–2015 年**,底层来自 Lloyd Heinze 与 John C. Calhoun《A Brief History of a Petroleum Engineering Education in the United States》(**1991**)。逐字引语:
    - Mohan Kelkar(University of Tulsa):"I do not believe that oil prices are going to help us significantly in increasing the enrollment"(理由是石油公司招聘受抑 + 反化石燃料叙事已传导到高中生)。
    - Tom Blasingame(2021 年 SPE 主席):"we can't use these data to predict the next distributions"。
    - Ozkan:该类外推 "neither captures the effect of the changing conditions"。
    - 1984 年峰值:原文为 "The 'reference' trend shown (red) occurs over the period from 1970 to 2000, which **peaked at 1,587 BS graduates around 1984**"——**这是拟合高斯分布的峰值、且是 "around 1984",不是某一年的普查实数。**
  - **【时点限定,第 3 席发现】** 该文发表于 **2022 年 3 月**,**不含** 2017 年峰值数、不含 2022/2023/2024 年毕业数、不含开设院校数——因此它是**先于后续崩塌报道的方法论保留意见,而非事后修正**。正确写法:「SPE 旗下 JPT 早在 2022 年 3 月就已刊文警告价格—入学的简单外推不可靠」。**这个改法让论据更强:事前警告胜过事后找补。**
  - **【必须写进去的不利事实,第 2 席发现】** 同一 Heinze 调查在 2023 年 12 月已显示反转——那篇 JPT 的标题本身就是「**More Students Going Into Petroleum Engineering Programs** as Research Work Tilts to Alternative Energy」,正文 "There has been a **13% increase in the number of freshman and sophomore students**"、"undergraduate enrollment is **up at seven of the 10 largest programs** surveyed in the US and the Middle East"。**把石油工程写成单向崩塌、当作「滞后期最清晰」的样板,会掩盖它在 2023 年已进入下一轮上行段。**
  - **加分点(第 3 席)**:「石油工程已跑过不止一轮蛛网」由该 2022 年文章本身支撑——它做的就是 1940 年以来的历史拟合,1984 年 1,587 人即第一轮峰值。建议写成「至少两轮」。
- **证据分级**:
  - IPEDS 学位序列:**方向存争**——两席各自取得且**趋势形状完全一致**(同一组数值),但**峰值年份相差一年(2017 vs 2018)**,且取数路径不同(NCES 原始文件 vs Urban Institute API 镜像);第 3 席完全未取得(NCES Digest 表 325.35 实为计算机与信息科学表,d24 版 404,CIP 14.2501 需走原始文件或 Trend Generator,其工具不可达)。
  - 「授予学位机构数上升」:**多源证实**(第 1、2 席独立计算,方向一致)。
  - **2,615 / 2,550 / 894 / 35→20:未验证(一手层)**——第 1 席明确「承载这些数字的那篇 SPE JPT 文章未能定位」;第 2 席定位到 2023-12-01 那篇并核到 2,615 与 660/572,但**未核到 894、35→20、25 个项目回应**;第 3 席两个峰值数均未定案。
  - JPT 2022-03-01 的三条引语与 1,587:**多源证实**(三席逐字命中)。
  - "This time is different":**方向存争**——第 1、3 席在原文中命中,第 2 席明确报告未能逐字核到。
  - 油价:**单源已核**(第 1 席回到 FRED 一手日频;第 3 席自陈未回 EIA 一手核对)。
- **数字定版**:
  - **峰值 → 定版为「IPEDS 官方普查口径下约 2,150 人,出现在 2017–18 学年前后」**,并明写「行业自报问卷(Heinze/JPT)记作 2,615 或 2,550,系统性高于官方普查约 19–23%,方向一致但水平不可混用」。理由:两席独立取得的 IPEDS 数值完全一致(2,151),仅年份标注差一年;**在年份未定案前,用「2017–18 学年前后」而不写单一年份,是唯一不越证据的写法。**
  - **2,615 vs 2,550 → 不择一,须并列呈现**:写「同一 Heinze 调查在不同 JPT 报道中分别记作 2,615 与 2,550」,并保留口径警告。理由:第 2 席已查明二者同源同调查、只是报道不同,择一等于制造不存在的确定性。
  - **降幅 → 定版 −77%(以 IPEDS 2024 年 488 对 2,151)**,并注明原稿「75–81%」区间是**跨口径相除**(调查峰值 2,615 ÷ 调查「预期毕业人数」655/500)得出,分子分母不同口径,不成立。**因 2023/2024 两年仅第 1 席取得,该 −77% 须标为单源。**
  - **「开设院校 35 → 20 所」→ 整句删除或改写**。若保留,必须写成「Heinze 问卷中设有项目/回应问卷的院校数」,并同时给出 IPEDS 授予学位机构数由 17 所升至 25 所这一反向事实。
  - **滞后期 → 须并列呈现「约三年至四年」**,或直接给出两个日期(油价 2014-06 见顶、学位峰值 2017–18 学年),并保留「业内经验拟合、非发表的计量估计」这一免责。理由:峰值年份未定案,精确到 2.5 年或 3 年都是伪精度;原稿内部本就自相矛盾(先写 2.5 年、后写约三年)。
  - **1984 年峰值 → 定版「拟合趋势峰值约 1,587 名学士,约 1984 年」**,不得写成某年实数。
- **不得这样写**:
  - ❌ 把 2,615 / 894 / 655 / 500 / 「35→20 所」当作官方或普查数字——它们出自 **Texas Tech 的 Lloyd Heinze 主持的年度自愿问卷**,由 JPT 报道,**应答项目数逐年浮动会制造伪趋势**。
  - ❌「2023 年仅 25 个项目回应」与「开设院校从 35 降至 20」并用而不指出矛盾——**回应数 25 > 在办院校数 20,不自洽**;且「25 个项目回应」本身第 2 席未能在一手件中核到。
  - ❌「峰值 2,615 人(2017)」当作已授予学位数——官方普查口径约 2,151;且 JPT 2023 文中的 660/572 是「**预期毕业的大四/大三在读人数**」,不是学位授予数。
  - ❌「2024 年约 500」——该数在 JPT 2023-12-01 原文中**不存在**(原文只到 "572 in 2025 based on the number of juniors")。
  - ❌「较峰值降约 75–81%」——**跨口径相除**(调查峰值 ÷ 调查预期毕业人数),不成立。
  - ❌「开设院校从 35 所降至 20 所」——**被 IPEDS 反证**:授予学士学位的机构数由 2008 年 17 所升至 2022 年 25 所。原写法会给读者「院校在关停」的错误印象。
  - ❌ 把 JPT 2022-03-01 那篇写成 SPE「同机构自我否证」或对崩塌叙事的事后反驳——它**发表于崩塌报道之前**,是先行的方法论保留意见;且不是 SPE 集体立场,是四位学者的邮件往返讨论(新闻报道,非研究)。
  - ❌ 用 Blasingame 的 "we can't use these data to predict the next distributions" 论证「专家否定外推」——**他本人恰恰做了预测**:"we predict that the downward trend may stabilize as it did before and level out at the range of **250 graduates a year**, while the demand for graduates is much higher";其 "This time is different" 是**转述业内说法并顺势看多**,不是用来否定外推。真正的反对意见来自 Kelkar 与 Ozkan。
  - ❌ 给 "This time is different" 加引号直引——第 2 席明确未能逐字核到,**存在版本争议,除非 Round 3 定案否则改述**。
  - ❌ 「1984 年石油工程学士毕业生峰值 1,587 人」写成实测数——原文是拟合高斯分布的峰值、"around 1984",底层是 Heinze & Calhoun 1991 年的背景论文。
  - ❌「滞后约 2.5 年」——伪精度,且与同段自述的「约三年」矛盾;按官方峰值年份未定案,只能写区间。
  - ❌ 把石油工程写成单向崩塌样板而不提 **2023 年低年级已 +13%、10 个最大项目中 7 个在读人数回升**。
- **利益相关**:
  - **Lloyd Heinze 调查**:由 Texas Tech 石油工程系主持、面向各石油工程系自愿填报,**调查方与被调查方同属该学科的招生利益共同体**;其数据经 SPE(石油工程师学会)会刊 JPT 传播,**SPE 是行业协会,「人才短缺」叙事与其会员招聘利益同向**。属**商业/行业调查口径**,方向可参考、程度不承重。
  - JPT 2022-03-01 文中做预测的 Tom Blasingame 时为 **2021 年 SPE 主席**,其「250 人/年但需求远高于此」的看多判断带有行业代言性质,引用须标身份。
  - IPEDS/NCES 与 FRED 为联邦官方统计,无利益相关。
- **待 Round 3**:**是,本条必须送审,且优先级仅次于 G27。**
  - ① **IPEDS 峰值年份定案(核心)**:两席取得的序列数值相同但整体错开一年(第 1 席 2018 = 2,151,第 2 席 2017 = 2,151)。需方法学审计席直接从 **NCES IPEDS Completions 原始 C20XX_A 文件**重跑(筛 CIPCODE=14.2501、AWLEVEL=5、MAJORNUM=1、CTOTALT),并裁定 IPEDS 年份标签与学年的对应关系,给出唯一的峰值年份与峰值人数。**在定案前,成文只能写「2017–18 学年前后约 2,150 人」。**
  - ② **2019 与 2020 均为 1,123 的可疑重复**(第 2 席自陈)需一并复核;**2023(623)与 2024(488)仅第 1 席取得**,需第二条路径确认,否则 −77% 这一降幅只能标单源。
  - ③ **Heinze 调查的方法学必须审计**:调查主体、抽样框、逐年应答项目数、问项定义(「预期毕业人数」vs「已授予学位」)、是否含境外项目(2023 文提到 "in the US **and the Middle East**")。**若取不到方法学描述,2,615/2,550/894/35→20 全部不得承重,只能作为「行业自报,与官方普查存在 19–23% 系统性差异」的对照物出现。**
  - ④ **承载 894 与「35→20 所」的那篇 JPT 文章三席均未定位到**,需反证搜索席定位或宣告弃用。
  - ⑤ **"This time is different" 是否在 2022-03-01 原文中逐字存在**,需第三方复核(第 1、3 席命中,第 2 席未命中)。
  - ⑥ 建议按第 3 席提议,增设 **ASEE《Engineering by the Numbers》**(对工程院校的准普查)作为 IPEDS 之外的独立交叉验证源。

---

## [G30] CRA Taulbee 2025:学位创纪录与招生转负出自同一份报告,但分属三种样本口径,不能连成一条时间序列

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - 数据源只有**两份**报告:《Taulbee Survey 2024: Annual Report》(2025-06-23 发布,数据为 2023–24 学年)与 **Taulbee Survey 2025**(第 55 届,2026-06 发布,学位与在读数据为 2024–25 学年,新生数据为 **2025–26 学年即 2025 秋季入学**)。样本为**美国与加拿大授予博士学位的 CS / CE / Information 系**(CRA 原文:"PhD-granting departments in computer science (CS), computer engineering (CE), and information (I) across the United States and Canada")。
  - **41,858 是 2025 年全部回应单位(127 个报 CS 的单位)的绝对数(报告本体 Table B1.a)**;CRA 自己的"创纪录"说法挂在**纵向队列**数 **32,266†** 上(83 单位;Highlights 逐字:"CS Bachelor's degrees awarded climbed to a record 32,266† (+48.5%† over five years, +12.8%† compared to 2024)")。按全回应单位口径,**2024 年报告的 2023–24 学年 CS 学士学位为 41,912(134 单位),高于 41,858 — 全样本序列并未创纪录。**
  - 报告自带口径声明:"Absolute counts (degrees, enrollment, applications, and other totals) reflect all responding units in 2025.";"(† denotes figures from the longitudinal cohort)"。
  - 队列定义:2025 报告的趋势线基于 **"a cohort of units that reported complete data in every year from 2020 to 2025"(83 单位、六年平衡面板)**,报告自陈这是本年新改的方法("a change from prior years, when trends were reported as the combined totals of all responding units")。**"两年均回应单位"是 2024 年报告的旧方法,也是 2025 报告 Overview 章节的口径 — 三者不可混称。**
  - 队列口径的五个数(全部为 CS-only、83/127 单位):新申报 CS 主修 **−12.9%†**(23,712† → 20,664†,原文 "After peaking at 23,712† in 2024, new CS majors fell 12.9%† to 20,664† in 2025");CS 本科总在读 **−4.1%†**(127,817† → 122,555†);CS 硕士总在读原文为 **"roughly 26 percent"** 下降、新录取 **−10.3%†**;CS 博士学位队列数 **1,351†**(+50.6%† 五年 / +16.1%† 单年),CS 博士新入学 **−15.0%†**,且为 2020–2025 期间首次下降。
  - 对应的**全回应单位绝对数**分别是:新申报主修 33,490(91 单位,Table B5.a)、CS 总在读 169,528(127 单位,Table B6.a)、CS 博士学位 1,909。**博客里的 33,490 与 −13% 分母不同,不可写成同一句话的分子分母。**
  - **同一份报告内存在直接反证,必须并列披露**:Enrollment & Degree Production Overview,Table 1a(两年同单位、95 单位、CS+CE+IN):本科新录取 **38,837 → 39,313 = +1.2%**;Table 1b(117 单位):本科总在读 198,533 → 192,329 = **−3.1%**;Table 1c(117 单位):本科学位 41,058 → 45,932 = +11.9%。报告原文:"Numbers here will not match the five-year-cohort figures … they supplement those views with a broader sample of the latest single-year movement." → **"本科招生领先指标已转负"只在 83 单位五年队列的 CS-only 口径下成立;放宽到 95 单位全计算领域,2025 年新招生是持平微升。**
  - 2024 年报告的两个基准数逐字:"For departments that responded both years, the data shows a **9.9% increase in total new reported majors across all department types**, and a 12.6% increase among U.S. CS departments.";"there was an increase in the total Bachelor's enrollment in 2023-2024 by **6.6%** across all departments … total CS enrollment aggregated across all department types increased by **7.3%**"。**+9.9% 是 CS+CE+I 合计、两年均回应单位、且指 2024 秋季入学(Table B5 标题:"newly admitted Bachelor's students enrolled in Fall 2024"),不是 2023–24 学年。**
  - **抽样框本身在收缩**(Methods Table 1):受邀单位 2024 年 314 家 / 回应 157(50%),2025 年仅 226 家 / 回应 141(**62.3%**);其中 CS 由 129/210 变为 120/176。2023 年报告回收率 176/314 = 56%。**跨年绝对数因此不可比。**
  - **拐点定位**:新申报主修统计的是秋季入学生。2024 报告的 +9.9% = 2024 秋入学,2025 报告的 −12.9%† = 2025 秋入学。**转折点在 2025 秋季入学这一届(2025–26 学年),不是"2024–2025 学年之间"。**
  - **研究生段不可读成美国国内需求信号**:CRA 自己把硕士下滑归因于签证/移民壁垒;同一报告显示国际博士申请 "grew from 15,469 in 2022 to 29,071 in 2025, an increase of 88 percent"。
  - 两句逐字引语三席均核对无误:"These downturns imply that degree counts will plateau and decline in the coming years." 与 "Together, these trends point to a computing education landscape that remains historically strong as it pertains to degrees produced but is showing leading indicators of a coming plateau, as evidenced by the enrollment figures."
  - **NCES 不可与 Taulbee 同图**:NCES《Digest of Education Statistics》Table 322.10,2021–22 学年 "Computer and information sciences and support services" 学士学位 **108,503**(2019-20 为 97,054,2020-21 为 104,883),universe 为参加 Title IV 的高校 + 军事院校、50 州 + DC。与 CRA 的 PhD-granting units 样本确非同一总体。
- **证据分级**:多源证实(三席各自回到 CRA CRN 博客与报告本体逐字核对;其中报告本体 Table B1.a/B5.a/B6.a、Overview Table 1a–1c、Methods Table 1 由一席直接下载 datavisualization.cra.org 全套页面取得,为最严格口径来源)
- **数字定版**:
  - **学士学位:文章用队列数 32,266†(83 单位、CS-only、2024–25 学年)承载"创纪录"**,并在括注里给出"全回应单位口径为 41,858(127 单位),而 2024 年报告同口径为 41,912,全样本并未创纪录"。理由:CRA 自己的"record"就挂在队列数上;用 41,858 说创纪录是把两种口径拼接。
  - **本科招生方向:须并列呈现**。83 单位五年队列 CS-only 为 **−12.9%†**,95 单位单年全计算领域为 **+1.2%**。二者出自同一份报告,取任一单值都会误导。
  - **2024 年报告在读增幅:定版 +6.6%(CS+CE+I)/ +7.3%(CS-only),+6.8% 不存在。**
  - **硕士在读:写 "roughly 26 percent"(原文措辞),不得写成精确的 −26%。**
- **不得这样写**:
  - ❌「41,858 个 CS 学士学位创纪录」——41,858 是全回应单位绝对数,该口径下 2024 年报告的 41,912 更高,并未创纪录。
  - ❌「+9.9% → −3.1% → −13% 说明拐点在两年内完成」——三点分属三种样本、两种字段范围(CS+CE+I 两年均回应 / CS+CE+IN 117 单位 / CS-only 83 单位六年队列),且其中两点出自**同一份 2026 年报告**,不构成时间序列。
  - ❌「2025 年度另有一次调查显示本科在读 −3.1%」——**不存在第三份调查**。−3.1% 就在 2025 报告的 Overview Table 1b 里。(第 2、3 席据此判"该观测凭空多出、须删除";第 1 席回到报告本体定位到了它。合并结论:数据点真实存在,**错的是来源归属**,不是数据本身。)
  - ❌「2024 年度 Taulbee 总在读 +6.8%」——报告中不存在 6.8%。
  - ❌ 把 +9.9% 说成"新生入学"——原文是 "new reported majors"(新申报主修),且是 CS+CE+I 合计。
  - ❌ 把百分比变化的分母写成"两年均回应单位"——2025 报告已改为 2020–2025 六年平衡面板。
  - ❌ 把 NCES 的 108,503 与 CRA 的 41,858 画在同一张图/同一句里比较。
  - ❌ 用硕士 −26% 论证"美国 CS 需求下滑"——CRA 自陈主因是签证与移民壁垒。
- **利益相关**:CRA(Computing Research Association)是计算研究机构的行业协会,Taulbee 调查为其会员单位自报数据;"创纪录学位产出"对会员招生有正向宣传价值。抽样框逐年收缩且由协会自行决定邀请名单,属自报-自选样本。
- **待 Round 3**:是。(1)Table B1.a 的 41,858 与 2024 年报告 Table B4 的 41,912 是否为同一字段定义(127 vs 134 单位),需再确认一次以免"未创纪录"这一反证本身踩坑;(2)Overview 各表的单位数(95/117)与 Highlights 队列(83)之间的样本嵌套关系需写清,供正文脚注使用。

---

## [G31] 数据科学与大数据技术(080910T)布点逐年序列:媒体依教育部附件人工汇总,一手复核后两年被订正、一年不可复核

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - **来源性质**:教育部**从未发布**该专业的逐年布点时序。流传的序列是第三方(网易/163 转载,上游为"全国高校人工智能与大数据创新联盟 + 华算人工智能研究院")对教育部历年备案审批结果附件的人工汇总。教育部各年度通知正文均无任何专业级统计。
  - **一手订正后的逐年"新增备案(含审批)"布点数**(专业代码 080910T,回教育部原件按附件分节计数):
    | 年度(批次) | 布点数 | 证据层级 |
    |---|---|---|
    | 2015 年度 | **3** | 一手(附件"二、新增审批",目录外新专业);第 3 席点数 |
    | 2016 年度 | **32** | 一手;第 3 席点数 |
    | 2017 年度 | **250**(峰值) | 一手;第 3 席点数 |
    | 2018 年度 | **196** | 一手;第 3 席分节点数(另有 7 条属"三、调整学位授予门类或修业年限",媒体的 203 = 196 + 7) |
    | 2019 年度 | **137(未复核,不可承重)** | 媒体汇总;教育部附件为**无文字层的扫描图像 PDF**(W020200303365402032446.pdf 19.7 MB、W020200303365403079451.pdf 9.9 MB),pdftotext 抽出 0 字符,三席均无法机器点数 |
    | 2020 年度 | **62** | 一手(附件 xls,另有调整 11、撤销 1) |
    | 2021 年度 | **34** | 一手分节点数(媒体的 40 = 34 + 6 条"调整") |
    | 2022 年度 | **30** | 一手(另有调整 4) |
    | 2023 年度 | **33** | 一手(该年附件已不分节,两席独立点数一致) |
    | 2024 年度 | **15(标注:该年附件未分节,该数为全文计数,可能含"调整"行)** | 一手计数,分节性存疑 |
  - **可承重的年份**:2015、2016、2017、2018、2020、2021、2022、2023(均已回教育部原件按节点数)。**2019 年度不可承重**,必须单独标注"教育部附件为扫描件,无法复核,数值取自媒体汇总"。**2024 年度可用但须注明未分节。**
  - **累计数必须降级并改写**:逐年新增相加(按媒体口径)为 3+32+250+203+137+62+40+30+33 = **790**,不是 775;第三方口径本身互相矛盾(163.com:"2015–2023 九年全国 775 所(不含重复备案)";今日头条:"2015–2024 十年全国 764 所";另一处 2025-04 更新称"全国 805 所高校备案、新增 15 所",805 ≠ 790+15)。一个"不含重复"的累计数不可能从 775 降到 764。→ 正文写「第三方汇总的在办布点存量约 760–810 所,口径不一且互不自洽」,或**只写已一手验证的年度增量,不写累计**。存量(净额,已扣撤销停招)与逐年新增流量**不能对齐相加**。
  - **分母必须加"本科"二字**:775 / 全国普通本科高校(约 1,275–1,308 所)≈ **59–61%**;若用"普通高等学校"(含高职高专,约 2,820–2,868 所)则仅约 **27%**。
  - **"2015 年 3 所"须加限定**:这是"**2015 年度**"批次(2016 年 2 月公布),不是 2015 自然年获批。同类问题贯穿全序列:媒体常按**公布年**标注(如把 2017 年度的 250 记作"2018 年 3 月第三批"),与按**年度**标注差一年,正文必须统一为"X 年度批次(次年 X+1 年 M 月公布)"。
  - **浪峰读法**:峰值在**第 3 个批次(2017 年度)**——2015 年度 3 → 2016 年度 32 → 2017 年度 250(人民网 2019-03-31:"2018 年 3 月,第三批共有 250 所高校获批";腾讯云社区 2018-03-27:"今年多达 250 所院校新增")。至 2023 年度 33,自峰值衰减 86.8%;若接受未分节的 2024 年度 15,则为 250 → 15、衰减约 94%。
- **证据分级**:多源证实(2018、2023 两年由两席以上独立点数;2015/2016/2017/2020/2021/2022 为**单源已核**,仅第 3 席分节点数)/ 2019 年度 **未验证** / 累计数与"775 所" **方向存争**
- **数字定版**:
  - **2018 年度定版 196**(新增备案口径),理由:第 3 席按附件分节计数并指出 203 混入了 7 条"调整学位授予门类",这是对另两席全文 grep 计数的**明确纠错**,符合"另一席明确指出该发现有误"的例外;且分节口径与"新增布点"的语义一致。正文提 203 时须写作"媒体口径 203(含 7 条学位门类调整)"。
  - **2021 年度定版 34**(同上,媒体的 40 含 6 条调整)。
  - **峰值定版 250(2017 年度)**,由一手点数确认(此前第 1 席标记为"最吃重却无一手支撑",已被第 3 席的一手点数解决)。
  - **累计数:须并列呈现且降级**——不给单一数字,写"第三方汇总 775(至 2023 年度)/764(至 2024 年度)/805(2025-04 更新),三者互相矛盾"。
  - **2024 年度 15:标注为待分节复核**,不作为衰减幅度的定版依据;文章的衰减幅度以 250 → 33(2017 年度 → 2023 年度,−86.8%)为准。
- **不得这样写**:
  - ❌「2018 年 203 所」「2021 年 40 所」——两个数都混入了"调整学位授予门类或修业年限"的存量专业,不是新增布点。
  - ❌ 把该序列称为"教育部数据"或"官方时序"——教育部从未发布该时序;它是第三方对附件的人工汇总,且该汇总方各年口径不统一(2018/2021 含调整行、2022 不含),**作为一个可比时序本身就不成立**,只有回到原件分节重数后才可比。
  - ❌「累计 775 所,约占全国普通高校 60%」——两处错:775 与逐年相加(790)不自洽且第三方口径互斥;分母漏了"本科",按含高职的全部普通高校只有约 27%。
  - ❌「布点浪峰在开设第 2 年见顶」——峰值是第 3 个批次(2017 年度)。
  - ❌ 直接引用 2019 年度的 137 而不标注"该年教育部附件为扫描件、无法复核"。
  - ❌ 把"2015 年 3 所"写成自然年,或在同一段里混用"年度"与"公布年"两种标注。
- **利益相关**:上游汇总方"全国高校人工智能与大数据创新联盟""华算人工智能研究院"为大数据/AI 领域行业组织,其统计口径与发布节奏服务于该领域推广,且从未公开逐校底表。
- **待 Round 3**:是。(1)**2019 年度扫描件需 OCR 或人工翻页点数**——这是唯一挡在完整一手序列前面的年份,且它落在浪峰的下降段上,是"衰减速度"的关键一格;(2)**2024 年度附件需按分节重数 080910T**,确认 15 是否含调整行;(3)"存量 775/805 所"的原始底表是否存在,若不存在,正文彻底弃用存量口径。

---

## [G32] 人工智能专业(080717T)逐年新增布点:一手序列已建立,但文章指定的"关键检验信号"(2025 年度备案审批结果)三席**均未取到一手**

- **判决**:CORRECTED(3/3 票 CORRECTED;关键检验点第 1 席判"该数据尚不存在"、第 2 席判 UNVERIFIABLE 但确证通知编号存在、第 3 席判"未见发布,且不排除已发布于未被存档的页面")
- **锁定表述**:
  - **一手点数的人工智能(080717T)逐年新增布点序列**(第 3 席按附件分节计数):**2018 年度 35**(在"二、**新增审批**本科专业名单",因当时 080717T 属目录外新专业)、**2019 年度 不可复核**(附件为扫描件)、**2020 年度 130**、**2021 年度 95**、**2022 年度 59**、**2023 年度 38**、**2024 年度 91**。
  - **这条序列的形状与"单调降温"叙事相反**:峰值在 **2020 年度(130)**,2023 年度跌到 38 后,**2024 年度反弹到 91**。正文必须如实呈现这个反弹,不得只写"从 35 增长到 91"或暗示持续降温。
  - **2024 年度的 91 是"专业布点数"不是"高校数"**:附件 1 中 080717T 出现 91 次,其中 **2 条备注为"二学位"**,故首次开设四年制本科人工智能专业的高校约 **89 所**。量词必须改。
  - **2018 年度同批次参照(一手点数,第 1、3 席一致)**:机器人工程 080803 = **101**;智能科学与技术 080907 = **96**;大数据管理与应用 120108T = **25**;网络空间安全 080911TK = **25**(在"二、新增审批",国控专业);物联网工程 080905 = **14**;数据科学与大数据技术 080910T = **196**(非 203,见 G31)。
  - **累计数不可承重**:流传的"截至 2024 年度累计 626 所"依赖不可复核的 2019 年度。第三方汇总方自身也不自洽(2022 年度新增 58 → 累计 498;2023 年度新增 38;2024 年度新增 91 → 累计 626,而 498+38+91 = **627**);学信网 2024-08-07 另称"全国共有 498 所高校开设人工智能本科专业"(同一时点第三个数)。**整条累计数列的精度只有 ±1~2 所,不得给两位有效数字之外的确定性。**
  - **2019 年度 179 vs 180 之争**:第 3 席指出,若坚持"截至 2024 年度累计 626",唯一自洽解是 2019 年度 = **178**、截至 2019 年度累计 213(因一手序列 35+130+95+59+38+91 = 448,626−448 = 178)。此为**倒算值,不是点数值**,只能作为"三个候选数都靠不住"的证据使用,**不得替换 179/180 写进正文**。正文只写已验证的年度增量,不写累计。
  - **【关键检验点 · 本条最重要的结论】文章"可检验信号"一节所依赖的教育部《2025 年度普通高等学校本科专业备案和审批结果》,Round 2 三席均未取得一手原文或附件,亦无任何一席取得 2025 年度的分项数字。**具体状态如下:
    - **第 1 席**:核到 2026 年唯一相关的教育部文件是**教高函〔2026〕2 号《教育部关于公布〈普通高等学校本科专业目录(2026 年)〉的通知》**(成文 2026-04-07,发布 2026-04-28),**唯一附件是 2026 年专业目录**,正文只说"教育部组织开展了 2025 年度普通高等学校本科专业设置和调整工作",**无逐校结果名单**。据此判断"2025 年度结果尚未公布"。
    - **第 2 席**:通过二手来源(中国矿业大学教务部 2026-06-26 页面、百度百科词条,参考资料均为 2026 年 4–6 月各校获批公告)确证**《教育部关于公布 2025 年度普通高等学校本科专业备案和审批结果的通知》(教高函〔2026〕3 号)已于 2026 年 4 月印发**,但**未能打开该通知页面及附件**(moe.gov.cn 对 WebFetch 形成 https↔http 302 循环;Wayback 在其环境被禁;Bing 触发人机验证)。**判 UNVERIFIABLE。**
    - **第 3 席**:用 Wayback CDX 枚举 moe.gov.cn/srcsite/A08/moe_1034/s4930/ 前缀,2025-05 至 2026-07 无任何新通知;逐条核对教育部答记者问栏目 2026 年 1–6 月全部存档条目,无一条涉及本科专业备案审批。**但自陈"WebSearch 额度耗尽、教育部站内搜索为 JS 加载,不排除该结果已发布于未被存档的页面"。**
    - → **合并结论:该通知(教高函〔2026〕3 号)极可能已存在,但 Round 2 无人取到原文、无人取到任何 2025 年度数字。**正文必须写成"**待检验信号,截至本文写作日(2026-07-24)我们未能取得该文件原文;二手来源显示编号为教高函〔2026〕3 号、2026 年 4 月印发**",绝不可暗示已知方向,也不可写成"教育部尚未公布"(那是第 1 席的结论,已被第 2 席的二手证据部分推翻)。
  - **2025 年度的全国汇总数同样不存在**:教育部 2026-04-28 新闻稿改了口径,只给"十四五"五年累计——逐字:"据统计,'十四五'期间,全国高校新增本科专业布点 **1.02 万个**、撤销或停招 **1.22 万个**。专业调整幅度持续增大,累计调整比例超 30%,今年全国高校专业调整比例首次突破 10%。"**没有与 2024 年度 1839/157/2220/1428 同格式的 2025 年度分项数,没有人工智能新增校数**;唯一具体校数是"支持哈尔滨工业大学、北京航空航天大学等 **9 所**高校增设具身智能新专业"。
  - **2024 年度官方基准数可复算(可加固文章)**:教育部高教司负责人答记者问逐字"新增专业点 **1839** 个""调整学位授予门类或修业年限专业点 **157** 个""撤销专业点 **1428** 个""停招 **2220** 个"。第 1 席用附件 1 独立验算:全表 **1996** 条 − 85(调整学位授予门类) − 72(调整修业年限) = **1839**,与官方吻合。→ 1839 可从"引用媒体"升级为"可复算的官方口径"。
  - **【会毁掉该检验信号的机制,必须写进文章】AI 布点正在跨专业代码分流**:2026 年目录新增具身智能(首批 9 所:哈工大、北航、北理工、上交、浙大、西交、北邮、南航、东北大学)、脑机科学与技术、人工智能教育、商业人工智能等。因此"080717T 人工智能新增校数下降"**不能**直接读成"AI 布点降温"。**可检验信号必须重新定义为"AI 相关全部专业代码的合计新增布点数",否则该指标自带向下偏误。**
- **证据分级**:**单源已核**(2018/2020/2021/2022/2023/2024 各年度 080717T 点数,仅第 3 席分节点数;2018 年度七项参照由第 1、3 席各自点数,为多源证实)/ 2019 年度 **未验证** / 累计 626 与 498 **方向存争** / **2025 年度结果:未验证(三席均未取到一手)**
- **数字定版**:
  - **人工智能新增布点序列定版为一手点数的 2018:35 / 2020:130 / 2021:95 / 2022:59 / 2023:38 / 2024:91**,2019 年度留空并标"教育部附件为扫描件,不可复核"。理由:这是唯一逐条回到教育部原件、且按附件分节区分"新增"与"调整"的口径。
  - **2024 年度写"91 个专业布点(含 2 个第二学士学位,即约 89 所高校首次开设)"**,不写"91 所高校"。
  - **累计数:不使用**(626/627/498/213 全部不自洽,且依赖不可复核的 2019 年度)。
  - **2019 年度 178/179/180:须并列呈现并注明全为推算或媒体值**,或整段不用。
- **不得这样写**:
  - ❌「2024 年度新增 91 **所高校**」——附件是专业点清单,其中 2 条为第二学士学位。
  - ❌「截至 2024 年度累计 626 所」——建立在不可复核的 2019 年度上,且汇总方自身算术差 1(498+38+91=627),另有 498 的第三口径。
  - ❌ 把 35/179–180/626/91 及同批次参照称为"教育部公布的数字"——教育部**从不按专业公布新增校数**;这些是第三方对附件的二次统计(第 3 席另行回原件点数的 35/130/95/59/38/91 才是一手)。
  - ❌「截至 2026-07,该结果应已正式公布」——这是论断的前提,不成立/未证实。
  - ❌「教育部尚未公布 2025 年度结果」——第 2 席已由二手来源确证教高函〔2026〕3 号于 2026 年 4 月印发。正确写法是"我们未能取得该文件原文"。
  - ❌ 暗示"2025 年度人工智能新增校数已低于 91"或给出任何方向——**目前无答案**。新高考网 2026-06-22 志愿库的"人工智能共 635 所"是**在办校数、非布点数**,不可承重。
  - ❌ 把"080717T 新增校数"单独当作 AI 降温的检验指标——具身智能等新代码正在分流布点,该指标自带向下偏误。
  - ❌ 把"人工智能布点单调降温"写成事实——一手序列显示 2020 年度是峰值、2024 年度是**反弹**。
- **利益相关**:626/91/498/38 等流传数字的上游为"全国高校人工智能与大数据创新联盟""华算人工智能研究院",系 AI 领域行业组织,未公开逐校底表。教育部新闻稿的"十四五"累计数为政策成效表述。
- **待 Round 3**:**是,最高优先。**(1)**必须取到《教育部关于公布 2025 年度普通高等学校本科专业备案和审批结果的通知》(教高函〔2026〕3 号)原文与附件 1**,点数 080717T 及全部 AI 相关代码,并复算 2025 年度的新增/撤销/停招/调整分项——这是文章"可检验信号"一节的核心数据,Round 2 三席全部落空(第 2 席受 302 循环阻断、第 3 席搜索额度耗尽、第 1 席据 2026 年 2 号文误判为未发布)。取不到就必须在正文明写取不到。(2)2019 年度扫描件 OCR,补齐 080717T(候选 178/179/180)。(3)确认 2026 年新增的具身智能、脑机科学与技术等代码,建立"AI 相关代码合计"的可复算口径。

---

## [G33] 撤销专业排行:教育部 2023/2024 年度附件里**根本没有撤销名单**,现有 Top5 榜单底表来源不明;2020–2022 年度可回一手点数

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - **最关键的发现**:2023 年度(教高函〔2024〕6 号)与 2024 年度(教高函〔2025〕3 号)两份通知**各只有两个附件**——附件 1《XX 年度普通高等学校本科专业备案和审批结果》与附件 2《普通高等学校本科专业目录》;**两份附件 1 全文检索"撤销",命中次数均为 0**。→ **2023、2024 两个年度的撤销排行不可能由"依教育部逐校附件二次汇总"得出,其底表来源未被披露。**这不是"降级为媒体计数",而是"**底表来源不明**",必须写进来源说明。
  - **2020–2022 年度教育部确实发布了逐校撤销名单**,第 3 席回原件分节点数(下限值,解析可能漏行):
    - 2020 年度:公共事业管理 21、信息管理与信息系统 16、电子信息科学与技术 15、产品设计 13、工业设计 12、服装与服饰设计 10、信息与计算科学 10。
    - 2021 年度:信息管理与信息系统 33、公共事业管理 31、服装与服饰设计 19、信息与计算科学 19、行政管理 16、教育技术学 16、产品设计 15。
    - 2022 年度:信息管理与信息系统 27、公共事业管理 23、市场营销 22、产品设计 21、信息与计算科学 21、广告学 18、电子信息科学与技术 13、网络工程 12。
  - **教育部就此发布过的唯一官方数字**是 2024 年度答记者问的四个总量:新增专业点 **1839**、调整学位授予门类或修业年限 **157**、撤销 **1428**、停招 **2220**(另:新专业 29 种、《目录(2025 年)》845 种)。**只有总量,没有分专业构成。**2026-04-28 新闻稿也只给"十四五"累计"撤销或停招 1.22 万个"。
  - **三套流传榜单的处置**:
    - **A(2024 年度 Top5:信息管理与信息系统 38、市场营销 34、信息与计算科学 27、网络工程 26、产品设计 24)**:第 2 席找到三家一致转载(搜狐 2025-05-09、腾讯新闻 2025-04-30、今日头条 2025-05-10),第 1 席检索未获任何出处。**处置:底表来源不明(教育部该年度附件无撤销名单),仅可作"媒体二次汇总"标注使用,不得作为事实承重。**
    - **B(麦可思研究院,2020–2024 五年:信息管理与信息系统 160、公共事业管理 138、信息与计算科学 123、市场营销 104、产品设计 93)**:出处已查实为**麦可思研究院**,经财新周刊(2025-08-23)、凤凰网、今日头条转载,五个数字与转载原文逐字一致。**因含 2023、2024 两年而同样不可回教育部原件复核**;麦可思未公开逐校底表。
    - **C(2018–2022 或 2022 单年)**:第 1 席查实"信息管理与信息系统 27、公共事业管理 23、市场营销 22、产品设计 21、信息与计算科学 21"实为 **2022 单年**数(与第 3 席的一手点数完全吻合),不是五年累计。
    - → **A/B/C 三套窗口互不嵌套且部分重叠,分属不同汇总方,并列呈现会制造"多方独立印证"的假象,实际可能是同一批底稿的不同切片。文章只保留一套(建议 B,注明来源麦可思、窗口 2020–2024、底表未公开),另一套仅作脚注。**
  - **"绝对数排名系统性高估大基数专业衰败感"这一批评成立**,有三条独立理由,建议全写:
    a. **未除以布点总数**:信息管理与信息系统、公共事业管理、市场营销的布点基数都在数百所量级,三套榜单**均未给分母**,没有任何一处给出撤销**率**。绝对数榜同时测了"基数大"和"淘汰率高"两件事,文章只想说后者。
    b. **停招不进撤销榜**:教育部同年停招 2220 个 > 撤销 1428 个,而停招往往是撤销的前置动作。只看撤销榜会系统性漏掉"已停止招生但未走完撤销流程"的专业,不同专业走这两条路径的比例未必相同。
    c. **底表来源不明**(见上),无法独立复算。
  - **核心推论必须重写**(这是本条对读者伤害最大的地方,两席各自给出一条硬理由,须合并):
    - **门类事实(第 2 席)**:信息管理与信息系统是 **120102(管理学·管理科学与工程类)**,信息与计算科学是 **070102(理学·数学类)**,二者都**不是**计算机类(0809);三套榜单里唯一的计算机类专业是**网络工程 080903**。计算机类核心专业(计算机科学与技术、软件工程、人工智能、数据科学与大数据技术)**未出现在任何一套 Top5 中**。
    - **榜单构成事实(第 3 席)**:撤销榜上同时挤满带"信息/计算/网络"字样和完全不带的专业——**公共事业管理在 2020 年度居第一、2021 与 2022 年度居第二**,产品设计、服装与服饰设计、工业设计、广告学、市场营销常年在榜;网络工程只在 2022 年度以 12 例进入前八。
    - → **锁定表述:「专业名字里有没有'信息/计算/网络'字样,与它是不是计算机类、与它是否被淘汰,都是三件事。撤销数居前的是挂着信息名号的管理学与数学类专业(信息管理与信息系统 120102、信息与计算科学 070102),以及公共事业管理、市场营销、产品设计等完全不带 IT 字样的专业;计算机类核心专业未进入任何一套 Top5。」**
  - **分层说法(撤销集中在地方本科院校 / 头部高校同名专业普遍未撤)**:第 1、2 席均未找到分层统计并建议删除;**第 3 席回一手做出了分层计数**——2022 年度撤销共解析到 918 行,按主管部门:山东 86、江西 74、辽宁 61、陕西 53、河南 48、安徽 44,**教育部直属仅 43(约 4.7%)**;该年 27 例信息管理与信息系统撤销中只有 1 例属教育部直属(国际关系学院,且为二年制第二学士学位),其余全为省属高校、学院与独立学院。→ **可写的只有前半句且必须收窄为:「在 2022 年度这一个年度的教育部撤销名单中,部属高校占撤销总量不足 5%」。后半句"头部高校同名专业普遍未撤"不得写入**——第 2 席另举反例:四川大学、东北林业大学、天津工业大学同期也撤了榜单内专业。
- **证据分级**:**多源证实**(2023/2024 年度附件无撤销名单一事,第 1、3 席各自 grep 命中 0;2024 年度四个总量)/ **单源已核**(2020–2022 年度逐校撤销点数,仅第 3 席)/ **商业调查**(麦可思 2020–2024 榜单,底表未公开)/ **未验证**(2024 年度 Top5 榜单 A 的底表)
- **数字定版**:
  - **文章的撤销叙事定版使用教育部一手 2020–2022 年度点数**(第 3 席的三年榜),麦可思 B 榜仅作补充并标"商业调查、底表未公开"。理由:唯一可回原件复算的口径;且它自带三年序列,比单一切片更能说明"常年在榜"。
  - **2024 年度撤销总量定版 1428 个(教育部答记者问,官方)**,并写明"教育部只发布总量,不发布分专业构成"。
  - **2024 年度 Top5(38/34/27/26/24):不定版、不承重**,若引用须写"媒体二次汇总,底表来源不明"。
- **不得这样写**:
  - ❌「A/B/C 三套排行是依教育部逐校附件二次汇总」——2023、2024 年度的教育部附件里没有撤销名单,"撤销"二字出现 0 次。
  - ❌ 把 A、B、C 三套并列呈现称"多方数据一致印证"——窗口重叠、汇总方不同、可能是同一批底稿的切片。
  - ❌「被撤最多的不是文科,而是信息管理与信息系统、信息与计算科学、网络工程这些 IT 相关专业」——一手数据不支持这个对立:公共事业管理常年居前二;前两个专业分属管理学与理学,不是计算机类。**按此写法,准大学生会得出"计算机类正在被大规模撤销"的错误结论,这是本篇最该避免的伤害。**
  - ❌ 引用任何撤销榜而不同时说明"无撤销率分母""停招不进榜""底表未公开"。
  - ❌「撤销集中在地方本科院校、头部高校同名专业普遍未撤」——后半句无任何证据且有反例(川大、东北林大、天津工大同期均撤了榜内专业),**哪怕加"据称"也不得写入**;前半句只能收窄为 2022 年度"部属高校占比不足 5%"。
  - ❌ 把 C 榜的五个数当作 2018–2022 五年累计——它是 2022 单年数(已被一手点数确认)。
- **利益相关**:麦可思研究院是商业性高教数据与咨询机构,其榜单为营销与媒体传播产品,底表不公开;媒体转载标题(如"史上最严!超 500 所高校专业,关停")具流量导向。
- **待 Round 3**:是。(1)**麦可思 2020–2024 榜单的原始方法说明与底表来源必须索取或明写"未公开"**——文章若用 B 榜,这是唯一的方法学抓手;(2)2024 年度 Top5(A 榜)的原始出处仍未定位,若 Round 3 仍找不到,**从文章中彻底删除**;(3)2020–2022 撤销点数为第 3 席单席解析(自陈"解析可能漏行",2022 年度 1138 行只解析到 918 行),需第二席独立复算后方可承重;(4)若能取到 2025 年度附件(见 G32),核对其是否恢复了撤销名单分节。

---

## [G34] AACN 护理拒收申请与师资空缺:数字与年份可锁定,但"执照/席位/师资三条件抑制过冲"这一判据过强且与文章自身案例矛盾

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - **AACN 可文献化的连续序列(同一张 fact sheet 的同一指标,逐年更新)**:**2023 = 65,766**(配 2023 年 10 月调查:1,977 个全职师资空缺 / 922 所院校 / 84.6% 回收率 / 空缺率 7.8%)→ **2024 = 80,162** → **2025 = 92,672**(配 2025 年 10 月 Special Survey:1,588 个全职空缺 / 863 所院校 / 80.3% 回收率 / 空缺率 7.2%)。
  - **92,672 的完整口径(逐字)**:"U.S. nursing schools turned away 92,672 qualified applications **(not applicants)** from baccalaureate and graduate nursing programs in **2025** due to insufficient number of faculty, clinical sites, classroom space, and clinical preceptors, as well as budget constraints." 其中**硕士项目 6,496 份、博士项目 10,359 份**(另有页面表述为"nearly 17,000 applications were turned away from graduate programs"),故**入门级学士层次约 75,817 份**。用 92,672 说护理"本科"培养瓶颈,**高估约 22%**。
  - **80,162 的年份口径(必须改)**:AACN 原文为 "According to AACN's report on **2024-2025 Enrollment and Graduations** in Baccalaureate and Graduate Programs in Nursing, U.S. nursing schools turned away 80,162 qualified applications from baccalaureate and graduate nursing programs **in 2024**"。→ **"2024-2025"是那份报告的名字,不是拒收发生的窗口;拒收年份是日历年 2024。**同样是本科+研究生合计。
  - **"applications 不是 applicants"由 AACN 自己写明**:括注 "(not applicants)" 出现在 AACN 原文中。文章应写"**连 AACN 自己都在数字后加括号标注 (not applicants),但媒体转述时普遍丢掉了这个括号**",这比"AACN 的措辞是 applications"更有力也更准确。一名申请人可投多校,真实被拒**人数**显著低于该值,而 **AACN 从未发布被拒人数**。
  - **师资空缺数据**(三席逐字核对一致):2025 年 10 月 AACN《Special Survey on Vacant Faculty Positions》——**1,588 个全职师资空缺、863 所院校(含学士和/或研究生项目)、80.3% 回收率、全国师资空缺率 7.2%**,各校自陈还需增设 150 个师资岗位。
  - **一处对论断不利、必须一并写出**:同一页给出 "the **10-year national average** full-time faculty vacancy rate was **7.64%**"。→ **2025 年的 7.2% 低于十年均值,把它当"瓶颈正在恶化"的证据站不住,它只支持"瓶颈长期存在"。**
  - **判据必须重写(本条最需要改的地方)**。原判据"(a) 执业需执照且执照供给受限 /(b) 实训席位 /(c) 师资瓶颈,任一满足则过冲被抑制"——**(a) 不成立,且与文章自身案例直接矛盾**:美国法学需 ABA 认证院校 + 律考执照,却是过冲的教科书案例(2007–2013),而论断自己把法学归进"开一个专业只需要教室和 PPT"一栏。其他硬反例:**美国药学(PharmD)**——需 ACPE 认证、州执照、强制实习轮转,三条全占,2000–2015 年培养单位仍近乎翻倍并形成著名的药师过剩;**执业护师(NP)**——需带教 preceptor 与执照,项目数与产出十年内仍数倍增长。
    → **锁定判据:决定过冲的不是"执业端有没有执照",而是「培养端产能是否受物理或人力约束」以及「扩张的边际成本」。执照卡在毕业之后(法学、药学)对招生端毫无约束;卡在入口的才抑制过冲(护理:临床实习席位、preceptor 与师资同时受限,这正是 AACN 自陈的拒收原因)。且认证机构本身会在热潮中顺周期放宽。**
    → **同时把"过冲几乎必然被抑制"降级为"过冲的幅度与速度显著更小/更慢"**:供给受限只能拉长滞后、削平振幅,**不能保证过冲不发生**。
  - **H-1B"把工程师市场调整期从约 4 年压到约 1 年"**:三席均未取得一手出处。蛛网-工程师这一学术脉络本身真实存在(**Freeman, R. B. (1976), "A cobweb model of the supply and starting salary of new engineers," ILR Review**,该文给出的是工程师约 4 年的调整期),但"压到 1 年"是另一条独立断言,**须另行补引原文,否则只保留方向性推论、删去具体数字**。"中美必须分国讨论"这一方法论提醒三席均判成立且必要。
  - **媒体转述的两处错误(处置)**:Becker's 用的 **66,000 是 65,766 的四舍五入,即 AACN 2023 年的正确数字,只是过时(stale),不是数值错误**;nurse.org 的"93,176 名申请人"**既错在 applicants/applications 量纲,数值也对不上 AACN 任何年份**。→ 写作"Becker's 用的 66,000 是 2023 年旧数,数值本身没错但已过时;nurse.org 把份数说成人数才是口径错误"。
- **证据分级**:**多源证实**(92,672 / 1,588 / 863 / 80.3% / 7.2% / "(not applicants)" 三席各自直取 AACN 现行页逐字一致;80,162 及其年份由第 2 席自 AACN 官方 PDF、第 3 席自 Wayback id_ 原始字节两处独立取得)/ **单源已核**(7.64% 十年均值、6,496 与 10,359 分层数,第 2、3 席)/ **未验证**(H-1B "4 年→1 年";nurse.org 与 Becker's 原文第 3 席未取回)
- **数字定版**:
  - **80,162 保留,年份定版为「2024 年」**。理由:第 1 席"AACN 无此数、须删除"的结论已被第 2 席(AACN 自家 PDF `Faculty-Shortage-Factsheet.pdf` 原文)与第 3 席(Wayback `id_` 原始字节两份快照)**明确指出为误**——第 1 席只检了网页版 fact sheet 与部分快照,未覆盖 PDF 版与 2026-03/2026-05 的快照。适用"另一席明确指出该发现本身有误"的例外。
  - **拒收序列定版为 2023 = 65,766 / 2024 = 80,162 / 2025 = 92,672,三个数并列成序、每个数必须带年份**。理由:这不是三个互相矛盾的口径,而是同一指标的连续年份;不标年份并列会让读者误以为存在口径争议。
  - **谈"本科培养瓶颈"时定版用 ~75,817(2025 年学士层次估算 = 92,672 − 6,496 − 10,359)**,并注明推算方式;引 92,672 时必须写"本科与研究生项目合计"。
  - **师资空缺率:7.2%(2025)必须与 7.64%(十年均值)成对出现**,不得单独引用。
- **不得这样写**:
  - ❌「2024–2025 学年拒收 80,162 份」——"2024-2025"是 AACN 报告的**名字**,拒收发生在**日历年 2024**。
  - ❌ 把 80,162 与 92,672 并列而不标年份,或暗示两者是"两个互相矛盾的口径"。
  - ❌ 用 92,672 论证护理**本科**培养瓶颈而不剥离研究生项目的约 16,855 份。
  - ❌「AACN 的措辞是 applications 而非 applicants,文章需要纠正它」——AACN 自己就在括号里写明了 (not applicants),该由文章指出的是**媒体丢掉了这个括号**。
  - ❌「Becker's 用 66,000、nurse.org 用 93,176,两处都错」——66,000 数值没错,只是过时(2023 年数)。在指摘别人时自己出错,代价最大。
  - ❌ 把师资空缺率 7.2% 当作"瓶颈正在恶化"的证据——它低于十年均值 7.64%,只支持"瓶颈长期存在"。
  - ❌「执业需执照且执照供给受限 → 过冲被抑制」——法学、药学、NP 三个反例俱在,其中法学还是文章自己举的过冲典型,内部自相矛盾。
  - ❌「满足供给约束条件则过冲不会发生」——只能写"幅度更小、速度更慢"。
  - ❌ 写出 H-1B「把调整期从约 4 年压到约 1 年」这个具体数字——三席均未取得一手出处。
- **利益相关**:**AACN 是美国本科及以上护理院校的行业协会**,其 fact sheet 明确自陈在 "leveraging its resources to secure federal funding for faculty development programs",长期游说 Title VIII 师资拨款;**拒收申请份数(分子)越大,越有利于其拨款诉求**,而它选择公布"份数"而非"人数"这一点本身即须随数字披露。回收率 80.3% 的调查为协会向会员发放的自报调查。
- **待 Round 3**:是。(1)**H-1B"4 年→1 年"必须补一手出处或从文章删除**——这是本条唯一完全悬空的数字;(2)AACN《2024-2025 Enrollment and Graduations》报告原件的**页码级引用**(80,162 目前只有 fact sheet 的转述);(3)药学(PharmD)与 NP 两个反例需补可引用的产能/产出时序,以支撑重写后的判据;(4)Becker's 与 nurse.org 原文需取回逐字,才可在文中点名指摘。

---

## ⚠️ [G35] 三条"自我否证"材料:一条引语被剪改并把作者转述当主张,一条把归因主体搞错,一条把论文结论写成了相反方向

- **判决**:CORRECTED(3/3 票判 CORRECTED;但第 1 席对子项 (b)(c) 明确判 **"REFUTED as stated"**,第 2 席对子项 (c) 明确判 **"实质 REFUTED"**,故标题加 ⚠️。**按现稿写入即为错误陈述。**)
- **锁定表述**:
  - **(a) SPE JPT 石油工程毕业生拟合文章**:Tom Blasingame 等(署名另含 Erdal Ozkan / Mohan Kelkar / Jennifer Miskimins / Stephen Rassenfoss),《History Matching of Petroleum Engineering Graduation Rates》,*Journal of Petroleum Technology*,**2022 年 3 月 1 日**。
    - **引语必须逐字,不得剪短**:原文为 "However, we **can't use these data to** predict the next distributions or to note that these features are always overreactions to the state of the industry in one form or another."(论断把它剪成"can't predict the next distributions"这一原文不存在的短语并标为逐字。)
    - **"This time is different" 是作者转述业界说法**:原句 "As many note about the present state of the industry, **'This time is different.'**"——作者在转述并加引号,**不是自己下判断**。
    - **紧接的下一句作者照样做了方向性预测**:"Petroleum engineering enrollment will need to begin growing soon **afer** hitting bottom."(原文即含拼写误 afer)。→ **这篇文章不是"拒绝预测"的样板,而是"一边声明不能预测、一边预测"的样本;如实写出这层反讽反而更有力。**
    - **该文通篇未出现 "cobweb" 一词**,称其为"SPE JPT 自家的蛛网文章"属过度关联;它能承重的只有"历史拟合不能外推"这一句。须注明这是 2022 年 3 月的文章、非新近材料,且第一作者曾任 SPE(石油工程师协会)主席,存在利益相关。
  - **(b) 2026 周期法学申请激增的归因**:
    - **不存在"申请人自陈主因是政治与经济不确定性"这回事。**可查到的申请人自陈数据是 **LSAC Post-LSAT Questionnaire**(15,000+ 名考生,**2024 年 8 月–2025 年 4 月**):首要动机为"**帮助他人" 49%**(同比升约 20%)与"**为社会公正发声" 37%**(同比升逾 30%),"经济保障" 34%;同时 **55% 把学费成本列为首要障碍**(上年 38%);申请人同比 **+29%**。
    - "政治、经济与社会剧变"是 **LSAC / 媒体 / 招生官给出的背景解读框架**,不是申请人填答的首要理由。被引来源里院长本人的归因也不是"不确定性"——波士顿大学法学院院长 Angela Onwuachi-Willig 归因于 "people who want to have an impact on society" 与法治的重要性,只有招生副主任 Anne Taylor 提到政治/经济动荡。
    - **锁定表述**:「2026 周期法学申请激增,考生在 LSAC 考后问卷中自陈的首要动机是"帮助他人"(49%)与"倡导社会公正"(37%),而非法律岗位需求上升;把它归因于政治经济不确定性的是 LSAC 的背景解读与招生官的事后归因,不是申请人自陈。」
    - **好消息:论断想要的结论反而更强了。**自陈动机是利他/价值观驱动,与就业信号更加无关,"供给冲击可由与就业信号无关的因素驱动、蛛网对此无解释力"这个论点因此更成立,只是机制要换成**价值观驱动**而非不确定性避险。
  - **(c) Peterson 的 AI 教育错配论文(arXiv:2508.19625,v1 2025-08-27 / v2 2025-11-28,Andrew J. Peterson,arXiv comments 字段为 "Under review",未过审)**:
    - **论文明确否认自己是蛛网模型**:"Our model builds on this cobweb tradition but identifies a **critically different** source of friction. In the classic framework, the forecasting error stems from a failure to anticipate the endogenous supply response of other agents to a public price signal. By contrast, the mechanism we propose is driven by a failure to anticipate the dual, cross-domain consequences of a single technological shock." 引 Freeman (1976) 只是文献背景。
    - **结论方向与主体都被写反了**。Proposition 1 (Growing Mismatch) 原文:"For all K > K₀, the naive planner invests **more** time in skill A than is socially optimal (t*_A > t†_A). Moreover, this mismatch is strictly increasing in the level of AI." 摘要:"The planner **over-invests** in skills destined for obsolescence, a distortion that increases monotonically with AI prevalence." → **决策主体是 educational planner(教育规划者/学校),不是个体学生;结论是过度投资,不是减少投资。**
    - **"当 AI 掌握某技能快于学生习得所需年限时"这一机制在论文中不存在。**真实机制是:AI 同时提高某技能的"可教性"并压低该技能的未来工资,规划者只看见前者、内部化不了后者。
    - **"4 个命题" HOLDS**:P1 Growing Mismatch、P2 Non-Cognitive Deficit、P3 Over-Adoption、P4 The Substitution Trap(证明在附录 A.1–A.4)。
    - **"无实证检验"须软化**:附录 B 有一项 **n=20** 的预注册探索性试点调查(90 个 O*NET 技能,数据挂在 OSF: https://osf.io/nwy4c/ ),作者自陈 "While not a formal test of our model"、"intended for illustrative purposes only. The model's formal validity does not depend on these preliminary findings",附录另称 "Given the small and non-representative sample and the use of LLM-derived disruption measures, the results should be interpreted as suggestive rather than as core quantitative evidence."。→ 写作「对模型本身无正式实证检验,仅有一项 n=20 的预注册探索性调查作为动机」。
    - **论文里真正对本文有用的一条是 Proposition 4 的政策含义(杠铃策略)**:"A linear increase in STEM education… might strand students in an unproductive middle ground of coding ability that is easily automated, whereas a socially optimal policy would encourage either broad digital literacy or deep, specialized expertise."
  - **【对"三条并列是否足以支撑'只给可检验信号、不做预测'"的评估 — 三席一致:按现稿不足以,且会适得其反】**这一节的功能是向读者证明作者有认识论纪律;若其中两条本身就误读了来源(一条把作者转述当主张、一条把论文结论写成相反方向),被任何读者查证一次,整篇的可信度损失将大于这一节带来的收益。
    - **改法**:(a) 保留并把"声明不能预测却转身就预测"的反讽点明;(b) 改成"申请人自陈是价值观驱动、与就业信号无关",论点反而更强;(c) **改述为"已有严肃建模指出 AI 时代教育错配的机制可能不是蛛网式的供给滞后,而是教育规划者的跨域信息缺口导致过度投资于易被替代技能——这直接质疑本文的蛛网框架能否外推"**,这样它才真正起到反证作用;否则直接删除。
    - **第 3 席另提一个更硬的自我否证素材,建议采纳**:文章自己设定的关键检验信号(教育部 2025 年度本科专业备案审批结果)**截至 2026-07 本项目三席都没能取到**。"连你指定的检验信号都可能不按时到达/不可取得"比引三条二手反证更能支撑"不做预测"的立场。
- **证据分级**:**多源证实**(Peterson 论文:三席各自下载 PDF v2 并逐行核对,命题原文、摘要 over-invests、cobweb 切割段、n=20 脚注三处一致)/ **多源证实**(JPT 引语:第 1、2 席各自自 jpt.spe.org 取得原文逐字一致)/ **单源已核**(LSAC 考后问卷数据,经 ABA Journal 2025-10-29 报道,第 1 席;第 2 席取到 BU 报道与 LSAC 口径约 +20%,第 3 席判 UNVERIFIABLE)/ **未验证**(2026 申请季"+33%"的路透 2025-10-15 报道,两席环境不可达)
- **数字定版**:
  - **法学申请增幅:须并列呈现并写清周期。**「2025 申请季 LSAC 口径约 **+20%**(BU 2025-04-30 引 LSAC);LSAC 考后问卷所涵盖的考生群体同比 **+29%**;路透 2025-10-15 报道的 2026 申请季申请人 **+33%** 本项目未能核到原文」。理由:三个数分属不同周期与不同分子(申请量 / 考生 / 申请人),取单值必错。
  - **arXiv 论文版本定版 v2(2025-11-28),状态写"Under review,未过同行评审"。**
- **不得这样写**:
  - ❌ 逐字引 "can't predict the next distributions" ——**这个短语在原文中不存在**,是剪改。
  - ❌「作者明确指出'this time is different'」——作者是在**转述业界说法**并加引号。
  - ❌ 称该 JPT 文章为"SPE 自家的蛛网文章"——全文无 "cobweb"。
  - ❌ 只引"不能预测"而不写作者下一句就做了预测("enrollment will need to begin growing soon after hitting bottom")——这会把一个自相矛盾的样本包装成认识论楷模。
  - ❌「2026 法学申请激增的**自陈**主因是政治与经济不确定性」——申请人自陈的首要动机是"帮助他人"(49%)与"社会公正"(37%);"不确定性"是招生官与 LSAC 的事后归因。"自陈"二字必须删。
  - ❌「Peterson 把蛛网套用到 AI 时代教育投资」——论文明确把自己与蛛网切割。
  - ❌「当 AI 掌握某技能快于学生习得所需年限时,个体理性地**减少**人力资本投资」——**方向反、主体错、机制不存在**,三处全错。按此引用会得出与论文完全相反的政策含义。这是本批次最严重的单点错误。
  - ❌「纯理论模型,无实证检验」——会被人拿附录 B 的 n=20 pilot 反驳;准确写出 n=20、作者自陈非正式检验,杀伤力反而更大。
  - ❌ 引用路透"+33%"作为已核事实——两席环境均不可达该域名。
  - ❌ 把 (a)(b)(c) 按现稿并列成一节"自我否证"——三条里两条被误引,这一节会成为全文最容易被推翻的地方。
- **利益相关**:(a) JPT 由 SPE(Society of Petroleum Engineers,石油工程师行业学会)出版,第一作者曾任 SPE 主席,该学会在石油工程招生回升上有直接利益。(b) LSAC 是 LSAT 考试的运营方,申请量增长与其业务直接相关;BU 报道的受访者为该校法学院院长与招生副主任,均为招生方。(c) Peterson 论文为未过审的单作者工作论文,无披露的资助方。
- **待 Round 3**:是。(1)**LSAC 一手报告(2026 Composition Report / Post-LSAT Questionnaire 原件)须取到页码级引用**——目前 49%/37%/34%/55% 全部经 ABA Journal 转述,第 3 席在其环境判 UNVERIFIABLE;(2)路透 2025-10-15 的"申请人 +33%"须取回原文或弃用;(3)三条自我否证材料改写后需重新评估该节是否仍有必要保留,或用 G32 的"检验信号未能取得"替换。**特别提示方法学审计席**:本批两席均报告 **WebFetch 的摘要模型对 arXiv:2508.19625 的 PDF 编造了四条完全不同的命题文本**(如 "Proposition 1: If skill-biased technological change occurs…"),与原文无一相符;凡本项目中经 WebFetch 摘要得来的 PDF 内容,一律需以本地抽取的原文复核。
---

## 前半禁用清单

> 汇总前半被判**不可用**的表述。每条:原表述 → 为什么禁用。逐条按条目号可回查上文完整判决。
> 分四类:**A 伪引与移花接木**(引语本身不存在、被剪改、或射错对象)、**B 事实错误与方向讲反**、**C 口径已过期或来源归属错**、**D 选择性引用与射程越界**。

### A · 伪引、剪改与移花接木(最高危,一旦见刊即为硬伤)

| # | 原表述 | 为什么禁用 |
|---|---|---|
| A1 | 把 Cappelli「政府预测岗位纪录不佳」那句当作**独立学者对 BLS 职业预测的批评**(G-extra) | 移花接木,三席全部点名。原句(NBER WP 20382, 2014-08,手稿 p.49)主语是 **"Governments"** 泛指,语境是佛罗里达州按雇主意愿调拨专业经费,**全文未点名也未引用 BLS 就业预测(EP)项目**。可用的改写射程:只能射向「政府主导的专业—岗位对口式人力规划」,不能射向 BLS EP 这一具体产品 |
| A2 | 引 Cappelli 时标 *ILR Review* 68(2), 2015 的**已发表版页码** | 发表版封闭获取,三席穷尽路径(SAGE 403、OpenAlex `oa_status=closed`、ResearchGate/PhilArchive 403、Wharton 404、Semantic Scholar 候选实为同题幻灯片)均未取到正文;工作论文版 60 余页 → 发表版 40 页有实质删减,**无法确认该句仍在**。只能引 NBER WP 20382 并标「工作论文版」 |
| A3 | 逐字引 "can't predict the next distributions"(G35) | **该短语在原文中不存在**,系剪改 |
| A4 | 逐字引 "an uptick in the dissimilarity of occupational mix between older and younger college graduates, though this remains at the high end of the historical range"(G24) | **两席在 Yale Budget Lab 2025-10 报告与 2026-06 追踪器中均查无此句**。Round 3 定版前不得作为逐字引语使用 |
| A5 | 「超 75,000 名申请人」「56% 的招生官表示……」(G27) | 三席均无源。补源或删 |
| A6 | 「H-1B 从 4 年缩到 1 年」(G34) | 完全悬空,无一手出处。补源或从文章删除 |
| A7 | 凡经 WebFetch 摘要得来的 PDF「原文」(跨条方法学警示,记于 G35) | 两席报告摘要模型对 arXiv:2508.19625 **编造了四条命题原文**。所有 PDF 逐字引语必须以本地抽取的原文复核后方可使用 |

### B · 事实错误与方向讲反(会把结论带反)

| # | 原表述 | 为什么禁用 |
|---|---|---|
| B1 | 「公开文献中基本不存在非 BLS 作者对 BLS 职业预测准确度的系统性量化评估」/「唯一找到的独立学者批评是 Cappelli」(G-extra) | **3/3 全票推翻**。至少有 Stekler & Thomas(MLR 2005-07)与 Bishop & Carter(MLR 1991-10)两项,均带正式误差指标与朴素模型基准,全文可得 |
| B2 | 「BLS 只发点估计,**从不**发布预测的置信区间或情景区间」(G3) | 「从不」是硬错误,一席据此整条判 REFUTED。须拆成两句:统计置信区间确实从不发布;**情景区间发布过**(2021 年疫情两套 + 1980–90 年代高/中/低三档) |
| B3 | 「2025-09 Anthropic Economic Index 显示 automation **首次越过 50%**」(G20) | 三席一致点名的实质性错误。原报告说的是首次**超过 augmentation**,绝对水平 49%/45%。把相对比较升级成绝对阈值 |
| B4 | 「当 AI 掌握某技能快于学生习得所需年限时,个体理性地**减少**人力资本投资」(G35) | **方向反、主体错、机制不存在**,三处全错。按此引用会得出与论文完全相反的政策含义 |
| B5 | 「2025 年 1L 稳定在约 38,000」(G27) | 实为 **42,817(+7.9%)**。方向相反,会把「已起跳」写成「已回稳态」 |
| B6 | 「毕业班规模 −7.0%」归给 Muller(G27) | 张冠李戴:−7.0% 是 ABA 表的数,Muller 的 7% 是大所岗位跌幅。**把分子端跌幅误当分母端缩幅**,会让「修复来自分母缩小」凭空多出一个不存在的量化支撑 |
| B7 | 「石油工程开设院校从 35 所降至 20 所」(G29) | 被 IPEDS 反证:授予学士学位的机构数由 2008 年 **17 所升至 2022 年 25 所**。原写法给读者「院校在关停」的错误印象 |
| B8 | 「石油工程 2024 年约 500」(G29) | 该数在 JPT 2023-12-01 原文中**不存在**(原文只到 "572 in 2025 based on the number of juniors") |
| B9 | 「被撤最多的不是文科,而是信息管理与信息系统、信息与计算科学、网络工程这些 IT 相关专业」(G33) | 一手数据不支持该对立:公共事业管理常年居前二;前两个专业分属管理学与理学,不是计算机类。按此写法准大学生会得出「计算机类正在被大规模撤销」的错误结论 |
| B10 | 「教育部 2023/2024 年度附件中的撤销专业 Top5 排行」(G33) | 教育部 2023、2024 年度附件里**根本没有撤销名单**,现有 Top5 榜单底表来源不明 |
| B11 | 「CEW:CS 应届失业率 7.2%,对比 2013–15 的 **4.3%**」(G14) | 报告正文是 **5.3%**;4.3% 只见于 CEW 博客,且疑为 2022 年 multi/interdisciplinary studies 的应届失业率(Figure 13),存在张冠李戴 |
| B12 | 「应届收入区间 $34,000(communication disorders)至 $86,000(computer science)」(G14) | 四个要素全错:最低是 zoology **$37,000**、communication disorders 是 $39,000、最高是 petroleum engineering **$98,000**、$86,000 属 computer engineering 与 chemical engineering |
| B13 | 「第三轮上升可能部分反映 CIP 11 口径扩张(**数据科学等新专业被归入**)」(G15) | 括号里的例子事实相反:CIP 2020 中 Data Science = 30.70/30.7001、Data Analytics = 30.71,归在 **CIP 30**,不在 CIP 11。口径宽度的警告成立,但这个佐证必须删除 |
| B14 | 「CS 第一轮谷底在 1993-94」(G15) | 实为 **1995-96 的 24,506**,且是一个五年平台而非单点谷底 |
| B15 | 「97.2% 的 openings 是替补退休者」(G6) | 两处错:严格表述只能是「年均分离量相当于 openings 的 97.2%」(衰退职业的分离者 BLS 明说并非都需被替补);且分离中 **55.5% 是职业间转移**,不是退休 |
| B16 | 「Data scientists:2010 SOC 中不存在该代码,2024 实际 245.9」不加限定(G5) | 任何「数据科学家十年增长上百倍」的读法都是错的——那是新设代码,不是增长。呈现给准大学生构成重大误导 |
| B17 | 「2025 年度另有一次调查显示 CS 本科在读 −3.1%」/「2024 年度 Taulbee 总在读 +6.8%」(G30) | 不存在第三份调查(−3.1% 就在 2025 报告 Overview Table 1b,错的是来源归属);**6.8% 在报告中根本不存在** |
| B18 | 「教育部尚未公布 2025 年度备案审批结果」(G32) | 教高函〔2026〕3 号极可能已于 2026 年 4 月印发(二手确证),只是三席均未取到原文。正文必须写「**我们未能取得原文**」,不可写「尚未公布」 |
| B19 | 「NAE 2018 年报告**指出** H-1B 扩张把调整期压缩到约一年」(G26) | 三重错误:附录 D 是两页教科书式模型推演、零统计估计,不是机构结论;「一年」指签证申请滞后即供给可被改变的最短时间,不是整个调整期;原文说的是 1990 年扩容的技术移民临时签证,不专指 H-1B |
| B20 | 「弹性 0.67」当作回归估计使用、并与「法国 0.1」做跨国对照(G26) | 0.67 是份额对相对工资的比值口径、无标准误、R²=0.02;Long 原文自陈不可与法国估计并列。仅一席经 Wayback 取得接受稿,Round 3 定案前不得承重 |
| B21 | 「NIH:26% 是 2012 年读数」(G28) | 终点实为 **2008**(SDR 滞后,报告 p.17/p.23 自陈)。四年时效虚增 |

### C · 口径已过期、来源归属错或不可比

| # | 原表述 | 为什么禁用 |
|---|---|---|
| C1 | CNBC 报道的 5.8% / 4.6%(G12) | 两端都已被后续修订(现行 5.672% / 4.521%)。只追 5.8% 的修订而不提 4.6% 也被改过,是半截更正。表述改「落后一个发布周期」,不写「已过期两年」 |
| C2 | 「CS 起薪涨 11.5%」单独出现(G11) | 同期 Overall 为 **+16.0%**;只给 +11.5% 会让读者以为 CS 起薪跑赢大盘,与数据相反。名义 +11.5% 与实际约 +4% 须并列 |
| C3 | 「BLS 软件开发者 +15%」与「+15.8%」混用(G16) | 前者是合并组、后者是单列职业,两个口径,必须并列区分 |
| C4 | 「软件岗位广告比疫情前低 30%」「+15% 反弹」(G17) | 实为**低约 27%**;且 +15% 的基期恰是序列谷底、由厂商事件选定,同一口径在不同抓取时点给出 +15% / +16.1% / +19.5% 三值(Indeed 回溯修订) |
| C5 | 「arXiv v5 **摘要**给出『仅 3%』『最多 49%』」(G18) | 归属错误:两个数在正文 Introduction,摘要里没有。三席一致点名为本条最严重错误。Science 版定版为 **1.8% / 46%**,80%/19% 须标预印本 β 口径 |
| C6 | 把 Canaries 的 16%、15 log points、6% 说成「三个口径互相印证」(G22) | 16% 与 15 log points 是**同一个**事件研究估计的两种写法,原稿把同一个数数了两次;6% 属最高**两个**五分位。且 13%→16% 是数据窗口延长,斯坦福 SIEPR 页至 2026-07 仍挂 13% |
| C7 | 把 EIG 的 <10%「计划采用」与 12%「实际采用」当同一指标(G23) | 不是同一指标;大企业定义为 250+ 员工;「与 Canaries 同源」只是 EIG 的 "We understand" 推定 |
| C8 | Johnston & Makridis 的三个系数(G24) | 三个全错:产出 **7%**(10% 是端点值)、4.8% 是**工资总额**非工资(人均仅 +1.0–1.1% 且劳动份额下降)、就业须按暴露类型拆分 |
| C9 | 引 Humlum & Vestergaard 的旧题名、1% 区间与「challenge narratives」句(G24) | 论文已改题、区间由 1% 放宽到 2%、该句已删;且其结论是**归因否定**而非现象否定 |
| C10 | 把 2025 届 ABA 类别写成 "Bar Passage Required"(G27) | ABA 已改名 "Bar Admission Required/Anticipated";跨年比较时这本身就是口径变更的一部分 |
| C11 | 石油工程「峰值 2,615」当普查数(G29) | 出自 Texas Tech(Lloyd Heinze)年度**自愿问卷**、经 SPE/JPT 报道,非 IPEDS 普查;官方序列峰值约 2,151,且两席的 IPEDS 序列整体错开一年。定案前只能写「2017–18 学年前后约 2,150 人」 |
| C12 | Taulbee「百分比变化的分母是两年均回应单位」(G30) | 2025 报告已改为 **2020–2025 六年平衡面板** |
| C13 | 数据科学布点「203」等媒体汇总年份值(G31) | 媒体依教育部附件人工汇总,非官方时序;一手复核后两年被订正(如 2018 年度实为 **196** 而非 203),2019 年度为扫描件、暂不可复核 |

### D · 选择性引用与射程越界

| # | 原表述 | 为什么禁用 |
|---|---|---|
| D1 | 只引 338 个细类的 MAPE 45.2%,不引 9 个大类的 5.86%(及 naïve 基准 13.8%)(G-extra) | 选择性引用,且与本篇批评「选择性引用」的立场自相矛盾。正确概括:**BLS 在大类层面的精度与朴素外推相当甚至更好,但在个人真正要选的那一级——细类职业——误差大到排序几乎失效(Spearman 0.43)** |
| D2 | 把 BLS "no comparable projections" 当作「没人评估过 BLS」的证据(G-extra) | 它说的是**没有可对标的独立预测**,不是没有独立评估。Stekler 正是在承认前者的同一篇里改用 naïve 基准完成了后者 |
| D3 | 「BLS 从未被外部审计」「BLS 拒绝外部评估」(G-extra) | BLS 自家刊物 MLR 主动刊出了这两篇外部批评,并配「always receptive to comment or criticism」的编者按 |
| D4 | 把 "BLS projection methods are not designed to capture extremely rapid technological change" 当独立引语(G2) | 被切掉的前后半句正是 BLS 的自辩(「因此我们假定技术变化速度与历史一致」),单引会读成 BLS 承认方法失效。且该文是 **BLS 评 BLS**,不是外部批评 |
| D5 | 把 "Each of the occupations in chart 1… had wages below the median for all occupations." 放在全经济前 15 榜之后(G7) | 三席全部点名。BLS 承认的只是**无学历要求档**的头部职业低薪,同文对更高学历档给出相反结论 |
| D6 | 把 EIG 的共线性发现当作「AI 暴露职业对利率更敏感」的证据(G23) | EIG 自己没证明这一步,且有两个来源(含独立第三方 Yale Budget Lab)测得**相反**方向 |
| D7 | 「0.01% / 0.09% 是最增强型(augmentation)分位」(G21) | 方向性错误:那是 augmentation **最低**两个分位 |
| D8 | 「执照/席位/师资三条件抑制护理过冲」当作判据(G34) | 判据过强,且与文章自身案例矛盾 |
| D9 | Freeman 的具体数字(G26) | 三席均判 UNVERIFIABLE,不得引具体值 |
| D10 | Bishop & Carter 的 MLR 1991-10 篇与 EEPA 13(3) 篇混引(G-extra) | 是两篇不同文章。评估 BLS 预测准确度只能引 **MLR 1991-10** 那篇 |
| D11 | 「20 个增长最快职业里只有 6 个真的最快」现在就当逐字数据引用(G-extra) | 口径不完整(判定基准与名单缺失、仅一席给出),**Round 3 补齐前不得承重**;需要这一层论证时改用 Spearman 0.43 |

---

## 送 Round 3 双席审计的单源承重实证(前半)

> 共 **21 条**。反证搜索席=找独立团队/独立数据的矛盾或证实测量并记录全部搜索角度(含未命中);方法学审计席=敌意审稿,**有否决权**,被否决的数字不得承重。

### 第一优先级 —— 文章核心论证压在上面,取不到就必须改写或删段

| 序 | 条目 | 需要审计什么 |
|---|---|---|
| 1 | **G32** 教育部 2025 年度普通高等学校本科专业备案和审批结果 | **三席均未取到一手**(第 1 席据教高函〔2026〕2 号判「尚未公布」;第 2 席由二手确证教高函〔2026〕3 号已于 2026-04 印发,但 moe.gov.cn 302 循环、Wayback 被禁;第 3 席 CDX 枚举无果且自陈额度耗尽)。必须取到**通知原文与附件 1**,点数 080717T 及全部 AI 相关代码并复算。**这是文章「可检验信号」一节的核心数据,取不到则该节必须改写口径** |
| 2 | **G-extra** Stekler & Thomas 的误差指标组 | ① 补齐 **MAPE 的分母定义**(相对实际就业水平还是相对实际增长率);② 核实「20 个最快里只有 6 个」的判定基准与名单;③ 确认 Spearman 0.43 的样本确为那 338 个细类;④ 评估「以 naïve share 模型为基准」是否足以支撑「大类预测尚可」;⑤ 反证搜索席穷尽确认「2005 年后无独立系统性量化评估」这一否定性主张;⑥ 复核 Bishop & Carter 的 44.5%/70%/87%(单席来源) |
| 3 | **G22** Canaries 的 16% | **必须双席**。未过审工作论文、数字在移动(13→16)、同机构两个官网口径打架。方法学审计席审 Poisson 设定、平行趋势、ADP 两道样本筛选、效应增长 vs 样本组成变化;反证搜索席找独立数据复现 |
| 4 | **G27** 法学院 2013 届 57.0% / 10.1% | 证据层级**不是**停在媒体转述:第 1、2 席回到 **Wayback 存档的 ABA 官方原始 PDF**(2014-07-02 快照)逐行读到 26,653/46,776=57.0%、4,715/46,776=10.1%,ABA 2014 年表脚注坐实测量时点 2014-02-15;但第 3 席因 americanbar.org 全站 403 且工具禁访 web.archive.org,完全无法复现。**层级=单源已核·经 Internet Archive 存档件**。需反证搜索席找第二条独立路径(建议 NALP《Jobs & JD's, Class of 2013》);取不到则成文必须标注存档层级 |
| 5 | **G5** 跨 SOC 版次(2010→2018)预测 vs 实际对照表 | **本批唯一由验证者自建且承重的量化表**,且 BLS 自己曾因分类改版放弃职业层面评估。审计:四行「严格一对一」判定是否穷尽(否则 −63.1% 与两处方向判反不得承重)、software developers +52%~+70.2% 区间上下界假设是否穷尽、15-0000 大组 +31%~+36% 未量化 15-1199→13-1082 流出、是否存在独立团队已发布的 SOC 回溯可比序列、以及单席发现的 Management +48.6% 反例 |
| 6 | **G24** 三份反方证据 | **必须双席**。反证搜索席定 Yale Budget Lab 的出版物序列与日期(引语出处三席冲突、其中一句两席查无实据);方法学审计席复核 Johnston & Makridis 正文系数——目前仅一席取得全文,属孤证 |

### 第二优先级 —— 单源承重数字或方法学脆弱点

| 序 | 条目 | 需要审计什么 |
|---|---|---|
| 7 | **G29** 石油工程峰值 | Heinze 问卷的抽样框与逐年应答项目数(「25 个项目回应」第 2 席在一手件中核不到,且与「20 所在办院校」自相矛盾);官方峰值年份两席错开一年(2017 vs 2018),须由方法学审计席从 NCES 原始 C20XX_A 重跑定案 |
| 8 | **G31** 中国数据科学布点逐年序列 | ① 2019 年度扫描件需 OCR 或人工翻页点数(唯一挡在完整一手序列前的年份,且落在浪峰下降段);② 2024 年度附件需按分节重数 080910T |
| 9 | **G14** CEW《The Major Payoff》 | ① 报告正文 5.3% 与 CEW 博客 4.3% 的机构内部矛盾,判定哪一版可承重、4.3% 是否为 multi/interdisciplinary studies 串味;② 该 detailed field 下辖 7 还是 8 个专业;③ 它与 NY Fed 同源、**不构成多源证实** |
| 10 | **G17** Indeed Hiring Lab 指数 | 回溯修订(2024-11 起改 Bundesbank 日频季调法并重算历史)导致 +15% / +16.1% / +19.5% 三值并存;需判定锁定哪一版,并以独立岗位广告数据复核 |
| 11 | **G13** EIG 的置信区间 | 单源承重区间估计 + 发布方有政策倡导利益;复核重复权重实现与区间宽度;「NY Fed 从未公布样本量/标准误」是无界否定命题,需反证搜索 |
| 12 | **G26** 蛛网底座 | 0.67 及其换算仅第 2 席经 Wayback 取得接受稿,需独立复现同一 PDF 并核对 0.014 / 2.07% / R²=0.02 / 脚注 29;Beffy 发表版是否有修订。取不到则 0.67 降级为「未经复现」 |
| 13 | **G20** Anthropic Economic Index | ① Amodei 的 Axios 表态一席因 403 未逐字取得;② 2026-07-24 Fortune 报道单席;③ 2026-03 换用 2019 版 O*NET 仅单席核到 |
| 14 | **G21** 暴露度构念引用链 | ① 「Anthropic 2026-03-05 的 coverage 架在 Eloundou β 之上」仅一席逐字取得,需第二席坐实;② Canaries 是否存在 2026 更新版,三席仅有 404 否定性证据 |
| 15 | **G9** 新 separations/openings 方法 | 「未检索到任何独立量化评估」是承重的**否定性主张**,须由反证搜索席穷尽搜索角度(州级 LMI 技术报告、AEA/JOLE/ILR Review 等)并记录未命中角度 |
| 16 | **G33** 撤销专业排行 | ① 麦可思 2020–2024 榜单的方法说明与底表来源必须索取或明写「未公开」;② 2024 年度 Top5 的原始出处仍未定位;③ 2020–2022 年度点数复算 |
| 17 | **G34** AACN 护理 | ① H-1B「4 年→1 年」补一手出处或删;② AACN《2024-2025 Enrollment and Graduations》原件页码级引用(80,162 目前只有 fact sheet 层级) |
| 18 | **G35** 三条自我否证材料 | ① LSAC 一手报告(2026 Composition Report / Post-LSAT Questionnaire)页码级引用——49%/37%/34%/55% 目前全经 ABA Journal 转述,第 3 席判 UNVERIFIABLE;② 路透 2025-10-15 的「申请 +33%」原文 |

### 第三优先级 —— 轻度,取不到即降级标注

| 序 | 条目 | 需要审计什么 |
|---|---|---|
| 19 | **G23** EIG 暴露度尺子 | 判定 EIG 的「GPT-4 β + 等权重」五分位与 Canaries 所用的 Eloundou 职业级 β 是否为**同一暴露度排序**(比对复现包的 core/supplemental 加权)。决定「两份反方证据是否独立」 |
| 20 | **G30** Taulbee 样本嵌套 | Table B1.a 的 41,858 与 2024 年报告 Table B4 的 41,912 是否同一字段定义(127 vs 134 单位);Overview 各表单位数(95/117)与 Highlights 队列的嵌套关系 |
| 21 | **G28** NIH ACD 引用链 | 1998 年 NRC《Trends in the Early Careers of Life Scientists》与 2011 年 NRC《Research Training in the Biomedical, Behavioral, and Clinical Research Sciences》原文三席均未取得;取不到则一律写「据 2012 年 NIH ACD 报告转述」。2012 报告本身三席逐字一致,无需再审 |
