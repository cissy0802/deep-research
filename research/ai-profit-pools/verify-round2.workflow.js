export const meta = {
  name: 'profit-pools-round2',
  description: 'Round 2: AI 利润池 31 组承重论断 × 3 票对抗验证',
  phases: [{ title: 'Verify', detail: '12 批 × 3 票独立反驳(三镜头)' }],
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
          caliber_fixes: { type: 'array', items: { type: 'string' }, description: '逐条口径修正:修正前 → 修正后;子论断判死的写「判死:…」' },
          primary_source_checked: { type: 'string', description: '你实际打开的一手 URL' },
          evidence_grade: { type: 'string', description: '多源证实|单源已核|方向存争|厂商口径|未验证' },
        },
      },
    },
  },
}

const HEAD = `你是对抗验证员。任务不是确认,而是**尽力反驳**——refute by default。文章题目:「AI 价值链的利润池会落在哪一层?」(截至 2026 年 10 月;今天是 2026-10-05)。

对每一组论断:
1. 用 WebFetch 打开一手来源逐字核对(SEC 10-K/10-Q/8-K 原文、财报电话会逐字稿、官方博客、论文原文)。SEC 文件可用 Bash: curl -s -A "research bot chengchen0802@gmail.com" <url> | 然后 grep/python 抽取相关段落,比 WebFetch 摘要可靠。WebFetch 的摘要小模型可能编造引语和数字——关键数字必须让它逐字引用原文,能用 curl 原文就用 curl。
2. 检查:分子/分母、时间窗(财年 vs 日历年)、GAAP vs non-GAAP、run-rate vs 确认收入、承诺额 vs 落地额、分部经营利润 vs 净利、限定语、是否被后续版本或重述修正、说话者利益位置。自算的比率要重算一遍。
3. 主动检索反证:有没有独立来源给出矛盾数字?有没有更新(2026-08 至 10 月)的数字或事件推翻它?
4. 判决 HOLDS(逐字核对无误、可按原强度写入)/ CORRECTED(方向对但口径须修正,给出修正后表述)/ REFUTED(核心事实站不住)。组内有多个子论断时,逐个在 caliber_fixes 里交代;任一子论断站不住写「判死:…」。
5. 宁可判 CORRECTED 也不要放过口径滑坡。找不到一手来源的数字或引语判死或降级为【未验证】;媒体转述的非上市公司数字,能找到最原始报道就标注到报道,找不到就标【未验证】。
6. 证据分级:多源证实 / 单源已核 / 方向存争 / 厂商口径 / 未验证。

`

const LENSES = [
  '你的侧重镜头:**逐字镜头**——每个数字和引语都必须回到一手文件逐字核对,数字精确到原文写法,引语逐词比对。',
  '你的侧重镜头:**反证镜头**——重点搜索与该论断矛盾的独立来源、更新的数据、后续重述/修订/取消事件,以及对立解读。',
  '你的侧重镜头:**口径镜头**——重点检查分子分母、时间窗、财年错位、GAAP/non-GAAP、run-rate/确认收入、承诺/落地、自算比率是否算对、标签是否同名不同物。',
]

