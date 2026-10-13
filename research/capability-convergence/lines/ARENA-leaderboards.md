# ARENA-leaderboards 调研线(截至 2026-10-12,进行中)

## 数据来源与自算方法
- 官方数据:Hugging Face `lmarena-ai/leaderboard-dataset`(CC-BY-4.0,Arena 官方发布的历史榜单快照,最后更新 2026-10-13 UTC)
  https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset
  - text(原始 BT,2023-05-08..2026-10-08,248 次快照)、text_style_control(2024-08-28..2026-10-08,188 次)、webdev(Code Arena,2025-11-12..2026-10-09)、agent(IPS,2026-06-04..2026-10-12)
  - README 原文: "On January 9, 2024, the rating system was updated from Elo to Bradley-Terry." / "On May 16, 2025, style control was made the default for text and vision arenas and the offset was adjusted to put the style control leaderboard on the same rating scale as non style control." / "On July 23, 2025, frequency-based re-weighting was implemented."
- 自算口径:每月取最后一次快照,category=overall;"开源"= license 不含 "Proprietary"(含 Kimi K3 license / MIT / Apache 等开权重);g12/g13/g110 = 第1名分 − 第2/3/10名分(按 rating 排序);CI 重叠计数 = rating_upper ≥ 第1名 rating_lower 的模型数(含自身);中美差 = 美国机构最高分 − 中国机构最高分。脚本:scratchpad ts.py / cat.py。
- 换算:BT/Elo 分差 d 对应期望胜率 p = 1/(1+10^(−d/400)):10→51.4%,20→52.9%,30→54.3%,40→55.7%,100→64.0%,140→69.0%。

## 自算结果 A:文本总榜(风格控制,即 2025-05-16 后官网默认)月末快照
| 日期 | #1 | g12 | g110 | 与#1 CI重叠数 | 最强开源(名次) | 闭源−开源 | 美−中 |
|---|---|---|---|---|---|---|---|
| 2024-08-28 | chatgpt-4o-latest | 27.6 | 52.5 | 1 | llama-3.1-405b (6) | 39.1 | 102.0 |
| 2024-12-30 | o1-2024-12-17 | 25.4 | 75.3 | 1 | deepseek-v3 (4) | 53.7 | 53.7 |
| 2025-01-28 | o1-2024-12-17 | 6.2 | 67.9 | 2 | deepseek-r1 (2) | 6.2 | 6.2 |
| 2025-02-27 | o1 | 2.8 | 54.5 | 2 | deepseek-r1 (2) | 2.8 | 2.8 |
| 2025-06-24 | gemini-2.5-pro | 15.9 | 67.3 | 1 | deepseek-r1-0528 (7) | 53.8 | 53.8 |
| 2025-10-17 | gemini-2.5-pro | 4.2 | 16.9 | 4 | glm-4.6 (13) | 29.2 | 16.9 |
| 2025-11-26 | gemini-3-pro | 10.4 | 47.4 | 2 | kimi-k2-thinking-turbo (18) | 61.6 | 59.3 |
| 2026-01-29 | gemini-3-pro | 12.2 | 37.0 | 1 | kimi-k2.5-thinking (12) | 37.7 | 34.7 |
| 2026-02-26 | claude-opus-4-6-thinking | 0.5 | 33.6 | 4 | glm-5 (16) | 48.0 | 33.6 |
| 2026-05-27 | claude-opus-4-6-thinking | 2.5 | 23.1 | 4 | glm-5.1 (16) | 28.3 | 27.4 |
| 2026-07-30 | claude-fable-5 | 2.7 | 21.7 | 4 | kimi-k3-max (11) | 21.8 | 21.8 |
| 2026-08-27 | claude-fable-5 | 2.7 | 18.7 | 4 | kimi-k3-max (10) | 18.7 | 18.7 |
| 2026-09-30 | gemini-4-argon-high | 19.4 | 30.7 | 1 | kimi-k3-max (17) | 36.8 | 36.8 |
| 2026-10-08 | gemini-4-argon-high | 18.3 | 31.4 | 1 | kimi-k3-max (16) | 37.3 | 37.3 |

