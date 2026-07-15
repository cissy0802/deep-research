# Round 1 已验证结论(25 claims → 10 merged findings,全部 3-0 挺过)

> workflow run: wf_71d43d15-568,108 agents,26 sources,124 claims extracted,25 verified/25 confirmed/0 refuted。时间基准 2026-07-15。

## Summary

截至 2026-07,业界已明显向 AGENTS.md 收敛:它由 OpenAI 主导发起、多厂商(Codex、Amp、Google Jules、Cursor、Factory)参与,2025-12 起交由 Linux Foundation 旗下 Agentic AI Foundation 中立托管,官网给出可复跑的 GitHub 检索口径宣称 60k+ 开源项目采用;Cursor 与 GitHub Copilot 已原生消费 AGENTS.md(Copilot 还接受根级 CLAUDE.md/GEMINI.md),互操作靠 symlink 或配置项而非自动识别。各厂商官方最佳实践高度共识:文件要短(Anthropic 明言臃肿的 CLAUDE.md 会导致指令被忽略;Codex 硬性 32 KiB 截断;Cursor 建议单规则 <500 行;GitHub 生成 prompt 限 2 页)、优先放可直接执行的构建/测试命令(带完整 flags)、给出项目结构/架构地图、用 always/ask-first/never 边界规则,monorepo 用分层嵌套文件且"最近文件优先、用户 chat 指令覆盖一切"。GitHub 官方分析了 2500+ 个公开 agents.md,总结出六个核心区域(commands、testing、project structure、code style、git workflow、boundaries)。需要强调:本轮存活的 25 条 claim 全部来自标准/厂商一手文档(调研线 1、2),原问题中的实证对照评测、反模式实测、大型开源库实地考察、llms.txt 体检与企业落地 playbook(线 3-7)没有产出经过验证的 claim,相关结论只能标注为厂商口径而非独立验证。

## Findings

### F1 [high] (vote: 3-0 (merged claims 0, 23, 24))

AGENTS.md 定位为简单、开放、跨工具的 'README for agents':纯 Markdown、无必填字段/schema,官方建议覆盖 project overview、build/test 命令、code style、testing、security 五类内容,并与面向人类的 README 分离;它起源于 OpenAI 主导的跨厂商协作(Codex、Amp、Google Jules、Cursor、Factory),2025-12 起由 Linux Foundation 旗下 Agentic AI Foundation 中立托管,已成为最接近事实标准的格式。

**Evidence**: 官方 spec repo 原文逐字核验:'AGENTS.md is a simple, open format for guiding coding agents... a README for agents'; FAQ: 'AGENTS.md is just standard Markdown. Use any headings you like'; LF 新闻稿确认 AAIF 创始项目含 AGENTS.md(与 MCP、goose 并列)。注意:'cross-vendor' 是官方叙事,独立报道称其实质为 OpenAI 主导后捐赠。

**Sources**:
- https://agents.md/
- https://github.com/agentsmd/agents.md
- https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- https://openai.com/index/agentic-ai-foundation/

### F2 [high] (vote: 3-0 (merged claims 1, 2, 22))

嵌套/monorepo 分层规则是标准核心:官方 FAQ 规定冲突时'离被编辑文件最近的 AGENTS.md 获胜,用户显式 chat 指令覆盖一切';monorepo 建议每个 package 放一份嵌套文件,agent 自动读取最近文件;官网引用 OpenAI 主仓库含 88 个 AGENTS.md 作为嵌套实践例证。

**Evidence**: FAQSection.tsx 逐字:'The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything.' HowToUseSection.tsx:'the main OpenAI repo has 88 AGENTS.md files'。注意:该规则在网站 FAQ 而非正式规范文本中,实际执行取决于各 agent 实现(如 OpenCode 不自动加载嵌套文件);88 数字为 OpenAI 对私有仓库的自报,不可外部审计。

**Sources**:
- https://agents.md/
- https://github.com/agentsmd/agents.md

### F3 [high] (vote: 3-0 (claim 21))

