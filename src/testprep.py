"""Test prep hub + SAT, ACT, AP, IB, PSAT, SAT vs ACT."""
from kit import page, article, quiz, faq, ad, lead_band, page_hero, e
from subjects import vids

TM = '<p class="small muted">SAT®, AP® and PSAT/NMSQT® are trademarks registered by the College Board. ACT® is a registered trademark of ACT Education Corp. IB is a trademark of the International Baccalaureate Organization. National Merit® is a trademark of NMSC. None of these organizations is affiliated with or endorses High.School. Always confirm dates, fees and policies on the official website.</p>'
LINKS = [("SAT Guide", "@@/test-prep/sat/"), ("ACT Guide", "@@/test-prep/act/"), ("SAT vs ACT", "@@/test-prep/sat-vs-act/"), ("SAT ↔ ACT Converter", "@@/tools/sat-act-converter/"), ("AP Exams", "@@/test-prep/ap/"), ("College Applications", "@@/college/applications/")]


def P(path, title, h1, desc, crumbs, body, kw, need="Test prep (SAT/ACT/AP)", faqs=None):
    schema = []
    if faqs:
        fq, fs = faq(faqs)
        body += fq
        schema.append(fs)
    body += TM
    html = article(h1, desc, crumbs, body, LINKS, title, need, eyebrow="Test Prep")
    page(path, title, desc, html + lead_band("Want a test-prep plan built for your target score?", "Tell us your current score, goal and test date. We’ll match you with free practice resources and vetted prep options.", "Test prep (SAT/ACT/AP)"), crumbs, schema, kw)


