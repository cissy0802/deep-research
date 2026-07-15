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

### 5. 机器 Oracle 全景:业界公认的裁判有哪些,LLM 分别能把它们做大多少? ✅ 2026-07
- 页面:`machine-oracles-plain/-deep` × zh/en
- 底座:8+3 条调研线、208 论断、29 组承重论断 × 3 票对抗验证(87 票:29/29 挺过、0 推翻,40+ 处口径修正);复用 #0/#2/#3 已验证口径(AlphaProof、Meta 离线→生产漏斗、弱测试欺骗、错误趋同 ICML 2025);研究材料存本地 `~/design/deep-research-runs/machine-oracles/`
- 核心口径记录:脊柱=LLM 坐生成/提议席增益有硬数字、坐裁判席独立复测系统性缩水(判据是"坐哪把椅子"而非"用没用 LLM");Argus 消融证明器把关 0/20 vs GPT-5 当裁判 20/20(机制=低错误率×极低底率=误报淹没真报);TOGA 两次独立复测崩到 0.38%/0.3%;PrimeVul 68.26→3.09(去污染);ULT 覆盖 92.18→45.10(污染抬覆盖不抬杀伤);Kitten 无 LLM 反超 Fuzz4All;SQLancer++ 无 LLM 196 bug(difftest 线原设"SQLancer++ 含 LLM 消融"前提被纠正,干净对照改用 ShQveL 同框架/Argus 只换裁判);N-version LLM 复现 z=29.20 但三版本投票 387→131;并发格 LLM 结构性缺席(OSS-Fuzz 主流程无 TSan);curl 两幕剧 <5%→反超 15-16%(激励×工具代际调制)
- 钩子(ruthless pruning 后保留 3 条):→ 候选池 1 条(autoformalization 规约层危机/"证明⊢陈述≠陈述=意图");→ system-design Day 51《低底率下的告警系统:AI-judge 当信号检测》(backlog,源自 Argus 底率机制)+ Day 52《给混沌工程装一个正确性 oracle》(backlog,对话中现推的差分 checksum oracle 架构);另 1 条仅记运行报告(mutation testing 工业复兴 + competent programmer 假设重检)。撤回 2 条(均与目标站已有 Day 重叠):super-individual《举证责任推回提交侧》撞 Day 54 oracle 盘点;ai-ml《错误趋同/N-version》撞 Day 54 LLM-as-Judge 的 correlated errors。判据是"够格才留",非配额

### 6. "70% 转型失败"考古:上一轮转型(Agile/DevOps)的尸检报告能预测 AI-native 吗? ✅ 2026-07
- 页面:`seventy-percent-failure-plain/-deep` × zh/en
- 底座:7 条调研线、30 组承重论断 × 3 票对抗验证(90 票:30/30 挺过、20 组含口径修正、0 推翻);沿用 #0 已验证口径(DORA 2024/2025 AI 效应量与放大器、METR);研究材料存本地 `~/design/deep-research-runs/seventy-percent-failure/`
- 核心口径记录:Kotter 1995 无整体失败率、但含"第一步远超 50% 失败"的阶段性观察(不能写成"全文无百分比");Bain 的 68% 系 2018 Soul Searching 口径、2024 版配套口径为"~13% 达成不足半";Gartner 变革意愿 2022 年的 43% 与 38% 均出自 Gartner 自家出版物(非流传错误);Gallup 一线员工频繁使用 AI 为 23%(11% 系日用口径误传);QuantumBlack 约 1,000 人(非 1,700);E&V 的 5.8%→94.2% 为构造的镜像反事实;Coch & French"产量跌 20%"引文实为转述、原文 ~60→~50 件/时且增益约 14%;"Lewin 三步系死后构造"是 Cummings 2016 论点、有对手方(Burnes 2020);GE 2018 为"独立运营但全资持有"的改组且拆分最终未完成
- 钩子:→ 候选池 1 条(AI 是不是一场管理时尚——用时尚周期理论实测 AI 话语曲线并对照能力曲线);→ system-design Day 53《项目风险要按肥尾管理》(backlog,反哺);→ leadership Day 70《赞助不掉线》(backlog,反哺);→ meta-knowledge Day 66《僵尸统计》(backlog,反哺);另 1 条仅记运行报告(管理学经典实验的复现状态盘点:Harwood/Kotter 八步/Lewin 三步)

