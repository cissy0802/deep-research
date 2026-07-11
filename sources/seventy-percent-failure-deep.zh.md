# 「70% 转型失败」考古:上一轮转型的尸检报告,能预测 AI-native 吗?(深入版)

> 本文的实证引用经过分级:正文引用的 30 组承重论断(数字的引用链原文、失败率一手测量、Agile/DevOps 档案、变革理论证据、AI 采纳数据)各经 3 名独立验证者对抗核查(逐字核对一手原文、检索反证、口径审查),30 组全部挺过反驳、其中 20 组按验证者意见完成 40 余处口径修正;未进入验证流程的引用标【未验证,来源】。方法学限定(自报口径/厂商利益/预测 vs 实测)在正文中如实交代,文末附来源索引。

## 0. 为什么给一个数字做考古

打开任何一份 AI 转型方案的开场白,大概率会撞见同一个句式:"研究表明,70% 的转型会失败——但我们知道怎么让你成为那 30%。"这个数字给整个变革咨询行业当了三十年招牌,现在正原封不动地搬进 AI 时代:2024-2026 年,《Why 70% of AI Transformations Fail》《The 70% Rule for AI Change Management》这类厂商文章批量出现,句式与三十年前逐字同构——先吓你,再卖你解药。【未验证,来源:novoslo.com、aiassemblylines.com 等】

