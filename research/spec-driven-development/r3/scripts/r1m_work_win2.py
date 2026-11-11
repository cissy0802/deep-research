exec(open('ana.py').read().split("S=df[df.repo.isin")[0])
df['m']=df.merged_at.dt.strftime('%y%m')
big=df.repo.value_counts().head(8).index
t=pd.crosstab(df[df.repo.isin(big)].repo,df[df.repo.isin(big)].m)
print(t.loc[:, '2504':'2604'].to_string())
# share of repos whose last-3-months share > 50%
rec=df.merged_at>=pd.Timestamp('2026-01-01',tz='UTC')
sh=df.groupby('repo').apply(lambda g:(g.merged_at>=pd.Timestamp('2026-01-01',tz='UTC')).mean())
print('repos with >50% of PRs in 2026-01..04-03 (~26% of window):',(sh>0.5).sum(),'/119; overall share',rec.mean())
