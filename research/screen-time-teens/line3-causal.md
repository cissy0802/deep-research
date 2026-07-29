# L3 因果证据:自然实验与 RCT

调研日期:2026-07-27。负责范围:社媒/屏幕的自然实验与减用/戒断 RCT、相关 meta 分析、broadband 自然实验、Instagram 内部研究。学校禁手机政策评估不在本线(另线负责)。

---

## 一、Braghieri, Levy & Makarin 2022(Facebook 大学 rollout 自然实验)

### 论断 1:设计与主效应 —— Facebook 引入使大学生"poor mental health 指数"上升 0.085 SD
- 设计:利用 2004-2006 年 Facebook 在美国大学间**分批(staggered)开放**的自然实验,generalized difference-in-differences。数据:775 所大学的 Facebook 开放日期(前 100 所来自已发表研究,其余 675 所用 Wayback Machine 重建,误差约 ±2 天)× **NCHA(National College Health Assessment)连续 17 波、43 万+ 份**学生自报问卷。
- 原文:"Our index of poor mental health, which aggregates all the relevant mental health variables in the NCHA survey, increased by 0.085 standard deviation units as a result of the introduction of Facebook."
- 结局口径:**自报症状**(NCHA 问卷,"last year felt hopeless / severely depressed / anxiety disorder…"),非临床诊断、非住院记录;子指数:depression symptoms、other conditions、depression services(诊断/心理治疗/抗抑郁药三项点估计为正但常规水平不显著;相对基线均值分别约 +13%/+20%)。
- 来源:Braghieri, Levy & Makarin, "Social Media and Mental Health," *American Economic Review* 2022, 112(11): 3660–3693. https://alexeymakarin.github.io/assets/Braghieri_Levy_Makarin_AER_2022.pdf ;AEA 页 https://www.aeaweb.org/articles?id=10.1257%2Faer.20211218 【研究】(已直接核对 PDF 原文 pp.3660-3667, 3676-3679)

### 论断 2:效应量的三个基准换算(作者自给)
逐字(AER p.3662):
1. "this magnitude is around **22 percent of the effect of losing one's job** on mental health, as reported in a meta-analysis by Paul and Moser (2009)."
2. "equivalent to a **2 percentage point increase in the share of students suffering from depression** according to the PHQ-9 **over a baseline of 25 percent**."
3. "Under a set of **relatively strong assumptions**, we calculate that the introduction of Facebook accounts for approximately **24 percent** of the increased prevalence of severe depression among college students over the last two decades."(back-of-the-envelope,作者自己标注强假设)
- 来源:同上【研究】

### 论断 3:稳健性与"安慰剂"检验
- 事件研究(event study)显示 **无 pretrends**:"the coefficients on the semesters prior to the introduction of Facebook at a college are all close to zero and exhibit no discernible pretrends"(p.3677)。
- 对 staggered DiD 的近年计量批评做了应对:TWFE OLS 之外用 Sun & Abraham (2021)、Callaway & Sant'Anna (2021)、de Chaisemartin & d'Haultfoeuille (2020)、Borusyak et al. (2021) 四种稳健估计量复核,方向一致;稳健估计量下 post 期效应**随暴露时间递增**(至 +2 学期约 0.2-0.35 SD,TWFE OLS 较平),作者倾向"length-of-exposure"解释。
- 机制:效应集中于更易做不利社会比较的群体(住校外、低 SES、非兄弟会/姐妹会成员);对饮酒之外的药物使用、身体健康等替代通道无显著证据。
- 来源:同上【研究】

### 论断 4:作者限定语(逐字)与后续批评情况
逐字(AER p.3663):
- "The results…should be interpreted with caution for several reasons. First, our estimates **cannot speak directly to the effects of social media features (e.g., news pages) that were introduced after the time period we analyze**…"
- "Second, despite being the core component of most mental health diagnoses, **self-reports may still suffer from measurement error** due to recall bias, lack of incentives, and social image concerns."
- "Finally, we note that our estimates are **local to college students**…future research should test whether social media has a similar effect on the mental health of other demographic groups."
- 另注:"our results do not imply that the overall welfare effects of social media are necessarily negative."
- 后续批评/复现:本次检索(2026-07)**未找到已发表的正式 Comment/复现挑战**(AER 无 comment 记录,搜索未见反驳论文);学界引用总体正面(获 2022 ESEM 最佳论文奖)。注意这是"未检得",不等于"无争议"——怀疑派(如 Ferguson 阵营)一般批评点在:NCHA 为重复截面而非个体面板、无个体层面 Facebook 使用数据(是 intent-to-treat 的"校园开放"处理)、自报结局。【研究/检索状态说明】

