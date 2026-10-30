"""High.School build kit: page template + reusable components.

All internal links in content use the token "@@/" for the site root; the
builder rewrites it to the correct relative prefix for each page so the
site works on GitHub Pages project URLs and on the custom domain.
"""
import html, json, os, datetime
from urllib.parse import quote

BASE_URL = "https://high.school"
SITE = "High.School"
PUB = "ca-pub-6620975821265271"
ADSENSE = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?'
           'client=ca-pub-6620975821265271" crossorigin="anonymous"></script>')
# Manual ad units: add slot IDs from AdSense to enable in-content units.
# Until then the site runs on Auto ads (the script above, on every page).
AD_SLOTS = {"in_article": "", "multiplex": ""}
PARTNER_URL = "https://web.works/contact"
TODAY = datetime.date.today()
UPDATED = TODAY.strftime("%B %Y")
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = []  # registry for sitemap + search
JK = False   # Jekyll mode: shared chrome emitted as {% include %} tags (GitHub Pages builds them)
import re as _re

e = html.escape


def root_prefix(path):
    p = path.strip("/")
    return "./" if not p else "../" * (p.count("/") + 1)


# ---------------------------------------------------------------- components
def video(vid, title, channel="", cat=""):
    t = e(title)
    return (f'<div class="video-card" data-cat="{cat}"><div class="video" data-yt="{vid}" data-title="{t}" tabindex="0" role="button" '
            f'aria-label="Play video: {t}"><img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">'
            f'<span class="play" aria-hidden="true"></span></div><h4>{t}</h4><p>{e(channel)}</p></div>')


def quiz(title, qs):
    out = [f'<div class="quiz" data-quiz><h3>✏️ {e(title)}</h3><p class="muted small">Tap an answer — you’ll see the explanation instantly.</p>']
    for i, (q, opts, ans, exp) in enumerate(qs, 1):
        out.append(f'<div class="q"><p>{i}. {q}</p>')
        for j, o in enumerate(opts):
            out.append(f'<button type="button"{" data-correct" if j == ans else ""}>{o}</button>')
        out.append(f'<div class="exp">{exp}</div></div>')
    out.append('<p class="score" aria-live="polite">Score: 0 / %d</p></div>' % len(qs))
    return "".join(out)


def faq(items):
    h = "".join(f"<details><summary>{e(q)}</summary><div><p>{a}</p></div></details>" for q, a in items)
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in items]}
    return '<h2 id="faq">Frequently asked questions</h2>' + h, schema


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def ad(kind="in_article"):
    slot = AD_SLOTS.get(kind)
    if not slot:
        return ""
    fmt = 'data-ad-format="autorelaxed"' if kind == "multiplex" else 'data-ad-layout="in-article" data-ad-format="fluid"'
    return (f'<div class="ad-slot"><div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block;text-align:center" '
            f'{fmt} data-ad-client="{PUB}" data-ad-slot="{slot}"></ins><script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script></div>')


LB_T = "Want a personal game plan?"
LB_X = "Tell us your goal and we’ll match you with free resources and vetted tutoring, test-prep or college-counseling options. Takes about 60 seconds."


def lead_band(title=LB_T, text=LB_X, need="", _q=None):
    if JK and _q is None and title == LB_T and text == LB_X:
        return '{% include leadband.html' + (f' needq="{quote(need)}"' if need else '') + ' %}'
    q = _q if _q is not None else (f"?need={quote(need)}" if need else "")
    return (f'<section><div class="band"><div class="grid g2" style="align-items:center"><div><span class="eyebrow" style="background:#24345e;color:var(--hl)">Free · No obligation</span>'
            f'<h2>{title}</h2><p>{text}</p></div><div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:flex-end">'
            f'<a class="btn btn-primary" href="@@/get-matched/{q}">Get matched free →</a><a class="btn btn-ghost" href="@@/tools/">Try the free tools</a></div></div></div></section>')


