export const meta = {
  name: 'scaling-wall-round2',
  description: 'Round 2: 44 组承重论断 × 3 票对抗验证',
  phases: [{ title: 'Verify', detail: '11 批 × 3 票独立反驳' }],
}

const SCHEMA = {
  type: 'object',
  required: ['batch', 'verdicts'],
  properties: {
    batch: { type: 'string' },
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        required: ['group', 'verdict', 'reasoning', 'corrected_statement'],
        properties: {
          group: { type: 'string' },
          verdict: { type: 'string', description: 'HOLDS | CORRECTED | REFUTED' },
          reasoning: { type: 'string', description: '你实际读到的一手内容与核对结果,含逐字引语' },
          corrected_statement: { type: 'string', description: '修正后可安全写进文章的表述(HOLDS 时重述原论断)' },
          caliber_fixes: { type: 'array', items: { type: 'string' }, description: '逐条口径修正:修正前 → 修正后' },
          primary_source_checked: { type: 'string', description: '你实际打开的一手 URL' },
          evidence_grade: { type: 'string', description: '多源证实|单源已核|方向存争|厂商口径|未验证' },
        },
      },
    },
  },
}

const HEAD = `你是对抗验证员。任务不是确认,而是**尽力反驳**——refute by default。文章题目:「Scaling laws 撞墙了吗?」(截至 2026 年 8 月)。

对每一组论断:
1. 用 WebFetch 打开一手来源逐字核对(论文原文/官方博客/发布页/访谈实录)。摘引不能凭记忆,必须实读。
2. 检查:分子/分母、时间窗、限定语、样本量、是否被后续研究或勘误修正、是否同名不同物(模型版本/基准版本/口径版本)、说话者利益位置。
3. 主动检索反证:有没有独立团队/独立数据给出矛盾结果?有没有更新的数字推翻它?
4. 判决 HOLDS(逐字核对无误、可按原强度写入)/ CORRECTED(方向对但口径须修正,给出修正后表述)/ REFUTED(核心事实站不住,不得按原强度写入)。
5. 宁可判 CORRECTED 也不要放过口径滑坡。找不到一手来源的引语判 REFUTED 或降级为【未验证】。
6. 证据分级:多源证实(≥2 独立来源同向)/ 单源已核(一手可回溯)/ 方向存争(独立来源矛盾)/ 厂商口径(利益相关方自述)/ 未验证。

你的最终输出是结构化判决数据,不是给人看的文章。以下是你这批要验证的组:

`

