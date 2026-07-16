export const meta = {
  name: 'agent-readme-verify-round3',
  description: 'Round 3: dedicated contradiction-search seat + methodology-audit seat for the 6 single-source load-bearing claim groups',
  phases: [{ title: 'Contradict' }, { title: 'Audit' }],
}

const CONTRA_SCHEMA = {
  type: 'object',
  properties: {
    independentCorroborations: { type: 'array', items: { type: 'object', properties: {
      source: { type: 'string' }, whatItShows: { type: 'string' },
      independent: { type: 'boolean', description: 'true only if different team AND different data/measurement — merely citing the original does NOT count' } },
      required: ['source', 'whatItShows', 'independent'] } },
    contradictions: { type: 'array', items: { type: 'object', properties: {
      source: { type: 'string' }, whatItContradicts: { type: 'string' }, strength: { type: 'string', enum: ['direct-measurement', 'indirect', 'opinion'] } },
      required: ['source', 'whatItContradicts', 'strength'] } },
    anglesSearched: { type: 'array', items: { type: 'string' }, description: 'every search angle you tried, including the ones that found nothing' },
    verdict: { type: 'string', enum: ['contradicted', 'independently-corroborated', 'single-source-unchallenged'] },
    notes: { type: 'string' },
  },
  required: ['independentCorroborations', 'contradictions', 'anglesSearched', 'verdict', 'notes'],
}

const AUDIT_SCHEMA = {
  type: 'object',
  properties: {
    fatalFlaws: { type: 'array', items: { type: 'string' }, description: 'methodological problems that invalidate the load-bearing number as evidence' },
    nonFatalCaveats: { type: 'array', items: { type: 'string' } },
    survivesAsEvidence: { type: 'boolean' },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
    notes: { type: 'string' },
  },
  required: ['fatalFlaws', 'nonFatalCaveats', 'survivesAsEvidence', 'confidence', 'notes'],
}

const GROUPS = [
  { id: 'G1', label: 'AGENTbench 成功率', finding: `arXiv 2602.11988 (Gloaguen et al., ETH Zurich/LogicStar.ai, Feb 2026, "Evaluating AGENTS.md"): repo context files tend to reduce coding-agent task success rates vs no context while raising inference cost >20%; LLM-generated files -0.5pp (SWE-bench Lite) / -2pp (their AGENTbench); developer-written +4% avg (all agents except Claude Code); ablation: with README/docs removed, LLM-generated files flip to +2.7%.` },
  { id: 'G2', label: 'Codex 效率', finding: `arXiv 2601.20404 (Lulla et al., JAWs@ICSE 2026): paired with/without-AGENTS.md runs of OpenAI Codex (gpt-5.2-codex) on 10 repos/124 PRs: median runtime 98.57s→70.34s (-28.64%), median output tokens 2,925→2,440 (-16.58%), comparable task completion.` },
  { id: 'G3', label: '遵从率因子实验', finding: `arXiv 2605.10039 (Damon McMillan, May 2026): factorial study, 1,650 Claude Code sessions/16,050 function observations: file size (25-500 lines), instruction position, single-vs-nested architecture, and contradictions show no detectable effect on compliance after correction (size & conflict = affirmative Bayesian nulls BF10 0.05-0.10); task identity dominates; within-session decay ~5.6% lower odds per function (OR=0.944).` },
  { id: 'G4', label: '2303 文件普查', finding: `arXiv 2511.12884 ("Agent READMEs", Nov 2025): census of 2,303 context files from 1,925 repos: implementation details 69.9%, architecture 67.7%, build/run commands 62.3%; security 14.5%, performance 14.5%; files evolve like configuration code via frequent small additions.` },
  { id: 'G5', label: 'Context rot', finding: `Chroma technical report (Hong, Troynikov & Huber, 2025-07-14): 18 LLMs; performance degrades non-uniformly with input length even on simple tasks; focused ~300-token prompts consistently beat the same info embedded in ~113k-token full histories (LongMemEval_s cleaned 306-prompt subset); distractors amplify degradation with length.` },
  { id: 'G6', label: 'llms.txt 零消费', finding: `Ahrefs server-log study (June 2026, 137,210-domain panel): 97% of ~38k domains with a valid llms.txt received zero requests for it in May 2026; of requests that occurred, 96% were bots, AI retrieval bots only ~1.1%.` },
]

phase('Contradict')
log('Seat A: independent contradiction/corroboration search, 6 groups')
const contra = await pipeline(
  GROUPS,
  g => agent(
`You are a contradiction hunter. Your ONLY task: search the world for independent evidence AGAINST or independently FOR the following published finding. Do NOT re-verify that the source says this (already done). "Independent" means a different team AND different data/measurement — a blog post citing the original paper does NOT count as corroboration.

## Finding (${g.id} ${g.label})
${g.finding}

## Method
1. Search at least 5 distinct angles: (a) replications or follow-up studies; (b) studies measuring the same construct with different setups (other agents/languages/benchmarks); (c) practitioner-reported measurements (engineering blogs WITH numbers, not opinions); (d) critiques/rebuttals of this specific work (reviews, HN/X threads by domain experts, OpenReview); (e) older or adjacent literature that already measured this construct.
2. For every angle, record what you searched even if nothing was found — absence-of-contradiction is only meaningful if the search was real.
3. Verdict: 'contradicted' if any direct-measurement contradiction exists; 'independently-corroborated' if ≥1 truly independent measurement agrees; else 'single-source-unchallenged'.
Time base: 2026-07. Be precise; cite URLs.`,
    { label: `contra:${g.id}`, phase: 'Contradict', schema: CONTRA_SCHEMA }
  ).then(r => ({ id: g.id, label: g.label, seat: 'contradiction', result: r }))
)

phase('Audit')
log('Seat B: methodology audit with kill authority, 6 groups')
const audit = await pipeline(
  GROUPS,
  g => agent(
`You are a hostile methods reviewer with kill authority. Your ONLY task: attack the methodology of the study behind this finding, as if reviewing for a top venue with a reject-by-default policy. Do NOT check whether the source says this (already done). Attack: sampling and denominators; dependent-variable validity (does the measured thing actually operationalize the claimed construct?); benchmark provenance (author-built? contaminated?); statistical practice (power, multiple testing, exploratory-vs-confirmatory); conflicts of interest; and the gap between what was measured and how the finding is being quoted.

## Finding (${g.id} ${g.label})
${g.finding}

## Method
Fetch the primary source if reachable (arXiv often 403s through this proxy — then reconstruct the methodology from multiple independent mirrors/summaries and say so). List fatal flaws (invalidate the number as evidence) separately from non-fatal caveats. Then rule: does the load-bearing number survive as evidence? A finding can be real-but-weak: survivesAsEvidence=true with heavy caveats is a legitimate verdict; so is false-precision → survivesAsEvidence=false.
Time base: 2026-07. Be specific.`,
    { label: `audit:${g.id}`, phase: 'Audit', schema: AUDIT_SCHEMA }
  ).then(r => ({ id: g.id, label: g.label, seat: 'methods-audit', result: r }))
)

return { contra: contra.filter(Boolean), audit: audit.filter(Boolean) }