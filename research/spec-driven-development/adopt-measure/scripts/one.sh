#!/bin/bash
kind=$1; repo=$2; base=/tmp/claude-0/-home-user-deep-research/000f24b9-fbee-5fa6-8bbb-c9de969fb25d/scratchpad/clones
d=$base/$kind-$(echo $repo|tr / _)
timeout 120 git clone -q --filter=blob:none --no-checkout --single-branch https://github.com/$repo $d 2>/dev/null || { echo -e "$kind\t$repo\tCLONE_FAIL"; exit; }
cd $d
case $kind in sk) tool='.specify'; sp='specs'; pat='^specs/[^/]+/spec\.md$';; kiro) tool='.kiro'; sp='.kiro/specs'; pat='^\.kiro/specs/[^/]+/requirements\.md$';; os) tool='openspec'; sp='openspec'; pat='^openspec/(specs|changes)/.+\.md$';; esac
nspec=$(git ls-tree -r --name-only HEAD | grep -cE "$pat")
first=$(git log --format=%cs --diff-filter=A -- $tool | tail -1)
lastspec=$(git log -1 --format=%cs -- $sp)
lasttool=$(git log -1 --format=%cs -- $tool)
lastrepo=$(git log -1 --format=%cs)
if [ -n "$first" ]; then
  tot=$(git rev-list --count --no-merges --since="$first" HEAD)
  specc=$(git rev-list --count --no-merges --since="$first" HEAD -- $sp)
  after=$( [ -n "$lastspec" ] && git rev-list --count --no-merges --since="$lastspec 23:59" HEAD || echo NA)
else tot=NA; specc=NA; after=NA; fi
echo -e "$kind\t$repo\t$nspec\t$first\t$lastspec\t$lasttool\t$lastrepo\t$tot\t$specc\t$after"
cd $base && rm -rf $d
