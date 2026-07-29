# Round 2 对抗验证合并判决 — screen-time-teens

24 组 × 3 票(opus,refute-by-default)。分票原文见 r2-votes/;本文件为三票合并后的最终判决。


---

# C01 最终判决:CORRECTED(3/3 票)

三票一致 CORRECTED。(a) 证词逐字与 (b) 官网逐字三票均以一手直取核过、一字不差;全部修正集中在 (c) 书内引语——被压缩掉了作者自限定语,且书内页面始终未取得一手影像。

## 锁定口径(成稿必须用)

### (a) 2022 参议院证词

- 出处标准写法:Jonathan Haidt, **"Teen Mental Health Is Plummeting, and Social Media is a Major Contributing Cause"**, Testimony of Jonathan Haidt, Professor of Ethical Leadership, New York University – Stern School of Business, Before the Senate Judiciary Committee, Subcommittee on Technology, Privacy, and the Law, **May 4, 2022**。一手 PDF:https://www.judiciary.senate.gov/imo/media/doc/Haidt%20Testimony.pdf(12 页)
- 承重引语(位于 PART 3 开头,PDF 第 10–11 页;三票均逐字核到,含 Oxford 逗号):
  > "Correlational, experimental, and eye-witness testimony points to social media as a major cause of the crisis. I do not believe that social media is the only cause of the crisis, but there is no alternative hypothesis that can explain the suddenness, enormity, and international similarity that I laid out in part 1 of this document."
- **`only` 在原件中为斜体**——三票分别用 pdftohtml -i、pdftoppm 130dpi 目视、pypdf 字体逐 run 提取(/ZYVGUU+Calibri-Italic)三种独立方法确认。引用时保留 *only*。
- 截断规则:省略号只能截在 "international similarity" 处;续接句为 "…that I laid out in part 1 of this document."(part 1 小写)。
- **勿混用标题与正文措辞**:文件标题作 "a Major Contributing Cause",正文作 "a major cause",后者更强。
- 二手转述常见错误:多数二手(如 Deseret News)漏掉 Oxford 逗号,写成 "suddenness, enormity and international similarity"。以一手 PDF 为准。
- 听证会背景(引用时应带):该场听证名为 **"Platform Transparency: Understanding the Impact of Social Media"**(GPO 记录 CHRG-117shrg56698),主题是平台数据透明度,不是青少年心理健康专场;Haidt 的政策落点是 PATA、修订 COPPA、年龄验证。小组委员会官方名为 **Subcommittee on Privacy, Technology, and the Law**——Haidt 文件抬头自己写成 "Technology, Privacy, and the Law"(词序不同,系一手文件自身瑕疵,照抄抬头即可但不要当官方名)。
- 证据链自述:证词自称依据是 Haidt 与 Twenge 维护的两份协作式 Google Docs(tinyurl.com/TeenMentalHealthReview、tinyurl.com/SocialMediaMentalHealthReview),非同行评议文献。

### (b) anxiousgeneration.com 官网

- 取用日期必须标注:**取自 2026-07-27 实时官网**(三票均以 curl 抓原始 HTML 剥标签比对,140,079 字节)。
- "The Four Norms" 主栏目逐字(与待验表述一致):
  > "The Four Norms to Roll Back the Phone-Based Childhood
  > 1 No smartphones before high school
  > 2 No social media before 16
  > 3 Phone-free schools, from bell to bell
  > 4 More independence, free play, and responsibility in the real world"
- **必须指明取自 "The Four Norms" 主栏目**:同一页面的 FAQ(Our Approach / "What changes do you recommend?")把第 3 条简写为 "Phone-free schools",无 "from bell to bell"。同页两处措辞不一致。
- 2012 句逐字(位于 FAQ 的 "The Problem" 栏目答案首句):
  > "In 2012, childhood shifted from play and independence to screens and social media."
  后接:"Constant notifications, endless scrolling, and online comparison wire kids for anxiety, depression, attention fragmentation, self-harm, and more."
- **时效限定**:2024-05-02 Wayback 快照的同栏目标题为 "The Four New Norms",第 3 条只作 "Phone-free schools"。现措辞是后期改的,不是自 2024 年以来的稳定表述。
- **勿把官网四条当成书里的四条**:书内 p.290 称之为 "four foundational reforms",第 4 条书内作 "Far more unsupervised play and childhood independence";书内 "Phone-free schools" 出现在 p.239,检索不到 "from bell to bell"。前两条 "No smartphones before high school" / "No social media before 16" 书内 p.15 与官网一致。
- **归属口径**:该站为 The Anxious Generation(TAG)运动官网,自述 "a fiscally sponsored 501(c)(3) led by Jonathan Haidt",页脚 "After Babel © 2026"。文案是组织文案,宜写"TAG 官网",不宜逐字归为 Haidt 本人措辞。
- **粒度差异**:官网 "In 2012" 是压缩表述,书内 Great Rewiring 的时间窗是 "Between 2010 and 2015"。两者不冲突但不可互换引用。

### (c) 书内 "single largest reason" 句

- **必须用完整两句,不得压缩**(三票转录一致):
  > "Between 2010 and 2015, the social lives of American teens moved largely onto smartphones with continuous access to social media, online video games, and other internet-based activities. This Great Rewiring of Childhood, **I argue**, is the single largest reason for the tidal wave of adolescent mental illness that began in **the early 2010s**."
- 三处不可省略:① **"I argue"**(作者自陈立场,非既定事实);② 时间窗 **"that began in the early 2010s"**;③ 主语是 **"This Great Rewiring of Childhood"**——由紧邻前句定义,指 2010–2015 年青少年社交生活整体迁移到智能手机并持续接入 social media / online video games / other internet-based activities,是"手机化童年"复合构念,**不等同于"社交媒体"单项**;措辞是 "single largest reason"(最大单一原因),非唯一原因。
- **不是宣传材料**:三票独立排除。anxiousgeneration.com/book 宣传文案只有小写 "great rewiring of childhood",不含 "single largest reason" / "tidal wave";Penguin UK(9780241647660)与 Penguin Random House US(书号页 729231)官方简介/护封文案均不含该措辞。
- 定位:**第 1 章 "The Surge of Suffering" 章末 "In Sum",美版精装 p.44**(见下"未回溯项"的置信度说明)。
- 年份讹传排雷:summit.org 版本作 "early 2000s",系转录笔误;正确为 **early 2010s**。
- **书中另有一处更弱、且由作者自我标注为"中心主张"的表述,引用时必须并列呈现**(取自 Penguin UK 官方样章 PDF 第 9 页,一手直核,https://cdn.penguin.co.uk/dam-assets/books/9780241647660/9780241647660-sample.pdf):
  > "My central claim in this book is that these two trends—overprotection in the real world and underprotection in the virtual world—are the major reasons why children born after 1995 became the anxious generation."
  三处差异:① 是"两条趋势"而非单一 Great Rewiring;② "the major reasons"(复数、程度更弱)vs "the single largest reason";③ 结果变量为 "became the anxious generation" vs "tidal wave of adolescent mental illness"。**不可把 p.44 那句当作全书中心论断。**
- 版本信息:Penguin Press,2024-03-26,400 页,ISBN 9780593655030,美版副标题 "How the Great Rewiring of Childhood Is Causing an Epidemic of Mental Illness";**英国版副标题为 "…Caused an Epidemic…"(过去时),两版不同,勿混引**。

### 官方勘误(引用整体论断时必须交代)

- 勘误页 https://www.anxiousgeneration.com/research/errata(Haidt 与 Zach Rausch 署名,2024-06-08 首发,Last published 2026-01-27)列出 6 处事实错误:p.4 Instagram 40% 口径改为 9–12 岁日活;p.104 18 岁饮酒年龄;p.183 图表把急诊就诊误标为住院;p.232 Snap streaks 可见性;p.236 路易斯安那年龄验证法;p.157–158 "Corpse Bride" 实验实为《华尔街日报》数据团队而非 CCDH。
- **该页未对 p.44 的 "single largest reason" 作任何修正或撤回**。
- 同页 "Postscript" 中 Haidt 主动让步一项核心机制论断:关于 p.128 Brain Drain(手机在场即损害认知),依据 2024-01 *Technology, Mind, and Behavior* 元分析(33 项研究、166 个效应量、N=4368,**d = −0.02,95% CI [−0.06, 0.01],p = .246**)承认 "my initial claim... may be incorrect",将在下一版修改。

## 修正记录(修正前→修正后)

1. **(c) 删掉了作者自限定语**。修正前:"Great Rewiring...single largest reason for the tidal wave of adolescent mental illness"(读作平铺直叙的断言)→ 修正后:补回 "I argue" 与 "that began in the early 2010s",并保留前句以定义 Great Rewiring。**三票一致,为本组最重的一处修正。**
2. **(c) 出处性质**。修正前:"是否书内原文,或仅宣传材料?"→ 修正后:确认为书内正文(Ch.1 章末 In Sum),已排除出版社文案与官网宣传文案两条可能。
3. **(c) 构念范围**。修正前:易读作"社交媒体是最大原因"→ 修正后:被指认的原因是"手机化童年"复合构念(含 social media + online video games + other internet-based activities),非社媒单项。
4. **(c) 不可当全书中心论断**。修正前(隐含):该句代表全书核心主张 → 修正后:书中自标 central claim 在导论 p.9,是"两条趋势 / the major reasons"的更弱表述,必须并列。
5. **(b) 时效与栏目定位**。修正前:"官网四条 norms 逐字"→ 修正后:须标取用日期(2026-07-27),须指明取自 "The Four Norms" 主栏目而非同页 FAQ(FAQ 第 3 条无 "from bell to bell");2024 年快照标题为 "The Four New Norms"。
6. **(b) 书 ≠ 官网**。修正前:易读成书与官网同一套措辞 → 修正后:书内称 "four foundational reforms",第 4 条措辞不同,"from bell to bell" 在书内检索不到。
7. **(b) 归属**。修正前:"Haidt 官网"→ 修正后:TAG 运动/组织官网(501(c)(3),Haidt 领导),属组织文案。
8. **(b) 时间粒度**。修正前:官网 "In 2012" 与书一致 → 修正后:书内时间窗是 "Between 2010 and 2015",两者粒度不同,不可互换。
9. **(a) 场合口径**。修正前:仅称"参议院证词"→ 修正后:补听证会名 "Platform Transparency: Understanding the Impact of Social Media"、小组委员会官方名 Subcommittee on **Privacy, Technology**, and the Law(Haidt 抬头词序不同)。
10. **(a) 标题 vs 正文**。修正前:未区分 → 修正后:标题 "a Major Contributing Cause" 比正文 "a major cause" 收敛,勿混用。
11. **(a) 小瑕疵留档**:正文用 "eye-witness"(带连字符),同文件 2.8 节小标题作 "eyewitness"。待验表述引的是正文句,连字符正确。
12. **(c) 年份讹传**:summit.org 作 "early 2000s" → 正确 "early 2010s"。

### 三票冲突与裁决

- **p.44 页码**:票1 用 Google Books(volume n9fDEAAAQBAJ / ISBN 9780593655030)站内精确短语检索,四种查询全部命中 Page 44,且三条故意改写的对照查询(reason→cause、2010s→2000s、无关改写)**全部零命中**,排除模糊匹配假阳性;票3 另有两个独立二手源标注页码 44(wisluthsem.org 引 "…(44)";summit.org 注 "(New York: Penguin Random House, 2024), 44")。票2 主张"p.44 来自搜索引擎生成式摘要,不予采信"——但票2 自身的 Google Books API 全程 429 被限流,是**未能验证**而非**反证**。**裁决:采信 p.44**,证据为"逐字命中 + 对照零命中 + 两个独立二手页码标注",置信度高,但仍列入未回溯项(无一手页面影像)。
- **章节归属**:票1 由检索命中页推断 p.44 落在第 1 章(章首 p.25,第 2 章章首 p.53);票3 由 stekel.org 的 "In Sum" 小标题整段复现定位为第 1 章章末。两条互不冲突且互补。**裁决:采信"第 1 章章末 In Sum, p.44",标为高置信推断。**

## 未回溯项

- **(c) 书内该句无一手页面影像**。Google Books 返回 "Restricted Page";Penguin 官方样章仅覆盖导论至约 p.31(grep "largest" 零命中,与该句在 pp.31–44 的定位不冲突但不构成确证);Open Library / Internet Archive 无该书扫描本(用书内已知句反测同样零命中,说明是缺书非缺句);Amazon Look Inside、JAACAP 全文 403。**结论:该句逐字依赖 Google Books 精确短语命中 + 3 个独立二手源(1 篇同行评议书评 BJGP 74(744):322 + 2–3 份独立读书笔记 + 1 条 Kindle 高亮)的一致转录。承重可用,但若需法务级引用须以纸质精装版 p.44 复核。**
- **无法证否 "from bell to bell" 与官网第 4 条措辞完全不在书中**:Google Books 对受限预览书目的站内索引可能不完整,零命中是强提示非证明。
- **"In 2012, childhood shifted…" 在官网的最早出现时间未定**:2024-05-02 Wayback 快照去标签后仅 3,982 字符(页面内容少且可能依赖 JS 渲染),故"该句 2024 年版中未出现"不能作为可靠结论。
- **书籍章节页码边界(Ch.1 p.25 / Ch.2 p.53)未与实体目录核对**,系检索命中页推断。
- **精装/平装/Kindle 各版本间是否存在措辞或页码差异未核**。
- **(a) 未能用 Wayback 独立比对证词 PDF 的历史版本**(本环境 WebFetch 拒绝 web.archive.org)。风险低——当前 judiciary.senate.gov 官方 URL 提供的即为一手文件本身;且 C02 组已用 Wayback CDX 证明该 PDF 自 2022-05-04 至今 186 条快照 digest 恒定、MD5 一致。
- **(a)(b)(c) 均未检索到官方文本层面的勘误或作者事后更正**(书籍勘误页存在但不涉这三处);"无勘误"属未能证否而非已证实。

## 证据分级

**分层评级:**

- **(a) 证词逐字 —— 多源证实(一手)**。三票各自独立下载官方 PDF 并逐字比对,斜体用三种不同技术方法交叉确认,版本稳定性经 Wayback digest 验证。
- **(b) 官网逐字 —— 多源证实(一手)**。三票均绕开摘要模型直接 curl 原始 HTML。仅时效性需标注取用日期。
- **(c) 书内引语 —— 单源已核(间接锁定)**。无一手页面影像;由 Google Books 逐字命中 + 对照实验 + 3 个独立二手转录共同支撑。可承重,但引用时应标"据 Ch.1 章末 In Sum, p.44"。
- **(a)(b) 作为"Haidt/TAG 主张为何"的证据 —— 已证实;作为"该因果主张是否成立"的证据 —— 厂商口径(利益相关方自述)**。证词是本人政策倡导文件、其证据底座为自建 Google Docs 综述;官网是其领导的倡导组织自撰文案。两者均不可当作因果主张本身的独立证据。
- 附:证词中 "there is no alternative hypothesis" 这一断言本身在学界有实质争议(Odgers 2024 Nature 书评、Przybylski、Ferguson 等),但**不影响本组判定**——本组只主张这些逐字句存在于相应文件中,此点成立。


---

# C02 最终判决:CORRECTED(3/3 票)

三票一致 CORRECTED。1.1–1.4 四条**逐字全部成立、一字不差**(含异常破折号与编号排版不一致);修正集中在四处:页码写错、"四特征"这个归并框架是自造、原文自带一处笔误必须标注、以及 "50%–150%" 是**源依赖**区间——被一手 CDC YRBS 数据在下限上部分证伪。

## 锁定口径(成稿必须用)

### 出处

- Jonathan Haidt, **"Teen Mental Health Is Plummeting, and Social Media is a Major Contributing Cause"**, Testimony before the Senate Judiciary Committee, Subcommittee on Technology, Privacy, and the Law, **May 4, 2022**。https://www.judiciary.senate.gov/imo/media/doc/Haidt%20Testimony.pdf(12 页;PDF 元数据 Author = Stanislawski, Aaron (Judiciary-Dem),CreationDate 2022-05-03)
- 听证会名 **"Platform Transparency: Understanding the Impact of Social Media"**,GPO 记录 CHRG-117shrg56698。
- **页码:1.1 与 1.2 在 p.2;1.3、1.4(及 1.5)在 p.3。不是 pp.2-4。** p.4 只有 Figure 2(major depression)与 1.6(国际性)。

### 框架口径(承重)

- PART 1 标题逐字(p.2):**"PART 1: THE SPECIFIC, GIGANTIC, SUDDEN, AND INTERNATIONAL MENTAL HEALTH CRISIS"**,其下注 "(See the adolescent mood disorders Google Doc for supporting evidence)"。
- **Part 1 实际列了六条(1.1–1.6),不是四条。**标题里的四个形容词对应的是 **1.1(specific)/ 1.4(gigantic)/ 1.3(sudden)/ 1.6(international)——不含 1.2,且必须含 1.6**。1.2 是对"测量假象假说"的反驳,不是危机的一个"特征"。Haidt 口头陈述亦自称 "I'll just make these six points"。**"危机四特征 = 1.1–1.4" 属自造归并,成稿不得沿用该框架。**

### 1.1 逐字(p.2,粗体止于 "mood disorders")

> "1.1. The crisis is specific to mood disorders – those related to depression and anxiety. It is not a general across-the-board increase in other illnesses."

破折号为 en dash「–」,非 em dash「—」。逐字引用时若规范化破折号须注明。

### 1.2 完整逐字(p.2,粗体止于 "to self-diagnose")

> "1.2. The crisis is not a result of changes in the willingness of young people to self-diagnose, **nor in the willingness of clinicians to expand terms or over-diagnose.** We know this because the same trends occurred, at the same time, and in roughly the same magnitudes, in behavioral manifestations of depression and anxiety, including hospital admissions for self-harm, and completed suicides. Figure 1, below, from a New York Times article (April 23, 2020), shows just how sharp and sudden the increase has been for hospital admissions for teen girls who had intentionally harmed themselves, mostly by cutting themselves."

- **粗体加粗那半句(clinician 端)绝不可省略**——见修正记录 #2。
- **构念警告**:正文写 "hospital admissions for self-harm"(住院收治),但底层数据 Mercado et al. (2017) *JAMA*(PMID 29164246,"Trends in **Emergency Department Visits** for Nonfatal Self-inflicted Injuries Among Youth Aged 10 to 24 Years in the United States, 2001-2015")统计的是**急诊科就诊**而非住院收治。转述时应写"自伤急诊就诊",或原样引 Haidt 的话并加注底层数据实为 ED visits。(该构念错位与书籍官方勘误页第 3 条"p.183 图表把急诊就诊误标为住院"是同类错误。)

### 1.3 完整逐字(p.3)

> "**1.3 The crisis came on suddenly, in the early 2010s.**
> The curves you can see in the Adolescent Mood Disorders Google Doc are not just the continuation of trends already in evidence for the Millennial generation (born 1982 through 2016). They are more like "hockey sticks," with a long relatively flat period before the early 2010s, and then a sharp upturn or elbow. This is rare in mental health data. It suggests that something changed in the lives of American teens around 2010."

- **"born 1982 through 2016" 是原文笔误**(千禧世代不可能生到 2016;Pew 定义 1981–1996,Haidt/Twenge 自己的体系约 1982–1995,《The Anxious Generation》核心表述为 "children born after 1995")。**整句引用必须带 [sic] 或在该括号前截断,不得静默修补。**该错误自 2022-05-04 首版至今未被更正。
- "hockey sticks" 是**复数、带弯引号**。
- 引用不得止于 "This is rare in mental health data."——**必须带上收尾句 "It suggests that something changed in the lives of American teens around 2010."**,这是 1.3 从"描述形状"跨到"因果暗示"的接口句。
- 若把小标题与正文用省略号缝在一起,须标明这是"标题+正文拼接",非一句连续原文。

### 1.4 完整逐字(p.3,小标题 "1.4 The increases in mental illness are very large.")

> "When you compare rates in 2009 –before most teens were daily users of social media––to 2019––the last full year before Covid made things even worse––the increases are generally between 50% and 150%, depending on the disorder, gender, and subgroup."

- 两处自述理由一字不差成立:2009 = **"before most teens were daily users of social media"**(限定词是 **most**,不是笼统的"在日常使用之前");2019 = **"the last full year before Covid made things even worse"**。
- 原文破折号使用混乱(一个前有空格、后无空格的 en dash + 两处双连字符/em dash;三票的 PDF 抽取渲染不一致)。**成稿如需逐字引用,应统一规范化并加注"破折号已规范化"。**
- 编号排版:原件 "1.1." "1.2." 带尾点,"1.3" "1.4" 无尾点,逐字转录时不要统一化。

### "50%–150%" 的证据地位(承重,必须照此写)

- 该句在证词内**没有任何数字、序列清单或计算过程**,只指向一份滚动更新、无版本锁的 Google Doc(*Adolescent Mood Disorders: A Collaborative Review*)。它是口头概括,不是可复算的统计量。**成稿必须把它当作"Haidt 的原话"呈现,不得当作事实陈述使用。**
- **该区间是源依赖的:**
  - **NSDUH 系落在区间内**:Daly M. (2022), *J Adolesc Health*, PMID 34663534,12–17 岁 N=167,783,窗口与 Haidt 完全相同——过去一年 MDE **8.1%→15.8%(+95%)**;女孩 **11.4%→23.4%(+105%)**。
  - **CDC YRBS 系全部低于 50%**(一手表格,《YRBS Data Summary & Trends Report: 2009-2019》p.58):持续悲伤/无望 26.1%→36.7%(**+40.6%**);认真考虑自杀 13.8%→18.8%(**+36.2%**);制定自杀计划 10.9%→15.7%(**+44.0%**);自杀未遂 6.3%→8.9%(**+41.3%**);未遂需就医 1.9%→2.5%(**+31.6%**)。
  - 结论表述:**"generally between 50% and 150%" 在全美最大规模匿名青少年调查(YRBS)上不成立;要落进该区间必须依赖 NSDUH 自报 + 急诊/自伤行政序列。NSDUH 系约 +95%~+105%,YRBS 系约 +32%~+44%,两者跨在 50% 门槛两侧。**
- **区间必须绑定 2009→2019 窗口,不可当通用结论**:Haidt 本人在《The Anxious Generation》改用 2010→2021 窗口,报告男孩重性抑郁 **+161%**,已超出证词 150% 上限。
- **基线敏感性(如实注明,但不构成"刻意挑谷底"指控)**:NSDUH 上 2009(8.1%)低于 2004(9.0%);改用 2004 起点则增幅由 +95% 降至 **+74%**(SAMHSA 2019 NSDUH 全国报告逐字:"increased from 9.0 percent … in 2004 to 15.7 percent … in 2019")。但 2009 起点并非 Haidt 独创——**CDC 官方十年趋势报告用的就是 2009-2019**(YRBS 双年制,2009 是调查年),所以"挑基线"这条攻击对**年份选择本身**不成立,只对**幅度对基线的敏感度**成立。
- **窗口内无 NSDUH 断点(此点对 Haidt 有利,应如实写)**:2014/2015 NSDUH 改版影响的是处方精神药物、阿片、甲基苯丙胺模块,MDE 模块未列入;真正的 MDE 断点在 2020(疫情期改网络作答),不落在 2009-2019 窗内。
- **口头版与书面版不同**:GPO 听证记录中 Haidt 口头说 "We're not talking 10 or 20 percent. Depending on what you look at, it's anything from 50 to 150 percent. Self-harm for young teen girls in particular is up more than 150 percent, in fact, 180 in the last data that I saw." 即口头把自残女孩单列为"超过 150%"。另口头逐字佐证 2019 截点理由:"I deliberately focused my analysis up to 2019, before COVID because I didn't want to be confused with what COVID has done."
- **流传的 "50%–200%" 版本不属于书面证词**——核 Psychology Today 2022-05 该场听证报道,全文无任何百分比区间、无 "hockey stick" 字样。书面证词的正确数字是 **50%–150%**。

### 1.3 "早 2010s 之前长期平坦"对"自杀既遂"不成立(反证,承重)

NCHS Data Brief No. 352(Curtin & Heron)一手逐字:"After a stable period from 2000 to 2007, suicide rates for persons aged 10–24 increased from 2007 to 2017";"increased 56% between 2007 (6.8 per 100,000) and 2017 (10.6)";15–19 岁 "stable from 2000 to 2007, and then increased 76% from 2007 (6.7) to 2017 (11.8)";讨论部分:"For persons aged 10–14, suicide rates **began increasing in 2010**"。→ **拐点对年长青少年比证词所述早约 3 年;只有 10–14 岁的拐点在 2010。**

### 版本稳定性(可直接写进方法说明)

Wayback CDX 对该 URL 共 186 条快照,从 2022-05-04 18:38:38 到 2026-07-23,**全部共享同一 content digest CWFX5PHCXWTMI7TGCUKAE5PXBVWLMZ4Q**;另下载 2022-05-04 与 2022-06-01 快照与现网版逐字符/逐页比对(MD5 均为 **2741376fa785e393c61b7c515d09ef5b**),完全一致。**该文件自听证当日起从未被修订,无勘误版。**

### 来源性质(引用时必须标注)

该 PDF 是国会听证的**倡导性证词**(PART 3 直接为 PATA、COPPA 修订、AADC/AB 2273、CAMRA 四项立法背书),1.1–1.6 的全部证据支撑指向 Haidt 与 Twenge/Rausch 自行策展、可滚动改写、无版本锁的两份 Google Docs。**应标为"Haidt 的主张",不宜当作独立学术来源。**

## 修正记录(修正前→修正后)

1. **页码**:"同一 PDF pp.2-4" → **pp.2-3**。三票一致。1.1/1.2 在 p.2,1.3/1.4 在 p.3,p.4 只有 Figure 2 与 1.6。
2. **1.2 省略号删掉了承重半句**。修正前:"…to self-diagnose… We know this because…" → 修正后:必须补回 **"nor in the willingness of clinicians to expand terms or over-diagnose."** 被省略的正是 clinician 端(诊断扩张/过度诊断),而这恰是测量伪影派(ICD-10 2015-10 编码切换、Corredor-Waldron & Currie)攻击的靶心。省略后读者会以为 Haidt 只反驳"青少年自我诊断意愿",实际他同时反驳了"临床医生诊断口径"——引用强度被无意削弱,且掩盖了最可争议的一半。**误引成因已定位:原文 1.2 的粗体小标题正好止于 "to self-diagnose",后半是非粗体续句;任何只抄粗体的二手转述都会犯同一错。**
3. **"危机四特征 = 1.1–1.4" 是自造归并** → 修正后:Part 1 有六条,标题四形容词对应 1.1/1.4/1.3/1.6,1.2 不是"特征"而是对测量假象假说的反驳。
4. **1.2 构念**:"住院收治(hospital admissions)" → 底层数据 Mercado et al. 2017 *JAMA* 统计的是**急诊科就诊(ED visits)**。转述时改写为"自伤急诊就诊",或原样引用并加注。
5. **1.3 原文笔误必须标注**:"the Millennial generation (born 1982 through 2016)" → 引用须带 [sic] 或在该括号前截断。三票一致,且票3 经 pdftotext 与 130dpi 页面图像双重目视确认确为原文所印。
6. **1.3 引用漏了收尾句**:止于 "This is rare in mental health data." → 必须补 "It suggests that something changed in the lives of American teens around 2010."
7. **1.3 引语定位**:"hockey sticks 句是 1.3 的开头" → 修正后:1.3 开头是粗体小标题 "The crisis came on suddenly, in the early 2010s.",hockey sticks 在第三句。
8. **1.4 中 2009 的限定词**:"before daily use" → **"before most teens were daily users of social media"**(限定词 **most**;丢掉会把人群比例陈述变成绝对时间点陈述)。
9. **1.4 数值带宽是窗口特定值**:"50%–150%" 作为通例 → 必须绑定 **2009→2019** 窗口;Haidt 本人在书中改用 2010→2021 窗口报告男孩 +161%,已越上限。
10. **1.4 证据地位降级**:事实陈述 → **Haidt 的原话**。该区间在一手层面不可复算(只指向无版本锁的 Google Doc)。
11. **1.4 区间被 CDC YRBS 一手数据在下限上部分证伪**:五项指标涨幅全部 +31.6%~+44.0%,均低于 50%。正确表述为"源依赖区间"。
12. **1.3 "long relatively flat period before the early 2010s" 对自杀既遂不成立**:NCHS Data Brief 352 显示 10–24 岁与 15–19 岁的拐点均在 **2007**,只有 10–14 岁在 2010。
13. **1.1 破折号**:en dash「–」而非 em dash「—」;编号尾点不一致(1.1./1.2. 有,1.3/1.4 无),转录不要统一化。
14. **出处标注**:须写明 2022-05-04、听证名 "Platform Transparency: Understanding the Impact of Social Media"、GPO CHRG-117shrg56698;不是 2023 年。
15. **来源性质**:标为倡导性证词,证据底座为自策展 Google Docs。

### 三票冲突与裁决

- **1.2 中 Figure 1 的构念**:票1 称"同一文件 p.3 Haidt 自己的 Figure 1 图注写的是 'Emergency room visits for self harm'";票3 引 1.2 正文时该句作 "…the increase has been for hospital admissions for teen girls…"。二者不矛盾(**正文用 hospital admissions,图注用 emergency room visits**),但票1 提供了更硬的上游链条(Mercado 2017 JAMA,PMID 29164246,统计口径明确为 ED visits)。**裁决:采信票1 的构念修正;成稿引 Haidt 原话时加注底层数据实为急诊就诊。**
- **1.4 破折号的确切形态**:三票 PDF 抽取结果不一致(票1/票2 得 "2009 –before … media––to 2019––the …";票3 得 "2009 –before … media—to 2019—the …")。系抽取工具对同一字形的渲染差异。**裁决:视为提取伪影,成稿统一规范化破折号并注明。文字内容三票完全一致,不受影响。**
- **1.4 数字方向**:票1、票2 只用 NSDUH(支持区间);票3 补上 CDC YRBS 一手表格(下限被证伪)。三者不冲突,是**并集**——票3 的 YRBS 数据是本组最有价值的新增反证,必须进入锁定口径。

## 未回溯项

- **"50%–150%" 的原始计算来源不可回溯**。证词只指向 tinyurl.com/TeenMentalHealthReview(*Adolescent Mood Disorders: A Collaborative Review*),该 Google Doc 为滚动文档,Wayback 对 Google Docs 抓取不可用,无法取得 2022-05-04 时点的冻结版本。**无从核对 Haidt 依据哪些序列、哪个性别/年龄子群算出 50% 下限与 150% 上限。→ 该区间在一手层面不可复算,只能作为引语呈现,不得承重。**
- **YRBS 分性别的 2009 与 2019 数值未取得一手**。CDC 该报告的分性别趋势为图像,pdftotext 取不到数字。2019 年女生 46.6%、男生 26.8% 有多方二手一致转述,**但 2009 年女生值(常被引为 33.9%)未取得 CDC 一手确认**。若成稿要用"女生 2009→2019"的具体增幅,须回 CDC YRBS Explorer 或 MMWR 增补卷再核。→ **未验证,不得承重。**
- **2009 年"多数青少年尚非社媒日活"这一定性无一手支撑**。证词内无脚注引证;本轮未回溯到 2009 年美国青少年"每日"社媒使用率的一手统计(Pew 2009 只给出用过 SNS 的比例,非日活)。→ **未验证。**
- **未取得 2022-05-04 听证会的口头陈述完整逐字稿/录像**(GPO 印刷版只收录口头陈述,未复制书面 1.1–1.6 编号大纲)。网络流传的 "50–200%" 版本未能回溯到任何一手口头记录。
- **1.1 "specific to mood disorders" 的实质正确性未验证**:未逐一核对同期进食障碍、ADHD、品行障碍等类别的一手趋势数据。该条只核了**逐字正确性**,**排他性主张本身未做独立验证**。→ **不得承重。**
- **页码只锚定在 judiciary.senate.gov 这一排版**:若下游引用其他排版(Haidt 个人站转载等),页码需另核。judiciary.senate.gov 备用下载链接返回 HTML 跳转页而非 PDF,第二份官方二进制副本改用 Wayback 快照替代。
- **证词 p.2 称 Figure 1 取自 "a New York Times article (April 23, 2020)";未直接核到该 NYT 原文**,故"该图底层即 Mercado et al. 2017"系构念与年份匹配推断。
- **CGO/Benchmark 反方文章《The Problems of Teen Suicide and Self-Harm Predate Social Media》全文被 Cloudflare 拦截**,未直接读取;其核心时间点主张已改由 NCHS Data Brief 352 一手数据独立验证(结论方向一致)。
- **未检索到任何针对 1.1–1.4 的公开更正、勘误或 Haidt 事后修订**(含 "born 1982 through 2016" 笔误);一手文件层面确认无变更,但无法排除他在别处口头更正过。

## 证据分级

**分层评级:**

- **1.1–1.4 逐字准确性 —— 多源证实(一手)**。三票各自独立下载官方 PDF 并逐字比对,三票结论完全一致;版本稳定性经 Wayback CDX(186 条快照 digest 恒定)+ 双快照 MD5 比对双重确认。
- **1.4 "50%–150%" 这个数字本身 —— 方向存争(源依赖)/ 部分证伪**。NSDUH 支持(+95%/+105%),CDC YRBS 反对(+32%~+44%,全部低于 50% 下限)。原始计算不可复算。**成稿只能作为 Haidt 的引语呈现,并必须同时给出两个数据源的实际涨幅。**
- **1.2 的实质断言("behavioral manifestations 与自报趋势 roughly the same magnitudes")—— 方向存争**。与 C15/C16 交叉:2015-10 ICD-9→ICD-10 切换引入更易识别的故意自伤编码;新泽西研究显示自伤相关就诊的报告涨幅可能大于底层行为涨幅;男孩非致死性自伤在美国未见显著上升。**"Haidt 说过这句话"成立,"这句话为真"不成立——文章若把 1.2 当作已证结论而非 Haidt 立场,会塌。**
- **1.3 "早 2010s 之前长期平坦" —— 对自杀既遂已被一手证伪**(NCHS Data Brief 352:10–24 岁与 15–19 岁拐点在 2007)。仅 10–14 岁成立。
- **整份文件作为证据来源 —— 厂商口径(利益相关方自述)**。倡导性国会证词,非同行评审,证据链是作者自策展的滚动 Google Docs,作者时点已确立商业与倡导立场(《The Anxious Generation》2024-03 出版)。
- **NSDUH(Daly 2022 / SAMHSA)与 CDC YRBS 反证 —— 多源证实(一手)**,可直接承重。


---

# C03 最终判决:HOLDS(2/3 票 HOLDS,1/3 票 CORRECTED)

(a)–(e) 五点三票均逐字核对成立,**引语一字不差**,伪引排雷(e)成立。第三票的 CORRECTED 仅涉**书目元数据精度**与**语境限定**,不涉及任何引语文字本身——故合并判决取 **HOLDS**,但其提出的四条修正全部并入锁定口径,因为它们直接决定成稿能不能正确使用这些引语。

## 锁定口径(成稿必须用)

### 书目信息(必须按此写)

- Candice L. Odgers, **"The great rewiring: is social media really behind an epidemic of teenage mental illness?"**, *Nature* **628, 29–30 (2024)**, issue **8006**, doi: 10.1038/d41586-024-00902-2
- **发表日期须拆两个口径**:**线上发表 2024-03-29**(一手 PDF 页眉逐字 "29 March 2024");**印刷期 Nature 628 期号 8006 的封面日期为 2024-04-04**。写成 "Nature 628, 29-30 (2024-03)" 会把卷页与月份错绑——29–30 页属四月刊。推荐写法:*Nature* 628, 29–30 (2024); published online 29 March 2024。
- 二手数据库把它标成 "April 2024" 是引期号日期,与 "2024-03" 不矛盾。
- 全文仅三个标题层级:主标题 + 小节 **"A complex problem"** + 小节 **"A generation in crisis"**。

### (d) 开篇句(逐字,三票一致)

> "Two things need to be said after reading *The Anxious Generation*."(书名斜体)

- 紧随其后:"First, this book is going to sell a lot of copies, because Jonathan Haidt is telling a scary story about children's development that many parents are primed to believe."
- **这是正文第一句,不是标题**。标题是 "The great rewiring: is social media really behind an epidemic of teenage mental illness?"
- **必须与另一处高度相似的平行句区分**:"Two things **can be independently true** about social media."(见 (b),位于 "A generation in crisis" 小节)。need to be said = 开篇;can be independently true = A generation in crisis。二者极易混淆。
- **standfirst(引题,Nature 编辑撰写、非 Odgers 的话)**:
  > "The evidence is equivocal on whether screen time is to blame for rising levels of teen depression and anxiety — and rising hysteria could distract us from tackling the real causes."
  引用时须标明为编辑撰写的副标题,不可归为作者句。

### (a) "not supported by science"(逐字,三票一致)

原文第一段第三句:

> "Second, the book's repeated suggestion that digital technologies are rewiring **our** children's brains and causing an epidemic of mental illness is not supported by science."

- 紧接下一句:"Worse, the bold proposal that social media is to blame might distract us from effectively responding to the real causes of the current mental-health crisis in young people."
- **这是句子片段,不是独立整句**——引号内不应加句首大写或当作完整句呈现。
- 连字符规则:此处 "mental illness" **无**连字符;下文 "mental-health crisis" **有**连字符。

### (b) "no evidence…"(逐字,三票一致)——全文被去语境化最严重的一句

位于小标题 **"A generation in crisis"** 之下:

> "Two things can be independently true about social media. First, that there is no evidence that using these platforms is rewiring **children's** brains or driving an epidemic of mental illness. **Second, that considerable reforms to these platforms are required, given how much time young people spend on them.**"

- **物主代词差异必须保留**:(a) 处是 "**our** children's brains",(b) 处是 "children's brains"(无 our)。两句不可互换。
- **成稿必须同时带上 Second 分句,或至少注明这是对句前半**。单引前半会让读者误以为 Odgers 认为社媒无害/无需监管,这与她原意相反。**Haidt 在 X 上的反驳正是只摘前半句**(https://x.com/JonHaidt/status/1774571680511508601,称她这两项断言 "Both of these assertions are untrue")。
- 逐字引用需保留 "First, that…" 的从句形态。

### (c) 反向因果句(逐字,三票一致)

> "Hundreds of researchers, myself included, have searched for the kind of large effects suggested by Haidt. Our efforts have produced a mix of no, small and mixed associations. Most data are correlative. When associations over time are found, they suggest not that social-media use predicts or causes depression, but that young people who already have mental-health problems use such platforms more often **or in different ways from their healthy peers**¹."

- **不得截断在 "more often"**。Odgers 的反向因果表述是**双支的**——不只"用得更频繁"(频率),还有"用法不同"(方式)。只引 more often 会把她的构念窄化为纯剂量效应。
- 句末带**文献标注 1**,不是无出处断言。
- 连字符必须保留:**social-media use**、**mental-health problems**。
- 前一句一手作 **"a mix of no, small and mixed associations"**(英式,**无** Oxford comma)。二手转载(kidsplaytech 汇编页)作 "no, small, and mixed" —— 沿用二手会引入非逐字的逗号偏差。

### (e) 伪引排雷(成立,三票一致)

- **"the kids are not all right" 不出现在 Odgers 的 Nature 书评中。**
- 它是 **Clare Morell** 书评的标题全文:**"The Kids Are Not All Right: A Review of Jonathan Haidt's *The Anxious Generation*"**,Public Discourse,**2024-04-24**,https://www.thepublicdiscourse.com/2024/04/94753/;EPPC 转载 https://eppc.org/publication/the-kids-are-not-all-right-a-review-of-jonathan-haidts-the-anxious-generation/;作者本人 Substack 亦有。
- **立场倒置警告(这正是该排雷点的价值所在)**:Morell 是 EPPC(Ethics and Public Policy Center)Technology and Human Flourishing Project 主任,其书评**支持** Haidt(认为他已证明危害,并主张比 Haidt 更强硬的政策),与 Odgers 的批评性书评**立场相反**。把这个标题误挂到 Odgers 名下会造成立场倒置。
- Morell 文中确有链接指向 Odgers 的 Nature 书评但未直接引用其原句,故不存在"Odgers 说过这话"的合理来源路径。

### 全文末段(逐字,可用于收束 Odgers 立场)

> "A third truth is that we have a generation in crisis and in desperate need of the best of what science and evidence-based solutions can offer. Unfortunately, our time is being spent telling stories that are unsupported by research and that do little to support young people who need, and deserve, more."

### 利益相关(引用时应披露)

- Nature 页面载明 **"The author declares no competing interests."**
- Odgers 在文中自陈立场:"As a psychologist who has studied children's and adolescents' mental health for the past 20 years…"、"As a parent of adolescents…"、"Hundreds of researchers, **myself included**, have searched for the kind of large effects suggested by Haidt" —— **她是被 Haidt 批评的那一派研究者本人,属当事方而非中立第三方**,对"大效应不存在"这一结论有学术既得利益。
- 机构关系(文中作者简介自披露):UC Irvine 心理科学与信息学教授、研究副院长;co-leads 加拿大 CIFAR(Child & Brain Development)与瑞士 Jacobs Foundation 的国际儿童发展网络。补充事实:Jacobs Foundation 曾向 UC Irvine 拨款约 1100 万美元支持 CERES,由 Odgers 参与共同领导,部分工作与产业界合作。**未检索到任何来自科技平台公司(Meta/Google 等)的直接资助记录,也未检索到针对她的利益冲突指控或调查。**
- **对照面 Morell(EPPC)同样非中立;Haidt 亦有书籍销售利益。三方立场都应标明。**

### 后续往还(无勘误)

- **未发现 Nature 对该书评发布任何 correction / erratum / editor's note**(三票独立检索,文章页无 "Updates & corrections" 段)。
- Nature 后续刊出的是读者来信,属正常学术往还:d41586-024-01488-5(Michael A. Spikes, Northwestern Medill,"Social-media influence on teen mental health goes beyond just cause and effect", *Nature* 629, 757, 2024-05-21,称该书评 "gives an incomplete view of Haidt's argument")、d41586-024-01489-4、d41586-024-01040-5。**注意:这封 Correspondence 的作者不是 Haidt——部分二手检索摘要误将其归为 Haidt 的回应,已核实证伪。**
- Haidt 本人的反驳发在 X 与 After Babel Substack(非 Nature 同行评议或勘误渠道),称其已汇集 22 项实验研究(16 项发现显著危害证据)与 9 项准实验(8 项发现危害证据)。**引用 (b) 时宜同时点明该实质争议存在,但它不构成对 Odgers 原文措辞的推翻。**

## 修正记录(修正前→修正后)

1. **引用元数据**。修正前:"Nature 628, 29-30, 2024-03"(把卷页与月份绑在一起)→ 修正后:**"Nature 628, 29–30 (2024), issue 8006;published online 29 March 2024"**。29–30 页属 2024-04-04 的四月刊。
2. **(b) 构句口径**。修正前:当作 Odgers 的独立断言句 → 修正后:它是 "Two things can be independently true… First, that…" 的**对句前半**;必须保留从句形态,且**必须并列 Second 分句**(她明确主张 "considerable reforms to these platforms are required")。**这是本组最重要的一处使用限定。**
3. **(c) 截断**。修正前:以 "…use such platforms more often..." 收尾 → 修正后:必须补全 **"or in different ways from their healthy peers¹"**,否则丢掉 Odgers 的第二个机制(使用方式差异),这是她论点的实质部分。
4. **(d) 标题与开篇句易混**。修正前:把 "Two things need to be said…" 当成可能的标题版本 → 修正后:它是**正文第一句**;标题另有其文;standfirst 由 Nature 编辑撰写,非 Odgers 的话。
5. **(a) 句法限定**。修正前:作为完整句呈现 → 修正后:它是 "Second, the book's repeated suggestion that…" 的片段,引号内不应加句首大写。
6. **(c) 上文逗号**:一手作 "a mix of no, small and mixed associations"(无 Oxford comma),沿用二手会引入逗号偏差。
7. **(a)/(b) 物主代词**:(a) "our children's brains" vs (b) "children's brains" —— 两处措辞确有差别,不可互换(三票均确认待验表述两处都引对了)。

### 三票冲突与裁决

- **verdict 本身**:票1 判 CORRECTED,票2、票3 判 HOLDS。票1 的四条 "corrections" 中,没有一条主张引语文字有误——(d)(a) 两条是句法定位说明,(b)(c) 两条是使用限定,元数据一条是精度补充。票2、票3 把同样的内容归入 "corrections(无实质修正)"与 "evidence_notes(使用警告)"。**裁决:三票在事实层完全一致,分歧只是归类习惯。取 HOLDS,并把全部四条并入锁定口径——因为它们决定成稿能不能正确使用这些引语。**
- **standfirst 逐字**:票1 说它仅由 shoresofacademia 单一来源提供、未在一手 PDF 中出现,标为"未完全核实";票3 从 nature.com 全文直取,给出**完全相同的措辞**。**裁决:采信 standfirst 逐字成立(两个独立来源措辞一致),但标明它是 standfirst(编辑撰写)、不在课程节选 PDF 的排版中。**
- **(e) 的证否强度**:票1 只有节选 PDF + 三个二手镜像的"一致缺席";票3 做了两次 nature.com 全文独立取回并定向检索 "kids"/"all right"/"alright",均无该短语。**裁决:(e) 成立,置信度高**;但票3 自陈的取回层瑕疵(见未回溯项)必须留档。

## 未回溯项

- **未取得未删节的 Nature 官方全文做穷举关键词扫描(三票共同瓶颈)**。nature.com 原文 303 跳转至 idp.nature.com 授权页(付费墙);web.archive.org 在本环境被禁止抓取(仅确认存在 2026-07-23 快照 20260723034521);archive.today 未成功。手上的一手 PDF(UW–Madison PSY 532 课程镜像 https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-11/Odgers_Nature_2024.pdf,页眉含 nature 刊头、DOI、"29 March 2024")**页脚明确标注 "This article has been excerpted for PSY 532",是节选版,不能用于证明任何措辞的"不存在"**。
- **(e) 的负面证据有一处已知瑕疵**:票3 的一次全文取回对单词 "kids" 的检索返回 NONE,而全文实际含 Haidt 引语 "a firehose of addictive content that entered through kids' eyes and ears"(在引号内)——说明取回层的关键词检索并非 100% 可靠。**综合判断 (e) 置信度高(短语的正面归属已由 Morell 三个独立站点确证),但严格意义上的"全文穷尽检索"只做到两次。**
- **节选版被删去的具体段落无法确定**。已知被略去的至少包括 Odgers 论述真实诱因的部分(儿童贫困、阿片危机、校园枪击、种族与性别歧视暴力等;二手检索显示原文含 "close to one in six children live below the poverty line…" 一句)。→ **该句未经一手逐字核对,不予采信,不得承重。** 同理不能声称"全文仅此两处提到 rewiring"。
- **广为流传的另一句未回到一手,不得使用**:「Haidt 所引研究几乎全是大学生或 18–35 岁成人,无一涉及 13 岁以下儿童,而政策处方却针对儿童和低龄青少年」。票3 取回的 "A complex problem" 小节全文(讲基因/环境多因、2008 金融危机、枪支、阿片、每 1119 名学生一名学校心理师等)不含此句;PSY 532 节选本亦不含。多个二手来源以近乎一致的措辞复述,提示它可能确在原文某处(可能在被节选删去的段落),**但无经一手核实的逐字版本。若正文要用,须另行取回 nature.com 全文定位原句后再引,不要照抄二手措辞。→ 未验证,不得承重。**
- **未核到 Nature 该文的 competing-interests 声明原文**(票1:节选版未含,付费墙阻挡)。票3 从 nature.com 页面读到 "The author declares no competing interests."——**两票结论不冲突,但该声明只经单票单次核到,标为单源已核。**

## 证据分级

**多源证实(一手)** —— (a)(b)(c)(d) 四处引语。

- 三票各自独立取源并逐字比对,结论完全一致,连字符、逗号、物主代词、文献标注等细节层面均交叉核对。
- 一手来源:Nature 原始排版 PDF(UW–Madison 课程镜像,含刊头/DOI/日期/脚注编号)+ nature.com 全文两次独立取回。
- 独立二手镜像互证:pxlnv.com 书评汇总页、shoresofacademia Substack、kidsplaytech.com 汇编页(逐字复现,与一手一致)。
- 书目信息经两条独立路径互证:ADS bibcode 2024Natur.628...29O + RePEc v628y2024i8006;Nature 自家两封读者来信正文引作 "Nature 628, 29–30; 2024"(出版方自证)。
- **强化性反证**:最有动机挑错的批评者(shoresofacademia Substack 的系列批评文,含 "The Alternate Reality of Candice Odgers")逐字引用了同样的句子,其攻击点是 Odgers 对既有证据的**解读与取舍**(称其忽略重度使用者的风险升高),而非引文或数据失实。这反向支持文本真实性。

**(e) 伪引排雷 —— 多源证实(正面归属)+ 高置信负面证据**。

- 正面归属(Morell 标题)由三个独立站点确证,一手可及。
- 负面证据("不在 Odgers 文中")由两次 nature.com 全文取回 + 节选 PDF + 三个二手镜像的一致缺席共同支撑,但受制于付费墙与取回层检索瑕疵,不是穷举证否。

**引语的实质内容 —— 双方均为利益相关方,非中立**。

- Odgers 是被 Haidt 点名批评的那一派研究者本人;Morell 属倡导限制儿童使用智能手机的政策智库;Haidt 有书籍销售利益。**引用任一方都应标明立场,不宜把任一方当中立裁判。**
- (b) 的实质争议(Haidt 称已汇集 22 项实验 / 9 项准实验)属**方向存争**,应并列呈现,但不推翻 Odgers 原文措辞。


---

# C04 最终判决:CORRECTED(2/3 票 CORRECTED,1/3 票 HOLDS)

三票均确认 (a)(b)(c) 所引的数字与逐字引语**全部命中一手原文**,归属(土豆=YRBS、眼镜=MCS、非同一数据集)也完全正确——这是那一票判 HOLDS 的理由。但两票各自独立挖出同一批**口径陷阱**:0.4% 不是全域上限、n=355,358 不是分析样本、1.7×–44.2× 是反方向且被近零分母撑大、摘要引语被省略号吞掉了条件从句。**这些口径若不修正,成稿会以正确的数字讲出错误的话。故合并取 CORRECTED。**

## 锁定口径(成稿必须用)

### 出处

- Amy Orben & Andrew K. Przybylski, **"The association between adolescent well-being and digital technology use"**, *Nature Human Behaviour* **3, 173–182 (2019)**, doi: 10.1038/s41562-018-0506-1
- 正式版被 idp.nature.com 登录墙 303 拦截。三票均改用两个独立一手镜像并逐字互证:出版版 PDF 镜像 https://gwern.net/doc/psychology/2019-orben.pdf(含 DOI 头、NHB 版式、Table 2/3、Fig 1–5)+ 牛津 ORA 作者接受稿 https://ora.ox.ac.uk/objects/uuid:5d844350-a359-47d3-b10c-4bfb93ce613b。摘要另经 PubMed(PMID 30944443)第三次互证。
- 代码 https://github.com/OrbenAmy/NHB_2019;预注册/材料 https://osf.io/phf8v

### (a) 摘要逐字(出版版,三票一致)

> "…by applying specification curve analysis (SCA) across three large-scale social datasets (total n = 355,358) to rigorously examine correlational evidence for the effects of digital technology on adolescents. The association we find between digital technology use and adolescent well-being is negative but small, explaining at most 0.4% of the variation in well-being. **Taking the broader context of the data into account suggests that these effects are** too small to warrant policy change."

- **省略号不得跨过第二句的前半**。原文的政策结论带前置限定"把数据的更广背景纳入考虑后",且用的是 **suggests**(有条件的推论),**不是无条件断言**。该推论依赖 (c) 的对比基准,不是从 0.4% 直接得出。**建议整句引。**
- AAM 与发表版有若干无实质差异的编辑性措辞变动(AAM: "an analytic flexibility"、"Specification Curve Analysis"、"(ntot = 355,358)"、"correlational evidence for digital technology affecting adolescents")。**逐字引用一律以发表版为准**;所引两个片段在两版中均一致。

### 0.4% 的确切口径(承重,最易被误用)

- **统计量是 partial η²**(Table 2 列名逐字 "Median partial η2 of SCA"),即方差解释比例,**不是 R²、不是相关系数**。
- **"at most" 指三数据集各自"完整 SCA 中位 partial η²"中的最大值**,不是所有规格的上限:
  | 数据集 | Complete SCA 中位 β | 中位 partial η² | 中位分析 n |
  |---|---|---|---|
  | YRBS | −0.035 | 0.001 | 62,297 |
  | MTF | −0.005 | <0.001 | 78,267 |
  | MCS | −0.032 | **0.004(=0.4%)** | 7,968 |
- **同一篇 Table 2 中多个子分析明显超过 0.4%**:MCS「Own a computer only」partial η² = **0.011(1.1%)**、「Hours of social media use only」= **0.009**、「Adolescent-report well-being only」= **0.008**、「Use of home Internet only」= **0.006**。即子口径可达摘要"上界"的约 2.75 倍。
- **正确写法:"在中位规格下最多解释 0.4% 的方差";不得写成"任何算法下都不超过 0.4%"。**
- 作者 2020 Reply 逐字自证该口径:"median β = − 0.032, percent variance explained = 0.4%"(对应 MCS Complete SCA)。

### (b) n = 355,358 的确切口径(承重)

- 355,358 是**三个互相独立数据集的加总名义总人数**,**不是任何一次分析的分析样本**:
  - YRBS 74,814 = 37,402 女 + 37,412 男
  - MTF 268,672 = 136,190 女 + 132,482 男
  - MCS 11,872 = 5,926 女 + 5,946 男(另含 10,605 名主要照护者,不计入)
  - 三者相加 = 355,358,算术自洽。
- **论文自己在 Methods 逐字警告**:"While the omnibus sample of adolescents totals 355,358 teenagers, it is important to note that the sample sizes of the analyses are often smaller, **in some cases by an order of magnitude or more**."
- **承载 0.4% 头条与"眼镜"对比的 MCS 分析,中位 n 只有约 7,968 —— 约为 355,358 的 2.2%。**(Fig.5 图注给出眼镜 median n = 7,963、技术使用 median n = 7,964。)
- **把 "n=355,358" 和 "0.4%" 并排放会造成量级错觉。成稿必须写清承载头条数字的实际样本量。**

### 时间窗(2007–2016 是并集包络,不是共同窗口)

- Methods 逐字:"encompassing a total of 355,358, predominately 12- to 18-year-old adolescents surveyed between the years 2007 and 2016."
- 逐库实际窗口:
  - **YRBS**:"collected from 2007 to **2015**",双年制,美国 9–12 年级,年龄从 "12 years or younger" 到 "18 years or older"(median = 16, s.d. = 1.24)
  - **MTF**:"collected from **2008** to 2016",年度调查,8/10 年级(12 年级因关键题项无法关联被排除)
  - **MCS**:**不是年份窗而是出生队列** —— "born between September 2000 and January 2001",分析用的是 13–15 岁那一轮(mean 13.77, s.d. 0.45),**单次横截面**
- 名称:论文写作 **"Youth Risk and Behaviour Survey"**,CDC 官方名为 **Youth Risk Behavior Survey**(无 and、美式拼写)。若给全称,建议用 CDC 官方写法并注明论文原文写法。

### (c) 对比倍数 —— Discussion 逐字(三票一致)

> "For example, in all three datasets the effects of both smoking marijuana and bullying have much larger negative associations with adolescent well-being (×2.7 and ×4.3, respectively for the YRBS) than does technology use. Positive antecedents of well-being are equally illustrative; simple actions such as getting enough sleep and regularly eating breakfast have much more positive associations with well-being than the average impact of technology use (ranging from ×1.7 to ×44.2 more positive in all datasets). Neutral factors provide perhaps the most useful context in which to judge technology engagement effects: the association of well-being with regularly eating potatoes was nearly as negative as the association with technology use (×0.9, YRBS), and wearing glasses was more negatively associated with well-being (×1.5, MCS)."

**待验论断 (c) 的五项归属全部命中:土豆=YRBS、眼镜=MCS、二者非同一数据集(论文自身即显式标注库名)、大麻 2.7×与霸凌 4.3×=YRBS、睡眠早餐区间=1.7×–44.2×。**

#### 精确表值(Table 3 | Comparison specification results,列序 YRBS / MTF / MCS)

- **Negative Factors**:Binge-drinking ×2.95 / ×8.10 / ×1.02;Marijuana **×2.70 / ×10.09 / ×1.14**;Bullying **×4.33 / – / ×4.92**;Getting into fights ×3.65 / ×15.58 / –;Cigarettes – / ×18.47 / –;Being arrested – / – / ×0.96
- **Neutral Factors**:Perceived weight ×1.02 / – / –;**Potatoes ×0.86 / – / –**;Asthma ×1.34 / – / –;Milk ×0.28* / – / –;Going to movies – / ×11.51* / –;Religion – / ×16.29* / –;Music – / ×32.68 / –;Homework – / ×3.57* / –;Cycling – / – / ×1.88*;Height – / – / ×1.53*;**Glasses – / – / ×1.45**;Handedness – / – / ×0.10
- **Positive Factors**:Fruit ×0.11 / ×9.49* / ×1.32*;Vegetables ×0.27 / ×20.63* / ×1.52*;**Sleep ×3.06\* / ×44.23\* / ×1.65\***;**Breakfast ×2.37\* / ×30.55\* / ×3.32\***
- 表注逐字:"The values indicate how many times larger the effects of the comparison variables are in comparison to technology use";星号 = **"Denotes when the effect of the comparison variable on well-being is positive, and therefore in the opposite direction to the effect of technology use."**
- 表注给出分母:**YRBS 平均 β = −0.049;MTF = −0.006;MCS = −0.042**。并声明分母与 Table 2 不同源:"Please note that these figures may be different from those found in Table 2, because the mean of technology use measures was used in these analyses." → **YRBS 倍数分母 −0.049,而 Table 2 YRBS Complete SCA 中位 β 为 −0.035,二者不可混用。**

#### 倍数可复算验证(两票各自独立复算,结果一致)

霸凌 YRBS β = −0.212 → 0.212/0.049 = **4.33** ✓;大麻 YRBS β = −0.132 → **2.69 ≈ 2.70** ✓;土豆 YRBS β = −0.042 → **0.857 ≈ 0.86** ✓;眼镜 MCS β = −0.061 → 0.061/0.042 = **1.45** ✓(Fig.5 图注逐字:"Wearing glasses has the most negative association with adolescent well-being (black, median β = −0.061, median n = 7,963, partial η2 = 0.005…); and more negative than the association of technology use with well-being (purple, median β = −0.042, median n = 7,964, partial η2 = 0.002…)")。

#### 四处必须随倍数一起写出的限定

1. **土豆/眼镜是四舍五入值,且方向须说清**。精确值 **×0.86**(土豆)/**×1.45**(眼镜);0.9 与 1.5 是论文 Discussion 自己的约整。**×0.86 意味着吃土豆的负相关略小于科技使用(科技使用反而约 16% 更负)**,原文措辞是 "nearly as negative as",**不是"更糟"**。
2. **1.7×–44.2× 是反方向(保护性)的正向倍数**,不能与大麻/霸凌的负向倍数并列陈述。须写成"更**正向** 1.7–44.2 倍"。
3. **该区间两端都来自"睡眠"行**,不是睡眠与早餐各占一端:下界 = Sleep@MCS ×1.65,上界 = Sleep@MTF ×44.23;Breakfast 全域仅 ×2.37–×30.55。
4. **MTF 的巨大倍数是近零分母伪影,44.2× 不可当实质证据**。MTF 分母 β = −0.006,故 MTF 列全部倍数被机械放大且不稳定。**铁证:论文自己归类为 "Neutral Factors" 的项在 MTF 同样爆表 —— Music ×32.68、Religion ×16.29、Going to movies ×11.51,Positive 里 Vegetables ×20.63、Cigarettes(Negative)×18.47。若 44.2× 说明睡眠重要,则"听音乐 32.7×""宗教 16.3×"同样成立,显系分母伪影。引用 44.2× 必须同时给出 MTF 分母 β = −0.006。**
5. **大麻 2.7×/霸凌 4.3× 只对 YRBS 成立,跨数据集差异极大**:大麻 MCS 仅 ×1.14(几乎打平),MTF ×10.09。**论文自身 "in all three datasets … much larger" 是一处过度概括**(MCS 大麻 β = −0.048 vs 技术 −0.042,谈不上 much larger)。待验论断已正确限定为 YRBS,故论断本身无误,但下游引用须避开原文的这句概括。

### 后续争议(必须并列呈现)

- **Twenge, Haidt, Joiner & Campbell (2020), "Underestimating digital media harm", *Nat Hum Behav* 4:346–348**(Matters Arising,PMID 32303719)。主张原文有六项分析选择系统性压低了效应量,尤以女生社媒使用为甚,并主张"百分比方差解释"不是评估效应大小的有用指标。Fig. 2 题为 "Average linear r values between well-being and various factors in boys and girls from two datasets"。
- **Orben & Przybylski (2020) Reply, *Nat Hum Behav* 4:349–351**(PMID 32303718;开放副本 https://pmc.ncbi.nlm.nih.gov/articles/PMC7116236/ 与 ORA https://ora.ox.ac.uk/objects/uuid:de333ddc-cc14-4d56-a7f4-bfd913e94cc8)。**按批评者要求重跑 SCA 后逐字报告:**
  > "The results (Figure 1, Table 1) illustrate that the median association and effect size (β = − 0.051 [−0.072, −0.031], percent variance explained = 0.3% [0.2, 0.6]) are not significantly different from those in our original SCA (median β = − 0.032, percent variance explained = 0.4%). **Wearing glasses was still more negatively associated with well-being in adolescents than digital technology use (βglasses = − 0.061 vs βtechnology = − 0.051).**"
  性别分层:"females: median β = − 0.069 [−0.074, −0.065], males: median β = − 0.037 [−0.041, −0.032]";并称技术使用 "predicted nearly one half of one percent of the variability in the well-being of girls"。
  **→ 批评方的重分析未推翻本组三项论断中的任何一项。**
- **Twenge & Haidt 等 (2022), *Acta Psychologica* 224:103512**(PMID 35101738):用同批数据但只看社交媒体、按性别分层、剔除被其视为中介的心理控制变量,得女生 median β 约 **−0.11 到 −0.24**。**这动摇的是 "too small to warrant policy change" 这一政策推论的稳健性,不动摇 (a)(b)(c) 所述的"该文说了什么"。若成稿用该文支撑"屏幕时间无害",必须同时呈现:聚合层级(全技术 vs 社交媒体、混合性别 vs 女生)会显著改变效应量。**
- 方法学批评:Bayesian SCA 再分析 JRSS-C 71(5):1330(https://academic.oup.com/jrsssc/article/71/5/1330/7073288)与 arXiv:2201.05381 指出"取中位数会掩盖异质效应"、SCA 的中位数检验可能统计上失效。
- 论文自身在 Discussion 承认:使用简单线性回归而忽略关系可能 "more complex, non-linear or hierarchical";"Many measures used were also of low quality, non-normal, heterogenous or outdated";自评式科技使用测量 "are known to be noisy",**可能反而低估效应**;超大样本下 NHST 本身有问题。另因算力限制,MCS 仅抽取 20,004 个 specification(全域 603,979,752 个),YRBS 372 个、MTF 40,966 个。

### 利益披露(应主动交代)

Competing interests 逐字:"A.O. has no competing interests. A.K.P. has no competing financial interests; in the last five years A.K.P. has served in an **unpaid advisory capacity** with the Organisation for Economic Co-operation and Development, **Facebook Inc., Google Inc.** and the ParentZone."

→ Przybylski 曾以无薪顾问身份服务 Facebook 与 Google;**考虑到本文结论对平台方有利,此项方向相关**,但由作者主动披露且声明无财务利益。资助方:A.O. 受 EU Horizon 2020 IBSEN,A.K.P. 受 ESRC Understanding Society Policy Fellowship;数据由 CDC / NIDA-Michigan / UCL CLS 提供;声明 "funders had no role"。**均非产业资金。**

### 无勘误

Crossref API 查 DOI 10.1038/s41562-018-0506-1 返回 update-to = None、updated-by = null;PubMed 记录仅列两条 "Comment in"(即上述 Matters Arising 与 Reply)。**截至 2026-07-27 无 correction / erratum / expression of concern / retraction。**(注:一次 PMID 试探命中无关的 *Orthopäde* 勘误,已排除。)

### 易混淆点排雷

"眼镜 1.5×" 的对比同时出现在本文(NHB 2019, MCS)与同年另一篇 Orben & Przybylski(*Psychological Science* 2019, "Screens, Teens, and Psychological Well-Being: Evidence From Three Time-Use-Diary Studies")的牛津新闻稿中。**牛津 OII 新闻稿的"wearing glasses had a more negative association"指的是 Psych Science 那篇时间日记研究,不是本文。引用 ×1.45/MCS 时必须锚定 NHB 2019,别引成新闻稿。**

## 修正记录(修正前→修正后)

1. **0.4% 的范围**。修正前:笼统说"最多解释 0.4% 的方差"(暗示全域上限)→ 修正后:**"在中位规格下最多 0.4%"**;这是三数据集 Complete SCA 中位 partial η² 的最大值(MCS 0.004),同篇 Table 2 中 MCS 多个子分析达 0.006–0.011。**两票独立提出。**
2. **0.4% 的统计量单位**。修正前:未标 → 修正后:**partial η²**(方差解释比例),不是 R²、不是相关系数。
3. **摘要引语的限定语**。修正前:"…too small to warrant policy change"(省略号跨过句号)→ 修正后:整句引 **"Taking the broader context of the data into account suggests that these effects are too small to warrant policy change."** 是有条件的 suggests,不是无条件断言。**三票均提出(判 HOLDS 那票以"提醒"形式给出)。**
4. **n=355,358 的分母**。修正前:直接当分析样本量 → 修正后:是三个独立数据集的名义加总;论文自陈分析 n "often smaller, in some cases by an order of magnitude or more";**承载 0.4% 的 MCS 中位分析 n 仅约 7,968**。
5. **2007–2016 的时间窗**。修正前:"三数据集覆盖 2007-2016" → 修正后:是并集外包络。YRBS 2007–2015;MTF 2008–2016;MCS 是 2000-09~2001-01 出生队列的 13–15 岁单次横截面。
6. **土豆 0.9× / 眼镜 1.5× 是正文约整值**。修正前:0.9×、1.5× → 修正后:Table 3 精确值 **×0.86 / ×1.45**;并须说明 ×0.86 意味着科技使用**反而**约 16% 更负,原文措辞是 "nearly as negative as",不是"更糟"。
7. **睡眠/早餐 1.7×–44.2× 须带方向标注**。修正前:与大麻/霸凌并列成一串倍数 → 修正后:这是**反方向(保护性)**的正向倍数,Table 3 该几格全带星号。
8. **该区间两端都出自 Sleep 行**(MCS ×1.65 / MTF ×44.23),不是睡眠与早餐各占一端。
9. **44.2× 是近零分母伪影**。修正前:当作睡眠重要性的实质证据 → 修正后:MTF 分母 β = −0.006;同库 Music ×32.68、Religion ×16.29、Movies ×11.51 同样爆表。引用必须同时给出分母。
10. **大麻 2.7× / 霸凌 4.3× 只是 YRBS 值**。修正前:未标数据集依赖性 → 修正后:大麻 MCS 仅 ×1.14;论文自身 "in all three datasets … much larger" 是过度概括,下游不可沿用。
11. **Table 3 与 Table 2 分母不同源**:Table 3 用 "mean of technology use measures"(YRBS −0.049),Table 2 Complete SCA 中位 β 为 −0.035,不可混用。
12. **利益披露须交代**:Przybylski 曾任 Facebook / Google 无薪顾问(论文自披露)。
13. **名称**:论文写 "Youth Risk and Behaviour Survey",CDC 官方为 "Youth Risk Behavior Survey"。

### 三票冲突与裁决

- **verdict**:两票 CORRECTED、一票 HOLDS。判 HOLDS 那票的 corrections 数组为空,但其 evidence_notes 中以"提醒""关键提醒""原文自身的一处过度概括"等形式**逐条给出了与另两票几乎相同的口径警告**(省略号吞掉限定语、355,358 不是分析样本、0.4% 出自 MCS、大麻 much larger 是过度概括)。**裁决:三票在事实层无冲突,分歧只在归类。取 CORRECTED,因为这些口径若不写进成稿会造成实质误导。**
- **各库中位分析 n**:票1 与票3 一致给出 **YRBS 62,297 / MTF 78,267 / MCS 7,968**(均称直接读自 Table 2);票2 给出 "YRBS ≈ 62,166 / MTF ≈ 115,000+ / MCS ≈ 7,964"(近似值,MTF 未给具体数)。**裁决:采信 2:1 的 62,297 / 78,267 / 7,968**;票2 的 MCS 7,964 与 Fig.5 图注的技术使用 median n = 7,964 吻合,属另一个口径(Fig.5 vs Table 2),不冲突。
- **1.7× 下界的来源**:票1、票3 称是 Table 3 的 Sleep@MCS **×1.65** 约整;票2 称是 MCS 睡眠 β = .070 / .042 = **1.67**。**裁决:以 Table 3 表值 ×1.65 为准**(表值优先于复算),两者差异不影响结论。
- **44.2× 的可复算性**:票1 明确未能复算(MTF 列双栏抽取串行);票2 给出 MTF 睡眠 β = .246 ÷ 未四舍五入的 −.00557;票3 未复算但给出全套 Table 3 表值与分母。**裁决:44.2× 以 Table 3 表值为准,分母 β = −0.006 已三票确认;分子未获可靠独立复算(见未回溯项)。**

## 未回溯项

- **正式出版版(Version of Record)全文未直读**。nature.com 被 idp.nature.com 登录墙 303 拦截;三票均以"出版版 PDF 镜像(gwern,带 DOI 与 NHB 版式)+ 牛津 ORA 作者接受稿"两个独立来源逐字互证,摘要另经 PubMed 第三次互证。**未能在 Nature 官网页面上做直接目视确认;若官网挂有 correction banner,本次核验看不到**——不过针对性检索与 Crossref API 均未检出任何勘误记录。
- **"×44.2" 未在 AAM 之外的一手渠道二次确认**(票2 明确指出这一点)。旁证:牛津大学新闻稿(经 medicalxpress 2019-01-14 转载)逐字给出 "2.7 times and 4.3 times more negative association",2020 Reply 复述了眼镜对比,但 44.2× 无第二一手来源。
- **MTF 睡眠 ×44.23 / 早餐 ×30.55 的分子(MTF 睡眠、早餐的 median β)未能可靠复算**:出版版 PDF 双栏抽取串行,无法与 MTF 列可靠对应。倍数以 Table 3 表值为准,分母 β = −0.006 已核实。→ **44.2× 可引用(表值),但不得用作实质论证,须标为近零分母伪影。**
- **Supplementary Information 未取得**(含 Supplementary Table 2 的 bootstrap 结果、Supplementary Fig. 2–4 的逐规格 n 分布)。**各规格 n 的完整分布只核到正文中位数,未核到极值。**
- **Twenge et al. 2020 批评文一手全文未取得**(Nature 登录墙;ResearchGate 为 Request PDF;未检得 PMC 开放副本)。**其六项分析选择的具体清单、以及其提出的 r ≈ .17(女生)/ r ≈ .20 等替代估计,仅经检索摘要与 Orben & Przybylski Reply 的转述获知,未逐字核对原文——存在被 Reply 单方框定的风险。→ 若成稿要引 Twenge 方的具体数字,须另取一手(与 C05 组交叉)。**
- **Orben & Przybylski 2020 Reply 全文**:票1 未取得(仅核到标题/卷页/主旨);票2、票3 通过 PMC7116236 / ORA 取得作者稿并逐字引用。**裁决:Reply 关键句已由两票一手确认,可用。**
- **arXiv:2201.05381(SCA 统计效力的方法学批评)本次未展开核读**。若成稿论述要依赖"SCA 方法本身是否可靠"这一层,需补核。
- **MCS 的具体调查年份(sweep 年份)未在论文 Methods 中给出**,仅给出生队列与受访年龄。据此可推断为 age-14 sweep(约 2015 年),但论文未写明,**该推断不计入已核证据**。

## 证据分级

**多源证实(一手)** —— (a)(b)(c) 的全部数字、引语与归属。

- 三票各自独立获取两个一手镜像(gwern 出版版 PDF + 牛津 ORA AAM)并逐行比对,两版关键内容一致;摘要另经 PubMed 第三方互证。
- 四组倍数由三票中的两票**各自独立复算成功**(霸凌 4.33、大麻 2.69、土豆 0.857、眼镜 1.45),与表值自洽 —— 这是本组证据强度最高的部分。
- Crossref API 确认无任何更正记录。
- 数据、代码、预注册全部公开(GitHub + OSF),可复现性强。

**分项降级:**

- **×44.2 —— 单源已核(表值),且不得用作实质论证**。分子未获独立复算、无第二一手来源、由近零分母(MTF β = −0.006)机械放大;同库中性/正性变量同样爆表可作反证。
- **"too small to warrant policy change" 这一政策推论 —— 方向存争**。Twenge/Haidt 方按社媒专项 + 女生分层得 median β −0.11~−0.24;作者自己的 Reply 亦承认女生 −0.069 > 男生 −0.037。**聚合层级的选择会显著改变结论,成稿不得把该句当作已定论的政策裁决。**
- **Twenge et al. 2020 的具体数字 —— 未验证**(全文未取得),不得承重。
- **利益相关性**:Przybylski 曾任 Facebook / Google **无薪**顾问(作者主动披露,无财务利益),资助方均非产业资金。**不构成厂商口径,但方向相关,若把该研究当作对抗"屏幕有害论"的核心证据,应主动交代。**


---

# C05 最终判决:CORRECTED(3/3 票)

三票一致 CORRECTED,且是本批最重的一组。证词 2.2/2.3/2.4/2.6 的**逐字引语全部成立、一字不差**;但三票各自独立击穿了同一批**上游归属与量级断裂**:

- **(d) 铅暴露基准根本不出自 Götz 等——三票一致证否。**
- **(a) "2 到 6 倍"的下界站不住,且倍数与 r≈.20 之间存在一个数量级的断裂。**
- **(a) O&P 2020 Reply 已按批评方要求把六项决策全部反转重跑,结果是 β≈−0.05(女生 −0.069),不是 r≈.20——这条一手反证与 Haidt 的核心推论直接冲突,成稿必须并列。**
- **(c) Orben 引语被截断且被升格为"共识"。**

## 锁定口径(成稿必须用)

### 出处

Jonathan Haidt, **"Teen Mental Health Is Plummeting, and Social Media is a Major Contributing Cause"**, Testimony before the Senate Judiciary Committee, Subcommittee on Technology, Privacy, and the Law, **May 4, 2022**。https://www.judiciary.senate.gov/imo/media/doc/Haidt%20Testimony.pdf(12 页;2.2 节起于 p.7,2.4 正文在 p.8)

**四个小节标题逐字**(引用时应带,因为标题本身即论断):

- **2.2** "The correlation is much larger than for \"eating potatoes\" or \"wearing glasses.\""
- **2.3** "There is an emerging consensus that the correlation is in the ballpark of r = .10 to r = .15."
- **2.4** "The correlations are larger for girls."
- **2.6** "Correlations between .15 and .20 are not \"small.\""

### (a) 证词 2.2 逐字(三票一致,一字不差)

> "Jean Twenge and I argued in a published response paper in the same journal that Orben and Przybylski made **6 analytical choices, each one defensible**, that collectively ended up reducing the statistical relationship and obscuring an association that is actually equivalent to a correlation coefficient of around **r=.20**."

> "**In their own published report**, when you zoom in on \"social media\" only, the relationship is between **2 and 6 times larger** than for \"digital media.\""

- 待验论断省略了 "In their own published report,",引用时应补回——它正是承重之处(声称倍数出自 O&P 自己的报告)。
- **措辞校准**:Twenge, Haidt, Joiner & Campbell (2020) 摘要一手逐字为 **"Orben and Przybylski made six analytical decisions that resulted in lower effect sizes"** —— 是 **decisions** 不是 choices,且原文摘要**没有 "each one defensible" 这一让步语**(是 Haidt 在证词里自己加的修辞)。"published response paper in the same journal" 属实(*Nat Hum Behav* 4:346–348,Matters Arising)。
- **2.2 节内部自相矛盾(可直接用作论据)**:该节首段 Haidt 自己写 "Orben and Przybylski report that the average regression coefficient (**using social media use** to predict positive mental health) is negative but tiny",两段后又指责别人把 O&P 的构念当社媒读(指出 potatoes 比的是 all "digital media use")。**同一节内先把 O&P 的构念说成 social media,再指责别人把它当 social media 读。**

### "2 到 6 倍"的实算(承重,三票各自独立复算)

回 O&P 2019 已发表 Table 2(中位 β / partial η²):

| 数据集 | Complete SCA | Social-media-only | 比值(β) |
|---|---|---|---|
| YRBS | β = −0.035 / η² = 0.001 | **无社媒测项**(只有 electronic device use −0.071、TV use −0.012) | 不可算 |
| MTF | β = −0.005 / η² < 0.001 | β = −0.031 / η² = 0.001 / n = 102,963 | **6.2×** |
| MCS | β = −0.032 / η² = 0.004 | β = −0.056 / η² = 0.009 / n = 7,972 | **1.75×** |

- **下界 2 不成立**。MCS 只有 **1.75×**(若改用 Table 3 的技术使用均值分母 −0.042,更低至 **1.33×**)。**要凑出 2 必须:① 改用 partial η²(MCS 0.009/0.004 = 2.25×)——但 η² 是平方尺度,η² 比 2.25 ≈ r 比 1.5,与 Haidt 随后换算成 r 的那把尺子不同;或 ② 用 YRBS 的 electronic device use only(−0.071/−0.035 = 2.0×)——但那不是 social media。**
- **YRBS 根本没有 social-media-only 这一行,该倍数最多只能来自 2 个数据集,不是"in their own published report"整体。**
- **正确表述:"约 1.3–1.8 倍(MCS)到约 5–6 倍(MTF),取决于数据集与分母;下界 2 需混用平方尺度或改用非社媒变量才成立。"**

### 倍数 ≠ 量级(本组承重风险最高的一处)

- 即便全盘接受倍数,**O&P 自报的 social-media-only 系数仍是 β = −0.031(MTF)与 β = −0.056(MCS),即 |r| ≈ .03–.06**。O&P 正文对同一数字的原话:"social media use had a median negative association with well-being of β = −0.031 … although the effect was small, suggesting that technology use operationalized in these terms **accounts for less than 0.1% of the observed variability in well-being**."
- **r ≈ .20 比这高一个数量级。倍数放大不通向 .20 —— 社媒专项最大中位 β 仅 −.056,6 倍于近零仍是近零。二者不能互相支撑。**
- **r=.20 不出自 O&P 的报告**,而出自 Haidt/Twenge 自行重跑的再分析。Haidt 后续 Substack 文(afterbabel.com/p/why-some-researchers-think-im-wrong)已改用更弱的措辞 "the numbers are several times larger",不再给出"2 到 6 倍"的具体区间,且明说 r≈.20 来自他与 Twenge 自己 "re-ran Orben and Przybylski's code"。

### 一手反证:O&P 2020 Reply(承重,必须与 2.2/2.4 并列呈现)

Orben & Przybylski, "Reply to: Underestimating digital media harm", *Nat Hum Behav* **4:349–351** (2020)。开放副本 https://pmc.ncbi.nlm.nih.gov/articles/PMC7116236/ 与 ORA https://ora.ox.ac.uk/objects/uuid:de333ddc-cc14-4d56-a7f4-bfd913e94cc8(两个独立镜像互证)。**他们按 Twenge 等提出的修改逐条实施后重跑 MCS 的 SCA:**

> "The results (Figure 1, Table 1) illustrate that the median association and effect size (**β = − 0.051 [−0.072, −0.031], percent variance explained = 0.3% [0.2, 0.6]**) **are not significantly different from those in our original SCA** (median β = − 0.032, percent variance explained = 0.4%)."

> "**Wearing glasses was still more negatively associated with well-being in adolescents than digital technology use (β_glasses = − 0.061 vs β_technology = − 0.051).**"

> "females showed a more negative association than males (**females: median β = − 0.069 [−0.074, −0.065], males: median β = − 0.037 [−0.041, −0.032]**)"

并称技术使用 "predicted nearly one half of one percent of the variability in the well-being of girls",该量级 "probably not practically significant: less than 1% of variance"。

**Methods 列出他们实际实施的五项修改**:仅用验证过的量表、加入自伤结局、去掉争议控制变量、只留人口学/族裔控制、按性别分开(第 6 项 MTF 小时制量表因 MCS 无对应测量未能实施)。

**→ 两条硬结论:①六项决策被逐条反转后既没逼近 r=.20,女生也没进入 .15–.22 区间。②证词 2.2 的小节标题("远大于吃土豆或戴眼镜")在一手证据上不成立——反转全部修改后,眼镜仍比技术使用更负。证词 2.2 未提及此 Reply。**

### (b) 证词 2.4 逐字(三票一致,一字不差)

> "What would the correlation be if we could just look at girls? Several studies have found that it is substantially larger than for boys. See Kelly, Zilanawala, Booker, & Sacker (2019), Nesi & Prinstein (2015), and Twenge, J.M. (2020). **I know of no study that has found a larger relationship for boys. A ballpark figure for the correlation just for girls is roughly r = .15 to r = .22.**"

**四条必须随引语一起写出的限定:**

1. **这是 Haidt 自陈的 ballpark figure,无推导、无 meta 支撑。**所引三项研究是用来支撑"女孩大于男孩"的**方向性判断**,**不是该区间本身**。该数值区间不出自任何被引一手研究。
2. **Kelly et al. 是 2018 不是 2019**。CrossRef 一手核:DOI 10.1016/j.eclinm.2018.12.005,"Social Media Use and Adolescent Mental Health: Findings From the UK Millennium Cohort Study", *EClinicalMedicine*, published-print **2018-12**, vol 6, pp. 59–68。Twenge 等自己 2020 年在 Nature 的参考文献里也标 2018。
3. **证词内部四处数字互不自洽**:2.2 称 O&P 数据"实际相当于 r=.20"(双性别合并口径);2.3 标题与正文认同双性别合并为 r=.10–.15;2.4 女孩 .15–.22;2.6 标题又改口辩护 ".15 到 .20"。
4. **同期一手对照值明显更低**:O&P 2020 Reply 的女生 median β = **−0.069**;Twenge/Haidt 自己 2022 年 *Acta Psychologica* 224:103512(PMID 35101738)那篇 SCA 报的女生 median β 区间是 **−0.11 到 −0.24**(该文同时称 O&P 原文的 median betas 在 −0.01 到 −0.04 之间)。即 .15–.22 落在 Twenge/Haidt 自家分析的偏上段,**且来自与 O&P 争议中的另一套分析选择,不是中立估计**。**注意该文发表于 Acta Psychologica,不是 Nature Human Behaviour。**

### (c) Orben 2020 引语(逐字成立,但被截断且被升格)

- 出处:Amy Orben (2020), **"Teenagers, screens and social media: a narrative review of reviews and key studies"**, *Soc Psychiatry Psychiatr Epidemiol* **55:407–414**, DOI 10.1007/s00127-019-01825-4(CC-BY,开放获取 PDF:https://link.springer.com/content/pdf/10.1007/s00127-019-01825-4.pdf)
- 证词 2.3 所引(p.409,"Systematic reviews and meta-analyses: social media" 节),逐字成立:
  > "The associations between social media use and well-being therefore range from about r = − 0.15 to r = − 0.10."
  证词句式:"Her own conclusion is that \"…\" **I agree with this assessment, for both sexes combined.**"
- **被截断的紧接下一句(必须补回)**:
  > "It is, however, still unclear what **such a small effect** can tell us about well-being outcomes as social media use is inherently linked in complex ways with other aspects of life."
- **更关键的是同文总结节(p.410, "Small negative associations between screens, social media and wellbeing")的完整表述(必须并列)**:
  > "Many studies and meta-analyses find a small negative association between social media use and well-being of about r = − 0.15 to r = − 0.10, **while the correlations fall to about r = − 0.10 to r = − 0.05 in some work lauded as being more transparent [42, 43].**"
  **[42, 43] 正是 O&P 自己的工作。**
- **"consensus" 是 Haidt 加的**:证词 2.3 把一篇**叙事性 review of reviews** 的目测区间升格成"emerging consensus",并略去了 Orben 本人指出的更低一档区间。
- **该区间的合成方式(构念警告)**:Orben 是把若干 review 报告的"社媒×抑郁症状 r = 0.11 / 0.13 / 0.17"与一篇 meta(总体 r < −0.01,仅青少年子集 r = −0.07)目测归并后写出的近似区间。**构念跨了"抑郁症状"与"well-being"两类,不是同一构念的合并估计量。**Orben 全文摘要定调为"the association … is—on average—negative but very small"。

### (d) Götz 基准 —— 归属被三票一致证否

#### 钙 × 骨量 r=.08 —— **成立**,仅构念用词需校准

- Götz 原文逐字:**"calcium intake and bone mass in premenopausal women (r = .08; Meyer et al., 2001)"**
- **构念是 bone mass(骨量),不是 bone mineral density(骨密度)。**
- 数值链条已回溯到底:Meyer et al. (2001) Table 1 第 10 项 "Calcium intake and bone mass in premenopausal women (Welten, Kemper, Post, & Van Staveren, 1995)" **r = .08, N = 2,493** → 再上溯 Welten et al. (1995) meta 分析(PMID 7472660)偏相关 **r = 0.08 [95% CI 0.05–0.12]**。三层完全一致。

#### 铅 × IQ r=.11 —— **不是 Götz 的例子(三票一致)**

- **Götz/Gosling/Rentfrow 全文根本没有铅的例子。**三票分别用三种独立方式验证:① OSF 作者接受稿(CC-BY,25 页含完整参考文献,https://osf.io/hzrxf/download)全文 grep "lead"/"lead exposure"/"IQ" 零命中;② SAGE 正式版全文(2023-05-21 Wayback 存档 https://web.archive.org/web/20230521064258/https://journals.sagepub.com/doi/full/10.1177/1745691620984483)同样零命中;③ 旁证 —— Primbs, Pennington, Lakens 等 (2023) 的正式反驳文逐条讨论 Götz 的医学类比时只处理阿司匹林等例,全文无铅-IQ 例子,与接收稿一致。
- **Götz 的完整医学/教育基准清单(逐字)**:
  > "the correlations between aspirin and prevention of heart attacks (**r = .03**; …); calcium intake and bone mass in premenopausal women (**r = .08**; Meyer et al., 2001), ibuprofen intake and pain alleviation (**r = .14**; Funder & Ozer, 2019; Meyer et al., 2001) or cardiac patient education and exercise (**r = .09**; Rosenthal & DiMatteo, 2001) **are small to minimal, according to Cohen's classic guidelines (1988), but still highly consequential from a public health perspective.**"
  另含成长型思维 meta r = .08、免费校餐 +.09 SD。
- **r=.11 的真实出处(裁决见下)**:证词该处**超链接指向 https://jamanetwork.com/journals/jama/fullarticle/2613157**,即 **Reuben et al. (2017), JAMA**,Table 2 报告童年血铅 × 38 岁 WAIS-IV 全量表 IQ 的 **r = −0.11**(Dunedin 单一出生队列;主结果为每高 5 µg/dL 对应成年 IQ 低 1.61 分 [95% CI −2.48, −0.74])。**数值 .11 与构念"成人 IQ"都对得上。**
- **相邻但非本源的数值(留档防混)**:Meyer et al. (2001), *American Psychologist* 56:128–165, Table 1 第 18 项 "Extent of **low-level** lead exposure and reduced **childhood** IQ (Needleman & Gatsonis, 1990;effect size reflects a **partial correlation** correcting for other baseline characteristics that affect IQ scores [e.g., parental IQ], derived as the weighted effect across blood and tooth lead measurements)" **r = .12, N = 3,210**;同表第 16 项 "Antihistamine use and reduced runny nose and sneezing" 恰为 r = .11。
- **成稿正确写法**:「Haidt 在证词中把钙摄入 r=.08 归给 Götz 等(正确),另**另起一句**给出铅暴露×成人 IQ r=.11 并链向 Reuben et al. 2017 JAMA(Dunedin 队列)——**该铅基准不是 Götz 文中的例子**。」

#### 两项规范性推论**不是 Götz 的话**(三票一致)

证词写 "r=.08 which is enough to recommend that women take calcium supplements"、"r=.11 which is enough to justify a national campaign to remove lead from water supplies" —— **Götz 原文只说这些效应 "small to minimal, according to Cohen's classic guidelines (1988), but still highly consequential from a public health perspective",未提补钙建议,也未提除铅运动。**

#### "r = .05 到 r = .15" 区间**不是 Götz 的话**

证词写 "in the domains of public health and education, many of the things that warrant public expenditure are correlated with outcomes in the ballpark of r = .05 to r = .15" —— **Haidt 未加引号,属自己的概括**。Götz 列出的实际值区间是 **.03–.14**(其中阿司匹林 .03 低于 .05 下限),且未使用 "warrant public expenditure" 这一表述。

#### Haidt 加了引号的那句**逐字成立** ✓

> "This phenomenon is especially true for effects that accumulate over time and at scale"

#### 年份

证词记作 "Gotz, Gosling, and Rentfrow (**2020**)" → 正式版为 ***Perspectives on Psychological Science* 2022;17(1):205–215**,在线首发 **2021-07-02**,PMID 34213378,DOI 10.1177/1745691620984483。**无 2020 年正式版**;"2020" 可追到作者自存预印本文件名自标的年份(2021-01-10 上传),属可理解但仍应更正的书目错误。证词自己的超链接指向 psycnet 记录 2022-26026-014。

#### Götz 的"小效应即重要"框架在其原刊遭正式反驳(2.6 的基准论本身有对立文献)

Primbs, Pennington, Lakens, et al. (2023), **"Are Small Effects the Indispensable Foundation for a Cumulative Psychological Science? A Reply to Götz et al. (2022)"**, *Perspect Psychol Sci*(https://pmc.ncbi.nlm.nih.gov/articles/PMC10018048/;另 https://pure.tue.nl/ws/portalfiles/portal/292873593/17456916221100420.pdf)。主张跨领域基准类比无效除非有理论/实证论证。防弹衣例逐字:"The effect size of wearing a bulletproof vest on the probability of dying is large if we examine people who get shot but very small if we include the millions of people who never get shot.";并称 "Categorizing r = .03 as small regardless of empirical context, discipline, study design, and outcome variable is…nonsensical"。

### 利益相关(必须标明,三方均非中立)

- 证词是**立法听证的倡导性文件、非同行评审**;证词正文**未见利益冲突或资助披露段落**(grep disclos/conflict/funding/compensat/expert witness 均无命中)。
- **2.2 用以反击 O&P 的"published response paper in the same journal"是 Haidt 本人合著**(Twenge, Haidt, Joiner & Campbell 2020)——**以自撰评论作为纠正 O&P 的权威依据,属自引**。
- Haidt 与 Twenge 均有以该论点为核心的畅销书(商业利益);反向看 Orben/Przybylski 的学术声誉亦系于怀疑论一侧,其 Reply 属被告方回应。**双方均非中立裁判。**
- Götz 等与本争议无直接利益关系。

## 修正记录(修正前→修正后)

1. **(d) 铅基准的归属 —— 三票一致证否**。修正前:"Götz/Gosling/Rentfrow 指出童年铅暴露与成人 IQ 的相关是 r=.11" → 修正后:**Götz 文中根本没有铅的例子**;证词是另起一句给出该数字并链向 Reuben et al. (2017) JAMA。**这是本组最重的一处修正。**
2. **(d) 两项政策推论不是 Götz 的话**("enough to recommend calcium supplements" / "justify a national campaign to remove lead from water supplies")→ 是 Haidt 的附加。
3. **(d) "r=.05 到 r=.15 warrant public expenditure" 不是 Götz 的话** → Haidt 的概括;Götz 实际值区间 .03–.14。
4. **(d) 构念**:钙 × "骨密度(BMD)" → **bone mass(骨量)**。
5. **(d) 年份**:"Götz et al. (2020)" → *Perspect Psychol Sci* **2022;17(1):205–215**,在线首发 2021-07-02。
6. **(a) "2 到 6 倍"的分子分母**。修正前:笼统的"social media 比 digital media 大 2-6 倍" → 修正后:**MCS 1.75×(或 1.33×)、MTF 6.2×;YRBS 无社媒测项**;下界 2 需混用 partial η²(2.25×)或改用 YRBS electronic device use(2.0×)才凑得出。
7. **(a) 倍数 ≠ 量级(承重风险最高)**。修正前:"2-6 倍"与"r≈.20"并列呈现,读起来像前者支撑后者 → 修正后:倍数作用在近零基线上,绝对值仍是 β = −0.031~−0.056(r ≈ .03–.06),**比 r=.20 小一个数量级,二者不能互相支撑**;且 r=.20 不出自 O&P 报告,出自 Haidt/Twenge 自行重跑的再分析。
8. **(a) "6 analytical choices, each one defensible" 的措辞**。修正前:当作 Twenge 等原话 → 修正后:一手摘要为 **"six analytical decisions that resulted in lower effect sizes"**;"each one defensible" 是 Haidt 自加的让步语。
9. **(a) 缺失的同刊反驳必须补上**:证词只呈现 Twenge & Haidt 一侧,未提 O&P 2020 Reply —— 后者按批评方要求全部反转重跑后得 **β = −0.051 / 0.3%**、女生 **−0.069**、男生 −0.037,与 r≈.20 和女孩 .15–.22 **直接冲突**。
10. **(a) 2.2 小节标题被同一份 Reply 顶回**:"远大于吃土豆或戴眼镜"在一手证据上不成立 —— 重跑后 β_glasses = −0.061 仍比 β_technology = −0.051 更负;O&P 2019 原表比值也是土豆 ×0.86、眼镜 ×1.45。
11. **(c) 引语被截断**。修正前:只引 "range from about r = − 0.15 to r = − 0.10" → 修正后:必须补 Orben 紧接的 "such a small effect" 限定句,以及总结节的 **"while the correlations fall to about r = − 0.10 to r = − 0.05 in some work lauded as being more transparent [42, 43]"**。
12. **(c) 被升格为"共识"**:一篇叙事性 review of reviews 的目测区间 → 证词 2.3 标题写成 "emerging consensus"。
13. **(c) 构念口径**:该区间跨了"抑郁症状"与"well-being"两类构念,由 r = 0.11/0.13/0.17 与一篇 meta(总体 r < −0.01、青少年子集 −0.07)目测归并而来,**不是同一构念的合并估计量**。
14. **(b) 女孩 r=.15–.22 需补限定**:逐字成立,但是 Haidt 自陈 ballpark、无推导、无 meta 支撑;所引三研究只支撑方向;**Kelly et al. 应为 2018 非 2019**;证词内部四处数字(.20 / .10–.15 / .15–.22 / .15–.20)互不自洽;同期一手对照值(O&P Reply 女生 −0.069)明显更低。

### 三票冲突与裁决

**铅基准 r=.11 的真实出处 —— 唯一实质冲突,已裁决。**

- 票1 与票2 主张:真正出处是 **Meyer et al. (2001) Table 1 第 18 项,r = .12,构念为"低水平铅暴露 × 儿童期 IQ"**,并据此认定证词有三处偏差(数值 .11→.12、构念成人 IQ→童年 IQ、归属层 Götz→Meyer)。
- 票3 主张:**证词该处的超链接直接指向 https://jamanetwork.com/journals/jama/fullarticle/2613157(Reuben et al. 2017, JAMA),Table 2 报告童年血铅 × 38 岁 WAIS-IV 全量表 IQ 的 r = −0.11**,即 Dunedin 队列。
- **裁决:采信票3。**理由:① 票3 读的是**证词 PDF 内嵌的超链接本身**,是关于"Haidt 引的是哪篇"这个归属问题的**直接一手证据**,而票1/票2 是在没有链接信息的情况下**反向猜测出处**;② 数值精确匹配(.11 vs .11,而非 .12);③ 构念精确匹配(**成人 IQ** vs Meyer 的**儿童期 IQ**)。两项独立特征同时吻合,巧合概率极低。
- **裁决的后果**:票1/票2 提出的"数值应为 .12""构念应为童年 IQ"两条修正**被推翻,不进入锁定口径**;Meyer 2001 第 18 项(r=.12,童年 IQ,偏相关)作为**相邻但非本源**的数值留档防混。**三票关于"Götz 文中无铅例子"的核心结论不受影响,仍为三票一致。**
- **残余风险**:票3 的超链接读取未被第二票复核。若成稿要点名 Reuben 2017,建议再开一次证词 PDF 确认该 anchor 的 href。

**其余冲突:无。**三票在 (a)(b)(c) 的逐字、O&P Table 2 数值、O&P Reply 关键句、Götz 基准清单、钙的三层溯源上完全一致(数值逐格吻合)。

## 未回溯项

- **r=.20 这个数字在 Twenge, Haidt, Joiner & Campbell (2020) 正文中的确切出处与推导,三票均无法回到一手。**该 Comment 完全闭源(Unpaywall oa_status = closed、has_repository_copy = false、oa_locations 为空;Semantic Scholar openAccessPdf 为空)。已尝试:nature.com 正文(付费墙)、证词内嵌 author_access_token epdf 链接(被 idp.nature.com 跨域重定向拦截)、Wayback(三次存档 2020-04-19 / 07-01 / 11-18 只保留摘要页、图注与参考文献)、scholar.archive.org、CORE、OSF/PMC、ResearchGate、ProQuest、作者主页。**仅能确认摘要段有 "six analytical decisions",Fig. 2 题为 "Average linear r values between well-being and various factors in boys and girls from two datasets"。**
  → **无法裁定 r≈.20 究竟出自该 NHB 回应文本身,还是 Haidt 在 2022 年证词中把 2022 年 Acta Psychologica(不同刊物)的女生 median β −0.11~−0.24 回填进了对 NHB 回应文的转述。但需注意:证词句式把 r=.20 明确挂在"published response paper in the same journal"名下。→ 该数字不得承重,只能作为"Haidt 声称"呈现。**
- **"六项分析决策"的逐条清单未取得一手**,只能从 O&P Reply 的 Methods 反推(该处只列出 5 项可在 MCS 实施的请求,第 6 项 MTF 小时制量表因 MCS 无对应测量未实施)。**"六项"这一计数由 Reply 与多个二手来源交叉佐证,但逐条内容与绑定对象未解。**
- **Haidt 与 Twenge "re-ran Orben and Przybylski's code" 得到 r≈.20 的那份再分析,其完整规格(六项决策如何叠加、样本、结局变量、是否分性别)未见于任何公开可核的文件或补充材料。→ 未验证,不得承重。**
- **Twenge, Haidt, Lozano & Cummins (2022) *Acta Psychologica* 全文未取得**(ScienceDirect 对本环境 403 / JS 渲染空壳;DOAJ 仅元数据)。女生 median β −0.11 至 −0.24 **仅经 PubMed 摘要(PMID 35101738)一处核到,未做第二镜像互证**;该文对"social media 比 digital media 大 2-6 倍"的具体算法也未能核。→ **单源已核,引用时须标注。**
- **证词 2.4 的 r = .15–.22 无从回溯到任何计算**:是 Haidt 自陈 ballpark。所引三项研究(Kelly et al.、Nesi & Prinstein 2015、Twenge 2020)本轮未逐篇取回其女孩专项相关系数。→ **属 C24 组的 Kelly Table 2 复核范围,建议在那一组一并解决。本组只能确认它不是这三篇中任何一篇直接给出的数字。**
- **Götz 正式版全文未拿到出版商 PDF 原件**:SAGE 需订阅、对 WebFetch 返回站点框架页。"正式版无铅例"依赖 **1 个 Wayback 镜像 + 1 份作者自存 CC-BY 接收稿 + Primbs 等公开批评文的交叉佐证**(三条独立线索一致)。**无法 100% 排除该例子在校样阶段被追加的可能(可能性极低)。**
- **证词是否附有独立的利益冲突 / Truth-in-Testimony 披露表未核**:参议院此类表格通常与证词 PDF 分开归档;本次仅确认证词正文内无披露段落。
- **票3 关于证词内嵌超链接指向 JAMA 2613157 的读取,未被第二票独立复核**(见上"三票冲突与裁决")。

## 证据分级

**分层评级:**

- **证词 2.2 / 2.3 / 2.4 / 2.6 的逐字引语 —— 多源证实(一手)**。三票各自独立下载官方 PDF 并逐字比对,四处引语与四个小节标题结论完全一致。
- **Orben 2020 的引语与其上下文 —— 多源证实(一手 CC-BY 原文)**。三票均下载 Springer OA PDF 并抽文比对,p.409 与 p.410 两处逐字一致。
- **Götz 基准清单 + "Götz 无铅例子" —— 多源证实**。两个版本(OSF 接收稿 + SAGE 正式版 Wayback 存档)+ 第三方批评文三线一致。
- **钙 r=.08 的三层溯源(Götz → Meyer 2001 #10 → Welten 1995)—— 多源证实(一手)**,可承重。
- **O&P 2019 Table 2/Table 3 数值与 O&P 2020 Reply 关键句 —— 多源证实(一手)**,三票逐格吻合,可承重。
- **铅 r=.11 归属 Reuben 2017 —— 单源已核**(票3 一票,依据是证词内嵌超链接 + 数值与构念双重吻合)。建议成稿前复核 anchor 的 href。
- **"2 到 6 倍" —— 已证伪(下界)/ 方向存争**。方向成立(社媒专项确实大于全技术),但下界 2 需混用平方尺度或替换变量;上界 6.2× 由近零分母(MTF β=−0.005)撑大。
- **r ≈ .20 —— 未验证,不得承重**。一手闭源,推导不可见,且与 O&P Reply 的重跑结果(β≈−0.05)相差一个数量级。**只能作为"Haidt 声称"呈现,并必须紧邻列出 Reply 的反证数字。**
- **女孩 r = .15–.22 —— 未验证(自陈 ballpark),方向存争**。逐字成立但无推导、无 meta;同期一手对照值 O&P Reply 女生 −0.069;Twenge/Haidt 自家 2022 分析给 −0.11~−0.24(单源已核)。
- **整份证词作为证据来源 —— 厂商口径(利益相关方自述)**。倡导性立法证词,非同行评审,2.2 的权威依据是作者本人合著的评论(自引),作者有畅销书商业利益;对立方(O&P)同为当事人。**三方立场都应在成稿中标明。**


---

# C06 最终判决:CORRECTED(3/3 票)

三票一致 CORRECTED,且三票的修正**高度重合**:引语与数字**逐字全部成立**(摘要句、β = −0.05 / −0.02、八波、Understanding Society、2009–2016、10–15 岁、n=12,672 均一字不差),但两处口径必须修正才能承重——**n=12,672 不是分析样本量(中位分析 n 仅 1,699,小一个数量级)**,以及 **β 是 2,268 种分析设定的中位数,不是任何单一模型的点估计**。

## 锁定口径(成稿必须用)

### 出处

- Amy Orben, Tobias Dienlin & Andrew K. Przybylski, **"Social media's enduring effect on adolescent life satisfaction"**, *PNAS* **116(21):10226–10228 (2019 May 21)**;PMID 31061122;PMCID PMC6534991;DOI 10.1073/pnas.1902058116;CC BY 开放获取。
- pnas.org 对本环境返回 **HTTP 403**(三票一致)。一手替代:Europe PMC 出版方存缴全文 XML https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6534991/fullTextXML + PMC HTML https://pmc.ncbi.nlm.nih.gov/articles/PMC6534991/ + PubMed 摘要,三处交叉核对。
- 文章类型为 PNAS **Brief Report**(全文仅 3 页),**无独立 Materials and Methods 章节**,方法细节散见正文。方法学细节须以 OSF(DOI 10.17605/OSF.IO/4XP3V)与 GitHub 仓库 https://github.com/OrbenAmy/PNAS_2019 为补充。数据:UK Data Service,DOI 10.5255/UKDA-SN-6614-12。

### (a) 数据集句逐字(三票一致)

> "To disentangle between-person associations from within-person effects, we analyzed an **eight-wave**, large-scale, and nationally representative panel dataset (**Understanding Society, the UK Household Longitudinal Study, 2009–2016**) using **random-intercept cross-lagged panel models**."

### 样本量口径(本组最重要的一处,三票一致)

论文原文紧接着写明:

> "While **12,672** 10- to 15-y-olds took part, the precise number of participants for any analysis varied by age and whether full or imputed data were used (**range, n = 539 to 5,492; median, n = 1,699**)."

- **12,672 是"参与过"青少年自填问卷的总人数,不是任何一个模型的分析 n。**
- **单个模型的分析 n 中位数仅 1,699,最大 5,492,最小 539 —— 比 12,672 小一个数量级。**
- **成稿正确写法:「12,672 名 10–15 岁青少年参与,单个模型分析 n 中位数 1,699(539–5,492)」。以 12,672 描述该研究的统计效力会夸大约 7 倍。**

### 波数口径

- **"eight-wave" 描述的是数据集本身**;波数是规范曲线中的**一个分析维度**,不是每个模型都用了八波。
- 论文的 best-practice 聚焦模型明确只用 "data from participants who completed **four** waves"(单票提出,见"三票冲突与裁决")。

### (b) 摘要末句逐字(三票一致,三处独立渲染完全相同)

> "**Instead,** social media effects are nuanced, small at best, reciprocal over time, **gender specific**, and contingent on analytic methods."

- **完整句以 "Instead," 引导**——待验片段是完整句的子串,逐字无误,但引用时建议保留 Instead 或用省略号标示。
- **"gender specific" 未加连字符**(非 gender-specific),逐字转录不要加。
- 前文完整语境:"In this study, we used large-scale representative panel data to disentangle the between-person and within-person relations linking adolescent social media use and well-being. We found that social media use is not, in and of itself, a strong predictor of life satisfaction across the adolescent population. Instead, …"

### (c) 两个 β 逐字(三票一致,负号为 U+2212)

> "Both median longitudinal effects were trivial in size (social media predicting life satisfaction, **β = −0.05**; life satisfaction predicting social media use, **β = −0.02**)."

**四条必须随数字一起写出的限定:**

1. **这是规范曲线(specification curve / multiverse)上 2,268 个分析选项的中位数,不是单一或首选模型的估计值。**论文逐字:"We report standardized coefficients for all **2,268** distinct analysis options considered." 设定维度包含:生活满意度分项、性别、波数、估计器、缺失值插补、控制变量。
2. **模型族是 random-intercept cross-lagged panel models(RI-CLPM),β 为组内(within-person)标准化交叉滞后系数。**原文该句**未给出置信区间**。
3. **必须同时给出组间对照值 ψ,否则会丢掉核心对比**。论文逐字:"Across all operationalizations, the median cross-sectional correlation was negative (**ψ = −0.13**), an effect judged as small by behavioral scientists." **ψ = −0.13 是组间(between-person)横断相关,与 β = −0.05 不可互换引用。**本文的核心发现正是"组间小负相关 vs 组内几乎为零"。
4. **两个 β 的方向含义**:均为负,即「高于个人均值的社媒使用 → 随后生活满意度略降」与「**低于**个人均值的生活满意度 → 随后社媒使用略升」(第二条上负号意味着反向)。原文自评为 **trivial in size**。

### 性别特异性(支撑摘要里 "gender specific" 的实证基础,引用 −0.05 时应带)

- 论文逐字:"**Only 16% of significant models arose from male data.**"
- 男生:"b = −0.08 to −0.04 or **β = −0.07 to −0.05**";女生:"b = −0.13 to −0.05 or **β = −0.09 to −0.04**"(除外貌满意度外全部分项)。
- **作者自己的告诫必须一并引(防止过度解读性别差异)**:"When comparing both genders, the effects' confidence intervals overlap, and the lower incidence of significant effects in males alone is not evidence that the effects are therefore substantial in females."

### 论文自身的限定语(转述时不应丢失)

> "Most effects are tiny—arguably trivial; where best statistical practices are followed, they are **not statistically significant in more than half of models**."

> "Self-report measures only partially reflect the objective time adolescents spend engaging with social media..."

### 构念口径(防过度外推,承重)

- **社交媒体使用是单题自报**,题干逐字:"**How many hours do you spend chatting or interacting with friends through a social website like [Bebo, Facebook, Myspace] on a normal school day?**"(5 点量表)
- **它测的是"与朋友聊天/互动"的时长,不是总体社媒使用;且只问上学日,不含周末。**
- 生活满意度:6 个生活领域陈述,7 点视觉模拟量表。另含 7 个儿童/照料者/家庭层面控制变量。

### 年份口径(轻微内部不一致)

- 正文写 **2009–2016**,与待验论断一致 —— **成稿以论文正文口径为准**。
- 但同文的数据引用(ref 6)写的是 "Understanding Society: **Waves 1-8, 2009–2017** and Harmonised BHPS: Waves 1-18, 1991–2009"(UKDS doi.org/10.5255/UKDA-SN-6614-12)。
- **不宜进一步推论为"数据截至 2016 年底",也不宜声称这是数据集的权威年份窗。**UKHLS 第 8 波实地调查跨到 2016 年之后。

### 无勘误,后续往还为常规学术批评

- **PubMed(efetch, PMID 31061122)显示无 Erratum in / 无 Retraction in / 无 Correction 记录。**(某次网络检索摘要曾声称存在"2019 correction notice",经回溯该说法来自一篇无关 PNAS 论文的更正报道,**已核实证伪,不予采信**。)
- 仅两条 Comment in / Reply:
  - **Foster & Jackson, "Measurement confounds in study on social media usage and adolescent life satisfaction"**, *PNAS* 116(31):15333, DOI 10.1073/pnas.1908385116, PMID 31315985, PMC6681716。批评点为**测量效度**:单题只问"上学日"漏掉周末,且限定于"与朋友聊天/互动",可能把重度但非社交型使用者误记为"never",实际在测外向性与社交网络规模;称测量问题 "profound and render the results of the study highly confounded"。
  - **作者回复**:Orben, Dienlin & Przybylski, "Reply to Foster and Jackson: Open scientific practices are the way forward for social media effects research", *PNAS* 116(31):15334–15335, DOI 10.1073/pnas.1909553116, PMID 31315984。反驳依据:用量与 Ofcom(2017)年度报告一致,且周中与周末使用高度相关(引 Trepte & Masur 2015, r = .72),**但未提供新分析、未修改任何报告数值**。
- **该批评针对测量效度,不推翻本组三条描述性论断的任何数字或措辞;但削弱其外推到"社媒使用总量"的解释力。**

### 利益相关(核实为无问题,此点常被误传)

- 论文脚注逐字:**"The authors declare no conflict of interest."**
- 资助:**Barnardo's UK**(儿童慈善机构,A.O. 与 A.K.P.)、**Volkswagen Foundation**(T.D.)、**Understanding Society Policy Fellowship Grant ES/K005146/1**(A.K.P.);数据来自 ESRC 资助的 Understanding Society(University of Essex ISER 主导)。
- **无科技/社交媒体产业资金。**且资助方立场(儿童权益慈善)若有偏倚应偏向"发现危害",而结论方向相反,**故资助偏倚不构成对结论的威胁**。
- 数据与代码公开。

### 防串台警告(两条,成稿必须避开)

1. **Twenge 等 "Underestimating digital media harm"(*Nature Human Behaviour* 2020)针对的是 Orben & Przybylski 2019 *Nature Human Behaviour* 那篇 specification-curve 论文,不是本 PNAS 文。**其"六项分析选择系统性压低效应量"的批评**不可直接挂到本文的 β = −0.05 上**。
2. **Semken & Rossell(arXiv:2201.05381)对 SCA 中位数检验统计效力的方法学批评,其对象同样是姊妹文 NHB 2019,不是本 PNAS 文。**其论点在原理上可迁移到本文的 2,268 规范中位数,**但不构成对本文数字的一手反证,不应误植。**

## 修正记录(修正前→修正后)

1. **样本量口径(三票一致,最重)**。修正前:"n=12,672" 被当作研究/分析样本量 → 修正后:**12,672 是参与过调查的 10–15 岁青少年总数;单个分析 n 中位数仅 1,699,范围 539–5,492**。以 12,672 描述统计效力会夸大约 7 倍。
2. **统计量口径(三票一致)**。修正前:β = −0.05 / −0.02 读作模型点估计 → 修正后:**是 2,268 个分析设定构成的规范曲线的中位数**,模型族为 RI-CLPM,β 为组内标准化交叉滞后系数,原文该句未给 CI。
3. **必须并列组间对照值**。修正前:只给 β → 修正后:同段还给出**中位组间横断相关 ψ = −0.13**;略去 ψ 会遗漏"组间小负相关 vs 组内几乎为零"这一核心对比。
4. **波数口径**。修正前:"八波"易被读作每个模型都用了八波 → 修正后:"eight-wave" 描述数据集本身;波数是规范曲线的一个分析维度。
5. **引语完整性**。修正前:以 "social media effects are nuanced..." 起头当独立句 → 修正后:完整句以 **"Instead,"** 引导;所引片段是子串,建议保留 Instead 或标省略号。另 **"gender specific" 无连字符**。
6. **效应方向的表述**。修正前:易被读成"社媒使用降低生活满意度、生活满意度降低社媒使用" → 修正后:第二条的负号意味着**低**满意度 → 后续**更多**使用(反向)。
7. **性别口径**。修正前:只引 −0.05 → 修正后:应补 "Only 16% of significant models arose from male data" 与男/女 β 区间,以及作者自己的告诫(两性 CI 重叠,男性显著模型少不等于女性效应实质)。
8. **年份口径(轻微)**。修正前:2009–2016 当作数据集权威年份窗 → 修正后:是论文正文自述;同文数据引用作 "Waves 1-8, 2009–2017"。照论文写 2009–2016 可以,但不得推论为"数据截至 2016 年底"。
9. **构念口径**。修正前:"社交媒体使用" → 修正后:单题自报,只测"与朋友聊天/互动"时长,且只问上学日。

### 三票冲突与裁决

- **无实质冲突。**三票的引语转录逐字一致(含 U+2212 负号、"gender specific" 无连字符、2,268、1,699、539–5,492、ψ=−0.13),核心修正完全重合。
- **单票项(采信但标明来源单一)**:
  - 票1 独有:"论文的 best-practice 聚焦模型明确只用 data from participants who completed **four waves**"。另两票未提及但也未反对。**裁决:采信,标为单票已核。**
  - 票2 独有:男女 β 区间的逐字("b = −0.08 to −0.04 or β = −0.07 to −0.05" / "b = −0.13 to −0.05 or β = −0.09 to −0.04")。票3 提到 "females β = −0.09 至 −0.04 与 −0.11 至 −0.07 等区间",措辞略异但不冲突(不同分项)。**裁决:以票2 的逐字引述为准,标为单票逐字。**
  - 票3 独有:Foster & Jackson 与作者回复的具体反驳依据(Ofcom 2017、Trepte & Masur 2015 r = .72)。**裁决:采信,但见未回溯项——两封信的全文均未逐字核到。**
- **一致的"证伪型"发现(值得留档)**:票2 与票3 各自独立排除了两个误传 —— 网络检索摘要声称的"2019 correction notice"(实为无关论文)与"产业资助"(实为儿童慈善 + 大众汽车基金会 + ESRC)。

## 未回溯项

- **pnas.org 官方排版页(HTML/PDF)三票均 403,未能直接读取**;teachertoolkit.co.uk 的 PDF 镜像同样 403。结论依赖 **Europe PMC 出版方全文 XML + PMC HTML + PubMed** 三处互证。三者对关键句完全一致,**但均源自 PNAS 同一份 JATS 供稿,严格意义上不算三条完全独立的一手链路**。(三票均认为这不影响三项待验要点的成立。)
- **Foster & Jackson 批评信与作者 Reply 的全文逐字未取到**(PNAS 403;Europe PMC 对 PMC6681716 未返回 abstract;PMC 抓取工具以版权为由只返回摘要式转述)。**其论点系经检索摘要与二手描述归纳。→ 若成稿要直接引用这两封信的原话,须另行取得 PNAS 116(31):15333–15335 全文再逐字核对。**
- **Supplementary Information 未取得**,故:① **"2,268 个分析选项"如何拆分(各维度取值个数的乘积、横断面 / 社媒→满意度 / 满意度→社媒 各占多少条规范)未从一手核实**;② **无法确认 β = −0.05 与 −0.02 各自是在多少条规范上取的中位数**;③ Fig.1 中各年龄段/性别的具体 β 分布与置信区间未核。正文只给出总数与三条中位数。
- **"八波"对应的具体 UKHLS wave 编号未从一手确认**(论文只写 eight-wave, 2009–2016,未逐波列出社媒题项的可得性),无法确定是 Wave 1–8 还是含 BHPS 样本的其他组合;需查 OSF 代码或 UK Data Service 数据字典才能定论。一次网络检索摘要曾把同数据集描述为 "7 annual waves"(疑为混淆 Orben et al. 2022 *Nature Communications* 对同数据集的描述),**未能回溯到一手,不据此修正**。按论文正文口径 "eight-wave" 成立。
- **β = −0.05 / −0.02 未经独立复算验证**。OSF 代码公开但 UKDS 数据需注册申请,本次未执行重算。→ **这两个数值属"与论文所报一致",而非"经独立复算验证"。**
- **未系统检索 2019 年后是否有独立团队用同一 Understanding Society 数据做过直接复制/再分析并得出不同的中位效应量。** → 未验证,该缺口不影响本组判定,但若成稿要断言"该结果已被独立复制/未被复制",须另核。

## 证据分级

**多源证实(一手,出版方存缴全文)** —— (a)(b)(c) 三项的全部引语与数字。

- 三票各自独立通过 Europe PMC 出版方 JATS 全文 XML / PMC HTML / PubMed 三条渲染路径取文,逐字比对结果完全一致(含 U+2212 负号、连字符、逗号序列)。
- PubMed efetch 确认无勘误、无撤稿;两条 Comment/Reply 均不改动任何数字或措辞。
- 数据(UKDS)、代码(GitHub + OSF)、预注册材料全部公开,可复现性强。
- 唯一削弱项:三条渲染路径同源于 PNAS 一份 JATS 供稿,非三条独立一手链路(出版商官网 403)。

**分项标注:**

- **利益相关性 —— 已核实为无问题**。资助方为儿童慈善(Barnardo's UK)、Volkswagen Foundation、ESRC,**无平台产业资金**;且资助方若有立场偏倚应偏向"发现危害",结论方向相反,构成对结论的**加强**而非削弱。"该文受产业资助"是误传,已证否。
- **外推到"社媒使用总量"的解释力 —— 方向存争**。Foster & Jackson 的测量效度批评(单题、仅上学日、限定"与朋友聊天/互动")未被作者以新分析回应。**成稿若用本文支撑"社媒使用与青少年福祉几乎无关",必须同时交代该构念只覆盖上学日的社交型使用。**
- **2,268 规范的内部结构、以及 β 中位数的规范分布 —— 未验证**(SI 未取得)。不影响引用这两个数字,但**不得声称"绝大多数规格都接近零"之类的分布性论断**。
- **独立复制情况 —— 未验证**,不得承重。


---

# C07 最终判决:CORRECTED(3/3 票)

三票独立验证,三票均判 CORRECTED。所有主数字逐字成立,但引用年份、k 的单位、效应量度量、构念范围、性别差异的显著性五处口径必须修正。

## 锁定口径(成稿必须用)

### 篇 (a) 书目与主数字
- **正确著录**:Ferguson, C. J., Kaye, L. K., Branley-Bell, D., Markey, P., Ivory, J. D., Klisanin, D., Elson, M., Smyth, M., Hogg, J. L., McDonnell, D., Nichols, D., Siddiqui, S., Gregerson, M., & Wilson, J. (2022). *Like This Meta-Analysis: Screen Media and Mental Health*. **Professional Psychology: Research and Practice, 53(2), 205–214**. DOI 10.1037/pro0000426。线上首发 2021-10-25(Accepted July 25, 2021,© 2021),纸本 2022-04。**成稿写「Ferguson et al. 2022(2021 线上首发)」**;Ferguson 本人在 (b) 篇参考文献中亦自引为 (2022) 53(2), 205–214。
- **Table 1「Meta-Analytic Results Screen Time and Mental Health Outcomes」逐字**(三票分别自 gwern 镜像与作者主页两个独立副本提取,数值完全一致):
  - All studies **k=37, r+=.052, 95% CI (.036, .068), χ²(36)=310.72, p<.001, I²=88.4, τ=.040, Publication bias? No**
  - Correlational k=25, r+=.051, (.031, .071), I²=91.6
  - Longitudinal k=12, r+=.055, (.032, .077), χ²(11)=21.88, p=.025, I²=49.7
  - (25+12=37 自洽;原文 CI 用**圆括号**)
- **k 的单位**:摘要逐字 "The current meta-analysis included 37 effect sizes from 33 separate studies." → 成稿写「**37 个效应量、来自 33 项独立研究**」。Table 1 表注写 "k = number of studies"、Method 又写 "37 papers",系原文自身口径不一致;技术类型分组 general screens 20 + smartphones 11 + social media/internet 6 = 37,证明 k 是效应量层级。
- **效应量度量**:r+ 主体不是零阶相关,而是多元回归标准化系数(β)折算成 r 度量后的合并值。逐字:"Particularly for correlational and longitudinal studies, analyses used results which were based upon multivariate analyses resulting in standardized regression coefficients (betas)." → 这是**控制协变量后的偏效应**,拿它对照 r=.10 的 crud-factor 阈值,与拿裸相关对照不是一回事。
- **构念范围**:是**屏幕媒体总体** meta,不是青少年专属、也不是社媒专属。逐字:"The original preregistered study design plan was limited to teen samples, but ultimately this broadened out to include all samples to get a wider view of data among young adults as well. Age is considered as a moderator." 其中 **social media/internet 子组仅 k=6,r+=.043 [.004, .082]**;general screens 子组 k=20,r+=.059 [.036, .083]。**若用 (a) 支撑「青少年 × 社媒」,分母只有 6 个效应量。**
- **非实验**逐字两处:"All studies included in the final sample were either cross-sectional or longitudinal in nature.";"the preregistration had criteria for both correlational/longitudinal as well as experimental study best practices. However, ultimately, no experimental studies were included in the analysis."
- **r=.10 阈值**逐字:"Although any cutoff threshold is arbitrary, the present analyses determined the cutoff as r = .10. This mitigated against the issue that any values below this would be explained primarily as due to study artifacts rather than real population-level effects (Ferguson & Heene, in press; Przybylski & Weinstein, 2019)." 结果段:"…in no case passed the r = .10 threshold for interpretation as hypothesis supportive."
- 检索范围:PsycINFO + MedLine,限 2015–2019,**排除未发表研究**。

### 篇 (b) 书目与主数字
- **正确著录**:Ferguson, C. J., Kaye, L. K., Branley-Bell, D., & Markey, P. (2025). **Professional Psychology: Research and Practice, 56(1), 73–83**. DOI 10.1037/pro0000589。Received 2023-09-22 / Revision 2024-05-13 / Accepted 2024-05-23;线上先发 2024-10-03,纸本 2025-02。**成稿写「2025(2024 接收/线上首发)」**。
- **完整标题(副标题不可略)**:"**There Is No Evidence That Time Spent on Social Media Is Correlated With Adolescent Mental Health Problems: Findings From a Meta-Analysis**"(校样版排作 "Meta-analysis",正式记录/APA 标题式大写作 "Meta-Analysis")。副标题正是「这是相关性 meta」的自限定语。
- **Table 1「Meta-analytic Results of Social Media and Mental Health Outcomes」逐字**(三票一致):
  - All studies **k=79, β=.061, 95% CI [.047, .075], χ²(78)=4404.45, p<.001, I²=98.8, τ=.055, Publication bias? No**
  - Male k=27, β=.044, [.025, .062], χ²(26)=164.79, I²=94.7
  - Female k=29, β=.075, [.050, .101], χ²(28)=388.10, I²=97.9
  - Correlational k=48, β=.072, [.05, .090], I²=99.3
  - Longitudinal k=30, β=.044, [.023, .066], I²=83.6
  - National survey k=53, β=.067, [.050, .084], I²=99.2, **Publication bias? Yes**
  - (原文 CI 用**方括号**)
- **样本构成逐字**:"Our search ultimately netted 55 studies on social media use and youth mental health. However, nine were subsequently found to be missing important data… This resulted in a final pool of 46 studies. Between them, allowing for different effects for boys and girls in some studies, these articles included 79 total effect sizes." 纳入年龄逐字:"have a sample only including participants between the ages of 12 and 18"(5 项略低于此)。
- **性别行不是全样本对半切分**:Male k=27 + Female k=29 = 56,远少于 79;只有部分研究报了分性别效应。原文自称 "biological sex differences",不是社会性别。
- **【硬性禁止】不得写「女生受影响更大」**:该性别调节效应**不显著**。逐字:"Initial results using a mixed-effects model (k = 56) were nonsignificant (p = .074); however, resilience testing suggested that model estimator had an impact on p value with p values ranging from <.001 (Hunter-Schmidt method) to .111 (Sidik-Jonkman method)." 且 "both effects fell below the threshold for evidence."。**只能写:两个子组点估计有微小差(女 .075 / 男 .044)、差异未达显著、两者均低于作者自定的 .10 判据阈值。**
- **效应量度量(脚注 3 逐字)**:"'r' is used here to denote the most controlled/conservative effect size from each study, which in most cases (but not all) were standardized regression coefficients." 即标题说 "Correlated",合并量却是**每项研究中最受控/最保守**的那个效应量——系统性偏向压低,是该文结论方向上的已知口径倾斜。
- **单位错配**:判据阈值原文以 r 表述("we considered an effect size of r = .10 as the minimum for practical significance"),而合并量以 β 报告(β=.061),论文直接拿 β 与 r 阈值比较。**转述时不宜写成「r+=.061」。**
- **效应量非独立**:79 个效应来自 46 项研究(同研究多效应:分性别、同一数据集多篇),且偏离预注册。逐字:"This differs from the intent in our preregistration where we had hoped to extract a single effect size from each data set… we decided to include all articles but include potential multiuse data sets as a moderator." 合并非独立效应会低估标准误,也是 I²=98.8 极端异质的部分来源。
- **实验研究处理(脚注 6)**:"There was only one experimental study; thus, this was not included in the analysis." 成稿表述:「79 个效应量中 78 个为相关/纵向,仅 1 个实验(该实验效应被排除出 study-type 调节分析)」。
- **发表偏倚不是干净的「无」**:Table 1「All studies」行标 No,但正文逐字 "Evidence from Egger's regression (p = .021) and trim and fill (missing studies: four) suggested potential for publication bias in this meta-analytic data set.",且 National survey 子组(占 79 个效应中的 53 个)Table 1 直接标 **Yes**。
- 预注册与数据:OSF 预注册 https://osf.io/9kd4x,数据 https://osf.io/gjt84,PRISMA https://osf.io/yaedq,纳入清单 https://osf.io/kx486;自陈两处偏离预注册(年龄范围放宽、每数据集单一效应量改为全纳入),计算软件由 CMA 改为 jamovi。

### 跨两篇的口径
- **两篇共用同一 r=.10 判据**,不是 (a) 独有;该阈值由作者自定并自承 "arbitrary"。
- **两篇不是相互独立的验证**:(b) 的 4 位作者全部在 (a) 的 14 人作者名单内,同一期刊,且样本重叠——(b) 正文逐字 "There was an overlap of seven studies (15%) with a previous study of screen time more broadly." **不宜作为「两项独立 meta 相互印证」呈现。**
- **纵向 vs 横断方向在两篇之间相反**:(a) 纵向 .055 > 相关 .051,原文称 "Longitudinal studies did not provide any more evidence for effects than correlational studies";(b) 则 "The effect sizes for longitudinal studies were slightly smaller (β = .044) than that of correlational studies (β = .072)"。**若跨两篇论证「纵向≈相关」,须注意这是两个方向相反的对比。**
- **【排雷】Rausch & Haidt 与 After Babel 的批评不针对本组这两篇**:其攻击对象是 Ferguson 另一篇**实验类** meta(《Do Social Media Experiments Prove a Link with Mental Health》,Psychology of Popular Media)。该批评既不能用来推翻本组数值,也不能被拿来当作这两篇已被质疑的证据。**引用时必须严格区分 Ferguson 的相关性 meta 与实验 meta。**
- **无勘误/撤稿**:Crossref 查询 10.1037/pro0000426 与 10.1037/pro0000589 的 relation / updated-by 字段均为空;期刊容器内检索 "Correction to Ferguson" 无命中。检索中出现的 "Correction to Ferguson et al. (2021)" 经 Crossref 解析属 *Crisis* 期刊 DOI 10.1027/0227-5910/a000868,与本组无关。
- **利益相关**:两篇均未见 COI/资助披露段。(a) 致谢含德国经费编号 1706dgn006(对应合著者 Elson 所在机构)。(b) 首页作者简介载 Linda K. Kaye 曾参与致 Zuckerberg 的公开信及英国 Online Safety Bill 相关工作——方向上不构成亲平台倾向。Ferguson 长期公开持「道德恐慌」立场,两篇正文均以该框架论证。**方向性立场相关成立,产业资助无证据,既不证实也不排除。**

## 修正记录(修正前→修正后)

1. 「Ferguson et al. 2021 Professional Psychology」→ **2022, 53(2), 205–214**(2021 仅为线上首发年)。
2. 「k=37」被读作 37 项研究 → **37 个效应量、33 项独立研究**。
3. 「r+=.052」被当作相关系数 → **合并的是控制后的标准化回归系数(β)折算值,非零阶相关**;拿它比 r=.10 crud 阈值属单位混用。
4. (a) 被当作「青少年 × 社媒」证据 → **屏幕媒体总体、含年轻成人;社媒/互联网子组仅 k=6, r+=.043 [.004, .082]**。
5. 「Ferguson/Kaye/Branley-Bell/Markey 2024」→ **2025, 56(1), 73–83**(2024 为接收/线上先发年)。
6. 标题引到 "…Adolescent Mental Health Problems" 为止 → **补全副标题 ": Findings From a Meta-Analysis"**。
7. 「女 .075 / 男 .044」被读作性别差异成立 → **调节效应不显著(mixed-effects k=56, p=.074;估计量不同 p 值从 <.001 到 .111);且 Male 27 + Female 29 = 56 ≠ 79,是子集不是切分**。
8. 「β=.061」未加限定 → **是每篇研究「最受控/最保守」效应量的合并(脚注 3),系统性偏向压低**。
9. 「46 研究 79 效应」未提依赖性 → **79 个非独立效应来自 46 项研究,偏离预注册的单效应量计划,低估标准误**。
10. 「(b) 是纯相关性 meta」→ **79 个效应中 78 个为相关/纵向,1 个实验被排除出 study-type 调节分析**((a) 则为 100% 非实验)。
11. 「(b) 无发表偏倚」→ **正文 Egger's p=.021 + trim-and-fill 缺 4 项提示存在;National survey 子组直接标 Yes**。
12. 「r=.10 阈值是 (a) 的判据」→ **两篇共用同一阈值,均为作者自定、自承 arbitrary**。
13. 「两项 meta 相互印证」→ **作者高度重叠(4/4 在 14 人名单内)、同期刊、样本重叠 7 项(15%),非独立验证**。

## 未回溯项

- **【三票均未回溯,须标未验证】(b) 篇 version of record(PPRP 56(1), 73–83)的 Table 1 未能逐字比对**。三票所依据的全文均为作者主页上的 BluPencil **自动排版校样**(页脚 "PRO-2023-0960_blupencil ▪ 18 July 2024",封页自称 "This version will not be as-is published online nor printed";单位名误作 "Stenson University")。APA PsycNet 为 JS 空壳、Ovid 返回 402、SSRN/ResearchGate 403、Edge Hill 机构库对非浏览器请求返回拦截页。卷期页与摘要口径(46 studies)已由 Crossref、Ovid、ProQuest 三处独立确认,但**表内 β/CI/I² 只有校样这一份来源**。校样系接收后排版件,数值变动概率低但未证伪。相较之下 (a) 篇已用两个独立副本(gwern 镜像 + christopherjferguson.com)交叉验证。
- **【三票均未回溯】两篇的 OSF 原始编码表(a: osf.io/mex4s、osf.io/rehys;b: osf.io/9kd4x、osf.io/gjt84、osf.io/kx486)未逐条下载复核**。因此无法独立验证效应量提取是否准确、各研究是否被正确归入 correlational/longitudinal/性别子组。**注意:Rausch/Haidt 对 Ferguson 另一篇实验 meta 提出的那类样本量提取错误,在本组两篇上尚无任何人做过检验,也未被本次核查排除。**
- **【三票均未回溯】两篇的利益冲突与资助披露**:两篇 PDF 正文均无 COI/funding 段((a) 的 Disclosures 段仅含预注册与数据可及性)。无法确认付印版是否另附披露声明。就 Ferguson 是否有科技行业资助或诉讼方关系,公开检索被大量同名干扰,**既不能证实也不能排除,不作断言**。
- (b) 校样版内部不一致的归因未定:Correlational(48)+ Longitudinal(30)= 78 与 All studies(79)差 1;Bespoke 行 k=21 但齐性检验 df=12。第三票读作「差的那 1 个即被排除的实验研究」,第二票认为无法判定是校样排版错误还是定稿已修正。**成稿不得依赖这两处数字。**

## 证据分级

- **篇 (a)(Ferguson et al. 2022,screen media meta):多源证实**。Table 1 全部主数字经两个独立 PDF 副本交叉提取一致,书目由 Crossref + 作者自引 + 第三方镜像三重确认。
- **篇 (b)(Ferguson et al. 2025,social media meta):单源已核**。三票均只取到作者自存的排版校样;卷期页与摘要经三处第三方独立确认,但表内数值为单一来源。**成稿引用 β=.061 / .075 / .044 时应可接受,但如需极高可靠度,标注「据作者自存校样版」。**
- **「女生受影响更大」:方向存争(实为不成立)**。点估计有差,调节检验不显著,估计量选择可让 p 从 <.001 摆到 .111。
- **「两篇独立互证」:未验证(实为不成立)**。作者与样本双重重叠。
- **整体立场背景:方向存争**。两篇由同一立场群体(「道德恐慌」框架)产出,判据阈值自定,合并量系统性取最保守值——**结论方向与作者先验一致,引用时须与相反方向的一手证据(如 C05/C12 组)并列呈现,不可单独承重「无关联」这一结论**。


---

# C08 最终判决:CORRECTED(3/3 票)

三票均判 CORRECTED。全部逐字引语 (a)–(d)(g) 成立,但样本口径 (f)、PHQ-9 构念 (c)、22% 分母 (b)、pretrends/稳健估计量的强度 (e) 四处必须修正;并须补入论文自身附录 Table A.13 暴露的显著性脆弱性——这是全组最重要的新增发现,三票独立命中。

## 锁定口径(成稿必须用)

### 书目与来源
- Braghieri, L., Levy, R., & Makarin, A. (2022). *Social Media and Mental Health*. **American Economic Review, 112(11): 3660–3693**. DOI 10.1257/aer.20211218。三票均以已刊版 PDF(https://alexeymakarin.github.io/assets/Braghieri_Levy_Makarin_AER_2022.pdf)+ 官方 Supplemental Appendix 逐字比对。

### (a) 主效应
- 逐字:"Our index of poor mental health, which aggregates all the relevant mental health variables in the NCHA survey, **increased by 0.085 standard deviation units** as a result of the introduction of Facebook."
- **Table 1 四列**:0.137 (0.040) / 0.124 (0.022) / **0.085 (0.033,首选设定:survey-wave FE + college FE + controls)** / 0.077 (0.032,加扩张组线性趋势)。**Observations = 359,827**(第 1 列 374,805)。SE 按 college 聚类。
- **单位**:指数在**处理前期**标准化(Table 1 注:"standardized so that, in the preperiod, it has a mean of zero and a standard deviation of one"),**不是任何临床量表的 SD**。
- 引用 0.085 时宜注明跨设定区间为 **0.077–0.137**。

### (b) 「= 失业效应的 22%」
- 逐字:"As a point of comparison, this magnitude is around 22 percent of the effect of losing one's job on mental health, as reported in a meta-analysis by Paul and Moser (2009)."
- **脚注 20 的限定必须一起带上**:"The estimates from Paul and Moser (2009) that can most credibly be interpreted as causal and hence be compared to our estimates are those that rely on quasi-experimental variation in job loss due to factory closures and mass layoffs."
- **【硬性禁止】不得写「相当于失业总体效应的 22%」**。正确表述:「相当于 Paul & Moser 中**依赖工厂关闭/大规模裁员这类准实验变异**的那部分估计的约 22%」,并注明**论文正文、脚注、Online Appendix、2021 工作论文版均从未给出该分母的数值**。反推分母 ≈ 0.085/0.22 ≈ 0.386 SD;若误用 P&M 的头条总体效应 d = 0.51,得到的是 ~17% 而非 22%。

### (c) 「PHQ-9 +2pp / 基线 25%」
- 逐字:"The effect of the introduction of Facebook on our index of poor mental health is equivalent to a 2 percentage point increase in the share of students suffering from depression according to the PHQ-9 over a baseline of 25 percent."
- 正文相对量:"The 2 percentage point increase corresponds to a 9 percent increase over the preperiod mean of 25 percent for depression and a 12 percent increase over the preperiod mean of 16 percent for generalized anxiety disorder."
- **【构念修正·必须写明】NCHA 从未施测 PHQ-9**。该数字是**模型预测(imputed)分类**:作者另做一份 Prolific 全职大学生验证调查(原始 523、清洗后 507 有效),学出把 NCHA 症状题映射到「PHQ-9 ≥ 10(中度/重度抑郁)」的权重(OLS/Logit/LASSO 三法),再外推回 2000–08 的 NCHA 样本。指数与 PHQ-9/GAD-7 的相关分别为 0.66 / 0.61。
- **Table A.30 实际系数**:PHQ-9 0.023(OLS)/ 0.022(Logit)/ 0.022(LASSO),SE 0.009,N=359,827;**「2 个百分点」是 2.2–2.3pp 的四舍五入**。GAD-7 为 0.019 / 0.017 / 0.022。
- **【设定依赖】「基线 25%」只对 OLS/Logit 预测器成立;LASSO 预测器的 predicted baseline mean 是 0.42**——同样约 2.2pp,相对增幅就只有约 5% 而非 9%。GAD-7 对应基线 0.16/0.17/**0.33**。
- 附录 Table A.28:Prolific 样本症状率远高于 NCHA(Had symptom/disorder 0.232 vs 0.082),即权重来自一个心理健康明显更差、且相隔约十五年的人群。

### (d) 「解释 24% 的抑郁上升」
- 逐字:"Under a set of relatively strong assumptions, we calculate that the introduction of Facebook accounts for approximately 24 percent of such increase." 正文:"Such calculation relies on strong assumptions and should therefore be interpreted with caution."
- **算式(脚注 22)**:24% = **2.96pp / 12.15pp**。分子 = Facebook 使「过去一年至少一次严重抑郁到难以正常生活」的自报比例上升 2.96pp(p<0.05);分母 = ACHA 2000–2019 汇总报告口径下该比例的上升幅度 12.15pp(2008 年题目措辞变更造成序列断点,用年份哑变量 + 春/秋哑变量 + 新措辞哑变量回归,取 2019 年固定效应)。
- **构念 = severe depression at least once in the past year 这一单一自报题项**,不是泛指「抑郁」,不是 PHQ-9,不是整体心理健康指数;时间窗是 2000–2019,不是研究期 2004–2006。
- **三条假设逐字**:"(i) Facebook utilization rates among college students did not change substantially after 2004–2005; (ii) the effects of Facebook did not change over time; (iii) Facebook does not have cumulative effects."
- **作者自我拆台必须一并写出**:脚注 23 明说本文 Section IVC(效应随暴露时长增强)"already casts some doubt on assumption (iii)"——**即作者自己指出其中一条假设与自家结果相悖**。

### (e) pretrends 与四种稳健估计量
- 逐字:"Figure 2 presents the event-study figures and shows that the estimates are consistent with the parallel trends assumption: independently of the estimator used, the coefficients on the semesters prior to the introduction of Facebook at a college are all close to zero and exhibit no discernible pretrends."
- **【必须限定】这是目视/系数接近零的图形判读,论文未报告任何 pre-trend 联合检验**。附录中唯一的 F-test(joint significance, p=0.86, N=377,614)是**人口学协变量平衡检验**,与 pretrend 无关。
- 四种估计量:De Chaisemartin & d'Haultfœuille (2020)、Borusyak, Jaravel & Spiess (2021)、Callaway & Sant'Anna (2021)、Sun & Abraham (2021);Figure 2 共五条线(含 TWFE OLS),横轴 −8 至 +2。
- **【必须限定】「四种稳健估计量都支持」要降级为「四取三显著,量级散布近两倍」**。Online Appendix **Table A.16**(均**不含控制变量**):
  - Borusyak-Jaravel-Spiess **0.107** (SE 0.030), CI [0.048, 0.166]
  - Callaway-Sant'Anna **0.113** (0.046), CI [0.023, 0.203]
  - **de Chaisemartin-d'Haultfœuille 0.075 (0.073), 95% CI [−0.069, 0.218] —— 跨零、不显著**
  - Sun-Abraham **0.164** (0.042), CI [0.081, 0.247]
  - 作者措辞是 "qualitatively similar",并未声称四个都显著。
- **窗口硬约束**:Figure 2 注 "the maximum number of postperiods that can be estimated robustly is two";Borusyak 只估 4 个 pre-period(更多会令标准误暴涨),dCdH 面板上限 5 个 pre-period。**「无 pretrends + 四估计量稳健」必须配上「事后动态只看得到两学期」。**

### 【新增·三票独立命中】显著性对扩张组的脆弱性(全文最脆弱处)
- Online Appendix **Table A.13 Panel (a)**(逐一剔除某一 Facebook 扩张组,基线 DiD):
  - 剔除 Group 1:**0.059 (0.040), t≈1.48 —— 5% 与 10% 水平均不显著**,N=293,112
  - 剔除 Group 2:0.096 (0.034),显著,N=216,328
  - 剔除 Group 3:0.094 (0.038),显著,N=268,554
  - 剔除 Group 4:**0.084 (0.044), t≈1.91 —— 5% 水平不显著**,N=301,487
- **Panel (b) length-of-exposure 设定(不依赖学院层面平行趋势)在四种剔除下全部保持显著**:0.015 (0.005) / 0.017 (0.006) / 0.020 (0.005) / 0.023 (0.005)。
- 正文脚注 17 的说法是 "our results do not significantly change when we drop colleges in each expansion group in turn" / "results remain fairly stable across the various restricted datasets"——**就点估计成立,就统计推断会让读者高估稳健性**。
- **成稿引用 0.085 主效应时,必须同时给出这一敏感性与补偿性的 Panel (b) 结果。**

### (f) 样本口径(三票一致判定为最重要的口径偏差)
- **775 = Facebook 上线日期数据集的规模,不是分析样本**。逐字:"the first dataset specifies the dates in which Facebook was introduced at 775 US colleges";附录 Table A.32 逐校列表编号至 775;Table A.1 表注 "refer to the full set of 775 colleges from the Facebook introduction dates dataset"(因 NCHA 剥掉了学校标识、无法与 IPEDS 匹配)。
- **430,000+ = NCHA 原始问卷池(2000 春–2008 春全部应答),不是回归样本**。逐字:"Our second main data source consists of more than 430,000 responses to the NCHA survey"。
- **正确表述**:775 所大学的开通日期数据 × NCHA 43 万+ 份原始问卷,合并后**主回归样本 = 420 所大学、359,827 份观测**。Table A.1 末行 "Number of colleges (NCHA subsample)" = 40+124+120+136 = **420**;Table A.17 直接标 **Clusters = 420**。
- **处理变异的粒度必须写明**:因隐私原因 ACHA 只给「上线学期」,处理变量是「expansion group g 在 wave t 是否已有 Facebook」,**实际只有 4 个扩张组**(2004春 / 2004秋 / 2005春 / 2005秋)。作者自陈:"Since we only have four expansion groups, which is lower than the number of clusters necessary for asymptotics to work",故在组层面聚类时补做 wild bootstrap(**p = 0.015**);Table A.17 三种聚类的 cluster 数为 420 / 4 / 67。**只出现在 NCHA、不在日期数据集里的学校被统一插补为 2005 秋(脚注 15)。**
- 附带小瑕疵:Table A.1「Number of colleges」行 58+231+263+204 = 756 ≠ 775,差 19 所(论文未解释,应为 IPEDS 合并未匹配)。
- 另一处敏感性:Table A.14 显示,对「恰在开通学期受访」者改用其他处理归类时,点估计从 0.085 降到 **0.043–0.071**。
- NCHA 平均应答率 37%,样本限于 **full-time undergraduates**,面板 unbalanced。

### (g) 作者自设的三条 caveat(逐字)
- **外推**:"we note that our estimates are **local to college students**, a population of direct interest in the discussion about the recent worsening of mental health trends among adolescents and young adults. Nevertheless, future research should test whether social media has a similar effect on the mental health of other demographic groups."
- **自报测量**:"despite being the core component of most mental health diagnoses, self-reports may still suffer from measurement error due to recall bias, lack of incentives, and social image concerns."
- **【逐字口径修正】功能外推警告举的例子是 "news pages",不是 "News Feed"**:"our estimates cannot speak directly to the effects of social media features (e.g., news pages) that were introduced after the time period we analyze"。成稿若要写这条,应改为「不能外推到本文时间窗之后引入的社媒功能(论文举例 news pages)」。
- 补充限定:NCHA 无社媒使用问题,估计量是**直接效应 + 同侪溢出效应的合计**(脚注 19 用 85% 渗透率论证不太可能主要由未加入者驱动);处理时点在**学校层面**,非个体层面。

### (h) 反证检索结果
- **截至 2026-07,无任何已发表的 Comment / Reply / Erratum / Corrigendum**。AEA 官方文章页(https://www.aeaweb.org/articles?id=10.1257/aer.20211218)附加材料仅三项:Replication Package(doi 10.3886/E175582V1)、Supplemental Appendix、Author Disclosure Statement(s)。该文亦**不在 i4replication.org 的复现报告清单中**。
- **但存在两份实质性的非同行评审批评,成稿不得写「未受挑战」**:
  1. **Dean Eckles(MIT Sloan)**,"thefacebook and mental health trends: Harvard and Suffolk County Community College",发于 **Andrew Gelman 的 Statistical Modeling 博客,2023-08-22**(第三票经 Wayback 快照 20240411002452 取得全文)。核心逐字主张:"It turns out that one needs both the first and the last (fourth) expansion groups in the analysis to find statistically significant estimates";并指出组 1(哈佛/常春藤)与组 4(社区学院)在 2000–2003 基线心理健康指数上的差距 "around the same size as the authors' preferred estimate"。**该主张已由论文自身 Table A.13 独立证实。** 文末 P.S. 记录作者回应:剔除组 1 也可能造成**向下**偏误(因效应随暴露时长与基线易感性上升);Eckles 回应称其关切在内部效度而非外部效度。
  2. **David Stein**,Shores of Academia(Substack)系列("Facebook Expansion: Invisible Impacts?" 等)。要点:论文正文/附录/复现包均未给出 2000–2008 期间 NCHA 抑郁比例的原始趋势图表;其自行汇编的 NCHA 数据显示 2006–2007 抑郁流行率相对 2002–2003 反而下降;并质疑正文「mid-2000s 开始恶化」的框架与论文自身附录不符。未重做系数估计,未见作者回应。
- **成稿表述**:「无已发表的期刊 comment,但有一份**基于论文自身附录、可独立复核**的公开方法学批评(Eckles),以及一份未经复算的博客质疑(Stein)。」

### 利益相关
- 披露逐字:"**Levy is an unpaid member of Facebook's 2020 Election Research Project**"——属向被研究对象方向的潜在关联,但为无薪、且论文结论对 Facebook 不利,**方向上不构成有利偏倚**。
- 资助:DFG CRC TRR 190(项目 280092119)与 Foerder Institute,**非平台资助**。Facebook 扩张日期由 Wayback 快照与既有学术数据集重建,NCHA 数据来自 ACHA(ACHA 另附免责声明,不为文中信息准确性背书)。DellaVigna 任 coeditor。**未发现来源利益冲突。**

## 修正记录(修正前→修正后)

1. 「775 所大学参与分析」→ **775 是 Facebook 上线日期数据集规模;进入回归的是 420 所**(Table A.1 NCHA subsample / Table A.17 Clusters=420)。
2. 「NCHA 43 万+ 问卷进入估计」→ **43 万+ 是原始问卷池;主回归 Observations = 359,827**(无控制变量列 374,805)。写「43 万+ 参与估计」属放大约 20%。
3. 「775 所学校错时上线提供变异」→ **实际只有 4 个扩张组**;组层面聚类下 cluster 数为 4,需 wild bootstrap(p=0.015);无日期学校统一插补为 2005 秋。
4. 「PHQ-9 实测抑郁比例 +2pp、基线 25%」→ **NCHA 从未施测 PHQ-9;这是由 507 人 Prolific 验证调查学出的权重外推的预测分类**;实际系数 0.022–0.023(SE 0.009);**「基线 25%」为设定依赖,LASSO 预测器下基线为 0.42(相对增幅仅约 5%)**。
5. 「24% 的青少年抑郁上升由 Facebook 解释」→ **分母是 ACHA 口径下美国大学生「过去一年至少一次严重抑郁」比例 2000→2019 上升的 12.15pp,分子 2.96pp**;构念为单一自报题项;且作者脚注 23 自承三条假设中的 (iii) 被自家 Section IVC 结果 "casts some doubt on"。
6. 「= 失业效应的 22%」→ **= Paul & Moser 中工厂关闭/大规模裁员准实验估计的 22%;论文从未给出该分母数值**。用 P&M 头条 d=0.51 则为 17%,不可自行反推后当作论文口径。
7. 「无 pretrends」是硬结论 → **是图形判读,无任何 pre-trend 联合检验;事后动态最多只估两个 post-period**。
8. 「四种稳健估计量都支持」→ **四取三显著;dCdH 为 0.075 (0.073), CI [−0.069, 0.218] 跨零不显著;点估计跨度 0.075–0.164;且 Table A.16 均为无控制变量设定**。
9. 「结果在逐组剔除下稳健」(论文脚注 17)→ **点估计稳、显著性不稳:剔除首组 0.059 (0.040) 与剔除末组 0.084 (0.044) 均不过 5%**;补偿性事实是 length-of-exposure 设定四次剔除后全部显著(0.015–0.023)。
10. 「作者警告不能外推到 News Feed 之后的社媒」→ **论文原话举的例子是 "news pages"**。
11. 「该研究未受挑战」→ **无已发表 comment,但有 Eckles(Gelman 博客,2023-08-22)与 Stein(Substack)两份公开批评,前者的量化主张已被论文自身 Table A.13 证实**。
12. 【三票冲突裁决】第一票称剔除 Group 4 的 0.084 「显著」,第二、三票称 t≈1.91、5% 水平不显著 → **裁决采信第二、三票**:0.084/0.044 = 1.91,双尾 p≈0.056,**不过 5%**。算术直接可验,第一票该处判断有误。

## 未回溯项

- **【三票均未回溯,不得承重】Paul & Moser (2009, JVB 74: 264–282) 中「工厂关闭/大规模裁员」准实验子组的具体 Cohen's d**。ScienceDirect 付费墙、ResearchGate 403、Semantic Scholar 标 openAccessPdf CLOSED、daneshyari 仅前 3 页预览(有摘要无 moderator 表)、多个镜像均不含 moderator 分组表。**BLM 论文本身也从未写出该分母,这一环在公开文献链上是断的。** 成稿若用 22%,须照抄论文措辞并注明分母未公开,**不要自行反推**。可确定的二手信息:P&M 摘要逐字 "The average overall effect size was d = 0.51 with unemployed persons showing more distress than employed persons"(0.085/0.51 = 16.7%,佐证 BLM 用的不是这个头条数字)。
- **【三票均未回溯】openICPSR 复现包(doi 10.3886/E175582V1)需登录,未下载核验**。因此 0.085 系数与 24% 的 back-of-envelope 均未做代码复算;所有数字来自已发表 PDF 与官方 Supplemental Appendix 的逐字比对。也未能确认包内是否有 22% 的计算脚本。
- **【三票均受限】2025–2026 年是否新刊出针对本文的正式 comment,无法穷尽排除**。三票的 WebSearch 配额均在核查过程中耗尽。已定点确认的两个权威登记处(AEA 文章页、i4replication.org 报告清单)均无记录——属强证据,但非穷尽性证明。建议后续以 Google Scholar 引文列表或 EconLit 做一次收口检索。
- Vuorre & Przybylski(2023, Royal Society Open Science,72 国 946,798 人,报告 Facebook 采纳与主观幸福感无一致关联)作为方向相反的旁证,仅经检索摘要获知,**未取回一手核对其构念(主观幸福感 vs 抑郁症状)、人群(成年人全龄 vs 大学生)与设计(国家层面 vs 校园错时上线)的可比性**。未核实前不应把它当作对本文的直接反驳。
- 本文第二条识别策略(校内 college×survey-wave 固定效应下的「暴露时长」设定,方程 4)未被本次核查逐项验算;Eckles 亦明确表示未评估该设定。它在 Table A.13 Panel (b) 四种剔除下均显著,但**其自身的识别假设未被检验**。

## 证据分级

- **主效应 0.085 SD 与全部逐字引语:多源证实**。三票各自独立取回已刊 AER PDF + AEA 官方 Supplemental Appendix,逐字比对结果完全一致;另有 2021 工作论文版佐证措辞未变。
- **样本口径(420 所 / 359,827 观测):多源证实**。Table A.1、Table A.17 两处交叉自洽。
- **PHQ-9「2pp / 基线 25%」:单源已核,但为模型预测量,且设定依赖**。引用必须带「预测/推算」与「LASSO 下基线 0.42」两个限定。
- **「= 失业效应 22%」:未验证**。分母在整个公开文献链上不可回溯。**不得作为承重对比使用**;若要用,只能转述论文措辞并明确标注分母未公开。
- **「24% 由 Facebook 解释」:单源已核,但属作者自标「relatively strong assumptions」的 back-of-envelope,且其中一条假设被作者自家结果削弱**。**只能作为量级示意,不可承重。**
- **主效应的统计显著性:方向存争**。点估计跨设定稳健(0.043–0.164),但 5% 显著性同时依赖保留首、末两个扩张组;dCdH 估计量下跨零。**成稿宜写「点估计稳定在 0.06–0.16 区间,显著性对扩张组构成敏感」,不宜写成「稳健显著」。**
- **利益相关:无有利偏倚**。唯一关联(Levy 无薪参与 Facebook 2020 选举研究项目)方向与结论相反;资助非平台。


---

# C09 最终判决:CORRECTED(3/3 票)

三票均判 CORRECTED。两条逐字引语完全成立,但 N=2,743、「WTA<$102 的 61%」、合规率、估计量类型、以及「心理干预」这个对标基准五处口径必须修正。最关键的一条:**0.09 SD 是在 N≈1,637 上估的 LATE,不是在 2,743 人上估的 ITT**。

## 锁定口径(成稿必须用)

### 书目与版本
- Allcott, H., Braghieri, L., Eichmeyer, S., & Gentzkow, M. (2020). *The Welfare Effects of Social Media*. **American Economic Review, 110(3): 629–676**。DOI 10.1257/aer.20190658。
- **【版本注】常被引用的 URL(web.stanford.edu/~gentzkow/research/facebook.pdf)实际提供的是 2019-11-08 工作论文版**(= NBER WP 25514,2019-01 初版 / 2019-11 修订)。第一、二票已对印刷版镜像(gwern.net/doc/sociology/technology/2020-allcott.pdf,页眉 "VOL. 110 NO. 3 … MARCH 2020",页码 629-676)与工作论文版逐字比对:**本组所有数字与措辞两版完全一致**。唯一排印差异:印刷版为 en dash "25–40 percent"。

### (b) 0.09 SD 与 25–40% 对标(逐字,印刷版)
> "Our overall index of subjective well-being improved by **0.09 standard deviations**. As a point of comparison, this is about **25–40 percent** of the effect of psychological interventions including self-help therapy, group training, and individual therapy, as reported in a meta-analysis by Bolier et al. (2013)."

- 正文 §5.3 的准确表述(**成稿应优先用这一版,引言那版省掉了 "positive"**):
> "a meta-analysis of 39 randomized evaluations finds that **positive psychology interventions** (i.e. self-help therapy, group training, and individual therapy) improve subjective well-being (excluding depression) by 0.34 standard deviations and reduce depression by 0.23 standard deviations (Bolier et al. 2013). Thus, deactivating Facebook increased our subjective well-being index by about 25-40 percent as much as **standard psychological interventions**."
- **25–40% 不是置信区间**,是 0.09 除以 Bolier 两个不同结局:0.09/0.34 = 26%(主观幸福感,不含抑郁);0.09/0.23 = 39%(抑郁)。
- **【硬性禁止】不得写成「相当于看心理医生效果的 25–40%」**。Bolier 2013 是**积极心理学干预**(自助疗法/团体训练/个体治疗)的元分析,不是临床心理治疗或抗抑郁治疗。

### (c) 相关 vs 因果(逐字)
> "However, we also show that the magnitudes of our causal effects are **far smaller than those we would have estimated using the correlational approach of much prior literature**."

- 量化支撑(§5.3 逐字):"The baseline correlation between our SWB index and Facebook use is about **three times larger** than the experimental estimate of the treatment effect of deactivation (**about 0.23 SD compared to 0.09 SD**), and the point estimates are highly statistically significantly different."

### 0.09 SD 的完整统计口径
- **Online Appendix Table A12**:Subjective well-being index **估计 0.09,SE 0.04,p = 0.02,sharpened FDR q = 0.03**(Benjamini-Krieger-Yekutieli 2006)。显著性属边际。
- **分项**:life satisfaction 0.12 SD、anxiety 0.10 SD、depression 0.09 SD、happiness 0.08 SD,"All of these effects remain significant after adjusting for multiple hypothesis testing"。
- **【必须保留的限定语】高频短信测量未达显著**:紧邻 0.09 SD 那句之前,论文自己写 "Effects on subjective well-being as measured by responses to brief daily text messages are positive but **not significant**"(点估计 0.01–0.06 SD)。**显著的是回溯式 endline 问卷测量;低回忆偏倚的实时测量不显著。单引 0.09 SD 而丢掉这句,会掩盖这一内部张力。**
- 原始单位参照:happiness 对照组均值 4.47/7、增加 0.12;life satisfaction 12.26/21、增加 0.56。

### 【最重要】样本 N 的三级口径
- **2,743 = 收到 BDM 报价的人数**(论文摘要措辞确为 "We recruited a sample of 2,743 users",故引 2,743 忠于论文自述)。
- **真正估计全部处理效应的 impact evaluation sample = N=1,661**(Treatment **580** / Control **1,081**,Table 3 Observations);完成 endline **1,637**;post-endline 手机用量仅 **1,219**。
- **成稿表述:「0.09 SD 估计于 N≈1,637」。用 N=2,743 描述该实验的效应量样本,把分析样本夸大约 65%。**
- **完整招募漏斗(三票逐行核对一致)**:1,892,191 人看到广告 → 32,201 点击(CTR 1.7%)→ 22,324 完成预筛 → 20,959 为美国居民且生于 1900–2000 → 17,335 日均 Facebook 使用 15–600 分钟 → 7,455 同意参与 → 3,910 完成 baseline → **2,897 有效并被随机化** → **2,743 收到报价** → **1,661 进入影响评估样本** → endline 1,637 → post-endline 1,219。**自选择层层收窄,是外部效度的主要限制。**

### 「61%」的方向与机制顺序
- 逐字:"We then randomly assigned the **61 percent of these subjects with WTA less than $102** to either a Treatment group that was paid to deactivate, or a Control group that was not."
- **【方向修正】是「2,743 人中有 61% 的人 WTA<$102」(1,661/2,743 = 60.6%),不是「WTA<$102 的人里有 61% 被随机化」。**
- **【机制顺序修正】论文引言这句是简写。实际顺序相反**:2,897 名有效 baseline 者**先**被随机分配到报价组(p=$102 约 33%、p=$0 约 67%、p~U[0,$170] 约 0.2%,在 48 个分层内平衡);**WTA<$102 是随机化之后**用来界定 impact evaluation sample 的筛选条件。分组非对半,故 580 vs 1,081。
- $102 阈值理由(脚注 11 逐字):"We chose $102 because our pilot data correctly suggested that there would be a point mass of WTAs at $100 and that it would maximize statistical power per dollar of cost";$170 为上限因 "it was the maximum that we could pay participants without requiring tax-related paperwork"。

### 合规率
- 引言逐字:"the Treatment group's compliance with deactivation **exceeded 90 percent**"——**该引语本身成立**。
- **但底层实测恰为 0.90**:Table 3 "Share days deactivated" Treatment = **0.90 (SD 0.29)**,Control = **0.02 (SD 0.13)**,p=0.00;正文 §3 作 "deactivated on 90 percent of checks between October 13 and November 7"。
- **【口径修正】严格说是「约 90%」而非「>90%」;且这是按公开主页 ping 的「检查次数占比」定义的 check 层面指标,不是账号级或人层面的二元合规率。SD 0.29 意味着相当一部分 Treatment 组成员在不小比例的时间里重新激活了账号;Control 组也有 2% 的时间处于停用状态。**
- Table 3 其余:Completed endline survey 0.99/0.98;Share of text messages completed 0.92/0.93;Completed post-endline survey 0.95/0.92。

### 【构念修正】估计量类型 = LATE,不是 ITT
- 逐字:"τ measures the **local average treatment effect** of deactivation for people induced to deactivate by the promised $102 payment."
- 设定:Equation (1) Yi = τDi + ρȲbi + νs + εi,以指派 Ti 作 Di(抽查中被观测为停用的比例)的工具变量,2SLS,稳健标准误。论文明确 "In the body of the paper, we present figures with local average treatment effects and 95 percent confidence intervals"。
- **预分析计划 2018-11-07 修订版明确改为 "use IV estimates instead of intent-to-treat estimates"**,理由是观察到的不合规原因;该调整为事前、有据。ITT 会小于 0.09。
- **成稿表述:「停用 Facebook 四周对依从者的 LATE 为 0.09 SD」**;且样本本身按 WTA<$102 筛选,即**相对不看重 Facebook 的人**。

### Bolier 2013 基准(一手核实)
- Bolier et al. (2013), *BMC Public Health* 13:119, PMC3599475。**39 项随机对照研究、6,139 名被试**。
- subjective well-being **d=0.34 [0.22, 0.45]**;psychological well-being **d=0.20 [0.09, 0.30]**;depression **d=0.23 [0.09, 0.38]**。→ **Allcott 等对该 meta 的数值引用准确,25–40% 的算术成立**(0.09/0.34=26.5%,0.09/0.23=39.1%)。
- **【必须一并写出的基准脆弱性】**
  - Bolier 自陈:"Indications for publication bias were found for **all outcome measures**";"no study met all of our quality criteria"(仅 1 项高质量[Mitchell 2009]、18 项中等、**20 项低质量**,平均质量分 2.56/6);仅 7/39 报告充分的随机化隐藏、仅 3/39 做 ITT 分析、0 项报告充分效能分析;I²=49.5%(SWB)/ 29.0%(psych WB)/ 47.0%(抑郁);多为 completers-only 分析。
  - **Trim-and-fill 校正后**:psychological well-being 与 depression 均从 0.20 / 0.23 降至 **0.16**。若用校正后的抑郁值,比值变为 0.09/0.16 ≈ **56%**。
  - **White, Uttl & Holder (2019), PLoS ONE, 10.1371/journal.pone.0216588** 对 Bolier 做小样本偏倚校正后:抑郁 r=.11→**.02**、心理幸福感 r=.10→**.02**、主观幸福感 r=.17→.13;结论 PPI 对 well-being 的效应约 r=.10。
  - **方向裁决:分母若有偏差是被高估的,即「25–40%」若失真是偏保守——实际相对比值可能更高。这与「所以这个效应很小」的常见引用意图方向相反。成稿若用 25–40% 表达「效应小」,必须同时披露基准本身建立在弱证据上。** 另:论文只取了 Bolier 的 0.34 与 0.23,未取 psychological well-being 的 0.20;若纳入,区间上沿为 0.09/0.20 = 45%。

### 设计与人群
- **四周**成立:摘要 "deactivating Facebook for the **four weeks** before the 2018 US midterm election";BDM 询问的是 "stay deactivated for four weeks rather than 24 hours";midline→endline 为 weeks 1–4,endline 后另有 weeks 5–8 的第二次 BDM。
- **入选规则逐字**:"a US resident **born between the years 1900 and 2000** who uses Facebook more than 15 minutes and no more than 600 minutes per day"。**这是出生年份切口,不是显式 18 岁门槛。**
- **【必须附的代表性警告】Table 2(impact evaluation / Facebook 用户 / 美国成人)**:**Age under 30 = 0.52 / 0.26 / 0.21**(中位年龄 31.5 岁);**College 0.51 / 0.33 / 0.29**;Income under $50,000 0.40/0.41/0.42;Male 0.43/0.44/0.49;White 0.68/0.73/0.74;Democrat 0.42 / — / 0.20;Republican 0.13 / — / 0.26;**Facebook minutes 74.52 / 45.00 / —**。
- **成稿表述:「偏年轻、偏高学历、偏民主党、重度用户的成年人自选样本」;研究对象是 2018 年的 Facebook,不涉及青少年、不涉及 Instagram/TikTok。用于青少年屏幕时间议题时只能作为成人类比证据,绝不可外推。**
- **作者自设的外推限制(脚注 23 逐字)**:"the treatment effects in our sample from a four-week deactivation are unlikely to generalize to the US population over Facebook's 15-year life";§5.3 另指出效应不随时间递增,"if anything, the point estimates are largest in the first week"——**「更长时间停用效应更大」没有证据支持**。
- **实验者需求效应(论文自设检验)**:endline 问 "Do you think the researchers in this study had an agenda?",Treatment 与 Control 各有 62% 认为无特定议程或不确定;论文承认 "demand effects could arise for the remaining 38 percent"。多数结局为自报。

### 预注册与利益相关
- **AEARCTR-0003409**(socialscienceregistry.org/trials/3409)双向核实:题为 "Evaluating Social Media",PI 为 Allcott(NYU)、Braghieri/Eichmeyer/Gentzkow(Stanford)及 Raj Bhargava,注册日 2018-10-11,干预期 2018-10-11 至 2018-12-06,计划样本 3,051(实际随机化 2,897),状态 Completed。PAP 初版 2018-10-12 提交("as this was the final day before the Treatment and Control groups could have begun to differ"),修订版 2018-11-07。
- 资助:**Sloan Foundation 与 Knight Foundation——无 Facebook/Meta 资助**。
- 披露逐字:"Allcott is a paid employee of Microsoft Research. Gentzkow does paid consulting work for Amazon and is a member of the Toulouse Network for Information Technology, a research group funded by Microsoft. Braghieri and Eichmeyer have no relevant or material disclosures."
- 致谢中出现 Nancy Baym、Moira Burke、Annie Franco、Alex Leavitt(当时均为 Facebook 研究人员),**仅为评论致谢,无资助、无数据供给、无发表审批权**;招募通过付费 Facebook 展示广告,未获 Facebook 内部数据。IRB:Stanford eProtocol #45403、NYU IRB-FY2018-2139。
- **AEA 官方文章页未列任何 erratum / correction / corrigendum / comment-reply**(截至 2026-07-27)。

## 修正记录(修正前→修正后)

1. 「N=2,743」作为效应估计样本 → **2,743 是收到 BDM 报价的人数;impact evaluation sample N=1,661(T 580 / C 1,081),endline 1,637,post-endline 1,219**。夸大约 65%。
2. 「WTA<$102 的 61% 被随机化」→ **方向反了:2,743 人中有 61% 的人 WTA<$102(1,661/2,743=60.6%),这 61% 构成被分入处理/对照的样本**。且机制顺序相反:随机化在 baseline 阶段(N=2,897)先完成,WTA<$102 是事后筛出分析样本的条件。
3. 「0.09 SD」未标估计量 → **是 LATE / IV 估计(2SLS,以指派为工具变量),不是 ITT,也不是总体 ATE;对应人群是被 $102 诱导而停用的 complier**。
4. 「合规>90%」→ **引言原话成立,但实测为 0.90 (SD 0.29),且是「停用天数/抽查次数占比」的 check 层面指标,非人层面二元合规;Control 组亦有 2%**。
5. 「psychological interventions(心理干预)」→ **positive psychology interventions(积极心理学干预:自助疗法/团体训练/个体治疗)**,不是临床心理治疗。
6. 「25–40%」被读作效应量区间 → **是 0.09 除以两个不同结局(0.34 SWB / 0.23 抑郁)的比值区间,不是置信区间**。
7. 「25–40% 说明效应小」→ **分母(Bolier)自陈全部结局有发表偏倚、39 项中 20 项低质量、trim-and-fill 后抑郁降至 0.16;White et al. 2019 小样本偏倚校正后抑郁 r 从 .11 降到 .02。校正后基准下,0.09 SD 的相对占比远高于 25–40%,方向与「所以很小」的引用意图相反。**
8. 「成人样本」→ **成立(入组规则为出生年份 1900–2000,零青少年覆盖),但样本在成年人中极不具代表性:52% 未满 30 岁(FB 用户 26%、美国成人 21%)、51% 大学学历(美国 29%)、日均 FB 74.5 分钟(普通用户 45 分钟)、民主党 42% vs 共和党 13%**。
9. 「引自 AER 2020」+ Stanford URL → **该 URL 是 2019-11-08 工作论文;发表版为 AER 110(3): 629–676。两版本组数字与措辞逐字一致,仅 en dash 排印差异。**
10. 「0.09 SD 是停用四周的效果」→ **须并列「高频短信实时测量的 happiness 不显著(0.01–0.06 SD)」这一内部张力**。

## 未回溯项

- **【三票均未回溯,须标未验证】是否实际入组过 17 岁被试**。入组规则是「生于 1900–2000 年」而非「年满 18 岁」,baseline 在 2018 年 9 月,理论上允许 2000 年下半年出生者(当时 17 岁)进入;论文未报告最小年龄或年龄分布下限,AEA 注册页亦未列显式年龄标准。**「零青少年」这一表述只能依据入组规则推断,不能作为已验证事实承重。**
- **【三票均未回溯】openICPSR 复制包(project 112081 / 117761)未下载**(需登录 / 返回 403)。因此 0.09 SD 及其标准误未做独立重算,仅核对了论文正文与附录表所报数值的内部一致性;也未能确认是否存在数据层面的事后更正。
- **【三票均受限】2020 年后针对本文的已发表评论/回复/失败复制,未做系统性检索**(三票的 WebSearch 配额均已耗尽)。已用 WebFetch 直接核过 AEA 官方文章页(无 erratum / comment / reply 记录),但这不等同于完整文献检索。**特别是 Allcott 等 2023–2025 年围绕 2020 年大选的 Facebook/Instagram 大规模停用实验(PNAS 2024 doi:10.1073/pnas.2321584121;NBER w33697,见 C10 组)对本文 SWB 结论的支持或反驳情况,本组未核实——不要据印象引用。**
- **【三票均未回溯】AER 发表版付费全文正文未直接读取**,故无法逐字确认 0.09 SD / 25–40 percent / 61 percent / compliance exceeded 90 percent / correlational approach 五处在**付印版**与 2019 工作论文完全一字不差。间接证据较强:第一、二票核了 gwern 的印刷版镜像(页眉/页码/DOI 齐全)且逐字命中,AEA 页摘要与工作论文摘要一致,NBER 记录显示末次修订为 2019-11。
- **【三票均未回溯】Bolier 2013 中 subjective well-being(d=0.34)是否经 trim-and-fill 校正**——一手报告中明确给出校正值的只有 psychological well-being 与 depression(均降至 0.16)。故「25–40%」区间**下端(0.09/0.34)是否也应上调,无法判定**。
- Online Appendix Table A1(与其余 12 项 Facebook 随机实验的对比)、A10/A11(各单项结局数值)、A17(SWB 与人口学的基线回归,"college completion 0.23 SD" 一说的来源)未取到一手,相关表述仅经正文转述核对。

## 证据分级

- **两条逐字引语 (b)(c):多源证实**。三票分别用工作论文版与已刊版镜像逐字比对,两版一致。
- **0.09 SD 的点估计与显著性(0.09, SE 0.04, p=0.02, q=0.03):单源已核**(Online Appendix Table A12,两票取到,第二票未取到)。
- **样本漏斗与 N=1,661:多源证实**。三票逐行核对 Figure 1 与 Table 3,数字完全一致。
- **合规率 0.90 与 Table 3:多源证实**。
- **AEARCTR-0003409 预注册:多源证实**(论文脚注 + 注册库页面双向)。
- **「25–40% of psychological interventions」这一对标:方向存争**。引语与算术均成立,但分母(Bolier 2013)已被其自身的质量/发表偏倚自陈与 White et al. 2019 的独立校正显著削弱,**校正后方向是让 0.09 SD 的相对占比上调,而非下调**。**该对比不宜作为「社媒效应很小」的承重证据。**
- **用于青少年议题:未验证(纯外推)**。零青少年覆盖,且样本在成年人中偏年轻/高学历/重度使用。
- **利益相关:无有利偏倚**。资助为 Sloan + Knight,非平台;披露透明;唯一可提的是致谢名单含当时的 Facebook 研究人员(仅评论致谢)。


---

# C10 最终判决:CORRECTED(3/3 票)

三票均判 CORRECTED。全部逐字引语与主数字成立(0.060 / 0.041 SD、p 值、"driven by" 摘要句、6周vs1周设计、"no news feed" 警告),但 N 的分母、统计量类型(LATE 非 ITT)、q 值 vs p 值、时间窗(5 周非 6 周)、年龄分箱口径、子组显著性强度六处必须修正。

## 锁定口径(成稿必须用)

### 书目与版本状态
- Allcott, H., Gentzkow, M., et al.(27 位作者)(2025). *The Effect of Deactivating Facebook and Instagram on Users' Emotional State*. **NBER Working Paper No. 33697, April 2025**。https://www.nber.org/system/files/working_papers/w33697/w33697.pdf
- **【必须披露】截至 2026-07-27:NBER 论文页无 Revision Date、无 published version、无勘误;RePEc(ideas.repec.org/p/nbr/nberwo/33697.html)亦无 "Published in" 条目。PDF 首页载明 "NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed."**——**成稿必须标注这是未经同行评审的工作论文。**
- 属 U.S. 2020 Facebook and Instagram Election Study;情绪状态为 **secondary outcome**,政治结果为 primary outcome(见姊妹篇 Allcott et al. 2024,同一 PAP 覆盖)。RCT 登记入口:https://osf.io/t9q2f。

### 样本 N 的两级口径
- **招募/主分析样本(逐字)**:"We recruited **19,857** Facebook users and **15,585** Instagram users who spent at least 15 minutes per day on the respective platform." 定义为「完成 baseline + 可链接平台数据 + 基线日均使用 ≥15 分钟」。
- **情绪效应的实际估计样本 = 完成 endline 者:Facebook 17,802 / Instagram 13,480**(流失率 **10% / 13%**)。论文自己的 **Figure 3 就把本文估计标为 "This paper (Facebook) (N = 17,802)" 与 "(N = 13,480)"**,并称总样本 31,282。
- **【必须披露】差异性流失**:"the Deactivation group was about **two percentage points more likely to finish endline** than the Control group, and this difference is statistically significant in our large sample."
- **招募漏斗**:FB 1,060 万邀请 → 673,388 点击 → 43,249 完成入组问卷 → 19,857;IG 260 万邀请 → 319,271 点击 → 42,658 → 15,585。作者自陈逐字:"The fact that **less than one percent** of the people who were invited to the study completed the experiment underscores that one should be cautious in generalizing results outside our sample." 且样本相对全体用户 "has a higher proportion of users with liberal views and high civic engagement"。

### 主效应
- **Facebook:0.060 SD**,单独 **p < 0.001**;**多重假设检验校正后 q = 0.002**(与 Allcott et al. 2024 全套政治结果一起校正)。引言逐字:"The effect is statistically distinguishable from zero at the p < 0.01 level, both when considered individually and after adjusting for multiple hypothesis testing."
- **Instagram:0.041 SD**,逐字:"The effect is statistically distinguishable from zero at the **p = 0.016** level when considered individually, and at the **p = 0.14** level after adjusting for multiple hypothesis testing along with the outcomes in Allcott et al. (2024). **The latter estimate does not meet our pre-registered p = 0.05 significance threshold.**"(原文 "p = 0.05" 带空格)
- **【统计量修正】0.14 是 q 值不是 p 值**:正文 4.3 节逐字 "The q-values adjusting for multiple hypothesis testing … are **0.002 and 0.139** for Facebook and Instagram"。**成稿写「校正后 q = 0.139(论文引言处自己写作 the p = 0.14 level)」。**
- **分项**(三票一致):
  - FB:happy **+0.064**(p<0.001)、depressed×(−1) **+0.039**(p=0.018)、anxious×(−1) **+0.028**(p=0.110)
  - IG:happy **+0.044**(p=0.030)、depressed×(−1) **+0.026**(p=0.156)、anxious×(−1) **+0.024**(p=0.205)——**三个分项中仅 happy 单独过 0.05**

### 【构念修正】0.060 / 0.041 是 LATE,不是 ITT
- 逐字:"τ measures the **local average treatment effect** of never using the platform instead of using the Control group average, for people induced to deactivate by the $150 payment."
- 设定:equation (1) 以 Deactivation 组指示变量 Ti 工具化停用依从度 Di,加 lasso 选出的控制变量与代表性权重。**第一阶段系数 FB 0.871 / IG 0.893 → 对应 ITT 约为 LATE 的 0.87 倍。**
- **成稿表述:「0.060 SD 的 LATE,含义是『完全不用该平台』vs『用到对照组平均水平』,且只对被 $150 报酬诱导而停用的 complier 成立」。**

### 【时间窗修正】6 周 vs 1 周,净差异暴露 5 周
- 设计逐字:"The Deactivation group was told that they would receive **$150** if they did not log into the focal platform for the next **six weeks**, while the Control group was told that they would receive **$25** if they did not log in for the next **week**." 分配比例 **Deactivation 27% / Control 73%**,按 36 个分层随机化。账号自 **9/23** 起统一停用;对照组 **9/30** 自动恢复、处理组 **11/4** 恢复。
- **【修正】效应是「6 周 vs 1 周」之差,实际差异暴露窗为 9/30–11/3 约五周**。论文自陈逐字:"our experiment measures the effects of an **incremental five weeks** of individual deactivation before the 2020 election";"During the **five weeks from September 30-November 3**, when only the Deactivation group was being paid to stay deactivated…";跨研究比较中自述 "the longest abstention period (**5 weeks**, compared to a prior maximum of 4 weeks)"。
- 设计意图逐字(值得引):"By including a short deactivation period for the Control group, we guaranteed that the only differences between Control and Deactivation were the total payment amount and deactivation length … This reduced the risk of experimenter demand effects, differential attrition, and any spurious effects that might be artifacts of the deactivation process itself."

### 异质性:摘要句 vs 底层检验
- **摘要逐字(可引)**:"Exploratory analysis suggests the Facebook effect is driven by people over 35, while the Instagram effect is driven by women under 25."
- **【必须并列的底层检验】**
  - FB:35+ vs 18-34 的差异检验 **p = 0.046**(勉强过 0.05)
  - IG:18-24 岁女性组内点估计 **0.111 SD(p = 0.002)**,"The point estimates for all other groups are less than half as large and are statistically indistinguishable from zero";但**四个「年龄×性别」子组之间的差异检验只到 p = 0.062,按论文自订的 0.05 门槛不显著**。
  - **摘要 "driven by" 的措辞强于其底层检验。**
- **【探索性属性:两个平台的子组结论都不是预注册的】**逐字:"the pre-analysis plan … **did not specify what subgroup analysis might be done for secondary outcomes such as emotional state**";"In the body of the paper, we present **non-preregistered 'exploratory' analysis** of subgroups defined by above- vs. below-median values";"**We present unadjusted p-values for subgroup analyses.**";"The preregistered moderators for the primary outcomes included median splits of age and gender separately, but **not interacted**."
- **【年龄分箱口径·三票一致列为关键修正】不是同一把年龄尺,是各自样本内的中位数切分**。逐字:"The age survey question had coarse response categories; we allocate the median category to the above-median group. This yields **18-34 vs. 35+ and 18-24 vs. 25+** as the age groups in the Facebook and Instagram samples, respectively." **阈值差异是样本中位数的产物,不构成跨平台可比的年龄梯度证据。**「over 35」严格说是「35+」(含 35 岁)。
- **FB 的异质性还有另两条(原论断遗漏)**:逐字 "Non-preregistered subgroup analyses suggest larger effects of Facebook on people over 35, **undecided voters, and people without a college degree**." 相等性检验 undecided **p = 0.053**、non-college **p = 0.058**(均未过 0.05)。

### 时间替代去向
- 逐字:"app use data show that when people deactivate, **most of time freed by Facebook deactivation and all of time freed by Instagram deactivation is substituted to other smartphone apps**."
- **【必须分平台】**
  - **Facebook**:FB 使用下降约 **37 分钟/天**,而全部 app 总时长仅下降约 **9 分钟/天** → "around **three-quarters** of the reduction in Facebook use from deactivation was substituted to other apps",离线时间有**中等**增加。
  - **Instagram**:手机总使用时长**无显著变化** → 释放时间**全部**流向其他 app,**离线时间无增加**。
- 替代去向:Twitter、Snapchat、TikTok、YouTube、网页浏览(各增数分钟/天);FB 停用还使 IG 使用增加 4 分钟/天,反向不显著。
- 机制推论逐字:"this suggests that the effects are mostly driven by the different user experiences of Facebook or Instagram compared to other apps."

### 与 Braghieri et al.(C08 组)的对照
- 逐字:"Facebook's user experience was very different during that rollout period—for example, **there was no news feed**—so the effects could be quite different two decades later."
- 加强版:"the Facebook user experience has changed significantly in the past two decades: for example, there was no news feed, and **the user base was over 100 times smaller**." 并给出量级对照:Braghieri 等估计心理健康指数恶化 0.085 SD,"**roughly forty percent larger than our point estimate**",且其样本是**大学生**而非 18 岁以上成年人。

### 【原论断组遗漏·必须补】基线不平衡
- 逐字:"For Facebook, the **Deactivation group has statistically significantly worse baseline emotional state** … If we did not control for baseline emotional state, this imbalance would **bias against** our finding"。论文按预注册控制了基线情绪。方向不利于其结论,故不构成有利偏倚。

### 效应量参照系(论文自设,用于判断 0.060 SD 的实际大小)
- 共和党人比民主党人的情绪指数高 **0.48 SD**
- van Agteren et al. (2021) meta 分析中平均心理干预改善 **0.27 SD**
- 2008–2022 年轻人情绪指数恶化 **0.37 SD**
- 先前七项停用实验的逆方差加权平均效应 **0.11 SD**——"larger than our estimates"
- 论文结论明言:"the estimated effect sizes are **smaller than** benchmarks such as the effects of psychological interventions, nationwide mental health trends, and previous experimental estimates in smaller samples."

### 论文自陈的五条局限(已核到原文)
样本选择性;仅为增量五周且处于选举期(2020 年 FB 内容仅约 6% 与政治相关,且 Meta 此后已减少信息流政治内容);个体层面而非网络层面停用;仅三道自报情绪题且嵌于政治主题问卷;实验者需求效应无法完全排除;FB 基线不平衡与流失。

### 【必须披露】利益相关:厂商深度参与
- 属 "a partnership between Meta researchers and unpaid independent academics"。**多位共同作者机构署名为 Meta**:Crespo-Tenorio、Dimmery、Moehler、Franco、Kiewiet de Jonge、Mason(第三票另列 Velasco Rivera、Wilkins,即 6–8 人;成稿写「多位共同作者受雇于 Meta」较稳妥)。
- **抽样、信息流顶部投放邀请、账号停用执行、被动追踪均由 Meta 完成。**
- NBER 披露页另载:2 人曾受雇 Meta、6 人获 Meta 研究资助、2 人有偿咨询、11 人参加 Meta 资助活动、3 人持有 Meta 股票、2 人收取 Meta 酬金;Nyhan、Pan、Tromble、Wojcieszak、Stroud、Tucker 等曾获 Meta 直接研究资助,Gentzkow、Stroud 有 Meta 咨询关系。
- **制衡条款逐字(必须一并给出)**:"the independent academic authors had **final authority** over the pre-analysis plan, data analysis, and manuscript text, and **Meta could not block any results from being published**."
- **方向裁决**:结论(停用改善情绪)对 Meta 不利,**与利益相关方向相反,削弱了「结果被赞助方牵引」的推断**。但仍属厂商深度参与的研究,须如实标注。

## 修正记录(修正前→修正后)

1. 「N = FB 19,857 / IG 15,585」作为效应估计样本 → **这是招募/主分析样本;情绪效应的估计样本是完成 endline 的 17,802 / 13,480(流失 10% / 13%),论文 Figure 3 自标即为此数**;另有约 2pp 的显著差异性流失。
2. 「停用 6 周 +0.060 SD」被读作 ITT → **是 IV/LATE(『完全不用』vs『用到对照组均值』,仅对被 $150 诱导的 complier 成立);第一阶段 FB 0.871 / IG 0.893,ITT ≈ 0.87×LATE**。
3. 「校正后仍显著」→ **统计量应写 q 值:FB q = 0.002;IG q = 0.139**。
4. 「校正后 p = 0.14」→ **精确统计量为 q = 0.139;0.14 是作者引言措辞**。引语本身逐字成立。
5. 「停用 6 周」→ **6 周 vs 1 周之差;论文自陈的因果对比窗是「增量五周」(9/30–11/3)**。
6. 「IG 效应由 25 岁以下女性驱动」→ **18-24 岁女性点估计 0.111 SD(未校正 p=0.002),但四个年龄×性别组的差异检验仅 p = 0.062,未过论文自订的 0.05 门槛**;FB 的 35+ vs 18-34 差异检验 p = 0.046,勉强过线。
7. 年龄线被读作统一梯度 → **FB 与 IG 用各自样本的中位数切分:FB 18-34 vs 35+,IG 18-24 vs 25+;年龄题选项粗糙,中位类别划入 above-median 组。阈值差异是样本中位数的产物,不构成跨平台年龄梯度证据。**
8. 「FB 效应由 35 岁以上驱动」被当作唯一调节 → **同一段还列出未决定选民(p=0.053)与无大学学历者(p=0.058);且 FB 的 35+ 结论与 IG 的年轻女性结论一样,都是非预注册的探索性分析、报告未校正 p 值**。
9. 「释放时间大部分流向其他 app」→ **FB 是 most(约四分之三,离线时间有中等增加),IG 是 all(离线时间无增加)**。
10. 原论断未提基线不平衡 → **FB 的 Deactivation 组基线情绪显著更差,已按预注册控制;方向不利于其结论**。
11. 原论断未提利益相关 → **Meta 深度参与(共同作者、抽样、投放、停用执行);须同时给出「学者对 PAP/分析/文稿有最终决定权、Meta 不能阻止发表」的制衡条款,并指出结论方向与利益方向相反**。
12. 原论断未提同行评审状态 → **NBER 工作论文,未经同行评审,无修订版、无期刊发表版、无勘误(NBER 与 RePEc 双源确认)**。

## 未回溯项

- **【三票均未回溯,不得承重】预注册文件(PAP / OSF 登记条目 https://osf.io/t9q2f)原件**。该页为 JS 渲染,WebFetch 只返回 "OSF" 字样;api 端点未成功。因此「年龄×性别交互未预注册」「情绪指数为 secondary outcome、分项为 auxiliary outcomes」「0.05 为预注册阈值」「以基线情绪为控制变量」「IV 设定」等表述**目前只有论文作者自陈这一个来源,未由登记原件独立交叉验证**。成稿引用「非预注册探索性分析」这一定性时,应写明系论文自述。
- **【三票均未回溯】Appendix D.3 / D.4 与 Table S13–S30 的逐格数值**(附录为单独文件,主 PDF 不含)。因此:子组点估计的完整清单、**预注册 subgroup 的结果(论文称在 D.4 报告)**、流失稳健性检验、完整 q 值矩阵、既往研究对照表,均只依赖正文转述。**「预注册 subgroup 里 35+/年轻女性效应是否同样成立」无法判定。**
- **【三票均受限】2025-04 之后针对该文的批评性回应、复现尝试、勘误或同行评审版,未做检索**(三票的 WebSearch 配额均已耗尽)。已用 NBER 官方页 + RePEc 两个独立来源确认「无修订、无发表版、无勘误」,但**不能据此推断该论文未受质疑**;尤其对 LATE 的 never-taker 外推、q 值校正族的选择、0.06 SD 的实质意义等争论点,未覆盖。
- 第一票未回溯 Braghieri, Levy & Makarin (2022, AER) 原文,其 0.085 SD 与「大学生样本」「2004-2005 rollout」等转述仅来自本文作者的二手描述。**本项已由 C08 组三票各自回溯一手 AER PDF 解决,跨组交叉确认无误(0.085 SD、Table 1 第 3 列、样本限于 full-time undergraduates 均成立)。**

## 证据分级

- **主数字(0.060 / 0.041 SD、p 与 q 值、分项、N、设计、替代去向、"no news feed" 警告):单源已核**——一手 NBER 工作论文原件,三票各自下载并逐字比对,结果完全一致;但**只有这一份来源,且该来源未经同行评审**。
- **版本状态(无修订/无发表版/无勘误):多源证实**(NBER 官方页 + RePEc)。
- **子组结论(「FB 由 35+ 驱动」「IG 由 25 岁以下女性驱动」):未验证/探索性**。非预注册、未校正 p 值、IG 的组间差异检验未过 0.05。**摘要那句可以引,但必须紧跟底层检验数字;不得作为承重论断。**
- **利益相关:厂商口径(利益相关方深度参与)**。Meta 抽样、投放、执行停用,多位共同作者受雇于 Meta;有明确的独立性制衡条款,且结论方向对 Meta 不利。**成稿引用时须同时给出「Meta 深度参与」与「结论方向与利益方向相反」两面。**
- **用于青少年议题:未验证(纯外推)**。样本为 18 岁以上成年用户,不含青少年;且入组率 <1%、偏自由派与高公民参与度。


---

# C11 最终判决:CORRECTED(3/3 票)

三票均判 CORRECTED。三个 dz 数值逐字成立,但「56.8% 装 app」这个数字**在原文中根本不存在**;「合规达预注册标准」中的「预注册」二字**被第三票用一手预注册文件推翻**;「大于抗抑郁药」的对比在同口径下**方向反转**。此外三票共同揭示:头条 dz 是合并两臂的**受试内前后差**,不是随机化组间对照。

## 锁定口径(成稿必须用)

### 书目
- Castelo, N., Kushlev, K., Ward, A. F., Esterman, M., & Reiner, P. B. (2025). *Blocking mobile internet on smartphones improves sustained attention, mental health, and subjective well-being*. **PNAS Nexus, 4(2), pgaf017**。DOI 10.1093/pnasnexus/pgaf017;PMID 39967678;PMCID PMC11834938。三票均以 OUP 原文页 + PMC 全文镜像两处独立比对,数字一致。
- 无 correction / erratum / expression of concern / retraction(Crossref relation 字段为空;OUP 与 PMC 文章页均无通告)。

### 干预与设计(逐字)
> "We used a mobile phone application to block all mobile internet access from participants' smartphones for 2 weeks and objectively track compliance. This intervention specifically targeted the feature that makes smartphones 'smart' (mobile internet) while allowing participants to maintain mobile connection (through texts and calls) and nonmobile access to the internet (e.g. through desktop computers)."

- 交叉设计(延迟起始 delayed-start):"those in the Intervention group blocked mobile internet access for the first 2 weeks only (T1–T2), while those in the Delayed Intervention group acted as a control for the first 2 weeks and then blocked mobile internet access for the second 2 weeks (T2–T3)"。全程一个月、三个时点。
- 工具:商业软件 **Freedom**(发放 premium 兑换码)。

### 样本 N 的三级口径
- **504** 人完成 baseline 并被**随机分组**(Intervention 253 / Delayed 251)
- 按 email、电话、Prolific ID **去重后保留 467 人**(Intervention **242** / Delayed **225**)——**两臂不等**
- **327** 人完成 T1 与 T2(70%);**313** 人完成全部三次调查(**67%**)
- **成稿表述:「随机化 504 / 去重承诺 467 / 分析 313」**。467 是随机化之后的去重存活样本,不是随机化单元数。
- **分析为 complete-case**:论文明言 "these analyses are based on 'complete cases' only—that is, participants who provided data at all three time points"。持续注意力分析实际 n≈**242**(由 F(1,242) 推得),仅占随机化 467 人的 **52%**;心理健康 F(1,306) → n≈308。
- **流失方向不利**:"Compared with participants lost to attrition, participants who completed all three time points had **significantly better mental health** and had **better sustained attention** at baseline."

### 三个 dz(逐字,三票一致)
> "The ITT pre–post intervention effects were **dz = 0.45 (P < 0.001) for SWB**, **dz = 0.56 (P < 0.001) for mental health** and **dz = 0.23 (P < 0.001) for sustained attention**."

- **【关键构念修正·必须写明】这三个 dz 不是随机化组间对比,而是把两组合并后的受试内前后差。** 逐字:"To increase power and the precision of effect size estimates, we **pooled data from both groups** into combined 'pre intervention' (all T1 data for the Intervention and Delayed Intervention groups) and 'post intervention' observations (matching T2 data for the Intervention group and matching **T3 data for the Delayed Intervention group**)." 即延迟组的 pre 取 T1、post 取 T3,**跨越 4 周(含 2 周无干预期)**,不含并行对照,不控制时间效应、重复测验练习效应与均值回归。
- **「ITT」的含义仅是「不因不合规而排除参与者」**:逐字 "We focus our analyses on intention-to-treat (ITT) effects, without excluding any participants based on compliance, while also reporting treatment-on-treated (TOT) effects as secondary analyses"——**不是缺失数据意义上的 ITT,未对 467 做任何插补**。
- **TOT(仅合规者)**:SWB dz = 0.50、mental health dz = 0.68、sustained attention dz = 0.26 (P = 0.009)。
- **【易混淆·必须标明是哪一组】**另有一组 Intervention 组 T1→T2 单组值 0.24 / 0.57 / 0.46:sustained attention t(130)=2.71, P=0.008, dz=0.24;mental health t(164)=7.31, P<0.001, dz=0.57;SWB t(166)=5.98, P<0.001, dz=0.46。**引用时必须标明是「合并 ITT」还是「干预组单组」,否则数字对不上。**

### 随机化层面的证据(三票合并后的准确图景)
- **Condition 主效应(组间)三个结局全部不显著**:mental health F(1,306) = 3.39, **P = 0.067**;SWB F(1,302) = 3.52, **P = 0.062**;sustained attention F(1,242) = 0.32, **P = 0.572**。
- **Condition×Time 交互三个结局全部显著**:mental health F(2,582) = 19.29, P < 0.001;SWB F(2,576) = 12.94, P < 0.001;sustained attention F(2,472) = 4.24, **P = 0.016**。
- **【对论文公平的反向证据·须一并呈现】交叉模式支持真实因果效应**:各组只在自己被拦截的窗口内改善——Intervention 组 T1→T2 改善 t(130)=2.71, P=0.008, dz=0.24,T2→T3 无变化(P=0.325);Delayed 组 T1→T2 无变化(P=0.519),T2→T3 改善 t(112)=3.03, P=0.003, dz=0.28。
- **T1→T2 随机化组间的改善比例对比**:SWB 75% vs 47%(χ²=17.6, P<0.001);mental health 68% vs 52%(χ²=13.0, P<0.001);**sustained attention 59% vs 46%(χ²=3.5, P=0.062)——注意力这一项未过 0.05**。
- **成稿的准确表述**:「头条 dz 为合并两臂的受试内前后差;交叉设计的随机化证据体现在 Condition×Time 交互(三个结局均显著)与两组各自窗口内的改善模式;但 Condition 主效应不显著,且注意力的组间改善比例对比仅 P=0.062。」**不可只引 dz 而说成随机对照效应,也不可因主效应不显著就说没有随机化证据——交叉设计中交互才是相关检验。**

### 合规链条(逐字)
> "Of the 467 codes, **272 were redeemed**; ∼41.7% of participants therefore did not sign up for the app used to block mobile internet." → "Of these 272, **266 set up the initial mobile internet block**, and **249 completed all three surveys**." → "These **119** represent ∼**25.5%** of the participants who completed survey 1 and agreed to keep mobile internet blocked for 2 weeks, or **47.8%** of those who downloaded and set up the Freedom app."

- 三个百分比自洽:119/467 = 25.48%;119/249 = 47.79%;249/313 = 79.6%。
- **【数字排雷】「56.8%」在原文中不存在**。全文检索 "56.8" 无命中。相邻的两个数是:**兑换码 272/467 = 58.2%**;**真正设置了首次拦截 266/467 = 57.0%(56.96%)**。**成稿若要保留单一数字,写「注册 app 58.2%、实际设置屏蔽 57.0%」。**

### 【三票冲突裁决·最硬的一处修正】「预注册标准」不成立
- 论文自述逐字:"119 (25.5% of those who committed) met our **preregistered** definition of 'compliant' (**having the block active for at least 10 of the 14 intervention days**, as recorded by the Freedom app)"。第一票据此认为 25.5% 逐字成立;第二票发现抽取中存在两种互斥的合规定义,建议不复述阈值。
- **第三票用一手预注册文件裁决**:下载并解包 OSF 上唯一的预注册文档(tfdm6 = "freedom pre reg draft 06 08.docx",2022-06-10T02:37:03Z 上传,current_version=1,从未修改,SHA256 5c846bfb114fe699bae7f5e9b6c718192708947b6ef86257bb6c1cc61a782c54),其逐字定义为:
  > "Participants will be 'compliant' if they **ended their session fewer than 5 times** and had **less than 60 minutes not in a session**."
  对该 .docx 全文做字符串检索:**'10 of' / 'ten of' / '14 days' / 'at least 10' / '10 out of' 全部 ABSENT**。并已确认 OSF 项目 uxcwm 的 "Pre-registration and miscellaneous" 文件夹内仅 2 个文件,预注册文档只有 1 份,排除「另有修订版预注册」的可能。
- **裁决:采信第三票的一手证据。锁定表述——「合规率 25.5%(119/467)采用的是『14 天中至少 10 天开启拦截』这一论文自定标准;该标准并不出现在预注册文件中,论文却称之为 preregistered」。**
- **【延伸】「OSF 预注册」这一说法也需降级**:OSF API 的 GUID 解析显示 tfdm6 的 type 为 "**files**"(不是 registration/node);api.osf.io/v2/registrations/tfdm6/ 返回 404。**它不是 OSF 的正式 Registration(冻结注册),而是挂在普通 project 节点 uxcwm 下的一个 .docx 文件。** 时间上确在数据采集前(预注册正文写明干预自 Friday June 10 或 June 24 开始,文件 2022-06-10 上传,即首波开始当日),属 just-in-time。
- **【其他偏离预注册·未标注】**
  - 合并前后分析不在预注册中:预注册规定的是 3×2 混合 ANOVA("DV = condition * time, with time as a 3-level within-subjects factor and condition as a 2-level between-subjects factor"),交互显著后做 T1→T2 / T2→T3 简单效应,未提及跨组合并前后数据。
  - 心理健康构念被删一维:预注册写明取 **six** symptom groups 的平均,明确包含 **repetitive behaviors**;论文实际只用 **five**(depression, anxiety, anger, social anxiety, personality functioning),**未标注为偏离预注册**。
  - 预注册确实规定了 ITT:"We will first report intent-to-treat analyses in which we include all participants regardless of whether they complied… we anticipate significant noncompliance (up to 50%)";样本量计划 "We will recruit 500 participants"。

### 心理健康构念
- **五域反向计分合成指数,非抑郁单项**。逐字:"mental health (a reverse-scored index including symptoms of **depression, anxiety, anger, personality function, and social anxiety**; dz = 0.57, P < 0.001)";量表来源 "Items were taken from the corresponding subscales of the **DSM-5 Level 1 cross-cutting symptom measure for adults**"(另加社交焦虑严重度量表 1 个条目,α = 0.90)。
- 持续注意力为 **gradCPT**(gradual onset continuous performance task),**客观任务而非自评**。

### 【方向反转】「大于抗抑郁药」的对比
- 论文原句:"The observed effect of the intervention on **depression symptoms** (dz = 0.56) was **larger than the meta-analytic effect of antidepressants** [29] and similar to that of cognitive behavioral therapy"。
- **ref 29 一手核实**:Kirsch I, Deacon BJ, Huedo-Medina TB, Scoboria A, Moore TJ, Johnson BT (2008). *Initial severity and antidepressant benefits: a meta-analysis of data submitted to the Food and Drug Administration*. **PLoS Medicine 5(2): e45**。(检索过程中曾有二手抽取把该文献误报为 JAMA 300(16):1882–1888,**系错误**,已以 PLoS Medicine 原刊页面核正。)
- **Kirsch 的 d = 0.32 是「药物减安慰剂」的组间标准化均差**(HRSD 差 **1.80 分**);作者并指出 1.80 分 "does not meet the three-point drug–placebo criterion for clinical significance used by NICE"。
- **同口径(组内前后)对照**:Kirsch 中**药物组组内改善 9.60 HRSD 点**(安慰剂组 7.80 点),换算 **d ≈ 1.24**(第一票换算)——**是 0.56 的两倍以上**。
- **裁决:「大于抗抑郁药」在同口径下方向反转。** 论文的 dz = 0.56 是未扣除安慰剂/期待/均值回归的受试内前后变化,拿去比一个已扣除安慰剂的组间差,是单位错配。
- **【叠加的第二层错误】构念错配**:0.56 是**五域 mental health 合成指数**的 ITT 值,论文却在这句里把它称作 "the effect on depression symptoms";**全文与附录从未单独报告抑郁分量表的 dz**。
- **论文对该对比给出的唯一保留意见只是样本与情境差异**("the nature of our sample and of our intervention is quite different from those studied in clinical psychology contexts"),**从未提及效应量口径不可比**——即这条批评论文自己没有披露。

### 手机使用时长
- **Intervention 组**:T1 **314** 分钟 → T2 **161** 分钟 → T3 反弹至 **265** 分钟。
- **Delayed Intervention 组**:T1 **336** → T2 **322** → T3 **190**。
- **【三条限定必须带】**(i) 这是**总屏幕使用时间**而非移动互联网时间;(ii) 由参与者**自行上传 iPhone 屏幕使用时间页截图**获得("We asked participants to upload screenshots of their iPhone's screen time page"),属「客观记录但自主提交」,非后台自动采集;(iii) **仅为单臂数据,且干预结束后大幅回弹,不能作为持久性证据**。

### 人群与自选(三票一致成立,且可加码)
- Prolific 美/加在线劳务池,**平均年龄 32 岁,63% 女性**,15% Asian / 9% Black / 62% White / 12% Other,**仅限 iPhone 用户**,**无未成年人**。
- **动机自选(逐字)**:"Our sample consisted mostly of individuals **motivated to reduce their smartphone use**: at the outset of the experiment, we asked how motivated participants were to reduce their smartphone use on a 1 (not at all) to 7 (very much) scale and **83% of our participants chose 5 or higher**."
- 预注册的预筛还要求自报日均手机使用 > 60 分钟,且必须对 "Are you REALLY willing to block the Internet from your smartphone for 2 entire weeks…" 回答「Yes I am committed to doing this for 2 weeks!」才入组;另设「每坚持 1 天 = 1 次 $500 抽奖资格」的激励。
- **期待效应(逐字)**:"**Expectancy effects, such as placebo and demand effects, could have contributed to our findings**… Participants may have guessed that the intervention was intended to improve their well-being and responded accordingly even if they did not really feel better. **This is a limitation of our design.**" 论文另自承**无主动对照组**,难以分离安慰剂效应。
- **【支持期待效应实际在起作用的内部证据】同一注意力构念,自评量表(MAAS)效应 dz = −0.79(t(163) = −10.07, P < 0.001),客观 gradCPT 仅 dz = 0.23–0.24,相差约 3 倍。主观测量被放大的模式与需求特征/期待效应一致。**

### 资助与利益相关
- 逐字:"Funding was provided by the **Silicon Valley Community Foundation** to P.B.R. (**grant # GR027378**)";作者声明 "**The authors declare no competing interests.**"
- 参与者获赠 Freedom premium 版。**Freedom 高级版激活码是厂商捐赠还是经费购买,论文未说明**;未发现厂商共同署名或数据控制迹象。
- 注:SVCF 是捐赠人建议基金(DAF)托管机构,**最终出资人不公开**——属透明度局限,而非已证实的利益冲突。

## 修正记录(修正前→修正后)

1. 「装 app 仅 56.8%」→ **该数字在原文中不存在**;正确为**兑换码 272/467 = 58.2%、实际设置首次拦截 266/467 = 57.0%**。
2. 「合规达**预注册**标准仅 25.5%」→ **25.5%(119/467)成立,但「预注册」不成立**:论文用的标准是「14 天中至少 10 天开启拦截」,而一手预注册文件写的是「结束会话少于 5 次且不在会话中的时间少于 60 分钟」,且 '10 of'/'14 days' 在预注册全文中 ABSENT。
3. 「OSF 预注册」→ **是挂在普通 project 节点下的一个 .docx 文件(OSF GUID type = files),不是 OSF 正式 Registration**;上传时间为首波干预开始当日,属 just-in-time。
4. 「N=467、随机交叉」→ **随机化 504(253/251),去重后 467(242/225,两臂不等),完成全部三次调查仅 313(67%);分析为 complete-case,注意力分析 n≈242 仅占 52%;流失者基线心理健康与注意力显著更差**。
5. 「ITT 效应 dz = 0.23/0.56/0.45」→ **数值成立,但「ITT」仅指不按合规剔除;这三个 dz 是把两臂合并后的受试内前后差(延迟组 pre 取 T1、post 取 T3,跨 4 周),不是随机化组间对照,不控制时间效应、练习效应与均值回归;该合并分析不在预注册中**。
6. 「随机化证据」的完整图景 → **Condition 主效应三项全不显著(P=0.067 / 0.062 / 0.572);Condition×Time 交互三项全显著(P<0.001 / <0.001 / 0.016);T1→T2 组间改善比例 SWB 与 mental health 显著、sustained attention 仅 P=0.062**。
7. 「mental health(DSM-5 Level 1)」→ **五域反向计分合成指数(抑郁/焦虑/愤怒/社交焦虑/人格功能),非抑郁单项;预注册规定的是六域(含 repetitive behaviors),论文删去一维且未标注为偏离**。
8. 「dz=0.56 是干预对抑郁症状的效应」(论文自身措辞)→ **0.56 是五域合成指数值;全文未单独报告抑郁分量的 dz**。
9. 「效应大于抗抑郁药」→ **同口径下方向反转**:Kirsch 的 d=0.32 是药物减安慰剂的**组间**差(HRSD 1.80 分,低于 NICE 临床显著阈值);与 dz 同口径的**药物组组内前后改善为 9.60 HRSD 点(d≈1.24)**,是 0.56 的两倍以上。
10. 「Kirsch 2008 发表于 JAMA 300(16)」(检索中出现的二手误报)→ **PLoS Medicine 5(2): e45, DOI 10.1371/journal.pmed.0050045**。
11. 「手机使用 314→161 分钟」作为全样本/持久结论 → **仅 Intervention 组,且 T3 反弹至 265;Delayed 组为 336→322→190;测量为参与者自行上传的 iPhone 总屏幕时间截图,非移动互联网时间、非后台采集**。
12. 「自选样本+期待效应未排除」→ **成立且可加码**:83% 自报减少手机使用动机 ≥5/7、入组需明确承诺、有抽奖激励、无主动对照组、流失方向有利于高估;**内部证据:自评 MAAS dz=−0.79 vs 客观 gradCPT dz=0.23,相差约 3 倍**。

## 未回溯项

- **【三票均未回溯】PubPeer 发表后质疑**:https://pubpeer.com/search?q=10.1093/pnasnexus/pgaf017 返回 HTTP 403。**无法确认是否存在同行的公开质疑;不能据此断言「无人质疑」。**
- **【三票均受限】广域反证检索未做**(三票的 WebSearch 配额均已耗尽)。反证覆盖仅限两条路径:期刊页面通告(无 correction/erratum/EoC/retraction;Crossref relation 空)+ Semantic Scholar 的 25 条引用记录(未见针对本研究的再分析、失败复制或方法学反驳)。**最相关的旁证是 "Going Light: The Effects of Minimal Mobile Phone Adoption on Young Adults' Well-Being Depend on Motivation"(2026, CHI),其「效应取决于动机」结论与本研究高动机自选样本的外推局限方向一致。**
- **【三票均未回溯】SI Appendix 中「使用全部可得数据」的替代分析**(论文声称与主分析一致)。**无法独立验证纳入非完成者数据后效应量是否衰减、衰减多少。**
- **【三票均未回溯】Freedom premium 激活码的取得方式(厂商捐赠 vs 经费购买)**。论文只写参与者获得免费高级版,未说明来源;公开页面亦无法核实。**「厂商是否为利益相关方」只能记为披露不足,不能下结论。**
- 数据采集的确切起止日期未给出;仅能从预注册正文的 "starting EITHER Friday June 10 or Friday June 24" 推断为 2022 年 6 月两波开始,**无法核实结束日期与是否有未报告的额外波次**。

## 证据分级

- **主数字(三个 dz、合规链条、N、屏幕时长、量表来源、自选与期待效应自述):单源已核**——期刊一手全文,OUP + PMC 双镜像三票一致。
- **预注册与论文的不一致(合规定义、合并前后分析、构念删一维):单源已核,但为高强度一手证据**——第三票直接从 OSF REST API 取元数据 + 下载解包 .docx(带 SHA256、版本号 1、创建与修改时间戳相同),并确认项目内无其他预注册版本。**该项裁决推翻了论文自述的「preregistered」标签,应作为承重修正写入。**
- **Kirsch 2008 基准:多源证实**(PLoS Medicine 开放获取原文,两票独立核到 9.60 / 7.80 / 1.80 / d=0.32 与 NICE 阈值)。
- **「效应大于抗抑郁药」:已被推翻(方向反转)**。**成稿不得沿用该对比;若要提,只能写成「论文作出了这一对比,但两者口径不同——一个是未扣安慰剂的受试内前后变化,一个是已扣安慰剂的组间差;同口径下抗抑郁药的组内改善远大于本干预」。**
- **因果强度整体:方向存争**。交叉设计的 Condition×Time 交互三项显著、两组各在自己窗口内改善,是支持真实效应的实质证据;但头条 dz 为受试内前后差、Condition 主效应不显著、注意力的组间比例对比仅 P=0.062、自选样本 + 无主动对照 + 期待效应自承 + 主客观测量相差 3 倍 + 流失方向有利于高估——**因果强度显著低于其对外传播口径。成稿宜引 dz=0.23(客观注意力)与交互显著性,慎引 dz=0.56 的心理健康值。**
- **用于青少年议题:未验证(纯外推)**。平均年龄 32 岁的成人 Prolific 自选样本,零青少年覆盖。
- **利益相关:披露不足(非已证实冲突)**。SVCF 为 DAF、最终出资人不公开;Freedom 许可证来源未说明;作者声明无利益冲突。


---

# C12 最终判决:CORRECTED(3/3 票)

三票均判 CORRECTED。三份 meta 的所有主数字逐字成立,但四处必须修正:①「限用 0.33 vs 戒断 0.15」被误读为限用更优(组间检验 Q(1)=0.85, p=0.36 不显著);②Ferguson 那篇**已有 APA 正式勘误**(原论断完全遗漏);③Thrul 再分析是**双向**结果(短干预显著变差),且 Ferguson **已发表回应**(原论断遗漏);④**三份 meta 没有一份是青少年证据**。此外第二票在底稿中查出一处会直接塌的误署(见「排雷」)。

## 锁定口径(成稿必须用)

### 【最高优先·排雷】底稿 line5-policy.md 第 90 行存在误署
- 《The Effects of Social Media Restriction: Meta-Analytic Evidence from Randomized Controlled Trials》(**SSM–Mental Health 2025, DOI 10.1016/j.ssmmh.2025.100459**)作者是 **Burnell, K., Meter, D. J., Andrade, F. C., Slocum, A. N., & George, M. J.**,**不是 Ferguson**;且结论**不是零效应**,而是 **32 项 RCT、5,544 人、91 个效应量、Hedges' g = .17 显著为正**(作者自评 "small in magnitude")。
- **把它当作「Ferguson 2025 预注册零效应 meta」引用会直接出错。成稿必须改正或删除。**
- 同刊 Thimm-Kaiser & Keyes (2025, DOI 10.1016/j.ssmmh.2025.100467) 是中立评述,不含具体数值转引。

### (a) May, Malouff & Meynadier(2025)——减用 RCT meta
- **著录**:May, W., Malouff, J. M., & Meynadier, J. (2025). *Reducing Social Media Use Decreases Depression Symptoms: A Meta-Analysis of Randomised Controlled Trials*. **EJIHPE 15(11), 文章号 222**。DOI 10.3390/ejihpe15110222,2025-10-27 上线。**MDPI 出版**(University Association of Education and Psychology 名下)。PROSPERO **531956**。检索截至 **2024 年 9 月**(ProQuest/PubMed/Scopus/EBSCOhost)。Received 2025-09-13 / Accepted 2025-10-18。**三份中最新,方法学声誉低于 Sci Rep。**
- **主结果**:10 项 RCT,**N = 1,491**。抑郁 raw **g = 0.28, 95% CI [0.13, 0.43], p < 0.001**;**trim-and-fill 补插 1 项后 g = 0.25, 95% CI [0.10, 0.41]**。摘要原句:"reducing social media use significantly decreases depressive symptoms, with an effect size of **g = 0.25, 95% CI [0.10, 0.41], p < 0.001, after adjusting for publication bias**." → **0.25 是论文自报的结论值,0.28 是未校正值,两个都对,引用时说明来历。**
- 异质性:**I² = 47.29%, τ² = 0.026, Q(9) = 17.24, p = 0.045**。
- **【削弱 trim-and-fill 的事实,须一并写】该 meta 并未检出发表偏倚**:"Visual inspection of the funnel plot indicated symmetry, and **Egger's test for asymmetry of the funnel plot was non-significant (p = 0.85)**." **故 0.25 是在无不对称证据下做的保守调整,不宜说成「扣掉发表偏倚后仍有效」。**
- **【三票一致列为最重要修正】亚组差异不成立**:
  - 限用型 **k=7, g = 0.33, SE = 0.09, [0.16, 0.51], p < 0.001**
  - 完全戒断型 **k=3, g = 0.15, SE = 0.17, [−0.18, 0.49], p = 0.369**
  - **组间调节检验 Q(1) = 0.85, p = 0.36 —— 不显著**
  - 作者摘要逐字:"Although interventions aimed at reducing use of social media had **twice the depression effect size** of interventions aimed at abstinence from social media, **the difference was not significant**."
  - 论文正文逐字:"The effect size of limited use interventions **did not significantly differ** from the effect size of full abstinence interventions (Q(1) = 0.85, p = 0.36)."
  - **【硬性禁止】不得写「限用比戒断更有效」。这是典型的 difference-in-significance 陷阱;戒断亚组不显著的主因是 k=3、CI 极宽。** 三个 moderator(干预类型、干预时长、所针对社交网络数)**全部不显著**。
- **人群**:**平均年龄 24.2 岁**,各研究均值区间 **18–28.93**,**75.39% 女性**,全为成人/大学生/社区成人,**无青少年样本**。论文限制段:"The meta-analysis did not include enough studies to evaluate whether interventions to reduce or to eliminate use of social media had more positive effects on depression in some populations versus others."
- 抑郁量表:DASS-21、BDI-II、CES-D、PHQ-8/PHQ-2。抑郁是**唯一结局**。
- 资助与 COI:"This research received **no external funding**." "The authors declare **no conflicts of interest**." Crossref 查无勘误。

### (b) Lemahieu et al.(2025)——**纯戒断** meta
- **著录**:Lemahieu, L., Vander Zwalmen, Y., Mennes, M., Koster, E. H. W., Vanden Abeele, M. M. P., & Poels, K. (2025). *The effects of social media **abstinence** on affective well-being and life satisfaction: a systematic review and meta-analysis*. **Scientific Reports 15**, 2025-03-04。DOI 10.1038/s41598-025-90984-3;PMID 40038410;PMCID PMC11880199。PROSPERO **CRD42023428990**。
- **【纳入口径修正·关键】这是「纯戒断」meta,不是「减用/戒断」**:一手明确要求受试者 "**completely abstain** from the use of social media platforms",**显式排除仅减少使用的干预**。**它在结构上无法对「减用」发言,与 (a) 的限用亚组不可比。**
- **【设计口径修正】不是 RCT-only meta**:纳入了非随机设计(**70% 为被试间设计**,其余为被试内/混合)。**把它与 May(RCT-only)并列为同类口径是错的。**
- **主结果**:**10 篇研究、38 个效应量、N = 4,674**。摘要逐字:"In total, ten studies (N = 4674) were included, allowing an examination of 38 effect sizes across these three outcomes. The analyses revealed **no significant effects** of social media abstinence interventions on positive affect, negative affect, or life satisfaction."
  - **positive affect g = 0.03, 95% CI [−0.11, 0.16], p = 0.69**(9 项研究 / 14 效应量,I² = 60.7%)
  - **negative affect g = −0.01, [−0.13, 0.10], p = 0.78**(9 项 / 14 效应量,I² = 63.7%)
  - **life satisfaction g = 0.03, [−0.17, 0.22], p = 0.75**(6 项 / 10 效应量,I² = 58.8%)
  - **【分母修正】不是每个结局都用满 10 项 N=4,674。**
- **【必须披露】样本由单项研究主导**:10 项 N 逐项相加 = 4,674 与自报吻合;其中 **Allcott 2020 一项 N = 2,813,占总样本 60.2%**。
- **【表述修正】「结局不含抑郁症状」太绝对**:该文未声明排除抑郁,只是把结局定义为 affective well-being + life satisfaction;**个别研究的抑郁量表被折算进 negative affect**(逐字:"there were few studies that used different measures for negative affect, including loneliness and depression";Tromholt 用 CES-D 计入 negative affect)。**正确写法:「未把抑郁设为独立结局,个别研究的抑郁量表被并入 negative affect」。**
- 戒断时长 **1–28 天**(7 天最常见),时长调节全部不显著。人群:**全成人**("All studies used an adult sample"),各研究均值 **19.9–34 岁**,跨度 18–80,**明确无未成年人**,以西方大学生为主。
- 该文对 Ferguson 的定位(逐字要点):Ferguson "combined two different intervention strategies (i.e., reducing social media use and totally refraining from using social media) under the term 'reduced social media experiments' and examined the effect on an **aggregated** mental health outcome",而本文采取 "a more **targeted** approach"。
- 资助:Research Foundation Flanders(FWO S005923N)+ ERC Starting Grant 'DISCONNECT' No. 950635;"The authors declare **no competing interests**." Crossref 查无勘误。

### (c-1) Ferguson(2024/2025)——实验 meta
- **著录**:Ferguson, C. J. (2024/2025). *Do social media experiments prove a link with mental health: A methodological and meta-analytic review*. **Psychology of Popular Media, 14(2), 201–206**。DOI 10.1037/ppm0000541。**线上首发 2024-05-02,纸本 2025**。**成稿写 2024 更稳。** k = **27**(25 篇已发表 + 2 篇学位论文),2013–2023 年。
- **合并效应**:**d = 0.088, p = 0.104**;流传的 95% CI 为 **[−.018, .197]**(**该 CI 未回溯到一手,见未回溯项**)。
- **【点估计可靠·两票独立复算】**两票分别下载 Ferguson 自己的 OSF 数据集(osf.io/hv7us,"Revised Experiments Effect Sizes.xlsx",k=27,ΣN=6,426),用 DerSimonian–Laird 随机效应独立重算:
  - 第二票:**d = 0.0865, 95% CI [−0.012, 0.185], τ² = 0.040, Q = 82.9**
  - 第三票:**d = 0.0865, 95% CI [−0.0124, 0.1854], τ² = 0.040, I² ≈ 69%**
  - Thrul 等独立复算:**d = 0.086**
  - **→ 零效应方向可靠,点估计锁定在 d ≈ 0.086–0.088、置信区间跨零。**
- **【必须写明】Ferguson 预注册把实用显著性门槛设为 r = .10(≈ d = .201)**——这是其「零效应」论述的一个关键前置设定。
- **【原论断完全遗漏·必须补】APA 已发表正式勘误**:*Correction to "Do social media experiments prove a link with mental health: A methodological and meta-analytic review" by Ferguson (2024)*,**Psychology of Popular Media 14(2), 328,DOI 10.1037/ppm0000586,Crossref 登记/更新日 2025-02-03**。即「誊录错误」不只是 SSRN 上的一面之词,**期刊层面已有形式承认**。
- **【关键事实】Ferguson 的 OSF 效应量文件于 2024-10-02 被修改,改后恰好采纳了 Rausch & Haidt 指出的三处样本量错误**:Lepp & Barkley **80→40**、Kleefeld **82→53**、Przybylski **600→297**;Brailovskaia 2022 编为 **d = 0.10**。**但零结论在修订后仍成立(0.086,CI 仍跨零)——这一点对双方都要如实写。**
- 摘要逐字(经 Thrul 预印本内嵌 CSL 元数据,来源标为 APA PsycNet):"Nonetheless, meta-analytic evidence for causal effects was **statistically no different than zero**. However, **remarkable between-study heterogeneity** was observed. Studies with citation bias produced higher effect sizes, suggesting a **research expectancy effect** in some studies."

### (c-2) Thrul 等再分析
- **著录**:Thrul, J., Devkota, J., AlJuboori, D., Regan, T., Alomairah, S., & Vidal, C. (2025). *Social media reduction or abstinence interventions are providing mental health benefits—Reanalysis of a published meta-analysis*. **Psychology of Popular Media, 14(2), 207–209**。DOI 10.1037/ppm0000574,发布 2025-04-01。**Johns Hopkins Bloomberg School of Public Health 等**(第三票已从接收稿全文核实机构)。预印本全文:PsyArXiv 10.31234/osf.io/degba。
- **【必须四步完整写,不能简写成「加了 moderator 就有益」】**
  1. 复算全部研究:**d = 0.086,不显著**
  2. **剔除 Ferguson 27 项中 7 项非减用/戒断干预**后 k=20:**d = 0.081,仍不显著**(逐字:"excluded seven studies because they were **not reduction/abstinence interventions**"——这是**纳入口径批评**,不是单纯建模批评)
  3. 加入时长调节后调节效应显著:**d = 0.333, SE = 0.120, p = .006**;分层结果**双向**:
     - **<1 周:d = −0.175, SE = 0.068, p = .010 —— 显著更差**(仅 **4 项**研究)
     - **≥1 周:d = +0.156, SE = 0.065, p = .016 —— 显著改善**(16 项)
  4. 连续型二次项分析(k = 19):**weeks p = .013、days p = .018**;建议**最短 1 周、理想约 3 周**
- **【转述红线】「短期干预反而显著变差」这一半在转述中几乎总被略去;成稿必须并列。且 <1 周那一格只有 4 项研究。**
- 稿件时间线自陈:2024-10-29 "updated all analyses due to updates to the original meta-analysis and dataset on OSF"。
- **资助含 Aramco Services Company(Saudi Aramco 子公司)+ NIDA / AACAP / Maryland DOH**。
- 该文也是 Ferguson 结论的独立中立转述来源:"The author concluded that meta-analytic pooled analyses indicated that social media effects were statistically no different from zero."

### (c-3) Ferguson 的回应(原论断遗漏)
- **著录**:Ferguson, C. J. (2025). *Longer-term interventions to reduce social media time do not improve mental health: A reply to Thrul et al. (2025)*. **Psychology of Popular Media, 14(2), 210–212**。DOI 10.1037/ppm0000592,2025-03-27。经 Crossref / OpenAlex / Semantic Scholar 多处核实存在。**正文未取得。**
- **→ Ferguson(201–206)、Thrul(207–209)、Ferguson 回应(210–212)三篇构成同期同刊的 comment–reply 组。该交锋不是单向的。**
- 【三票冲突裁决】第二票的 unresolved 称「未查到 Ferguson 是否回应过 Thrul」;第一、三票均经 Crossref 核到 DOI 10.1037/ppm0000592。**裁决:回应文确实存在,以第一、三票为准。**

### (c-4) Rausch & Haidt 的批评
- **著录(Crossref 核实)**:Rausch, Z., & Haidt, J. (2025). *Why Ferguson's Meta-Analysis Should Not Be Used to Inform Debates on Social Media's Impact on **Adolescent** Depression and Anxiety: A Commentary*. **SSRN 5224958,DOI 10.2139/ssrn.5224958**,posted **2025-04-21**,机构 New York University。据 Rausch 本人 publications 页标注 Psychology of Popular Media "**in press**";**截至 2026-07 未见于 Crossref / OpenAlex 的已发表记录**。
- **【跨组冲突裁决】C07 组的两票把标题记作 "…Social Media's Impact on Depression and Anxiety"(无 "Adolescent")。本组三票均经 Crossref 直查 DOI,标题含 "Adolescent"。裁决:以 Crossref 版本为准,标题含 "Adolescent Depression and Anxiety"。** 标题本身即表明核心是「不该用于青少年抑郁/焦虑之争」的**适用性/外推批评**,誊录错误至多是其中一条。
- **实质指控(经其自有平台 After Babel 三连文逐字核到;SSRN 正文未取得),须分三类,不可混为一谈**:
  1. **誊录/编码错误**:2 处效应量(Lepp & Barkley 2022 把「安静静坐」的厌恶任务当作对照;Brailovskaia 2022 被编为 d=0)+ **3 处样本量错误**(Kleefeld 82→53、Lepp & Barkley 80→40、Przybylski 600→297)
  2. **纳入违规**:Gajdics & Jagodics(手机禁用而非社媒时长,d=−0.364)、Deters & Mehl 2013(未测社媒时长,d=−0.207)
  3. **漏纳**:Mosquera 2019、Engeln 2020;另指 2 项「操纵失败」(van Wezel 2021 对照组减 49.7% vs 干预组 58.3%;Collis & Eggers 2022 总屏幕时间反升)
- **其修正后合并值**:**d = +0.146, 95% CI [+0.048, +0.244]**;**仅抑郁/焦虑 11 项:d = +0.26, [+0.13, +0.40]**。第二票用 Ferguson 修订版 OSF 数据近似复现(剔 Deters + Gajdics、翻转 Lepp 符号)得 **d = 0.133 [0.038, 0.227]**,方向与量级吻合——**即他们的算术可复现**。
- **【最重要的裁决,三票一致】第 (1) 类誊录错误 Ferguson 已实质接受**(2024-10-02 修订 OSF 表中 Kleefeld=53、Lepp=40、Przybylski=297、Brailovskaia 2022 d=0.10 均与指控一致),**而合并值仍为 d ≈ 0.086 的零效应**。**「更正后转为显著」依赖的是第 (2)(3) 类有争议的纳入/剔除判断,不是誊录错误本身。成稿必须这样表述。**
- **利益相关须并列标注**:Rausch 与 Haidt 是《The Anxious Generation》因果论的主推者,**是被该 meta 直接反驳的主张方**;Ferguson 是长期公开的怀疑派;Thrul 等为公卫背景、立场相对独立但同为批评方。**三方均有立场,不宜把任一方当作裁决者。** After Babel 三连文为其自有 Substack,**非同行评审**。

### (d) 「三方混战」的准确结构
- **【措辞修正】「混战」高估了三者的相互 engagement**:May 等人**全文未引用** Ferguson、Lemahieu 或 Thrul 中的任何一方;Lemahieu 引用 Ferguson 但仅作描述性区分。**真实结构是:两场以 Ferguson 为中心的双边交锋(PPM 上 Ferguson ↔ Thrul,含 Ferguson 的正式回应;SSRN/After Babel 上 Rausch & Haidt → Ferguson),外加两份互不往来的独立 meta。**
- **【并存性的硬证据·研究级重叠量化,第二票逐条比对纳入清单】**
  - **May ∩ Lemahieu = 0 项**
  - **May ∩ Ferguson = 5 项**(Brailovskaia 2020、Brailovskaia 2022、Faulhaber 2023、Lambert 2022、Thai 2021)
  - **Lemahieu ∩ Ferguson = 6 项**(Allcott、Hall、Przybylski、Tromholt、Vally、Vanman)
  - **【三票冲突裁决】第三票称「三份 meta 共享大量原始研究,不构成独立证据链」,并举 Lambert/Hunt/Brailovskaia/Hall/Faulhaber 为例,但自承「未逐条提取 May 与 Lemahieu 的完整清单」。第二票做了 item-level 逐条比对。裁决:采信第二票的量化结果——重叠集中在 Ferguson 与另两份之间(各 5–6 项),而 May 与 Lemahieu 之间零重叠。第三票「不是三次独立检验」的定性对 Ferguson 那条轴成立,对 May–Lemahieu 那条轴不成立。**
- **正确表述**:「May 与 Lemahieu **零研究重叠**、结局与干预类型互不相交,严格意义上**不构成矛盾**;真正的冲突只在 Ferguson 与另两者的重叠区(各 5–6 项),而那里的分歧是**编码错误与聚合口径之争**,已有正式勘误与再分析在处理。」
- **三者系统性不同的三条轴**:①**结局构念**(抑郁症状 vs 享乐性情感/生活满意度 vs 聚合心理健康复合指标);②**干预类型**(限用+戒断 vs 纯戒断 vs 任意实验操纵含非减用研究);③**纳入设计**(仅 RCT vs 含非随机 vs 任意设计)。另有年份差:May 的 5 项 2023–2024 新研究晚于 Ferguson 的检索窗。
- **内部一致点(可作正面论据)**:May 自己的**完全戒断亚组 g=0.15 不显著**,与 Lemahieu 的**纯戒断零效应方向一致**;May 的显著总效应主要由**限用型(k=7)**驱动,而 Lemahieu 按设计排除了限用型研究;Ferguson 的聚合零结果部分可由 Thrul 揭示的两点解释(混入 7 项非减用/戒断实验 + 短时长干预的负向效应稀释)。

### 【横贯全组·对本选题最关键】三份 meta 无一是青少年证据
- **May**:平均年龄 24.2,各研究均值 18–28.93,全成人。
- **Lemahieu**:"All studies used an **adult** sample",均值 19.9–34,18+,明确无未成年人。
- **Ferguson**:按其 OSF 数据集年龄列,27 项中仅 **2 项均值 ≤17**(Ward 2017 = 16、Gajdics 2022 = 16.57);按 <19 岁计为 **4 项**(另加 Thai 2021 = 18、Yuen 2019 = 18.8);其余 19.74–34(Tromholt 34、Sagioglou 33.83、Allcott 29)。
- **→ 任何「减用社媒对青少年抑郁有效/无效」的表述都属跨年龄外推,必须显式标注。Rausch & Haidt 的标题主张(不应用于青少年抑郁/焦虑之争)在这一点上是成立的。**

## 修正记录(修正前→修正后)

1. 「限用型 0.33 显著 vs 戒断型 0.15 不显著」被读作限用更优 → **组间调节检验 Q(1) = 0.85, p = 0.36 不显著;作者摘要自己写明 "the difference was not significant";三个 moderator 全不显著。典型 difference-in-significance 陷阱。**
2. 「May 抑郁 g = 0.28,trim-and-fill 后 0.25」→ **0.25 是论文自报的结论值(仅补插 1 项);且该 meta 并未检出发表偏倚(Egger p = 0.85,漏斗对称),故 0.25 是无不对称证据下的保守调整,不宜说成「扣掉发表偏倚后仍有效」。**
3. 「Lemahieu 属减用/戒断 RCT meta」→ **是纯戒断 meta(显式排除仅减少使用的干预),且不是 RCT-only(70% 为被试间设计,含非随机)。与 May 并列为同类口径是错的。**
4. 「Lemahieu 10 研究 N=4,674 三结局全不显著」→ **数字全部成立,但须补:每个结局分母不同(PA/NA 各 9 项 14 效应量、LS 6 项 10 效应量);且 Allcott 2020 单项 N=2,813 占总样本 60.2%。**
5. 「Lemahieu 结局不含抑郁症状」→ **未把抑郁设为独立结局;个别研究的抑郁量表(如 Tromholt 的 CES-D)被并入 negative affect。**
6. 「Ferguson 2024/2025」含糊 → **PPM 14(2), 201–206, DOI 10.1037/ppm0000541;线上 2024-05-02、纸本 2025;成稿写 2024。**
7. **【原论断遗漏】Ferguson 那篇已有 APA 正式勘误:DOI 10.1037/ppm0000586, PPM 14(2), 328, 2025-02-03。** 且其 OSF 数据集 2024-10-02 已被修订,采纳了三处样本量更正。
8. 「Johns Hopkins reanalysis:加干预时长 moderator 后有益」→ **四步:①全样本复算 d=0.086 不显著 → ②剔除 7 项非减用/戒断研究后 k=20, d=0.081 仍不显著 → ③时长调节 d=0.333 (p=.006),分层双向:<1 周 d=−0.175 (p=.010,显著更差,仅 4 项)、≥1 周 d=+0.156 (p=.016)→ ④二次项 k=19,weeks p=.013 / days p=.018,最优约 3 周。「短干预反而有害」这一半不得略去。**
9. **【原论断遗漏】Ferguson 已发表正式回应:PPM 14(2), 210–212, DOI 10.1037/ppm0000592(2025-03-27)。该交锋是双向的。**
10. 「Rausch & Haidt 指效应量/样本量誊录错误」→ **标题即为外推批评(含 "Adolescent");指控须分三类:誊录/编码错误(已被 Ferguson 在 OSF 修订中实质接受,零结论不变)、纳入违规、漏纳。其「更正后 d=+0.146 [+0.048,+0.244]」依赖的是有争议的纳入/剔除判断,不是誊录错误本身。**
11. 「三方混战」→ **实为两场以 Ferguson 为中心的双边交锋 + 两份互不往来的独立 meta;May 全文未引用另两方。**
12. 「因结局与纳入口径不同可部分并存」→ **可量化:May ∩ Lemahieu = 0;May ∩ Ferguson = 5;Lemahieu ∩ Ferguson = 6。May 与 Lemahieu 严格不构成矛盾;真正冲突只在 Ferguson 的重叠区。**
13. **【横贯】三份 meta 都不是青少年证据基础**(May 均值 24.2;Lemahieu 全成人;Ferguson 27 项中仅 2 项均值 ≤17)。**任何用于青少年的表述必须标注为外推。**
14. **【底稿排雷】line5-policy.md 第 90 行把 Burnell et al. 的 SSM–Mental Health meta(32 RCT、5,544 人、g = .17 显著为正)误署为 Ferguson 的零效应 meta,必须改正。**

## 未回溯项

- **【三票均未回溯,不得承重】Ferguson (2024) PPM 正文与 95% CI [−.018, .197]**。APA 完全闭源(Unpaywall: is_oa=false, oa_status="closed",无任何 OA 副本或仓储版本);PsycNet 为 JS 渲染并被 Incapsula 反爬拦截;ResearchGate 403;作者个人站未挂该 PDF;SSRN 路径受阻;Wayback 无快照或被禁。**该 CI 目前唯一可查的逐字出处是 After Babel Part 3(David Stein 客座,2024-10-04)——属对立阵营的 Substack,非一手。**
  - 缓解证据:点估计已由两票分别从 Ferguson 自己的 OSF 数据独立复算(0.0865)+ Thrul 等独立复算(0.086)三向佐证;且所述 CI 与 p=0.104 算术自洽(中点 0.0895、半宽 0.1075 → z≈1.63 → p≈0.103)。
  - **成稿建议:只写 "d ≈ 0.086–0.088,置信区间跨零(原文 .088,后经勘误)",或对 CI 明确标注「未核到一手」。**
- **【三票均未回溯】APA 勘误 DOI 10.1037/ppm0000586 的具体更正内容**。存在性、日期(2025-02-03)、卷期页(14(2), 328)由 Crossref relation 字段确认,但**勘误具体改了什么、是否改动了发表版的合并 d 与 CI,无法确定**(PsycNet 全文与记录页均被反爬拦截;Semantic Scholar / EuropePMC 无摘要;Wayback 429 限流)。**因此「发表版 article of record 现在报的到底是 .088 还是别的数」这一点无法裁决;也无法判断该勘误是否即对应 Rausch & Haidt 所指的誊录错误。**
- **【三票均未回溯】Rausch & Haidt SSRN 5224958 正文与具体指控**。SSRN 全站 Cloudflare CAPTCHA(papers.cfm 与 Delivery.cfm 均 403,代理路径同样撞到验证,按规则未绕过);Wayback 无快照;Semantic Scholar 无该 DOI 记录。**其实质指控仅靠同作者的 After Babel 三连文(2024-08/09/10)核实;SSRN 版本(2025-04-21)可能已因 Ferguson 的勘误而调整措辞或数字,存在不一致风险。是否已在 PPM 正式发表亦无法确认(Crossref 与 OpenAlex 截至 2026-07 均无条目,仅作者本人网页标注 in press)。**
- **【三票均未回溯】Ferguson 对 Thrul 的回应正文(DOI 10.1037/ppm0000592)**。仅有标题与书目;**其反驳理由未核**。
- **【三票均受限】更晚近的第四份 meta、其他勘误/撤稿通知、以及针对 May(2025-10 发表,极新)的批评性回应,未做主动检索**(三票的 WebSearch 配额均已耗尽,仅能用 WebFetch 直连已知 URL 与 API + DuckDuckGo HTML 端点)。**该方向的反证检索属未覆盖面。**
- 第一票的 unresolved「Thrul 等的 Johns Hopkins 机构归属未核实」**已由第三票从接收稿全文核实,不再是未回溯项**。
- 第一票的 unresolved「May 参与者年龄范围未核到」**已由第二、三票核到各研究均值区间 18–28.93,不再是未回溯项**;但**个别纳入研究是否含 18 岁以下受试者仍无法完全排除**(论文未设年龄纳入限制这一点已核实)。
- 第三票的 unresolved「May 与 Lemahieu 完整纳入清单未逐条提取」**已由第二票从各自 PMC 全文提取并做 item-level 比对,不再是未回溯项**。

## 证据分级

- **May, Malouff & Meynadier (2025):单源已核**。PMC 全文,三票逐字一致。**但期刊为 MDPI、2025-10 才上线、尚无独立复核或引用检验;10 项 RCT、N=1,491 属小样本合成。**
- **Lemahieu et al. (2025):多源证实**。PMC 全文 + Europe PMC REST API + Sci Rep,三票一致;10 项 N 逐项相加与自报吻合。**但 60% 样本来自单一研究(Allcott 2020),且含非随机设计。**
- **Ferguson (2024/2025):方向存争 + 部分未验证**。正文闭源、CI 未核到一手、且**存在内容不明的正式勘误**;但**零效应方向可靠**——点估计经两票各自从作者自己的 OSF 数据独立复算(0.0865),加 Thrul 的第三次独立复算(0.086),三向一致。**引用时必须同时标注勘误 DOI 10.1037/ppm0000586。**
- **Thrul 等再分析:单源已核**。PsyArXiv 接收稿全文,两票取到并逐字核对。**注意其资助含 Aramco Services Company。**
- **Rausch & Haidt:未验证 + 利益相关方自述**。SSRN 正文三票均未取得;实质指控仅由其自有 Substack(非同行评审)核实。**唯一被硬证据支撑的部分是「三处样本量错误确实存在」——因 Ferguson 自己的 OSF 修订版已采纳这三处更正,构成间接证实。「更正后转为显著」则依赖有争议的纳入判断,属方向存争。作者为被批评 meta 所反驳的主张方,须标注利益相关。**
- **「限用优于戒断」:已被推翻**(Q(1)=0.85, p=0.36)。
- **整组用于青少年:未验证(纯外推)**。三份 meta 无一以青少年为主体。
- **「三份可部分并存」这一判断本身:多源证实**。由 May 与 Lemahieu 零重叠 + 三条系统性不同的轴 + May 戒断亚组与 Lemahieu 零效应的方向一致性共同支撑。


---

# C13 最终判决:CORRECTED(3/3 票)

论断组:Broadband 自然实验三连 —— (a) Donati 意大利 / (b) Arenas-Arroyo 西班牙 / (c) Golin 德国。
三票独立验证结论一致:核心数值与方向成立,但**「三连同构念」的框架不成立**,且 (c) 的效应量三票均无法回到一手。

---

## 锁定口径(成稿必须用)

### 组框架层(最重要,三票一致)

1. **不能写成「三连结局都是临床/住院」。** 只有 (a)(b) 是医院行政记录;(c) Golin 用的是德国社会经济追踪调查(GSOEP)的**自报**心理健康量表。第三方一手佐证:Arenas-Arroyo 等 IZA DP15728 脚注 12 原文 —— "Golin (2022) uses self-reported measures of wellbeing and mental health from the German Socio Economic Panel (SOEP)";Donati 等 IZA DP15202 正文亦述 Golin "using survey data from the German Socio-Economic Panel"。
2. **(b) 的作者在正文里点名把 (c) 当作方法论缺陷案例**(IZA DP15728,第 135–138 行):"Another problem arises from studies using self-reported mental health measures (e.g., Golin, 2022), as the Internet is a frequent source of information about emotional issues, which can affect a person's perception regardless of whether there is an actual effect on health or not." 因此 (c) 不构成对 (a)(b) 的独立临床佐证。
3. **不能写成「三个互相独立的自然实验」。** (a) 与 (c) 共享同一工具变量族 —— 市镇/住户到既有语音电信骨干网的距离(承自 Falck et al. 2014),(b) 原文自述这一点:"comes from the distance of households to older pre-existing infrastructure";只有 (b) 用 FTTH 铺设作外生变异。三条证据里两条共用同一识别假设,共同暴露于同一条排他性约束批评。
4. **不能写成「三连性别模式一致」。** (a) Donati 摘要明写效应见于两性("for both genders":抑郁/焦虑、药物滥用、人格障碍),仅进食障碍为女性特有;只有 (b)(c) 是女性特异。
5. **构念不是同一个「高速互联网」。** (a) = 意大利 ADSL(+3G),2001–2013;(b) = 西班牙 FTTH 光纤,2007–2019;(c) = 2000 年代德国 DSL。技术代际、时间窗、同期主导线上活动差异很大;(a) 的暴露窗基本早于智能手机与社媒饱和期。

### (a) Donati 等,意大利

6. 出处:Donati D, Durante R, Sobbrio F, Zejcirovic D. "Lost in the net? Broadband internet and youth mental health." *Journal of Health Economics* **103**, 文章号 103017, 2025-09(线上 2025-07-04),DOI 10.1016/j.jhealeco.2025.103017,PII S0167629625000529,PMID 40652858。Crossref 确认无勘误/撤稿。
7. 摘要逐字(经 Europe PMC / PubMed / RePEc-EconPapers 三处镜像一致):
   > "administrative data on the universe of cases of mental disorders diagnosed in Italian hospitals between 2001 and 2013"
   > "Broadband internet access raises the prevalence of mental disorders among younger cohorts (born between 1985 and 1995) by 0.08 standard deviation units, but it does not impact older individuals (1974 and 1984). The adverse effects are driven by individuals who were exposed early in their lives (before the age of 20)."
   → 论断四要点(意大利 / 住院精神障碍诊断 / +0.08 SD / 1985-95 世代 / 20 岁前驱动 / 1974-84 无影响)全部逐字成立。
8. 作者已主动排除「检出率上升」这一替代解释,逐字:"indicating that the negative outcomes are not merely a result of increased awareness and detection of these conditions"(效应在自伤、急诊/强制住院上同样存在)。这一句应保留,它是该文最硬的一环。
9. **剂量口径警示(源自工作论文 IZA DP15202,2022-03)**:该文处理强度全篇表述为 "increasing the ADSL coverage from 0 to 100%",即满剂量对比,不是「1 个标准差宽带」的边际效应。主设定因变量为 "dummies indicating the occurrence of any case of a specific mental disorder in a given municipality-year"(市镇-年是否出现至少一例),不是个体患病率。**该口径来自 WP 版,发表版是否沿用未能确证 —— 见「未回溯项」。**
10. 关键词含 "Mental health, Internet, ADSL, 3G",即同时含固网宽带与 3G 移动网,只写「宽带」略窄。

### (b) Arenas-Arroyo 等,西班牙

11. 出处(须改):Arenas-Arroyo E, Fernandez-Kranz D, Nollenberger N. "High speed internet and the widening gender gap in adolescent mental health: **Evidence from Spanish hospital records**." *Journal of Health Economics* **102**, 文章号 103014, 2025-08(线上 2025-05-24),DOI 10.1016/j.jhealeco.2025.103014。工作论文版为 IZA DP15728(2022-11,本版 2023-05),标题末尾无 "Spanish"。Crossref 确认无勘误/撤稿。
12. 发表版摘要逐字:
    > "We exploit variations in fiber optic (FTTH) deployment to assess the impact of high-speed internet access on adolescent mental health. Our findings reveal that FTTH access increases addictive Internet usage and reduces time allocated to sleep, homework, as well as social interactions with family and friends. Access to FTTH increases mental health diagnoses in hospitals and contributes to a notable rise in adolescent suicide rates, particularly among girls."
    → **「自杀死亡率上升」这条必须补上**,原论断只写「诊断上升」,漏掉了比诊断更硬的结局。
13. 主结局逐字(IZA DP15728):"We find that fiber penetration significantly increases BMH cases in adolescents aged 15 to 19. One standard deviation (SD) increase in fiber penetration increases cases of BMH by 13.3%. Girls entirely drive this effect. When we analyze older individuals (20 to 24 years old), we do not find statistically significant results. Instead, we do find negative effects of Internet exposure for younger girls (ages 10-14) but, again, no effect for boys of that age."
14. 分性别系数(IV 主设定,15–19 岁,1 SD 光纤渗透,SD=0.067 lines/inhabitant):全体 +24.5%(系数 2.378,10% 显著)、男孩 +13.2%(系数 1.199,SE 1.750,不显著)、女孩 +35.3%(系数 3.631,SE 1.629,p<0.05)。20–24 岁全不显著(全体 1.9%、男 7.7%、女 −5.7%)。
15. 自伤/自杀未遂(Table 2,IV,15–19 岁):女孩系数 1.123***(1% 显著)→ **+112.3%**;男孩 −0.089 不显著。**必须标注基线极低**:因变量均值 0.067 例/百人,+112.3% 是极低基数上的相对变化。女孩焦虑 0.551*(10%)、药物滥用 1.157**(5%);进食障碍、ADHD、精神分裂、酒精滥用均不显著。
16. 机制逐字:"a one standard deviation increase in fiber penetration leading to an almost 9% increase in addictive internet use, which is statistically significant at the 5% level. Conversely, the effect for boys is 3.6% and statistically insignificant. The results also show that exposure to high-speed internet reduces sleep time by 21%, homework time by 30%, and time spent socializing with family and friends by 44% for girls, but not for boys."
17. **「男孩无」必须限定**:对住院 BMH 主结局成立(不显著非零);但作业时间对男孩**统计显著**——"Although the effect on homework time is statistically significant for boys, it is much smaller in magnitude than the effect for girls (+17% versus +30%)"。
18. 网络霸凌零结果逐字(IZA DP15728,Table 5 第 (6) 列):"the results also show that fiber expansion has no effect on the probability of being a victim of online bullying, neither for girls nor for boys"。摘要级表述:"we find no evidence of online bullying"。**构念是「自报遭受网络霸凌的概率」(受害方)**,且只在工作论文核到。
19. **分析层级须写明**:省(province)-年面板,N≈600(约 50 省 × 12 年),标准误按省聚类。光纤渗透率数据来自 CNMC,省级 —— "Our data comes at the province level and covers the period 2007 to 2019."。西班牙仅 52 个省,识别单元**远粗于** (a) 的意大利市镇级,横向比较时不应当作同等精度。
20. **两文效应量尺度不可直接并列**:(a) 是「ADSL 覆盖 0→100%」,(b) 是「光纤渗透率 1 个 SD」。

### (c) Golin,德国

21. 出处:Golin M(单作者)。"The effect of broadband Internet on the gender gap in mental health: Evidence from Germany." *Health Economics* **31**(Suppl S2): 6–21, 2022-07-13,DOI 10.1002/hec.4570,PMID 35833231。经 PubMed / Crossref / OpenAlex 三源确认,无勘误撤稿。
22. 摘要逐字(Europe PMC 与 Semantic Scholar 两镜像一致):
    > "In this paper, I analyze the causal effect of broadband Internet access on **the mental health of adults**. I leverage confidential information on the coordinates of respondents to the German Socio-Economic Panel (GSOEP) and exploit technological features of the German telecommunication network to instrument for broadband Internet access. **The results are suggestive that** broadband Internet leads to worse mental health for women (primarily those aged 17-30) but not for men, thus widening the gender gap in mental disorders. Looking at sub-facets of mental health, broadband access leads to a worsening of socializing behavior and ability to cope with emotional problems."
23. **三处必改**:(i) 研究对象是 **adults**(成人),17–30 只是效应集中的子样本、不是抽样框,不能读作青少年研究;(ii) 作者自设限定语 **"suggestive"** 不得剥掉;(iii) 结局是自报量表的社交行为与情绪应对分维度。
24. **效应量:不得给任何数字**(见未回溯项)。只能作定性引用。

### 独立后续证据(方向支持,机制冲突,建议并列)

25. Churchill BF, Johnson KR. "Broadband Internet Access and Adolescent Mental Health in the U.S." NBER WP w34614, 2026-01(https://www.nber.org/papers/w34614)。用美国 2009–2019 YRBS + 全国宽带铺设,摘要逐字:"a one-standard-deviation increase in broadband internet access was associated with a 9.3–16.5-percent increase in adolescent suicide ideation... we show that greater broadband internet access was associated with increases in cyberbullying and body dissatisfaction among adolescent girls"。
    → **结局方向被独立重复,但机制未收敛**:该文发现女孩网络霸凌上升(与 (b) 的零结果**相反**)、男孩睡眠不足上升(与 (b) 的女孩专属睡眠效应相反),且**男女两性自杀意念皆升**。因此「未发现网络霸凌增加」是西班牙单国结果,不可推广;「仅女孩」的叙事也被弱化。

---

## 修正记录(修正前→修正后)

| # | 修正前 | 修正后 |
|---|---|---|
| 1 | 三连结局都是临床/住院诊断 | 仅 (a)(b) 是医院行政记录;(c) 是 GSOEP 自报量表,且被 (b) 作者点名批评为构念缺陷 |
| 2 | 三个独立自然实验 | (a)(c) 共享 Falck et al. 2014 的电信骨干网距离工具变量族;三者均为 IV/准实验而非政策冲击 |
| 3 | 三连同向支持「女孩受损」 | (a) 效应 "for both genders",仅进食障碍女性特有;性别模式三连不一致 |
| 4 | 构念 = 高速互联网(单一处理变量) | 三代技术、三个时间窗:意 ADSL(+3G) 2001-13 / 西 FTTH 2007-19 / 德 DSL 2000s |
| 5 | (c) 德国 17-30 岁女性心理健康变差 | (c) 研究对象为 **adults**;17-30 是效应集中子组;作者措辞为 "results are suggestive that" |
| 6 | (c) Golin 2022(Health Economics) | Marta Golin 单作者,Health Economics 31(S2):6-21, DOI 10.1002/hec.4570 |
| 7 | (b) Arenas-Arroyo et al.(JHE 2025, IZA DP15728) | Arenas-Arroyo, Fernandez-Kranz & Nollenberger;JHE 102:103014, 2025-08, DOI 10.1016/j.jhealeco.2025.103014 |
| 8 | (b) 只写「女孩住院诊断上升」 | 须补:该文同时报告**青少年自杀死亡率显著上升**(发表版摘要写入) |
| 9 | (b) 男孩无效应 | 主结局(住院 BMH)男孩不显著;但作业时间对男孩统计显著(+17% vs 女 +30%) |
| 10 | (b) 读起来像个体级出院记录 | 省-年面板 N≈600,约 50 省 × 12 年,省级聚类;+112.3% 是均值 0.067 例/百人的极低基线上的相对变化 |
| 11 | (b) 西班牙光纤(未标粒度) | CNMC 省级(52 省)面板,识别单元远粗于 (a) 的市镇级 |
| 12 | (b) 未发现网络霸凌增加 | 成立,但构念是「自报**遭受**网络霸凌的概率」,且仅在 IZA DP15728 工作论文正文核到 |
| 13 | (a) 宽带使 1985-95 世代 +0.08 SD | 该系数(WP 口径)对应 ADSL 覆盖 **0→100%** 的满剂量对比;主设定因变量为**市镇-年是否出现至少一例**,非个体患病率 |
| 14 | (a) 出处只写「宽带」 | 关键词含 ADSL **与 3G**;JHE 103:103017, 2025-09 |

**票间冲突与裁决:**
- **(b) 男孩自杀死亡是否为零**:一票依发表版摘要("particularly among girls")判「男孩无」;另一票依 IZA DP15728 全文,报告 15–19 岁男孩在 **IV Poisson 设定下** "statistically significant but much smaller in magnitude than for girls"(男约 23% vs 女 71%),仅线性死亡率模型下不显著。**裁决:采后者**(更靠近一手全文、且是更具体的模型层级信息),成稿写「自杀死亡上升主要在女孩;男孩在部分设定下亦显著但幅度小得多」。
- **(a) 0.08 SD 的剂量/层级口径**:仅一票从 IZA DP15202 全文提出;另两票只核到发表版摘要,未反驳。**裁决:保留该限定,但明确标注它源自工作论文版,发表版未能确证**(该票自己也把这一点列为 unresolved)。
- **(a) 汇总设定不显著**:一票据 WP Table 2 指出「所有年龄组和性别合并后 no statistically significant relationship」,效应只在按出生世代 × 性别切分后出现。同上,标为 WP 口径。

---

## 未回溯项

1. **(c) Golin 2022 的具体效应量(系数、SD 单位、样本量、置信区间)—— 三票全部失败,标记「未回溯,不得承重」。** 已穷尽路径:Wiley 全文 HTTP 402、SSRN 403、OpenAlex(is_oa=false,best_oa_location=null)、Unpaywall、Semantic Scholar(openAccessPdf 空)、Europe PMC(inEPMC=N,无 PMCID)、PMC 无全文、OpenAIRE、RePEc/IDEAS(仅出版商链接)、牛津 ORA 404、苏黎世 ZORA 被拦、作者 Google Sites 需登录、Wayback 快照仅含摘要与参考文献(无结果节)。**成稿若要写具体数字,必须先取得全文;不得估算。**
2. **(c) 结局变量的确切量表未从一手确认。** 摘要只说 GSOEP 自报并提到 sub-facets(社交行为、情绪应对),高度提示 SF-12 心理成分量表(MCS),但全文不可及 ——「SF-12 MCS」不得作为已核事实使用。
3. **(b) 的全部数值(13.3% / 112.3% / 9% / 21% / 30% / 44% / 13.2% / 35.3%)均来自 IZA DP15728(2023-05 版),非 JHE 102 发表版。** ScienceDirect 403,发表版全文三票均未取得。引用这些百分比时**必须标注为工作论文版口径**。另需注意措辞强度差异:WP 正文为 "Girls entirely drive this effect",发表版摘要为较弱的 "particularly among girls" —— 是否因同行评审放宽,无法确证。
4. **(b) 网络霸凌零结果是否保留在发表版**,以及表号是否变动,未能确认(发表版摘要未提)。
5. **(a) 发表版是否沿用 WP 的「市镇-年 至少一例」主设定、0.08 SD 究竟标准化的是什么指标**,无法确证:ScienceDirect 403、Tor Vergata 机构库文件处于 request-item 限制、无 PMCID。
6. **(a) 正文层面细节**(样本量、一阶段强度、ADSL 与 3G 两套变异的分别效应量、平行趋势检验)未经一手核对,仅核到官方摘要级别。
7. **三篇的资助来源与利益冲突声明未能统一核实。** 一票从发表版/机构页取得:(a) European Research Council / Horizon 2020(grant 759885)/ Bocconi LEAP;(b) Fundación de las Cajas de Ahorros;(c) Nuffield College, Oxford —— 均为学术与公共科研资助;但另两票因付费墙无法复核 JHE 的 Declaration of Competing Interest。**结论:未发现利益相关证据,但不能据此声明三篇无利益冲突。**
8. **反证检索覆盖不完整**:三票的 WebSearch 配额在任务开始前均已耗尽(200/200),无法做开放式反证检索(是否存在质疑这三篇的评论文章、重复性研究或失败的复制)。已通过 Crossref 的 update-to / updated-by 字段确认三篇均无正式勘误或撤稿,但无法排除非正式学术批评。

---

## 证据分级

- **(a) Donati 意大利:多源证实(摘要级)/ 单源已核(正文级)。** 摘要经 Europe PMC、PubMed、RePEc、Tor Vergata 机构库多镜像逐字一致;正文口径依赖 IZA DP15202 工作论文单一来源。可承重,但剂量与层级限定语必须带上。
- **(b) Arenas-Arroyo 西班牙:单源已核(工作论文版)。** 发表版摘要多镜像确认定性方向,全部具体数值仅回溯到 IZA DP15728 一个版本。可承重,须标「工作论文版口径」。
- **(c) Golin 德国:方向单源已核 / 数值未验证。** 方向(女性变差、男性无、集中 17–30、作者自限 "suggestive")经两个独立镜像逐字确认;**效应量属「未回溯,不得承重」**。只可作定性引用,且不得与 (a)(b) 并列为同构念临床证据。
- **组框架(「三连收敛」):方向存争 → 已修正。** 三票一致认定原框架夸大了收敛度(构念不同构、识别不独立、性别模式不一致)。修正后的框架 ——「三国四类外生变异指向同方向的负面心理健康效应,但结局构念、识别策略与性别模式各异」—— 属**多源证实**。
- **独立复制(Churchill & Johnson NBER w34614):单源已核(工作论文,未同行评审)。** 结局方向支持,机制归因与 (b) 冲突,引用时须并列。


---

# C14 最终判决:CORRECTED(3/3 票)

论断组:美国自报趋势 —— (a) YRBS 女生持续悲伤/绝望;(b) NSDUH 2021 官方断点;(c) 2021 MDE 数字;(d) Keyes 2019 MTF。
三票一致:**(c)(d) 数值全部逐字成立无需修正**;(a)(b) 的**数值方向成立,但三处引语与两处出处属误植**,必须换掉。

---

## 锁定口径(成稿必须用)

### (a) YRBS —— 2011 基线裁决与三个引语

1. **2011 女生基线裁决 = 35.9%(常引作 36%),35% 错误。**
   一手:MMWR Surveill Summ 2012;61(SS-4) Table 21「Percentage of high school students who felt sad or hopeless」—— 女生 Total **35.9%(95% CI 34.1–37.8)**,男生 21.5%(19.9–23.1),全体 28.5%(27.2–29.7)。正文:"During the 12 months before the survey, 28.5% of students nationwide had felt so sad or hopeless … higher among female (35.9%) than male (21.5%) students"。
   交叉校验:CDC 2023 稿称 57% 是 "a nearly 60% increase" —— 57/35.9 = +58.8%(合 "nearly 60%");若基线 35%,则 +62.9%,应写成 "more than 60%"。
   35% 的来源疑为混淆:35% 是 2021 年 Asian 学生与 heterosexual 学生的值(YRBS DSTR 2011–2021 分组页)。
   **建议写法:2011 = 35.9%(常引作 36%)。**

2. **CDC 2023-02-13 新闻稿逐字(介词是 over,不是 in):**
   > "According to new CDC data released today, nearly 3 in 5 (57%) U.S. teen girls felt persistently sad or hopeless in 2021—double that of boys, representing a nearly 60% increase and **the highest level reported over the past decade**."
   出处:《U.S. Teen Girls Experiencing Increased Sadness and Violence》,https://www.cdc.gov/media/releases/2023/p0213-yrbs.html(**不是** p0213-yrbs-report.html),For Immediate Release: Monday, February 13, 2023。同稿另称女生 "Nearly 1 in 3 (30%) seriously considered attempting suicide—up nearly 60% from a decade ago"。

3. **CDC 2024-08-06 新闻稿真实 URL 与逐字:**
   https://www.cdc.gov/media/releases/2024/p0806-youth-mental-health.html(**不是** p0806-YRBS-report.html),标题《CDC Data Show Improvements in Youth Mental Health but Need for Safer and More Supportive Schools》,"For immediate release: August 6, 2024"。
   > "Decreases in the percentage of students overall who experienced persistent feelings of sadness or hopelessness (from 42% to 40%)."
   > "Decreases in the percentage of female students who experienced persistent feelings of sadness or hopelessness (from 57% to 53%) and who seriously considered attempting suicide (30% to 27%)."
   同稿另有反向恶化项:校内被武器威胁 7%→9%、被霸凌 15%→19%、因安全顾虑缺课 9%→13%。

4. **「十年首降」不是 CDC 措辞 —— 三票一致,这是本组最重要的引注修正。**
   CDC 全篇未用 first / first time + decade 描述该下降。可用的官方逐字只有两条:
   > (DSTR 2013–2023)"Two-year changes show a recent decrease in the percentage of high school students who experienced persistent feelings of sadness or hopelessness from 2021 to 2023. All other experiences and behaviors did not change."
   > (DSTR 2013–2023 趋势判词)"The percentage of female students who experienced persistent feelings of sadness or hopelessness increased from 2013 to 2023 but decreased from 2021 to 2023." 男生:"increased from 2013 to 2023 but did not change from 2021 to 2023."
   **「首降」这一事实本身成立**(总体序列 2013–2023 = 30/30/31/37/42/40,窗口内无更早下降;2013→2015 为持平非下降),但**必须标为分析者推论,不得引作 CDC 原话**。

5. **CDC 自己给的限定语必须带上(原论断漏掉):**
   > "The 2021 data are drawn from a year when schooling was still substantially disrupted due to COVID."(2024-08-06 稿逐字)
   即 57% 峰值是 COVID 扰动年读数。

6. **下降的适用范围有限:** 2021→2023 的显著下降只见于**全体、女生、西班牙裔学生**三项;男生 29%→28% 未达显著;按种族「For most groups … did not change from 2021 to 2023」。

7. **精确值 vs 取整值:**
   2023 一手精确值(MMWR Suppl 2024;73(4)《Mental Health and Suicide Risk Among High School Students and Protective Factors — YRBS, United States, 2023》,PMC11559681):全体 **39.7%**、女生 **52.6%**、男生 **27.7%**;逐字 "Overall, 39.7% of students experienced persistent feelings of sadness and hopelessness, 28.5% experienced poor mental health, 20.4% seriously considered attempting suicide, and 9.5% had attempted suicide." / "The prevalence among female students was higher than among male students for persistent feelings of sadness or hopelessness (52.6% versus 27.7%)"。
   2021 对应值:女 57.0%、全体 42.3%。
   53% / 40% / 28% 是 CDC 新闻稿与 DSTR 图注的取整。

8. **序列(取整,DSTR「Progress At A Glance」):**
   全体持续悲伤/绝望 2013–2023 = 30 / 30 / 31 / 37 / 42 / 40;认真考虑自杀 = 17 / 18 / 17 / 19 / 22 / 20;自杀未遂 = 8 / 9 / 7 / 9 / 10 / 9。
   女生 2013 = 39%,2021 = 57%,2023 = 53%;男生 2013 = 21%,2021 = 29%,2023 = 28%。
   2011 版口径(DSTR 2011–2021):全体 2011 = 28%,女 36%,男 21%;重叠年份(2013–2021)与 2023 版完全一致,交叉校验通过。

9. **跨报告拼接必须标注。** 36%/2011 来自 2011–2021 版报告,53%/2023 来自 2013–2023 版报告;2023 版自身的十年基线是 2013(女生 39%)。用 2011 起点会放大涨幅(36→57 为 +58%;CDC 自身口径 2013→2023 为 39→53)。

10. **构念逐字(不可与另一指标混用):**
    > "felt so sad or hopeless almost every day for at least two weeks in a row that they stopped doing their usual activities"
    时窗为 **During the Past Year**(过去 12 个月),单题、自报、非临床诊断。与另一独立指标「poor mental health(过去 30 天)」(2021=29%、2023=28.5–29%,2021 年新增题)**不可混用**。

### (b) NSDUH 官方断点 —— 引语必须整句替换

11. **原引语 "estimates from this year should not be compared with previous years" 在所指 PDF 中不存在。** 三票分别用 pdftotext 全文检索(约 106 万字符 / 15,266 行),"from this year"、"this year" 命中数为 0。**方向成立,引语必须换。**
    该 PDF 为《2021 NSDUH Methodological Summary and Definitions》(CBHSQ, Rockville MD, October 2022),https://www.samhsa.gov/data/sites/default/files/reports/rpt39442/2021NSDUHMethodSummDefs100422.pdf(HTTP 200,3,783,516 字节,直连与 Wayback 双源确认)。
    **可用逐字(任选其一):**
    > (1) "Because of changes to data collection procedures and other methodological changes for 2021, estimates between 2021 and prior years should not be compared."(术语表前言)
    > (2) "It would not be appropriate to compare estimates from the 2021 NSDUH with those from prior years."
    > (3) "No statistical tests will be performed to compare estimates in 2021 with those in 2019 or prior years because estimates from a multimode year are not comparable with estimates from a single-mode year."
    > (4) "methodological investigations led to the conclusion that estimates based on multimode data collection in 2021 are not comparable with estimates from 2020 or prior years. Therefore, national reports and tables for the 2021 NSDUH present estimates from 2021 only."
    > (5) "A concatenated public use file will not be produced that contains data from 2021 and prior years."

12. **断点是双重的,不止 2021。** §3.3.3.2(第 52 页)逐字:"...led the Substance Abuse and Mental Health Services Administration (SAMHSA) to conclude that estimates for 2020 (which included multimode data collection) should not be compared with estimates for 2021.";且 "no statistical tests will be performed to compare 2020 estimates (based on two quarters of data) with those of any other year, including 2021"。故 2005→2021 连线跨越 **2020 与 2021 两处**官方断点。

13. **断点性质:** 2021 全年改为 web / 入户混合模式(multimode),web 应答者报告物质使用与心理健康问题的倾向系统性偏低,COVID 效应与模式效应混淆不可分离;2021 年 54.6% 网访 / 45.4% 入户。

14. **更贴题的可替换官方引注(建议直接用这条):** NIMH major depression 统计页对同一 20.1% 数字自带断点声明:
    > "2021 NSDUH estimates are not comparable with estimates from prior years given the use of multimode data collection procedures throughout the entire year and the rate of non-response."
    这条的价值在于:**断点由 NIMH 自己在同一页转载**,不是外部批评者的说法。

15. **8.7%(2005)必须标为二次分析,不是 SAMHSA 官方口径。**
    Mojtabai R, Olfson M, Han B. "National Trends in the Prevalence and Treatment of Depression in Adolescents and Young Adults." *Pediatrics* 2016 Dec;138(6):e20161878;DOI 10.1542/peds.2016-1878;PMID 27940701;PMCID PMC5127071。数据 NSDUH 2005–2014 公用文件,12–17 岁 **N=172,495**。逐字:
    > "the 12-month prevalence of MDEs increased from 8.7% in 2005 to 11.3% in 2014 in adolescents"

16. **8.7%→20.1% 连线还掩盖了前段平台期(必须写)。** 前七年基本持平:2005–2011 = 8.7, 8.0, 8.2, 8.4, 8.0, 8.0, 8.3;原文亦称 "the prevalence of 12-month MDE was stable over the 2005 to 2011 period; however, it gradually increased in later years"。**更稳妥的表述是「2011/2012 年前后起转折」,而非两点直连。**

### (c) 2021 MDE —— 全部成立,无需修正

17. NIMH(https://www.nimh.nih.gov/health/statistics/major-depression),数据年 2021 NSDUH,12–17 岁:
    - MDE **20.1%**;逐字 "An estimated 5.0 million adolescents aged 12 to 17 in the United States had at least one major depressive episode. This number represented 20.1% of the U.S. population aged 12 to 17."
    - 女 **29.2%**,男 **11.5%**
    - MDE with severe impairment 14.7%
    - 逐字 "In 2021, an estimated 40.6% of U.S. adolescents with major depressive episode received treatment in the past year."(分母为「有 MDE 的青少年」)
    - 同页自带 (b) 的断点警示(见第 14 条)

### (d) Keyes 2019 MTF —— 全部成立,补三处精确化

18. Keyes KM, Gary D, O'Malley PM, Hamilton A, Schulenberg J. "Recent increases in depressive symptoms among US adolescents: trends from 1991 to 2018." *Soc Psychiatry Psychiatr Epidemiol.* 2019 Aug;54(8):987–996;DOI 10.1007/s00127-019-01697-8;PMID 30929042;PMCID PMC7015269。
19. 逐字:
    > "Data are drawn from 1991 to 2018 Monitoring the Future yearly cross-sectional surveys of 8th, 10th, and 12th grade students (N = 1,260,159). Depressive symptoms measured with four questions that had consistent wording and data collection procedures across all 28 years."
    > "Among girls, depressive symptoms decreased from 1991 to 2011, then reversed course, peaking in 2018; these increases reflected primarily period effects, which compared to the mean of all periods showed a gradual increase starting in 2012 and peaked in 2018 (estimate = 1.15, p < 0.01). Cohort effects were minimal"
    > "It is noteworthy that the survey procedures and items assessing depressive symptoms in this data set have remained constant across 28 years."
20. **N 用精确值 1,260,159**(不是约 126 万才对得上)。
21. **2012 拐点的主语要收紧。** 论文给出 2012 拐点的逐字句是就**总样本**而言:"Beginning in 2012, depressive symptoms increased in the total sample by year through 2018, from 7.67 (SD = 3.85) in 2012 to 9.18 in 2018 (SD = 4.34)."。女生的涨幅更陡、更显著,但 2012 拐点本身不应仅归给女生。
22. **须补前段:** 女生是先 "decreased from 1991 to 2011" 再反转。
23. **利益冲突声明逐字:** "The authors report no conflicts of interest and have no financial relationships with commercial interests."

### 跨项构念边界(必须写,防止读者把三条曲线连成一条)

24. (a) YRBS 单题「持续悲伤/绝望,过去 12 个月」、(b)(c) NSDUH 的 MDE(DSM 诊断式访谈)、(d) MTF 四题自评 depressive symptoms 量表 —— **三者不是同一构念,不可互相换算或串成同一条曲线。**

---

## 修正记录(修正前→修正后)

| # | 修正前 | 修正后 |
|---|---|---|
| 1 | 2011 基线 36% 或 35%(待裁决) | **35.9%(95% CI 34.1–37.8),常引作 36%;35% 错误** |
| 2 | "highest level reported **in** the past decade" | "the highest level reported **over** the past decade" |
| 3 | CDC 2023 稿 URL p0213-yrbs-report.html | https://www.cdc.gov/media/releases/2023/p0213-yrbs.html |
| 4 | CDC 2024 稿 URL p0806-YRBS-report.html | https://www.cdc.gov/media/releases/2024/p0806-youth-mental-health.html |
| 5 | 「2021→2023 十年首降」= CDC 逐字 | CDC 从未用 first/decade 表述;「首降」是可由趋势表推出的**分析者推论**,须如此标注 |
| 6 | 下降读作全面反转 | 只见于全体、女生、西班牙裔;男生 29%→28% 未达显著;长趋势方向仍是 2013→2023 上升 |
| 7 | 2023 女 53%、全体 40%(当作精确值) | 一手精确值 女 **52.6%**、全体 **39.7%**、男 **27.7%**;53/40/28 是取整 |
| 8 | 漏掉 CDC 的 COVID 限定语 | 须补 "The 2021 data are drawn from a year when schooling was still substantially disrupted due to COVID." |
| 9 | 2011→2021→2023 一条序列 | 跨两份报告拼接;2023 版自身十年基线是 2013(女 39%);须标注口径 |
| 10 | SAMHSA 逐字 "estimates from this year should not be compared with previous years" | **该串在所指 PDF 中零命中**;换用 "Because of changes to data collection procedures and other methodological changes for 2021, estimates between 2021 and prior years should not be compared."(或另四条备选) |
| 11 | 只提 2021 一处断点 | **2020 与 2021 两处**官方断点 |
| 12 | 8.7%(2005)隐含为 SAMHSA 官方数 | 出自 Mojtabai, Olfson & Han, *Pediatrics* 2016;138(6):e20161878 的 NSDUH 二次分析,N=172,495 |
| 13 | 8.7%→20.1% 直线上升 | 2005–2011 为平台期(8.7/8.0/8.2/8.4/8.0/8.0/8.3);应写「2011/2012 前后起转折」 |
| 14 | (d) 女生 2012 起反转上升 | 2012 拐点的逐字句是就**总样本**而言(7.67→9.18);女生涨幅更陡但拐点不应仅归女生 |
| 15 | (d) N ≈ 126 万 | N = 1,260,159(精确值) |

**票间冲突与裁决:**
- **CDC 2024-08-06 是否存在 YRBS 新闻稿**:一票判定「2024-08-06 是报告发布日、非新闻稿日期,CDC 站内无该日 YRBS 新闻稿」,并把它列为出处不成立;另两票经 Wayback CDX 前缀检索**定位到实际新闻稿** https://www.cdc.gov/media/releases/2024/p0806-youth-mental-health.html,并逐字提取了 42%→40% / 57%→53% / 30%→27% 三组数字。
  **裁决:采后两票。** 第一票的负面证据源于按 `p0806-yrbs*` 型 URL 检索,而该稿的实际 slug 是 `youth-mental-health`,故其「不存在」结论是检索模式所致的假阴性。**成稿引 2024-08-06 稿时用 youth-mental-health 这个 URL 与标题。**
- **2011 基线的证据层级**:一票依 DSTR 2011–2021 报告图表取整值 36%;另一票回到 MMWR Surveill Summ 2012;61(SS-4) Table 21 取得 35.9% 及 95% CI。**裁决:采 MMWR 一手表(更硬),写作 35.9%(常引作 36%)。** 两者不冲突,后者是前者的未取整原值。

---

## 未回溯项

1. **是否存在另一份 SAMHSA 文件恰好含有原引语字符串 "estimates from this year should not be compared with previous years"**(例如 2021 NSDUH Annual National Report / Key Substance Use and Mental Health Indicators / Detailed Tables 封面提示)—— 三票的 WebSearch 配额均已耗尽(200/200),无法做全域字符串检索。**能确定的只是:论断所指定的那份 PDF 中该串命中数为 0。** 若正文坚持用该引语,须先补搜定位出处;否则按第 11 条替换。
2. **2015 年 NSDUH 问卷改版是否构成 12–17 岁 MDE 序列的第三处官方断点** —— 未从 SAMHSA 一手文件核实。所查的《2021 NSDUH Methodological Summary and Definitions》未覆盖该问题;SAMHSA 历年报告确曾连续呈现跨 2015 的青少年 MDE 趋势(暗示其认为可比)。**建议正文只主张 2020 / 2021 两处已核实的断点。**
3. **SAMHSA 官方自己发布的 2005 年 12–17 岁 MDE 百分比原文未取得**(2005 NSDUH National Findings 的候选 URL 均 404/移除)。8.7% 仅回溯到 Mojtabai et al. 2016 这一层同行评议二次分析。
4. **YRBS 各年百分比在 DSTR 中一律取整数呈现;女生 2015/2017/2019 三年的精确小数值未取得**(需 YRBS Explorer 或对应 MMWR Supplement 表格)。因此 42%→40%、57%→53% 的**幅度不宜再做二次精算**(如换算成相对下降百分比)。CDC 的显著性判定本身已核到(女生 decreased、男生 no change),方向性结论不受影响。
5. **全体 42%→40% 这 2 个百分点变化的置信区间与 p 值未逐项核对。** CDC 在 DSTR 中将其标为方向正确的双年变化,新闻稿未给 CI 或 p 值。
6. **cdc.gov 全站对本环境直连返回 403(WebFetch 与 curl 均是),所有 CDC 逐字均经 Wayback 存档取得。** MMWR/DSTR 内容另有 PMC 独立镜像交叉印证(MMWR Suppl 2024 经 PMC),但 **2023-02-13 与 2024-08-06 两份新闻稿仅有 Wayback 单一存档源**,未取得第二个独立镜像(archive.today 未尝试;Wayback CDX 期间多次 429/503 限流)。存档内容自洽且与 PDF 报告数字互相印证。
7. **反证检索覆盖不完整**:三票 WebSearch 配额均在会话开始前耗尽,未能系统检索针对上述四项的后续批评、再分析或勘误文献;「未发现勘误」仅基于所访问的一手页面本身。

---

## 证据分级

- **(a) YRBS 数值:多源证实。** 2011 值有 MMWR SS-4 原表(带 CI)+ DSTR 2011–2021 图表两条独立线;2023 值有 MMWR Suppl 2024;73(4)(经 PMC 独立镜像)+ DSTR 2013–2023 + 新闻稿三条线;重叠年份跨报告校验通过。
- **(a) 两份 CDC 新闻稿引语:单源已核。** 内容逐字确认,但仅有 Wayback 单一存档通道(cdc.gov 直连 403),未取得第二独立镜像。可用,须知其取证通道。
- **(a)「十年首降」措辞:未验证(作为 CDC 引语)/ 已核(作为数据序列推论)。** 不得引作 CDC 原话。
- **(b) NSDUH 断点:多源证实。** SAMHSA 方法学报告(直连 200 + Wayback 字节数一致,双源)+ NIMH 统计页自行转载 + SAMHSA 2021 Detailed Tables 页面,三处独立表述同一断点。**但原引语字符串本身:未验证 —— 三票全文检索零命中,不得使用。**
- **(b) 8.7%(2005):单源已核。** 回溯到 Mojtabai et al. 2016(PubMed/PMC 官方摘要),未回到 SAMHSA 一手表。
- **(c) 2021 MDE 四个数字:单源已核(官方权威源)。** NIMH 页面逐字对上,数据生产方即发布方;NIMH 同页主动披露不可比性,属对己不利的披露,可信度高。
- **(d) Keyes 2019:多源证实。** PubMed/PMC 官方摘要 + NCBI efetch 独立取得,书目、卷期页、N、四题恒定、period effect、estimate=1.15 全部对上;作者声明无利益冲突;未检出勘误或撤稿。
- **来源利益相关性总评:无一来源来自倡导团体或产业方。** CDC/SAMHSA/NIMH 为联邦统计机构,存在「强调议题严重性」的一般性机构倾向,但本组数字均可回溯到技术报告表格层级,且 SAMHSA 主动公布了不利于连年比较的断点声明。反向证据主要落在「口径」而非「数值」—— 即 CDC 自己把十年窗口从 2011–2021 改为 2013–2023,以及 SAMHSA/NIMH 明确禁止 2021 跨年连线,两者都指向论断里的**拼接式叙事**而非算错数。


---

# C15 最终判决:CORRECTED(3/3 票;其中 (b) 后半与 (c) 出处归属为 REFUTED)

论断组:硬结局与混杂 —— (a) 10–14 岁自杀率 0.9(2007)→2.9(2018) 及「起点早于 2012」;(b) 2022–2024 转降、主要男性驱动;(c) 枪支 +59% vs 非枪支 +29%。
三票一致:**(a) 逐字全成立**;**(b) 有两处被一手数据推翻**;**(c) 的 59%/29% 数对在任何版本的 Everytown 报告中都不存在,三票均未定位到原始出处 —— 不得承重。**

---

## 锁定口径(成稿必须用)

### (a) NCHS 10–14 岁自杀率 —— 逐字成立,补三处限定

1. **核心逐字(NCHS Data Brief No. 471,2023-06,Curtin SC & Garnett MF,《Suicide and Homicide Death Rates Among Youth and Young Adults Aged 10–24: United States, 2001–2021》,DOI 10.15620/cdc:128423):**
   > "The suicide rate for people aged 10–14 declined from 2001 through 2007 (from 1.3 deaths per 100,000 to 0.9), tripled from 2007 through 2018 (from 0.9 to 2.9), and then did not change significantly through 2021."
   (Key findings 框重复同一表述。0.9→2.9 实为 3.22 倍,NCHS 用词是 tripled。)

2. **分子分母(db471 备份表 db471-tables.pdf,10–14 岁,人数/率):** 2001 = 272 / 1.3;2007 = 180 / 0.9;2017 = 517 / 2.5;2018 = 596 / 2.9;2019 = 534 / 2.6;2020 = 581 / 2.8;2021 = 598 / 2.8。10–24 岁合计:2010 = 4,867 / 7.6;2019 = 6,488 / 10.2;2021 = 7,126 / 11.0。

3. **Joinpoint 分段脚注(图 2)与正文分段并存,不可混用:**
   > "Significant decreasing trend from 2001–2007, then significant increasing trend from 2007–2021 (p < 0.05)"
   即模型只在 2007 处设了一个拐点、把 2007–2021 当作一整段上升;**2018 不是拟合出的拐点**,「2018→2021 无显著变化」是成对比较表述。

4. **方法学限定(决定「2007 起点」能证明什么):** db471 的 joinpoint 设置为 "a maximum of two joinpoints were searched" + "as few as three observed time points in the beginning, ending, and middle line segments"。**该模型在 10–14 岁的 2007–2021 段内不具备再切一个 2012 拐点的自由度**,故 db471 只能证明「起点是 2007」,不能证明「2012 没有加速」。db541 亦自述 "Reported significant patterns in trend analyses may differ from previous reports that use a different time period, particularly with a different start and end year."

5. **「起点 2007 早于 2012」必须限定年龄段 —— 三票一致的关键修正。**
   - 10–14 岁与 10–24 岁总体:成立。
   - 15–19 岁:2001–2009 无显著趋势,2009–2017 显著上升(+57%),2017–2021 无显著趋势。
   - **20–24 岁:全期上升,但 db471 自己写明 2012–2021 年均 +4%,快于 2001–2012 的年均 +1%** —— 即 20–24 岁的加速拐点恰好就在 2012。
   用「2007 早于 2012」去整体否定 2012 叙事,会漏掉 db471 写在纸面上的这条。

6. **10–14 岁逐年率(Health, United States 系列表,data.cdc.gov 9j2v-jamp):** 2001=1.3, 2002=1.2, 2003=1.1, 2004=1.3, 2005=1.3, 2006=1.0, **2007=0.9**, 2008=1.0, 2009=1.3, 2010=1.3, 2011=1.4, **2012=1.5**, 2013=1.9, 2014=2.1, 2015=2.0, 2016=2.1, 2017=2.5, **2018=2.9**。
   → **3.22 倍中约 1.9 倍发生在 2012 之后**(0.9→1.5 是 1.67x,1.5→2.9 是 1.93x)。「起点 2007」是 joinpoint 起点,不等于「主要涨幅在 2012 前」。

7. **2007 起点的独立二次确认:** NCHS Data Brief No. 509(2024-09,Garnett & Curtin,《Suicide Mortality in the United States, 2002–2022》)图 3(男性)10–14 岁脚注:"No statistically significant trend from 2002 to 2007; significant increasing trend from 2007 to 2020 (p < 0.05)" —— 不同起始年、不同报告,仍落在 2007。

### (b) 2021→2024 —— 两处被推翻,一处收紧

8. **2021→2022 是唯一被官方显著性检验支持的青少年下降。**
   - 计数:10–14 岁 598(2021)→ 493(2022)→ 481(2023)。493 见于 NVSR Vol.73 No.10《Deaths: Leading Causes for 2022》(Curtin, Tejada-Vera & Bastian, 2024-12)10–14 岁栏:Intentional self-harm (*U03, X60–X84, Y87.0) = 493 例,占该年龄段全死因 3,672 例的 13.4%,列第 2 位死因;男 303、女 190(303+190=493 自洽)。
   - **598→493 = −17.6%,是计数口径;对应粗率是 2.8→2.4,约 −14%。两者因分母人口变动而不同,引用时必须写明是哪个口径。**(VSRR-34 临时版列的率为 2.8→2.3、−18%。)
   - 2023 终版计数(NVSR Vol.74 No.10《Deaths: Leading Causes for 2023》,2025-09):10–14 岁 481 / 2.3(男 268 / 2.5,女 213 / 2.1);15–19 岁 2,156 / 9.8(男 1,645 / 14.6,女 511 / 4.7);20–24 岁 3,780 / 17.3(男 3,115 / 28.0,女 665 / 6.2)。与 DQS 数据集完全吻合。

9. **完整终版率序列(NCHS DQS 数据集 w26f-tf3h,源 CDC WONDER / NVSS Mortality File,粗率 per 100,000):**
   | 年龄 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
   |---|---|---|---|---|---|---|---|
   | 10–14 | 2.9 | 2.6 | 2.8 | 2.8 | 2.4 | 2.3 | **2.3** |
   | 15–19 | 11.4 | 10.5 | 10.6 | 10.9 | 10.0 | 9.8 | **9.4** |
   | 20–24 | 17.4 | 17.3 | 17.8 | 19.4 | 17.1 | 17.3 | **17.0** |
   分性别 2023→2024:男 10–14 2.5→2.4;女 10–14 2.1→2.3;男 15–19 14.6→13.3;女 15–19 4.7→5.4;男 20–24 28.0→27.1;女 20–24 6.2→6.4。

10. **「2023→2024 三个年龄段均降」—— REFUTED。**
    - 10–14 岁 **2.3→2.3,完全持平**(两年 95% CI 均为 2.1–2.5);计数口径 482→481。
    - 15–19 岁 9.8→9.4,z ≈ −1.4,**不显著**。
    - 20–24 岁 17.3→17.0,z ≈ −0.75~−0.8,**不显著**。
    正确表述:**「仅 15–19 岁点估计明显下降,10–14 与 20–24 持平;三组的年度变化在统计上均不可区分于零(合计口径)。」**

11. **「女性统计上无变化」—— REFUTED,方向相反。**
    2023→2024 女性三个年龄段点估计**全部上行**:10–14 岁 2.1→2.3;15–19 岁 **4.7(4.3–5.2)→5.4(4.9–5.8)**;20–24 岁 6.2→6.4。其中 **15–19 岁女性是六个性别×年龄格中唯一的显著上升**(z ≈ +2.2~+2.5,p ≈ 0.014–0.03)。

12. **「主要男性驱动」—— HOLDS,但须收紧。**
    唯一统计显著的下降是 **15–19 岁男性 14.6→13.3(z ≈ −2.6,p ≈ 0.009)**;男性 10–14(2.5→2.4)与 20–24(28.0→27.1)变化不显著。
    **准确表述:「2023→2024 六格中唯一显著下降在 15–19 岁男性,唯一显著上升在 15–19 岁女性,其余四格持平。」** 而非「普遍下降、男性驱动」。

13. **「2022–2024 持续转降」的时间窗表述须改。** NCHS 官方检验(Data Brief No. 541,2025-09,Garnett & Zehner,《Changes in Suicide Rates in the United States From 2022 to 2023》,终版数据)逐字:
    > 女性:"Between 2022 and 2023, the suicide rate for females age 75 and older increased by 10.9%… **Changes were not significant for any other age group**"
    > 男性:"From 2022 to 2023, the suicide rate for males age 75 and older decreased by 7.3%… **Changes were not significant for any other age group.**"
    且 20–24 岁 2023 还回升(17.1→17.3)。
    **正确表述:「2021→2022 有一次显著下降,之后 2022→2024 基本走平、无显著年度变化。」**

14. **性别不对称的官方支持存在,但窗口不同(不可挪用):** NCHS Data Brief No. 509 逐字:"Between 2020 and 2022, rates decreased for males ages 10–14 (3.6 deaths per 100,000 population to 2.8) and 15–24 (22.4 to 21.1)";"For females ages 10–14 and 15–24, rates did not change significantly between 2018 and 2022."
    → **「男性驱动、女性无显著变化」这一框架在 2020→2022 窗口有官方支持,但不能挪用到 2023→2024。**

15. **2024 是终版数据。** NCHS Data Brief No. 548(2026-01,Xu, Murphy, Kochanek & Arias,《Mortality in the United States, 2024》):"This report presents final 2024 U.S. mortality data…";全年龄年龄调整自杀率 2023 = 14.1 → 2024 = 13.7(−2.8%)。
16. **临时数据的一般性告诫(备用):** VSRR Report No. 40(2025-09):"Deaths from external causes of injury, such as suicide and drug overdose, took 6–9 months to reach similar levels of completeness";"For suicides, an average of 33.4% of records were available by 4 weeks, 77.6% by 8 weeks, and 92.7% by 16 weeks."

### (c) 枪支 vs 非枪支 —— 数字与出处双错

17. **「枪支 +59%(2010–2019)」不存在于 Everytown 任何版本 —— 三票一致。** 必须替换为:
    - **Everytown 自报口径:+42%。** 2021-03-05 版(Wayback 20210412002224)stat-block 逐字:
      > "The rate of firearm suicide among young people has increased 42 percent over the past decade."
      脚注:"CDC, WISQARS Fatal Injury Reports, Ages 10-24, Percent Change: 2010 to 2019."
      同页分年龄柱图(value axis 明写 "% Change from 2010 to 2019"):10–14 **+114%**、15–24 +40%、25–34 +21%、35–44 +8%、45–54 −3%、55–64 +8%、65+ +11%。
    - **独立重算(NVSS 终版,一手):**《Deaths: Final Data for 2010》(NVSR 61-4)表 10 与《Deaths: Final Data for 2019》(NVSR 70-8)表 6,5–24 岁合并:枪支自杀 2,127 → 2,972(**+39.7%** 计数,折率约 **+40.6%**);非枪支 2,747 → 3,528(**+28.4%** 计数,折率约 **+29.3%**);全口径 4,874 → 6,500(+33.4%),与 db471 实测的 10–24 岁 7.6→10.2(+34.2%)相符。
    - **另一条独立算路(同样落在 +42%/+28%):** 2010 年枪支占青少年自杀约 43.7%(CDC/NCHS Injury Mortality 数据集 nt65-c7a7:<15 岁 Firearm 81 死、15–24 岁 Firearm 2,046 死,合计 2,127 / 全口径 4,874),与 db471 的 10–24 岁总率 7.6→10.2 联立,得枪支率 3.32→4.72(**+42%**)、非枪支率 4.28→5.48(**+28%**)。

18. **「非枪支 +29%」数值近似正确(约 +28~29%),但它不是 Everytown 的表述。** Everytown 该报告**从不发布非枪支对照项**,该数只能由残差推算。三票均确认。

19. **倍数必须改:枪支涨得比非枪支快的方向成立,但倍差约 1.4–1.5 倍(42% vs 28%),不是 59:29 所暗示的约 2 倍。**

20. **Everytown 的口径是滚动窗口,不同版本给出不同数,引用必须带起止年 + 年龄段:**
    - 2021-03-05 版:42%(10–24 岁,2010 vs 2019 粗率)
    - 2022-07-01 存档版:"the rate of firearm suicide among those 10 to 24 years old has increased significantly (53 percent) over the past decade",脚注 "Rate percentage change: 2011 to 2020";10–14 岁 "the rate has increased a disturbing 146 percent from 2011 to 2020"
    - 现行版(更名《Too Many, Too Soon: Youth Firearm Suicide in the United States》,页面标注 6.2.2022 发布 / Last Updated 8.25.2025):"longer-term trends show the rate of firearm suicide among people ages 10 to 24 has increased significantly (41 percent) in the past decade",脚注 "Based on percentage change in crude rates: 2014 vs. 2023. Ages 10–24";摘要作 "increased over 40 percent"
    - 现行版另载:"After reaching a nearly 30-year high in 2021, the youth firearm suicide rate fell by 12 percent in 2022, and rose by 2 percent in 2023"(2021 = 5.93/10万,2022 = 5.24,2023 = 5.35;1994 record high 6.36);"From 2019 to 2023 … a 14 percent increase in the youth firearm suicide rate, even as overall suicide rates for young people fell"(4.68→5.35;总体自杀率 10.22→9.91)

21. **基线选择是关键混杂,必须写。** 同一套 CDC 数据下,15–24 岁 1999→2016 枪支自杀率仅 **+3%**(5.99→6.17),而非枪支 **+70%**(4.10→6.99);15–24 岁枪支自杀率在 2006–2007 触底(4.62 / 4.40)。**从 2010 起算等于从谷底附近起算,系统性放大枪支涨幅。**「枪支驱动」这一说法对起始年高度敏感。

22. **年龄段也极度敏感,引用必须写明:** NCHS Injury Mortality(vc9m-u7tv,1999–2016)15–24 岁 2010→2016 枪支率 +31.5% / 非枪支 +19.3%(比值 1.6);<15 岁 枪支 +98% / 非枪支 +47%。用 10–24 合并会被 15–24 段稀释,用 10–14 段则枪支涨幅翻倍。

23. **利益相关声明必须带:** Everytown for Gun Safety (Support Fund) 是**控枪倡导组织**,其数字为自行分析 CDC WONDER/WISQARS、非同行评议;「过去十年」为自选滚动窗口(2011–2020 / 2014–2023 / 2019–2023 三个版本先后给出 53% / 41% / 14% 三个数),属典型基线可选性风险。
    **但须公允记录:本例中偏差方向与利益相关预期相反 —— Everytown 公布的是较保守的 +42%,与 NVSS 终版独立重算的 +40.6% 吻合;被夸大到 +59% 的版本并非出自 Everytown。**
    另注:AFSP 与 JED 均为倡导型非营利且已公开宣布合并意向,二者转述不能算相互独立的证据源。

---

## 修正记录(修正前→修正后)

| # | 修正前 | 修正后 |
|---|---|---|
| 1 | (a)「起点 2007 早于 2012」可整体否定 2012 叙事 | 只对 10–14 与 10–24 总体成立;**20–24 岁 db471 自己写明 2012–2021 年均 +4% 快于 2001–2012 的 +1%**;15–19 岁上升段是 2009–2017 |
| 2 | (a) 0.9→2.9 主要涨幅在 2012 前 | 逐年看 0.9(2007)→1.5(2012)→2.9(2018),**3.22 倍里约 1.9 倍发生在 2012 之后** |
| 3 | (a) 2018 是拐点 | 2018 **不是** joinpoint 拟合出的拐点;模型只在 2007 设一个拐点,且最多搜索两个拐点、每段至少三点 —— 无自由度再切 2012 |
| 4 | (b) 2021→2022 降 −18% | −17.6% 是**计数**口径(598→493);**率**口径为 2.8→2.4 约 −14%。须标明用哪个 |
| 5 | (b) 2023→2024 三个年龄段均降 | **REFUTED**。10–14 岁 2.3→2.3 完全持平;15–19(9.8→9.4)与 20–24(17.3→17.0)点估计降但不显著 |
| 6 | (b) 女性统计上无变化 | **REFUTED,方向相反**。女性三段点估计全部上行;**15–19 岁女性 4.7→5.4 是唯一显著上升**(z≈2.2–2.5) |
| 7 | (b) 主要男性驱动(普遍下降) | 收紧为:**唯一显著下降在 15–19 岁男性(14.6→13.3, z≈−2.6);其余五格不显著** |
| 8 | (b) 2022–2024 持续转降 | 真正的显著转折是 **2021→2022 一次**;NCHS db541 官方判定 2022→2023 青少年各组「Changes were not significant for any other age group」;20–24 岁 2023 还回升 |
| 9 | (c) 枪支 2010–2019 **+59%** | **+40~42%**(Everytown 自报 42%;NVSS 终版独立重算 +40.6%) |
| 10 | (c)「+59% vs +29%(Everytown 汇总)」 | **该配对表述在 Everytown 任何版本中都不存在**;Everytown 从不发布非枪支对照项。+29% 数值本身近似正确(独立算得 +28~29%)但非其表述 |
| 11 | (c) 枪支涨幅约为非枪支 2 倍 | 约 **1.4–1.5 倍**(42% vs 28%) |
| 12 | (c) 用 2010–2019 窗口 | Everytown 现行版已改为 2014 vs 2023(41%);引用任何版本都必须带起止年 + 年龄段 |

**票间冲突与裁决:**
- **2022 年 10–14 岁死亡数 493 是临时值还是终版值。** 两票判定 493 是 provisional(源自 VSRR-34),并由 DQS 终版率 2.4 × Census 人口反推终版应为约 505–519 例,主张改写为「−14%(终版)」;第三票取得 **NVSR Vol.73 No.10《Deaths: Leading Causes for 2022》**(终版年度死因报告)10–14 岁栏,逐字读到 493 例(男 303 + 女 190 = 493,内部自洽),并进一步用 NVSR 74-10 取得 2023 = 481 与 DQS 完全吻合,证明 DQS 用的就是终版数据。
  **裁决:采第三票 —— 493 有终版一手表格支持,不应改写为推算的 509。** 但残留一处未解的算术不一致:493 / 21,196,255 = 2.33,应四舍五入为 2.3,而 DQS 终版率列的是 2.4(NVSR 与 DQS 可能用不同 vintage 的人口分母)。**成稿建议:引计数用 598→493(NVSR 73-10 终版),引率用 2.8→2.4(DQS);不要把两者相除或据一方反推另一方。** 见未回溯项 1。
- **2023→2024 女性 15–19 上升的显著性强度。** 三票的 z 值分别为 +2.16、未算、+2.5(均用 DQS 公布的 SE/CI 自行做两样本 z 检验)。**裁决:方向与显著性一致,均越过 α=0.05;但因紧邻临界且非 NCHS 官方检验,成稿宜写「统计显著的上升(自算 z≈2.2–2.5,非 NCHS 官方检验)」。**
- **Everytown 2021 版 10–14 岁数值:一票读到 +114%(2010→2019),另一票读到 2022 版 +146%(2011→2020)。** 二者不冲突,分属两个版本/窗口,均已收进锁定口径第 20 条。

---

## 未回溯项

1. **2022 年 10–14 岁自杀死亡的率与计数之间的算术不一致未解:** 493(NVSR 73-10 终版计数)与 DQS 终版率 2.4 对不上(493/21.2M = 2.33 → 应为 2.3)。两票用 Census PEP 分母反推终版应为约 498–519 例。CDC WONDER / WISQARS 在三票的环境中均 403(POST 型代理亦被拒),无法用 UCD-ICD-10、ICD U03/X60–X84/Y87.0、Five-Year Age Groups=10–14 直接复核。**标记「未回溯」:不得用 493 与 2.4 做互相推算。**
2. **NCHS 尚未发布覆盖 2023→2024 的官方显著性检验报告**(最新为 db541,止于 2023;2026 年 Data Brief 目录中无对应条目;VSRR 系列在 No.34 之后未再出专门的 provisional suicide 报告)。**本组所有 2023 vs 2024 的显著/不显著判定均为分析者用 DQS 公布的 SE 与 95% CI 自行做的两样本 z 检验(方法与 NCHS 一致,α=0.05),非 NCHS 官方结论。** 若 NCHS 后续用 joinpoint 或不同方差假设,个别结论(尤其女性 15–19 的 z≈2.2)可能被判为边缘。**唯一不依赖任何检验假设的是「10–14 岁 2.3→2.3 无下降」。**
3. **「+59%」的原始出处始终未定位 —— 三票全部失败,标记「未回溯,不得承重或须标未验证」。** 已排除:Everytown 2020/2021/2022/现行四个版本全文(grep "59 percent"/"59%" 零命中)、其 gun-suicide 议题页、youth-firearm-suicide 图表页、另一份《Firearm Suicide in the United States》报告。已测试的替代窗口也都对不上:2010→2021(5–24 岁)枪支 +79.9% / 非枪支 +20.5%;2010→2016(15–24 岁)枪支 +31.5%。**没有任何合理的年龄段/时间窗组合能同时产出 (+59%, +29%) 这一对数**,而 (+40~42%, +29%) 在 2010–2019 窗口下内部自洽。三票 WebSearch 配额均已耗尽(200/200),无法穷尽排查。**建议:直接改用可核的一手对(db471 全口径 + WISQARS/NVSS 枪支口径),并自报窗口与年龄段。**
4. **2017–2019 年分机制(枪支/非枪支)青少年自杀计数无法从数据集直接取得:** NCHS Injury Mortality 数据集止于 2016,WISQARS 与 WONDER 不可达。2010→2019 的枪支/非枪支拆分是用 NVSR 终版表(61-4 / 70-8)重算得出,属一手但为 5–24 岁口径(非 10–24)。
5. **2024 年各年龄组的自杀死亡计数未取到一手值。** 终版 2024 数据已发布(db548),但按年龄组分列计数的《Deaths: Leading Causes for 2024》尚未出版(NVSR 目录最新为 75-3);2024 各格计数为由 DQS 率 × 反推人口得出的近似值,仅用于辅助显著性判断。
6. **10–14 岁自杀「认定标准/编码实践随时间变化」这一潜在混杂未追查**(例如低龄自杀意图判定尺度是否在 2007 后放宽)。db471/db509/db541 均只声明 ICD-10 编码不变(U03, X60–X84, Y87.0),未讨论认定实践漂移。这对「2007→2018 三倍」的解释力度有影响,但无一手证据可下结论。
7. **Everytown 窗口选择偏差的量级未评估。** 已核实其数字与 CDC 底数一致(同页 "Deaths in 2019" 图给出 Suicide = 6,488,与 db471 备份表完全一致),但未量化其起始年选择(2010 恰为青少年枪支自杀相对低点)带来的偏差。
8. **claim 提及的「Jed/AFSP 转述」未能核到对应文本**(afsp.org 统计页为 JS 渲染、代理只返回骨架;jedfoundation.org 统计页无 2023→2024 分性别表述)。因此无法判断该说法是这些机构的原话还是转述走样。
9. **取证通道说明(可复现性):** 三票环境中 www.cdc.gov / wonder.cdc.gov / stacks.cdc.gov 一律 403,所有 NCHS 出版物经 Internet Archive 取得(db471.pdf 在 2023-06 至 2025-01 的多次快照中 CDX 摘要恒为 G5Y3GQDDR5AGFSZVMIDHKSKWR25LSSF4,可作完整性校验);数值序列走 CDC 自营活站 data.cdc.gov 的 Socrata API(非存档、非二手),与存档 PDF 互为独立通道。WebSearch 配额三票均已耗尽,DuckDuckGo 触发人机验证(按规定未尝试破解),故未能做开放式反证检索(如是否有其他机构发布过 +59% 的口径、有无对 db471 的勘误)。已确认 NCHS 未对 db471 发布勘误,其后续 db509 与 db541 内容与之一致而非相互推翻。

---

## 证据分级

- **(a) NCHS 10–14 岁趋势:多源证实。** db471 正文 + Key findings + 图 2 脚注 + db471 备份表 + Health US 逐年表(data.cdc.gov 9j2v-jamp,独立通道)+ db509 不同起始年的二次确认,五条线互证。政府法定统计,无倡导立场,无勘误。**可承重。**
- **(b) 终版率序列本身:多源证实。** DQS(w26f-tf3h)与 NVSR 73-10 / 74-10 的年度死因报告逐格吻合,且 db548 确认 2024 为终版。**可承重。**
- **(b) 2023→2024 的显著性判定:方向存争 / 单源已核(分析者自算)。** 三票用相同方法独立得出一致结论,但**没有任何 NCHS 官方检验覆盖该年度对**。成稿须标注「自算 z 检验,非官方判定」。「10–14 岁 2.3→2.3 无下降」不依赖检验,可直接承重。
- **(b)「2020→2022 男性驱动、女性无显著变化」:多源证实(但仅限该窗口)。** db509 官方逐字支持。挪用到 2023→2024 即失效。
- **(c) 「+59% vs +29%」:未验证 —— 不得承重。** 三票均未定位到任何原始出处,且穷尽了替代窗口/年龄段组合仍无法复现该数对。
- **(c) 替换数字(枪支 +40~42% / 非枪支 +28~29%,2010–2019):多源证实。** Everytown 自报(+42%)、NVSS 终版 NVSR 61-4/70-8 独立重算(+40.6%/+29.3%)、CDC Injury Mortality 数据集反推(+42%/+28%)三条独立路径收敛。
- **(c) Everytown 作为来源:厂商口径(利益相关方自述)。** 控枪倡导组织自行分析、非同行评议、滚动窗口自选。**须标注立场;但本例其数字经独立一手重算证实,偏差方向与其利益预期相反。** 引用时优先用 NVSS/db471 一手对,把 Everytown 仅作为「该说法的流通出处」提及。
- **(c) 基线敏感性(1999 起算枪支仅 +3% vs 非枪支 +70%):单源已核。** 来自 NCHS Injury Mortality 数据集(官方一手),仅一票核到,但数据源可公开复现。建议在正文中作为「结论对起始年高度敏感」的证据保留。


---

# C16 最终判决:CORRECTED(3/3 票;其中 (c) 与 (d) 的表述方向为 REFUTED)

论断组:测量伪影双向 —— (a) Corredor-Waldron & Currie 新泽西;(b) ICD-10 切换跳变;(c) 匿名调查免疫伪影;(d) 挪威 Ungdata 测量不变性。
三票一致:**(a) 核心逐字成立但跳点年份与数据来源口径错**;**(b) 引语漏关键限定语、正负号未经一手确认、两条证据非独立**;**(c) 原表述被 SAMHSA 一手反驳,必须收窄**;**(d) 「校正后仍在」说反了 —— 该研究是检验后发现不变性成立。**

---

## 锁定口径(成稿必须用)

### (a) Corredor-Waldron & Currie —— 新泽西住院/急诊

1. **出处:** Corredor-Waldron A, Currie J. "To What Extent Are Trends in Teen Mental Health Driven by Changes in Reporting? The Example of Suicide-Related Hospital Visits." *Journal of Human Resources* 2024;**59(S):S14–S40**,DOI 10.3368/jhr.0423-12854R1。工作论文版:NBER WP w31493(2023-07)。资助:NOMIS Foundation 与普林斯顿 Center for Health and Wellbeing;作者声明无利益冲突。
2. **摘要逐字(三票独立核到,一致):**
   > "Using data on all hospital visits in New Jersey from 2008-2019, we investigate two inflection points in adolescent suicide-related visits and show that **a rise in 2012** followed changes in screening recommendations, while **a sharp rise in 2016-2017** followed changes in the coding of suicidal ideation. Rates of other suicidal behaviors including self-harm, attempted suicides, and completed suicides were **essentially flat** over this period."
3. **跳点年份必须改:数据上的折点是 2012 与 2016–2017;2011 / 2016-10 是被指认的制度诱因日期,不是折点。** 正文另有 "suicide-related visits clearly tick up after 2011, and again after 2016" 的表述并存,但引用时不得把政策年当成折点年。
4. **筛查建议的年份归属必须改:USPSTF 对 12–18 岁抑郁筛查的 B 级建议发布于 2009-03-15,不是 2011。**
   - JHR 正文逐字:"In 2009, the USPSTF recommended that providers screen adolescents 12–18 for depression. However, insurers were not required to pay for these services until 2011"
   - USPSTF 原文逐字:"The USPSTF recommends screening of adolescents (12-18 years of age) for major depressive disorder (MDD) when systems are in place to ensure accurate diagnosis, psychotherapy (cognitive-behavioral or interpersonal), and follow-up"(7–11 岁为 I 级,证据不足)
   - 另一条制度线:2011 年 8 月 Women's Preventive Services Guidelines(针对 12 岁以上女性/女孩每年抑郁筛查),保险覆盖实际生效于 "plan years starting on or after August 1, 2012"
5. **2016-10「编码指令」的性质须精确化:** 2015 年 10 月启用的 ICD-10 对 R40–R46(含自杀意念)设了 **Exclude 1** 注记,禁止与 F01–F99 主诊断同时编码;Cooperating Parties 承认此为错误,**2016 年 10 月改为 Exclude 2**,构成 180 度反转。JHR 称此为 "the first time that clinicians were specifically directed to record suicidal ideation as a secondary diagnosis in cases with a primary diagnosis of a mental health condition";并称 "clinicians were now actively encouraged to include symptoms such as suicidal ideation as secondary diagnoses when present with a primary diagnosis of mental illness"。
6. **人群与数据口径:** 10–18 岁(**不是 12–17**),新泽西全州住院出院记录 + 急诊就诊记录,2008–2019。编码:ICD-9 用 V62.84 + E950-E959;ICD-10 用 R45.851、T14.91、T36.xx2-T50.xx2、T51.xx2-T65.xx2、X71-X83。
7. **量化(逐字):**
   > "Between 2014/15 and 2018/19 the number of visits with a suicide-related code grew by 50 percent from 50.3 per 10,000 teens to 75.6 per 10,000 teens."
   > "the bulk of this increase, **24.9 out of 25.3 visits, was due to an increase in diagnoses of suicidal ideation, and 18.5 of these were secondary diagnoses**"
   > "The increase in suicidal behaviors is entirely accounted for by increases in suicidal ideation as a secondary diagnosis in teens with other mental health disorders."
   更早一段:2009–2010 → 2014–2015 自杀相关就诊 +14/万,"with all of that increase accounted for by an increase in suicidal ideation"。
   **精确化:出现趋势断裂的是「作为次要诊断的」自杀意念;SI 作为主要诊断只是 "trend[s] upwards gently and smoothly"。**
8. **"essentially flat" 的适用范围要分层:**
   - 摘要级逐字成立:"Rates of other suicidal behaviors, including self-harm, attempted suicides, and completed suicides were essentially flat over this period."
   - 正文对自伤/未遂:"the trend in self-injury and intentional self-harm, which includes attempted suicide, is essentially flat";"no significant increase in self-injury, intentional self-harm, or suicide attempts ... after 2015 or in the following years"
   - **但对完成自杀,正文措辞更弱:** "Completed suicides among teens in New Jersey **do not show a clear trend** over this period",并承认 "Those in the northeast region as a whole show some upward movement between 2015 and 2017"。
9. **完成自杀不来自医院数据。** 来自另一来源(New Jersey Department of Families and Children 2016 生命统计),两条序列量纲差异巨大(2014 年 2.9/10万 vs 约 431/10万 就诊),论文将二者各自归一化到 2008=1 才作比较。
10. **外推限制(作者自陈,必须带):** 脚注 1 —— "**youth suicides rose nationally but not in New Jersey**";NJ 枪支自杀排第 48 位、属全美青少年自杀率最低的五个州之一;作者称 "regionally specific factors are driving much of the overall increase in teen suicides"。
    **因此「自杀完成率 essentially flat」是新泽西的事实,不能用来论证全国自杀上升是伪影;作者只主张「报告量的上升在全国是类似的」。**
11. **作者本人的解读限定(引用时应保留):**
    > "These results should not be interpreted in a way that casts doubt on the seriousness of the youth mental health crisis."
    并指出高诊断率可能是好事 —— "may be a positive rather than a negative development if it means that more children in crisis are being diagnosed and treated"。
12. **NJ 数据中 ICD-10 采用本身未产生跳变:** "there was no significant rise in the use of suicide-related diagnoses between 2015 and 2016" —— 跳变发生在 2016-10 指令修订之后。**这意味着 (a) 与 (b) 讲的是两个应当分开处理的事件。**

### (b) ICD-10 切换的跳变 —— 三处必改

13. **Acad Pediatr 2026 出处与逐字:** Ryan TC, Angerhofer JE, Stewart C, Rossom RC, Harry ML, Ahmedani BK, Lynch FL, Beck A, Owen-Smith A, Daida YG, Coleman KJ, Penfold RB. "Impact of the Transition from ICD9-CM to ICD10-CM on Measuring Rates of Child and Adolescent Self-harm in Nine Health Systems." *Academic Pediatrics* 2026 Apr 17:103327,DOI 10.1016/j.acap.2026.103327,PMID 42002139。
    > 方法:"interrupted time series (ITS) analyses on monthly rates of medically attended deliberate self-harm in the **15 months prior to and 15 months following** the transition to ICD10 in October 2015 across nine health systems ... Separate models were estimated for youths aged 6-11 years and youths aged 12-17 years"
    > 结果:"There was a 0.18 per 100,000 youths per month (slope change) in the 6-11 age group. There was an **immediate 38.5 per 100,000 youths change** in medically attended deliberate self-harm and a **sustained 6.5 per 100,000 per month (slope) change** in the 12-17 age group."
14. **正负号在一手摘要中并未标明 —— 三票一致。** 原文只写 "change",**无正负号、无置信区间、无 p 值**。「+38.5」「+6.5」的正号属机制推断(undetermined intent 被重新归入 intentional self-harm)与引用综述方向的反推,**未经一手确认**。成稿应去掉「+」或明确标注方向未在摘要中给出。
15. **6–11 岁组必须一并报:仅有斜率变化 0.18/10万/月、无即时跳变。** 效应集中在 12–17 岁,论断只引 12–17 岁是恰当的,但不报 6–11 岁会让读者误以为全龄段跳变。
16. **窗口长度必须写:ITS 窗口仅为切换前后各 15 个月。** 窗口短会削弱把水平跳变与既有趋势分离的能力;且 "6.5/10万/月" 只在该 30 个月窗口内成立(若外推等于 78/10万/年,15 个月累计即约 +97/10万),**不可当作长期稳定斜率参数**。
17. **Psychiatric Services 2017 引语必须补回关键限定语 "of intent":**
    Stewart C, Crawford PM, Simon GE. "Changes in Coding of Suicide Attempts or Self-Harm With Transition From ICD-9 to ICD-10." *Psychiatr Serv.* 2017 Mar 1;**68(3):215**,DOI 10.1176/appi.ps.201600450,PMID 27903145。
    > "Marked changes in coding of **intent** for injuries and poisonings during the fall of 2015 almost certainly represent artifacts of coding changes rather than true changes in suicidal behavior."
    **其所指是 self-inflicted 与 undetermined-intent 之间的意图归类互换,不是自伤总量。**
    同文其余关键句:"We used data from ten health systems in the Mental Health Research Network (MHRN)";"Diagnoses of self-inflicted injury or poisoning appeared to increase abruptly with the coding transition, and this pattern was consistent across health systems";"Diagnoses of injury or poisoning of undetermined intent appeared to decrease with the coding transition, but this pattern varied considerably across health care systems"。
    **体裁与口径限定:** 一页 Datapoints 专栏(PubMed/Europe PMC 均标 "No abstract available"),**十个** MHRN 系统的**全体参保人**(非仅青少年),单位为**每万参保人**,仅描述性判断("appeared to increase"),**无正式统计检验**。
18. **方向性修正 —— 不可读作单向「虚增」(三票一致的核心):**
    JHR 论文自己的转述逐字:
    > "The adoption of the ICD-10 in October 2015 has been the focus of previous research which showed that it increased the number of injury and poisoning visits coded as self-harm and decreased the number of visits with 'undetermined intent.' **The net result that the total number of visits involving intentional self-harm remained largely unchanged** around the October 2015 adoption point (Stewart et al., 2017, 2019; Zima et al., 2020)."
    后续文献进一步把它读作**测准度改善**而非虚增:
    > Sentinel System 2023(montelukast 分析):"The increased detection of self-harm outcomes with ICD-10-CM coding compared to ICD-9-CM was described by Stewart et al. as **better ascertainment** of intentional self-harm, rather than an actual change in incidence of suicidal behavior"
    > 2025 rapid review(Accuracy of Suicidal Behaviors in Administrative Data, 2000-2024):"Stewart et al found an increase in nonfatal self-harm events in the period immediately after adoption of ICD-10-CM across 10 health systems in the United States."
    **即:伪影在切换前的低估一侧,+38.5 大部分是重新归类,不能等同于「真实率没变但报告虚增」。**
19. **两条证据非独立,不能并列为交叉验证:** Christine Stewart 同时是 PS 2017 与 Acad Pediatr 2026 两篇的作者;均出自 Mental Health Research Network / Kaiser Permanente 体系(2017 为 10 个系统,2026 为 9 个,高度重叠)。作者机构:UW / KP Washington、HealthPartners、Essentia、Henry Ford、KP Northwest / Colorado / Georgia / Hawaii / Southern California。**应作为同一研究组的前后续作引用。**
20. **COI 披露:** "Dr. Penfold reports receiving research funding to his institution from SAGE Therapeutics and the Lundbeck Foundation."(与编码伪影议题相关性低,但须披露。)
21. **(a) 与 (b) 存在实质张力,必须并陈:** (a) 说 2015-10 在 NJ 未产生显著跳变、净量基本不变;(b) 说 12–17 岁蓄意自伤即时跳变 38.5/10万。两者口径不同(全人群 vs 12–17 岁;是否吸收 undetermined intent;州级全量 vs 九个医疗系统会员),**不能当作同一结论叠加使用**。

### (c) 匿名调查免疫伪影 —— 原表述被推翻,必须收窄

22. **修正后的可用表述:「YRBS/MTF/NSDUH 不受**临床筛查与 ICD 诊断编码**这两类伪影影响(它们不使用诊断编码),但并非无测量伪影 —— 有自身的模式效应、应答率与可比性断裂。」**
23. **硬反证(SAMHSA 一手,逐字):**
    > "Unlike previous NSDUH detailed tables, there are no trend tables comparing estimates to previous years for 2021. This is because changes in survey methodology mean the indicators are not comparable to past NSDUH estimates."
    (SAMHSA 2021 NSDUH Detailed Tables 页面,https://www.samhsa.gov/data/report/2021-nsduh-detailed-tables)
    → **NSDUH 无法承载跨 2020–21 的连续趋势。**
24. **逻辑内部矛盾必须点破:(c) 与 (d) 冲突。** (d) 之所以存在,正因为「匿名自评的报告行为可能漂移」是一个**需要检验而非可以假定**的命题;若匿名调查天然免疫伪影,该研究无从立题。

### (d) 挪威 Ungdata —— 表述反了

25. **出处:** Nilsen SA, Stormark KM, Bang L, Brunborg GS, Larsen M, Breivik K. "Time trends in adolescent depressive symptoms from 2010 to 2019 in Norway: real increase or artifacts of measurements?" *Psychological Medicine* 2024 Oct;**54(14):3949–3961**,DOI 10.1017/S0033291724002447,PMID 39370997,PMCID PMC11578914(另有 PsyArXiv 预印本 10.31234/osf.io/4g8hu)。开放获取。
26. **摘要逐字:**
    > "560 712 responses from adolescents aged 13 to 19 years"
    > "Depressive symptoms were measured with the Kandel and Davies' six-item Depressive Mood Inventory"
    > "**Across most conditions, the instrument was found measurement invariant across time. The few noninvariant parameters detected had negligible impact on trend estimates.** From 2014, latent mean depressive symptom scores increased among girls. For boys, a U shaped pattern was detected, whereby an initial decrease in symptoms was followed by an increase from 2016. **Larger issues of noninvariance were found across age in girls and between genders.**"
    > 结论:"the notion that changed reporting of symptoms has been an important driver of secular trends in depressive symptoms **was not supported**"
27. **核心表述错误:不是「校正测量不变性后女生上升仍在」,而是「检验后发现跨时间不变性基本成立,趋势无需校正即成立」。**
28. **构念错配须点明:测的是抑郁症状(Kandel & Davies 六题 Depressive Mood Inventory),不是自伤或自杀行为。** 用它支撑自杀相关趋势属跨构念外推,与 (a)(b) 不可直接互证。
29. **时间窗须精确:女生潜均值上升是从 2014 起(非全窗口 2010–2019);男生 U 形为先降、自 2016 起回升。**
30. **被略去的反向限定必须补:** "Larger issues of noninvariance were found across age in girls and between genders." —— **跨性别与跨年龄比较恰恰是该研究中最不可靠的部分,而 (d) 的论证方式(女生 vs 男生对比)正好踩在这一弱点上。**
31. **在框架中的角色应标明为反向证据:** 该文否证的是测量伪影解释,与 (a)(b) 方向相反。**这正是「双向」成立之处,但原论断把四项并列陈述,读者易误读为四项同向支持伪影解释。**

---

## 修正记录(修正前→修正后)

| # | 修正前 | 修正后 |
|---|---|---|
| 1 | (a) 两个跳点 = 2011 筛查建议 + 2016-10 编码指令 | **数据折点是 2012 与 2016–2017**;2009 USPSTF / 2011 保险强制 / 2011-08 WPSG / 2016-10 编码指令是**制度诱因日期**,不是折点 |
| 2 | (a) 2011 抑郁筛查建议 | **USPSTF 建议发布于 2009-03-15**;2011 只是保险被强制承保的起点;WPSG 保险覆盖实际生效于 2012-08-01 起的计划年度 |
| 3 | (a) 2016-10「编码指令」(性质不明) | 2015-10 ICD-10 对 R40–R46 设 **Exclude 1**(禁止与 F01–F99 主诊断并编),Cooperating Parties 承认为错误,**2016-10 改为 Exclude 2**,构成 180 度反转 |
| 4 | (a) 新泽西医院数据(未标年龄) | **10–18 岁**(非 12–17),全州住院 + 急诊,2008–2019 |
| 5 | (a) 自杀完成率来自新泽西医院数据 | **不来自医院数据**,来自 NJ 生命统计(Dept. of Families and Children 2016);正文措辞更弱:"do not show a clear trend",并承认东北地区整体 2015–2017 有些上行 |
| 6 | (a) 涨幅主要来自自杀意念 | 更精确:趋势断裂的是**作为次要诊断的**自杀意念(25.3 增量中 24.9 来自 SI,其中 18.5 为次要诊断);SI 作为主要诊断只是平缓上升 |
| 7 | (a) 可用于论证全国自杀上升是伪影 | **不可**。作者脚注自陈 "youth suicides rose nationally but not in New Jersey";并明写 "These results should not be interpreted in a way that casts doubt on the seriousness of the youth mental health crisis." |
| 8 | (b) 即时跳变 **+**38.5/10万、斜率 **+**6.5/10万/月 | 摘要原文只写 "change",**无正负号、无 CI、无 p 值**;正号属推断 |
| 9 | (b) 未标窗口 | ITS 窗口仅切换**前后各 15 个月**;6–11 岁组仅斜率 0.18/10万/月、**无即时跳变** |
| 10 | (b) PS 2017 引语作为「ICD-10 使自伤就医率虚增」的通用背书 | 逐字含关键限定语 "coding of **intent**" —— 指意图归类互换,不是自伤总量;且为一页 Datapoints、十个 MHRN 系统**全体参保人**、每万参保人、纯描述性无统计检验 |
| 11 | (b) ICD-10 跳变 = 单向虚增 | Stewart 的自伤编码上升被 undetermined-intent 下降**抵消**;JHR 总结净量 "remained largely unchanged";后续文献读作**测准度改善**(better ascertainment) |
| 12 | (b) PS 2017 与 Acad Pediatr 2026 是两条互证线索 | **非独立**:Christine Stewart 同为两篇作者,同属 MHRN/KP 体系(10 vs 9 个系统高度重叠) |
| 13 | (c) 匿名调查不受伪影影响 | **REFUTED(作为无限定断言)**。收窄为「不受临床筛查与 ICD 编码伪影影响,但有自身模式效应/应答率/可比性断裂」;SAMHSA 一手明示 2021 NSDUH 不可跨年比较 |
| 14 | (d) **校正**测量不变性后女生上升仍在 | **REFUTED**。该研究未做校正,而是**检验后发现不变性成立**:"the instrument was found measurement invariant across time";结论是趋势无需校正即成立 |
| 15 | (d) 置于自伤/自杀测量伪影论证链 | 构念是**抑郁症状**(Kandel & Davies 六题),13–19 岁,N=560,712,不是自伤/自杀;跨构念不可直接互证 |
| 16 | (d) 2010–2019 女生上升 | 女生上升**自 2014 起**;男生 U 形先降、**自 2016 起**回升 |
| 17 | (d) 未提该文自陈弱点 | 须补 "Larger issues of noninvariance were found across age in girls and between genders" —— 跨性别对比恰是最弱环节 |
| 18 | 四项并列陈述 | 须明示 (d) 是**反向证据**(否证伪影解释),(a)(b) 之间亦有张力 —— 这才是「双向」的实义 |

**票间冲突与裁决:**
- **PS 2017 引语能否逐字核到一手。** 一票经 **Wayback 快照(20251217134339)取得该 Datapoints 全文**并逐字核对成功;第二票仅经 Google Scholar 索引取得完整原句(单一二次索引);第三票尝试 7 条独立路径(PubMed、Europe PMC、Semantic Scholar、scholar.archive.org、fatcat、CORE、Unpaywall→出版社)全部失败,主张「在能逐字核到之前不应把该引语当作可引用证据」。
  **裁决:采第一票 —— 引语已由存档全文逐字确认,可以使用。** 但须记录:**仅有 Wayback 单一存档通道**(Psychiatry Online 出版方 403),未达「两个以上独立镜像」标准;且**三票一致要求补回被原引语漏掉的 "of intent" 限定语**,这一点比引语真伪更实质。
- **PS 2017 与 Acad Pediatr 2026 的具体系统重叠名单。** 三票均只能从机构署名判断高度重叠(PS 2017 的 online appendix appi.ps.201600450.ds001.pdf 未取得)。**裁决:结论「非独立」成立(共同作者是硬事实),但「重叠名单」不写具体系统数对应关系。**

---

## 未回溯项

1. **Acad Pediatr 2026 中 38.5、6.5、0.18 三个估计的正负号与置信区间 —— 三票全部失败,标记「未回溯」。** 全文闭源(Unpaywall is_oa=false, oa_status=closed;无 PMCID、inEPMC=N;无预印本);ScienceDirect / linkinghub / doi.org 全部 403;Google Scholar 无免费全文;PubMed 与 Europe PMC 摘要本身不含符号。**成稿写这三个数时不得加正号,或须明确标注「方向未在摘要中给出,依机制推断为正」。**
2. **Ryan et al. 2026 是否同时报告了 undetermined-intent(意图不明)序列的对冲下降 —— 未能确认。** 这决定 +38.5 中有多大比例只是重新归类而非净增,**是评估 (b) 力度的关键缺口**。全文闭源,摘要未提。
3. **Acad Pediatr 2026 切换前的基线月率未取得**,因此无法判断 38.5/10万 的即时跳变相对基线是多大幅度(小幅还是接近翻倍),也就无法评估它与 Stewart 2017「净量基本未变」之间张力的实际大小。**这是本组最需要补一手全文的缺口。**
4. **PS 2017 的 online appendix 未取得**,故 10 个 MHRN 系统与 Acad Pediatr 2026 的 9 个系统之间的具体重叠名单无法逐一比对;该 Datapoints 专栏的具体数值(ICD-10 前后自伤/自杀未遂编码率的实际数字)亦未取得,故无法核实其结论强度是否支撑论断赋予它的分量。
5. **PS 2017 引语的第二独立镜像未取得**(Psychiatry Online HTML 与 PDF 均 403;Semantic Scholar 存档 PDF 已 301 到无正文落地页;fatcat 连接被拒;CORE 403;Europe PMC 全文检索对 "artifacts of coding changes" 等三种变体均 0 命中)。目前仅 Wayback 单源。
6. **(c) 关于 YRBS 与 MTF 各自的方法学断点未回溯到一手**(YRBS 2021 疫情期施测条件、MTF 2020 采集中断;CDC MMWR YRBS 2023 方法学页与 monitoringthefuture.org 年报页均 403)。**(c) 的修正目前只由 NSDUH 2021 的自陈不可比性 + (d) 研究的立题逻辑支撑。** 若正文要主张「YRBS/MTF 也有断点」,须另补一手。
7. **三篇论文的后续勘误/评论/独立重复研究未做系统检索。** 三票的 WebSearch 配额均在会话开始时已耗尽(200/200),只能用 WebFetch 直接取址。三篇的 PubMed 记录页均未显示勘误标记,但未做 citing-article 反证检索。

---

## 证据分级

- **(a) Corredor-Waldron & Currie:多源证实。** 三票分别经 JHR 官方全文 PDF(jhr.uwpress.org,pdftotext)、JHR HTML 全文、NBER w31493 PDF 三条独立通道取得并逐字核对,摘要与正文数字完全一致。开放可得、有明确资助与无 COI 声明。**可承重**,但必须带上第 8/10/11 条的三处作者自设限定语。
- **(b) Acad Pediatr 2026:单源已核(仅摘要级)/ 关键参数未验证。** 数字、年龄段、系统数、时间点、窗口经 PubMed 与 Europe PMC 两处独立镜像一致确认;**但正负号、CI、基线、对冲序列全部未回溯,全文闭源。** 可引用数值,不得引用方向,不得当作「净增」证据。
- **(b) Stewart PS 2017:单源已核(存档通道)+ 厂商口径无涉。** 引语经 Wayback 全文逐字确认(单一存档源);体裁为一页描述性专栏、无统计检验,**证据强度本身就弱**,不宜承重。COI:Penfold(2026 文)申报 SAGE Therapeutics 与 Lundbeck Foundation 机构资助,与议题相关性低。
- **(b) 组内两条证据的独立性:方向存争 → 已裁定为非独立。** 不得并列为交叉验证。
- **(c) 原表述:未验证 → 已被一手反驳。** SAMHSA 官方页面逐字反证(三票中两票独立核到同一句)。**必须按第 22 条收窄后才能使用。**
- **(d) Nilsen et al. 2024:多源证实。** 开放获取(PMC11578914),经 PubMed 与 Europe PMC 两处独立镜像逐字一致。**可承重**,但必须(i)改正「校正后」的表述,(ii)标明构念是抑郁症状而非自杀行为,(iii)带上作者自陈的跨性别不变性弱点。
- **整组框架:「双向」成立,但原并列写法会误导。** 建议成稿结构改为:「(a)(b) 指向报告/编码侧的伪影,但两者对同一个 2015-10 事件给出相反净效应,且 (a) 作者明确反对用其结论质疑危机本身;(d) 用挪威匿名调查直接检验了自评漂移假说并**否证**了它;(c) 则不能作为无限定断言 —— 匿名调查有自己的模式断点。」


---

# C17 最终判决:CORRECTED(3/3 票;(c) 的「剪刀差」框架为 REFUTED)

论断组:国际不同步 —— (a) Haidt 2022 证词逐字;(b) 德国 KiGGS 19.9%→16.9%;(c) 北欧自杀率平稳/芬兰大降;(d) 英国 MHCYP 三线同步。
三票一致:**四条引语/数字本身逐字成立,但四条的「用途」全部错位** —— (a) 已被作者自己推翻且原段落主旨是**同步**不是不同步;(b) 的下降由男孩驱动、女孩无下降、且同数据自报口径给出相反结论;(c) 三国口径混用,且瑞典与青少年女性切片方向相反;(d) "remained stable" 是选择性引用、口径断裂被错误归因。

---

## 锁定口径(成稿必须用)

### (a) Haidt 2022 参议院证词

1. **出处全称:** Testimony of Jonathan Haidt,《Teen Mental Health Is Plummeting, and Social Media is a Major Contributing Cause》,Before the Senate Judiciary Committee, Subcommittee on Technology, Privacy, and the Law, **May 4, 2022**,**p.4 §1.6「The crisis has hit many countries, not just the USA.」**。https://www.judiciary.senate.gov/imo/media/doc/Haidt%20Testimony.pdf(三票均以 pdftotext 全文核对)
   (注:文件自称的小组委员会词序为 "Technology, Privacy, and the Law",与官方名 "Privacy, Technology, and the Law" 相反。)
2. **完整逐字(省略号必须补回):**
   > "**The patterns are nearly identical in the UK and Canada, and the trends are similar though not identical in Australia and New Zealand.** We do not yet see signs of similar epidemics in continental Europe or in East Asia, although **I have not yet found good data from those regions**."
   → 他 2022 年划的线是「英语圈 vs 其余」,不是「两国 vs 世界」;且**原句自带 "I have not yet found good data" 的自限**。
3. **紧随其后的同段文字必须一并引 —— 这是最重要的语境修正(一票发现,决定性):**
   > "…Jean Twenge and analysed the PISA dataset ... **Sure enough, we found a sudden increase between 2012 and 2015 in all regions of the world.**"
   > Figure 3 标题:"**Loneliness at school increased in all regions of the world after 2012.**"
   > "The cause is likely to be something that affected teens in many or all regions of the world at the same time."
   → **该段整体论证的是国际同步,不是不同步。只截取欧亚那一句会倒转段落主旨。**
4. **该表述已被作者本人推翻,不能当作 Haidt 的现行立场或「不同步」的证据。**
   Haidt & Rausch,《The Teen Mental Illness Epidemic is International, Part 2: The Nordic Nations》,After Babel,**2023-04-19**:
   > "The mental health of teen girls, based on self-report measures, has been declining, often sharply, **in all five Nordic nations** since the early 2010s."
   > "the basic pattern largely holds"
   文中并自陈原本预期北欧会 substantially differ 而落空;亦承认自伤数据不一致(丹麦 2000 年代末见顶后回落,归因扑热息痛 OTC 限售;瑞典自伤 2020 前增幅很小;芬兰/挪威/冰岛数据不足)。
   另有《The Youth Mental Health Crisis is International Part 4: Europe》,2024-01-30。
   **引用规则:2022 证词只能当「2022 年时点快照 + 他当时手上没数据」来引,并必须标注 11 个月后被作者自行修订。**
5. **来源性质标注:** 证词为立场性文件(标题即 "Social Media is a Major Contributing Cause"),引用时应作为「主张」而非「证据」处理;After Babel 为主张方自营 Substack、非同行评议、作者有专著商业利益,仅可用于证明其立场变更,不作为北欧趋势的独立证据。

### (b) 德国 KiGGS

6. **出处:** Klipker K, Baumgarten F, Göbel K, Lampert T, Hölling H,《Psychische Auffälligkeiten bei Kindern und Jugendlichen in Deutschland – Querschnittergebnisse aus KiGGS Welle 2 und Trends》/ 英文版 *Journal of Health Monitoring* 2018;**3(3)**,PMID 35586801 / PMC8848775。
   **DOI 有两个版本(德文版与英文版不同),两票各引其一,均可核:** 德文版 DOI 10.17886/RKI-GBE-2018-077(pp.37-45,edoc.rki.de/bitstream/handle/176904/5767/);英文版 DOI 10.17886/RKI-GBE-2018-084(pp.34-41,edoc.rki.de/handle/176904/5774)。成稿引用建议同时给 PMC8848775。
7. **Table 1 完整数值(基线 2003-06 vs Welle 2 2014-17,%,95% CI):**
   | | 基线 | Welle 2 |
   |---|---|---|
   | 合计 | **19.9 (19.0–20.8)** | **16.9 (15.9–17.9)** |
   | 女孩 | 15.9 (14.9–17.0) | 14.5 (13.2–15.9) |
   | 男孩 | 23.6 (22.3–24.9) | 19.1 (17.7–20.6) |
   | 女孩 15–17 岁 | 13.4 (11.5–15.6) | **14.6 (12.2–17.3)**(不降反升) |
   | 男孩 9–11 | 28.8 | 22.2 |
   | 男孩 12–14 | 25.8 | 19.2 |
   | 男孩 15–17 | 17.2 | 12.2 |
   样本 n=14,477(基线)/ 13,205(Welle 2);Welle 1(2009-2012)相对基线 "unverändert geblieben"。
8. **两个基线数字不可混用。** 摘要/引言用的 **20.0%** 是 KiGGS 原始基线发表值;**19.9%** 是为算趋势按 2015-12-31 人口做年龄标准化后重新加权的值。官方解释逐字:
   > "In comparison to the KiGGS publication in 2007, the minimal difference in the indicated prevalence at KiGGS baseline is due to the adjusted weighting procedure (age-standardised prevalence according to the population on 31 December 2015) necessary for the calculation of time trends."
9. **「显著下降」只对男孩成立 —— 三票一致的最关键口径修正:**
   > "A detailed analysis for girls and boys within different age groups reveals **a statistically significant decrease for mental health problems among boys between 9 and 17 years of age**"
   > "However, **there is no comparable statistically significant decline in the frequency of mental health problems among girls across all age groups** (Table 1)."
   德文原句:"Ein vergleichbarer, statistisch bedeutsamer Rückgang in der Häufigkeit psychischer Auffälligkeiten bei Mädchen kann zu KiGGS Welle 2 über alle Altersgruppen hinweg nicht nachgewiesen werden."
   **由于英美危机恰恰集中在女孩,用德国总体数去反驳女孩危机是构念错配。**
10. **构念与时窗:** **家长版(Elternversion)SDQ**、3–17 岁、总困难分 **≥13 分**为「有问题」(即 borderline+abnormal 合并),非诊断。方法逐字:"Participants with a sum score of 12 points or less were categorized as ... without mental health problems, whereas those with 13 points or more ... with mental health problems"。RKI 自陈 SDQ "does not enable valid conclusions" 关于具体障碍。**Welle 2 现场期 2014–2017,终点在疫情前,仅覆盖智能手机普及后最初数年。**
11. **同一套 KiGGS 数据的自报口径给出相反结论 —— 必须并陈:**
    Baumgarten F, Junker S, Schlack R. "Prevalence and Time Trends of Self-Reported Mental Health Problems Among Children and Adolescents Between 11 and 17 Years in the KiGGS Study." *Zeitschrift für Kinder- und Jugendpsychiatrie und Psychotherapie* 2023;**51(4):311-320**,DOI 10.1024/1422-4917/a000936(CC BY 4.0;PMID 37417965)。
    > "the prevalence estimates did not vary significantly between the study waves, neither regarding the category 'abnormal' (**9.3 % vs. 9.4 %**) nor the pooled categories 'borderline/abnormal' (**16.9 % vs. 15.4 %**)"
    > "**These findings differ from those based on the SDQ parent report, which suggests significant declines in symptom load between the study waves.**"
    > "The emotional problems of girls at a higher age increased in KiGGS wave 2. For example, the mean value of emotional problems for 16-year-old girls was **3.37** in the KiGGS baseline study (boys: 2.07) and **3.85** in KiGGS Wave 2 (boys: 2.08)."
    作者称此 "is in line with the results of other international studies, which describe an increase in internalizing psychological problems in girls"。
    → **德国「下降」只是家长报告口径;11–17 岁自报口径无变化,且高龄女孩情绪问题上升。**
12. **RKI 自己给出的替代解释(不是「无危机」而是「服务侧改善」):** 儿少精神科医师数由 2003 年 **557 名**增至 2017 年 **1,062 名**;U10/U11 筛检扩展。

### (c) 北欧 —— 三国口径混用,框架被推翻

13. **芬兰 -45%/-31% 的时窗与统计量必须补全。**
    一手表述(Nordic Health and Welfare Statistics, nhwstat.org):
    > "Finland stands out among the Nordic countries with a marked fall over the past decades from an earlier higher level."
    > "**The age-standardized suicide rate was its highest in 1990 but decreased by 45% for men and by 31% for women in the following two decades.**"
    → 是 **1990→约 2010 这两个十年、全年龄**的降幅,**不是至今降幅,也不是青少年降幅**。归因于 1986–1996 全国自杀预防计划与抗抑郁药使用增加。**该窗口在 2012 年之前就已结束,对 2012 年后青少年趋势无信息量。**
14. **芬兰一手复核(Statistics Finland PxWeb,表 11ay 死因码 50 = Suicides, X60-X84/Y870):**
    粗死亡率:1990 男 49.5 / 女 12.5;2010 男 27.3 / 女 8.6 → **−44.8% / −31.2%**,精确复现 −45%/−31%。
    年龄标准化率:1990 男 52.6 / 女 12.9 → 2024 男 20.7(或 20.6)/ 女 6.5 → **−60.8% / −49.6%**。
    峰值年 1990 由表 11by 确认(男 1,193、女 319,为 1970 年后最高);2012 男 655/女 218;2015 男 558/女 173;2024 男 577/女 184。
    佐证:芬兰统计局 2020 年死因统计 —— "The number of suicides has decreased relatively evenly since 1990, when more than 1,500 suicides were committed in Finland";2020 年 717 例、13/10万(男 19、女 7)。
15. **芬兰青少年切片与「剪刀差」方向相反(必须写):** StatFin 表 11by,15–19 岁**女性**自杀数 1990–94 年均 **6.6 例** → 2020–24 年均 **14.4 例**(约翻倍);同期 15–19 岁男性由 62(1990)降至 2020–24 年均约 19.6。(单年计数小、噪声大,故用五年均值。)
16. **挪威口径必须改。** 论断所依据的原始表述来自评论文章而非数据论文:
    Ekeberg Ø, Hem E. "Why is the suicide rate not declining in Norway?" *Tidsskr Nor Legeforen* 2019(**PERSPECTIVES / kronikk 观点栏目**):
    > "Despite these efforts, **the suicide rate has remained largely unchanged in Norway from 1995 to 2015** (Figure 1)"
    > 图注:"Suicide rates in Scandinavia 1990–2015 (**unadjusted figures** based on national suicide statistics)"
    → **未年龄标准化的全人群率,非青少年。**
    **官方绝对数(Statistics Norway 表 08877「Suicides, by sex, age and method (closed series) 1969-2012」):** 1990=659, 1995=548, 2000=541, 2005=533, 2010=548, 2011=598, 2012=515。同期挪威人口约 +16%,故「率」实为温和下降(约 −14%),**「平稳」只对绝对数成立**。
    (另一票取 NSSF/UiO《Facts about Suicide》2020-11:1995=548、2000=548、2005=533、2010=551、2015=593、2018=674、2019=652、2020=639;文字 "since 1988 the rate has been decreasing yearly, with some variations. **The past 10-15 years, the suicide rate has stabilized at around 12-14 per 100 000 people.**" —— 注意该表述把「平稳」定位在约 2005 年之后,且同期绝对例数是上升的。)
17. **瑞典条目与「剪刀差」方向相反 —— 三票一致,这是本组最实质的推翻。**
    Junuzovic M, Lind KMT, Jakobsson U. "Child suicides in Sweden, 2000–2018." *Eur J Pediatr* 2022;**181(2):599–607**,DOI 10.1007/s00431-021-04240-7,PMID 34476611,PMC8821491。
    > "In total, **416** child suicides were found in the period from 2000 through 2018. The suicide rate was, on average, **22 suicides/year or 1.1 per 100,000 child population/year** (mean child population during the study period was 1.97 million)."
    > "**The number of child suicides increased with 2.2% by each successive year** during the study period (p < 0.001)."
    > "time (years) was a significant and positive predictor of the number of child suicides (p < 0.001)"
    统计量:Poisson 回归,"adjusted for child population size",**B=0.021, S.E.=0.012, IRR=1.022**;96% 为 13–17 岁;男 55% / 女 45%;数据源为 Swedish National Board of Forensic Medicine(法医全覆盖尸检),对象为 <18 岁。
    → **瑞典 <18 岁自杀率是统计显著上升,与自报症状恶化同向,不能充当「客观指标未恶化」的一侧。**
    **单位精确化:原文是自杀「例数」每年 +2.2%(已按儿童人口数调整),不是「自杀率年增长率」。** 论文未给出逐年或分性别的趋势分解,故不能用它论证「女孩行为学指标未动」。
18. **构念混用必须点破:** 芬兰/挪威用的是**全年龄国民自杀率**(且主要由中老年男性、酒精政策与抗抑郁药可及性驱动),瑞典用的是 **<18 岁专项率**,两者不可并列作同一「北欧自杀率」证据。
19. **更强的北欧反证(青少年女性亚组,两篇独立学术论文):**
    > Oskarsson H, Mehlum L, Titelman D, Isometsä E, Erlangsen A, Nordentoft M, Mittendorfer-Rutz E, Hökby S, Tomasson H, Palsson SP. "Nordic region suicide trends 2000-2018; sex and age groups." *Nord J Psychiatry* 2023,DOI 10.1080/08039488.2023.2231918,PMID 37435817:"The largest decrease was found in Finland (34.9%), the smallest in Norway (1.4%)";"**Among females, an increase was seen among 15-24-year olds in all countries except Iceland, in all age groups in Norway, and in 25-44-year olds in Sweden.**"
    > Titelman D et al. "Suicide mortality trends in the Nordic countries 1980-2009." *Nord J Psychiatry*,PMID 23293897:"The suicide rates across the Nordic countries declined from 25-50 per 100,000 in 1980 to 20-36 in 2009 for men and from 9-26 in 1980 to 8-11 in 2009 for women.";"**A significant increase of suicides in young women in Finland and Norway and a lack of a decline among young women in Sweden were noted.**"
    → **北欧总量下降的同时,年轻女性这一亚组在芬兰、挪威是显著上升的。「剪刀差」只在全年龄汇总层面成立,必须限定。**

### (d) 英国 NHS MHCYP

20. **完整序列(8–16 岁 probable mental disorder):12.5%(2017)→ 17.1%(2020)→ 17.7%(2021)→ 19.0%(2022)→ 20.3%(2023)。**
    报告逐字(Part 1: Mental health):
    > "The prevalence of a probable mental disorder in children aged 8 to 16 years rose between 2017 and 2020, from 12.5% in 2017 to 17.1% in 2020. Rates in the subsequent survey waves were similar with no statistically significant differences between these years. In 2021, 17.7% of children in this age group had a probable mental disorder, in 2022, the figure was 19.0% and in 2023, it was 20.3%."
    2023 其他年龄组:17–19 岁 **23.3%**、20–25 岁 21.7%;17–25 岁 "rates were twice as high for young women than young men",8–16 岁男女相近。
    **跳升集中在 2017→2020(+4.6pp),之后三年合计 +3.2pp。**
    **常被引的 18.0% 属 7–16 岁口径,基数不同,勿与 19.0%(8–16 岁,2022)混用。**
21. **"remained stable" 是选择性引用 —— 三处必改:**
    > 报告原句(性别段):"For girls and young women in both age groups (8 to 16 years, and 17 to 19 years), prevalence of probable mental disorder rose between 2017 and 2020, **then remained stable over the subsequent survey waves**. Rates were similar between 2022 and 2023."
    > **紧接着的下一句:"For boys aged 8 to 16 years, prevalence of probable disorder also rose between 2017 and 2020, and then remained stable."** → **不是女生特征。**
    > 另一处官方表述:"After a rise in prevalence between 2017 and 2020, rates of probable mental disorder **remained stable in all age groups between 2022 and 2023**." → **限定的是 2022→2023 这一年,不是「2020 之后」;限定对象是 all age groups。**
    > "stable" 指置信区间重叠、无统计显著差异(n≈2,370,CI 宽),**点估计仍在连续上行**(17.1→17.7→19.0→20.3)。
    > **17–19 岁并不 stable:"there was an increase in the rate of a probable mental disorder between 2021 and 2022, from 17.4% in 2021 to 25.7% in 2022."**
22. **口径断裂被错误归因 —— 三票一致的关键修正。量表在该趋势序列中是恒定的。**
    > "although the SDQ was used in MHCYP 2017, the mental disorder prevalence estimates in the initial MHCYP 2017 survey report drew on a different and more detailed diagnostic assessment of mental disorder, the Development and Well-Being Assessment (DAWBA). **For the 2020, 2021, 2022 and 2023 follow up waves, only the SDQ was used.** This was mainly due to the shift to online data collection during the pandemic"
    > "**When the 2023 report was produced, comparable SDQ measures were produced for 2017, 2020, 2021, 2022 and 2023 for mental disorder prevalence estimates.**"
    → **12.5%(2017)是用 2017 年全部 9,117 人样本重算的 SDQ 估计值,不是 DAWBA 头条数字。**
    **真正的断裂是:**
    (i) **施测方式**:2017 面访 → 2020 起线上(CAWI)/ 电话(CATI)。报告自陈:"comparisons with the MHCYP 2017 estimates may be affected by changes in survey design, such as the use of face to face interviews in the 2017 survey while the follow up waves were online";
    (ii) **纵向追踪与流失**:2020–2023 各波不是新抽样横断面,而是 2017 样本的追访。技术附录:2017 完成访问 **9,117** 人;同意再联系 6,898;2023 合资格 6,773;**2023 实际参与仅 2,370 人(约为原样本 26%)**。把 12.5%→20.3% 当作人群患病率趋势时,必须写明这是**重加权后的追踪面板估计**,存在差异性流失风险。
23. **12.5% 不是那个著名的「八分之一」,两条线不可拼接。** MHCYP 2017 另有可比的 **5–15 岁 DAWBA 面访序列:9.7%(1999)→ 10.1%(2004)→ 11.2%(2017)**(情绪障碍 4.3%→3.9%→5.8%);NHS 原文 "Comparable data is available for 5 to 15 year olds living in England in 1999, 2004, and 2017"。该 5–15 岁序列与 8–16 岁 SDQ 序列是两条不同的线。
24. **学术引用格式:** Newlove-Delgado T, Marcheselli F, Williams T, Mandalia D, Dennes M, McManus S, Savic M, Treloar W, Croft K, Ford T. (2023) *Mental Health of Children and Young People in England, 2023*. NHS England, Leeds。官方新闻稿交叉印证:https://www.england.nhs.uk/2023/11/one-in-five-children-and-young-people-had-a-probable-mental-disorder-in-2023/

---

## 修正记录(修正前→修正后)

| # | 修正前 | 修正后 |
|---|---|---|
| 1 | (a) 引语只点名 UK/Canada | 省略号吞掉了澳新分句:"the trends are similar though not identical in Australia and New Zealand" —— 他划的线是「英语圈 vs 其余」 |
| 2 | (a) 该引语支持「国际不同步」 | **段落主旨相反**。紧随其后:与 Twenge 分析 PISA "we found a sudden increase between 2012 and 2015 **in all regions of the world**";Figure 3 标题 "Loneliness at school increased in all regions of the world after 2012." |
| 3 | (a) 作为 Haidt 的立场/现行证据 | **已被作者自己在 11 个月后推翻**(After Babel 2023-04-19:北欧五国 "the basic pattern largely holds");只能作 2022 年时点快照引用;原句自带 "I have not yet found good data from those regions" |
| 4 | (b) 德国青少年心理问题显著下降 | **下降由 9–17 岁男孩驱动;女孩各年龄组均无显著下降;15–17 岁女孩 13.4%→14.6% 不降反升** |
| 5 | (b) 基线 19.9% | 19.9% 是为趋势比较按 2015-12-31 人口年龄标准化后的重加权值;原始发表基线是 **20.0%**,两者不可混用 |
| 6 | (b) 未标构念 | **家长版 SDQ**、3–17 岁、总困难分 ≥13(borderline+abnormal 合并),非诊断;n=14,477/13,205 |
| 7 | (b) 可作为德国「无同步恶化」的证据 | **同一套 KiGGS 的自报口径给出相反结论**(Baumgarten 2023:11–17 岁自报 abnormal 9.3% vs 9.4%、borderline/abnormal 16.9% vs 15.4%,均不显著;16 岁女孩情绪问题均值 3.37→3.85);且 RKI 自己提出「服务侧改善」的替代解释(儿少精神科医师 557→1,062) |
| 8 | (b) 时窗可代表智能手机时代 | Welle 2 现场期 2014–2017,终点在疫情前,仅覆盖智能手机普及后最初数年 |
| 9 | (c) 芬兰「长期大降」男 −45%/女 −31% | 是 **1990→约 2010、全年龄**的降幅(粗率复现为 −44.8%/−31.2%);窗口在 2012 前就已结束,对 2012 后青少年趋势无信息量;归因于全国自杀预防计划与抗抑郁药 |
| 10 | (c) 芬兰数据支持「客观指标未恶化」 | **芬兰 15–19 岁女性自杀数 1990–94 年均 6.6 → 2020–24 年均 14.4,约翻倍**(StatFin 11by) |
| 11 | (c) 挪威 1995-2015 大体平稳 | 出处是 Ekeberg & Hem 2019 的 **观点栏文章**,用的是**未年龄标准化的全人群率**;官方绝对数 1995=548→2012=515 近乎持平,但同期人口 +16%,率实为约 −14% |
| 12 | (c) 瑞典数据构成剪刀差 | **REFUTED,方向相反**。瑞典 <18 岁自杀 2000–2018 **显著上升 +2.2%/年(p<0.001, IRR=1.022)**,与自报症状恶化同向 |
| 13 | (c) 瑞典「年均 +2.2%」(读作率增长) | 原文是自杀**例数**每年 +2.2%(Poisson,已按儿童人口调整);416 例、22 例/年、1.1/10万/年 |
| 14 | (c) 三国并列为「北欧自杀率」 | **构念混用**:芬/挪是全年龄国民率(中老年男性主导),瑞典是 <18 岁专项率,不可并列 |
| 15 | (d)「2020 后女生 remained stable」 | 三重错置:(i) 官方 "remained stable" 限定的是 **2022→2023**;(ii) 对象是 **all age groups / 男生也一样**;(iii) 点估计仍连续上行 17.1→17.7→19.0→20.3;(iv) 17–19 岁并不 stable(17.4%→25.7%) |
| 16 | (d) 1999/2004/2017 面访诊断式、2020 起改线上 SDQ 口径 | **该趋势序列量表恒定** —— 2017 的 12.5% 是用 SDQ 回溯重算值;真正断裂是**施测方式**(面访→线上/电话)与**纵向追踪流失**(9,117 → 2,370,约 26%) |
| 17 | (d) 12.5% 与著名的「八分之一」同源 | 是两条线。5–15 岁 DAWBA 面访序列为 9.7%(1999)→10.1%(2004)→11.2%(2017),不可与 8–16 岁 SDQ 序列拼接 |
| 18 | (d) 只给三个锚点 | 完整序列须补 2021=17.7%、2022=19.0%;18.0% 属 7–16 岁口径勿混用 |

**票间冲突与裁决:**
- **(c) 挪威数字的出处。** 一票溯到 NSSF/UiO《Facts about Suicide》(2020-11)PDF;一票溯到 Statistics Norway 表 08877 官方序列;一票溯到 Ekeberg & Hem 2019 Tidsskriftet 观点文(其中含 "the suicide rate has remained largely unchanged in Norway from 1995 to 2015" 这一与论断措辞最贴合的原句)。
  **裁决:三者不冲突,分属三个层级。** 成稿写法:**引数字用 SSB 表 08877(官方一手);引「1995–2015 平稳」这一措辞时须标明出自 Ekeberg & Hem 2019 的观点栏文章、且是未年龄标准化的全人群率。** 两票在 2000 年数值上有小差异(NSSF 548 vs SSB 541)—— **以 SSB 为准。**
- **(c) 芬兰 −45%/−31% 是粗率还是年龄标准化率。** NHWSTAT 原文写 "age-standardized";但一票用 Statistics Finland 表 11ay 复现,发现该对数字精确对应 **1990→2010 的粗死亡率**变化(−44.8%/−31.2%),而同期年龄标准化率的降幅更大(至 2024 为 −60.8%/−49.6%)。
  **裁决:引用时只写 NHWSTAT 的逐字原句 + 「约 1990→2010、全年龄」这一窗口限定,不要自行标注是粗率还是标准化率**(两者在 1990→2010 段上数值相近,但 NHWSTAT 未公布分年数值表,无法确证其算法)。见未回溯项 2。
- **(b) Baumgarten 2023 自报口径反证。** 一票把它列为「本组最值得追补的一处」但只检索到题录;另一票取得 edoc.rki.de 的 CC BY 全文并逐字提取。**裁决:采后者 —— 该反证已核实,必须写进成稿。** 这是本组从「未回溯」升级为「已核」的一项。
- **(b) KiGGS 论文内部不一致:** Table 1 给出 Welle 2 女孩 14.5%,而讨论段落写 "(girls 14.9%, boys 19.1%)"。两处均在同一篇全文中,未见勘误。**裁决:以 Table 1 的 14.5%(13.2–15.9)为准,并在脚注注明原文有此出入。**

---

## 未回溯项

1. **挪威 2013–2015 三年数据无法回溯到一手:** SSB 官方序列(表 08877 / 03272)在 2012 年封闭(死因统计移交 Folkehelseinstituttet),FHI statistikkbank 未能通过可用工具访问、FHI 英文自杀页多个 URL 均 404。故「1995–2015」窗口的后段只能靠 Oskarsson 2023(2000–2018、15 岁以上、口径不同)与 NSSF《Facts about Suicide》间接旁证,**不算逐字核到**。
2. **芬兰 −45%/−31% 的原始出处与确切端点未确认。** 只核到 NHWSTAT 的文字表述,未取到其背后的分年数值表(pxweb.nhwstat.org 需交互查询),因此无法独立复算该降幅、也无法确认 "the following two decades" 的确切终点年(1990→2009 还是 1990→2010),更无法确认待验论断作者用的就是这个端点与这个统计量。**按「可复现但需补端点」处理,不得写成精确到年的表述。**
3. **KiGGS 原文内部不一致(14.5% vs 14.9%)未解决,无勘误。**
4. **MHCYP 的 SDQ pseudo-diagnostic algorithm 细节、以及 2017 年数据如何被重新评分为 12.5%,未取得一手方法学文件。** 记载于 2021 Survey Design and Methods Report(files.digital.nhs.uk/08/0B5432/mhcyp_2021_meth.pdf);digital.nhs.uk 全域被 Cloudflare bot 挑战拦截,三票均未能直接读取活页面。**算法本身与 2017 重算过程属未验证部分 —— 这是本组口径风险最高的点。**
5. **MHCYP 8–16 岁各年度的具体 95% CI 未独立核算**(未打开 Table 1.2 Excel 数据表);"无统计显著差异"/"remained stable" 均引自报告正文自述,而非复核 CI 得出。
6. **(d) 的数字取证通道:** 三票分别经 UK Government Web Archive、2023-11-22 抓取的整页 PDF 镜像(保留 NHS 原 URL 页眉与 1/81…81/81 分页)、以及搜索引擎对 Part 1 页面的索引摘录取得,并与 NatCen 一手页面(2023 年 20.3%/23.3%/21.7%)及 NHS England 新闻稿交叉印证。**内容自洽,但 12.5%/17.1%/17.7%/19.0% 四个中间值未从 digital.nhs.uk 活页面直接目验。建议人工打开 Part 1 页面把四个数字与 Table 1 再对一次。**
7. **Haidt 2022 证词本身未检出任何正式更正或补充材料**(Senate 页面只有 PDF);其立场反转仅见于自营 Substack,**不构成对证词文件的正式勘误**。若需「正式修正」级证据,此项仍为空缺。
8. **Haidt & Rausch 北欧 Substack 所依据的原始数据集(北欧各国自报心理压力序列)未逐条回溯。** 该文非同行评议、作者有专著商业利益,仅用于证明其立场变更。
9. **(c) 三个北欧数字的原始出处(论断组作者当初引的是哪份文件)无法确认。** 三票是按数字反查到 nhwstat.org / Tidsskriftet / NSSF / Eur J Pediatr 各源,数字吻合,但不排除原作者引自其他中介来源并带入了不同口径。
10. **德国/北欧同期青少年自报心理症状序列的完整对照缺失(部分已补)。** Baumgarten 2023 已补上德国自报侧;但瑞典 Folkhälsomyndigheten 的 psykosomatiska besvär 序列、HBSC 德国序列、2023 年后德国 COPSY/HBSC 新波次均未检索。**缺了这一侧,(b)(c) 所称的「剪刀差」仍只有部分数据。**
11. **反证检索覆盖不完整:** 三票 WebSearch 配额均在会话开始前耗尽(200/200),检索靠 Europe PMC REST、各国官方统计 API、直接 curl 与 Brave/Ecosia 结果页抓取完成(Brave 中途 429、lite.duckduckgo 中途 CAPTCHA)。故未能系统检索瑞典儿童自杀论文与 KiGGS 两篇是否存在后续勘误/更正声明,亦不能排除上述四项还有未检索到的更正或再分析。Europe PMC 检索未见 Junuzovic 与 Oskarsson 两文的 correction/erratum 记录。

---

## 证据分级

- **(a) Haidt 2022 证词:厂商口径(利益相关方自述)+ 已过时。** 立场性文件(标题即结论),作者为该议题主张方与商业出版方;引语逐字成立(三票均以官方 PDF 逐字核对,**多源证实**),但**其内容已被作者自己推翻,且原段落主旨与「不同步」相反**。**不得作为国际不同步的证据使用**;只可作为「2022 年时点认知」的引文,并必须同时给出第 3、4 条。
- **(b) KiGGS 家长报告口径:单源已核(官方一手)。** RKI 联邦公共卫生机构自办自报的官方统计,三票分别经 Europe PMC fullTextXML、edoc.rki.de PDF(德/英两版)逐字核对 Table 1,数值完全一致。**可承重,但必须带第 9 条的性别分裂限定。**
- **(b) 自报口径反证(Baumgarten 2023):单源已核(CC BY 全文)。** 与 (b) 主体同属 RKI/KiGGS 体系(非独立数据源,但为不同口径的独立分析)。**必须并陈 —— 否则 (b) 会被误读成「德国无危机」。**
- **(b) 整体:方向存争。** 同一数据集的家长报告与自报口径给出相反结论。
- **(c) 芬兰:单源已核(二手汇编)+ 窗口失效。** NHWSTAT 是北欧官方统计门户但属**可靠二手汇编、非一手数据源**;数字可由 Statistics Finland PxWeb API(一手)复现。**但窗口(1990→2010)在争议期之前结束,对本文论证无信息量。**
- **(c) 挪威:单源已核 + 出处降级。** 论断措辞的出处是**观点栏评论文章**(非数据论文),用未年龄标准化的全人群率;官方序列(SSB 08877)在 2012 封闭,2013–2015 未回溯。
- **(c) 瑞典:多源证实,但方向与论断相反 → REFUTED。** Eur J Pediatr 同行评议论文,法医全覆盖数据,三票逐字一致。
- **(c) 整组「剪刀差」框架:REFUTED。** 三个数字分属三种口径(全年龄 vs <18 岁),且两条独立学术论文(Oskarsson 2023、Titelman 2013)显示**北欧青少年/年轻女性亚组自杀是上升的**;芬兰 15–19 岁女性一手计数亦约翻倍。**该框架不得承重。**
- **(d) NHS MHCYP:多源证实(内容)/ 单源已核(取证通道)。** NHS England 委托、Exeter/NatCen/ONS 团队执行的官方调查;数字经报告正文、NatCen 页面、NHS England 新闻稿三处印证。**可承重,但必须带第 21、22 条的两组限定(stable 的适用范围、面板流失 9,117→2,370)。**


---

# C18 最终判决:CORRECTED(3/3 票)

论断组:PISA 孤独感(Twenge, Haidt, Blake, McAllister, Lemon & Le Roy 2021)。
三票一致:**所有引用的数字与引语逐字成立,无一处被报错**;修正全部落在**口径、分母、构念与计数**上。其中三处是三票独立同时发现的:(c) 因果保留声明是**五处**不是两处;(f) 的分母不是 37 国而是 31 国 / 83 个国-年;(e) 韩国「唯一未上升」只在连续均值口径成立。另有两票发现「36 out of 37」与论文自家表格算不平。

---

## 锁定口径(成稿必须用)

### 书目

1. Twenge JM, Haidt J, Blake AB, McAllister C, Lemon H, Le Roy A. "Worldwide increases in adolescent loneliness." *Journal of Adolescence* 2021 Dec;**93:257-269**。DOI 10.1016/j.adolescence.2021.06.006,PMID 34294429,OpenAlex W3183254835。Epub 2021-07-20。
   Crossref / PubMed / OpenAlex 三源一致;**无勘误、无更正、无撤稿**(Crossref update-to/updated-by/relation 字段皆空;PubMed 无 CommentsCorrections;OpenAlex is_retracted=false)。
   论文为 **CC BY 开放获取**(版权行:"This is an open access article under the CC BY license")。

### (a) 36/37 国 —— 引语成立,计数须加注

2. **摘要逐字:** "**School loneliness increased 2012–2018 in 36 out of 37 countries.**"(en dash;PubMed 渲染为连字符)
   正文 §3.3 用词略异:"Adolescent loneliness increased after 2012 in 36 of 37 countries";讨论区:"school loneliness increased between 2012 and 2018 in 36 out of 37 countries around the world"。
3. **分母有洞,须加注:** 论文自家 Table 1 与 Table 2 显示**冰岛(Iceland)与匈牙利(Hungary)2012 年格为破折号**,表注 5 明言 "Dashes indicate that the survey or measure was not administered in that country in that year",两国的 d(2012–2018) 与 % diff(2012–2018) 同为 "–"。
   **即:37 国中只有 35 国能算出 2012→2018 变化,其中 34 国上升、1 国(韩国)下降。**
   方法节的入选规则只是 "These items were asked in at least 4 of the 5 administrations"。
   **成稿写法:引 "36 out of 37" 逐字,但须注明有 2 国缺 2012 基线。**

### (b) 17.12% → 30.86% —— 数字成立,三处口径限定

4. **Table 2「Worldwide average」行逐格:** 2000 = 16.15%,2003 = 13.21%,**2012 = 17.12%**,2015 = 24.03%,**2018 = 30.86%**;% diff 2012–2018 = **80.26%**;% diff 2000–2018 = 91.05%。30.86/17.12 = 1.80。
5. **三处必须限定:**
   (i) **「高孤独」= 1–4 量表上得分 ≥2.22**,该切点由 **2 成分正态混合模型(mixtools)**估出,**非临床阈值**(表注 2:"High loneliness is defined as a score of 2.22 or above on the 1–4 scale.");
   (ii) **该「全球平均」按各国人口规模加权**(表注 4:"Region and worldwide averages are weighted by the population size of each country";方法称 weighted by country population in 2018),**不是把百万受访者直接汇总的原始比例**;
   (iii) **该二分变量只用于描述统计,不进入任何模型** —— 逐字:"**We present only descriptive statistics for this dichotomous variable; all other analyses and models are based on the continuous measure of loneliness.**"
6. **「nearly twice」的基线年在论文内部不一致,引用必须指明用哪一个:** 摘要写 "nearly twice as many adolescents in 2018 (**vs. 2012**)"(= +80.26%);正文 §3.3 写 "nearly twice as many adolescents in 2018 scored high in loneliness than **in 2000**"(= +91.05%)。
7. **样本口径:** n = **1,049,784**(531,370 girls + 518,414 boys;51% female)是 **2000/2003/2012/2015/2018 五轮的合计**,不是 2012→2018 对比的样本。
   分轮 n(Table 1 全球行):2000 = 107,666、2003 = 221,735、**2012 = 198,992**、2015 = 258,058、**2018 = 264,506**(2012+2018 合计约 463,498)。
8. **年龄口径须补两处限定:** "nationally representative samples of 15- and 16-year-olds **enrolled in school**";"**Most students (67%) were 15 years old**, with the rest 16 years old"。**是在校生、且以 15 岁为主,失学/辍学青少年不在抽样框内。**

### (c) 因果保留声明 —— 是五处,不是两处(三票独立一致)

9. **三处完全逐字的 "causation cannot be proven":**
   > ① 摘要 Conclusions:"…though **causation cannot be proven** and more years of data will provide a more complete picture."
   > ② 引言:"(although **causation cannot be proven**, given the impossibility of experimental research on cultural change)"
   > ③ 全文最后一句:"The rapid spread of smartphones and social media in the years since 2012 may be connected to this rise in loneliness, though **causation cannot be proven**."
10. **另两处同义变体:**
    > ④ 方法前言:"Although such analyses **cannot prove causation**, they can test whether cultural indicators can be ruled in or out."
    > ⑤ 讨论:"Although these analyses **cannot prove causation**, they demonstrate that loneliness grew among adolescents around the world in tandem with widespread smartphone and internet use."
    **合计五处。原论断低估了论文的自我限定强度,方向无误。**

### (d) 构念 = 学校孤独感 —— 成立,可加强

11. **六题(1–4 量表,Cronbach alpha = .82):**
    "I feel like an outsider (or left out of things) at school" / "I make friends easily at school"(反向)/ "I feel like I belong at school"(反向)/ "I feel awkward and out of place in my school" / "Other students seem to like me"(反向)/ "I feel lonely at school"。
12. **论文自认该构念是 PISA 学校归属感量表之反向:** "School loneliness (also known as school belonging or school connectedness in its inverse)"。**六题中仅一题字面提及 lonely,其余为归属/社交接纳,且限定于「在学校」场景,非 UCLA 等通用孤独量表。**
13. **论文自认不测抑郁(逐字):**
    > "Although the school loneliness measure does not directly assess depressive symptoms, it is positively correlated with a measure of negative affect including emotions linked to depression (such as feeling miserable and sad) and negatively correlated with positive affect and general life satisfaction."
14. **效标关联度中等偏弱(仅 2018、国内计算):** 与负性情感 r = .18 ~ .46;与正性情感 r = −.29 ~ −.47;与生活满意度 r = −.20 ~ −.45。

### (e) 测量不变性与韩国

15. **13 国名单逐字(含日、韩、法,计数无误):**
    > "The remaining 13 countries did not pass configural invariance (Brazil, Bulgaria, France, Hong Kong, **Iceland**, Indonesia, **Japan**, Luxembourg, Peru, Mexico, Russia, **South Korea**, and Thailand)."
    另两组:**完全不变性 12 国**(Australia, Canada, the Czech Republic, Finland, Hungary, **Iceland**, the Netherlands, New Zealand, Norway, Sweden, the United Kingdom, the United States);**仅组态+度量不变性 12 国**(Austria, Belgium, Chile, Denmark, Germany, Greece, Italy, Latvia, Poland, Portugal, Spain, Switzerland)。判定标准:CFI > 0.90 定 configural,ΔCFI ≤ 0.02 定 metric/scalar。
16. **一手内部错误(三票中两票独立发现,须加注):Iceland 同时出现在「12 国完全不变性」与「13 国未过组态不变性」两份名单中,而 Ireland(确为 37 国之一,见 Table 1 English-speaking 组)三份名单都未出现。** 12+12+13=37 只因冰岛被重复计数。**其中一处 "Iceland" 几乎肯定应为 "Ireland" 的笔误。此误不影响 13 这个计数,也不影响日/韩/法在列。** 另:冰岛与匈牙利被列入「跨五个时间点完全测量不变性」的 12 国,但两国 Table 1/2 的 2012 栏为空缺,实际只有四个时间点 —— 这是第二处内部矛盾。
17. **韩国「唯一未上升」只在连续均值口径成立 —— 三票一致:**
    - 正文逐字:"school loneliness declined in South Korea, **the only country of the 37 to not increase in loneliness**";Table 1 韩国:1.99(2000)/ 1.96(2003)/ 1.87(2012)/ 1.84(2015)/ 1.82(2018);**d(2012–2018) = −.10(95% CI −.14, −.05)**。
    - **但 Table 2 的二分「高孤独占比」口径下,韩国上升:** 27.29% / 23.83% / **18.79%(2012)** / 17.86% / **20.48%(2018)**,% diff 2012–2018 = **+8.99%**。
    **两张表相互抵触,「唯一未上升」不是跨指标稳健的结论。**
18. **韩国本身属于未过 configural invariance 的 13 国之一**,其趋势估计是全样本中可比性最弱的一档,**不宜当作强反例或强正例使用**。
19. **论文对「测量不变性会不会制造假上升」做了正面回应,且方向对自己不利地稳健 —— 必须并陈(否则对论文不公允):**
    > "The loneliness increase averaged **d = 0.43** from 2012 to 2018 among countries showing **full measurement invariance** on the loneliness scale, **d = 0.31** among countries with configural and metric invariance, and **d = 0.32** among countries **without** configural measurement invariance over time (weighted by population size). Thus, **the countries with the most stable measurement had the largest increase in loneliness.**"

### (f) 相关因素 —— 系数全对,分母与层级必须改

20. **Table 3(additive models,即每个指标单独与 Year 同时入模)逐字:**
    | 指标 | b | t | Std. b | 95% CI | n | k |
    |---|---|---|---|---|---|---|
    | Smartphone access | .0037*** | 3.72 | **.29** | [.0017, .0055] | **83** | **31** |
    | Internet use | .0753** | 2.97 | **.38** | [.0308, .1287] | **83** | **31** |
    | Unemployment | −.0057* | −2.54 | **−.18** | [−.0101, −.0008] | 179 | 37 |
    | Income inequality (GINI) | −.0001 | 0.45 | −.05 ns | | 123 | 26 |
    | GDP | .0001 | 0.47 | .05 ns | | 179 | 37 |
    | Total fertility rate | .0037 | 0.17 | .01 ns | | 179 | 37 |
    表注:"n's represent the total number of datapoints by k countries over time";"**Data on smartphone access and internet use are only available 2012–2018.**"
21. **分母不是 37 国 —— 三票一致的关键修正。** 手机/上网模型是 **83 个「国-年」数据点、k = 31 国**(该两变量仅 37 国中的 31 国采集、且仅 2012/2015/2018);失业/GDP/生育率 n=179, k=37;GINI n=123, k=26。
22. **层级必须写明:全部为国家-年度层面的生态学(ecological / group-level)关联,论文自陈 "we take an ecological approach",非个体层面剂量-反应。**
23. **"smartphone access" 的构念必须改:是家庭可及性单题** —— "Which of these is available for you to use at home? … Cell phone with Internet access",计入回答 "yes, and I use it" 的百分比。**既非个人持有率,也非使用时长。**
24. **失业率的负向关联不稳健:** 交互模型中 Std. b = −.05, t = −0.50,不显著;两个综合模型中均掉出。
25. **综合模型逐字:**
    > "In a model including smartphone access, unemployment, income inequality, GDP, total fertility rate, and year, only **smartphone access (Std. b = .26)** and **year (Std. b = 0.29)** were significant predictors of school loneliness. In a model including internet use, unemployment, GDP, income inequality, total fertility rate, and year, only **internet use (Std. b = .40)** was a significant predictor."
26. **时间与技术普及高度共线,须点明:** Year 本身在每个模型都是强预测项(Std. b .23–.48);在智能手机加性模型里 Year(.28)几乎等于智能手机(.29)。
27. **GINI 的「不显著」只对 additive 主效应成立:** interaction model 中 GINI × year 交互项显著(b = .0003, t = 2.31, p < .05)。(仅一票核到,见冲突裁决。)

### (g) 两轮均在 COVID 前 —— 成立

28. PISA 2012 与 2018 两轮按定义均在各自年份实施,均早于 2019-12 的 COVID-19。论文自身把疫情划在数据窗之外,逐字:
    > "events occurring after 2018, such as the COVID-19 pandemic and its associated impacts, may also impact trends in loneliness (Loades et al., 2020)."

### 必须并列的后续反证(引 (f) 时不可省)

29. **Freije SL, Rhew IC, Evans YN, Chan KCG, Enquobahrie DA. "Adolescent Loneliness Trends and Contextual Correlates Across 38 Countries From 2000 to 2022." *J Adolesc Health.* 2025 Oct;77(4):643-650. DOI 10.1016/j.jadohealth.2025.06.017, PMID 40838904。**
    独立团队、同一 PISA 六题学校孤独量表、扩展至 2022 轮、n = 1,267,476、15–16 岁、38 个 OECD 国。
    - **趋势侧支持 Twenge:** 2000–2012 变化不显著;2012–2015 每年 +0.045 分;2015–2022 每年 +0.017 分(上升延续但斜率放缓)。
    - **相关因素侧方向相反:** 国家层面每周上网时间每高 1 小时,对应孤独感每年**低** 0.012 分(95% CI −0.021, −0.003)。**与 Twenge 等 Table 3 的 internet use Std. b = +.38 方向相反。**
    **使用 (f) 支撑「智能手机/上网 → 孤独」时必须并列此反证。**
30. **另一条因果侧反证:** Vuorre M, Przybylski AK. "Global Well-Being and Mental Health in the Internet Age." *Clinical Psychological Science* 2023,DOI 10.1177/21677026231207791 —— 跨国分析未支持互联网普及导致福祉下降。本文的描述性趋势与该文的因果否定不直接冲突,但引 .29/.38 时应并列。
31. **构念旁证(非反证):** Jefferson R 等. "Adolescent loneliness across the world and its relation to school climate, national culture and academic performance." *BJEP* 2023,DOI 10.1111/bjep.12616,n=518,210、75 国,同用 PISA 学校孤独题组,重点归因于学校氛围、师生信任等**校级因素**。提示同一题组的国家间差异可由学校环境大量解释。

### 利益相关(须标注)

32. **未见资助/COI 声明:** OpenAlex funders/awards 为空数组;PubMed 无 CoiStatement;所取的两个版本 PDF(出版商 in-press 版与 Elsevier 接受稿)中均无 Declaration of competing interest / Funding / CRediT 段落。
33. **非财务利益相关须说明:** 第二作者 Jonathan Haidt 与第一作者 Jean Twenge 均为「智能手机—青少年心理健康」假说的主要公共倡导者与商业出版者(《iGen》《The Coddling of the American Mind》《The Anxious Generation》2024);**本文检验的正是其本人主张,属作者有既定立场的研究**;支撑性引用中至少 3 条为 Twenge 本人研究(Twenge et al., 2018;Twenge, Spitzberg & Campbell, 2019;Twenge & Spitzberg, 2020)。**不构成不当行为 —— 三票逐字核对未发现任何数字被错报 —— 但在权重上应与独立团队的复核(Freije 2025)并读。**

### 引用时的避坑清单(一手内部印刷错误)

34. Table 1 秘鲁 2015 年均值印为 **1.04 (.55)**,夹在 2012 年 1.88 与 2018 年 2.01 之间,极可能是 2.04 之误。
35. Table 2 印尼「高孤独比例」2012 = 14.51% → 2015 = 6.70% → 2018 = 24.15%,波动异常。
36. Table 1「Worldwide average」各轮 n 相加为 1,050,957,比论文所述总 n = 1,049,784 多 1,173。
37. Table 3 若干印刷疑误:smartphone 交互模型 Year 行 b = .0290 而 CI 为 [.0556, .2387](区间不含点估计);income inequality 加法行 b = −.0001 却 t = 0.45、Std. b = −.05(符号不一致);GDP 加法模型 GDP 行与 Year 行的 CI 疑似互换。**均不影响本论断组所引的三个 Std. b。**
38. 正文与 Table 4 的一处冲突:正文写 comprehensive model 中 "only smartphone access (Std. b = .26) and year (Std. b = 0.29)",而 Table 4 model A 列的是 smartphone .29 / year .27(两数疑似互换);Table 4 的 n = 61, k = 23。

---

## 修正记录(修正前→修正后)

| # | 修正前 | 修正后 |
|---|---|---|
| 1 | (c) 两处 "causation cannot be proven" | **五处**:三处完全逐字 + 两处 "cannot prove causation" 变体。论断低估了论文的自我限定强度 |
| 2 | (a) 36/37 国 2012–2018 上升 | 引语逐字无误,但**冰岛与匈牙利无 2012 基线**;有 2012 数据的只有 **35 国**,其中 34 国上升、1 国(韩国)下降 |
| 3 | (b) 全球高孤独 17.12%→30.86% | 数字逐字正确,须三处限定:①「高孤独」= ≥2.22,由 mixtools 混合模型估出的切点,**非临床阈值**;②**按各国人口规模加权**的平均,非原始受访者比例;③**该二分变量只用于描述统计,不进入任何模型** |
| 4 | (b)「nearly twice」 | 精确值 +80.26%(2012→2018);正文另有一处用 2000 作基线(+91.05%)。**引用必须指明基线年** |
| 5 | (b) n=1,049,784 与 2012→2018 对比并列 | 该 n 是**五轮合计**;分轮 2012=198,992、2018=264,506,合计约 463,498 |
| 6 | (b) 15–16 岁 | "15- and 16-year-olds **enrolled in school**";**67% 为 15 岁**;失学青少年不在抽样框 |
| 7 | (e) 韩国是唯一未上升国家 | **只在连续均值口径成立**(d = −.10);在同文 Table 2 的二分「高孤独占比」口径上韩国**上升 +8.99%**(18.79%→20.48%)。且韩国本身属未过 configural invariance 的 13 国 |
| 8 | (f) 分母 37 国 | 手机/上网模型 **n = 83 个国-年、k = 31 国**,数据仅 2012–2018;失业/GDP/生育率 n=179, k=37;GINI n=123, k=26 |
| 9 | (f) 读作个体层面剂量-反应 | 全部为**国家-年度层面生态学关联**,论文自陈 "we take an ecological approach" |
| 10 | (f) smartphone access = 智能手机拥有/使用 | 是**家庭可及性单题** —— "Which of these is available for you to use at home? … Cell phone with Internet access",计 "yes, and I use it" |
| 11 | (f) 失业率 Std.b = −.18(读作稳健) | **不稳健**:交互模型 Std. b = −.05(t = −0.50, ns);两个综合模型中均掉出 |
| 12 | (f) GINI 不显著 | 仅对 additive 主效应成立;interaction model 中 GINI × year 交互项显著(b=.0003, t=2.31, p<.05) |
| 13 | (f) 未提共线性 | Year 在每个模型都是强预测项(Std.b .23–.48);智能手机加性模型里 Year(.28)≈ smartphone(.29),时间与技术普及高度共线 |
| 14 | (e) 13 国名单(直接引用) | 计数与日/韩/法在列均无误,但须加注:**Iceland 在两份名单中重复出现,Ireland 三份名单皆缺,应为笔误** |
| 15 | 未提论文对不变性批评的正面回应 | 须补:**测量最稳的国家涨幅最大**(full invariance d=0.43 > configural+metric d=0.31 ≈ 无 configural d=0.32),这削弱了「上升系测量漂移」的替代解释 |
| 16 | (f) 单独支撑「上网 → 孤独」 | 必须并列 **Freije 2025**(J Adolesc Health,独立团队、同量表、扩到 2022):趋势侧支持,但**国家层面上网时长与孤独感增长呈负相关**(−0.012/年/小时,CI −0.021, −0.003),方向与 Std.b=+.38 相反 |

**票间冲突与裁决:**
- **「36 out of 37」与表格算不平这一发现:** 两票独立发现(冰岛/匈牙利 2012 缺格),第三票未提及。**裁决:采两票 —— 该发现有论文自家 Table 1/2 与表注 5 的直接支持,属可验证的硬事实,收进锁定口径第 3 条。**
- **GINI × year 交互项显著:** 仅一票核到,另两票未涉及、未反驳。**裁决:收录但标注为单票核对项**;成稿若不需要这一层细节可略,但不得写成「GINI 在所有设定下均不显著」。
- **全文取证通道:** 一票用 district8sonpm.org 镜像的出版商排版 in-press PDF(13 页);另两票用 scholar.archive.org / fatcat 取得 2021-08-04 存档的 Elsevier 接受稿 PDF(701,242 字节)。**两条独立通道对 Table 2、Table 3、六题、13 国名单、五处因果声明的读数完全一致 —— 这构成表格级数值的交叉验证。**
- **秘鲁 2015 = 1.04 的判读:** 两票均独立标为疑似 2.04 之误。一致。

---

## 未回溯项

1. **补充材料(Supplemental Tables 1–4、Supplemental Figs. 1–2)全部未取得**,托管于 ScienceDirect 附录且不可达。因此:
   (i) **无法判定三份国别名单中重复出现的 "Iceland" 究竟哪一处应为 "Ireland"**,只能定性为疑似印刷错误;
   (ii) **无法核实冰岛/匈牙利在缺 2012 数据的情况下如何被判为「跨五个时间点完全不变性」**;
   (iii) 各国 measurement invariance 的具体 CFI / ΔCFI 数值未取得。
2. **正式发表定稿版(93:257-269)未取得。** ScienceDirect 403、Wiley 402/403、archive.ph 与 web.archive.org 在部分环境被封、scispace 与 mojeek 403、Elsevier API 需密钥、fatcat 连接被拒、DuckDuckGo 触发 CAPTCHA(按规定未破解)。**本次全部逐字核对基于出版商 in-press 版与 Elsevier 接受稿(AIP)两个版本。** 摘要文本已与 PubMed / Crossref / OpenAlex / Semantic Scholar 记录逐字比对一致,正文数值极可能与终版相同,**但严格说表格数字未在定稿排版上目验,存在校样阶段被改动的残余风险**;第 37 条列出的 Table 3 印刷疑误是否已在定稿修正,亦无法确认。
3. **利益冲突 / 资助声明未能核到。** 两个可得版本中均无 Declaration of Competing Interest / Funding / CRediT 段落(grep funding / competing interest / conflict / declaration / acknowledg 均无命中);PubMed 无 CoiStatement;OpenAlex 无资助记录。**「作者是否申报了与主题相关的书籍/演讲收入」这一事实仍未解。**(第 33 条列出的非财务利益相关是可独立确认的公开事实,不受此影响。)
4. **PISA 2012 与 2018 主调查的具体实施月份窗口未从 OECD 一手文件核实**(oecd.org 403)。(g) 的判定依据是调查轮次年份定义、论文数据截至 2018 年,以及论文自身把 COVID 划在数据窗之外的表述,**而非 OECD 实地作业日历原件**。
5. **灰色文献层面的批评未覆盖。** 三票的 WebSearch 配额均在会话开始前耗尽(200/200),开放式反证检索改由 OpenAlex(cites:W3183254835,扫描全部 394–408 篇引用文献标题)与 Semantic Scholar 引文 API(100–333 条)完成 —— **已发表文献层面确认无 Comment、Reply、勘误或重分析**;但预印本、博客级方法学批评(如 Orben / Przybylski 等常见批评者的评论)未覆盖,不能排除存在未检出的批评。
6. **方法学附注(非缺口但须知悉):** 据一手方法节,聚合仅按 2018 年各国人口加权("we weighted by country population in 2018"),**文中未提及使用 PISA 自带的学生抽样权重 W_FSTUWT、复制权重(BRR)或 plausible values**;年份在各子集内以最早年份居中;样本为在校生、学校层面要求 ≥80% 应答率。

---

## 证据分级

- **书目与「无勘误/撤稿」:多源证实。** Crossref、PubMed、OpenAlex、Europe PMC、Semantic Scholar 五源一致;OpenAlex 全量引用文献扫描未见评论/再分析。
- **(a) 摘要引语:多源证实。** 经出版商 in-press PDF、Elsevier 接受稿 PDF、PubMed、OpenAlex abstract_inverted_index、Semantic Scholar 五处一致。
- **(a) 「36/37」的计数问题:单源已核(论文自家表格),但两票独立复现。** 属论文内部不一致,须加注。
- **(b)(e)(f) 表格级数值(Table 1/2/3、13 国名单、五处因果声明):多源证实。** 三票经**两条互相独立的全文通道**(district8sonpm.org 出版商 in-press 镜像 vs scholar.archive.org/fatcat 的 Elsevier 接受稿)逐字比对,读数完全一致。**可承重。**
- **(c) 五处因果保留声明:多源证实。** 三票独立同时发现同一结论。
- **(d) 构念:多源证实。** 六题、alpha、论文自认、效标相关系数,三票一致。
- **(f) 「智能手机/上网 → 孤独」的解读:方向存争。** 论文自身的生态学系数为正(.29/.38),但独立团队 Freije 2025(更长窗口、更多国家、国内变异模型)在同一量表上得到**相反符号**的上网—孤独关联;Vuorre & Przybylski 2023 亦未支持因果方向。**该系数不得单独承重,必须并列反证。**
- **(g) 两轮均在 COVID 前:单源已核(逻辑 + 论文自陈),OECD 一手日历未核。** 结论稳健,风险极低。
- **来源立场:非商业利益相关,但属作者自我检验(方向性利益一致)。** 无产业或倡导团体资助记录;两位主要作者以该命题出版商业畅销书。**三票逐字核对未发现任何数字被错报 —— 这是对该论文最有力的公允记录**;权重上应与独立复核并读。


---

# C19 最终判决:CORRECTED(3/3 票)

组题:挪威禁手机 Abrahamsson —— 全样本零效应逐字;女孩专科就诊 −29% vs 媒体 60%(须裁决);GPA 0.08 SD vs 外部数学 0.22 SD;霸凌 p=0.067/0.094;多数学校"禁"=上课静音;working paper 未同行评审。

三票独立取得同一份一手件(NHH Discussion Paper SAM 01/24, ISSN 0804-6824, 2024 年 2 月, 73 页),经 Wayback 快照下载,文件字节数 4,178,887 与 Sikt/NVA 官方仓库元数据登记值完全一致,CDX 显示 2024-03 至 2025-07 所有 200 快照 digest 相同(单一版本,无静默改版)。三票的数值核对结果彼此完全一致。

---

## 锁定口径(成稿必须用)

### 版本与发表状态(必须随每个数字出现)
- 论文:Sara Abrahamsson, "Smartphone Bans, Student Outcomes and Mental Health"。**已同行评审并发表**:Journal of Human Resources, published online before print **2026-03-11**, DOI **10.3368/jhr.0224-13403R2**(稿号后缀 R2 = 第二轮修回),University of Wisconsin Press,归入 Vol. 61 Supplement 1 (Jun 2026)。
- **本文所有数字均引自 NHH DP 01/2024(2024 年 2 月工作论文版),JHR 发表版付费墙未能逐字复核。凡引用具体点估计与 p 值,必须标注"2024 年工作论文版",不得标注为"JHR 2026 发表版"。**
- 发表版摘要逐字(与 DP 摘要口径不同,已重写并把零效应前置):"banning smartphones in middle schools has no average effect on education or mental health but masks important gender differences."
- DP 摘要逐字(口径较强,以女孩效应开篇):"banning smartphones significantly decreases the health care take-up for psychological symptoms and diseases among girls"。注意 take-up 通常读作 extensive margin,而正文明说 extensive margin 无效应 —— DP 摘要与正文本身存在张力。引用"原文措辞"时必须指明是哪个版本的哪一处。
- 作者单位:挪威公共卫生研究所(FHI)。资助:挪威研究理事会项目 262700、275800。无产业或倡导组织资助,COI 风险低。

### (a) 全样本零效应 —— 论断成立,逐字
- DP §5.1(p.18):"Analysis of the full sample indicates no effect of banning smartphones on student's likelihood of being treated, or on the intensity of treatment, related to psychological symptoms and diseases, as shown in Figure 3."
- 导言(p.3):"However, I find no effect on students' likelihood (extensive margin) of being diagnosed or treated by specialists or GPs"
- **关键限定:零效应同时覆盖两个边际**(是否就医 + 就医强度),不只其一。

### (b) 60% / 29% / 2–3 次 —— "三选一"是伪命题,三个数全部出自论文本身,指向不同结局
- **主口径(专科,intensive margin,女孩)逐字**(§5.1, p.19):"One year of exposure to a smartphone ban reduces the number of consultations by 0.98 visits (p-value 0.044), and three and four years of exposure lead to a reduction of 2–2.7 visits (p-value 0.011 and 0.008 respectively). Girls visit specialist care on average 3.4 times pretreatment, hence this is a significant reduction by almost 60% fewer specialist consultations three years post-ban."
- **GP 口径逐字**(§5.1):"girls exposed full-time in middle school to the smartphone ban have 0.22 (p-value 0.076) fewer consultations ... at their GP. This corresponds to a decline of about 29% in number of visits compared to pretreatment mean."
- **结论段把两者并列写死**(§6, p.26):"...by 60% and 29% relative to pretreatment mean, respectively" —— 60% = 专科,29% = GP,同一句内区分清楚。
- **显著性差别**:60% 对应 p=0.011 / 0.008(5% 水平显著);29% 对应 **p=0.076,5% 水平不显著**。引用 29% 不带此限定,等于把边缘结果当确证结果。
- **单位**:"2–3 次"是**整个初中阶段每人累计**,不是每人每年。导言逐字:"by about 2–3 visits **during middle school years** when exposed for full-time in middle school";结局定义(§3.2):"how many times a student visited a specialist during middle school years"。折成年化约 0.7 次/年。
- **导言与正文的内部出入**:导言写 "2–3",正文写 "2–2.7";60% 只对得上低端(2.0/3.4 = 58.8%)。
- **"almost 60%" 是论文作者本人的措辞**(导言与 §5.1 各一次),不是媒体发明或放大。但引用时必须钉死四重限定:**仅女孩 × 仅专科(ICD-10 "F" 码)× 仅就诊次数(intensive margin)× 禁令后第 3 年**。不可写成"心理问题就医下降 60%"或"心理问题人数下降 60%"—— 接受治疗的概率(extensive margin)是零效应。
- **分母极小**:处理前均值 3.4 次;Table 1 显示专科就诊概率仅 0.08–0.10。因此这是"同样比例的人在治疗、但每人诊次骤减"的长尾现象,论文未排除供给侧/转诊/就医行为解释。

### (c) 教育结局 —— 数字对,但事件年与人群限定必须补齐
- 逐字(§5.3, p.20–21):"Girls who started middle school one year after a ban was established gain on average 0.08 standard deviations in GPA, and 0.09 standard deviations in average grades set by teachers (p-values 0.064 and 0.05, respectively)."
- 逐字:"The gain in mathematics is 0.07 standard deviations (p-value 0.067) one year post-ban and increases to 0.22 standard deviations four years post-ban (p-value 0.014)."
- **0.08 SD 与 0.22 SD 不可并列比较**:前者是 GPA、禁令后 1 年入学队列;后者是外部阅卷数学、禁令后**第 4 年**;同一结局在 1 年后只有 0.07 SD。
- 均为**女孩子样本**。全样本 GPA、教师评分、升学轨道均无效应(脚注 11);挪威语与英语外部阅卷无效应(脚注 12);全样本仅数学外部考试有 "some positive effects"(Appendix Fig A4)。
- 升学轨道:女孩暴露 ≥2 年,进入学术高中概率上升 4–7 个百分点(处理前均值 49%,即相对增幅 8–14%)。
- **承重限定(必须写)**:论文原文明说男女系数差异不显著 —— "I cannot reject the null hypothesis that the coefficients between girls and boys are equal, in any of these results"。**用"女孩获益、男孩没有"做强对比,超出论文自己的统计支持。**

### (d) 霸凌 —— "不显著"过宽,须限定到"全样本 + 5% 水平"
- 逐字(§5.2, p.19–20):"the estimates show a significant decline in the incidents of bullying after two years of exposure. Bullying incidents decline by 0.25–0.35 standard deviation two to four years after a smartphone ban is implemented (p-values of 0.067 and 0.094)"
- 这两个 p 值**专属全样本**、禁令后第 2 与第 4 年。**论文自己称其为 "a significant decline"(即按 10% 水平)。**
- 分性别:女孩 2 年 0.30 SD(p=0.058);女孩全程暴露 3 年 0.42 SD(**p=0.039,5% 水平显著**,相当于 46% 降幅);男孩 4 年后 0.39 SD(43% 降幅,**正文未报告 p 值**)。
- 正确说法:全样本仅 10% 水平边缘显著,女孩全程暴露 3 年的估计在 5% 水平显著,男孩缺 p 值。
- **测量层级**:霸凌来自 Pupil Survey 的**学校层面聚合均值**并按年标准化(均值 0、SD 1),仅 431 所学校可链接(全挪威初中的 36%),不是个体层面测量。

### (e) "多数学校只是上课静音" —— 方向成立,补精确分母
- Figure 2(477 所可链接学校):"Silent mood during lectures" **249 所(52.2%,过半)**、"Handed in during lectures" 148、"Do not bring to school" 52、"Should not distract teaching" 25、未答 3。
- 问卷选项原文:(a) "Mobile phones are not allowed on school premises";(b) "...turned off or kept in 'mobile phone hotels'";(c) "Mobile phones are allowed, but should always be on silent mode and turned off during class"。
- 论文定义:严格 = "(1) ask students not to bring their phones to school or (2) collect phones before classes and store them in a 'mobile phone hotel'";宽松 = 课间可用但上课须静音。
- **论文内部口径不一致(须披露)**:正文两处称严格政策占 45%,但按 Figure 2 计算为 (52+148)/477 = 41.9%;且 §7.2 把 strict 描述为"早上上交、课间也拿不到",与 Figure 2 标签 "handed in during **lectures**" 措辞不符。

### 设计脆弱点(不在原论断内但承重,必须披露)
- **无 never-treated 对照组**,原文逐字:"Note that I do not use estimators discussed in (Roth et al., 2023) here as I do not have a group of schools that never introduced a smartphone ban and could serve as a control group." 即交错采纳(2010–2019 逐年铺开)+ TWFE 事件研究下,未做任何异质性处理效应稳健性检验。
- 全文无多重检验校正(无 Bonferroni / Romano–Wolf / FDR / q-value / 预注册),而关键 p 值密集落在 0.03–0.09 区间。
- 禁令实施年份由校长 2019 年**回溯自报**,最长回忆跨度近十年。脚注 17 自承宽松政策学校存在较明显的处理前趋势。
- **样本选择性(Table 1)**:2019 年向全挪威 1,187 所初中发问卷,2020-03 前回收 529 份(应答率 45%),可链接注册数据 477 所(40%),霸凌样本 431 所(36%)。应答校与非应答校系统性不同 —— 五年级测验分 −0.09 vs −0.14(t=−3.04)、GPA 0.01 vs −0.04、专科就诊概率 0.08 vs 0.12(t=5.51)、专科就诊次数 2.69 vs 4.97(t=3.55)、GP 就诊次数 0.84 vs 1.21、学校规模 57.66 vs 46.39。**样本系统性偏向"学业更好、心理就医更少、规模更大"的学校**,外部效度须打折。
- 数据:GP 用 KUHR(2006–2019, ICPC-2 "P" 开头),专科用 NPR(2009–2019, ICD-10 "F" 开头),按学年构造;基线 161,371 观测(49% 女生);数学外部考试 53,484 观测;覆盖 328/425 个市镇(77%)。

### 外部对冲证据(方向存争,建议主动披露)
- Henry Saffer, "Youth Mental Health and School Smartphone Bans: Early Evidence", NBER WP w35181, May 2026 —— 用 2016–2024 全国调查数据 + synthetic DiD 研究美国州级校园禁手机令,**未发现明确证据表明禁令减少屏幕时间或改善心理健康**。构成对本组外部效度的直接对冲(不同国家、不同设计、更粗的暴露测量)。
- 批评性引用检索(24 篇引用文献):World Journal of Pediatrics 2025 "Smartphone bans in schools remain unproven"(DOI 10.1007/s12519-025-00951-1)已下载全文核对,对本文仅一句 "An earlier study in Norway revealed only mixed and weak evidence in support of bans",**未**给出 29% 或任何再计算;BMJ 2025 "What is the evidence for school smartphone bans?"(DOI 10.1136/bmj.r1729)闭源未取。**未检出针对本文的正式勘误、撤稿或复制失败报告。**

---

## 修正记录(修正前 → 修正后)

1. **(f) 发表状态 —— 被一手直接推翻。** 修正前:"working paper,截至 2026-07 未同行评审"。修正后:**已同行评审并发表**(JHR, online first 2026-03-11, DOI 10.3368/jhr.0224-13403R2)。任何以"只是未评审的工作论文"为由的折价论证已失效。可保留的表述只有:"本文数字引自 2024 年工作论文版,已发表版未能逐字复核"。(3/3 票一致)

2. **(b) 主口径裁决 —— "60% vs 29% vs 2–3 次三选一"这个框架本身是错的。** 修正前:三选一,裁决哪个是主口径。修正后:三个数字全部出自论文,指向不同结局 —— 60% = 女孩·专科·就诊次数(p=0.011/0.008),29% = 女孩·GP·就诊次数(p=0.076),"2–3 次"是 60% 的绝对值表达。论文结论段把 60% 与 29% 并列写死。"媒体夸大 60%、批评者纠正为 29%"这一叙事在一手证据里不成立 —— **是换了结局,不是同一数字的两种算法**。(3/3 票一致)

3. **(b) 单位错误。** 修正前:"2–3 次/人年"。修正后:"2–3 次/人·整个初中三年累计"。折成年化仅约 0.7 次/年。(3/3 票一致)

4. **(b) "almost 60%" 的构念限定缺失。** 修正前:泛指"心理健康就医下降 60%"。修正后:必须带**女孩 × 专科 × 就诊次数(intensive margin) × 禁令后第 3 年**四重限定,且分母是处理前均值 3.4 次;extensive margin(是否曾就诊)全样本与女孩均为零效应。(3/3 票一致)

5. **(c) 0.08 SD 与 0.22 SD 不可并列。** 修正前:"GPA 0.08 SD vs 外部数学 0.22 SD"并列比较。修正后:两者是不同结局 + 不同事件年 + 不同显著性(0.08 SD 为 p=0.064 不显著;0.22 SD 为禁令后第 4 年 p=0.014;同结局第 1 年仅 0.07 SD, p=0.067)。且均为女孩子样本,全样本 GPA/教师评分/升学轨道无效应。(3/3 票一致)

6. **(c) 新增承重限定:男女系数差不显著。** 修正前:未提。修正后:原文 "I cannot reject the null hypothesis that the coefficients between girls and boys are equal, in any of these results" —— "女孩获益、男孩没有"的强对比超出论文自己的统计支持。(1/3 票发现;另两票未涉及此点,无反驳,按并集采纳)

7. **(d) 霸凌"不显著"过宽。** 修正前:"霸凌下降 p=0.067/0.094 不显著"。修正后:该口径只对**全样本**成立,且论文自己称之为 "a significant decline"(10% 水平);分性别后女孩全程暴露 3 年 0.42 SD 的 p=0.039 在 5% 水平显著。另须披露霸凌是学校层面聚合、仅 431 校。(3/3 票一致)

8. **(e) "多数只是上课静音"—— 方向成立,补分母并披露论文内部不一致。** 修正前:定性表述。修正后:249/477 = 52.2%;正文称严格政策 45% 但按 Figure 2 计算为 41.9%,且 §7.2 的严格政策描述与 Figure 2 标签措辞不符。(3/3 票一致)

9. **新增:识别策略脆弱点。** 修正前:未提。修正后:无 never-treated 对照组、未用交错采纳稳健估计量、无多重检验校正、禁令年份为校长回溯自报、应答校存在系统性选择偏误。(3/3 票均独立提出)

### 票间冲突与裁决
- **冲突:严格校 vs 宽松校的心理健康效应异质性方向。** 第 2 票称"心理健康效应在宽松学校反而更大(禁令后第四年专科就诊少 3.48 次 vs 严格校 2.3 次,p=0.036/0.068)",并据此推论"'只是静音所以是弱干预'与论文自身异质性结果方向相反";第 3 票则引论文逐字 "the effect between schools with a more lenient and strict policy is relatively similar"。
  - **裁决:采用论文自述逐字("relatively similar")作为承重表述。** 理由:逐字引语是硬证据,点估计的大小对比是二次计算且两组 p 值均在 0.036–0.068 的边缘带、区间必然重叠,不足以支撑"宽松校效应更大"这一方向性主张。
  - 两票在**教育效应**上无冲突且一致:教育效应主要来自严格校(严格校女孩 GPA +0.12 SD, p=0.032;数学第 4 年 +0.25 SD, p=0.028)。
  - 写作口径:**不得**写"宽松校心理健康效应更大";可写"教育效应集中在严格政策学校,心理健康效应在两类政策学校之间相对接近"。

---

## 未回溯项(不得承重或须标未验证)

1. **JHR 2026 发表版全文付费墙**(Unpaywall is_oa=false,无任何 OA 镜像/仓储版本,.full/.figures-only/.full.pdf 均返回订阅页)。无法核实 0.98 / 2–2.7 次、almost 60%、29%、0.08 SD、0.22 SD、霸凌 p=0.067/0.094 这些点估计在两轮修回后是否被改动。**已知的唯一确定变化是摘要被重写(前置"no average effect")**,强烈提示审稿意见正压在论断 (a) 这一点上,因此必须假定正文数字**可能**已变。→ **所有数字必须标注"NHH DP 01/2024 版",不得标为发表版。**(3/3 票一致标记)

2. **"处理前专科就诊均值 3.4 次(女孩)"是条件均值还是非条件均值,论文未明示。** 论文正文行文中出现该数,但任何表格中都没有女孩分性别的处理前均值,也未说明是否条件于"至少一次就诊"。据 Table 1(学校层面全样本)专科就诊概率仅 0.08–0.10 而次数均值 2.69–4.97 推断为非条件均值、由长尾驱动 —— 但若为非条件均值,则就诊者人均需达 30–50 次,数值上不太自洽。**这直接决定 "almost 60%" 的分母是"全体女孩"还是"进入专科系统的那约一成女孩"。无法从一手件裁决。**(3/3 票一致标记为未决)

3. **Boston Globe 原文未取得**(WebSearch 配额 200/200 耗尽;Wayback CDX 对 bostonglobe.com 覆盖不完整,检索无命中)。因此无法逐字比对该报是否把 "almost 60%" 正确挂在"女孩 × 专科 × 就诊次数 × 禁令后第 3 年"这一结局上。**可确认的只有:"almost 60%" 这一措辞本身出自论文而非媒体发明。**媒体是否漏掉限定语,未核实 —— 不得写"媒体夸大"或"媒体误报"。(3/3 票一致)

4. **"批评者引约 29%"的具体出处与批评者身份未定位到一手。** 已排除 World J Pediatr 2025(该文只用 "mixed and weak evidence" 定性,未引 29%)。若该批评来自播客/Substack 等非索引渠道,在无 WebSearch 条件下无法回溯。**可确认的是 29% 本身就是论文自己的 GP 口径数字,不是杜撰。**(3/3 票一致)

5. **DP 正文未报告男孩霸凌下降 0.39 SD 的 p 值**(女孩的 0.058/0.039 都给了),而结论段仍并列断言 "bullying decreases by 0.42 and 0.39 of a standard deviation for girls and boys, respectively"。该数是否达常规显著水平,文本层面无一手依据(只能目测 Figure 5 Panel B 误差棒)。→ **引用男孩霸凌数字须标"论文未报告显著性"。**

6. **SSRN 版本(SSRN 4735240)页面返回 403**,无法核对 SSRN 版与 NHH DP 版是否逐字一致或有后续修订版。

7. **勘误/更正检索非穷尽**(WebSearch 配额耗尽)。"无 erratum" 是"未发现"而非"已确认不存在"。

---

## 证据分级

**单源已核(一手逐字,字节级校验,三票互证)—— 但外部效度方向存争,且版本存在未核风险。**

- **一手强度高**:三票各自独立取得同一份 NHH DP 01/2024 PDF,均经 Wayback 存档下载并与 Sikt/NVA 官方仓库元数据(4,178,887 字节、73 页、NFR 资助号 262700/275800)交叉校验,CDX digest 一致确认无静默改版。三票的所有数值核对结果完全一致,无一处数字冲突。发表状态由 Crossref + OpenAlex + JHR 站点 citation_* 元数据三路确认。
- **降级因素一(版本)**:承载数字的是工作论文版,已发表版付费墙不可核且摘要已被明显重写 → 数字层必须带版本戳,不能当作"已发表的定论数字"引用。
- **降级因素二(设计)**:无 never-treated 对照组、交错采纳下未用稳健估计量、无多重检验校正而关键 p 值密集落在 0.03–0.09、应答校系统性选择偏误、禁令年份校长回溯自报。这是一项**方法学脆弱的准实验单点证据**,不是稳健因果证据。
- **降级因素三(方向存争)**:NBER WP w35181(Saffer 2026,美国州级禁令,synthetic DiD)未发现禁令改善心理健康的明确证据,与本文方向相反。校园禁手机的跨国证据基线是**存争**而非**收敛**。
- **无利益冲突**:作者为 FHI 公共卫生机构研究者,公共经费资助,无产业或倡导组织资金。
- **承重建议**:可作为"单一国家、单项准实验的正向信号"引用,**不可作为"校园禁手机有效"的定论证据**;凡引用 60%,必须四重限定 + 版本戳 + 分母说明,并同时给出全样本零效应这一同源事实。


---

# C20 最终判决:CORRECTED(3/3 票)

组题:英格兰 SMART Schools —— WEMWBS adj diff −0.48 [−2.05,1.06] p=0.62;在校用机 −0.67h/社媒 −0.54h 但全天总量无差异;横断设计;宽松组 9/10 已禁课堂、限制组仅 4/20 锁袋(Haidt 方批评与论文自述一致性)。

三票均取得开放获取一手全文(PMC / Europe PMC fullTextXML / PubMed XML 三镜像),Table 1 与 Table 3 逐字核对结果完全一致。第 2、3 票另取得 After Babel 批评原文并逐字比对。

---

## 锁定口径(成稿必须用)

### 出处
- Goodyear VA, Randhawa A, et al. "School phone policies and their association with mental wellbeing, phone use, and social media use (SMART Schools): a cross-sectional observational study." **Lancet Reg Health Eur. 2025;51:101211**, 在线 2025-02-04。DOI **10.1016/j.lanepe.2025.101211**,PMID 40213498,PMCID PMC11984610。ISRCTN77948572。协议论文 PMID 37407051 / PMC10335462 (BMJ Open 2023)。
- 出版商站(thelancet.com / sciencedirect.com)对自动请求返回 403;逐字核对以 **PMC 开放获取版 + Europe PMC 全文 XML + PubMed XML** 三镜像为准,内容一致。
- 无勘误/撤稿:Crossref update-to 与 updated-by 均为 None;PubMed XML 无 ErratumIn/RetractionIn/CommentIn 节点;Europe PMC 无关联更正记录(截至 2026-07-27)。

### (a) 设计与样本
- 逐字:"We conducted a cross-sectional observational study with adolescents from 30 English secondary schools, comprising 20 with restrictive (recreational phone use is not permitted) and 10 with permissive (recreational phone use is permitted) policies."
- 逐字:"We recruited 1227 participants (age 12–15) across 30 schools."
- **关键:两组的分界线是"娱乐性(recreational)使用",不是"课堂使用"。**
- **分母细化**:1,227 为招募数;主要结局 WEMWBS 的**分析样本为 1,223**(限制校 817 / 宽松校 406)。学生层面应答率:限制校 75.93%、宽松校 71.90%。

### (b) 主要结局 WEMWBS —— 逐字成立
- 逐字:"Mean WEMWBS score was 47 (SD = 9) with no evidence of a difference between groups (adjusted mean difference −0.48, 95% CI −2.05 to 1.06, p = 0.62)."
- 效应量语境:WEMWBS 量程 14–70、SD=9,故 −0.48 ≈ 0.05 个标准差;Table 3 给出标准化效应量 **−0.05 (−0.23 to 0.12)**。
- **必须补的口径:−0.48 是"调整后"值。未调整 WEMWBS 差值为 −1.62 (95% CI −3.32 to 0.07, p=0.072),方向是"限制校幸福感更低"且接近显著。**
- WEMWBS 取相隔 4–8 周两次测量的平均;仅用第一次的敏感性分析同样无显著差异。

### (c) 使用时长 —— 在校显著下降、校外无差异
- 逐字:"Adolescents attending schools with restrictive, compared to permissive policies had lower phone (adjusted mean difference −0.67 h, 95% CI −0.92 to −0.43, p = 0.00024) and social media time (adjusted mean difference −0.54 h, 95% CI −0.74 to −0.36, p = 0.00018) during school time, but there was no evidence for differences when comparing usage time on weekdays or weekends."
- **时间窗不止工作日/周末两档,还有"整周"**,三者调整后均无差异:
  - 手机:工作日 0.01 [−0.49, 0.54] p=0.96;周末日 0.58 [−0.32, 1.50] p=0.31;整周 1.46 [−2.82, 5.85] p=0.59
  - 社媒:工作日 0.25 [−0.18, 0.69] p=0.33;周末日 0.61 [−0.12, 1.36] p=0.19;整周 2.66 [−0.67, 6.08] p=0.22
- **方向性(须写明)**:所有校外点估计方向都是**限制校学生用得更多**,即"无差异"是零效应而非"略低"。
- **未调整模型中限制校校外用量显著更高**:社媒工作日 0.63 (0.24–1.02, p=0.0043)、社媒周末日 1.13 (0.44–1.81, p=0.0032)、社媒整周 5.50 (2.24–8.76, p=0.0023)、屏幕时间周末日 0.98 (0.12–1.83, p=0.033);调整后全部归零。论文原文:"the median use duration in restrictive schools was greater"。
- **测量口径**:−0.67h / −0.54h 来自**问卷回忆式自报**,不是设备客观记录。论文明确因准确性问题弃用了从 iOS Screentime / Android Digital Wellbeing 转录的手机应用数据(缺失率高、输入错误,近三分之一参与者报告的社媒时长竟高于总手机时长)。

### (d) 结论句 —— 必须连引,不可截断
- Interpretation 全文逐字:**"There is no evidence that restrictive school policies are associated with overall phone and social media use or better mental wellbeing in adolescents. The findings do not provide evidence to support the use of school policies that prohibit phone use during the school day in their current form, and indicate that these policies require further development."**
- **关键词是 "overall"(总量),不是在校期间。**截断引用会让读者误以为论文否定了在校时段的效果,而在校时段效果恰恰是显著的。
- 作者定位是"**现有形态**的政策无效、需进一步发展",不是"校园禁令一律无用"。

### (e) 政策落地强度 —— Table 1 原始分层(裁决 Haidt 批评点 1 的唯一一手依据)
逐字分类:
- **宽松校 10 所**:类别 1「Phones are allowed to be used at any time during the school day」= **1 所**;类别 2「Phones are allowed to be used at school during certain times/in certain areas」= **9 所**,细分 (2a) 午餐与课间 7 所、(2b) 指定区域 2 所。
- **限制校 20 所**:类别 3「Phones are not allowed to be used at school but are accessible to pupils」= **16 所**(Phones must be kept off inside bags);类别 4「Phones are not allowed to be used at school and are inaccessible to pupils」= **4 所**,细分 (4a) 储物柜 1 所、(4b) 收纳袋/pouch 1 所、(4c) 上交学校前台 1 所、(4d) 不许带入校园 1 所。
- **因此:真正用"锁袋或储物柜"的只有 2 所;"手机对学生不可取用"的是 4 所。**
- 论文对限制型的定义原文:"Phones were not allowed to be used during the school day for recreational purposes, and were required to be kept off inside bags, stored in lockers, kept in a pouch, handed into the school reception, or phones were not allowed onto the school premises altogether."

### (e-2) Haidt 方批评 —— 原文已定位并逐字核对,数字层与论文 Table 1 完全吻合
- 出处:Jon Haidt、Zach Rausch、Alec McClean,**"Flaws in a Recent Lancet Study on Phone Use in Schools", After Babel, 2025-02-13**, https://www.afterbabel.com/p/lancet-study-flaws
- 五个批评点:①宽松校并不很宽松/多数限制校并非无手机;②因果论断无依据;③学业结果依赖单一二元评分;④客观手机数据采集失败;⑤屏幕与社媒时长估计异常。**待验论断说的两条事实同属 Problem #1,不是"批评点 1-2"。**
- Problem #1 逐字:"Of the ten permissive schools, nine had classroom ban policies, and only one allowed phone use at any time throughout the school day." / "only four of the twenty restrictive schools had policies that made phones truly inaccessible. One used locked pouches, one used phone lockers, one required that students hand in their phones to the front office, and one did not allow phones on the school premises. The other 16 schools seem to have had a 'backpack policy'"
- 结论句:"In reality, the study was primarily a comparison of schools with a classroom ban versus schools that let students keep their phones with them at all times, in their backpacks."
- **裁定:After Babel 在这两点上数字准确,没有编造。**

### (e-3) 论文的预设反制 —— 引用该争议时不得略去
- Results 逐字:**"In the sensitivity analysis using only restrictive schools where phones were inaccessible to pupils, there were no significant differences with permissive schools across all outcomes"**
- After Babel 自己也承认了这点("the authors did re-run some of the analyses, limiting the restrictive schools to the four truly phone-free schools, and they report that it did not change the results"),但辩称对照组仍非真正宽松。

### (f) 结局清单与因果限定
- **WEMWBS 是唯一主结局;焦虑与抑郁是预先登记的次要结局,已测已报,同为零效应:**
  - 焦虑 (GAD-7):adjusted mean difference **0.10 [95% CI −0.76, 0.97], p=0.84**
  - 抑郁 (PHQ-9):adjusted mean difference **−0.04 [95% CI −0.98, 0.92], p=0.94**
- Methods 逐字:"Secondary health and education-related outcomes assessed in pupil participants were: anxiety, depression, physical activity, sleep, classroom behaviour, attainment, and problematic social media use."
- Discussion 逐字:"we observed no differences in adolescents' self-reported mental wellbeing, anxiety, depression, problematic social media use, and their motives for using social media."
- 其余次要结局调整后亦均为零:问题性社媒使用 0.5 (−2.6 to 3.53, p=0.80)、睡眠时长 1.27 分钟 (−8.67 to 10.12, p=0.82)、MVPA 1.78 (−2.59 to 6.09, p=0.46)、课堂扰乱 (PBQ) 0.06 (−0.57 to 0.68, p=0.88)、英语/数学低于目标 OR 1.45 (0.85–2.47, p=0.18) / 1.01 (0.45–2.27, p=0.98)。
- 因果限定逐字:"A limitation is that the study design is cross sectional which makes it difficult to draw conclusions about causality and reverse causality cannot be ruled out. Furthermore, there is a risk of selection bias and unmeasured confounding in this study."(**是"difficult to draw conclusions about causality"+"反向因果无法排除",不是"不支持任何方向的因果结论"**)
- 论文另承认宽松校中选择性学校、单性别学校、世俗学校占比更高。

### 反向读风险(必须主动披露,否则属误读)
- 论文自身报告了明确的剂量-反应关联:"Increases in smartphone and social media time were associated with reduced mental wellbeing on a weekday, on a weekend day, and across a week";"Increases in smartphone and social media time were associated with increases in anxiety, depression and problematic social media use across all measurement periods.";"our data also provide evidence to support claims of adverse consequences associated with increased overall phone/social media use"
- **该研究的零结果是针对"学校政策",不是针对"手机使用本身"。把它引作"屏幕使用无害"的证据属误读。**

### 利益相关(双向核查)
- 资助:英国 NIHR Public Health Research Programme(**NIHR131396**),款项付至伯明翰大学;论文声明资助方未参与设计/分析/撰写/投稿决定。AS 另持 NIHR 资助并受 NIHR 伯明翰生物医学研究中心支持,HA 持 Wellcome Trust 学校与职场福祉投资研究奖。其余作者声明无竞争性利益。**未发现手机产业/平台方资助,亦未发现禁令倡导方资助 —— 两个方向的明显利益冲突都不存在。**
- 对立面 After Babel 是 Haidt《The Anxious Generation》的配套 Substack,对"校园禁手机有效"有明确先验立场与著作利益;**但其两条事实陈述经一手 Table 1 验证属实,不因立场而失真。**

---

## 修正记录(修正前 → 修正后)

1. **(f) 前半句被一手推翻。** 修正前:"结局是幸福感量表,非抑郁/焦虑"(用于限定该研究适用范围)。修正后:WEMWBS 只是**主**结局;焦虑(GAD-7)与抑郁(PHQ-9)是**协议论文预先登记的次要结局,实际测了也报了**,同为零效应(0.10, p=0.84 / −0.04, p=0.94)。**"没测抑郁/焦虑"这个限定站不住;正确的说法反而更强:"连抑郁/焦虑次要结局也是零。"** 协议论文(PMID 37407051)明载 GAD-7 与 PHQ-9,证实非事后添加。(3/3 票一致)

2. **(e) "20 所限制校中仅 4 所用锁袋/储物柜"—— 数字对但措辞失真。** 修正前:4 所用锁袋/储物柜。修正后:那 4 所是「手机不可**取用**」这一上位类别,细分为储物柜 1 所、锁袋 1 所、上交前台 1 所、禁止带入校园 1 所 —— **真正用锁袋或储物柜的只有 2 所**。其余 16 所仅要求关机放书包内,手机仍在学生身上。**失真是二次转述引入的:After Babel 原文写的是 "made phones truly inaccessible" 并逐一列出四种方式,与论文完全一致。**(3/3 票一致)

3. **(e) "10 所宽松校中 9 所已禁课堂用机(与论文自述一致)"—— 事实方向成立,但归属错。** 修正前:称其为"论文自述"。修正后:论文 Table 1 原词是「Phones are allowed to be used at school during certain times/in certain areas」9 所(午餐课间 7、指定区域 2),另 1 所任何时间可用;**论文全文从未出现 "classroom ban" 字样**,"nine had classroom ban policies" 是 After Babel 的概括。其中"指定区域"那 2 所按空间而非课时定义,归入"禁课堂用机"属合理推断而非论文明写。**应表述为"9/10 宽松校不允许全天自由使用手机",不宜说"论文自述 9 校已禁课堂用机"。**(3/3 票一致)

4. **(e) 批评点归属错位。** 修正前:"Haidt 方批评点 1-2"。修正后:这两条事实同属 After Babel 的 **Problem #1(政策落地强度)**;Problem #2 是另一议题(作者时而混同相关与因果)。(1/3 票发现,另两票未涉及,按并集采纳)

5. **(e) 遗漏关键反制,必须补入。** 修正前:只呈现"仅 4 所"。修正后:论文已做只保留 4 所"不可取用"学校的敏感性分析,**所有结局仍无显著差异**;After Babel 自己也承认这点。**引用该争议时不应只呈现"仅 4 所"而略去该敏感性分析。**(1/3 票发现;第 3 票另在 unresolved 中指出该敏感性分析的具体点估计与效能未见 —— 两者并存,见未回溯项)

6. **(d) 引语须补全限定语。** 修正前:截断为 "There is no evidence that restrictive school policies are associated with..."。修正后:完整句含 **"overall"** —— "...associated with **overall** phone and social media use or better mental wellbeing in adolescents.";并应连引下一句("in their current form... require further development")。(3/3 票一致)

7. **(c) "工作日全天/周末总量无差异"—— 须补第三个时间窗并写明方向。** 修正前:两档。修正后:工作日、周末日、**整周**三者调整后均无差异;且所有点估计方向都是限制校用得更多;未调整模型中限制校校外社媒用量**显著更高**(整周 5.50, p=0.0023)。(3/3 票一致,三票各补一部分)

8. **(c) 测量口径须标注。** 修正前:"在校手机 −0.67h、社媒 −0.54h"。修正后:该数字来自**问卷回忆式自报**,论文因准确性问题弃用了 iOS Screentime / Android Digital Wellbeing 转录数据。这正是 After Babel 批评点 4 的事实基础。(1/3 票发现,无反驳,采纳)

9. **(a) 分母需细化。** 修正前:N=1,227。修正后:1,227 为招募数,主要结局分析样本 1,223(限制 817 / 宽松 406);应答率 75.93% / 71.90%。(1/3 票发现,采纳)

10. **(b) −0.48 是调整后值,须补未调整值。** 修正前:只给 −0.48。修正后:未调整 WEMWBS 差值 −1.62 [−3.32, 0.07] p=0.072,方向为限制校更低且接近显著。(1/3 票发现,采纳)

11. **(f) 后半句措辞略强于原文。** 修正前:"横断设计不支持任何方向的因果结论"。修正后:原文为 "difficult to draw conclusions about causality and reverse causality cannot be ruled out" —— 方向一致但比"不支持任何方向的因果结论"软。(1/3 票发现,采纳)

12. **量表缩写:PAQ-9 → PHQ-9。** 三票均在 PMC 渲染的 Table 3 表注中读到 "PAQ-9"。裁定为 **PHQ-9(Patient Health Questionnaire-9)的排版/抓取讹误**,依据:协议论文(BMJ Open 2023)明载 "Patient Health Questionnaire (PHQ-9)";Kelly 该量表在文献中的通用性;论文全文无 "PHQ" 字样。**成稿写 PHQ-9。**数值 −0.04 [−0.98, 0.92] p=0.94 不受影响。(3/3 票一致标记)

### 票间冲突与裁决
- **冲突:Haidt 方批评原文是否可回溯。** 第 1 票称 afterbabel.com 多个候选 slug 均 404、web.archive.org 被封禁、WebSearch 耗尽,故把"这两点确系 Haidt 方批评"列为未核实。第 2、3 票均直接取得 https://www.afterbabel.com/p/lancet-study-flaws 原始 HTML(第 3 票记录 278KB)并逐字引出五点标题与 Problem #1 全文。
  - **裁决:采信第 2、3 票。**理由:两票独立取得同一 URL 的原文并给出彼此一致的逐字引语,属更硬的一手证据;第 1 票是取证失败而非发现反证。**Haidt 方批评可具名归因,不必降级为"针对该研究的常见批评"。**

---

## 未回溯项(不得承重或须标未验证)

1. **补充材料(Supplementary Figures and Tables, Appendix A)未逐份下载核对。** 因此:(i) **只含 4 所"不可取用"学校的敏感性分析的具体点估计、CI 与样本量未见** —— 正文仅给出 "no significant differences across all outcomes" 的定性表述,检验效能未知,而这恰是 After Babel 反驳该敏感性分析的着力点;(ii) 该子分析的实际学生 N 未知。→ **引用该敏感性分析时须标注"论文仅给定性表述,效能未知"。**

2. **After Babel 把限制型学校的定义引作 "Required phones to be inaccessible to pupils",该措辞未在论文正文或 Table 1 中定位到**(正文定义更宽:"required to be kept off inside bags, stored in lockers, kept in a pouch, handed into the school reception, or phones were not allowed onto the school premises altogether")。可能出自 Table 2 或补充材料某一行,未能定位确切出处。→ **若该定义确不存在于论文中,则 After Babel"定义看起来很好但实际只有 4 所"的修辞前提需打折。此点未决,不得据以指控 After Babel 曲解。**

3. **出版商版全文(thelancet.com / sciencedirect.com)对三票均返回 HTTP 403。**逐字核对全部依赖 PMC / Europe PMC / PubMed 三个 NLM 系镜像,未取得独立于 NLM 体系的第三个镜像(如作者主页 PDF)。排版差异(表注、supplementary)无法完全排除。

4. **论文未逐字说明"所有学校(含宽松组)课堂内一律禁用手机"这一跨组共同基线。** 该基线是评估"限制组与宽松组真实对比度有多大"的关键,但一手文本只给了 Table 1 分类,无显式陈述。→ **不得写"两组的唯一差别是课间与午餐"。**

5. **作者是否曾公开回应 Haidt 的五点批评,未能核实。** 三票 WebSearch 配额均已耗尽(200/200),无法做开放式反向引证检索。已用 Crossref / PubMed / Europe PMC 三处确认无正式勘误与 Comment-in,但非索引渠道(预印本、博客学界回应、Lancet 在线评论区/rapid response)可能存在遗漏。→ **"学界无实质反驳"只能写作"截至 2026-07-27 未见正式勘误或期刊内 correspondence"。**

6. 后续同队列产出为独立新论文而非更正:PMID 41667290(BMJ Ment Health 2026 卫生经济学分析)、PMID 41855785(Soc Sci Med 2026 定性比较个案研究)。未纳入本次核对。

---

## 证据分级

**多源证实。**

- **论文一手**:开放获取,三票经 PMC 网页版、Europe PMC 全文 XML、PubMed XML 三条独立路径取得,Table 1 / Table 3 / Interpretation / Limitations 的逐字与数值三票**完全一致,无一处冲突**。Crossref + PubMed + Europe PMC 三处确认无勘误撤稿。协议论文(BMJ Open 2023)提供了预注册结局的第四条独立佐证。
- **批评方一手**:After Babel 原文经两票独立取得并逐字比对,其 Problem #1 的两组数字与论文 Table 1 完全吻合 —— **这是一个罕见的"立场对立双方在事实层不冲突"的案例**,争的是解释(对比度够不够大),不是数字。
- **无利益冲突**:资助为英国 NIHR 公共卫生公共经费,双向核查均未发现产业或倡导方资金。批评方 After Babel 有明确著作与立场利益,须披露,但不影响其已核实的事实陈述。
- **证据位阶的关键限定(必须随引用出现)**:这是**横断观察研究**,论文自陈难以支持因果推论且无法排除反向因果、存在选择偏倚与未测量混杂。它能承重的是"**现有形态的英格兰校园手机政策与更好的心理健康无关联,且不改变全天总使用量**",**不能**承重"校园禁令一律无效",更**不能**承重"手机使用无害"—— 同一篇论文里用量与结局的剂量-反应关联是显著的。


---

# C21 最终判决:CORRECTED(3/3 票)

组题:澳大利亚禁令 —— 2025-12-10 生效、全球首个;Meta 关停约 50 万账号;3 个月评估 >85% 16 岁以下仍在用;"账号 vs 使用"构念差;12-13 岁几乎无变化。

**票质说明**:第 1 票只提交了一条 (a) 生效日修正,且该条本身在书写中途自我更正,evidence_notes 与 unresolved 均为"占位",实质证据为零。**实质证据来自第 2、3 票**,两票均独立从 legislation.gov.au 官方端点直取法条正本、从 Europe PMC / Wayback 取得 BMJ 全文,结论方向一致。三票在唯一重合点(生效日拆分)上一致。

---

## 锁定口径(成稿必须用)

### (a1) 生效日 —— 必须拆成两层
- 法案:**Online Safety Amendment (Social Media Minimum Age) Act 2024, No. 127, 2024**(登记号 C2024A00127)。
- **法案本身**:2024-12-10 御准,**2024-12-11 全部条款生效**。s 2 生效表逐字:"1. The whole of this Act | The day after this Act receives the Royal Assent. | **11 December 2024**"
- **承载禁令的实体义务 s 63D**:由 s 63E 延后生效,须由部长以 notifiable instrument 指定日期。指定件为 **Online Safety (Day of Effect of Social Media Minimum Age) Instrument 2025 (F2025N00628)**,通信部长 Anika Wells **2025-07-29 签署**、2025-07-30 注册,逐字:"I, Anika Wells, Minister for Communications, acting under subsection 63E(2) of the Online Safety Act 2021, specify **10 December 2025** as the day section 63D of that Act takes effect."
- **成稿表述:2025-12-10 是"s 63D 义务生效日",不是"该法生效日"。两者差近一年。**
- s 63E(3):"The specified day must not be later than 12 months after the day this section commences."
- s 63E(4):义务及于**已存在的账号**,无 grandfathering。

### (a2) 义务条文与定义 —— 逐字
- s 63D:"**63D Civil penalty for failing to take reasonable steps to prevent age-restricted users having accounts** — A provider of an age-restricted social media platform must take reasonable steps to prevent age-restricted users having accounts with the age-restricted social media platform. **Civil penalty: 30,000 penalty units.**"
- s 5 定义:"age-restricted user means an Australian child who has not reached 16 years."
- **注意:义务是"take reasonable steps to prevent … having accounts",不是"禁止未成年人访问内容"。**

### (a3) 罚款上限 —— 法条里没有澳元数字,49.5m 是推算值且已过期
- 法条只写 "30,000 penalty units"。
- 法人乘数:Regulatory Powers (Standard Provisions) Act 2014 s 82(5)(a) 逐字:"The pecuniary penalty must not be more than: (a) if the person is a body corporate—**5 times** the pecuniary penalty specified for the civil penalty provision" → 150,000 penalty units。
- Penalty unit 基数:Crimes Act 1914 s 4AA(1) "penalty unit means the amount of **$330** (subject to indexation under subsection (3))";s 4AA(3) 指数化日为 2026-07-01 及其后每第三个 7 月 1 日。
- **150,000 × $330 = AUD 49.5m,仅对 2025-12-10 至 2026-06-30 期间成立。**
- **2026-07-01 起 penalty unit 指数化至 $364**(Crimes (Amount of a Penalty Unit) Instrument 2026, F2026N00424, 2026-06-15 签署, s 5:"the amount of a penalty unit is $364")→ **150,000 × $364 = AUD 54.6m**。
- eSafety 现行 FAQ 措辞已同步改为:"court-imposed fines of up to 150,000 penalty units for corporations – **currently equivalent to a total of $54.6 million AUD**"(旧版为 $49.5 million)。
- 非法人主体上限只有 30,000 PU(当时 $9.9m,现 $10.92m)。
- **成稿必须带时间戳:写 $49.5m 须注明"2025-12 至 2026-06 币值";写当前值用 $54.6m(2026-07 起)。**

### (a4) 父母同意 —— 是"法条不存在该通道",不是"法条明文否定"
- 对 C2024A00127 全文 grep "parent" / "guardian":**零命中**;s 63D 为无条件义务,无任何同意例外。
- 议会图书馆 Bills Digest 25bd039 逐字:"The civil penalty provision at the centre of the Bill states that providers of ARSMPs must take reasonable step to prevent age restricted users from having accounts. It does not otherwise place any obligations on ARSMPs to prohibit people under the age of 16 from accessing content on their platforms. **There is no civil penalty for parents or other people who provide access to ARSMPs for children under 16.**"
- eSafety FAQ 逐字:"There are no penalties for under-16s who access an age-restricted social media platform, or for their parents or carers." / "Parents and carers don't have to say 'yes' or 'no' to social media accounts, instead they can say 'not yet'."
- **成稿表述:"法律不设父母同意通道,义务与责任全部落在平台"。不要写成"法条明文规定父母同意无效"。**

### (a5) "全球首个" —— 成立但必须带限定语
- BMJ 论文自述:"a world first national policy";eSafety:"world-first social media age restrictions" / "the world-leading SMMA";同刊 Livingstone 社论(BMJ 2026;394:e100148)口径一致。
- **反例限定语**:法国 2023 年已立法设 15 岁数字成年门槛(Loi n° 2023-566 du 7 juillet 2023),**以父母同意为通道且据称未真正实施**;BMJ 引言亦记载法国国民议会通过 under-15 禁令 "with provisions for parental consent"。另有 Slovenia、Poland、Spain、Denmark、Malaysia 在议。
- **准确说法:"首个在国家层面、以平台义务落地、不设父母同意通道、且已实际施行的社媒最低年龄制度"。**

### (a6) 覆盖面 —— 不是"禁社媒",是禁 10 个被指定平台
- eSafety 认定的 **10 个 age-restricted social media platform**:Facebook、Instagram、Kick、Reddit、Snapchat、Threads、TikTok、Twitch、X、YouTube。
- 明确**不在内**:Discord、GitHub、Google Classroom、LEGO Play、Messenger、Pinterest、Roblox、Steam 与 Steam Chat、WhatsApp、YouTube Kids。
- 2026-03-25 部长登记新 legislative rule(F2026L00370),把定义进一步绑定到 recommender feature / logged-in feature;eSafety 复核后名单未变。

### (b) Meta 关停数量 —— "约 50 万"低估,且混了两个来源
- **eSafety 事前估算**约 50 万(Instagram 约 350,000 + Facebook 约 150,000 名 13-15 岁用户)—— **这才是"约 50 万"的来源。**
- **Meta 自报实际数(2026-01-11/12 博文)**:**总计 544,052**,分解为 **Instagram 330,639 / Facebook 173,497 / Threads 39,916**,时间窗 **2025-12-04 至 12-11(8 天)**,口径为 "accounts Meta believed to be held by users under 16"。
- **成稿表述**:"Meta 称其在 2025-12-04 至 12-11 的 8 天内停用了 544,052 个其判定为 16 岁以下用户持有的账号(Instagram 330,639、Facebook 173,497、Threads 39,916)"。
- **时点性质**:12-04 早于法定义务生效日(12-10)**6 天**,属 Meta **自行提前合规**,不是被法律强制在该日执行。
- **口径性质**:Meta 自报、未经外部审计;eSafety 明示不公开分平台数据,无法交叉验证。
- **必须给出分母**:eSafety 官方口径为全行业 **"about 4.7 million age-restricted accounts were removed or restricted from platforms as at mid-December 2025"**(数据由平台在法定 information-gathering notices 下提供)。另:"At the start of March 2026, over 310,000 additional age-restricted accounts were prevented from accessing platforms."
- eSafety 逐字拒绝分拆:"eSafety will not be publishing specific numbers or detailed information obtained using its information-gathering powers."

### (c1) BMJ 研究 —— 出处与样本
- Barnes C, Hall A, Mantach S, Oldmeadow C, Attia J, Backholer K, Williams C, Tefera Y, Kay F, Wolfenden L. "**Assessing early effects of Australia's Social Media Minimum Age Act on adolescents' social media use: observational study.**" **BMJ 2026;393:e363695**, DOI 10.1136/bmj-2026-363695, 在线 **2026-06-24**, CC BY-NC。PMID 42342272, PMC13327661。注册号 ACTRN12625001056482,伦理号 H-2025-0242。
- **是 The BMJ 旗舰刊本身,不是"BMJ 系"子刊。**配套社论:Sonia Livingstone, BMJ 2026;394:e100148(2026-07-01)。
- **样本**:基线招募 **436** 人(招募期 2025-09 至 12,即实施前),随访有效 **408** 人。随访按当时年龄分组:12-13 岁 n=139、14-15 岁 n=197、≥16 岁 n=100。两波 = 实施前基线 + 实施后约 3 个月随访。
- **样本代表性(表 1)**:澳洲出生 94%、家中主要讲英语 98%、高 SES 69%(低 SES 30%)、居于 major cities 84%、67% 集中于新南威尔士一州。招募方式为社媒广告 + 课题组既往试验家长 + 邮件列表/合作机构数据库,须先取得家长同意 —— **便利样本,不具人群代表性。**

### (c2) 使用量结果 —— "12-13 岁几乎无变化"只对一个口径成立
**表 2(全部社媒,共同主要结局)**:
| 组 | 每日使用 基线→随访 | 日均时长(0–6 序数量表) |
|---|---|---|
| 12-13 岁 | 71 (51%) → 64/130 (49%) | 2.64 → 2.49 |
| 14-15 岁 | 153 (78%) → 124/179 (69%) | 3.40 → 3.13 |
| ≥16 岁 | 80 (80%) → 86/97 (**89%**) | 3.76 → 3.84 |

**表 4(受限平台,即法律标的)**:
| 组 | 过去一周用过 ≥1 个受限平台 | 每日使用受限平台 |
|---|---|---|
| 12-13 岁 | 132 (95%) → 119 (**86%**) | 60% → 52% |
| 14-15 岁 | 192 (98%) → 176 (**89%**) | 77% → 65% |
| ≥16 岁 | 100 (100%) → 96 (96%) | 89% → 85% |

- **"12-13 岁几乎无变化"只对"全部社媒的每日使用"成立;在受限平台口径上 12-13 岁明显下降(95%→86%,每日 60%→52%)。**
- **"16+ 反升"是最大的口径陷阱**:80%→89% 指的是"任何社媒的每日使用";同一批 ≥16 岁在受限平台上反而略降(100%→96%,每日 89%→85%)。**成稿须写"16 岁及以上组的整体每日社媒使用率上升(80%→89%),但其受限平台使用略降"。**
- 论文摘要写 ">16 years"、正文与表格写 "≥16 years / 16 years and over",存在内部不一致;**引用时用"16 岁及以上"。**

### (c3) ">85% 仍在用" —— 成立但必须补基线
- 随访时 12-13 岁 119/139 = **86%**、14-15 岁 176/197 = **89%**;**基线分别为 95%、98%。**
- **"仍有 85%+ 在用"同时也意味着"确实降了约 9 个百分点";只引前半句会误导。**
- 摘要逐字:"More than 85% of participants aged under 16 years reported using social media platforms subject to the Act at follow-up, **predominately via use of their own accounts (54-68%)**, 66% of whom reported exposure to platform age verification, most commonly self-declared age (24-39%) or uploading of a picture ('selfie') (13-27%). Efforts to circumvent restrictions, such as use of a 'fake' account (15-19%) or social media access via a private browser (6-11%) were also reported."

### (c4) 规避手段的分母与方向
- **分母 = "随访时仍访问受限平台者"**(12-13 岁 n=119、14-15 岁 n=176、≥16 岁 n=96),不是全体参与者。
- 表 5 逐字:"Through someone else's account 34 (**29**) / 16 (**9**) / 4 (4)";"Through a fake account 18 (**15**) / 34 (**19**) / 7 (7)";"Using incognito or private browser mode 13 (11) / 10 (6) / 1 (1)";"virtual network provider or proxy server 3 (3) / 4 (2) / 0"。
- **注意 9–29% 区间的方向与年龄相反**:借他人账号 12-13 岁 29% > 14-15 岁 9% > ≥16 岁 4%;假账号则 14-15 岁 19% > 12-13 岁 15%。

### (c5) 论文自己的主要因果结论 —— 原论断漏掉,且是最承重的一条
- 预设的 sharp RDD **在 16 岁阈值上没有检出断点**。表 3 逐字:"Social media daily use **−0.05 (−0.92 to 0.83) P=0.92**, bandwidth 2.25, N-h 349, N+h 38";"Social media average daily use **−0.35 (−1.65 to 0.96) P=0.60**, bandwidth 3.40, N-h 218, N+h 55"。
- 结论段逐字:"we found **insufficient evidence** to conclude that exposure to the Act had any early substantial effects on social media use among adolescents aged under 16 years."
- **局限段逐字(必须随结论一起引)**:"Firstly, the study was **underpowered** … A substantial number of participants, particularly those aged 12-13 years, were not included in the regression discontinuity design analyses as they were **too far from the threshold**";"We found some evidence suggesting potential concerns about the **continuity assumption**, with significant associations observed between age and both primary outcomes at baseline … We observed a **significant discontinuity for the pre-specified covariate of socioeconomic status** … Such matters raise concerns about whether the design can adequately support causal inference";"the reliance on **self-reported** measures … is a considerable methodological limitation"。
- **成稿表述:不能写"研究证明禁令无效",只能写"一项功效不足、连续性假设存疑的准实验未能检出断点"。**

### (d) 构念差 —— 成立,且是双向的
- 法律的操作构念:**在 10 个被指定平台上持有账号**;且 eSafety 明确合规判定看的是系统与流程而非个案 —— 逐字:"Whether a platform has taken reasonable steps will include an assessment of the totality of the steps taken by a platform… **This is about systems and processes, not individual accounts.**" / "While these numbers are helpful, they are not determinative of whether reasonable steps have been taken"。
- 研究的共同主要结局:**全部社媒的自报使用频率与时长**("self-reported use of social media in the previous seven days (every day versus not every day)" 与 "time spent using social media per day"),覆盖了 Discord/Messenger/WhatsApp/Pinterest/Roblox/YouTube Kids 等被明确排除在规制外的服务。
- **但反向也成立**:论文并非完全没测账号 —— 它报告 under-16 者仍 "predominately via use of their own accounts (54-68%)" 访问受限平台,这正是法律标的;同时 eSafety 的 470 万是平台侧"账号被停"计数,同样测不到孩子是否仍在看内容。
- **准确表述:两侧指标各自单边、互不可比,而非单向的"法律测账号 vs 调查测使用"。**">85% 仍在使用"既不等于">85% 仍持有被禁账号",也不构成平台违法的度量。**

### 第二条独立同向证据(建议引用)
- eSafety 家长 pulse 调查(2026-01-19 至 02-02,n=898):在 2025-12-10 前孩子有账号的家长中,约七成报告孩子仍有账号 —— Facebook 63.6%、Instagram 69.1%、Snapchat 69.4%、TikTok 69.3%、YouTube 48.5%。最常见原因是"平台还没要求验证年龄"(66.8%)。

### 利益相关
- BMJ 论文资助:Preventive Health SA(南澳政府)与 Healthway 的 Healthy Research Grant (G-202603-94270);LW 受 NHMRC investigator (L2) fellowship、CB 受 Heart Foundation 博后、KB 受 Heart Foundation future leader fellowship 支持。逐字:"Funding bodies were not involved in the development or design of the study or in the collection, management, analysis, or interpretation of the data." 及 "**No authors advised government on the legislation, contributed to parliamentary submissions, engaged in advocacy related to the policy, or consulted with regulators or advocacy organisations prior to conducting the study.**" → 无平台方或政策倡导方利益冲突。Crossref updated-by 为空,无勘误/撤稿。
- **Meta 数字为利益相关方自述**(被规制主体自报合规成绩),须如此标注。

---

## 修正记录(修正前 → 修正后)

1. **(a) 生效日口径。** 修正前:"2024 法案,2025-12-10 生效"。修正后:法案本身 2024-12-11 生效;2025-12-10 生效的是它插入 Online Safety Act 2021 的 **s 63D 义务**,由 F2025N00628 指定。差近一年。(3/3 票一致 —— 这是第 1 票唯一提交的一条)

2. **(a) 罚款上限口径 + 时效。** 修正前:"AUD 49.5m"。修正后:法条只写 30,000 penalty units,49.5m 是三段推导(×5 法人乘数 ×$330);**且已过期** —— 2026-07-01 起 penalty unit 升至 $364,当前上限为 **$54.6m**,eSafety 官方表述已同步更新。写作必须带时间戳。(2/2 实质票一致)

3. **(a) "父母同意不可豁免"的性质。** 修正前:读作法条明文豁免排除条款。修正后:是"全法无此概念"的推论(parent/guardian 零命中),旁证为 Bills Digest 与 eSafety FAQ。表述改为"法条未提供任何同意例外"。(2/2 实质票一致)

4. **(a) "全球首个"须带限定语。** 修正前:"全球首个"。修正后:法国 2023 年即立法设 15 岁门槛(以父母同意为通道、未真正实施),故准确说法是"首个由平台承担义务、无父母同意豁免、且已实际施行的国家级最低年龄制度"。(2/2 实质票一致)

5. **(a) 覆盖面口径缺失。** 修正前:泛称"禁社媒"。修正后:只禁 10 个被指定平台,Discord/Messenger/WhatsApp/Roblox/Pinterest/YouTube Kids 等明确排除。(1/2 实质票发现,无反驳,采纳)

6. **(b) Meta 数字口径 —— 混了两个来源。** 修正前:"Meta 自 12-04 起关停约 50 万账号"。修正后:**"约 50 万"是 eSafety 的事前估算**(IG 约 35 万 + FB 约 15 万);**Meta 自报的实际数是 544,052**(IG 330,639 / FB 173,497 / Threads 39,916),窗口 2025-12-04 至 12-11。(2/2 实质票一致定位到混淆,数值见下方冲突裁决)

7. **(b) 时点性质须补。** 修正前:"自 12-04 起"。修正后:12-04 比法定生效日早 6 天,是 **Meta 自行提前执行**,不是法定义务起算点。(2/2 实质票一致)

8. **(b) 分母缺失。** 修正前:只给 Meta 一家的数。修正后:须给出 eSafety 全行业口径 **约 470 万**账号被移除/限制(截至 2025 年 12 月中);Meta 拒绝被交叉验证(eSafety 不公布分平台数)。(2/2 实质票一致)

9. **(c) 期刊定位。** 修正前:"BMJ 系"。修正后:**The BMJ 本刊**(BMJ 2026;393:e363695)。(2/2 实质票一致)

10. **(c) 样本口径。** 修正前:"400+ 人两波调查"。修正后:基线招募 436、随访有效 408;RDD 分析只用带宽内子集,大量 12-13 岁因离阈值太远被排除。(2/2 实质票一致)

11. **(c) "12-13 岁几乎无变化"—— 最实质的口径错误。** 修正前:一句话概括。修正后:**只对"全部社媒每日使用"成立,对"受限平台使用"恰恰相反**(95%→86%,每日 60%→52%)。把两个不同测量混成一句。(2/2 实质票一致,第 2 票给出表 4 逐格数值)

12. **(c) "16+ 反升"的陷阱。** 修正前:80%→89%。修正后:该升幅只在"任何社媒"口径上;同组在受限平台上是**降的**(100%→96%,每日 89%→85%)。(1/2 实质票发现,采纳)

13. **(c) ">85% 仍在用"须补基线。** 修正前:只引 >85%。修正后:基线为 95%/98%,即同时意味着降了约 9pp。(1/2 实质票发现,采纳)

14. **(c) 规避手段百分比的分母。** 修正前:未注明。修正后:分母是"随访时仍访问受限平台者"(119/176/96),不是全体;且 9–29% 的区间方向与年龄相反(12-13 岁 29% vs 14-15 岁 9%)。(1/2 实质票发现,采纳)

15. **(c) 漏掉论文自己的主要因果结论 —— 最承重的补充。** 修正前:未提。修正后:预设 sharp RDD **未检出断点**(每日使用 −0.05, P=0.92;日均时长 −0.35, P=0.60),且作者自陈功效不足、连续性假设可能被违反(基线年龄与两主结局显著相关、SES 在阈值处显著断点)、全部结局自报、便利样本 67% 集中于 NSW。**任何"禁令无效"的表述必须带这些限定。**(2/2 实质票一致)

16. **(d) 构念差是双向的。** 修正前:单向"法律测账号 vs 调查测使用"。修正后:研究也测了账号(54-68% 用自己的账号),eSafety 的 470 万也测不到内容消费;两侧指标各自单边、互不可比。(2/2 实质票一致)

### 票间冲突与裁决

- **冲突:Meta 关停数的精确值。** 第 2 票给 **544,052**(IG 330,639 / FB 173,497 / Threads 39,916),引 The Guardian(Josh Taylor, 2026-01-11)逐字:"between 4 December, when the company began deactivating accounts, and 11 December, 544,052 accounts Meta believed to be held by users under 16 were deactivated. That included 330,639 on Instagram, 173,497 on Facebook and 39,916 on Threads.",并称 BBC/DW/CNBC/Forbes AU 数字一致。第 3 票给 **≈542,000**(330,000 + 173,000 + 39,000),引 ABC News 2026-01-12,并注明 AFR/DW 报 544k、BBC/ABC 标题报 550,000。
  - **裁决:采用 544,052(Instagram 330,639 / Facebook 173,497 / Threads 39,916)。**理由:第 2 票的数字是精确到个位的原始转引且有逐字引语,第 3 票的 330,000/173,000/39,000 明显是 ABC 的四舍五入表述,且第 3 票自己也记录了 AFR/DW 的 544k 与其一致。550,000 是媒体标题的口语化取整,不用。
  - **两票共同的限制照录:Meta 原始博文 URL 未定位到,四个数字均为媒体转引。成稿写"据 Meta 博文(经 The Guardian、BBC、DW 等转引)"。**

- **冲突:BMJ 表 4/表 5 的具体数值是否可得。** 第 2 票逐格给出了表 2/3/4/5 的数值;第 3 票把表 4/5 列为未取到(表格在文章 HTML 中以弹窗加载,存档页只含表题),只核到正文定性表述。
  - **裁决:采信第 2 票的表格数值。**理由:第 2 票从 PMC13327661 全文 XML 直取(结构化数据,不依赖 HTML 弹窗渲染),是更硬的取证路径;第 3 票是取证失败而非发现冲突数值。第 3 票核到的正文定性表述("small reductions occurred … particularly among those aged 12-13 and 14-15 years")与第 2 票的表 4 数值方向完全一致,互为佐证。

---

## 未回溯项(不得承重或须标未验证)

1. **Meta 2026-01-11/12 的原始博文 URL 未定位到。** about.fb.com 澳洲区 newsroom(/au/news/)在 Wayback 无存档、全站 WordPress REST API 检索无命中、about.fb.com/news/2026/01 前缀存档中亦无该篇(两票分别尝试)。544,052 / 330,639 / 173,497 / 39,916 由 The Guardian、BBC、DW、CNBC、Forbes AU、ABC、AFR 多家独立复述且彼此一致,**但公司原帖未直接核到。成稿必须写"Meta 称/据 Meta 博文(经媒体转引)"。**

2. **法国 2023 年 Loi n° 2023-566(majorité numérique)一手条文未核到** —— Legifrance 与 vie-publique.fr 均被 Cloudflare/JS 墙拦截(403 / requires JS),Wayback 无该 JORFTEXT 页快照。这是"全球首个"最强的潜在反例。**"全球首个"只能在限定语下使用**(见锁定口径 a5)。

3. **法案 Explanatory Memorandum 与 Supplementary EM 原文未取得**(parlinfo.aph.gov.au 对两票均返回 403 / Azure WAF bot 拦截,r.jina.ai 代理同样被拦)。因此"父母同意不可豁免"缺一条政府自己的明文表述,只能靠三条间接佐证:(i) 法条全文无 parent/guardian 命中、(ii) Bills Digest 转述、(iii) eSafety FAQ。

4. **eSafety 分平台的账号移除数字不可得** —— eSafety 明示 "does not intend to release the disaggregated number of accounts removed",故 **Meta 自报的 544,052 无法与监管数据交叉验证,也无法从一手推算其在 470 万中的占比。**

5. **2026-06-27 政府宣布"罚款翻倍至约 $99m"** —— 已核到该宣布未成法(截至 2026-07-28 联邦法规登记册无对应的 2026 年 Online Safety 修正法案,最新相关件仅为 F2026L00370 规则修正,2026-03-25),**但未核到该法案的议会编号、提交日与当前审议状态**(aph.gov.au 403)。→ 若写入正文,须标"已宣布、未成法,议案状态未核"。(单票发现)

6. **eSafety 官网与 parlinfo 在两票沙箱内均不可直连**(TLS 握手后无响应 / 403),eSafety 的 compliance update PDF、FAQ、家长页均经 r.jina.ai 文本代理或 Wayback 快照取得。内容与 BMJ 论文引用的同一 URL、页数(17 页)、发布时间一致,可信度高,**但严格说不是从 esafety.gov.au 直接取的字节。**

7. **BMJ 网站的 rapid responses 未逐条核。** 已确认 PubMed / Crossref 无 erratum/retraction 记录,但读者来信层未穷尽。

8. **后续演变仅核到标题层,未纳入一手核对**:2026-03-31 多家报道 eSafety 指 Meta/Snapchat/TikTok/YouTube 未充分合规并准备诉讼(eSafety 3 月合规报告确载对 Facebook/Instagram/Snapchat/TikTok/YouTube 五家立案调查);2026-04-01 Guardian 报"三分之二仍保有 Instagram/Snapchat/TikTok 账号"。方向与 BMJ 一致,但未逐篇核到一手。

9. **三票的 WebSearch 配额均已耗尽(200/200)**,检索改由 curl + 官方 API + Wayback + Europe PMC/Crossref 完成。2026-07 之后的执法决定或更晚近勘误可能遗漏。

---

## 证据分级

**法律事实层:多源证实。使用效果层:单源已核 + 功效不足。Meta 数字层:厂商口径(利益相关方自述)。**

分层给分,不可混为一谈:

- **法条、生效指令、罚款推导链、指数化 —— 多源证实(最高级)。** 全部来自 legislation.gov.au 官方端点直取的授权版正本(C2024A00127、F2025N00628、C2014A00093、C1914A00012、F2026N00424),两票独立取得同一批文件并给出一致逐字;另有议会图书馆 Bills Digest 与 eSafety 官方文件作独立第二源。**这一层可以放心承重。**
- **BMJ 研究 —— 单源已核,但研究本身功效不足、设计存疑。** 论文一手全文经 Europe PMC / PMC XML / Wayback 取得并逐字核对,无勘误,资助与 COI 声明干净(作者明确声明未参与立法咨询或政策倡导)。**但论文自陈 underpowered、连续性假设可能被违反、SES 在阈值处出现显著断点、结局全为自报、便利样本 67% 集中于一州、94% 澳洲出生 / 69% 高 SES。** → **只能承重"未能检出效应",不能承重"证明无效"。**
- **eSafety 的 470 万与家长 pulse 调查 —— 单源已核(监管方口径)。** 官方文件,但数据由被规制平台在法定通知下提供、eSafety 不公布分平台明细,不可外部审计。
- **Meta 的 544,052 —— 厂商口径(利益相关方自述)。** 被规制主体自报合规成绩,口径为"其判定为 16 岁以下",未经外部审计,原始博文未核到,只有媒体转引。**引用必须双重标注:利益相关方自述 + 媒体转引。**
- **"全球首个" —— 方向存争(定义之争)。** 监管方与独立同行评议文献口径一致,但法国 2023 年先例的一手条文未核到;不带限定语使用会失真。


---

# C22 最终判决:CORRECTED(3/3 票)

组题:Surgeon General 措辞梯度 —— 2023 "we do not yet have enough evidence to determine if social media is sufficiently safe" 逐字;2024 op-ed "is associated with significant mental health harms" + "has not been proved safe" 逐字;从未说 proved to cause。

三票均逐字核实了两条核心引语(均成立,一字不差),但三票**独立地在同一处发现该论断的判断层错误**:"措辞始终停留在 associated" 不成立。

---

## 锁定口径(成稿必须用)

### (A) 2023 Advisory —— 出处与署名
- 文件:**"Social Media and Youth Mental Health: The U.S. Surgeon General's Advisory"**,Office of the Surgeon General (OSG), U.S. Department of Health and Human Services, 2023。发布日 **2023-05-23**(Wayback CDX 对 PDF 与 SG 专页的首个快照均为 20230523;HHS 新闻稿 "FOR IMMEDIATE RELEASE May 23, 2023")。
- **署名主体是 OSG,不是 Murthy 个人。** advisory 全文(pdftotext 提取)不出现 "Murthy" 或 "Vivek" 任何一次,无署名信。**引用 advisory 时记为"美国医务总监办公室(OSG)/HHS 2023 年公告",不要写成"Murthy 在公告中说"。**个人署名的表述只存在于 2024 年 NYT op-ed。
- 自述证据位阶(NBK594757 "About the Advisory"):**"This document is not an exhaustive review of the literature."**
- 全文因果用词自查:**"causal" 0 次、"causation" 0 次;"cause" 仅 2 处,且均为开放式研究问题**("more research is necessary to understand whether one causes the other";"What are the potential pathways through which social media may cause harm...")。

### (B) advisory 核心引语 —— 逐字成立,但"sufficiently safe"出现两次且措辞不同,不可混用
- **第一处(PDF p.4,开篇节)完整段落逐字**:
  > "More research is needed to fully understand the impact of social media; however, the current body of evidence indicates that while social media may have benefits for some children and adolescents, there are ample indicators that social media **can also have** a profound risk of harm to the mental health and well-being of children and adolescents. At this time, we **do not yet have enough evidence to determine** if social media is sufficiently safe for children and adolescents."
- **第二处(第三章 "Critical Questions Remain Unanswered",PDF p.10–11)逐字**:
  > "Nearly every teenager in America uses social media, and yet we do not have enough evidence to **conclude** that it is sufficiently safe for them."
- **引用时必须指明是哪一处,不能把 determine 与 conclude 混用或合成一句。**
- 紧随第一处之后的一句(同一梯度):"We must acknowledge the growing body of research about **potential harms**, increase our collective understanding of the **risks associated with** social media use, and urgently take action to create safe and healthy digital environments..."
- 同章另有:"robust independent safety analyses on the impact of social media on youth have not yet been conducted"。

### (C) "profound risk of harm" —— 三重对冲的从句,且不是 HHS 的统一口径
- **必须连引的三重限定**:(1) 前置 "More research is needed to fully understand the impact of social media; **however**";(2) 让步 "**while social media may have benefits** for some children and adolescents";(3) 情态 "there are **ample indicators** that social media **can also have** a profound risk of harm" —— 载体是"指标充分 + 可能同时具有",不是 "has" / "poses" / "causes"。
- **截断成 "social media has a profound risk of harm" 属篡改。**
- **"profound" 只出现在 PDF 正文,不是 HHS 的统一口径**,同一份 advisory 有三种官方措辞:
  - PDF 正文:"can also have a **profound** risk of harm"
  - HHS 2023-05-23 官方新闻稿同一段:"there are ample indicators that social media can also **pose a risk of harm**"(**无 profound**)
  - HHS 现行 advisory 落地页 Key Takeaways:"Social media presents a **meaningful** risk of harm to youth, while also providing benefits"
- **引用 "profound" 时必须标明出自 PDF 正文。**

### (D) 2024 op-ed —— 出处与两条核心引语(逐字成立)
- Vivek H. Murthy,**"Surgeon General: Why I'm Calling for a Warning Label on Social Media Platforms"**,The New York Times Opinion,**2024-06-17**(纸质版 2024-06-18 A24 版题 "Social Media Platforms Need a Health Warning")。署名注 "Dr. Murthy is the surgeon general."
- 逐字(注意句首大写、用 "proved" 非 "proven"):
  > "**It is time to require a surgeon general's warning label on social media platforms, stating that social media is associated with significant mental health harms for adolescents. A surgeon general's warning label, which requires congressional action, would regularly remind parents and adolescents that social media has not been proved safe.**"
- **口径限定:"has not been proved safe" 不是 Murthy 的独立断言句,原文是 "would regularly remind parents and adolescents **that** ..." 的从属结构 —— 是"标签应当提醒的内容",不是"我宣称"。引用需带该从属结构。**
- **"which requires congressional action" 出自 Murthy 本人,是"需国会立法"这一点的一手依据,不是二手转述。**
- 页面无 Correction / Editors' Note。

### (E) 判决:"从未说 proved to cause"成立;"措辞始终是 associated"不成立
- **成立的部分**:Murthy 从未宣称因果"已被证明"(never "proved to cause");advisory 全文 causal/causation 出现 0 次。
- **不成立的部分 —— 同一批文本中的更强归因措辞(三票各自独立发现,须并列呈现)**:
  - 2024 op-ed 逐字:**"The mental health crisis among young people is an emergency — and social media has emerged as an important contributor."**
  - 2024 op-ed 逐字:**"These harms are not a failure of willpower and parenting; they are the consequence of unleashing powerful technology without adequate safety measures, transparency or accountability."**
  - 2023-05-23 HHS 新闻稿中 Murthy 的直接引语:**"The answer is that we don't have enough evidence to say it's safe, and in fact, there is growing evidence that social media use is associated with harm to young people's mental health... We are in the middle of a national youth mental health crisis, and I am concerned that social media is an important driver of that crisis – one that we must urgently address."**
- **锁定表述**:Murthy 的措辞是**双层**的 —— **拟议标签文案与安全性判断停留在关联性("associated with" / "has not been proved safe"),但他本人的论证声部使用了贡献性因果表述("an important contributor" / "an important driver" / "are the consequence of")**。把梯度描述成"始终只是 associated"会低估其实际强度;把它描述成"宣称已证明因果"则会高估。

### (F) 警示标签立法状态 —— 必须加"联邦"层级限定
**联邦层面:未通过(成立)**
- 对口法案 **Stop the Scroll Act**:118 届 **S.5150**(2024-09-24 提出,随届失效);119 届 **S.1885**(主提 Sen. Katie Britt [R-AL],共提 Sen. John Fetterman,2025-05-22 提出),最新行动 **2026-04-14 参议院商业、科学与运输委员会 "Ordered to be reported with an amendment in the nature of a substitute favorably"**,current_status = reported。**截至 2026-07-27 未经两院表决、未成法。**
- S.1885 法案文本(govinfo 一手 BILLS-119s1885is)SEC.4:标签须 "warn the user of potential negative mental health impacts of accessing the covered platform" 并提供含 988 的联邦资源,"clearly and conspicuously",每连续使用一小时重现。
- KOSA(S.1748,119 届,2025-05-14)仍为 introduced;同名众院法案 H.R.6484 于 2025-12-05 introduced。
- 以 congress=119 + enacted_signed 过滤检索,无任何警示标签相关联邦成法。

**州层面:已有生效的强制警示标签(反证,必须披露)**
- **Minnesota Statutes § 325M.335 "MENTAL HEALTH WARNING LABEL"**(History: 1Sp2025 c 3 art 19 s 13)一手条文逐字:"(a) **Effective July 1, 2026**, a social media platform must ensure that a **conspicuous mental health warning label** ... (2) only disappears when the user: (i) exits... or (ii) acknowledges the potential for harm and chooses to proceed... despite the risk."。Subd.2:"By **March 1, 2026**, the commissioner of health, in consultation with the commissioner of commerce, must develop guidelines... based on current evidence regarding the negative mental health impacts of social media platforms." 须提供 988 危机热线入口。
- **注意:它不是 surgeon general's label** —— 标签内容由明尼苏达州卫生专员制定,与联邦 SG 标签是两回事。
- **California AB 56**:Newsom 于 **2025-10-13** 签署,要求对 18 岁以下用户显示烟草式公共卫生警示标签,**2027-01-01 生效**。
- **成稿表述:只能说"联邦 / surgeon general 版警示标签未通过",不能笼统说"警示标签未通过"或"美国目前没有社交媒体警示标签"。**
- 明尼苏达法已生效但据报道随即被暂停:MPR News(2026-07-01)标题 "Not yet as Minnesota law is paused until court sorts it out";Minnesota Daily(2026-07-18)报道 NetChoice 代表主要科技公司起诉,主张该法 "violates the First Amendment"。**须标注:一手司法文书未取得(见未回溯项)。**

### (G) op-ed 支撑数字的口径问题(建议主动披露,否则文章会二次传播失真)
- **"double the risk"这一句**:op-ed 原文 "Adolescents who spend more than three hours a day on social media face double the risk of anxiety and depression symptoms",超链接指向 **Riehm et al. 2019, JAMA Psychiatry(PMC6739732)**。该文是 PATH 纵向队列,n=6,595,基线 12–15 岁,结局构念是 GAIN-SS 测的 **internalizing / externalizing problems(非确诊焦虑抑郁)**;>3h 组 **internalizing-only 的 RRR = 1.60 (95% CI 1.11–2.31)**;接近 2.0 的是 **comorbid internalizing+externalizing** 类别(>3–6h RRR=2.01;>6h RRR=2.44)。作者明言 "it is possible that the observed associations were an artifact of unmeasured confounding"。→ **"double the risk of anxiety and depression symptoms" 把共病类别的 RRR 与内化问题结局混说了。**
- **"4.8 hours"这一句**:op-ed "the average daily use in this age group, as of the summer of 2023, was 4.8 hours" 链接到 **Gallup 民调**(news.gallup.com/poll/512576),自报数据非客观测量。而 HHS advisory 落地页在同一"3 小时/双倍风险"论断上配的是 "teenagers spend an average of **3.5 hours** a day"。**同一机构文本内平均使用时长口径 3.5h vs 4.8h 不一致,引用时须注明取自哪一份。**

### 利益相关
- 一手文件均为政府出版物(HHS/OSG、明尼苏达州法典、govinfo 法案文本)或作者本人署名评论,无商业赞助披露问题。
- **Murthy 作为倡导者本身有政策立场,其 op-ed 属主张性文本而非证据综述** —— 这反而使"associated / not proved safe"的克制措辞更具说服力(倡导语境下仍未升格为"已证明因果")。
- NetChoice 的诉讼立场为行业利益相关方,其第一修正案主张不构成对科学口径的评价。

---

## 修正记录(修正前 → 修正后)

1. **(c) "措辞始终是 associated / not proved safe"—— 方向对但过强,须降一档。** 修正前:措辞"始终"停留在关联性。修正后:Murthy 从未主张 proved to cause(此点成立),**但也从未只停留在 associated** —— 同一篇 op-ed 有 "social media has emerged as an important contributor"、"they are the consequence of unleashing powerful technology...";2023 HHS 新闻稿有 "I am concerned that social media is an important driver of that crisis"。正确表述是**双层措辞:标签文案与安全性判断是关联性,论证声部是贡献性因果归因。**(**3/3 票独立发现,这是本组最重要的修正**)

2. **(a) "profound risk of harm" 的呈现方式须加限定语。** 修正前:读作独立断言。修正后:原句是三重对冲的从句(More research is needed…however / while social media may have benefits / ample indicators that … **can also have**),且同句前半明确承认对部分儿童青少年可能有益。**截断成 "social media has a profound risk of harm" 属篡改。**(3/3 票一致)

3. **(a) "profound" 不是 HHS 的统一口径。** 修正前:视作该 advisory 的官方定性。修正后:同一份 advisory 存在三种官方措辞 —— PDF 正文 "profound"、HHS 新闻稿无形容词("pose a risk of harm")、HHS 落地页 Key Takeaways "meaningful"。**引用须标明出自 PDF 正文。**(1/3 票发现,证据为并列三处官方文本,无反驳,采纳)

4. **(a) 归属修正:advisory 不是 Murthy 个人署名文件。** 修正前:"Murthy 在 advisory 中说"。修正后:advisory 全文 grep 无 "Murthy" / "Vivek" 命中,署名主体是 Office of the Surgeon General, U.S. HHS, 2023。个人署名表述只存在于 2024 op-ed。(见下方票间冲突裁决)

5. **(a) advisory 中 "sufficiently safe" 出现两次且措辞不同。** 修正前:视作同一句。修正后:开篇节(p.4)用 **determine**,第三章(p.10–11)用 **conclude**,且后者句式不同("Nearly every teenager in America uses social media, and yet...")。**引用必须指明是哪一处,不可混用。**(2/3 票发现,一致)

6. **(b) op-ed 引语的两处形式修正。** 修正前:小写 "it is time to require...";把 "has not been proved safe" 当独立断言句。修正后:原文句首大写 "**It** is time to require...";"has not been proved safe" 嵌在 "would regularly remind parents and adolescents **that**..." 的从属结构中;用 "**proved**" 非 "proven"(psychiatrist.com 转载写作 "[proven]" 带方括号,系其编辑替换,以 NYT 原词为准)。(2/3 票发现,一致)

7. **(c) "警示标签未通过"须限定为联邦层级。** 修正前:笼统"警示标签未通过"。修正后:**联邦确未通过**(S.1885 止于 2026-04-14 委员会 reported);**但州层面已落地** —— Minn. Stat. § 325M.335 已于 2026-07-01 生效,California AB 56 已于 2025-10-13 签署、2027-01-01 生效。**"美国目前没有社交媒体警示标签"是错的。**(3/3 票一致)

8. **(a) 发布日期精确化。** 修正前:"2023-05"。修正后:**2023-05-23**(Wayback CDX 首快照 + HHS 新闻稿日期两路确认)。(1/3 票发现,采纳)

9. **新增:op-ed 支撑数字的口径问题应主动披露。** "double the risk" 混说了 comorbid 类别 RRR 与 internalizing 结局(一手 Riehm et al. 2019);"4.8 hours" 来自 Gallup 自报民调,且与 HHS 落地页的 3.5 小时口径不一致。(2/3 票发现,一致)

### 票间冲突与裁决

- **冲突:advisory 那两句核心引语的署名归属。** 第 1 票称该句出自 "advisory 正文首章(Murthy 署名前言段)";第 3 票称对存档 PDF 做 pdftotext 提取后 grep,**"Murthy" 与 "Vivek" 零命中,文件无署名信**;第 2 票未就署名表态。
  - **裁决:采信第 3 票。** 理由:第 3 票执行的是对 PDF 全文的机械 grep,属可复现的硬检验;第 1 票的"Murthy 署名前言段"是从 advisory 惯例作出的推断,未给出该署名的逐字证据。
  - **成稿口径:引用 advisory 记为 OSG/HHS 机构文件;引用 "important driver" 记为 Murthy 在 HHS 新闻稿中的个人直接引语;引用 op-ed 记为 Murthy 署名评论。三者不可混称。**

- **冲突:明尼苏达法是否已被法院暂停。** 第 1 票给出两则新闻(MPR News 2026-07-01、Minnesota Daily 2026-07-18)佐证"已生效但随即被暂停";第 3 票明确将此列为未能核实(CourtListener API 对匿名用户 403,WebSearch 配额耗尽)。
  - **裁决:可写入,但须降级标注。** 理由:第 3 票是取证失败而非发现反证,而第 1 票有两则独立新闻;但两票都没有一手司法文书。**成稿表述:"该州法虽已于 2026-07-01 生效,但据 MPR News 与 Minnesota Daily 报道随即因 NetChoice 的第一修正案诉讼被法院暂停(裁定文书未取得)"。不得写"该州标签已在实际展示"。**

---

## 未回溯项(不得承重或须标未验证)

1. **NYT op-ed 全文付费墙 / 对自动请求封锁。** 三票均无法从 nytimes.com 直接抓取。逐字核对路径:第 1 票 = NYT 自身检索摘要 + psychiatrist.com 全文转载 + 多处新闻复现;第 2 票 = Internet Archive 两个时间点快照(2024-06-19 与 2025-09-01,二者一致且无勘误标记);第 3 票 = Wayback 快照 20260219170401。**两句核心引语可判定逐字成立(三票互证 + 两个独立时间点快照一致)**,但:(i) 未取得与 Wayback 完全独立的第三方全文镜像(archive.today 返回 429/不可达);(ii) **op-ed 中是否还存在其他更强或更弱的因果措辞,无法穷尽核查**(已发现的三处更强措辞见锁定口径 E)。→ 若需最高强度证据,建议用 NYT TimesMachine 或 ProQuest/Factiva 再核一次。

2. **hhs.gov 原 PDF 对三票均返回 403(带浏览器 UA 亦然)。** 逐字核对依赖 **Wayback 原样字节(20230523112805if_,974,593 bytes)+ NCBI Bookshelf 官方转载(NBK594757/NBK594759/NBK594761)** 两个独立镜像互证,内容完全一致。未能从 hhs.gov 活链直接取得字节;PDF 排版版本的页码级比对(如封面信、执行摘要中是否另有 "profound risk of harm" 出现)未做,仅确认在 "Social Media and Youth Mental Health" 章内出现一次。

3. **明尼苏达法被法院暂停的确切裁定日期、法院与案号未取得一手司法文书**(CourtListener API 匿名 403)。仅有两则新闻报道佐证。

4. **明尼苏达州卫生专员是否已按 subd.2 于 2026-03-01 前发布标签内容指引、指引具体文案为何,未核到一手文件。**

5. **未系统清点明尼苏达、加州以外的其他州警示标签法。** 只能确认"至少明尼苏达已生效、加州已签署待生效",不能主张"仅此两州"。

6. **未做联邦成文法全文审计。** 仅以 GovTrack 法案状态检索确认无警示标签法案成法,未逐条排查 2025–2026 综合拨款法 / NDAA 等大部头法案内是否夹带过相关条款。

7. **Murthy 2025 年 1 月卸任后是否有更新表述、现任 Surgeon General 是否维持/撤回/强化该 advisory 立场,未检索**(WebSearch 配额耗尽)。**可确认的只有:advisory 本身仍挂在 hhs.gov 现行页面上,可视为未撤回。**

8. 三票 WebSearch 配额均已耗尽(200/200),后续检索改用 WebFetch 直取 + DuckDuckGo Lite 代理(期间遭遇 CAPTCHA)。检索覆盖面弱于正常搜索,**可能遗漏 2026-07 下旬的联邦立法动态。**

---

## 证据分级

**多源证实。**

- **两条核心引语:三票独立逐字核实,全部一字不差成立。** advisory 经 Wayback 原样字节 + NCBI Bookshelf 官方转载双镜像互证(第 2 票另做规范化空白后逐字符比对);op-ed 经 Wayback 两个不同时间点快照 + NYT 检索摘要 + psychiatrist.com 全文转载 + 五家新闻复现交叉确认。
- **立法状态:多源已核。** GovTrack API 法案状态 + govinfo 法案文本一手 + 明尼苏达州法典官方 revisor.mn.gov 一手条文,均为可复核的官方源。
- **无利益冲突问题**:全部一手件为政府出版物或作者署名评论。须披露的是 Murthy 的倡导者身份(其 op-ed 是主张性文本,不是证据综述)与 NetChoice 的行业身份。
- **本组的判决性质**:引语层 **HOLDS**,判断层 **CORRECTED** —— 三票独立地在同一处推翻了"措辞始终是 associated"这一概括。这个修正是本组最承重的产出:**梯度是真实存在的,但比原论断描述的更陡**(标签文案克制 / 论证声部已用"重要推手"级归因),且"未通过"必须限定到联邦层。
- **降级项(须标注)**:明尼苏达法的诉讼状态为新闻层证据、无司法文书;op-ed 全文的穷尽性核查未完成(付费墙),因此"从未出现更强措辞"这一否定性主张只能限定为"在已核到的全文快照中未见更强于 important contributor 的表述"。


---

# C23 最终判决:CORRECTED(3/3 票)

组题:剂量背景 —— Pew TikTok "almost constantly" 16%(2022)→21%(2025);36% 至少一平台 almost constantly(2024);Common Sense 8h39m 系 2021 口径不可当"如今"。

三票均直接 WebFetch 一手(Pew 报告正文 + 官方 topline PDF 逐页 + Common Sense 全文 PDF + 官方 research sitemap),数值核对结果高度一致。**三票独立地在同一处发现同一个跨年串号错误。**

---

## 锁定口径(成稿必须用)

### (A) 两份 Pew 报告的正确身份
- **Pew《Teens, Social Media and Technology 2024》**,发布 **2024-12-12**,调查期 2024-09-18 至 2024-10-10,**n=1,391**,13–17 岁,MoE ±3.3。
- **Pew《Teens, Social Media and AI Chatbots 2025》**,发布 **2025-12-09**,调查期 2025-09-25 至 2025-10-09,**n=1,458**,13–17 岁,MoE ±3.3。
- **⚠ 不存在"Teens, Social Media and Technology 2025"。**2025 年这一期改名为 "…and AI Chatbots 2025"。引用时必须用新名,否则读者按旧名检索会查无此报告。
- Pew 2024 页面已自加注指向后续:"For the latest survey data on social media and tech use among teens, see 'Teens, Social Media and AI Chatbots 2025.'" —— **来源方本身已把 2024 数字标记为过时。**两页 HTML 的 dateModified 均为 2026-07-09,均无勘误声明。

### (B) "36% 至少一平台 almost constantly" —— 归 2025,不归 2024
- **Pew 2025 逐字**:"Across these five platforms, **36%** of teens use at least one of these sites almost constantly."
- **Pew 2024 逐字**:"Across all five platforms, **one-third** of teens use at least one of these sites almost constantly." —— **正文、报告 PDF 图表、topline PDF 三处均只有文字表述,未发布该 NET 的具体百分数。**
- **可比的已发表整数是 Pew 2022 报告的 35%**:"Fully **35%** of teens say they are using at least one of them almost constantly."(2022 报告,field 2022-04-14 至 05-04,n=1,316)
- **成稿表述**:"2024 年 Pew 表述为约三分之一;2025 年为 36%;2022 年为 35%"。**不要自行为 2024 填 33% / 34% / 35% / 36%,也不要据此计算 2024→2025 的变动幅度。**

### (C) TikTok "almost constantly" 时间序列 —— 基准年问题的裁决
- **Pew 2025 正文逐字**:"The share of teens who say they are on TikTok almost constantly ticked up slightly to **21% this year, from 16% in 2022**."
- **官方 topline(BASED ON ALL TEENS)完整四年序列**:**2022 = 16、2023 = 17、2024 = 16、2025 = 21**。
- **裁决**:用 "vs 2022" 是**逐字忠实于 Pew 的**;用 "vs 2024" 在数值上也不错(2022 与 2024 恰好都是 16),但不是 Pew 的原始表述。**真实的上升发生在 2024→2025 单年内(16→21,+5pp),此前 2022–2024 基本横盘。**若文章要表达"近年持续攀升",该口径不成立。
- **建议成稿写法**:"2025 年较 2024 年上升 5 个百分点(16%→21%),此前 2022–2024 三年基本持平"。
- **⚠ 口径隔离**:topline 另有 "ASK IF USER" 版(TikTok 用户中 2024 = 25%),与 BASED ON ALL TEENS 口径完全不同,**不可混用**。

### (D) 各平台 almost constantly(BASED ON ALL TEENS)
| 平台 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| TikTok | 16 | 17 | 16 | **21** |
| YouTube | 19 | 16 | 15 | **17** |
| Instagram | 10 | 8 | 12 | **12** |
| Snapchat | 15 | 14 | 13 | **12** |
| Facebook | 2 | 3 | 3 | **3** |

- **五个平台里只有 TikTok 单项上升;Snapchat 微降,Instagram / Facebook 持平。**
- Pew 2025 副标题是 "Roughly 1 in 5 U.S. teens say they are on TikTok and YouTube almost constantly",**但两者数值不同:TikTok = 21%,YouTube = 17%。**把 "1 in 5" 套到 YouTube 会高估。

### (E) NET Daily(每日使用率)
- **2024**:YouTube 73(15/39/18)、TikTok **57**(16/34/7)、Instagram 50(12/28/10)、Snapchat 48(13/27/8)、Facebook 20(3/10/8)
- **2025**:YouTube 76(17/43/16)、TikTok **61**(21/34/6)、Instagram 55(12/31/12)、Snapchat 46(12/26/8)、Facebook ~19–20(3/9/7)
- Pew 2024 逐字:"Overall, **73%** of teens say they go on YouTube daily… This share includes **15%** who describe their use as 'almost constant.'" / "**About six-in-ten** visit TikTok daily. This includes **16%** who report being on it almost constantly."
- **"约六成每天 TikTok" 忠实于 Pew 的口语化措辞,但精确值 2024 = 57%,不是 60%。2025 年才真正到 61%。若给整数须写 57%(2024)/ 61%(2025)。**

### (F) 【框架修正】"使用量未退潮"这个统领说法必须收窄
- **整体"almost constantly online"(INTREQ,BASED ON ALL TEENS)**:2014-15 = 24、2022 = 46、2023 = 46、2024 = 46、**2025 = 40**。
- **Pew 2025 正文逐字**:"Nearly all U.S. teens (97%) say they use the internet daily, including **four-in-ten** who say they are almost constantly online. The share of teens who say they're online almost constantly is much higher today than a decade ago, **though it's a slight dip from last year**."
- Pew 2025 另有:"Overall, teen daily use of these platforms remains relatively stable from past years."
- **准确表述:"平台级日用大体稳定、TikTok 近乎不间断使用逆势上升,但自报的整体近乎不间断上网比例 2025 年单年下降 6 个百分点(46%→40%)。"**
- **"使用量未退潮"属以偏概全,不可作为小标题或统领句。**

### (G) 性别拆分
- **2024 逐字(可用)**:"teen girls are more likely than boys to say they use TikTok almost constantly (**19% vs. 13%**)"。
- **2025 性别拆分:须复核后方可使用(见票间冲突裁决)。**稳妥做法是文章只用 2024 的 19% / 13%,并注明年份。

### (H) Common Sense 8h39m —— 出处、口径与年份
- **报告**:《**The Common Sense Census: Media Use by Tweens and Teens, 2021**》。建议引用格式 **Rideout, Peebles, Mann & Robb (2022),数据采集 2021 年秋**。
- **现场期 2021-09-29 至 2021-10-25;n=1,306;8–18 岁;Ipsos KnowledgePanel 概率抽样;报告 2022-03-09 才发布。**报告名年份是数据年,不是发布年。
- **核心数字逐字**:"On average, 8- to 12-year-olds use about five and a half hours of screen media per day (**5:33**), while 13- to 18-year-olds use about eight and a half hours of screen media (**8:39**)."
- **分母是全样本均值(含零使用者),不是使用者均值。** 同表 among-users 版本为 **teens 8:55 / tweens 5:50**。
- **年龄段分母必须写死**:8:39 的分母是 **13–18 岁**(含 18 岁),5:33 的分母是 **8–12 岁**;**Pew 是 13–17 岁**。两套调查年龄边界不同,并列时不可互相当作同一人群。

### (I) 8h39m 的三条必带限定语(缺一则失真)
1. **构念 = 非学业的娱乐性屏幕使用。**方法学逐字:"The survey concerns the use of media for entertainment purposes, therefore **all questions focus on non-school-related activities**." 正文另明确排除 "the time spent using digital devices for classes or homework"。
2. **是内容累加时长,不是独占钟表时长。**报告逐字:"**These findings on total amount of screen media used do not mean that young people devote five and half or eight and a half hours each day exclusively to screen media**" —— 理由是多屏并用(两小时内容可压进一小时)与背景性使用(边坐车/吃饭边用)。直接当作"每天 8.5 小时盯屏"会高估。
3. **与 2019 口径并非完全可比**:2021 首次把 ebook 计入(teens +8 分钟)、剔除影院与 iPod Touch(teens 之前占 6 分钟)。

### (J) 8h39m 还是疫情峰值口径,不是稳态基线
- 趋势(Figure A / Table 1):**teens 2015 = 6:40 → 2019 = 7:22 → 2021 = 8:39**;**tweens 2015 = 4:36 → 2019 = 4:44 → 2021 = 5:33**。
- 两年涨幅(teens +1:17)超过前四年之和,报告自陈 "**we cannot determine how much COVID-19 restrictions played a role**"。
- **成稿须标注为"2021 年秋疫情期口径",不得作为稳态基线。**
- **比均值更稳健的分布口径(建议改用)**:13–18 岁中"每天超过 8 小时"占比 **2019 = 29% → 2021 = 41%**;"2 小时及以下" **2019 = 15% → 2021 = 7%**。

### (K) 无同口径更新 —— 论断成立
- 官方 research sitemap 穷举(https://www.commonsensemedia.org/research/sitemap.xml)确认全部含 census 的条目仅 7 条:plugged-in-parents 2016、zero-to-eight 2017、21st-century-classroom、**tweens-and-teens 2019**、zero-to-eight 2020、**tweens-and-teens 2021**、the-2025-common-sense-census-media-use-by-kids-**zero-to-eight**。
- **8–18 岁 census 序列止于 2021,其后(2022–2026)无任何续作。**直接构造 2025 版 tweens-and-teens URL 返回 404,交叉确认。
- 最新一期《The 2025 Common Sense Census: Media Use by Kids Zero to Eight》(2025-02-26,自述为 "The fifth iteration")**仅覆盖 0–8 岁**,头条数字约 2.5 小时/天,不含 tweens/teens,亦未预告 8–18 岁续作。
- **因此"8.5 小时"是 2021 年秋数据,至今约 4.8 年,"如今 8.5 小时"属过期引用。论断 (c) 成立。**
- 同源但不同构念的近期替代数据(**不能当作 census 更新**):Common Sense《Constant Companion: A Week in the Life of a Young Person's Smartphone Use》为手机被动测量研究,测手机使用而非全屏幕娱乐时长,口径与 8:39 不可互换。

### (L) 来源位阶与利益相关(两者不宜并列当作等价一手)
- **Pew Research Center**:无党派机构,由 Pew Charitable Trusts 资助,无平台方资金,两期报告均经独立 IRB(Advarra)审查;五平台频率题(TSNS1/TSNS2)2022/2023/2024/2025 四轮题干与选项一致,**可做纵向比较**。→ 低利益冲突,证据位阶高。
- **Common Sense Media**:**同时是儿童在线安全立法的倡导组织**(其 research 页并列 "Betting on Boys"、"Age Assurance Attitudes" 等政策导向研究,并直接游说立法);census 为**自行发布、非同行评审**;2021 census 由 Carnegie Corporation of New York 与 Craig Newmark Philanthropies 资助。→ **屏幕时间数字与自身倡导立场同向,引用时须披露其倡导身份与资助方。**但方法学披露完整(Ipsos 概率抽样、n=1,306、公开完整问卷与方法学附录、剔除 22 个 outlier),核对的 8:39 / 5:33 与其公开 PDF 表格逐字一致,不足以推翻数字本身。

---

## 修正记录(修正前 → 修正后)

1. **【最严重】36% 归错年份。** 修正前:"Pew 2024-12 报告 36% 至少一平台 almost constantly"。修正后:**36% 出自 Pew 2025-12**;Pew 2024 报告正文只写 "one-third",全文/报告 PDF/topline 三处均未给出该 NET 的具体百分数。**把 36% 挂到 2024 会同时虚增 2024 的剂量、并抹掉 2024→2025 的真实变化。**可比的已发表整数是 2022 年的 35%。(**3/3 票独立发现,一致定为本组核心错误**)

2. **报告名错。** 修正前:隐含 Pew 2025-12 是《Teens, Social Media and Technology 2025》。修正后:**2025 年这期改名为《Teens, Social Media and AI Chatbots 2025》**(2025-12-09),不存在 "Technology 2025" 版。按旧名检索会查无此报告。(3/3 票一致)

3. **【框架被部分推翻】"使用量未退潮"这个统领说法须收窄。** 修正前:笼统"未退潮"。修正后:同一份 Pew 2025 一手数据显示整体 "almost constantly online" 从 46%(2022–2024 连续三年)降到 **40%**,Pew 自称 "a slight dip from last year";Snapchat 13→12、Instagram 12→12、Facebook 3→3 均无增长。**五个平台里只有 TikTok 上升。**准确表述是"总体在线强度略降、TikTok 逆势上升",不是"整体未退潮"。(**3/3 票独立发现**)

4. **基准年待核点已解决,但结论要改写。** 修正前:待裁决是 vs 2022 还是 vs 2024。修正后:Pew 原文逐字就是 "from 16% in 2022",引 2022 是逐字忠实的;**但 topline 显示 2022=16 / 2023=17 / 2024=16 / 2025=21,即三年横盘后 2025 单年跳 5pp。**若文章想表达"近年持续攀升",该口径不成立。(3/3 票一致)

5. **"约六成每天 TikTok"的精确分母。** 修正前:"约六成"。修正后:"About six-in-ten" 是 Pew 自己的口语化措辞;**topline 全体基数精确值 2024 = 57%(16+34+7),2025 = 61%**。用"六成"忠实于 Pew;若给整数,2024 是 57% 不是 60%。(3/3 票一致)

6. **Pew 2025 副标题的 "1 in 5" 不适用于 YouTube。** 修正前:未提。修正后:副标题 "Roughly 1 in 5 … on TikTok and YouTube almost constantly",但 TikTok = 21%、**YouTube = 17%**,把 "1 in 5" 套到 YouTube 会高估。(1/3 票发现,采纳)

7. **Common Sense 年份/发布日须区分。** 修正前:"Common Sense 2021 census"(易被读成 2021 年发布)。修正后:**现场期 2021-09-29 至 10-25,报告 2022-03-09 才发布**;报告名年份是数据年不是发布年。引用格式 Rideout et al. (2022),数据采集 2021 年秋。(3/3 票一致)

8. **8:39 / 5:33 的分母是全样本均值,不是使用者均值。** 修正前:未注明。修正后:同表 among-users 版本为 teens **8:55** / tweens **5:50**;8:39/5:33 是全体受访者(含零使用者)的日均。(2/3 票发现,一致)

9. **8:39 的构念口径须写明三条限定。** 修正前:"13-18 岁娱乐性屏幕 8h39m/天"。修正后:必须同时带 (i) 非学业娱乐性屏幕(明确排除上课/作业);(ii) **内容累加时长而非独占钟表时长**,报告逐字自陈"do not mean that young people devote … exclusively to screen media";(iii) 2021 首次计入 ebook、剔除影院与 iPod Touch,与 2019 口径非完全可比。**直接当作"每天 8.5 小时盯屏"会高估。**(3/3 票一致,各补一部分)

10. **8:39 不只是"过期",还是疫情峰值口径。** 修正前:只强调过期。修正后:2019→2021 两年涨 1:17,超过前四年涨幅,报告自陈 "we cannot determine how much COVID-19 restrictions played a role"。**须标注为 2021 秋疫情期峰值,而非稳态基线。**(1/3 票发现,依据为报告自述逐字,采纳)

11. **年龄边界不可互换。** 修正前:与 Pew 数据并列。修正后:Common Sense 8–18 / 13–18 岁 vs Pew 13–17 岁,两套调查边界不同(Common Sense 含 18 岁),不能互相当作同一人群。(1/3 票发现,采纳)

12. **来源位阶须披露。** 修正前:Pew 与 Common Sense 并列。修正后:Common Sense Media 是儿童在线安全倡导组织、census 自行发布非同行评审、资助方为 Carnegie 与 Craig Newmark Philanthropies;Pew 为无党派机构。**二者证据位阶不同,不宜并列当作等价一手。**(3/3 票一致)

13. **建议改用比均值更稳健的分布口径。** 13–18 岁"每天超过 8 小时"2019 = 29% → 2021 = 41%;"2 小时及以下"2019 = 15% → 2021 = 7%。这比单一均值更适合做剂量论证。(1/3 票提出,采纳为写作建议)

### 票间冲突与裁决

- **冲突:Pew 2025 的 TikTok 性别拆分。** 第 2 票称页面摘要返回 **girls 16% / boys 14%**,并判定"与总体 21% 逻辑矛盾(两性均低于总体不可能)",定为不可用。第 3 票称 **2025 TikTok almost constantly 女 24% vs 男 17%;YouTube 反向,男 20% vs 女 13%**,并提醒 2024 的 19/13 只适用于 2024。第 1 票未涉及。
  - **裁决:第 2 票的 16/14 确定不可用(内部逻辑矛盾,判为抓取错误);第 3 票的 24/17 与总体 21% 逻辑自洽(加权约 20.5),更可能正确,但仅单票、且另一票在同一处抓到了错误数据 → 判为"须复核后方可使用"。**
  - **成稿口径:只用 2024 的 19% / 13% 并注明年份。若必须用 2025 性别拆分,须先回 Pew 2025 topline PDF 的性别分层表复核。**

- **无实质数值冲突**:三票在 Pew topline 四年序列、NET Daily、Common Sense 8:39/5:33/8:55/5:50、2015/2019/2021 趋势、sitemap 穷举结果上完全一致,无一处需要裁决。

---

## 未回溯项(不得承重或须标未验证)

1. **Pew 2024 "至少一个平台 almost constantly" 的精确整数无法回溯到一手。** 报告正文、报告 PDF 图表、topline PDF 三处均只有 "one-third" 的文字表述,topline 无对应的跨平台 NET 行,Pew 也未公布该 NET 的题号。→ **无法判定 2024→2025 的 36% 是上升、持平还是四舍五入差异。成稿只能写"2024 年 Pew 表述为约三分之一,2025 年为 36%",不得自行填 33/34/35,不得计算跨年差值。若正文需要一个可核的跨年差值,改用 TikTok 16%→21%。**(3/3 票一致标记)

2. **Pew 2025 报告附录是否给出 "at least one almost constantly" 的分人群拆分,未核**(仅核到正文 36% 一处,appendix 表未逐页解析)。

3. **Pew 2025 的 TikTok 性别拆分存在票间冲突,须复核**(见上)。

4. **未做第三方对 Pew / Common Sense 口径的方法学批评或再分析检索**(三票 WebSearch 配额均耗尽,全部核对靠 WebFetch/curl 直取一手 URL)。特别是**自报屏幕时间与客观测量之间系统性偏差的文献**未覆盖。→ 这是覆盖面上的空缺,**不是已发现的反证**。

5. **Common Sense《The State of Kids and Families in America》2024/2025/2026 系列是否含 8–18 岁屏幕时长数字,未核。** 若含,则存在一个更新的(但非同口径的)替代数据源。→ **"此后无更新"应写作"截至 2026-07-27 未见同口径 census 更新",不得写"已停办"或"此后无任何更新"。**

6. **未取得 Common Sense 官方对"下一期 8–18 岁 census 是否/何时发布"的公开说明**(官网、2025 零到八岁报告页、sitemap 均无预告)。

---

## 证据分级

**多源证实(Pew 部分);单源已核 + 利益相关方口径(Common Sense 部分)。**

分层给分:

- **Pew 数据 —— 多源证实,证据强度最高。** 三票各自独立取得报告正文 HTML + 官方 topline PDF(逐页读取)+ 报告 PDF 图表三类一手件,四年序列、NET Daily、各平台 almost constantly 数值**三票完全一致,无一处冲突**(唯一例外是 2025 性别拆分,已单独标记)。Pew 为无党派机构、Advarra IRB、题干四轮一致可纵向比较、无平台方资金。**这一层可以放心承重。**
- **Common Sense 8:39 —— 单源已核,且来源为利益相关方(倡导组织)自发布、非同行评审。** 数字本身经三票逐字核对与官方 PDF 表格完全一致,方法学(Ipsos 概率抽样、n=1,306)披露完整;但发布方同时游说相关立法,数字与其倡导立场同向。**引用必须:(i) 披露倡导身份与资助方;(ii) 带三条构念限定语;(iii) 标注为 2021 年秋疫情期口径;(iv) 不得写成"如今"。**"无同口径更新"这一否定性主张由官方 sitemap 穷举 + URL 404 交叉确认,证据充分。
- **本组的判决性质**:数字层大部分成立,但**三票独立发现了同一个跨年串号(36% 归 2024)与同一个框架性过度概括("使用量未退潮")**。这两处是本组最承重的修正 —— 前者是硬性事实错误,后者会让整篇文章的剂量论证建立在一个被一手数据部分否定的前提上。


---

# C24 最终判决:CORRECTED(3/3 票)

组题:MCS/Kelly 剂量图 —— Haidt 自 Kelly Table 2 重绘、女孩 0→5+ 小时约 11%→38%(约三倍)/ 男孩约两倍;Kelly 原文完全调整模型衰减幅度(需核原表);Twenge 方"女孩×社媒 r≈.17-.20"回一手。

三票均取得 Kelly 一手全文(PMC + Europe PMC fullTextXML 两条独立路径),Table 1/2/3 逐字与数值**三票完全一致**。三票均独立推翻了 (b) 与 (c) 的出处归属。

---

## 锁定口径(成稿必须用)

### (A) Kelly 论文的正确引用
- Kelly Y, Zilanawala A, Booker C, Sacker A. "**Social Media Use and Adolescent Mental Health: Findings From the UK Millennium Cohort Study.**" **EClinicalMedicine, Volume 6, pp. 59–68.** DOI **10.1016/j.eclinm.2018.12.005**,PMID 31193561,PMCID PMC6537508。
- **年份口径**:Crossref 与 PubMed 的 issued / published-print 日期均为 **2018 年 12 月**(电子版 2019-01-04)。卷/页码正确;**"2019" 是含 Haidt 在内的通行误标。严谨引用应写 2018(或 "2018/2019",或直接用卷页)。**
- 样本:**N = 10,904**(女孩 n = 5,496,男孩 n = 5,408),平均年龄 14.3 岁(SD 0.34),MCS 第 6 次调查(14 岁波次)。
- 资助:ESRC ES/R008930/1,逐字 "The funder had no role in the study design; in the collection, analysis, and interpretation of data"。PubMed 记录无 ErratumIn / RetractionIn / CommentIn / UpdateIn 字段;Europe PMC 检索未发现勘误、更正或已发表的批判性再分析。无产业资助迹象。

### (B) Table 2 数值 —— Haidt 读数本身核对无误
**Table 2 标题逐字**:"Mean (geometric) depressive symptom scores and clinically relevant symptoms (percent) by social media use, explanatory factors and confounders."
**表注逐字**:"Estimates are weighted with sample weights."(**仅抽样加权,零协变量调整**)

临床相关症状比例(%):
| 每工作日社媒时长 | 女孩 | 男孩 |
|---|---|---|
| None | **11.2** | **7.4** |
| < 1h | 15.1 | 7.2 |
| 1–<3h | 18.1 | 6.8 |
| 3–<5h | 25.1 | 11.4 |
| ≥5h | **38.1** | **14.5** |

几何均数分:女孩 2.7 / 3.3 / 3.9 / 5.2 / 6.6;男孩 2.5 / 2.3 / 2.3 / 3.0 / 3.5。总体几何均数女 4.6 vs 男 2.5。

- **比值:女孩 38.1 ÷ 11.2 = 3.40 倍(不是"约三倍",是接近 3.4 倍);男孩 14.5 ÷ 7.4 = 1.96 倍("约两倍"成立)。**
- **Haidt 的读数与原表一致,无捏造。**

### (C) 【本组最大硬伤】Haidt 证词 Figure 5 图注的 "including controls" 与一手表不符
- **Haidt 参议院证词 Figure 5 图注逐字**:"Percent of UK adolescents with 'clinically relevant depressive symptoms' by hours per weekday of social media use, **including controls**. Haidt and Twenge created this graph from the data given in **Table 2** of Kelly, Zilanawala, Booker, & Sacker (2019), page 6."
- **但 Kelly 的 Table 2 是纯描述性双变量表,表注仅"Estimates are weighted with sample weights",没有任何协变量调整。**
- 推测成因:把表标题里的 "confounders" 一词(指该表另有若干混杂因素的**描述性行块**)误读成了"已调整"。
- **成稿必须指出:这张广泛流传的剂量曲线图是零调整的描述性百分比,图注的 "including controls" 是错的。**

### (D) 参照组口径错位 —— 论文回归的参照组是 1–<3h,不是 0h
- 原文逐字:"**1–3 h was the most prevalent category and is used as the reference category.**"
- **因此原文中根本不存在"0 小时 → 5+ 小时"的调整版梯度;该对比只存在于描述性表格。**
- **若改用论文自己的参照组重算比值:女孩 38.1/18.1 = 2.10x、男孩 14.5/6.8 = 2.13x —— 相对风险比上的性别差基本消失。**性别差体现在**绝对增量**(女 +20.0 个百分点 vs 男 +7.7 个百分点),不在倍数。

### (E) 分母极小且是选择性人群
- Table 1 暴露分布(加权 %):女孩 None **4.4** / <1h 19.0 / 1–<3h 33.4 / 3–<5h 17.7 / ≥5h 25.4;男孩 None **10.2** / 35.1 / 32.7 / 10.3 / 11.6。
- 原文逐字:"**Only 4% of girls reported not using social media compared to 10% of boys.**" 另有:"Over two-fifths of girls (43.1%) used social media for 3 or more hours daily, compared with one-fifth of boys (21.9%)."
- **女孩"零组"约 242 人(约 27 例达切点),男孩约 552 人。三倍梯度的左端锚点建在女孩样本中 4% 的非典型少数群体上;且男女零组占比相差一倍以上,使跨性别倍数比较本身不可比。Kelly 本人正是因此把参照组设在 1–3h。**

### (F) 男孩曲线非单调 —— "翻倍"只在两端成立
- 男孩:7.4 → 7.2 → 6.8 → 11.4 → 14.5。**轻中度使用者反而低于零使用组,最低点在 1–3h,呈 J 形。**
- 调整后同向:男孩 None 组 M0 = 1.01 (0.91–1.11) 无差异,但 M1(控制网络骚扰后)= 1.11 (1.01–1.23)、M4 = 1.10 (1.01–1.20),**显著高于 1–3h 参照组**。
- **写成"男孩也是两倍剂量-反应"会掩盖这一点。**

### (G) 【关键】"完全调整模型"在原文中不存在
- **模型定义逐字**:"Model 0 – social media use plus confounders (family income, family structure, age, internalising symptoms at age 11)" / "**Model 1 – M0 plus** online harassment" / "**Model 2 – M0 plus** sleep quantity and quality (sleep hours, latency and disruption)" / "**Model 3 – M0 plus** self-esteem" / "**Model 4 – M0 plus** body image"
- **M1–M4 各自只在 M0 上加一个变量,不是累加。论文没有同时纳入全部四组中介的模型。**
- 数值佐证非累加:女孩 ≥5h 的 M4 = 1.30 **高于** M2 = 1.28 与 M3 = 1.26(若累加则应单调递减)。
- **M0 本身已是混杂调整模型**,表注逐字:"All regressions adjust for covariates: family income and structure at age 14, internalising scores at age 11, and age and are weighted with sample weights." → **原文不存在真正的"未调整回归"。**
- **M1–M4 加入的是中介变量(通路分解),不是混杂控制。所谓"调整后衰减",衰减掉的是中介,不是混杂。**

### (H) Table 3 数值与衰减幅度(几何均数之比,参照组 1–<3h)
| | M0 | M1(+骚扰) | M2(+睡眠) | M3(+自尊) | M4(+身体意象) |
|---|---|---|---|---|---|
| 女孩 ≥5h | **1.50 (1.39–1.62)** | 1.30 (1.21–1.40) | 1.28 (1.19–1.38) | 1.26 (1.17–1.35) | **1.30 (1.21–1.40)** |
| 男孩 ≥5h | **1.35 (1.23–1.50)** | 1.27 (1.15–1.39) | 1.21 (1.10–1.34) | 1.31 (1.18–1.44) | **1.30 (1.19–1.42)** |
| 女孩 None | 0.74 (0.62–0.89) | 0.84 | 0.87 | 0.77 | 0.88 (0.76–1.01) |
| 男孩 None | 1.01 (0.91–1.11) | 1.11 (1.01–1.23) | — | — | 1.10 (1.01–1.20) |

- 3–5h 段两性 M4 均为 **1.17**;女孩 3–5h M0 = 1.26,男孩 3–5h M0 = 1.21。
- **衰减幅度(按"超出部分"计)**:女孩超额 0.50 → 0.26–0.30,**衰减约 40–48%**;男孩超额 0.35 → 0.21–0.31。**所有区间在各模型下仍显著。**
- **加入身体意象后,女孩相对男孩的"额外剂量效应"基本消失(两性均落到 ≥5h 1.30 / 3–5h 1.17)。**
- 女孩 None 组 M0 = 0.74(比参照低 26%)在加入中介后升至 0.77–0.88,M4 转为不显著 —— **"不用社媒的女孩更健康"在调整后不是干净证据。**

### (I) 统计量单位 —— 不是 OR
- 表注逐字:"**Regression coefficients have been exponentiated to aid interpretation.**" 因变量是**对数变换后的连续 SMFQ 分数**,系数取指数后为**几何均数之比**。
- **不可写成"患抑郁风险高 50%";正确表述是"抑郁症状得分高约 50%"。**
- 摘要逐字:"Compared with 1–3 h of daily use: 3 to < 5 h **26% increase in scores** vs 21%; ≥ 5 h **50% vs 35%** for girls and boys respectively." —— **这 50%/35% 对应 M0(已含混杂调整),不是原始未调整值。**
- **因此论文中没有任何一个调整后的估计对应 11%→38% 这个临床比例对比;不能说"调整后从 38% 降到某某%"。**

### (J) 结局构念 —— 二分变量是补充分析,不是诊断
- 原文逐字:"**In supplementary analysis** we derived a binary variable to capture the presence of clinically relevant symptoms using a cut point of ≥ 12"。
- 表注:"Moods and feelings score ranges from 0 to 26 and scores ≥ 12 indicate clinically relevant depressive symptoms."
- **SMFQ(13 项,近两周情感症状),≥12 是症状筛查阈值,不是临床诊断。**不可将 11.2%→38.1% 描述为"本文主要发现"或"临床抑郁症确诊率"。

### (K) 暴露构念含即时通讯 + 因果限定
- 问卷题干逐字:"On a normal week day during term time, how many hours do you spend on **social networking or messaging sites or Apps** on the internet such as Facebook, Twitter and **WhatsApp**?" → **含即时通讯类,不是纯"社交媒体"。**
- **暴露与结局同在 14 岁同一波次测量**(仅以 11 岁 SDQ 内化分做前置控制)。
- 作者自陈逐字:"**Findings are based largely on cross sectional data and thus causality cannot be inferred.**" / "caution is needed when interpreting our findings as the data used in this paper were, for the most part, cross sectional." / "Due to data availability we were not able to take account of some factors hypothesised to be on the pathway between social media use and poor mental health."
- 反向因果自陈逐字:"**a cyclical relationship between social media use and mental health could be at play, whereby young people experiencing poor mental health might be more likely to use social media for extended periods of time.**"

### (L) 【出处 REFUTED】"女孩 × 社媒 r ≈ .17–.20"
- **Haidt 证词 §2.4 原文逐字**:"What would the correlation be if we could just look at girls? Several studies have found that it is substantially larger than for boys. See Kelly, Zilanawala, Booker, & Sacker (2019), Nesi & Prinstein (2015), and Twenge, J.M. (2020). I know of no study that has found a larger relationship for boys. **A ballpark figure for the correlation just for girls is roughly r = .15 to r = .22.**"(注意:证词写的是 **.15–.22**,不是 .17–.20)
- **所引三个来源没有一个报告过女孩专属的这一量级 r**:
  - Kelly 2018/2019 报的是几何均数之比,**通篇无 r**;
  - **Nesi & Prinstein 2015**(J Abnorm Child Psychol 43:1427–1438, PMID 25899879, PMC5985443)的预测变量是 **MEIS-SCFS「技术媒介社会比较与寻求反馈」动机量表**(10 题 5 点,例题 "I use electronic interaction to see what others think about how I look"),**不是小时数**;n=619,12–16 岁(均龄 14.6),两波约隔一年;未报告女孩专属零阶 r;
  - "Twenge, J.M. (2020)" 所指无法在证词内确定(证词无参考文献列表,引用为超链接)。
- **可核到的最接近一手**:**Twenge JM, Haidt J, Lozano J, Cummins KM (2022), "Specification curve analysis shows that social media use is linked to poor mental health, especially among girls," Acta Psychologica 224:103512**,PMID 35101738,DOI 10.1016/j.actpsy.2022.103512,**CC BY 开放获取**。摘要逐字:"among girls, there is a consistent and substantial association between mental health and social media use (**median betas from −0.11 to −0.24**)"。
- **三点必须随之修正**:① 一手给的是**标准化回归 β 的中位数区间 −0.11 至 −0.24**(规格曲线分析跨三个数据集、成千上万种设定的中位数),**不是零阶相关 r**;② 区间比 .17–.20 宽得多;③ 符号为负是因为结局是"幸福感/心理健康"而非"抑郁"。**区间下端 .11 与 Orben (2020) 的 .10–.15 其实重叠。**
- **该文不是独立第三方**:是 Haidt 本人共同署名、对 Orben & Przybylski 2019 SCA 的对抗性再分析,重做时改动了四项设定(分开各类数字活动、男女分开、把中介移出控制变量、各量表等权)。
- **".17" 这个具体值不来自任何期刊论文**:Haidt 自己在 After Babel 中把它归给 **Chris Said 的博客分析**("a correlation of r = .17 could account for a 50% increase in the number of depressed girls in a population"),并写 "we're reaching a consensus that for girls the true value is north of r = .15, which is consistent with the values around .20 that Twenge, Lozano, Cummins and I found in our SCA paper"。**".17–.20" 是博客值与 SCA 值的拼合区间,不是任一篇一手论文的报告值。**
- **附带的引用错配**:证词 §2.2 把 "6 analytical choices…obscuring an association that is actually equivalent to a correlation coefficient of around r=.20" 归给 "a published response paper in the same journal"(即 Twenge, Haidt, Joiner & Campbell 2020, Nature Human Behaviour 4:346–348),**但真正重跑 SCA 并得出该数值的是 2022 年 Acta Psychologica 那篇,且后者摘要自述的是 4 项修订约束,不是 6 项。**(归属错配为"高度可能"而非"已确证",因 NHB 全文不可及)

### (M) (L) 的一手反证 —— 开放获取,建议并列呈现
**Orben A & Przybylski AK, "Reply to: Underestimating digital media harm," Nat Hum Behav 2020;4(4):349–351**, DOI 10.1038/s41562-020-0840-y, **PMC7116236(开放获取)**。**按 Twenge 等人自己提出的修改重跑后**:
- 中位 β = **−0.051**,解释方差 0.3%(原分析 β = −0.032, 0.4%)
- 分性别:**女性中位 β = −0.069,男性 −0.037**;技术使用对女孩幸福感变异的解释力 "nearly one half of one percent"
- 逐字:"**wearing glasses was still more negatively associated with well-being in adolescents than digital technology use (β_glasses = −0.061 vs β_technology = −0.051)**"
→ **同一场论战中对方的一手数据把"女孩 × 数字技术"放在 β ≈ .07 量级,与 r ≈ .17–.20 相差约 2.5–3 倍。该数值即便存在也属争议读数,且高度依赖"社交媒体专用测量 vs 泛数字技术"这一测量口径之争。**
- **引用 Twenge 方效应量时必须同时呈现被其反驳的原始 SCA 结果(median betas −0.01 至 −0.04)与本条 reply 的 −0.051。**

### (N) 【出处 REFUTED + 更正】"每小时 +13%"
- **不是 Vidal**:Vidal C, Lhaksampa T, Miller L, Platt R (2020), "Social media use and depression in adolescents: **a scoping review**," Int Rev Psychiatry 32(3):235–253, PMID 32065542, PMC7392374。经全文核查:设计为 scoping review(遵循 Arksey & O'Malley 2005 框架),**不合并效应量、不是 meta 分析,全文无「13%」、无任何每小时剂量-反应估计。**
- **正确出处**:**Liu M, Kamper-DeMarco KE, Zhang J, Xiao J, Dong D, Xue P (2022), "Time Spent on Social Media and Risk of Depression in Adolescents: A Dose-Response Meta-Analysis," Int J Environ Res Public Health 19(9):5164**, DOI 10.3390/ijerph19095164, PMID 35564559, PMCID PMC9103874。**判据**:Haidt 本人在 After Babel 该句上挂的超链接就是 pubmed.ncbi.nlm.nih.gov/**35564559**/。
- **逐字**:"The risk of depression increased by **13% (OR = 1.13, 95%CI: 1.09 to 1.17, p < 0.001)** for each hour increase in social media use in adolescents."

### (O) 引用 13% 时必须同时给出的限定
- **整体合并 OR = 1.60 (95%CI 1.45–1.75)**(两票逐字一致;见票间冲突裁决)
- 纳入 **26 项研究 / 30 份报告 / 55,340 人**,其中 **21 项横断面、仅 5 项纵向**
- **剂量-反应分析只基于 5 项研究、7 份报告** —— 逐字:"Five studies [6,17,19,20,54] (seven reports) were included for the dose–response analysis." **不是全部 26 项。**
- 异质性 **I² = 72.6%**(Q(29) = 105.9, p < 0.001);**Egger's p = 0.039**(提示发表偏倚),trim-and-fill 无需削补
- 剂量插补逐字:"the dose was calculated as the midpoint of the lower and upper boundaries in each group; for the open-ended lower or upper group, the boundary was assumed as the same as the closest group."
- 因果限定逐字:"**all included studies were observational... Hence, we cannot speak to causality in the interpretation of the results.**"
- 暴露为**自报**社媒时长;期刊为 MDPI 系(IJERPH)
- **性别口径(Haidt 转述说反了程度)**:**每小时 OR 女孩 1.13 (1.08–1.16)、男孩 1.09 (1.03–1.15)** —— **女孩值与总体 13% 完全相同,并未"更高";高的只是相对男孩。**另一口径的整体分性别合并 OR 女 1.72 (1.41–2.09) vs 男 1.20 (1.05–1.37),**勿与每小时 OR 混用。**
- **Haidt 转述句逐字**(After Babel):"A meta-analysis of **26** such studies found that the risk of depression increased by 13% for each hour increase on social media for adolescents (and that increase was **even higher for girls**)." → **两处口径错误:26 是整体合并的基数不是剂量-反应的基数;"even higher for girls" 说反了程度。**

### (P) 混淆源已排除
- **Liu M, Wu L, Yao S (2016)**, "Dose-response association of screen time-based sedentary behaviour... and depression: a meta-analysis," Br J Sports Med 50(20):1252–1258, PMID 26552416, PMC4977203。总体 **OR = 1.12 (1.03–1.22)**,极易被误当作 13% 的出处,**但它测的是总屏幕时间(电视/电脑/游戏)而非社交媒体**,且呈**非线性 J 型** —— 1 h/day 时风险反而最低 **OR = 0.88 (0.84–0.93)**;"those with 2.5, 3, 4 or ≥5 h of ST per day had an 8%, 19%, 46% and 80% increased risk relative to no ST"。16 项研究 / 127,714 人。**已排除为 13% 的出处。**

### (Q) 【跨论断非独立性】(a)(b)(c) 不是三条独立证据线
- **Liu 2022 纳入的 26 项研究中包含 Kelly 等人的英国 MCS 研究**(样本量 N = 10,904 完全一致)。
- **因此文章若同时把 Haidt 的 Kelly 剂量图和"13% per hour"并列为两条证据,属于同一份数据被数了两次。**
- (b) 的 Acta Psychologica SCA 与 (c) 的 meta 在作者群/数据集上亦有重叠(Liu 2022 剂量-反应参考文献 [6] = Twenge & Farley 2021)。
- **不可作为"多源互证"呈现。**

### (R) 利益相关
- **Twenge 与 Haidt 是"社媒有害"论的主要公开倡导者**(Haidt 著有《The Anxious Generation》,其个人站 jonathanhaidt.com/reviews 现 308 跳转至 anxiousgeneration.com 商业推广页)。Acta Psychologica 2022 与 NHB 评论均属对 Orben & Przybylski 的**对抗性再分析,选取设定的自由度较高**。→ **引用其效应量时应同时呈现被其反驳的原始 SCA 结果与 O&P 的 reply。**
- Kelly 等为 UCL 学术团队,ESRC 公共经费,未见商业利益冲突。

---

## 修正记录(修正前 → 修正后)

1. **【最大硬伤】(a) Haidt 图注 "including controls" 与一手表不符 —— 已证误。** 修正前:图注称该曲线 "including controls"。修正后:Kelly Table 2 是纯描述性双变量表,表注仅"Estimates are weighted with sample weights",**零协变量调整**;很可能是把表标题里的 "confounders" 误读成"已调整"。(1/3 票发现,两票在事实层同向支持"Table 2 是零调整描述性",无反驳,采纳)

2. **(a) "完全调整模型"这一提法本身不成立 —— 提问预设错误。** 修正前:预设存在一个"完全调整模型",问其衰减幅度。修正后:**Table 3 的 M1–M4 各自只在 M0 上加一个中介,不是累加;论文不存在同时纳入全部中介的模型。**且 **M0 本身已是混杂调整模型**,原文无真正的"未调整回归"。M1–M4 加的是**中介**(通路分解),不是混杂控制 —— **"调整后衰减"衰减掉的是中介。**(3/3 票一致)

3. **(a) 参照组口径错位(最关键的方法学修正)。** 修正前:以"0 小时"为基线得出"女孩三倍 vs 男孩两倍"的性别差。修正后:**论文回归参照组是 1–<3h**,逐字 "1–3 h was the most prevalent category and is used as the reference category";**原文中"0 小时 → 5+ 小时"这个对比从未进入任何调整模型。**若改用论文参照组,女孩 2.10x、男孩 2.13x,**倍数上的性别差基本消失**;性别差在绝对增量(+20.0pp vs +7.7pp)。(3/3 票一致)

4. **(a) 统计量单位错配。** 修正前:把 1.50/1.30 当作"临床相关抑郁"的比值比(OR)。修正后:因变量是**对数变换后的连续 SMFQ 分数**,系数指数化后为**几何均数之比**;不可写"患抑郁风险高 50%",须写"抑郁症状得分高约 50%"。**论文中没有任何一个调整后估计对应 11%→38% 这个临床比例对比。**(3/3 票一致)

5. **(a) 分母极小且是选择性人群。** 修正前:把"0 小时组"当作正常对照。修正后:女孩零组仅 **4.4%**(约 242 人,约 27 例达切点),男孩 10.2%;原文 "Only 4% of girls reported not using social media compared to 10% of boys"。**三倍梯度的左端锚点建在最小的一格上,且男女零组占比相差一倍以上,跨性别倍数比较本身不可比。**(3/3 票一致)

6. **(a) 男孩曲线非单调。** 修正前:暗示男孩也有单调剂量梯度。修正后:男孩 7.4 → 7.2 → 6.8 → 11.4 → 14.5,**轻中度使用者反而低于零使用组,呈 J 形**;M4 中男孩 None 组 1.10 (1.01–1.20) **显著高于**参照组。**"男孩也是两倍剂量-反应"会掩盖这一点。**(3/3 票一致)

7. **(a) 结局构念:二分变量是补充分析。** 修正前:当作主发现/临床诊断。修正后:原文 "In supplementary analysis we derived a binary variable…using a cut point of ≥ 12";SMFQ ≥12 是筛查阈值不是诊断。(2/3 票发现,一致)

8. **(a) 引用年份。** 修正前:"Kelly et al. 2019"。修正后:Crossref / PubMed 均为 **2018 年 12 月**(EClinicalMedicine Vol 6, Dec 2018, pp.59–68;电子版 2019-01-04)。"2019" 是通行误标。(2/3 票发现,一致)

9. **(a) 暴露构念含即时通讯。** 修正前:称"社交媒体"。修正后:问卷题干含 "messaging sites or Apps…such as Facebook, Twitter and **WhatsApp**",不是纯社媒;且暴露与结局同波次测量。(1/3 票发现,采纳)

10. **(a) 衰减幅度定量(补上原论断留白)。** 女孩 ≥5h M0 1.50 → M1 1.30 / M2 1.28 / M3 1.26 / M4 1.30;男孩 1.35 → 1.27 / 1.21 / 1.31 / 1.30。以"超出部分"计,**女孩超额 0.50 缩至 0.26–0.30(衰减约 40–48%)**,男孩超额 0.35 缩至 0.21–0.31;所有区间仍显著。**加入身体意象后两性 ≥5h 均落到 1.30、3–5h 均落到 1.17,女孩相对男孩的"额外剂量效应"基本消失。**(3/3 票数值完全一致)

11. **【(b) 出处 REFUTED】"r ≈ .17–.20"。** 修正前:"见 Twenge & Martin 2020(J Adolescence)或 Twenge et al. 2020 NHB 评论"。修正后:**Twenge & Martin 2020 摘要通篇不报告任何相关系数**(只用 "heavy users of digital media were often twice as likely as low users to be low in well-being" 这类比值表述);Haidt 证词 §2.4 所引三来源(Kelly / Nesi & Prinstein 2015 / Twenge 2020)**无一报告女孩专属的这一量级 r**。**可核到的最接近一手是 Twenge, Haidt, Lozano & Cummins 2022, Acta Psychologica 224:103512,给的是 median betas −0.11 至 −0.24(标准化 β 中位数区间,非零阶 r,区间宽得多)。**且证词原文写的是 **r = .15 到 r = .22**,不是 .17–.20。(3/3 票一致)

12. **(b) ".17" 不来自任何期刊论文。** 修正前:当作文献报告值。修正后:Haidt 自己在 After Babel 中把 .17 归给 **Chris Said 的博客分析**;".17–.20" 是博客值与 SCA 值的拼合区间。(1/3 票发现,给出 After Babel 逐字归因,采纳)

13. **(b) 附带引用错配。** 证词 §2.2 把 "6 analytical choices / r≈.20" 归给 NHB 2020 response paper,但真正重跑 SCA 得出该数值的是 2022 Acta Psychologica,且后者自述四项修订约束不是六项。**标为"高度可能"而非"已确证"**(NHB 全文不可及)。(1/3 票发现,采纳并降级)

14. **【(c) 出处 REFUTED + 更正】"每小时 +13%"。** 修正前:"疑为 Vidal et al."。修正后:**Vidal 2020 是 scoping review,不合并效应量,全文无 13%,归属被一手推翻;正确出处是 Liu M et al. (2022), IJERPH 19(9):5164**(判据:Haidt 该句的超链接直指 PMID 35564559)。(3/3 票一致)

15. **(c) 引用 13% 必须补齐限定。** 修正前:裸引数值。修正后:剂量-反应**仅基于 5 项研究 / 7 份报告**(不是 26 项);整体 OR = 1.60 (1.45–1.75);I² = 72.6%;Egger's p = 0.039;21 项横断 + 5 项纵向;剂量由分组中点插补;作者自述 "we cannot speak to causality";暴露为自报;MDPI 系期刊。**不可写成"每多用一小时,抑郁风险上升 13%"这种因果句式。**(3/3 票一致,各补一部分)

16. **(c) Haidt 转述的两处口径错误。** 修正前:照引"26 项研究…女孩更高"。修正后:① 26 是整体合并 OR 的基数,13% 只基于 5 项;② **"even higher for girls" 说反了程度** —— 每小时 OR 女 1.13 = 总体 13%,男 1.09,**女孩并未高于总体**;整体分性别 OR(女 1.72 vs 男 1.20)是另一口径,勿混用。(1/3 票发现,数值经另两票独立核实一致,采纳)

17. **(c) 已排除的混淆源。** Liu M, Wu L, Yao S (2016) BJSM 也是"剂量-反应 meta"且总体 OR = 1.12,极易误当出处,但测总屏幕时间且呈非线性 J 型(1h/day OR = 0.88)。**已排除。**(1/3 票发现,采纳)

18. **【新增】跨论断非独立性。** 修正前:(a)(b)(c) 当作三条独立证据线。修正后:**Liu 2022 纳入的 26 项研究中包含 Kelly 的 MCS 研究**;三条在底层数据与作者群上有重叠。**同时并列 Kelly 剂量图与"13% per hour"属同一份数据被数了两次,不可作为"多源互证"呈现。**(2/3 票发现,一致)

19. **【新增】必须并列呈现的一手反证。** Orben & Przybylski 2020 NHB reply(PMC7116236,开放获取):按 Twenge 等自己提出的修改重跑后,中位 β = −0.051,女性 −0.069、男性 −0.037,且 "wearing glasses was still more negatively associated with well-being … than digital technology use"。**与 r ≈ .17–.20 相差 2.5–3 倍。**(1/3 票取得,开放获取可复核,采纳)

### 票间冲突与裁决

- **冲突:Liu 2022 的整体合并 OR。** 第 1 票记为 **1.59 (1.44–1.77)**;第 2、3 票均给出摘要逐字 "**OR = 1.60, 95%CI: 1.45 to 1.75**"。
  - **裁决:采用 1.60 (1.45–1.75)。** 理由:两票各自独立引出同一句摘要逐字(第 3 票另经 PubMed efetch 与 Europe PMC 全文 XML 两条路径),属直接引语;第 1 票的数值无逐字支持,判为转录误差。

- **冲突:Kelly 是否落在 Liu 2022 剂量-反应的那 5 项研究之内。** 第 2 票称"剂量-反应参考文献 [19] 正是 Kelly et al. (2018) MCS";第 3 票称全文 XML 参考文献列表提取时被截断,仅确证 [6] = Twenge & Farley 2021,**未能确证 [17,19,20,54]**;第 1 票只说 Kelly 在 26 项纳入研究之中。
  - **裁决:只可主张"Kelly 的 MCS 数据落在 Liu 2022 的 26 项纳入研究之中"(已确证);不可主张"13%/小时 的剂量-反应估计由 Kelly 直接驱动"(未确证)。**成稿写"同一份 MCS 数据在两条证据线中重复出现",不写"13% 的斜率来自 Kelly"。

- **冲突:Kelly Table 3 的 M1–M4 是各自单加还是累加。** 第 3 票自陈两次独立抽取给出冲突答案(一次"各自单独加",一次 "progressively add");第 1、2 票均明确判为**各自在 M0 上单加**,并给出 Methods 逐字与数值佐证(女孩 M4 = 1.30 **高于** M2 = 1.28 与 M3 = 1.26,若累加应单调递减)。
  - **裁决:判为各自单加。** 理由:Methods 逐字("Model 1 – M0 plus…"/"Model 2 – M0 plus…")与数值非单调两条独立证据同向。**结论:论文根本不存在"把四组中介一并调整后的最终模型",不得称 M4 为"完全调整模型"。**数值本身不受影响(三票已互校一致)。

---

## 未回溯项(不得承重或须标未验证)

1. **【核心未决】"r ≈ .17–.20"(以及证词原文的 .15–.22)的确切数值,在本次可及的任何一手文献中均未逐字出现。**
   - **Twenge, Haidt, Joiner & Campbell (2020), "Underestimating digital media harm," Nature Human Behaviour 4:346–348** 全文不可及。三票合计尝试至少 8 条独立路径全部失败:nature.com 303 跳转至 idp.nature.com 登录墙;Unpaywall is_oa = false 且 oa_locations 为空;PMC ID Converter 确认无 PMCID;Semantic Scholar 摘要被出版方 elided、openAccessPdf 为空;OpenAlex best_oa_location 为 null;CORE.ac.uk 403;scholar.archive.org 无全文;作者主页 jeantwenge.com/publications 404、jonathanhaidt.com 已 308 跳商业站;web.archive.org 在部分环境被禁用;Semantic Scholar snippet 接口 429。**未使用 Unpaywall 邮箱查询串(隐私约束),未使用盗版镜像。**
   - **Twenge & Martin (2020), J Adolescence 79:91–102** 正文与表格不可及(Unpaywall is_oa=false / oa_status=closed / has_repository_copy=false;ScienceDirect 与 Wiley 402/403;ResearchGate 403)。**仅核到完整摘要,其中不含任何相关系数。**因此不能排除正文表格中存在 r ≈ .17–.20 量级的系数,但可确认该数值不是该文摘要或结论所报告的效应量口径。
   - **→ 判定:未回溯,不得承重。** 若正文必须保留,须标注为"**Twenge 方读数、有争议、未回溯到一手**",并同时给出 Orben & Przybylski 2020 reply 的 −0.051 / 女性 −0.069 作对照。**建议改用可核的替代表述**:Acta Psychologica 2022 的 median betas −0.11 至 −0.24(须注明是 Haidt 共同署名的对抗性再分析),或 Liu 2022 的性别分层 OR(女 1.72 vs 男 1.20),或 Twenge & Martin 摘要的 "heavy users 约为 low users 的两倍"。
   - 次级未决:.17–.20 究竟指哪种统计量(Pearson r / 标准化 β / 转换后效应量)、哪个数据集(MTF / YRBSS / MCS)、对应哪个结果变量(抑郁症状 / 低幸福感 / 自杀风险因素),三项均不定 —— **这三项不定,数值本身无法被正确解读。**

2. **NHB 2020 评论的归属错配未确证。**证词把 "6 analytical choices" 与 "r≈.20" 都归给 NHB 3 页评论,但 SCA 重跑与 median betas −0.11~−0.24 明确出自 2022 Acta Psychologica。**因 NHB 全文不可及,该归属错配为"高度可能"而非"已确证"。**

3. **Liu 2022 剂量-反应那 5 项研究的具体构成([17,19,20,54])未逐项核到**;13% 是否为线性剂量-反应模型的斜率、5 项纵向研究是否单独也支持该斜率,未核到 forest plot / 敏感性分析层级。→ **不得主张"纵向研究单独也支持 13%"。**

4. **Kelly Table 2 各社媒时长格子的原始(未加权)分子/分母例数未在可及内容中给出。** 文中"女孩零组约 242 人、约 27 例达切点、男孩约 552 人"系由 Table 1 加权百分比 × 分性别样本量推算,**属推导值而非原文报告值**。若正文要写病例数,应回原表或补充材料确认。

5. **Kelly 的利益冲突声明未能从可取回的 XML/PMC 版本中逐字提取到**(仅取到资助声明 ESRC ES/R008930/1)。已排除撤稿与勘误,但 COI 原文未核。

6. **Kelly 2018/2019 的勘误/批判性再分析检索为宽泛检索的阴性结果**(Europe PMC 检索式含 erratum/correction/reanalysis/comment),证据力有限。

7. **Acta Psychologica 与 IJERPH 两刊近年的 Web of Science 收录状态变动未能核实**(可能影响来源质量评估;三票 WebSearch 配额均已耗尽 200/200)。**不作为证据使用,但 MDPI 系期刊身份应在引用 Liu 2022 时披露。**

---

## 证据分级

**分层给分,三条子论断证据等级差异极大,不可混为一谈:**

- **(a) Kelly Table 2/3 数值 —— 多源证实(最高级)。** 三票各自经 PMC 网页版 + Europe PMC fullTextXML 两条独立路径取得全文,Table 1/2/3 的每一格数值、模型定义逐字、表注逐字、摘要逐字**三票完全一致,无一处冲突**。UCL 学术团队、ESRC 公共经费、无勘误撤稿、无商业利益冲突。**数字层可以放心承重。**
- **(a) Haidt 图注 "including controls" —— 已证误(本组唯一硬性误述)。** 一手表注与图注直接矛盾,可复核,应在文章中点明。
- **(a) 的解释层 —— 方向存争 / 须大幅降级。** 该曲线是**零调整的描述性百分比**、参照组错位、左端分母仅 4.4%、男孩非单调、统计量是几何均数之比而非 OR、暴露含即时通讯、暴露与结局同波次测量、论文自陈 "causality cannot be inferred" 且明说反向因果可能。**这张图能承重的只是"14 岁女孩中重度使用者的抑郁症状筛查阳性率明显更高"这一描述性事实,不能承重剂量-反应因果,更不能承重"女孩受害是男孩三倍"。**
- **(b) r ≈ .17–.20 —— 未验证(不得承重)。** 三票均未能回到一手;可核到的最接近值是 Haidt 本人共同署名的对抗性再分析给出的 median betas −0.11 至 −0.24;而同一论战对方的开放获取一手 reply 给出 −0.051(女性 −0.069),相差 2.5–3 倍。**这是一个"方向存争 + 关键数值未回溯"的双重降级项。**
- **(c) 13% per hour —— 单源已核(一手逐字),但研究本身证据位阶低。** 出处已由三票一致更正并有 Haidt 自己的超链接作判据;但该 meta 为 MDPI 系期刊、剂量-反应仅基于 5 项研究、21/26 为横断、I² = 72.6%、Egger's p = 0.039 提示发表偏倚、剂量由中点插补、暴露自报、作者自陈不可言因果。**须带全部限定引用,不得用因果句式。**
- **【结构性警告】(a)(b)(c) 在底层数据与作者群上重叠(Kelly 的 MCS 落在 Liu 2022 的 26 项之中),不可作为"多源互证"呈现。**
