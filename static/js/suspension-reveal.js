/*
 * Suspension-Reveal — Zonules.com gateway interaction.
 *
 * Embodies the thesis in three meaningful states:
 *   held      — the lens appears in focus; the fibers are hidden.
 *   revealed  — the hidden zonular fibers that hold it become visible.
 *   collapsed — the fibers are cut; the lens drifts and focus is lost.
 *
 * The visitor is meant to feel that focus was never a property of the lens.
 * It was produced by hidden tension. No network, no data collection.
 * Inlined into static/gateway/index.html by scripts/build_gateway.py.
 */
(function () {
  "use strict";

  var STATES = {
    held: {
      cls: "",
      text: "This is the lens, apparently in focus. <strong>Nothing visible is holding it.</strong>"
    },
    revealed: {
      cls: "is-revealed",
      text: "These are the <strong>zonules</strong> — the hidden fibers that suspend the lens in precise tension. Focus was never the lens alone."
    },
    collapsed: {
      cls: "is-collapsed",
      text: "Cut the fibers and the lens is still present — but <strong>focus collapses.</strong> Focus is a product of hidden structural tension."
    }
  };
  var ORDER = ["held", "revealed", "collapsed"];

  var body = document.body;
  var svg = document.getElementById("gw-svg");
  var caption = document.getElementById("gw-caption");
  var controls = document.getElementById("gw-controls");
  if (!svg || !caption || !controls) return;

  // Signal JS is active: the CSS hides the static triptych and shows controls.
  body.classList.add("js");

  function setState(name) {
    var s = STATES[name];
    if (!s) return;
    svg.classList.remove("is-revealed", "is-collapsed");
    if (s.cls) svg.classList.add(s.cls);
    caption.innerHTML = s.text;
    var btns = controls.querySelectorAll(".gw-step");
    for (var i = 0; i < btns.length; i++) {
      btns[i].setAttribute("aria-pressed", btns[i].getAttribute("data-state") === name ? "true" : "false");
    }
  }

  ORDER.forEach(function (name) {
    var btn = controls.querySelector('.gw-step[data-state="' + name + '"]');
    if (btn) btn.addEventListener("click", function () { setState(name); });
  });

  setState("held");
})();
