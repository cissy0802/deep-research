import csv,collections as C,sys,statistics as S,math
r=list(csv.DictReader(open(sys.argv[1])))
f=lambda x,k: float(x[k]) if x[k]!='' else None
print('total=spec+build', sum(1 for x in r if int(x['total_minutes'])!=int(x['spec_minutes'])+int(x['build_minutes'])))
print('spec>45',sum(1 for x in r if int(x['spec_minutes'])>45),'build>45',sum(1 for x in r if int(x['build_minutes'])>45))
print('maxes', max(int(x['spec_minutes']) for x in r), max(int(x['build_minutes']) for x in r))
print('control spec_minutes', C.Counter(x['spec_minutes'] for x in r if x['arm']=='no_spec'))
print('stop', C.Counter((x['arm'],x['stop_reason']) for x in r))
# cost fit by least squares for claude-code arms: cost = a*in + b*out
import itertools
cc=[x for x in r if x['agent']=='claude-code']
def fit(rows):
  X=[(int(x['tokens_spec_in'] or 0)+int(x['tokens_build_in']), int(x['tokens_spec_out'] or 0)+int(x['tokens_build_out'])) for x in rows]
  y=[float(x['cost_usd']) for x in rows]
  sxx=sum(a*a for a,b in X); sxy=sum(a*b for a,b in X); syy=sum(b*b for a,b in X)
  sxc=sum(a*c for (a,b),c in zip(X,y)); syc=sum(b*c for (a,b),c in zip(X,y))
  det=sxx*syy-sxy*sxy; pa=(sxc*syy-syc*sxy)/det; pb=(syc*sxx-sxc*sxy)/det
  res=[c-(pa*a+pb*b) for (a,b),c in zip(X,y)]
  return pa*1e6,pb*1e6,max(abs(e) for e in res)
print('fit cc', fit(cc))
for a in ['spec_kit','bmad','openspec','no_spec']: print(a, fit([x for x in cc if x['arm']==a]))
print('decimals cost', C.Counter(len(x['cost_usd'].split('.')[1]) if '.' in x['cost_usd'] else 0 for x in r))
# last digits tokens
for k in ['tokens_spec_in','tokens_spec_out','tokens_build_in','tokens_build_out']:
  d=C.Counter(x[k][-1] for x in r if x[k]); print(k, sorted(d.items()))
  vals=[int(x[k]) for x in r if x[k]]; print('  min/max',min(vals),max(vals))
# correlation tokens vs minutes
def corr(a,b):
  ma,mb=S.mean(a),S.mean(b); return sum((x-ma)*(y-mb) for x,y in zip(a,b))/math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))
sp=[x for x in r if x['arm']!='no_spec']
print('corr spec_min vs spec tokens', corr([int(x['spec_minutes']) for x in sp],[int(x['tokens_spec_in']) for x in sp]))
print('corr build_min vs build_in', corr([int(x['build_minutes']) for x in r],[int(x['tokens_build_in']) for x in r]))
print('corr in vs out build', corr([int(x['tokens_build_in']) for x in r],[int(x['tokens_build_out']) for x in r]))
print('ratio out/in build', [round(int(x['tokens_build_out'])/int(x['tokens_build_in']),3) for x in r[:20]])
print('corr spec_lines vs spec_out', corr([int(x['spec_lines']) for x in sp],[int(x['tokens_spec_out']) for x in sp]))
print('corr merged vs completeness', corr([int(x['merged']) for x in sp],[int(x['spec_completeness']) for x in sp]))
print('defects dist', C.Counter((x['arm'],x['review_defects']) for x in r if x['merged']=='1'))
print('defects on unmerged', C.Counter(x['review_defects'] for x in r if x['merged']=='0'))
print('dev/drift', C.Counter((x['merged'],x['spec_deviations'],x['spec_drift']) for x in sp))
print('kiro credits', sorted(C.Counter(x['kiro_credits'] for x in r if x['arm']=='kiro').items()))
