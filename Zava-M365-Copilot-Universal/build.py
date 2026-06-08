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
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Run:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "source" / "zava.yaml"
HTML_OUT = ROOT / "Zava-M365-Copilot-Universal-Briefing.html"
MD_OUT = ROOT / "Prompts" / "Zava-M365-Copilot-Universal-Demo.md"


def cet_today() -> str:
    """Today's date in Europe/Berlin (CET/CEST), falling back to local time."""
    try:
        from zoneinfo import ZoneInfo

        return datetime.now(ZoneInfo("Europe/Berlin")).strftime("%Y-%m-%d")
    except Exception:
        return datetime.now().strftime("%Y-%m-%d")


def stamp_version_and_date() -> str:
    """Auto-bump meta.version patch segment and set meta.date to today (CET).

    Edits source/zava.yaml in place with a targeted regex so comments and
    formatting are preserved. Returns the new version string.
    """
    text = SRC.read_text(encoding="utf-8")
    new_version = {"v": ""}

    def _bump(m: re.Match) -> str:
        parts = (m.group(2).split(".") + ["0", "0"])[:3]
        try:
            parts[2] = str(int(parts[2]) + 1)
        except ValueError:
            parts[2] = "1"
        new_version["v"] = ".".join(parts)
        return f'{m.group(1)}{new_version["v"]}{m.group(3)}'

    text = re.sub(r'(\bversion:\s*")([^"]+)(")', _bump, text, count=1)
    text = re.sub(r'(\bdate:\s*")[^"]+(")', rf"\g<1>{cet_today()}\g<2>", text, count=1)
    SRC.write_text(text, encoding="utf-8")
    return new_version["v"]



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
    if kind == "clickpath":
        return render_clickpath(step, title)
    # action / presenter narration — NO copy button, NO <pre>
    body = esc(text).replace("\n", "<br>")
    return (
        '<article class="step action">'
        '<div class="step-head">'
        f'<span class="step-kind">Presenter</span><h4>{title}</h4>'
        "</div>"
        f'<p class="action-body">{body}</p>'
        "</article>"
    )