## 自算结果 B:文本总榜(原始,无风格控制)
- 2026-08-27:#1 claude-opus-5-max 1505,最强开源 kimi-k3-max(第16),闭源−开源 28.7 ← 与媒体"2026-09 扩大到 29 Elo"吻合(媒体用的是原始榜,不是官网默认风格控制榜)
- 同日风格控制榜闭源−开源仅 18.7 ← 与 BenchLM "18.4 by 2026-09-01" 吻合。两数字之差=风格控制口径差。
- 2026-10-08 原始:#1 gemini-4-argon-high 1534,g12=19.0,g110=42.6,最强开源 mimo-v2.6-pro(第9)差 42.2
- 历史:2025-01-28 deepseek-r1 原始榜第1(开源反超 6.5);2025-02-27 仍第1(领先 3.7)

## 自算结果 C:Code Arena WebDev(overall)
| 日期 | #1 | g12 | g110 | 最强开源(名次) | 闭源−开源 |
|---|---|---|---|---|---|
| 2025-11-26 | claude-opus-4-5-thinking | 14.4 | 135.0 | glm-4.6 (9) | 122.8 |
| 2026-01-29 | claude-opus-4-5-thinking | 29.0 | 109.6 | glm-4.7 (5) | 57.1 |
| 2026-04-28 | claude-opus-4-7-thinking | 6.6 | 80.8 | glm-5.1 (5) | 37.1 |
| 2026-06-21 | claude-fable-5 | 60.7 | 124.1 | glm-5.2 max (2) | 60.7 |
| 2026-08-30 | claude-opus-5-max | 14.7 | 80.4 | kimi-k3-max (2) | 14.7 |
| 2026-09-30 | claude-opus-5.5-max | 28.7 | 148.1 | kimi-k3-max (12) | 160.0 |
| 2026-10-08 | claude-opus-5.5-max | 26.9 | 139.5 | kimi-k3-max (14) | 158.7 |

## 自算结果 D:Agent Arena(IPS τ̂,相对基线的处理效应,非 Elo)
- 2026-10-12:#1 Claude Opus 5.5 (Max) 0.179 [0.137,0.221];最强开源 DeepSeek V4.1 Flash (Max) 0.033 [0.029,0.037];比值 5.35x,CI 不重叠
- 时序:比值 2026-06-16 3.43 → 08-12 1.14(Kimi K3 逼近,CI 重叠)→ 09-08 2.20 → 10-02 3.42 → 10-12 5.35
- 注意:τ̂ 相对"均匀基线"计算,字段组成与方法(2026-09-30 Steerability 改版)变化会使同一模型分数漂移(Kimi K3 0.105→0.030),比值不宜做长期趋势。

(论断与一手摘引见下,持续追加)

