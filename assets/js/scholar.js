(function () {
  "use strict";

  var snapshot = document.getElementById("scholar-snapshot");
  var widget = document.querySelector("[data-scholar-source]");
  if (!snapshot || !widget) return;

  var chinese = document.documentElement.lang === "zh";
  var locale = chinese ? "zh-CN" : "en-US";
  var currentDate = 0;

  function normalize(title) {
    return title.normalize("NFKC").toLowerCase().replace(/[^\p{L}\p{N}]/gu, "");
  }

  function render(data) {
    var updated = Date.parse(data.updated_at);
    if (data.profile_id !== "4n5whr0AAAAJ" || !Number.isFinite(updated) || updated < currentDate) return;
    var keys = ["citations", "h_index", "i10_index"];
    if (!keys.every(function (key) { return Number.isSafeInteger(data[key]) && data[key] >= 0; })) return;
    if (!Array.isArray(data.papers) || !data.papers.length) return;
    currentDate = updated;
    document.querySelectorAll("[data-scholar-metric]").forEach(function (node) {
      node.textContent = new Intl.NumberFormat(locale).format(data[node.dataset.scholarMetric]);
    });
    document.querySelectorAll("[data-scholar-updated]").forEach(function (node) {
      node.dateTime = data.updated_at;
      node.textContent = new Intl.DateTimeFormat(locale, { year: "numeric", month: "short", day: "numeric" }).format(updated);
      node.title = new Intl.DateTimeFormat(locale, { dateStyle: "long", timeStyle: "short" }).format(updated);
    });
    var byTitle = new Map();
    var byId = new Map();
    data.papers.forEach(function (paper) {
      if (typeof paper.title !== "string" || !Number.isSafeInteger(paper.citations) || paper.citations < 0) return;
      if (typeof paper.url !== "string" || !paper.url.startsWith("https://scholar.google.com/citations?")) return;
      byTitle.set(normalize(paper.title), paper);
      byId.set(paper.id, paper);
    });
    document.querySelectorAll("[data-scholar-title]").forEach(function (node) {
      var paper = byId.get(node.dataset.scholarId) || byTitle.get(normalize(node.dataset.scholarTitle)) || byTitle.get(normalize(node.dataset.scholarAlias || ""));
      node.hidden = !paper || paper.citations < 50;
      if (node.hidden) return;
      node.textContent = new Intl.NumberFormat(locale).format(paper.citations) + (chinese ? " 次引用" : paper.citations === 1 ? " citation" : " citations");
      node.href = paper.url;
      node.title = (chinese ? "Google Scholar 数据更新于 " : "Google Scholar, updated ") + new Date(updated).toLocaleDateString(locale);
    });
  }

  try { render(JSON.parse(snapshot.textContent)); } catch (_) { /* The rendered snapshot stays visible. */ }

  var local = ["127.0.0.1", "localhost", "[::1]"].includes(window.location.hostname);
  var source = local ? "/scholar.json" : widget.dataset.scholarSource;
  var controller = new AbortController();
  var timeout = window.setTimeout(function () { controller.abort(); }, 8000);
  fetch(source + "?v=" + Math.floor(Date.now() / 3600000), { signal: controller.signal, cache: "no-cache" })
    .then(function (response) { if (!response.ok) throw new Error("Scholar snapshot unavailable"); return response.json(); })
    .then(render)
    .catch(function () { /* Keep the last verified counts and their original date. */ })
    .finally(function () { window.clearTimeout(timeout); });
})();