def render_clickpath(step: dict, title: str) -> str:
    """Render a portal navigation as a bold, followable visual walkthrough.

    YAML fields (all optional except steps):
        portal:  name of the portal (shown as a pill)
        url:     deep link opened by the "Open portal" button
        path:    list of breadcrumb crumbs after the portal
        scenario: framing/setup callout (what just happened)
        steps:   ordered list of concrete actions (the click-path)
        watch:   "on screen" outcome callout (what the audience sees)
        say:     presenter narration callout
    """
    portal = step.get("portal", "")
    url = step.get("url", "")
    crumbs = step.get("path", []) or []
    scenario = step.get("scenario", "")
    steps = step.get("steps", []) or []
    watch = step.get("watch", "")
    say = step.get("say", "")

    head_right = ""
    if url:
        label = esc(portal) if portal else "Open portal"
        head_right = (
            f'<a class="portal-link" href="{esc(url)}" target="_blank" rel="noopener">'
            f"{label} ↗</a>"
        )

    breadcrumb = ""
    crumb_items = ([portal] if portal else []) + list(crumbs)
    if crumb_items:
        chips = '<span class="cp-sep">›</span>'.join(
            f'<span class="cp-crumb{" start" if i == 0 and portal else ""}">{esc(c)}</span>'
            for i, c in enumerate(crumb_items)
        )
        breadcrumb = f'<div class="cp-breadcrumb">{chips}</div>'

    scenario_html = (
        f'<div class="cp-callout cp-scenario"><span class="cp-tag">Scenario</span>'
        f"<p>{esc(scenario)}</p></div>" if scenario else ""
    )
    steps_html = ""
    if steps:
        items = "".join(f"<li>{esc(s)}</li>" for s in steps)
        steps_html = f'<ol class="cp-steps">{items}</ol>'
    watch_html = (
        f'<div class="cp-callout cp-watch"><span class="cp-tag">On screen</span>'
        f"<p>{esc(watch)}</p></div>" if watch else ""
    )
    say_html = (
        f'<div class="cp-callout cp-say"><span class="cp-tag">Say</span>'
        f"<p>{esc(say)}</p></div>" if say else ""
    )

    return (
        '<article class="step clickpath">'
        '<div class="step-head">'
        f'<span class="step-kind">Click-path</span><h4>{title}</h4>'
        f"{head_right}"
        "</div>"
        '<div class="cp-body">'
        f"{scenario_html}{breadcrumb}{steps_html}{watch_html}{say_html}"
        "</div>"
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
        meta_bits.append(f'<span class="m-strong">{esc(demo["duration"])} min</span>')
    if demo.get("license"):
        meta_bits.append(f'<span class="m-strong">{esc(demo["license"])}</span>')
    surfaces = demo.get("surfaces", [])
    if surfaces:
        meta_bits.append(f'<span>{esc(", ".join(surfaces))}</span>')
    meta_html = ('<div class="meta-line">'
                 + '<span class="sep">·</span>'.join(meta_bits)
                 + "</div>") if meta_bits else ""
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
        f'{meta_html}'
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

    # Baseline vs Agent 365 — grouped comparison TABLE with two filter axes
    gov = ctx.get("agent_governance")
    if gov:
        def _gov_cell(txt: str) -> str:
            t = str(txt).strip()
            for glyph, cls in (("\u2713", "yes"), ("\u2717", "no"), ("~", "part"), ("\u2014", "part")):
                if t.startswith(glyph):
                    return f'<span class="{cls}">{glyph}</span> {esc(t[len(glyph):].lstrip())}'
            return esc(t)

        cols = gov.get("columns", [])
        ncols = len(cols)
        head = "".join(f"<th>{esc(c)}</th>" for c in cols)
        body = ""
        for gi, group in enumerate(gov.get("groups", []), start=1):
            body += (
                f'<tr class="cmp-group" data-group="{gi}">'
                f'<th colspan="{ncols}">'
                f'<span class="cmp-gnum">{gi:02d}</span>{esc(group["label"])}'
                "</th></tr>"
            )
            for row in group.get("rows", []):
                types = set(row.get("types", []))
                is_all = bool(row.get("all"))
                if is_all:
                    types |= {"builder", "studio", "foundry", "external"}
                dt = " ".join(sorted(types))
                da = ' data-all="1"' if is_all else ""
                planes = " ".join(sorted(set(row.get("planes", []))))
                rh = f'<th scope="row">{esc(row["cap"])}</th>'
                applies = f'<td class="applies">{esc(row.get("applies", ""))}</td>'
                cells = (
                    f'<td>{_gov_cell(row.get("baseline", ""))}</td>'
                    f'<td>{_gov_cell(row.get("agent365", ""))}</td>'
                )
                body += (
                    f'<tr data-group="{gi}" data-types="{dt}"{da} '
                    f'data-planes="{planes}">{rh}{applies}{cells}</tr>'
                )
        note = f'<p class="gov-note">{esc(gov["note"])}</p>' if gov.get("note") else ""
        type_filter = (
            '<div class="gov-filter"><span class="gov-filter-lbl">Filter by agent type</span>'
            '<div class="chips gov-chips" id="gov-chips">'
            '<button class="chip active" data-gtype="all">All agent types</button>'
            '<button class="chip" data-gtype="builder" style="--c:#5c2d91"><span class="dot"></span>Agent Builder</button>'
            '<button class="chip" data-gtype="studio" style="--c:#2563eb"><span class="dot"></span>Copilot Studio</button>'
            '<button class="chip" data-gtype="foundry" style="--c:#107c10"><span class="dot"></span>Foundry</button>'
            '<button class="chip" data-gtype="external" style="--c:#d83b01"><span class="dot"></span>3rd-party</button>'
            '<button class="chip" data-gtype="firstparty" style="--c:#0078d4"><span class="dot"></span>First-party (Researcher/Analyst)</button>'
            "</div></div>"
        )
        plane_filter = (
            '<div class="gov-filter"><span class="gov-filter-lbl">Filter by what you need</span>'
            '<div class="chips gov-chips" id="gov-planes">'
            '<button class="chip active" data-plane="all">Any plane</button>'
            '<button class="chip" data-plane="baseline" style="--c:#107c10"><span class="dot"></span>Baseline · admin role only</button>'
            '<button class="chip" data-plane="agent365" style="--c:#d83b01"><span class="dot"></span>Microsoft Agent 365 · E7</button>'
            '<button class="chip" data-plane="powerplatform" style="--c:#2563eb"><span class="dot"></span>Power Platform admin center</button>'
            '<button class="chip" data-plane="entra" style="--c:#5c2d91"><span class="dot"></span>Entra ID P1·P2</button>'
            '</div><p class="gov-filter-hint" id="gov-filter-hint"></p></div>'
        )
        out.append(
            '<section class="view ctx-view" id="ctx-governance">'
            '<a class="back" href="#home">← Back to catalog</a>'
            '<span class="view-eyebrow">Baseline vs Agent 365</span>'
            f'<h2 class="view-title">{esc(gov["title"])}</h2>'
            f'<p class="view-summary">{esc(gov.get("intro",""))}</p>'
            f'<div class="gov-filters">{type_filter}{plane_filter}</div>'
            f'<div class="cmp-wrap"><table class="cmp cmp-gov"><thead><tr>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table></div>'
            f'{note}'
            f"{render_sources(gov.get('sources', []))}"
            "</section>"
        )

    # PPAC vs Agent 365 — standalone objection-handling TABLE
    pac = ctx.get("pac_governance")
    if pac:
        def _pac_cell(txt: str) -> str:
            t = str(txt).strip()
            for glyph, cls in (("\u2713", "yes"), ("\u2717", "no"), ("~", "part"), ("\u2014", "part")):
                if t.startswith(glyph):
                    return f'<span class="{cls}">{glyph}</span> {esc(t[len(glyph):].lstrip())}'
            return esc(t)

        phead = "".join(f"<th>{esc(c)}</th>" for c in pac["columns"])
        prows = ""
        for row in pac.get("rows", []):
            q, ppac, a365 = row[0], row[1], row[2]
            prows += (
                "<tr>"
                f'<th scope="row">{esc(q)}</th>'
                f"<td>{_pac_cell(ppac)}</td>"
                f'<td class="pac-add">{_pac_cell(a365)}</td>'
                "</tr>"
            )
        pverdict = (
            f'<div class="pac-verdict"><span class="pac-verdict-tag">Bottom line</span>'
            f'<p>{esc(pac["verdict"])}</p></div>'
            if pac.get("verdict")
            else ""
        )
        pnote = (
            f'<div class="gov-note">{esc(pac["note"])}</div>' if pac.get("note") else ""
        )
        out.append(
            '<section class="view ctx-view" id="ctx-pac">'
            '<a class="back" href="#home">← Back to catalog</a>'
            '<span class="view-eyebrow">PPAC vs Agent 365</span>'
            f'<h2 class="view-title">{esc(pac["title"])}</h2>'
            f'<p class="view-summary">{esc(pac.get("intro",""))}</p>'
            f"{pverdict}"
            f'<div class="cmp-wrap"><table class="cmp pac-cmp"><thead><tr>{phead}</tr></thead>'
            f"<tbody>{prows}</tbody></table></div>"
            f"{pnote}"
            f"{render_sources(pac.get('sources', []))}"
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
        '<a class="nl" href="#ctx-governance" data-search="baseline agent 365 admin center registry governance difference">🛡 Baseline vs Agent 365</a>'
        '<a class="nl" href="#ctx-pac" data-search="ppac power platform admin center agent 365 why need objection complementary build plane tenant">🔀 PPAC vs Agent 365</a>'
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
  border:1px solid var(--border);border-radius:5px;padding:3px 8px;width:fit-content;
  text-transform:uppercase;letter-spacing:.5px;font-weight:600}
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
.chip{padding:6px 12px;border-radius:6px;border:1px solid var(--border);background:var(--surface);
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
  border:1px solid var(--border);border-radius:4px;padding:1px 6px;margin-left:6px;
  text-transform:uppercase;letter-spacing:.4px}

/* Focus demo view */
.demo-view[data-track="chat"]{--track:var(--chat)}
.demo-view[data-track="analysis"]{--track:var(--analysis)}
.demo-view[data-track="apps"]{--track:var(--apps)}
.demo-view[data-track="agents"]{--track:var(--agents)}
.demo-view[data-track="governance"]{--track:var(--governance)}
.demo-view[data-track="collab"]{--track:var(--collab)}
.demo-view .view-eyebrow{color:var(--track)}
.meta-line{display:flex;flex-wrap:wrap;align-items:center;gap:9px;margin-bottom:16px;
  font-size:13.5px;color:var(--muted)}
.meta-line .m-strong{color:var(--text);font-weight:600}
.meta-line .sep{color:var(--border);font-weight:700}
.files{display:flex;flex-wrap:wrap;align-items:center;gap:7px;margin-bottom:16px}
.files-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--muted)}
.file-chip{display:inline-flex;align-items:center;gap:6px;font-size:12px;background:var(--surface-2);
  border:1px solid var(--border);border-radius:5px;padding:3px 9px 3px 6px;color:var(--text)}
