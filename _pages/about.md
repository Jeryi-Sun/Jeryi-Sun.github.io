---
layout: research
permalink: /
title: "Zhongxiang Sun (孙忠祥)"
excerpt: "About me"
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="research-profile">
  <div>
    <p class="research-kicker">Large-model agents | Hallucination | Mechanistic interpretability | Search</p>
    <h1>Zhongxiang Sun (孙忠祥)</h1>
    <p>
      I am a Ph.D. candidate at the Gaoling School of Artificial Intelligence, Renmin University of China,
      advised by Prof. Jun Xu. My research focuses on trustworthy LLM agents, especially hallucination
      mechanisms, reasoning and planning, information retrieval, explainability, and legal AI. I use
      cognitive-neuroscience-inspired task design, behavior analysis, representation analysis, mechanism
      intervention, and process-level control to study these systems.
    </p>
    <p>
      I expect to graduate in June 2027 and am seeking research positions. If you are interested in
      trustworthy LLMs and agents, their synergy with information retrieval, applied mechanistic
      interpretability, or cognitive-neuroscience-inspired AI, I would welcome the opportunity to discuss.
    </p>
    <div class="research-link-row">
      <a class="research-button" href="mailto:sunzhongxiang@ruc.edu.cn">Email</a>
      <a class="research-button research-button--secondary" href="https://scholar.google.com/citations?user=4n5whr0AAAAJ">Google Scholar</a>
      <a class="research-button research-button--secondary" href="https://github.com/Jeryi-Sun">GitHub</a>
    </div>
  </div>
  <img src="/images/profile.png" alt="Zhongxiang Sun">
</section>

<section class="research-section research-impact">
  <h2>Impact Snapshot</h2>
  <div class="research-evidence-list">
    <article>
      <span>Contribution</span>
      <strong>A thesis-level program on trustworthy LLM agents</strong>
      <p>
        The work connects internal organization, module-level hallucination mechanisms, and long-horizon
        metacognitive control into one coherent research program.
      </p>
    </article>
    <article>
      <span>Evidence</span>
      <strong>First-author work across ICLR, SIGIR, and ACL</strong>
      <p>
        Representative projects cover retrieval-augmented generation, large reasoning models,
        personalized LLMs, process rewarding, and deep-search agents.
      </p>
    </article>
    <article>
      <span>Recognition</span>
      <strong>ICLR Spotlight, SIGIR-AP Best Paper Award, and Paper Digest Hot Papers</strong>
      <p>
        Selected work received an ICLR Spotlight, won the SIGIR-AP Best Paper Award, and was selected by
        Paper Digest as Hot Papers at SIGIR and CIKM.
      </p>
    </article>
    <article>
      <span>Public Assets</span>
      <strong>NeuroCogMap website, code, and full publication record</strong>
      <p>
        The site links project pages, source artifacts, and a compact full publication list for fast
        faculty-level evaluation of scope, continuity, and impact.
      </p>
    </article>
  </div>
</section>

<section class="research-section">
  <h2>Research</h2>
  <p class="research-section-intro">
    My research studies large-model agents as complex artificial intelligent systems that perceive context,
    reason over goals, call tools, use memory, interact with humans and other agents, and act in changing
    environments. I build cognitive-neuroscience-inspired methods for explaining and controlling these
    systems: task paradigms reveal behavioral boundaries, representation analysis locates internal
    structure, mechanism intervention validates causal pathways, and process-level monitoring turns
    diagnosis into control.
  </p>
  <div class="research-program-path">
    <article>
      <span class="research-tag">Explain</span>
      <div>
        <h3>Internal Cognitive Organization</h3>
        <p>
          I build NeuroCogMap-style internal cognitive maps that connect sparse features, functional parcels,
          capability hierarchy, and pathology localization.
        </p>
      </div>
      <a href="/research/cognitive-neuroscience/#internal-organization">Explore internal organization</a>
    </article>
    <article>
      <span class="research-tag">Locate</span>
      <div>
        <h3>Agent Module Mechanisms</h3>
        <p>
          I analyze tool evidence use, temporal reasoning dynamics, and personalized-memory drift through
          ReDeEP, RHD, and FPPS.
        </p>
      </div>
      <a href="/research/cognitive-neuroscience/#module-mechanisms">View module mechanisms</a>
    </article>
    <article>
      <span class="research-tag">Regulate</span>
      <div>
        <h3>Metacognitive Control</h3>
        <p>
          I design process reward, hierarchical monitoring, reflection, corrective action, and experience
          updating through ReARTeR and DS-MCM.
        </p>
      </div>
      <a href="/research/cognitive-neuroscience/#metacognitive-control">View metacognitive control</a>
    </article>
  </div>
