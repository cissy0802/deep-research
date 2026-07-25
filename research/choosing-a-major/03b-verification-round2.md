# 03b · Round 2 对抗验证判决 — 后半(G36–G59)

> 4 批 × 3 席独立投票,共 72 票,model=opus,refute-by-default。
> 覆盖:执照护城河正反(G36–G41)、专业 vs 院校(G42–G47)、中国官方口径(G48–G53)、中国商业调查(G54–G59)。
> 票型:CORRECTED 66 / HOLDS 4 / REFUTED 2。**高修正率是 refute-by-default 的预期结果,不是论断质量差**——多数修正是口径限定语的收紧。


## 批次 E1 — verify:执照护城河正反


### 第 1 席


#### [G36] HOLDS · confidence=high

**核验依据**:我 curl 下载了 https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-outcomes-by-major-data.csv（2026-07-24 取得），并逐格核对：文件为 1 行表头 + 73 个专业 + 1 行 Overall。Nursing 行逐字为 `Nursing,2.147,12.781,70000,87000,30.292`；Overall 行为 `Overall,4.211,39.35,58000,87000,39.347`；`Computer Science,6.992,19.127,87000,120000,32.691`；`Elementary Education,1.18,16.213,45000,55000,50.596`。涨幅复算：87/70=+24.3%（文称 +24% ✓）、87/58=+50.0% ✓、120/87=+37.9%（+38% ✓）、55/45=+22.2%（+22% ✓）。

口径：https://www.newyorkfed.org/medialibrary/Research/Interactives/data/college-labor-chart-meta.json 的 `--#explore#outcomes-by-major` 逐字为 “releaseDateInfo: February 4, 2026, based on data from 2024”“Notes: Figures are for 2024. Unemployment and underemployment rates are for recent college graduates (that is, those aged 22 to 27 with a bachelor's degree or higher), and median wages are for full-time workers with a bachelor's degree only. Early career graduates are those aged 22 to 27, and mid-career graduates are those aged 35 to 45.” —— 与论断的括注（2024 ACS、22–27 岁学士及以上、中位工资仅全职且仅学士、mid-career 35–45）逐字吻合。Wayback CDX 交叉验证了口径年份：digest 在 2026-01-31 前为旧版（Nursing 1.422/9.672/65000/84000，2023 ACS），2026-03-03 起换为当前版本，即 2026-02-04 发布的 2024 ACS 版。

排序核验（我用 sort 复算）：低就业率最低五名 = Nursing 12.781 → Aerospace Eng 14.709 → Civil Eng 15.567 → Computer Eng 15.835 → Special Education 16.042，Nursing 确为 73 个专业中最低 ✓。失业率最低三名 = Special Education 0.739、Miscellaneous Education 1.089、Elementary Education 1.180，故 Elementary Education 是第 3 低，“全表最低之一”成立但不是最低。

“恰好等于”核验：Nursing 与 Overall 的 mid-career 中位工资在发布表中均逐字为 87000，是真相等而非四舍五入的假相等——但须加一条限定：全部 74 行 mid-career 值都是千元整数（early career 有 46600/45300/41600/49900/45200/47500 六个非整千值），故这是千元网格上的相等，底层中位数可能相差数百美元；且 Journalism 同为 87000。另外此“巧合”随口径年份摆动：2023 ACS 版为 Nursing 84000 vs Overall 83000（护理高 1000），2022 ACS 版两者同为 80000。Nursing 的中期工资在 73 专业中排第 32 位——正好落在中位附近，与论断方向一致。


#### [G37] CORRECTED · confidence=high

**修正**:（1）覆盖率分母错。原表述：“需持州执照才能合法从业的劳动力占比…升至 2008 年的约 29%”→ 正确表述：**州级**持照占比是 <5%（1950 年代初）→ **25%**（2008）；**29%** 是把地方与联邦执照一并计入后的“完全持照”占比，不是州级口径。白宫报告逐字：“the percentage of the workforce covered by State licensing laws grew from less than 5 percent in the early 1950s to 25 percent by 2008…the addition of local and Federal licensed occupations further raises the share of the workforce that is licensed to 29 percent.” NBER WP 14979 摘要逐字：“35 percent of employees were either licensed or certified by the government, and that 29 percent were fully licensed.” 另：2008 年那次调查是 **Westat**（2006 年那次是 Gallup），样本仅约 2,500 人。

（2）B 的标题过硬。原表述：“执照工资溢价对护士和教师**恰恰不成立**”→ 正确表述：Kleiner 原文只说“murky, with some studies finding small effects and others finding none”，即“证据模糊、小效应或无效应”，不是“不成立”。反证：Law & Marks, “What Are the Long Run Effects of Nurse Occupational Licensure?”（UC Riverside WP 201439, 2014）用各州分时立法的准实验发现 RN 执照有**正向且在其中一个设定下显著**的效应——“each additional year that registered nurse licensing is in place raises average real wages by almost $100 (in 2014 dollars), or…10 years of occupational licensing raises registered nurse wages by $1,000”。这正落在 Kleiner 所谓“small effects”一侧，因此 B 的引文本身成立，但中文标题需改为“对护士和教师，溢价证据模糊、量级很小”。

（3）14% vs 18%：本席只能一手证实 **14%**（NBER WP 14979 摘要逐字：“licensing is associated with about 14 percent higher wages”）。JOLE 2013 发表版（uchicago 10.1086/669060）被 Cloudflare 拦截，18% 未能回一手。建议正文只引 14% 并注明“NBER 工作论文口径”。

（4）“幅度 3–16%”须限定。白宫正文的“3 to 16 percent”只指 NP 与幼儿体检价格这**一项**，不是 11 项价格研究的幅度范围；且白宫自己的 Research Appendix Table 2 把 Kleiner et al. (2014) 记为 6.0（中度监管）与 16.0（高度监管），没有“3”；Kleiner 2015 THP 正文对同一篇论文又写成“raises prices of well-child exams by **10 percent**”。同一底层研究出现 3–16 / 6 与 16 / 10 三套数字，引用时必须指明取自哪一处。另：“11 项价格研究”实为 Appendix Table 2 中 **5 篇论文的 11 个估计**（Kleiner & Todd 的 2 行被正文以“In addition to the studies listed below”排除在计数外，13 行 − 2 = 11，其中 9 行显著更高价 ✓），而这 5 篇里有 4 篇是 1978–2000 年的**牙科**研究，只有 Kleiner et al. (2014) 一篇涉及护理。

（5）D 的推论方向错。原表述：“限制 NP 独立执业权的执照规则，损害的是 NP 自己”→ 白宫与 Kleiner 引用该发现时的落点是**消费者付更高价格**（幼儿体检价涨 3–16%），不是 NP 自身收入。若要主张“损害 NP 自己”，需另引 Kleiner et al. (2014) 关于 NP 工资的系数，本批材料未提供。

（6）利益相关须补标：南卡 12%/爱荷华 33% 的州际极差来自“a new Harris survey used by Kleiner and Vorotnikov (2015)”——商业民调机构的自报调查，不是官方统计（表内精确值 South Carolina 12.4、Iowa 33.3）。白宫报告同时给出一个更保守的官方对照：Census SIPP（n≈58,000，2012 年秋）显示“28 percent of civilian workers aged 18 through 64 had attained a license or certification…and about 20 percent were licensed”，即官方大样本口径下持照率约 20%，远低于 29%。Kleiner 本人是执照批评方，两份报告（Hamilton Project / 奥巴马白宫 CEA）均属政策倡导文本，须打折。

**核验依据**:一手件：Kleiner, “Reforming Occupational Licensing Policies”, The Hamilton Project (https://www.brookings.edu/wp-content/uploads/2016/06/THP_KleinerDiscPaper_final.pdf)，我自行下载并 pdftotext。
• B 引文逐字核到（p.12–13）：“…For occupations associated with both higher education and higher income and that are mainly in the private sector, such as physicians, dentists, and attorneys, licensing appears to have large effects by limiting entry or making it more difficult for an individual to be hired for a job in another state. However, for other occupations, including teachers, nurses, and cosmetologists, the impact of licensing on earnings is murky, with some studies finding small effects and others finding none (Kleiner 2006, 2013).” 注意论断引文省略了“by limiting entry or making it more difficult for an individual to be hired for a job in another state”，这句把“large effects”限定在**进入/流动**而非单纯收入上，省略后语义被放大。
• C 引文逐字核到：“working in a universally licensed occupation appears to increase hourly earnings by between 10 to 15 percent relative to unlicensed individuals with similar education and skills… For individuals working in an occupation that is licensed in some states and not in others, the impact of being licensed is much smaller, about 5 to 8 percent.” 注意是 **hourly earnings**。“识别更干净的一组”是文章自己的推断，Kleiner 原文未如此表述。
• “5–33%”核到：“The impact on prices of licensing-related practices ranges from 5 to 33 percent, depending on the type of occupational practice and location (Kleiner 2006).”

白宫 2015 报告（https://obamawhitehouse.archives.gov/sites/default/files/docs/licensing_report_final_nonembargo.pdf）：
• 覆盖率见正文与第 17 页；“About two-thirds of this change stems from an increase in the number of professions that require a license, with the remaining growth coming from changing composition of the workforce.” ✓
• 质量计票：“Stricter licensing was associated with quality improvements in only 2 out of the 12 studies reviewed.” 我复核 Research Appendix Table 1：14 行、12 篇不同论文，标 “Increase in quality” 的恰为 Larsen (2015) 高收入学区与 Holen (1978) 两项 → 12/2 精确对得上 ✓。
• 价格计票：“In 9 of the 11 studies we reviewed (see Research Appendix Table 2), significantly higher prices accompanied stricter licensing.” 我复核 Table 2：13 行，扣除脚注 131 单独处理的 Kleiner & Todd 两行后余 11 行，其中 9 行显著更高价 ✓（另 2 行为 −1.0 与 No effect）。
• NP 价格：“more restrictive State licensing of nurse practitioners raises the price of a well-child medical exam by 3 to 16 percent”（正文）vs Appendix Table 2 的 6.0 / 16.0（矛盾，见 correction）。
• 州际极差与来源：“ranging from a low of 12 percent of workers in South Carolina to 33 percent in Iowa… using a new Harris survey used by Kleiner and Vorotnikov (2015)”；Table 1 精确值 SC 12.4、IA 33.3。

NBER WP 14979 摘要（https://www.nber.org/papers/w14979，2009 年 5 月，致谢中鸣谢 Westat）。

E（HOLDS）：NBER WP 24107（https://www.nber.org/system/files/working_papers/w24107/w24107.pdf，即 Johnson & Kleiner, AEJ:EP 12(3): 347–73, 2020，已在 https://www.aeaweb.org/articles?id=10.1257/pol.20170704 核到卷期页码）。摘要逐字：“the between-state migration rate for individuals in occupations with state-specific licensing exam requirements is 36 percent lower relative to members of other occupations. Members of licensed occupations with national licensing exams show no evidence of limited interstate migration.” 正文：state-specific 组 −36%，quasi-national 组 **+5%**。Table 1“Universally licensed occupations identifiable in the ACS”把 **Nurse (RN/LPN) 明确列在 quasi-national（全国统考）列**，脚注来源即 https://www.ncsbn.org/licensure.htm；Elementary/secondary teacher 列在 state-specific 列，且分职业结果中“Pharmacists and teachers have the lowest relative rates, at −47 and −39 percent”。论文还引 DePasquale & Stange（NBER WP 22344）指出 NLC 的采纳“does not affect the labor supply or the geographic mobility of nurses”。因此“护士不适用”不仅成立，且论文明确把护士归为不受影响那一组。
NLC 辖区数：NCSBN 官方 https://www.nursecompact.com/（版权页署 National Council of State Boards of Nursing）逐字“**43 jurisdictions are currently part of the NLC.**”（2026-07-24 取得），页面附星号“* See additional implementation status information”，即 43 家中部分为已立法未实施，正文宜写“43 个参与辖区（含部分尚未实施）”。

反证检索：Law & Marks, UC Riverside WP 201439（https://economics.ucr.edu/repec/ucr/wpaper/201439.pdf），摘要与正文见 correction。该文结论偏“公共利益理论”，与 Kleiner 立场相反，属独立反向证据。


#### [G38] CORRECTED · confidence=high

**修正**:数字全部逐字无误，但**标题与两处标注需修**：

（1）原表述：“BLS 数字不支持‘医疗是最高增长赛道’”→ 正确表述：在 BLS 大类口径下，**医疗支持类（healthcare support）+12.4% 恰恰是 22 个大类中增长最快的一个**，计算机与数学类 +10.1% 只排第二（新闻稿自己写的就是“second fastest”）。绝对增量差距更大：两个医疗大类合计 +1,715,200 个岗位（726,900 + 988,300），计算机与数学类只有 +545,600。可承重的表述应是“医疗最高增长的那一档是低薪的医疗支持类（中位 $37,180），执业与技术类只有 +7.2%”，而不是“BLS 不支持医疗是最高增长赛道”。

（2）原表述：“BLS OOH 2024–2034 全部下降”后紧跟“中位年薪…学前 $37,120”→ 学前教师并不下降：Preschool teachers 2024 年 555,100 人、Job Outlook +4%（As fast as average）、+22,900。把学前薪资混进“全部下降”那一段会误导，需在薪资行注明“学前教师为 +4%，不在下降之列”。

（3）原表述：“小学 $62,310”→ $62,310 是 OOH “Kindergarten and Elementary School Teachers” 合并职业的中位数；同页 Pay 段落给的分项是“elementary school teachers, except special education $62,340”“kindergarten teachers, except special education $61,430”（2024 年 5 月）。

（4）原表述：“教育与图书馆大类整体年均缺口高达 890,300 个”→ 大类正式名称是 **Educational instruction and library occupations（SOC 25-0000）**，且它**整体是微增不是下降**：9,813,200 → 9,875,400，+62,200，**+0.6%**，年均缺口 890,300，中位年薪 $59,220。OOH 大类页逐字为“Overall employment in educational instruction and library occupations is projected to grow slower than the average… Despite limited employment growth, about 890,300 openings are projected each year”。“缺口≠岗位增长”的核心推论成立，但“大类下降”不成立。

（5）“低失业与负增长并存，因为**供给端萎缩得同样快**”——本席**未能**回到一手（Title II / IPEDS 师范生完成人数）证实供给萎缩，title2.ed.gov 取不到、本会话搜索额度已用尽。BLS 自己给出的解释只有替补需求：OOH 逐字只说全部 103,800 个缺口来自替补，未提供给端。建议正文把“因为供给端萎缩得同样快”降格为待证假说，或改为 BLS 口径的可承重表述：“1,539,800 的存量每年产生 103,800 个替补缺口（约 6.7% 的年周转），替补流量本身就足以吸收新毕业生”。

**核验依据**:新闻稿（bls.gov 直取 403，改用 Wayback id_ 快照 https://web.archive.org/web/20260723110547id_/https://www.bls.gov/news.release/ecopro.nr0.htm，USDL-25-1324，2025 年 8 月 28 日发布）逐字：
• “Total employment is projected to increase to 175.2 million and grow 3.1 percent” ✓
• “healthcare support occupations and healthcare practitioners and technical occupations are projected to be among the fastest growing occupational groups, growing 12.4 percent and 7.2 percent, respectively” ✓
• “Computer and mathematical occupations are projected to grow the second fastest of any occupational group (+10.1 percent), which is more than three times the average rate of growth projected for the total economy (+3.1 percent).” ✓ 论断引文逐字无误。

我另下载了 BLS 就业矩阵 occupation.xlsx（https://web.archive.org/web/20260612175342id_/https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx），用 openpyxl 对 Table 1.1 按增速排序：Healthcare support 12.4（$37,180）> Computer and mathematical 10.1（$105,850）> Healthcare practitioners and technical 7.2（$83,090）> Community and social service 6.6 > Management 6.1。Table 1.2 中 Educational instruction and library occupations (25-0000)：9,813.2 → 9,875.4 千人，+62.2，+0.6%，年均缺口 890.3 千，中位 $59,220。

四个 OOH 教师页（均取 2026 年 6 月 Wayback id_ 快照）Quick Facts 逐格核对，全部命中：
• kindergarten-and-elementary-school-teachers：$62,310 / 1,539,800 / −2% (Decline) / −29,800 ✓
• middle-school-teachers：$62,970 / 633,700 / −2% / −12,400 ✓
• high-school-teachers：$64,580 / 1,094,500 / −2% / −17,800 ✓
• special-education-teachers：$64,270 / 559,500 / −1% / −7,700 ✓
• preschool-teachers：$37,120 / 555,100 / **+4% (As fast as average)** / **+22,900**（见 correction 第 2 条）
引文逐字核到：“Despite declining employment, about 103,800 openings for kindergarten and elementary school teachers are projected each year, on average, over the decade.”“All of those openings are expected to result from the need to replace workers who transfer to other occupations or exit the labor force, such as to retire.”（论断引文省略了结尾“, such as to retire”）。
890,300 出自 OOH 大类页 https://web.archive.org/web/20260614022427id_/https://www.bls.gov/ooh/education-training-and-library/home.htm，逐字见 correction 第 4 条。
NY Fed 小学教育失业率 1.18%（1.2%）已在 G36 核实。


#### [G39] CORRECTED · confidence=high

**修正**:BLS 部分（论断 A）逐格无误，**HRSA 部分（B、C）存在两处口径错误**：

（1）B 用的是**已被官方取代的旧版**。原表述：“HRSA 预测 NP 2036 年供给 652,870 FTE vs 需求 340,830 FTE，充足率 192%（2026 年 132%、2031 年 164%）。麻醉护士 2036 年 118%、助产士 139%”→ 这些数字确实逐字出自 HRSA《Nurse Workforce Projections, **2021-2036**》（**2024 年 3 月**版，基年 2021、含疫情数据），但 HRSA 已于 **2025 年 12 月**用《Nurse Workforce Projections, **2023-2038**》（基年 2023）取代它。新版对应数字应为：NP **2028 年 126%**（供给 501,010 / 需求 399,200）、**2033 年 152%**（638,990 / 420,250）、**2038 年 175%**（**供给 766,260 FTE / 需求 437,330 FTE**）；麻醉护士 2028/2033/**2038 = 102% / 108% / 113%**；助产士 **104% / 123% / 140%**。采集者未取得的 2038 年 NP 数字，本席已从新版简报补齐。文章 C 段刚刚批评“流传的 30 万缺口引自已被取代的旧版”，B 段自己却仍在引同一份旧版，必须统一到 2025-12 版（过剩结论方向不变，但幅度从 192% 降到 175%）。

（2）C 的医师地理数字张冠李戴。原表述：“医师 2038 年缺口 141,160 名（**非都会区初级保健 39%**，都会区 5%）”→ HRSA 2025-12《Physician Workforce Projections》里**没有 39% 这个数**、也没有“primary care”的都会/非都会拆分。原文逐字是：“The percent adequacy of supply across all physician specialties is projected to be **42% in nonmetro areas (a shortage of 58%)**, compared to **95% in metro areas (a shortage of 5%)** in 2038.” 即：全科别口径下非都会区短缺 **58%**、都会区 5%；初级保健医师 2038 年全国缺口为 **70,610 FTE**（无都会/非都会百分比）。（旧的 2024-11 版对应值是 40% 充足率 / 近 60% 短缺 vs 都会区 90% 充足率 / 10% 短缺，同样不是 39%/5%。）建议改为“医师 2038 年全国缺口 141,160 FTE；非都会区短缺 58%，都会区仅 5%”。

（3）两处可加固的小口径：① RN 增速，OOH 页面显示“5% (Faster than average)”，就业矩阵的精确值是 **4.9%**；② 文章说“年均缺口 32,700 是合并组的数字，不能挂在 NP 名下”——这条提醒正确，但可以直接给出 NP 单职业的官方数：BLS Table 1.2 中 29-1171 的 **年均缺口 = 29,500**（29.5 千），不必只做否定式表述。

**核验依据**:BLS：我下载了 https://web.archive.org/web/20260612175342id_/https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx（bls.gov 直取 403），用 openpyxl 逐行读取。Table 1.3“Fastest growing occupations”与 Table 1.2 中：
• Nurse practitioners 29-1171：320.4 → 448.8，+128.4，+40.1%，中位 $129,210；年均缺口 29.5 千；入职学历 Master's degree ✓
• Software developers 15-1252：1,693.8 → 1,961.4，+267.7，+15.8%，$133,080；年均缺口 115.2 千 ✓
• Physician assistants 29-1071：162.7 → 195.8，+33.2，+20.4%，$133,260 ✓
• Home health and personal care aides 31-1120：4,347.7 → 5,087.5，+739.8，+17.0%，$34,900 ✓
• Registered nurses 29-1141：3,391.0 → 3,557.1，+166.1，**4.9%**，年均缺口 189.1 千，$93,600
表中 NP 在“最快增长职业”里排第 3（前两名 wind turbine service technicians 49.9%、solar photovoltaic installers 42.1%），“增长最快的职业之一”成立。软件开发中位薪 $133,080 > NP $129,210 ✓。
OOH 页（Wayback id_ 快照）：Registered Nurses = $93,600 / 3,391,000 / 5% (Faster than average) / +166,100，“About 189,100 openings for registered nurses are projected each year” ✓；Nurse Anesthetists, Nurse Midwives, and Nurse Practitioners = $132,050 / 382,700 / 35% (Much faster than average) / +134,000，“About 32,700 openings for nurse anesthetists, nurse midwives, and nurse practitioners are projected each year” ✓——确为合并组。

HRSA（bhw.hrsa.gov 直取 403，全部改用 Wayback id_ 快照）：
• 2025-12 版护理简报 https://web.archive.org/web/20260722231528id_/https://bhw.hrsa.gov/sites/default/files/bureau-health-workforce/data-research/nursing-projections-factsheet.pdf，标题“Nurse Workforce Projections, 2023-2038 / December 2025”。逐字：“there is a projected 8% shortage of registered nurses (RNs) in 2028. By 2038, the shortage is 3% (a shortage of **108,960** full-time equivalent [FTE] RNs)”✓；“Nonmetro areas… **11% vs 2% in 2038**”✓；LPN 2038 短缺 **245,950** FTE ✓；“At the national level, the supply of nurse practitioners (NPs) is projected to exceed demand over the projection period; however, distribution remains the most important issue.” ✓ 逐字。Exhibit 1a/1b/1c 给出 NP 126% / 152% / 175%、麻醉护士 102% / 108% / 113%、助产士 104% / 123% / 140%（见 correction）。
• 2024-03 旧版 https://web.archive.org/web/20240510094621id_/…/nursing-projections-factsheet.pdf，标题“Nurse Workforce Projections, **2021-2036** / March 2024”，逐字：“By 2036, the shortage is 9% (a shortage of **337,970** full-time equivalent [FTE] RNs)”；LPN 2036 短缺 **99,070** FTE；Exhibit 1c 中 NP 供给 652,870 / 需求 340,830 / 充足率 **192%**，麻醉护士 **118%**，助产士 **139%**；Exhibit 1a/1b 中 NP 2026 **132%**、2031 **164%**。—— 论断 B 与 C 中“下修三倍（337,970 → 108,960）”“LPN 反而扩大（99,070 → 245,950）”均一手核实无误。
• 2025-12 版医师简报 https://web.archive.org/web/20260724171413id_/…/physicians-projections-factsheet.pdf：2038 年供给 1,010,060 / 需求 1,151,220 / 短缺 **141,160** / 充足率 88% ✓；地理段逐字见 correction。我在该 PDF 全文 grep 过 “39”“primary care”，**零命中**。HRSA 官网页（https://web.archive.org/web/20260711190554id_/https://bhw.hrsa.gov/data-research/projecting-health-workforce-supply-demand）另注明初级保健医师 2038 缺口 70,610。

口径辨析（BLS 测已实现就业≈需求侧，HRSA 分别建模供需，两者不必然矛盾）——本席认同，这一段写法正确。


#### [G40] CORRECTED · confidence=high

**修正**:NCSBN 侧（A、C）逐字全对；**NSI 侧（B）峰值年份错、且掩盖了最新一年的反转；回收率区间也低估了问题严重性**：

（1）原表述：“NSI 报告的医院 RN 实际离职率从 **CY2022 峰值 27.1%** 降至 CY2025 17.6%”→ 正确表述：峰值是 **CY2021 的 27.1%**。NSI 2026 报告《HOSPITAL STAFF RN TURNOVER RATE》图逐年序列为 **CY21 27.1% → CY22 22.5% → CY23 18.4% → CY24 16.4% → CY25 17.6%**（同图 FT/PT-only 口径为 22.5 / 18.2 / 15.0 / 13.5 / 14.6）。

（2）更要紧的是方向：**CY2025 是回升，不是继续下降**。NSI 正文逐字：“RN turnover is recorded at 17.6%, **a 1.2% increase**”“This is a 1.2% annual increase and **directly responsible for the bump in hospital turnover**”“Of note is that **RN retirement is on the rise** and frequently cited as why nurses voluntarily resigned.” 医院全员离职率 18.5% 也是“a nominal increase from CY24（18.3%）”。因此“行为指标与意向指标方向相反”这一论断只在 2021→2024 段成立，到 CY2025 已经反转——而且反转的驱动因素（退休上升）恰好与 NCSBN 意向数据中 21.9pp“计划退休”那一半同向。原表述“行为指标方向相反”需改为“行为指标在 2021–2024 大幅回落、2025 年小幅回升 1.2 个百分点”。

（3）原表述：“NCSBN 2024 调查各州回收率仅约 **9–22%**（加州 RN 14.0%、LPN/LVN **最低 9.1%**）”→ 这只覆盖了 24 个辖区的**邮寄**部分（该部分合计 RN 16.9%、LPN/LVN 13.7%；州级区间 RN 8.2%–22.3%、LPN/LVN 8.6%–20.6%）。另有 18 个辖区走**电邮**问卷，回收率低得多：合计 **RN 9.7%、LPN/LVN 7.4%**，州级最低为**新罕布什尔 LPN/LVN 2.2%**、华盛顿特区 LPN/LVN 2.9%、罗德岛 3.9%、犹他 4.1%、佛州 RN 5.8%。此外还有 10 个辖区**根本没做问卷**（直接取 Nursys e-Notify 记录），夏威夷用的是州内部调查。正确表述应为：“两种问卷模式的州级回收率区间约 **2.2%–22.3%**，电邮组整体不足 10%；另有 10 个辖区无问卷、由行政记录补入。”把 39.9% 视为上界的判断因此更有理据，但理据要写对。

**核验依据**:NCSBN 一手：https://www.journalofnursingregulation.com/article/S2155-8256(25)00047-X/fulltext 直取被 Cloudflare 拦（403），改用 Wayback id_ 快照 https://web.archive.org/web/20251008232225id_/…/fulltext 取到全文（Journal of Nursing Regulation, Vol 16, Issue 1, Supplement, S1–S88, April 2025）。逐字核对：
• Table 27“Plans of RNs for the Next 5 Years, 2020–2024”：Yes 2020 **22.1**（n=7,584.5）/ 2022 **28.7**（62,234.8）/ 2024 **39.9**（216,151.3）；“I plan to retire” 2024 = **21.9**（118,480.0）；“I plan to leave nursing” 2024 = **18.0**（97,671.3）；No 2024 = 60.1 ✓（21.9+18.0=39.9）。
• 表注逐字：“This question was introduced in the 2020 survey and **modified in 2024** to offer separate options for those who plan to retire, and those who plan to leave nursing.” ✓ 与论断引文完全一致。
• 正文逐字：“Approximately 40% of RNs reported they plan to retire or leave nursing within the next 5 years, **a 11.2% increase** over the proportion who reported similar intentions on the 2022 survey (28.7%).” ✓ 39.9 − 28.7 = 11.2 个百分点，原文把百分点差写成 “increase”，论断对这处措辞歧义的指认成立。
• 中位年龄：“The median age of both RNs and LPNs/LVNs was **50 years**” ✓。
• 倦怠（Table 52）：“The proportion of RNs reporting they feel burned out from work either every day or a few times per week decreased from **45.2% in 2022 to 35.4% in 2024**.” ✓ 情绪耗竭（Table 49）“Every day”：2022 **23.9%** → 2024 **18.9%** ✓。
• 摘要逐字：“While reported levels of emotional exhaustion, including burnout, and workloads have **moderated** over the past 2 years, about 40% of nurses report they plan to leave nursing or retire over the next 5 years.” ✓
• 抽样：Table 1（邮寄，24 辖区）Total 行 = RN 95,567 寄出 / 16,146 回 / **16.9%**；LPN/LVN 96,354 / 13,174 / **13.7%**；加州 RN **14.0%**、加州 LPN/LVN **9.1%** ✓（但非最低）。Table 2（电邮，18 辖区）Total 行 = RN 121,685 / 11,804 / **9.7%**；LPN/LVN 121,682 / 8,956 / **7.4%**；我用正则抽全部州行复算，RN 最低 FL 5.8%、最高 NH 17.9%，LPN/LVN 最低 **NH 2.2%**、最高 AZ 11.2%。方法段逐字：“A survey was mailed to a randomized sample… in 24 jurisdictions, supplemented by an email-based survey… in 18 jurisdictions, and data from Nursys e-Notify for 10 jurisdictions.”

NSI 一手：我自行从官网下载 https://www.nsinursingsolutions.com/Documents/Library/NSI_National_Health_Care_Retention_Report.pdf（2026-07-24，19 页，md5 4d115040bf44867b2a958e6fccf35d8a），标题“2026 NSI National Health Care Retention & RN Staffing Report”。
• 离职率序列见 correction（两张图逐格读出）。
• 空缺率：“the RN vacancy rate… currently stands at **8.6%**”；表内历年 AVERAGE = 2022 17.0% / 2023 15.7% / 2024 9.9% / 2025 **9.6%** / 2026 *8.6%；星号脚注逐字：“*The RN Vacancy Rate in previous reports were based on the average of the range selected. Beginning 2026, NSI collected data on RN FTEs filled & vacant, and modified the formula to where RN Vacancy Rate = (Unfilled RN FTEs/Budgeted FTEs)*100.” ✓ 论断对“口径已改、不可直接比较”的标注完全正确。
• 利益相关全部核实：“the average cost of turnover for a bedside RN is **$60,090**”；“NSI estimates the current national RN shortage at **158,600**”；“**Every RN hired saves $66,081.** An NSI contract to replace 20 travel nurses could save your institution $1,322,000… **Contact Michael Colosi at (717) 575-7817** to learn how NSI can improve your bottom line.” ✓ 逐字。方法段：“acute care hospitals were **invited to participate**… **527 hospitals from forty states** responded”——自愿报名、非概率抽样，论断标注成立。


#### [G41] CORRECTED · confidence=high

**修正**:九个评分与两段限定语逐字全对，评分构造的推测也对；**三处口径需收紧**：

（1）原表述：“数据窗口为 2024 年 Copilot 对话”→ 正确表述：**2024 年 1 月 1 日至 9 月 30 日**（9 个月），论文逐字“gathered from January 1, 2024 to September 30, 2024”。

（2）原表述：“基于 20 万条经匿名化的 Bing Copilot 真实人机对话”→ 数字本身是摘要原话，但结构须交代：这 20 万条是**两个各 10 万条的样本**——主样本是均匀抽样的约 10 万条（用于覆盖度与影响范围），辅样本是**从获得过点赞/点踩反馈的对话中抽的 10 万条**（用于测算“完成度”），后者不是代表性样本。且数据来自**免费消费级 Bing Copilot**（论文自述“a mainstream, publicly available, free-to-use generative AI chatbot”），不是企业版 Copilot，用它推断职业内的实际工作行为存在选择性。就业权重取自 **2023 年 OEWS**。

（3）原表述：“中小学教师（0.18）**高于**律师（0.17）”“大学教师（0.31）**高于**计算机职业（0.29）”→ 数值上确实如此，但差距只有 **0.01 与 0.02**，论文对这些 SOC 次要组评分**未报告置信区间或标准误**，两位小数的排序差不可承重。面向准大学生的文本应改为“中小学教师（0.18）与律师（0.17）基本持平，都明显高于医疗诊疗执业者（0.13）”“大学教师（0.31）与计算机职业（0.29）处在同一档”。真正稳健、也真正支撑论断的是那道**大缺口**：教育口 0.18–0.31 vs 医疗照护口 0.04–0.13，量级差 3–7 倍。

另需补两点：① 医疗内部并不齐平——“Other Healthcare Pracs. and Tech. Occs.”为 **0.16**、“Health Technologists and Technicians”为 0.10，写“护理阵营”时不宜整体化；② 该文**至今仍是预印本**：arXiv v1 为 2025-07-10、v6 为 2025-12-22，arXiv 页面无 journal-ref，微软研究院自己的出版物页面把它标为“Preprint”，无证据显示已通过同行评审。

**核验依据**:一手件：arXiv:2507.07935v6（https://arxiv.org/pdf/2507.07935v6，我自行下载后 pdftotext -layout）。abs 页 https://arxiv.org/abs/2507.07935 逐字：“[Submitted on 10 Jul 2025 (v1), last revised 22 Dec 2025 (this version, v6)]”，Comments 仅“40 pages”，无 journal-ref。

Table 1“SOC minor groups by AI applicability score”逐格核对，九个数字全部命中：Healthcare Diagnosing or Treating Pracs. **0.13**；Home Health Aides and Nursing Assts. **0.04**；Occupational and Physical Therapy Assts. **0.05**；Other Healthcare Support Occupations **0.06**；Prim., Second., and Special Ed. Teachers **0.18**；Postsecondary Teachers **0.31**；Computer Occupations **0.29**；Mathematical Science Occupations **0.32**；Lawyers, Judges, and Related Workers **0.17**。（同表另有 Other Healthcare Pracs. and Tech. Occs. 0.16、Health Technologists and Technicians 0.10。）

评分构造：Table 1 表注逐字回答了论断提出的问题——“Score is the employment-weighted average AI applicability score for each specific occupation in the SOC minor group, **averaging the mean of the user goal and AI action scores**.” 正文 §2.2 与 §4.4.2 补充：分数由 IWA 层的 coverage（频率阈值 ≥0.05%）、completion、scope 三项聚合，并按 O*NET 任务重要性/相关性加权到 SOC 职业，再按就业加权到次要组；“We compute AI applicability score separately for user goals and AI actions, averaging the two when we need a single score.” 故论断的推测**成立**。

限定语逐字核到（§3 讨论）：“It is tempting to conclude that occupations that have high AI action applicability score will be automated and thus experience job or wage loss, and that occupations with high user goal applicability score will be augmented and raise wages. **This would be a mistake**, as downstream consequences of new technologies are very hard to predict and often counterintuitive (33).” ✓（论断的省略号处省掉的是“and that occupations with high user goal applicability score will be augmented and raise wages”，未改变语义。）

配套博客逐字核到：微软研究院 “Applicability vs. job displacement: further notes on our recent research on AI and occupations”（直取被限流，改用 https://web.archive.org/web/20251025005004id_/https://www.microsoft.com/en-us/research/blog/applicability-vs-job-displacement-further-notes-on-our-recent-research-on-ai-and-occupations/）：“**our study does not draw any conclusions about jobs being eliminated; in the paper, we explicitly cautioned against using our findings to make that conclusion.**” ✓

数据段（§4.1）逐字：“We analyze anonymized and privacy-scrubbed U.S. conversation data from Microsoft Bing Copilot… gathered from **January 1, 2024 to September 30, 2024**… Our main dataset is a uniform sample of approximately **100k** conversations… We use a supporting dataset of **100k** conversations uniformly sampled from **those that received at least one thumbs up or thumbs down reaction**…”；§4.2：“We combine O*NET with data on wages and employment from the **2023** Occupational Employment and Wage Statistics data.” 利益相关：作者五人全部为 Microsoft Research，数据为微软自有产品日志，IRB #11028，聚合指标开源于 https://github.com/microsoft/working-with-ai——AI 厂商自测自家产品对职业的适用度，须标注。


### 第 2 席


#### [G36] CORRECTED · confidence=high

**修正**:(1) 「Elementary Education 失业率 1.180%(全表最低之一)」→ 全表第 3 低。Special Education 0.739% 第 1、Miscellaneous Education 1.089% 第 2。最低的那个也是教育类专业,这一点反而强化论点,但不能写成「最低」。(2) 「护理的 35–45 岁中位工资($87,000)恰好等于全体专业的中位数」→ 两值在已发布精度上确实同为 $87,000,但 NY Fed 该列全部按千元取整(Journalism 也是 $87,000),这是取整后的重合,不是可承重的「恰好相等」。应写成「同为 $87,000(均按千元取整)」,不要用「恰好」「巧合」这类暗示精确等式的措辞。(3) 建议补一条对读者更重要的口径:护理的失业率 2.147% 在 73 个专业中只排第 10,并不突出;它真正独一档的是低就业率 12.781%(第 2 名 Aerospace Engineering 14.709%)。把「确定性」挂在失业率上会被数据打脸,挂在低就业率上才成立。(4) 其余逐格无误:Nursing 2.147/12.781/70,000/87,000;Overall 4.211/39.350/58,000/87,000;CS 87,000→120,000(+37.9%,称 +38% 可);Elementary Education 1.18/45,000→55,000(+22.2%)。涨幅 +24%/+50%/+22% 均与原始值自洽。

**核验依据**:直接下载 https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-outcomes-by-major-data.csv(2026-07-24 取),74 行数据 = 73 个专业 + 「Overall」行(文件首尾各出现一次)。程序化排序结果:低就业率升序前 6 = Nursing 12.781、Aerospace Engineering 14.709、Civil Engineering 15.567、Computer Engineering 15.835、Special Education 16.042、Elementary Education 16.213 —— Nursing 确为 73 个专业最低,成立。失业率升序前 8 = Special Education 0.739、Miscellaneous Education 1.089、Elementary Education 1.18、Agriculture 1.395、Foreign Language 1.579、Geography 1.6、Engineering Technologies 1.74、Social Services 1.943;Nursing 排第 10。中期工资 = 87000 的专业恰为 Journalism 与 Nursing 两个。注:NY Fed 说明页 https://www.newyorkfed.org/research/college-labor-market 对本机 WebFetch 返回 403,故「2024 ACS / 22–27 岁 / 35–45 岁 / 仅全职 / 仅学士」这组定义未能回到一手页面逐字确认,仅 CSV 数值经过核对;引用时应保留该定义出处的不确定性。


#### [G37] CORRECTED · confidence=high

**修正**:最重要的一处:(1) 论断 E 张冠李戴。「Johnson & Kleiner(AEJ:EP 12(3), 2020)……低 36%」→ 36% 出自 NBER Working Paper w24107(2017-12)摘要;已发表的 AEJ:EP 12(3):347–73 (2020) 摘要里根本没有 36% 这个数,其偏好设定(preferred specification,仅限长距离迁移者、对照组为全国统考持照职业)给出的是 **低 7%**,而不做长距离限制的朴素估计是 −58%。即:经同行评审发表的那一版,系数比流传的 36% 小五倍。应改为「Johnson & Kleiner 的工作论文(NBER w24107, 2017)报 36%(对照组=其他所有职业);其 2020 年 AEJ:EP 发表版偏好估计为 7%(对照组=全国统考持照职业)」,或直接改用 7% 并注明。(2) 论断 B 的省略号删掉了要害。原文完整为:「licensing appears to have large effects **by limiting entry or making it more difficult for an individual to be hired for a job in another state**. However, for other occupations, including teachers, nurses, and cosmetologists, the impact of licensing **on earnings** is murky…」—— 前半句的「large effects」说的是**进入门槛与跨州流动**,不是工资。照现在的省略方式,读者会以为 Kleiner 在做「医生律师有工资溢价 vs 护士教师没有」的同口径对比,原文并非如此。必须把 by limiting entry… 补回去。(3) 论断 E 遗漏了对本文最有用的一半:Johnson & Kleiner Table 1 明确把 **Elementary/secondary teacher 列入 state-specific(州专属考试)组**,把 **Nurse (RN/LPN) 列入 quasi-national 组**。所以流动性惩罚不是「护士不适用」而已,是「护士豁免、教师正中靶心」。(4) 论断 A 的 29% 与 25% 是两个口径,不能并列而不说明:Kleiner 2015 的「almost 29 percent(2008)」引 K&K 2013、含各级政府;白宫报告的 25% 明确限定为 **州级**持照(原文:「about 25 percent of today's U.S. workforce is in an occupation licensed at the State level… this share is higher when local and Federal licenses are included」)。另,州际极差精确值为南卡 12.4%、爱荷华 33.3%,且来自 Harris 民调自报,应标注。(5) 论断 C 的 14 / 18 之争定论:14% 出自 NBER WP 14979(2009-05)摘要,18% 出自其正式发表版 JOLE 2013。**应引 18% 并同时说明 Kleiner 本人 2015 年报告已退到 10–15%**——由批评方自己下调,比外部质疑更有说服力。另 10–15% 原文限定为「hourly earnings」且限「universally licensed occupation」。(6) 论断 D 一处内部矛盾值得写进文章:白宫报告正文说 NP 执照使儿童保健检查涨价「3 to 16 percent」,但其自家 Research Appendix Table 2 里 Kleiner et al. (2014) 的两行是 6.0(medium regulation)与 16.0(high regulation),并无 3。引用时用正文原话没错,但别把「3」当作独立数据点。(7) 论断 D 的推论「损害的是 NP 自己」不是这句话说的——well-child exam 涨价讲的是**消费者付更多钱**。该推论另有出处支持(Nunn, Brookings:「when especially stringent licensing rules limit the ability of nurse practitioners to work autonomously, they receive lower wages and physicians receive higher wages」),请改挂这一条。(8) 未能找到「执照对护士有正向工资溢价」的干净一手研究,故 B 不予 REFUTED。但补一条反向证据:DePasquale & Stange(NBER w22344, 2016)用 180 万护士数据发现 NLC 的采纳对护士劳动供给与流动性**没有可测效果**,即「NLC 覆盖 43 州所以护士流动无碍」这个推论本身也缺乏实证支撑,不宜写得太满。

**核验依据**:Kleiner 2015 Hamilton Project 报告 PDF(https://www.brookings.edu/wp-content/uploads/2016/06/THP_KleinerDiscPaper_final.pdf,curl 200,864KB,pdftotext -layout)第 12–13 页双栏原文逐字核:murky 段完整句、「10 to 15 percent」「about 5 to 8 percent (Gittleman, Klee, and Kleiner 2014; Gittleman and Kleiner 2014; Kleiner 2006)」、「In the early 1950s less than 5 percent… By 2008… almost 29 percent (Kleiner and Krueger 2013)」、Table 2 中 Iowa 33.3 / South Carolina 12.4(licensed 列)。白宫 2015 报告 PDF(https://obamawhitehouse.archives.gov/sites/default/files/docs/licensing_report_final_nonembargo.pdf,curl 200,1.9MB)逐字核:第 73–78 行「More than one-quarter… risen five-fold since the 1950s」「About two-thirds of this change stems from an increase in the number of professions that require a license, with the remaining growth coming from changing composition of the workforce」;第 215 行「about 25 percent… licensed at the State level」;第 535–536 行「Stricter licensing was associated with quality improvements in only 2 out of the 12 studies reviewed」;第 555–558 行「In 9 of the 11 studies we reviewed (see Research Appendix Table 2)… more restrictive State licensing of nurse practitioners raises the price of a well-child medical exam by 3 to 16 percent」;第 2542–2543 行 Research Appendix Table 2 两行 Nursing = 6.0 / 16.0。Johnson & Kleiner 工作论文全文(https://files.webservices.illinois.edu/8503/johnson.pdf,curl 200,1.3MB)Table 1「Universally licensed occupations identifiable in the ACS」:State-specific 列首行 Elementary/secondary teacher(ACS 2300–2340),Quasi-national 列首行 Nurse (RN/LPN)(3130, 3255, 3256, 3258, 3500);附录列 Nurses = NCLEX-RN / NCLEX-PN(NCSBN);摘要「7 percent less likely to move between states」,正文「This difference is much closer to zero than that using all individuals regardless of migration status: -58 percent」。AEA 发表版页面(https://www.aeaweb.org/articles?id=10.1257%2Fpol.20170704)摘要全文核对,无 36%。NBER w24107(https://www.nber.org/papers/w24107,2017-12)摘要含「36 percent lower relative to members of other occupations」。NBER w14979(https://www.nber.org/papers/w14979,2009-05)摘要「licensing is associated with about 14 percent higher wages」。NLC 计数:NCSBN 官方站 https://www.nursecompact.com/ 页面写「43 jurisdictions are currently part of the NLC」,但页面未标注日期,只指向另一份 implementation status PDF。DePasquale & Stange:https://www.nber.org/papers/w22344(2016-06)。


#### [G38] CORRECTED · confidence=high

**修正**:数字全部逐格无误,但标题级推论过头,且有两处口径需收紧:(1) 「BLS 数字不支持『医疗是最高增长赛道』」→ 同一份新闻稿明确写 healthcare and social assistance「is projected to have the largest job growth and be the fastest growing industry sector (+8.4 percent)」,且计算机与数学类被 BLS 自己称为「the **second** fastest」——第一快的正是医疗支持类 +12.4%。所以 BLS 数字**恰恰支持**「医疗是最高增长赛道」(在行业层面和医疗支持职业层面)。真正成立的是收窄版:「医疗**执业与技术类** +7.2% 慢于计算机与数学类 +10.1%」,且医疗支持类的高增速对应的是 $34,900 的中位年薪。标题必须改写,否则是可被一句原文推翻的表述。(2) 「教育与图书馆大类整体年均缺口高达 890,300 个」的上下文是「Despite **limited employment growth**」——该大类 2024→2034 是 9,813.2→9,875.4 千人、**+0.6% 正增长**,不是下降。只有四个教师职业在下降。别让读者以为整个大类在萎缩。(3) 「教师三个学段全部负增长」需限定为 K-12:学前教师(preschool teachers)2024–34 是 **+4%(+22,900)**,555,100 人,中位 $37,120。(4) 「低失业与负增长并存,因为供给端萎缩得同样快」——**供给端机制未经核实**。我没有取到师范生培养规模(Title II / IPEDS)的一手数据,BLS 本身也不提供该解释。这一句应降格为假设并明说未验证,或删去因果部分只保留「两者可以并存」这一事实描述。(5) 四页 Quick Facts 与逐字引语全部无误,可原样使用。

**核验依据**:BLS 2024–2034 就业预测新闻稿(bls.gov 直连 403,改走 Wayback id_ 快照 http://web.archive.org/web/20260601055334id_/https://www.bls.gov/news.release/ecopro.nr0.htm)逐字:「Computer and mathematical occupations are projected to grow the second fastest of any occupational group (+10.1 percent), which is more than three times the average rate of growth projected for the total economy (+3.1 percent)」;「healthcare support occupations and healthcare practitioners and technical occupations are projected to be among the fastest growing occupational groups, growing 12.4 percent and 7.2 percent, respectively」;「Healthcare and social assistance is projected to have the largest job growth and be the fastest growing industry sector (+8.4 percent)」。四个 OOH 教师页(Wayback 2026-06-12 快照)Quick Facts 逐格:小学 $62,310 / 1,539,800 / −2% / −29,800;初中 $62,970 / 633,700 / −2% / −12,400;高中 $64,580 / 1,094,500 / −2% / −17,800;特教 $64,270 / 559,500 / −1% / −7,700。四页均含同构逐字句,小学版为「Despite declining employment, about 103,800 openings for kindergarten and elementary school teachers are projected each year, on average, over the decade. All of those openings are expected to result from the need to replace workers who transfer to other occupations or exit the labor force, such as to retire.」(初中 40,500、高中 66,200、特教 37,800)。学前教师页(Wayback 20260612181240):$37,120 / 555,100 / 4% (As fast as average) / +22,900。890,300 见 OOH 教育大类首页(Wayback 20260612181255)逐字:「Overall employment in educational instruction and library occupations is projected to grow slower than the average… Despite limited employment growth, about 890,300 openings are projected each year, on average, in these occupations largely due to the need to replace workers who leave the occupations permanently. The median annual wage for this group was $59,220 in May 2024」。大类就业数见 EP Table 1.1(Wayback 20260502091542,https://www.bls.gov/emp/tables/emp-by-major-occupational-group.htm):25-0000 教育指导与图书馆 9,813.2 → 9,875.4(+62.2 千,+0.6%,中位 $59,220);29-0000 医疗执业与技术 10,067.5 → 10,794.4(+726.9,+7.2%);31-0000 医疗支持 7,982.8 → 8,971.1(+988.3,+12.4%)。


#### [G39] CORRECTED · confidence=high

**修正**:论断 A 逐格无误,但论断 B 用了**已被官方取代的旧版**,这正是论断 C 指控别人犯的错——且两者出现在同一条论断里,自相矛盾。(1) 「HRSA 预测 NP 2036 年供给 652,870 FTE vs 需求 340,830 FTE,充足率 192%(2026 年 132%、2031 年 164%);麻醉护士 2036 年 118%、助产士 139%」→ 这些是 **2024 年 3 月版(2021–2036)** 的数字(我已逐格核实,确实如此)。但 HRSA 现行版是 **2025 年 12 月版(2023–2038)**,其 NP 数字为:供给 766,260、需求 437,330、**充足率 175%**(2028 年 126%、2033 年 152%);麻醉护士 2038 年 **113%**、助产士 **140%**。若文章 C 部分用 2025-12 版讲 RN 下修,B 部分就必须同版讲 NP,否则读者会看到一篇同时引用两个版本的文章。建议统一改用 2025-12 版:「NP 2038 年充足率 175%(供给 766,260 vs 需求 437,330)」,并可补一句「上一版对 2036 年的估计是 192%,新版虽下调但仍是显著过剩」——这样反而更有力。(2) 「医师 2038 年缺口 141,160 名(非都会区初级保健 39%,都会区 5%)」→ 141,160 与都会区 5% 无误,但**「非都会区初级保健 39%」在医师 factsheet 中查无此数**。该文件原话是全科别合计:非都会区充足率 42%(**短缺 58%**),都会区 95%(短缺 5%)。请删除 39% 或另找出处;若想保留「地理问题」这个结论,用 58% vs 5% 反而更强。(3) 论断 C 其余全部无误:337,970(2036)→108,960(2038)、2038 年 3% 短缺、非都会区 11% vs 都会区 2%、LPN 99,070→245,950,均逐字核实。(4) 口径辨析段(BLS 测已实现就业 vs HRSA 分建供需;年均缺口 32,700 属 APRN 合并组不能挂 NP 名下)完全正确,建议保留原样。(5) 可补强的一点:NP 在 BLS Table 1.3 中排**第 3 快**(前两名为风电运维技师 +49.9%、光伏安装工 +42.1%),说「增长最快的职业之一」准确。

**核验依据**:BLS EP Table 1.3(Wayback 20260501185014,https://www.bls.gov/emp/tables/fastest-growing-occupations.htm)逐格:Total, all occupations 169,956.1→175,167.9(+5,211.8,+3.1%,$49,500);Nurse practitioners 29-1171 320.4→448.8(+128.4,+40.1%,$129,210);Software developers 15-1252 1,693.8→1,961.4(+267.7,+15.8%,$133,080);Physician assistants 29-1071 162.7→195.8(+33.2,+20.4%,$133,260);Home health and personal care aides 31-1120 4,347.7→5,087.5(+739.8,+17.0%,$34,900);表内顺序显示 NP 位列第 3。OOH:RN 页(Wayback 20260501184935)$93,600 / 3,391,000 / 5% / +166,100 /「About 189,100 openings for registered nurses are projected each year」;APRN 合并页(Wayback 20260605125432)$132,050 / 382,700 / 35% / +134,000 /「About 32,700 openings for nurse anesthetists, nurse midwives, and nurse practitioners are projected each year」。HRSA 2024-03 版《Nurse Workforce Projections, 2021-2036》(https://njccn.org/wp-content/uploads/2024/10/HRSA-nursing-projections-factsheet.pdf,curl 200)Exhibit 1c(2036):NP 供给 652,870 / 需求 340,830 / 192%;RN 91%;LPN 88%;麻醉护士 118%;助产士 139%;正文「By 2036, the shortage is 9% (a shortage of 337,970 full-time equivalent [FTE] RNs)」「shortage (99,070 LPN FTEs) in 2036」。HRSA 2025-12 版《Nurse Workforce Projections, 2023-2038》—— bhw.hrsa.gov 直连 403,经 Wayback id_ 快照取得(http://web.archive.org/web/20260617042955id_/https://bhw.hrsa.gov/sites/default/files/bureau-health-workforce/data-research/nursing-projections-factsheet.pdf,210KB)——Exhibit 1a(2028)NP 501,010/399,200/126%;Exhibit 1b(2033)638,990/420,250/152%;Exhibit 1c(2038)NP 766,260/437,330/**175%**、RN 3,509,970/3,618,930/97%、LPN 70%、麻醉护士 113%、助产士 140%;正文「By 2038, the shortage is 3% (a shortage of 108,960 full-time equivalent [FTE] RNs)」「11% vs 2% in 2038」「shortage (245,950 LPN FTEs) in 2038」。两版均含完全相同的逐字句:「At the national level, the supply of nurse practitioners (NPs) is projected to exceed demand over the projection period; however, distribution remains the most important issue.」医师版《Physician Workforce: Projections, 2023-2038》(December 2025,Wayback 20260602013657):「there is a projected shortage of 141,160 full-time equivalent (FTE) physicians in 2038」;「The percent adequacy of supply across all physician specialties is projected to be 42% in nonmetro areas (a shortage of 58%), compared to 95% in metro areas (a shortage of 5%) in 2038」;全文 grep「primary care」无匹配。


#### [G40] CORRECTED · confidence=high

**修正**:NCSBN 一侧逐字全对(含工具效应与 11.2 百分点的措辞批评,都成立);NSI 一侧有两处会直接推翻本条核心论断的错误:(1) 「CY2022 峰值 27.1%」→ **27.1% 是 CY2021**。NSI 图表横轴为 CY21–CY25,All Staff RN 序列依次是 27.1% / 22.5% / 18.2% / 16.4% / 17.6%,CY2022 是 22.5%。(2) **方向错了**:CY2025 的 17.6% 不是继续下降,而是**回升**。报告逐字:「RN turnover is recorded at 17.6%, **a 1.2% increase**」,即由 CY2024 的 16.4% 上升 1.2 个百分点;医院全员 18.5% 亦为「a nominal increase from CY24」。所以「行为指标方向相反(意向恶化、行为改善)」只在「距 2021 年峰值」这个比较上成立,最新一年的行为指标已经掉头向上。论断 B 应改为:「医院 RN 实际离职率从 CY2021 峰值 27.1% 降至 CY2024 的 16.4%,但 CY2025 回升 1.2 个百分点至 17.6%」——否则文章会在最关键的一处把趋势讲反。(3) 「各州回收率仅约 9–22%(加州 RN 14.0%、LPN/LVN 最低 9.1%)」→ 两处错。NCSBN 用了**邮寄与电邮两种问卷**:邮寄卷各辖区回收率 8.2%–22.3%(合计 RN 16.9%、LPN/LVN 13.7%);电邮卷 **2.2%–49.0%**,远低于 9%。且 9.1% 是**加州的** LPN/LVN 回收率,不是全表最低(邮寄卷最低 8.2% 为北马里亚纳群岛 RN;电邮卷有低至 2.9%、4.0%、2.2% 者)。应改为:「邮寄卷各辖区 8.2%–22.3%(合计 RN 16.9%、LPN/LVN 13.7%),电邮卷低至 2.2%;加州 RN 14.0%、LPN/LVN 9.1%」——回收率比原稿说的还要差,「39.9% 应视为上界」这个结论因此更站得住。(4) 利益相关段全部属实且可加强:527 家医院是「invited to participate」的自愿样本、覆盖 40 州;「Every RN hired saves $66,081」与「Contact Michael Colosi at (717) 575-7817 to learn how NSI can improve your bottom line」确实印在执行摘要正文里;$60,090 与 158,600 均为 NSI 基于自家问卷的自估。(5) 空缺率口径无误:8.6%(2026 报告)带星号,脚注逐字说明改了公式,与上一年 9.6% 不可比。

**核验依据**:NCSBN 论文全文(journalofnursingregulation.com 直连 403,经 Wayback id_ 快照并 gzip 解压取得 http://web.archive.org/web/20251008232225id_/https://www.journalofnursingregulation.com/article/S2155-8256%2825%2900047-X/fulltext,20 万字符)。Table 27「Plans of RNs for the Next 5 Years, 2020–2024」:Yes 2020=22.1%、2022=28.7%、2024=39.9%;2024 细分 I plan to retire 21.9%、I plan to leave nursing 18.0%;表注逐字「This question was introduced in the 2020 survey and modified in 2024 to offer separate options for those who plan to retire, and those who plan to leave nursing.」正文逐字「a 11.2% increase over the proportion who reported similar intentions on the 2022 survey (28.7%)」(39.9−28.7=11.2,确为百分点差被写成百分比增幅)。摘要逐字「The median age of both RNs and LPNs/LVNs was 50 years」与「While reported levels of emotional exhaustion, including burnout, and workloads have moderated over the past 2 years, about 40% of nurses report they plan to leave nursing or retire over the next 5 years.」倦怠逐字「The proportion of RNs reporting they feel burned out from work either every day or a few times per week decreased from 45.2% in 2022 to 35.4% in 2024」;情绪耗竭逐字「Nearly one-fifth of RNs (18.9%) reported that they felt emotionally drained from work every day in 2024, representing a decrease from 23.9% in 2022」。回收率:邮寄卷表(TABLE 1 Mail Survey Responses)程序化提取 50 个比率,min 8.2%(Northern Mariana Islands RN)max 22.3%,Total 行 RN 16,146/95,567=16.9%、LPN/LVN 13,174/96,354=13.7%,CA 行「523,864 4,870 682 14.0% / 110,453 7,932 721 9.1%」;电邮卷表 40 个比率 min 2.2% max 49.0%(如 DC LPN 2.9%、AL LPN 4.0%、FL RN 5.8%)。NSI 报告 PDF(https://www.nsinursingsolutions.com/documents/library/nsi_national_health_care_retention_report.pdf,curl 200,1.48MB,pdftotext -layout)执行摘要逐字「Nationally, the hospital turnover rate is 18.5%, a nominal increase from CY24, and RN turnover is recorded at 17.6%, a 1.2% increase」;正文「Turnover continues to be elevated for hospital RNs with a national average of 17.6%. This is a 1.2% annual increase」;区域表「NATIONAL AVERAGE 17.6% (+1.2%) 14.6% (+1.1%)」;图表数据行 27.1% / 22.5% / 22.5% / 18.2% / 18.4% / 15.0% / 16.4% / 13.5% / 17.6% / 14.6%,横轴标签行「CY21 CY22 CY23 CY24 CY25」。方法学「In January, acute care hospitals were invited to participate… 527 hospitals from forty states responded. In total, this survey covers 965,886 healthcare workers, and 262,405 registered nurses.」销售话术「Every RN hired saves $66,081… Contact Michael Colosi at (717) 575-7817 to learn how NSI can improve your bottom line.」空缺率表 AVERAGE 行 2022=17.0% 2023=15.7% 2024=9.9% 2025=9.6% 2026=*8.6%,脚注逐字「*The RN Vacancy Rate in previous reports were based on the average of the range selected. Beginning 2026, NSI collected data on RN FTEs filled & vacant, and modified the formula to where RN Vacancy Rate = (Unfilled RN FTEs/Budgeted FTEs)*100.」


#### [G41] CORRECTED · confidence=high

**修正**:十个评分逐格无误(我对照 Table 1 全部核过),评分构造的描述也对,但有三处必须收紧,否则最关键的两个比较承不住重:(1) **两处核心对比落在小数点后两位,论文自己说不能这么用**。作者逐字警告:「The use of a frequency threshold means relative comparisons are more meaningful than absolute score values」,且全文未给任何置信区间。「中小学教师 0.18 高于律师 0.17」相差 0.01、「大学教师 0.31 高于计算机职业 0.29」相差 0.02——这两条不能写成事实性排序。真正扛得住的只有 0.18 vs 0.13(中小学教师 vs 医疗诊疗执业者)这个量级差。建议把结论重写为:「教育类的 AI 适用度落在知识工作区间(中小学 0.18、大学 0.31),与计算机(0.29)、数学(0.32)、律师(0.17)同档;而医疗诊疗(0.13)与医疗照护类(0.04–0.06)明显更低。护理与教育不属于同一阵营。」——放弃「高于律师」「高于计算机」这两个精确排序,论点丝毫不减。(2) 数据窗口与样本口径:不是「2024 年 Copilot 对话」,而是 **2024-01-01 至 2024-09-30 的九个月**,且仅限美国境内对话。「20 万条」与摘要一致,但构成需说明:主分析集是约 **10 万条均匀抽样**,另 10 万条是**从获得点赞/点踩反馈的对话中抽样**的辅助集(用于估计 completion rate),后者不是代表性样本。就业加权用的是 **OEWS 2023**,不是 2024。(3) 「中小学与特教教师」对应的 SOC 次要组是 25-2000,其完整名称含**学前与幼儿园**教师,不止中小学。(4) 评分构造确认:a_i = (a_user + a_AI)/2,确为「用户目标适用度」与「AI 行为适用度」两者的**算术平均**;但每一侧本身 = Σ_j 1[频率≥0.05%]·完成率·范围占比·O*NET 任务权重,并非原始使用份额,描述时不要简化成「使用占比」。(5) **未过审**:截至 2026-07-24 仍是 arXiv 未评审预印本(v1 2025-07-10,v6 2025-12-22,comments 栏仅「40 pages」,无期刊信息)。注意别把 Nature Computational Science 上的《AI and the democratization of knowledge work》(Daepp, Tomlinson, Counts 等,2026-05)当成它的发表版——那是另一篇 Perspective。(6) 微软利益相关标注必要,且有现实理据:该论文发布后被大量媒体改写为「微软列出 AI 将消灭的 40 种职业」,作者被迫另发博文澄清——这本身就是文章可用的素材。

**核验依据**:arXiv:2507.07935 v6 PDF 全文(https://arxiv.org/pdf/2507.07935v6,3.3MB,pdftotext -layout,2174 行)。Table 1「SOC minor groups by AI applicability score」逐格核对,全部命中:Mathematical Science Occupations 0.32、Postsecondary Teachers 0.31、Computer Occupations 0.29、Prim., Second., and Special Ed. Teachers 0.18、Lawyers, Judges, and Related Workers 0.17、Healthcare Diagnosing or Treating Pracs. 0.13、Other Healthcare Support Occupations 0.06、Occupational and Physical Therapy Assts. 0.05、Home Health Aides and Nursing Assts. 0.04。表注逐字「Score is the employment-weighted average AI applicability score for each specific occupation in the SOC minor group, averaging the mean of the user goal and AI action scores.」§4.4.2 公式 (1) 与「We report a_i = (a_user_i + a_AI_i)/2 unless otherwise specified.」§2.2 逐字「The use of a frequency threshold means relative comparisons are more meaningful than absolute score values (see Section 4 and Figures S19 and S20).」§4.1 逐字「anonymized and privacy-scrubbed U.S. conversation data from Microsoft Bing Copilot… gathered from January 1, 2024 to September 30, 2024… Our main dataset is a uniform sample of approximately 100k conversations… We use a supporting dataset of 100k conversations uniformly sampled from those that received at least one thumbs up or thumbs down reaction from the user.」§4.2 逐字「We combine O*NET with data on wages and employment from the 2023 Occupational Employment and Wage Statistics data」。限定语逐字(第 433–440 行)「It is tempting to conclude that occupations that have high AI action applicability score will be automated and thus experience job or wage loss, and that occupations with high user goal applicability score will be augmented and raise wages. This would be a mistake, as downstream consequences of new technologies are very hard to predict and often counterintuitive (33).」——与论断所引完全一致。arXiv 摘要页(https://arxiv.org/abs/2507.07935)确认作者 Kiran Tomlinson, Sonia Jaffe, Will Wang, Scott Counts, Siddharth Suri(均微软研究院),v1 2025-07-10、v6 2025-12-22,comments 仅「40 pages」,无期刊/会议标注。配套博文为 Microsoft Research《Applicability vs. job displacement: further notes on our recent research on AI and occupations》(2025-08-21),该文即论断所引「does not draw any conclusions about jobs being eliminated… we explicitly cautioned against using our findings to make that conclusion」的出处。Nature Comput. Sci. 文章 s43588-026-00985-z 经检索确认为 Daepp, M.I.G., Tomlinson, K., Counts, S. et al.《AI and the democratization of knowledge work》(2026-05,Perspective),标题与作者列均不同,非本文发表版。


### 第 3 席


#### [G36] CORRECTED · confidence=high

**修正**:(1)【核心巧合口径错】原表述「护理的 35–45 岁中位工资($87,000)恰好等于全体专业的中位数」→ 正确表述「恰好等于全体大学毕业生(35–45 岁)的合并中位数($87,000)」。CSV 中 Overall 行是所有学士及以上毕业生的**合并中位数**,不是 73 个专业中位数的中位数——后者我实算为 **$82,000**。「全体专业的中位数」这一措辞会被读成后者,必须改。另:Journalism 中期中位工资也是 $87,000,并非护理独有。
(2)原表述「Elementary Education 失业率 1.180%(全表最低之一)」→ 正确表述「1.180%,全表第 3 低」。更低的是 Special Education 0.739%、Miscellaneous Education 1.089%(两者同为教育类,反而强化文章论点,建议直接用)。
(3)原表述「低就业率(underemployment)…仅学士」→ 正确表述:NY Fed FAQ 明确「The underemployment figures are calculated as a percentage holding a bachelor's degree or higher, so they do include those with graduate and professional degrees」。「仅学士」这一限定只适用于工资列,不适用于失业/低就业率列。护理 30.3% 持研究生学位、小学教育 50.6%,分母差异不可忽略。
(4)数据时效必须标注:该 CSV 在 2026-03-03 前后被替换过一次(Wayback digest 由 FFCVTS… 变为 BYPYCX…),现行版本 bundle.js 中标题为「Labor Market Outcomes of College Graduates by Major in 2024」,即 2024 ACS;2026-01 之前抓取到的是上一版(如 Agriculture 早期薪 $50,000 而非 $56,000)。同时 NY Fed 页面挂有告示:「Due to the suspension of necessary data, The Labor Market for Recent College Graduates has not been updated as scheduled.(October 31, 2025)」——引用时应写明「2024 年数据,更新已暂停」。
方向与全部数字均无误:Nursing 2.147 / 12.781(73 个专业中最低,实算确认)/ 70,000→87,000(+24.29%);Overall 4.211 / 39.350 / 58,000→87,000(+50.0%);CS 87,000→120,000(+37.93%);Elementary Education 45,000→55,000(+22.22%)。

**核验依据**:直接下载并逐格核对一手 CSV:https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-outcomes-by-major-data.csv(74 行 = 73 专业 + Overall)。用 Python 排序确认 underemployment 最低 5 名为 Nursing 12.781、Aerospace Eng 14.709、Civil Eng 15.567、Computer Eng 15.835、Special Ed 16.042;unemployment 最低 6 名为 Special Ed 0.739、Misc. Education 1.089、Elementary Ed 1.18、Agriculture 1.395、Foreign Language 1.579、Geography 1.6;statistics.median(73 个专业 mid-career)=82,000。年龄口径与低就业定义取自 https://www.newyorkfed.org/research/college-labor-market 页面 FAQ 原文(「Early career graduates are those aged 22 to 27, and mid-career graduates are those aged 35 to 45」)。数据年份取自页面 JS 包 https://www.newyorkfed.org/medialibrary/Research/Interactives/college-labor-market/college-labor-chart.bundle.js 中的 title 字段。版本变更经 Wayback CDX 比对确认。


#### [G37] CORRECTED · confidence=high

**修正**:B 段引文逐字无误,C 的 10–15%/5–8%、D 的 12/2、覆盖率的「超过四分之一」「五倍」「约三分之二」、南卡 12.4%/爱荷华 33.3%、NLC 43 均核实。但有 7 处必须改:
(1)【最重要】原表述「需持**州**执照才能合法从业的劳动力占比…升至 2008 年的约 29%」→ 正确表述「**州级**持照占比由 1950 年代初不足 5% 升至 2008 年的 **25%**(约五倍);再加上地方与联邦执照后总计 **29%**」。白宫报告原文:「the percentage of the workforce covered by State licensing laws grew from less than 5 percent in the early 1950s to 25 percent by 2008, meaning that the State licensing rate grew roughly five-fold」「the addition of local and Federal licensed occupations further raises the share of the workforce that is licensed to 29 percent」。把 29% 挂在「州执照」名下是错的。
(2)【E 段实质错误】原表述「Johnson & Kleiner(2020)——采用州专属执照考试的职业跨州迁移率比其他职业低 **36%**」→ 正确表述「其**首选识别策略**(限定长距离迁移者以剔除自选择)得到的是 **低 7%**」。论文摘要逐字:「We find individuals in state-specific licensed occupations who move a long distance are **7 percent less likely** to move between states than those in occupations with a national licensing exam」;AEJ:EP 已发表版摘要根本没有 36%,只说「the magnitude of the effect can only account for a small part of the overall decline」。−36.00 只是表中一个未做长距离限定的「percentage effect」,正是作者认为被自选择污染的那一列。引用 36% 而不说这是最粗的估计,等同于 C 段批评的「引用 18% 而不给识别问题」。
(2b)但 E 的实质结论成立且可加强:论文 Table 1 亲自把 **Nurse (RN/LPN) 归入 quasi-national(全国统考)组**,把 **Elementary/secondary teacher 归入 state-specific 组**——即迁移惩罚恰好落在教师身上、不落在护士身上。这比原稿的说法更有力。
(3)原表述「**11 项价格研究**中 9 项」→ 正确表述「白宫报告正文称 9/11,但 Research Appendix Table 2 实际只列 **6 篇论文、13 行估计**;剔除正文另行讨论的 Kleiner & Todd(2009)两行后恰为 11 行、其中 9 行显著为正,且这 11 行只来自 **5 篇**论文(Kleiner et al. 2014、Kleiner & Kudrle 2000、Liang & Ogur 1987、Conrad & Sheldon 1982、Shepard 1978)」。说成「11 项研究」高估了证据独立性。相比之下 12/2 的质量计票**完全对得上**(13 行,Larsen 2015 占两行按一篇计 = 12 篇;判为 increase in quality 的正是 Larsen 高收入学区 + Holen 1978)。
(4)原表述「幅度 3–16%」→ 正确表述「3–16% 是 NP 的儿童保健检查这一项的幅度,不是 9 项的区间;Appendix Table 2 各项估计从 −1.0% 到 +17.9%(Shepard 平均 6.5%)」。另注:Kleiner 本人 2015 报告对同一结果给的是 **10%**(「raises prices of well-child exams by 10 percent」),与白宫的 3–16% 并存,应择一并说明来源。
(5)【14% vs 18% 定论】用 **18%**,并注明这是 **JOLE 2013 已发表版**(版本记录)的口径:「We find that licensing is associated with about 18% higher wages but that the effect of governmental certification on pay is much smaller」;NBER WP 14979(2009-05)工作论文版为 **14%**,是同一研究的早期版本,不是两个独立结果。同时必须写明 18% 是**未做教育/培训控制的横截面相关**;白宫报告读同一份 Westat 数据得州级 **17%**、州+联邦/地方 **25%**;控制教育培训后 10–15%;最干净识别 5–8%(Kleiner 2015)/ 8.4%(Gittleman, Klee & Kleiner 2015)/ 常为零。
(6)原表述「执照工资溢价对护士和教师恰恰**不成立**」→ 正确表述「**证据不明确(murky)**」。原文是「murky, with some studies finding small effects and others finding none」,是「未定」不是「为零」。另,B 的省略号掩盖了关键限定:被省掉的是「by limiting entry or making it more difficult for an individual to be hired for a job in another state」——即医生/牙医/律师那句的「large effects」指的是**限制进入与跨州受雇**,并非直接的工资溢价。放在「工资溢价」标题下会误导。
(7)NLC:NCSBN 官方地图 PDF 逐字为「43 jurisdictions have enacted the NLC」,但关岛、马萨诸塞、美属维尔京群岛为「NLC Enacted, Awaiting Implementation」,实际可用的约 40 个。写成「43 个辖区已立法、约 40 个已实施」。
(8)反证搜寻结果:未找到「执照对 RN 有正向工资溢价」的一手研究,故 B 不被推翻。最接近的反向证据反而支持 D——Kleiner, Marier, Park & Wing(NBER WP 19906)摘要逐字:「when only physicians are allowed to prescribe controlled substances that this is associated with a **reduction in nurse practitioner wages**, and increases in physician wages」,并「increase the price of a well-child medical exam by 3 to 16 %」。即执照规则确实会动护士的收入,只是方向对 NP 为负。D 的推论「损害的是 NP 自己」成立,但支撑它的应是这句工资结论,而不是消费者价格结论。
(9)立场折扣:Kleiner 是白宫 2015 报告的主要引用来源、也是 Hamilton Project(Brookings)报告作者,D 段「12 项中仅 2 项」「9/11」两组计票均出自其学术圈自选的文献集,需在文中标注。

**核验依据**:一手 PDF 全文下载并 pdftotext 逐段核对:Kleiner 2015 Hamilton Project(https://www.brookings.edu/wp-content/uploads/2016/06/THP_KleinerDiscPaper_final.pdf,murky 段在第 12–13 页两栏排版中,10–15% 与 5–8% 段同页;「5 to 33 percent」与 NP「10 percent」在价格一节;Table 2 州分布 Iowa 33.3 / South Carolina 12.4);白宫 2015(https://obamawhitehouse.archives.gov/sites/default/files/docs/licensing_report_final_nonembargo.pdf,p.1 摘要三条、p.13 价格段、p.19 五倍段、Research Appendix Table 1 与 Table 2 全表);Johnson & Kleiner 工作论文全文(https://files.webservices.illinois.edu/8503/johnson.pdf,摘要 7% 在第 1 页,Table 1 职业分类在 p.36,−36.00 出现在一张未限定长距离的表中),已发表版摘要经 https://ideas.repec.org/a/aea/aejpol/v12y2020i3p347-73.html 与 https://www.aeaweb.org/articles?id=10.1257%2Fpol.20170704 核对(AEJ:EP 12(3):347-73);NBER w14979 摘要原文「licensing is associated with about 14 percent higher wages」(https://www.nber.org/papers/w14979);JOLE 2013 已发表摘要「about 18% higher wages」经 https://experts.umn.edu/en/publications/analyzing-the-extent-and-influence-of-occupational-licensing-on-t/ 取得(J. Labor Econ. 31(2 PART2), S173-S202);NBER w19906 摘要(https://www.nber.org/papers/w19906);NLC 计数取自 NCSBN 官方地图 PDF https://www.ncsbn.org/public-files/NLC_Map.pdf 与 https://www.nursecompact.com/。


#### [G38] CORRECTED · confidence=high

**修正**:数字全部核实无误(+10.1% / +7.2% / +12.4% / +3.1%;小学 1,539,800 / −2% / −29,800 / $62,310;初中 633,700 / −2% / −12,400 / $62,970;高中 1,094,500 / −2% / −17,800 / $64,580;特教 559,500 / −1% / −7,700 / $64,270;学前 $37,120;103,800 与 890,300 两个缺口数;两段逐字引文亦准确)。但标题与三处口径要改:
(1)【标题过头】原表述「BLS 数字不支持『医疗是最高增长赛道』」→ 正确表述「BLS 数字不支持『医疗**执业**类是增长最快的职业大类』」。同一份新闻稿逐字写着:「Healthcare and social assistance is projected to have the **largest job growth** and be the **fastest growing industry sector** (+8.4 percent)」;而在职业大类层面,最快的是医疗**支持**类 +12.4%,计算机与数学类被明确称为「the **second** fastest」(+10.1%)。所以行业口径下医疗确实既最大又最快,只有「医疗执业与技术类 +7.2%」这一支慢于计算机。原标题在行业口径上是错的。
(2)原表述「教师三个学段全部负增长」→ 需补「但学前教师 +4%(+22,900,共 555,100 人)」。文章只引了学前 $37,120 的低薪却没说它是唯一正增长的学段,对准大学生是有方向性影响的遗漏。
(3)890,300 属于 OOH 的「**Educational Instruction and Library Occupations**」大类,该大类 OOH 原文是「projected to **grow slower than the average**」——是慢增长,不是负增长;且原文为「**largely** due to the need to replace workers who leave the occupations permanently」,不是「全部来自替补」。「全部来自替补」只对 kindergarten and elementary school teachers 那一句成立(「All of those openings…」)。
(4)$62,310 是 OOH 合并职业「Kindergarten and Elementary School Teachers」的 2024 中位薪;同页另分列 elementary $62,340、kindergarten $61,430。
(5)【未证实】「低失业与负增长并存,因为**供给端萎缩得同样快**」这个因果解释我未能取得一手支撑(Title II 师范培养完成人数官网 https://title2.ed.gov 陷入重定向循环,取不到)。且两个数字口径不同:1.18% 是 ACS 中 22–27 岁「小学教育**专业**」毕业生的失业率,−2% 是 BLS 对该**职业** 2024–34 的就业变动预测。另一同样合理的解释是:教师执照把进入端拦住、拿了教育学位却没进课堂的人转入其他工作 → 被记为 underemployed(小学教育 16.2%)而非 unemployed。文章应把「供给端萎缩」写成待证假设,不能写成解释。

**核验依据**:BLS 2024–2034 就业预测新闻稿全文(bls.gov 直连 403,改用 Wayback id_ 快照 https://web.archive.org/web/20260716215413if_/https://www.bls.gov/news.release/ecopro.nr0.htm,USDL-25-1324,2025-08-28 发布),逐字核对「second fastest…(+10.1 percent)」「growing 12.4 percent and 7.2 percent, respectively」「largest job growth and be the fastest growing industry sector (+8.4 percent)」。四个教师 OOH 页 + 学前教师页 + 大类首页均取自 Wayback 2026-06-13 快照(https://web.archive.org/web/20260613if_/https://www.bls.gov/ooh/education-training-and-library/…),逐格读取 Quick Facts 与 Job Outlook 段。890,300 出现在大类页原句「Despite limited employment growth, about 890,300 openings are projected each year, on average, in these occupations largely due to the need to replace workers who leave the occupations permanently.」


#### [G39] CORRECTED · confidence=high

**修正**:A 段整张表逐格核对**完全正确**(EP 表:NP 29-1171 320.4→448.8/+128.4/+40.1%/$129,210;Software developers 15-1252 1,693.8→1,961.4/+267.7/+15.8%/$133,080;PA 29-1071 162.7→195.8/+33.2/+20.4%/$133,260;HHA/PCA 31-1120 4,347.7→5,087.5/+739.8/+17.0%/$34,900;OOH:RN 3,391,000/+5%(表内 4.9%)/+166,100/189,100/$93,600;APRN 合并组 382,700/35%/32,700/$132,050),口径辨析也对。但 B、C 有三处必须改:
(1)【最严重:B 段用了已被官方取代的旧版】原表述「HRSA 预测 NP 2036 年供给 652,870 FTE vs 需求 340,830 FTE,充足率 192%(2026 年 132%、2031 年 164%);麻醉护士 2036 年 118%、助产士 139%」→ 这些数字属于 2024 年 3 月版《Nurse Workforce Projections, 2021-2036》,已被 **2025 年 12 月版《Nurse Workforce Projections, 2023-2038》**取代。现行数字为:**NP 充足率 2028 年 126%、2033 年 152%、2038 年 175%(供给 766,260 FTE vs 需求 437,330 FTE);麻醉护士 2038 年 113%;助产士 2038 年 140%**。更要命的是内部不一致:C 段用的 108,960(2038,2025-12 版),B 段用的 192%(2036,2024-03 版)——同一篇文章一边说旧版已被下修不可用,一边继续引旧版的 NP 数字。必须统一到 2025-12 版:NP 过剩结论仍成立,但幅度是 175% 不是 192%。
(2)C 段 RN 与 LPN 数字**全部正确**并已取得一手 PDF:2038 年 RN 短缺 108,960 FTE(3%),2028 年 8%;「Nonmetro areas are projected to have a higher shortage of RNs than metro areas in each of the three interval years: 11% vs 2% in 2038, 18% vs 4% in 2033, and 24% vs 5% in 2028」;LPN 2038 短缺 245,950 FTE(充足率 70%,2028 年 83%)。旧版对应值 337,970 FTE(2036,9% 短缺)、LPN 99,070 FTE 亦确认。「美国将缺 30 万护士」确系源自已被取代的旧版,该判断成立。
(3)【医师那组是苹果比橘子】原表述「医师 2038 年缺口 141,160 名(非都会区初级保健 39%,都会区 5%)」→ 141,160 FTE 正确;但同一份《Physician Workforce: Projections, 2023-2038》给的配对是**全部专科**口径:「The percent adequacy of supply across all physician specialties is projected to be 42% in nonmetro areas (a **shortage of 58%**), compared to 95% in metro areas (a **shortage of 5%**) in 2038」。39% 是**非都会区初级保健**的另一口径数字,与 5%(全专科都会区)不同源,不能并列。要么写「非都会区 58% / 都会区 5%(全专科)」,要么把初级保健的都会区对应值一起给出(我未能取得初级保健 factsheet 的一手 PDF,bhw.hrsa.gov 全站对 curl/WebFetch 403,该配对值判为待补)。
(4)可加强 A 段:EP 表中 **NP 单职业的年均缺口是 29,500**,与 APRN 合并组的 32,700 并列给出,能把「不能挂在 NP 名下」这句从提醒变成实证。
(5)口径辨析建议再加一句:HRSA 两版的基年不同(2021 含疫情 vs 2023),需求侧模型也做过修订,所以 192%→175% 既有数据更新也有模型更新,不能单纯读成「NP 过剩变轻了」。

**核验依据**:BLS 数据取自 Occupational Projections and Worker Characteristics 表(bls.gov 403,改用 Wayback https://web.archive.org/web/2026if_/https://www.bls.gov/emp/tables/occupational-projections-and-characteristics.htm),逐行提取 SOC 29-1171 / 15-1252 / 29-1071 / 31-1120 / 29-1141 / 29-1151 / 29-1161 的全部列;OOH 五个职业页取自 Wayback 2026-06-13 快照。HRSA 旧版 PDF 经镜像取得(https://njccn.org/wp-content/uploads/2024/10/HRSA-nursing-projections-factsheet.pdf,《Nurse Workforce Projections, 2021-2036》March 2024,Exhibit 1a/1b/1c 全表);**新版 PDF 经 Wayback id_ 快照绕过 403 取得**:https://web.archive.org/web/2026id_/https://bhw.hrsa.gov/sites/default/files/bureau-health-workforce/data-research/nursing-projections-factsheet.pdf(《Nurse Workforce Projections, 2023-2038》December 2025,Exhibit 1a/1b/1c 全表 + 都会区/非都会区段 + LPN 段);医师版同法取得 https://web.archive.org/web/2026id_/https://bhw.hrsa.gov/sites/default/files/bureau-health-workforce/data-research/physicians-projections-factsheet.pdf(December 2025,141,160 FTE 与 42%/95% 段)。NP 逐字引文「At the national level, the supply of nurse practitioners (NPs) is projected to exceed demand over the projection period; however, distribution remains the most important issue.」在**两版中均原样出现**。


#### [G40] CORRECTED · confidence=high

**修正**:A、C 两段与利益相关披露**逐字核实全部无误**(Table 27:2020 年 22.1%、2022 年 28.7%、2024 年 39.9%,其中 I plan to retire 21.9%、I plan to leave nursing 18.0%;表注「This question was introduced in the 2020 survey and modified in 2024 to offer separate options for those who plan to retire, and those who plan to leave nursing.」;正文「a 11.2% increase over the proportion who reported similar intentions on the 2022 survey (28.7%)」——「11.2 是百分点差」的批评成立;burnout「decreased from 45.2% in 2022 to 35.4% in 2024」;emotionally drained every day 23.9%→18.9%;RN 与 LPN/LVN 中位年龄均 50 岁;摘要 moderated 一句;NSI 527 家医院、$60,090、「Every RN hired saves $66,081」「Contact Michael Colosi at (717) 575-7817」、158,600、自述为「a national high-volume nurse recruitment and retention firm」)。但 B 段的离职率序列有两处硬伤:
(1)【年份错】原表述「NSI 报告的医院 RN 实际离职率从 **CY2022 峰值 27.1%** 降至 CY2025 17.6%」→ 正确表述「**CY2021 峰值 27.1%**」。NSI 2026 报告图表 x 轴为 CY21–CY25,RN 序列为 27.1%(CY21)、22.5%(CY22)、18.4%(CY23)、16.4%(CY24)、17.6%(CY25)。CY2022 是 22.5%。
(2)【方向错】原表述「降至 CY2025 17.6%」→ 正确表述「降至 CY2024 的 16.4% 后,**CY2025 回升 1.2 个百分点至 17.6%**」。NSI 正文逐字:「RN turnover is recorded at 17.6%, **a 1.2% increase**」「Turnover continues to be elevated for hospital RNs with a national average of 17.6%. This is a 1.2% annual increase and directly responsible for the bump in hospital turnover.」全员离职率 18.5% 也是「a nominal **increase** from CY24」。「行为指标方向相反」这个论断仍大致成立(17.6% 远低于 27.1%),但必须加上「2025 年已掉头回升」,否则是选择性叙述。
(3)补:NSI 同时公布第二套口径——只统计全职/兼职离职的医院,RN 离职率为 **14.6%**(中位 14.1%);17.6% 是含 per-diem/prn/casual 的口径。引哪个是方法学选择,应说明。
(4)【回收率区间要改】原表述「各州回收率仅约 9–22%(加州 RN 14.0%、LPN/LVN 最低 9.1%)」→ 加州 14.0%/9.1% 正确,但那只是**邮寄问卷臂**(24 个辖区;RN 合计 16.9%、LPN 合计 13.7%;区间 8.2%–22.3%)。另有**电邮问卷臂**(18 个辖区)合计 **RN 9.7%、LPN 7.4%**,各州低至 FL RN 5.8%、**NH LPN 2.2%**、DC LPN 2.9%;还有 **10 个辖区的数据来自 Nursys e-Notify 自注册记录,根本没有概率抽样**。所以正确表述是「三种模式混合抽样,邮寄臂 RN 合计 16.9%、电邮臂 RN 合计 9.7%(个别州低至 2.2%),另有 10 个辖区为自注册数据」。原区间明显低估了无回应偏误的严重程度,「39.9% 应视为上界」的判断因此更站得住。
(5)【分母限定要补】Table 27 表注还写着:「Survey participants were asked to answer this question only if they were **actively employed in nursing**. This question was **not administered in Hawaii**.」——39.9% 的分母是「在职护士」,且不含夏威夷。
(6)两个指标不同宇宙:NCSBN 是全美执照持有者抽样调查(意向),NSI 是急症医院雇主自愿报名的基准调查(行为),前者含非医院、非在职渠道,后者只覆盖 527 家自选医院。做「意向 vs 行为方向相反」的对比时要写明这不是同一群人。

**核验依据**:NCSBN/JNR 全文经浏览器渲染取得(Cloudflare 挡 curl 与 WebFetch,改用 Browser 面板 + JS 提取 innerText):https://www.journalofnursingregulation.com/article/S2155-8256(25)00047-X/fulltext(Smiley et al., J Nurs Regul 16(1) Suppl S1-S88, April 2025)。逐字读取 Table 27 全表与表注、Table 52(burnout 45.2→35.4)、Table 49(emotionally drained 23.9→18.9)、摘要、Table 1(邮寄臂:CA RN 523,864 licenses / 4,870 mailed / 682 responses / **14.0%**;CA LPN 110,453 / 7,932 / 721 / **9.1%**;Total 16.9% / 13.7%;MT 22.3% 最高,Northern Mariana 8.2% 最低)、Table 2(电邮臂 Total RN **9.7%** / LPN **7.4%**;NH LPN 2.2%;FL RN 5.8%)、Table 3(10 个辖区 e-Notify)。NSI 一手 PDF 直接下载:https://www.nsinursingsolutions.com/Documents/Library/NSI_National_Health_Care_Retention_Report.pdf(《2026 NSI National Health Care Retention & RN Staffing Report》,Brian Colosi 署名 March 2026),逐段读取 Preface(527 家医院、40 个州、965,886 名医护、262,405 名 RN;Michael Colosi 电话)、Executive Summary(18.5% / 17.6% / 「a 1.2% increase」/ $60,090 / 8.6% / 158,600 / 「Every RN hired saves $66,081」)、两张 CY21–CY25 离职率图、空缺率表(2022 17.0%→2023 15.7%→2024 9.9%→2025 9.6%→2026 *8.6%)及其脚注「The RN Vacancy Rate in previous reports were based on the average of the range selected. Beginning 2026, NSI collected data on RN FTEs filled & vacant, and modified the formula…」。


#### [G41] CORRECTED · confidence=high

**修正**:全部评分与限定语在 v6 中**逐字核实无误**(Table 1:Mathematical Science Occupations 0.32、Postsecondary Teachers 0.31、Computer Occupations 0.29、Prim., Second., and Special Ed. Teachers 0.18、Lawyers, Judges, and Related Workers 0.17、Healthcare Diagnosing or Treating Pracs. 0.13、Other Healthcare Support Occupations 0.06、Occupational and Physical Therapy Assts. 0.05、Home Health Aides and Nursing Assts. 0.04;限定语原文「It is tempting to conclude that occupations that have high AI action applicability score will be automated and thus experience job or wage loss… This would be a mistake, as downstream consequences of new technologies are very hard to predict and often counterintuitive.」;v1 2025-07-10、v6 2025-12-22)。评分构造问题的答案是**是**:「We compute AI applicability score separately for user goals and AI actions, **averaging the two**」,表注「Score is the **employment-weighted average** AI applicability score for each specific occupation in the SOC minor group」。需修正/补足 6 点:
(1)原表述「数据窗口为 2024 年 Copilot 对话」→ 精确表述「**2024 年 1 月 1 日至 9 月 30 日**、且**仅限美国**的对话」(原文:「gathered from January 1, 2024 to September 30, 2024. We focus only on conversations in the United States」)。
(2)原表述「20 万条…真实人机对话」→ 需说明构成:**约 10 万条是均匀抽样的主数据集**,另 **10 万条是从「获得过用户点赞/点踩」的对话中均匀抽样的辅助数据集**——后者是反馈自选择样本,用于分析成败,不是代表性样本。写成「20 万条随机对话」会高估代表性。
(3)就业权重用的是 **OEWS 2023**(不是 2024);人口学/工资另用 CPS 2024。
(4)【最需要写进文章的限定】该分数衡量的是「Copilot 用户实际做的活动」与「某职业 O*NET 中间工作活动」的重叠度——**论文并不知道用户本人的职业**,0.18 不代表教师在用 AI,也不代表教师会被替代。「教育的 AI 暴露度接近知识工作」是对分数的合理读法,但必须紧跟这句限定,否则就是作者亲自警告过的那种误用。
(5)【结论要留余地】同表中「Other Healthcare Pracs. and Tech. Occs.」= **0.16**,与教师的 0.18 只差 0.02。用「0.13 vs 0.18」讲「医疗 vs 教育两个阵营」显得比数据本身干净。至少要提 0.16 这一档。
(6)【审稿状态】arXiv 记录中 **无 journal-ref**,Comments 仅「40 pages」,即截至 2026-07 仍是**预印本**;作者全部来自 Microsoft Research(Tomlinson, Jaffe, Wang, Counts, Suri),AI 厂商利益相关必须标注(这点原稿已提,保留)。
(7)【未能核实】配套博客那句「our study does not draw any conclusions about jobs being eliminated…」我未能取得微软官方博客一手页面(本次搜索额度用尽),判为待补;但论文正文中的「This would be a mistake」段已逐字核实,承载同一意思,建议直接用论文原文而非博客转述。

**核验依据**:一手 PDF:https://arxiv.org/pdf/2507.07935v6(《Working with AI: Measuring the Applicability of Generative AI to Occupations》,Kiran Tomlinson, Sonia Jaffe, Will Wang, Scott Counts, Siddharth Suri),pdftotext 后逐格读取 Table 1「SOC minor groups by AI applicability score」全表及表注、第 4.4.2 节评分聚合方法、第 4.1 节「Bing Copilot data」(日期窗口、100k+100k 两个样本、IRB #11028)、第 4.2 节(OEWS 2023 / CPS 2024)、讨论段的「This would be a mistake」全句、限制段(不掌握用户职业、只覆盖一个 AI 平台等)。版本历史与是否有 journal-ref 取自 https://arxiv.org/abs/2507.07935(v1 2025-07-10 → v6 2025-12-22,Comments: 40 pages,无 Journal ref 字段)。


## 批次 F1 — verify:专业vs院校


### 第 1 席


#### [G42] CORRECTED · confidence=high

**修正**:两处必须修正。(1)【最严重】关键论断(c)「学费(办学支出)溢价从未消失,消失的只是同学平均SAT溢价」→ 错误,且被作者本人推翻。学费溢价恰恰是2011/2014版用SSA行政数据消掉的那一个:WP17159第19-20页明说结果与DK(2002)是 partly a contrast——2002版self-revelation模型里log(net tuition)系数为.058(.018)显著;2011版对同批学校重估,自报收入降到.041(.038)不显著,换成SSA行政收入再降到.033(.046),整个1983-2007期间该系数 generally between 0 and .02(never greater than .033)。结论段逐字说Barron's Index与net tuition在self-revelation模型中 small and never statistically distinguishable from zero。正确表述:「学费溢价只存在于2002年那篇的单年自报收入里;换成行政收入长周期数据后同样归零,作者自己做了reconciliation」。另:net tuition=标价学费减平均助学金,是价格,不是「办学支出」,不可译作办学支出。(2)论断C院校数错了:「C&B的30所院校」→ 被引的那句caveat出自WP17159,原句数字是27所(2002年那篇的分析样本才是30所,C&B库共34所)。且原句紧接着有作者自辩:C&B估计与全国代表性的NLS-72结果相近甚至略高,且NLS-72上跑self-revelation模型同样不显著——这句自辩不能删,否则是反向截断,「不覆盖重点vs普通大跨度对比」的推论被作者预先回应过。论断A(WP7322摘要)、论断B(WP17159摘要)与12%/14%/5.2%/virtually no return四个数、JHR 2014题名与卷期页(49(2):323-358,题名确与NBER版不同)全部逐字无误。

**核验依据**:NBER WP7322 PDF (https://www.nber.org/system/files/working_papers/w7322/w7322.pdf) 摘要逐字比对,论断A一字不差;正文「The 30 colleges and universities in our sample」。NBER WP17159 PDF (https://www.nber.org/system/files/working_papers/w17159/w17159.pdf):摘要notable exceptions段逐字一致;p.22 剔除HBCU后1989队列minority的12%/14%;p.22-23 父母教育12年→5.2%(1989队列self-revelation,2007收入)、16年→virtually no return;p.19-20 net tuition的.058/.041/.033 reconciliation;p.23结论net tuition归零;p.27 caveat原句为「the 27 colleges and universities in the C&B dataset」并接NLS-72自辩。JHR版题名/卷期页经 https://jhr.uwpress.org/content/49/2/323 核实(NBER页面那条published-version注记本身有误,并把QJE卷号误植为v107,实为117(4):1491-1527)。


#### [G43] CORRECTED · confidence=high

**修正**:实质内容全部逐字成立,但出处标注需修正两点。(1)版本与数字不匹配:论断标为「NBER WP 31492, 2023-07」,但所引摘要里的「by 50%」是2025-08修订版的数字。2023年7月首发版摘要该处是 60%。正确表述:「NBER WP 31492,2023年7月首发、2025年8月修订;上尾效应经修订后由 +60% 下调为 +50%」。这点对本篇尤其要紧——读者去翻2023年版会看到不同的数字。$101,000/$143,000、top quartile不显著那段、以及「not because of differences in research design」那段,在2023年首发版中即已存在,未变。(2)发表状态:截至2026-07仍是未过审的NBER工作论文,NBER页面无published version注记,PDF首页载明未经同行评议。面向准大学生使用时必须标明这一点。其余全部核实:Ivy-Plus定义(Ivy League+Stanford+MIT+Duke+Chicago,即8+4=12所)与摘要逐字一致;对照组为9所旗舰公立(其中5所有内部录取数据),$143,000是按同分布重新加权后的反事实均值——未加权的旗舰公立均值是$110,000,Ivy-Plus均值$244,000,引用时不要把$143,000说成旗舰公立的实际均值。另注:摘要说 almost triples 名企就业概率,正文对应处写的是 2.5 times,两者并存。

**核验依据**:NBER w31492 PDF (https://www.nber.org/system/files/working_papers/w31492/w31492.pdf) 封面「July 2023, Revised August 2025」;摘要与p.3引言逐字比对全部引语无误。2023年首发版经 Opportunity Insights 镜像 (https://opportunityinsights.org/wp-content/uploads/2023/07/CollegeAdmissions_Paper.pdf) 核对,$101,000/$143,000/top quartile/research design 四段均已存在。60%→50%的改动经 Wayback 快照 http://web.archive.org/web/20230731214938/https://www.nber.org/papers/w31492 确认(该页摘要为「by 60%」)。$110,000/$244,000/$143,000三值见Appendix Figure 28。NBER摘要页无published version。


#### [G44] HOLDS · confidence=high

**核验依据**:NBER WP20816 PDF (https://www.nber.org/system/files/working_papers/w20816/w20816.pdf) 逐字核对:摘要「different fields have widely different payoffs...rival the college wage premiums...as important as the decision to enroll in college」一字不差;p.32「by choosing Science instead of Humanities, individuals almost triple their earnings early in their working career」与「choosing Science instead of Engineering or Business has little payoff」两句均在,后半句确实常被漏引;p.37 预测院校控制后相关系数 0.84、预测同学质量控制后 0.98(附图注分别为0.8386/0.9805);p.32 USD 43,200(无高教学历)vs USD 54,700(有高教学历),均为age 30,+26.6%。数据与识别核实:申请记录1998-2004,教育登记1998-2012,税务登记1998-2012,收入在申请后第8年测量(p.13、p.19、图注),集中录取分数线断点2SLS,LATE。QJE版 131(3):1057-1111, 2016 经期刊页与EconPapers核实。口径警告完全正确:摘要用的是「college wage premiums」,正文对应句是「rival the usual estimates of college earnings premiums」,而43,200/54,700只是他们自己样本里30岁的描述性差距,不是因果大学溢价,更不是美国口径,搬到中美语境说「选专业和上不上大学一样重要」确属换分母。两处轻微用词可收紧(非承重):(a)「挪威全部高教集中申请记录」→ 原文说该集中录取程序 covers almost all universities and colleges,是「几乎全部」不是「全部」;(b)括注的美国大学溢价约+70-80%本轮未回一手核验,建议单独标源或删去。


#### [G45] CORRECTED · confidence=high

**修正**:三段引语与全部数字逐字无误,但两处口径必须补。(1)【必须补】$720,000 / $1.82 million / $500,000 / $3.5 million 全部是按 3% 年贴现率折算的现值,不是名义累计收入——报告尾注ii逐字写明 All cumulative earnings are calculated using a 3 percent annual discount rate,converts earnings into a present value。原表述「生涯累计收入为合成队列」→ 应为「按3%贴现率折现的生涯累计收入现值,由ACS横截面构造的合成队列」。少了「贴现」二字,读者会把$1.82M当成实发工资总额。(2)「同一份报告里方向相反的两句」这个措辞过强:A比的是「全体学士的p25-p75跨度(154%)」对「中位数上最低专业到最高专业的跨度」;B比的是「同一分位上最高专业与最低专业的差额,随分位上升而扩大」。两者是不同的比较对象,逻辑上完全相容,不是相反,只是修辞方向相反。原表述「方向相反的话」→ 应为「修辞方向相反但逻辑相容的两句;A用的是中位数处的专业间跨度做基准,B用的是各分位上的专业间跨度」。至于「只引A会得出选专业无所谓、只引B会得出专业决定一切」这个判断——成立,是准确的选择性引用警告。(3)Andrews et al. 的发表状态需收紧:NBER页面(w30331,2022-08首发/2024-03修订)不列published version,Lovenheim个人主页仍标 Forthcoming,ReStat 侧只有 DOI 10.1162/rest_a_01503 的 accepted 版,尚无卷期页。原表述「ReStat 2024」→ 建议写「NBER WP 30331(2022年8月,2024年3月修订),ReStat 已接收(截至2026-07未见卷期页)」。

**核验依据**:Hamilton Project PDF (https://www.hamiltonproject.org/assets/legacy/files/downloads_and_links/Major_Decisions_Lifetime__Earnings_by_Major.pdf) 逐字核对:p.4「the variation of lifetime earnings within any given major is at least as large as the variation across majors」及$720,000/$1.82 million/154 percent;p.4「fan out」段及第10分位约$500,000、第90分位 over $3.5 million;p.1要点「double—or even triple—...These increases are larger for lower-earning majors」;p.2自设局限「do not necessarily reflect a wage premium for that particular major. The estimates cannot distinguish why...」;p.2样本「workers with exactly a bachelor's degree...do not go on to earn an advanced or professional degree」「not limited to full-time workers and include part-time workers and those who experience unemployment」,80个专业;尾注ii的3%贴现率。NBER w30331 PDF (https://www.nber.org/system/files/working_papers/w30331/w30331.pdf) 引言p.2逐字核对$983/$7,901(四年制,相对liberal arts,高中后16-20年,2016年美元)与分位处理效应那段「notably fields that tend to have higher mean earnings - generating much larger effects at the top of the distribution...substantial (and differential) ex-ante risk」。


#### [G46] CORRECTED · confidence=high

**修正**:全部引语与数字逐字无误,但论断A的护栏本身犯了它要防的那个错:「In levels, earnings growth is rapid for all college graduates, regardless of major」这句之后紧跟一句方向相反的限定语,被截掉了——原文接着说 while computer science, engineering and business majors are earning substantially more in their mid-twenties than do life/physical sciences and social sciences majors, this advantage is greatly diminished by age 40。原表述「原文明说In levels...,媒体写成CS毕业生中年后收入下滑是错的」→ 应为「原文说绝对收入所有专业都在快速增长,媒体写成CS中年后收入绝对下滑是错的;但原文同一段紧接着说,CS/工程/商科相对生命/物理科学与社科的绝对收入优势到40岁已 greatly diminished——所以只引前半句同样是截断」。另两处建议收紧(非承重):(a)45%→33% 的完整基准是 Relative to all other major groups (including education),写「相对所有其他专业」时最好带上 including education;(b)Andrews et al. 的12.7倍在同一篇内有两种时窗表述——引言写 over a 10 to 15-year period,正文第4节写 in the two decades after high school,引用时须标明用的是哪一处。结论「不存在支持专业效应普遍衰减的强证据、三者方向不一致」——成立。Webber的「moderate convergence」逐字核实无误,但须加限定:那是三个出生队列(1955-64/1965-74/1975-84)之间、相对高中毕业生的生涯收入溢价的收敛,且依赖「未观测生涯段的收入形状不随队列剧变」这一强假设,与Deming-Noray/Andrews的「同一队列内随年龄变化」不是同一个维度,并列时不可混为一谈。

**核验依据**:Deming & Noray, QJE 135(4):1965-2005 PDF (https://www.sas.upenn.edu/~vr0j/oldteaching/712tqm-22/DemingNoray_2020.pdf) 逐字核对:p.1989 45%/33%、business 38%/20%、life and physical sciences 与 social sciences 溢价随时间上升;p.1990「In levels, earnings growth is rapid for all college graduates, regardless of major」及其后紧跟的 greatly diminished by age 40 一句;p.1993「Declining relative returns is a feature of STEM jobs, not majors」及 non-STEM 专业在 STEM 职业里由约40%降到20%;p.1995 CS/工程从26岁59%降到50岁41%、18个百分点、由非STEM管理岗抵消。样本核实为2009-2017 ACS、四年制本科毕业生23-50岁、左侧省略组为 all other majors。Andrews et al. NBER w30331 引言p.2 的 12.7倍($413→$5,655)已核,正文对应段写作 in the two decades after high school。Webber 原文 (http://www.doug-webber.com/LE%20paper.pdf) p.3「there has been a moderate convergence over time in the return to the various major categories」,三队列定义见p.20。


#### [G47] CORRECTED · confidence=high

**修正**:三套数字全部复算无误,但四处口径须修。(1)【必须补】NSCG 2019 已被取代:NSCG 2023 数据表(NSF 25-322,2025年发布)同名Table 1-3——全体(56,061,000):closely 53.7% / somewhat 27.1% / not related 19.1%;仅本科为最高学历者(34,311,000):43.6% / 31.1% / 25.3%。原表述「NSCG: 2019 Table 1-3」→ 应改用2023波,或至少标明2019已非最新。(2)【必须补】NSCG问的是「工作与最高学历的关系」,不是「与本科专业的关系」。对全体那一行(含硕博),19.6%指的是与最高学历领域不对口,不能读成「本科专业转行率」。仅本科那一行(25.7%)才近似本科对口率。(3)Abel-Deitz的27%有一个被省略的样本限制:计算College Major Match时作者明确剔除了有研究生学历的人(we omit individuals with a graduate degree from our analysis that utilizes this measure),因此27%与NSCG的54.1%不可直接对照。另需补:数据为2010年ACS,SR587为2012年12月稿、2014年12月修订,已发表于Regional Science and Urban Economics。(4)【题名错误】EdWorkingPaper 23-760 的真实题名是《The Increasing Penalty to Occupation-Education Mismatch》,不是「Occupation-Major Mismatch」;作者 Cassidy & Gaulke,已发表于 Economic Inquiry 62(2):607-632 (2024)。结论成立:1993→2019 不对口率仅由19%微降至17%(全职样本),但工资惩罚上升51%(1993年基准约11%,Robst 2007a),somewhat mismatched 的惩罚上升179%。但两点须标:它用的是与A同一套NSCG自报「与最高学历不对口」指标,不是独立测量;且是观测性OLS,非因果。(5)由此,「+25%与+5%即学历门槛比对不对口重要5倍」这句要加限定——那是 Abel-Deitz 在2010年ACS上用分析师交叉编码得到的条件回归系数比;换成 Cassidy-Gaulke 的自报口径,不对口惩罚本身就有11-17%,与+5%相差三倍以上。原表述「有没有学历门槛比对不对口重要5倍」→ 应为「按 Abel-Deitz 的分析师编码口径,学历门槛的工资溢价约为专业对口额外溢价的5倍;换成NSCG自报口径,对口的重要性要高得多,两套口径不可互换」。

**核验依据**:NSCG 2019 数据表 NSF22-310 PDF (https://ncses.nsf.gov/pubs/nsf22310/assets/nsf22310.pdf) Table 1-3 原始计数复算:全体 27,340,000/13,258,000/9,927,000 ÷ 50,524,000 = 54.11%/26.24%/19.65%;Bachelor's 13,818,000/9,508,000/8,048,000 ÷ 31,373,000 = 44.04%/30.31%/25.65%,与论断一致。NSCG 2023 数据表 NSF25-322 PDF (https://ncses.nsf.gov/pubs/nsf25322/assets/nsf25322.pdf) 同表复算得 53.74/27.14/19.11 与 43.56/31.09/25.34。NY Fed Staff Report 587 PDF (https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr587.pdf):p.7 的27%与剔除研究生学历的说明;p.7-8 的CS 73%/33%、Computer Engineering 80%/Studio Arts 44%;p.22 逐字「almost 25 percent more」与「an additional 5 percent more...on top of the wage premium for a College Degree Match」;p.5「2010 American Community Survey」;封面 December 2012, revised December 2014,注明将发表于 Regional Science and Urban Economics;College Degree Match 平均率 62%、正文另称约two-thirds。Census 2021-06-02 story (https://www.census.gov/library/stories/2021/06/does-majoring-in-stem-lead-to-stem-job-after-graduation.html):2019年ACS 1年数据、25-64岁在职大学毕业生5000万,六个专业比例52/51/28/16/10/9 与 $101,100 vs $87,600 逐字一致。EdWorkingPaper 23-760 PDF (https://edworkingpapers.com/sites/default/files/ai23-760.pdf) 封面题名为 Occupation-Education Mismatch,摘要含19%→17%与+51%,正文p.3含1993年11%基准、2003年+35%、2010年+57%、somewhat mismatched +179%,样本限于全职;发表版见 Economic Inquiry 62(2):607-632 (2024)。


### 第 2 席


#### [G42] CORRECTED · confidence=high

**修正**:(1) 最严重一处 —— 关键论断 (c)「学费(办学支出)溢价从未消失,消失的只是『同学平均 SAT』溢价」→ 被 DK 自己的更新版直接推翻。WP 17159 结论段逐字:"the returns to other college characteristics (the Barron's Index and net tuition) are substantial in the basic model that controls for commonly observed student characteristics but small and never statistically distinguishable from zero in the self-revelation model";并明说与 2002 年的差异:"These results are partly a contrast to Dale and Krueger (2002), in that the earlier analysis of self-reported earnings data showed a statistically significant relationship between earnings and the log of net tuition in the self-revelation model, as the coefficient on net tuition was of .058 (.018)." 正确表述:「学费溢价在 1999/2002 自报收入版本中显著(0.058, se 0.018),但在 2011/2014 用 SSA 行政收入的更新版中同样落到不显著 —— 它不是从未消失,而是和 SAT 溢价一起消失了。」(2) 论断 A 的出处标注错误。所引摘要逐字出自 NBER WP 7322(1999-08),不是 QJE 2002。QJE 117(4):1491-1527 的已发表摘要**完全不含学费那句**,且末句是 "Children from low-income families, however, earned more if they attended selective colleges."(低收入家庭),而非「更弱势家庭背景」。原表述「QJE 2002 / NBER WP 7322 摘要逐字」→ 应为「NBER WP 7322(1999)摘要逐字;QJE 2002 已发表摘要另有措辞且删去了学费句」。(3) 论断 C 院校数与引语不匹配:该「非全国代表性」caveat 出自 WP 17159,其原文为 "the sample is derived from the 27 colleges and universities in the C&B dataset";30 所是 DK 1999/2002 的样本(C&B 共 34 所)。原表述「C&B 的 30 所院校」+ 该引语 → 应为「WP 17159 为 27 所;DK 2002 为 30 所(C&B 共 34 所)」。(4) 论断 C「不覆盖『重点 vs 普通』的大跨度对比」需加限定:同段紧接着写 "estimates ... based on the C&B dataset were similar to -- indeed, slightly higher than -- those based on a nationally representative dataset, the National Longitudinal Study (NLS) of the High School Class of 1972",且 DK 2002 用 NLS-72 跑 self-revelation model 同样得到不显著结果。作者已用全国代表性数据做过稳健性检验,不能只说样本窄。(5) 以下逐字无误,可放心引用:12%/14%(1989 队列剔除 HBCU 后的少数族裔估计)、200 分 → 5.2%(父母平均 12 年教育)、"there was virtually no return"(父母平均 16 年教育)、"does not pertain to a nationally representative sample of schools"、WP 7322 与 WP 17159 两段摘要全文。(6) JHR 题名判断正确并已证实:JHR 49(2):323-358 (2014) 题为 "Estimating the Effects of College Characteristics over the Career Using Administrative Earnings Data" —— 注意 NBER 官网自己的 published-version 字段是错的(写成 "...Return to College Selectivity of the Career ... Earning Data")。(7) 关键论断 (a)「结果变量是对数收入」已由独立一手来源交叉证实:Chetty-Deming-Friedman 原文写 "consistent with the findings of Dale and Krueger (2002), whose primary outcome is log earnings"。

**核验依据**:我自行下载 PDF 并用 pdftotext 逐字提取,非二手转述。NBER WP 7322 全文 https://www.nber.org/system/files/working_papers/w7322/w7322.pdf(摘要逐字核对通过;正文「The 30 colleges and universities in our sample」);NBER WP 17159 全文 https://www.nber.org/system/files/working_papers/w17159/w17159.pdf(摘要逐字通过;第22页 12%/14% 段;第22-23页 5.2%/virtually no return 段;结论段 net tuition 不显著 + 「partly a contrast to Dale and Krueger (2002)」+ .058(.018);caveat 段「27 colleges and universities」);QJE 2002 已发表摘要 https://ideas.repec.org/a/oup/qjecon/v117y2002i4p1491-1527..html;JHR 题名 https://jhr.uwpress.org/content/49/2/323.short 与 https://econpapers.repec.org/RePEc:uwp:jhriss:v:49:y:2014:ii:1:p:323-358;NBER 著录页 https://www.nber.org/papers/w17159


#### [G43] CORRECTED · confidence=high

**修正**:(1) 全部引语与数字逐字无误 —— 摘要「reaching the top 1% of the earnings distribution by 50%」句、"The impact of Ivy-Plus admission on reaching the top quartile of the distribution is small and statistically insignificant"、"$101,000 at age 33 (relative to a counterfactual mean of $143,000...)"、"not because of differences in research design but rather because our richer data..."、"modest impacts ... on log earnings, consistent with the findings of Dale and Krueger (2002), whose primary outcome is log earnings" —— 我在正文 p.3 逐字比对全部命中。Ivy-Plus 定义也逐字证实:"(Ivy League, Stanford, MIT, Duke, and Chicago)",即 8+4=12 所。(2) 引用版本已过期。原表述「NBER WP 31492, 2023-07」→ 应为「NBER WP 31492, July 2023, **Revised August 2025**;已发表于 Quarterly Journal of Economics 141(1), 2026-02, pp. 51-145」。截至 2026-07 该文早已过审发表,以工作论文身份引用会让读者低估其地位。(3) 关键推论「分歧是结果变量口径,不是研究设计」**只说对了一半**,漏掉作者给出的第一条理由。原句是并列两项:"our richer data allow us to directly identify college's fixed effects (rather than using proxies for quality such as test scores) **and** isolate impacts on upper tail outcomes"。前一项是**数据与质量度量口径**之差(直接估院校固定效应 vs 用同学平均 SAT 做代理),不是结果变量之差;且作者另外写 "we find little association between students' average outcomes and the mean test scores of the college they choose to attend, the proxy for college quality used by Dale and Krueger and others" —— 这是对 DK 代理变量本身的批评。正确表述:「分歧来自两处:一是 DK 用『同学平均 SAT』做院校质量代理而 CDF 直接识别院校固定效应,二是结果变量选对数收入还是上尾概率。研究设计确实不是分歧来源(CDF 复刻 DK 的 matriculation design 得到统计上无法区分的结果)。」(4) 「名校对中位数几乎没用」是转写而非原文。论文的空结果是「进入收入分布**前四分之一**的概率」这一门槛跨越概率不显著,以及 matriculation design 下**对数收入**影响 modest;论文没有直接报中位数效应。建议按原文说「对进入前 25% 的概率无显著影响、对对数收入影响不大」。(5) $101,000/$143,000 须与「均值」二字同时出现:这是**均值**收入提升(约 +71%),由上尾拉动,与「对中位数几乎没用」并置时若不点明均值/中位数之别,读者会算出矛盾。原文亦以 "As a result of these upper-tail impacts" 领起。

**核验依据**:我自行下载 https://www.nber.org/system/files/working_papers/w31492/w31492.pdf 并 pdftotext 提取:封面「July 2023, Revised August 2025」;摘要逐字含 Ivy-Plus 定义与 50%/nearly doubles/almost triples;正文 p.3 含 top quartile 空结果、$101,000/$143,000、"not because of differences in research design"、"whose primary outcome is log earnings"、"little association ... the proxy for college quality used by Dale and Krueger"。发表信息:QJE 141(1):51-145 (2026-02),https://academic.oup.com/qje/article-abstract/141/1/51/8306880 与 https://ideas.repec.org/a/oup/qjecon/v141y2026i1p51-145..html


#### [G44] CORRECTED · confidence=high

**修正**:(1) 本条是本批最扎实的一条。全部引语与三个数字逐字命中:摘要 "We find that different fields have widely different payoffs..." 整段;"by choosing Science instead of Humanities, individuals almost triple their earnings early in their working career. By comparison, choosing Science instead of Engineering or Business has little payoff.";"The correlation between the estimated payoffs with and without controls for predicted institution is 0.84.";"We find a correlation of 0.98 between the estimated payoffs with and without controls for predicted peer quality.";"USD 43,200 at age 30" / "USD 54,700"。方法学描述也逐字证实:1998–2004 全部集中申请记录、挪威税务登记 1998–2012、"every cohort is observed for at least eight years after their application"、结果变量为申请后第 8 年年收入。发表信息证实:QJE 131(3):1057–1111 (2016)。(2) 需修正的**分母口径**(claim 自己在警告分母,但它自己的转述也差一格):原表述「个人未完成任何高等教育者平均年收入 43,200 美元 vs ...54,700」被称作「挪威口径的大学溢价」→ 原文对照组是 "individuals with a **post-secondary** degree",即**任何高等教育学位(含短学制/学院)**,不是「大学」;且这是**原始描述性均值差**(30 岁),不是任何回归估计的溢价。正确表述:「作者在自己数据里给出的参照是:无任何高等教育者 30 岁平均 43,200 美元,有高等教育学位者 54,700 美元(+26.6%),这是未加控制的原始均值差,不是估计出的大学溢价。」(3) 摘要与正文措辞不同,引用时宜用正文的完整版:摘要作 "the payoffs rival the college wage premiums",正文(WP 版)作 "the payoffs rival the **usual estimates of** college earnings premiums" —— 正文措辞更清楚地说明这是与文献通行估计比,不是与作者自算的那两个数比。claim 把「rival 的对象」直接等同于 43,200/54,700 这一对数字,是推断而非原文断言(原文只是紧接着举这两个数作 "In our data, for example" 的量级说明)。(4) 「不是美国的大学溢价(约 +70-80%)」这一背景数字在本批未回到一手核实,属 claim 自带的未标源断言,发表前须补 BLS 或 Census 一手出处。(5) 外部效度限制成立且应写明:估计是断点附近 compliers 的 LATE;挪威为集中录取、公立免学费、工资压缩显著的劳动力市场,专业间收入差本就被压缩,把「专业和上不上大学一样重要」直接搬到中美语境,除换分母外还换了整个工资分布形态。

**核验依据**:我自行下载 https://www.nber.org/system/files/working_papers/w20816/w20816.pdf 并 pdftotext 提取:摘要整段;引言第 2 页 "almost triple ... little payoff";正文 p.789/797/810-821「1998 to 2004」「Norwegian tax registers over the period 1998 to 2012」「observed for at least eight years after their application」「earnings 8 years after application」;p.~34「rival the usual estimates of college earnings premiums ... USD 43,200 at age 30 ... USD 54,700」;p.~36「correlation ... predicted institution is 0.84」;p.~37「a correlation of 0.98 ... predicted peer quality」。发表信息 https://academic.oup.com/qje/article-abstract/131/3/1057/2461218 与 https://econpapers.repec.org/RePEc:oup:qjecon:v:131:y:2016:i:3:p:1057-1111.


#### [G45] CORRECTED · confidence=high

**修正**:(1) **最重要的一处口径遗漏:所有美元数字都是按 3% 折现的现值,不是名义生涯收入总和。** 报告尾注 ii 逐字:"All cumulative earnings are calculated using a 3 percent annual discount rate. This converts earnings into a 'present value'..."。$720,000 / $1.82 million / $500,000 / $3.5 million / $1.19 million 全部是 PV。原表述「生涯累计收入」→ 应为「按 3% 折现的生涯累计收入现值」。面向准大学生时这个差别很大。(2) **$720,000 / $1.82 million 这一对数字不是「专业内」方差。** 原文逐字:"**For all majors combined**, lifetime earnings at the 25th percentile ... are $720,000, but they are $1.82 million at the 75th percentile" —— 这是**所有专业合并后**的 25/75 分位差,同时包含专业内与专业间变异,因此不能单独用来支撑「专业内方差 ≥ 专业间方差」。报告真正的专业内陈述是另一句:"Cumulative earnings double—or even triple—when moving from the bottom quarter to the top quarter of earners in a given major." 引用时两句不可互换。(3) **論斷 C 的「因果版本」定性错误 —— 这是本条最硬的一处。** Andrews, Imberman, Lovenheim & Stange(WP 30331)自述逐字:"**Our selection-on-observables method** compares students with similar pre-collegiate test scores and student demographics who graduated from the same high school in the same year and who attended the same college ... While this approach makes the strong assumption that these observables are sufficient to account for all differences across students in potential labor market outcomes...";并明说 "there are few opportunities to use a **regression discontinuity (RD) approach** in the US across multiple fields and institutions"(即他们没用 RD);结论段再次自我归类 "the returns to major literature using **selection on observables** techniques"。原表述「论断 C(因果版本)」→ 应为「论断 C(可观测项选择模型,非因果识别;控制同高中同届同校同届入学 + 大学前测验分)」。把它与挪威 RD/2SLS 并列称因果证据,是本批最容易误导读者的一处。(4) 版本:WP 30331 为 "August 2022, **Revised March 2024**";claim 所称「ReStat 2024」我未回到 ReStat 一手核实,发表前须补验。(5) 逐字无误可引用:"the variation of lifetime earnings within any given major is at least as large as the variation across majors"、154 percent、"These increases are larger for lower-earning majors."、"grow larger—or fan out—higher up" 及 10th/90th 分位 $500,000 / over $3.5 million、"Quarterly returns (relative to liberal arts) range from $983 in communications to $7,901 in engineering and architecture 16-20 years after high school"、"notably fields that tend to have higher mean earnings - generating much larger effects at the top of the distribution. This suggests the mean effects embed substantial (and differential) ex-ante risk for students."、以及作者自设局限 "...do not necessarily reflect a wage premium for that particular major. The estimates cannot distinguish why graduates in certain majors earn more than those in others." 全部命中。(6) 样本描述正确并可再补一句:"workers with exactly a bachelor's degree ... do not go on to earn an advanced or professional degree";"not limited to full-time workers and include part-time workers and those who experience unemployment throughout the year"。这一条在与 Deming-Noray(限全职)对照时必须点明,否则两文数字不可比。(7) 「同一份报告里两句方向相反的话」这个定性**偏重**。A 与 B 在原文里不矛盾:A 是合并样本的四分位跨度,B 是分布两端的专业间差距,二者是同一分布的不同切面(与 G43 的上尾/中位数问题同构)。报告自身的首条结论恰是 "a college degree—in any major—is important for advancing one's earnings potential"。正确表述:「不是两句相反的话,而是同一分布在不同分位上的两个切面;单引任一句都会被误读,但报告本身并不自相矛盾。」(8) 利益相关须标注:Hamilton Project 隶属 Brookings,是政策倡导型项目而非统计机构;作者 Hershbein(Upjohn)、Kearney(Maryland)。

**核验依据**:我自行下载 https://www.hamiltonproject.org/assets/legacy/files/downloads_and_links/Major_Decisions_Lifetime__Earnings_by_Major.pdf 并 pdftotext 提取:p.1 首条结论;p.2「workers with exactly a bachelor's degree」「not limited to full-time workers」;p.4 自设局限段;p.5「LIFETIME EARNINGS DIFFERENCES WITHIN MAJOR」整段($720,000 / $1.82 million / 154 percent)与「fan out」段($500,000 / over $3.5 million);p.6 尾注 ii 折现率 3%。Andrews et al.:我自行下载 https://www.nber.org/system/files/working_papers/w30331/w30331.pdf 并提取,封面「August 2022, Revised March 2024」,引言 p.1-2 自述 selection-on-observables 与「few opportunities to use a regression discontinuity (RD) approach」,p.2 $983/$7,901 与 QTE 段,结论 p.27「using selection on observables techniques」


#### [G46] CORRECTED · confidence=high

**修正**:(1) Deming-Noray 全部引语与数字逐字命中:45%→33%、business 38%→20%、"In contrast, the earnings premium grows over time for life and physical sciences and social sciences majors."、"declines from 59% at age 26 to 41% by age 50. This decline of 18 percentage points is almost entirely offset by increased employment in non-STEM management occupations."、"Declining relative returns is a feature of STEM jobs, not majors." 整段、"In levels, earnings growth is rapid for all college graduates, regardless of major." 全部存在。QJE 135(4):1965-2005、2009–2017 ACS、23–50 岁亦证实。(2) **样本限定漏了一个关键词:全职。** 图表注逐字为 "full-time working four-year college graduates aged 23–50 in the 2009–2017 American Community Survey"。原表述「2009-2017 ACS,23-50 岁四年制本科毕业生」→ 应加「**全职在职**」。这一点在与 Hamilton Project(明确纳入兼职者与全年有失业经历者)并置时是决定性的,否则两文不可比。(3) **claim 自己犯了它要防的截断。** 「In levels, earnings growth is rapid for all college graduates, regardless of major」的**下一句**是:"However, while computer science, engineering and business majors are earning substantially more in their mid-twenties than do life/physical sciences and social sciences majors, **this advantage is greatly diminished by age 40.**" 只引前半句会让读者以为绝对量上的领先也稳固;原文说的是绝对收入都在涨、但 CS/工程/商科对生命物理科学与社科的绝对领先到 40 岁已大幅缩小。两句必须同时出现。(4) **漏掉脚注 23 的机制警告。** 原文脚注 23 逐字:"The rapid growth in life cycle earnings for life and physical sciences majors is partly due to their very high rate of graduate school attendance." claim 把「生命科学/社科溢价扩大」当作反驳「普遍衰减」的正面证据,却不提作者已把其中一部分归因于读研率,这是选择性引用。(5) **論斷 B 同样被错标为因果**(与 G45 C 同一错误):Andrews et al. 自述 "Our selection-on-observables method...",并说明美国跨专业跨院校几乎无法做 RD。原表述「Andrews et al. 的德州因果估计」→ 应为「Andrews et al. 的德州可观测项选择估计」。(6) **12.7 倍被断章为「生物健康是例外」。** 原文在四年制部门写的是 "The return to **each** major increases relative to liberal arts over time, although the rate of..." —— 是**所有**专业相对文理科的回报都随生涯上升,生物健康只是涨幅最大者(12.7 倍,$413→$5,655)。更关键的是**基准不同**:Andrews et al. 的基准是 liberal arts,Deming-Noray 的基准是 "all other majors"(图注逐字:"The left-out category is all other majors"),且一个是季度美元水平差、一个是对数工资溢价。两者不构成对同一量的相反测量。(7) Webber 的「中度收敛」是**出生队列之间**(1955–64 / 1965–74 / 1975–84)的专业溢价收敛,不是同一队列**生涯内**的衰减 —— 把它并入「生涯剖面方向不一致」的三方对照属类别混用(claim 的括注「队列间」已暗示,但正文并列时会被读成同类证据);此项我只查到二手著录,未回到 Webber (2014, Labour Economics) 原文,发表前须补验。(8) 最终结论需降级重写。原表述「没有一篇支持『专业效应普遍衰减』的强证据;三者方向不一致」→ 应为「三项研究基准不同(all other majors vs liberal arts)、度量不同(对数溢价 vs 季度美元)、样本与年龄窗不同(全职 23–50 岁全国 ACS vs 德州高中队列毕业后 16–20 年),不能直接互相印证或互相反驳。可以说的是:**目前没有可比口径的证据支持『专业效应普遍衰减』**,而不是『三者方向不一致因此不存在衰减』。」

**核验依据**:我自行下载 https://www.sas.upenn.edu/~vr0j/oldteaching/712tqm-22/DemingNoray_2020.pdf 并 pdftotext 提取:p.1989-1990 含 45%/33%、38%/20%、life and physical sciences 句、脚注 23、"In levels, earnings growth is rapid..." 及其后 "this advantage is greatly diminished by age 40";图 VI 注 "The left-out category is all other majors";p.1993 "Declining relative returns is a feature of STEM jobs, not majors" 整段;p.1994 59%→41% 与 18 percentage points;正文 p.121-122、1333、1549、1604 确认 2009–2017 ACS、full-time working、aged 23–50。Andrews et al. https://www.nber.org/system/files/working_papers/w30331/w30331.pdf:p.2 "increasing by a factor of 12.7 (from $413 to $5,655)";p.~30 "The return to each major increases relative to liberal arts over time";p.1-2 selection-on-observables 自述。Webber 仅二手:https://www.sciencedirect.com/science/article/abs/pii/S0927537114000281


#### [G47] CORRECTED · confidence=high

**修正**:(1) **論斷 A 全部六个百分比经我用官方 xlsx 逐格复算,全部正确。** NSCG 2019 表 1-3:全体(All degrees)N=50,524,000,closely 27,340,000=54.11%、somewhat 13,258,000=26.24%、not related 9,927,000=19.65%;仅本科为最高学历(Bachelor's)N=31,373,000,closely 13,818,000=44.04%、somewhat 9,508,000=30.31%、not related 8,048,000=25.65%。与 claim 完全吻合。(2) **但版本已过期,须换 2023。** NSCG **2023** 数据表已于 2025-01-13 发布(NSF 25-322)。同一张表 1-3(我同样下载官方 xlsx 复算):全体 N=56,061,000 → closely 53.7% / somewhat 27.1% / **not related 19.1%**;仅本科 N=34,311,000 → closely 43.6% / somewhat 31.1% / **not related 25.3%**。原表述「NSCG: 2019 ... 19.6% / 25.7%」→ 2026 年发表应改用 2023 年数据「19.1% / 25.3%」(结论方向不变,数字须更新)。(3) **論斷 B 引语逐字全部命中,包括最关键的 +25% 与 +5%** —— "college graduates working in a job that requires a college degree earn, on average, almost 25 percent more than those who do not match along this dimension" 与 "those college graduates who work in a job closely related to their college degree major earn, on average, an additional 5 percent more than those who do not, which in principle is on top of the wage premium for a College Degree Match"。27%、73%/33%、80%/44%(Studio Arts)、Degree Match 62%/约三分之二 也全部逐字命中。(4) **但 B 的样本限定被系统性省略了四条,必须补上。** 原表述「NY Fed Staff Report No. 587,数据=2010 年 ACS」→ 应为「NY Fed Staff Report No. 587,**2012 年 12 月发布、2014 年 12 月修订**,数据=2010 年 ACS,样本限**大都市区内**、16–64 岁、在民用劳动力中;27% 的对口率**剔除了所有拥有研究生学位者**;产生 +25%/+5% 的那组回归进一步限**全职(每周≥35 小时且每年≥40 周)、时薪 5–400 美元、无研究生学位**,约 162,000 观测代表约 1,700 万人;且这是一组**城市工资(集聚效应)回归**中的条件相关系数,非因果估计。」(5) **「『有没有学历门槛』比『对不对口』重要 5 倍」是过度解读,须改写。** 原文明说这 5% 是 "**on top of**" 那 25% —— 两者是嵌套的两道门槛而不是二选一的替代项;把两个来自同一横截面回归的点估计相除得出「重要 5 倍」,既没有统计检验支撑,也暗示了一个原文没有的取舍。正确表述:「在这份 2010 年横截面的城市工资回归里,『岗位要求本科学历』对应约 +25% 的工资,在此之上『岗位与专业对口』再对应约 +5%。两者叠加而非互斥,系数之比不等于重要性之比。」(6) **論斷 C 逐字无误**:六个专业的 STEM 就业比例(工程 52%、计算机/数学/统计 51%、物理科学 28%、生物/环境/农业 16%、心理 10%、社科 9%)与 "$101,100 vs. $87,600" 全部命中;出处为 Census 2021-06-02、作者 Jennifer Cheeseman Day 与 Anthony Martinez、数据为 2019 年 ACS 1-year、25–64 岁。**需补一句限定**:$101,100 vs $87,600 是**在 STEM 职业内部**比较「STEM 专业出身 vs 非 STEM 专业出身」的薪资,不是一般意义上的专业溢价。(7) **EdWorkingPaper 23-760 的题名 claim 写错了。** 原表述「《The Increasing Penalty to Occupation-**Major** Mismatch》」→ 正确为「《The Increasing Penalty to Occupation-**Education** Mismatch》,Hugh Cassidy & Amanda Gaulke,EdWorkingPaper 23-760(2023-04),已发表于 Economic Inquiry 62(2): 607-632 (2024)」。其结论**成立**且确实构成对「专业不重要反正都要转行」的反驳:用 NSCG 数据,1993–2019 年间错配率仅微降(19%→17%),但错配的工资惩罚**上升了 51%**。**但须同时说明其机制**:作者把上升部分归因于「专业构成变化」与「"excess" education(超出岗位要求的学历)回报下降」,后者是**学历层级**口径而非专业对口口径 —— 这反而与 Abel-Deitz 的「学历门槛」那一维相通。(8) **claim 的核心框架(三套口径不可混用)完全成立,是本条最有价值的部分,建议保留并加粗**:A 是受访者**自评**「工作与**最高学位**的相关程度」(三档,只有『完全不相关』一档计入 19.6%);B 是分析师用职业—专业交叉编码判定「是否**直接对口本科专业**」(二值,27% 对口即 73% 不直接对口);C 是「是否在 **STEM 职业**就业」。三者分子分母定义各不相同,任何跨口径的加减或对比都是错的。

**核验依据**:NSCG 2019:我下载官方表格 https://ncses.nsf.gov/pubs/nsf22310/assets/data-tables/tables/nsf22310-tab001-003.xlsx 并用 openpyxl 逐格读原始计数后自行复算百分比(All degrees 行第 6 行、Bachelor's 行第 46 行);表页 https://ncses.nsf.gov/pubs/nsf22310/table/1-3。NSCG 2023:同法下载 https://ncses.nsf.gov/pubs/nsf25322/assets/data-tables/tables/nsf25322-tab001-003.xlsx(All degrees 第 6 行 56,061,000/30,129,000/15,217,000/10,715,000;Bachelor's 第 46 行 34,311,000/14,948,000/10,669,000/8,694,000),发布状态见 https://ncses.nsf.gov/surveys/national-survey-college-graduates/2023(数据表 2025-01-13 发布)。Abel-Deitz:WebFetch 遭 403,改用带 UA 的 curl 取回 https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr587.pdf 后 pdftotext 提取 —— 封面「Staff Report No. 587, December 2012, Revised December 2014」;p.7-8 的 27%/73%/33%/80%/44%;p.7 的 2010 ACS 与大都市区限定;p.~28 的全职与时薪限定、162,000 观测;p.~30 的 25%/5% 段。Census:https://www.census.gov/library/stories/2021/06/does-majoring-in-stem-lead-to-stem-job-after-graduation.html。Cassidy-Gaulke:我下载 https://edworkingpapers.com/sites/default/files/ai23-760.pdf 提取封面与摘要(题名为 Occupation-Education Mismatch,19%→17%,penalty +51%),发表信息 https://onlinelibrary.wiley.com/doi/abs/10.1111/ecin.13192 与 https://ideas.repec.org/a/bla/ecinqu/v62y2024i2p607-632.html


### 第 3 席


#### [G42] CORRECTED · confidence=high

**修正**:关键论断(c) 方向完全相反,必须删改。原表述:"学费(办学支出)溢价从未消失,消失的只是'同学平均 SAT'溢价" → 正确表述:"学费溢价只存在于 2002 年那版(自报收入);2011/2014 年改用 SSA 行政收入记录后,学费溢价与 SAT 溢价一起消失了"。WP 17159 第23页逐字:"the returns to other college characteristics (the Barron's Index and net tuition) are substantial in the basic model that controls for commonly observed student characteristics but small and never statistically distinguishable from zero in the self-revelation model";并明确写"These results are partly a contrast to Dale and Krueger (2002), in that the earlier analysis of self-reported earnings data showed a statistically significant relationship between earnings and the log of net tuition in the self-revelation model, as the coefficient on net tuition was of .058 (.018)." 作者复算:同一批学生 1995 年自报收入 self-revelation 系数降为 .041 (.038) 不显著,换成 SSA 行政数据后进一步降至 .033 (.046)。所以"学费溢价"恰恰是被 2011 版修订掉的那一条,拿它当"从未消失"的论据是把修订方向读反了。第二处:样本院校数。原表述"C&B 的 30 所院校"(挂在"nationally representative"那句限定语上)→ 正确表述:WP 17159 该句原文是 "the sample is derived from the 27 colleges and universities in the C&B dataset, the majority of which are very selective";30 所是 DK 2002/WP 7322 的样本(C&B 库共 34 所),两版数字不同,不可混用。论断 A、B 引语与 12%/14%/5.2%/"virtually no return" 四个数字逐字无误,(a)(b) 两条以及 JHR 题名/卷期页码无误。

**核验依据**:NBER WP 7322 PDF (https://www.nber.org/system/files/working_papers/w7322/w7322.pdf) 摘要逐字核对,论断 A 三句("do not earn more..."/"However, the average tuition charged by the school is significantly related..."/"Lastly, the payoff to attending an elite college appears to be greater for students from more disadvantaged family backgrounds.")完全一致;正文见 "The 30 colleges and universities in our sample"(源自 34 所库)。NBER WP 17159 PDF (https://www.nber.org/system/files/working_papers/w17159/w17159.pdf) 摘要逐字一致;pp.22 "implying returns of 12 percent for attending a school with 100 point higher SAT score and 14 percent for attending a school in a higher Barron's category, even in the self-revelation model"(1989 队列、剔除 HBCU);pp.22-23 "a 200-point higher SAT score would lead to 5.2 percent higher earnings in 2007 for those with average parental education of 12 years... for those whose parents averaged 16 years of education... there was virtually no return";pp.24 "the analysis does not pertain to a nationally representative sample of schools, as the sample is derived from the 27 colleges and universities in the C&B dataset";pp.23 与 pp.19 为学费溢价被推翻的两处原文。发表版题名经 JHR/EconPapers 核实:Journal of Human Resources 49(2): 323-358, 2014, "Estimating the Effects of College Characteristics over the Career Using Administrative Earnings Data"(https://jhr.uwpress.org/content/49/2/323.short),确与 NBER 版题名不同。


#### [G43] CORRECTED · confidence=high

**修正**:全部引语与数字逐字无误,但两处口径/著录需修:(1) 著录已过期。原表述"NBER WP 31492, 2023-07" → 正确表述:"NBER WP 31492, 2023 年 7 月、2025 年 8 月修订;已发表于 Quarterly Journal of Economics 141(1): 51-145, 2026 年 2 月"。核验任务问"截至 2026-07 是否已过审",答案是已过审并正式刊出,不应再按未过审工作论文引用(NBER PDF 首页现印 "July 2023, Revised August 2025",且载明 NBER WP "have not been peer-reviewed",此免责声明已不适用于发表版)。(2) 对照组构造被高估了普适性。原表述"对照组 = the average flagship public college"若读成"美国旗舰公立大学的平均" → 正确表述:该对照组是作者自有 college-specific 样本中 9 所旗舰公立的平均,原文 "the outside option (college O), which we define as the average flagship public college in our college-specific sample (i.e., the 9 colleges listed in Appendix Table 1)",且 $143,000 反事实均值是按测验分数 reweighted 后的口径(图注 "Mean Income for Flagship Public (Reweighted): $143,000")。(3) 一处小提示:摘要写 "almost triples their chances of working at a prestigious firm" 与 "nearly doubles",正文导论对应处写作 "2.5 times as likely" 与 "nearly twice as likely";引摘要版无误,但两处并存,勿混引。Ivy-Plus 定义(8 常春藤 + Stanford + MIT + Duke + Chicago,共 12 所)、"top quartile... small and statistically insignificant"、$101,000/$143,000、"not because of differences in research design" 均逐字无误,关键推论(结果变量选中位数还是上尾会给出相反答案)成立。

**核验依据**:NBER WP 31492 PDF (https://www.nber.org/system/files/working_papers/w31492/w31492.pdf) 逐字核对:首页 "July 2023, Revised August 2025";摘要 "attending an Ivy-Plus college instead of the average flagship public college increases students' chances of reaching the top 1% of the earnings distribution by 50%, nearly doubles their chances of attending an elite graduate school, and almost triples their chances of working at a prestigious firm" 及 "Ivy-Plus colleges (Ivy League, Stanford, MIT, Duke, and Chicago)";导论 p.3 "The impact of Ivy-Plus admission on reaching the top quartile of the distribution is small and statistically insignificant, while the impact on chances of reaching the top 1% far exceed what one would predict based on a constant percentage treatment effect" 与 "increases mean earnings by $101,000 at age 33 (relative to a counterfactual mean of $143,000 if the same students were to attend state flagships)";p.4 "the matriculation design again implies modest impacts of attending an Ivy-Plus college on log earnings, consistent with the findings of Dale and Krueger (2002), whose primary outcome is log earnings... our findings differ from the conclusions of prior studies not because of differences in research design but rather because our richer data allow us to directly identify college's fixed effects... and isolate impacts on upper tail outcomes";§4.1.1 对照组定义原句(9 所)。发表状态经 Oxford Academic 核实:QJE 141(1): 51-145 (https://academic.oup.com/qje/article-abstract/141/1/51/8306880),EconPapers 记 v141 y2026 i1 p51-145。


#### [G44] CORRECTED · confidence=high

**修正**:KLM 本体全部逐字无误,唯一需修的是用来做对比的美国数字。原表述"不是美国的大学溢价(约 +70-80%)" → 正确表述:"不是美国的大学溢价(BLS《Education Pays 2024》口径:本科中位周薪 $1,543 vs 高中 $930,约 +66%)"。+70-80% 高估了通行口径;换成 +66% 后,该条"换了分母"的论证反而更稳(挪威 +26.6% vs 美国 +66%,仍是 2.5 倍差距)。另两处建议补限定语,不影响判决:(a) 43,200/54,700 这组数在原文里是"未完成任何 post-secondary education"对"持 post-secondary degree"、30 岁上的均值,比"大学 vs 不上大学"口径更宽,且与 payoff 的测量时点(申请后第 8 年)并非同一时点;(b) "payoffs rival the college wage premiums" 是摘要措辞,正文对应句为 "For many fields the payoffs rival the usual estimates of college earnings premiums",引用时勿把两者当同一句。数据、识别、结果变量描述(1998-2004 集中申请记录 + 教育登记 + 税务登记、分数线断点 2SLS、次优选择固定、申请后第 8 年年收入、断点附近 compliers 的 LATE)与 0.84 / 0.98 / 43,200 / 54,700 四个数字、"almost triple"、"choosing Science instead of Engineering or Business has little payoff" 均逐字无误;QJE 131(3): 1057-1111, 2016 著录正确。

**核验依据**:NBER WP 20816 PDF (https://www.nber.org/system/files/working_papers/w20816/w20816.pdf) 逐字核对:摘要 "We find that different fields have widely different payoffs, even after accounting for institutional differences and quality of peer groups. For many fields the payoffs rival the college wage premiums, suggesting the choice of field is potentially as important as the decision to enroll in college. The estimated payoffs are consistent with individuals choosing fields in which they have comparative advantage.";导论 "by choosing Science instead of Humanities, individuals almost triple their earnings early in their working career. By comparison, choosing Science instead of Engineering or Business has little payoff.";正文 "The correlation between the estimated payoffs with and without controls for predicted institution is 0.84." 与 "We find a correlation of 0.98 between the estimated payoffs with and without controls for predicted peer quality."(附图注另记 weighted correlation 0.8386 / 0.9805);"individuals who did not complete any post-secondary education were, on average, earning USD 43,200 at age 30, whereas the average earnings of individuals with a post-secondary degree was USD 54,700 at the same age"(复算 54,700/43,200 = +26.6%,与论断一致);数据段 "all applications to post-secondary education for the years 1998 to 2004"、"the Norwegian tax registers over the period 1998 to 2012"、"earnings 8 years after application"。发表著录经 Oxford Academic 核实 QJE 131(3): 1057-1111 (https://academic.oup.com/qje/article-abstract/131/3/1057/2461218)。美国口径经 BLS Education Pays 2024 核实 $1,543 vs $930 = +66% (https://www.bls.gov/careeroutlook/2025/data-on-display/education-pays.htm)。


#### [G45] CORRECTED · confidence=high

**修正**:A/B/C 三组引语与全部数字逐字无误,但"两句相反的话"这个框架本身要改,另有两处口径需补。(1) 原表述"同一份报告里方向相反的话" → 正确表述:"同一份报告里服务于相反修辞用途、但逻辑上并不矛盾的两句话"。A(专业内离散 ≥ 专业间离散)与 B(专业间差距在高分位上扇形张开)可以同时为真,不构成自相矛盾;把它说成"方向相反/互相打脸"会让读者以为报告自我否定。判断中"只引 A 得出选什么专业无所谓、只引 B 得出专业决定一切"这半句成立,予以保留。(2) 原表述把 $720,000 / $1.82M / 154% 当作 A 句"within any given major"的证据 → 正确表述:这三个数原文明写 "For all majors combined",是所有专业合并后的 25/75 分位,同时含专业内与专业间两种离散,并不能单独支撑"任一专业内部"的说法;报告真正的专业内证据是另一句 "Cumulative earnings double—or even triple—when moving from the bottom quarter to the top quarter of earners in a given major."(3) 漏掉的关键口径:全部"生涯累计收入"按 3% 年贴现率折算为现值,报告尾注 ii 逐字 "All cumulative earnings are calculated using a 3 percent annual discount rate. This converts earnings into a 'present value'"。$1.19M/$720,000/$1.82M 都是贴现后现值,不是名义累计额,面向准大学生时这一点必须讲明。(4) 著录小修:Andrews et al. 已正式刊出于 Review of Economics and Statistics(doi 10.1162/rest_a_01503),"NBER WP 30331 / ReStat 2024" 可用。样本描述(仅学士学位未再读研、含兼职者与全年有失业经历者、80 个专业、ACS)与作者自设局限引语均逐字无误。

**核验依据**:Hamilton Project《Major Decisions: What Graduates Earn over Their Lifetimes》PDF (https://www.hamiltonproject.org/assets/legacy/files/downloads_and_links/Major_Decisions_Lifetime__Earnings_by_Major.pdf) 逐字核对:p.4 "In fact, the variation of lifetime earnings within any given major is at least as large as the variation across majors. For all majors combined, lifetime earnings at the 25th percentile—the level at which one-quarter of graduates earn less—are $720,000, but they are $1.82 million at the 75th percentile... This is an increase of 154 percent";p.4 "It is quite apparent that earnings differences across majors grow larger—or fan out—higher up in the earnings distributions. For instance, at the 10th percentile the difference in lifetime earnings between the highest-earning major and the lowest-earning one is about $500,000; at the 90th percentile, this difference is over $3.5 million.";p.1 要点 "Cumulative earnings double—or even triple—when moving from the bottom quarter to the top quarter of earners in a given major. These increases are larger for lower-earning majors.";p.2 样本 "80 majors among workers with exactly a bachelor's degree... do not go on to earn an advanced or professional degree" 与 "not limited to full-time workers and include part-time workers and those who experience unemployment throughout the year";p.1 自设局限 "earnings differences across majors are driven by many factors and do not necessarily reflect a wage premium for that particular major. The estimates cannot distinguish why graduates in certain majors earn more than those in others.";p.6 尾注 ii 贴现率。Andrews/Imberman/Lovenheim/Stange NBER WP 30331 PDF (https://www.nber.org/system/files/working_papers/w30331/w30331.pdf) p.2 逐字 "Quarterly returns (relative to liberal arts) range from $983 in communications to $7,901 in engineering and architecture 16-20 years after high school (inflation adjusted to 2016 dollars)" 与 p.2 "notably fields that tend to have higher mean earnings - generating much larger effects at the top of the distribution. This suggests the mean effects embed substantial (and differential) ex-ante risk for students.";表内 Engineering+Architecture 7,901 与 Communications 983 对得上。发表状态见 MIT Press (https://direct.mit.edu/rest/article-abstract/doi/10.1162/rest_a_01503/124434)。


#### [G46] CORRECTED · confidence=high

**修正**:结论"不存在普遍衰减"成立,予以保留;A/B 全部引语与数字逐字无误(含 "In levels, earnings growth is rapid for all college graduates, regardless of major" 确实存在),Webber"中度收敛"亦经其本人论文原文证实。需修三处:(1) 样本漏了限定语。原表述"数据=2009-2017 ACS,23-50 岁四年制本科毕业生" → 正确表述:"2009-2017 ACS 中 23-50 岁、全职在职(full-time working)的四年制本科毕业生"。图注原文 "all full-time working four-year college graduates aged 23-50 in the 2009-2017 American Community Survey"。这一条在本篇内部很要紧:G45 的 Hamilton Project 明确含兼职与失业期,两者分母不同,不能并排对比。(2) "生命科学/社科扩大"这条腿必须带作者自己的脚注 23,否则被高估。脚注 23 逐字:"The rapid growth in life cycle earnings for life and physical sciences majors is partly due to their very high rate of graduate school attendance. When restricting the ACS sample to respondents with exactly a BA, we find similar results for the other three major groups... but slower growth for life and physical sciences majors." 即该专业的"溢价随生涯扩大"部分是读研构成效应,限定在只有学士学位的人群里会明显减弱。(3) "必须处理的误读"那段只引了半句,建议补全。原文 "In levels, earnings growth is rapid for all college graduates, regardless of major" 之后紧接 "However, while computer science, engineering and business majors are earning substantially more in their mid-twenties than do life/physical sciences and social sciences majors, this advantage is greatly diminished by age 40." 正确表述应是:"绝对收入对所有专业都在快速增长,CS 毕业生中年后收入下滑是错的;但 CS/工程/商科在绝对额上的领先幅度到 40 岁确实被大幅压缩"——只说前半句会矫枉过正。另:12.7 倍在导论写作"over a 10 to 15-year period",正文另一处写作 "in the two decades after high school",两种表述并存,引用需择一并注明。

**核验依据**:Deming & Noray, QJE 135(4):1965-2005 发表版 PDF (https://www.sas.upenn.edu/~vr0j/oldteaching/712tqm-22/DemingNoray_2020.pdf) 逐字核对:p.1989 "computer science and engineering majors earn about 45% more early in their career, but only 33% more by age 50. The earnings advantage for business majors declines from around 38% initially to 20% by age 50. In contrast, the earnings premium grows over time for life and physical sciences and social sciences majors.";p.1990 "In levels, earnings growth is rapid for all college graduates, regardless of major. However, while computer science, engineering and business majors are earning substantially more in their mid-twenties than do life/physical sciences and social sciences majors, this advantage is greatly diminished by age 40.";p.1993 "Declining relative returns is a feature of STEM jobs, not majors. The earnings premium for non-STEM majors in STEM occupations starts off near 40%, but declines to 20% within a decade. In contrast, the relative earnings advantage grows over time for computer science and engineering majors working in non-STEM occupations.";p.1994 "the share of computer science and engineering majors working in computer and engineering occupations declines from 59% at age 26 to 41% by age 50. This decline of 18 percentage points is almost entirely offset by increased employment in non-STEM management occupations.";脚注 23 全文;图注样本 "full-time working"。Andrews et al. NBER WP 30331 PDF p.2 "The returns to biology and health grow the most over time, increasing by a factor of 12.7 (from $413 to $5,655) over a 10 to 15-year period.",表中 Biology+Health 行 413 / 2,718 / 5,655 对得上;该文同页显示四年制各领域回报多数随生涯上升(物理科学/数学与传播 >400%,商经/职教/工程建筑 100-200%),构成对"普遍衰减"的直接反证。Webber《The Lifetime Earnings Premia of Different Majors》作者主页 PDF (http://www.doug-webber.com/LE%20paper.pdf) 逐字 "I find that there has been a moderate convergence over time in the return to the various major categories" 及正文 "a moderate convergence in the lifetime earnings premia (both unadjusted and selection-corrected) across majors over time"。


#### [G47] CORRECTED · confidence=high

**修正**:三套口径的全部数字逐字/逐格无误,百分比经我独立复算全部对得上(NSCG 2019:27,340/50,524=54.11%、13,258/50,524=26.24%、9,927/50,524=19.65%;仅本科 13,818/31,373=44.04%、9,508/31,373=30.31%、8,048/31,373=25.65%)。需修四处:(1) 最重要:官方口径已过期两轮。原表述"NSF NCSES《National Survey of College Graduates: 2019》Table 1-3" → 正确表述:应改用 NSCG 2023(NSF 25-322,2025-01-13 发布,参考周为 2023-02-01)。2023 年 Table 1-3 同格数字:全体大学以上在职者 56,061,000,closely 30,129,000=53.7% / somewhat 15,217,000=27.1% / not related 10,715,000=19.1%;仅本科为最高学历者 34,311,000,closely 14,948,000=43.6% / somewhat 10,669,000=31.1% / not related 8,694,000=25.3%。(中间还有 NSCG 2021 / NSF 23-306。)方向与量级没变,但面向 2026 年读者引 2019 年数据且不注明已有两轮更新,是可避免的口径瑕疵。(2) EdWorkingPaper 23-760 题名引错。原表述"《The Increasing Penalty to Occupation-Major Mismatch》" → 正确表述:"Cassidy & Gaulke,《The Increasing Penalty to Occupation-**Education** Mismatch》,EdWorkingPaper 23-760, 2023 年 4 月"。是 Education 不是 Major,一词之差改变了错配的定义口径。该文结论成立:用 NSCG,1993-2019 年间错配率仅由 19% 微降至 17%,而错配的工资惩罚上升 51%——确实可用来反驳"专业不重要反正都要转行"。(3) "+25% 与 +5%"这条被抬得过高,须补三个限定语。原表述"'有没有学历门槛'比'对不对口'重要 5 倍" → 正确表述:"在同一个横截面工资回归里,学历门槛匹配的系数(0.244 对数点,严格换算 +27.6%,作者自己写成 almost 25 percent)约为专业对口系数(0.054,+5.5%)的 4.5 倍"。三个限定语:(a) 这是 2010 年 ACS 横截面的描述性 OLS,不是因果估计,论文主题是集聚经济与城市工资溢价,匹配变量只是其中的控制项,自选择未处理;(b) 该回归样本剔除了研究生学历者(N=162,454),且控制了 171 个专业固定效应,所以 +5% 是专业内估计;(c) 两个系数出自同一个回归(Table 4 第 (2)(4) 列),这一点是好的,五倍比较在算术上站得住,但"5 倍"宜写"约 4.5-5 倍"。(4) "College Degree Match 约 62-67%"是把两个不同量并成了一个区间:62% 是回归样本均值("the average College Degree Match rate of 62 percent"),约三分之二是描述性表述("about two-thirds of all college graduates are working in a job that requires a Bachelor's degree")。另 Abel-Deitz 用 2010 年 ACS、已 16 年,确无同口径更新版,现有最接近的更新证据即上述 Cassidy-Gaulke。Census 2019 ACS 六个专业比例与 $101,100 vs $87,600 逐字无误。

**核验依据**:NSCG 2019 一手数据表 NSF 22-310 Table 1-3 PDF (https://ncses.nsf.gov/pubs/nsf22310/assets/data-tables/tables/nsf22310-tab001-003.pdf):"All degrees 50,524,000 / 27,340,000 / 13,258,000 / 9,927,000";"Bachelor's 31,373,000 / 13,818,000 / 9,508,000 / 8,048,000";六个百分比经我用原始计数复算,与论断完全一致。NSCG 2023 一手数据表 NSF 25-322 Table 1-3 PDF (https://ncses.nsf.gov/pubs/nsf25322/assets/data-tables/tables/nsf25322-tab001-003.pdf) 标题 "...: 2023","All degrees 56,061,000 / 30,129,000 / 15,217,000 / 10,715,000","Bachelor's 34,311,000 / 14,948,000 / 10,669,000 / 8,694,000";NSCG 2021 表见 NSF 23-306 PDF (https://ncses.nsf.gov/pubs/nsf23306/assets/nsf23306.pdf) Table 1-3:"All degrees 51,764,000 / 28,026,000 / 13,514,000 / 10,224,000";最新周期与发布日期见 NCSES 调查页 (https://ncses.nsf.gov/surveys/national-survey-college-graduates/)。NY Fed Staff Report No. 587 PDF (https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr587.pdf,2012 年 12 月、2014 年 12 月修订,数据为 2010 ACS) 逐字:p.7 "We find that about 27 percent of undergraduate degree holders are working in a job that is directly related to their college major." 与 "about 73 percent of these majors work in jobs that require a college degree, while 33 percent work in jobs directly related to their major"、"80 percent of those with a Computer Engineering degree but only 44 percent of those with a Studio Arts degree";p.24 "college graduates working in a job that requires a college degree earn, on average, almost 25 percent more than those who do not match along this dimension... those college graduates who work in a job closely related to their college degree major earn, on average, an additional 5 percent more than those who do not, which in principle is on top of the wage premium for a College Degree Match";Table 4 系数 0.244 (0.011) 与 0.054 (0.005),表注 "Models also include... individual's major (171 degree fields)... Individuals with graduate degrees are excluded from the analysis.",N=162,454。Census 报道 (https://www.census.gov/library/stories/2021/06/does-majoring-in-stem-lead-to-stem-job-after-graduation.html,2021-06-02 发布,2019 ACS):工程 52%、计算机/数学/统计 51%、物理科学 28%、生物/环境/农业 16%、心理 10%、社科 9%,及 "STEM workers who majored in a STEM field in college typically made higher salaries than those who did not: on average, $101,100 vs. $87,600"。EdWorkingPaper 23-760 PDF (https://edworkingpapers.com/sites/default/files/ai23-760.pdf) 封面题名 "The Increasing Penalty to Occupation-Education Mismatch",Hugh Cassidy & Amanda Gaulke,2023 年 4 月,摘要 "although the rate of this mismatch declined only slightly (19% to 17%), the wage penalty increased by 51% between 1993 and 2019",doi 10.26300/stdh-s857。


## 批次 H1 — verify:中国官方口径


### 第 1 席


#### [G48] CORRECTED · confidence=medium

**修正**:（1）绝对表述站不住。原表述：「中国**没有**官方的『分专业毕业生失业率』『分专业起薪』『分专业学历错配率』任何一项」「中国没有任何官方的分专业就业数据」→ 正确表述：「中国没有**公开发布的、全国性、可比、连续**的分专业就业率／起薪／错配率统计；分专业就业数据在体制内确实存在并被用于行政处置，但不对外发布。」反证三条：①教育部2014-10-14通过『微言教育』公开发布《近两年（2012、2013）就业率较低的本科专业名单》，含全国15种专业及分省名单——这是官方、分专业、基于就业率的公开数据（虽为名单非费率）；②《普通高等教育学科专业设置调整优化改革方案》（教育部等五部门2023）逐字规定「对办学条件严重不足、教学质量低下、**就业率过低**的，要责令暂停招生、限期整改」——说明省级教育行政部门掌握并使用分专业就业率；③教育部2026-04-28逐字：各省份已发布「覆盖473种专业的急需专业清单和专业预警清单」，是官方分专业预警。
（2）公式引文已过期。原表述把「毕业去向落实率=协议和合同就业率+创业率+灵活就业率+升学率」（教学厅函〔2021〕19号附件1，逐字无误）当作现行口径 → 正确表述：该式为2021版；教育部发展规划司《中国教育监测与评价统计指标体系（2025年版）》第29页逐字改依《教育部办公厅关于进一步做好普通高等学校毕业生就业监测工作的通知》（**教就业厅函〔2024〕11号**），现行式为「毕业去向落实率=**单位就业率+自主创业率+自由职业率+升学率**」，「协议和合同就业率」「灵活就业率」两个术语已不在公式中。引用时须标注版本年份。
（3）美方举证过宽。原表述「美方（NY Fed / **BLS** / ACS）有分专业微观数据」→ 正确表述：分专业（field of degree）微观数据来自 Census Bureau 的 ACS（2009年起设该题），NY Fed 的 Labor Market for Recent College Graduates 由 ACS 微观数据加工而来；**BLS 不发布分专业失业率**（BLS 是分职业/分行业）。删去 BLS 或改为「Census/ACS + NY Fed」。
（4）可加固的正面证据（原文未用，建议补入）：《中国教育监测与评价统计指标体系（2025年版）》全108页中，「毕业生毕业去向落实率」的『指标分解』逐字为「**分层次；分就业形式；分办别**」——官方指标体系里该指标压根没有『分专业』这一维；全书所有指标的最细学科维度只到「分学科领域」（门类级），无一条『分专业』。同页官方自述局限性：「毕业去向落实率……**不能完全反映毕业生人岗匹配的实际情况**、毕业生长期发展情况等」——这是官方承认无 underemployment 指标的最好一手依据。

**核验依据**:①教学厅函〔2021〕19号原件PDF（湖南省教育厅转发，逐页图像核对）：https://jyt.hunan.gov.cn/jyt/sjyt/bys/tzgg_1/202105/16548110/files/d1856b6e22214d6abd4256691c63fd34.pdf 第5页附件1表格右栏逐字「毕业去向落实率=协议和合同就业率+创业率+灵活就业率+升学率」，各分率分母均为「毕业生总数」；正文第1页逐字「为更加准确反映高校毕业生升学、就业等毕业去向情况，从2021届起，将『就业率』改为『毕业去向落实率』」。②教育部发展规划司《中国教育监测与评价统计指标体系（2025年版）》PDF（108页，指标36，第29–30页）：https://zpb.slu.edu.cn/_upload/article/files/0a/7c/b69716df4a52a2fe4553666aedf2/7ac328df-ad66-4108-96bd-2e9d72af0b42.pdf ——逐字引「教就业厅函〔2024〕11号」，新公式「单位就业率+自主创业率+自由职业率+升学率」；指标分解「分层次；分就业形式；分办别」；全书指标分解字段经全文正则统计，无一处出现「专业」。③教育部2014-10-14《教育部公布就业率较低本科专业名单》：http://www.moe.gov.cn/jyb_xwfb/s5147/201410/t20141015_175978.html ④教高〔2023〕1号《普通高等教育学科专业设置调整优化改革方案》全文（连云港师专高教所镜像，教育部原页 http://www.moe.gov.cn/srcsite/A08/s7056/202304/t20230404_1054230.html ）：https://gdjyyjs.jou.edu.cn/info/1019/4256.htm ⑤教育部2026-04-28《〈普通高等学校本科专业目录（2026年）〉发布》原页（curl直取全文）：http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202604/t20260428_1435016.html


#### [G49] CORRECTED · confidence=high

**修正**:三段引文与2021年原件**逐字完全一致**（我逐页比对了PDF图像，标点、编码、审核依据一字不差），配套的「灵活就业=其他录用形式就业（编码12）+自由职业（编码76）」也与附件1表格一致，「数据发布管制」两句亦逐字无误。需要修正的是**时效与表述精度**：
（1）原表述把教学厅函〔2021〕19号附件2当作**现行**标准 → 正确表述：附件2的「毕业去向界定及标准」已被《教育部办公厅关于进一步做好普通高等学校毕业生就业监测工作的通知》（**教就业厅函〔2024〕11号**）取代。一手佐证：湖南农业大学2025-07-04《关于开展2025届毕业生就业监测数据自查工作的通知》逐字要求「是否按照《关于进一步做好普通高等学校毕业生就业监测工作的通知》（**教就业厅函〔2024〕11号**）要求的毕业去向分类、界定和审核依据严格审核材料」；教育部发展规划司2025年版指标体系亦改引该文号。文章须写成「2021年版规定……（该文2024年由教就业厅函〔2024〕11号接续修订）」。
（2）原表述「官方『就业』的下限 = **月入**达当地最低工资 + 一张本人签字的说明」→ 正确表述：文件只写「薪酬需达到当地最低工资标准」，未限定为月薪；附件2说明1逐字「当地最低工资标准参见人社部公布的《全国各地区最低工资标准情况》」，该表同时含**月最低工资标准与小时最低工资标准**。且「一张本人签字的说明」只适用于**自由职业（编码76）**；**其他录用形式就业（编码12）**仍需「用人单位出具的聘用证明或毕业生本人提供的工资收入证明、收入流水等」。应拆开写，勿合并。
（3）「四不准」已被扩充。2021年原件只有「四不准」；2025年在执行的还有「**三不得**」——「不得不切实际向高校或院系提去向落实率具体指标；不得层层加码向辅导员摊派就业任务；不得将单一的去向落实率指标与就业工作人员或者辅导员的绩效考核、评优等挂钩」。这条对文章有利（说明主管部门自己承认存在指标摊派的注水压力），建议补入。
（4）建议补入的注水监测项（同一份湖南农大文件逐字）：教育部/省校反馈的「疑似虚假就业数据」监测口径包括「对**灵活就业率、自由职业率和自主创业率过高，其他录用形式占比过高**，疑似小企业扎堆就业」——即主管部门自己把这三类高占比列为造假嫌疑信号，这是比推理更硬的证据。

**核验依据**:①一手PDF逐页图像比对：https://jyt.hunan.gov.cn/jyt/sjyt/bys/tzgg_1/202105/16548110/files/d1856b6e22214d6abd4256691c63fd34.pdf ——第7页（附件2）「7.其他录用形式就业（编码12）」分类界定与审核依据、第8页「8.自主创业（编码75）（3）电子商务创业……依据网店网址、网店信息截图和收入流水」「9.自由职业（编码76）……互联网营销工作者、全媒体运营工作者、电子竞技工作者等／依据毕业生本人签字确认的证明材料，由校、院两级就业部门负责同志审定，薪酬需达到当地最低工资标准」、第9页说明1（最低工资标准出处）、第2页正文第三条「各省级就业工作部门在对外公开本省毕业生毕业去向落实率之前，须与教育部高校学生司核实数据，未经核实不得擅自公开。各高校未经省级就业工作部门同意，不得向其他部门、机构等提供本校就业数据。」——全部逐字命中。②湖南农业大学2025-07-04通知PDF（提取全文）：https://jc.hunau.edu.cn/tzgg/202511/P020251106552975382670.pdf ——含教就业厅函〔2024〕11号引用、「三不得」全文、疑似虚假就业数据监测口径。③《中国教育监测与评价统计指标体系（2025年版）》第29页。


#### [G50] CORRECTED · confidence=high

**修正**:所有数字均已核实为真：2023年6月旧口径16—24岁城镇调查失业率21.3%（2023-07-17发布，2018年有统计以来最高，2023-08-15宣布暂停发布）；2023年12月新口径首月14.9%；2026年6月14.9%、5月15.6%、4月16.3%、3月16.9%，25—29岁7.1%、30—59岁4.0%（6月环比分别−0.7／−0.1／−0.1个百分点）。「未公布重叠期双算数据」经核实**属实**——《关于完善分年龄组调查失业率有关情况的说明》全文无任何新旧口径并列或换算。三处需修正／补强：
（1）**最严重的遗漏**。原表述只列「2026年6月14.9%（5月15.6%、4月16.3%、3月16.9%）」，读起来是单向改善 → 必须补：**2025年6月同口径为14.5%，2026年6月的14.9%高于上年同期0.4个百分点**。「连续三个月下降」是每年3→6月的季节性形状（2025年同样是「连续4个月下降」到6月的14.5%），**同比方向是上升**。面向准大学生只给环比不给同比，会造成实质误导。
（2）出处标注。原表述暗示这些月度数字应能在 stats.gov.cn 新闻稿页找到 → 正确表述：统计局**不以新闻稿形式**发布该系列；《说明》末段逐字「今后我局将按月在『国家统计局数据发布库』中发布不包含在校学生的16—24岁、25—29岁、30—59岁劳动力失业率」。正确引法是标注「国家统计局数据发布库（data.stats.gov.cn），按月」。我尝试直取 data.stats.gov.cn／easyquery 均返回403，四个月度值系由财新、澎湃、观察者网等多家独立转述交叉一致确认，**未能落到数据库原页**，文章应据实说明这一取证限制。
（3）逐字顺序。原表述把《说明》拆成两句并调序 → 原文为一句连读：「**在校学生的主要任务是学习，而不是兼职工作**，如果把在校学生包含在分年龄组内，会把在校寻找兼职和毕业后寻找工作的青年混在一起……」引用时勿倒装。
（4）建议补入（原文未用的官方数字）：《说明》给出2023年各月平均，16—24岁城镇人口中在校学生约**6200万**（占六成多）、非在校学生约**3400万**（占三成多）。这是官方唯一可用来粗估「排除在校生」量级的数字，虽不能反推失业率落差，但能让读者理解分母被砍掉了多大一块。
（5）ILO 1小时标准的表述可保留，但应加限定：中国调查失业率对「就业」采用参考周内工作1小时以上的国际劳工组织标准，与美方 CPS 同源，因此**这一条不构成中美不可比的理由**；不可比出在分专业维度和分子构念，不在1小时标准。

**核验依据**:①国家统计局《关于完善分年龄组调查失业率有关情况的说明》（2024-01-17）原页逐字核对，含排除在校生理由、25—29岁组理由、6200万/3400万人口构成、末段「按月在『国家统计局数据发布库』中发布」；经二次定向提问确认全文**无**2023年12月具体数值、**无**新旧口径并列数据、**无**21.3%或暂停发布的说明：https://www.stats.gov.cn/sj/zxfb/202401/t20240117_1946641.html ②2026年6月：财新2026-07-20「6月不含在校生青年失业率降至14.9% 高于上年同期」https://economy.caixin.com/2026-07-20/102466293.html （明确「较上年同期有所上升」）；观察者网 https://www.guancha.cn/politics/2026_07_20_824452.shtml ③2026年3月16.9%：财新 https://economy.caixin.com/2026-04-21/102436199.html ④2026年4月16.3%（25–29岁7.4%、30–59岁4.2%）：澎湃 https://m.thepaper.cn/newsDetail_forward_33205433 ⑤2025年6月14.5%：https://m.voc.com.cn/xhn/news/202507/29971057.html ⑥data.stats.gov.cn easyquery 接口返回HTTP 403，数据库原页未能直取。


#### [G51] CORRECTED · confidence=high

**修正**:**标题数字错了。** 原表述「非私营 vs 私营**差 1.94 倍**」→ 正确表述：**1.81 倍**。129,441 ÷ 71,590 = **1.808**。这与同一条论断自己写的「私营不足非私营的56%」自相矛盾（71,590/129,441 = **55.3%**，其倒数正是1.81，不可能是1.94）。1.94 这个数在2025年数据里没有任何对应来源，须整条替换为「非私营是私营的 1.81 倍，私营仅为非私营的 55.3%」。
其余逐格核对**全部命中**，无第二处错误：非私营全国129,441元（名义增长4.3%，实际4.2%）；信息传输、软件和信息技术服务业248,752（+4.1%，非私营口径居首）；金融业211,164（+4.6%）；科研技术服务182,064（+3.8%）；卫生和社会工作146,266（+2.2%）；教育133,539（+5.8%）；制造业113,594（+5.2%）；住宿餐饮62,461（+3.7%）。私营全国71,590元（名义增长3.0%，实际2.9%）；金融业140,451（+3.8%）确实反超信息传输业128,166（+4.0%）；制造业76,055（+6.4%）；教育63,908；卫生和社会工作75,631（+0.5%）；住宿餐饮55,123（+2.0%）。
采集者标注的增速矛盾已解决：**私营口径教育业为 +5.3%，不是 +3.3%**，原文即5.3%，论断正文写的「教育（+5.3%/+5.8%）」是对的，采集备注里的3.3%是笔误，删掉即可。
79% 复算无误：128,166 ÷ 71,590 = 1.790，即私营IT高出私营总平均 **79.0%**。
四条口径中三条逐字命中，一条需改：(a) 逐字为「工资总额是税前工资，包括单位从个人工资中直接为其代扣或代缴的个人所得税、社会保险基金和住房公积金等个人缴纳部分**以及房费、水电费等**」——论断的引文在「个人缴纳部分」处截断，漏了尾巴，补全或加省略号。(b) 逐字「城镇单位指城镇地域内就业人数在5人及以上的法人单位，2025年纳入统计的单位共计306.2万家」✓，不含个体工商户和自由职业者 ✓。(c) 「国家统计局不公布分行业工资中位数」✓——该发布页通篇无中位数；但表述宜精确为：统计局公布的**平均工资**定义逐字为「就业人员平均工资 = 就业人员工资总额 / 就业人员平均人数」，是加权算术平均；发布页并未自称「算术平均」，这四个字是文章的解读而非官方原话，需改成「按此定义即为算术平均值」。另需提醒读者：统计局确实公布**居民人均可支配收入中位数**，只是不公布**分行业工资中位数**，别把两者混为一谈。(d) ✓ 全部在岗人员平均，发布页无任何应届生起薪数据。
「IT不赚钱了在统计局口径上不成立」的推论成立且可承重；「溢价在缩窄而非消失」的增速比较（IT私营+4.0%／非私营+4.1% vs 制造业+6.4%/+5.2%、教育+5.3%/+5.8%）四个数全部核实无误。

**核验依据**:国家统计局《2025年城镇单位就业人员年平均工资情况》（2026-05-15）原页，两次定向抓取逐格核对全部19个行业门类×2套口径、规模以上企业分岗位工资、附注全文：https://www.stats.gov.cn/sj/zxfb/202605/t20260515_1963707.html 。附注逐字：「工资总额是税前工资，包括单位从个人工资中直接为其代扣或代缴的个人所得税、社会保险基金和住房公积金等个人缴纳部分以及房费、水电费等」；「城镇单位指城镇地域内就业人数在5人及以上的法人单位，2025年纳入统计的单位共计306.2万家」；「平均工资：是指在报告期内单位发放工资的人均水平。计算公式为：就业人员平均工资 = 就业人员工资总额 / 就业人员平均人数」。页面无「中位数」字样。比值均为本人手算：129441/71590=1.8081；71590/129441=0.5531；128166/71590=1.7902。


#### [G52] CORRECTED · confidence=high

**修正**:数字部分全部命中，两处推论必须改写，其中一处是**方向性错误**。
（1）**最重要的一处，判为错误**。原表述「教育部相关政策文件**通篇未把『就业率』列为撤销的明示标准**，因此『撤销多=这个专业没前途』是媒体与考生的推断，不是官方论断」→ 正确表述：《普通高等教育学科专业设置调整优化改革方案》（教育部等五部门，教高〔2023〕1号）**逐字**规定「省级教育行政部门要定期开展学科专业建设质量检查，对办学条件严重不足、教学质量低下、**就业率过低**的，要**责令暂停招生、限期整改**」；同一份文件另有「对高校**连续五年未招生**的专业予以撤销处理」。两句合起来构成一条官方明示链条：**就业率过低 → 责令停招 → 连续五年未招生 → 撤销**。此外该方案还要求「国务院有关行业部门要主动开展行业人才需求预测、**毕业生就业反馈预警**及人才使用情况评价」「建立健全**招生培养就业联动机制**」；教育部2025-04-22新闻稿结尾亦逐字「教育部将进一步强化**专业设置与就业工作的联动**」。所以应改为：「就业率过低是官方明示的**停招**触发条件（撤销的明示条件是连续五年未招生），因此『停招/撤销与就业有关』并非纯媒体推断；但官方从不公布某专业的就业率数值，也未把就业率列为**唯一或首要**标准，读者无法据此反推某个专业的具体就业水平。」这一改动同时反向加固了 G48——分专业就业率在体制内存在且被用于行政处置，只是不公开。
（2）原表述「专业类减少1、专业种数增加38，**说明发生了合并重组，不能读作『净增38种全新专业』**」→ 前半对、后半错。845 + 38 = **883**，分毫不差，说明本轮**专业种数确实是净增38种、无一种被删**，38种都是新专业种。真正的合并重组体现在**门类与专业类结构**上：门类 12 → **13**（首增交叉学科门类），专业类 93 → **92**（减1），并有「未来机器人、交叉工程等**11种目录内已有专业**」被**迁入**交叉学科门类（这11种是搬家不是新增，交叉学科门类首批15种 = 11种已有 + 4种新专业）。改写为：「专业种数是干净的净增38种；被重组的是门类和专业类的框架——12门类93专业类 → 13门类92专业类，11种既有专业整体迁入新设的交叉学科门类。」另需一句限定：交叉学科门类是**本科专业目录**首次增设，研究生教育学科专业目录早在2021年就已设『交叉学科』门类，教育部2026-04-28原文的表述正是「推动本科专业目录与研究生教育学科专业目录有机衔接、上下贯通」。
（3）引语归属需改。原表述把「**撤销、停招专业点数大幅超过增设专业点数，专业结构不断优化**」标为教育部逐字 → 教育部2025-04-22新闻稿正文的对应句是「**专业调整优化力度进一步加大**」；「撤销、停招……大幅超过增设」这一说法出自答记者问／媒体标题（新京报），不宜标成新闻稿逐字。第一句「全国高校共新增专业点1839个，调整学位授予门类或修业年限专业点157个，停招专业点2220个，撤销专业点1428个」**是**新闻稿逐字，可放心用。
（4）以下逐字/逐数全部核实无误，可承重：1839／157／2220／1428；全国本科专业布点共 **6.28万个**（教育部2025-04-22原文末段）；2025年目录 **93个专业类、845种专业**、增列29种（教育部2025-04-22原文）；2026年目录 **13个门类、92个专业类、883种专业**、交叉学科门类首批「未来机器人、交叉工程等11种目录内已有专业和具身智能、脑机科学与技术等4种本次列入目录的新专业」（教育部2026-04-28原文逐字）；「十四五」期间「新增本科专业布点**1.02万个**、撤销或停招**1.22万个**……累计调整比例**超30%**，今年全国高校专业调整比例**首次突破10%**」（教育部2026-04-28原文逐字）；毕业生规模 2021届909万 → 2024届1179万 → 2025届1222万 → 2026届预计**1270万**（同比增48万，1270−48=1222自洽）；「全国目录里总共才883种专业」用于反衬「3648个专业被砍」的媒体误读，成立。

**核验依据**:①教育部2025-04-22《教育部公布2024年度本科专业备案和审批结果并更新发布本科专业目录》原页，用curl直取并剥标签得全文（WebFetch 因 http/https 302 循环失败）：http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202504/t20250422_1188245.html ——含1839/157/2220/1428、「新目录包含93个专业类、845种专业」「目前全国高校本科专业布点共有6.28万个」「进一步强化专业设置与就业工作的联动」。②教育部2026-04-28《〈普通高等学校本科专业目录（2026年）〉发布》原页，curl直取全文：http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202604/t20260428_1435016.html ——含13门类/92专业类/883种、11+4、十四五1.02万/1.22万/超30%/首次突破10%、各省「覆盖473种专业的急需专业清单和专业预警清单」。③教高〔2023〕1号全文（教育部原页 http://www.moe.gov.cn/srcsite/A08/s7056/202304/t20230404_1054230.html ，实取自连云港师专高教所镜像）：https://gdjyyjs.jou.edu.cn/info/1019/4256.htm ——「就业率过低的，要责令暂停招生、限期整改」「对高校连续五年未招生的专业予以撤销处理」「毕业生就业反馈预警」「到2025年，优化调整高校20%左右学科专业布点」。④教育部高教司答记者问：https://www.gov.cn/zhengce/202504/content_7020385.htm ⑤2026届1270万（同比增48万）：新华网 https://www.news.cn/20251120/ead0f25dff2948dfa7f01fa78f207882/c.html


#### [G53] CORRECTED · confidence=high

**修正**:两处必须推翻，一处口径需软化，其余核实无误。
（1）**「首次跌破350万」是错的。** 原表述「2026年……**并首次跌破350万**」→ 正确表述：**2020年考研报名341万，早已低于350万**；2019年290万，此前各年更低。343万只是**2021年（377万）以来首次回到350万以下**，也是**2020年以来的最低值**。完整序列应写全：2019年290万 → 2020年341万 → 2021年377万 → 2022年457万 → 2023年474万（峰值）→ 2024年438万 → 2025年388万 → 2026年343万。用「首次」二字会让考生误以为出现了历史性拐点。
（2）**「招录计划本身也在扩张」是错的，且方向相反。** 原表述「国考『创新高』中……**招录计划本身也在扩张**」→ 正确表述：2026年度国考计划招录 **3.81万人，较2025年度的3.97万人减少1602人，是2019年以来首次缩招**。也就是说 98:1 这个竞争比同时来自**分子上升（341.6万→371.8万，+8.8%）和分母收缩（3.97万→3.81万）**——两头夹击，而不是文章说的「分母也在扩张」。这一改动实际**加强**了文章的论点，务必改过来。可补：2025年度竞争比约 **86:1**（341.6/3.97），2026年度约 **98:1**（371.8/3.81），复算均吻合。
（3）口径表述需软化。原表述「口径=**网上报名并缴费确认人数**」→ 教育部原文只写「据统计，2026年全国硕士研究生招生考试报名人数为343万」，**未定义**是否为缴费确认口径。应改为「教育部仅公布『报名人数』一个数，未说明是否为缴费确认口径，亦不公布应届/往届拆分，更非实际参考或录取人数」。「不公布应届/往届拆分」经核实属实（教育部通稿全文仅此一数）。
（4）「2026年度国考放宽报考年龄上限」**属实且可写具体**：一般职位年龄上限由35周岁放宽至**38周岁**（1986年10月至2007年10月出生），2026年应届硕士、博士研究生由40周岁放宽至**43周岁**（1981年10月以后出生）；官方给出的理由是「按照实施渐进式延迟法定退休年龄有关政策要求，对公务员招录年龄条件作了适当放宽调整」。文章说「会机械性推高报名基数」是合理推论，且「官方未拆分其中多少来自年龄放宽」属实，保留。
（5）新华社定性需改。原表述称《报考回归理性 发展路径多元》（新华社2025-11-24）是「**官方解读框架**」→ 正确表述：该文副题即「**专家分析**2026年考研报名人数」，通篇引述的是厦门大学教育研究院副院长王树涛、华中师范大学胡向东等**学者**观点，不是教育部的官方口径。教育部当天的通稿（《教育部部署2026年全国硕士研究生招生考试安全工作》）只给数字、**不作任何解读**。改成「新华社约请专家给出的解读框架」更准确，同时这反而强化了文章「两种解释都无法证伪」的立论。
（6）以下核实无误：343万（教育部原文逐字）；较388万减45万、−11.6%（45/388=11.60%）；自2024年起连续第三年下降；371.8万通过资格审查、约98:1、较2025年度341.6万增加30余万（371.8−341.6=30.2万）、刷新历史新高；「过审人数≠报名人数≠实际参考人数」「98:1是过审比不是录取率」的口径提醒完全正确；「考研343万（报名数）与国考371.8万（过审数）口径不同不能并列比较」正确；「考研降−11.6%与国考升+8.8%同时发生，否定『青年整体退出竞争』」的推论成立。

**核验依据**:①教育部原页（curl直取全文，末段逐字「据统计，2026年全国硕士研究生招生考试报名人数为343万。」）：http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/moe_1485/202511/t20251124_1421370.html ②新华网2025-11-24《报考回归理性 发展路径多元——专家分析2026年考研报名人数》：http://www.news.cn/20251124/e54d3157f15744f5beb5b76644035f5d/c.html （标题含「专家分析」，引述王树涛、胡向东）③国考3.81万招录、371.8万过审、98:1、较2025年度减少1602人为2019年以来首次缩招、2025年度3.97万/341.6万/86:1：北京日报 https://news.bjd.com.cn/2025/10/15/11352154.shtml ；新京报 https://m.bjnews.com.cn/detail/1761479397168803.html ；新浪财经 https://finance.sina.com.cn/jjxw/2025-10-26/doc-infvfpzi6004563.shtml ；央视网《招录年龄放宽！2026年国考报名人数创新高》 https://edu.cctv.com/2025/10/27/ARTIjpBHmnytUTCFm5ip7xqd251027.shtml ④年龄放宽至38/43周岁及「渐进式延迟法定退休年龄」理由：北京市政府门户 https://www.beijing.gov.cn/fuwu/bmfw/sy/jrts/202510/t20251015_4224547.html ；2026年度国考报考指南（国家公务员局/学信网专题） https://www.ncss.cn/ncss/zt/2026gk.shtml ⑤2020年考研341万（低于350万）：历年考研报名人数统计 https://www.dxsbb.com/news/124228.html ，与「2020年考研报名人数首次突破300万」的公开表述一致。


### 第 2 席


#### [G48] CORRECTED · confidence=high

**修正**:原表述:「中国**没有**官方的『分专业毕业生失业率』『分专业起薪』『分专业学历错配率』任何一项」「中美分专业就业对比在数据上根本无法对称完成」→ 正确表述:「中国**没有全国性、可与 NY Fed/ACS 微观数据对称**的分专业就业指标:无分专业失业率、无分专业起薪、无分专业学历错配率(这三项经穷尽搜索确实未见任何官方发布)。但『没有任何官方分专业就业数据』是过强的表述——省级教育行政部门与各高校确有公开的**分学科门类/分专业毕业去向落实率**:湖南省教育厅《关于全省普通高等学校2020届毕业生初次就业情况的通报》第六节『按学科专业大类划分就业情况』逐字给出本科分学科门类就业率(历史学84.78%、工学83.02%、教育学83.02%)与高职专业大类就业率;安徽省教育厅《普通高校本科专业布局和需求分析报告(2023)》公布毕业去向落实率相对较低的21个专业;江西以落实率低于50%亮黄牌、连续2年低于50%亮红牌责令停招,四川设连续2年/3年低于50%的黄牌/红牌;教育部《关于做好2024届全国普通高校毕业生就业创业工作的通知》第23条逐字『持续实施高校毕业生就业去向落实率红黄牌提示制度』;教育部2026-04-28发布逐字『推动各省份发布覆盖473种专业的急需专业清单和专业预警清单』;各高校依教育部要求年度发布的《毕业生就业质量报告》普遍含分专业落实率。因此正确说法应为:『官方分专业数据存在,但口径是落实率而非失业率、层级是省/校而非全国、发布不连续不可汇总,且受教学厅函〔2021〕19号发布管制约束——所以中美对比仍无法对称完成』。」另,配套论断(落实率与 NY Fed unemployment rate 是不同构念、中国无对应 underemployment 的官方指标)与两处逐字公式**完全无误**,不需修改。

**核验依据**:一手 PDF(教学厅函〔2021〕19号,湖南省教育厅转发件 https://jyt.hunan.gov.cn/jyt/sjyt/bys/tzgg_1/202105/16548110/files/d1856b6e22214d6abd4256691c63fd34.pdf)经 pdftotext 全文提取,附件1表格逐字为『毕业去向落实率=协议和合同就业率+创业率+灵活就业率+升学率』,四个分率逐字分别为『协议和合同就业率=协议和合同就业数/毕业生总数』『创业率=自主创业数/毕业生总数』『灵活就业率=灵活就业数/毕业生总数』『升学率=升学数/毕业生总数』,分母统一无误;正文第一条逐字『为更加准确反映高校毕业生升学、就业等毕业去向情况，从 2021 届起，将“就业率”改为“毕业去向落实率”。』——与论断逐字一致。反证来源(均为一手政府网页):湖南省教育厅通报原文 http://jyt.hunan.gov.cn/sjyt/bys/tzgg_1/202104/t20210427_16516285.html(含分学科门类就业率);教育部2023-12-05通知原文 http://www.moe.gov.cn/srcsite/A15/s3265/202312/t20231205_1093196.html(红黄牌提示制度);教育部2026-04-28发布(CERNET镜像 https://www.edu.cn/ke_yan_yu_fa_zhan/gao_xiao_cheng_guo/gao_xiao_zi_xun/202604/t20260428_2731285.shtml,专业预警清单)。另核《中国劳动统计年鉴》目录(13部分,含就业与失业、分单位类型工资)确无分专业维度,国家统计局2025年工资发布亦仅到分行业——该部分论断成立。


#### [G49] CORRECTED · confidence=high

**修正**:三段附件2逐字引用与『数据发布管制』段落**逐字无误**(已与 PDF 原件字符级比对),『灵活就业=其他录用形式就业(编码12)+自由职业(编码76)』亦由附件1表格逐字证实。需修正两处推论与补一处限定:(1)原表述:「官方『就业』的下限 = 月入达当地最低工资 + 一张本人签字的说明。开网店、做电竞、当博主均计入落实率」→ 正确表述:「『薪酬需达到当地最低工资标准』只适用于**三类**——附件2说明第1条逐字:『“科研助理、管理助理”“其他录用形式就业”“自由职业”中当地最低工资标准参见人社部公布的《全国各地区最低工资标准情况》』;**自主创业(编码75)不设最低工资门槛**,电商创业的审核依据逐字仅为『依据网店网址、网店信息截图和收入流水』。因此『开网店』计入落实率属实,但不需达到最低工资。」(2)原表述:「+ 一张本人签字的说明」→ 正确表述:「『依据毕业生本人签字确认的证明材料，由校、院两级就业部门负责同志审定』**仅是自由职业(编码76)的审核依据**;其他录用形式就业(编码12)的审核依据是『用人单位出具的聘用证明**或**毕业生本人提供的工资收入证明、收入流水等其他证明材料』,没有『本人签字』与『校院两级审定』字样。电竞/全媒体运营走76、由本人签字材料认定属实;走12的则需单位证明或流水。」(3)时效限定:未检索到明文废止或替代教学厅函〔2021〕19号的文件,但2023年后官方表述已由『就业统计』转为『就业监测』——教育部办公厅2023-06-21建立『高校毕业生毕业去向登记制度』,教育部2024届就业创业工作通知第21条逐字要求『严格落实就业监测工作“四不准”“三不得”要求…严格执行就业监测工作违规处理办法』(19号原文只有『四不准』、无『三不得』、无违规处理办法)。故应加限定:『该文件是现行可查的最新公开界定标准,但2021年后指标框架有增补,是否存在未公开的新版界定标准无法核实。』

**核验依据**:逐字比对源为同一份 PDF 全文提取。附件2第7项逐字:『用人单位不签订就业协议或劳动合同，仅提供聘用证明、工资收入流水等证明材料』/审核依据『依据用人单位出具的聘用证明或毕业生本人提供的工资收入证明、收入流水等其他证明材料，薪酬需达到当地最低工资标准』;第8项(3)逐字『电子商务创业，利用互联网平台从事经营活动，如开设网店等』/审核依据『依据网店网址、网店信息截图和收入流水』;第9项逐字『指以个体劳动为主的一类职业，如作家、自由撰稿人、翻译工作者、中介服务工作者、某些艺术工作者、互联网营销工作者、全媒体运营工作者、电子竞技工作者等』/审核依据『依据毕业生本人签字确认的证明材料，由校、院两级就业部门负责同志审定，薪酬需达到当地最低工资标准』;正文第三条逐字『各省级就业工作部门在对外公开本省毕业生毕业去向落实率之前，须与教育部高校学生司核实数据，未经核实不得擅自公开。各高校未经省级就业工作部门同意，不得向其他部门、机构等提供本校就业数据。』——四段全部字符级一致。时效反证:http://www.moe.gov.cn/srcsite/A15/s3265/202312/t20231205_1093196.html 第21条原文。


#### [G50] HOLDS · confidence=high

**核验依据**:国家统计局《关于完善分年龄组调查失业率有关情况的说明》原页(https://www.stats.gov.cn/sj/zxfb/202401/t20240117_1946641.html)经 curl 取全文,逐字核对四处引用全部一致:『从我国国情看，在校学生的主要任务是学习，而不是兼职工作，如果把在校学生包含在分年龄组内，会把在校寻找兼职和毕业后寻找工作的青年混在一起，不能准确反映进入社会真正需要工作的青年人的就业失业情况』『多数青年 24 岁时刚毕业不久，尚处于择业期』『至 29 岁时绝大多数已度过择业期』。**『未公布重叠期双算数据』属实**:该说明全篇仅给出2023年各月平均在校生近6200万/非在校生约3400万的**存量结构**,无任何新旧口径换算或并行月份;结尾逐字『今后我局将按月在国家统计局数据发布库中发布不包含在校学生的 16—24 岁、25—29 岁、30—59 岁劳动力失业率』——说明分年龄组数据的**发布载体本就是数据发布库(data.stats.gov.cn)而非新闻稿页面**,故『统计局原页缺失』是制度设计而非采集疏漏(我确认 stats.gov.cn/sj/zxfb/ 2026年7月列表中确无分年龄组失业率条目)。2026年月度数字经四家独立媒体同日引述统计局7月20日发布交叉验证一致:6月16—24岁14.9%(较上月降0.7pp)、25—29岁7.1%、30—59岁4.0%(澎湃 https://www.thepaper.cn/newsDetail_forward_33621182);5月15.6%;4月16.3%、25—29岁7.4%、30—59岁4.2%(澎湃 https://m.thepaper.cn/newsDetail_forward_33205433);3月16.9%、7.7%、4.3%,且『结束了此前连续六个月的下降』(财新 https://economy.caixin.com/m/2026-04-21/102436199.html)。2023年6月旧口径21.3%及2023年8月起暂停发布、2023年12月新口径14.9%均获证实;21.3−14.9=6.4pp 的不可比性论断成立。ILO 1小时标准亦经统计局知识页证实(『在调查参考期内…为了取得劳动报酬或经营收入而工作了至少1小时的人』,并明示1小时标准『用于界定有没有就业，而非就业“足不足”』)。唯一建议:引注应写『国家统计局数据发布库(data.stats.gov.cn),经××媒体同日引述』,不宜暗示存在一个新闻稿式原页。


#### [G51] CORRECTED · confidence=high

**修正**:两套口径的全部行业数字、四条口径表述、79% 与 56% 复算**全部无误**,但**标题里的倍数是错的**。原表述:「非私营 vs 私营差 **1.94 倍**」→ 正确表述:「非私营 129,441 元 ÷ 私营 71,590 元 = **1.81 倍**」。1.94 是**信息传输业内部**的两口径之比(248,752 ÷ 128,166 = 1.94),被误当成全国总体之比;且 1.94 与本条自己写的『私营不足非私营的56%』内部矛盾(1÷0.553=1.81,1÷0.56=1.79)。另需修两处小口径:(a)税前逐字引用被截断,原文完整为『工资总额是税前工资，包括单位从个人工资中直接为其代扣或代缴的个人所得税、社会保险基金和住房公积金等个人缴纳部分**以及房费、水电费等**』,作为逐字引用应补全或加省略号;(c)『算术平均』的官方依据不是统计局自称『算术平均』,而是其平均工资计算公式逐字『就业人员平均工资 = 就业人员工资总额 / 就业人员平均人数』(即工资总额除以平均人数,受高薪者拉高的结论成立);统计局在该发布中确实未出现『中位数』三字。采集者标注的『教育 63,908 元 +3.3%』矛盾已核实:统计局表5私营教育增速为 **+5.3%**,原文中无 3.3%,采集笔误,文章按 5.3% 用即可。

**核验依据**:国家统计局《2025年城镇单位就业人员年平均工资情况》原页 https://www.stats.gov.cn/sj/zxfb/202605/t20260515_1963707.html 逐格核对:非私营全国129,441(名义+4.3%/实际+4.2%),信息传输、软件和信息技术服务业248,752(+4.1%)、金融业211,164(+4.6%)、科学研究和技术服务业182,064(+3.8%)、卫生和社会工作146,266(+2.2%)、教育133,539(+5.8%)、制造业113,594(+5.2%)、住宿和餐饮业62,461(+3.7%);私营全国71,590(名义+3.0%/实际+2.9%),金融业140,451(+3.8%)>信息传输业128,166(+4.0%),制造业76,055(+6.4%)、卫生和社会工作75,631(+0.5%)、教育63,908(+5.3%)、住宿和餐饮业55,123(+2.0%)——反超关系、增速对比(IT私营+4.0/非私营+4.1 双双低于制造+6.4/+5.2 与教育+5.3/+5.8)全部成立。口径注逐字:『城镇单位指城镇地域内就业人数在5人及以上的法人单位，2025年纳入统计的单位共计306.2万家』。复算:129441/71590=1.8081(≠1.94);248752/128166=1.9408(=1.94,来源即此);71590/129441=55.31%(『不足56%』成立);128166/71590=1.7903→高出私营总平均79.0%(成立)。


#### [G52] CORRECTED · confidence=high

**修正**:全部**数字与逐字引用无误**(1839/157/2220/1428、6.28万、1.02万/1.22万、超30%、首次突破10%、13门类/92专业类/883种、2025年版93类/845种、845+38=883、交叉学科11+4、毕业生909/1179/1222/1270万、2220+1428=3648 均已一手核实),但**两处承重推论必须修正**。(1)原表述:「官方文件通篇**未把『就业率』列为撤销的明示标准**…『撤销多=这个专业没前途』是媒体与考生的推断,不是官方论断」→ 正确表述:「官方文件把『就业率过低』明示为**停招/暂停招生**的触发条件——《普通高等学校本科专业设置管理规定》(教高〔2012〕9号)第二十六条逐字:『高校设置的专业在教育教学过程中出现办学条件严重不足、教学质量低下、**就业率过低**等情况，高校主管部门须责令有关高校限期整改、暂停招生。』;教高〔2023〕1号第13条逐字:『定期开展学科专业建设质量检查，对办学条件严重不足、教学质量低下、**就业率过低**的，要责令暂停招生、限期整改。』;教育部2024届就业创业工作通知第23条逐字:『持续实施高校毕业生**就业去向落实率红黄牌提示制度**…把毕业生就业状况作为“双一流”建设成效评价、**学科专业设置和调整评估**、招生计划安排…的重要依据。』;省级层面江西/四川以落实率50%为红黄牌阈值。因此:**『停招』有官方就业率依据(且停招数2220 > 撤销数1428),只有『撤销』(由高校申请、教育部备案)没有明示就业率标准。**『撤销多=没前途』是媒体推断;『停招多≈就业差』则有官方制度支撑。」(2)原表述:「布点数净减少 ≠ 招生规模缩小…**布点在减少而人数在增加**」→ 正确表述:「**布点数并未净减少**——按本条自己给出的定义,停招保留专业点、只有撤销从目录删除,故2024年度净变化为 1839−1428 = **净增411个布点**;2023年度为 增设1673−撤销1670 ≈ 净增3;目录专业种数亦逐年增(2024年版816种→2025年版845种→2026年版883种)。正确说法是『**在招**布点在收缩、**存量**布点仍在净增,同时毕业生人数在增加』。」另,『十四五累计新增1.02万、撤销或停招1.22万』因把撤销与停招合并统计,同样不能推出布点净减。

**核验依据**:教育部2025-04-22新闻稿 http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202504/t20250422_1188245.html 逐字:『全国高校共新增专业点1839个，调整学位授予门类或修业年限专业点157个，停招专业点2220个，撤销专业点1428个』『新目录包含93个专业类、845种专业』『目前全国高校本科专业布点共有6.28万个』——与论断逐字完全一致(注:该逐字出自新闻稿,非答记者问)。答记者问 http://www.moe.gov.cn/jyb_xwfb/s271/202504/t20250422_1188246.html 逐字:『撤销、停招专业点数大幅超过增设专业点数，专业结构不断优化』。教育部2026-04-28发布逐字:『目前，本科专业目录共涵盖13个门类、92个专业类、883种专业』『“十四五”期间，全国高校新增本科专业布点1.02万个、撤销或停招1.22万个。专业调整幅度持续增大，累计调整比例超30%，今年全国高校专业调整比例首次突破10%』;教高函〔2026〕2号原文 http://www.moe.gov.cn/srcsite/A08/moe_1034/s3882/202604/t20260427_1434931.html 逐字确认『首批列入“交叉学科”门类有未来机器人、交叉工程等11种目录中已有的专业和具身智能、脑机科学与技术等4种新专业』(落款2026年4月7日,门户发布日2026-04-28)。反证:教高〔2023〕1号原文 http://www.moe.gov.cn/srcsite/A08/s7056/202304/t20230404_1054230.html 第13条;教高〔2012〕9号第二十六条(济南大学高教研究院全文转载 https://ihe.ujn.edu.cn/info/1008/1312.htm);2023年度数据(增设1673/撤销1670、2024年版目录93类816种)见教育部2024-03-19通知。毕业生规模:新华社2025-11-20『2026届全国普通高校毕业生规模预计1270万人』同比增48万→2025届1222万,2024届1179万,2021届909万。


#### [G53] CORRECTED · confidence=high

**修正**:考研序列、−45万/−11.6%、连续第三年下降、国考3.81万/371.8万/98:1/+30余万、年龄放宽属实、四条构念效度局限本身——**均成立**。需修正三处:(1)原表述:「2026年…**首次跌破350万**」→ 正确表述:「**2020年全国硕士研究生招生考试报名人数即为341万,已在350万之下**;2021年377万、2022年457万。343万应表述为『**为2020年以来最低**』或『退回到2020年水平』,不是首次跌破350万。」(可对照的媒体口径是:2025年388万被称为『十年来首次跌破400万』。)(2)原表述:「国考…**招录计划本身也在扩张**」→ 正确表述:「**招录计划反而在收缩**:2025年度国考计划招录**3.97万人**、过审341.6万、比例约**86:1**;2026年度计划招录**3.81万人**(同比约**−4.0%**)、过审371.8万(同比**+8.8%**)、比例约98:1。**98:1 的抬升同时来自分子上升与分母下降**,不能只归因于报名端。」(3)原表述:「口径=网上报名并缴费确认人数」「官方解读框架(新华社…)」→ 正确表述:「教育部原文仅逐字称『**报名人数为343万**』,**未公开界定该口径**(是否剔除未缴费/未确认者、是否为去重人数均无官方说明),亦不公布应届/往届拆分——应写『口径未公开界定』而非替它指定为缴费确认人数;另新华社该稿标题下的内容是**受访专家(厦门大学教育研究院副院长王树涛等)的分析**,应表述为『新华社援引专家的解读框架』,不是教育部的官方解读。」

**核验依据**:教育部2025-11-24原文(curl 取全文,http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/moe_1485/202511/t20251124_1421370.html,标题《教育部部署2026年全国硕士研究生招生考试安全工作》)结尾逐字:『据统计，2026年全国硕士研究生招生考试报名人数为343万。』——全文再无口径界定、无应往届拆分、无『回归理性』字样。历史序列:2020年341万、2021年377万、2022年457万、2023年474万、2024年438万(『比上年度减少36万…2015年以来连续8年增长态势就此终止』)、2025年388万,均见人民网/央广网等对教育部数据的报道。国考:2026年度3.81万人/371.8万过审/约98:1/较上年增30.2万,并逐字『报考者年龄一般为18周岁以上、38周岁以下…2026年应届硕士、博士研究生放宽到43周岁以下』(原为35/40周岁,背景为渐进式延迟法定退休年龄政策),见国家公务员局公告及央视网 https://edu.cctv.com/2025/10/27/ARTIjpBHmnytUTCFm5ip7xqd251027.shtml、京报 https://news.bjd.com.cn/2025/10/15/11352154.shtml;2025年度国考『共计划招录3.97万人…共有341.6万人通过了资格审查，通过资格审查人数与录用计划数之比约为86:1』见新华网 http://www.news.cn/politics/20241201/ce8b28b6e0084f4f901dec1c26a1fea1/c.html 与中国日报 https://cn.chinadaily.com.cn/a/202412/01/WS674bdbdba310b59111da6685.html。复算:3.81/3.97−1=−4.03%;371.8/341.6−1=+8.84%;371.8万/3.81万=97.6≈98:1。新华社原稿《报考回归理性 发展路径多元——专家分析2026年考研报名人数》(2025-11-24,http://www.news.cn/20251124/e54d3157f15744f5beb5b76644035f5d/c.html)标题即含『专家分析』。


### 第 3 席


#### [G48] CORRECTED · confidence=high

**修正**:逐字公式与改名句 100% 无误,但"没有任何官方的分专业就业数据"这一绝对表述必须收窄,否则读者一查即破。

(1) 原表述:"中国没有任何官方的'分专业毕业生失业率''分专业起薪''分专业学历错配率'任何一项" → 正确表述:"中国没有官方公开发布的分专业**数值型**指标(失业率/起薪/错配率一个都没有),但教育部确实按专业口径**采集并公开发布过排序型产物**:2014年10月教育部高等教育司公布了全国及31省份'近两年(2012、2013年)就业率较低的本科专业名单'(全国15个专业),只给专业名、不给就业率数字;2026-04-28教育部称已'推动各省份发布覆盖473种专业的急需专业清单和专业预警清单';教就业〔2024〕5号更明令'对就业质量不高的专业实行红黄牌提示制度'。因此准确说法是:官方**掌握**分专业就业数据,但**只发布名单、从不发布分母与数值**。"

(2) 由此,方法论结论要改口径:原来的"中方根本没有分专业数据" → "中方有分专业数据但不公开数值,美方(NY Fed/BLS/ACS)公开微观数据可复算——不对称在**可复现性**而非**存在性**"。这个修正反而更强:不可复算比不存在更值得写。

(3) 配套论断的逐字公式有一处结构错误。原表述:"分子包含升学、灵活就业、自由职业、创业"(四项并列) → 正确表述:附件1公式只有四个加项"协议和合同就业率+创业率+灵活就业率+升学率",**自由职业(编码76)是灵活就业的子项**,不是并列加项;另外"升学率"的包含内容含"出国、出境(编码85)",即出国留学也计入落实率分子,这一点原文漏了,而它对准大学生更有解释力。

(4) "各分率分母统一为毕业生总数"——逐字核对无误,附件1四个分率均写作"/毕业生总数"。

(5) "中国无对应 underemployment 的官方指标"——穷尽搜索未发现任何官方学历错配/低度就业指标,该句可保留。

**核验依据**:回到一手 PDF 逐字核对(湖南省教育厅转发的教育部办公厅教学厅函〔2021〕19号原件,pdftotext 全文提取):https://jyt.hunan.gov.cn/jyt/sjyt/bys/tzgg_1/202105/16548110/files/d1856b6e22214d6abd4256691c63fd34.pdf 。附件1原文表格右栏逐字:"毕业去向落实率=协议和合同就业率+创业率+灵活就业率+升学率";正文第一条逐字:"为更加准确反映高校毕业生升学、就业等毕业去向情况,从 2021 届起,将'就业率'改为'毕业去向落实率'。"四个分率在表中逐字写作"协议和合同就业率=协议和合同就业数/毕业生总数""创业率=自主创业数/毕业生总数""灵活就业率=灵活就业数/毕业生总数""升学率=升学数/毕业生总数";"灵活就业"行的"包含的毕业去向"栏逐字为"其他录用形式就业(编码 12)"与"自由职业(编码 76)",证明自由职业是灵活就业子项;"升学"行含"出国、出境(编码 85)"。

反证来源(证明官方分专业产物存在):① 教育部官网 http://www.moe.gov.cn/jyb_xwfb/s5147/201410/t20141015_175978.html 原文:"教育部官方微信'微言教育'推送近两年(2012年、2013年)就业率较低的本科专业名单……共15个专业榜上有名";"名单由教育部高等教育司整理并公布";"同时公布的还有全国31个省份和新疆生产建设兵团分省的就业率较低的本科专业名单"——只有名单,无一个就业率数字。② 教育部 2026-04-28 http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202604/t20260428_1435016.html 原文:"推动各省份发布覆盖473种专业的急需专业清单和专业预警清单"。③ 教就业〔2024〕5号 http://www.moe.gov.cn/srcsite/A15/s3265/202411/t20241112_1162526.html 原文:"对就业质量不高的专业实行红黄牌提示制度"。④ 教高司函〔2025〕3号 http://www.moe.gov.cn/s78/A08/tongzhi/202506/t20250630_1196068.html 原文:"于7月31日前发布本年度省级急需本科专业清单和过剩专业预警清单"。

穷尽性说明:检索国家统计局年鉴栏目(https://www.stats.gov.cn/hd/lyzx/zxgk/tjnj/index.html)与《中国劳动统计年鉴》条目,未见任何分专业就业率/起薪表;《中国劳动统计年鉴》口径为分行业、分职业、分年龄,无分专业。流传的"红牌/绿牌专业"(法学、绘画、公共事业管理等)来自麦可思 MyCOS《中国大学生就业报告》——**商业调查机构,自费抽样,非官方**,文章若引用必须标注利益相关。


#### [G49] CORRECTED · confidence=high

**修正**:四段引文逐字核对**全部精确无误**(编码12、编码76、编码75(3)、数据发布管制),这是本批质量最高的一组引用。但归纳句 overreach,须修两处:

(1) 原表述:"官方'就业'的下限 = **月入**达当地最低工资 + 一张本人签字的说明。**开网店**、做电竞、当博主均计入落实率" → 正确表述:"最低工资门槛只约束三类——'科研助理、管理助理''其他录用形式就业(编码12)''自由职业(编码76)';**自主创业(编码75)中的电子商务创业没有任何薪酬下限**,审核依据逐字只有'网店网址、网店信息截图和收入流水',不要求达到最低工资。所以'开网店'恰恰是门槛最低的一档:一个网址、一张截图、一份流水即可,连最低工资都不必达到。"这个修正让论断更锋利,不要放过。

(2) 原表述"**月入**达当地最低工资" → 正确表述:原文只写"薪酬需达到当地最低工资标准",附件2说明1指向人社部《全国各地区最低工资标准情况》,该表同时含**月最低工资标准与小时最低工资标准**,文件未指定按月还是按小时。"月入"是推断,不是逐字。

(3) "灵活就业 = 编码12 + 编码76"——附件1原表逐字确认,HOLDS,可原样使用。

(4) 时效性(必须标注的限制):未能检索到 2021 年后修订或废止 19 号文的教育部文件;2024 年 11 月的教就业〔2024〕5号未改动毕业去向分类。因此**推定仍现行,但"截至 2026-07 未见修订版"应写成显式限定语**,不要断言"至今有效"。

**核验依据**:一手 PDF 全文提取逐字比对(同上 URL:https://jyt.hunan.gov.cn/jyt/sjyt/bys/tzgg_1/202105/16548110/files/d1856b6e22214d6abd4256691c63fd34.pdf)。

附件2 第7项原文逐字:"7.其他录用形式就业(编码 12)|用人单位不签订就业协议或劳动合同,仅提供聘用证明、工资收入流水等证明材料|依据用人单位出具的聘用证明或毕业生本人提供的工资收入证明、收入流水等其他证明材料,薪酬需达到当地最低工资标准"——与论断逐字一致。

第9项原文逐字:"9.自由职业(编码 76)|指以个体劳动为主的一类职业,如作家、自由撰稿人、翻译工作者、中介服务工作者、某些艺术工作者、互联网营销工作者、全媒体运营工作者、电子竞技工作者等|依据毕业生本人签字确认的证明材料,由校、院两级就业部门负责同志审定,薪酬需达到当地最低工资标准"——逐字一致。

第8项原文逐字:"8.自主创业(编码 75)……(3)电子商务创业,利用互联网平台从事经营活动,如开设网店等|依据网店网址、网店信息截图和收入流水"——**注意该行审核依据到'收入流水'即结束,无'薪酬需达到当地最低工资标准'字样**,这是修正(1)的直接证据。

附件2 末尾说明1逐字:"'科研助理、管理助理''其他录用形式就业''自由职业'中当地最低工资标准参见人社部公布的《全国各地区最低工资标准情况》。"——最低工资门槛的适用范围被显式限定为这三类,自主创业不在其中。

数据发布管制,正文第三条原文逐字:"各省级就业工作部门在对外公开本省毕业生毕业去向落实率之前,须与教育部高校学生司核实数据,未经核实不得擅自公开。各高校未经省级就业工作部门同意,不得向其他部门、机构等提供本校就业数据。"——逐字一致。完整语境是第三条"严格落实就业统计责任制",紧接在省级/校级分管领导签字确认要求之后,即该管制与"签字问责"是同一条款的两半。同条另有第五条"四不准"(不准强迫签约、不准与发证挂钩、不准以户档托管劝签虚假就业协议、不准以顶岗实习证明充作就业证明),文章若写门槛低,应并列这条以示官方亦知造假风险。


#### [G50] CORRECTED · confidence=high

**修正**:口径断裂这一核心判断 HOLDS,统计局说明的三处引文逐字精确。但有三处溯源问题必须修:

(1) 原表述把 "21.3%" 与 "14.9%" 写得像出自统计局《关于完善分年龄组调查失业率有关情况的说明》 → 正确表述:该说明全文**只字未提 21.3%、14.9% 或任何一个失业率数字**。21.3% 出自 2023 年 7 月 17 日统计局例行发布的 2023 年 6 月数据(旧口径最后一次公布),14.9% 出自 2024 年 1 月 17 日随说明同日启用的数据发布库首月新口径值。引用时须分三个出处标注,不能合并归给该说明。

(2) 原表述:"国家统计局未公布新旧口径的重叠期双算数据,因此无法量化'排除在校生'造成的落差" → **HOLDS,且可补一条更硬的证据**:说明中唯一给出的换算素材是分母存量而非失业率——逐字"2023年各月平均,我国16—24岁城镇人口中,在校学生占比6成多,近6200万人;非在校学生占比3成多,约3400万人"。即统计局只交代了"谁被剔除、有多少人",从未给出剔除后同期失业率。补上这句,"无法量化落差"就从断言变成有据可查的事实。

(3) 原表述:2026 年 3—6 月月度数字 → 正确表述:6 月 14.9%、25—29 岁 7.1%、30—59 岁 4.0% 可确认,且官方口径是"较上月分别下降 0.7、0.1、0.1 个百分点,三个年龄段均连续 3 个月下降",由此 5 月 16—24 岁 = 15.6% 可反算确认。**但 4 月 16.3%、3 月 16.9% 未能落到一手页面**,只能内部自洽反推,建议文中只写 6 月与 5 月,或对 3—4 月加"据月度环比反推"限定语。另须写明:自 2024 年 1 月起这组数字**不再有独立发布页**,统计局说明逐字"今后我局将按月在国家统计局数据发布库中发布",一手出处是 data.stats.gov.cn 数据库而非 stats.gov.cn 新闻稿——这本身就是可发布性下降的证据,值得写进方法论一节。

(4) ILO 1 小时标准与"对就业质量恶化不敏感"——HOLDS,与统计局"就业人员"定义(调查参考期内工作1小时以上取得报酬)一致。

**核验依据**:一手页面 curl 全文提取逐字核对:https://www.stats.gov.cn/sj/zxfb/202401/t20240117_1946641.html (《关于完善分年龄组调查失业率有关情况的说明》,2024/01/17 10:30,来源国家统计局)。

逐字命中(与论断完全一致):"从我国国情看,在校学生的主要任务是学习,而不是兼职工作,如果把在校学生包含在分年龄组内,会把在校寻找兼职和毕业后寻找工作的青年混在一起,不能准确反映进入社会真正需要工作的青年人的就业失业情况";"多数青年24岁时刚毕业不久,尚处于择业期,一些人未就业或就业不稳定,至29岁时绝大多数已度过择业期,就业情况趋向稳定"。

全文检索该页:未出现 "21.3"、"14.9" 或任何失业率百分数,亦无任何新旧口径重叠期换算、回溯序列或折算系数——"关键空白"属实。该页给出的唯一定量素材逐字为:"2023年各月平均,我国16—24岁城镇人口中,在校学生占比6成多,近6200万人;非在校学生占比3成多,约3400万人。"发布方式逐字:"今后我局将按月在国家统计局数据发布库中发布不包含在校学生的16—24岁、25—29岁、30—59岁劳动力失业率,大家可以在数据发布库中查询数据。"

2026 年 6 月数据:统计局按上述规定只在数据发布库(https://data.stats.gov.cn/)发布,无独立新闻稿页。经转述可核的官方措辞为"6月份,全国城镇不包含在校生的16-24岁劳动力失业率为14.9%,较上月下降0.7个百分点;25-29岁为7.1%,较上月下降0.1个百分点;30-59岁为4.0%,较上月下降0.1个百分点","三个年龄段均连续3个月下降"(观察者网 2026-07-20 https://www.guancha.cn/politics/2026_07_20_824452.shtml 、新浪财经 2026-07-21 引国家统计局)。据"较上月下降0.7"可确认 5 月为 15.6%;3 月 16.9%、4 月 16.3% 仅与"连续3个月下降"自洽,未取得一手页面确认——本席判为待补,不予背书。


#### [G51] CORRECTED · confidence=high

**修正**:全部行业数字与四条口径逐格核对**无误**,采集者标注的增速矛盾也证实是对的。但**标题里的倍数算错了,而且错得很典型**:

(1) 原表述:"非私营 vs 私营差 **1.94 倍**" → 正确表述:"非私营 vs 私营全国平均差 **1.81 倍**(129,441 ÷ 71,590 = 1.808)"。1.94 这个数其实是**信息传输业内部**的两套口径之比(248,752 ÷ 128,166 = 1.941),被误当成了全国总平均之比。这是一处会被读者用计算器当场戳穿的错误,必须改。若想保留 1.94,须改写为:"IT 行业内部,非私营口径是私营口径的 1.94 倍——比全国总体的 1.81 倍还悬殊,说明 IT 的'高薪印象'高度依赖非私营样本。"

(2) 采集者标注的"教育 63,908 元 +3.3%→实为 5.3%"——**确认应为 +5.3%**,原页私营教育为 63,908 元、增长 5.3%。文中后段"教育(+5.3%/+5.8%)"是对的,前段列表若写 3.3% 须删。

(3) 复算确认:71,590 ÷ 129,441 = 55.31%,"不足非私营的 56%"成立;128,166 ÷ 71,590 − 1 = **79.03%**,"高出私营总平均 79%"成立。可再补一个更有冲击力的对照:非私营 IT 高出非私营总平均 92.2%,即无论哪套口径 IT 溢价都在 79%–92%,"IT 不赚钱了"确实不成立。

(4) 四条口径逐字确认全部成立:(a)"工资总额是税前工资,包括单位从个人工资中直接为其代扣或代缴的个人所得税、社会保险基金和住房公积金等个人缴纳部分";(b)5 人及以上法人单位、2025 年 306.2 万家("不包括个体工商户和自由职业者"是法人单位口径的推论,非原文字面,建议写成"因限于法人单位,个体工商户与自由职业者不在样本内");(c) 该发布通篇只有算术平均,统计局不发布分行业工资中位数,与美方 median earnings 不可并列;(d) 为全部就业人员平均,非应届生起薪。

(5) 建议补一条口径不对称提醒:全国平均 129,441(非私营)+4.3%、71,590(私营)+3.0%,两套口径的**样本量差异极大**,把两个平均值直接相减或相除得出的"倍数"本身就带有构成偏误(行业与所有制混杂),文中用倍数时宜加限定。

**核验依据**:一手页面逐格核对:https://www.stats.gov.cn/sj/zxfb/202605/t20260515_1963707.html(国家统计局《2025年城镇单位就业人员年平均工资情况》,2026-05-15)。

城镇非私营单位,全国 129,441 元(名义增长 4.3%、实际 4.2%);信息传输、软件和信息技术服务业 248,752(+4.1%)居首;金融业 211,164(+4.6%);科学研究和技术服务业 182,064(+3.8%);卫生和社会工作 146,266(+2.2%);教育 133,539(+5.8%);制造业 113,594(+5.2%);住宿和餐饮业 62,461(+3.7%)——与论断逐格一致。

城镇私营单位,全国 71,590 元(名义 +3.0%、实际 +2.9%);金融业 140,451(+3.8%)**高于**信息传输业 128,166(+4.0%);制造业 76,055(+6.4%);**教育 63,908(+5.3%)**;卫生和社会工作 75,631(+0.5%);住宿和餐饮业 55,123(+2.0%);科学研究和技术服务业 83,560(+1.4%)——除教育增速外与论断一致,教育确为 5.3% 而非 3.3%。

口径逐字:"工资总额是税前工资,包括单位从个人工资中直接为其代扣或代缴的个人所得税、社会保险基金和住房公积金";统计范围为"就业人数在5人及以上的法人单位",2025 年纳入统计 306.2 万家;全篇只发布平均值,无中位数。

复算(python 验证):129441/71590 = 1.8081(**非 1.94**);248752/128166 = 1.9409(即 1.94 的真实来源);71590/129441 = 55.31%;128166/71590 = 1.7903 → +79.03%;248752/129441 → +92.17%。


#### [G52] REFUTED · confidence=high

**修正**:**所有数字逐字核对无误,但本条两处承重的解读性论断被官方原文直接推翻,且有一处引文系伪引——按"不可承重"判 REFUTED。**

(1) 最严重:原表述"官方文件通篇**未把'就业率'列为撤销的明示标准**",以及"'撤销多=这个专业没前途'是媒体与考生的推断,不是官方论断" → **正确表述:教育部至少三份现行文件把就业率写成了明示的行政后果触发条件。**教高〔2023〕1号第13条逐字:"定期开展学科专业建设质量检查,对办学条件严重不足、教学质量低下、**就业率过低**的,要责令**暂停招生**、限期整改";同文件第16条逐字:"对高校**连续五年未招生**的专业予以**撤销**处理"——两条构成完整链条:就业率过低 → 责令暂停招生 → 连续五年未招生 → 撤销。教高司函〔2025〕3号逐字:"对本地区**布点量大、就业率过低**的专业及相近专业,原则上不再支持增设"。教就业〔2024〕5号逐字:"对**就业质量不高**的专业实行**红黄牌提示制度**","将高校毕业生**就业状况**作为高校办学资源配置、教学质量评估、**招生计划安排的重要依据**"。因此正确写法是:"就业率是官方明示的**停招**触发条件(撤销则以'连续五年未招生'为直接条件),二者由同一条政策链相连——'撤销多=就业差'不是民间脑补,是政策设计的预期结果;真正需要提醒考生的是**滞后性**(从就业率过低到撤销可长达五年以上),而不是'官方没这么说'。"

(2) 伪引:原表述把"**撤销、停招专业点数大幅超过增设专业点数,专业结构不断优化**"标为教育部逐字 → 该句**不在** 2025-04-22 与 2026-04-28 两份教育部发布中。2025-04-22 原文对应表述是"**专业调整优化力度进一步加大**";2026-04-28 原文是"**本科专业结构进一步优化**"。须删除该引号或替换为上述真实原文。

(3) 原表述"《目录(2026年)》**新增 38 种**专业"→ 教育部 2026-04-28 发布**通篇未出现"38"**,只逐字写了交叉学科门类"首批列入未来机器人、交叉工程等11种目录内已有专业和具身智能、脑机科学与技术等4种本次列入目录的新专业"。38 是 883−845 的净差,系媒体算出。

(4) 原表述"专业类减少 1、专业种数增加 38,**说明发生了合并重组,不能读作'净增 38 种全新专业'**"→ 推理不成立。若确有 38 种新专业列入目录且净增恰为 38,则**没有专业种被删除**,38 种就是真新增;93→92 的变化发生在**专业类**层级(交叉学科门类新设导致专业类重划),与专业种数的增减无关。正确表述应为:"门类由 12 增至 13(新设交叉学科)、专业类由 93 减至 92、专业种由 845 增至 883;专业类的减少是门类重划的结果,不能据此推断专业种发生了合并。"

(5) 以下数字**逐字核对全部无误,可放心使用**:2024 年度新增专业点 1,839、调整学位授予门类或修业年限 157、停招 2,220、撤销 1,428;布点总数 6.28 万;十四五新增布点 1.02 万、撤销或停招 1.22 万、累计调整比例超 30%、今年首次突破 10%;2026 年目录 13 门类/92 专业类/883 种;2025 年目录 93 专业类/845 种(该版增列 29 种)。"单位是专业点不是人""停招≠撤销""全国目录仅 883 种专业"三条口径提醒均成立且有价值,应保留。

(6) "布点净减少 ≠ 招生规模缩小"方向成立:2021 届 909 万 → 2024 届 1,179 万 → 2025 届 1,222 万 → 2026 届预计 1,270 万。但 1,270 万仅经二手确认(教育部 2026 届就业创业工作部署),**未落到一手页面**,建议加"教育部预计"限定。

**核验依据**:① 教高〔2023〕1号《普通高等教育学科专业设置调整优化改革方案》一手全文 curl 提取:http://www.moe.gov.cn/srcsite/A08/s7056/202304/t20230404_1054230.html 。第13条逐字:"定期开展学科专业建设质量检查,对办学条件严重不足、教学质量低下、就业率过低的,要责令暂停招生、限期整改。"第16条逐字:"加强学科专业存量调整,完善退出机制。对高校连续五年未招生的专业予以撤销处理。"第14条逐字:"省级教育行政部门要……及时公布本地优先发展和暂缓发展的学科专业名单。建立健全招生培养就业联动机制。"第21条逐字:"对人才需求趋少的行业产业进行学科专业设置预警。"

② 教高司函〔2025〕3号一手全文:http://www.moe.gov.cn/s78/A08/tongzhi/202506/t20250630_1196068.html 逐字:"对本地区布点量大、就业率过低的专业及相近专业,原则上不再支持增设,对办学质量不高的专业,要尽快调整。"及"于7月31日前发布本年度省级急需本科专业清单和过剩专业预警清单"。

③ 教就业〔2024〕5号一手全文:http://www.moe.gov.cn/srcsite/A15/s3265/202411/t20241112_1162526.html 第2条逐字:"对就业质量不高的专业实行红黄牌提示制度,及时调整或更新升级已经不适应社会需要的学科专业。"第3条逐字:"各地各高校要将高校毕业生就业状况作为高校办学资源配置、教学质量评估、招生计划安排的重要依据。"

④ 教育部 2025-04-22 一手全文:http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202504/t20250422_1188245.html 逐字:"全国高校共新增专业点1839个,调整学位授予门类或修业年限专业点157个,停招专业点2220个,撤销专业点1428个,专业调整优化力度进一步加大。";"《普通高等学校本科专业目录(2025年)》,增列29种新专业。新目录包含93个专业类、845种专业。";"目前全国高校本科专业布点共有6.28万个。";结尾逐字"教育部将进一步强化专业设置与就业工作的联动"——**全文检索无"撤销、停招专业点数大幅超过增设专业点数,专业结构不断优化"一句**。

⑤ 教育部 2026-04-28 一手全文:http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202604/t20260428_1435016.html 逐字:"2026年本科专业目录在'交叉学科'门类中首批列入未来机器人、交叉工程等11种目录内已有专业和具身智能、脑机科学与技术等4种本次列入目录的新专业。目前,本科专业目录共涵盖13个门类、92个专业类、883种专业。";"'十四五'期间,全国高校新增本科专业布点1.02万个、撤销或停招1.22万个。专业调整幅度持续增大,累计调整比例超30%,今年全国高校专业调整比例首次突破10%。本科专业结构进一步优化"——**全文无"38"字样**。

⑥ 复算:883−845=38;93→92 为专业类层级变化。1,270 万(2026 届)经 moe.gov.cn 索引确认存在但未取得一手正文页,标为二手。

⑦ 利益相关提示:教育部是撤销/停招的执行方,"结构优化"为其自评话语;而流传的"红牌专业"榜(法学、绘画等)出自麦可思 MyCOS——商业调查公司,靠就业报告与咨询业务盈利,与"专业风险"叙事存在商业利益关联,不可与教育部数据并列。


#### [G53] CORRECTED · confidence=high

**修正**:构念效度那一整段是本批最扎实的论述,应原样保留。但**两处事实错误必须改,其中一处把结论说反了**:

(1) 原表述:"2026 年考研报名 343 万……并**首次跌破 350 万**" → **错误。**2020 年全国硕士研究生招生考试报名人数为 **341 万**,2019 年 290 万,均低于 350 万。正确表述:"343 万为 **2020 年(341 万)以来最低**",或"自 2022 年冲上 457 万的高点后首次回落至 350 万以下"。写"首次跌破"会被任何查过历年序列的读者推翻。

(2) 原表述:"国考……**招录计划本身也在扩张**。'创新高'中有多少来自年龄放宽、多少来自就业压力,官方未拆分。" → **方向说反了。**2026 年度国考计划招录 3.81 万人,**较 2025 年度减少 1,602 人(约 0.16 万),为 2019 年以来首次缩招**。正确表述:"分母不但没扩张,反而是 2019 年以来第一次缩招(3.97 万 → 3.81 万);因此 98:1 的过审比同时受到**报名端扩张(+30.2 万,+8.8%)与录用端收缩(−1,602)**双向推高。年龄放宽会机械抬高报名基数这一点仍成立且更重要,但不能再用'招录也在扩张'去对冲——那反而低估了竞争强度。"这处修正会改变段落结论的方向。

(3) 建议补一个可复算的对照,让读者自己校验口径:2025 年度过审 341.6 万 ÷ 计划 3.97 万 ≈ **86:1**;2026 年度 371.8 万 ÷ 3.81 万 ≈ **97.6:1**,四舍五入为 98:1。官方口径本身即"通过资格审查人数与录用计划数之比",不是录取率。

(4) 年龄放宽的具体内容(原论断只说"放宽了上限",可补实):一般报考者由 18 周岁以上、**35 周岁以下放宽至 38 周岁以下**;2026 年应届硕士、博士研究生由 **40 周岁以下放宽至 43 周岁以下**,两类各放宽 3 岁,官方定位为与延迟退休政策相衔接。政策变更属实,论断成立。

(5) 以下逐字/数值**核对无误**:考研 343 万(教育部原文"据统计,2026年全国硕士研究生招生考试报名人数为343万");388→343 减少 45 万、−11.6%;"自 2024 年起连续第三年下降"(474→438→388→343,三次连降);国考 3.81 万、371.8 万、98:1、较 2025 年度 341.6 万增加 30 余万、过审比创新高;"371.8 万是通过资格审查人数、不是报名人数";"考研 343 万(报名缴费)与国考 371.8 万(过审)口径不同不可并列";"教育部不公布应届/往届拆分";考研 −11.6% 与国考 +8.8% 同时发生。

(6) 未能核实项:新华社 2025-11-24《报考回归理性 发展路径多元》这一具体篇名与日期本席未取得一手页面(本会话检索额度耗尽),"官方解读框架与民间叙事方向相反"这一判断在方向上与教育部/央媒基调一致,但**具体标题与出处请二次确认后再加书名号引用**。

**核验依据**:① 考研 343 万一手:教育部官网 http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/moe_1485/202511/t20251124_1421370.html《教育部部署2026年全国硕士研究生招生考试安全工作》(2025-11-24),curl 全文提取,末段逐字:"据统计,2026年全国硕士研究生招生考试报名人数为343万。"

② 历年序列反证(推翻"首次跌破350万"):教育部官网 http://www.moe.gov.cn/jyb_xwfb/s5147/201912/t20191219_412639.html《考研报名人数屡创新高 今年突破三百万》确认 2020 年报名 **341 万**(较 2019 年 290 万增 51 万);教育部官网 http://www.moe.gov.cn/jyb_xwfb/s5147/202012/t20201228_507808.html 确认 2021 年 **377 万**。341 万 < 350 万,故 2026 年的 343 万并非首次跌破 350 万。

③ 国考一手/权威:新华网 2025-11-30 http://www1.xinhuanet.com/politics/20251130/7da14327e1c24cafbf0af0a287a2f085/c.html《2026年国考今日开考:招录年龄放宽 报名创新高》逐字要点:"2026年国考共计划招录3.81万人,较上年度减少了0.16万人";通过资格审查 371.8 万人创历史新高;过审人数与录用计划之比"从70:1逐年递增至98:1";年龄"18周岁以上、38周岁以下",2026 年应届硕博"43周岁以下",较以往 35 岁与 40 岁上限各放宽 3 岁。另财新 2025-10-27 https://m.caixin.com/m/2025-10-27/102376073.html 与北京日报客户端 https://bjqn-app.bjd.com.cn/content/s68fe7853e4b0221b9beeb464.html 均载 371.8 万过审、较 2025 年度 341.6 万增加 30 余万,且明确 3.81 万"较2025年减少1602人,为2019年以来首次缩招"。

④ 复算(python 验证):371.8/3.81 = 97.6 ≈ 98:1;2025 年度计划 3.81+0.16 = 3.97 万,341.6/3.97 = 86.0:1;(371.8/341.6 − 1) = +8.84%;(343/388 − 1) = −11.6%,差 45 万。

⑤ 未取得一手:新华社 2025-11-24《报考回归理性 发展路径多元》篇名未验证(WebSearch 额度已耗尽,WebFetch 经 bing/ddg 转介被反爬拦截)。


## 批次 H2 — verify:中国商业调查


### 第 1 席


#### [G54] HOLDS · confidence=high

**核验依据**:我取到了两份一手文件并逐字核对。(1) 新三板研报 PDF（https://pdf.dfcfw.com/pdf/H3_AP201911121370658000_1.pdf，新三板智库 2019-11-07，研究员麦棋昌/方俊杰，图表标注「资料来源：公司年报」）：「公司于 2015 年 10 月上市，股票代码为 833861」；图表1 王伯庆 690.00 万股、61.61%（正文另写「个人持股比例达到 61%」）；图表3：2018 主营业务收入 110,752,232.01、其他业务收入 2,749,597.93、毛利率 87.39%；数据监测类收入 96,886,518.62（占营业收入 85.36%）、咨询类 16,615,311.32（14.64%）。分母核验：96,886,518.62 ÷ 113,501,829.94（=主营+其他业务收入）= 85.36% ✓，采集者写的「占营业收入」口径正确（若误按主营业务收入作分母应为 87.48%）。客户描述逐字：「公司直接面对高校、院系/专业、教育厅/局等机构客户提供产品和解决方案」；「在中国教育部门批准 2500 所高校中累计合作 706 所，正在执行签约项目的 569 所，其中服务年限在三年以上的客户占比为 83%」。(2) 2023 年本科生就业报告 PDF 我用 pdftotext 抽出 20,809 行——与采集者所述行数完全一致，确认同一文件。论断B逐字命中（PDF 第207-208页）：「全国本科生样本为 13.5 万人。覆盖了 428 个本科专业，覆盖了全国 30 个省、自治区和直辖市」；「不包括成人高等教育、军事院校和港澳台院校的毕业生」；「以电子邮件方式发放答题邀请函……答题时间为 10~30 分钟」；「1. 答题通过电子问卷客户端实现，未被邀请的答题被视为无效。」我独立复跑检索：「回收率」「应答率」「答题率」「响应率」在全书 0 命中——关键缺口属实，13.5 万确无分母。论断C逐字命中：「2. 本研究对答题和未答题的样本进行了检验，没有发现存在自我选择性样本偏差问题（Self-selection Bias）」，确无变量、检验方法、p 值。补强一点：该句脚注自己给的例子正是「可能存在就业的毕业生更容易选择参与答题，而没有就业的学生可能不愿意参加答题」——书方自陈了这一偏差方向却未给检验细节，张力比采集者所述更强。论断D逐字命中：「本研究采用权数加以修正（即对回收的全国总样本，基于学历、地区、院校类型、专业的实际分布比例进行再抽样）」，附表1 东部 38.5%/38.5%、中部 26.7%/26.7%、西部 25.4%/25.4% 完全相等，确为再抽样特征。我另检索全书「客户」「付费」「合作高校」「利益」：除「问卷客户端」外 0 命中，即书内确未披露高校付费客户关系，支持「未见披露」。未能独立复核的两点（已在置信度中体现）：论断E（官网不公开）我未逐页遍历 mycos.com.cn；「不存在任何对麦可思数据做效度检验或与行政数据交叉验证的学术研究」属否定性命题，本次 WebSearch 额度耗尽无法穷尽复核，建议行文写「未检索到」而非「不存在」。


#### [G55] CORRECTED · confidence=high

**修正**:论断B的归因需要收紧。原表述：「2026 年媒体通稿把红牌改写为『……市场需求端呈现减少或增长缓慢趋势……』——『失业量较大』这一原始首要判据被替换掉了」，标题作「定义在传播中被偷换」。→ 正确表述：「2026 年公开传播中的红/绿牌定义已普遍不含『失业量』；但因未能取得《2026 年中国本科生就业报告》原书，无法判定改写发生在麦可思发布环节还是媒体转述环节，不应断言为『传播中被偷换』。」理由：我核到的三家 2026 年报道给出的是三套彼此不同的措辞——搜狐「就业落实率、薪资水平与就业满意度等方面综合表现相对较低，同时在市场需求端呈现减少或增长缓慢趋势」、新浪财经「就业落实率、薪资和就业满意度综合较高，且市场需求增长的专业」、网易「就业质量持续较高，且产业需求增长的专业」。措辞各异更像各家改写，但三家一致丢掉「失业量」也可能是原书已改口径，两种可能无法排除。对准大学生而言「谁改的口径」影响是否该信任榜单本身，必须留白而非坐实。

**核验依据**:一手 PDF 第44页（我抽取文本第4343-4351行）逐字核对论断A，与采集者所引完全一致，一字不差：「红牌专业指的是失业量较大，毕业去向落实率、薪资和就业满意度综合较低的专业。黄牌专业指的是除红牌专业外，失业量较大，毕业去向落实率、薪资和就业满意度综合较低的专业。绿牌专业指的是失业量较小，毕业去向落实率、薪资和就业满意度综合较高的专业，为需求增长型专业。」——「失业量」确为首要判据。论断D逐字命中：「部分近年来新增数量较多的专业（如人工智能、数据科学与大数据技术、机器人工程）由于尚无成规模、成趋势的毕业生就业数据，暂未包括在内。」论断C：我在全书 20,809 行独立检索「权重」「阈值」「算法」——三词均 0 命中，确无任何一版公开权重或阈值，四判据的合成规则不可复现，属实。论断B措辞本身核到：https://www.sohu.com/a/1041564081_121294 逐字给出「红牌专业主要指在就业落实率、薪资水平与就业满意度等方面综合表现相对较低，同时在市场需求端呈现减少或增长缓慢趋势的专业」，确无「失业量」；2026 本科红牌六个（绘画、音乐表演、美术学、文化产业管理、劳动与社会保障、城乡规划）亦一致。论断E时间线核实：2023 版书内白纸黑字写机器人工程「暂未包括在内」，而 https://www.sohu.com/a/966574848_121123712 载 2025 年（2024届）本科绿牌为「电气工程及其自动化、微电子科学与工程、机械电子工程、新能源科学与工程、车辆工程、机器人工程」——机器人工程确已入榜，两年内从「无数据故豁免」变为「绿牌」，规则变更无说明，E 成立。论断F（无回溯效度检验）因 WebSearch 额度耗尽未能穷尽复核，建议同样写「未检索到」。


#### [G56] CORRECTED · confidence=high

**修正**:论断A的五年绿牌序列有实质错误，五列中四列错，必须整体替换。我用 pdftotext -bbox 取出表12-7（PDF 第211页）每个词的 x 坐标来判定归属列（列心：2023≈67-87，2022≈145-161，2021≈217-225，2020≈272-292，2019≈352-361），结果如下——原表述 → 正确表述：
2019：原「信息安全、软件工程、网络工程、物联网工程、数字媒体技术、电气工程及其自动化」→ 正确「信息安全、软件工程、网络工程、物联网工程、数字媒体技术、通信工程、数字媒体艺术」（7 个；该列无电气工程及其自动化）
2020：原「信息安全、软件工程、信息工程、网络工程、计算机科学与技术、数字媒体技术」→ 正确「信息安全、软件工程、信息工程、网络工程、计算机科学与技术、数字媒体艺术、电气工程及其自动化」（7 个；是数字媒体艺术不是数字媒体技术）
2021：原「信息安全、软件工程、信息工程、网络工程、数字媒体技术、数字媒体艺术」→ 正确「信息安全、软件工程、信息工程、网络工程、数字媒体技术、电气工程及其自动化」（末位是电气工程及其自动化）
2022：原「信息安全、网络工程、信息工程、微电子科学与工程、数字媒体技术、能源与动力工程、电气工程及其自动化」→ 正确「信息安全、网络工程、信息工程、微电子科学与工程、数字媒体技术、能源与动力工程」（6 个；无电气工程及其自动化）
2023：不变（信息工程、微电子科学与工程、电气工程及其自动化、能源与动力工程、道路桥梁与渡河工程、机械电子工程）✓
交叉校验证明我的版本对、采集者版本错：书内自述「近五年进入绿牌名单的专业共 14 个」与「数字媒体技术（3 次）」。我的版本恰为 14 个不重复专业、数字媒体技术恰 3 次（2019/2021/2022）；采集者版本只有 13 个、数字媒体技术 4 次，与书内自述自相矛盾。
另两处降级：955 所/661 所未获证实（我检到的一个来源称计算机科学与技术开设院校 834 所，未含独立学院），「毕业五年后月收入 14,090 元居主要专业类第一」亦未取得任何一手或可靠二手确认——这两个数在文中应删除或标注未核。「十五年前」宜改「约十六年前」（2010 年报告基于 2009 届）。

**核验依据**:表12-7 一手核对：我不信任 pdftotext 的文本流顺序（它把表格按行跨列打散），改用 pdftotext -bbox 抽词级坐标重排，逐格确认。跨行折行的「电气工程及其/自动化」x=217.1/228.3 落在 2021 列；末行「电气工程及其自动化」x=272.5 落在 2020 列、「数字媒体艺术」x=352.8 落在 2019 列。书内两句自述（PDF 第210-211页）作为独立校验：「近五年被列为绿牌专业次数最多的是网络工程、信息安全、信息工程（均为 4 次），其后是电气工程及其自动化、软件工程、数字媒体技术（均为 3 次）」「近五年进入绿牌名单的专业共 14 个，其中网络工程、信息安全、软件工程、数字媒体技术、物联网工程、计算机科学与技术 6 个专业均属于计算机类专业」——我的重排在 14 个总数、各专业次数上全部对得上，采集者版本对不上。论断B（本篇最有力论据）我按要求回到两个独立来源核实并且成立：https://gaokao.haedu.cn/zyjd/2010/0513/89406.html（2010-05-13，与蓝皮书发布同期）给出本科红牌十个「动画、法学、生物技术、生物科学与工程、数学与应用数学、体育教育、生物工程、计算机科学与技术、英语、国际经济与贸易」，含计算机科学与技术与国际经济与贸易；另一独立聚合源（新浪博客 blog_a5e122a60101cnpa）给出 2010、2011 两年同一名单，且称 2012 年计算机科学与技术已退出。中国新闻网 2015-08-11（https://www.chinanews.com.cn/m/gn/2015/08-11/7459393.shtml）第三方佐证：六年预警榜中法学与生物工程年年上榜，计算机科学与技术共上榜 3 次，并明确「2011 年榜单与 2010 年相同」。反证排查：新浪教育 2010-10-26 一篇给出的本科红牌名单不含计算机科学与技术（含音乐表演、动物医学），但该页正文我未能取到原文（curl 超时，仅得摘要器输出且其自述「未在摘录中逐项列出」），可靠性低于上述三源，故不推翻 B。论断C：82.4%、61 个主要专业类倒数第 11、本科平均 86.7%、历史学类 87.2%、外国语言文学类 86.9% 由多个转述源一致指向《2025 年中国本科生就业报告》，且相互独立；采集者确未取得原书，行文须标「转述」。「首次跌出本科月收入前十、榜首微电子科学与工程 7,814 元」获多家一致确认（羊城晚报、第一财经、新浪财经、国际电子商情），2026 前十为微电子科学与工程、电子科学与技术、自动化、信息安全、光电信息科学与工程、采矿工程、机械工程、测控技术与仪器、材料科学与工程、通信工程。「落实率含升学不是纯失业指标」经一手证实：2023 版书第9页毕业去向七分类明确把「国内外读研」与「受雇工作」并列计入。「两面呈现」在一手中也成立：表12-6 载计算机类 2022 届月收入 6863 元 vs 本科平均 5990 元。


#### [G57] REFUTED · confidence=high

**修正**:三条全部判为禁用，我独立溯源同样失败，且其中两条另发现实质性硬伤。
(a)「计算机类对口率 2020 届 76% → 2024 届 62%」→ 禁用。除溯源失败外补充两点证伪材料：其一，麦可思体系内该指标的正式名称是「工作与专业相关度」，不叫「对口率」，混用本身提示转述链失真；其二，一手数据与该曲线不符——2023 年报告表12-6 载计算机类 2022 届工作与专业相关度为 77%（本科平均 74%），若 2020 届为 76%，则 2022 届仍在 77% 高位，要在两年内跌到 62%（-15 个百分点）属异常断崖，无任何一手支撑。
(b)「1 个岗位 17.2 份简历／投 150-200 份换 1 次面试／offer 率不足 8%」→ 禁用。量级冲突经我一手核实成立：智联《大学生就业力调研报告》口径逐字为「截至 4 月中旬，在有求职计划的应届毕业生中，47.8% 已获得 offer」，分母是「有求职计划的应届毕业生（人）」；而「不足 8%」若成立只可能是「简历投递→offer」的份次转化率，分母是简历份数。两者分母一个是人、一个是简历份数，不可互换，把后者说成「offer 率」并与官方口径并列传播即是分母偷换。原文出处为新浪财经转载自媒体文《2026 年，1270 万毕业生的天崩开局》（2026-05-23），归因「智联招聘的数据」但无报告名、无页码，不可承重。
(c)「多地教师招聘缩减 50%+／竞争比 200:1」→ 禁用。我未能取到任何省级教育厅/人社厅招聘计划汇总一手数据，仅见自媒体与境外中文媒体，无法承重。

**核验依据**:(a) 我在一手 PDF 全书检索未见任何 76%/62% 组合；本次能做的外部检索（Bing/DuckDuckGo/Mojeek/Sogou 多引擎，含精确串）均未返回任何含该组合的页面（多数引擎对中文长查询返回不相关结果或反爬拦截）。反向证伪来自一手：report2023.txt 第17869行「机类专业的 2022 届本科毕业生，毕业半年后月收入为 6863 元，工作与专业相关度……」及表12-6「工作与专业相关度 计算机类 77 / 本科平均 74」。(b) 智联口径我取到逐字原文：「截至4月中旬，在有求职计划的应届毕业生中，47.8%已获得offer」，并核到 2023 年 50.4%、2022 年 46.7%、大专 56.6% 的历年序列，确认 45%-50% 量级与「不足 8%」相差近六倍，只可能是不同分母。该口径同时反证：因分母限定为「有求职计划者」，已排除升学/考公备考/慢就业人群，故它既不能反推就业率，也不能与「简历转化率」并列。(c) 未取到任何省级官方汇总，判 UNVERIFIABLE 级别证据不足以支撑写入面向准大学生的文章，按本批规则归入禁用。说明：本次 WebSearch 额度（200 次）在核验中途耗尽，(a)(c) 的外部检索改由 WebFetch 打搜索引擎完成，覆盖面弱于正常检索；但三条均无一手，禁用结论不受影响。


#### [G58] CORRECTED · confidence=medium

**修正**:构念警告全部成立、论断A获一手证实，但论断B、C的具体数字我未能取得任何原始报告核对，须降级标注。
论断A → 维持，并可加强：分母口径已逐字坐实为「在有求职计划的应届毕业生中」，因此「不能反推就业率」这一判断可以写死。
论断B → 原表述把「TOP50 高薪专业中 43 个为工学／TOP50 高薪院校中 47 所为双一流／机器人 83.8%、新材料 60.1%、人工智能 24.4%」作为既有事实陈述 → 应改为「据智联招聘 2026-06-16 发布的《大学生就业前景研判及高考志愿填报攻略》（未取得原始报告，转述）」，或整段删除。我尝试的路径均未取得该报告原文或可核对的转述。
论断C → 猎聘「电子商务 1165.94%、银行 251.39%、保险 145.74%、人工智能 57.98%」同样未取得一手，应标注为未核转述。但对这组数字的构念批评本身无需数字为真即成立，可保留为方法论提醒。
另建议补一句更硬的构念表述：智联「薪资」来自岗位挂出薪资/平台简历薪资（要约端），麦可思「月收入」来自毕业生自报实得（实现端），两者在同一篇文章中并列或相减都会产生伪结论。

**核验依据**:论断A的关键——分母——我取到逐字原文并确认：「截至4月中旬，在有求职计划的应届毕业生中，47.8%已获得offer」，调查时点为 3 月下旬至 4 月中旬（春招中期），与采集者描述一致；历年 2023 年 50.4%、2022 年 46.7%、分学历大专 56.6%/本科 45.4%/硕博 44.4% 亦与其一致。该分母确实排除升学、考公备考、慢就业者，故「不能反推就业率」成立。样本量/抽样方式/院校层次配额：我在能触及的所有转述中均未见任何一处披露有效样本量或抽样设计，与「未公开」相符（但这是否定性命题，且我未能取得原始 PDF，故置信度只给 medium）。论断B：我尝试 https://www.sohu.com/a/1044183808_121117449 等路径，该文实际只引用百度热搜高考大数据（采集时间 2026-06-30）与麦可思《2026 年中国本科生就业报告》，并不含智联的 43 个工学/47 所双一流/83.8%/60.1%/24.4% 任何一项，且全文无方法论、样本规模、统计周期说明——这与采集者「原文未提供完整的方法论说明」的结论方向一致，但我没能定位到承载这些数字的原始智联报告。论断C：猎聘四个数字我未取得一手，水滴/登录墙未突破。构念判断本身我认为准确且可独立于数字成立：招聘挂出薪资是要约端价格、毕业生自报月收入是实现端价格，二者构念不同；院校薪酬排行的分母是该校在该平台的投递/被录用者，平台用户结构失衡会系统性抬高名校排名；1165.94% 这类增速在低基数下几乎必然产生，且分母（上年该行业在猎聘的新发职位数）确未见披露，不能读作行业真实用工增长。


#### [G59] CORRECTED · confidence=high

**修正**:实质内容成立，但有三处必须修正，其中两处涉及可核查性与完整性。
1. 出处 URL 错误。原表述引 https://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202308/t20230804_1072471.html → 正确为 http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202308/t20230804_1072396.html 。原 URL 在教育部站上返回「页面不存在!」，且 Wayback 无任何快照（该 URL 从未存在），照抄会让读者无法自核。
2. 「四不准」表述不完整。原文规定是「『四不准』『三不得』规定」，采集者只列四不准、完全略去三不得。三不得逐字为：「不得不切实际向高校和学院提去向落实率具体指标；不得层层加码向辅导员摊派就业任务；不得将单一的去向落实率指标与就业工作人员或者辅导员的绩效考核、评优等挂钩」——这三条恰恰是官方自陈「造假压力来自指标层层加码」的证据，对本篇论证的价值高于四不准，漏掉是实质损失。另第四条逐字为「不准将毕业生顶岗实习、见习证明材料作为就业证明材料」，原表述漏「毕业生」二字。
3. 论断C的一手未取到。教学厅函〔2021〕19 号所谓「每年 9 月初，教育部委托国家统计局开展毕业生就业状况抽样调查，结果将向各地通报」一句，我在教育部政府信息公开该栏目 2021 年全部文件中未能定位到 19 号文本身 → 应改为「据教学厅函〔2021〕19 号（该文未见于教育部政府信息公开栏目，转引自二手）」，或改用已核实的 2023-08-04 新闻稿中『8 月起，还将委托国家统计局和第三方调查机构在全国范围内开展 2023 届高校毕业生去向落实情况抽样调查』这句作为「制度化存在」的证据——这句我已逐字核实，足以支撑论点，不必依赖 19 号。
4. 论断E的归因需精确化。原推定「官方含编码 12 而麦可思算作受雇全职」→ 更准确的机制是：麦可思「灵活就业」按其自身定义仅由受雇半职 1.4% + 自由职业 2.0% + 自主创业 1.2% 三项构成，受雇全职工作（周 32 小时以上）被整体排除在灵活就业之外；叠加麦可思该数为本科口径、官方 16.9%/16.25% 为含高职高专的全口径，两项即可解释大部分差距。官方 16.9%/16.25% 我未取得一手，须标注。

**核验依据**:论断A：教育部原页现已 404，我通过 Wayback id_ 原始快照取回全文（http://web.archive.org/web/20230806104110id_/http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202308/t20230804_1072396.html），标题《教育部派出工作组赴各省开展专项核查 严查高校毕业生就业数据弄虚作假》，日期 2023-08-04，来源教育部。逐字命中：「对经核实存在虚假签约、虚假证明等违规行为的，责成有关部门依规依纪严肃处理，并追究相关高校和人员责任，切实维护高校毕业生就业合法权益。」（采集者引文止于「责任」，后半句被截断）；「重点核查灵活就业等相关数据，以『零容忍』的态度严肃查处就业违规行为」；「8月起，还将委托国家统计局和第三方调查机构在全国范围内开展2023届高校毕业生去向落实情况抽样调查。」原文明写「严格执行就业工作『四不准』『三不得』规定」并完整列出七条。论断C：我用 Wayback CDX 遍历 moe.gov.cn/srcsite/A15/s3265/2021* 全目录，逐份打开核对发文字号，取到 12 号、15 号、17 号、20 号、21 号、22 号、31 号，未见 19 号；教育部现网两个候选 URL 均返回「页面不存在!」。故 19 号引文无法回到一手，判该子项证据不足。论断D：一手期刊页（https://xbjk.ecnu.edu.cn/CN/10.16382/j.cnki.1000-5560.2023.09.010）确认为岳昌君、冯沁雪、辛晓佳、邱文琪《中国高校毕业生就业趋势研究报告：来自2003—2021年调查数据》，《华东师范大学学报（教育科学版）》2023 年第 41 卷第 9 期第 138-154 页；表2 三数全中：已落实 76.5%、升学 33.0%、已确定单位 32.1%；2021 年样本 34 所高校、20,269 人，落在采集者所述 28-45 所、15,060-21,753 人区间内。论断E 麦可思侧一手命中（PDF 第134页）：「2022 届有 4.6% 的本科毕业生在毕业半年后选择灵活就业，其中包括 1.4% 选择受雇半职工作，2.0% 选择自由职业，1.2% 选择自主创业。」同书第9页毕业去向定义：「受雇工作包含受雇全职工作、受雇半职工作，受雇全职工作指平均每周工作 32 小时或以上」——据此可确证麦可思灵活就业不含受雇全职，这是口径撕裂的主因。官方 16.9%/16.25% 我未取得一手。论断B（承认有假、未公布查出多少假）：我未检索到任何点名通报或处理结果公告，与采集者一致，但因 WebSearch 额度耗尽无法穷尽复核，建议行文写「未见公开通报」而非「不存在」。


### 第 2 席


#### [G54] CORRECTED · confidence=high

**修正**:【必改·财务口径】原表述「2018 年主营业务收入 110,752,232.01 元，其中『数据监测类收入』96,886,518.62 元（占营业收入 85.36%），『咨询类收入』16,615,311.32 元（14.64%）」→ 正确表述：「2018 年营业收入 113,501,829.94 元（主营业务收入 110,752,232.01 元 + 其他业务收入 2,749,597.93 元），其中数据监测类 96,886,518.62 元占 85.36%、咨询类 16,615,311.32 元占 14.64%」。两个分项之和恰为 113,501,829.94，即营业收入，而非主营业务收入——原句用「主营业务收入…其中…」把分子挂在了错误的分母下。毛利率 87.39%、王伯庆 690.00 万股 /61.61%、「累计合作 706 所、正在执行签约项目 569 所」「高校、院系/专业、教育厅/局等机构」均逐字无误。

【必加·利益标注】该财务数据的载体是《新三板智库》2019-11 的卖方式专题研究报告（报告自述数据「资料来源：公司年报」，正文含「风险提示」「客户不应以本报告取代其独立判断」等免责条款）。引用时应写明「据新三板智库研究报告转引公司年报」，不宜写成「麦可思年报显示」。

【B/C/D/E 全部逐字成立，且可加强】技术报告第 207–209 页原文逐字核对通过：「全国本科生样本为 13.5 万人。覆盖了 428 个本科专业，覆盖了全国 30 个省、自治区和直辖市」「不包括成人高等教育、军事院校和港澳台院校的毕业生」「以电子邮件方式发放答题邀请函、问卷客户端链接…答题时间为 10~30 分钟」「未被邀请的答题被视为无效」「本研究对答题和未答题的样本进行了检验，没有发现存在自我选择性样本偏差问题（Self-selection Bias）」「本研究采用权数加以修正（即对回收的全国总样本，基于学历、地区、院校类型、专业的实际分布比例进行再抽样）」，附表 1 东部 38.5%/38.5%、中部 26.7%/26.7%、西部 25.4%/25.4% 逐字一致。我在同一份 20,809 行提取文本中检索「回收率/应答率/答题率/回复率/响应率/邀请函发放」——除「以电子邮件方式发放答题邀请函」一句外零结果，缺口属实。

【可新增的更硬证据】全书 235 页中「客户」二字仅出现一次，且是「问卷客户端」；「委托」「合作高校」「付费」「签约高校」零命中。即：这本书里连「高校是麦可思付费客户」这件事的字面痕迹都不存在，「未见披露」不是「找得不细」，是文本级为零。

【采集者限定语必须保留】「客户=样本源」仍只是结构性风险提示；我同样未找到任何证据表明样本仅取自其签约高校。

【另一处可写但采集者未提】技术报告称加权用的「本科毕业生的实际分布比例来自中华人民共和国国家统计局网站」——本科分专业/分院校类型的实际分布通常出自教育部教育统计，此处基准来源标注本身存疑。

【学术效度检验】我未找到任何将麦可思数据与行政数据交叉验证或做效度检验的公开学术研究，与采集者一致；但受本次检索预算限制，这一条只能记为「未找到」，不能写成「不存在」。

**核验依据**:新三板智库《麦可思（833861.OC）：中国高教管理数据与咨询产业的领军者》PDF 全文提取，https://pdf.dfcfw.com/pdf/H3_AP201911121370658000_1.pdf —— 图表3「营业收入概览」：主营业务收入 110,752,232.01 / 其他业务收入 2,749,597.93 / 毛利率 87.39%；图表4「分主营业务收入」：数据监测类 96,886,518.62（占营业收入 85.36%）、咨询类 16,615,311.32（14.64%）；图表1 主要股东：王伯庆 690.00 万股、61.61%；正文「公司于 2015 年 10 月上市，股票代码为 833861」「在中国教育部门批准 2500 所高校中累计合作 706 所，正在执行签约项目的 569 所，其中服务年限在三年以上的客户占比为 83%」「公司直接面对高校、院系/专业、教育厅/局等机构客户提供产品和解决方案」。

《2023 年中国本科生就业报告》技术报告 PDF（235 页，Adobe InDesign CS6 生成，创建于 2023-06-13），https://xiuzhenorgweb.oss-cn-zhangjiakou.aliyuncs.com/uploads/files/20231127/cc79a43039780361b3bfe6540f797713.pdf —— 书页 207「（一）评价覆盖面」、208「（二）评价对象/（三）评价方式/二 研究概况/（二）研究样本」、209「附表 1」，均已用 pdftotext -layout 与 -bbox 双路核对。全书「回收率」「应答率」「答题率」检索为 0；「客户」仅命中「问卷客户端」1 处。


#### [G55] CORRECTED · confidence=high

**修正**:【A 逐字成立】第 44 页原文一字不差：「红牌专业指的是失业量较大，毕业去向落实率、薪资和就业满意度综合较低的专业。黄牌专业指的是除红牌专业外，失业量较大，毕业去向落实率、薪资和就业满意度综合较低的专业。绿牌专业指的是失业量较小，毕业去向落实率、薪资和就业满意度综合较高的专业，为需求增长型专业。」后接「红黄绿牌专业反映的是全国总体情况，各省区、各高校情况可能会有差别」——这句限定语建议一并引用，它本身就是「不可外推到个人」的官方自认。

【B 需修正归属，且修正后更有力】原表述「2026 年**媒体通稿**把红牌改写为…」→ 正确表述「2026 年**麦可思自家发布口径**把红牌改写为…」。搜狐该文页面标注「稿件来源：麦可思研究」、发布日期 2026-06-25，即改写发生在麦可思自己的传播渠道，不是外部媒体转述失真。经核，该文全篇不出现「失业量」三字，红牌被重新定义为「在就业落实率、薪资水平与就业满意度等方面综合表现相对较低，同时在市场需求端呈现减少或增长缓慢趋势的专业」——首要判据被替换为「市场需求端趋势」。这是发布方自己换掉了自己的定义。

【C 成立，且可大幅加强】原表述「四个判据没有任何权重、阈值、排序规则」→ 建议升级为「全书 235 页中，『权重』『阈值』『评定标准』三词命中数均为 0；『失业量』全书仅出现 4 次（第 44 页定义段 3 次、第 195 页概述 1 次），且**从未被定义**——技术报告与名词解释里有『毕业去向落实率』『工作与专业相关度』『就业满意度』的分子分母公式，唯独『失业量』没有任何计算口径」。也就是说，红黄绿牌的第一判据本身是一个未定义量。

【D 逐字成立】第 44 页原文：「红黄绿牌专业是基于各专业连续多年应届毕业生就业质量变化趋势综合判断的，部分近年来新增数量较多的专业（如人工智能、数据科学与大数据技术、机器人工程）由于尚无成规模、成趋势的毕业生就业数据，暂未包括在内。」

【E 部分成立，需降级表述】2023 版「机器人工程…暂未包括在内」已一手确认；「2025 版（2024 届）机器人工程直接进了绿牌」我未取得 2025 版原书，仅有二手转述与 2026 版报道的间接印证。建议写成「据公开报道，机器人工程在 2025 版榜单中已出现在绿牌名单」，并保留「规则变更未见说明」的判断（我同样未找到任何说明）。

【F】我亦未找到任何对红黄绿牌预测效度的回溯检验研究；受检索预算限制记为「未找到」，不宜写成「不存在」。

**核验依据**:《2023 年中国本科生就业报告》技术报告 PDF 第 44 页「四 专业预警分析」逐字提取（同上 aliyuncs 链接）。全书检索：「权重」0 命中、「阈值」0 命中、「评定标准」0 命中、「计算公式」6 命中但均属满意度/晋升次数/满足度等其他指标；「失业量」4 命中（行 4343、4344、4345、18004），无一处给出定义或算法。第 195 页原文另证：「已连续十余年根据失业量、毕业去向落实率、薪资和就业满意度等就业指标，综合评价筛选出需求增长型和预警专业」——同样只列指标不给权重。

B 的改写：https://www.sohu.com/a/1041564081_121294 ，页面标注发布 2026-06-25、稿件来源「麦可思研究」，红牌定义为「在就业落实率、薪资水平与就业满意度等方面综合表现相对较低，同时在市场需求端呈现减少或增长缓慢趋势的专业」，2026 年本科红牌名单：绘画、音乐表演、美术学、文化产业管理、劳动与社会保障、城乡规划；全文无「失业量」。


#### [G56] CORRECTED · confidence=high

**修正**:【重大错误·必须整段替换】论断 A 的「近五年绿牌序列」有 4 个年份抄错。我用 pdftotext -bbox 取出表 12-7 每个单元格的 x 坐标做列归属（列心：2023≈98、2022≈172、2021≈236、2020≈303、2019≈371），并用书内自述交叉校验，正确的表 12-7 如下：
2019 年（7 个）：信息安全、软件工程、网络工程、物联网工程、数字媒体技术、**通信工程**、**数字媒体艺术**
2020 年（7 个）：信息安全、软件工程、信息工程、网络工程、计算机科学与技术、**数字媒体艺术**、**电气工程及其自动化**
2021 年（6 个）：信息安全、软件工程、信息工程、网络工程、数字媒体技术、**电气工程及其自动化**
2022 年（6 个）：信息安全、网络工程、信息工程、微电子科学与工程、数字媒体技术、能源与动力工程（**无**电气工程及其自动化）
2023 年（6 个）：信息工程、微电子科学与工程、电气工程及其自动化、能源与动力工程、道路桥梁与渡河工程、机械电子工程（仅此年与原稿一致）
逐项对照原稿的错误：2019 年误加「电气工程及其自动化」、漏「通信工程」「数字媒体艺术」；2020 年误加「数字媒体技术」、漏「数字媒体艺术」「电气工程及其自动化」；2021 年把「电气工程及其自动化」误写成「数字媒体艺术」；2022 年误加「电气工程及其自动化」。
校验依据（内证）：书内自述「近五年被列为绿牌专业次数最多的是网络工程、信息安全、信息工程（均为 4 次），其后是电气工程及其自动化、软件工程、数字媒体技术（均为 3 次）」「近五年进入绿牌名单的专业共 14 个」。按我的读法，三者各 4 次、后三者各 3 次、去重恰为 14 个，全部自洽；按原稿的读法，数字媒体技术变成 4 次、去重只有 13 个，与书内自述冲突。原稿版本可直接判为抄错。

【顺带一处可加的强化】书内紧接着写「其中网络工程、信息安全、软件工程、数字媒体技术、物联网工程、计算机科学与技术 6 个专业均属于计算机类专业」——即麦可思自己认定近五年绿牌名单里有 6 个是计算机类。这句配上 2026 版计算机类全线出榜，比原稿的名单罗列更有力。

【B 关键论据：成立，但须写清证据等级】「2010–2011 年本科红牌名单含计算机科学与技术」经三条独立线索交叉确认：①《中国青年报》2015-08-11「近六年被亮红牌最多专业」（人民网转载，Wayback id_ 快照）逐字写「计算机科学与技术、国际经济与贸易、美术学 3 次上榜」，并写「2011 年的预警榜与前一年相比，『红牌』专业从类目到排序均一模一样」；②百度百科「红牌专业」词条称「计算机专业在 2009 年至 2011 年连续被列为红牌专业」；③多份 2010/2011 年名单转载（含新浪博客 2010/2011/2012 三年对照、2011 年当年新闻转载）给出的 2010、2011 本科红牌十专业完全一致：动画、法学、生物技术、生物科学与工程、数学与应用数学、体育教育、生物工程、计算机科学与技术、英语、国际经济与贸易。**但我未取得 2010/2011 年蓝皮书原书**，均为转述。建议行文写「据《中国青年报》2015 年对麦可思历年榜单的统计与多份当年名单转载」，不要写成「麦可思原书载明」。
【B 另需补的一句关键限定】当年红牌是「失业量较大、就业率较低、薪资较低的专业中的**前 10 个**」——它是一份按绝对失业人数排的 Top10。计算机科学与技术当年（及今天）都是全国招生规模最大的专业之一，「失业量」判据对大专业有机械性偏置。这一点不削弱「蛛网会反转」的论点，反而把「红牌≠该专业不好」讲得更准确，且直接呼应 G55 的「失业量从未被定义」。

【C 需两处口径修正】
① 原表述「计算机类『毕业五年后月收入 14,090 元仍居主要专业类第一』」→ 正确表述「计算机类**2019 届**毕业生**毕业五年后**（2024 年调查）月收入 14,090 元，居本科主要专业类第一（电子信息类 13,584 元次之）」。该数出自《2025 年中国本科生就业报告》的五年后跟踪部分，届别与同文并列的 82.4%（2024 届半年后）不是同一批人，行文若不写清届别会让读者误以为是同一群毕业生的两面。另需注意：麦可思 2026-07 已发布 2020 届五年后数据（电子信息类 13,992 元、能源动力类 13,022 元），14,090 元这个「第一」已是上一版口径。
② 82.4% / 倒数第 11 / 61 个主要专业类 / 全国本科平均 86.7% / 历史学类 87.2% / 外国语言文学类 86.9%：多家媒体（新浪财经、DoNews 等）与 AI 摘要口径完全一致且内部自洽（86.7−82.4=4.3 个百分点），但**全部为对《2025 年中国本科生就业报告》的转述，我同样未取得原书**，与采集者情况相同。建议标注「据媒体转述的《2025 年中国本科生就业报告》数据」。
③「落实率含升学，不是纯失业指标」——一手可证：技术报告第 12 页「毕业去向落实率＝已就业本科毕业生数/本科毕业生总数。其中已就业人群包括『受雇工作』、国内外读研等五类」。建议直接引这句原文，比转述更硬。

【C 供给侧数字需加时间戳并修一处】原表述「开设计算机科学与技术的高校 955 所、软件工程 661 所，两专业毕业生规模均在 10 万人以上」→ 正确表述「截至 2025 年 11 月（教育部阳光高考平台口径），开设计算机科学与技术的高校 955 所、软件工程 661 所」。两点问题：(a) 该数在漂移——2026 年 6 月「掌上高考」已列 960 所；(b)「毕业生规模均在 10 万人以上」在来源中就有分歧，部分转述写的是「两个专业每年的毕业生**总数合计**超过 10 万人」，与「**均**在 10 万人以上」量级差一倍。建议只保留「两专业年毕业生规模合计逾 10 万人」这一各来源都支持的下限说法。

【2026 版名单核对通过】2026 年本科绿牌六个全为工科：电气工程及其自动化、微电子科学与工程、自动化、能源与动力工程、车辆工程、新能源科学与工程；自动化首次入榜；微电子连续五年在榜；红牌：绘画、音乐表演、美术学、文化产业管理、劳动与社会保障、城乡规划；计算机科学与技术、软件工程首次跌出 2025 届本科月收入前十，榜首微电子科学与工程 7,814 元（电子科学与技术 7,752 元次之），2025 届本科平均月收入 6,435 元。

**核验依据**:表 12-7 一手坐标级核对：pdftotext -bbox -f 211 -l 211 输出，各单元格 xMin 与表头列心对齐结果为（y=268/280）「电气工程及其/自动化」x=217/228→2021 列；（y=274）机械电子工程 x=79→2023、能源与动力工程 x=150→2022、数字媒体艺术 x=284→2020、通信工程 x=360→2019；（y=295）电气工程及其自动化 x=272→2020、数字媒体艺术 x=353→2019。书内自述见第 195 页。

2010/2011 红牌：《中国青年报》2015-08-11《近六年被亮红牌最多专业：法学生物工程居首》，Wayback id_ 快照 http://web.archive.org/web/20151013211116id_/http://edu.people.com.cn/n/2015/0811/c244541-27442023.html ，原文「在过去 6 年的预警榜上，法学和生物工程年年都属于『红牌』专业…计算机科学与技术、国际经济与贸易、美术学 3 次上榜」「2011 年的预警榜与前一年相比，『红牌』专业从类目到排序均一模一样」；名单转载 https://blog.sina.com.cn/s/blog_a5e122a60101cnpa.html ；百度百科「红牌专业」词条 https://baike.baidu.com/item/红牌专业/5830558 。

落实率定义：技术报告第 12 页原文（同 aliyuncs 链接）。2026 版数据：https://news.qq.com/rain/a/20260706A03ET100 、https://finance.sina.com.cn/roll/2026-06-11/doc-iniazyem3923536.shtml 。955/661：多篇 2025-11 起的报道均标注「教育部阳光高考平台，截至 2025 年 11 月」；掌上高考 2026-06-28 列 960 所。


#### [G57] CORRECTED · confidence=high

**修正**:三条不能一刀切禁用。逐条判：

【(a) 判 CORRECTED——采集者溯源失败，但源头存在】原表述「计算机类专业对口率从 2020 届 76% 降至 2024 届 62%（五年降 14 个百分点）」→ 正确表述「**计算机科学与技术专业**的工作与专业相关度从 2020 届 76% 降至 2024 届 62%，下降 14 个百分点（麦可思研究《别了，专业对口！》2026-05-12）」。错在把**一个专业**说成**一个专业类**。同一篇给出的整组数是：计算机科学与技术 −14pp（2024 届 62%／2020 届 76%）、软件工程 −13pp（65%／78%）、信息安全 −10pp（69%／79%）、网络工程（64%／73%）、物联网工程（58%／67%）。
**计算机类（专业类）另有一组不同口径的数**：《2026 年中国本科生就业报告》——计算机类 2025 届工作与专业相关度 62%，较 2021 届 78% 下降 16 个百分点，低于 2025 届工学门类平均 70%；同报告计算机类 2025 届月收入 6,897 元，已低于工学门类平均 7,033 元。两组数「终点都是 62%」，极易被混着用，行文必须二选一并写明主语与届别。
**另须补一句分母**：麦可思「工作与专业相关度」的一手定义（2023 技术报告）为「受雇全职工作并且与专业相关的毕业生人数 / **受雇全职工作的毕业生**人数」，分母是已受雇全职者，不是全体毕业生，也不是行政意义上的「对口就业率」。用「对口率」三字会让读者以为分母是全体毕业生。

【(b) 判 REFUTED——禁用】「1 个岗位 17.2 份简历／投 150–200 份换 1 个面试／offer 率不足 8%」我从三个角度独立追溯（精确串检索、智联报告名逐一比对、沿转载链上溯至最早出现日期），所有出处一律是「智联招聘的数据」「智联招聘和多家机构联合发布的报告」这类无名报告、无发布日、无页码的自媒体表述，最早可见 2026-03 的 CSDN 博文与 2026-05 的新浪财经转载，**不存在任何可指名的智联报告**。同一批文章内部还在滚雪球：同组数字有写成「热门岗位竞争比突破 2000:1」「文科专业供需比 1:42」「热门赛道 60:1」的。
**量级冲突证实成立，且比采集者说的更尖锐**：新浪同一篇文章里，「最终 offer 率不足 8%」与「今年春招专科生的 offer 率是 56%，反而高于本科生的 45% 和硕博生的 40%」并排出现——**同一篇稿子里两个相差 6 倍的「offer 率」被当成同一件事**。智联自身口径已一手确认：《2024 大学生就业力调研报告》调研期 2024 年 3 月下旬至 4 月中旬，「截至 4 月中旬，在有求职计划的应届毕业生中，47.8% 已获得 offer」。

【(c) 判 CORRECTED——采集者结论应推翻，一手确实存在】原表述「多地教师招聘缩减 50%+…未追到任何省级官方招聘计划数据」→ 正确表述「湖北省中小学教师公开招聘计划从 2025 年的 5,799 名降至 2026 年的 2,740 名，减少 52.8%」，**两个数都出自省级官方招聘公告**：《湖北省 2025 年中小学教师公开招聘公告》（湖北省教育厅、湖北省人力资源和社会保障厅，2025-03-13，湖北日报同日全文转载）「2025 年面向社会公开招聘 5799 名中小学教师」；《湖北省 2026 年中小学教师公开招聘公告》（湖北省教育厅，2026-04-15）「2026 年面向社会公开招聘 2740 名中小学教师」。2740/5799 = 47.25%，降幅 52.75%，与流传的 52.8% 吻合。江西 2023 年 7,821 名→2026 年 1,190 名（降 84.8%）目前只有媒体转述，需回江西省教育厅原公告后才可用。
**必须加的口径限定**：这是**省级统一公开招聘计划数**，不含特岗计划、公费师范生履约、市县自主招聘与编外聘用，因此只能写「湖北省统招计划腰斩」，不能写「湖北教师招聘总量减半」。
**「竞争比 200:1」判 REFUTED（禁用）**：三个角度均未追到任何省级人社/教育部门的报名与计划比数据，仅见自媒体。

**核验依据**:(a) 麦可思研究《别了，专业对口！》2026-05-12，原文「以计算机类为例，近年来多个专业的对口率都在下降：计算机科学与技术下降了 14 个百分点（2024 届：62%，2020 届：76%），软件工程下降了 13 个百分点（2024 届：65%，2020 届：78%），信息安全下降了 10 个百分点（2024 届：69%，2020 届：79%），网络工程（2024 届：64%，2020 届：73%）、物联网工程（2024 届：58%，2020 届：67%）也下降了 9 个…」（经多家转载交叉一致）；计算机类 2025 届 62% vs 2021 届 78%、月收入 6,897 元 vs 工学 7,033 元出自《2026 年中国本科生就业报告》相关报道。相关度定义见 2023 技术报告脚注：「工作与专业相关度＝受雇全职工作并且与专业相关的毕业生人数 / 受雇全职工作的毕业生人数」。
(b) 智联 47.8%：国家大学生就业服务平台 2024-08-28 转载《2024 大学生就业力调研报告》「智联招聘在今年 3 月下旬至 4 月中旬…面向 2024 届毕业生的问卷调研」；百度百科「2024 大学生就业力调研报告」词条同。冲突原文见新浪《16.3% 的青年失业率背后》，同段并列「最终 offer 率不足 8%」与「今年春招专科生的 offer 率是 56%，反而高于本科生的 45% 和硕博生的 40%」。
(c)《湖北省 2025 年中小学教师公开招聘公告》（湖北省人力资源和社会保障厅官网、湖北日报 2025-03-13）；《湖北省 2026 年中小学教师公开招聘公告》（湖北省教育厅官网 2026-04-15）；南方+ 2026-07-06「2026 年湖北省公开招聘中小学教师 2740 名，较 2025 年的 5799 名…」。


#### [G58] CORRECTED · confidence=medium

**修正**:三条构念警告我判定**准确**，但有四处口径需要拧紧。

【A 基本成立】调查时点与分母已一手确认：《2024 大学生就业力调研报告》调研期 2024 年 3 月下旬至 4 月中旬，「截至 4 月中旬，**在有求职计划的应届毕业生中**，47.8% 已获得 offer」。「该 offer 率不能反推就业率」的判断成立。
**需降级的一句**：「未公开有效样本量、抽样方式、院校层次配额」——我未能取得 2024/2025/2026 三版报告的原始 PDF（智联未在官网公开下载，网传版本散落于付费/网盘渠道），因此这条我只能确认「在所有可及的官方转载与摘要中均未见样本量」，不能确认「报告正文中没有」。建议行文改为「公开可及的发布稿与转载中均未披露有效样本量与抽样方式」。「样本来自智联平台用户+自愿填答的双重自选择」是合理推断，不是报告自述，建议以推断语气写。

【B 需三处修正】
① 原表述「机器人 83.8%、新材料 60.1%、人工智能 24.4%（招聘增速）」→ 正确表述「**2026 年 1–5 月，机器人行业应届生招聘职位数同比增长 83.8%、新材料行业 60.1%、光电子 30.7%、航空/航天/船舶制造 29.7%、汽车零部件 28.4%、人工智能 24.4%**」。三点：是**行业**不是专业；是**职位数同比**不是招聘人数；有明确时间窗 2026 年 1–5 月。
② 报告自己就带了反内卷限定语，应当一并引用：「增速大不等于岗位总量最大——2026 年 1–5 月应届生招聘需求**绝对量**较大的行业仍包括互联网、培训/辅导服务、医药制造、电子/半导体/集成电路等」。文章若只引增速榜而不引这句，等于替智联做了它自己都没做的推断。
③「TOP50 高薪专业中 43 个为工学」有来源支持（榜首电子科学与技术 8,064 元、智能科学与技术 7,956 元）；「TOP50 高薪院校中 47 所为双一流」我未找到独立佐证，建议不用或标注单一来源。
**构念警告在这里可以钉死**：智联榜首电子科学与技术 8,064 元 vs 麦可思 2025 届同专业类口径 7,752 元——两个「高薪专业榜」的榜首专业数值就差 300 余元，正因为一个是平台岗位/简历标薪、一个是毕业生自报实得月收入。这组对照比抽象说「构念不同」更有说服力。

【C 成立，一处存疑】猎聘「电子商务 1165.94%」已确认：《2026 届大学生校招全景洞察》（2026-05-28），原文「新发校招职位同比增长 TOP15 行业中，电子商务以 1165.94% 的增速遥遥领先，银行、保险、通信设备等行业增速均超 70%，电子商务、人工智能（+57.98%）、新能源（+32.12%）三大新质生产力行业增速亮眼」。人工智能 57.98% ✓。**但「银行 251.39%、保险 145.74%」我未在原文中找到**——原文只写「银行、保险、通信设备等行业增速均超 70%」。建议删去这两个具体数或标注为未核实。分母（上年该行业在猎聘的新发职位数）确未公开，「低基数+平台自身销售拓展」的解释是合理推断而非已证事实，宜以推断语气写。

【总判】三条构念警告（岗位挂出薪资≠实得收入；院校薪酬榜分母是平台用户；超高增速不可读作行业真实用工增长）在方法学上全部站得住，且「绝不可与麦可思并列」这一条尤其重要——保留。

**核验依据**:智联 2024 报告口径：国家大学生就业服务平台 2024-08-28 转载稿、百度百科同名词条。智联 2026 报告：上观新闻 2026-06-16《考生填志愿，如何看懂就业市场信号？》与湖南日报 2026-06-23 报道，均逐字给出「2026 年 1 至 5 月…机器人行业职位数同比增长 83.8%，新材料行业增长 60.1%，光电子行业增长 30.7%，航空/航天/船舶制造增长 29.7%，汽车零部件增长 28.4%，人工智能增长 24.4%」及「增速大不等于岗位总量最大」；红星新闻 2026-06-16 确认发布日为 2026 年 6 月 16 日；百度百科「2026 年大学生就业前景研判及高考志愿填报攻略」词条同。猎聘：《2026 届大学生校招全景洞察》报道稿，原文含「电子商务以 1165.94% 的增速遥遥领先…人工智能（+57.98%）、新能源（+32.12%）」。麦可思对照值 7,752 元（电子科学与技术，2025 届本科半年后）见 https://news.qq.com/rain/a/20260706A03ET100 。


#### [G59] CORRECTED · confidence=high

**修正**:【A 逐字成立，两处要补】原文已在教育部官网一手核对（正确 URL 是 t20230804_**1072396**.html，采集者若记的是 1072142 则为误记，该号在教育部站内不存在）。三段引文逐字无误：「对经核实存在虚假签约、虚假证明等违规行为的，责成有关部门依规依纪严肃处理，并追究相关高校和人员责任」「重点核查灵活就业等相关数据，以『零容忍』的态度严肃查处就业违规行为」「8 月起，还将委托国家统计局和第三方调查机构在全国范围内开展 2023 届高校毕业生去向落实情况抽样调查」。
补正两处：① 原文是「『四不准』『三不得』规定」，采集者只列了四不准，漏掉的「三不得」恰恰是最能说明行政压力传导的部分，建议补上：「不得不切实际向高校和学院提去向落实率具体指标；不得层层加码向辅导员摊派就业任务；不得将单一的去向落实率指标与就业工作人员或者辅导员的绩效考核、评优等挂钩」。② 第四不准原文是「不准将**毕业生**顶岗实习、见习证明材料作为就业证明材料」，原稿漏「毕业生」二字。

【B 成立——这是本条最硬的空白】我以多角度检索「就业数据造假 处理结果 通报」「高校 就业率 造假 处分 名单」，返回结果**全部是同一篇 2023-08-04 稿件的转载**（教育部官网、国家大学生就业服务平台重复转载数次、信用海口等），未出现任何一份点名通报、处理结果公告或查实数量。「承认有假、未公布查出多少假」可以直接写，判断成立。

【C 需精确化——「存在但不公开」要拆成两层】原表述「教育部委托国家统计局的抽样调查制度化存在…但未见任何一年公开发布」→ 更准确的表述是：**调查制度本身是公开的，只有结果不公开**。国家统计局网站公开挂有《全国普通高校毕业生就业状况统计调查制度》（2020-12-16），载明「调查对象为全国普通高校普通本专科和研究生毕业生，以及录用该毕业生就业的用人单位」「采用非全面调查的抽样调查方法」「由教育部高校学生司、全国高等学校学生信息咨询与就业指导中心统一组织，委托第三方机构具体实施」。教学厅函〔2021〕19 号的原句亦已核到（经山西省教育厅转发件确认）：「每年 9 月初，教育部委托国家统计局开展毕业生就业状况抽样调查，**结果将向各地通报**。」教育部 2022-06-06 另有一句可用：「从 2020 年起，教育部已连续两年委托国家统计局对全国和各地高校毕业生就业状况开展抽样调查。」——即：制度公开、连续执行至少六年、结果只「向各地通报」，从未向社会发布。这比原稿的说法更锋利也更站得住。

【D 数字全部成立，一处未验】76.5%／33.0%／32.1%、《华东师范大学学报（教育科学版）》2023 年第 41 卷第 9 期第 138–154 页、多阶段分层抽样、样本高校 28–45 所、样本 15,060–21,753 人，全部核对通过（2021 年那一轮为 34 所高校、20,269 人；专科 14.8%、本科 68.9%、硕士 15.1%、博士 1.2%）。摘要自述「正规就业比例创新低，升学比例持续走高；落实率下滑，待就业率回升」。
**未能核实：「调查时点为 6–7 月学生离校前」**——该刊摘要页不含调查时点，全文 PDF 需权限，我未取得。这一句是「与麦可思半年后口径不可比」的关键支点，建议要么补一手，要么改写成「岳昌君团队的调查在毕业当年进行，与麦可思『毕业半年后』的观测窗口不同」这类不依赖具体月份的说法。
**另需加的一句谨慎话**：76.5% 与 86% 不能直接相减比较——时点不同（离校前 vs 半年后）、样本框不同（30 余所高校 vs 13.5 万人邀请制）、学历构成不同（含专科硕博 vs 纯本科）。「拆开报 vs 合并报」的论点成立，但要说成「两种呈现方式给读者的画面不同」，不要说成「两个数互相证伪」。

【E 成立，但归因要改】数字两端都已核实：麦可思一手——技术报告第 134 页「2022 届有 4.6% 的本科毕业生在毕业半年后选择灵活就业，其中包括 1.4% 选择受雇半职工作，2.0% 选择自由职业，1.2% 选择自主创业」；官方端——全国高等学校学生信息咨询与就业指导中心口径「2020 届全国高校毕业生的灵活就业占比 16.9%，2021 届高校毕业生灵活就业占比 16.25%」，见全国高校就业创业指导教师网（2021-10-21）与中国就业网（人社部系统）转载，另附「天津、河北、山西三省市 2021 届毕业生灵活就业占比超过 30%」。
**归因必须修正**：原稿推定「官方含编码 12 而麦可思算作受雇全职」我无法证实，且方向可能相反——麦可思的 4.6% **已经把自主创业（1.2%）算了进去**，而官方毕业去向登记里自主创业是与灵活就业并列的独立类别；也就是说在这一维度上麦可思的口径反而更宽，定义差异**不足以**解释 3–4 倍的差距。可证实的差异来源只有三条，建议按此改写：① **分母不同**——16.9%/16.25% 是全国高校毕业生（含高职专科与研究生），麦可思 4.6% 只是本科，而高职灵活就业比例显著更高；② **数据生成方式不同**——官方是高校填报的行政数据，麦可思是毕业生自报问卷；③ **行政激励**——教育部自己在 2023-08-04 的通稿里点名「重点核查**灵活就业**等相关数据」，等于官方承认灵活就业这一栏是造假高发区。第三条是这个 3–4 倍缺口最有力也最有一手依据的解释，应当写在最前面。

**核验依据**:教育部原文：http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202308/t20230804_1072396.html （标题《教育部派出工作组赴各省开展专项核查 严查高校毕业生就业数据弄虚作假》，日期 2023-08-04，来源：教育部），全文含「四不准」「三不得」完整七条及各省举报电话邮箱表。教学厅函〔2021〕19 号引文经山西省教育厅转发件核到（托管于教育部学生服务与素质发展中心站点），原句「每年 9 月初，教育部委托国家统计局开展毕业生就业状况抽样调查，结果将向各地通报」。《全国普通高校毕业生就业状况统计调查制度》，国家统计局网站，2020-12-16。教育部 2022-06-06 稿「从 2020 年起，教育部已连续两年委托国家统计局…开展抽样调查」。
岳昌君等《中国高校毕业生就业趋势研究报告：来自 2003—2021 年调查数据》，《华东师范大学学报（教育科学版）》2023, 41(9): 138-154，doi:10.16382/j.cnki.1000-5560.2023.09.010，https://xbjk.ecnu.edu.cn/CN/10.16382/j.cnki.1000-5560.2023.09.010 （摘要页含全部作者单位、基金号 22JJD880038；表 1 样本高校 28–45 所、样本 15,060–21,753 人；表 2 2021 年已落实 76.5%、升学 33.0%、已确定单位 32.1%、待就业 14.0%）。
麦可思 4.6%：2023 技术报告第 134 页（aliyuncs 链接同上）。官方 16.9%/16.25%：全国高校就业创业指导教师网 2021-10-21 稿、中国就业网 2023-11-13《灵活就业成大学生就业新形态》。


### 第 3 席


#### [G54] CORRECTED · confidence=high

**修正**:财务与股权数据逐字无误（新三板智库研报第205-227行：主营业务收入110,752,232.01、数据监测类96,886,518.62/85.36%、咨询类16,615,311.32/14.64%、毛利率87.39%、王伯庆61.61%、"2500所高校中累计合作706所，正在执行签约项目的569所"、"公司直接面对高校、院系/专业、教育厅/局等机构客户提供产品和解决方案"）。但三处口径必须修正：

(1) 【时态错误，最重要】原表述"新三板挂牌(833861,2015-10)"（现在时）→ 正确表述"2015年10月挂牌新三板(833861)，2020年已终止挂牌"。这不是减弱而是加强论点：麦可思自2020年起再无强制信息披露义务，2018年报是其最后一份公开财务数据，写作时已是8年前的旧账。

(2) 【算术口径】原表述"2018年主营业务收入110,752,232.01元，其中'数据监测类收入'96,886,518.62元"→ 正确表述：96,886,518.62+16,615,311.32=113,501,829.94元，等于**营业收入**（主营110,752,232.01+其他业务2,749,597.93），不等于主营业务收入。"其中"关系不成立。研报图表4标题写"分主营业务收入"但实际按营业收入拆分，85.36%的分母也确是营业收入。建议改写为"2018年营业收入1.135亿元，其中数据监测类9689万元占85.36%"。

(3) 【来源性质须标注】该文件是**卖方推介性质**的《新三板专题研究报告·寻找新三板精选层标的专题报告（二十三）》（新三板智库，2019-11-07，研究员麦棋昌、方俊杰），不是审计报表或交易所披露文件，其自述数据来源为"公司年报"。用它论证"利益相关"时须标明这是一份为拉抬标的而写的推介材料。

(4) 论断D的**统计学推理有误**：原表述"加权后区域分布与实际分毫不差…这是'再抽样'而非事后分层加权的特征"→ 正确表述"事后分层加权按构造同样会使加权维度的边际分布与目标完全吻合，因此'分毫不差'并不能区分再抽样与事后加权；判定其为再抽样的唯一依据是技术报告本身写的'再抽样'二字"。另："意味着可能丢弃了部分回收样本"是推测——有放回再抽样只会复制不会丢弃。另："分毫不差"仅对**加权维度**成立（附表1区域38.5/38.5、26.7/26.7、25.4/25.4、9.4/9.4完全吻合），而非加权维度的省份表（附表2）并不吻合（北京2.6 vs 2.8、河北4.9 vs 4.7）——这个对照本身就是加权维度与非加权维度的教科书式区分，比原论断更有说服力。

(5) 论断B、C、E经独立复核成立，且C可**加强**：技术报告脚注A自己就把自我选择偏差定义为"可能存在就业的毕业生更容易选择参与答题，而没有就业的学生可能不愿意参加答题"——即麦可思**逐字点名了这一风险，然后无任何检验细节地宣称它不存在**。这比"未说明用什么变量、什么检验、p值多少"更尖锐。

(6) "未见披露利益关系"经核实属实：全书20,809行中与披露相关的只有一条"法律声明"（版权声明），无任何利益冲突、资助或客户关系声明。

**核验依据**:一手件1：新三板智库《麦可思(833861.OC): 中国高教管理数据与咨询产业的领军者》PDF，https://pdf.dfcfw.com/pdf/H3_AP201911121370658000_1.pdf ，自行下载(1,822,839字节)并pdftotext -layout提取798行，逐行核对第7、46、107、110、124、136、180、205-227、616-617行，上列所有数字与引语逐字命中。
一手件2：《2023年中国本科生就业报告》技术报告PDF，https://xiuzhenorgweb.oss-cn-zhangjiakou.aliyuncs.com/uploads/files/20231127/cc79a43039780361b3bfe6540f797713.pdf ，自行下载(7,161,706字节)，235页，pdftotext提取得20,809行（与采集者行数完全一致，说明同一提取口径）。逐字命中第19,656-19,660行（13.5万/428专业/30省/592职业/327行业）、19,681行（电子邮件发放答题邀请函、10~30分钟）、19,689行（不含成人高等教育、军事院校和港澳台院校）、19,710行（"未被邀请的答题被视为无效"）、19,711-19,712行（自我选择性检验）、19,717行（脚注定义）、19,721-19,723行（权数/再抽样）、附表1（区域38.5/38.5等）、附表2（北京2.6/2.8、河北4.9/4.7）。
独立检索：grep "回收率|应答率|答题率|响应率|回复率" 全书 → **0命中**，独立复现了采集者的零结果。grep "利益冲突|利益相关|付费客户|资助|赞助|声明" → 仅"法律声明"1条。
摘牌：百度百科麦可思词条及新三板相关检索均记载"2015年10月登陆新三板（证券代码：833861），后终止上市，公司股票于2020年在全国中小企业股份转让系统终止挂牌"（未取得股转系统原始摘牌公告，故摘牌一节置中等置信度）。
效度检验研究：经百度多角度检索（麦可思 信度/效度/检验/质疑/样本偏差/方法论批评）未见任何对麦可思数据做效度检验或与行政数据交叉验证的学术研究，独立复现采集者零结果；但受限于无法访问CNKI，此项为中等置信度。


#### [G55] CORRECTED · confidence=high

**修正**:A、B、C、D、F 全部成立，其中B为本批最干净的一击；唯 **E 的时间线错了一年，且错在削弱论点的方向**。

【E 必须修正】原表述"2023版书内明确说机器人工程'暂未包括在内'，但**2025版(2024届)**机器人工程直接进了绿牌"→ 正确表述"…但**2024版(2023届)**机器人工程即已进入绿牌"。2024年本科绿牌为：微电子科学与工程、电气工程及其自动化、新能源科学与工程、能源与动力工程、机械电子工程、**机器人工程**。即：麦可思在2023年6月的书里写"尚无成规模、成趋势的毕业生就业数据，暂未包括在内"，**仅隔一年（2024年6月）**同一专业就直接上了绿牌榜，且规则变更无任何说明。反转周期是1年不是2年，论点因此更强，不是更弱。（机器人工程随后在2025年继续在榜，2026年出榜。）

【A】逐字无误。技术报告第43-44页原文："红牌专业指的是失业量较大，毕业去向落实率、薪资和就业满意度综合较低的专业。黄牌专业指的是除红牌专业外，失业量较大，毕业去向落实率、薪资和就业满意度综合较低的专业。绿牌专业指的是失业量较小，毕业去向落实率、薪资和就业满意度综合较高的专业，为需求增长型专业。"——"失业量"确为首要判据，且**红牌与黄牌的定义文字除"除红牌专业外"五字外完全相同**，本身就说明二者无可操作的区分标准，这是比原论断更硬的不可复现证据，建议补入。

【B】逐字坐实。搜狐2026-06-25文对红牌的改写原文为："在就业落实率、薪资水平与就业满意度等方面综合表现相对较低，同时在市场需求端呈现减少或增长缓慢趋势的专业。"——"失业量较大"这一原始首要判据被整体替换为"市场需求端减少或增长缓慢"，且该文所列2026红牌6专业（绘画、音乐表演、美术学、文化产业管理、劳动与社会保障、城乡规划）与官方一致，说明这是随通稿一起流通的**权威版本**改写，不是个别小编笔误。

【C】成立。穷尽检索"红黄绿牌 权重/阈值/算法/评定标准/公式"未见任何一版公开权重或阈值；连百度生成式摘要都直接判定"麦可思未公开具体的权重数值与算法公式"。补强：书中另一处（第195页）自述判据为"失业量、毕业去向落实率、薪资和就业满意度**等**就业指标"——一个"等"字使判据集合本身都是开放的。

【D】逐字无误（第44页）："部分近年来新增数量较多的专业（如人工智能、数据科学与大数据技术、机器人工程）由于尚无成规模、成趋势的毕业生就业数据，暂未包括在内。"

【F】成立，未发现任何对红黄绿牌预测效度的回溯检验研究（受限于无CNKI访问，中等置信度）。

**核验依据**:一手：《2023年中国本科生就业报告》技术报告PDF（同上OSS链接，自行下载核对）第4343-4351行=书内第43-44页，红黄绿牌三定义与"暂未包括在内"逐字命中；第18004行=书内第195页"根据失业量、毕业去向落实率、薪资和就业满意度等就业指标，综合评价筛选出需求增长型和预警专业"。
B：https://www.sohu.com/a/1041564081_121294 （2026-06-25）实取，改写后定义与2026红牌6专业逐字确认。
E：2024年本科绿牌名单经检索确认为"微电子科学与工程、电气工程及其自动化、新能源科学与工程、能源与动力工程、机械电子工程、机器人工程"；2025年绿牌经中北大学机械工程学院转载的麦可思原文确认为"电气工程及其自动化、微电子科学与工程、机械电子工程、新能源科学与工程、车辆工程、机器人工程"；2026年绿牌经安徽新华学院发展规划处、浙江师范大学发展规划处转载确认为"电气工程及其自动化、微电子科学与工程、自动化、能源与动力工程、车辆工程、新能源科学与工程"。
C：百度多轮检索（麦可思 红黄绿牌 权重 算法 评定标准）零结果。


#### [G56] CORRECTED · confidence=high

**修正**:【A 严重错误：表12-7 的2019–2022四列被读错，必须整列替换】原表述与一手表格不符。技术报告第195-196页表12-7"近五年本科绿牌专业"的正确内容是：
- 2019（7个）：信息安全、软件工程、网络工程、物联网工程、数字媒体技术、**通信工程**、**数字媒体艺术**
- 2020（7个）：信息安全、软件工程、信息工程、网络工程、计算机科学与技术、**数字媒体艺术**、**电气工程及其自动化**
- 2021（6个）：信息安全、软件工程、信息工程、网络工程、数字媒体技术、**电气工程及其自动化**
- 2022（6个）：信息安全、网络工程、信息工程、微电子科学与工程、数字媒体技术、能源与动力工程（**无电气工程及其自动化**）
- 2023（6个）：信息工程、微电子科学与工程、电气工程及其自动化、能源与动力工程、道路桥梁与渡河工程、机械电子工程（原表述此列正确）
逐条差异：原表述在2019列错加"电气工程及其自动化"、漏"通信工程"和"数字媒体艺术"；2020列错写"数字媒体技术"（实为该列无此专业）、漏"数字媒体艺术"和"电气工程及其自动化"；2021列把"电气工程及其自动化"错写成"数字媒体艺术"；2022列错加"电气工程及其自动化"。**"通信工程"在原表述中整个消失了。**
判据（不是我的排版猜测，是书自身的四条叙述约束，只有上述一种排法能同时满足）：①书称"近五年进入绿牌名单的专业共14个"——正确排法恰好14个，原表述只有13个；②书称"次数最多的是网络工程、信息安全、信息工程（均为4次），其后是电气工程及其自动化、软件工程、数字媒体技术（均为3次）"——正确排法下数字媒体技术恰为3次，原表述会算出4次，与书自相矛盾；③书称14个中"网络工程、信息安全、软件工程、数字媒体技术、物联网工程、计算机科学与技术6个专业均属于计算机类"——正确排法恰好6个；④书称"这些专业除数字媒体艺术之外，均属于工学门类"——需数字媒体艺术在榜，原表述几乎把它读没了。另以pdftotext -layout的**行首token绝对列位**独立校验：折行单元格"电气工程及其/自动化"行首在第32/33列（居中38）＝2021列表头中心38；末行"电气工程及其自动化"行首在第42列（居中51）＝2020列表头中心50。两条证据链一致。
**注意：此错误不动摇文章论点，反而加强它**——正确名单里2019年还有"通信工程"，14个绿牌中6个是计算机类，而2026年计算机类全灭。

【B 成立，且是本批最扎实的一条，可再加强】2010年本科红牌10专业经四个2010年当期独立来源交叉确认：动画、法学、生物技术、生物科学与工程、数学与应用数学、体育教育、生物工程、**计算机科学与技术**、英语、国际经济与贸易。中新网2010-05-10当期报道标题级表述：本科的计算机科学与技术、电子信息科学与技术、信息管理与信息系统"都出现了毕业生滞销的现象"。2011年红牌名单同款。**建议补入的更强反例**：同一份2010年榜单的**绿牌**是地质工程、港口航道与海岸工程、船舶与海洋工程、石油工程、采矿工程、油气储运工程、矿物加工工程、过程装备与控制工程、水文与水资源工程——清一色资源开采类，十六年后正是被劝退最狠的一批。**红榜和绿榜同时反转**，比只讲红榜有力得多。另："十五年前"宜改"十六年前"或"2010年"（2010年榜基于2009届毕业生）。

【C 需加时间戳与一处删改】原表述"同一体系中计算机类'毕业五年后月收入14,090元**仍**居主要专业类第一'"→ 正确表述"计算机类**2019届**毕业五年后月收入14,090元，居主要专业类第一（数据出自《2025年中国本科生就业报告》，同榜第二为电子信息类13,584元）"。理由：①14,090是2019届（2015年入学、2024年调查）的队列数据，与同句的"2024届82.4%"不是同一批人，不加届次会误导读者以为是当下应届生的前景；②"仍"字不可用——2026版报告已改报2020届五年后数据，其中电子信息类为13,992元，计算机类是否仍居第一未获证实。
82.4%/61个主要专业类中倒数第11/全国本科平均86.7%/历史学类87.2%/外国语言文学类86.9% 五数经多来源一致复现且内部自洽（87.2−82.4=4.8、86.9−82.4=4.5），但**全部为媒体转述，无一手原书**，须标注"转引自《2025年中国本科生就业报告》媒体报道"。
2026版月收入前十经多源确认为：微电子科学与工程、电子科学与技术、自动化、信息安全、光电信息科学与工程、采矿工程、机械工程、测控技术与仪器、材料科学与工程、通信工程；区间7,249–7,814元，榜首微电子7,814元✓；2025届本科平均月收入6,435元。**必须防的坑**：榜上第4的"信息安全"本身就是计算机类专业，所以"计算机类跌出前十"是错的；原表述写"计算机科学与技术、软件工程首次跌出"是准确的，务必保持这个精确措辞，不要采信媒体标题的"计算机跌出前十"。
955所/661所成立，但须标源：出自**教育部阳光高考平台**（截至2025年11月），不是麦可思。

**核验依据**:一手：《2023年中国本科生就业报告》技术报告PDF（同上OSS链接）第195-196页表12-7，用 pdftotext -layout 提取后以python计算每行token的显示列偏移逐格还原（脚本与列位数据见 /private/tmp/claude-502/-Users-cissychen-Desktop-repos/8f82afa8-649c-4c17-b39f-b18b26c6bb77/scratchpad/g5x/mycos_lay.txt 第8889-8901行）；书内自述约束见第18004-18016行（"共14个""均为4次""均为3次""6个专业均属于计算机类""除数字媒体艺术之外均属于工学门类"）。
B：2010年当期四来源交叉——北京物资学院新闻中心2010-06-02、广西新闻网2010-05-17《本科10个专业被预警》、新浪教育2010-06-02、中国新闻网2010-05-10《2010年大学生就业"红黄绿牌"专业名单出炉》；2011年名单见查字典高考网2011-07-12。2010绿牌名单见宿州职业技术学院2010-05-11转载及百度文库《2010年中国大学生就业蓝皮书》解读。
C：82.4%/86.7%/87.2%/86.9%/倒数第11 见NGA玩家社区2026-04-23、爱企查、知了爱学等多源转述《2025年中国本科生就业报告》；14,090元（2019届毕业五年后TOP10专业类，电子信息类13,584、自动化类12,825…全国本科10,619）见麦可思微信公众号原榜及搜狐2025-09-01；2026版高薪TOP10与7,814元/6,435元见金融界2026-06-16、老王侃高考2026-06-22；2020届五年后电子信息类13,992元见微博2026-07-13；955/661所见多源标注"教育部阳光高考平台数据（截至2025年11月）"。


#### [G57] CORRECTED · confidence=high

**修正**:三条须分别处置，不能一刀切禁用——(a)(b) 判 REFUTED 禁用，(c) 可救活但必须改写。

【(a) "计算机类对口率从2020届76%降至2024届62%" —— REFUTED，禁用】我独立换了四个角度（麦可思官方口径检索、精确串"76% 62% 对口率"、麦可思公众号/官网、传播链回溯）均未触及一手。查到的全部载体是自媒体，且**发文日期高度集中在2026年7月21日前后的同一波**（"学习不打烊""阿间教育""鲜美茱萸""学业百事通"等），典型的单点起源级联，无一给出报告名与页码。**另有一条判定性反证**：麦可思体系里根本不存在"专业对口率"这个指标名，其指标叫"工作与专业相关度"；一个连指标名都不对的数字不可能来自蓝皮书原文。禁用。

【(b) "1个岗位17.2份简历 / 投150–200份换1个面试 / offer率不足8%" —— REFUTED，禁用】溯源到的最靠前载体是新浪财经转载自媒体文《2026年，1270万毕业生的天崩开局》(2026-05-23)，另见新东方网、知乎转载，均写"智联招聘的数据显示"。部分转载进一步指名《2026春节后首周就业市场景气报告》——但该报告的实际指标体系是CIER景气指数（=市场招聘需求人数/市场求职申请人数），核查后**其中并无"17.2份简历"或任何按岗位统计的简历数，也不报告应届生offer率**。即：这是一次**指名到具体报告的错误归因**，比无名归因更该禁用。
量级冲突**成立**，且原表述的诊断正确：智联《大学生就业力调研报告》2024版原文逐字为"截至2024年4月中旬，在**有求职计划的应届毕业生**中，47.8%已获得offer"——分母是人、且是筛过的人；"offer率不足8%"若成立只能是"简历→offer"的事件级转化率，两者分母不同、量级差近6倍，被当成同一件事传播。禁用该组数字，但"两个分母被混为一谈"这个**方法论观察本身可以写**。

【(c) 教师招聘缩减 —— CORRECTED，可用但须整句改写】原表述"多地教师招聘缩减50%+、竞争比200:1"→ 正确表述："以湖北省为例，省级统一公开招聘中小学教师的计划数从2025年的5,799名降至2026年的2,740名，一年减少52.8%。"这两个数字**能落到省级官方招聘公告**（湖北省教育厅2025年公告5,799名；2026年公告2,740名，jyt.hubei.gov.cn），因此不再是无源数字。
但必须剥掉两层：①"多地"不成立——我只坐实了湖北一省；江西"三年从七千余降至一千余（约-84%）"仅见于自媒体，未追到省级公告，不可用。②"竞争比200:1"**仍判REFUTED**——"部分岗位甚至超过200比1""热门学科普遍80比1"只见于自媒体解说，无任何省级教育厅/人社厅的报名人数与计划数汇总数据支撑，禁用。

**核验依据**:(a) 独立四角度检索均未达一手；命中的全部为2026-07-21前后同批自媒体（学习不打烊、阿间教育、鲜美茱萸等），措辞"就业蓝皮书数据显示，2020届计算机类毕业生的专业对口率为76%，而到了2024届，这一数据已经滑落至62%"；反证：麦可思公开体系使用"工作与专业相关度"，检索未见其使用"专业对口率"一词。
(b) 载体：新浪财经转载《2026年，1270万毕业生的天崩开局》(2026-05-23)、新东方网、知乎，均标"智联招聘的数据显示"；指名的《2026春节后首周就业市场景气报告》经核查仅含CIER指数（定义"就业市场景气指数(CIER)=市场招聘需求人数/市场求职申请人数"），无17.2、无offer率。智联《2024大学生就业力调研报告》原文逐字："截至2024年4月中旬，在有求职计划的应届毕业生中，47.8%已获得offer"，调研窗口"今年3月下旬至4月中旬"。
(c) 湖北省教育厅2026年公告："2026年面向社会公开招聘2740名中小学教师"（jyt.hubei.gov.cn，2026-04-15）；湖北省教育厅2025年公告："2025年面向社会公开招聘5799名中小学教师"（2025-03-13）。降幅(5799-2740)/5799=52.75%。江西84%与200:1竞争比经检索仅见自媒体（狐狸先森讲升学规划、遇见转运官等），无省级教育厅/人社厅原始文件。


#### [G58] CORRECTED · confidence=medium

**修正**:三条构念警告**全部准确**，可放心使用；但B有两处须修正、一处须降级。

【A 成立，逐字坐实】智联《2024大学生就业力调研报告》原文："截至2024年4月中旬，在**有求职计划的应届毕业生**中，47.8%已获得offer"；调研窗口"在今年3月下旬至4月中旬…开展问卷调研"。分母确为"有求职计划的应届毕业生"，确实排除了升学、考公备考、慢就业者，**不能反推就业率**——这一条成立且措辞精确。"未公开有效样本量、抽样方式、院校层次配额"经核实属实（可获取的报告版本与新闻稿均未披露）。

【B 修正两点】
(1) 原表述"机器人83.8%、新材料60.1%、人工智能24.4%（招聘增速）"→ 正确表述应写明这是**行业职位数同比增长**，不是专业维度的招聘增速：原文为"机器人行业职位数同比增长83.8%，新材料行业增长60.1%，光电子行业增长30.7%，航空/航天/船舶制造增长29.7%，汽车零部件增长28.4%，人工智能增长24.4%"。**"行业职位数增长"与"某专业毕业生需求增长"是两个东西**，把行业增速当专业推荐依据正是本文要批判的构念滑移，写的时候别自己踩进去。
(2) 原表述"TOP50高薪专业中43个为工学；TOP50高薪院校中47所为双一流"→ **未获独立证实**，我在可及范围内没能复现这两个数字，建议降级为不写，或写明"据该报告"并接受其为未经核验的引述。
(3) "原文未提供完整的方法论说明、数据统计周期或样本规模"经核实属实。

【C 成立，且可加一句】1165.94%（电子商务）确为猎聘2026届校招新发职位同比增速TOP15榜首，发布于2026年5月下旬；分母（上年该行业在猎聘的新发职位数）确实从未公开，样本、口径、统计周期均无披露。**可补的硬话**：同一榜单里电子商务1165.94%与人工智能57.98%并列呈现，本身就自证了这是平台侧基数效应而非产业信号——若电商用工真在一年内涨12倍，它会是宏观经济事件而不是一张招聘网站的榜单。

【构念警告核准】"高薪专业排行"来自岗位挂出薪资/平台简历薪资、"院校薪酬排行"分母是在该平台投递或被录用的该校毕业生、名校用户占比失衡会系统性抬高其排名、与麦可思"自报实得月收入"是两个不同构念绝不可并列——三点均准确，且可再补一条更狠的：智联的分母是**平台用户**，麦可思的分母是**受邀毕业生**，两者都不是全体毕业生，因此"哪个更准"是个伪问题，正确的说法是它们各自只对自己的用户池有效。

**核验依据**:智联2024报告原文逐字"截至2024年4月中旬，在有求职计划的应届毕业生中，47.8%已获得offer"及调研窗口"3月下旬至4月中旬"，经百度检索多源一致复现；样本量/抽样方式/院校配额在可获取材料中均无披露。
智联2026-06-16《2026大学生就业前景研判及高考志愿填报攻略》："机器人行业职位数同比增长83.8%，新材料行业增长60.1%，光电子行业增长30.7%，航空/航天/船舶制造增长29.7%，汽车零部件增长28.4%，人工智能增长24.4%"；报告自述基础为"产业趋势、薪酬数据"，未给样本量或方法论；TOP50高薪专业43个工学、TOP50高薪院校47所双一流两项未能复现。
猎聘：2026-05-28口径"新发校招职位同比增长TOP15行业中，电子商务以1165.94%的增速遥遥领先，银行、保险、通信设备等行业增速均超70%"；无基数、无样本量、无统计周期披露。
未取得智联2024/2025/2026报告原始PDF（水滴研报需登录），以上为多源转述交叉，故B(2)判未证实而非成立。


#### [G59] CORRECTED · confidence=high

**修正**:A、B 成立（B是文章最该点名的空白，经独立穷尽检索确认为真）；C 的**出处引错了文件，但换上正确文件后论点更强**；D 的**76.5%口径拆错**，且缺一个致命的可比性说明；E 官方侧成立。

【A 逐字无误，两处小补】教育部2023-08-04原文全部命中："对经核实存在虚假签约、虚假证明等违规行为的，责成有关部门依规依纪严肃处理，并追究相关高校和人员责任"（原文此句后还有"，切实维护高校毕业生就业合法权益"）；"重点核查灵活就业等相关数据，以'零容忍'的态度严肃查处就业违规行为"；"8月起，还将委托国家统计局和第三方调查机构在全国范围内开展2023届高校毕业生去向落实情况抽样调查。"补正两点：①原文是"'四不准''三不得'"并列，文章只引四不准会漏掉更能说明行政压力传导的三不得（"不得不切实际向高校和学院提去向落实率具体指标；不得层层加码向辅导员摊派就业任务；不得将单一的去向落实率指标与就业工作人员或者辅导员的绩效考核、评优等挂钩"）——这三条恰恰是**教育部自己承认存在指标摊派**，比四不准更有力；②第四条原文是"不准将**毕业生**顶岗实习、见习证明材料作为就业证明材料"。

【B 成立】独立换角度穷尽检索，只检出"核查行动"类公告（2023-08-04教育部及各省转发、举报电话邮箱、截止8月31日），**未检出任何一份点名通报、查实数量、处理结果公告**。"承认有假、未公布查出多少假"这一判断可以直接写。

【C 出处须替换】原表述把"结果将向各地通报"归给"教学厅函〔2021〕19号"→ 我未能在该文号下核到这句话（该文可核到的相关表述是"9月初，教育部将会同国家统计局对就业统计工作开展抽样调查，向毕业生本人和用人单位核实就业情况"）。**正确出处是《全国普通高校毕业生就业状况统计调查制度》（国家统计局批准，2020-12-16）**，其原文更硬："本制度有关结果将通过**函件形式**反馈31个省（区、市）和新疆生产建设兵团教育行政部门。"——这不是"通报"而是**以函件定向反馈给行政部门**，即制度设计上就写明了不面向公众。用这句替换，"存在但不公开"从推断升级为**制度白纸黑字**。检索未见任何一年的抽样调查结果公开发布，此项成立。

【D 两处必须改】
(1) 原表述"2021年'已落实'比例（**已确定单位 + 升学**）76.5%"→ 正确表述"已落实76.5% = 已确定单位32.1% + 升学33.0% + **灵活就业11.4%**"。32.1+33.0=65.1，根本不等于76.5；补上灵活就业11.4后恰好=76.5。这个错误方向很坏：它把"灵活就业"从画面里抹掉了，而灵活就业正是本文E段要攻击的口径争议核心——原表述等于在批判灵活就业注水的同一篇文章里，自己把11.4个百分点的灵活就业悄悄并进了"正规去向"。
(2) **缺失的关键限定**：岳昌君调查的时点是学生**离校前**，麦可思是毕业**半年后**，教育部去向落实率的统计时点是**8月31日与12月31日**。76.5%对86%的差距里有相当大一块只是**时点差**，不全是口径差。原表述把它整体呈现为"合并vs拆开"的口径撕裂，会被人一句"你拿6月比人家次年3月"打回。必须加限定："在**离校前**这个时点上，已确定单位者只有32.1%"——这样说才站得住，而且照样有力。
样本数据核准：28–45所高校、15,060–21,753人**完全正确**（最少15,060人为2013年，最多21,753人为2009年；2021年为34所、20,269人；2003起每两年一次共10轮）。期刊卷期正确：《华东师范大学学报（教育科学版）》2023年第41卷第9期，第138-154页，题《中国高校毕业生就业趋势研究报告：来自2003—2021年调查数据》，作者岳昌君、冯沁雪、辛晓佳、邱文琪。2021年待就业14.0%、平均起薪7,025元。"调查时点为6–7月学生离校前"我未在可及页面中核到明确表述，建议改为"离校前"这一较弱但安全的措辞。

【E 官方侧成立，归因须降级为假说】2020届16.9%、2021届16.25%确出自全国高等学校学生信息咨询与就业指导中心（学职平台2021-10-20发布）。但**必须标明一个已知的构成差异**：官方16.9%的分母是**全体高校毕业生（含高职专科）**，麦可思4.6%是**本科单口径**，高职灵活就业率显著更高，因此3–4倍差距中有一部分是学历构成而非造假。采集者推定的另两条归因（官方含就业编码12而麦可思算作受雇全职；行政数据有把难核实去向者归入灵活就业的激励）我未能取得一手佐证，**应写成待证假说而非结论**。麦可思2022届本科4.6%、2025届6.9%两数我未取得一手原书，属媒体/采集者转述。

**核验依据**:A：教育部原文，http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202308/t20230804_1072396.html （WebFetch陷入http/https重定向环，改用curl直取HTML并解析正文），上列所有引语逐字命中，含完整"四不准""三不得"七条与举报电话邮箱表。
B：多角度检索仅得行动类公告，无任何结果类通报。
C：《全国普通高校毕业生就业状况统计调查制度》（国家统计局，2020-12-16）逐字"本制度有关结果将通过函件形式反馈31个省（区、市）和新疆生产建设兵团教育行政部门"；教学厅函〔2021〕19号下仅核到"9月初，教育部将会同国家统计局对就业统计工作开展抽样调查，向毕业生本人和用人单位核实就业情况"，未核到"结果将向各地通报"原句，故判该归属为出处错误（对19号全文本身判UNVERIFIABLE——moe.gov.cn未取到全文，省级转载亦未见完整件）。
D：https://xbjk.ecnu.edu.cn/CN/10.16382/j.cnki.1000-5560.2023.09.010 实取，题名/作者/卷期页码/样本表（2003:45校18,723人、2005:34/21,220、2007:28/16,388、2009:29/21,753、2011:30/19,768、2013:30/15,060、2015:28/15,421、2017:33/18,076、2019:32/16,571、2021:34/20,269）与2021年分项（已确定单位32.1%、升学33.0%含国内升学29.3%、灵活就业11.4%、待就业14.0%、已落实76.5%）核对；32.1+33.0+11.4=76.5恰好闭合，故已落实口径确含灵活就业。全文PDF下载返回HTTP 500，未取得。
E：学职平台2021-10-20："根据全国高等学校学生信息咨询与就业指导中心数据统计，2020届全国高校毕业生的灵活就业占比16.9%，2021届高校毕业生灵活就业占比16.25%"。麦可思4.6%/6.9%未取得一手。
