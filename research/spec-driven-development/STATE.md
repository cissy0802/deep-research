# 25. Spec-driven development — 运行状态

- **Slug**: spec-driven-development
- **登记日期**: 2026-11-11(ae757bb)
- **时效声明**: 成文标注「截至 2026 年 11 月」
- **运行规模(计划)**: 标准运行:7 条调研线(目标 80–160 源)、约 15–25 组承重论断 × 3 票、单源承重实证双席审计;编排用 Agent 子代理
- **联网约束(写进每个子代理 brief)**: 禁止把用户邮箱或任何个人信息放进 User-Agent、header、URL 或 payload;要求 UA 带联系方式的站点用通用 UA 或跳过。

## 核心问题
把"spec-driven development"叙事拆成三个可分别检验的主张:
1. **先写 spec 提升 agent 产出**(质量/合并率/缺陷/成本)——现在可检验;
2. **spec 保持活性**、不与代码漂移,维护成本可接受——可用返工率/漂移率检验;
3. **spec 成为唯一事实源、代码可再生**(Tessl 路线)——多为预测,只给条件与可观测信号,不给判决。
以及:它与瀑布/MDA/BDD 的历史前科是同构还是真不同(差异在哪个机制上)。

## spec 分型(全程统一口径,证据不得跨型混引)
- T1 需求/PRD 型(自然语言意图、user story、验收标准)
- T2 计划/任务分解型(plan.md、tasks.md、设计文档)
- T3 形式契约型(类型、前后置条件、形式规约、Lean/Dafny)
- T4 可执行规约型(测试、BDD 场景、property)

