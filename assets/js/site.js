/* High.School — core site script (no dependencies) */
(function () {
  'use strict';
  var d = document, w = window;
  var ROOT = (d.body && d.body.getAttribute('data-root')) || './';

  /* ---------- storage helpers (never throw) ---------- */
  var store = {
    get: function (k) { try { return w.localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { w.localStorage.setItem(k, v); } catch (e) {} },
    sget: function (k) { try { return w.sessionStorage.getItem(k); } catch (e) { return null; } },
    sset: function (k, v) { try { w.sessionStorage.setItem(k, v); } catch (e) {} }
  };
  w.HS = w.HS || {};
  w.HS.store = store;

  /* ---------- contact route (assembled at runtime, never in markup) ---------- */
  var _r = [116,118,106,53,115,112,104,116,110,71,56,104,122,114,121,118,126,105,108,126];
  function route() { return _r.map(function (c) { return String.fromCharCode(c - 7); }).reverse().join(''); }
  w.HS.endpoint = function () { return 'https://formsubmit.co/ajax/' + route(); };

  d.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('[data-mail]');
    if (!a) return;
    ev.preventDefault();
    var subj = a.getAttribute('data-mail') || 'High.School inquiry';
    w.location.href = 'mai' + 'lto:' + route() + '?subject=' + encodeURIComponent(subj);
  });

  /* ---------- theme ---------- */
  var themeBtn = d.querySelector('[data-theme-toggle]');
  if (themeBtn) themeBtn.addEventListener('click', function () {
    var cur = d.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    d.documentElement.setAttribute('data-theme', cur);
    store.set('hs-theme', cur);
  });

  /* ---------- nav: drawer + dropdowns ---------- */
  var drawer = d.getElementById('drawer');
  d.querySelectorAll('[data-drawer]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!drawer) return;
      var open = drawer.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  if (drawer) drawer.addEventListener('click', function (e) { if (e.target === drawer) drawer.classList.remove('open'); });
  d.querySelectorAll('.menu > li > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentElement, open = !li.classList.contains('open');
      d.querySelectorAll('.menu > li.open').forEach(function (x) { x.classList.remove('open'); });
      if (open) li.classList.add('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  d.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      d.querySelectorAll('.menu > li.open').forEach(function (x) { x.classList.remove('open'); });
      if (drawer) drawer.classList.remove('open');
      var s = d.getElementById('slidein'); if (s) s.classList.remove('show');
    }
  });
  d.addEventListener('click', function (e) {
    if (!e.target.closest('.menu')) d.querySelectorAll('.menu > li.open').forEach(function (x) { x.classList.remove('open'); });
  });

  /* ---------- toast ---------- */
  function toast(msg) {
    var t = d.getElementById('toast'); if (!t) return;
    t.textContent = msg; t.classList.add('show');
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('show'); }, 3200);
  }
  w.HS.toast = toast;

  /* ---------- forms ---------- */
  function formToObject(form) {
    var o = {}, fd = new FormData(form);
    fd.forEach(function (v, k) {
      if (k === '_honey') return;
      if (o[k]) o[k] = o[k] + ', ' + v; else o[k] = v;
    });
    if (o['Email']) o._replyto = o['Email'];
    o._template = 'table';
    o['Page'] = d.title + ' — ' + w.location.pathname;
    o['Submitted'] = new Date().toISOString();
    return o;
  }
  function submitForm(form) {
    var status = form.querySelector('.form-status');
    var btn = form.querySelector('[type=submit]');
    var hp = form.querySelector('[name=_honey]');
    if (hp && hp.value) return; // bot
    var age = form.querySelector('[name="I am"]:checked, select[name="I am"]');
    if (age && /under 13/i.test(age.value)) {
      if (status) { status.className = 'form-status err'; status.textContent = 'Sorry — High.School forms are for ages 13+. Please ask a parent or guardian to contact us.'; }
      return;
    }
    var minor = form.querySelector('[data-minor-check]');
    if (minor && age && /13.?17/.test(age.value) && !minor.checked) {
      if (status) { status.className = 'form-status err'; status.textContent = 'Please confirm a parent or guardian has approved this request.'; }
      minor.focus(); return;
    }
    var data = formToObject(form);
    if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = 'Sending…'; }
    if (status) { status.className = 'form-status'; status.textContent = ''; }
    fetch(w.HS.endpoint(), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(data)
    }).then(function (r) { return r.json().catch(function () { return {}; }); })
      .then(function () {
        store.set('hs-lead', '1');
        var thanks = form.getAttribute('data-thanks');
        if (thanks) { w.location.href = ROOT + thanks; return; }
        form.reset();
        if (status) { status.className = 'form-status ok'; status.textContent = form.getAttribute('data-ok') || 'Thank you! We received your message and will reply soon.'; }
        toast('Sent — thank you!');
      })
      .catch(function () {
        if (status) { status.className = 'form-status err'; status.textContent = 'Network issue — please try again in a moment.'; }
      })
      .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn._t; } });
  }
  w.HS.submitForm = submitForm;
  d.querySelectorAll('form[data-form]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!f.checkValidity()) { f.reportValidity(); return; }
      submitForm(f);
    });
  });

  /* ---------- multi-step lead form ---------- */
  d.querySelectorAll('[data-stepper]').forEach(function (form) {
    var steps = form.querySelectorAll('.step'), i = 0;
    var bar = form.querySelector('.progress i'), count = form.querySelector('.step-count');
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle('active', k === n); });
      if (bar) bar.style.width = ((n + 1) / steps.length * 100) + '%';
      if (count) count.textContent = 'Step ' + (n + 1) + ' of ' + steps.length;
      var pb = form.querySelector('[data-prev]'), nb = form.querySelector('[data-next]');
      if (pb) pb.style.visibility = n === 0 ? 'hidden' : 'visible';
      if (nb) nb.style.display = n === steps.length - 1 ? 'none' : '';
      var minorWrap = form.querySelector('[data-minor-wrap]');
      var role = form.querySelector('[name="I am"]:checked');
      if (minorWrap) minorWrap.style.display = role && /13.?17/.test(role.value) ? 'flex' : 'none';
      i = n;
    }
    function valid(step) {
      var ok = true;
      step.querySelectorAll('input,select,textarea').forEach(function (el) {
        if (!ok) return;
        if (!el.checkValidity()) { el.reportValidity(); ok = false; }
      });
      var groups = step.querySelectorAll('[data-require-one]');
      groups.forEach(function (g) {
        if (!ok) return;
        if (!g.querySelector('input:checked')) { ok = false; toast(g.getAttribute('data-require-one')); }
      });
      return ok;
    }
    form.addEventListener('click', function (e) {
      var n = e.target.closest('[data-next]'), p = e.target.closest('[data-prev]');
      if (n) { e.preventDefault(); if (!valid(steps[i])) return;
        var role = form.querySelector('[name="I am"]:checked');
        if (role && /under 13/i.test(role.value)) { toast('High.School forms are for ages 13+. Please ask a parent or guardian.'); return; }
        show(Math.min(i + 1, steps.length - 1)); form.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
      if (p) { e.preventDefault(); show(Math.max(i - 1, 0)); }
    });
    var pre = new URLSearchParams(w.location.search).get('need');
    if (pre) { var el = form.querySelector('input[name="I need"][value="' + pre.replace(/"/g, '') + '"]'); if (el) el.checked = true; }
    show(0);
  });

  /* ---------- cookie notice ---------- */
  var ck = d.getElementById('cookie');
  if (ck && !store.get('hs-consent')) ck.classList.add('show');
  d.querySelectorAll('[data-consent]').forEach(function (b) {
    b.addEventListener('click', function () {
      store.set('hs-consent', b.getAttribute('data-consent'));
      if (ck) ck.classList.remove('show');
      if (b.getAttribute('data-consent') === 'reject') toast('Saved. Ads will be non-personalized.');
    });
  });

  /* ---------- lead slide-in (once per session, after engagement) ---------- */
  var si = d.getElementById('slidein');
  if (si && !d.body.hasAttribute('data-noslide') && !store.sget('hs-slide') && !store.get('hs-lead')) {
    var shown = false;
    function pop() { if (shown) return; shown = true; si.classList.add('show'); store.sset('hs-slide', '1'); }
    setTimeout(pop, 45000);
    w.addEventListener('scroll', function () {
      var h = d.documentElement; if ((h.scrollTop + w.innerHeight) / h.scrollHeight > 0.6) pop();
    }, { passive: true });
    var x = si.querySelector('.x'); if (x) x.addEventListener('click', function () { si.classList.remove('show'); });
  }

  /* ---------- lite YouTube embeds ---------- */
  d.querySelectorAll('.video[data-yt]').forEach(function (v) {
    function load() {
      var id = v.getAttribute('data-yt');
      var f = d.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
      f.title = v.getAttribute('data-title') || 'Video';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      f.allowFullscreen = true;
      v.innerHTML = ''; v.appendChild(f);
    }
    v.addEventListener('click', load);
    v.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); load(); } });
  });

  /* ---------- practice quizzes ---------- */
  d.querySelectorAll('[data-quiz]').forEach(function (qz) {
    var total = qz.querySelectorAll('.q').length, right = 0, done = 0;
    var out = qz.querySelector('.score');
    qz.querySelectorAll('.q').forEach(function (q) {
      q.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function () {
          if (q.classList.contains('done')) return;
          q.classList.add('done'); done++;
          var ok = b.hasAttribute('data-correct');
          b.classList.add(ok ? 'right' : 'wrong');
          if (ok) right++; else { var c = q.querySelector('[data-correct]'); if (c) c.classList.add('right'); }
          if (out) out.textContent = 'Score: ' + right + ' / ' + total + (done === total ? (right === total ? ' — perfect! 🎉' : ' — review the explanations above.') : '');
        });
      });
    });
  });

  /* ---------- filter chips (videos, guides) ---------- */
  d.querySelectorAll('[data-filter-group]').forEach(function (g) {
    var target = d.querySelector(g.getAttribute('data-filter-group'));
    g.addEventListener('click', function (e) {
      var c = e.target.closest('[data-filter]'); if (!c || !target) return;
      g.querySelectorAll('[data-filter]').forEach(function (x) { x.classList.remove('active'); x.setAttribute('aria-pressed', 'false'); });
      c.classList.add('active'); c.setAttribute('aria-pressed', 'true');
      var f = c.getAttribute('data-filter');
      target.querySelectorAll('[data-cat]').forEach(function (it) {
        it.style.display = (f === 'all' || it.getAttribute('data-cat').indexOf(f) > -1) ? '' : 'none';
      });
    });
  });

  /* ---------- search ---------- */
  function goSearch(q) { w.location.href = ROOT + 'search/?q=' + encodeURIComponent(q); }
  d.querySelectorAll('form[data-search]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault(); var q = (f.querySelector('input').value || '').trim(); if (q) goSearch(q);
    });
  });
  var res = d.getElementById('search-results');
  if (res) {
    var q = new URLSearchParams(w.location.search).get('q') || '';
    var inp = d.getElementById('search-input'); if (inp) inp.value = q;
    function render(idx, term) {
      term = term.toLowerCase().trim();
      if (!term) { res.innerHTML = '<p class="muted">Type a topic like “GPA”, “SAT”, “essay” or “chemistry”.</p>'; return; }
      var words = term.split(/\s+/);
      var hits = idx.map(function (p) {
        var hay = (p.t + ' ' + p.d + ' ' + p.k).toLowerCase(), s = 0;
        words.forEach(function (wd) { if (hay.indexOf(wd) > -1) s += 1; if (p.t.toLowerCase().indexOf(wd) > -1) s += 3; });
        return { p: p, s: s };
      }).filter(function (h) { return h.s > 0; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 25);
      res.innerHTML = hits.length ? hits.map(function (h) {
        return '<a href="' + ROOT + h.p.u + '"><strong>' + h.p.t + '</strong><br><small>' + h.p.d + '</small></a>';
      }).join('') : '<p>No results for “' + term.replace(/</g, '&lt;') + '”. Try a broader word, or <a href="' + ROOT + 'get-matched/">ask us for help</a>.</p>';
    }
    fetch(ROOT + 'search-index.json').then(function (r) { return r.json(); }).then(function (idx) {
      render(idx, q);
      if (inp) inp.addEventListener('input', function () { render(idx, inp.value); });
    }).catch(function () { res.innerHTML = '<p>Search is loading slowly — please refresh.</p>'; });
  }

  /* ---------- year ---------- */
  d.querySelectorAll('[data-year]').forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();
