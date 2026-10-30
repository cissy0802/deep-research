import json
G = {
 "G01": ("「约 70% 事故来自变更」的出处与口径;其他机构的变更占比", ["CHANGE:C01","CHANGE:C02","CHANGE:C08","CHANGE:C09","CHANGE:C19","CHANGE:C26","CHANGE:C28","CHANGE:C29","CANARY:C11"]),
 "G02": ("事故由谁发现:自动监控 vs 人/客户;漏检主因", ["CHANGE:C04","CHANGE:C05","CHANGE:C07","CHANGE:C20","DETECT:D17","DETECT:D18","DETECT:D19"]),
 "G03": ("公开复盘时间线:检测时间、发现来源、缓解时间(逐案)", ["POSTMORTEM:C3","POSTMORTEM:C4","POSTMORTEM:C5","POSTMORTEM:C6","POSTMORTEM:K1","POSTMORTEM:K2","POSTMORTEM:K3","POSTMORTEM:K4","POSTMORTEM:K5","POSTMORTEM:K6","POSTMORTEM:K7","POSTMORTEM:K8","CANARY:C23","CHANGE:C24"]),
 "G04": ("全局配置/数据推送绕过渐进发布;canary 的结构性盲区(复盘证据)", ["POSTMORTEM:C1","POSTMORTEM:C2","POSTMORTEM:C7","POSTMORTEM:C8","POSTMORTEM:C8b","CANARY:C22","CANARY:C24","CANARY:C30","CANARY:C31","CANARY:C32","CHANGE:C23","CHANGE:C25"]),
 "G05": ("Microsoft Gandalf 的检出率、精度、召回与检测时间", ["CANARY:C01","CANARY:C02","CANARY:C03","CANARY:C04","CANARY:C05","DETECT:D20","DETECT:D21","CHANGE:C11"]),
 "G06": ("Google CAS / Kayenta / SRE workbook:canary 判定方法与局限", ["CANARY:C06","CANARY:C07","CANARY:C08","CANARY:C09","CANARY:C10","CANARY:C12","CANARY:C13","CANARY:C14","CANARY:C15"]),
 "G07": ("Netflix 序贯检验与 Facebook/Amazon/Azure 渐进发布实践;MDE 以下的累积回退", ["CANARY:C16","CANARY:C17","CANARY:C18","CANARY:C19","CANARY:C21","CANARY:C25","CANARY:C26","CHANGE:C10","CHANGE:C21"]),
 "G08": ("Meta FBDetect / ServiceLab 的检出能力、误报与漏报口径", ["DETECT:D01","DETECT:D02","DETECT:D03","DETECT:D04","DETECT:D05","DETECT:D06","DETECT:D07","DETECT:D08","DETECT:D28"]),
 "G09": ("时序异常检测评测的系统性高估(point-adjust、基准缺陷、基础模型/LLM)", ["DETECT:D09","DETECT:D10","DETECT:D11","DETECT:D12","DETECT:D13","DETECT:D14","DETECT:D15","DETECT:D16"]),
 "G10": ("低底率、告警信任与人工推翻:检测快不等于处置", ["DETECT:D24","DETECT:D26","DETECT:D27","CANARY:C29","CANARY:C05","CANARY:C08"]),
 "G11": ("学术坏变更检测器的自报成绩与复现(SCWarn、SCELM、Walmart)", ["CHANGE:C28","DETECT:D22","DETECT:D23","CANARY:C27","CANARY:C28"]),
 "G12": ("大厂 LLM/ML 根因分析的原始口径(Meta 42%、RCACopilot、Ahmed、Triangle、DrP)", ["RCA:L1","RCA:L2","RCA:L3","RCA:L4","RCA:L5","RCA:L15","RCA:L16","RCA:L17","RCA:L18"]),
 "G13": ("独立 RCA 基准成绩(AIOpsLab、OpenRCA 1/2、ITBench、2026 排行榜)", ["RCA:L6","RCA:L7","RCA:L8","RCA:L9","RCA:L10","RCA:L11","RCA:L12","RCA:L13","RCA:L14"]),
 "G14": ("AI SRE 厂商宣称与「LLM 不进检测段」", ["RCA:L19","RCA:L20","RCA:L21","RCA:L22","RCA:L23","RCA:L24","RCA:L25","RCA:L26","RCA:L27","RCA:L28","RCA:L29"]),
 "G15": ("DORA 指标与 MTTR 作为度量的失效", ["CHANGE:C12","CHANGE:C13","CHANGE:C14","CHANGE:C15","CHANGE:C16","CHANGE:C17","CHANGE:C18"]),
}
idx = {}
for k in ["CHANGE","CANARY","DETECT","RCA","POSTMORTEM"]:
    d = json.load(open(f"lines/{k}.json"))
    for c in (d["claims"] if isinstance(d, dict) else d):
        idx[f"{k}:{c['id']}"] = c
cases = json.load(open("lines/POSTMORTEM.json")).get("cases", [])
for g, (title, ids) in G.items():
    out = [f"# {g} {title}\n"]
    for i in ids:
        c = idx[i]
        out.append(f"## {i}\n- 论断:{c['claim']}\n- 原文:{c.get('quote','')}\n- URL:{c.get('source_url','')}\n- 日期:{c.get('date','')}\n- 来源类型:{c.get('source_type','')}\n")
    if g in ("G03", "G04"):
        out.append("## 附:POSTMORTEM 案例表(原始 JSON)\n```json\n" + json.dumps(cases, ensure_ascii=False, indent=1) + "\n```\n")
    open(f"groups/{g}.md", "w").write("\n".join(out))
json.dump({g: {"title": t, "ids": i} for g, (t, i) in G.items()}, open("groups/index.json", "w"), ensure_ascii=False, indent=1)
print({g: len(i) for g, (t, i) in G.items()})