## 自算结果 E:年度汇总(每次快照,category=overall,2024 起)
| 口径 | 年 | 闭源−开源 最小/中位/最大 | g110 中位 | g12 中位 | 最强开源名次中位 | 美−中 中位 |
|---|---|---|---|---|---|---|
| 原始 text | 2024 | 22.4 / 66.1 / 135.0 | 75.1 | 20.2 | 8 | 80.6 |
| 原始 text | 2025 | −9.1 / 40.3 / 54.0 | 59.6 | 16.2 | 4 | 39.2 |
| 原始 text | 2026(至10-08) | 27.1 / 34.3 / 59.6 | 31.4 | 3.4 | 12 | 28.1 |
| 风格控制 | 2024(8月起) | 10.7 / 48.8 / 75.9 | 52.4 | 17.5 | 8 | 56.4 |
| 风格控制 | 2025 | 2.7 / 43.0 / 70.4 | 54.6 | 10.2 | 7 | 42.3 |
| 风格控制 | 2026 | 17.7 / 35.1 / 57.7 | 26.4 | 2.7 | 16 | 32.2 |
| WebDev | 2025(11月起) | 67.7 / 113.0 / 150.6 | 144.5 | 38.6 | 7 | 113.0 |
| WebDev | 2026 | −8.4 / 60.2 / 166.9 | 121.1 | 17.0 | 5 | 55.0 |
- 开源登顶日期:原始 text 2025-01-24..2025-02-27(deepseek-r1);风格控制榜从未登顶;WebDev 2026-07-26 一次(kimi-k3)。
- 结论:分差(点数)趋同;名次差扩大("small in points, large in rank");前沿新品发布时出现锯齿状重新拉开(2025-11 gemini-3-pro、2026-09 gemini-4-argon / claude-opus-5.5)。

## 自算结果 F:实验室级(每家取最高分)
风格控制榜 #1 实验室 − #5 实验室:2024-12 75.3 → 2025-06 57.6 → 2025-12 42.7 → 2026-03 37.2 → 2026-06 32.7 → 2026-08 23.6 → 2026-10 40.3。
#1 − #10 实验室:96.6 → 121.7 → 75.1 → 59.6 → 47.0 → 39.8 → 50.9。
(按实验室去重是为排除"同一实验室多变体塞满前十"造成的假性拥挤:2026-10-08 风格控制前 10 中 6 个是 Anthropic 变体。)

## 媒体 29 Elo 说法核对
- cryptobriefing 2026-09-03(媒体转述)原文:"As of September 2026, the gap between the best closed frontier models and their top open-weight competitors has ballooned to 29 Elo points, according to Arena AI's evaluation data. Claude Opus 5 Max sits at a rating of 1505"; 副标题称 "by the largest margin in nearly two years"; 并称 "The Elo rating gap on Arena's crowdsourced leaderboard hit zero" (2025-01)。
- 自算核对:数字 28.7 对应原始(非风格控制)榜 2026-08-27 快照(claude-opus-5-max 1505.0 vs kimi-k3-max)——数字可复现;但"近两年最大"不成立:同一原始榜 2026-02-26 差 49.9、2026-03-31 51.1、2025-11-26 45.8。且官网默认的风格控制榜同日只有 18.7。2025-01 并非"归零"而是开源(deepseek-r1)反超 6.5。
- Arena 官方 X(2026-05-07)原话:"In Text Arena, the proprietary winner had a +250 Arena lead. By early 2025, it had fallen to low double digits, and at its narrowest was almost closed entirely. Today, the proprietary lead is about +30 points. It separates #1 from roughly #18 on the current leaderboard." / "The remaining gap is small in points, but still large in rank" — https://x.com/arena/status/2052455463573426452
- 同 thread:"Code Arena: Frontend ... the proprietary lead rose +100 points, then compressed sharply through spring 2026. Today, the lead is around +40 points." / "Expert ... DeepSeek R1 moved ahead briefly in early 2025 ... That lead did not hold. ... Today, the gap is +40 points, roughly the distance from rank #1 to #8."

