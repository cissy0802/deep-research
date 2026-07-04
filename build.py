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
FIGURES = {
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

SHARED_SCRIPTS = """<script src="https://cissy0802.github.io/comments.js" defer></script>
<script src="https://cissy0802.github.io/search.js" defer></script>
<script src="https://cissy0802.github.io/index-button.js" defer></script>
<script src="https://cissy0802.github.io/i18n-tts.js" defer></script>"""

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
}

CHIPS = {
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
