import csv,sys,statistics as S
r=list(csv.DictReader(open(sys.argv[1])))
m=[x for x in r if x['noise_rerun']=='0']
I=lambda x,k:int(x[k] or 0)
for a in ['spec_kit','kiro','bmad','openspec','no_spec']:
  s=[x for x in m if x['arm']==a]; mg=sum(I(x,'merged') for x in s)
  c=sum(float(x['cost_usd']) for x in s)
  tin=sum(I(x,'tokens_spec_in')+I(x,'tokens_build_in') for x in s); tout=sum(I(x,'tokens_spec_out')+I(x,'tokens_build_out') for x in s)
  uni=(tin*4.0+tout*18.0)/1e6
  print(a,'merged',mg,'cost/merged %.2f'%(c/mg),'uniform $4/$18 cost/merged %.2f'%(uni/mg),'per-ticket mean %.2f median %.2f'%(c/50,S.median(float(x['cost_usd']) for x in s)), 'ratio actual/uniform %.4f'%(c/uni))
sp=[x for x in m if x['arm'] not in('no_spec','kiro')]
print('spec CC median ticket cost',S.median(float(x['cost_usd']) for x in [x for x in m if x['arm']!='no_spec']))
