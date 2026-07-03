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

## 待研究

### 3. 学习科学的证据等级:哪些方法真的有效?
- **一句话**:间隔重复、检索练习、刻意练习、主动学习——按证据强度重新排座次。
- **为什么适合**:教科书级学术对战("一万小时"神话 vs Macnamara meta 分析 vs Ericsson 回应);结论能直接反哺全部学习站的内容设计。
- **理论底座**:认知负荷理论(Sweller)、检索练习效应(Roediger & Karpicke)、间隔效应(Ebbinghaus→Cepeda meta)、刻意练习(Ericsson 1993)、desirable difficulties(Bjork)。
- **关键争议/正反**:刻意练习解释力(Macnamara et al. 2014/2016 meta:体育/音乐/教育中方差解释远低于宣称)、学习风格神话(已被反复证伪但仍流行)、主动学习 vs 讲授的实证(Freeman 2014 meta 及其批评)。
- **实证锚点**:各效应的 meta 分析效应量、预注册复现研究、Dunlosky et al. 2013 十大学习技巧评级。

### 4. 屏幕时间与青少年心理健康:Haidt 对不对?
- **一句话**:《焦虑的一代》的因果主张,经得起方法学检验吗?
- **为什么适合**:当下争议最激烈、双方都有重量级学者的题目,对抗验证格式的完美展示品;贴育儿站。
- **理论底座**:媒介效应研究方法学(相关 vs 因果)、displacement hypothesis、社会比较理论、Granovetter 式集体动力学(Haidt 的"集体行动问题"框架)。
- **关键争议/正反**:Haidt/Twenge 的时序与剂量论证 vs Odgers/Przybylski 的方法学批评(效应量≈"吃土豆"、specification curve 分析)、自然实验证据(社交媒体接入的准实验)、各国青少年心理指标趋势是否同步。
- **实证锚点**:Haidt 的公开协作文档(与批评者的逐条对账)、meta 分析效应量、英美挪威等国队列数据。

### 5. 长寿干预的证据分级
- **一句话**:雷帕霉素、二甲双胍、NAD+、禁食——把炒作与证据的落差量化出来。
- **为什么适合**:炒作密度最高的领域,厂商/网红口径 vs 独立复现的落差极大;"厂商口径"标注体系可直接复用;贴 health-longevity 站。
- **理论底座**:衰老机制理论(hallmarks of aging)、mTOR/AMPK 通路、热量限制文献谱系、证据医学分级(动物模型→观察性→RCT)。
- **关键争议/正反**:ITP(NIA 干预测试计划,金标准动物数据)哪些过了哪些没过;二甲双胍 UKPDS/TAME 之争与 2024 前后的观察性研究翻转;NAD+ 补剂人体证据薄弱 vs 市场规模;禁食/限时进食 RCT(TREAT 等)与体重外结局。
- **实证锚点**:ITP 官方结果、ClinicalTrials 注册与发表偏倚核查、补剂厂商宣称 vs 试验原文。
- **注意**:通篇需挂"非医疗建议"免责声明;人体证据与动物证据严格分档。

### 6. 指数化的终局:被动投资会破坏市场吗?
- **一句话**:被动占比过半后,"指数泡沫论"有没有实证支撑?
- **为什么适合**:Michael Green/David Einhorn 的警告流传很广但很少被逐条核查;SPIVA 数据一边倒 vs 结构性风险论,正反阵营清晰;贴 investing 站。
- **理论底座**:Grossman-Stiglitz 悖论(有效市场的信息成本内生矛盾)、价格发现与流动性提供、指数纳入效应文献、所有权集中(common ownership)反垄断争论。
- **关键争议/正反**:主动管理长期跑输(SPIVA/Morningstar Active-Passive Barometer)vs"被动扭曲定价"的实证(指数纳入溢价的衰减研究、大小盘相关性变化);"被动导致波动放大"的证据与反驳;三巨头投票权集中的治理研究。
- **实证锚点**:SPIVA 年度报告、Sammon/Coles 等价格信息含量研究、指数纳入效应 meta。

### 7. 这轮 AI 资本开支是不是 1999?
- **一句话**:用铁路/电信/光纤泡沫的资本周期理论,给当前 AI capex 做体检。
- **为什么适合**:与第 0 篇互补(组织视角 → 资本视角);历史对照有丰富的定量文献,当前数据全部公开可查;多空双方都在大声说话。
- **理论底座**:资本周期理论(Marathon/Chancellor)、技术革命与金融资本(Perez 的 installation/deployment 框架)、Minsky 金融不稳定假说、通用技术(GPT)扩散经济学。
- **关键争议/正反**:"收入缺口"论(capex vs AI 收入的缺口测算,Sequoia/经济学人口径差异)vs"算力稀缺是真需求"论;1999 光纤过剩的利用率数据 vs 当前 GPU 利用率;折旧周期(GPU 3-5 年 vs 光纤 20 年)对泡沫类比的破坏力;头部公司现金流自给 vs 1999 债务融资的结构差异。
- **实证锚点**:四大云厂商 capex 与 AI 收入披露、Perez 框架的既有学术检验、1999-2002 电信 capex/利用率史料、GPU 转售/租赁市场价格。

### 8. Scaling laws 撞墙了吗?
- **一句话**:预训练收益递减是实测事实还是融资叙事?"数据墙"与推理时代的证据体检。
- **为什么适合**:厂商话术密度极高、每季度风向反转的话题,恰好需要对抗验证分离"实测曲线"和"叙事";一手材料(论文+基准)全部公开。
- **理论底座**:神经网络缩放律谱系(Kaplan 2020 → Chinchilla/Hoffmann 2022 的算力最优修正)、test-time compute 缩放(o1/R1 谱系)、数据约束模型(Villalobos et al. "Will we run out of data")、算法效率增益的独立测量(Epoch AI)。
- **关键争议/正反**:"撞墙"报道(2024 底 Orion/Gemini 传闻、Ilya "预训练时代终结"发言)vs 后续旗舰模型的实测跃升;基准饱和 vs 基准污染(评测本身失效的问题);合成数据是解药还是模型坍缩(model collapse 文献两边);推理缩放的成本曲线是否可持续。
- **实证锚点**:Epoch AI 的算力/效率/数据存量测算、Chinchilla 原文与复现、主要基准(MMLU→FrontierMath/ARC-AGI 等)的时序成绩、厂商技术报告 vs 独立评测的口径差。
- **注意**:变化极快,开跑前先刷新到当月;成文时明确标注"截至 X 年 X 月"。

## 候选池(未排期)

- Agent 协议标准化会不会重演 TCP/IP 沙漏(第 0 篇 Headless Firm 线的深挖)
- HRT 的兴衰与再评价(WHI 研究如何被重新解读——"证据翻转"经典案例)
- AI 时代该让孩子学什么(编程还值得学吗)
