#!/usr/bin/env python3
"""Exporta data/board.json a partir do repo PRIVADO do Galápagos, só com o que pode ser público.
Uso: python3 tools/export_board.py /caminho/do/repo/galapagos
Publica: contagens por status, total, ledger somado, e (título + uma frase) só das hipóteses em testing/alive/scaling."""
import sys, re, csv, json, pathlib, datetime as dt
from zoneinfo import ZoneInfo
repo = pathlib.Path(sys.argv[1]).expanduser(); out = pathlib.Path(__file__).resolve().parent.parent / "data/board.json"
def fm(p):
    t = p.read_text(encoding="utf-8", errors="replace"); m = re.match(r"^---\n(.*?)\n---", t, re.S); d = {}
    if m:
        for l in m[1].splitlines():
            if ":" in l and not l.startswith(" "): k, v = l.split(":", 1); d[k.strip()] = v.strip()
    f = re.search(r"## Em uma frase\n+(.+)", t); d["_frase"] = (f[1].strip() if f else "")
    return d
H = [fm(p) for p in sorted((repo / "hypotheses").glob("H-*.md"))]
counts = {}
for h in H: counts[h.get("status", "?")] = counts.get(h.get("status", "?"), 0) + 1
rows = list(csv.DictReader((repo / "ledger/ledger.csv").open())) if (repo / "ledger/ledger.csv").exists() else []
s = lambda d: sum(float(r["amount_usd"] or 0) for r in rows if r["direction"] == d)
pub = [{"id": h["id"], "title": h.get("title", ""), "status": h["status"], "one_liner": h["_frase"][:180]} for h in H if h.get("status") in ("testing", "alive", "scaling")]
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"as_of": dt.datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%Y-%m-%d %H:%M BRT"), "counts": counts, "total": len(H), "earned_usd": s("in"), "spent_usd": s("out"), "public": pub}, ensure_ascii=False, indent=1))
print(out, counts, len(pub), "públicas")
