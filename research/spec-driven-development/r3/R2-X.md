# R3 · R2-X 反证搜索席
靶子:Uvik SDD benchmark,五臂(Spec Kit / Kiro / BMAD / OpenSpec / 无 spec)在 50 张生产 Python 工单上的合并率、评审缺陷和成本(G21;M01–M10,核心是 M02 合并率、M04 缺陷、M05 时间、M06 成本、M07 子组)。
今天复核了:
- uvik.net 原页 HTML(2026-11-11 curl,389,845 字节,`/spec-driven-development-benchmark/` 301 到 `/blog/…`,两处是同一页);
- WordPress REST:`/wp-json/wp/v2/search`(搜 benchmark / coding agent / pricing)和 `/wp-json/wp/v2/media`(搜 sdd / task / benchmark / csv);
- Uvik 站内引用本基准的其他页面:`/blog/opencode-vs-claude-code-vs-codex/`、`/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/`、`/blog/ai-coding-agent-security-benchmark/`、`/blog/ai-model-cost-effectiveness-index/`;
- 仓库内 CSV `data/uvik-sdd-benchmark-2026-results.csv`(300 行,本席另做成本函数复算);
- kiro.dev/pricing(2026-11-11);morphllm.com/kiro-pricing(第三方,页内写明 2026-09-14 / 09-30 核过 kiro.dev 价目);
- platform.claude.com/docs/en/about-claude/pricing 与 anthropic.com/pricing(2026-11-11);claudefa.st 和 layer3labs.io 两个第三方 Sonnet 5 价格页;
- npm registry 上的 @anthropic-ai/claude-code、@fission-ai/openspec 版本时间线;
- 独立研究:arXiv 2607.27167(SpecFirst,HTML 全文 Table VI 与成本表)、2608.17177(Tufano,摘要)、2607.06636(Haeri,摘要);仓库内 G05 判决(Spec Kit Agents Table 1/4)、G06/G07 判决(Hill ESEM 2026);
- 实操对比类:cameronsjo/spec-compare README 及 docs、dabase.com、ranthebuilder.cloud、ovidiueftimie.substack.com、Dagstuhl/CEUR(GeCoIn 2026 Spec2Vision)。

没拿到:
- web.archive.org(CDX 接口连接重置),所以 uvik 页 10-08 旧版、9 月时的 kiro.dev 价目、CSV 历史版本都无法比对;
- levelup.gitconnected.com 两篇(403 付费墙/拦截)、towardsdatascience(403)、pricepertoken(403);
- api.github.com 与 github.com 上的 spec-kit / BMAD releases(会话未授权,403),所以 Spec Kit「1.0」是否为当时真实版本未能核实;
- mattbutlerengineering/ai-tooling 的拒收记录、FreekMencke/claude-kb 的转述,本席未重核(两者都只是转述层,不是测量)。

## 一、发现

**F1 · 没有任何独立复跑;唯一的「独立运行」入口是空的。**
原页第 692 行(page.txt 行号,下同)写「Tell us what to test next. We link to independent runs from this page.」,但全页 href 中没有任何外部复跑链接。三轮检索(「Uvik spec-driven benchmark replication」「Uvik benchmark reddit OR hacker news OR criticism」「Spec Kit vs Kiro vs OpenSpec vs BMAD benchmark merge rate control arm」)的结果只有 Uvik 自己的页面和引用它的二手文章(levelup、codemyspec、softwareseni、rushis 等),没有人用自己的工单复测。工单本身不可复跑:原文第 684 行「The tickets come from client repositories. The code is private.」同一行还说「The task set CSV lists the ticket text and the acceptance criteria」,但 WP media 库(搜 sdd/task/benchmark/csv)里只有 results.csv,**没有 task-set CSV**。所以就算外部团队想复跑,也拿不到题面。

