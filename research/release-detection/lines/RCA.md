# 调研线 RCA:LLM 根因分析与 agentic SRE —— 宣称 vs 独立测量

截至 2026 年 10 月(调研日 2026-10-30)。来源分级:同行评审 / 官方一手 / 厂商自报(厂商口径)/ 从业者博客 / 媒体转述 / 分析机构。
"承重" = 若此条错,主文叙事会变。"叙事":A = AI 显著缩短发布后定位/检测;B = 宣称被口径放大 / 独立测量远低;C = 中性/口径说明。

---

## L1. Meta AI 辅助根因:42% 是 top-5、回放、限 web monorepo、限"代码变更"候选
- 论断:Meta 的 42% 是**回放评估(backtesting)**,分母为与 web monorepo 相关的**历史 investigation**,只用"调查创建时可用的信息",判定为**根因落在 top-5 候选代码变更中**;不是 top-1,不是全部事件,不是线上实测。模型为微调的 Llama 2 7B,先用启发式检索把候选从数千缩到数百。
- 原文:"Based on exhaustive backtesting, with historical investigations and the information available at their start, 42% of these investigations had the root cause in the top five suggested code changes." / "Our testing has shown this new system achieves 42% accuracy in identifying root causes for investigations at their creation time related to our web monorepo." / "The biggest lever to achieving 42% accuracy was fine-tuning a Llama 2 (7B) model using historical investigations for which we knew the underlying root cause."
- URL:https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/
- 日期:2024-06-24
- 来源类型:官方一手(工程博客,非同行评审)
- 承重:是
- 叙事:C/B(常被转述为"42% 准确率",省略 top-5 与回放)

## L2. Meta 自认风险:可能误导工程师,用置信度过滤"牺牲覆盖换精度"
- 论断:Meta 承认 AI 根因可能给出错误根因误导工程师,并对低置信答案不展示——意味着 42% 之外还有一个未公开的"覆盖率"(展示了多少 investigation)维度。
- 原文:"it can reduce effort and time needed to root cause an investigation significantly, but it can potentially suggest wrong root causes and mislead engineers." / "We also rely on confidence measurement methodologies to detect low confidence answers and avoid recommending them to the users – sacrificing reach in favor of precision."
- URL:同 L1
- 日期:2024-06-24
- 来源类型:官方一手
- 承重:中
- 叙事:B

## L3. Microsoft Ahmed et al. (ICSE 2023):4 万+ 事件上用词汇/语义相似度评估,人评正确性 2.28–3.16 / 5
- 论断:该研究在 Microsoft 40,000+ 事件上微调 GPT-3.x 生成根因与缓解文本,自动指标是 BLEU/ROUGE 等文本相似度,不是"是否找对根因";对 50 个近期事件的事故 owner 人评中,OpenAI 模型正确性评分 2.28–3.16(1–5 分),>70% owner 打 3 分及以上。这是"生成一段像样的根因描述",不是定位准确率。
- 原文:"We do a rigorous study at Microsoft, on more than 40,000 incidents and compare several large language models in zero-shot, fine-tuned and multi-task setting using semantic and lexical metrics." / "Though the correctness score of the OpenAI models ranges from 2.28 to 3.16, several OCEs pointed out that the models recommend beneficial root causes and mitigation plans." / "More than 70% of incident owners gave three or above for the recommendations of the models."
- URL:https://arxiv.org/abs/2301.03797
- 日期:2023-01(ICSE 2023)
- 来源类型:同行评审(作者为 Microsoft 员工/实习生)
- 承重:中
- 叙事:C

