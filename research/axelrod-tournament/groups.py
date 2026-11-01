import json
def r(p, a, b): return [f"{p}{i:02d}" for i in range(a, b + 1)]
G = {
 "G01": ("第一届锦标赛口径:参赛、规则、得分、nice 与造王者、收益敏感性", ["O01","O02","O03","O04","O05","O07","O08","O13"]),
 "G02": ("流行细节:四行代码、从不赢单局、TF2T 反事实、参赛者事先知情", ["O06","O09","O10","O11","O12","O15","M18","M29"]),
 "G03": ("第二届口径与生态模拟:规模、终止规则、实际局长、代表性变体、fixation vs 14.5%、可复现性", ["O14","O16","O17","O18","O19","O22","O23","O24","O30","N30"]),
 "G04": ("四性质的出处与 Science 1981 稳定性主张;TFT 不是 ESS 之争", ["O20","O21","O25","O26","N01","N02","N03","N04","N05","N07"]),
 "G05": ("噪声:TFT 回声、Molander、Wu-Axelrod 1995 带噪重跑与生态模拟", ["O27","N08","N09","N10","N11","N18","N19","N20"]),
 "G06": ("慷慨与 WSLS:GTFT 上限、Nowak-Sigmund 1992/1993、有限群体循环、WSLS 弱点", r("N",12,17)+["N21","N22","N24","N25","N26","N27","N28","N29"]),
 "G07": ("理论挑不出 TFT:民间定理、Bendor-Swistak、Binmore 批评、partners/rivals", ["N06","N23","O28","Z23","Z24","Z26"]),
 "G08": ("零行列式原文与媒体放大", r("Z",1,12)+["Z28"]),
 "G09": ("零行列式的演化命运与人类实验", r("Z",13,22)+["Z25","Z27","M15"]),
 "G10": ("2004/2005 二十周年赛与南安普顿合谋", r("M",1,13)),
 "G11": ("现代大规模锦标赛:Axelrod-Python、Harper 2017、Glynatsi 2024、RSC 2015、Gradual", ["M14","M16","M17"]+r("M",19,28)+["M30","O29"]),
 "G12": ("人类实验室证据:Dal Bó-Fréchette、FRD 2012", r("E",1,10)),
 "G13": ("动物互惠证据与一战堑壕", r("E",11,25)),
 "G14": ("LLM 下场重复囚徒困境", r("E",26,32)),
}
idx = {}
for k in ["ORIGIN","NOISE","ZD","MODERN","EVIDENCE"]:
    for c in json.load(open(f"lines/{k}.json"))["claims"]:
        idx[c["id"]] = (k, c)
used = {i for _, ids in G.values() for i in ids}
print("unused:", sorted(set(idx) - used), "missing:", sorted(used - set(idx)))
def fmt(i):
    k, c = idx[i]
    return (f"## {i} ({k})\n- 论断:{c['claim']}\n- 原文:{c.get('quote','')}\n- URL:{c.get('source_url','')}\n"
            f"- 来源:{c.get('source_title','')} · {c.get('date','')} · {c.get('source_type','')} · {c.get('confidence','')}\n- 备注:{c.get('notes','')}\n")
for g, (title, ids) in G.items():
    open(f"groups/{g}.md", "w").write(f"# {g} {title}\n\n" + "\n".join(fmt(i) for i in ids))
json.dump({g: {"title": t, "ids": i} for g, (t, i) in G.items()}, open("groups/index.json", "w"), ensure_ascii=False, indent=1)
raw = ["# 01 Round 1 原始论断(5 线合并)\n"]
for k in ["ORIGIN","NOISE","ZD","MODERN","EVIDENCE"]:
    d = json.load(open(f"lines/{k}.json"))
    raw.append(f"\n# 线 {k}\n")
    raw += [fmt(c["id"]) for c in d["claims"]]
    raw.append("\n### 交叉口径问题\n" + "\n".join(f"- {q}" for q in d.get("open_questions", [])))
open("01-raw-claims.md", "w").write("\n".join(raw))
print({g: len(i) for g, (t, i) in G.items()})
