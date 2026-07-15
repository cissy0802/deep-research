export const meta = {
  name: 'agent-readme-verify-round2',
  description: 'Adversarial 3-vote verification of 10 load-bearing claim groups from research lines 3-7 (empirical evals, llms.txt, security, vendor monorepo docs, production examples)',
  phases: [{ title: 'Verify' }],
}

const VERDICT = {
  type: 'object',
  properties: {
    holds: { type: 'boolean', description: 'true if the claim group survives your refutation attempt' },
    corrections: { type: 'string', description: 'Specific scope/number corrections needed (empty if none). E.g. wrong denominator, misattributed date, narrower population than claimed.' },
    keyEvidence: { type: 'string', description: 'The decisive primary-source evidence you found (verbatim quotes where possible, with URL)' },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
  },
  required: ['holds', 'corrections', 'keyEvidence', 'confidence'],
}

const GROUPS = [
  { id: 'V1', label: 'AGENTbench 对照评测', claim: `arXiv 2602.11988 (ETH Zurich SRI Lab + LogicStar.ai, "Evaluating AGENTS.md"): (a) across multiple coding agents and LLMs, providing repo context files does NOT generally improve task success rates while increasing inference cost by over 20% on average; (b) LLM-generated context files REDUCE average resolution rates ~0.5pp on SWE-bench Lite and ~2-3pp on their AGENTBENCH; (c) developer-written context files give only ~4pp average improvement on AGENTBENCH, mainly where no other docs existed, while increasing steps/cost by ~20% in some setups; (d) methodology = SWE-bench Lite (300 tasks, 11 popular Python repos, LLM-generated files) + AGENTBENCH (138 real PR tasks, 12 niche Python repos with developer-committed files), agents include Claude Code and Codex.` },
  { id: 'V2', label: '遵从率因子实验', claim: `arXiv 2605.10039: factorial study of coding-agent instruction compliance, 1,650 Claude Code CLI sessions / 16,050 function-level observations, 2 TypeScript codebases, 5 tasks; none of 4 structural variables (config file size 25-500 lines, instruction position in file, single vs multi-file/nested architecture, contradictions in adjacent files) nor 3 two-way interactions produced a detectable effect on adherence after multiple-testing correction; size and conflict nulls have affirmative Bayes factors BF10 0.05-0.10; but compliance varied by task and DECAYED within-session across the sequence of generated functions.` },
  { id: 'V3', label: '2303 文件实证', claim: `arXiv 2511.12884 (first large-scale empirical study of agent context files): analyzed 2,303 context files from 1,925 GitHub repos; content analysis over 16 instruction types: implementation details in 69.9% of files, architecture 67.7%, build/run commands 62.3%; non-functional requirements rare: security 14.5%, performance 14.5%; files evolve like configuration code via frequent small additions; study is observational (prevalence, not effectiveness).` },
  { id: 'V4', label: 'Codex 效率对照', claim: `arXiv 2601.20404: controlled with/without-AGENTS.md comparison running OpenAI Codex on 10 repos / 124 GitHub PR tasks; with AGENTS.md: median runtime -28.64% (98.57s → 70.34s), median output tokens -16.58% (2,925 → 2,440), while task completion behavior stayed comparable (efficiency gain, NOT capability gain); hypothesized mechanism = less exploratory navigation; only one agent tested.` },
  { id: 'V5', label: 'Context rot', claim: `Chroma technical report "Context Rot" (July 2025): evaluated 18 frontier LLMs (GPT-4.1, Claude 4, Gemini 2.5, Qwen3 families); performance degrades non-uniformly as input length grows even on simple tasks; LongMemEval: models consistently better with focused prompt (relevant excerpts only) than full ~113k-token history; distractors amplify errors with length; all 18 models performed BETTER on shuffled haystacks than logically coherent ones; argues NIAH overstates long-context ability.` },
  { id: 'V6', label: 'llms.txt 体检', claim: `(a) Ahrefs server-log study (June 2026, ~137,210 domains): 97% of published llms.txt files got ZERO requests in May 2026; adoption grew 8.8x in 12 months to 36,120 instances (38,980 incl. llms-full.txt/ai.txt); of files WITH requests, ~96% of traffic was bots, mostly non-AI; AI retrieval bots (ChatGPT/Perplexity-linked) ~1%. (b) Google's John Mueller stated on Bluesky 2025-06-18 "FWIW no AI system currently uses llms.txt" and later compared it to the keywords meta tag; Gary Illyes confirmed July 2025 Google does not support llms.txt and is not planning to. (c) Contradiction: Chrome Lighthouse agentic-browsing audit checks for llms.txt presence while Google Search says it does not consume it (covered by Search Engine Journal 2026-06-06).` },
  { id: 'V7', label: 'NVIDIA 注入 PoC', claim: `NVIDIA AI Red Team blog "Mitigating indirect AGENTS.md injection attacks" (~April 2026): working PoC where a malicious Golang build-time dependency detects Codex environments via the CODEX_PROXY_CERT env var and writes a crafted AGENTS.md directing Codex to inject a five-minute time.Sleep into Golang main functions, with stealth directives to omit the change from PR descriptions/commit messages/summaries; attack presupposes compromised dependency (supply-chain framing); OpenAI acknowledged the disclosure but declined changes; risk class applies across Cursor .cursorrules and Claude Code CLAUDE.md too.` },
  { id: 'V8', label: 'VS Code 自动注入攻击面', claim: `prompt.security blog "When your repo starts talking": VS Code Chat (Copilot) auto-includes the repo's AGENTS.md into chat requests and treats it as instructions, so typing even a single character triggers injection of repo-defined goals; a malicious AGENTS.md can hijack the agent toward data exfiltration; classified as OWASP ASI01 (Agent Goal Hijack) / ASI02 (Tool Misuse). VERIFY SPECIFICALLY: does VS Code actually auto-include AGENTS.md by default (check VS Code official docs/settings like chat.useAgentsMdFile / github.copilot.chat.codeGeneration.useInstructionFiles), and is the OWASP Agentic Security Initiative taxonomy (ASI01/ASI02) real?` },
  { id: 'V9', label: 'Anthropic 大仓官方口径', claim: `Anthropic official doc code.claude.com/docs/en/large-codebases: (a) loading model = at launch load CLAUDE.md from cwd + every parent dir; subdirectory CLAUDE.md files load on demand when Claude reads files there; (b) for large codebases/monorepos recommends root + per-directory CLAUDE.md split, warning a single root file either bloats context or stays too generic; (c) maintenance guidance: review CLAUDE.md edits in PRs, prune after major model releases, optionally a Stop hook proposing updates from transcripts; (d) acknowledges per-directory layering has governance failure modes (drift, staleness, unowned root) and recommends migrating conventions into on-demand skills/plugins/MCP; (e) claudeMdExcludes setting exists to skip files by path/glob, managed-policy files cannot be excluded. Also verify whether the doc gives a size guideline (e.g. <10k words).` },
  { id: 'V10', label: '生产 repo 逐字核验', claim: `Production AGENTS.md examples: (a) getsentry/sentry AGENTS.md opens by declaring AGENTS.md files "the source of truth for AI agent instructions" and tells agents NOT to add guidance to CLAUDE.md or Cursor rules; (b) cloudflare/workers-sdk AGENTS.md leads development commands with "Use pnpm - never use npm or yarn" (pnpm monorepo lockfile guardrail) and references per-package nested AGENTS.md files; (c) apache/airflow enforces prose rule "Write Dag (title case) in all prose" and forbids running pytest directly on host; (d) coder/coder sets a Rule #1 requiring explicit permission before breaking any rule and bans sycophantic phrasing. Verify against the live GitHub files (fetch raw.githubusercontent.com or github.com).` },
]

