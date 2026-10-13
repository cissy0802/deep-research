export const meta = {
  name: 'convergence-round3',
  description: 'Round 3: 4 条单源承重实证 × 反证搜索席/方法学审计席',
  phases: [{ title: 'Audit', detail: '4 条 × 2 席' }],
}

const SCHEMA = {
  type: 'object',
  required: ['claim', 'seat', 'verdict', 'reasoning', 'usable_statement'],
  properties: {
    claim: { type: 'string' },
    seat: { type: 'string' },
    verdict: { type: 'string', description: '升级多源 | 维持单源 | 方向存争 | 降级为弱结论 | 否决(不得承重)' },
    reasoning: { type: 'string' },
    search_angles: { type: 'array', items: { type: 'string' }, description: '反证席:全部搜索角度,包括没搜到的' },
    independent_measurements: { type: 'array', items: { type: 'string' }, description: '找到的独立测量(来源 URL + 数字 + 是否同向)' },
    method_issues: { type: 'array', items: { type: 'string' }, description: '方法学席:样本量/推断/选样/拟合假设/利益冲突等问题' },
    usable_statement: { type: 'string', description: '经审计后可以写进文章的最强表述(中文)' },
  },
}

const CTX = '文章:「AI 能力最终会趋同是真的吗」(截至 2026 年 10 月,今天 2026-10-12)。下面是一条只有单一来源(或单一数据集上的自算)支撑、且文章结论压在上面的实证。原始数据可下载:Epoch https://epoch.ai/data/benchmark_data.zip(eci_scores.csv、eci_bootstraps.json);Arena HF 数据集 lmarena-ai/leaderboard-dataset;METR https://metr.org/assets/benchmark_results_1_1.yaml 与 github.com/METR/eval-analysis-public。可用 Bash curl + python 复算。\n\n'

const SEATS = {
  counter: '你是**反证搜索席**。任务:主动搜索独立团队+独立数据对同一问题的测量——矛盾的和证实的都要。记录全部搜索角度(包括没搜到结果的)。判断这条实证能否升级为多源证实、维持单源、还是方向存争。一手优先。',
  method: '你是**方法学审计席**,敌意审稿,有否决权。任务:读原始来源的方法/数据,审查样本量、拟合假设、参数敏感性(换一个合理假设结论还在不在)、选样与覆盖偏差、数据版本漂移、利益冲突;必要时下载数据做敏感性复算。你可以判「否决(不得承重)」——被否决的结论不得承重,只能降级为弱结论或弃用。',
}

