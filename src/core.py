"""Home, Get Matched, Online High School, Videos, About, Contact, Search, Thank-you, 404."""
from kit import page, page_hero, article, faq, ad, lead_band, video, e, BASE_URL, PARTNER_URL
from subjects import SUBJECTS, V, vids
from tools import TOOLS

HP = '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'
ROLES = [("🎒", "Student 13–17"), ("👪", "Parent / guardian"), ("🎓", "Adult learner 18+"), ("🍎", "Educator"), ("🧒", "Under 13")]
NEEDS = [("📘", "Tutoring"), ("📝", "Test prep (SAT/ACT/AP)"), ("🧭", "College counseling"), ("💻", "Online diploma / credit recovery"), ("🏆", "Scholarship alerts"), ("✍️", "Essay coaching"), ("☀️", "Summer programs")]


def opt(name, items, kind="radio", req=False):
    return "".join(f'<label class="option"><input type="{kind}" name="{name}" value="{e(v)}"{" required" if req and kind == "radio" else ""}><span><i>{i}</i>{e(v)}</span></label>' for i, v in items)


def stepper(subject, source, steps_extra, need_items=NEEDS, heading="Get matched in about 60 seconds"):
    return f'''<form class="stepper" data-form data-stepper data-thanks="thank-you/" novalidate><input type="hidden" name="_subject" value="{e(subject)}"><input type="hidden" name="Lead source" value="{e(source)}">{HP}
<div class="step-count">Step 1 of 4</div><div class="progress" aria-hidden="true"><i></i></div><h2 style="margin-top:6px">{heading}</h2>
<div class="step"><p class="legend">Who are you?</p><div class="option-grid" data-require-one="Please choose who you are.">{opt("I am", ROLES, req=True)}</div><p class="small muted" style="margin-top:10px">Under 13? Please ask a parent or guardian to fill this in for you.</p></div>
<div class="step"><p class="legend">What do you need? <span class="muted small">(choose all that apply)</span></p><div class="option-grid" data-require-one="Choose at least one option.">{opt("I need", need_items, "checkbox")}</div></div>
<div class="step">{steps_extra}</div>
<div class="step"><div class="row2"><div class="field"><label for="gm-name">Full name</label><input id="gm-name" name="Name" type="text" required autocomplete="name"></div><div class="field"><label for="gm-email">Email</label><input id="gm-email" name="Email" type="email" required autocomplete="email"></div></div>
<div class="row2"><div class="field"><label for="gm-phone">Phone <span class="muted">(optional)</span></label><input id="gm-phone" name="Phone" type="tel" autocomplete="tel"><small>Only if you’d like a call or text back.</small></div><div class="field"><label for="gm-time">Best time to reach you</label><select id="gm-time" name="Best time"><option>Any time</option><option>Weekday mornings</option><option>Weekday afternoons</option><option>Weekday evenings</option><option>Weekends</option></select></div></div>
<div class="field"><label for="gm-msg">Anything else? <span class="muted">(optional)</span></label><textarea id="gm-msg" name="Message" placeholder="Goals, current grades or scores, deadlines, learning needs…"></textarea></div>
<label class="check" data-minor-wrap style="display:none"><input type="checkbox" name="Guardian approval" value="Yes" data-minor-check><span><strong>I’m 13–17 and my parent/guardian has approved this request.</strong> We’ll include them in any follow-up.</span></label>
<label class="check"><input type="checkbox" name="Consent" value="Yes" required><span>I agree that High.School and, with my request, a matched partner may contact me by email (and phone/text if provided) about this request. Consent is not a condition of any purchase. See our <a href="@@/privacy/">Privacy Policy</a>.</span></label>
<button class="btn btn-primary btn-block" type="submit">Get my free match →</button><p class="form-status" aria-live="polite"></p></div>
<div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-ink" data-next>Continue →</button></div>
<div class="trust"><span>Free</span><span>No obligation</span><span>No spam — unsubscribe anytime</span><span>We never sell minors’ data</span></div></form>'''


