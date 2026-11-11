import csv,sys,collections as C
r=list(csv.DictReader(open(sys.argv[1])))
m=[x for x in r if x['noise_rerun']=='0']; n=[x for x in r if x['noise_rerun']=='1']
g={(x['ticket_id'],x['arm']):x for x in m}
for c in r[0]:
  same=sum(1 for x in n if g[(x['ticket_id'],x['arm'])][c]==x[c])
  print(f'{c:20s} identical {same}/50')
# The one changed merge
for x in n:
  o=g[(x['ticket_id'],x['arm'])]
  if o['merged']!=x['merged']: print('flip',x['ticket_id'],x['arm'],{k:(o[k],x[k]) for k in r[0] if o[k]!=x[k]})
# first-run merge status of rerun tickets per arm
print(C.Counter((x['arm'],g[(x['ticket_id'],x['arm'])]['merged']) for x in n))
# overall merge rate in rerun tickets vs others
rt=set(x['ticket_id'] for x in n)
for a in ['spec_kit','kiro','bmad','openspec','no_spec']:
  print(a, sum(int(x['merged']) for x in m if x['arm']==a and x['ticket_id'] in rt),'/10 rerun tickets;', sum(int(x['merged']) for x in m if x['arm']==a and x['ticket_id'] not in rt),'/40 others')
# engineer hours
h=C.Counter()
for x in r: h[x['engineer_id']]+=int(x['total_minutes'])
print({k:round(v/60,1) for k,v in h.items()}, round(sum(h.values())/60,1))
# spec_completeness vs merge
print(C.Counter((x['spec_completeness'],x['merged']) for x in m if x['arm']!='no_spec'))
