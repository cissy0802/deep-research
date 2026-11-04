import json
def r(p, a, b): return [f"{p}{i:02d}" for i in range(a, b + 1)]
LINES = ["US", "INTL", "WINDFALL", "JOBLESS", "RENTIER", "VOICES", "META"]
G = {
 "G01": ("ORUS 劳动供给、时间使用与资助口径", r("U",1,7)+["U11","V04"]),
 "G02": ("ORUS 健康/政治/育儿;Stockton SEED;Baby's First Years", ["U08","U09","U10"]+r("U",12,17)),
 "G03": ("美国市级试点、AEI 汇总与 1970s 负所得税实验", r("U",18,23)+["M22","M23"]),
 "G04": ("Dauphin Mincome 与切罗基赌场分红", r("U",24,27)),
 "G05": ("芬兰 2017–18 基本收入试验", r("I",1,5)+["V15"]),
 "G06": ("肯尼亚 GiveDirectly 长期 UBI 与一般均衡", r("I",6,11)+["V14"]),
 "G07": ("Haushofer-Shapiro 及长期效应衰减", r("I",12,15)+r("M",12,17)),
 "G08": ("全民/永久项目:伊朗、阿拉斯加(劳动侧)与 PFD 法定设计", r("I",16,19)+["V23"]),
 "G09": ("高收入国家新证据与无对照试点:德国、巴塞罗那、安大略、纳米比亚、印度", r("I",20,22)+r("I",24,27)),
 "G10": ("低中收入国家劳动供给综述与 UBI 健康综述", ["I23"]+r("M",1,5)+["M18","M19"]),
 "G11": ("现金与主观福祉/精神健康 meta 及幸福测量口径", r("M",6,11)+["M20","M21"]+r("M",24,27)),
 "G12": ("彩票中奖者的劳动供给", r("W",1,9)),
 "G13": ("彩票中奖者的福祉、Brickman 1978 与「中奖后还工作吗」", r("W",10,16)+["J30"]),
 "G14": ("退休对健康/认知/精神健康的因果证据;失业者退休", r("W",17,24)+["J28"]),
 "G15": ("马林塔尔、潜在剥夺理论及其检验、SDT", r("J",1,10)+["J31"]),
 "G16": ("失业伤害的量级与收入/非收入分解", r("J",11,19)+["J29"]),
 "G17": ("情绪 vs 满意度、救济能补多少、社会规范", r("J",20,27)),
 "G18": ("食利国家理论与石油诅咒跨国实证", r("R",1,13)),
 "G19": ("税收-问责实验、动员与选举权、阿拉斯加政治、海湾调查", r("R",14,23)),
 "G20": ("AI 版论证(intelligence curse / gradual disempowerment)与 Amodei 表态", r("R",24,27)+["V09","V10","V11"]),
 "G21": ("科技领袖与倡导者的 UBI 口径", r("V",1,3)+r("V",5,8)+["V12","V13"]),
 "G22": ("对手方立法、民调与制度设计", r("V",16,22)+["V24"]),
}
BATCH = {"B1": [f"G{i:02d}" for i in range(1, 9)], "B2": [f"G{i:02d}" for i in range(9, 16)], "B3": [f"G{i:02d}" for i in range(16, 23)]}
idx = {}
for k in LINES:
    for c in json.load(open(f"lines/{k}.json"))["claims"]:
        idx[c["id"]] = (k, c)
used = [i for _, ids in G.values() for i in ids]
print("unused:", sorted(set(idx) - set(used)), "missing:", sorted(set(used) - set(idx)), "dups:", sorted({i for i in used if used.count(i) > 1}))
def fmt(i):
    k, c = idx[i]
    return (f"## {i} ({k})\n- 论断:{c['claim']}\n- 原文:{c.get('quote','')}\n- URL:{c.get('source_url','')}\n"
            f"- 来源:{c.get('source_title','')} · {c.get('date','')} · {c.get('source_type','')} · {c.get('design','')} · {c.get('confidence','')}\n- 备注:{c.get('notes','')}\n")
for g, (title, ids) in G.items():
    open(f"groups/{g}.md", "w").write(f"# {g} {title}\n\n" + "\n".join(fmt(i) for i in ids))
json.dump({"groups": {g: {"title": t, "ids": i} for g, (t, i) in G.items()}, "batches": BATCH}, open("groups/index.json", "w"), ensure_ascii=False, indent=1)
raw = ["# 01 Round 1 原始论断(7 线合并)\n"]
urls = set()
for k in LINES:
    d = json.load(open(f"lines/{k}.json"))
    raw.append(f"\n# 线 {k}\n")
    raw += [fmt(c["id"]) for c in d["claims"]]
    urls |= {c.get("source_url", "").split("#")[0].rstrip("/") for c in d["claims"]}
    raw.append("\n### 交叉口径问题\n" + "\n".join(f"- {q}" for q in d.get("open_questions", [])))
open("01-raw-claims.md", "w").write("\n".join(raw))
print("claims", len(idx), "unique source URLs", len(urls))
print({g: len(i) for g, (t, i) in G.items()})