const BATCHES = [
  { key: 'B01-theory-quotes', model: 'sonnet', body: `
【G01】Christensen 原典:(a) HBR "Breakthrough Ideas for 2004"(2004-02)中的「利润守恒定律」:"When attractive profits disappear at one stage in the value chain because a product becomes commoditized, the opportunity to earn attractive profits with proprietary products usually emerges at an adjacent stage."(b)《The Innovator's Solution》(Christensen & Raynor 2003):性能不够好时(performance gap),"firms that build their products around proprietary, interdependent architectures enjoy an important competitive advantage against competitors whose product architectures are modular";(c) 同书:"companies that position themselves at a spot in the value chain where performance is not yet good enough will capture the profit." (d) "Skate to Where the Money Will Be" 发表于 HBR 2001-11(Christensen, Raynor, Verlinden),含 IBM「70% of the entire mainframe market, controlled 95% of its profits」。核对原文措辞、出处年份与作者。
【G02】Ben Thompson 的 2026 年三次表态(Stratechery):(a) 2026-03-16「Agents Over Bubbles」:"profits flow away from modular parts of the value chain — which are commoditized — and flow towards integrated parts of the value chain, which are differentiated",并认为 Anthropic/OpenAI 利润前景比 2025 年底好;(b) 2026-06-15「Anthropic's Safety Superpower」:"the biggest beneficiaries have been Nvidia, TSMC, and the memory makers (SK hynix, Samsung, and Micron). Anthropic and OpenAI, meanwhile, have collectively lost tens of billions of dollars building leading-edge models that, once released, are distilled and commoditized by open source models, primarily from China." 及 "Right now that's compute, but in the fullness of time, whenever we have enough compute, the most valuable place to be in the value chain will be the place that has always been the most valuable: owning the user touchpoint.";(c) 2026-09-21「Frontier Overhangs」:"current model capabilities are 'good enough' for customers to not do whatever is necessary to get access to the cutting edge ... Pure capability no longer translates directly into a moat." 以及 Microsoft Copilot Cowork 可换模型。另:2015「Aggregation Theory」核心表述;2025-11「The Benefits of Bubbles」:光纤因建设者破产近乎免费成就了今天的互联网,以及 "Chips break down and get superseded by better ones; most hyperscalers depreciate them over five years, and that may be generous." 核对每句是否原文、日期、是否被断章(例如 (b) 的"亏损数百亿"是 Thompson 本人观点还是在转述看空论点)。
【G03】Nadella(Microsoft CEO,利益相关方):(a) Dwarkesh 播客 2025-11:"if you're a model company, you may have a winner's curse. You may have done all the hard work, done unbelievable innovation, except it's one copy away from that being commoditized."(b) 同访谈:不想被某一代硬件的大规模部署套牢、不愿做只服务单一模型公司的托管商,愿从 neocloud 租入容量;(c) 2026-06 博文(The Decoder 转述):"If all the value is accrued by only a few models, the political economy will simply not tolerate it." 核对原话、日期,判断 (c) 是否真能读作"转向"(担心模型层拿走全部回报)还是另有语境。
【G04】其他从业者/厂商原话:(a) Benedict Evans 2026-07-09「Ways to think about token pricing」:"whether the foundation models have sustainable pricing power ... or whether they become low-margin commodity infrastructure providers. At the moment, I think every dynamic we can see points to the latter." 以及他称"widely reported"推理毛利 40-50%、"we don't yet know of a network effect or any other winner-takes-all effect";(b) Dario Amodei(Cheeky Pint 播客 2025-08):"If you consider each model to be a company, the model that was trained in 2023 was profitable. You paid $100 million, and then it made $200 million of revenue." 他是否自称这是简化/卡通示例;(c) Meta/Zuckerberg 2024-07-23「Open Source AI Is the Path Forward」:"selling access to AI models isn't our business model"。(d) Joel Spolsky 2002 "Smart companies try to commoditize their products' complements."
` },
  { key: 'B02-history', model: 'sonnet', body: `
【G05】PC 时代利润分布(SEC 10-K 原文):Intel 2000 年净营收 $33,726M、经营利润 $10,395M(30.8%);Microsoft FY2000(截至 2000-06-30)营收 $22,956M、经营利润 $10,937M(47.6%);Dell FY2001(截至 2001-02-02)营收 $31,888M、经营利润 $2,663M(8.4%);Compaq 2000 商用 PC 分部营收 $13,136M、经营利润 $289M(约 2.2%),1999/1998 分别亏 $448M/$46M,消费 PC 分部 $170M(营收 $7,586M),企业计算分部经营利润 $2,140M。自算:Intel+MSFT 约 $21.3B vs Dell+Compaq 两个 PC 分部约 $3.1B,约 7 倍。逐个回 SEC 原文核对,并检查自算(财年错位、Intel 含非 PC 业务)。
【G06】其他历史类比:(a) Odlyzko 2003(ITCom):"Backbone transport is likely to remain a commodity ... backbone revenues will stay low, as the complexity, cost, and revenue and profit opportunities continue to migrate towards the edges of the network.";Odlyzko 1998 测得骨干链路平均利用率约 10-15%、企业长途专线 3-5%(是平均利用率,不是"点亮比例");(b) 英国铁路狂热:Odlyzko(预印本)称到 1850 年底投资者投入约 £250M(近 GDP 一半),损失约三分之一(约 £80M);(c) Paul David 1990「The Dynamo and the Computer」:工厂电气化要到 1920 年代初(首座中心电站开业约四十年后)才影响制造业生产率;(d) Counterpoint:Apple 2022 年以 18% 出货份额拿走全球手机 48% 收入、85% 经营利润;(e) Global Crossing 2002-01-28 申请破产保护。逐条核对出处、数字与限定语。
` },
  { key: 'B03-nvidia-core', model: 'opus', body: `
【G07】NVIDIA 财务(SEC 8-K/10-Q/CFO commentary):(a) Q2 FY27(截至 2026-07-26,2026-08-26 发布)收入 $96,221M(同比 +106%,环比 +18%),数据中心 $89,023M(同比 +117%),GAAP 与 non-GAAP 毛利率均 75.0%,GAAP 经营利润 $63,734M(约 66%),GAAP 净利 $59.7B(含股权投资收益 $7.8B,高于 non-GAAP);(b) 时间序列 GAAP:FY23 收入 $26,974M、毛利率 56.9%、经营利润 $4,224M(约 16%);FY24 $60,922M、72.7%、$32,972M(约 54%);FY25 毛利率 75.0%、经营利润率约 62%;FY26(截至 2026-01-25)收入 $215,938M、数据中心 $193,737M、毛利率 71.1%(含 H20 约 $4.5B 减值)、经营利润 $130,387M(约 60%);(c) 指引:Q3 FY27 毛利率 74%±50bp,Q4 见底约 71-72%,FY28 约 72-73%,原因是内存价格("extreme pricing conditions in memory" 类原话);(d) 供应/产能采购承诺由上季 $119B 增至 $279B,主要用于内存。注意 NVIDIA 自 Q1 FY27 起 non-GAAP 不再剔除 SBC。
【G08】DeepSeek 自然实验:2025-01-27 NVDA 单日下跌约 17%、市值蒸发约 $589B(当时美股单日最大市值损失);NVIDIA 当日声明称 DeepSeek 是 test-time scaling 的例证、推理仍需大量 GPU;此后数据中心季度收入从 $35.6B(Q4 FY25)到 $89.0B(Q2 FY27);市值约 $5.7T(2026-10)。核对数字,并评估"事后支持杰文斯式解读"的归因强度(混杂:Blackwell 换代、主权/AI 云需求、NVIDIA 自身融资支持)。
` },
  { key: 'B04-nvidia-financing', model: 'opus', body: `
【G09】NVIDIA 用资产负债表支撑下游需求(10-Q nvda-20260726 + Q2 FY27 电话会):(a) 客户集中度:Q2 FY27 单一直接客户占总收入 16%;H1 FY27 三家直接客户分别占 16%/15%/13%;上年同季两家 23%/16%;10-Q 称一家 AI 研究与部署公司通过向其客户购买云服务贡献了可观收入;Hyperscale 占数据中心收入约 55%;(b) CFO 称已向前沿实验室投资近 $50B;预计"靠 NVIDIA 资产负债表撑起的实验室需求"约占明年业务四分之一;公司承认外界会称之为循环融资;与六家资管搭建融资平台拟募 $500B+;(c) 与 AI 云签有算力回购承诺共 $36B(一般 6 年);非上市股权投资余额由 $22.3B(2026-01)增至 $51.2B(2026-07)(另一处说法:由 $3.8B(2025-07)到 $47.9B——核对哪个对、是否口径不同);DSO 由 45 天升到 60 天;(d) H1 FY27 GAAP 税前利润 $141.4B 中有 $24.1B 其他收益(主要为股权投资收益净 $23.7B),约 17%;(e) 10-Q 承认 AI 云与模型商缺乏长期合同与投资级融资能力,由 NVIDIA 提供土地、电力、机房与容量担保;新云收入分成结构:take-or-pay/最低收入担保换取底线以上租金分成,自称 "get paid twice"。
【G10】NVIDIA–OpenAI:(a) 2025-09 宣布至多 $100B 投资意向(LOI,非约束);(b) 2026-02 OpenAI 融资中 NVIDIA 出资 $30B(该轮 $122B,投后 $852B);Jensen Huang 2026-03-04 称 $100B "probably not in the cards",对 Anthropic 的 $10B 大概也是最后一笔;(c) 2026-08-17 8-K:NVIDIA 为 OpenAI 在 SB Energy PORTS-Pike 园区约 4.25GW、20 年租约提供残值担保,上限 $105B,换取独家部署 NVIDIA;OpenAI 获满意信用评级后担保终止,OpenAI 同意偿付;公司称该园区每一代部署约 150 万颗 GPU、$150-200B NVIDIA 收入;(d) OpenAI 现有加计划承诺约 12GW NVIDIA 算力。
【G11】芯片层主动商品化互补品:(a) NVIDIA 2026-09 宣布以约 $11.9B 收购 Hugging Face(8-K nvda-20260902),并在文件中称开源模型需求会推动 NVIDIA 产品使用——这件事是否真实发生、金额、原话;(b) Microsoft/NVIDIA 对 Anthropic 投资至多 $15B 同时 Anthropic 承诺 $30B Azure(2025-11)。
` },
  { key: 'B05-memory-custom', model: 'opus', body: `
【G12】利润沿供应链上游分流:(a) Micron FQ4 2026(截至 2026-09-03)收入 $54.23B,GAAP 毛利率 86.8%,GAAP 经营利润率 80.7%;FY26 收入 $133.19B、GAAP 毛利率 80.7%(FY25 39.8%);分部:Cloud Memory BU(含 HBM)毛利 83%、经营利润率 76%,Core Data Center BU 与 Mobile & Client BU 毛利约 90%;(b) SK hynix 2Q26 收入 79.32 万亿韩元、经营利润 60.54 万亿韩元(76%,历史新高);(c) TSMC 2Q26 收入 US$40.20B、毛利率 67.7%、经营利润率 60.3%、HPC 占收入 66%、3Q26 毛利指引 65-67%。核对每个数,检查 Micron 季度与财年口径。
【G13】定制芯片与挑战者:(a) Broadcom Q3 FY26(截至 2026-08-02)AI 半导体收入 $16.7B(同比 +221%)、Q4 指引 $21.7B;全公司收入 $29.6B;non-GAAP 毛利约 75%(环比 -210bp)、Q4 指引约 73%,因 XPU 内存含量高;管理层的 FY27 约 $115B / FY28 约 $230B AI 收入目标;Anthropic 被称为 2027 年最大 XPU 客户;(b) AMD Q2 2026 数据中心收入 $6.7B(+107%)、分部经营利润 $2.1B(约 31%);向 OpenAI 和 Meta 各发行至多 1.6 亿股、行权价 $0.01 的认股权证按里程碑归属,截至 2026-06 零归属;(c) Alphabet 自 2026 Q2 起把 TPU 系统外售作为 Google Cloud 产品收入确认;(d) AWS 自研芯片(Trainium+Graviton)run-rate 超过 $25B、同比三位数增长,Jassy 称未来可能单独出售 Trainium;(e) Anthropic 2026-04-06 与 Google、Broadcom 签数 GW 下一代 TPU 产能(媒体称约 3.5GW),2027 年起上线。
【G14】SemiAnalysis 估算(2025-11-28 "TPUv7: Google Takes a Swing at the King"):(a) 从 Google 自身看 TPUv7 Ironwood 全口径单芯片 TCO 比 GB200 服务器低约 44%;(b) "光是 TPU 的竞争威胁就让 OpenAI 在整个 NVIDIA 机队上省了约 30%";(c) NVIDIA 选择用股权投资而非降价保住实验室份额以免毛利率下降;(d) Anthropic 100 万颗 TPU 中约 40 万由 Broadcom 直售(约 $10B)、60 万经 GCP 租用。核对原文措辞(付费墙内的部分标未验证),检查是否有反驳(如 NVIDIA 回应、其他分析机构给出的不同 TCO)。
` },
  { key: 'B06-cloud-margins-depr', model: 'opus', body: `
【G15】云层分部利润(SEC 原文):(a) AWS 2026Q2 收入 $42.2B(+37%)、分部经营利润 $16.6B(上年 $10.2B)、利润率 39.4%(上年 32.9%),含能源合同衍生品未实现收益,剔除后约 38%;(b) Google Cloud 2026Q2 收入 $24.8B(+82%,含首次确认的 TPU 系统硬件销售)、经营利润 $8.81B(上年 $2.83B)、35.6%(上年 20.7%);Alphabet-level 共享前沿模型研发 Q2 约 -$5.8B 未分摊到 Cloud;(c) 微软 Intelligent Cloud FY26Q4 毛利率 57.1%(上年 60.4%,自算)、经营利润率约 40.6% 持平;Microsoft Cloud 毛利率 FY26 降到 66%、Q4 65%;2026-09 重述后 Azure FY26 $101.9B(FY25 $72.6B,+40%)。
【G16】GPU 租赁毛利:The Information(2025-10-07,经 CNBC 转述)称 Oracle 截至 2025-08 的季度 NVIDIA GPU 租赁收入约 $9 亿、毛利约 14%;Oracle 回应称 6 年期合同全周期毛利 30-40%(另有 35% 说法)。各家 10-Q 未分拆 AI 租赁毛利。核对原报道措辞与 Oracle 回应原话及后续(Oracle 2025-10 分析师日是否给出 AI 基础设施毛利 35% 目标)。
【G17】折旧年限:(a) 微软 2022-07 把服务器与网络设备年限从 4 年延到 6 年,估计 FY23 经营利润 +$3.7B;FY27 起把数据中心建筑年限从 15 年延到 25 年;(b) Alphabet 2023 把服务器延到 6 年;(c) Meta 自 2025-01-01 起把多数服务器与网络资产延到 5.5 年,2025 年少计折旧 $2.92B、净利 +$2.59B;(d) Amazon 自 2025-01 起把部分服务器从 6 年缩到 5 年(理由:AI/ML 迭代加快),2025 年折旧增加约 $1.4B,2024Q4 另计提约 $920M 提前报废;(e) CoreWeave GPU 按 6 年(2023 年起由 5 年延长);Nebius 2026 年起 4→5 年;(f) Michael Burry 2025-11 估计超大云 2026-2028 年少计折旧 $176B(投资人估算)。逐个核对 10-K 原文数字。
` },
  { key: 'B07-cloud-capex-rpo', model: 'opus', body: `
【G18】capex 与自由现金流(SEC 原文/电话会):(a) 微软 FY26 现金 capex $115.9B(FY25 $64.6B),经营现金流 $182.9B(占比 63%),FCF 约 $67B;Q4 含融资租赁 capex $41B、约 2/3 为短寿命资产;日历 2026 指引约 $175B(由约 $190B 下调,因融资租赁转经营租赁);尚未起租租赁 $329.1B;(b) Alphabet 2026 capex 指引 $195-205B(2025 实际 $91.4B);2026Q2 capex $44.9B > 经营现金流 $39.1B,FCF -$5.9B;6 月宣布 $80B 股权融资(Q2 到账净额 $49.6B),发债净额 $20.3B;(c) Amazon 截至 2026Q2 TTM FCF -$7.6B(净 capex $169.0B > OCF $161.4B);2026 现金 capex 约 $220B;(d) Meta 2026 capex 指引 $130-145B(2025 约 $72.2B),Q2 FCF $0.78B(上年 $8.5B),未起租数据中心租赁约 $279B;(e) Oracle FY26(截至 2026-05)capex $55.7B、OCF $32.0B、FCF -$23.7B;Q1 FY27(截至 2026-08-31)收入 $19.3B、capex $28.5B、FCF -$5.4B、ATM 发股 $20B;OCF 中含 $11.4B 带重大融资成分的客户预付款;$288B 未起租租约。逐个核对,特别是 Alphabet 发股这类不寻常事件。
【G19】积压订单(RPO)与集中度:(a) 微软商业 RPO $678B(+84%),剔除 OpenAI 仅 +25%,约 30% 在 12 个月内确认,CFO 称环比增长全部来自前沿模型公司以外客户(核对原话);(b) Alphabet 收入积压 $519.5B,其中 Google Cloud $513.9B,略超一半 24 个月内确认,2026Q1 起口径含 1 年以内合同;(c) AWS 未确认长期合同承诺约 $496B、加权剩余 6.4 年,包含 OpenAI 在 $38B 之上 8 年追加 $100B、Anthropic 10 年追加 $100B+;(d) Oracle RPO $664B(上年 $455B),约 13% 在 12 个月内确认;(e) CoreWeave RPO $103.7B;合计超过 $2.4T。核对每个数字与"集中于 OpenAI/Anthropic"的程度。
` },
  { key: 'B08-equity-flows', model: 'opus', body: `
【G20】模型层估值记入上游 GAAP 利润:(a) Amazon 2026Q2 经营利润 $27.5B、其他收益(非经营)$53.4B、税前 $80.9B;私营公司股权上调 $50.5B 主要来自 Anthropic 无投票权优先股的可观察价格调整(H1 合计 $62.8B),约为同季 AWS 经营利润 $16.6B 的 3 倍;(b) Alphabet 2026Q2 其他收益约 $98.0B,其中非上市股权未实现收益 $77.5B(公司仅称 "a private company",未具名),另持有 SpaceX 股份;当季净利 $112.2B、经营利润 $40.8B;(c) 微软 FY26 对 OpenAI 权益法净收益 $6.5B(主要为稀释收益;FY25 净亏 $4.8B),FY26Q4 Anthropic 投资收益 $3.2B,non-GAAP 剔除 OpenAI 影响。核对数字;判断 Alphabet 那笔是否可合理推断为 Anthropic(不可具名就写未具名)。
【G21】模型层 ↔ 云层的双向资金:(a) 微软 FY26 10-K:来自 OpenAI 商业安排的收入(含收入分成)$24.1B,应收 $6.0B,已出资 $11.9B(承诺 $13.0B),按转换后口径持股约 25-27%;对比 OpenAI 2025 日历年确认收入约 $13.1B(媒体口径)——两者财年不同、$24.1B 含分成,能否说"微软从 OpenAI 收的钱超过 OpenAI 一年收入"?(b) 2025-10-28 重组:微软持有 OpenAI Group PBC 约 27%(约 $135B),OpenAI 追加 $250B Azure 承诺,微软放弃优先购买权;(c) 2026-04-27 再修订:OpenAI 向微软的收入分成持续到 2030 年、比例不变但设总上限,微软不再向 OpenAI 付分成,IP 许可改为非独占;(d) Amazon 对 OpenAI $50B:H1 投 $28.7B Series C、6-30 后付清 $21.3B;AWS-OpenAI $38B 扩大 $100B/8 年;(e) Amazon–Anthropic:2023-2025 投 $8B,2026Q2 再投 $10B,另设至多 $20B 融资额度按 AWS 算力交付里程碑释放;AWS-Anthropic 承诺再扩 $100B+/10 年。
` },
  { key: 'B09-neocloud-power', model: 'opus', body: `
【G22】CoreWeave(SEC 8-K/10-Q/电话会):Q2 2026 收入 $2,575M(+112%);GAAP 经营亏损 $49M;净利息支出 $640M;GAAP 净亏损 $626M;调整后 EBITDA $1,510M(59%);调整后经营利润 $128M(5%,上年 16%);单季 D&A $1,393M(收入 54%);有息债务约 $35.1B、经营租赁负债约 $16.3B、股东权益 $5.0B;2025 全年微软占收入 67%,Q2 2026 前三大客户 36%/26%/10%;Q3 利息指引 $860-940M 高于调整后经营利润指引 $200-260M;2026 capex 指引 $35-39B(约收入 3 倍);7 月全 SKU 提价约 25%;A100 合同续到 2029 年;存量票据利率 8.5%-9.75%;NVIDIA 2026-01 认购 $2.0B。
【G23】GPU 租价时序:H100 云租价 2024 年初约 $8/h → 2025-10 低点约 $1.70/h(SemiAnalysis 一年期合约价)→ 2026-03 约 $2.35 → 2026 年 9-10 月约 $2.8-3.3(核对最新数与来源);Silicon Data H100 指数 2025-12 至 2026-01 由 $2.00 升到 $2.20;不同指数口径(按需/合约/挂牌价)差异。核对"约 80% 下跌后反弹 60-90%"是否成立。
【G24】电力与数据中心物业:(a) PJM 2028/29 容量拍卖以上限 $325/MW-day 出清(2024/25 为 $28.92),比可靠性标准少 6,831 MW,总额约 $16.4B,连续三次撞上限;(b) Vistra Q2 2026 Ongoing Ops 调整后 EBITDA $1,767M(+31%);(c) Epoch AI(2026-05-14):1 GW GB200 数据中心年化 TCO $8.5B,服务器 $5B(60%),能源仅 $0.6B(约 7%,电价 8.34 美分/kWh),IT 寿命 3 年时 TCO 升到 $12B;(d) 宾州州长 Shapiro 2026-01 争取把 PJM 价格上限再延两次拍卖、称节省约 $27B;(e) Digital Realty Q2 2026 续约租金 cash +25.4%,>1MW 续约 cash 价差 66.7%;(f) GE Vernova 燃气设备积压+槽位预订 116 GW,产能 2026Q3 20GW/年→2030 30GW/年;(g) LBNL Queued Up 2026:2025 年投运项目申请到投运中位数超 5 年,排队约 2,061 GW;(h) ERCOT 2026-08-03 暂停 Batch Zero 分类通知(德州州长要求核验大负荷)。
` },
  { key: 'B10-model-labs', model: 'opus', body: `
【G25】前沿实验室收入(厂商口径/媒体转述,注意 run-rate vs 确认收入):(a) Anthropic 官方:run-rate 2026-04 超 $30B、2026-05 上旬突破 $47B(Series H $65B、投后 $965B);2026-07 末超 $65B(TechCrunch 2026-08-17);(b) Anthropic 确认收入:2025 全年约 $4.6B(2024 约 $0.39B)、2026Q1 $4.73B、Q2 >$11.5B——来自泄露的保密 S-1(Fortune 2026-09-29),EDGAR 未见公开版本;(c) WSJ 2026-08:OpenAI 2026 确认收入 Q1 $5.7B、Q2 $6.7B;Anthropic Q2 $11.6B,季度确认收入首次超过 OpenAI;(d) Axios 2026-09-29:OpenAI ARR 接近 $70B;CFO Friar 2026-08-14 称企业收入已超过消费者、总 run-rate 约 $40B、广告 run-rate 接近 $1B——两个 run-rate 数字是否冲突;(e) OpenAI 2025 确认收入约 $13.1B。
【G26】前沿实验室利润与承诺(全部为媒体转述/泄露,找到最原始报道):(a) OpenAI 2025 调整后毛利 33%(2024 年 40%,原目标 46%)(The Information);(b) Anthropic 2025 毛利约 40%(原预期 50%),2024 年 -94%(The Information 2026-01);(c) FT/Reuters 2026-09:Anthropic 毛利超过 80% 但剔除渠道分成和训练成本;连续第二个季度 adjusted 经营利润为正;(d) 泄露 S-1:Anthropic 2025 经营亏损 $8.06B(2024 $2.98B)、GAAP 净亏约 $42B(其中约 $34B 非现金重估)、未来云/算力义务 $518B、两大客户占 2025 收入近四分之一;(e) OpenAI 经营亏损 2026Q1 $9.3B、Q2 $12.3B(含 SBC);(f) FT 2026-09:OpenAI 预测 2026-2030 累计负 FCF $278B(5 月版 $305B),2026 确认收入 $36B → 2030 $350B;(g) OpenAI 算力支出口径 $1.4T(Altman)→ 2030 前约 $600B(2026-02)→ $856B(2026-07 推介)。
` },
  { key: 'B11-prices-open-gap', model: 'opus', body: `
【G27】两条价格曲线:(a) Epoch AI 2025-03「LLM inference price trends」:达到给定基准分的价格年降 9×-900×(中位约 50×),GPT-4 级 GPQA 表现年降约 40×;(b) Epoch 2026-09-22「The plunging price of thought」:给定性能成本自 2023 年起每季降约 47%(约 13×/年),刚成为 SOTA 时最快(66%/季)、两年后降速减半;(c) MIT FutureTech 预印本(arXiv 2511.23455):给定性能价格年降 5-10×,但运行前沿级模型的成本年升 3-18×;(d) OpenAI 官方 API 旗舰价(每百万 token 输入/输出):GPT-5 $1.25/$10 → gpt-5.4 $2.5/$15 → gpt-5.5 $5/$30,gpt-5.5-pro $30/$180;Anthropic 顶档 $10/$50;(e) a16z「LLMflation」2024-11:同等能力成本每年降 10×。核对数字与定义(固定能力 vs 前沿)。
【G28】开源 vs 闭源:(a) Epoch 2026-05-29:最强开源权重模型落后闭源前沿平均约 4 个月(ECI 差约 8 点),比 2025-10 约 3 个月略扩大;(b) Linux Foundation 工作论文 2025-11(OpenRouter 数据):闭源约占 80% 用量、96% 收入,平均价格为开源 6 倍,未实现节省约 $24.8B/年;(c) Menlo Ventures 2025-12 企业调查(495 人):企业 LLM API 支出份额 Anthropic 40%、OpenAI 27%、Google 21%,开源份额从 19% 降到 11%(Menlo 是 Anthropic 投资方);企业 GenAI 支出 $37B,其中应用层 $19B,初创公司拿 63%。
【G29】收入缺口测算:(a) Sequoia/David Cahn 2024-06「AI's $600B Question」算法:NVIDIA 数据中心 run-rate ×2(GPU 约占数据中心 TCO 一半)×2(终端用户 50% 毛利);(b) Cahn 2026-07「AI's $1.5T Question」:$1.5T 对应 2026 单年 capex 所需终身终端收入(约 $750B ×2),$3T 是 ChatGPT 以来累计;(c) Bain 2025-09:2030 年需约 $2T 年收入支撑约 $500B 年 capex,即便算上 AI 节省仍差 $800B;(d) Bain 2026-09-29 技术报告:2031 年 AI 基建年支出可达 $1.5T,按 capex 约占收入 25% 需约 $6T 年收入,现有消费+企业 AI 只能贡献 $1.2-1.8T,约 $4.2T 需来自新品类;(e) 从业者估算(Tailwinds/Agrawal 2026-04):半导体占 AI 生态约 79% 毛利美元;(f) a16z 2023-01:基础设施厂商拿走流经技术栈的大部分资金,生成式 AI 收入 10-20% 流向云。
` },
  { key: 'B12-apps-aggregators', model: 'opus', body: `
【G30】AI 原生应用层:(a) Bessemer State of AI 2025:约 10 家 "Supernova" 公司平均毛利约 25%,"Shooting Stars" 约 60%;(b) Cursor:截至 2026-01 的季度毛利 -23%(The Information,二手转述),2026-04 "微弱正毛利"、仅企业客户正毛利(TechCrunch 2026-04-17);Composer 2 基于 Moonshot 开源 Kimi K2.5 继续预训练+RL,联创 Aman Sanger 公开确认;Cursor 被 SpaceX 以约 $60B(约 15 倍 run-rate,SpaceX 股票支付)收购——核实这件事是否真实发生;(c) Anthropic 2025-06 切断 Windsurf 对 Claude 3.x 的大部分一手访问(提前不到五天);Windsurf 后被拆给 Google($2.4B 授权+人才)和 Cognition;(d) Anthropic 2026-01 起拒绝第三方工具使用 Claude 订阅 OAuth,2026-02-19 写进条款,2026-04-04 起订阅不再覆盖第三方 harness;GitHub Copilot 改按用量计费称原有模式 "no longer sustainable";(e) Anthropic 官方 2026-02-12:Claude Code run-rate 超过 $2.5B、企业占一半以上,同期公司总 run-rate $14B;(f) Perplexity 约 60% 毛利剔除免费用户推理成本。
【G31】握有分发的现有巨头:(a) Alphabet 2026Q2 Search & other $63.27B(+17%),Google Services 经营利润 $39.54B(约 41.8%,上年约 40.1%);AI Mode 月活超 10 亿;(b) Meta 2026Q2 广告收入 $59.4B(+27%)、经营利润 $18.78B 同比 -8%、FoA 经营利润率 53%→39%,成本驱动明确包括第三方云服务与第三方 AI token 成本(核对 10-Q 原文措辞);(c) 微软 FY26Q4 M365 Copilot 付费席位超 3000 万;Productivity & Business Processes 经营利润率约 57.9%;(d) Apple FY26Q3 Services 收入 $30.74B、毛利率约 75.6%,前九个月 capex $6.80B(上年同期 $9.47B);2026-01-12 Apple-Google 联合声明下一代 Apple Foundation Models 基于 Gemini,彭博称 Apple 年付约 $1B;对比 Google 2022 年为默认搜索付 Apple 约 $20B;(e) Salesforce Q2 FY27 Agentforce ARR 超 $1.5B(+240%,口径扩大)、总营收 $11.35B(+11%)。
` },
]

phase('Verify')
const jobs = []
for (const b of BATCHES) {
  for (let v = 0; v < 3; v++) {
    jobs.push(() => agent(HEAD + LENSES[v] + '\n\n以下是你这批要验证的组:\n' + b.body, {
      label: `${b.key}-v${v + 1}`, phase: 'Verify', schema: SCHEMA, model: b.model,
    }).then(r => r ? { ...r, batch: b.key, voter: v + 1 } : null))
  }
}
const results = await parallel(jobs)
log(`完成 ${results.filter(Boolean).length}/${jobs.length} 票`)
return results.filter(Boolean)
