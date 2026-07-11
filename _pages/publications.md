---
layout: research
title: "Publications"
permalink: /publications/
author_profile: false
---

<section class="research-hero research-hero--text">
  <div class="research-hero__text">
    <p class="research-kicker">Full publication list</p>
    <h1>Publications</h1>
    <p class="research-lede">
      This page keeps the full publication list in a compact text-only format. Representative works with
      project pages are highlighted on the homepage; this list preserves the broader publication record
      without images or project-page requirements.
    </p>
    <div class="research-link-row">
      <a class="research-button" href="/">Selected Publications</a>
      <a class="research-button research-button--secondary" href="https://scholar.google.com/citations?user=4n5whr0AAAAJ">Google Scholar</a>
      <a class="research-button research-button--secondary" href="/research/cognitive-neuroscience/">Research Program</a>
    </div>
  </div>
</section>

<section class="research-section">
  <h2>Full List</h2>
  <ol class="research-publication-list">
    {% for paper in site.data.publications_full %}
    <li>
      <p class="research-paper-title">{{ paper.title }}</p>
      <p class="research-paper-authors">{{ paper.authors }}</p>
      <p class="research-paper-meta">
        <strong>{{ paper.venue }}</strong>
        {% if paper.highlight and paper.highlight != "" %}
          <span>{{ paper.highlight }}</span>
        {% endif %}
      </p>
      {% if paper.links and paper.links.size > 0 %}
      <p class="research-paper-links">
        {% for link in paper.links %}
          <a href="{{ link.url }}">{{ link.label }}</a>{% unless forloop.last %}<span>/</span>{% endunless %}
        {% endfor %}
      </p>
      {% endif %}
    </li>
    {% endfor %}
  </ol>
</section>
