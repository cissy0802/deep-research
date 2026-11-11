#!/bin/bash
# usage: m.sh owner/repo ; prints per-repo line + per-file lines
repo=$1; base=/tmp/claude-0/-home-user-deep-research/000f24b9-fbee-5fa6-8bbb-c9de969fb25d/scratchpad/r5x-clones
d=$base/$(echo $repo|tr / _)
timeout 150 git clone -q --filter=blob:none --no-checkout --single-branch https://github.com/$repo $d 2>/dev/null || { echo -e "R\t$repo\tCLONE_FAIL"; rm -rf $d; exit; }
cd $d
files=$(git ls-tree -r --name-only HEAD | grep -E '^specs/[^/]+/spec\.md$')
n=0; single=0
for f in $files; do c=$(git rev-list --count HEAD -- "$f"); n=$((n+1)); [ "$c" = 1 ] && single=$((single+1)); echo -e "F\t$repo\t$f\t$c"; done
# commit-level co-change: non-merge commits touching specs/
tot=0; co=0
for h in $(git rev-list --no-merges HEAD -- specs); do tot=$((tot+1)); if git diff-tree --no-commit-id --name-only -r $h | grep -vE '^(specs/|\.specify/|\.claude/|\.github/(prompts|agents)/|\.cursor/|\.gemini/|\.codex/|\.opencode/|\.windsurf/|\.kilocode/|\.roo/|\.agents?/)' | grep -vqE '\.md$'; then co=$((co+1)); fi; done 2>/dev/null
# fixed: grep -q inverted logic below handled in python; also output raw
lastspec=$(git log -1 --format=%cs -- specs); lastrepo=$(git log -1 --format=%cs)
after=$( [ -n "$lastspec" ] && git rev-list --count --no-merges --since="$lastspec 23:59" HEAD || echo NA)
echo -e "R\t$repo\t$n\t$single\t$tot\t$co\t$lastspec\t$lastrepo\t$after"
cd $base && rm -rf $d