const CLAIMS = [
  { key: 'R1-eci-gap-widening', body: `【R1】基于 Epoch ECI(2026-10 版 eci_scores.csv)的自算:最强闭源与最强开源的 ECI 分差从 2025 年的约 5–6 点扩大到 2026 年的约 9–11 点(2026-10:Claude Opus 5.5 167.33 vs Kimi K3 157.45,CI 不重叠);闭源前沿年增量 +14.5 → +17.1,开源前沿 +16.0 → +12.4;而追平月数大致稳定在 4–8 个月(Epoch 官方:2025 年约 3–3.5 个月,2026 年约 4 个月)。
文章用它承重的结论:「在跨基准合成量尺上,2026 年开源与闭源的差距没有收窄:分差扩大约一倍,追平月数大致持平或略增——"差距只剩几个百分点"的印象来自饱和考卷与偏好榜。」请检验:ECI 重拟合漂移(5 月 Epoch 发布 4 个月/8 点 vs 10 月数据复算 5.9 个月/9.8 点)是否足以让"扩大"成为伪影;选择不同的开源定义/是否计入中国闭源模型/是否只取 Epoch 打过分的模型(Google 最新 Pro 级未打分,Epoch 开源条目覆盖不全)会不会改变方向;ECI 本身是否偏向闭源实验室常跑的基准;独立指数(Artificial Analysis、LiveBench、CAISI、Ihle、Scale)是否同向。` },
  { key: 'R2-metr-open-lag', body: `【R2】基于 METR TH1.0 原始 runs 的自算:开源模型在 time horizon 曲线上追平闭源前沿的滞后,从 DeepSeek-R1(2025-01)的约 3.4 个月拉长到 R1-0528 约 6.8、gpt-oss-120b 约 7.2、Kimi K2 Thinking(2025-11)约 8.2 个月;同时 METR 官方在 2025-02 称开源"on par with state-of-the-art models from 6 months ago"、2025-06 称 mid-2025 DeepSeek ≈ late-2024 前沿;且 METR 从未在 TH1.1 上测开源、2026 年无开源数据。
文章用它承重的结论:「在最直接测量长任务的量尺上,2025 年内开源的滞后在拉长而不是缩短;2026 年这一量尺对开源是空白。」请检验:样本只有约 5 个开源模型、CI 很宽,8.2 vs 3.4 的差异是否统计上可区分;R1 是否是异常点(选样);METR 对开源模型的 elicitation 投入(约一个工作日)是否系统性低估开源;其他长程量尺(Terminal-Bench 同 harness 约 3 个月、AISI cyber 6–10 → 4–7 个月收窄、Vending-Bench 111 天、APEX-Agents 约 5 个月、CAISI 8 个月)是否与之矛盾。` },
  { key: 'R3-arena-perception', body: `【R3】基于 Arena 风格控制榜(2026-10-08)与 Epoch ECI(2026-10)的自算:全体 111 个匹配模型 Spearman 0.947,但在 ECI 前 15 名内约为 −0.025、前 30 名 0.192;Opus 4.6(2026-02)与 Opus 5.5 CI 重叠;Kimi K3 排在 ECI 高约 9 点的 GPT-6.1 Sol 之上;Arena 困难类目(hard_prompts/expert/coding)的头部分差不比 overall 大。
文章用它承重的结论:「偏好排行榜在前沿区间已经失去区分能力——它的收敛反映的是"用户在日常提示上分不出来"(用户感知饱和),不是能力收敛。」请检验:名称近似匹配与"多变体取最高分"的误差;前 15 名范围受限(restriction of range)本身会把任何相关系数压向 0——这是否让"≈0"失去意义(对照:ECI 与其他独立量尺在前 15 名内的相关是多少?);是否有独立研究(如 Arena 与 SWE-bench/GPQA/LiveBench 相关性研究、"Arena 是否测能力"的论文)证实或反驳;风格控制本身是否改变结论。` },
  { key: 'R4-caisi-8months', body: `【R4】NIST CAISI(2026-05-01)称 DeepSeek V4 Pro 落后美国前沿约 8 个月(≈GPT-5),而按 DeepSeek 自报数据只落后约 2 个月;CAISI 用 IRT 综合 16 个基准、35 个模型,含非公开基准(PortBench、CTF-Archive-Diamond 等),分项上饱和题几乎持平、私有 agentic/网络安全题差 30+pp。
文章用它承重的结论:「厂商自报与独立评测给出的追赶速度可以相差数倍(2 个月 vs 8 个月),差额集中在私有、智能体类题目——公开基准上的"追平"部分来自对公开考卷的针对性优化。」请检验:CAISI 的利益位置(执行美国 AI Action Plan、由商务部长政治定调)与方法透明度(私有基准不可复现);是否有独立评测(Epoch ECI、Artificial Analysis、UK AISI、Ihle、Scale SEAL)对 DeepSeek V4 Pro 给出接近 2 个月还是 8 个月;Epoch 自述"open-weight models tend to perform worse on private benchmarks"的证据基础;"针对性优化公开考卷"是否有直接证据还是推测。` },
]

phase('Audit')
const jobs = []
for (const c of CLAIMS) for (const s of ['counter', 'method']) {
  jobs.push(() => agent(CTX + SEATS[s] + '\n\n' + c.body, { label: `${c.key}-${s}`, phase: 'Audit', schema: SCHEMA, model: 'opus' })
    .then(r => r ? { ...r, claim: c.key, seat: s } : null))
}
return (await parallel(jobs)).filter(Boolean)