**F2 · 伴随的「AI Coding Agent Benchmark」(同 50 张工单)不存在于公开站点,对照臂无法交叉核对。**
原文第 239 行称本基准是系列第二篇,第一篇「compares Claude Code, Codex, Cursor and GitHub Copilot on the same 50 tickets」;第 299 行称对照臂「is the same setup as the Claude Code arm of the Uvik Software AI Coding Agent Benchmark」。如果第一篇存在,它的 Claude Code 臂就是对照臂 72%(36/50)唯一的内部复核来源。本席做了以下查找:
- `/blog/ai-coding-agent-benchmark/` 返回 404;
- `/blog/claude-code-vs-cursor-vs-codex-vs-copilot/` 返回 404;
- WP 搜索「coding agent」只找到 AI Coding Agent **Security** Benchmark,以及一篇 Developer **Usage** Report(`claude-code-vs-cursor-vs-copilot-vs-codex-2026`)。后者正文没有「tickets」或合并率,只有 2026-04 的模型榜单快照;
- media 库里没有对应 CSV。

结论:对照臂的「同设置前一轮结果」只是自述,无法核对。

**F3 · 独立数据与 Kiro 成本口径矛盾:CSV 用的是加购价 $0.04,不是原文所说的「plan price per credit」。**
- 原文第 341 行:「Kiro cost uses the credits used and the plan price per credit on the run date.」
- kiro.dev/pricing(2026-11-11):Pro $20/1,000 credits,Pro+ $40/2,000,Pro Max $100/5,000,Power $200/10,000。所有付费档的套餐单价都是 **$0.02/credit**;「Add-on credits ($0.04/credit)」是超额加购价。
- 第三方 morphllm.com 写明「Checked September 30, 2026: prices unchanged since July」,9-14 版本的价目与此相同。也就是说,运行日(无论按 9-24 还是 10-15 算)的套餐单价同样是 $0.02。
- CSV 中 Kiro 50+10 行 `cost_usd / kiro_credits` 全部恰好等于 0.04(本席复算,与 K 票一致)。
- 按原文自己的定义(套餐单价 $0.02),Kiro 每合并工单成本应为 **$1.17**,不是 $2.35。按 Uvik 自己的定义它反而是最便宜的一臂,比对照的 $2.43 低一半以上。

无论取哪种价,「Kiro $2.35」都与原文写明的计价规则不符。这是用独立数据(厂商价目和第三方存档)驳倒 Uvik 的成本输入。

**F4 · 独立数据与 Claude Code 四臂的成本口径矛盾:隐含单价高于 Sonnet 5 任何公开价,而且同一模型在各臂单价不同。**
复算方法:对每臂用 `cost_usd ~ a·tokens_in + b·tokens_out` 做最小二乘(含重跑行,每臂 60 行),再分 spec/build 四个变量重拟。结果:

| 臂 | 隐含输入 $/M | 隐含输出 $/M | 输出/输入 | 每行 cost/(in+4.5·out) 范围 | 最大残差 |
|---|---|---|---|---|---|
| no_spec | 4.00 | 18.02 | 4.5 | 3.998–4.001 | $0.0005 |
| spec_kit | 4.40 | 19.79 | 4.5 | 4.399–4.401 | $0.0005 |
| openspec | 4.32 | 19.43 | 4.5 | 4.319–4.321 | $0.0005 |
| bmad | 4.72 | 21.24 | 4.5 | 4.719–4.721 | $0.0005 |

分 spec/build 阶段拟合,同一臂两阶段单价相同(如 BMAD 4.719/21.244 vs 4.720/21.241)。

