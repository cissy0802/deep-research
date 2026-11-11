exec(open('ana.py').read().split("S=df[df.repo.isin")[0])
S=df[df.repo.isin(szzrepos)]
print('merged_at max',df.merged_at.max(),'min',df.merged_at.min())
cut=pd.Timestamp('2026-02-26',tz='UTC')
late=df.merged_at>cut
print('share merged last ~30d',late.mean(),'spec rate late',df[late].T0.mean(),'early',df[~late].T0.mean())
print('rework rate late',df[late].reworked.mean(),'early',df[~late].reworked.mean())
d=df[~late]
print('H2 WA excl last30d T0',wa(d,'T0','reworked'),' T1',wa(d,'T1','reworked'))
# H3/H4 quality on clean spec'd only
sc=df[df.q_overall.notna()]
for lab,sub in [('all scored (author)',sc),('scored & T0',sc[sc.T0==1]),('scored & T1 clean',sc[sc.T1==1])]:
    print(lab,len(sub),'H3',wa(sub[sub.repo.isin(szzrepos)],'q_overall','szz_buggy'),'| H4',wa(sub,'q_overall','reworked'))
# FP share by fix flag
print(pd.crosstab(df.fix, df.T0, normalize='index'))
# per-repo base SZZ rate spread
r=S.groupby('repo').szz_buggy.mean(); print('SZZ rate across repos: min %.3f p10 %.3f median %.3f p90 %.3f max %.3f, zero-rate repos %d'%(r.min(),r.quantile(.1),r.median(),r.quantile(.9),r.max(),(r==0).sum()))
print('n repos in SZZ set with PRs',r.size)
