# R2-X 反证搜索席：Payne & Alloui-Cros「strategic fingerprints」

**判定：方向存争。** 「Claude 宽恕」有两支独立团队给出方向一致的证据。「Gemini 更不合作」有弱支持。「OpenAI 高度合作」被三支团队的数据反驳或削弱。厂商级「性格」在跨版本、跨 prompt 时能否稳定复现，目前没有证据。

## 原文状态
- arXiv 2507.02618 至今（2026-10-31）只有 v1（2025-07-03），没有 journal-ref，没有 v2，也没检索到同行评审版本。没有找到独立复现或专门批评它的文章，只有 podcast 和 review 站的转述。来源：https://arxiv.org/abs/2507.02618
- 自身局限（见 E29/E30）：每个条件只跑 1 次；用的是小型/快速档模型（gpt-3.5/4o-mini、gemini-1.5/2.5-flash）；Claude 只有 claude-3-haiku，且只出现在 1 场 Showdown 里。

## 独立证据
1. **Pal, Mallela, Hilbe, …, Nowak 2026**，arXiv 2601.09849（v1 2026-01-14，未见正式发表）。五个模型：claude-sonnet-4、gemini-2.5-pro、gpt-4o、gpt-5、llama-3.3-70b。
   - 支持 Claude 宽恕：Claude 基线策略是 Forgiver，且基本不随终止概率变化。原文 "Claude always opts for Forgiver"。
   - 弱支持 Gemini 偏狠：五个模型里只有它首轮会先怀疑，原文 "Only Gemini is suspicious: it cooperates 41 times in 50 trials."。终止概率上升时，它的合作率下降。
   - 反驳「OpenAI 高度合作」：gpt-4o 起手是 GRIM，提到终止概率后才转向类 WSLS；gpt-5 是唯一在已知 10 轮的最后一轮背叛的模型，代价高时接近 ALLD。最合作的是 Llama（类 GTFT）。
   - prompt 能翻转行为：competitive 框架下多数模型趋向 ALLD，altruistic 框架下趋向 ALLC。原文 "none of them exhibit full consistency over all tasks"。
   - URL：https://arxiv.org/abs/2601.09849
2. **Akata et al. 2025**，NHB（E26/E27）。GPT-4 遇到只背叛一次的对手后，原文 "never cooperates again"，是不宽恕的 Grim 型。这直接反驳「OpenAI = 宽恕/高度合作」。但它是已知 10 轮的有限博弈，与 Payne 的随机终止设定不同。
3. **Willis, Du, Leibo, Luck 2025**，arXiv 2501.16173，只有 v1（另有 AAMAS 2025 扩展摘要）。让模型写完整策略，再跑演化动态，比较 ChatGPT-4o 和 Claude 3.5 Sonnet。
   - ChatGPT-4o 产生最多的 aggressive 均衡：Default prompt、无噪声、4:1:1 侵略型占多数起步时，66% 收敛到侵略型。
   - Claude 3.5 Sonnet 最不侵略：均衡起步时只有 4% 收敛到侵略型，GPT-4o 是 14%。
   - 结论：Claude 那一侧方向一致；OpenAI 那一侧方向相反。
   - URL：https://arxiv.org/abs/2501.16173
4. **Zúñiga Bolívar 2026**，arXiv 2605.29874（v2 2026-06-14 为勘误，单作者，未经同行评审）。把 Willis 的基准扩展到 Claude Sonnet 4.6、Gemini 2.5 Flash / 3.1 Pro、GPT-5.4 Mini。
   - 摘要原文 "Provider identity, rather than model generation, is the strongest correlate"。
   - Gemini 2.5 Flash 在偏置条件下最高 77% 收敛到侵略型均衡；GPT-5.4 Mini 在 Self-Refine 下 70% 收敛到合作型均衡。
   - 这是 Payne 方向的唯一较直接的跨代支持，但证据强度弱：单作者、未审、发表前还改过一次关键数字（9/12 改为 10/12）。
   - URL：https://arxiv.org/abs/2605.29874
5. **Fontana, Pierri, Aiello 2024**，arXiv 2406.13605（E28）。GPT-3.5 比人类更合作、更宽恕（Payne 同样认定 gpt-3.5 合作）。同一厂商内部，Llama2 与 Llama3 的方向相反，说明「家族性格」在代际之间会翻转。
6. **Singh, Radhakrishna, Gulwani 2025**，arXiv 2509.04847，只有 v1。对阵 240 个经典策略，但没有公布所用模型和分模型结果，所以对家族论断是 null。论文自承 "the instructions in the prompt chosen heavily influence the behavior"。
7. **Huynh … Buscemi, Han 2026**，arXiv 2601.19082。payoff 放大后，LLM 反而更合作。摘要层面看不到逐模型的对比，对家族论断是 null，但能作为语言框架、payoff 敏感性的旁证。
8. **CoopEval**（Tewolde, …, Conitzer, Jin；ICML 2026，PMLR v306）。重复博弈带来的合作，在对手更换时会 "deteriorates drastically"。摘要里没有家族对比，对家族论断是 null。

## 搜索角度（含 null）
- arXiv abs 页查版本，以及「Payne Alloui-Cros 2026 journal」：只有 v1，没有发表版本。（null）
- 「Strategic Intelligence… replication OR critique」：没有独立复现或批评。（null）
- 「LLM IPD model family prompt sensitivity 2025」：找到 Willis、IBM ToM（LLaMA/Falcon 合作下降，Qwen 保持信任）、Zúñiga 2026、Bologna 硕士论文（prompt 敏感）。
- 「framing OR persona flips cooperation」：找到 2601.19082，以及一篇 Cambridge 托管的 Yamagishi 复制研究（框架对高级模型影响小，对 GPT-3.5 不稳定）。这篇与「框架翻转」部分相悖，未细读。
- 「same model different prompts / GTBench / GAMA-Bench」：没搜到 GTBench、GAMA-Bench 的 IPD 家族数据（null）。找到了 Pal/Nowak 2026、CoopEval、2603.19167（反事实 PD，摘要没有逐模型结果，null）。
- FAIRGAME 2504.14325：只是框架论文，见 E32，没有可用的 IPD 家族数字。（null）

## 文章可安全印出的句子
> 2025 年一篇尚未经同行评审的预印本（Payne & Alloui-Cros）让 OpenAI、Google、Anthropic 的模型参加演化囚徒困境锦标赛：每种条件只跑了一次，Gemini 表现得最冷酷，OpenAI 最爱合作，Claude 最宽恕。后来的独立研究只部分印证了这一点：Nowak 团队 2026 年的实验同样发现 Claude 偏「宽恕型」、Gemini 起手更多疑；但 GPT-4、GPT-4o 在其他实验里反而像「一次背叛、永不原谅」的冷酷触发者，换一种措辞，多数模型就会在全背叛和全合作之间翻转。所谓「厂商性格」更像特定版本、特定提示下的倾向，而不是稳定的指纹。
