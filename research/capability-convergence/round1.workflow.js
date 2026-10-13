export const meta = {
  name: 'convergence-round1',
  description: 'Round 1: AI 能力趋同 6 条调研线并行收集一手来源与论断',
  phases: [{ title: 'Research', detail: '6 条调研线并行' }],
}

const DIR = '/Users/cissychen/Desktop/repos/deep-research/research/capability-convergence/lines'

const SCHEMA = {
  type: 'object',
  required: ['line', 'claims', 'caliber_issues', 'summary'],
  properties: {
    line: { type: 'string' },
    summary: { type: 'string', description: '本线发现的 5-10 句要点(中文)' },
    claims: {
      type: 'array',
      items: {
        type: 'object',
        required: ['id', 'claim', 'source_url', 'source_type', 'loadbearing'],
        properties: {
          id: { type: 'string' },
          claim: { type: 'string', description: '论断(中文),数字带口径:哪个基准/版本、哪些模型、时间点、分差还是比值、置信区间' },
          quote: { type: 'string', description: '一手原文逐字摘引(英文原文)' },
          source_url: { type: 'string' },
          source_type: { type: 'string', description: '同行评审|官方/一手(论文、官方报告、官方榜单)|厂商自报|从业者博客|媒体转述|分析机构' },
          date: { type: 'string' },
          loadbearing: { type: 'boolean', description: '是否可能承重(错了会影响"能力是在趋同还是分化"的判断)' },
          side: { type: 'string', description: '支持哪种叙事:趋同/商品化|测量伪影|长任务分化/赢家通吃|中性' },
        },
      },
    },
    caliber_issues: { type: 'array', items: { type: 'string' }, description: '交叉口径问题清单(供验证阶段)' },
  },
}

const HEAD = `你是深度研究调研员。研究总题:「AI 能力最终会趋同是真的吗?」——排行榜上头部模型越挤越近、开源与闭源差距看似只剩几个百分点,这是能力真的在趋同,还是旧考卷饱和造成的测量错觉?在长任务与可靠性这类不饱和的维度上,头部与第二梯队差距是在收窄还是拉大?今天是 2026-10-12,成文标「截至 2026 年 10 月」,必须刷新到最新(2026 年 8-10 月)数据。

「差距」有三种可检验定义,必须分清:(1) 分差:同一基准同一时点头部与追赶者的分数差(含置信区间);(2) 追平月数:追赶者达到前沿某一水平所需月数;(3) 比值:如长任务 time horizon 之比、完成率之比。三者可能给出相反方向。另须区分「用户感知饱和」(日常任务分不出)与「能力饱和」。

已知刷新线索(均待核,你负责回一手):Epoch 2026-05-29 称 2026-01 以来最强开源落后闭源约 4 个月/8 ECI 点、此前约 3 个月;媒体称 Arena 2026-09 闭源 vs 开源差距扩大到 29 Elo;METR TH1.1(2026-01)与 2026-03-20 笔记称任务集饱和使结果对建模选择敏感;第三方称 Claude Mythos Preview 50% time horizon 约 17 小时。

工作要求:
- 用 WebSearch/WebFetch 找**一手来源**(论文原文/arXiv、官方报告 PDF、官方榜单与数据下载、官方博客),逐字摘引原文。WebFetch 的摘要模型可能编造引语与数字——关键数字让它逐字引用;能直接下载数据(CSV/JSON,如 Epoch 数据、METR GitHub、Arena 数据)就用 Bash curl 抓原始数据自己算,并在论断里写明自算方法。
- 来源分级:同行评审 / 官方一手 / 厂商自报 / 从业者博客 / 媒体转述 / 分析机构。厂商自报基准分标「厂商口径」,优先独立复测。
- 正反证据都要收,尤其是与你这条线主流叙事相反的。
- 目标约 25-40 条论断,宁精勿滥;每条带 URL 与日期。
- **随时落盘**:边调研边把论断与引文写到 ${DIR}/<你的线 key>.md(Write 工具),结束前确保文件完整。最终输出结构化数据。

你负责的调研线:
`