采用量有可核查口径:agents.md 官网宣称 '60k+ 开源项目使用',并链接可复跑的 GitHub code search 查询(path:AGENTS.md NOT is:fork NOT is:archived)。但验证者复跑发现该查询做路径子串匹配(会误计名为 agents.md/ 的目录内文件),且计的是文件数而非项目数——是可审计但偏松的 proxy。

**Evidence**: Hero.tsx 逐字含 'used by over 60k open-source projects' 及查询链接;验证者通过 GitHub code-search API 复跑确认查询可执行但存在计数口径瑕疵。承重数字应表述为'官网宣称、查询可复跑、口径偏松'。

**Sources**:
- https://agents.md/
- https://github.com/agentsmd/agents.md

### F4 [high] (vote: 3-0 (merged claims 3, 13, 15-part, 16-part))

跨工具互操作现状:官方迁移路径是重命名+symlink(mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md),Aider/Gemini CLI 靠配置项兼容;Codex 默认只认 AGENTS.override.md 和 AGENTS.md,CLAUDE.md 等其他文件名需用户级 project_doc_fallback_filenames 配置才生效(不随 repo 走);反向地,GitHub Copilot 官方接受根级 CLAUDE.md 或 GEMINI.md 作为 agent instructions 替代文件,Cursor 原生支持 AGENTS.md(含嵌套)——收敛趋势明确但互认不对称,symlink 仍是最可靠的多工具方案。

**Evidence**: FAQ 逐字含 symlink 命令与 .aider.conf.yml 'read: AGENTS.md'、.gemini/settings.json fileName 配置;Codex 源码 candidate_filenames() 证实默认仅两个文件名、fallback 默认为空数组;GitHub docs 逐字:'Alternatively, you can use a single CLAUDE.md or GEMINI.md file stored in the root'。

**Sources**:
- https://github.com/agentsmd/agents.md
- https://developers.openai.com/codex/guides/agents-md
- https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- https://cursor.com/docs/rules
- https://github.com/openai/codex (codex-rs/core/src/agents_md.rs)

### F5 [high] (vote: 3-0 (merged claims 4, 5, 6))

GitHub 官方分析 2500+ 公开 agents.md 文件后总结的最佳实践:成功文件给 agent 具体职责/persona、可直接执行的命令(带完整 flags/options、放在文件靠前章节)、明确边界与好输出示例;建议覆盖六个核心区域(commands、testing、project structure、code style、git workflow、boundaries),边界用 always do / ask first / never do 三档规则防止破坏性错误。这是目前样本量最大的公开模式分析,但属厂商叙事——未公布方法学或数据集,且文章语境部分围绕 Copilot custom agents 而非纯根级 AGENTS.md。

**Evidence**: 文章(2025-11-19 发布,11-25 更新,作者 Matt Nigh)逐字核验:'cover the six core areas: Commands, testing, project structure, code style, git workflow, and boundaries'; 'Put relevant executable commands in an early section with flags and options, not just tool names'; GitHub 官方 X 账号发帖确认 'We analyzed 2500+ agents.md files'。证据等级:厂商模式分析,非受控评测。

**Sources**:
- https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
- https://x.com/github/status/2003502651422449901

### F6 [high] (vote: 3-0 (merged claims 7, 8, 9, 10))

Anthropic 的 CLAUDE.md 官方最佳实践:(a) 必须精简——每行自问'删掉会不会导致 Claude 出错',并明确断言'臃肿的 CLAUDE.md 会导致 Claude 忽略你的真正指令'(厂商自己反对'多写上下文'路线);(b) 该写:Claude 猜不到的 bash 命令、非默认 code style、测试指令、repo etiquette、项目特有架构决策;不该写:能从代码推断的内容、详细 API 文档、频繁变化的信息,偶发领域知识放按需加载的 skills;(c) 分层加载:home 目录、项目根、CLAUDE.local.md、父目录(monorepo 自动加载)、子目录(按需拉取);(d) /init 自动分析代码库生成初稿,CLAUDE.md 应'像代码一样对待'——进 git、定期修剪、通过观察行为变化来测试,可用 IMPORTANT/YOU MUST 等强调词调节遵从度。

