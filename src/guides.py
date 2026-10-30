"""Guides (articles) + guides hub."""
from kit import page, article, faq, ad, lead_band, page_hero, e
from subjects import vids

G = []


def g(slug, cat, emoji, title, desc, kw, body, faqs, links, need="Tutoring"):
    G.append((slug, cat, emoji, title, desc))
    crumbs = [("Guides", "@@/guides/"), (title, "")]
    fq, fs = faq(faqs)
    html = article(f"{emoji} {title}", desc, crumbs, body + fq, links + [("All guides", "@@/guides/")], title, need, eyebrow=cat.title())
    art = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "author": {"@type": "Organization", "name": "High.School Editorial Team"}, "publisher": {"@type": "Organization", "name": "High.School"}}
    page(f"guides/{slug}/", title, desc, html + lead_band(need=need), crumbs, [fs, art], kw, og_type="article")


def build():
    g("how-to-study", "study skills", "🧠", "How to Study Effectively: 7 Science-Backed Methods",
      "The study methods research actually supports — retrieval practice, spacing, interleaving, elaboration and more — with a weekly plan you can start today.",
      "how to study effectively, study tips for high school, retrieval practice, spaced repetition", f'''
<p>Most students study the way that <em>feels</em> productive: re-reading notes, highlighting and cramming. Decades of learning-science research show these are among the least effective methods. The techniques below feel harder in the moment — that difficulty is exactly what makes them work.</p>
<h2>1. Retrieval practice (test yourself)</h2><p>Close the book and pull information out of memory: answer practice questions, use <a href="@@/tools/flashcards/">flashcards</a>, or write everything you remember on a blank page. Each retrieval strengthens the memory and shows you what you don’t know.</p>
<h2>2. Spaced practice</h2><p>Spread study over days instead of one long session. Reviewing a topic on day 1, day 3, day 7 and day 14 beats the same total time crammed the night before.</p>
<h2>3. Interleaving</h2><p>Mix different problem types in one session (e.g., several kinds of algebra problems instead of 20 of the same). It trains you to choose the right method — exactly what tests require.</p>
<h2>4. Elaboration</h2><p>Ask “how?” and “why?” and connect new ideas to what you already know. Explaining a concept in your own words builds deeper understanding.</p>
{ad()}
<h2>5. Concrete examples</h2><p>Abstract ideas stick when attached to specific examples. For every definition, write one real-world example of your own.</p>
<h2>6. Dual coding</h2><p>Combine words with visuals: diagrams, timelines, flowcharts. Draw a process from memory, then compare with the textbook.</p>
<h2>7. Protect sleep and focus</h2><p>Memory consolidates during sleep, and multitasking with a phone nearby measurably lowers learning. Use the <a href="@@/tools/study-timer/">study timer</a> for distraction-free sprints.</p>
<h2>A simple weekly plan</h2><table><thead><tr><th>Day</th><th>What to do (30–60 min)</th></tr></thead><tbody><tr><td>Mon–Thu</td><td>Review today’s notes for 10 min (self-quiz), then homework with mixed practice</td></tr><tr><td>Fri</td><td>Blank-page recall for each class’s week</td></tr><tr><td>Sat</td><td>Rest or light review</td></tr><tr><td>Sun</td><td>Spaced review of last week’s and last month’s hardest topics; plan the week</td></tr></tbody></table>
<h2>Watch</h2>{vids(["practice", "memory", "exams", "notes"])}''',
      [("How many hours should a high schooler study?", "It varies by course load. Many students do 1–3 hours of homework and review on school nights. Focused, active study beats long passive hours."),
       ("Is highlighting useless?", "Highlighting alone does little. If you highlight, follow up by turning highlights into questions you quiz yourself on.")],
      [("Note-Taking Guide", "@@/guides/note-taking/"), ("Time Management", "@@/guides/time-management/"), ("Flashcards", "@@/tools/flashcards/"), ("Study Timer", "@@/tools/study-timer/")])

    g("time-management", "study skills", "⏰", "Time Management for High School Students",
      "A practical time-management system for busy students: weekly planning, the 2-list method, beating procrastination, and balancing school, activities, work and rest.",
      "time management for students, how to stop procrastinating, student planner", f'''
<p>Between classes, homework, activities, jobs, family and friends, high school schedules get crowded fast. Time management isn’t about squeezing more in — it’s about deciding what matters and protecting time for it.</p>
<h2>Step 1: Capture everything</h2><p>Use one place — a planner or calendar app — for every deadline, test, practice and shift. Your brain is for thinking, not storage.</p>
<h2>Step 2: Plan weekly (15 minutes on Sunday)</h2><ol><li>List fixed commitments (school, practice, work).</li><li>List deadlines and tests for the next two weeks.</li><li>Break big assignments into steps and schedule each step on a specific day.</li><li>Block study time like an appointment.</li></ol>
<h2>Step 3: The 2-list method each day</h2><p>Write <strong>Must do</strong> (max 3 items) and <strong>Could do</strong>. Finish the must-dos first; everything else is a bonus.</p>
{ad()}
<h2>Beating procrastination</h2><ul><li><strong>Shrink the first step:</strong> “open the doc and write the title” — starting is the hardest part.</li><li><strong>Use a timer:</strong> commit to one 25-minute <a href="@@/tools/study-timer/">Pomodoro</a>.</li><li><strong>Remove friction:</strong> phone in another room, materials ready the night before.</li><li><strong>Pair it:</strong> study with a focused friend or in the library.</li></ul>
<h2>Balance</h2><p>Schedule rest, exercise and social time on purpose. Students who sleep 8–10 hours (the amount recommended for teens) typically learn and perform better than those who sacrifice sleep for extra study.</p>''',
      [("What’s the best planner app for students?", "The best one is the one you’ll use daily. A paper planner, Google Calendar or a simple to-do app all work if you check it every morning and evening."),
       ("How do I balance a job and school?", "Agree on a fixed weekly hour cap, front-load homework on days off, and tell your manager about exam weeks in advance.")],
      [("How to Study", "@@/guides/how-to-study/"), ("Study Timer", "@@/tools/study-timer/"), ("Wellbeing & Stress", "@@/guides/wellbeing/")])

    g("note-taking", "study skills", "📝", "How to Take Better Notes: Cornell, Outline & Mapping",
      "How to take notes that actually help you learn — the Cornell method, outlining, mind mapping, digital vs handwritten, and how to review notes for tests.",
      "note taking methods, cornell notes, how to take notes in class", f'''
<p>Good notes do two jobs: they capture key ideas during class, and they become a study tool afterward. The method matters less than what you do with notes later — but the right format makes reviewing much easier.</p>
<h2>The Cornell method</h2><p>Divide the page into three areas: a narrow <strong>cue column</strong> on the left, a wide <strong>notes column</strong> on the right, and a <strong>summary</strong> strip at the bottom. Take notes on the right during class. Afterward, write questions in the cue column and a 2–3 sentence summary at the bottom. To study, cover the right side and answer the cue questions.</p>
<h2>Outline method</h2><p>Use headings and indented bullets for main ideas and supporting details. Best for well-organized lectures and textbooks.</p>
<h2>Mapping</h2><p>Put the central idea in the middle and branch out. Great for subjects with many connections (biology systems, history causes, literature themes).</p>
{ad()}
<h2>Handwritten vs digital</h2><p>Typing is faster, which tempts people to transcribe word-for-word. Handwriting forces you to summarize, which helps understanding. If you type, deliberately paraphrase. Either way, keep notes organized by date and unit.</p>
<h2>The 24-hour rule</h2><p>Review notes within a day: fill gaps, add questions, and quiz yourself. This turns notes into <a href="@@/guides/how-to-study/">retrieval practice</a>.</p>
<h2>Watch</h2>{vids(["notes"])}''',
      [("Should I copy everything the teacher says?", "No. Capture main ideas, examples, and anything the teacher repeats or writes on the board — those are likely test material."),
       ("How do I take notes from a textbook?", "Skim headings first, read a section, close the book, then write notes from memory and check.")],
      [("How to Study", "@@/guides/how-to-study/"), ("Flashcards", "@@/tools/flashcards/"), ("English Guide", "@@/study/english/")])

    g("freshman-survival-guide", "student life", "🎒", "Freshman Survival Guide: How to Start High School Strong",
      "Everything new 9th graders need: first-week tips, how grades and GPA work now, getting organized, finding your people, and avoiding the most common freshman mistakes.",
      "freshman year tips, starting high school, 9th grade advice", f'''
<p>Ninth grade is a fresh start — and it counts. Freshman grades are part of the GPA colleges see, and habits you build now will carry you through senior year. Here’s how to start strong.</p>
<h2>First week checklist</h2><ul><li>Walk your schedule so you know every room and the fastest routes.</li><li>Learn each teacher’s grading policy, late-work rules and how to get extra help.</li><li>Set up your planner and your school’s grade portal.</li><li>Introduce yourself to your counselor.</li></ul>
<h2>Grades work differently now</h2><p>Every semester grade goes on your permanent transcript. Learn how your <a href="@@/tools/gpa-calculator/">GPA</a> is calculated and use the <a href="@@/tools/grade-calculator/">grade calculator</a> to watch each class.</p>
<h2>Get organized</h2><p>One binder or folder per class, one planner for everything, and a 10-minute nightly reset: check the planner, pack the bag, review one set of notes.</p>
{ad()}
<h2>Find your people</h2><p>Try at least two clubs, teams or activities in the first month. It’s the fastest way to make friends and discover interests — and you can drop what doesn’t fit.</p>
<h2>Common freshman mistakes</h2><ol><li>Waiting until a grade is low to ask for help.</li><li>Skipping small assignments — they add up.</li><li>Staying up late on devices and running on no sleep.</li><li>Thinking freshman year doesn’t matter for college.</li></ol>
<p>Next: follow the <a href="@@/college/roadmap/">4-year roadmap</a>.</p>''',
      [("Does freshman year matter for college?", "Yes. Most colleges see all four years of grades, though many value an upward trend. A strong start gives you more options."),
       ("How do I make friends in high school?", "Join activities, sit with new people at lunch once a week, and say yes to group projects and events.")],
      [("4-Year Roadmap", "@@/college/roadmap/"), ("Time Management", "@@/guides/time-management/"), ("Extracurriculars", "@@/guides/extracurriculars/")])

    g("extracurriculars", "college prep", "🏅", "Extracurricular Activities That Actually Matter",
      "How to choose extracurriculars, what colleges really look for (depth, impact, leadership), how to describe activities on applications, and ideas for every interest.",
      "extracurricular activities, extracurriculars for college, activities list common app", f'''
<p>Colleges don’t have a checklist of “right” activities. They look for <strong>depth</strong> (sustained involvement), <strong>impact</strong> (what changed because you were there) and <strong>initiative</strong> (things you started or grew). Two activities done seriously beat ten done casually.</p>
<h2>Types of activities that count</h2><ul><li>Clubs, sports, arts and music</li><li>Part-time jobs and family responsibilities (caring for siblings counts!)</li><li>Volunteering and community service</li><li>Independent projects: a website, a business, research, a YouTube channel</li><li>Summer programs and online courses</li></ul>
<h2>Turn participation into impact</h2><p>Ask: what problem can I solve here? Organize an event, mentor younger members, raise money, build something. Then measure it — “raised $2,400 for…” is stronger than “helped with fundraising.”</p>
{ad()}
<h2>Describing activities on applications</h2><p>The Common App gives 150 characters per activity description. Lead with action verbs and numbers: <em>“Founded coding club; grew to 35 members; taught weekly Python lessons; built school lunch-menu app.”</em></p>
<h2>Need ideas? Start with High.School</h2><p>Enter our <a href="@@/contests/">student contests</a>, become a <a href="@@/join/">student ambassador</a>, or contribute guides — all real activities you can list.</p>''',
      [("How many extracurriculars should I have?", "Quality over quantity. Many strong applicants have 3–6 meaningful activities, with deep involvement in 1–2."),
       ("Do jobs count as extracurriculars?", "Yes. Colleges value work experience — it shows responsibility and time management.")],
      [("Summer Programs", "@@/guides/summer-programs/"), ("College Applications", "@@/college/applications/"), ("Contests", "@@/contests/")], need="College counseling")

    g("summer-programs", "college prep", "☀️", "Summer Programs, Jobs & Projects for High Schoolers",
      "How to spend high school summers well: pre-college programs, free and paid options, internships, jobs, volunteering, independent projects, and application timelines.",
      "summer programs for high school students, free summer programs, high school internships", f'''
<p>Summer is your chance to explore an interest deeply, earn money, help your community or build something of your own. Colleges don’t expect an expensive program — they care what you did and learned.</p>
<h2>Options at a glance</h2><table><thead><tr><th>Option</th><th>Cost</th><th>Best for</th></tr></thead><tbody><tr><td>Selective free programs (government, university, nonprofit)</td><td>Free–low; often stipends</td><td>Strong students in STEM, policy, arts</td></tr><tr><td>Pre-college programs at universities</td><td>Often paid</td><td>Trying campus life and a subject</td></tr><tr><td>Jobs</td><td>You earn</td><td>Everyone — responsibility and savings</td></tr><tr><td>Internships / research</td><td>Free–paid</td><td>Career exploration</td></tr><tr><td>Volunteering</td><td>Free</td><td>Community impact</td></tr><tr><td>Independent projects</td><td>Free</td><td>Self-starters: build, write, code, create</td></tr></tbody></table>
<h2>Timeline</h2><p>Many selective programs have deadlines from <strong>January to April</strong>. Start researching in the fall. Ask teachers for recommendations at least three weeks early.</p>
{ad()}
<h2>Spotting value (and avoiding expensive fluff)</h2><p>Be cautious with programs that charge high fees but admit almost everyone and promise admissions advantages. A summer job or a self-driven project is often just as valuable — and sometimes more.</p>''',
      [("Do summer programs help college admissions?", "Selective, free programs can be impressive, but what matters most is what you learned and did. A job or meaningful project can be equally strong."),
       ("I can’t afford a program. What should I do?", "Work, volunteer, take free online courses, or start a project. These are fully respected by colleges.")],
      [("Extracurriculars", "@@/guides/extracurriculars/"), ("Majors & Careers", "@@/college/majors-careers/"), ("Scholarships", "@@/college/scholarships/")], need="College counseling")

    g("wellbeing", "student life", "💚", "Student Wellbeing: Managing Stress, Sleep & Balance",
      "Practical, evidence-based ways for high school students to manage stress, sleep better, handle test anxiety and know when and where to get support.",
      "student stress, test anxiety, sleep for teens, high school mental health", f'''
<p>Some stress is normal — it can even help you prepare. But chronic stress, poor sleep and constant pressure make learning harder. These habits help, and asking for support is a sign of strength.</p>
<h2>Sleep is a study tool</h2><p>Teens are recommended to get 8–10 hours of sleep. Keep a consistent schedule, charge your phone outside the bedroom, and avoid caffeine late in the day.</p>
<h2>Managing test anxiety</h2><ul><li>Prepare with practice tests under realistic conditions — familiarity reduces fear.</li><li>Use slow breathing before and during exams (inhale 4 counts, exhale 6).</li><li>Reframe nerves as energy: “I’m ready” rather than “I’m scared.”</li><li>Start with questions you know to build momentum.</li></ul>
{ad()}
<h2>Daily balance</h2><p>Movement, time outdoors, time with friends and offline hobbies all buffer stress. Schedule them like any other priority — see <a href="@@/guides/time-management/">time management</a>.</p>
<h2>When to get help</h2><p>Talk to a trusted adult, school counselor or doctor if stress, sadness or worry lasts for weeks or affects sleep, eating, school or relationships. In the US, you can call or text <strong>988</strong> (Suicide & Crisis Lifeline) any time, 24/7, if you or someone you know is struggling. Outside the US, contact local emergency services or a national helpline.</p>
<p class="small muted">This guide is general educational information, not medical advice.</p>''',
      [("Is it normal to feel stressed in high school?", "Yes, many students do. If stress feels unmanageable or lasts for weeks, talk to a counselor or trusted adult."),
       ("How can parents help with stress?", "Listen without immediately problem-solving, keep expectations realistic, protect sleep and downtime, and model balance.")],
      [("Time Management", "@@/guides/time-management/"), ("How to Study", "@@/guides/how-to-study/"), ("Parent Guide", "@@/guides/parent-guide/")])

    g("parent-guide", "parents", "👪", "The Parent’s Guide to High School",
      "A practical guide for parents of high schoolers: how grades, credits and GPA work, supporting without pressure, college costs, financial aid timing, and when to get outside help.",
      "parent guide high school, how to help my teen in high school, college planning for parents", f'''
<p>Your teen is building independence, and your role is shifting from manager to coach. Here’s what to know — and when to step in — across all four years.</p>
<h2>Know how the system works</h2><ul><li><strong>Credits:</strong> graduation requires a set number per subject. Track them with the <a href="@@/tools/credit-tracker/">credit tracker</a>.</li><li><strong>GPA:</strong> every semester grade counts. Weighted GPA adds points for Honors/AP/IB — see the <a href="@@/tools/gpa-calculator/">GPA calculator</a>.</li><li><strong>Grade portals:</strong> check together weekly, not daily, to avoid micromanaging.</li></ul>
<h2>Support without pressure</h2><p>Praise effort and strategy, not just results. Ask open questions (“What was hard today?”). Protect sleep and downtime. Let your teen lead conversations with teachers, stepping in only when needed.</p>
<h2>Money and timing</h2><table><thead><tr><th>When</th><th>Parent to-do</th></tr></thead><tbody><tr><td>9th–10th</td><td>Estimate costs with the <a href="@@/tools/college-cost-calculator/">college cost calculator</a>; open or fund education savings</td></tr><tr><td>11th</td><td>Run Net Price Calculators for colleges on the list; discuss budget honestly</td></tr><tr><td>12th (Oct)</td><td>Complete the <a href="@@/college/financial-aid/">FAFSA</a> and CSS Profile if needed</td></tr><tr><td>12th (spring)</td><td>Compare aid offers by net cost; appeal if needed</td></tr></tbody></table>
{ad()}
<h2>When to get outside help</h2><p>Consider a tutor when a grade drops for more than a few weeks, test prep when your teen has a clear target score, and a counselor or coach when the college process becomes a source of conflict at home. If your teen is behind on credits or needs a flexible schedule, our <a href="@@/online-high-school/">online high school guide</a> explains your options.</p>''',
      [("How involved should parents be in high school?", "Stay informed and available, but let your teen own day-to-day work. Step in for patterns (consistently low grades, missing assignments), not single bad days."),
       ("When should we start talking about college costs?", "By 10th grade. Early, honest conversations prevent heartbreak when admission and aid offers arrive.")],
      [("Financial Aid & FAFSA", "@@/college/financial-aid/"), ("Online High School", "@@/online-high-school/"), ("Wellbeing & Stress", "@@/guides/wellbeing/")], need="Tutoring")

    g("teacher-resources", "educators", "🍎", "Free Resources for High School Teachers & Counselors",
      "Free, classroom-ready resources for high school teachers and counselors: how to use High.School tools in class, study-skills mini-lessons, college-planning materials and partnership options.",
      "high school teacher resources, counselor resources, free classroom resources", f'''
<p>High.School is free for classrooms. Here’s how teachers and counselors use it, plus ways to collaborate with us.</p>
<h2>Use our tools in class</h2><ul><li><strong>GPA and grade calculators:</strong> a quick lesson on weighted averages that students immediately care about.</li><li><strong>Practice quizzes</strong> on every <a href="@@/study/">subject page</a> as bell-ringers or exit tickets.</li><li><strong>Study timer</strong> projected for focused work blocks.</li><li><strong>Flashcards</strong> for vocabulary review stations.</li></ul>
<h2>Mini-lessons (10 minutes each)</h2><ol><li>Retrieval practice vs re-reading — demo with a 2-minute quiz.</li><li>Cornell notes — model with today’s content.</li><li>Planning a big assignment backward from the due date.</li><li>Reading a college’s middle-50% score range.</li></ol>
{ad()}
<h2>For counselors</h2><p>Share the <a href="@@/college/roadmap/">4-year roadmap</a> at registration time, the <a href="@@/college/financial-aid/">FAFSA guide</a> at fall family nights, and the <a href="@@/college/scholarships/">scholarship tracker</a> with seniors.</p>
<h2>Work with us</h2><p>Teachers can <a href="@@/join/">write or review guides</a>, suggest tools, or sponsor a class entry in our <a href="@@/contests/">contests</a>. Schools and organizations can explore <a href="@@/partner/">partnerships</a>.</p>''',
      [("Is High.School free for schools?", "Yes. All guides and tools are free to use in classrooms."),
       ("Do students need accounts?", "No. Tools save data only in the student’s own browser.")],
      [("Study Hub", "@@/study/"), ("Join the Team", "@@/join/"), ("Partner with Us", "@@/partner/")], need="Tutoring")

    cats = ["study skills", "student life", "college prep", "parents", "educators"]
    chips = '<div class="chips" data-filter-group="#guide-grid" role="group" aria-label="Filter guides"><button type="button" class="chip active" data-filter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" class="chip" data-filter="{c}" aria-pressed="false">{c.title()}</button>' for c in cats) + "</div>"
    cards = "".join(f'<a class="card" data-cat="{c}" href="@@/guides/{s}/"><div class="ico t">{em}</div><span class="tag">{c}</span><h3 style="margin-top:8px">{e(t)}</h3><p>{e(d[:120])}…</p></a>' for s, c, em, t, d in G)
    body = page_hero("Guides", "Practical, research-backed guides for students, parents and educators — study skills, student life, college prep and more.", [("Guides", "")], eyebrow="For students · parents · educators")
    body += f'<div class="wrap"><section>{chips}<div class="grid g3" id="guide-grid" style="margin-top:18px">{cards}</div></section></div>'
    page("guides/", "Guides for High School Students, Parents & Teachers", "Research-backed guides on studying, time management, note-taking, freshman year, extracurriculars, summer programs, wellbeing, parenting and teaching.", body + lead_band(), [("Guides", "")], keywords="high school guides, study tips, parent guide")
    return G