## L4. RCACopilot (EuroSys 2024):"RCA accuracy up to 0.766" 实为单服务、653 事件、根因**类别**分类的 Micro-F1
- 论断:常被引的 0.766 是 Microsoft Transport(邮件)服务一年 653 个事件上预测"根因类别"的 Micro-F1(Macro-F1 仅 0.533);且依赖每个团队手工构建的诊断 handler。24.96% 的事件属于新根因类别。直接用 GPT-4 prompt 的 Micro-F1 仅 0.026。
- 原文:"Our evaluation demonstrates that RCACopilot achieves RCA accuracy up to 0.766." / "RCACopilot achieves 0.766 and 0.533 for Micro-F1 and Macro-F1 separately when predicting the root cause category of cloud incidents" / "We collect a one-year dataset of 653 incidents from Microsoft's Transport service" / "incidents with a new root cause category account for 24.96% (163 among 653) of all incidents."
- URL:https://arxiv.org/abs/2305.15778
- 日期:2023-05 预印 / EuroSys 2024
- 来源类型:同行评审(Microsoft 自家系统)
- 承重:是
- 叙事:B(摘要用 "accuracy" 一词,正文是类别 F1)

## L5. RCACopilot 部署的是"诊断信息收集"模块(4 年、30+ 团队),根因预测只在单服务推出
- 论断:长期大规模部署的是自动化收集诊断信息(非 LLM 根因);LLM 根因预测模块仅 "rolled out in the Transport service"。
- 原文:"We have successfully deployed RCACopilot's diagnostic information collection module across over 30 teams within Microsoft, where it has been in active use for over four years." / "The root cause prediction module has also been rolled out in the Transport service."
- URL:https://arxiv.org/abs/2305.15778
- 日期:2024(EuroSys 2024)
- 来源类型:同行评审
- 承重:中
- 叙事:B

## L6. AIOpsLab (MLSys 2025, Microsoft):受控故障注入,RCA 任务最佳 45.45%,缓解 54.55%;检测任务 LLM 69–100%
- 论断:在 Microsoft 自建的 Kubernetes 微服务故障注入基准(48 个问题)上,GPT-4 等 agent 的 RCA 准确率 9.09%–45.45%,缓解 0%–54.55%;检测(二元判断有无故障)69.23%–100%,定位 top-1 30.77%–61.54%。传统非 LLM 方法(MKSMC 检测 15.38%,PDiagnose 定位 15.38%)更差。样本量小(每类十余题),非真实生产事件;"检测"为给定已注入故障环境下的二元问答,无误报率/真实流量。
- 原文:"FLASH achieves the highest accuracy among all agents. Although GPT-3.5-TURBO completes the tasks the fastest, it has the lowest accuracy at 15.25%." / "The detection task, being a binary choice question, should be the simplest task ... However, as shown in Table 4(a), only FLASH answers all the detection problems correctly." / "The RCA and mitigation tasks prove to be the most challenging for the agents." / Table 4(c): "GPT-4-W-SHELL 40.90% ... REACT 45.45% ... FLASH 36.36%"
- URL:https://arxiv.org/abs/2501.06706
- 日期:2025-01(MLSys 2025)
- 来源类型:同行评审(Microsoft 自建基准,自家 agent FLASH 参评)
- 承重:是(唯一同时测检测/定位/RCA/缓解四段的基准)
- 叙事:B/C

## L7. OpenRCA (ICLR 2025):335 个真实系统故障,最佳 Claude 3.5 + RCA-agent 仅 11.34%
- 论断:OpenRCA 335 个故障(来自三套企业系统,68GB 遥测),要求根因要素(时间、组件、原因)全部正确才计分;最佳 Claude 3.5 Sonnet + RCA-agent 11.34% 全对,17.31% 部分对;纯 prompt 最佳 Gemini 1.5 Pro 7.16%。无人类 SRE 基线。
- 原文:"Even with the specially designed RCA-agent, the best-performing model, Claude 3.5, solved only 11.34% failure cases." / "OpenRCA includes 335 failures from three enterprise software systems, along with over 68 GB of telemetry data (logs, metrics, and traces)." / "current models can only handle the simplest cases."
- URL:https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf
- 日期:2025(ICLR 2025)
- 来源类型:同行评审(Microsoft + CUHK)
- 承重:是
- 叙事:B

