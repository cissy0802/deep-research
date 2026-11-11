import csv,sys,statistics as S,math,collections as C
r=list(csv.DictReader(open(sys.argv[1])))
def lstsq(X,y):
  k=len(X[0]); A=[[sum(a[i]*a[j] for a in X) for j in range(k)] for i in range(k)]; b=[sum(a[i]*c for a,c in zip(X,y)) for i in range(k)]
  # gauss
  M=[A[i]+[b[i]] for i in range(k)]
  for i in range(k):
    p=max(range(i,k),key=lambda q:abs(M[q][i])); M[i],M[p]=M[p],M[i]
    for q in range(k):
      if q!=i:
        f=M[q][i]/M[i][i]; M[q]=[u-f*v for u,v in zip(M[q],M[i])]
  c=[M[i][k]/M[i][i] for i in range(k)]
  res=[yy-sum(ci*xi for ci,xi in zip(c,x)) for x,yy in zip(X,y)]
  return [round(ci*1e6,4) for ci in c], max(map(abs,res))
I=lambda x,k:int(x[k] or 0)
cc=[x for x in r if x['agent']=='claude-code']
X=[[I(x,'tokens_spec_in'),I(x,'tokens_spec_out'),I(x,'tokens_build_in'),I(x,'tokens_build_out')] for x in cc]
y=[float(x['cost_usd']) for x in cc]
print('4coef all cc',lstsq(X,y))
for a in ['spec_kit','bmad','openspec']:
  s=[x for x in cc if x['arm']==a]
  print(a,lstsq([[I(x,'tokens_spec_in'),I(x,'tokens_spec_out'),I(x,'tokens_build_in'),I(x,'tokens_build_out')] for x in s],[float(x['cost_usd']) for x in s]))
s=[x for x in cc if x['arm']=='no_spec']
print('no_spec 2coef build only rows spec=0',lstsq([[I(x,'tokens_build_in'),I(x,'tokens_build_out')] for x in s if I(x,'tokens_spec_in')==0],[float(x['cost_usd']) for x in s if I(x,'tokens_spec_in')==0]))
print('no_spec spec tokens nonzero', sum(1 for x in s if I(x,'tokens_spec_in')>0))
# kiro tokens-implied
k=[x for x in r if x['arm']=='kiro']
print('kiro cost==credits*0.04', max(abs(float(x['cost_usd'])-0.04*int(x['kiro_credits'])) for x in k))
def corr(a,b):
  ma,mb=S.mean(a),S.mean(b); return sum((x-ma)*(y-mb) for x,y in zip(a,b))/math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))
tok=lambda x:sum(I(x,c) for c in ['tokens_spec_in','tokens_spec_out','tokens_build_in','tokens_build_out'])
print('kiro credits vs tokens corr', corr([int(x['kiro_credits']) for x in k],[tok(x) for x in k]))
print('kiro credits/ktok', [round(int(x['kiro_credits'])/tok(x)*1e4,3) for x in k[:15]])
for a in ['spec_kit','kiro','bmad','openspec']:
  s=[x for x in r if x['arm']==a]
  print(a,'corr spec_min~spec_in',round(corr([int(x['spec_minutes']) for x in s],[I(x,'tokens_spec_in') for x in s]),3),
   'build_min~build_in',round(corr([int(x['build_minutes']) for x in s],[I(x,'tokens_build_in') for x in s]),3),
   'spec_in~spec_out',round(corr([I(x,'tokens_spec_in') for x in s],[I(x,'tokens_spec_out') for x in s]),3))
  print('   tokens_spec_in / spec_min', S.mean(I(x,'tokens_spec_in')/int(x['spec_minutes']) for x in s), S.pstdev(I(x,'tokens_spec_in')/int(x['spec_minutes']) for x in s))
