/*
 * Focus Integrity Engine — Zonules.com
 *
 * Deterministic, client-side, no network, no data collection.
 * Reads three governed JSON blocks embedded in the page (FIO, FIS, FIE)
 * and computes a Focus Integrity reading by inverting FIS criteria into
 * FIO classes. The reading is a pure function of the user's selections;
 * nothing is sent anywhere.
 *
 * Source of truth: data/focus-integrity-ontology.json,
 * data/focus-integrity-standard.json, data/focus-integrity-engine.json.
 * This file is inlined into static/engine/index.html by scripts/build_engine.py.
 */
(function () {
  "use strict";

  function readJSON(id) {
    var el = document.getElementById(id);
    if (!el) return null;
    try {
      return JSON.parse(el.textContent);
    } catch (e) {
      return null;
    }
  }

  var FIO = readJSON("fio-data");
  var FIS = readJSON("fis-data");
  var FIE = readJSON("fie-data");

  if (!FIO || !FIS || !FIE) {
    return; // Static fallback content remains visible; nothing to enhance.
  }

  var fisById = {};
  FIS.criteria.forEach(function (c) { fisById[c.id] = c; });
  var fioById = {};
  FIO.classes.forEach(function (c) { fioById[c.id] = c; });

  var STATES = ["intact", "at-risk", "failed"];
  var STATE_LABEL = { "intact": "Intact", "at-risk": "At risk", "failed": "Failed" };

  var app = document.getElementById("fie-app");
  if (!app) return;
  app.hidden = false;

  var state = { layer: null, selections: {} };

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === "text") node.textContent = attrs[k];
        else if (k === "html") node.innerHTML = attrs[k];
        else node.setAttribute(k, attrs[k]);
      });
    }
    (children || []).forEach(function (c) { if (c) node.appendChild(c); });
    return node;
  }

  function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }

  // Step 1 — layer chooser
  function renderLayers() {
    var wrap = el("fieldset", { "class": "fie-step", "aria-label": "Choose the seeing system" });
    wrap.appendChild(el("legend", { text: "1 · Which seeing system?" }));
    wrap.appendChild(el("p", { "class": "fie-thesis", text: FIE.thesis_line }));
    var list = el("div", { "class": "fie-layers" });
    Object.keys(FIE.layers).forEach(function (lid) {
      var L = FIE.layers[lid];
      var btn = el("button", { "type": "button", "class": "fie-layer", "data-layer": lid });
      btn.appendChild(el("span", { "class": "fie-layer-id", text: lid }));
      btn.appendChild(el("span", { "class": "fie-layer-label", text: L.label }));
      btn.appendChild(el("span", { "class": "fie-layer-framing", text: L.framing }));
      btn.addEventListener("click", function () { selectLayer(lid); });
      list.appendChild(btn);
    });
    wrap.appendChild(list);
    return wrap;
  }

  function selectLayer(lid) {
    state.layer = lid;
    state.selections = {};
    render();
    var q = document.getElementById("fie-questions");
    if (q) q.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  // Step 2 — criteria questions for the chosen layer
  function renderQuestions() {
    if (!state.layer) return null;
    var L = FIE.layers[state.layer];
    var wrap = el("fieldset", { "class": "fie-step", "id": "fie-questions" });
    wrap.appendChild(el("legend", { text: "2 · Test each criterion" }));

    L.criteria.forEach(function (cid) {
      var fis = fisById[cid];
      var prompt = L.prompts[cid];
      var row = el("div", { "class": "fie-q" });
      row.appendChild(el("p", { "class": "fie-q-text" }, [
        el("span", { "class": "fie-crit-id", text: fis.id + " · " + fis.name }),
        el("span", { "class": "fie-q-question", text: prompt.question })
      ]));
      var opts = el("div", { "class": "fie-opts", "role": "radiogroup", "aria-label": fis.name });
      STATES.forEach(function (st) {
        var id = "opt-" + cid + "-" + st;
        var label = el("label", { "class": "fie-opt", "for": id });
        var input = el("input", {
          "type": "radio", "name": "crit-" + cid, "id": id, "value": st
        });
        if (state.selections[cid] === st) input.checked = true;
        input.addEventListener("change", function () {
          state.selections[cid] = st;
        });
        label.appendChild(input);
        label.appendChild(el("span", { text: STATE_LABEL[st] }));
        opts.appendChild(label);
      });
      row.appendChild(opts);
      wrap.appendChild(row);
    });

    var actions = el("div", { "class": "fie-actions" });
    var run = el("button", { "type": "button", "class": "fie-run", text: "Compute reading" });
    run.addEventListener("click", computeReading);
    actions.appendChild(run);
    wrap.appendChild(actions);
    return wrap;
  }

  // Step 3 — deterministic reading
  function computeReading() {
    var L = FIE.layers[state.layer];
    var findings = [];
    var worst = "intact";

    L.criteria.forEach(function (cid) {
      var st = state.selections[cid] || "intact";
      if (st === "failed") worst = "failed";
      else if (st === "at-risk" && worst !== "failed") worst = "at-risk";
      if (st === "intact") return;
      var fis = fisById[cid];
      var fioId = fis.inverse_of;
      var fio = fioById[fioId];
      var sign = st === "failed" ? L.prompts[cid].failed_sign : L.prompts[cid].atrisk_sign;
      findings.push({
        criterion: fis, state: st, sign: sign, fio: fio,
        links: FIE.class_links[fioId] || []
      });
    });

    renderReading(worst, findings);
  }

  function verdictKey(worst) {
    if (worst === "failed") return "compromised";
    if (worst === "at-risk") return "at-risk";
    return "intact";
  }

  function renderReading(worst, findings) {
    var L = FIE.layers[state.layer];
    var out = document.getElementById("fie-reading");
    clear(out);
    out.hidden = false;

    var vkey = verdictKey(worst);
    out.appendChild(el("h2", { "class": "fie-verdict fie-verdict-" + worst, "tabindex": "-1",
      text: FIE.verdict_labels[vkey] }));
    out.appendChild(el("p", { "class": "fie-reading-sub",
      text: "Focus Integrity Assessment · " + L.label }));

    if (L.medical_guard) {
      out.appendChild(el("p", { "class": "fie-guard", text:
        "Educational reference only. This reading describes structural reasoning about focus. " +
        "It is not a diagnosis or assessment of any individual's eyes and is no substitute for a qualified eye-care professional." }));
    }

    if (!findings.length) {
      out.appendChild(el("p", { "class": "fie-clean", text:
        "Every applicable criterion is intact. Under this assessment, the suspension layer is holding focus." }));
    } else {
      var list = el("div", { "class": "fie-findings" });
      findings.forEach(function (f) {
        var card = el("article", { "class": "fie-finding fie-finding-" + f.state });
        card.appendChild(el("h3", {}, [
          el("span", { "class": "fie-finding-state", text: STATE_LABEL[f.state] }),
          el("span", { "class": "fie-finding-crit", text: f.criterion.id + " " + f.criterion.name })
        ]));
        card.appendChild(el("p", { "class": "fie-finding-sign", text: f.sign }));
        card.appendChild(el("p", { "class": "fie-finding-map" }, [
          el("span", { "class": "fie-arrow", text: "maps to " }),
          el("strong", { text: f.fio.id + " · " + f.fio.name })
        ]));
        card.appendChild(el("p", { "class": "fie-finding-claim", text: f.fio.governing_claim }));
        if (f.links.length) {
          var refs = el("p", { "class": "fie-finding-refs" });
          refs.appendChild(el("span", { text: "Reference: " }));
          f.links.forEach(function (href, i) {
            if (i) refs.appendChild(document.createTextNode(" · "));
            refs.appendChild(el("a", { "href": href, text: href }));
          });
          card.appendChild(refs);
        }
        list.appendChild(card);
      });
      out.appendChild(list);
    }

    out.appendChild(el("p", { "class": "fie-provenance", text:
      "Computed locally from FIO v" + FIO.version + " · FIS v" + FIS.version +
      " · FIE v" + FIE.version + ". No input left your device." }));

    var verdict = out.querySelector(".fie-verdict");
    if (verdict) verdict.focus();
  }

  function render() {
    clear(app);
    app.appendChild(renderLayers());
    var q = renderQuestions();
    if (q) app.appendChild(q);
  }

  render();
})();
