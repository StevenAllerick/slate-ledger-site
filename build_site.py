#!/usr/bin/env python3
"""Slate & Ledger marketing site — single source of truth for every page.

Same house convention as the product build scripts: one script generates every
HTML file; nothing here is hand-edited afterward. Run `python3 build_site.py`
from this directory to regenerate index.html + products/*.html.

Copy is pulled from each product's own MARKETING_COPY.md (already researched/
written this suite's marketing pass) and GO_TO_MARKET.md — nothing here is
invented fresh. Design is the same committed-dark "companion-tool skin"
documented in branding/BRAND_GUIDE.md (navy/gold on a dark ground, Georgia
masthead, sprocket-strip motif) — this site had been the one surface still
using the older light/paper skin; this brings it in line with the rest of the
suite, and with the 2026 "dark mode as a core identity" web trend the owner
asked to follow.
"""
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_DIR = os.path.join(OUT_DIR, "products")
os.makedirs(PRODUCTS_DIR, exist_ok=True)

# ------------------------------------------------------------------
# The brand mark (used in the header on every page). Every product hero is a
# real, licensed photo (or, for the residuals card, a bespoke graphic) in
# img/ — see img/_raw and PROJECT history for the sourcing/compositing steps.
# ------------------------------------------------------------------

CLAPPERBOARD = """
<svg viewBox="0 0 100 100" aria-hidden="true">
  <rect x="4" y="11" width="92" height="82" rx="6" fill="none" stroke="#F3EEE1" stroke-width="2.5"/>
  <line x1="12" y1="41" x2="88" y2="41" stroke="#D9A93A" stroke-width="2.5"/>
  <circle cx="19" cy="26" r="3" fill="#D9A93A"/>
  <line x1="34" y1="17" x2="41" y2="35" stroke="#D9A93A" stroke-width="2.5"/>
  <line x1="51" y1="17" x2="58" y2="35" stroke="#D9A93A" stroke-width="2.5"/>
  <line x1="68" y1="17" x2="75" y2="35" stroke="#D9A93A" stroke-width="2.5"/>
  <line x1="15" y1="54" x2="85" y2="54" stroke="#D9A93A" stroke-width="1.6" opacity=".8"/>
  <line x1="15" y1="66" x2="85" y2="66" stroke="#D9A93A" stroke-width="1.6" opacity=".8"/>
  <line x1="15" y1="78" x2="85" y2="78" stroke="#D9A93A" stroke-width="1.6" opacity=".8"/>
</svg>
"""

# ------------------------------------------------------------------
# Product data — taglines/descriptions/prices are pulled verbatim or near-
# verbatim from each repo's own MARKETING_COPY.md; nothing invented here.
# `buy_url` is intentionally empty until each product is live on Lemon
# Squeezy — see the TODO note rendered next to the button below.
# ------------------------------------------------------------------

PRODUCTS = [
    {
        "slug": "micro-budget-film-budget-builder",
        "title_break": True,
        "order": "1 · Budget",
        "name": "Micro-Budget Film Budget Builder",
        "tagline": "Not just a total. A plan.",
        "subhead": "It doesn’t just calculate your budget. It helps you build it.",
        "hero_img": "camera-hero",
        "hero_alt": "A vintage cine camera",
        "price": "$35",
        "paragraphs": [
            "A full single-feature budget with real 2026 SAG-AFTRA tiers — Micro-Budget, Student Film, SPA, "
            "UPA, MPA, LBA, and New Media (Deferred) — each explained right where you fill it in, not buried "
            "in a manual.",
            "Pick a tier your project doesn’t actually qualify for and it warns you immediately, not after "
            "you’ve built a whole budget on the wrong assumption. Every number is color-coded so you always "
            "know where it came from — a starting suggestion, something you entered, or a real union minimum.",
            "A financier-ready Top Sheet, an Actuals tab to track real spend once you’re shooting, and a "
            "Resources tab with real vendors and marketplaces — grouped to match your budget — for every "
            "placeholder line you still need to price out.",
            "Verified to recalculate identically in Excel, Google Sheets, and Apple Numbers. Your co-producer "
            "doesn’t have to use your software.",
        ],
        "buy_url": "",
    },
    {
        "slug": "episodic-series-budget-builder",
        "title_break": True,
        "order": "2 · Budget",
        "name": "Episodic Series Budget Builder",
        "tagline": "Built for a season. Not bent into the shape of one.",
        "subhead": "Real per-episode and season-level costs, both — not one spreadsheet pretending to be the other.",
        "hero_img": "tv-hero",
        "hero_alt": "A vintage dark television set",
        "price": "$35",
        "paragraphs": [
            "Budgeting a series in a single-project tool means picking a lie to live with: treat every cost as "
            "season-long and your per-episode economics are wrong, or treat everything as per-episode and you "
            "lose the season-level picture entirely.",
            "This tool does both, at once. A season-level estimate and a real per-episode grid coexist rather "
            "than compete — you see the whole season’s number and every episode’s own number, together. "
            "Episode count is a first-class variable throughout.",
            "It reuses the film budget builder’s real, sourced union rate data — not a separate, invented "
            "set — and evaluates the Micro-Budget SAG-AFTRA cap the way it actually works: per episode, not "
            "per season, a detail that’s easy to miss and expensive to get wrong.",
        ],
        "buy_url": "",
    },
    {
        "slug": "schedule-builder",
        "order": "3 · Schedule",
        "name": "Schedule Builder",
        "tagline": "From script to shoot day, in one file.",
        "subhead": "A real breakdown, a real stripboard, a real Day Out of Days — not a subscription.",
        "hero_img": "hourglass-hero",
        "hero_alt": "A backlit hourglass with flowing sand",
        "price": "$35",
        "paragraphs": [
            "Drop in your actual script — Final Draft (.fdx) or Fountain, not a flattened PDF — and it reads "
            "every scene: INT/EXT, day or night, the set, page length, and who’s speaking.",
            "Everything the parser can’t know for certain — props, vehicles, stunts, extras, wardrobe, "
            "minors, special effects — comes back as an honest first-pass suggestion next to the line it came "
            "from, that you review and correct in one editable table. Never presented as done when it isn’t.",
            "Drag scenes onto shoot days on a real color-coded stripboard, or click Auto-arrange for a starting "
            "point. Exports a stripboard, a Day Out of Days, a one-line schedule, and the schedule.csv the "
            "budget builders and Paperwork Tracker can read directly.",
        ],
        "buy_url": "",
    },
    {
        "slug": "paperwork-tracker",
        "order": "4 · Paperwork",
        "name": "Paperwork Tracker",
        "tagline": "Fill in your production once. Get every union form filled out.",
        "subhead": "Every SAG, WGA, DGA, and IATSE deadline, merged into one calendar — with its source cited.",
        "hero_img": "laptop-hero",
        "hero_alt": "An open laptop",
        "price": "$35",
        "paragraphs": [
            "A first-time producer’s real fear: a SAG filing deadline, a WGA packet due date, an IATSE notice "
            "window — four unions, four separate paperwork tracks, none of them coordinated with each other.",
            "This tool does two things nothing else in this category does at all. It fills the actual "
            "paperwork — open the companion Filler in any browser, enter your production’s details once, and "
            "it fills WGA’s real filing packet, SAG-AFTRA’s Cast Clearance form, and the Exhibit G time "
            "report directly onto the unions’ own PDFs.",
            "For the forms the unions don’t provide a fillable version of at all, it generates a clean, "
            "correct equivalent. And the workbook itself tracks every deadline across every union in one "
            "chronological list, each one cited to where it actually comes from.",
        ],
        "buy_url": "",
    },
    {
        "slug": "residuals-revenue-tracker",
        "title_break": True,
        "order": "5 · Residuals",
        "name": "Residuals & Self-Distribution Revenue Tracker",
        "tagline": "What your film earns after it’s finished — not just what it cost.",
        "subhead": "Real SAG-AFTRA and WGA residual formulas, plus a real self-distribution revenue split.",
        "hero_img": "card-hero",
        "hero_alt": "A dark Slate & Ledger member card",
        "price": "$15",
        "paragraphs": [
            "Almost nothing in this category models what happens after a film is finished — every budget tool "
            "stops at the wrap party. This one picks up from there.",
            "SAG-AFTRA residuals, calculated per performer across every category that actually applies at this "
            "budget size: free TV reruns, Pay TV/Basic Cable, Home Video/DVD, SVOD, foreign theatrical, and New "
            "Media/Ad-Supported Internet.",
            "WGA residuals at a real sourced rate for theatrical reuse, split automatically across credited "
            "writers. Plus a YouTube ad-revenue and profit-share calculator for a self-distributed release — "
            "the side of the business every other tool in this category ignores.",
        ],
        "buy_url": "",
    },
]