const LINES = [
  { key: 'T-theory', body: `【T 理论与数学】独占产出:原典逐字 + 数学推导。
- 天花板效应与基准饱和的测量学:心理测量中的 ceiling effect;IRT(项目反应理论)视角下高分段区分度丧失;Ott et al. 2022 Nature Communications "Mapping global dynamics of benchmark creation and saturation in AI";Kiela et al. 2021 Dynabench "benchmarks saturate";Epoch/其他对基准饱和速度加快的测量(如从发布到饱和的年数缩短)。
- 可靠性复合:单步成功率 p 在 n 步任务上为 p^n(0.95^50≈7.7%, 0.99^50≈60.5%,自己验算);其批评——步骤错误不独立、可自我纠错、长任务非简单串联。Toby Ord 2025「Is there a half-life for the success rates of AI agents?」(恒定风险率模型、半衰期)原文;METR Kwa et al. 2025「Measuring AI Ability to Complete Long Tasks」中关于 logistic 拟合与 50%/80% 时长关系的表述。推论:分差小的模型在长任务上比值可能很大——找原文或实证支撑,也找反例。
- Elo/Bradley-Terry 的统计性质:分差压缩、置信区间、Elo 差与胜率的映射(如 30 Elo ≈ 54% 胜率,自己算),非传递性;为什么排行榜顶部"挤"不等于能力相等。
- 技术扩散与追赶:模仿成本低于创新成本(Mansfield 1981 模仿成本约为创新成本 65%、时间 70% 一类经典实证)、知识溢出;后发优势;S 曲线接力(预训练→RL/推理时计算→agent)。
- 反方理论:规模经济/学习效应/数据飞轮导致发散(收益递增,Arthur 1989/1994)。` },
  { key: 'ARENA-leaderboards', body: `【ARENA 偏好排行榜】独占产出:Arena(原 LMArena/Chatbot Arena)数据与对其的批评。
- Arena 文本总榜头部分差时序:例如 2024、2025、2026 各时点第 1 名与第 10 名 Elo 差、前 3 名差、置信区间是否重叠;最新(2026-09/10)头部格局。官方数据或 Hugging Face 上的 leaderboard 数据集若可下载就自己算。
- 闭源前沿 vs 最强开源 Elo 差的时序(媒体称 2026-09 扩大到 29 Elo——找 Arena 官方出处与原话);中美模型差。
- Singh et al. 2025「The Leaderboard Illusion」(arXiv 2504.20879):私下测试多变体只公布最好的、采样不均、数据访问不对称——逐字摘引关键数字(如 Meta 测试 27 个私有变体);Arena 方回应。
- 风格控制(style control):长度/markdown 对排名的影响,开风格控制前后排名变化;"用户偏好 ≠ 能力"的证据;用户感知饱和——日常提示上头部模型胜率接近 50%。
- Arena 在困难类目(编程、数学、hard prompts、WebDev Arena、Search Arena 等)上的分差是否比总榜大。
- 反方:Arena 与其他能力基准的相关性证据。` },
  { key: 'BENCH-static-index', body: `【BENCH 静态基准与年度报告】独占产出:静态基准饱和时序 + Stanford AI Index 统计。
- Stanford AI Index 2025 与 2026(若已发布)关于"差距收窄"的原文统计:Arena 第 1 与第 10 名差距从 11.9% 到 5.4%、前两名 0.7%;开源 vs 闭源差距从 8.0% 到 1.7%;中美差距 MMLU/HumanEval 等;逐字回 PDF 核对数字与口径(这些是基于 Arena 的还是基于基准的)。
- 主要基准饱和时序:MMLU、GPQA Diamond、MATH、HumanEval、SWE-bench Verified(含 OpenAI 2026 年前后对 SWE-bench Verified 污染/题目缺陷的声明)、Humanity's Last Exam、FrontierMath(各 tier)、ARC-AGI-1/2/3——每个基准从发布到被头部打到 >80% 或接近人类基线的时间;最新(2026)头部分数与追赶者分数。
- 饱和基准上的分差 vs 未饱和基准上的分差:同一批模型在饱和与未饱和基准上的分布是否不同(例如在 HLE/FrontierMath Tier 4/ARC-AGI-2 上头部与第二梯队差距是否更大)——找 Epoch Benchmarking Hub、Artificial Analysis、Scale SEAL 等独立复测数据。
- 厂商更换头条基准的时点:发布博客里主打基准的迁移(MMLU→GPQA→SWE-bench→HLE/τ-bench/GDPval 等),作为"旧考卷饱和"的信号。
- Epoch Capabilities Index(ECI)作为跨基准合成指标的方法论(如何对饱和基准降权)。` },
  { key: 'HORIZON-longtask', body: `【HORIZON 长任务与可靠性】独占产出:长任务/可靠性实测数据。
- METR time horizon:Kwa et al. 2025 原论文(翻倍约 7 个月);TH1.1(2026-01)更新;各模型 50% 与 80% time horizon 最新数值(METR 官网/GitHub 数据,若可下载就自己算);METR 2026-03-20 方法学笔记逐字(任务集饱和、建模选择敏感度);METR 对 >16h 估计不可靠的警示;2026 年最新模型(Claude Mythos、GPT-5.x、Gemini 3.x、Grok、DeepSeek/Qwen/Kimi 等开源)的数值。
- 关键问题:在 time horizon 曲线上,头部与追赶者(第二家实验室、最强开源、中国模型)的差距以月计是固定、收窄还是拉大?以比值计呢?用 METR 数据自算并写明方法。METR 是否测过开源/中国模型(如 DeepSeek-R1、Kimi K2、Qwen)及其相对前沿的滞后。
- 80%/50% 比值:头部模型 80% 时长与 50% 时长的比值是否随代际改善(可靠性是否在追上能力)。
- 其他可靠性/长任务测量:τ-bench / τ²-bench 的 pass^k(k 次全成功率随 k 衰减)、Terminal-Bench 2、Vending-Bench(长期一致性崩溃)、OpenAI GDPval、RE-Bench、SWE-Lancer、METR 的开发者 RCT 以及"在真实代码库上 merge 率"类研究;各自头部与第二梯队的差距。
- 反方:长任务差距被夸大的证据(脚手架/agent harness 差异、算力预算不同、任务集偏向编程)。` },
  { key: 'CATCHUP-open-china', body: `【CATCHUP 开源与中国追赶】独占产出:追赶速度的测量。
- Epoch AI 开源 vs 闭源滞后:2025-10 Data Insight(约 3 个月)与 2026-05-29 更新(约 4 个月/8 ECI 点)原文逐字;方法(ECI、取最强模型的包络线);Epoch 对公开基准可能抬高开源的警示;更早 Epoch 2024 "open models lag ~1 year" 之类估计,观察滞后是缩短还是延长。
- DeepSeek-R1(2025-01)作为追赶标志:与 o1 的时间差与基准差;之后 DeepSeek V3.x/R2、Qwen 3.x、Kimi K2.x、GLM-5.x 等 2026 年开源的追赶情况。
- 美国 NIST CAISI 对 DeepSeek/Kimi 等中国模型的评估报告(2025-09 起)原文:在哪些任务(尤其 agent/网络安全/软件工程)上落后多少;以及其利益位置(政府机构)。
- 蒸馏:Gudibande et al. 2023「The False Promise of Imitating Proprietary LLMs」——模仿学到风格不学到能力;DeepSeek-R1 论文中的蒸馏结果;蒸馏在可验证长任务/agent 任务上是否同样有效的证据;OpenAI/Anthropic 指控蒸馏的公开声明(厂商口径)。
- 中美差距:AI Index、Epoch、Artificial Analysis 等对美中头部模型差距的时序。
- 反方:开源在长任务/agent 基准上落后更多的证据(如 METR、Terminal-Bench、SWE-bench Pro 上的开源成绩)。` },
  { key: 'LOCKIN-compute', body: `【LOCKIN 输入侧锁定】独占产出:输入侧集中度证据。
- Epoch AI:前沿训练算力增长(每年约 4-5×)、超过 10^25/10^26 FLOP 的模型数量随时间增长(扩散信号)与最大训练运行的集中(锁定信号);各家最大训练集群规模;最新(2026)数据。
- 下一代 10× 规模谁负担得起:各家 2026 capex 与算力合同(只取"负担得起前沿训练的玩家数"这一角度,不重复利润池论证);中国受出口管制约束的算力差距及其对能力差距的影响(Epoch/CSIS/其他测算)。
- RL 与推理时计算:RL 训练算力占比上升、RL 数据/环境飞轮是否形成护城河的证据(正反);推理时计算让较弱模型用更多 token 追平的证据(如 test-time compute 扩展曲线),以及它对"差距"测量的含义(同成本 vs 同模型比较)。
- 人才流动与知识扩散:前沿实验室人员流动、论文发表减少;Meta 超级智能实验室挖人等事件;知识扩散速度的测量。
- 反方:算力效率进步(算法进步每年约 3×,Epoch)让追赶者以更少算力追平;"领先者无护城河"(Google 内部备忘录 2023 "We have no moat")原文。` },
]

phase('Research')
const results = await parallel(LINES.map(l => () =>
  agent(HEAD + l.body + `\n\n你的线 key 为 ${l.key},落盘文件 ${DIR}/${l.key}.md。`, { label: l.key, phase: 'Research', schema: SCHEMA })
))
return results.filter(Boolean)
