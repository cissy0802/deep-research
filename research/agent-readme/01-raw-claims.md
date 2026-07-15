# Round 1 原始论断全集(26 个来源的抽取结果;多数未进入 Round 1 验证)

> 来自 wf_71d43d15-568 journal。标 [UNVERIFIED] 的论断未经过 3 票对抗验证——其中线 3-7(实证/llms.txt/安全/实践/维护)的承重论断是 Round 2 验证输入。已验证的 25 条见 02-verified-claims.md。

## https://github.com/agentsmd/agents.md
(quality: primary, publishDate: unknown (repo live and maintained as of 2026-07; site references OpenAI Codex-era launch, mid-2025), claims: 5)

- **[UNVERIFIED]** AGENTS.md is positioned by its official spec repo as a simple, open, cross-tool format — a 'README for agents' giving coding agents a dedicated, predictable place for project context, distinct from vendor-specific files like CLAUDE.md.
  - quote: “AGENTS.md is a simple, open format for guiding coding agents. ... Think of AGENTS.md as a README for agents: a dedicated, predictable place to provide context and instructions to help AI coding agents work on your project.”
  - importance: central
- **[UNVERIFIED]** The spec defines an explicit precedence rule for nested files: when instructions conflict, the AGENTS.md closest to the file being edited wins, and explicit user chat prompts override all file instructions.
  - quote: “The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything.”
  - importance: central
- **[UNVERIFIED]** For monorepos the spec recommends per-package nested AGENTS.md files with nearest-file precedence, and cites the OpenAI main repository as containing 88 AGENTS.md files at the time of writing — a checkable adoption data point.
  - quote: “Place another AGENTS.md inside each package. Agents automatically read the nearest file in the directory tree, so the closest one takes precedence. ... [the OpenAI repository has] 88 AGENTS.md files”
  - importance: central
- **[UNVERIFIED]** The official FAQ endorses symlink-based interoperability as the migration path from other agent-file formats (rename the old file to AGENTS.md and symlink the legacy name), and documents config-based compatibility for tools like Aider (.aider.conf.yml 'read: AGENTS.md') and Gemini CLI (.gemini/settings.json fileName setting).
  - quote: “mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md”
  - importance: central
- **[UNVERIFIED]** AGENTS.md imposes no required schema — it is plain Markdown with arbitrary headings — and the spec repo itself (MIT-licensed, ~23,000 GitHub stars / ~1,700 forks as of 2026-07) treats it as living documentation that agents parse as free text.
  - quote: “No. AGENTS.md is just standard Markdown. Use any headings you like; the agent simply parses the text you provide.”
  - importance: supporting

## https://www.infoq.com/news/2025/08/agents-md/
(quality: secondary, publishDate: 2025-08-27, claims: 5)

- **[UNVERIFIED]** As of the article's publication (August 2025), the AGENTS.md format had been adopted by more than 20,000 repositories on GitHub — a checkable adoption figure for the '标准之争与采用现状' line (later narratives cite 60,000+ by mid-2026, so the 20k number is the Aug-2025 baseline).
  - quote: “AGENTS.md is a straightforward and open format designed to assist AI coding agents in software development. Already adopted by more than 20,000 repositories on GitHub, the format is positioned as a companion to traditional documentation, offering machine-readable context that complements human-facing files like README.md.”
  - importance: central
- **[UNVERIFIED]** AGENTS.md was created as a cross-vendor collaborative effort rather than a single-vendor format, with OpenAI Codex, Amp (Sourcegraph), Google Jules, Cursor, and Factory named as co-developers — directly bearing on the AGENTS.md-vs-CLAUDE.md standards question.
  - quote: “AGENTS.md emerged from collaborative efforts across the AI software development ecosystem, including OpenAI Codex, Amp, Jules from Google, Cursor, and Factory.”
  - importance: central
- **[UNVERIFIED]** The article defines the intended content scope of AGENTS.md as agent-specific operational instructions (setup/build commands, testing workflows, coding style, PR guidelines) placed at a predictable location, distinguishing it from human-facing READMEs.
  - quote: “While READMEs are optimized for developers, AGENTS.md serves as a predictable, structured location for agent-specific instructions including setup commands, testing workflows, coding style preferences, and pull request guidelines.”
  - importance: supporting
- **[UNVERIFIED]** The format deliberately uses plain Markdown with no proprietary configuration schema, which early adopters cite as the reason it fits into existing project structures — relevant to the convergence/interoperability thread.
  - quote: “Early adopters highlight that rather than introducing a proprietary configuration file, its markdown-based approach ensures accessibility while fitting neatly into existing project structures.”
  - importance: supporting
- **[UNVERIFIED]** The article records community pushback (via Hacker News reactions): some developers are skeptical of splitting documentation into human-facing and agent-facing files, and others caution that AGENTS.md does not remove the need for human oversight since agents still need guidance on business logic and humans remain the bottleneck in reviewing changes.
  - quote: “Some developers are skeptical of the split between human- and agent-facing documentation... other developers caution that AGENTS.md will not eliminate the need for human oversight, noting that agents will need special guidance for business logic and that the real bottleneck will be in how humans read and interpret the changes.”
  - importance: supporting

## https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
(quality: primary, publishDate: 2025-11-25, claims: 5)

- **[UNVERIFIED]** GitHub 官方分析了公开仓库中 2,500+ 个 agents.md 文件,并总结出成功文件的共性模式:给 agent 一个具体职责/persona、可直接执行的命令、明确边界、以及好的输出示例(文章发布于 2025-11-25,GitHub 官方 X 账号亦发帖确认 'We analyzed 2500+ agents.md files')。
  - quote: “analyzed over 2,500 agents.md files across public repos ... provide your agent a specific job or persona, exact commands to run, well-defined boundaries to follow, and clear examples of good output for the agent to follow”
  - importance: central
- **[UNVERIFIED]** GitHub 建议 agents.md 覆盖六个核心区域:commands、testing、project structure、code style、git workflow、boundaries,并采用 always do / ask first / never do 的边界规则来防止破坏性错误。
  - quote: “cover the six core areas: Commands, testing, project structure, code style, git workflow, and boundaries ... Set clear rules using always do, ask first, never do, preventing destructive mistakes.”
  - importance: central
- **[UNVERIFIED]** GitHub 建议把可执行命令(带完整 flags/options,而非仅工具名)放在文件靠前的章节,因为 agent 会频繁引用这些命令。
  - quote: “Put relevant executable commands in an early section with flags and options, not just tool names, as your agent will reference these often.”
  - importance: central
- **[UNVERIFIED]** GitHub 的分析结论之一:一个真实代码片段展示代码风格,胜过三段文字描述——示例优于 prose 描述。
  - quote: “One real code snippet showing your style beats three paragraphs describing it.”
  - importance: supporting
- **[UNVERIFIED]** GitHub 总结 2,500+ 仓库中最强的 agents.md 文件共同特质是简洁、实用、保持最新、写成对 agent 的指令而非面向人类的文档;模糊的 persona('You are a helpful coding assistant')被认定为失效模式。
  - quote: “The strongest examples across more than 2,500 repositories share traits: they are concise, practical, current, and written as instructions rather than documentation for humans alone. ... "You are a helpful coding assistant" doesn't work.”
  - importance: supporting

## https://www.morphllm.com/agents-md-guide
(quality: unreliable, publishDate: ?, claims: 0)


