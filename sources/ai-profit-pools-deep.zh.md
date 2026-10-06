# AI 价值链的利润池会落在哪一层?——五层账本与一个转圈的资金环(深入版)

> 方法学说明:本文承重论断分为 31 组,每组派 3 个独立验证 agent(共 93 票),要求「尽力反驳」:逐字回到 10-K/10-Q/8-K、财报电话会逐字稿、官方定价页与论文原文,核对分子、分母、时间窗、财年、GAAP 与 non-GAAP、run-rate 与确认收入、承诺额与落地额。结果:31 组没有一组三票都判「原样成立」(只有 2 组各有一到两票判成立),子论断层面 70 余处被判死或被禁止按原稿形式使用。另对 3 条「单一来源承担关键结论」的实证加做反证搜索席与方法学审计席(共 6 席):电费在 AI 数据中心总成本中的占比升级为多源证实,但「所以电力层租金薄」的推论被方法席否决;「两条方向相反的价格曲线」被判方向存争,改写为口径更窄的版本;「Anthropic 季度收入超过 OpenAI」升级为多源,但「利润已集中到一家」被降级。证据分级:【多源】≥2 个独立来源同向;【单源已核】一手文件可回溯;【方向存争】独立来源矛盾;【厂商口径】利益相关方自述,方向可参考、程度不承重;【未验证】。前沿实验室均未上市,它们的财务数字全部来自泄露文件或媒体转述,一律不承重。所有数字截至 2026 年 10 月初(最新季报:NVIDIA 截至 2026-07-26 的 Q2 FY27;云厂商 2026 年第二季度;Micron 截至 2026-09-03 的 FQ4 FY26)。

## 0. 先选尺子:用什么量「利润落在哪」

「做模型的是不是在给人做嫁衣」这个问题,有四套流行答案:卖铲子的赢(芯片与基建);模型终将商品化(价格每年降一个数量级、开源追平);聚合者通吃(握住用户的人把上游压成商品);前沿实验室赢家通吃。再加一个较新的版本:电力和电网接入才是最持久的稀缺。四套答案互相矛盾,却都能找到数字支撑。原因之一是它们用的尺子不同。

本文先把尺子定下来,后面每一层都用同一把:

- **用分部经营利润,不用净利润。** 2026 年第二季度,Amazon 的税前利润里有约 $505 亿来自对 Anthropic 优先股的公允价值上调,Alphabet 单季净利 $1,122 亿是其经营利润的 2.75 倍。净利润在这一年被前沿实验室的估值重估严重扭曲,用它比较各层,等于把模型层的估值重复计进云层和芯片层(第 10 节专门讨论这一点)。
- **用确认收入,不用 run-rate。** run-rate 是「最近一个月收入 ×12」。Anthropic 2025 年确认收入约 $46 亿,而年末 run-rate 约 $90 亿;OpenAI 7 月的 run-rate 约 $400 亿,它自己预测的 2026 全年收入是 $360 亿,上半年实际确认约 $124 亿。两种口径差一倍是常态。
- **区分承诺额与落地额。** 云厂商的合同积压、实验室的算力承诺、芯片商的担保上限,都是多年名义值,不是已经发生的现金。
- **区分「当下的利润分布」与「长期的利润落点」。** 前者可以从财报里读;后者只能给情景和可检验的信号,不给点预测。

本文的结论分两部分。当下的分布相当清楚:利润压倒性地在芯片与存储层,而且芯片层内部的稀缺租金正在向存储迁移。长期落点则被一个结构性事实搅乱:五层之间的资金在转圈,上游用股权和信用为模型层托底,模型层的估值又以账面收益回到上游的利润表。「哪一层赚钱」因此有一部分变成了「谁在承担模型层的信用风险」。

## 1. 两种利润迁移理论,以及一位分析师一年里的三次改口

**Christensen 的「利润守恒」。** Clayton Christensen 在 HBR 2004 年 2 月《Breakthrough Ideas for 2004》的一页短文里写道:「When attractive profits disappear at one stage in the value chain because a product becomes modular and commoditized, the opportunity to earn attractive profits with proprietary products will usually emerge at an adjacent stage.」【单源已核】同文他自称这「still a hypothesis」,而且因篇幅所限写得过于简化;这个名字是 Tensilica CEO Chris Rowen 提议的。网上广泛流传的那个不带「modular and」的版本,是 HBR 编辑写的目录摘要,不是他的原话。思想更早见于他与 Raynor 的《The Innovator's Solution》(2003):当产品性能「还不够好」(存在 performance gap)时,「firms that build their products around proprietary, interdependent architectures enjoy an important competitive advantage against competitors whose product architectures are modular」;性能过剩之后,架构转向模块化,利润迁往客户仍不满意的环节。

这套理论用在 AI 上,推论取决于前提:如果前沿模型的能力对客户来说仍「不够好」,那么把模型与产品整合在一起的前沿实验室应该拿走利润;如果已经「够好」,模型会模块化,利润迁往相邻环节。

**Thompson 的聚合理论。** Ben Thompson 2015 年的「Aggregation Theory」认为,互联网让分发和交易成本趋零,握住用户关系的一方可以把模块化的供给方压成商品。按这套理论,利润的终点是用户触点,不是供给侧的任何一层。与它相关但不是同一命题的,是 Joel Spolsky 2002 年的那句「Smart companies try to commoditize their products' complements」:你若卖 A,就希望它的互补品 B 便宜。

**Thompson 本人在 2026 年改了三次口。** 这三次改口本身就是这个问题难度的读数:

- 2026-03-16《Agents Over Bubbles》:「profits flow away from modular parts of the value chain — which are commoditized — and flow towards integrated parts of the value chain, which are differentiated」。他的条件式推论是:如果 agent 需要模型与 harness(调度模型干活的外壳程序)紧密整合,那么 Anthropic 与 OpenAI「are actually poised to be significantly more profitable than it might have seemed as recently as late last year」。他没有把 Google 算进去,理由是它还没有一个有吸引力的 harness。这是预期,不是已实现利润【单源已核】。
- 2026-06-15《Anthropic's Safety Superpower》:「the biggest beneficiaries have been Nvidia, TSMC, and the memory makers (SK hynix, Samsung, and Micron)」。他以未注出处的方式称两家实验室「have collectively lost tens of billions of dollars」,并把「实验室永远收不回成本」称为「the bear case for the labs ... and I think it's a legitimate one」;接着写道:「Right now that's compute, but in the fullness of time, whenever we have enough compute, the most valuable place to be in the value chain will be the place that has always been the most valuable: owning the user touchpoint.」全文的主旨是实验室必须去占用户触点,以反制这个熊市论点【单源已核】。
- 2026-09-21《Frontier Overhangs》:他从一个事件出发——客户愿意根据数据保留政策而不是纯性能来选模型——推论「current model capabilities are “good enough” for customers to not do whatever is necessary to get access to the cutting edge」,并写下「Pure capability no longer translates directly into a moat」。同文他也写明这并不意味着新能力没人要,并报道微软的 Copilot Cowork 现在可以选择底层模型,即 harness 与模型可以分开。这是对 3 月「整合者赚钱」论的部分修正【单源已核;单一事件推论】。

**利益相关方的说法要按利益位置读。** 微软 CEO Satya Nadella 2025-11 在 Dwarkesh 播客上说:「I can make the argument that if you're a model company, you may have a winner's curse ... it's one copy away from that being commoditized」,紧接着是「So I think the argument can be made both ways」【厂商口径】。微软卖 Azure、卖 Copilot、自研模型、又是 OpenAI 股东,模型越可替换,它的位置越好。Anthropic CEO Dario Amodei 2025-08 在 Cheeky Pint 播客上把「每个模型当成一家公司」:2023 年训练花 $1 亿、带来 $2 亿收入,所以单个模型是盈利的。他自称这是一个「cartoonish cartoon example」,不是公司的真实财务【厂商口径】。Benedict Evans 2026-07-09 判断模型更可能成为「low-margin commodity infrastructure providers」,「At the moment, I think every dynamic we can see points to the latter」,下一句是「Clearly, the situation today is transitory」;他还写道,目前「we don't yet know of a network effect or any other winner-takes-all effect」能让一家持续领先【单源已核】。

一个常被引用的例子已经过时。Meta 2024-07 的「selling access to AI models isn't our business model」是开源 Llama 时期的立场;此后 Meta 推出了 Llama API,并在 2026-04 发布了不开放权重的 Muse Spark。它不能再当作「把互补品商品化」的现行例证。现行例证换了一家:NVIDIA 2026-09-02 签署最终协议,拟以约 $119 亿收购 Hugging Face(另有至多约 $10 亿留任股权计划,预计 2027 年上半年交割),8-K 的风险因素里写着「Demand for open-source foundation models and applications based on them promotes the use of our products worldwide」【单源已核】。卖铲子的人希望模型便宜。