### 14. 给 Agent 看的 README:代码库上下文文件是工程必需品还是货物崇拜? ✅ 2026-07
- 页面:`agent-readme-plain/-deep` × zh/en
- 底座:5 角度调研、26 来源、124 论断提取;两轮对抗验证 35 组承重论断 × 3 票(105 票:35/35 挺过、0 推翻、30+ 处口径修正);研究材料存仓库 `research/agent-readme/`(本期运行环境为临时容器,材料改存仓库内)
- 核心口径记录:"CLAUDE.md 一万词以内"系伪引用(官方口径为 memory 页 target under 200 lines);AGENTbench 的 LLM 生成文件 -0.5/-2pp 为均值(最差 -3)、手写 +4% 对除 Claude Code 外成立、消融(+2.7%)做在 LLM 生成文件上不可移植给手写;llms.txt 的 8.8x/36,120 系 Originality.ai 口径,与 Ahrefs 137k 域名日志(97% 零请求)是两家独立研究,媒体常并成一家;Mueller Bluesky 原帖 2025-06-17(6-18 是报道日)、keywords meta tag 类比先于该帖;AGENTS.md 60k+ 查询可复跑但计文件非项目;NVIDIA 注入 PoC 仅演示于 Codex(.cursorrules/CLAUDE.md 为风险类别陈述);VS Code 默认注入自 v1.104(chat.useAgentsMdFile,与 copilot-instructions 设置是两回事);遵从率四零结果限 25-500 行、单一因变量,会话内衰减(OR=0.944)系探索性发现
- 钩子:→ 候选池 2 条(prompt injection 防御独立体检;机器可读标准的死亡模式谱系);另 1 条仅记运行报告(会话内指令衰减的预注册复现设计)

## 待研究

