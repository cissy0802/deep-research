# Everyone Says Your Repo Needs an AGENTS.md. Does It? (Plain-Language Edition)

> This is the condensed edition of the deep dive of the same name. Every key number went through three rounds of independent checking (105 fidelity-to-source votes, plus 12 contradiction-search and hostile methods-audit verdicts — the audit struck down two widely circulated numbers, and the contradiction search surfaced studies that flatly disagree). For the full arguments, evidence tiers, and sources, read the deep dive.

## A new kind of technical shaming, and what it's missing

For the past year or two, every AI coding vendor has been saying the same thing: give your codebase a "README for AI" — OpenAI calls it AGENTS.md, Anthropic calls it CLAUDE.md, Cursor and Copilot have their own names. The logic sounds airtight: an AI agent enters your repo cold every single session, so write down the build commands, the directory layout, and the house rules, and it stops wandering. "Your repo *still* doesn't have an AGENTS.md?" is fast becoming a new flavor of technical shaming.

What the logic is missing is a control group. We fact-checked every piece of primary evidence we could find, and the results are more interesting than the slogan.

## Surprise one: the controlled studies fight each other — the only statistically tested win is time and money

The first half of 2026 produced three with-vs-without controlled studies, and they contradict each other: an ETH Zurich team says success rates don't rise and costs go up ~20%; a second team's paired experiment measured **28.64% lower median time and 16.58% fewer output tokens with the file present** (the only number of the three that carries a statistical significance test); a third team measured LLM-generated guidance files *raising* resolve rates by 2.8–7.5 percentage points.

We ran a hostile methods audit on all three. Result: the most famous one (ETH) had its success-rate numbers struck down — no statistical tests anywhere in the paper, every task run exactly once, an effective sample of just 12 repositories; at that precision, a ±2–4-point "direction" simply cannot be read off.

So the honest summary: **nobody currently knows whether these files move success rates; the only benefit left standing is saved time and tokens — and even that has been measured exactly once.** Use that framing with your boss: worth trying, worth measuring yourself, no capability miracles promised.

## Surprise two: most of the how-to-write folklore aims at the wrong target

There's a whole scripture of file-writing rules online: keep it short, put important things at the top, don't split into too many files, never contradict yourself. Someone finally ran a randomized experiment (1,650 real agent sessions): **file size, instruction position, single vs. nested files, presence of contradictions — none of the four had any detectable effect on whether the agent obeyed.** For size and contradictions, the "no effect" even carries affirmative statistical support — it's not just "we couldn't tell."

What actually predicts obedience: **which task it is**, and **how deep into the session the agent is** — with every additional piece of work, the odds of following your instruction slip a little further. Which *line of the file* an instruction sits on doesn't matter; which *item of the session* the agent is on does.

So does "keep it short" survive? Yes — but for a different reason. Not "shorter files are obeyed better" (no evidence), but **every line you write competes with the agent's working memory for the actual task** — long-context degradation is a measured phenomenon, and OpenAI's Codex silently truncates everything past 32 KB, so beyond that point your prose is invisible anyway.

## What should actually go in it? Copy these homework answers

We verified several big production repos' files verbatim against the originals; the pattern is remarkably consistent:

- **Commands first**: fully-flagged build/test commands you have personally run, at the top of the file.
- **Prohibitions concrete, and first**: Cloudflare's file leads with "Use `pnpm` — never use npm or yarn" (otherwise an agent corrupts the whole monorepo's lockfile).
- **Only what AI can't guess**: Airflow writes "spell it **Dag**, title case, in all prose" and "never run pytest directly on the host" — house rules no amount of code-reading would reveal.
- **One file to rule them**: Sentry's file opens by declaring "AGENTS.md files are the source of truth — do not add to CLAUDE.md or Cursor rules," killing multi-file drift.
- **Don't paste the README**: a context file's value *probably* comes from information the AI can't get elsewhere — the field's most promising hypothesis, with weak signals from two independent studies pointing the same way; paraphrasing the README is most likely pure overhead.

And one cautionary tale: llms.txt (the AI index file for websites, often recommended alongside AGENTS.md) — **97% of deployed files received zero requests in a full month**, and Google says on the record that it doesn't use them. Before writing any machine-facing document, confirm the machine actually comes to read it.

## The question most people haven't asked: this file is an attack surface

Agents execute context files as **instructions**, not as text. That means: whoever can write your AGENTS.md can command your agent. NVIDIA's red team ran the full demo — a malicious dependency rewrites AGENTS.md at build time, directs the agent to plant a backdoor, and adds stealth clauses like "do not mention this change in the PR description." Separately, VS Code now injects your repo's AGENTS.md into **every** chat request by default — worth remembering before you open a stranger's repository.

So: context-file changes go through code review — especially ones arriving via bots and automated PRs — and when you open a third-party repo, treat its instruction files as untrusted content.

## The action list for your company's codebase

1. **Inventory first**: which agents your teams use (this decides the filenames), and which repos have the worst documentation (documentation deserts gain the most; well-documented repos should expect little).
2. **Pick one standard**: default to AGENTS.md as the single source of truth, add a symlink for Claude Code, and open the file by declaring "this is the only one — write nowhere else."
3. **Spend 1–2 hours per repo on a minimum version**: commands you've run, a 3–5 line directory map, rules in three tiers (always / ask-first / never), under 200 lines. Bulk-AI-generate and commit sight-unseen? One study says harm, another says gain — nobody has won that fight; the robust route is generate a draft, prune by hand, and let step 5's measurements decide.
4. **Layer for monorepos**: a root file for global rules, nested files only for high-risk subdirectories, and an owner named in every file.
5. **Measure instead of believing**: pick one or two pilot repos, keep one or two test prompts per common task, run before and after. The published studies contradict each other, so your own measurement is the only local ground truth you'll get; expect saved time and money, and treat any success-rate gain as a bonus.
6. **Maintain it like code**: changes via PR; re-prune after major model releases (patches for an old model's quirks become dead weight); have security glance at your editors' auto-load defaults.

And remember the state of this field: **plenty of vendor advice, very few controlled experiments — and the first controlled experiments side neither with the vendors nor with each other.** Use vendor guidance as defaults. Use your own measurement as the judge.