两套理论对 AI 给出的答案相反,但它们共同指向两个可以观测的量:**客户是否认为前沿能力已经「够好」**,以及**物理瓶颈(算力、存储、电力)是否解除**。第 11 节用这两个量搭情景。

## 2. 历史类比:谁拿走了利润,以及这次哪里不一样

**PC 时代:组件和平台拿走了约 7 倍的利润。** 按 SEC 10-K 原文:Intel 2000 日历年净营收 $337.26 亿、经营利润 $103.95 亿(30.8%,合并口径,含非 PC 业务);微软 FY2000(截至 2000-06-30)营收 $229.56 亿、经营利润 $109.37 亿(47.6%,全公司);Dell FY2001(截至 2001-02-02)营收 $318.88 亿、经营利润 $26.63 亿(8.4%,全公司,含服务器与服务);Compaq 2000 年商用 PC 分部经营利润 $2.89 亿(营收 $131.36 亿,约 2.2%,未摊公司费用前;1998、1999 两年该分部亏损),消费 PC 分部 $1.70 亿。Intel 加微软约 $213 亿,Dell 全公司加 Compaq 两个 PC 分部约 $31 亿,比值约 6.8 倍【多源;算术】。这不是严格同口径的比较:财年最多错开约 8 个月,Intel 含非 PC 业务,Dell 是全公司;换口径后比值在 6.2 到 7.7 倍之间。按 Compaq 下一年 10-K 把公司费用摊进分部后的重述,其 2000 年 PC 加消费业务只剩 $1.45 亿(0.7%)。2000 年还是 PC 周期的高点。方向是稳的:模块化的整机层很薄,掌握专有标准的组件与平台层很厚。

**光纤与铁路:建设者承担风险,使用者拿走剩余。** Andrew Odlyzko 2003 年预测:「Backbone transport is likely to remain a commodity ... It is probable that backbone revenues will stay low, as the complexity, cost, and revenue and profit opportunities continue to migrate towards the edges of the network.」【单源已核;是预测,带概率语气】Global Crossing 2002-01-28 申请破产保护(Chapter 11 重整,不是清算)。Thompson 2025-11 写道,这些光纤「basically existed for free — because the companies who built it went bankrupt」,成就了今天几乎免费的互联网。英国铁路狂热中,到 1850 年底投资者累计投入约 £2.5 亿,接近当年 GDP 的一半;Odlyzko 估计损失约三分之一、约 £8,000 万,这是他的估算而非实测,另有学者认为扩张期的融资对投资者而言是理性的【方向存争】。Paul David 1990 年的研究发现,工厂电气化要到 1920 年代初、首座中央电站开业约四十年后,才影响到制造业生产率——收益最终落在重组了生产流程的使用者那里,但他讨论的是生产率,不是利润分配。

**智能手机:一家整合者拿走了大部分利润,但那是峰值。** Counterpoint 估计 Apple 2022 年以 18% 的出货份额拿到全球手机 48% 的收入、85% 的经营利润,三项都是其历史最高;此后收入份额回落到约 40%–46%【厂商口径,研究机构估算】。

**这次哪里不一样:GPU 不会留下廉价遗产。** 光纤和铁路的「建设者破产、使用者受益」依赖一个条件:资产寿命长,破产后能被后来者以远低于建设成本的价格接手,继续用几十年。Thompson 在同一篇文章里指出了 AI 的不同:「Chips break down and get superseded by better ones; most hyperscalers depreciate them over five years, and that may be generous.」【单源已核】GPU 的会计寿命是 5 到 6 年,经济寿命可能更短。如果这一轮建设过度,留下来能被廉价接手的是晶圆厂、电力设施、已接入电网的场地和机房外壳,不是算力本身。历史类比在这里最可能失效。

## 3. 芯片层:当下最厚,但稀缺租金在往存储走

**NVIDIA 的账。** 按 8-K(2026-08-26):截至 2026-07-26 的 Q2 FY27,收入 $962.21 亿(同比 +106%),数据中心 $890.23 亿(同比 +117%),GAAP 毛利率 75.0%,GAAP 经营利润 $637.34 亿,经营利润率 66.2%【单源已核】。GAAP 年度序列:FY23 毛利率 56.9%、经营利润率 15.7%(含约 $13.5 亿 Arm 收购终止费);FY24 72.7%、54.1%;FY25 75.0%、62.4%;FY26 收入 $2,159.38 亿、71.1%、60.4%。FY26 毛利率下滑的原因有两个:从 Hopper 板卡转向 Blackwell 整机方案,以及 H20 超额库存与采购义务计提(全年净额约 $43 亿)【多源】。NVIDIA 自 FY27 第一季起 non-GAAP 不再剔除股权激励,旧报道里的 non-GAAP 毛利率与新口径不能直接比,所以这里一律用 GAAP。

**稀缺租金在上移。** 存储厂的利润率已经超过 NVIDIA。Micron 截至 2026-09-03 的 FQ4 FY26(14 周),收入 $542.3 亿,GAAP 毛利率 86.8%,GAAP 经营利润率 80.7%;FY26 全年 GAAP 毛利率 80.7%(上一财年 39.8%),全年经营利润率 74.6%【多源】。SK hynix 2026 年第二季度经营利润率 76%,连续第五个季度创纪录。TSMC 同季毛利率 67.7%、经营利润率 60.3%。

最厚的不是 HBM。Micron 分部数据显示,主要服务超大规模云、含 HBM 的 Cloud Memory 事业部毛利 83%,反而低于核心数据中心事业部和手机与 PC 事业部的约 90%;管理层称 HBM 占比上升拉低了前者的毛利,并计划在 2027 年大幅上调 HBM 定价,以「narrow the profitability gap between HBM and conventional DRAM」【单源已核】。AI 需求造成的是整个存储市场的缺货涨价,通用 DRAM 和 NAND 吃到的租金比 HBM 本身还厚。

NVIDIA 的报表在印证这一点。它在 8-K 里正式给出的 Q3 FY27 毛利率指引是 74.0%±0.5 个百分点;CFO Colette Kress 在电话会上口头补充,因为「we are experiencing extreme pricing conditions in memory」,毛利率将在 Q4 降到 71%–72% 见底,再于 FY28 回到 72%–73%,前提是「as executed price increases take effect in Q1」——也就是 NVIDIA 自己的提价【厂商口径;仅电话会,不在 SEC 文件中】。它的供应与产能采购承诺从上一季的 $1,190 亿增至 $2,790 亿,「primarily related to the procurement of memory」,分布在多个财年【单源已核】。存储涨价正在压 NVIDIA 的毛利,而 NVIDIA 打算把一部分转嫁给下游。所以这次租金迁移可能是暂时的。

**定制芯片没有消灭芯片层的利润,而是在层内重新分配。** Broadcom 截至 2026-08-02 的季度,AI 半导体收入 $167 亿(同比 +221%),下季指引 $217 亿;non-GAAP 毛利率约 75%,环比降 2.1 个百分点,原因是 AI 收入占比上升;下季指引降到约 73%,原因是内存含量更高的定制芯片占比上升【单源已核】。管理层称 Anthropic 将在 2027 年成为其最大的定制芯片客户。AMD 数据中心分部 2026 年第二季度经营利润率约 31%,并向 OpenAI 和 Meta 各发行至多 1.6 亿股、行权价 $0.01 的认股权证,按 GPU 采购里程碑与 AMD 股价目标分档归属;截至 2026-06-27 零归属【多源】。挑战者在用股权换订单。

关于自研芯片的两个常见数字要按口径读。Amazon 称其芯片业务(Trainium、Graviton、Nitro)年化 run-rate 超过 $250 亿,这是 AWS 内部按 EC2 用量的归因,不是对外销售收入,不能与 NVIDIA 或 Broadcom 的芯片收入并列【厂商口径】。SemiAnalysis 2025-11 估算,按 Google 自己的采购价,TPUv7 单芯片全口径成本比 GB200 服务器低约 44%;外部客户经 Google Cloud 租用,仍可便宜至多约 30%;并估算 OpenAI 尚未部署 TPU,就已凭竞争威胁在整个 NVIDIA 机队上拿到约 30% 的有效成本改善。它还认为 NVIDIA 选择用股权投资而不是降价来守住前沿实验室,以免毛利率下滑。这些都是分析机构的模型估算和解读,NVIDIA 公开反驳过【单源;方向存争】。Alphabet 自 2026 年第二季度起开始确认有限数量的 TPU 系统外售收入,金额未披露,绝大部分将在 2027 年确认【单源已核】。

