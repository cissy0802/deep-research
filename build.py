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


# slug → list of (lang_or_None, version_or_None, heading_text_prefix, figure_fn)
# figure inserted right AFTER the first heading whose text starts with the prefix.
FIGURES = {
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
}


def inject_figures(body: str, slug: str, lang: str) -> str:
    for fig_lang, prefix, fn in FIGURES.get(slug, []):
        if fig_lang != lang:
            continue
        pat = re.compile(r"(<h[23]>" + re.escape(prefix)[:60] + r"[^<]*</h[23]>)")
        m = pat.search(body)
        if m:
            # insert after the first paragraph following the heading (reads better)
            after = body[m.end():]
            p_end = after.find("</p>")
            pos = m.end() + (p_end + 4 if p_end != -1 else 0)
            body = body[:pos] + "\n" + fn(lang) + body[pos:]
        else:
            print(f"  WARN figure anchor not found: {slug} {lang} '{prefix}'")
    return body


# ---------------------------------------------------------------- page templates

SHARED_SCRIPTS = """<script src="https://cissy0802.github.io/comments.js" defer></script>
<script src="https://cissy0802.github.io/search.js" defer></script>
<script src="https://cissy0802.github.io/index-button.js" defer></script>
<script src="https://cissy0802.github.io/i18n-tts.js" defer></script>"""

# Section accent colors cycled by h2 order (matches the hub's multi-color card language).
H2_COLORS = ["#4cc9f0", "#7b61ff", "#ff6ec4", "#5eead4", "#f0b429", "#52b788", "#e8794b", "#a29bfe"]

ARTICLE_CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,"SF Pro Display","Noto Serif SC","Songti SC",serif;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0a0e1a 100%);color:#dde1ea;line-height:1.85;min-height:100vh}
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
]

KICKERS = {
    ("zh", "plain"): "深度研究 · 易读版",
    ("zh", "deep"):  "深度研究 · 深入版",
    ("en", "plain"): "Deep Research · Plain-language",
    ("en", "deep"):  "Deep Research · Deep dive",
}

TLDRS = {
    ("ai-native-plain", "zh"):
        "AI 把「写代码」变便宜,把瓶颈推到「确认代码是对的」。个人变快 ≠ 组织变快;评估 AI 靠交付数据、不靠体感;维护高可靠老系统的组织,从迁移类任务切入、护栏先于规模。",
    ("ai-native-plain", "en"):
        "AI makes writing code cheap and pushes the bottleneck to confirming the code is right. Faster individuals ≠ a faster organization; judge AI by delivery data, not gut feel; legacy organizations should enter through migrations, guardrails before scale.",
    ("ai-native-deep", "zh"):
        "交易成本没有消失,而是从生产/协调转移到整合/验证——这一枢轴同时解释了 METR 的减速、DORA 的稳定性惩罚与人的角色重构,并推出高可靠 legacy 组织「迁移切入 → 护栏先于规模 → 验证基础设施资本化」的转型序列。全文以六个可检验主张收尾。",
    ("ai-native-deep", "en"):
        "Transaction costs don't disappear — they migrate from production/coordination to integration/verification. This single pivot explains METR's slowdown, DORA's stability penalty, and the restructuring of human roles, and yields the sequence for high-reliability legacy organizations: enter through migrations → guardrails before scale → capitalize verification infrastructure. The essay closes with six testable claims.",
}

CHIPS = {
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
}

VERSION_NOTES = {
    ("zh", "plain"): '本文是<strong>易读版</strong> · <a href="ai-native-deep.html">查看深入版(完整论证与出处)→</a>',
    ("zh", "deep"):  '本文是<strong>深入版</strong> · <a href="ai-native-plain.html">查看易读版(精简直白)→</a>',
    ("en", "plain"): 'This is the <strong>plain-language edition</strong> · <a href="ai-native-deep.en.html">read the deep dive (full arguments &amp; sources) →</a>',
    ("en", "deep"):  'This is the <strong>deep-dive edition</strong> · <a href="ai-native-plain.en.html">read the plain-language edition →</a>',
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
            version_note=VERSION_NOTES[(lang, version)],
            tldr=TLDRS[(slug, lang)], chips=chips,
            body=body, date=date, scripts=SHARED_SCRIPTS,
        )
        Path(this).write_text(page, encoding="utf-8")
        print(f"Written {this} ({len(page)} bytes)")


# ---------------------------------------------------------------- index pages

INDEX_CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,"SF Pro Display","Noto Serif SC","Songti SC",sans-serif;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0a0e1a 100%);color:#e4e6eb;line-height:1.7;min-height:100vh}
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
     "86 个来源 · 166 票对抗验证",
     "86 sources · 166 adversarial votes",
     [("t1", "组织经济学", "Org economics"), ("t2", "软件工程", "Software eng"), ("t3", "复杂系统/控制论", "Cybernetics"),
      ("t4", "创新理论", "Innovation"), ("t5", "高可靠 legacy", "HRO / legacy")]),
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
