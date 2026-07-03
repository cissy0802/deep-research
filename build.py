#!/usr/bin/env python3
"""Render sources/*.md into styled HTML pages for the Deep Research site.

Run from repo root:  python3 build.py
Adds a new research piece = drop 4 md files in sources/ (slug.{zh,en}.md × plain/deep),
add an entry to ARTICLES and INDEX_ENTRIES below, re-run.
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
    body = "\n".join(out)
    # First h1 becomes the page title block; drop it from body (template renders it).
    return body


# ---------------------------------------------------------------- page templates

SHARED_SCRIPTS = """<script src="https://cissy0802.github.io/comments.js" defer></script>
<script src="https://cissy0802.github.io/search.js" defer></script>
<script src="https://cissy0802.github.io/index-button.js" defer></script>
<script src="https://cissy0802.github.io/i18n-tts.js" defer></script>"""

ARTICLE_CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,"SF Pro Display","Noto Serif SC","Songti SC",serif;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0a0e1a 100%);color:#dde1ea;line-height:1.85;min-height:100vh}
.container{max-width:760px;margin:0 auto;padding:56px 24px 90px}
h1{font-size:1.9rem;font-weight:800;line-height:1.4;background:linear-gradient(135deg,#4cc9f0 0%,#7b61ff 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px}
h2{font-size:1.35rem;font-weight:700;color:#fff;margin:44px 0 14px;padding-top:10px;border-top:1px solid rgba(123,97,255,0.25)}
h3{font-size:1.08rem;font-weight:700;color:#c9d4ff;margin:30px 0 10px}
p{margin:0 0 16px}
ul,ol{margin:0 0 16px 1.4em}
li{margin-bottom:8px}
strong{color:#fff}
em{color:#b8c4e8}
code{font-family:"SF Mono",Menlo,monospace;font-size:0.85em;background:rgba(123,97,255,0.15);padding:1px 6px;border-radius:4px;color:#c9d4ff}
a{color:#4cc9f0;text-decoration:none;border-bottom:1px dotted rgba(76,201,240,0.4)}
a:hover{color:#7b61ff}
blockquote{border-left:3px solid #4cc9f0;background:rgba(76,201,240,0.06);padding:14px 18px;margin:0 0 20px;border-radius:0 8px 8px 0;font-size:0.92rem;color:#a8b4d0}
blockquote p{margin-bottom:8px}
blockquote p:last-child{margin-bottom:0}
hr{border:none;border-top:1px solid rgba(255,255,255,0.12);margin:36px 0}
.topbar{position:fixed;top:14px;right:14px;display:flex;gap:8px;z-index:100;font-family:"SF Mono",Menlo,monospace;font-size:0.75rem}
.topbar a{background:rgba(255,255,255,0.06);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:6px 13px;color:#a0a8c0;border-bottom:none}
.topbar a.active{background:#7b61ff;color:#fff;font-weight:700}
.topbar a:hover:not(.active){background:rgba(255,255,255,0.1);color:#fff}
.version-note{display:inline-block;font-family:"SF Mono",Menlo,monospace;font-size:0.76rem;color:#4cc9f0;border:1px solid rgba(76,201,240,0.35);border-radius:14px;padding:3px 12px;margin:6px 0 26px}
.version-note a{border-bottom:none;font-weight:700}
.backlink{font-family:"SF Mono",Menlo,monospace;font-size:0.8rem;margin-bottom:18px;display:inline-block;border-bottom:none;color:#7b61ff}
footer{margin-top:56px;padding-top:18px;border-top:1px solid rgba(255,255,255,0.1);font-size:0.75rem;color:#5a6378;font-family:"SF Mono",Menlo,monospace}
footer a{border-bottom:none}
@media(max-width:700px){.container{padding:44px 16px 70px}h1{font-size:1.5rem}.topbar{top:8px;right:8px}}"""

