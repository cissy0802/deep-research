import csv,sys,statistics as S,math,collections as C
r=list(csv.DictReader(open(sys.argv[1])))
I=lambda x,k:int(x[k] or 0)
m=[x for x in r if x['noise_rerun']=='0']; n=[x for x in r if x['noise_rerun']=='1']
g={(x['ticket_id'],x['arm']):x for x in m}
print('rerun tickets', sorted(set(x['ticket_id'] for x in n)))
cols=['spec_minutes','build_minutes','tokens_spec_in','tokens_build_in','tokens_build_out','spec_lines','review_defects','cost_usd','rework_rounds','spec_completeness']
diffs=C.defaultdict(list)
for x in n:
  o=g[(x['ticket_id'],x['arm'])]
  for c in cols:
    a,b=float(o[c] or 0),float(x[c] or 0)
    if a: diffs[c].append((b-a)/a)
  diffs['merge_same'].append(o['merged']==x['merged']); diffs['eng'].append((int(o['engineer_id'][1]),int(x['engineer_id'][1])))
for c in cols: 
  v=diffs[c]; print(c, 'n',len(v),'mean rel diff %.3f sd %.3f maxabs %.3f'%(S.mean(v),S.pstdev(v),max(map(abs,v))) if v else '')
print('merge same',sum(diffs['merge_same']), 'eng shift', C.Counter((b-a)%5 for a,b in diffs['eng']))
print('rerun defects same', sum(1 for x in n if g[(x['ticket_id'],x['arm'])]['review_defects']==x['review_defects']))
# underdispersion of category merges
cats=['bug_fix','feature','refactor','data_pipeline','tests']
tot=0;df=0
for a in ['spec_kit','kiro','bmad','openspec','no_spec']:
  rows=[x for x in m if x['arm']==a]; p=sum(I(x,'merged') for x in rows)/50
  ch=sum((sum(I(x,'merged') for x in rows if x['category']==c)-10*p)**2/(10*p*(1-p)) for c in cats)
  print(a,'cat chi2 %.2f (df4)'%ch); 
  if a!='no_spec': tot+=ch; df+=4
print('spec arms pooled chi2',round(tot,2),'df',df)
# exact lower tail via simulation
import random
random.seed(1)
def sim(p):
  return sum(((sum(random.random()<p for _ in range(10)))-10*p)**2/(10*p*(1-p)) for _ in cats)
ps=[0.8,0.82,0.82,0.84]; obs=tot; N=200000
cnt=sum(1 for _ in range(N) if sum(sim(p) for p in ps)<=obs+1e-9)
print('P(pooled chi2 <= obs) under binomial', cnt/N)
# defects dispersion among merged
for a in ['spec_kit','kiro','bmad','openspec','no_spec']:
  d=[I(x,'review_defects') for x in m if x['arm']==a and x['merged']=='1']
  mu=S.mean(d); v=S.pvariance(d); print(a,'defects mean %.3f var %.3f VMR %.2f'%(mu,v,v/mu), C.Counter(d))
d=[I(x,'review_defects') for x in m if x['merged']=='0']; print('unmerged defects mean',S.mean(d))
# build tokens/minute
for a in ['spec_kit','kiro','bmad','openspec','no_spec']:
  s=[x for x in m if x['arm']==a]; q=[I(x,'tokens_build_in')/int(x['build_minutes']) for x in s]
  print(a,'build in tok/min mean %.0f cv %.3f'%(S.mean(q),S.pstdev(q)/S.mean(q)))