SUITE_PRICE = "$99"

# ------------------------------------------------------------------
# Shared HTML shell
# ------------------------------------------------------------------

def head(title, description, depth=""):
    return f"""<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="{depth}icon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Zilla+Slab:wght@400;500;600;700&family=Mulish:wght@400;500;600;700&family=Jost:wght@500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.cdnfonts.com/css/simplifica" rel="stylesheet">
<style>
{CSS}
</style>
</head>"""

CSS = """
  /* Slate & Ledger house dark skin — the same committed-dark "cutting-room"
     world as the companion browser tools (see branding/BRAND_GUIDE.md).
     Not theme-responsive on purpose: dark mode is the identity here, not a
     toggle — 2026's own web-design trend line agrees with that call. */
  :root{
    --bg:#14161d; --surface:#1b1e27; --surface-raised:#20242e; --line:#2c2f3a;
    --navy:#1F4E78; --slate:#17324b; --slate-line:#24567e;
    --gold:#D9A93A; --gold-dim:#A9822A; --red:#C1442E; --green:#7BA383;
    --text:#F3EEE1; --text-dim:#ABA391; --text-faint:#6E6857;
    --f-display:'Georgia','Times New Roman',serif;
    --f-head:'Jost','Helvetica Neue',Helvetica,Arial,sans-serif;
    --f-body:'Simplifica','Avenir Next','Avenir','Mulish','Nunito Sans',system-ui,sans-serif;
    --f-util:'Zilla Slab','Georgia',serif;
  }
  *{ box-sizing:border-box; }
  html,body{ margin:0; padding:0; }
  body{ background-color:var(--bg);
    background-image:linear-gradient(rgba(20,22,29,.68),rgba(20,22,29,.68)), var(--bg-image);
    background-size:cover; background-position:center; background-repeat:no-repeat;
    background-attachment:fixed;
    color:var(--text); font-family:var(--f-body); font-weight:700;
    line-height:1.6; min-height:100vh; text-transform:uppercase; letter-spacing:.03em;
    -webkit-text-stroke:.4px currentColor; }
  .wrap{ max-width:1080px; margin:0 auto; padding:0 24px 90px; }
  a{ color:var(--gold); text-decoration:none; }
  a:hover{ text-decoration:underline; }

  /* ---- fade-up choreography: shell, then image, then text, ~.5s apart ---- */
  @keyframes fadeUp{ from{ opacity:0; transform:translateY(16px);} to{ opacity:1; transform:translateY(0);} }
  .fade-1,.fade-2,.fade-3{ opacity:0; animation:fadeUp .7s ease-out forwards; }
  .fade-1{ animation-delay:.05s; }
  .fade-2{ animation-delay:.55s; }
  .fade-3{ animation-delay:1.05s; }
  @media (prefers-reduced-motion: reduce){
    .fade-1,.fade-2,.fade-3{ animation:none; opacity:1; }
  }

  /* ---- ticker: a scrolling strip of the union/guild/paperwork terms the suite
     actually tracks — the same "always-moving status strip" cue as the fade
     choreography above, just horizontal. Two copies of the list sit side by
     side and slide together by exactly one copy's width, so the loop seams
     invisibly. ---- */
  .ticker{ background:var(--bg); border-bottom:1px solid var(--line); overflow:hidden;
    margin:0 -24px; white-space:nowrap; }
  .ticker-track{ display:inline-flex; animation:ticker-scroll 38s linear infinite; }
  .ticker-track span{ font-family:var(--f-util); font-size:12px; letter-spacing:.08em;
    text-transform:uppercase; color:var(--text-faint); padding:10px 22px; flex:0 0 auto; }
  .ticker-track span.dot{ color:var(--gold-dim); padding:10px 0; }
  @keyframes ticker-scroll{ from{ transform:translateX(0); } to{ transform:translateX(-50%); } }
  @media (prefers-reduced-motion: reduce){ .ticker-track{ animation:none; } }

  /* ---- floating status chips: small pill call-outs that drift near a hero
     object, each on its own fade delay so they don't all land at once. ---- */
  .chip-field{ position:relative; }
  .status-chip{ position:absolute; display:flex; align-items:center; gap:7px;
    background:var(--surface-raised); border:1px solid var(--line); border-radius:99px;
    padding:8px 16px 8px 12px; font-family:var(--f-util); font-size:12.5px; color:var(--text-dim);
    box-shadow:0 10px 24px rgba(0,0,0,.4); animation:chipfloat 7s ease-in-out infinite; white-space:nowrap; }
  .status-chip .ok{ width:16px; height:16px; border-radius:50%; background:var(--green);
    display:flex; align-items:center; justify-content:center; color:#0c140f; font-size:10px; flex:0 0 auto; }
  @keyframes chipfloat{ 0%{ transform:translateY(0); } 50%{ transform:translateY(-8px); } 100%{ transform:translateY(0); } }
  @media (prefers-reduced-motion: reduce){ .status-chip{ animation:none; } }

  header.marquee{ background:var(--slate);
    background-image:linear-gradient(180deg,#1a3a58,#17324b 62%,#142a40);
    border-bottom:2px solid var(--gold); margin:0 -24px; padding:22px 24px 26px;
    position:relative; overflow:hidden; }
  .sprockets{ position:absolute; top:0; left:0; right:0; height:12px;
    background-image:repeating-linear-gradient(90deg,var(--gold-dim) 0 7px,transparent 7px 24px); opacity:.45; }
  .brandline{ display:flex; align-items:center; gap:11px; }
  .brandline svg{ width:28px; height:28px; display:block; flex:0 0 auto; }
  .brandline .wm{ font-family:var(--f-display); font-size:13px; letter-spacing:.32em;
    color:var(--text); display:inline-block; transform:scaleX(1.06); transform-origin:left; opacity:.92; }
  nav.crumb{ margin-top:10px; }
  nav.crumb a{ font-family:var(--f-util); font-size:12.5px; color:var(--text-dim); }
  nav.crumb a:hover{ color:var(--gold); }
  nav.crumb a.on{ color:var(--gold); }
  footer .footer-links{ display:inline-block; margin-top:8px; }
  footer .footer-links a{ color:var(--text-dim); font-size:12px; }

  .hero{ text-align:center; padding:64px 0 16px; }
  h1{ font-family:var(--f-head); font-weight:700; letter-spacing:.01em;
    font-size:clamp(34px,6.2vw,58px); line-height:1.08; text-transform:uppercase; margin:0 0 16px; }
  h1 .gold{ color:var(--gold); }
  .subhead{ font-family:var(--f-body); font-size:21px; color:var(--text-dim); max-width:640px;
    margin:0 auto 30px; }
  .eyebrow-label{ font-family:var(--f-head); letter-spacing:.14em; text-transform:uppercase;
    font-size:14px; color:var(--gold); }

  /* ---- the "floating in a void" hero treatment: a real photo cutout, not flat line art,
     hovering over a radial-gradient spotlight so the dark ground reads as depth, not a flat page.
     This is a flat image, not a 3D model, so motion stays to a gentle front-to-back nod (rotateX)
     and a slow float — a real spin (rotateY past ~90°) would show the image edge-on and then
     mirrored (backwards numerals, reversed wordmark), which reads as broken, not as depth. */
  .void-wrap{ position:relative; display:flex; justify-content:center; align-items:center;
    padding:18px 0 42px; perspective:1100px; }
  .void-glow{ position:absolute; width:520px; height:520px; max-width:90vw;
    background:radial-gradient(circle, rgba(217,169,58,.16) 0%, rgba(217,169,58,.05) 38%, transparent 68%);
    pointer-events:none; }
  .void-float{ position:relative; width:300px; max-width:70vw; animation:hover 10s ease-in-out infinite;
    transform-style:preserve-3d; }
  .void-float img{ width:100%; height:auto; display:block;
    filter:drop-shadow(0 30px 40px rgba(0,0,0,.65)) drop-shadow(0 4px 14px rgba(217,169,58,.12)); }
  @keyframes hover{
    0%{ transform:translateY(0) rotateX(0deg); }
    50%{ transform:translateY(-14px) rotateX(-16deg); }
    100%{ transform:translateY(0) rotateX(0deg); }
  }
  @media (prefers-reduced-motion: reduce){ .void-float{ animation:none; } }

  .rule{ height:2px; background:linear-gradient(90deg,transparent,var(--gold-dim),transparent);
    border:none; margin:40px 0; opacity:.7; }

  .tools{ display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:8px; }
  @media (max-width:640px){ .tools{ grid-template-columns:1fr; } }
  .tool{ background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:20px 22px;
    transition:border-color .15s; }
  .tool:hover{ border-color:var(--gold-dim); }
  .tool .order{ text-transform:uppercase; letter-spacing:.1em; font-size:11.5px; color:var(--gold);
    font-family:var(--f-head); margin:0 0 6px; }
  .tool h3{ font-family:var(--f-head); letter-spacing:.02em; font-size:20px; color:var(--text);
    margin:0 0 6px; font-weight:400; text-transform:uppercase; }
  .tool p{ margin:0; font-size:16.5px; color:var(--text-dim); line-height:1.55; }
  .tool .price{ display:block; margin-top:10px; font-family:var(--f-head); letter-spacing:.03em; color:var(--gold); font-size:18px; }

  .pitch{ font-family:var(--f-util); background:var(--surface); border:1px solid var(--line);
    border-left:4px solid var(--gold); border-radius:6px; padding:22px 26px; margin-top:46px; font-size:16px;
    line-height:1.6; }

  .body-copy p{ font-size:18.5px; color:var(--text-dim); max-width:66ch; margin:0 auto 18px; text-align:left; }
  .body-copy{ max-width:66ch; margin:0 auto; }

  .price-line{ text-align:center; margin:40px 0 18px; }
  .price-line .amt{ font-family:var(--f-head); letter-spacing:.02em; font-size:48px; color:var(--gold); }
  .price-line .note{ display:block; font-family:var(--f-util); font-size:13px; color:var(--text-faint); margin-top:4px; }
  .cta-row{ text-align:center; margin:22px 0 8px; }
  .btn{ display:inline-block; font-family:var(--f-head); font-size:16px; letter-spacing:.06em;
    text-transform:uppercase; padding:14px 28px; border-radius:5px; border:1px solid var(--slate-line); }
  .btn.primary{ background:var(--navy); color:var(--text); }
  .btn.primary:hover{ border-color:var(--gold); text-decoration:none; }
  .btn.disabled{ background:var(--surface); color:var(--text-faint); border-color:var(--line); cursor:not-allowed; }
  .btn-note{ display:block; margin-top:10px; font-family:var(--f-util); font-size:11.5px; color:var(--text-faint); }

  footer{ text-align:center; margin-top:64px; font-size:12.5px; color:var(--text-faint);
    font-family:var(--f-util); border-top:1px solid var(--line); padding-top:22px; }
  footer a{ color:var(--text-dim); }

  .page-title{ font-family:var(--f-head); font-size:clamp(30px,5vw,44px); letter-spacing:.04em;
    text-transform:uppercase; text-align:center; margin:56px 0 30px; }
  .prose{ max-width:70ch; margin:0 auto; font-size:18.5px; color:var(--text-dim); }
  .prose h2{ font-family:var(--f-head); letter-spacing:.03em; text-transform:uppercase;
    color:var(--text); font-size:20px; font-weight:400; margin:34px 0 10px; }
  .prose p{ margin:0 0 16px; }
  .prose strong{ color:var(--text); }
  .callout{ font-family:var(--f-util); background:var(--surface); border:1px solid var(--line);
    border-left:4px solid var(--gold); border-radius:6px; padding:18px 22px; margin:22px 0; font-size:14.5px;
    line-height:1.6; color:var(--text-dim); }
  .sources{ font-family:var(--f-util); font-size:13.5px; color:var(--text-dim); line-height:2; }
  .contact-block{ text-align:center; margin:48px 0; }
  .contact-block .email{ font-family:var(--f-head); font-size:28px; letter-spacing:.03em; }
"""