def mini_lead(source="Inline", need="Tutoring", _mid=None):
    mid = _mid or _re.sub(r"[^a-z0-9]+", "-", source.lower()).strip("-")
    if JK and _mid is None:
        return f'{{% include minilead.html source="{e(source)}" need="{e(need)}" mid="{mid}" %}}'
    if _mid is not None:
        es, en = source, need
    else:
        es, en = e(source), e(need)
    return f'''<div class="lead-box"><h4>Get a free match</h4><p>Tutoring, test prep, college counseling or online-diploma advice — matched to your goal.</p>
<form class="form" data-form data-thanks="thank-you/"><input type="hidden" name="_subject" value="New High.School lead — {es}"><input type="hidden" name="Lead source" value="{es}">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="field"><label for="ml-{mid}-n">Name</label><input id="ml-{mid}-n" type="text" name="Name" required autocomplete="name"></div>
<div class="field"><label for="ml-{mid}-e">Email</label><input id="ml-{mid}-e" type="email" name="Email" required autocomplete="email"></div>
<div class="field"><label for="ml-{mid}-r">I am</label><select id="ml-{mid}-r" name="I am" required><option value="">Choose…</option><option>Parent / guardian</option><option>Student 13–17</option><option>Adult learner 18+</option><option>Educator</option><option>Under 13</option></select></div>
<div class="field"><label for="ml-{mid}-i">I need help with</label><select id="ml-{mid}-i" name="I need"><option>{en}</option><option>Tutoring</option><option>Test prep (SAT/ACT/AP)</option><option>College counseling</option><option>Online diploma / credit recovery</option><option>Scholarship alerts</option></select></div>
<label class="check"><input type="checkbox" name="Consent" value="Yes" required> <span>I agree to be contacted about my request. Students under 18: a parent/guardian has approved this.</span></label>
<button class="btn btn-primary btn-block" type="submit">Send my request</button><p class="form-status" aria-live="polite"></p></form></div>'''


def aside(links, source="Sidebar", need="Tutoring"):
    lis = "".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in links)
    return (f'<aside><div class="aside-sticky"><div class="aside-box"><h4>Related on High.School</h4><ul>{lis}</ul></div>'
            f'{mini_lead(source, need)}<div class="aside-box"><h4>❤️ Keep High.School free</h4><p class="small muted">We’re reader-supported. A small gift funds new guides, tools and student contests.</p>'
            f'<a class="btn btn-hl btn-sm" href="@@/support/">Support us</a></div></div></aside>')


def page_hero(title, sub="", crumbs=None, meta=True, eyebrow=""):
    cr = ""
    if crumbs:
        parts = ['<a href="@@/">Home</a>'] + [f'<a href="{u}">{e(t)}</a>' if u else f'<span aria-current="page">{e(t)}</span>' for t, u in crumbs]
        cr = '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(parts) + '</nav>'
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    ml = f'<div class="meta-line"><span>📅 Updated {UPDATED}</span><span>✍️ High.School Editorial Team</span><span>✅ <a href="@@/editorial-policy/">Editorial policy</a></span></div>' if meta else ""
    return f'<header class="page-hero"><div class="wrap">{cr}{eb}<h1>{title}</h1>' + (f'<p class="lead">{sub}</p>' if sub else "") + ml + '</div></header>'


def article(title, sub, crumbs, body, links, source, need="Tutoring", eyebrow=""):
    return page_hero(title, sub, crumbs, eyebrow=eyebrow) + f'<div class="wrap"><div class="layout"><article class="prose">{body}</article>{aside(links, source, need)}</div></div>'


# ---------------------------------------------------------------- chrome
NAV = [
    ("Study", [("📐 Math", "study/math/", "Algebra → Calculus"), ("🧬 Biology", "study/biology/", "Cells, genetics, ecology"),
               ("⚗️ Chemistry", "study/chemistry/", "Atoms, reactions, moles"), ("🧲 Physics", "study/physics/", "Motion, energy, waves"),
               ("📚 English", "study/english/", "Reading, writing, essays"), ("🏛️ History", "study/history/", "World & US history"),
               ("⚖️ Government & Economics", "study/government-economics/", "Civics, micro, macro"), ("💻 Computer Science", "study/computer-science/", "Coding & CS principles"),
               ("🧠 Psychology", "study/psychology/", "Mind & behavior"), ("🌍 World Languages", "study/world-languages/", "Spanish, French & more"),
               ("🗂️ All subjects", "study/", "Study hub")]),
    ("Test Prep", [("📝 SAT", "test-prep/sat/", "Digital SAT guide"), ("🧾 ACT", "test-prep/act/", "Enhanced ACT guide"), ("🎓 AP Exams", "test-prep/ap/", "Advanced Placement"),
                   ("🌐 IB Diploma", "test-prep/ib/", "International Baccalaureate"), ("🏅 PSAT/NMSQT", "test-prep/psat/", "National Merit"), ("⚔️ SAT vs ACT", "test-prep/sat-vs-act/", "Which test + quiz"),
                   ("🗂️ All test prep", "test-prep/", "Hub")]),
    ("Tools", [("🧮 GPA Calculator", "tools/gpa-calculator/", "Weighted & cumulative"), ("🎯 Final Grade Calculator", "tools/final-grade-calculator/", "What do I need?"),
               ("📊 Grade Calculator", "tools/grade-calculator/", "Weighted categories"), ("🔁 SAT ↔ ACT Converter", "tools/sat-act-converter/", "Official concordance"),
               ("💸 College Cost Calculator", "tools/college-cost-calculator/", "Savings & gap"), ("✅ Credit Tracker", "tools/credit-tracker/", "Graduation progress"),
               ("⏱️ Study Timer", "tools/study-timer/", "Pomodoro focus"), ("🃏 Flashcards", "tools/flashcards/", "Make & study decks"), ("🗂️ All tools", "tools/", "Tool hub")]),
    ("College", [("🗺️ 4-Year Roadmap", "college/roadmap/", "Grade 9–12 checklist"), ("📮 Applications", "college/applications/", "Timeline & strategy"),
                 ("✍️ College Essays", "college/essays/", "Personal statement"), ("💵 Financial Aid & FAFSA", "college/financial-aid/", "Grants, loans, SAI"),
                 ("🏆 Scholarships", "college/scholarships/", "Find + track"), ("🧭 Majors & Careers", "college/majors-careers/", "Explore paths"), ("🗂️ College hub", "college/", "Hub")]),
]