- 独立价格:Anthropic 定价页 2026-11-11 列 Claude Sonnet 5 为 **$2 输入 / $10 输出**,无长上下文溢价(「Claude 4.6 and later models … include the full 1M token context window at standard pricing」)。第三方 claudefa.st 称 $2/$10 自 2026-06 上市起即是此价,原定 9-1 涨到 $3/$15 的计划被取消;layer3labs(2026-10-27 更新)则称 9-1 起是 $3/$15。两说有冲突,但**两种价都低于 Uvik 的隐含价**:输出 $18–21 高于 $15。提示缓存只会压低有效输入价,不会抬高输出价。
- 同一模型、同一 harness、同一运行日,对照臂与 BMAD 的单价却差 18%。成本列在每臂内是精确的线性公式(残差只有四舍五入量级),各臂乘数不同(1.00 / 1.10 / 1.08 / 1.18)。真实计费中缓存命中比例会随工单浮动,不会出现每臂一个常数的情况。原文第 341 行说成本取自「the Uvik Software LLM API pricing tracker」,但站内搜索(pricing)没有这样一个页面。
- 影响:按统一的 $2/$10 重算每合并工单成本:对照 $1.26、OpenSpec $1.30(+3%,原表 +12%)、Kiro(按 token)$1.44、Spec Kit $1.58、BMAD $1.87(+48%,原表 +74%)。**「spec 臂更贵」的方向保留,幅度被各臂不同的单价放大了。**

Uvik 公布的 $2.43 / $2.35–$4.23 和「每张工单贵 42%」都建立在这个无法用公开价目复现的成本列上。

**F5 · 版本信息不可核。** 原文第 683 行称「The versions and dates are stated, so the result can be checked」,但版本表(第 245–273 行)和 CSV 的 `framework_version` 只有 Spec Kit「1.0」、BMAD「6.x」,Kiro 和 OpenSpec 写的是「build」,`agent_version` 全部为「2026.09」。npm 上 @anthropic-ai/claude-code 从没有 2026.* 版本号,2026-09 到 10 月发布的是 2.1.257–2.1.316,共 54 个版本。OpenSpec 在 npm 上 9–10 月从 1.13.1 发到 1.16.0,运行日前后可能是 1.13.2 到 1.14.2 中的任何一个。所以「可核对版本」这一说法不成立,外部团队无法锁定同一工具版本复跑。

