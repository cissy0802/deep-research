# 02b · 锁定口径清单 — 后半(G36–G59)

> 由 Round 2 后半 72 票(4 批 × 3 席 × 6 组)合并。三席不一致时取最严格者:任何一席发现的口径问题都成立,除非另一席明确指出该发现本身有误。
> **成文时必须逐条对照本文件,不得回退到 01 的原始表述。**
> 票型:CORRECTED 66 / HOLDS 4 / REFUTED 2。合并后判决:HOLDS 0 / CORRECTED 22 / REFUTED 2(G52、G57)。
> 凡标题带「⚠️」者,至少一席判 REFUTED,必须读完「不得这样写」再动笔。

---

## [G36] 纽约联储分专业劳动力市场数据:护理的低就业率是全表最低,但「工资恰好相等」是取整效应

- **判决**:CORRECTED(3/3 票 CORRECTED,无 REFUTED)
- **锁定表述**:
  - 据纽约联储《Labor Market Outcomes of College Graduates by Major》(2026-02-04 发布,基于 **2024 年 ACS**,73 个专业 + 1 行全体合并值;失业率与低就业率的口径为 **22–27 岁、持学士及以上学位**的近期毕业生,**含硕博**;中位工资口径为**仅持学士学位的全职工作者**;mid-career 指 35–45 岁):护理专业的低就业率(underemployment)为 **12.8%,是 73 个专业中最低的一个**,第二名航空航天工程为 14.7%。
  - 护理的失业率为 **2.1%,在 73 个专业中排第 10**,并不突出。**「确定性」只能挂在低就业率上,挂在失业率上会被数据打脸。**
  - 教育类专业的失业率占据全表最低三名:**特殊教育 0.7%(第 1)、其他教育类 1.1%(第 2)、小学教育 1.2%(第 3)**。
  - 护理的 35–45 岁中位工资 **$87,000,与全体大学毕业生(35–45 岁)的合并中位数同为 $87,000**;该列全部 74 行均按千元取整,新闻学同样是 $87,000。护理的中期工资在 73 个专业中排第 32 位。
  - 早期→中期涨幅:护理 $70,000→$87,000(+24%);全体 $58,000→$87,000(+50%);计算机科学 $87,000→$120,000(+38%);小学教育 $45,000→$55,000(+22%)。
- **证据分级**:多源证实(三席各自独立下载同一份 CSV 逐格核对,数值全部一致;口径定义由二席回到 NY Fed 说明页/JS bundle 核到,一席因 403 未取到)
- **不得这样写**:
  - ❌「护理的中位工资**恰好等于**全体专业的中位数」——两处错。一是 Overall 行是**所有学士及以上毕业生的合并中位数**,不是 73 个专业中位数的中位数(后者实算为 **$82,000**);二是该列按千元取整,「恰好」「巧合」这类暗示精确等式的措辞不可用,只能写「同为 $87,000(均按千元取整)」。且这个「相等」随口径年份摆动:2023 ACS 版为护理 84,000 vs 全体 83,000,2022 ACS 版两者同为 80,000。
  - ❌「小学教育失业率 1.18%,**全表最低之一**」——是全表**第 3 低**,前两名也是教育类。直接写「教育类包揽失业率最低三名」更强也更准。
  - ❌ 把「仅学士」这个限定挂在失业率/低就业率上——NY Fed FAQ 明确低就业率的分母**含研究生与专业学位持有者**(护理 30.3% 持研究生学位、小学教育 50.6%)。「仅学士」只适用于工资列。
  - ❌ 不标数据年份——该 CSV 在 2026-03-03 前后被整体替换过一次;且 NY Fed 页面挂有告示「Due to the suspension of necessary data, The Labor Market for Recent College Graduates has not been updated as scheduled.(October 31, 2025)」。引用须写明「2024 年数据,常规更新已暂停」。
- **利益相关**:无(联邦储备银行的公共数据产品,无商业利益)
- **待 Round 3**:否(三席独立复算一致,属多源证实)

---

## [G37] 职业执照:覆盖率、工资溢价与跨州流动惩罚

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **覆盖率(必须分两个口径)**:白宫经济顾问委员会 2015 年报告逐字——受**州级**执照法覆盖的劳动力占比,由 1950 年代初的不足 5% 升至 **2008 年的 25%**(约五倍);**再计入地方与联邦执照后为 29%**。该 29% 来自 NBER WP 14979(Kleiner & Krueger,2009)所依据的 2008 年 **Westat 电话调查,样本仅约 2,500 人**(2006 年那次为 Gallup)。同一份白宫报告给出的官方大样本对照是 Census SIPP(n≈58,000,2012 年秋):18–64 岁民用就业者中约 **20% 持执照**、28% 持执照或证书。
  - **工资溢价(必须以阶梯呈现,不可取单值)**:Kleiner & Krueger 的**已发表版**(JOLE 2013, 31(2 Pt 2): S173–S202)为「about **18%** higher wages」,这是**未控制教育与培训的横截面相关**;其 NBER 工作论文版(WP 14979, 2009-05)为 **14%**,是同一研究的早期版本、**不是第二个独立结果**;Kleiner 本人 2015 年 Hamilton Project 报告已退到「**10 to 15 percent**」(限 **hourly earnings**、限「universally licensed occupation」);识别最干净的一组——仅在部分州持照的职业——只有「about **5 to 8 percent**」。
  - **跨州流动惩罚(必须用发表版)**:Johnson & Kleiner 的**已发表版**(AEJ: Economic Policy 12(3): 347–373, 2020)偏好设定——限定长距离迁移者、对照组为全国统考持照职业——为「**7 percent less likely** to move between states」;不做长距离限定的朴素估计为 −58%,NBER 工作论文版(w24107, 2017-12)摘要报的「**36 percent** lower relative to members of other occupations」对照组是「其他所有职业」。
  - **落点(本条对文章最有用的一半)**:该论文 Table 1 亲自把 **注册护士/执业护士(RN/LPN)归入 quasi-national(全国统考)组**,把 **中小学教师归入 state-specific(州专属考试)组**;分职业结果中「Pharmacists and teachers have the lowest relative rates, at −47 and −39 percent」。即**流动惩罚豁免护士、正中教师靶心**。
  - **执照对护士/教师的工资效应**:Kleiner 原文逐字为「the impact of licensing on earnings is **murky**, with some studies finding small effects and others finding none」——是「证据不明确」,不是「不成立」。
  - **执照的价格效应**:白宫报告「In 9 of the **11 studies** we reviewed…significantly higher prices accompanied stricter licensing」;质量则是「quality improvements in only **2 out of the 12 studies** reviewed」。
  - **护士执业权限制的受害者**:Kleiner, Marier, Park & Wing(NBER WP 19906)摘要逐字——只允许医师开管制药物「is associated with a **reduction in nurse practitioner wages**, and increases in physician wages」,同时使幼儿体检价格上涨 3–16%。**要主张「损害 NP 自己」,必须挂这条工资结论,不能挂消费者价格结论。**
  - **NLC**:NCSBN 官方口径「43 jurisdictions」已立法,其中关岛、马萨诸塞、美属维尔京群岛为「Enacted, Awaiting Implementation」——写「43 个辖区已立法,约 40 个已实施」。
- **证据分级**:多源证实(三席各自下载 PDF 逐字核对);其中 18% 一项为**单源已核**(发表版摘要,一席 403 未取到、二席取到)
- **数字定版**:
  - **36% vs 7% → 文章用 7%**,并写明「工作论文版报 36%,对照组是其他所有职业;经同行评审的发表版偏好估计为 7%,对照组是全国统考持照职业,系数小五倍」。理由:发表版经同行评审、且作者自陈朴素估计被自选择污染。引 36% 而不说明它是最粗的估计,正是本文批评的那种引用方式。
  - **14% / 18% / 10–15% / 5–8% → 须并列呈现(阶梯式)**,不得取单值。文章主引 **18%(JOLE 2013 发表版,未控教育培训)**,紧跟 **10–15%(Kleiner 本人 2015 年控制教育技能后的口径)** 与 **5–8%(部分州持照职业,识别最干净)**。理由:「由批评方自己一路下调」比外部质疑更有说服力,而取任何单值都会丢掉这个信息。**14% 不再单独使用**(它只是 18% 的工作论文早期版)。
  - **NP 价格 3–16% / 6.0 与 16.0 / 10% → 三处并存,必须指明取自哪一处**。文章用白宫报告正文的「3 to 16 percent」并加注:白宫自家 Research Appendix Table 2 把同一篇 Kleiner et al.(2014)记为 6.0(中度监管)与 16.0(高度监管),**没有「3」**;Kleiner 2015 年报告对同一结果写作「10 percent」。**不得把「3」当作独立数据点。**
- **不得这样写**:
  - ❌「需持**州**执照才能合法从业的劳动力占比升至 2008 年的约 29%」——29% 是州+地方+联邦的「完全持照」口径,州级口径是 25%。
  - ❌「执照工资溢价对护士和教师**恰恰不成立**」——原文是 murky(未定),不是为零。
  - ❌ 引用 Kleiner 那句 murky 段时省略「**by limiting entry or making it more difficult for an individual to be hired for a job in another state**」——这半句把医生/牙医/律师的「large effects」限定在**进入门槛与跨州受雇**上,删掉后读者会误以为原文在做「医生律师有工资溢价 vs 护士教师没有」的同口径对比。三席全部点名这一处。
  - ❌「幅度 3–16%」被写成「11 项价格研究的幅度范围」——3–16% 只指 NP 与幼儿体检价格**这一项**。
  - ❌「**11 项价格研究**」被读作 11 篇独立论文——Appendix Table 2 的 11 行估计只来自 **5 篇论文**(Kleiner et al. 2014、Kleiner & Kudrle 2000、Liang & Ogur 1987、Conrad & Sheldon 1982、Shepard 1978),其中 4 篇是 1978–2000 年的**牙科**研究。质量计票的 12/2 则完全对得上,可放心用。
  - ❌「限制 NP 独立执业权的执照规则,**损害的是 NP 自己**」——挂在幼儿体检涨价那句上是推论方向错误(那句讲的是消费者付更高价)。改挂 NBER WP 19906 的 NP 工资结论。
  - ❌「NLC 覆盖 43 州所以护士流动无碍」——DePasquale & Stange(NBER w22344, 2016)用 180 万护士数据发现 NLC 的采纳对护士劳动供给与地理流动性**没有可测效果**,这个推论本身缺乏实证支撑。
  - ❌ 把南卡 12.4% / 爱荷华 33.3% 的州际极差当官方统计——它出自 Kleiner & Vorotnikov(2015)所用的 **Harris 商业民调自报调查**。
- **利益相关**:Kleiner 是执照制度的主要批评者,同时是 Hamilton Project(Brookings)报告作者与白宫 2015 年报告的主要引用来源;两份报告均属**政策倡导文本**,其「12 项中仅 2 项」「9/11」两组计票均出自其学术圈自选的文献集。须随数字标注。反向立场的独立证据:Law & Marks(UC Riverside WP 201439, 2014)用各州分时立法准实验发现 RN 执照有小幅正向工资效应(每多一年执照制度使实际工资涨近 $100,10 年约 $1,000),落在 Kleiner 所谓「small effects」一侧。
- **待 Round 3**:**是**。① JOLE 2013 发表版的「18%」只有一席取到一手(另一席被 Cloudflare 拦截),需反证搜索席确认发表版摘要逐字;② Law & Marks 是唯一一篇支持「护士执照有正向溢价」的研究,需方法学审计席评估其准实验设计与显著性(原文自述仅在其中一个设定下显著)。

---

## [G38] BLS 2024–2034 预测:教师岗位负增长与「缺口≠增长」

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **必须用的收窄版标题**:在 BLS 职业大类口径下,增长最快的是**医疗支持类 +12.4%**(2024 年中位年薪 **$37,180**),计算机与数学类 +10.1% 被 BLS 自己称为「the **second** fastest」;医疗**执业与技术类**只有 **+7.2%**。全经济体平均 +3.1%。绝对增量上,两个医疗大类合计 **+1,715,200** 个岗位,计算机与数学类只有 +545,600。
  - 四个 K-12 教师职业 2024–2034 全部负增长(2024 年 5 月中位年薪 / 2024 年就业 / 变动率 / 变动量):幼儿园与小学教师 $62,310 / 1,539,800 / −2% / −29,800;初中教师 $62,970 / 633,700 / −2% / −12,400;高中教师 $64,580 / 1,094,500 / −2% / −17,800;特教教师 $64,270 / 559,500 / −1% / −7,700。
  - **学前教师是例外**:$37,120 / 555,100 / **+4%(As fast as average)/ +22,900**。
  - 「缺口≠增长」的一手句(OOH 幼儿园与小学教师页逐字):「Despite declining employment, about **103,800 openings**…are projected each year, on average, over the decade. **All of those openings** are expected to result from the need to replace workers who transfer to other occupations or exit the labor force, **such as to retire**.」(初中 40,500、高中 66,200、特教 37,800)
  - 教育指导与图书馆大类(SOC 25-0000)整体:9,813,200 → 9,875,400,**+62,200,+0.6%(微增,非下降)**,年均缺口 **890,300**,2024 年 5 月中位年薪 $59,220;OOH 原句为「grow **slower than the average**」「about 890,300 openings…**largely** due to the need to replace workers who leave the occupations permanently」。
  - 可承重的机制表述(BLS 口径,不越界):「1,539,800 的存量每年产生 103,800 个替补缺口(约 6.7% 的年周转),替补流量本身就足以吸收新毕业生。」
- **证据分级**:多源证实(三席分别从 Wayback id_ 快照取新闻稿全文、就业矩阵 xlsx 与 EP Table 1.1/1.2 逐格复算,数字全部一致)
- **不得这样写**:
  - ❌「**BLS 数字不支持『医疗是最高增长赛道』**」——三席一致判为**可被同一份新闻稿一句原文推翻**的标题。同一份新闻稿逐字写着「Healthcare and social assistance is projected to have the **largest job growth** and be the **fastest growing industry sector**(+8.4 percent)」,而职业大类层面最快的正是医疗支持类 +12.4%。**行业口径下医疗既最大又最快**,只有医疗执业与技术类 +7.2% 慢于计算机与数学类。必须改成上面的收窄版。
  - ❌「教师三个学段**全部**负增长」后紧跟学前 $37,120 的低薪——学前教师是 +4%,是唯一正增长的学段。只引其低薪却不说它在增长,对准大学生是有方向性影响的遗漏。
  - ❌「教育与图书馆大类整体年均缺口高达 890,300 个」被读作大类在萎缩——该大类是 +0.6% 微增。
  - ❌「890,300 个缺口**全部来自替补**」——大类页原文是「**largely** due to」;「All of those openings…」只对幼儿园与小学教师那 103,800 个成立。
  - ❌「$62,310 是小学教师中位薪」——它是 OOH「Kindergarten and Elementary School Teachers」**合并职业**的中位数;同页分项为小学(非特教)$62,340、幼儿园(非特教)$61,430。
  - ❌⚠️「低失业与负增长并存,**因为供给端萎缩得同样快**」——**三席全部未能回到一手证实**(title2.ed.gov 取不到 / 重定向循环),BLS 本身只给替补需求这一个解释。且两个数字口径不同:1.18% 是 ACS 中 22–27 岁「小学教育**专业**」毕业生的失业率,−2% 是 BLS 对该**职业**的就业变动预测。另一同样合理的解释是:教师执照把进入端拦住,拿了教育学位却没进课堂的人转入其他工作,被记为低就业(小学教育 16.2%)而非失业。**必须降格为待证假设并明说未验证,或整句删去因果部分。**
- **利益相关**:无(BLS 官方统计)
- **待 Round 3**:**是**。「师范生供给萎缩」这一因果链条无任何一手支撑,需反证搜索席检索 Title II / IPEDS 师范培养完成人数序列;若取不到,该因果句在成文中必须删除而非降级。

---

## [G39] 护士执业者(NP)供需:BLS 增速 vs HRSA 过剩预测

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **BLS(2024–2034,已实现就业口径,近似需求侧)**:护士执业者(SOC 29-1171)320,400 → 448,800,**+128,400,+40.1%**,2024 年中位年薪 **$129,210**,入职学历硕士,**单职业年均缺口 29,500**;在 BLS「增长最快职业」表中**排第 3**(前两名为风电运维技师 +49.9%、光伏安装工 +42.1%)。对照:软件开发者 +15.8%、中位 **$133,080**(高于 NP);医师助理 +20.4%、$133,260;家庭健康与个人护理助理 +17.0%、$34,900;注册护士 +**4.9%**(OOH 页显示为「5% (Faster than average)」)、年均缺口 189,100、中位 $93,600。
  - **HRSA(必须统一用 2025 年 12 月版《Nurse Workforce Projections, 2023-2038》)**:NP 供给充足率 **2028 年 126%(供给 501,010 / 需求 399,200)、2033 年 152%(638,990 / 420,250)、2038 年 175%(供给 766,260 FTE / 需求 437,330 FTE)**;麻醉护士 102% / 108% / **113%**;助产士 104% / 123% / **140%**。逐字句(两版均原样出现):「At the national level, the supply of nurse practitioners (NPs) is projected to exceed demand over the projection period; however, distribution remains the most important issue.」
  - **「30 万护士缺口」确系引自已被取代的旧版**:2024-03 版(2021–2036)称 2036 年 RN 短缺 9%(**337,970** FTE);2025-12 版(2023–2038)称 2038 年短缺 3%(**108,960** FTE),下修约三倍;而 LPN 反向扩大:99,070(2036 旧版)→ **245,950**(2038 新版)。非都会区 vs 都会区 RN 短缺 **11% vs 2%(2038)**、18% vs 4%(2033)、24% vs 5%(2028)。
  - **医师(2025-12 版《Physician Workforce: Projections, 2023-2038》)**:2038 年全国缺口 **141,160 FTE**(供给 1,010,060 / 需求 1,151,220,充足率 88%);地理差距的官方配对是**全科别口径**:「42% in nonmetro areas (a **shortage of 58%**), compared to **95% in metro areas (a shortage of 5%)** in 2038」。初级保健医师 2038 年全国缺口 **70,610 FTE**(HRSA 官网另注,无都会/非都会拆分)。
  - **口径辨析(原稿写法正确,建议原样保留)**:BLS 测的是已实现就业(近似需求侧),HRSA 分别建模供给与需求,两者不必然矛盾;OOH 的年均缺口 32,700 属于「麻醉护士+助产士+NP」**合并组**,不能挂在 NP 名下——NP 单职业是 29,500。