---

## 二、Allcott, Braghieri, Eichmeyer & Gentzkow 2020(付费停用 Facebook 4 周 RCT)

### 论断 5:停用 Facebook 4 周使主观幸福感指数提高 0.09 SD
- 设计:通过 Facebook 广告招募 2,743 名用户(2018 年美国中期选举前),要求日均使用 >15 分钟;引出 4 周停用的 willingness-to-accept(WTA),**将 WTA < $102 的 61% 受试者随机分组**,处理组付费停用 4 周,合规通过公开 profile 页核查,合规率 >90%,endline 失访 <2%。RCT 注册:AEA registry **AEARCTR-0003409**;IRB:Stanford、NYU。
- 效应(逐字,working paper p.4):"Our overall index of subjective well-being improved by **0.09 standard deviations**. As a point of comparison, this is about **25-40 percent of the effect of psychological interventions** including self-help therapy, group training, and individual therapy, as reported in a meta-analysis by Bolier et al. (2013)."(happiness、life satisfaction、depression、anxiety 单项均改善;每日短信情绪测量为正但不显著)
- 关键限定(逐字):"we also show that **the magnitudes of our causal effects are far smaller than those we would have estimated using the correlational approach** of much prior literature."
- 其他发现:停用释放约 60 分钟/天;停用者事后使用持续下降(post-experiment use 指数 −0.61 SD),约 80% 处理组认同停用对自己有好处。
- 样本口径注意:成年 Facebook 用户(自选样本、WTA≤$102),**不是青少年**。Braghieri et al. 2022 脚注指出该样本的选择性:"includes participants who reported using Facebook more than 15 minutes per day and were willing to accept $102 to deactivate."
- 来源:Allcott, Braghieri, Eichmeyer & Gentzkow, "The Welfare Effects of Social Media," *AER* 2020, 110(3): 629-676. PDF: https://web.stanford.edu/~gentzkow/research/facebook.pdf ;AEA 页 https://www.aeaweb.org/articles?id=10.1257%2Faer.20190658 【研究】(已核对 PDF pp.1-4)

---

## 三、2020 大选前 Meta 合作大型停用实验(2024 PNAS + 2025 NBER)

### 论断 6:史上最大停用实验 —— Facebook 停用 6 周改善情绪状态 0.060 SD;Instagram 0.041 SD(后者未过预注册显著性门槛)
- 设计:U.S. 2020 Facebook and Instagram Election Study(Meta 研究者 + 不受薪独立学者合作;"the independent academic authors had final authority over the pre-analysis plan, data analysis, and manuscript text, and Meta could not block any results from being published")。**19,857 名 Facebook 用户、15,585 名 Instagram 用户**(日均 ≥15 分钟),27% 随机分入停用组($150 停用 6 周),对照组 $25 只停用第 1 周(巧妙设计:两组都经历"停用",压 demand effect 与差异性流失)。预注册:OSF https://osf.io/t9q2f 。
- 效应(NBER w33697 摘要逐字):"People who deactivated Facebook for the six weeks before the election reported a **0.060 standard deviation improvement** in an index of happiness, depression, and anxiety, relative to controls…People who deactivated Instagram for those six weeks reported a **0.041 standard deviation improvement**."
- 显著性口径:Facebook 效应 p<0.01 且**经多重检验校正后仍显著**;Instagram 效应单独看 p=0.016,但**校正后 p=0.14,"does not meet our pre-registered p = 0.05 significance threshold"**。
- 异质性(非预注册、探索性):"the Facebook effect is driven by **people over 35**, while the Instagram effect is driven by **women under 25**."(Instagram × 年轻女性正好是 Haidt 论点最关键的人群——但这是探索性分析)
- 基准:平均心理干预 = 0.27 SD(van Agteren et al. 2021 meta);2008-2022 年轻人情绪状态指数恶化 0.37 SD;共和党 vs 民主党人差 0.48 SD。
- 机制:app 计量数据显示**停用释放的时间大部分(IG 为全部)转移到其他手机 app**,并非转向线下生活。
- 作者限定(逐字,w33697 pp.6-7):"our findings are only directly informative about the people who agreed to participate and deactivate their accounts for the payments we offered";"our experiment measures the effects of an incremental five weeks of individual deactivation before the 2020 election. Effects could differ for longer-term deactivation, simultaneous deactivation of many users, deactivation during a non-election period";"the baseline emotional state outcomes were imbalanced by chance in the Facebook sample"。并特别指出对 Braghieri 2022 的外推警告:"Facebook's user experience was very different during that rollout period—for example, there was no news feed—so the effects could be quite different two decades later."
- 来源:Allcott, Gentzkow, Wittenbrink et al., "The Effect of Deactivating Facebook and Instagram on Users' Emotional State," NBER WP 33697, April 2025. https://www.nber.org/system/files/working_papers/w33697/w33697.pdf 【研究(NBER WP,注明未经同行评审)】(已核对 PDF pp.3-8);政治结局姊妹篇:Allcott et al., PNAS 2024, 121(21) e2321584121. https://www.pnas.org/doi/10.1073/pnas.2321584121 【研究】

