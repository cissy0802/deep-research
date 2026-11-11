import json
def r(p, a, b): return [f"{p}{i:02d}" for i in range(a, b + 1)]
LINES = ["PRO", "CON", "HIST", "VENDOR", "MEASURE", "FORMAL", "ADOPT"]
G = {
 "G01": ("LLM 计划先行(T2):Self-planning、MapCoder、Self-collaboration、SCoT、PlanSearch", r("P",1,9)+["P24"]),
 "G02": ("需求澄清(T1):ClarifyGPT、Ambig-SWE、HumanEvalComm、Ask or Assume", r("P",10,13)+["P25","P29","P31","M18"]),
 "G03": ("TiCoder 与测试入提示(T4)", r("P",14,19)+["P28"]),
 "G04": ("意图形式化 vs SDD:Lahiri、nl2postcond、Dafny 规约评估", ["P20","P21"]+r("F",9,13)),
 "G05": ("仓库级计划/流程:CodePlan、Spec Kit Agents、SWE-RPG、Google 规约驱动测试", ["P22","P23","P26","P27","P30","M20","M23"]),
 "G06": ("Hill ESEM 2026:设计、处理变量、选样与评审轨迹", r("C",1,3)+r("C",10,12)+["C15","C16"]),
 "G07": ("Hill ESEM 2026:H1–H5 结果、版本差与勘误", r("C",4,9)+["C13","C14","M29"]),
 "G08": ("SDD 文献引用链与转述失真", ["C17","C18"]),
 "G09": ("Böckeler 实操评测(Kiro/spec-kit/Tessl)", r("C",19,24)),
 "G10": ("Eberhardt(Scott Logic)与 Zaninotto(Marmelab)实操", r("C",25,31)),
 "G11": ("Spec Kit 用户 issue、幽灵完成、小型试点与成本断言", r("C",32,35)),
 "G12": ("Royce 1970 原文与「waterfall」一词考古", r("H",1,10)),
 "G13": ("专家论证:Brooks、Parnas、Dijkstra、Knuth", r("H",11,17)+["H34"]),
 "G14": ("Boehm 缺陷成本曲线与其溯源/反证", r("H",18,22)),
 "G15": ("UML/MDA/CASE 采用与衰落", r("H",23,28)),
 "G16": ("BDD 与 TDD 证据", r("H",29,33)),
 "G17": ("Spec Kit 厂商口径与自家 dogfooding", r("V",1,10)),
 "G18": ("OpenSpec、BMAD 与各家 plan mode", r("V",11,16)+r("V",29,32)),
 "G19": ("AWS Kiro:发布、用量、定价与客户案例", r("V",17,21)+["A31"]),
 "G20": ("Tessl、Grove「新代码」演讲与 Thoughtworks Radar", r("V",22,28)+["V33","V34","A09","M31"]),
 "G21": ("Uvik SDD benchmark", r("M",1,10)),
 "G22": ("单人对照、Rebuild Dossier 与门控流程个案", r("M",11,16)+r("M",24,28)),
 "G23": ("规约完整度的受控消融", ["M17","M19","M21","M22"]),
 "G24": ("#14/#0 已核口径的迁移", r("M",32,35)),
 "G25": ("Autoformalization 忠实率与形式基准题面错位", r("F",1,8)+["F34"]),
 "G26": ("LLM 生成形式规约:AutoCLRS、SpecGen、Verus、TLA+、Clover", r("F",14,24)+["F27"]),
 "G27": ("PBT、规约审阅成本与形式验证中的规约缺陷", ["F25","F26"]+r("F",28,33)),
 "G28": ("开发者调查(SO/JetBrains/DORA/Octoverse)", r("A",1,8)),
 "G29": ("GitHub 足迹与 SpecMine 普查", r("A",10,16)+["A28","A29","M30"]),
 "G30": ("装了≠用了:constitution 空模板、spec 活性与冻结", r("A",17,21)),
 "G31": ("弃用 PR 与弃用理由", r("A",22,27)),
 "G32": ("企业案例与话语场", ["A30"]+r("A",32,35)),
}
BATCH = {"B1": [f"G{i:02d}" for i in range(1, 9)], "B2": [f"G{i:02d}" for i in range(9, 17)],
         "B3": [f"G{i:02d}" for i in range(17, 25)], "B4": [f"G{i:02d}" for i in range(25, 33)]}
idx = {}
for k in LINES:
    for c in json.load(open(f"lines/{k}.json"))["claims"]:
        idx[c["id"]] = (k, c)
used = [i for _, ids in G.values() for i in ids]
print("unused:", sorted(set(idx) - set(used)), "missing:", sorted(set(used) - set(idx)), "dups:", sorted({i for i in used if used.count(i) > 1}))
def fmt(i):
    k, c = idx[i]
    return (f"## {i} ({k})\n- 论断:{c['claim']}\n- 原文:{c.get('quote','')}\n- URL:{c.get('source_url','')}\n"
            f"- 来源:{c.get('source_title','')} · {c.get('date','')} · {c.get('source_type','')} · {c.get('spec_type','')} · {c.get('design','')} · {c.get('confidence','')}\n- 备注:{c.get('notes','')}\n")
for g, (title, ids) in G.items():
    open(f"groups/{g}.md", "w").write(f"# {g} {title}\n\n" + "\n".join(fmt(i) for i in ids))
json.dump({"groups": {g: {"title": t, "ids": i} for g, (t, i) in G.items()}, "batches": BATCH}, open("groups/index.json", "w"), ensure_ascii=False, indent=1)
raw = ["# 01 Round 1 原始论断(7 线合并)\n",
       "> 运行约束:本会话网络策略拦截 arXiv/ACM/IEEE/Dagstuhl/martinfowler.com/uvik.net/厂商站点等;一手原文主要经 GitHub 仓库(作者仓库、LaTeX 源、复现包、博客源仓库)取得。confidence=secondhand 的条目 quote 为空,验证阶段优先回一手。\n"]
urls = set(); conf = {}
for k in LINES:
    d = json.load(open(f"lines/{k}.json"))
    raw.append(f"\n# 线 {k}\n")
    raw += [fmt(c["id"]) for c in d["claims"]]
    for c in d["claims"]:
        urls.add(c.get("source_url", "").split("#")[0].rstrip("/")); conf[c["confidence"]] = conf.get(c["confidence"], 0) + 1
    raw.append("\n### 搜索角度\n" + "\n".join(f"- {q}" for q in d.get("searched_angles", [])))
    raw.append("\n### 交叉口径问题\n" + "\n".join(f"- {q}" for q in d.get("cross_caliber_issues", [])))
open("01-raw-claims.md", "w").write("\n".join(raw))
print("claims", len(idx), "unique source URLs", len(urls), conf)
print({g: len(i) for g, (t, i) in G.items()})
