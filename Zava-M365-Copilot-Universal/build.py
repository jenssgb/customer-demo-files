#!/usr/bin/env python3
"""Zava demo generator — single source (source/zava.yaml) -> HTML briefing + PromptPrompter MD.

Usage:
    python build.py

Outputs (never hand-edit these):
    Zava-M365-Copilot-Universal-Briefing.html
    Prompts/Zava-M365-Copilot-Universal-Demo.md
"""
from __future__ import annotations

import html
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Run:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "source" / "zava.yaml"
HTML_OUT = ROOT / "Zava-M365-Copilot-Universal-Briefing.html"
MD_OUT = ROOT / "Prompts" / "Zava-M365-Copilot-Universal-Demo.md"


def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def track_styles(tracks: list[dict]) -> str:
    rules = []
    for t in tracks:
        rules.append(f'[data-track="{t["id"]}"]{{--track:{t["color"]};}}')
    return "".join(rules)


def render_sources(sources: list[dict]) -> str:
    if not sources:
        return ""
    links = " · ".join(
        f'<a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["label"])}</a>'
        for s in sources
    )
    return f'<p class="sources">Sources: {links}</p>'


def render_step(step: dict) -> str:
    kind = step.get("kind", "prompt")
    title = esc(step.get("title", ""))
    text = step.get("text", "").rstrip("\n")
    if kind == "prompt":
        return (
            '<article class="step prompt">'
            '<div class="step-head">'
            f'<span class="step-kind">Prompt</span><h4>{title}</h4>'
            '<button class="copy" type="button">Copy</button>'
            "</div>"
            f"<pre>{esc(text)}</pre>"
            "</article>"
        )
    # action / presenter click-path — NO copy button, NO <pre>
    body = esc(text).replace("\n", "<br>")
    return (
        '<article class="step action">'
        '<div class="step-head">'
        f'<span class="step-kind">Presenter</span><h4>{title}</h4>'
        "</div>"
        f'<p class="action-body">{body}</p>'
        "</article>"
    )


_ICON_SPEC = {
    "xlsx": ("#217346", "X"), "xls": ("#217346", "X"), "csv": ("#217346", "X"),
    "docx": ("#2b579a", "W"), "doc": ("#2b579a", "W"),
    "pptx": ("#c43e1c", "P"), "ppt": ("#c43e1c", "P"),
    "pdf": ("#d83b01", "PDF"), "json": ("#5b6573", "{ }"),
}


def ext_of(name: str) -> str:
    n = name.strip().lower()
    for e in ("xlsx", "xls", "docx", "doc", "pptx", "ppt", "pdf", "json", "csv"):
        if n.endswith("." + e) or n == e:
            return e
    return ""


def file_icon_svg(name: str) -> str:
    """Inline SVG file-type icon (white page, folded corner, colored app band)."""
    color, letter = _ICON_SPEC.get(ext_of(name), ("#5b6573", "•"))
    fs = "5.2" if len(letter) <= 1 else "3.4"
    return (
        '<svg class="ficon" viewBox="0 0 20 20" width="20" height="20" aria-hidden="true">'
        '<path d="M4 1.4h7.2L16 6.2V17a1.4 1.4 0 0 1-1.4 1.4H4A1.4 1.4 0 0 1 2.6 17V2.8A1.4 1.4 0 0 1 4 1.4z" '
        'fill="#fff" stroke="#cfd4da" stroke-width=".7"/>'
        '<path d="M11.2 1.4 16 6.2h-4.8z" fill="#e4e8ed"/>'
        f'<rect x="2.6" y="11" width="13.4" height="6.4" rx="1.2" fill="{color}"/>'
        f'<text x="9.3" y="15.9" font-size="{fs}" font-weight="700" fill="#fff" '
        f'text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">{esc(letter)}</text>'
        "</svg>"
    )