# The terms the suite actually tracks across its five products — pulled from
# each product's own MARKETING_COPY.md, nothing invented for the ticker.
TICKER_TERMS = [
    "IATSE", "SAG-AFTRA", "ACTRA", "WGA", "DGA", "Teamsters",
    "Micro-Budget Tier", "SPA", "UPA", "Day Out of Days", "Exhibit G",
    "Coogan Law", "Residuals", "Tier Ceilings", "Cast Clearance",
]

def ticker():
    items = "".join(f'<span>{t}</span><span class="dot">&#9679;</span>' for t in TICKER_TERMS)
    return f"""<div class="ticker"><div class="ticker-track">{items}{items}</div></div>"""

def brandline(depth="", current=""):
    def link(label, href, key):
        cls = ' class="on"' if key == current else ""
        return f'<a{cls} href="{href}">{label}</a>'
    links = [
        link("All Tools", f"{depth}index.html", "home"),
        link("About", f"{depth}about.html", "about"),
        link("Help", f"{depth}help.html", "help"),
        link("FAQ", f"{depth}faq.html", "faq"),
        link("Terms", f"{depth}terms.html", "terms"),
        link("Contact", f"{depth}contact.html", "contact"),
    ]
    return f"""<header class="marquee">
    <div class="sprockets"></div>
    <div class="brandline">
      {CLAPPERBOARD}
      <span class="wm">SLATE &amp; LEDGER</span>
    </div>
    <nav class="crumb">{" &middot; ".join(links)}</nav>
  </header>
  {ticker()}"""

