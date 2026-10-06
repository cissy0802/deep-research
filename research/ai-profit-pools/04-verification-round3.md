# Round 3 单源承重实证双席审计

## R1-energy-tco · counter · 判决:升级多源

**可用表述**:多个独立测算都显示,电费只占 AI 数据中心总拥有成本的一小部分:Epoch AI 估算 1 GW GB200 园区约 7%,SemiAnalysis 估算 H100 集群约 9-11%,按更高电价测算约 14-17%。IT 设备的折旧和寿命假设对成本的影响大得多:寿命从 5 年改为 3 年,年化成本增加约 40%;电价翻倍只增加约 7%,PJM 容量价暴涨后的增幅也不到 2%。但电费占比小,不等于电力层的租金薄。正因为电费在总账里无足轻重,而一个 GW 级 AI 集群每年可产生约 $100-120 亿收入(SemiAnalysis),开发商宁愿多付溢价,用表后燃气发电换取提前上线。"有没有电"的影子价格远高于电费本身。这份接入速度的稀缺租金真实存在,目前分散流向燃机厂商、已拿到并网资格的开发商、带电机房房东和容量市场。它的总量是否小于芯片层,方向上很可能如此,但尚无直接测量,应写成推断。

**推理**:一、成本占比这个事实可以升级为多源,方向一致。其他独立团队和数据给出的数字是:SemiAnalysis 测算 Meta 24,576 卡 H100 集群,电力约占 TCO 的 9%,占 OpEx 约 32%,电价约 8.3¢/kWh;按 GPU 小时口径,$1.49/H100-hr 里电费约 $0.16,约 11%。这组数字来自搜索摘要的转述,原文在付费墙后,我只核到了公开部分。Cloudrift 按每 GPU 测算,在 8-12¢/kWh 下电费占 14-17%,折旧占 52-55%;它是 GPU 云厂商博客,有利益相关,而且电价和利用率假设更高。Thunder Said Energy 认为在线率和利用率对经济性的影响约是电价的 5 倍,这与 Epoch"寿命假设比电价重要"同向。所有来源都落在约 7% 到 17% 区间,没有一个来源说电费是 AI 数据中心的主要成本。

二、电价敏感性(我自己算的,基于 Epoch 的参数):
- 电价翻倍到约 16.7¢:能源从 $0.6B 升到约 $1.2B,TCO 约 $9.1B,占比约 13%。这已不是个位数,但仍远小于服务器的 60%。
- PJM 容量价按 2027/28 年度出清价 $333/MW-day 算,满负荷折合约 $13.9/MWh,即每度电加约 1.4¢,能源成本只多约 17%(约 +$0.1B)。若没有价格上限(约 $530/MW-day),也只加约 2.2¢。
- 寿命从 5 年变 3 年会让 TCO 增加约 $3.5B,远大于电价翻倍带来的约 $0.6B。所以"寿命假设比电价影响大"这句很稳健。"个位数百分比"的措辞则比较脆:换高电价或零售电价,就会进入 10-17%。

三、影子价格。这一处有实质的方向争议,文章的推论在这里站不稳:
- SemiAnalysis(2025-12-30)称 AI 云每 GW 年收入约 $10-12B,200 MW 早上线半年值 $1-1.2B;它还明确说,表后供电并不更便宜,而是更早,企业是有意识地付溢价买时间。
- 纳德拉(2025 年 11 月 BG2 播客)说手里有芯片却没有带电机房可插。部分报道把时间写成 2024 年 11 月,有误,文章引用时需要核对。
- Goldman 称并网等待 40-70 个月(二手转述);GridLab 报告显示燃气轮机成本因数据中心需求上涨;PJM 容量价从 $28.92 涨到 $329-333/MW-day,约 11 倍。
所以"没电就开不了机"的机会成本约为电费本身的 15-20 倍(每 GW 年收入 $10-12B 对比电费 $0.6B)。这份稀缺租金确实存在,而且量级不小。但它被谁拿走了,不是 Epoch 这个 TCO 数据能回答的:可能是燃气轮机厂商(如 GE Vernova)、已拿到并网资格的开发商和带电机房房东,也可能是容量市场里的发电商,它们未必算"电力卖方"。

四、口径问题。Epoch 的"能源 7%"只是电费,变电站、UPS、发电机、冷却等电力相关资本开支都算在设施的 $1.4B 和 CapEx 里。如果把"电力层"定义为整条供电链(电费、电气设施、表后发电、并网资格),它的份额会明显高于 7%。

结论:"电费占 TCO 个位数到低两位数、远小于服务器"可以升级为多源。"电力层租金薄"不能直接从 TCO 占比推出,因为成本占比小不等于租金小;反而正因为电费占比小,需求方对电价不敏感,电力稀缺方才有提价空间。"量级远小于芯片层"在方向上大概率成立(芯片层是每 GW 约 $5B 的年化服务器成本,且毛利率高),但没有直接测量,只能作为推断。

**方法问题**:
- Epoch 是单一参数化模型,不是实测:采用美国平均电价 8.34¢、PUE 1.14、利用率 71%、全部电网供电。真实园区若走表后燃气或零售电价,能源占比会更高
- 口径:Epoch 的'能源'只含电费;电气设施、变电站、备用发电等电力相关资本开支计入设施的 $1.4B。用'电费占比'代表'电力层可分得的价值'会系统性低估
- 推论跳跃:'成本占比小'推不出'租金薄'。需求方对价格不敏感,恰恰意味着供给稀缺方有议价空间。这是需求弹性问题,文章把成本结构当成了租金分配
- '个位数百分比'对电价敏感:电价翻倍约 13%,Cloudrift 口径 14-17%。建议改为'约一成上下'
- SemiAnalysis 的 9% 和每 GPU 小时口径无法直接核到(付费墙),只能通过搜索摘要转述,可信度中等
- Cloudrift 是 GPU 云服务商,有利益相关;SemiAnalysis 卖咨询和数据模型,并有表后供电订单追踪业务,有动机强调电力稀缺(参见 electroneconomics 对其 75 GW 订单的质疑)
- 纳德拉引语的时间在多家媒体中有误写(2024 vs 2025),引用时需以 BG2 播客原期为准
- '电力租金量级远小于芯片层'没有任何独立来源做过直接比较,属于推断

