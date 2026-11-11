import pandas as pd, numpy as np, statsmodels.api as sm, sys, warnings
warnings.filterwarnings("ignore")
exec(open('ana.py').read().split("S=df[df.repo.isin")[0].replace("D=sys.argv[1]","D=sys.argv[1]"))
def fe(data,t,y,ctrl,fes,cl):
    w=data.copy()
    cols=[t,y]+ctrl
    for c in cols: w[c]=pd.to_numeric(w[c],errors='coerce')
    w=w.dropna(subset=cols+fes+[cl]).reset_index(drop=True)
    X=w[[t]+ctrl].astype(float); Y=w[y].astype(float)
    # alternating projections for multiple FEs
    Z=pd.concat([X,Y.rename('_y')],axis=1)
    for it in range(30 if len(fes)>1 else 1):
        for f in fes: Z=Z-Z.groupby(w[f]).transform('mean')
    r=sm.OLS(Z['_y'],Z[[t]+ctrl],hasconst=False).fit(cov_type='cluster',cov_kwds={'groups':pd.factorize(w[cl])[0]})
    ci=r.conf_int().loc[t]
    return f"b={r.params[t]*100:+.2f}pp [{ci[0]*100:+.2f},{ci[1]*100:+.2f}] p={r.pvalues[t]:.3f} N={len(w)}"
df['ym']=df.merged_at.dt.strftime('%Y-%m'); df['repo_ym']=df.repo+'|'+df.ym
S=df[df.repo.isin(szzrepos)]
JC=PSF
for t in ['T0','T1']:
  print('==',t)
  for lab,ctrl,fes,cl in [('repoFE+size, cl=repo',SIZE,['repo'],'repo'),
                          ('repoFE+JIT, cl=repo',PSF,['repo'],'repo'),
                          ('repo-month FE+JIT, cl=repo',PSF,['repo_ym'],'repo'),
                          ('authorFE+size, cl=author',SIZE,['author'],'author'),
                          ('authorFE+size, cl=repo',SIZE,['author'],'repo'),
                          ('authorFE+JIT, cl=author',PSF,['author'],'author'),
                          ('author+repo-month FE+JIT, cl=repo',PSF,['author','repo_ym'],'repo')]:
    print(f" {lab:38s} H1 {fe(S,t,'szz_buggy',ctrl,fes,cl)} | H2 {fe(df,t,'reworked',ctrl,fes,cl)}")