def footer(depth=""):
    return f"""<footer>
    Slate &amp; Ledger is a product of The Allerick Dynasty Inc.<br>
    One-time purchase &mdash; no subscription, no account, no cloud.<br>
    <span class="footer-links"><a href="{depth}about.html">About</a> &middot;
    <a href="{depth}help.html">Help</a> &middot;
    <a href="{depth}faq.html">FAQ</a> &middot;
    <a href="{depth}terms.html">Terms of Sale</a> &middot;
    <a href="{depth}contact.html">Contact</a></span>
  </footer>"""

# ------------------------------------------------------------------
# index.html
# ------------------------------------------------------------------

tool_cards = "\n".join(f"""      <a class="tool" href="products/{p['slug']}.html">
        <p class="order">{p['order']}</p>
        <h3>{p['name']}</h3>
        <p>{p['subhead']}</p>
        <span class="price">{p['price']}</span>
      </a>""" for p in PRODUCTS)

index_html = f"""<!DOCTYPE html>
<html lang="en">
{head(
    "Digital Indie Film Desk, by Slate & Ledger",
    "Budgeting, scheduling, union paperwork, and residuals tools for indie and micro-budget filmmakers. "
    "One-time purchase, no subscription, works offline."
)}
<body style="--bg-image:url('img/bg-filmset.jpg')">
  <div class="fade-1">{brandline(current="home")}</div>
  <div class="wrap">
    <div class="hero fade-1">
      <h1>Digital Indie<br><span class="gold">Film Desk</span></h1>
      <p class="subhead">Tools for independent producers, by Slate &amp; Ledger.</p>
    </div>

    <div class="void-wrap chip-field fade-2">
      <div class="void-glow"></div>
      <div class="void-float"><picture>
        <source srcset="img/clapperboard-hero.webp" type="image/webp">
        <img src="img/clapperboard-hero.png" alt="A film clapperboard" loading="eager">
      </picture></div>
      <div class="status-chip" style="top:8%; left:2%; animation-delay:.2s;">
        <span class="ok">&#10003;</span> SAG tier flagged
      </div>
      <div class="status-chip" style="bottom:14%; right:1%; animation-delay:2.1s;">
        <span class="ok">&#10003;</span> Day Out of Days built
      </div>
      <div class="status-chip" style="top:44%; right:6%; animation-delay:4.4s;">
        <span class="ok">&#10003;</span> Residual logged
      </div>
    </div>

    <div class="fade-3">
      <p class="subhead" style="max-width:680px">Budgeting, scheduling, union paperwork, and residuals &mdash;
        built for the film you're actually making. Five downloadable tools for indie and micro-budget
        productions. Every rate and deadline is cited to a real source. One-time purchase &mdash; no
        subscription, no account, no server. The project stays with you.</p>

      <hr class="rule">

      <div class="tools">
{tool_cards}
      </div>

      <div class="pitch">We know we could charge more. We built these to get more films made &mdash;
        make your fucking film.</div>

      <div class="price-line">
        <span class="amt">{SUITE_PRICE}</span>
        <span class="note">the full suite, once &mdash; buy two tools and the other three are basically free</span>
      </div>

      {footer()}
    </div>
  </div>
</body>
</html>
"""

