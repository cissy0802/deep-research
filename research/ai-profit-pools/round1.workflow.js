export const meta = {
  name: 'profit-pools-round1',
  description: 'Round 1: AI 价值链利润池 7 条调研线并行收集一手来源与论断',
  phases: [{ title: 'Research', detail: '7 条调研线并行' }],
}

const DIR = '/Users/cissychen/Desktop/repos/deep-research/research/ai-profit-pools/lines'

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
          claim: { type: 'string', description: '论断(中文),数字带口径:分子/分母/时间窗/GAAP或non-GAAP/run-rate或确认收入' },
          quote: { type: 'string', description: '一手原文逐字摘引(英文原文)' },
          source_url: { type: 'string' },
          source_type: { type: 'string', description: '同行评审|官方(财报/SEC/官方博客)|厂商自报|从业者博客|媒体转述|分析机构' },
          date: { type: 'string' },
          loadbearing: { type: 'boolean', description: '是否可能承重(错了会影响"利润落在哪一层"的判断)' },
          side: { type: 'string', description: '支持/反驳哪种叙事:卖铲子赢|模型商品化|聚合者通吃|前沿赢家通吃|电力稀缺|中性' },
        },
      },
    },
    caliber_issues: { type: 'array', items: { type: 'string' }, description: '交叉口径问题清单(供验证阶段)' },
  },
}

const HEAD = `你是深度研究调研员。研究总题:「AI 价值链的利润池会落在哪一层?」——芯片、电力/数据中心、云、模型、分发/应用五层里,长期利润会沉淀在哪?做模型的是不是在给人做嫁衣?今天是 2026-10-05,成文标「截至 2026 年 10 月」,必须刷新到最新季报(NVIDIA 最新为 Q2 FY27 截至 2026-07-26;云厂商最新为 2026 年 Q2,7 月底发布)。

四套互相矛盾的流行叙事:(1) 卖铲子的赢(芯片/基建);(2) 模型商品化(价格年降一个数量级、开源追平);(3) 聚合者通吃(握住用户关系者把上游商品化);(4) 前沿实验室赢家通吃。外加 (5) 电力/电网是最持久的稀缺点。

工作要求:
- 用 WebSearch/WebFetch 找**一手来源**(10-K/10-Q/8-K 新闻稿、财报电话会逐字稿、官方定价页、论文原文、原著),逐字摘引原文。WebFetch 的摘要模型可能编造引语——关键数字要求它逐字引用,能用 SEC 原文就用 SEC 原文(可用 Bash curl -A "research bot chengchen0802@gmail.com" 抓 sec.gov)。
- 来源分级:同行评审 / 官方 / 厂商自报 / 从业者博客 / 媒体转述 / 分析机构。厂商与利益相关方的数字标注口径。前沿实验室是非上市公司,其财务数字几乎全是厂商口径或媒体转述——照收但标清楚。
- 口径必须分开:"AI 收入"各公司定义不同;承诺额 vs 落地额;run-rate vs 确认收入;毛利 vs 经营利润;GAAP vs non-GAAP;财年 vs 日历年。
- 正反证据都要收,尤其是与主流叙事相反的。区分"当下利润分布"与"长期利润落点"。
- 目标约 25-40 条论断,宁精勿滥;每条带 URL 与日期。
- **随时落盘**:边调研边把论断与引文写到 ${DIR}/<你的线 key>.md(Write 工具),结束前确保文件完整。最终输出结构化数据。

你负责的调研线:
`

