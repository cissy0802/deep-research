# 「95% 试点失败」体检:一个病毒数字的解剖,与企业 AI 的真实基率(深入版)

> 本文承重论断经 34 组 × 3 票对抗验证(102 票:34/34 挺过、0 推翻、11 组口径修正),其中 4 组单源实证另设反证搜索席与方法学审计席(8 份判决:1 组普遍否定被降级、1 组"两家对台"框架被独立证据推翻重写、1 组因果证据被拆分降级、1 组自报数字被禁止与 RCT 并列)。正反证据并陈,引用尽量带口径。

## 0. 两天,一句话,千亿市值

2025 年 8 月 18 日,Fortune 发表了一篇报道,标题是 "MIT report: 95% of generative AI pilots at companies are failing"。第二天,美股 AI 板块回调:Nvidia 跌 3.5%,Arm 跌 3.8%,Palantir 单日重挫(Gizmodo 记为近 -9%,Fortune 记为近 -10%)。多家财媒把这次回调与这份"MIT 报告"联系起来——通常还并列另一个触发因素:Sam Altman 同周说投资者"整体上对 AI 过度兴奋"。D.A. Davidson 的分析师 Gil Luria 给了第三种读法:"This is really just the pendulum swinging back"——估值太高了,回摆而已。没有任何事件研究能把跌幅归给哪一句话;归因是叙事,不是测量。

确定的事实只有一个:从这一周起,"95% 的企业 AI 试点失败"成了整个行业引用密度最高的统计量。它出现在董事会简报里、卖方研报里、供应商的营销页里,一直活到今天。

这份报告是 MIT Project NANDA 的《The GenAI Divide: State of AI in Business 2025》,26 页,版本号 v0.1,自我定位是 "Preliminary Findings"。本文做三件事:把报告原文逐字解剖一遍;把"95%"这一年的传播变异链和它背后的利益结构对齐;然后回答那个更值得问的问题——**企业 AI 落地的真实失败率到底是多少,以及"失败率"这个词到底在测什么。**