with open(os.path.join(OUT_DIR, "index.html"), "w") as f:
    f.write(index_html)
print("index.html written")

# ------------------------------------------------------------------
# products/*.html
# ------------------------------------------------------------------

for p in PRODUCTS:
    paras = "\n".join(f"        <p>{para}</p>" for para in p["paragraphs"])
    words = p["name"].split(" ", 1)
    if len(words) == 2:
        # Short titles ("Schedule Builder") read fine wrapping naturally. Longer
        # ones split the gold phrase across lines awkwardly at normal widths —
        # for those, force the break between the white prefix and the gold
        # phrase instead, so the gold phrase always reads together as a line
        # (or lines) of its own rather than being torn apart mid-word.
        gold_text = words[1]
        if p["slug"] == "residuals-revenue-tracker":
            gold_text = "& Self-Distribution<br>Revenue Tracker"
        sep = "<br>" if p.get("title_break") else " "
        h1 = f"{words[0]}{sep}<span class=\"gold\">{gold_text}</span>"
    else:
        h1 = p["name"]

    if p["buy_url"]:
        cta = f'<a class="btn primary" href="{p["buy_url"]}">Buy the {p["price"]} 2026-2027 Edition</a>'
    else:
        cta = f'<span class="btn disabled">Buy the {p["price"]} 2026-2027 Edition</span>\n        <span class="btn-note">Store link goes live at launch.</span>'

    hero_block = f"""<div class="void-wrap fade-2">
      <div class="void-glow"></div>
      <div class="void-float"><picture>
        <source srcset="../img/{p['hero_img']}.webp" type="image/webp">
        <img src="../img/{p['hero_img']}.png" alt="{p['hero_alt']}" loading="eager">
      </picture></div>
    </div>"""

    page = f"""<!DOCTYPE html>
<html lang="en">
{head(f"{p['name']} — Slate & Ledger", p["subhead"], depth="../")}
<body style="--bg-image:url('../img/bg-filmset.jpg')">
  <div class="fade-1">{brandline(depth="../", current="home")}</div>
  <div class="wrap">
    <div class="hero fade-1">
      <p class="eyebrow-label">{p['order']}</p>
      <h1>{h1}</h1>
      <p class="subhead">{p['subhead']}</p>
    </div>

    {hero_block}

    <div class="fade-3">
      <div class="body-copy">
{paras}
      </div>

      <div class="price-line">
        <span class="amt">{p['price']}</span>
        <span class="note">2026-2027 Edition &mdash; one-time purchase, yours to keep</span>
      </div>
      <div class="cta-row">
        {cta}
      </div>

      {footer(depth="../")}
    </div>
  </div>
</body>
</html>
"""
    out_path = os.path.join(PRODUCTS_DIR, f"{p['slug']}.html")
    with open(out_path, "w") as f:
        f.write(page)
    print(f"products/{p['slug']}.html written")

# ------------------------------------------------------------------
# about.html / terms.html / contact.html
# ------------------------------------------------------------------

SOURCES_SAMPLE = [
    "SAG-AFTRA 2026 Theatrical/Television Agreement",
    "WGA Low Budget Agreement",
    "2026–2028 IATSE Low Budget Theatrical Agreement",
    "California Family Code § 6752 (Coogan Law)",
    "NY Estates Powers &amp; Trusts Law § 7-7.1",
    "820 ILCS 206/90",
    "U.S. Copyright Office registration guidance",
    "California Film Commission location agreement templates",
]