def render_demo_view(demo: dict, prev_id, next_id) -> str:
    did = demo["id"]
    meta_bits = []
    if demo.get("duration"):
        meta_bits.append(f'<span class="meta-pill">⏱ {esc(demo["duration"])} min</span>')
    if demo.get("license"):
        meta_bits.append(f'<span class="meta-pill">⬢ {esc(demo["license"])}</span>')
    for s in demo.get("surfaces", []):
        meta_bits.append(f'<span class="meta-pill ghost">{esc(s)}</span>')
    files = demo.get("files") or []
    files_html = ""
    if files:
        tags = "".join(
            f'<span class="file-chip">{file_icon_svg(f)}<span>{esc(f)}</span></span>'
            for f in files
        )
        files_html = f'<div class="files"><span class="files-label">Files</span>{tags}</div>'
    note_html = f'<p class="demo-note">{esc(demo["note"])}</p>' if demo.get("note") else ""
    steps = "".join(render_step(s) for s in demo.get("steps", []))

    nav = '<div class="focus-nav">'
    if prev_id is not None:
        nav += f'<a class="fnav prev" href="#demo-{prev_id}">← Demo {prev_id}</a>'
    else:
        nav += "<span></span>"
    nav += '<a class="fnav home" href="#home">All demos</a>'
    if next_id is not None:
        nav += f'<a class="fnav next" href="#demo-{next_id}">Demo {next_id} →</a>'
    else:
        nav += "<span></span>"
    nav += "</div>"

    return (
        f'<section class="view demo-view" id="demo-{did}" data-track="{esc(demo["track"])}">'
        '<a class="back" href="#home">← Back to catalog</a>'
        f'<span class="view-eyebrow">Demo {did}</span>'
        f'<h2 class="view-title">{esc(demo["title"])}</h2>'
        f'<p class="view-summary">{esc(demo.get("summary",""))}</p>'
        f'<div class="meta-row">{"".join(meta_bits)}</div>'
        f"{files_html}{note_html}"
        f'<div class="steps">{steps}</div>'
        f"{render_sources(demo.get('sources', []))}"
        f"{nav}"
        "</section>"
    )


def render_catalog(data: dict) -> str:
    meta = data["meta"]
    tracks = data["tracks"]
    demos = data["demos"]

    stats = "".join(
        f'<div class="stat"><strong>{esc(s["value"])}</strong><span>{esc(s["label"])}</span></div>'
        for s in meta.get("stats", [])
    )

    # group demos by track, preserving track order
    cards_by_track = {t["id"]: [] for t in tracks}
    for d in demos:
        cards_by_track.setdefault(d["track"], []).append(d)

    groups = []
    for t in tracks:
        items = cards_by_track.get(t["id"], [])
        if not items:
            continue
        cards = ""
        for d in items:
            opt = '<span class="opt">optional</span>' if d.get("optional") else ""
            cards += (
                f'<a class="demo-card" href="#demo-{d["id"]}" data-track="{esc(d["track"])}" '
                f'data-search="{esc((d["title"] + " " + d.get("summary","")).lower())}">'
                f'<span class="num">{d["id"]:02d}</span>'
                f'<span class="dc-title">{esc(d["title"])}{opt}</span>'
                f'<span class="dc-summary">{esc(d.get("summary",""))}</span>'
                f'<span class="dc-foot">{esc(t["label"])} · {esc(d.get("license",""))}</span>'
                "</a>"
            )
        groups.append(
            f'<div class="track-group" data-track="{esc(t["id"])}">'
            f'<div class="tg-head"><span class="dot"></span><h3>{esc(t["label"])}</h3>'
            f'<p>{esc(t.get("desc",""))}</p></div>'
            f'<div class="card-grid">{cards}</div>'
            "</div>"
        )

    return (
        '<section class="view catalog" id="home">'
        '<div class="hero">'
        f'<span class="view-eyebrow">{esc(meta["customer"])} · live runbook</span>'
        f'<h1>{esc(meta["title"])}</h1>'
        f'<p class="hero-sub">{esc(meta["subtitle"])}</p>'
        f'<div class="hero-strip">{stats}</div>'
        "</div>"
        '<div class="filterbar"><div class="chips" id="chips"></div></div>'
        f'<div class="groups">{"".join(groups)}</div>'
        "</section>"
    )


