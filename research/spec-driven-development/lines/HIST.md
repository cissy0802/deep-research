# HIST · 历史前科考古(Round 1)

34 条论断,来自 23 个独立一手来源。可信度分布:verbatim-checked 18、paraphrase-checked 6、secondhand 10。
**运行约束**:本会话 WebFetch 对 wikipedia/leanpub/arXiv/ACM/IEEE/umd 等全部 DNS 拦截。一手文本只能通过 GitHub(git clone 公共仓库里的 PDF/转录)和 WebSearch 摘要拿到。凡没读到原件的条目都已标 secondhand,验证阶段应优先补这些。

## 1. Royce 1970:原文到底说了什么(最强证据块)
- 一手 PDF 取自 tpn/pdfs(sha 9f7db065…)。用 pdftotext 抽文本,再对照页面图像核对;与 tamnd/papers 的 olmOCR 转录(同一 sha)一致。
- **两句都在原文,成文必须并引**:
  - Fig.2 正下方:"I believe in this concept, but the implementation described above is risky and invites failure."(H01)
  - 同页:"However, I believe the illustrated approach to be fundamentally sound."(H02)。全文是在这个"基本方法"上**追加**五步修正。
- 流行叙事"Royce 反对瀑布"只对一半。他反对的是不加修正的单趟实施,方向是**更重的前置设计和文档**:
  - "ruthless enforcement of documentation requirements"
  - 文档不合格就"Replace project management"
  - "the documentation **is** the specification and **is** the design"(H04)
  - 外加一次试点("do it twice",30 个月项目里安排 10 个月,H06)和客户正式介入。
- **与 SDD 同构最强的一点**:Royce 认为编码"managed with relative ease",难点在两头(H07)。"代码便宜、规约贵"并不是 LLM 时代的新命题。SDD 要证明的是:这次的机制哪里不同。
- 口径陷阱:
  - 规约页数在原件上残损,"1?00 page",可能是 1000 也可能是 1500(H05),不得单点引用 1500。
  - "100-percent overrun"是经验判断,没有数据。
- "waterfall"一词在原文中出现 0 次(H08,两种抽取方式结果一致)。

## 2. "瀑布"一词与误读史
- 已知最早的印刷用例归于 Bell & Thayer 1976(同属 TRW):"he introduced the concept of the 'waterfall'"(H09)。
  - 他们引用 Royce 是为"top-down 优于 bottom-up"背书。被冠以"瀑布"的图,正是 Royce 自己说会招致失败的 Fig.2。
  - 一手 PDF 没读到,依据是两份独立转录逐字一致。
  - 只能说"已知最早",不能说"创造"。
- Larman & Basili 2003(H10)两面都要看:
  - 引 Walker Royce 的私人通信("always a proponent of iterative…"),这是亲属事后转述,属弱证据。
  - 同文也承认 Royce 的方案"clearly not classic IID"。
  - Larman 是敏捷推广者,立场相关。
- 未入表(仅二手):Benington 1956/1983 前言提到先做原型;DOD-STD-2167(1985)把顺序流程制度化,MIL-STD-498(1994)又松绑。

## 3. 同时代反思:spec 先行的边界(专家论述,非测量)
- Brooks 1986(H11–H14):
  - "hardest single part … deciding precisely what to build"。
  - "specify a satisfactory system in advance"这一采购假设"fundamentally wrong"。
  - 自动编程被期待了约 40 年,引 Parnas:"a euphemism for programming with a higher-level language"(H12,直接对位"specs are the new code")。
  - "much of the essence of building a program is in fact the debugging of the specification"(H13,连接 FORMAL 线)。
  - 流程图是"after, not before"画的(H14)。
- Parnas & Clements 1986(H15–H16):
  - 理性设计过程永远找不到,"we can fake it":spec 是事后整理出来的理性化表述。
  - 文档"expensive to maintain and, in most cases, will not be maintained"。这是 spec 漂移在 40 年前的机制描述。
- Dijkstra EWD667(H17):自然语言的"naturalness"等于"statements the nonsense of which is not obvious";窄接口和形式符号是一种"privilege"。是 T1 自然语言 spec 的反方历史论据,转录本为二手。
- **分级提醒**:以上都是"评论",不得与实验数据同级承重。

## 4. Boehm 缺陷修复成本曲线与 Bossavit 溯源
- Boehm 1981 曲线(H18,经 Menzies 等重绘和综述;原书未读):
  - 数据来自 1970 年代后期的大型系统(IBM / TRW / GTE / SAFEGUARD)。
  - "data points … not published";成本单位是工时还是费用,不明。
  - 同图的"较小项目"虚线明显平坦,约 4–5 倍,对比大项目运行阶段约 100 倍以上。
