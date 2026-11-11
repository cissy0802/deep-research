import csv,collections as C,sys
r=list(csv.DictReader(open(sys.argv[1])))
m=[x for x in r if x['noise_rerun']=='0']; n=[x for x in r if x['noise_rerun']=='1']
print(len(m),len(n))
print('arm x engineer', C.Counter((x['arm'],x['engineer_id']) for x in m))
print('arm x order', C.Counter((x['arm'],x['arm_order']) for x in m))
print('rerun arm x eng', C.Counter((x['arm'],x['engineer_id']) for x in n))
# order of rows per ticket
seq=C.Counter()
for t in sorted(set(x['ticket_id'] for x in m)):
  rows=[x for x in m if x['ticket_id']==t]
  seq[tuple((x['arm'],x['arm_order'],x['engineer_id']) for x in rows)]+=1
for k,v in seq.most_common(10): print(v,k)
print(C.Counter((x['category'],x['size_band']) for x in m if x['arm']=='control'))
print('tickets by cat',[ (c,sorted(set(x['ticket_id'] for x in m if x['category']==c))) for c in sorted(set(x['category'] for x in m))])
print('size by ticket', [(x['ticket_id'],x['size_band']) for x in m if x['arm']=='control'])