**Evidence**: 2026-07-15 实时抓取逐字核验全部要点,含 'Bloated CLAUDE.md files cause Claude to ignore your actual instructions!' 与 'The over-specified CLAUDE.md... Claude ignores half of it'。注意:强调词提升遵从度是厂商建议,无引用实证数据。

**Sources**:
- https://code.claude.com/docs/en/best-practices

### F7 [high] (vote: 3-0 (merged claims 11, 12, 14; claim 14 verifier confidence medium))

OpenAI Codex 的 AGENTS.md 机制(文档+源码双重核验):按 ~/.codex 全局 → repo 根到 cwd 逐目录发现,root-to-leaf 拼接,更深文件在冲突时优先;所有文件合计硬性默认上限 32 KiB(project_doc_max_bytes),超出静默截断(有真实 issue #7138/#13386 佐证),官方补救是拆分到嵌套目录或调高配置;内容建议是简短具体的 working agreements(构建/测试命令、依赖策略),沟通风格偏好放全局文件、团队/代码库规则放 repo 文件。

**Evidence**: 源码逐字:DEFAULT_PROJECT_DOC_MAX_BYTES = 32 * 1024;agents_md.rs 模块注释确认 root-to-cwd 拼接与 AGENTS.override.md;shipped system prompt:'More-deeply-nested AGENTS.md files take precedence'。内容建议部分(claim 14)因官方页面被代理 403,靠精确短语搜索+多家独立转载核验,措辞建议对照 live URL 复核——该子项 medium。

**Sources**:
- https://developers.openai.com/codex/guides/agents-md
- https://github.com/openai/codex (codex-rs/core/src/agents_md.rs, config_toml.rs, config.schema.json)

### F8 [high] (vote: 3-0 (merged claims 15, 16, 17))

GitHub Copilot 官方支持三类 repo custom instructions:repo 级 .github/copilot-instructions.md、路径级 .github/instructions/NAME.instructions.md、以及 AGENTS.md(可多份嵌套、最近文件优先,docs 直接链接 agentsmd/agents.md 作为标准出处);官方自动生成 copilot-instructions.md 的 prompt 要求:不超过 2 页、每条 build/test/lint 命令须实际运行验证、包含项目结构/架构地图,并显式让 agent '信任 instructions、仅在不完整或有误时才重新搜索 repo'。

**Evidence**: 从 github/docs 源码(main 分支,2026-07-15)逐字核验,含 'Instructions must be no longer than 2 pages'、'Each command should be validated by running it'、trust-instructions 指令。注意:github.com 上路径级 instructions 目前仅支持 Copilot coding agent 与 code review;VS Code 中非根目录 AGENTS.md 默认关闭需设置开启。

**Sources**:
- https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot

### F9 [high] (vote: 3-0 (merged claims 18, 19, 20))

Cursor 官方规则最佳实践:单条规则 <500 行、大规则拆成可组合的多条、给具体示例或引用文件、避免模糊表述('像写清晰的内部文档');原生支持 AGENTS.md(根目录+子目录嵌套,与父目录合并、更具体者优先);legacy .cursorrules 仍可用但官方宣布将弃用并建议迁移到 Project Rules 或 AGENTS.md;Cursor 2.2 起新规则采用文件夹形式(.cursor/rules/<name>/RULE.md),.mdc 单文件保持可用。

**Evidence**: 官方 docs 逐字核验(直接抓取被 403,经 raw MDX/多个逐字镜像/搜索索引交叉确认):'Keep rules under 500 lines... Write rules like clear internal docs'; 'Instructions from nested AGENTS.md files are combined with parent directories, with more specific instructions taking precedence'。注意:社区 bug 报告显示 RULE.md 文件夹格式在部分版本中实现落后于文档;docs 自述 AGENTS.md 适合 'straightforward use cases'(缺 glob/always-apply 元数据)。

**Sources**:
- https://cursor.com/docs/rules

### F10 [high] (vote: synthesized from claims 5-7, 9, 12, 14, 17, 18 (all 3-0))

跨厂商共识(综合性发现):四家主要厂商(Anthropic、OpenAI、GitHub、Cursor)的官方指南在三点上完全一致——(1) 短:Anthropic 警告臃肿导致指令被忽略、Codex 32 KiB 硬截断、GitHub 限 2 页、Cursor 限 500 行;(2) 可执行命令优先:带完整 flags 的 build/test/lint 命令是所有指南的第一优先内容;(3) 分层嵌套+最近文件优先:monorepo 场景四家均支持 per-folder 文件且语义一致(nearest wins,用户指令覆盖)。主要分歧在机制层:Cursor 的 rules 有 glob/always-apply 元数据而 AGENTS.md 无 schema;Copilot 区分三类文件而其他厂商单文件分层;Codex 靠字节上限强制精简而其他靠建议。

**Evidence**: 由上述各厂商一手文档独立核验后的横向综合;共识三要素在每家文档中均有逐字出处。注意这是解释性综合(interpretive synthesis),各单项均 3-0 通过,但'共识'本身是本报告的归纳而非任何单一来源的断言;且共识全部为厂商口径,无独立对照实验证明这些做法提升 agent 表现。

**Sources**:
- https://code.claude.com/docs/en/best-practices
- https://developers.openai.com/codex/guides/agents-md
- https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- https://cursor.com/docs/rules
- https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

## Caveats(覆盖缺口声明)

重大覆盖缺口:25 条存活 claim 全部落在调研线 1(标准之争)和线 2(厂商最佳实践),原问题的线 3(带/不带 context 文件的对照评测、compliance 研究、context rot 文献)、线 4(React/Kubernetes/LLVM 等大型开源库实地考察)、线 5(反模式:文档腐烂实测、prompt injection 安全通告)、线 6(CI 校验/repomix 等工具边界)、线 7(企业落地 playbook)以及 llms.txt 体检(含 Google 表态)均无经过验证的 claim 存活——报告中所有'该怎么写'的结论证据等级均为【厂商官方口径】,'写了确实更好'的实证层面本轮无法背书。承重数字口径问题:60k+ 采用量的官方查询做路径子串匹配且计文件非项目;OpenAI repo 88 个 AGENTS.md 为对私有仓库的自报;GitHub 2500+ 文件分析未公布方法学,且语境部分是 Copilot custom agents 而非纯根级 AGENTS.md。访问限制:developers.openai.com、github.blog、cursor.com、agents.md 在验证环境中被代理 403,相关引文靠精确短语搜索索引、官方 GitHub 源码仓库和多家逐字镜像交叉核验(claim 14 因此仅 medium);建议对承重引文做一次 live URL 复核。时效性:该领域变化极快(AAIF 托管 2025-12 才成立,Cursor 2.2 格式变更为近期),所有结论以 2026-07-15 为基准,文档路径与默认行为可能已变;Cursor 存在已记录的 docs-vs-实现落差(RULE.md 文件夹格式)。'厂商收敛于 AGENTS.md' 的叙事部分来自 OpenAI 主导生态的自我表述,Anthropic 的 CLAUDE.md 仍是独立体系(本轮未发现 Anthropic 官方消费 AGENTS.md 的证据)。

## Open questions(线 3-7 缺口)

- 实证缺口:是否存在带/不带 AGENTS.md/CLAUDE.md 的受控对照评测(如 SWE-bench 变体)量化 context 文件对 agent 成功率的提升?agent 对文件内指令的实际遵从率(compliance rate)有无系统测量?厂商'臃肿导致忽略指令'的断言有无独立复现?
- llms.txt 的真实消费方现状:Google 公开表态不消费它之后,2026 年年中有哪些主流 crawler/agent 实际读取 llms.txt?其采用叙事与实际消费的差距如何量化?
- 安全面:第三方仓库中的 AGENTS.md/instructions 文件作为 prompt injection 攻击面,有无 CVE、厂商安全通告或学术研究?各 agent 对不可信 repo 的 instructions 文件采取了什么隔离措施?
- 大型开源项目实地数据:React、Kubernetes、LLVM、Rust 等头部仓库 2026 年年中实际采用哪种方案(根级 vs 分层、手写 vs /init 自动生成)、更新频率如何、有无 CI 校验文档与代码同步的实践?

## Source registry

- [primary] https://github.com/agentsmd/agents.md (angle: 标准规范与采用现状(一手规范原文), claims: 5)
- [primary] https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/ (angle: 标准规范与采用现状(一手规范原文), claims: 5)
- [secondary] https://www.infoq.com/news/2025/08/agents-md/ (angle: 标准规范与采用现状(一手规范原文), claims: 5)
- [secondary] https://www.seroundtable.com/google-ai-llms-txt-39607.html (angle: 标准规范与采用现状(一手规范原文), claims: 4)
- [unreliable] https://www.morphllm.com/agents-md-guide (angle: 标准规范与采用现状(一手规范原文), claims: 0)
- [blog] https://medium.com/@kaispriestersbach/the-llms-txt-is-dead-more-precisely-a-dud-ab7bee4f469c (angle: 标准规范与采用现状(一手规范原文), claims: 5)
- [primary] https://code.claude.com/docs/en/best-practices (angle: 厂商官方最佳实践文档, claims: 5)
- [primary] https://developers.openai.com/codex/guides/agents-md (angle: 厂商官方最佳实践文档, claims: 5)
- [primary] https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot (angle: 厂商官方最佳实践文档, claims: 5)
- [primary] https://cursor.com/docs/rules (angle: 厂商官方最佳实践文档, claims: 5)
- [primary] https://agents.md/ (angle: 厂商官方最佳实践文档, claims: 5)
- [primary] https://code.visualstudio.com/docs/agent-customization/custom-instructions (angle: 厂商官方最佳实践文档, claims: 5)
- [primary] https://arxiv.org/html/2602.11988v1 (angle: 实证评测与遵从率研究(学术/基准), claims: 5)
- [primary] https://arxiv.org/abs/2605.10039 (angle: 实证评测与遵从率研究(学术/基准), claims: 5)
- [primary] https://arxiv.org/html/2511.12884v1 (angle: 实证评测与遵从率研究(学术/基准), claims: 5)
- [primary] https://arxiv.org/html/2601.20404v1 (angle: 实证评测与遵从率研究(学术/基准), claims: 5)
- [primary] https://research.trychroma.com/context-rot (angle: 实证评测与遵从率研究(学术/基准), claims: 5)
- [secondary] https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/ (angle: 怀疑与安全视角(反模式、注入攻击、llms.txt 质疑), claims: 5)
- [secondary] https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/ (angle: 怀疑与安全视角(反模式、注入攻击、llms.txt 质疑), claims: 5)
- [primary] https://arxiv.org/html/2601.17548v1 (angle: 怀疑与安全视角(反模式、注入攻击、llms.txt 质疑), claims: 5)
- [primary] https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/ (angle: 怀疑与安全视角(反模式、注入攻击、llms.txt 质疑), claims: 5)
- [blog] https://prompt.security/blog/when-your-repo-starts-talking-agents-md-and-agent-goal-hijack-in-vs-code-chat (angle: 怀疑与安全视角(反模式、注入攻击、llms.txt 质疑), claims: 5)
- [primary] https://code.claude.com/docs/en/large-codebases (angle: 实践者落地:开源 repo 实例与维护工具链, claims: 5)
- [blog] https://securityboulevard.com/2026/06/6-agents-md-examples-from-real-production-repos/ (angle: 实践者落地:开源 repo 实例与维护工具链, claims: 5)
- [blog] https://dev.to/datadog-frontend-dev/steering-ai-agents-in-monorepos-with-agentsmd-13g0 (angle: 实践者落地:开源 repo 实例与维护工具链, claims: 5)
- [blog] https://dev.to/wolfejam/your-agentsmd-is-already-stale-and-your-agent-trusts-it-completely-2nfh (angle: 实践者落地:开源 repo 实例与维护工具链, claims: 5)
