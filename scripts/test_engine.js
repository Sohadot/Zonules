#!/usr/bin/env node
/*
 * Focus Integrity Engine — reproducibility tests.
 *
 * Runs the exact classify() function inlined into /focus-integrity-engine/
 * against the governed registries and checks:
 *   1. every published worked example reproduces its expected reading;
 *   2. identical inputs always yield identical results;
 *   3. not-applicable criteria are never scored, even if a value is supplied;
 *   4. unanswered criteria are reported as not assessed, never as intact.
 *
 * No dependencies, no network. Exit code 0 = pass, 1 = fail.
 * Usage: node scripts/test_engine.js
 */
"use strict";
var fs = require("fs");
var path = require("path");
var assert = require("assert");

var ROOT = path.resolve(__dirname, "..");
function load(rel) { return JSON.parse(fs.readFileSync(path.join(ROOT, rel), "utf8")); }

var classify = require(path.join(ROOT, "static/js/focus-integrity-engine.js")).classify;
var FIE = load("data/focus-integrity-engine.json");
var FIS = load("data/focus-integrity-standard.json");

var failures = 0, passed = 0;
function test(name, fn) {
  try { fn(); passed++; }
  catch (e) { failures++; console.log("FAIL " + name + ": " + e.message); }
}

function inputsOf(example) {
  var sel = {};
  Object.keys(example.inputs).forEach(function (k) {
    if (example.inputs[k]) sel[k] = example.inputs[k];
  });
  return sel;
}

(FIE.examples || []).forEach(function (ex) {
  test(ex.id + " reproduces its published reading", function () {
    var r = classify(FIE, FIS, ex.layer, inputsOf(ex));
    assert.strictEqual(r.verdict, ex.expected.verdict);
    assert.deepStrictEqual(r.classes, ex.expected.classes);
    assert.deepStrictEqual(r.not_applicable, ex.expected.not_applicable);
    assert.deepStrictEqual(r.not_assessed, ex.expected.not_assessed);
  });
  test(ex.id + " is deterministic", function () {
    var a = JSON.stringify(classify(FIE, FIS, ex.layer, inputsOf(ex)));
    for (var i = 0; i < 25; i++) {
      assert.strictEqual(JSON.stringify(classify(FIE, FIS, ex.layer, inputsOf(ex))), a);
    }
  });
  test(ex.id + " inputs are applicable to its layer", function () {
    Object.keys(ex.inputs).forEach(function (cid) {
      assert.ok(FIE.layers[ex.layer].criteria.indexOf(cid) !== -1, cid + " not applicable at " + ex.layer);
    });
  });
});

test("at least three worked examples cover L1, L2 and L3", function () {
  var layers = (FIE.examples || []).map(function (e) { return e.layer; }).sort();
  assert.deepStrictEqual(layers, ["L1", "L2", "L3"]);
});

test("not-applicable criteria are never scored", function () {
  var r = classify(FIE, FIS, "L1", { "FIS-1": "intact", "FIS-2": "intact", "FIS-3": "intact",
                                     "FIS-4": "failed", "FIS-5": "failed" });
  assert.strictEqual(r.verdict, "intact");
  assert.deepStrictEqual(r.classes, {});
  assert.deepStrictEqual(r.not_applicable, ["FIS-4", "FIS-5"]);
});

test("unanswered criteria are not counted as intact", function () {
  var r = classify(FIE, FIS, "L3", { "FIS-1": "intact" });
  assert.strictEqual(r.verdict, "incomplete");
  assert.deepStrictEqual(r.not_assessed, ["FIS-2", "FIS-3", "FIS-4", "FIS-5"]);
  var empty = classify(FIE, FIS, "L2", {});
  assert.strictEqual(empty.verdict, "incomplete");
});

test("failure dominates at-risk; each class maps to its FIS inverse", function () {
  var r = classify(FIE, FIS, "L2", { "FIS-1": "at-risk", "FIS-2": "intact", "FIS-3": "intact",
                                     "FIS-4": "failed", "FIS-5": "intact" });
  assert.strictEqual(r.verdict, "compromised");
  assert.deepStrictEqual(r.classes, { "FIO-01": "at-risk", "FIO-04": "failed" });
});

test("every layer's criteria and not-applicable notes partition FIS", function () {
  Object.keys(FIE.layers).forEach(function (lid) {
    var L = FIE.layers[lid];
    var na = Object.keys(L.not_applicable || {});
    FIS.criteria.forEach(function (c) {
      var inScope = L.criteria.indexOf(c.id) !== -1;
      var applicable = c.applicable_layers.indexOf(lid) !== -1;
      assert.strictEqual(inScope, applicable, lid + " " + c.id + " scope disagrees with FIS");
      if (!inScope) assert.ok(na.indexOf(c.id) !== -1, lid + " " + c.id + " lacks a not-applicable note");
    });
  });
});

if (failures) {
  console.log("ENGINE TESTS: FAIL (" + failures + " failed, " + passed + " passed)");
  process.exit(1);
}
console.log("ENGINE TESTS: PASS (" + passed + " checks)");
