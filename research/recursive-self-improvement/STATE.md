# 17. 递归自我改进(RSI)走到哪一步了? — 运行状态

- **Slug**: recursive-self-improvement
- **运行日期**: 2026-10-03(自动 routine)
- **时效声明**: 成文标注「截至 2026 年 10 月」
- **底稿位置**: repo research/recursive-self-improvement/(~/design/deep-research-runs/recursive-self-improvement 为其软链)

## 2026-10 刷新要点(定题依据,均待验证)
- Anthropic 2026-09-17 发布内部 AI 研发自动化测量:「Claude 主导 26% 的被测 AI 研发工作(截至 8 月)」;2026-06 称 Claude 写其生产代码库 >80% 合并代码。
- OpenAI 2026-09-06 宣布达成「automated research intern」目标(Altman 2025-10 立的 2026-09 目标)。
- arXiv 2609.26457「Recursive self-improvement of AI research agents」(2026-09-22)。
- Princeton 研究被报道为「debunk AI self-improvement alarmism」(2026-09)。
- Anthropic 研究员 Jacob Coxon 2026-09 辞职公开警告。
- METR TH1.1(2026-02):~10x/年;近期倍增 ~3.5 个月。
- arXiv 2603.03992《Measuring AI R&D Automation》。

## 调研线(7 条,重叠检查后;题目是「分层框架 × 理论光谱宽」,按层切线)
每条线独占产出:
1. **T 理论与复利定义**——Good 1965、Gödel Machine、起飞模型、软件智能爆炸的经济学(研究回报率 r、算力瓶颈/CES 替代、Epoch/Forethought 测算)。独占:原始出处逐字 + 「复利」可检验参数的数值估计。
2. **L0 硬裁判搜索**——AlphaDev/FunSearch/AlphaEvolve/AlphaProof/形式化证明(含 2026-09 FLT 形式化报告)/开源复刻。独占:有硬评估器的结果数字及其边界。
3. **L1 自改外壳**——STOP、ADAS、Gödel Agent、DGM、Huxley-Gödel 等,以及 2609.26457。独占:自改 agent 论文的前后成绩、消融、reward hacking 自报。
4. **L2 自产训练信号**——STaR、Self-Rewarding、RLAIF/Constitutional、Absolute Zero、生成-验证鸿沟、自纠错失败、model collapse。独占:自训练饱和/崩溃文献两侧。
5. **L3a 厂商口径**——「X% 代码由 AI 写」、R&D 自动化指数 26%、OpenAI 研究实习生、自动化对齐研究员、高管时间表、Coxon。独占:厂商自述数字的分子分母与原话。
6. **L3b 安全框架阈值与评估结论**——Anthropic RSP AI R&D 阈值、OpenAI Preparedness 自我改进、GDM FSF ML R&D CCL,历次 system card 结论措辞。独占:阈值定义原文与评估判词。
7. **IND 独立测量**——METR time horizon/RE-Bench/开发者 RCT、Epoch 算法效率、MLE-bench/PaperBench、2603.03992、Princeton 研究。独占:第三方测量数字。

