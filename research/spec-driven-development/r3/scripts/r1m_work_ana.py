import pandas as pd, numpy as np, statsmodels.api as sm, sys, warnings
from scipy.stats import chi2, norm
warnings.filterwarnings("ignore")
D=sys.argv[1]
df=pd.read_csv(D+'/master-prs.csv',low_memory=False)
szz=pd.read_csv(D+'/szz-results-merged.csv'); jit=pd.read_csv(D+'/jit-features-merged.csv')
rc=pd.read_csv('reclass.csv')
df=df.merge(rc[['repo','pr_number','specd_fix']],on=['repo','pr_number'],how='left')
df['merged_at']=pd.to_datetime(df.merged_at,utc=True,errors='coerce')
for c in ['reworked','specd']: df[c]=df[c].fillna(False).astype(bool)
bp=szz[['repo','bug_pr_number']].drop_duplicates().rename(columns={'bug_pr_number':'pr_number'}); bp['szz_buggy']=True
df=df.merge(bp,on=['repo','pr_number'],how='left'); df['szz_buggy']=df.szz_buggy.fillna(False).astype(bool)
J=["ns","nd","nf","entropy","la","ld","lt","fix","ndev","age","nuc","exp","rexp","sexp"]
df=df.merge(jit[['repo','pr_number']+J],on=['repo','pr_number'],how='left')
df=df[~df.f_is_bot_author.fillna(False).astype(bool)].copy()
df['log_add']=np.log1p(df.additions); df['log_del']=np.log1p(df.deletions); df['log_files']=np.log1p(df.files_count)
df['T0']=df.specd.astype(int)
df['T1']=(df.specd & df.specd_fix.fillna(False).astype(bool)).astype(int)
df['fp']=(df.specd & ~df.specd_fix.fillna(False).astype(bool))
szzrepos=set(szz.repo.unique())
SIZE=['log_add','log_del','log_files']
PSF=SIZE+["ns","nd","nf","entropy","la","ld","lt","fix","ndev","age","nuc","exp","rexp"]

def wa(data,t,y,controls=SIZE):
    ac=data.author.value_counts(); m=data[data.author.isin(ac[ac>=2].index)].copy()
    cols=[t]+controls+[y]
    for c in cols: m[c]=pd.to_numeric(m[c],errors='coerce')
    m=m.dropna(subset=cols)
    dm=m[cols]-m.groupby('author')[cols].transform('mean')
    r=sm.OLS(dm[y],dm[[t]+controls],hasconst=False).fit(cov_type='cluster',cov_kwds={'groups':m.author})
    ci=r.conf_int().loc[t]
    return f"WA  b={r.params[t]*100:+.2f}pp [{ci[0]*100:+.2f},{ci[1]*100:+.2f}] p={r.pvalues[t]:.3f} N={len(m)}"

def psm(data,t,y,within_repo=False,seed=None):
    w=data.copy()
    for c in [t,y]+PSF: w[c]=pd.to_numeric(w[c],errors='coerce')
    w=w.dropna(subset=[t,y]+PSF).reset_index(drop=True)
    X=sm.add_constant(w[PSF].astype(float)); 
    if within_repo:
        X=pd.concat([X,pd.get_dummies(w.repo,drop_first=True,dtype=float)],axis=1)
    ps=(sm.GLM(w[t].astype(int),X,family=sm.families.Binomial()).fit() if within_repo else sm.Logit(w[t].astype(int),X).fit(disp=0,maxiter=200)).predict(X).clip(.01,.99)
    w['lps']=np.log(ps/(1-ps)); cal=0.05*w.lps.std()
    pairs=[]
    groups=[w] if not within_repo else [g for _,g in w.groupby('repo')]
    for g in groups:
        tr=g[g[t]==1].sort_values('lps'); ct=g[g[t]==0].sort_values('lps')
        cl=ct.lps.values; ci=ct.index.values; used=np.zeros(len(ci),bool)
        for ti,tl in zip(tr.index.values,tr.lps.values):
            lo=np.searchsorted(cl,tl-cal,'left'); hi=np.searchsorted(cl,tl+cal,'right')
            best=None;bd=1e9
            for i in range(lo,hi):
                if used[i]: continue
                d=abs(cl[i]-tl)
                if d<bd: bd=d;best=i
            if best is not None: used[best]=True; pairs.append((ti,ci[best]))
    a=w.loc[[p[0] for p in pairs],y].values.astype(int); b=w.loc[[p[1] for p in pairs],y].values.astype(int)
    rp=w.loc[[p[0] for p in pairs],'repo'].values
    d=a-b; n=len(d); diff=d.mean()
    B=((a==1)&(b==0)).sum(); C=((a==0)&(b==1)).sum()
    pm=chi2.sf((abs(B-C)-1)**2/(B+C),1)
    se=d.std(ddof=1)/np.sqrt(n)
    # repo-clustered SE of mean paired diff (cluster = treated PR's repo)
    dd=pd.DataFrame({'d':d,'r':rp}); 
    r=sm.OLS(dd.d,np.ones(n)).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(dd.r)[0]})
    cse=r.bse.iloc[0]
    return (f"PSM{'(within-repo)' if within_repo else ''} pairs={n} {a.mean()*100:.2f} vs {b.mean()*100:.2f} diff={diff*100:+.2f}pp "
            f"McNemar p={pm:.3f} | iid95%[{(diff-1.96*se)*100:+.2f},{(diff+1.96*se)*100:+.2f}] "
            f"| repo-cl95%[{(diff-1.96*cse)*100:+.2f},{(diff+1.96*cse)*100:+.2f}] p_cl={2*norm.sf(abs(diff/cse)):.3f} "
            f"| cross-repo pairs={(rp!=w.loc[[p[1] for p in pairs],'repo'].values).mean()*100:.0f}%")

S=df[df.repo.isin(szzrepos)]
mode=sys.argv[2] if len(sys.argv)>2 else 'main'
if mode=='main':
  for lab,d,t in [('orig',df,'T0'),('clean(FP->unspec)',df,'T1'),('drop FP PRs',df[~df.fp],'T0')]:
    s=d[d.repo.isin(szzrepos)]
    print(f"\n== {lab}: specd={int(d[t].sum())}")
    print(" H1 SZZ ",wa(s,t,'szz_buggy'))
    print(" H2 RW  ",wa(d,t,'reworked'))
    print(" H1 SZZ ",psm(s,t,'szz_buggy'))
    print(" H2 RW  ",psm(d,t,'reworked'))
elif mode=='repo':
  for lab,d,t in [('orig',df,'T0'),('clean',df,'T1')]:
    s=d[d.repo.isin(szzrepos)]
    print(f"\n== {lab} within-repo PSM")
    print(" H1 SZZ ",psm(s,t,'szz_buggy',within_repo=True))
    print(" H2 RW  ",psm(d,t,'reworked',within_repo=True))
