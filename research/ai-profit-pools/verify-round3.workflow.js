export const meta = {
  name: 'profit-pools-round3',
  description: 'Round 3: 3 条单源承重实证 × 反证搜索席/方法学审计席',
  phases: [{ title: 'Audit', detail: '3 条 × 2 席' }],
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
    method_issues: { type: 'array', items: { type: 'string' }, description: '方法学席:样本量/推断/选样/利益冲突等问题' },
    usable_statement: { type: 'string', description: '经审计后可以写进文章的最强表述(中文)' },
  },
}

const CTX = '文章:「AI 价值链的利润池会落在哪一层?」(截至 2026 年 10 月,今天 2026-10-05)。下面是一条只有单一来源支撑、且文章结论压在上面的实证。\n\n'

const SEATS = {
  counter: '你是**反证搜索席**。任务:主动搜索独立团队+独立数据对同一问题的测量——矛盾的和证实的都要。记录全部搜索角度(包括没搜到结果的)。判断这条实证能否升级为多源证实、维持单源、还是方向存争。用 WebSearch/WebFetch,一手优先。',
  method: '你是**方法学审计席**,敌意审稿,有否决权。任务:读原始来源的方法部分,审查样本量、模型假设、参数敏感性(换一个合理假设结论还在不在)、选样程序、数据来源、利益冲突。你可以判「否决(不得承重)」——被否决的数字不得承重,只能降级为弱结论或弃用。用 WebFetch 读原文。',
}

const CLAIMS = [
  { key: 'R1-energy-tco', body: `【R1】Epoch AI(2026-05-14,"AI datacenter cost breakdown",https://epoch.ai/data-insights/ai-datacenter-cost-breakdown):1 GW GB200 数据中心前期 capex 约 $38B,年 opex 约 $0.9B;年化 TCO 约 $8.5B,其中服务器约 $5B(约 60%),能源仅约 $0.6B(约 7%,电价 8.34 美分/kWh);IT 设备寿命按 3 年算年化 TCO 升到约 $12B,按 7 年降到约 $7B。
文章用它承重的结论:「电力层是持久的稀缺点,但能拿走的租金薄——电费只占 AI 数据中心总成本的个位数百分比,GPU 寿命假设对成本的影响远大于电价;电力卖方拿到的是『接入速度』的稀缺租金,量级远小于芯片层。」请检验:电力/能源占 AI 数据中心 TCO 的比例,是否有其他独立测算(SemiAnalysis、IEA、LBNL、Uptime、学术论文、电力公司披露)给出相近或矛盾的数字;若电价翻倍或用 PJM 容量价上涨后的电价,结论是否仍成立;"电力租金薄"是否忽略了"没电就没法开机"的影子价格(接入延误的机会成本)。` },
  { key: 'R2-price-curves', body: `【R2】Epoch AI(2026-09-22,"The plunging price of thought",https://epoch.ai/publications/the-plunging-price-of-thought):达到给定性能的成本自 2023 年起每季度降约 47%(约 13×/年);刚成为 SOTA 时降得最快(约 66%/季),两年后降速减半(约 32%/季);新能力可以短暂收溢价。配合 MIT FutureTech 预印本(arXiv 2511.23455):给定性能价格年降 5-10×,但运行前沿级模型的成本年升 3-18×;以及 OpenAI 官方旗舰 API 价逐代上调(GPT-5 $1.25/$10 → gpt-5.5 $5/$30)。
文章用它承重的结论:「存在两条方向相反的价格曲线——固定能力的价格每年降约一个数量级(商品化叙事说的是这条),前沿的价格不降反升(前沿溢价叙事说的是这条);两派争论其实在描述不同的曲线。」请检验:各测算的方法(用哪些基准、价格取最低价还是平均价、是否只看 API 标价而忽略 token 用量/推理长度变化);是否有独立测算(a16z、Artificial Analysis、OpenRouter、学术)矛盾;「前沿价格上升」是否只是 OpenAI 一家的定价选择(Anthropic/Google 的旗舰价时序如何);"每 token 价格"与"每任务成本"是否方向不同(推理模型 token 数暴增)。` },
  { key: 'R3-lab-revenue-crossover', body: `【R3】WSJ(2026-08 报道,经 Yahoo Finance 转载)与泄露的 Anthropic 保密 S-1(Fortune 2026-09-29 等):Anthropic 2026Q2 确认收入约 $11.5-11.6B,OpenAI 2026Q2 确认收入约 $6.7B——Anthropic 季度确认收入首次超过 OpenAI;Anthropic 称连续两个季度 adjusted 经营利润为正(FT 2026-09),而 OpenAI Q2 经营亏损约 $12.3B(含 SBC)。
文章用它承重的结论:「模型层内部已经分化——利润(哪怕只是 adjusted 口径)集中在头部一家,『模型层整体给人做嫁衣』的说法需要按公司拆开看。」请检验:这些数字是否有第二个独立来源(不同媒体各自看到文件,而不是互相转载);收入确认口径差异(Anthropic 是否按总额确认、经云渠道的收入是否含云厂商分成;OpenAI 是否按净额确认微软分成)是否足以解释「超越」;泄露 S-1 数字与 Anthropic 官方 run-rate 是否一致;是否有矛盾报道(如 OpenAI 方面的反驳、The Information 不同数字)。注意利益冲突:泄露方、投资方。` },
]

phase('Audit')
const jobs = []
for (const c of CLAIMS) for (const s of ['counter', 'method']) {
  jobs.push(() => agent(CTX + SEATS[s] + '\n\n' + c.body, { label: `${c.key}-${s}`, phase: 'Audit', schema: SCHEMA, model: 'opus' })
    .then(r => r ? { ...r, claim: c.key, seat: s } : null))
}
return (await parallel(jobs)).filter(Boolean)