def render_context_views(data: dict) -> str:
    ctx = data.get("context", {})
    out = []

    # Setup (with one-liner)
    setup = ctx.get("setup")
    if setup:
        roles = "".join(
            f'<div class="info-card"><h4>{esc(r["name"])}</h4><p>{esc(r["body"])}</p></div>'
            for r in setup.get("roles", [])
        )
        out.append(
            '<section class="view ctx-view" id="ctx-setup">'
            '<a class="back" href="#home">← Back to catalog</a>'
            '<span class="view-eyebrow">Setup</span>'
            f'<h2 class="view-title">{esc(setup["title"])}</h2>'
            '<article class="step prompt"><div class="step-head">'
            '<span class="step-kind">One-liner</span><h4>Copy demo files to the VM desktop</h4>'
            '<button class="copy" type="button">Copy</button></div>'
            f'<pre>{esc(data["meta"]["one_liner"])}</pre></article>'
            f'<div class="info-grid">{roles}</div>'
            "</section>"
        )

    # Demo files bundle
    bundle = data.get("bundle", [])
    if bundle:
        tags = "".join(
            f'<div class="file-tag">{file_icon_svg(b["icon"])}'
            f'<div><div class="file-name">{esc(b["name"])}</div>'
            f'<div class="file-dl">{esc(b["desc"])}</div></div></div>'
            for b in bundle
        )
        repo = data["meta"]["repo_url"]
        out.append(
            '<section class="view ctx-view" id="ctx-files">'
            '<a class="back" href="#home">← Back to catalog</a>'
            '<span class="view-eyebrow">Demo files</span>'
            '<h2 class="view-title">Full bundle &amp; one-liner</h2>'
            '<article class="step prompt"><div class="step-head">'
            '<span class="step-kind">One-liner</span><h4>PowerShell — copy the bundle to the desktop</h4>'
            '<button class="copy" type="button">Copy</button></div>'
            f'<pre>{esc(data["meta"]["one_liner"])}</pre></article>'
            f'<div class="file-tags">{tags}</div>'
            f'<p class="sources">Cloud source: <a href="{esc(repo)}" target="_blank" rel="noopener">customer-demo-files/{esc(data["meta"]["repo_folder"])}</a></p>'
            "</section>"
        )

    # Timing
    timing = ctx.get("timing")
    if timing:
        rows = "".join(
            f'<li><span class="when">{esc(r["when"])}</span>'
            f'<span><span class="what">{esc(r["what"])}</span><br>'
            f'<span class="muted">{esc(r["note"])}</span></span></li>'
            for r in timing.get("rows", [])
        )
        out.append(
            '<section class="view ctx-view" id="ctx-timing">'
            '<a class="back" href="#home">← Back to catalog</a>'
            '<span class="view-eyebrow">Timing</span>'
            f'<h2 class="view-title">{esc(timing["title"])}</h2>'
            f'<ul class="timing">{rows}</ul>'
            "</section>"
        )

    # Feature matrix + License map (shared card-grid renderer)
    for key, anchor, eyebrow in (
        ("feature_matrix", "ctx-features", "Microsoft Learn verified"),
        ("license_map", "ctx-license", "License & Frontier"),
    ):
        block = ctx.get(key)
        if not block:
            continue
        cards = "".join(
            f'<div class="info-card" data-track="{esc(c["track"])}">'
            f'<h4>{esc(c["h"])}</h4><p>{esc(c["p"])}</p></div>'
            for c in block.get("cards", [])
        )
        out.append(
            f'<section class="view ctx-view" id="{anchor}">'
            '<a class="back" href="#home">← Back to catalog</a>'
            f'<span class="view-eyebrow">{eyebrow}</span>'
            f'<h2 class="view-title">{esc(block["title"])}</h2>'
            f'<p class="view-summary">{esc(block.get("intro",""))}</p>'
            f'<div class="info-grid">{cards}</div>'
            f"{render_sources(block.get('sources', []))}"
            "</section>"
        )

    # Customer
    customer = ctx.get("customer")
    if customer:
        notes = "".join(f"<p>{esc(n)}</p>" for n in customer.get("notes", []))
        out.append(
            '<section class="view ctx-view" id="ctx-customer">'
            '<a class="back" href="#home">← Back to catalog</a>'
            '<span class="view-eyebrow">Customer briefing</span>'
            f'<h2 class="view-title">{esc(customer["title"])}</h2>'
            f'<p class="view-summary">{esc(customer.get("intro",""))}</p>'
            f'<div class="prose">{notes}</div>'
            f"{render_sources(customer.get('sources', []))}"
            "</section>"
        )

    # Q&A
    qa = ctx.get("qa")
    if qa:
        items = "".join(
            f'<div class="info-card"><h4>{esc(i["q"])}</h4><p>{esc(i["a"])}</p></div>'
            for i in qa.get("items", [])
        )
        out.append(
            '<section class="view ctx-view" id="ctx-qa">'
            '<a class="back" href="#home">← Back to catalog</a>'
            '<span class="view-eyebrow">Likely questions</span>'
            f'<h2 class="view-title">{esc(qa["title"])}</h2>'
            f'<div class="info-grid">{items}</div>'
            "</section>"
        )

    return "".join(out)