- Boehm & Basili 2001 自己设了限定(H19):"**often** 100 times",对小型非关键系统"more like 5:1 than 100:1"。流行转述几乎都丢掉了这两处限定。
- Bossavit gist(H20,一手):
  - Pressman 版"1:6.5:15:60-100"出自"IBM Systems Sciences Institute"。那是 IBM 内部培训单位,不是研究机构。
  - 原始数据不晚于 1981 年,可能早至 1967 年。
  - 这条出处链与 Boehm 曲线是两条,不得合并。
- Menzies 等 2017(H21–H22,作者 LaTeX 源):
  - 171 个 TSP 项目里未发现延迟问题效应。
  - **局限**:中位工期 46 天,修复工时由开发者自记,数据来自 SEI 推广的 TSP(作者有利益关联)。
  - 与 Boehm 的大项目口径不重叠,不等于"推翻 Boehm"。
  - 综述显示几乎所有引用都追到 Boehm 1981;Toshiba 1:137、IBM 1:117 没有原始数据。
- 对 SDD 的含义:"越早发现越便宜"作为 spec 先行的经济学论据,**只在大型/长周期/高仪式项目上有(老)数据**。在短迭代、agent 秒级重生成的语境下,迁移证据为零。

## 5. MDA / UML / CASE:上一代"模型即源"的采用记录
- Petre 2013(H23–H24,pdfx 全文):
  - 50 家公司 50 名开发者的声明使用:无 UML 35、选择性 11、代码生成 3、事后补画 1、全面采用 0。
  - 不采用的理由包括"synchronization … between models and code"。
- Hutchinson 2011(H25):
  - 文献宣称生产率 +20%~+800%,比较研究只有 +35%~−27%。
  - 拖累因素明确包括"the need to keep models/code in sync"。
- Whittle 2014(H26):
  - 样本为 450 名实践者加 22 人访谈。
  - 很少用 MDE 生成整个系统,主要靠 DSL 生成关键部分;多数公司约 20–30% 增益,不足以驱动采用。
  - 代码生成是"red herring";单一案例中认证成本升至 8 倍;社会和组织因素主导。
  - **分母陷阱**:样本全是 MDE 实践者,有幸存者偏差。
- OMG MDA Guide 2003(H27,厂商/联盟口径,二手):PIM "contains enough information to drive" PSM。这是 Tessl "spec-as-source" 的直接前代。
- Kemerer 1992 CASE(H28):流行的"70% 从未使用"数字未能定位一手,按未验证处理,不承重。

## 6. BDD / Cucumber(T4 可执行规约的维护成本)
- Binamungu 2018(H29,一手 PDF):
  - 75 名实践者:20% 所在组织强制使用,61% 作为可选工具。
  - 61% 认为重复会让规约难以修改,可能导致功能"frozen"。
  - "放弃 BDD、回到技术测试"只是**轶事**,没有比例。
- Hellesøy(H30,工具作者、厂商口径,只有摘要):Cucumber 被当成测试工具误用,导致 Rails 团队弃用。
- Zampetti 2020(H31,只有摘要):框架常被挪作单元测试用;共同演化的具体比例未核。

## 7. TDD 证据方向
- Nagappan 2008(H32,一手 PDF):
  - 发布前缺陷密度下降 40–90%;开发时间增加 15–35% 是"Management estimates"。
  - 4 对比较,非随机;作者研究的是自家公司团队。
- 元分析方向(H33,一手全被拦截,多源逐字一致):
  - Rafique & Mišić 2013:质量小幅正效应,生产率几乎无效应,工业研究中两者都更大。
  - Bissi 2016:76% / 88% 是"报告改进的研究占比"(计票),不是效应量。
  - Fucci 2017:**写测试与写代码的先后顺序没有重要影响**,粒度和节奏才重要。迁移到 SDD("spec 先行"的顺序是否是有效成分)只能作类比假设。

## 8. 文学编程
- Knuth 1984 原句(H34,多源一致)。没有搜到采用率的系统调查;Jupyter 后代的研究只看到摘要,未入表。

## 最强 / 最弱
- **最强**:
  - H01/H02/H04:Royce 原文,一手 PDF + 页面图像核对。
  - H23/H26:Petre、Whittle 全文计数。
  - H20/H21:Bossavit 一手 gist,Menzies 作者源文件。
- **最弱**:
  - H28:Kemerer 70%,未定位一手。
  - H30/H31:Hellesøy、Zampetti,只有摘要。
  - H27:MDA Guide,二手且为联盟口径。
- **未搜到的关键角度**:
  - Leprechauns 书本体;Boehm 1981 原书;Bell & Thayer 一手。
  - 早于 1976 的"waterfall"用例。
  - CASE/MDA 衰落的独立市场数据;BDD 弃用率的定量数据;文学编程采用率。
