# 01 · Round 1 原始论断 — #16 未来十年选什么专业?给准大学生的就业证据体检(中美对比)

> 8 条调研线并行采集,截至 2026-07-24。来源分级:【官方】/【研究】/【商业调查】/【媒体】。
> 本文件为**未验证**原始采集。任何数字在通过 Round 2 三票对抗验证(及单源实证的 Round 3 双席审计)前不得承重。

## 线 A:BLS 就业预测的自我体检(本篇方法学脊柱)

> 取证说明:bls.gov 对本次抓取工具返回 403,所有 BLS 页面均通过 Internet Archive Wayback Machine 快照取得(快照日期见各条)。原始 URL 为 bls.gov 正规路径,内容含 BLS 页脚与 "Last Modified Date",可回溯。数据表(occupation.xlsx / 2014-24.zip / 2016-26.zip)为 BLS 官方 Excel 原件,已本地解析,标注【本轮自算】的数字由我从原始单元格计算,须在 Round 2 复核。

### 关键论断

---

#### 一、2024–2034 版官方预测本体

- **[A1]** BLS 最新一版十年预测(2024–2034)projects 全美就业十年只增 5.2 百万个岗位、+3.1%,不到上一个十年实际增幅(+13.0%)的四分之一。
  - 口径:分子=就业净变化(employment change,非 openings);分母=2024 年基期总就业 169,956.1 千;时间窗 2024→2034;样本=National Employment Matrix 全口径就业(含 wage and salary + self-employed,是"岗位数"job count 不是"人数"person count);发布日 2025-08-28,编号 USDL-25-1324。对照的 "13.0%" 是 2014–24 实际值。
  - 来源:【官方】U.S. Bureau of Labor Statistics · "Employment Projections: 2024-2034 Summary"(News Release USDL-25-1324)· 2025-08-28 · https://www.bls.gov/news.release/ecopro.nr0.htm(快照 20260723110547)
  - 逐字摘引:"The U.S. economy is projected to add 5.2 million jobs from 2024 to 2034... Total employment is projected to increase to 175.2 million and grow 3.1 percent, which is slower than the 13.0-percent growth recorded over the 2014-24 decade."
  - 反证/矛盾测量:见 [A2] —— 这个 3.1% **不是需求预测**,几乎完全等于劳动力供给预测,不能被读成"未来十年岗位很少"。

- **[A2]** 【本篇最重要的方法学揭穿】"十年增 5.2 百万个岗位"在数学上基本等同于 BLS 的劳动力人口预测(+5.35 百万人,+3.2%),因为 BLS 的模型强制令劳动供给=劳动需求。它不是对"AI 会不会消灭岗位"的回答。
  - 口径:Table 3.1,Civilian labor force 16 岁及以上,2024=168,104 千 → 2034=173,454 千,变化 +5,350 千 = +3.2%;同期就业变化 +5,211.8 千 = +3.1%。两者差异只来自"一人可兼多职"的口径差(labor force 数人、employment 数岗位)。
  - 来源:【官方】BLS · Employment Projections Table 3.1 "Civilian labor force by age, sex, race, and ethnicity, 2004, 2014, 2024, and projected 2034" · https://www.bls.gov/emp/tables/civilian-labor-force-summary.htm ;及【官方】BLS · "Employment Projections: 2024-2034 Technical Note" · 2025-08-28 · https://www.bls.gov/news.release/ecopro.tn.htm(快照 20260613063217)
  - 逐字摘引(Technical Note,BLS 自己说的):"BLS **does not project an overall labor shortage or surplus** because in the BLS projections data framework, labor supply (the labor force) and labor demand (employment) are linked—a projected increase in labor supply necessarily results in an increase in employment."
  - 反证/矛盾测量:搜索角度——找 BLS 是否在别处给出"独立于劳动力供给的岗位需求预测";未发现。BLS 的 macro model 先定 GDP/potential output,再由 full-employment 假设倒推就业,故不存在独立需求路径。

---

#### 二、BLS 自己写的"本模型不做什么"(逐字摘引,本线最有价值的素材)

- **[A3]** BLS 在技术说明里明文声明:本预测**不预测经济周期**,**不是 forecast**,只是给定假设下的一个情景。
  - 口径:适用于全部 2024–34 系列(labor force / macro / industry / occupation)。
  - 来源:【官方】BLS · "Employment Projections: 2024-2034 Technical Note" · 2025-08-28 · https://www.bls.gov/news.release/ecopro.tn.htm
  - 逐字摘引:"The projections focus on long-term structural trends of the economy and **do not try to anticipate future business cycle activity**." / "The projections **are not intended to be a forecast of what the future will be** but instead are a description of what would be expected to happen under these specific assumptions and circumstances. When these assumptions are not realized, actual values will differ from projections."
  - 反证/矛盾测量:无矛盾;但媒体与"最好就业专业"榜单普遍把它当 forecast 用,这正是本文要打的点。

- **[A4]** 【AI 时代的自爆式免责声明】BLS 明说:如果技术进步显著快于历史,本方法"不太可能给出合理结果"。
  - 口径:同上,Technical Note "Technological progress assumptions" 一节;针对 AI 专门写的段落。
  - 来源:【官方】BLS · Employment Projections: 2024-2034 Technical Note · 2025-08-28 · https://www.bls.gov/news.release/ecopro.tn.htm
  - 逐字摘引:"**In a future state where technology advances much more rapidly than it has historically, it is unlikely that historical relationships would hold, and therefore BLS projection methods are unlikely to yield reasonable results.**" 以及:"BLS methods could capture this, but **BLS has no data on which to base these differential productivity impacts.** BLS therefore chooses to present a scenario with technological progress in line with historical patterns, which allows the projections to be grounded by historical data relationships rather than introducing adjustments that would be highly speculative."
  - 反证/矛盾测量:BLS 同时主张历史上技术冲击是渐进的,并引 Handel(MLR 2022)为据 —— 见 [A5]。

- **[A5]** BLS 在专门讨论 AI 的方法学论文里,再次逐字承认:本方法**不是为捕捉极快技术变革设计的**,且 GenAI 的时点与规模"太不确定,无法反映进预测"。
  - 口径:MLR 文章,基于 2023–33 预测周期的案例研究;作者 Christine Machovec、Michael J. Rieley、Emily Rolen;2025 年 2 月;非匿名评审期刊(MLR 是 BLS 官方刊物,不是同行评审)。
  - 来源:【官方】Machovec, Rieley & Rolen · "Incorporating AI impacts in BLS employment projections: occupational case studies" · Monthly Labor Review, BLS · 2025-02 · https://www.bls.gov/opub/mlr/2025/article/incorporating-ai-impacts-in-bls-employment-projections.htm(全文 PDF 自 FRASER 取得:https://fraser.stlouisfed.org/files/docs/publications/bls_mlr/bls_mlr_20250210.pdf)
  - 逐字摘引:"**BLS projection methods are not designed to capture extremely rapid technological change** and, therefore, assume that the overall pace of technological [change is in line with history]." / "**The timing and scale of many potential impacts of GenAI are too uncertain to be reflected in BLS projections.** New technologies such as autonomous vehicles or AI are harder to assess than technologies that constitute incremental improvements." / "EP generally makes adjustments to its models **only if its research on a new technology provides clear expectations** for the technology's employment impacts."
  - 该文自陈的两个历史案例(极佳的正反对照素材):
    - **做对了的一次**:数码相机 → BLS 在无历史下滑数据的情况下主动下调,预测 photographic process workers 2004–14 下降 23.6%;实际从 2004 年峰值 86,300 跌至 2014 年 28,800,再跌到 2023 年 9,200。
    - **克制住了的一次**:自动驾驶 → 2010 年代 BLS 判断"太不确定"、不调整卡车司机模型;heavy and tractor-trailer truck drivers 从 2012 年约 1.7 百万增到 2023 年逾 2.2 百万,BLS 的克制被事后证明正确。
  - 反证/矛盾测量:这两个案例是 BLS 自选的、对自己有利的样本;[A9]–[A11] 的系统性误差数据是相反方向的证据。

- **[A6]** 官方新闻稿正文内嵌一个方框,劝读者**不要看具体数值**,只看方向和相对大小。
  - 口径:News Release USDL-25-1324 正文方框 "Interpreting the Employment Projections"。
  - 来源:【官方】同 [A1]
  - 逐字摘引:"The Employment Projections (EP) program estimates specific values for projected employment levels and growth rates. **However, this precision in the data does not account for the inherent uncertainty of predicting long-term changes in the labor market. Focusing on the direction and relative size of projected changes, rather than on the precise value estimates,** may yield similar insights..."
  - 反证/矛盾测量:搜索角度——找 BLS 是否发布过预测区间/置信区间;未发现,BLS 只发点估计。这是"精确的假象"的直接证据。

- **[A7]** full-employment 假设的完整定义与后果:BLS 把每一版预测都锚定在"目标年经济 100% 满产"上,故**预测中不含任何周期成分**;基期若处在周期低谷,预测就会系统性偏低。
  - 口径:BLS 定义 full employment = 失业率等于 NAIRU、无周期性失业、GDP 等于潜在产出。文中给出量化例证:2010 年(衰退刚结束、经济远低于潜在产出)BLS 发布的未来十年实际 GDP 增速为 3.0%,而 CBO 的 2010→2020 潜在 GDP 增速为 2.3%,差额 0.7 个百分点可归因于基期的周期因素。
  - 来源:【官方】Kevin S. Dubina · "Full employment: an assumption within BLS projections" · Monthly Labor Review, BLS · 2017-11 · https://www.bls.gov/opub/mlr/2017/article/full-employment-an-assumption-within-bls-projections.htm
  - 逐字摘引:"Accordingly, **BLS projections contain no cyclical deviations**; rather, a full-employment assumption is used that projects only structural changes to the economy."
  - 反证/矛盾测量:这是 BLS 的辩护,也是它的软肋。见 [A10] —— 两次最近的回溯评估中,BLS 自己把误差归因于周期。

---

#### 三、BLS 自己的回溯评估:十年前预测 vs 实际(本线核心)

- **[A8]** BLS 设有专门的 Projections Evaluations 板块,最新一版评估的是 **2014–24** 周期(评估页 2026-04-10 更新)。BLS 已停止评估 labor force 与 macro 分项。
  - 口径:评估对象=2015 年发布的 2014–24 版预测,与 2024 实际值对照。
  - 来源:【官方】BLS · "Employment Projections Data Evaluations"(Projections Evaluations Homepage)· last modified 2026-04-10 · https://www.bls.gov/emp/evaluations/projections-evaluations.htm
  - 逐字摘引:"With the release of the 2014–24 Projections Evaluations, **BLS did not evaluate the 2014–24 Labor Force Projections or the Macro Projections.**"
  - 补充【官方】BLS · "Methods of Projections Evaluation" · last modified 2026-04-10 · https://www.bls.gov/emp/evaluations/methods.htm:"**Due to the impact of the COVID-19 pandemic on data for 2020, BLS did not evaluate the 2010–20 projections.**"(即 2010–20 这一版从未被公开体检)
  - 反证/矛盾测量:搜索角度——找是否有第三方替 BLS 做了 2010–20 评估;未发现。

- **[A9]** 【职业预测,最新一版体检】2014–24:BLS 预测的职业平均增长率 6.5%,实际 12.9% —— **实际增速是预测的近两倍**;方向(增/减)判对 86%。
  - 口径:分子/分母=职业组(occupational groups)的平均增长率,时间窗 2014→2024;"86 percent" 的分母 BLS 原文写作 "occupational groups"(Table 3 列出 22 个 major groups,须 Round 2 确认 86% 的确切分母)。22 个大组中,BLS 预测 4 组低于平均、10 组约等于平均、6 组高于平均、2 组下降;**实际是 3 组低于、1 组平均、14 组高于、4 组下降**。
  - 来源:【官方】BLS · "Occupational Projections Evaluation: 2014–24" · last modified 2026-04-10 · https://www.bls.gov/emp/evaluations/2014-2024-occupational.htm
  - 逐字摘引:"BLS correctly projected whether an occupational group would grow or decline 86 percent of the time." / "The projected average growth rate for occupations from 2014 to 2024 was 6.5 percent." / "The actual average growth rate for occupations from 2014 to 2024 was 12.9 percent." / 归因:"Recovery and expansion in the years following the Great Recession and the later COVID-19 pandemic contributed to actual average growth rates exceeding the projected average growth rate. **BLS projections assume stable GDP growth and a full-employment labor market in the target (end) year.**"
  - 反证/矛盾测量:BLS 在同页强调自己击败了 naive model —— 见 [A11]。

- **[A10]** 【产业预测,同一版体检】2014–24:大产业部门方向只判对 **69%**;非农工资薪金就业预测 149,132 千 vs 实际 158,569 千,**绝对百分比误差 6.0%,少算 9.4 百万个岗位**;CAGR 预测 0.6% vs 实际 1.3%。
  - 口径:employment in thousands;absolute percent error = |proj − actual| / actual。分部门误差:mining 57.7%、transportation and warehousing 28.2%、federal government 21.8%、construction 15.6%、utilities 14.6%、manufacturing 11.3%、information 7.8%、financial activities 7.4%、professional and business services 7.2%、leisure and hospitality 6.9%、educational services 5.2%、retail trade 3.8%、health care and social assistance 3.0%、state and local government 2.4%、other services 0.7%、wholesale trade 0.1%。
  - 来源:【官方】BLS · "Industry Projections Evaluation: 2014–24" · last modified 2026-04-10 · https://www.bls.gov/emp/evaluations/2014-2024-industry.htm
  - 逐字摘引:"BLS correctly projected which major industry sectors would grow and which would decline 69 percent of the time." / "...**utilities, information, and federal government were all expected to decrease, but instead experienced growth.** While BLS correctly predicted that the goods-producing sector as a whole would increase, BLS incorrectly predicted that mining would slightly increase and manufacturing would slightly decrease. Instead, mining saw an employment decline, and manufacturing saw employment growth."
  - 反证/矛盾测量:BLS 在 total nonfarm 上大幅优于 naive model(6.0% vs 13.0%);naive model 只在 utilities、educational services、leisure and hospitality、federal government 四个部门更准。

- **[A11]** 【最尖锐的一条】在**细分职业**层面,BLS 只在 820 个职业中的 475 个上打败了"份额不变"的朴素模型,即 **57.9% 的命中率**(略优于抛硬币)。
  - 口径:2014–24 occupational evaluation, Table 2 "Detailed occupations, combined scorecard":Sum of absolute differences of employment shares —— BLS 19.6 vs Naïve 21.1;Count of better score —— BLS 475 vs Naïve 345。475+345=820,**475/820 = 57.9%【本轮自算】**。大组层面 Table 1:BLS 9.6 vs Naïve 11.5,count 13 vs 9(22 组中 13 组胜出 = 59.1%【本轮自算】)。naive model 定义 = occupational–share naïve model,"assumes that the overall proportion of each occupation in the economy was not projected to change over the 10-year period"。
  - 来源:【官方】BLS · "Occupational Projections Evaluation: 2014–24" · https://www.bls.gov/emp/evaluations/2014-2024-occupational.htm ;naive 定义见 https://www.bls.gov/emp/evaluations/methods.htm
  - 逐字摘引(BLS 承认没有外部对照):"An important way to evaluate any projection is to compare it against other, similar projections. **This is not possible for occupational projections because there are no comparable projections which are not in some way derived from BLS projections.**"
  - 反证/矛盾测量:BLS 版本的辩护是"我们仍然赢了 naive"。公平地说,在 22 个大组的份额误差总和上 BLS 确实更小(9.6 vs 11.5),且 BLS 在 Computer and mathematical(0.45 vs 0.62)、Office and administrative support(1.44 vs 2.07)、Production(0.29 vs 0.84)、Healthcare practitioners(0.04 vs 0.55)等关键组上明显更准;naive 更准的组包括 Management(2.11 vs 2.17)、Education/training/library、Healthcare support(0.02 vs 0.46)、Transportation and material moving。

- **[A12]** 【上一版体检,可比对照】2012–22:方向判对 77%;预测平均增速 10.8% vs 实际 13.2%;"判对哪些组会跑赢大盘"只有 **67%**。
  - 口径:同类指标,时间窗 2012→2022。BLS 归因:"The actual growth rate was faster than projected because the labor force grew faster than projected and the unemployment rate in 2022 was lower than projected."
  - 来源:【官方】BLS · "Occupational Projections Evaluation: 2012–2022" · https://www.bls.gov/emp/evaluations/2012-2022-occupational.htm
  - 逐字摘引:"BLS correctly projected which occupational groups would grow faster than the economy as a whole 67 percent of the time."
  - 反证/矛盾测量:2012–22 与 2014–24 两版方向准确率从 77% 升到 86%,可以读成"在改善";但两版基期都在复苏期,偏差方向一致,不构成独立验证。

- **[A13]** 【系统性偏差方向会翻转 —— 这是本线最反直觉的发现】BLS 不是"总是高估"或"总是低估"。近两版(2012–22、2014–24)**系统性低估**;而 1996–06 / 1998–2008 / 2000–10 那三版**系统性高估**。误差方向由"基期处在周期的哪个位置"决定,而周期恰恰是 BLS 声明不预测的东西。
  - 口径:早期三版评估的关键结论 —— BLS 高估劳动参与率(2006 预测 67.6% vs 实际 66.2%;2008 预测 67.6% vs 实际 66.0%;2010 预测 67.5% vs 实际 64.7%),严重低估制造业下滑幅度,且"BLS consistently expected faster employment growth and a lower unemployment rate than did EIA in each of the three sets"。近两版则反向低估。
  - 来源:【官方】BLS · "Evaluation of BLS employment, labor force and macroeconomic projections to 2006, 2008, and 2010" · Monthly Labor Review · 2015 · https://www.bls.gov/opub/mlr/2015/article/evaluation-of-bls-employment-labor-force-and-macroeconomic-projections.htm
  - 逐字摘引:"BLS correctly expected that U.S. employment was moving toward a larger share of service sector jobs, with fewer opportunities in manufacturing. **However, the magnitude of the decline in manufacturing was greatly underestimated.**" / "Although these changes in trends were correctly anticipated, **BLS overprojected the labor force participation rate in all three sets of projections.**" / "BLS determined that the market was at its bottom and projected that very slight increases would occur in manufacturing employment between 1998–2008 and 2000–10."
  - 反证/矛盾测量:该文的 BLS 自评结论偏正面 —— "In broad strokes, the BLS projections performed well. The mean absolute errors in the BLS projections were very close to those of other government agencies."(对照 CBO、OMB、EIA;figure 1)。但同文承认 EIA 在非农就业上误差更小(0.4 vs 0.7 个百分点)。这条正反都要收。

- **[A14]** BLS 自 1999 年就发现:预测准确度**没有随时间提高**。
  - 口径:BLS 自评的历史结论,涉及 1988–2000 等更早周期。
  - 来源:【媒体/检索转述,追一手中】搜索结果引 BLS MLR 1999-05 文章(https://www.bls.gov/opub/mlr/1999/05/art3full.pdf,PDF)称"Broad trends in occupational employment have been projected fairly accurately, but accuracy has not increased over time",另有 1988–2000 评估称误差反映 "a conservative tilt to the projections"。
  - **【未取得全文】** —— 本轮未能逐字核对该 PDF 原文(bls.gov 403,该 PDF 未在 Wayback 抓取范围内成功取得)。Round 2 必须打开 https://www.bls.gov/opub/mlr/1999/05/art3full.pdf 逐字核实"accuracy has not increased over time"与"conservative tilt"两处措辞及其确切主语。

---

#### 四、openings 口径陷阱(用户特别指定的取证任务)

- **[A15]** 【核心数字】2024–34 期间,BLS 预测的年均 occupational openings 为 **1,886.33 万个/年**;其中来自"净岗位增长"的只有 **52.12 万个/年,占 2.8%**;其余 **1,834.21 万个/年、占 97.2%** 全部来自 separations(劳动力退出 815.50 万 + 职业转换 1,018.71 万)。
  - 口径:Table 1.10,"Total, all occupations",单位千人,2024–34 annual average。Employment 2024=169,956.1;2034=175,167.9;change=+5,211.8(十年);Labor force exits 8,155.0;Occupational transfers 10,187.1;Total separations 18,342.1;Occupational openings 18,863.3。恒等式:18,863.3 = 18,342.1 + 5,211.8/10 ✓。**占比 97.2% / 2.8% 为【本轮自算】**。
  - 定义限定语(极关键):openings **不包含**在同一职业内换工作的人 —— "This estimate of openings does not count workers who change jobs but remain in the same occupation." 因此 openings ≠ JOLTS 的 job openings(后者是某时点的空缺存量),两者绝不可混用。
  - 来源:【官方】BLS · Employment Projections Table 1.10 "Occupational separations and openings, projected 2024–34"(occupation.xlsx, National Employment Matrix)· 2025-08-28 · https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx ;定义见【官方】BLS · "Occupational Separations" · last modified 2025-08-28 · https://www.bls.gov/emp/documentation/separations.htm
  - 逐字摘引:"**In most occupations, openings due to separations of existing workers provide many more opportunities than employment growth does.**"
  - 反证/矛盾测量:搜索角度——找 BLS 是否在任何面向学生的材料里提示 openings 主要是"换人"而非"新增";Career Outlook 的 openings 榜单(见 [A16])并未在榜单旁标注这一点。

- **[A16]** openings 榜单会系统性地把人导向低薪、高流失职业:年均 openings 前 15 名中,**13 个的 2024 年中位年薪低于全职业中位数**,榜首"快餐及柜台服务员"年均 openings 904,300、中位年薪 30,480 美元、97.4% 的 openings 来自 separations、净增长仅 2.33 万/年。
  - 口径:Table 1.10 + Table 1.2 合并,Line item 级别。前 15(年均 openings 千人 / 中位年薪美元 / separations 占 openings %【本轮自算】):
    | 职业 | openings/年(千) | 中位年薪 | sep 占比 |
    |---|---|---|---|
    | Fast food and counter workers | 904.3 | 30,480 | 97.4% |
    | Home health and personal care aides | 765.8 | 34,900 | 90.3% |
    | Retail salespersons | 555.8 | 34,580 | 100.4% |
    | Cashiers | 542.6 | 31,190 | 105.8% |
    | Stockers and order fillers | 472.3 | 37,090 | 95.0% |
    | Waiters and waitresses | 456.7 | 33,760 | 100.4% |
    | Laborers and freight/stock movers | 384.3 | 38,940 | 98.9% |
    | Janitors and cleaners | 351.3 | 35,930 | 98.6% |
    | Customer service representatives | 341.7 | 42,830 | 104.5% |
    | General and operations managers | 308.7 | 102,950 | 94.7% |
    | Office clerks, general | 282.4 | 43,630 | 106.3% |
    | Cooks, restaurant | 250.7 | 36,830 | 91.3% |
    | Heavy and tractor-trailer truck drivers | 237.6 | 57,440 | 96.3% |
    | Nursing assistants | 204.1 | 39,530 | 98.4% |
    | Secretaries and admin assistants | 202.8 | 46,290 | 101.5% |
  - **占比 >100% 的含义**:该职业就业在**萎缩**(retail salespersons、cashiers、customer service reps、office clerks、secretaries 均为净减少),openings 全部来自补缺、且还不够补。榜单不区分这一点。
  - 来源:【官方】BLS Table 1.10 + Table 1.2(occupation.xlsx,同上);BLS 官方也以同样榜单形式对学生发布:【官方】BLS · "Education level and projected openings, 2024–34" · Career Outlook · 2025 · https://www.bls.gov/careeroutlook/2025/article/education-level-and-openings-2024-34.htm
  - 逐字摘引(BLS Career Outlook 自己承认):"Each of the occupations in chart 1, like most at this education level, **had wages below the median for all occupations.**"
  - 反证/矛盾测量:BLS 在该 Career Outlook 文章中确实按学历分组呈现,没有把所有学历混在一张榜上;真正混用的是二手媒体与择校榜单。Round 2 应找具体的中文/英文"最好就业专业"榜单实例来坐实。

- **[A17]** 【最反直觉的一条,可直接用于"选专业"结论】要求学士及以上学历的职业占 2024 年就业的 **29.9%**,却只占年均 openings 的 **20.6%** —— 但占十年净增岗位的 **58.0%**。openings 榜单和"增长"榜单会给出方向相反的建议。
  - 口径【全部本轮自算,基于 Table 1.2 的 "Typical education needed for entry" 字段,Line item 级加总,单位千人】:
    - 年均 openings 占比:High school diploma 35.8%(6,753.6)/ No formal credential 33.3%(6,287.8)/ Bachelor's 17.7%(3,333.5)/ Postsecondary nondegree award 6.2%(1,161.1)/ Some college 2.3% / Associate's 1.8% / Master's 1.7%(316.8)/ Doctoral or professional 1.3%(236.3)。**Bachelor's+Master's+Doctoral = 3,886.6 千/年 = 20.6%**。
    - 2024 就业占比:同三档合计 50,809.7 千 = **29.9%**。
    - 十年净增就业占比:Bachelor's 2,378.5 千(45.6%)+ Master's 391.7 千(7.5%)+ Doctoral 255.0 千(4.9%)= **58.0%**;而 High school 19.6%、No formal credential 12.1%、Some college **−157.0 千(−3.0%,唯一净减少档)**。
  - 机制:学位类职业的 separation rate 更低(人不容易离开),所以 openings 相对少 —— openings 少恰恰是"稳定"的表现,不是"机会少"。
  - 来源:【官方】BLS Employment Projections Table 1.2 "Occupational projections, 2024–2034, and worker characteristics, 2024"(occupation.xlsx)· 2025-08-28 · https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx
  - 反证/矛盾测量:该结论只说明"岗位结构",不说明"个人回报"。它不回答学费/机会成本/是否对口。绝不能单独用来论证"读本科划算"。另,"Typical education needed for entry" 是 BLS 的**指派字段**(BLS 判断该职业入门通常需要什么学历),不是在岗者的实际学历分布 —— 这是一个必须写清的口径限定。

- **[A18]** 【致命口径断层】2016–26 版之前的 openings 数字与之后的**完全不可比**,差约 4 倍;而且列名同时从"十年合计"变成了"年均",不加注意会造成约 40 倍的误读。
  - 口径【本轮自算,基于两个 vintage 的原始 Excel 表头与首行】:
    - 2014–24 版 Table 1.2 列名:"**Job openings due to growth and replacements, 2014-24**",Total all occupations = **46,506.9 千(十年合计)**,即约 465 万/年。
    - 2016–26 版 Table 1.2 列名:"**Occupational openings, 2016-26 annual average**",Total all occupations = **18,981.5 千(年均)**,即约 1,898 万/年。
    - 同口径年化对比:465 万/年 → 1,898 万/年,**方法变更导致的跳升约 4.1 倍**;若误把 46,506.9 与 18,981.5 直接并列,会得出"openings 腰斩"的完全错误结论。
  - 变更原因(BLS 自陈,措辞很重):BLS 从 1991 年到 2014–24 版一直用 cohort-component "replacement needs" 法,**该法已被废弃**,新的 separations 法自 2016–26 版启用,并首次把 gross occupational transfers 计入。
  - 来源:【官方】BLS · "Occupational Separations" · https://www.bls.gov/emp/documentation/separations.htm ;【官方】BLS · "Estimating Occupational Replacement Needs" · last modified 2025-08-28 · https://www.bls.gov/emp/documentation/replacements.htm ;原始数据:BLS Projections Archive · https://www.bls.gov/emp/projections-archive/2014-24.zip 与 https://www.bls.gov/emp/projections-archive/2016-26.zip
  - 逐字摘引(BLS 对自己旧数据的判决):"BLS used a cohort-component method for estimating job openings due to replacement needs from the 1991 through the 2014–24 projections. **This method is no longer in use because BLS identified statistical and conceptual issues with the implementation of this method that compromised the accuracy and validity of the resulting estimates.**" 以及旧法的核心缺陷:"...it requires a strong assumption: that workers who need to be replaced are those who are replaced by workers from different (usually younger) cohorts... **However, many workers do not remain in the same occupation throughout their career**."
  - 反证/矛盾测量:BLS 列出了新法的多项优势(可直接测量离开者、可拆分退出 vs 转换、可覆盖新职业、小职业更稳);没有第三方对新法提出质疑的一手来源被找到。搜索角度:"separations method critique"、"occupational transfers overstate openings";未发现独立批评。

---

#### 五、BLS 对计算机/软件类职业的历次预测 vs 实际(与线 B 直接对接)

- **[A19]** 【本轮自算的关键对照表】把 BLS 2015 年发布的 2014–24 版预测,与 2024 年实际值对照:BLS **同时低估了赢家的增长和输家的萎缩**,并且**根本没有"数据科学家"这个职业代码**。
  - 口径与重大限定语:2014 基期与预测值来自 2014–24 vintage(2010 SOC);2024 实际值来自 2024–34 vintage 基期(2018 SOC)。**SOC 分类 2018 年大改,两者非严格可比**;BLS 自己在评估中使用了正式 crosswalk(按拆分/合并做加总或比例分摊),我**没有**做这一步。单位:千人。
    | 职业 | 2014 实际 | 2024 **预测** | 2024 **实际** | 预测 vs 实际 |
    |---|---|---|---|---|
    | Computer and mathematical occupations (15-0000) | 4,068.3 | 4,599.7(+13.1%) | 5,416.7(+33.1%) | 少算 817.0 千 |
    | Software developers(2014: apps 15-1132 + systems 15-1133 → 2024: 15-1252) | 1,114.0 | 1,300.7(+16.8%) | 1,693.8(+52.0%) | **少算 393.1 千,实际增幅是预测的 3.1 倍** |
    | Information security analysts | 82.9 | 97.7(+17.9%) | 182.8(+120.5%) | 实际是预测的 1.87 倍 |
    | Computer and information systems managers (11-3021) | 348.5 | 402.2(+15.4%) | 667.1(+91.4%) | 实际是预测的 1.66 倍 |
    | Computer and information research scientists | 25.6 | 28.3 | 40.3 | 实际是预测的 1.42 倍 |
    | **Computer programmers** | 328.6 | 302.2(**−8.0%**) | 121.2(**−63.1%**) | **实际只有预测的 40%;BLS 大幅低估了崩塌** |
    | Computer systems analysts | 567.8 | 686.3(+20.9%) | 521.1(**−8.2%**) | **方向判反** |
    | Network and computer systems administrators | 382.6 | 412.8(+7.9%) | 331.5(**−13.4%**) | **方向判反** |
    | Computer user support specialists | 585.9 | 661.0(+12.8%) | 729.5(+24.5%) | 少算 |
    | **Data scientists (15-2051)** | 【2010 SOC 中不存在该代码】 | 【无法预测】 | 245.9 | **分类系统本身滞后于劳动力市场** |
  - 来源:【官方】BLS Projections Archive · 2014–24 vintage, occupation.xlsx Table 1.2 · https://www.bls.gov/emp/projections-archive/2014-24.zip ;【官方】BLS 2024–34 vintage occupation.xlsx Table 1.2 · https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx ;SOC 变更的官方说明见 https://www.bls.gov/emp/evaluations/methods.htm
  - 逐字摘引(BLS 对可比性的官方警告):"The Standard Occupational Classification (SOC) system used by Employment Projections is routinely re-evaluated so that it can capture new and emerging occupations. **When these changes occur, it can result in some occupations not being comparable between when the projection was made and when the projection can be evaluated.** SOC codes were updated in 2010 and again in 2018."
  - 反证/矛盾测量:**这是本轮最需要 Round 2 复核的一条**。风险点:(a) 2018 SOC 新设 15-1253 Software quality assurance analysts and testers(2024 年 201.7 千),其人员部分来自原 15-1199,可能虚增/虚减 developers 的对照;(b) Web developers 2014 版 148.5 → 预测 188.0,而 2018 SOC 把它拆成 15-1254 Web developers(86.0)+ 15-1255 Web and digital interface designers(128.9),合计 214.9,单看 86.0 会得出"腰斩"的错误结论;(c) OEWS 抽样与估计方法在此期间亦有变更。

- **[A20]** 【对"CS 饱和"叙事的直接反证,必须并列呈现】截至最新一版(2024–34),BLS **仍然**把 software developers 列为全经济体绝对增量第二大的职业(+267,700,+15.8%),并把 data scientists(+33.5%)与 information security analysts(+28.5%)列入增长最快的前五。BLS 明确表示这些数字**已经**把 AI 的影响考虑进去了。
  - 口径:2024–34,Line item 级。Software developers 15-1252:2024=1,693.8 千 → 2034=1,961.5 千,+267.7 千,+15.8%,中位年薪 133,080 美元,年均 openings 115.2 千(其中 76.7% 来自 separations【本轮自算】)。Data scientists 15-2051:245.9 → +82.5 千,+33.5%,中位年薪 112,590。Information security analysts 15-1212:182.8 → +52.1 千,+28.5%,中位年薪 124,910。
  - **同一张表里的反向证据**:Computer programmers 15-1251 −6.0%(中位年薪 98,670);Network and computer systems administrators 15-1244 −4.2%;Computer user support specialists 15-1232 −3.7%。**"计算机类"内部是分化的,不是整体涨或整体跌。**
  - 来源:【官方】Michael J. Rieley & Javier Colato · "Industry and occupational employment projections overview and highlights, 2024–34" · Monthly Labor Review, BLS · 2026-01 · https://doi.org/10.21916/mlr.2026.1 · https://www.bls.gov/opub/mlr/2026/article/industry-and-occupational-employment-projections-overview.htm ;数据见 occupation.xlsx Table 1.2/1.10
  - 逐字摘引:"Not only are they projected to experience employment growth that is over 5 times faster than the all-occupation average (15.8 percent), but they are also projected to have **the second-largest increase in employment of all occupations with 267,700 new jobs added through 2034.**" / AI 被写成利好:"The growing adoption of AI technologies, including generative AI tools, is another factor that will fuel strong job growth among computer and mathematical occupations." / 同文亦写 AI 的**利空**:"The growing adoption of AI technologies, including generative AI tools, and resulting productivity gains are expected to dampen labor demand in a variety of fields, such as sales, design, and administrative support."
  - 反证/矛盾测量:**这条论断的最强反证不是"BLS 错了",而是"BLS 测的不是同一件事"**。BLS 预测的是**存量总就业**,不区分年龄、经验、是否应届。Stanford Digital Economy Lab 的 Brynjolfsson / Chandar / Chen "Canaries in the Coal Mine?" 用 ADP 微观数据发现 22–25 岁软件开发者就业自 2022 年末下降约 20%,而同公司内资深开发者就业增长 —— 这与 BLS 的总量增长**在数学上完全兼容**。→ 该论文的完整取证归线 B;线 A 只负责标出这个口径边界。

---

### 交叉口径问题(Round 2 必须逐条核对)

1. **openings vs employment change**:同一张 BLS 表里两个数量级不同的量。2024–34 年均 openings 1,886 万,十年净增只有 521 万。任何"XX 职业未来十年有 X 万个机会"的说法,必须问是 openings 还是 change。**97.2% 的 openings 是补缺,不是新增**。
2. **openings 的"年均"vs"十年合计"标签在 2016–26 版被静默改写**。2014–24 版列名是十年合计(46,506.9 千),2016–26 起是年均(18,981.5 千)。任何跨版本的 openings 时间序列都是伪序列,除非明确说明。
3. **replacement needs 方法在 2016–26 版被整体替换,BLS 自陈旧法"compromised the accuracy and validity"**。所有引用 2016 年以前 BLS "job openings" 的中文/英文材料,都在引用一个 BLS 自己废弃的数字。
4. **BLS openings ≠ JOLTS job openings**。前者是流量(一年内有多少人需要被补上),后者是某时点的空缺存量;且 BLS openings 明确排除同职业内跳槽。二者绝不可并列。
5. **"5.2 million jobs / +3.1%" 不是需求预测**。它由 full-employment 假设锁定在劳动力预测(+5.35 million / +3.2%)上。把它读成"AI 时代岗位增长枯竭"是彻底的误读。
6. **"Typical education needed for entry" 是 BLS 的指派字段,不是在岗者实际学历分布**。用它算"多少 openings 需要本科"时必须写清。
7. **SOC 2010 → SOC 2018 的分类断层**。[A19] 的整张对照表都受此影响;BLS 自己的评估用了正式 crosswalk,我没有。Web developers 的拆分(15-1254 + 15-1255)是一个现成的踩坑例子:只看 15-1254 会得出"腰斩",合并后是增长。
8. **86% / 77% / 69% 三个"方向准确率"的分母各不相同**(2014–24 职业组 86%、2012–22 职业组 77%、2014–24 大产业部门 69%),而且 2012–22 还有一个更严格的指标"判对哪些组跑赢大盘 = 67%"。不要把这四个数并列。
9. **BLS 的"我们赢了 naive model"是一个很低的标杆**。naive model = 假设该职业占总就业的份额十年不变。细分职业层面 BLS 只赢了 57.9%(475/820)。媒体从不报道这个分母。
10. **误差方向不稳定**。近两版低估、更早三版高估。任何"BLS 系统性偏保守"或"BLS 系统性偏乐观"的单向断言都是错的,须写成"误差方向由基期在周期中的位置决定"。
11. **2010–20 这一版从未被公开评估**(BLS 以疫情数据为由跳过)。任何"BLS 预测被历次评估验证"的说法要扣掉这一版。

### 未取得/存疑

- **【未取得全文】** BLS MLR 1999-05 "How accurate are recent BLS occupational projections?"(https://www.bls.gov/opub/mlr/1999/05/art3full.pdf)。检索结果转述其结论为"accuracy has not increased over time"与 1988–2000 评估的 "a conservative tilt to the projections",但我未能打开 PDF 逐字核对(bls.gov 返回 403,Wayback 无该 PDF 可用快照)。**这两句话如果要进正文,Round 2 必须取得原文**,并确认"conservative tilt"的确切主语(是指方向保守还是幅度保守)。
- **【追不到一手 / 独立评估缺位】** 我搜了以下角度均未找到**非 BLS 作者**、针对 BLS 职业预测准确度的系统性量化评估:"independent academic evaluation BLS occupational projections accuracy"、"forecast error occupational projections journal article"、"critique BLS employment projections methodology peer reviewed"、"naive model benchmark occupational forecast"。检索到的 philarchive 条目 "Review of BLS Employment Projection Methodologies"(https://philarchive.org/archive/JOSROB-2)返回 403,**未能确认作者、发表状态与是否过审**,不可引用。**结论:BLS 的预测准确度评估在公开文献中基本是自评垄断的**,BLS 自己也承认没有可比外部预测("there are no comparable projections which are not in some way derived from BLS projections")。这本身就是一条可写进文章的发现。
- **【研究,明确非同行评审】** Peter Cappelli · "Skill Gaps, Skill Shortages and Skill Mismatches: Evidence for the US" · NBER Working Paper 20382 · 2014-08 · https://www.nber.org/papers/w20382 —— 封面页明写 "NBER working papers are circulated for discussion and comment purposes. **They have not been peer-reviewed**"。可用的逐字摘引:"**Governments do not have a particularly good record of forecasting where jobs will be years in advance, however, and students and their families would bear the costs when those forecasts are wrong.**" 这是我找到的唯一一条**独立学者对"用政府就业预测指导专业选择"的直接批评**,且它正是本文的论点。**存疑点**:该 WP 有已发表版本(Cappelli, ILR Review 68(2), 2015),Round 2 应核对该句在已发表版中是否保留、页码为何,并优先引用已过审版本。
- **【存疑,本轮未追一手】** 2025–26 年 BLS 预算与人员削减对数据质量的影响。检索到的均为媒体转述(Bloomberg、Fortune)与倡导组织(C2ER、COPAFS、CAP)材料,一手应为 DOL FY2026 Congressional Budget Justification。本轮**未取得**该文件,故本报告中不作任何断言。若线 A 要写"数据本身在变弱",Round 2 必须取 DOL/BLS 预算文件原文。
- **【时效确认】** 2024–34 是截至 2026-07-24 的最新一版;下一版(2025–35)预计 2026-08-27 发布(来源为检索转述的 BLS 发布日历,**Round 2 应核对 https://www.bls.gov/schedule/news_release/ecopro.htm 原页**)。成文时应写明"截至 2026 年 7 月,最新一版为 2024–34,发布于 2025 年 8 月 28 日"。

---

I have all the evidence. Writing up now.

## 线 B:美国应届生就业实测与"CS 已饱和"叙事对账

> **取证方式说明**:NY Fed 交互页对 WebFetch 返回 403,我从页面 JS bundle(`college-labor-chart.bundle.js`)中定位到其底层数据端点,直接下载了四份一手 CSV/JSON(`college-labor-outcomes-by-major-data.csv`、`college-labor-unemployment-data.csv`、`college-labor-underemployment-data.csv`、`college-labor-chart-meta.json`、以及工资分位数 xlsx)。历史口径通过 Wayback Machine 的 `id_` 原始快照取得四个不同发布年份的同一文件,做了逐格对账。以下所有 NY Fed 数字均为**逐格取自原始数据文件**,非媒体转述。本地留存于 `/private/tmp/claude-502/-Users-cissychen-Desktop-repos/8f82afa8-649c-4c17-b39f-b18b26c6bb77/scratchpad/`。

### 关键论断

---

- **[B1]** NY Fed"分专业结果"表当前一期发布于 2026 年 2 月 4 日,基于 **2024 年 ACS**(不是 CPS),覆盖 73 个专业。
  - 口径:数据文件自带元数据原文——`"releaseDateInfo": "February 4, 2026, based on data from 2024"`;来源标注为 `Source: U.S. Census Bureau, American Community Survey (IPUMS).`。注意:同一交互页的**月度失业率/低就业率折线图**用的是 **CPS(IPUMS)**,与本表不是同一数据源(见 [B15])。
  - 关键定义(逐字):
    - recent college graduates = "those aged 22 to 27 with a bachelor's degree or higher"(22–27 岁、**学士及以上**——注意是"及以上",不是"学士为最高学历")
    - 中位工资口径不同:"median wages are for full-time workers with a **bachelor's degree only**"(仅学士、且**全职**)
    - Early career = 22–27 岁;Mid-career = **35–45 岁**
    - "All figures exclude those currently enrolled in school."(排除在校生)
    - Graduate degree share 的分母又是另一个:25–65 岁、学士及以上
  - 来源:【官方】Federal Reserve Bank of New York · The Labor Market for Recent College Graduates(Outcomes by Major)· 2026-02-04 · https://www.newyorkfed.org/research/college-labor-market#--:explore:outcomes-by-major (数据文件:https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-outcomes-by-major-data.csv )
  - 反证/矛盾测量:搜索角度——NY Fed 是否公布该表的抽样误差/置信区间、样本量;**未发现**。数据文件与页面注释均不给 MOE 或 N。这本身是本线最大的方法论缺口(见 [B6])。

---

- **[B2]** "低就业率(underemployment)"的精确判定规则是 **O*NET 的 50% 门槛**,不是主观判断。
  - 口径:逐字——"The underemployment rate is defined as the share of graduates working in jobs that typically do not require a college degree. **A job is classified as a college job if 50 percent or more of the people working in that job indicate that at least a bachelor's degree is necessary; otherwise, the job is classified as a non-college job.**" 分子=在"非大学岗位"工作的毕业生;分母=**在业**毕业生(失业者不进入该比率)。判定依据来自 U.S. Department of Labor, O*NET 的从业者调查。
  - 来源:【官方】NY Fed · `college-labor-chart-meta.json`(`--#explore#underemployment` 节点)· 2026-05-05 · https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-chart-meta.json
  - 注意:这是一个**职业层面的粗分类**,不是"是否学以致用/对口"。一个 CS 毕业生去做产品经理、量化交易员,只要该职业 50%+ 从业者认为需要学位,就**不算** underemployed。中文语境的"专业对口率"与此**不等价**,不可互换。

---

- **[B3]** 【本线最核心的口径悖论】在最新一期(2024 ACS)中,Computer Science 在 73 个专业里**失业率倒数第 4(第 70 差)**,但**低就业率正数第 9 好**、**起薪第 2 高**。
  - 口径:73 个专业(不含 Overall 行)全排序,由我从原始 CSV 计算:
    | 专业 | 失业率 | 失业率排名(1=最低) | 低就业率 | 低就业率排名(1=最低) | 早期中位工资 | 排名(1=最高) | 中期中位工资 |
    |---|---|---|---|---|---|---|---|
    | Computer Engineering | 7.783% | 72/73 | 15.835% | 4/73 | $90,000 | **1/73** | $131,000 |
    | Computer Science | 6.992% | 70/73 | 19.127% | 9/73 | $87,000 | **2/73** | $120,000 |
    | Information Systems & Mgmt | 5.979% | 60/73 | 25.637% | 17/73 | $67,000 | 18/73 | $100,000 |
    | Mechanical Engineering | 4.364% | 43/73 | 20.088% | 10/73 | $80,000 | 7/73 | $120,000 |
    | Mathematics | 5.767% | 59/73 | 26.225% | 19/73 | $70,000 | 14/73 | $100,000 |
    | Economics | 3.524% | 27/73 | 33.094% | 30/73 | $72,000 | 12/73 | $115,000 |
    | Nursing | 2.147% | 10/73 | **12.781%** | **1/73** | $70,000 | 15/73 | $87,000 |
    | Elementary Education | 1.180% | 3/73 | 16.213% | 6/73 | $45,000 | 62/73 | $55,000 |
    | Biology | 4.292% | 39/73 | 51.130% | 60/73 | $45,000 | 64/73 | $83,000 |
    | Psychology | 4.985% | 52/73 | 48.291% | 50/73 | $45,000 | 66/73 | $72,000 |
    | History | 4.311% | 40/73 | 50.077% | 57/73 | $47,500 | 54/73 | $80,000 |
    | Fine Arts | 7.655% | 71/73 | 58.870% | 71/73 | $45,000 | 69/73 | $72,000 |
    | Art History | 6.688% | — | 45.263% | — | $45,000 | — | $91,000 |
    | Finance | 2.758% | 24/73 | 27.758% | 21/73 | $70,000 | 16/73 | $112,000 |
    | **Overall(全专业)** | **4.211%** | — | **39.350%** | — | **$58,000** | — | **$87,000** |
  - 失业率最高的 8 个专业:Anthropology 7.922、Computer Engineering 7.783、Fine Arts 7.655、Computer Science 6.992、Performing Arts 6.950、Architecture 6.844、Art History 6.688、Physics 6.631。
  - 低就业率最低的 12 个专业(依次):Nursing 12.781、Aerospace Eng 14.709、Civil Eng 15.567、**Computer Eng 15.835**、Special Ed 16.042、Elementary Ed 16.213、Chemical Eng 17.862、Construction Services 17.933、**Computer Science 19.127**、Mechanical Eng 20.088、Electrical Eng 21.106、Accounting 21.156。
  - 早期工资最高 10 名全部是工程/CS 类:CE $90k、CS $87k、Aerospace $85k、Chemical $85k、Industrial $83k、Electrical $82k、Mechanical $80k、General/Civil/Misc Eng 各 $75k。
  - 来源:【官方】NY Fed · 同 [B1] 数据文件 · 2026-02-04
  - **这就是"正反都在同一张表里"**:CS 更难找到"第一份工作",但一旦找到,几乎不会屈就于不需要学位的岗位,且薪资天花板全表第二。用失业率单指标判定"CS 已饱和"是选择性取数。

---

- **[B4]** CS 应届失业率**确实在上升**,而且我拿到了同口径的四个年份(这是 NY Fed 页面本身不提供的时序)。
  - 口径:同一文件 `college-labor-outcomes-by-major-data.csv` 的四个历史版本,均为 ACS、22–27 岁、学士及以上、排除在校生:
    | 发布日 | 数据年(ACS) | CS 失业率 | CS 低就业率 | CS 早期中位工资 | CE 失业率 | Overall 失业率 |
    |---|---|---|---|---|---|---|
    | 2023-02-10 | 2021 | 4.8% | 19.1% | $73,000 | 3.7% | 5.1% |
    | 2024-02-22 | 2022 | 4.267% | 16.654% | $78,000 | 2.311% | 3.557% |
    | 2025-02-20 | 2023 | **6.056%** | 16.456% | $80,000 | **7.538%** | 3.640% |
    | 2026-02-04 | 2024 | **6.992%** | 19.127% | $87,000 | **7.783%** | 4.211% |
  - 各年数据年份来自各版本 `college-labor-chart-meta.json` 中 `--#explore#outcomes-by-major` 的 `releaseDateInfo` 与 "Figures are for YYYY" 注释,逐版本核对。
  - 来源:【官方】NY Fed,四个 Wayback 原始快照:
    - 2021 数据 · http://web.archive.org/web/20231122172655id_/https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-outcomes-by-major-data.csv
    - 2022 数据 · .../web/20240507092624id_/...
    - 2023 数据 · .../web/20250416141515id_/...
    - 2024 数据 · .../web/20260303160457id_/...
  - 注意方向性:CS 失业率 2 年内从 4.27% → 6.99%(+2.7pp),但**低就业率 2022→2023 还在下降**(16.65→16.46),2024 才回到 19.13;**起薪同期从 $78k 涨到 $87k(+11.5%)**。三个指标不同向,不能只讲失业率那一条。

---

- **[B5]** 【最强反证之一,我自己算的】同一份数据的相邻两版之间,大量专业的失业率发生了**统计上不可信的巨幅跳变**,说明单年 ACS 分专业估计噪声极大。
  - 口径:2023 ACS 版 vs 2024 ACS 版逐专业比对,73 个专业全覆盖。失业率变化中位绝对值 **1.25pp**;**73 个中有 20 个绝对变化超过 2pp**。跳变最大的前 12 个:
    | 专业 | 2023 ACS | 2024 ACS | 变化 |
    |---|---|---|---|
    | Early Childhood Education | 1.298% | 6.593% | **+5.29pp** |
    | Performing Arts | 2.718% | 6.950% | +4.23pp |
    | **Nutrition Sciences** | **0.441%** | **4.536%** | **+4.09pp** |
    | Environmental Studies | 2.582% | 6.307% | +3.73pp |
    | **Art History** | **3.047%** | **6.688%** | **+3.64pp** |
    | Medical Technicians | 2.823% | 6.236% | +3.41pp |
    | Public Policy and Law | 5.513% | 2.237% | −3.28pp |
    | Mechanical Engineering | 1.529% | 4.364% | +2.83pp |
    | Chemical Engineering | 2.024% | 4.711% | +2.69pp |
    | Business Analytics | 2.392% | 5.034% | +2.64pp |
    | Architecture | 4.284% | 6.844% | +2.56pp |
    | Foreign Language | 4.040% | 1.579% | −2.46pp |
  - 对比:**CS 同期只变了 +0.94pp,CE 只变了 +0.25pp**。也就是说,CS/CE 的"高失业率"在两版之间是**稳定复现的**,而被媒体拿来做对照的"艺术史/营养学吊打 CS"则**一年就翻车了**——Art History 3.0%→6.7%,Nutrition Sciences 0.4%→4.5%。
  - 来源:【官方】NY Fed 原始数据,我基于 [B4] 两个版本计算。计算脚本与中间文件在上述 scratchpad 目录。
  - 这条同时是 **[B7] 叙事的反证**,也是 **[B4] 的部分佐证**(CS 的上升比其他专业的波动更稳定)。

---

- **[B6]** 独立机构用 ACS 微观数据复算了置信区间,结论是该表**分专业失业率的置信区间宽到不足以支撑任何专业间排序结论**。
  - 口径:作者 Connor O'Brien,用 2023 ACS(与 NY Fed 同源),22–27 岁、学士及以上。95% 置信区间:
    - Computer Engineering 点估计 7.5% → **CI 约 4%–11%**
    - Physics → CI 约 2%–12%
    - Public Policy → CI 约 0%–13%
  - 逐字摘引:"the confidence intervals around these estimates of recent grad unemployment are so large that it makes no sense to use them to make firm conclusions about the returns to particular majors."
  - 另一测量口径(该文主张改用的):Computer and Information Sciences 专业 22–27 岁的**就业人口比(EPOP)**,2023 年为 **90%**,文中称"by historical standards"仍属强劲。结论句:"News of the much-anticipated implosion of the computer science graduate job market is greatly exaggerated, at least for now." 文中另称计算机类职业就业增速仍为整体大学毕业生就业增速的约 4 倍。
  - 来源:【研究(非同行评审,智库博客)】Economic Innovation Group(EIG)· Agglomerations · "A viral chart on recent graduate unemployment is misleading" · 2025-08-13 · https://agglomerations.eig.org/p/a-viral-chart-on-recent-graduate
  - 反证/矛盾测量:EIG 自身是政策倡导型智库(非营利、非党派但有立场);且其 EPOP 论证**只回答"有没有工作"**,回避了"起薪/岗位层级"变化。另见 [B11]:Georgetown 用 3 年合并样本(直接缓解样本量问题)后,CS 上升趋势**依然成立**——这削弱了"纯粹是噪声"的解释。**这两条必须并列呈现。**

---

- **[B7]** "CS 已饱和"这一轮传播的**原始触发点可精确定位**:NY Fed 2025-02-20 发布的 2023 ACS 版本 → CNBC 2025-05-16 报道 → 病毒式传播。
  - 口径与对账:CNBC(记者 Jessica Dickler,标题《College majors with the best and worst job prospects — art history beats finance》,2025-05-16 发布 / 2025-06-05 更新)引用的数字,我**逐个回对到 2025-02-20 版原始 CSV**,完全吻合:
    | CNBC 引用 | 原始 CSV(2023 ACS 版) | 是否吻合 |
    |---|---|---|
    | Nutritional Sciences 0.4% | 0.441 | ✅ |
    | Art History 3% | 3.047 | ✅ |
    | Philosophy 3.2% | 3.180 | ✅ |
    | Finance 3.7% | 3.704 | ✅ |
    | **Computer Science 6.1%** | **6.056** | ✅ |
    | **Computer Engineering 7.5%** | **7.538** | ✅ |
    | Nursing 1.4% | 1.422 | ✅ |
    | CS/CE 起薪 $80,000 | 80000 / 80000 | ✅ |
  - 来源:【媒体】CNBC / Jessica Dickler · 2025-05-16 · https://www.cnbc.com/2025/05/16/college-majors-with-the-best-and-worst-employment-prospects.html (CNBC 直连 403;经其授权转载版核实:https://www.nbcwashington.com/news/business/money-report/college-majors-with-the-best-and-worst-employment-prospects-philosophy-now-outranks-finance/3915293/ );【官方】原始数据同 [B4]。
  - **该报道自身的口径混装**(必须在成文中点名):文中同时给出"2025 年 3 月应届生失业率 5.8%(同比 4.6%)",这来自 NY Fed **CPS 月度序列**(全部专业合计),却与 **2023 ACS 分专业**数字并排呈现,读者极易误读为"同一年、同一口径"。两者数据源、时间窗、频率全不同。
  - 另注:该 5.8% 本身也被后续修订过。NY Fed 2025-08 存档版对 2025 年 3 月给的是 **5.710%**,当前(2026-05-05)版修订为 **5.672%**——该序列做季调 + 三月移动平均,会**回溯修订**,引用时必须写明"截至哪一期"。

---

- **[B8]** 【反方一手证据】BLS 对 software developers 的十年增速预测仍是 **15%**,"much faster than the average"。
  - 口径:SOC 组合职业 "Software Developers, Quality Assurance Analysts, and Testers"(**三个职业合并**,不是 software developer 单列)。2024 年在业 **1,895,500** 人;2024–34 预测增长 **15%**,绝对增量 **+287,900**;年均岗位空缺 **约 129,200 个**(含替换性空缺);2024 年中位年薪 **$131,450**($63.20/小时);典型入门学历=学士。全职业平均增速为 3%。
  - 逐字摘引:"Overall employment of software developers, quality assurance analysts, and testers is projected to grow 15 percent from 2024 to 2034, much faster than the average for all occupations."
  - 来源:【官方】U.S. Bureau of Labor Statistics · Occupational Outlook Handbook, Software Developers, Quality Assurance Analysts, and Testers · 2024–34 预测(EP 项目)· https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm 【BLS 直连 403,内容取自 2026-07-05 的 Wayback 完整快照,Quick Facts 表与正文逐格核对】
  - **与 [B4] 不是同一构念,可以同时为真**:BLS 测的是**全年龄段职业存量的十年净增长 + 年均空缺流量**,基于宏观模型外推;NY Fed 测的是**22–27 岁某专业毕业生在某一年的当期失业率**。前者是"这个行业十年后有多少个位子",后者是"今年新人挤不挤得进去"。**存量扩张与入门口拥堵完全可以并存**——[B10][B16] 提供了这个机制的直接证据。
  - 反证:BLS 预测本身是模型外推,不是观测值;且 BLS 在 EP 中并未单独就生成式 AI 对入门岗的影响做结构性调整假设(未取得其假设文档全文,见"未取得/存疑")。

---

- **[B9]** 【"计算机"内部并不同向】同一 BLS 预测轮次里,Computer Programmers 是 **−6%(Decline)**。
  - 口径:2024 年在业 121,200 人;2024–34 变化 **−7,200 人(−6%)**;年均空缺仅约 5,500 个,且**全部**来自替换需求。2024 年中位年薪 $98,670。
  - 逐字摘引:"**Despite declining employment**, about 5,500 openings for computer programmers are projected each year, on average, over the decade. **All of those openings** are expected to result from the need to replace workers who transfer to other occupations or exit the labor force."
  - 来源:【官方】BLS OOH · Computer Programmers · 2024–34 · https://www.bls.gov/ooh/computer-and-information-technology/computer-programmers.htm 【同上,经 2026-07-10 Wayback 快照取数】
  - 意义:"学 CS = 做 software developer"是错误的一一映射。BLS 在同一分类体系下,把"开发者"判为 +15%、把"程序员"判为 −6%。**成文时不能用"计算机行业"这种模糊层级做论断。**

---

- **[B10]** 【招聘广告口径,非就业口径】Indeed 软件开发岗位广告量仍比疫情前基准低约 **27.5%–30%**,而全岗位广告量已回到基准线。
  - 口径:Indeed Job Postings Index,**季节调整,7 日滚动平均,2020-02-01 = 100**。这是**招聘广告存量指数**,不是雇佣数、不是就业人数,也不是失业率。
    - 截至 2026 年 6 月:software development ≈ **73**(即较 2020-02 低约 30%);全部岗位 JPI = **101.0**(2026-06-30),环比 +1.0%,同比 −3.7%。
    - 2026-07-08 文中表述为"about 27.5% below their pre-pandemic level"。
    - 回升的**结构**:2025-05 至 2026-05 软件开发岗位广告增量中,**71% 来自资深岗(senior roles)**,**37% 来自标题含 AI 的岗位**。自 2025-02-24 起算,美国软件开发岗位广告 **+15%**,同期全部岗位广告 **−7%**。
  - 逐字摘引:"Even after the recent rise, software development job postings remain about 27.5% below their pre-pandemic level, while overall job postings are essentially the same as in February 2020."
  - 来源:【商业调查(利益相关方:Indeed 是招聘平台)】Indeed Hiring Lab · "AI and Job Postings: From Destruction to Creation?" · 2026-07-08 · https://www.hiringlab.org/2026/07/08/ai-and-job-postings-from-destruction-to-creation/ ;Indeed Hiring Lab · "US Labor Market Snapshot — June 2026" · 2026-07-23 · https://www.hiringlab.org/2026/07/23/us-labor-market-snapshot-june-2026/
  - 已知偏差:Indeed 只覆盖在 Indeed 上发布的岗位,平台份额随时间变化会污染指数;且"广告数下降"可能反映**招聘方式变化**(内推、猎头、AI 筛选)而非需求下降。
  - **这条恰好解释 [B8] 与 [B4] 如何同时成立**:存量岗位十年增长,但当下的**新增招聘集中在资深岗**,入门口被压缩。

---

- **[B11]** 【独立复算,且用 3 年合并样本解决了 [B6] 的样本量问题】Georgetown CEW 用合并样本得出:CS 应届失业率 **7.2%**(2021–23),对比 2013–15 的 **4.3%**;computers/statistics/mathematics 大类应届失业率 **6.8%**,为 STEM 内最高,但同组应届中位收入 **$79,000**、75 分位 **$107,000**。
  - 口径:报告《The Major Payoff》,2025-10-16 发布,152 个专业。**recent college graduates = 22–26 岁**(注意:与 NY Fed 的 22–27 **不同**);prime-age = 25–54 岁。失业率为 **2021–2023 三年合并**估计(与 NY Fed 的单年 ACS 不同)。在线工具覆盖 142 个应届专业、152 个 prime-age 专业。
    - 全体 prime-age 学士 vs 仅高中:中位收入高 70%(**$81,000**),失业率 2.9% vs 6.2%
    - 应届中位收入区间:$34,000(communication disorders sciences and services)至 **$86,000(computer science)**
    - 应届失业率区间:1.3%(operations logistics and e-commerce)至 11%(film, video, and photographic arts)
    - 供给侧机制:2009–2023 年 computers/statistics/mathematics 大类**学位产出增长 159%**,为增长最快的专业大类
  - 逐字摘引(合著者、CEW 高级经济学家 Ban Cheah):"The number of students graduating with degrees in computers, statistics, and mathematics has ballooned by 159% between 2009 and 2023, but the unemployment rate for recent college graduates with degrees in these fields is now 6.8%—the highest within STEM." 以及关键的方法论提醒:"This illustrates that high unemployment does not always go hand-in-hand with low earnings—and vice versa."
  - 来源:【研究(大学研究中心报告,非同行评审)】Georgetown University Center on Education and the Workforce · The Major Payoff: Evaluating Earnings and Employment Outcomes Across Bachelor's Degrees · 2025-10-16 · https://cew.georgetown.edu/cew-reports/major-payoff/ ;新闻稿全文(已提取 PDF 正文)https://cew.georgetown.edu/wp-content/uploads/GeorgetownCEW_PressRelease_Major-Payoff_10.16.25.pdf ;配套博客(2026-02-12,作者 Catherine Morris)https://cew.georgetown.edu/resource/cew-blog-major-payoff/
  - **这是本线最重要的交叉验证**:用完全不同的年龄定义(22–26)、不同的样本策略(3 年合并)、不同的机构,得到**同向且量级接近**的结论(CS 7.2% vs NY Fed 2023 年 6.06% / 2024 年 6.99%),同时保留高薪结论。它同时削弱了 [B6] 的"纯噪声"解释,也削弱了 [B7] 的"CS 已完蛋"叙事。
  - 未取得:CEW 报告正文 PDF 与在线工具的完整分专业表(仅取得新闻稿 + 博客数字),见"未取得/存疑"。

---

- **[B12]** 【务必与 [B3] 区分】Census 官方"按学位领域"的 CS 中位收入是 **$108,500**,但那是**完全不同的人群**。
  - 口径:U.S. Census Bureau,ACS **2022** 年 1 年期数据,**25 岁及以上**、持学士及以上学位者,按**第一主修专业**分组的中位年收入。CS $108,500;Electrical engineering $121,600;Economics $101,400;General education $58,000;Social work $55,060;Fine arts $53,450。全部专业中位数区间在报告口径下从 $51,000 到 $146,000(CEW 口径)不等。性别差:"Women earned less than men across all fields of degree presented in this report, ranging from 70.8% to 90.5% of men's earnings."
  - 来源:【官方】U.S. Census Bureau · 新闻稿《Field of Bachelor's Degree Report》· 2025-07-09 · https://www.census.gov/newsroom/press-releases/2025/field-of-bachelors-degree-report.html ;明细表包 https://www.census.gov/data/tables/2022/demo/educational-attainment/acs-detailed-tables.html ;API 表号 **B15013**(按性别 × 学位领域的中位收入)、**B15014**(按年龄 25–39 / 40–64 × 学位领域的中位收入)、B15011、B15010,均在 `https://api.census.gov/data/2024/acs/acs1/groups.json` 中确认存在。
  - **口径陷阱**:$108,500(25 岁以上全体 CS 学位持有者,2022)vs NY Fed $87,000(22–27 岁、仅学士、全职,2024)vs CEW $86,000(22–26 岁,2021–23)。三个数字**都对**,但年龄段、学历限定、时间窗全不同,**绝不可并列**。
  - 未取得:B15014 的逐格数值——Census API 对多变量查询强制要求 API key(返回 "Missing Key"),我只取得了变量元数据与标签结构。**Round 2 需用 API key 或 data.census.gov 下载补齐**。注意 B15014 的分类是粗粒度大类("Computers, Mathematics, and Statistics"),不是 CS 单列,且年龄段是 25–39 / 40–64,与 NY Fed 的 22–27 / 35–45 **不可对齐**。

---

- **[B13]** 【宏观背景,非 CS 专属】美国应届生失业率已连续 **63 个月**高于全体劳动者失业率,这是 1990 年以来最长的一次倒挂。
  - 口径:NY Fed 月度序列,**CPS(IPUMS)**,季调 + 三月移动平均。recent graduates = 22–27 岁、学士及以上、排除在校生;all workers = 16–65 岁;college graduates = 22–65 岁学士及以上;young workers = 22–27 岁**无**学士学位。
    | 时点 | 应届生 | 全体劳动者 | 大学毕业生(22–65) | 22–27 岁无学位 |
    |---|---|---|---|---|
    | 2022-01 | 4.487% | 4.032% | 2.365% | 7.060% |
    | 2023-01 | 4.161% | 3.465% | 2.120% | 7.328% |
    | 2024-01 | 4.414% | 3.683% | 2.234% | 6.239% |
    | 2025-01 | 4.784% | 3.976% | 2.510% | 6.962% |
    | 2025-06 | 4.887% | 4.051% | 2.729% | 7.372% |
    | **2026-02(峰值)** | **5.819%** | 4.243% | 3.113% | 7.472% |
    | **2026-03(最新)** | **5.628%** | 4.227% | 3.073% | 7.244% |
  - 我从 435 个月的完整序列计算:1990-01 至 2026-03 共 435 个月中,应届生失业率高于全体劳动者的有 **88 个月**;当前连续倒挂始于 **2021-01**,已持续 **63 个月**;史上首次出现倒挂是 **2001-09**(4.693% vs 4.658%)。
  - 来源:【官方】NY Fed · `college-labor-unemployment-data.csv`,2026-05-05 发布(含 2026:Q1 数据)· https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-unemployment-data.csv
  - **重要限定**:NY Fed 明确注明 "October 2025 results are estimated due to missing data"(2025 年 10 月为估算值,疑因政府关门导致 CPS 采集中断)。引用 2025Q4 数据时必须带此限定。
  - **注意**:22–27 岁**无**学位者的失业率(7.2%)始终远高于应届毕业生(5.6%)。"读大学不划算"不能从这组数据推出。

---

- **[B14]** 应届生低就业率(41.5%)已回到 2022 年初水平,但**并非历史高位**。
  - 口径:同 [B13] 的 CPS 序列 + O*NET 判定([B2])。2026-03 = **41.494%**;2025-11 为 2022 年以来峰值 **42.416%**;2025-01 曾低至 **39.177%**;2022-01 为 41.565%;**1990-01 即为 42.918%**。全体大学毕业生(22–65)低就业率 2026-03 = 34.267%。
  - 来源:【官方】NY Fed · `college-labor-underemployment-data.csv` · 2026-05-05
  - **反证/矛盾测量**:媒体常报"低就业率创 2020 年以来新高"。从 35 年完整序列看,**41–43% 是长期常态**,1990 年就是 42.9%。NY Fed 自己也在旧文中指出这点(【官方/研究】Liberty Street Economics · "Working as a Barista After College Is Not as Common as You Might Think" · 2016-01 · https://libertystreeteconomics.newyorkfed.org/2016/01/working-as-a-barista-after-college-is-not-as-common-as-you-might-think/ ,**未取得全文**)。**"高位"必须指明是相对哪个基准年。**

---

- **[B15]** 【口径陷阱,必须写进成文】NY Fed 同一个交互页里的两组数字来自**两个不同数据源**,数值不可比。
  - 口径对照:
    | | Outcomes by Major 表 | 月度折线图 |
    |---|---|---|
    | 数据源 | **ACS**(IPUMS) | **CPS**(IPUMS) |
    | 频率 | 年度,单年 | 月度,季调 + 3 月移动平均 |
    | 最新一期 | 2026-02-04,2024 年数据 | 2026-05-05,含 2026:Q1 |
    | 应届生失业率(Overall) | **4.211%** | **5.628%**(2026-03) |
    | 应届生低就业率(Overall) | **39.350%** | **41.494%**(2026-03) |
  - 同一机构、同一网页、同一定义的人群,两个数字差 **1.4pp / 2.1pp**,纯粹因为数据源和时间窗不同。**媒体把"某专业 X%"(ACS 年度)和"应届生整体 Y%"(CPS 月度)并排放,是本线最高频的错误**,CNBC 那篇([B7])就犯了。
  - 来源:【官方】NY Fed `college-labor-chart-meta.json` 的 source 字段逐节点比对 · https://www.newyorkfed.org/medialibrary/research/interactives/data/college-labor-market/college-labor-chart-meta.json

---

- **[B16]** 【机制侧,支持"入门口收缩"】ADP 行政数据显示 22–25 岁 software developers 就业自 2022 年末峰值到 2025 年 9 月下降**近 20%**,同职业年长者未降。
  - 口径:ADP 工资单**行政数据**(非抽样调查),月度,覆盖数百万美国雇员。核心结果:
    - 22–25 岁、AI 高暴露职业:控制企业层面冲击后,**相对就业下降 16%**;有经验者稳定。
    - 22–25 岁在**最高 AI 暴露**职业:2022 年末至 2025 年 9 月就业 **−6%**,同期年长者 **+6% 至 +9%**。
    - Software developers 22–25 岁:至 2025-09 较 2022 年末峰值 **下降近 20%**(逐字:"By September 2025, employment for software developers aged 22-25 declined nearly 20% compared to its peak in late 2022")。
    - 调整发生在**就业量而非薪酬**;集中在 AI **替代(automate)**而非**增强(augment)**的职业;结果对剔除科技公司、剔除可远程职业均稳健。
  - 来源:【研究(工作论文,**未经同行评审**)】Erik Brynjolfsson, Bharat Chandar, Ruyu Chen · "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence" · 2025-11-13 版 · Stanford Digital Economy Lab / SIEPR Working Paper · https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ (PDF: https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf ,已下载并提取全文 5,909 行)
  - **作者自己的限定**(常被转述掉,务必保留):论文脚注 30 指出 CPS 中"22–25 岁 software developers 每月只有 26–53 个样本",这正是他们改用 ADP 的理由;脚注 31 明确呼吁用 ACS 交叉验证——"We encourage comparison of our findings to results from other data sources such as the ACS upon their release."
  - 已知偏差:ADP 客户群偏向特定企业规模/行业,不是全国代表性样本;且"AI 暴露度"用的是 Eloundou et al. (2024) 的**任务层面理论评分**,不是实际 AI 采用度的观测。

---

- **[B17]** 【机制侧反证】耶鲁 Budget Lab 用 CPS 全经济口径,截至 2026 年 3 月**未检出**可归因于 AI 的劳动力市场扰动。
  - 口径:CPS 月度,以 2022-11(ChatGPT 发布)为基准,计算职业结构与行业结构的**相异性指数(dissimilarity index)**,并与历史技术冲击基准对照(计算机 = 1984-01 基准;互联网 = 1996-01 基准;对照组 = 2016-01 基准);另按 AI 暴露度五分位比较就业/失业。
  - 逐字摘引(Key Takeaways,2026-04-16 更新版):
    - "While the occupational mix is changing more quickly than it has in the past, it is not a large difference and **predates the widespread introduction of AI** in the workforce."
    - "Currently, measures of exposure, automation, and augmentation **show no sign of being related to changes in employment or unemployment**."
    - "Better data is needed to fully understand the impact of AI on the labor market."
    - "The addition of the March 2026 CPS and the introduction of Anthropic's February usage metrics do not suggest any substantial changes to the analysis TBL released in March. Occupational dissimilarity, industry dissimilarity, and our exposure and usage metrics all remain flat, lie within historical ranges, or continue along the trends they were already exhibiting."
    - 唯一异动:"The most notable difference is an **uptick in the dissimilarity of occupational mix between older and younger college graduates**, though this remains at the high end of the historical range."(注意:这一条恰好**部分支持** [B16] 的年龄分化叙事)
    - 明确自限:"our analysis is not predictive of the future."
  - 关于青年:2026Q1 出现失业率上升迹象(全样本约 +0.5pp,16–34 岁子样本更大),但**统计不显著**。
  - 来源:【研究(智库,非同行评审)】The Budget Lab at Yale · "Tracking the Impact of AI on the Labor Market" · 2026-04-16 发布/更新 · https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-novemberdecember-cps-update (PDF 全文已提取:https://budgetlab.yale.edu/sites/default/files/page_to_pdf/1419/publication_1419.pdf );相关联合发布【研究/媒体】Molly Kinder, Martha Gimbel, Joshua Kendall, Maddie Lee · Brookings · "New data show no AI jobs apocalypse—for now" · 2025-10-01 · https://www.brookings.edu/articles/new-data-show-no-ai-jobs-apocalypse-for-now/
  - **[B16] 与 [B17] 并不直接矛盾**:前者是**职业 × 年龄的微观切片**(ADP 行政数据),后者是**全经济职业结构的宏观聚合**(CPS)。一个 22–25 岁软件开发者群体 −20% 的变化,在全经济职业结构相异性指数上完全可能看不见。Brookings 文中也承认 "AI may be contributing to unemployment among early-career workers",只是认为也可能是整体劳动力市场疲软。**成文时不能把这两篇写成"专家打架",要写成"两个不同分辨率的测量"。**

---

- **[B18]** 【线 F 用】NY Fed 提供了应届生年薪的**完整分位数序列**(1990–2025),可直接做分布重叠度分析。
  - 口径:CPS March Supplement(IPUMS)+ BLS CPI;**恒定 2025 年美元**;recent college graduates = 22–27 岁、**仅学士**;**全职**工作者;排除在校生。
    | 年 | P10 | P25 | P50 | P75 | P90 | P95 | P97 |
    |---|---|---|---|---|---|---|---|
    | 1990 | 29,638 | 44,357 | 58,138 | 73,929 | 91,312 | 105,964 | 123,214 |
    | 2019 | 30,227 | 40,302 | 56,675 | 81,864 | 113,350 | 147,355 | 182,619 |
    | 2020 | 31,096 | 43,535 | 62,193 | 87,070 | 118,167 | 149,263 | 180,360 |
    | 2022 | 29,429 | 41,812 | 57,216 | 79,223 | 110,031 | 137,539 | 159,546 |
    | 2023 | 31,701 | 44,381 | 63,402 | 82,422 | 110,953 | 142,654 | 169,072 |
    | 2024 | 30,792 | 44,135 | 61,584 | 82,112 | 112,904 | 153,960 | 169,972 |
    | **2025** | **30,002** | **45,000** | **60,000** | **85,000** | **130,000** | **160,000** | **190,000** |
  - 对照组:同口径 22–27 岁**仅高中**毕业者中位年薪:2020 $38,560 → 2025 **$40,000**。
  - 逐字限定(NY Fed 自己写的):"Note that some portion of the earnings gap could reflect **differences in aptitude** between graduates and non-graduates."(收入差距中有一部分可能反映能力差异,而非教育因果效应)
  - 来源:【官方】NY Fed · Distribution of Annual Wages 1990-Present, By Percentile(xlsx)· 2026-02-04 发布,含至 2025 年数据 · https://www.newyorkfed.org/medialibrary/Research/Interactives/Data/college-labor-market/Distribution-of-Annual-Wages-Various-Percentile
  - 关键观察(供线 F):**1990 至 2025 年,P50 从 $58,138 到 $60,000(实际基本零增长),但 P97 从 $123,214 涨到 $190,000(+54%)**。应届生内部的收入分散度在持续扩大——"选专业"的中位回报没怎么变,变的是尾部。

---

- **[B19]** 【供给侧一手数据】美国计算机与信息科学学士学位授予数 12 年间增长近 **1.7 倍**。
  - 口径:NCES Digest 表 325.35,"Degrees in computer and information sciences conferred by postsecondary institutions, by level of degree and sex of student: Academic years 1964-65 through 2021-22",学士层级、全部性别:
    | 学年 | 学士学位数 |
    |---|---|
    | 2009-10 | 39,593 |
    | 2013-14 | 55,271 |
    | 2017-18 | 79,597 |
    | 2019-20 | 97,054 |
    | 2020-21 | 104,883 |
    | **2021-22** | **108,503** |
  - 即 2009-10 → 2021-22 增长 **+174%**。来源注:"U.S. Department of Education, National Center for Education Statistics, Earned Degrees Conferred... through Completions component, IPEDS Fall 2000 through Fall 2022 (provisional data)."(2021-22 为**临时数据**)
  - 来源:【官方】NCES · Digest of Education Statistics 2023, Table 325.35 · https://nces.ed.gov/programs/digest/d23/tables/dt23_325.35.asp
  - 与 [B11] 的 CEW"159%(2009–2023)"**同向但不同口径**(CEW 是 computers+statistics+mathematics 合并大类,NCES 是 CIP 11 计算机与信息科学单列;年份终点也不同)。**不可互换引用。**
  - 意义:这是"饱和"叙事里唯一有扎实一手支撑的机制——**供给端确实翻了近三倍**。失业率上升可以是纯供给现象,不必然是需求崩塌。

---

### 交叉口径问题

**Round 2 必须逐条核对的陷阱:**

1. **【最高优先级】"CS 应届失业率 6.1%" 已经过期。** 该数字来自 NY Fed **2025-02-20** 发布的 **2023 ACS** 版本(原值 6.056)。当前(2026-02-04 发布、2024 ACS)是 **6.992%**。2026 年 7 月成文若仍写 6.1%,就是引用了两年前的数据年。同理 CE 的 7.5% → 现为 7.783%。**任何写"截至 2026 年 7 月"的文章必须用 6.99% / 7.78%,并标注数据年为 2024。**

2. **【最高优先级】NY Fed 同一页面两个数据源混装。** ACS 年度分专业表(Overall 失业率 4.211%)与 CPS 月度折线(2026-03 为 5.628%)不是同一口径。媒体几乎必然混用。见 [B15]。

3. **"22–27 岁、学士及以上"≠"学士为最高学历"。** NY Fed 失业率/低就业率分母含硕博;但**中位工资**分母是"仅学士 + 全职"。同一行表格里的两列人群不同。CS 的 graduate degree share 高达 32.7%,Biology 63.98%,这会实质性影响跨专业比较。任务书里写的"学士为最高学历"**不成立**,需修正。

4. **三个"CS 起薪"数字互不可比**:NY Fed $87,000(22–27,仅学士,全职,2024 ACS)/ CEW $86,000(22–26,2021–23 合并)/ Census $108,500(**25 岁以上全体**,2022 ACS)。第三个高出 25%,纯粹因为人群不同。

5. **BLS "+15%" 与 NY Fed "6.99%" 不是同一构念,不可对冲叙述。** 前者=全年龄职业存量十年净增长率(模型外推);后者=特定年龄段特定专业当期失业率(横截面观测)。二者可同时为真,机制见 [B10] 入门岗被压缩。且 BLS 的 +15% 是 developers+QA+testers **三职业合并**,同轮次的 computer programmers 是 **−6%**。

6. **"低就业率(underemployment)"≠中文"专业对口率"。** 前者是 O*NET 职业层面的 50% 学位门槛二分类,与所学专业**完全无关**——一个 CS 毕业生去做投行分析师不算 underemployed。中美对比时这是硬性构念不等价点。

7. **NY Fed 月度序列会回溯修订。** 2025 年 3 月的应届生失业率,2025-08 版为 5.710%,2026-05 版为 5.672%,媒体当时报 5.8%。原因是季调 + 三月移动平均重新估计。引用必须写"截至 X 期发布版"。

8. **2025 年 10 月数据为估算值。** NY Fed 原文:"October 2025 results are estimated due to missing data."(疑与联邦政府关门导致 CPS 采集中断有关,**此归因我未取得一手确认**)。任何跨 2025Q4 的趋势判断需带此限定。

9. **"艺术史/哲学吊打金融/CS"的媒体框架已被下一年数据自我推翻。** Art History 3.047% → 6.688%,Nutrition Sciences 0.441% → 4.536%(见 [B5])。若成文引用 CNBC 那篇,必须同时给出翻转后的数字,否则等于复制一个已证伪的结论。

10. **NCES 174% 与 CEW 159% 不可互换。** 不同专业聚合口径(CIP 11 单列 vs computers+stats+math)、不同年份终点(2021-22 vs 2023)。

11. **单年 ACS 分专业估计的 95% CI 可宽达 ±3.5pp**(CE:4%–11%)。任何"专业 A 比专业 B 高 0.5pp 所以 A 更差"的排序论断都不成立。但**跨年稳定复现的方向性**(CS 连续两版上升、CE 连续两版处于最高档)比单年点估计可信得多——这是 [B6] 与 [B4]/[B11] 之间的正确调和方式,不要简化成"数据不可信"。

---

### 未取得/存疑

**技术性访问障碍(来源确实存在,内容未取得或部分取得):**

1. **BLS 官网(bls.gov)对本环境全面 403**,包括 OOH 页面、`bls.gov/emp` 的 Employment Projections xlsx 表(occupation.xlsx / occupational-projections-and-characteristics.xlsx)。[B8][B9] 的数字取自 **Wayback Machine 的完整页面快照**(2026-07-05 / 2026-07-10),Quick Facts 表与正文逐格解析,可信度高,但**Round 2 建议用可访问 BLS 的环境复核**。另:**未取得 software developers(SOC 15-1252)与 QA analysts and testers(15-1253)分开的明细预测数**,只有合并数;EP Table 1.2 需要重取。

2. **FRED(fred.stlouisfed.org)与 St. Louis Fed 官网在本环境完全无法建立连接**(curl 返回 000)。因此:
   - Indeed 软件开发岗位广告指数的**逐月原始数值**(FRED series `IHLIDXUSTPSOFTDEVE`)**未取得**。[B10] 的 27.5% / ≈73 / 101.0 均来自 Indeed Hiring Lab 博客正文,是一手发布方但非逐格数据。
   - St. Louis Fed 的《Recent College Grads Bear Brunt of Labor Market Shifts》(2025-08)**完全未取得**,仅在搜索结果中确认其存在。

3. **Cleveland Fed Economic Commentary EC 2025-14,《Are Young College Graduates Losing Their Edge in the Job Market?》(2025)未取得全文**(clevelandfed.org 403)。这是一份联储研究评论,**与本线高度相关,Round 2 应优先补取**:https://www.clevelandfed.org/publications/economic-commentary/2025/ec-202514-are-young-college-graduates-losing-their-edge

4. **Census API 对多变量查询强制要求 API key**。表 **B15014**(按年龄 × 学位领域的中位收入,含 25–39 岁组)与 **B15013** 的逐格数值**未取得**,只确认了表的存在与变量标签结构。这是 [B12] 与线 F 分布分析的关键缺口。且需注意该表只有粗大类("Computers, Mathematics, and Statistics"),**没有 CS 单列**。

5. **Georgetown CEW《The Major Payoff》报告正文 PDF 与在线数据工具的分专业完整表未取得**,[B11] 的数字来自新闻稿 PDF 全文 + 官方博客。**未取得的关键信息:该报告用的 ACS 年份是否确为 2021–23 三年合并(博客提及 "2021–23" 与 "2013–15" 两个区间,但未见方法论章节)、142 个应届专业的完整失业率表、Computer Engineering 是否单列。**

6. **CNBC 原文 403**,[B7] 经其官方授权转载版(NBC Washington,同一记者同一标题)取得,内容应一致但**未逐字比对原页**。

7. **NY Fed 2019/2020 年份的 outcomes-by-major 数据未取得**。Wayback 对该 CSV 的最早快照是 2023-11-22(对应 2021 年数据)。若需 2019/2020 ACS 的 CS 失业率做更长时序,需另找 NY Fed 更早的数据文件路径或用 IPUMS ACS 自行复算。

**主动搜索但未找到的角度(记录以备 Round 2 换角度):**

8. **未找到 NY Fed 官方对"CS 失业率上升"的专题解释文章。** 搜索角度:Liberty Street Economics 站内的 recent college graduates + majors + computer science 组合;2025 年 5 月的《The College Economy》(Chakrabarti, Pham, Pierce, Pinkovskiy,2025-05-15)**明确不涉及分专业内容**,只讲整体大学溢价(就业溢价 11.9pp,2025 年 3 月)。**结论:NY Fed 发布了引爆舆论的数据,但从未自己写过一篇解释它的博客。** 这本身值得在成文中指出——所有"CS 已饱和"的因果解释都是第三方叠加上去的。

9. **未找到任何政府或联储机构对"CS 专业选择"给出规范性建议的一手文件。** 搜索角度:BLS/Education Dept/Fed 的 major-choice guidance。所有"该不该学 CS"的论断在一手来源层面**都不存在**,只有指标。

10. **未找到 NY Fed 公布该分专业表的样本量或标准误的任何官方文档。** 搜索角度:数据文件内元数据、页面 notes、技术附录。[B6] 的置信区间是第三方(EIG)自行用 ACS 微观数据复算的,**NY Fed 从未自己公布过**。

11. **未找到反驳 [B19] 供给侧解释的一手证据**(即"学位产出增长与失业率上升无关"的实证)。搜索角度:CS degree supply saturation labor market。CEW([B11])把二者并置陈述但**未做因果识别**。**供给侧解释目前是"合理但未经检验的假说",成文时不可写成已证实的因果。**

---

## 线 C:AI 暴露度研究的三方对垒(暴露 ≠ 替代)

> **本轮取证方式说明**:Eloundou 原文、Canaries 原文、EIG 批评文、Humlum 丹麦论文均已下载 PDF 并用 `pdftotext` 提取全文,下方逐字摘引来自全文原件,可信度高。Anthropic Economic Index 各期报告为网页,经 WebFetch 摘要器提取,**引号内文字属"经二次提取的原文片段",Round 2 必须回原页面逐字核对**,已在条目内标注。

---

### 关键论断

#### 一、Eloundou et al. "GPTs are GPTs"

- **[C1]** 该论文有**两个版本、两套不同的头条数字**,媒体和后续研究引用时经常混用。
  - 口径:arXiv 工作论文版(v5,2023-08-21,标题含 "An Early Look at")与 *Science* 正式发表版(2024-06-20,标题改为 "Labor market impact potential of LLMs",Science 384(6702):1306–1308)。arXiv 版摘要:80% 劳动力至少 10% 任务受影响、19% 劳动力至少 50% 任务受影响;人工标注下"仅 3% 的美国劳动者有超过一半任务暴露(仅 LLM 本体)"、"最多 49% 的劳动者可能有一半或以上任务暴露(含互补技术)"。Science 版摘要给出的是 **1.8%** 和 **46%**。
  - 来源:【研究·未过审版】arXiv · GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models · v1 2023-03-17,v5 2023-08-21 · https://arxiv.org/abs/2303.10130
  - 来源:【研究·已过审】Science · GPTs are GPTs: Labor market impact potential of LLMs · 2024-06-20 · https://www.science.org/doi/10.1126/science.adj0998(**science.org 返回 403,【未取得全文】**;1.8%/46% 两个数字经三处独立二手确认:GovAI 论文页 https://www.governance.ai/research-paper/gpts-are-gpts-labor-market-impact-potential-of-llms、NASA ADS 书目 2024Sci...384.1306E、搜索摘要)
  - 逐字摘引(arXiv v5 摘要):"Our findings reveal that around 80% of the U.S. workforce could have at least 10% of their work tasks affected by the introduction of LLMs, while approximately 19% of workers may see at least 50% of their tasks impacted. **We do not make predictions about the development or adoption timeline of such LLMs.**"
  - 逐字摘引(GovAI 转述 Science 版):"roughly 1.8% of jobs could have over half their tasks affected by LLMs with simple interfaces and general training… just over 46% of jobs"
  - 反证/矛盾测量:**RePEc 的记录至今未标注已发表**——"Papers 2303.10130, arXiv.org, revised Aug 2023",没有 published-version 字段。这意味着按 RePEc 引用的人会以为它仍是工作论文。搜索角度:arXiv abs 页 journal-ref 字段(空)、RePEc、Semantic Scholar、Science DOI 页(403)。

- **[C2]** exposure 的精确定义是**"能否把完成某任务/DWA 的时间在不降低质量前提下缩短至少 50%"**,不是"能否被替代"。
  - 口径:标注单位是 O*NET 的 task 与 DWA(Detailed Work Activity);阈值 = 时间减少 ≥50%;质量约束 = "第三方(通常是产出接收者)不会注意到或不在意有 LLM 参与";三档:E0 无暴露、E1 直接暴露(仅靠 ChatGPT/OpenAI Playground 即可达标)、E2 "LLM+"暴露(需在 LLM 之上再开发软件才能达标,含图像生成能力,单列为 E3 但分析时并入 E2)。作者明确说 50% 这个阈值"somewhat arbitrary"。
  - 来源:【研究】arXiv 2303.10130v5 · §3.3 Exposure 及附录 A.1 · 2023-08-22
  - 逐字摘引(rubric 原文):"**No exposure (E0) if:** using the described LLM results in no or minimal reduction in the time required to complete the activity or task while maintaining equivalent quality or … results in a decrease in the quality of the activity/task output. **Direct exposure (E1) if:** using the described LLM via ChatGPT or the OpenAI playground can decrease the time required to complete the DWA or task by at least half (50%). **LLM+ Exposed (E2) if:** access to the described LLM alone would not reduce the time … by at least half, but additional software could be developed on top of the LLM that could reduce the time it takes to complete the specific activity/task with quality by at least half."
  - 逐字摘引(阈值自陈):"Although this threshold is somewhat arbitrary, it was selected for ease of interpretation by annotators."

- **[C3]** 作者**四处明文声明 exposure 不等于自动化/替代**,且流传最广的"80%"用的是 β 口径(α + 0.5×E2),不是"80% 的人会被 AI 替代"。
  - 口径:三个指标 α = E1(下界)、β = E1 + 0.5×E2(主用口径)、ζ = E1 + E2(上界)。摘要中的 80%/19% 用 β。
  - 来源:【研究】arXiv 2303.10130v5 · §1 Introduction、§4.1、Table 4 脚注、§7 Conclusion
  - 逐字摘引(定义层):"**We define exposure as a proxy for potential economic impact without distinguishing between labor-augmenting or labor-displacing effects.**"
  - 逐字摘引(技术可行性 ≠ 结果):"This exposure measure reflects an estimate of the technical capacity to make human labor more efficient; however, **social, economic, regulatory, and other determinants imply that technical feasibility does not guarantee labor productivity or automation outcomes.**"
  - 逐字摘引(Table 4 脚注,针对"高暴露职业列表"):"occupations listed in this table are those where we estimate that GPTs and GPT-powered software are able to save workers a significant amount of time completing a large share of their tasks, **but it does not necessarily suggest that their tasks can be fully automated by these technologies.**"
  - 逐字摘引(结论):"while the technical capacity for LLMs to make human labor more efficient appears evident, it is important to recognize that social, economic, regulatory, and other factors will influence actual labor productivity outcomes."
  - 反证/矛盾测量:搜索角度——是否有作者本人或他人指出该论文被过度解读为"替代率";未发现作者公开的更正声明,但论文内部至少 4 处限定语被媒体系统性省略。

- **[C4]** 标注方法:人工标注者是 **OpenAI 自己的对齐标注承包商**(非各职业从业者),GPT-4 用的 rubric 与人类用的 rubric **不是同一份**;人机一致率随口径在 65.6%–82.1% 之间大幅波动,Pearson 相关最低仅 0.221。
  - 口径:Table 2,GPT-4 Rubric 1 vs Human:α 一致率 80.8%/r=0.223;β 一致率 65.6%/r=0.591;ζ 一致率 82.1%/r=0.654。人工方面,作者本人标注了明显需要体力/手部灵巧的 DWA,其余交给"reviewed GPT-3, GPT-3.5 and GPT-4 outputs as part of OpenAI's alignment work"的承包标注员。论文正文以人工标注为主结果。
  - 来源:【研究】arXiv 2303.10130v5 · Table 2、§3.3、§3.4.1、§3.4.2
  - 逐字摘引(标注者不具职业多样性):"A fundamental limitation of our approach lies in the subjectivity of the labeling. In our study, we employ annotators who are familiar with LLM capabilities. However, **this group is not occupationally diverse**, potentially leading to biased judgments regarding LLMs' reliability and effectiveness in performing tasks within unfamiliar occupations."
  - 逐字摘引(rubric 不同 + 无 ground truth):"there are slight differences between the rubric presented to humans and the one used for GPT-4… As a result, we use multiple annotation sources, but **none should be considered the definitive ground truth relative to the others.**"
  - 逐字摘引(标注员不知道对应职业):"Human annotators were mostly unaware of the specific occupations mapped to each DWA during the labeling process."
  - 逐字摘引(框架有效性风险):"If indeed, the task-based breakdown is not a valid representation of how most work in an occupation is performed, **our exposure analysis would largely be invalidated.**"

- **[C5]** 最高/零暴露职业名单(注意:人工与 GPT-4 排出来的名单几乎不重叠)。
  - 口径:Table 4,数字为"该职业中被判定暴露的任务占比(%)",任务等权重。
  - **人工 α 最高**:Interpreters and Translators 76.5、Survey Researchers 75.0、Poets/Lyricists and Creative Writers 68.8、Animal Scientists 66.7、Public Relations Specialists 66.7
  - **人工 β 最高**:Survey Researchers 84.4、Writers and Authors 82.5、Interpreters and Translators 82.4、Public Relations Specialists 80.6、Animal Scientists 77.8
  - **人工 ζ = 100%**:Mathematicians、Tax Preparers、Financial Quantitative Analysts、Writers and Authors、Web and Digital Interface Designers(人工共标 15 个职业为"fully exposed")
  - **GPT-4 α 最高**:Mathematicians 100.0、Correspondence Clerks 95.2、Blockchain Engineers 94.1、Court Reporters and Simultaneous Captioners 92.9、Proofreaders and Copy Markers 90.9
  - **GPT-4 ζ = 100%**:Accountants and Auditors、News Analysts/Reporters/Journalists、Legal Secretaries、Clinical Data Managers、Climate Change Policy Analysts(GPT-4 共标 **86 个**职业为 fully exposed,是人工的 5.7 倍)
  - **零暴露职业(附录 D,无任何被标暴露任务)**:Agricultural Equipment Operators、Athletes and Sports Competitors、Automotive Glass Installers、Bus and Truck Mechanics、Cement Masons、Cooks(Short Order)、Derrick Operators(Oil and Gas)、Dishwashers、Dredge Operators、Electrical Power-Line Installers、Floor Layers、Foundry Mold and Coremakers、Helpers–Carpenters / Roofers / Plumbers 等、Meat/Poultry/Fish Cutters、Motorcycle Mechanics、Pile Driver Operators、Pourers and Casters(Metal)、Rail-Track Laying Equipment Operators 等
  - 来源:【研究】arXiv 2303.10130v5 · Table 4、Appendix D
  - 反证/矛盾测量:作者自陈这套排序有明显反直觉结果——"not weighting relative importance of a task to a given occupation yields some curious results (**e.g. ranking Barbers as having reasonably high exposure**)";GPT-4 口径下 Barbers、Blockchain Engineers 等排名也可疑。**给准大学生的提示:E1 高不等于"该专业没前途",Mathematicians ζ=100% 与"数学家会失业"是两码事。**

---

#### 二、Anthropic Economic Index

- **[C6]** 它测的是 **Claude 用户对话在 O*NET 任务上的分布(使用分布)**,不是就业影响,也不是全劳动力代表性样本。厂商自有数据,应按**【商业/厂商口径】**处理。
  - 口径:首期(2025-02-10)基于 Clio 隐私保护系统,约 100 万条 Claude.ai Free/Pro 对话(配套论文 arXiv:2503.04761 为 400 万+ 条);把对话映射到美国劳工部 O*NET 的约 20,000 条任务。
  - 来源:【商业调查/厂商】Anthropic · Introducing the Anthropic Economic Index · 2025-02-10 · https://www.anthropic.com/news/the-anthropic-economic-index
  - 来源:【研究·预印本,未过审】Handa, Tamkin, McCain, Huang, Durmus, … Amodei, Kaplan, Clark, Ganguli · "Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations" · arXiv:2503.04761,提交 2025-02-11 · https://arxiv.org/abs/2503.04761
  - 逐字摘引(摘要,作者自陈边界):"While our data and methods face important limitations and **only paint a picture of AI usage on a single platform**, they provide an automated, granular approach for tracking AI's evolving role in the economy and **identifying leading indicators of future impact**"
  - 逐字摘引(摘要,核心数字):"AI usage primarily concentrates in software development and writing tasks, which together account for nearly half of all total usage… approximately **36% of occupations using AI for at least a quarter of their associated tasks**… **57% of usage suggests augmentation** of human capabilities (e.g., learning or iterating on an output) while **43% suggests automation** (e.g., fulfilling a request with minimal human involvement)."

- **[C7]** automation vs augmentation 的分类比例**在两年内发生方向性反转,且分类器换过模型**,不可跨期直接比较。
  - 口径与时序:
    - **2025-02(首期,Claude.ai Free/Pro)**:automation 42.6%(Directive 27.8% + Feedback Loop 14.8%),augmentation 57.4%(Task Iteration 31.3% + Learning 23.3% + Validation 2.8%)。定义:Directive = "Complete task delegation with minimal interaction";Task Iteration = "Collaborative refinement process"。职业大类占比:Computer & Mathematical 37.2%、Arts/Design/Media 10.3%、Education & Library 9.3%、Office & Admin 7.9%、Life Sciences 6.4%、Business & Financial 5.9%。仅约 **4%** 的职业把 AI 用于其 ≥75% 的任务。
    - **2025-09(Claude.ai 数据窗 2024-12 至 2025-08;API 数据窗 2025-08,约 100 万条随机抽样 transcript)**:Claude.ai 上 directive 从 27%(V1)升至 39%(V3),automation 份额**首次越过 50%**;**第一方 API 上 automation-dominant 占 77%,augmentation 约 12%**;任务层面 API 有 97% 的任务呈 automation-dominant,Claude.ai 仅 47%。Claude.ai V3 任务大类:Computer & Mathematical 36%、Education & Library 12.4%、Life/Physical/Social Sciences 7.2%、Business & Financial 3%;API:Computer & Mathematical 44%。
    - **2026-03「Learning curves」(数据窗 2026-02-05 至 02-12,100 万条对话)**:Claude.ai 上 augmentation 小幅回升,API 上 automation "decreased sharply";top-10 任务占比 19%,低于 11 月的 24%;Claude.ai 上 Computer & Mathematical 35%、个人用途 42%、课业 12%。
    - **2026-06「Cadences」(数据窗 2026-04-10 至 06-10)**:覆盖 Claude.ai chat、Claude Desktop、Claude Code、第一方 API;约 9,700 名调查受访者与使用数据关联;产出类型 explanations 17%、documents/reports 15%、guidance 11%;个人用途工作日约 35%、周末约 50%。受访者中 Computer & Mathematical 约 30%(全美就业占比约 4%)、Management 23%(全美约 7%)。
  - 来源:【商业调查/厂商】Anthropic · Introducing the Anthropic Economic Index · 2025-02-10 · https://www.anthropic.com/news/the-anthropic-economic-index
  - 来源:【商业调查/厂商】Anthropic · Anthropic Economic Index report: Uneven geographic and enterprise AI adoption · 2025-09-15 · https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
  - 来源:【商业调查/厂商】Anthropic · Anthropic Economic Index report: Learning curves · 2026-03-24 · https://www.anthropic.com/research/economic-index-march-2026-report
  - 来源:【商业调查/厂商】Anthropic · Anthropic Economic Index report: Cadences · 2026-06-26 · https://www.anthropic.com/research/economic-index-june-2026-report
  - 逐字摘引(9 月报告的可比性自陈,**需 Round 2 回原页核对**):"V3 uses Claude Sonnet 4 for classification, while V2 used Sonnet 3.7, **which complicates direct comparison**"
  - 逐字摘引(6 月报告的代表性自陈,**需 Round 2 回原页核对**):"The Economic Index Survey is **not representative of the general population**. We reach a random sample of Claude users, there may be selection in who completes the survey, and we filter out infrequent users from our analysis."
  - 逐字摘引(首期限制,经提取):无法确认对话是否与工作相关;不知用户如何使用回复(复制粘贴 vs 编辑);只覆盖 Claude.ai 计划、不含 API/Enterprise;Clio 可能误分类;Claude 当时不能生成图像因而低估创意类用途;**编程用途可能因 Claude 的市场定位而被高估**。
  - 反证/矛盾测量:9 月报告自曝数据污染——"When further investigating Utah's activity, we discovered a notable fraction of its usage appeared to be possibly associated with **coordinated abuse**"。这直接说明该指数的地理/份额数字含非人类或滥用流量。搜索角度:是否有第三方复现 Anthropic 的 automation/augmentation 分类——未发现独立复现(唯一的外部使用是 Brynjolfsson 等把它当外生暴露度变量,见 C11)。

- **[C8]** Anthropic 自己在 2026-03 另发了一篇**尝试跨过"使用分布→就业"这道坎**的研究,结论比媒体叙事保守得多。
  - 口径:提出 "observed exposure",把 Eloundou et al.(2023)的任务级能力估计 × Anthropic 自有使用数据(偏重 automated 且 work-related 的用途),覆盖 O*NET 800+ 职业,再对接 CPS 就业结果与 BLS 2024–2034 就业预测。关键数字:Computer Programmers 暴露最高(coverage 75%);30% 的劳动者 coverage 为零;高暴露劳动者平均薪资高 47%,研究生学历占比 17.4% vs 未暴露组 4.5%;coverage 每升 10 个百分点,BLS 预测增长率降 0.6 个百分点;**自 2022 年底以来未检测到暴露组失业率显著上升**;但 22–25 岁在暴露职业的 **job-finding rate 下降 14%**。
  - 来源:【商业调查/厂商 + 研究】Anthropic · Labor market impacts of AI: A new measure and early evidence · 2026-03-05 · https://www.anthropic.com/research/labor-market-impacts
  - 逐字摘引(**需 Round 2 回原页核对**):"This approach won't capture every channel through which AI could reshape the labor market";并自陈找到 "limited evidence that AI has affected employment to date"。
  - 反证/矛盾测量:该文本身就是对 Canaries 叙事的部分反证(总体失业无显著上升)又是部分佐证(青年 job-finding 下降 14%)。注意**利益相关**:Anthropic 既是 AI 厂商,其 CEO 又是"AI 将消灭半数入门级白领岗"这一公开预测的提出者(见 C9 口径),该公司发布的"影响有限"结论与其 CEO 公开表态方向相反,值得 Round 2 单独审。

---

#### 三、Brynjolfsson, Chandar & Chen "Canaries in the Coal Mine?"

- **[C9]** 核心发现:**22–25 岁、在 AI 最暴露职业的劳动者,相对就业下降 16%**;这是**工作论文,未经同行评审**。
  - 口径:摘要原文口径 = "Early-career workers (ages 22-25) in AI-exposed occupations experienced 16% **relative** employment declines, **controlling for firm-level shocks**"。注意是"相对下降"(相对最低暴露五分位),不是绝对下降 16%。分子分母见下:
    - **Fact 2(绝对口径)**:2022 年末至 2025 年 9 月,22–25 岁在**最暴露职业**的就业下降 **6%**,同期年长组**上升 6–9%**。
    - **Fact 4(带 firm-time 固定效应的事件研究)**:22–25 岁最高暴露五分位相对最低五分位,**15 log points** 的相对就业下降,统计显著;其他年龄组估计量"much smaller in magnitude and not statistically significant"。
  - 数据:ADP(全美最大薪资服务商,为雇佣超 2500 万美国劳动者的企业提供服务)月度个人级薪资记录,**2021 年 1 月至 2025 年 9 月**;主分析样本每月 **350 万–500 万**劳动者;仅 22–25 岁一档每月就有 **25 万–35 万**名有薪资记录的在职者(论文用此对比 CPS:CPS 每月全年龄在职受访者仅 44,000–51,000 人,其中 outgoing rotation group 含收入记录者仅 10,000–12,000 人)。ADP 只对约 **70%** 的劳动者观测到职位名称,无职位名称者被剔除;职位名称经推断映射到 2018 SOC。
  - 发表状态:【研究·工作论文,未过审】Stanford Digital Economy Lab / SIEPR Working Paper,版本日期 **2025-11-13**(初版 2025-08-26)。作者署 Stanford + NBER,但未见 NBER WP 编号或期刊。
  - 来源:【研究·工作论文】Brynjolfsson, Chandar & Chen · Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence · 2025-11-13 · https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf
  - 逐字摘引(摘要):"Adjustments occur primarily via employment rather than compensation, with employment changes concentrated in occupations where AI automates rather than augments labor. Results are robust to excluding technology firms and occupations that are remotable. These six facts provide **early large-scale evidence consistent with** generative AI disproportionately impacting entry-level workers"
  - 逐字摘引(作者自设的因果保留):"While we explore a variety of alternative explanations, **we caution that the facts we document may in part be influenced by factors other than generative AI.** Taken as a whole, our results are **consistent with the hypothesis** that generative AI has begun to affect entry-level employment."
  - 逐字摘引(样本代表性自陈):"the distribution of firms using ADP services **does not exactly match** the distribution of firms across the broader US economy"(并引 Cajner et al. 2018 指出 ADP 高估东北部企业、ADP 企业平均增长快于全美典型企业)

- **[C10]** 六个 fact 的完整表述(用于防止媒体只引第一条)。
  - Fact 1:22–25 岁在最暴露职业(如 software developers、customer service representatives)就业大幅下降;同职业的资深工作者、以及低暴露职业(如 nursing aides)所有年龄段稳定或继续增长。
  - Fact 2:总体就业仍稳健增长,但青年就业自 2022 年末起停滞;低暴露职业中青年与年长者增速相当。
  - Fact 3:**并非所有 AI 用途都伴随就业下降**——自动化型用途伴随入门级就业下降,增强型用途反而伴随就业增长。
  - Fact 4:控制 firm-time 效应后结论仍在(15 log points)。
  - Fact 5:调整体现在**就业量**而非**薪酬**;各年龄、各暴露五分位的年薪趋势差异很小,提示工资黏性。
  - Fact 6:对多种替代样本构造稳健(剔科技公司、剔可远程职业、剔计算机类 SOC 15-1、高/低大学学历占比职业分别看);且该暴露度分类**在 LLM 普及之前(含 COVID 失业高峰期)并不能预测青年就业结果**。
  - 来源:同 [C9]
  - 逐字摘引(Fact 3 的方法):"We distinguish between automation and augmentation empirically using **estimates of the extent to which observed queries to Claude, the LLM, substitute or complement the tasks in that occupation.**"
  - 逐字摘引(Fact 5 的双向解读,作者自己给的):"AI may have larger effects on employment than on wages, at least initially, **or even that AI may boost wages for as many workers as it hurts.**"

- **[C11]** **⚠️ 三项研究并非彼此独立:Canaries 的"AI 暴露度"自变量,直接就是 Eloundou 的 GPT-4 β 分数和 Anthropic Economic Index。**
  - 口径:论文 §"我们用两种方法测职业 AI 暴露度":(1) Eloundou et al.(2024)按 O*NET 任务估计的暴露度,聚合到 2018 SOC,**"We focus on the GPT-4 based β exposure measures from their paper."**;(2) Anthropic Economic Index(Handa et al. 2025)基于数百万条 Claude 对话的 O*NET 任务级使用数据,该指数对每个任务给出 automation/augmentation 类查询占比,被用来构造 automation 暴露与 augmentation 暴露。用 BLS 的 2010→2018 SOC crosswalk 合并到薪资数据。
  - 来源:同 [C9],数据与测量章节
  - 反证/矛盾测量:这构成一条**引用链风险**——如果 Eloundou 的 rubric 有系统偏差(C4 已列作者自陈的多项),Canaries 的分组也随之偏。作者自己发现两套暴露度**在安慰剂检验中表现不同**:"for the Eloundou et al. (2024) measures the most exposed quintile had **slower employment growth starting around 2020**. This is not the case for the Anthropic exposure measures"——即 Eloundou 口径在 2020 年就已经"预测"到下降,这正是 EIG 反驳的抓手(见 C13)。另注:第 1、2 个 augmentation 五分位的 Claude 使用量极低(占对话 0.01% 和 0.09%),即最"增强型"分组其实是**样本极稀薄**的分组。

- **[C12]** **版本漂移:头条数字从 13% 变成 16%**,媒体两个数字同时在流通。
  - 口径:2025-08-26 初版为"约 13% 相对下降";2025-11-13 版摘要为 16%。EIG 的批评文明确写"Our comments in this note were written about the original version of the 'Canaries' paper published on 26 August 2025"。
  - 来源:【研究·工作论文】Stanford Digital Economy Lab,两版对照(Nov25 PDF 摘要 vs 2025-08 版被 EIG 与多家媒体引作 13%)
  - 来源:【媒体】Silicon Canals / Fortune 等仍在 2026 年引用 13% · 例:https://fortune.com/2026/06/27/what-is-ai-impact-entry-level-jobs-stanford-adp-canaries-brynjolfsson-richardson/
  - 反证/矛盾测量:见交叉口径问题第 3 条。

- **[C13]** 作者本人 2026-02 的更新承认:**加入最广泛控制后,下降只在 2024 年之后才显著**——与"ChatGPT 发布即刻见效"的原叙事时点不同。
  - 口径:2026-02-09 Stanford Digital Economy Lab 博文,回应两条批评(利率是否比 AI 暴露度更能解释;时点是否合理)。使用 Eloundou et al.(2024)暴露度 + Zens et al.(2020)利率敏感度 + firm-time 固定效应回归,数据延至 2025 年 10 月。
  - 来源:【研究·机构博文,未过审】Stanford Digital Economy Lab · Canaries, interest rates, and timing: more on recent drivers of employment changes for young workers · 2026-02-09 · https://digitaleconomy.stanford.edu/news/canaries-interest-rates-and-timinga-more-on-recent-drivers-of-employment-changes-for-young-workers
  - 逐字摘引(**经 WebFetch 提取,需 Round 2 回原页核对**):"more AI-exposed jobs are actually **less** exposed to interest rates on average";控制更广宏观因素后,就业下降 "significant only after 2024"。
  - 反证/矛盾测量:这条本身就是对该论文早期版本时点主张的部分自我修正,应作为"作者已让步的部分"记录。

---

#### 四、对 Canaries 的独立批评与反向证据(重点)

- **[C14]** **最系统的批评:EIG《Looking for the Ladder》——用 Lightcast 招聘广告数据指出时点对不上,主因是加息周期不是 AI。作者是 Google 首席经济学家团队,利益相关必须标注。**
  - 口径:数据 = Lightcast Job Posting Analytics,**2019 年 9 月至 2025 年 8 月共 2.38 亿条美国招聘广告(月均约 330 万条)**,767 个 6 位 SOC 职业 × 21 个 2 位 NAICS 行业;资历分级用 Lightcast 自有的 Junior/Intermediate/Senior 专有分类(由职位名与描述推断)。AI 暴露五分位**用的是 Eloundou et al.(2024)复现包、GPT-4 β 分数、等权重方案——与 Canaries 同一基础**。
  - 关键论点:
    1. **时点错位**:最高 AI 暴露五分位的职位空缺在 **2022 年 3–4 月见顶**并全年下滑,比 ChatGPT(2022-11)早半年以上;OpenAI API 到 2023-03-01 才发布,ChatGPT Enterprise 到 2023-08-28 才上线。
    2. **企业采用率太低**:美国普查局数据显示,即使到 2023 Q4,**大企业中计划未来六个月用 AI 生产商品/服务的不到 10%**;到 2025 Q3 也只升到 12%(且同期 250 人以上企业"过去两周实际使用"不到 6%)。
    3. **年龄段机械性收缩**:22–25 岁这个窄年龄带几乎完全靠新招聘补充,老年龄带会被下面的人"自然递补"。作者给出反例算术——**一个各年龄人数相等、完全冻结招聘但零裁员的职业,一年后 22–25 岁就业会"暴跌 25%",而其他年龄段纹丝不动。**
    4. **AI 暴露度与利率敏感度高度共线**:2023 年普查数据显示,最高 AI 暴露五分位中约 **38%** 的劳动者就业于 Information、Finance and Insurance、Professional and Technical Services;最低暴露五分位中**不到 2%**。
    5. **安慰剂**:2020 年初的招聘冷却期,"AI 暴露"职业的职位空缺同样跌得更狠——当时生成式 AI 在理论上都不可能是解释。
    6. **岗位分资历看无差异**:"There is no evidence that job postings for junior roles within occupations most exposed to AI have declined more than postings for senior positions."
  - 来源:【商业/厂商口径 · 经济学分析】Zanna Iscenko & Fabien Curto Millet · Looking for the Ladder: Is AI Impacting Entry-Level Jobs? · Economic Innovation Group, American Worker Project · 2026 年 1 月 · https://eig.org/wp-content/uploads/2026/01/TAWP-Iscenko-Millet.pdf
  - **利益相关(必须写进正文)**:文末署名——"**Zanna Iscenko is AI & Economy Lead, Chief Economist's Team, Google; and Fabien Curto Millet is Chief Economist, Google.**" 致谢名单含 Google 高管 Ruth Porat、Kent Walker、James Manyika。即:**主张"AI 没在杀入门级岗位"的这份文件,由全球最大 AI 厂商之一的首席经济学家撰写。**这与 [C8] 中 Anthropic 自陈"影响有限"构成同一类现象,Round 2 应作为独立议题处理。
  - 逐字摘引(核心主张):"The most plausible explanation is that the data patterns observed are **not early warnings of large-scale technological displacement, but rather the predictable consequences of a classic macroeconomic shock: the sharpest monetary policy tightening cycle in four decades.**"
  - 逐字摘引(机械收缩):"Consider, for instance, a hypothetical professional occupation which starts with an equal number of workers of each age between 22 and 65 and experiences a complete hiring freeze but zero layoffs, across all seniorities, for a year. If we study this occupation a year later we will find that entry-level employment for the 22–25 year-old workers has shrunk by a shocking **25 percent** while it remained level for all other age groups."
  - 逐字摘引(自设边界,防止被反向过度引用):"**absence of evidence is not the same as evidence of absence**; going forward, it is of course possible that advanced AI tools could materially alter the tasks performed by entry-level workers"

- **[C15]** **Yale Budget Lab × Brookings:用 CPS 做全经济体口径,自 ChatGPT 发布以来看不到就业结构断点。**
  - 口径:Martha Gimbel、Molly Kinder、Joshua Kendall、Maddie Lee;数据为 CPS 职业构成;方法为**dissimilarity index**(衡量职业构成变化速度),把生成式 AI 时期与历史上计算机、互联网普及期对比;窗口为 ChatGPT 发布后 33 个月。核心结论:高/中/低 AI 暴露度就业占比"remarkably steady over time";失业者中并未出现 AI 暴露度上升的模式;职业构成的变化在 2021 年(生成式 AI 之前)就已在进行,之后并未加速。另指出**暴露度与实际使用之间存在"striking gaps"**,且约一半聊天机器人用途是 augmentation,而企业 API 用途中 **77%** 是 automation(与 [C7] 的 Anthropic 数字一致)。
  - 来源:【研究·机构报告,未过审】The Budget Lab at Yale · Evaluating the Impact of AI on the Labor Market(系列更新:September CPS Update、November/December CPS Update)· https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-novemberdecember-cps-update(**该 URL 返回 403,【未取得全文】**)
  - 来源:【研究/媒体混合】Brookings · New data show no AI jobs apocalypse—for now · 2025-10-01 · https://www.brookings.edu/articles/new-data-show-no-ai-jobs-apocalypse-for-now/
  - 逐字摘引(**经 WebFetch 提取,需 Round 2 核对**):作者自陈其宽口径方法 "might miss the labor market equivalent of a small fire starting on the stove";并明确表示对更窄职业(writers、translators)"considerable uncertainty about AI's early impact"。
  - 反证/矛盾测量:该团队**明确承认**存在检测不到窄口径影响的可能,并点名引用了 Canaries。即两方并非直接矛盾,而是**分辨率不同**(见交叉口径问题第 1 条)。另注:Fortune 2026-02-02 报道用该报告质疑企业以"AI"为名裁员("AI-washing"),属【媒体】延伸,不可当证据。

- **[C16]** **丹麦全样本准实验:AI 聊天机器人对收入和工时的影响是"精确的零"。**
  - 口径:两轮大规模采用率调查(2023 年 11–12 月、2024 年 11–12 月),每轮约 **25,000 名劳动者、7,000 家职场**,覆盖 **11 个高暴露职业**(accountants、customer support specialists、financial advisors、HR professionals、teachers 等),与丹麦行政数据(收入、工时)链接;方法为 difference-in-differences,个人层与职场层双口径。结果:置信区间**排除大于 1% 的效应**;生产率增益仅 **3% 的时间节省**;采用伴随职业转换与任务重组,但无净工时/收入变化。
  - 发表状态:【研究·工作论文,未过审】NBER Working Paper w33777(2025-04-15 首发),本轮取到的是 2025-07-15 修订版全文。
  - 来源:【研究·工作论文】Anders Humlum(Chicago Booth & NBER)、Emilie Vestergaard(哥本哈根大学)· Large Language Models, Small Labor Market Effects · 2025-07-15 · https://www.andershumlum.com/s/chatbots_july25.pdf ;NBER 版 https://www.nber.org/papers/w33777
  - 逐字摘引(摘要):"Using difference-in-differences, we estimate **precise null effects** at both the individual and workplace levels, with **confidence intervals ruling out effects above 1%**. While adoption is associated with occupational switching and task restructuring, these shifts do not result in net changes to hours or earnings. Modest productivity gains (**3% time savings**) and the emergence of integration and oversight tasks help explain these muted effects. Our findings **challenge narratives of imminent disruption** from Generative AI, highlighting instead the slow burn of productivity J-curves."
  - 关于入门级:Canaries 自己引用道——"the most recent version of Humlum and Vestergaard (2025) found minimal effects on entry-level earnings or hours worked in Denmark";EIG 补充称该文虽也观察到 early-career 就业下降,但 DiD 显示 AI 不是驱动因素。**⚠️【存疑】**:我在 Humlum 全文中未定位到关于 early-career 的专门章节结论段,该转述来自 EIG 与 Canaries 的引用,Round 2 需回原文定位。
  - **中美/中丹构念不等价提醒**:丹麦有强工会、高解雇成本、集中工资谈判,"就业"与"工时"由行政记录直接观测;美国 ADP 数据是薪资单头数,CPS 是自报。丹麦的零效应**不可直接外推**到美国,更不可外推到中国。

- **[C17]** **反方核心证据:也有研究发现 AI 暴露度越高,就业反而增长。**
  - **(a) Johnston & Makridis(2025)——QCEW 州×行业口径,就业增加。**
    - 口径:把 Eloundou et al.(2024)的职业级暴露度按州×行业就业加权平均,构造 state-industry 暴露度,匹配 QCEW(Quarterly Census of Employment and Wages,官方全覆盖行政数据)。**2017–2024 年:AI 暴露度每增加一个标准差,对应生产率 +10%、就业 +3.9%、工资 +4.8%**。另用 Gallup Workforce Panel 的实际使用频率:高频 AI 使用者占比每增 1 个百分点,对应实际产出高 0.1%–0.2%、就业高 0.2%–0.4%;高频使用者占比从 2024 年中约 12% 升到 2025 年末约 26%,对应实际产出高约 1.4%–2.8%。
    - 来源:【研究·工作论文,未过审】Andrew Johnston & Christos Makridis · SSRN,DOI 10.2139/ssrn.5375017 · https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5375017(**SSRN 返回 403,【未取得全文】**;数字经 phys.org 2026-04 报道 https://phys.org/news/2026-04-industries-exposed-ai-productivity-gains.html 与 Canaries 脚注 9 双向确认存在与方向,但**具体系数需 Round 2 取原文核对**)
    - Canaries 作者对它的处置(逐字):"Johnston and Makridis (2025) find **employment increases** in state-industry pairs more exposed to AI using Quarterly Census of Employment and Wages (QCEW) data." 并在脚注 9 反驳:"**Industry-level labor market changes may be distinct from the occupation-level changes studied in this paper** if firms make capital investments or become more productive in ways that increases overall labor demand"。这正是"生产率效应/补充效应"的机制表述。
  - **(b) Hampole, Papanikolaou, Schmidt & Seegmiller——企业层面劳动需求增长抵消了暴露职业的相对下降。**
    - 口径:Revelio Labs 的 LinkedIn 简历与职位数据(约 5,800 万份美国工作档案,搜索结果口径 2014–2023;Canaries 转述为 2011–2023——**两个时间窗需 Round 2 核对**);用 AI 开发者的简历识别企业实际部署的 AI 应用,再用 NLP 判定哪些任务被影响。
    - 来源:【研究·工作论文,未过审】NBER Working Paper 33509 · Artificial Intelligence and the Labor Market · 2025 · https://www.nber.org/papers/w33509 ;作者版 PDF https://www.bryanseegmiller.com/files/AI_Draft_v202508.pdf(**本轮未取得全文**)
    - Canaries 转述(逐字):"Hampole et al. (2025) use job postings and LinkedIn profiles from Revelio labs from 2011 to 2023 to find **limited employment impacts overall, with growing labor demand at firms offsetting relative declines in demand for exposed occupations.**"
  - **(c) Chandar(2025b)——用 CPS 做同一件事,总体几乎无差异趋势。**
    - 注意:这是 Canaries 的**共同作者本人**用公共数据做的版本。Canaries 逐字转述:"Chandar (2025b) uses data from the CPS to compare employment changes in more and less AI-exposed professions, **finding little differential trend overall** but noting difficulty with measuring changes for young workers given limited effective sample size."
    - 来源:同 [C9] 文献综述部分。**【未取得全文】**,Round 2 需找到 Chandar(2025b)原件。
  - **(d) Jiang et al.(2025)**:AI 暴露度与**更长工时**相关(与"AI 减少劳动投入"方向相反)。来源:同 [C9] 文献综述转引,**【未取得全文】**。
  - **(e) Dallas Fed(2026-02-24)"AI is simultaneously aiding and replacing workers, wage data suggest"** —— https://www.dallasfed.org/research/economics/2026/0224(**返回 403,【未取得全文】**),仅记录存在。
  - **(f) PwC 2026 Global AI Jobs Barometer**:称被 AI"专业化"的岗位增速是被"平民化"岗位的两倍、自 2021 年起工资增速快 42%。【商业调查】,PwC 为 AI 咨询业务利益相关方,https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html(**本轮未取得方法论**)。
  - **(g) Canaries 自己的 Fact 3 就是补充效应的证据**:"we find employment growth in occupations in which AI use is most augmentative"。
  - 搜索角度记录:搜索了"AI exposure employment growth"、"complementarity productivity effect"、"QCEW AI exposure"、"employment grew high exposure occupations"、"Autor Thompson expertise"。**确实存在多项方向相反的证据,不存在"找不到反证"的情况。**

- **[C18]** 与 Canaries 同向的独立证据(避免只收反证):Hosseini & Lichtinger(2025)、Klein Teeselink(2025)用美国与英国的 LinkedIn 数据,同样发现 AI 暴露职业的入门级就业下降。
  - 来源:同 [C9] 文献综述,逐字:"work by Hosseini and Lichtinger (2025) and Klein Teeselink (2025) similarly found declines in AI-exposed entry-level employment using LinkedIn data from the US and UK."
  - **【未取得全文】**,Round 2 需分别定位原件并核对发表状态。注意 LinkedIn/Revelio 数据本身对入门级白领严重过采样。

---

### 三者的构念差异(可直接用于成文)

**这三项研究回答的是三个不同的问题,不能互为证据。**

| | Eloundou et al. | Anthropic Economic Index | Brynjolfsson et al. Canaries |
|---|---|---|---|
| 回答的问题 | "**理论上**,LLM 能把哪些任务的耗时砍一半?" | "Claude 用户**实际上**在拿它做哪些 O*NET 任务?" | "生成式 AI 普及后,美国薪资单上的就业**事实上**怎么变了?" |
| 数据性质 | 前瞻性能力评分(人工 + GPT-4 对 O*NET 任务打标) | 单一厂商平台的使用日志分布 | 事后就业实测(ADP 行政薪资微观数据) |
| 分母 | O*NET 全部任务 / 全美职业 | Claude 对话总数(**不是**劳动者总数,**不是**工时总数) | ADP 覆盖企业的在职人数 |
| 时间指向 | 无时间指向(作者明说"We do not make predictions about the development or adoption timeline") | 观测期内的当下 | 2021-01 至 2025-09 的已发生变化 |
| 不能推出什么 | 不能推出替代率、失业率、任何采用时间表 | 不能推出劳动力总体的 AI 使用率(样本是 Claude 用户),不能推出就业影响 | 不能推出"AI 是原因"(作者自陈"may in part be influenced by factors other than generative AI") |
| 利益相关 | OpenAI 员工为主要作者,标注员为 OpenAI 对齐承包商 | Anthropic 自有数据、自有分类器、自行发布 | Stanford,数据由 ADP 提供、Stanford Digital Economy Lab 资助 |

**关键的引用链事实:第三项的自变量,就是第一项和第二项。** Canaries 的 AI 暴露度直接取自 Eloundou 的 GPT-4 β 分数,其 automation/augmentation 划分直接取自 Anthropic Economic Index。因此"三项研究互相印证"是**假独立**——它们共享同一套构念前提。任何对 Eloundou rubric 的质疑(作者本人已列出至少 4 项)会同时传导到 Canaries 的分组和 EIG 的反驳(EIG 也用同一套 β 分数)。

**给读者的一句话**:"某专业 AI 暴露度高"≠"该专业会失业"。exposure 的字面含义是"这份工作里有多少任务,LLM 能帮你省一半时间"。省时间的结果可能是裁员(替代效应),也可能是同样的人产出更多、需求随之扩大(生产率/补充效应)——Canaries 自己的 Fact 3 和 Johnston-Makridis 的 QCEW 结果就分别指向这两个方向。

---

### 交叉口径问题(Round 2 必核)

1. **"AI 没影响" vs "AI 影响青年" 不是同一个问题的两个答案,而是两个分辨率下的两个问题。** Yale Budget Lab 用 CPS 看全经济体职业构成(dissimilarity index),Canaries 用 ADP 看 22–25 岁 × 暴露五分位。前者自陈"might miss the labor market equivalent of a small fire starting on the stove"。**媒体把二者并列成"专家吵架"是构念错误。** 成文时必须写清:一个是宏观构成,一个是特定年龄段的相对变化。

2. **"16%"是相对下降不是绝对下降。** Canaries 的绝对口径是 6%(2022 年末→2025-09,22–25 岁最暴露职业),相对口径 16%(控制企业层冲击后 vs 最低暴露组),事件研究口径 15 log points。三个数字在不同段落,媒体常把 16% 当作"这些年轻人有 16% 丢了工作"。**分母是"最低暴露五分位的同龄人",不是"全部 22–25 岁劳动者"。**

3. **13% vs 16% 的版本漂移。** 初版(2025-08-26)约 13%,Nov25 版 16%。EIG 的批评针对的是 13% 那版。截至 2026 年 7 月,Fortune、Silicon Canals 等仍在引 13%。引用时必须标版本日期。

4. **Eloundou 的 arXiv 版与 Science 版数字不同(3% vs 1.8%,49% vs 46%)。** 且 RePEc 记录至今未标已发表。Round 2 必须确定:成文时引哪一版?建议引 Science 版并注明 arXiv 版差异。另:"80% 的美国劳动力受影响"这句流传语用的是 **β 口径 + 至少 10% 的任务**这两个限定,两个限定在传播中几乎总被砍掉。

5. **Anthropic Economic Index 的 automation 比例跨期不可比。** 分类器从 Sonnet 3.7 换成 Sonnet 4(报告自陈 "complicates direct comparison");数据面从 Claude.ai Free/Pro 扩到 Claude Code + Desktop + 第一方 API(不同面自然有不同的 automation 比例:API 77% vs Claude.ai 47%);2026-06 起还混入了调查数据。**"automation 份额从 43% 升到 50%+ 再回落"这条曲线不能当趋势读。**

6. **"77% 的企业 API 用途是自动化"是关于 Anthropic 企业客户的,不是关于美国企业的。** Yale/Brookings 引用了这个数字,传播链里容易被读成后者。

7. **Canaries 的 augmentation 最低两个五分位,Claude 使用量仅占对话的 0.01% 和 0.09%。** 也就是说"AI 增强型职业 vs 自动化型职业"的对比,在低端是拿几乎没有 Claude 数据的职业在做分组。这是 Fact 3 的一个薄弱点,Round 2 应核实作者如何处理。

8. **ADP 只对 70% 的劳动者有职位名称,其余被剔除。** 被剔除的那 30% 是否系统性偏向某类岗位(如零工、时薪、低技能),论文未详述。这会直接影响"入门级"的定义。

9. **利益相关的双向性,必须在正文中显式处理。** 主张"AI 暴露度高"的 Eloundou 出自 OpenAI;主张"AI 使用广泛/automation 上升"的 Index 出自 Anthropic;而主张"AI 没有在杀入门级岗位"的 EIG 文章由 **Google 首席经济学家**撰写、致谢 Google 高管。**厂商在这场争论的两端都有人。** 不能简单用"厂商=夸大 AI 影响"这条启发式。

10. **中美构念不等价(本线涉及跨国的部分)**:Eloundou 的暴露度基于 **O*NET**(美国劳工部职业任务库),中国没有对等的任务级职业数据库,任何"中国某专业的 AI 暴露度"若基于 O*NET crosswalk,必须写明是**移植构念**;丹麦 Humlum 的"工时"来自行政记录,美国 CPS 的"就业"是自报,ADP 的"就业"是薪资单头数——三者的分母不同。

---

### 未取得 / 存疑

| 项 | 状态 | 说明 |
|---|---|---|
| Science 384(6702):1306–1308 正式版全文 | 【未取得全文】 | science.org 返回 403。1.8%/46% 经 GovAI 论文页 + ADS 书目 + 搜索摘要三处二手确认,但**摘要逐字原文未取得**。Round 2 需通过机构订阅或作者版取得。 |
| Johnston & Makridis(2025)SSRN 5375017 | 【未取得全文】 | SSRN 403。方向(就业增加)经 Canaries 脚注 9【研究】+ phys.org【媒体】双向确认;+10%/+3.9%/+4.8% 三个系数**目前只有媒体来源**,必须回原文核对。 |
| Hampole, Papanikolaou, Schmidt & Seegmiller,NBER w33509 | 【未取得全文】 | 数据时间窗有冲突:搜索结果说 2014–2023、约 5,800 万份 LinkedIn 档案;Canaries 转述为 2011–2023。需核。 |
| Yale Budget Lab 的 CPS 更新原报告 | 【未取得全文】 | budgetlab.yale.edu 两个 URL 均 403。目前依赖 Brookings 2025-10-01 文章。Round 2 需取原报告的 dissimilarity index 方法与数字。 |
| Dallas Fed 2026-02-24 | 【未取得全文】 | dallasfed.org 403。仅记录该来源存在。 |
| Chandar(2025b)CPS 版本 | 【未取得全文】 | 仅在 Canaries 文献综述中被引,未找到独立出处。这是**共同作者用公共数据得到"总体几乎无差异"结论**的关键文件,Round 2 高优先级。 |
| Hosseini & Lichtinger(2025)、Klein Teeselink(2025) | 【未取得全文】 | 仅经 Canaries 转引。发表状态未知。 |
| Jiang et al.(2025)"AI 暴露与更长工时" | 【未取得全文】 | 仅经 Canaries 转引。 |
| Humlum & Vestergaard 关于 early-career 的具体结论 | 【存疑】 | EIG 与 Canaries 都转述该文对入门级为零效应,但我在 2025-07-15 版全文中未定位到该专门结论段。可能在更新版(SSRN 5250742 "Still Waters, Rapid Currents")中。Round 2 需核。 |
| Anthropic 各期报告的逐字限制条款 | 【需回原页核对】 | 本轮 Anthropic 网页均经 WebFetch 摘要器提取,引号内文字**不保证逐字**。所有百分比与 limitations 引文须回 anthropic.com 原页确认。 |
| PwC 2026 AI Jobs Barometer 方法论 | 【未取得】 | 商业调查、利益相关方,方法论未取。若成文要用,必须先拿到口径。 |
| BLS《Incorporating AI impacts in BLS employment projections》 | 【未取得,建议 Round 2 补】 | https://www.bls.gov/opub/mlr/2025/article/incorporating-ai-impacts-in-bls-employment-projections.htm —— **这是本线唯一一个【官方】来源候选**(美国劳工统计局如何把 AI 纳入职业就业预测),对"未来十年选什么专业"这个主题价值极高,本轮未及展开。强烈建议 Round 2 优先取。 |

---

## 线 D:中国侧官方统计(教育部 / 国家统计局 / 人社部)

### 关键论断

---

#### 一、本科专业布点的增设与撤销

- **[D1]** 2024 年度全国高校**新增本科专业点 1839 个、撤销 1428 个、停招 2220 个**,另有 157 个专业点调整学位授予门类或修业年限。撤销+停招(3648)远超新增(1839)。
  - 口径:**单位是"专业点"(布点数),即"某所学校开设某个专业"这一组合**,不是招生人数,不是在校生数,更不是岗位数。一所 3000 人的学校撤销一个每年招 20 人的专业,与一所学校新增一个招 200 人的专业,在这套统计里都记作"1 个专业点"。分母是全国普通本科高校的全部现有专业点(2024 年度约 6 万量级,教育部未在该新闻稿中给出分母)。时间窗:2024 年度申报、2025 年 4 月 22 日公布,对应 2025 年秋季招生。"停招"与"撤销"是两个不同动作:停招指暂停招生但专业点保留,撤销指从该校专业目录中删除;两者不重复计数但性质不同,媒体常把二者相加成"3648 个专业被砍",这是错的。
  - 来源:【官方】中华人民共和国教育部 · 《教育部公布 2024 年度本科专业备案和审批结果并更新发布本科专业目录》 · 2025-04-22 · http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202504/t20250422_1188245.html
  - 同源交叉:【官方】中国政府网 · 《教育部高等教育司负责人就 2024 年度普通高等学校本科专业备案和审批结果及〈普通高等学校本科专业目录(2025 年)〉答记者问》 · 2025-04 · https://www.gov.cn/zhengce/202504/content_7020385.htm
  - 逐字摘引:"全国高校共新增专业点1839个,调整学位授予门类或修业年限专业点157个,停招专业点2220个,撤销专业点1428个";"撤销、停招专业点数大幅超过增设专业点数,专业结构不断优化"
  - 反证/矛盾测量:**教育部本身把"撤销数大于新增数"叙述为正面成绩("结构不断优化"),而非危机信号**。文件通篇未把"就业率低"列为撤销的明示标准,措辞是"服务高质量发展""人才培养供需更适配"。因此"撤销多=这个专业没前途"是媒体与考生的推断,不是官方论断。搜索角度:教育部答记者问全文、政策解读、2023 年〔教高〔2023〕1 号〕改革方案表述——**未发现教育部公开文件将"就业率"直接写为撤销触发条件**。

- **[D2]** "十四五"期间(2021—2025)全国高校累计**新增本科专业布点 1.02 万个、撤销或停招 1.22 万个**,累计调整比例超 30%,2026 年当年调整比例首次突破 10%。
  - 口径:单位仍是**布点数**,5 年累计。"撤销或停招"是**合并口径**(与 [D1] 分开列示的做法不同),两个年度序列不可直接拼接。"累计调整比例超30%"的分母是专业布点总数,教育部未在新闻稿中给出该分母绝对值。"今年调整比例首次突破10%"指 2026 年度当年调整布点数 / 全部布点数。
  - 来源:【官方】教育部 · 《〈普通高等学校本科专业目录(2026 年)〉发布》 · 2026-04-28 · http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202604/t20260428_1435016.html;转载同文:【官方媒体】新华网 · 2026-04-28 · https://education.news.cn/20260428/fbaf09cb35484123a0861639845bcc27/c.html
  - 逐字摘引:"全国高校新增本科专业布点1.02万个、撤销或停招1.22万个";"累计调整比例超30%,今年全国高校专业调整比例首次突破10%"
  - 反证/矛盾测量:**布点数净减少 ≠ 招生规模缩小**。同期高校毕业生规模从 2021 届 909 万增至 2026 届预计 1270 万(见 [D6]),即**布点在减少而人数在增加**——说明调整主要是"集中化"(小而散的布点被砍,存量布点扩容),不是"总盘子收缩"。搜索角度:是否有官方发布"分专业招生人数"时间序列——**未找到教育部公开的分专业年度招生人数序列**,这是本条最关键的缺口。

- **[D3]** 《普通高等学校本科专业目录(2026 年)》新增 38 种本科专业,并**首次增设"交叉学科"门类**,首批列入未来机器人、交叉工程等 11 种已有专业和具身智能、脑机科学与技术等 4 种新专业。目录现涵盖 **13 个门类、92 个专业类、883 种专业**。
  - 口径:"种"是专业名目数(目录条目),与"布点数"是两套完全不同的计量。2025 年版目录为 93 个专业类、845 种专业;2026 年版为 92 个专业类、883 种专业——**专业类减少 1、专业种数增加 38**,说明发生了专业类合并/重组,不能把 845→883 读作"净增 38 种全新专业"而不看结构调整。
  - 来源:【官方】教育部 · 《教育部关于公布〈普通高等学校本科专业目录(2026 年)〉的通知》(教高函〔2026〕2 号,成文日期 2026-04-07,公布 2026-04-28) · http://www.moe.gov.cn/srcsite/A08/moe_1034/s3882/202604/t20260427_1434931.html;附件 PDF:http://www.moe.gov.cn/srcsite/A08/moe_1034/s3882/202604/W020260427440749576927.pdf;中国政府网同文:https://www.gov.cn/zhengce/zhengceku/202604/content_7067247.htm
  - 逐字摘引:"增设'交叉学科'门类,首批列入'交叉学科'门类有未来机器人、交叉工程等11种目录中已有的专业和具身智能、脑机科学与技术等4种新专业";"本科专业目录共涵盖13个门类、92个专业类、883种专业"
  - 2026 年新增专业中被点名者:能源科学与工程、深地科学与工程、交通能源融合工程、农业机器人、生物制造、脑机科学与技术、数字文旅、商业人工智能、数字贸易、数字金融、具身智能等(来源同上转载:【媒体·官方背景】中国教育和科研计算机网 CERNET · 2026-04-28 · https://www.cernet.edu.cn/ke_yan_yu_fa_zhan/gao_xiao_cheng_guo/gao_xiao_zi_xun/202604/t20260428_2731325.shtml)
  - 反证/矛盾测量:**"目录里有"与"能招到人/能就业"完全无关**。目录新增只意味着教育部允许这个名称存在。2026 年新增的 38 种专业中,绝大多数首批只有个位数高校开设,首届毕业生要到 2030 年才出现,**在 2026 年做志愿决策时不存在任何就业证据**。搜索角度:是否有任何官方或研究机构对"新目录专业"的就业追踪——**没有,也不可能有,时间上不成立**。

- **[D4]** 2020—2024 年五年间撤销点数最多的本科专业为:信息管理与信息系统(160 个)、公共事业管理(138 个)、信息与计算科学(123 个)、市场营销(104 个)、产品设计(93 个)。
  - 口径:【**注意来源分级**】这一排名**不是教育部直接发布的榜单**,而是麦可思研究院对教育部逐年公布的《备案和审批结果》附件名单的**二次汇总**。分子=五年累计撤销布点数;分母无(是绝对数排名,未除以该专业总布点数)。**未做标准化处理**:信息管理与信息系统本身布点基数极大(数百所高校开设),撤销 160 个的"撤销率"可能低于某个只有 30 所开设、撤销 20 个的小专业。用绝对数排名会系统性高估大基数专业的"衰败感"。
  - 来源:【商业调查】麦可思研究院(利益相关方:主营高校就业调查与咨询,其"红黄绿牌专业"体系与高校服务采购存在商业关联)· 经媒体转述,原始统计口径文档未公开取得 · 转述见 https://m.sohu.com/a/832850315_121124324/
  - 一手可回溯路径:教育部每年度《普通高等学校本科专业备案和审批结果》通知的**附件名单**(逐校逐专业列出撤销点),是可重算的一手底稿,但为 PDF/Excel 附件,本轮**未取得全文**。
  - 反证/矛盾测量:**撤销名单里的专业不等于"该专业毕业生失业"**。公共事业管理、信息管理与信息系统这类被大量撤销的专业,共同特征是"口径宽泛、无明确对口岗位、在非优势院校开设",撤销集中发生在地方本科院校;头部高校的同名专业普遍未撤。因此这个信号的正确读法是"**在什么学校读什么专业**",而不是"这个专业不能读"。搜索角度:是否有官方或学术研究把撤销点按院校层次(985/211/地方本科)分解——**未找到公开的分层统计**。

- **[D5]** 2024 年度新增布点最多的本科专业为**人工智能**,当年新增 91 所高校备案,累计备案高校达 626 所。
  - 口径:分子=2024 年度新增备案该专业的高校数(91);"626 所"为历年累计备案总数。专业代码 080717T,四年制,授工学学士。**统计方**为全国高校人工智能与大数据创新联盟、华算人工智能研究院的汇总,非教育部直接发布的排名。
  - 来源:底层名单为【官方】教育部 2024 年度备案和审批结果附件;排名汇总为【商业调查/行业联盟】全国高校人工智能与大数据创新联盟、华算人工智能研究院 · 经媒体转述 · https://www.163.com/dy/article/JTTJT7L50532N2UB.html
  - 反证/矛盾测量:**626 所高校开设 ≠ 626 所高校都有师资和产业资源**。人工智能布点数的爆炸式增长与 [D4] 中被撤销的"信息管理与信息系统""信息与计算科学"高度同构——都是在政策风口期由大量地方院校集中开设。**没有任何官方数据能证明这一轮 AI 布点不会重演上一轮的撤销周期**。搜索角度:找教育部或第三方对"新增专业点师资/实验条件达标率"的评估——**未找到公开数据**。这是本线最重要的空白。

---

#### 二、高校毕业生规模

- **[D6]** 2026 届全国普通高校毕业生规模**预计 1270 万人,同比增加 48 万人**。
  - 口径:分子=全国普通高校(含本科、高职专科、研究生)当年毕业生总数,为教育部**预计数**而非实际统计数;时间窗为 2026 届(2026 年夏毕业)。发布场合:教育部部署"2026 届高校毕业生就业扩容提质行动"。
  - 来源:【官方】教育部 · 经新华社发布 · 2025-11-20 · https://www.news.cn/20251120/ead0f25dff2948dfa7f01fa78f207882/c.html;人民网同文 http://edu.people.com.cn/n1/2025/1121/c367001-40608931.html
  - 逐字摘引:"2026届全国普通高校毕业生规模预计1270万人";"同比增加48万人"
  - 历年序列(同一发布机制):2025 届预计 1222 万人,同比增加 43 万人(【官方】教育部,经新华网 2024-11-14 发布 · http://www.news.cn/20241114/f7195b45585f419c8da27472bfcb8b1f/c.html);由此倒推 2024 届为 1179 万人。
  - 反证/矛盾测量:**"1270 万"是全部层次毕业生,不是本科毕业生,更不是"1270 万人抢工作"**。其中含相当比例升学(考研/专升本/出国)、参军、基层项目,不进入当年就业市场;同时该数字不含往届未就业者(实际竞争池更大)。搜索角度:是否有官方公布的"当年进入劳动力市场的毕业生净数"——**未找到,教育部不发布该口径**。

---

#### 三、分行业工资(国家统计局)

- **[D7]** 2025 年全国城镇**非私营**单位就业人员年平均工资 129441 元;信息传输、软件和信息技术服务业 248752 元(名义增长 4.1%)居首,金融业 211164 元(+4.6%),科学研究和技术服务业 182064 元(+3.8%),卫生和社会工作 146266 元(+2.2%),教育 133539 元(+5.8%),制造业 113594 元(+5.2%),住宿和餐饮业 62461 元(+3.7%)。
  - 口径:**税前**。逐字口径:"工资总额是税前工资,包括单位从个人工资中直接为其代扣或代缴的个人所得税、社会保险基金和住房公积金等个人缴纳部分"。统计单位为"城镇地域内就业人数在 5 人及以上的法人单位",2025 年共 306.2 万家,**不包括个体工商户和自由职业者**。"平均"为算术平均(受高薪者拉高),非中位数;**国家统计局不公布分行业工资中位数**。且是**全部在岗人员**平均,不是应届生起薪。
  - 来源:【官方】国家统计局 · 《2025 年城镇单位就业人员年平均工资情况》 · 2026-05-15 · https://www.stats.gov.cn/sj/zxfb/202605/t20260515_1963707.html

- **[D8]** 同年城镇**私营**单位年平均工资仅 71590 元,不足非私营口径的 56%;私营口径下金融业 140451 元反超信息传输业 128166 元;制造业 76055 元(+6.4%),教育 63908 元(+3.3%→实为 5.3%),卫生和社会工作 75631 元(+0.5%),住宿和餐饮业 55123 元。
  - 口径:两套口径**样本框完全不同**。非私营单位含国有、集体、股份有限、外商投资等;私营单位为私营法人企业。**同一行业两套口径差 2~2.7 倍,绝不可混用**。流传的"IT 行业年薪 25 万"几乎全部取自非私营口径 248752 元,而中国 IT 从业者大量就职于私营企业(该口径 128166 元)——**这是本线最严重的传播口径陷阱**。
  - 来源:同 [D7],表 5。
  - 反证/矛盾测量:即便取私营口径,信息传输业 128166 元仍高出私营总平均(71590 元)79%,即**"IT 不赚钱了"的叙述在统计局口径上不成立**;但增速(私营 +4.0%、非私营 +4.1%)已低于制造业(+6.4% / +5.2%)和教育(+5.3% / +5.8%),**溢价在缩窄而非消失**。搜索角度:找"分专业应届起薪"的官方数据——**国家统计局不发布,教育部也不发布;只有麦可思等商业调查提供(见交叉口径问题)**。

---

#### 四、青年失业率(新口径)

- **[D9]** 2026 年 6 月,全国城镇**不包含在校生**的 16—24 岁劳动力失业率 **14.9%**(5 月 15.6%、4 月 16.3%、3 月 16.9%);25—29 岁 7.1%(5 月 7.2%);30—59 岁 4.0%(5 月 4.1%)。三个年龄组连续第三个月下降。
  - 口径:分子=该年龄段内失业人口;分母=该年龄段**劳动力**(就业+失业),**已剔除在校生**;地域范围为**全国城镇**(不含农村)。月度频率,来自劳动力抽样调查。**注意:6—7 月是应届生集中进入市场的月份,该序列历史上存在强季节性,3—6 月的下降不能外推为"就业转好"的趋势判断,须与去年同月比较**。
  - 来源:【官方】国家统计局按月在数据发布库发布 · 6 月数据发布日 2026-07-21;5 月数据发布日 2026-06-22。本轮**未直接取得 stats.gov.cn 对应月度页面全文**,数字经财经媒体逐字转述:新浪财经 https://finance.sina.cn/2026-07-21/detail-iniipxxe9285261.d.html(6 月)、新浪 https://news.sina.cn/gn/2026-06-22/detail-iniehfpw2612991.d.html(5 月);3 月/4 月经澎湃新闻 https://m.thepaper.cn/newsDetail_forward_33017619、https://m.thepaper.cn/newsDetail_forward_33205433;3 月数据另见【媒体】财新 https://economy.caixin.com/2026-04-21/102436199.html
  - **【口径断裂说明——极重要】** 2023 年 6 月旧口径 16—24 岁城镇调查失业率报 21.3% 后暂停发布;2023 年 12 月起改为新口径(排除在校生)重启,首月(2023 年 12 月)报 14.9%。**21.3% 与 14.9% 分母不同,绝不可并列为"下降了 6.4 个百分点"**。官方逐字理由:"如果把在校学生包含在分年龄组内,会把在校寻找兼职和毕业后寻找工作的青年混在一起,不能准确反映进入社会真正需要工作的青年人的就业失业情况";"在校学生的主要任务是学习,而不是兼职工作"。同时新增发布 25—29 岁组,理由:"多数青年24岁时刚毕业不久,尚处于择业期",至"29岁时绝大多数已度过择业期,就业情况趋向稳定"。
  - 口径说明来源:【官方】国家统计局 · 《关于完善分年龄组调查失业率有关情况的说明》 · 2024-01-17 · https://www.stats.gov.cn/sj/zxfb/202401/t20240117_1946641.html
  - 反证/矛盾测量:新口径**排除在校生会系统性降低报出的失业率**——被排除的在校生中,"慢就业""考研二战""在校但已在找工作"的群体正是压力最大的部分。同时中国调查失业率对"就业"的定义沿用 ILO 标准(参考周内工作 1 小时以上即算就业),该定义下大量低质量、临时性就业计入"就业",**失业率对"就业质量恶化"不敏感**。搜索角度:是否有官方发布的青年"不充分就业率/学历错配率"(对应美国 underemployment)——**国家统计局不发布该指标,中国无对应官方口径**。这是中美对比中最硬的不可比之处。

---

#### 五、考研 / 国考(间接指标)

- **[D10]** 2026 年全国硕士研究生招生考试报名人数 **343 万人**,较 2025 年的 388 万减少 45 万(-11.6%),**自 2024 年起连续第三年下降**,并首次跌破 350 万。序列:2023 年 474 万 → 2024 年 438 万 → 2025 年 388 万 → 2026 年 343 万。
  - 口径:分子=网上报名并缴费确认的人数(教育部口径),非实际参考人数,亦非录取人数;分母无。含往届生与应届生,教育部**不公布应届/往届拆分**。时间窗:2025 年 10 月报名,2025-12-20/21 考试。
  - 来源:【官方】教育部 · 经人民日报/人民网发布 · 2025-11-24 · https://edu.people.com.cn/n1/2025/1124/c367001-40610589.html;教育部本身发布见 http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/moe_1485/202511/t20251124_1421370.html;中国研究生招生信息网 https://yz.chsi.com.cn/kyzx/kydt/202512/20251220/2293443380.html
  - **构念效度局限(必须交代)**:考研报名人数是**多重因素的合成信号**,不是就业压力的纯粹计量。同期影响因素至少包括:(a) 研究生扩招后学历贬值预期上升,读研收益率下降;(b) 部分专业改为专硕、学制延长、学费上涨、取消宿舍;(c) 报考门槛与推免比例提高,统考名额被挤压;(d) 应届生总量仍在增加(见 [D6])却报名下降,说明**是分流去向变化(考公、就业、出国)而非人口变化**。**"考研人数下降=就业变好"和"=大家躺平了"都是无根据的推断**。
  - 反证/矛盾测量:【官方媒体】新华社 · 《报考回归理性 发展路径多元——专家分析2026年考研报名人数》 · 2025-11-24 · http://www.news.cn/20251124/e54d3157f15744f5beb5b76644035f5d/c.html —— 官方解读框架为"理性回归、路径多元",与"就业压力大到考不动了"的民间叙事**方向相反**。两种解释在现有数据上**都无法证伪**,应在成文中并列呈现而非择一。

- **[D11]** 2026 年度国家公务员考试计划招录 **3.81 万人**,通过资格审查 **371.8 万人**,过审/录用比约 **98:1**,较 2025 年度的 341.6 万过审人数增加 30 余万,**刷新历史新高**。最热门岗位报名超 7000 人。
  - 口径:分子=通过用人单位资格审查人数(**不是报名人数,也不是实际参考人数**;报名后未过审、过审后弃考者均不计入实际考场人数);分母=招录计划数。**"98:1"是过审比,不是录取率**——实际到考率通常显著低于过审数。招录结构:约 2.6 万个计划面向应届高校毕业生(市地级及以下),2.8 万余个计划补充到县区级及以下,3000 余个定向招录服务基层项目人员和退役大学生士兵。
  - 来源:【官方】国家公务员局 · 数据经中央媒体发布 · 2025-10-26/27 · 中国青年报 https://zqb.cyol.com/pc/content/202510/27/content_417869.html;证券时报 https://stcn.com/article/detail/3415404.html
  - **构念效度局限**:2026 年度国考**放宽了报考年龄上限**(政策变更),这会机械性推高报名基数,**"创新高"中有多少来自年龄放宽、多少来自就业压力,官方未拆分**。同时招录计划本身也在扩张(3.81 万),所以过审人数与竞争比必须一起看。
  - 反证/矛盾测量:**考研下降(-11.6%)与国考上升(+9%)同时发生**,这本身就否定了"青年整体退出竞争"的单一叙事,更像是**升学赛道向稳定就业赛道的迁移**。搜索角度:是否有官方对"考研降/考公升"的联合解释——**未找到官方联合分析**。

---

#### 六、需求侧官方信号:人社部"最缺工"职业排行

- **[D12]** 人社部/中国就业培训技术指导中心的《全国招聘大于求职"最缺工"的 100 个职业排行》,在人社部"中国就业网"的"短缺职业排行"专栏中,**公开可见的最新一期为 2022 年第四季度**(发布日期 2023-01-30)。截至 2026 年 7 月,该专栏未见 2023—2026 年度的季度榜单公开更新。
  - 口径(以 2022 年可取得的一期为例,逐字):"本期排名数据来源于全国102个定点监测城市公共就业服务机构填报的人力资源市场招聘、求职数据,综合考量岗位缺口数量、填报城市数量等因素,经加工汇总整理形成,按'招聘需求人数'与'求职人数'岗位缺口数量和填报城市数量加权取值后从大到小排列"。**关键限定:数据来源是"公共就业服务机构填报"**——即只覆盖走公共就业服务渠道的岗位,系统性偏向蓝领、制造业、生活服务业,**几乎不覆盖通过校招、猎头、互联网招聘平台流转的大学生对口岗位**。因此该榜单**不能用于本科专业选择的指导**。
  - 来源:【官方】人力资源社会保障部 / 中国就业培训技术指导中心 · 中国就业网"短缺职业排行"专栏 · https://chinajob.mohrss.gov.cn/h5/sjpd/dqzypx/ ;2022 年第四季度榜单 https://www.mohrss.gov.cn/SYrlzyhshbzb/dongtaixinwen/buneiyaowen/rsxw/202301/t20230118_493691.html
  - 榜单构成(2022Q4,可取得的最后一期):前十为营销员、汽车生产线操作工、快递员、餐厅服务员、商品营业员、家政服务员、保洁员、保安员、包装工、车工;100 个职业中 41 个属生产制造及有关人员、30 个属社会生产服务和生活服务人员、23 个属专业技术人员。
  - 反证/矛盾测量:**"最缺工"≠"高薪"≠"适合大学毕业生"**。榜单前列长期由营销员、餐厅服务员、保洁员、保安员占据,这些岗位的"缺工"反映的是**流动率高与薪资吸引力不足**,而非人才稀缺的溢价。用"缺工榜"论证"制造业/服务业有机会"是构念误用。搜索角度:mohrss.gov.cn、chinajob.mohrss.gov.cn、chrm.mohrss.gov.cn 三站点检索 2023—2026 各季度——**未找到公开发布,标【追不到一手】**。

---

#### 七、官方对"专业扩招与就业错配"的正反表态

- **[D13]** 官方口径同时存在**继续扩招优质本科**与**收缩饱和专业**两条并行动作:国家发展改革委明确"十五五"时期支持"双一流"高校本科扩招 10 万人以上;东南大学增加 600 人、西安交通大学 360 人、兰州大学 300 人、北京科技大学 90 人,新增计划重点投向人工智能、集成电路、未来机器人等前沿领域,同时"调减社会需求饱和领域"。
  - 口径:2026 年全国高考报名人数 1290 万人;2026 届毕业生预计 1270 万人。扩招 10 万人的分母是全国本科招生总量(约 480 万量级),**占比约 2%,且集中在头部院校**——对绝大多数考生的选择集不构成变化。
  - 来源:【官方媒体/评论】中国发展改革报社 · 《当高考扩招遇上就业变局,人才培养如何实现精准匹配?》 · 2026-06-18 · 载于国家发展和改革委员会网站 https://www.ndrc.gov.cn/wsdwhfz/202606/t20260618_1405988.html
  - 逐字摘引:"优本扩容不是大水漫灌,而是把优质资源投向国家最急需的地方";"伴随着新一轮科技革命加速演进,AI成为影响就业的更深层次变量"
  - **来源性质提示**:该文为中国发展改革报社的报道/评论,**发布在发改委网站但不是发改委的正式政策文件**,不应作为"发改委官方结论"引用。其中"脑机接口 2024 年市场规模 32 亿元、预计 2027 年 55.8 亿元、专业人才缺口巨大"一句**未给出数据来源**,属【追不到一手】,不可引用。
  - 反证/矛盾测量:**扩招与撤销并存本身构成对"专业调整是在响应就业信号"的挑战**——如果调整完全由就业信号驱动,不会在毕业生规模连年创新高的同时继续扩招。官方框架是"服务国家战略",战略需求与个体就业结果**不是同一目标函数**。搜索角度:找教育部/发改委是否公布过"专业调整的就业数据依据"——**未找到任何公开的、可复核的就业数据到撤销决定的映射规则**。

---

### 交叉口径问题(Round 2 必须核对)

1. **【最高优先级】非私营 vs 私营工资口径**。流传的"IT 年薪 25 万"来自 2025 年城镇**非私营**单位口径 248752 元;私营单位同行业仅 128166 元。差 1.94 倍。任何单引其中一个数字的写法都是误导。且两者均为**税前、含个人缴纳的社保公积金和个税**,与美国 median earnings(税前但不含雇主端、且为**中位数**)**不可并列**——中国是**算术平均**,美国常用**中位数**,平均值系统性高于中位数。

2. **【最高优先级】青年失业率 21.3% 与 14.9% 的断裂**。2023 年 6 月旧口径 21.3%(含在校生)与 2023 年 12 月起新口径(排除在校生)**分母不同**。网上大量图表把两段拼成一条连续曲线,是错误的。国家统计局的说明文件明确了改动理由,但**未公布新旧口径的重叠期双算数据**,因此**无法量化"排除在校生"造成的落差**——这是一个官方未填的洞,须在成文中明说。

3. **【最高优先级】"专业点"不是"人"**。1839 新增 / 1428 撤销 / 2220 停招 / 1.02 万 vs 1.22 万——全部是**布点数**。媒体标题"3648 个专业被砍"把撤销与停招相加且省略"点"字,读者会理解成"3648 个专业消失了",而全国目录里总共才 883 种专业。这是本线最普遍的传播失真。

4. **撤销排行榜的来源分级**。"信息管理与信息系统 160 个、公共事业管理 138 个"这组被广泛引用的数字来自**麦可思(商业调查机构,利益相关方)**对教育部附件的二次汇总,**不是教育部发布的榜单**。Round 2 需回到教育部各年度《备案和审批结果》附件重算,或明确标注为麦可思口径。另需注意该排名是**绝对数**,未除以该专业的总布点数。

5. **2025 年度全国汇总数缺失**。教育部 2026 年 4 月只公布了 2026 年版目录和"十四五"5 年合计,**本轮未找到与 2024 年度同格式的"2025 年度全国新增/撤销/停招专业点数"官方新闻稿**。目前只有省级数字(江苏新增 151、撤销 55,人民日报客户端 2026-05-10 https://www.peopleapp.com/rmharticle/30052093149)。Round 2 须确认该全国数是否发布过。

6. **考研与国考不是同一构念**。343 万(考研,报名缴费人数)与 371.8 万(国考,**过审人数**)口径不同,不能并列比较"哪个更卷"。国考 371.8 万是过审数,实际到考率明显更低;98:1 是过审比不是录取率。且 2026 年国考**放宽了年龄上限**,这一政策变更单独就会推高报名量。

7. **"最缺工"榜单口径与受众错配**。该榜单来自 102 个定点监测城市**公共就业服务机构填报**,天然覆盖蓝领与生活服务岗位,不覆盖大学生主流求职渠道。且公开更新已停在 2022Q4。用它论证"某专业有需求"在方法上不成立。

8. **"毕业去向落实率"不是"就业率"**。自 2021 届起教育部改用"毕业去向落实率",其分子**包含升学、灵活就业、自由职业、创业**。麦可思报的 2024 届本科 86.7% 用的就是这个口径。与美国 NY Fed 的 unemployment rate(分母是劳动力,升学者不在分母内)**是完全不同的构念,绝不可并列**。中国**无**对应 underemployment 的官方指标。

9. **目录"种数"845→883 的读法**。2025 版 93 个专业类 845 种,2026 版 92 个专业类 883 种。专业类少了 1 个,说明发生了合并重组,不能把 +38 简单读作"净增 38 种新专业"。

---

### 未取得 / 存疑

- **【未取得全文】** 教育部各年度《普通高等学校本科专业备案和审批结果》的**逐校逐专业附件**(2023/2024/2025 年度)。这是唯一能重算"哪些专业撤销最多、集中在哪类院校"的一手底稿,为 PDF/Excel 附件,本轮未下载。Round 2 必取。
- **【未取得全文】** 《普通高等学校本科专业目录(2026 年)》附件 PDF(http://www.moe.gov.cn/srcsite/A08/moe_1034/s3882/202604/W020260427440749576927.pdf)。38 种新专业的完整名单与专业代码未取全。
- **【未取得原文页】** 国家统计局分年龄组失业率的**月度发布页面本身**(stats.gov.cn 数据发布库)。2026 年 3—6 月数字均经财经媒体逐字转述,**数字一致且互相印证**,但未落到统计局原页 URL。Round 2 需补 https://data.stats.gov.cn 或 stats.gov.cn/sj/zxfb/ 对应月度页。
- **【未找到】** 2025 年度全国本科专业新增/撤销/停招的**全国汇总数**(与 2024 年度 1839/1428/2220 同格式)。
- **【追不到一手】** 人社部"最缺工"100 职业排行 2023 年至今各季度。搜索角度:mohrss.gov.cn 部内要闻、chinajob.mohrss.gov.cn 短缺职业排行专栏、chrm.mohrss.gov.cn 中国人力资源市场网、新华社/人民日报转载——公开可见最新一期仍为 2022Q4。**"停止公开发布"本身可能是一个信号,但不能据此推断原因**。
- **【追不到一手】** 发改委网站所载评论文中"脑机接口 2024 年市场规模 32 亿元、2027 年 55.8 亿元"未标来源,不可引用。
- **【存疑·需 Round 2 判定】** 麦可思《2025 年中国本科生就业报告》(社科文献出版社,2025 年 6 月)中的"2024 届本科毕业去向落实率 86.7%""2025 届本科月收入 6435 元""自动化首次进入绿牌专业"等数字。**麦可思是利益相关的商业调查机构**(主营高校就业咨询与数据服务,客户即高校),其抽样框为参与其调查的合作高校,**非概率抽样、非全国代表性样本**,且技术报告在皮书数据库内需付费。若引用必须标【商业调查】并写明"非全国代表性抽样"。技术报告链接 https://www.pishu.com.cn/skwx_ps/literature/6331/16133320.html 【未取得全文】。
- **【结构性空白】** 中国**没有**官方的"分专业毕业生失业率""分专业起薪""分专业学历错配率"任何一项。这意味着中美对比中,美方(NY Fed / BLS / ACS)有分专业微观数据,中方只有分**行业**工资和分**年龄**失业率。**"中美分专业就业对比"在数据上根本无法对称完成**——这一点必须在成文中作为方法论限制明写,而不是用麦可思数据去填补这个洞后假装对称。

---

## 线 E:中国侧商业调查与就业质量口径

> 全线时点:检索完成于 2026-07-24。凡标【商业调查】者均为利益相关方自产数据,不得与官方统计并列。

---

### 关键论断

#### 一、麦可思(MyCOS)——机构性质与利益结构

- **[E1]** 麦可思不是研究机构而是一家营利公司,其主营收入来自向高校卖数据监测服务;就业蓝皮书的样本高校与其付费客户高度重叠。
  - 口径:麦可思数据(成都)股份有限公司,新三板挂牌(股票代码 833861,2015 年 10 月挂牌);实际控制人王伯庆持股 61.61%。2018 年主营业务收入 110,752,232.01 元,其中"数据监测类收入"96,886,518.62 元(占营业收入 85.36%),"咨询类收入"16,615,311.32 元(14.64%);毛利率 87.39%。客户为"高校、院系/专业、教育厅/局等机构","在中国教育部门批准 2500 所高校中累计合作 706 所,正在执行签约项目的 569 所"。
  - 来源:【商业调查】新三板智库(研究员麦棋昌、方俊杰)·《寻找新三板精选层标的专题报告(二十三)麦可思(833861.OC):中国高教管理数据与咨询产业的领军者》·2019-11-07·https://pdf.dfcfw.com/pdf/H3_AP201911121370658000_1.pdf(数据自述来自"公司年报")
  - 逐字摘引:"公司直接面对高校、院系/专业、教育厅/局等机构客户提供产品和解决方案,通过标准化及定制化的产品和服务获取服务收入。";"因此,公司在该领域处于绝对的垄断地位。"
  - 为何重要:高校既是麦可思的付费客户,又是其毕业生调查样本的来源与被评价对象。此结构性利益关系,麦可思公开材料中未见披露。
  - 反证/矛盾测量:搜索角度——"麦可思 独立性""麦可思 利益冲突""麦可思 高校 付费 样本";未发现麦可思或第三方对该利益结构的正面回应或否认。亦未发现证据表明样本仅限于其客户高校(蓝皮书技术报告称覆盖全国 30 个省区市)。**该"客户=样本源"推论属结构性风险提示,不是已证实的样本偏差,Round 2 需明确区分。**

---

#### 二、麦可思方法学——一手技术报告(唯一取得全文的一版)

- **[E2]** 麦可思的调查是"邮件邀请制封闭问卷",非随机拦截、非行政全量数据;答题时间 10–30 分钟。
  - 口径:《2023 年中国本科生就业报告》技术报告。2022 届本科生毕业半年后跟踪评价,**于 2023 年 3 月初完成**,全国本科生样本 **13.5 万人**,覆盖 428 个本科专业、30 个省区市、592 个职业、327 个行业。评价对象"包括'双一流'院校、地方本科院校的毕业生,**不包括成人高等教育、军事院校和港澳台院校**的毕业生"。
  - 来源:【商业调查】麦可思研究院主编、王伯庆/王梦萍执行主编·《2023 年中国本科生就业报告》(就业蓝皮书),社会科学文献出版社,2023 年 6 月第 1 版,ISBN 978-7-5228-1799-6,附录"技术报告"第 207–208 页·第三方托管全文 PDF:https://xiuzhenorgweb.oss-cn-zhangjiakou.aliyuncs.com/uploads/files/20231127/cc79a43039780361b3bfe6540f797713.pdf
  - 逐字摘引:"分别向毕业半年后的 2022 届大学毕业生、毕业三年后的 2019 届大学毕业生和毕业五年后的 2017 届大学毕业生以电子邮件方式发放答题邀请函、问卷客户端链接,三类评价的问卷不同。答卷人回答问卷,答题时间为 10~30 分钟。";"答题通过电子问卷客户端实现,未被邀请的答题被视为无效。"
  - 反证:同一技术报告未披露**邀请函发放总量、回收率/应答率**——因此"13.5 万样本"这个分子没有对应分母。搜索角度——"麦可思 回收率""麦可思 答题率""麦可思 应答率""就业蓝皮书 技术报告 抽样";在 2023 版全书 20809 行文本中检索"回收率""应答率""答题率"均无结果,仅出现"回收的全国总样本"一处。**未见任何一版公开回收率。**

- **[E3]** 麦可思自称"没有发现自我选择性样本偏差",但未公开该检验的方法、统计量或结果。
  - 口径:技术报告"研究样本"注意事项第 2 条,针对 2022 届评价。
  - 来源:同 [E2],第 208 页。
  - 逐字摘引:"本研究对答题和未答题的样本进行了检验,没有发现存在自我选择性样本偏差问题(Self-selection Bias)。"脚注自定义:"自我选择性样本偏差问题:是指调查中存在某类群体选择答题的概率和其他群体有明显不同。例如,可能存在就业的毕业生更容易选择参与答题,而没有就业的学生可能不愿意参加答题等。"
  - 反证/矛盾测量:这是一句**无检验细节的断言**——未说明用什么变量比较答题/未答题者、用什么检验、p 值多少。且麦可思若能对"未答题样本"做检验,意味着其掌握未答题者的就业结果信息,而这与"就业状态只能靠问卷获取"存在张力。搜索角度——"麦可思 自我选择 检验 方法""self-selection bias 麦可思 论文";未找到任何公开的检验报告或同行评审文献支持该断言。**这是本线最需 Round 2 追问的方法学空洞。**

- **[E4]** 麦可思用"再抽样加权"把样本分布强行对齐国家统计局的实际分布,对齐维度为学历、地区、院校类型、专业。
  - 口径:同上技术报告第 3 条。加权后 2022 届本科样本区域分布与实际分布完全一致(东部 38.5%/38.5%、中部 26.7%/26.7%、西部 25.4%/25.4%、东北 9.4%/9.4%)。
  - 来源:同 [E2],第 209 页附表 1。资料来源自述:"麦可思-中国 2022 届大学毕业生培养质量跟踪评价,中华人民共和国国家统计局。"
  - 逐字摘引:"对于样本中与实际比例的明显差异可能带来的统计误差,本研究采用权数加以修正(即对回收的全国总样本,基于学历、地区、院校类型、专业的实际分布比例进行再抽样)。"
  - 关键限定:加权只能修正**可观测的结构性偏差**(地区/院校类型/专业),**无法修正"就业者比未就业者更愿答题"这类结果相关偏差**。附表显示对齐后比例分毫不差,这是"再抽样"(而非事后分层加权)的典型特征,意味着可能丢弃了部分回收样本。
  - 反证:搜索角度——"麦可思 加权 方法 争议""再抽样 就业蓝皮书";未发现独立方法学评议。

- **[E5]** 麦可思官网/出版方页面**不公开**样本量、抽样框、回收率;方法学细节仅存在于纸质书附录。
  - 口径:检索麦可思官网产品页(www.mycos.com.cn 与 www.mycosinstitute.org 的"2025 年中国本科/高职生就业报告"页面)、皮书数据库书目页(pishu.com.cn ID=16133169)。三处均只有"本书简介",无样本量、无抽样方法、无回收率、无指标定义。
  - 来源:【商业调查】麦可思研究院·"2025 年中国本科/高职生就业报告"产品页·访问 2026-07-24·https://www.mycos.com.cn/index.php/Index/service_info/nav/2/i/4.html ;【商业调查】社会科学文献出版社皮书数据库·2025 年中国本科生就业报告·https://www.pishu.com.cn/skwx_ps/bookdetail?SiteID=14&ID=16133169
  - 逐字摘引(官网全部方法学表述仅此一段):"本报告基于麦可思公司 2024 年度的大学毕业生跟踪数据而撰写,反映的是社会第三方专业机构对大学生就业信息的跟踪评价结果。麦可思公司自 2007 年以来,每年对毕业半年后大学生的就业状态和工作能力进行全国性研究……建立了 2006~2023 届中国大学毕业生就业数据库。"
  - 结论:**方法学公开度=零(网络端)**;年度样本量只能从新闻通稿或纸质书获得。皮书数据库目录显示存在"技术报告"章节但需付费。

---

#### 三、红黄绿牌——评定规则与名单

- **[E6]** "红黄绿牌"的原始定义中,**第一判据是"失业量"**(绝对人数,不是失业率),这一条在近年媒体转述中普遍消失。
  - 口径:麦可思自定义指标,基于"各专业连续多年应届毕业生就业质量变化趋势综合判断";红黄绿牌"反映的是全国总体情况,各省区、各高校情况可能会有差别"。
  - 来源:【商业调查】《2023 年中国本科生就业报告》第 44 页(三·专业预警分析)·同 [E2] PDF
  - 逐字摘引:"红牌专业指的是失业量较大,毕业去向落实率、薪资和就业满意度综合较低的专业。黄牌专业指的是除红牌专业外,失业量较大,毕业去向落实率、薪资和就业满意度综合较低的专业。绿牌专业指的是失业量较小,毕业去向落实率、薪资和就业满意度综合较高的专业,为需求增长型专业。"
  - 另一处自述(第 195 页):"麦可思研究院在国内率先提出'红黄绿牌'专业理念,已连续十余年根据失业量、毕业去向落实率、薪资和就业满意度等就业指标,综合评价筛选出需求增长型和预警专业"。
  - **关键漏洞**:四个判据(失业量、落实率、薪资、满意度)**没有任何权重、阈值、排序规则**。"综合较低""综合较高"未算法化。这是一个**不可复现的榜单**。
  - 重要豁免条款(逐字):"部分近年来新增数量较多的专业(如人工智能、数据科学与大数据技术、机器人工程)由于尚无成规模、成趋势的毕业生就业数据,暂未包括在内。"——即**新专业系统性地不进红牌榜**,榜单对"新专业是否过热"完全无预警能力。
  - 反证:搜索角度——"红黄绿牌 权重""红黄绿牌 算法""麦可思 评定标准 公式";未发现任何一版公开权重或阈值。

- **[E7]** 2026 版(2025 届)本科绿牌 6 个全为工科,计算机类专业**完全消失**;而 2019–2022 年绿牌榜由计算机类专业主导。
  - 口径:麦可思《2026 年中国本科生就业报告》,基于 2025 届毕业半年后跟踪评价。2026 本科绿牌:电气工程及其自动化、微电子科学与工程、自动化、能源与动力工程、车辆工程、新能源科学与工程(自动化首次入榜,微电子连续 5 年在榜)。
  - 对照(一手):2023 版书内表 12-7"近五年本科绿牌专业"逐字给出——2019 年:信息安全、软件工程、网络工程、物联网工程、数字媒体技术、电气工程及其自动化;2020 年:信息安全、软件工程、信息工程、网络工程、计算机科学与技术、数字媒体技术;2021 年:信息安全、软件工程、信息工程、网络工程、数字媒体技术、数字媒体艺术;2022 年:信息安全、网络工程、信息工程、微电子科学与工程、数字媒体技术、能源与动力工程、电气工程及其自动化;2023 年:信息工程、微电子科学与工程、电气工程及其自动化、能源与动力工程、道路桥梁与渡河工程、机械电子工程。书中自述:"近五年被列为绿牌专业次数最多的是网络工程、信息安全、信息工程(均为 4 次)"。
  - 来源:【商业调查·媒体转述】腾讯新闻转载·《2026 大学生就业报告:制造业吸纳力在增强,自动化首次跻身绿牌专业》·2026-06-11·https://news.qq.com/rain/a/20260611A08LAN00 ;搜狐/麦可思研究转载《2026 年绿牌专业榜揭晓》·https://www.sohu.com/a/1035095629_120619008 ;IT之家·2026-07-06·https://www.ithome.com/0/972/906.htm 。近五年对照表来自【商业调查·一手】《2023 年中国本科生就业报告》第 196 页表 12-7。
  - **叙事价值极高**:同一家机构、同一套(未公开的)判据,7 年内把计算机类从"连续四年绿牌"翻转为"完全出榜"。这既可读作"市场真变了",也可读作"该榜单是滞后指标、跟随而非预测"。**Round 2 必须处理这个二义性。**
  - 反证:搜索角度——"绿牌专业 预测能力 检验""红牌专业 是否准确 回溯";未发现任何对红黄绿牌预测效度的回溯检验研究。**该榜单从未被验证过。**

- **[E8]** 2026 版本科红牌 6 个:绘画、音乐表演、美术学、文化产业管理、劳动与社会保障、城乡规划。
  - 口径:同上报告,2025 届。媒体同时给出的分专业数字:音乐表演月收入 5527 元、专业相关度 51%;绘画月收入 5100 元、相关度 59%;美术学月收入 5031 元、相关度 61%;劳动与社会保障工作相关度 41%、就业满意度 73%;文化产业管理相关度 44%、满意度 76%;城乡规划"专业对口度从 2020 届 81% 下降至 2025 届的 50%"。
  - 来源:【商业调查·媒体转述】搜狐(麦可思研究授权号)·《2026 红牌专业榜,揭晓!》·https://www.sohu.com/a/1041564081_121294(文中标注报告名《2026 年中国本科生就业报告》、发布日 2026 年 6 月 25 日 — 与 [E7] 的 6 月 11 日发布日**不一致**,见交叉口径问题)
  - 反证/矛盾测量:该文给出的红牌定义为"在就业落实率、薪资水平与就业满意度等方面综合表现相对较低,同时在市场需求端呈现减少或增长缓慢趋势的专业"——**"失业量较大"这一原始首要判据被替换成了"市场需求端减少或增长缓慢"**,与 [E6] 书内原文不符。属媒体/通稿改写。

- **[E9]** 2025 版(2024 届)榜单:本科绿牌=电气工程及其自动化、微电子科学与工程、机械电子工程、新能源科学与工程、车辆工程、机器人工程;本科红牌=公共事业管理、音乐表演、绘画、法学、美术学。高职绿牌=铁道机车运用与维护、电气自动化技术、应用化工技术、工业机器人技术、新能源汽车技术、智能控制技术。
  - 口径:麦可思《2025 年中国本科生就业报告》《2025 年中国高职生就业报告》,2025-06-11 发布,基于 2024 届毕业半年后跟踪评价。媒体同时称"法学、绘画连续五年被列为红牌专业;音乐表演、应用心理学五年上榜 4 次,公共事业管理今年首次上榜"。
  - 来源:【商业调查·媒体转述】新浪财经·《2025 年版就业蓝皮书发布 绿牌专业揭晓》·2025-06-11·https://finance.sina.com.cn/tjhz/2025-06-11/doc-inezskcq8164637.shtml
  - 注意:**"机器人工程"在 2025 版进了绿牌**,而 2023 版书内明确说机器人工程"尚无成规模、成趋势的毕业生就业数据,暂未包括在内"([E6])。两年内从"数据不足不予评价"变为"绿牌",而判据规则未公开变更说明。**这是榜单稳定性的直接反例。**

- **[E10]** 2026 版高职绿牌:铁道机车运用与维护、石油化工技术、发电厂及电力系统、应用化工技术、工业过程自动化技术、电力系统自动化技术。
  - 口径:同 [E7] 报告,2025 届高职。
  - 来源:【商业调查·媒体转述】搜狐(麦可思研究)·https://www.sohu.com/a/1035095629_120619008
  - 2026 版高职红牌名单:**未取得**(见"未取得/存疑")。

---

#### 四、麦可思核心口径的精确定义(一手,2023 版书内)

- **[E11]** 麦可思"毕业去向落实率"的分母是全体毕业生,分子含升学与出国——与教育部口径同构,但调查时点是"毕业半年后"而非官方的 8 月 31 日。
  - 逐字定义:"毕业去向落实率:本科生的毕业去向落实率＝已就业本科毕业生数/本科毕业生总数。其中已就业人群包括'受雇工作'、国内外读研等五类。"
  - 数值(2022 届本科,毕业半年后):全国 **86.0%**;"双一流"院校 91.1%;地方本科院校 85.0%。
  - 来源:【商业调查·一手】《2023 年中国本科生就业报告》第 12 页·同 [E2] PDF
  - 后续年份(媒体转述):2024 届本科 86.7%("双一流"91.9%,地方本科 85.6%)。

- **[E12]** 麦可思"月收入"是**税前现金总额**口径,含奖金提成福利补贴——不是基本工资,也不扣社保个税。
  - 逐字定义(脚注):"月收入:指工资、奖金、业绩提成、现金福利补贴等所有的月度现金收入。"
  - 数值序列(毕业半年后本科平均):2018 届起逐年上升,2022 届 5990 元(五年涨幅 16.7%,"剔除通货膨胀因素影响后涨幅达 7.5%");"双一流"7336 元、地方本科 5721 元。2023 届 6050 元;2025 届 **6435 元**;2025 届高职 4882 元。
  - 参照系(麦可思自设):2022 届 5990 元"明显高于城镇居民 2022 年月均可支配收入(4107 元)";2025 届 6435 元 vs 城镇居民月均可支配收入 4709 元。
  - 来源:【商业调查·一手】同上书第 45 页;后续年份【媒体转述】麦可思官网转载第一财经《2023 届本科毕业生平均月收入 6050 元》·2024-06-13·https://www.mycos.com/index.php/Index/response_info/nav/3/id/20250810.html;搜狐《2026 年中国大学生就业报告》·https://www.sohu.com/a/1035094103_120619008
  - **口径警告**:"毕业生月收入"是自报数据(self-reported),与国家统计局的城镇居民可支配收入**不是同一构念**(后者为家庭人均、含转移性收入、口径不同),麦可思自己把两者并列比较,本身就是一次口径混用。
  - 分布(重要,压制"平均数"误读):2023 届本科毕业半年后月收入 **6000 元以下占 57.8%**,6000–8000 元 23.9%,8000 元以上 18.3%,**10000 元以上仅 7.0%**;2023 届高职 6000 元以下占 81.7%。来源同上第一财经转述。

- **[E13]** 麦可思"工作与专业相关度"(对口率)的分母是**受雇全职工作者**,不是全体毕业生——升学、灵活就业、待就业者都不在分母里。
  - 逐字定义(脚注):"工作与专业相关度＝受雇全职工作并且与专业相关的毕业生人数/受雇全职工作的毕业生人数。"
  - 数值:2018–2020 届本科均为 71%,2022 届升至 74%;2025 届本科 71%、高职 59%;医学类本科最高(2025 届毕业半年后 89%);2017 届本科毕业五年后 65%,比半年后(71%)**低 6 个百分点**(即对口率随职业生涯下降);2022 届外科医师对口率 100%,内科医师、药剂师、护士、康复治疗师、全科医师均 99%。
  - 来源:【商业调查·一手】同上书第 96 页;2025 届数据【媒体转述】搜狐·https://www.sohu.com/a/1035094103_120619008
  - **"相关"由谁判定未定义**:书内未说明"与专业相关"是毕业生自评还是编码员判定。**Round 2 需追问。**

- **[E14]** 麦可思"灵活就业"= 受雇半职 + 自由职业 + 自主创业,与教育部口径**不一致**(教育部把自主创业单列、把"其他录用形式就业"计入灵活就业)。
  - 逐字数值:"2022 届有 4.6% 的本科毕业生在毕业半年后选择灵活就业,其中包括 1.4% 选择受雇半职工作,2.0% 选择自由职业,1.2% 选择自主创业。"地方本科院校 5.0% 更高。
  - 序列:本科 2021 届 4.2% → 2022 届 4.6% → 2023 届 5.1% → 2024 届 5.8% → 2025 届 **6.9%**;高职 2021 届 7.7% → 2024 届 9.6% → 2025 届 **10.9%**。
  - 来源:【商业调查·一手】同上书第 134 页;序列【媒体转述】搜狐·https://www.sohu.com/a/1035094103_120619008 ;第一财经《近三成就业者灵活就业》·https://www.yicai.com/news/102490802.html
  - 结构细节(一手):受雇半职本科毕业生中 39.6% 服务于教育领域,自由职业中 24.5% 在教育业,自主创业中 15.1% 在教育业(均较 2021 届下降,分别降 5.5、0.3、5.8 个百分点)。

- **[E15]** 其他 2025 届关键数值(媒体转述,待 Round 2 核):本科境内读研 18.2%;高职专升本 19.4%;未就业备考研的本科生 3.4%(2023 届为 5.6%);本科就业满意度 81%(2021 届 74%),高职 84%(2021 届 72%);在直辖市和副省级城市就业比例由 2021 届 42% 降至 2025 届 37%,地级及以下城市由 58% 升至 63%。
  - 来源:【商业调查·媒体转述】搜狐·《2026 年中国大学生就业报告:本科起薪 6435 元,超六成流向地级及以下城市》·https://www.sohu.com/a/1035094103_120619008

- **[E16]** 麦可思年度样本量逐年增长:2022 届本科 13.5 万 → 2024 届本科 17.1 万/高职 18.8 万 → 2025 届本科 **19.5 万**/高职 **17.0 万**(覆盖本科 522 个专业、高职 584 个专业,2026 年 3 月初完成)。
  - 来源:2022 届【一手】同 [E2];2024 届【媒体转述】新浪财经 2025-06-11(同 [E9]);2025 届【媒体转述】搜狐(麦可思研究)·https://www.sohu.com/a/1035095629_120619008
  - 注意:高职样本从 18.8 万降到 17.0 万、本科从 17.1 万升到 19.5 万,原因未说明;分母(邀请量)始终未公开,所以**样本量增长不等于代表性提升**。

---

#### 五、计算机类专业翻转(本线最具传播力、也最需要口径校验的数字)

- **[E17]** 2024 届计算机类毕业去向落实率 82.4%,在 61 个主要专业类中倒数第 11,低于全国本科平均 86.7%;历史学类 87.2%、外国语言文学类 86.9% 均高于它。
  - 口径:麦可思《2025 年中国本科生就业报告》,2024 届本科,**毕业半年后**(2025 年 3 月初完成调查),分母为该专业类全体毕业生,分子含升学出国。"专业类"= 教育部专业目录二级类(61 个)。
  - 来源:【商业调查·媒体转述】虎嗅·《计算机专业就业率跌至 82.4%,低于文科类专业平均水平》·https://www.huxiu.com/article/4803484.html ;凤凰网·https://news.ifeng.com/c/8oGsCNDXAMi
  - 同源其他数字:计算机科学与技术专业月收入排名由长期前五 → 2022 届第 8 → 2023 届第 27;应届起薪 2021 届 6886 元 → 2023 届 6771 元(降 115 元);但**毕业五年后月收入 14090 元仍居主要专业类第一**。供给侧:开设计算机科学与技术的高校 955 所、软件工程 661 所,两专业毕业生规模均在 10 万人以上。
  - **【追不到一手】**:未取得《2025 年中国本科生就业报告》原书或麦可思官方发布页对 82.4% 的直接表述。搜过角度:麦可思官网 news/response 栏目、皮书数据库、mycosinstitute.org、知乎原帖(403)。
  - 反证/矛盾测量:**同一报告体系中"就业率倒数"与"五年后薪资第一"并存**——若只引前者会严重误导。另外"计算机类落实率低"部分由该专业类**升学率与考公比例结构**驱动(落实率含升学,故不是纯失业指标),Round 2 必须拆开。

- **[E18]** 2026 版报告中计算机科学与技术、软件工程**首次跌出本科月收入前十**;榜首为微电子科学与工程 7814 元、第二电子科学与技术 7752 元。
  - 口径:2025 届毕业半年后月收入([E12] 定义)。
  - 来源:【商业调查·媒体转述】IT之家·2026-07-06·https://www.ithome.com/0/972/906.htm ;新浪财经·https://finance.sina.com.cn/tech/digi/2026-07-06/doc-inifvqsa2004975.shtml
  - 对照(一手,2023 届):月收入前十为信息安全 7756、微电子科学与工程 7151、软件工程 7061、数据科学与大数据技术 7014、电子科学与技术 7011、物联网工程 6967、智能科学与技术 6966、光电信息科学与工程 6911、电子信息科学与技术 6872、机械电子工程 6842。来源:麦可思官网转载第一财经·2024-06-13·https://www.mycos.com/index.php/Index/response_info/nav/3/id/20250810.html

- **[E19]**【追不到一手·存疑】"计算机类专业对口率从 2020 届 76% 降至 2024 届 62%(五年降 14 个百分点)"——广泛流传,但溯源失败。
  - 状态:该数字出现在多篇 2026 年媒体稿中并归因麦可思,但我逐篇核查虎嗅原文时,该文**未出现此数字**(WebFetch 明确回报"原文未发现'专业对口率 76%→62%'的数据")。搜过角度:麦可思官网、IT之家、新浪、esmchina(超时)、知乎(403)、"76% 62% 计算机 对口率"精确检索。
  - **Round 2 处理建议:除非追到原书页码,否则不得使用。**

---

#### 六、教育部官方口径(用来校准所有商业调查)

- **[E20]** "就业率"自 2021 届起正式改名"毕业去向落实率",这是一个**四率之和**的复合指标,升学与灵活就业都计入分子。
  - 口径与逐字公式(附件 1《高校毕业生毕业去向统计分类》):"**毕业去向落实率=协议和合同就业率+创业率+灵活就业率+升学率**";各分率分母统一为"毕业生总数"。
    - 协议和合同就业:签就业协议(编码 10)、签劳动合同(11)、应征义务兵(46)、科研助理/管理助理、国家基层项目、地方基层项目
    - 自主创业:编码 75
    - **灵活就业 = 其他录用形式就业(编码 12) + 自由职业(编码 76)**
    - 升学 = 升学 + 出国出境(编码 85)
    - 未就业 = 暂不就业(不就业拟升学 71、其他暂不就业)+ 待就业
  - 统计对象:"普通高等学校、科研院所具有普通高等教育学籍且取得毕业资格的所有本科、专科(高职)学生和研究生,包含定向、委培等。"
  - 来源:【官方】教育部办公厅·《关于进一步做好普通高校毕业生就业统计与核查工作的通知》·教学厅函〔2021〕19 号·2021 年 5 月 10 日·省级转发 PDF 全文:https://jyt.hunan.gov.cn/jyt/sjyt/bys/tzgg_1/202105/16548110/files/d1856b6e22214d6abd4256691c63fd34.pdf(转发页:http://jyt.hunan.gov.cn/sjyt/bys/tzgg_1/202105/t20210514_16548110.html)
  - 逐字摘引:"为更加准确反映高校毕业生升学、就业等毕业去向情况,从 2021 届起,将'就业率'改为'毕业去向落实率'。"

- **[E21]** 官方"其他录用形式就业"与"自由职业"的认定门槛极低:只需**达到当地最低工资标准**,自由职业甚至只需**毕业生本人签字确认**。
  - 逐字定义(附件 2《高校毕业生毕业去向界定及标准》):
    - "**7. 其他录用形式就业(编码 12)**:用人单位不签订就业协议或劳动合同,仅提供聘用证明、工资收入流水等证明材料。审核依据:依据用人单位出具的聘用证明或毕业生本人提供的工资收入证明、收入流水等其他证明材料,**薪酬需达到当地最低工资标准**"
    - "**9. 自由职业(编码 76)**:指以个体劳动为主的一类职业,如作家、自由撰稿人、翻译工作者、中介服务工作者、某些艺术工作者、**互联网营销工作者、全媒体运营工作者、电子竞技工作者**等。审核依据:**依据毕业生本人签字确认的证明材料,由校、院两级就业部门负责同志审定**,薪酬需达到当地最低工资标准"
    - "**8. 自主创业(编码 75)**……(3)电子商务创业,利用互联网平台从事经营活动,如开设网店等。审核依据:依据网店网址、网店信息截图和收入流水"
    - 说明条款:"'科研助理、管理助理''其他录用形式就业''自由职业'中当地最低工资标准参见人社部公布的《全国各地区最低工资标准情况》。"
  - 来源:同 [E20] PDF,附件 2,第 6–8 页。
  - **这是本线最重要的一手证据**:官方"就业"的下限 = 月入达当地最低工资 + 一张本人签字的说明。开网店、做电竞、当博主均计入落实率。

- **[E22]** 官方报送节奏为"年报/月报/周报/日报",**8 月 31 日是"初次就业"截止时点**;各校自行发布的《就业质量年度报告》通常用 12 月 31 日前后的"年终"数据,两者不可比。
  - 逐字:"每年 12 月至次年 8 月为就业进展情况定期报送时间,分为'年报''月报''周报'和'日报'。'年报'时间是 8 月 31 日,为毕业生初次就业情况报送截止时间";"'日报'时间是 4 月至 8 月,**100 所布点监测高校**在每个工作日 17 时前完成就业数据报送。"
  - 数据发布管制(逐字):"各省级就业工作部门在对外公开本省毕业生毕业去向落实率之前,须与教育部高校学生司核实数据,未经核实不得擅自公开。各高校未经省级就业工作部门同意,不得向其他部门、机构等提供本校就业数据。"
  - 来源:同 [E20]。
  - **推论**:这条规定意味着**全国/分省毕业去向落实率不是公开发布的常规统计**——这解释了为什么中国侧缺少可对标 BLS 的官方分专业就业率序列,也解释了麦可思等第三方数据为何具有事实上的信息垄断地位。

- **[E23]** 官方核查体系:高校自查 → 省级 8 月 31 日前核查 → 教育部与企事业单位数据库比对 + 委托第三方抽查 + **委托国家统计局做抽样调查**。
  - 逐字:"每年 9 月初,教育部委托国家统计局开展毕业生就业状况抽样调查,结果将向各地通报。教育部开展就业数据核查,与国家相关部门的企事业单位数据库进行比对,并委托第三方机构进行抽查。……各高校在数据报送前要做好全面自查,严格审核每个毕业生的就业材料,相关纸质或电子材料要在校级就业部门存档备查,存档时间为 3—5 年。"
  - 来源:同 [E20]。
  - **重要空白**:该国家统计局抽样调查结果"向各地通报",**未见公开发布**。搜索角度——"国家统计局 高校毕业生 去向落实 抽样调查 结果 公布""教育部 通报 抽样调查 落实率";未找到任何一年的公开结果。**这是中国侧最关键的一份"存在但不公开"的官方校验数据。**

---

#### 七、就业数据造假的官方核查(本线最硬的"数据不可信"证据)

- **[E24]** 教育部于 2023 年 8 月**公开承认存在虚假签约、虚假证明**,派工作组赴各省专项核查,并公布 33 条举报电话与邮箱。
  - 逐字摘引(原文):"教育部工作组以直奔主题、直插一线的方式,深入高校、院系,通过检查就业数据自查清单、核对自查报告、抽查相关就业佐证材料,结合有关问题举报线索和存疑信息逐一开展调查核实和现场约谈……**对经核实存在虚假签约、虚假证明等违规行为的,责成有关部门依规依纪严肃处理,并追究相关高校和人员责任**";"**重点核查灵活就业等相关数据**,以'零容忍'的态度严肃查处就业违规行为";"8 月起,还将委托国家统计局和第三方调查机构在全国范围内开展 2023 届高校毕业生去向落实情况抽样调查。"
  - "四不准":不准以任何方式强迫毕业生签订就业协议和劳动合同;不准将毕业证书、学位证书发放与毕业生签约挂钩;不准以户档托管为由劝说毕业生签订虚假就业协议;不准将毕业生顶岗实习、见习证明材料作为就业证明材料。
  - "三不得":不得不切实际向高校和学院提去向落实率具体指标;不得层层加码向辅导员摊派就业任务;不得将单一的去向落实率指标与就业工作人员或者辅导员的绩效考核、评优等挂钩。
  - 违规后果(2021 年文件逐字):"纳入负面清单,在招生计划安排、学科专业申报、教学评估、评奖评优、领导班子考核等工作中作为负面因素重点参考,原则上应取消相关增量安排、评奖评优评先等资格。"
  - 来源:【官方】教育部·《教育部派出工作组赴各省开展专项核查 严查高校毕业生就业数据弄虚作假》·2023-08-04·http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/s5987/202308/t20230804_1072396.html(含教育部学生发展中心举报电话 010-67410311、jyjb@chsi.com.cn 及 31 省市自治区+兵团举报方式,截止 8 月 31 日)
  - **注意**:官方公开的是**核查行动**,不是**核查结果**。搜索角度——"教育部 就业数据 造假 处理结果 通报""高校 就业率 造假 处分 通报 名单";**未找到任何一份点名通报或处理结果公告**。即:承认有假、未公布查出多少假。
  - 制度化延续:【官方】教育部·《关于做好 2025 届全国普通高校毕业生就业创业工作的通知》(2024-11-12,http://www.moe.gov.cn/srcsite/A15/s3265/202411/t20241112_1162526.html)仍要求"严格审核毕业生就业材料和去向信息,规范做好毕业去向登记,确保数据真实准确"。

- **[E25]** 学界对就业率注水的判断:问题至少存在十余年,且是考核机制的必然产物。
  - 来源:【媒体·署名学者评论】马亮(中国人民大学国家发展与战略研究院研究员、公共管理学院教授)·界面新闻·《为何教育部严查就业数据造假,但高校还在继续"套路"?》·2020-07-18·https://www.jiemian.com/article/4695504.html
  - 逐字:"就业统计数据造假至少存在了十余年"(可追溯至"1990 年代初高校不再为毕业生分配工作以来")
  - **限定**:此为评论文章,**非实证研究**,未引用具体审计报告或抽样数据。已核查原文确认无实证支撑。
  - 反证/搜索记录:搜索角度——"高校就业率 实证研究 论文""就业质量报告 信息披露 质量 研究""社保数据 核验 就业率 研究""tax data verify graduate employment China";**未找到任何用社保/税务/行政数据交叉验证高校上报就业率的学术研究**。这是中国侧的实证空白,应如实写入文章。

---

#### 八、高校《就业质量年度报告》——分散、口径自定、不可汇总

- **[E26]** 高校就业质量报告的落实率普遍高于麦可思调查值,时点也不同(年终 vs 半年后)。实例:某高职院校 2025 届毕业去向落实率 95.60%,**截止时点 2025 年 12 月 30 日**;全校"自由职业"仅 19 人。
  - 口径:该报告脚注自定义"就业总人数"= "包含签就业协议形式就业、签劳动合同形式就业、其他录用形式就业、自由职业、自主创业"(注意:**该脚注下的"就业"不含升学**,与落实率分子不同)。
  - 来源:【官方(校方自发布)】浙江工业职业技术学院·《2025 届毕业生就业质量年度报告(对外发布版)》·发布于 2026-01-19·http://cjyw.zsit.edu.cn/attachment/ypc/ueditor/file/20260119/8523_2025届就业质量报告（对外发布版）.pdf
  - 逐字:"截至 2025 年 12 月 30 日,学校 2025 届毕业生的毕业去向落实率为 95.60%。";"学校 2025 届毕业生自由职业 19 人"
  - **口径陷阱**:同一份报告里"毕业去向落实率"和"就业总人数"用了两套不同分子(前者含升学、后者不含),脚注只对后者做了界定。这在高校报告中相当典型。

- **[E27]** "双一流"高校 2025 届就业质量报告普遍**不披露灵活就业**,且各校口径不统一、常以"重点单位比例"替代落实率。
  - 抽样观察:西安交通大学(2026-01-09 发布,报"71.5% 进入重点单位",本科升学 67.4%)、同济大学(2026-01-30,本科升学 75.05%,未单列落实率)、西北工业大学(2026-01-21,落实率"超 97%",本科升学 72%)、华中科技大学(2026-01-19,"超 70% 进入央国企")、西安电子科技大学(2026-01-30,97.22%,本科升学 54.10%)、北京邮电大学(94.35%,本科升学 63.76%)、上海科技大学(93.0%,本科升学 85.5%)。
  - 来源:【媒体汇编】中国教育在线·《多所"双一流高校"公布 2025 届毕业生就业数据》·2026-02-05·https://www.eol.cn/news/yaowen/202602/t20260205_2718602.shtml(转述各校自发布报告)
  - **【未取得一手】**:上述各校原始 PDF 未逐一取回,发布日期以中国教育在线转述为准,其中"北京邮电大学 2026 年 10 月 31 日""上海科技大学 2026 年 11 月 30 日"两个日期**晚于今日(2026-07-24),必属转述错误**,Round 2 必须回到各校原报告核对。
  - 可用结论(稳健):这些高落实率(93%–97%)的**主要构成是升学**(升学率 54%–85%),不是就业市场吸纳。用"某某大学落实率 97%"论证专业前景是典型的口径滥用。

---

#### 九、招聘平台报告(智联/BOSS/猎聘)——样本=平台用户,自选择极严重

- **[E28]** 智联招聘《大学生就业力调研报告》:调查时点固定在春招中期(3 月下旬–4 月中旬),分母是"有求职计划的应届毕业生",不是全体毕业生。
  - 口径与数值(2024 版):"智联招聘在 2024 年 3 月下旬至 4 月中旬开展问卷调研";截至 4 月中旬,**在有求职计划的应届毕业生中 47.8% 已获得 offer**(2023 年 50.4%,2022 年 46.7%);分学历:大专 56.6%(上年 54.4%)、本科 45.4%(上年 47.5%)、硕博 44.4%(上年 56.7%);普通院校本科 43.9%、普本硕博 33.2%。
  - 来源:【商业调查】智联招聘·《2024 年大学生就业力调研报告》·2024 年 5 月·转载:https://zhuanlan.zhihu.com/p/698712933(原始 PDF 见 https://www.sdyanbao.com/detail/758986,需登录)
  - **方法学缺陷(已核实)**:未公开有效样本量、未公开抽样方式、未公开院校层次配额。搜索角度——"智联 就业力调研 样本量""有效问卷";**多个转载版本均无样本量。属【方法学不可评估】。**
  - **分母陷阱**:"有求职计划的应届毕业生"排除了升学、考公备考、慢就业者,分母远小于毕业生总数,该 offer 率**不能反推就业率**。
  - **自选择**:样本来自智联平台用户 + 自愿填答,双重自选择。

- **[E29]** 智联近两年主打产品已转向面向高考志愿的《大学生就业前景研判及高考志愿填报攻略》,数据基础是平台招聘/投递记录而非毕业生调查。
  - 2026 版:2026-06-16 发布。TOP50 高薪专业中 43 个为工学;TOP50 高薪院校中 47 所为"双一流",中国科学院大学、清华、北大居毕业生薪酬前三;机器人 83.8%、新材料 60.1%、人工智能 24.4%(招聘增速);人工智能与数据工程师以约三成招聘增速领跑高增长职业。
  - 来源:【商业调查·媒体转述】搜狐·https://www.sohu.com/a/1037434148_121478296 ;新浪·https://k.sina.com.cn/article_7857201856_1d45362c001907ikw6.html ;东方财富·2026-06-16·https://wap.eastmoney.com/a/202606163772766457.html
  - **已核实的方法学缺陷**:核查新浪转载原文后,WebFetch 明确回报"文章未明确说明数据来自智联平台的招聘投递统计或其他具体来源……原文未提供完整的方法论说明、数据统计周期或样本规模等学术规范信息"。
  - **构念警告**:"高薪专业排行"来自**招聘岗位挂出薪资 / 平台简历薪资**,不是毕业生实得收入;"院校薪酬排行"的分母是**在该平台投递/被录用的该校毕业生**,名校用户占比失衡会系统性抬高其排名。与麦可思的"自报实得月收入"是两个不同构念,**绝不可并列**。

- **[E30]** 猎聘校招报告:纯平台侧供需数据(新发职位、投递人数),无毕业生结果数据。
  - 2026 届数值:校招新发职位同比增速 TOP15 中电子商务 1165.94%、银行 251.39%、保险 145.74%、通信设备 76.96%、人工智能 57.98%、汽车零部件 57.94%、新能源 32.12%;2026 新发校招职位学历要求 本科 69.70%、硕士 18.88%、博士 2.77%、大专及以下 6.16%;2026 届毕业生中标注具备 AI 技能的人数同比增长 76.5%;销售/客服类三季度投递人数同比增长 25.05%。
  - 来源:【商业调查·媒体转述】猎聘《2025 三季度人才供需洞察报告》及校招洞察·网易科技·https://www.163.com/tech/article/KCIDKIT600099BK0.html ;凤凰网河北·https://hebei.ifeng.com/c/8txf3PYyYQq
  - **口径警告**:"电子商务岗位增速 1165.94%"这类超高增速几乎必然是**低基数 + 平台自身销售拓展**共同作用,不能读作行业真实用工增长。分母(上年该行业在猎聘的新发职位数)从未公开。

- **[E31]**【追不到一手·高危】"2026 年春招平均 1 个岗位收到 17.2 份简历,应届生平均投递 150–200 份才能拿到 1 个面试,最终 offer 率不足 8%"——广泛流传,溯源失败。
  - 出处:【媒体·自媒体】新浪财经转载《2026 年,1270 万毕业生的天崩开局》·2026-05-23·https://finance.sina.com.cn/stock/stockzmt/2026-05-23/doc-inhyvanc7423622.shtml。该文归因"智联招聘的数据",但未给报告名与页码。
  - 搜索角度:智联官网、"17.2 份简历 智联""offer 率 不足 8% 2026""投递 150-200 份";**未找到智联任何一份报告含此三项指标**。且"offer 率不足 8%"与 [E28] 智联自己历年 45%–50% 的口径**量级完全冲突**(前者疑似"简历→offer 转化率",后者是"求职者中拿到 offer 的人数占比"——两个完全不同的分母被当成同一件事传播)。
  - **Round 2 处理建议:禁用,或作为"口径混淆传播"的反面案例引用。**

---

#### 十、独立学术数据源(用于交叉验证麦可思)

- **[E32]** 北京大学教育经济研究所(岳昌君团队)自 2003 年起每两年一次的"全国高校毕业生就业状况调查",是唯一可与麦可思对照的、公开了抽样设计的学术调查。
  - 口径:2003–2021 年共 10 次调查;**调查时点为每个调查年份的 6–7 月学生离校前**(注意:比麦可思"毕业半年后"早约半年,比教育部"8 月 31 日"早约 2 个月);"参照我国高等教育的地区结构、学校类型结构、学历结构和专业结构进行多阶段分层抽样,选取东、中、西部地区部分省份中一定数量的高校,并在每所高校内根据毕业生学科和学历层级,按比例发放 500~1000 份问卷";样本学校 28–45 所,样本学生总数 15,060–21,753 人;2021 年为 34 所学校、20,269 人。
  - 关键结果:"已落实"比例(= 已确定单位 + 升学)2003 年 59.8% → 2021 年 **76.5%**;"升学"比例 2003 年 15.1% → 2021 年 **33.0%**;"已确定单位"(正规就业)2021 年 **32.1%,创历年新低**。
  - 来源:【研究·过审】岳昌君、冯沁雪、辛晓佳、邱文琪·《中国高校毕业生就业趋势研究报告:来自 2003—2021 年调查数据》·《华东师范大学学报(教育科学版)》2023 年第 41 卷第 9 期,138–154 页·https://xbjk.ecnu.edu.cn/CN/10.16382/j.cnki.1000-5560.2023.09.010
  - **这是本线最有价值的对照**:2021 年学术调查"离校前已落实"76.5%,其中**升学就占 33.0%,真正签单位的只有 32.1%**。而麦可思 2022 届"毕业半年后落实率 86.0%"。两者差 9.5 个百分点主要来自时点差(离校前 vs 半年后),但更重要的是:**岳昌君把"升学"和"单位就业"拆开报,麦可思和教育部把它们合并成一个率。** 拆开后的画面(三个人里只有一个签了正式单位)与合并后的画面(86% 已落实)在读者感受上是两个世界。
  - **未取得**:2023 年、2025 年两轮调查的期刊论文全文。已知《2023 年全国高校本科毕业生就业调查分析》(岳昌君)存在于先晓书院(https://xianxiao.ssap.com.cn/catalog/7440446.html),需付费,标【未取得全文】。
  - 反证:该调查样本仅 28–45 所高校、2 万人,远小于麦可思的十几万;且以部属/重点高校为主的可能性未在摘要中排除。**两者互为反证,不是一方压倒另一方。**

- **[E33]** 灵活就业比例的官方数字与麦可思数字相差 **3–4 倍**。
  - 官方:"根据全国高等学校学生信息咨询与就业指导中心数据统计,**2020 届全国高校毕业生的灵活就业占比 16.9%,2021 届高校毕业生灵活就业占比 16.25%**"
  - 麦可思:2022 届本科 4.6%、2023 届 5.1%、2024 届 5.8%、2025 届 6.9%([E14])
  - 来源:官方数字见【媒体转载官方数据】《中国青年报》·《灵活就业成大学生就业新形态》·2022-01-17·教育部门户网站转载 http://www.moe.gov.cn/jyb_xwfb/s5147/202201/t20220117_594898.html ;麦可思数字见 [E14]
  - **差异归因(推定,需 Round 2 确认)**:(a)官方口径含"其他录用形式就业(编码 12)"——即有工资流水但无劳动合同者,麦可思很可能把这部分算作"受雇全职工作";(b)官方数含专科(高职灵活就业率约为本科两倍),麦可思 4.6% 仅为本科;(c)官方数为高校上报的行政数据,存在把难以核实去向者归入灵活就业的激励(教育部 2023 年核查明确"**重点核查灵活就业等相关数据**",[E24])。
  - **这是全线最尖锐的一处口径撕裂,必须在文章中显式处理。**

---

### 交叉口径问题(Round 2 必查)

1. **"红牌/绿牌"定义在传播中被偷换。** 一手书面定义首要判据是"**失业量较大/较小**"(绝对人数);2026 年媒体通稿改写为"市场需求端减少或增长缓慢",删掉了失业量。同时"绿牌"定义在 2023 年书内是"失业量较小,毕业去向落实率、薪资和就业满意度综合较高……为需求增长型专业",2026 年通稿写成"就业质量持续较高,且产业需求增长"。**同一榜单两套定义并行流通。**

2. **红黄绿牌无权重、无阈值、不可复现,且系统性排除新专业。** 书内自述新增较多的专业(人工智能、数据科学与大数据技术、机器人工程)"暂未包括在内",但两年后机器人工程直接进了 2025 版绿牌,规则变更无说明。**任何"榜单预示未来"的写法都必须加这条限定。**

3. **"就业率"这个词在中文语境里至少有五个不同东西:**
   - 教育部"毕业去向落实率"(8 月 31 日初次,含升学+灵活就业+创业,不公开发布)
   - 高校自发布"毕业去向落实率"(通常 12 月 31 日年终口径,系统性更高)
   - 麦可思"毕业去向落实率"(毕业半年后,问卷自报,含升学)
   - 岳昌君"落实率"(离校前 6–7 月,已确定单位 + 升学,且**拆开报**)
   - 智联"offer 获得率"(分母 = 有求职计划者,4 月中旬时点)
   **五者数值可在 32%–97% 之间,不可并列、不可比较、不可跨年拼接。**

4. **[E31] 的"offer 率不足 8%"与 [E28] 的"47.8%"来自同一被引机构,量级差 6 倍。** 几乎可以确定是"简历→offer 转化率"与"求职者→offer 人数占比"两个分母被混为一谈。这是本次调研中最典型的口径事故样本,建议在文章中作为教学案例。

5. **麦可思"月收入 6435 元"与国家统计局"城镇居民月均可支配收入 4709 元"的对比是麦可思自己做的,但两者构念不同**(前者个人税前现金总收入自报,后者住户人均可支配收入含转移性收入)。媒体广泛复制这一对比。**不要转述这一比较。**

6. **平均月收入掩盖分布。** 2023 届本科毕业半年后 **57.8% 月收入在 6000 元以下,月入过万仅 7.0%**。任何只报平均值(6050/6435)的写法都会误导。

7. **[E17] 的"计算机落实率 82.4% 倒数第 11"与同一体系"计算机毕业五年后月收入 14090 元居第一"必须同时呈现。** 单引前者即是选择性引用。且落实率含升学,不能等同于失业率。

8. **[E19]"计算机对口率 76%→62%"追不到一手,已核查虎嗅原文并确认该文无此数字。** 未溯源前禁用。

9. **发布日期冲突**:2026 版就业蓝皮书,腾讯/搜狐/新浪多数稿件写 2026-06-11,搜狐"麦可思研究"授权号的红牌稿写 2026-06-25。可能是本科/高职分册或分主题发布,需核。

10. **[E27] 中国教育在线给出的北邮"2026 年 10 月 31 日"、上科大"2026 年 11 月 30 日"发布日期晚于今日,必为转述错误。** 各校数据须回原报告。

11. **[E33] 灵活就业 16.9% vs 4.6% 的 3–4 倍撕裂**,归因尚属推定,需 Round 2 用教育部编码 12/76 与麦可思"受雇半职/自由职业/自主创业"逐项对齐。

---

### 未取得/存疑

**【未取得全文】**
- 麦可思《2025 年中国本科生就业报告》《2026 年中国本科生就业报告》《2025/2026 年中国高职生就业报告》原书 — 社会科学文献出版社出版,ISBN(2025 版本科)978-7-5228-5473-1、(2025 版高职)978-7-5228-5475-5;皮书数据库/先晓书院需付费。**本线 2024 届与 2025 届的全部数字均为媒体转述,只有 2023 版(2022 届)是一手。**
- 麦可思 2025/2026 版技术报告(样本量之外的抽样细节、有无变更)。
- 智联招聘《2024/2025/2026 年大学生就业力调研报告》原始 PDF(水滴研报 sdyanbao.com 需登录;智联官网未见公开下载入口)。
- 猎聘《2025 届/2026 届大学生就业供需洞察报告》原始 PDF(发现报告 fxbaogao.com detail/4947940 需登录)。
- 岳昌君《2023 年全国高校本科毕业生就业调查分析》(先晓书院,付费)。
- [E27] 中各"双一流"高校 2025 届就业质量年度报告原始 PDF。

**【追不到一手】**
- **"计算机类专业对口率从 2020 届 76% 降至 2024 届 62%"** — 搜过:麦可思官网 news/response 栏、IT之家、新浪科技、虎嗅原文(已确认无此数)、esmchina(超时)、知乎(403)、精确串检索"76% 62% 计算机 对口率"。
- **"2026 春招 1 个岗位 17.2 份简历 / 投递 150–200 份换 1 个面试 / offer 率不足 8%"** — 归因智联但无报告名;搜过智联官网、多平台转载、精确串检索。见 [E31]。
- **2026 版高职"红牌专业"名单** — 搜过搜狐/腾讯/网易/新浪多篇 2026 报告稿,均只给高职绿牌,未给高职红牌。
- **教育部委托国家统计局的"高校毕业生去向落实情况抽样调查"历年结果** — 文件明确其存在且"向各地通报"([E23][E24]),但搜遍 moe.gov.cn 与统计局公开渠道**未见任何一年公开发布**。**这是中国侧最重要的一份"存在但不公开"的官方校验数据,建议在文章中直接点名指出。**
- **教育部就业数据造假核查的处理结果/点名通报** — 只公开了核查行动与举报渠道([E24]),未公开查实数量、涉事高校名单或处理决定。搜过"通报""处分""名单""查处结果"。

**【搜索了但没有的东西(如实记录)】**
- **无任何对麦可思数据做效度检验或与行政数据交叉验证的学术研究。** 搜过:"麦可思 效度""麦可思 数据 质疑 论文""就业蓝皮书 代表性""麦可思 交叉验证"、以及英文向 "MyCOS survey validity China graduate employment"。仅找到麦可思自行陈列的名人背书(潘懋元、王辉耀、刘献君等)与其产学研合作机构清单(厦大、西安交大、中央财大、北师大、清华、北大、人大、西南财大)。
- **无任何对"红黄绿牌"预测效度的回溯检验。**
- **无任何用社保/税务/工商行政数据核验高校上报就业率的公开研究或审计结果。**
- 麦可思的"就业满意度"指标在 2023 版全书中**未给出定义脚注**(与月收入、相关度、落实率不同,后三者均有明确公式)。已 grep 全文确认。**Round 2 需追问该指标如何测量(几点量表?阈值?)。**

**【存疑但可用的推论】**
- 麦可思"高校客户 706 所 / 在执行 569 所"([E1])与"样本覆盖 30 个省区市、522 个本科专业"([E16])之间的关系未公开:样本高校是否即客户高校?若是,则存在"被评价者付费、被评价者供样"的闭环。**此为结构性风险提示,非已证实事实,写作时必须如此标注。**

---

## 线 F:专业效应 vs 院校效应——"专业不重要学校才重要"到底对不对

### 关键论断

- **[F1]** Dale & Krueger 原始论文的结论**不是**"上什么学校不重要",而是"在**同一录取集合内**、比较**被同一批学校录取/拒绝**的学生时,学校平均 SAT 的溢价消失;但**学费(人均办学支出的代理)**的溢价**没有**消失。
  - 口径:分子/分母=对数年收入回归系数;数据=College and Beyond(C&B)数据库 1976 年入学队列 + NLS-72;样本限于 30 所 C&B 院校在校生、1995 年**全职**在业者;结果变量=1995 年自报税前年收入(区间型,10 档,顶端截尾按 36-38 岁、年入>20 万美元的对数均值填补);自变量=就读院校平均 SAT、平均净学费、Barron's 分类;"self-revelation model"=控制学生**申请过的**学校平均 SAT + 录取数;"matched applicant model"=对"被同一组学校录取且拒绝"的学生组内固定效应。
  - 来源:【研究·NBER 工作论文,未过审版】Stacy Berg Dale & Alan B. Krueger · *Estimating the Payoff to Attending a More Selective College: An Application of Selection on Observables and Unobservables* · NBER WP 7322 · 1999-08 · https://www.nber.org/system/files/working_papers/w7322/w7322.pdf ;【研究·已过审】同题发表于 QJE 117(4): 1491-1527, 2002-11 · https://academic.oup.com/qje/article-abstract/117/4/1491/1876022
  - 逐字摘引(摘要):"We find that students who attended more selective colleges do not earn more than other students who were accepted and rejected by comparable schools but attended less selective colleges. **However, the average tuition charged by the school is significantly related to the students' subsequent earnings.** Indeed, we find a substantial internal rate of return from attending a more costly college. **Lastly, the payoff to attending an elite college appears to be greater for students from more disadvantaged family backgrounds.**"
  - 反证/矛盾测量:见 [F3]、[F9]、[F10]。

- **[F2]** **常被漏掉的限定语(必须逐字引):DK 的"零效应"只对整体样本成立;对少数族裔与低教育家庭子女,选择性溢价在校正后依然很大。** 这是 2011/2014 更新版的摘要原话。
  - 口径:数据=C&B 调查 + SSA(社保局)**行政**收入记录;两个队列——1976 年入学(收入观测 1983-2007)与 1989 年入学(收入观测至 2007,约 37-38 岁);核心自变量=就读院校平均 SAT(每 100 分)、Barron's 分类;"selection-adjusted"=self-revelation model(控制**申请过**的学校平均 SAT)。
  - 来源:【研究·NBER 工作论文】Stacy Dale & Alan B. Krueger · *Estimating the Return to College Selectivity over the Career Using Administrative Earnings Data* · NBER WP 17159 · 2011-06 · https://www.nber.org/system/files/working_papers/w17159/w17159.pdf ;【研究·已过审】发表版题名**不同**:*Estimating the Effects of College Characteristics over the Career Using Administrative Earnings Data*, Journal of Human Resources 49(2): 323-358, 2014 · https://jhr.uwpress.org/content/49/2/323.short
  - 逐字摘引(NBER 摘要):"…when we adjust for unobserved student ability by controlling for the average SAT score of the colleges that students applied to, our estimates of the return to college selectivity fall substantially and are generally indistinguishable from zero. **There were notable exceptions for certain subgroups. For black and Hispanic students and for students who come from less-educated families (in terms of their parents' education), the estimates of the return to college selectivity remain large, even in models that adjust for unobserved student characteristics.**"
  - 具体量级(逐字):1989 队列、剔除 HBCU 后,少数族裔"implying returns of **12 percent** for attending a school with 100 point higher SAT score and **14 percent** for attending a school in a higher Barron's category, even in the self-revelation model";按父母受教育年限交互——"attending a college with a **200-point higher SAT score** would lead to **5.2 percent** higher earnings in 2007 for those with average parental education of **12 years**…however, for those whose parents averaged **16 years** of education…**there was virtually no return** to attending a more selective college"。
  - 基准对照(未校正模型):"for the 1976 and 1989 cohorts, attending a college with a 100-point higher SAT score lead to students receive **about 6 percent higher earnings** (in 1995 and 2007 respectively) according to results from the **basic model**; for both cohorts, this return was **close to zero** in our selection-adjusted model."
  - 作者自陈局限(逐字):"the analysis does not pertain to a **nationally representative sample of schools**"(样本来自 C&B 的 30 所院校,普遍为选择性较高的四年制大学,**外推到"上不上重点"这一更大跨度的问题是超出数据范围的**)。
  - 反证:见 [F3]、[F9]。

- **[F3]** **对 DK 识别策略最有名的一手批评来自 Hoxby(2009):她认为该策略把全部识别力压在"做了怪异选择的 10% 学生"身上。** 但注意:Hoxby 在 2015 年论文中的表述**更温和且不同**——她说 DK 的方法在原理上只能处理"水平选择(horizontal selection)",不能处理"垂直选择(vertical selection)",且明确声明**不是**在批评该研究。两处措辞差异很大,不能混用。
  - 口径:两处均为方法论文字论证,非新的实证估计。
  - 来源 A:【研究·NBER 工作论文;发表于 JEP 23(4):95-118】Caroline M. Hoxby · *The Changing Selectivity of American Colleges* · NBER WP 15446 · 2009 · https://www.nber.org/papers/w15446
  - 逐字摘引 A:"Finally, Dale and Krueger (2002) compute lower rates of return but their estimates are based on an identification strategy that is **much less credible**. …since **at least 90 percent** of students who have the same menu similarly choose the more selective college(s) within it, the strategy generates estimates that rely entirely on the small share of students who make what is **a very odd choice**. …Yet, they choose differently than 9 out of 10 students. **Almost certainly, these odd students are characterized by omitted variables** that affect both their college decision and their later life outcomes."
  - 来源 B:【研究·工作论文/政府发布】Caroline M. Hoxby · *Computing the Value-Added of American Postsecondary Institutions* · IRS Statistics of Income · 2015 · https://www.irs.gov/pub/irs-soi/15rpcompvalueaddpostsecondary.pdf
  - 逐字摘引 B:"Dale and Krueger (2002) attempt to use the method to address vertical selection. Since the identifying assumptions are inconsistent in such an application, we have not described their study in detail. **The aforegoing discussion is not intended to criticize their study** but simply to clarify that the method they propose is only useful for addressing horizontal selection."
  - 反证/矛盾测量:Mountjoy & Hickman(见 [F4])用 60 万+ 德州行政数据、同样的"录取集合"设计,得到与 DK 一致的结论,说明"只剩 10% 怪人"的样本量担忧在大规模行政数据里被缓解。
  - 【追不到一手】未检索到 Hoxby 用同一数据对 DK 结论做**定量**复现或推翻。

- **[F4]** **迄今规模最大的"同一录取集合"院校增值研究(德州全州行政数据)结论:院校间的因果增值差异存在但不大,且"选择性"几乎不预测增值;选择性带来的收入溢价在入职后几年内衰减到零。**
  - 口径:数据=德州 K-12 学籍 + 公立高校学籍 + 州失业保险工资记录连接;识别=比较"申请并被同一组公立大学录取"的学生;结果=入学后 8-10 年年收入(约 27-29 岁)、BA 完成率;VA=相对增值(以学生选择集内均值为基准);加权=按在校生规模。
  - 来源:【研究·NBER 工作论文,未过审(2021 年 9 月版;截至检索时最新修订 2024-06)】Jack Mountjoy & Brent R. Hickman · *The Returns to College(s): Relative Value-Added and Match Effects in Higher Education* · NBER WP 29276 · 2021-09 · https://www.nber.org/system/files/working_papers/w29276/w29276.pdf
  - 逐字摘引:"we estimate a **relatively tight, though non-degenerate**, distribution of relative value-added across the wide diversity of Texas public universities. **Selectivity poorly predicts value-added** within student choice sets, with only a **fleeting selectivity earnings premium fading to zero after a few years in the labor market**. **Non-peer college inputs like instructional spending more strongly predict value-added**, especially conditional on selectivity. **Colleges that boost BA completion, especially in STEM majors, also tend to boost earnings.**"
  - 量级(逐字):"a gain of roughly **12.3 percentage points of BA completion and $4,440 of annual income between the 10th to the 90th percentiles** of the college distribution";"The **signal SD of relative value-added** for each outcome is around **one-fifth of the SD in raw outcome means**";"for earnings, a **$10,000 increase in the raw earnings mean predicts an increase in value-added of just $330**"。
  - 关键含义:**院校的"生均收入排行榜"几乎不含因果信息**(原始均值差异 5/6 是学生构成差异)。这与"instructional spending 比 selectivity 更预测增值"合起来,是对"名校光环"叙事的直接反驳,但同时也说明**"随便上哪所都行"也不对**(10-90 分位仍差 $4,440/年)。
  - 反证:见 [F9](Chetty-Deming-Friedman 2023 用同样设计但看**上尾**结果,得出相反结论)。

- **[F5]** **专业效应的最强因果证据(挪威录取分数断点):不同专业的回报差异巨大,且在控制了院校与同学质量之后依然巨大;对许多专业而言,"选什么专业"的回报可与"上不上大学"的回报相当。**
  - 口径:数据=挪威 1998-2004 年全部高等教育集中申请记录 + 教育登记(1998-2012)+ **税务登记**年收入(1998-2012);识别=集中录取的分数线断点(2SLS),**且**利用申请人的策略无关排序(strategy-proof ranking)固定"次优选择(next-best alternative)";结果=申请后**第 8 年**的年收入;样本=断点附近的 compliers(边际申请人),**非全体**;效应为 LATE。
  - 来源:【研究·NBER 工作论文,未过审版】Lars Kirkebøen, Edwin Leuven & Magne Mogstad · *Field of Study, Earnings, and Self-Selection* · NBER WP 20816 · 2014-12 · https://www.nber.org/system/files/working_papers/w20816/w20816.pdf ;【研究·已过审】QJE 131(3): 1057-1111, 2016-08 · https://academic.oup.com/qje/article-abstract/131/3/1057/2461218
  - 逐字摘引(摘要):"We find that **different fields have widely different payoffs, even after accounting for institutional differences and quality of peer groups. For many fields the payoffs rival the college wage premiums, suggesting the choice of field is potentially as important as the decision to enroll in college.** The estimated payoffs are consistent with individuals **choosing fields in which they have comparative advantage**."
  - 效应量(逐字):"by choosing **Science instead of Humanities**, individuals **almost triple** their earnings early in their working career. By comparison, choosing **Science instead of Engineering or Business has little payoff**."(注意:后半句同样常被漏掉——**高薪专业之间差异很小**)
  - 对照基准(作者自算的"上大学溢价",逐字):"individuals who did not complete any post-secondary education were, on average, earning **USD 43,200 at age 30**, whereas the average earnings of individuals with a post-secondary degree was **USD 54,700** at the same age."(即约 +26.6%;"payoffs rival the college wage premium" 是相对这个基准说的)
  - 院校/同学质量的排除检验(逐字):控制"预测就读院校"后,"The correlation between the estimated payoffs **with and without controls for predicted institution is 0.84**";控制"预测同学平均申请分"后,"We find a correlation of **0.98** between the estimated payoffs with and without controls for predicted peer quality."
  - 反证/局限:LATE 只对分数线附近的边际申请人成立;挪威高等教育体系(集中录取、免学费、工资压缩)与中美均不同,**外推需谨慎**;作者本人强调 "individuals tend to choose fields in which they have comparative advantage",即**观测到的专业差异不能直接当成"任何人转专业就能拿到"的收益**。

- **[F6]** **美国 ACS 数据下,专业间收入差距的量级确实"够得上"上大学溢价本身:电气工程 vs 一般教育学男性对数时薪差 0.561,而大学-高中差 0.577。**
  - 口径:2009 年 ACS;男性;控制基本人口学、潜在劳动力市场经验、是否有研究生学历;结果=对数时薪;括号内为标准误。**这是描述性/条件均值差,不是因果估计**。
  - 来源:【研究·NBER 工作论文;发表于 Annual Review of Economics 4:185-223, 2012】Joseph G. Altonji, Erica Blom & Costas Meghir · *Heterogeneity in Human Capital Investments: High School Curriculum, College Major, and Careers* · NBER WP 17985 · 2012-04 · https://www.nber.org/system/files/working_papers/w17985/w17985.pdf
  - 逐字摘引:"the difference in returns across college majors **rivals the college wage premium**. For example, using the data from the 2009 American Community Survey (ACS), we find that after adjusting for basic demographics, potential labor market experience, and graduate education, the **gap in log wages rates between male electrical engineering and male general education majors is 0.561 (0.016)**. This is nearly as large as the **0.577 (0.003)** difference between college graduates and high school graduates. Furthermore, the **standard deviation of the return to various majors is 0.177 for men**—about double the typical estimate of the value of the year of school."
  - 作者自设的反证(逐字):"**the extent to which these differences reflect unobserved differences in high school preparation and worker ability or represent compensating differentials for nonpecuniary aspects of jobs is not well-established.**"

- **[F7]** **专业内部的收入方差不小于专业之间的方差:全体本科学历者 25 分位终身收入 72 万美元 vs 75 分位 182 万美元(+154%),与"最低薪专业中位数 vs 最高薪专业中位数"的相对差距几乎相同。**
  - 口径:数据=Census Bureau ACS;样本=**只有学士学位、未再读研究生**的劳动者;**包含兼职者与全年有失业经历者**(不限于全职);结果=按年龄剖面累加的"生涯累计收入"(合成队列,非真实队列追踪);覆盖 80 个专业。
  - 来源:【研究/倡导机构·Brookings 旗下 The Hamilton Project】Brad Hershbein & Melissa S. Kearney · *Major Decisions: What Graduates Earn Over Their Lifetimes* · 2014 · https://www.hamiltonproject.org/assets/legacy/files/downloads_and_links/Major_Decisions_Lifetime__Earnings_by_Major.pdf
  - 逐字摘引:"In fact, **the variation of lifetime earnings within any given major is at least as large as the variation across majors.** For all majors combined, lifetime earnings at the 25th percentile…are **$720,000**, but they are **$1.82 million** at the 75th percentile… This is an increase of **154 percent**—almost precisely the relative spread at the median from the lowest-earning to the highest-earning major."
  - 另一条(逐字):"Cumulative earnings **double—or even triple**—when moving from the bottom quarter to the top quarter of earners in a given major. **These increases are larger for lower-earning majors.**"(即:低薪专业的内部离散度更大——"艺术史高分位者比低分位者好得多得多")
  - **反证(同一份报告内,方向相反,必须一起引)**:"earnings differences across majors **grow larger—or fan out—higher up** in the earnings distributions. For instance, at the **10th percentile** the difference in lifetime earnings between the highest-earning major and the lowest-earning one is about **$500,000**; at the **90th percentile**, this difference is **over $3.5 million**."(即:分布重叠主要发生在中低分位;在上尾,专业差距反而被放大。)
  - 作者自陈局限(逐字):"earnings differences across majors are driven by many factors and **do not necessarily reflect a wage premium for that particular major**. The estimates **cannot distinguish why** graduates in certain majors earn more than those in others."

- **[F8]** **专业效应的"分布形状"有因果证据支持上一条的反证:高薪专业的处理效应主要集中在分布上端,而不是均匀平移。**
  - 口径:数据=德州公立 K-12 学籍→高校→州工资记录;识别=选择性可观测(比较**同一所高中同一届、同一所大学**、入学前测验分数与人口学相同、但专业不同的学生);结果=季度收入(2016 年美元),按高中毕业后年数分段;基准专业=liberal arts;方法=分位处理效应(DFL/Firpo RIF)。
  - 来源:【研究·NBER 工作论文;后发表于 Review of Economics and Statistics(2024)】Rodney J. Andrews, Scott A. Imberman, Michael F. Lovenheim & Kevin M. Stange · *The Returns to College Major Choice: Average and Distributional Effects, Career Trajectories, and Earnings Variability* · NBER WP 30331 · 2022-08 · https://www.nber.org/system/files/working_papers/w30331/w30331.pdf
  - 逐字摘引:"Quarterly returns (relative to liberal arts) range from **$983 in communications to $7,901 in engineering and architecture 16-20 years after high school**";"quantile treatment effect estimates…indicate there is substantial variation in how major choice influences the distribution of earnings, with some majors shifting the earnings distribution relatively uniformly and others – **notably fields that tend to have higher mean earnings - generating much larger effects at the top of the distribution. This suggests the mean effects embed substantial (and differential) ex-ante risk for students.**"
  - 关键补充(专业效应**随生涯增长**,与 [F11] 方向相反):"The returns to **biology and health grow the most over time, increasing by a factor of 12.7 (from $413 to $5,655)** over a 10 to 15-year period."
  - 反证:方法为 selection-on-observables,作者自陈"makes the **strong assumption** that these observables are sufficient to account for all differences across students in potential labor market outcomes"。

- **[F9]** **推翻"名校无所谓"主流叙事的最强新证据:Ivy-Plus 相对旗舰公立,对"进入收入前 1%"有大效应,但对"进入收入前 25%"效应小且不显著;对**对数收入**的影响很小(与 DK 一致)。**
  - 口径:数据=多所高校匿名招生数据 + IRS 个税记录 + SAT/ACT;识别=**候补名单(waitlist)**中录取决定的特异性变异(准随机),辅以复制 DK 的"matriculation design";结果=33 岁时的收入分位、是否就读顶尖研究生院、是否在"prestigious firm"就业;对照="the average flagship public college";Ivy-Plus=8 所常春藤 + Stanford + MIT + Duke + Chicago。
  - 来源:【研究·NBER 工作论文,未过审】Raj Chetty, David J. Deming & John N. Friedman · *Diversifying Society's Leaders? The Determinants and Causal Effects of Admission to Highly Selective Private Colleges* · NBER WP 31492 · 2023-07 · https://www.nber.org/system/files/working_papers/w31492/w31492.pdf
  - 逐字摘引(摘要):"attending an Ivy-Plus college instead of the average flagship public college increases students' chances of **reaching the top 1% of the earnings distribution by 50%**, **nearly doubles** their chances of attending an elite graduate school, and **almost triples** their chances of working at a prestigious firm."
  - **必须一起引的限定语**:"**The impact of Ivy-Plus admission on reaching the top quartile of the distribution is small and statistically insignificant**, while the impact on chances of reaching the top 1% far exceed what one would predict based on a constant percentage treatment effect… attending an Ivy-Plus college increases **mean earnings by $101,000 at age 33 (relative to a counterfactual mean of $143,000** if the same students were to attend state flagships)."
  - 作者对与 DK 分歧的解释(逐字,这是本线最重要的口径拆解):"the matriculation design again implies **modest impacts of attending an Ivy-Plus college on log earnings, consistent with the findings of Dale and Krueger (2002), whose primary outcome is log earnings**. Furthermore, we find **little association between students' average outcomes and the mean test scores of the college** they choose to attend, the proxy for college quality used by Dale and Krueger and others. In short, our findings differ from the conclusions of prior studies **not because of differences in research design** but rather because our richer data allow us to **directly identify college's fixed effects** (rather than using proxies for quality such as test scores) and **isolate impacts on upper tail outcomes**."
  - **对本线的直接含义**:"专业 vs 学校"这个二选一提法本身有陷阱——**结果变量选"中位数/对数收入"还是"上尾概率",会给出相反答案**。
  - 反证:上尾结果(前 1%、精英研究生院、名企)对绝大多数准大学生的期望效用意义有限;且样本为申请 Ivy-Plus 的候补生,外部效度窄。

- **[F10]** **DK 框架下的另一处异质性:性别。同一批 C&B 数据,男性零效应,女性非零。**
  - 口径:数据=College and Beyond;方法=DK matched-applicant 的变体;**不限于全职工作者**(这是与 DK 的关键口径差异);结果含收入、研究生学历、婚姻。
  - 来源:【研究·NBER 工作论文;发表于 Journal of Labor Economics 40(S1): 383-427, 2022】Suqin Ge, Elliott Isaac & Amalia R. Miller · *Elite Schools and Opting In: Effects of College Selectivity on Career and Family Outcomes* · NBER WP 25315 · https://www.nber.org/papers/w25315
  - 数字:院校平均 SAT 每高 100 分,女性获得研究生学历概率 +5 个百分点、收入 +14%、结婚概率 −4 个百分点;男性在控制选择后收入关系消失。
  - 反证/矛盾测量:【未取得全文】未取得 JOLE 正式版 PDF,上述数字来自检索摘要与 NBER 页面转述,Round 2 需核对原文表格与显著性。
  - 口径警示:**DK 把样本限定为"1995 年全职在业者"本身就是一个选择**,而女性的选择性退出劳动力市场正是被这个限定抹掉的东西。

- **[F11]** **专业效应会随生涯衰减——但只对"技术变化快"的专业成立,方向并非普遍收敛。**
  - 口径:数据=2009-2017 年 ACS(汇合);样本=23-50 岁四年制本科毕业生;结果=对数年工资薪金收入;回归=两年年龄组 × 专业交互,控制性别×年龄、年龄与年份固定效应、种族族裔、公民身份、退伍军人身份、**是否有任何研究生教育**;省略组=其他所有专业;标准误按 major×age 聚类。
  - 来源:【研究·已过审】David J. Deming & Kadeem Noray · *Earnings Dynamics, Changing Job Skills, and STEM Careers* · Quarterly Journal of Economics 135(4): 1965-2005, 2020-11 · https://academic.oup.com/qje/article/135/4/1965/5858010 (全文 PDF:https://www.sas.upenn.edu/~vr0j/oldteaching/712tqm-22/DemingNoray_2020.pdf)
  - 逐字摘引:"computer science and engineering majors earn about **45% more early in their career, but only 33% more by age 50**. The earnings advantage for **business** majors declines from around **38% initially to 20% by age 50**. **In contrast, the earnings premium grows over time for life and physical sciences and social sciences majors.**"
  - 机制证据(逐字):"the share of computer science and engineering majors working in computer and engineering occupations **declines from 59% at age 26 to 41% by age 50**. This decline of **18 percentage points** is almost entirely offset by increased employment in **non-STEM management occupations**."
  - 关键辨析(逐字):"**Declining relative returns is a feature of STEM jobs, not majors.** The earnings premium for **non-STEM majors in STEM occupations** starts off near 40%, but declines to 20% within a decade. In contrast, **the relative earnings advantage grows over time for computer science and engineering majors working in non-STEM occupations.**"
  - 作者自陈局限(逐字):"The STEM major premium **could reflect differences in unobserved ability across majors**, or differences in other job characteristics."
  - 反证:[F8] 的德州因果估计发现 biology/health、物理数学、传播学的相对回报**随生涯上升**(生物健康 10-15 年内涨 12.7 倍),说明"专业效应会衰减"不是普遍规律。

- **[F12]** **"转行率":美国有两套完全不同口径的数字,相差一倍以上,不可混用。**
  - 口径 A(**自报**,官方):"最高学历与当前工作的关系"——受访者自评。全体大学以上在职者(50,524,000 人):**closely related 54.1%(27,340,000)/ somewhat related 26.2%(13,258,000)/ not related 19.6%(9,927,000)**。**仅本科为最高学历者(31,373,000 人):closely 44.0%(13,818,000)/ somewhat 30.3%(9,508,000)/ not related 25.7%(8,048,000)**。
  - 来源 A:【官方】NSF NCSES · *National Survey of College Graduates: 2019*, Table 1-3 "Relationship of highest degree to job among employed college graduates, by level of highest degree, minor field of highest degree, and broad occupation: 2019" · NSF 22-310 · https://ncses.nsf.gov/pubs/nsf22310/assets/data-tables/tables/nsf22310-tab001-003.pdf (总体页面 https://ncses.nsf.gov/pubs/nsf22310/table/2-2);统计口径=居住在美国、至少学士学位、<76 岁,参考周为 2019-02-01 当周。百分比为本报告依据表中人数自算。
  - 口径 B(**分析师交叉编码**,研究):"College Major Match"——由研究者把专业与职业做对应表,只有**直接对口**才算匹配。**约 27% 的本科学历者(不含研究生学历者)在与本专业直接相关的岗位上工作**;另一指标 "College Degree Match"(岗位是否要求本科学历)约 62-67%。
  - 来源 B:【研究·联储工作论文,未过审】Jaison R. Abel & Richard Deitz · *Agglomeration and Job Matching among College Graduates* · Federal Reserve Bank of New York Staff Report No. 587 · https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr587.pdf ;数据=**2010 年 ACS**(1% 样本),16-64 岁,至少学士学位。
  - 逐字摘引 B:"We find that **about 27 percent of undergraduate degree holders are working in a job that is directly related to their college major**.";专业间差异:"about **73 percent** of these [Computer Science] majors work in jobs that require a college degree, while **33 percent** work in jobs directly related to their major";"**80 percent** of those with a Computer Engineering degree but only **44 percent** of those with a Studio Arts degree" 在需要本科学历的岗位上。
  - 匹配的收入回报(逐字):"college graduates working in a job that **requires a college degree** earn, on average, **almost 25 percent more**…those college graduates who work in a job **closely related to their college degree major** earn, on average, an **additional 5 percent** more."(注意:对口本身只值 +5%,**"有没有学历门槛"比"对不对口"重要 5 倍**)
  - 补充口径(专业细分,官方):Census Bureau 用 2019 ACS 1 年估计,25-64 岁在职大学毕业生中,工程 52%、计算机/数学/统计 51%、物理科学 28%、生物/环境/农业 16%、心理 10%、社科 9% 在 STEM 职业就业;"STEM workers who majored in a STEM field…typically made higher salaries than those who did not: on average, **$101,100 vs. $87,600**"。来源:【官方】U.S. Census Bureau · Jennifer Cheeseman Day & Anthony Martinez · *Does Majoring in STEM Lead to a STEM Job After Graduation?* · 2021-06-02 · https://www.census.gov/library/stories/2021/06/does-majoring-in-stem-lead-to-stem-job-after-graduation.html
  - 反证/搜索角度:搜过"major-job mismatch penalty""occupation-major mismatch"——存在一支文献称错配惩罚在上升(EdWorkingPaper 23-760),但**未取得全文**,Round 2 需核。

- **[F13]** **信号理论(Spence 1973)的核心机制与它对"专业选择"的不同预测。**
  - 口径:纯理论模型,无实证数字。
  - 来源:【研究·已过审】Michael Spence · *Job Market Signaling* · Quarterly Journal of Economics 87(3): 355-374, 1973 · 公开全文 https://www.sfu.ca/~allen/Spence.pdf
  - 逐字摘引(核心区分):"I shall refer to observable, **unalterable** attributes as **indices**, reserving the term **signals** for those observable characteristics attached to the individual that are **subject to manipulation by him**."
  - 逐字摘引(核心假设):"a signal will **not** effectively distinguish one applicant from another, **unless the costs of signaling are negatively correlated with productive capability**. For if this condition fails to hold…everyone will invest in the signal in exactly the same way, so that they cannot be distinguished on the basis of the signal."
  - 对本线的推论:在纯信号世界里,**"难专业"的价值来自它筛掉了低能力者(信号成本与能力负相关),而不是它教了什么**;这与人力资本解释在均衡薪资上观察等价,必须靠"文凭效应/羊皮纸效应"或断点设计来区分。
  - 反证(**信号理论的最强反例**):【研究·已过审】Damon Clark & Paco Martorell · *The Signaling Value of a High School Diploma* · Journal of Political Economy 122(2), 2014-04 · 公开全文 https://masteringmetrics.com/wp-content/uploads/2015/02/clark_martorell_2014.pdf ——用高中毕业会考的断点比较"刚过"与"刚没过"的人,**发现很少证据支持文凭本身有信号价值**,可拒绝"持文凭者多挣 8%"的假设,合并各州估计后可拒绝大于 5-6% 的信号值。
  - 对照文献(支持羊皮纸效应):【研究·已过审】David A. Jaeger & Marianne E. Page · *Degrees Matter: New Evidence on Sheepskin Effects in the Returns to Education* · Review of Economics and Statistics 78(4): 733-740, 1996 · https://econpapers.repec.org/RePEc:tpr:restat:v:78:y:1996:i:4:p:733-40 ——用 1991/1992 年 3 月 CPS 匹配样本(同时含**受教育年数**与**实际取得的学位**),发现显著的学位效应。**两者不矛盾:Jaeger-Page 是相关性设计,Clark-Martorell 是断点因果设计。**
  - 【未取得全文】Clark & Martorell 与 Jaeger & Page 均未取得正式期刊版 PDF 全文核对表格,数字来自公开预印/摘要转述,Round 2 需核。

- **[F14]** **能力分选(ability sorting)在多大程度上解释专业间收入差:控制选择后专业溢价依然大,但**分选本身**几乎不是由钱驱动的。**
  - 口径:数据=NLS72(1972 年高中毕业生纵向调查);模型=大学与专业选择的动态离散选择模型;专业合并为 4 类(自然科学、商科、社科/人文、教育);收入=1986 年,样本限周工作 30-60 小时、年收入在 5,500-148,500 美元(1999 年美元)之间者。
  - 来源:【研究·已过审】Peter Arcidiacono · *Ability Sorting and the Returns to College Major* · Journal of Econometrics 121(1-2): 343-375, 2004 · 作者公开稿 https://public.econ.duke.edu/~psarcidi/arcidimetrics.pdf
  - 逐字摘引(摘要):"**Even after controlling for selection, large earnings premiums exist for certain majors. Differences in monetary returns explain little of the ability sorting across majors; virtually all ability sorting is because of preferences for particular majors in college and the workplace**, with the former being larger than the latter."
  - 描述性反面(逐字):最高薪(自然科学)与最低薪(教育)专业 1986 年平均收入相差"more than sixteen thousand dollar";但"**those who chose not to attend college actually had higher average earnings than those who chose education**";作者随即警告"the results in Table 1 may be **in large part due to selection**"。
  - 相关证据:【研究·已过审】Douglas A. Webber · *The lifetime earnings premia of different majors: Correcting for selection based on cognitive, noncognitive, and unobserved factors* · Labour Economics 28: 14-23, 2014 · https://econpapers.repec.org/RePEc:eee:labeco:v:28:y:2014:i:c:p:14-23 ——数据=NLSY79 + ACS;通过加入 AFQT、母亲教育、Rotter 自控量表、Rosenberg 自尊量表来度量选择偏误的大小;结论商科与 STEM 回报最高、人文艺术最低,并发现各专业溢价在不同出生队列间**存在中度收敛**。【未取得全文】未取得正式版 PDF,量化幅度待核。

- **[F15]** **Chetty et al. 的"流动性成绩单"衡量的是**排名流动性**,不是绝对收入,且作者明确声明**不是因果**。这一点在传播中被大量误用。**
  - 口径:数据=1999-2013 年 3000 万+ 大学生的联邦纳税记录(与 1098-T 表匹配);"upward mobility rate"=**父母收入处于最低五分位、子女收入达到最高五分位的学生占该校学生的比例**(= 低收入准入率 × 该校低收入生进入顶层五分位的条件概率);"upper-tail mobility"=底部五分位→前 1%;子女收入在约 32-34 岁测量。
  - 来源:【研究·NBER 工作论文,未过审】Raj Chetty, John N. Friedman, Emmanuel Saez, Nicholas Turner & Danny Yagan · *Mobility Report Cards: The Role of Colleges in Intergenerational Mobility* · NBER WP 23618 · 2017-07 · https://www.nber.org/system/files/working_papers/w23618/w23618.pdf
  - 逐字摘引:"children whose parents are in the top 1%…are **77 times more likely** to attend an Ivy League college than those whose parents are in the bottom income quintile";"**rates of upward mobility – the fraction of students who come from families in the bottom income quintile and reach the top quintile – differ substantially across colleges because low-income access varies significantly across colleges with similar earnings outcomes**. Rates of bottom-to-top quintile mobility are **highest at certain mid-tier public universities, such as the City University of New York and California State colleges**. Rates of **upper-tail (bottom quintile to top 1%) mobility are highest at elite colleges**."
  - **必引的免责声明(逐字)**:"**Although our descriptive analysis does not identify colleges' causal effects on students' outcomes**, the publicly available statistics constructed here highlight colleges that deserve further study as potential engines of upward mobility."
  - 另一条常被漏掉的结论(逐字):"children from low- and high-income families have **similar earnings outcomes conditional on the college they attend**, indicating that low-income students are **not mismatched** at selective colleges."(这是对"低收入生进名校会 mismatch"这一说法的直接反驳)
  - 反证:见 [F4]——同一类"原始产出均值"在德州行政数据里被证明几乎不含因果增值信息。

- **[F16]** **Georgetown CEW 的专业收入数字是本线传播最广的一手来源,但必须按"研究/倡导机构"标注,并注意它给的是描述性中位数、不含因果校正。**
  - 口径(2015 报告):137 个细分专业、15 个大类;数据=Census(ACS)数据;"lifetime earnings" 为合成生涯累计。
  - 来源:【研究/倡导机构·Georgetown University Center on Education and the Workforce】Anthony P. Carnevale, Ban Cheah & Andrew R. Hanson · *The Economic Value of College Majors* · 2015-05-07 · https://cew.georgetown.edu/cew-reports/valueofcollegemajors/ (全文 PDF:https://cew.georgetown.edu/wp-content/uploads/The-Economic-Value-of-College-Majors-Full-Report-Web.compressed.pdf)
  - 数字:"The top-paying college majors earn **$3.4 million more** than the lowest-paying majors over a lifetime";最低薪专业:early childhood education($39,000)、human services($41,000)、studio arts / social work($42,000)、theology / elementary education($43,000)、drama and theater arts($45,000)。
  - 最新版(2025):【研究/倡导机构】CEW · *The Major Payoff: Evaluating Earnings and Employment Outcomes Across Bachelor's Degrees* · 2025-10-15 · https://cew.georgetown.edu/cew-reports/major-payoff/ ——"median earnings vary significantly by major for **prime-age workers**, from **$58,000 in education and public service fields to $98,000 in STEM fields**";STEM 内部 $64,000(miscellaneous agriculture)到 $146,000(petroleum engineering),共 65 个专业;人文艺术 $58,000-$73,000;本科对高中中位数溢价 70%;失业率 2.9% vs 6.2%。
  - 反证/局限:**CEW 未在检索到的摘要页给出因果性免责声明,也未给出院校 vs 专业的对比**;其口径为"prime-age workers"(需 Round 2 确认具体年龄区间与是否限全职),与 [F7] 的"仅本科最高学历、含兼职"口径不同,**两组数字不可并列**。
  - 【未取得全文】未下载 2025 版全文 PDF 核对数据年份、样本定义与方法附录。

- **[F17]** **英国(继续教育部门)的直接对比研究:"学什么"比"在哪学"更重要。**
  - 口径:数据=英格兰行政学籍 + 劳动力市场轨迹面板;对象=英格兰 Further Education(FE)学院的青年与成人学员(注意:**是继续教育/职业教育,不是大学**);结果=日收入、就业概率、学业成绩;VA=院校增值。
  - 来源:【研究·已过审】Esteban M. Aucejo, Claudia Hupkau & Jenifer Ruiz-Valenzuela · *Where versus What: College Value-Added and Returns to Field of Study in Further Education* · Journal of Human Resources 60(2): 607-652, 2025-03 · https://jhr.uwpress.org/content/60/2/607 ;工作论文版:CVER Discussion Paper 030(2020)· https://cver.lse.ac.uk/textonly/cver/pubs/cverdp030.pdf
  - 逐字摘引(工作论文版结论):"we also find important variations in returns to field of study, suggesting that **what one studies rather than where one does so may be more relevant for labour market outcomes**. Importantly, **labour market returns to specialisations tend to materialise only several years after graduation. The fact that the timing of measurement matters has important policy implications** for the evaluation of colleges."
  - 量级对照(工作论文版逐字):"Broecke (2012) shows that a one standard deviation increase in **university selectivity in the UK** leads to an increase in earnings of approximately **7%**… we conclude that our results **do not indicate substantial disparities in FE college value-added in wages**";一个标准差院校增值只提高"employed more than 90 days in a given year" 概率 **1.7 / 1.0 个百分点**(青年/成人)。
  - 【未取得全文】发表版 JHR 摘要中被广泛引用的"从专业 10 分位换到 90 分位,回报增幅比同样做院校增值练习**大约 84%**"这一数字,**未在工作论文版中检索到**,Round 2 必须回到 JHR 正式版核对该数字及其口径。

- **[F18]** **中国:院校层级("一本线")的因果溢价有断点证据,量级不小;但这不是"专业 vs 院校"的对比研究。**
  - 口径:数据=作者自建的"中国大学生调查(CCSS)"2010-2015 六轮,原计划抽 100 所高校、实际 90 所参与,共 40,916 名学生样本、34,733 人有完整高考成绩信息;识别=高考"第一批本科线(elite-tier cutoff)"断点;结果=**毕业时的第一份工作起薪**(自报)。
  - 来源:【研究·已过审】Ruixue Jia & Hongbin Li · *Just above the exam cutoff score: Elite college admission and wages in China* · Journal of Public Economics, 2021 · NBER WP 28450 · https://www.nber.org/papers/w28450
  - 逐字摘引:"those who score above the cutoff receive a **5.2–9.7% higher wage offer for their first job** after college, based on unweighted and weighted methods… The reduced-form estimate on wages, together with the discrete impact of scoring above the cutoff for elite college admission, implies that attending an elite college **increases the average monthly wage by 28–45% of the mean monthly wage** based on an instrumental variable (IV) approach."
  - **反向机制(极重要,常被漏掉)**:论文指出刚过线的学生"has a greater likelihood of being ranked toward the bottom in college",且在**专业**上处于劣势(即被挤出经济、金融、法律、STEM 等高薪专业)——**换句话说,"过线上更好的学校"是以"被调剂到更差的专业"为代价换来的,而净效应仍为正。** 这正是本线要问的"专业 vs 院校"权衡的中国版直接证据。
  - 口径警示(中美不等价):中国的"精英大学"由政府指定层级(作者原话:"The elite status of a college stems from **government designation**, not competition within the education market");结果变量是**第一份工作起薪(自报、月薪、含义未明是否税前/含社保)**,与美国研究的"33 岁 IRS 记录年收入"完全不同,**绝不可并列**。
  - 反证/搜索角度:搜过"中国 专业 收入 断点/因果""专业调剂 收入"——**未检索到**中国境内用录取分数断点识别**专业(而非院校)**因果回报的一手研究。这是本线的中国侧空白。

- **[F19]** **中国"专业对口率"数字:71%(2025 届本科),但**追不到一手**,且与美国任何一个口径都不可比。**
  - 口径:麦可思"工作与专业相关度",毕业半年后调查;媒体转述称 2025 届本科 71%、高职 59%;医学类本科半年后 89%,2020 届五年后 91%;2025 届本科平均月收入 6,435 元。**未取得样本量、抽样框、问卷措辞与"相关度"的操作化定义。**
  - 来源:【商业调查/媒体转述】麦可思研究院《中国本科生就业报告》(就业蓝皮书);经搜狐转述 https://www.sohu.com/a/1035297877_121478296 ;麦可思官网 http://www.mycos.net.cn / http://www.mycosinstitute.org 在本次检索中**连接被拒/证书不匹配,无法访问**。
  - 【追不到一手】搜过的角度:麦可思官网新闻页、麦可思研究院服务页、"就业蓝皮书 2025/2026 新闻发布会"、"社会科学文献出版社 就业蓝皮书"。社科文献出版社数据库有条目(https://cpms.ssap.com.cn/skwx_cmr/bookdetail?SiteID=23&ID=8096322)但未取得内容。
  - **口径冲突警示**:媒体转述中"2025 届 71%"同时被挂在《2025 年中国大学生就业报告》和《2026 年中国大学生就业报告》名下(搜狐文中标注发布日为 2026-06-11),**报告年份与届别对应关系存疑**,Round 2 必须核实。
  - 中美不等价:麦可思 71% 是**毕业生自评的"相关度"**,最接近美国 NSCG 的"closely + somewhat related"(本科 44.0% + 30.3% = 74.3%),而**绝不能**与 Abel-Deitz 的 27%(分析师交叉编码的直接对口)比较。且麦可思是**毕业半年后**、NSCG 是**全年龄段在职者**。

---

### 交叉口径问题(Round 2 必须核对)

1. **"Dale-Krueger 证明上什么学校不重要"是最严重的口径截断。** 三处限定必须保留:(a) 结果变量是**对数收入**(均值/中位数),不是上尾;(b) 样本是 **C&B 的 30 所院校**,本身都是选择性较高的四年制大学,**不覆盖"重点 vs 普通"的大跨度对比**,作者原文明说 "does not pertain to a nationally representative sample of schools";(c) **学费(办学支出)溢价从未消失**,消失的只是"同学平均 SAT"溢价。DK 自己的政策结论是"给弱势学生更多进精英校的机会可能提高国民收入",而不是"学校无所谓"。

2. **DK vs Chetty-Deming-Friedman 的分歧是"结果变量口径"分歧,不是"研究设计"分歧。** CDF 用 DK 的 matriculation design 复现,得到"对数收入影响很小"(与 DK 一致)+"进入前 1% 概率 +50%"(DK 从未测过)。写作时若把两者写成"新研究推翻旧研究",是错的;正确表述是**"名校对中位数几乎没用,对上尾极有用"**。同时 CDF 明确说"进入前 25% 的效应小且不显著"——这一句在几乎所有媒体转述里被删掉。

3. **"专业比学校重要"这句话在不同数据里有不同真值。** Kirkebøen et al.(挪威、断点因果)和 Aucejo et al.(英国 FE)支持;Mountjoy-Hickman(德州)显示院校因果增值窄(10-90 分位仅 $4,440/年),间接支持;但 CDF(美国 Ivy-Plus 上尾)方向相反。**三者的"学校"定义完全不同**:挪威=同一集中录取体系内的院校;德州=公立大学;CDF=Ivy-Plus vs 旗舰公立。绝不可并列。

4. **"转行率"至少三套口径,数字从 19.6% 到 73% 都能"合法"引用:**
   - NSCG 自报"not related":全体 19.6% / 仅本科 25.7%(2019)
   - Abel-Deitz "College Major Match" 反面:约 **73%** 的本科学历者不在直接对口岗位(2010 ACS)
   - Census "STEM 专业不在 STEM 职业":工程 48%、CS/数学 49%、生物 84%(2019 ACS)
   媒体常见的"74% 的 STEM 毕业生不做 STEM 工作"(2014 年 Census 新闻稿口径,基于 2012 ACS)与上面任何一个都不同。**Round 2 需固定一个口径并全文一致。**

5. **Hamilton Project 的"专业内方差 ≥ 专业间方差"与"高分位处专业差距扇形放大"是同一份报告里的两句话,方向相反。** 只引前一句会得出"选什么专业无所谓",只引后一句会得出"专业决定一切"。必须同时引。Andrews et al. 的分位处理效应给了因果版本的同一现象。

6. **Hamilton Project 与 CEW 的"生涯累计收入"都是合成队列(把某一年横截面的各年龄组收入拼起来),不是真实追踪。** 两者样本口径还不同:HP 限"仅本科、未读研",且**含兼职与失业者**;CEW 2025 版限"prime-age workers"(具体定义待核)。**两份报告的绝对数字不可互换。**

7. **Hoxby 对 DK 的两段批评措辞差异极大**(2009 JEP:"much less credible"、"very odd choice";2015:"not intended to criticize their study")。Econlib 博客只引前者。若引用 Hoxby 的批评,必须注明是 2009 年的版本,且注明她 2015 年的更精确表述(方法只适用于水平选择)。

8. **Deming-Noray 的 "CS/工程溢价从 45% 降到 33%" 是相对"所有其他专业"的对数工资溢价,不是绝对收入下降。** 原文明说 "In levels, earnings growth is rapid for all college graduates, regardless of major"。媒体常写成"CS 毕业生中年后收入下滑",是错的。

9. **中国数字全部需要单列口径栏**:Jia & Li 的结果是**第一份工作起薪、自报、月薪**;麦可思是**毕业半年后自评相关度、月收入**。与美国的 IRS/SSA 行政年收入、33 岁/36-38 岁、税前口径无一对应。

10. **Kirkebøen et al. 的 "payoffs rival the college wage premium" 里的 "college wage premium" 是作者用**自己样本**算出的挪威口径(43,200 → 54,700 美元,约 +27%),不是美国的大学溢价(约 +70-80%)。若把这句话搬到中美语境说"选专业和上不上大学一样重要",是**换了分母**。

---

### 未取得/存疑

- **【未取得全文】** Aucejo, Hupkau & Ruiz-Valenzuela, JHR 60(2), 2025 正式版。广为引用的"专业 10→90 分位的回报增幅比院校增值大 **84%**"仅见于二手摘要,CVER 工作论文版中未检索到该数字。付费墙:https://jhr.uwpress.org/content/60/2/607(Project MUSE 有验证墙)。
- **【未取得全文】** Ge, Isaac & Miller, *Journal of Labor Economics* 40(S1), 2022。女性 +14% 收入、+5pp 研究生学历、−4pp 结婚率的数字来自检索摘要,未核原表。NBER WP 25315 可作替代:https://www.nber.org/papers/w25315
- **【未取得全文】** Webber (2014), Labour Economics 28:14-23。ScienceDirect 返回 403。EconPapers 摘要仅一句话,选择校正对专业溢价的**削减幅度**未取得。
- **【未取得全文】** CEW *The Major Payoff*(2025-10-15)完整 PDF 及方法附录:数据年份、"prime-age" 定义、是否限全职、是否含研究生学历者,均未确认。作者名单也未从页面取得。
- **【未取得全文】** Clark & Martorell (2014 JPE) 与 Jaeger & Page (1996 ReStat) 正式版。前者有公开教学副本(masteringmetrics.com),后者仅有 EconPapers 条目。
- **【追不到一手】** 麦可思《中国大学生就业报告》原始发布:官网 mycos.net.cn 连接被拒(ECONNREFUSED),mycosinstitute.org 证书不匹配。所有数字目前只有搜狐/网易/凤凰的媒体转述。且**报告届别与年份的对应关系存疑**(同一 71% 被挂在 2025 与 2026 两个报告名下)。
- **【追不到一手】** 未找到中国境内用**专业录取分数断点**识别专业因果回报的一手研究(挪威 Kirkebøen 那类)。搜过角度:"高考 专业 分数线 断点 收入""college major regression discontinuity China""专业调剂 工资"。中国侧只有院校层级(一本线)的断点证据。
- **【存疑,待核】** NY Fed *The Labor Market for Recent College Graduates* 交互数据页(分专业失业率/低度就业率/收入分位)本次 WebFetch 返回 403,未能取得最新(2026 年)分专业收入分位数据。这是本线"分布重叠度"论断唯一缺的**当期**数据源,建议 Round 2 换路径取(如 NY Fed 的 Excel 下载链接或 Staff Report 749)。
- **【存疑,待核】** EdWorkingPaper 23-760 *The Increasing Penalty to Occupation-Major Mismatch*(2023-04)存在,URL https://edworkingpapers.com/sites/default/files/ai23-760.pdf,但未取得内容。若成立,会直接反驳"专业不重要、反正都要转行"这条线。

**本轮搜索但未发现证据的角度(记录以备核查):**
- 搜过"专业效应在生涯中期收敛/消失"的一般性证据——**只找到方向不一致的结果**:Deming-Noray(CS/工程/商科溢价收窄,生命科学/社科扩大)、Andrews et al.(生物健康、物理数学、传播学的回报**随生涯上升**)、Webber(队列间"中度收敛")。**没有一篇支持"专业效应普遍衰减"的强证据。**
- 搜过"院校效应随生涯扩大 vs 缩小"——Mountjoy-Hickman 明确说选择性溢价**衰减到零**;DK 2011 说 1976 与 1989 队列在同一生涯阶段上的选择性回报**没有随时代上升**。未发现"名校效应随生涯放大(中位数口径)"的一手证据。
- 搜过中国"985/211 vs 专业"哪个对起薪影响更大的一手计量研究——**未找到**符合一手来源标准的结果。

---

## 线 G:执照护城河职业(护理/医疗/教育)——抗自动化是真的,但代价呢

> 数据截止 2026 年 7 月。本线最重要的发现是:**"护城河"在"不失业"这个维度上是真的、且证据很硬;但在"高增长""高薪""执照带来溢价""短缺会持续"这四个维度上,一手证据要么不支持,要么被官方自己下修了。**

---

### 关键论断

#### 一、正面:护城河在"不失业"维度上是真的

- **[G1]** NY Fed 按专业口径:护理专业应届生失业率 2.1%、低度就业率 12.8%,是全部 75 个专业中低度就业率最低的一档;计算机科学同口径失业率 7.0%、低度就业率 19.1%。
  - 口径:分子/分母=22–27 岁、持学士及以上学位、且**当前未在校就读**者中的失业/低度就业人数 ÷ 该专业同龄劳动力。低度就业(underemployment)定义为"从事不要求学士学位的工作"。中位工资一栏仅限**全职、且最高学历为学士**者。数据年份 2024(ACS/IPUMS 微观数据),发布日 2026-02-04。全体专业均值:失业率 4.2%、低度就业率 39.4%。
  - 来源:【官方】Federal Reserve Bank of New York · "The Labor Market for Recent College Graduates — Outcomes by Major" · 最新发布 2026-02-04(2024 年数据)· https://www.newyorkfed.org/research/college-labor-market
  - 逐字摘引(表注):"Unemployment and underemployment rates are for recent college graduates (that is, those aged 22 to 27 with a bachelor's degree or higher), and median wages are for full-time workers with a bachelor's degree only."
  - 反证/矛盾测量:同一张表显示护理的**中期工资曲线极平**——早期中位 $70,000 → 中期(35–45 岁)$87,000,涨幅 +24%;而全体专业均值 $58,000 → $87,000,涨幅 +50%;计算机科学 $87,000 → $120,000,涨幅 +38%。**护理的 35–45 岁中位工资($87,000)恰好等于全体专业的中位数**。即:护理买到的是确定性,不是高度。教育类更极端:小学教育失业率仅 1.2%(全表最低之一),但早期 $45,000 → 中期 $55,000,涨幅仅 +22%。

- **[G2]** 微软研究院基于**真实 AI 使用日志**的职业适用度评分:医疗诊疗类执业者 0.13、家庭健康助理与护理助理 0.04、职业/物理治疗助理 0.05、其他医疗支持类 0.06;对照计算机类职业 0.29、数学科学类 0.32。
  - 口径:分子/分母=对 20 万条经匿名化与隐私清洗的 Microsoft Bing Copilot 人机对话,用 LLM 流水线归类到 O*NET 的中间工作活动(IWA),再按 SOC 次要职业组的**就业加权平均**聚合;分数为"用户目标适用度"与"AI 行为适用度"两者的均值。数据窗口为 2024 年 Copilot 对话样本。
  - 来源:【研究·工作论文,未标注过审】Tomlinson, Jaffe, Wang, Counts, Suri · "Working with AI: Measuring the Applicability of Generative AI to Occupations" · arXiv:2507.07935,首版 2025-07-10,v6 2025-12-22 · https://arxiv.org/abs/2507.07935
  - 逐字摘引(论文自设限定语):"It is tempting to conclude that occupations that have high AI action applicability score will be automated and thus experience job or wage loss... **This would be a mistake**, as downstream consequences of new technologies are very hard to predict and often counterintuitive." 作者在配套博客(2025-08-21)中再次声明:"our study does not draw any conclusions about jobs being eliminated; in the paper, we explicitly cautioned against using our findings to make that conclusion."(https://www.microsoft.com/en-us/research/blog/applicability-vs-job-displacement-further-notes-on-our-recent-research-on-ai-and-occupations/)
  - 反证/矛盾测量:**同一张表里,中小学与特教教师是 0.18,明显高于护理类(0.13),也高于律师(0.17)**;大学教师 0.31,高于计算机职业(0.29)。也就是说"教育=抗 AI 护城河"在这份数据里**不成立**——教育的 AI 暴露度接近知识工作,而非接近护理。这一条应直接推翻"护理和教育同属抗自动化阵营"的叙事。

#### 二、正面:执照壁垒确实存在(但覆盖率数字有版本差异)

- **[G3]** 美国需持州政府执照才能合法从业的劳动力占比,从 1950 年代初的不足 5% 升至 2008 年的约 29%;白宫报告口径为"超过四分之一"、"约 25%"。
  - 口径:分子=自报需持照才能合法从事本职工作的在职者;分母=全体在职者。29% 来自 Kleiner & Krueger 2008 年专门设计的全国劳动力调查(自报口径,非行政记录)。白宫报告的"约 25%"与"州级持照份额自 1950 年代起翻了五倍"为不同分子(仅州级发照)。约三分之二的增长来自"需持照的职业种类增加",而非既有持照职业就业扩张。
  - 来源:【研究·Brookings 政策报告】Morris M. Kleiner · "Reforming Occupational Licensing Policies" · The Hamilton Project Discussion Paper 2015-01,2015 年 3 月 · https://www.brookings.edu/wp-content/uploads/2016/06/THP_KleinerDiscPaper_final.pdf
  - 【官方】U.S. Dept. of the Treasury Office of Economic Policy, Council of Economic Advisers, U.S. Dept. of Labor · "Occupational Licensing: A Framework for Policymakers" · 2015 年 7 月 · https://obamawhitehouse.archives.gov/sites/default/files/docs/licensing_report_final_nonembargo.pdf
  - 逐字摘引(Kleiner):"In the early 1950s less than 5 percent of U.S. workers were required to have a license from a state government in order to perform their jobs legally. By 2008, the share of workers requiring a license to work was estimated to be almost 29 percent."
  - 逐字摘引(白宫):"More than one-quarter of U.S. workers now require a license to do their jobs... The share of workers licensed at the State level has risen five-fold since the 1950s."
  - 反证/矛盾测量:白宫报告同时给出州际极差——**南卡罗来纳 12%,爱荷华 33%**,说明"25–29%"是全国平均,单一数字掩盖了三倍差异。欧盟同期为 9–24%,即美国是发达国家中偏高的。

#### 三、反面(重点):执照溢价对护士和教师**恰恰不成立**

- **[G4]** 执照工资溢价的可信估计只有 10–15%(全国普遍持照职业)乃至 5–8%(仅部分州持照的职业);且 Kleiner 明确指出:**对护士、教师、美容师这三类,执照对收入的影响"murky",有的研究测到微小效应,有的测到零。**
  - 口径:10–15% 为"在全国普遍持照职业中工作"相对于教育、技能相近的非持照者的**小时**工资差(Gittleman/Klee/Kleiner 2014;Kleiner & Krueger 2010, 2013)。5–8% 为"同一职业在部分州持照、部分州不持照"的识别设计——**这是识别更干净的一组,系数明显更小**,提示 10–15% 里含有大量职业选择/能力自选造成的偏误。溢价集中在本就高薪的职业。
  - 来源:【研究·Brookings 政策报告】同 [G3],Kleiner 2015 · 第 13 页
  - 逐字摘引:"For occupations associated with both higher education and higher income and that are mainly in the private sector, such as physicians, dentists, and attorneys, licensing appears to have large effects... **However, for other occupations, including teachers, nurses, and cosmetologists, the impact of licensing on earnings is murky, with some studies finding small effects and others finding none.**"
  - 反证/矛盾测量:主动搜了"执照对护士工资有正向溢价"的证据。Kleiner 本人是执照批评方,其立场需打折;但白宫 2015 报告(跨部委官方文件、立场更中性)给出的数字是 10–15%,并未对护士单列更高的估计。**未发现任何一手研究给出"护理执照带来显著工资溢价"的估计**。

- **[G5]** 执照提升服务质量的证据极弱:白宫报告复核的 12 项质量研究中,**仅 2 项**发现更严执照与质量改善相关;而复核的 11 项价格研究中,**9 项**发现更严执照伴随显著更高价格。
  - 口径:白宫报告 Research Appendix Table 1(质量,12 项)与 Table 2(价格,11 项)的文献计票。价格影响幅度 3–16%(Kleiner 2015 另给 5–33% 的区间,依职业与地区而异)。
  - 来源:【官方】同 [G3] 白宫 2015 报告,第 13 页
  - 逐字摘引:"most research does not find that licensing improves quality or public health and safety... **Stricter licensing was associated with quality improvements in only 2 out of the 12 studies reviewed.**"
  - **对护理最直接的一条**:"more restrictive State licensing of nurse practitioners raises the price of a well-child medical exam by 3 to 16 percent"——即**限制 NP 独立执业权的执照规则,损害的是 NP 自己**(Kleiner 2015 给出的同一发现为"raises prices of well-child exams by 10 percent")。
  - 反证/矛盾测量:报告自己承认质量难测量、文献集中于特定案例("the literature focuses on specific examples and that quality is difficult to measure")。Kleiner 2015 也列出**正向证据**:建筑承包商放宽发照会降低质量提升效应(Maurizi 1980);会计师在要求 3 年以上经验的州,入职后接受培训的概率高 26–36%(白宫报告)。**Larsen 2012** 是教师执照的正向证据:富裕学区更严的教师执照与更高标准化考试分数相关——但**低收入学区完全无关**。

- **[G6]** 执照显著抑制跨州流动:采用州专属执照考试的职业,其跨州迁移率比其他职业低 36%。
  - 口径:识别策略为比较"州专属执照考试"职业 vs "全国统一执照考试"职业(以此剥离"持照职业本身流动性低"的混淆);因变量为跨州迁移率。共 22 个持照职业。
  - 来源:【研究·同行评审】Janna E. Johnson & Morris M. Kleiner · "Is Occupational Licensing a Barrier to Interstate Migration?" · American Economic Journal: Economic Policy, Vol. 12, No. 3 (2020 年 8 月), pp. 347–73 · https://www.aeaweb.org/articles?id=10.1257/pol.20170704
  - **重要限定语(反证)**:护士恰恰**不在**受害最重的一类——RN 使用**全国统一的 NCLEX 考试**,且护士执照互认协议(Nurse Licensure Compact, NLC)已覆盖约 43 个辖区(截至 2026 年);相比之下律师、部分医师专科为州专属。**因此 [G6] 的 36% 不能直接套到护士头上。** 【未取得全文】未能取得论文全文以确认 22 个职业名单中 RN 的具体归类,Round 2 需核。NLC 辖区数量仅取到聚合类媒体口径,**【追不到一手】**——已搜 NCSBN 官网 nlc 页面,未在本轮取得带日期的官方计数。

#### 四、反面:BLS 自己的数字不支持"医疗是最高增长赛道"

- **[G7]** 2024–2034 十年:**计算机与数学类职业(+10.1%)projected 增速快于医疗执业与技术类职业(+7.2%)**;全经济体仅 +3.1%。
  - 口径:BLS Employment Projections,基年 2024、目标年 2034,主要职业大类的就业人数百分比变化。发布日 2025-08-28,文号 USDL-25-1324。全经济体 2024 年 169,956.1 千人 → 2034 年 175,167.9 千人(+5,211.8 千,+3.1%);对照上一个十年(2014–24)实际增长 13.0%。
  - 来源:【官方】U.S. Bureau of Labor Statistics · "Employment Projections: 2024-2034 Summary" · 2025-08-28 · https://www.bls.gov/news.release/ecopro.nr0.htm
  - 逐字摘引:"Computer and mathematical occupations are projected to grow the second fastest of any occupational group (+10.1 percent), which is more than three times the average rate of growth projected for the total economy (+3.1 percent)."
  - 反证/矛盾测量:医疗**支持**类(healthcare support,即护理助理、家庭健康助理等低薪岗)+12.4%,确实高于计算机类——但这一类的中位年薪是 $34,900(家庭健康与个人护理助理),不是"体面就业"的候选。BLS 在同一新闻稿加了自我限定框:"this precision in the data does not account for the inherent uncertainty of predicting long-term changes in the labor market."

- **[G8]** 逐职业细看:NP 增速 40.1% 是真的,但**基数小、绝对增量少于软件开发**;而 RN 增速仅 5%。
  - 口径(全部为 BLS EP Table 1.3 / OOH,基年 2024、目标年 2034,中位年薪为 OEWS 2024 年 5 月):
    | 职业 | SOC | 2024 就业(千) | 2034 就业(千) | 绝对增量(千) | 增速 | 2024 中位年薪 |
    |---|---|---|---|---|---|---|
    | Nurse practitioners | 29-1171 | 320.4 | 448.8 | **+128.4** | **+40.1%** | $129,210 |
    | Software developers | 15-1252 | 1,693.8 | 1,961.4 | **+267.7** | +15.8% | **$133,080** |
    | Data scientists | 15-2051 | 245.9 | 328.3 | +82.5 | +33.5% | $112,590 |
    | Physician assistants | 29-1071 | 162.7 | 195.8 | +33.2 | +20.4% | $133,260 |
    | Physical therapist assistants | 31-2021 | 111.5 | 136.0 | +24.5 | +22.0% | $65,510 |
    | Home health & personal care aides | 31-1120 | 4,347.7 | 5,087.5 | +739.8 | +17.0% | $34,900 |
    - OOH 层面:**RN** 2024 年 3,391,000 人,2024–34 增速 **5%**(+166,100),年均缺口 189,100 个,2024 年中位 $93,600/年($45.00/小时);**APRN 合并组**(麻醉护士+助产士+NP)382,700 人,增速 35%,年均缺口仅 **32,700** 个,中位 $132,050;**PA** 增速 20%,中位 $133,260;**PT** 增速 11%,中位 $101,020(需博士/专业学位)。
  - 来源:【官方】BLS · "Table 1.3 Fastest growing occupations, 2024 and projected 2034" · 更新 2025-08-28 · https://www.bls.gov/emp/tables/fastest-growing-occupations.htm;【官方】BLS OOH 各职业页,末次修订 2025-08-28
  - 反证/矛盾测量:**这是本线最需要写进正文的对照**——"NP 是全美第三快增长职业"为真,但十年只新增 12.8 万个岗位,而"增速平庸"的软件开发新增 26.8 万个、且中位年薪更高。**给准大学生的现实含义是:NP 赛道窄且需硕士学位,不是可规模化的选项。**

#### 五、反面:年薪口径陷阱(护士的 12 小时班 vs 教师的 10 个月工作年)

- **[G9]** OEWS 的"年薪"是**按每年 2,080 小时全职全年折算的**,不是实发年收入;因此 RN 的 $93,600 已隐含"全年 40 小时/周"的假设,不含加班溢价的额外工时,也不体现夜班/周末津贴的分布。
  - 口径:OEWS 明确声明 "The OEWS annual wage estimates assume a full-time, year-round schedule of 2,080 hours."
  - 来源:【官方】BLS · "Occupational Employment and Wage Statistics — Questions and Answers" · https://www.bls.gov/oes/oes_ques.htm
  - 反证/矛盾测量:**教师方向是反向偏误**——BLS 的 OOH 教师页面只给"per year"、**不给"per hour"**(RN 页面两者都给),因为教师的工作年份不是 12 个月。因此"RN $93,600 vs 高中教师 $64,580"这个对比**两端的时间口径都不是可比的**:一端是虚构的 2,080 小时,另一端是约 9–10 个月合同。Round 2 必须处理。

#### 六、反面:护士离职意向的数字被严重误读

- **[G10]** NCSBN 2024 年全国护士队伍调查:**39.9% 的 RN 表示计划在未来 5 年内退休或离开护理**——但其中 **21.9 个百分点是"计划退休"**,只有 **18.0 个百分点是"计划离开护理(非退休原因)"**。且该问题**在 2024 年被改写过**,2022 年的 28.7% 与之不可直接比较。
  - 口径:分母=**仅限当前在护理岗位就业的** RN 受访者(加权后 N=542,343.9;夏威夷州未施测该题);时间窗=调查执行期 2024-03-25 至 2024-12-31,"未来 5 年"≈至 2029。问法为原二元(是/否)题,2024 年新增选项拆分"计划退休"与"计划离开护理"。趋势:2020 年 22.1% → 2022 年 28.7% → 2024 年 39.9%。LPN/LVN 同题 41.3%(其中退休 18.6pp、离开 22.7pp)。RN 与 LPN/LVN 中位年龄均为 50 岁。
  - 来源:【研究·期刊增刊,NCSBN 官方调查】Smiley RA, Kaminski-Ozturk N, Reid M, …, Martin B · "The 2024 National Nursing Workforce Survey" · Journal of Nursing Regulation, Vol. 16, Issue 1 Supplement, S1–S88, 2025 年 4 月 · https://www.journalofnursingregulation.com/article/S2155-8256(25)00047-X/fulltext
  - 逐字摘引(原文自述工具变更):"The 2024 survey **added one new question** pertaining to nurses' intent to leave"; 表 27 注:"This question was introduced in the 2020 survey and **modified in 2024** to offer separate options for those who plan to retire, and those who plan to leave nursing."
  - 逐字摘引(离职原因,N=34,644.3,多选):退休 52.4%、压力与倦怠 41.5%、工作量 32.6%、人手不足 29.5%、薪酬不足 25.0%、职场暴力或霸凌 11.0%。
  - **反证/矛盾测量(强)**:同一份调查显示**倦怠在下降**——"每天或每周数次感到 burned out"的 RN 比例从 2022 年的 45.2% 降至 2024 年的 **35.4%**;"每天感到情绪耗竭"从 23.9% 降至 18.9%;"从不感到倦怠"从 10.9% 升至 15.0%。摘要原文:"While reported levels of emotional exhaustion, including burnout, and workloads have **moderated** over the past 2 years, about 40% of nurses report they plan to leave nursing or retire over the next 5 years." 另:调查各州回收率仅约 9–22%(如加州 RN 14.0%、蒙大拿 22.3%),**存在明显无回应偏误风险**,倾向离职者更可能作答。

- **[G11]** 医院 RN 实际离职率(**行为**而非**意向**)已从疫情峰值大幅回落:CY2025 为 17.6%,CY2022 峰值为 27.1%。
  - 口径:分子=当年 RN 主动+被动离职人数,分母=平均在职 RN;**明确排除临时工、中介工与旅行护士**,不计内部调岗。样本=527 家急症照护医院、40 个州、覆盖 965,886 名医护与 262,405 名 RN,自愿报名参与(**自选样本,非概率抽样**)。数据年份 CY2025,报告发布 2026 年 3 月。同期医院全员离职率 18.5%;RN 空缺率 8.6%(NSI 自述本年更改了计算方法,与去年 9.6% 不可直接比较);招到一名有经验 RN 平均需 78 天。
  - 来源:【商业调查·利益相关】NSI Nursing Solutions, Inc.(**护士招聘/猎头公司**)· "2026 NSI National Health Care Retention & RN Staffing Report" · 2026 年 3 月 · https://www.nsinursingsolutions.com/documents/library/nsi_national_health_care_retention_report.pdf
  - **利益披露(必须写进正文)**:该报告在执行摘要里直接嵌入销售话术——"Every RN hired saves $66,081. An NSI contract to replace 20 travel nurses could save your institution $1,322,000… Contact Michael Colosi at (717) 575-7817 to learn how NSI can improve your bottom line." 其"每名 RN 离职成本 $60,090""全国 RN 缺口 158,600"均为自估、无独立验证。**这是媒体引用最频繁的护士离职数字来源,但它是招聘公司的销售材料。**
  - 反证/矛盾测量:趋势线 CY21 25.9%(全员)/27.1%(RN,CY22)→ CY25 18.5%/17.6%,**方向与"护士大逃亡持续恶化"的叙事相反**。

#### 七、反面:官方短缺预测被大幅下修,NP 更是预测**过剩**

- **[G12]** HRSA 把 RN 短缺预测从 337,970 FTE(2036 年,2024 年 3 月版)下修到 **108,960 FTE(2038 年,2025 年 12 月版)**;且都会区 2038 年短缺仅 **2%**,非都会区 11%。
  - 口径:HRSA Health Workforce Simulation Model(HWSM),供给与需求均以 FTE 计(FTE 定义为每周 40 小时),"短缺%"= 1 −(预测供给÷预测需求)。旧版基年 2021、目标年 2036;新版基年 2023、目标年 2038。旧版明确警告其使用了疫情期间数据。
  - 来源:【官方】HRSA National Center for Health Workforce Analysis · "Nurse Workforce Projections, 2021-2036" · 2024 年 3 月;及 · "Health Workforce Projections"(2023–2038 投影,2025 年 12 月发布)· https://bhw.hrsa.gov/data-research/projecting-health-workforce-supply-demand
  - 逐字摘引(2024 年 3 月版):"By 2036, the shortage is 9% (a shortage of 337,970 full-time equivalent [FTE] RNs)... These projections assume that historical patterns of attrition, graduation, and labor force participation remain the same over the forecast period."
  - 逐字摘引(2025 年 12 月版页面):"NCHWA projects nationwide nursing shortages, including: 108,960 registered nurses (RNs), 245,950 licensed practical nurses (LPNs)... In 2038, there is a projected shortage of 11% for RNs in nonmetropolitan areas while there is a projected shortage of 2% for RNs in metropolitan areas."
  - 反证/矛盾测量:LPN 的短缺反而扩大(旧版 2036 年 99,070 FTE → 新版 2038 年 245,950 FTE)。医师短缺仍然巨大:2038 年 141,160 名(其中初级保健 70,610 名);非都会区初级保健短缺 39%,都会区 5%。**结论应是"短缺是地理问题,不是职业问题"**,而非"护理整体短缺"。

- **[G13]** HRSA 预测 **NP 供给将大幅超过需求**:2036 年供给 652,870 FTE vs 需求 340,830 FTE,充足率 **192%**。
  - 口径:同 [G12] 旧版(2024 年 3 月,基年 2021)。充足率=预测供给÷预测需求。分年:2026 年 132%、2031 年 164%、2036 年 192%。麻醉护士 2036 年 118%、助产士 139%,同样过剩。
  - 来源:【官方】同 [G12],HRSA 2024 年 3 月 factsheet,Exhibits 1a–1c
  - 逐字摘引:"At the national level, the supply of nurse practitioners (NPs) is projected to exceed demand over the projection period; however, distribution remains the most important issue."
  - **这是本线最反直觉、也最该写进正文的一条**:BLS 说 NP 是全美第三快增长职业(+40.1%),HRSA 说 NP 到 2036 年供给将是需求的近两倍。两者不必然矛盾(BLS 预测的是实际就业=已实现的需求侧,HRSA 分别预测供需),但对准大学生的含义是一致的:**NP 的培养管道扩张速度远快于需求扩张速度**。
  - 【未取得全文】2025 年 12 月版 HRSA 护理简报 PDF 反复 403,未取得 2038 年 NP 的更新数字;该网页的护理短缺清单只列 RN 与 LPN、未列 NP,**间接**提示 NP 仍为过剩,但 Round 2 需通过 Workforce Projections Dashboard 核实。

#### 八、反面:教师——BLS 预测三个学段**全部负增长**

- **[G14]** 美国 K–12 教师 2024–2034 全部预测**下降**:幼儿园与小学教师 −2%(−29,800)、初中 −2%(−12,400)、高中 −2%(−17,800)、特教 −1%(−7,700)。
  - 口径:BLS OOH,基年 2024、目标年 2034。规模:小学 1,539,800 人、高中 1,094,500 人、初中 633,700 人、特教 559,500 人。中位年薪(2024 年 5 月):小学 $62,310、初中 $62,970、高中 $64,580、特教 $64,270、学前 $37,120。小学教师年均岗位缺口 103,800 个——OOH 明确写明这些缺口**全部**来自替补离职,而非新增。
  - 来源:【官方】BLS OOH · Kindergarten and Elementary School Teachers / Middle School Teachers / High School Teachers / Special Education Teachers · 末次修订 2025-08-28 · https://www.bls.gov/ooh/education-training-and-library/
  - 逐字摘引:"Despite declining employment, about 103,800 openings for kindergarten and elementary school teachers are projected each year, on average, over the decade. **All of those openings** are expected to result from the need to replace workers who transfer to other occupations or exit the labor force."
  - 反证/矛盾测量:教育与图书馆大类整体年均缺口高达 890,300 个,"缺口大"是真的;但缺口≠岗位增长。**"教育永远需要人"在 BLS 口径下是错的:需要的是替补,不是扩张。** 另,[G1] 的 NY Fed 数据显示小学教育专业失业率仅 1.2%——**低失业与负增长可以并存**,因为供给端萎缩得同样快。

- **[G15]** 美国公立学校教师年离职率 8%,另有 8% 换校。
  - 口径:分母=2020–21 学年在职的公立学校教师;分子=2021–22 学年已离开教职者。84% 留任原校("stayers")、8% 换校("movers")、8% 离开教职("leavers")。私立学校:82%/6%/12%。
  - 来源:【官方】Taie S. & Lewis L.(Westat)· "Teacher Attrition and Mobility: Results From the 2021–22 Teacher Follow-up Survey to the National Teacher and Principal Survey" · NCES 2024-039,U.S. Dept. of Education,2023 年 12 月 · https://nces.ed.gov/pubs2024/2024039SummaryM.pdf
  - 反证/矛盾测量:该窗口横跨疫情(2020–21 → 2021–22),很可能是**上界**而非常态。这是目前 NTPS/TFS 系列最新一轮,截至 2026 年 7 月未见更新轮次。

- **[G16]** 教师**工资**惩罚 2024 年创纪录 −26.9%,但**总薪酬**惩罚只有 −17.1%(福利优势抵消了约 9.8 个百分点)。
  - 口径:分子/分母=公立中小学教师 vs 其他大学毕业生的**周工资**之比,经回归调整(控制教育、经验、性别、种族、州、婚姻、年龄);样本限于 18–64 岁、每周工作 ≥35 小时、持学士及以上、且**自报工资**者(BLS 推算值被剔除);顶端截尾值用 Pareto 分布均值按性别分别替换。数据源:CPS-ORG(工资)+ NCS/ECEC(福利,含健康与人寿保险、退休计划、工薪税)。年份 2024。作者刻意用"周工资"而非年工资以规避"暑假"问题。1996 年为 −6.1%;州际极差 −10.0%(罗德岛)至 −38.5%(科罗拉多);按性别:男 −36.4%、女 −21.5%。
  - 来源:【研究·倡导型智库,有明确立场】Sylvia Allegretto · "The teacher pay penalty reached a record high in 2024: Three decades of leaving public school teachers behind" · Economic Policy Institute,2025-09-24 · https://files.epi.org/uploads/The-teacher-pay-penalty.pdf
  - 逐字摘引:"Although teachers typically receive better benefits packages than other professionals, this 'benefits advantage' is not sufficiently large to offset the growing wage penalty that teachers face. **In 2024, the teacher total compensation gap was −17.1%.**"
  - **反证/矛盾测量(必须并列)**:AEI 的 Andrew Biggs 与 Heritage 的 Jason Richwine 长期主张相反结论——用认知能力测验(SAT 等)而非学历作为匹配变量,并按更低的贴现率给养老金与退休后医保定价,得出教师**总薪酬高于**私部门可比者。EPI 的反驳是对方"把教师养老金成本算成三倍"。这是一场关于**养老金贴现率**与**匹配变量选择**的长期方法论争议,**双方都有明确立场,不存在中立的一手数字**。来源:【倡导型智库】AEI · "Are Teachers Overpaid? A Response to Critics" https://www.aei.org/articles/are-teachers-overpaid-a-response-to-critics/;EPI 反驳 https://www.epi.org/publication/ib324-public-school-teacher-benefits/。**Round 2 建议:正文写"26.9%"必须同时写"17.1%"和这场争议,否则等于单方采信。**

#### 九、护城河的机制=准入难度(供给侧被人为卡住)

- **[G17]** 美国护理院校 2025 年拒绝了 **92,672 份**合格**申请**(注意:是申请份数,不是申请人数);全职师资空缺 1,588 个,空缺率 7.2%。
  - 口径:分子=学士与研究生层次护理项目拒绝的合格申请份数(一名申请人可投多校,**因此该数字高于实际被拒人数**);年份 2025。师资数据来自另一项调查:AACN "Special Survey on Vacant Faculty Positions"(2025 年 10 月),863 所护理院校、回收率 80.3%,另需 150 个岗位以满足学生需求。学校自述原因:师资不足、临床实习点不足、教室空间、临床带教不足、预算限制。
  - 来源:【行业协会】American Association of Colleges of Nursing(AACN)· "Nursing Faculty Shortage" fact sheet,引 "2025-2026 Enrollment and Graduations in Baccalaureate and Graduate Programs in Nursing" · https://www.aacnnursing.org/news-data/fact-sheets/nursing-faculty-shortage
  - 逐字摘引:"U.S. nursing schools turned away 92,672 qualified applications from baccalaureate and graduate nursing programs in 2025"
  - **矛盾测量(重要)**:媒体普遍报道为"93,176 名申请**人**被拒"(nurse.org 等),**与 AACN 自己的措辞"applications"不一致,且数字也不同**。AACN 作为院校行业协会,在"我们需要更多师资拨款"这件事上有直接利益。
  - 反证:这条与 [G12](HRSA 已把 RN 短缺下修到 2038 年 2%(都会区))并列时会打架:**如果每年有九万多份合格申请被拒、而 HRSA 又说都会区几乎不缺护士,那么"被拒"更可能反映的是护理教育的产能瓶颈+申请热,而不是护士缺口。** 这是本线最该在正文里点破的张力。

- **[G18]** 美国住院医师名额自 1997 年《平衡预算法案》起被 Medicare 冻结在 1996 年水平,近 25 年间仅两次扩增、共 1,200 个;AAMC 预测到 2036 年医师缺口最多 86,000 名。
  - 口径:1997 BBA 对每家教学医院的 Medicare 资助住院医名额设上限,冻结于 1996 年水平。2021 年与 2023 年《综合拨款法案》分别扩增,合计 1,200 个 Medicare 资助名额。
  - 来源:【行业协会】AAMC · GME 相关新闻稿与议题页 · https://www.aamc.org/news/press-releases/new-medicare-supported-gme-residency-positions-expand-health-care-access-physician-workforce;https://aamcaction.org/issues/gme/
  - 反证/矛盾测量:AAMC 是医学院与教学医院的行业协会,其"医师短缺"预测长期被批评为利益相关(扩大 GME 拨款即扩大会员收入)。**独立对照**:HRSA(官方)2038 年医师缺口预测为 141,160 FTE,**高于** AAMC 的 86,000——即在这一项上,官方口径比行业协会更悲观,方向一致。另有同行评审文献主张"美国不需要更多医学院、瓶颈在住院医名额"(PMC12256077),**【未取得全文】**未在本轮取得全文核对。

#### 十、中国侧(口径与美国不可比,不得并列)

- **[G19]** 中国 2024 年末注册护士 585.5 万人,每千人口注册护士 4.16 人;**已提前超额完成"十四五"规划目标(2025 年 550 万人 / 每千人口 3.8 人)**。
  - 口径:分子=年末在册注册护士数(卫生技术人员口径),分母=常住人口。2023 年为 563.7 万人 / 3.40→4.00 人。同期执业(助理)医师 508.2 万人、每千人口 3.61 人,医护比约 1:1.15。发布日 2025-12-01。
  - 来源:【官方】国家卫生健康委员会 · 《2024 年我国卫生健康事业发展统计公报》· 2025-12-01 · https://www.nhc.gov.cn/guihuaxxs/c100133/202512/f1c3a3c617484a27a1a26a468afbaeee/
  - 目标来源:【官方】国家卫生健康委 · 《全国护理事业发展规划(2021–2025 年)》· 2022 年 5 月 · https://www.nhc.gov.cn/yzygj/c100068/202205/5c2dc667011449428655582e19a6c9bd.shtml
  - **中美构念不等价(必须写清)**:①中国"注册护士"包含中专、大专学历取得护士执业资格者,美国 RN 需 ADN/BSN/diploma 且通过 NCLEX,BLS 列其典型入门学历为学士;②分母上中国用常住人口、美国 OEWS 用就业岗位数,**"每千人口护士数"与"RN 就业人数"不是同一类量**;③美国 3,391,000 名 RN / 约 3.4 亿人 ≈ 每千人 10 人,与中国 4.16 人**看似 2.4 倍差距,但相当部分是"谁被算作护士"的定义差异**(中国的护工、养老护理员不计入注册护士,美国的 nursing assistants 也不计入 RN,但两国的分界线位置不同)。**绝不可并列这两个数字。**
  - 反证/矛盾测量:中国的规划目标被提前超额完成,与"中国护士严重短缺"的流行叙事方向相反。未搜到卫健委发布的官方"护士缺口"数字。

- **[G20]** 中国基础教育需求正在断崖式收缩:2024 年小学招生 1,616.63 万人,较 2023 年的 1,877.88 万人**减少 261.25 万人(−13.9%)**;学前教育在园幼儿 2023 年 4,092.98 万(同比 −11.55%)→ 2024 年 3,583.99 万(再降约 −12.4%)。小学专任教师已从 2023 年 665.63 万降至 2024 年 659.01 万。
  - 口径:分子/分母均为教育部年度统计公报口径。"小学招生"含普通小学、小学教学点、九年一贯制小学段、十二年一贯制小学段及其他学校附设小学班。注意 2023 年小学招生曾**同比增长 10.37%**(二胎高峰入学),2024 年的暴跌是出生人口下降传导的开始。同期初中招生 1,754.63 万(2023)→ 1,848.75 万(2024),**仍在增长**(二胎高峰升入初中);普通高中招生 967.80 万 → 1,036.20 万,也在增长。
  - 来源:【官方】中华人民共和国教育部 · 《2024 年全国教育事业发展统计公报》· 2025-06-11 · http://www.moe.gov.cn/jyb_sjzl/sjzl_fztjgb/202506/t20250611_1193760.html;《2023 年全国教育事业发展统计公报》· http://www.moe.gov.cn/jyb_sjzl/sjzl_fztjgb/202410/t20241024_1159002.html
  - **反证/矛盾测量(重要)**:**学段错位**——小学在收缩,初中和高中还在扩张。给 2026 年入学的准大学生(约 2030 年毕业)的含义是:**小学教师岗位已在萎缩,初高中教师岗位约在 2030 年前后见顶后转跌**。这比"教师岗位会减少"的笼统说法精确得多,也是本线对中国读者最有用的一条。
  - 【追不到一手】"多地教师招聘缩减 50%+""竞争比 200:1"等说法仅见于自媒体与境外中文媒体(搜狐、阿波罗网、大纪元),**未追到任何省级教育厅/人社厅的官方招聘计划汇总数据**。已搜角度:教育部+人社部 2025 年中小学幼儿园教师公开招聘通知(该文件只规定时间节点,不含名额)、"特岗计划"通知、省级公务员/事业单位招考公告聚合站。**建议 Round 2 若要用,须逐省抓取教师招聘公告的岗位数,或直接放弃、只用 [G20] 的招生数据做机械推断。**
  - 【追不到一手】中国住院医师规范化培训的**全国年度招收总量**未取得官方数字。已搜角度:国家卫健委人才交流服务中心住培栏目、中国医师协会毕业后医学教育网(ccgme-cmda.cn)、各省市卫健委年度招收通知——只取到单家医院的招生简章与政策文本(本科/科学学位硕博培训 3 年;住培合格的本科临床医师"按临床医学、口腔医学、中医专业学位硕士研究生同等对待"),**无总量**。

---

### 交叉口径问题(Round 2 必须核)

1. **"40% 的护士要跑了"是被折叠过的数字。** 39.9% 里有 21.9pp 是**计划退休**(受访护士中位年龄 50 岁,退休是正常生命周期事件),只有 18.0pp 是非退休离开。且该题在 2024 年被改写(拆分退休/离开选项),NCSBN 自己写了"This question was **altered** in 2024",因此 28.7%(2022)→39.9%(2024)的跳升**混入了工具效应**,不能当作纯粹的态度恶化。另,原文写"a **11.2% increase** over the proportion who reported similar intentions on the 2022 survey (28.7%)"——**11.2 是百分点差,不是相对增幅**,原文措辞本身就有歧义。

2. **意向 ≠ 行为,且两者方向相反。** 意向指标(NCSBN 39.9%)上升,而行为指标(NSI 实际离职率 27.1%→17.6%)和体验指标(NCSBN 倦怠 45.2%→35.4%)**都在改善**。任何只引用意向数字的段落都是选择性取样。

3. **NSI 是猎头公司的销售材料。** "每名护士离职成本 $60,090""全国缺口 158,600"是被媒体引用最多的护士数字,但来自一家护士招聘公司自愿报名的 527 家医院自选样本,报告正文直接嵌入销售电话。必须标注利益相关,不能与 BLS/HRSA 并列为同级证据。

4. **HRSA 两个版本的短缺数字差了三倍以上,且被媒体混用。** 337,970 FTE(2036,2024 年 3 月版,基年 2021 含疫情数据)vs 108,960 FTE(2038,2025 年 12 月版,基年 2023)。目前网上流传的"美国将缺 30 万护士"几乎全部引自已被官方自己取代的旧版。**成文必须用 2025 年 12 月版,并说明下修这件事本身。**

5. **BLS 的 "NP +40.1%" 与 OOH 的 "APRN 合并组 +35%" 是两个不同口径。** 前者是 SOC 29-1171 单一职业(EP Table 1.3),后者是麻醉护士+助产士+NP 三职业合并的 OOH 档案页。年均岗位缺口 32,700 是**合并组**的数字,不能挂在 NP 单独名下。

6. **BLS 增长率与 HRSA 供需充足率会被误当成互相矛盾。** BLS 预测的是**已实现就业**(≈需求侧),HRSA 分别建模供给与需求。NP 可以同时"就业增长 40%"和"供给达需求的 192%"。正文必须解释,否则读者会认为其中一个是错的。

7. **Kleiner & Krueger 的工资溢价有 14% 和 18% 两个流传值。** NBER WP 14979(2009 年 5 月)摘要写 "about 14 percent higher wages";多个二手来源引用发表版(JOLE 2013, Vol.31 No.S1, pp.S173–S202)时写 "about 18 percent"。**【未取得全文】未取得 JOLE 发表版全文核对。** 而无论 14 还是 18,Kleiner 本人 2015 年的综述都以 10–15%(普遍持照)/5–8%(部分州持照)作为更可信区间——**引用 18% 而不给识别问题,是最常见的误用。**

8. **"执照=工资护城河"对护士和教师不成立,但这一句几乎从不被引用。** Kleiner 2015 原文明确把 teachers、nurses 与 cosmetologists 一起划入"影响 murky"。这是本线最容易被漏掉、也最反直觉的一条。

9. **Johnson & Kleiner 的 36% 不适用于护士。** 该估计的识别来自"州专属执照考试 vs 全国统一考试"的对比;RN 用全国统一的 NCLEX,且有 NLC 互认。把 36% 套在护理上是构念错配。

10. **AACN 的 92,672 是"申请份数"不是"申请人数",媒体版本(93,176 名申请人)两处都错。** 一名申请人可投多校,真实被拒人数显著低于该值。且 AACN 是院校行业协会,在争取师资拨款上有直接利益。

11. **RN 年薪与教师年薪的时间口径都不干净,且方向相反。** RN 的 $93,600 由 OEWS 按 2,080 小时折算(护士常为 12 小时轮班,实际工时分布与之偏离);教师的 $62,310–$64,580 对应约 9–10 个月合同,BLS 干脆不为教师发布小时工资。任何 RN vs 教师、或 RN vs 软件工程师的年薪并列都需加口径注。

12. **EPI 的 26.9% 与 17.1% 必须同时出现。** 26.9% 是工资惩罚,17.1% 是含福利的总薪酬惩罚,后者才是可比的经济量。EPI 有明确倡导立场,AEI/Heritage 有相反立场,分歧核心是养老金贴现率与匹配变量(学历 vs 认知测验)。**不存在中立的一手数字,只能并列。**

13. **"教育是抗 AI 护城河"与微软数据直接冲突。** 中小学与特教教师 0.18 > 医疗诊疗执业者 0.13,大学教师 0.31 > 计算机职业 0.29。若正文把"护理+教育"打包成一个"执照护城河"类别,这份数据会直接推翻它。

14. **中美"护士"与"教师短缺"均为不等价构念。** 中国"注册护士"含中专学历者;"每千人口注册护士 4.16"分母为常住人口,与美国 RN 就业人数不同类。中国的"教师编制"与美国的"teacher certification"不是同一制度物(前者是财政编制配额,后者是执业许可),**"考编竞争比"与美国的"teacher shortage"不可对话。**

---

### 未取得/存疑

- **【未取得全文】** HRSA《Nurse Workforce Projections》2025 年 12 月版 PDF(https://bhw.hrsa.gov/sites/default/files/bureau-health-workforce/data-research/nursing-projections-factsheet.pdf)反复返回 403,浏览器亦触发下载而非渲染。已从 HRSA 官网 HTML 摘要页取得 RN 108,960 FTE、LPN 245,950 FTE、非都会区 11%/都会区 2% 三项;**2038 年 NP 与麻醉护士的供需充足率未取得**。Round 2 可试 Workforce Projections Dashboard 导出 CSV。
- **【未取得全文】** Kleiner & Krueger, JOLE 2013, 31(S1): S173–S202 发表版(https://www.journals.uchicago.edu/doi/10.1086/669060)未取得,付费墙。仅取得 NBER WP 14979 摘要(14%)。18% 一值待核。
- **【未取得全文】** Johnson & Kleiner, AEJ:EP 2020, 12(3): 347–73 全文未取得(伊利诺伊大学托管的 PDF 抓取失败)。36% 一值经 AEA 页面确认存在,但 22 个持照职业的名单、以及 RN 是否被归入"州专属考试"组未能核实。
- **【未取得全文】** "The Wrong Fix: Why America Doesn't Need More Medical Schools to Solve the Physician Shortage"(PMC12256077)未取得全文,该文可能是 [G18] 的关键反证(主张瓶颈在住院医名额而非医学院)。
- **【追不到一手】** 中国各省 2025–2026 年中小学教师招聘岗位数的官方汇总。已搜:教育部+人社部 2025 年公开招聘通知(仅规定"4 月底前启动、7 月底前完成",无名额)、特岗计划通知、省级招考公告聚合站。流传的"湖北骤降 52.8%""竞争比 200:1"仅见自媒体与境外中文媒体,**建议不采用**。
- **【追不到一手】** 中国住院医师规范化培训全国年度招收总量。已搜:国家卫健委人才交流服务中心住培栏目、中国医师协会毕业后医学教育网、多省卫健委招收通知——仅得单机构简章与制度文本,无全国总量。
- **【追不到一手】** NCSBN 官方发布的 NLC 成员辖区数(截至 2026 年)。仅取到聚合类媒体口径"43 个辖区(2026 年 4 月)",未取得 NCSBN 带日期的官方计数页。
- **【追不到一手】** 中国官方发布的"护士缺口"数字。已搜卫健委统计公报、护理事业发展规划、政策解读三处,**均无缺口口径**,只有总量目标。流传的中国护士缺口数字疑为行业媒体自估,建议正文不引用。
- **存疑:** NCSBN 2024 调查各州回收率仅约 9–22%(LPN/LVN 最低至加州 9.1%)。虽为随机抽样+加权,但如此低的回收率下,"打算离职者更愿意作答"的无回应偏误无法排除,39.9% 应视为上界。
- **存疑:** NCES 教师离职率 8% 的观测窗口(2020–21 → 2021–22)横跨疫情,截至 2026 年 7 月无更新轮次,可能高估常态。

---

## 线 H:供给过剩机制与历史前科——热门专业是怎么崩的

### 关键论断

#### 一、机制本体:蛛网模型

- **[H1]** 蛛网定理(cobweb theorem)是本线的机制母体:当供给决策必须在价格实现前若干期做出,且行为者用**当期价格**外推**未来价格**,市场不会收敛到均衡,而是围绕均衡震荡;震荡是收敛、发散还是等幅,取决于供给曲线与需求曲线斜率之比。
  - 口径:纯理论模型,原始语境是农产品(生猪、玉米),非劳动力市场。迁移到专业选择时的对应物:"价格"=某专业毕业生起薪/就业率,"生产滞后"=学制(本科 4 年 + 决策提前量)。
  - 来源:【研究】Mordecai Ezekiel · "The Cobweb Theorem" · Quarterly Journal of Economics, Vol. 52, No. 2, Feb. 1938, pp. 255–280 · https://doi.org/10.2307/1881734
  - **【未取得全文】**:未取回 QJE 原文(付费墙),以上为该文公认的核心机制表述,Round 2 若要直接引用 Ezekiel 原话需另取全文。
  - 反证/矛盾测量:蛛网模型的发散/收敛结论**完全依赖供给弹性大于/小于需求弹性**这一参数,不是无条件预言。见 [H5](学生对薪资反应极弱→蛛网被阻尼)与 [H3](移民供给→周期被压缩)。

- **[H2]** Freeman 用蛛网模型实证解释了美国工程师市场的起薪与供给震荡,这是把蛛网从农产品搬到高技能劳动力市场的奠基性工作。
  - 口径:研究对象为美国**新毕业工程师**的起薪与学位供给量;Freeman 另有一篇平行研究针对物理学家市场(1948–1975)。
  - 来源:【研究·同行评审】Richard B. Freeman · "A Cobweb Model of the Supply and Starting Salary of New Engineers" · *ILR Review* (Industrial and Labor Relations Review), Vol. 29, No. 2, January 1976, pp. 236–248 · https://journals.sagepub.com/doi/10.1177/001979397602900204
  - 平行来源:【研究·同行评审】Richard B. Freeman · "Supply and Salary Adjustments to the Changing Science Manpower Market: Physics, 1948–1975" · *American Economic Review*, March 1975。另见其专著 *The Overeducated American* (Academic Press, 1976)。
  - **【未取得全文】**:ILR Review 与 AER 原文均在付费墙后,Harvard Scholar 页面返回 403。**未取得 Freeman 本人给出的周期长度与弹性数值**。Round 2 必须补全,不要在成文中给 Freeman 安上具体数字。

- **[H3]** 美国国家工程院官方报告采纳蛛网模型解释工程师"短缺—过剩"循环,给出**约四年**的周期长度;并明确指出**移民供给(H-1B)把调整期压缩到约一年**,从而显著削平工资波动。
  - 口径:定性模型 + 周期长度估计;"四年"对应供给仅来自美国本土新毕业生的情形,"一年"对应 1990 年后 H-1B 扩张、供给可由已训练成熟的外国工程师即时补充的情形。非计量估计,是模型推演。
  - 来源:【官方/研究】National Academy of Engineering · *Understanding the Educational and Career Pathways of Engineers*, 2018 · Appendix D: "Cobweb Model of the Engineering Labor Market" · https://www.nationalacademies.org/read/25284/chapter/11
  - 逐字摘引:高工资"induces more students to study engineering…Once the additional engineers enter the market, however, the wage drops",四年后出现"talk of a 'glut'"。
  - **这是本线最重要的边界条件**:蛛网周期长度不是常数,它由**供给响应速度**决定。凡是能被移民、转专业、训练营、在职转岗快速补充的岗位,蛛网被压平;凡是供给只能靠本土四年制学位的,蛛网最陡。
  - 反证/矛盾测量:该报告同时引用 Ryoo & Rosen (2004) 作为后续研究;未在本轮取得该文对周期长度的独立估计。

- **[H4]** 有计量研究直接测出"劳动力市场信号 → 完成专业"的滞后期与弹性:**弹性 0.67,最强相关的是三年前(即学生大一时)观察到的工资**。
  - 口径:分子/分母=按细分专业计的完成学位数对该专业对口职业工资溢价的弹性;时间窗 1982–2012;样本为美国全国性调查与行政数据;被解释变量是**完成的专业(completed majors)**而非入学时申报的意向专业。弹性 0.67 = 对口职业工资溢价上升 10%,四年后该专业毕业生数上升约 6.7%。
  - 来源:【研究·同行评审】Mark C. Long, Dan Goldhaber, Nick Huntington-Klein · "Do completed college majors respond to changes in wages?" · *Economics of Education Review*, Vol. 49, 2015, pp. 1–14 · https://www.sciencedirect.com/science/article/abs/pii/S027277571500103X · RePEc 索引:https://ideas.repec.org/a/eee/ecoedu/v49y2015icp1-14.html
  - 异质性(重要):女性、黑人、拉美裔、低测验分数学生**对工资变化的反应显著更弱**。即"追热门"本身有社会分层。
  - **【未取得全文】**:ScienceDirect 返回 403,以上数值来自检索摘要与 RePEc 摘要。Round 2 需核对 0.67 的标准误与"三年前"的具体设定。
  - 反证/矛盾测量:见 [H5]。

- **[H5]** **反证**:另有同行评审研究发现专业选择对预期收入的弹性"**非常低**",非货币因素(对学科的兴趣/禀赋)才是主导。
  - 口径:法国大学体系;识别策略=利用法国商业周期造成的各专业相对回报变动;控制了动态选择(mixture distributions)。结论:弹性显著但极小。
  - 来源:【研究·同行评审】Magali Beffy, Denis Fougère, Arnaud Maurel · "Choosing the Field of Study in Postsecondary Education: Do Expected Earnings Matter?" · *The Review of Economics and Statistics*, Vol. 94, No. 1, 2012, pp. 334–347 · https://direct.mit.edu/rest/article-abstract/94/1/334/57999/Choosing-the-Field-of-Study-in-Postsecondary
  - **构念不等价警告**:H4(美国,0.67,高弹性)与 H5(法国,极低弹性)结论方向相反。二者国别、时间窗、被解释变量(完成专业 vs 申报专业)、识别策略均不同,**绝不可并列**。这本身是本篇的一个诚实结论:学生到底多"追热门",各国各口径答案不一致。
  - **【未取得全文】**:MIT Press 页面仅取到摘要级信息。

---

#### 二、历史崩塌案例

##### 案例 1:法学院泡沫(记录最完整,且已跑完一整轮)

- **[H6]** LSAT 报考量与申请人数的峰值到谷底:LSAT 施测量峰值 **171,514 人次(2009–10 测试年度)**,到 2014 年 2 月较峰值跌 38.5%;申请**件数**从 2010 年的 602,300 件跌到 2013 年的 385,400 件(三年 -36%)。
  - 口径:LSAT 施测**人次**(同一人多次考试重复计),非人头数;申请**件数**非申请**人**数——一人可申多校,两者不可混用。
  - 来源:【商业调查/机构】NCBE · "The State of Law School Admissions: Where Are We in 2014?" · *The Bar Examiner*, June 2014 · https://thebarexaminer.ncbex.org/article/june-2014/the-state-of-law-school-admissions-where-are-we-in-2014/;原始数据出自 LSAC。
  - 反证/矛盾测量:搜索角度=是否有其他机构给出不同的 LSAT 峰值;未发现相冲突的一手数字,171,514 与"2009–10 峰值"在多处一致。

- **[H7]** 法学院一年级(1L)入学人数峰值 **52,404 人(2010 年)**,总 JD 在读峰值 **147,525 人(2010 年)**;此后连跌四年,2013 年秋 1L 跌至不足 40,000 人(较 2012 年再跌 10.8%),回到 1977 年水平。到 2025 年 1L 稳定在约 38,000 人,总 JD 在读较 2010 年峰值低 **18.6%**。
  - 口径:ABA 认证法学院、LSAC 会员校;1L = 首次入学的 JD 一年级学生。**重要口径断裂**:LawHub 明示"2011 年及以后的总 JD 在读数由 LawHub 自行汇总,2011 年前由 ABA 汇总";1L 数据 2010 年起亦由 LawHub 自各校报告汇总。跨 2010/2011 的比较存在汇总主体变更。
  - 来源:【官方/机构】LSAC LawHub · "Law School Enrollment Trends, 1963–2025" · https://www.lawhub.org/trends/enrollment(数据来源标注为 American Bar Association)
  - 逐字摘引(口径警告):"Total JD enrollment totals before 2011 were computed by the ABA, but the totals in 2011 or later were totaled by LawHub."

- **[H8]** 就业崩塌的量化:2013 届毕业生中,仅 **57.0%** 获得"全职、长期、须通过律师资格考试(bar passage required)"的岗位;另有 **10.1%** 为"全职、长期、JD 有优势(JD Advantage)"岗位。
  - 口径:分子=全职且长期的 BPR 岗位人数;分母=当届全体毕业生;测量时点=2014 年 2 月 15 日,即 2013 年春季毕业后约九个月。ABA 强制披露制度下的自报数据。2012 届对应数字为 56.2% 与 9.5%。
  - 来源:【官方】ABA Section of Legal Education and Admissions to the Bar · Class of 2013 employment data(2014 年 4 月发布);经 TaxProf Blog 转述 · https://taxprof.typepad.com/taxprof_blog/2014/04/aba-releases-.html;原始逐校数据库:https://abarequireddisclosures.org/EmploymentOutcomes.aspx
  - **【追不到一手】(部分)**:ABA 官网 americanbar.org 对本工具返回 403,未能取回 ABA 新闻稿原文;abarequireddisclosures.org 为 JS 驱动的逐校查询库,未能在本轮取得全国汇总表。57.0%/10.1% 系经【媒体】转述 ABA 发布。Round 2 必须回到 ABA 原始汇总表核对。

- **[H9]** **蛛网跑完了一整圈**:供给收缩后,法学院就业率大幅修复。2025 届 **82.7%(29,928/36,206)** 进入全职长期须过律考岗位,另 5%(1,815 人)为 JD Advantage,合计 **87.7%**;2024 届合计为 **87.1%(33,931 人)**,2023 届为 85.6%(30,160 人)。
  - 口径:分母=Council 认证法学院全体毕业生(2025 届 36,206 人);测量时点=2026 年 3 月 16 日,毕业后约十个月。2025 届毕业班规模较 2024 届**小 7.0%**——即百分比上升的同时**岗位绝对数在下降**。
  - 来源:【官方/机构】LSAC LawHub · "2025 Graduate Job Outcomes, Aggregated and by School" · https://www.lawhub.org/trends/job-outcomes-vs-schools(标注数据来自 ABA);【官方】ABA · "Law school graduate employment rate for top-tier jobs remains high for the class of 2025", 2026-04 · https://www.americanbar.org/news/abanews/aba-news-archives/2026/04/law-school-employment-rate-remains-high/(本工具取该页返回 403,【未取得全文】)
  - 补充:2025 届中 25.7%(9,298 人)进入 100 名律师以上的大所,3.2%(1,144 人)获联邦法官助理职位;8.8% 为"underemployed"(兼职、短期、在读其他学位或失业求职中)。
  - **口径陷阱(极重要)**:57%(2013)与 87.1%(2024)**不可直接相减**。前者是 BPR 单项,后者是 BPR + JD Advantage 合计。可比构造应为:2013 届 57.0%+10.1% = **67.1%** vs 2024 届 **87.1%**;或 2013 届 BPR 57.0% vs 2025 届 BPR 82.7%。
  - 反证/矛盾测量:【媒体/学者】Derek Muller · "Class of 2025 legal employment outcomes mixed: placement rates improve, but total jobs, large law firm jobs in decline" · https://excessofdemocracy.com/blog/2026/4/class-of-2025-legal-employment-outcomes-mixed-placement-rates-improve-but-total-jobs-large-law-firm-jobs-in-decline —— 明确指出**率在升、量在降**,即修复部分来自分母缩小而非需求扩张。这是对"法学市场已复苏"叙事的关键反证。

- **[H10]** **下一轮蛛网正在起跳**:2026 申请季开局申请**人数同比 +33%**、申请**件数 +27%**;2025 申请季最终以申请人 +18%、申请件 +22% 收官,为十余年来最高。到 2026 年 4 月,已有超 **75,000 人**申请至少一所法学院,而此前四年平均约 59,000 人(+27%)。
  - 口径:LSAC 官方口径,"同一时点对比"(cycle-to-date),非全季终值。LSAT 考生量:2025 年 8 月约 26,000 人(同比 +18%,较 2023 年 8 月 +约 60%)、9 月约 23,000 人(+24%)、10 月约 26,000 人(+16%)。
  - 来源:【官方/机构】LSAC · "Too Soon for Predictions, but the 2026 Admission Cycle Is Starting Strong" · 2025-10-13 · https://www.lsac.org/blog/too-soon-predictions-2026-admission-cycle-starting-strong
  - 逐字摘引(LSAC 自设的限定语,成文必须一并给出):"this is extremely early data",仅代表全季预期总量的"about 15 percent",应"be viewed as broadly directional at best"。
  - 反证/矛盾测量:LSAC 与招生官把激增归因于"especially dynamic political environment"与"uncertain economic climate"(56% 招生官认为政治是主因),**而非法律岗位需求上升**。即:这一轮供给扩张的驱动力可能与就业信号无关,是"避险型"而非"追高型"——这对蛛网机制是一个重要的修正而非确证。

##### 案例 2:石油工程(滞后期最清晰)

- **[H11]** 石油工程学士学位授予数峰值 **2,615 人(2017 年)**,2022 年 894 人,2023 年预期 **655 人**,2024 年预期约 500 人——**较峰值降约 75–81%**;开设该专业的美国院校数从 35 所降至 20 所。
  - 口径:Lloyd Heinze(Texas Tech, Bob L. Herd 石油工程系)年度问卷调查,2023 年有 **25 个项目**回应(上年 27 个)。**样本为回应问卷的项目,非 IPEDS 全口径普查**;地理覆盖以北美为主,仅约占全球 SPE 学生分会会员的 10%。
  - 来源:【商业调查/学会】SPE · *Journal of Petroleum Technology* · "US Petroleum Engineering Graduation Rates Keep Falling, but Oil Execs Are Not Complaining Yet" · 2023-03-01 · https://jpt.spe.org/us-petroleum-engineering-graduation-rates-keep-falling-but-oil-execs-are-not-complaining-yet
  - 口径冲突:另有来源称 2017 年峰值为 **2,550**。两个数字并存,Round 2 需定一个。
  - **【未取得】**:未取得 IPEDS/NCES 官方口径的 petroleum engineering (CIP 14.2501) 学位授予数时序。Heinze 调查虽是业内标准引用源,但它是**行业自报样本**,不是政府普查。成文若用 2,615 必须标注调查性质。

- **[H12]** **滞后期约 2.5 年**:石油工程入学与学位授予受油气价格强烈影响,**变化滞后价格约 2.5 年**。油价从 2014 年 6 月的 105 美元/桶跌至 2016 年 1 月不足 27 美元(-70%+),学位授予峰值出现在 2017 年——即**价格见顶后约三年,学位授予才见顶**。
  - 口径:该滞后估计为业内经验拟合,非发表的计量估计。
  - 来源:【商业调查/学会】SPE JPT · "Petroleum Engineering Enrollment Projected to Drop Sharply" · https://jpt.spe.org/petroleum-engineering-enrollment-projected-drop-sharply
  - **反证/矛盾测量(强)**:同属 SPE JPT 的另一篇 "History Matching of Petroleum Engineering Graduation Rates"(https://jpt.spe.org/history-matching-of-petroleum-engineering-graduation-rates)明确否定价格—入学的简单外推能力。该文引用 Kelkar:"I do not believe that oil prices are going to help us significantly in increasing the enrollment",因为"oil companies are not investing significantly in new production";并强调历史数据"can't predict the next distributions"、"this time is different"。**同一机构的两篇文章对同一机制给出相反的预测力判断**——这正是本篇该讲的方法论教训:蛛网能解释过去,不能外推未来。
  - 补充历史锚点:1984 年石油工程学士毕业生峰值 **1,587 人**(数据源:Heinze;历史部分引自 John C. Calhoun, "A Brief History of a Petroleum Engineering Education in the United States", 1991)。即石油工程**已经跑过不止一轮**蛛网。

##### 案例 3:生物医学博士(唯一有官方机构书面认错的案例)

- **[H13]** **NIH 预算翻倍 → 博士产能暴增的滞后被官方文件直接点名**:生物医学博士授予数的陡增始于 **2004 年**,恰在 NIH 预算翻倍期(**1999–2003**)结束之后;报告将其归因于 **5–7 年的培养周期**。
  - 口径:数据源为 NSF *Survey of Earned Doctorates* (SED);对比组为行为与社会科学、化学博士,同期基本持平。
  - 来源:【官方】NIH Advisory Committee to the Director · *Biomedical Research Workforce Working Group Report* · 2012-06-14 · https://acd.od.nih.gov/documents/reports/Biomedical_research_wgreport.pdf(p.17, Figure 1)
  - 逐字摘引:"The steep increase in the number of biomedical PhDs awarded began in 2004, just after the end of the doubling of the NIH budget (1999-2003). Given a 5-7 year training period, this illustrates a close relationship between the size of the NIH budget and the number of biomedical PhD slots."
  - 共同主席:Shirley Tilghman(普林斯顿大学校长)、Sally Rockey(NIH 副主任)。

- **[H14]** **官方白纸黑字承认过剩**:该报告写明每年培养的未来科学家数量"**远超过**"学术界、政府与产业界研究型岗位的数量。
  - 口径:定性判断,报告未给出"过剩倍数"。
  - 来源:同 [H13],p.10("Staff Scientists"节)
  - 逐字摘引:"This creates a system in which a large number of future scientists are being produced each year, well in excess of the number of research-oriented jobs in academia, government and industry."
  - 另一处(p.14)对当时的就业前景判断:"the numbers of positions available for biomedical PhDs that take advantage of their long training are less than the number of PhDs produced each year. As a consequence their career path is marked by uncertainty."

- **[H15]** 进入终身教职轨道的博士比例从 **1993 年约 34% 降至 2012 年约 26%**;同期非终身轨教职比例相对稳定但绝对数增长;进入产业与政府的比例基本不变,**增长的是"不做研究的科学相关职业"和"不需要研究生训练的职业"**。生物医学博士整体失业率"very low"。
  - 口径:主数据源为 NSF *Survey of Doctorate Recipients* (SDR)。报告自陈 SDR 的两个缺陷:**不含外国培养的博士**(而这是生物医学劳动力中占比上升的群体),且**数据滞后**(委员会当时能拿到的最新数据是 2008 年)。
  - 来源:同 [H13],p.7(Executive Summary)、p.17
  - 逐字摘引:"Although the vast majority of people holding biomedical PhDs are employed (i.e. unemployment is very low), the proportion of PhDs that move into tenured or tenure-track faculty positions has declined from ~34 percent in 1993 to ~26 percent today."
  - **这是本篇最重要的口径示范**:"失业率极低"与"职业前景恶化"**同时为真**。失业率是错的指标,**对口率/学非所用率**才是。
  - 补充(训练成本):2001 届生物医学博士,取得博士学位的中位年龄 32 岁,**开始终身教职轨道岗位的中位年龄 37 岁**;化学博士对应为 30 岁与 33 岁。2011 财年公立研究机构生物医学助理教授平均起薪约 **$68,000**,化学 $69,000,临床与健康 $79,000,经济学 **超过 $100,000**(数据源:Oklahoma State University 公立研究机构薪资调查)。

- **[H16]** **两份官方报告互相矛盾——这是本线最有价值的"专家也会看错"证据**:1998 年美国国家研究委员会(NRC)报告已判定博士产能超过岗位并建议**限制增长**;该报告发布**恰在 NIH 预算翻倍之前**。而 2011 年 NRC 报告(Chalkley 主持)却基于"低失业率"和"未来十年科学就业将大幅增长"的模型,判定 NRSA 岗位数**够用、应维持**。2012 年 NIH ACD 工作组直接推翻了 2011 年的判断。
  - 口径:三份文件均为官方/半官方委员会报告。
  - 来源:【官方/研究】National Research Council · *Trends in the Early Careers of Life Scientists*(Shirley Tilghman 主持), National Academy Press, 1998 · https://www.nap.edu/catalog.php?record_id=6244;2011 年 NRC 研究(Roger Chalkley 主持);均经 [H13] 报告 p.14–15 转述。
  - 逐字摘引(1998 报告的结论,经 2012 报告转述):"the level of PhD production in 1998 exceeded the availability of jobs in academe, government and industry where they can use their training as independent scientists";1998 委员会认为"the absence of suitable employment has led to a crisis of expectations that could discourage the best students from entering the field"。
  - 逐字摘引(2012 报告对 1998 报告时机的评论):"It is notable that this report was released just before the doubling of the NIH budget, which may have affected the perception of the urgency of its recommendations."
  - 逐字摘引(2012 报告对 2011 报告的反驳):"the data gathered by the ACD working group do not indicate such growth in employment opportunities."

---

#### 三、中国对应物

- **[H17]** 中国教育部已把"撤销/停招"制度化,且**撤销与停招的规模已大幅超过新增**:2024 年度全国高校新增专业点 **1,839 个**、调整学位授予门类或修业年限专业点 **157 个**、停招专业点 **2,220 个**、撤销专业点 **1,428 个**;全国本科专业布点总数 **6.28 万个**;《普通高等学校本科专业目录(2025 年)》共 **845 种**专业,本年度新增 **29 种**新专业。
  - 口径:统计单位是"**专业点**"(校×专业),不是专业种数,也不是招生人数或学生数。"撤销"≠已有学生失学(通常为停止新招生后自然消化)。时间窗为 2024 年度审批批次,2025 年 4 月 22 日公布。
  - 来源:【官方】中华人民共和国教育部 · 《教育部关于公布2024年度普通高等学校本科专业备案和审批结果及〈普通高等学校本科专业目录(2025年)〉的通知》/ 高等教育司负责人答记者问 · 2025-04-22 · http://www.moe.gov.cn/srcsite/A08/moe_1034/s4930/202504/t20250422_1188239.html · http://www.moe.gov.cn/jyb_xwfb/s271/202504/t20250422_1188246.html · 中国政府网转载:https://www.gov.cn/zhengce/202504/content_7020385.htm
  - 逐字摘引:"撤销、停招专业点数大幅超过增设专业点数,专业结构不断优化";"强化专业建设与就业互促机制,不断增强高等教育与经济社会发展的契合度"。
  - **构念差异警告(中美不等价)**:美国没有对应机制。美国高校专业设置不需联邦审批,IPEDS 只做事后统计;中国的"备案/审批/撤销"是**行政准入**。因此中国的"布点数"是**政策变量**,美国的"学位授予数"是**市场结果**。两者不能当作同一条供给曲线并列。

- **[H18]** 2024 年度撤销数量最多的本科专业 Top5:**信息管理与信息系统(38)、市场营销(34)、信息与计算科学(27)、网络工程(26)、产品设计(24)**。长期看,信息管理与信息系统连续多年居撤销榜首,近五年累计撤销约 160 个专业点;公共事业管理、信息与计算科学、市场营销累计撤销均超 100 个点。
  - 口径:由媒体依据教育部逐校名单**自行汇总计数**,教育部本身**不发布**"撤销最多专业排行"。不同媒体的统计年份窗口不一致(有"2018–2022 五年"口径给出信息管理与信息系统 100 所、公共事业管理 97 所、服装与服饰设计 70、产品设计 66、信息与计算科学 65),与上述"近五年 160 个点"口径不同。
  - 来源:【媒体】中国教育在线 · "这些专业,正在'消失'" · 2024-07-22 · https://news.eol.cn/guancha/202407/t20240722_2625290.shtml;【媒体】每日经济新闻 · 2024-07-13 · https://www.nbd.com.cn/articles/2024-07-13/3466593.html
  - **注意 [H18] 的一个反直觉点**:被撤最多的不是文科,而是**信息管理与信息系统、信息与计算科学、网络工程**这些"IT 相关"专业。这直接打脸"选 IT 相关就安全"的叙事——**专业名字带不带"信息/网络/计算"与是否被淘汰无关**。
  - 反证/矛盾测量:搜索角度=教育部是否发布过官方的撤销专业排行;未发现,教育部只发布逐校名单附件。所有排名均为第三方计数,**Round 2 必须回到教育部附件名单自行核对,或明确标注为媒体计数**。

- **[H19]** 【商业调查】麦可思"红牌专业"提供了中国最长的连续预警序列:**法学**自 2010 年该榜创设以来长期在榜,与**绘画**在近五年榜单中**连续五年**上榜;2025 届本科红牌专业为**公共事业管理、音乐表演、绘画、法学、美术学**(其中艺术学门类占 3 个);2017 年本科红牌为历史学、音乐表演、生物技术、法学、美术学、生物工程;2010–2011 年本科红牌包含动画、法学、生物技术、生物科学与工程、数学与应用数学、体育教育、生物工程、**计算机科学与技术**、英语、国际经济与贸易。
  - 口径:麦可思自定义,"红牌"= 就业落实率、薪资和就业满意度综合较低,且市场需求减少或增长缓慢的专业;榜单基于**前三年综合数据**。麦可思研究院是**商业调查机构**,样本为其自建毕业生调查(具体样本量在本轮取得的转述中未披露),**非政府统计**;"就业落实率"是麦可思口径,与教育部"毕业去向落实率"不必然一致。
  - 来源:【商业调查】麦可思研究院 · 《2025年中国本科生就业报告》(就业蓝皮书) · 2025-07-02;经【媒体】澎湃新闻转述 · https://www.thepaper.cn/newsDetail_forward_31066577;历史序列经【媒体】人民日报社《民生周刊》· https://www.msweekly.com/show.html?id=35488 与中国教育在线 · https://news.eol.cn/yaowen/202007/t20200709_1737460.shtml
  - **【未取得全文】**:麦可思官网 mycos.net.cn 连接超时,未取得蓝皮书原文的样本量、抽样方法与红牌判定阈值。**这是利益相关方的商业产品(麦可思同时向高校售卖就业质量评估服务),成文必须标明分级并给出这一利益关系。**
  - **极重要的历史反讽**:2010–2011 年麦可思红牌名单里赫然有"**计算机科学与技术**"。这是本篇最有力的一句话论据——十五年前被中国就业报告打红牌的专业,正是今天最热的专业。它同时证明两件事:(a) 蛛网确实会反转;(b) **任何一年的红/绿牌榜都不构成对四年后的预测**。

- **[H20]** **中国 AI 专业布点曲线**:2018 年度批次(2019 年 3 月公布)首批 **35 所**高校获批"人工智能"(专业代码 080717T);2019 年度批次新增约 **179–180 所**,累计约 **214–215 所**;至 2024 年度批次(2025 年 4 月公布)新增 **91 所**,**累计 626 所**普通高校备案人工智能本科专业,2025 年招生。
  - 口径:统计单位为"备案/审批该专业的高校数(专业点)",非招生人数、非在校生数。首批 35 所出自教育部 2018 年度审批结果。
  - 来源:【官方】教育部 · 《关于公布2018年度普通高等学校本科专业备案和审批结果的通知》· 2019-03-29 · http://www.moe.gov.cn/srcsite/A08/moe_1034/s4930/201903/t20190329_376012.html;【官方】教育部 2024 年度结果(见 [H17]);【媒体】汇总:https://www.163.com/dy/article/JTTJT7L50532N2UB.html(2025-04-24)
  - **口径冲突待核**:同一批次的新增校数有"179 所"与"180 所"两种说法,累计数相应为 214 或 215。Round 2 需回教育部 2019 年度附件名单点数。
  - 同批次参照(2018 年度):机器人工程 101 所、智能科学与技术 96 所、数据科学与大数据技术 203 所、大数据管理与应用 25 所、网络空间安全 25 所、物联网工程 14 所。

- **[H21]** **"数据科学与大数据技术"提供了一条完整的、已经走完上升段并显著衰减的布点浪峰**——这是预判 AI 专业布点走向的最佳同构参照。逐年新增备案高校数:**2015 年 3 → 2016 年 32 → 2017 年 250(峰值) → 2018 年 203 → 2019 年 137 → 2020 年 62 → 2021 年 40 → 2022 年 30 → 2023 年 33**,累计 **775 所**。
  - 口径:新增备案高校数(增量,非存量);2015–2023 累计。约占全国普通高校总数的 60%。
  - 来源:【媒体】网易 · "2024全国775所高校数据科学与大数据技术专业教育教学综合实力排行榜" · https://c.m.163.com/news/a/J2MAIN5G0532N2UB.html(依据教育部历年备案名单汇总)
  - **【追不到一手】**:该逐年序列为第三方依教育部历年附件名单汇总,教育部未发布此时序。搜索角度:教育部官网、中国教育在线、阳光高考平台;未找到官方发布的分专业布点时序表。Round 2 若要用这条曲线,须逐年回教育部 9 份年度通知附件自行计数,或明确标注为媒体汇总。
  - **机制读法(可检验、不预测)**:布点浪峰在开设第 2 年见顶,随后 6 年衰减 87%。**布点数的一阶导(新增校数)比存量更早反转**。对 AI 专业,可检验信号是:教育部 2025、2026 年度批次的 AI 新增校数是否已低于 2024 年度的 91 所。

---

#### 四、当下的 AI/CS 扩招:是不是同一部剧

- **[H22]** **美国计算机专业已经跑完两轮完整蛛网,幅度都在 35–42%**。计算机与信息科学学士学位授予数:**1985–86 年 42,337(第一轮峰) → 1993–94 年 24,527(谷,-42.1%) → 2003–04 年 59,488(第二轮峰) → 2008–09 年 37,992(谷,-36.1%) → 2021–22 年 108,503**。
  - 口径:美国全部授予学位的高等教育机构;学科为"computer and information sciences"(CIP 11 全类,**范围大于 computer science 本身**,含信息系统、IT 等);学年制;2021–22 为 provisional。硕士 2021–22 为 51,338,博士 2,790。
  - 来源:【官方】U.S. Department of Education, NCES · *Digest of Education Statistics 2023*, Table 325.35 · "Degrees in computer and information sciences conferred by postsecondary institutions, by level of degree and sex of student: Academic years 1964-65 through 2021-22" · https://nces.ed.gov/programs/digest/d23/tables/dt23_325.35.asp(来源注:"Earned Degrees Conferred" 与 IPEDS Fall 2022)
  - **滞后期实测**:互联网泡沫破裂在 2000 年 3 月,而 CS 学位授予数峰值出现在 **2003–04 学年**,即**冲击后约 4 年**——与 [H3] 国家工程院给出的四年周期、[H4] 给出的"最相关的是三年前工资"高度一致。三条独立证据互相印证:**本科专业的供给对市场信号的滞后是 3–4 年**。
  - 反证/矛盾测量:2008–09 谷底之后的这一轮上升(37,992 → 108,503,+186%)**远超**前两轮峰值,幅度是史无前例的。这意味着若第三轮回撤按前两轮 36–42% 的比例发生,绝对量的调整规模将远大于历史。但也可能反映 CIP 11 口径本身的扩张(数据科学、信息科学等新专业被归入)。**成文不得把 108,503 与 42,337 当作同质可比。**

- **[H23]** **第三轮回撤的领先指标已经出现(截至 2026 年 6 月)**:2025 年度 CRA Taulbee 调查显示,学士学位产出仍创纪录(41,858 个 CS 学士学位),但**新申报主修学生数同比 -13%**、**本科总在读 -4%**;硕士**总在读 -26%**、新录取 -10%;博士产出 1,909 个(五年 +51%)但**新入学 -15%**,为 2020–2025 年间首次下降。
  - 口径:CRA Taulbee 调查,样本为**美国与加拿大的博士授予单位**(PhD-granting departments),**不是全美普查**;百分比变化为"两年均回应单位"的纵向可比子样本(longitudinal cohort);学位数据主要覆盖 2024–25 学年,在读数据反映 2025–26 学年。
  - 来源:【商业调查/学会】Computing Research Association · "CRA Update: New CRA Taulbee Survey Findings Show Record Degree Production Alongside a Cooling Enrollment Pipeline" · 2026-06 · https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
  - 逐字摘引:"These downturns imply that degree counts will plateau and decline in the coming years.";描述为"a computing education landscape that remains historically strong as it pertains to degrees produced but is showing leading indicators of a coming plateau."
  - 转折点定位:2024 年度 Taulbee(2023–24 学年)新生入学还是 **+9.9%**、总在读 +6.8%;2025 年度调查转为本科在读 **-3.1%**;2026 年发布的调查再转为新申报主修 -13%。**拐点发生在 2024–2025 学年之间。**
  - **【口径陷阱·必须核】**:NCES 口径 2021–22 年 CS 学士 **108,503** vs CRA 口径 2025 年 **41,858**,相差 2.6 倍。二者**不是同一个总体**(NCES=全美所有院校 + CIP 11 全类;CRA=北美博士授予系 + 较窄的 CS 定义)。**绝不可把这两个数放在同一张时序图上。**

- **[H24]** 需求侧官方对照:BLS 预测软件开发人员、软件质量保证分析师与测试员 2024–2034 年就业增长 **15%**("much faster than average"),年均岗位空缺约 **129,200 个**,且明确指出多数空缺来自**替换需求**(转岗、退休),而非净增长。
  - 口径:BLS Employment Projections 2024–2034;"openings"= 净增长 + 替换需求,**不是净新增岗位**;职业口径(software developers/QA/testers),与学位口径(CIP 11)不对应。BLS 明示增长驱动含"the continued expansion of software development for artificial intelligence (AI), Internet of Things (IoT), robotics"。
  - 来源:【官方】U.S. Bureau of Labor Statistics · *Occupational Outlook Handbook*, "Software Developers, Quality Assurance Analysts, and Testers" · https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm;新闻稿:https://www.bls.gov/news.release/pdf/ecopro.pdf
  - **方法论警告**:BLS 预测是**外推模型**,不是对 AI 冲击的独立判断;BLS 自身在历次技术变革中的预测误差需在 Round 2 单独核查。**不得把 BLS 预测当作"AI 不会替代程序员"的证据。**
  - 反证:[H16] 已经给出一个先例——2011 年 NRC 也是基于"低失业率 + 模型预测就业将增长"判定供给够用,一年后被 NIH 工作组用实际数据推翻。

- **[H25]** 【工作论文·未过审】有 2025 年的理论工作直接把蛛网机制套用到 AI 时代的教育投资上,提出"AI 驱动的教育陷阱"。
  - 口径:纯理论模型(4 个命题),**无实证检验、未经同行评审**的 arXiv 预印本。
  - 来源:【研究·工作论文】Andrew J. Peterson · "Training for Obsolescence? The AI-Driven Education Trap" · arXiv:2508.19625v2 · 2025 年 8 月 · https://arxiv.org/pdf/2508.19625
  - 核心主张:当 AI 掌握某项技能的速度快于学生习得该技能所需的年限时,个体理性地**减少**人力资本投资,产生协调失败与经济体层面的生产率拖累。
  - **使用建议:仅作为"有人在严肃建模这个问题"的存在性证据,不得引用其命题作为对现实的判断。** 逐字摘引待 Round 2 从 PDF 原文核实(本轮摘引经工具转述,已下载 PDF 于 `/Users/cissychen/.claude/projects/-Users-cissychen-Desktop-repos/8f82afa8-649c-4c17-b39f-b18b26c6bb77/tool-results/webfetch-1784944069929-1m9i2o.pdf`)。

---

#### 五、反证:热门专业**没有**崩的案例,以及蛛网的适用边界

- **[H26]** **护理是最清晰的"没崩"案例,而原因恰恰证明了蛛网的边界条件:当供给被执照与培养产能硬约束时,蛛网无法过冲。** 2024–2025 学年美国护理院校因**师资不足**拒收了 **80,162 份**合格申请;护理院校报告 **1,588 个**全职教师岗位空缺;超过三分之一的护理教师预计未来数年退休。
  - 口径:分子=被拒的**合格申请件数**(非申请人数,一人可申多校);统计主体为 AACN 成员院校自报。**AACN(美国护理学院协会)是行业协会、利益相关方**,该数字被用于游说增加护理教育经费,存在方向性动机。主要瓶颈按 AACN 自陈为:临床实习点不足、师资、带教老师、教室空间、预算削减。
  - 来源:【商业调查/行业协会】American Association of Colleges of Nursing · Faculty Shortage Fact Sheet · https://www.aacnnursing.org/Portals/0/PDFs/Fact-Sheets/Faculty-Shortage-Factsheet.pdf;经【媒体】Becker's Hospital Review 转述 · https://www.beckershospitalreview.com/nursing/66-000-qualified-nursing-applications-turned-down-amid-faculty-shortages-aacn.html(注:Becker's 标题用的是 66,000,与 80,162 分属不同年度,**两个数字不可混用**)
  - **机制结论(本线最可迁移的判据之一)**:蛛网过冲需要**供给能自由扩张**。凡满足以下任一条件,过冲被抑制——(a) 执业需执照且执照供给受限;(b) 培养需临床/实训席位等物理产能;(c) 师资本身即瓶颈。反之,凡是**开一个专业只需要教室和 PPT** 的领域(法学、市场营销、信息管理、以及大部分 AI/数据科学本科专业),供给可以在 1–2 年内翻倍,过冲几乎必然。
  - **【未取得】**:未取得 HRSA(美国卫生资源与服务管理局,官方)的护理人力供需预测原文。Round 2 应补 HRSA National Center for Health Workforce Analysis 的官方口径,以替代/校验 AACN 的利益相关方口径。
  - 补充反证的反证:检索到的商业来源提到疫情后医院曾出现招聘冻结,即护理在局部时段也出现"人才瓶颈而非真实过剩"之外的需求侧波动。该说法来源均为【媒体/商业】,未取得一手,**不采用**。

- **[H27]** **第二类边界:移民/横向流入**。见 [H3]——H-1B 扩张把工程师市场的调整期从约 4 年压缩到约 1 年。推论:一个岗位越容易由**海外已训练成熟的人力**或**转行者(训练营、硕士转轨)**填补,其蛛网周期越短、幅度越小,但**在位者的工资保护也越弱**。这对中国准大学生的含义与美国相反(中国不是移民接收方),**是一个必须分国讨论、不可并列的机制**。
  - 反证/矛盾测量:搜索角度=是否有研究测量中国专业选择的蛛网效应或滞后期;**本轮未找到任何一手的中国计量研究**。这是本线最大的空白,见"未取得/存疑"。

---

### 交叉口径问题

Round 2 必须逐条核对的陷阱:

1. **法学就业率 57% vs 87%——分子构成完全不同。** 57.0%(2013 届)是"全职长期须过律考(BPR)"单项;87.1%(2024 届)/87.7%(2025 届)是 **BPR + JD Advantage 合计**。可比构造:2013 届 67.1%(57.0+10.1) vs 2024 届 87.1%;或 BPR 对 BPR:57.0%(2013) vs 82.7%(2025)。**媒体极易把 57% 与 87% 直接相减得出"回升 30 个百分点",这是错的。**

2. **法学"率升量降"。** 2025 届率(87.7%)高于 2024 届(87.1%),但毕业班规模小 7.0%,大所岗位与总岗位数**在下降**。用率讲"法学复苏"会误导;必须同时给分子绝对数。

3. **CS 学位数两套口径差 2.6 倍。** NCES 2021–22 年 108,503(全美所有院校,CIP 11 全类)vs CRA Taulbee 2025 年 41,858(北美博士授予系,窄 CS 定义)。**不可同图、不可相除。** 且 CRA 的百分比变动全部基于"两年均回应"的子样本,与其绝对数不同底。

4. **LSAT"人次"vs 申请"件数"vs 申请"人数"。** 171,514 是施测人次(重复计);602,300 是申请件数;75,000+ 是申请人数。三者常被混用。2026 季申请人 +33% 与申请件 +27% 也是两个不同分母。

5. **LSAC 自设限定语被媒体剥掉。** "+33%"是 cycle-to-date、仅覆盖全季约 15% 的量,LSAC 原文说只能"broadly directional at best";多家媒体标题直接写成"申请激增 33%"。成文必须带回限定语。

6. **石油工程 2017 峰值:2,615 还是 2,550?** 两个数并存于 SPE 系统内。且该数据是 **Heinze 问卷调查(2023 年仅 25 个项目回应)**,不是 IPEDS 普查;回应项目数逐年变化本身会造成伪趋势。需补 IPEDS CIP 14.2501 官方序列。

7. **石油工程"滞后 2.5 年"的地位。** 这是业内经验值,非发表的计量估计;且**同一机构(SPE JPT)的另一篇文章明确否定该规律的预测力**。不可写成"研究表明滞后 2.5 年"。

8. **中国"撤销专业排行"无官方版本。** 教育部只发逐校名单附件,所有 Top5 排名(信息管理与信息系统 38 个等)均为媒体自行计数,且不同媒体的年份窗口不同("近五年 160 个点" vs "2018–2022 共 100 所")。需回附件核。

9. **中国"数据科学与大数据技术"逐年布点序列(3/32/250/203/137/62/40/30/33)是媒体汇总,非官方发布。** 这条曲线在本篇分量很重,必须回教育部 9 份年度通知附件逐年点数,或明确标注为媒体计数。

10. **中国 AI 布点 2019 年度批次:179 所还是 180 所?累计 214 还是 215?** 需回教育部附件点数。

11. **麦可思"红牌"是商业机构自定义指标,且麦可思向高校售卖就业评估服务(利益相关方)。** "就业落实率"与教育部"毕业去向落实率"是否同一口径未经证实;样本量与判定阈值本轮**未取得**。不可与教育部数字并列。

12. **中美构念不等价(本线核心)。** 中国的"专业布点数"是**行政审批变量**(政府可直接开关),美国的"学位授予数"是**市场结果变量**(政府不审批专业设置)。中国 626 所 AI 专业与美国 108,503 个 CS 学位**不是同一类量**,不能并列成"中美 AI 人才供给对比"。

13. **专业选择弹性:0.67(美,Long et al. 2015)vs "非常低"(法,Beffy et al. 2012)。** 国别、时间窗、被解释变量(完成专业 vs 申报专业)、识别策略均不同,方向相反。不可择一而用而不提另一个。

14. **"失业率低"≠"没有过剩"。** NIH 报告同时给出"生物医学博士失业率 very low"与"产出远超研究型岗位数"。这是全篇最该强调的口径教训:**衡量专业过剩要用对口率/学非所用率,不是失业率。**

---

### 未取得/存疑

**付费墙 / 未取得全文(存在性已确认,内容不得臆测):**
- Ezekiel (1938) QJE 原文 — 未取回,H1 的机制表述属公认转述,非逐字引用。
- Freeman (1976) *ILR Review* 29(2):236–248 原文 — SagePub 付费墙,Harvard Scholar 页 403。**Freeman 本人给出的周期长度与弹性数值本轮完全未取得**,成文不得为其编派具体数字。
- Freeman (1975) AER 物理学家市场论文 — 仅确认存在。
- Freeman, *The Overeducated American* (1976) 专著 — 仅确认存在,未取得任何具体数据。
- Long, Goldhaber & Huntington-Klein (2015) — ScienceDirect 403,0.67 与"三年前"来自检索摘要与 RePEc,未见标准误与设定细节。
- Beffy, Fougère & Maurel (2012) REStat 94(1):334–347 — 仅取得摘要级信息,"非常低"未量化。
- Ryoo & Rosen (2004) 工程师市场研究 — 仅经国家工程院报告转引,未取得原文。
- NRC (1998) *Trends in the Early Careers of Life Scientists* 与 NRC (2011) Chalkley 报告 — 均仅经 NIH 2012 报告转引,**未取得两份原文**。[H16] 的"官方内部矛盾"叙事分量很重,Round 2 应取原文。

**站点拒绝访问(需换路径):**
- americanbar.org 全站对本工具返回 403 — ABA 关于 2013 届、2024 届、2025 届的**新闻稿原文均未取得**,相关数字经 LawHub / TaxProf / 检索摘要转述。**[H8] 的 57.0%/10.1% 目前只有【媒体】转述层级,是本线证据链最薄的一环。**
- abarequireddisclosures.org — JS 驱动的逐校查询库,未取得全国汇总表。
- mycos.net.cn(麦可思官网)— 连接超时,蓝皮书原文的样本量/方法/阈值未取得。

**完全未取得、Round 2 需新开检索:**
- **IPEDS/NCES 口径的 petroleum engineering (CIP 14.2501) 学位授予数时序** — 目前石油工程全案仅靠 SPE 的行业自报调查,证据等级偏低。
- **HRSA National Center for Health Workforce Analysis 的护理供需官方预测** — [H26] 目前只有 AACN(利益相关方)口径。
- **NSF SED 的生物医学博士授予数逐年绝对值** — 本轮只从 NIH 报告图 1 读到趋势描述,无逐年数字。
- **中国任何一手的专业选择滞后期/蛛网效应计量研究** — 本轮检索**零结果**。搜索角度:蛛网模型 + 专业选择、扩招 + 就业滞后、教育部 + 专业调整实证。若 Round 2 仍找不到,成文必须明说"中国侧缺乏公开的计量估计,滞后期只能由布点曲线形态间接推断"。
- **中国"法学扩招 → 就业恶化"的一手时序**(法学专业布点数/招生数的历史峰谷)— 目前只有麦可思红牌这一商业口径,**没有教育部口径的法学布点或招生时序**。这是中国侧最值得补的一块,因为它是与美国法学院案例唯一可做机制对照(非数字对照)的素材。
- **教育部 2025 年度本科专业备案审批结果** — 2025 年 8 月有公示(https://www.edu.cn/rd/gao_xiao_cheng_guo/ssgx/202508/t20250815_2685680.shtml),本轮未取。**这是检验 [H21] 所提可检验信号(AI 新增校数是否已低于 91 所)的关键数据,截至 2026-07 应已正式公布,Round 2 优先补。**

**方法论存疑(需在成文中明确处理,而非回避):**
- 全线论据都是**事后解释**。[H12] 中 SPE 自家文章明确指出历史拟合"can't predict the next distributions"、"this time is different"。本篇若用蛛网论证 AI 专业,**必须同时呈现这一自我否证**,并把结论限定为"可检验信号"(新增布点数一阶导、CRA 新申报主修数、教育部年度批次 AI 新增校数)而非预测。
- [H10] 揭示的驱动力问题:2026 法学申请激增的自陈主因是政治与经济不确定性,**不是法律岗位需求上升**。这说明专业选择的供给冲击可以由与就业信号无关的因素驱动,蛛网模型对此**无解释力**。这一点削弱了把蛛网当作通用判据的做法,应诚实写入。

---
