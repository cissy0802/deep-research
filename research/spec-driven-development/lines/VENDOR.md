# VENDOR 线 · 厂商口径摘要(#25 spec-driven development)

> 34 条论断(V01–V34),全部是【厂商】自述或转述厂商数据的【媒体】/【官方】。抓取时间 2026-11-11。
> **网络限制**:本会话只能访问 github.com(WebFetch + git 克隆)和搜索引擎摘要。github.blog、kiro.dev、tessl.io、thoughtworks.com、youtube.com、ai.engineer、cursor.com、npm/pypistats 全部不可达。所以 Kiro、Tessl、Thoughtworks、Cursor、Copilot 的论断都是 `secondhand`,quote 留空,成文前须回原页核对。逐字核对过的只有本地克隆的仓库文件和 Grove 演讲的第三方 Whisper 转录。

## 1. GitHub Spec Kit(谁受益:GitHub/微软,Copilot 渠道)
- **关注度**(V01):149.2k stars / 13.4k forks / 741 watching。数字经 WebFetch 转述,API 被拒,没有交叉核对。**拿不到任何下载量或使用量数据。** star ≠ 采用。
- **时间线**(V02):2025-08-21 首次提交;2026-01-22 主维护者换人;2026-08-21 发布 1.0;2026-11-10 发布 1.4.0;共 245 个版本条目。
- **叙事转向**(V03,强):v0.0.17(2025-09)的 README 有「Experimental goals」一节,原文是要 "Validate the hypothesis…"。当前 README 删掉了这一节的文字,只留下锚点。**厂商从未发布过验证结果**,实验框架就悄悄变成了产品。
- **规范性主张**(V04、V06):"code serves specifications"、"there is no gap—only transformation"、"Specifications stay in sync with code because they generate it",都是机制断言,没有测量。
- **唯一的量化对比**(V05,弱):「~12 小时 vs 15 分钟」出自一个虚构的聊天功能示例,只算文档生成的墙钟时间,不算审阅时间,也不看质量。**不得作为效率证据。**
- **自家 dogfood 的反向事实**(V07,本线最强证据):CONTRIBUTING 写明不是每个变更都走全流程,并且 `.specify/`、`specs/` 被**刻意 gitignore**,不进入仓库历史。也就是说,最大的 SDD 工具自己只做到 spec-first,没有把 spec 当作长期维护的事实源。这与 V06 的"保持同步"主张冲突。
- **生态扩张**(V08):43 个 integrations,5+197 个 extensions,2+42 个 presets。README 自己声明 "Catalog listings are not audits or endorsements"。现在 SDD 在 Spec Kit 里只是几个入口之一(另有 bug fixing、idea assessment)。
- 宪法九条(V09):Test-First 等门禁由 LLM 自评执行,没有找到遵从率数据。
- GitHub 博客发布文(V10):"from code is the source of truth to intent is the source of truth"。目前只有搜索摘要,待核。

## 2. OpenSpec(Fission-AI)与 BMAD(BMad Code, LLC)
- OpenSpec(V11–V14):74.6k stars;自称 "The most loved spec framework"(没有数据)。竞品互评说 Spec Kit "Thorough but heavyweight"、Kiro "locked into their IDE and limited to Claude models"(后一条已过时)。定位是 brownfield、"iterative not waterfall"。**自家仓库确实在 dogfood**:44 个 spec、108 个已归档变更(n=1 仓库)。默认开启匿名遥测:厂商手里有真实使用数据,但没有公开。
- BMAD(V15–V16):55.2k stars;名称是商标,项目接受赞助,README 号召 "Star the repository"(star 受号召驱动)。README 写 "Small changes go straight to build",**厂商自己承认全流程对小任务不划算**。

## 3. AWS Kiro(谁受益:AWS;也是 credit 卖方)
- V17:2025-07-14 preview,2025-11-17 GA。GA 的 property-based testing 原文自我限定为 "not verification or proof"(摘要,待核)。
- V18 用量:首周 10 万+、三个月 25 万+、3 亿次请求,都是 AWS 自报。**口径是"用过 Kiro",不是"用过 spec 模式";spec 与 vibe 的使用占比从未披露。**
- V19 定价史:2025-07 按交互次数计;2025-08 拆成 spec/vibe 两种请求,Pro 为 125 spec + 225 vibe,舆论称之为 "wallet-wrecking";之后承认计量 bug 并退款;2025-09 改为统一 credits(Pro $20 = 1,000 credits,超额 $0.04/credit)。**单独给 spec request 定更紧的额度,是"流程税"的间接信号**,但这是定价口径,不是 token 口径。
- V20:2026 年 Pro Max、预付 add-on、模型倍率多次调整,第三方来源互相矛盾,只能定性引用。
- V21 客户案例:PKFARE 称"months to days"、"3 天→半天";Socure 称"估计 3 周、实际 2 天"。基线都是估计值,属卖方挑选的案例,不能当效果证据。

