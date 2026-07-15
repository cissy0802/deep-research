# 给 Agent 看的 README:上下文文件是基建还是货物崇拜?(深入版)

> 本文的实证引用经过分级:两轮对抗验证共 35 组承重论断,每组经 3 名独立验证者反驳式核查(逐字核对一手原文、复算数字口径、检索反证),105 票中 0 组被推翻,并按验证者意见完成 30 余处口径修正——包括揪出一条流传中的伪引用(官方文档并不存在"CLAUDE.md 控制在一万词以内"的说法,真实口径是另一个页面上的"200 行以内")。厂商口径与独立实证在正文中分开标注;未进入验证流程的引用标【未验证,来源】。文末附来源索引。

## 0. 一句听起来显然正确的话,和三个不配合的事实

2025 到 2026 年,几乎每一家 coding agent 厂商都在告诉你同一件事:给你的代码库写一个"给 agent 看的 README"——AGENTS.md、CLAUDE.md、`.cursor/rules`、`copilot-instructions.md`,名字不同,道理相同:agent 每次进入你的仓库都要从零探索,把构建命令、目录地图、团队规矩预先写好,它就能少走弯路。这个道理听起来显然正确,以至于"你的 repo 还没有 AGENTS.md?"已经成了一种新的技术羞辱。

但对抗验证挖出了三个不配合的事实:

**第一,目前唯一的多 agent 对照评测发现:上下文文件总体上并不提升任务成功率,反而平均多花 20% 以上的推理成本。**ETH Zurich 与 LogicStar.ai 的研究者在 438 个真实任务上跑了三个 agent(Claude Code、Codex、Qwen Code),原文结论是"context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%"。【已验证】

**第二,"文件要短、重要指令放开头"这类怎么写的民间智慧,第一次接受随机对照检验就全体翻车。**1,650 次 Claude Code 会话的因子实验里,文件大小、指令位置、单文件还是嵌套、相邻文件有没有矛盾——四个结构变量对 agent 遵从率全部没有可检测的效应。【已验证】

**第三,同类叙事里声量最大的 llms.txt,实测消费为零的比例是 97%。**Ahrefs 对 13.7 万个域名的服务器日志分析发现,发布了 llms.txt 的站点里 97% 在 2026 年 5 月一个请求都没收到。【已验证】