const LINES = [
  { key: 'T-theory-history', body: `【T 理论与历史类比】独占产出:原典逐字 + 历史上各层利润分配的数据。
- Bain 利润池(Gadiesh & Gilbert 1998 HBR "Profit Pools: A Fresh Look at Strategy");微笑曲线(施振荣/Stan Shih 1992)。
- Christensen「利润守恒定律」(Law of Conservation of Attractive Profits;Christensen & Raynor《The Innovator's Solution》2003,及 2004 HBR "Skate to Where the Money Will Be")——逐字找原文表述:模块化商品化的一层,利润迁移到相邻的整合层。
- Ben Thompson 聚合理论(Stratechery 2015 "Aggregation Theory")及他对 AI 的应用(AI 时代谁是聚合者;他对模型商品化的论述)。Joel Spolsky "commoditize your complements"(2002)。
- 历史:1999-2002 光纤/电信泡沫(建设者破产,如 Global Crossing、WorldCom;光纤利用率/暗光纤比例;使用者赢);铁路狂热与电气化(基建承担风险、使用方拿剩余);PC 时代 Wintel 拿走利润、整机商品化(Intel/微软 vs Dell/Compaq/IBM PC 利润率数字);智能手机(苹果占行业利润 80%+ 的口径)。
- 反方:类比失效的理由(例如 AI 模型层与 PC OS 的差别、规模经济/学习效应、网络效应是否存在)。
- 现代应用:a16z、Sequoia、Bain Technology Report 2024/2025 对 AI 利润池的分析;Benedict Evans 论模型商品化。` },
  { key: 'CHIP-semis', body: `【CHIP 芯片层】独占产出:半导体财报数字。
- NVIDIA 数据中心收入、毛利率(GAAP/non-GAAP)、经营利润率时序(FY2023→Q2 FY27),前几大客户收入集中度(10-Q 里的 direct customer 占比)。
- AMD 数据中心 GPU、Broadcom AI 收入(定制 ASIC/XPU,客户如 Google、Meta、OpenAI)、Marvell;TSMC(先进制程/CoWoS 毛利,AI 加速器收入占比);SK hynix/美光 HBM 利润率——利润是否沿供应链上游分流。
- 自研芯片:Google TPU(含对外销售/出租,如 Anthropic 的 TPU 协议)、AWS Trainium(Project Rainier)、Meta MTIA、微软 Maia;其成本优势的一手或可信测算;在推理负载中的占比。
- CUDA 护城河正反:开发者生态、互联(NVLink/InfiniBand)、供给约束 vs 大客户议价、推理负载对软件锁定的弱化。
- DeepSeek-R1(2025-01-27):NVDA 单日跌幅与市值蒸发(约 17%、约 $589B,待核),之后恢复——作为"模型商品化/杰文斯悖论"自然实验的解读正反。
- NVIDIA 毛利率是否已出现压缩迹象(新品爬坡、对大客户折扣、对 OpenAI 等的投资回流)。` },
  { key: 'CLOUD-hyperscalers', body: `【CLOUD 超大云厂商层】独占产出:云厂商财报与 10-K/10-Q 口径。
- 微软(Azure 增速、AI 业务 run-rate 口径如"AI business surpassed $X annual revenue run rate"、Intelligent Cloud 利润率、对 OpenAI 的收入分成与权益法亏损)、Alphabet(Google Cloud 收入与经营利润率、积压订单)、Amazon(AWS 收入与经营利润率、Bedrock)、Meta(无云业务,AI 回报经广告体现)、Oracle(OCI、RPO 数千亿、毛利率争议——The Information 报道 GPU 租赁毛利约 14% 待核)。
- capex:各家 2025 实际与 2026 指引(一手:财报电话会/新闻稿);capex 占经营现金流比例;自由现金流变化。
- 折旧政策:各家服务器使用年限变更(MSFT/GOOG 4→6 年,Meta 5→5.5 年,Amazon 2025 部分回调 6→5 年)及其对利润的影响额(10-K 原文数字);Michael Burry 等对折旧年限的批评与反驳。
- 云层 AI 毛利:GPU 出租业务毛利 vs 传统云毛利;"AI 收入"定义差异。
- 只用一手数字,二手分析标注。` },
  { key: 'PHYS-neocloud-power', body: `【PHYS 算力租赁与电力/数据中心层】独占产出:GPU 租价与电力经济学——"谁拿走稀缺租金"。
- neocloud:CoreWeave(收入、调整后经营利润 vs GAAP 净亏损、利息支出、债务规模、客户集中度——微软/OpenAI 占比、RPO)、Nebius、Lambda、Crusoe;其商业模式是否只是"带杠杆的折旧套利"。
- GPU 小时租价时序:H100 从 2023 年约 $8/h 到 2025-26 的价格(SemiAnalysis、Ornn/Silicon Data H100 租赁指数 SDH100RT 等独立指数);B200/GB200 定价;租价下跌对 GPU 经济寿命和折旧年限的含义。
- 电力层:公用事业与独立发电商(Vistra、Constellation、Talen)利润与股价、核电 PPA 价格(微软-三里岛、Meta-Constellation 等)、电网接入排队、数据中心电价;燃气轮机(GE Vernova)订单积压与定价权;数据中心 REIT(Equinix/Digital Realty)及租金。
- 判断:电力/电网接入是否是最持久的稀缺点——供给弹性(建厂周期、电网建设周期)vs 需求被高估(幽灵需求)。可复用的已知:#15 期研究指出约束从芯片移到电力,但不要重复论证短缺本身,只看利润分配。` },
  { key: 'MODEL-labs', body: `【MODEL 模型层】独占产出:模型层单位经济学。
- OpenAI、Anthropic、xAI、Google DeepMind(内部)、Mistral 等的收入(年化 run-rate vs 确认收入)、亏损、毛利率、推理成本、训练成本口径;来源多为 The Information / FT / Reuters / CNBC 报道或公司自述——逐条找最原始的报道并标注"媒体转述/厂商自报"。2026 年最新数字(如 OpenAI 年化约 $70B、Anthropic 年化 $30B+、毛利 33%/40%、OpenAI 2026-2030 累计负 FCF $278B 等,均待核)。
- API 价格时序:GPT-4 级能力每百万 token 价格从 2023 到 2026 的下降(Epoch AI "LLM inference prices" 研究——不同能力阈值下年降 9×-900× 之类的数字,逐字核;a16z "LLMflation" 年降 10×)。
- 开源权重追赶:Epoch 开源 vs 闭源滞后月数测算;DeepSeek V3/R1 训练成本口径($5.6M 仅最后一次训练运行);Qwen/Llama/Kimi 等;蒸馏。
- 前沿溢价证据:最新前沿模型的定价是否维持高价(如顶级模型每百万 token 价格不降反升)、企业市场份额(Menlo Ventures 企业 LLM API 份额调查——Anthropic 超过 OpenAI 等,注意为调查口径)、订阅价格上探($200/月档)。
- 模型公司的成本侧:向云/芯片支付的算力承诺(OpenAI 与 Oracle/微软/AWS/CoreWeave 合同额)——说明利润被上游截走的程度。` },
  { key: 'APP-distribution', body: `【APP 应用/分发层】独占产出:应用层单位经济学与分发争夺。
- AI 应用公司毛利:Cursor(Anysphere)、Perplexity、Replit、Lovable、GitHub Copilot 等的毛利率/推理成本占收入比(多为媒体报道);"wrapper" 被上游供应商挤压的案例(如供应商涨价/限流、Anthropic 对 Windsurf 断供、Cursor 定价风波)。
- 模型公司纵向整合:ChatGPT C 端订阅收入占比、Claude Code 收入、OpenAI 的应用层扩张(浏览器、设备、广告、购物);是否在吃掉应用层利润——"模型公司做应用"vs "应用公司自研模型"(Cursor Composer 等)。
- 聚合者:Google 搜索 AI Overviews 对广告收入的影响(Alphabet 财报数据)、Apple(Apple Intelligence 与 Gemini 协议)、Meta(AI 驱动广告效果提升的财报口径)、微软 Office Copilot 采用与收费——握有分发的现有巨头是否拿走了利润。
- 企业应用层收入总量(Menlo Ventures 2025 State of Generative AI in the Enterprise 等,标调查口径)、SaaS 公司 AI 加价能否兑现。
- 反方证据:应用层"厚"的论点(工作流锁定、数据、品牌)与应用层高增长公司的实际利润。` },
  { key: 'FLOW-crosslayer', body: `【FLOW 跨层资金流与总量账】独占产出:跨层资金流与总量账。
- 收入缺口测算:Sequoia David Cahn "AI's $200B Question"(2023)→ "$600B Question"(2024)的算法与后续更新;Bain 2025 年 "需要 $2T 年收入支撑 2030 年算力需求、缺口 $800B" 类测算(逐字核);其他(摩根士丹利、高盛、JPMorgan)对 AI 收入 vs capex 的估算。
- 循环融资:NVIDIA 对 OpenAI 最多 $100B 投资意向(2025-09)及其后实际落地情况;AMD-OpenAI 6GW 协议与认股权;Oracle-OpenAI $300B 合同;CoreWeave-OpenAI 合同与 NVIDIA 对 CoreWeave 的持股/回购承诺;微软-OpenAI 重组后的收入分成与 Azure 承诺 $250B;Anthropic-Google/Amazon/微软/NVIDIA 投资与算力采购。核心问题:钱从哪层流到哪层,承诺额 vs 落地额。
- 各层收入/利润总量的第三方估算(如"芯片层拿走 AI 经济的大部分利润"的量化,或各层毛利美元额的比较);注意口径。
- 2026 年最新进展(截至 10 月):任何关于循环融资的新交易、减记、取消或重新谈判。` },
]

phase('Research')
const results = await parallel(LINES.map(l => () =>
  agent(HEAD + l.body + `\n\n你的线 key 为 ${l.key},落盘文件 ${DIR}/${l.key}.md。`, { label: l.key, phase: 'Research', schema: SCHEMA })
))
return results.filter(Boolean)
