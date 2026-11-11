import itertools, math
rows={'Baseline':([3.21,3.75,3.65,3.30,3.25],3.46),'Augmented':([3.58,3.56,3.31,3.45,3.55],3.50),
'Full':([3.10,3.35,3.90,3.48,3.61],3.51),'FullAug':([3.52,3.44,4.00,3.64,3.69],3.66)}
cols=['FastAPI','Airflow','Dexter','Plausible','Strapi']
for k,(v,o) in rows.items(): print(k,'unweighted mean %.4f'%(sum(v)/5),'reported',o)
sols=[]
for n in itertools.product(range(1,20),repeat=5):
    if sum(n)!=32: continue
    ok=all(abs(round(sum(a*b for a,b in zip(n,v))/32,2)-o)<1e-9 for v,o in rows.values())
    # allow +-0.005 tolerance via inputs rounding
    ok2=all(abs(sum(a*b for a,b in zip(n,v))/32-o)<=0.005+0.005 for v,o in rows.values())
    if ok2: sols.append((n,ok))
print('n weight vectors consistent (tol 0.01):',len(sols))
cons=[s for s in sols if s[0][2]>=5 and s[0][0]>=5 and s[0][1]>=5 and s[0][3]>=5 and s[0][4]>=7]
print('consistent & >= Table6 min ids (5,5,5,5[pla-05],7[str-07]):',cons[:20], len(cons))
# per-repo sign Baseline vs Full
b=rows['Baseline'][0]; f=rows['Full'][0]
print('Full-Baseline per repo',[round(y-x,2) for x,y in zip(b,f)])
# sign test human 19 vs 8
def binom2(k,n):
    p=sum(math.comb(n,i) for i in range(0,k+1))/2**n
    return min(1,2*p)
print('sign test 8 of 27 two-sided p=%.4f'%binom2(8,27))
# SWE-bench Lite granularity
for p in (56.5,58.2): print(p, [ (k, round(100*k/300,2)) for k in range(int(p*3)-1,int(p*3)+3)])
# power: paired n=32, SD diff assumptions
for sd in (0.3,0.5,0.7):
    se=sd/math.sqrt(32); print('sd_diff',sd,'SE %.3f  95%%CI half %.3f  MDE(80%%) %.3f'%(se,1.96*se,2.80*se))
for sd in (0.3,0.5,0.7):
    se=sd/math.sqrt(16); print('n=16 sd_diff',sd,'MDE %.3f'%(2.8*se))
print('---- all consistent vectors')
for s in sols: 
    n=s[0]; print(n,'exact-round' if s[1] else '', [round(sum(a*b for a,b in zip(n,v))/32,4) for v,o in rows.values()])