## L8. Anthropic 在 Opus 4.6 发布页把 OpenRCA 当卖点;聚合站转录 34.9%(待核)
- 论断:到 2026 年,模型厂商开始在发布页报告 OpenRCA,口径为"全部根因要素匹配才得 1 分"、"在基准作者 harness 上跑、已提交官方验证"。第三方聚合站 llm-stats 记录 Opus 4.6 为 0.349,标注 "Self-reported",未验证。即从 11.34%(2024 末)到 ~35%(2026-02)提升约 3 倍,但仍是三分之一。
- 原文(Anthropic):"Opus 4.6 excels at diagnosing complex software failures." / "For each failure case in OpenRCA, Claude receives 1 point if all generated root-cause elements match the ground-truth ones, and 0 points if any mismatch is identified. ... The benchmark was run on the benchmark author's harness, graded using their official methodology, and has been submitted for official verification."(llm-stats:"0.349",验证状态 "Self-reported1" / "StatusUnverified")
- URL:https://www.anthropic.com/news/claude-opus-4-6 ;https://llm-stats.com/benchmarks/openrca
- 日期:2026-02(发布页);llm-stats 访问于 2026-10-30
- 来源类型:厂商自报(数字在图表中,本调研未能从页面文本直接读到 34.9,经聚合站转录)
- 承重:中
- 叙事:A(进步)/ 需验证

## L9. OpenRCA 2.0(2026-06):11 个前沿模型精确根因集合平均仅 20.7%;"定位到服务"76.0%,但有因果链支撑的只 61.5%
- 论断:OpenRCA 2.0(500 例,故障注入 + 逐步因果标注)显示,"至少找对一个根因服务"(宽松)与"精确根因集合"(严格)差距巨大(76.0% vs 20.7%),且相当部分"找对"没有被验证过的传播路径支撑——"未落地的诊断(ungrounded diagnosis)"。说明宽松口径会大幅高估可信度。
- 原文:"Across 11 frontier LLMs, recovering the exact root-cause set succeeds in only 20.7% of cases on average." / "agents identify at least one correct root-cause service in 76.0% of cases, but ground that service in a verified causal propagation path to the observed symptom in only 61.5%. Outcome-only evaluation hides this failure mode"
- URL:https://arxiv.org/abs/2606.27154
- 日期:2026-06-25
- 来源类型:预印本(未同行评审)
- 承重:是(口径敏感性的最好例证)
- 叙事:B

## L10. 对 OpenRCA 的 1,675 次 agent 运行失败分析:幻觉式数据解读跨模型普遍存在
- 论断:2026 年一项过程级分析在 OpenRCA 上跑 5 个模型共 1,675 次,发现最常见失败是"幻觉式数据解读"和"探索不完整",且不随模型能力档位消失;仅靠 prompt 工程无法消除。
- 原文:"the most prevalent pitfalls, notably hallucinated data interpretation and incomplete exploration, persist across all models regardless of capability tier, indicating that these failures originate from the shared agent architecture rather than from individual model limitations." / "prompt engineering alone cannot resolve the dominant pitfalls"
- URL:https://arxiv.org/abs/2602.09937
- 日期:2026-02-10
- 来源类型:预印本
- 承重:中
- 叙事:B

## L11. OpenRCA 上的规则挖掘:Full Score 14.10 → 35.90(留出 cloudbed),结论仅限 OpenRCA
- 论断:2026-07 预印本显示,在 OpenRCA 某留出子系统上,从审计报告挖出的规则把 Full Score 从 14.10 提到 35.90(人工规则 24.36),但作者明言挖掘依赖标签、结果特定于 OpenRCA——说明基准分数对"程序/领域知识注入"高度敏感,也提示过拟合基准的风险。
- 原文:"Rules mined from the audit reports of one Market cloudbed raise Full Score on a held-out cloudbed from 14.10 to 35.90, surviving correction for multiple testing, against 24.36 for manual rules" / "Mining is label-supervised, and all results are specific to OpenRCA."
- URL:https://arxiv.org/abs/2607.13548
- 日期:2026-07-15
- 来源类型:预印本
- 承重:否
- 叙事:C