</section>

<section class="research-section">
  <div class="research-section-heading">
    <div>
      <h2>Selected Publications</h2>
      <p>
        Representative work with project pages. The complete publication list is maintained separately as a
        compact text list.
      </p>
    </div>
    <a class="research-button research-button--secondary" href="/publications/">Full Publication List</a>
  </div>
  {% assign homepage_projects = site.data.research_projects | where: "show_on_homepage", true | sort: "homepage_priority" %}
  {% for project in homepage_projects %}
  <article class="research-publication">
    <a href="{{ project.project_url }}"><img src="{{ project.teaser }}" alt="{{ project.short_title }} teaser"></a>
    <div>
      <h3><a href="{{ project.project_url }}">{{ project.title }}</a></h3>
      <p><strong>{{ project.venue }}</strong> | {{ project.role }} | {{ project.layer }}</p>
      <p>{{ project.one_liner }}</p>
      <div class="research-link-row">
        {% if project.paper_url and project.paper_url != "" %}
          <a href="{{ project.paper_url }}">paper</a>
        {% endif %}
        <a href="{{ project.project_url }}">project</a>
        {% if project.code_url and project.code_url != "" %}
          <a href="{{ project.code_url }}">code</a>
        {% endif %}
      </div>
    </div>
  </article>
  {% endfor %}
</section>

<section class="research-section">
  <h2>Education</h2>
  <ul>
    <li><strong>08.2022-present</strong> Ph.D. candidate, Gaoling School of Artificial Intelligence, Renmin University of China.</li>
    <li><strong>08.2018-06.2022</strong> Bachelor of Computer Science and Technology, Beijing Jiaotong University (ranked 1st, top 0.4%).</li>
  </ul>
</section>

<section class="research-section">
  <h2>Awards</h2>
  <ul>
    <li>The National Scholarship 2024, selected as one of the 100 national representatives of Graduate National Scholarship recipients in China. <a href="https://www.peopleapp.com/column/30048976446-500006240986">News</a></li>
    <li>2024 China Association for Science and Technology Youth Talent Support Program for Ph.D. Students.</li>
    <li>Renmin University of China Innovative Talent Program.</li>
    <li>SIGIR-AP 2024 Best Paper Award.</li>
    <li>First Prize in the inaugural Artificial Intelligence and Smart Governance Innovation and Entrepreneurship Competition for University Students.</li>
  </ul>
</section>

<section class="research-section">
  <h2>Teaching</h2>
  <ul>
    <li>Teaching Assistant, Introduction to Big Data Analytics, Renmin University of China, Fall 2022 and Fall 2023.</li>
    <li>Teaching Assistant, Python, Renmin University of China, Spring 2023.</li>
  </ul>
</section>

<section class="research-section">
  <h2>Experience</h2>
  <ul>
    <li><strong>NTU</strong>, visiting student, Sep. 2025-Mar. 2026. Advisor: Yang Liu.</li>
    <li><strong>Kuaishou</strong>, research intern, Feb. 2022-Jun. 2025. Advisors: Xiaoxue Zang, Kai Zheng, Yang Song.</li>
    <li><a href="http://cail.cipsc.org.cn/index.html"><strong>CAIL 2022</strong></a>, committee member.</li>
    <li><strong>WWW 2024, 2025</strong>, reviewer.</li>
    <li><strong>SIGIR 2024, 2025</strong>, program committee member.</li>
    <li><strong>TOIS</strong>, reviewer.</li>
    <li><strong>TASLP</strong>, reviewer.</li>
    <li><strong>CIKM 2023, 2024</strong>, program committee member.</li>
    <li><strong>NeurIPS 2025</strong>, reviewer.</li>
    <li><strong>ICLR 2026</strong>, reviewer.</li>
  </ul>
</section>

<section class="research-section">
  <h2>Talks</h2>
  <ul>
    <li>Renmin University of China's First "Frontiers of Innovation: International Academic Symposium for Doctoral Students": Accurate and Explainable Legal Case Matching. <a href="https://drive.google.com/file/d/1TxD8YiEUV4R7nvxL46bRJ_YGata4P8QZ/view?usp=sharing">Slides</a></li>
    <li>Invited participant, Zhongguancun Science City "Rixin Youth Talk" Forum. <a href="https://mp.weixin.qq.com/s/_31wIQDcXwO5QquX6EUAMw">News</a></li>
  </ul>
</section>