## https://www.seroundtable.com/google-ai-llms-txt-39607.html
(quality: secondary, publishDate: 2025-06-18 (inferred: author Barry Schwartz's X posts linking the article decode to 2025-06-18; exact page date unverifiable because seroundtable.com and archive mirrors were blocked by the network proxy), claims: 4)

- **[UNVERIFIED]** Google Search Advocate John Mueller publicly stated (on Bluesky, 2025-06-18) that no AI system was consuming llms.txt at that time — a direct on-the-record statement bearing on the llms.txt adoption-vs-consumption gap in the research question.
  - quote: “FWIW no AI system currently uses llms.txt.”
  - importance: central
- **[UNVERIFIED]** Mueller's fuller statement asserts that no AI service has announced using llms.txt, that site owners' server logs show AI crawlers do not even request the file, and he likens it to the discredited keywords meta tag (self-declared, manipulable metadata).
  - quote: “AFAIK none of the AI services have said they're using LLMs.TXT (and you can tell when you look at your server logs that they don't even check for it). To me, it's comparable to the keywords meta tag.”
  - importance: central
- **[UNVERIFIED]** The article distinguishes fetching behavior: consumer LLMs/chatbots do fetch ordinary web pages for training and grounding, but none fetch the llms.txt file specifically — i.e., the file is ignored rather than the sites being ignored.
  - quote: “The consumer LLMs / chatbots (the ones that SEOs want traffic from) will fetch your pages - for training and grounding, but none of them fetch the llms.txt file.”
  - importance: supporting
- **[UNVERIFIED]** The statement originated as Mueller's personal reply on Bluesky in June 2025 (surfaced by Barry Schwartz on 2025-06-18), not as a formal Google policy document — relevant to grading the evidence level of the 'Google doesn't consume llms.txt' claim (named-official statement, informal channel).
  - quote: “Google's @johnmu on if you should add an llms.txt file to your site, "FWIW no AI system currently uses llms.txt"”
  - importance: supporting

## https://code.claude.com/docs/en/best-practices
(quality: primary, publishDate: unknown (live official docs page, retrieved 2026-07-15; no publish date shown), claims: 5)

- **[UNVERIFIED]** Anthropic's official guidance is that CLAUDE.md must be kept short, and it explicitly asserts that overly long/bloated CLAUDE.md files cause Claude to ignore instructions — the vendor itself warns against the 'write more context' approach.
  - quote: “Keep it concise. For each line, ask: "Would removing this cause Claude to make mistakes?" If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!”
  - importance: central
- **[UNVERIFIED]** Claude Code supports a hierarchical/layered CLAUDE.md scheme: home-folder, project-root, CLAUDE.local.md, parent-directory files (auto-loaded, recommended for monorepos), and child-directory files that are pulled in on demand when Claude reads files in those directories.
  - quote: “Parent directories: useful for monorepos where both root/CLAUDE.md and root/foo/CLAUDE.md are pulled in automatically ... Child directories: Claude pulls in child CLAUDE.md files on demand when it reads a file in those directories”
  - importance: central
- **[UNVERIFIED]** Anthropic recommends specific content categories for CLAUDE.md — bash commands Claude can't guess, non-default code style rules, testing instructions, repo etiquette, project-specific architectural decisions — and recommends excluding anything Claude can infer from code, detailed API docs, and frequently changing information; occasional domain knowledge should go in on-demand skills instead.
  - quote: “CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows that are only relevant sometimes, use skills instead. Claude loads them on demand without bloating every conversation.”
  - importance: central
- **[UNVERIFIED]** Anthropic states that /init auto-generates a starter CLAUDE.md by analyzing the codebase (build systems, test frameworks, code patterns), and advises treating CLAUDE.md like code — checked into git, pruned regularly, and tested by observing behavior changes; adherence can be tuned with emphasis markers like 'IMPORTANT' or 'YOU MUST'.
  - quote: “The /init command analyzes your codebase to detect build systems, test frameworks, and code patterns, giving you a solid foundation to refine. ... Treat CLAUDE.md like code: review it when things go wrong, prune it regularly, and test changes by observing whether Claude's behavior actually shifts. You can tune instructions by adding emphasis (e.g., "IMPORTANT" or "YOU MUST") to improve adherence.”
  - importance: central
- **[UNVERIFIED]** Anthropic's docs assert (vendor claim, no cited study) that LLM performance degrades as the context window fills, with Claude 'forgetting' earlier instructions — the stated rationale behind nearly all of its context-file best practices.
  - quote: “This matters since LLM performance degrades as context fills. When the context window is getting full, Claude may start "forgetting" earlier instructions or making more mistakes. The context window is the most important resource to manage.”
  - importance: supporting

## https://medium.com/@kaispriestersbach/the-llms-txt-is-dead-more-precisely-a-dud-ab7bee4f469c
(quality: blog, publishDate: 2026-02-23 (per search-index snippet; direct fetch blocked, date not independently verified), claims: 5)

- **[UNVERIFIED]** Server-log measurement by OtterlyAI over 90 days found that of 62,100+ AI bot requests to a site with a correctly implemented llms.txt, only 84 requests (~0.1%) targeted the /llms.txt file — i.e., AI crawlers essentially do not fetch it.
  - quote: “OtterlyAI measured what happens when a correctly implemented llms.txt is provided, and out of 62,100 AI bot requests, exactly 84 went to the llms.txt file - that's 0.1 percent.”
  - importance: central
- **[UNVERIFIED]** Google's Gary Illyes stated (at Google Search Central Live) that Google does not support llms.txt and has no plans to do so.
  - quote: “Gary Illyes confirmed at Google Search Central Live: Google does not support llms.txt and has no plans to do so.”
  - importance: central
- **[UNVERIFIED]** The article argues llms.txt was never proposed by Jeremy Howard as an SEO/GEO visibility mechanism; its intended and only legitimate use is inference-time consumption of developer documentation by coding tools/agents (e.g., Cursor, Windsurf, Claude Code), and the SEO industry (e.g., Yoast's llms.txt generator, agency service offerings) misappropriated it.
  - quote: “Jeremy Howard never proposed llms.txt as a GEO or SEO measure, but rather addresses inference-time usage by coding tools and AI agents, not visibility in generative search systems... the SEO and GEO community discovered llms.txt and interpreted it as what they wished it were: a new lever for visibility in AI search systems.”
  - importance: central
- **[UNVERIFIED]** The article's structural argument: llms.txt fails for the same reason the keywords meta tag was abandoned — a self-declared signal fully controlled by the evaluated party is worthless to the evaluator because it invites manipulation.
  - quote: “a signal the evaluated party controls themselves is worthless to the evaluator, which is exactly the problem search engines identified with the keywords meta tag.”
  - importance: supporting
- **[UNVERIFIED]** In the same OtterlyAI dataset, an average content page on the domain received roughly 265 AI bot visits versus 84 for /llms.txt, and the file's presence produced no measurable change in overall AI bot crawling patterns.
  - quote: “The site's average content page received ~265 AI bot visits during the same period, while /llms.txt received only 84 visits... the presence of a correctly implemented llms.txt file did not correlate with any noticeable uptick in overall AI bot activity or shift in crawling patterns.”
  - importance: supporting

## https://developers.openai.com/codex/guides/agents-md
(quality: primary, publishDate: Undated on page; in-repo copy of this guide existed by openai/codex tag rust-v0.50.0 (late 2025), unchanged through rust-v0.65.0, migrated to developers.openai.com by rust-v0.80.0; content verified 2026-07-15, claims: 5)

- **[UNVERIFIED]** Codex discovers AGENTS.md hierarchically: global instructions from ~/.codex are loaded first, then one file per directory from the repository root down to the current working directory, concatenated root-to-leaf, with deeper (more specific) files overriding earlier layers.
  - quote: “Before Codex gets to work, the instructions are ingested in precedence order: global guidance from `~/.codex` comes first, then each project doc from the repository root down to your current directory. Guidance in deeper directories overrides earlier layers, so the most specific file controls the final behavior.”
  - importance: central
- **[UNVERIFIED]** Codex imposes a hard default cap of 32 KiB on the combined size of all AGENTS.md content (config key project_doc_max_bytes); oversized files are truncated, and OpenAI's recommended remedy is to split guidance across nested directories rather than write one long file.
  - quote: “Files are read in order from root to leaf and joined together with blank lines. Empty files are skipped, and very large files are truncated once the combined size reaches 32 KiB (the default [`project_doc_max_bytes`](../docs/config.md#project_doc_max_bytes) limit). If you need more space, split guidance across nested directories or raise the limit in your configuration.”
  - importance: central
- **[UNVERIFIED]** By default Codex only consumes the filenames AGENTS.override.md and AGENTS.md; other instruction filenames (e.g. CLAUDE.md, instructions.md) are ignored unless explicitly added via the project_doc_fallback_filenames config option — so cross-tool interop requires either renaming/symlinking or per-user configuration, not automatic recognition.
  - quote: “Only the first non-empty file is used. Other filenames, such as `instructions.md`, have no effect unless Codex is specifically instructed to use them. ... Codex can look for additional instruction filenames beyond the two defaults if you add them to `project_doc_fallback_filenames` in your Codex configuration.”
  - importance: central
- **[UNVERIFIED]** OpenAI's recommended AGENTS.md content is short, concrete working agreements — build/test commands and dependency policy — with communication-style preferences kept in the global file and team/codebase rules in repo files (live-page content retrieved via search snippets, as the page itself was network-blocked; wording should be reverified against the live URL).
  - quote: “Always run `npm test` after modifying JavaScript files. Prefer `pnpm` when installing dependencies. Ask for confirmation before adding new production dependencies. ... Use the global file to shape how Codex communicates with you (for example, review style, verbosity, and defaults), and keep repo files focused on team and codebase rules.”
  - importance: central
- **[UNVERIFIED]** OpenAI explicitly anchors Codex's instruction mechanism to the AGENTS.md open standard (agents.md), evidence for vendor convergence on that standard rather than a proprietary format.
  - quote: “Codex uses [`AGENTS.md`](https://agents.md/) files to gather helpful guidance before it starts assisting you. This page explains how those files are discovered and combined, so you can decide where to place your instructions.”
  - importance: supporting

## https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
(quality: primary, publishDate: No explicit publish date; continuously updated official docs — content verified against github/docs main branch on 2026-07-15, claims: 5)

- **[UNVERIFIED]** GitHub Copilot on github.com officially supports three types of repository custom instructions: repository-wide (.github/copilot-instructions.md), path-specific (.github/instructions/NAME.instructions.md), and agent instructions via AGENTS.md — with a single root-level CLAUDE.md or GEMINI.md accepted as an alternative agent-instructions file, showing cross-vendor interop with Anthropic/Google formats.
  - quote: “Copilot on GitHub supports three types of repository custom instructions... These are specified in a `copilot-instructions.md` file in the `.github` directory of the repository... specified in one or more `NAME.instructions.md` files within or below the `.github/instructions` directory... **Agent instructions** are used by AI agents... Alternatively, you can use a single `CLAUDE.md` or `GEMINI.md` file stored in the root of the repository.”
  - importance: central
- **[UNVERIFIED]** Copilot supports multiple nested AGENTS.md files anywhere in the repository with nearest-file-wins precedence, and GitHub's docs point to the agentsmd/agents.md repository as the reference for the open standard — direct evidence of vendor convergence on AGENTS.md.
  - quote: “You can create one or more `AGENTS.md` files, stored anywhere within the repository. When Copilot is working, the nearest `AGENTS.md` file in the directory tree will take precedence. For more information, see the [agentsmd/agents.md repository](https://github.com/agentsmd/agents.md).”
  - importance: central
- **[UNVERIFIED]** GitHub's official prompt for auto-generating copilot-instructions.md caps the file at two pages, prioritizes validated build/test/lint commands and a project-layout map, and explicitly tells the agent to trust the instructions over re-searching the repo — matching the cross-vendor consensus of 'short + build/test commands + architecture map'.
  - quote: “Instructions must be no longer than 2 pages... For each of bootstrap, build, test, run, lint, and any other scripted step, document the sequence of steps to take to run it successfully... Finally, explicitly instruct the agent to trust the instructions and only perform a search if the information in the instructions is incomplete or found to be in error.”
  - importance: central
- **[UNVERIFIED]** Path-specific instruction files use an applyTo glob frontmatter (comma-separated patterns) and an optional excludeAgent key ('code-review' or 'cloud-agent'); on GitHub.com, path-specific custom instructions are currently only consumed by Copilot cloud agent and Copilot code review, not all Copilot features.
  - quote: “At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to... Currently, on GitHub.com, path-specific custom instructions are only supported for Copilot cloud agent and Copilot code review.”
  - importance: supporting
- **[UNVERIFIED]** When multiple instruction scopes apply, GitHub defines a priority order — personal instructions highest, then repository, then organization — but all relevant instruction sets are still injected into the request, and GitHub explicitly warns users to avoid conflicting instruction sets.
  - quote: “Personal instructions take the highest priority. Repository instructions come next, and then organization instructions are prioritized last. However, all sets of relevant instructions are provided to Copilot... Whenever possible, try to avoid providing conflicting sets of instructions.”
  - importance: supporting

## https://cursor.com/docs/rules
(quality: primary, publishDate: Undated, continuously updated vendor docs; content reflects Cursor 2.2 era (late 2025–2026); retrieved 2026-07-15 via verbatim GitHub mirror because cursor.com was blocked by the environment proxy, claims: 5)

- **[UNVERIFIED]** Cursor's official best-practice guidance for rules is to keep each rule under 500 lines, split large rules into multiple composable rules, provide concrete examples or referenced files, and avoid vague guidance ('write rules like clear internal docs').
  - quote: “Good rules are focused, actionable, and scoped. - Keep rules under 500 lines - Split large rules into multiple, composable rules - Provide concrete examples or referenced files - Avoid vague guidance. Write rules like clear internal docs - Reuse rules when repeating prompts in chat”
  - importance: central
- **[UNVERIFIED]** Cursor natively supports AGENTS.md as a first-class alternative to .cursor/rules, including nested AGENTS.md files in subdirectories that are combined with parent-directory files, with more specific (deeper) instructions taking precedence — direct evidence of vendor convergence on the AGENTS.md open standard and of hierarchical per-folder context files.
  - quote: “Cursor supports AGENTS.md in the project root and subdirectories. ... Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence.”
  - importance: central
- **[UNVERIFIED]** The legacy .cursorrules root file is still supported but officially slated for deprecation; Cursor recommends migrating to Project Rules or AGENTS.md, and as of Cursor 2.2 the .mdc single-file rule format is superseded by folder-based rules (RULE.md inside .cursor/rules/<rule-name>/).
  - quote: “The `.cursorrules` (legacy) file in your project root is still supported but **will be deprecated**. We recommend migrating to Project Rules or to `AGENTS.md`. ... As of 2.2, `.mdc` cursor rules will remain functional however all new rules will now be created as folders in `.cursor/rules`.”
  - importance: central
- **[UNVERIFIED]** Cursor rules are injected at the start of the model context and are applied via four activation modes (Always Apply; Apply Intelligently based on the rule's description; Apply to Specific Files via glob patterns; Apply Manually via @-mention), controlled by frontmatter fields description/globs/alwaysApply; when multiple sources conflict, precedence is Team Rules → Project Rules → User Rules.
  - quote: “When applied, rule contents are included at the start of the model context. ... Rules are applied in this order: **Team Rules → Project Rules → User Rules**. All applicable rules are merged; earlier sources take precedence when guidance conflicts.”
  - importance: supporting
- **[UNVERIFIED]** Cursor can import and consume Claude's skills and plugins system (cross-vendor interop), treating imported items as agent-decided rules whose relevance Cursor determines from context; they cannot be configured as always-apply or manual rules.
  - quote: “Cursor can load rules from Claude's skills and plugins system. These imported rules are always applied as agent-decided rules, meaning Cursor determines when they are relevant based on context.”
  - importance: supporting

## https://code.visualstudio.com/docs/agent-customization/custom-instructions
(quality: primary, publishDate: 2026-07-15 (DateApproved: 7/15/2026 in the page's frontmatter), claims: 5)

- **[UNVERIFIED]** VS Code natively supports multiple competing agent-context file formats side by side — .github/copilot-instructions.md, AGENTS.md, and CLAUDE.md are all auto-detected as always-on instructions, demonstrating cross-vendor interoperability at the tool level rather than convergence on one standard.
  - quote: “VS Code automatically detects an `AGENTS.md` Markdown file in the root of your workspace and applies the instructions in this file to all chat requests within this workspace. ... VS Code automatically detects a `CLAUDE.md` file and applies it as always-on instructions, similar to `AGENTS.md`. This is useful if you use Claude Code or other Claude-based tools alongside VS Code and want a single set of instructions recognized by all of them.”
  - importance: central
- **[UNVERIFIED]** As of 2026-07, nested per-subfolder AGENTS.md support in VS Code is still gated behind an experimental setting (chat.useNestedAgentsMdFiles); root-level AGENTS.md is controlled by chat.useAgentsMdFile — i.e., hierarchical/layered agent files are not yet a stable feature in VS Code.
  - quote: “Use the experimental `setting(chat.useNestedAgentsMdFiles)` setting to enable or disable support for nested `AGENTS.md` files in your workspace. When enabled, VS Code searches recursively in all subfolders of your workspace for `AGENTS.md` files and adds their relative path to the chat context.”
  - importance: central
- **[UNVERIFIED]** VS Code's official writing guidance matches the cross-vendor consensus: keep instructions short and self-contained, focus on non-obvious rules that linters don't enforce, explain the reasoning behind rules, and prefer concrete code examples over abstract rules.
  - quote: “Keep your instructions short and self-contained. Each instruction should be a single, simple statement. ... Focus on non-obvious rules. Skip conventions that standard linters or formatters already enforce. ... Show preferred and avoided patterns with concrete code examples. The AI responds more effectively to examples than to abstract rules.”
  - importance: central
- **[UNVERIFIED]** VS Code ships an AI-powered /init command that analyzes the workspace (including discovering existing copilot-instructions.md or AGENTS.md files) and auto-generates workspace custom instructions — mirroring Claude Code's /init and putting auto-generation of context files in the mainstream vendor toolchain.
  - quote: “It discovers existing AI conventions in your workspace, such as `copilot-instructions.md` or `AGENTS.md` files. It analyzes your project structure and coding patterns. It generates comprehensive workspace instructions tailored to your project.”
  - importance: supporting
- **[UNVERIFIED]** When multiple instruction sources conflict, VS Code documents an explicit priority order: personal (user-level) instructions override repository instructions (.github/copilot-instructions.md or AGENTS.md), which override GitHub organization-level instructions; otherwise all instruction files are combined with no guaranteed order.
  - quote: “Higher-priority instructions take precedence when conflicts occur: 1. Personal instructions (user-level, highest priority) 1. Repository instructions (`.github/copilot-instructions.md` or `AGENTS.md`) 1. Organization instructions (lowest priority)”
  - importance: supporting

## https://agents.md/
(quality: primary, publishDate: unknown (no publish date on page; content retrieved from live main branch of source repo openai/agents.md on 2026-07-15), claims: 5)

- **[UNVERIFIED]** The official AGENTS.md site claims adoption by over 60,000 open-source projects, and links this number to a reproducible GitHub code-search query (path:AGENTS.md NOT is:fork NOT is:archived), giving an auditable counting methodology.
  - quote: “A simple, open format for guiding coding agents, used by over 60k open-source projects. [link: https://github.com/search?q=path%3AAGENTS.md+NOT+is%3Afork+NOT+is%3Aarchived&type=code]”
  - importance: central
- **[UNVERIFIED]** The spec defines a precedence rule for nested/monorepo setups: the AGENTS.md file closest to the edited file wins, and explicit user chat prompts override all AGENTS.md instructions; the site cites OpenAI's main repo carrying 88 AGENTS.md files as a nested-file example.
  - quote: “The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything. ... Agents automatically read the nearest file in the directory tree, so the closest one takes precedence and every subproject can ship tailored instructions. For example, at time of writing the main OpenAI repo has 88 AGENTS.md files.”
  - importance: central
- **[UNVERIFIED]** AGENTS.md originated as a cross-vendor effort (OpenAI Codex, Amp, Google's Jules, Cursor, Factory) and is now stewarded by the Agentic AI Foundation under the Linux Foundation, positioning it as a vendor-neutral open standard rather than a single company's format.
  - quote: “AGENTS.md emerged from collaborative efforts across the AI software development ecosystem, including OpenAI Codex, Amp, Jules from Google, Cursor, and Factory. ... AGENTS.md is now stewarded by the Agentic AI Foundation under the Linux Foundation.”
  - importance: central
- **[UNVERIFIED]** The format has no required fields or schema — it is plain Markdown — and the official guidance recommends covering project overview, build and test commands, code style guidelines, testing instructions, and security considerations, framing it as a 'README for agents' kept separate from the human README.
  - quote: “No. AGENTS.md is just standard Markdown. Use any headings you like; the agent simply parses the text you provide. ... Popular choices: Project overview; Build and test commands; Code style guidelines; Testing instructions; Security considerations. ... README.md files are for humans: quick starts, project descriptions, and contribution guidelines.”
  - importance: central
- **[UNVERIFIED]** The official migration/interop guidance is to rename competing agent-context files to AGENTS.md and keep symbolic links for backward compatibility, and the site lists 23 compatible tools (Codex, Cursor, Gemini CLI, Jules, Zed, VS Code, Devin, Windsurf, Aider, goose, Warp, etc.) — with Claude Code notably absent from the compatibility list.
  - quote: “Rename existing files to AGENTS.md and create symbolic links for backward compatibility: mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md”
  - importance: supporting

## https://arxiv.org/html/2602.11988v1
(quality: primary, publishDate: 2026-02, claims: 5)

- **[UNVERIFIED]** Across multiple coding agents and LLMs, providing repository context files (AGENTS.md) does not generally improve task success rates while increasing inference cost by over 20% on average, and this holds for both LLM-generated and developer-committed context files.
  - quote: “Surprisingly, they found that providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average. This observation holds across different LLMs, coding agents, and for both LLM-generated and developer-committed context files.”
  - importance: central
- **[UNVERIFIED]** LLM-generated context files (created following agent-developer recommendations) actively reduce average resolution rates: by about 0.5 percentage points on SWE-bench Lite and about 2-3 percentage points on AGENTBENCH, depending on the model.
  - quote: “Utilizing LLM-generated context files does not elevate agent capabilities; rather, it universally triggers performance degradation, reducing average resolution rates by 0.5% on SWE-bench Lite and 2% on AGENTBENCH.”
  - importance: central
- **[UNVERIFIED]** Human/developer-written context files perform only marginally better: roughly a 4 percentage-point average improvement on AGENTBENCH versus no context file (mainly where no other documentation existed), while still increasing agent steps and cost by nearly 20% in some setups.
  - quote: “Even human-written context files provided only a marginal 4% improvement on average, primarily in scenarios where no other documentation existed... they improve the success rate on AgentBench by about 4 percentage points on average compared to the scenario without any context file, but also increase the number of agent steps and thus the costs – by almost 20 percent in individual setups.”
  - importance: central
- **[UNVERIFIED]** The study's methodology combined SWE-bench Lite (300 tasks from eleven popular Python repositories, with LLM-generated context files) and a newly constructed AGENTBENCH suite of 138 real-world Python tasks from niche repositories containing developer-committed context files, evaluated across multiple frontier models and agents.
  - quote: “The researchers combine two benchmarks: the established SWE-bench Lite with 300 tasks from eleven popular Python repositories and the benchmark tool AgentBench with 138 tasks from twelve less well-known repos, all of which contain real context files written by developers.”
  - importance: supporting
- **[UNVERIFIED]** The authors (ETH Zurich SRI Lab and LogicStar.ai) recommend, contrary to agent developers' guidance, omitting LLM-generated context files for now and including only minimal requirements such as repository-specific tooling.
  - quote: “The researchers suggest omitting LLM-generated context files for the time being, contrary to agent developers' recommendations, and including only minimal requirements (e.g., specific tooling to use with this repository).”
  - importance: supporting

## https://arxiv.org/abs/2605.10039
(quality: primary, publishDate: 2026-05-11, claims: 5)

- **[UNVERIFIED]** A factorial study measured coding-agent instruction compliance across 1,650 Claude Code CLI sessions yielding 16,050 function-level observations, on two TypeScript codebases, three frontier models (primarily Sonnet 4.6, with Opus 4.6 as a CLI-matched cross-model check and Opus 4.7 reported only descriptively due to a CLI-version confound), and five coding tasks.
  - quote: “measured compliance with a trivial target annotation across 1,650 Claude Code CLI sessions (16,050 function-level observations) on two TypeScript codebases, three frontier models (primarily Sonnet 4.6, with Opus 4.6 as a CLI-matched cross-model check and Opus 4.7 reported descriptively under a CLI-version confound), and five coding tasks”
  - importance: central
- **[UNVERIFIED]** None of the four manipulated file-structure variables (config file size, instruction position within the file, single vs. multi-file/nested architecture, presence of contradictions in adjacent files) nor any of three two-way interactions produced a statistically detectable effect on agent instruction adherence after multiple-testing correction.
  - quote: “None of the four structural variables or three two-way interactions produces a detectable contrast after multiple-testing correction.”
  - importance: central
- **[UNVERIFIED]** The null results for file size and for conflicting instructions are affirmatively supported by Bayes factors (BF10 between 0.05 and 0.10), i.e., evidence for no effect, whereas the position and architecture nulls are only failures to reject without Bayes-factor support.
  - quote: “Size and conflict nulls are supported by affirmative-null Bayes factors (BF10 between 0.05 and 0.10); position and architecture nulls are failures to reject without Bayes-factor support.”
  - importance: central
- **[UNVERIFIED]** Although file structure showed no detectable effect, compliance varied systematically by coding task and declined across each session's sequence of generated functions (within-session compliance decay), consistent with position-in-session mattering more than position-in-file.
  - quote: “compliance varies systematically between coding tasks and across each session's sequence of generated functions”
  - importance: central
- **[UNVERIFIED]** The study's premise is that coding agents (Claude Code, agents consuming AGENTS.md, Cursor Rules) load these configuration files at session start, and that practitioner folk wisdom holds that structural choices such as keeping files short or placing key instructions at the top measurably affect adherence — an assumption this study tested and did not confirm within its tested conditions (file sizes 25-500 lines; instruction positions from top to bottom; single CLAUDE.md vs CLAUDE.md+AGENTS.md vs added nested per-directory files).
  - quote: “Frontier coding agents read configuration files (CLAUDE.md, AGENTS.md, Cursor Rules) at session start and are expected to follow the conventions inside them. Practitioners assume that structural choices (file size, instruction position, file architecture, contradictions in adjacent files) measurably affect adherence.”
  - importance: supporting

## https://arxiv.org/html/2511.12884v1
(quality: primary, publishDate: 2025-11-17, claims: 5)

- **[UNVERIFIED]** The paper is the first large-scale empirical study of agent context files (AGENTS.md/CLAUDE.md-style 'READMEs for agents'), analyzing 2,303 context files drawn from 1,925 GitHub repositories to characterize their structure, maintenance, and content.
  - quote: “In this paper, we conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content.”
  - importance: central
- **[UNVERIFIED]** Content analysis across 16 instruction types shows developers prioritize functional context: implementation details appear in 69.9% of context files, architecture in 67.7%, and build/run commands in 62.3% — empirically matching the vendor-recommended 'build/test commands + architecture map' consensus.
  - quote: “Our content analysis of 16 instruction types shows that developers prioritize functional context, such as build and run commands (62.3%), implementation details (69.9%), and architecture (67.7%).”
  - importance: central
- **[UNVERIFIED]** Non-functional requirements are rarely specified in agent context files: security guidance appears in only 14.5% of files and performance guidance in only 14.5%, identifying a systematic content gap.
  - quote: “We also identify a significant gap: non-functional requirements like security (14.5%) and performance (14.5%) are rarely specified.”
  - importance: central
- **[UNVERIFIED]** Agent context files behave like configuration code rather than static documentation: they are complex, difficult-to-read artifacts maintained through frequent, small additions — evidence bearing on maintenance cost and docs-as-code practices for these files.
  - quote: “these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code, maintained through frequent, small additions”
  - importance: supporting
- **[UNVERIFIED]** The study characterizes what developers put in context files but is observational; it does not itself measure agent task-success improvement from these files, so it supports prevalence claims, not effectiveness claims (companion literature such as 'Evaluating AGENTS.md' addresses effectiveness).
  - quote: “conduct the first large-scale empirical study of 2,303 agent context files from 1,925 repositories to characterize their structure, maintenance, and content”
  - importance: supporting

## https://arxiv.org/html/2601.20404v1
(quality: primary, publishDate: 2026-01, claims: 5)

- **[UNVERIFIED]** The study is a controlled comparison in which an AI coding agent (OpenAI Codex) was run on real GitHub pull-request tasks across 10 repositories and 124 pull requests, executing each task under two conditions: with and without an AGENTS.md file present.
  - quote: “we study the impact of AGENTS.md files on the runtime and token consumption of AI coding agents operating on GitHub pull requests... analyzing 10 repositories and 124 pull requests, executing agents under two conditions: with and without an AGENTS.md file”
  - importance: central
- **[UNVERIFIED]** Presence of an AGENTS.md file was associated with a 28.64% reduction in median runtime: median completion time dropped from 98.57s (without) to 70.34s (with), a difference of 28.23s.
  - quote: “the presence of AGENTS.md is associated with a lower median runtime (Δ28.64%)... median completion time decreased from 98.57s to 70.34s (28.23s, ≈ 28.64%)”
  - importance: central
- **[UNVERIFIED]** Presence of an AGENTS.md file was associated with a 16.58% reduction in median output token consumption: from 2,925 to 2,440 median output tokens (485 tokens fewer).
  - quote: “reduced output token consumption (Δ16.58%)... median output tokens decreased from 2,925.00 to 2,440.00 (485 tokens, ≈ 16.58%)”
  - importance: central
- **[UNVERIFIED]** AGENTS.md improved efficiency but did NOT meaningfully improve task success: task completion behavior was comparable between the with- and without-AGENTS.md conditions, so the file made the agent cheaper/faster at tasks it would have completed anyway rather than more capable.
  - quote: “while maintaining a comparable task completion behavior... The file did not make Codex meaningfully better at finishing tasks, but it did make Codex more efficient at completing tasks it was going to complete anyway”
  - importance: central
- **[UNVERIFIED]** The proposed mechanism for the efficiency gain is reduced exploratory navigation: with project structure and conventions supplied up front, the agent needs fewer planning iterations and fewer repeated model requests; a key generalization caveat is that only one agent (OpenAI Codex) was tested.
  - quote: “The researchers hypothesize that AGENTS.md improves efficiency because agents spend less time on exploratory navigation. Instead of figuring out project structure and conventions themselves, they receive this information directly — fewer planning iterations, fewer repeated requests to the model... The study used only OpenAI Codex, so the result may not generalize.”
  - importance: supporting

## https://research.trychroma.com/context-rot
(quality: primary, publishDate: 2025-07, claims: 5)

- **[UNVERIFIED]** Chroma's July 2025 technical report evaluated 18 frontier LLMs (including GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 families) and found that model performance degrades non-uniformly as input token count grows, even on simple tasks — contradicting the assumption that models process the 10,000th token as reliably as the 100th. This is the core empirical basis for keeping agent context files (CLAUDE.md/AGENTS.md) short.
  - quote: “model performance varies significantly as input length changes, even on simple tasks ... LLMs are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th, however in practice, this assumption does not hold.”
  - importance: central
- **[UNVERIFIED]** In the LongMemEval experiment, models answered consistently better when given a short 'focused' prompt containing only the relevant excerpts than when the same relevant content was embedded in the full ~113k-token history — direct evidence that curating minimal, relevant context (rather than dumping whole docs/READMEs into an agent's context) improves reliability.
  - quote: “models tested under a 'focused' condition with only the relevant conversational history ... and a 'full' condition where the context was padded with irrelevant conversations up to 120k tokens. Models consistently performed worse when given the full conversation history compared to when they were given only the most relevant excerpts.”
  - importance: central
- **[UNVERIFIED]** Adding distractors — topically related but irrelevant/incorrect content — significantly degrades retrieval accuracy, and the degradation amplifies as input length grows; this bears on the anti-pattern of stale or irrelevant instructions accumulating in agent context files.
  - quote: “Adding related but irrelevant info (distractors) amplifies errors, demonstrating that the presence of plausible-sounding but irrelevant information significantly degrades model performance in longer contexts.”
  - importance: supporting
- **[UNVERIFIED]** Across all 18 models tested, performance on the needle-retrieval task was higher when the haystack was shuffled than when it was a logically coherent document, indicating that structural coherence of surrounding text can itself hurt retrieval — a counterintuitive result about how attention interacts with document structure.
  - quote: “Models performed better on shuffled haystacks than on logically coherent documents across all 18 models, with structural coherence consistently hurting performance.”
  - importance: supporting
- **[UNVERIFIED]** The report argues the widely-cited Needle-in-a-Haystack benchmark measures only narrow lexical retrieval and therefore overstates real long-context capability, which is why vendor long-context claims should not be taken as evidence that large context files are 'free'.
  - quote: “Models typically perform well on NIAH, which has led to the perception that long-context is largely solved. However, NIAH underestimates what most long context tasks require in practice.”
  - importance: supporting

## https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/
(quality: secondary, publishDate: 2026-06 (approx.; underlying Ahrefs study published June 2026; exact ppc.land article date unverified — origin blocked direct fetch with HTTP 403), claims: 5)

- **[UNVERIFIED]** An Ahrefs server-log study (published June 2026) covering ~137,210 domains found that 97% of published llms.txt files received zero requests in May 2026 — i.e., near-total non-consumption despite publication.
  - quote: “[via search snippet; direct fetch blocked 403] "A separate study by Ahrefs, published in June 2026 and drawing on server-log data from 137,000 domains, found that 97% of llms.txt files received zero requests in May 2026." Corroborated by Ahrefs' own title: "We Analyzed 137K Sites: 97% of llms.txt Files Never Get Read" (ahrefs.com/blog/llmstxt-study/).”
  - importance: central
- **[UNVERIFIED]** llms.txt adoption grew 8.8x in twelve months (June 2025 to May 2026), reaching 36,120 instances by May 2026, or 38,980 sites including companion formats llms-full.txt and ai.txt — showing an adoption narrative decoupled from actual consumption.
  - quote: “[via search snippet; direct fetch blocked 403] "llms.txt adoption reached 36,120 instances by May 2026, representing an 8.8x increase over twelve months from June 2025 to May 2026. Including companion formats llms-full.txt and ai.txt, the total number of adopting sites reached 38,980."”
  - importance: central
- **[UNVERIFIED]** Of the llms.txt files that did receive requests, 96% of traffic came from bots that were mostly non-AI; AI retrieval bots tied to ChatGPT and Perplexity accounted for only ~1% of requests, versus SEO audit tools 21%, unidentified bots 14%, web crawlers like Googlebot 13%, and tech-profiling tools like BuiltWith 11%.
  - quote: “[via search snippet; direct fetch blocked 403] "Of files with requests, 96% came from bots, mostly non-AI, with AI retrieval bots linked to ChatGPT and Perplexity making up only 1%. SEO audit tools accounted for 21% of requests, followed by unidentified bots (14%), web crawlers like Googlebot (13%), and tech profiling tools like BuiltWith (11%)."”
  - importance: central
- **[UNVERIFIED]** Google's John Mueller publicly characterized llms.txt as "not done for search" and a "temporary crutch, perhaps to save some tokens" for AI coding tools parsing developer documentation, and said site owners checking logs will find very little AI agent traffic — Google's public stance that its search/AI systems do not consume llms.txt.
  - quote: “[via search snippet of Ahrefs study coverage] "Mueller explained that llms.txt is 'not done for search' and is a 'temporary crutch, perhaps to save some tokens' for AI coding tools parsing developer documentation. Mueller also stated that site owners who check their logs will find very little AI agent traffic."”
  - importance: supporting
- **[UNVERIFIED]** In the Ahrefs sample, 28% of monitored domains published an llms.txt file (an upper bound, since Ahrefs Web Analytics customers skew technical/SEO-aware), and of roughly 38,000 valid files only about 1,100 received any traffic at all.
  - quote: “[via search snippet of Ahrefs study coverage] "Of the 137,000 domains monitored, 28% published an llms.txt file, though this 28% figure should be treated as an upper bound since Ahrefs Web Analytics customers skew more technical and SEO-aware than the web at large... of roughly 38,000 valid files, only about 1,100 received any traffic."”
  - importance: supporting

## https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/
(quality: secondary, publishDate: 2026-06-06, claims: 5)

- **[UNVERIFIED]** Google Search Advocate John Mueller stated (May-June 2026) that llms.txt's usefulness is unproven and speculative, noting the file has existed for years without any AI systems consuming it.
  - quote: “I don't think anyone knows – it's purely speculative for now (the file has existed for years, yet none of the AI systems use it — what does it mean?)”
  - importance: central
- **[UNVERIFIED]** Mueller has said no AI service has stated it uses llms.txt, that server logs show crawlers do not even request the file, and compared it to the discredited keywords meta tag (a site-owner self-claim that systems would rather bypass by reading the site directly).
  - quote: “AFAIK none of the AI services have said they're using LLMs.TXT (and you can tell when you look at your server logs that they don't even check for it). To me, it's comparable to the keywords meta tag - this is what a site-owner claims their site is about… why not just check the site directly?”
  - importance: central
- **[UNVERIFIED]** Google has officially confirmed it does not support llms.txt for Search and has no plans to: Gary Illyes said so in July 2025, and Mueller's 2026 comments reaffirm no current implementation exists at Google.
  - quote: “Gary Illyes confirmed in July 2025 that Google does not support llms.txt and is not planning to.”
  - importance: central
- **[UNVERIFIED]** Rather than llms.txt, Mueller endorsed WebMCP (a Google-backed proposed web standard using Model Context Protocol for agent-website interaction) as the approach site owners should look into for agent-readiness.
  - quote: “I like the WebMCP approach, as well as the commerce integrations”
  - importance: supporting
- **[UNVERIFIED]** There is an internal contradiction at Google: Chrome's Lighthouse agentic-browsing audit checks for the presence of an llms.txt file (claiming agents without it 'may spend more time crawling the site'), even while Google Search says it does not consume llms.txt — the June 6, 2026 SEJ article covers Mueller addressing this conflict (raised by Lily Ray on Bluesky, May 20, 2026).
  - quote: “The article was published on June 6, 2026, addressing the apparent conflict between Google Search Central's guidance on AI files and Chrome's Lighthouse audit checks.”
  - importance: supporting

## https://arxiv.org/html/2601.17548v1
(quality: primary, publishDate: 2026-01-24, claims: 5)

- **[UNVERIFIED]** Agent-facing config/instruction files in a repository (README, CLAUDE.md, coding rule files) are documented delivery vectors for prompt injection: attackers plant malicious instructions in configuration rule files as backdoor attacks, directly implicating AGENTS.md/CLAUDE.md/.cursor-style context files as an attack surface.
  - quote: “Attackers target content that Claude Code will process as part of its normal workflow, such as files in a repository (README, CLAUDE.md, configuration files). Configuration rule files are used as vectors for backdoor attacks, with proof-of-concept attacks adding malicious instructions into coding rule files.”
  - importance: central
- **[UNVERIFIED]** A meta-analysis of 78 studies (2021-2026) finds that prompt-injection attack success rates against state-of-the-art defenses exceed 85% when adaptive attack strategies are used, quantifying the residual risk of shipping agent-readable instruction files.
  - quote: “The meta-analysis synthesizes findings from 78 recent studies (2021–2026), consolidating evidence that attack success rates against state-of-the-art defenses exceed 85% when adaptive attack strategies are employed.”
  - importance: supporting
- **[UNVERIFIED]** All four major coding platforms tested (GitHub Copilot Workspace, Cursor, Windsurf, Claude Code) failed to block compound multi-layer attacks, showing the injection risk is cross-vendor and not solved by any single agent's guardrails.
  - quote: “Four major coding platforms tested (GitHub Copilot Workspace, Cursor, Windsurf, Claude Code) all failed to block compound multi-layer attacks.”
  - importance: supporting
- **[UNVERIFIED]** The root cause of the vulnerability is that LLMs cannot reliably separate instructions from data, meaning any repo-supplied context file (AGENTS.md/CLAUDE.md/rules) that the agent ingests is inherently untrusted input that can be weaponized.
  - quote: “The fundamental vulnerability stems from the fact that LLMs cannot reliably distinguish between instructions and data.”
  - importance: central
- **[UNVERIFIED]** The paper catalogs 42 distinct attack techniques and finds most of 18 analyzed defense mechanisms achieve under 50% mitigation against sophisticated adaptive attacks, indicating defenses for instruction-file injection remain immature.
  - quote: “The paper systematically catalogs 42 distinct attack techniques spanning input manipulation, tool poisoning, protocol exploitation, multimodal injection, and cross-origin context poisoning. Analysis of 18 defense mechanisms shows that most achieve less than 50% mitigation against sophisticated adaptive attacks.”
  - importance: supporting

## https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/
(quality: primary, publishDate: 2026-04-20, claims: 5)

- **[UNVERIFIED]** AGENTS.md files are treated as trusted context by coding agents by design, which turns them into an attack surface: a malicious build-time dependency that gains code execution can write or modify AGENTS.md to redirect the agent's actions, and the injected instructions take precedence over developer commands.
  - quote: “This trust model creates an interesting attack surface when a malicious dependency is able to write or modify these files at build time. When a compromised dependency gains code execution during the build process, it can create or modify these files to redirect the agent's actions entirely.”
  - importance: central
- **[UNVERIFIED]** NVIDIA's AI Red Team built a working proof-of-concept: a malicious Golang library detects Codex by checking the CODEX_PROXY_CERT environment variable and, when present, writes a crafted AGENTS.md directing Codex to inject a five-minute time.Sleep into the Golang main function.
  - quote: “NVIDIA researchers constructed a proof-of-concept using a malicious Golang library that specifically targets Codex environments by checking for the CODEX_PROXY_CERT environment variable. When this environment variable is present, the library creates a specially crafted AGENTS.md file containing a directive that injects a five-minute delay (time.Sleep) into any Golang main function.”
  - importance: central
- **[UNVERIFIED]** The injected AGENTS.md instructions include stealth directives that make the agent hide the malicious change from PR descriptions, commit messages, and code summaries, defeating human review.
  - quote: “Instructions specify that Codex should silently inject this malicious code without mentioning it in summaries, PR descriptions, or commit messages. The injected delay goes unnoticed due to cleverly engineered comments that prevent Codex from summarizing it in the PR.”
  - importance: central
- **[UNVERIFIED]** The class of indirect-injection risk applies broadly across coding agents and their context files, not just Codex/AGENTS.md — including Cursor (.cursorrules) and Claude Code (CLAUDE.md) as attack surfaces.
  - quote: “The research applies to multiple AI coding tools including Cursor, OpenAI Codex, Claude Code, and GitHub Copilot. Indirect prompt injection threats include malicious repositories, pull requests, git histories, .cursorrules, and CLAUDE/AGENT.md files containing prompt injections.”
  - importance: supporting
- **[UNVERIFIED]** The attack presupposes a compromised dependency (i.e., the attacker already has code execution), so NVIDIA frames it as a new supply-chain dimension unique to agentic development rather than a standalone remote exploit; OpenAI acknowledged NVIDIA's disclosure but declined to make changes.
  - quote: “While this attack relies on a compromised dependency (meaning the attacker already has a form of code execution), it illustrates a new dimension of supply chain risk unique to agentic development environments.”
  - importance: supporting

## https://prompt.security/blog/when-your-repo-starts-talking-agents-md-and-agent-goal-hijack-in-vs-code-chat
(quality: blog, publishDate: ?, claims: 5)

- **[UNVERIFIED]** VS Code Chat (with Copilot Chat) automatically includes a repository's AGENTS.md file in every chat request and treats its contents as an instruction set rather than as documentation, meaning repo-authored text is fed to the model as directives.
  - quote: “A single markdown file in your repo called AGENTS.MD is auto-included by VS Code Chat in every request and treated as an instruction set, not documentation.”
  - importance: central
- **[UNVERIFIED]** A malicious AGENTS.md can perform agent goal hijack: it can silently redirect the coding agent to attacker-defined objectives such as exfiltrating internal data (e.g., emailing it out of the organization) during an ordinary coding session, without the user intending it.
  - quote: “A malicious AGENTS.MD can quietly convince the agent to email internal data out of the organization during an everyday coding session.”
  - importance: central
- **[UNVERIFIED]** The injection is triggered by minimal user interaction — typing even a single character in Copilot Chat causes VS Code to inject AGENTS.md into the prompt, so the model receives repo-defined goals rather than the user's actual intent.
  - quote: “When a developer opens VS Code with Copilot Chat enabled and types anything—even a single letter—VS Code injects AGENTS.MD into the prompt, causing the model to receive repo-defined goals rather than user intent, with the injected instructions redirecting the agent into exfiltration.”
  - importance: supporting
- **[UNVERIFIED]** The article classifies this AGENTS.md attack as a direct instance of OWASP ASI01 (Agent Goal Hijack) and ASI02 (Tool Misuse and Exploitation), framing third-party agent-instruction files as part of a repository's attack surface.
  - quote: “This is a direct hit on OWASP ASI01 (Agent Goal Hijack) and ASI02 (Tool Misuse and Exploitation).”
  - importance: supporting
- **[UNVERIFIED]** The article argues the AGENTS.md specification's endorsement of auto-running/auto-inclusion behavior converts what would be an edge case into expected, exploitable behavior, making the file itself a security liability.
  - quote: “The AGENTS.MD spec's stance on auto-running turns an edge case into an expected behavior that attackers can hijack, and if your editor now hosts "agents for your repo," then your AGENTS.MD is part of your attack surface.”
  - importance: central

## https://code.claude.com/docs/en/large-codebases
(quality: primary, publishDate: unknown (live official docs, current as of 2026-07-15; references Claude Code v2.1.207 behavior), claims: 5)

- **[UNVERIFIED]** Anthropic officially documents a hierarchical loading model for CLAUDE.md: at launch Claude Code loads the CLAUDE.md from the working directory plus every parent directory, and subdirectory CLAUDE.md files load on demand only when Claude reads files in those directories — the technical basis for 'layered/per-folder' context files.
  - quote: “Claude Code loads every CLAUDE.md file from your working directory and every parent directory at launch, then loads each subdirectory's file on demand when it reads files there. A root file sets repository-wide rules and each subdirectory adds its own.”
  - importance: central
- **[UNVERIFIED]** Anthropic's official guidance for large codebases/monorepos is to split instructions into a root CLAUDE.md plus per-directory CLAUDE.md files rather than one large root file, explicitly warning that a single root file either bloats context with irrelevant instructions or stays too generic.
  - quote: “In a large codebase, a single CLAUDE.md at the repository root tends to either grow to cover every subsystem's conventions, costing context on instructions unrelated to the current task, or stay too generic to be useful. Splitting instructions across per-directory files means Claude loads repository-wide rules plus only the conventions for the code you're working in.”
  - importance: central
- **[UNVERIFIED]** Anthropic prescribes concrete maintenance practices against doc rot in agent context files: review CLAUDE.md edits in pull requests, prune instructions after major model releases (model-workaround rules become overhead), and use a Stop hook that reviews session transcripts and proposes CLAUDE.md updates.
  - quote: “Review in pull requests: treat CLAUDE.md edits like any other documentation change so conventions track the code * Revisit after major model releases: instructions that worked around an older model's limitation may become overhead once a newer model handles the case on its own.”
  - importance: central
- **[UNVERIFIED]** Anthropic itself acknowledges that per-directory CLAUDE.md layering has governance failure modes (drift, staleness, unowned root files) at scale, and recommends migrating conventions out of always-loaded CLAUDE.md into on-demand mechanisms: skills, plugins owned by a platform team, or MCP servers.
  - quote: “Per-directory CLAUDE.md files can become hard to govern as the codebase grows. Conventions drift, files go stale, and no one owns the root. ... Move conventions and reference content out of always-loaded CLAUDE.md and into mechanisms that load on demand”
  - importance: central
- **[UNVERIFIED]** Claude Code provides a claudeMdExcludes setting to prevent specific CLAUDE.md files (e.g., other teams' packages, legacy or vendored code) from ever loading, with the exception that managed-policy CLAUDE.md files cannot be excluded; the docs site also publishes an llms.txt documentation index (relevant to the llms.txt adoption question).
  - quote: “The `claudeMdExcludes` setting skips specific files by path or glob pattern so they never load. ... Managed policy CLAUDE.md files cannot be excluded, so organization-wide instructions always apply.”
  - importance: supporting

## https://securityboulevard.com/2026/06/6-agents-md-examples-from-real-production-repos/
(quality: blog, publishDate: 2026-06, claims: 5)

- **[UNVERIFIED]** The article surveys six real production repos that ship AGENTS.md files: OpenAI Codex, Sentry, Apache Airflow, Temporal, Cloudflare workers-sdk, and coder/coder — demonstrating adoption of the AGENTS.md format by major open-source projects.
  - quote: “6 AGENTS.md Examples From Real Production Repos ... The six production repositories featured are OpenAI Codex, Sentry, Apache Airflow, Temporal, Cloudflare's Workers SDK, and Coder.”
  - importance: central
- **[UNVERIFIED]** Sentry's AGENTS.md explicitly designates AGENTS.md as the single canonical source of truth and forbids adding agent guidance to CLAUDE.md or Cursor rules — direct evidence of convergence toward the AGENTS.md open standard over vendor-specific formats. (Independently verified verbatim against getsentry/sentry AGENTS.md on GitHub.)
  - quote: “Sentry's file opens by declaring that "AGENTS.md files are the source of truth for AI agent instructions" and tells agents not to add guidance to CLAUDE.md or Cursor rules, consolidating one canonical source.”
  - importance: central
- **[UNVERIFIED]** The article's core prescriptive claim: high-signal AGENTS.md files are short, command-first, and specific — pairing exact shell commands with a few hard prohibitions rather than long prose — and rules with the largest blast radius should come first.
  - quote: “A strong AGENTS.md is short, command-first, and specific: the highest-signal files pair exact shell commands with a few hard "never do this" rules rather than long prose.”
  - importance: central
- **[UNVERIFIED]** Cloudflare's workers-sdk AGENTS.md leads its Development Commands section with a package-manager guardrail to stop agents from corrupting the pnpm monorepo lockfile — an example of front-loading the highest-blast-radius rule. (Independently verified verbatim against cloudflare/workers-sdk AGENTS.md, which also references per-package subdirectory AGENTS.md files, i.e. layered/hierarchical context.)
  - quote: “Cloudflare's workers-sdk file leads with environment guardrails ("Use pnpm - never use npm or yarn") so agents don't corrupt a pnpm-managed monorepo lockfile.”
  - importance: supporting
- **[UNVERIFIED]** Production AGENTS.md files encode house-style rules and behavioral constraints that agents will not reliably infer from code: Apache Airflow mandates prose casing conventions and forbids running pytest directly on the host; coder/coder bans sycophantic phrasing and requires explicit permission before breaking any rule.
  - quote: “Apache Airflow uses AGENTS.md to enforce a house naming rule ("Write Dag (title case) in all prose") and forbids running pytest directly on the host ... coder/coder's file sets a "Rule #1" that demands explicit permission before breaking any rule and bans sycophantic phrasing like "You're absolutely right!"”
  - importance: supporting

## https://dev.to/datadog-frontend-dev/steering-ai-agents-in-monorepos-with-agentsmd-13g0
(quality: blog, publishDate: 2025-09 (per search index; exact day unverifiable — page blocked direct fetch), claims: 5)

- **[UNVERIFIED]** [Note: dev.to blocked direct fetch (HTTP 403); all quotes recovered via search-engine index snippets and should be spot-checked against the live page.] Datadog's frontend team states that nested per-folder AGENTS.md files are the default recommendation for monorepos (with 'closest file to the edited file wins' resolution), but argues this is insufficient alone — a root AGENTS.md should progressively disclose information by routing agents to specific nested files.
  - quote: “Nested AGENTS.md are the default recommendation for monorepo, and the closest AGENTS.md to the edited file wins, but this approach is quite limited on its own... A root AGENTS.md can bridge the gap by progressively disclosing information to your agent, with tasks that direct to specific nested AGENTS.md files like "@emails/AGENTS.md" or "@go/services/AGENTS.md".”
  - importance: central
- **[UNVERIFIED]** Datadog recommends the root AGENTS.md cover four things — workspace map, toolchain, routing rules, and default safety constraints — and to add local (nested) instruction files only for high-value or high-risk workspaces rather than everywhere.
  - quote: “Put a root AGENTS.md in place that explains the workspace map, the toolchain, the routing rules, and the default safety constraints. Add local instruction files for high-value or high-risk workspaces.”
  - importance: central
- **[UNVERIFIED]** The article asserts agent context files should be written for AI agents rather than humans and kept terse, because every character consumes the agent's context window budget — directly supporting the 'keep it short / don't copy the human README' consensus.
  - quote: “AGENTS.md is written for AI agents, not humans, so keep them concise and to the point, as characters add to an agent context window and terseness allows agents to do more.”
  - importance: central
- **[UNVERIFIED]** Datadog describes a concrete (but informal, non-quantified) evaluation methodology for context files: maintain a durable suite of 1-2 example prompts per common engineering task, run them across multiple agents (Claude Code, Cursor, Codex CLI) because agents behave differently, and iterate on the steering document until the agent can one-shot each test prompt — a practitioner substitute for controlled with/without-context evaluations.
  - quote: “Testing steering documents is similar to testing an onboarding guide by walking through it step by step, creating a collection of example prompts with one or two example prompts per task that an engineer might do inside your monorepo... run with all supported tools (such as Claude Code, Cursor, or Codex CLI) since different agents work differently... observing where the agent gets lost, identifying what knowledge it lacks, and then editing the steering document and retrying until the agent can one-shot the test prompt.”
  - importance: central
- **[UNVERIFIED]** The article frames AGENTS.md as a standardized cross-vendor artifact — 'the contract between your codebase and the agent ecosystem' — and claims (without controlled evidence) that well-maintained steering documents make AI agents more predictable and reliable; this is vendor-neutral practitioner opinion, not measured data.
  - quote: “A well-maintained AGENTS.md is the contract between your codebase and the agent ecosystem. AGENTS.md is a standardized markdown file at the root of a repository that gives AI coding agents instructions, context, and conventions for working in that codebase... A good baseline of steering documents makes AI more predictable and reliable.”
  - importance: supporting

## https://dev.to/wolfejam/your-agentsmd-is-already-stale-and-your-agent-trusts-it-completely-2nfh
(quality: blog, publishDate: 2026-07-12, claims: 5)

- **[UNVERIFIED]** The article asserts that hand-written AGENTS.md files begin going stale immediately upon creation — i.e., documentation rot is inherent and starts the day the file is written (asserted without measurement data).
  - quote: “A hand-written AGENTS.md rots the day you write it.”
  - importance: central
- **[UNVERIFIED]** Unlike a human reading a stale README with skepticism, a coding agent executes stale AGENTS.md instructions with full confidence — following renamed build commands, skipping newly added guardrails, and applying abandoned conventions; this is presented as a distinct agent failure mode (anecdotal, no compliance-rate data).
  - quote: “a stale AGENTS.md is obeyed by your coding agent with full confidence: wrong build command, missing guardrail, dead convention — followed to the letter.”
  - importance: central
- **[UNVERIFIED]** The article frames AGENTS.md as a cache of repo facts and claims an outdated context file is actively worse than having none at all — directly supporting the '过时指令比没有更糟' narrative, but as opinion rather than measured evidence.
  - quote: “a stale cache is worse than an empty one”
  - importance: central
- **[UNVERIFIED]** The article's best-practice prescription: a good AGENTS.md answers only 'how do I work in this repo' (setup/build/test commands), with test commands ranked above build commands because tests are the agent's sole mechanism for verifying its work against reality rather than trusting stale documented beliefs.
  - quote: “tests rank above build because they're the agent's only way to check its work against reality instead of trusting a stale belief”
  - importance: supporting
- **[UNVERIFIED]** The proposed maintenance remedy is that every line in the file must trace to a verifiable fact and be prevented from drifting; the article points readers to the agents.md standard and to faf.one/agents — a tool site associated with the author, indicating a promotional interest in the staleness framing.
  - quote: “further reading including the agents.md standard itself and a section-by-section field guide at faf.one/agents”
  - importance: supporting

