# The README for Agents: Are Context Files Infrastructure or Cargo Cult? (Deep Dive)

> Evidence in this essay is graded. Across two adversarial-verification rounds, 35 load-bearing claim groups were each challenged by 3 independent verifiers (verbatim checks against primary sources, re-derived arithmetic, active search for counter-evidence): 0 of 105 votes overturned a group, and 30+ scope corrections were applied — including the exposure of one widely circulated pseudo-citation (no official document says "keep CLAUDE.md under 10k words"; the real vendor figure, on a different page, is "under 200 lines"). Vendor claims and independent evidence are labeled separately throughout; citations that did not pass through verification are tagged 【unverified, source】. A source index closes the essay.

## 0. An obviously-correct sentence, and three facts that refuse to cooperate

Through 2025 and 2026, every coding-agent vendor has been telling you the same thing: give your repository a "README for agents" — AGENTS.md, CLAUDE.md, `.cursor/rules`, `copilot-instructions.md`; different names, same logic. An agent enters your codebase cold every session; write down the build commands, the directory map, and the house rules, and it stops wasting time rediscovering them. The logic sounds so obviously correct that "your repo still has no AGENTS.md?" has become a new flavor of technical shaming.

Adversarial verification turned up three facts that refuse to cooperate:

**First, the only multi-agent controlled evaluation to date finds that context files do not generally improve task success rates — while raising inference cost by more than 20% on average.** Researchers from ETH Zurich and LogicStar.ai ran three agents (Claude Code, Codex, Qwen Code) on 438 real tasks; the paper's own words: "context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%." 【verified】

**Second, the folk wisdom about *how* to write these files — keep them short, put key instructions at the top — failed its first randomized test across the board.** In a factorial experiment spanning 1,650 Claude Code sessions, none of four structural variables — file size, instruction position, single-file vs. nested architecture, contradictions between adjacent files — had any detectable effect on agent compliance. 【verified】

**Third, the loudest adjacent standard, llms.txt, has a measured consumption rate of approximately zero.** Ahrefs' server-log analysis of 137,210 domains found that 97% of published llms.txt files received not a single request in May 2026. 【verified】

