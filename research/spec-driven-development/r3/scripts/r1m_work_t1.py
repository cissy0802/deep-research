import pandas as pd, sys
D=sys.argv[1]
df=pd.read_csv(D+'/master-prs.csv',low_memory=False)
df=df[~df.f_is_bot_author.fillna(False).astype(bool)]
s=df[df.specd.fillna(False).astype(bool)]
print(len(df),len(s))
vc=s.spec_source.value_counts()
print(vc.head(40))
for v in vc.index[:25]:
    print(repr(v), s[s.spec_source==v].repo.value_counts().head(3).to_dict())
print(s.classification.value_counts().head(20))
