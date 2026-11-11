import csv,sys,math,random,statistics as st
from datetime import date
R=[r for r in csv.reader(open(sys.argv[1]),delimiter='\t')]
def d(s): return date.fromisoformat(s) if s else None
def wil(k,n,z=1.96):
    if n==0: return (float('nan'),)*2
    p=k/n; den=1+z*z/n; c=(p+z*z/(2*n))/den; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den; return (round(c-h,3),round(c+h,3))
NOW=date(2026,11,11)
for k in ['sk','kiro','os']:
    rows=[r for r in R if r[0]==k]
    n=len(rows)
    nspec=[int(r[2]) for r in rows]
    z=sum(1 for x in nspec if x==0)
    print(f"\n== {k} n={n} nspec0={z} {z/n:.3f} CI{wil(z,n)} median={st.median(nspec)}")
    # bootstrap median
    random.seed(1); bs=sorted(st.median(random.choices(nspec,k=n)) for _ in range(5000)); print(" median nspec boot95",bs[125],bs[4875])
    sh=[]
    for r in rows:
        tot,specc=r[7],r[8]
        if tot not in('NA','') and int(tot)>0: sh.append(int(specc)/int(tot))
    bs=sorted(st.median(random.choices(sh,k=len(sh))) for _ in range(5000))
    print(f" share n={len(sh)} median={st.median(sh):.3f} boot95 [{bs[125]:.3f},{bs[4875]:.3f}] zero-share={sum(1 for x in sh if x==0)}")
    # freeze variants
    def frz(r,A=20,G=60,mode='repo'):
        if r[9] in('NA',''): return False
        ls=d(r[4]); lr=d(r[6])
        gap=(lr-ls).days if mode=='repo' else (NOW-ls).days
        return int(r[9])>=A and gap>=G
    havespec=[r for r in rows if r[9] not in('NA','')]
    for A,G,m in [(20,60,'repo'),(20,60,'now'),(10,30,'repo'),(10,60,'repo'),(20,90,'repo'),(50,60,'repo'),(5,30,'repo'),(20,0,'repo')]:
        kk=sum(frz(r,A,G,m) for r in rows)
        print(f" freeze A>={A} gap>={G}({m}): {kk}/{n}={kk/n:.3f} CI{wil(kk,n)} | among spec-having {kk}/{len(havespec)}")
    # eligible: repos where lastspec <= NOW-60 ... and active (lastrepo>=?) 
    fr=[r for r in rows if frz(r)]
    # censoring: repos whose tool first-add within 60d of lastrepo cannot be frozen
    young=sum(1 for r in rows if r[3] and (d(r[6])-d(r[3])).days<60)
    print(" repos with tool-age (lastrepo-first)<60d (cannot be frozen):",young)
    elig=[r for r in havespec if (d(r[6])-d(r[3])).days>=60]
    kk=sum(frz(r) for r in elig); print(f" freeze among eligible spec-having & age>=60d: {kk}/{len(elig)} CI{wil(kk,len(elig))}")
    # nspec=0 but after? also: lastspec==first (spec dir only touched at install?)
    print(" frozen repos:",[(r[1],r[2],r[3],r[4],r[6],r[7],r[8],r[9]) for r in fr])
    # stale 3 months
    for cut in [date(2026,8,11),date(2026,8,13)]:
        s=sum(1 for r in rows if d(r[6])<cut); print(f" stale lastrepo<{cut}: {s}/{n} {s/n:.3f} CI{wil(s,n)}")
    # first-add dates
    fd=sorted(d(r[3]) for r in rows if r[3]); print(" tool first-add range",fd[0],fd[len(fd)//2],fd[-1])