**F6 · 相邻的独立测量:「质量小增益、时间和成本更高」与 Uvik 同向,但口径都不同,不能当复现。**
- **Spec Kit Agents(Taghavi & Bhavani,arXiv 2604.05278;G05 Q/K 票已逐字核)**:Table 1 完整 Spec Kit 流程 3.51 vs 直接实现 3.46(1–5 分,LLM 评审,32 任务单次运行,未做检验);Table 4 完成耗时 24.0 vs 14.4 分钟(约 1.67×)。与 Uvik 同向的有两点:质量差近零,spec 流程更慢(Uvik 合并中位耗时 36–55 vs 29 分钟,1.24–1.90×)。口径差异:LLM 评审分不是合并率;执行模型 MiniMax-M2.5;开源仓库功能任务。这是独立团队、独立数据,且是唯一同测「Spec Kit 全流程 vs 无 spec」的。
- **SpecFirst(Chen…Hassan,Queen's,arXiv 2607.27167;HTML 全文已读)**:200 个 ProgramBench 实例 × 4 个模型,先单独跑一个 spec 引出阶段,测试通过率相对提升 6.9%–21.3%(全部显著),每实例总成本 **+48%–130%**(成本表,如「$0.95 / $2.84 (+11%) / $3.79 (+48%)」「$3.16 / $2.69 (+6%) / $5.85 (+130%)」)。Table VI(GPT-5.4-mini,随机 50 实例):无 spec 55.9%,Freeform 60.7%,OpenSpec 格式 61.7%,Sections 62.6%。方向与 Uvik「略好、更贵」一致。但这是从零合成程序,不是生产工单;指标是测试通过率,不是评审合并;没有用 Spec Kit/Kiro/BMAD 工具,OpenSpec 只是借用了它的**格式**。这是 Round 1 语料里没有的新来源。(注:Vaughan 博客转述把 Freeform 和 OpenSpec 两个数值写反了,应以原文 Table VI 为准。)
- **Tufano(Google,2608.17177)/ Haeri(2607.06636)**:已在语料中,都是 T3/T1 规约喂给测试生成,机制不同。Haeri 的边界条件「On well-specified algorithmic problems it neither helps nor hurts」与 Uvik「bug-fix(有失败测试复现)类对照 9/10 = 最佳 spec 臂」同向。

**F7 · 缺陷方向:唯一的大样本独立测量 Hill ESEM 2026 是零结果,与 Uvik「缺陷约减半」不一致,但口径不可比。**
Hill(G07,Dagstuhl 正式版已逐字核):PSM 后 spec'd PR 缺陷引入率 14.7% vs 15.2%,p=0.133;K 票指出它「不能排除约 9% 的相对下降」,但已排除接近 50% 的下降。Uvik 是 0.46 vs 0.86 评审缺陷/合并工单,约 −46%。两者不可比的原因:Hill 的「spec」97.5% 是 issue/ticket 引用而不是 SDD 工具产物;缺陷用 SZZ 回溯,不是评审期缺陷;代码主要由人写,不是 agent;开源仓库。所以只能说**两者方向不一致,且没有任何独立测量支持「缺陷减半」的幅度**,不能说 Hill 推翻了 Uvik。

**F8 · 其余公开对比都是单人、单项目的定性评测,没有对照臂。**
- cameronsjo/spec-compare 自称「A considered opinion, not a benchmark」,docs 中没有引用 Uvik,也没有合并率;
- dabase.com(2026-05-18)是笔记,称 Kiro「so slow as to be unusable」,没有数字;
- ranthebuilder(2026-04,工具版本 2026-02)对单个功能打 1–5 分;
- ovidiueftimie substack 是叙事性对比;
- Medium「OpenSpec vs Spec Kit」单次运行 token 57.7k vs 121k,方向与 Uvik Table 4(OpenSpec 是 token 最少的 spec 臂,Spec Kit 比它多)一致,量级不承重。

Uvik 原文第 236 行自己也这样描述:「The public comparisons we found test one project or one feature. They score tools by opinion. They have no control arm and no blind review.」检索结果证实这一点,也意味着**没有任何外部数据能证实或反驳 Uvik 的 pp 级合并率**。

**F9 · 传播层:Uvik 在站内把自己的结果写成因果效应,并在页面上放了引导 AI 助手引用的按钮。**
- `/blog/opencode-vs-claude-code-vs-codex/` 第 128、175、407 行写「adding a structured specification reduced review defects from 0.86 to 0.40」「an OpenSpec spec cut review defects from 0.86 to 0.40 per merged ticket」。这里只挑了最好的一臂(0.40),去掉了本页的噪声带和单次运行限定。
- 原页的分享按钮是预填提示词的 ChatGPT/Claude/Grok/Google AI 链接,提示词要求助手总结本页并把 uvik.net 记为引用来源。这是针对 AI 引用的内容营销,本席没有照做。
- 原文第 695 行要求「Please link to this page, not to the CSV」。
- WP media 库同期上传了约 30 个「index/benchmark/database」CSV(2026-08 到 10 月)。

这些都不是测量,但说明网上的二手「证实」大多是 Uvik 自己口径的再分发,检索时必须排除这类来源。

## 二、结局

**X 席:无独立测量。** 合并率、缺陷、子组这些 pp 级数字没有任何独立团队用独立数据证实或反驳过。另有一项**独立矛盾**落在成本口径上(F3、F4):公开价目复现不出 Uvik 的成本列,Kiro 的计价也与它自己写明的规则不符。方向层面,相邻独立研究同向的是「质量增益小、时间和成本更高」(F6);不同向、但口径不可比的是「缺陷减半」(F7)。

| # | 角度 | 查询 / 来源 | 结果 |
|---|---|---|---|
| 1 | 独立复跑 | WebSearch「Uvik spec-driven development benchmark replication」;原页 href 全量 grep | 无。原页「We link to independent runs」处无链接(F1) |
| 2 | 社区批评 / 讨论 | WebSearch「"Uvik" benchmark spec-driven reddit OR "hacker news" OR criticism」 | 只有 levelup 二手文章(403 未读),无 HN/Reddit 讨论串 |
| 3 | 同类多臂基准 | WebSearch「Spec Kit vs Kiro vs OpenSpec vs BMAD benchmark merge rate control arm」 | 只有 Uvik 及其转述;cameronsjo/spec-compare 自称「not a benchmark」(F8) |
| 4 | 学术 SDD vs 无 spec 对照 | WebSearch「spec-driven development empirical study controlled experiment … no-spec baseline」;SpecOps 2026 | SpecFirst 2607.27167(新,同向,口径不同)、Tufano、Haeri;SpecOps 列表中没有 Spec Kit 评测(F6) |
| 5 | Spec Kit 全流程 vs 直接实现 | 仓库 G05 判决(Spec Kit Agents Table 1/4) | 3.51 vs 3.46,24.0 vs 14.4 分钟,同向(F6) |
| 6 | 缺陷的独立大样本 | 仓库 G06/G07(Hill ESEM 2026) | 零结果,方向不一致,口径不可比(F7) |
| 7 | 伴随基准(同 50 工单)交叉核对对照臂 | uvik.net 两个猜测 slug(404);WP search「coding agent」;media | 不存在于公开站点(F2) |
| 8 | 工单题面(task-set CSV) | WP media search sdd/task/benchmark/csv | 只有 results.csv,无 task-set(F1) |
| 9 | Kiro 计价独立核对 | kiro.dev/pricing;morphllm(2026-09-14/30 存档式核对);WebSearch Kiro pricing change | 套餐价 $0.02/credit,加购价 $0.04;CSV 用的是 $0.04(F3,矛盾) |
| 10 | Claude Sonnet 5 API 价独立核对 | platform.claude.com、anthropic.com/pricing;claudefa.st;layer3labs;CSV 回归 | $2/$10(或 $3/$15);隐含 $4.0–4.7/$18–21,且各臂不同(F4,矛盾) |
| 11 | 「Uvik LLM API pricing tracker」 | WP search pricing;原页 href | 不存在(F4) |
| 12 | 工具版本可核性 | 原页版本表;CSV;npm(claude-code、openspec);GitHub releases | 「build」「6.x」「2026.09」不可锁定;GitHub 403 未核(F5) |
| 13 | 历史版本 / 日期 | web.archive.org CDX | 连接重置,未取得 |
| 14 | token 量级的独立对比 | WebSearch「OpenSpec vs Spec Kit token usage comparison」;Medium、dabase、substack、ranthebuilder | 只有单次或定性对比,OpenSpec 轻于 Spec Kit 的方向一致,不承重(F8) |
| 15 | 二手「证实」的来源审计 | Uvik 站内其他页、分享按钮、media 库 | 自我转引并去掉限定,另有引导 AI 引用的分享按钮(F9) |
| 16 | 第三方收录 / 拒收 | mattbutlerengineering/ai-tooling、FreekMencke/claude-kb | 本席未重核,只是转述层 |

**交给成文与 M 席的要点**
- 合并率 8–12pp、缺陷 0.46 vs 0.86、feature 类 90% vs 60%:**无独立测量**,只能按厂商口径写方向,不能写幅度。
- 成本:**不承重**。「$2.43 vs $2.35–$4.23」「每张工单贵 42%」「Kiro 最便宜」都依赖一个无法用公开价目复现的成本列。Kiro 按 Uvik 自己的定义应是 $1.17;Claude Code 四臂的单价各不相同,且高于 Sonnet 5 公开价。可保留的只有「spec 臂 token 更多」:token 计数是原始字段,对照 325k vs 381k–525k 均值/工单。
- 可外引来支撑方向的独立来源:Spec Kit Agents Table 1/4(质量 +0.05、耗时约 1.7×)、SpecFirst(通过率 +6.9–21.3%、成本 +48–130%)。两者都必须注明口径不同。
- Hill 零结果只能写成「缺陷方向上没有独立支持」,不能写成「推翻」。