## L12. 基准作者自身的反方:Traversal 称 OpenRCA "不是根因分析"
- 论断:AI SRE 厂商 Traversal 批评 OpenRCA 只考"有界静态遥测上的模式匹配",部分故障根本无法从遥测中恢复、因果归属本身有歧义——即低分不一定代表生产能力,但也意味着高分不代表生产能力。(注意:批评者是厂商,受益于"基准不代表我们"的叙事;页面无日期)
- 原文:"OpenRCA evaluates pattern matching over bounded, static telemetry artifacts." / "The fault is not recoverable from the telemetry." / "selecting a labeled answer is not the same as performing root cause analysis."
- URL:https://www.traversal.com/blog/openrca-isnt-root-cause-analysis-why-that-matters
- 日期:未标注(约 2026)
- 来源类型:厂商(从业者博客)
- 承重:否
- 叙事:C(基准效度之争,双刃)

## L13. ITBench(IBM,ICML 2025):真实环境 SRE 场景,GPT-4o 诊断 pass@1 仅 13.81%,去掉 trace 降至 9.52%
- 论断:IBM ITBench 在 42 个 SRE 场景(Kubernetes 故障注入)、每场景每模型 10 次运行上,最佳 GPT-4o 诊断 pass@1 13.81%,缓解 11.43%;去掉 trace 后诊断 9.52%、缓解 2.86%——可观测性数据的完备度直接决定 AI 定位能力。
- 原文:"agents powered by state-of-the-art models resolve only 13.8% of SRE scenarios, 25.2% of CISO scenarios, and 0% of FinOps scenarios." / "GPT-4o consistently outperforms the other models, achieving the highest pass@1 scores for diagnosis (13.81%) and mitigation (11.43%)" / "GPT-4o's pass@1 in diagnosis falls from 13.81% with traces to 9.52% without them, and mitigation plummets to 2.86%."
- URL:https://arxiv.org/abs/2502.05352
- 日期:2025-02(ICML 2025 / PMLR 267)
- 来源类型:同行评审(IBM 自建基准)
- 承重:是
- 叙事:B

## L14. ITBench-AA(Artificial Analysis × IBM,2026-05):前沿模型根因识别仍 < 50%,最佳 47%
- 论断:2026-05 的 SRE 排行榜(59 个任务,含 19 个留出任务),评分为"全召回下的精度"(漏掉任一真根因即 0 分);Claude Opus 4.7 47%、GPT-5.5 46%、Qwen3.7 Max 42%;无人类基线;更长的 agent 运行不带来更高分。
- 原文:"Claude Opus 4.7 (Adaptive Reasoning, Max Effort) leads at 47%, followed by GPT-5.5 (xhigh) at 46% and Qwen3.7 Max at 42%" / "Scoring uses average precision at full recall." / "if a model misses any of the ground-truth root causes, it scores 0.0 for that repeat."
- URL:https://artificialanalysis.ai/articles/itbench-aa-launch
- 日期:2026-05-27
- 来源类型:分析机构(与基准方 IBM 合作;经 WebFetch 摘录,未二次逐字核对)
- 承重:是(最新 SOTA)
- 叙事:B(进步但仍不过半)

## L15. Microsoft Ahmed 系后续:ReAct agent 在 100 个抽样事故上人工标注约 34–38 个"正确",检索基线错误答案中 49% 为幻觉
- 论断:Microsoft 团队(Roy et al. 2024)对 100 个抽样生产事故人工标注:检索基线/CoT/ReAct 正确数 38/38/34;检索基线的错误预测中 49% 属幻觉(编造"已重启集群"等未发生的处置),ReAct 降到 6%,但代价是更多"证据不足"拒答(39 例)。
- 原文:"26% (10/38) of the correct predictions made by the RB (k=10) contain hallucinations, while it is < 1% for CoT and ReAct S+Q BM25. Similarly, 49% (29/59) of the RB (k=10)'s incorrect predictions are hallucinations, dropping to 18% (11/59) for CoT and 6%(4/63) for ReAct. Overall, ReAct has the highest precision among the 3, but this comes at the cost of lower overall accuracy." / "we randomly sample 100 incidents from the evaluation set"
- URL:https://arxiv.org/abs/2403.04123
- 日期:2024-03
- 来源类型:预印本 / 工业论文(Microsoft)
- 承重:中
- 叙事:B