phase('Verify')
log(`Verifying ${GROUPS.length} claim groups × 3 adversarial votes`)

const LENSES = [
  'numbers-and-denominators: re-derive every number, check denominators, populations, units, and whether the claimed figure is the headline figure or a subgroup/corrected figure',
  'source-and-attribution: confirm the source actually exists, says this (verbatim where possible), the date and author attribution are right, and the claim is not a misreading of a secondary summary',
  'scope-and-overclaim: check whether the claim generalizes beyond what the source supports (models/agents/languages tested, observational vs causal, vendor narrative vs independent evidence)',
]

const results = await pipeline(
  GROUPS,
  g => parallel(LENSES.map((lens, i) => () =>
    agent(
`You are an adversarial verifier. Your job is to REFUTE the following claim group if possible. Default to skepticism: if you cannot locate primary-source support, say holds=false or record corrections.

Lens for this vote: ${lens}

## Claim group ${g.id} (${g.label})
${g.claim}

## Method
1. Fetch the PRIMARY source(s) named in the claim (use WebFetch; for arXiv try both /abs/ and /html/ URLs; for GitHub files fetch raw.githubusercontent.com). If a page 403s, use WebSearch with exact-phrase queries and corroborate via at least two independent mirrors/citations — and say so in keyEvidence.
2. Check the claim through your lens. Hunt for: wrong numbers, wrong denominators, misattributed dates/authors, overgeneralization, vendor narrative presented as independent finding.
3. Report holds (survives) or not, with specific corrections. A claim can hold WITH corrections — record every needed correction precisely.

Your final output goes through the StructuredOutput schema. Be precise and terse; quote verbatim where it matters.`,
      { label: `verify:${g.id}:lens${i+1}`, phase: 'Verify', schema: VERDICT }
    )
  )).then(votes => ({ id: g.id, label: g.label, claim: g.claim, votes }))
)

const out = results.filter(Boolean).map(r => {
  const votes = (r.votes || []).filter(Boolean)
  const holdCount = votes.filter(v => v.holds).length
  return { id: r.id, label: r.label, holdCount, total: votes.length, votes }
})
return { groups: out }