## 自算结果 G:文本榜困难类目(风格控制)随时间 —— 格式 g110 / 闭源−开源 / 最强开源名次
| 日期 | overall | hard_prompts | coding | math | expert | creative | multi_turn |
|---|---|---|---|---|---|---|---|
| 2024-12-30 | 75.3/53.7/4 | 65.8/46.8/5 | 58.8/37.7/5 | - | - | 70.7/57.2/6 | - |
| 2025-06-24 | 67.3/53.8/7 | 75.0/57.1/6 | 56.6/40.5/6 | 61.9/34.6/3 | - | 71.0/69.5/8 | 69.6/54.2/7 |
| 2025-12-30 | 41.7/51.4/18 | 32.4/51.8/18 | 46.6/59.2/15 | 50.1/51.3/11 | 39.0/54.8/12 | 52.7/82.8/19 | 29.3/29.1/9 |
| 2026-06-25 | 26.9/34.7/19 | 28.2/35.8/17 | 37.4/38.5/12 | 25.6/34.5/14 | 32.2/35.1/11 | 34.4/39.5/16 | 30.9/37.1/14 |
| 2026-08-27 | 18.7/18.7/10 | 21.0/14.8/6 | 21.0/9.3/6 | 33.3/28.3/6 | 24.0/20.8/8 | 33.8/37.5/13 | 19.6/16.6/7 |
| 2026-10-08 | 31.4/37.3/16 | 33.9/33.9/10 | 22.4/22.4/10 | 24.5/26.6/13 | 16.3/17.0/11 | 36.0/58.9/28 | 55.1/53.3/9 |
→ 文本 Arena 内"困难类目"并不比总榜拉得更开(expert/coding/math 的 g110 反而常小于 overall);真正拉开的是 Code Arena WebDev(g110≈140)与 Agent Arena(比值 5x)。

## 自算结果 H:Vision / Search
- Vision(风格控制前的原始 vision 子集)2026-10-09:g12=3.4,g110=10.9,13 个模型 CI 与 #1 重叠 ← 偏好层面最饱和的竞技场
- Search:开源模型几乎缺席(最强开源 diffbot-small-xl 排 33/34,差 234.7),不具可比性

## 自算结果 I:Arena 与 Epoch ECI 的相关(反方/正方证据)
- 方法:Epoch benchmark_data.zip 中 eci_scores.csv(下载于 2026-10-12)与 Arena 风格控制 overall 2026-10-08 快照做名称规范化匹配(去标点小写,前缀匹配,多变体取最高分),匹配 111 个模型
- 全体 Spearman 0.947 / Pearson 0.956;2025-06 之后发布的 70 个 Spearman 0.811;按 ECI 前 30 名 Spearman 0.192;前 15 名 Spearman −0.025
- 解读:Arena 在粗粒度上与能力强相关,但在前沿区间几乎不再区分能力(例:GPT-6 Astra ECI 第2,Arena 1475;Kimi K3 ECI 第12,Arena 1488 高于多数 GPT-6 系列)
- 局限:名称匹配近似;多变体取最高分偏向多变体实验室

## 一手文献摘引
- Singh et al. 2025, The Leaderboard Illusion, arXiv 2504.20879v2 (2025-05-12):
  - "At an extreme, we identify 27 private LLM variants tested by Meta in the lead-up to the Llama-4 release."
  - "Providers like Google and OpenAI have received an estimated 19.2% and 20.4% of all data on the arena, respectively. In contrast, a combined 83 open-weight models have only received an estimated 29.7% of the total data."
  - "even limited additional data can result in relative performance gains of up to 112% on ArenaHard"
  - "out of 243 public models, 205 have been silently deprecated" / "Among the models that are silently deprecated, 64% are open-weight or fully open-source."
  - 同卵实验:"identical checkpoints: 1052 (±21/22) and 1069 (±19/23). As a result, 4 models are positioned between our two identical checkpoints."
  - 模拟:v2 摘要框写 "testing just 10 variants yields a notable increase of approximately 100 points",正文写 "testing just 20 variants yields a notable increase of approximately 50 points"(版本内不一致,引用时须注明是模拟)
- Arena 回应 (arena.ai/blog/our-response, 2025-05-09,更新 2025-06-13):
  - "Official Chatbot Arena stats (published 2025/4/27) show Open Models at 40.9%"
  - "Our analysis shows the effect of pre-release testing is smaller than claimed with finite data (around +11 Elo after 50 tests and 3000 votes) and diminishes to zero as fresh evaluation data accumulates."
  - "any model provider can submit as many public and private variants as they would like, as long as we have capacity for it."
  - "The best models, regardless of provider, are upsampled to improve the user experience."
  - 让步:"we will mark model scores as "provisional" until additional 2,000 fresh votes have been collected after model release, if more than 10 models were pre-release tested in parallel."
