import csv,collections as C,sys
r=list(csv.DictReader(open(sys.argv[1])))
m=[x for x in r if x['noise_rerun']=='0']
print('eng==order', all(x['engineer_id'][1:]==x['arm_order'] for x in r))
arms=['spec_kit','kiro','bmad','openspec','no_spec']
T=sorted(set(x['ticket_id'] for x in m))
g={(x['ticket_id'],x['arm']):x for x in m}
# rotation pattern vs ticket idx
for t in T[:12]:
  print(t, g[(t,'no_spec')]['size_band'], g[(t,'spec_kit')]['arm_order'], ''.join(g[(t,a)]['merged'] for a in arms))
print('size per ticket idx within cat', C.Counter((int(t[2]), g[(t,'no_spec')]['size_band']) for t in T))
# merge matrix
print('ticket-level merge count dist', C.Counter(sum(int(g[(t,a)]['merged']) for a in arms) for t in T))
print('ticket-level spec merges dist', C.Counter(sum(int(g[(t,a)]['merged']) for a in arms[:4]) for t in T))
# merge by engineer, by order
for key in ['engineer_id']:
  print(key,{k:sum(int(x['merged']) for x in m if x[key]==k) for k in sorted(set(x[key] for x in m))})
# per arm per cat merges, per size
for a in arms:
  print(a, [sum(int(g[(t,a)]['merged']) for t in T if g[(t,a)]['category']==c) for c in ['bug_fix','feature','refactor','data_pipeline','tests']],
   [sum(int(g[(t,a)]['merged']) for t in T if g[(t,a)]['size_band']==s) for s in ['small','medium','large']])
# fails position within cat
for a in arms:
  print(a,'failed tickets',[t for t in T if g[(t,a)]['merged']=='0'])