## L16. Microsoft Triangle(ASE 2025):"准确率最高 97%、TTE 最多降 91%"是分团队最好值,且是**分派(triage)**不是根因
- 论断:Triangle 解决的是"事故该派给哪个团队",指标是 Time to Engage(TTE);97% 与 91% 均为 "up to",来自不同团队(91% TTE 降幅来自分派准确率最低 82% 的 Team B)。属于检测之后、定位之前的一段。
- 原文:"TRIANGLE significantly improved incident triage accuracy (up to 97%) and reduced Time to Engage (TTE) by as much as 91%" / "Team B experiences the most dramatic impact, with a 91% reduction in TTE." / "While Team B's accuracy is slightly lower at 82%"
- URL:https://conf.researchr.org/details/ase-2025/ase-2025-papers/22/Triangle-Empowering-Incident-Triage-with-Multi-Agent
- 日期:2025(ASE 2025)
- 来源类型:同行评审(Microsoft 自家生产系统)
- 承重:中
- 叙事:A(分派段确有加速)/ C(口径)

## L17. Azure 博客:Triangle 本地分派 6 个团队生产、"agents achieving 90% accuracy",单一团队 TTM 降 38%
- 论断:Microsoft 官方博客(2025-03)称本地分派系统 2024 年中起在 Azure 生产,至 2025-01 有 6 个团队上线;"90% 准确率"(分派接受/拒绝判断)与"一个团队 TTM 降 38%"——TTM 是缓解时间,混合多段,且只有一个团队。
- 原文:"The Local Triage system has been in production in Azure since mid-2024. As of Jan 2025, 6 teams are in production with over 15 teams in the process of onboarding. The initial results are promising, with agents achieving 90% accuracy and one team saw a reduction in their TTM of 38%"
- URL:https://azure.microsoft.com/en-us/blog/optimizing-incident-management-with-aiops-using-the-triangle-system/
- 日期:2025-03-06
- 来源类型:官方一手(厂商口径)
- 承重:中
- 叙事:A/C

## L18. Meta DrP(2025-12):**非 LLM** 的代码化排障手册平台,MTTR 平均改善 20%;LLM 集成仍是"进行中"
- 论断:Meta 自己大规模生产的自动排障平台 DrP(2000+ analyzer、300+ 团队、日均 5 万次分析、5 年生产)靠代码化 playbook + 统计/ML(维度分析、异常检测、代码/配置变更排序),不是 LLM;MTTR 平均改善 20%,深度接入(≥10 个 analyzer)的团队 50–80%。MTTR 的定义是"解决时间戳 − 检测时间戳",**不含检测时间**;对比为用/不用 DrP 的事件(观察性,存在选择偏差)。论文称 LLM 库集成是 ongoing work。
- 原文:"Overall, the average MTTR improvement over the period of study was 20%." / "Teams that onboarded DrP more comprehensively, with at least 10 analyzers, achieved substantially higher MTTR reductions ranging from 50% to 80%." / "aggregating the mean time difference between resolution and detection timestamps" / "We are also actively looking into integrating LLM based libraries into the DrP SDK as part of ongoing work."
- URL:https://arxiv.org/abs/2512.04250 ;https://engineering.fb.com/2025/12/19/data-infrastructure/drp-metas-root-cause-analysis-platform-at-scale/
- 日期:2025-12
- 来源类型:官方一手 / 预印本(Meta 自评)
- 承重:是(大厂最扎实的生产数据来自非 LLM 自动化;且明确 MTTR 不含 TTD)
- 叙事:B/C