- **证据分级**:多源证实(BLS 部分三席逐格一致;HRSA 新旧两版 PDF 三席分别经 Wayback id_ 快照或镜像取得,数字一致)
- **不得这样写**:
  - ❌「NP 2036 年充足率 **192%**(2026 年 132%、2031 年 164%),麻醉护士 118%、助产士 139%」——这是 **2024 年 3 月旧版(基年 2021、含疫情数据)**的数字。三席一致指出:文章 C 段刚批评「流传的 30 万缺口引自已被取代的旧版」,B 段自己却仍在引同一份旧版,**同一篇文章自相矛盾**。必须统一到 2025-12 版:**175%**。可补一句「上一版对 2036 年的估计是 192%,新版虽下调但仍是显著过剩」——这样反而更有力。
  - ❌「医师 2038 年缺口 141,160 名(**非都会区初级保健 39%**,都会区 5%)」——**39% 在 HRSA 医师 factsheet 中查无此数**(一席全文 grep「39」「primary care」零命中);且把「非都会区初级保健」与「都会区全科别」并列是苹果比橘子。改用 58% vs 5%(全科别)反而更强。
  - ❌ 不说明两版基年差异——2021(含疫情)vs 2023,需求侧模型也做过修订,192%→175% 既有数据更新也有模型更新,**不能单纯读成「NP 过剩变轻了」**。
- **利益相关**:HRSA 与 BLS 均为联邦机构;HRSA 的供需模型是政策规划工具,其修订本身即证明模型结果对基年高度敏感,引用时须标「模型预测」而非「观测」。
- **待 Round 3**:否(新旧两版一手 PDF 三席均取得,数字交叉一致)

---

## [G40] 护士离职:意向指标 vs 行为指标

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **意向端(NCSBN 2024 全国护士人力普查,刊于 Journal of Nursing Regulation 16(1) Suppl, S1–S88, 2025-04)**:计划在未来 5 年内退休或离开护理的 RN 占比 2020 年 22.1% → 2022 年 28.7% → **2024 年 39.9%**(其中「计划退休」21.9% + 「计划离开护理」18.0%)。表注逐字:「This question was introduced in the 2020 survey and **modified in 2024** to offer separate options for those who plan to retire, and those who plan to leave nursing.」——**问法改过,序列不可直接连读**。另:原文把 39.9−28.7 = 11.2 个**百分点**差写成「a 11.2% increase」,措辞有歧义。**分母限定**:该题只向「actively employed in nursing」者提问,且**未在夏威夷施测**。RN 与 LPN/LVN 中位年龄均 **50 岁**。倦怠(每天或每周数次)由 2022 年 45.2% 降至 2024 年 **35.4%**;每天感到情绪耗竭由 23.9% 降至 **18.9%**。
  - **行为端(2026 NSI National Health Care Retention & RN Staffing Report)**:医院 RN 实际离职率 **CY2021 峰值 27.1% → CY2022 22.5% → CY2023 18.4% → CY2024 16.4% → CY2025 17.6%**。**CY2025 是回升,不是继续下降**:报告逐字「RN turnover is recorded at 17.6%, **a 1.2% increase**」「directly responsible for the bump in hospital turnover」「**RN retirement is on the rise** and frequently cited as why nurses voluntarily resigned」;医院全员离职率 18.5% 亦为「a nominal **increase** from CY24(18.3%)」。NSI 同时公布第二套口径(只统计全职/兼职离职):CY21–CY25 为 22.5 / 18.2 / 15.0 / 13.5 / **14.6%**——**引哪个是方法学选择,必须说明**。
  - **RN 空缺率 8.6%(2026 报告)不可与往年比较**:脚注逐字「*The RN Vacancy Rate in previous reports were based on the average of the range selected. Beginning 2026, NSI collected data on RN FTEs filled & vacant, and modified the formula…」。历年 AVERAGE 为 2022 17.0% / 2023 15.7% / 2024 9.9% / 2025 9.6% / 2026 *8.6%。
  - **可承重的合并结论**:「意向指标(39.9%)与行为指标在 2021–2024 方向相反——离职率从 27.1% 一路降到 16.4%;但 CY2025 行为指标已回升 1.2 个百分点至 17.6%,且回升的驱动因素(退休上升)恰与意向数据中 21.9pp『计划退休』那一半同向。」
  - **两个指标不是同一群人**:NCSBN 是全美执照持有者抽样调查(意向,含非医院、非在职渠道),NSI 是 527 家自愿报名的急症医院雇主基准调查(行为)。做对比时必须写明。
- **证据分级**:多源证实(NCSBN 全文与 NSI PDF 三席分别经 Wayback/浏览器渲染/直接下载取得,数字逐格一致)
- **不得这样写**:
  - ❌「NSI 报告的医院 RN 实际离职率从 **CY2022 峰值 27.1%** 降至 CY2025 17.6%」——**年份错(峰值是 CY2021)+ 方向错(CY2025 是回升)**。三席全部点名,一席明言「否则文章会在最关键的一处把趋势讲反」。
  - ❌「各州回收率仅约 **9–22%**(加州 RN 14.0%、LPN/LVN **最低 9.1%**)」——这只覆盖了**邮寄问卷臂**(24 个辖区;合计 RN 16.9%、LPN/LVN 13.7%;州级区间 8.2%–22.3%)。另有**电邮问卷臂**(18 个辖区)合计 **RN 9.7%、LPN/LVN 7.4%**,州级最低为**新罕布什尔 LPN/LVN 2.2%**、华盛顿特区 2.9%、佛州 RN 5.8%;还有 **10 个辖区根本没做问卷**(直接取 Nursys e-Notify 自注册记录),夏威夷用州内部调查。9.1% 是**加州的** LPN/LVN 回收率,不是全表最低。正确表述:「三种模式混合抽样,邮寄臂合计 RN 16.9%、电邮臂合计 RN 9.7%(个别州低至 2.2%),另有 10 个辖区为行政/自注册记录。」——回收率比原稿说的还要差,「39.9% 应视为上界」这个判断因此**更站得住**。
- **利益相关**:**NSI 是护士招聘与留任服务商**,报告执行摘要里直接印着销售话术:「the average cost of turnover for a bedside RN is **$60,090**」「NSI estimates the current national RN shortage at **158,600**」「**Every RN hired saves $66,081.** An NSI contract to replace 20 travel nurses could save your institution $1,322,000… **Contact Michael Colosi at (717) 575-7817** to learn how NSI can improve your bottom line.」方法段自述「acute care hospitals were **invited to participate**…**527 hospitals from forty states** responded」——**自愿报名、非概率抽样**。$60,090 与 158,600 均为 NSI 基于自家问卷的自估,**属厂商口径,方向可参考、程度不承重**。
- **待 Round 3**:否(两份一手件三席均取得并逐格核对)

---

## [G41] 微软 AI 适用度评分:教育与医疗不在同一阵营

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - 据 Tomlinson, Jaffe, Wang, Counts & Suri《Working with AI: Measuring the Applicability of Generative AI to Occupations》(arXiv:2507.07935,v1 2025-07-10 / v6 2025-12-22,**截至 2026-07 仍是未经同行评审的预印本**,arXiv 页无 journal-ref),SOC 次要组的 AI 适用度评分为:数学科学 0.32、**大学教师 0.31**、计算机 0.29、**中小学与特教教师 0.18**、律师 0.17、**其他医疗执业与技术 0.16**、医疗诊疗执业者 0.13、卫生技师 0.10、其他医疗支持 0.06、职业/物理治疗助理 0.05、**家庭健康助理与护理助理 0.04**。
  - **唯一扛得住的读法**:「教育类的 AI 适用度落在知识工作区间(中小学 0.18、大学 0.31),与计算机(0.29)、数学(0.32)、律师(0.17)同档;而医疗诊疗(0.13)与医疗照护类(0.04–0.06)明显更低。**护理与教育不属于同一阵营**——量级差 3–7 倍。」
  - **数据口径**:**2024 年 1 月 1 日至 9 月 30 日**(九个月)、**仅限美国境内**的匿名化 Bing Copilot 对话;20 万条由**两个各 10 万条的样本**构成——主数据集是约 10 万条**均匀抽样**,辅助数据集是 10 万条**从获得过点赞/点踩反馈的对话中抽样**(反馈自选择样本,仅用于估计完成率,**不是代表性样本**);产品为**免费消费级** Bing Copilot,非企业版;就业权重取自 **OEWS 2023**(不是 2024),人口学与工资另用 CPS 2024。
  - **评分构造(原稿的推测成立)**:表注逐字「Score is the **employment-weighted average** AI applicability score…**averaging the mean of the user goal and AI action scores**」,即 a = (a_user + a_AI)/2;每一侧本身由 IWA 层的 coverage(频率阈值 ≥0.05%)、completion、scope 三项聚合后按 O*NET 任务权重加权,**不是原始使用份额**。
  - **必须紧跟的限定语(作者原文)**:「It is tempting to conclude that occupations that have high AI action applicability score will be automated and thus experience job or wage loss…**This would be a mistake**, as downstream consequences of new technologies are very hard to predict and often counterintuitive.」以及「The use of a frequency threshold means **relative comparisons are more meaningful than absolute score values**.」
  - **另一条必须写的限定**:该分数衡量的是「Copilot 用户实际做的活动」与「某职业 O*NET 中间工作活动」的重叠度——**论文并不知道用户本人的职业**。0.18 不代表教师在用 AI,也不代表教师会被替代。
- **证据分级**:**厂商口径**(AI 厂商用自家产品日志测算自家产品对职业的适用度)+ 单源已核(三席均下载 v6 PDF 逐格核对 Table 1,十个评分全部命中)
- **不得这样写**:
  - ❌「中小学教师(0.18)**高于**律师(0.17)」「大学教师(0.31)**高于**计算机职业(0.29)」——差距只有 0.01 与 0.02,论文**未报告任何置信区间或标准误**,且作者自己写明「relative comparisons are more meaningful than absolute score values」。三席一致判为不可承重的精确排序。放弃这两条排序,论点丝毫不减。
  - ❌ 把医疗写成齐平的一档——同表中「其他医疗执业与技术」为 **0.16**,与教师的 0.18 只差 0.02。用「0.13 vs 0.18」讲两个阵营显得比数据本身干净。
  - ❌「数据窗口为 2024 年 Copilot 对话」——是 2024-01-01 至 2024-09-30 的九个月、仅限美国。
  - ❌「基于 20 万条**随机**对话」——会高估代表性,须说明 10 万 + 10 万的构成。
  - ❌「中小学教师」当作 SOC 25-2000 的完整名称——该次要组含**学前与幼儿园**教师。
  - ❌ 把 Nature Computational Science 上的《AI and the democratization of knowledge work》(Daepp, Tomlinson, Counts 等,2026-05,Perspective)当成本文的发表版——**不是同一篇**。