about_html = f"""<!DOCTYPE html>
<html lang="en">
{head("About — Slate & Ledger", "Why Slate & Ledger is priced the way it is, and what every rate in it is sourced to.")}
<body style="--bg-image:url('img/bg-filmset.jpg')">
  <div class="fade-1">{brandline(current="about")}</div>
  <div class="wrap">
    <h1 class="page-title fade-1">About</h1>

    <div class="fade-3 prose">
      <p><strong>The honest version.</strong> This took months to research and every rate in it is cited to
      the actual union agreement or the statute &mdash; not a blog, not a guess. We could price it like the
      companies that sell to studios. Movie Magic charges about $600 a year and still won't track a single
      SAG deadline for you.</p>

      <p>We're not doing that. We built this because we want to see more films get made &mdash; specifically
      yours. Specifically the one you keep saying you'll start once you've got the right tools lined up.</p>

      <p>You've got them now. So make your fucking film.</p>

      <h2>Every rate, cited</h2>
      <p>Every rate, threshold, and deadline in this suite is cited to its source &mdash; the actual union
      agreement, statute, or agency page. Estimates are labelled as estimates. No guessing, no "trust us."
      A sample of what that sourcing looks like:</p>
      <p class="sources">{" &middot; ".join(SOURCES_SAMPLE)}</p>

      <h2>What this isn't</h2>
      <div class="callout">Legal, financial, or production advice, and not a guarantee of accuracy for your
      production. It's research and planning estimates, current as of each product's Edition year. Union
      agreements get renegotiated; always confirm a figure directly with the union, guild, agency, or a
      qualified entertainment attorney before you rely on it for a real production. Provided "as is"; total
      liability is limited to what you paid. Full terms: <a href="terms.html">Terms of Sale</a>.</div>

      <h2>Pay-what-you-want, student pricing, and genuine hardship</h2>
      <p>Pay-what-you-want is available on the flagship tools and the suite bundle, with a real floor.
      Students pay a reduced price on any tool or the suite &mdash; a .edu address or a photo of a student ID
      is enough. And if a listed price is genuinely out of reach: email us and tell us what you're making. No
      form, no means-testing &mdash; a human reply, every time.</p>

      {footer()}
    </div>
  </div>
</body>
</html>
"""
with open(os.path.join(OUT_DIR, "about.html"), "w") as f:
    f.write(about_html)
print("about.html written")

# ------------------------------------------------------------------
# help.html — one section per tool. Content is hand-copied from
# HELP_GUIDE.md at the suite root (that file is the source of truth; keep
# this block in sync with it by hand, same convention as every other page
# here pulling from a markdown source).
# ------------------------------------------------------------------

help_html = f"""<!DOCTYPE html>
<html lang="en">
{head("Help — Slate & Ledger", "How to use every tool in the Slate & Ledger suite, step by step.")}
<body style="--bg-image:url('img/bg-filmset.jpg')">
  <div class="fade-1">{brandline(current="help")}</div>
  <div class="wrap">
    <h1 class="page-title fade-1">Help</h1>

    <div class="fade-3 prose">
      <p style="text-align:center">One section per tool &mdash; what it does, how to get started, and the
      questions people actually get stuck on. Every tool is a single downloadable file (or, for Paperwork
      Tracker, a workbook plus a companion browser page) &mdash; no install, no account, no server.</p>

      <h2>Micro-Budget Film Budget Builder</h2>
      <p>Real, sourced 2026 SAG-AFTRA and IATSE rates across all 7 low-budget tiers, plus a Resources tab
      pointing you to real places to price locations, gear, props, insurance, and legal help.</p>
      <p><strong>Getting started:</strong> Open the workbook in Excel, Sheets, or Numbers &rarr; enter your
      project basics and pick a budget tier &rarr; watch the TIER ALERT banner, which fires the moment
      something doesn't fit the tier you picked &rarr; use the Resources tab when you don't know what a line
      item should cost &rarr; the Top Sheet totals everything automatically.</p>
      <p><strong>Non-union?</strong> Every tier has a Non-Union path. <strong>First time budgeting a film?</strong>
      That's who this is built for &mdash; it explains what each tier requires and warns you before a real
      mistake, not after.</p>

      <h2>Episodic Series Budget Builder</h2>
      <p>The same real rates as the film tool, built for a season: per-episode and season-level costs modeled
      separately, plus a per-episode Tier Cap Check (the Micro-Budget tier's cap applies per episode, not per
      season).</p>
      <p><strong>Getting started:</strong> Set your episode count first &mdash; it drives the rest of the sheet
      &rarr; keep season-long cast/crew separate from per-episode guest cast &rarr; watch the per-episode Tier
      Cap Check if you're on the Micro-Budget tier &rarr; import a Schedule Builder export into Actuals to
      track real cost against budget, episode by episode.</p>

      <h2>Schedule Builder</h2>
      <p>Import your actual script &mdash; Final Draft (.fdx) or Fountain, not a flattened PDF &mdash; and get
      an editable scene breakdown, a real drag-and-drop stripboard, an Auto-arrange starting point, and a Day
      Out of Days.</p>
      <p><strong>Getting started:</strong> Import your script file &rarr; review the scene-by-scene breakdown
      (anything the parser can't know for certain comes back as a flagged first-pass guess &mdash; check and
      correct those) &rarr; drag scenes onto shoot days, or click Auto-arrange for a starting point that
      explains every choice and flags every compromise &rarr; enter cast availability so a conflict gets
      flagged before you shoot around it by accident &rarr; export the Day Out of Days and
      <code>schedule.csv</code> for the rest of the suite.</p>

      <h2>Paperwork Tracker (+ the Filler)</h2>
      <p>Tracks every WGA, SAG-AFTRA, DGA, and IATSE deadline &mdash; chronologically on the Timeline tab, or
      grouped by union on Timeline &mdash; By Union if you're splitting the paperwork across more than one
      person. The companion Filler (open "Paperwork Filler.html" in any browser) fills your production's
      details once and downloads real, filled union forms. Chain of Title tracks the documents that decide
      whether the finished film can be sold. The Deliverables Checklist is the final sale-readiness
      gate &mdash; a plain red/amber/green banner across 14 items.</p>
      <p><strong>Getting started:</strong> Enter key dates and union choices on Production Info &rarr; check
      the Timeline (or Timeline &mdash; By Union) for deadlines &rarr; track Chain of Title as it's locked in,
      pre-production &rarr; open the Filler and download real filled forms &rarr; before submitting anywhere,
      run the Deliverables Checklist.</p>
      <div class="callout">Slate &amp; Ledger is not a law firm; nothing here is legal advice, and using it
      does not create an attorney-client relationship. It's a document organiser &mdash; confirm every item
      with a qualified entertainment attorney before relying on it for a real production or sale.</div>

      <h2>Residuals &amp; Self-Distribution Revenue Tracker</h2>
      <p>The only tool in the suite that looks after release: real SAG-AFTRA residual formulas by category,
      WGA residuals (a sourced 1.2% theatrical-reuse rate, split by writer percentage), and a YouTube
      ad-revenue/profit-share tracker for self-distribution outside a union contract.</p>
      <p><strong>Getting started:</strong> Pick the calculator that matches your situation &mdash; a
      traditional distribution deal, a self-distributed YouTube release, or both &rarr; for SAG-AFTRA, enter
      each performer once; the per-performer table sums what they're owed across every category that applies
      &rarr; for YouTube, enter gross ad revenue and the sheet applies the platform split, recoups your costs,
      then splits the remainder across participants, flagging if shares ever exceed 100%.</p>

      <h2>Pricing, bundles, and discounts</h2>
      <p>See the <a href="faq.html">FAQ</a> for current pricing. Short version: each tool is a one-time
      purchase, the bundle covers all five at a lower combined price, and there's a standing student/hardship
      discount &mdash; no form, no means-testing, just email us.</p>

      <h2>Still stuck?</h2>
      <p style="text-align:center">Email <a href="mailto:hello@slateandledger.net">hello@slateandledger.net</a>
      with which tool, what you were trying to do, and what happened instead &mdash; a real person reads every
      message.</p>

      {footer()}
    </div>
  </div>
</body>
</html>
"""
with open(os.path.join(OUT_DIR, "help.html"), "w") as f:
    f.write(help_html)