**芯片层在总毛利里的份额:很高,但在下降。** 投资人 Apoorv Agrawal 2026-04 的自建估算显示,半导体约占 AI 生态毛利美元的 79%(基础设施约 $400 亿、应用约 $200 亿、半导体约 $2,250 亿),两年前是 87%【单源已核;从业者自估,应用层用 run-rate,时间窗不齐】。方向是芯片层的份额在被稀释,不是继续扩大。

**DeepSeek 自然实验说明不了需求弹性。** 2025-01-27,DeepSeek-R1 引发抛售,NVIDIA 单日下跌约 17%,市值蒸发约 $5,900 亿,为当时美股单家公司单日最大市值损失【多源】。此后其数据中心季度收入从 $355.8 亿(Q4 FY25)涨到 $890.2 亿(Q2 FY27)。这个走势与「效率提升带来更多需求」的杰文斯式解读相容,但不构成证据:收入是价格乘以数量,管理层自己说每 GW 的收入机会从约 $180 亿涨到 Blackwell 的 $250 亿、再到 Vera Rubin 的 $400 亿,大块增长来自单位价值;超大云厂商的资本开支在 DeepSeek 之前就已锁定;NVIDIA 自己还在为需求融资(第 10 节)。没有反事实,也没有价格弹性数据【未验证因果】。

## 4. 云层:分部利润率高,但建立在三个假设上

**分部经营利润率在 35%–41% 之间。** AWS 2026 年第二季度收入 $422 亿(+37%),分部经营利润 $166 亿,利润率 39.4%(上年 32.9%),其中含 $5.51 亿能源合同衍生品未实现收益,剔除后约 38%–39%【单源已核】。Google Cloud 收入 $248 亿(+82%),经营利润 $88.1 亿,利润率 35.6%(上年 20.7%);但 +82% 不是有机增长,里面有首次确认的 TPU 系统硬件收入和 2026-03 并表的 Wiz【单源已核】。微软 Intelligent Cloud FY26 第四季度(截至 2026-06-30)经营利润率 40.6%,与上年持平;毛利率从 60.4% 降到 57.1%(自算);Microsoft Cloud 全年毛利率降到 66%,第四季度 65%,CFO 称原因是销售结构向 Azure 转移【单源已核】。AI 基础设施在压毛利,经营利润率靠费用杠杆守住。

**第一个假设:研发不摊进分部。** Alphabet 本季有 $57.9 亿「Alphabet-level activities」不分摊到任何分部,10-Q 称其「primarily」是共享 AI 研发(通用模型的人员与算力),另含公司共享成本等【单源已核】。Google Cloud 的 35.6% 和 Google Services 的 41.8%,都没有承担训练前沿模型的成本。

**第二个假设:GPU 能用 5 到 6 年。** 微软 2022-07 把服务器与网络设备年限从 4 年延到 6 年(当时预计 FY23 经营利润 +$37 亿);Alphabet 2023 年延到 6 年(当年实际少计折旧 $39 亿);Meta 自 2025 年起延到 5.5 年(按 2024 年底前已投用资产测算,2025 年折旧因此减少 $29.2 亿);Amazon 方向相反,2024 年先延到 6 年,2025 年又以「increased pace of technology development, particularly in the area of artificial intelligence and machine learning」为由把一部分服务器缩回 5 年,2025 年折旧因此增加 $14 亿(2025 10-K 实际值)【多源;SEC 一手】。Michael Burry 2025-11 估计超大云厂商 2026–2028 年少计折旧约 $1,760 亿,他持有空头头寸,这个数字无法用财报复核【未验证;利益相关方】。云层的利润率有一部分取决于这个会计假设,而 GPU 的经济寿命在租价反弹期和下跌期会给出不同答案(第 5 节)。

**第三个假设:AI 租赁的毛利会爬上去。** 关于 GPU 出租业务本身的毛利,唯一的具体数字来自媒体。The Information 援引 Oracle 内部文件报道,截至 2025-08 的三个月,Oracle 的 NVIDIA 云业务销售约 $9 亿、毛利率约 14%(经 CNBC 转述)【单源;媒体】。9 天后的分析师日上,Oracle 给出 AI 基础设施「经调整毛利率 30%–40%」,这是合同全周期的预测目标,不是当期实现值,也不是对报道的回应【厂商口径】。截至 2026 年 9 月的季报仍未出现这个毛利的实际值;Oracle「Cloud and software」分部利润率(只含直接成本)从上年同期 59.6% 降到 54.5%【单源已核】。

**现金流:不能笼统说「转负」。** 按 SEC 文件:Amazon 截至 2026 年第二季度的过去 12 个月自由现金流 −$76 亿;Oracle FY26 自由现金流 −$237 亿,截至 2026-08-31 的季度 −$54 亿(其中经营现金流含 $114 亿带融资成分的客户预付款,剔除后单季约 −$168 亿);Alphabet 单季 −$59 亿,但过去 12 个月仍为 +$533 亿;微软 FY26 约 +$670 亿;Meta 第二季度约 +$7.8 亿【多源】。转负的是 Amazon(过去 12 个月)和 Oracle;Alphabet 只有单季为负,Meta 单季接近零但为正;微软仍有大额正现金流。

更说明问题的是融资方式。Alphabet 第二季度从股权融资到账净额 $496 亿(公开发行普通股、伯克希尔私募、强制可转换优先股),同季发债净所得 $203 亿【单源已核】。Oracle 当季用完 $200 亿市价增发额度,并有 $2,880 亿尚未起租的数据中心租约。2026 年资本开支指引:Alphabet $1,950–2,050 亿,Amazon 现金口径约 $2,200 亿(从约 $2,000 亿上调,主因内存涨价),Meta $1,300–1,450 亿,微软日历年约 $1,750 亿(从约 $1,900 亿下调,是租约改为经营租赁后的会计重分类,CFO 称实际投资计划不变)【厂商口径】。

**合同积压约 $2.46 万亿,但不是独立需求。** 微软商业 RPO $6,780 亿、Alphabet 收入积压 $5,195 亿、AWS 未确认长期承诺约 $4,960 亿、Oracle RPO $6,640 亿、CoreWeave RPO $1,037 亿,加总约 $2.46 万亿【单源已核;算术】。这个数不能当作「AI 订单池」:各家截止日与定义不同,含大量非 AI 合同;同一批买家(OpenAI、Anthropic)在多家供应商处重复出现;CoreWeave 的客户里本身就有超大云厂商。微软 CFO 说「All sequential commercial RPO growth was driven by commitments from customers outside of frontier model companies. And RPO increased 25% when excluding OpenAI」,按两个增速推算 OpenAI 约占其商业 RPO 的三分之一【推算】;Oracle RPO 环比只增加了 $260 亿,而且只有约 13% 会在未来 12 个月内确认。AWS 10-Q 同期披露 OpenAI 在原 $380 亿之上 8 年追加 $1,000 亿、Anthropic 10 年追加 $1,000 亿以上,但没有写明是否已全部计入 $4,960 亿。

## 5. 算力租赁与电力层:带杠杆的折旧套利,以及一份没被计价的稀缺

**neocloud 的利润被利息吃掉。** CoreWeave 2026 年第二季度收入 $25.75 亿(+112%);non-GAAP 调整后 EBITDA $15.1 亿(59%),调整后经营利润只有 $1.28 亿(5%,上年 16%),GAAP 经营亏损 $4,900 万,净利息支出 $6.40 亿,GAAP 净亏损 $6.26 亿。差额主要是单季折旧摊销 $13.93 亿,占收入 54%【单源已核】。截至 6 月末,有息债务约 $351 亿、经营租赁负债约 $163 亿,股东权益 $50 亿。非可转换优先票据票面利率 8.5%–9.75%,另有约 $66 亿 1.75% 可转债;9 月又发了约 $37–42 亿 2.875% 可转债。管理层指引 Q3 利息支出 $8.6–9.4 亿,高于 Q3 调整后经营利润指引 $2.0–2.6 亿;2026 年资本开支指引 $350–390 亿,约为全年收入指引的 3 倍【厂商口径】。2025 年微软一家贡献其约 67% 的收入。

这种结构是超大云厂商主动外包出来的。Nadella 在同一次访谈里说,「I didn't want to get stuck with massive scale of one generation」,理由是机架功率与散热每代都在变、一代硬件要折旧四五年;缺容量时,「we will take leases, we will take build-to-suit, we'll even take GPUs-as-a-service」【厂商口径】。单代硬件的折旧风险和单一客户的集中风险,被留在了 neocloud 和它的债权人那里。