def build():
    # ------------------------------------------------------------ HOME
    from kit import NAV
    tag = {u: sub for _, u, sub in NAV[0][1]}
    subj = "".join(f'<a class="card" href="@@/study/{s["slug"]}/"><div class="ico">{s["emoji"]}</div><h3>{s["name"]}</h3><p>{e(tag.get("study/" + s["slug"] + "/", ""))} · guide, videos & quiz</p></a>' for s in SUBJECTS[:8])
    tools = "".join(f'<a class="card" href="@@/tools/{s}/"><div class="ico t">{i}</div><h3>{t}</h3><p>{d}</p></a>' for s, i, t, d in TOOLS[:4])
    vrow = '<div class="grid g4">' + "".join(video(*V[k]) for k in ["calc", "chem", "lit", "practice"]) + "</div>"
    fq, fs = faq([
        ("Is High.School free?", "Yes. Every guide, tool, quiz and video page is free. We’re supported by advertising, optional partner referrals and reader donations."),
        ("Who is High.School for?", "Students aged 13+, parents and guardians, adult learners finishing a diploma, and teachers and counselors."),
        ("Is High.School a school?", "No. High.School is an independent educational resource. We don’t grant diplomas or credits; our guides help you choose accredited programs and succeed in your own school."),
        ("How does “Get Matched” work?", "Tell us your goal in four quick steps. We reply with free resources and, if you want, introductions to vetted tutoring, test-prep, counseling or online-school options. No obligation.")])
    home = f'''<section class="hero"><div class="wrap hero-grid"><div><span class="eyebrow">Free for every student · Parents · Adult learners</span>
<h1>Everything high school, <mark>in&nbsp;one&nbsp;place.</mark></h1>
<p class="lead">Study guides for every subject, SAT/ACT/AP prep, a free GPA calculator and 7 more tools, college & scholarship planning, and honest advice on online diplomas — all free, all in plain English.</p>
<form class="searchbar" data-search role="search"><label class="sr-only" for="hero-q">Search High.School</label><input id="hero-q" type="search" placeholder="Try “weighted GPA”, “SAT vs ACT”, “FAFSA”…"><button class="btn btn-primary" type="submit">Search</button></form>
<div class="chips"><a class="chip" href="@@/tools/gpa-calculator/">🧮 Calculate my GPA</a><a class="chip" href="@@/tools/final-grade-calculator/">🎯 What do I need on my final?</a><a class="chip" href="@@/test-prep/sat-vs-act/">⚔️ SAT or ACT?</a><a class="chip" href="@@/college/scholarships/">🏆 Find scholarships</a><a class="chip" href="@@/online-high-school/">💻 Online diploma options</a><a class="chip" href="@@/get-matched/?need=Tutoring">📘 Get a tutor</a></div></div>
<div><div class="hero-card" aria-hidden="true"><div class="small muted">Your semester at a glance</div><div style="display:flex;align-items:end;gap:14px;margin:6px 0 10px"><span class="big">3.86</span><span class="muted">weighted GPA</span></div>
<div class="row"><span>AP Biology</span><b>A− · 4.7</b></div><div class="row"><span>Honors English 10</span><b>A · 4.5</b></div><div class="row"><span>Algebra II</span><b>B+ · 3.3</b></div><div class="row"><span>US History</span><b>A · 4.0</b></div><div class="row" style="border:0"><span>Final exam needed (Algebra II → A−)</span><b style="color:var(--coral)">94%</b></div></div>
<div class="sticky-note">Weighted GPA counts AP as +1.0 ✏️</div></div></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="grid g4">
<a class="card" href="@@/study/"><div class="ico">🎒</div><h3>I’m a student</h3><p>Study guides, practice quizzes, test prep and tools that make the semester easier.</p></a>
<a class="card" href="@@/guides/parent-guide/"><div class="ico c">👪</div><h3>I’m a parent</h3><p>How grades, credits and college costs work — and how to help without pressure.</p></a>
<a class="card" href="@@/online-high-school/"><div class="ico v">🎓</div><h3>I’m an adult learner</h3><p>Finish your diploma online, compare GED vs diploma, and avoid diploma mills.</p></a>
<a class="card" href="@@/guides/teacher-resources/"><div class="ico t">🍎</div><h3>I’m an educator</h3><p>Free classroom-ready tools, quizzes and counseling resources.</p></a></div></div></section>
<section><div class="wrap"><div class="stats"><div class="stat"><b>10</b><span>subject study guides</span></div><div class="stat"><b>8</b><span>free calculators & tools</span></div><div class="stat"><b>50</b><span>practice questions with explanations</span></div><div class="stat"><b>15.6M</b><span>US public high school students (NCES, fall 2023)</span></div></div></div></section>
<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">Free tools</span><h2>The calculators students actually use</h2></div><a class="btn btn-ghost btn-sm" href="@@/tools/">All 8 tools →</a></div><div class="grid g4">{tools}</div></div></section>
<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">Study Hub</span><h2>Pick a subject</h2></div><a class="btn btn-ghost btn-sm" href="@@/study/">All subjects →</a></div><div class="grid g4">{subj}</div></div></section>
<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">Plan ahead</span><h2>Your 4-year roadmap</h2></div><a class="btn btn-ghost btn-sm" href="@@/college/roadmap/">Open the interactive checklist →</a></div>
<div class="roadmap"><div class="grade"><h3>9th</h3><p class="small">Build habits, explore activities, learn graduation requirements.</p></div><div class="grade"><h3>10th</h3><p class="small">Take rigorous classes, try a practice SAT/ACT, explore careers.</p></div><div class="grade"><h3>11th</h3><p class="small">PSAT/NMSQT, SAT/ACT, AP/IB, build your college list.</p></div><div class="grade"><h3>12th</h3><p class="small">FAFSA, applications, scholarships, decide by May 1.</p></div></div></div></section>
<section><div class="wrap"><div class="band"><div class="grid g2" style="align-items:center"><div><span class="eyebrow" style="background:#24345e;color:var(--hl)">Get Matched · Free</span><h2>Your goal + the right help, in 60 seconds</h2>
<ol style="color:#c9d0e2;padding-left:1.2em"><li><strong style="color:#fff">Tell us who you are</strong> — student, parent, adult learner or educator.</li><li><strong style="color:#fff">Pick what you need</strong> — tutoring, test prep, college counseling, online diploma, scholarships.</li><li><strong style="color:#fff">Get your match</strong> — free resources plus vetted options, with no obligation.</li></ol></div>
<div style="text-align:right"><a class="btn btn-primary" href="@@/get-matched/">Start my free match →</a><p class="small" style="margin-top:10px;color:#98a3bf">No spam. Under 18? We include your parent/guardian.</p></div></div></div></div></section>
<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">Video library</span><h2>Learn from the best free teachers online</h2></div><a class="btn btn-ghost btn-sm" href="@@/videos/">All videos →</a></div>{vrow}</div></section>
<section><div class="wrap"><div class="grid g3">
<a class="card" href="@@/online-high-school/"><span class="tag hot">Popular</span><h3 style="margin-top:8px">💻 Online high school & diploma completion</h3><p>Tuition-free public options, private schools, credit recovery, GED vs diploma — and how to spot accreditation red flags.</p></a>
<a class="card" href="@@/contests/"><span class="tag new">New</span><h3 style="margin-top:8px">🏆 Student contests & prizes</h3><p>Essay, STEM video, math and design challenges — sponsor-funded prizes. Pre-register now.</p></a>
<a class="card" href="@@/support/"><span class="tag">Community</span><h3 style="margin-top:8px">❤️ Keep High.School free</h3><p>Donations fund new guides, student contests and the team that builds them.</p></a></div></div></section>
<section class="wrap narrow prose">{fq}</section>'''
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "High.School", "url": BASE_URL + "/", "potentialAction": {"@type": "SearchAction", "target": BASE_URL + "/search/?q={search_term_string}", "query-input": "required name=search_term_string"}}
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "High.School", "url": BASE_URL + "/", "logo": BASE_URL + "/assets/img/icon-512.png"}
    page("", "High.School", "Free high school study guides, SAT/ACT/AP prep, GPA calculator and student tools, college and scholarship planning, and online diploma guidance for students, parents and adult learners.", home, None, [site, org, fs], "high school, gpa calculator, study guides, sat prep, act prep, college planning, scholarships, online high school")

    # ------------------------------------------------------------ GET MATCHED
    details = '''<div class="row2"><div class="field"><label for="gm-grade">Current grade / status</label><select id="gm-grade" name="Grade" required><option value="">Choose…</option><option>Grade 9</option><option>Grade 10</option><option>Grade 11</option><option>Grade 12</option><option>Graduated / adult learner</option><option>Middle school (planning ahead)</option><option>Not applicable (educator)</option></select></div>
<div class="field"><label for="gm-subj">Subjects, tests or goals</label><input id="gm-subj" name="Subjects / goals" type="text" placeholder="e.g. Algebra II, SAT 1400, finish diploma"></div></div>
<div class="row2"><div class="field"><label for="gm-when">Timeline</label><select id="gm-when" name="Timeline"><option>As soon as possible</option><option>Within a month</option><option>Next semester</option><option>Just exploring</option></select></div>
<div class="field"><label for="gm-fmt">Preferred format</label><select id="gm-fmt" name="Format"><option>Online</option><option>In person</option><option>Either</option></select></div></div>
<div class="row2"><div class="field"><label for="gm-budget">Budget</label><select id="gm-budget" name="Budget"><option>Free resources only</option><option>Under $40/hour</option><option>$40–$80/hour</option><option>$80+/hour</option><option>Not sure yet</option></select></div>
<div class="field"><label for="gm-country">Country</label><select id="gm-country" name="Country"><option>United States</option><option>Canada</option><option>United Kingdom</option><option>India</option><option>Australia</option><option>Other</option></select></div></div>
<div class="field"><label for="gm-zip">ZIP / postal code <span class="muted">(helps with local and state-specific options)</span></label><input id="gm-zip" name="ZIP / postal" type="text" autocomplete="postal-code"></div>'''
    fq, fs = faq([("Is it really free?", "Yes. Matching is free for students and families. Some partner programs we introduce may charge for their services; you’ll always know before you commit, and there’s never any obligation."),
                  ("Who will contact me?", "A member of the High.School team, and — only for the needs you select — a vetted partner relevant to your request."),
                  ("Do you sell my data?", "No. We never sell personal information, and we never share a minor’s information without a parent/guardian’s approval."),
                  ("How fast will I hear back?", "Typically within 1–2 business days.")])
    body = page_hero("Get Matched — Free Help for Your Goal", "Tutoring, test prep, college counseling, online diplomas or scholarships: answer four quick questions and we’ll match you with free resources and vetted options.", [("Get Matched", "")], meta=False, eyebrow="Free · No obligation · ~60 seconds")
    body += f'''<div class="wrap"><div class="layout"><div>{stepper("New High.School lead — Get Matched", "Get Matched page", details)}</div>
<aside><div class="aside-sticky"><div class="aside-box"><h4>What happens next</h4><ol class="small" style="padding-left:1.1em"><li>We review your request (1–2 business days).</li><li>You get free resources for your goal by email.</li><li>If you want, we introduce up to 3 vetted options.</li><li>You decide — no pressure, no obligation.</li></ol></div>
<div class="aside-box"><h4>Why families use High.School</h4><ul class="small" style="list-style:none;padding:0"><li>✅ Independent — no school or test company owns us</li><li>✅ Free tools and guides first, paid help only if you want it</li><li>✅ Parent/guardian included for students under 18</li></ul></div>
<div class="aside-box"><h4>Prefer to talk business?</h4><p class="small">Schools, tutoring companies and online programs: <a href="@@/partner/">become a partner</a>.</p></div></div></aside></div>
<section class="prose narrow">{fq}</section></div>'''
    page("get-matched/", "Get Matched: Free Tutoring, Test Prep & College Help", "Get a free, no-obligation match for tutoring, SAT/ACT/AP prep, college counseling, online diploma or credit recovery options and scholarship alerts.", body, [("Get Matched", "")], fs, "find a tutor, sat tutor, college counselor, online diploma help", noslide=True)

    # ------------------------------------------------------------ ONLINE HIGH SCHOOL
    od_details = '''<div class="row2"><div class="field"><label for="od-reason">Main reason</label><select id="od-reason" name="Main reason" required><option value="">Choose…</option><option>Credit recovery / catching up</option><option>Flexible schedule (work, family, travel)</option><option>Health or medical needs</option><option>Athlete or performer</option><option>Safety, bullying or a better fit</option><option>Accelerate / graduate early</option><option>Adult — finish my diploma</option></select></div>
<div class="field"><label for="od-type">Program preference</label><select id="od-type" name="Program preference"><option>Not sure — advise me</option><option>Tuition-free public online school</option><option>Private online school</option><option>Adult diploma program</option><option>High school equivalency (GED/HiSET)</option><option>Individual courses only</option></select></div></div>
<div class="row2"><div class="field"><label for="od-grade">Grade level / credits</label><select id="od-grade" name="Grade"><option>Grade 9</option><option>Grade 10</option><option>Grade 11</option><option>Grade 12</option><option>Adult — some credits earned</option><option>Adult — not sure of credits</option></select></div>
<div class="field"><label for="od-state">State / province + ZIP</label><input id="od-state" name="Location" type="text" required placeholder="e.g. Texas 75001"></div></div>
<div class="field"><label for="od-when">When do you want to start?</label><select id="od-when" name="Timeline"><option>This month</option><option>Next semester</option><option>Within 6 months</option><option>Just researching</option></select></div>'''
    od_needs = [("💻", "Online diploma / credit recovery"), ("🎓", "Adult diploma completion"), ("🧾", "GED / HiSET prep"), ("📘", "Tutoring"), ("🧭", "College counseling")]
    fq, fs = faq([("Are online high school diplomas legit?", "Yes — when the school is accredited and recognized by your state. Diplomas from accredited online public and private schools are accepted by colleges, employers and the military. Unaccredited “diploma mills” are not."),
                  ("Is online high school free?", "Many states fund tuition-free public online schools for residents. Private online schools charge tuition."),
                  ("What’s the difference between a GED and a diploma?", "A diploma is awarded by a school after completing required credits. The GED and HiSET are high school equivalency exams that award a state credential. Both are widely accepted, but some employers, colleges and the military have different policies, so check your goals."),
                  ("Can adults earn a real high school diploma online?", "Yes. Many districts, community colleges and accredited private schools run adult diploma programs that credit previous coursework.")])
    body = f'''<p>Online high school has gone mainstream. Students choose it for flexibility, health, athletics, safety, to catch up on credits or to graduate early — and adults use it to finally finish a diploma. The options are good, but quality varies enormously. This guide explains each path and how to choose a legitimate program.</p>
<h2>Your options</h2><table><thead><tr><th>Option</th><th>Cost</th><th>Best for</th></tr></thead><tbody>
<tr><td><strong>Tuition-free public online school</strong></td><td>Free for state residents (state-funded)</td><td>Full-time students who want a public-school diploma from home</td></tr>
<tr><td><strong>District virtual programs</strong></td><td>Usually free</td><td>Staying enrolled with your local district while learning online</td></tr>
<tr><td><strong>Private online high school</strong></td><td>Tuition</td><td>Flexible start dates, self-paced study, international students</td></tr>
<tr><td><strong>Credit recovery</strong></td><td>Free–low cost</td><td>Students who need to retake or catch up on specific courses</td></tr>
<tr><td><strong>Adult diploma programs</strong></td><td>Free–tuition</td><td>Adults completing remaining credits for a real diploma</td></tr>
<tr><td><strong>High school equivalency (GED / HiSET)</strong></td><td>Exam fees</td><td>Adults who want the fastest route to a credential</td></tr></tbody></table>
<h2>How to verify accreditation</h2><ol><li>Check your <strong>state department of education</strong> list of approved online schools.</li><li>Confirm accreditation from a recognized accreditor (for example Cognia, ACS WASC, MSA-CESS, NEASC) on the accreditor’s own website — not just the school’s logo.</li><li>Athletes: confirm courses are approved by the NCAA Eligibility Center.</li><li>Ask whether credits transfer back to a traditional school.</li></ol>
{ad()}
<h2>Diploma-mill red flags</h2><ul><li>“Earn your diploma in days” or diplomas based on “life experience.”</li><li>No real coursework, teachers or proctored assessments.</li><li>Accreditation from organizations you can’t verify.</li><li>Pressure to pay immediately; flat fee for a diploma.</li></ul>
<h2>Is online school right for you?</h2><p>Online learners do best with a consistent daily schedule, a dedicated workspace and regular contact with teachers. Ask any program about live classes, teacher response times, counseling, special-education support, and how students socialize (clubs, field trips, meetups).</p>
<h2 id="advisor">Free online diploma advisor</h2><p>Tell us your situation and we’ll send a short list of options that fit your state, schedule and budget. <strong>Disclosure:</strong> High.School may receive compensation from some partner programs; this never affects our editorial guidance or which programs we include.</p>
{stepper("New High.School lead — Online Diploma Advisor", "Online High School page", od_details, od_needs, "Find the right online option")}'''
    crumbs = [("Online High School", "")]
    html = article("💻 Online High School & Diploma Completion Guide", "Tuition-free public online schools, private programs, credit recovery, adult diplomas and GED vs diploma — plus how to verify accreditation and avoid diploma mills.", crumbs, body + fq,
                   [("Credit Tracker", "@@/tools/credit-tracker/"), ("Parent Guide", "@@/guides/parent-guide/"), ("Financial Aid", "@@/college/financial-aid/"), ("Majors & Careers", "@@/college/majors-careers/")], "Online HS sidebar", "Online diploma / credit recovery", eyebrow="Diploma pathways")
    page("online-high-school/", "Online High School & Diploma Guide: Options, Costs, Accreditation", "Compare online high school options — tuition-free public, private, credit recovery, adult diploma and GED/HiSET — and learn how to verify accreditation. Free advisor.", html, crumbs, fs, "online high school, accredited online high school, adult high school diploma, credit recovery, ged vs diploma")

    # ------------------------------------------------------------ VIDEOS
    groups = [("math", "Math", ["algebra", "trig", "calc", "stats"]), ("science", "Science", ["bio", "carbon", "ecology", "anatomy", "chem", "physics", "astro", "eng"]),
              ("english", "English & media", ["lit", "media", "digital"]), ("history", "History & social studies", ["world", "ushist", "gov", "econ", "finlit", "psych", "soc", "philo"]),
              ("cs", "Computer science & languages", ["cs", "ling"]), ("study", "Study skills", ["notes", "memory", "exams", "practice"]), ("college", "Test prep & college", ["sat", "satweb", "essay", "essay2", "soft"])]
    chips = '<div class="chips" data-filter-group="#vgrid" role="group" aria-label="Filter videos"><button type="button" class="chip active" data-filter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" class="chip" data-filter="{c}" aria-pressed="false">{n}</button>' for c, n, _ in groups) + "</div>"
    grid = "".join(video(*V[k], cat=c) for c, n, ks in groups for k in ks)
    body = page_hero("Video Library", f"{len(V)} hand-picked lessons from CrashCourse, Khan Academy, TED-Ed, 3Blue1Brown and more — organized by subject and played through YouTube’s privacy-enhanced player.", [("Videos", "")], eyebrow="Free video lessons")
    body += f'''<div class="wrap"><section>{chips}<div class="grid g3" id="vgrid" style="margin-top:18px">{grid}</div></section>
<section class="prose narrow"><h2>How to learn from videos (not just watch them)</h2><ol><li>Watch once without notes; then rewatch and pause to write the key idea of each segment.</li><li>After the video, close it and explain the topic out loud in 60 seconds.</li><li>Do 3–5 practice problems or the quiz on the matching <a href="@@/study/">subject page</a>.</li></ol>
<p class="small muted">Videos are embedded with YouTube’s official player and remain the property of their creators. High.School is not affiliated with these channels. Click a thumbnail to load the player — no YouTube cookies are set until you do.</p></section></div>'''
    page("videos/", "Free Educational Video Library for High School", "Free high school video lessons in math, science, English, history, government, economics, psychology, computer science, study skills and college prep.", body + lead_band(), [("Videos", "")], keywords="educational videos, crash course, khan academy, high school video lessons")

    # ------------------------------------------------------------ ABOUT
    body = '''<p><strong>High.School is a free, independent command center for high school.</strong> We bring together what students, parents, adult learners and educators need most — study guides, test prep, practical tools, college and career planning, and honest guidance on diploma pathways — in one fast, ad-supported, no-sign-up website.</p>
<h2>Our mission</h2><p>Every student deserves the kind of clear, organized guidance that usually comes from an expensive counselor or a well-connected family. We want a 9th grader in any town, a parent navigating the FAFSA for the first time, or a 35-year-old finishing a diploma to find the answer in minutes.</p>
<h2>What we do</h2><ul><li><strong>Explain</strong> — plain-English guides to every core subject and test.</li><li><strong>Equip</strong> — free calculators and study tools that save data only on your device.</li><li><strong>Connect</strong> — optional, no-obligation matches with vetted tutoring, test-prep, counseling and online-school options.</li><li><strong>Celebrate</strong> — student contests with sponsor-funded prizes.</li></ul>
<h2>How we make money (transparently)</h2><p>High.School is funded by advertising served by Google AdSense, referral fees from some partner programs when families ask to be matched, sponsorships, and reader donations. Advertisers and partners never influence our editorial content. See our <a href="@@/editorial-policy/">editorial policy</a>.</p>
<h2>Who we are</h2><p>High.School is written and maintained by the High.School Editorial Team — writers and reviewers with backgrounds in teaching, tutoring, counseling and educational publishing. We welcome corrections and new contributors: <a href="@@/join/">join the team</a>.</p>
<h2>Independence</h2><p>High.School is not a school and is not affiliated with any school, district, testing organization or government agency. See our <a href="@@/trademark-disclosure/">trademark & copyright disclosure</a>.</p>
<h2>Contact</h2><p>Questions, corrections or ideas? <a href="@@/contact/">Contact us</a>. For domain, sponsorship, advertising or partnership inquiries, visit <a href="''' + PARTNER_URL + '''" target="_blank" rel="noopener">web.works/contact</a>.</p>'''
    page("about/", "About High.School", "High.School is a free, independent resource for high school students, parents, adult learners and educators. Learn about our mission, funding and editorial independence.", article("About High.School", "Free, independent, built for every student.", [("About", "")], body, [("Editorial Policy", "@@/editorial-policy/"), ("Contact", "@@/contact/"), ("Support Us", "@@/support/"), ("Join the Team", "@@/join/")], "About page"), [("About", "")])

    # ------------------------------------------------------------ CONTACT
    body = page_hero("Contact High.School", "Questions, feedback, corrections or partnership ideas — we read every message.", [("Contact", "")], meta=False)
    body += f'''<div class="wrap"><div class="layout"><div class="card"><form class="form" data-form data-thanks="thank-you/"><input type="hidden" name="_subject" value="Contact form — High.School">{HP}
<div class="row2"><div class="field"><label for="c-name">Name</label><input id="c-name" name="Name" type="text" required autocomplete="name"></div><div class="field"><label for="c-email">Email</label><input id="c-email" name="Email" type="email" required autocomplete="email"></div></div>
<div class="row2"><div class="field"><label for="c-topic">Topic</label><select id="c-topic" name="Topic"><option>General question</option><option>Feedback or correction</option><option>Tool request / bug report</option><option>Partnership or advertising</option><option>Domain or website inquiry</option><option>Press</option><option>Privacy request</option></select></div>
<div class="field"><label for="c-role">I am</label><select id="c-role" name="I am" required><option value="">Choose…</option><option>Student 13–17</option><option>Parent / guardian</option><option>Adult learner 18+</option><option>Educator</option><option>Business / organization</option><option>Under 13</option></select></div></div>
<div class="field"><label for="c-msg">Message</label><textarea id="c-msg" name="Message" required></textarea></div>
<label class="check"><input type="checkbox" name="Consent" value="Yes" required><span>I agree to the <a href="@@/privacy/">Privacy Policy</a>. If I’m under 18, a parent/guardian knows I’m contacting High.School.</span></label>
<button class="btn btn-primary" type="submit">Send message</button><p class="form-status" aria-live="polite"></p></form></div>
<aside><div class="aside-sticky"><div class="aside-box"><h4>✉️ Prefer email?</h4><p class="small">Click below to open a pre-addressed email in your mail app.</p><a href="#" class="btn btn-ink btn-sm" data-mail="Hello from a High.School reader">Email High.School</a></div>
<div class="aside-box"><h4>🤝 Domain, sponsorship & partnerships</h4><p class="small">Interested in this website or domain name, sponsorship, advertising or partnership?</p><a class="btn btn-hl btn-sm" href="{PARTNER_URL}" target="_blank" rel="noopener">Contact via web.works</a></div>
<div class="aside-box"><h4>⏱️ Response time</h4><p class="small">Usually 1–2 business days.</p></div></div></aside></div></div>'''
    page("contact/", "Contact Us", "Contact High.School with questions, feedback, corrections, tool requests, partnership or advertising inquiries.", body, [("Contact", "")], noslide=True)

    # ------------------------------------------------------------ SEARCH / THANKS / 404
    body = page_hero("Search High.School", "", [("Search", "")], meta=False)
    body += '''<div class="wrap narrow" style="padding:30px 20px"><form class="searchbar" onsubmit="return false" role="search"><label class="sr-only" for="search-input">Search</label><input id="search-input" type="search" placeholder="Search guides, tools and topics…" autofocus></form><div id="search-results" class="search-results" aria-live="polite"></div></div>'''
    page("search/", "Search", "Search High.School guides, tools, subjects and test-prep pages.", body, [("Search", "")], index=False, noslide=True, ads=False)

    body = '''<section class="hero"><div class="wrap narrow center"><div style="font-size:4rem">🎉</div><h1>Thank you — we’ve got it!</h1><p class="lead" style="margin:0 auto">Your request is in. Expect a reply within 1–2 business days. In the meantime, here are a few things you can do right now:</p>
<div class="grid g3" style="margin-top:30px;text-align:left"><a class="card" href="@@/tools/gpa-calculator/"><div class="ico">🧮</div><h3>Check your GPA</h3><p>Weighted, unweighted and a target planner.</p></a><a class="card" href="@@/college/roadmap/"><div class="ico t">🗺️</div><h3>Open your roadmap</h3><p>Grade-by-grade checklist.</p></a><a class="card" href="@@/support/"><div class="ico c">❤️</div><h3>Support High.School</h3><p>Help keep every tool free.</p></a></div>
<p class="small muted" style="margin-top:24px">Didn’t mean to submit, or want your information deleted? <a href="@@/contact/">Contact us</a>.</p></div></section>'''
    page("thank-you/", "Thank You", "Thanks for contacting High.School.", body, None, index=False, noslide=True, ads=False)

    body = '''<section class="hero"><div class="wrap narrow center"><div class="notfound">404</div><h1>This page skipped class.</h1><p class="lead" style="margin:0 auto 20px">We couldn’t find that page. Try a search or jump to a popular spot.</p>
<form class="searchbar" data-search role="search" style="margin:0 auto 20px"><label class="sr-only" for="nf-q">Search</label><input id="nf-q" type="search" placeholder="Search High.School"><button class="btn btn-primary" type="submit">Search</button></form>
<div class="chips" style="justify-content:center"><a class="chip" href="@@/">Home</a><a class="chip" href="@@/tools/gpa-calculator/">GPA Calculator</a><a class="chip" href="@@/study/">Study Hub</a><a class="chip" href="@@/test-prep/">Test Prep</a><a class="chip" href="@@/college/">College</a></div></div></section>'''
    # 404 uses absolute-from-root paths on custom domain; GitHub Pages serves it at any depth.
    from kit import page as _p
    _p("404.html", "Page Not Found", "Page not found.", body, None, index=False, noslide=True, ads=False)