- Llama 4 事件(Arena X 2025-04-08,经 Simon Willison 转引):"Meta's interpretation of our policy did not match what we expect from model providers. Meta should have made it clearer that "Llama-4-Maverick-03-26-Experimental" was a customized model to optimize for human preference." 公开版 llama-4-maverick-17b-128e-instruct 在官方数据 2025-04-09 风格控制榜排名第 31。
- 风格控制 (lmsys.org/blog/2024-08-28-style-control, 2024-08-29):length 是 "the dominant style factor";"All other markdown effects are second order";Overall 名次(length+markdown):Claude 3.5 Sonnet 6→4,GPT-4o-mini 6→11,Grok-2-mini 6→18,Llama-3.1-405B 6→6。
- 数据集 README:2025-05-16 风格控制成默认;2025-07-23 频率重加权。changelog 2025-07-23:battles reweighted "inversely proportionally to how frequently they appear",使区间变宽、平局增多(WebFetch 摘要,非逐字)。2026-05-12 BT 加入 same_org_indicator(同组织偏好)特征。
- Chiang et al. 2024, arXiv 2403.04132(ICML 2024):"the crowdsourced human votes are in good agreement with those of expert raters."
- Min et al. 2025 arXiv 2501.17858:"omnipresent rigging strategies can improve model rankings by rigging only hundreds of new votes."
- Huang et al. 2025 arXiv 2501.07493:"an attacker can alter the leaderboard ... at the cost of roughly a thousand votes" ; 识别模型 ">95% accuracy"
- Search Arena, arXiv 2506.05334 (2025-06-05):"user preferences are influenced by the number of citations, even when the cited content does not directly support the attributed claims"

## 本线小结(截至 2026-10-12)
1. 文本 Arena 头部在"分差"上明确趋同:风格控制榜 #1−#10 从 2024-12 的 75 分(#1 对 #10 期望胜率约 60.7%)降到 2026-08 的 19 分(约 52.7%),2026-10 因 gemini-4-argon 回升到 31(约 54.5%);实验室级 #1−#5 从 75 降到 24 再回到 40。锯齿形:新前沿发布拉开,随后被追平。
2. 闭源−开源分差在点数上收窄(风格控制中位 49→43→35),但最强开源名次变差(中位 8→7→16);开源只在原始榜 2025-01/02(DeepSeek-R1)登顶,风格控制榜从未登顶。
3. 媒体"2026-09 扩大到 29 Elo"=原始榜 2026-08-27 快照 28.7,可复现;但"近两年最大"错误(原始榜 2026-03 为 51),且官网默认风格控制榜同日仅 18.7。两套口径相差 10 分,是"扩大/收窄"叙事分歧的来源之一。
4. 文本 Arena 内困难类目(hard/coding/math/expert)并不比总榜拉得更开;真正分化的是 Code Arena WebDev(#1−#10≈140,闭源−开源≈159,2026-10)与 Agent Arena(头部/最强开源 τ̂ 比值 5.4x,CI 不重叠)。WebDev 开源差距时序剧烈震荡(2026-07-26 Kimi K3 登顶 → 2026-10 差 159)。
5. Arena 与 ECI 全样本 Spearman 0.95,但在 ECI 前 15 名内≈0:偏好排行在前沿区间失去能力区分度——支持"用户感知饱和≠能力饱和"。
6. 测量层面的批评(私测多变体、采样不均、静默下线、投票操纵)有一手证据,Arena 方回应称选择偏差 ≈+11 Elo 并随新票趋零;这些偏差量级(10–50 分)与当前头部分差(10–30 分)同量级,足以改变头部排序。
