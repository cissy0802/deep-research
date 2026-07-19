#!/usr/bin/env python3
"""Render sources/*.md into styled HTML pages for the Deep Research site.

Run from repo root:  python3 build.py
Adds a new research piece = drop 4 md files in sources/ (slug.{zh,en}.md × plain/deep),
add entries to ARTICLES / TLDRS / INDEX_ENTRIES (and optionally FIGURES) below, re-run.
"""

import html
import re
from pathlib import Path

# ---------------------------------------------------------------- markdown → html

def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md_to_html(md: str) -> str:
    out, para, ul, ol, quote = [], [], [], [], []

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_lists():
        if ul:
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in ul) + "</ul>")
            ul.clear()
        if ol:
            out.append("<ol>" + "".join(f"<li>{x}</li>" for x in ol) + "</ol>")
            ol.clear()

    def flush_quote():
        if quote:
            out.append("<blockquote>" + "".join(f"<p>{x}</p>" for x in quote) + "</blockquote>")
            quote.clear()

    def flush_all():
        flush_para(); flush_lists(); flush_quote()

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_all()
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush_all()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue
        if line.strip() == "---":
            flush_all()
            out.append("<hr>")
            continue
        if line.startswith(">"):
            flush_para(); flush_lists()
            quote.append(inline(line.lstrip("> ").strip()))
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m:
            flush_para(); flush_quote()
            if ol:
                flush_lists()
            ul.append(inline(m.group(1)))
            continue
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            flush_para(); flush_quote()
            if ul:
                flush_lists()
            ol.append(inline(m.group(1)))
            continue
        if quote:
            quote.append(inline(line.strip()))
            continue
        if ul:
            ul[-1] += " " + inline(line.strip())
            continue
        if ol:
            ol[-1] += " " + inline(line.strip())
            continue
        para.append(line.strip())
    flush_all()
    return "\n".join(out)


# ---------------------------------------------------------------- inline SVG figures

