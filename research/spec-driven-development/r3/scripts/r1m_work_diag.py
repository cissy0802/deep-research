exec(open('ana.py').read().split("S=df[df.repo.isin")[0])
S=df[df.repo.isin(szzrepos)]
t='T0';y='szz_buggy'
w=S.copy()
for c in [t,y]+PSF: w[c]=pd.to_numeric(w[c],errors='coerce')
w=w.dropna(subset=[t,y]+PSF).reset_index(drop=True)
X=sm.add_constant(w[PSF].astype(float)); X=pd.concat([X,pd.get_dummies(w.repo,drop_first=True,dtype=float)],axis=1)
res=sm.Logit(w[t].astype(int),X).fit(disp=0,maxiter=300,method='lbfgs')
print('converged',res.mle_retvals.get('converged'))
res2=sm.GLM(w[t].astype(int),X,family=sm.families.Binomial()).fit()
for nm,ps in [('lbfgs',res.predict(X)),('glm',res2.predict(X))]:
  ps=ps.clip(.01,.99); lps=np.log(ps/(1-ps)); print(nm,'lps sd',lps.std(), 'coef fix', (res.params if nm=='lbfgs' else res2.params)['fix'])
# simple: exact repo + nearest neighbour on GLM ps
ps=res2.predict(X).clip(.01,.99); w['lps']=np.log(ps/(1-ps)); cal=0.05*w.lps.std()
pairs=[]
for _,g in w.groupby('repo'):
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
T=w.loc[[p[0] for p in pairs]]; C=w.loc[[p[1] for p in pairs]]
print('pairs',len(pairs),T[y].mean(),C[y].mean())
for c in PSF:
    sd=np.sqrt((w[w[t]==1][c].var()+w[w[t]==0][c].var())/2)
    print(f"{c:10s} SMD after {(T[c].mean()-C[c].mean())/sd:+.3f}")