print("help.html written")

# ------------------------------------------------------------------
# faq.html — quick suite-wide answers. Reuses the per-product FAQs already
# drafted in each MARKETING_COPY.md and marketing/suite-bundle-listing.md
# rather than inventing new copy (same house convention as the rest of this
# file). Pricing here must match GO_TO_MARKET.md §2 exactly -- that's the
# one confirmed source; PRODUCT_LINE_PLAN.md has a separate, explicitly
# "not final" repricing under discussion that does NOT belong here yet.
# ------------------------------------------------------------------

faq_html = f"""<!DOCTYPE html>
<html lang="en">
{head("FAQ — Slate & Ledger", "Frequently asked questions about the Slate & Ledger suite, pricing, and each tool.")}
<body style="--bg-image:url('img/bg-filmset.jpg')">
  <div class="fade-1">{brandline(current="faq")}</div>
  <div class="wrap">
    <h1 class="page-title fade-1">FAQ</h1>

    <div class="fade-3 prose">
      <h2>General</h2>
      <p><strong>Is there a subscription?</strong> No. Every tool is a one-time purchase &mdash; no account, no
      server, no recurring charge. Yours to keep and run offline for as long as you keep the file.</p>
      <p><strong>Which apps does it work in?</strong> Excel, Google Sheets, and Apple Numbers for the
      workbooks &mdash; tested, not assumed. The Paperwork Filler runs in any browser.</p>
      <p><strong>Is this legal, financial, or production advice?</strong> No. Slate &amp; Ledger is not a law
      firm and these aren't legal, financial, or production advice &mdash; they're research and planning
      estimates. Always confirm a figure directly with the union, guild, agency, or a qualified entertainment
      attorney before relying on it for a real production. Full terms: <a href="terms.html">Terms of Sale</a>.</p>
      <p><strong>Do the tools talk to each other?</strong> Yes, where it's real data: the Schedule Builder's
      export feeds real shoot dates into the Budget Builder's Actuals tab and the Paperwork Tracker's weekly
      deadlines; the Residuals Tracker is a companion to the budget builders' own cast/crew data.</p>

      <h2>Pricing</h2>
      <p>Each tool is <strong>$35</strong> (Residuals &amp; Self-Distribution Revenue Tracker is $15), or get
      all five in the <strong>suite bundle for $99</strong> &mdash; bought separately that's $155, so the
      bundle pays for itself once you need two or three of them.</p>
      <p><strong>Pay-what-you-want</strong> is available on the flagship tool and the bundle, with a real
      floor ($49 for the bundle). <strong>Students</strong> pay a reduced price on any tool or the suite
      ($15 / $39) &mdash; a .edu address or a photo of a student ID is enough. <strong>Genuine hardship:</strong>
      email us and tell us what you're making &mdash; no form, no means-testing, a human reply.</p>
      <p><strong>What happens when union rates update?</strong> A new dated Edition ships as a separate,
      low-cost upgrade ($15 single tool / $39 suite) for owners of the immediately prior Edition. Your current
      Edition keeps working regardless.</p>

      <h2>Festival partners</h2>
      <p><strong>Are you affiliated with any festivals?</strong> We're building relationships with a small
      number of festivals to offer their filmmakers a discount on the suite. If your festival is interested in
      partnering, email <a href="mailto:hello@slateandledger.net">hello@slateandledger.net</a>.</p>

      <h2>Micro-Budget Film Budget Builder</h2>
      <p><strong>Do I still need Movie Magic Budgeting?</strong> No &mdash; built to replace it at this budget
      size. <strong>Non-union?</strong> Every tier has a Non-Union path. More on the
      <a href="products/micro-budget-film-budget-builder.html">product page</a>.</p>

      <h2>Episodic Series Budget Builder</h2>
      <p><strong>Is this just the film tool with an episode counter?</strong> No &mdash; per-episode/season
      cost modeling and the per-episode tier-cap check are genuinely episodic concerns a single-project tool
      can't represent. More on the <a href="products/episodic-series-budget-builder.html">product page</a>.</p>

      <h2>Schedule Builder</h2>
      <p><strong>Does it read a PDF script?</strong> No, on purpose &mdash; .fdx and Fountain parse reliably;
      a PDF breakdown is always a rough guess. <strong>Will Auto-arrange give a perfect schedule?</strong> No
      &mdash; it's a reviewable first pass, not a final answer. More on the
      <a href="products/schedule-builder.html">product page</a>.</p>

      <h2>Paperwork Tracker (+ the Filler)</h2>
      <p><strong>Does this file anything for me?</strong> No &mdash; it fills and generates the paperwork; you
      (or your Business Representative, or the union's own portal) still submit it. More on the
      <a href="products/paperwork-tracker.html">product page</a> or the <a href="help.html">Help</a> page.</p>

      <h2>Residuals &amp; Self-Distribution Revenue Tracker</h2>
      <p><strong>Do I need this if I already bought a budget builder?</strong> Only if you want to model what
      the film earns after release &mdash; it's a genuinely separate calculation. More on the
      <a href="products/residuals-revenue-tracker.html">product page</a>.</p>

      <p style="text-align:center; margin-top:34px">Question not answered here? Check the
      <a href="help.html">Help</a> page, or email
      <a href="mailto:hello@slateandledger.net">hello@slateandledger.net</a>.</p>

      {footer()}
    </div>
  </div>
</body>
</html>
"""
with open(os.path.join(OUT_DIR, "faq.html"), "w") as f:
    f.write(faq_html)
