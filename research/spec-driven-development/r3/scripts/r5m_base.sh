#!/bin/bash
kind=$1; repo=$2; base=/tmp/claude-0/-home-user-deep-research/000f24b9-fbee-5fa6-8bbb-c9de969fb25d/scratchpad/r5m/clones
d=$base/b-$kind-$(echo $repo|tr / _)
timeout 120 git clone -q --filter=blob:none --no-checkout --single-branch https://github.com/$repo $d 2>/dev/null || { echo -e "$kind\t$repo\tCLONE_FAIL"; exit; }
cd $d
rd=$(git ls-tree --name-only HEAD | grep -iE '^readme(\.md|\.rst|\.txt)?$' | head -1)
lastrd=$( [ -n "$rd" ] && git log -1 --format=%cs -- "$rd")
lastrepo=$(git log -1 --format=%cs)
afterrd=$( [ -n "$lastrd" ] && git rev-list --count --no-merges --since-as-filter="$lastrd 23:59" HEAD || echo NA)
echo -e "$kind\t$repo\t$rd\t$lastrd\t$lastrepo\t$afterrd"
cd $base && rm -rf $d