**GPU 租价没有一条曲线。** 常见的「H100 从每小时 $8 跌到 $1.70、跌了 80%、又反弹 60%–90%」是把不同指数拼起来算的,三票中两票判死。分口径看:超大云厂商的按需挂牌价,2024 年 1–5 月中位约 $7.92/小时,2025 年下半年中位约 $6.26,同口径只跌约 21%(Silicon Data)。SemiAnalysis 的一年期合约价,2025-10 低点 $1.70,2026-03 回到 $2.35(+38%)。SemiAnalysis 自家的现货与合约综合指数在 2025-10 到 2026-04 之间基本持平在约 $2.8。Silicon Data 的 neocloud 标准化 H100 指数 2026-10-05 为 $2.81,较 2025-12 约 +40%【单源各自已核】。CoreWeave 说 7 月「an approximately 25% increase across SKUs」,还签下一份延续到 2029 年的 A100 合同(A100 是 2020 年发布的芯片)【厂商口径】。能说的是:合约租价自 2025-10 低点反弹了约四成,2026 年是卖方市场;不能说租价「暴跌八成」。

**电费在总成本里占比小,这一点是多源的。** Epoch AI 2026-05 的示意模型:一座 1 GW、全部 GB200 的数据中心,年化总拥有成本约 $85 亿,其中服务器约 $50 亿(60%),电费约 $6 亿(约 7%,按美国平均工业电价 8.34 美分/度)【单源已核;模型估算】。反证搜索席找到的其他测算都落在同一区间:SemiAnalysis 估算 H100 集群电费约占 9%–11%,一家 GPU 云厂商按更高电价算出 14%–17%;没有任何来源说电费是 AI 数据中心的主要成本【升级为多源;区间约 7%–17%】。电价翻倍只让年化成本多约 $6 亿,而 IT 设备寿命从 7 年改成 3 年会让它多约 $50 亿。

**但「电力层租金薄」这个推论被否决了。** 方法学审计席指出,成本占比小推不出租金小;恰恰相反,正因为电费在总账里无足轻重,需求方对电价不敏感,供电稀缺的一方才有提价空间。按 Epoch 自己的年化口径粗算,一座 1 GW 园区晚通电一年,闲置算力的机会成本约 $60–70 亿,是全年电费的约 10 倍;SemiAnalysis 估计 GW 级 AI 集群每年可产生 $100–120 亿收入,并说企业选择表后燃气发电「不是更便宜而是更早」,是有意付溢价买时间【单源;估算】。Nadella 2025-11 也说过手里有芯片却没有通电的机房可插。所以「能马上通电」有一个很高的影子价格。

这份租金落在哪里,财报里只看得到碎片,而且大部分不在受管制的公用事业手里:

- **容量市场被政治封顶。** PJM 2028/29 年度容量拍卖全区以上限 $325/MW-day 出清,2024/25 年度只有 $28.92;比可靠性目标少 6,831 MW,自 2026/27 年度起连续三次在上限出清【多源】。宾州州长 Shapiro 牵头争取延长价格上限,PJM 已于 2026-02 同意延至 2030 年【厂商口径;州政府自估节省】。
- **独立发电商的调整后数字好看,GAAP 数字不一定。** Vistra 2026 年第二季度调整后 EBITDA $17.67 亿(+31%,含收购贡献),同期 GAAP 净利 $3.05 亿,低于上年 $3.27 亿【单源已核】。
- **燃机和已供电的场地在收稀缺租金。** GE Vernova 燃气设备积压加槽位预订从 100 GW 增至 116 GW(其中 63 GW 是槽位预订,不是确定订单);Digital Realty 2026 年第二季度 1 MW 以上续约的现金租金价差达 66.7%(单季,受亚太拉动,不宜当趋势)【单源已核】。并网排队方面,LBNL 数据显示 2025 年投运项目从申请到投运的中位数超过 5 年。