def render_sidebar(data: dict) -> str:
    meta = data["meta"]
    tracks = data["tracks"]
    demos = data["demos"]
    cards_by_track = {t["id"]: [] for t in tracks}
    for d in demos:
        cards_by_track.setdefault(d["track"], []).append(d)

    nav = ""
    for t in tracks:
        items = cards_by_track.get(t["id"], [])
        if not items:
            continue
        links = "".join(
            f'<a class="nl" href="#demo-{d["id"]}" data-track="{esc(d["track"])}" '
            f'data-search="{esc(d["title"].lower())}">'
            f'<span class="nl-num">{d["id"]:02d}</span>{esc(d["title"])}</a>'
            for d in items
        )
        nav += (
            f'<div class="nav-group" data-track="{esc(t["id"])}">'
            f'<span class="nav-label"><span class="dot"></span>{esc(t["label"])}</span>'
            f"{links}</div>"
        )

    ctx_links = (
        '<div class="nav-group reference">'
        '<span class="nav-label">Reference</span>'
        '<a class="nl" href="#ctx-setup" data-search="setup">⚡ Setup &amp; one-liner</a>'
        '<a class="nl" href="#ctx-files" data-search="demo files">📦 Demo files</a>'
        '<a class="nl" href="#ctx-timing" data-search="timing">⏱ Timing</a>'
        '<a class="nl" href="#ctx-features" data-search="feature matrix">✅ Feature matrix</a>'
        '<a class="nl" href="#ctx-license" data-search="license frontier">⬢ License &amp; Frontier</a>'
        '<a class="nl" href="#ctx-customer" data-search="customer">👥 Customer briefing</a>'
        '<a class="nl" href="#ctx-qa" data-search="questions">💬 Q&amp;A</a>'
        "</div>"
    )

    return (
        "<aside>"
        '<div class="brand">'
        f'<a class="brand-name" href="#home">{esc(meta["customer"])} runbook</a>'
        f'<span class="version-badge">v{esc(meta["version"])} · {esc(meta["date"])}</span>'
        "</div>"
        '<input id="search" class="search" type="search" placeholder="Search demos…" autocomplete="off">'
        f'<nav>{nav}{ctx_links}</nav>'
        '<button id="theme" class="theme-toggle" type="button">🌓 Theme</button>'
        "</aside>"
    )


