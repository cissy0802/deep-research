import csv,sys,random,collections as C
r=list(csv.DictReader(open(sys.argv[1])))
m=[x for x in r if x['noise_rerun']=='0']
g={(x['ticket_id'],x['arm']):int(x['merged']) for x in m}
cat={x['ticket_id']:x['category'] for x in m}
T=sorted(cat); cats=sorted(set(cat.values()))
arms=['spec_kit','kiro','bmad','openspec']
random.seed(7); N=200000
for a in arms:
  others=[b for b in arms if b!=a]
  # p_t from other spec arms, smoothed (k+0.5)/(n+1)
  p={t:(sum(g[(t,b)] for b in others)+0.5)/(len(others)+1) for t in T}
  obs=[sum(g[(t,a)] for t in T if cat[t]==c) for c in cats]
  # stat: number of categories equal to their own... use variance of cat counts
  def var(v): mu=sum(v)/len(v); return sum((x-mu)**2 for x in v)
  ov=var(obs); hit=0; all8=0
  for _ in range(N):
    s=[sum(random.random()<p[t] for t in T if cat[t]==c) for c in cats]
    if var(s)<=ov+1e-9: hit+=1
    if s==obs: all8+=1
  print(a,obs,'P(var<=obs | ticket difficulty from other spec arms)=%.4f'%(hit/N),'P(exact same vector)=%.4f'%(all8/N))
# simple binomial with reestimated p for spec kit all equal
hit=0
for _ in range(N):
  s=[sum(random.random()<0.8 for _ in range(10)) for c in cats]
  if len(set(s))==1: hit+=1
print('binomial p=.8 P(all 5 cats equal any value)=',hit/N)