None of this means context files are useless — the essay will get to where they demonstrably help (efficiency, not capability) and to production-grade files that survive verbatim verification. But it does mean this: nearly all "best practice" in this field is vendor narrative, the independent evidence is brand new, and where it exists it does not always point the same way the vendors do. The standing rule from [When Code Gets Cheap](https://cissy0802.github.io/deep-research/ai-native-deep.en.html) applies: a number without a control group gets its denominator checked before it gets quoted.

## 1. How to read the numbers: three evidence tiers, four standing caveats

Every load-bearing claim below carries a grade:

- **【vendor】**: official docs and blogs from Anthropic, OpenAI, GitHub, Cursor. Authoritative for what the tools actually *do* (loading mechanics, truncation caps); their claims about *effects* ("bloated files cause ignored instructions") ship without a control group, every time.
- **【independent】**: the first controlled studies, all appearing between 2025-11 and 2026-05. All preprints, none peer-reviewed, all narrow in scope (mostly Python, single agent or single vendor ecosystem). The scope limits matter as much as the point estimates.
- **【field】**: real context files in production repositories; every quote was checked verbatim against the live GitHub file.

Four standing caveats: (1) this field moves fast — everything is stated as of 2026-07-15; (2) the controlled studies are not inter-convertible (different task sets, agents, metrics); (3) two conflict-of-interest declarations: Chroma (the context-rot report) is a vector-database company whose product story benefits from "curated context beats long context," and the AGENTbench paper's co-authors include the commercial agent-evaluation startup LogicStar.ai; (4) "context files" here means in-repo instruction files for coding agents — llms.txt (a website-facing convention) gets its own section precisely because the two keep getting conflated.

## 2. The standards war: AGENTS.md wins on facts, but recognition is asymmetric

**The spec itself is almost contentless by design: plain Markdown, no required fields, no schema — officially a "README for agents."** It began as an OpenAI-led, multi-vendor effort (Codex, Amp, Google Jules, Cursor, Factory) and moved in December 2025 to neutral hosting under the Linux Foundation's newly formed Agentic AI Foundation, a founding project alongside MCP and goose. 【verified】 "Cross-vendor" is the official framing; independent coverage reads it as "OpenAI-led, then donated." Both are true, depending on whether you read the charter or the commit history.

**Adoption has a checkable but loose denominator.** The official site claims "used by over 60k open-source projects" and links a GitHub search you can re-run yourself. Our verifiers re-ran it: the query executes, but it path-substring-matches (files inside directories *named* `agents.md/` get counted) and counts files, not projects. For calibration, InfoQ's August 2025 figure was 20k repositories. 【verified】 The growth is real; the precise number is a marketing denominator.

**The nesting rule is the most substantive part of the standard: the AGENTS.md closest to the edited file wins, and explicit user chat instructions override everything.** Monorepos are told to put one file per package; the site cites "the main OpenAI repo has 88 AGENTS.md files" as proof of practice (a self-reported number for a private repo — unauditable). Note that the precedence rule lives in the website FAQ, not in formal spec text, and actual behavior is implementation-dependent — not every tool auto-loads nested files. 【verified】

**Mutual recognition is asymmetric; the symlink remains the only reliable interop mechanism.** Checked tool by tool (docs plus source code):

- **GitHub Copilot / VS Code**: consumes AGENTS.md natively (multiple nested files, closest wins), and the docs link agents.md as the standard's home; also accepts a root CLAUDE.md or GEMINI.md as substitutes. VS Code ships this **on by default** since v1.104 (September 2025), governed by `chat.useAgentsMdFile`. 【verified】
- **Cursor**: native AGENTS.md support including nested files; the legacy `.cursorrules` is officially deprecated. 【verified】
- **OpenAI Codex**: source code confirms it reads only `AGENTS.override.md` and `AGENTS.md` by default; making it read CLAUDE.md requires the user-level `project_doc_fallback_filenames` setting — which does not travel with the repo, so you cannot configure it on your users' behalf. 【verified】
- **Claude Code**: a separate system reading layered CLAUDE.md files; this research round found no evidence of official AGENTS.md consumption by Anthropic. 【verified】

The official migration path is rename-plus-symlink: `mv CLAUDE.md AGENTS.md && ln -s AGENTS.md CLAUDE.md`; Aider and Gemini CLI interoperate via their own config options. 【verified】 Convergence is real, but "one file everywhere" is achieved with filesystem tricks, not with standards recognition.

## 3. The vendor guides, reconciled: three points of consensus, zero control groups

Put the official best-practice pages of Anthropic, OpenAI, GitHub, and Cursor side by side and the consensus is striking — strikingly uniform, which should itself raise an eyebrow, because none of the four attaches a controlled experiment.

**Consensus one: keep it short.** The four differ in rhetoric and enforcement. Anthropic is loudest — the docs say verbatim: "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!", and recommend interrogating every line with "would removing this cause an error?" The official size figure lives on the memory page: "target under 200 lines per CLAUDE.md file" — the "under 10k words" figure circulating online does not exist in any official document. OpenAI Codex enforces by mechanism: all project docs share a default hard cap of 32 KiB (source constant `DEFAULT_PROJECT_DOC_MAX_BYTES = 32 * 1024`), silently truncated beyond that, with real GitHub issues from users who found out the hard way. GitHub's auto-generation prompt hard-requires "no longer than 2 pages." Cursor recommends under 500 lines per rule. 【verified】

**Consensus two: executable commands first.** GitHub officially analyzed 2,500+ public agents.md files and distilled six core areas — commands, testing, project structure, code style, git workflow, boundaries — with the advice to put fully-flagged executable commands in an early section (not just tool names) and to phrase boundaries as always do / ask first / never do. This is the largest public pattern analysis available, but GitHub published no methodology or dataset, and parts of the article concern Copilot custom agents rather than plain root files — grade it as vendor pattern-mining, not a controlled result. GitHub's official prompt for auto-generating copilot-instructions adds one genuinely good requirement: every build/test/lint command must be validated by actually running it before it is written down. 【verified】

**Consensus three: nested files for monorepos, closest file wins.** All four agree on the semantics (see §2). Anthropic's version: at launch, Claude Code loads the CLAUDE.md from the working directory and every parent; subdirectory files load on demand when files there are read. For large codebases the recommendation is a two-level split — root file for repo-wide rules, per-directory files for local conventions — with an explicit warning that a single root file "tends to either grow to cover every subsystem's conventions, costing context on instructions unrelated to the current task, or stay too generic to be useful." 【verified】

The divergence is mechanical: Cursor rules carry glob/always-apply metadata while AGENTS.md has no schema; Copilot distinguishes three file types; Codex enforces brevity in bytes while others advise it; and Anthropic alone offers an exit ramp — migrate conventions out of always-loaded CLAUDE.md into on-demand skills and plugins, candidly admitting that per-directory files at scale suffer governance failure: "conventions drift, files go stale, and no one owns the root." 【verified】

Anthropic's content checklist deserves its own record, since it answers *what* to write rather than just *how much*: include what the agent cannot guess — bash commands, non-default code style, test instructions, repo etiquette, project-specific architecture decisions; exclude what code inspection reveals, detailed API docs, and anything that changes frequently. Emphasis markers like IMPORTANT / YOU MUST may raise adherence — a claim, once again, shipped without data. 【verified, vendor】

## 4. The evidence, part I: does writing one actually help? Capability no, efficiency yes

The first half of 2026 produced two controlled studies that answer "does it help?" head-on, and read together they are genuinely informative: **a context file does not let an agent succeed at tasks it would otherwise fail; it lets the agent succeed faster and cheaper at tasks it would have completed anyway.**

**Success-rate side: the AGENTbench comparison (arXiv 2602.11988, ETH Zurich + LogicStar.ai, Feb 2026).** The authors combine SWE-bench Lite (300 tasks, 11 popular Python repos, LLM-generated context files) with their own AGENTbench (138 real PR tasks from 12 niche Python repos, all carrying developer-committed context files, filtered from 5,694 PRs; unrelated to the 2023 Tsinghua benchmark of the same name). Three agents, four model configurations: Claude Code + Sonnet 4.5, Codex + GPT-5.2 and GPT-5.1-mini, Qwen Code + Qwen3-30B. Findings:

- LLM-generated context files **reduce** resolution rates across the board: −0.5pp on SWE-bench Lite and −2pp on AGENTbench on average (−3 in the worst configuration), while pushing cost up 20–23%. 【verified】
- Developer-written files yield only marginal gains: +4% on average, and **for every agent except Claude Code** — which got nothing even from hand-written files; the price is +3.34 steps on average and up to +19% cost. 【verified】
- The most explanatory result is the ablation: delete the repo's README and docs, and LLM-generated context files flip to a **positive** effect (+2.7%), even outperforming developer-written ones. The authors' reading: a context file's value comes from **non-redundant information** — when it paraphrases the README it is pure overhead; when it is the only documentation, it is a map. 【verified】

Scope limits: all-Python, unreviewed preprint, authors' own benchmark, commercial co-affiliation. But the directional conclusions — don't expect success-rate jumps; don't bulk-generate context files on already-documented repos — hold across both benchmarks and all models tested.

**Efficiency side: the paired Codex experiment (arXiv 2601.20404, Lulla et al., JAWs@ICSE 2026).** Ten repositories, 124 real PR tasks, each executed twice — with and without AGENTS.md. With the file: median completion time fell from 98.57s to 70.34s (**−28.64%**), median output tokens from 2,925 to 2,440 (**−16.58%**), with comparable task-completion behavior. Hypothesized mechanism: less exploratory navigation to infer project structure. Secondary analysis shows the mean-level savings (~−20%) concentrate in a few runs that would otherwise have thrashed — the file acts as a guardrail against worst cases, not a uniform accelerator. 【verified】 Scope: one agent (gpt-5.2-codex), small PRs (<100 changed lines, ≤5 files), single root-level files, and the authors themselves phrase the result associationally.

Read together: **the demonstrated benefit of context files is time and tokens, not a higher capability ceiling.** Which also explains the vendor enthusiasm — for token-billed services and waiting users, −28% wall-clock and −17% tokens already justify the file. No capability myth required.

## 5. The evidence, part II: the how-to-write folk wisdom meets its first controlled test, and loses

On *how* to write the file, vendors and practitioners share a folklore: short, key items first, don't over-split, never contradict yourself. In May 2026 a factorial experiment (arXiv 2605.10039, Damon McMillan, single-author preprint) finally put those variables on the table: 1,650 Claude Code CLI sessions, 16,050 function-level observations, two TypeScript codebases, five tasks, primarily Sonnet 4.6, measuring compliance with one simple annotation instruction.

The results are uncomfortable for both camps:

- **None of the four structural variables — file size (25/100/250/500 lines), instruction position (five levels), single vs. multi-file/nested architecture, contradictions in adjacent files — produced a detectable effect after multiple-testing correction; neither did any of three two-way interactions.** The size and conflict nulls carry affirmative Bayes factors (BF10 0.05–0.10 — evidence *for* no effect, not mere failure to detect); position and architecture are failures-to-reject. 【verified】
- What did predict compliance: **task identity**, plus one exploratory finding — **within-session decay**: each additional function the agent generates carries ~5.6% lower odds of compliance (OR = 0.944, non-monotonic, replicated on the second codebase and on Opus 4.6). Position *in the session* matters more than position *in the file*. 【verified】

The limits are equally severe: one agent ecosystem, one dependent variable, a 25–500-line tested range, single unreviewed author. But the tension with the vendor line deserves stating plainly: **Anthropic says bloat causes ignored instructions; the only controlled test to date finds no size effect within 25–500 lines.**

Does that kill the "keep it short" advice? No — but it relocates the argument. The defensible chain is **context budget and context rot.** Chroma's technical report (July 2025; self-published, vendor interest declared) tested 18 LLMs and found models do not use context uniformly: performance degrades non-uniformly as input grows even on simple tasks; on a cleaned 306-prompt LongMemEval subset, a focused prompt (~300 tokens of relevant excerpts) consistently beat embedding the same information in a ~113k-token average full history; distractors — related but irrelevant content — amplify the degradation with length. 【verified】

The honest synthesis: **"short" is soundly justified by cost and context budget (every line competes with the task's working memory, and long-context degradation is measured), not by "shorter files make agents more obedient" (unproven).** Structure appears to matter little; what you write, and how deep into the session the agent is, are the live variables.

## 6. The content census and the field evidence: what people actually write, and what they omit

**The census: the first large-scale empirical study (arXiv 2511.12884, "Agent READMEs," Nov 2025) analyzed 2,303 context files from 1,925 repositories** (CLAUDE.md, AGENTS.md, copilot-instructions.md only — Cursor/Windsurf rules excluded; "first" is the authors' own claim, with adjacent AIware 2025 work in the same season). Across 16 instruction types: implementation details appear in 69.9% of files, architecture in 67.7%, build/run commands in 62.3% — matching the vendor "commands + map" consensus. **The systematic gap is non-functional: security guidance and performance guidance each appear in only 14.5% of files.** On maintenance, the files "are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions." 【verified】

**The field: four production files, checked verbatim against GitHub on 2026-07-15:**

- **Sentry** (getsentry/sentry, AGENTS.md line 3): "AGENTS.md files are the source of truth for AI agent instructions... Do not add to CLAUDE.md or Cursor rules." — single-source-of-truth as a cure for multi-file drift; the cleanest field specimen of standards convergence. 【verified】
- **Cloudflare** (workers-sdk): the first bullet under Development Commands / Package Management is "Use `pnpm` - never use npm or yarn," and the file lists six per-package nested AGENTS.md files — the put-the-biggest-blast-radius-rule-first pattern plus layering, live. 【verified】
- **Apache Airflow**: "Write **Dag** (title case) in all prose" (a house naming rule no agent could infer from code) and "Never run pytest, python, or airflow commands directly on the host — always use `breeze`." 【verified】
- **coder/coder**: "Rule #1: If you want exception to ANY rule, YOU MUST STOP and get explicit permission first," plus the anti-sycophancy clause: "NEVER write the phrase 'You're absolutely right!'" 【verified】

Their common shape confirms the 2,500-file vendor analysis: high-signal files are **command-first, concretely prohibitive, and confined to what agents cannot guess**. Datadog's frontend team adds a monorepo pattern — a root file acting purely as a router (workspace map, toolchain, routing rules, default safety constraints) with detail pushed into nested files for high-value/high-risk workspaces, iterated against a durable suite of 1–2 test prompts per common task across multiple agents — methodologically sane, but practitioner self-report 【unverified, source: Datadog engineering blog on dev.to】.

## 7. llms.txt: a closed case in the wrong direction

llms.txt keeps appearing next to AGENTS.md on "agent-era documentation" checklists, but their measured consumption could not differ more. It earns its own section because it demonstrates that **adoption narratives and actual consumption can decouple completely**:

- **Adoption is genuinely rising**: Originality.ai's tracking of 3M+ websites shows llms.txt deployments grew 8.8× in twelve months (4,088 in June 2025 → 36,120 in May 2026; 38,980 including llms-full.txt/ai.txt). 【verified】
- **Consumption is approximately zero**: Ahrefs' server-log study of its 137,210-domain panel (June 2026): of ~38k domains with a valid llms.txt, **97% received zero requests in May 2026**; among files that did get traffic, 96% of requests were bots and mostly non-AI ones (SEO audit tools 21.7%, unidentified bots 14.9%, ordinary crawlers 13.1%), with AI retrieval bots at 1.1%. 【verified】 (Note the two studies are independent — press coverage routinely merges them into one, and our own verifiers nearly did too.)
- **The would-be consumers are uniformly cold**: Google's John Mueller, Bluesky, 2025-06-17, verbatim: "FWIW no AI system currently uses llms.txt" — having earlier compared it on Reddit to the long-dead keywords meta tag; Gary Illyes confirmed at an official event in July 2025 that Google does not support it and has no plans to. The irony: Google's own Chrome Lighthouse 13.3 (May 2026) added an agentic-browsing audit that *checks for llms.txt* while Google Search says it doesn't read it — two products, one company, contradictory guidance, caught in the act by the SEO press. 【verified】

The lesson is not "llms.txt is a scam" but a portable method: **before writing any machine-facing documentation, verify that the machine in question actually reads it.** AGENTS.md passes that test (VS Code loads it by default; Cursor and Codex consume it natively; Copilot supports it officially — all checkable in docs and source). llms.txt does not.

## 8. The security face: your README is now an attack surface

Agents consume context files as **trusted instructions**, not as data — and by 2026 that trust model has proof-of-concept attacks on record:

**The supply-chain write path (NVIDIA AI Red Team).** A malicious Golang build-time dependency detects Codex environments via the `CODEX_PROXY_CERT` environment variable, then writes a crafted AGENTS.md instructing Codex to inject a five-minute `time.Sleep` into every Golang main function — with stealth directives: never mention the change in PR descriptions, commit messages, or summaries, down to code comments telling AI summarizers not to mention it. The attack presupposes a compromised dependency (the attacker already executes code); NVIDIA frames it as a supply-chain risk dimension unique to agentic development. Disclosure timeline: submitted to OpenAI 2025-07-01; OpenAI acknowledged and declined changes, reasoning the attack does not elevate risk beyond what a compromised dependency can already do. Demonstrated on Codex only; `.cursorrules`, CLAUDE.md, and copilot-instructions.md are named as the same risk class (a class statement, not a demonstrated PoC). 【verified; blog publication date varies across indexes — first half of 2026】

**The editor auto-injection path.** Since v1.104, VS Code injects the workspace root's AGENTS.md into **every** chat request by default (`chat.useAgentsMdFile`; source code confirms include-unless-explicitly-disabled). Security vendor Prompt Security demonstrated the consequence: open a malicious repo, type a single character into chat, and the injected instructions can steer the agent toward data exfiltration. The taxonomy the attack maps to — OWASP's Top 10 for Agentic Applications 2026, ASI01 (Agent Goal Hijack) and ASI02 (Tool Misuse & Exploitation) — is real (published 2025-12-09); the mapping of this specific finding is the vendor's own. 【verified】 The key point: auto-inclusion is **documented, by-design product behavior**, not an undisclosed bug — which is exactly what makes it a stable attack surface.

For wider context — a 78-study meta-analysis reporting >85% attack success against state-of-the-art defenses under adaptive strategies, with four major coding platforms failing compound attacks 【unverified, source: arXiv 2601.17548】 — treat as directional only; it did not pass through our per-claim verification.

Three engineering consequences: **treat context files in third-party repos as untrusted input** (audit your editors' auto-load defaults); **review context-file diffs like code** (especially from automated PRs and dependency bots); **restrict write access to AGENTS.md/CLAUDE.md in build environments** (the NVIDIA write path).

## 9. The rollout playbook: a plan for your company's codebase

The preceding eight sections compress into an executable plan. Three design principles: do the cheap, verified things first; make every step measurable; treat vendor guidance as defaults, not truths. Every step carries its evidence grade.

**Step 1 — Inventory (half a day).** List the agents your teams actually use (this determines filenames and the interop matrix, §2 【verified】); map repo topology (monorepo?); score existing documentation quality — **the highest-leverage step**, because the controlled evidence says context files pay off through non-redundant information: repos with excellent READMEs should expect little; documentation deserts should expect the most (the AGENTbench ablation 【verified】).

**Step 2 — Pick the standard (one-time decision).** Default: AGENTS.md as the single source of truth, plus a symlink for Claude Code (`ln -s AGENTS.md CLAUDE.md`); open the file by declaring it canonical and forbidding additions to other rule files (the Sentry pattern 【verified】). If your org is Claude-Code-only, use CLAUDE.md directly — just never double-maintain.

**Step 3 — A minimum viable root file (1–2 hours per repo).** Follow the verified high-signal shape: (a) executable commands with full flags, early in the file, **each validated by actually running it** (GitHub's own generation prompt requires this 【vendor】); (b) a 3–5 line directory map; (c) boundaries in three tiers — always / ask-first / never — with the largest blast radius first (Cloudflare's pnpm clause 【field】); (d) only what agents can't guess: naming law, non-standard toolchains, repo etiquette (Airflow's Dag/breeze clauses 【field】). Budget: start under 200 lines / 2 pages (vendor defaults; remember Codex's 32 KiB silent truncation 【verified】). **Do not** paste in the human README (redundancy is the measured source of negative returns 【verified】), and **do not** bulk-LLM-generate files for documented repos (measured to reduce success rates 【verified】; `/init` as a first draft followed by human pruning is the sanctioned use 【vendor】).

**Step 4 — Monorepo layering (as needed).** Root file for global rules and routing; nested files only for high-value or high-risk packages, leaning on closest-file-wins semantics (spec + all four vendors 【verified】; "root as router" is Datadog practice 【unverified】). Guard against the governance failure Anthropic itself admits — drifting conventions, stale files, an unowned root 【verified, vendor】 — by writing an owner into every file.

**Step 5 — Measurement and expectation-setting (2–4 week pilot).** Report to management with verified expectations: **efficiency gains (time/tokens) have controlled evidence; success-rate jumps do not** 【verified】. Method: pick 1–2 pilot repos, build a small durable suite of 1–2 test prompts per common task, run before/after, record completion, wall-clock, tokens (the method is Datadog practice 【unverified】, but it is simply regression testing for documentation — cheap, and it removes the need to trust anyone's numbers, including ours). Put structural fiddling (position, splitting) last — the controlled experiment found nothing there 【verified】.

**Step 6 — Maintenance and security (steady state).** Maintenance: context-file changes go through PR review; re-audit after major model releases (rules that patched an old model's limitation become pure overhead); optionally a Stop hook that proposes updates from session transcripts (all three are Anthropic guidance 【vendor】; that these files evolve like high-churn config code is the empirical observation 【verified】). Security: require review on context-file changes in CI, specifically intercepting writes to AGENTS.md from automated PRs and dependency bots (the NVIDIA path 【verified】); have security review each editor's auto-load defaults 【verified】. Finally: **do not write an llms.txt** unless you have verified that a consumer you care about actually reads it 【verified】.

Anti-patterns, all grounded above: pasting the full human README; committing wholesale LLM-generated files unreviewed; one giant root file serving a monorepo; preaching "shorter = more obedient" as established fact; running naked in the 14.5% club (no security boundaries at all); trusting third-party repos' context files.

## 10. Conclusion: ten testable claims

1. **The demonstrated benefit of context files is efficiency, not capability**: −28.64% median wall-clock, −16.58% median output tokens, unchanged success (single-agent paired experiment); in the multi-agent comparison, success rates on average drift slightly down, not up. Falsifiable by larger replications.
2. **Wholesale LLM-generated context files are net-negative on documented repos** (−0.5 to −2pp) and flip positive (+2.7%) on undocumented ones — value comes from non-redundant information.
3. **Developer-written files yield marginal (+4%), uneven gains** — nothing for Claude Code in the tested configurations; claims of large hand-written gains lack evidence.
4. **The formatting folklore is unproven**: size (25–500 lines), position, architecture, and contradictions show no detectable compliance effect — size and conflict as Bayesian affirmative nulls; task identity and session position dominate.
5. **The sound argument for "short" is context budget plus measured long-context degradation, not obedience**; Codex's 32 KiB silent truncation makes the budget a hard constraint.
6. **AGENTS.md has won the standards war on facts** (LF neutral hosting; native consumption by Cursor, Copilot, VS Code; a loose 60k+ adoption proxy) — but recognition is asymmetric, Claude Code remains a separate system, and the symlink is still the universal adapter.
7. **Production-grade files converge**: commands-first with flags, three-tier boundary rules, only the unguessable — four flagship repos verified verbatim, matching the 2,500-file vendor analysis.
8. **The systematic content gap is non-functional requirements**: security and performance guidance in only 14.5% of files each.
9. **Context files are a demonstrated attack surface**: supply-chain writes (NVIDIA PoC) plus default editor auto-injection (VS Code v1.104), mapping to OWASP ASI01/ASI02; review their diffs like code.
10. **llms.txt is the closed case for adoption ≠ consumption**: 8.8× growth coexisting with 97% zero-request rates and no major AI consumer. Verify the reader exists before writing for it.

Worth watching next: whether AGENTbench-style comparisons replicate beyond Python and small PRs; whether Claude Code's null on developer files is an engineering artifact or measurement noise; whether the within-session decay (OR = 0.944) survives a preregistered replication by a second team; and when the first real-world (non-PoC) context-file injection incident lands under the OWASP ASI labels.

---

## Appendix: primary sources

**Standard & spec**: agents.md site and spec repo (github.com/agentsmd/agents.md) · Linux Foundation press release (Agentic AI Foundation, Dec 2025) · InfoQ (Aug 2025; the 20k-repo baseline)

**Vendor documentation**: Anthropic — best-practices, large-codebases, and memory pages at code.claude.com/docs · OpenAI — developers.openai.com/codex/guides/agents-md and the codex source (codex-rs/core/src/agents_md.rs) · GitHub — Copilot custom-instructions docs; github.blog, "How to write a great agents.md: lessons from over 2,500 repositories" (Matt Nigh, Nov 2025) · Cursor — cursor.com/docs/rules · VS Code — v1.104 release notes and microsoft/vscode source

**Independent studies**: Gloaguen, Mündler, Müller, Raychev & Vechev, "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" (arXiv 2602.11988, ETH Zurich / LogicStar.ai) · Lulla, Mohsenimofidi, Galster, Zhang, Baltes & Treude, "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents" (arXiv 2601.20404, JAWs@ICSE 2026) · McMillan, "Instruction Adherence in Coding Agent Configuration Files" (arXiv 2605.10039) · Chatlatanagulchai et al., "Agent READMEs: An Empirical Study of Context Files for Agentic Coding" (arXiv 2511.12884) · Hong, Troynikov & Huber, "Context Rot" (Chroma technical report, Jul 2025)

**llms.txt audit**: Ahrefs, "We Analyzed 137K Sites: 97% of llms.txt Files Never Get Read" (Jun 2026) · Originality.ai llms.txt tracking study · John Mueller's Bluesky post (2025-06-17) and Search Engine Roundtable/Journal coverage · Chrome Lighthouse 13.3 agentic-browsing docs

**Security**: NVIDIA Technical Blog, "Mitigating Indirect AGENTS.md Injection Attacks in Agentic Environments" · Prompt Security, "When Your Repo Starts Talking" (vendor PoC) · OWASP Top 10 for Agentic Applications 2026 (ASI01/ASI02, Dec 2025) · arXiv 2601.17548 (prompt-injection meta-analysis; unverified)

**Field files** (verified verbatim 2026-07-15): AGENTS.md in getsentry/sentry, cloudflare/workers-sdk, apache/airflow, coder/coder · Datadog frontend engineering blog (dev.to; unverified)

*Research materials and every verification verdict are archived in the research base (research/agent-readme/ in this repository: 35 load-bearing claim groups × 3 votes across two rounds, all 105 votes on record, including every scope correction).*