- **利益相关**:作者五人**全部为 Microsoft Research**,数据为微软自有产品日志(IRB #11028),聚合指标开源于 github.com/microsoft/working-with-ai。该论文发布后被大量媒体改写为「微软列出 AI 将消灭的 40 种职业」,作者被迫另发博文澄清「our study does not draw any conclusions about jobs being eliminated; in the paper, we explicitly cautioned against using our findings to make that conclusion.」(该博文一席未能取到一手,建议**直接引论文正文的「This would be a mistake」段**,不依赖博客转述。)这段媒体误读史本身就是文章可用的素材。
- **待 Round 3**:**是**。该文是未过审预印本、且为厂商自测,是本篇「AI 暴露度」论述的唯一定量支点。需方法学审计席评估:频率阈值 0.05% 对小职业的截断效应、免费消费级产品用户与在职专业人士的选择性、以及 O*NET IWA 映射的主观性。**若被否决,只能作为方向性提示,不得承重。**

---

## [G42] Dale & Krueger:名校溢价与「学费溢价」的真实命运

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - Dale & Krueger 的**早期版**(NBER WP 7322, 1999-08;发表为 QJE 117(4): 1491–1527, 2002)摘要逐字:进入更具选择性院校的学生,与被同等院校录取但选择就读次优院校者相比**收入并无更高**;但**院校平均学费**与收入显著正相关;且名校回报「appears to be greater for students from more **disadvantaged family backgrounds**」。
  - **更新版**(NBER WP 17159, 2011;发表为 Journal of Human Resources 49(2): 323–358, 2014,题《Estimating the Effects of College Characteristics over the Career Using Administrative Earnings Data》)用 **SSA 行政收入记录**重估后,结论段逐字:「the returns to other college characteristics (**the Barron's Index and net tuition**) are substantial in the basic model…but **small and never statistically distinguishable from zero in the self-revelation model**」;并明说与 2002 年那版「are **partly a contrast**」——2002 版 self-revelation 模型中 net tuition 系数为 **.058 (.018) 显著**,同批学生改用 1995 年自报收入降至 **.041 (.038) 不显著**,再换 SSA 行政收入降至 **.033 (.046)**,整个 1983–2007 期间该系数「generally between 0 and .02(never greater than .033)」。
  - **仍然成立的异质性**:剔除 HBCU 后 1989 队列的少数族裔学生,SAT 高 100 分对应 **12%**、进入更高 Barron's 等级对应 **14%** 的收入回报(即使在 self-revelation 模型中);父母平均受教育年限 12 年者,SAT 高 200 分对应 2007 年收入高 **5.2%**;父母平均 16 年者「there was **virtually no return**」。
  - **样本限定(必须连作者自辩一起引)**:WP 17159 逐字「the analysis does not pertain to a nationally representative sample of schools, as the sample is derived from the **27 colleges and universities** in the C&B dataset, the majority of which are very selective」;但**同段紧接着**写「estimates…based on the C&B dataset were similar to — indeed, slightly higher than — those based on a nationally representative dataset, the **National Longitudinal Study (NLS) of the High School Class of 1972**」,且 DK 2002 在 NLS-72 上跑 self-revelation 模型同样得到不显著结果。
- **证据分级**:多源证实(三席各自下载 WP 7322 与 WP 17159 全文 pdftotext 逐字核对,结论一致)
- **不得这样写**:
  - ❌「**学费(办学支出)溢价从未消失,消失的只是同学平均 SAT 溢价**」——**三席一致判为方向完全相反,必须删改**。学费溢价恰恰是 2011/2014 版用 SSA 行政数据消掉的那一个,作者自己做了 reconciliation。正确表述:「学费溢价只存在于 2002 年那版(自报收入);换成行政收入长周期数据后,它与 SAT 溢价一起归零。」
  - ❌ 把 net tuition 译作「**办学支出**」——它是「标价学费减平均助学金」,是**价格**。
  - ❌「C&B 的 **30 所**院校」挂在那句 nationally-representative caveat 上——该 caveat 出自 WP 17159,原句是 **27 所**;30 所是 DK 1999/2002 的分析样本(C&B 库共 34 所)。
  - ❌ 只引「不覆盖重点 vs 普通的大跨度对比」而删掉作者的 NLS-72 自辩——这是**反向截断**,作者已用全国代表性数据做过稳健性检验。
  - ❌ 把 WP 7322 的摘要标成「QJE 2002 摘要」——QJE 117(4) 的**已发表摘要完全不含学费那句**,且末句是「Children from **low-income families**, however, earned more if they attended selective colleges.」(低收入家庭),不是「更弱势家庭背景」。
  - ⚠️ 著录陷阱:NBER 官网 w17159 页的 published-version 字段**本身是错的**(题名写错,并把 QJE 卷号误植为 v107,实为 117(4): 1491–1527)。以期刊页为准。
- **利益相关**:无
- **待 Round 3**:否

---

## [G43] Chetty-Deming-Friedman:名校对上尾有效、对中位数无效

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - 据 Chetty, Deming & Friedman,NBER WP 31492(**2023 年 7 月首发、2025 年 8 月修订**;**已发表于 Quarterly Journal of Economics 141(1): 51–145, 2026 年 2 月**):就读 **Ivy-Plus 院校**(定义逐字为 Ivy League + Stanford + MIT + Duke + Chicago,共 12 所)而非「the average flagship public college」,使学生进入收入分布**前 1% 的概率提高 50%**、进入精英研究生院的概率「nearly doubles」、进入名企就业的概率「almost triples」(**正文对应处写作 nearly twice / 2.5 times,两套措辞并存,勿混引**)。
  - **空结果**:「The impact of Ivy-Plus admission on reaching the **top quartile** of the distribution is **small and statistically insignificant**」;matriculation design 下对**对数收入**的影响 modest,「consistent with the findings of Dale and Krueger (2002), whose primary outcome is log earnings」。
  - **均值效应**:使 33 岁**均值**收入提高 **$101,000**(反事实均值 $143,000,即约 +71%),原文以「As a result of these **upper-tail impacts**」领起。$143,000 是**按测验分数重新加权后**的反事实均值(未加权的旗舰公立均值为 $110,000,Ivy-Plus 均值 $244,000)。
  - **对照组的真实构造**:「the outside option (college O), which we define as the average flagship public college **in our college-specific sample (i.e., the 9 colleges listed in Appendix Table 1)**」——是作者自有样本中的 **9 所**旗舰公立,不是全美旗舰公立的平均。
  - **与 DK 分歧的来源(两处,不是一处)**:原句逐字「not because of differences in research design but rather because our richer data allow us to **directly identify college's fixed effects (rather than using proxies for quality such as test scores)** **and** **isolate impacts on upper tail outcomes**」。即:① DK 用「同学平均 SAT」做院校质量代理,CDF 直接识别院校固定效应;② 结果变量选对数收入还是上尾概率。作者另写「we find **little association** between students' average outcomes and the mean test scores of the college they choose to attend, the proxy for college quality used by Dale and Krueger and others」。
- **证据分级**:多源证实(三席各自下载 WP PDF 逐字核对;发表信息由二席经 Oxford Academic / EconPapers 独立确认)
- **数字定版**:**用发表版的 50%**。2023 年 7 月首发版摘要该处为 **60%**,2025-08 修订后下调为 50%;读者若去翻 2023 版会看到不同的数字,**必须写明「经修订由 +60% 下调为 +50%」**。$101,000 / $143,000 / top quartile 空结果 / research design 四段在首发版中即已存在,未变。
- **不得这样写**:
  - ❌「NBER WP 31492, 2023-07」并按未过审工作论文引用——截至 2026-07 该文**早已发表于 QJE 141(1): 51–145 (2026-02)**。以工作论文身份引用会让读者低估其地位。(一席仍按未过审处理,已被另两席的期刊页核实推翻。)
  - ❌「分歧是**结果变量口径**,不是研究设计」——只说对了一半,漏掉作者给出的第一条理由(直接估院校固定效应 vs 用同学平均 SAT 做代理)。
  - ❌「名校对**中位数**几乎没用」——论文没有直接报中位数效应。按原文说「对进入前 25% 的概率无显著影响、对对数收入影响不大」。
  - ❌ 把 $101,000 / $143,000 与「对中位数几乎没用」并置而不点明前者是**均值**——读者会算出矛盾。
  - ❌ 把 $143,000 说成旗舰公立的实际均值——它是重新加权后的反事实均值。
- **利益相关**:无(Opportunity Insights 团队,数据为国税与院校录取行政记录)
- **待 Round 3**:否

---

## [G44] Kirkeboen, Leuven & Mogstad:选专业与上不上大学一样重要?

- **判决**:CORRECTED(3/3 票;其中一席原判 HOLDS,但另两席各指出一处必修口径,取严)
- **锁定表述**:
  - 据 Kirkeboen, Leuven & Mogstad(NBER WP 20816;发表为 **QJE 131(3): 1057–1111, 2016**),用挪威 1998–2004 年**几乎全部**高教集中录取申请记录 + 教育登记(1998–2012)+ 税务登记(1998–2012),以集中录取分数线断点做 2SLS 并固定「次优选择」,结果变量为**申请后第 8 年的年收入**:摘要逐字「different fields have widely different payoffs, even after accounting for institutional differences and quality of peer groups. For many fields the payoffs **rival the college wage premiums**, suggesting the choice of field is potentially as important as the decision to enroll in college.」
  - **常被漏引的后半句**:「by choosing Science instead of Humanities, individuals **almost triple** their earnings early in their working career. By comparison, choosing Science instead of **Engineering or Business has little payoff**.」
  - **院校/同学质量的作用极小**:控制预测院校前后的回报估计相关系数 **0.84**;控制预测同学质量前后为 **0.98**(附图注分别为 0.8386 / 0.9805)。
  - **作者自己给的量级参照(必须写清它是什么)**:「未完成**任何高等教育**者 30 岁平均年收入 **USD 43,200**,持**任何高等教育学位**者 **USD 54,700**(+26.6%)」——这是**未加控制的原始描述性均值差**,不是任何回归估计的大学溢价,对照组是「post-secondary degree」(含短学制/学院)而非「大学」,且测量时点与 payoff(申请后第 8 年)并非同一时点。
  - **换分母警告(本条的价值所在)**:摘要用的是「college wage premiums」,正文对应句是「the payoffs rival the **usual estimates of** college earnings premiums」——是与文献通行估计比,**不是与 43,200/54,700 这对数字比**。把「选专业和上不上大学一样重要」搬到中美语境,除换分母外还换了整个工资分布形态:挪威是集中录取、公立免学费、工资压缩显著的劳动力市场,专业间收入差本就被压缩;估计本身是断点附近 compliers 的 **LATE**。
- **证据分级**:多源证实(三席各自下载 WP 20816 逐字核对,全部数字命中;期刊卷期页由二席独立确认)
- **数字定版**:**美国大学溢价用 BLS《Education Pays 2024》口径的 +66%**(本科中位周薪 $1,543 vs 高中 $930),**不用「约 +70–80%」**。理由:+70–80% 三席均未回到一手,属原稿自带的未标源断言;换成 +66% 后论证反而更稳——挪威 +26.6% vs 美国 +66%,仍是 2.5 倍差距。
- **不得这样写**:
  - ❌「挪威**全部**高教集中申请记录」——原文是该集中录取程序 covers **almost all** universities and colleges。
  - ❌ 把 43,200 / 54,700 说成「挪威口径的大学溢价」——它是原始均值差,且对照组是任何高等教育学位。
  - ❌ 把摘要的「rival the college wage premiums」与正文的「rival the usual estimates of college earnings premiums」当同一句混引。
  - ❌ 用未标源的「美国大学溢价约 +70–80%」。
- **利益相关**:无
- **待 Round 3**:否

---

## [G45] Hamilton Project:专业内方差 ≥ 专业间方差?

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - 据 Hershbein & Kearney,《Major Decisions: What Graduates Earn over Their Lifetimes》(Hamilton Project / Brookings),样本为 **80 个专业、恰好持学士学位且未再攻读研究生/专业学位**的劳动者,由 ACS 横截面构造的合成队列,**不限于全职,含兼职者与全年有失业经历者**;**全部「生涯累计收入」按 3% 年贴现率折算为现值**(尾注 ii 逐字:「All cumulative earnings are calculated using a **3 percent annual discount rate**. This converts earnings into a 'present value'」)。
  - **A 句(专业内离散)**:「the variation of lifetime earnings **within any given major** is at least as large as the variation across majors.」其**真正的专业内证据**是:「Cumulative earnings **double—or even triple—**when moving from the bottom quarter to the top quarter of earners **in a given major**. These increases are **larger for lower-earning majors**.」
  - **$720,000 / $1.82 million / 154% 是「所有专业合并后」的数字**,原文逐字:「**For all majors combined**, lifetime earnings at the 25th percentile…are $720,000, but they are $1.82 million at the 75th percentile…This is an increase of 154 percent」——同时含专业内与专业间两种离散。
  - **B 句(专业间差距在高分位扇形张开)**:「earnings differences across majors grow larger—or **fan out**—higher up in the earnings distributions. For instance, at the 10th percentile the difference…is about **$500,000**; at the 90th percentile, this difference is **over $3.5 million**.」
  - **因果版本(必须改称呼)**:Andrews, Imberman, Lovenheim & Stange,NBER WP 30331(**2022 年 8 月首发、2024 年 3 月修订**;ReStat 已接收,doi 10.1162/rest_a_01503,截至 2026-07 未见卷期页):「Quarterly returns (relative to **liberal arts**) range from **$983** in communications to **$7,901** in engineering and architecture **16–20 years after high school**(inflation adjusted to 2016 dollars)」,分位处理效应「notably fields that tend to have higher mean earnings — generating much larger effects at the top of the distribution. This suggests the mean effects embed **substantial (and differential) ex-ante risk** for students.」
  - **报告自设局限(必须引)**:「earnings differences across majors are driven by many factors and **do not necessarily reflect a wage premium for that particular major**. The estimates **cannot distinguish why** graduates in certain majors earn more than others.」报告首条结论恰是「a college degree—**in any major**—is important for advancing one's earnings potential」。
- **证据分级**:多源证实(三席各自下载两份 PDF 逐字核对)
- **不得这样写**:
  - ❌ 把 $720,000 / $1.82 million / 154% 当作 A 句「within any given major」的证据——原文明写 **For all majors combined**。三席一致点名。两句不可互换。
  - ❌ 不写「按 3% 贴现的现值」——少了「贴现」二字,读者会把 $1.82M 当成实发工资总额。面向准大学生这个差别很大。
  - ❌「同一份报告里**方向相反**的两句」/「互相打脸」——**框架本身要改**。A 是合并样本的四分位跨度,B 是各分位上的专业间差距,二者是同一分布的不同切面,**逻辑上完全相容**。正确表述:「同一份报告里服务于相反修辞用途、但逻辑上并不矛盾的两句话。」判断「只引 A 会得出选专业无所谓、只引 B 会得出专业决定一切」——**成立,保留**。
  - ❌⚠️ 把 Andrews et al. 称为「**因果版本**」/「德州因果估计」并与挪威 RD/2SLS 并列——作者自述逐字「**Our selection-on-observables method** compares students with similar pre-collegiate test scores and student demographics who graduated from the same high school in the same year and who attended the same college…While this approach makes the **strong assumption** that these observables are sufficient…」并明说「there are **few opportunities to use a regression discontinuity (RD) approach** in the US across multiple fields and institutions」,结论段再次自归类为「using **selection on observables** techniques」。改称「**可观测项选择模型,非因果识别**」。两席独立点名,判为本批最容易误导读者的一处。
  - ❌「ReStat 2024」写成已刊出卷期——写「NBER WP 30331(2022-08,2024-03 修订),ReStat 已接收(doi 10.1162/rest_a_01503),截至 2026-07 未见卷期页」。
- **利益相关**:Hamilton Project 隶属 Brookings,是**政策倡导型项目而非统计机构**;作者 Hershbein(Upjohn)、Kearney(Maryland)。须标注。
- **待 Round 3**:否

---

## [G46] 专业效应会随生涯衰减吗?三项研究口径不可互证

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **Deming & Noray, QJE 135(4): 1965–2005 (2020)**,样本为 **2009–2017 ACS 中 23–50 岁、全职在职(full-time working)的四年制本科毕业生**,左侧省略组为「**all other majors**」:「computer science and engineering majors earn about **45%** more early in their career, but only **33%** more by age 50. The earnings advantage for business majors declines from around **38%** initially to **20%** by age 50. In contrast, the earnings premium **grows over time** for life and physical sciences and social sciences majors.」
  - **必须成对引用的两句**:「**In levels**, earnings growth is rapid for all college graduates, regardless of major. **However**, while computer science, engineering and business majors are earning substantially more in their mid-twenties than do life/physical sciences and social sciences majors, **this advantage is greatly diminished by age 40.**」
  - **该文自己的机制结论**:「**Declining relative returns is a feature of STEM jobs, not majors.**」非 STEM 专业在 STEM 职业里的溢价由约 40% 十年内降到 20%;CS/工程专业在 STEM 职业的就业份额「declines from **59% at age 26 to 41% by age 50**. This decline of **18 percentage points** is almost entirely offset by increased employment in **non-STEM management occupations**.」
  - **作者自己的脚注 23(必须带)**:「The rapid growth in life cycle earnings for life and physical sciences majors is **partly due to their very high rate of graduate school attendance**. When restricting the ACS sample to respondents with exactly a BA…**slower growth** for life and physical sciences majors.」
  - **Andrews et al.(可观测项选择模型,非因果)**:生物与健康的回报随生涯增长最多,**增长 12.7 倍($413 → $5,655)**;且原文写的是「The return to **each** major increases relative to liberal arts over time」——**所有**专业相对文理科的回报都随生涯上升,生物健康只是涨幅最大者。
  - **Webber**:「there has been a **moderate convergence** over time in the return to the various major categories」——这是**出生队列之间**(1955–64 / 1965–74 / 1975–84)相对高中毕业生的生涯收入溢价的收敛,依赖「未观测生涯段的收入形状不随队列剧变」这一强假设,与「同一队列内随年龄变化」**不是同一个维度**。
  - **锁定结论(降级重写版)**:「三项研究基准不同(all other majors vs liberal arts)、度量不同(对数溢价 vs 季度美元水平)、样本与年龄窗不同(全职 23–50 岁全国 ACS vs 德州高中队列毕业后 16–20 年)、维度不同(队列内 vs 队列间),**不能直接互相印证或互相反驳**。可以说的是:**目前没有可比口径的证据支持『专业效应普遍衰减』**——而不是『三者方向不一致因此不存在衰减』。」
- **证据分级**:多源证实(Deming-Noray 与 Andrews 三席逐字核对;Webber 二席回到作者主页 PDF 原文、一席仅二手)
- **数字定版**:**12.7 倍的时窗须择一并注明**——引言写「over a **10 to 15-year** period」,正文第 4 节写「in the **two decades** after high school」,两种表述并存。建议统一用引言的「10–15 年」并注明正文另有表述。
- **不得这样写**:
  - ❌ 只引「In levels, earnings growth is rapid for all college graduates, regardless of major」而截掉下一句——**这是本条自己犯的、它本要防的那个错**,三席一致点名。只引前半句会让读者以为绝对量上的领先也稳固。
  - ❌ 把「生命科学/社科溢价扩大」当作反驳「普遍衰减」的干净正面证据而不提脚注 23——作者已把其中一部分归因于读研率。
  - ❌「数据 = 2009–2017 ACS,23–50 岁四年制本科毕业生」——漏了「**全职在职**」。这在与 G45 的 Hamilton Project(明确含兼职与全年失业经历者)并置时是**决定性的**,否则两文数字不可比。
  - ❌ 把 Andrews et al. 称作「德州**因果**估计」(同 G45)。
  - ❌ 把 12.7 倍读作「生物健康是例外」——原文是所有专业的回报都随生涯上升。
  - ❌ 把 Webber 的队列间收敛与前两者并列为「同类证据」。
  - ❌「45%→33% 的基准」写成不完整——完整基准是「Relative to **all other major groups (including education)**」。
- **利益相关**:无
- **待 Round 3**:**是(低优先)**。Webber(2014, Labour Economics)一席仅得二手著录、二席回到作者主页 PDF(非期刊版),需确认期刊发表版措辞一致。

---

## [G47] 「专业对不对口」的三套口径不可混用

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **口径 A(受访者自评,与最高学位的相关程度)**:NSF NCSES《National Survey of College Graduates: **2023**》(NSF 25-322,2025-01-13 发布,参考周 2023-02-01)Table 1-3——**全体(N=56,061,000)**:closely 53.7% / somewhat 27.1% / **not related 19.1%**;**仅本科为最高学历者(N=34,311,000)**:43.6% / 31.1% / **not related 25.3%**。注:该题问的是「工作与**最高学历**的关系」,**不是与本科专业的关系**;含硕博的那一行不能读成「本科专业转行率」,只有「仅本科」那一行(25.3%)才近似本科对口率。
  - **口径 B(分析师职业—专业交叉编码,二值)**:纽约联储 Staff Report No. 587(Abel & Deitz,**2012 年 12 月发布、2014 年 12 月修订**,数据为 **2010 年 ACS**,样本限**大都会区内、16–64 岁民用劳动力**,且**剔除全部研究生学位持有者**)——「about **27 percent** of undergraduate degree holders are working in a job that is **directly related** to their college major」;计算机科学专业中 73% 在要求本科学历的岗位、33% 在直接对口岗位;计算机工程 80%、Studio Arts 44%;College Degree Match 回归样本均值 **62%**(正文另作「about two-thirds」的描述性表述)。
  - **B 的两个工资系数(必须写清嵌套关系)**:同一回归(Table 4 第 (2)(4) 列,N≈162,454,控制 171 个专业固定效应,剔除研究生学历者,限全职每周≥35 小时且每年≥40 周、时薪 $5–400)——学历门槛匹配系数 **0.244 (0.011)**(作者写作「almost 25 percent more」,严格换算 +27.6%);专业对口系数 **0.054 (0.005)**(+5.5%),原文逐字「which in principle is **on top of** the wage premium for a College Degree Match」。**两者叠加而非互斥,比值约 4.5–5 倍。**
  - **口径 C(是否在 STEM 职业就业)**:Census 2021-06-02 报道(2019 年 ACS 1 年数据,25–64 岁在职大学毕业生约 5,000 万)——工程 52%、计算机/数学/统计 51%、物理科学 28%、生物/环境/农业 16%、心理 10%、社科 9%;「STEM workers who majored in a STEM field in college typically made higher salaries than those who did not: on average, **$101,100 vs. $87,600**」——这是**在 STEM 职业内部**比较「STEM 专业出身 vs 非 STEM 专业出身」,不是一般意义上的专业溢价。
  - **口径 D(错配惩罚随时间上升)**:Cassidy & Gaulke,《The Increasing Penalty to **Occupation-Education** Mismatch》,EdWorkingPaper 23-760(2023-04);**已发表于 Economic Inquiry 62(2): 607–632 (2024)**——用 NSCG 数据,1993–2019 年间错配率仅由 **19% 微降至 17%**(全职样本),而错配的**工资惩罚上升 51%**(1993 年基准约 11%,2003 年 +35%,2010 年 +57%),somewhat mismatched 的惩罚上升 **179%**。作者把上升部分归因于「专业构成变化」与「'excess' education(超出岗位要求的学历)回报下降」——**后者是学历层级口径而非专业对口口径**。该文用的是与口径 A 同一套 NSCG 自报指标,**不是独立测量**,且是观测性 OLS、非因果。
  - **核心框架(三席一致认定是本条最有价值的部分,建议加粗保留)**:A 是自评「与**最高学位**的相关程度」(三档,只有「完全不相关」计入 19.1%);B 是分析师交叉编码判定「是否**直接对口本科专业**」(二值);C 是「是否在 **STEM 职业**就业」。**三者分子分母定义各不相同,任何跨口径的加减或对比都是错的。**
- **证据分级**:多源证实(NSCG 2019 与 2023 两波数据表三席分别用 xlsx/PDF 独立复算,百分比全部对得上;SR587 与 Cassidy-Gaulke 三席逐字核对)
- **数字定版**:**用 NSCG 2023(19.1% / 25.3%),不用 2019(19.6% / 25.7%)**。理由:2019 波已被 2021(NSF 23-306)与 2023(NSF 25-322)两轮更新取代,面向 2026 年读者引 2019 年数据是可避免的口径瑕疵。方向与量级未变。
- **不得这样写**:
  - ❌「『有没有学历门槛』比『对不对口』**重要 5 倍**」——**过度解读,三席均要求改写**。原文明说 5% 是「**on top of**」那 25%,两者是**嵌套的两道门槛**而非二选一的替代项;把同一横截面回归的两个点估计相除得出「重要性之比」,既无统计检验支撑,也暗示了一个原文没有的取舍。正确表述:「在这份 2010 年横截面的城市工资回归里,『岗位要求本科学历』对应约 +25% 的工资,**在此之上**『岗位与专业对口』再对应约 +5%(系数 0.244 vs 0.054,约 4.5–5 倍)。两者叠加而非互斥,系数之比不等于重要性之比。」并须写明:换成 NSCG 自报口径,不对口惩罚本身就有 11–17%,与 +5% 相差三倍以上——**两套口径不可互换**。
  - ❌ 把 Abel-Deitz 的 27% 与 NSCG 的 54.1% 直接对照——前者剔除了全部研究生学历者。
  - ❌ 题名写成《The Increasing Penalty to Occupation-**Major** Mismatch》——**是 Education 不是 Major**,一词之差改变了错配的定义口径。三席均点名。
  - ❌ 把 SR587 的两个系数说成因果估计——该文主题是集聚经济与城市工资溢价,匹配变量只是控制项,自选择未处理。
  - ❌ 把「College Degree Match 约 62–67%」写成一个区间——62% 是回归样本均值,「约三分之二」是另一句描述性表述,是两个不同的量。
  - ❌「NSCG: 2019」而不注明已有两轮更新。
- **利益相关**:无(NSF NCSES、纽约联储、Census 均为官方或联储机构)
- **待 Round 3**:否

---

## [G48] 中国的分专业就业数据:不是不存在,是不公开数值

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **锁定版本**:「中国**没有公开发布的、全国性、可比、连续的分专业数值型就业指标**——无分专业失业率、无分专业起薪、无分专业学历错配率,三项经三席穷尽搜索均未见任何官方发布。但『没有任何官方分专业就业数据』是过强的表述:分专业就业数据在体制内确实存在、被采集并被用于行政处置,官方也公开发布过**排序型产物**,只是**从不发布分母与数值**。」
  - **官方分专业产物(三条实例,均可回到一手)**:① 2014-10-14 教育部高等教育司通过「微言教育」公布《近两年(2012、2013)就业率较低的本科专业名单》,全国 15 个专业 + 31 省份及新疆兵团分省名单——**只给专业名,不给一个就业率数字**;② 教育部 2026-04-28 逐字:已「推动各省份发布**覆盖 473 种专业的急需专业清单和专业预警清单**」;③ 教就业〔2024〕5 号逐字:「对**就业质量不高的专业**实行**红黄牌提示制度**」;教高司函〔2025〕3 号要求各省「于 7 月 31 日前发布本年度省级急需本科专业清单和过剩专业预警清单」。
  - **省/校两级确有公开的分学科门类/分专业落实率**:湖南省教育厅《关于全省普通高等学校 2020 届毕业生初次就业情况的通报》第六节按学科专业大类给出本科就业率(历史学 84.78%、工学 83.02%、教育学 83.02%);安徽省教育厅《普通高校本科专业布局和需求分析报告(2023)》公布落实率相对较低的 21 个专业;江西以落实率低于 50% 亮黄牌、连续 2 年低于 50% 亮红牌责令停招,四川设连续 2 年/3 年低于 50% 的黄牌/红牌;各高校依教育部要求年度发布的《毕业生就业质量报告》普遍含分专业落实率。
  - **官方指标体系里没有「分专业」这一维(最硬的正面证据)**:教育部发展规划司《中国教育监测与评价统计指标体系(2025 年版)》第 29 页,「毕业生毕业去向落实率」的『指标分解』逐字为「**分层次;分就业形式;分办别**」——**没有『分专业』**;全书 108 页所有指标的最细学科维度只到「分学科领域」(门类级),经全文正则统计**无一处出现「专业」作为指标分解字段**。同页官方自陈局限:落实率「**不能完全反映毕业生人岗匹配的实际情况**、毕业生长期发展情况等」——这是官方承认无 underemployment 指标的最好一手依据。
  - **落实率公式必须标版本年份**:2021 版(教学厅函〔2021〕19 号附件 1)逐字「毕业去向落实率 = 协议和合同就业率 + 创业率 + 灵活就业率 + 升学率」,四个分率分母统一为「毕业生总数」;**现行版**依《教育部办公厅关于进一步做好普通高等学校毕业生就业监测工作的通知》(**教就业厅函〔2024〕11 号**),公式改为「毕业去向落实率 = **单位就业率 + 自主创业率 + 自由职业率 + 升学率**」——「协议和合同就业率」「灵活就业率」两个术语已不在公式中(见《中国教育监测与评价统计指标体系(2025 年版)》第 29 页)。
  - **正确的方法论落点(比原稿更强)**:「中方**有**分专业数据但不公开数值,美方(Census/ACS + NY Fed)公开微观数据可复算——**不对称在可复现性,而非存在性**。」
- **证据分级**:多源证实(19 号文 PDF 三席逐字核对;反证来源为教育部/省教育厅一手页面)
- **不得这样写**:
  - ❌「中国**没有**官方的『分专业毕业生失业率』『分专业起薪』『分专业学历错配率』**任何一项**」「中国没有任何官方的分专业就业数据」——三席一致判为**过强、读者一查即破**。
  - ❌「美方(NY Fed / **BLS** / ACS)有分专业微观数据」——分专业(field of degree)微观数据来自 **Census Bureau 的 ACS**(2009 年起设该题),NY Fed 的产品由 ACS 微观数据加工而来;**BLS 不发布分专业失业率**(BLS 是分职业/分行业)。删去 BLS 或改为「Census/ACS + NY Fed」。
  - ❌ 把 2021 版落实率公式当作**现行**口径而不标版本年份。
  - ❌「分子包含升学、灵活就业、**自由职业**、创业」四项并列——**自由职业(编码 76)是灵活就业的子项**,不是并列加项(2021 版口径);另「升学」含「**出国、出境(编码 85)**」,即出国留学也计入分子,原稿漏了这一点,而它对准大学生更有解释力。
  - ❌ 把流传的「红牌/绿牌专业」当官方数据——出自**麦可思 MyCOS 商业调查**,见 G54/G55。
- **利益相关**:教育部既是数据采集方也是「结构优化」的执行与自评方;省级教育行政部门掌握并使用分专业就业率做行政处置。「红牌专业」榜的发布方麦可思是商业调查公司(详见 G54)。
- **待 Round 3**:否(三席均已穷尽检索并给出反证清单)

---

## [G49] 官方「就业」的认定门槛与数据发布管制

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - 据教学厅函〔2021〕19 号附件 2(三席逐页图像/字符级比对,**四段引文全部一字不差**):
    - **其他录用形式就业(编码 12)**:界定为「用人单位不签订就业协议或劳动合同,仅提供聘用证明、工资收入流水等证明材料」;审核依据为「用人单位出具的聘用证明**或**毕业生本人提供的工资收入证明、收入流水等其他证明材料,**薪酬需达到当地最低工资标准**」。
    - **自主创业(编码 75)第(3)项电子商务创业**:「利用互联网平台从事经营活动,如开设网店等」;审核依据**仅为**「网店网址、网店信息截图和收入流水」——**该行到此结束,无任何薪酬下限**。
    - **自由职业(编码 76)**:「指以个体劳动为主的一类职业,如作家、自由撰稿人、翻译工作者、中介服务工作者、某些艺术工作者、**互联网营销工作者、全媒体运营工作者、电子竞技工作者**等」;审核依据为「**依据毕业生本人签字确认的证明材料,由校、院两级就业部门负责同志审定**,薪酬需达到当地最低工资标准」。
    - **说明第 1 条**:最低工资门槛的适用范围被**显式限定为三类**——「『科研助理、管理助理』『其他录用形式就业』『自由职业』中当地最低工资标准参见人社部公布的《全国各地区最低工资标准情况》」。
    - **数据发布管制(正文第三条,逐字)**:「各省级就业工作部门在对外公开本省毕业生毕业去向落实率之前,**须与教育部高校学生司核实数据,未经核实不得擅自公开**。各高校未经省级就业工作部门同意,**不得向其他部门、机构等提供本校就业数据**。」该条属「严格落实就业统计责任制」,紧接在省级/校级分管领导签字确认要求之后——**管制与签字问责是同一条款的两半**。
  - **锁定版的「门槛」表述(比原稿更锋利)**:「最低工资门槛只约束三类,**开网店(自主创业·电商)反而是门槛最低的一档**:一个网址、一张截图、一份流水即可,连最低工资都不必达到;做电竞、当博主走自由职业(编码 76),需本人签字材料 + 校院两级审定;走编码 12 的则需单位证明或工资流水。」
  - **「四不准」与「三不得」必须并列**:四不准逐字为不准以任何方式强迫毕业生签订就业协议和劳动合同、不准将毕业证书发放与签约挂钩、不准以户档托管为由劝说毕业生签订虚假就业协议、不准将**毕业生**顶岗实习、见习证明材料作为就业证明材料;**三不得**逐字为「不得不切实际向高校或院系提去向落实率具体指标;不得层层加码向辅导员摊派就业任务;不得将单一的去向落实率指标与就业工作人员或者辅导员的绩效考核、评优等挂钩」。
  - **主管部门自陈的造假信号(比推理更硬)**:教育部/省校反馈的「疑似虚假就业数据」监测口径包括「**灵活就业率、自由职业率和自主创业率过高,其他录用形式占比过高**,疑似小企业扎堆就业」(湖南农业大学 2025-07-04《关于开展 2025 届毕业生就业监测数据自查工作的通知》逐字)。
  - **时效限定(必须显式写出)**:该文件是**现行可查的最新公开界定标准**,但附件 2 的毕业去向界定已由**教就业厅函〔2024〕11 号**接续修订(湖南农业大学 2025-07-04 通知逐字要求按该文号审核;《中国教育监测与评价统计指标体系(2025 年版)》亦改引该文号)。写「2021 年版规定……(该文 2024 年由教就业厅函〔2024〕11 号接续修订,新版全文未公开)」。
- **证据分级**:多源证实(三席均回到同一份 PDF 原件做字符级比对,四段引文完全一致)
- **不得这样写**:
  - ❌「官方『就业』的下限 = **月入**达当地最低工资 + 一张本人签字的说明。**开网店**、做电竞、当博主均计入落实率」——**三处错**:① 文件只写「薪酬需达到当地最低工资标准」,**未限定为月薪**,人社部该表同时含月最低与小时最低工资标准,「月入」是推断;② **自主创业(含开网店)不设最低工资门槛**;③「一张本人签字的说明」**只适用于自由职业(编码 76)**,编码 12 需单位证明或工资流水。三席一致要求拆开写,勿合并。
  - ❌ 只列「四不准」而略去「三不得」——三不得恰恰是官方自陈「造假压力来自指标层层加码」的证据,对本篇论证的价值**高于**四不准。
  - ❌ 断言 19 号文「至今有效」——写成显式限定语:「截至 2026-07 未见公开的替代版全文;但 2024 年已有接续文号,是否存在未公开的新版界定标准无法核实。」
- **利益相关**:教育部既是落实率的定义方、采集方,也是考核方与问责方。
- **待 Round 3**:否

---

## [G50] 青年失业率口径断裂

- **判决**:CORRECTED(3/3 票;其中一席原判 HOLDS,但另两席各指出溯源问题,取严)
- **锁定表述**:
  - **旧口径终点**:2023 年 6 月 16–24 岁城镇调查失业率 **21.3%**(2023-07-17 由国家统计局例行发布,为 2018 年有统计以来最高;2023-08-15 宣布暂停发布)。
  - **新口径起点**:2023 年 12 月,不含在校生的 16–24 岁劳动力失业率 **14.9%**(2024-01-17 随《关于完善分年龄组调查失业率有关情况的说明》同日启用)。**21.3 − 14.9 = 6.4 个百分点的差不可读作改善——两者不可比。**
  - **改口径的官方理由(逐字,勿倒装)**:「从我国国情看,**在校学生的主要任务是学习,而不是兼职工作**,如果把在校学生包含在分年龄组内,会把在校寻找兼职和毕业后寻找工作的青年混在一起,不能准确反映进入社会真正需要工作的青年人的就业失业情况」;「多数青年 24 岁时刚毕业不久,尚处于择业期,一些人未就业或就业不稳定,至 29 岁时绝大多数已度过择业期,就业情况趋向稳定」。
  - **关键空白(HOLDS,且有更硬的证据)**:该《说明》全文**只字未提 21.3%、14.9% 或任何一个失业率数字**,也**无任何新旧口径并列、重叠期双算、回溯序列或折算系数**。它给出的唯一定量素材是**分母存量**:「2023 年各月平均,我国 16—24 岁城镇人口中,在校学生占比 6 成多,**近 6200 万人**;非在校学生占比 3 成多,**约 3400 万人**。」——即统计局只交代了「谁被剔除、有多少人」,从未给出剔除后的同期失业率。**「无法量化落差」由此从断言变成有据可查的事实。**
  - **可用的月度数字(只用这两个)**:2026 年 **6 月 14.9%**(25–29 岁 7.1%、30–59 岁 4.0%,较上月分别下降 0.7、0.1、0.1 个百分点);由「较上月下降 0.7」可反算 **5 月 15.6%**。
  - **必须同时给出的同比(最严重的遗漏)**:**2025 年 6 月同口径为 14.5%,2026 年 6 月的 14.9% 高于上年同期 0.4 个百分点。**「连续三个月下降」是每年 3→6 月的季节性形状(2025 年同样是连续下降到 6 月的 14.5%),**同比方向是上升**。面向准大学生只给环比不给同比,会造成实质误导。
  - **发布载体(必须据实说明取证限制)**:《说明》末段逐字「今后我局将按月在**国家统计局数据发布库**中发布不包含在校学生的 16—24 岁、25—29 岁、30—59 岁劳动力失业率」——自 2024 年 1 月起这组数字**不再有独立发布页**,一手出处是 data.stats.gov.cn 数据库。三席均遭 easyquery/直取 403,月度值系由财新、澎湃、观察者网等多家独立媒体同日引述交叉一致确认。**这一可发布性下降本身值得写进方法论一节。**
  - **ILO 1 小时标准**:中国调查失业率对「就业」采用参考周内工作 1 小时以上的 ILO 标准,与美国 CPS 同源,统计局自己也明示 1 小时标准「用于界定有没有就业,而非就业『足不足』」——**因此这一条不构成中美不可比的理由**;不可比出在分专业维度和分子构念,不在 1 小时标准。
- **证据分级**:《说明》引文与 6200 万/3400 万为**单源已核**(统计局原页,三席逐字一致);月度数字为**多源证实但未落一手数据库**(四家独立媒体同日引述一致);2026 年 3 月 16.9%、4 月 16.3% 为**未验证**(两席明确未能落到一手,仅与「连续下降」自洽)。
- **不得这样写**:
  - ❌ 把 21.3% 与 14.9% 写得像出自《关于完善分年龄组调查失业率有关情况的说明》——该说明全文无任何失业率数字。**须分三个出处标注**:21.3% = 2023-07-17 例行发布;14.9%(2023 年 12 月)= 2024-01-17 数据发布库首月值;《说明》= 口径变更理由与人口构成。
  - ❌ 只列 2026 年 6 月 14.9%(5 月 15.6%、4 月 16.3%、3 月 16.9%)而不给同比——读起来是单向改善,但同比是上升 0.4 个百分点。
  - ❌ 直接使用 2026 年 3 月 16.9% 与 4 月 16.3% 而不加限定——两席未能落到一手页面。**要么只写 6 月与 5 月,要么加「据月度环比反推/据媒体转述」限定语。**
  - ❌ 暗示这些月度数字应能在 stats.gov.cn 新闻稿页找到——统计局**不以新闻稿形式**发布该系列。
  - ❌ 把《说明》两句拆开调序引用——原文为一句连读。
- **利益相关**:国家统计局既是口径的制定方也是唯一发布方;口径变更发生在旧口径创历史新高并被暂停发布之后,时序本身即须向读者交代。
- **待 Round 3**:**是**。① 2026 年 3 月与 4 月的月度值需反证搜索席落到 data.stats.gov.cn 或统计局发布会文字实录;② 2025 年 6 月 14.5% 目前只有一席一个媒体来源(voc.com.cn),而它是「同比上升」这一关键反转的唯一支点,**必须补第二个独立来源**。

---

## [G51] 统计局年平均工资:IT 溢价缩窄但未消失

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - 据国家统计局《2025 年城镇单位就业人员年平均工资情况》(2026-05-15 发布):
    - **城镇非私营单位**全国 **129,441 元**(名义 +4.3%、实际 +4.2%);信息传输、软件和信息技术服务业 **248,752**(+4.1%,居首)、金融业 211,164(+4.6%)、科学研究和技术服务业 182,064(+3.8%)、卫生和社会工作 146,266(+2.2%)、教育 133,539(+5.8%)、制造业 113,594(+5.2%)、住宿和餐饮业 62,461(+3.7%)。
    - **城镇私营单位**全国 **71,590 元**(名义 +3.0%、实际 +2.9%);**金融业 140,451(+3.8%)反超信息传输业 128,166(+4.0%)**;制造业 76,055(+6.4%)、科学研究和技术服务业 83,560(+1.4%)、卫生和社会工作 75,631(+0.5%)、**教育 63,908(+5.3%)**、住宿和餐饮业 55,123(+2.0%)。
    - **两套口径之比 = 129,441 ÷ 71,590 = 1.81 倍**;私营为非私营的 **55.3%**。
    - IT 溢价:私营 IT 高出私营总平均 **79.0%**(128,166 ÷ 71,590);非私营 IT 高出非私营总平均 **92.2%**(248,752 ÷ 129,441)。**无论哪套口径,IT 溢价都在 79%–92% 之间——「IT 不赚钱了」在统计局口径上不成立。**
    - 「溢价在缩窄而非消失」的增速比较:IT 私营 +4.0% / 非私营 +4.1%,**双双低于**制造业 +6.4% / +5.2% 与教育 +5.3% / +5.8%。
  - **四条口径注**:(a) 逐字「工资总额是税前工资,包括单位从个人工资中直接为其代扣或代缴的个人所得税、社会保险基金和住房公积金等个人缴纳部分**以及房费、水电费等**」;(b) 逐字「城镇单位指城镇地域内就业人数在 **5 人及以上的法人单位**,2025 年纳入统计的单位共计 **306.2 万家**」——因限于法人单位,个体工商户与自由职业者不在样本内;(c) 平均工资计算公式逐字「就业人员平均工资 = 就业人员工资总额 / 就业人员平均人数」,**按此定义即为加权算术平均值**,该发布页**通篇无「中位数」三字**;(d) 为全部在岗就业人员平均,**非应届生起薪**。
- **证据分级**:多源证实(三席分别抓取同一发布页,19 个行业门类 × 2 套口径逐格一致;倍数由三席各自手算/python 复算)
- **数字定版**:**1.94 倍必须整条替换为 1.81 倍。** 1.94 的真实来源是**信息传输业内部**的两口径之比(248,752 ÷ 128,166 = 1.941),被误当成全国总体之比。且 1.94 与同一条论断自己写的「私营不足非私营的 56%」内部矛盾(1 ÷ 0.553 = 1.81)。若想保留 1.94,须改写为:「**IT 行业内部,非私营口径是私营口径的 1.94 倍——比全国总体的 1.81 倍还悬殊,说明 IT 的『高薪印象』高度依赖非私营样本。**」
- **不得这样写**:
  - ❌「非私营 vs 私营**差 1.94 倍**」——三席一致判为会被读者用计算器当场戳穿的错误。
  - ❌ 采集稿列表中的「私营教育 63,908 元 **+3.3%**」——**原页为 +5.3%**,3.3% 是采集笔误,须删。正文后段写的「教育(+5.3%/+5.8%)」是对的。
  - ❌ 税前口径引文在「个人缴纳部分」处截断——须补全「以及房费、水电费等」或加省略号。
  - ❌ 把「算术平均」说成统计局原话——官方原话是计算公式,「按此定义即为算术平均」是解读。
  - ❌ 混淆两类中位数——统计局**确实公布居民人均可支配收入中位数**,只是不公布**分行业工资中位数**;与美方 median earnings 不可并列。
  - ❌ 不加限定地使用「倍数」——两套口径的样本量与行业/所有制构成差异极大,直接相除得出的倍数带有构成偏误。
- **利益相关**:无(官方统计);但须提醒:该口径不含个体工商户与自由职业者,而这两类正是青年就业的重要吸纳池。
- **待 Round 3**:否

---

## ⚠️ [G52] 专业撤销与停招:官方口径被读反,并有一处伪引

- **判决**:**REFUTED**(1/3 席判 REFUTED,2/3 席判 CORRECTED——按 refute-by-default 取最严,整条按「原表述不可承重」处理,数字部分可用)
- **锁定表述**:
  - **数字部分(三席逐字核对全部无误,可放心承重)**:
    - 教育部 2025-04-22 新闻稿逐字:「全国高校共**新增专业点 1839 个**,调整学位授予门类或修业年限专业点 **157 个**,**停招专业点 2220 个,撤销专业点 1428 个**,专业调整优化力度进一步加大。」「《普通高等学校本科专业目录(2025 年)》,**增列 29 种新专业**。新目录包含 **93 个专业类、845 种专业**。」「目前全国高校本科专业布点共有 **6.28 万个**。」结尾「教育部将进一步强化**专业设置与就业工作的联动**」。
    - 教育部 2026-04-28 发布逐字:「2026 年本科专业目录在『交叉学科』门类中首批列入**未来机器人、交叉工程等 11 种目录内已有专业**和**具身智能、脑机科学与技术等 4 种本次列入目录的新专业**。目前,本科专业目录共涵盖 **13 个门类、92 个专业类、883 种专业**。」「『十四五』期间,全国高校**新增本科专业布点 1.02 万个、撤销或停招 1.22 万个**。专业调整幅度持续增大,**累计调整比例超 30%**,今年全国高校**专业调整比例首次突破 10%**。**本科专业结构进一步优化**。」
    - 毕业生规模:2021 届 909 万 → 2024 届 1,179 万 → 2025 届 1,222 万 → **2026 届预计 1,270 万**(同比增 48 万;1,270 − 48 = 1,222 自洽;须加「教育部预计」限定,一席未取得一手正文页)。
    - **口径提醒(三条,均成立且有价值,保留)**:单位是**专业点**不是人;**停招 ≠ 撤销**;全国目录**总共才 883 种专业**——用于反衬「3648 个专业被砍」(2220 + 1428)的媒体误读。
  - **锁定的政策链条表述(替换原推论)**:「**就业率过低是官方明示的『停招』触发条件**,撤销的明示条件是『连续五年未招生』——二者由同一条政策链相连。一手依据:《普通高等学校本科专业设置管理规定》(教高〔2012〕9 号)第二十六条逐字『高校设置的专业在教育教学过程中出现办学条件严重不足、教学质量低下、**就业率过低**等情况,高校主管部门须责令有关高校限期整改、暂停招生』;《普通高等教育学科专业设置调整优化改革方案》(教高〔2023〕1 号)第 13 条逐字『定期开展学科专业建设质量检查,对办学条件严重不足、教学质量低下、**就业率过低**的,要**责令暂停招生**、限期整改』,第 16 条逐字『对高校**连续五年未招生**的专业予以**撤销**处理』;教高司函〔2025〕3 号逐字『对本地区**布点量大、就业率过低**的专业及相近专业,原则上不再支持增设』;教就业〔2024〕5 号逐字『对**就业质量不高**的专业实行**红黄牌提示制度**』『将高校毕业生**就业状况**作为高校办学资源配置、教学质量评估、**招生计划安排的重要依据**』。**因此『撤销/停招多 = 就业差』不是民间脑补,是政策设计的预期结果。** 真正需要提醒考生的是**滞后性**——从就业率过低到最终撤销可长达五年以上,而不是『官方没这么说』。」
  - **目录结构变化的正确读法**:「专业种数是**干净的净增 38 种**(845 + 38 = 883,无一种被删);被重组的是**门类与专业类的框架**——门类 12 → **13**(首增交叉学科门类)、专业类 93 → **92**(减 1),并有 11 种**目录内已有专业整体迁入**新设的交叉学科门类(该门类首批 15 种 = 11 种已有 + 4 种新专业,是搬家不是新增)。」另须一句限定:交叉学科门类是**本科专业目录**首次增设,研究生教育学科专业目录早在 2021 年就已设「交叉学科」门类,教育部原文表述正是「推动本科专业目录与研究生教育学科专业目录有机衔接、上下贯通」。
  - **布点存量的正确读法**:按本条自己给的定义(停招保留专业点、只有撤销从目录删除),2024 年度净变化为 1,839 − 1,428 = **净增 411 个布点**;2023 年度为增设 1,673 − 撤销 1,670 ≈ 净增 3;目录专业种数亦逐年增(2024 年版 816 种 → 2025 年版 845 种 → 2026 年版 883 种)。正确说法是「**在招**布点在收缩、**存量**布点仍在净增,同时毕业生人数在增加」。
- **证据分级**:多源证实(数字部分三席逐字核对一致;政策链条条文三席分别 curl 教育部原页/镜像取得)
- **不得这样写(逐条)**:
  - ❌⚠️**【被推翻的承重推论】**「教育部相关政策文件**通篇未把『就业率』列为撤销的明示标准**,因此『撤销多 = 这个专业没前途』是媒体与考生的推断,不是官方论断」——**三席全部推翻**,其中一席据此判 REFUTED。至少三份现行文件把就业率写成明示的行政后果触发条件(见上)。这一改动同时**反向加固 G48**:分专业就业率在体制内存在且被用于行政处置,只是不公开。
  - ❌⚠️**【伪引·必须点名】**「**撤销、停招专业点数大幅超过增设专业点数,专业结构不断优化**」被标为教育部新闻稿逐字——**该句不在 2025-04-22 与 2026-04-28 两份教育部发布的任何一份中**。一席全文检索两份原页确认零命中;2025-04-22 原文对应表述是「**专业调整优化力度进一步加大**」,2026-04-28 原文是「**本科专业结构进一步优化**」。另有一席指出该句可见于**教育部高教司答记者问**(gov.cn 转载)。**处理方式:删除该引号,改用上述两句真实原文;若确要引答记者问版本,必须标明出处是答记者问而非新闻稿,不得标成「教育部新闻稿逐字」。**
  - ❌「《目录(2026 年)》**新增 38 种**专业」标为教育部原文——教育部 2026-04-28 发布**通篇无「38」字样**,38 是 883 − 845 的净差,系媒体/复算所得。
  - ❌「专业类减少 1、专业种数增加 38,**说明发生了合并重组,不能读作『净增 38 种全新专业』**」——推理不成立。845 + 38 = 883 分毫不差,说明**没有专业种被删除**;93 → 92 的变化发生在**专业类**层级(门类重划所致),与专业种数的增减无关。
  - ❌「布点数**净减少**」/「**布点在减少而人数在增加**」——布点数并未净减少(见上)。「十四五累计新增 1.02 万、撤销或停招 1.22 万」因把撤销与停招**合并统计**,同样不能推出布点净减。
  - ❌ 把 1,270 万写成已发生的确数——须加「教育部预计」。
- **利益相关**:**教育部既是撤销/停招的执行方,也是「结构优化」的自评方**——「专业结构进一步优化」是其自评话语,须随引用标注。另:流传的「红牌专业」榜(法学、绘画、公共事业管理等)出自**麦可思 MyCOS 商业调查公司**,靠就业报告与咨询业务盈利,与「专业风险」叙事存在商业利益关联,**不可与教育部数据并列**。
- **待 Round 3**:**是**。① 「撤销、停招专业点数大幅超过增设专业点数」一句的真实出处需锁定(是否确为教育部高教司答记者问,还是新京报标题),这决定它能否作为官方口径引用;② 2026 届 1,270 万仅一席取得二手确认,需落一手。

---

## [G53] 考研降温与国考创新高

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **考研**:教育部 2025-11-24 通稿末段逐字「据统计,**2026 年全国硕士研究生招生考试报名人数为 343 万**」——**全文再无口径界定、无应届/往届拆分、无解读**。较 2025 年的 388 万减少 45 万(**−11.6%**),**自 2024 年起连续第三年下降**(474 → 438 → 388 → 343)。完整历史序列:2019 年 290 万 → **2020 年 341 万** → 2021 年 377 万 → 2022 年 457 万 → **2023 年 474 万(峰值)** → 2024 年 438 万 → 2025 年 388 万 → 2026 年 343 万。**343 万应表述为「2020 年(341 万)以来最低」或「自 2022 年冲上 457 万的高点后首次回落至 350 万以下」。**
  - **国考**:2026 年度计划招录 **3.81 万人,较 2025 年度的 3.97 万人减少 1,602 人,是 2019 年以来首次缩招**;通过资格审查 **371.8 万人**(创历史新高),较 2025 年度的 341.6 万人增加 30.2 万(**+8.8%**);过审人数与录用计划之比 **371.8 ÷ 3.81 ≈ 97.6,约 98:1**(2025 年度为 341.6 ÷ 3.97 ≈ **86:1**)。**98:1 的抬升同时来自分子上升(+8.8%)与分母收缩(−4.0%)——两头夹击。**
  - **年龄放宽属实,可写具体**:一般职位年龄上限由 **35 周岁放宽至 38 周岁**(1986 年 10 月至 2007 年 10 月出生);2026 年应届硕士、博士研究生由 **40 周岁放宽至 43 周岁**(1981 年 10 月以后出生);官方理由逐字为「按照实施渐进式延迟法定退休年龄有关政策要求,对公务员招录年龄条件作了适当放宽调整」。**「年龄放宽会机械性推高报名基数、官方未拆分其中多少来自年龄放宽」这一判断成立,保留。**
  - **口径提醒(全部成立,保留)**:371.8 万是**通过资格审查人数**,不是报名人数,更不是录取率;考研 343 万(报名数)与国考 371.8 万(过审数)**口径不同,不可并列比较**;「考研 −11.6% 与国考 +8.8% 同时发生,否定『青年整体退出竞争』」这一推论成立。
- **证据分级**:考研 343 万为**单源已核**(教育部原页逐字,三席均取得);历史序列与国考数据为**多源证实**(教育部旧稿 + 新华网/北京日报/财新/央视网多家一致,三席独立复算)
- **不得这样写**:
  - ❌⚠️「2026 年考研报名 343 万……并**首次跌破 350 万**」——**三席全部判为事实错误**。2020 年即为 341 万,2019 年 290 万,均低于 350 万。写「首次」会让考生误以为出现历史性拐点,且会被任何查过历年序列的读者推翻。(可对照的媒体口径是:2025 年 388 万被称为「十年来首次跌破 400 万」。)
  - ❌⚠️「国考『创新高』中……**招录计划本身也在扩张**」——**方向说反了,三席全部推翻**。招录计划反而是 2019 年以来首次缩招。**这一改动实际加强文章的论点,务必改过来**;继续写「招录也在扩张」会低估竞争强度。
  - ❌「口径 = **网上报名并缴费确认人数**」——教育部**未定义**该口径(是否剔除未缴费/未确认者、是否为去重人数均无说明)。应写「教育部仅公布『报名人数』一个数,**口径未公开界定**,亦不公布应届/往届拆分,更非实际参考或录取人数」。
  - ❌ 把新华社《报考回归理性 发展路径多元》(2025-11-24)称为「**官方解读框架**」——该文副题即「**专家分析** 2026 年考研报名人数」,通篇引述的是厦门大学教育研究院副院长王树涛、华中师范大学胡向东等**学者**观点;教育部当天的通稿只给数字、**不作任何解读**。改写为「新华社约请专家给出的解读框架」——这反而**强化**文章「两种解释都无法证伪」的立论。
- **利益相关**:教育部与国家公务员局既是数据发布方也是政策制定方;年龄放宽与延迟退休政策同源,报名基数的政策性抬升未被官方拆分。
- **待 Round 3**:**是(低优先)**。新华社《报考回归理性 发展路径多元》的篇名与日期有一席未能取得一手页面(检索额度耗尽),另两席取到;加书名号引用前建议再确认一次。

---

## [G54] 麦可思是谁:商业公司、客户即样本源、方法学空白

- **判决**:CORRECTED(3/3 票;其中一席原判 HOLDS,另两席各指出必修口径,取严)
- **锁定表述**:
  - **公司与股权**:麦可思 **2015 年 10 月挂牌新三板(证券代码 833861),2020 年已终止挂牌**——自 2020 年起再无强制信息披露义务,**2018 年报是其最后一份公开财务数据,写作时已是 8 年前的旧账**。创始人王伯庆持股 690.00 万股、**61.61%**。
  - **收入结构(分母必须写对)**:2018 年**营业收入 113,501,829.94 元**(= 主营业务收入 110,752,232.01 + 其他业务收入 2,749,597.93),其中**数据监测类 96,886,518.62 元占 85.36%**、**咨询类 16,615,311.32 元占 14.64%**;毛利率 **87.39%**。
  - **客户即样本源**:研报正文逐字「公司**直接面对高校、院系/专业、教育厅/局等机构客户**提供产品和解决方案」;「在中国教育部门批准 2500 所高校中**累计合作 706 所,正在执行签约项目的 569 所**,其中服务年限在三年以上的客户占比为 83%」。**「客户 = 样本源」仍只是结构性风险提示——三席均未找到证据表明样本仅取自其签约高校,此限定语必须保留。**
  - **样本与施测方式(《2023 年中国本科生就业报告》技术报告,235 页,PDF 三席独立提取均为 20,809 行)**:逐字「全国本科生样本为 **13.5 万人**。覆盖了 **428 个本科专业**,覆盖了全国 **30 个省、自治区和直辖市**」;「**不包括成人高等教育、军事院校和港澳台院校**的毕业生」;「以**电子邮件**方式发放答题邀请函……答题时间为 **10~30 分钟**」;「答题通过电子问卷客户端实现,**未被邀请的答题被视为无效**」。
  - **关键缺口(三席独立复现,零命中)**:全书检索「回收率」「应答率」「答题率」「响应率」「回复率」**全部 0 命中**——**13.5 万确无分母**。
  - **自我选择偏差的处理(比原稿更尖锐的版本)**:逐字「本研究对答题和未答题的样本进行了检验,**没有发现存在自我选择性样本偏差问题(Self-selection Bias)**」——**无变量、无检验方法、无 p 值**;而该句**自己的脚注**就把这一风险定义为「可能存在**就业的毕业生更容易选择参与答题,而没有就业的学生可能不愿意参加答题**」。即:**麦可思逐字点名了这一风险,然后无任何检验细节地宣称它不存在。**
  - **加权方式**:逐字「本研究采用权数加以修正(即对回收的全国总样本,基于学历、地区、院校类型、专业的实际分布比例进行**再抽样**)」;附表 1 区域分布加权后与目标**完全相等**(东部 38.5/38.5、中部 26.7/26.7、西部 25.4/25.4、东北 9.4/9.4)。
  - **利益披露为零**:全书 20,809 行中「客户」二字仅出现一次(「问卷客户端」),「委托」「合作高校」「付费」「签约高校」「利益冲突」「资助」**零命中**,与披露相关的只有一条「法律声明」(版权声明)。**即「未见披露」不是「找得不细」,是文本级为零。**
- **证据分级**:多源证实(三席各自下载研报 PDF 与技术报告 PDF 逐行核对,数字与引文完全一致;两席独立复现「回收率」零命中)
- **不得这样写**:
  - ❌「2018 年**主营业务收入** 110,752,232.01 元,**其中**数据监测类 96,886,518.62 元(占营业收入 85.36%)」——**「其中」关系不成立**。两个分项之和恰为 113,501,829.94 = **营业收入**。三席一致要求改写。
  - ❌「新三板挂牌(833861,2015-10)」用现在时——**2020 年已终止挂牌**。这不是减弱而是加强论点。
  - ❌ 把研报写成「麦可思年报显示」——载体是**新三板智库《寻找新三板精选层标的专题报告(二十三)》(2019-11-07,研究员麦棋昌、方俊杰)**,是**卖方推介性质**的专题研究报告(自述数据来源为「公司年报」,正文含「风险提示」「客户不应以本报告取代其独立判断」等免责条款),**不是审计报表或交易所披露文件**。用它论证「利益相关」时须标明这是一份为拉抬标的而写的推介材料。
  - ❌「加权后区域分布与实际**分毫不差**……这是『再抽样』而非事后分层加权的特征」——**统计学推理有误**。事后分层加权按构造同样会使**加权维度**的边际分布与目标完全吻合,因此「分毫不差」并不能区分二者;判定其为再抽样的**唯一依据是技术报告自己写的「再抽样」三字**。另:「意味着可能丢弃了部分回收样本」是推测——有放回再抽样只会复制不会丢弃。**更有说服力的替代写法**:「分毫不差」只对**加权维度**成立,而**非加权维度**的省份表(附表 2)并不吻合(北京 2.6 vs 2.8、河北 4.9 vs 4.7)——这个对照本身就是加权维度与非加权维度的教科书式区分。
  - ❌「**不存在**任何对麦可思数据做效度检验或与行政数据交叉验证的学术研究」——这是**否定性命题**,三席均因检索额度/无 CNKI 访问而只能确认「未检索到」。行文写「**未检索到**」而非「不存在」。
  - ❌ 把技术报告称加权基准来自「中华人民共和国国家统计局网站」当作无问题——本科分专业/分院校类型的实际分布通常出自**教育部教育统计**,此处基准来源标注本身存疑,可作为一处附带质疑。
- **利益相关**:**麦可思是营利性商业调查公司**,创始人持股 61.61%,收入 85% 来自向高校、院系、教育厅局销售的数据监测服务;高校既是其付费客户又是其样本来源;2020 年退市后无强制披露义务。**其全部数据均属商业调查,不可与官方统计并列。**
- **待 Round 3**:否(两份一手件三席均取得并逐行核对)

---

## [G55] 红黄绿牌:第一判据未定义、定义被改写、规则一年内变更

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **原始定义(《2023 年中国本科生就业报告》技术报告第 43–44 页,三席逐字核对一致)**:「**红牌专业指的是失业量较大**,毕业去向落实率、薪资和就业满意度综合较低的专业。**黄牌专业指的是除红牌专业外,失业量较大**,毕业去向落实率、薪资和就业满意度综合较低的专业。**绿牌专业指的是失业量较小**,毕业去向落实率、薪资和就业满意度综合较高的专业,为需求增长型专业。」——**「失业量」是首要判据**。
  - **不可复现性(三席独立复现,可加粗写)**:① 全书 235 页中「**权重**」「**阈值**」「**评定标准**」三词命中数**均为 0**,四判据的合成规则完全不可复现;② 「**失业量**」全书仅出现 4 次(第 44 页定义段 3 次、第 195 页概述 1 次)且**从未被定义**——技术报告与名词解释里有「毕业去向落实率」「工作与专业相关度」「就业满意度」的分子分母公式,**唯独『失业量』没有任何计算口径**。即**红黄绿牌的第一判据本身是一个未定义量**;③ 第 195 页自述判据为「失业量、毕业去向落实率、薪资和就业满意度**等**就业指标」——一个「等」字使**判据集合本身也是开放的**;④ **红牌与黄牌的定义文字除「除红牌专业外」五字外完全相同**,本身就说明二者无可操作的区分标准。
  - **麦可思自己的限定语(建议一并引用)**:定义段后接「红黄绿牌专业反映的是**全国总体情况,各省区、各高校情况可能会有差别**」——这句本身就是「不可外推到个人」的发布方自认。
  - **定义在传播中已改**:标注「稿件来源:**麦可思研究**」的传播稿(搜狐,2026-06-25)把红牌重新定义为「在**就业落实率、薪资水平与就业满意度**等方面综合表现相对较低,同时在**市场需求端呈现减少或增长缓慢**趋势的专业」——**全文不出现「失业量」三字**,首要判据被替换为「市场需求端趋势」。该文所列 2026 年本科红牌六专业(绘画、音乐表演、美术学、文化产业管理、劳动与社会保障、城乡规划)与通行版本一致,说明这是**随通稿一起流通的权威版本改写,不是个别小编笔误**。
  - **规则变更无说明(时间线锁定为 1 年)**:2023 版书内逐字写「部分近年来新增数量较多的专业(如**人工智能、数据科学与大数据技术、机器人工程**)由于**尚无成规模、成趋势的毕业生就业数据,暂未包括在内**」;而 **2024 版(2023 届)榜单中机器人工程即已进入绿牌**(2024 年本科绿牌:微电子科学与工程、电气工程及其自动化、新能源科学与工程、能源与动力工程、机械电子工程、**机器人工程**),并在 2025 年继续在榜、2026 年出榜。**即:2023 年 6 月的书里说「尚无成规模数据,暂未包括」,仅隔一年同一专业就直接上了绿牌榜,规则变更无任何说明。**
- **证据分级**:定义与不可复现性为**多源证实**(三席各自从同一 PDF 逐字提取并独立复现零命中检索);2024/2025/2026 榜单为**商业调查 + 二手转述**(三席均未取得 2024–2026 版原书,依赖高校/媒体转载)
- **不得这样写**:
  - ❌「2026 年**媒体通稿**把红牌改写为……」/ 标题作「定义**在传播中被偷换**」——**归属未定,不可坐实**。一席指出三家 2026 年报道给出三套彼此不同的措辞(搜狐/新浪财经/网易各异),更像各家改写;两席则查到搜狐该文标注「稿件来源:麦可思研究」,指向发布方自己的传播渠道。**但三席均未取得《2026 年中国本科生就业报告》原书,无法判定原书是否已改口径。** 锁定写法:「2026 年公开传播中的红/绿牌定义已普遍不含『失业量』,该改写至少出现在标注『稿件来源:麦可思研究』的传播稿中;**但因未取得 2026 年原书,无法断言原书口径已变,亦不应写成『媒体偷换』。**」——对准大学生而言「谁改的口径」影响是否该信任榜单本身,必须留白而非坐实。
  - ❌「2025 版(2024 届)机器人工程直接进了绿牌」——**时间线错一年,且错在削弱论点的方向**。是 **2024 版(2023 届)**即已进榜,反转周期是 **1 年不是 2 年**。
  - ❌「**不存在**任何对红黄绿牌预测效度的回溯检验研究」——三席均受检索额度/无 CNKI 访问限制,只能写「**未检索到**」。
- **利益相关**:同 G54——麦可思是商业调查公司,红黄绿牌榜是其最主要的公共传播产品与获客入口,「专业风险」叙事与其商业利益直接相关。
- **待 Round 3**:**是**。① 2026 年红牌定义的改写归属(原书 vs 传播稿)需取得《2026 年中国本科生就业报告》原书或麦可思官方发布页确认;② 2024/2025/2026 三版绿牌名单全部为二手转载,需至少一条可回溯的一手或官方转载源。

---

## [G56] 蛛网反转:2010 年计算机是红牌,2026 年计算机跌出高薪前十

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **近五年本科绿牌专业(《2023 年中国本科生就业报告》表 12-7,经三席分别用 pdftotext -bbox 坐标级重排 + 书内自述交叉校验后的正确版本)**:
    - **2019(7 个)**:信息安全、软件工程、网络工程、物联网工程、数字媒体技术、**通信工程**、**数字媒体艺术**
    - **2020(7 个)**:信息安全、软件工程、信息工程、网络工程、计算机科学与技术、**数字媒体艺术**、**电气工程及其自动化**
    - **2021(6 个)**:信息安全、软件工程、信息工程、网络工程、数字媒体技术、**电气工程及其自动化**
    - **2022(6 个)**:信息安全、网络工程、信息工程、微电子科学与工程、数字媒体技术、能源与动力工程(**无**电气工程及其自动化)
    - **2023(6 个)**:信息工程、微电子科学与工程、电气工程及其自动化、能源与动力工程、道路桥梁与渡河工程、机械电子工程
    - **书内自述作为交叉校验(四条约束,只有上述排法能同时满足)**:「近五年进入绿牌名单的专业共 **14 个**」;「次数最多的是**网络工程、信息安全、信息工程(均为 4 次)**,其后是**电气工程及其自动化、软件工程、数字媒体技术(均为 3 次)**」;「其中网络工程、信息安全、软件工程、数字媒体技术、物联网工程、计算机科学与技术 **6 个专业均属于计算机类专业**」;「这些专业**除数字媒体艺术之外,均属于工学门类**」。
  - **2010 年的反转证据(本条最有力的论据)**:2010 年本科**红牌**十专业为动画、法学、生物技术、生物科学与工程、数学与应用数学、体育教育、生物工程、**计算机科学与技术**、英语、**国际经济与贸易**;2011 年名单与 2010 年**完全相同**(《中国青年报》2015-08-11 逐字:「2011 年的预警榜与前一年相比,『红牌』专业从类目到排序均一模一样」;同文另称「计算机科学与技术、国际经济与贸易、美术学 3 次上榜」)。
  - **红榜绿榜同时反转(建议补入,比只讲红榜有力得多)**:同一份 2010 年榜单的**绿牌**是地质工程、港口航道与海岸工程、船舶与海洋工程、石油工程、采矿工程、油气储运工程、矿物加工工程、过程装备与控制工程、水文与水资源工程——**清一色资源开采类,十六年后正是被劝退最狠的一批**。
  - **当年红牌的机械性偏置(必须写的限定)**:当年红牌是「失业量较大、就业率较低、薪资较低的专业中的**前 10 个**」,即一份**按绝对失业人数排的 Top10**。计算机科学与技术当年(及今天)都是全国招生规模最大的专业之一,「失业量」判据**对大专业有机械性偏置**。这一点不削弱「蛛网会反转」的论点,反而把「红牌 ≠ 该专业不好」讲得更准确,且直接呼应 G55 的「失业量从未被定义」。
  - **2026 年的另一端**:2026 年本科绿牌六个全为工科(电气工程及其自动化、微电子科学与工程、自动化、能源与动力工程、车辆工程、新能源科学与工程);2025 届本科月收入前十为微电子科学与工程(榜首 **7,814 元**)、电子科学与技术(7,752 元)、自动化、**信息安全**、光电信息科学与工程、采矿工程、机械工程、测控技术与仪器、材料科学与工程、通信工程(区间 7,249–7,814 元);2025 届本科平均月收入 **6,435 元**。
  - **「落实率含升学,不是纯失业指标」(一手可证)**:技术报告第 12 页逐字「毕业去向落实率 = 已就业本科毕业生数 / 本科毕业生总数。其中已就业人群包括『受雇工作』、国内外读研等五类」;第 9 页毕业去向七分类明确把「国内外读研」与「受雇工作」并列计入。
  - **两面呈现(一手可证)**:表 12-6 载计算机类 2022 届月收入 **6,863 元** vs 本科平均 5,990 元;工作与专业相关度 **77%** vs 本科平均 74%。
  - **供给侧数字(须带时间戳与出处)**:截至 **2025 年 11 月**(**教育部阳光高考平台**口径,不是麦可思),开设计算机科学与技术的高校 **955 所**、软件工程 **661 所**;「掌上高考」2026-06 已列 960 所,**该数在漂移**。
- **证据分级**:表 12-7 为**多源证实**(三席各自用坐标级/列位重排独立还原,结论完全一致,且均以书内自述四条约束交叉校验);2010/2011 年红绿牌名单为**方向存争→转为多源证实**(三席分别用《中国青年报》2015 年统计、2010 年当期多家报道、名单转载交叉确认,但**三席均未取得 2010/2011 年蓝皮书原书**);2025/2026 年数字为**商业调查 + 二手转述**
- **不得这样写**:
  - ❌ 采集稿的五年绿牌序列——**五列中四列错**,三席独立还原后结论一致:2019 列误加「电气工程及其自动化」、漏「通信工程」与「数字媒体艺术」(**「通信工程」在原表述中整个消失了**);2020 列误加「数字媒体技术」、漏「数字媒体艺术」与「电气工程及其自动化」;2021 列把「电气工程及其自动化」误写成「数字媒体艺术」;2022 列误加「电气工程及其自动化」。原稿版本只有 13 个不重复专业、数字媒体技术 4 次,与书内自述(14 个 / 3 次)**自相矛盾,可直接判为抄错**。**必须整表替换。**
  - ❌ 写「麦可思原书载明」2010/2011 年名单——三席均未取得原书,应写「据《中国青年报》2015 年对麦可思历年榜单的统计与多份当年名单转载」。
  - ❌「计算机类『毕业五年后月收入 **14,090 元仍**居主要专业类第一』」——**须加届次并删「仍」字**。正确表述:「计算机类 **2019 届**毕业生**毕业五年后**(2024 年调查)月收入 14,090 元,居本科主要专业类第一(电子信息类 13,584 元次之),数据出自《2025 年中国本科生就业报告》。」理由:① 14,090 是 2019 届的队列数据,与同句并列的「2024 届 82.4%」**不是同一批人**;② 麦可思 2026-07 已发布 2020 届五年后数据(电子信息类 13,992 元、能源动力类 13,022 元),**14,090 元这个「第一」已是上一版口径**,计算机类是否仍居第一未获证实。
  - ❌ 把 82.4% / 61 个主要专业类倒数第 11 / 全国本科平均 86.7% / 历史学类 87.2% / 外国语言文学类 86.9% 写成已核数据——**三席均未取得《2025 年中国本科生就业报告》原书**,全部为媒体转述(内部自洽:86.7 − 82.4 = 4.3 个百分点)。须标「转引自媒体报道的《2025 年中国本科生就业报告》数据」。
  - ❌「**计算机跌出前十**」——**2025 届月收入前十中第 4 位的「信息安全」本身就是计算机类专业**。原稿写「**计算机科学与技术、软件工程**首次跌出前十」是准确的,**务必保持这个精确措辞,不要采信媒体标题的『计算机跌出前十』**。
  - ❌「955 所 / 661 所」不标源不标时间——出自教育部阳光高考平台、截至 2025 年 11 月。
  - ❌「两专业毕业生规模**均**在 10 万人以上」——来源本身就有分歧,部分转述写的是「两个专业每年的毕业生**总数合计**超过 10 万人」,量级差一倍。**只保留各来源都支持的下限说法:「两专业年毕业生规模合计逾 10 万人」。**
  - ❌「十五年前」——2010 年榜基于 2009 届毕业生,应写「**约十六年前**」或直接写「2010 年」。
- **利益相关**:同 G54/G55(麦可思商业调查);955/661 所出自教育部阳光高考平台(官方)。
- **待 Round 3**:**是**。① 2010/2011 年红牌与绿牌名单是本篇「蛛网反转」论证的核心历史锚点,但**三席全部只有二手**(《中国青年报》2015 年回顾统计 + 当年报道转载),需反证搜索席寻找 2010/2011 年蓝皮书原书或麦可思官方发布页;② 82.4% 及配套的 86.7% / 87.2% / 86.9% / 倒数第 11 全部为媒体转述,若要承重须补一手。

---

## ⚠️ [G57] 三条流传数字:两条禁用,一条可救活但须整句改写

- **判决**:**REFUTED**(1/3 席整条判 REFUTED;另两席按子项分判,其中 (b) 三席一致 REFUTED、(a) 2/3 席 REFUTED、「竞争比 200:1」3/3 席 REFUTED。按最严处理)
- **锁定表述**:
  - **(a) 计算机对口率下滑——原表述禁用**。可写的只有:「麦可思体系中该指标的正式名称是『**工作与专业相关度**』,其一手定义(2023 技术报告)为『**受雇全职工作并且与专业相关的毕业生人数 / 受雇全职工作的毕业生人数**』——**分母是已受雇全职者,不是全体毕业生**,也不是行政意义上的『对口就业率』。」一手可核的对照数是:**计算机类 2022 届工作与专业相关度 77%,本科平均 74%**(表 12-6)。
  - **(b) 简历/面试/offer 率——三条全部禁用**。可写的只有其**方法论观察**:「智联《大学生就业力调研报告》的官方口径逐字为『截至 4 月中旬,**在有求职计划的应届毕业生中**,47.8% 已获得 offer』——**分母是人,且是筛过的人**;而『offer 率不足 8%』若成立只可能是『简历投递 → offer』的**份次转化率**,分母是简历份数。**两者分母一个是人、一个是简历份数,量级相差近六倍,被当成同一件事传播,即是分母偷换。**」最尖锐的证据:新浪同一篇文章里,「最终 offer 率不足 8%」与「今年春招专科生的 offer 率是 56%,反而高于本科生的 45% 和硕博生的 40%」**并排出现——同一篇稿子里两个相差 6 倍的『offer 率』被当成同一件事**。
  - **(c) 教师招聘缩减——只可写湖北一省,且须整句改写**:「以湖北省为例,**省级统一公开招聘中小学教师的计划数从 2025 年的 5,799 名降至 2026 年的 2,740 名,一年减少 52.8%**(2,740 / 5,799 = 47.25%)。」两个数字均出自省级官方招聘公告(《湖北省 2025 年中小学教师公开招聘公告》,湖北省教育厅、湖北省人力资源和社会保障厅,2025-03-13;《湖北省 2026 年中小学教师公开招聘公告》,湖北省教育厅,2026-04-15)。**必须加的口径限定**:这是**省级统一公开招聘计划数**,不含特岗计划、公费师范生履约、市县自主招聘与编外聘用,因此只能写「**湖北省统招计划腰斩**」,**不能写「湖北教师招聘总量减半」**。
- **证据分级**:(a) **未验证/伪流传**;(b) **未验证/伪流传**;(c) 湖北两个数为**单源已核**(两席分别定位到省级官方公告,一席未取到)
- **不得这样写(逐条,含溯源记录)**:
  - ❌⚠️「计算机类**对口率**从 2020 届 **76%** 降至 2024 届 **62%**(五年降 14 个百分点)」——**禁用**。溯源记录:三席分别用「一手 PDF 全书检索」「精确串多引擎检索(Bing/DuckDuckGo/Mojeek/Sogou)」「麦可思官方口径/公众号/官网检索」「传播链回溯」四类角度追溯,**均未触及一手**;查到的全部载体是自媒体,**发文日期高度集中在 2026-07-21 前后同一波**(典型的单点起源级联),无一给出报告名与页码。**判定性反证**:麦可思体系里**根本不存在「专业对口率」这个指标名**——一个连指标名都不对的数字不可能来自蓝皮书原文;且一手数据与该曲线不符(计算机类 2022 届工作与专业相关度为 77%,若 2020 届为 76%,则两年内跌到 62% 属异常断崖,无任何一手支撑)。
    - ⚠️**注意**:一席另查到一组**指标名正确但主语不同**的数字——麦可思研究《别了,专业对口!》(2026-05-12)称**计算机科学与技术专业**(不是专业类)的工作与专业相关度由 2020 届 76% 降至 2024 届 62%,同篇另有软件工程 78%→65%、信息安全 79%→69%、网络工程 73%→64%、物联网工程 67%→58%;《2026 年中国本科生就业报告》另称计算机**类** 2025 届 62%、较 2021 届 78% 降 16 个百分点。**这两组数「终点都是 62%」,极易被混着用**,且均为自媒体/媒体转载、未取得原书。**结论:原表述(把一个专业说成一个专业类)禁用;替代数字属单源二手,不得承重,须送 Round 3。**
  - ❌⚠️「1 个岗位 **17.2 份简历** / 投 **150–200 份**换 1 次面试 / **offer 率不足 8%**」——**三席一致禁用**。溯源记录:最靠前的载体是新浪财经转载的自媒体文《2026 年,1270 万毕业生的天崩开局》(2026-05-23),另见新东方网、知乎、CSDN(最早可见 2026-03),**全部写作「智联招聘的数据显示」,无报告名、无发布日、无页码**。部分转载进一步指名《2026 春节后首周就业市场景气报告》,但**该报告的实际指标体系是 CIER 景气指数(= 市场招聘需求人数 / 市场求职申请人数),其中并无「17.2 份简历」或任何按岗位统计的简历数,也不报告应届生 offer 率**——即这是一次**指名到具体报告的错误归因,比无名归因更该禁用**。同一批文章内部还在滚雪球:同组数字有写成「热门岗位竞争比突破 2000:1」「文科专业供需比 1:42」「热门赛道 60:1」的。
  - ❌⚠️「**多地**教师招聘缩减 50%+」——**「多地」不成立**,三席合计只坐实**湖北一省**。江西「2023 年 7,821 名 → 2026 年 1,190 名(降 84.8%)」**仅见自媒体与媒体转述,未追到江西省教育厅原公告,不可用**。
  - ❌⚠️「教师招聘**竞争比 200:1**」——**三席一致禁用**。「部分岗位甚至超过 200 比 1」「热门学科普遍 80 比 1」只见于自媒体解说,**无任何省级人社/教育部门的报名人数与计划数汇总数据支撑**。
- **利益相关**:上述流传数字的载体均为自媒体与内容平台,其收益来自「就业惨烈」叙事的流量;智联招聘与猎聘是商业招聘平台,其口径服务于自身产品叙事。
- **待 Round 3**:**是(高优先)**。① 湖北 5,799 → 2,740 两份省级公告需反证搜索席直接落到 jyt.hubei.gov.cn 原页(目前两席定位、一席未取到);② 麦可思《别了,专业对口!》(2026-05-12)的 76%→62% 组数据需确认是否存在于麦可思官方渠道原文,以及主语究竟是「计算机科学与技术专业」还是「计算机类」;③ 江西教师招聘 7,821 → 1,190 需追省级公告,追不到则并入禁用清单。

---

## [G58] 招聘平台数据的构念问题

- **判决**:CORRECTED(3/3 票,三席均给 confidence=medium)
- **锁定表述**:
  - **智联 offer 率的分母(一手逐字,三席一致)**:《大学生就业力调研报告》——调研窗口为当年 **3 月下旬至 4 月中旬**(春招中期);逐字「截至 4 月中旬,**在有求职计划的应届毕业生中**,47.8% 已获得 offer」。历年:2023 年 50.4%、2022 年 46.7%;分学历大专 56.6% / 本科 45.4% / 硕博 44.4%。**该分母已排除升学、考公备考、慢就业者,因此不能反推就业率——这一条可以写死。**
  - **智联 2026 年行业增速(必须写清是行业职位数,不是专业)**:据智联招聘《2026 年大学生就业前景研判及高考志愿填报攻略》(2026-06-16 发布)——**2026 年 1–5 月,应届生招聘职位数同比增长**:机器人行业 **83.8%**、新材料 **60.1%**、光电子 **30.7%**、航空/航天/船舶制造 **29.7%**、汽车零部件 **28.4%**、人工智能 **24.4%**。
  - **报告自带的反内卷限定语(必须一并引用)**:「增速大不等于岗位总量最大——2026 年 1–5 月应届生招聘需求**绝对量**较大的行业仍包括互联网、培训/辅导服务、医药制造、电子/半导体/集成电路等。」**文章若只引增速榜而不引这句,等于替智联做了它自己都没做的推断。**
  - **猎聘增速(《2026 届大学生校招全景洞察》,2026-05-28)**:原文「新发校招职位同比增长 TOP15 行业中,**电子商务以 1165.94% 的增速遥遥领先**,银行、保险、通信设备等行业增速均超 70%,电子商务、**人工智能(+57.98%)**、**新能源(+32.12%)** 三大新质生产力行业增速亮眼」。**分母(上年该行业在猎聘的新发职位数)从未公开**,样本、口径、统计周期均无披露。
  - **三条构念警告(三席一致认定全部准确,予以锁定)**:
    1. 「高薪专业排行」来自**岗位挂出薪资/平台简历薪资(要约端价格)**,麦可思「月收入」来自**毕业生自报实得(实现端价格)**——两者在同一篇文章中并列或相减都会产生伪结论。
    2. 「院校薪酬排行」的分母是**在该平台投递或被录用的该校毕业生**,平台用户结构失衡会**系统性抬高名校排名**。
    3. 1165.94% 这类增速在低基数下几乎必然产生,**不能读作行业真实用工增长**;同一榜单里电子商务 1165.94% 与人工智能 57.98% 并列呈现,本身就自证了这是平台侧基数效应——若电商用工真在一年内涨 12 倍,它会是宏观经济事件而不是一张招聘网站的榜单。
    4. **(建议补的第四条)** 智联的分母是**平台用户**,麦可思的分母是**受邀毕业生**,两者**都不是全体毕业生**——因此「哪个更准」是个伪问题,正确的说法是**它们各自只对自己的用户池有效**。
  - **最有说服力的对照(建议用)**:智联榜首电子科学与技术 8,064 元 vs 麦可思 2025 届同专业口径 7,752 元——**两个「高薪专业榜」的榜首专业数值就差 300 余元**,正因为一个是平台岗位/简历标薪、一个是毕业生自报实得月收入。
- **证据分级**:47.8% 及其分母为**多源证实**(三席均取得逐字原文);行业增速为**商业调查**(二席经上观新闻/湖南日报/红星新闻等逐字转述交叉一致,**三席均未取得原始 PDF**);猎聘数字为**商业调查 + 单源转述**
- **不得这样写**:
  - ❌「TOP50 高薪专业中 **43 个为工学**」「TOP50 高薪院校中 **47 所为双一流**」——**「47 所双一流」三席均未找到独立佐证,不用**;「43 个工学」仅一席找到来源支持(配榜首电子科学与技术 8,064 元、智能科学与技术 7,956 元),**若用须标注单一来源**。
  - ❌ 把「机器人 83.8%、新材料 60.1%、人工智能 24.4%」当作**专业维度**的招聘增速——是**行业职位数同比**,不是专业、不是招聘人数。**把行业增速当专业推荐依据,正是本文要批判的构念滑移,写的时候别自己踩进去。**
  - ❌「银行 **251.39%**、保险 **145.74%**」——**猎聘原文只写「银行、保险、通信设备等行业增速均超 70%」,无这两个具体数**。须删去或标注未核实。
  - ❌「(智联报告)**未公开**有效样本量、抽样方式、院校层次配额」——三席均未取得原始 PDF(智联未在官网公开下载),只能确认「**在所有可及的官方转载与摘要中均未见样本量**」。改写为:「公开可及的发布稿与转载中均未披露有效样本量与抽样方式。」
  - ❌ 把「样本来自智联平台用户 + 自愿填答的双重自选择」写成报告自述——**这是推断,须以推断语气写**。
  - ❌ 把「低基数 + 平台自身销售拓展」写成已证事实——同样是合理推断。
- **利益相关**:**智联招聘与猎聘均为商业招聘平台**,其榜单是获客与品牌传播产品;数据分母为自家平台用户,无外部审计,方法论未披露。**属商业调查,方向可参考、程度不承重,绝不可与麦可思或官方数据并列相减。**
- **待 Round 3**:**是(低优先)**。智联《2026 年大学生就业前景研判及高考志愿填报攻略》与猎聘《2026 届大学生校招全景洞察》两份原始报告三席均未取得,所有数字为媒体转述;若文章要引用具体百分比,须补一手,否则只保留构念警告部分。

---

## [G59] 就业数据造假:官方承认、专项核查、以及从未公布的查实结果

- **判决**:CORRECTED(3/3 票)
- **锁定表述**:
  - **官方承认与核查(教育部 2023-08-04《教育部派出工作组赴各省开展专项核查 严查高校毕业生就业数据弄虚作假》,正确 URL 尾号 **1072396**,三席逐字核对一致)**:
    - 「对经核实存在**虚假签约、虚假证明**等违规行为的,责成有关部门依规依纪严肃处理,并追究相关高校和人员责任**,切实维护高校毕业生就业合法权益**。」(原稿引文在「责任」处截断)
    - 「**重点核查灵活就业等相关数据**,以『**零容忍**』的态度严肃查处就业违规行为。」
    - 「**8 月起,还将委托国家统计局和第三方调查机构在全国范围内开展 2023 届高校毕业生去向落实情况抽样调查。**」
    - 原文明写「严格执行就业工作『**四不准**』『**三不得**』规定」并完整列出七条。**三不得逐字**:「不得不切实际向高校和学院提去向落实率具体指标;不得层层加码向辅导员摊派就业任务;不得将单一的去向落实率指标与就业工作人员或者辅导员的绩效考核、评优等挂钩」——**这三条恰是教育部自己承认存在指标摊派,比四不准更有力**。第四不准原文为「不准将**毕业生**顶岗实习、见习证明材料作为就业证明材料」。
  - **最硬的空白(三席独立穷尽检索一致)**:以多角度检索「就业数据造假 处理结果 通报」「高校 就业率 造假 处分 名单」,返回结果**全部是同一篇 2023-08-04 稿件的转载**(教育部官网、国家大学生就业服务平台重复转载、各省转发、举报电话邮箱表、截止 8 月 31 日),**未出现任何一份点名通报、查实数量或处理结果公告**。「**承认有假、从未公布查出多少假**」可以直接写。
  - **抽样调查:制度公开,只有结果不公开(须拆成两层)**:
    - 制度层:《全国普通高校毕业生就业状况统计调查制度》(国家统计局批准,2020-12-16)公开挂网,载明「调查对象为全国普通高校普通本专科和研究生毕业生,以及录用该毕业生就业的用人单位」「采用**非全面调查的抽样调查方法**」「由教育部高校学生司、全国高等学校学生信息咨询与就业指导中心统一组织,**委托第三方机构具体实施**」;**最硬的一句**:「本制度有关结果将通过**函件形式反馈 31 个省(区、市)和新疆生产建设兵团教育行政部门**。」——**制度设计上就写明了不面向公众。**
    - 执行层:教育部 2022-06-06 另有一句「从 2020 年起,教育部已连续两年委托国家统计局对全国和各地高校毕业生就业状况开展抽样调查」。
    - 结论:**制度公开、连续执行至少六年、结果只以函件反馈行政部门,从未向社会发布。**
  - **学术调查的对照(岳昌君、冯沁雪、辛晓佳、邱文琪《中国高校毕业生就业趋势研究报告:来自 2003—2021 年调查数据》,《华东师范大学学报(教育科学版)》2023 年第 41 卷第 9 期第 138–154 页,doi:10.16382/j.cnki.1000-5560.2023.09.010)**:
    - 2021 年轮次:**34 所高校、20,269 人**(2003 年起每两年一次共 10 轮,样本高校 28–45 所、样本量 15,060–21,753 人;学历构成专科 14.8%、本科 68.9%、硕士 15.1%、博士 1.2%)。
    - **2021 年「已落实」76.5% = 已确定单位 32.1% + 升学 33.0% + 灵活就业 11.4%**(三项相加恰好闭合;待就业 14.0%,平均起薪 7,025 元)。
    - 摘要自述:「正规就业比例创新低,升学比例持续走高;落实率下滑,待就业率回升。」
    - **可承重的表述**:「**在离校前这个时点上,已确定单位者只有 32.1%。**」
  - **灵活就业口径撕裂**:麦可思一手(2023 技术报告第 134 页逐字)——「2022 届有 **4.6%** 的本科毕业生在毕业半年后选择灵活就业,其中包括 **1.4%** 选择受雇半职工作,**2.0%** 选择自由职业,**1.2%** 选择自主创业」;同书第 9 页「受雇全职工作指平均每周工作 32 小时或以上」,即**麦可思的灵活就业不含受雇全职**。官方端:全国高等学校学生信息咨询与就业指导中心口径「**2020 届全国高校毕业生的灵活就业占比 16.9%,2021 届 16.25%**」(另附「天津、河北、山西三省市 2021 届毕业生灵活就业占比超过 30%」)。
  - **3–4 倍缺口的可证实解释(按强度排序,替换原推定)**:① **行政激励**——教育部自己在 2023-08-04 通稿里点名「**重点核查灵活就业等相关数据**」,等于官方承认灵活就业这一栏是造假高发区(**最有力且最有一手依据,应写在最前面**);② **分母不同**——16.9%/16.25% 是全国高校毕业生(**含高职专科与研究生**),麦可思 4.6% 只是**本科**,而高职灵活就业比例显著更高;③ **数据生成方式不同**——官方是高校填报的行政数据,麦可思是毕业生自报问卷。
- **证据分级**:教育部 2023-08-04 通稿为**多源证实**(三席逐字一致);统计调查制度与岳昌君论文为**单源已核**;官方灵活就业 16.9%/16.25% 为**单源已核**(二席取到发布方转载,一席未取到);麦可思 4.6% 为**单源已核**(一手 PDF)
- **不得这样写**:
  - ❌ 引用 URL 尾号 **1072471**——**该 URL 在教育部站上返回「页面不存在!」,Wayback 无任何快照(从未存在)**,照抄会让读者无法自核。正确尾号为 **1072396**。
  - ❌ 只列「四不准」而略去「三不得」——漏掉的正是最能说明行政压力传导的部分,**是实质损失**。
  - ❌ 第四不准漏「**毕业生**」二字。
  - ❌ 把「每年 9 月初,教育部委托国家统计局开展毕业生就业状况抽样调查,**结果将向各地通报**」归给教学厅函〔2021〕19 号——**归属存疑**:一席用 Wayback CDX 遍历 moe.gov.cn 2021 年该栏目全目录,取到 12/15/17/20/21/22/31 号,**未见 19 号**,教育部现网两个候选 URL 均返回「页面不存在」;另一席在 19 号下只核到「9 月初,教育部将会同国家统计局对就业统计工作开展抽样调查,向毕业生本人和用人单位核实就业情况」,**未核到「结果将向各地通报」原句**;第三席经山西省教育厅转发件核到该原句。**处理方式:改用《全国普通高校毕业生就业状况统计调查制度》(国家统计局,2020-12-16)的「本制度有关结果将通过函件形式反馈 31 个省(区、市)……教育行政部门」——这句更硬,能把「存在但不公开」从推断升级为制度白纸黑字**,且不依赖 19 号。
  - ❌「2021 年『已落实』比例(**已确定单位 + 升学**)76.5%」——**32.1 + 33.0 = 65.1,不等于 76.5**,必须补上**灵活就业 11.4%**。这个错误方向很坏:它把「灵活就业」从画面里抹掉了,**而灵活就业正是本文 E 段要攻击的口径争议核心**——等于在批判灵活就业注水的同一篇文章里,自己把 11.4 个百分点悄悄并进了「正规去向」。
  - ❌ 把 76.5% 与 86% 直接相减对比——**时点不同**(离校前 vs 毕业半年后 vs 教育部的 8 月 31 日/12 月 31 日两个统计时点)、**样本框不同**(30 余所高校 vs 13.5 万人邀请制)、**学历构成不同**(含专科硕博 vs 纯本科)。差距里有相当大一块只是**时点差**。「拆开报 vs 合并报」的论点成立,但要说成「两种呈现方式给读者的画面不同」,**不要说成「两个数互相证伪」**。
  - ❌「调查时点为 **6–7 月**学生离校前」——两席未在可及页面中核到该具体月份,改用不依赖具体月份的「**离校前**」。
  - ❌ 把「官方含就业编码 12 而麦可思算作受雇全职」当作缺口的主因——**方向可能相反**:麦可思的 4.6% **已经把自主创业(1.2%)算了进去**,而官方毕业去向登记里自主创业是与灵活就业并列的独立类别;即在这一维度上麦可思口径反而更宽,**定义差异不足以解释 3–4 倍的差距**。改用上述三条可证实解释。
  - ❌「**不存在**任何点名通报」——三席均因检索额度限制,写「**未见公开通报**」。
- **利益相关**:教育部既是造假的核查方,也是造假压力的制度来源(指标考核);麦可思为商业调查公司(见 G54)。
- **待 Round 3**:**是**。① 官方灵活就业 16.9% / 16.25% 是「口径撕裂」论证的官方侧唯一支点,目前只有发布方转载(学职平台/中国就业网),需落到全国高等学校学生信息咨询与就业指导中心原始发布;② 教学厅函〔2021〕19 号全文三席均未取到教育部原件(仅省级转发件),该文号在本篇 G48/G49/G59 三处承重,**必须补一手或全部标注「转引自省级转发件」**。

---

# 禁用清单

> 以下数字/表述经 Round 2 判为不可承重,**成文中一律不得出现**(除非作为「流传但溯源失败」的反面素材点名使用,且必须同时写明溯源过程)。

| # | 流传表述 | 为什么禁用 | 溯源试过哪些角度 |
|---|---|---|---|
| 1 | **「撤销、停招专业点数大幅超过增设专业点数,专业结构不断优化」**(标为教育部新闻稿逐字) | **伪引**。该句不在教育部 2025-04-22 与 2026-04-28 两份发布的任何一份中。真实原文分别是「专业调整优化力度进一步加大」与「本科专业结构进一步优化」。另一席指该句可见于教育部高教司**答记者问**,亦有媒体(新京报)标题化流传——**无论如何都不得标成「新闻稿逐字」** | 一席 curl 直取两份教育部原页全文并全文检索该句,**零命中**;另两席分别核对两页原文,给出真实对应句;答记者问版本经 gov.cn 转载页确认存在但性质不同 |
| 2 | 「计算机类**对口率**从 2020 届 **76%** 降至 2024 届 **62%**」 | 指标名不存在(麦可思叫「工作与专业相关度」)、主语错(把一个专业说成一个专业类)、与一手矛盾(计算机类 2022 届相关度为 77%)、传播链为单点起源级联 | ① 一手 PDF 全书检索 76%/62% 组合零命中;② 多引擎精确串检索(Bing / DuckDuckGo / Mojeek / Sogou),仅返回 2026-07-21 前后同批自媒体;③ 麦可思官网/公众号口径检索;④ 传播链回溯至最早发文日。**唯一疑似源头**《别了,专业对口!》(2026-05-12)讲的是「计算机科学与技术**专业**」,且亦未取得官方原文 |
| 3 | 「1 个岗位 **17.2 份简历**」 | 无任何可指名的智联报告;被指名的《2026 春节后首周就业市场景气报告》实际只含 CIER 景气指数(= 市场招聘需求人数 / 市场求职申请人数),**无按岗位统计的简历数** | 精确串检索、智联历年报告名逐一比对、沿转载链上溯至最早出现日期(2026-03 CSDN、2026-05 新浪财经转载);CIER 指标体系逐条核查 |
| 4 | 「投 **150–200 份**简历换 1 次面试」 | 同上,无源;同批文章内部数字滚雪球(另有「热门岗位竞争比突破 2000:1」「文科专业供需比 1:42」「热门赛道 60:1」等互斥版本) | 同上 |
| 5 | 「应届生 **offer 率不足 8%**」 | **分母偷换**。智联官方口径是「**在有求职计划的应届毕业生中** 47.8% 已获得 offer」(分母是人);「不足 8%」若成立只能是「简历 → offer」的份次转化率(分母是简历份数),量级差近六倍。最尖锐的证据:新浪同一篇文章里「offer 率不足 8%」与「专科 56% / 本科 45% / 硕博 40%」**并排出现** | 同上 + 智联《大学生就业力调研报告》逐字口径一手核对(三席一致) |
| 6 | 「**多地**教师招聘缩减 50%+」 | 「多地」不成立,三席合计只坐实**湖北一省**(5,799 → 2,740,−52.8%,两份省级公告);江西「7,821 → 1,190(−84.8%)」仅见自媒体与媒体转述 | 一席检索无任何省级教育厅/人社厅招聘计划汇总一手数据;两席定位到湖北省教育厅 2025 / 2026 两份公告;江西经检索仅见自媒体(狐狸先森讲升学规划、遇见转运官等),未追到省级原公告 |
| 7 | 教师招聘「**竞争比 200:1**」(及「热门学科普遍 80:1」) | 无任何省级人社/教育部门的报名人数与计划数汇总数据支撑,仅见自媒体解说 | 三席分别从省级人社/教育部门公告、招录公示、媒体报道三个角度检索,均无一手 |
| 8 | 猎聘「**银行 251.39%、保险 145.74%**」 | 猎聘原文只写「银行、保险、通信设备等行业增速**均超 70%**」,**无这两个具体数** | 一席取到《2026 届大学生校招全景洞察》(2026-05-28)报道原文逐字比对,两数不在其中 |
| 9 | 智联「**TOP50 高薪院校中 47 所为双一流**」 | 三席均未找到任何独立佐证 | 两席分别检索智联 2026 报告转载与原始 PDF 渠道(水滴研报需登录),未复现 |
| 10 | 「HRSA 预测 NP 2036 年充足率 **192%**(2026 年 132%、2031 年 164%)」 | 数字本身属实,但出自**已被官方取代的 2024-03 版**(基年 2021、含疫情数据)。现行 2025-12 版对应值为 **175%**(2028 年 126%、2033 年 152%) | 三席分别取得新旧两版 HRSA factsheet 一手 PDF 并逐格比对 |
| 11 | 「医师 2038 年**非都会区初级保健短缺 39%**」 | **HRSA 医师 factsheet 中查无此数**;官方配对是全科别口径的「非都会区 58% / 都会区 5%」 | 一席对该 PDF 全文 grep「39」「primary care」**零命中**;另两席分别核对原文段落,确认无此拆分 |
| 12 | 「NSI 医院 RN 离职率 **CY2022 峰值 27.1%**,降至 CY2025 17.6%」 | **年份错 + 方向错**。峰值是 CY2021;CY2025 的 17.6% 是**回升 1.2 个百分点**,不是继续下降 | 三席分别下载 NSI 2026 报告 PDF,逐格读出 CY21–CY25 两套序列并核对正文「a 1.2% increase」 |
| 13 | 「非私营 vs 私营工资**差 1.94 倍**」 | 真实值为 **1.81 倍**(129,441 ÷ 71,590)。1.94 的来源是**信息传输业内部**两口径之比(248,752 ÷ 128,166),被误当成全国总体之比;且与同条自述「私营不足非私营的 56%」内部矛盾 | 三席分别抓取统计局原页并 python 复算 |
| 14 | 「2026 年考研 343 万,**首次跌破 350 万**」 | 2020 年即为 341 万、2019 年 290 万,均低于 350 万。应写「2020 年以来最低」 | 三席分别核对历年序列;一席落到教育部 2019-12 与 2020-12 两篇原稿确认 341 万 / 377 万 |
| 15 | 「国考竞争比创新高,**招录计划本身也在扩张**」 | **方向说反了**。2026 年度计划招录 3.81 万人,较 2025 年度 3.97 万减少 1,602 人,**为 2019 年以来首次缩招** | 三席分别经新华网、北京日报、财新、央视网核实,并复算 3.81 / 3.97 − 1 = −4.0% |
| 16 | 「学费(办学支出)溢价从未消失,消失的只是同学平均 SAT 溢价」 | **方向完全相反**,被作者本人的更新版推翻:学费溢价恰恰是 2011/2014 版用 SSA 行政收入消掉的那一个(.058 → .041 → .033) | 三席分别下载 NBER WP 7322 与 WP 17159 全文 pdftotext,逐字核对结论段与 reconciliation 段 |
| 17 | 「BLS 数字不支持『医疗是最高增长赛道』」 | 可被同一份新闻稿一句原文推翻:「Healthcare and social assistance is projected to have the **largest job growth** and be the **fastest growing industry sector**(+8.4 percent)」;职业大类最快的正是医疗支持类 +12.4% | 三席分别取得 BLS 新闻稿全文(Wayback id_ 快照)与就业矩阵 xlsx 逐格排序 |
| 18 | 麦可思近五年绿牌专业序列(2019–2022 四列) | **五列中四列抄错**,与书内自述(共 14 个专业、数字媒体技术 3 次、6 个计算机类、除数字媒体艺术外均属工学)四条约束**全部冲突** | 三席分别用 pdftotext -bbox 坐标级 / 行首 token 列位两种方法独立重排表 12-7,结论完全一致 |
| 19 | 「Johnson & Kleiner:州专属执照职业跨州迁移率低 **36%**」(作为单一数值使用) | 36% 出自 NBER 工作论文版、对照组是「其他所有职业」、且作者自陈被自选择污染;**已发表的 AEJ:EP 版摘要根本没有 36%**,其偏好设定为 **7%** | 三席分别核对 NBER w24107 摘要、工作论文全文、AEA 期刊页与 IDEAS/EconPapers 已发表摘要 |
| 20 | 「岳昌君调查:2021 年已落实 76.5% = 已确定单位 32.1% + 升学 33.0%」 | **算术不闭合**(32.1 + 33.0 = 65.1),漏掉**灵活就业 11.4%**;且方向很坏——在批判灵活就业注水的文章里把 11.4pp 悄悄并进了「正规去向」 | 一席实取期刊页表 2 全部分项并验算闭合 |
| 21 | 教育部 2023-08-04 通稿 URL 尾号 **1072471** | 该 URL 在教育部站返回「页面不存在」,**Wayback 无任何快照(从未存在)**。正确尾号为 **1072396** | 两席分别尝试原 URL 与 Wayback CDX,均确认不存在;正确 URL 三席均取得全文 |
| 22 | 「美国大学溢价约 **+70–80%**」 | 三席均未回到一手,属原稿自带的未标源断言。改用 BLS《Education Pays 2024》的 **+66%**($1,543 vs $930) | 一席落到 BLS careeroutlook 页核实;另两席标为「未回一手,发表前须补源」 |

---

# 送 Round 3 双席审计的单源承重实证

> 「只有一个来源支撑、且文章结论压在上面」的数字,按重要性排序。**反证搜索席**须记录全部搜索角度(含未搜到的);**方法学审计席**有否决权,被否决者不得承重。

### 第一优先级(文章核心论证压在其上)

1. **微软 AI 适用度评分(G41)** — 教育 0.18/0.31 vs 医疗 0.04–0.13。**未过审预印本 + AI 厂商用自家产品日志自测**,是本篇「AI 暴露度」论述的唯一定量支点。审计点:频率阈值 0.05% 对小职业的截断效应;免费消费级 Bing Copilot 用户与在职专业人士的选择性(论文**不知道用户本人的职业**);O*NET IWA 映射的主观性;两位小数排序的不可承重性(作者自述「relative comparisons are more meaningful」且无置信区间)。反证搜索:Anthropic Economic Index、OpenAI 或第三方(非厂商)的职业 AI 暴露度测量,是否与教育/医疗的排序一致。

2. **麦可思 2010/2011 年红牌与绿牌名单(G56)** — 「计算机科学与技术曾是红牌、资源开采类曾是绿牌」是全篇「蛛网反转」论证的历史锚点。**三席全部只有二手**(《中国青年报》2015-08-11 回顾统计 + 2010 年当期报道转载 + 名单聚合页),**无一取得 2010/2011 年蓝皮书原书**。反证搜索:蓝皮书原书 PDF、麦可思官方历年榜单归档页、2010 年当期新浪教育那份**不含计算机科学与技术**的异版名单(一席见到摘要但未取到原文,可靠性存疑,须查清)。方法学审计:当年红牌是「按绝对失业人数排的 Top10」,对大专业有机械性偏置,这一偏置是否足以解释计算机上榜。

3. **官方灵活就业占比 16.9%(2020 届)/ 16.25%(2021 届)(G59)** — 与麦可思本科 4.6% 构成 3–4 倍缺口,是「口径撕裂 + 造假高发区」论证的官方侧唯一支点。目前仅有发布方转载(学职平台 2021-10-20、中国就业网)。反证搜索:全国高等学校学生信息咨询与就业指导中心原始发布、教育部新闻发布会实录、省级同口径数据。方法学审计:分母含高职专科所带来的构成差异究竟能解释多少个百分点。

4. **教学厅函〔2021〕19 号原件(G48 / G49 / G59 三处承重)** — 落实率公式、毕业去向界定与审核依据、数据发布管制三段引文全篇承重。三席均只取到**省级转发件**(湖南省教育厅 PDF、山西省教育厅转发件),**一席用 Wayback CDX 遍历 moe.gov.cn 2021 年该栏目全目录未见 19 号**。反证搜索:教育部政府信息公开原件;若取不到,全文三处必须统一标注「转引自省级转发件」。另须查清:「结果将向各地通报」一句究竟是否在 19 号文中(两席未核到、一席核到)。

### 第二优先级(承重但已有部分交叉)

5. **湖北省教师招聘 5,799 → 2,740(G57)** — 唯一坐实的「教师招聘腰斩」实证,两席定位到省级公告、一席未取到。反证搜索:jyt.hubei.gov.cn 两份公告原页;江西 7,821 → 1,190 是否存在省级公告(追不到则并入禁用清单)。方法学审计:省级统一公开招聘计划数与教师岗位总需求之间的口径落差(特岗、公费师范生履约、市县自主招聘、编外聘用均不在内)。

6. **《2025 年中国本科生就业报告》的 82.4% / 86.7% / 87.2% / 86.9% / 倒数第 11(G56)** — 「计算机落实率跌到主要专业类倒数」是全篇最直观的现状证据,但**三席全部为媒体转述,无一手原书**(内部自洽仅说明转述链一致,不构成独立证实)。反证搜索:原书、麦可思官方发布页、高校转载的原始图表。

7. **Kleiner & Krueger 已发表版的「18%」(G37)** — 工资溢价阶梯的起点,一席被 Cloudflare 拦截未取到、两席分别经期刊页与机构库取到。反证搜索:JOLE 31(2 Pt 2): S173–S202 发表版摘要逐字。

8. **2025 年 6 月青年失业率 14.5%(G50)** — 「2026 年 6 月同比上升 0.4 个百分点」这一关键反转的唯一支点,目前仅一席一个媒体来源。反证搜索:统计局数据发布库、财新/澎湃等对 2025 年 7 月发布的报道。同批需补:2026 年 3 月 16.9% 与 4 月 16.3%(两席未落一手,仅与「连续下降」自洽)。

### 第三优先级(方法学提示,不承重但已引用)

9. **Law & Marks, UC Riverside WP 201439(G37)** — 唯一支持「护士执照有正向工资溢价」的反向证据,单源工作论文,原文自述仅在其中一个设定下显著。方法学审计:各州分时立法准实验的识别强度与显著性稳健性。

10. **Webber《The Lifetime Earnings Premia of Different Majors》(G46)** — 「队列间中度收敛」一席仅二手著录、两席取自作者主页 PDF(非期刊版)。反证搜索:Labour Economics 发表版措辞是否一致。

11. **智联《2026 年大学生就业前景研判及高考志愿填报攻略》与猎聘《2026 届大学生校招全景洞察》(G58)** — 所有具体百分比均为媒体转述,三席均未取得原始报告。若补不到一手,**文章只保留构念警告部分,删去全部具体数字**。

12. **教育部 2026 届毕业生 1,270 万(G52)** — 一席仅经索引确认存在、未取一手正文页;另两席经新华社稿确认。反证搜索:教育部原页。