def header():
    items = []
    for label, links in NAV:
        dd = "".join(f'<a href="@@/{u}"><b>{e(t)}<span>{e(s)}</span></b></a>' for t, u, s in links)
        items.append(f'<li><button type="button" aria-expanded="false" aria-haspopup="true">{label} ▾</button><div class="dropdown">{dd}</div></li>')
    items.append('<li><a href="@@/online-high-school/">Online School</a></li><li><a href="@@/videos/">Videos</a></li><li><a href="@@/guides/">Guides</a></li>')
    drawer = "".join(f"<h4>{label}</h4>" + "".join(f'<a href="@@/{u}">{e(t)}</a>' for t, u, s in links) for label, links in NAV)
    drawer += ('<h4>More</h4><a href="@@/online-high-school/">Online High School</a><a href="@@/videos/">Video Library</a><a href="@@/guides/">Guides</a>'
               '<a href="@@/contests/">Contests</a><a href="@@/support/">Support Us</a><a href="@@/join/">Join the Team</a><a href="@@/partner/">Advertise & Partner</a><a href="@@/contact/">Contact</a>'
               '<p style="margin-top:16px"><a class="btn btn-primary btn-block" href="@@/get-matched/" style="color:#fff;border:0">Get matched free</a></p>')
    logo = ('<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="2" width="36" height="36" rx="10" fill="#14213d"/><path d="M11 12v16M11 20h9M20 12v16" stroke="#ffd84d" stroke-width="3.4" stroke-linecap="round"/>'
            '<circle cx="28" cy="26.5" r="2.6" fill="#ff5a4e"/></svg>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note">📣 <a href="{PARTNER_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-header"><div class="wrap nav"><a class="brand" href="@@/" aria-label="High.School home">{logo}<span>High<span class="brand-dot">.</span>School</span></a>
<nav aria-label="Main"><ul class="menu">{"".join(items)}</ul></nav>
<div class="nav-actions"><a class="icon-btn" href="@@/search/" aria-label="Search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></a>
<button class="icon-btn" type="button" data-theme-toggle aria-label="Toggle dark mode"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
<a class="btn btn-primary btn-sm" href="@@/get-matched/">Get matched</a>
<button class="icon-btn burger" type="button" data-drawer aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div></div></header>
<div class="drawer" id="drawer"><div class="drawer-panel" role="dialog" aria-label="Menu"><button class="icon-btn" type="button" data-drawer aria-label="Close menu" style="float:right">✕</button><a class="brand" href="@@/">High<span class="brand-dot">.</span>School</a>{drawer}</div></div>'''


def footer():
    cols = [
        ("Learn", [("Study Hub", "study/"), ("Test Prep", "test-prep/"), ("Video Library", "videos/"), ("Guides", "guides/"), ("Online High School", "online-high-school/"), ("Parents", "guides/parent-guide/"), ("Educators", "guides/teacher-resources/")]),
        ("Tools", [("GPA Calculator", "tools/gpa-calculator/"), ("Final Grade Calculator", "tools/final-grade-calculator/"), ("SAT ↔ ACT Converter", "tools/sat-act-converter/"), ("College Cost Calculator", "tools/college-cost-calculator/"), ("Study Timer", "tools/study-timer/"), ("Flashcards", "tools/flashcards/")]),
        ("Get involved", [("Get Matched", "get-matched/"), ("Contests & Prizes", "contests/"), ("Support Us", "support/"), ("Join the Team", "join/"), ("Advertise & Partner", "partner/"), ("Contact", "contact/")]),
        ("Company", [("About", "about/"), ("Editorial Policy", "editorial-policy/"), ("Privacy Policy", "privacy/"), ("Terms of Use", "terms/"), ("Cookie Policy", "cookies/"), ("Disclaimer", "disclaimer/"), ("Trademark & Copyright", "trademark-disclosure/"), ("Accessibility", "accessibility/")]),
    ]
    c = "".join(f'<div><h4>{h}</h4><ul>' + "".join(f'<li><a href="@@/{u}">{e(t)}</a></li>' for t, u in ls) + '</ul></div>' for h, ls in cols)
    return f'''<footer class="site-footer"><div class="wrap"><div class="foot-grid"><div><div class="foot-brand">High<span style="color:var(--coral)">.</span>School</div>
<p>The free, independent command center for high school — study guides, test prep, tools, college and diploma pathways for students, parents, adult learners and educators.</p>
<form class="news" data-form data-ok="You’re in! Watch your inbox for the Weekly Study Pack."><input type="hidden" name="_subject" value="Newsletter signup — High.School"><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="sr-only" for="news-email">Email</label><input id="news-email" type="email" name="Email" placeholder="Your email for the Weekly Study Pack" required><button class="btn btn-hl btn-sm" type="submit">Join</button></form><p class="form-status small" aria-live="polite"></p>
<p class="small">1 email a week. Unsubscribe anytime. Ages 13+.</p></div>{c}</div>
<div class="disclosure"><p><strong>Trademark & copyright disclosure:</strong> High.School is an independent educational resource. “High school” is used in its ordinary, descriptive sense; we claim no trademark rights in the generic term and are not affiliated with, endorsed by, or representing any school, district, school board, testing organization or government agency. SAT®, AP® and PSAT/NMSQT® are trademarks registered by the College Board; ACT® is a registered trademark of ACT Education Corp.; IB and International Baccalaureate are trademarks of the International Baccalaureate Organization; National Merit® is a trademark of NMSC. None of these organizations sponsor or endorse this site. Embedded videos are played through YouTube’s official player and remain the property of their creators. All other content © <span data-year>2026</span> High.School. See our <a href="@@/trademark-disclosure/">full disclosure</a>.</p>
<p>Advertising: this site shows ads served by Google and may earn referral fees from some partners; this never changes our editorial content. Information is educational and not professional, legal or financial advice — always confirm requirements with your school, district or the official testing body.</p>
<p>© <span data-year>2026</span> High.School · <a href="{PARTNER_URL}" target="_blank" rel="noopener">Domain, sponsorship & partnership inquiries</a></p></div></div></footer>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie notice"><strong>🍪 Cookies & ads</strong><p style="margin:.4em 0 0">We use cookies to run the site, measure traffic and show ads from Google, which may be personalized. See our <a href="@@/cookies/">Cookie Policy</a> and <a href="@@/privacy/">Privacy Policy</a>.</p>
<div class="btns"><button class="btn btn-ink btn-sm" type="button" data-consent="accept">Accept all</button><button class="btn btn-ghost btn-sm" type="button" data-consent="reject">Non-personalized only</button></div></div>
<div class="slidein" id="slidein" role="dialog" aria-label="Free match offer"><button class="x" type="button" aria-label="Close">×</button><h4>Need a hand this semester? 🎒</h4><p class="small muted">Get a free, no-obligation match for tutoring, test prep or college help.</p>
<form class="form" data-form data-thanks="thank-you/"><input type="hidden" name="_subject" value="New High.School lead — Slide-in"><input type="hidden" name="Lead source" value="Slide-in"><input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label class="sr-only" for="si-e">Email</label><input id="si-e" type="email" name="Email" placeholder="Email" required>
<label class="sr-only" for="si-r">I am</label><select id="si-r" name="I am" required><option value="">I am a…</option><option>Parent / guardian</option><option>Student 13–17</option><option>Adult learner 18+</option><option>Educator</option><option>Under 13</option></select>
<label class="check"><input type="checkbox" name="Consent" value="Yes" required><span class="small">OK to contact me. Under 18? A parent/guardian approved.</span></label>
<button class="btn btn-primary btn-block btn-sm" type="submit">Get my free match</button><p class="form-status small" aria-live="polite"></p></form></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>'''


NOADS = "<!-- AdSense intentionally omitted: no-content utility page (AdSense policy) -->"


def head_static(ads=True, _tpl=False):
    if JK and not _tpl:
        return '{% include head.html' + ('' if ads else ' ads="0"') + ' %}'
    adtag = ('{% if include.ads == "0" %}' + NOADS + '{% else %}' + ADSENSE + '{% endif %}') if _tpl else (ADSENSE if ads else NOADS)
    return f'''<meta name="theme-color" content="#14213d">
<meta name="google-adsense-account" content="{PUB}">
<link rel="icon" href="@@/assets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="@@/assets/img/icon-192.png"><link rel="manifest" href="@@/manifest.webmanifest">
<script>try{{var t=localStorage.getItem('hs-theme');if(t)document.documentElement.setAttribute('data-theme',t);if(localStorage.getItem('hs-consent')==='reject'){{(window.adsbygoogle=window.adsbygoogle||[]).requestNonPersonalizedAds=1}}}}catch(e){{}}</script>
{adtag}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="@@/assets/css/site.css">'''


# ---------------------------------------------------------------- page writer
def page(path, title, desc, body, crumbs=None, schema=None, keywords="", tools=False, noslide=False, index=True, og_type="website", full_title=None, ads=True):
    R = root_prefix(path)
    base_js = ""
    if path == "404.html":  # served at any depth: resolve links from a runtime <base>
        R = ""
        base_js = "<script>document.write('<base href=\"'+(location.hostname.indexOf('github.io')>-1?'/'+location.pathname.split('/')[1]+'/':'/')+'\">')</script>"
    url = BASE_URL + "/" + path.strip("/") + ("/" if path.strip("/") else "")
    if path.endswith(".html"):
        url = BASE_URL + "/" + path
    ft = full_title or (f"{title} | {SITE}" if title != SITE else f"{SITE} — Study Guides, Test Prep, GPA Tools & College Planning")
    schemas = []
    if crumbs is not None:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"}]
        for i, (t, u) in enumerate(crumbs, 2):
            items.append({"@type": "ListItem", "position": i, "name": t, "item": (BASE_URL + "/" + u.replace("@@/", "")) if u else url})
        schemas.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if schema:
        schemas += schema if isinstance(schema, list) else [schema]
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = "index,follow,max-image-preview:large" if index else "noindex,follow"
    tools_js = '<script src="@@/assets/js/pay-config.js" defer></script><script src="@@/assets/js/tools.js" defer></script>' if tools else ""
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
{base_js}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(ft)}</title>
<meta name="description" content="{e(desc)}">
{f'<meta name="keywords" content="{e(keywords)}">' if keywords else ''}
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{SITE}"><meta property="og:title" content="{e(ft)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE_URL}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(ft)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{BASE_URL}/assets/img/og.png">
{head_static(ads)}
{ld}
</head>
<body data-root="{R}"{' data-noslide' if noslide else ''}>
{"{% include header.html %}" if JK else header()}
<main id="main">
{body}
</main>
{"{% include footer.html %}" if JK else footer()}
<script src="@@/assets/js/site.js" defer></script>{tools_js}
</body>
</html>'''
    doc = doc.replace("@@/", R)
    if JK:
        doc = f'---\nr: "{R}"\n---\n' + doc
    fp = os.path.join(OUT, path) if path.endswith(".html") else os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(doc)
    if index:
        PAGES.append({"u": path.strip("/") + ("/" if path.strip("/") and not path.endswith(".html") else ""), "t": title, "d": desc, "k": keywords, "loc": url})
    return fp


def write_includes(outdir):
    """Write Jekyll _includes for JK mode (shared chrome, rendered by GitHub Pages)."""
    d = os.path.join(outdir, "_includes")
    os.makedirs(d, exist_ok=True)
    global JK
    was, JK = JK, False
    parts = {
        "header.html": header(),
        "footer.html": footer(),
        "head.html": head_static(True, _tpl=True),
        "minilead.html": mini_lead("{{ include.source }}", "{{ include.need }}", "{{ include.mid }}"),
        "leadband.html": lead_band(_q="{% if include.needq %}?need={{ include.needq }}{% endif %}"),
    }
    JK = was
    for n, t in parts.items():
        with open(os.path.join(d, n), "w", encoding="utf-8") as f:
            f.write(t.replace("@@/", "{{ page.r }}"))