CSS = r"""
*{box-sizing:border-box}
:root{
  --bg:#eef1f5;--surface:#ffffff;--surface-2:#f6f8fb;--text:#1a1d21;--muted:#5b6573;
  --border:#e1e6ec;--shadow:0 1px 2px rgba(16,24,40,.06),0 8px 24px rgba(16,24,40,.06);
  --accent:#b11f4b;--accent-soft:rgba(177,31,75,.10);--radius:14px;
  --chat:#0078d4;--analysis:#107c10;--apps:#2563eb;--agents:#5c2d91;--governance:#d83b01;--collab:#6264a7;
}
[data-theme="dark"]{
  --bg:#17181c;--surface:#202228;--surface-2:#262932;--text:#eef0f3;--muted:#9aa3b0;
  --border:#2f333c;--shadow:0 1px 2px rgba(0,0,0,.3),0 12px 30px rgba(0,0,0,.35);
  --accent:#ff5d86;--accent-soft:rgba(255,93,134,.14);
}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);
  font-family:"Segoe UI Variable","Segoe UI",system-ui,-apple-system,sans-serif;
  font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.shell{display:grid;grid-template-columns:288px 1fr;min-height:100vh}

/* Sidebar */
aside{position:sticky;top:0;align-self:start;height:100vh;overflow-y:auto;
  background:var(--surface);border-right:1px solid var(--border);padding:22px 16px;
  display:flex;flex-direction:column;gap:14px}
.brand{display:flex;flex-direction:column;gap:6px}
.brand-name{font-weight:700;font-size:17px;color:var(--text)}
.brand-name:hover{text-decoration:none;color:var(--accent)}
.version-badge{font-size:11px;color:var(--muted);background:var(--surface-2);
  border:1px solid var(--border);border-radius:999px;padding:3px 9px;width:fit-content}
.search{width:100%;padding:9px 12px;border-radius:10px;border:1px solid var(--border);
  background:var(--surface-2);color:var(--text);font-size:13px}
.search:focus{outline:2px solid var(--accent-soft);border-color:var(--accent)}
nav{display:flex;flex-direction:column;gap:16px;flex:1}
.nav-group{display:flex;flex-direction:column;gap:2px}
.nav-label{font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:var(--muted);
  font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:7px}
.dot{width:8px;height:8px;border-radius:50%;background:var(--track,var(--accent))}
.nav-group[data-track="chat"]{--track:var(--chat)}
.nav-group[data-track="analysis"]{--track:var(--analysis)}
.nav-group[data-track="apps"]{--track:var(--apps)}
.nav-group[data-track="agents"]{--track:var(--agents)}
.nav-group[data-track="governance"]{--track:var(--governance)}
.nav-group[data-track="collab"]{--track:var(--collab)}
.nl{display:flex;align-items:center;gap:9px;padding:6px 9px;border-radius:8px;color:var(--text);
  font-size:13px;border-left:2px solid transparent}
.nl:hover{background:var(--surface-2);text-decoration:none}
.nl.active{background:var(--accent-soft);border-left-color:var(--track,var(--accent));font-weight:600}
.nl-num{font-size:11px;font-weight:700;color:var(--muted);min-width:18px}
.reference .nl{font-size:13px}
.theme-toggle{margin-top:auto;padding:8px;border-radius:9px;border:1px solid var(--border);
  background:var(--surface-2);color:var(--text);font-size:13px;cursor:pointer}
.theme-toggle:hover{border-color:var(--accent)}

/* Main */
main{padding:34px clamp(20px,4vw,56px);max-width:1180px;width:100%}
.view{display:none;animation:fade .25s ease}
.view.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.view-eyebrow{display:inline-block;font-size:11px;text-transform:uppercase;letter-spacing:1px;
  font-weight:700;color:var(--accent);margin-bottom:8px}
.view-title{font-size:27px;font-weight:700;margin:0 0 8px;letter-spacing:-.3px}
.view-summary{color:var(--muted);font-size:16px;margin:0 0 20px;max-width:70ch}
.back{display:inline-block;font-size:13px;color:var(--muted);margin-bottom:14px}

/* Catalog hero */
.hero{margin-bottom:26px}
.hero h1{font-size:32px;line-height:1.15;margin:0 0 12px;letter-spacing:-.6px;max-width:18ch}
.hero-sub{color:var(--muted);font-size:16px;max-width:75ch;margin:0 0 20px}
.hero-strip{display:flex;flex-wrap:wrap;gap:12px}
.stat{background:var(--surface);border:1px solid var(--border);border-radius:12px;
  padding:12px 18px;box-shadow:var(--shadow);min-width:120px}
.stat strong{display:block;font-size:22px;font-weight:700}
.stat span{font-size:12px;color:var(--muted)}

/* Filter chips */
.filterbar{margin:0 0 22px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{padding:6px 13px;border-radius:999px;border:1px solid var(--border);background:var(--surface);
  font-size:12.5px;font-weight:600;cursor:pointer;color:var(--muted);display:flex;align-items:center;gap:7px}
.chip .dot{background:var(--c,var(--accent))}
.chip.active{color:#fff;background:var(--c,var(--accent));border-color:transparent}
.chip.active .dot{background:rgba(255,255,255,.9)}

/* Track groups + cards */
.track-group{margin-bottom:30px}
.track-group[data-track="chat"]{--track:var(--chat)}
.track-group[data-track="analysis"]{--track:var(--analysis)}
.track-group[data-track="apps"]{--track:var(--apps)}
.track-group[data-track="agents"]{--track:var(--agents)}
.track-group[data-track="governance"]{--track:var(--governance)}
.track-group[data-track="collab"]{--track:var(--collab)}
.tg-head{margin-bottom:12px}
.tg-head h3{display:inline-flex;align-items:center;gap:9px;font-size:16px;margin:0}
.tg-head .dot{background:var(--track)}
.tg-head p{margin:3px 0 0 17px;color:var(--muted);font-size:13.5px}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}
.demo-card{display:flex;flex-direction:column;gap:7px;padding:16px;border-radius:var(--radius);
  background:var(--surface);border:1px solid var(--border);border-top:3px solid var(--track,var(--accent));
  box-shadow:var(--shadow);color:var(--text);transition:transform .12s,box-shadow .12s}
.demo-card:hover{transform:translateY(-3px);text-decoration:none;
  box-shadow:0 6px 14px rgba(16,24,40,.10),0 18px 40px rgba(16,24,40,.10)}
.demo-card .num{font-size:12px;font-weight:800;color:var(--track,var(--accent));letter-spacing:1px}
.dc-title{font-size:15.5px;font-weight:700;line-height:1.3}
.dc-summary{font-size:13px;color:var(--muted);flex:1}
.dc-foot{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.4px;
  border-top:1px solid var(--border);padding-top:8px}
.opt{font-size:10px;font-weight:700;color:var(--collab);background:var(--surface-2);
  border-radius:6px;padding:1px 6px;margin-left:6px;text-transform:uppercase;letter-spacing:.4px}

/* Focus demo view */
.demo-view[data-track="chat"]{--track:var(--chat)}
.demo-view[data-track="analysis"]{--track:var(--analysis)}
.demo-view[data-track="apps"]{--track:var(--apps)}
.demo-view[data-track="agents"]{--track:var(--agents)}
.demo-view[data-track="governance"]{--track:var(--governance)}
.demo-view[data-track="collab"]{--track:var(--collab)}
.demo-view .view-eyebrow{color:var(--track)}
.meta-row{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.meta-pill{font-size:12px;font-weight:600;padding:4px 11px;border-radius:999px;
  background:var(--track,var(--accent));color:#fff}
.meta-pill.ghost{background:var(--surface-2);color:var(--muted);border:1px solid var(--border)}
.files{display:flex;flex-wrap:wrap;align-items:center;gap:7px;margin-bottom:16px}
.files-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--muted)}
.file-chip{display:inline-flex;align-items:center;gap:6px;font-size:12px;background:var(--surface-2);
  border:1px solid var(--border);border-radius:7px;padding:3px 9px 3px 6px;color:var(--text)}
.file-chip .ficon{width:16px;height:16px;flex:none}
.demo-note{background:var(--accent-soft);border-left:3px solid var(--track,var(--accent));
  padding:11px 15px;border-radius:0 9px 9px 0;font-size:14px;margin:0 0 20px}
.steps{display:flex;flex-direction:column;gap:14px;margin-bottom:22px}
.step{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  box-shadow:var(--shadow);overflow:hidden}
.step.prompt{border-left:3px solid var(--track,var(--accent))}
.step.action{border-left:3px solid var(--governance);background:var(--surface-2)}
.step-head{display:flex;align-items:center;gap:10px;padding:13px 16px}
.step-kind{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.7px;
  padding:3px 8px;border-radius:6px;background:var(--track,var(--accent));color:#fff}
.step.action .step-kind{background:var(--governance)}
.step-head h4{margin:0;font-size:14.5px;font-weight:700;flex:1}
.copy{font-size:12px;font-weight:600;padding:5px 13px;border-radius:8px;border:1px solid var(--border);
  background:var(--surface);color:var(--text);cursor:pointer}
.copy:hover{border-color:var(--accent);color:var(--accent)}
.copy.done{background:var(--analysis);color:#fff;border-color:transparent}
pre{margin:0;padding:14px 16px;background:var(--surface-2);border-top:1px solid var(--border);
  font-family:"Cascadia Code",Consolas,monospace;font-size:13px;line-height:1.55;
  white-space:pre-wrap;word-break:break-word;color:var(--text)}
.action-body{margin:0;padding:0 16px 15px;font-size:14px;color:var(--text)}
.sources{font-size:12.5px;color:var(--muted);margin:18px 0 0}
.focus-nav{display:flex;justify-content:space-between;align-items:center;gap:10px;
  margin-top:26px;padding-top:18px;border-top:1px solid var(--border)}
.fnav{font-size:13px;font-weight:600;padding:8px 14px;border-radius:9px;background:var(--surface);
  border:1px solid var(--border);color:var(--text)}
.fnav:hover{border-color:var(--accent);text-decoration:none}
.fnav.home{color:var(--muted)}

/* Context / info grids */
.info-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;margin-bottom:18px}
.info-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:15px 17px;box-shadow:var(--shadow);border-top:3px solid var(--track,var(--accent))}
.info-card h4{margin:0 0 6px;font-size:14.5px}
.info-card p{margin:0;font-size:13.5px;color:var(--muted)}
.info-card[data-track="chat"]{--track:var(--chat)}
.info-card[data-track="analysis"]{--track:var(--analysis)}
.info-card[data-track="apps"]{--track:var(--apps)}
.info-card[data-track="agents"]{--track:var(--agents)}
.info-card[data-track="governance"]{--track:var(--governance)}
.info-card[data-track="collab"]{--track:var(--collab)}
.prose p{margin:0 0 12px;max-width:75ch}
.timing{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:2px}
.timing li{display:flex;gap:16px;padding:12px 14px;background:var(--surface);border:1px solid var(--border);
  border-radius:10px;margin-bottom:8px;box-shadow:var(--shadow)}
.when{font-weight:800;color:var(--accent);min-width:54px;font-family:"Cascadia Code",Consolas,monospace}
.what{font-weight:700}.muted{color:var(--muted);font-size:13.5px}
.file-tags{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin-bottom:16px}
.file-tag{display:flex;gap:12px;align-items:flex-start;background:var(--surface);border:1px solid var(--border);
  border-radius:12px;padding:13px 15px;box-shadow:var(--shadow)}
.file-tag .ficon{width:30px;height:30px;flex:none}
.file-name{font-weight:700;font-size:13.5px}.file-dl{font-size:12.5px;color:var(--muted)}

@media(max-width:860px){
  .shell{grid-template-columns:1fr}
  aside{position:static;height:auto;border-right:none;border-bottom:1px solid var(--border)}
  main{padding:24px 18px}
}
"""