---

## 四、减用/戒断 RCT 谱系

### 论断 7:Hunt et al. 2018("No More FOMO")—— 限用 30 分钟/天减少孤独与抑郁
- 设计:143 名宾大本科生,随机分为"Facebook/Instagram/Snapchat 每平台每天 ≤10 分钟(合计约 30 分钟)"vs 照常使用,3 周,凭 iOS 电池截图核查用量。**构念是"限用"不是戒断**。
- 结果:限用组孤独感与抑郁显著低于对照;抑郁改善集中于基线高抑郁者(限用组高基线者 BDI 均值 23 → 14.5;低基线者 5.1 → 4.1,统计显著但无临床意义)【转述,待核:BDI 具体数字来自检索摘要,未直接核对原文表格】。两组的焦虑与 FOMO 都较基线下降(作者解释为自我监测本身的作用)。
- 未预注册;样本小、单校本科生。
- 来源:Hunt, Marx, Lipson & Young, *Journal of Social and Clinical Psychology* 2018, 37(10): 751-768. https://guilfordjournals.com/doi/10.1521/jscp.2018.37.10.751 【研究】

### 论断 8:Tromholt 2016 —— 戒 Facebook 1 周提高生活满意度(小效应、方法弱)
- 设计:丹麦,1,095 名志愿者(经 Facebook 招募、86% 女性)随机分组,处理组戒 Facebook 1 周,87% 自报全周合规。
- 结果:处理组生活满意度显著更高(组间差约 **0.37 分,量表 1-10**,p<0.001),正面情绪更多;效应在重度用户、被动使用者、易嫉妒者中更大。
- 弱点:未预注册、结局自报、志愿者自选样本、无法排除 demand effect(当时即有 Neuroskeptic 等批评)。
- 来源:Tromholt, "The Facebook Experiment: Quitting Facebook Leads to Higher Levels of Well-Being," *Cyberpsychology, Behavior, and Social Networking* 2016, 19(11). https://www.liebertpub.com/doi/10.1089/cyber.2016.0259 【研究】;批评见 https://www.discovermagazine.com/mind/if-you-want-to-be-happy-quit-facebook 【媒体】

### 论断 9:Lambert et al. 2022 —— 全平台停用 1 周改善幸福感/抑郁/焦虑
- 设计:154 名英国成人(均龄 29.6),随机停用 Facebook/Instagram/Twitter/TikTok 1 周 vs 照常。
- 结果:组间差 well-being(WEMWBS)**MD 4.9, 95% CI [3.0, 6.8]**;depression(PHQ-8)**MD −2.2 [−3.3, −1.1]**;anxiety(GAD-7)**MD −1.7 [−2.8, −0.6]**,均利于停用组。
- 注意:成人样本、1 周、自报结局。
- 来源:Lambert, Barnstable, Minter, Cooper & McEwan, *Cyberpsychology, Behavior, and Social Networking* 2022, 25(5). https://journals.sagepub.com/doi/10.1089/cyber.2021.0324 【研究】