### 7. 自动化的反讽:40 年人因工程证据对"人握终审"的预测
- **一句话**:自动化越好,人这个终审席位退化越快——Bainbridge 1983 起的人因工程文献,对"human-in-the-loop"AI 工作流是判词还是可工程化的约束?
- **为什么适合**:主研究方向的承重假设体检——#0/#2/#3/#5 的结论都收敛到"裁决留给人",但这个席位本身会不会在自动化下退化(警觉衰减、技能萎缩、自动化自满),整条主线还没检验过;这是在攻击自己方案最薄的地方。
- **理论底座**:Bainbridge《Ironies of Automation》(1983)、Parasuraman & Riley(use/misuse/disuse/abuse, 1997)、automation complacency & bias(Parasuraman & Manzey 2010)、Endsley 态势感知/out-of-the-loop、信号检测论与底率(接 #5 Argus 机制)、技能衰退文献。
- **关键争议/正反**:航空实证(AF447、Children of the Magenta、FAA 自动化依赖报告)vs "反讽被夸大/可用适应性自动化缓解"派;医疗警报疲劳与 CDSS 覆盖率数据;2024-2025 的 AI 版新证据(内镜 AI 撤除后医生检出率下降的 deskilling 研究、LLM 辅助的认知卸载研究、Copilot 技能影响)及其方法学强度;认知强制函数(cognitive forcing functions)等干预的实效。
- **实证锚点**:Bainbridge 原文、BEA AF447 报告、NTSB/FAA 自动化报告、医疗 alert fatigue meta 分析、2025 年内镜 deskilling 研究原文、LLM 认知卸载研究一手数据。
- **复用指引**:#5 的 Argus 底率×误报机制、#2 的眼动实验、#0 的 METR 感知落差直接沿用;验证票集中在航空/医疗一手数字与 2024-2025 新研究口径上。

### 8. 企业 AI 落地实证失败率:"95% 试点失败"体检
- **一句话**:MIT NANDA"95% 企业 GenAI 试点失败"病毒式数字的方法学体检,加上企业 AI ROI 口径混战——转型难度的基率到底是多少?
- **为什么适合**:主研究方向的基率参照——和 leadership 对话时需要一个诚实的先验;该数字 2025 年病毒式传播但样本、"失败"定义、作者背景全被质疑,厂商自报 ROI 与独立测算落差极大,正是对抗验证的用武之地。
- **理论底座**:生产率 J 曲线(Brynjolfsson——GPT 落地的先亏后赚)、吸收能力(Cohen & Levinthal)、Solow 悖论谱系(IT 生产率悖论的历史对照)、技术扩散 S 曲线。
- **关键争议/正反**:NANDA 报告方法学(非同行评审、样本构成、"失败"=未达 P&L 影响的口径)vs 媒体转述层层加码;厂商自报 ROI(Microsoft/Google 案例集)vs 独立调查(Census BTOS、各国央行/统计局采用率数据);"试点炼狱"是 AI 特有还是所有企业 IT 的常态(对照 ERP/大数据时代的失败率);影子 AI(员工自带工具)对官方统计的侵蚀。
- **实证锚点**:NANDA 报告原文与逐条批评、Census Bureau BTOS 时序数据、St. Louis Fed 采用研究、Ramp 企业 AI 支出数据、历史 IT 项目失败率文献(与 #6 的 CHAOS 考古共享)。
- **复用指引**:#0 的企业采用与 ROI 口径直接沿用;与 #6 共享 Standish CHAOS 考古结论(先跑 #6 的话)。

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

### 11. 屏幕时间与青少年心理健康:Haidt 对不对?
- **一句话**:《焦虑的一代》的因果主张,经得起方法学检验吗?
- **为什么适合**:当下争议最激烈、双方都有重量级学者的题目,对抗验证格式的完美展示品;贴育儿站。
- **理论底座**:媒介效应研究方法学(相关 vs 因果)、displacement hypothesis、社会比较理论、Granovetter 式集体动力学(Haidt 的"集体行动问题"框架)。
- **关键争议/正反**:Haidt/Twenge 的时序与剂量论证 vs Odgers/Przybylski 的方法学批评(效应量≈"吃土豆"、specification curve 分析)、自然实验证据(社交媒体接入的准实验)、各国青少年心理指标趋势是否同步。
- **实证锚点**:Haidt 的公开协作文档(与批评者的逐条对账)、meta 分析效应量、英美挪威等国队列数据。

### 12. 长寿干预的证据分级
- **一句话**:雷帕霉素、二甲双胍、NAD+、禁食——把炒作与证据的落差量化出来。
- **为什么适合**:炒作密度最高的领域,厂商/网红口径 vs 独立复现的落差极大;"厂商口径"标注体系可直接复用;贴 health-longevity 站。
- **理论底座**:衰老机制理论(hallmarks of aging)、mTOR/AMPK 通路、热量限制文献谱系、证据医学分级(动物模型→观察性→RCT)。
- **关键争议/正反**:ITP(NIA 干预测试计划,金标准动物数据)哪些过了哪些没过;二甲双胍 UKPDS/TAME 之争与 2024 前后的观察性研究翻转;NAD+ 补剂人体证据薄弱 vs 市场规模;禁食/限时进食 RCT(TREAT 等)与体重外结局。
- **实证锚点**:ITP 官方结果、ClinicalTrials 注册与发表偏倚核查、补剂厂商宣称 vs 试验原文。
- **注意**:通篇需挂"非医疗建议"免责声明;人体证据与动物证据严格分档。

### 13. 指数化的终局:被动投资会破坏市场吗?
- **一句话**:被动占比过半后,"指数泡沫论"有没有实证支撑?
- **为什么适合**:Michael Green/David Einhorn 的警告流传很广但很少被逐条核查;SPIVA 数据一边倒 vs 结构性风险论,正反阵营清晰;贴 investing 站。
- **理论底座**:Grossman-Stiglitz 悖论(有效市场的信息成本内生矛盾)、价格发现与流动性提供、指数纳入效应文献、所有权集中(common ownership)反垄断争论。
- **关键争议/正反**:主动管理长期跑输(SPIVA/Morningstar Active-Passive Barometer)vs"被动扭曲定价"的实证(指数纳入溢价的衰减研究、大小盘相关性变化);"被动导致波动放大"的证据与反驳;三巨头投票权集中的治理研究。
- **实证锚点**:SPIVA 年度报告、Sammon/Coles 等价格信息含量研究、指数纳入效应 meta。

## 候选池(未排期)

- AI 是不是一场管理时尚?用 Abrahamson 时尚周期理论给 AI 话语做实测曲线(财报电话会提及/认证量/岗位名/文献计量的钟形检验),与真实能力曲线(METR 等)对照——时尚理论第一次遇到内在能力持续上升的宿主,钟形消退预测是否失效(钩子·源自 #6)
- Autoformalization 的规约层危机:当"证明⊢陈述"被验证器守死,风险全部上移到"陈述=意图"——形式数学基准半数题面错位、autoformalization 忠实率、spec-intent 鸿沟的可测性与工程后果(钩子·源自 #5)
- 神经神话为什么杀不死:学习风格、多元智能、左右脑的传播动力学——师训体系为何成为误念的主要传染源,揭穿式干预的实效边界(信念降 37% 但行为传导仅半)(钩子·源自 #4)
- ~~形式化方法的 LLM 复兴~~(已折叠进已发布 #5 机器 Oracle 全景,作为形式验证格)(钩子·源自 #3)
- Agent 协议标准化会不会重演 TCP/IP 沙漏(第 0 篇 Headless Firm 线的深挖)
- AI 基准的 Goodhart 化:数据污染、榜单收割与评测激励结构,为什么评测体系一建成就失效(可与 #10 scaling laws 的基准饱和线互补)(钩子·源自 #2)
- HRT 的兴衰与再评价(WHI 研究如何被重新解读——"证据翻转"经典案例)
- AI 时代该让孩子学什么(编程还值得学吗)
- Prompt injection 防御的独立体检:78 研究 meta 的"自适应攻击 >85% 成功率"口径核验 + 主流 agent 平台护栏(权限模式/沙箱/注入过滤)的实测拦截率——防御声称 vs 红队复测的落差(钩子·源自 #14)
- 机器可读标准的死亡模式谱系:llms.txt(97% 零请求)、keywords meta tag、P3P、Do-Not-Track——"给机器写文档"何时会死于无消费方?采用曲线与消费曲线脱钩的判据能否提前一年预警(钩子·源自 #14)