print("faq.html written")

terms_html = f"""<!DOCTYPE html>
<html lang="en">
{head("Terms of Sale — Slate & Ledger", "The Slate & Ledger Terms of Sale.")}
<body style="--bg-image:url('img/bg-filmset.jpg')">
  <div class="fade-1">{brandline(current="terms")}</div>
  <div class="wrap">
    <h1 class="page-title fade-1">Terms of Sale</h1>

    <div class="fade-3 prose">
      <p style="text-align:center; color:var(--text-faint)">The Allerick Dynasty Inc. (an S corporation formed in
      California) &mdash; effective date to be set at launch. Applies to all Slate &amp; Ledger products
      (the Digital Indie Film Desk product line) unless a specific product states otherwise.</p>

      <h2>1. What you're buying</h2>
      <p>A digital spreadsheet/software product delivered as a file download. You're purchasing a
      <strong>license to use</strong> the product, not the underlying design, formulas, structure, or content.</p>

      <h2>2. License grant &mdash; what you may do</h2>
      <p>Use the product for your own film, video, or television productions, including commercial
      productions. Edit, customize, and fill it in with your own production's data. Make personal backup
      copies. Share a completed budget or filled-in output with your own collaborators, investors, or team as
      part of running your production.</p>

      <h2>3. What you may not do</h2>
      <p>Without separate written permission: resell, redistribute, sublicense, or give away the product
      itself (the blank/unfilled template, or any substantial copy of its structure, formulas, or design) to
      any third party, for money or for free. Use the product, or any substantial part of its structure,
      formulas, or content, to build, train, or offer a competing commercial product or service. Remove or
      obscure any branding or license notice. Claim authorship of the product as your own.</p>
      <p>Each license is for one purchaser's own productions. Want multiple people using it independently
      across different productions? Contact us about a multi-seat license.</p>

      <h2>4. No professional advice</h2>
      <p>Slate &amp; Ledger products provide research and planning estimates only. They are not legal,
      financial, tax, or production advice, and do not guarantee accuracy for any specific production. Always
      confirm current requirements directly with the relevant union, guild, government agency, or a qualified
      entertainment attorney or accountant before relying on any figure for a real production.</p>

      <h2>5. No warranty</h2>
      <p>Provided "as is" and "as available," without warranty of any kind, express or implied.</p>

      <h2>6. Limitation of liability</h2>
      <p>To the maximum extent permitted by law, The Allerick Dynasty Inc. is not liable for any direct, indirect,
      incidental, special, consequential, or exemplary damages arising from the purchase or use of a Slate
      &amp; Ledger product. <strong>Total liability for any claim is limited to the amount actually paid for
      that product.</strong></p>

      <h2>7. Refunds</h2>
      <p>Digital goods &mdash; no refunds once downloaded, except for a broken file we can't fix. Email us
      and we'll make it right.</p>

      <h2>8. Editions and updates</h2>
      <p>Each product is sold as a dated Edition. Your purchase is a one-time purchase of that Edition: yours
      to keep and use offline indefinitely, not a subscription. Corrections within an Edition are free to
      that Edition's owners. A new Edition (e.g. a renegotiated union agreement) is a separate purchase, at a
      reduced upgrade price for owners of the immediately prior Edition where offered. Your existing Edition
      keeps working regardless.</p>

      <h2>9. Changes to these terms</h2>
      <p>We may update these Terms of Sale from time to time. The version in effect at the time of your
      purchase applies to that purchase.</p>

      <h2>10. Governing law</h2>
      <p>These terms are governed by the laws of the State of California, without regard to conflict-of-law
      principles.</p>

      <h2>11. Contact</h2>
      <p>Questions about these terms, licensing, or a refund: <a href="mailto:hello@slateandledger.net">hello@slateandledger.net</a>.</p>

      <div class="callout">This page is a first draft, not a substitute for review by a qualified attorney
      before relying on it for real commercial sales at volume.</div>

      {footer()}
    </div>
  </div>
</body>
</html>
"""
with open(os.path.join(OUT_DIR, "terms.html"), "w") as f:
    f.write(terms_html)
print("terms.html written")

contact_html = f"""<!DOCTYPE html>
<html lang="en">
{head("Contact — Slate & Ledger", "Get in touch with Slate & Ledger.")}
<body style="--bg-image:url('img/bg-filmset.jpg')">
  <div class="fade-1">{brandline(current="contact")}</div>
  <div class="wrap">
    <h1 class="page-title fade-1">Contact</h1>

    <div class="fade-3">
      <div class="contact-block">
        <a class="email" href="mailto:hello@slateandledger.net">hello@slateandledger.net</a>
      </div>
      <div class="prose">
        <p style="text-align:center">Questions about a product, a licensing question, a refund, or which
        tool is right for your production &mdash; that's what this address is for. A real person reads every
        one.</p>
        <div class="callout" style="text-align:center">Money genuinely tight? Email us and tell us what
        you're making. No form, no means-testing &mdash; just tell us the truth and we'll work something out.</div>
      </div>
      {footer()}
    </div>
  </div>
</body>
</html>
"""
with open(os.path.join(OUT_DIR, "contact.html"), "w") as f:
    f.write(contact_html)
print("contact.html written")

print("Done.")
