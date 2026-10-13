# 19. AI 能力最终会趋同是真的吗 — 运行状态

- **Slug**: capability-convergence
- **运行日期**: 2026-10-12(自动 routine)
- **时效声明**: 成文标注「截至 2026 年 10 月」
- **底稿位置**: repo research/capability-convergence/(~/design/deep-research-runs/capability-convergence 为其软链)

## 2026-10 刷新要点(定题依据,均待验证)
- METR Time Horizon 1.1(2026-01 起):三方聚合站称 Claude Mythos Preview 50% 时长约 1,045 分钟(2026-04),Gemini 3.1 Pro 约 384、GPT-5.2 约 352;METR 2026-03-20 笔记:任务集饱和、建模选择可使近期模型 50% 时长下降至多 35%、80% 时长上升至多 100%;>16h 估计不可靠。GPT-5.6 Sol 预部署评估约 11.3h(二手)。
- Epoch(2026-05-29):2026-01 以来最强开源权重模型落后闭源前沿约 4 个月 / 8 ECI 点;此前(2023-01~2025-10)约 3 个月——差距略扩大。
- Arena(原 LMArena):媒体称 2026-09 闭源前沿与最强开源差距扩大到 29 Elo;2026-08-12 文本榜前三相差约 5 分、第四约 8 分(置信区间重叠)。
- Artificial Analysis 指数:最强开源 GLM-5.2 落后约 9 分(二手)。

## 「差距」的可检验定义(成文前锁定)
1. **分差**:同一基准、同一时点,头部 vs 第二梯队/开源最强的分差(含置信区间)。
2. **追平月数**:追赶者达到前沿某一分数所需月数(Epoch 式滞后)。
3. **长任务比值**:同一时长尺度上完成率之比 / time horizon 之比(比值 ≠ 分差)。
三者可以给出相反方向,文章的核心就是把它们拆开。

## 调研线(6 条;题目是「同一个问题被不同量尺给出相反答案」的测量学题,按量尺切线 + 理论线 + 输入侧线)
重叠检查:每条线独占一类证据。
1. **T 理论**——天花板效应/基准饱和的测量学(IRT、Ott 2022 基准饱和动力学)、p^n 复合与其批评(错误不独立、Ord 2025 半衰期/恒定风险率)、技术扩散追赶、S 曲线接力、Elo 统计性质。独占:原典与数学。
2. **ARENA 偏好排行榜**——Arena 时序(头部分差、CI 重叠、开源闭源 Elo 差)、Leaderboard Illusion、风格控制、用户感知饱和。独占:偏好排行数据与对其的批评。
3. **BENCH 静态基准与 AI Index**——AI Index 2025/2026 的「差距收窄」统计逐字;MMLU/GPQA/SWE-bench Verified/HLE/FrontierMath/ARC-AGI 饱和时序;厂商换头条基准。独占:静态基准成绩与年度报告统计。
4. **HORIZON 长任务与可靠性**——METR TH1.0/1.1 各模型数据、50% vs 80%、头部与追赶者在时长曲线上的月数差;pass^k(τ-bench)、Terminal-Bench、Vending-Bench、GDPval 等;可靠性复合实测。独占:长任务/可靠性数据。
5. **CATCHUP 开源与中国追赶**——Epoch 开源滞后、ECI;DeepSeek-R1 案例;蒸馏在可验证长任务上的效果与局限(含 "False Promise of Imitating" 2023);CAISI/NIST 对中国模型评估;中美差距。独占:追赶速度测量。
6. **LOCKIN 输入侧锁定**——前沿训练算力集中度(Epoch 超阈值模型计数、最大训练运行)、10× 规模负担者数量、RL 数据飞轮与人才流动证据。独占:输入侧集中度。