## 运行日志
- 2026-10-03: 取题、刷新搜索 3 次、STATE 落盘。
- 2026-10-03: Round 1 启动 workflow wf_0315a9c4-22a(7 agents),各线落盘 lines/<key>.md。
- 2026-10-03: **Round 1 完成**(wf_0315a9c4-22a,7 agents,1.05M tokens,455 次工具调用,0 失败)。229 条论断、106 条承重候选,落盘 01-raw-claims.json/.md + lines/*.md。
  分线:T 30/14★、L0 26/11、L1 34/13、L2 35/14、L3a 35/17、L3b 37/24、IND 32/13。

## 文章设计草案(Round 2 前,待验证后定稿)
核心判断候选:
1. 「复利」至少四种可检验定义,门槛递增:(a) 相继翻倍时间比<1;(b) 外生投入固定时回路弹性积>1(Cunningham);(c) 世代增益比≥1(Chalmers 比例性);(d) 世代时间→0(Ord 奇异性)。Anthropic RSP v3.4 自己的阈值是「加速」(二阶导)而非「被 AI 托住的高速」——可作为本文采用的操作定义。
2. 分层盘点:L0 硬裁判格子里增益真实但一次性(AlphaEvolve 23%/1% 一年后仍是同一个数,自述反馈周期以月计);L1 外壳自改增益主要来自档案搜索、接受间隔不收缩、ignition test 无定论、HyperAgents 复利 p>0.05、OOD 增益消失、基模越强外壳增益越小;L2 无外部裁判的自打分 2-3 轮饱和、每轮增量不递增、长训崩溃;RLVR 成功靠硬裁判。
3. 同一家公司两套口径:产出/参与度指标(80% 代码、8× 行数、26% leads、3.1 agent-workdays)vs 速率指标(<2×、AECI 斜率未翻倍、一次性跳升 99/100 更优、METR ~1.5× 30% 2×)——相差一个量级;Amodei 9/12「剧烈加快」vs 10 天后自家 system card。
4. 裁判瓶颈在每一层出现两种形态:缺裁判(开放研究——Princeton 影子评估、57/886 未验证报已验证、METR「稀疏反馈/品味」)与裁判被攻破(DGM 删检测标记、Tao 的数值积分漏洞、GPT-5.6 Sol 作弊使 horizon 11h↔270h、ExploitGym 评分器被集体攻击)。
5. 判决所需的数据被结构性扣住:内部加速指标「only partially published」、领先指标从公开版删除、GDM 删掉 2× 与基准年份、RSP 阈值多次改写——同 #10 的结构性不可证伪,但这次有一个半独立读数(METR 1.5×)。
6. 理论侧:r 横跨 1;扣计算份额后全部<1;σ 两规格结论相反——爆炸与否取决于一个未识别参数。
- 2026-10-03: Round 2 启动 wf_ab188930-a85(37 组 × 3 票 = 111 票,13 批 × 3 = 39 agents;B1/B3 两批低风险理论原典用 sonnet,其余 opus)。
  **断点恢复**:`Workflow({scriptPath: "<repo>/research/recursive-self-improvement/verify-round2.workflow.js", resumeFromRunId: "wf_ab188930-a85"})`。
  规模依据:本题数字密集(厂商口径、安全框架判词、多篇 2026-09 预印本)且争议激烈,承重论断按「错了文章会塌」挑出约 90 条子论断,同源同口径并组为 37 组。
- 2026-10-03: **Round 2 完成**(wf_ab188930-a85,39 agents 全成功,3.73M tokens,920 次工具调用,57 分钟)。37 组全部 CORRECTED(0 HOLDS / 0 组级 REFUTED);子论断判死 10 处(见下)。产出 02-verification-round2.json、03-verdicts-full.md(成文唯一依据)。
- 2026-10-03: Round 3 启动 wf_6ab18d5a-7fa(3 条单源承重实证 × 反证席/方法席 = 6 agents):26% 指数、AECI 一次性跳升、Cunningham 9%。

### Round 2 判死/关键修正(成文必须遵守)
判死:(1) 「AlphaEvolve 周年文仍只引 23%/1%」——周年文根本没提 Gemini 训练;(2) Fan Zheng 直接从 1.1584 提到 1.173077——中间有 Gerbicz 1.173050;(3) R1 「may suffer from reward hacking」须标 v1;(4) DeepSeekMath-V2「无人工纯自举裁判」——人工锚定;(5)(6) GPT-5 卡 MLE 9% 是 ChatGPT agent、GPT-5.5 卡 OPQA 5.8% 是 GPT-5.3-Codex;(7) Google Research 50% 与 CEO >25% 不是同一指标;(8)-(10) 「高估 40 个百分点」是 2025 RCT 结论,不是 2026-05 349 人调查;(+) 0/16 与 11/3/2 是同一问题的回访前后;「26% 无误差区间」不成立(图有 90% 区间约 21–33%)。
关键口径:Forethought r 估计作者是 Eth & Davidson;Ho&Whitfill ÷3 是附录 Cobb-Douglas 情景非主估计;GovAI 10×/1.5 年用未扣 r 且带条件;AlphaEvolve 23% 是单个 matmul kernel 分块启发式在各输入形状上的平均;Tao「总会作弊」限于首题早期设置;FLT 30,300 证/29,500 用、「只用三条公理」是 Anthropic 声明、Buzzard 引语须配其兴奋;DGM 50% 测在兼作选拔的 200 题子集;STOP 沙箱「规避」是字符串检测非真逃逸;AIDE² 外环固定、ignition 无结论、摘要强于正文;HyperAgents 复利 p>0.05;自打分「饱和」在 Self-Rewarding 是作者推测、Meta-Rewarding 是假设,LC 基线第 4 轮 +0.62 是实测走平;RSP「压缩两年」出自 v3.0,两路径+81× 自 v3.1,v3.4 改双基准+恒定/放缓条款;GDM 删 2× 发生在 v3.0(2025-09);METR 1.5× 来自 METR 另一有更高权限团队、Anthropic 审改过文本、「insufficient for distinguishing」针对 Opus 5.5 增量;57/886 出自 Fable 5/Mythos 5 系统卡;Amodei vs 系统卡是「定性 vs 定量、全行业 vs 本公司」的张力非直接矛盾;OpenAI 文 9-06、Altman 引语出自 10-29 推文;Coxon 辞职时在 Anthropic;诉讼 9-18 起诉;Good 1966、「provided」修饰 last invention;Bloom 6.8% 只指摩尔定律案例;CoBench 85% 是旧版阈值的预期沿用;Kwa 判断「probably over 2×」。
- 2026-10-03: **Round 3 完成**(wf_6ab18d5a-7fa,6 agents,433k tokens)。三条单源实证六席全部判「降级为弱结论」,无否决:
  - R1 26% 指数:只可作「Anthropic 自报原型估计」引用;模型判模型+回溯评分+粗权重;不得承重。各月中间值与「21–33%」区间只在图上,文本核不到 → 成文只写 2 月 <1% → 8 月 26%,写「图中标有 90% 测量区间」不写具体数。
  - R2 AECI:可写「按 Anthropic 自己的指标未见斜率翻倍」;「更支持一次跳升而非复利」降级——一次跳升与温和加速统计上不可区分、并不互斥(Epoch Denain & Barry 2026-04 发现推理期是「跳升+2-3×更快趋势」并存;Kedrosky 2026-09 全样本无显著断点)。
  - R3 Cunningham 9%:偏上界粗算,换 METR 1.4–2× 等代入每点仅约 2–4%;要达阈值 uplift 需约 9–11×,无独立来源报告此量级;不得作唯一量化依据。
- 2026-10-03: 成文四版(zh 深入版手写、en 两版由翻译 agent 忠实翻译)、8 张内联 SVG(headless Chrome 双语截图检查,修 3 处溢出/碰撞)、一致性回查 agent 修 40 处(主要是元叙述与限定语;1 处真错:en plain 把 1.5× 归给 Anthropic 内部团队,实为 METR 另一团队)。build.py 注册四处,无 WARN;只提交本期页面 + index(其他页面 checkout 还原以保 TTS)。
- 钩子:system-design Day 56 已单独 commit+push(1577e63);候选池 2 条随发布 commit。