本站[《当代码变得便宜》](https://cissy0802.github.io/deep-research/ai-native-deep.html)论证了 AI-native 转型的困难主要在组织而不在技术。顺着这条线索,自然的下一问是:上一轮席卷软件业的大转型——敏捷与 DevOps——留下了完整的档案,这批档案对这一轮有多少预测力?而检查档案的第一步,是检查档案封面上那个最响亮的数字。

这篇文章做三件事:**给"70%"验尸**(它从哪来、怎么变异、为什么杀不死);**问测量要一个诚实的基率**(真实的转型失败率到底是多少——剧透:这个问题本身有问题);**评估上一轮尸检报告对 AI-native 的预测力**(哪些失败机制在原样重演,哪些结构性条件已经变了)。

## 1. 数字的一生:1993-2026

"70%"有精确的出生记录,而且出生证明上写着"非科学"。

**1993 年,出生。**Hammer 与 Champy 的《Reengineering the Corporation》(再造企业)写道:"Our unscientific estimate is that as many as 50 to 70 percent of the organizations that undertake a reengineering effort do not achieve the dramatic results they intended."(我们的非科学估计是,多达 50%-70% 进行流程再造的组织,没有达到它们预期的戏剧性成果。)【已验证;不同版本"50 to 70 percent"与"50 percent to 70 percent"拼写略异】注意三个限定:**估计是"非科学的"**;范围只是**流程再造**这一种变革;"失败"的定义是**没达到预期的戏剧性成果**——不是搞砸,是没够到自己喊出的高目标。

**1995 年,作者收回。**Hammer 在《The Reengineering Revolution》里亲自纠偏:"……this simple descriptive observation has been widely misrepresented and transmogrified and distorted into a normative statement. There is no inherent success or failure rate for reengineering."(这个简单的描述性观察,被广泛地误传、扭曲成了一个规范性论断。流程再造并不存在什么固有的成功率或失败率。)【已验证】这段收回几乎从不被引用——数字活了下来,免责声明死了。

**1995 年,被冤枉的"源头"。**日后被无数引用指认为 70% 出处的,是 Kotter 同年在《哈佛商业评论》的名文《Leading Change: Why Transformation Efforts Fail》。可原文里**没有任何整体失败率数字**,更没有 70%。Kotter 看了 100 多家公司,给出的是印象式判断:"A few of these corporate change efforts have been very successful. A few have been utter failures. Most fall somewhere in between, with a distinct tilt toward the lower end of the scale."(少数非常成功,少数彻底失败,大多数介于两者之间——明显偏向下端。)全文唯一一个与失败沾边的百分比是分阶段的:他观察的公司里"远超过 50%"倒在第一步(建立紧迫感)。【已验证】

**2000 年,关键变异。**Beer 与 Nohria 在《哈佛商业评论》写下:"The brutal fact is that about 70% of all change initiatives fail."(残酷的事实是,约 70% 的变革计划都会失败。)没有脚注,没有研究,没有出处。【已验证】一句"非科学估计"在这里完成了两次脱落:**范围脱落**(流程再造 → 一切变革)、**免责声明脱落**(unscientific estimate → brutal fact)。

**2008 年,Kotter 终于亲口说出 70%。**在《A Sense of Urgency》里:"From years of study, I estimate that today more than 70% of needed change either fails to be launched, even though some people clearly see the need, fails to be completed, even though some people exhaust themselves trying, or finishes over budget, late, and with initial aspirations unmet."(基于多年研究,我估计如今超过 70% 的必要变革,或者根本没能启动,或者没能完成,或者超预算、延期、未达最初期望。)【已验证】依然是个人估计、依然无研究引用——且口径宽到把"该变而没变"也计入失败。

**2008-2009 年,第三次变异:出处被发明出来。**McKinsey 的 Keller 与 Aiken 在《The Inconvenient Truth About Change Management》里写道:"In 1995, John Kotter published research that revealed only 30 percent of change programs are successful."(1995 年,John Kotter 发表的研究揭示,只有 30% 的变革项目是成功的。)【已验证】如前所述,Kotter 1995 年的文章里**不存在这个数字**,也不存在任何整体百分比——"published research that revealed"是无中生有的学术包装。同期的实证遮羞布是 McKinsey 自己 2008 年 7 月的全球调查:3,199 名高管自评本组织的转型,其中经历过转型的约 2,663 人打分,"只有约三分之一说自己的组织成功实现了目标"。同一份数据里,明确评为"完全不成功"的只有约 5%-6%——**"三分之二没说成功"被卖成了"70% 失败"**。【已验证】

**2011 年,学术验尸。**Hughes 在《Journal of Change Management》发表《Do 70 per cent of all organizational change initiatives really fail?》,逐条追溯五个已发表的 70% 论断——Hammer & Champy 1993、Beer & Nohria 2000、Kotter 2008、Bain 的 Senturia 等 2008、McKinsey 的 Keller & Aiken 2009——结论原文:"whilst the existence of a popular narrative of 70 percent organizational change failure is acknowledged, there is no valid and reliable empirical evidence to support such a narrative."(70% 变革失败的流行叙事确实存在,但**没有任何有效可靠的实证证据支持它**。)【已验证】

**2011 年之后,僵尸期。**被验尸不影响流通:McKinsey 2015 年《Changing Change Management》继续不带出处地写"70 percent of change programs fail to achieve their goals"【已验证】;2021 年《Losing from day one》干脆在脚注里引 Kotter(《Leading Change》1996 与《A Sense of Urgency》2008)为 70% 背书【已验证】——**咨询公司引用大师,而大师这个数字的"研究出处"正是这家咨询公司当年发明的**。引用链闭环了。BCG 则在 2020 年为数字化转型重启了这个数字(70% fall short,下文细拆)。然后是 2024-2026 年的 AI 版宿主。

这条传播链在医学文献计量里有现成的分类学:Greenberg 对引用网络的研究把这类机制命名为引用偏倚、放大与发明(citation bias / amplification / invention),原文的警句是"citation can be used to generate information cascades resulting in unfounded authority of claims"(引用可以制造信息级联,让论断获得无根据的权威)。【未验证,来源:BMJ 2009;339:b2680】"70%"三十年的旅程,是这三种机制的教科书标本:范围脱落是偏倚,反复转述是放大,"Kotter 1995 published research"是发明。

## 2. 那真实的失败率是多少?测量给出的诚实答案

考古只能证明"70% 没有出处",不能证明失败率不高。要回答"到底多少",得去看认真测过的人测出了什么——以及测量本身遇到了什么。

### 2.1 被引最多的"测量":Standish CHAOS 与三次拆解

软件业自己的"70%"叫 CHAOS 报告。Standish Group 1994 年的首份报告:成功 16.2%、"受挑战"52.7%、受损/取消 31.1%(365 名受访者,覆盖 8,380 个应用项目)。【已验证】注意定义:"成功"= **按时、按预算、交付全部预定功能**——三条全中才算赢。这份报告喂养了此后三十年"软件项目大多失败"的叙事,但它经受的三次独立拆解值得逐一记录:

- **Jørgensen 与 Moløkken(2006)**指出:Standish 报告的 189% 平均成本超支,是三份更早的同行评审调查(Jenkins 1984、Phan 1988、Bergeron 1992)所测 33-34% 的约 5-6 倍——作者同时说明两边口径不完全可比(Standish 只统计"受挑战"项目),但差距大到口径解释不了;并直言"可能存在严重的调查设计与分析方法问题,例如抽样可能强烈偏向'失败项目'",而 Standish 从不公开方法。【已验证】
- **Eveleens 与 Verhoef(2010,IEEE Software)**做了最彻底的一击:他们把 Standish 的定义套到 1,211 个真实项目的 5,457 次预算预测上,发现 CHAOS 数字是**预测偏差的伪像**——一个无偏差、业内一流的组织按 Standish 定义只能拿到约 35% 的"成功率"(成本与功能双达标口径);他们构造了一个镜像组织(偏差幅度相同、方向相反的反事实),其 Standish"成功率"从 5.8% 翻到 94.2%。判词原文:Standish 的成功/受挑战定义有四大问题——"misleading, one-sided, pervert the estimation practice, and result in meaningless figures"(误导、片面、扭曲估算实践、产出无意义的数字)。被当面质询时,Standish 主席 Jim Johnson 的回答值得裱起来:"All data and information in the Chaos reports and all Standish reports should be considered Standish opinion and the reader bears all risk in the use of this opinion."(CHAOS 报告与所有 Standish 报告中的一切数据与信息,应被视为 Standish 的**观点**,读者使用该观点风险自负。)【已验证】
- **Standish 自己的数字自己打架。**其成功率 1994-2009 年间在 16-35% 波动、失败率在 18-40% 非单调起伏;2015 年报告里,同一批项目按传统三约束定义算出 36-41% 成功、按新的"按时按预算且结果令人满意"定义只剩 27-31%——**换个定义,同一批项目的成绩单浮动 10 个百分点**。【已验证】顺带说明:即便按 Standish 最严的口径,"彻底失败"(取消)也从未到过 70%;2020 年报告约为成功 31%/受挑战 50%/失败 19%。【已验证】

### 2.2 认真测量的人测到了什么:肥尾,而不是"大多数失败"

Flyvbjerg 团队的项目数据库是这个领域样本最大的测量:

- **1,471 个 IT 项目**(2011,HBR):平均成本超支只有 27%——但**六分之一**的项目是"黑天鹅",平均超支约 200%、工期平均超 70%。【已验证】
- **约 16,000 个项目的数据库**(2023,《How Big Things Get Done》):47.9% 的项目达到或优于预算;预算与工期双达标的只有 8.5%;预算、工期、收益三达标的只有 **0.5%**。IT 项目平均超支 +73%(实际价格,以决策基线计);而超支超过 50% 的那 18% 的 IT 项目,平均超支达 **+447%**。【已验证;基线取"决策建设时点"这一口径有学术争议——Love & Ahiaga-Dagbui 与 Ika 认为它相对合同基线夸大了超支【未验证,来源:相关评论文献】】

这两组数字并排看,教训不是"大多数项目失败",而是**分布是肥尾的**:典型项目超支可控,毁灭性的是尾部——那六分之一会吃掉不成比例的损失。注意 0.5% 这个数字的结构:它和 Standish 的 16.2% 是同一种"多杆全中才算赢"的定义装置,杆加得越多,"成功"越稀有。**用三杆全中的口径宣布"99.5% 失败"与用取消率宣布"只有 19% 失败",用的是同一批项目。**

### 2.3 组织变革的学术基率:答案是"没有答案"

跳出软件项目,组织变革整体的测量记录更薄:

- **Smith(2002)**汇编 49 项已发表研究(覆盖超过 4 万家组织),按变革类型给出**中位报告成功率**:重组/裁员约 46%、并购整合约 33%、软件系统安装约 26%、文化变革约 19%。【已验证】两个必须带上的限定:这些是**各研究自报口径的中位数**(多为从业者调查与自评),且每类底下的研究数很少(文化变革仅约 3 项)——是脆弱的中位数,不是稳定基率。
- **Cândido 与 Santos(2015)**系统梳理战略实施失败率:已发表的估计从 7% 到 90% 不等(一般企业战略类为 28-90%,计入特定战略研究后下探到 7%),均值约 50%;判词原文:"Most of the estimates presented in the literature are based on evidence that is outdated, fragmentary, fragile or just absent."(文献中的大多数估计,依据的证据要么过时、要么零碎、要么脆弱、要么干脆不存在。)【已验证】

这就是学术界的诚实答案:**真实失败率是"未定"**——不是因为没人测过,而是因为"失败"没有统一定义,而定义选择本身决定数字。

### 2.4 定义机器:咨询公司的数字是怎么造出来的

理解了定义的杠杆,再看今天流通的转型统计,机器的构造一目了然:

- **BCG 2020**:"70% 的数字化转型未达目标"(825 名高管自评 + 约 70 个 BCG 客户案例)。看它自己的三段拆分:30% 完全达标、**44% 创造了部分价值但未达目标**、26% 价值有限。【已验证】70 里有 44 个百分点是"部分成功"——被会计进"失败"。这与 1993 年"没达到预期的戏剧性成果"是同一个手法。
- **Bain 2024**:"88% of business transformations fail to achieve their original ambitions"(88% 的企业转型未达最初雄心;400 多名高管)。同一研究的配套文章里写着:如果把失败定义为"达成不到一半目标",只有约 13% 够格。【已验证】**同一批数据,既可以是"88% 失败",也可以是"约 87% 至少完成了一半"**——全看你把"雄心"还是"腰斩"设为及格线。
- 更早的经典还有单位错位:KPMG 新西兰 2010 年调查的"70% 的组织在过去 12 个月里至少有一个项目失败",流通成了"KPMG:70% 的项目失败"。【未验证,来源:Calleam 汇编】

自报口径还有一层系统性问题:打分的高管既是转型的责任人又是评委,且咨询公司的调查问卷天然以"是否达到最初目标"为标尺——而最初目标是销售阶段定的。**卖转型服务的机构,同时垄断了"转型是否成功"的计分权。**这不需要阴谋论,只需要注意每份此类报告的最后一章都是服务介绍。

## 3. Agile 档案:一场转型运动的自我记录

敏捷是软件业上一场全行业转型,它留下的档案有独特的价值:**长达十七年的同题问卷**,和一个从未兑现的测量承诺。

### 3.1 十七年问卷:同一批挑战年年榜首

State of Agile 调查(VersionOne → CollabNet → Digital.ai)是敏捷运动的自我镜像——厂商主办、受访者自选样本,这两条先记在案。它测出的东西恰恰因此有趣:

- **挑战榜十年不换人。**第 14 期(2019,1,121 名受访者)的前五名:组织对变革的普遍抵触 48%、领导层参与不足 46%、跨团队流程实践不一致 45%、组织文化与敏捷价值观冲突 44%、管理层支持与赞助不足 43%——五项里四项是文化-领导力集群(第 15 期的单项榜首是流程不一致,文化项居 2-3 位)。到第 17 期(2023),榜首依然是"对变革的普遍抵触/文化冲突"(47%,作为业务侧采纳敏捷的最大障碍)。【已验证】**一场以文化变革为卖点的运动,自己的问卷连续十几年把"文化没变"报为最大障碍。**
- **满意度崩塌与退潮。**第 17 期:对本组织敏捷实践的满意度从上年的 71% 跌到 59%。第 18 期(2025 年 7-8 月调查,样本只剩 349 人——样本本身就是退潮信号):74% 使用混合/自创方法(第 16 期约 50%,提问口径不完全相同);只有 13% 说敏捷在组织中深度扎根;42% 的评价是"聊胜于无"(better than nothing);24% 削减了敏捷投入。【已验证】
- **它的正面数字不可用。**第 15 期宣称软件团队敏捷采用率一年内从 37% 跳到 86%——自选样本换了一批人,就能造出这种"增长"。【已验证】同一份问卷,负面信号(满意度、挑战榜)比正面信号(采用率)可信,因为厂商没有动机夸大前者。

学术侧的系统综述与之互证:Dikert、Paasivaara 与 Lassenius(2016)梳理 52 篇大规模敏捷转型文献(42 个案例),发现**将近 90% 是经验报告而非严谨研究**;单项最高频挑战是"其他职能不愿改变"(约 31% 的案例);作者的结论是(原话):"large-scale agile cannot be just taken into use off-the-shelf"(大规模敏捷不能拿来即用,必须仔细定制)。【已验证】

### 3.2 该诚实记录的反证:敏捷实践本身可能有效

给敏捷验尸,不等于说敏捷无效。Jørgensen(IEEE Software 2019)对 196 个挪威软件项目的分析:使用敏捷方法的项目在所有规模档上结果都好于非敏捷(小型项目 p<0.01、中型 p≈0.03,大型不显著;成功为自评口径、设计为相关性)。【已验证】这与前述档案并不矛盾,反而拼出这场运动最重要的一课:**实践与转型是两回事**——迭代交付、持续集成这些实践与更好的结果相关;而"敏捷转型"这个组织仪式批发的是实践的名字,不是实践本身。

### 3.3 规模化框架:一个几乎零证据的产业

如果说敏捷实践有证据、敏捷转型证据稀薄,那么"规模化敏捷框架"是证据真空:

- **SAFe 的证据全部自产。**Scaled Agile 官网:"Seventy percent of Fortune 100 companies... have certified SAFe professionals"(财富 100 强中 70% 拥有 SAFe 认证人员)——注意口径,是**有认证员工**,不是在用框架;外加自报的"20,000+ 企业"与"上市速度快 30-75%"。Putta 等的多源综述(XP 2018)发现 SAFe 证据基础绝大多数是灰色文献、大量发布在 Scaled Agile 自家网站上,商业收益只出现在厂商案例里。**2016-2025 年间,我们与验证者均未找到任何一项独立的受控结果研究**——这个空白本身就是发现。【已验证】
- **最大的独立比较研究测到的是"无实际差异"。**Verwijs 与 Russo(EMSE 2024;约 15,000 名敏捷团队成员、4,013 个团队,外加 1,841 名利益相关者)比较各规模化路线(SAFe、LeSS、Scrum of Scrums、自创、不规模化):统计上有显著差异,但效应量小到无实际意义——论文自己的措辞是框架选择"does not markedly influence"团队效能;对效能最强的预测变量是团队的敏捷经验,不是用哪个框架。【已验证;效能为自报口径】这一枪同时打穿两边:厂商的"快 30-75%"与批评者的"SAFe 独害论"。
- **采购方的用脚投票。**美国空军首席软件官 Chaillan 2019 年 12 月的备忘录白纸黑字:"Programs are highly discouraged from using rigid, prescriptive frameworks such as the Scaled Agile Framework (SAFe)"(强烈不建议项目使用僵化、规定性的框架,例如 SAFe)。【已验证;注意美空军 2020 年又与 Scaled Agile 有过合作接触,此文件不是长期禁令【未验证,来源:后续报道】】

### 3.4 两个标本:被模仿的虚构,与退潮的具名案例

- **Spotify 模型是其作者自认的愿景稿。**前 Spotify 敏捷教练 Joakim Sundén:"Even at the time we wrote it, we weren't doing it. It was part ambition, part approximation."(写它的时候我们自己都没在这么做,一半是愿景一半是近似。)合著者 Ivarsson:"It worries me when people look at what we do and think it's a framework they can just copy and implement."Kniberg:"它根本不是通用框架,只是一家公司工作方式的例子。"【已验证】全行业照抄的组织图,在原产地是一份没实施过的理想稿——这为第 5 节的模仿性同构提供了一个纯度罕见的标本。
- **Capital One,2023 年 1 月:裁撤约 1,100 个敏捷职位**(敏捷教练、交付主管、组合主管),发言人原话:"The agile role in our tech organization was critical to our earlier transformation phases but as our organization matured, the natural next step is to integrate agile delivery processes directly into our core engineering practices."(敏捷角色在早期转型阶段至关重要,但随着组织成熟,自然的下一步是把敏捷交付流程直接并入核心工程实践。)【已验证】同一句话有两种读法——"敏捷毕业了"或"敏捷层被裁了"——两种读法都与档案一致;确定的是**专职敏捷阶层在退场**,从业者侧的培训报名与岗位数据同方向【未验证,来源:Age of Product、BirJob 汇编】。

## 4. DevOps 档案:测得最认真的一波,和它的天花板

DevOps 一代比敏捷一代在证据上前进了一大步,也正因此,它的档案暴露了这类测量的上限在哪。

**进步是真的。**DORA/State of DevOps 测的是**结果指标**(部署频率、变更前置时间、变更失败率、恢复时间),不是满意度;四键指标可以从系统数据直接测(Google 开源了 Four Keys 工具),别人可以用自己的数据复算。这比"你觉得你们敏捷吗"是范式升级。

**但它的纵向叙事撑不住自己的方法。**2022 年报告里,"精英"绩效集群整个消失了——官方原文:"Unlike in years past, there was no evidence of an 'Elite' cluster."低绩效组从 2021 年的 7% 跳到 19%,DORA 给出的解释是一个未检验的疫情假说。把历年精英占比连成线(2018 年 7% → 2019 年 20% → 2021 年 26% → 2022 年消失 → 2023-24 年约 18-19%),这条"行业在进步"的曲线其实不可比:DORA 自己的 FAQ 承认,集群每年从**当年的不同受访者**中重新涌现,不是校准过的行业指数。加上自报问卷、可能的自选偏差(自认精英的人更愿意答卷,The Register 2021 年就点过名)、原始数据不公开、能力→绩效路径模型无独立复现——**这一波测量最认真,也只能认真到这里**。【已验证】

**预测被当成了测量。**广为流传的"75% 的 DevOps 计划将因组织学习与变革问题达不到预期"(Gartner,2019,预测期到 2022;另有 90% 版本到 2023)是分析师**预测**,从未被回头验证过。【未验证,来源:Gartner 2019 及其社交媒体贴】它照样进了无数张胶片当"研究表明"。

**具名的大案:GE Digital。**转型叙事经济里最响的案例给出了最硬的收尾数字:GE 2015 年宣布目标"2020 年软件与解决方案收入超过 150 亿美元"(当时约 50 亿);据报道 2016 年一年就向 GE Digital 投入超 40 亿美元(第三方估计,GE 未正式披露该口径);2018 年 12 月,GE 宣布把数字业务改组为**独立运营但仍全资持有**的公司,当时年软件收入约 12 亿美元——目标的 8%——并把 2016 年花 9.15 亿美元买的 ServiceMax 多数股权卖给了 Silver Lake(这次拆分后来也没走完,GE Digital 最终并入 GE Vernova)。【已验证;注意 GE 2018 年那笔 220 亿美元商誉减记属于 GE Power,与 Digital 无关,常被混引】同期,GE 系的转型故事还在行业峰会上作为成功案例巡讲【未验证,来源:DOES 议程存档】。

**幸存者经济。**DevOps 的案例库结构性偏成功:企业峰会讲台由自荐的成功故事组成,运动的奠基文本(《凤凰项目》)本身是小说;没有失败者分会场。【未验证,来源:DOES 2016 新闻稿、IT Revolution 案例库】这不是谁作弊,是这类档案的生成机制——记住它,第 7 节读 AI 案例集时原样适用。

**这一波档案里已经有 AI 的第一行记录。**DORA 2024:AI 采用度每升 25%,交付吞吐量估计降 1.5%、交付稳定性估计降 7.2%;2025 年报告吞吐量转正、稳定性依旧为负,官方定调改为放大器:"AI doesn't fix a team; it amplifies what's already there."(AI 不会修好一个团队,它放大团队本来的样子。)【已验证,口径沿用[《当代码变得便宜》](https://cissy0802.github.io/deep-research/ai-native-deep.html)】上一波转型建起来的测量基础设施,已经开始给下一波转型出成绩单——这是两波档案之间最有价值的连续性。

## 5. 卖药的人:变革管理学自己的证据体检

"70% 会失败"是恐吓,"照我们的框架做就能成功"是解药。恐吓部分已经验完尸,现在验解药。

- **Kotter 的八步法:从未被整体检验。**Appelbaum 等(2012)在模型问世 15 年后做了第一次系统对账:多数单步能找到零散支持,但**没有任何正式研究检验过整个模型**;模型建立在 Kotter 的个人商业与研究经验之上、未引用外部研究;结论原文:"Kotter's change management model appears to derive its popularity more from its direct and usable format than from any scientific consensus on the results."(其流行更多来自直接好用的格式,而非任何关于效果的科学共识。)【已验证】此后至今,我们与验证者也未找到对八步法整体的受控检验;主要的实证应用(Pollack & Pollack 2015)反而发现实践中各步骤并行、回绕,对不上线性叙事【未验证,来源:Systemic Practice and Action Research 28】。Kotter 2014 年的回应(《Accelerate》,双操作系统)把八步改成八个并发"加速器"——承认了线性批评,依然没带新证据,且 Kotter Inc. 以此为产品。【未验证,来源:HBS Press】
- **Lewin 的"解冻-变革-再冻结":死后被造出来的模型。**Cummings、Bridgman 与 Brown(2016,Human Relations)对照 Lewin 原著与后世教材,论点原文:"we argue that he never developed such a model and it took form after his death"(我们论证他从未发展过这样一个模型,它是在他 1947 年去世后才成形的)——由 Lippitt、Schein 与教科书逐层构造。【已验证】需要如实交代:这是有对手方的论点,Burnes(2020)撰文反驳,认为三步说深植于 Lewin 的场论、并非简化伪造【已验证(反方存在性)】。对本文论证而言,两边打平也足够:**变革管理教科书的第一课,其出处本身是学术争议现场,而不是被验证的方法**。
- **系统的证据对账只有一份,结论谦逊。**Stouten、Rousseau 与 De Cremer(2018,Academy of Management Annals)把七个流行模型(Lewin、Beer、Judson、Kanter/Stein/Jick、Kotter、ADKAR、欣赏式探询)与学术证据逐条对表:这些模型的根基更多是专家意见而非科学证据;个别招牌处方(如"先制造紧迫感"而不诊断)缺乏支持,另一些(愿景、沟通、参与)与证据部分吻合;作者最后自己蒸馏了一套约十步的循证清单。【已验证】
- **为什么没证据也卖得动:合法性,不是效果。**DiMaggio 与 Powell(1983)的模仿性同构给出理论机制:"When organizational technologies are poorly understood, when goals are ambiguous, or when the environment creates symbolic uncertainty, organizations may model themselves on other organizations."(当组织技术不被充分理解、目标含混、环境制造符号不确定性时,组织会模仿其他组织。)以及:"The ubiquity of certain kinds of structural arrangements can more likely be credited to the universality of mimetic processes than to any concrete evidence that the adopted models enhance efficiency."(某类结构安排的无处不在,更应归功于模仿过程的普遍性,而非任何"这些模式提升效率"的具体证据。)【已验证】实证跟上了理论:Staw 与 Epstein(2000)对百家最大美国企业的检验——与流行管理技术(TQM 等)沾边**不带来任何经济绩效提升,但带来更高的声望评价和更高的 CEO 薪酬**;Westphal、Gulati 与 Shortell(1997,2,700 余家医院)——早期采用者为效率定制 TQM,晚期采用者为合法性照抄标准形态,而照抄程度与效率收益负相关。【已验证】(如实补一句边界:后续研究显示认真实施者确有回报——质量奖得主财务表现更好,同构的元分析平均效应也不为负【未验证,来源:Hendricks & Singhal 1997/2001、Heugens & Lander 2009】。被判死的不是实践,是**为了像同行而采用的仪式**。)
- **管理时尚有测得出的生命周期。**Abrahamson 的管理时尚理论及其与 Fairchild 的实证:质量圈等风潮的文献量呈钟形暴起暴落,上升期话语"情绪化、狂热、不讲条件",下降期才恢复冷静限定——他们称之为"迷信式集体学习"。【未验证,来源:AMR 1996、ASQ 1999】把这条曲线记住:第 7 节会用它对照 AI。

这一节的合订结论:**变革工业的恐吓数字没有实证出处,解药框架没有整体检验,而购买行为由合法性驱动**——三十年卖了个寂寞?不。卖出去的东西真实发生了作用,只是作用机制是 Staw-Epstein 式的:采纳者获得合法性、声望与薪酬,咨询方获得收入。唯一没被证明的,是它对"70%"那个分母的作用。

## 6. 「中层冻土」再审:谁真的杀死转型

每个转型故事都有一个官方反派:中层经理——"上面想变,下面想变,中间冻住了"。这个"冻土层"(frozen middle)值得单独过堂,因为它正被原句搬进 AI 叙事。

**出身先存疑。**这个说法通常被归给 1980 年代通用汽车 CEO Roger Smith,但可查证的只有咨询博客互相转引(连 Dartmouth Tuck 的案例页也这么写)——**没有任何 1980 年代的一手出处**(演讲、访谈、当时报道)可以定位。【已验证(缺失性)】一个用来解释转型失败的概念,自己的出处就是转述链——与"70%"是同一种生物。

**学术档案给中层翻案,但翻得有条件。**Wooldridge 与 Floyd(1990,20 家组织的定量研究):中层参与战略制定与组织绩效正相关。Huy(2002,三年田野,ASQ):激进变革中,中层经理的"情绪平衡"工作(一边推动项目、一边接住下属的情绪)是适应得以发生的机制。Balogun 与 Johnson(2004,AMJ):变革走样的主因是高层撤出后中层在**沟通真空**里各自意会(sensemaking),不是蓄意抵抗。反面钉子也是学术的:Guth 与 MacMillan(1986)证实,当中层认定变革损害自身利益时,能把战略拖慢、降级乃至"totally sabotage"(彻底破坏)。【已验证】合起来:**中层是条件反应器,不是冻土**——条件是激励对齐、信任与参与,而这三个旋钮都在高层手里。

**从业者最大的数据集把矛头指向楼上。**Prosci 自 1998 年起的两年一度调查(厂商自报、从业者样本,这两条记在案):"积极且可见的高管赞助"连续每期都是变革成功的第一贡献因子,提及率约为第二名的三倍;"与中层经理的互动"在七项里排**第七**;赞助极其有效时,项目达标概率约为极其无效时的 3.5 倍(该倍数为本期口径,其他版次为 2.5-2.9 倍)。同一份材料也如实写着中层是其调查里抵抗最强的群体——与"条件反应器"读法一致:抵抗是测得到的,但它是因变量。【已验证】另一条同向证据来自反面:MIT Sloan 的 Johnson 总结变革研究的取样偏差——多数研究只覆盖头几个月、只访谈领导层,"变革失败怪懒经理"的证据本身是这么生产出来的。【未验证,来源:strategy+business 2020】

**连"参与"这块金字招牌都是有条件的。**变革管理的创世实验——Coch 与 French(1948,Harwood 睡衣厂)——被教科书讲成"参与消除抵抗":无参与组产量从约 60 件/时跌到约 50(约 17-20%),32 天无起色;全参与组回升并超出变革前约 14%。但原始实验的对照组只有 18 人、实验组 13/8/7 人,头 40 天对照组 17% 的人离职;Bartlem 与 Locke(1981)指出解释、培训、工作可得性、计件价公平性全是混杂变量;挪威复制实验(French、Israel 与 Ås,1960)没测到产量效应。【已验证】参与→承诺是个**条件启发式**,不是定律——这对下文的 AI 强制令 vs 自下而上之争是直接的校准。

**冻土叙事在 AI 时代的新工作,以及数据怎么说。**2025-2026 年的"AI 冻土层"文章批量出现,但它们引用的报告常常说着相反的话:McKinsey《Superagency》(2025)的结论是员工已准备好、**领导层才是最大瓶颈**;Kyndryl 2025 年调查的"45% 的 CEO 认为员工抵触 AI"是 CEO 对全体员工的**感知**,被博客改装成了"中层阻挡 AI"。【未验证,来源:各原报告与转引文】而直接测使用率的数据给出的梯度方向干脆是反的——领导 > 中层 > 一线(Gallup 2025 年四季度:每周多次使用 AI 者,领导约 44%、经理约 30%、一线约 23%)。【已验证】中层不是 AI 的冻土;如果有冻土,它在别处(见下节)。

**变革疲劳是真实的,数字是乱的。**员工侧的档案:2022 年平均每人经历 10 项计划内企业变革,2016 年只有 2 项(HBR 2023,Gartner 作者)。【已验证】"支持变革的意愿从 2016 年 74% 跌到 2022 年 __%"这道填空题,Gartner 自家出版物给过两个答案:43%(2022 年 10 月发布材料)与 38%(2023 年一季度刊物)——本文最初把 43% 判为流传错误,验证者纠正:**分歧存在于 Gartner 内部**,另有一对巧合同数的"留任意愿 43%/74%"统计与之并存。【已验证】一个关于"变革让人疲劳"的统计,自己都疲劳出了两个版本——这句不是俏皮话,是本文方法论的免费教具。

## 7. 预测力评估:这套尸检对 AI-native 说了什么

现在合卷作答标题问题。把前六节的失败机制列成清单,对着 2024-2026 年的 AI 采纳记录逐项打勾,得到的是一张**大部分打勾、三处断裂**的表。

### 7.1 机制在原样重演

- **模仿性采纳,这次有实测数字。**IBM/牛津经济研究院对 2,000 名 CEO 的调查(2025):64% 承认"落后的风险驱使我们在弄清价值之前就投资某些技术";CEO 自报只有约 25% 的 AI 计划达到了预期 ROI。【已验证】这就是 DiMaggio-Powell 的 1983 年语句在当代的问卷回声——"目标含混 + 符号不确定性 → 模仿"。配套的合法性剧场也齐了:标普 500 财报电话会提及 AI 的次数连创十年新高【未验证,来源:FactSet】,董事会压力调查密集出现【未验证,来源:Dataiku/Harris、BCG 新闻稿】。
- **强制令与指标,Goodhart 剧本已首演完毕。**Shopify(2025 年 4 月,Lütke 备忘录):"Reflexive AI usage is now a baseline expectation"(反射性使用 AI 已是基线期望),AI 使用进绩效与同侪评审,并要求"Before asking for more headcount and resources, teams must demonstrate why they cannot get what they want done using AI"(申请增员前须先证明 AI 干不了这活)。微软开发部门(2025 年 6 月,Liuson 内部信,经 Business Insider 报道):AI 使用"不再是可选项"、纳入绩效反思。Meta(2025 年 11 月宣布):2026 年起"AI 驱动的影响"成为全员绩效核心预期。Coinbase 的 Armstrong 按他自己的说法,解雇了限期内无正当理由不上手 AI 编码工具的工程师。而 Duolingo 用约 12 个月跑完了整个周期:2025 年 4 月"AI-first"备忘录、AI 使用进绩效 → 数周内公开软化 → 2026 年 4 月,von Ahn 确认绩效中的 AI 使用要求已撤销,原话(Silicon Valley Girl 播客,经 Fortune 报道):"At the end, we backtracked... the most important thing in your performance is that you are doing whatever your job is as well as possible."【已验证】**一家公司已经从"考核 AI 使用量"退到"考核工作本身"的同一年,另一家把前者制度化**——第 3 节的仪式采纳与第 6 节的强制-参与教训,在同一个新闻周期里同时上演。工程师刷 token 仪表盘、点接受再重写的应对手法,从业者已有具体记述【未验证,来源:Patrick God 2026 等】。
- **仪式采纳与实质改造的比例,已经测出来了。**McKinsey 2025 年 3 月的调查:用上生成式 AI 的组织里,只有 **21%** 从根本上重设计过哪怕部分工作流——而在其测试的 25 个属性里,工作流重设计对 EBIT 影响的相关性最大(自报口径、相关性设计)。【已验证】79% 的"已采纳"是把新工具垫在旧流程下面——这正是 Westphal 式的仪式采纳,而 DORA 2024-2025 的"放大器"读数(吞吐转正、稳定性持续为负)与之互为注脚。
- **卖药层已经重组完毕,规模空前。**Accenture 的 GenAI 新签约:FY2024 30 亿美元、FY2025 59 亿美元(SEC 文件)。BCG:AI 相关业务约占 2024 年创纪录的 135 亿美元收入的 20%。McKinsey 领导层(经 WSJ 等报道):AI 相关工作约占全公司业务的 40%,由约千人规模的 QuantumBlack 牵头。认证工业同步复刻 SAFe 曲线:AI 认证已占专业档案上所列认证的近 30%,是 ChatGPT 前的约 20 倍(Revelio Labs)。【已验证】外加 Chief AI Officer 岗位的爆发与"AI 卓越中心"作为标准商品回归【未验证,来源:IEEE-USA、各咨询官网】。同一批公司、同一个产品形态(转型计划 + 认证 + CoE),换了名词。

### 7.2 三处断裂:这一轮不一样的地方

- **采纳方向倒转:从"仪式下压"到"影子上涌"。**敏捷的典型病是高层买了仪式、一线照做给人看。AI 的第一批大样本数据画出的是反向图:75% 的知识工作者已在工作中使用 AI,其中 **78% 自带工具**(BYOAI;微软/LinkedIn 2024,31 国 31,000 人);57% 的在职 AI 使用者承认有过不透明使用——包括把 AI 产出当自己的交出、或回避说明用了 AI(KPMG × 墨尔本大学 2025,47 国 48,000+ 人,两类行为的合并口径)。【已验证】敏捷时代员工**表演使用**,AI 时代员工**隐瞒使用**——组织病是同一种(仪式与实质脱节),但症状反相。这直接改变处方:敏捷转型要解决"怎么让人真用",AI 转型要解决"怎么让已经在用的人敢说、以及用得对"。
- **被采纳物在改进,而且是测得出的指数级。**敏捷仪式二十年没变过;被强制的 AI 工具的能力在按测量曲线爬升——METR:前沿模型能以 50% 可靠性自主完成的任务时长,过去六年约每 7 个月翻倍。【已验证】这打破了尸检报告的一个隐含前提:上一轮里"转型失败"基本等于"组织失败",因为方法本身是常量;这一轮,组织搞砸了转型、技术自己长到够用,或组织做对了一切、被下一代模型改写前提,都是可能的结局。管理时尚理论预测的钟形消退曲线(第 5 节),第一次遇到一个内在能力持续上升的时尚宿主——旧曲线未必适用。
- **供给侧经济学部分改变。**敏捷的钱主要在按小时计费的转型服务与认证;AI 的工具层是按席位的 SaaS,自助拉动,厂商收入与使用挂钩而不与"转型工期"挂钩——OpenAI 2025 年中付费企业用户达 300 万【未验证,来源:CNBC】。但只能算半处断裂:上文 Accenture 的 59 亿美元说明按小时计费的转型层同样在暴涨,两层并存。

### 7.3 合卷

上一轮尸检报告对 AI-native 的预测力,可以压成三句:

1. **组织机制层面,预测力高。**模仿性采纳、定义驱动的恐吓数字、仪式对实质的替代、强制令的 Goodhart 反噬、把失败归罪中层的叙事错位——五项全部已在 AI 采纳记录中复现,且多数已有量化证据。失败的**形态**会押韵。
2. **失败率层面,预测力为零——因为那个数字从来不存在。**"70% 的 AI 转型会失败"在它被任何人测出来之前就已经在流通,这是本文考古部分的全部意义:它是修辞装置,不是测量结果。同理,请对"AI 试点 95% 失败"这类新一代候选僵尸数字预先持械(那是另一篇文章的题目)。
3. **技术动力学层面,类比断裂,方向存疑。**自下而上的影子采纳与指数改进的工具,是上一轮档案里没有的变量;它们既可能让这一轮真的不同,也可能只是把同一批组织病搬到新的病灶。分辨两者的工具恰好是上一轮留下的最好遗产:结果测量。[《当代码变得便宜》](https://cissy0802.github.io/deep-research/ai-native-deep.html)的处方在此处闭环——**用交付数据、不用体感与问卷,给自己的转型记账**;DORA 式仪表盘已经在给 AI 出成绩单了,别再让下一个三十年靠一个编出来的百分比导航。

## 8. 结语:十一个可检验主张

按证据强度排序:

1. **"70% 转型失败"没有实证出处:它 1993 年以"非科学估计"出生、被作者 1995 年收回、2000 年被改写为无出处的"残酷事实"、2008-09 年被发明出"Kotter 1995 研究"这一虚假出处。**(强:全链条逐字对照,经对抗验证)
2. **Kotter 1995 年的名文不含任何整体失败率;他本人首次给出 70% 是 2008 年、且自称估计。**(强:原文核查;唯一百分比是"第一步失败者远超 50%"的阶段性观察)
3. **Hughes 2011 的学术追溯结论成立——五个已发表实例背后"没有有效可靠的实证证据"——且该数字在被验尸后继续流通,包括 McKinsey 2015/2021 与 2024-26 年的 AI 版变体。**(强)
4. **测得到的真实基率是"未定":学术区间 7-90%、均值约 50%,证据"过时、零碎、脆弱或缺失";失败率是定义的函数,同一批数据可产出"88% 失败"与"87% 完成过半"。**(强:Cândido & Santos、BCG/Bain 自家拆分)
5. **软件项目的实测分布是肥尾而非"多数失败":平均超支 27-73%,但六分之一黑天鹅平均 +200%,超支超 50% 的 IT 项目平均 +447%。**(强:Flyvbjerg 两代数据;基线口径有学术争议)
6. **CHAOS 报告的数字是预测偏差的伪像:同一组织换个估算偏差方向,"成功率"5.8% ↔ 94.2%;Standish 主席自认其报告为"观点"。**(强:Eveleens & Verhoef 复算 + 当面质询记录)
7. **敏捷档案的自我诊断十七年不变——文化与领导力始终是自报的最大障碍——而规模化框架产业在 2016-2025 年间没有产出一项独立受控结果研究;最大的独立比较研究测得框架选择的实际差异可忽略。**(中强:厂商问卷的负面信号 + Dikert + Verwijs & Russo,均自报口径)
8. **敏捷实践本身与更好的项目结果相关(所有规模档,小中型显著)——失败的档案属于"转型仪式",不属于实践。**(中:单国样本、自评、相关性)
9. **变革工业的解药框架未经整体检验:Kotter 八步无整体受控研究,Lewin 三步模型系死后构造(此点有学术对手方),唯一的系统对账(Stouten 2018)判其根基为专家意见;而采纳行为的实证驱动是合法性与 CEO 薪酬,不是绩效。**(中强:Appelbaum/Cummings[contested by Burnes]/Stouten/Staw & Epstein)
10. **"中层冻土"出处不可考,且与实证方向相反:中层参与与绩效正相关、阻挡行为是激励错位的条件反应;从业者最大数据集把第一因子给了高管赞助(中层互动排第七);AI 使用率梯度实测为领导 44% > 经理 30% > 一线 23%,方向与冻土叙事相反。**(中:学术条件性证据 + Prosci 厂商自报 + Gallup)
11. **AI 转型正在复现上一轮的组织机制(64% 的 CEO 自认先投资后理解、仅 21% 重设计工作流、Duolingo 已跑完强制→撤销全周期、咨询/认证层以数十亿美元规模重组),同时在两处结构性偏离:影子式自下而上采纳(78% BYOAI、57% 隐瞒)与每 7 个月翻倍的工具能力。**(中强:各厂商/调查一手数字已验证,但均为快变量,截至 2026 年 7 月)

值得盯的信号:Meta 的 AI 绩效指标能否活过 2026 年(Duolingo 剧本预测它会退);McKinsey 的"21% 重设计工作流"在 2026-27 年调查里的走向(升=实质化开始,平=仪式期延长);DORA 2026 的 AI 稳定性符号;规模化敏捷框架会不会在 AI 时代出现第一项独立受控研究(基率:九年零项);以及下一个僵尸数字——"95% 的 AI 试点失败"——的引用链会不会重演本文第 1 节(我们打算届时也给它验一次尸)。三十年前,一个自称非科学的估计当上了一个行业的导航仪;这一轮的组织有当年没有的东西——自己的交付数据。**用它。**

---

## 附:主要来源

**数字考古**:Hammer & Champy, *Reengineering the Corporation* (1993) · Hammer & Stanton, *The Reengineering Revolution* (1995) · Kotter, "Leading Change: Why Transformation Efforts Fail" (HBR, 1995) · Beer & Nohria, "Cracking the Code of Change" (HBR, 2000) · Kotter, *A Sense of Urgency* (2008) · Keller & Aiken, "The Inconvenient Truth About Change Management" (McKinsey, 2009) · McKinsey Global Survey, "Creating Organizational Transformations" (2008-07) · Hughes, "Do 70 per cent of all organizational change initiatives really fail?" (J. Change Management 11(4), 2011, DOI 10.1080/14697017.2011.630506) · Ewenstein, Smith & Sologar, "Changing Change Management" (McKinsey, 2015) · McKinsey, "Losing from day one" (2021-12) · Greenberg, "How citation distortions create unfounded authority" (BMJ 2009;339:b2680) · Tourish, *Management Studies in Crisis* (CUP, 2019)

**基率测量**:Standish CHAOS Reports (1994/2015/2020) · Eveleens & Verhoef, "The Rise and Fall of the Chaos Report Figures" (IEEE Software 27(1), 2010) · Jørgensen & Moløkken, "How large are software cost overruns?" (IST 48(4), 2006) · Flyvbjerg & Budzier, "Why Your IT Project May Be Riskier Than You Think" (HBR, 2011; arXiv:1304.0265) · Flyvbjerg & Gardner, *How Big Things Get Done* (2023) · Smith, "Success rates for different types of organizational change" (Performance Improvement 41(1), 2002) · Cândido & Santos, "Strategy implementation: What is the failure rate?" (JMO 21(2), 2015) · BCG, "Flipping the Odds of Digital Transformation Success" (2020-10) · Bain, 88% 新闻稿 (2024-04) 与 Mankins & Litre, "Transformations That Work" (HBR, 2024) · Sauer, Gemino & Reich (CACM 50(11), 2007) · Loureiro et al. (Heliyon, 2024) · Ika & Pinto, "The re-meaning of project success" (IJPM 40(7), 2022)

**Agile 档案**:Digital.ai/VersionOne, State of Agile Reports 第 14-18 期 · Dikert, Paasivaara & Lassenius (JSS 119, 2016) · Jørgensen, "Relationships Between Project Size, Agile Practices, and Successful Software Development" (IEEE Software 36(2), 2019) · Scaled Agile, framework.scaledagile.com/about 及 scaledagile.com 营销页 · Putta, Paasivaara & Lassenius (XP/PROFES 2018) · Verwijs & Russo, "Do Agile Scaling Approaches Make A Difference?" (EMSE, 2024; arXiv:2310.06599) · USAF CSO Chaillan, Memorandum for Record on Agile Frameworks (2019-12-28) · Jeremiah Lee, "Spotify's Failed #SquadGoals" (2020) · Kniberg (blog.crisp.se, 2015) · Banking Dive, Capital One 报道 (2023-01) · Fowler, "FlaccidScrum" (2009) · Dave Thomas, "Agile is Dead (Long Live Agility)" (2014)

**DevOps 档案**:DORA/Google Cloud, State of DevOps / DORA Reports (2018-2025) 及 dora.dev/faq · Forsgren, Humble & Kim, *Accelerate* (2018) · Sallin et al. (XP 2021) · The Register (2021-09) · Gartner, "The Secret to DevOps Success" (2019) · GE 新闻稿 (2015-09-29、2018-12-13) · The Conversation, GE Digital 分析 (2018) · Keunwoo Lee, Accelerate 书评及 Humble 回应

**变革理论与中层**:Appelbaum, Habashy, Malo & Shafiq (JMD 31(8), 2012) · Cummings, Bridgman & Brown (Human Relations 69(1), 2016) · Burnes (JABS 56(1), 2020) · Stouten, Rousseau & De Cremer (AMA 12(2), 2018) · Pollack & Pollack (SPAR 28, 2015) · DiMaggio & Powell (ASR 48(2), 1983) · Staw & Epstein (ASQ 45(3), 2000) · Westphal, Gulati & Shortell (ASQ 42(2), 1997) · Abrahamson (AMR 21(1), 1996) · Abrahamson & Fairchild (ASQ 44(4), 1999) · Wooldridge & Floyd (SMJ 11(3), 1990) · Huy (ASQ 47(1), 2002) · Balogun & Johnson (AMJ 47(4), 2004) · Guth & MacMillan (SMJ 7(4), 1986) · Oreg, Vakola & Armenakis (JABS 47(4), 2011) · Coch & French (Human Relations 1(4), 1948) · Bartlem & Locke (1981) · French, Israel & Ås (1960) · Prosci, "Top Contributors to Success" · Gartner 变革疲劳系列 (2022-2023) · O Morain & Aykens (HBR, 2023-05) · Reichers, Wanous & Austin (AME 11(1), 1997)

**AI 采纳记录**:Lütke 备忘录 (X, 2025-04-07) · Fortune, von Ahn 播客言论报道 (2026-04-13) · Business Insider/Entrepreneur, Liuson 内部信报道 (2025-06) · HR Grapevine, Meta 绩效新规 (2025-11) · TechCrunch, Coinbase (2025-08) · McKinsey, "The State of AI" (2025-03) · IBM/牛津经济研究院 CEO 调查 (2025-05) · Accenture 8-K (SEC, FY2024/FY2025) · BCG 年报新闻稿 (2025) · WSJ/Alex Singla, QuantumBlack (2025) · Revelio Labs, AI 认证分析 (2026) · Microsoft/LinkedIn Work Trend Index (2024) · KPMG × 墨尔本大学, "Trust, attitudes and use of AI" (2025) · Gallup, Q4 2025 工作场所 AI 使用 (gallup.com/workplace/701195) · METR, "Measuring AI Ability to Complete Long Tasks" (arXiv:2503.14499) · DORA 2024/2025(口径沿用本站《当代码变得便宜》已验证记录)

*调研材料与全部验证判定存于研究底座(7 条调研线、30 组承重论断 × 3 票对抗验证:30/30 挺过、20 组含口径修正、0 推翻)。*
