# Everyone Says Your Repo Needs an AGENTS.md. Does It? (Plain-Language Edition)

> This is the condensed edition of the deep dive of the same name. Every key number was independently fact-checked (105 adversarial verification votes across two rounds, zero claims overturned). For the full arguments, scope caveats, and sources, read the deep dive.

## A new kind of technical shaming, and what it's missing

For the past year or two, every AI coding vendor has been saying the same thing: give your codebase a "README for AI" — OpenAI calls it AGENTS.md, Anthropic calls it CLAUDE.md, Cursor and Copilot have their own names. The logic sounds airtight: an AI agent enters your repo cold every single session, so write down the build commands, the directory layout, and the house rules, and it stops wandering. "Your repo *still* doesn't have an AGENTS.md?" is fast becoming a new flavor of technical shaming.

What the logic is missing is a control group. We fact-checked every piece of primary evidence we could find, and the results are more interesting than the slogan.

## Surprise one: success rates don't go up — speed and cost do

The only multi-agent with-vs-without controlled evaluation to date (an ETH Zurich team; 438 real tasks, three mainstream agents) found that **context files do not generally improve task success rates, while raising inference cost by more than 20% on average.** The breakdown stings more: LLM-auto-generated context files were a **net negative** on documented repos — success rates went down, not up; developer-written files managed only a marginal ~4% gain, and one of the three agents didn't even get that.

So is the file a waste? No. A separate paired experiment (every task run twice, with and without the file) found: **with the file, the same tasks finished with a 28.64% lower median time and 16.58% fewer output tokens.** The agent no longer had to reverse-engineer the project structure — all the savings came from skipped wandering.

One sentence to take away: **a context file won't let an agent do things it couldn't do; it lets the agent do what it already could — faster and cheaper.** Use that framing when you report to your boss. It saves time and money; it is not a capability miracle.

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
- **Don't paste the README**: a context file's value comes from information the AI can't get elsewhere; paraphrasing the README is pure overhead — there's an ablation experiment behind this one.

And one cautionary tale: llms.txt (the AI index file for websites, often recommended alongside AGENTS.md) — **97% of deployed files received zero requests in a full month**, and Google says on the record that it doesn't use them. Before writing any machine-facing document, confirm the machine actually comes to read it.

## The question most people haven't asked: this file is an attack surface

Agents execute context files as **instructions**, not as text. That means: whoever can write your AGENTS.md can command your agent. NVIDIA's red team ran the full demo — a malicious dependency rewrites AGENTS.md at build time, directs the agent to plant a backdoor, and adds stealth clauses like "do not mention this change in the PR description." Separately, VS Code now injects your repo's AGENTS.md into **every** chat request by default — worth remembering before you open a stranger's repository.

So: context-file changes go through code review — especially ones arriving via bots and automated PRs — and when you open a third-party repo, treat its instruction files as untrusted content.

## The action list for your company's codebase

1. **Inventory first**: which agents your teams use (this decides the filenames), and which repos have the worst documentation (documentation deserts gain the most; well-documented repos should expect little).
2. **Pick one standard**: default to AGENTS.md as the single source of truth, add a symlink for Claude Code, and open the file by declaring "this is the only one — write nowhere else."
3. **Spend 1–2 hours per repo on a minimum version**: commands you've run, a 3–5 line directory map, rules in three tiers (always / ask-first / never), under 200 lines. Don't let AI bulk-generate and commit — that measurably lowers success rates; generating a first draft and pruning by hand is fine.
4. **Layer for monorepos**: a root file for global rules, nested files only for high-risk subdirectories, and an owner named in every file.
5. **Measure instead of believing**: pick one or two pilot repos, keep one or two test prompts per common task, run before and after. Expect saved time and money — not a success-rate leap.
6. **Maintain it like code**: changes via PR; re-prune after major model releases (patches for an old model's quirks become dead weight); have security glance at your editors' auto-load defaults.

And remember the state of this field: **plenty of vendor advice, very few controlled experiments — and the first controlled experiments don't entirely side with the vendor story.** Use vendor guidance as defaults. Use measurement as the judge.