结论是:电力公司通过电费收到的钱在 AI 价值链里占比不大;「有没有电」的稀缺租金真实存在、量级可观,分散流向燃机厂商、持有并网排位和已供电场地的开发商、带电机房的房东。它的总量是否小于芯片层,方向上很可能如此,但没有直接测量【推断】。本站另一篇[《AI 带来的硬件短缺与电力短缺:是真的吗,还要多久?》](https://hub.cissychen.com/deep-research/ai-hardware-power-deep.html)讨论短缺本身的规模与持续时间,这里只看谁拿走了租金。

## 6. 模型层:收入分化,利润还没有

**收入:两种口径,一次超越。** 前沿实验室都未上市,以下数字全部来自公司自述、泄露文件或媒体转述。Anthropic 官方公告:run-rate 2025 年末约 $90 亿,2026-04 超过 $300 亿,5 月「crossed $47 billion」;Bloomberg 2026-08-17 首报其 7 月末超过 $650 亿【厂商口径;单源】。确认收入:据 Reuters 2026-09-28 首报的保密 S-1 草案,2025 年 $45.9 亿(2024 年约 $3.86 亿);2026 年第一季度 $47.3 亿;第二季度约 $115–116 亿,为初步、未审计数字【单源;泄露】。OpenAI:2025 年收入约 $130.7 亿(泄露的审计财报,FT 核实);据 WSJ 2026-08,2026 年第一、二季度收入分别为 $57 亿和 $67 亿【单源】。

于是出现了「Anthropic 季度收入首次超过 OpenAI」。反证搜索席确认 Bloomberg 与 WSJ 各自看到了投资者材料,Anthropic 一侧升级为多源;但比较的一端(OpenAI 的 $67 亿)仍只有 WSJ 一个来源。两家的确认口径也不同:Anthropic 对经 AWS、Google Cloud 渠道卖出的收入按总额确认(泄露草案显示 2025 年约 47% 的收入经这两个渠道),OpenAI 对微软渠道按扣除分成后的净额确认。按标题数,Anthropic 约为 OpenAI 的 1.7 倍;按草案里的渠道分成比例折算约 1.6 倍;按 OpenAI 方面指称的约 27% 高估折算约 1.3 倍。领先不会被口径翻转,但幅度比标题小【R3 审计:收入分化升级为多源,幅度方向存争】。

**利润:只有一家、一个季度、一个调整后口径。** WSJ 报道 Anthropic 2026 年第二季度首次录得剔除股权激励后的调整后经营利润,约 $5.59 亿,约占收入 5%;公司告诉部分股东预计第三季度仍为正——「连续两个季度」在报道时是预测,不是事实,三票一致判死【单源】。泄露草案显示 Anthropic 2025 年经营亏损 $80.6 亿(2024 年 $29.8 亿),GAAP 净亏损约 $420 亿,其中约 $340 亿是可转换融资工具的非现金重估;两大客户各约占 2025 年收入 12%【单源;泄露】。OpenAI 含股权激励的经营亏损从 2026 年第一季度 $93 亿扩大到第二季度 $123 亿,约为当季收入的 1.8 倍(WSJ)【单源】。FT 2026-09 报道 OpenAI 的投资者材料预测 2026–2030 年累计负自由现金流 $2,780 亿(5 月版本为 $3,050 亿),收入预测从 2026 年 $360 亿到 2030 年 $3,500 亿【单源;公司预测】。

审计席对这里的结论做了降级:**收入在头部之间已经明显分化,所以「模型层整体在给人做嫁衣」需要按公司拆开检验;但现在还不能说利润已经集中到某一家。** Anthropic 的盈利是公司自定义的调整后口径,剔除了股权激励等项目,方法未披露;OpenAI 的亏损数含股权激励;两边不是同一把尺子。

**毛利:几乎全部未验证。** The Information 报道两家 2025 年都没达到自己的毛利预测:OpenAI 调整后毛利约 33%(2024 年约 40%,原目标 46%),Anthropic 约 40%(内部预期约 50%,原因是推理成本比预期高 23%);但 6 月泄露的 OpenAI 2025 年财务显示毛利约 43%,口径不同【未验证;方向存争】。FT 报道 Anthropic 毛利超过 80%,这是扣除给 Amazon 等渠道伙伴的分成之前、且不计训练成本的数字【单源】。Evans 转述的「推理毛利 40%–50%」含服务器折旧,但不含「currently far larger than revenue」的下一代训练成本【未验证;他本人也未给出处】。

**承诺:模型层欠上游的账。** 泄露草案显示 Anthropic 与六家伙伴有约十年期、合计约 $5,180 亿的云、算力与基础设施义务,约 80% 不可撤销(与 Broadcom 相关的设备租赁 $1,612 亿、Google $1,111 亿、Amazon $1,100 亿)【单源;泄露】。OpenAI 的算力支出数字有多个版本,口径各不相同,不能连成一条时间序列:Altman 2025-11 说的约 $1.4 万亿(约 8 年承诺);2026-02 对投资者说 2030 年前约 $6,000 亿(CNBC);WSJ 2026-07 报道的 $7,500 亿;7 月投资者材料里 2026–2030 年约 $8,560 亿【各自单源】。

## 7. 两条价格曲线:商品化与前沿溢价说的不是同一条线

「模型商品化」与「前沿溢价」两派吵了两年。两派的分歧有一部分来自他们在看不同的曲线;但「前沿价格不降反升、与固定能力价格对称」这种说法不成立。下面分开看。

**第一条:固定能力的最低价格在暴跌。** Epoch AI 2025-03 测得,达到给定基准分数的每 token 价格每年下降 9 倍到 900 倍,中位约 50 倍;GPT-4 级 GPQA 表现约每年降 40 倍。Epoch 2026-09-22 的报告改用「跑完基准的总成本」,测得给定性能的成本自 2023 年起每季度下降约 47%,约合每年 13 倍(换聚合方法,季降幅在 43%–58% 之间,即每年约 9–30 倍);刚成为最强时降得最快,两年后降速减半;这个规律只在 5 个主基准中的 3 个上出现【多源】。MIT FutureTech 的 Gundlach 等测得给定性能的价格每年降 5–10 倍。a16z 2024-11 的「LLMflation」是每年 10 倍,作者自认方法「far from perfect」【多源;幅度从每年 5 倍到 50 倍以上不等,方向一致】。商品化叙事说的是这条线。

**第二条:用最强模型干一件事,在变贵。** 同一篇 MIT 论文的摘要写道:「the price of running frontier models is rising between 3× to 18× per year due to bigger models and larger reasoning demands」【单源已核;样本只有 3 个基准、19 个月】。上升的主因是推理模型消耗的 token 暴增,不是每 token 单价普遍上涨。前沿溢价叙事说的是这条线。

**标价本身:顶档上探,但分层了。** OpenAI 定价页(每百万 token 输入/输出,标准档):GPT-5 $1.25/$10 → gpt-5.4 $2.5/$15 → gpt-5.5 $5/$30;截至 2026-10,顶部是 gpt-6-astra $10/$50,而同代主力档 gpt-6-sol 只要 $2/$10,另有 $0.10/$0.50 的 gpt-6-luna。Anthropic 顶档(Fable 5/5.1、Mythos 5/5.1)为 $10/$50,低于 2025 年 Opus 4/4.1 的 $15/$75【多源;官方定价页】。所以「旗舰价格逐代单调上涨」不成立;成立的是「顶档在上探,同时出现了更便宜的主力档」。

**开源权重落后约 4 个月,闭源拿走大部分收入。** Epoch 2026-05 测得,2026 年以来最强的开源权重模型平均落后闭源前沿约 4 个月【多源】;它此前测得的 2023-01 至 2025-10 平均约 3 个月,两次时间窗不同,只能说近期区间略大,不能写成「差距在扩大」。Frank Nagle 与 Yue 的 SSRN 工作论文(经 Linux Foundation 博客介绍)用 OpenRouter 数据称,闭源模型约占 80% 用量、96% 收入,均价约为开源的 6 倍,企业每年因此多花 $200–480 亿(首选 $248 亿);OpenRouter 只占全球 API 支出约 1%,偏开发者【单源已核;样本偏】。Menlo Ventures(Anthropic 的投资方)的企业调查估计,企业 LLM 支出份额 Anthropic 40%、OpenAI 27%、Google 21%,开源份额从 19% 降到 11%【厂商口径;投资方估算】。

把两条线放在一起,模型层的利润取决于一个需求问题:客户的钱是留在第二条线上(为最强能力付每任务越来越高的账单),还是滑向第一条线(用便宜得多的「够好」的能力)。Cursor 的经历给了一个微观样本(第 8 节):它靠把自研模型的底座换成开源的 Kimi K2.5,才把毛利从负翻成微正。

## 8. 应用与分发层:利润在握有分发的现有巨头手里

**现有巨头没有被颠覆,而且更稳了。** Alphabet 2026 年第二季度 Search & other 收入 $632.7 亿(+17%),Google Services 分部经营利润率 41.8%(上年 40.1%),Pichai 称 AI Mode 月活超过 10 亿;但这个利润率不含 $57.9 亿主要为共享 AI 研发的 Alphabet 层成本,所以偏高【单源已核】。Meta 广告收入 $593.6 亿(+27.5%);合并经营利润 $187.8 亿,同比 −8%,但当季含 $24 亿法律费用和 $11.8 亿裁员遣散费,剔除后约 +9%。10-Q 列出的成本增长驱动依次是员工薪酬、数据中心与第三方云服务、法律费用、第三方 AI token 成本,token 是四项之一且列最后,所以「AI 成本在侵蚀 Meta 利润」不成立【单源已核】。微软 Productivity and Business Processes 分部第四季度经营利润率 57.9%,M365 Copilot 付费席位超过 3,000 万(未披露单价)。Apple Services 收入 $307.4 亿,毛利率 75.6%;前九个月资本开支 $68 亿,低于上年同期的 $94.7 亿。

Apple 是「轻资产聚合者」的样本。2026-01-12 Apple 与 Google 联合声明,下一代 Apple Foundation Models 将基于 Gemini;彭博签约前报道 Apple 接近达成每年约 $10 亿的协议,正式条款未披露【单源;媒体】。对比法院在反垄断案中认定的数字:2022 年 Google 为成为默认搜索引擎付给 Apple 超过 $200 亿。两笔钱年份不同、方向相反,只能作量级对比:握着分发的一方,从模型商那里拿到的,远多于它付给模型商的。

**AI 原生应用:增长快,毛利薄,受上游掣肘。** Bessemer 统计的约 10 家增长最快的「Supernova」AI 应用公司平均毛利约 25%,常常为负【VC 样本口径】。Cursor 据 TechCrunch 2026-04 援引知情人,「operated at negative gross margins until recently」,靠自研 Composer 加调用 Kimi 等更便宜的模型才实现微弱正毛利,且据单一信源只有大企业客户是正毛利、个人开发者账户仍在亏【单源】。Composer 2 以月之暗面开源的 Kimi K2.5 为底座,Cursor 联创 Aman Sanger 承认「It was a miss to not mention the Kimi base in our blog from the start」【多源】。流传的「截至 2026 年 1 月的季度毛利 −23%」一说无人核到原文,不可用。

上游断供有两例。2025-06,据 Windsurf CEO Varun Mohan 的单方说法,Anthropic 提前不到五天切断其对 Claude 3.x 模型的几乎全部一手容量,当时正值 OpenAI 传出要收购 Windsurf;此后 Windsurf 被拆分,Google 以约 $24 亿取得非独家授权并招走 CEO,Cognition 收购其余部分【单源;当事方自述】。2026-08-14,SpaceX 完成对 Cursor 的收购,支付约 3.89 亿股 SpaceX A 类股,隐含股权价值 $600 亿,按媒体报道的约 $30 亿 run-rate 约 20 倍;交割后 OpenAI 宣布停止向 Cursor 提供模型【SEC 一手;断供为多源媒体】。

模型方也在收紧自家订阅的外溢。2026-01 起,Anthropic 技术封堵冒充 Claude Code 的第三方工具;2 月在合规文档中澄清订阅 OAuth 只限 Claude Code 与 Claude.ai(消费者条款本身自 2024-02 起即禁止未授权的自动化访问,并未修改);2026-04-04 起先对 OpenClaw 停用订阅额度,并称将推及所有第三方 harness【多源】。GitHub 2026-04-27 宣布 Copilot「the current premium request model is no longer sustainable」,6 月起全部方案改按用量计费【单源已核】。

**模型公司在吃应用层。** Anthropic 2026-02 自报 Claude Code run-rate 超过 $25 亿,企业占其一半以上,同期公司总 run-rate $140 亿【厂商口径】。OpenAI 8 月称广告业务已达约 $10 亿 run-rate;CFO Sarah Friar 对投资者说企业收入已超过消费者收入【厂商口径;与会者转述】。现有 SaaS 公司的 AI 加价兑现有限:Salesforce 截至 2026-07-31 的季度 Agentforce ARR 超过 $15 亿,但本季起口径扩大到 Slackbot 等;总营收 +11%,扣除并购贡献后有机增长约 6%【单源已核】。

应用层被收购时的估值并不低(Cursor 约 20 倍 run-rate),但它的利润和控制权受制于上游的供给。当下的 AI 应用层利润,主要落在本来就握着用户的人手里。

## 9. 并排看:当下的利润在哪一层

把前五节的数字放到同一把尺子上(最近一个季度的 GAAP 经营利润率,分部口径):存储(Micron 80.7%、SK hynix 76%)> 芯片设计(NVIDIA 66.2%)> 代工(TSMC 60.3%)> 云分部(微软 Intelligent Cloud 40.6%、AWS 39.4%、Google Cloud 35.6%)> neocloud(CoreWeave −1.9%)> 前沿实验室(OpenAI 经营亏损约为收入的 1.8 倍,媒体报道)。应用层里,握着分发的巨头分部利润率在 40%–58% 之间(且不含 AI 研发),AI 原生应用毛利在负数到 25% 之间。

几个限定:各家财年最多错开约两个月;Google Cloud 与 Services 未摊入 AI 研发;云分部利润率依赖 5.5–6 年的折旧假设;实验室数字是媒体口径。限定不改变排序。**截至 2026 年 10 月,AI 价值链的当下利润分布是一条向上游倾斜的线:越靠近物理稀缺(存储、先进芯片、代工),利润率越高;越靠近模型,越亏。**这是「卖铲子赢」叙事站得住的部分。它没回答的是:这条线由什么维持,能维持多久。

**撑住这条线需要多少下游收入。** 这类测算都是「餐巾纸算法」,而且一年比一年大。Sequoia 的 David Cahn 2024-06 取 NVIDIA 的 run-rate 收入预测,乘 2(GPU 约占数据中心总成本一半)再乘 2(终端用户要有 50% 毛利),得出「$6,000 亿问题」;他 2026-07 在个人 Substack 上用同一算法得出 $1.5 万亿,含义是「一年的资本开支需要多少终身终端收入来回本」,并称 ChatGPT 以来累计约 $3 万亿(他自称是粗估)【单源已核】。Bain 2025-09 估计 2030 年约 $5,000 亿的年资本开支需要约 $2 万亿年收入,即便假设企业把全部本地 IT 预算迁上云、再投入 AI 带来的节省,仍差约 $8,000 亿;2026-09 的新版估计 2031 年 AI 基建年支出可达 $1.5 万亿,按资本开支约占收入 25% 需要接近 $6 万亿的年市场,现有消费与企业 AI 只能贡献 $1.2–1.8 万亿,缺口 $4.2–4.8 万亿【咨询机构口径】。两版 Bain 用的资本开支与收入之比相同,缺口扩大来自资本开支预测上调了约 3 倍。这些数字不是预测,是「需要多少」;它们说明上游的利润率要维持,下游收入必须以远快于今天的速度增长。

## 10. 资金在转圈:「嫁衣」的方向反了一半

如果只看现金,模型层确实在给上游打工。但把股权、信用和会计收益都画进来,资金是一个环。

**现金向上流。** 微软 FY26 从 OpenAI 的商业安排确认收入 $241 亿(含收入分成,大部分是 Azure 算力款),期末应收 $60 亿【单源已核】。常见的「微软从 OpenAI 收的钱超过 OpenAI 一年的收入」说法不成立:窗口不同(微软财年对日历年),而且对照的 OpenAI 收入是媒体数字。更准确的说法是:这笔钱主要由 OpenAI 的融资支付,而微软本身就是出资方之一。Anthropic 那 $5,180 亿、约 80% 不可撤销的十年义务,是同一方向的更大一笔。

**股权和信用向下流。** NVIDIA CFO 在 2026-08 电话会上说「we've invested nearly $50 billion in the frontier AI labs」,并预计借助 NVIDIA 资产负债表的实验室需求将「contribute toward roughly a quarter of our business next year」;她预先点出「we know some will call this circular financing. We see it differently」【厂商口径;前瞻】。NVIDIA 10-Q 写道:「We believe AI clouds and AI model makers ... currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity」,所以由 NVIDIA 提供土地、电力、机房外壳和容量担保;它对 AI 云有 $360 亿云服务采购承诺(一般 6 年),若 AI 云卖不出承诺容量,NVIDIA 同意买下【单源已核】。2025-09 那份「至多 $1,000 亿」的投资意向书没有约束力;实际落地是 2026 年 OpenAI 融资中的 $300 亿股权,黄仁勋 2026-03 说投 $1,000 亿「probably not in the cards」【多源】。2026-08 NVIDIA 又为 SB Energy 租给 OpenAI 的 PORTS-Pike 园区(约 4.25 GW、20 年)提供残值担保,累计支付上限 $1,050 亿——这是或有的违约缺口担保,2028 年起分期生效、随租期递减、OpenAI 取得满意信用评级即终止、OpenAI 须偿付 NVIDIA 实付款项,不是当下已经流出的信用【单源已核】。

不止 NVIDIA。Amazon 对 OpenAI 承诺的 $500 亿已在 2026 年付清;对 Anthropic,2023–2025 年投了 $80 亿可转债,2026 年第二季度再投 $100 亿优先股,其中 $50 亿来自一个至多 $200 亿、**按 AWS 算力交付里程碑释放**的融资额度【单源已核】——股权下流和算力上流被写进了同一份合同。NVIDIA 与微软 2025-11 分别承诺向 Anthropic 投资至多 $100 亿和 $50 亿,Anthropic 同时承诺购买 $300 亿 Azure 算力【多源】。Broadcom 通过与 Apollo、Blackstone 的融资平台(首期 $350 亿)为 Anthropic 的部署融资【单源;仅一票核到】。

**估值以账面收益回到上游利润。** Amazon 2026 年第二季度经营利润 $275 亿,而对 Anthropic 优先股的公允价值上调约 $505 亿(上半年 $628 亿),是同季 AWS 分部经营利润 $166 亿的约 3 倍;这是税前、非经营项,上半年为此计提了约 $159 亿离散所得税【单源已核】。NVIDIA 上半年 GAAP 税前利润 $1,414 亿中有 $241 亿其他收益,主要是股权投资的未实现收益,约占 17%(单看第二季度约 11%)【单源已核】。微软 FY26 对 OpenAI 投资录得税前净收益 $65 亿(主要是 OpenAI 重组带来的稀释收益),第四季度另有 Anthropic 投资收益 $32 亿,后者留在了 non-GAAP 里【单源已核】。Alphabet 第二季度 $775 亿的非上市股权未实现收益来自一家未具名的私营公司,市场普遍推断为 Anthropic,但 10-Q 全文没有这个名字,同季的收益里还混有 SpaceX,不宜当作干净的例证。

同一次重估在两边留下镜像:Anthropic 2025 年约 $340 亿非现金亏损来自可转换工具重估,Amazon 一侧是收益。

这个环说明三件事。第一,用净利润比较各层,会把模型层的估值重复计算。第二,「做模型的在给人做嫁衣」在现金上成立,在风险上反了:上游在为模型层的信用托底,NVIDIA 明年约四分之一的业务、云厂商积压订单里的大头、Amazon 本季税前利润的大头,都系在少数几家实验室的偿付能力和估值上(Alphabet 本季也有一大块收益来自一家未具名的私营公司)。第三,这个环正在受到压力:WSJ 2026-08 下旬报道 NVIDIA 因内部反垄断顾虑与合作方反弹,暂停了部分 AI 云收入分成交易,NVIDIA 回应该模式「still in place and continues to evolve」【未验证;媒体转述】;黄仁勋 3 月表示股权投资大概到此为止,8 月电话会上支持方式转为对另一家前沿实验室约 2 GW 的「selective credit enhancement」。

所以「利润落在哪一层」至少有一部分要换成另一个问题:**模型层的信用风险最后由谁承担。**本站[《这轮 AI 资本开支是不是 1999?》](https://hub.cissychen.com/deep-research/ai-capex-1999-deep.html)从融资结构角度审过这个类比,这里补上的是层间的会计与信用联系。

## 11. 长期落点:两个变量,四种情景

理论给不出点预测,但第 1 节的两套理论共同指向两个可以观测的变量。把它们交叉,得到四种情景。每种情景都写下最先会露出的信号。

**变量一:前沿能力对客户来说是否「够好」。** Christensen 的前提是 performance gap;Thompson 9 月的推论是「good enough」。可观测的代理:企业是否在愿意为最强模型付溢价(每任务成本上升而支出份额不降),还是迁往便宜的「够好」模型(开源份额回升、主力档放量、应用公司换底座)。

**变量二:物理瓶颈是否解除。** 存储、先进封装、电力接入的稀缺什么时候缓解。可观测的代理:存储厂利润率是否回落到 NVIDIA 以下;H100/B200 合约租价方向;PJM 容量价能否在上限以下出清;燃机槽位预订是否转为确定订单。

1. **瓶颈持续 × 前沿不够好:物理层与整合的前沿实验室分利润。** 芯片与存储维持高利润率,前沿实验室凭能力溢价覆盖算力承诺。信号:存储与 NVIDIA 利润率都维持高位,头部实验室的 GAAP 经营利润率转正。
2. **瓶颈持续 × 前沿够好:物理层独占。** 模型降为可替换件,价值被稀缺的物理投入(存储、芯片、已供电场地)吸走。信号:存储利润率继续高于 NVIDIA;开源与主力档份额上升;实验室收入增长而毛利不升。
3. **瓶颈解除 × 前沿不够好:整合者赢。** 算力变便宜,前沿差距靠模型与产品整合维持溢价(Thompson 3 月的情景)。信号:GPU 租价与存储价格回落,同时前沿每任务支出份额继续上升,实验室的 harness 产品(如编程 agent)吃掉应用层。
4. **瓶颈解除 × 前沿够好:用户触点赢。** 模型与算力都商品化,利润回到握有用户与分发的一方(Thompson 6 月所说的「in the fullness of time」)。信号:租价与存储价格回落,开源份额回升,Google、微软、Apple、Meta 的分部利润率继续上升而资本开支占收入比下降。

截至 2026 年 10 月的读数更接近情景 1 与 2 之间:物理瓶颈在持续(存储利润率创纪录、租价反弹、容量价撞顶),而「够好」的证据刚刚出现(Thompson 9 月的单一事件、Cursor 换开源底座、OpenAI 推出更便宜的主力档),还不能确认。资金环把这个判断变得更脆弱:如果某家前沿实验室的融资出问题,受冲击的首先是为它托底的上游。

## 12. 判决

**第一,当下的利润在上游,而且越往物理稀缺走越厚。** 存储 > 芯片 > 代工 > 云分部 > neocloud > 模型层。这一条有 SEC 一手数据,是本文最硬的结论。它不支持「芯片层的份额还在扩大」:从业者估算的芯片层毛利份额从约 87% 降到约 79%,NVIDIA 的毛利正在被存储涨价挤压。

**第二,稀缺租金在芯片层内部迁移。** 从 GPU 到存储,而且落在通用 DRAM/NAND 的缺货涨价上,不是 HBM 本身。NVIDIA 计划靠自己提价把毛利拉回,所以这次迁移可能是暂时的。

**第三,云层的高利润率是有条件的。** 研发不摊入、5.5–6 年折旧、AI 租赁毛利会爬升,三个假设各自都有反例。现金流已经分化:Amazon 和 Oracle 为负,Alphabet 开始在股市融资。

**第四,模型层内部已分化,但利润还没出现。** 收入领先者在一年内换了位,唯一的盈利是一个季度的调整后数字。「模型层整体给人做嫁衣」要按公司拆开看。

**第五,「嫁衣」的方向反了一半。** 现金从模型层流向上游,股权和信用从上游流向模型层,模型层的估值又以账面收益回到上游的利润表。最该追问的已经不是哪一层利润率最高,而是**谁在承担模型层的信用风险**。

**第六,长期落点取决于两个可观测的变量:前沿是否「够好」、物理瓶颈是否解除。** 理论给不出答案,但给出了该盯什么。

## 13. 十一个可检验主张

按证据强度排序,强的在前。

1. **截至 2026 年中,按最近一季的 GAAP 经营利润率,AI 价值链上利润率最高的是存储与芯片层(Micron 80.7%、SK hynix 76%、NVIDIA 66.2%、TSMC 60.3%),高于云分部(35.6%–40.6%),远高于 neocloud(CoreWeave −1.9%)与前沿实验室(OpenAI 经营亏损约为收入 1.8 倍)。**【最强:SEC 一手,实验室一端为媒体口径】检验方式:后续季报;若云分部或任一前沿实验室的 GAAP 经营利润率追近芯片层,本条即被推翻。
2. **前沿实验室的估值正以未实现收益的形式计入上游 GAAP 利润,用净利润衡量各层利润会重复计算模型层的价值。** Amazon 2026 年第二季度对 Anthropic 的税前公允价值上调约 $505 亿,约为同季 AWS 分部经营利润的 3 倍;NVIDIA 上半年约 17% 的税前利润来自股权收益。【强:10-Q 一手】检验方式:若前沿实验室出现估值下调轮次,这些收益应以同等规模反向出现在上游利润表。
3. **neocloud 的利息支出高于其调整后经营利润。** CoreWeave 第二季度净利息 $6.40 亿对调整后经营利润 $1.28 亿,第三季度指引仍是利息高于经营利润。【强:SEC 一手,但只有一家】检验方式:Nebius 等同类公司的同口径数字;或 CoreWeave 调整后经营利润首次覆盖利息。
4. **云厂商的现金流已经分化,高分部利润率与负自由现金流并存。** Amazon 过去 12 个月 −$76 亿、Oracle FY26 −$237 亿,Alphabet 单季为负并在股市融资 $496 亿,微软仍为 +$670 亿。【强:SEC 一手】检验方式:2026 年下半年各家自由现金流;若 Amazon 与 Oracle 转正而资本开支不降,本条的「分化」读数即被削弱。
5. **固定能力的价格每年下降约一个数量级,而用最强模型完成一项任务的成本在上升;商品化与前沿溢价两派描述的是不同的曲线。**【中强:多源,但两条曲线的取样口径不对称,第二条只有一项研究】检验方式:Epoch 与 MIT 的后续更新;若前沿每任务成本也开始逐年下降,「两条曲线方向相反」不再成立。
6. **芯片层内部的稀缺租金已从 GPU 迁移到存储,且主要落在通用 DRAM/NAND 而非 HBM。**【中强:Micron、SK hynix、NVIDIA 一手,但 NVIDIA 预期靠提价恢复】检验方式:2027 年存储扩产后,若 Micron 经营利润率回落到 NVIDIA 以下、NVIDIA 毛利回到 72%–73% 以上,迁移即为暂时。
7. **AI 应用层当下的利润主要落在握有分发的现有巨头(Google Services 41.8%、微软 P&BP 57.9%、Apple Services 毛利 75.6%),AI 原生应用毛利薄(约 25% 或更低),且受上游断供约束。**【中:巨头为 SEC 一手;应用公司为媒体与 VC 样本】检验方式:任一 AI 原生应用公司公开披露持续正毛利且高于 50%;或巨头分部利润率在扣除 AI 研发后转为下降。
8. **NVIDIA 正在用资产负债表支撑约四分之一的下一年需求。**【中:厂商前瞻口径】检验方式:FY28 实际披露中,来自其投资或担保对象的收入占比;以及 PORTS-Pike 担保是否在 2028 年后被触发。
9. **前沿实验室的收入已在头部之间明显分化,但利润尚未集中:截至 2026 年 10 月,只有 Anthropic 一个季度录得调整后经营利润,没有任何一家披露过 GAAP 季度经营盈利。**【中:多源媒体与泄露文件,未审计】检验方式:Anthropic S-1 公开版本;第三季度实际数字;OpenAI 的同口径披露。
10. **电费只占 AI 数据中心总成本的约一成上下(约 7%–17%),但「能马上通电」的影子价格约为全年电费的 10 倍,这份稀缺租金主要落在已供电场地、并网排位与燃机供应链,而不是受管制的公用事业。**【中弱:成本占比多源,租金归属为推断】检验方式:电力开发商与燃机厂商的利润率;已供电场地的交易溢价;PJM 价格上限到期后的出清价。
11. **长期利润落点由两个可观测变量决定:客户是否认为前沿能力「够好」,以及物理瓶颈是否解除;截至 2026 年 10 月的读数位于「瓶颈持续」一侧,「够好」的证据刚出现。**【弱:理论框架加初步信号】检验方式:第 11 节列出的八个信号。

**值得盯什么。** 四件事一旦发生,本文的判断就该改:一是**存储利润率回落到 NVIDIA 以下**,说明物理瓶颈开始解除;二是**某家前沿实验室发布 GAAP 口径的经营盈利**,或者反过来,**出现估值下调的融资轮**——后者会在上游利润表里留下反向的账;三是**开源或主力档模型的企业支出份额回升**,这是「够好」的直接读数;四是 **NVIDIA 的 PORTS-Pike 担保、AI 云采购承诺被实际触发**,那是资金环受压的第一个硬信号。

## 附:方法学与本期的自我修正

本期 31 组承重论断各派 3 个独立验证 agent(两批低风险的理论原话与历史数字用较小模型,其余用 Opus 级),分逐字、反证、口径三个镜头,要求尽力反驳。结果:31 组中没有一组三票都判原样成立;子论断层面 70 余处被判死或被禁止按原稿形式使用。另对 3 条单源承重实证加做反证搜索席与方法学审计席。

被验证推翻或改写的原稿表述,挑最重要的列出:

1. **「前沿旗舰价格逐代上涨」被判死。** OpenAI 已推出 gpt-6 代,顶档 $10/$50,主力档只要 $2/$10;Anthropic 顶档比 2025 年还便宜。改为「顶档上探、价格分层」,并以每任务成本(而非每 token 标价)作为「前沿变贵」的证据。
2. **「电力层租金薄」被方法学审计席否决。** 电费占比小是多源事实,但成本占比推不出租金大小;改为「电费份额小,而接入速度的稀缺租金可观、流向分散」。
3. **「微软从 OpenAI 收的钱超过 OpenAI 一年收入」被判死。** 窗口不同,对照数是媒体数字;改为「这笔钱主要由 OpenAI 的融资支付」。
4. **「Anthropic 已连续两个季度盈利」被判死。** 只有第二季度一个已完成的调整后盈利季度,第三季度是预期。
5. **「H100 租价暴跌 80% 后反弹 60%–90%」被判死。** 是跨指数拼接;同口径按需价只跌约 21%,合约价从低点反弹约 38%。
6. **「NVIDIA 担保 $1,050 亿」不加限定被禁止使用。** 它是 2028 年起分期生效、递减、可获偿付的或有上限,不是当下流出的信用。
7. **「HBM 是存储厂最厚的利润」被判死。** 含 HBM 的事业部毛利反而最低,最厚的是通用 DRAM/NAND 的缺货涨价。
8. **「NVIDIA 已收购 Hugging Face」改为「已签最终协议、预计 2027 年上半年交割」。**
9. **「Meta 利润下滑由 AI token 成本驱动」被判死。** 下滑主要来自一次性法律与遣散费用,剔除后同比约 +9%。
10. **「云厂商自由现金流转负」不得笼统使用。** 只有 Amazon(过去 12 个月)和 Oracle 为负;Alphabet 过去 12 个月仍为 +$533 亿。
11. **「Cursor 季度毛利 −23%」与「SpaceX 以约 15 倍收入收购」被判死。** 前者无人核到原文,后者按报道 run-rate 约为 20 倍。
12. **「开源差距从 3 个月扩大到 4 个月」被判死。** 两次测量的时间窗不同,不能写成趋势。

这些修正有一个共同方向:**几乎每一个让某一层显得「更极端」的数字——更暴跌的租价、更薄的电力租金、更高的前沿价格、更集中的利润——送回原文之后都温和了一些。**

## 附:主要来源

**理论与历史**:Christensen,HBR《Breakthrough Ideas for 2004》(https://hbr.org/2004/02/breakthrough-ideas-for-2004)、Christensen–Raynor–Verlinden《Skate to Where the Money Will Be》(https://hbr.org/2001/11/skate-to-where-the-money-will-be)、Thompson《Aggregation Theory》(https://stratechery.com/2015/aggregation-theory/)、《The Benefits of Bubbles》(https://stratechery.com/2025/the-benefits-of-bubbles/)、《Agents Over Bubbles》(https://stratechery.com/2026/agents-over-bubbles/)、《Anthropic's Safety Superpower》(https://stratechery.com/2026/anthropics-safety-superpower/)、《Frontier Overhangs》(https://stratechery.com/2026/frontier-overhangs/)、Spolsky《Strategy Letter V》(https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/)、Evans《Ways to think about token pricing》(https://www.ben-evans.com/benedictevans/2026/7/9/ways-to-think-about-token-pricing)、Nadella 访谈(https://www.dwarkesh.com/p/satya-nadella-2)、Amodei 访谈(https://cheekypint.substack.com/p/a-cheeky-pint-with-anthropic-ceo)、Odlyzko 2003(https://www-users.cse.umn.edu/~odlyzko/doc/itcom.internet.growth.pdf)、Odlyzko 铁路狂热(https://www-users.cse.umn.edu/~odlyzko/doc/hallucinations.pdf)、Intel 2000 10-K(https://www.sec.gov/Archives/edgar/data/50863/000091205701503434/0000912057-01-503434.txt)、Compaq 2000 10-K(https://www.sec.gov/Archives/edgar/data/714154/000089056601000112/0000890566-01-000112.txt)

**芯片与存储**:NVIDIA Q2 FY27 CFO commentary(https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm)、NVIDIA 10-Q(https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm)、NVIDIA PORTS-Pike 8-K(https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)、NVIDIA Hugging Face 8-K(https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm)、Micron FQ4 FY26(https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/a2026q4ex991-pressrelease.htm)、SK hynix 2Q26(https://news.skhynix.com/en/q2-2026-business-results/)、TSMC 2Q26(https://www.sec.gov/Archives/edgar/data/1046179/000104617926000451/a2q26e_withguidancexfinal.htm)、Broadcom Q3 FY26(https://www.sec.gov/Archives/edgar/data/1730168/000173016826000076/avgo-08022026x8kxex99.htm)、AMD 10-Q(https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm)、SemiAnalysis TPUv7(https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)、Agrawal《The Economics of Generative AI》(https://tailwinds.substack.com/p/the-economics-of-generative-ai-two)

**云与 neocloud**:Amazon Q2 2026 10-Q(https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm)、Alphabet Q2 2026 10-Q(https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm)、Microsoft FY26 10-K(https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)、Meta Q2 2026 10-Q(https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm)、Oracle Q1 FY27 10-Q(https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm)、CoreWeave Q2 2026(https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm)、Oracle GPU 毛利报道(https://www.cnbc.com/2025/10/07/oracle-stock-nvidia-chip-margins.html)、SemiAnalysis《The Great GPU Shortage》(https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity)

**电力**:Epoch AI 数据中心成本拆解(https://epoch.ai/data-insights/ai-datacenter-cost-breakdown)、PJM 2028/29 容量拍卖(https://www.prnewswire.com/news-releases/pjm-capacity-auction-procures-138-318-mw-of-generation-resources-as-work-continues-to-address-growing-electricity-demand-302825613.html)、Vistra Q2 2026(https://www.sec.gov/Archives/edgar/data/1692819/000169281926000017/vistra-20260630xearningsre.htm)、GE Vernova Q2 2026(https://www.sec.gov/Archives/edgar/data/1996810/000199681026000147/gevpressrelease2q26.htm)、Digital Realty Q2 2026(https://www.sec.gov/Archives/edgar/data/1297996/000110465926086270/dlr-20260723xex99d1.htm)

**模型层与价格**:Anthropic Series H(https://www.anthropic.com/news/series-h)、Anthropic–Google–Broadcom(https://www.anthropic.com/news/google-broadcom-partnership-compute)、Anthropic S-1 草案报道(https://fortune.com/2026/09/29/anthropic-ipo-s-1-prospectus-income-statement/)、WSJ 收入报道转载(https://finance.yahoo.com/technology/ai/articles/openai-q2-growth-trails-anthropic-102250259.html)、OpenAI 现金流预测报道(https://finance.yahoo.com/technology/ai/articles/openai-projects-burning-278-billion-230655542.html)、Epoch 价格趋势 2025(https://epoch.ai/data-insights/llm-inference-price-trends)、Epoch《The Plunging Price of Thought》(https://epoch.ai/publications/the-plunging-price-of-thought)、Gundlach 等(https://arxiv.org/abs/2511.23455)、OpenAI 定价页(https://developers.openai.com/api/docs/pricing)、Epoch 开源差距(https://epoch.ai/data-insights/open-closed-eci-gap)、Nagle(https://www.linuxfoundation.org/blog/revealing-the-hidden-economics-of-open-models-in-the-ai-era)、Menlo Ventures(https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)

**应用与资金流**:Microsoft–OpenAI 2026-04 修订(https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)、Bessemer State of AI 2025(https://www.bvp.com/atlas/the-state-of-ai-2025)、Cursor 毛利报道(https://techcrunch.com/2026/04/17/sources-cursor-in-talks-to-raise-2b-at-50b-valuation-as-enterprise-growth-surges/)、Windsurf 断供(https://techcrunch.com/2025/06/03/windsurf-says-anthropic-is-limiting-its-direct-access-to-claude-ai-models)、Salesforce Q2 FY27(https://www.sec.gov/Archives/edgar/data/1108524/000110852426000187/crm-q2fy27xexhibit991.htm)、Sequoia《AI's $600B Question》(https://sequoiacap.com/article/ais-600b-question/)、Cahn《AI's $1.5T Question》(https://dcahn.substack.com/p/ais-15t-question)、Bain 2026 技术报告(https://www.bain.com/insights/new-innovation-is-required-to-fund-ais-6-trillion-buildout-technology-report-2026/)

**本站相关研究**:这轮建设的融资结构与 1999 的对照见[《这轮 AI 资本开支是不是 1999?——给一个类比做体检》](https://hub.cissychen.com/deep-research/ai-capex-1999-deep.html);硬件与电力短缺本身的规模与持续时间见[《AI 带来的硬件短缺与电力短缺:是真的吗,还要多久?》](https://hub.cissychen.com/deep-research/ai-hardware-power-deep.html);前沿能力是否仍在快速提升见[《Scaling laws 撞墙了吗?一场没有定义的争论》](https://hub.cissychen.com/deep-research/scaling-wall-deep.html)。