## L19. AWS DevOps Agent GA:"up to 75% lower MTTR、80% faster investigations、94% root cause accuracy"——预览期客户与伙伴自报,无方法学
- 论断:AWS GA 博客(2026-03-31)的三个数字来源为"预览期客户与伙伴报告",均为 "up to"/未给分母、事件集合、评判者;94% 准确率未说明 top-k 或谁判定。博客中的客户案例为单次事故:20–30 分钟 vs"估计" 1–2 小时人工。
- 原文:"In preview, customers and partners using AWS DevOps Agent report up to 75% lower MTTR, 80% faster investigations, and 94% root cause accuracy, enabling 3–5x faster incident resolution." / "The full investigation wrapped in 20–30 minutes, roughly a 75% reduction compared to the 1–2 hours it would have taken manually."
- URL:https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/
- 日期:2026-03-31
- 来源类型:厂商自报(厂商口径;AWS 按 agent-秒计费,受益于"更多自动调查")
- 承重:是(最常被引的"94%")
- 叙事:A(宣称)/ 需验证

## L20. LLM 调查由告警触发:AI SRE 普遍位于"检测之后"
- 论断:AWS DevOps Agent 的客户描述与集成说明显示,调查由 CloudWatch 高严重度告警或 PagerDuty 告警**自动触发**——即检测仍由传统监控/阈值/异常检测完成,LLM 缩短的是之后的定位段(TTD 不变)。Datadog 文档同样以"monitor alert 上的 Bits 分析"为入口。
- 原文:"We've integrated AWS DevOps Agent directly into our incident response process, where it automatically triggers investigations on high-severity CloudWatch alarms" / "PagerDuty: Native integration for automatic incident response triggered by PagerDuty alerts"
- URL:https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/
- 日期:2026-03-31
- 来源类型:官方一手(客户引语经厂商发布)
- 承重:是(TTD vs RCA 区分的直接证据)
- 叙事:C

## L21. Azure SRE Agent GA:"1,300+ agents、35,000+ incidents mitigated、20,000+ 工程小时"——产量指标,无准确率
- 论断:Microsoft 内部使用数据以"部署数/缓解事故数/节省工时"呈现,未给根因准确率、误判率、分母(总事故数)或 TTD/TTM 分段;"mitigated"含义未定义。(另有二手来源称 50,000+ 小时,与 GA 帖不一致,未采用)
- 原文:"Microsoft runs Azure SRE Agent across its own services — 1,300+ agents deployed, 35,000+ incidents mitigated, and over 20,000 engineering hours saved."
- URL:https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-general-availability-for-the-azure-sre-agent/4500682
- 日期:2026-03-10
- 来源类型:厂商自报
- 承重:中
- 叙事:A(规模)/ B(无质量口径)

## L22. Datadog Bits AI SRE:内部"真实事故基准"存在但不公开数字;官方承认早期版本把对的线索总结成错的根因
- 论断:Datadog 称用跨数百团队标注的真实事故构建基准并"显著改进",但正文未给出准确率数字;2026-03 版本口径是"约 2 倍快、3–4 分钟完成调查"(速度,不是准确率)。工程博客坦承一个失败模式:12 次工具调用中有一次找到真根因,但被上游噪声信号带偏,最终输出错误根因。
- 原文:"We worked across hundreds of teams at Datadog to collect and label real incidents and used them to create a benchmark dataset of test scenarios." / "One of the tool calls correctly pinpointed the root cause. But because other tool responses included suspicious signals like critical application errors in an upstream service, the summarization prompt returned an incorrect root cause." / "Bits Investigation can complete investigations about 2 times faster than before—in approximately 3-4 minutes, depending on complexity." / "The result is an agent that's more accurate on internal benchmarks and approximately twice as fast."
- URL:https://www.datadoghq.com/blog/building-bits-ai-sre/ ;https://www.datadoghq.com/blog/bits-ai-sre-deeper-reasoning/
- 日期:2026-01-12;2026-03-05
- 来源类型:厂商(官方工程博客)
- 承重:中
- 叙事:B/C

## L23. Traversal:单一 Fortune 100 客户 "82% RCA accuracy in under 5 minutes",跨客户 "around a 40% reduction in MTTR"
- 论断:厂商口径;82% 来自单一金融客户,未说明分母、top-k、评判者;40% 是 MTTR(混合多段)。Traversal 同时是 OpenRCA 批评者(L12)。
- 原文:"a Fortune 100 financial-services customer saw over 82% RCA accuracy in under 5 minutes, and across enterprise clients, Traversal has driven around a 40% reduction in MTTR."
- URL:https://www.traversal.com/blog/ai-sre-accuracy-and-speed
- 日期:约 2026(页面未标日期)
- 来源类型:厂商自报
- 承重:否
- 叙事:A(宣称)