const BATCHES = [
  { key: 'B1-theory', body: `
【G1】Kaplan et al. 2020 (arXiv 2001.08361) 的原始口径:(a) 幂律针对的是 WebText2 交叉熵 test loss 而非下游能力,"trends spanning more than seven orders of magnitude";(b) 指数 αN≈0.076、αD≈0.095、αC_min≈0.050,原文写 "doubling the number of parameters yields a loss that is smaller by a factor 2^−αN = 0.95";(c) 原文自承 "performance must flatten out eventually before reaching zero loss"。核对三句逐字、核对指数值、核对 0.95 那句的上下文(是否针对非嵌入参数)。

【G2】「撞墙」的可检验定义:Chinchilla 参数化形式 L = E + A/N^α + B/D^β 中不可约项 E 的存在(Epoch 复现拟合值 E=1.8172);由此推出「收益递减」是幂律内生性质(2020 年就写在公式里),而可检验的「墙」只有两种:(a) 实测点系统性偏离幂律线,(b) 幂律照旧但边际算力的经济代价不可承受。核对 E 的数值与含义(是否为「数据分布的熵/不可约损失」),并检索:有没有 2024-2026 的公开实证显示前沿模型的 loss 实测点系统性偏离了拟合的幂律线?(这是本文最关键的空白检验——如果查无,请明确报告「未检索到」并说明搜索角度。)

【G3】Hoffmann et al. 2022 (arXiv 2203.15556) Chinchilla:(a) "current large language models are significantly undertrained";(b) "for every doubling of model size the number of training tokens should also be doubled";(c) 实践口径约 20 tokens/param(Chinchilla 70B × 1.4T tokens);(d) Chinchilla MMLU 67.5%、"greater than a 7% improvement over Gopher"。另核对:Chinchilla 对 Kaplan 分歧的自家解释(固定 token 数与学习率日程)与 Pearce & Song 2024 (arXiv 2406.12907) 的不同归因(非嵌入参数 vs 总参数、小规模实验)是否如实。

【G4】Epoch AI 的 Besiroglu et al. 2024 (arXiv 2404.10102) 复现:(a) 指出 Hoffmann 第三种估计法与前两种不一致、拟合不上重建数据、置信区间过窄,原文称这么窄的区间 "would require over 600,000 experiments, while they likely only ran fewer than 500";(b) 修正拟合 L(N,D)=1.8172+482.01/N^0.3478+2085.43/D^0.3658,隐含约 20 tokens/param,而 Hoffmann 原 Approach 3 隐含约 70;(c) Hoffmann 主要作者 Borgeaud 承认标准误异常小源于 L-BFGS-B 中 Huber loss 按样本平均而非求和。**重点核对 (c)**:这个「作者承认」到底以什么形式存在(社交媒体?正式勘误?),Besiroglu v2 是怎么引的,arXiv 原文是否有勘误。` },

  { key: 'B2-metrics', body: `
【G5】涌现之争:(a) Wei et al. 2022 (arXiv 2206.07682, TMLR) 对涌现能力的定义 "an ability to be emergent if it is not present in smaller models but is present in larger models" 及「无法从小模型外推预测」;(b) Schaeffer et al. 2023 (arXiv 2304.15004) 是 NeurIPS 2023 Outstanding Paper,主张 "nonlinear or discontinuous metrics produce apparent emergent abilities, whereas linear or continuous metrics produce smooth, continuous predictable changes",且 "alleged emergent abilities evaporate with different metrics or with better statistics"。核对两句逐字、核对 Schaeffer 确实获 NeurIPS 2023 杰出论文奖、并核对该文结论的边界(它是否主张「规模无用」?是否被后续文献反驳?检索 2024-2026 对 Mirage 论文的反驳)。

【G6】GPT-4 技术报告 (arXiv 2303.08774) 的缩放预测力声明:"This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4." 核对 "some aspects" 限定语确实存在、核对报告中同时承认哪些能力事前难料(如 hindsight neglect 的反缩放翻转是否真在该报告中)、以及该报告拒绝披露数据构成的原文("this report contains no further details about the architecture...dataset construction...")。

【G7】基准寿命与污染:(a) arXiv 2602.16763(ICML 2026?)系统研究 60 个 LLM 基准的饱和属性,称近半数已饱和(29/60)、60 个月以上老基准饱和率 54.5% vs 24 个月内新基准 42.9%、抗饱和靠专家策题。**核对该文是否真实存在、作者与发表状态、这些数字是否逐字对得上**(这是一条高风险论断,arXiv 编号可能是幻觉)。(b) Scale AI 的 GSM1k (arXiv 2405.00332):"accuracy drops of up to 13%"、Phi 与 Mistral 系统性过拟合、而前沿模型 "show minimal signs of overfitting"、Spearman r²=0.32。

【G8】Epoch AI 独立复测 GPQA Diamond 自报分数(https://epoch.ai/data-insights/self-reported-gpqa):结论是厂商对近期旗舰的自报分数与独立评测一致、系统性虚报罕见;最大缺口 Llama 4 Maverick 自报 69.8% vs 实测 67.0%(2.8pp,p=0.32);评测噪声 ±4-6pp(90% 置信)。核对数字与 Epoch 自列的限定(只覆盖每家最强一个模型、只适用 GPQA)。另核对:GPQA 原论文中 PhD 专家在自己领域的准确率大约是多少(用于判断 91.9% 是否已逼近标注噪声上限)。` },

  { key: 'B3-narrative-origin', body: `
【G9】撞墙叙事的两篇起点报道:(a) The Information 2024-11-09(Amir Efrati/Stephanie Palazzolo),称 Orion 相对 GPT-4 的提升 "far smaller" 于 GPT-4 相对 GPT-3、且在编码任务上 "isn't reliably better than its predecessor",信源为匿名 OpenAI 员工;(b) Bloomberg 2024-11-13,称三家领先公司 "seeing diminishing returns"、Orion "fell short when trying to answer coding questions that it hadn't been trained on"、Gemini 迭代 "not living up to internal expectations"、Anthropic 3.5 Opus 时间表推迟。两篇均在付费墙后——请尽力回溯逐字引语(存档、权威转述),明确标注哪些字句你实际读到了、哪些只有转述。核对日期。

【G10】Ilya Sutskever 的 "plateaued" 是不是逐字原话:Reuters 2024-11-11 报道中,"results from scaling up pre-training have plateaued" 究竟是引号内直接引语还是记者的间接转述?他的直接引语是否为 "The 2010s were the age of scaling, now we're back in the age of wonder and discovery once again" 和 "Scaling the right thing matters more now than ever"?请打开 Reuters 原文核对句式结构。这条是本文的关键——最高频引用的「撞墙实证」可能是一句转述。

【G11】Ilya 在 NeurIPS 2024(2024-12-13)Test of Time 演讲的逐字内容:"Pre-training as we know it will unquestionably end";"data is the fossil fuel of AI";"we have but one internet";"we've achieved peak data and there'll be no more"。核对逐字(有现场视频与多方转录)、核对日期与场合、并核对**关键口径判断**:他给的理由是数据受限还是算力/幂律失效?

【G12】"there is no wall" 与 "what wall?":(a) Sam Altman 2024-11-14 X 帖是否全文仅 "there is no wall"(四个词)、是否明确指向那三篇报道;(b) Google DeepMind 的 Oriol Vinyals 是否同期回复 "what wall?";(c) 两人当时的利益位置(OpenAI 2024-10 完成 $6.6B 融资等)。核对帖子存在与逐字。注意:X 帖可能无法直接抓取,请通过可靠转述/存档核实并如实标注核实强度。` },

  { key: 'B4-narrative-checkpoints', body: `
【G13】两条疑似伪引 + 一条待核:(a) "Orion 只比 GPT-4 好 20%" —— 检索这一具体百分比在 The Information/Bloomberg 原报道中是否存在;若不存在,核实「可回溯版本」是否为「Orion 完成约 20% 训练时性能已接近 GPT-4」(训练进度口径)。(b) "the age of giant models is over" 常被当 Altman 原话且挪到 2024-11;一手是否为 2023-04 Wired 记录的 MIT 发言 "I think we're at the end of the era where it's going to be these, like, giant, giant models"?(c) Margaret Mitchell 的 "The AGI bubble is bursting a little bit" 是否真出自 Bloomberg 2024-11-13?能否回溯?

【G14】GPT-4.5 作为撞墙叙事的公开验证点:(a) 2025-02-27 发布,Altman 自述 "it is a giant, expensive model"、"this isn't a reasoning model and won't crush benchmarks";(b) API 定价 $75/百万输入、$150/百万输出;(c) system card 初版含 "GPT-4.5 is not a frontier model" 且该句后被 OpenAI 删除;(d) GPT-4.5 后被从 API 下线(核实时间与官方理由)。逐条核对,(c) 尤其要核实删改是否真实发生、依据是什么存档。

【G15】Ilya 2025-11-25 Dwarkesh 播客逐字 + 行为反证:(a) "from 2020 to 2025, it was the age of scaling"、"it's back to the age of research again, just with big computers"、"But is the belief that if you just 100x the scale, everything would be transformed? I don't think that's true"、"more companies than ideas";(b) 2026-07-27 NVIDIA 宣布向 SSI 投资 $50 亿并给 Vera Rubin 平台访问权,"expected to increase the startup's compute resources by an order of magnitude";(c) SSI 融资史 $1B(2024,$5B 估值)→$2B(2025-02,$32B 估值);(d) SSI 至 2026-08 无产品。核对逐字与 NVIDIA 官方新闻稿。**并检验一个反驳**:Ilya 说的是「带着大计算机做研究」,那么「他一边说 scaling 结束一边买 10 倍算力」是不是断章取义?给出你的裁决。

【G16】Vinyals 的 Gemini 3 发帖(2025-11-18)口径拆解:原文 "Pre-training: Contra the popular belief that scaling is over...the team delivered a drastic jump. The delta between 2.5 and 3.0 is as big as we've ever seen. No walls in sight!" —— 核对逐字;并裁决关键口径问题:"improving pre-training"(配方/数据/算法改进)与 "scaling pre-training compute"(纯算力放大)是否是两个命题,他的措辞属于哪一个?Google 是否公开过 Gemini 3 的预训练 FLOP?另核实帖中提到的 "NeurIPS '25 talk with @ilyasut and @quocleix" 是否成立(发帖日 2025-11-18 时 NeurIPS 2025 是否尚未举行)。` },

  { key: 'B5-narrative-hedges', body: `
【G17】Dario Amodei 2026-03-03 在 Morgan Stanley TMT 大会上的 "We do not see hitting the wall. We don't see a wall." 与「2026 年会有激进加速」的预言。**这条只有中文转述(36kr)作为来源,风险高**:请尽力回溯英文一手(会议实录、权威英文媒体报道、Anthropic 官方)。若回溯不到,判 REFUTED 或降级为【未验证】,并给出可替代的、有一手来源的 Amodei 2026 年表态。

【G18】Karpathy 的两次表态与转职:(a) 2025-10-17 Dwarkesh 播客:"the industry is making too big of a jump and is trying to pretend like this is amazing, and it's not. It's slop"、RL is "sucking supervision through a straw"、AGI 还要十年;(b) 2026-05-19 宣布加入 Anthropic 领导用 Claude 加速预训练研究的团队,原话 "I've joined Anthropic..."。核对两处逐字与日期;并裁决:「此举证明预训练没死」是否为评论者推断而非当事人主张。

【G19】GPT-5 (2025-08-07) 反弹的两个口径:(a) 反弹主因是产品事故(路由器故障、4o 下线引发用户情感反弹、发布会图表错误)还是模型能力停滞?(b) Altman 是否说过 OpenAI "totally screwed up" 发布;(c) Gary Marcus 的 "overdue, overhyped, and underwhelming" 逐字与日期;(d) 这场反弹被引作「能力撞墙」证据的程度。逐条核对,并给出你对 (a) 的裁决。

【G20】三条对冲型表态(用于证明「双方旗手都在对冲」):(a) Alexandr Wang 2024-11 在 Cerebral Valley:"It seems to be the case that we've hit a wall on pre-training" 但 "we haven't hit a wall on progress in AI"(注意其 Scale AI 卖数据的利益位置);(b) Satya Nadella 2024-11:scaling laws "are not physical laws. There are just empirical observations that hold true just like Moore's law did"(经 Gary Marcus 转引,请尽力回溯原始场合);(c) Demis Hassabis 2026-04-07(20VC):scaling 收益仍 "very substantial"、收益递减叙事被夸大,但他也说过 scaling 只占通往 AGI 的约一半。逐条核对逐字与场合。` },

  { key: 'B6-bench-series', body: `
【G21】SWE-bench Verified 时序(撞墙叙事发布后能力是否持续跃升的主数据链):(a) 2024 年末约 49% 一线(Claude 3.5 Sonnet 升级版 49.0%、o1 48.9%、o3-mini 49.3%、DeepSeek R1 49.2%);(b) Claude 3.7 Sonnet (2025-02) 62.3%,加 custom scaffold 70.3%,且 70.3% 是 n=489 子集口径;(c) GPT-5 (2025-08) 74.9%;(d) Gemini 3 Pro (2025-11-18) 76.2%、GPT-5.1-Codex-Max 77.9%、Claude Opus 4.5 (2025-11-24) 80.9%(首个破 80)。逐条回溯厂商发布页核对,标明哪些是厂商自报、哪些有独立复测。**并补一个 2026 年的读数**:检索 2026-08 时 SWE-bench Verified 的最高公开成绩(注意 Claude Fable 5 声称 95.0% 的说法是否可回溯到官方)。

【G22】scaffold 混杂变量:Epoch AI(https://epoch.ai/gradient-updates/why-benchmarking-is-hard)称仅更换 scaffold 就能让 SWE-bench Verified 上 GPT-5 分数波动最多 11 个百分点、Kimi K2 Thinking 最多 15 个百分点,且 "The choice of scaffold has the single biggest impact on the overall performance"。核对逐字与数字;并裁决推论「跨厂商榜单 1-3pp 的差距无判别力」是否成立(是 Epoch 说的还是本文推断)。

【G23】FrontierMath 资助争议与 o3 数字的两次口径:(a) Epoch 声明(2025-01-16):OpenAI 出资、拥有 300 题所有权、可见其中 250 题的题面与解答,50 题 holdout 仅给题面;多数出题者不知情;Epoch 承认沟通失误。(b) TechCrunch 报道中「不用于训练」仅为口头协议(verbal agreement)。(c) OpenAI 2024-12 称 o3 FrontierMath >25%,Epoch 2025-04 用发布版 o3 独立实测约 10%;Mark Chen 逐字:"We're seeing [internally], with o3 in aggressive test-time compute settings, we're able to get over 25%."逐条核对逐字。

【G24】ARC-AGI 的 o3-preview 四重口径(2024-12-20 arcprize.org):(a) semi-private 集 75.7%($10k 算力上限、6 样本、33.5M tokens、$26/题、总 $2,680);(b) 172 倍算力档 87.5%(1024 样本、5.7B tokens、$4,560/题、总 $456,000);(c) OpenAI 自述该模型 "trained on 75% of the Public Training set";(d) 成本数字后被重新核算(2025 年按 o3-pro 价 $80/M tokens 上修,有说法称 $4,560 上修至约 $30,000)。**(d) 是高风险数字,请务必回溯**:上修到底发生过吗、上修后的准确数字是多少、依据什么价目。另核对 Chollet 同篇中「人类解 ARC 约 $5/题」与「o3-preview 低算力档 $27/题」的对照,以及他同时预测成本-性能会快速改善。` },

  { key: 'B7-caliber-traps', body: `
【G25】同名不同模(本题最典型口径陷阱):ARC Prize 2025-04-22 复测发布版 o3:ARC-AGI-1 semi-private 上 o3-low 41%、o3-medium 53%,ARC-AGI-2 均未超 3%(对照 preview 的 75.7%/87.5%);OpenAI 确认 "this public o3 model differs from the o3-preview we tested in December 2024";发布版未直接用 ARC 训练;preview 的 test-time 算力档在产品中不可用。另:o3-high 在 100 题中只返回 37 题、其中 82% 正确,ARC Prize 明确称该数据 "should not be reported on"。逐条核对逐字。

【G26】ARC-AGI-2 时序与 ARC-AGI-3:(a) 2025-03 发布时前沿模型个位数(Gemini 2.5 Pro 4.9%、发布版 o3 2.9%);(b) GPT-5.1 17.6%;(c) Gemini 3 Pro 31.1%(Deep Think 45.1%,2025-11);(d) GPT-5.2 约 53%(2026-01);(e) 2026-08 榜首约 92.5%(GPT-5.6 Sol)、Claude Opus 5 约 90.4%;(f) ARC-AGI-3(2026-03 推出)把所有前沿模型打回近零。**(d)(e)(f) 来自第三方聚合榜(benchlm/adaline),风险高**——请到 arcprize.org 官方 leaderboard 核对 verified 标记、算力/成本档与准确数字,对不上的一律修正或降级。

【G27】Humanity's Last Exam 时序:(a) 2025-01 发布时 GPT-4o 2.7%、Claude 3.5 Sonnet 4.1%、o1 8.0%;(b) Grok 4 自报 25.4%(带工具 44.4%,2025-07)、GPT-5 25.3%;(c) Gemini 3 Pro 37.5%(2025-11);(d) 2026-08-16 Scale 公开榜 Gemini 3.1 Pro Preview (thinking high) 46.44%、GPT-5.4 Pro 44.32%。核对 no-tools vs with-tools 口径、text-only vs 全集口径;到 scale.com/leaderboard 核对 2026-08 读数。另核对 HLE 由 Scale AI + CAIS 维护、Scale 同时是数据供应商这一利益关联。

【G28】顶部拥挤(判断「放缓」还是「多家追平」):Artificial Analysis 2026-07-16 报告称 8 天内 4 家发旗舰、6 家实验室有 Intelligence Index >50 的模型(6 月初仅 2 家)、前三名仅差 3 分、榜首领先从 4 分缩到 1 分,而 2022 年末以来大部分时间前沿由一两家独占。核对逐字与数字;并核对 AA 指数是否换过版本(跨版本可比性)、AA 是否接受厂商付费(利益位置)。裁决:这些数字支持「进步放缓」还是「多家追平且绝对分仍在涨」?` },

  { key: 'B8-independent', body: `
【G29】METR 2025-03-19 原始论文:(a) 50% time horizon 的定义;(b) 2019-2025 指数增长、倍增期约 7 个月;(c) Claude 3.7 Sonnet 约 1 小时;(d) METR 自报 caveat:"there remains the possibility of substantial model error"、结果 "do not account for future changes in the trend or external validity concerns, which are responsible for the majority of our uncertainty"。核对逐字;并核对任务集构成(HCAST+RE-Bench+SWAA)与 80% horizon 比 50% 低多少。

【G30】METR Time Horizon 1.1(2026-01-29)改版:(a) 任务从 170 扩到 228(新增 73 个 HCAST 任务、8 小时以上长任务从 14 增到 31、删 15 改 53);(b) 基础设施从 Vivaria 迁到 UK AISI 的 Inspect;(c) 2023 年以来倍增期 130.8 天 [95%CI 107,161],TH1.0 为 165.3 天;2024 年以来 88.6 天(约 10x/年),TH1.0 为 108.9 天;(d) 整体较 TH1.0 判快约 20%;(e) 具体模型 50% horizon:Claude Opus 4.5 = 320 分钟 [170,729]、GPT-5 = 214 [117,480]、o3 = 121 [74,201]、Claude 3.7 Sonnet = 60 [32,106];(f) METR 自列 caveat:31 个 8h+ 长任务中只有 5 个有实测人类基线。**这是本文的独立测量脊柱,逐条核对**;并核对全样本 P50 倍增是否仍为 196.5 天(即「10x/年」是 2024 后子样本斜率)。另检索:2026-08 前 METR 有没有更新的读数或对 1.1 的批评。

【G31】Epoch Capabilities Index:(a) 149 个模型、2021-12 至 2025-12;(b) 前沿能力进步在 2024-04 前后出现断点加速,从约 8 分/年升到约 15 分/年;(c) 此后未见减速。核对数字与断点日期;并核对**关键限定**:ECI 测的是部署能力总进步(含推理/RL/后训练/工具)还是预训练单因子?这直接决定「预训练收益递减」与「总能力加速」能否同时为真。

【G32】2025 年 7 月的 IMO 金牌:(a) OpenAI 实验推理模型与 DeepMind Gemini Deep Think 均达 35/42 金牌线;(b) 人类同规则(两场 4.5 小时、无工具、自然语言证明);(c) DeepMind 经 IMO 官方评委认证,OpenAI 抢在官方放榜前自行宣布、由 3 名前 IMO 奖牌得主评分;(d) 两家均为实验版模型而非发售产品。逐条核对。` },

  { key: 'B9-reasoning-axis', body: `
【G33】o1 的双曲线与采样口径:(a) OpenAI o1 博客(2024-09-12)原文 "The performance of o1 consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute). The constraints on scaling this approach differ substantially from those of LLM pretraining";(b) 图的 x 轴是否标注绝对算力刻度;(c) AIME 三档口径:单样本 74%(11.1/15)、64 样本共识 83%(12.5/15)、1000 样本+学习打分器重排 93%(13.9/15)。逐条核对逐字与数字。

【G34】DeepSeek 的三个成本口径:(a) V3 论文(arXiv 2412.19437)"2.788M GPU hours"、"$2 per GPU hour"、"$5.576M",且原文明确 "excluding the costs associated with prior research and ablation experiments";(b) R1 的 RL 阶段约 $294,000、512 块 H800、约 80 小时,首次披露于 2025-09 Nature 论文(s41586-025-09422-z)补充材料;(c) Epoch 在官方披露前独立估算 RL 阶段 "around $1M"。逐条核对;并裁决媒体口径「训练 R1 只花 560 万美元」错在哪。

【G35】RL 缩放的形状与时间表:(a) Meta《The Art of Scaling RL Compute for LLMs》(arXiv 2510.13786):40 万+ GPU 时,拟合出 **sigmoid** 而非幂律的算力-性能曲线,可从小规模外推预测 10 万 GPU 时单次 RL run;(b) Epoch(2025-05)依据 OpenAI 披露「o3 训练算力是 o1 的 10 倍」推断:推理 RL 训练算力若继续每几个月 10 倍增长,最快一年内触及总训练算力前沿,此后回落到约 4x/年。核对 (a) 的 sigmoid 结论与 GPU 时数、核对 (b) 的推断链与 OpenAI 那个「10 倍」的原始出处。**并检索 2026 年的后续**:RL 缩放到 2026-08 是否已如 Epoch 预测那样触顶回落?

【G36】RL 是引出还是新增能力:(a) Yue et al.(arXiv 2504.13837):RLVR 模型在小 k 占优、基座在大 k 反超,"the current training setup does not elicit fundamentally new reasoning patterns...originate from and are bounded by the base model";(b) NVIDIA ProRL(arXiv 2505.24864)反例:延长 RL(2000+ 步)"can uncover novel reasoning strategies that are inaccessible to base models, even under extensive sampling",全 k 区间 pass@k 占优;(c) 分歧根源(训练步数、模型规模 1.5B vs 前沿、k 取值、可验证域蒙对)。核对两文逐字与实验规模;检索 2026 年这场争论有没有新的裁决性证据。` },

  { key: 'B10-data-wall', body: `
【G37】推理经济的双向性:(a) Epoch:达到同一性能水位的 LLM 推理价格每年下降 9 至 900 倍,"the price to achieve GPT-4's performance on a set of PhD-level science questions fell by 40x per year",且最快降幅集中在最近一年、能否持续存疑;(b) 反向:Artificial Analysis 数据显示跑完 7 个基准 o1 花 $2,767.05 而 GPT-4o 只要 $108.85(约 25 倍),12 个推理模型共花 $5,200 超过 80 多个非推理模型的 $2,400;(c) OpenAI 2025-06-10 将 o3 降价 80%($10/$40→$2/$8)称 "Same exact model—just cheaper",ARC Prize 复测确认性能未变。逐条核对;并裁决「推理变便宜」与「推理变贵」同时为真的口径拆解是否正确。

【G38】数据存量的三个口径:(a) Villalobos et al. v1(2022-10)"high-quality language data 很可能在 2026 年前耗尽";(b) v2(ICML 2024)改为「2026-2032 年间训练集规模追平公开人类文本存量,过训练则更早」;(c) Epoch 2024-06 博客:质量与重复调整后有效存量约 300 万亿 token、80% 置信区间 2026-2032、过训练 5 倍则 2027 用完、过训练 100 倍则 2025 用完。逐条回溯两版摘要逐字;并裁决关键语义:Epoch 口径是「训练集规模追上存量」还是「数据被物理用光」。

【G39】Muennighoff et al.(NeurIPS 2023, arXiv 2305.16264):"with constrained data for a fixed compute budget, training with up to 4 epochs of repeated data yields negligible changes to loss compared to having unique data";"with more repetition, the value of adding compute eventually decays to zero";实验规模至 900B token、9B 参数、400 个 run。核对逐字与规模上限,并明确该结论的外推限度。

【G40】Model collapse 的两侧:(a) Shumailov et al. Nature 2024-07-24:摘要限定语 "indiscriminately training generative artificial intelligence on real and generated content...can lead to a collapse";实验为替换式递归(OPT-125m/wikitext2,不保留原始数据时数代内 perplexity 从 34 恶化到 50+);同文称保留 10% 原始数据时 10 代内基本稳定。(b) Gerstgrasser et al.(arXiv 2404.01413):"accumulating the successive generations of synthetic data alongside the original real data avoids model collapse",累积时测试误差有与迭代次数无关的有限上界。**核对 (a) 中「保留 10%」这一条是否真在 Nature 原文里**(这是高风险数字,经二手转述)。(c) 检索:截至 2026-08 有没有任何一例经证实的「model collapse 在真实生产训练管线中被观测到」的公开报告?明确报告你的全部搜索角度。` },

  { key: 'B11-compute-econ', body: `
【G41】合成数据的分母陷阱与测量缺席:(a) 微软 phi-4(arXiv 2412.08905):合成数据占预训练 token 预算 40%(总约 10T token)、约 400B 独立合成 token、合成部分重复约 13.8 epoch;自报 14B 的 phi-4 在 GPQA 与 MATH 上超过其教师 GPT-4o;(b) NVIDIA Nemotron-4 340B:"over 98%" 是**对齐阶段**(SFT+DPO/RPO)数据占比、人工标注仅约 2 万条——不是预训练占比;(c) 前沿闭源模型的合成数据占比无独立测量(GPT-4 报告起拒绝披露数据构成)。逐条核对;并裁决推论「合成数据成功案例几乎全是有更强教师的蒸馏,不能外推为前沿模型自举越过数据墙」。

【G42】数据供给收紧与「墙咬到了吗」:(a) Longpre et al.《Consent in Crisis》(arXiv 2407.14933):robots.txt 收紧使 C4 全体 token 的约 5%+、C4 中最活跃维护关键来源 token 的 28%+ 被完全禁止抓取;ToS 口径则 45% 受限。(b) WSJ 2024-12-20 关于 Orion 的报道:至少两次大型训练 run 不及预期、每次成本约 5 亿美元、"there may not be enough data in the world to make it smart enough";OpenAI 转向雇人写数据与合成数据。(c) 公开预训练规模仍逐代上涨:Llama 3 15T → Qwen3 约 36T → Llama 4 Scout 约 40T(注意多模态 token 口径)。逐条核对逐字与数字;(b) 尤其核对 WSJ 原文措辞与 OpenAI 是否证实过「数据不足」这一归因。

【G43】Epoch 的供给侧论证(与「收益递减」的关键区别):(a) 2024-08《Can AI scaling continue through 2030?》:索引网络约 500T 词、2030 前增 50%;计入多模态与合成后 2030 年有效 token 400 万亿–2 京;2e29 FLOP 的训练 run 到 2030 "likely possible";最先咬合的约束是电力,其次是芯片产能——**不是数据**。(b) 2025-09-05《Compute scaling will slow down due to increasing lead times》:"every additional 10x increase in compute scale lengthens lead times by around a year";GPU 采购约 0.5 年、数据中心 1-2 年、超大数据中心+电厂 2-3 年、新建先进晶圆厂 4-5 年;训练算力仍可维持 5x/年约 1-2 年。逐条核对逐字;并裁决:Epoch 预测的放缓机制是供给侧交付还是技术收益递减?

【G44】算力经济的四组数字:(a) Epoch:frontier 训练算力 2010–2024.5 年增 5.3x(90%CI 4.9–5.7),notable 模型 4.1x,frontier 语言模型 5.0x(80%CI 3.1–7.3);(b) 最大 run 成本 2.4x/年(95%CI 2.0–3.1),从 GNMT 约 $20 万(2016)到 Grok 4 约 $5 亿(2025),口径为**摊销硬件+能源**(2023 美元)非集群全额资本开支;(c) 算法效率:达到同一性能所需预训练算力每约 8 个月减半(95%CI 5–14 个月,arXiv 2403.05812,基于 200+ 语言模型在 Wikitext/Penn Treebank);(d) Epoch 估 GPT-5 总训练算力约 5e25 FLOP(含 RL),高于 GPT-4 约 2e25 但低于 GPT-4.5 >1e26,归因于后训练技术与时间压力而非撞墙,并预测 GPT-6 回升;Epoch 定性为 "a pause, not a halt"。逐条核对;(d) 尤其核对 Epoch 的原文措辞与「a pause, not a halt」是否为逐字。` },
]

phase('Verify')
const results = await parallel(
  BATCHES.flatMap((b) =>
    [1, 2, 3].map((v) => () =>
      agent(HEAD + b.body, {
        label: `${b.key}-v${v}`,
        phase: 'Verify',
        schema: SCHEMA,
        model: 'opus',
      })
    )
  )
)
const out = []
BATCHES.forEach((b, bi) => {
  out.push({ batch: b.key, votes: results.slice(bi * 3, bi * 3 + 3).filter(Boolean) })
})
return out