.file-chip .ficon{width:16px;height:16px;flex:none}
.demo-note{background:var(--accent-soft);border-left:3px solid var(--track,var(--accent));
  padding:11px 15px;border-radius:0 9px 9px 0;font-size:14px;margin:0 0 20px}
.steps{display:flex;flex-direction:column;gap:14px;margin-bottom:22px}
.step{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  box-shadow:var(--shadow);overflow:hidden}
.step.prompt{border-left:3px solid var(--track,var(--accent))}
.step.action{border-left:3px solid var(--governance);background:var(--surface-2)}
.step-head{display:flex;align-items:center;gap:11px;padding:13px 16px}
.step-kind{font-size:10.5px;font-weight:800;text-transform:uppercase;letter-spacing:1px;
  color:var(--track,var(--accent))}
.step.action .step-kind{color:var(--governance)}
.step-head h4{margin:0;font-size:14.5px;font-weight:700;flex:1}
.copy{font-size:12px;font-weight:600;padding:5px 13px;border-radius:8px;border:1px solid var(--border);
  background:var(--surface);color:var(--text);cursor:pointer}
.copy:hover{border-color:var(--accent);color:var(--accent)}
.copy.done{background:var(--analysis);color:#fff;border-color:transparent}
pre{margin:0;padding:14px 16px;background:var(--surface-2);border-top:1px solid var(--border);
  font-family:"Cascadia Code",Consolas,monospace;font-size:13px;line-height:1.55;
  white-space:pre-wrap;word-break:break-word;color:var(--text)}
.action-body{margin:0;padding:0 16px 15px;font-size:14px;color:var(--text)}

/* Click-path (bold, followable portal walkthrough) */
.step.clickpath{border-left:3px solid var(--track,var(--governance))}
.step.clickpath .step-kind{color:var(--track,var(--governance))}
.step.clickpath .step-head{flex-wrap:wrap}
.portal-link{font-size:12px;font-weight:700;padding:5px 12px;border-radius:6px;
  border:1px solid var(--track,var(--governance));color:var(--track,var(--governance));
  background:var(--surface);white-space:nowrap}
.portal-link:hover{background:var(--track,var(--governance));color:#fff;text-decoration:none}
.cp-body{padding:4px 16px 16px;display:flex;flex-direction:column;gap:12px}
.cp-breadcrumb{display:flex;flex-wrap:wrap;align-items:center;gap:7px;
  background:var(--surface-2);border:1px solid var(--border);border-radius:6px;padding:8px 11px}
.cp-crumb{font-size:12.5px;font-weight:600;color:var(--text);font-family:"Cascadia Code",Consolas,monospace}
.cp-crumb.start{color:var(--track,var(--governance));font-weight:800}
.cp-sep{color:var(--muted);font-weight:700;font-size:13px}
.cp-steps{margin:0;padding:0;list-style:none;counter-reset:cp;display:flex;flex-direction:column;gap:9px}
.cp-steps li{position:relative;padding:3px 0 3px 40px;font-size:14px;line-height:1.55;
  counter-increment:cp;min-height:28px;display:flex;align-items:center}
.cp-steps li::before{content:counter(cp);position:absolute;left:0;top:1px;width:26px;height:26px;
  border-radius:7px;background:var(--track,var(--governance));color:#fff;font-weight:800;font-size:13px;
  display:flex;align-items:center;justify-content:center}
.cp-steps li::after{content:"";position:absolute;left:13px;top:29px;bottom:-9px;width:2px;
  background:var(--border)}
.cp-steps li:last-child::after{display:none}
.cp-callout{display:flex;gap:11px;align-items:flex-start;padding:10px 13px;border-radius:8px;
  border:1px solid var(--border)}
.cp-callout p{margin:0;font-size:13.5px;line-height:1.5}
.cp-tag{font-size:9.5px;font-weight:800;text-transform:uppercase;letter-spacing:.8px;
  padding:3px 8px;border-radius:5px;white-space:nowrap;flex:none;margin-top:1px}
.cp-scenario{background:var(--accent-soft);border-color:transparent}
.cp-scenario .cp-tag{background:var(--accent);color:#fff}
.cp-watch{background:rgba(16,124,16,.10);border-color:transparent}
.cp-watch .cp-tag{background:var(--analysis);color:#fff}
.cp-watch p{font-weight:600}
.cp-say{background:var(--surface-2)}
.cp-say .cp-tag{background:var(--muted);color:#fff}
.cp-say p{font-style:italic;color:var(--muted)}
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
.cmp-wrap{overflow-x:auto;margin:0 0 14px;border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow)}
.cmp{width:100%;border-collapse:collapse;font-size:13px;background:var(--surface)}
.cmp th,.cmp td{padding:11px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--border);border-right:1px solid var(--border)}
.cmp thead th{background:var(--surface-2);font-weight:800;font-size:12.5px;border-bottom:2px solid var(--border)}
.cmp thead th:first-child{width:24%}
.cmp thead th:nth-child(2){width:18%}
.cmp thead th:last-child{color:var(--governance)}
.cmp tbody th{font-weight:700;font-size:12.5px;color:var(--text);width:24%}
.cmp tbody td{color:var(--muted)}
.cmp td.applies{color:var(--apps);font-weight:700;font-size:12px;line-height:1.4}
.cmp td:last-child,.cmp th:last-child{border-right:none}
.cmp tbody tr:last-child th,.cmp tbody tr:last-child td{border-bottom:none}
.cmp tbody tr:hover td,.cmp tbody tr:hover th{background:var(--surface-2)}
.cmp .yes{color:var(--analysis);font-weight:800}
.cmp .no{color:var(--governance);font-weight:800}
.cmp .part{color:var(--apps);font-weight:800}
.gov-note{font-size:12.5px;color:var(--muted);background:var(--accent-soft);border-left:3px solid var(--accent);padding:10px 13px;border-radius:0 6px 6px 0;margin:0 0 16px}
.gov-filters{display:flex;flex-direction:column;gap:12px;margin:0 0 16px;padding:14px;background:var(--surface-2);border:1px solid var(--border);border-radius:var(--radius)}
.gov-filter{margin:0}
.gov-filter-lbl{display:block;font-size:11px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
.gov-chips{margin:0}
.gov-filter-hint{font-size:12px;color:var(--muted);margin:10px 0 0;min-height:16px;font-weight:600}
.cmp tbody tr.cmp-group th{width:auto;background:var(--surface-2);color:var(--text);font-weight:800;font-size:11.5px;letter-spacing:.6px;text-transform:uppercase;border-bottom:2px solid var(--border)}
.cmp tbody tr.cmp-group:hover th{background:var(--surface-2)}
.cmp-gnum{display:inline-block;min-width:22px;margin-right:9px;color:var(--accent);font-weight:800;font-variant-numeric:tabular-nums}
.cmp tbody tr.hide{display:none}
.pac-cmp thead th:first-child{width:26%}
.pac-cmp thead th:nth-child(2){width:37%}
.pac-cmp thead th:last-child{width:37%}
.pac-cmp td.pac-add{background:var(--accent-soft);color:var(--text);border-left:2px solid var(--accent)}
.pac-verdict{display:flex;gap:12px;align-items:flex-start;background:linear-gradient(135deg,var(--accent-soft),var(--surface-2));border:1px solid var(--accent);border-radius:var(--radius);padding:14px 16px;margin:0 0 16px}
.pac-verdict-tag{flex:none;font-size:10.5px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:#fff;background:var(--accent);padding:4px 9px;border-radius:4px;margin-top:1px}
.pac-verdict p{margin:0;font-size:13px;line-height:1.55;color:var(--text)}
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
  [...chips.querySelectorAll('.chip')].forEach(c=>c.classList.toggle('active',c===b));
  const t=b.dataset.track;
  $$('.demo-card').forEach(c=>{c.style.display=(t==='all'||c.dataset.track===t)?'':'none';});
  $$('.track-group').forEach(g=>{g.style.display=(t==='all'||g.dataset.track===t)?'':'none';});
});

// governance table — two filter axes (agent type + what you need), AND-combined
const govChips=$('#gov-chips');
if(govChips){
  const planeChips=$('#gov-planes');
  const dataRows=$$('#ctx-governance .cmp tbody tr:not(.cmp-group)');
  const groupRows=$$('#ctx-governance .cmp tbody tr.cmp-group');
  const hint=$('#gov-filter-hint');
  const tLabels={builder:'Agent Builder',studio:'Copilot Studio',foundry:'Foundry',external:'3rd-party',firstparty:'first-party (Researcher/Analyst)'};
  const pLabels={baseline:'the baseline admin center (admin role only)',agent365:'Microsoft Agent 365 / E7',powerplatform:'Power Platform admin center',entra:'Entra ID P1·P2'};
  let curType='all',curPlane='all';
  const apply=()=>{
    let shown=0;
    dataRows.forEach(r=>{
      const types=(r.dataset.types||'').split(' ').filter(Boolean);
      const planes=(r.dataset.planes||'').split(' ').filter(Boolean);
      const tv=(curType==='all')||(r.dataset.all==='1'&&curType!=='firstparty')||types.includes(curType);
      const pv=(curPlane==='all')||planes.includes(curPlane);
      const vis=tv&&pv;
      r.classList.toggle('hide',!vis);
      if(vis)shown++;
    });
    groupRows.forEach(g=>{
      const gid=g.dataset.group;
      const any=dataRows.some(r=>r.dataset.group===gid&&!r.classList.contains('hide'));
      g.classList.toggle('hide',!any);
    });
    const parts=[];
    if(curType!=='all')parts.push(tLabels[curType]+' agents');
    if(curPlane!=='all')parts.push('governed via '+pLabels[curPlane]);
    hint.textContent=parts.length?(shown+' of '+dataRows.length+' capabilities — '+parts.join(' · ')):'';
  };
  govChips.addEventListener('click',e=>{
    const b=e.target.closest('.chip');if(!b)return;
    [...govChips.querySelectorAll('.chip')].forEach(c=>c.classList.toggle('active',c===b));
    curType=b.dataset.gtype;apply();
  });
  if(planeChips)planeChips.addEventListener('click',e=>{
    const b=e.target.closest('.chip');if(!b)return;
    [...planeChips.querySelectorAll('.chip')].forEach(c=>c.classList.toggle('active',c===b));
    curPlane=b.dataset.plane;apply();
  });
}
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
            kind = s.get("kind")
            lines.append(f"### {s.get('title','')}")
            lines.append("")
            if kind == "clickpath":
                lines.append("```demo")
                if s.get("scenario"):
                    lines.append(f"Scenario: {s['scenario']}")
                crumb = ([s["portal"]] if s.get("portal") else []) + list(s.get("path", []) or [])
                if crumb:
                    lines.append("Path: " + " > ".join(crumb))
                if s.get("url"):
                    lines.append(f"Open: {s['url']}")
                for i, stp in enumerate(s.get("steps", []) or [], 1):
                    lines.append(f"{i}. {stp}")
                if s.get("watch"):
                    lines.append(f"On screen: {s['watch']}")
                if s.get("say"):
                    lines.append(f"Say: {s['say']}")
                lines.append("```")
                lines.append("")
                continue
            fence = "prompt" if kind == "prompt" else "demo"
            lines.append(f"```{fence}")
            lines.append(s.get("text", "").rstrip("\n"))
            lines.append("```")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    bump = "--no-bump" not in sys.argv
    version = stamp_version_and_date() if bump else None
    data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    HTML_OUT.write_text(render_html(data), encoding="utf-8")
    MD_OUT.parent.mkdir(parents=True, exist_ok=True)
    MD_OUT.write_text(render_md(data), encoding="utf-8")
    stamp = f"v{version} · {data['meta']['date']}" if version else "(no version bump)"
    print(f"OK  {len(data['demos'])} demos  {stamp}")
    print(f"    -> {HTML_OUT.name} ({HTML_OUT.stat().st_size:,} bytes)")
    print(f"    -> {MD_OUT.relative_to(ROOT)} ({MD_OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
