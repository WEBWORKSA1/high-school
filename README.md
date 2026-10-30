# High.School

**The free command center for high school.** It has study guides for 10 subjects, SAT/ACT/AP/IB/PSAT prep, 8 free tools (GPA, final grade, weighted grade, SAT↔ACT, college cost, credit tracker, Pomodoro, flashcards), and college, financial-aid and scholarship planning. It also covers online-diploma guidance and a video library, and has a lead-generation funnel, donations, contests, hiring and partnership pages.

Static HTML/CSS/vanilla JS that GitHub Pages hosts for free from the `main` branch root.

## Build
```bash
python3 build.py                 # plain static HTML: every page fully assembled (+ .nojekyll)
python3 build.py --jekyll OUT    # same pages, with header/footer/head as {% include %} tags
```
**How the repo is published today:** the repo contains the `--jekyll` output (`_includes/`, `_config.yml` and the page files). GitHub Pages' built-in Jekyll assembles the pages on every push, and the result is byte-identical to the plain build, so no workflow is needed.

**Optional, for auto-builds:** add `.github/workflows/build.yml` (the file is in `docs/build-workflow.yml`; copy it through GitHub's web UI, since API integrations can't write workflow files). After that, each push to `src/` regenerates the plain HTML and the PNG icons on GitHub.

Content lives in `src/*.py`. The shared template, header, footer and components are in `src/kit.py`. Every internal link is relative, so the site works at `https://webworksa1.github.io/high-school/` and on `https://high.school/`.

## Configure
| What | Where |
|---|---|
| AdSense publisher / script | `src/kit.py` → `PUB`, `ADSENSE` (on all content pages; left off thank-you, search and 404 to follow AdSense policy) |
| Manual ad units (optional) | `src/kit.py` → `AD_SLOTS` (paste slot IDs to enable in-article/multiplex units; Auto ads work without them) |
| Donation links | `assets/js/pay-config.js` (PayPal, Stripe, Buy Me a Coffee; empty means the pledge form is used) |
| Canonical domain | `src/kit.py` → `BASE_URL` |
| Partnership link | `src/kit.py` → `PARTNER_URL` (web.works/contact) |

Form submissions are delivered by FormSubmit to the site inbox. The address never appears in the HTML; it is assembled at runtime in `assets/js/site.js`. **The first submission triggers a one-time FormSubmit activation email, which you must confirm.**

## Deploy (GitHub Pages, free)
1. Settings → Pages → *Deploy from a branch* → `main` / `(root)` → Save.
2. Custom domain: enter `high.school` (GitHub creates `CNAME`). At your DNS provider:
   - `A` @ → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - `CNAME` www → `webworksa1.github.io`
3. Tick **Enforce HTTPS** once the certificate is issued.
4. In AdSense, add the site `high.school`. `ads.txt` must be served at the domain root. Then enable Google's certified CMP under Privacy & messaging for EEA/UK/CH visitors.

## Docs
- `docs/STRATEGY.md`: idea, revenue model, numbers
- `docs/BUILD-PROMPT.md`: the phase-wise build prompt
- `docs/RESEARCH.md`: teardown of 47 competitor sites

## Trademark
High.School is an independent educational resource and claims no rights in the generic term "high school". Third-party marks (SAT®, AP®, PSAT/NMSQT®, ACT®, IB, National Merit®, etc.) belong to their owners. See `/trademark-disclosure/`.
