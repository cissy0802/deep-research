# 22. AI 能接住坏发布吗 — 运行状态

- **Slug**: release-detection
- **运行日期**: 2026-10-30(BigCat 点名插队,排在 #20/#21 之前)
- **时效声明**: 成文标注「截至 2026 年 10 月」
- **运行规模**: 比标准运行小一档(token 成本):5 条调研线、约 15 组承重论断 × 3 票、单源承重实证双席审计;编排用 Agent 子代理(非 Workflow)

## 核心问题
离线验证(测试、staging、canary)漏掉的问题,上线后多快被发现?AI(统计/ML 异常检测、自动 canary 分析、LLM 根因分析)把「发布后检测」这段时间缩短了多少?
三段分开论证:检测(TTD)/ 定位(RCA)/ 缓解(回滚)。不得用 MTTR 一个数混论。

## 调研线(5 条,每条独占一类证据)
1. **CHANGE 变更与事故的基本事实**:「约 70% 来自变更」原始出处与口径;学术事故研究(云事故分类、配置变更占比);DORA 变更失败率;VOID 对 MTTR 的批判;事故由谁发现(自动告警 vs 客户)。
2. **CANARY 渐进发布与自动 canary 分析**:Gandalf、Kayenta/Netflix ACA、Google canary 分析服务、Meta/LinkedIn 发布系统;canary 统计学(样本量、最小可检测效应、序贯检验);误回滚率;canary 结构性看不见什么。
3. **DETECT 生产回归与异常检测**:FBDetect 等大厂系统的检出率/误报口径;KPI 异常检测学术线与对其基准的批评;告警疲劳与底率。
4. **RCA LLM 根因分析与 agentic SRE**:Meta 42% top-5、RCACopilot、OpenRCA/RCAEval/ITBench/AIOpsLab 等独立基准;2025-2026 厂商产品宣称 vs 独立测量。
5. **POSTMORTEM 公开复盘一手**:CrowdStrike 2024、Google Cloud 2025-06、Cloudflare 2025-11、AWS 2025-10 等,逐案抽取触发类型、是否走渐进发布、检测时间、发现来源、缓解时间、是否自动回滚,做成表。

## 运行日志
- 2026-10-30: 登记 #22(f3e2a65);STATE 落盘;Round 1 派 5 个调研子代理,产出 lines/<key>.md + lines/<key>.json。
- 2026-10-30: POSTMORTEM 线完成:11 案例 / 22 论断(curl 原文子串比对)。待核:CF 11-18 影响开始 11:20 vs 11:28;CrowdStrike 78 分钟只是发布→回滚间隔;AWS 2025-10 非发布事故应剔出分母。
- 2026-10-30: RCA 线完成:29 论断。要点:Meta 42% = 回放+web monorepo+top-5 候选 diff;RCACopilot 0.766 = 单服务 653 事件类别 Micro-F1;无证据显示 LLM 缩短 TTD。待核:AWS DevOps Agent 94%、Opus 4.6 OpenRCA 34.9%(聚合站转录)、ITBench-AA 47%。
- 2026-10-30: DETECT 线完成:28 论断。要点:FBDetect 0.005% = 子程序级 gCPU 性能回归、每 2h 跑、无 TTD 分布;point-adjust 让随机分数 SOTA;Microsoft 监控检出 96.7%(全服务)vs Teams 高严重度 55%;漏检主因无监控。待核:Gandalf 100% recall 分母、Walmart MTTD -7 分钟、FBDetect 13 年一次误报。
- 2026-10-30: CANARY 线完成:32 论断。要点:检出率数字停在 2015-2020 自评(Gandalf/CAS/Kayenta/Configerator);无大厂公开误回滚率;canary 六类盲区。待核:Gandalf 控制面 99.8% recall 分母疑为全部部署(标准算法约 94.9%);SCELM F1 1.000(~20 案例);Netflix 11s/65s 为精选案例。
- 2026-10-30: CHANGE 线完成:29 论断。Round 1 全部完成(5 线 ~140 论断)。
- 2026-10-30: 01-raw-claims.md 合并完成;抽 15 组承重论断(groups/G01–G15.md,groups.py 生成)。
- 2026-10-30: Round 2 启动:15 组 × 3 票 = 45 票;3 批(B1 G01-04+G15 / B2 G05-08+G10 / B3 G09+G11-14)× 3 镜头(逐字 V / 反证 R / 口径 K)= 9 个验证子代理;判决落 verdicts/<G>-<镜头>.md。
- 2026-10-30: Round 3 并行启动:3 条单源承重实证 × 反证席/方法席 = 6 子代理。R1 复盘汇总(TTD 中位≈3 分钟、0/11 客户发现、6/11 绕过渐进发布,派生自 11 份公开复盘);R2 Microsoft GenAI 事故人报 38.3% vs 13.7%(单篇预印本);R3 大厂检测器自评(Gandalf、FBDetect)作为「发布后检测有效」的证据。产出 r3/R*-{X,M}.md。
- 2026-10-30: 电脑睡眠中断 R1-M(已重派)、R2-M(SendMessage 续跑);已申请 keep-awake。R3-X 完成:降级——生产系统无独立复测,但 FBDetect 2024、Slack/Atoms 2025 自报;SCELM 复测 Gandalf F1≈0.87(竞品作者);Gandalf 控制面 recall 实为 ≈95%;无带分母的拦截率/误回滚率。
- 2026-10-30: R2-X 完成:单源已核(两篇均 Microsoft 数据不独立);口径不可比不得算进步;人报含内部工程师≠用户先发现;Ganatra 96.7% 说明 13.7% 非普适基线。
- 2026-10-30: R2-M 完成:降级——无 CI/检验、预览期混杂未分层、两篇均未经评审的 Microsoft 预印本、无检出时延数据。
- 2026-10-30: R1-X 完成:TTD≈3 分钟方向存争(客户报告事故检测慢 ~10.7×);「客户先发现 0/11」降级(Atlassian 2022 客户先报);全局推送绕过+检测快缓解慢=多源证实(方向);无自动回滚仅样本内(Slack/GitHub 常规部署自动回滚有效)——样本是选择出来的「漏网大事故」,成文要点:公开复盘只看得到失败。
- 2026-10-30: R3-M 完成:否决 Gandalf 控制面 99.8%(实为 37/39=94.9%)、数据面 100%(Sev0-2 代理真值)、FBDetect「13 年一次误报」、Walmart MTTD;FBDetect 可核精度 49/70=70%,漏报真值 2 起均检出未拦住;5 分钟是决策延迟非 TTD。
- 2026-10-30: B2-V 完成(G05/06/07/08/10):0 推翻;Gandalf 99.8% 分母未说明(勿断定为全部部署);Kayenta nanStrategy=replace 不是补救;TOCS「数万台」是 could have cost;Opprentice 0.66 是百度点级目标,不能当告警门槛。
- 2026-10-30: B2-K 完成:0 推翻;99.8% 与 1−2/1200/specificity/NPV 均吻合未说明;CAS 原文有「可能避免数百起 postmortem 级事故」粗估;AWS bake time 是设计参数非上界;FB 10 分钟是 canary 时长非 TTD;FBDetect 根因 71/217≈33%;1/18857 只对应短期检测列(~210 条)。
- 2026-10-30: B1-V 完成:0 推翻;Uptime 54% 电力未验证;55%/96.7%/74% 口径不同不得并列;TTD 中位 3–5 分钟(范围 1–25);「4/6 缓解>1h」不成立,明确的只有 2 案;CF-12-05 是两配置系统对比;潜伏期「6 周」查无出处;VOID 近 1 万未核。
- 2026-10-30: R1-M 完成(Round 3 全部完成):降级——按结局选样;TTD 锁定中位 3–5 分钟、范围 1–25;CF-11 TTD 3–11 分钟;「4/6」撤销,改为主要缓解中位约 2.5–3 小时;剔除 AWS/Meta 后 n=9:自动信号 6/9、全局推送 5/9 + 1 案人工绕过;Google 总时长 3h00m。
- 2026-10-30: B1-R 完成:0 推翻;Google 68% 是 top-8 触发内占比(八类合 100%)非全部 outage;ING precision 仅 0.04;Ganatra 96.7% 全严重度不可与 55% 并列,40/30% 是修复项占比;Atlassian 2022、Ai-Media 2026 客户首报;渐进发布照样出事 AFD-29、CF-2026。
- 2026-10-30: B2-R 完成:0 推翻;Gandalf 99.2% 论文自相矛盾(可疑 vs bad rollouts);TOCS 版新增 ServiceLab 漏报率约 32%;FBDetect FPR 用自身输出定义真阴性;D26 多指标推算假设独立。
- 2026-10-30: B1-K 完成:0 推翻;无监控事故 70% 代码 bug 只基于 ~9/13;TTD 从变更时刻起算为 8–13 分钟(从影响开始 3–5);「4/6」按厂商恢复锚点只 2/6。
- 2026-10-30: B3-V 完成:0 推翻;无 PA 随机 F1 0.11–0.23(四集);Walmart 63% 分母 37/58;Roy 97 例;Triangle 未验证;AIOpsLab 检测 23.07–100%;AWS 也有人工发起调查(「均由告警触发」不成立,改为「主要由告警触发」)。
- 2026-10-30: B3-K 完成:0 推翻;D09 五集、SMD 上随机 F1-PA 0.804 低于多数方法、均用事后最优阈值;Ahmed 人评=OCE 从 5 候选挑最好;Roy 标注者=作者;DrP Team 8 仅 7%;OpenRCA 同 baseline 框架 2026 模型独立复测仅 3.9–12.5%(34.9% 厂商自报);TNS 文为 PagerDuty 员工赞助投稿;「TTD 不变」是推断。
- 2026-10-30: B3-R 完成,Round 2 全部完成:45 份判决,子论断判决 397 次(231 HOLDS / 166 CORRECTED / 0 REFUTED);组级票型 44 CORRECTED / 1 HOLDS(G15-R)/ 0 REFUTED。Round 3 有 4 个数字被否决(Gandalf 控制面 99.8%、数据面 100%、FBDetect 13 年一次误报、Walmart MTTD)。另:ITBench-AA 榜首已为 56.2%;SCELM 有 FSE'25 Industry 版;AnoFusion 非独立复现。下一步:3 个锁定口径子代理 → locked/part{1,2,3}.md → 合并 05-locked-calibers.md。
- 2026-10-30: 锁定口径完成 → 05-locked-calibers.md(part1 49 子论断+案例表 / part2 37 条 / part3 36 条)。逐票合计 HOLDS 55+73+106?见各 part 统计。下一步:成文。
- 2026-10-30: 成文 zh deep/plain 写完;一致性回查子代理运行中(06-consistency-check.md)。
