---
layout: research
title: "论文"
permalink: /zh/publications/
author_profile: false
lang: zh
lang_switch_url: /publications/
---

<section class="research-hero research-hero--text">
  <div class="research-hero__text">
    <p class="research-kicker">完整发表记录</p>
    <h1>论文</h1>
    <p class="research-lede">
      本页按紧凑的纯文本形式收录完整论文列表。与当前研究主线关系最紧密的工作放在主页，并配有项目介绍。
    </p>
    <div class="research-link-row">
      <a class="research-button" href="/zh/">代表论文</a>
      <a class="research-button research-button--secondary" href="https://scholar.google.com/citations?user=4n5whr0AAAAJ">Google Scholar</a>
      <a class="research-button research-button--secondary" href="/zh/research/cognitive-neuroscience/">研究计划</a>
    </div>
  </div>
</section>

<section class="research-section">
  <h2>完整列表</h2>
  <ol class="research-publication-list">
    {% for paper in site.data.publications_full_zh %}
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
