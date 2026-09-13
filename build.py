#!/usr/bin/env python3
"""Galápagos public site — static build. No framework; Python 3.9+.
Reads:  content/*.md  proposals/*.md  log/*.md  data/board.json
Writes: docs/   (GitHub Pages: Settings → Pages → Deploy from branch → main /docs)
Usage:  python3 build.py
Frontmatter keys (proposals): title, slug (=filename), summary, price, price_note, cta_label,
  cta_url (mailto: or https), status (draft|live|closed), hypothesis (H-XXXX), contact, updated.
"""
import re, json, shutil, pathlib, html, datetime as dt
from zoneinfo import ZoneInfo
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "docs"
SITE = json.loads((ROOT / "site.json").read_text())
NOW = dt.datetime.now(ZoneInfo("America/Sao_Paulo"))

try:
    import markdown as _md
    def md(text): return rebase(_md.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "smarty", "attr_list"]))
except ImportError:                      # minimal fallback: paragraphs, headings, lists, links, emphasis
    def md(text):
        out, buf, inlist = [], [], False
        def inl(s):
            s = html.escape(s, quote=False)
            s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s); s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
            s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
            return re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
        def flush():
            nonlocal buf
            if buf: out.append("<p>" + inl(" ".join(buf)) + "</p>"); buf = []
        for line in text.splitlines():
            if m := re.match(r"^(#{1,3})\s+(.*)", line): flush(); out.append(f"<h{len(m[1])}>{inl(m[2])}</h{len(m[1])}>"); continue
            if m := re.match(r"^\s*[-*]\s+(.*)", line):
                flush()
                if not inlist: out.append("<ul>"); inlist = True
                out.append(f"<li>{inl(m[1])}</li>"); continue
            if inlist and line.strip() == "": out.append("</ul>"); inlist = False
            if line.strip() == "": flush()
            else: buf.append(line.strip())
        flush()
        if inlist: out.append("</ul>")
        return "\n".join(out)

def frontmatter(path):
    t = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", t, re.S)
    if not m: return {}, t
    fm = {}
    for line in m[1].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1); fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, m[2]

def page(title, body, path, desc="", current=""):
    nav = "".join(f'<a href="{SITE["base"]}{href}"{" aria-current=page" if key == current else ""}>{label}</a>'
                  for key, label, href in SITE["nav"])
    doc = f"""<!doctype html><html lang="{SITE['lang']}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title) if title == SITE['name'] else html.escape(title) + ' · ' + SITE['name']}</title>
<meta name="description" content="{html.escape(desc or SITE['tagline'])}">
<link rel="icon" href="{SITE['base']}/assets/beagle.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{SITE['base']}/static/style.css">
</head><body>
<header class="site-head"><div class="wrap">
<a class="brand" href="{SITE['base']}/"><img src="{SITE['base']}/assets/beagle.png" alt=""><span>{SITE['name']}<small>{SITE['tagline_short']}</small></span></a>
<nav class="main">{nav}</nav></div></header>
<main><div class="wrap">{body}</div></main>
<footer class="site-foot"><div class="wrap">
<span>{SITE['footer_left']}</span>
<span><a href="{SITE['base']}/about/#how-we-operate">{SITE['footer_disclosure']}</a> · <a href="mailto:{SITE['contact']}">{SITE['contact']}</a></span>
</div></footer></body></html>"""
    p = OUT / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(doc, encoding="utf-8")

