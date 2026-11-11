import pandas as pd, json, sys, glob, os
D=sys.argv[1]
df=pd.read_csv(D+'/master-prs.csv',low_memory=False)
df=df[~df.f_is_bot_author.fillna(False).astype(bool)]
s=df[df.specd.fillna(False).astype(bool)]
g=s.groupby(['repo','spec_source']).size().sort_values(ascending=False)
g=g[g>=10]
bodies={}
for (repo,src),n in g.items():
    if repo not in bodies:
        d=json.load(open(f"{D}/prs-{repo.replace('/','-')}.json"))
        bodies[repo]={p['pr_number']:(p.get('body') or '') for p in d}
    nums=s[(s.repo==repo)&(s.spec_source==src)].pr_number.tolist()
    b=bodies[repo].get(nums[0],'')
    i=b.find(src.rstrip(').'))
    print(f"\n### {repo} | {src!r} | n={n}")
    print(repr(b[max(0,i-200):i+80]))
