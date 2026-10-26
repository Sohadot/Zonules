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
 *
 * classify() is the whole assessment protocol (FIA). It is a pure function and
 * is exported for scripts/test_engine.js, so the worked examples published on
 * the page are reproduced by the same code visitors run.
 */
(function () {
  "use strict";

  // FIA: a pure function of (layer, selections). Unanswered applicable criteria
  // are "not-assessed" (never counted as intact); criteria outside the layer's
  // scope are "not-applicable" and never scored.
  function classify(FIE, FIS, layerId, selections) {
    var L = FIE.layers[layerId];
    var sel = selections || {};
    var criteria = [], classes = {}, notApplicable = [], notAssessed = [];
    var anyFailed = false, anyAtRisk = false;

    FIS.criteria.forEach(function (c) {
      if (L.criteria.indexOf(c.id) === -1) {
        notApplicable.push(c.id);
        criteria.push({ id: c.id, state: "not-applicable" });
        return;
      }
      var st = sel[c.id];
      if (st !== "intact" && st !== "at-risk" && st !== "failed") {
        notAssessed.push(c.id);
        criteria.push({ id: c.id, state: "not-assessed" });
        return;
      }
      criteria.push({ id: c.id, state: st });
      if (st === "failed") { anyFailed = true; classes[c.inverse_of] = "failed"; }
      else if (st === "at-risk") { anyAtRisk = true; classes[c.inverse_of] = "at-risk"; }
    });

    var verdict = anyFailed ? "compromised"
      : anyAtRisk ? "at-risk"
      : notAssessed.length ? "incomplete"
      : "intact";
    return { layer: layerId, verdict: verdict, classes: classes, criteria: criteria,
             not_applicable: notApplicable, not_assessed: notAssessed };
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { classify: classify };
  }
  if (typeof document === "undefined") return;

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
  var STATE_LABEL = { "intact": "Intact", "at-risk": "At risk", "failed": "Failed",
    "not-assessed": "Not assessed", "not-applicable": "Not applicable" };
  var VERDICT_CLASS = { "compromised": "failed", "at-risk": "at-risk", "intact": "intact", "incomplete": "incomplete" };

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
      var btn = el("button", { "type": "button", "class": "fie-layer", "data-layer": lid,
        "aria-pressed": state.layer === lid ? "true" : "false" });
      btn.appendChild(el("span", { "class": "fie-layer-id", text: lid }));
      btn.appendChild(el("span", { "class": "fie-layer-label", text: L.label }));
      btn.appendChild(el("span", { "class": "fie-layer-framing", text: L.framing }));
      btn.addEventListener("click", function () { selectLayer(lid); });
      list.appendChild(btn);
    });
    wrap.appendChild(list);
    if (FIE.examples && FIE.examples.length) {
      var ex = el("div", { "class": "fie-presets", "role": "group", "aria-label": "Load a worked example" });
      ex.appendChild(el("span", { "class": "fie-presets-label", text: "Or load a worked example:" }));
      FIE.examples.forEach(function (e) {
        var b = el("button", { "type": "button", "class": "fie-preset", text: e.id + " · " + e.title });
        b.addEventListener("click", function () { loadExample(e); });
        ex.appendChild(b);
      });
      wrap.appendChild(ex);
    }
    return wrap;
  }

  function loadExample(e) {
    state.layer = e.layer;
    state.selections = {};
    Object.keys(e.inputs).forEach(function (cid) {
      if (e.inputs[cid]) state.selections[cid] = e.inputs[cid];
    });
    state.example = e;
    render();
    computeReading();
  }

  function selectLayer(lid) {
    state.example = null;
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
          state.example = null; // edited inputs are no longer the published example
        });
        label.appendChild(input);
        label.appendChild(el("span", { text: STATE_LABEL[st] }));
        opts.appendChild(label);
      });
      row.appendChild(opts);
      wrap.appendChild(row);
    });

    Object.keys(L.not_applicable || {}).forEach(function (cid) {
      var fis = fisById[cid];
      wrap.appendChild(el("div", { "class": "fie-q fie-q-na" }, [
        el("p", { "class": "fie-q-text" }, [
          el("span", { "class": "fie-crit-id", text: fis.id + " · " + fis.name + " · not applicable" }),
          el("span", { "class": "fie-q-question", text: L.not_applicable[cid] })
        ])
      ]));
    });
    wrap.appendChild(el("p", { "class": "fie-note", text:
      "Leave a criterion unanswered if you cannot judge it. It is reported as not assessed and is never counted as intact." }));

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
    var result = classify(FIE, FIS, state.layer, state.selections);
    var findings = [];
    result.criteria.forEach(function (c) {
      if (c.state !== "failed" && c.state !== "at-risk") return;
      var fis = fisById[c.id];
      var fioId = fis.inverse_of;
      var sign = c.state === "failed" ? L.prompts[c.id].failed_sign : L.prompts[c.id].atrisk_sign;
      var notes = state.example && state.example.input_notes;
      if (notes && notes[c.id]) sign = notes[c.id];
      findings.push({
        criterion: fis, state: c.state, sign: sign, fio: fioById[fioId],
        links: FIE.class_links[fioId] || []
      });
    });
    renderReading(result, findings);
  }

  function renderReading(result, findings) {
    var L = FIE.layers[state.layer];
    var out = document.getElementById("fie-reading");
    clear(out);
    out.hidden = false;

    out.appendChild(el("h2", { "class": "fie-verdict fie-verdict-" + VERDICT_CLASS[result.verdict], "tabindex": "-1",
      text: FIE.verdict_labels[result.verdict] }));
    out.appendChild(el("p", { "class": "fie-reading-sub",
      text: "Focus Integrity Assessment · " + L.label +
        (state.example ? " · worked example " + state.example.id : "") }));

    if (L.medical_guard) {
      out.appendChild(el("p", { "class": "fie-guard", text:
        "Educational reference only. This reading describes structural reasoning about focus. " +
        "It is not a diagnosis or assessment of any individual's eyes and is no substitute for a qualified eye-care professional." }));
    }

    if (!findings.length && result.verdict === "intact") {
      out.appendChild(el("p", { "class": "fie-clean", text:
        "Every applicable criterion was judged intact. On the inputs supplied, no FIO class is triggered." }));
    } else if (!findings.length) {
      out.appendChild(el("p", { "class": "fie-note", text:
        "No criterion was judged at risk or failed, but not every applicable criterion was assessed, so integrity cannot be reported as intact." }));
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

    function stateLine(ids, label) {
      if (!ids.length) return;
      out.appendChild(el("p", { "class": "fie-note", text: label + ": " + ids.map(function (id) {
        return id + " " + fisById[id].name;
      }).join(" · ") + "." }));
    }
    stateLine(result.not_assessed, "Not assessed (not counted as intact)");
    stateLine(result.not_applicable, "Not applicable at this layer (not scored)");

    out.appendChild(el("p", { "class": "fie-note", text:
      "This reading classifies the judgements you supplied. It does not verify them, inspect any media, or replace domain-specific evaluation." }));

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