## 运行日志
- 2026-10-12: 取题(#19 为待研究首条)、刷新搜索 3 次、STATE 落盘。
- 2026-10-12: Round 1 启动 wf_b7ee22f7-f82(6 agents),各线落盘 lines/<key>.md。断点恢复:`Workflow({scriptPath: "<repo>/research/capability-convergence/round1.workflow.js", resumeFromRunId: "wf_b7ee22f7-f82"})`。
- 2026-10-12: **Round 1 完成**(wf_b7ee22f7-f82,6 agents,1.10M tokens,447 次工具调用,0 失败)。207 条论断、130 条承重候选,落盘 01-raw-claims.json/.md + lines/*.md。分线:T 36/22★、ARENA 30/16、BENCH 32/21、HORIZON 38/24、CATCHUP 35/25、LOCKIN 36/22。
- 2026-10-12: Round 2 启动 wf_55233b43-314(27 组 × 3 票 = 81 票,9 批 × 3 = 27 agents;三镜头逐字/反证/口径;B01 理论与数学用 sonnet,其余 opus)。断点恢复:`Workflow({scriptPath: "<repo>/research/capability-convergence/verify-round2.workflow.js", resumeFromRunId: "wf_55233b43-314"})`。
  规模依据:本题是「量尺混战型」——同一个"差距"被 Arena 偏好榜 / 静态基准 / ECI 合成指数 / 长任务 time horizon / pass^k 可靠性 / 政府私有评测六种量尺给出相反方向,且大量承重数字是调研线基于原始数据的自算(必须复算),同源同口径并成 27 组。
- 2026-10-12: Round 3 并行启动 wf_681a4639-c79(4 条单源承重实证 × 反证席/方法席 = 8 agents):R1 ECI 分差扩大、R2 METR 开源滞后拉长、R3 Arena 前沿区间失去区分力、R4 CAISI 8 个月 vs 自报 2 个月。

## 文章设计草案(Round 2 前,待验证后定稿)
核心判断候选:
1. 「趋同」的证据几乎全部来自两类量尺:已饱和的静态考卷(天花板压缩:同一能力差在 99% 基线只显示为 0.57pp)与偏好排行榜(前沿区间与能力相关≈0)。AI Index 的「x%」是 Elo 除以 Elo 绝对值,无尺度意义。
2. 换到不饱和量尺,差距不但没收窄,2026 年还在扩大:ECI 分差 5→10;长程 agentic 基准上开源/闭源比值 0.27–0.78;私有 vs 公开基准滞后翻倍;可靠性(pass^4)差距大于单次成功率差距。
3. 三种「差距」定义方向相反:追平月数大致持平(3-8 个月)、分差扩大、比值在长任务上更大——前沿加速时「月数不变」就意味着「比值拉大」。
4. 最尖锐的事实:最直接测量长任务的量尺本身已饱和/停更(METR TH1.1 16h 上限、页面 2026-09 停更、从未测 2026 开源);所以「长任务上分化」的证据是拼图,强度中等。
5. 头部之间(美国闭源前沿内部)不是趋同也不是一家独大:领先者按任务类型轮换,能维持在前沿 6 ECI 内的机构从 5 家降到 2 家(含覆盖缺口)。
6. 输入差距(训练算力约 50×、中美新增算力 21–49×)没有按比例变成能力差距(约 8 个月);算力是门槛不是保证(Meta/xAI)。追赶机制(算法效率、蒸馏、学前沿经验)真实但对长程 agent 弱。
- 2026-10-12: **Round 3 完成**(wf_681a4639-c79,8 agents,679k tokens):R1 ECI 分差扩大 双席降级(同一拟合内没收窄、2026 稳定约 10 点;「翻倍」依赖基准点,重拟合漂移约 3 点,AA 指数 2025-04→2026-04 曾收窄);R2 METR 开源滞后 反证席方向存争/方法席降级(R1 是偏低点,2025 年停在 6–9 个月,2026 空白);R3 Arena 前沿失去区分 双席降级(脱钩真实且非范围受限伪影,但 Arena 仍能排开头部,只是测的不是同一样东西,原因不可分);R4 CAISI 8 个月 反证席方向存争/方法席降级(Epoch 独立复算约 8.6 个月→多源;「针对公开考卷优化」只是推测)。产出 04-verification-round3.md/.json。
- 2026-10-12: **Round 2 完成**(wf_55233b43-314,27 agents 全成功,3.04M tokens,847 次工具调用,17 分钟)。组级票型:80 CORRECTED / 1 HOLDS / 0 REFUTED;27 组中 26 组全票需修正(G23 蒸馏 2:1),显式「判死」子论断 29 条,口径修正约 490 处。产出 02-verification-round2.json、03-verdicts-full.md、verdicts/G*.md。
- 2026-10-12: 锁定口径汇总 wf_bbd604df-5df(6 agents)→ locked/part*.md → 合并为 05-locked-calibers.md(成文唯一依据)。
- 2026-10-12: 成文(zh 手写,en 由翻译 agent 忠实翻译)、8 张内联 SVG(headless Chrome 双语渲染检查,修 2 处:图例溢出、均值虚线压数值标签)、一致性回查 agent 改约 50 处(全部为口径收紧/元叙述清除)+ 主循环处理其 5 个遗留疑点;build.py 注册四处无 WARN;只提交本期页面 + index(其余重建页面已还原以保留 TTS)。发布 8fd1fd4,Pages 部署成功,4 页 + index 200。钩子:ai-ml Day 62 单独 commit(18395fa);候选池 1 条随发布 commit。子代理消耗合计约 6.0M tokens(R1 1.10M / R2 3.04M / R3 0.68M / 锁定 0.73M / 翻译 0.18M / 回查 0.26M)。