**独立测量**:
- SemiAnalysis, H100 vs GB200 / neocloud TCO 系列(https://newsletter.semianalysis.com/p/h100-vs-gb200-nvl72-training-benchmarks 等):Meta 24,576 卡 H100 集群电力约占 TCO 9%,占 OpEx 约 32%;约 $0.16/$1.49 每 GPU 小时(约 11%),电价约 8.3¢/kWh。与 Epoch 同向。注意:该百分比来自搜索摘要转述,原文付费墙后,未直接核到
- Cloudrift 博客(https://www.cloudrift.ai/blog/the-true-cost-of-gpu-ownership):电费约每 GPU 每年 $4-6k(8-12¢/kWh),占年成本 14-17%,折旧占 52-55%。方向同向,但数字更高;来源是 GPU 云厂商,有利益相关
- Thunder Said Energy(https://thundersaidenergy.com/downloads/data-centers-the-economics/):在线率和利用率对经济性的影响约是电价的 5 倍;电力占(传统)数据中心 OpEx 15-25%。与'寿命/利用率 > 电价'同向
- SemiAnalysis, Onsite Gas Deep Dive(2025-12-30,https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power):AI 云每 GW 年收入 $10-12B;200 MW 早上线半年值 $1-1.2B;表后供电往往(远)贵于电网,企业有意付溢价买时间。与'电力租金薄'的推论方向相反,支持影子价格很高
- PJM 容量拍卖(https://www.utilitydive.com/news/pjm-interconnection-capacity-auction-data-center/808264/;https://www.enelnorthamerica.com/insights/blogs/pjm-2027-2028-capacity-auction-results):2027/28 年度出清 $333.44/MW-day,较 2024/25 年度的 $28.92 约涨 11 倍;无上限约 $530。折合约 1.4-2.2¢/kWh,对 TCO 占比影响很小(<2%)
- 纳德拉 BG2 播客(2025 年 11 月,https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-ceo-says-the-company-doesnt-have-enough-electricity-to-install-all-the-ai-gpus-in-its-inventory-you-may-actually-have-a-bunch-of-chips-sitting-in-inventory-that-i-cant-plug-in):有芯片插不上、缺带电机房。定性支持影子价格存在
- GridLab 燃机成本报告(https://gridlab.org/wp-content/uploads/2025/09/GridLab_Gas-Turbine-Costs-Report-1.pdf)、E&E News 报道燃机成本上涨 195%:接入速度租金部分流向燃机供应链

**搜索角度**:
- Epoch 原文复核(已核:$38B capex,$0.9B opex,$8.5B TCO,服务器 $5B,能源约 $0.6B,8.34¢,PUE 1.14,利用率 71%,寿命 3/5/7 年)
- SemiAnalysis AI 数据中心 TCO 电力占比(命中:H100 约 9% 和约 11%,原文付费墙)
- SemiAnalysis neocloud playbook 原文(公开部分无百分比拆分,未命中直接数字)
- SemiAnalysis H100 vs GB200 TCO 原文(只有定性'电力占比适中',无公开百分比)
- 通用搜索:电力占 AI 数据中心 TCO 比例、GPU 折旧(命中 Cloudrift 14-17%,以及若干 SEO 聚合站,未采信)
- IEA Energy and AI / Key Questions on Energy and AI 中电费占数据中心成本的比例(未找到 IEA 给出的 TCO 占比数字)
- Thunder Said Energy 数据中心经济学(命中:利用率影响约是电价 5 倍)
- LBNL / Uptime Institute 电费占 TCO(搜索结果中未出现可用的 AI 专项一手数字,未命中)
- 学术论文(arXiv 2509.07218 等出现在结果中,未见 TCO 占比数字,未深挖)
- 电力公司披露(未命中具体到 AI 数据中心 TCO 占比的披露)
- PJM 2027/28 容量价及对数据中心电价的影响(命中 $333.44/MW-day,无上限约 $530)
- 纳德拉'芯片插不上/缺带电机房'(命中,并发现部分报道时间误写)
- speed-to-power 溢价、表后燃机 $/MWh(命中 SemiAnalysis'不是更便宜而是更早',燃机成本上涨 195%;具体 $/MWh 溢价在付费墙后,未命中)
- 1 GW 延误每月机会成本(只命中 60 MW 每月约 $14.2M 等二手估算,来源质量低,未采信)
- AI 实验室愿付高电价的分析(Epoch/RAND 无专项命中;SemiAnalysis 命中)

## R1-energy-tco · method · 判决:降级为弱结论

**可用表述**:按 Epoch AI 的示意模型(2026-05,1GW GB200,美国平均工业电价 8.34¢/kWh,PUE 1.14,利用率 71%),电费约占 AI 数据中心年化总成本的 7%,服务器约占 60%。即便电价翻倍,或计入 PJM 创纪录的容量价,电费占比也只升到约 9%–15%;对总成本而言,GPU 寿命假设(3 年 vs 7 年,年化成本差约 $5B/GW)的影响远大于电价(翻倍约多 $0.6B/GW)。因此,电力公司通过电费收到的钱在 AI 价值链里占比不大。但这不等于电力层的租金薄:一座 1GW 园区晚通电一年,闲置算力的机会成本约为全年电费的 10 倍。所以"能马上通电"的稀缺租金可能相当可观,只是主要落在持有已供电地块和并网排位的开发商与表后发电方手里,而不是受管制的公用事业。成本占比本身不能用来比较电力层与芯片层的利润池大小。

**推理**:一、原文方法核对(WebFetch epoch.ai 原页):数字与文章一致。年化 TCO $8.5B/GW,服务器 $5,021M(60%),能源 $594M(7%)。前期 capex $37.9B,年 opex $0.9B。假设如下:电价 8.34¢/kWh,是 2024 年 EIA 各州工业电价按 Aterio 项目分布加权的结果;PUE 1.14(LBNL);利用率 71%,取 Tyler Norris 汇编的四个估计的均值;IT 寿命 5 年,厂房 14 年;CRF 0.24/0.13,折现率取计算机服务业 WACC;服务器成本来自 SemiAnalysis 的公开估计。全部为纯电网供电,未建模表后发电。作者自称这是"stylized model, not an estimate for any specific facility"。这是一个参数化的示意模型,没有样本,不是实测。能源这一项可以反推核对:594M/0.0834=7.12TWh,约等于 1GW×8760h×0.71×1.14,内部算术自洽。利益冲突:Epoch 是非营利研究机构,看不出它与电力或芯片利益相关。真正的弱点在后面。

二、参数敏感性(按原文结构自算):
(a) 电价翻倍到 16.7¢:能源约 $1.19B,TCO 约 $9.1B,占比约 13%,已进入两位数。所以"个位数百分比"这个说法不稳健。
(b) PJM 容量价:2027/28 拍卖清算价 $333.44/MW-day,按 1.14GW 峰值算约 $139M/yr,折合每度电加约 2¢。全包电价按约 10.5¢ 算,能源约 $0.75B,占比约 8.7%。若再叠加电价整体上涨到约 12–13¢,占比约 10–11%。
(c) 利用率从 71% 提到 90%:能源 ×1.27,约 $0.75B,占比约 9%。
(d) 用 7 年 IT 寿命(TCO 约 $7B)再加电价翻倍:占比约 16%。
(e) 反方向:大型数据中心的实际 PPA 或批发电价常低于工业均价,占比可能低于 7%。
结论:在任何合理假设下,能源占比都落在约 5%–16%,远低于服务器的约 50–60%。"GPU 寿命假设的影响远大于电价"这一条稳健:寿命 3↔7 年带来约 $5B 的摆幅,电价翻倍只多出约 $0.6B,差约 8 倍。

三、独立测算:搜到的都是二手或质量偏低的来源。有一个二手转述称 SemiAnalysis 测算 Meta 24,576 张 H100 集群的电费约占 TCO 9%,但 SemiAnalysis 原文付费,我没能核实。SiliconAnalysts 的计算器在默认配置下给出 4.1%,FAQ 给的范围是 10–20%,但没有说明方法。方向一致,都是"个位数到十几%",但都算不上独立的高质量测量。原始数字因此维持单源加方向旁证。

四、致命的推理问题:文章的承重点是"电力租金薄"。Epoch 测的是成本份额,不是租金或利润份额。用成本占比推出租金大小,是范畴错误。租金取决于稀缺性,与这项投入在成本里占多少无关。影子价格可以粗算:一座 1GW 园区若因没电晚一年投产,约 $21B 的服务器在闲置中贬值并占用资本,按 Epoch 自己的年化口径约 $6–7B/年,即每月约 $0.5B,大约是全年电费的 10 倍。所以谁手里有"可以马上通电的地块或并网排位",谁就能收到与全年电费同量级甚至更大的稀缺租金。这部分租金主要落到持有已供电地块的开发商、矿企转型的托管方和表后发电方手里,而不是受价格管制的公用事业。文章写的"量级远小于芯片层",就公用事业收的电费而言大致成立:英伟达约 75% 的毛利率作用在每 GW 每年约 $5B 的服务器年化成本上,对应每年数十亿美元的租金,而电费总共约 $0.6B,何况其中只有一小部分是利润。但若把"接入速度"的租金也算进电力层,这个比较就不成立了,Epoch 的数据也无法支撑这种比较。

五、其他方法问题:没有建模表后燃气发电或溢价购电,而这正是 2025–26 年"接入速度"溢价的主要表现形式;1GW 的口径是 IT 负载,设施总负载约 1.14GW,文中需要写清;服务器价格来自 SemiAnalysis 的公开估计,而服务器是最大的一项,其不确定性会直接摊薄或抬高能源占比。

**方法问题**:
- Stylized parametric model with no sample or measured facility; the authors say themselves it is not an estimate for any specific facility
- Sensitivity analysis covers only IT lifetime, not electricity price, utilization or PUE; my own calculation shows doubled electricity takes the share to about 13%, so 'single-digit percent' is not robust
- Electricity price uses the 2024 EIA industrial state average weighted by project distribution; it does not reflect PJM capacity-price increases after 2025 or regional differences (Virginia/Ohio vs Texas)
- Utilization of 71% is an average of four secondary estimates; at 90% energy cost is ×1.27
- Pure grid power; behind-the-meter gas or premium power purchases are not modeled, and that is exactly how the 'time-to-power' premium shows up
- Category error: the source measures a cost share; the article reads it as a profit/rent share. Rent is set by scarcity and the shadow price of delayed grid connection, not by cost share
- Shadow price omitted: one year of delay leaves about $21B of servers idle, an opportunity cost of about $6–7B/yr on Epoch's own annualization, about 10× the annual electricity bill
- Server prices (the largest item) rest on SemiAnalysis public estimates; their uncertainty feeds straight into the energy share denominator
- 1 GW is IT load; total facility draw is about 1.14 GW, so the article should state the basis
- No conflict of interest found (Epoch is a nonprofit research organization)

**独立测量**:
- https://epoch.ai/data-insights/ai-datacenter-cost-breakdown: original source, verified. Energy $594M/$8.5B = 7%, servers 60%; sensitivity only on IT lifetime (3y→$12B, 7y→$7B), none on electricity price
- SemiAnalysis Meta 24,576×H100 cluster, electricity about 9% of TCO (secondhand via search summary; SemiAnalysis original is paywalled, not verified; https://newsletter.semianalysis.com/p/h100-vs-gb200-nvl72-training-benchmarks does not contain this number): same direction
- https://siliconanalysts.com/tools/cluster-tco: 1,024×H100 colocation default config, electricity 4.1% of 3-year TCO; FAQ says 10–20%, no methodology: same direction but low quality
- https://www.utilitydive.com/news/pjm-interconnection-capacity-auction-data-center/808264/ and https://www.enelnorthamerica.com/insights/blogs/pjm-2027-2028-capacity-auction-results: PJM 2027/28 capacity price $333.44/MW-day; my conversion is about +2¢/kWh, pushing energy share to about 9–11%, still direction-consistent

**搜索角度**:
- Epoch original method section (fetched, verified)
- electricity share of AI data center TCO H100/GB200 (hits are mostly low-quality blogs/calculators; one secondhand SemiAnalysis 9%)
- SemiAnalysis GB200 TCO electricity percent (original paywalled, could not verify the 9%)
- PJM 2027/28 capacity auction price and data center cost impact (found $333.44/MW-day)
- time-to-power delay opportunity cost / behind-the-meter premium (only low-quality blogs, e.g. 60MW delay costing $14.2M/month, not usable as load-bearing; replaced by my own calculation)
- Not searched or not found: IEA, LBNL or Uptime giving an explicit electricity share of AI DC TCO; IEA Energy and AI gives consumption not cost shares; no utility disclosure found of AI-load margins

## R2-price-curves · counter · 判决:方向存争

**可用表述**:多个团队用不同方法测量,结论一致:达到固定能力的最便宜方式,价格每年下降约一个数量级。各家口径不同,幅度在 5× 到 50×/年之间。a16z 用 MMLU 和每 token 价格测得约 10×/年;MIT FutureTech 测得 5-10×/年;Epoch 2026 用最低每任务成本测得约 13×/年,并发现新能力刚登顶时降得最快。

前沿这一侧要分口径讲。按每 token 标价,OpenAI 旗舰从 GPT-5 的 $1.25/$10 一路涨到 GPT-6 Astra 的 $10/$50;Google 只是温和上调;Anthropic 的顶档反而比 2025 年便宜。按每任务成本,MIT 测得前沿模型跑基准的总成本每年上升 3-18×,主要原因是推理 token 暴增。但具体到单代模型,涨幅可以很小,甚至下降:GPT-5.5 标价翻倍,每任务成本只涨约 20%(Artificial Analysis 测);真实账单涨 49-92%(OpenRouter 测);GPT-6 Sol 的每任务成本反而比上一代低约一半。

因此,"商品化"和"前沿溢价"两派的分歧,确实有一部分源于他们看的是不同曲线:前者看固定能力的最低价,后者看前沿的标价或每任务成本。但"前沿涨价"并非全行业一致的规律,主要体现在 OpenAI 的定价和推理用量增长上,不宜表述为一条和固定能力价格曲线对称的、方向确定的上升曲线。

**推理**:这条论断其实是两条曲线拼在一起的,两半的证据强度差很多,要分开判。

一、固定能力的价格快速下降:这一半可以升级为多源。
- Epoch 2026 的方法是"cost frontier":在某一时点,所有可用模型里达到某个性能阈值的最低花费。所以取的是最低价,不是平均价。基准用了 5 个:AIME、Chess Puzzles、FrontierMath T1-3、GPQA Diamond、Mystery Game。它用 CAISI 的方法按不同 token 预算重建性能曲线,也就是说已经把推理长度算进去,算的是每任务成本,不只是 token 标价。
- MIT 的论文(Gundlach、Lynch、Mertens、Thompson)测的是"benchmark price",即 token 数乘以单价,基准为 GPQA-D、AIME、SWE-bench Verified。结论是年降 5-10×,同向。但它的数据来自 Artificial Analysis 和 Epoch,只能算独立团队、共用数据,不是完全独立的样本。
- a16z(Appenzeller,"LLMflation")是真正的独立团队和独立方法:用 MMLU、看每 token 价格,得出每年约 10×,同向。
- Epoch 2025 年 3 月的数据洞察给出 9×-900×/年(中位数约 50×),同向,幅度更大;不过它和 2026 那篇是同一机构。
- 我没找到任何独立测算显示"固定能力的价格在上升"。
- 要注意,各家的幅度从 5× 到 50×/年不等。"约一个数量级"大致站得住,但"13×"这个精确数字只有 Epoch 一家。

二、前沿价格不降反升:方向成立,但只在部分口径下成立,且不能归到 Epoch 名下。
(a) Epoch 2026 这篇本身并不主张前沿价格上升。它说的是"新能力短暂收溢价,而且溢价衰减很快"(刚成为 SOTA 时降 66%/季)。这和"前沿涨价"是两种不同的说法,文章不能拿 Epoch 给第二条曲线背书。

(b) 按每 token 标价看,三家走势不一样:
- OpenAI:GPT-5 $1.25/$10(2025-08)→ GPT-5.4 $2.50/$15 → GPT-5.5 $5/$30(Artificial Analysis 一手确认翻倍)→ GPT-6 Astra $10/$50(2026-09,Artificial Analysis 确认)。持续上调。
- Google:Gemini 2.5 Pro $1.25/$10 → 3/3.1 Pro $2/$12,输入涨 60%、输出涨 20%,之后持平,数据来自官方定价页。另外 Flash 档将在 2027-01-01 翻倍,这是非前沿档在涨价,信息来自二手文章,它称引自 Google 定价页;我直接取官方页面时也看到了这条公告。
- Anthropic:最高档从 Opus 4/4.1 的 $15/$75 降到新顶档 Fable 5/5.1 的 $10/$50。Opus 线从 $15/$75 降到 $5/$25,再降到 Opus 5.5 的 $4/$20。以上来自官方定价页。不过 4.7 以后换了新 tokenizer,同样文本多出约 30% 的 token,等于隐性涨了价。
- 结论:"旗舰标价逐代上调"主要是 OpenAI 的定价选择,Google 是温和上涨。Anthropic 的顶档价比 2025 年低,只是在 2025-11 降价之后,又在 Opus 之上新开了一个更贵的档位。如果按"各家当前最高档"比,2026 年三家大致收敛到 $10/$50(OpenAI、Anthropic)和 $2/$12(Google)。

(c) 每 token 价和每任务成本的方向不一致,而且幅度差很多:
- MIT 的 3-18×/年测的是在基准上跑前沿模型的总成本,主要靠推理 token 暴增驱动。它测的不是标价。
- Artificial Analysis 测 GPT-5.5:标价翻倍,但 token 用量减少约 40%,跑 Intelligence Index 的净成本只涨了约 20%。
- OpenRouter 用真实用户的"切换者队列"测 GPT-5.4 到 GPT-5.5,实际成本涨 49-92%,短提示涨得多,长提示涨得少。
- 反向证据:按 Artificial Analysis,GPT-6 Sol(max)每任务 $1.06,比 GPT-5.6 Sol 的 $1.99 低约 50%。GPT-6 Astra 和 Claude Fable 5.1 同分(53),每任务成本分别是 $3.26 和 $7.63;Astra 的 token 用量只有 Fable 的约 1/3。可见前沿每任务成本受 token 效率影响极大,不是单调上升的。

三、方法学提醒
- Epoch 取最低价,前沿那一侧取的是标价或单一旗舰。两边口径不对称,"两条曲线"有一部分是取样方式造出来的。
- 主要基准(AIME、GPQA)都是数学和科学类,有 benchmaxxing 的风险,能不能代表真实工作负载存疑。
- 2026 年这些测算的时间窗只有约 3 年。

总判断:第一条曲线升级为多源。第二条曲线方向大体成立:OpenAI 标价、MIT 每任务成本、OpenRouter 实际账单三者同向。但幅度在不同口径下差一个数量级(+20% 到 3-18×/年)。它也不是所有厂商一致的现象(Anthropic 顶档降价),还有反例(GPT-6 Sol 每任务成本下降)。所以整条论断判为"方向存争",不能当成干净的两条曲线来承重。

**方法问题**:
- Epoch 取的是达到阈值的最低价(cost frontier),前沿一侧比的是单一旗舰的标价;两条曲线取样口径不对称,'方向相反'有一部分是口径造成的
- Epoch 2026 本身没有声称前沿价格上升,只说新能力短暂收溢价、而且衰减很快;文章把第二条曲线也挂在 R2 名下,属于引用越界
- MIT 的'前沿年升 3-18×'是每任务(基准)总成本,主要由推理 token 增长驱动,不是每 token 标价;不能和 OpenAI 标价上调当成同一种现象并列
- MIT 的数据来自 Artificial Analysis 和 Epoch,与 Epoch 的数据不独立
- 主要基准(AIME、GPQA、FrontierMath)偏数学和科学,有 benchmaxxing 的风险;Epoch 自己也承认基准和真实效用的对应不完美
- 时间窗约 3 年,13×/年的外推稳定性有限;各来源幅度从 5× 到 50×+/年不等
- 前沿标价上涨主要是 OpenAI 一家的定价选择:Anthropic 顶档相对 2025 年是降价,Google 只是温和上涨
- 新 tokenizer 会让每 token 价格不可比(Anthropic 4.7 以后多约 30% token),这种隐性涨价被标价比较漏掉了
- '前沿'定义漂移:厂商在原旗舰之上新开更贵的档位(Fable、Astra),比的是'当前最高档',还是'同一产品线的下一代'?口径不同,结论就不同
- OpenAI 的价格时序和 Gemini Flash 涨价的部分细节来自二手站点;openai.com 定价页返回 403,未能一手核对

**独立测量**:
- a16z LLMflation (https://a16z.com/llmflation-llm-inference-cost/):固定 MMLU 性能下的每 token 价格每年降约 10×,与第一条曲线同向,团队和方法都独立
- Epoch 2025 数据洞察 (https://epoch.ai/data-insights/llm-inference-price-trends):固定里程碑价格年降 9×-900×,GPQA 上 GPT-4 水平每年降 40×;同向,但与 2026 那篇是同一机构
- MIT FutureTech arXiv 2511.23455 (https://arxiv.org/abs/2511.23455):Pareto 前沿上给定性能年降 5-10×(同向);前沿模型跑基准的总成本年升 3-18×,口径是每任务成本、不是标价;数据来自 Artificial Analysis 和 Epoch,只算半独立
- Artificial Analysis 测 GPT-5.5 (https://artificialanalysis.ai/articles/openai-gpt5-5-is-the-new-leading-AI-model):标价较 5.4 翻倍,token 用量少约 40%,跑 Intelligence Index 净成本约 +20%;方向同向,幅度远小于标价涨幅
- OpenRouter 切换者队列 (https://openrouter.ai/blog/insights/gpt55-cost-analysis/):GPT-5.4 换到 5.5 后,真实使用的每百万 token 实际成本涨 49-92%;同向
- Artificial Analysis 测 GPT-6 (https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra 及 GPT-6 Sol/Luna 一文):Astra 标价 $10/$50,但每任务 $3.26,约为同分 Claude Fable 5.1($7.63)的 40%;GPT-6 Sol(max)每任务 $1.06,比 GPT-5.6 Sol($1.99)低约 50%;这是前沿每任务成本可以下降的反例
- Anthropic 官方定价页 (https://platform.claude.com/docs/en/about-claude/pricing):Opus 4/4.1 $15/$75 → Opus 4.5-5 $5/$25 → Opus 5.5 $4/$20;顶档 Fable 5/5.1 $10/$50,低于 2025 年的 Opus 4;4.7 以后新 tokenizer 同样文本多约 30% token;前沿标价上涨在这家不成立(反向)
- Google 官方定价页 (https://ai.google.dev/gemini-api/docs/pricing):Gemini 2.5 Pro $1.25/$10 → 3.1 Pro $2/$12,温和上涨;Gemini 3.x Flash 将于 2027-01-01 起价格翻倍(非前沿档涨价)
- OpenAI 价格时序(二手:cloudzero.com/blog/openai-pricing;5.5 和 GPT-6 Astra 的价格经 Artificial Analysis 一手确认):GPT-5 $1.25/$10 → 5.4 $2.50/$15 → 5.5 $5/$30 → GPT-6 Astra $10/$50;2026-07-30 下调了低档 Terra/Luna 的价格,Sol 档维持不变

**搜索角度**:
- 抓取 Epoch 原文的方法细节:基准、最低价口径、token 预算(已取到)
- arXiv 2511.23455 的摘要和 HTML 全文:前沿成本上升是标价还是每任务成本(已取到:每任务)
- a16z LLMflation 原文和数字(找到,同向)
- Epoch 2025 'LLM inference prices have fallen rapidly but unequally'(找到,同向)
- GPT-5.5 定价及其与 GPT-5.4 的比较(找到)
- OpenAI 旗舰价格时序 GPT-5 → 5.4 → 5.5 → 5.6 → GPT-6 Astra(找到,二手加 Artificial Analysis 一手)
- openai.com/api/pricing 一手核对(403 失败)
- Anthropic Opus 价格时序和官方定价页(找到,反向)
- Gemini 3 Pro 对 2.5 Pro 的价格,以及官方定价页(找到,温和上涨;另发现 Flash 2027 年翻倍)
- Artificial Analysis 每任务成本和跑 Intelligence Index 的成本(找到:GPT-5.5 +20%,GPT-6 Sol -50%,Astra 只有 Fable 的 40%)
- OpenRouter 真实使用的成本分析(找到 GPT-5.5 +49-92%)
- Tom's Hardware 'token volume explodes 25-fold' 的出处(没取到正文,出处和方法未核)
- 检索'固定能力价格上升'的反向独立测算(没找到)

## R2-price-curves · method · 判决:方向存争

**可用表述**:两条曲线可以写,但要换口径。按 Epoch AI(2026-09)和 MIT FutureTech 的测算,达到固定能力水平的最低成本(已计入 token 用量)约每年下降一个数量级(Epoch 点估计 13×/年,口径敏感区间大约 9-30×;MIT 估 5-10×),但这个降幅主要发生在新能力刚出现之后,两年后降速减半。另一方面,用当时最强模型完成一项任务的成本却在上升(MIT 估年升 3-18×,样本仅 19 个月、3 个基准;Artificial Analysis 的指数运行成本也从几十美元涨到几千美元),原因主要是推理和 agentic 模式消耗的 token 暴增,而不是每 token 标价普遍上涨。旗舰标价各家不一:OpenAI 逐代上调,Google 小幅上调,Anthropic 反而降价约三分之二。所以"商品化"和"前沿溢价"两派很大程度上在描述不同的曲线:前者是固定能力的最低价,后者是前沿能力的每任务开销。不要写成"前沿 token 价格不降反升",也不要把 Epoch 列为前沿上升的来源。

**推理**:一、Epoch(R2)的方法。它测的是每个能力水平上的帕累托前沿成本,也就是"当时市面上达到该准确率最便宜的方式"。算法用 CAISI 截断法:先拿高预算运行的转录,再把预算卡在各个 token 上限,统计在上限内答对的题数。所以它算的是含 token 用量的每任务成本,而且取的是最低价,不是均价,也不是旗舰价。基准有五个主基准:AIME 模拟题、国际象棋残局、FrontierMath T1-3、GPQA Diamond、推理游戏谜题;另有六个副基准。这些全是数学、科学、游戏类的封闭题,主基准里没有 agentic 或真实工作负载。作者自己不给置信区间,原话是"reasonable but rough"(合理但粗略)。换一种跨准确率的聚合口径,季降幅就落在 42.9-58.0% 之间,所以"47%/季≈13×/年"属于点估计,区间大约在年降 9×-30×,但方向很稳。作者列出的局限:刷榜(benchmaxxing)、基准不等于真实效用、真实用户不会逐任务切换到最便宜的模型、数据只有三年。最要紧的一点:Epoch 原文明确说其数据里没有前沿成本上升的证据,前沿曲线只往外推,只是 SOTA 刚出现两年后降速减半(66%→32%/季)。所以 R2 只支撑第一条曲线,不支撑"前沿不降反升"。

二、MIT FutureTech(arXiv 2511.23455,Gundlach/Lynch/Mertens/Thompson)的方法。价格数据取自 Artificial Analysis 在 Internet Archive 上的历史快照,而且只收最低的输入/输出单价;基准成本等于 token 数乘以单价。"运行前沿模型成本年升 3-18×"来自其图 9:在 GPQA-Diamond、SWE-bench Verified、AIME 三个基准上,看当时最佳模型的推理成本,时间窗只有 2024-04 到 2025-11 约 19 个月,每个基准 13-53 个观测点。作者明说的机制是每 token 单价下降、但边际性能需要多得多的推理 token。也就是说,前沿上升的是每任务成本,驱动力是推理 token 暴增,不是标价上调。年升 3-18× 区间很宽,窗口短,对少数几个推理模型的发布时点很敏感。数据源与 Epoch 部分重叠(AA 加 Epoch 数据),独立性只算中等。

三、标价证据只来自 OpenAI 一家。OpenAI 旗舰确实逐代涨价:GPT-5 $1.25/$10,GPT-5.4 $2.50/$15,gpt-5.5(2026-04-23)$5/$30。但 Anthropic 方向相反:Opus 4/4.1 $15/$75,Opus 4.5 降到 $5/$25,Opus 4.6/4.7 持平(不过 4.7 的新分词器让同样文本的 token 数最多多出 35%,属于隐性涨价)。Google 小幅上调:Gemini 2.5 Pro $1.25/$10,3/3.1 Pro $2/$12。所以"前沿每 token 标价上升"只是厂商各自的定价选择,不是行业规律;要拿它承重,反例(Anthropic)不成立。

四、每 token 价格与每任务成本方向不同,这一点是成立的,并且是这条论断真正的支点。Artificial Analysis 的 Intelligence Index 跑一遍的成本已从几十美元涨到几千美元,原因是模型更大、推理 token 预算更大、agentic 迭代更多;MIT 也指出同一机制。注意 Epoch 的"固定能力价格"已经把 token 用量算进去,所以两条曲线的差别不在"每 token 还是每任务",而在于"同一能力水平的最低成本"对比"当时最高能力的成本"。

结论:"两条相反曲线"的框架可以用,但文章写法有三处方法问题。(a) 把"价格"说成标价,而前沿上升那条有证据的是每任务成本;(b) 用 OpenAI 单家涨价当行业证据;(c) 把 Epoch 当成前沿上升的来源,而 Epoch 原文反对这一点。改写后的版本有 Epoch、MIT、AA 三方支撑,方向一致;现在的写法不能原样承重。

**方法问题**:
- Epoch 不给置信区间,作者自认结果粗略;换一种聚合口径,季降幅在 42.9-58.0% 之间,'13×/年'应写成'约一个数量级(区间约 9-30×)'
- Epoch 主基准全是数学、科学、游戏类封闭题,没有 agentic 或编码类的真实负载,外推到企业实际花费有缺口;作者也列了刷榜风险
- Epoch 取的是帕累托前沿上的最便宜方式;真实用户不会逐任务换模型,实际支付的价格降得更慢(作者自认)
- Epoch 原文明说其数据里没有前沿成本上升的证据,文章把它和'前沿不降反升'放进同一证据链是误引
- MIT 的'前沿年升 3-18×'只基于 3 个基准、2024-04 到 2025-11 共 19 个月、每基准 13-53 个点,区间宽,对少数推理模型的发布时点敏感
- MIT 的前沿上升是每任务成本,由推理 token 增长驱动,不是每 token 单价上升;文章把它和 OpenAI 标价上调混为一谈
- MIT 价格只取最低单价,数据源是 Artificial Analysis 快照,与 Epoch 部分重叠,独立性只算中等
- OpenAI 标价逐代上调是单一厂商的定价选择:Anthropic 旗舰 $15/$75 降到 $5/$25,Google 仅 $1.25/$10 涨到 $2/$12,不构成行业规律
- 隐性涨价(Opus 4.7 新分词器多出最多 35% token)说明标价本身也不是可靠的比较口径
- 利益冲突:Epoch 和 MIT FutureTech 都是独立研究机构,未见商业利益冲突;Artificial Analysis 有商业基准业务,但不涉及方向偏向

**独立测量**:
- https://arxiv.org/html/2511.23455 (MIT FutureTech):给定性能价格年降 5-10×,与 Epoch 同向但幅度更低;最佳模型的每任务推理成本年升 3-18×,支持'前沿每任务成本上升'
- Artificial Analysis(经 tomshardware 和 arXiv 引述):Intelligence Index 跑一遍的成本从几十美元涨到几千美元,原因是模型更大、推理 token 和 agentic 迭代更多。同向支持前沿每任务成本上升;AA 也按能力档追踪最低价,并持续报告下降(如 x.com/ArtificialAnlys/status/1970251031373390292),支持固定能力降价
- https://epoch.ai/publications/the-plunging-price-of-thought:固定能力成本 47%/季,口径为每任务、含 token 用量;原文说没有前沿上升的证据。对第二条曲线是反向或中性
- Anthropic 标价时序(Opus 4 $15/$75 → Opus 4.5/4.6/4.7 $5/$25),来源 cloudzero/finout 等定价汇总页:与'前沿标价上升'反向
- Google 标价时序(Gemini 2.5 Pro $1.25/$10 → 3/3.1 Pro $2/$12),来源 benchlm.ai/google/api-pricing 等:同向,但幅度小
- OpenAI 标价时序(GPT-5 $1.25/$10 → 5.4 $2.50/$15 → 5.5 $5/$30,2026-04-23),来源 openrouter.ai/openai/gpt-5.5、apidog 等:同向

**搜索角度**:
- 读 Epoch 原文的方法部分:基准、帕累托前沿、CAISI token 截断、聚合口径敏感性、局限
- 读 MIT arXiv 2511.23455 的 HTML 全文:价格口径(最低价、token×单价)、图 9 的前沿成本样本与时间窗
- gpt-5.5 标价核实
- Anthropic Opus 4 → 4.5 → 4.7 标价时序与分词器的隐性涨价
- Google Gemini 2.5 Pro → 3 → 3.1 Pro 标价时序
- Artificial Analysis 的指数运行成本与按能力档的最低价追踪
- 未深搜:a16z 'LLMflation' 的原始数据(已知结论为同能力年降约 10×,与 Epoch 同向,未在本次重新核实)
- 未搜:OpenRouter 的实际加权支付价格数据,无法确认真实用户支付的是否在下降

## R3-lab-revenue-crossover · counter · 判决:升级多源

**可用表述**:据 Bloomberg 和 WSJ 各自看到的投资者材料,Anthropic 2026 年第二季度收入约 115-116 亿美元(初步数),OpenAI 同季约 67 亿美元,Anthropic 季度收入首次反超。Anthropic 对经云厂商转售的收入按总额确认(泄露的 S-1 显示,2025 年约 47% 的收入经 AWS 和 Google 渠道,分发费约占渠道销售的 16%),但即使全部换算成净额,Q2 仍约 107 亿美元,反超结论不变。利润方面只能谨慎表述:Anthropic 称 Q2 实现了公司自定义口径的 adjusted 经营利润(约 5.6 亿美元,剔除股权激励等项目),并预计 Q3 再次为正;OpenAI 同季含股权激励的经营亏损约 123 亿美元。两者口径不同,且 Anthropic 2025 全年 GAAP 经营亏损仍约 80 亿美元。所以「模型层内部已经分化、收入和(调整后)盈利能力向头部一家集中」这个说法有多源支撑;「利润」这个词应该限定为 adjusted、单季、未经审计。

**推理**:一、来源独立性。收入数字有两家通讯社各自看到文件:Bloomberg 2026-08-14 报道,依据它看到的文件,Anthropic Q2 初步收入「超过 $11.5B」,上年同期 $787M,Q1 $4.73B,adjusted 经营利润为正;WSJ(Berber Jin、Corrie Driebusch,约 2026-08-18/19)的数字是 Anthropic $11.6B,外加 OpenAI 告诉投资者的 Q2 $6.7B 和 $12.3B 经营亏损。两家数字只差 $0.1B,符合「初步数与细化数」的差别,不像互相转载。另外 CNBC 2026-05-20 引消息人士称 Anthropic「预计 Q2 达 $10.9B」,这是事前独立预测,方向一致。The Information 报道的 Q1 数字是 OpenAI 约 $5.7B、Anthropic $4.8B,和 WSJ 的 Q1 基数($5.7B)、Bloomberg 的 Q1($4.73B)也对得上。OpenAI 的 $6.7B 和 $12.3B 目前我只找到 WSJ 一个原始出处,其余全是转载,但 OpenAI 没有否认。

二、关键纠错:Q2 数字不在泄露的 S-1 里。Reuters 首先拿到并审阅泄露的保密 S-1,Fortune、TechCrunch、SiliconANGLE 在 2026-09-28/29 转述。S-1 是 6 月准备的,主体是 2024-2025 年报数:2025 收入 $4.6B,经营亏损 $8.06B,净亏 $42B(其中约 $34B 是非现金会计费用)。Q2 的 $11.5-11.6B 来自给投资者的材料(Bloomberg、WSJ),不是 S-1。文章如果写成「泄露 S-1 显示 Q2 收入 $11.6B」就是误引,应当改。

三、收入确认口径能不能解释「超越」:不能。S-1 经 Reuters 确认,Anthropic 对云渠道收入按总额确认,理由是自己是 principal,云厂商的分成记在营销费用里。2025 年经 AWS 和 Google 卖出的收入是 $2.16B,占总收入 47%;付给平台的分发费约 $351M,大约每 1 美元市场销售付 16 美分。按这个比例,全部改成净额只会让收入下降约 7-8%,Q2 约从 $11.6B 降到 $10.7B,仍然明显高于 $6.7B。即使用 OpenAI CRO Denise Dresser 2026-04 内部备忘录里最激进的估计(把 $30B run-rate 打到约 $22B,折约 27%),Q2 也有约 $8.5B,仍然超过 $6.7B。反过来,OpenAI 对 Azure 渠道按净额只记它的约 20% 分成,如果把这部分改成总额,OpenAI 数字会上调一些,但公开信息不足以把 $3-4B 的差距补平。结论:口径差异会缩小差距,但推翻不了 Q2 的超越;Q1 那种「接近」时期,口径差异才真正关键。

四、和官方 run-rate 是否一致:Anthropic 官方 4 月宣布 $30B run-rate,投资者材料称 7 月达 $65B(CNBC、Axios 2026-08-17)。如果 4 月月收入约 $2.5B、6 月约 $4.5-5B,单季合计约 $11B,和 $11.5-11.6B 大体吻合。

五、利润部分需要降级。(a) 「连续两个季度」:FT 2026-09-15 报道的是 Anthropic「预计」Q3 是第二个 adjusted 经营利润为正的季度,也就是 Q2 已实现,Q3 只是指引,到今天(10-05)还没有实际数。(b) adjusted 的定义:WSJ 说 $559M 计入训练成本、剔除 SBC;FT 和 Bloomberg 说 adjusted 剔除了「例外/一次性项目」,而 FT 引的 80% 以上毛利率是在扣除伙伴分成和训练成本之前。这个口径由公司自定义,无法核验。拿它和 OpenAI 含 SBC 的 $12.3B GAAP 式亏损对比,两边口径不对等。GAAP 层面,2025 年 Anthropic 本身也是 $8B 经营亏损。

六、反方声音和利益冲突。OpenAI 方面(Dresser 备忘录、Friar 对投资者的说法)攻击的是口径和增长前景,没有否认 Q2 数字本身。泄露渠道都是「给投资者的材料」,Anthropic 正处在 IPO 前推估值的阶段(上一轮 $965B 估值,目标 $2T),有动机放大正面数字;OpenAI 一方的数字同样是对投资者讲的。亚马逊和谷歌既是投资方又是渠道,Anthropic 按总额确认对它们也有利益关系。

**方法问题**:
- 来源误标:Q2 收入和 adjusted 利润来自给投资者的材料(Bloomberg/WSJ),不是泄露的 S-1;S-1 只覆盖到 2025 年报(加上可能的 Q1),文章不应写「S-1 显示 Q2 $11.6B」
- 「连续两个季度 adjusted 盈利」里 Q3 只是公司预期(FT 9/15),截至 10-05 没有实际数
- adjusted 口径由公司自定义:剔除 SBC 以及 Bloomberg 所说的「例外/一次性项目」;各报道对是否含训练成本说法不一(WSJ 说含,FT 的毛利率口径不含),无法核验
- 对比不对称:Anthropic 用 adjusted(剔除 SBC),OpenAI 用含 SBC 的经营亏损;应该用同一口径,或者明确注明口径不同
- 收入确认:Anthropic 对云渠道按总额确认,OpenAI 对 Azure 渠道按净额。经估算差异约 7-8%(S-1 的 16%×47%),最多约 27%(OpenAI 的说法),都不足以逆转 Q2 排序,但会缩小差距
- 数字是初步、未经审计的(Bloomberg 明说「preliminary,可能变动」);Q1 有 $4.73B 和 $4.8B 两个版本
- OpenAI $6.7B 和 $12.3B 实际只有 WSJ 一个原始出处(OpenAI 未否认,其余媒体都是转载)
- 利益冲突:泄露方是 IPO 前的投资者圈,Anthropic 有推高估值($965B 到目标 $2T)的动机;OpenAI 的反驳出自竞争对手内部备忘录;亚马逊和谷歌同时是投资方和渠道方
- OpenAI 的 7 月 run-rate 约 $40-41B 与 Q2 $6.7B(年化约 $27B)差距较大,可能是 7 月新模型带来的跳升(NYT 称企业收入环比 +32%),也可能有口径差异,应注意不要混用 run-rate 与确认收入

**独立测量**:
- Bloomberg 2026-08-14 https://www.bloomberg.com/news/articles/2026-08-14/anthropic-revenue-ahead-of-ipo-surges-over-14-fold-in-second-quarter :Anthropic Q2 初步收入 >$11.5B,Q1 $4.73B,adjusted 经营利润为正。依据它看到的文件,与 WSJ 互相独立,同向(证实)
- WSJ(经 TNW 2026-08-19 转述 https://thenextweb.com/news/openai-q2-revenue-anthropic-surpasses ):Anthropic $11.6B;OpenAI Q2 $6.7B(Q1 $5.7B),经营亏损 $12.3B(Q1 $9.3B)。OpenAI 数字只此一个原始出处,同向
- CNBC 2026-05-20 https://www.cnbc.com/2026/05/20/anthropic-revenue-explosive-growth-ipo-profitable-quarter.html :引消息人士事前预计 Anthropic Q2 约 $10.9B,同向(独立的事前测量)
- The Information https://www.theinformation.com/articles/openai-held-1-billion-revenue-lead-anthropic-first-quarter :Q1 OpenAI 约 $5.7B 对 Anthropic $4.8B,OpenAI 领先约 $1B。与 WSJ 的 Q1 基数一致,佐证 Q2 是首次反超
- Reuters 独家审阅泄露 S-1(2026-09-29,https://www.yahoo.com/news/articles/exclusive-anthropic-ipo-prospectus-lays-205226515.html ):2025 收入 $4.6B,47%($2.16B)经 AWS/Google,分发费约 $351M(约 16%),按 principal 总额确认。S-1 里没有 Q2 数字,只能用来校准口径
- Fortune/SiliconANGLE 2026-09-29(转述 Reuters/FT):2025 经营亏损 $8.06B,净亏 $42B(约 $34B 非现金)。与 adjusted 正利润叙事形成张力(口径不同,不算直接矛盾)
- FT 2026-09-15(经 Reuters/Investing.com、TNW 转述 https://thenextweb.com/news/anthropic-second-quarter-adjusted-operating-profit-ipo ):Anthropic 预计 Q3 为第二个 adjusted 盈利季度,是指引而非实绩;80% 以上毛利率在扣伙伴分成和训练成本之前
- CNBC/Axios 2026-08-17:Anthropic 告诉投资者 7 月 run-rate 达 $65B;结合官方 4 月 $30B,与 Q2 约 $11.5B 吻合
- 反方:OpenAI CRO Dresser 2026-04 内部备忘录(officechai/enterprisedna 转述):称 Anthropic run-rate 因总额确认被高估约 $8B(约 27%)。按此折算 Q2 仍约 $8.5B,高于 $6.7B,不推翻方向

**搜索角度**:
- Anthropic S-1 second quarter revenue OpenAI $6.7 billion:搜到 WSJ/Yahoo/PYMNTS/TNW 等多篇,大多是转载
- Anthropic revenue surpasses OpenAI quarter 2026:搜到 qz、Axios run-rate 稿
- TNW 原文:追溯原始出处为 WSJ(OpenAI 数字、Anthropic $11.6B)与 Bloomberg($11.5B)
- Axios $65B run-rate 稿:WebFetch 403,内容改由 CNBC 转述获得
- gross vs net accounting AWS Bedrock Microsoft revenue share:搜到 the-decoder、valueaddvc、SemiAnalysis
- the-decoder 原文:定性说明口径差异,没有量化
- Axios 2026-09-03 revenue chasm explained:WebFetch 403,没拿到
- Bloomberg preliminary Q2 $11.5B:确认为独立的一手报道(2026-08-14)
- OpenAI disputes Anthropic revenue $8B gross accounting:搜到 Dresser 4 月备忘录与 Anthropic 的 principal 回应
- Fortune leaked S-1 adjusted operating profit:发现 S-1 主体是 2025 年数,不含 Q2
- SiliconANGLE、Fortune 原文:泄露最先由 Reuters 获得,S-1 无季度明细
- Reuters prospectus revenue recognition principal cloud partners:拿到 47%、$351M、16% 这组可量化口径数据
- WSJ OpenAI Q2 $6.7B $12.3B:只找到 WSJ 一个原始出处,没有找到 OpenAI 反驳具体数字的报道
- The Information OpenAI revenue first half 2026:只找到 Q1 数据(OpenAI 领先约 $1B),没找到 The Information 给出的不同 Q2 数字
- FT adjusted operating income second straight quarter:确认是 Q3 预期而不是两个已实现季度
- TNW second straight quarter 原文:adjusted 剔除例外项目;没找到 $559M 的第二个独立来源(只有 WSJ/SiliconAngle 转述)

## R3-lab-revenue-crossover · method · 判决:降级为弱结论

**可用表述**:据 WSJ、Bloomberg、FT、Reuters 各自获得的投资人文件和泄露的 S-1 草稿,Anthropic 2026 年第二季度确认收入约 115-116 亿美元;据 WSJ(单一来源)报道,同期 OpenAI 约 67 亿美元,Anthropic 季度收入首次超过 OpenAI。两家的确认口径不同:Anthropic 对经 AWS、Google Cloud 渠道的收入按总额确认,OpenAI 扣除微软分成后按净额确认。即使按 OpenAI 方面指称的约 27% 高估打折,Anthropic 仍领先,但差距从约 1.7 倍缩到约 1.3 倍。利润方面,Anthropic 只有 Q2 一个已完成季度实现了剔除股权激励后的 adjusted 经营盈利(约 5.6 亿美元,约占收入 5%),Q3 盈利是公司对投资人的预测;它从未披露 GAAP 口径的季度盈利,2025 年全年经营亏损超过 80 亿美元。OpenAI 的 Q2 经营亏损 123 亿美元则包含股权激励。因此能说的是:模型层的收入在头部之间已明显分化,"模型层整体给人做嫁衣"的说法需要按公司拆开检验;但目前还不能说利润已经集中到某一家。

**推理**:一、来源独立性。Anthropic 的收入数字比"单源"强:WSJ($11.6B)、Bloomberg($11.5B)、FT 2026-09-13(给投资人的说明,$11.5B)、Reuters 和 FT 2026-09-28(泄露的 S-1,$11.5B)、CNBC 都各自报了。两套底层文件(投资人通讯、S-1 草稿)都指向同一个数,$11.5B 和 $11.6B 的差异很小,应该是四舍五入或"初步数、可能调整"的问题。Fortune 自己没有看到 S-1,是转述 Reuters/FT 的报道,不能算独立来源。OpenAI 一侧实际是单源:Q2 $6.7B 收入和 $12.3B 经营亏损只出自 WSJ(依据投资人通讯),Yahoo、Investing.com、Seoul Economic Daily、TNW 都是转载 WSJ,我没找到 The Information、Bloomberg 或 Reuters 独立核实的 OpenAI Q2 数。OpenAI 没有否认这个数字,只拿"7 月企业收入环比 +32%"和"7 月 ARR 超过 Q2 总额"转移话题,后一个说法没有给出支撑数据。
二、确认口径能不能解释"超越"。口径差异是真的,而且对外公开过:OpenAI CRO Dresser 在 2026-04-13 的内部备忘录(经 Fortune、Axios 等报道)指称,Anthropic 把经 AWS、Google Cloud 渠道卖出的收入按总额确认,高估约 $8B/$30B,即约 27%;OpenAI 则按净额确认,先扣掉给微软的分成。Anthropic 方面通过 FT 回应:它是交易的主责方,云厂商只是分销渠道,所以按总额确认合规。BofA 估算 2026 年 Anthropic 给云厂商的分成最高约 $6.4B。敏感性测算:按 Dresser 的约 27% 打折,Anthropic Q2 净额约 $8.4-8.5B,仍高于 OpenAI 的 $6.7B;如果反过来把 OpenAI 也按总额还原(假设所有收入都扣过微软 20% 分成,这是上限),OpenAI 约 $8.4B,和 Anthropic 净额基本打平,而口径一致时(两边都按总额:11.6 对 8.4;两边都按净额:约 8.5 对 6.7)Anthropic 仍领先约 27-38%。所以"超越"这个方向在口径一致的比较下站得住,但按标题直接对比 1.7 倍差距是夸大的;只有一边换口径、另一边不换的混合比较才接近打平。另外,S-1 里写了近四分之一的 2025 年收入来自两个客户,超越有很强的客户集中性。
三、和官方 run-rate 是否一致。Anthropic 对外的 run-rate 约 $30B(4 月,Amodei),5 月约 $47B(Bloomberg),7 月底约 $65B(FT)。由此推算 Q2 月均约 $3-4.5B,季度约 $11B,和 $11.5B 吻合,内部自洽。但 run-rate 本身也是按总额算的,所以这只说明数字一致,不说明口径中立。
四、利润部分是这条论断最弱的一环,有三个问题。(1)"连续两个季度 adjusted 经营利润为正"是误读。FT 2026-09-13 和 Irish Times 写得很清楚:已完成的只有 Q2 一个季度(adjusted 约 $559M),"第二个连续季度"是对当时尚未结束的 Q3 的预测,是公司在 IPO 前对股东做的安抚性说法。(2)两边口径不对称。Anthropic 的 adjusted 剔除了 SBC 等项,WSJ/TNW 都说"不清楚具体怎么算";OpenAI 的 $12.3B 亏损含 SBC。用 adjusted 盈利对比 GAAP 式亏损是苹果比橘子。没有任何来源披露 Anthropic Q2 的 GAAP 经营结果;最近一个 GAAP 数是 2025 年全年经营亏损超过 $8B。FT 提到的毛利率 80%+ 也是在扣除分销分成和训练成本之前。(3)$559M 只占 $11.6B 收入的约 5%,而 adjusted 剔除的 SBC 对一家大量用股权给研究员发薪的公司数额很大,GAAP 下很可能仍然亏损。所以"利润集中在头部一家"在 GAAP 口径下没有证据。
五、利益冲突。Anthropic 的数字主要来自公司向投资人做的 IPO 前说明,FT 明说目的是打消"现金快烧完"的担忧,属于有动机的选择性披露;泄露的 S-1 是草稿,数字被标为初步。OpenAI 的数字同样来自投资人通讯。Dresser 的备忘录则来自竞争对手的 CRO,有明确的敌对动机,但它指出的口径差异有 Anthropic 方面的回应和 BofA 的估算佐证,方向可信,$8B 这个量级未经审计。
结论:"Anthropic Q2 确认收入超过 OpenAI"这一半可以升级为多源(OpenAI 数字仍是 WSJ 单源),而且在口径一致的比较下方向成立,但必须注明总额/净额差异会把 1.7 倍压缩到约 1.3 倍。"利润集中在头部一家"这一半只能降级:已实现的只有一个季度的 non-GAAP 正值,第二个季度是预测,和 OpenAI 的比较口径不一致,没有 GAAP 证据。

**方法问题**:
- OpenAI Q2 的 $6.7B 收入和 $12.3B 亏损只有 WSJ 一个来源,其余报道都是转载,所以这次比较的一端仍是单源。
- 收入确认口径不对称:Anthropic 对云渠道收入按总额确认,OpenAI 扣除微软分成后按净额确认。BofA 估算 2026 年 Anthropic 给云厂商的分成最高约 $6.4B;Dresser 估计高估约 27%。口径一致时 Anthropic 仍领先约 1.3 倍,但按标题直接对比的约 1.7 倍是夸大的。
- '连续两个季度 adjusted 经营利润为正'是误读:已完成的只有 Q2 一个季度,第二个季度是公司在 IPO 前对投资人的 Q3 预测。
- 利润比较是苹果比橘子:Anthropic 的 adjusted 剔除 SBC 等项,计算方法未披露;OpenAI 的 $12.3B 亏损含 SBC。Anthropic 未披露任何 GAAP 季度经营结果,2025 年 GAAP 经营亏损超过 $8B。
- FT 报道的 80%+ 毛利率是在扣除分销分成和训练成本之前,属于高度调整后的口径,不能用来支持利润已经集中。
- 数字是初步的:S-1 草稿未经 SEC 审阅,Yahoo 转载明说 Q2 数字'可能调整';$11.5B 与 $11.6B 的小差异即反映了这一点。
- 利益冲突:Anthropic 的盈利说法出自 IPO 前给股东的说明,FT 明说目的是打消现金担忧,有选择性披露的动机;OpenAI 的'7 月 ARR 超过 Q2 总额'没有数据支撑;Dresser 备忘录来自竞争对手,有敌对动机。
- 客户集中度:S-1 显示 2025 年近四分之一收入来自两个客户,季度领先可能对少数大客户合同高度敏感,持续性存疑。
- run-rate 与确认收入不能混用:OpenAI 7 月 ARR 约 $41B,而 Q2 确认收入年化只有约 $27B,两者口径差异大,文章不应把 ARR 和确认收入交叉比较。

**独立测量**:
- https://finance.yahoo.com/technology/ai/articles/anthropic-surpasses-openai-q2-revenue-121706311.html — Yahoo 转载:Anthropic Q2 $11.6B(引 CNBC)、adjusted 经营利润 $559M(剔除 SBC);OpenAI Q2 $6.7B、经营亏损 $12.3B(引 WSJ)。与论断同向,但属转载。
- https://thenextweb.com/news/openai-q2-revenue-anthropic-surpasses — WSJ 报 Anthropic $11.6B,Bloomberg 报 $11.5B,两家分别报道;OpenAI 数字来自 WSJ(投资人通讯);明说'不清楚 Anthropic 的 adjusted 利润怎么算',OpenAI 亏损含 SBC。同向,但提示利润口径不对称。
- https://siliconangle.com/2026/09/29/leaked-anthropic-ipo-filing-reveals-8b-operating-loss-rapid-revenue-growth/ — Reuters 和 FT 于 2026-09-28 根据泄露的 S-1 报道:Q2 $11.5B;2025 年经营亏损约 $8B;本季度'有望'实现 adjusted 经营盈利。收入数同向,另一套文件来源。
- https://fortune.com/2026/09/29/anthropic-ipo-s-1-prospectus-income-statement/ — Q1 $4.73B、Q2 $11.5B、2025 年净亏损约 $42B(其中约 $34B 为可转换融资工具重估);Fortune 引自 Reuters/FT,不是独立看到文件,不算独立来源。
- https://www.irishtimes.com/business/2026/09/14/anthropic-tells-investors-it-will-be-profitable-for-second-straight-quarter/ — FT 2026-09-13:Q2 $11.5B;'第二个连续盈利季度'指 Q3 预测;毛利 80%+ 未扣分销分成和训练成本。收入同向;利润论断须降级(两个季度里有一个只是预测)。
- https://enterprisedna.co/resources/news/openai-anthropic-revenue-war-cro-memo-2026/ 及 https://aiweekly.co/alerts/openai-disputes-anthropic-revenue-by-billions — OpenAI CRO Dresser 备忘录:Anthropic 按总额确认,run-rate 高估约 $8B/$30B;Anthropic 回应自己是主责方。这是反向证据,会削弱超越的幅度。
- https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth 及 aimagazine(7 月底 run-rate $65B)— 官方/半官方 run-rate 路径为 $30B→$47B→$65B,与 Q2 约 $11.5B 自洽。
- https://www.investing.com/news/stock-market-news/openais-q2-revenue-growth-lagged-anthropic-as-losses-deepened-wsj-reports-4866258 — OpenAI 数字只追溯到 WSJ,未找到 The Information、Bloomberg 或 Reuters 的独立数字。

**搜索角度**:
- Anthropic S-1 泄露 Q2 收入 + OpenAI $6.7B(找到:Fortune、Yahoo、PYMNTS、TNW、SiliconANGLE)
- WSJ 原始报道及转载链(找到:Investing.com、Yahoo、Seoul Economic Daily,都追溯到 WSJ)
- Reuters/FT 获得的 S-1 草稿(找到:SiliconANGLE、Quartz、TechCrunch、Engadget)
- 总额/净额确认、AWS Bedrock/Vertex 分成、微软 20% 分成(找到:Dresser 备忘录相关报道、BofA 分成估算、Anthropic 回应自己是主责方)
- OpenAI 反驳 Anthropic 收入口径(找到:2026-04 Dresser 备忘录,经 Fortune/Axios 报道)
- Anthropic 官方 run-rate 时间线(找到:$30B→$47B→$65B,与 Q2 自洽)
- FT 关于'连续第二个季度 adjusted 盈利'的原意与 SBC 剔除(找到:Irish Times/FT 9-13,第二个季度是 Q3 预测)
- The Information 等独立的 OpenAI Q2 数字(没找到独立数字,只有 WSJ 转载)
- PitchBook/Morningstar 对泄露财报的批评(页面 403,未能读取)
- Anthropic Q1/Q2 GAAP 季度经营结果(没找到,所有来源只有 adjusted 数)