JS = r"""
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const tcolors={chat:'#0078d4',analysis:'#107c10',apps:'#2563eb',agents:'#5c2d91',governance:'#d83b01',collab:'#6264a7'};

// theme
const root=document.documentElement;
const saved=localStorage.getItem('zava-theme');
if(saved)root.setAttribute('data-theme',saved);
else if(matchMedia('(prefers-color-scheme:dark)').matches)root.setAttribute('data-theme','dark');
$('#theme').onclick=()=>{const d=root.getAttribute('data-theme')==='dark'?'light':'dark';
  root.setAttribute('data-theme',d);localStorage.setItem('zava-theme',d);};

// router
function show(hash){
  if(!hash||hash==='#')hash='#home';
  const id=hash.slice(1);
  const target=document.getElementById(id)||$('#home');
  $$('.view').forEach(v=>v.classList.toggle('active',v===target));
  $$('.nl').forEach(n=>n.classList.toggle('active',n.getAttribute('href')===hash));
  window.scrollTo({top:0,behavior:'instant'});
}
window.addEventListener('hashchange',()=>show(location.hash));
show(location.hash);

// copy
$$('.copy').forEach(b=>b.onclick=async()=>{
  const pre=b.closest('.step').querySelector('pre');if(!pre)return;
  await navigator.clipboard.writeText(pre.textContent);
  const t=b.textContent;b.textContent='Copied';b.classList.add('done');
  setTimeout(()=>{b.textContent=t;b.classList.remove('done');},1200);
});

// search filters catalog cards + nav
$('#search').addEventListener('input',e=>{
  const q=e.target.value.trim().toLowerCase();
  $$('.demo-card').forEach(c=>{c.style.display=(!q||c.dataset.search.includes(q))?'':'none';});
  $$('.nl').forEach(n=>{const s=n.dataset.search||'';n.style.display=(!q||s.includes(q))?'':'none';});
  $$('.track-group').forEach(g=>{
    const any=[...g.querySelectorAll('.demo-card')].some(c=>c.style.display!=='none');
    g.style.display=any?'':'none';});
});

// track filter chips
const chips=$('#chips');
chips.innerHTML='<button class="chip active" data-track="all">All tracks</button>'+
  Object.entries(tcolors).map(([id,c])=>{
    const lbl=({chat:'Context',analysis:'Analysis',apps:'Apps',agents:'Agents',governance:'Governance',collab:'Collab'})[id];
    return `<button class="chip" data-track="${id}" style="--c:${c}"><span class="dot"></span>${lbl}</button>`;
  }).join('');
chips.addEventListener('click',e=>{
  const b=e.target.closest('.chip');if(!b)return;
  $$('.chip').forEach(c=>c.classList.toggle('active',c===b));
  const t=b.dataset.track;
  $$('.demo-card').forEach(c=>{c.style.display=(t==='all'||c.dataset.track===t)?'':'none';});
  $$('.track-group').forEach(g=>{g.style.display=(t==='all'||g.dataset.track===t)?'':'none';});
});
"""