### 论断 10:Castelo et al. 2025(PNAS Nexus)—— 手机断网 2 周,效应量最大但合规率最低
- 设计:467 名美加 iPhone 用户(Prolific 招募,均龄 32),Freedom app **屏蔽手机上所有移动互联网(Wi-Fi+流量,保留电话短信、电脑上网)2 周**,随机交叉(延迟干预组先做对照)。预注册 OSF https://osf.io/tfdm6 。手机使用从约 314 分钟/天降到 161 分钟/天。
- 效应(ITT):sustained attention(gradCPT 客观任务)**dz = 0.23**, p<0.001("about the same magnitude as 10 years of age-related decline");mental health(DSM-5 Level 1 跨症状量表)**dz = 0.56**, p<0.001;subjective well-being **dz = 0.45**, p<0.001。TOT 更大(0.26/0.68/0.50)。91% 受试者三项结局至少一项改善。
- 争议点:论文称抑郁症状效应(dz=0.56)"larger than the meta-analytic effect of antidepressants"(引 Kirsch et al. 2008)——该对比本身有口径问题(within-subject dz vs 药物试验组间 d;Kirsch 的抗抑郁药 meta 又是出名有争议的基准)。
- 合规:仅 **25.5% 达到预注册合规标准**(≥10/14 天保持屏蔽);只有 56.8% 装了 app。
- 作者限定(逐字):"Our sample consisted mostly of individuals motivated to reduce their smartphone use";"Expectancy effects, such as placebo and demand effects, could have contributed to our findings"。
- 构念注意:干预是**"移动互联网"整体**,不是社媒,更不是"屏幕时间"(手机仍可打电话发短信、电脑仍可上网)。成人样本。
- 来源:Castelo, Kushlev, Ward, Esterman & Reiner, "Blocking mobile internet on smartphones improves sustained attention, mental health, and subjective well-being," *PNAS Nexus* 2025, 4(2): pgaf017. https://academic.oup.com/pnasnexus/article/4/2/pgaf017/8016017 ;全文 https://pmc.ncbi.nlm.nih.gov/articles/PMC11834938/ 【研究】

