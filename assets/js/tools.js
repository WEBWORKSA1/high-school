/* High.School — interactive tools (vanilla JS) */
(function () {
  'use strict';
  var d = document, S = (window.HS && window.HS.store) || { get: function () { return null; }, set: function () {} };
  function $(s, r) { return (r || d).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); }
  function num(v, f) { var n = parseFloat(v); return isNaN(n) ? (f === undefined ? 0 : f) : n; }
  function money(n) { return '$' + Math.round(n).toLocaleString('en-US'); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function load(k, def) { try { var v = S.get(k); return v ? JSON.parse(v) : def; } catch (e) { return def; } }
  function save(k, v) { S.set(k, JSON.stringify(v)); }

  /* ================= GPA CALCULATOR ================= */
  var gpa = $('#gpa-tool');
  if (gpa) {
    var PTS = { 'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0 };
    var BONUS = { 'Regular': 0, 'Honors': 0.5, 'AP / IB / Dual': 1.0 };
    var body = $('#gpa-rows');
    function row(c) {
      c = c || { n: '', g: 'A', l: 'Regular', cr: 1 };
      var tr = d.createElement('tr');
      tr.innerHTML = '<td><input type="text" aria-label="Course name" placeholder="e.g. Algebra II" value="' + esc(c.n) + '"></td>' +
        '<td><select aria-label="Grade">' + Object.keys(PTS).map(function (k) { return '<option' + (k === c.g ? ' selected' : '') + '>' + k + '</option>'; }).join('') + '</select></td>' +
        '<td><select aria-label="Course level">' + Object.keys(BONUS).map(function (k) { return '<option' + (k === c.l ? ' selected' : '') + '>' + k + '</option>'; }).join('') + '</select></td>' +
        '<td><input type="number" aria-label="Credits" min="0" step="0.25" value="' + c.cr + '" style="max-width:84px"></td>' +
        '<td><button type="button" class="del" aria-label="Remove course">✕</button></td>';
      body.appendChild(tr);
    }
    function calc() {
      var tc = 0, uw = 0, wt = 0, rows = [];
      $$('tr', body).forEach(function (tr) {
        var f = $$('input,select', tr), g = f[1].value, l = f[2].value, cr = num(f[3].value);
        rows.push({ n: f[0].value, g: g, l: l, cr: cr });
        if (cr <= 0) return;
        var p = PTS[g]; tc += cr; uw += p * cr; wt += (p > 0 ? p + BONUS[l] : 0) * cr;
      });
      var pg = num($('#gpa-prior').value, NaN), pc = num($('#gpa-prior-cr').value, 0);
      var u = tc ? uw / tc : 0, wg = tc ? wt / tc : 0, cum = u;
      if (!isNaN(pg) && pc > 0) cum = (pg * pc + uw) / (pc + tc);
      $('#gpa-u').textContent = u.toFixed(2);
      $('#gpa-w').textContent = wg.toFixed(2);
      $('#gpa-c').textContent = cum.toFixed(2);
      $('#gpa-cr').textContent = tc;
      var tg = num($('#gpa-target').value, NaN), nx = num($('#gpa-next').value, 0), plan = $('#gpa-plan');
      if (plan && !isNaN(tg) && nx > 0) {
        var havePts = (!isNaN(pg) && pc > 0 ? pg * pc : 0) + uw, haveCr = (!isNaN(pg) && pc > 0 ? pc : 0) + tc;
        var needG = (tg * (haveCr + nx) - havePts) / nx;
        plan.className = 'form-status ' + (needG > 4 ? 'err' : 'ok');
        plan.textContent = needG > 4 ? 'You’d need above a 4.0 next term (' + needG.toFixed(2) + ') — spread the goal over more terms or credits.' :
          needG <= 0 ? 'You’re already above that target. Keep it up!' : 'You need about a ' + needG.toFixed(2) + ' unweighted GPA over the next ' + nx + ' credits to reach ' + tg.toFixed(2) + '.';
      }
      save('hs-gpa', rows);
    }
    var saved = load('hs-gpa', null);
    (saved && saved.length ? saved : [
      { n: 'English 10', g: 'A-', l: 'Honors', cr: 1 }, { n: 'Algebra II', g: 'B+', l: 'Regular', cr: 1 },
      { n: 'AP Biology', g: 'B', l: 'AP / IB / Dual', cr: 1 }, { n: 'US History', g: 'A', l: 'Regular', cr: 1 },
      { n: 'Spanish II', g: 'B+', l: 'Regular', cr: 1 }]).forEach(row);
    gpa.addEventListener('input', calc);
    gpa.addEventListener('change', calc);
    gpa.addEventListener('click', function (e) {
      if (e.target.classList.contains('del')) { e.target.closest('tr').remove(); calc(); }
    });
    $('#gpa-add').addEventListener('click', function () { row(); calc(); });
    $('#gpa-reset').addEventListener('click', function () { body.innerHTML = ''; row(); calc(); });
    calc();
  }

  /* ================= FINAL GRADE ================= */
  var fg = $('#final-tool');
  if (fg) {
    function fcalc() {
      var cur = num($('#fg-cur').value), w = num($('#fg-w').value) / 100, t = num($('#fg-t').value);
      var out = $('#fg-out'), note = $('#fg-note');
      if (w <= 0 || w >= 1) { out.textContent = '—'; note.textContent = 'Enter a final exam weight between 1% and 99%.'; return; }
      var need = (t - cur * (1 - w)) / w;
      out.textContent = need.toFixed(1) + '%';
      var best = cur * (1 - w) + 100 * w, worst = cur * (1 - w);
      $('#fg-best').textContent = best.toFixed(1) + '%';
      $('#fg-worst').textContent = worst.toFixed(1) + '%';
      note.textContent = need > 100 ? 'Above 100% — even a perfect final won’t reach this target. Ask about extra credit or retakes.' :
        need <= 0 ? 'You’ve already locked it in — even a zero on the final keeps your target.' :
        need > 90 ? 'Tough but possible. Start a daily review plan now.' : 'Very doable with a steady study plan.';
    }
    fg.addEventListener('input', fcalc); fcalc();
  }

  /* ================= CATEGORY GRADE ================= */
  var cg = $('#cat-tool');
  if (cg) {
    var cb = $('#cat-rows');
    function crow(c) {
      c = c || { n: '', w: 10, s: 90 };
      var tr = d.createElement('tr');
      tr.innerHTML = '<td><input type="text" aria-label="Category" value="' + esc(c.n) + '" placeholder="Category"></td>' +
        '<td><input type="number" aria-label="Weight percent" min="0" max="100" value="' + c.w + '"></td>' +
        '<td><input type="number" aria-label="Score percent" min="0" max="150" value="' + c.s + '"></td>' +
        '<td><button type="button" class="del" aria-label="Remove">✕</button></td>';
      cb.appendChild(tr);
    }
    function ccalc() {
      var tw = 0, ts = 0;
      $$('tr', cb).forEach(function (tr) { var f = $$('input', tr), w = num(f[1].value), s = num(f[2].value); tw += w; ts += w * s; });
      var g = tw ? ts / tw : 0;
      $('#cat-out').textContent = g.toFixed(1) + '%';
      $('#cat-w').textContent = tw + '%';
      var L = g >= 97 ? 'A+' : g >= 93 ? 'A' : g >= 90 ? 'A-' : g >= 87 ? 'B+' : g >= 83 ? 'B' : g >= 80 ? 'B-' : g >= 77 ? 'C+' : g >= 73 ? 'C' : g >= 70 ? 'C-' : g >= 67 ? 'D+' : g >= 63 ? 'D' : g >= 60 ? 'D-' : 'F';
      $('#cat-l').textContent = L;
      $('#cat-warn').textContent = tw !== 100 ? 'Weights add up to ' + tw + '%. Most syllabi total 100% — we normalize automatically.' : '';
    }
    [{ n: 'Tests', w: 40, s: 84 }, { n: 'Quizzes', w: 20, s: 90 }, { n: 'Homework', w: 20, s: 96 }, { n: 'Labs / Projects', w: 20, s: 88 }].forEach(crow);
    cg.addEventListener('input', ccalc);
    cg.addEventListener('click', function (e) { if (e.target.classList.contains('del')) { e.target.closest('tr').remove(); ccalc(); } });
    $('#cat-add').addEventListener('click', function () { crow(); ccalc(); });
    ccalc();
  }

  /* ================= SAT <-> ACT ================= */
  var sa = $('#satact-tool');
  if (sa) {
    var A2S = { 36: 1590, 35: 1540, 34: 1500, 33: 1460, 32: 1430, 31: 1400, 30: 1370, 29: 1340, 28: 1310, 27: 1280, 26: 1240, 25: 1210, 24: 1180, 23: 1140, 22: 1110, 21: 1080, 20: 1040, 19: 1010, 18: 970, 17: 930, 16: 890, 15: 850, 14: 800, 13: 760, 12: 710, 11: 670, 10: 630, 9: 590 };
    var S2A = [[1570, 36], [1530, 35], [1490, 34], [1450, 33], [1420, 32], [1390, 31], [1360, 30], [1330, 29], [1300, 28], [1260, 27], [1230, 26], [1200, 25], [1160, 24], [1130, 23], [1100, 22], [1060, 21], [1030, 20], [990, 19], [960, 18], [920, 17], [880, 16], [830, 15], [780, 14], [730, 13], [690, 12], [650, 11], [620, 10], [590, 9]];
    function pct(s) { // rough SAT percentile bands (illustrative)
      return s >= 1500 ? '~99th' : s >= 1400 ? '~94–98th' : s >= 1300 ? '~86–93rd' : s >= 1200 ? '~74–85th' : s >= 1100 ? '~58–73rd' : s >= 1000 ? '~40–57th' : s >= 900 ? '~22–39th' : 'below ~22nd';
    }
    function s2a() {
      var s = Math.round(num($('#sa-sat').value) / 10) * 10, a = '—';
      for (var i = 0; i < S2A.length; i++) if (s >= S2A[i][0]) { a = S2A[i][1]; break; }
      if (s < 590) a = 'Below 9';
      $('#sa-act-out').textContent = a; $('#sa-pct').textContent = pct(s);
    }
    function a2s() {
      var a = Math.round(num($('#sa-act').value)); var s = A2S[a];
      $('#sa-sat-out').textContent = s ? s : (a > 36 ? '—' : 'Below 590');
    }
    $('#sa-sat').addEventListener('input', s2a); $('#sa-act').addEventListener('input', a2s); s2a(); a2s();
  }

  /* ================= COLLEGE COST ================= */
  var cc = $('#cost-tool');
  if (cc) {
    function cost() {
      var C = num($('#cc-cost').value), Y = Math.max(0, num($('#cc-years').value)), N = Math.max(1, num($('#cc-len').value, 4)),
        inf = num($('#cc-inf').value) / 100, sav = num($('#cc-sav').value), m = num($('#cc-mo').value), r = num($('#cc-ret').value) / 100 / 12,
        aid = num($('#cc-aid').value);
      var total = 0; for (var k = 0; k < N; k++) total += Math.max(0, C - aid) * Math.pow(1 + inf, Y + k);
      var n = Y * 12, fv = r ? sav * Math.pow(1 + r, n) + m * (Math.pow(1 + r, n) - 1) / r : sav + m * n;
      var gap = Math.max(0, total - fv), need = n ? (r ? gap * r / (Math.pow(1 + r, n) - 1) : gap / n) : gap;
      $('#cc-total').textContent = money(total); $('#cc-fv').textContent = money(fv);
      $('#cc-gap').textContent = money(gap); $('#cc-need').textContent = n ? money(need) + '/mo' : '—';
    }
    cc.addEventListener('input', cost); cost();
  }

  /* ================= CREDIT TRACKER ================= */
  var ct = $('#credit-tool');
  if (ct) {
    var DEF = [['English / Language Arts', 4, 2], ['Mathematics', 3, 2], ['Science', 3, 1], ['Social Studies', 3, 1], ['World Language', 2, 1], ['Fine / Performing Arts', 1, 0], ['Physical Education & Health', 1.5, 1], ['Electives', 6.5, 2]];
    var data = load('hs-credits', null) || DEF;
    var tb = $('#credit-rows');
    function draw() {
      tb.innerHTML = '';
      data.forEach(function (r, i) {
        var tr = d.createElement('tr');
        tr.innerHTML = '<td><input type="text" aria-label="Subject area" value="' + esc(r[0]) + '"></td><td><input type="number" aria-label="Required credits" step="0.5" min="0" value="' + r[1] + '"></td><td><input type="number" aria-label="Earned credits" step="0.5" min="0" value="' + r[2] + '"></td><td><div class="meter" style="min-width:80px"><i></i></div></td><td><button type="button" class="del" data-i="' + i + '" aria-label="Remove">✕</button></td>';
        tb.appendChild(tr);
      });
      ctotal();
    }
    function ctotal() {
      var req = 0, got = 0;
      $$('tr', tb).forEach(function (tr, i) {
        var f = $$('input', tr); data[i] = [f[0].value, num(f[1].value), num(f[2].value)];
        req += data[i][1]; got += Math.min(data[i][2], data[i][1] || data[i][2]);
        $('.meter i', tr).style.width = (data[i][1] ? Math.min(100, data[i][2] / data[i][1] * 100) : 0) + '%';
      });
      $('#ct-req').textContent = req; $('#ct-got').textContent = got;
      $('#ct-left').textContent = Math.max(0, req - got);
      $('#ct-pct').textContent = (req ? Math.round(got / req * 100) : 0) + '%';
      save('hs-credits', data);
    }
    ct.addEventListener('input', ctotal);
    ct.addEventListener('click', function (e) { if (e.target.classList.contains('del')) { data.splice(+e.target.getAttribute('data-i'), 1); draw(); } });
    $('#ct-add').addEventListener('click', function () { data.push(['New area', 1, 0]); draw(); });
    $('#ct-reset').addEventListener('click', function () { data = DEF.map(function (r) { return r.slice(); }); draw(); });
    draw();
  }

  /* ================= STUDY TIMER ================= */
  var tm = $('#timer-tool');
  if (tm) {
    var modes = { focus: 25, short: 5, long: 15 }, mode = 'focus', left = 25 * 60, h = null, sessions = num(S.get('hs-pomo'), 0);
    var face = $('#tm-face'), startBtn = $('#tm-start');
    function fmt(s) { return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); }
    function paint() { face.textContent = fmt(left); d.title = fmt(left) + ' · Study Timer · High.School'; $('#tm-sessions').textContent = sessions; }
    function beep() { try { var a = new (window.AudioContext || window.webkitAudioContext)(), o = a.createOscillator(), g = a.createGain(); o.connect(g); g.connect(a.destination); o.frequency.value = 880; g.gain.value = .15; o.start(); setTimeout(function () { o.stop(); a.close(); }, 600); } catch (e) {} }
    function setMode(m) { mode = m; clearInterval(h); h = null; startBtn.textContent = 'Start'; left = num($('#tm-' + m).value, modes[m]) * 60; $$('[data-mode]', tm).forEach(function (b) { b.classList.toggle('active', b.getAttribute('data-mode') === m); }); paint(); }
    startBtn.addEventListener('click', function () {
      if (h) { clearInterval(h); h = null; startBtn.textContent = 'Resume'; return; }
      startBtn.textContent = 'Pause';
      h = setInterval(function () {
        left--; paint();
        if (left <= 0) {
          clearInterval(h); h = null; beep();
          if (mode === 'focus') { sessions++; S.set('hs-pomo', sessions); setMode(sessions % 4 === 0 ? 'long' : 'short'); }
          else setMode('focus');
          if (window.HS && HS.toast) HS.toast(mode === 'focus' ? 'Break over — back to focus!' : 'Nice work! Take a break.');
        }
      }, 1000);
    });
    $('#tm-reset').addEventListener('click', function () { setMode(mode); });
    $$('[data-mode]', tm).forEach(function (b) { b.addEventListener('click', function () { setMode(b.getAttribute('data-mode')); }); });
    $$('.tm-set', tm).forEach(function (i) { i.addEventListener('change', function () { setMode(mode); }); });
    $('#tm-clear').addEventListener('click', function () { sessions = 0; S.set('hs-pomo', 0); paint(); });
    setMode('focus');
  }

  /* ================= FLASHCARDS ================= */
  var fc = $('#flash-tool');
  if (fc) {
    var deck = load('hs-deck', null) || [
      { f: 'Mitochondria', b: 'Organelle that produces ATP through cellular respiration' },
      { f: 'Pythagorean theorem', b: 'a² + b² = c² for a right triangle' },
      { f: 'Thesis statement', b: 'A one- or two-sentence claim your essay argues and supports' },
      { f: 'Newton’s 2nd law', b: 'F = m·a — net force equals mass times acceleration' }];
    var at = 0, card = $('#fc-card');
    function show() {
      card.classList.remove('flipped');
      if (!deck.length) { $('#fc-front').textContent = 'Your deck is empty — add a card below.'; $('#fc-back').textContent = ''; $('#fc-pos').textContent = '0 / 0'; return; }
      at = (at + deck.length) % deck.length;
      $('#fc-front').textContent = deck[at].f; $('#fc-back').textContent = deck[at].b;
      $('#fc-pos').textContent = (at + 1) + ' / ' + deck.length;
      save('hs-deck', deck);
    }
    card.addEventListener('click', function () { card.classList.toggle('flipped'); });
    card.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); card.classList.toggle('flipped'); } });
    $('#fc-next').addEventListener('click', function () { at++; show(); });
    $('#fc-prev').addEventListener('click', function () { at--; show(); });
    $('#fc-shuffle').addEventListener('click', function () { for (var i = deck.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = deck[i]; deck[i] = deck[j]; deck[j] = t; } at = 0; show(); });
    $('#fc-del').addEventListener('click', function () { if (deck.length) { deck.splice(at, 1); show(); } });
    $('#fc-form').addEventListener('submit', function (e) {
      e.preventDefault(); var f = $('#fc-f').value.trim(), b = $('#fc-b').value.trim(); if (!f || !b) return;
      deck.push({ f: f, b: b }); at = deck.length - 1; $('#fc-f').value = ''; $('#fc-b').value = ''; show();
    });
    $('#fc-import').addEventListener('click', function () {
      var lines = $('#fc-bulk').value.split('\n'), n = 0;
      lines.forEach(function (l) { var p = l.split(/\s+[-–:]\s+|\t/); if (p.length >= 2) { deck.push({ f: p[0].trim(), b: p.slice(1).join(' - ').trim() }); n++; } });
      $('#fc-bulk').value = ''; at = deck.length - n; show(); if (window.HS && HS.toast) HS.toast(n + ' cards imported');
    });
    d.addEventListener('keydown', function (e) { if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return; if (e.key === 'ArrowRight') { at++; show(); } if (e.key === 'ArrowLeft') { at--; show(); } });
    show();
  }

  /* ================= ROADMAP CHECKLIST ================= */
  var rm = $('#roadmap-tool');
  if (rm) {
    var done = load('hs-roadmap', {});
    function rpaint() {
      $$('.grade', rm).forEach(function (g) {
        var boxes = $$('input', g), c = boxes.filter(function (b) { return b.checked; }).length;
        $('.meter i', g).style.width = (boxes.length ? c / boxes.length * 100 : 0) + '%';
        $('.cnt', g).textContent = c + '/' + boxes.length;
      });
    }
    $$('input[data-key]', rm).forEach(function (b) { b.checked = !!done[b.getAttribute('data-key')]; b.addEventListener('change', function () { done[b.getAttribute('data-key')] = b.checked; save('hs-roadmap', done); rpaint(); }); });
    rpaint();
  }

  /* ================= SCHOLARSHIP TRACKER ================= */
  var st = $('#sch-tool');
  if (st) {
    var list = load('hs-sch', []);
    function sdraw() {
      list.sort(function (a, b) { return (a.d || '9999') < (b.d || '9999') ? -1 : 1; });
      var tb = $('#sch-rows'), tot = 0, won = 0;
      tb.innerHTML = list.length ? '' : '<tr><td colspan="5" class="muted">No scholarships yet — add your first one above.</td></tr>';
      list.forEach(function (s, i) {
        tot += num(s.a); if (s.s === 'Won') won += num(s.a);
        var days = s.d ? Math.ceil((new Date(s.d) - new Date()) / 864e5) : null;
        var tr = d.createElement('tr');
        tr.innerHTML = '<td>' + esc(s.n) + '</td><td>' + money(num(s.a)) + '</td><td>' + (s.d || '—') + (days !== null ? ' <span class="tag ' + (days < 14 && days >= 0 ? 'hot' : '') + '">' + (days < 0 ? 'passed' : days + 'd') + '</span>' : '') + '</td>' +
          '<td><select data-i="' + i + '" aria-label="Status">' + ['Researching', 'Drafting', 'Submitted', 'Won', 'Not selected'].map(function (o) { return '<option' + (o === s.s ? ' selected' : '') + '>' + o + '</option>'; }).join('') + '</select></td>' +
          '<td><button class="del" data-x="' + i + '" aria-label="Remove">✕</button></td>';
        tb.appendChild(tr);
      });
      $('#sch-count').textContent = list.length; $('#sch-total').textContent = money(tot); $('#sch-won').textContent = money(won);
      save('hs-sch', list);
    }
    $('#sch-form').addEventListener('submit', function (e) {
      e.preventDefault(); list.push({ n: $('#sch-n').value, a: $('#sch-a').value, d: $('#sch-d').value, s: 'Researching' }); e.target.reset(); sdraw();
    });
    st.addEventListener('change', function (e) { var i = e.target.getAttribute('data-i'); if (i !== null) { list[+i].s = e.target.value; sdraw(); } });
    st.addEventListener('click', function (e) { var x = e.target.getAttribute('data-x'); if (x !== null) { list.splice(+x, 1); sdraw(); } });
    sdraw();
  }

  /* ================= DONATION UI ================= */
  var dn = $('#donate-tool');
  if (dn) {
    var amt = 15, freq = 'One-time';
    var cfg = window.HS_PAY || {};
    function dpaint() {
      $('#dn-amount').value = amt; $('#dn-label').textContent = '$' + amt + (freq === 'Monthly' ? '/month' : '');
      $('#dn-freq-field').value = freq;
    }
    $$('.tier', dn).forEach(function (t) { t.addEventListener('click', function () { $$('.tier', dn).forEach(function (x) { x.classList.remove('active'); }); t.classList.add('active'); amt = num(t.getAttribute('data-amt')); dpaint(); }); });
    $('#dn-custom').addEventListener('input', function (e) { var v = num(e.target.value); if (v > 0) { amt = v; $$('.tier', dn).forEach(function (x) { x.classList.remove('active'); }); dpaint(); } });
    $$('.toggle button', dn).forEach(function (b) { b.addEventListener('click', function () { $$('.toggle button', dn).forEach(function (x) { x.classList.remove('active'); }); b.classList.add('active'); freq = b.textContent.trim(); dpaint(); }); });
    $$('[data-pay]', dn).forEach(function (b) {
      var url = cfg[b.getAttribute('data-pay')];
      b.addEventListener('click', function (e) {
        if (url) { e.preventDefault(); window.open(url.replace('{amount}', amt), '_blank', 'noopener'); }
        else { e.preventDefault(); var p = $('#pledge'); p.scrollIntoView({ behavior: 'smooth' }); var sel = $('[name="Payment preference"]'); if (sel) sel.value = b.getAttribute('data-pay'); if (window.HS && HS.toast) HS.toast('Complete the pledge form — we’ll send secure payment details.'); }
      });
    });
    dpaint();
  }
})();