## 调研线(7 条)
1. **PRO** 正方一手与 LLM 侧机制证据:计划先行(self-planning code generation、CodePlan)、需求澄清(ClarifyGPT 等)、TiCoder 测试驱动意图形式化用户研究、spec/plan 条件下的 agent 基准结果;支持 SDD 的已发表实验。
2. **CON** 反方一手与对照实测:ESEM 2026「Specification Artifacts in OSS PR Workflows Do Not Reduce Defects」(单源承重候选,全文、样本、缺陷口径、混杂);Böckeler(martinfowler.com)Kiro/Spec Kit/Tessl 实操评测原文;Scott Logic、Marmelab 实操;流程税/token 成本的独立测量。
3. **HIST** 历史前科考古:Royce 1970 原文;"瀑布"一词的出处与误读史;Boehm 1981 缺陷修复成本曲线原始数据 + Bossavit 溯源;MDA/UML/可执行 UML/CASE 工具的采用与衰落(调查数据);BDD/Cucumber 采用与弃用;TDD meta 分析(Rafique-Mišić 2013 等)方向;literate programming。
4. **VENDOR** 厂商口径:GitHub Spec Kit(文档、博客、发布说明、star/使用数据)、AWS Kiro(定价、credit、官方案例)、Tessl(spec-as-source 叙事、registry、融资)、BMAD、OpenSpec、Augment/Cursor/Claude Code 的 plan 模式;"specs are the new code"类口号的逐字出处(Sean Grove/OpenAI 等,回一手视频);谁受益。
5. **MEASURE** 独立/半独立测量:Uvik SDD benchmark(50 工单 × 5 臂,原始数据 CC BY 4.0,可复跑;厂商口径)、单人对照实验(DEV 等)、spec 漂移/返工率测量、#14 已核 AGENTbench(arXiv 2602.11988)与 Shepard & Albrecht 的可迁移口径、METR 2025 RCT(#0 已核)、context rot 文献(#14 已核)。
6. **FORMAL** 形式化一端(吸收候选池 #5 钩子):autoformalization 忠实率、形式数学基准题面错位率、"陈述=意图"鸿沟的可测性;Dafny/Lean/Verus 上 LLM 生成规约的正确性研究;规约审阅成本 vs 代码审阅成本(连 #2/#5)。
7. **ADOPT** 采用与实践现场:开发者调查(Stack Overflow、JetBrains、DORA 2025/2026 中关于 spec/plan 工作流的题项)、GitHub 上 spec 目录/文件的普查(可复跑查询,计文件非项目——#14 教训)、企业落地案例的口径(厂商案例 vs 独立报告)。

## 交叉口径预警
- star/下载 ≠ 采用 ≠ 效果
- 合并率 / 缺陷率 / 测试通过率 / token / 墙钟 / 返工率 不得互换
- 单次采样的 agent 运行结果按假精度审计(#14 AGENTbench 教训)
- 已核口径(METR、AGENTbench、context rot、llms.txt 零消费)直接复用,标注来源期号

## 运行日志
- 2026-11-11: 登记 #25(ae757bb),吸收候选池「Autoformalization 的规约层危机」。STATE 落盘,调研线 7 条。
- 2026-11-11: Round 1 通用 brief 落盘(brief.md);并行派 7 个调研子代理(PRO/CON/HIST/VENDOR/MEASURE/FORMAL/ADOPT),产出 lines/<LINE>.{json,md}。

- 2026-11-11: Round 1 七线全部返回:PRO 31 / CON 35 / HIST 34 / VENDOR 34 / MEASURE 35 / FORMAL 34 / ADOPT 35 = 238 论断,153 个独立来源 URL;confidence:verbatim 129 / paraphrase 23 / secondhand 86。
- 2026-11-11: **网络约束**:环境网络策略拦截 arxiv.org、openreview、dl.acm.org、ieeexplore、drops.dagstuhl.de、martinfowler.com、uvik.net、dev.to、kiro.dev、tessl.io、thoughtworks.com、github.blog、youtube.com、web.archive.org 等(CONNECT 403);尝试 update_environment 添加白名单被服务拒绝,需用户在环境设置中放行。一手原文主要经 GitHub 取得(作者仓库/LaTeX 源/复现包/博客源仓库)。ADOPT 现场测量脚本与数据存 adopt-measure/。
- 2026-11-11: groups.py 合并 01-raw-claims.md;抽 32 组(groups/G01–G32),分 4 批(B1 G01–G08 / B2 G09–G16 / B3 G17–G24 / B4 G25–G32)。

- 2026-11-11: 网络已改为不受限(arXiv/Dagstuhl/martinfowler/uvik/kiro 可达;dl.acm.org 站方 403)。Round 2 brief 落盘(brief-r2.md);派 12 个验证子代理(B1–B4 × Q/X/K),判决落 verdicts/<G>-<镜头>.md,共 96 票。

- 2026-11-11: Round 2 十二个验证子代理全部返回,96 票:10 HOLDS / 86 修正 / 0 组级推翻;伪引用 4 处(H27 OMG、V30 Claude Code 文档、V26 Grove 口号、M31 Tessl),子论断推翻约 40 处,禁写清单见 03。Uvik 原始 CSV 存 data/。上游修订(AGENTbench v3、METR 2026-02 更新)影响已发布 #14/#0,已作为独立修正任务提出,不在本期处理。03-verification-round2.md 落盘。
- 2026-11-11: Round 3 brief(brief-r3.md)与 6 个靶子(r3/targets.md)落盘;派 12 个子代理(R1–R6 × X 反证搜索席 / M 方法学审计席)。

- 2026-11-11: Round 3 十二份审计全部返回:R1 Hill B/D、R2 Uvik **D**、R3 Spec Kit Agents C、R4 TiCoder C(标题 D)、R5 活性测量 C、R6 形式基准 **B**;47 项否决;R6 方向获独立证实(两团队逐题 κ=0.74)。主线程回一手补核 SpecFirst(arXiv 2607.27167)。04 与 02(承重论断 + 证据分级)落盘;复算脚本存 r3/scripts/。

- 2026-11-11: 成文 zh deep/plain;en 由 2 个子代理忠实翻译(deep 65 条英文引语逐字校验 1 处仅括号差异;plain 4 处被回译的引语由主线程改回原文;分级标签统一为 house 口径 Single-source verified)。build.py 注册四处,python3 build.py 构建通过,其余页面 build 后还原以保留已烘焙 TTS;手机宽度渲染无横向滚动。TOPICS 归档 #25、候选池 +3(钩子收割,Second Brain 站未在本会话可达,未反哺)。上游修订(AGENTbench v3、METR 2026-02)对 #14/#0 的修正已作为独立任务提出。

## 下一步(已完成)
全部步骤完成并已推送。待办:#14/#0 的上游修订修正(独立任务)。