def render_html(data: dict) -> str:
    meta = data["meta"]
    sidebar = render_sidebar(data)
    catalog = render_catalog(data)
    demos = data["demos"]
    demo_views = ""
    for i, d in enumerate(demos):
        prev_id = demos[i - 1]["id"] if i > 0 else None
        next_id = demos[i + 1]["id"] if i < len(demos) - 1 else None
        demo_views += render_demo_view(d, prev_id, next_id)
    ctx_views = render_context_views(data)
    extra_track_css = track_styles(data["tracks"])
    return (
        "<!DOCTYPE html>\n"
        f"<!-- GENERATED by build.py from source/zava.yaml — do not hand-edit. v{meta['version']} · {meta['date']} -->\n"
        '<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{esc(meta['customer'])} — Copilot demo runbook</title>"
        f"<style>{CSS}{extra_track_css}</style></head><body>"
        f'<div class="shell">{sidebar}<main>{catalog}{demo_views}{ctx_views}</main></div>'
        f"<script>{JS}</script></body></html>"
    )


# ---------------------------------------------------------------------------
# Markdown (PromptPrompter) rendering
# ---------------------------------------------------------------------------

def render_md(data: dict) -> str:
    lines = [f"# {data['meta']['customer']} Top Microsoft 365 Copilot Demo", ""]
    for d in data["demos"]:
        lines.append(f"## {d['id']} - {d['title']}")
        lines.append("")
        if d.get("note"):
            lines.append(f"> {d['note']}")
            lines.append("")
        for s in d.get("steps", []):
            fence = "prompt" if s.get("kind") == "prompt" else "demo"
            lines.append(f"### {s.get('title','')}")
            lines.append("")
            lines.append(f"```{fence}")
            lines.append(s.get("text", "").rstrip("\n"))
            lines.append("```")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    HTML_OUT.write_text(render_html(data), encoding="utf-8")
    MD_OUT.parent.mkdir(parents=True, exist_ok=True)
    MD_OUT.write_text(render_md(data), encoding="utf-8")
    print(f"OK  {len(data['demos'])} demos")
    print(f"    -> {HTML_OUT.name} ({HTML_OUT.stat().st_size:,} bytes)")
    print(f"    -> {MD_OUT.relative_to(ROOT)} ({MD_OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