def rebase(h): return h.replace('href="/', f'href="{SITE["base"]}/') if SITE["base"] else h
def disclosure_box(): return rebase(f'<div class="disclosure">{SITE["disclosure_html"]}</div>')

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(); (OUT / ".nojekyll").write_text("")
    if SITE.get("cname"): (OUT / "CNAME").write_text(SITE["cname"] + "\n")
    shutil.copytree(ROOT / "static", OUT / "static"); shutil.copytree(ROOT / "assets", OUT / "assets")

    # proposals
    props = []
    for f in sorted((ROOT / "proposals").glob("*.md")):
        fm, body = frontmatter(f)
        if fm.get("status", "draft") == "draft": continue
        slug = fm.get("slug") or f.stem; fm["slug"] = slug; props.append(fm)
        price = f'<div class="price">{html.escape(fm["price"])}<small>{html.escape(fm.get("price_note",""))}</small></div>' if fm.get("price") else ""
        cta = f'<p><a class="cta" href="{html.escape(fm["cta_url"])}">{html.escape(fm.get("cta_label","Get in touch"))}</a></p>' if fm.get("cta_url") else ""
        badge = f'<span class="badge {fm.get("status","")}">{fm.get("status","")}</span>'
        b = f"""<p class="eyebrow">Proposal {badge}</p><h1>{html.escape(fm['title'])}</h1>
<p class="lede">{html.escape(fm.get('summary',''))}</p>{price}{cta}
<p class="meta">Updated {html.escape(fm.get('updated',''))} · Questions: <a href="mailto:{html.escape(fm.get('contact', SITE['contact']))}">{html.escape(fm.get('contact', SITE['contact']))}</a></p>
{md(body)}{cta}{disclosure_box()}"""
        page(fm["title"], b, f"p/{slug}/index.html", fm.get("summary",""), "proposals")
    items = "".join(f'<li><a class="t" href="{SITE["base"]}/p/{p["slug"]}/">{html.escape(p["title"])}</a> <span class="badge {p.get("status","")}">{p.get("status","")}</span><div class="d">{html.escape(p.get("summary",""))}</div></li>' for p in props)
    page("Proposals", f'<p class="eyebrow">Proposals</p><h1>What Beagle is offering right now</h1><p class="lede">Each page below is a small, priced experiment. If one is useful to you, reply to the email or use the button on the page. If nobody wants it, it gets retired.</p><ul class="list">{items or "<li>Nothing live at the moment.</li>"}</ul>', "p/index.html", current="proposals")

    # log
    logs = []
    for f in sorted((ROOT / "log").glob("*.md"), reverse=True):
        fm, body = frontmatter(f); fm["slug"] = f.stem; fm["html"] = md(body); logs.append(fm)
        page(fm.get("title", f.stem), f'<p class="eyebrow">Log · {html.escape(fm.get("date", f.stem))}</p><h1>{html.escape(fm.get("title", f.stem))}</h1>{fm["html"]}<p class="meta"><a href="{SITE["base"]}/log/">← All entries</a></p>', f"log/{f.stem}/index.html", current="log")
    entries = "".join(f'<li><a class="t" href="{SITE["base"]}/log/{l["slug"]}/">{html.escape(l.get("title", l["slug"]))}</a><div class="d">{html.escape(l.get("date",""))} — {html.escape(l.get("summary",""))}</div></li>' for l in logs)
    page("Log", f'<p class="eyebrow">Log</p><h1>Field notes, in the open</h1><p class="lede">One entry per working day: what was born, what died, what we spent, what we learned.</p><ul class="list">{entries or "<li>No entries yet.</li>"}</ul>', "log/index.html", current="log")

    # board
    bd = json.loads((ROOT / "data/board.json").read_text()) if (ROOT / "data/board.json").exists() else {}
    c = bd.get("counts", {})
    stats = "".join(f'<div class="stat {k}"><b>{c.get(k,0)}</b><span>{k}</span></div>' for k in ("idea","screening","testing","alive","killed"))
    live = "".join(f'<li><span class="t">{html.escape(h["title"])}</span> <span class="badge {h["status"]}">{h["status"]}</span><div class="d">{html.escape(h.get("one_liner",""))}</div></li>' for h in bd.get("public", []))
    page("Board", f'<p class="eyebrow">Board · as of {html.escape(bd.get("as_of",""))}</p><h1>Natural selection, counted</h1><p class="lede">Every idea gets a number, a kill date and a kill condition. Most die. The board shows how many, and what is still standing.</p><div class="grid">{stats}</div><h2>In the water now</h2><ul class="list">{live or "<li>Nothing public yet.</li>"}</ul><p class="meta">Money in: ${bd.get("earned_usd",0):.2f} · Money out: ${bd.get("spent_usd",0):.2f} · Ideas born so far: {bd.get("total",0)}</p>', "board/index.html", current="board")

    # about + home
    fm, about = frontmatter(ROOT / "content/about.md")
    about_hero = f'<img class="about-hero" src="{SITE["base"]}/assets/beagle.png" alt="HMS Beagle, watercolor — the ship that names this expedition">'
    page("About", f'{about_hero}<p class="eyebrow">About</p>{md(about)}', "about/index.html", current="about")
    fm, home = frontmatter(ROOT / "content/home.md")
    latest = logs[0] if logs else None
    latest_html = f'<div class="card"><h3><a href="{SITE["base"]}/log/{latest["slug"]}/">{html.escape(latest.get("title",""))}</a></h3><p class="d">{html.escape(latest.get("summary",""))}</p></div>' if latest else ""
    page(SITE["name"], f'{md(home)}<div class="grid">{stats}</div><h2>Latest from the log</h2>{latest_html}<h2>Live proposals</h2><ul class="list">{items or "<li>Nothing live at the moment.</li>"}</ul>{disclosure_box()}', "index.html")
    (OUT / "build.txt").write_text(f"built {NOW:%Y-%m-%d %H:%M} BRT · {len(props)} proposals · {len(logs)} log entries\n")
    print((OUT / "build.txt").read_text().strip())

if __name__ == "__main__": build()
