# Deep Research — 选题清单

> 入选标准:流行叙事强、争议大、但存在可核查的一手证据——对抗验证增值最大的题目。
> 每个条目的"研究问题草案"可直接作为 deep-research workflow 的 args 起点;开跑前按当时最新进展微调。
> 流程:多 agent 并行调研一手来源 → 关键论断 3 票对抗验证 → 易读版 + 深入版 × 中英,`build.py` 渲染发布。
> **钩子收割**:每期发布后提炼 ≤5 个钩子(超出本篇范围的支线问题):适合 deep research 的进本文件「候选池」,适合某个 Second Brain routine 站的按该站 TOPICS 格式追加到其 backlog(单独 commit,行尾标「钩子·源自 #N」),并在本文件该期「已发布」条目下记录去向。

## 已发布

### 0. 传统软件组织的 AI-native 转型 ✅ 2026-07
- 页面:`ai-native-plain/-deep` × zh/en
- 底座:86 来源、166 票对抗验证;研究材料存本地 `~/design/ai-native-article/research/`
- 钩子:→ system-design Day 41《当故障快于人类反应》(2026-07,反哺);→ AI code review 已升级为待研究 #2

### 1. "初级工程师正在消失"是真的吗? ✅ 2026-07
- 页面:`junior-engineers-plain/-deep` × zh/en
- 底座:7 条调研线索、103 论断、15 条承重论断 × 3 票对抗验证(13 HOLDS / 2 修正 / 0 推翻);研究材料存本地 `~/design/deep-research-runs/junior-engineers/`
- 钩子:→ super-individual Day 53《用 AI 学习的护栏工程》(2026-07,反哺)

### 2. AI code review:验证瓶颈的解药,还是套娃? ✅ 2026-07
- 页面:`ai-code-review-plain/-deep` × zh/en
- 底座:7 条调研线索、15 条承重论断 × 3 票对抗验证(9 HOLDS / 6 修正 / 0 推翻),另沿用 #0 已验证的 6 组口径(METR、Sonar、Google 迁移、DORA、Faros 2025、Anthropic 会话);研究材料存本地 `~/design/deep-research-runs/ai-code-review/`
- 核心修正记录:Sonar 96/48 实为"信任 vs 检查行为"口径(非语法/功能正确性);SAGA 32.58% 是合成测试套件 VAcc 且为最优方法成绩;CriticGPT 人机团队增益=降幻觉而非超越模型查全率;pr-review-bench 作者任职 Sentry(COI)
- 钩子:→ system-design Day 50《把 Code Review 当信号检测系统》(2026-07,反哺);→ ai-ml Day 54《LLM-as-Judge 的偏差与校准》(2026-07,反哺);→ 候选池 2 条(scalable oversight 地基体检、AI 基准 Goodhart 化);另 1 条仅记运行报告(AI code review RCT 设计要点)

### 3. Scalable oversight 的地基体检:"验证比生成容易"是被证实的假设,还是路线信仰? ✅ 2026-07
- 页面:`scalable-oversight-plain/-deep` × zh/en
- 底座:6 条调研线、112 论断、20 条承重论断 × 3 票对抗验证(20 HOLDS / 0 推翻,30+ 处口径修正);复用 #2 验证者可靠性文献;研究材料存本地 `~/design/deep-research-runs/scalable-oversight/`
- 核心口径记录:prover-estimator 的 stability 只撑完备性(soundness 不依赖);Lu et al. 为 ICLR 2026 workshop 非主会;Anthropic 25%/39% 为提示复述率;AlphaProof 银牌为与 AlphaGeometry 2 组合成绩;Bowman 自限对象是其对话式基线
- 钩子:→ ai-ml《CoT 监控与可监控性》(backlog,反哺);→ super-individual《给自己的 AI 工作流做 oracle 盘点》(backlog,反哺);→ 候选池 1 条(形式化方法的 LLM 复兴);另 1 条仅记运行报告(NSO 复现与 stability 实证检验设计)

### 4. 学习科学的证据等级:哪些方法真的有效? ✅ 2026-07
- 页面:`learning-science-plain/-deep` × zh/en
- 底座:6 条调研线、106 论断、24 组承重论断 × 3 票对抗验证(72 票:24/24 挺过、0 推翻,15 组含修正票、30+ 处口径修正);研究材料存本地 `~/design/deep-research-runs/learning-science/`
- 核心口径记录:Macnamara 2014 有 2018 正式勘误(12%→14%,分域 24/23/20/5/1)——头条数字是勘误前的;Latimier g=0.74 系 trim-and-fill 校正值(未校正 1.01,间隔化子集仅 11 项研究);Ericsson & Harwell 29%=未校正、61%=衰减校正(信度假设 0.6/0.8);M&M 2019 双盲=实验者+被试(非编码者),practice alone=独自练习;Yang 2021 对精细加工策略 0.095 不显著;Nancekivell 93.7% 为排除前 383 人口径;准教师 vs 在职信念差异不显著;Martella"0 篇全控制"=计入实施保真度口径;Cepeda 2008 正式版为 20-40%→5-10%
- 钩子:→ 候选池 1 条(神经神话传播动力学);→ super-individual《把三个已验证开关装进自己的学习流程》(backlog,反哺);→ meta-knowledge《学习≠表现:元认知错觉》(backlog,反哺);另 1 条仅记运行报告(Kraft 基准商榷线 + Dunlosky 评级无十年更新的跟踪信号)

## 待研究

### 5. 机器 Oracle 全景:业界公认的裁判有哪些,LLM 分别能把它们做大多少?
- **一句话**:按公认分类法盘点软件验证的全部 oracle 家族,逐格核查"LLM 增益"的正反证据——检验一条可证伪的脊柱主张:裁判越独立,LLM 越是纯赚;裁判由 LLM 自己定义时,声称的增益在独立复测中系统性缩水。
- **为什么适合**:#0/#2/#3 验证瓶颈三部曲的"建设篇"——前三篇说瓶颈在验证、AI 当裁判不可靠、"验证更容易"分任务族,本篇回答"那怎么把可信的机器裁判做大";形状是评估式综述(合法变体,参照系统综述),每格自带正反张力,可跑对抗验证。范围**限定在软件/代码 oracle**,不扩到 ML 评测 oracle。
- **理论底座(锚定权威分类法,防"所有"承诺兜不住)**:Barr, Harman, McMinn, Shahbaz & Yoo,《The Oracle Problem in Software Testing》(IEEE TSE 2015)的四分类(specified / derived / implicit / human oracles)作组织骨架;metamorphic testing(Chen et al.)、差分测试(McKeeman;csmith/SQLancer 谱系)、mutation testing(DeMillo/Offutt)、property-based testing(Claessen & Hughes QuickCheck)、不变量挖掘(Ernst, Daikon)、形式验证工业谱系(Newcombe CACM 2015;seL4;CompCert)。
- **脊柱主张(可证伪版,含指标定义——防可测性偏差的循环)**:每格的"LLM 增益"必须用该格自己的独立指标事先定义——测试格=mutation-kill 增量;fuzzing 格=独立 crash/新覆盖产出率;定理证明格=验证器判定的证明完成率;静态分析格=经人工裁决的真阳性率;生产格=escaped-defect 变化。主张:在裁判独立的格子,LLM 增益有受控/生产级数字;在裁判由 LLM 定义或裁决的格子,声称的增益在独立复测中缩水。**必须主动找反例**:有没有 LLM 起草规约/property 经独立校验后抓到真 bug 的一手案例(Meta ACH?、autoformalization 落地案例)——反例足够多则软化脊柱为条件式。
- **必查格子(对照 Barr 分类逐格覆盖,loop-until-dry 补漏)**:形式验证/定理证明(TLA+、Lean/AlphaProof、autoformalization 及其基准污染问题);fuzzing+sanitizers(OSS-Fuzz 的 LLM fuzz-driver 一手数据;裁判=崩溃/ASan/TSan,独立性最强格);差分/变形测试(csmith、SQLancer;LLM 提议 metamorphic relations 的实证);property-based testing(LLM 推断不变量、Daikon 谱系;同义反复 property 的发生率);静态分析/类型(CodeQL/Semgrep 规则生成、误报分诊——注意分诊即 AI-judge,接 #2);测试+mutation(元 oracle;LLM 生成测试经 mutation 闸的通过率一手数字);运行时验证/生产断言(金丝雀作 oracle,接 #3 第三轴);并发检测器(TSan/race detector 作 implicit oracle)。
- **关键争议/正反**:正方——OSS-Fuzz LLM 报告、AlphaProof/Lean、verifier-grounded RL 的训练收益;反方——同义反复 property/测试(接 #2 弱测试污染)、autoformalization 的"规约规定错了东西"(接 #3 规格-意图鸿沟)、LLM 生成规则的误报洪水、以及"增益只在可测处可见"的可测性偏差本身。
- **实证锚点**:Barr et al. TSE 2015;Google OSS-Fuzz LLM 博客/论文;AlphaProof (Nature 2025,承 #3 已验证口径);Newcombe CACM 2015(承 #0);Meta 自动化合规/测试工作(ACH 等,需核);SQLancer/csmith 原文;QuickCheck/Hypothesis;Daikon;#2/#3 已验证的验证者可靠性文献全部复用。
- **注意**:承 #2/#3 大量文献,增量必须在"每格的 LLM 增益实证"层,不复写"AI 当裁判不可靠"的结论;完整性用 Barr 分类逐格核对并做 loop-until-dry;每格指标不同,跨格不许直接比大小(各基线不同);"所有 oracle"表述收敛为"按公认分类法逐格覆盖的主要家族+显式纳入标准"。

### 6. 屏幕时间与青少年心理健康:Haidt 对不对?
- **一句话**:《焦虑的一代》的因果主张,经得起方法学检验吗?
- **为什么适合**:当下争议最激烈、双方都有重量级学者的题目,对抗验证格式的完美展示品;贴育儿站。
- **理论底座**:媒介效应研究方法学(相关 vs 因果)、displacement hypothesis、社会比较理论、Granovetter 式集体动力学(Haidt 的"集体行动问题"框架)。
- **关键争议/正反**:Haidt/Twenge 的时序与剂量论证 vs Odgers/Przybylski 的方法学批评(效应量≈"吃土豆"、specification curve 分析)、自然实验证据(社交媒体接入的准实验)、各国青少年心理指标趋势是否同步。
- **实证锚点**:Haidt 的公开协作文档(与批评者的逐条对账)、meta 分析效应量、英美挪威等国队列数据。

### 7. 长寿干预的证据分级
- **一句话**:雷帕霉素、二甲双胍、NAD+、禁食——把炒作与证据的落差量化出来。
- **为什么适合**:炒作密度最高的领域,厂商/网红口径 vs 独立复现的落差极大;"厂商口径"标注体系可直接复用;贴 health-longevity 站。
- **理论底座**:衰老机制理论(hallmarks of aging)、mTOR/AMPK 通路、热量限制文献谱系、证据医学分级(动物模型→观察性→RCT)。
- **关键争议/正反**:ITP(NIA 干预测试计划,金标准动物数据)哪些过了哪些没过;二甲双胍 UKPDS/TAME 之争与 2024 前后的观察性研究翻转;NAD+ 补剂人体证据薄弱 vs 市场规模;禁食/限时进食 RCT(TREAT 等)与体重外结局。
- **实证锚点**:ITP 官方结果、ClinicalTrials 注册与发表偏倚核查、补剂厂商宣称 vs 试验原文。
- **注意**:通篇需挂"非医疗建议"免责声明;人体证据与动物证据严格分档。

### 8. 指数化的终局:被动投资会破坏市场吗?
- **一句话**:被动占比过半后,"指数泡沫论"有没有实证支撑?
- **为什么适合**:Michael Green/David Einhorn 的警告流传很广但很少被逐条核查;SPIVA 数据一边倒 vs 结构性风险论,正反阵营清晰;贴 investing 站。
- **理论底座**:Grossman-Stiglitz 悖论(有效市场的信息成本内生矛盾)、价格发现与流动性提供、指数纳入效应文献、所有权集中(common ownership)反垄断争论。
- **关键争议/正反**:主动管理长期跑输(SPIVA/Morningstar Active-Passive Barometer)vs"被动扭曲定价"的实证(指数纳入溢价的衰减研究、大小盘相关性变化);"被动导致波动放大"的证据与反驳;三巨头投票权集中的治理研究。
- **实证锚点**:SPIVA 年度报告、Sammon/Coles 等价格信息含量研究、指数纳入效应 meta。

### 9. 这轮 AI 资本开支是不是 1999?
- **一句话**:用铁路/电信/光纤泡沫的资本周期理论,给当前 AI capex 做体检。
- **为什么适合**:与第 0 篇互补(组织视角 → 资本视角);历史对照有丰富的定量文献,当前数据全部公开可查;多空双方都在大声说话。
- **理论底座**:资本周期理论(Marathon/Chancellor)、技术革命与金融资本(Perez 的 installation/deployment 框架)、Minsky 金融不稳定假说、通用技术(GPT)扩散经济学。
- **关键争议/正反**:"收入缺口"论(capex vs AI 收入的缺口测算,Sequoia/经济学人口径差异)vs"算力稀缺是真需求"论;1999 光纤过剩的利用率数据 vs 当前 GPU 利用率;折旧周期(GPU 3-5 年 vs 光纤 20 年)对泡沫类比的破坏力;头部公司现金流自给 vs 1999 债务融资的结构差异。
- **实证锚点**:四大云厂商 capex 与 AI 收入披露、Perez 框架的既有学术检验、1999-2002 电信 capex/利用率史料、GPU 转售/租赁市场价格。

### 10. Scaling laws 撞墙了吗?
- **一句话**:预训练收益递减是实测事实还是融资叙事?"数据墙"与推理时代的证据体检。
- **为什么适合**:厂商话术密度极高、每季度风向反转的话题,恰好需要对抗验证分离"实测曲线"和"叙事";一手材料(论文+基准)全部公开。
- **理论底座**:神经网络缩放律谱系(Kaplan 2020 → Chinchilla/Hoffmann 2022 的算力最优修正)、test-time compute 缩放(o1/R1 谱系)、数据约束模型(Villalobos et al. "Will we run out of data")、算法效率增益的独立测量(Epoch AI)。
- **关键争议/正反**:"撞墙"报道(2024 底 Orion/Gemini 传闻、Ilya "预训练时代终结"发言)vs 后续旗舰模型的实测跃升;基准饱和 vs 基准污染(评测本身失效的问题);合成数据是解药还是模型坍缩(model collapse 文献两边);推理缩放的成本曲线是否可持续。
- **实证锚点**:Epoch AI 的算力/效率/数据存量测算、Chinchilla 原文与复现、主要基准(MMLU→FrontierMath/ARC-AGI 等)的时序成绩、厂商技术报告 vs 独立评测的口径差。
- **注意**:变化极快,开跑前先刷新到当月;成文时明确标注"截至 X 年 X 月"。

## 候选池(未排期)

- 神经神话为什么杀不死:学习风格、多元智能、左右脑的传播动力学——师训体系为何成为误念的主要传染源,揭穿式干预的实效边界(信念降 37% 但行为传导仅半)(钩子·源自 #4)
- ~~形式化方法的 LLM 复兴~~(已折叠进待研究 #10 作为其中一格)(钩子·源自 #3)
- Agent 协议标准化会不会重演 TCP/IP 沙漏(第 0 篇 Headless Firm 线的深挖)
- AI 基准的 Goodhart 化:数据污染、榜单收割与评测激励结构,为什么评测体系一建成就失效(可与 #8 scaling laws 的基准饱和线互补)(钩子·源自 #2)
- HRT 的兴衰与再评价(WHI 研究如何被重新解读——"证据翻转"经典案例)
- AI 时代该让孩子学什么(编程还值得学吗)