ARTICLE_TMPL = """<!DOCTYPE html>
<html lang="{html_lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — BigCat Deep Research</title>
<meta name="description" content="{desc}">
<style>
{css}
</style>
</head><body>
<div class="topbar">
  {lang_toggle}
</div>
<div class="container">
<a class="backlink" href="{index_href}">← Deep Research</a>
<h1>{title}</h1>
<div class="version-note">{version_note}</div>
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
        # Drop the md h1 (template renders the title).
        md = re.sub(r"^#\s+.*\n", "", md, count=1)
        body = md_to_html(md)
        other = article_fname(slug, "en" if lang == "zh" else "zh")
        this = article_fname(slug, lang)
        if lang == "zh":
            lang_toggle = f'<a href="{this}" class="active">中文</a><a href="{other}">EN</a>'
            index_href = "index.html"
        else:
            lang_toggle = f'<a href="{other}">中文</a><a href="{this}" class="active">EN</a>'
            index_href = "index.en.html"
        page = ARTICLE_TMPL.format(
            html_lang="zh-CN" if lang == "zh" else "en",
            title=title, desc=desc, css=ARTICLE_CSS,
            lang_toggle=lang_toggle, index_href=index_href,
            version_note=VERSION_NOTES[(lang, version)],
            body=body, date=date, scripts=SHARED_SCRIPTS,
        )
        Path(this).write_text(page, encoding="utf-8")
        print(f"Written {this} ({len(page)} bytes)")


# ---------------------------------------------------------------- index pages

INDEX_CSS = """*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,"SF Pro Display","Noto Serif SC","Songti SC",sans-serif;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0a0e1a 100%);color:#e4e6eb;line-height:1.7;min-height:100vh}
.container{max-width:860px;margin:0 auto;padding:48px 24px 80px}
header{text-align:center;padding:40px 0 34px}
header h1{font-size:2.2rem;font-weight:800;background:linear-gradient(135deg,#4cc9f0 0%,#7b61ff 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:1px;margin-bottom:12px}
header .tagline{font-size:0.98rem;color:#a0a8c0;font-weight:300}
header .method{max-width:640px;margin:18px auto 0;font-size:0.82rem;color:#8a93ad;font-family:"SF Mono",Menlo,monospace;background:rgba(76,201,240,0.05);border:1px solid rgba(76,201,240,0.2);border-radius:10px;padding:12px 16px;line-height:1.65}
.topbar{position:fixed;top:14px;right:14px;display:flex;gap:8px;z-index:100;font-family:"SF Mono",Menlo,monospace;font-size:0.75rem}
.topbar a{background:rgba(255,255,255,0.06);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:6px 13px;color:#a0a8c0;text-decoration:none}
.topbar a.active{background:#7b61ff;color:#fff;font-weight:700}
.entry{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.09);border-left:4px solid #4cc9f0;border-radius:12px;padding:24px 26px;margin-bottom:16px}
.entry .etitle{font-size:1.2rem;font-weight:700;color:#fff;margin-bottom:8px}
.entry .edesc{font-size:0.9rem;color:#a8b0c0;margin-bottom:16px}
.entry .emeta{font-family:"SF Mono",Menlo,monospace;font-size:0.72rem;color:#6a7080;margin-bottom:14px}
.entry .links{display:flex;gap:10px;flex-wrap:wrap}
.entry .links a{font-family:"SF Mono",Menlo,monospace;font-size:0.82rem;font-weight:700;text-decoration:none;padding:8px 18px;border-radius:8px;transition:all 0.15s}
.entry .links a.primary{background:linear-gradient(90deg,#4cc9f0,#7b61ff);color:#fff}
.entry .links a.secondary{border:1px solid rgba(76,201,240,0.45);color:#4cc9f0}
.entry .links a:hover{transform:translateY(-1px);filter:brightness(1.1)}
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
        method="方法:每篇研究由数十至上百个 AI agent 并行调研一手来源;关键论断各由 3 名独立验证者尝试反驳(逐字核对原文、检索反证),没挺过验证的论断被剔除或降级标注。",
    ),
    "en": dict(
        html_lang="en",
        page_title="Deep Research — BigCat",
        page_desc="Research reports built with multi-agent investigation and adversarial fact-checking.",
        h1="Deep Research",
        tagline="Multi-agent investigation · adversarial verification · counter-evidence included",
        method="Method: each report is researched by dozens to hundreds of parallel AI agents reading primary sources; every load-bearing claim is challenged by 3 independent verifiers (word-for-word source checks, counter-evidence search). Claims that fail are cut or downgraded.",
    ),
}

# slug, date, title_zh, title_en, desc_zh, desc_en, stats_zh, stats_en
INDEX_ENTRIES = [
    ("ai-native", "2026-07",
     "传统软件组织的 AI-native 转型",
     "The AI-Native Transformation of Software Organizations",
     "为什么人人自觉变快、组织却更不稳定?从交易成本、Conway/Brooks、控制论到创新理论的完整论证,含高可靠 legacy 组织(BigQuery 式)专章。",
     "Why everyone feels faster while organizations get less stable — from transaction costs, Conway/Brooks and cybernetics to innovation theory, with a dedicated chapter on high-reliability legacy organizations.",
     "86 个来源 · 166 票对抗验证 · 中英双语",
     "86 sources · 166 adversarial votes · bilingual"),
]


def build_indexes():
    for lang, fname in (("zh", "index.html"), ("en", "index.en.html")):
        t = INDEX_I18N[lang]
        cards = []
        for slug, date, tzh, ten, dzh, den, szh, sen in INDEX_ENTRIES:
            if lang == "zh":
                title, desc, stats = tzh, dzh, szh
                plain, deep = f"{slug}-plain.html", f"{slug}-deep.html"
                l_plain, l_deep = "📖 易读版", "🔬 深入版"
            else:
                title, desc, stats = ten, den, sen
                plain, deep = f"{slug}-plain.en.html", f"{slug}-deep.en.html"
                l_plain, l_deep = "📖 Plain-language", "🔬 Deep dive"
            cards.append(f"""<div class="entry">
  <div class="etitle">{title}</div>
  <div class="edesc">{desc}</div>
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