## 4. Tessl(spec-as-source 的旗手)
- V22 融资:1.25 亿美元(种子 2,500 万 + A 轮 1 亿,2024-11 宣布)。估值有 **$500M+ 与 $750M 两个口径,不得混引**。当时承诺"早 2025 上线",实际 2025-09 才发布 registry。
- V23:Spec Registry(open beta,宣称 "10,000+ specs")和 Framework(closed beta)。这 10,000 个是**库用法文档,不是应用级 spec-as-source**。
- V24(对核心主张 3 重要):2026-01 起转向 "skills 包管理器 / Agent Enablement Platform"。代码再生引擎从未 GA,据评论者描述是非确定性的。**最激进的 spec-as-source 厂商在产品层面转向了。** 这条全部来自二手,须回原页核对。
- V25:Podjarny 的单点预测"2027 年底开发者大多不看代码"。按红线,只能作为利益相关方的预期引用。

## 5. 「specs are the new code」逐字溯源(V26–V28)
- 出处:Sean Grove(OpenAI 对齐团队),AI Engineer World's Fair 2025 的演讲 "The New Code"(YouTube 8rABwKRsec4,约 21 分钟)。活动页标题是 "The New Code: Specifications as the Source of Truth",URL slug 是 specifications-are-the-new-code。
- **可得转录里没有"specs are the new code"这句原话。** 最接近的是 [00:00:43] "the coming of the new code, in particular specifications"。**这个口号是标题和媒体压缩出来的。** 成文建议写成"Grove 演讲《The New Code》",不要加引号当原话。
- 转录质量:来自 lawwu/transcripts 的 Whisper 自动转录,首行有幻觉文本,时间戳是近似值。没能对上官方字幕。
- "10–20% / 80–90%"([00:02:44]):修辞断言,带 "sort of",没有出处。
- 语境迁移:Grove 的 spec 主要指 OpenAI **Model Spec**(模型行为规约 + 评测,偏 T4,"test against the spec"),被 SDD 厂商移用到应用 PRD 语境(T1)。

## 6. Plan 模式(T2,工具内可选模式 ≠ SDD 方法论)
- Claude Code(V29–V30):CHANGELOG 里有 opusplan、Plan 子代理,"Plan Mode now builds more precise plans…",以及修复"压缩后丢失 plan mode"的 bug。官方最佳实践写 "If you could describe the diff in one sentence, skip the plan"(摘要)。**利益披露:Anthropic 是本研究所用工具的厂商。**
- Cursor 1.7/2.1、VS Code 1.105 Plan agent、GitHub changelog(V31):"agent 运行更久"是时长口径,"检查需求覆盖"是功能描述。都没有效果数据。
- Augment Intent(V32):宣称 "living spec" 会自动更新。搜索结果被 Augment 的 SEO 对比页大量污染。

## 7. Thoughtworks Radar(V33–V34,【官方】但属专家判断)
- Vol.33(2025-11-05):SDD 列在 **Assess**,并警告 spec 冗长难审、可能重学"手写规则不可扩展"的教训。Vol.34(2026-04):Spec Kit 列在 Assess,brownfield 为主,资深工程师获益最多。
- Vol.35:搜索结果矛盾。据二手报道 OpenSpec 升到 Trial,依据是团队的主观报告。SDD 条目当前的环位**未能确认**。
- **非独立**:Thoughtworks 和 Böckeler(CON 线)是同一家公司。"waterfall"一词没有在 blip 原文中找到。

## 最强 / 最弱
- **最强**:V07(Spec Kit 自家 specs/ 被 gitignore,本地逐字核对);V03(实验框架被删、验证结果从未发布,tag 间可比对);V26(口号不是 Grove 原话,有带时间戳的转录)。
- **最弱**:V05(虚构的 12h vs 15min);V18(Kiro 25 万用户,自报、口径错位、原文未定位);V25(Podjarny 单点预测)。

## 缺口
没有拿到任何下载量或安装量数据;Kiro spec 与 vibe 的使用占比从未披露;所有厂商都没有自测效果数据;Kiro、Tessl、Thoughtworks、GitHub 博客的原文都没能逐字核对(网络限制)。需要放行的主机:kiro.dev、tessl.io、thoughtworks.com、github.blog、youtube.com、ai.engineer、aws.amazon.com、npmjs.com/api.npmjs.org、pypistats.org、techcrunch.com、code.claude.com、cursor.com、code.visualstudio.com。