这三个事实不意味着"上下文文件没用"——后文会给出它真正有用的地方(效率,而非能力),以及生产环境里经得起逐字核验的写法。但它们意味着:这个领域的最佳实践几乎全部是厂商口径,独立实证刚刚起步,而且起步的几篇结果与厂商叙事并不完全同向。本站[《当代码变得便宜》](https://cissy0802.github.io/deep-research/ai-native-deep.html)的老话在这里同样适用:凡是没有对照组的数字,先问口径再引用。

## 1. 读数说明:三档证据,四条限定

正文给每条承重结论标注证据等级:

- **【厂商口径】**:Anthropic/OpenAI/GitHub/Cursor 的官方文档与官方博客。这一档的价值是"厂商自己怎么说"——它定义了工具的真实行为(加载机制、截断上限),但它对"效果"的断言(比如"臃肿的文件导致指令被忽略")均未附带对照实验。
- **【独立实证】**:2025-11 至 2026-05 之间出现的第一批对照研究。全部是 preprint、尚无同行评审,样本范围窄(Python 为主、单一 agent 或单一厂商生态),读数时限定条件与数字同等重要。
- **【现场证据】**:生产 repo 里真实的上下文文件,本文引用的每一句都对着 GitHub 上的原文件逐字核验过。

四条通用限定:(1) 本领域变化极快,所有结论以 2026-07-15 为基准;(2) 对照研究互相之间不可直接换算——各自的任务集、agent、度量都不同;(3) 两个厂商利益声明:Chroma(context rot 报告作者)是向量数据库公司,"精简上下文优于长上下文"与其产品叙事同向;AGENTbench 论文的共同作者来自商业 agent 评测公司 LogicStar.ai;(4) 本文说的"上下文文件"指 repo 内给 coding agent 的指令文件,llms.txt(面向网站/爬虫)单独一章处理,两者常被混为一谈。

## 2. 标准之争:AGENTS.md 事实胜出,但互认是不对称的

**规范本体简单到几乎没有内容:纯 Markdown、无必填字段、无 schema,官方定位是"README for agents"。**它由 OpenAI 主导发起、多家参与(Codex、Amp、Google Jules、Cursor、Factory),2025 年 12 月起交给 Linux Foundation 旗下新成立的 Agentic AI Foundation 中立托管,与 MCP、goose 并列为创始项目。【已验证】"跨厂商"是官方叙事,独立报道的版本是"OpenAI 主导后捐赠"——两种说法都对,取决于你问的是章程还是提交记录。

**采用量有一个可复跑但偏松的口径。**官网宣称"60k+ 开源项目使用",并附上可以自己点开复跑的 GitHub 检索式;验证者复跑后确认查询可执行,但发现两处水分:该查询做路径子串匹配(名为 `agents.md/` 的目录内文件也会被计入),且计的是文件数而非项目数。作为对照,2025 年 8 月 InfoQ 报道时的口径是 2 万仓库。【已验证】增长趋势是真的,精确数字当传播口径读。

**嵌套规则是这个标准最有内容的部分:离被编辑文件最近的 AGENTS.md 获胜,用户在对话里的显式指令覆盖一切。**monorepo 建议每个 package 放一份,官网引用"OpenAI 主仓库有 88 个 AGENTS.md"作为例证(私有仓库自报数字,不可外部审计)。注意这条优先级规则写在官网 FAQ 里而非正式规范文本中,实际行为取决于各家实现——并非所有工具都自动加载嵌套文件。【已验证】

**互认现状是不对称的,symlink 仍是最可靠的兼容方案。**逐家核验(文档+源码):

- **GitHub Copilot / VS Code**:原生消费 AGENTS.md(可多份嵌套、最近文件优先),文档直接链接 agents.md 作为标准出处;还接受根级 CLAUDE.md 或 GEMINI.md 作为替代。VS Code 从 v1.104(2025 年 9 月)起默认开启,由 `chat.useAgentsMdFile` 控制。【已验证】
- **Cursor**:原生支持 AGENTS.md(含子目录嵌套、更具体者优先);legacy `.cursorrules` 官方宣布将弃用。【已验证】
- **OpenAI Codex**:源码证实默认只认 `AGENTS.override.md` 和 `AGENTS.md` 两个文件名;要让它读 CLAUDE.md 需要用户级配置 `project_doc_fallback_filenames`——这个配置不随 repo 走,意味着你不能替你的用户配好。【已验证】
- **Claude Code**:体系独立,读 CLAUDE.md 及其分层;本轮未发现 Anthropic 官方消费 AGENTS.md 的证据。【已验证】

官方推荐的迁移法就是重命名加软链:`mv CLAUDE.md AGENTS.md && ln -s AGENTS.md CLAUDE.md`;Aider、Gemini CLI 靠各自配置项兼容。【已验证】收敛趋势明确,但"一个文件走天下"要靠文件系统技巧,不靠标准互认。

## 3. 厂商指南对账:共识三条,全部没有对照组

把 Anthropic、OpenAI、GitHub、Cursor 四家的官方最佳实践并排放,共识惊人地整齐——整齐到值得警惕,因为四家没有一家给出对照实验。

**共识一:短。**四家的表述和执法力度不同:Anthropic 最激烈,官方文档原句"Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"(臃肿的 CLAUDE.md 会导致 Claude 忽略你的真正指令),并建议对每一行自问"删掉会不会导致出错";官方尺寸口径在 memory 页:"target under 200 lines per CLAUDE.md file"——网上流传的"一万词以内"在官方文档中并不存在。OpenAI Codex 用机制执法:所有项目文档合计默认上限 32 KiB(源码常量 `DEFAULT_PROJECT_DOC_MAX_BYTES = 32 * 1024`),超出部分静默截断,有真实 issue 佐证踩坑。GitHub 的自动生成 prompt 硬性要求"不超过 2 页"。Cursor 建议单条规则 500 行以内。【已验证】

**共识二:可执行命令优先。**GitHub 官方分析了公开仓库中 2,500 多个 agents.md 文件,总结出六个核心区域——commands、testing、project structure、code style、git workflow、boundaries——并强调把带完整 flags 的可执行命令放在文件靠前章节,而不是只写工具名;边界规则用 always do / ask first / never do 三档表述。注意这是目前样本量最大的模式分析,但 GitHub 未公布方法学与数据集,且文章语境部分围绕 Copilot custom agents,证据等级是厂商模式归纳而非受控评测。GitHub 自动生成 copilot-instructions 的官方 prompt 另有一条好要求:每条 build/test/lint 命令都必须实际运行验证过才能写进去。【已验证】

**共识三:monorepo 分层嵌套、最近文件优先。**四家语义一致(见上章),Anthropic 的版本是:启动时加载工作目录及所有父目录的 CLAUDE.md,子目录文件在读到该目录代码时按需加载;大仓库推荐"根文件放全局约定 + 子目录文件放局部约定"的两层结构,并明确警告单个根文件"要么膨胀到覆盖每个子系统、浪费上下文,要么泛泛而谈、毫无用处"。【已验证】

分歧在机制层:Cursor 的 rules 带 glob/always-apply 元数据而 AGENTS.md 无 schema;Copilot 区分三类文件(repo 级、路径级、AGENTS.md);Codex 用字节上限强制精简而其他家靠劝;Anthropic 独有一条出口——规模大了之后把约定从"每次都加载的 CLAUDE.md"迁去按需加载的 skills/plugins,官方自己承认分层文件"约定会漂移、文件会过期、没人认领根文件"。【已验证】

Anthropic 的内容取舍清单值得单独记录(它回答"写什么"而不只是"写多短"):该写的是 agent 猜不到的东西——bash 命令、非默认代码风格、测试指令、repo 礼仪、项目特有架构决策;不该写的是能从代码推断的内容、详细 API 文档、频繁变化的信息。可以用 IMPORTANT/YOU MUST 等强调词调节遵从度——这条同样没有引用任何实证数据。【已验证,厂商口径】

## 4. 实证体检 I:写了究竟有没有用?——能力没涨,效率真涨

2026 年上半年出现了两篇正面回答"写了有没有用"的对照研究,结论拼在一起相当有信息量:**上下文文件不能让 agent 做成原本做不成的任务,但能让它更快更省地做成原本就能做成的任务。**

**成功率侧:AGENTbench 对照(arXiv 2602.11988,ETH Zurich + LogicStar.ai,2026-02)。**研究者组合了两个基准:SWE-bench Lite(300 个任务、11 个知名 Python repo,配 LLM 生成的上下文文件)和自建的 AGENTbench(138 个真实 PR 任务、12 个小众 Python repo,全部带开发者手写的上下文文件,从 5,694 个 PR 中筛出;注意与 2023 年清华的同名基准无关)。三个 agent、四种模型配置(Claude Code + Sonnet 4.5、Codex + GPT-5.2/GPT-5.1-mini、Qwen Code + Qwen3-30B)。结果:

- LLM 生成的上下文文件**普遍降低**解决率:SWE-bench Lite 平均 -0.5 个百分点,AGENTbench 平均 -2 个百分点(个别配置最差 -3),同时把成本推高 20-23%。【已验证】
- 开发者手写的文件也只有边际收益:平均 +4%,且**对除 Claude Code 之外的所有 agent 成立**——Claude Code 上连这 4% 都没有;代价是平均多走 3.34 步、成本最多 +19%。【已验证】
- 最有解释力的是消融实验:把 repo 的 README 和文档全部删掉之后,LLM 生成的上下文文件反而变成正收益(+2.7%),甚至超过开发者手写的。作者的解读是:上下文文件的价值来自**不冗余的信息**——当它只是复述 README 时是纯负担,当它是唯一文档时才是地图。【已验证】

限定条件:全 Python、preprint 未同行评审、AGENTbench 是作者自建基准、共同作者有商业评测公司背景。但方向性结论("别指望成功率跳涨"、"别让 LLM 在有文档的仓库上批量生成上下文文件")在两个基准、多个模型上一致。

**效率侧:Codex 配对实验(arXiv 2601.20404,Lulla 等,JAWs@ICSE 2026)。**10 个仓库、124 个真实 PR 任务,每个任务跑两遍(带/不带 AGENTS.md):带文件时中位完成时间从 98.57 秒降到 70.34 秒(**-28.64%**),中位输出 token 从 2,925 降到 2,440(**-16.58%**),任务完成行为不变。机制假设:agent 不用靠探索式导航自己摸清项目结构了。二次分析显示均值口径的节省(约 -20%)集中在少数原本会"来回打转"的高成本运行上——上下文文件更像防最坏情况的护栏,而非均匀加速器。【已验证】限定:单 agent(gpt-5.2-codex)、小 PR(<100 行、≤5 文件)、仅根级单文件、作者用词是"关联"而非因果。

把两篇拼起来读:**上下文文件的已证实收益是省时间省 token,不是提升能力上限。**这恰好也解释了为什么厂商都在推——对按 token 计费的服务方和等结果的用户,-28% 时间与 -17% token 已经值回票价,不需要能力神话。

## 5. 实证体检 II:"怎么写"的民间智慧,第一次对照检验就没过

关于"文件该怎么写",厂商与社区有一整套folk wisdom:要短、重要的放开头、别拆太多文件、别有矛盾指令。2026 年 5 月的一项因子实验(arXiv 2605.10039,Damon McMillan,单作者 preprint)第一次把这些变量摆上手术台:1,650 次 Claude Code CLI 会话、16,050 个函数级观测、两个 TypeScript 代码库、五种任务,主力模型 Sonnet 4.6,测量 agent 对一条简单标注指令的遵从率。

结果让两边都不舒服:

- **四个结构变量——文件大小(25/100/250/500 行)、指令在文件中的位置(五档)、单文件 vs 多文件嵌套、相邻文件矛盾——没有一个在多重检验校正后有可检测效应,三个两两交互也没有。**其中"大小"和"矛盾"两个零结果有贝叶斯因子加持(BF10 0.05-0.10,即"确证无效应"而非"没测出来");位置和架构只是未能拒绝。【已验证】
- 真正预测遵从率的是**任务类型**,以及一个探索性发现:**会话内衰减**——agent 每多生成一个函数,遵从该指令的几率约降 5.6%(OR=0.944,非单调,在第二个代码库和 Opus 4.6 上复现)。指令"在会话里的位置"比"在文件里的位置"重要。【已验证】

限定同样苛刻:单一 agent 生态、单一因变量(一条简单标注指令的遵从)、25-500 行的测试区间、单作者未同行评审。但它与厂商叙事的张力值得直说:**Anthropic 说"臃肿导致指令被忽略",而目前唯一的受控检验在 25-500 行区间内找不到大小效应。**

那"短"的建议就作废了吗?不。支持"短"的证据链要换一条:**上下文预算与 context rot。**Chroma 的技术报告(2025-07,自发布、非同行评审,厂商利益已声明)测了 18 个模型,核心发现是模型并不均匀地使用上下文:输入越长,即便简单任务表现也非均匀退化;在 LongMemEval 子集(306 条清洗后的提示)上,只给相关摘录(约 300 token)的"聚焦"条件一致优于把同样信息埋进平均约 11.3 万 token 全量历史的条件;加入主题相关但无关的干扰内容,退化随长度放大。【已验证】

诚实的综合读法:**"短"的可靠论证是成本与上下文预算(每一行都在挤占任务本身的工作记忆,且长上下文有实测退化),而不是"短了 agent 就更听话"(未获证实)。**结构怎么排,目前证据说影响不大;写了什么、以及会话进行到哪,才是遵从率的主变量。

## 6. 内容普查与现场证据:大家实际写什么,漏了什么

**普查:第一份大规模实证(arXiv 2511.12884,"Agent READMEs",2025-11)分析了 1,925 个仓库的 2,303 个上下文文件**(限 CLAUDE.md、AGENTS.md、copilot-instructions.md 三种;Cursor/Windsurf 规则不在内;"第一份"是作者自述,同期另有 AIware 2025 的两篇相邻工作)。16 类指令的分布:实现细节 69.9%、架构 67.7%、构建/运行命令 62.3%——与厂商共识的"命令+地图"高度吻合;**缺口在非功能项:安全指引和性能指引各只出现在 14.5% 的文件里。**维护形态上,这些文件"不是静态文档,而是像配置代码一样演化的复杂工件,靠高频小步添加维护"。【已验证】

**现场:四个生产 repo 的文件,逐字核验过(2026-07-15 对着 GitHub 原文件):**

- **Sentry**(getsentry/sentry,AGENTS.md 第 3 行):"AGENTS.md files are the source of truth for AI agent instructions... Do not add to CLAUDE.md or Cursor rules."——用单一事实源终结多文件漂移,是标准收敛的最干净现场样本。【已验证】
- **Cloudflare**(workers-sdk):Development Commands 的 Package Management 第一条就是"Use `pnpm` - never use npm or yarn",并列出六个子包各自的嵌套 AGENTS.md——把爆炸半径最大的规则放最前 + 分层,两条厂商建议的现场版。【已验证】
- **Apache Airflow**:"Write **Dag** (title case) in all prose"(团队命名法,agent 从代码里猜不出来)和"Never run pytest, python, or airflow commands directly on the host — always use `breeze`"。【已验证】
- **coder/coder**:"Rule #1: If you want exception to ANY rule, YOU MUST STOP and get explicit permission first",以及禁止谄媚措辞:"NEVER write the phrase 'You're absolutely right!'"。【已验证】

四个文件的共性印证了 GitHub 那份 2,500 文件分析的归纳:高信号文件是**命令优先、禁令具体、写 agent 猜不到的东西**。Datadog 前端团队另有一个 monorepo 模式——根文件只当路由器,写工作区地图、工具链、路由规则和默认安全约束,把细节留给高价值/高风险子目录的嵌套文件,并用"每类任务 1-2 条测试提示词、跨多个 agent 跑到能一把过"的方式迭代文件——方法论上是清醒的,但属实践者自述【未验证,来源:dev.to Datadog 工程博客】。

## 7. llms.txt:一个已经可以盖棺的反面教材

llms.txt 常与 AGENTS.md 并列出现在"agent 时代文档基建"清单里,但两者的实测消费天差地别,它值得单独一章,因为它演示了**采用叙事与实际消费可以完全脱钩**:

- **采用侧确实在涨**:Originality.ai 对 300 万+网站的追踪显示,llms.txt 部署量 12 个月涨了 8.8 倍(2025-06 的 4,088 → 2026-05 的 36,120;算上 llms-full.txt/ai.txt 共 38,980)。【已验证】
- **消费侧约等于零**:Ahrefs 对自家 137,210 个域名的服务器日志分析(2026-06 发布):有有效 llms.txt 的约 3.8 万个域名中,**97% 在 2026 年 5 月零请求**;有请求的那些,96% 的流量来自 bot 且多数与 AI 无关(SEO 审计工具 21.7%、身份不明 bot 14.9%、常规爬虫 13.1%),AI 检索类 bot 只占 1.1%。【已验证】(注意两组数字来自两家的独立研究,媒体转述常把它们并成一家——本文验证者也差点被带偏。)
- **消费方的官方表态一致地冷**:Google 的 John Mueller 在 2025-06-17 的 Bluesky 原帖写"FWIW no AI system currently uses llms.txt",更早在 Reddit 把它类比为已死的 keywords meta 标签;Gary Illyes 在 2025-07 的官方活动上确认 Google 不支持也不计划支持。讽刺的是 Google 自家的 Chrome Lighthouse 13.3(2026-05)新增的 agentic browsing 审计却检查 llms.txt 是否存在——同一家公司两个产品口径打架,被 SEO 媒体当场抓包。【已验证】

教训不是"llms.txt 骗人",而是一条可以带走的方法:**写任何"给机器看的文档"之前,先核实哪个机器真的会读它。**AGENTS.md 过了这条检验(VS Code 默认加载、Cursor/Codex 原生消费、Copilot 官方支持——都有文档和源码可查);llms.txt 没过。

## 8. 安全面:你的 README 现在是攻击面

上下文文件被 agent 当作**可信指令**而非普通数据消费——这个信任模型在 2026 年已经有了带 PoC 的攻击面证据:

**供应链写入路径(NVIDIA AI Red Team)。**一个恶意 Golang 构建依赖检测 `CODEX_PROXY_CERT` 环境变量识别出 Codex 环境后,写入一份精心构造的 AGENTS.md,指示 Codex 往所有 Golang main 函数注入五分钟 `time.Sleep`,并附带隐身指令:不得在 PR 描述、commit message 和摘要里提及这处修改,甚至在代码注释里写"AI 摘要器请勿提及"。攻击前提是依赖已被攻破(攻击者已有代码执行权),NVIDIA 把它定性为 agent 开发环境特有的新型供应链风险维度;披露时间线:2025-07-01 提交 OpenAI,OpenAI 确认后拒绝修改,理由是风险不超出"被攻破的依赖"本身已能做到的事。演示仅针对 Codex;`.cursorrules`、CLAUDE.md、copilot-instructions.md 被列为同类风险面(风险类别陈述,非已演示的 PoC)。【已验证;博客发布日期各索引口径不一,2026 年上半年】

**编辑器自动注入路径。**VS Code 从 v1.104 起**默认**把工作区根目录的 AGENTS.md 注入每一次 chat 请求(`chat.useAgentsMdFile`,源码确认"未显式关闭即包含");安全厂商 Prompt Security 的 PoC 演示了打开一个恶意 repo、在聊天框输入任意一个字符,注入的指令即可把 agent 引向数据外传。该攻击对应的分类——OWASP 2026 年 Agentic Applications Top 10 的 ASI01(Agent Goal Hijack)与 ASI02(Tool Misuse & Exploitation)——是真实存在的官方分类法(2025-12-09 发布),但把这个具体发现归入哪一类是厂商自己的标注。【已验证】要点:自动注入是**有文档记载的、按设计的产品行为**,不是未公开漏洞——这正是它成为稳定攻击面的原因。

更广的背景数字——78 项研究的 meta 分析称自适应攻击对最先进防御的成功率超过 85%,四大 coding 平台全数未能拦截复合多层攻击【未验证,来源:arXiv 2601.17548】——本轮未做逐票核验,仅作方向参考。

工程含义三条:**打开第三方仓库时把上下文文件当不可信输入**(检查编辑器的自动加载开关);**把上下文文件的 diff 当代码 review**(尤其来自自动化 PR 和依赖更新的);**构建环境里限制对 AGENTS.md/CLAUDE.md 的写权限**(NVIDIA 攻击的写入点)。

## 9. 落地 playbook:给公司代码库制定 plan

以下步骤把前八章的证据收敛成可执行方案。设计原则只有三条:先做便宜且被验证的,每一步可度量,厂商口径当默认值而不是真理。每步标注证据等级。

**Step 1 盘点(半天)。**列出团队实际在用的 agent(决定文件名与互认矩阵,见第 2 章【已验证】);标记 monorepo/多仓拓扑;给现有文档质量打分——**这是最重要的一步**,因为对照证据说上下文文件的价值来自不冗余信息:README 已经很好的仓库,收益预期要调低;文档荒地仓库,收益最大(AGENTbench 消融【已验证】)。

**Step 2 选标准(一次性决策)。**默认选 AGENTS.md 做单一事实源 + 为 Claude Code 建 symlink(`ln -s AGENTS.md CLAUDE.md`);在文件头写明"本文件是唯一事实源,不要往其他规则文件加内容"(Sentry 模式【已验证】)。如果团队只用 Claude Code,直接 CLAUDE.md 亦可,别双维护。

**Step 3 根文件最小可用(每仓 1-2 小时)。**内容按验证过的高信号模式:(a) 可执行命令带完整 flags,放最前,**每条都实际跑过再写**(GitHub 官方生成 prompt 的要求【厂商口径】);(b) 三五行目录地图;(c) 边界规则用 always / ask-first / never 三档,爆炸半径最大的放第一条(Cloudflare 的 pnpm 禁令模式【现场证据】);(d) 只写 agent 猜不到的:团队命名法、非标准工具链、repo 礼仪(Airflow 的 Dag/breeze 模式【现场证据】)。预算:200 行/2 页以内起步(厂商口径;记住 Codex 有 32 KiB 硬截断【已验证】)。**不要**把人类 README 复制进来(冗余是实测的负收益来源【已验证】),**不要**在有文档的仓库上让 LLM 全自动批量生成(实测普遍降成功率【已验证】;`/init` 生成初稿后人工修剪是厂商推荐的用法【厂商口径】)。

**Step 4 monorepo 分层(按需)。**根文件放全局约定与路由,只给高价值/高风险的子包加嵌套文件,依赖"最近文件优先"语义(规范+四厂商一致【已验证】;"根文件当路由器"是 Datadog 实践【未验证】)。警惕 Anthropic 自己承认的治理失效:约定漂移、文件过期、根文件没人认领【已验证,厂商口径】——每个文件写个 owner。

**Step 5 度量与期望管理(试点 2-4 周)。**向管理层报告时用被验证的预期:**效率收益(时间/token 下降)是有对照数据的,成功率跳涨不是**【已验证】。度量方法:选 1-2 个试点仓库,建一套"每类常见任务 1-2 条测试提示词"的小套件,改版前后各跑一轮,记录完成率、耗时、token(方法来自 Datadog 实践【未验证】,但它本质上就是给文档建回归测试,成本低且无需相信任何人的口径)。结构折腾(位置、拆分)优先级放最低——受控实验找不到效应【已验证】。

**Step 6 维护与安全(常态化)。**维护:上下文文件的改动走 PR review;大模型版本更新后重审一遍(给旧模型打的补丁规则会变成纯开销);可选 Stop hook 自动从会话记录提议更新(三条均为 Anthropic 官方建议【厂商口径】;"这些文件像配置代码一样高频演化"是实证观察【已验证】)。安全:CI 对上下文文件的变更加 required review,特别拦截来自自动化 PR/依赖机器人对 AGENTS.md 的写入(NVIDIA 攻击路径【已验证】);安全团队审一遍各编辑器的自动加载默认值【已验证】。最后,**不要写 llms.txt**,除非你核实了某个你在乎的消费方真的读它【已验证】。

反模式清单(全部前文有据):复制 README 全文;LLM 全自动生成后直接提交;单个巨型根文件服务 monorepo;把"短=更听话"当已证事实到处布道;在 14.5% 俱乐部里裸奔(不写任何安全边界);把第三方 repo 的上下文文件当可信内容。

## 10. 结论:十个可检验主张

1. **上下文文件的已证实收益是效率而非能力**:-28.64% 中位耗时、-16.58% 中位输出 token、成功率不变(单 agent 配对实验);多 agent 对照里成功率总体不升反微降。可被未来更大规模复现推翻。
2. **LLM 全自动生成的上下文文件在有文档的仓库上是负收益**(-0.5 到 -2pp),在无文档仓库上转正(+2.7%)——价值来自不冗余信息。
3. **开发者手写文件的收益是边际的(+4%)且不均匀**——在被测配置里对 Claude Code 无效;宣传"手写就有大收益"缺乏依据。
4. **"怎么排版"的民间智慧未获证实**:大小(25-500 行)、位置、架构、矛盾四变量对遵从率无可检测效应,大小与矛盾是贝叶斯确证的零效应;任务类型与会话内位置才是主变量。
5. **"短"的可靠论据是上下文预算与实测的长上下文退化,不是"短了更听话"**;Codex 的 32 KiB 静默截断把预算变成了硬约束。
6. **AGENTS.md 在标准之争中事实胜出**(LF 中立托管、Cursor/Copilot/VS Code 原生消费、60k+ 松口径采用),但互认不对称,Claude Code 体系独立,symlink 仍是通用解。
7. **生产级高信号文件收敛于:命令优先带 flags、三档边界规则、只写猜不到的**——四个头部 repo 逐字核验一致,与 2,500 文件的厂商归纳吻合。
8. **实际文件的系统性缺口是非功能项**:安全与性能指引各仅 14.5%。
9. **上下文文件是已演示的攻击面**:供应链写入(NVIDIA PoC)+ 编辑器默认自动注入(VS Code v1.104),对应 OWASP ASI01/ASI02;把它们的 diff 当代码审。
10. **llms.txt 是"采用≠消费"的盖棺案例**:8.8 倍增长与 97% 零请求并存,主要 AI 厂商无一消费。写机器文档前先核实读者存在。

值得盯的后续判据:AGENTbench 式对照会不会在非 Python、更大 PR 上复现;Claude Code 在 dev 文件上的"无收益"是工程差异还是测量噪声;会话内衰减(OR=0.944)能否被第二个团队预注册复现;OWASP ASI 分类下第一批真实世界(非 PoC)的上下文文件注入事件何时出现。

---

## 附:主要来源

**标准与规范**:agents.md 官网与 spec repo(github.com/agentsmd/agents.md) · Linux Foundation 新闻稿(Agentic AI Foundation,2025-12) · InfoQ(2025-08,2 万仓库基线口径)

**厂商官方文档**:Anthropic — code.claude.com/docs 的 best-practices、large-codebases、memory 页 · OpenAI — developers.openai.com/codex/guides/agents-md 与 codex 源码(codex-rs/core/src/agents_md.rs) · GitHub — docs.github.com Copilot custom instructions;github.blog "How to write a great agents.md: lessons from over 2,500 repositories"(Matt Nigh,2025-11) · Cursor — cursor.com/docs/rules · VS Code — v1.104 release notes 与 microsoft/vscode 源码

**独立实证**:Gloaguen, Mündler, Müller, Raychev & Vechev, "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"(arXiv 2602.11988,ETH Zurich/LogicStar.ai) · Lulla, Mohsenimofidi, Galster, Zhang, Baltes & Treude, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents"(arXiv 2601.20404,JAWs@ICSE 2026) · McMillan, "Instruction Adherence in Coding Agent Configuration Files"(arXiv 2605.10039) · Chatlatanagulchai 等, "Agent READMEs: An Empirical Study of Context Files for Agentic Coding"(arXiv 2511.12884) · Hong, Troynikov & Huber, "Context Rot"(Chroma 技术报告,2025-07)

**llms.txt 体检**:Ahrefs, "We Analyzed 137K Sites: 97% of llms.txt Files Never Get Read"(2026-06) · Originality.ai llms.txt 追踪研究 · John Mueller Bluesky 原帖(2025-06-17)与 Search Engine Roundtable/Journal 报道 · Chrome Lighthouse 13.3 agentic browsing 文档

**安全面**:NVIDIA Technical Blog, "Mitigating Indirect AGENTS.md Injection Attacks in Agentic Environments" · Prompt Security, "When Your Repo Starts Talking"(厂商 PoC) · OWASP Top 10 for Agentic Applications 2026(ASI01/ASI02,2025-12) · arXiv 2601.17548(prompt injection meta 分析,未验证)

**现场文件**(2026-07-15 逐字核验):getsentry/sentry、cloudflare/workers-sdk、apache/airflow、coder/coder 各自的 AGENTS.md · Datadog 前端工程博客(dev.to,未验证)

*调研材料与全部验证判定存于研究底座(仓库 research/agent-readme/:两轮共 35 组承重论断 × 3 票,105 票全录,含全部口径修正)。*
