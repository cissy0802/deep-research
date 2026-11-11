# Reimplementation of Hill's spec classifier (tools/spec_signals/coverage.py @a23d38a) + fixed variant
import re, json, sys, glob, pandas as pd
D=sys.argv[1]
FP={"UTF","SHA","TLS","SSL","HTTP","TCP","UDP","ISO","RFC","IEEE","AES","RSA","CWE","CVE","GPT","AI","CSS","LICENSE","NEXT","CLA","WIP","GPU","GHSA"}
TP=[re.compile(r"[A-Z]{2,10}-\d+"),re.compile(r"(?<!\w)#(\d+)\b"),re.compile(r"(?:fixes|closes|resolves)\s+#(\d+)",re.I),re.compile(r"[A-Z]{2,10}-[a-z0-9]+")]
URL_RE=re.compile(r"https?://\S+")
SECTION_RE=re.compile(r"^##\s*(?:Spec|Requirements|Acceptance\s+Criteria)",re.M|re.I)
PH={"tbd","todo","n/a","na","none","yes","done","see above","[fill in]","fill in","placeholder"}
PH_RE=re.compile(r"^\s*(?:"+"|".join(re.escape(p) for p in sorted(PH,key=len,reverse=True))+r")\s*$",re.I)
HC=re.compile(r"<!--.*?-->",re.S)
HDR=re.compile(r"^#{1,6}\s")
SPEC_URL=re.compile(r"(?:notion\.so|notion\.site|confluence|atlassian\.net|docs\.google\.com|linear\.app|jira|shortcut\.com|github\.com/[^/]+/[^/]+/issues/)",re.I)
SPEC_EX=re.compile(r"issues/new|issues/choose|/issues/new\b",re.I)
CKW=re.compile(r"(?:fix|fixes|closed?|closes|resolves?|references|refs|related?\s+to)\s+#(\d+)",re.I)
# verified template strings (checked against PR bodies; not inside HTML comments)
TEMPLATE_STR=["https://github.com/kubernetes/enhancements/issues/<kep-issue-number>",
 "https://docs.google.com/document/d/1YyVqrgX4gHTtrstbq8oWUImOyPCKSGnJ7xtTpmXzlRs",  # vllm release-notes doc in checklist
 "https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Improvement+Proposal", # airflow template
 "https://issues.apache.org/jira/projects/FLINK/issues", # flink template checklist
]
def tickets(t):
    ids=set()
    for p in TP:
        for m in p.finditer(t):
            c=m.group(1) if p.groups and m.group(1) else m.group(0)
            n=c.upper()
            if n.isdigit(): n="#"+n
            ids.add(n)
    return ids
def section(body):
    m=SECTION_RE.search(body)
    if not m: return False
    st=m.end(); nh=re.search(r"^##\s",body[st:],re.M)
    c=body[st:st+nh.start()] if nh else body[st:]
    c="\n".join(l for l in c.splitlines() if not HDR.match(l)).strip()
    c=HC.sub("",c).strip()
    if not c: return False
    s=c.strip().lower()
    lines=[l.strip().lower() for l in c.splitlines() if l.strip()]
    if s in PH or all(l in PH or PH_RE.fullmatch(l) for l in lines): return False
    return len(c.split())>=20
def detect(text, sections, fixed):
    if not text.strip() or text.strip().lower()=="no description provided": return False,None
    if sections and section(text): return True,"template section"
    if fixed:
        text=HC.sub("",text)
        for s in TEMPLATE_STR: text=text.replace(s,"")
    cl="\n".join(l for l in text.splitlines() if not l.strip().startswith(">"))
    ctx={m.group(1) for m in CKW.finditer(cl)}
    for tid in sorted(tickets(cl)):
        if tid.startswith("#"):
            if tid[1:] not in ctx: continue
        elif "-" in tid:
            pre,suf=tid.split("-",1)
            if pre in FP: continue
            if fixed and not any(ch.isdigit() for ch in suf): continue   # hyphenated word, e.g. CPU-ONLY
        return True,tid
    for m in URL_RE.finditer(cl):
        u=m.group()
        if SPEC_URL.search(u) and not SPEC_EX.search(u): return True,u
    return False,None
def classify(pr,fixed):
    s,src=detect(pr.get('body') or "",True,fixed)
    if not s: s,src=detect(pr.get('title') or "",False,fixed)
    return s,src
rows=[]
for f in sorted(glob.glob(D+"/prs-*.json")):
    for pr in json.load(open(f)):
        a=classify(pr,False); b=classify(pr,True)
        rows.append((pr['repo'],pr['pr_number'],a[0],a[1],b[0],b[1]))
out=pd.DataFrame(rows,columns=['repo','pr_number','specd_re','src_re','specd_fix','src_fix'])
out.to_csv(sys.argv[2],index=False)
print(len(out))