def build():
    C = lambda n: [("Test Prep", "@@/test-prep/"), (n, "")]

    P("test-prep/sat/", "Digital SAT Guide: Format, Scoring & Study Plan", "📝 The Digital SAT: Complete Guide", "Everything about the digital SAT — sections, timing, adaptive modules, scoring, what’s a good score, and an 8-week study plan.", C("SAT"), f'''
<p>The SAT is a college admission test used by most US colleges and many international universities. Since 2024 it has been fully <strong>digital</strong> and <strong>adaptive</strong>: you take it on a laptop or tablet in the official Bluebook app at a test center, and the second module of each section adjusts to how you did on the first.</p>
<h2>Format at a glance</h2>
<table><thead><tr><th>Section</th><th>Questions</th><th>Time</th><th>Score</th></tr></thead><tbody>
<tr><td>Reading & Writing (2 modules)</td><td>54</td><td>64 min</td><td>200–800</td></tr>
<tr><td>Math (2 modules)</td><td>44</td><td>70 min</td><td>200–800</td></tr>
<tr><td><strong>Total</strong></td><td><strong>98</strong></td><td><strong>2 h 14 min</strong> + 10-min break</td><td><strong>400–1600</strong></td></tr></tbody></table>
<h2>What’s on each section</h2>
<h3>Reading & Writing</h3><p>Short passages — usually a single paragraph — each with one question. Skills tested: information and ideas (main idea, evidence, inferences), craft and structure (vocabulary in context, text structure), expression of ideas (transitions, rhetorical synthesis) and standard English conventions (grammar, punctuation).</p>
<h3>Math</h3><p>Algebra (linear equations and systems), advanced math (quadratics, exponentials, functions), problem-solving and data analysis (ratios, percentages, statistics) and geometry/trigonometry. A <strong>Desmos graphing calculator is built into the app</strong> for the whole math section — learning to use it well is one of the biggest score multipliers.</p>
<h2>What is a good SAT score?</h2><p>The average total score is roughly in the low 1000s. As a rule of thumb: <strong>1200+</strong> is competitive at many public universities, <strong>1350+</strong> is strong for selective colleges, and <strong>1500+</strong> is in range for the most selective. The best target is the <em>middle 50% range</em> published by each college on your list. Use our <a href="@@/tools/sat-act-converter/">SAT ↔ ACT converter</a> to compare scores.</p>
{ad()}
<h2>8-week study plan</h2><ol>
<li><strong>Week 1 — Baseline:</strong> take a full-length official practice test in Bluebook under real timing. Log every miss by skill.</li>
<li><strong>Weeks 2–3 — Biggest gaps:</strong> drill the 2–3 skills that cost the most points. For most students: linear equations, grammar boundaries (commas/semicolons), and inference questions.</li>
<li><strong>Week 4 — Practice test #2</strong> and update your error log.</li>
<li><strong>Weeks 5–6 — Mixed practice + Desmos:</strong> timed mixed sets; learn to graph systems and find intersections in Desmos.</li>
<li><strong>Week 7 — Practice test #3</strong>, pacing review (aim for ~1 min 11 s per R&W question and ~1 min 35 s per math question).</li>
<li><strong>Week 8 — Taper:</strong> light review, sleep, logistics (admission ticket, charged device, ID).</li></ol>
<div class="callout"><p><strong>Free official practice:</strong> College Board’s Bluebook app has full-length adaptive practice tests, and Khan Academy offers free official SAT practice. Start there before paying for anything.</p></div>
<h2>Watch</h2>{vids(["sat", "satweb"])}''', "digital sat, sat format, sat scoring, good sat score, sat study plan, sat practice", faqs=[
        ("Is the SAT still required for college?", "Policies vary. Many colleges are test-optional, but a growing number of selective colleges have reinstated testing requirements. Check each college’s current admissions page."),
        ("How many times can I take the SAT?", "As many times as you like. Many students take it 2–3 times; many colleges “superscore,” combining your best section scores across dates."),
        ("Can I use a calculator on the whole math section?", "Yes. On the digital SAT a calculator is allowed on all math questions, and a Desmos graphing calculator is built into the testing app."),
        ("When should I take the SAT?", "Most students take it for the first time in spring of junior year, leaving time to retest in summer or early fall of senior year.")])

    P("test-prep/act/", "ACT Guide: Enhanced ACT Format, Scoring & Strategy", "🧾 The ACT: Complete Guide", "The enhanced ACT explained — shorter test, optional science, composite scoring, timing per question, what’s a good score and how to prepare.", C("ACT"), f'''
<p>The ACT is the other major US college admission test. In 2025 ACT introduced the <strong>enhanced ACT</strong>: a shorter test with fewer questions, more time per question, and the Science section made optional. Colleges accept the ACT and SAT equally.</p>
<h2>Enhanced ACT format</h2>
<table><thead><tr><th>Section</th><th>Questions</th><th>Time</th><th>Notes</th></tr></thead><tbody>
<tr><td>English</td><td>50</td><td>35 min</td><td>Grammar, punctuation, rhetorical skills</td></tr>
<tr><td>Math</td><td>45</td><td>50 min</td><td>Calculator allowed; 4 answer choices</td></tr>
<tr><td>Reading</td><td>36</td><td>40 min</td><td>Passages from literature, social science, humanities, natural science</td></tr>
<tr><td>Science <em>(optional)</em></td><td>40</td><td>40 min</td><td>Data interpretation, experiments, conflicting viewpoints</td></tr>
<tr><td>Writing <em>(optional)</em></td><td>1 essay</td><td>40 min</td><td>Argumentative essay</td></tr></tbody></table>
<p>The <strong>composite score (1–36)</strong> is the average of English, Math and Reading. If you take Science, you also receive a Science score and a STEM score. Check whether the colleges and scholarship programs on your list want the Science section.</p>
<h2>What is a good ACT score?</h2><p>The national average composite is around 19–20. Roughly: <strong>24+</strong> is solid for many state universities, <strong>28+</strong> is strong for selective colleges, and <strong>33+</strong> is in range for the most selective. Compare with SAT scores using our <a href="@@/tools/sat-act-converter/">converter</a>.</p>
{ad()}
<h2>Strategy</h2><ul>
<li><strong>Pacing first.</strong> Even on the enhanced test, the ACT rewards speed. Practice with a timer from day one.</li>
<li><strong>English is the fastest section to improve.</strong> A small set of grammar rules (commas, semicolons, apostrophes, subject–verb agreement, concision) covers most questions.</li>
<li><strong>Math:</strong> memorize core formulas — the ACT does not provide a formula sheet.</li>
<li><strong>Reading:</strong> try reading the passage briskly for structure, then hunt for evidence for each answer.</li>
<li><strong>Science:</strong> it is mostly graph and table reading — you rarely need outside science knowledge.</li></ul>
<div class="callout t"><p><strong>Not sure which test fits you?</strong> Take our 1-minute <a href="@@/test-prep/sat-vs-act/">SAT vs ACT quiz</a>.</p></div>''', "act test, enhanced act, act scoring, act science optional, good act score, act prep", faqs=[
        ("Is ACT Science still required?", "On the enhanced ACT, Science is optional and not included in the composite score. Some colleges or programs may still want it — check their requirements."),
        ("Is the ACT easier than the SAT?", "Neither is objectively easier. The ACT is faster-paced and has no built-in graphing calculator; the SAT is adaptive and has more algebra emphasis. Take a practice test of each."),
        ("Do colleges superscore the ACT?", "Many do. ACT also reports a superscore if you have taken the test more than once.")])

    P("test-prep/ap/", "AP Exams Guide: Courses, Scores, Credit & Strategy", "🎓 AP Courses & Exams Guide", "How AP courses and exams work — scoring 1–5, college credit, how many APs to take, exam timing in May and proven study strategies.", C("AP Exams"), f'''
<p>Advanced Placement (AP) courses are college-level classes taught in high school. Each ends with an exam in <strong>May</strong>, scored <strong>1 to 5</strong>. Many colleges grant credit or placement for scores of 3, 4 or 5 — which can save tuition and let you start in higher-level courses.</p>
<h2>How AP scoring works</h2><table><thead><tr><th>Score</th><th>Meaning</th></tr></thead><tbody><tr><td>5</td><td>Extremely well qualified</td></tr><tr><td>4</td><td>Very well qualified</td></tr><tr><td>3</td><td>Qualified</td></tr><tr><td>2</td><td>Possibly qualified</td></tr><tr><td>1</td><td>No recommendation</td></tr></tbody></table>
<p>Most exams combine a multiple-choice section and a free-response section. Most AP exams are now taken digitally in the Bluebook app, while some are hybrid (answers to free-response questions handwritten). Scores are typically released in early July.</p>
<h2>Popular AP courses by interest</h2><ul>
<li><strong>STEM:</strong> Calculus AB/BC, Statistics, Biology, Chemistry, Physics 1/2/C, Computer Science A & Principles, Environmental Science</li>
<li><strong>Humanities:</strong> English Language, English Literature, US History, World History, European History, Art History</li>
<li><strong>Social sciences:</strong> Psychology, US Government, Comparative Government, Macroeconomics, Microeconomics, Human Geography</li>
<li><strong>Languages & arts:</strong> Spanish, French, Chinese, Latin, Music Theory, Studio Art, AP Seminar & Research (Capstone)</li></ul>
<h2>How many AP classes should I take?</h2><p>Quality beats quantity. Colleges evaluate rigor <em>relative to what your school offers</em>. A common pattern is 0–1 AP in 10th grade, 2–3 in 11th and 2–4 in 12th — chosen around your strengths and intended major. Overloading to the point that grades drop or sleep disappears is a net negative. Use the <a href="@@/tools/gpa-calculator/">GPA calculator</a> to see how weighted AP grades affect your GPA.</p>
{ad()}
<h2>AP study strategy</h2><ol><li>Download the course and exam description (CED) for each course — it lists every unit and skill.</li><li>Practice past free-response questions; College Board publishes many with scoring guidelines.</li><li>Score your own responses using the rubric — it teaches you what readers reward.</li><li>From March, do one timed mixed MCQ set per week per course.</li><li>Use AP Classroom progress checks your teacher assigns — they mirror exam style.</li></ol>''', "ap exams, ap scores, ap credit, how many ap classes, ap study tips", faqs=[
        ("Do AP scores go on my college application?", "You may self-report AP scores on most applications. Policies vary; some students choose to report only strong scores. Colleges see your AP course grades on your transcript regardless."),
        ("Can I take an AP exam without taking the class?", "Yes, you can self-study and register through a school that offers the exam. Contact the school’s AP coordinator early (usually by fall)."),
        ("Do all colleges give credit for a 3?", "No. Credit policies vary by college and even by department. Search “[college name] AP credit policy” for the details.")])

    P("test-prep/ib/", "IB Diploma Programme Guide: Subjects, Core & Scoring", "🌐 IB Diploma Programme Guide", "How the International Baccalaureate Diploma works — six subject groups, HL vs SL, TOK, the Extended Essay, CAS and the 45-point scoring scale.", C("IB Diploma"), f'''
<p>The International Baccalaureate (IB) Diploma Programme is a rigorous two-year curriculum for students aged 16–19, offered at thousands of schools worldwide. Unlike AP (individual courses), the IB Diploma is a complete program with a shared core.</p>
<h2>Structure</h2><ul><li><strong>Six subjects</strong>, one from each group: Language & Literature, Language Acquisition, Individuals & Societies, Sciences, Mathematics, and the Arts (or a second subject from another group).</li>
<li>Usually <strong>three at Higher Level (HL)</strong> and <strong>three at Standard Level (SL)</strong>.</li>
<li><strong>The core:</strong> Theory of Knowledge (TOK), the Extended Essay (an independent research paper of up to 4,000 words) and Creativity, Activity, Service (CAS).</li></ul>
<h2>Scoring</h2><table><thead><tr><th>Component</th><th>Points</th></tr></thead><tbody><tr><td>6 subjects × 7 points</td><td>42</td></tr><tr><td>TOK + Extended Essay (combined)</td><td>up to 3</td></tr><tr><td><strong>Maximum</strong></td><td><strong>45</strong></td></tr></tbody></table>
<p>A minimum of 24 points (plus other conditions, such as completing CAS) is required to earn the diploma. Results are released in early July for May exams.</p>
{ad()}
<h2>Is IB right for you?</h2><p>IB suits students who like interdisciplinary thinking, writing and long-term projects. The workload is sustained over two years rather than concentrated in exam season. Universities worldwide recognize the diploma, and many grant credit for strong HL scores.</p>
<h2>Survival tips</h2><ol><li>Start the Extended Essay topic search early in year one — pick a question you genuinely care about.</li><li>Log CAS experiences weekly; don’t reconstruct them at the end.</li><li>Use subject guides and past papers with mark schemes.</li><li>Protect sleep — IB is a marathon.</li></ol>''', "ib diploma, international baccalaureate, extended essay, tok, cas, ib scoring", need="Tutoring", faqs=[
        ("IB vs AP — which is better?", "Neither is universally better. IB is an integrated program with a research and service core; AP lets you pick individual courses. Colleges value both when taken at a high level."),
        ("Can I take IB courses without the full diploma?", "Yes, many schools let students take individual IB courses and earn course certificates.")])

    P("test-prep/psat/", "PSAT/NMSQT Guide: Scoring & National Merit", "🏅 PSAT/NMSQT & National Merit Guide", "How the PSAT/NMSQT works, how it’s scored (320–1520), the National Merit Selection Index, and how juniors qualify for recognition and scholarships.", C("PSAT/NMSQT"), f'''
<p>The PSAT/NMSQT is a practice version of the SAT, usually taken in October. When taken in <strong>11th grade</strong>, it is also the qualifying test for the <strong>National Merit Scholarship Program</strong>. It uses the same digital, adaptive format as the SAT.</p>
<h2>Scoring</h2><p>Total scores range from <strong>320 to 1520</strong> (Reading & Writing 160–760, Math 160–760). National Merit uses a separate <strong>Selection Index</strong> (48–228), which double-weights Reading & Writing: <span class="kbd">Selection Index = (2 × RW + Math) ÷ 10</span>.</p>
<h2>National Merit recognition</h2><ul><li>Roughly the top 50,000 Selection Index scorers receive recognition.</li><li>About 16,000 are named <strong>Semifinalists</strong>, based on state-specific cutoffs.</li><li>Semifinalists who complete an application (grades, recommendation, essay, confirming SAT/ACT score) can become <strong>Finalists</strong>, and some receive scholarships.</li></ul>
{ad()}
<h2>How to prepare</h2><p>Because the PSAT mirrors the SAT, SAT prep is PSAT prep. Take a full practice test in the Bluebook app in summer before junior year, focus on Reading & Writing (it counts double for National Merit), and review your score report to plan SAT prep.</p>''', "psat, nmsqt, national merit, selection index, psat score", faqs=[
        ("Does the PSAT count for college admissions?", "No. Colleges don’t see PSAT scores. It matters for National Merit (junior year) and as SAT practice."),
        ("Can 10th graders take the PSAT?", "Yes, many do for practice, but only the junior-year score counts for National Merit.")])

    # SAT vs ACT with quiz
    qz = '''<div class="tool" id="svs"><h3 style="margin-top:0">⚔️ 1-minute SAT vs ACT quiz</h3><p class="small muted">Pick the statement that sounds most like you.</p>
<div class="form">''' + "".join(f'''<fieldset class="field" style="border:0;padding:0;margin:0"><legend class="legend">{i}. {q}</legend><div class="option-grid">
<label class="option"><input type="radio" name="sv{i}" value="s"><span>{a}</span></label><label class="option"><input type="radio" name="sv{i}" value="a"><span>{b}</span></label></div></fieldset>''' for i, (q, a, b) in enumerate([
        ("Under time pressure, I…", "Prefer more time per question", "Work fast and stay accurate"),
        ("In math, I’m stronger at…", "Algebra and functions", "A broad mix incl. geometry & trig"),
        ("For calculators, I want…", "A built-in graphing calculator (Desmos)", "My own approved calculator"),
        ("On reading, I prefer…", "Many short passages, one question each", "Fewer long passages with several questions"),
        ("Science-style data questions…", "I’d rather skip them", "I’m comfortable reading charts and experiments"),
        ("Test format I’d enjoy…", "Adaptive, on a device", "Linear sections — same for everyone")], 1)) + '''
<button type="button" class="btn btn-primary" id="svs-go">See my result</button><div id="svs-out" aria-live="polite"></div></div></div>
<script>document.getElementById('svs-go').addEventListener('click',function(){var s=0,a=0,n=0;for(var i=1;i<=6;i++){var c=document.querySelector('input[name=sv'+i+']:checked');if(c){n++;c.value==='s'?s++:a++;}}var o=document.getElementById('svs-out');if(n<4){o.innerHTML='<p class="form-status err">Answer at least 4 questions.</p>';return;}var r=s>a?'SAT':(a>s?'ACT':'either test');o.innerHTML='<div class="result"><div><b>'+r+'</b><span>Your likely better fit ('+s+' SAT · '+a+' ACT)</span></div></div><p style="margin-top:12px">Confirm it by taking one official practice test of each, then compare with our <a href="../../tools/sat-act-converter/">converter</a>. Want a prep plan? <a href="../../get-matched/?need=Test%20prep%20(SAT/ACT/AP)">Get matched free →</a></p>';});</script>'''
    P("test-prep/sat-vs-act/", "SAT vs ACT: Which Test Should You Take? (+ Quiz)", "⚔️ SAT vs ACT: Which Should You Take?", "Side-by-side comparison of the digital SAT and enhanced ACT — timing, content, calculators, scoring — plus a 1-minute quiz to find your better test.", C("SAT vs ACT"), f'''
<p>Every US college that accepts test scores accepts both the SAT and the ACT equally. So the question isn’t which test colleges prefer — it’s which test <strong>you</strong> will score higher on. Most students score similarly on both, but about one in three has a meaningful edge on one test.</p>
{qz}
<h2>Side-by-side comparison</h2><table><thead><tr><th></th><th>Digital SAT</th><th>Enhanced ACT</th></tr></thead><tbody>
<tr><td>Length</td><td>2 h 14 min</td><td>~2 h core (+40 min optional Science)</td></tr>
<tr><td>Format</td><td>Digital, adaptive by module</td><td>Paper or online, linear</td></tr>
<tr><td>Sections</td><td>Reading & Writing; Math</td><td>English; Math; Reading; optional Science & Writing</td></tr>
<tr><td>Calculator</td><td>All math; Desmos built in</td><td>All math; bring an approved calculator</td></tr>
<tr><td>Reading style</td><td>Short passages, 1 question each</td><td>Longer passages, multiple questions</td></tr>
<tr><td>Scoring</td><td>400–1600</td><td>1–36 composite</td></tr></tbody></table>
{ad()}
<h2>How to decide</h2><ol><li>Take one full official practice test of each, under timed conditions.</li><li>Convert scores with our <a href="@@/tools/sat-act-converter/">SAT ↔ ACT converter</a>.</li><li>Pick the test with the higher converted score — and the one you <em>felt</em> better on — then commit to it.</li></ol>''', "sat vs act, which test should i take, sat or act quiz", faqs=[
        ("Do colleges prefer the SAT or ACT?", "No. Colleges that accept test scores treat them equally."),
        ("Should I take both?", "Usually it’s better to choose one and prepare deeply. Take a practice test of each first, then commit.")])

    hub = page_hero("Test Prep Hub", "Plain-English guides to the SAT, ACT, AP, IB and PSAT — formats, scoring, good scores and free study plans. Plus a 1-minute quiz to pick your test.", [("Test Prep", "")], eyebrow="Free · Official-practice first")
    cards = [("📝", "Digital SAT", "Sections, adaptive modules, scoring and an 8-week plan.", "sat/"), ("🧾", "Enhanced ACT", "Shorter test, optional science, composite scoring.", "act/"), ("⚔️", "SAT vs ACT", "Compare side by side and take the 1-minute quiz.", "sat-vs-act/"),
             ("🎓", "AP Exams", "Scores 1–5, college credit, how many APs to take.", "ap/"), ("🌐", "IB Diploma", "Subjects, HL/SL, TOK, Extended Essay, CAS.", "ib/"), ("🏅", "PSAT/NMSQT", "Selection Index and National Merit.", "psat/")]
    hub += '<div class="wrap"><section><div class="grid g3">' + "".join(f'<a class="card" href="@@/test-prep/{u}"><div class="ico s">{i}</div><h3>{t}</h3><p>{d}</p></a>' for i, t, d, u in cards) + '</div></section>'
    hub += f'''<section class="prose narrow"><h2>Testing timeline</h2><table><thead><tr><th>When</th><th>What</th></tr></thead><tbody><tr><td>Grade 10 (fall)</td><td>Optional PSAT 10 / PSAT/NMSQT practice</td></tr><tr><td>Grade 11 (October)</td><td>PSAT/NMSQT — counts for National Merit</td></tr><tr><td>Grade 11 (winter–spring)</td><td>First SAT or ACT; AP exams in May</td></tr><tr><td>Summer before grade 12</td><td>Targeted prep and retake</td></tr><tr><td>Grade 12 (Aug–Oct)</td><td>Final retake before early application deadlines</td></tr></tbody></table>
<p>Official calendars and registration: <a href="https://satsuite.collegeboard.org/sat" target="_blank" rel="noopener">SAT (College Board)</a> · <a href="https://www.act.org/" target="_blank" rel="noopener">ACT</a> · <a href="https://apstudents.collegeboard.org/" target="_blank" rel="noopener">AP Students</a> · <a href="https://www.ibo.org/" target="_blank" rel="noopener">IB</a>.</p>{TM}</section></div>'''
    page("test-prep/", "Test Prep Hub: SAT, ACT, AP, IB & PSAT Guides", "Free test prep guides for the digital SAT, enhanced ACT, AP exams, IB Diploma and PSAT/NMSQT — formats, scoring, timelines and study plans.", hub + lead_band("Get a free test-prep match", "Tutors, courses and free official resources matched to your score goal and timeline.", "Test prep (SAT/ACT/AP)"), [("Test Prep", "")], keywords="sat prep, act prep, ap exams, ib, psat")