def fig_cost_transfer(lang: str) -> str:
    """Schematic: cost migrates from writing to verification/integration."""
    t = {
        "zh": dict(before="传统开发", after="人 + AI agent", write="写代码", verify="验证与整合",
                   bottleneck="新瓶颈", cap="示意图:生成成本趋零后,成本与瓶颈移向验证/整合环节(比例为示意,非实测)"),
        "en": dict(before="Traditional", after="Human + AI agents", write="Writing code", verify="Verify & integrate",
                   bottleneck="new bottleneck", cap="Schematic: as generation cost approaches zero, cost and the bottleneck move to verification/integration (proportions illustrative)"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="52" fill="#7c8593" font-size="13" font-family="Menlo,monospace">{t['before']}</text>
  <rect x="24" y="64" width="380" height="40" rx="6" fill="#4cc9f0" opacity="0.75"/>
  <rect x="408" y="64" width="150" height="40" rx="6" fill="#7b61ff" opacity="0.6"/>
  <text x="214" y="89" fill="#0a0e1a" font-size="13" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['write']}</text>
  <text x="483" y="89" fill="#e4e6eb" font-size="12" text-anchor="middle" font-family="-apple-system,sans-serif">{t['verify']}</text>

  <path d="M 350 118 Q 380 138 410 158" stroke="#ff6ec4" stroke-width="2" fill="none" stroke-dasharray="5,4" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#ff6ec4"/></marker></defs>

  <text x="24" y="166" fill="#7c8593" font-size="13" font-family="Menlo,monospace">{t['after']}</text>
  <rect x="24" y="178" width="64" height="40" rx="6" fill="#4cc9f0" opacity="0.75"/>
  <rect x="92" y="178" width="466" height="40" rx="6" fill="#7b61ff" opacity="0.85" stroke="#ff6ec4" stroke-width="2"/>
  <text x="325" y="203" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['verify']} ← {t['bottleneck']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_perrow(lang: str) -> str:
    """Perrow coupling × interactive-complexity risk quadrant."""
    t = {
        "zh": dict(x="交互复杂性 →", y="耦合度 →", q_danger="高危象限", d1="BigQuery / 支付 / 交易系统",
                   q_green="初创绿地", g1="错误预算宽裕 · 爆炸半径小",
                   cap="Perrow 风险透镜(示意):同一个 AI 工具,在两个象限积分出完全不同的风险;高危象限还叠加短时延——系统滑向灾难快于人类认知"),
        "en": dict(x="Interactive complexity →", y="Coupling →", q_danger="Danger quadrant", d1="BigQuery / payments / trading",
                   q_green="Greenfield startup", g1="generous error budget · small blast radius",
                   cap="Perrow risk lens (schematic): the same AI tool integrates to very different risk in the two quadrants; the danger quadrant adds short latency — systems slide to catastrophe faster than human cognition"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg" role="img">
  <line x1="70" y1="340" x2="650" y2="340" stroke="#5a6378" stroke-width="1.5"/>
  <line x1="70" y1="340" x2="70" y2="40" stroke="#5a6378" stroke-width="1.5"/>
  <text x="360" y="376" fill="#7c8593" font-size="13" text-anchor="middle" font-family="Menlo,monospace">{t['x']}</text>
  <text x="34" y="190" fill="#7c8593" font-size="13" text-anchor="middle" font-family="Menlo,monospace" transform="rotate(-90 34 190)">{t['y']}</text>

  <rect x="82" y="200" width="272" height="128" rx="10" fill="#52b788" opacity="0.12" stroke="#52b788" stroke-opacity="0.5"/>
  <text x="218" y="252" fill="#52b788" font-size="15" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['q_green']}</text>
  <text x="218" y="276" fill="#8fbfa8" font-size="11.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['g1']}</text>

  <rect x="366" y="52" width="272" height="128" rx="10" fill="#e85a4f" opacity="0.14" stroke="#e85a4f" stroke-opacity="0.6"/>
  <text x="502" y="104" fill="#ff8a80" font-size="15" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['q_danger']}</text>
  <text x="502" y="128" fill="#d9a09a" font-size="11.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['d1']}</text>

  <circle cx="150" cy="300" r="6" fill="#52b788"/>
  <circle cx="560" cy="90" r="7" fill="#e85a4f"/>
  <path d="M 175 292 Q 360 220 535 105" stroke="#7c8593" stroke-width="1.5" fill="none" stroke-dasharray="3,5"/>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_four_gauges(lang: str) -> str:
    """Four measurement gauges of the same job market pointing different ways."""
    t = {
        "zh": dict(title="同一个市场,四个仪表盘",
                   r1="存量就业 (BLS)", v1="历史新高", r2="招聘广告 (Indeed)", v2="−27.5% vs 2020",
                   r3="大厂新人占比 (SignalFire)", v3="≈ −65% vs 2019", r4="22–25 岁在册 (ADP)", v4="≈ −20% vs 2022 峰值",
                   cap="示意:四个口径量的不是同一个东西——存量创新高,入口端崩塌(条长为示意,各口径基线不同)"),
        "en": dict(title="One market, four dashboards",
                   r1="Employment stock (BLS)", v1="record high", r2="Job postings (Indeed)", v2="−27.5% vs 2020",
                   r3="New-grad share (SignalFire)", v3="≈ −65% vs 2019", r4="Age 22–25 on payroll (ADP)", v4="≈ −20% vs late-2022 peak",
                   cap="Schematic: the four gauges measure different things — the stock at a record while the entrance collapses (bar lengths illustrative; baselines differ)"),
    }[lang]
    rows = [
        (t['r1'], t['v1'], 14, "#52b788"),
        (t['r2'], t['v2'], 110, "#4cc9f0"),
        (t['r3'], t['v3'], 250, "#ff6ec4"),
        (t['r4'], t['v4'], 82, "#7b61ff"),
    ]
    # same single-baseline layout as fig_review_scissors: label right-aligned to the
    # axis, bar grows right, value at the bar end — direction lives in the value text.
    bars = []
    y = 64
    for label, val, w, color in rows:
        bars.append(f'<text x="218" y="{y + 15}" fill="#7c8593" font-size="12" text-anchor="end" font-family="Menlo,monospace">{label}</text>')
        bars.append(f'<rect x="230" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        bars.append(f'<text x="{230 + w + 8}" y="{y + 15}" fill="{color}" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{val}</text>')
        y += 52
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="230" y1="52" x2="230" y2="252" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(bars)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_age_scissors(lang: str) -> str:
    """Diverging employment lines: older devs grow, 22-25 falls after late 2022."""
    t = {
        "zh": dict(older="26 岁以上:继续增长", young="22–25 岁:峰值以来 ≈ −20%", gpt="ChatGPT 发布",
                   cap="示意:ADP 工资单口径(Canaries,2025-11 版)——同为软件开发者,分化只出现在最年轻一档;作者 2026-02 承认最宽控制下 2024 年后才显著"),
        "en": dict(older="Age 26+: keeps growing", young="Age 22–25: ≈ −20% from peak", gpt="ChatGPT release",
                   cap="Schematic: ADP payroll (Canaries, Nov 2025) — same occupation, divergence only in the youngest bracket; authors' Feb 2026 note concedes significance only after 2024 under broadest controls"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img">
  <line x1="60" y1="270" x2="660" y2="270" stroke="#5a6378" stroke-width="1.5"/>
  <line x1="60" y1="270" x2="60" y2="40" stroke="#5a6378" stroke-width="1.5"/>
  <text x="70" y="292" fill="#7c8593" font-size="12" font-family="Menlo,monospace">2021</text>
  <text x="255" y="292" fill="#7c8593" font-size="12" font-family="Menlo,monospace">2022</text>
  <text x="420" y="292" fill="#7c8593" font-size="12" font-family="Menlo,monospace">2024</text>
  <text x="610" y="292" fill="#7c8593" font-size="12" font-family="Menlo,monospace">2026</text>
  <line x1="300" y1="58" x2="300" y2="270" stroke="#f0b429" stroke-width="1.2" stroke-dasharray="4,5" opacity="0.7"/>
  <text x="308" y="70" fill="#f0b429" font-size="11" font-family="Menlo,monospace">{t['gpt']}</text>
  <path d="M 70 190 C 160 160, 240 148, 300 145 C 400 141, 520 128, 645 112" stroke="#4cc9f0" stroke-width="3" fill="none"/>
  <path d="M 70 196 C 160 168, 240 152, 300 150 C 380 152, 440 175, 500 200 C 560 224, 610 238, 645 246" stroke="#ff6ec4" stroke-width="3" fill="none"/>
  <circle cx="300" cy="145" r="4" fill="#4cc9f0"/>
  <circle cx="300" cy="150" r="4" fill="#ff6ec4"/>
  <text x="640" y="100" fill="#4cc9f0" font-size="12.5" font-weight="700" text-anchor="end" font-family="-apple-system,sans-serif">{t['older']}</text>
  <text x="640" y="240" fill="#ff6ec4" font-size="12.5" font-weight="700" text-anchor="end" font-family="-apple-system,sans-serif">{t['young']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_rct_paradox(lang: str) -> str:
    """Left: RCT gains largest for novices. Right: market outcome worst for novices."""
    t = {
        "zh": dict(lab="实验室(RCT):个体产出增益", mkt="劳动市场(2023–26):就业结果",
                   nov="新手", vet="老手", lnov="+27–39%", lvet="+8–13%", mnov="≈ −20%", mvet="增长",
                   arrow="组织的成本响应",
                   cap="示意:同一项技术,个体层面最帮新手(左,Copilot 三场 RCT),市场层面新手岗位收缩最狠(右,ADP)——分岔发生在企业的雇佣决策,不在技术里"),
        "en": dict(lab="The lab (RCTs): individual output gains", mkt="The market (2023–26): employment outcome",
                   nov="Novice", vet="Veteran", lnov="+27–39%", lvet="+8–13%", mnov="≈ −20%", mvet="growing",
                   arrow="the firm's cost response",
                   cap="Schematic: the same technology helps novices most at the individual level (left, three Copilot RCTs) while novice jobs contract hardest (right, ADP) — the fork is the firm's hiring decision, not the technology"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 310" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="165" y="34" fill="#e4e6eb" font-size="13.5" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['lab']}</text>
  <text x="535" y="34" fill="#e4e6eb" font-size="13.5" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['mkt']}</text>
  <line x1="50" y1="220" x2="280" y2="220" stroke="#5a6378" stroke-width="1.5"/>
  <rect x="80" y="90" width="60" height="130" rx="6" fill="#4cc9f0" opacity="0.85"/>
  <rect x="180" y="175" width="60" height="45" rx="6" fill="#4cc9f0" opacity="0.45"/>
  <text x="110" y="82" fill="#4cc9f0" font-size="13" font-weight="700" text-anchor="middle" font-family="Menlo,monospace">{t['lnov']}</text>
  <text x="210" y="167" fill="#7c8593" font-size="12" text-anchor="middle" font-family="Menlo,monospace">{t['lvet']}</text>
  <text x="110" y="242" fill="#a8b4d0" font-size="12.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['nov']}</text>
  <text x="210" y="242" fill="#a8b4d0" font-size="12.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['vet']}</text>
  <line x1="420" y1="140" x2="650" y2="140" stroke="#5a6378" stroke-width="1.5"/>
  <rect x="450" y="140" width="60" height="75" rx="6" fill="#ff6ec4" opacity="0.85"/>
  <rect x="550" y="95" width="60" height="45" rx="6" fill="#52b788" opacity="0.7"/>
  <text x="480" y="234" fill="#ff6ec4" font-size="13" font-weight="700" text-anchor="middle" font-family="Menlo,monospace">{t['mnov']}</text>
  <text x="580" y="87" fill="#52b788" font-size="12" text-anchor="middle" font-family="Menlo,monospace">{t['mvet']}</text>
  <text x="480" y="256" fill="#a8b4d0" font-size="12.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['nov']}</text>
  <text x="580" y="156" fill="#a8b4d0" font-size="12.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['vet']}</text>
  <path d="M 300 150 Q 350 130 400 150" stroke="#f0b429" stroke-width="2" fill="none" stroke-dasharray="5,4" marker-end="url(#arrowp)"/>
  <defs><marker id="arrowp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#f0b429"/></marker></defs>
  <text x="350" y="115" fill="#f0b429" font-size="11.5" text-anchor="middle" font-family="Menlo,monospace">{t['arrow']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_review_scissors(lang: str) -> str:
    """Faros telemetry: throughput gain vs review-side pile-up."""
    t = {
        "zh": dict(title="AI 高采用期 vs 低采用期(Faros 遥测,22,000 名开发者)",
                   r1="任务完成 / 人", v1="+33.7%", r2="PR 审查中位时长", v2="+441.5%",
                   r3="事故 / PR", v3="+242.7%", r4="零审查直接合并的 PR", v4="+31.3%",
                   cap="示意:同一批组织,产出小幅上升,代价堆在评审环节——评审变慢、事故变多、越来越多 PR 无人审(厂商遥测,前后对比口径,条长为示意)"),
        "en": dict(title="High vs low AI-adoption periods (Faros telemetry, 22,000 devs)",
                   r1="Tasks completed / dev", v1="+33.7%", r2="Median PR review time", v2="+441.5%",
                   r3="Incidents / PR", v3="+242.7%", r4="PRs merged with zero review", v4="+31.3%",
                   cap="Schematic: same organizations — a modest output gain, with the cost piling up at review: slower reviews, more incidents, more PRs merged unseen (vendor telemetry, before/after; bar lengths illustrative)"),
    }[lang]
    rows = [
        (t['r1'], t['v1'], 34, "#52b788"),
        (t['r2'], t['v2'], 400, "#ff6ec4"),
        (t['r3'], t['v3'], 220, "#e8794b"),
        (t['r4'], t['v4'], 30, "#7b61ff"),
    ]
    bars = []
    y = 64  # top of each bar; label & value share the bar's vertical center line
    for label, val, w, color in rows:
        bars.append(f'<text x="218" y="{y + 15}" fill="#7c8593" font-size="12" text-anchor="end" font-family="Menlo,monospace">{label}</text>')
        bars.append(f'<rect x="230" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        bars.append(f'<text x="{230 + w + 10}" y="{y + 15}" fill="{color}" font-size="13" font-weight="700" font-family="Menlo,monospace">{val}</text>')
        y += 52
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="230" y1="52" x2="230" y2="252" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(bars)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_bench_spread(lang: str) -> str:
    """Same tool, four benchmarks, four wildly different scores."""
    t = {
        "zh": dict(title="同一个工具,四张考卷(Greptile,2025-07 至 2026-05)",
                   b1="自家基准 · 捕获率", b2="竞品 Augment 重测 · F 分", b3="竞品 Tenki · 召回", b4="竞品 Tenki · 精确率",
                   note="6 家自办基准,发布者 6 次全部第一",
                   cap="示意:分数取决于谁出题、量哪根轴——只报捕获率不报误报率,是信号检测论 1966 年就判过的度量错误(各基准指标不同,不可直接比大小)"),
        "en": dict(title="One tool, four exams (Greptile, Jul 2025 – May 2026)",
                   b1="Own benchmark · catch rate", b2="Rival Augment re-test · F-score", b3="Rival Tenki · recall", b4="Rival Tenki · precision",
                   note="6 self-run benchmarks — publisher ranked #1 all 6 times",
                   cap="Schematic: the score depends on who writes the exam and which axis gets measured — publishing catch rate without false-alarm rate is the measurement error signal detection theory settled in 1966 (metrics differ across benchmarks; not directly comparable)"),
    }[lang]
    rows = [
        (t['b1'], "82%", 410, "#4cc9f0"),
        (t['b2'], "45%", 225, "#7b61ff"),
        (t['b3'], "36.1%", 181, "#f0b429"),
        (t['b4'], "15.9%", 80, "#ff6ec4"),
    ]
    bars = []
    y = 76
    for label, val, w, color in rows:
        bars.append(f'<text x="24" y="{y}" fill="#7c8593" font-size="12" font-family="Menlo,monospace">{label}</text>')
        by = y + 10
        bars.append(f'<rect x="24" y="{by}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        bars.append(f'<text x="{24 + w + 10}" y="{by + 15}" fill="{color}" font-size="13" font-weight="700" font-family="Menlo,monospace">{val}</text>')
        y += 62
    return f"""<figure>
<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  {''.join(bars)}
  <rect x="24" y="326" width="500" height="30" rx="8" fill="#e85a4f" opacity="0.12" stroke="#e85a4f" stroke-opacity="0.5"/>
  <text x="38" y="346" fill="#ff8a80" font-size="12.5" font-weight="700" font-family="-apple-system,sans-serif">{t['note']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_offline_funnel(lang: str) -> str:
    """Offline eval scores vs production adoption: the order-of-magnitude funnel."""
    t = {
        "zh": dict(meta="Meta(2507.13499)", google="Google(ICSE-SEIP 2024)",
                   m1="离线 exact-match", m1v="67.96%", m2="展示后被采纳", m2v="≈28.7%", m3="生产 Actionable→Applied", m3v="19.75%",
                   g1="模型高置信预测", g1v="49%", g2="被作者预览", g2v="10.7%", g3="被采纳入库", g3v="7.5%",
                   cap="示意:两家第一方漏斗——离线分数是自家精选考卷上的成绩,生产采纳率才是市场价(两家分母口径不同,不可互比,只看各自衰减)"),
        "en": dict(meta="Meta (2507.13499)", google="Google (ICSE-SEIP 2024)",
                   m1="Offline exact-match", m1v="67.96%", m2="Applied when shown", m2v="≈28.7%", m3="Production Actionable→Applied", m3v="19.75%",
                   g1="Confident model predictions", g1v="49%", g2="Previewed by author", g2v="10.7%", g3="Applied to the codebase", g3v="7.5%",
                   cap="Schematic: two first-party funnels — the offline score is a grade on a self-curated exam; the production apply rate is the market price (different denominators; compare each funnel's decay, not the two columns)"),
    }[lang]
    def col(x, title, steps, color):
        parts = [f'<text x="{x + 150}" y="58" fill="#e4e6eb" font-size="13" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{title}</text>']
        y = 78
        widths = [300, 190, 110]
        for (label, val), w in zip(steps, widths):
            bx = x + 150 - w / 2
            parts.append(f'<rect x="{bx}" y="{y}" width="{w}" height="34" rx="6" fill="{color}" opacity="{0.9 - 0.22 * (widths.index(w))}"/>')
            parts.append(f'<text x="{x + 150}" y="{y + 22}" fill="#0a0e1a" font-size="12.5" font-weight="700" text-anchor="middle" font-family="Menlo,monospace">{val}</text>')
            parts.append(f'<text x="{x + 150}" y="{y + 50}" fill="#7c8593" font-size="10.5" text-anchor="middle" font-family="-apple-system,sans-serif">{label}</text>')
            y += 66
        return ''.join(parts)
    meta_steps = [(t['m1'], t['m1v']), (t['m2'], t['m2v']), (t['m3'], t['m3v'])]
    google_steps = [(t['g1'], t['g1v']), (t['g2'], t['g2v']), (t['g3'], t['g3v'])]
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  {col(20, t['meta'], meta_steps, "#4cc9f0")}
  {col(370, t['google'], google_steps, "#7b61ff")}
  <line x1="350" y1="52" x2="350" y2="280" stroke="#5a6378" stroke-width="1" stroke-dasharray="2,5"/>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_review_turtles(lang: str) -> str:
    """The nesting-doll verification chain with each layer's failure mode."""
    t = {
        "zh": dict(l1="AI 写代码", n1="产出不可靠 → 需要检查", l2="AI 审代码", n2="幻觉 bug · 与生成器错误趋同",
                   l3="人审 AI 的审查", n3="自动化自满:「训练无法预防」", q="谁来验证验证者?",
                   cap="示意:每一层验证自身引入新的错误源;当验证层与生成层盲区相关,叠层降低的是体感风险而非真实风险"),
        "en": dict(l1="AI writes the code", n1="unreliable output → needs a check", l2="AI reviews the code", n2="hallucinated bugs · errors converging with the generator",
                   l3="Humans review the AI's review", n3="automation complacency: 'cannot be prevented by training'", q="Who verifies the verifiers?",
                   cap="Schematic: each verification layer introduces its own error source; when verifier and generator share blind spots, stacking layers lowers perceived — not actual — risk"),
    }[lang]
    rows = [
        (t['l1'], t['n1'], "#4cc9f0", 60),
        (t['l2'], t['n2'], "#7b61ff", 150),
        (t['l3'], t['n3'], "#ff6ec4", 240),
    ]
    parts = []
    for label, note, color, y in rows:
        parts.append(f'<rect x="60" y="{y}" width="250" height="48" rx="10" fill="{color}" opacity="0.18" stroke="{color}" stroke-opacity="0.7" stroke-width="1.5"/>')
        parts.append(f'<text x="185" y="{y + 29}" fill="#e4e6eb" font-size="14" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{label}</text>')
        parts.append(f'<text x="336" y="{y + 29}" fill="#7c8593" font-size="11.5" font-family="-apple-system,sans-serif">{note}</text>')
        if y < 240:
            parts.append(f'<path d="M 185 {y + 48} L 185 {y + 90}" stroke="#5a6378" stroke-width="1.5" marker-end="url(#arrowt)"/>')
    return f"""<figure>
<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" role="img">
  <defs><marker id="arrowt" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a6378"/></marker></defs>
  {''.join(parts)}
  <path d="M 185 288 L 185 326" stroke="#f0b429" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrowt)"/>
  <text x="185" y="352" fill="#f0b429" font-size="14" font-weight="700" text-anchor="middle" font-family="Menlo,monospace">{t['q']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_cure_conditions(lang: str) -> str:
    """Quadrant: independent oracle × human verdict → cure zone vs turtles zone."""
    t = {
        "zh": dict(x="独立于 LLM 的 oracle(测试/编译器/类型)→", y="人保留裁决权 →",
                   cure="解药区", c1="Google 迁移 · Cloudflare 全量部署", c2="窄场景 · 控误报 · 廉价额外一层",
                   turt="套娃区", t1="无测试兜底的业务逻辑 · AI 写 AI 审", t2="零审查合并 +31.3% 的漂移方向",
                   cap="示意:同一类工具,落在哪个象限由使用结构决定——oracle 密度与人的位置,比模型分数更能预测结果"),
        "en": dict(x="Oracle independent of the LLM (tests/compiler/types) →", y="Humans keep the verdict →",
                   cure="Cure zone", c1="Google migrations · Cloudflare full deployment", c2="narrow scope · controlled false alarms · cheap extra layer",
                   turt="Turtles zone", t1="untested business logic · AI writes, AI reviews", t2="the drift behind +31.3% zero-review merges",
                   cap="Schematic: where the same tool lands is decided by the structure of use — oracle density and the human's position predict outcomes better than model scores"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg" role="img">
  <line x1="70" y1="340" x2="650" y2="340" stroke="#5a6378" stroke-width="1.5"/>
  <line x1="70" y1="340" x2="70" y2="40" stroke="#5a6378" stroke-width="1.5"/>
  <text x="360" y="376" fill="#7c8593" font-size="12.5" text-anchor="middle" font-family="Menlo,monospace">{t['x']}</text>
  <text x="34" y="190" fill="#7c8593" font-size="12.5" text-anchor="middle" font-family="Menlo,monospace" transform="rotate(-90 34 190)">{t['y']}</text>

  <rect x="366" y="52" width="272" height="128" rx="10" fill="#52b788" opacity="0.12" stroke="#52b788" stroke-opacity="0.5"/>
  <text x="502" y="94" fill="#52b788" font-size="15" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['cure']}</text>
  <text x="502" y="118" fill="#8fbfa8" font-size="11" text-anchor="middle" font-family="-apple-system,sans-serif">{t['c1']}</text>
  <text x="502" y="138" fill="#8fbfa8" font-size="11" text-anchor="middle" font-family="-apple-system,sans-serif">{t['c2']}</text>

  <rect x="82" y="200" width="272" height="128" rx="10" fill="#e85a4f" opacity="0.14" stroke="#e85a4f" stroke-opacity="0.6"/>
  <text x="218" y="242" fill="#ff8a80" font-size="15" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['turt']}</text>
  <text x="218" y="266" fill="#d9a09a" font-size="11" text-anchor="middle" font-family="-apple-system,sans-serif">{t['t1']}</text>
  <text x="218" y="286" fill="#d9a09a" font-size="11" text-anchor="middle" font-family="-apple-system,sans-serif">{t['t2']}</text>

  <circle cx="560" cy="90" r="7" fill="#52b788"/>
  <circle cx="150" cy="300" r="6" fill="#e85a4f"/>
  <path d="M 535 105 Q 360 200 175 292" stroke="#7c8593" stroke-width="1.5" fill="none" stroke-dasharray="3,5"/>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""



def fig_so_genealogy(lang: str) -> str:
    """Timeline: qualified assumption (top) vs accumulating cracks (bottom)."""
    t = {
        "zh": dict(title="「验证比生成容易」这句话的八年",
                   leg_a="● 上轨:这句话被引用/强化", leg_b="● 下轨:反面证据在积累",
                   a1="2018 写成「假设2」,限定『许多任务』", a2="2018 提出者自注:『只是类比』", a3="2022 OpenAI 当公理引用",
                   b1="2020:谎言能藏到裁判找不出(无修复)", b2="2024 裁判不缺信息时效果不稳", b3="2025 监督更强 AI ≈ 抛硬币", b4="理论每修补一次,就多一个新前提",
                   cap="示意:2018 年这句话带着限定语出生(上轨),四年后限定语在引用中消失;同期反面证据持续积累(下轨)——正文第 1、2 节是本图的逐条展开"),
        "en": dict(title="Eight years of one sentence",
                   leg_a="● top: the sentence cited / strengthened", leg_b="● bottom: counter-evidence accumulating",
                   a1="2018 \"Assumption 2\", limited to \"many tasks\"", a2="2018 authors' note: \"analogies only\"", a3="2022 OpenAI cites it as an axiom",
                   b1="2020: lies can hide from judges (no fix)", b2="2024 unstable without info gap", b3="2025 vs stronger AI ≈ coin flip", b4="each theory patch adds a premise",
                   cap="Schematic: born with qualifiers in 2018 (top track), the qualifiers vanished from citations within four years while counter-evidence accumulated (bottom track) — sections 1-2 unpack each dot"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="24" y="52" fill="#4cc9f0" font-size="11" font-family="-apple-system,sans-serif">{t['leg_a']}</text>
  <text x="24" y="288" fill="#ff6ec4" font-size="11" font-family="-apple-system,sans-serif">{t['leg_b']}</text>
  <line x1="40" y1="150" x2="660" y2="150" stroke="#5a6378" stroke-width="1.5"/>
  <text x="52" y="168" fill="#7c8593" font-size="11" font-family="Menlo,monospace">2018</text>
  <text x="330" y="168" fill="#7c8593" font-size="11" font-family="Menlo,monospace">2022</text>
  <text x="620" y="168" fill="#7c8593" font-size="11" font-family="Menlo,monospace">2026</text>

  <circle cx="70" cy="150" r="5" fill="#4cc9f0"/>
  <line x1="70" y1="145" x2="70" y2="96" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="46" y="92" fill="#4cc9f0" font-size="11.5" font-family="-apple-system,sans-serif">{t['a1']}</text>

  <circle cx="150" cy="150" r="5" fill="#4cc9f0"/>
  <line x1="150" y1="145" x2="150" y2="66" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="126" y="76" fill="#4cc9f0" font-size="11.5" font-family="-apple-system,sans-serif">{t['a2']}</text>

  <circle cx="368" cy="150" r="5" fill="#7b61ff"/>
  <line x1="368" y1="145" x2="368" y2="96" stroke="#7b61ff" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="330" y="92" fill="#a29bfe" font-size="11.5" font-weight="700" font-family="-apple-system,sans-serif">{t['a3']}</text>

  <circle cx="215" cy="150" r="5" fill="#ff6ec4"/>
  <line x1="215" y1="155" x2="215" y2="200" stroke="#ff6ec4" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="136" y="216" fill="#ff6ec4" font-size="11.5" font-family="-apple-system,sans-serif">{t['b1']}</text>

  <circle cx="500" cy="150" r="5" fill="#e8794b"/>
  <line x1="500" y1="155" x2="500" y2="200" stroke="#e8794b" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="392" y="216" fill="#e8794b" font-size="11.5" font-family="-apple-system,sans-serif">{t['b2']}</text>

  <circle cx="572" cy="150" r="5" fill="#e85a4f"/>
  <line x1="572" y1="155" x2="572" y2="242" stroke="#e85a4f" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="430" y="258" fill="#ff8a80" font-size="11.5" font-family="-apple-system,sans-serif">{t['b3']}</text>

  <circle cx="620" cy="150" r="5" fill="#f0b429"/>
  <line x1="620" y1="155" x2="620" y2="230" stroke="#f0b429" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="676" y="242" fill="#f0b429" font-size="11.5" text-anchor="end" font-family="-apple-system,sans-serif">{t['b4']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_so_debate(lang: str) -> str:
    """Debate scorecard: paired baseline vs debate bars, one baseline per row."""
    t = {
        "zh": dict(title="AI 辩论实测:什么条件下有效",
                   r1="人类裁判(裁判缺信息)", r2="LLM 裁判(裁判缺信息)", r3="监督更强的 AI(差距大)",
                   base="基线", deb="debate", other="其他协议",
                   note="无信息差任务(数学/代码/逻辑):相对直接问答 mixed(GDM 2024);单条独立批评可收回大部分收益(2026)",
                   cap="示意:正结果集中在裁判缺信息的设定;能力差距拉大后 debate 51.7% ≈ 抛硬币,仍是四种协议中最好(条长=准确率/成功率)"),
        "en": dict(title="AI debate measured: when it works",
                   r1="Human judges (judge lacks info)", r2="LLM judges (judge lacks info)", r3="Overseeing stronger AI (big gap)",
                   base="baseline", deb="debate", other="other protocols",
                   note="Without info asymmetry (math/code/logic): mixed vs direct QA (GDM 2024); one independent critique recovers most of the benefit (2026)",
                   cap="Schematic: positive results concentrate where judges lack information; at a large capability gap debate is 51.7% ≈ a coin flip — still the best of four protocols (bar length = accuracy/success rate)"),
    }[lang]
    rows = [
        (t['r1'], 60, 88, "#7c8593", "#4cc9f0", t['base'], t['deb']),
        (t['r2'], 48, 76, "#7c8593", "#4cc9f0", t['base'], t['deb']),
        (t['r3'], 10, 51.7, "#e85a4f", "#f0b429", t['other'], t['deb']),
    ]
    bars = []
    y = 60
    for label, v1, v2, c1, c2, l1, l2 in rows:
        bars.append(f'<text x="218" y="{y + 16}" fill="#7c8593" font-size="12" text-anchor="end" font-family="Menlo,monospace">{label}</text>')
        w1, w2 = v1 * 3.6, v2 * 3.6
        bars.append(f'<rect x="230" y="{y}" width="{w1:.0f}" height="10" rx="3" fill="{c1}" opacity="0.6"/>')
        bars.append(f'<text x="{230 + w1 + 8:.0f}" y="{y + 9}" fill="{c1}" font-size="10.5" font-family="Menlo,monospace">{v1}% {l1}</text>')
        bars.append(f'<rect x="230" y="{y + 13}" width="{w2:.0f}" height="10" rx="3" fill="{c2}" opacity="0.9"/>')
        bars.append(f'<text x="{230 + w2 + 8:.0f}" y="{y + 22}" fill="{c2}" font-size="10.5" font-weight="700" font-family="Menlo,monospace">{v2}% {l2}</text>')
        y += 56
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="230" y1="48" x2="230" y2="{y - 20}" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(bars)}
  <text x="24" y="{y + 8}" fill="#8a93ad" font-size="11" font-family="-apple-system,sans-serif">{t['note']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_so_spectrum(lang: str) -> str:
    """Task-family verifiability spectrum."""
    t = {
        "zh": dict(title="「验证更容易」按任务族分层",
                   z1="形式化证明", z2="有测试的代码", z3="事实性文本", z4="开放论证/对抗",
                   s1="成立·被工业利用", s2="条件成立(oracle 质量=上限)", s3="开始反转", s4="多数证据反对",
                   e1="AlphaProof×Lean", e2="弱测试会被糊弄", e3="核查可能比写慢", e4="藏错·自查崩塌",
                   ax_l="← oracle 独立 · 无对抗", ax_r="无证书 · 有对抗 →",
                   cap="示意:判据轴——oracle 是否独立、是否有对抗压力;第三轴见正文:请裁判开庭的成本与时延(生产是终极裁判,但判决在事后)。scalable oversight 要用的恰好是最右端"),
        "en": dict(title="\"Verification is easier\" stratified by task family",
                   z1="Formal proofs", z2="Code with tests", z3="Factual text", z4="Open argument / adversarial",
                   s1="holds · exploited", s2="conditional (oracle = ceiling)", s3="starts inverting", s4="most evidence against",
                   e1="AlphaProof × Lean", e2="weak tests get gamed", e3="checking can be slower", e4="hidden errors · self-critique collapse",
                   ax_l="← independent oracle · no adversary", ax_r="no certificate · adversarial →",
                   cap="Schematic: criteria — oracle independence and adversarial pressure; the third axis is in the text: the cost and latency of the judge's verdicts (production is the ultimate judge, but it rules after the fact). Scalable oversight must operate at the far right"),
    }[lang]
    zones = [
        (t['z1'], t['s1'], t['e1'], "#52b788"),
        (t['z2'], t['s2'], t['e2'], "#4cc9f0"),
        (t['z3'], t['s3'], t['e3'], "#f0b429"),
        (t['z4'], t['s4'], t['e4'], "#e85a4f"),
    ]
    blocks = []
    x = 30
    w = 160
    for name, status, ex, color in zones:
        cx = x + w / 2
        blocks.append(f'<rect x="{x}" y="70" width="{w - 8}" height="56" rx="9" fill="{color}" opacity="0.16" stroke="{color}" stroke-opacity="0.55"/>')
        blocks.append(f'<text x="{cx - 4}" y="94" fill="{color}" font-size="13" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{name}</text>')
        blocks.append(f'<text x="{cx - 4}" y="114" fill="{color}" font-size="10.5" text-anchor="middle" opacity="0.9" font-family="-apple-system,sans-serif">{status}</text>')
        blocks.append(f'<text x="{cx - 4}" y="152" fill="#8a93ad" font-size="10.5" text-anchor="middle" font-family="-apple-system,sans-serif">{ex}</text>')
        x += w
    return f"""<figure>
<svg viewBox="0 0 700 220" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  {''.join(blocks)}
  <line x1="30" y1="176" x2="662" y2="176" stroke="#5a6378" stroke-width="1.5" marker-end="url(#soarrow)"/>
  <defs><marker id="soarrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5a6378"/></marker></defs>
  <text x="30" y="198" fill="#52b788" font-size="11" font-family="Menlo,monospace">{t['ax_l']}</text>
  <text x="662" y="198" fill="#e85a4f" font-size="11" text-anchor="end" font-family="Menlo,monospace">{t['ax_r']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_so_retreat(lang: str) -> str:
    """The retreat tower: roadmap layer vs experiment layer vs deployed layer."""
    t = {
        "zh": dict(title="路线图 vs 实际部署(2025-26)",
                   l1="Debate / Amplified oversight", d1="路线图层 · 生产实证:0",
                   l2="Sandwiching / Weak-to-strong", d2="实验层 · 现象在,干预不稳(p=.135)",
                   l3="CoT 监控(已部署)", d3="GPT-5:标记 2.1-4.8% · 复述率 25-39% · 三家联署:「脆弱」",
                   arrow="退守",
                   cap="示意:实验室实际部署的是假设的最弱形式——不验证产出,只监控过程痕迹,且部署者自认其脆弱"),
        "en": dict(title="Roadmap vs actual deployment (2025-26)",
                   l1="Debate / Amplified oversight", d1="roadmap layer · production evidence: 0",
                   l2="Sandwiching / Weak-to-strong", d2="experiment layer · phenomenon real, interventions unstable (p=.135)",
                   l3="CoT monitoring (deployed)", d3="GPT-5: flags 2.1-4.8% · mention rate 25-39% · tri-lab: \"fragile\"",
                   arrow="retreat",
                   cap="Schematic: what labs actually deploy is the assumption's weakest form — monitoring the process trace, not verifying the output, and its deployers call it fragile"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 290" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <rect x="140" y="48" width="420" height="52" rx="9" fill="#7b61ff" opacity="0.10" stroke="#7b61ff" stroke-opacity="0.45" stroke-dasharray="5,4"/>
  <text x="350" y="70" fill="#a29bfe" font-size="13" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['l1']}</text>
  <text x="350" y="90" fill="#8a93ad" font-size="11" text-anchor="middle" font-family="Menlo,monospace">{t['d1']}</text>
  <rect x="140" y="112" width="420" height="52" rx="9" fill="#4cc9f0" opacity="0.10" stroke="#4cc9f0" stroke-opacity="0.45" stroke-dasharray="5,4"/>
  <text x="350" y="134" fill="#4cc9f0" font-size="13" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['l2']}</text>
  <text x="350" y="154" fill="#8a93ad" font-size="11" text-anchor="middle" font-family="Menlo,monospace">{t['d2']}</text>
  <rect x="100" y="186" width="500" height="60" rx="9" fill="#ff6ec4" opacity="0.14" stroke="#ff6ec4" stroke-width="2"/>
  <text x="350" y="210" fill="#ff6ec4" font-size="13.5" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['l3']}</text>
  <text x="350" y="232" fill="#d9a0c0" font-size="10.5" text-anchor="middle" font-family="Menlo,monospace">{t['d3']}</text>
  <path d="M 80 60 Q 56 150 92 208" stroke="#f0b429" stroke-width="2" fill="none" stroke-dasharray="5,4" marker-end="url(#soarr2)"/>
  <defs><marker id="soarr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#f0b429"/></marker></defs>
  <text x="44" y="140" fill="#f0b429" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['arrow']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


# slug → list of (lang_or_None, version_or_None, heading_text_prefix, figure_fn)
# figure inserted right AFTER the first heading whose text starts with the prefix.
def fig_ls_control(lang: str) -> str:
    """Same technique, three control groups, three numbers (Yang 2021)."""
    t = {
        "zh": dict(title="同一个「测验有效」,三个对照组,三个数字",
                   r1="对无活动/填充任务", v1="g=0.610", r2="对重读(严格对照)", v2="g=0.330",
                   r3="对精细加工策略", v3="g=0.095(不显著)",
                   cap="示意:课堂测验的效应量随对照组类型变化(Yang 等 2021,222 项课堂研究、48,478 名学生);对概念图等精细加工策略的 0.095 不显著(p=.062)——宣传引第一个数,严格比较看后两个"),
        "en": dict(title="One “quizzing works”, three controls, three numbers",
                   r1="vs no activity / filler", v1="g=0.610", r2="vs restudying (strict)", v2="g=0.330",
                   r3="vs elaborative strategies", v3="g=0.095 (ns)",
                   cap="Schematic: the effect of class quizzing by control-group type (Yang et al. 2021; 222 classroom studies, 48,478 students); 0.095 vs elaborative strategies is non-significant (p=.062) — ads quote the first number, strict comparisons are the other two"),
    }[lang]
    rows = [
        (t['r1'], t['v1'], 340, "#4cc9f0"),
        (t['r2'], t['v2'], 184, "#7b61ff"),
        (t['r3'], t['v3'], 53, "#ff6ec4"),
    ]
    bars = []
    y = 64
    for label, val, w, color in rows:
        bars.append(f'<text x="258" y="{y + 15}" fill="#7c8593" font-size="12" text-anchor="end" font-family="Menlo,monospace">{label}</text>')
        bars.append(f'<rect x="270" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        bars.append(f'<text x="{270 + w + 8}" y="{y + 15}" fill="{color}" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{val}</text>')
        y += 52
    return f"""<figure>
<svg viewBox="0 0 700 240" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="270" y1="52" x2="270" y2="204" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(bars)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ls_lab2class(lang: str) -> str:
    """Lab-to-classroom shrinkage, with interleaving as the exception."""
    t = {
        "zh": dict(title="实验室的尺子,课堂的账本",
                   r1="检索·实验室(Rowland 2014)", v1="g=0.50",
                   r2="检索·真实课堂(Yang 2021)", v2="g=0.33",
                   r3="交错·课堂预注册 RCT(Rohrer 2020)", v3="g≈0.83:罕见的不缩水",
                   note="间隔练习轻剂量塞进 9 门常规大学课:平均只 +2.06 个百分点(Bego 2024)",
                   cap="示意:同为「对重读」口径,检索练习从实验室到课堂缩水约三分之一;交错练习是罕见例外(七年级数学,54 班预注册整群 RCT);间隔练习轻剂量进常规课堂时收益缩到约 2 个百分点"),
        "en": dict(title="The lab's ruler vs the classroom's ledger",
                   r1="retrieval, lab (Rowland 2014)", v1="g=0.50",
                   r2="retrieval, classroom (Yang 2021)", v2="g=0.33",
                   r3="interleaving RCT (Rohrer 2020)", v3="g≈0.83: the rare survivor",
                   note="Spacing added lightly to 9 regular university courses: avg +2.06 percentage points (Bego 2024)",
                   cap="Schematic: on the same vs-restudy calibration, retrieval practice loses about a third from lab to classroom; interleaving is the rare exception (7th-grade math, 54-class preregistered cluster RCT); light-dose spacing in regular courses shrinks to ~2 percentage points"),
    }[lang]
    rows = [
        (t['r1'], t['v1'], 250, "#4cc9f0"),
        (t['r2'], t['v2'], 165, "#7b61ff"),
        (t['r3'], t['v3'], 415, "#52b788"),
    ]
    bars = []
    y = 60
    for label, val, w, color in rows:
        bars.append(f'<text x="268" y="{y + 15}" fill="#7c8593" font-size="11.5" text-anchor="end" font-family="Menlo,monospace">{label}</text>')
        bars.append(f'<rect x="280" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        if w > 300:
            bars.append(f'<text x="{280 + w - 8}" y="{y + 15}" fill="#0a0e1a" font-size="11.5" font-weight="700" text-anchor="end" font-family="-apple-system,sans-serif">{val}</text>')
        else:
            bars.append(f'<text x="{280 + w + 8}" y="{y + 15}" fill="{color}" font-size="11.5" font-weight="700" font-family="-apple-system,sans-serif">{val}</text>')
        y += 50
    return f"""<figure>
<svg viewBox="0 0 700 280" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="280" y1="50" x2="280" y2="200" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(bars)}
  <rect x="24" y="216" width="652" height="36" rx="8" fill="#f0b429" opacity="0.08" stroke="#f0b429" stroke-opacity="0.4" stroke-dasharray="4,4"/>
  <text x="350" y="239" fill="#f0b429" font-size="11.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['note']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ls_practice_war(lang: str) -> str:
    """Timeline of the deliberate-practice war, 1993-2024."""
    t = {
        "zh": dict(title="刻意练习之战:三十年时间线",
                   e1a="1993 强主张登场", e1b="练习量「很大程度上解释」差异(N=30)",
                   e2a="2008《Outliers》", e2b="一万小时=「伟大的魔法数字」",
                   e3a="2014 Macnamara meta:12%", e3b="(2018 勘误为 14%)",
                   e4a="2016 定义之战", e4b="双方互指对方口径",
                   e5a="2019 预注册复现", e5b="顶尖组 8,224h ≯ 优秀组 9,844h",
                   e6a="2024 交互模型", e6b="天赋×练习相互放大",
                   cap="示意:从 1993 年强主张到 2019 年预注册复现失败——「练习很重要」活着,「练习量解释一切」死了;两派均为同一批数据的再编码者"),
        "en": dict(title="The deliberate-practice war: a 30-year timeline",
                   e1a="1993 strong claim", e1b="practice “largely accounts” (N=30)",
                   e2a="2008 Outliers", e2b="10,000 hrs = “magic number”",
                   e3a="2014 Macnamara meta: 12%", e3b="(corrected to 14% in 2018)",
                   e4a="2016 definition war", e4b="each side disputes coding",
                   e5a="2019 preregistered replication", e5b="best 8,224h ≯ good 9,844h",
                   e6a="2024 interaction model", e6b="talent × practice amplify",
                   cap="Schematic: from the 1993 strong claim to the failed 2019 preregistered replication — “practice matters” survives, “practice explains it all” does not; both camps re-code the same datasets"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 290" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="50" y1="160" x2="670" y2="160" stroke="#5a6378" stroke-width="1.5"/>
  <circle cx="80" cy="160" r="6" fill="#4cc9f0"/><line x1="80" y1="154" x2="80" y2="86" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="30" y="62" fill="#4cc9f0" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['e1a']}</text>
  <text x="30" y="79" fill="#8a93ad" font-size="10.5" font-family="-apple-system,sans-serif">{t['e1b']}</text>
  <circle cx="205" cy="160" r="6" fill="#ff6ec4"/><line x1="205" y1="166" x2="205" y2="204" stroke="#ff6ec4" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="120" y="222" fill="#ff6ec4" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['e2a']}</text>
  <text x="120" y="239" fill="#8a93ad" font-size="10.5" font-family="-apple-system,sans-serif">{t['e2b']}</text>
  <circle cx="345" cy="160" r="6" fill="#7b61ff"/><line x1="345" y1="154" x2="345" y2="116" stroke="#7b61ff" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="345" y="93" fill="#7b61ff" font-size="12" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['e3a']}</text>
  <text x="345" y="110" fill="#8a93ad" font-size="10.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['e3b']}</text>
  <circle cx="455" cy="160" r="6" fill="#f0b429"/><line x1="455" y1="166" x2="455" y2="204" stroke="#f0b429" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="455" y="222" fill="#f0b429" font-size="12" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{t['e4a']}</text>
  <text x="455" y="239" fill="#8a93ad" font-size="10.5" text-anchor="middle" font-family="-apple-system,sans-serif">{t['e4b']}</text>
  <circle cx="560" cy="160" r="6" fill="#e85a4f"/><line x1="560" y1="154" x2="560" y2="86" stroke="#e85a4f" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="676" y="62" fill="#ff8a80" font-size="12" font-weight="700" text-anchor="end" font-family="-apple-system,sans-serif">{t['e5a']}</text>
  <text x="676" y="79" fill="#8a93ad" font-size="10.5" text-anchor="end" font-family="-apple-system,sans-serif">{t['e5b']}</text>
  <circle cx="655" cy="160" r="6" fill="#5eead4"/><line x1="655" y1="166" x2="655" y2="204" stroke="#5eead4" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="676" y="222" fill="#5eead4" font-size="12" font-weight="700" text-anchor="end" font-family="-apple-system,sans-serif">{t['e6a']}</text>
  <text x="676" y="239" fill="#8a93ad" font-size="10.5" text-anchor="end" font-family="-apple-system,sans-serif">{t['e6b']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ls_styles_gap(lang: str) -> str:
    """Learning styles: belief prevalence vs evidence."""
    t = {
        "zh": dict(title="学习风格:信念与证据的剪刀差",
                   r1="相信匹配教学的教育者", v1="89.1%(18 国 15,405 人)",
                   r2="呈现交叉互作的结果", v2="26%(最有利的 2024 meta)",
                   r3="2008 权威综述的合格证据", v3="「几乎不存在」",
                   cap="示意:18 国教育者的信念率(Newton & Salvi 2020)vs 理论所需交叉互作在最有利 meta 中的出现率(Clinton-Lisell 2024,且仅 5/21 研究达质量标准)vs Pashler 等 2008 的判语"),
        "en": dict(title="Learning styles: the belief-evidence scissors",
                   r1="educators who believe matching works", v1="89.1% (15,405 educators, 18 countries)",
                   r2="outcomes showing the crossover", v2="26% (friendliest 2024 meta)",
                   r3="qualifying evidence, 2008 review", v3="“virtually no evidence”",
                   cap="Schematic: educator belief across 18 countries (Newton & Salvi 2020) vs the rate of theoretically required crossover interactions in the friendliest meta-analysis (Clinton-Lisell 2024; only 5/21 studies met quality standards) vs the Pashler et al. 2008 verdict"),
    }[lang]
    rows = [
        (t['r1'], t['v1'], 321, "#ff6ec4", True),
        (t['r2'], t['v2'], 94, "#4cc9f0", False),
        (t['r3'], t['v3'], 3, "#e85a4f", False),
    ]
    bars = []
    y = 64
    for label, val, w, color, inside in rows:
        bars.append(f'<text x="273" y="{y + 15}" fill="#7c8593" font-size="11.5" text-anchor="end" font-family="Menlo,monospace">{label}</text>')
        bars.append(f'<rect x="285" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        if inside:
            bars.append(f'<text x="{285 + w - 8}" y="{y + 15}" fill="#0a0e1a" font-size="11.5" font-weight="700" text-anchor="end" font-family="-apple-system,sans-serif">{val}</text>')
        else:
            bars.append(f'<text x="{285 + w + 8}" y="{y + 15}" fill="{color}" font-size="11.5" font-weight="700" font-family="-apple-system,sans-serif">{val}</text>')
        y += 52
    return f"""<figure>
<svg viewBox="0 0 700 240" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="285" y1="52" x2="285" y2="204" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(bars)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ls_feel_vs_learn(lang: str) -> str:
    """Deslauriers 2019: measured learning up, felt learning down."""
    t = {
        "zh": dict(title="同一批学生,两把尺子",
                   r1="实测成绩(随堂测验)", v1="+0.46 SD", r2="自感学到多少", v2="−0.56 SD",
                   zero="0",
                   cap="示意:Deslauriers 等 2019(哈佛物理导论,N=149,随机分组、讲义相同)——主动学习组实测多学 0.46 SD,自我感觉却少学 0.56 SD;与「读 14 遍最自信、记得最少」是同一个元认知现象"),
        "en": dict(title="Same students, two rulers",
                   r1="measured learning (test)", v1="+0.46 SD", r2="feeling of learning", v2="−0.56 SD",
                   zero="0",
                   cap="Schematic: Deslauriers et al. 2019 (intro physics at Harvard, N=149, randomized, identical handouts) — the active group measurably learned 0.46 SD more yet felt it learned 0.56 SD less; the same metacognitive illusion as “read it 14 times, most confident, remembered least”"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 220" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="380" y1="52" x2="380" y2="188" stroke="#5a6378" stroke-width="1.5"/>
  <text x="380" y="204" fill="#7c8593" font-size="11" text-anchor="middle" font-family="Menlo,monospace">{t['zero']}</text>
  <text x="225" y="85" fill="#7c8593" font-size="12" text-anchor="end" font-family="Menlo,monospace">{t['r1']}</text>
  <rect x="380" y="70" width="115" height="22" rx="5" fill="#52b788" opacity="0.9"/>
  <text x="503" y="86" fill="#52b788" font-size="13" font-weight="700" font-family="-apple-system,sans-serif">{t['v1']}</text>
  <text x="225" y="145" fill="#7c8593" font-size="12" text-anchor="end" font-family="Menlo,monospace">{t['r2']}</text>
  <rect x="240" y="130" width="140" height="22" rx="5" fill="#e85a4f" opacity="0.9"/>
  <text x="388" y="146" fill="#ff8a80" font-size="13" font-weight="700" font-family="-apple-system,sans-serif">{t['v2']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ls_ladder(lang: str) -> str:
    """The final evidence-tier table."""
    t = {
        "zh": dict(title="重排座次:证据等级表",
                   t1="一档:检索练习 · 间隔练习", s1="多 meta 收敛 · 课堂成立 · 偏倚检验干净;条件:反馈 + 延迟",
                   t2="二档:交错 · 主动学习 · 例题学习", s2="方向稳,幅度或边界存疑(词汇反向 · 0.47 SD 打折读 · 随专长反转)",
                   t3="三档:刻意练习", s3="结构化练习必要,但「一万小时」是包装——勘误后仅解释 14% 方差",
                   t4="四档:学习风格匹配 · 纯发现式教学", s4="合格检验反复失败;后者是两大对立学派唯一的共识敌人",
                   cap="示意:按效应稳健性 × 课堂证据 × 独立复现 × 偏倚检验四判据排出的座次;重读/划线为「低效用」而非无效"),
        "en": dict(title="The re-seated ranking: evidence tiers",
                   t1="Tier 1: retrieval practice · spaced practice", s1="converging metas · classroom-valid · clean bias checks; conditions: feedback + delay",
                   t2="Tier 2: interleaving · active learning · worked examples", s2="direction solid, size or borders in question (vocab reverses · discount 0.47 SD · reverses with expertise)",
                   t3="Tier 3: deliberate practice", s3="structured practice is necessary, but “10,000 hours” is packaging — 14% of variance post-corrigendum",
                   t4="Tier 4: styles matching · pure discovery", s4="fails qualified tests repeatedly; the latter is the one shared enemy of both opposing schools",
                   cap="Schematic: seating by four criteria — effect robustness × classroom evidence × independent replication × bias checks; rereading/highlighting are “low utility”, not useless"),
    }[lang]
    tiers = [
        (t['t1'], t['s1'], "#52b788"),
        (t['t2'], t['s2'], "#4cc9f0"),
        (t['t3'], t['s3'], "#f0b429"),
        (t['t4'], t['s4'], "#e85a4f"),
    ]
    boxes = []
    y = 50
    for main, sub, color in tiers:
        boxes.append(f'<rect x="24" y="{y}" width="652" height="54" rx="10" fill="{color}" opacity="0.10" stroke="{color}" stroke-opacity="0.5"/>')
        boxes.append(f'<text x="42" y="{y + 23}" fill="{color}" font-size="13" font-weight="700" font-family="-apple-system,sans-serif">{main}</text>')
        boxes.append(f'<text x="42" y="{y + 42}" fill="#8a93ad" font-size="10.5" font-family="-apple-system,sans-serif">{sub}</text>')
        y += 62
    return f"""<figure>
<svg viewBox="0 0 700 310" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  {''.join(boxes)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_mo_map(lang: str) -> str:
    """The four oracle categories (Barr 2015) with each cell's judge and LLM verdict."""
    t = {
        "zh": dict(title="判定「程序对不对」的四种裁判,AI 进场后各自的战绩",
                   sub="裁判(oracle)=判定程序行为对错的机制;按判据从哪来分四类(Barr et al. 2015)",
                   leg="✓ = AI 增益有独立硬数字 · ⚠ = 这一格的坑",
                   c1t="按规格书判 · Specified", c1j="裁判:证明检查器——照规格自动判卷",
                   c1a="✓", c1v="AI 证数学定理:完成率 88→90%",
                   c1b="⚠", c1w="但规格书(题目)本身可能是错的",
                   c2t="崩溃即错 · Implicit", c2j="裁判:崩溃 / 内存越界,不需要规格",
                   c2a="✓", c2v="AI 写探针:26 个真漏洞+20 年老 CVE",
                   c2b="⚠", c2w="并发 bug 这一格,AI 至今缺席",
                   c3t="对照着判 · Derived", c3j="裁判:另一个实现 / 旧版本 / 对照关系",
                   c3a="✓", c3v="AI 只当生成器:新挖 55 个数据库 bug",
                   c3b="⚠", c3w="AI 亲自当裁判:20 份报告全是误报",
                   c4t="人来判 · Human", c4j="裁判:维护者与安全团队人工分诊",
                   c4a="⚠", c4v="2025:AI 垃圾报告洪水,真报率 <5%",
                   c4b="✓", c4w="2026:报告质量反超,确认率 15-16%",
                   cap="示意:每格一个代表性战绩与一个坑,详见正文逐格对账;四格各用自己的指标,不可跨格比大小"),
        "en": dict(title="Four kinds of judges of 'is the program right?', and AI's record in each",
                   sub="An oracle = the judge of program behavior; four families by where the criterion comes from (Barr et al. 2015)",
                   leg="✓ = AI gain with hard independent numbers · ⚠ = the cell's trap",
                   c1t="Judged by spec · Specified", c1j="Judge: proof checkers — mechanical grading",
                   c1a="✓", c1v="AI proves math: completion 88→90%",
                   c1b="⚠", c1w="but the spec (the question) can be wrong",
                   c2t="Crash = wrong · Implicit", c2j="Judge: crashes / memory violations, no spec",
                   c2a="✓", c2v="AI probes: 26 real vulns + a 20-yr CVE",
                   c2b="⚠", c2w="concurrency bugs: AI still absent here",
                   c3t="Judged by contrast · Derived", c3j="Judge: another implementation / relations",
                   c3a="✓", c3v="AI as generator only: 55 new DB bugs",
                   c3b="⚠", c3w="AI as the judge: 20/20 reports false",
                   c4t="Humans judge · Human", c4j="Judge: maintainers and security triage",
                   c4a="⚠", c4v="2025: AI slop flood, real rate <5%",
                   c4b="✓", c4w="2026: quality overshoot, 15-16% confirmed",
                   cap="Schematic: one representative win and one trap per cell — see the essay for the full audit; each cell uses its own metric, no cross-cell comparison"),
    }[lang]
    cells = [
        (24, 96, t['c1t'], t['c1j'], t['c1a'], t['c1v'], t['c1b'], t['c1w'], "#4cc9f0"),
        (356, 96, t['c2t'], t['c2j'], t['c2a'], t['c2v'], t['c2b'], t['c2w'], "#5eead4"),
        (24, 278, t['c3t'], t['c3j'], t['c3a'], t['c3v'], t['c3b'], t['c3w'], "#7b61ff"),
        (356, 278, t['c4t'], t['c4j'], t['c4a'], t['c4v'], t['c4b'], t['c4w'], "#ff6ec4"),
    ]
    parts = []
    for x, y, title, judge, i1, l1, i2, l2, color in cells:
        col1 = "#dde1ea" if i1 == "✓" else "#f0b429"
        col2 = "#dde1ea" if i2 == "✓" else "#f0b429"
        parts.append(f'<rect x="{x}" y="{y}" width="320" height="162" rx="12" fill="{color}" opacity="0.07" stroke="{color}" stroke-opacity="0.45"/>')
        parts.append(f'<text x="{x + 16}" y="{y + 30}" fill="{color}" font-size="13.5" font-weight="700" font-family="-apple-system,sans-serif">{title}</text>')
        parts.append(f'<text x="{x + 16}" y="{y + 56}" fill="#a8b0c0" font-size="10.5" font-family="-apple-system,sans-serif">{judge}</text>')
        parts.append(f'<text x="{x + 16}" y="{y + 94}" fill="{col1}" font-size="11.5" font-family="-apple-system,sans-serif">{i1} {l1}</text>')
        parts.append(f'<text x="{x + 16}" y="{y + 126}" fill="{col2}" font-size="11.5" font-family="-apple-system,sans-serif">{i2} {l2}</text>')
    return f"""<figure>
<svg viewBox="0 0 700 466" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="24" y="58" fill="#7c8593" font-size="11" font-family="-apple-system,sans-serif">{t['sub']}</text>
  <text x="24" y="78" fill="#7c8593" font-size="11" font-family="-apple-system,sans-serif">{t['leg']}</text>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_mo_seats(lang: str) -> str:
    """The three seats an LLM can take in a verification chain, with verdicts."""
    t = {
        "zh": dict(title="同一个 AI,三把椅子,三种成色",
                   s1t="干活的(生成器)", s1d="产测试输入 / fuzz 探针,判决全在机器闸", s1e="挖出 26 个真漏洞 · 采纳率 73%", s1v="增益有硬数字",
                   s2t="起草的(提议者)", s2d="起草规则 / 规约,先过独立筛再上岗", s2e="证明器把关后:误报 0/20", s2v="真增益,筛完人工不省",
                   s3t="当裁判的", s3d="直接判对错 / 分诊 / 打分", s3e="独立复测:精度 0.38% · F1 3%", s3v="复测后系统性缩水",
                   cap="示意:判据不是「用没用 AI」,是裁决权在谁手里——判决全在独立机制(左)到判决就是 AI 本身(右);数字详见正文"),
        "en": dict(title="One AI, three seats, three grades",
                   s1t="Worker (generator)", s1d="makes test inputs / probes; machines judge", s1e="26 real vulns · 73% accepted", s1v="hard-numbered gains",
                   s2t="Drafter (proposer)", s2d="drafts rules / specs, filtered before duty", s2e="behind a prover: 0/20 FPs", s2v="real gains, human toll stays",
                   s3t="Judge", s3d="rules directly / triages / scores", s3e="re-tested: 0.38% precision · 3% F1", s3v="shrinks under re-testing",
                   cap="Schematic: the criterion is not whether AI is used, but who holds adjudication — from fully independent mechanisms (left) to the AI itself being the verdict (right); numbers detailed in the essay"),
    }[lang]
    seats = [
        (24, t['s1t'], t['s1d'], t['s1e'], t['s1v'], "#52b788"),
        (250, t['s2t'], t['s2d'], t['s2e'], t['s2v'], "#f0b429"),
        (476, t['s3t'], t['s3d'], t['s3e'], t['s3v'], "#ff6ec4"),
    ]
    parts = []
    for x, title, desc, ev, verdict, color in seats:
        parts.append(f'<rect x="{x}" y="58" width="200" height="200" rx="12" fill="{color}" opacity="0.08" stroke="{color}" stroke-opacity="0.5"/>')
        parts.append(f'<text x="{x + 100}" y="88" fill="{color}" font-size="14" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{title}</text>')
        parts.append(f'<text x="{x + 100}" y="118" fill="#a8b0c0" font-size="10.5" text-anchor="middle" font-family="-apple-system,sans-serif">{desc}</text>')
        parts.append(f'<text x="{x + 100}" y="164" fill="#dde1ea" font-size="10.5" text-anchor="middle" font-family="Menlo,monospace">{ev}</text>')
        parts.append(f'<rect x="{x + 18}" y="196" width="164" height="34" rx="8" fill="{color}" opacity="0.16"/>')
        parts.append(f'<text x="{x + 100}" y="218" fill="{color}" font-size="11.5" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{verdict}</text>')
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_mo_shrink(lang: str) -> str:
    """Claimed vs independently re-tested numbers when the LLM defines/judges."""
    t = {
        "zh": dict(title="LLM 坐裁判席:声称 vs 独立复测",
                   r1="漏洞检测 F1:旧基准 BigVul → 去污染 PrimeVul", r1a="68.26%", r1b="3.09%",
                   r2="Semgrep 分诊一致率:头条 → 误报侧", r2a="96%", r2b="41%",
                   r3="LLM 测试覆盖率:旧基准 → 未污染 ULT", r3a="92.18%", r3b="45.10%",
                   r4="AI 断言工具 TOGA:原评测 → 修正评测漏洞后的精度", r4a="声称 30 个独家 bug", r4b="0.38%",
                   la="声称 / 旧口径", lb="独立复测",
                   cap="示意:四组各自口径不同、不可互比,只看各组内的缩水方向(条长为示意;PrimeVul/ULT/TOGA 为独立学术复测,Semgrep 为同一博客的头条 vs 细则)"),
        "en": dict(title="LLM in the judge seat: claimed vs independently re-tested",
                   r1="Vuln-detection F1: old BigVul → de-leaked PrimeVul", r1a="68.26%", r1b="3.09%",
                   r2="Semgrep triage agreement: headline → FP side", r2a="96%", r2b="41%",
                   r3="LLM test coverage: old bench → uncontaminated ULT", r3a="92.18%", r3b="45.10%",
                   r4="AI assertion tool TOGA: original eval → precision after fixing the eval leak", r4a="claimed 30 exclusive bugs", r4b="0.38%",
                   la="claimed / old scope", lb="independent re-test",
                   cap="Schematic: four pairs with four different metrics — compare only the within-pair shrink direction (bar lengths illustrative; PrimeVul/ULT/TOGA are independent academic re-tests, Semgrep is headline vs fine print of one blog post)"),
    }[lang]
    rows = [
        (t['r1'], t['r1a'], 273, t['r1b'], 13),
        (t['r2'], t['r2a'], 384, t['r2b'], 164),
        (t['r3'], t['r3a'], 369, t['r3b'], 180),
        (t['r4'], t['r4a'], 240, t['r4b'], 8),
    ]
    parts = []
    y = 84
    for label, va, wa, vb, wb in rows:
        parts.append(f'<text x="24" y="{y}" fill="#a8b0c0" font-size="11.5" font-family="-apple-system,sans-serif">{label}</text>')
        by = y + 10
        parts.append(f'<rect x="24" y="{by}" width="{wa}" height="14" rx="4" fill="#4cc9f0" opacity="0.75"/>')
        parts.append(f'<text x="{24 + wa + 8}" y="{by + 11}" fill="#4cc9f0" font-size="11" font-weight="700" font-family="Menlo,monospace">{va}</text>')
        by2 = by + 20
        parts.append(f'<rect x="24" y="{by2}" width="{max(wb, 4)}" height="14" rx="4" fill="#ff6ec4" opacity="0.9"/>')
        parts.append(f'<text x="{24 + max(wb, 4) + 8}" y="{by2 + 11}" fill="#ff6ec4" font-size="11" font-weight="700" font-family="Menlo,monospace">{vb}</text>')
        y += 82
    return f"""<figure>
<svg viewBox="0 0 700 440" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <rect x="24" y="48" width="12" height="12" rx="3" fill="#4cc9f0" opacity="0.75"/>
  <text x="42" y="58" fill="#7c8593" font-size="11" font-family="Menlo,monospace">{t['la']}</text>
  <rect x="220" y="48" width="12" height="12" rx="3" fill="#ff6ec4" opacity="0.9"/>
  <text x="238" y="58" fill="#7c8593" font-size="11" font-family="Menlo,monospace">{t['lb']}</text>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_mo_argus(lang: str) -> str:
    """Argus judge-swap ablation: prover-gated vs GPT-5-judged false positives."""
    t = {
        "zh": dict(title="只换裁判的消融(Argus,SIGMOD 2026,DuckDB 上 20 份 bug 报告)",
                   b1="SQLSolver 证明器把关(LLM 只提议)", v1="误报 0/20",
                   b2="GPT-5 当裁判(同一框架)", v2="误报 20/20",
                   note="机制:LLM 单次判定错误率仅约 1/20,但成熟 DBMS 真 bug 底率极低 → 报告层面误报被放大到 100%",
                   cap="示意:同一框架、同一 DBMS、人工逐条终裁——低错误率 × 极低底率 = 误报淹没真报(误报数为人工裁定口径)"),
        "en": dict(title="The judge-swap ablation (Argus, SIGMOD 2026; 20 bug reports on DuckDB)",
                   b1="SQLSolver prover gates (LLM only proposes)", v1="0/20 false positives",
                   b2="GPT-5 as the judge (same framework)", v2="20/20 false positives",
                   note="Mechanism: the LLM errs on only ~1/20 calls, but true-bug base rates in mature DBMSs are so low that report-level FPs amplify to 100%",
                   cap="Schematic: same framework, same DBMS, human final adjudication per report — low error rate × very low base rate = false alarms drown true ones"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 280" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="24" y="80" fill="#a8b0c0" font-size="12" font-family="-apple-system,sans-serif">{t['b1']}</text>
  <rect x="24" y="90" width="8" height="22" rx="4" fill="#52b788"/>
  <text x="44" y="107" fill="#52b788" font-size="15" font-weight="700" font-family="Menlo,monospace">{t['v1']}</text>
  <text x="24" y="156" fill="#a8b0c0" font-size="12" font-family="-apple-system,sans-serif">{t['b2']}</text>
  <rect x="24" y="166" width="560" height="22" rx="4" fill="#ff6ec4" opacity="0.85"/>
  <text x="594" y="183" fill="#ff6ec4" font-size="15" font-weight="700" font-family="Menlo,monospace">{t['v2']}</text>
  <rect x="24" y="216" width="652" height="40" rx="8" fill="#f0b429" opacity="0.10" stroke="#f0b429" stroke-opacity="0.4"/>
  <text x="38" y="241" fill="#f0b429" font-size="11.5" font-family="-apple-system,sans-serif">{t['note']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_mo_curl(lang: str) -> str:
    """curl's two-act play: confirmation rate over time under a human judge."""
    t = {
        "zh": dict(title="curl 安全报告确认率:人类裁判格的两幕剧",
                   p1="2019-2024 · 赏金时代", v1=">15%", p2="2025 · AI slop 洪水(约 20% 是 slop)", v2="<5%",
                   p3="2026-01 · 关闭七年赏金", v3="—", p4="2026-04 · 重返后反超(几乎全用 AI)", v4="15-16%",
                   cap="示意:同一项目、同一人类裁判、同一确认率口径(真漏洞/全部安全提交,Stenberg 一手时间序列)——洪水受赏金激励与工具代际调制,不是恒久定律"),
        "en": dict(title="curl's security-report confirmation rate: the human-judge cell's two acts",
                   p1="2019-2024 · bounty era", v1=">15%", p2="2025 · AI slop flood (~20% slop)", v2="<5%",
                   p3="2026-01 · 7-year bounty closed", v3="—", p4="2026-04 · post-return overshoot (nearly all AI-assisted)", v4="15-16%",
                   cap="Schematic: same project, same human judges, same metric (real vulns / all security submissions; Stenberg's first-party time series) — the flood is modulated by bounty incentives and tool generations, not a permanent law"),
    }[lang]
    rows = [
        (t['p1'], t['v1'], 170, "#4cc9f0"),
        (t['p2'], t['v2'], 48, "#ff6ec4"),
        (t['p3'], t['v3'], 4, "#5a6378"),
        (t['p4'], t['v4'], 178, "#52b788"),
    ]
    parts = []
    y = 70
    for label, val, w, color in rows:
        parts.append(f'<text x="360" y="{y + 15}" fill="#7c8593" font-size="11.5" text-anchor="end" font-family="-apple-system,sans-serif">{label}</text>')
        parts.append(f'<rect x="372" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        parts.append(f'<text x="{372 + w + 10}" y="{y + 15}" fill="{color}" font-size="13" font-weight="700" font-family="Menlo,monospace">{val}</text>')
        y += 52
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="372" y1="58" x2="372" y2="270" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_sp_life(lang: str) -> str:
    """Timeline: the 70% number circulating (top) vs corrections/debunks (bottom)."""
    t = {
        "zh": dict(title="「70%」的一生:上轨在流通,下轨在辟谣",
                   leg_a="● 上轨:数字被引用/强化", leg_b="● 下轨:收回与验尸(几乎无人引用)",
                   t1="1993:『非科学估计』出生,只限流程再造", t2="2000:升级为『残酷的事实』,无出处",
                   t3="2008-09:Kotter『我估计』+ 麦肯锡发明出处", t4="2024:宿主换成 AI 转型",
                   b1="1995:作者收回,『不存在固有失败率』", b2="2011:Hughes 验尸,『无有效可靠实证』",
                   cap="示意:数字每次变异都更响亮(上轨),两次纠偏几乎无人引用(下轨)——正文第 1 节是本图的逐条展开"),
        "en": dict(title="The life of '70%': circulation above, debunking below",
                   leg_a="● top: the number cited / strengthened", leg_b="● bottom: retraction &amp; autopsy (rarely cited)",
                   t1="1993: born 'unscientific', reengineering only", t2="2000: upgraded to 'brutal fact', unsourced",
                   t3="2008-09: Kotter 'I estimate' + McKinsey invents source", t4="2024: new host, AI transformation",
                   b1="1995: authors retract, 'no inherent failure rate'", b2="2011: Hughes autopsy, 'no valid evidence'",
                   cap="Schematic: every mutation got louder (top track) while both corrections went uncited (bottom) — section 1 unpacks each dot"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="24" y="52" fill="#4cc9f0" font-size="11" font-family="-apple-system,sans-serif">{t['leg_a']}</text>
  <text x="24" y="304" fill="#ff6ec4" font-size="11" font-family="-apple-system,sans-serif">{t['leg_b']}</text>
  <line x1="40" y1="165" x2="660" y2="165" stroke="#5a6378" stroke-width="1.5"/>
  <text x="52" y="183" fill="#7c8593" font-size="11" font-family="Menlo,monospace">1993</text>
  <text x="330" y="183" fill="#7c8593" font-size="11" font-family="Menlo,monospace">2009</text>
  <text x="620" y="183" fill="#7c8593" font-size="11" font-family="Menlo,monospace">2026</text>

  <circle cx="70" cy="165" r="5" fill="#4cc9f0"/>
  <line x1="70" y1="160" x2="70" y2="106" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="46" y="100" fill="#4cc9f0" font-size="11" font-family="-apple-system,sans-serif">{t['t1']}</text>

  <circle cx="200" cy="165" r="5" fill="#4cc9f0"/>
  <line x1="200" y1="160" x2="200" y2="70" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="176" y="64" fill="#4cc9f0" font-size="11" font-family="-apple-system,sans-serif">{t['t2']}</text>

  <circle cx="352" cy="165" r="5" fill="#7b61ff"/>
  <line x1="352" y1="160" x2="352" y2="128" stroke="#7b61ff" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="328" y="122" fill="#a29bfe" font-size="11" font-weight="700" font-family="-apple-system,sans-serif">{t['t3']}</text>

  <circle cx="612" cy="165" r="5" fill="#4cc9f0"/>
  <line x1="612" y1="160" x2="612" y2="92" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="688" y="86" fill="#4cc9f0" font-size="11" text-anchor="end" font-family="-apple-system,sans-serif">{t['t4']}</text>

  <circle cx="115" cy="165" r="5" fill="#ff6ec4"/>
  <line x1="115" y1="170" x2="115" y2="212" stroke="#ff6ec4" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="60" y="228" fill="#ff6ec4" font-size="11" font-family="-apple-system,sans-serif">{t['b1']}</text>

  <circle cx="445" cy="165" r="5" fill="#ff6ec4"/>
  <line x1="445" y1="170" x2="445" y2="248" stroke="#ff6ec4" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="380" y="264" fill="#ff6ec4" font-size="11" font-family="-apple-system,sans-serif">{t['b2']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_sp_gauge(lang: str) -> str:
    """Two stacked bars: same self-reported data, packaged as 70%/88% failure."""
    t = {
        "zh": dict(title="定义机器:同一批数据,两种成绩单",
                   h1="BCG 2020:数字化转型(825 名高管自评)", s1a="30% 达标", s1b="44% 有价值但未达标", s1c="26% 价值有限",
                   br1="→ 打包卖出:『70% fall short』",
                   h2="Bain 2024:企业转型(400+ 名高管自评)", s2a="12%", s2b="约 75% 完成过半、未达最初雄心", s2c="~13%",
                   br2="→ 打包卖出:『88% 未达雄心』(同一批数据:约 87% 至少完成一半)",
                   cap="示意:及格线设在「完美」,失败率想多高有多高;分段为各报告自己的拆分,正文 2.4 节逐条展开"),
        "en": dict(title="The definition machine: one dataset, two report cards",
                   h1="BCG 2020: digital transformations (825 executives, self-graded)", s1a="30% met targets", s1b="44% created value, missed targets", s1c="26% limited value",
                   br1="→ packaged as: '70% fall short'",
                   h2="Bain 2024: business transformations (400+ executives, self-graded)", s2a="12%", s2b="~75% got at least halfway, short of full ambition", s2c="~13%",
                   br2="→ packaged as: '88% fail' (same data: ~87% achieved at least half)",
                   cap="Schematic: set the pass bar at 'perfect' and the failure rate is whatever you need; segments are each report's own breakdown — section 2.4 unpacks both"),
    }[lang]
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>

  <text x="60" y="72" fill="#7c8593" font-size="11" font-family="-apple-system,sans-serif">{t['h1']}</text>
  <rect x="60" y="82" width="168" height="24" fill="#52b788" opacity="0.85"/>
  <rect x="228" y="82" width="246" height="24" fill="#4cc9f0" opacity="0.85"/>
  <rect x="474" y="82" width="146" height="24" fill="#e8794b" opacity="0.85"/>
  <text x="66" y="98" fill="#0f1115" font-size="10.5" font-weight="700" font-family="-apple-system,sans-serif">{t['s1a']}</text>
  <text x="234" y="98" fill="#0f1115" font-size="10.5" font-weight="700" font-family="-apple-system,sans-serif">{t['s1b']}</text>
  <text x="480" y="98" fill="#0f1115" font-size="10.5" font-weight="700" font-family="-apple-system,sans-serif">{t['s1c']}</text>
  <path d="M 228 112 L 228 120 L 620 120 L 620 112" stroke="#ff6ec4" stroke-width="1.5" fill="none"/>
  <text x="424" y="136" fill="#ff6ec4" font-size="11" text-anchor="middle" font-family="-apple-system,sans-serif">{t['br1']}</text>

  <text x="60" y="182" fill="#7c8593" font-size="11" font-family="-apple-system,sans-serif">{t['h2']}</text>
  <rect x="60" y="192" width="67" height="24" fill="#52b788" opacity="0.85"/>
  <rect x="127" y="192" width="420" height="24" fill="#4cc9f0" opacity="0.85"/>
  <rect x="547" y="192" width="73" height="24" fill="#e8794b" opacity="0.85"/>
  <text x="66" y="208" fill="#0f1115" font-size="10.5" font-weight="700" font-family="-apple-system,sans-serif">{t['s2a']}</text>
  <text x="133" y="208" fill="#0f1115" font-size="10.5" font-weight="700" font-family="-apple-system,sans-serif">{t['s2b']}</text>
  <text x="553" y="208" fill="#0f1115" font-size="10.5" font-weight="700" font-family="-apple-system,sans-serif">{t['s2c']}</text>
  <path d="M 127 222 L 127 230 L 620 230 L 620 222" stroke="#ff6ec4" stroke-width="1.5" fill="none"/>
  <text x="373" y="248" fill="#ff6ec4" font-size="11" text-anchor="middle" font-family="-apple-system,sans-serif">{t['br2']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_sp_fattail(lang: str) -> str:
    """Bar rows: mean overrun vs fat-tail overruns (Flyvbjerg)."""
    t = {
        "zh": dict(title="实测的危险是肥尾,不是「多数失败」(Flyvbjerg 项目库)",
                   r1="IT 项目平均成本超支(约 1.6 万项目库)", v1="+73%",
                   r2="六分之一『黑天鹅』项目的平均超支", v2="+200%",
                   r3="超支>50% 的那 18% IT 项目的平均超支", v3="+447%",
                   cap="示意:均值可控、尾部致命——以决策时点为基线、实际价格计;bar 长度按数值等比,正文 2.2 节含口径与争议"),
        "en": dict(title="The measured danger is the fat tail, not 'most fail' (Flyvbjerg database)",
                   r1="Mean IT cost overrun (~16,000-project database)", v1="+73%",
                   r2="Mean overrun of the 1-in-6 'Black Swan' projects", v2="+200%",
                   r3="Mean overrun of the 18% of IT projects >50% over", v3="+447%",
                   cap="Schematic: the mean is survivable, the tail is lethal — decision-to-build baseline, real terms; bars proportional to values, caveats in section 2.2"),
    }[lang]
    rows = [
        (t['r1'], t['v1'], 42, "#4cc9f0"),
        (t['r2'], t['v2'], 116, "#ff6ec4"),
        (t['r3'], t['v3'], 260, "#e8794b"),
    ]
    parts = []
    y = 70
    for label, val, w, color in rows:
        parts.append(f'<text x="360" y="{y + 15}" fill="#7c8593" font-size="11.5" text-anchor="end" font-family="-apple-system,sans-serif">{label}</text>')
        parts.append(f'<rect x="372" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        parts.append(f'<text x="{372 + w + 10}" y="{y + 15}" fill="{color}" font-size="13" font-weight="700" font-family="Menlo,monospace">{val}</text>')
        y += 52
    return f"""<figure>
<svg viewBox="0 0 700 250" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="372" y1="58" x2="372" y2="220" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_sp_archive(lang: str) -> str:
    """Two-column comparison of the Agile vs DevOps archives."""
    t = {
        "zh": dict(title="两轮转型留下的档案,对照读",
                   ha="Agile 档案(2001-2025)", hb="DevOps 档案(2014-2025)",
                   r1="测量方式", a1="情绪问卷,厂商自办、样本自选", b1="结果指标(四键),可用自家数据复算",
                   r2="档案要害", a2="『文化/领导层』障碍连续十七年居首", b2="2022 精英集群消失,年际不可比",
                   r3="框架与证据", a3="SAFe:九年零项独立受控研究", b3="能力→绩效模型无独立复现",
                   r4="具名退场", a4="Capital One 裁撤约 1,100 敏捷岗", b4="GE:150 亿美元目标 → 12 亿实际收入",
                   cap="示意:一波比一波测得认真,但都测不出「行业失败率」;正文第 3、4 节逐格展开"),
        "en": dict(title="Two waves, two archives, side by side",
                   ha="The Agile archive (2001-2025)", hb="The DevOps archive (2014-2025)",
                   r1="Method", a1="Sentiment surveys, vendor-run, self-selected", b1="Outcome metrics (four keys), recomputable",
                   r2="The tell", a2="'Culture/leadership' top challenge for 17 years", b2="2022: elite cluster vanished; years not comparable",
                   r3="Frameworks", a3="SAFe: zero independent controlled studies in 9 yrs", b3="Path model never independently replicated",
                   r4="Retreat", a4="Capital One cut ~1,100 agile roles", b4="GE: $15B target → $1.2B revenue at carve-out",
                   cap="Schematic: each wave measured harder than the last, and neither could produce an industry failure rate — sections 3-4 unpack each cell"),
    }[lang]
    rows = [(t['r1'], t['a1'], t['b1']), (t['r2'], t['a2'], t['b2']), (t['r3'], t['a3'], t['b3']), (t['r4'], t['a4'], t['b4'])]
    parts = []
    y = 100
    for rl, a, b in rows:
        parts.append(f'<text x="24" y="{y}" fill="#7c8593" font-size="10.5" font-family="-apple-system,sans-serif">{rl}</text>')
        parts.append(f'<text x="100" y="{y}" fill="#e4e6eb" font-size="11" font-family="-apple-system,sans-serif">{a}</text>')
        parts.append(f'<text x="400" y="{y}" fill="#e4e6eb" font-size="11" font-family="-apple-system,sans-serif">{b}</text>')
        parts.append(f'<line x1="24" y1="{y + 16}" x2="676" y2="{y + 16}" stroke="#2a3040" stroke-width="1"/>')
        y += 52
    return f"""<figure>
<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="100" y="64" fill="#ff6ec4" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['ha']}</text>
  <text x="400" y="64" fill="#4cc9f0" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['hb']}</text>
  <line x1="392" y1="48" x2="392" y2="290" stroke="#5a6378" stroke-width="1" stroke-dasharray="2,4"/>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_sp_transfer(lang: str) -> str:
    """Two panels: mechanisms replaying in AI adoption vs structural breaks."""
    t = {
        "zh": dict(title="上一轮剧本 vs 这一轮现实",
                   ha="在重演的机制", hb="断裂的条件",
                   a1="跟风投资:64% 的 CEO 自认先投钱后理解", a2="指标考核:Duolingo 12 个月走完强制→撤销",
                   a3="仪式采纳:仅 21% 重设计过工作流", a4="认证工业:AI 认证升至近三成,约 20 倍",
                   b1="方向倒转:78% 自带工具、57% 隐瞒使用", b2="工具在变强:能力约每 7 个月翻倍",
                   b3="按席位收费的工具层(咨询层照涨,算半条)",
                   cap="示意:组织机制在原样重演(左),但三个结构条件是上一轮档案里没有的(右)——正文第 7 节逐条展开"),
        "en": dict(title="Last wave's script vs this wave's reality",
                   ha="Mechanisms replaying", hb="Conditions that broke",
                   a1="Herd: 64% of CEOs invest before seeing value", a2="Mandates: Duolingo, mandate→retreat in 12 months",
                   a3="Ritual: only 21% redesigned workflows", a4="Cert boom: AI certs near 30%, ~20x pre-ChatGPT",
                   b1="Inverted: 78% BYOAI, 57% hide their use", b2="Capability doubles ~every 7 months",
                   b3="Seat-based SaaS layer (half a break)",
                   cap="Schematic: the organizational machinery replays (left) while three structural conditions have no precedent in the last archive (right) — section 7 unpacks each"),
    }[lang]
    la = [t['a1'], t['a2'], t['a3'], t['a4']]
    lb = [t['b1'], t['b2'], t['b3']]
    parts = []
    y = 96
    for item in la:
        parts.append(f'<circle cx="34" cy="{y - 4}" r="3" fill="#ff6ec4"/>')
        parts.append(f'<text x="46" y="{y}" fill="#e4e6eb" font-size="11" font-family="-apple-system,sans-serif">{item}</text>')
        y += 44
    y = 96
    for item in lb:
        parts.append(f'<circle cx="374" cy="{y - 4}" r="3" fill="#4cc9f0"/>')
        parts.append(f'<text x="386" y="{y}" fill="#e4e6eb" font-size="11" font-family="-apple-system,sans-serif">{item}</text>')
        y += 44
    return f"""<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="24" y="64" fill="#ff6ec4" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['ha']}</text>
  <text x="364" y="64" fill="#4cc9f0" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['hb']}</text>
  <line x1="352" y1="48" x2="352" y2="270" stroke="#5a6378" stroke-width="1" stroke-dasharray="2,4"/>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ai_lab(lang: str) -> str:
    """1993 founding complacency experiment: detection rates under three conditions."""
    t = {
        "zh": dict(title="1993 奠基实验:人抓住自动化故障的比例",
                   r1="自动化恒定可靠 · 人在多任务", v1="33%",
                   r2="自动化偶尔出错 · 人在多任务", v2="82%",
                   r3="单任务纯监控(对照条件)", v3="约 97%",
                   cap="示意:Parasuraman, Molloy & Singh 1993(大学生、MATB 多任务平台)——从不出错的自动化教会注意力离开;注意实验室故障率远高于真实系统,外推受限(正文第 3 章)"),
        "en": dict(title="The 1993 founding experiment: detecting automation failures",
                   r1="Constantly reliable automation · multitasking", v1="33%",
                   r2="Occasionally failing automation · multitasking", v2="82%",
                   r3="Single-task pure monitoring (control)", v3="~97%",
                   cap="Schematic: Parasuraman, Molloy & Singh 1993 (students, MATB multitask platform) — automation that never fails teaches attention to leave; lab failure rates far exceed real systems, so extrapolate with care (Chapter 3)"),
    }[lang]
    rows = [(t['r1'], t['v1'], 33, "#ff6ec4"), (t['r2'], t['v2'], 82, "#4cc9f0"), (t['r3'], t['v3'], 97, "#52b788")]
    bars = []
    y = 70
    for label, val, pct, color in rows:
        w = int(pct * 3.0)
        bars.append(f'<text x="326" y="{y + 15}" fill="#7c8593" font-size="11.5" text-anchor="end" font-family="Menlo,monospace">{label}</text>')
        bars.append(f'<rect x="338" y="{y}" width="{w}" height="20" rx="5" fill="{color}" opacity="0.85"/>')
        bars.append(f'<text x="{338 + w + 8}" y="{y + 15}" fill="{color}" font-size="12.5" font-weight="700" font-family="-apple-system,sans-serif">{val}</text>')
        y += 54
    return f"""<figure>
<svg viewBox="0 0 700 250" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="32" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <line x1="338" y1="58" x2="338" y2="228" stroke="#5a6378" stroke-width="1.5" stroke-dasharray="2,4"/>
  {''.join(bars)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ai_tension(lang: str) -> str:
    """The two ledgers: in-use gain vs post-withdrawal decay (colonoscopy ADR)."""
    t = {
        "zh": dict(title="同一项技术的两本账:AI 辅助肠镜的腺瘤检出率(ADR)",
                   ha="账本一:AI 在场时(21 项 RCT 的 meta)", hb="账本二:AI 撤走后(单一观察性研究)",
                   a1="标准肠镜", a2="AI 辅助", b1="引入 AI 前", b2="引入 AI 后",
                   an="35.9% → 44.0%(多源证实)", bn="28.4% → 22.4%(待确认假说)",
                   cap="示意:左=Hassan 2023 RCT meta(在场增益,RR 1.24);右=Budzyń 2025(资深医生无 AI 肠镜,-6.0pp,观察性、混杂未除)——部署评估必须同时记两本账(正文第 5 章)"),
        "en": dict(title="Two ledgers, one technology: adenoma detection rate (ADR) in colonoscopy",
                   ha="Ledger 1: with AI present (meta of 21 RCTs)", hb="Ledger 2: after AI removed (one observational study)",
                   a1="Standard", a2="AI-assisted", b1="Before AI era", b2="After AI era",
                   an="35.9% → 44.0% (multi-source)", bn="28.4% → 22.4% (unconfirmed hypothesis)",
                   cap="Schematic: left = Hassan 2023 RCT meta (in-use gain, RR 1.24); right = Budzyń 2025 (senior physicians' non-AI colonoscopies, −6.0pp, observational, confounds unexcluded) — deployment evaluation must keep both books (Chapter 5)"),
    }[lang]
    def vbar(x, pct, color, label):
        h = int(pct * 3.4)
        y0 = 250 - h
        return (f'<rect x="{x}" y="{y0}" width="72" height="{h}" rx="6" fill="{color}" opacity="0.85"/>'
                f'<text x="{x + 36}" y="{y0 - 8}" fill="{color}" font-size="12.5" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{pct}%</text>'
                f'<text x="{x + 36}" y="272" fill="#7c8593" font-size="11" text-anchor="middle" font-family="Menlo,monospace">{label}</text>')
    return f"""<figure>
<svg viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="60" y="62" fill="#4cc9f0" font-size="11.5" font-weight="700" font-family="-apple-system,sans-serif">{t['ha']}</text>
  <text x="390" y="62" fill="#ff6ec4" font-size="11.5" font-weight="700" font-family="-apple-system,sans-serif">{t['hb']}</text>
  <line x1="352" y1="50" x2="352" y2="290" stroke="#5a6378" stroke-width="1" stroke-dasharray="2,4"/>
  <line x1="60" y1="250" x2="320" y2="250" stroke="#5a6378" stroke-width="1.5"/>
  <line x1="390" y1="250" x2="650" y2="250" stroke="#5a6378" stroke-width="1.5"/>
  {vbar(100, 35.9, "#4cc9f0", t['a1'])}
  {vbar(210, 44.0, "#52b788", t['a2'])}
  {vbar(430, 28.4, "#7b61ff", t['b1'])}
  {vbar(540, 22.4, "#ff6ec4", t['b2'])}
  <text x="190" y="300" fill="#52b788" font-size="11.5" text-anchor="middle" font-weight="700" font-family="-apple-system,sans-serif">{t['an']}</text>
  <text x="520" y="300" fill="#ff6ec4" font-size="11.5" text-anchor="middle" font-weight="700" font-family="-apple-system,sans-serif">{t['bn']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ai_dratsch(lang: str) -> str:
    """Radiologists' accuracy with correct vs wrong AI advice, by experience."""
    t = {
        "zh": dict(title="AI 建议错误时,放射科医生的判读准确率崩塌(Dratsch 2023)",
                   g1="低年资组", g2="中年资组", g3="资深组",
                   lc="AI 建议正确时", lw="AI 建议错误时",
                   cap="示意:27 名放射科医生读乳腺X光,AI 提示为实验操纵;资历只买到部分抵抗力——「无论资历,所有放射科医生都可能发生 automation bias」(正文第 5 章)"),
        "en": dict(title="Radiologists' accuracy collapses under wrong AI advice (Dratsch 2023)",
                   g1="Inexperienced", g2="Moderately exp.", g3="Very experienced",
                   lc="With correct AI advice", lw="With wrong AI advice",
                   cap="Schematic: 27 radiologists reading mammograms, AI prompts experimentally manipulated; seniority buys only partial resistance — 'all radiologists, regardless of expertise, can be subject to automation bias' (Chapter 5)"),
    }[lang]
    groups = [(t['g1'], 79.7, 19.8, 90), (t['g2'], 81.3, 24.8, 300), (t['g3'], 82.3, 45.5, 510)]
    parts = []
    for label, ok, bad, x in groups:
        h1, h2 = int(ok * 2.2), int(bad * 2.2)
        parts.append(f'<rect x="{x}" y="{280 - h1}" width="52" height="{h1}" rx="5" fill="#4cc9f0" opacity="0.8"/>')
        parts.append(f'<text x="{x + 26}" y="{280 - h1 - 7}" fill="#4cc9f0" font-size="11.5" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{ok}%</text>')
        parts.append(f'<rect x="{x + 60}" y="{280 - h2}" width="52" height="{h2}" rx="5" fill="#ff6ec4" opacity="0.85"/>')
        parts.append(f'<text x="{x + 86}" y="{280 - h2 - 7}" fill="#ff6ec4" font-size="11.5" font-weight="700" text-anchor="middle" font-family="-apple-system,sans-serif">{bad}%</text>')
        parts.append(f'<text x="{x + 56}" y="302" fill="#7c8593" font-size="11.5" text-anchor="middle" font-family="Menlo,monospace">{label}</text>')
    return f"""<figure>
<svg viewBox="0 0 700 360" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="14.5" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <rect x="440" y="44" width="12" height="12" rx="3" fill="#4cc9f0" opacity="0.8"/>
  <text x="458" y="55" fill="#a8b4d0" font-size="11.5" font-family="-apple-system,sans-serif">{t['lc']}</text>
  <rect x="440" y="64" width="12" height="12" rx="3" fill="#ff6ec4" opacity="0.85"/>
  <text x="458" y="75" fill="#a8b4d0" font-size="11.5" font-family="-apple-system,sans-serif">{t['lw']}</text>
  <line x1="60" y1="280" x2="660" y2="280" stroke="#5a6378" stroke-width="1.5"/>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ai_levers(lang: str) -> str:
    """Intervention scorecard: what measurably works, with costs; what doesn't."""
    t = {
        "zh": dict(title="干预杠杆记分卡:40 年实测",
                   h1="有实测效果(各有代价)", h2="实测无效", h3="缺最后一公里",
                   a1="亲历 AI 失效的演习(非口头告知)", a2="对总体结果的个人问责",
                   a3="决策时点的行为 nudge", a4="把核验成本降到一眼可核对",
                   a5="定期手动剂量(需核查落地)", a6="认知强制:子任务层有效,感知更复杂",
                   b1="叮嘱「请核对 AI 建议」", b2="说教式培训 / 20 小时通识课", b3="单纯增加透明度",
                   c1="适应性自动化(动态轮换控制权):", c2="模拟环境有效 30 年,无运营部署评估",
                   cap="示意:每条的效应量、边界条件与代价见正文第 8 章;「有效」不等于普适,多数效应依设计而定"),
        "en": dict(title="Intervention scorecard: forty years of measurements",
                   h1="Measured effective (each with a cost)", h2="Measured ineffective", h3="Missing its last mile",
                   a1="Drills with experienced AI failures (not briefings)", a2="Personal accountability for overall outcomes",
                   a3="Behavioral nudges at decision time", a4="Cutting verification cost to at-a-glance",
                   a5="Scheduled manual dose (audit that it happens)", a6="Cognitive forcing: works at subtask level, feels harder",
                   b1='"Please verify the AI" exhortations', b2="Lecture-style training / 20-hour courses", b3="Naive transparency",
                   c1="Adaptive automation (rotating control):", c2="30 years in sims; no operational evaluation",
                   cap="Schematic: effect sizes, boundary conditions, and costs per lever in Chapter 8; 'effective' is not universal — most effects are design-dependent"),
    }[lang]
    rows_a = [t['a1'], t['a2'], t['a3'], t['a4'], t['a5'], t['a6']]
    rows_b = [t['b1'], t['b2'], t['b3']]
    parts = []
    y = 92
    for item in rows_a:
        parts.append(f'<circle cx="36" cy="{y - 4}" r="4" fill="#52b788"/>')
        parts.append(f'<text x="50" y="{y}" fill="#e4e6eb" font-size="11.5" font-family="-apple-system,sans-serif">{item}</text>')
        y += 30
    y2 = 92
    for item in rows_b:
        parts.append(f'<circle cx="420" cy="{y2 - 4}" r="4" fill="#e85a4f"/>')
        parts.append(f'<text x="434" y="{y2}" fill="#e4e6eb" font-size="11.5" font-family="-apple-system,sans-serif">{item}</text>')
        y2 += 30
    return f"""<figure>
<svg viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="30" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  <text x="24" y="64" fill="#52b788" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['h1']}</text>
  <text x="408" y="64" fill="#ff8a80" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['h2']}</text>
  <line x1="396" y1="48" x2="396" y2="200" stroke="#5a6378" stroke-width="1" stroke-dasharray="2,4"/>
  {''.join(parts)}
  <text x="408" y="214" fill="#f0b429" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{t['h3']}</text>
  <circle cx="420" cy="238" r="4" fill="#f0b429"/>
  <text x="434" y="242" fill="#e4e6eb" font-size="11.5" font-family="-apple-system,sans-serif">{t['c1']}</text>
  <text x="434" y="260" fill="#e4e6eb" font-size="11.5" font-family="-apple-system,sans-serif">{t['c2']}</text>
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


def fig_ai_map1983(lang: str) -> str:
    """The four 1983 ironies and their 2026 evidence status."""
    t = {
        "zh": dict(title="1983 年四个反讽的 2026 成绩单",
                   i1="技能不用则退化,监控者由老手变新手", s1="证实:航空对照实测 + 技能衰退元分析", c1="#52b788",
                   i2="人对少事件信源的警觉撑不过约半小时", s2="证实:警戒实验稳健复现四十年", c2="#52b788",
                   i3="最需要人接管时,人恰恰最不在状态", s3="现场档案强支持:AF447 / FAA 事故统计", c3="#5eead4",
                   i4="人无法实时核查一台比自己强的机器", s4="仍是分析性论断;scalable oversight 证据同向", c4="#f0b429",
                   cap="示意:「证实」指方向获独立证据支持,非逐字量化;分级与出处见正文各章与第 9 章"),
        "en": dict(title="The four 1983 ironies: a 2026 report card",
                   i1="Skills decay without use; the monitor turns novice", s1="Confirmed: aviation measurements + decay meta-analysis", c1="#52b788",
                   i2="Vigilance on low-event sources fails after ~half an hour", s2="Confirmed: vigilance studies replicate across 40 years", c2="#52b788",
                   i3="The human is least ready exactly when most needed", s3="Strong field support: AF447 / FAA accident statistics", c3="#5eead4",
                   i4="Humans cannot real-time-check a stronger machine", s4="Still an analytical claim; oversight evidence points the same way", c4="#f0b429",
                   cap="Schematic: 'confirmed' means the direction has independent empirical support, not literal quantification; grades and sources in the chapters and Chapter 9"),
    }[lang]
    rows = [(t['i1'], t['s1'], t['c1']), (t['i2'], t['s2'], t['c2']), (t['i3'], t['s3'], t['c3']), (t['i4'], t['s4'], t['c4'])]
    parts = []
    y = 78
    for irony, status, color in rows:
        parts.append(f'<rect x="24" y="{y - 20}" width="652" height="54" rx="8" fill="{color}" opacity="0.07" stroke="{color}" stroke-opacity="0.35"/>')
        parts.append(f'<text x="40" y="{y}" fill="#e4e6eb" font-size="12" font-weight="700" font-family="-apple-system,sans-serif">{irony}</text>')
        parts.append(f'<text x="40" y="{y + 21}" fill="{color}" font-size="11.5" font-family="-apple-system,sans-serif">{status}</text>')
        y += 66
    return f"""<figure>
<svg viewBox="0 0 700 350" xmlns="http://www.w3.org/2000/svg" role="img">
  <text x="24" y="34" fill="#e4e6eb" font-size="15" font-weight="700" font-family="-apple-system,sans-serif">{t['title']}</text>
  {''.join(parts)}
</svg>
<figcaption>{t['cap']}</figcaption>
</figure>"""


FIGURES = {
    "automation-irony-deep": [
        ("zh", "3. 实验室 40 年", fig_ai_lab, "end"),
        ("en", "3. Forty years in the lab", fig_ai_lab, "end"),
        ("zh", "5. 医疗", fig_ai_tension, "end"),
        ("en", "5. Medicine", fig_ai_tension, "end"),
        ("zh", "6. AI 时代体检", fig_ai_dratsch, "end"),
        ("en", "6. The AI-era physical", fig_ai_dratsch, "end"),
        ("zh", "8. 可工程化清单", fig_ai_levers, "end"),
        ("en", "8. The engineerable list", fig_ai_levers, "end"),
        ("zh", "9. 结论", fig_ai_map1983, "end"),
        ("en", "9. Conclusion", fig_ai_map1983, "end"),
    ],
    "automation-irony-plain": [
        ("zh", "一位医生的检出率", fig_ai_tension, "end"),
        ("en", "One doctor's detection rate", fig_ai_tension, "end"),
        ("zh", "40 年证据最狠的几刀", fig_ai_lab, "end"),
        ("en", "The sharpest cuts", fig_ai_lab, "end"),
        ("zh", "有效的招和它们的价格", fig_ai_levers, "end"),
        ("en", "What works, and what it costs", fig_ai_levers, "end"),
    ],
    "seventy-percent-failure-deep": [
        ("zh", "1. ", fig_sp_life, "end"),
        ("en", "1. ", fig_sp_life, "end"),
        ("zh", "2.2", fig_sp_fattail, "end"),
        ("en", "2.2", fig_sp_fattail, "end"),
        ("zh", "2.4", fig_sp_gauge, "end"),
        ("en", "2.4", fig_sp_gauge, "end"),
        ("zh", "4. ", fig_sp_archive, "end"),
        ("en", "4. ", fig_sp_archive, "end"),
        ("zh", "7.3", fig_sp_transfer, "end"),
        ("en", "7.3", fig_sp_transfer, "end"),
    ],
    "seventy-percent-failure-plain": [
        ("zh", "一个数字的一生", fig_sp_life, "end"),
        ("en", "The life of a number", fig_sp_life, "end"),
        ("zh", "那真实的失败率是多少", fig_sp_gauge, "end"),
        ("en", "So what is the real failure rate", fig_sp_gauge, "end"),
        ("zh", "AI 转型:剧本重演了多少", fig_sp_transfer, "end"),
        ("en", "AI transformation: how much of the script", fig_sp_transfer, "end"),
    ],
    "machine-oracles-deep": [
        ("zh", "1. 读图说明", fig_mo_map, "end"),
        ("en", "1. How to read the map", fig_mo_map, "end"),
        ("zh", "4. Derived", fig_mo_argus, "end"),
        ("en", "4. Derived", fig_mo_argus, "end"),
        ("zh", "7. Specified 弱端", fig_mo_shrink, "end"),
        ("en", "7. The weak end of specified", fig_mo_shrink, "end"),
        ("zh", "8. Human oracle 对照组", fig_mo_curl, "end"),
        ("en", "8. The human-oracle control group", fig_mo_curl, "end"),
        ("zh", "10. 座次", fig_mo_seats, "end"),
        ("en", "10. The seating chart", fig_mo_seats, "end"),
    ],
    "machine-oracles-plain": [
        ("zh", "一个四十年的老问题", fig_mo_seats, "end"),
        ("en", "A forty-year-old problem", fig_mo_seats, "end"),
        ("zh", "AI 一坐上裁判席", fig_mo_shrink, "end"),
        ("en", "The moment AI takes the bench", fig_mo_shrink, "end"),
        ("zh", "同一种 AI 产出", fig_mo_curl, "end"),
        ("en", "One AI output, two judges", fig_mo_curl, "end"),
    ],
    "learning-science-deep": [
        ("zh", "1. 读数说明书", fig_ls_control, "end"),
        ("en", "1. How to read the numbers", fig_ls_control, "end"),
        ("zh", "3. 间隔与交错", fig_ls_lab2class, "end"),
        ("en", "3. Spacing and interleaving", fig_ls_lab2class, "end"),
        ("zh", "4. 刻意练习之战", fig_ls_practice_war, "end"),
        ("en", "4. The deliberate-practice war", fig_ls_practice_war, "end"),
        ("zh", "5. 学习风格", fig_ls_styles_gap, "end"),
        ("en", "5. Learning styles", fig_ls_styles_gap, "end"),
        ("zh", "6. 主动学习 vs 讲授", fig_ls_feel_vs_learn, "end"),
        ("en", "6. Active learning vs. lecture", fig_ls_feel_vs_learn, "end"),
        ("zh", "8. 重排座次", fig_ls_ladder, "end"),
        ("en", "8. The re-seated ranking", fig_ls_ladder, "end"),
    ],
    "learning-science-plain": [
        ("zh", "你听过的学习建议", fig_ls_ladder, "end"),
        ("en", "Most study advice you", fig_ls_ladder, "end"),
        ("zh", "先学三个防骗口诀", fig_ls_control, "end"),
        ("en", "First, three anti-scam questions", fig_ls_control, "end"),
        ("zh", "座次表最上面", fig_ls_lab2class, "end"),
        ("en", "Top of the table", fig_ls_lab2class, "end"),
        ("zh", "座次表中间", fig_ls_feel_vs_learn, "end"),
        ("en", "Middle of the table", fig_ls_feel_vs_learn, "end"),
        ("zh", "座次表下面", fig_ls_practice_war, "end"),
        ("en", "Bottom of the table", fig_ls_practice_war, "end"),
        ("zh", "座次表下面", fig_ls_styles_gap, "end"),
        ("en", "Bottom of the table", fig_ls_styles_gap, "end"),
    ],
    "scalable-oversight-deep": [
        ("zh", "1. 假设的谱系", fig_so_genealogy, "end"),
        ("en", "1. The genealogy", fig_so_genealogy, "end"),
        ("zh", "3. 实证正面", fig_so_debate, "end"),
        ("en", "3. The positive empirics", fig_so_debate, "end"),
        ("zh", "5. 任务族分解", fig_so_spectrum, "end"),
        ("en", "5. Task-family decomposition", fig_so_spectrum, "end"),
        ("zh", "6. 实验室自己怎么做", fig_so_retreat, "end"),
        ("en", "6. What the labs themselves do", fig_so_retreat, "end"),
    ],
    "scalable-oversight-plain": [
        ("zh", "一句话撑起一个行业", fig_so_genealogy, "end"),
        ("en", "One sentence holding up", fig_so_genealogy, "end"),
        ("zh", "检查什么时候突然变难", fig_so_spectrum, "end"),
        ("en", "When checking suddenly gets hard", fig_so_spectrum, "end"),
        ("zh", "那\"AI 辩论\"呢", fig_so_debate, "end"),
        ("en", 'What about "AI debate"', fig_so_debate, "end"),
        ("zh", "提出这句话的人", fig_so_retreat, "end"),
        ("en", "What the people who proposed", fig_so_retreat, "end"),
    ],
    "ai-native-plain": [
        ("zh", "成本没有消失", fig_cost_transfer),
        ("en", "The cost didn", fig_cost_transfer),
        ("zh", "如果你维护的是", fig_perrow),
        ("en", "If you run systems", fig_perrow),
    ],
    "ai-native-deep": [
        ("zh", "1.4 枢轴的解释力", fig_cost_transfer),
        ("en", "1.4 What the pivot explains", fig_cost_transfer),
        ("zh", "4.1 为什么初创玩法不能照搬", fig_perrow),
        ("en", "4.1 Why the startup playbook", fig_perrow),
    ],
    "junior-engineers-plain": [
        ("zh", "先看四个仪表盘", fig_four_gauges),
        ("en", "Four gauges, four answers", fig_four_gauges),
        ("zh", "可是,AI 明明最帮新手", fig_rct_paradox),
        ("en", "But AI helps beginners most", fig_rct_paradox),
        ("zh", "那到底是不是 AI 干的?", fig_age_scissors),
        ("en", "So did AI actually do this?", fig_age_scissors),
    ],
    "junior-engineers-deep": [
        ("zh", "1. 先对表:同一个市场,四个仪表盘", fig_four_gauges),
        ("en", "1. Calibrating the gauges", fig_four_gauges),
        ("zh", "3. 计量对战:两类数据,两个结论", fig_age_scissors),
        ("en", "3. The econometric battle", fig_age_scissors),
        ("zh", "5. 悖论的解法:个体生产率不是雇佣决策", fig_rct_paradox),
        ("en", "5. Resolving the paradox", fig_rct_paradox),
    ],
    "ai-code-review-plain": [
        ("zh", "检查代码为什么成了瓶颈", fig_review_scissors),
        ("en", "Why checking code became the bottleneck", fig_review_scissors),
        ("zh", "卖家的成绩单", fig_bench_spread),
        ("en", "Why you can", fig_bench_spread),
        ("zh", "大厂自己用得怎么样", fig_offline_funnel),
        ("en", "How is it going for the companies", fig_offline_funnel),
        ("zh", "套娃到底套在哪", fig_review_turtles),
        ("en", "Where exactly the nesting dolls", fig_review_turtles),
        ("zh", "那它什么时候真的管用", fig_cure_conditions),
        ("en", "So when does it actually work", fig_cure_conditions),
    ],
    "ai-code-review-deep": [
        ("zh", "1. 需求侧", fig_review_scissors),
        ("en", "1. The demand side", fig_review_scissors),
        ("zh", "2. 供给侧的证明材料", fig_bench_spread),
        ("en", "2. The supply side", fig_bench_spread),
        ("zh", "3. 大厂一手数据", fig_offline_funnel),
        ("en", "3. First-party data from big tech", fig_offline_funnel),
        ("zh", "5. 根本问题", fig_review_turtles),
        ("en", "5. The root question", fig_review_turtles),
        ("zh", "7. 裁决", fig_cure_conditions),
        ("en", "7. The verdict", fig_cure_conditions),
    ],
}


def inject_figures(body: str, slug: str, lang: str) -> str:
    for entry in FIGURES.get(slug, []):
        fig_lang, prefix, fn = entry[0], entry[1], entry[2]
        place = entry[3] if len(entry) > 3 else "para1"
        if fig_lang != lang:
            continue
        pat = re.compile(r"(<h[23]>" + re.escape(prefix)[:60] + r"[^<]*</h[23]>)")
        m = pat.search(body)
        if not m:
            print(f"  WARN figure anchor not found: {slug} {lang} '{prefix}'")
            continue
        after = body[m.end():]
        if place == "end":
            # insert at the END of the section: before the next h2/h3, or at body end
            nxt = re.search(r"<h[23]>", after)
            pos = m.end() + (nxt.start() if nxt else len(after))
        else:
            # insert after the first paragraph following the heading
            p_end = after.find("</p>")
            pos = m.end() + (p_end + 4 if p_end != -1 else 0)
        body = body[:pos] + "\n" + fn(lang) + "\n" + body[pos:]
    return body


# ---------------------------------------------------------------- page templates

SHARED_SCRIPTS = """<script src="https://hub.cissychen.com/comments.js" defer></script>
<script src="https://hub.cissychen.com/search.js" defer></script>
<script src="https://hub.cissychen.com/index-button.js" defer></script>
<script src="https://hub.cissychen.com/i18n-tts.js" defer></script>"""

# Section accent colors cycled by h2 order (matches the hub's multi-color card language).
H2_COLORS = ["#4cc9f0", "#7b61ff", "#ff6ec4", "#5eead4", "#f0b429", "#52b788", "#e8794b", "#a29bfe"]

ARTICLE_CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei",-apple-system,"Noto Serif SC",sans-serif;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0a0e1a 100%);color:#dde1ea;line-height:1.85;min-height:100vh}
.container{max-width:760px;margin:0 auto;padding:56px 24px 90px}
.kicker{font-size:0.78rem;color:#4cc9f0;letter-spacing:2px;text-transform:uppercase;font-family:"SF Mono",Menlo,monospace;margin-bottom:10px}
h1{font-size:1.9rem;font-weight:800;line-height:1.4;background:linear-gradient(135deg,#4cc9f0 0%,#7b61ff 55%,#ff6ec4 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px}
h2{font-size:1.32rem;font-weight:700;color:#fff;margin:46px 0 14px;padding:10px 0 8px;border-top:1px solid rgba(255,255,255,0.08)}
h2::before{content:"";display:inline-block;width:14px;height:14px;border-radius:4px;margin-right:10px;background:var(--h2,#4cc9f0);transform:translateY(1px)}
h3{font-size:1.08rem;font-weight:700;color:#c9d4ff;margin:30px 0 10px}
p{margin:0 0 16px}
ul,ol{margin:0 0 16px 1.4em}
li{margin-bottom:8px}
strong{color:#fff}
em{color:#8be0e8;font-style:normal}
code{font-family:"SF Mono",Menlo,monospace;font-size:0.85em;background:rgba(123,97,255,0.15);padding:1px 6px;border-radius:4px;color:#c9d4ff}
a{color:#4cc9f0;text-decoration:none;border-bottom:1px dotted rgba(76,201,240,0.4)}
a:hover{color:#7b61ff}
blockquote{border-left:3px solid #4cc9f0;background:rgba(76,201,240,0.06);padding:14px 18px;margin:0 0 20px;border-radius:0 8px 8px 0;font-size:0.92rem;color:#a8b4d0}
blockquote p{margin-bottom:8px}
blockquote p:last-child{margin-bottom:0}
hr{border:none;border-top:1px solid rgba(255,255,255,0.12);margin:36px 0}
figure{margin:26px 0;padding:18px 16px 12px;background:rgba(255,255,255,0.025);border:1px solid rgba(76,201,240,0.18);border-radius:12px}
figure svg{width:100%;height:auto;display:block}
figcaption{margin-top:10px;font-size:0.8rem;color:#7c8593;text-align:center;font-family:"SF Mono",Menlo,monospace;line-height:1.55}
.tl{background:linear-gradient(135deg,rgba(76,201,240,0.10),rgba(123,97,255,0.10));border:1px solid rgba(76,201,240,0.35);border-radius:12px;padding:18px 20px;margin:24px 0 8px}
.tl .tl-label{font-family:"SF Mono",Menlo,monospace;font-size:0.72rem;letter-spacing:2px;color:#4cc9f0;margin-bottom:8px}
.tl .tl-text{font-size:0.98rem;color:#e8ecf5;line-height:1.75}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 30px}
.chip{font-family:"SF Mono",Menlo,monospace;font-size:0.74rem;font-weight:700;padding:5px 13px;border-radius:14px;border:1px solid;white-space:nowrap}
.chip.c1{color:#4cc9f0;border-color:rgba(76,201,240,0.5);background:rgba(76,201,240,0.08)}
.chip.c2{color:#ff6ec4;border-color:rgba(255,110,196,0.5);background:rgba(255,110,196,0.08)}
.chip.c3{color:#5eead4;border-color:rgba(94,234,212,0.5);background:rgba(94,234,212,0.08)}
.chip.c4{color:#f0b429;border-color:rgba(240,180,41,0.5);background:rgba(240,180,41,0.08)}
.topbar{position:fixed;top:14px;right:14px;display:flex;gap:8px;z-index:100;font-family:"SF Mono",Menlo,monospace;font-size:0.75rem}
.topbar a{background:rgba(255,255,255,0.06);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:6px 13px;color:#a0a8c0;border-bottom:none}
.topbar a.active{background:#7b61ff;color:#fff;font-weight:700}
.topbar a:hover:not(.active){background:rgba(255,255,255,0.1);color:#fff}
.version-note{display:inline-block;font-family:"SF Mono",Menlo,monospace;font-size:0.76rem;color:#4cc9f0;border:1px solid rgba(76,201,240,0.35);border-radius:14px;padding:3px 12px;margin:6px 0 6px}
.version-note a{border-bottom:none;font-weight:700}
.backlink{font-family:"SF Mono",Menlo,monospace;font-size:0.8rem;margin-bottom:18px;display:inline-block;border-bottom:none;color:#7b61ff}
footer{margin-top:56px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.1);font-size:0.75rem;color:#5a6378;font-family:"SF Mono",Menlo,monospace}
footer a{border-bottom:none}
.mmd-lang-toggle{display:none!important}
@media(max-width:700px){.container{padding:44px 16px 70px}h1{font-size:1.5rem}.topbar{top:8px;right:8px}}"""


def h2_color_css(body: str) -> str:
    """Give each h2 its own accent color via nth-of-type rules."""
    n = body.count("<h2>")
    rules = []
    for i in range(n):
        c = H2_COLORS[i % len(H2_COLORS)]
        rules.append(f"h2:nth-of-type({i + 1}){{--h2:{c}}}")
    return "\n".join(rules)


ARTICLE_TMPL = """<!DOCTYPE html>
<html lang="{html_lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — BigCat Deep Research</title>
<meta name="description" content="{desc}">
<style>
{css}
{h2_css}
</style>
</head><body>
<div class="topbar">
  {lang_toggle}
</div>
<div class="container">
<a class="backlink" href="{index_href}">← Deep Research</a>
<div class="kicker">{kicker}</div>
<h1>{title}</h1>
<div class="version-note">{version_note}</div>
<div class="tl"><div class="tl-label">TL;DR</div><div class="tl-text">{tldr}</div></div>
<div class="chips">{chips}</div>
{body}
<footer>BigCat Deep Research · {date} · <a href="https://cissy0802.github.io/">Learning Hub</a></footer>
</div>
{scripts}
</body></html>
"""

# slug, lang, version(plain|deep), title, desc, date
ARTICLES = [
    ("automation-irony-deep", "zh", "deep",
     "自动化的反讽:AI 越好,人握的终审越会退化吗?(深入版)",
     "1983 年的预言对上 40 年证据:实验室的 complacency/automation bias、航空与医疗两份现场档案、2024-2026 的 AI 新证据与干预实测——「人握终审」是判词还是可工程化约束;32 组承重论断 × 3 票对抗验证 + 反证搜索与方法学审计席。",
     "2026-07"),
    ("automation-irony-deep", "en", "deep",
     "The Ironies of Automation: The Better the AI, the Faster the Human Veto Decays? (Deep Dive)",
     "The 1983 prophecy against forty years of evidence: lab complacency and automation bias, the aviation and medicine field archives, the newest AI-era evidence and measured interventions — is 'the human holds the veto' a death sentence or an engineerable constraint; 32 load-bearing claim groups × 3 adversarial votes plus contradiction-search and methods-audit seats.",
     "2026-07"),
    ("automation-irony-plain", "zh", "plain",
     "AI 越好用,人越不中用?一个 42 年前就被预言的问题(易读版)",
     "AI 在场时人机更强,撤走后人可能比从前更差;从不出错的自动化最危险;上课防不住。易读版:主线结论 + 席位设计四问。",
     "2026-07"),
    ("automation-irony-plain", "en", "plain",
     "The Better the AI, the Worse the Human? A Question Predicted 42 Years Ago (Plain-Language Edition)",
     "Stronger with AI present, possibly weaker once it's gone; never-failing automation is the most dangerous kind; courses don't protect. Plain edition: the main findings plus four seat-design questions.",
     "2026-07"),
    ("agent-readme-deep", "zh", "deep",
     "给 Agent 看的 README:上下文文件是基建还是货物崇拜?(深入版)",
     "AGENTS.md/CLAUDE.md 的标准之争、厂商共识与第一批对照实证的正面对撞:三项研究互相矛盾、方法学审计否决两组流传数字、唯一带统计检验的收益是效率;含企业落地 playbook;三轮验证(105 票转述保真 + 反证搜索与方法学审计席)。",
     "2026-07"),
    ("agent-readme-deep", "en", "deep",
     "The README for Agents: Are Context Files Infrastructure or Cargo Cult? (Deep Dive)",
     "The AGENTS.md standards war, the vendor consensus, and the first controlled studies colliding head-on: three mutually contradicting studies, two widely quoted numbers struck down by methods audit, efficiency as the only statistically tested benefit; with an enterprise rollout playbook; three verification rounds (105 fidelity votes + contradiction-search and methods-audit seats).",
     "2026-07"),
    ("agent-readme-plain", "zh", "plain",
     "都说要给代码库写 AGENTS.md,写了真的有用吗?(易读版)",
     "对照研究互相打架,唯一带统计检验的收益是省时省 token;「短了更听话」没有证据;llms.txt 97% 零请求。易读版:主线结论 + 行动清单。",
     "2026-07"),
    ("agent-readme-plain", "en", "plain",
     "Everyone Says Your Repo Needs an AGENTS.md. Does It? (Plain-Language Edition)",
     "The controlled studies fight each other; the only statistically tested win is saved time and tokens; 'shorter = more obedient' has no evidence; llms.txt gets zero requests 97% of the time. Plain edition: the main findings plus an action list.",
     "2026-07"),
    ("seventy-percent-failure-deep", "zh", "deep",
     "「70% 转型失败」考古:上一轮转型的尸检报告,能预测 AI-native 吗?(深入版)",
     "追溯「70%」的引用链原文、复算失败率测量、盘点 Agile/DevOps 档案并评估其对 AI-native 转型的预测力;30 组承重论断 × 3 票对抗验证。",
     "2026-07"),
    ("seventy-percent-failure-deep", "en", "deep",
     "The '70% of Transformations Fail' Autopsy: Can the Last Wave's Post-Mortems Predict AI-Native? (Deep Dive)",
     "Tracing the '70%' citation chain to its sources, re-reading the measured failure-rate record, and auditing the Agile/DevOps archives for what they predict about AI-native transformation; 30 load-bearing claim groups adversarially verified.",
     "2026-07"),
    ("seventy-percent-failure-plain", "zh", "plain",
     "「70% 的转型都会失败」?这个数字是编的(易读版)",
     "先吓你再卖你解药的「70% 会失败」,出生证上写着「非科学」。易读版:主线论证 + 直白语言。",
     "2026-07"),
    ("seventy-percent-failure-plain", "en", "plain",
     "'70% of Transformations Fail'? That Number Was Made Up (Plain-Language Edition)",
     "The scare-then-sell '70% fail' was born with 'unscientific' on its birth certificate. The accessible edition.",
     "2026-07"),
    ("machine-oracles-deep", "zh", "deep",
     "机器裁判全景:LLM 能把软件验证的 oracle 做大多少?(深入版)",
     "按 Barr 分类法逐格盘点软件验证的裁判家族,核查每格的「LLM 增益」——脊柱主张:LLM 坐生成/提议席则增益有硬数字,坐裁判席则独立复测系统性缩水。29 组承重论断 × 3 票对抗验证。",
     "2026-07"),
    ("machine-oracles-deep", "en", "deep",
     "The Machine-Judge Atlas: How Much Can LLMs Scale Software's Oracles? (Deep Dive)",
     "A cell-by-cell audit of software's oracle families along the Barr taxonomy, checking each cell's 'LLM gain' — the spine: gains are hard-numbered in the generator/proposer seat and shrink under re-testing in the judge's seat. 29 load-bearing claims adversarially verified.",
     "2026-07"),
    ("machine-oracles-plain", "zh", "plain",
     "AI 找 bug 靠不靠谱?先看裁判是谁(易读版)",
     "AI 能写测试、报漏洞,但它的成绩取决于坐哪把椅子——干活的、起草的、还是当裁判的。易读版:主线论证 + 直白语言。",
     "2026-07"),
    ("machine-oracles-plain", "en", "plain",
     "Can AI Find Real Bugs? First Ask Who the Judge Is (Plain-Language Edition)",
     "AI can write tests and report bugs, but its score depends on which seat it takes — worker, drafter, or judge. The accessible edition.",
     "2026-07"),
    ("learning-science-deep", "zh", "deep",
     "学习科学的证据等级:哪些学习方法真的有效?(深入版)",
     "检索、间隔、交错、刻意练习、学习风格、主动学习——五场学术对战逐一对账,把常见学习方法按证据强度重新排座次;含一处几乎没人引用的正式勘误。",
     "2026-07"),
    ("learning-science-deep", "en", "deep",
     "The Evidence Hierarchy of Learning Science: What Actually Works? (Deep Dive)",
     "Retrieval, spacing, interleaving, deliberate practice, learning styles, active learning — five academic battles audited line by line, the common study methods re-seated by evidence strength; includes a rarely cited official corrigendum.",
     "2026-07"),
    ("learning-science-plain", "zh", "plain",
     "学习方法排座次:哪些真有效,哪些是神话?(易读版)",
     "一万小时、学习风格、划重点——流行的学习建议大多没有你以为的那种证据。易读版:主线论证 + 直白语言。",
     "2026-07"),
    ("learning-science-plain", "en", "plain",
     "Ranking Study Methods by Evidence: What Works and What's Myth (Plain-Language Edition)",
     "Ten thousand hours, learning styles, highlighting — most popular study advice lacks the evidence you think it has. The accessible edition.",
     "2026-07"),
    ("scalable-oversight-deep", "zh", "deep",
     "验证真的比生成容易吗?——Scalable oversight 的地基体检(深入版)",
     "整个「AI 看住 AI」的路线站在「验证比生成容易」上——创始假设如何被公理化,理论裂缝、条件化实证与实验室的退守。",
     "2026-07"),
    ("scalable-oversight-deep", "en", "deep",
     "Is Verification Really Easier Than Generation? A Foundation Inspection of Scalable Oversight",
     "The 'AI watching AI' program stands on one sentence. How a qualified assumption became an axiom — cracks, conditional empirics, and the labs' retreat.",
     "2026-07"),
    ("scalable-oversight-plain", "zh", "plain",
     "AI 看住 AI 的大前提:一句没人验过的话(易读版)",
     "「检查比做容易」撑起了整个 AI 监督行业——它什么时候真的成立,什么时候翻车?易读版。",
     "2026-07"),
    ("scalable-oversight-plain", "en", "plain",
     "The Premise Behind \"AI Watching AI\": One Sentence Nobody Verified",
     "'Checking is easier than doing' holds up the whole AI-oversight industry — when is it actually true? The plain-language edition.",
     "2026-07"),
    ("ai-native-plain", "zh", "plain",
     "当写代码变得便宜:软件组织怎么转向 AI-native(易读版)",
     "为什么每个人都觉得 AI 让自己更快,组织却没变快?易读版:主线论证 + 直白语言。",
     "2026-07"),
    ("ai-native-plain", "en", "plain",
     "When Writing Code Becomes Cheap: A Plain-Language Guide to the AI-Native Transformation",
     "Why everyone feels faster with AI while organizations don't. The accessible edition.",
     "2026-07"),
    ("ai-native-deep", "zh", "deep",
     "当代码变得便宜:传统软件组织向 AI-native 转型的理论与证据(深入版)",
     "四大理论光谱 + 高可靠 legacy 专章;86 个来源、166 票对抗验证的完整论证。",
     "2026-07"),
    ("ai-native-deep", "en", "deep",
     "When Code Becomes Cheap: Theory and Evidence for the AI-Native Transformation of Software Organizations",
     "Four theoretical spectra plus a high-reliability legacy chapter; fully adversarially verified.",
     "2026-07"),
    ("junior-engineers-plain", "zh", "plain",
     "「初级工程师正在消失」是真的吗?(易读版)",
     "总就业创新高,22-25 岁一档却跌了近 20%——职业没消失,入口在收窄。易读版:主线论证 + 直白语言。",
     "2026-07"),
    ("junior-engineers-plain", "en", "plain",
     "Are Junior Engineers Really Disappearing? (Plain-Language Edition)",
     "Employment at a record high while the youngest bracket falls 20% — the profession isn't vanishing, the entrance is narrowing. The accessible edition.",
     "2026-07"),
    ("junior-engineers-deep", "zh", "deep",
     "「初级工程师正在消失」是真的吗:入门岗位的证据体检(深入版)",
     "四个数据口径对表、Canaries 对战空值派、RCT 悖论的组织经济学解法;15 条承重论断 × 3 票对抗验证。",
     "2026-07"),
    ("junior-engineers-deep", "en", "deep",
     "Are Junior Engineers Really Disappearing? An Evidence Audit of the Entry-Level Software Job Market",
     "Four gauges calibrated, Canaries versus the null camp, and the organizational economics that resolves the RCT paradox; 15 load-bearing claims adversarially verified.",
     "2026-07"),
    ("ai-code-review-plain", "zh", "plain",
     "AI 审代码,谁来审 AI?(易读版)",
     "查代码的人跟不上 AI 写代码的速度,行业的药方是再买一个 AI 来查——它什么时候是解药,什么时候是套娃。易读版:主线论证 + 直白语言。",
     "2026-07"),
    ("ai-code-review-plain", "en", "plain",
     "AI Reviews the Code — Who Reviews the AI? (Plain-Language Edition)",
     "Humans can't keep up with AI-written code, so the industry bought another AI to do the checking — when that's medicine, and when it's nesting dolls. The accessible edition.",
     "2026-07"),
    ("ai-code-review-deep", "zh", "deep",
     "AI code review:验证瓶颈的解药,还是套娃?(深入版)",
     "基准混战解剖、大厂生产漏斗、'AI 验证 AI'的四个脚注与 1983 年的人因剧本;15 条承重论断 × 3 票对抗验证。",
     "2026-07"),
    ("ai-code-review-deep", "en", "deep",
     "AI Code Review: Cure for the Verification Bottleneck, or Turtles All the Way Down? (Deep Dive)",
     "An anatomy of the benchmark wars, big tech's production funnels, four footnotes to 'AI verifying AI', and the human-factors script written in 1983; 15 load-bearing claims adversarially verified.",
     "2026-07"),
]

KICKERS = {
    ("zh", "plain"): "深度研究 · 易读版",
    ("zh", "deep"):  "深度研究 · 深入版",
    ("en", "plain"): "Deep Research · Plain-language",
    ("en", "deep"):  "Deep Research · Deep dive",
}

TLDRS = {
    ("automation-irony-deep", "zh"):
        "「自动化越好,人握终审越会退化」在 1983 年是过程控制语境的分析性预言,原文一半篇幅其实是工程处方。40 年后的成绩单:技能退化(剂量依赖、认知先于运动)与警觉上限被证实;automation bias 多源证实且 RCT 因果确立——掺错的 LLM 建议让上过 20 小时 AI 课的医生准确率掉 14 个百分点,资深放射科医生也从 82.3% 掉到 45.5%。2025 年内镜研究首次给出「撤走 AI 后人比从前差」的真实世界信号(ADR 28.4%→22.4%,观察性、待确认),与在场增益(RCT meta RR 1.24)构成部署评估的两本账。40 年没长出「反讽被证伪」派,长出的是缓解文献:亲历失效、结果问责、决策 nudge、可核验性设计有实测效果,叮嘱与通识培训无效;警觉生理、未知故障不可预演、底率数学是三个不可工程化的硬底。十一个可检验主张收尾。",
    ("automation-irony-deep", "en"):
        "'The better the automation, the faster the human veto decays' was an analytical prophecy in a 1983 process-control paper — half of which was actually engineering prescriptions. The forty-year report card: skill decay (dose-dependent, cognitive-first) and the vigilance ceiling are confirmed; automation bias is multi-source with RCT causality — error-laced LLM advice cost physicians with 20 hours of AI training 14 points of diagnostic accuracy, and even very experienced radiologists fell from 82.3% to 45.5%. The 2025 endoscopy study delivered the first real-world signal of 'worse after AI is removed' (ADR 28.4%→22.4%, observational, unconfirmed), pairing with the in-use gain (RCT meta RR 1.24) as the two ledgers of deployment evaluation. Forty years grew no falsification school, only a mitigation literature: experienced failure, outcome accountability, decision-time nudges, and verifiability design have measured effects; exhortation and generic training don't. Vigilance physiology, unrehearsable unknown failures, and base-rate arithmetic are the three unengineerable floors. Eleven testable claims close the essay.",
    ("automation-irony-plain", "zh"):
        "AI 在场时人机组合更强,撤走后人可能比从前更差——评估 AI 部署要记两本账。从不出错的自动化最危险(故障检出 33% vs 82%);AI 说错时专家也跟着错,20 小时 AI 课防不住(-14 个百分点);技能停用就生锈,且脑子锈得比手快。有效的招:亲历失效、结果问责、决策时提醒、把核对做便宜;没用的招:口头叮嘱和说教课。三条绕不开的底线:盯梢撑不过半小时、未知故障没法预演、AI 越好人的检出越差。",
    ("automation-irony-plain", "en"):
        "With AI present the combo is stronger; once it's removed the human may be worse than before — keep two ledgers when evaluating AI. Never-failing automation is the most dangerous kind (33% vs 82% failure detection); experts follow wrong AI too, and a 20-hour AI course didn't protect (−14 points); unused skills rust, brain before hands. What works: experienced failure, outcome accountability, decision-time nudges, cheap verification. What doesn't: exhortations and lectures. Three unremovable floors: vigilance dies within half an hour, unknown failures can't be rehearsed, and the better the AI the worse the human's detection.",
    ("seventy-percent-failure-deep", "zh"):
        "「70% 的转型会失败」有精确的出生记录:1993 年以「非科学估计」出生、1995 年被作者收回、2000 年被改写成无出处的「残酷事实」、2009 年被麦肯锡发明出「Kotter 1995 研究」这个不存在的出处;2011 年学术验尸确认无实证基础,数字照样活进 AI 时代。真实基率的诚实答案是「未定」:已发表估计横跨 7-90%,失败率是及格线的函数,实测分布是肥尾而非多数失败。Agile/DevOps 档案显示组织机制正在 AI 采纳中原样重演(64% 的 CEO 先投资后理解、仅 21% 重设计工作流、Duolingo 跑完强制→撤销全周期),但影子式自下而上采纳与每 7 个月翻倍的工具能力,是上一轮档案里没有的变量。十一个可检验主张收尾。",
    ("seventy-percent-failure-deep", "en"):
        "'70% of transformations fail' has a precise birth record: born in 1993 as an 'unscientific estimate', retracted by its authors in 1995, rewritten in 2000 as an unsourced 'brutal fact', and gifted a fabricated pedigree in 2009 when McKinsey cited 'research Kotter published in 1995' that does not exist; a 2011 academic autopsy found no valid empirical basis, and the number lived on into the AI era anyway. The honest measured answer is 'undetermined': published estimates span 7-90%, the failure rate is a function of where you set the pass bar, and the measured distribution is fat-tailed rather than majority-failure. The Agile/DevOps archives show the organizational machinery replaying in AI adoption (64% of CEOs invest before understanding value, only 21% redesigned workflows, Duolingo ran the full mandate-to-retreat cycle), while shadow bottom-up adoption and capability doubling every ~7 months are variables the last archive never saw. Eleven testable claims close the essay.",
    ("seventy-percent-failure-plain", "zh"):
        "「70% 的转型会失败」没人测出来过:它以「非科学估计」出生,被作者收回、被升级成「事实」、被安上假出处,2011 年被学术验尸后照样流通到 AI 时代。真实失败率取决于及格线怎么画——同一批数据既能是「88% 失败」也能是「87% 至少干成一半」;实测的危险是少数惨败的肥尾,不是多数失败。上一轮敏捷/DevOps 的教训:买实践、别买仪式;这一轮的新变量:员工在藏着用 AI,工具自己在变强。",
    ("seventy-percent-failure-plain", "en"):
        "Nobody ever measured '70% of transformations fail': it was born an 'unscientific estimate', retracted by its authors, upgraded to a 'fact', given a fake pedigree, academically debunked in 2011 — and kept circulating right into the AI era. The real failure rate depends on where you draw the pass line: the same data can read '88% fail' or '87% got at least halfway'; the measured danger is a fat tail of disasters, not majority failure. The last wave's lesson: buy practices, not rituals. This wave's new variables: employees using AI in secret, and tools that keep getting stronger.",
    ("machine-oracles-deep", "zh"):
        "把软件验证的裁判按 Barr 四分类逐格摊开:决定「LLM 增益」真伪的不是格子,是 LLM 坐的椅子。生成器席(判决全在崩溃/差分/mutation/人审)增益有生产级硬数字——OSS-Fuzz 26 漏洞、ShQveL 55 bug、Dr.Fix 86% 采纳;提议者席(起草规约/规则,过独立筛)增益真实但筛余负担不消失;裁判席声称的增益在独立复测中系统性缩水——TOGA 0.38%、PrimeVul 3.09%、Argus 消融 20/20 误报。三个软化条款:投票增益衰减非归零、人类裁判洪水受激励调制可逆转、机器闸必要非充分。十一个可检验主张收尾。",
    ("machine-oracles-deep", "en"):
        "Software's judges, spread out along Barr's four categories: what decides whether an 'LLM gain' is real is not the cell but the seat the LLM takes. The generator seat (adjudication fully with crash/differencing/mutation/human review) has production-grade numbers — OSS-Fuzz's 26 vulnerabilities, ShQveL's 55 bugs, Dr.Fix's 86% acceptance; the proposer seat (drafting specs/rules, filtered independently) yields real gains with residual burden intact; the judge seat's claimed gains shrink under re-testing — TOGA 0.38%, PrimeVul 3.09%, Argus's 20/20 false-positive ablation. Three softening clauses: voting gains decay rather than vanish, the human-judge flood is incentive-modulated and reversible, machine gates are necessary but not sufficient. Eleven testable claims close the essay.",
    ("machine-oracles-plain", "zh"):
        "AI 找 bug 的成绩单,取决于它在验证流水线里坐哪把椅子:当干活的(生成测试输入)、起草的(提议规则交独立机制筛)、还是当裁判的(直接判对错)。前两把椅子有真金白银——26 个漏洞、二十年 CVE、Meta 73% 采纳;第三把椅子几乎每次独立复查都缩水——0.38%、3%、20/20 全是误报。评估任何「AI 找 bug」方案,第一个问题永远是:裁判是谁?",
    ("machine-oracles-plain", "en"):
        "AI's bug-finding report card depends on which seat it takes in the verification pipeline: the worker (generating test inputs), the drafter (proposing rules filtered by an independent mechanism), or the judge (ruling directly). The first two seats pay real money — 26 vulnerabilities, a twenty-year CVE, Meta's 73% acceptance; the third seat shrinks under nearly every independent re-check — 0.38%, 3%, 20/20 false alarms. Evaluating any 'AI finds bugs' product, the first question is always: who is the judge?",
    ("learning-science-deep", "zh"):
        "把常见学习方法按证据强度重排座次:检索练习与间隔是证据最厚的两项(课堂成立、出版偏倚五法检验干净);交错强但边界窄(词汇反向);主动学习方向稳、数字虚(0.47 SD 站在 88% 准实验上);刻意练习勘误后仅解释 14% 方差,预注册复现中顶尖组没练得更多;学习风格匹配在合格检验下反复失败,却有约九成教育者相信。效应量必须连着对照组与场景读。十二个可检验主张收尾。",
    ("learning-science-deep", "en"):
        "The common study methods, re-seated by evidence strength: retrieval practice and spacing carry the thickest dossiers (classroom-valid, five bias checks clean); interleaving is strong within narrow borders (vocabulary reverses); active learning is directionally solid with soft numbers (0.47 SD atop 88% quasi-experiments); deliberate practice explains just 14% of variance post-corrigendum, and in preregistered replication the best violinists hadn't practiced more; learning-styles matching keeps failing qualified tests while ~9 in 10 educators believe it. Every effect size must be read with its control group and setting. Twelve testable claims close the essay.",
    ("learning-science-plain", "zh"):
        "考自己 + 隔开学是证据最硬的两个方法;混着练只在内容易混时有效;一万小时是畅销书发明——练习量只解释约 14% 的成就差异,重做原研究时顶尖组根本没练得更多;学习风格匹配教学检验了几十年都不过关,九成教师却相信。看任何宣传数字先问三件事:跟谁比、在哪测、谁在卖。",
    ("learning-science-plain", "en"):
        "Self-testing + spacing are the two best-evidenced methods; mixing practice only helps when material is confusable; the 10,000-hour rule is a bestseller's invention — practice explains ~14% of achievement differences, and in the redo of the original study the top group hadn't practiced more; learning-styles matching has failed tests for decades while nine in ten teachers believe it. Before trusting any advertised number, ask: compared to what, measured where, and who's selling.",
    ("scalable-oversight-deep", "zh"):
        "「验证比生成容易」在 2018 年是带限定语的编号假设,四年后被当公理引用。理论裂缝(obfuscated arguments 六年未解)、条件化的实证(debate 正结果几乎全靠信息不对称)、与实验室退守 CoT 监控的生产行为共同表明:这块地基按任务族分层——有独立 oracle 处坚实,对抗与开放论证处至今无人证明其承重。九个可检验主张收尾。",
    ("scalable-oversight-deep", "en"):
        "In 2018, 'verification is easier than generation' was a qualified, numbered assumption; within four years it was cited as an axiom. Theoretical cracks (obfuscated arguments unsolved for six years), conditional empirics (debate's positives almost all require information asymmetry), and the labs' own retreat to CoT monitoring point the same way: the foundation stratifies by task family — solid where an independent oracle exists, unproven under adversarial pressure. Nine testable claims close the essay.",
    ("scalable-oversight-plain", "zh"):
        "整个「AI 看住 AI」的行业押在「检查比做容易」这句话上。它在有独立裁判的任务(数学证明、有测试的代码)上真金白银地成立;在有对手、没标准答案、AI 自查的场景里,实测证据大多反对。实验室自己已退到最弱形式——盯思维链,还自认脆弱。",
    ("scalable-oversight-plain", "en"):
        "The whole 'AI watching AI' industry is betting on 'checking is easier than doing.' It genuinely holds where an incorruptible judge exists (math proofs, tested code); with adversaries, no answer key, or AI checking itself, the measurements mostly say no. The labs themselves have retreated to the weakest form — watching the chain of thought — and call it fragile.",
    ("ai-native-plain", "zh"):
        "AI 把「写代码」变便宜,把瓶颈推到「确认代码是对的」。个人变快 ≠ 组织变快;评估 AI 靠交付数据、不靠体感;维护高可靠老系统的组织,从迁移类任务切入、护栏先于规模。",
    ("ai-native-plain", "en"):
        "AI makes writing code cheap and pushes the bottleneck to confirming the code is right. Faster individuals ≠ a faster organization; judge AI by delivery data, not gut feel; legacy organizations should enter through migrations, guardrails before scale.",
    ("ai-native-deep", "zh"):
        "交易成本没有消失,而是从生产/协调转移到整合/验证——这一枢轴同时解释了 METR 的减速、DORA 的稳定性惩罚与人的角色重构,并推出高可靠 legacy 组织「迁移切入 → 护栏先于规模 → 验证基础设施资本化」的转型序列。全文以六个可检验主张收尾。",
    ("ai-native-deep", "en"):
        "Transaction costs don't disappear — they migrate from production/coordination to integration/verification. This single pivot explains METR's slowdown, DORA's stability penalty, and the restructuring of human roles, and yields the sequence for high-reliability legacy organizations: enter through migrations → guardrails before scale → capitalize verification infrastructure. The essay closes with six testable claims.",
    ("junior-engineers-plain", "zh"):
        "美国软件开发者总就业创历史新高,但 22-25 岁一档从 2022 年底跌了近 20%:职业没消失,给新人开的门在收窄。实验反复证明 AI 最帮新手——这与新手岗位收缩不矛盾:帮新手最多的技术,恰恰让「不雇新手」变得可行。宏观因素解释了塌方,解释不了塌方只砸最年轻的人。",
    ("junior-engineers-plain", "en"):
        "Total US software developer employment is at a record high, yet the 22-25 bracket is down nearly 20% since late 2022: the profession isn't vanishing — the door for newcomers is narrowing. Experiments keep showing AI helps novices most, and that's no contradiction: the technology that helps beginners most is what makes not-hiring-them feasible. Macro forces explain the collapse, not why it lands only on the youngest.",
    ("junior-engineers-deep", "zh"):
        "「消失」是流量现象而非存量现象:存量创新高,入口端(22-25 岁 × 高 AI 暴露)在 firm-time 固定效应内持续收缩且 2024 年后加深。RCT 一致显示 AI 个体层面最帮新手;雇佣是组织对成本结构的响应,两者在企业账本上是同一句话。宏观混淆项解释水位、解释不了构成;离岸是唯一同样能解释构成的竞争假说。全文以七个可检验主张收尾。",
    ("junior-engineers-deep", "en"):
        "The \"disappearance\" is a flow phenomenon, not a stock phenomenon: record-high stock, contracting entrance — concentrated in the youngest-by-most-exposed cell, inside firm-time fixed effects, deepening after 2024. RCTs consistently show AI helps novices most at the individual level; hiring is the firm's response to a changed cost structure, and on the ledger those are one sentence. Confounders explain the water level, not the composition; offshoring is the one rival that fits both. Closes with seven testable claims.",
    ("ai-code-review-plain", "zh"):
        "AI 写代码提速,查代码的人跟不上——瓶颈是真的。行业的药方是再买一个 AI 来查,但 AI 检查员自己会捏造 bug,而且和写代码的 AI 犯的错越来越像。有测试兜底、误报受控、人握终审权时,它是每次一美元的廉价额外保险;三个条件缺任何一个,它就开始向套娃滑动。",
    ("ai-code-review-plain", "en"):
        "AI speeds up writing code and the humans checking it can't keep up — the bottleneck is real. The industry's prescription is another AI to do the checking, but AI inspectors invent bugs of their own and increasingly make the same mistakes as the AI writers. With tests underneath, false alarms controlled, and humans holding the verdict, it's a dollar-a-run extra safety layer; remove any one condition and it slides toward nesting dolls.",
    ("ai-code-review-deep", "zh"):
        "验证瓶颈真实且在恶化(评审中位时长 +441.5%、零审查合并 +31.3%),但供给侧的证明材料已经失效:6 家自办基准发布者全部第一,同一工具跨基准分数差 3.7 倍;第一方生产漏斗显示离线分数与生产价值隔一个数量级(Meta 67.96%→19.75%);错误趋同正在瓦解'AI 验证 AI'的独立性前提。裁决是条件句:独立 oracle + 控误报 + 人握裁决 = 解药,否则是套娃。全文以八个可检验主张收尾。",
    ("ai-code-review-deep", "en"):
        "The verification bottleneck is real and worsening (median review time +441.5%, zero-review merges +31.3%), but the supply side's evidence regime has failed: six self-run benchmarks, publisher first every time, the same tool varying 3.7× across exams; first-party production funnels put an order of magnitude between offline scores and production value (Meta 67.96%→19.75%); converging errors are dissolving the independence premise of AI-verifying-AI. The verdict is conditional: independent oracle + controlled false alarms + humans keeping the verdict = cure; otherwise, turtles. Closes with eight testable claims.",
    ("agent-readme-deep", "zh"):
        "AGENTS.md 在标准之争中事实胜出(LF 中立托管、Cursor/Copilot/VS Code 原生消费),但互认不对称、symlink 仍是通用解;四厂商指南共识整齐却零对照组。第一批对照实证互相打架:效率增益(-28.64% 耗时、-16.58% token,p<0.05)是唯一带统计检验的效应,成功率方向三项研究互相矛盾且旗舰阴性研究的方向性数字被方法学审计否决(零推断统计、单次采样、有效 n=12);「怎么排版」四变量对遵从率无可检测效应,任务类型与会话深度才是主变量。llms.txt 是「采用≠消费」的多源证实盖棺案例(97% 零请求);上下文文件已是带 PoC 的攻击面。以六步落地 playbook 和十个可检验主张收尾。",
    ("agent-readme-deep", "en"):
        "AGENTS.md has won the standards war on facts (LF neutral hosting; native consumption by Cursor/Copilot/VS Code), but recognition is asymmetric and the symlink remains the universal adapter; the four vendor guides agree neatly — with zero control groups. The first controlled studies fight each other: the efficiency gain (−28.64% wall-clock, −16.58% tokens, p<0.05) is the only statistically tested effect; on success rates three studies contradict one another, and the flagship negative study's directional numbers were struck down by methods audit (no inferential statistics, single sampling, effective n=12); the formatting folklore shows no detectable compliance effect — task identity and session depth dominate. llms.txt is the multi-source closed case for adoption ≠ consumption (97% zero requests); context files are now a PoC-backed attack surface. Closes with a six-step rollout playbook and ten testable claims.",
    ("agent-readme-plain", "zh"):
        "给代码库写 AGENTS.md/CLAUDE.md 值得,但证据和口号不一样:省 28.64% 时间、16.58% token 是唯一带统计检验的数字;成功率方向三项研究互相打架,谁也没赢;「短了更听话」「重要的放开头」这些讲究在随机实验里全无效应。该写的是命令、禁令和 AI 猜不到的团队私规;该防的是把这个文件当攻击面的供应链注入。附六步行动清单。",
    ("agent-readme-plain", "en"):
        "Writing an AGENTS.md/CLAUDE.md is worth it — but the evidence differs from the slogans: 28.64% time and 16.58% token savings are the only statistically tested numbers; on success rates, three studies fight each other and nobody has won; 'keep it short' and 'important things first' showed zero effect in the randomized test. Write commands, prohibitions, and the house rules AI can't guess; guard against supply-chain injection that treats the file as an attack surface. Six-step action list included.",
}

CHIPS = {
    ("automation-irony-deep", "zh"): [
        ("c1", "96 票对抗验证 · 32/32 挺过"), ("c2", "在场 RR 1.24 vs 撤后 -6.0pp"), ("c3", "可工程化 + 3 个硬底"), ("c4", "11 个可检验主张"),
    ],
    ("automation-irony-deep", "en"): [
        ("c1", "96 votes · 32/32 survived"), ("c2", "in-use RR 1.24 vs post-AI −6.0pp"), ("c3", "engineerable + 3 hard floors"), ("c4", "11 testable claims"),
    ],
    ("automation-irony-plain", "zh"): [
        ("c1", "从不出错的自动化:检出 33% vs 82%"), ("c2", "20 小时 AI 课防不住:-14pp"), ("c3", "资深医生也掉到 45.5%"), ("c4", "撤走 AI 后:28.4%→22.4%"),
    ],
    ("automation-irony-plain", "en"): [
        ("c1", "never-failing automation: 33% vs 82%"), ("c2", "20h AI course didn't help: −14pp"), ("c3", "even experts fall to 45.5%"), ("c4", "after AI removed: 28.4%→22.4%"),
    ],
    ("seventy-percent-failure-deep", "zh"): [
        ("c1", "90 票对抗验证 · 30/30 挺过"), ("c2", "考古:1993 非科学估计 → 2009 假出处"), ("c3", "基率:已发表估计 7-90%"), ("c4", "11 个可检验主张"),
    ],
    ("seventy-percent-failure-deep", "en"): [
        ("c1", "90 votes · 30/30 survived"), ("c2", "1993 'unscientific' → 2009 invented source"), ("c3", "base rate: estimates span 7-90%"), ("c4", "11 testable claims"),
    ],
    ("seventy-percent-failure-plain", "zh"): [
        ("c1", "Kotter 1995:原文无 70%"), ("c2", "同一批数据:88% 失败 或 87% 过半"), ("c3", "仅 21% 重设计工作流"), ("c4", "78% 员工自带 AI 工具"),
    ],
    ("seventy-percent-failure-plain", "en"): [
        ("c1", "Kotter 1995: no 70% in the text"), ("c2", "same data: 88% fail or 87% halfway"), ("c3", "only 21% redesigned workflows"), ("c4", "78% bring their own AI"),
    ],
    ("machine-oracles-deep", "zh"): [
        ("c1", "87 票对抗验证 · 29/29 挺过"), ("c2", "裁判席:TOGA 0.38% · PrimeVul 3.09%"), ("c3", "生成器席:OSS-Fuzz 26 漏洞"), ("c4", "11 个可检验主张"),
    ],
    ("machine-oracles-deep", "en"): [
        ("c1", "87 votes · 29/29 survived"), ("c2", "judge seat: TOGA 0.38% · PrimeVul 3.09%"), ("c3", "generator seat: OSS-Fuzz 26 vulns"), ("c4", "11 testable claims"),
    ],
    ("machine-oracles-plain", "zh"): [
        ("c1", "证明完成率 88→90%"), ("c2", "Argus 消融:证明器 0/20 → GPT-5 裁判 20/20"), ("c3", "curl 真报率 <5% → 反超 15-16%"), ("c4", "AI 断言 99% 锚旧行为"),
    ],
    ("machine-oracles-plain", "en"): [
        ("c1", "proof completion 88→90%"), ("c2", "Argus: prover 0/20 → GPT-5 judge 20/20"), ("c3", "curl real rate <5% → 15-16%"), ("c4", "AI assertions: 99% anchor old behavior"),
    ],
    ("learning-science-deep", "zh"): [
        ("c1", "72 票对抗验证 · 24/24 挺过"), ("c2", "刻意练习:方差仅 14%(勘误后)"), ("c3", "学习风格:信念 89% vs 互作 26%"), ("c4", "12 个可检验主张"),
    ],
    ("learning-science-deep", "en"): [
        ("c1", "72 votes · 24/24 survived"), ("c2", "deliberate practice: 14% of variance"), ("c3", "styles: 89% belief vs 26% crossover"), ("c4", "12 testable claims"),
    ],
    ("learning-science-plain", "zh"): [
        ("c1", "读 14 遍 40% vs 考 3 次 61%"), ("c2", "一万小时:复现不成立"), ("c3", "九成教师信学习风格"), ("c4", "交错课堂 RCT:61 vs 38 分"),
    ],
    ("learning-science-plain", "en"): [
        ("c1", "read 14×: 40% vs test 3×: 61%"), ("c2", "10,000 hrs: failed replication"), ("c3", "9 in 10 teachers buy styles"), ("c4", "interleaving RCT: 61 vs 38"),
    ],
    ("scalable-oversight-deep", "zh"): [
        ("c1", "60 票对抗验证 · 20/20 挺过"), ("c2", "创始假设 → 公理:4 年"), ("c3", "debate@Elo差400 ≈ 抛硬币"), ("c4", "9 个可检验主张"),
    ],
    ("scalable-oversight-deep", "en"): [
        ("c1", "60 votes · 20/20 survived"), ("c2", "assumption → axiom in 4 yrs"), ("c3", "debate @ Elo-400 ≈ coin flip"), ("c4", "9 testable claims"),
    ],
    ("scalable-oversight-plain", "zh"): [
        ("c1", "辩论:60% → 88%(有条件)"), ("c2", "自查自洽率仅 76%"), ("c3", "内心独白复述率 25-39%"), ("c4", "数学证明:裁判不可收买"),
    ],
    ("scalable-oversight-plain", "en"): [
        ("c1", "debate: 60% → 88% (conditional)"), ("c2", "self-check agreement: 76%"), ("c3", "inner monologue: 25-39%"), ("c4", "math proofs: incorruptible judge"),
    ],
    ("ai-native-plain", "zh"): [
        ("c1", "90% 在用 AI"), ("c2", "实测 −19% vs 自感 +20%"), ("c3", "稳定性连续两年负相关"), ("c4", "迁移:1.5 人年 → 6 周"),
    ],
    ("ai-native-plain", "en"): [
        ("c1", "90% use AI"), ("c2", "measured −19% vs felt +20%"), ("c3", "stability negative 2 yrs running"), ("c4", "migration: 1.5 eng-yrs → 6 wks"),
    ],
    ("ai-native-deep", "zh"): [
        ("c1", "86 个来源"), ("c2", "166 票对抗验证"), ("c3", "4 大理论光谱"), ("c4", "6 个可检验主张"),
    ],
    ("ai-native-deep", "en"): [
        ("c1", "86 sources"), ("c2", "166 adversarial votes"), ("c3", "4 theoretical spectra"), ("c4", "6 testable claims"),
    ],
    ("junior-engineers-plain", "zh"): [
        ("c1", "总就业创新高"), ("c2", "22-25 岁 ≈ −20%"), ("c3", "大厂新人 3 成 → 1 成"), ("c4", "RCT:新手受益最大"),
    ],
    ("junior-engineers-plain", "en"): [
        ("c1", "employment: record high"), ("c2", "age 22-25: ≈ −20%"), ("c3", "new grads: 3-in-10 → 1-in-10"), ("c4", "RCTs: novices gain most"),
    ],
    ("junior-engineers-deep", "zh"): [
        ("c1", "7 条线索 · 103 论断"), ("c2", "45 票对抗验证"), ("c3", "13/15 挺过反驳"), ("c4", "7 个可检验主张"),
    ],
    ("junior-engineers-deep", "en"): [
        ("c1", "7 lines · 103 claims"), ("c2", "45 adversarial votes"), ("c3", "13/15 survived refutation"), ("c4", "7 testable claims"),
    ],
    ("ai-code-review-plain", "zh"): [
        ("c1", "评审时长 +441.5%"), ("c2", "6/6 自办基准第一"), ("c3", "Meta 离线 68% → 生产 19.75%"), ("c4", "AI 评论采纳率 0.9–19.2%"),
    ],
    ("ai-code-review-plain", "en"): [
        ("c1", "review time +441.5%"), ("c2", "6/6 self-benchmarks won"), ("c3", "Meta offline 68% → prod 19.75%"), ("c4", "AI comments acted on: 0.9–19.2%"),
    ],
    ("ai-code-review-deep", "zh"): [
        ("c1", "7 条线索 · 15 条承重论断"), ("c2", "45 票对抗验证"), ("c3", "9 过 · 6 修正 · 0 推翻"), ("c4", "8 个可检验主张"),
    ],
    ("ai-code-review-deep", "en"): [
        ("c1", "7 lines · 15 load-bearing claims"), ("c2", "45 adversarial votes"), ("c3", "9 held · 6 amended · 0 overturned"), ("c4", "8 testable claims"),
    ],
    ("agent-readme-deep", "zh"): [
        ("c1", "三轮验证 · 审计否决 2 组流传数字"), ("c2", "唯一带统计检验的收益:-28.64% 耗时"), ("c3", "成功率:三项研究互相矛盾"), ("c4", "10 个可检验主张"),
    ],
    ("agent-readme-deep", "en"): [
        ("c1", "3 rounds · 2 famous numbers struck"), ("c2", "only tested win: −28.64% time"), ("c3", "success rates: 3 studies at war"), ("c4", "10 testable claims"),
    ],
    ("agent-readme-plain", "zh"): [
        ("c1", "省时 28.64% · 省 token 16.58%"), ("c2", "成功率:研究互相打架"), ("c3", "写法讲究:随机实验全无效应"), ("c4", "六步行动清单"),
    ],
    ("agent-readme-plain", "en"): [
        ("c1", "−28.64% time · −16.58% tokens"), ("c2", "success rates: studies at war"), ("c3", "formatting folklore: zero effect"), ("c4", "six-step action list"),
    ],
}

VERSION_NOTES = {
    ("zh", "plain"): '本文是<strong>易读版</strong> · <a href="{other}">查看深入版(完整论证与出处)→</a>',
    ("zh", "deep"):  '本文是<strong>深入版</strong> · <a href="{other}">查看易读版(精简直白)→</a>',
    ("en", "plain"): 'This is the <strong>plain-language edition</strong> · <a href="{other}">read the deep dive (full arguments &amp; sources) →</a>',
    ("en", "deep"):  'This is the <strong>deep-dive edition</strong> · <a href="{other}">read the plain-language edition →</a>',
}

# Footer pointer lines in the md sources reference local files / the other edition by
# name; on the web the version-note banner covers this, so strip them.
STRIP_PATTERNS = [
    re.compile(r"^\*想看每个结论的完整论证.*$", re.M),
    re.compile(r"^\*For the full arguments, every source.*$", re.M),
    re.compile(r"^\*详细的证据分级.*$", re.M),
    re.compile(r"^\*For detailed evidence grading.*$", re.M),
]


def article_fname(slug: str, lang: str) -> str:
    return f"{slug}.html" if lang == "zh" else f"{slug}.en.html"


def build_articles():
    for slug, lang, version, title, desc, date in ARTICLES:
        md = Path(f"sources/{slug}.{lang}.md").read_text(encoding="utf-8")
        for pat in STRIP_PATTERNS:
            md = pat.sub("", md)
        # Drop the md h1 and the leading methodology blockquote (the TL;DR box +
        # chips replace them above the fold; deep editions keep their inline notes).
        md = re.sub(r"^#\s+.*\n", "", md, count=1)
        body = md_to_html(md)
        body = inject_figures(body, slug, lang)
        other = article_fname(slug, "en" if lang == "zh" else "zh")
        this = article_fname(slug, lang)
        other_version = (slug.replace("-plain", "-deep") if version == "plain"
                         else slug.replace("-deep", "-plain"))
        if lang == "zh":
            lang_toggle = f'<a href="{this}" class="active">中文</a><a href="{other}">EN</a>'
            index_href = "index.html"
        else:
            lang_toggle = f'<a href="{other}">中文</a><a href="{this}" class="active">EN</a>'
            index_href = "index.en.html"
        chips = "".join(f'<span class="chip {cls}">{txt}</span>' for cls, txt in CHIPS[(slug, lang)])
        page = ARTICLE_TMPL.format(
            html_lang="zh-CN" if lang == "zh" else "en",
            title=title, desc=desc, css=ARTICLE_CSS, h2_css=h2_color_css(body),
            lang_toggle=lang_toggle, index_href=index_href,
            kicker=KICKERS[(lang, version)],
            version_note=VERSION_NOTES[(lang, version)].format(other=article_fname(other_version, lang)),
            tldr=TLDRS[(slug, lang)], chips=chips,
            body=body, date=date, scripts=SHARED_SCRIPTS,
        )
        Path(this).write_text(page, encoding="utf-8")
        print(f"Written {this} ({len(page)} bytes)")


# ---------------------------------------------------------------- index pages

INDEX_CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:"PingFang SC","Microsoft YaHei",-apple-system,"Noto Serif SC",sans-serif;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0a0e1a 100%);color:#e4e6eb;line-height:1.7;min-height:100vh}
.container{max-width:860px;margin:0 auto;padding:48px 24px 80px}
header{text-align:center;padding:40px 0 30px}
header h1{font-size:2.3rem;font-weight:800;background:linear-gradient(135deg,#4cc9f0 0%,#7b61ff 55%,#ff6ec4 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:1px;margin-bottom:12px}
header .tagline{font-size:0.98rem;color:#a0a8c0;font-weight:300}
header .method{max-width:660px;margin:20px auto 0;font-size:0.82rem;color:#8a93ad;font-family:"SF Mono",Menlo,monospace;background:rgba(76,201,240,0.05);border:1px solid rgba(76,201,240,0.2);border-radius:10px;padding:12px 16px;line-height:1.65;text-align:left}
.method .step{color:#4cc9f0;font-weight:700}
.topbar{position:fixed;top:14px;right:14px;display:flex;gap:8px;z-index:100;font-family:"SF Mono",Menlo,monospace;font-size:0.75rem}
.topbar a{background:rgba(255,255,255,0.06);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:6px 13px;color:#a0a8c0;text-decoration:none}
.topbar a.active{background:#7b61ff;color:#fff;font-weight:700}
.entry{position:relative;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);border-radius:14px;padding:26px 28px;margin-bottom:18px;overflow:hidden;transition:all 0.2s}
.entry::before{content:"";position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,#4cc9f0,#7b61ff,#ff6ec4)}
.entry:hover{transform:translateY(-2px);border-color:rgba(76,201,240,0.35);box-shadow:0 6px 24px rgba(0,0,0,0.35)}
.entry .etitle{font-size:1.25rem;font-weight:700;color:#fff;margin-bottom:10px}
.entry .edesc{font-size:0.9rem;color:#a8b0c0;margin-bottom:14px;line-height:1.65}
.entry .tags{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:14px}
.entry .tag{font-family:"SF Mono",Menlo,monospace;font-size:0.7rem;font-weight:700;padding:3px 11px;border-radius:12px;border:1px solid}
.tag.t1{color:#4cc9f0;border-color:rgba(76,201,240,0.45);background:rgba(76,201,240,0.07)}
.tag.t2{color:#ff6ec4;border-color:rgba(255,110,196,0.45);background:rgba(255,110,196,0.07)}
.tag.t3{color:#5eead4;border-color:rgba(94,234,212,0.45);background:rgba(94,234,212,0.07)}
.tag.t4{color:#f0b429;border-color:rgba(240,180,41,0.45);background:rgba(240,180,41,0.07)}
.tag.t5{color:#a29bfe;border-color:rgba(162,155,254,0.45);background:rgba(162,155,254,0.07)}
.entry .emeta{font-family:"SF Mono",Menlo,monospace;font-size:0.72rem;color:#6a7080;margin-bottom:16px}
.entry .links{display:flex;gap:10px;flex-wrap:wrap}
.entry .links a{font-family:"SF Mono",Menlo,monospace;font-size:0.82rem;font-weight:700;text-decoration:none;padding:9px 20px;border-radius:9px;transition:all 0.15s}
.entry .links a.primary{background:linear-gradient(90deg,#4cc9f0,#7b61ff);color:#fff}
.entry .links a.secondary{border:1px solid rgba(255,110,196,0.5);color:#ff6ec4}
.entry .links a:hover{transform:translateY(-1px);filter:brightness(1.15)}
footer{text-align:center;padding:44px 0 12px;font-size:0.78rem;color:#5a6378}
footer a{color:#7b61ff;text-decoration:none}
.mmd-lang-toggle{display:none!important}
@media(max-width:700px){header h1{font-size:1.6rem}.container{padding:36px 16px 60px}}"""

INDEX_TMPL = """<!DOCTYPE html>
<html lang="{html_lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{page_desc}">
<style>
{css}
</style>
</head><body>
<div class="topbar">
  {lang_toggle}
</div>
<div class="container">
<header>
  <h1>{h1}</h1>
  <div class="tagline">{tagline}</div>
  <div class="method">{method}</div>
</header>
{entries}
<footer>BigCat Deep Research · <a href="https://cissy0802.github.io/">Learning Hub</a> · <a href="https://github.com/cissy0802/deep-research">GitHub</a></footer>
</div>
{scripts}
</body></html>
"""

INDEX_I18N = {
    "zh": dict(
        html_lang="zh-CN",
        page_title="深度研究 — BigCat Deep Research",
        page_desc="多 agent 深度调研 + 对抗式事实核查的研究报告。",
        h1="深度研究",
        tagline="多 agent 调研 · 对抗式核查 · 正反证据并陈",
        method='方法:<span class="step">① 调研</span> 数十至上百个 AI agent 并行阅读一手来源 → <span class="step">② 对抗核查</span> 每条关键论断由 3 名独立验证者尝试反驳(逐字核对原文、检索反证)→ <span class="step">③ 成文</span> 没挺过验证的论断被剔除或降级标注,正反证据并陈。',
    ),
    "en": dict(
        html_lang="en",
        page_title="Deep Research — BigCat",
        page_desc="Research reports built with multi-agent investigation and adversarial fact-checking.",
        h1="Deep Research",
        tagline="Multi-agent investigation · adversarial verification · counter-evidence included",
        method='Method: <span class="step">① Investigate</span> — dozens to hundreds of parallel AI agents read primary sources → <span class="step">② Adversarial check</span> — every load-bearing claim is challenged by 3 independent verifiers (word-for-word source checks, counter-evidence search) → <span class="step">③ Write</span> — claims that fail are cut or downgraded; counter-evidence stays in.',
    ),
}

# slug, date, title_zh, title_en, desc_zh, desc_en, stats_zh, stats_en, tags[(cls, zh, en)]
INDEX_ENTRIES = [
    ("ai-native", "2026-07",
     "传统软件组织的 AI-native 转型",
     "The AI-Native Transformation of Software Organizations",
     "为什么人人自觉变快、组织却更不稳定?从交易成本、Conway/Brooks、控制论到创新理论的完整论证,含高可靠 legacy 组织(BigQuery 式)专章。",
     "Why everyone feels faster while organizations get less stable — from transaction costs, Conway/Brooks and cybernetics to innovation theory, with a dedicated chapter on high-reliability legacy organizations.",
     "166 票对抗验证 · 6 个可检验主张",
     "166 adversarial votes · 6 testable claims",
     [("t1", "组织经济学", "Org economics"), ("t2", "软件工程", "Software eng"), ("t3", "复杂系统/控制论", "Cybernetics"),
      ("t4", "创新理论", "Innovation"), ("t5", "高可靠 legacy", "HRO / legacy")]),
    ("junior-engineers", "2026-07",
     "「初级工程师正在消失」是真的吗?",
     "Are Junior Engineers Really Disappearing?",
     "总就业创新高,22-25 岁一档却跌近两成——「消失」是流量现象,不是存量现象。四个数据口径逐一对表,并回答一个悖论:最帮新手的技术,为什么最先收缩新手的岗位。",
     "Employment at record highs while the 22-25 bracket falls nearly a fifth — a flow phenomenon, not a stock one. Four data gauges calibrated against each other, answering one paradox: why the technology that helps novices most shrinks novice jobs first.",
     "45 票对抗验证 · 7 个可检验主张",
     "45 adversarial votes · 7 testable claims",
     [("t1", "劳动经济学", "Labor economics"), ("t2", "招聘数据", "Hiring data"), ("t3", "RCT 证据", "RCT evidence"),
      ("t4", "职业阶梯", "Career ladder"), ("t5", "AI 与就业", "AI & jobs")]),
    ("ai-code-review", "2026-07",
     "AI code review:验证瓶颈的解药,还是套娃?",
     "AI Code Review: Cure for the Verification Bottleneck, or Turtles All the Way Down?",
     "查代码的人跟不上 AI 写代码的速度,行业的答案是再买一个 AI 来查。解剖厂商基准混战与大厂生产漏斗,追问「AI 验证 AI」还剩多少独立性——以及它在什么条件下真的管用。",
     "Humans can't keep up with reviewing AI-written code, so the industry's answer is another AI to do the checking. An anatomy of the vendor benchmark wars and big tech's production funnels, asking how much independence AI-verifying-AI retains — and when it genuinely works.",
     "45 票对抗验证 · 8 个可检验主张",
     "45 adversarial votes · 8 testable claims",
     [("t1", "验证不对称", "Verification asymmetry"), ("t2", "基准混战", "Benchmark wars"), ("t3", "大厂生产数据", "Production data"),
      ("t4", "自动化人因", "Human factors"), ("t5", "LLM 当裁判", "LLM-as-judge")]),
    ("scalable-oversight", "2026-07",
     "Scalable oversight 的地基体检",
     "A Foundation Inspection of Scalable Oversight",
     "整个「AI 看住 AI」的路线站在「验证比生成容易」一句话上——创始文献里它是带限定的假设,后来被当成了公理。理论裂缝、条件化的实证、与实验室退守 CoT 监控的生产行为,拼出这块地基的真实承重图。",
     "The whole 'AI watching AI' program stands on one sentence: 'verification is easier than generation.' The founding papers qualified it; later citation used it as an axiom. Theoretical cracks, conditional empirics, and the labs' own retreat to CoT monitoring map what the foundation actually bears.",
     "60 票对抗验证 · 9 个可检验主张",
     "60 adversarial votes · 9 testable claims",
     [("t1", "AI 对齐", "AI alignment"), ("t2", "验证不对称", "Verification asymmetry"), ("t3", "debate 实证", "Debate empirics"),
      ("t4", "弱监督强", "Weak-to-strong"), ("t5", "CoT 监控", "CoT monitoring")]),
    ("learning-science", "2026-07",
     "学习科学的证据等级:哪些方法真的有效?",
     "The Evidence Hierarchy of Learning Science: What Actually Works?",
     "一万小时、学习风格、划重点——为什么流行的学习建议和实测证据几乎对不上?五场学术对战逐一对账,把常见学习方法按证据强度重新排座次,并给出读效应量数字的防骗规则。",
     "Ten thousand hours, learning styles, highlighting — why does popular study advice barely overlap with the measured evidence? Five academic battles audited one by one, the common methods re-seated by evidence strength, with anti-scam rules for reading effect sizes.",
     "72 票对抗验证 · 12 个可检验主张",
     "72 adversarial votes · 12 testable claims",
     [("t1", "学习科学", "Learning science"), ("t2", "meta 分析", "Meta-analyses"), ("t3", "刻意练习之战", "Deliberate practice"),
      ("t4", "学习风格神话", "Learning styles"), ("t5", "主动学习", "Active learning")]),
    ("machine-oracles", "2026-07",
     "机器裁判全景:LLM 能把软件验证的 oracle 做大多少?",
     "The Machine-Judge Atlas: How Much Can LLMs Scale Software's Oracles?",
     "同一种 AI,接崩溃检测器产出二十年 CVE,扔给人类分诊却是 slop 洪水——差别只在裁判是谁。按软件验证的裁判家族逐格盘点,核查每格「LLM 增益」的正反证据。",
     "The same AI yields a twenty-year CVE plugged into a crash detector and a slop flood dumped on human triage — the only difference is who judges. A cell-by-cell audit of software's oracle families, checking the evidence for and against each cell's 'LLM gain'.",
     "87 票对抗验证 · 11 个可检验主张",
     "87 adversarial votes · 11 testable claims",
     [("t1", "验证不对称", "Verification asymmetry"), ("t2", "test oracle", "Test oracles"), ("t3", "形式验证", "Formal verification"),
      ("t4", "fuzzing/差分", "Fuzzing / differencing"), ("t5", "LLM 当裁判", "LLM-as-judge")]),
    ("seventy-percent-failure", "2026-07",
     "「70% 转型失败」考古:上一轮的尸检报告能预测 AI 吗?",
     "The '70% of Transformations Fail' Autopsy: Does the Last Wave Predict AI?",
     "被整个变革工业当了三十年招牌的「70% 会失败」,是谁测出来的?——没有人。追溯这个数字的引用链原文,复读真实失败率的测量记录,再用 Agile/DevOps 留下的完整档案,评估上一轮转型对 AI-native 转型的预测力。",
     "The transformation industry's thirty-year calling card — '70% fail' — was measured by whom? Nobody, it turns out. A citation autopsy of the number, a re-reading of the measured failure-rate record, and an audit of the Agile/DevOps archives for what they do and don't predict about AI-native transformation.",
     "90 票对抗验证 · 11 个可检验主张",
     "90 adversarial votes · 11 testable claims",
     [("t1", "组织变革", "Org change"), ("t2", "僵尸统计", "Zombie statistics"), ("t3", "Agile/DevOps 档案", "Agile/DevOps record"),
      ("t4", "制度同构", "Institutional isomorphism"), ("t5", "AI 转型", "AI transformation")]),
    ("agent-readme", "2026-07",
     "给 Agent 看的 README:上下文文件是基建还是货物崇拜?",
     "The README for Agents: Infrastructure or Cargo Cult?",
     "人人都说要给代码库写 AGENTS.md/CLAUDE.md,但第一批对照实证互相打架,方法学审计还否决了两组流传最广的数字。标准之争、厂商共识、安全攻击面与企业落地 playbook,逐条对抗核验+反证搜索。",
     "Everyone says your repo needs an AGENTS.md/CLAUDE.md — but the first controlled studies fight each other, and a hostile methods audit struck down two of the most-quoted numbers. The standards war, the vendor consensus, the attack surface, and an enterprise rollout playbook — adversarially verified, contradiction-searched, claim by claim.",
     "三轮 117 份验证 · 10 个可检验主张",
     "117 verdicts across 3 rounds · 10 testable claims",
     [("t1", "Agent 上下文文件", "Agent context files"), ("t2", "AGENTS.md 标准", "AGENTS.md standard"), ("t3", "对照实证", "Controlled evidence"),
      ("t4", "prompt injection", "Prompt injection"), ("t5", "落地 playbook", "Rollout playbook")]),
    ("automation-irony", "2026-07",
     "自动化的反讽:AI 越好,人握的终审越会退化吗?",
     "The Ironies of Automation: Does the Human Veto Decay as AI Improves?",
     "自动化越可靠,人这个终审席位退化越快——1983 年的预言正在 AI 工作流里重演吗?从 40 年人因工程实验、航空与医疗两份现场档案,到最新的 AI 时代证据与干预实测,给「人握终审」做一次全面体检。",
     "The more reliable the automation, the faster the human veto seat decays — is the 1983 prophecy replaying inside AI workflows? A full physical for 'the human holds the veto': forty years of human-factors experiments, the aviation and medicine field archives, and the newest AI-era evidence with measured interventions.",
     "96 票对抗验证 · 11 个可检验主张",
     "96 adversarial votes · 11 testable claims",
     [("t1", "自动化人因", "Human factors"), ("t2", "技能退化", "Skill decay"), ("t3", "automation bias", "Automation bias"),
      ("t4", "人在环", "Human-in-the-loop"), ("t5", "AI 工作流设计", "AI workflow design")]),
]


def build_indexes():
    for lang, fname in (("zh", "index.html"), ("en", "index.en.html")):
        t = INDEX_I18N[lang]
        cards = []
        for slug, date, tzh, ten, dzh, den, szh, sen, tags in INDEX_ENTRIES:
            if lang == "zh":
                title, desc, stats = tzh, dzh, szh
                plain, deep = f"{slug}-plain.html", f"{slug}-deep.html"
                l_plain, l_deep = "📖 易读版", "🔬 深入版"
            else:
                title, desc, stats = ten, den, sen
                plain, deep = f"{slug}-plain.en.html", f"{slug}-deep.en.html"
                l_plain, l_deep = "📖 Plain-language", "🔬 Deep dive"
            tag_html = "".join(
                f'<span class="tag {cls}">{zh if lang == "zh" else en}</span>' for cls, zh, en in tags)
            cards.append(f"""<div class="entry">
  <div class="etitle">{title}</div>
  <div class="edesc">{desc}</div>
  <div class="tags">{tag_html}</div>
  <div class="emeta">{date} · {stats}</div>
  <div class="links">
    <a class="primary" href="{plain}">{l_plain}</a>
    <a class="secondary" href="{deep}">{l_deep}</a>
  </div>
</div>""")
        if lang == "zh":
            lang_toggle = '<a href="index.html" class="active">中文</a><a href="index.en.html">EN</a>'
        else:
            lang_toggle = '<a href="index.html">中文</a><a href="index.en.html" class="active">EN</a>'
        page = INDEX_TMPL.format(css=INDEX_CSS, lang_toggle=lang_toggle,
                                 entries="\n".join(cards), scripts=SHARED_SCRIPTS, **t)
        Path(fname).write_text(page, encoding="utf-8")
        print(f"Written {fname} ({len(page)} bytes)")


if __name__ == "__main__":
    build_articles()
    build_indexes()