## L24. Resolve AI × Salesforce:MTTR 降 ~60%,但"调查时间"只降 ~30%——MTTR 改善大于定位改善,说明 MTTR 混入了其他段
- 论断:同一客户页上,"调查时间 ~30% 降低"小于"MTTR ~60% 降低",告警分诊 "~70% 更快"。如果 AI 的作用主要在定位,MTTR 的更大降幅必然来自其他因素(分诊、协调、修复流程或基线变化)——是 MTTR 不能当定位/检测证据的现成例子。首页另称 "5x faster MTTR"、"cutting downtime by up to 80%"。
- 原文:"MTTR reduction ~60% Alert triage ~70% faster Investigation time ~30% reduction" / "~60% reduction in mean time to resolve ( MTTR )" / "Drives reliability with 5x faster MTTR"
- URL:https://resolve.ai/customers/salesforce ;https://resolve.ai/
- 日期:访问于 2026-10-30
- 来源类型:厂商自报
- 承重:中(口径论证)
- 叙事:B/C

## L25. Cleric:58% 告警"无需工程师即关闭"(Cleric 自判),51% 已解决事故采用其修复;并宣称做"发布后变更验证"
- 论断:Cleric 首页三个自有指标均为自评口径:"No action needed" 由 Cleric 自己判定(经 WebFetch 读取到的脚注,未经 curl 复核),工程师评分为可选打分。它把产品定位延伸到发布后检测("检查每个变更……在成为事故前修复回归"),但未给出回归检出率、误报率或检出时间——这是 LLM 进入"检测段"的宣称,无测量。自动关闭告警若误判,即为漏检代价。
- 原文:"58% Alerts Closed Without an Engineer 51% Resolutions That Applied Cleric's Fix 4.08/5 Average Engineer Rating" / "Cleric checks each change in production and fixes any regressions before they become incidents."
- URL:https://cleric.ai/
- 日期:访问于 2026-10-30(统计窗口称 2026 年 5–10 月)
- 来源类型:厂商自报
- 承重:中(唯一明确宣称 LLM 做发布后检测的样本)
- 叙事:A(宣称)/ B(自判口径)

## L26. Grafana:单一内部事故轶事——AI 8 分钟找到根因,比 on-call 早 20 分钟
- 论断:标题"3.5x faster"来自一个事故;且 AI 是在告警触发、人类已开始排查后并行启动。属 n=1 轶事。
- 原文:"Eight minutes later, it found the root cause, 20 minutes before our on-call team came to the same conclusion."
- URL:https://grafana.com/blog/a-tale-of-two-incident-responses-how-our-ai-assist-helped-us-find-the-cause-3-5x-faster/
- 日期:2026-01-29
- 来源类型:厂商(从业者博客)
- 承重:否
- 叙事:A(轶事)

## L27. 厂商自己给买家的评估建议:用 5–10 个已结事故回放——行业评估样本量的现实
- 论断:incident.io 建议买家用 precision/recall 做历史回放,但样本仅 "5-10 closed incidents";说明大多数"客户自测准确率"背后的样本量可能极小。
- 原文:"Run historical incidents with known root causes through the system to measure AI accuracy. Select test incidents: Choose 5-10 closed incidents where you definitively know the root cause."
- URL:https://incident.io/blog/ai-root-cause-analysis-accuracy-testing-guide
- 日期:2026-02-20
- 来源类型:厂商(从业者博客)
- 承重:否
- 叙事:B/C