### 论断 11:零效应 RCT 同样存在 —— Hall 2021、Przybylski et al. 2021
- Hall, Xing, Ross & Johnson, "Experimentally manipulating social media abstinence: results of a four-week diary study," *Media Psychology* 2021, 24(2): 259-275:N=130,随机分 0/1/2/3/4 周戒断五组,**"no main effect of social media abstinence"**,戒断时长与结局变化无关。 https://www.tandfonline.com/doi/abs/10.1080/15213269.2019.1688171 【研究】
- Przybylski, Nguyen, Law & Weinstein, "Does Taking a Short Break from Social Media Have a Positive Effect on Well-being? Evidence from Three Preregistered Field Experiments," *Journal of Technology in Behavioral Science* 2021, 6: 507-514:三个**预注册**田野实验,1 天/1 周休停,未发现对情绪与满意度的正效应。【研究】
- (背景:Vuorre & Przybylski 阵营与 Haidt 阵营互相批评对方方法——Sigaud, Rausch, McClean & Haidt 2026 撰文批评 Vuorre & Przybylski 三篇论文, https://journals.sagepub.com/doi/10.1177/21677026261425910 【研究/评论】)

---

## 五、RCT meta 分析(2023-2026):正反都有

### 论断 12:说"有效"的 meta —— May, Malouff & Meynadier 2025:减用社媒使抑郁症状下降 g≈0.25
- 10 项 RCT,N=1,491(75% 女性,均龄 24.2);抑郁合并效应 **Hedges g = 0.28 [0.13, 0.43]**,trim-and-fill 校正发表偏倚后 **g = 0.25 [0.10, 0.41]**;I² = 47.3%。
- 细节:限用型干预 g = 0.33 显著,完全戒断型 g = 0.15 不显著(二者差异不显著);干预时长、平台数不是显著调节变量。纳入试验含 Lambert 2022、Hunt 2023、Thai 2021、Brailovskaia 2020/2022、Faulhaber 2023 等。
- 局限(作者自报):10 项中仅 4 项含不合规者(其余非严格 ITT);最长干预仅 3 周;无长期随访。
- 来源:May, Malouff & Meynadier, "Reducing Social Media Use Decreases Depression Symptoms: A Meta-Analysis of Randomised Controlled Trials," *European Journal of Investigation in Health, Psychology and Education* 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12651081/ 【研究】

### 论断 13:说"无效"的 meta —— Lemahieu et al. 2025(Sci Rep)与 Ferguson 2024
- Lemahieu et al. 2025, *Scientific Reports*:社媒**戒断**干预,10 项研究、N=4,674、38 个效应量:positive affect **g = 0.03 [−0.11, 0.16]**、negative affect **g = −0.01 [−0.13, 0.10]**、life satisfaction **g = 0.03 [−0.17, 0.22]**,全部不显著;I²≈60%。结论逐字:"The analyses revealed no significant effects of social media abstinence interventions on positive affect, negative affect, or life satisfaction."(注意结局是**情感/生活满意度**,不含抑郁症状) https://www.nature.com/articles/s41598-025-90984-3 【研究】
- Ferguson 2024, "Do social media experiments prove a link with mental health: A methodological and meta-analytic review," *Psychology of Popular Media*:27 项实验研究,结论为效应与零无统计差异。https://www.researchgate.net/publication/380304294 【研究】
  - 对 Ferguson 的正式批评:Rausch & Haidt, "Why Ferguson's Meta-Analysis Should Not Be Used to Inform Debates on Social Media's Impact on Depression and Anxiety," SSRN 5224958, https://doi.org/10.2139/ssrn.5224958 【研究/评论】;After Babel 三连文指其效应量、样本量、纳排标准存在多处事实错误(https://www.afterbabel.com/p/the-case-for-causality-part-1)【博客/Substack,有立场】。
- 同名作者另一篇易混:Ferguson, Kaye, Branley-Bell & Markey, "There Is No Evidence That Time Spent on Social Media Is Correlated With Adolescent Mental Health Problems," *Professional Psychology: Research and Practice* 2024(APA, doi 10.1037/pro0000589):这是 **46 项青少年研究的相关性 meta**,不是实验证据(已核对 PDF 首页摘要:"the current pool of research is unable to support claims of harmful effects")。 https://christopherjferguson.com/Social%20Media%20Meta.pdf 【研究】

---

## 六、其他自然实验:broadband/光纤 rollout

### 论断 14:Donati et al.(意大利)—— 宽带接入使年轻世代精神障碍住院诊断上升 0.08 SD
- 设计:意大利 2001-2013 医院精神障碍诊断全量行政数据 × 市镇级宽带可得性;工具:与旧语音电信基础设施的距离(前互联网时代无关、宽带时代变关键)。
- 结果:宽带使 1985-1995 出生世代精神障碍患病率上升 **0.08 SD**,1974-1984 世代无影响;不利效应由 20 岁前暴露者驱动。**结局是住院/临床诊断,非自报**——是对"自报偏误"批评的最强回应之一。
- 来源:Donati, Durante, Sobbrio & Zejcirovic, "Lost in the Net? Broadband Internet and Youth Mental Health," *Journal of Health Economics* 2025(先行版 IZA DP 15202 / SSRN 2022). https://www.sciencedirect.com/science/article/pii/S0167629625000529 ;https://ssrn.com/abstract=3949645 【研究】

### 论断 15:Golin(德国)与 Arenas-Arroyo et al.(西班牙)—— 性别不对称:伤女孩不伤男孩
- Golin 2022,*Health Economics* 31(S2): 6-21:德国 GSOEP 住户坐标 + 电信网络技术特征做工具变量,宽带使 **17-30 岁女性**心理健康变差(男性无),拉大心理健康性别差;社交行为与情绪应对能力恶化。效应量未在摘要给出【转述,待核:SD 数值需查原文】。 https://pubmed.ncbi.nlm.nih.gov/35833231/ 【研究】
- Arenas-Arroyo, Fernández-Kranz & Nollenberger, "High Speed Internet and the Widening Gender Gap in Adolescent Mental Health: Evidence from Spanish Hospital Records," *Journal of Health Economics* 2025(IZA DP 15728):2007-2019 西班牙各省光纤部署 × **医院出院诊断记录**:青少年女孩心理/行为住院显著上升、男孩无;机制:成瘾性上网、睡眠剥夺、作业与家庭社交减少(均由女孩驱动),父女关系质量受损;**未发现网络霸凌增加的证据**。 https://www.sciencedirect.com/science/article/pii/S0167629625000499 ;https://repec.iza.org/dp15728.pdf 【研究】
- 构念注意:这组研究的处理是"高速互联网接入"(靠近 Haidt 的"智能手机时代"论,但不是社媒本身,也不是屏幕时间);结局是临床/住院口径。

---

## 七、Instagram 内部研究(Facebook Files)

### 论断 16:"1 in 3 teen girls" 的原始口径与后续澄清
- 原始泄露 slide(2019 内部演示,WSJ 2021-09-14 报道)逐字:"We make body image issues worse for one in three teen girls."
- 底层数据口径(2020 年 3 月内部演示):**32% 的"已经对身体形象感觉不好"的青少年女孩**说刷 Instagram 让感觉更糟——分母是已有身体形象困扰的女孩,不是全体女孩;数据是**自我感知影响的问卷调查**(teens' own perceptions),不是因果估计、不是诊断。
- Meta 回应(2021-09-26 发布带注释的两套 slide):在 12 个议题中的 **11 个**(孤独、焦虑、悲伤、进食问题等),报告有困扰的女孩中说 Instagram "使之更好"多于"使之更糟";body image 是唯一"更糟居多"的议题——且即便该项,多数有困扰女孩仍报告"更好或无影响"。
- 定位:这是**内部非同行评审的描述性调查**,证据等级低于本线所有学术研究;它的意义在"公司自己知道什么",不在效应量。
- 来源:WSJ Facebook Files 报道(转述见 Time 汇总 https://time.com/6097704/facebook-instagram-wall-street-journal/ 【媒体】);Meta 官方回应与注释 slide:"What Our Research Really Says About Teen Well-Being and Instagram," https://about.fb.com/news/2021/09/research-teen-well-being-and-instagram/ 【官方(涉事公司,有立场)】;泄露 slide 汇总 https://digitalwellbeing.org/the-facebook-files-on-instagram-harms-all-leaked-slides-on-a-single-page/ 【博客】;Slate 报道 https://slate.com/technology/2021/09/instagram-facebook-body-image-documents-wall-street-journal.html 【媒体】

---

## 八、方向汇总(论断 17):因果证据版图

**发现负效应(社媒→心理健康变差)的设计:**
- 平台整体引入类(效应最可外推到"总体影响"):Braghieri 2022(0.085 SD,自报);Donati 2025(0.08 SD,住院诊断);Golin 2022、Arenas-Arroyo 2025(女性/女孩特异,临床口径)。量级稳定在 **≈0.08-0.1 SD**,且四项相互独立(美/意/德/西,自报与住院口径都有)。
- 个体停用/减用 RCT:Allcott 2020(0.09 SD);Allcott et al. 2025(FB 0.060 SD 稳;IG 0.041 SD 未过校正门槛);Tromholt 2016、Hunt 2018、Lambert 2022(小样本、正向);Castelo 2025(断移动互联网,dz 0.45-0.56,但合规低、期待效应未排除)。
- meta:May et al. 2025 抑郁 g=0.25。

**发现零效应的设计:**
- Hall 2021(4 周戒断,零);Przybylski et al. 2021(3 个预注册实验,零);Lemahieu 2025 meta(情感/生活满意度,g≈0.00-0.03);Ferguson 2024 meta(27 项实验,零——但被指存在数据错误)。

**能对齐的读法:** 短期个体戒断对**情感/幸福感**的效应在零附近,对**抑郁症状**的合并效应约 g 0.2-0.3;单平台停用 4-6 周约 0.04-0.09 SD;平台/网络"进入整个社区"的自然实验约 0.08 SD 且随暴露时间增长、集中于女性与易感者。**没有任何一个因果设计支持"0 效应+方向存疑"的强怀疑立场,也没有任何一个支持"社媒是青少年心理危机主因"量级(如解释 0.37 SD 恶化的大头)的强因果论断**——Braghieri 的 24% back-of-envelope 是目前最接近后者的估计,且作者自标"relatively strong assumptions"。

---

## 交叉口径问题(待核清单)

1. **媒体转述的 "7% 严重抑郁、8% 焦虑上升"(Braghieri)**:检索摘要与 MIT Sloan 新闻稿口径,论文正文主打的是 0.085 SD 与 PHQ-9 换算;7%/8% 应为相对基线的百分比换算,**未在本次读取的页码中直接核到**。【转述,待核】
2. **Hunt 2018 的 BDI 23→14.5**:来自二手摘要,系限用组内高基线子组的前后对比(within-group),不是对照组间效应;引用时勿当组间效应量。【转述,待核】
3. **Tromholt 的 0.37**:是 1-10 量表上的原始分差,不是 Cohen's d,也不是 SD;与 Allcott 2025 里"青年情绪恶化 0.37 SD"数字巧合相同,极易误接。
4. **Castelo 2025 "效应大于抗抑郁药"**:within-subject dz 与药物 RCT 组间 d 不可直接比;基准取的又是 Kirsch 2008(本身争议极大);且合规达标仅 25.5%、样本自选"想减少用机的人"、期待效应未排除。引用此对比需整段带上限定。
5. **Instagram 停用 0.041 SD**:单独 p=0.016,多重校正后 p=0.14,未过预注册门槛;"Instagram 停用改善幸福感"这一说法在传播中常丢掉此限定。而"IG 效应由 25 岁以下女性驱动"又是**非预注册探索性分析**——正反双方都容易选择性引用同一篇。
6. **两篇 Ferguson meta 极易混引**:*Professional Psychology* 2024(46 项,**相关性**研究、青少年)与 *Psychology of Popular Media* 2024(27 项,**实验**、混合年龄)结论相似但证据类型完全不同;后者被 Rausch & Haidt 指出效应量/样本量誊录错误(该批评来自对立阵营,亦需带立场标注)。
7. **meta 之间"矛盾"部分是结局口径差异**:May 2025(抑郁症状,g=0.25 显著)vs Lemahieu 2025(积极/消极情感与生活满意度,≈0)可以同时为真;比较时必须对齐结局与干预类型(限用 vs 戒断:May 内部 g=0.33 vs 0.15)。
8. **构念梯度**:smartphone ownership ≠ mobile internet(Castelo)≠ social media(Allcott/Lambert)≠ 单平台(FB/IG 停用)≠ screen time(几乎没有因果研究直接操纵"屏幕时间")。Haidt 的书级论断跨这几层构念,引用任何单项研究时要标明它实际操纵的是哪一层。
9. **年龄错位**:最强 RCT 证据(Allcott 2020/2025、Castelo、Lambert、Tromholt)都是**成人**样本;Allcott 2025 的 FB 效应甚至由 35 岁以上驱动。直接针对青少年的因果证据主要来自自然实验(Braghieri=大学生;西班牙/意大利=青少年住院)而非 RCT。
10. **结局测量梯度**:自报症状(NCHA、PHQ、WEMWBS)vs 临床/住院记录(Donati、Arenas-Arroyo)。怀疑派对自报的批评不适用于意/西住院研究——这两项是"负效应"一侧目前最硬的口径。
11. **Braghieri 外推 2004-06 → 现在**:当年 Facebook 无 News Feed、无算法流;Allcott 2025 作者原话提醒"the effects could be quite different two decades later"——正方引用时常略去。
12. **Braghieri 无已发表正式批评**:本次检索未找到 AER comment 或复现挑战;这是检索状态陈述,不能写成"无可争议"。
13. **停用实验的时间替代**:Allcott 2025 的 app 计量显示停用释放时间大都流向其他手机 app——"戒断组去过线下生活所以变好"的常见机制叙事与该数据不符,引用机制时注意。
14. **Facebook Files "1 in 3"**:分母是"已有身体形象困扰的女孩";且为自我感知调查、非因果;Meta 注释版 slide 有公司立场,WSJ 摘引亦有选择性——两边口径都要标。
