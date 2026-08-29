# 10. Scaling laws 撞墙了吗? — 运行状态

- **Slug**: scaling-wall
- **运行日期**: 2026-08-25(自动 routine)
- **时效声明**: 变化极快题目,成文标注「截至 2026 年 8 月」
- **研究问题(刷新后)**: 预训练收益递减是实测事实还是融资叙事?「撞墙」叙事(2024-11 起)与其后 21 个月旗舰实测、独立测量的对抗体检。

## 2026-08 刷新要点(定题依据)
- 旗舰现状:GPT-5.6 / Gemini 3.1 Pro / Claude Opus 5·Fable 5 / Grok 4.3;顶部拥挤,composite 指数差距几个点。
- METR Time Horizon 1.1(2026):新增长任务、剔除有缺陷任务后,判进步速度 ~10x/年(2024 前 ~3x/年)——独立测量反而提速。
- Epoch:frontier LLM 训练算力 2020 起 ~5x/年;预测 2026-27 因数据中心 lead time(GW 级需 4-5 年)增速放缓——放缓的机制是基建交付而非收益递减。
- 叙事侧:NeurIPS 2025 仍在讨论 naive scaling 不达 AGI;「撞墙」与「10x/年」两种叙事并存,正是本题的张力。

## 调研线(6 条,重叠检查后)
每条线独占产出的证据类型已互斥:
1. **L1 缩放律一手谱系**(理论线)——Kaplan/Chinchilla 原文口径、Epoch 复现修正、幂律=内生递减的概念澄清、数据受限/精度缩放后续。独占:论文原文公式与措辞。
2. **L2 撞墙叙事考古**(话语线)——2024-11 报道群(Orion/Gemini)、Ilya NeurIPS、Altman "no wall"、GPT-5 发布反响、2025-2026 双向表态 + 说话者利益位置。独占:带日期的逐字引语。
3. **L3 旗舰实测时序**(能力实证线)——2024-11→2026-08 基准时序(SWE-bench V/GPQA/FrontierMath/ARC-AGI/HLE)、厂商自报 vs 独立复测口径差、FrontierMath COI、METR 时序。独占:基准数字时序。
4. **L4 test-time/RL 缩放**(推理时代线)——o1/o3/R1 曲线、log-linear 声称、单题成本、RL 缩放证据与争议(elicitation vs 新能力)、推理成本曲线可持续性。独占:推理侧曲线与成本。
5. **L5 数据墙与合成数据**——Villalobos 存量测算、Muennighoff 数据受限、model collapse 正反(Shumailov vs Gerstgrasser)、合成数据实践、robots.txt 收紧。独占:数据存量数字与坍缩文献两侧。
6. **L6 算力/成本独立测量与经济可持续**——Epoch 算力/成本/效率趋势、最大训练 run 序列、lead-time 放缓论、预训练是否仍在被 scale、融资叙事侧(可复用 #9 已验证口径)。独占:算力经济独立测量。

## 运行日志
- 2026-08-25: 取题、刷新搜索(3 次)、STATE.md 落盘。
- 2026-08-25: **Round 1 完成**(workflow wf_599b5cce-03b,6 agents,468k tokens,204 次工具调用,0 失败)。产出 151 条论断、134 源、69 条承重候选,落盘 `01-raw-claims.json` / `01-raw-claims.md`。分线统计:L1 26/18源、L2 26/30、L3 26/24、L4 23/19、L5 25/22、L6 25/21。
- 2026-08-25: Round 2 脚本写好并落盘为 `verify-round2.workflow.js`(44 组承重论断 × 3 票 = 132 票,11 批 × 3,验证 agent model=opus,refute-by-default)。**用户叫停,未启动**。

## 断点(下次从这里继续)
**下一步**:跑 Round 2 —— `Workflow({scriptPath: "<repo>/research/scaling-wall/verify-round2.workflow.js"})`(脚本自含 44 组待验证口径与一手 URL,可直接跑;判决存 `03-verification-round2.md`)。此后按流程头:Round 3 双席审计(挑单源承重实证)→ 成文四版 → build.py 注册 → 发布 → 钩子收割。

## 已成型的文章设计(供成文阶段用,勿丢)
**结构性发现候选**(待验证后定稿):
1. 「撞墙」一词在这场争论里指四件互不兼容的事——预训练幂律偏离 / 数据墙(Ilya)/ 架构墙(LeCun)/ 算力增速放缓(Epoch 的供给侧 lead-time 论),而争论双方各自只报有利的那格。Epoch 明确预测 2026-27 放缓但机制是数据中心交付周期,被广泛错引为「收益递减」。
2. 幂律本身内生递减(Kaplan 原文:参数翻倍 loss ×0.95),所以「收益递减」是 2020 年就写在公式里的事实,不构成新闻;可检验的墙只有两种(实测偏离幂律线 / 边际算力经济上不可行),而双方引用的证据没有一条针对这两种定义——**开篇「先问口径」的骨架**。
3. 预训练轴的边际转化率确实降了(GPT-4.5 下线是最硬的市场判决:最大预训练模型因经济性被撤;Epoch 估 GPT-5 总训练算力反低于 GPT-4.5),而总能力进步同期反而加速(Epoch ECI 断点 8→15 分/年;METR TH1.1 把倍增期从 165.3 天改判 130.8 天、判快 20%)。两件事同时为真,而双方的商业叙事各只需要一半。
4. 话语与行为的系统性错位:喊「scaling 时代结束」的 Ilya 拿 NVIDIA $50 亿把算力扩 10 倍;喊「没有墙」的 OpenAI 把最大预训练模型下线。(注意 Round 2 G15 专门检验这是否断章取义——Ilya 原话是「age of research, just with big computers」。)
5. 最高频引用的「撞墙实证」可能是一句记者转述:Ilya 的 "results from scaling up pre-training have plateaued" 疑为 Reuters 间接引语,其逐字原话明显更弱(G10 专验)。

**已知高风险数字**(Round 2 重点,若验不住必须降级):arXiv 2602.16763 基准饱和研究(编号可能是幻觉)、Amodei 2026-03「We don't see a wall」(仅中文转述)、ARC 成本 $4,560→约 $30,000 上修、ARC-AGI-2 的 2026 年读数(第三方聚合榜)、Shumailov「保留 10% 即稳定」、Mitchell「AGI bubble」引语。

## 复用池(前期已验证口径,可直接引)
- #9 ai-capex-1999:资本开支与融资结构口径(Cahn 序列、NVIDIA 承诺实数等)。
- #15 ai-hardware-power:电力/硬件交付口径(GE Vernova backlog、互联队列)。
- #2/#5:基准污染与 LLM-judge 口径(PrimeVul 去污染、错误趋同)。

## 发布状态
**未发布**。TOPICS.md 中 #10 仍留在「待研究」,未标已发布——下次运行会自动重拾同一题。

---

## Round 2 完成(2026-08-27)
workflow `wf_0b991a37-760`,33 agents,**30 成功 / 3 失败**(B11-compute-econ 三票全部撞 session limit,resets 2:10am)。3.26M subagent tokens、1656 次工具调用、45 分钟。

**组级判决(已验证 40 组 / 44 组)**:CORRECTED 38、HOLDS 2(G6 GPT-4「some aspects」限定语、G39 Muennighoff 4-epoch)、REFUTED 0(组级);**子论断级 18 条判死**。
产出:`02-verification-round2.json`(原始judgments)、`03-locked-calibers.md`(成文唯一依据,90 万字符)。

### ⚠️ 未验证:G41-G44(需补跑 B11)
合成数据分母陷阱(phi-4 40% vs Nemotron 98%)/ 数据供给收紧与 WSJ Orion / Epoch 供给侧 lead-time / 算力经济四组数字(4-5x/年、成本 2.4x/年、算法效率 8 个月减半、GPT-5 算力低于 GPT-4.5)。
补跑命令:`Workflow({scriptPath: "<repo>/research/scaling-wall/verify-round2.workflow.js", resumeFromRunId: "wf_0b991a37-760"})` —— 30 个已完成 agent 走缓存,只重跑 B11 三票。

### 被验证判死的关键项(绝不可按原强度写入)
1. **「Ilya 一边说 scaling 结束、一边买 10 倍算力」是伪矛盾**(2 票判死)——他原话是「回到研究的时代,只不过带着大计算机」,并明确承认放大规模「确实会带来不同」;NVIDIA 新闻稿中他说「我们有值得放大的研究」。**原计划的结构性发现 #4 作废**。可成立的替代角度:(a) 刻度漂移——他口中「够用的算力」不到一年抬高一个数量级;(b) SSI 至 2026-08 无公开论文或产品,其研究主张无从被外部检验。
2. **「Orion 只比 GPT-4 好 20%」查无一手**——20% 是训练进度口径(完成 20% 训练时已近 GPT-4),不是提升幅度。(Box CEO Levie 说的 GPT-4.5「约好 20%」是对 GPT-4o 的另一件事,不可混用。)
3. **「Claude Opus 4.5 首个破 80%」不成立**——Anthropic 2025-05 就报过 Sonnet 4 在高算力配置下 80.2%;80.9% 只能说「首个在不加并行测试时计算的标准配置下越过 80」,且官方 bash-only 榜单同模型读数是 76.80%。
4. **「Claude Fable 5 声称 SWE-bench 95.0%」查无实据,不得写入**。另注:Anthropic 2026 年两次旗舰发布已完全不报 SWE-bench Verified(改报 Frontier-Bench / ARC-AGI-3 / OSWorld 2.0 等)。
5. **ARC 成本上修方向搞反了**——$4,560/题是 2025-12-10 按 o3-pro 价重算后的**下修**结果;发布当时高算力档成本 ARC 明说不可得;中间 2025-03 按 o1-pro 价重估时媒体报道过「可能约 3 万美元」。
6. **o1 跑基准 $2,767.05 vs GPT-4o $108.85 查无一手**(2 票判死),不得使用;可替代的实测是 ARC Prize 2025-04 的 o3 每题 $1.22–$2.52 vs o4-mini $0.05–$0.23。
7. **Shumailov 那句 "indiscriminately...can lead to" 是 Nature 编辑导语,不是摘要**——作者自己的摘要更强:"irreversible defects"、"tails of the original content distribution disappear"。修正方向与原设想相反。
8. **ProRL 不是干净的反例**——其论文自己写明数学域「pass@1 改善而 pass@128 常常下降」,与 Yue et al. 观察一致;扩张只出现在起点弱的域,且起点模型已被 R1 蒸馏过。
9. **Vinyals 帖中 "NeurIPS '25 talk" 是笔误**,实为 NeurIPS 2024——正是 Ilya 说 "pre-training as we know it will end" 的那场 Test of Time 演讲。

### 被验证加固的关键项
- **G10 坐实**:Ilya 的 "plateaued" 确系路透记者间接引语(全句无引号),他打引号的原话只有两句,其中 "Scaling the right thing matters more now than ever" 是 **pro-scaling** 的——「撞墙最高频实证」是一句转述,且当事人原话方向更弱。
- **G2 空白检验坐实**:截至 2026-08 **未检索到任何公开实证**显示前沿模型 loss 实测点系统性偏离拟合幂律线;且该检验在公开信息下**结构性不可证伪**(前沿闭源模型的 N、D 与同口径 loss 均不公开,loss 跨语料/分词器不可比)。正面证据只有厂商自述(GPT-4 报告、Llama 3 论文)。这是本文最强论点之一。
- **G2 修正**:「不可约项 E 2020 年就写在公式里」不成立——Kaplan 2020 的拟合式没有 E、外推趋于零损失;带常数项是 Henighan et al. 2020 与 Chinchilla 2022 的事。2020 年写死的是幂律指数蕴含的边际递减(参数翻倍→loss ×0.95)。
- **G1 修正**:Kaplan 摘要原文是 "with **some** trends spanning more than seven orders of magnitude";且「performance must flatten out」必须整句引——原句主句是「上端未见任何偏离迹象」,让步从句才是走平,单摘后半句是把作者主张翻面。

---

## ✅ 已发布(2026-08-28)
四个页面全部 200,index 中英条目已上线:
- https://hub.cissychen.com/deep-research/scaling-wall-deep.html
- https://hub.cissychen.com/deep-research/scaling-wall-deep.en.html
- https://hub.cissychen.com/deep-research/scaling-wall-plain.html
- https://hub.cissychen.com/deep-research/scaling-wall-plain.en.html

commit 46edbda(只提交本期页面 + index,避免剥掉全站已烘焙 TTS)。
一致性回查抓到 26 处偏差并全部修复,其中一条判死项(「a pause, not a halt」误挂 Epoch)
曾溜回四份文稿;三条未进验证流程的引用(Nadella 播客、Epoch 算力荒、Burry 折旧)已标【未验证】。

**⚠️ TOPICS.md 的「待研究」区现已为空** —— 下次 routine 运行会无题可取,需 BigCat 从候选池升级排期。