这是本站第二次给一个百分比做体检。上一次是[「70% 转型失败」考古](https://cissy0802.github.io/deep-research/seventy-percent-failure-deep.html),那篇文章结尾写道:值得盯住的下一个候选僵尸数字,是"95% 的 AI 试点失败"。现在它排到了。

## 1. 解剖:报告里到底写了什么

### 1.1 一句话,三个构念

"95%"在报告里的出生地是执行摘要,原句:

> "Despite $30–40 billion in enterprise investment into GenAI, this report uncovers a surprising result in that 95% of organizations are getting zero return. … Just 5% of integrated AI pilots are extracting millions in value, while the vast majority remain stuck with no measurable P&L impact."

注意口径:**"95% 的组织零回报"**。而报告里唯一能追溯到数据图表的 5%,在第 3.2 节——一张漏斗图,对象是"嵌入式或任务专用 GenAI 工具"(即定制企业工具):调研过的组织 60%,进入试点 20%,成功实施 5%。对照组是通用 LLM 聊天工具:80% → 50% → 40%。报告随后写道:"The 95% failure rate for enterprise AI solutions represents the clearest manifestation of the GenAI Divide."

把这三处并排,你会发现**同一对 95%/5% 被套在三个互不等价的构念上**:①95% 的组织"零回报";②5% 的"integrated AI pilots"提取百万级价值;③任务专用工具漏斗里 5% 进入生产(漏斗的基数本身还在"组织"和"解决方案"之间摇摆)。三者不是同一件事:一家公司的定制工具没进产线,不等于它零回报——它可能正用着通用 ChatGPT 省下真金白银,这正是报告自己在别处测到的。分子从"未进入生产"被悄悄改写成"零回报",①和③才凑成了同一个 95%。

Wharton 教授 Kevin Werbach 抓住的正是这一点。他通读报告多遍后公开写道:

> "There appears to be no further support for the 95% claim. … There is a 5% number in Section 3.2, for 'custom enterprise AI tools' being 'successfully implemented.' But that's much narrower. And successful deployment is defined as 'causing a marked and sustained productivity and/or P&L impact.' In other words, 'unsuccessful' explicitly does not mean 'zero returns.'"

另一层换算被 80,000 Hours 的复盘点破:漏斗里 80% 的组织**根本没试点过**任务专用工具。若以"做过试点的"为分母,成功率是 5/20 = 25%;"95% 试点失败"这句话里的"试点",大部分从未发生。

### 1.2 "成功"的两套定义,与"方向性准确"

报告第 6-7 页的 Research Note 给出成功的定义:

> "We define successfully implemented for task-specific GenAI tools as ones users or executives have remarked as causing a marked and sustained productivity and/or P&L impact"

——**有用户或高管"评价说"造成了显著且持续的影响**。这是访谈印象口径,不是财务数据口径。而附录 8.2 又给了第二套定义:"Success defined as deployment beyond pilot phase with measurable KPIs. ROI impact measured 6 months post-pilot"。两套定义互不一致,报告自己承认 "success definitions may differ across organizations",并且写明:

> "Research Limitations: These figures are directionally accurate based on individual interviews rather than official company reporting."

以及一句几乎无人转引的自我豁免:六个月观察窗"may be insufficient to fully assess 'successful deployment' for complex enterprise systems, potentially understating success rates"。也就是说,那个抹掉千亿市值的数字,按报告自己的说法,是一个基于访谈印象、方向性准确、观察窗可能太短、定义在两套之间移动的初步估计。

### 1.3 样本:52 + 153 + 300,审稿人是第四作者

报告 NOTES 页的方法学自述:300+ 个公开披露 AI 项目的案头梳理、52 家机构的结构化访谈、四场行业会议现场收集的 153 位高管问卷。研究期 2025 年 1-6 月。问卷是会议现场的便利样本,不是随机抽样;附录自认 "Selection bias possible"。

署名四人:Aditya Challapally、Chris Pease、Ramesh Raskar、Pradyumna Chari。"Reviewers" 一栏列着 Pradyumna Chari 与 Project NANDA——Chari 是第四作者,即自己审自己。报告非同行评审,获取渠道从发布至今是一个 Google 表单;爆火当口,连记者都拿不到原文,镜像 PDF 靠第三方网站流传。80,000 Hours 的 Rob Wiblin 对样本量的评语:"Flip one or two interviews the other way and you'd get a completely different headline."

### 1.4 报告里方向相反的数据

被标题掩埋的是,报告内部有一批与"AI 全面失败"方向相反的测量,几乎无人转述:

- **影子 AI 经济**:"While only 40% of companies say they purchased an official LLM subscription, workers from over 90% of the companies we surveyed reported regular use of personal AI tools for work tasks. In fact, almost every single person used an LLM in some form for their work." 报告甚至写道,这种影子使用 "often delivers better ROI than formal initiatives"。
- **通用工具的漏斗是成功故事**:80% → 50% → 40%,报告另一处给出 "Generic LLM chatbots appear to show high pilot-to-implementation rates (~83%)"。
- **外购比自建成功率高一倍**(约 67% vs 33%)——且报告自己紧跟着承认 "The correlation between external partnerships and success does not necessarily prove causation"。

### 1.5 内部对不上的数字

报告内部至少三处自相矛盾:行业总数执行摘要说 8 个、正文说 9 个;销售营销吃掉的 AI 预算占比,同一节内一处写约 70%、另一处写约 50%;知识工作者个人 AI 使用率,一处写"超过 40%"、另一处写 90% 的公司几乎人人在用。一份内部数字都没有对齐的 26 页初稿,成了 2025 年被引用最多的企业 AI 统计来源。

## 2. 变异:一条数字的一年

### 2.1 首发即变异

病毒式误读通常被想象成长链条末端的走样。这一次不是——**第一篇报道就换了口径**。Fortune 标题把"95% 的组织零回报"写成"95% 的试点在失败";正文还把方法学写成 "150 interviews with leaders, a survey of 350 employees, and an analysis of 300 public AI deployments"。对唯一公开的 v0.1 版本做全文检索,150 和 350 这组数字不存在;报告自述是 52 家机构访谈、153 位高管问卷(是否存在含此数字的未公开版本,无从证实)。Fortune 不仅把样本量放大了 2-3 倍,还把"153 位高管"变成了"350 名员工"——身份也漂了。这组错误数字被数十家媒体照抄,至今没有更正;2026 年的很多引用页仍在用 Fortune 版方法学。

### 2.2 变体谱系

传播链上可辨识出九类变体,举其要者:

- **V0(原文)**:"95% of organizations are getting zero return"。
- **V1(Fortune 标题)**:95% 的试点在失败——organizations 变 pilots,zero return 变 failing。
- **V3(Entrepreneur)**:"Nearly 95% of Companies Saw Zero Return on In-House AI Investments"——凭空加了 in-house 限定,而报告说的恰恰是外购成功率更高。
- **V5/V6(泛化终点)**:"95% of Enterprise AI Fails" → "95% of AI projects fail"——所有限定语(generative、pilot、P&L、六个月)全部脱落。
- **V7(机构升格)**:FT 专栏写成 "Recent research led by Aditya Challapally at the MIT Media Lab"——一份项目组初步报告,层层升格为 MIT Media Lab 研究。
- **2026 年的杂交代际**:长尾内容里出现了无出处的"90% 的企业 AI 实施失败"——95%(NANDA)与 80%(RAND 转引)在内容农场里杂交出的新数字。

### 2.3 对照组:与 95% 混用的那些数字

"失败率仪表盘"式的文章通常把 95% 与一串数字并列;把它们的口径逐一还原:**S&P Global 451**:"The share of companies abandoning most of their AI initiatives jumped to 42%, up from 17% last year"——主语是公司不是项目(n=1,006,北美+欧洲,2024 年 10-11 月实地),同报告称平均组织在投产前砍掉 46% 的 PoC。**Gartner**:"At least 30% of generative AI projects will be abandoned after proof of concept by the end of 2025"——2024 年 7 月的预测,将来时;2026 年 Gartner 自我修订称实际超过 50%,而把 2024 预测当已发生统计引用的文章无人回头改。**RAND**:"By some estimates, more than 80 percent of AI projects fail"——RAND 报告开篇转引的他人估计,RAND 自己的工作是访谈 65 位从业者归纳失败根因,没测过失败率。**IBM**:"only 25% of AI initiatives have delivered expected ROI"——2,000 名 CEO 的自报,分母是项目、标尺是自家预期。五个数字,五种分母,被当同一个"AI 失败率"混用。

### 2.4 2026 年的来世

截至 2026 年 7 月:NANDA 没有出续作或修订版,底层数据从未公开,报告仍以 v0.1 流传,MIT Media Lab NANDA 小组的 publications 页面不收录它,无撤稿、无免责声明、无作者更正。数字本身活得很好——最卖力的引用者是有方案要卖的厂商内容营销("MIT says 95%…开头,数据治理/平台方案结尾"),少数引用者(如 Pertama)保留了原始限定语。2026 年最系统的清算不是来自学术界或 MIT,而是 80,000 Hours 的播客复盘,其定性:"an opaque, conflicted, barely-scrutinised report managed to attract the MIT label, move markets and have a vast impact on global opinion about AI."

## 3. 利益:谁写的报告,卖什么药

### 3.1 诊断书末尾的药方

Project NANDA 的全称是 Networked Agents And Decentralized Architecture——MIT Media Lab 教授 Ramesh Raskar 发起的 agent 协议项目,自我定位是"AI 的 TCP/IP",做 agent 注册、发现、信誉与支付基础设施。报告的核心论点是:GenAI 试点失败是因为工具不会学习("The core barrier to scaling is not infrastructure, regulation, or talent. It is learning"),解药是有记忆、能自适应的 agentic AI。而报告正文两次把 NANDA 与 MCP、A2A 并列为支撑这一转型的基础设施;§6.5 描绘的未来里,agent 将 "execute trustless transactions through blockchain-enabled smart contracts";结论章建议企业 "start partnering with vendors"。

80,000 Hours 的复盘把这层关系说破:四位作者 "all either currently developing or trying to sell" 报告推荐的那类 agentic 框架,报告 "marketed under the MIT brand with no conflict of interest disclosure"。NOTES 页那句"匿名化是为了防止商业化观感"的声明,与正文里三次出现的自家协议名并存。

### 3.2 具名批评与零回应

批评者的名单不短,且都留了逐字记录:Werbach 要求 "release the full supporting data. If not, it should retract the report";Marketing AI Institute 的 Paul Roetzer 称其 "not a viable, statistically valid thing";Oxford fellow Ajit Jaokar 称其 "a clever marketing gimmick";Futuriom 的首席分析师 Raynovich 称其 "irresponsible and unfounded",并用自家 130+ 企业案例库举反例。一年过去,这些批评得到的回应是零。

### 3.3 MIT 的另一个数字

2025 年,MIT 出圈的企业 AI 数字有两个。另一个方向相反:博士生论文称 AI 让材料发现提速,被顶级学者背书、被国会引用——2025 年 5 月 16 日,MIT 经济系公开声明对该论文数据 "no confidence in the provenance, reliability or validity of the data and has no confidence in the veracity of the research",请求从 arXiv 撤下、从 QJE 审议中撤回(批评者称数据涉伪造;论文从未正式发表)。正反两个最出圈的"MIT 数字",都没过方法学体检。教训不是"MIT 不可信",而是:**机构品牌不传递方法学质量,正面结论和负面结论一样需要验尸。**

## 4. 口径混战:90% 成功与 90% 失败同时为真

把 2024-2026 年主要的"企业 AI 回报"数字排开,光谱两端能差出九十个百分点。逐份还原口径之后,混战的机制清晰可辨。

### 4.1 厂商的暖数字是怎么造出来的

**Microsoft/IDC 的 "$1 回报 $3.7x"**(2024-11,Copilot 营销的主力数字):底层是一道自估选择题——"What would you estimate your organization's ROI is for every $1 spent on generative AI projects or initiatives?",选项是 1x/2x/3x/4x/5x/5x+ 的倍数桶,"not sure" 被剔除出分母,受访者本身是"负责推动 AI 转型的人"——评价自己主抓的项目。全样本里只有 **1%** 选了 "No ROI"。配套的 "top leaders 回报 10.3x" 是循环定义:"Top leaders are 18% of the leaders who realize more than 5x return"——先按回报筛人,再宣布这群人回报高。

**Google Cloud 的 "74% 一年内实现 ROI"**(2025-09):分母只包含年收入 $10M 以上**且已部署 GenAI** 的企业——没上车和上车后退出的都不在样本里。报告另有一个巧合同值的广度指标:74% 在"至少一个用例"上见到 ROI(agentic 早期采用者 88%)。两个 74% 一个是时间维度、一个是用例维度,营销页把它们叠成一句。至于收入:自报"带来业务增长"的 56%,其中"收入上升"的 71%,其中"涨了 6-10%"的 53%——三层套娃相乘,全样本约两成。

厂商侧也有异类:Anthropic 的 Economic Index 只报用量结构、不做回报倍数断言;AWS 的采用率调查同样回避 ROI 题。主动给倍数的,恰是要卖 Copilot 和云的那两家。

### 4.2 咨询的冷数字,与惊人收敛的"精英少数"

**McKinsey**(2025-11,n≈2,000):88% 的组织至少一个职能在用 AI,但 "Meaningful enterprise-wide bottom-line impact from the use of AI continues to be rare"——约 39% 能把任意程度的企业级 EBIT 影响归因于 AI(其中大多数说影响不足 5%);同时满足"≥5% EBIT 归因 + 自评获得显著价值"的 "AI high performers" 约占 6%。

**BCG**(2025-09,n=1,250):5% 的公司在规模化产生价值,60% 没有实质价值。方法节里有一句罕见的自我披露:"Unless explicitly stated as realized…reported numbers reflect expected future impact. … responses may be subject to perception bias."——除非注明"已实现",数字是**预期**,且自认有感知偏差。

**Deloitte** 一家给出两幅面孔:2024 年 Q4 wave 说近 3/4 的项目达到或超出 ROI 预期——只问受访者**最先进的那一个**项目,标尺是自家预期,受访者是 AI 项目干系人;2025 年的欧洲中东版说一年内回本的只有 6%,典型回本期 2-4 年。同一家公司,换个问法,从暖到冷。

**IBM**(2025-05,2,000 名 CEO):只有 25% 的 AI 项目达成预期 ROI,16% 实现企业级规模化;同一份报告里,85% 的 CEO 预计到 2027 年会有正回报。64% 的 CEO 承认怕落后所以"在弄清价值之前就投了钱"。失败是现在时,成功永远是将来时。

**PwC**(2026-01,4,454 名 CEO,过去 12 个月实际结果口径):"56% report neither increased revenue nor lower costs from AI over the past 12 months";22% 说成本反而升了;实现增收+降本双收益的只有 12%。

**Bain**(2026-06,951 家 $100M+ 企业,只统计实际度量了结果的子样本):"The technology worked. The value didn't arrive." 37% 的公司把降本目标定在 11-20%,实测度量过的公司里近四成落在 0-10% 档。最尖锐的发现是资金结构:44% 的大企业把**先前自动化项目的节省**列为下一轮 GenAI/agentic 投资的资金来源——而 Bain 的分析是,那批节省本身系统性未达标;在这批欠交付企业中,约 90% 如今仍在为 AI agent 加码预算。用尚未兑现的节省给下一轮下注,是期望的滚动结构。

注意咨询侧"少数赢家"比例的收敛:BCG 5%、McKinsey 6%、Accenture 8%(front-runners)、PwC 12%。这既可能是真实基率,也恰好契合"少数人成功、你需要帮助"的服务销售叙事——两种解释不互斥。

### 4.3 谁在回答,答案就归谁

Wharton 与 GBK 的《Accountable Acceleration》(2025-10,n≈800 美国大企业决策者)被媒体广泛当作 NANDA 的对台戏(报告与新闻稿本身并未点名 MIT;Wharton 作者 Puntoni 在采访中说得直白:"Our definition is very different from the MIT report. Theirs is much more stringent.")。它测到:近四分之三的决策者"已见到正 ROI"。原文用词是 perceptions、believe——感知口径。而同一份数据里藏着口径混战的微观机制:**VP 及以上 81% 认为 ROI 为正,中层管理者只有 69%**。职级差 12 个百分点,而绝大多数调查只问高管。S&P 的样本含中层,数字立刻变冷;KPMG 每季约 130 人的小样本里,agent 部署率一年内走出 11%→42%→26% 的过山车——"谁在回答、怎么问"本身就是测量结果的一部分。

### 4.4 一把尺子的阶梯

混战可以用六个维度几乎完全解释:**分母**(项目/组织/你最好的那个项目/至少一个用例)、**标尺**(自估倍数 < 达成自家预期 < 感知正回报 < 实测增收降本 < EBIT 归因 < P&L 显著加速)、**样本准入**(只查已部署者=剔除失败退出者)、**回答者职级**、**时间窗**、**自报还是实测**。标尺每严一级,"成功率"掉一档:IDC 口径 99% 有回报 → Deloitte 最佳项目 74% 达预期 → Wharton 感知 74% → IBM 项目层 25% → PwC 实测双收益 12% → McKinsey EBIT 高标准 6% → BCG 规模化 5% ≈ NANDA 试点→P&L 5%。

看清这个阶梯,NANDA 的位置就清楚了:**它的 5% 在严口径末端并不是离群值**——与 McKinsey 的 6%、BCG 的 5%、PwC 的 12% 同处一段。它的问题从来不是方向,而是:用 52 个访谈的便利样本报出精确到个位的百分比,再把"未达显著 P&L 影响"改写成"零回报",最后被媒体升格为"AI 全面失败"。同一段阶梯,Wharton 的 74% 与 McKinsey 的 6% 不构成矛盾——它们是两把不同的尺子,而"95% vs 74% 谁在撒谎"的争论,本身就是没看懂尺子。

## 5. 独立测量:政府统计与注册数据的三个事实

跳出厂商与咨询的问卷,官方统计与学术注册数据给出的图景可以概括成三句话:用得快,用得浅,藏着用。

### 5.1 用得快

Bick、Blandin 与 Deming 的 RPS 调查(美国人口代表性样本)测到:生成式 AI 三年达到约 53% 的成人采用率,扩散速度超过 PC 和互联网的同期;2025 年 11 月轮,成人采用 54.6%,工作中使用 37.4%。Census BTOS(约 120 万企业样本框)的企业口径曲线从 2023 年 9 月的 3.7-3.8% 升到 2025 年底约 18%(就业加权约 32%)——但引用这条官方曲线必须带一个脚注:**2025 年 11 月起问卷从"用 AI 生产商品或服务"放宽为"任一业务职能使用"**,Census 与 Fed 都书面承认后段涨幅含测量效应。

### 5.2 用得浅

同样是官方数据:采用 AI 的美国企业中,57% 只在三个及以下业务职能使用;在报告了任务效应的企业中,约 66% 纯粹用于增强而非替代;因 AI 减员的企业约 2%(Census 工作论文,2025-11~2026-01 窗口)。欧元区:约 71% 的企业称在用 AI(含实验性使用),但 ECB 2026 年 6 月的评估是强度使用仅约 7%——"The intensive use that drives transformation…remains rare"。支付口径同构:Ramp 客户企业的付费 AI 采用率 2026 年 3 月首破 50%(50.4%,一年前为 35%),但到 6 月,企业 AI 支出的**中位数只有每员工每月 $11.38**,top 1% 是 $7,449——"付费采用过半"与"绝大多数企业投入接近零"同时为真。

效果端,最好的因果证据也指向"浅":RPS 受访者自报 AI 节省的时间只占总工时约 1.6%。丹麦的全员行政注册数据(Humlum & Vestergaard,11 个暴露职业、约 2.5 万工人 × 7,000 个工作场所)对工资与工时给出精确零效应——"precise null effects on earnings and recorded hours…ruling out effects larger than 2%"(ChatGPT 发布两年后的测量);采用者自报省时约 3%,而任务级 RCT 文献(如 QJE 客服实验的 +15%)高出一个数量级。2026 年 3 月的修订版把标题改成了 "Still Waters, Rapid Currents",解释重心移向"结构先变、收入后动":任务在重组、AI 相关新任务在铺开、人在向 AI 相关职业流动,只是还没走进工资单。宏观端同向:Goldman Sachs 自家经济学家 2026 年 3 月的结论是 "We still do not find a meaningful relationship between productivity and AI adoption at the economy-wide level"(与其 2023 年"AI 十年抬升全球 GDP 7%"的预测同门对照);其口径下的亮点——客服与软件开发约 30% 的中位增益——来自财报电话会上自愿披露数字的少数公司的自报,不是独立测量;S&P 500 里量化了 AI 对盈利影响的公司,Goldman 数出来约 1%。

### 5.3 藏着用

Fed 2026 年 4 月的研究简报点名了同一时点三个官方数字的打架:BTOS 企业口径约 18%,RPS 工人自报约 41%,Atlanta Fed SBU 的就业加权口径约 78%(就业加权近似"劳动力中有多少人在已采用 AI 的企业工作")。Fed 给出的解释之一是**答卷人之间的信息不对称**:员工用个人账号使用 AI,高管看不见。覆盖 47 国 48,000 人的 KPMG-墨尔本大学调查提供了机制证据:**57% 的员工向雇主隐瞒 AI 使用、把 AI 产出当自己的成果**,近半承认曾把敏感信息传进公共 AI 工具。NANDA 报告里那组 90%(员工私用)对 40%(官方采购)的缺口,方法虽弱,方向与官方数据同构——**企业口径测的是官方部署率,不是实际使用率**。"95% 试点失败"与"人人都在用 AI"因此并不矛盾:失败的是正式项目的 P&L 归因,繁荣的是统计不到的影子使用。

## 6. 历史基率:把 95% 放进三十年序列

"高失败率数字 + 权威署名 + 卖方传播"不是 AI 时代的发明。逐个验尸:

- **Standish CHAOS(1994 起,"只有 16% 的软件项目成功")**——同一家公司的数据按其口径可以在 5.8% 与 94.2% 的成功率之间翻转,主席自认数据应被视为"观点"。完整解剖见[「70% 转型失败」考古](https://cissy0802.github.io/deep-research/seventy-percent-failure-deep.html),此处不重复。
- **"85% 大数据项目失败"(2017)**——全部证据是 Gartner 分析师 Nick Heudecker 的一条个人推文("closer to 85 percent"),该推文后来被删除;Gartner 正式预测的原文是 "Through 2017, 60 percent of big-data projects will fail to go beyond piloting and experimentation and will be abandoned"(2015 年做出的预测,将来时)。一条已删除的推文,被当作"Gartner 研究结论"引用了近十年。
- **"85% 的 AI 项目失败"(2018)**——Gartner 原句是 "Through 2022, 85 percent of AI projects will deliver erroneous outcomes due to bias in data, algorithms or the teams responsible for managing them":一个关于**偏差会导致错误结果**的预测(几乎恒真),流通中变形为实测失败率。Tom Davenport 的评语:"actually has no data at all on what percentage of projects fail."
- **Cisco "近四分之三的 IoT 项目在失败"(2017)**——自家数据是:60% 的项目停在 PoC,26% 的**受访公司**曾有过一个自评"完全成功"的 IoT 项目;标题的 74% 是把"不是完全成功的公司"全部算成 failing 倒推出来的。而按已完成项目口径,约三分之二被认为成功;64% 的受访者说失败试点的经验教训反而加速了投资。
- **"制造业卡在试点炼狱"(2018-2021)**——McKinsey 系口径:84%(2018,"做 IoT 的公司",经 IndustryWeek 转述)、56%(2019,制造企业)/74%(2020)——后两个均经 LNS 转引,一手未核;竞争对手 LNS Research 测得 13%(2019)、7%(2021)并公开称这套叙事是 "fake news"。而高侧其实有独立同向证据(BCG 71% 未突破规模化、IDC "每 33 个 AI 试点只有 4 个投产"、WEF 千余场址普查 >70%、Capgemini 约 86%),而 LNS 的 7-13% 是孤立低值,且构念更窄——它数的是把"卡在试点**且结果不明**"勾进前三大挑战的公司。两边数字都真实,差距是**单向的定义错位**,不是测量僵局。这组对照证明的是:失败率是问法的函数。
- **"80-90% 的新产品失败"**——Castellion & Markham 2013(JPIM)综述 1977 年以来的实证文献:实测约 40% 或更低,80-90% 之说是靠诉诸大众与卖方自利存续数十年的 urban legend。

序列里还有一个**逐字同值的先例**。哈佛商学院的 Shikhar Ghosh 研究了 2,000+ 家获投创业公司,WSJ 2012 年的报道口径:"If failure is defined as failing to see the projected return on investment…then more than 95% of start-ups fail." 同一批公司,按清算口径失败率 30-40%,按"未返还资本"口径 65-75%,按预期 ROI 口径 95%——失败定义每收紧一档,数字翻一番。药物研发同理:Phase I 到上市的成功率,BIO 口径 9.6%,Wong et al. 2019 的 path-by-path 口径 13.8%——44% 的相对差主要出自方法学(原文措辞是 "may be due to"),数据窗与数据库亦不同——而没有人因为九成候选药失败而宣称"制药不行",高失败率在制药被理解为**漏斗的形态**,不是行业的死刑。

学术直测的 IT 项目"彻底失败"基率,反而低得多:Sauer、Gemino 与 Reich 对 412 个英国项目的测量,只有 9.2% 被放弃,约 67% 接近预期交付;28 项调查的元综述给出 6.87-31.1% 的放弃率区间。Flyvbjerg 的 5,392 个 IT 项目数据库显示超支与低于预算"about equally frequent",中位数与众数接近零、均值约 +80%——**肥尾,不是普遍失败**。

这个序列给出三个结论。第一,作为"试点→规模化"的漏斗数字,95% 毫不异常——它与 VC 的 ROI 口径逐字同值,与药物、新品、大数据、IoT 的试点存活率同一形态。第二,作为"AI 项目全军覆没"的读法,95% 与全部历史测量矛盾——彻底放弃率的实测从来在一到三成之间。第三,也是最重要的:**这些失败率数字几乎从不测量它们声称测量的东西**——测的是预测偏差(Standish)、是偏差预测(Gartner 85%)、是"非完全成功"(Cisco)、是定义自选(LNS/McKinsey)、是及格线设在"完美"(Ghosh 的 95%)。为什么辟谣杀不死它们?Letrud & Hernes 2019 给过量化答案:在引用了辟谣文献的论文里,468 篇仍在确认迷思,只有 40 篇否定——12 比 1。辟谣文献成了迷思的传播载体。

## 7. 理论:四种读法,四个互斥的处方

理论底座决定你把"95%"读成什么。四个框架,四种读法,处方互斥。

### 7.1 J 曲线:这就是谷底的样子

Brynjolfsson、Rock 与 Syverson 的生产率 J 曲线(AEJ: Macroeconomics 2021)机制:通用技术要求大量无形互补投资(流程再造、数据、培训),这些投资在国民账户里先计为成本、不计为产出,于是新 GPT 的早期生产率被系统性低估,收获期又被高估。关键预测原文:

> "In fact, the more transformative the new technology, the more likely its productivity effects will initially be underestimated."

在这个框架下,"95% 无可测 P&L 影响"是模型对下探段的**定义性预测,而非反例**。论文结尾把 Solow 名言正面翻转:"in the future…we will see new technologies everywhere including the productivity statistics."

这个机制层有独立确认,但带修正:KU Leuven 团队用比利时 B2B 交易微观数据确认了无形资产驱动的企业级 J 曲线,但量级只有约 3% 的 TFP 低估(BRS 的头条数字是 15.9%),且偏差集中于小而年轻的企业——异质性方向与美国证据相反;国际复现分裂(韩国存在、法日未见)。实证上最常被引的"因果确认"是 Census 工作论文(CES-WP-25-27,2025-04,Brynjolfsson 合著):在美国制造业微观数据中报告了 J 型回报的因果证据,短期损失集中于老企业、其中约三分之一可归因于结构化管理实践被放弃。方法学审计席对这份证据作出降级:它未经同行评审、底层是外人无法复制的保密数据、依赖一根作者自认排他性无法直接检验的工具变量、上行臂来自幸存企业的组间比较;它测的是 **2021 年前的工业/预测型 AI,不是 GenAI**;而且它的 J 曲线机制是真实的生产扰动("rather than primarily mismeasurement"),与 BRS 的计量假象机制**相反**——同形状,不同病理。加拿大统计局微观数据上的独立尝试则没有找到 J 曲线。

2026 年 2 月,对垒进入最干净的一周:Brynjolfsson 公开宣称美国正 "transitioning out of this investment phase into a harvest phase"(依据:2025 年生产率增速约 2.7%,几乎两倍于十年均值);前一天,Apollo 首席经济学家 Torsten Slok 写下 "AI is everywhere except in the incoming macroeconomic data"。同一批宏观数据,相反结论;2.7% 的提速没有任何 AI 因果归因。"走出谷底"目前是公开争议,不是事实。

### 7.2 吸收能力:失败不是随机的,一部分人永远过不去

Cohen & Levinthal 1990(ASQ)定义吸收能力为 "ability to recognize the value of new, external information, assimilate it, and apply it to commercial ends"——它是先验相关知识的函数,是自己做研发与运营的**副产品,买不来**。最狠的预测是锁死(lockout):在快速演进的领域一旦停止投资吸收能力,"it may never assimilate and exploit new information in that field, regardless of the value of that information"。

这个框架与 NANDA 报告有一次针尖对麦芒的相遇。NANDA 的诊断句是 "The core barrier to scaling is not infrastructure, regulation, or talent. It is learning."——字面上与吸收能力理论一致。但 NANDA 把 learning 归给**软件**(工具要会记忆、要能自适应),C&L 传统把 learning 归给**组织**(先验知识、流程、守门人);报告全文检索不到 "absorptive" 一词。同一个词,两张完全相反的采购单:买"会学的工具",还是建"会学的组织"。而报告作者卖的恰是前者。Bresnahan、Brynjolfsson 与 Hitt 的经典三角互补(QJE 2002)站在后者一边:IT 的回报取决于 IT 与组织再造、新产品流程的组合,单买技术不出回报。在吸收能力读法下,95% 不会自动收敛——失败集中于缺乏先验能力存量的组织,其中一部分会被锁死在门外。

### 7.3 Acemoglu:95% 可能是天花板的影子

Acemoglu 2024(NBER w32487)的测算:AI 十年 TFP 增益 "no more than a 0.66%",且他自己两次强调这是**上界**;计入 hard tasks 折扣后不到 0.53%。原文点名这远低于 Goldman(全球 GDP +7%)与 McKinsey($17-26 万亿)的预测。他的 2030 预言:"most companies are going to be doing more or less the same things." 在这个读法下,试点大面积不动 P&L 是**正确测量到了小效应**——不是测量假象,等十年也不会有 J 型反弹;高失败率是技术经济价值有限加上方向错误(过度自动化、不足增强)的表现。

### 7.4 电气化同构:1900 年的"95%"

Paul David 1990(AER P&P)在讨论 Solow 悖论时写下一个句式复刻:"In 1900, contemporary observers well might have remarked that the electric dynamos were to be seen 'everywhere but in the productivity statistics!'"(dynamos,发电机)。电气化从第一座中央电站(1880 年代)到制造业生产率显效(1920 年代初)历时约四十年;延迟的主因是仍可用的旧厂房不值得推倒——直到单机电驱(unit drive)让单层厂房、物料流优化、柔性布线成为可能,而这又要求"building up a cadre of experienced factory architects and electrical engineers"(转引自 David 对 Devine 1983 的引述)。收益的大头从来不在省电费,在重构工作流——与今天"21% 重设计工作流"的调查数字异曲同工。Solow 的原话出自 1987 年 7 月 12 日《纽约时报书评》("We'd Better Watch Out",p.36);十三年后,Oliner & Sichel 2000 裁定:IT 使用加上计算机制造,合计解释了 1990 年代后半段生产率提速(约 1 个百分点)的三分之二——"information technology largely is the story"。上一轮悖论有闭环。但 ECB 的 Lane(2026-03)补充了一个当代修正:近几十年 GPT 的扩散速度在加快,四十年的电气化基准可能系统性偏慢。

### 7.5 四种读法怎么共存

四个框架对两个判据给出不同答案:**失败会不会自动收敛**(J 曲线、电气化:会,等互补投资到位;吸收能力:不会,有 lockout;Acemoglu:不会,池子本来就浅),以及**问题出在哪**(J 曲线:测量假象;电气化:真实但必要的重构成本;吸收能力:组织缺陷;Acemoglu:技术上限)。它们不能全对——J 曲线说"越变革越先被低估",Acemoglu 说早期证据反而高估了未来(easy tasks 先行)——但可以分区域各对一块:任务级增益真实存在(RCT 多次复现),企业级归因普遍缺席(严口径 5-12%),宏观级信号至今没有(BLS/Fed/Goldman 同向)。哪个框架赢,要等的正是这三层之间的传导是否发生。已经有人用这些框架评论 NANDA 数字(Rasmus 接 Solow、Sequoia 接 J 曲线——注意 VC 立场),但截至 2026 年 7 月,没有任何同行评审论文正面检验过那个 95%。

## 8. 裁决:企业 AI 落地的真实基率

回到题目。"转型难度的基率到底是多少?"诚实的答案是分层的:

| 你想测什么 | 最好的现有测量 | 数字 |
|---|---|---|
| 高管感知正回报 | Wharton n≈800(2025) | ~74%(VP+ 81%,中层 69%) |
| 组织自报某目标有正面影响 | S&P VotE(2025-10) | 70-76%,逐年下滑 |
| 项目达成自家预期 ROI | IBM 2,000 CEO(2025) | 25% |
| 过去 12 个月实测增收+降本 | PwC 4,454 CEO(2026) | 12% |
| 企业级 EBIT 归因 ≥5% 且显著价值 | McKinsey n≈2,000(2025) | ~6% |
| 规模化产生价值 | BCG n=1,250(2025) | 5% |
| 定制工具试点→显著 P&L(6 个月窗) | NANDA n=52+153(2025) | 5%(方法最弱) |
| 公司弃置大多数 AI 计划 | S&P n=1,006(2025) | 42%(上年 17%) |
| 历史 IT 项目彻底放弃基率 | 学术直测 28 项调查 | 7-31% |

三个可以负责任写下的判断:

其一,**"95% of organizations are getting zero return" 这句话本身不成立**——报告自己的成功定义(未达"显著且持续"≠零回报)、自己的影子 AI 数据(90% 公司的员工在用且"often delivers better ROI")、自己的通用工具漏斗(约 83% 试点转化)都不支持它;它是把一个窄口径漏斗数字重新包装成的总判词。

其二,**作为严口径漏斗数字的 5% 是可信方向**——它与 McKinsey 6%、BCG 5%、PwC 12% 在阶梯末端收敛,与 VC/药物/新品/IoT 的试点存活形态一致。企业 AI 的真实图景不是"全面失败",是**头部集中**:少数组织在严标准下真金白银地赢,多数组织广而浅地用,官方统计的效果信号被影子使用和时滞双重稀释。

其三,**"失败率"在这个行业里首先是修辞,其次才是测量**。从 Standish 到 85% 推文到 95%,三十年的序列里,数字的生产者几乎总同时是解药的销售者。下一个病毒失败率出现时,三问依旧:分母是什么?标尺是什么?说这话的人卖什么?

## 9. 结语:十二个可检验主张

按证据强度从硬到软排序;每条给出核查方式。

1. **NANDA 报告执行摘要原句是 "95% of organizations are getting zero return",而报告内唯一可追溯的 5% 是任务专用工具漏斗(60→20→5)**——两处口径不等价;一手 PDF 可逐字核对。[多源证实]
2. **报告自述样本为 52 家机构访谈 + 153 位高管会议问卷;Fortune 首发写成 150 访谈 + 350 员工调查,该组数字未见于唯一公开的 v0.1 版本,页面至今无更正**。[多源证实;"任何版本"不可证,故限定于公开版]
3. **报告的"成功"定义是访谈口碑口径("users or executives have remarked…"),附录另有一套 KPI+6 个月定义,两处不一致;报告自称数字仅 "directionally accurate"**。[一手已核]
4. **报告与作者存在未披露的利益结构**:正文两次把 NANDA 协议列为解决方案基础设施,结论建议 "start partnering with vendors";80,000 Hours 记录四位作者均在开发或销售同类 agentic 框架。[多源证实]
5. **截至 2026-07,NANDA 无续作、无数据公开、无更正;MIT Media Lab NANDA 小组 publications 页不含该报告**。[现场核验]
6. **严口径端的独立测量收敛于 5-12%**(McKinsey ~6%、BCG 5%、PwC 12%、IBM 25% 居中),感知口径端收敛于 70-80%(Wharton、S&P 逐目标)——两端测的不是同一件事,口径阶梯几乎完全解释光谱。[咨询自报,口径已逐份核对]
7. **官方统计:采用史上最快、使用广而浅**——RPS 三年 53%;BTOS 企业口径约 18%(2025 底,含问法放宽效应);采用企业 57% 限于 ≤3 职能;自报省时约占总工时 1.6%;ECB 强度使用约 7%;Ramp 中位支出 $11.38/员工/月。[一手官方/独立数据]
8. **丹麦全员注册数据对工资与工时给出精确零效应(排除 >2%),宏观生产率无 AI 归因信号**(BLS 序列、Fed、Goldman 自家研究同向)。[同行评审轨道+一手官方;多源]
9. **影子使用让企业口径系统性低估**:同一时点 BTOS 18% vs RPS 工人 41% vs SBU 就业加权约 78%;57% 员工自报隐瞒 AI 使用。[一手官方+大样本调查]
10. **"95%"有逐字同值先例**:按"未达预期 ROI"口径,"more than 95% of start-ups fail"(Ghosh/WSJ 2012);药物、新品、大数据、IoT 的试点存活率同形态——高失败率漏斗是实验组合的常态,不是 AI 的独症。[同行评审+多源]
11. **历史失败率数字几乎从不测量它声称测量的东西**:85% 大数据=已删推文;85% AI=偏差预测变形;Cisco 74%=非完全成功;pilot purgatory 高低两侧差距=单向定义错位(高侧有独立多源,低侧是窄构念孤值)。[多源证实]
12. **理论四读法(J 曲线/吸收能力/Acemoglu 上界/电气化同构)对"95% 会不会自动收敛"给出互斥答案**;Census 的 J 曲线因果证据属上一代工业 AI 且带方法学保留,GenAI 版检验尚不存在——这是下一个五年最值得盯的空格。[理论+带降级标注的单源]

**值得盯什么**:NANDA 会不会公开数据或出续作(两年零回应后概率渺茫,但那将是唯一能复测 95% 的途径);BLS 生产率序列 2026-2027 的修订会不会出现可归因于 AI 的加速(Brynjolfsson vs Slok 之争的裁决点);Gartner 把"至少 30%"上修到"超过 50%"之后还会不会再修;Bain 发现的"用未兑现节省滚动融资"结构会不会在 2027 年预算周期爆出第一批具名案例;以及下一个病毒失败率数字——按本序列的节奏,它应该已经在路上了。

## 附:主要来源

**报告原文与批评**:NANDA《The GenAI Divide》v0.1(镜像 PDF);Werbach LinkedIn 长评(经 Futuriom);80,000 Hours 播客复盘(2026-04-28);Futuriom;Pivot to AI;Marketing AI Institute;BankInfoSecurity(Jaokar/Furr & Shipilov/Narayanan 汇编)。
**传播链**:Fortune 2025-08-18 首发及 08-21 跟进;The Register;Gizmodo;Axios;Entrepreneur;consultancy.uk;FT(经转引)。
**厂商/咨询口径**:IDC×Microsoft 2024 InfoBrief;Google Cloud ROI of AI 2025;McKinsey State of AI 2025;BCG Widening AI Value Gap 2025(含方法节);Deloitte 2024 Q4 wave 与 2025 AI ROI paradox;IBM CEO Study 2025;KPMG AI Pulse 2025 Q1-Q4;Accenture Front-Runners 2025;Wharton-GBK Accountable Acceleration 2025;PwC 第 29 届 Global CEO Survey 2026;Bain 2026-06;S&P Global 451 VotE 2025-03/2025-10;Gartner 2024-07 预测与 2026 修订;RAND RRA2680-1。
**独立测量**:Census BTOS 及 CES-WP-26-25;Fed FEDS Notes 2026-04;Bick-Blandin-Deming(NBER w32966 及更新);Humlum & Vestergaard(NBER w33777,2026-03 修订版);Brynjolfsson-Li-Raymond(QJE 2025);Otis et al.(Management Science);KPMG-Melbourne 2025;ECB SAFE 2025Q4 与 2026-06 blog;UK ONS BICS;Ramp AI Index;Stanford AI Index 2026;Goldman Sachs 2026-03(经 Fortune)。
**历史基率**:Eveleens & Verhoef(IEEE Software 2010);Sauer/Gemino/Reich(CACM 2007);Flyvbjerg 等(JMIS 2022;HBR 2011);Castellion & Markham(JPIM 2013);Wong/Siah/Lo(Biostatistics 2019);BIO 2016;Cisco 2017 新闻稿;LNS Research;Ghosh(经 WSJ/HBS 2012);Letrud & Hernes(PLoS ONE 2019);Davenport(IIA)。
**理论**:Brynjolfsson/Rock/Syverson(AEJ Macro 2021);Cohen & Levinthal(ASQ 1990);Bresnahan/Brynjolfsson/Hitt(QJE 2002);Solow(NYT Book Review 1987-07-12);David(AER P&P 1990);Devine(JEH 1983,转引);Oliner & Sichel(2000);Acemoglu(NBER w32487 及 2024-12 访谈);McElheran 等(Census CES-WP-25-27);Bijnens/Konings/Putseys(KU Leuven);Slok(Apollo 2026-02);ECB Lane(2026-03)。

*想看每个结论的完整论证、数据出处和反方证据,请读本页;易读版为本文的精简直白改写。*
