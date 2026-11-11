exec(open('ana.py').read().split("S=df[df.repo.isin")[0])
g=df.groupby('repo').agg(n=('pr_number','size'),first=('merged_at','min'),last=('merged_at','max'),p10=('merged_at',lambda x:x.quantile(.1)))
g['span_days']=(g['last']-g['first']).dt.days; g['span10']=(g['last']-g['p10']).dt.days
print(g.n.describe()); print(g.span_days.describe()); print('repos with span<120d',(g.span_days<120).sum(),'<60d',(g.span_days<60).sum())
print(g.sort_values('span_days').head(15)[['n','span_days','span10']])
print(df.merged_at.dt.to_period('M').value_counts().sort_index().tail(16))
print('PRs merged before 2025-03-28', (df.merged_at<pd.Timestamp('2025-03-28',tz='UTC')).sum())
