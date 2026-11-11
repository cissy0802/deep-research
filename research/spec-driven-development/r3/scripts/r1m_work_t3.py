import pandas as pd, sys
D=sys.argv[1]
df=pd.read_csv(D+'/master-prs.csv',low_memory=False)
rc=pd.read_csv('reclass.csv')
m=df.merge(rc,on=['repo','pr_number'],how='left')
m=m[~m.f_is_bot_author.fillna(False).astype(bool)]
m['specd']=m.specd.fillna(False).astype(bool)
print('nonbot',len(m),'specd orig',m.specd.sum(),'specd reimpl',m.specd_re.sum(),'fix',m.specd_fix.sum())
print(pd.crosstab(m.specd,m.specd_re))
print('src agree', (m.spec_source.fillna('')==m.src_re.fillna('')).mean())
print(pd.crosstab(m.specd,m.specd_fix))
fl=m[m.specd & ~m.specd_fix]
print('flipped to unspecd',len(fl), len(fl)/m.specd.sum())
print(fl.repo.value_counts().head(12))
print(fl.spec_source.value_counts().head(15))
# categorize
import re
def cat(s):
    s=str(s)
    if re.fullmatch(r"[A-Z]{2,10}-[A-Z]+",s): return 'hyphen-word'
    return 'template/comment'
print(fl.spec_source.map(cat).value_counts())
# changed sources but still specd
ch=m[m.specd & m.specd_fix & (m.src_re!=m.src_fix)]
print('still specd but different trigger', len(ch))