## L28. Google Gemini Cloud Assist investigations:仍为 Preview,官方文档承认结果不确定、无准确率
- 论断:Google 未公布准确率;文档明言同一调查重跑结果会不同(LLM 概率性 + 云状态变化),且 2026-04 后限 Premium Support 用户。
- 原文:"Investigations are subject to the general limitations of AI technology. Investigation runs are dynamic, which means re-running the same investigation can produce results with small differences." / "the probabilistic nature of output from large-language models such as Gemini"
- URL:https://docs.cloud.google.com/cloud-assist/investigations
- 日期:访问于 2026-10-30
- 来源类型:官方一手
- 承重:否
- 叙事:B/C

## L29. 信任差距:PagerDuty 赞助调研中 59% IT 决策者 vs 37% 开发者预期 AI 让停机/恢复改善 >20%
- 论断:注意这不是"信任"问题本身,而是对改善幅度 >20% 的预期;来源为 PagerDuty 赞助的 The New Stack 文章(利益相关)。
- 原文:"Research indicates that 59% of IT decision-makers expect AI to improve downtime and recovery performance by more than 20%. However, developers appear not to share the same enthusiasm, with only 37% agreeing."
- URL:https://thenewstack.io/fix-developer-burnout-outages/
- 日期:2026-04-21
- 来源类型:媒体转述(厂商赞助内容)
- 承重:否
- 叙事:B

---

## 交叉口径问题(供验证阶段)

1. **top-k 不一致**:Meta 42% = top-5 候选变更命中;AIOpsLab 定位报 Acc@1 与 Acc@3;OpenRCA/ITBench-AA = 全部要素/全部根因命中才计分;AWS 94%、Traversal 82% 未说明 top-k。不可横比。
2. **分母类型**:回放历史事件(Meta、Ahmed、RCACopilot、Roy)vs 故障注入基准(AIOpsLab、ITBench、OpenRCA 2.0)vs 客户自报生产事件(AWS、Traversal、Resolve)vs 厂商自判(Cleric "No action needed")。
3. **"accuracy" 一词偷换**:RCACopilot "accuracy up to 0.766" 实为类别分类 Micro-F1;Ahmed 用 BLEU/人评 1–5 分;Triangle 97% 为分派准确率而非根因。
4. **严格 vs 宽松判定差距巨大**:OpenRCA 2.0 同一批模型 20.7%(精确根因集)vs 76.0%(至少一个正确服务)vs 61.5%(有因果链)。任何宣称都应追问用的是哪档。
5. **MTTR ≠ 定位 ≠ 检测**:DrP 明确 MTTR = 解决 − 检测时间戳(不含 TTD);Resolve/Salesforce MTTR 降幅(60%)大于调查时间降幅(30%);Triangle 的 TTE、Azure 博客的 TTM 各是不同段。没有任何一个厂商/论文给出 LLM 缩短 TTD 的实测。
6. **LLM 是否参与检测**:证据仅有 (a) AIOpsLab 的二元检测题(故障已注入、样本十余题、无误报率);(b) Cleric 的"变更验证"宣称(无数字)。生产中 AWS/Datadog/PagerDuty 的调查均由告警触发。
7. **基准分数的时间线**:OpenRCA 11.34%(Claude 3.5,2024 末)→ ~34.9%(Opus 4.6,2026-02,厂商自报、聚合站转录、"已提交官方验证"但截至访问仍 Unverified);ITBench 13.81%(GPT-4o,2025)→ 47%(Opus 4.7,ITBench-AA,2026-05,评分规则不同)。不同版本/评分规则不可连成趋势线而不加说明。
8. **人类基线缺失**:OpenRCA、ITBench、ITBench-AA、AIOpsLab 均无人类 SRE 基线;"AI 比人快多少"只有厂商轶事(Grafana n=1、AWS 单案"估计 1–2 小时")。
9. **覆盖率(reach)隐藏**:Meta 用置信度过滤低置信答案、ReAct 更多"证据不足"拒答——准确率提升可能以覆盖率下降换取,厂商均不报覆盖率。
10. **利益相关**:Microsoft 自建 AIOpsLab/OpenRCA 并让自家 agent 参评;IBM 自建 ITBench;Anthropic 自报 OpenRCA;Traversal 既批评 OpenRCA 又卖产品;PagerDuty 赞助信任调研。
