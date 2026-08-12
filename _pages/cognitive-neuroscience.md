---
layout: research
title: "Cognitive Neuroscience of AI Agents"
permalink: /research/cognitive-neuroscience/
author_profile: false
lang: en
lang_switch_url: /zh/research/cognitive-neuroscience/
redirect_from:
  - /research/ai-cognitive-neuroscience/
---

<section class="research-hero research-hero--program">
  <div class="research-hero__heading">
    <p class="research-kicker">Research program</p>
    <h1>Cognitive Neuroscience of AI Agents</h1>
  </div>
  <div class="research-hero__text">
    <p class="research-lede">
      AI agents combine reasoning, memory, tools, interaction, and long-horizon action. My long-term program
      studies how their intelligence, knowledge, value, and action structures form, organize, evolve, and
      influence behavior. The near-term focus is how local anomalies propagate across goal, evidence, memory,
      tool feedback, and action, and how they can be diagnosed and recovered during execution.
    </p>
    <div class="research-link-row">
      <a class="research-button research-button--secondary" href="#papers">Current Work</a>
      <a class="research-button" href="#future-plan">Future: AI4Science</a>
    </div>
  </div>
  <figure class="research-hero__media research-program-overview">
    {% include optimized-image.html src="/images/research/cognitive-neuroscience-overview-en.png" alt="Research roadmap for long-horizon agent state distortion, propagation, causal localization, and trustworthy control" loading="eager" fetchpriority="high" %}
    <figcaption>
      From local mechanisms to long-horizon trustworthy control.
    </figcaption>
  </figure>
</section>

<nav class="research-anchor-nav" aria-label="On this page">
  <span>On this page</span>
  <a href="#why-this-program">Why the program</a>
  <a href="#the-object">Research object</a>
  <a href="#problem-groups">Four problem groups</a>
  <a href="#methodological-loop">Methodological loop</a>
  <a href="#papers">Current thesis</a>
  <a href="#future-plan">AI4Science</a>
</nav>

<section class="research-section" id="why-this-program">
  <h2>Why This Program</h2>
  <p>
    A research framework becomes necessary when a new object appears, existing frameworks explain only
    partial slices, stable problem groups repeatedly arise, a new method combination is required, and the
    object carries long-term social importance. AI agents now meet these conditions.
  </p>
  <div class="research-detail-list">
    <div class="research-detail-list__item">
      <h3>A New Object</h3>
      <p>
        Agent systems combine perception, language, reasoning, memory, tool use, interaction, long-horizon
        goals, multi-agent coordination, and emerging self-improvement loops.
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>Partial Existing Frames</h3>
      <p>
        Evaluation maps behavior; interpretability locates mechanisms; safety studies constraints. This
        program connects behavior, mechanism, knowledge, value, and action.
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>Stable Problem Groups</h3>
      <p>
        Recurring failures expose shared questions about how agent capabilities, internal knowledge,
        preferences, and actions form, update, and break down.
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>A Method Combination</h3>
      <p>
        Cognitive task design, behavior analysis, representation analysis, mechanism intervention, and
        process-level control form the methodological core.
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>Long-Term Importance</h3>
      <p>
        Autonomous, social, embodied, and self-improving agents require scientific tools for inspection,
        guidance, and human-agent coexistence.
      </p>
    </div>
  </div>
</section>

<section class="research-section" id="the-object">
  <h2>The Object: AI Agents as Complex Intelligent Systems</h2>
  <p>
    Earlier artificial systems usually had clearer task boundaries, ability boundaries, and behavioral
    boundaries. Modern AI agents increasingly form abilities through large-scale training, post-training,
    tool interaction, memory, and environmental feedback. They can transfer across tasks, organize
    long-horizon goals, call external tools, collaborate with other agents, and influence real environments.
  </p>
  <p>
    This object calls for a system-level account of internal organization and external action. The research
    target is the structure of agency itself: how an artificial system organizes intelligence, stores and
    uses knowledge, develops goal-directed tendencies, and turns model computation into sustained action.
  </p>
</section>

<section class="research-section" id="problem-groups">
  <h2>Four Problem Groups</h2>
  <p>
    The cognitive neuroscience of AI agents studies four linked structures. Each structure defines a set of
    empirical questions, mechanisms to locate, and interventions to test.
  </p>
  <div class="research-detail-list">
    <div class="research-detail-list__item">
      <h3>Intelligence Structure</h3>
      <p>
        Reasoning, planning, memory, abstraction, tool use, and long-horizon task organization emerge under
        training and interaction. I study how these abilities form, generalize, fluctuate, and fail.
      </p>
      <ul>
        <li>Which internal structures support reasoning, planning, and tool use?</li>
        <li>Which conditions make a capability stable, brittle, or misleading?</li>
        <li>How do post-training and environment interaction reshape capability use?</li>
      </ul>
    </div>
    <div class="research-detail-list__item">
      <h3>Knowledge Structure</h3>
      <p>
        Agents may store and recombine knowledge in forms that surface prompts reveal only partially. I
        study where knowledge is organized, how it is called, and how it can be translated into
        human-checkable evidence.
      </p>
      <ul>
        <li>Where do factual, procedural, and task-specific structures live internally?</li>
        <li>How do external evidence, parametric knowledge, and personalized memory interact?</li>
        <li>How can internal knowledge be tested and translated into inspectable forms?</li>
      </ul>
    </div>
    <div class="research-detail-list__item">
      <h3>Value Structure</h3>
      <p>
        Goals, preferences, and behavioral tendencies are shaped by training objectives, reward models,
        human feedback, deployment context, and social interaction. I treat value as an evolving structure
        that can be measured and guided.
      </p>
      <ul>
        <li>How do reward signals and feedback shape stable agent tendencies?</li>
        <li>How do value-related representations interact with task and knowledge structures?</li>
        <li>How can process-level monitoring detect drift in goal-directed behavior?</li>
      </ul>
    </div>
    <div class="research-detail-list__item">
      <h3>Action Structure</h3>
      <p>
        Tool use, external memory, multi-agent collaboration, embodiment, and environment feedback turn
        internal computation into action. I study how agent action is organized, monitored, corrected, and
        updated over time.
      </p>
      <ul>
        <li>How does model ability become sustained action in external environments?</li>
        <li>How do tool interfaces and memory systems reshape agent behavior?</li>
        <li>How can agents monitor, reflect, correct, and learn from execution failures?</li>
      </ul>
    </div>
  </div>
</section>

<section class="research-section" id="methodological-loop">
  <h2>Methodological Loop</h2>
  <p>
    Cognitive neuroscience contributes a research workflow for complex intelligent systems. I adapt this
    workflow to AI agents as a loop from task design to behavioral evidence, internal representation,
    mechanism intervention, and process-level control.
  </p>
  <div class="research-flow">
    <div class="research-flow__item">
      <strong>Task Paradigms</strong>
      <p>Design tasks that expose capability boundaries, strategy changes, and failure structures.</p>
    </div>
    <div class="research-flow__item">
      <strong>Behavior Boundaries</strong>
      <p>Measure when abilities remain stable, when they transfer, and when they collapse.</p>
    </div>
    <div class="research-flow__item">
      <strong>Representation Analysis</strong>
      <p>Locate functional parcels, pathway imbalance, temporal dynamics, and memory-factuality conflict.</p>
    </div>
    <div class="research-flow__item">
      <strong>Intervention Validation</strong>
      <p>Use ablation, steering, pathway scoring, reward shaping, and environment changes to test mechanisms.</p>
    </div>
    <div class="research-flow__item">
      <strong>Process Control</strong>
      <p>Turn diagnosis into monitoring, reflection, corrective action, process reward, and experience updating.</p>
    </div>
  </div>
  <div class="research-callout">
    <p>
      The working loop is: use tasks to define ability, behavior to characterize boundaries,
      representation analysis to locate structure, intervention to validate mechanism, and process
      monitoring to connect mechanism with reliable action.
    </p>
  </div>
</section>

<section class="research-section" id="papers">
  <h2>Current Thesis Program</h2>
  <p>
    My thesis work uses hallucination as an entry point into this program. Hallucination exposes how
    internal organization, module mechanisms, knowledge use, memory, reasoning, and long-horizon control can
    break down. The current papers form a three-level research path: explain the internal coordinate system,
    locate failures in core agent modules, and regulate long-horizon execution through metacognitive
    control.
  </p>
  <div class="research-flow">
    <div class="research-flow__item">
      <strong>Explain</strong>
      <p>NeuroCogMap builds an internal coordinate system for model cognition, capability hierarchy, and pathology localization.</p>
    </div>
    <div class="research-flow__item">
      <strong>Locate</strong>
      <p>ReDeEP, RHD, and FPPS locate failures in evidence use, temporal reasoning dynamics, and personalized-memory drift.</p>
    </div>
    <div class="research-flow__item">
      <strong>Regulate</strong>
      <p>ReARTeR and DS-MCM develop process reward, hierarchical monitoring, reflection, corrective action, and experience updating.</p>
    </div>
  </div>

  <div class="research-contribution-map">
    <article>
      <span>Research question</span>
      <strong>How do agent failures form before final output?</strong>
      <p>
        The program uses hallucination as a visible signal of internal organization, pathway imbalance,
        temporal reasoning dynamics, memory-factuality conflict, and process-control failure.
      </p>
    </article>
    <article>
      <span>Methodological contribution</span>
      <strong>From task behavior to representation, mechanism, and control</strong>
      <p>
        Each project defines a task that exposes a failure, measures behavior, locates internal structure,
        validates mechanisms, and uses diagnosis to design control.
      </p>
    </article>
    <article>
      <span>Empirical coverage</span>
      <strong>Evidence use, reasoning, personalization, process reward, and deep search</strong>
      <p>
        The current work spans several core agent modules and connects local mechanism diagnosis with
        long-horizon regulation.
      </p>
    </article>
    <article>
      <span>Field contribution</span>
      <strong>A bridge between mechanistic interpretability and trustworthy agents</strong>
      <p>
        The program provides an explanatory language for where failures form, how they propagate, and how
        control mechanisms can be designed.
      </p>
    </article>
  </div>

  <div class="research-paper-group" id="internal-organization">
    <p class="research-kicker">Explain: Internal Cognitive Organization</p>
    {% assign neurocogmap = site.data.research_projects | where: "id", "neurocogmap" | first %}
    <article class="research-publication">
      <a href="{{ neurocogmap.project_url }}">
        {% include optimized-image.html src=neurocogmap.teaser alt="NeuroCogMap teaser" loading="lazy" %}
      </a>
      <div>
        <h3><a href="{{ neurocogmap.project_url }}">{{ neurocogmap.title }}</a></h3>
        <p><strong>{{ neurocogmap.venue }}</strong> | {{ neurocogmap.role }}</p>
        <p>{{ neurocogmap.summary }}</p>
        <div class="research-link-row">
          <a href="{{ neurocogmap.project_url }}">official project page</a>
          {% if neurocogmap.code_url and neurocogmap.code_url != "" %}
            <a href="{{ neurocogmap.code_url }}">code</a>
          {% endif %}
        </div>
      </div>
    </article>
  </div>

  <div class="research-paper-group" id="module-mechanisms">
    <p class="research-kicker">Locate: Agent Module Mechanisms</p>
    {% for project in site.data.research_projects %}
      {% if project.id == "redeep" or project.id == "rhd" or project.id == "fpps" %}
      <article class="research-publication">
        <a href="{{ project.project_url }}">
          {% include optimized-image.html src=project.teaser alt=project.short_title loading="lazy" %}
        </a>
        <div>
          <h3><a href="{{ project.project_url }}">{{ project.title }}</a></h3>
          <p><strong>{{ project.venue }}</strong> | {{ project.role }}</p>
          <p>{{ project.summary }}</p>
          <div class="research-link-row">
            {% if project.paper_url and project.paper_url != "" %}
              <a href="{{ project.paper_url }}">paper</a>
            {% endif %}
            <a href="{{ project.project_url }}">project page</a>
          </div>
        </div>
      </article>
      {% endif %}
    {% endfor %}
  </div>

  <div class="research-paper-group" id="metacognitive-control">
    <p class="research-kicker">Regulate: Metacognitive Control</p>
    {% for project in site.data.research_projects %}
      {% if project.id == "rearter" or project.id == "mcm_ds" %}
      <article class="research-publication">
        <a href="{{ project.project_url }}">
          {% include optimized-image.html src=project.teaser alt=project.short_title loading="lazy" %}
        </a>
        <div>
          <h3><a href="{{ project.project_url }}">{{ project.title }}</a></h3>
          <p><strong>{{ project.venue }}</strong> | {{ project.role }}</p>
          <p>{{ project.summary }}</p>
          <div class="research-link-row">
            {% if project.paper_url and project.paper_url != "" %}
              <a href="{{ project.paper_url }}">paper</a>
            {% endif %}
            <a href="{{ project.project_url }}">project page</a>
          </div>
        </div>
      </article>
      {% endif %}
    {% endfor %}
  </div>
</section>

<section class="research-section" id="impact-horizon">
  <h2>Trajectory</h2>
  <p>
    The program develops from current hallucination mechanisms toward broader scientific tools for
    increasingly autonomous AI agents. The trajectory moves from systematic failure analysis, to internal
    knowledge translation, to the explanatory basis for long-term human-agent coexistence.
  </p>
  <div class="research-timeline">
    <article>
      <span>Short term</span>
      <h3>Understand Systematic Failures</h3>
      <p>
        Trace recurring failures from observable behavior back to internal organization, module mechanisms,
        and process-control breakdowns.
      </p>
    </article>
    <article>
      <span>Mid term</span>
      <h3>Locate and Translate Internal Knowledge</h3>
      <p>
        Study where complex knowledge is organized, how it is called and recombined, how reliable it is,
        and how it can become human-checkable evidence.
      </p>
    </article>
    <article>
      <span>Long term</span>
      <h3>Support Human-Agent Coexistence</h3>
      <p>
        Build tools for understanding and guiding agents that form goals, use tools, interact with social
        systems, and connect action with human values over time.
      </p>
    </article>
  </div>
</section>

<section class="research-section" id="future-plan">
  <h2>Future Plan: From Agent Science to AI4Science</h2>
  <p>
    The next stage develops this program in two connected directions. First, I will extend the current
    thesis from hallucination mechanisms to systematic accounts of intelligence, knowledge, value, and
    action structure. Second, I will use the same experimental loop to study scientific discovery agents.
    These agents search literature, operate analytical tools and simulators, reason across scales, generate
    hypotheses, and design experiments. The aim is to make their discovery trajectories inspectable,
    causally testable, and correctable.
  </p>
  <div class="research-roadmap">
    <article>
      <span>Year 1</span>
      <h3>Intelligence Structure</h3>
      <p>
        Map how reasoning, planning, memory, abstraction, and tool use form stable capabilities and failure
        patterns across tasks.
      </p>
    </article>
    <article>
      <span>Years 1-2</span>
      <h3>Knowledge Structure</h3>
      <p>
        Locate, test, and translate internal knowledge structures so humans can inspect knowledge that
        surface prompting only partially reveals.
      </p>
    </article>
    <article>
      <span>Years 2-3</span>
      <h3>Value and Action Structure</h3>
      <p>
        Study how goals, preferences, tool interfaces, social feedback, and environment interaction shape
        sustained action, then build monitoring and control mechanisms for reliable human-agent coexistence.
      </p>
    </article>
    <article>
      <span>AI4Science</span>
      <h3>Scientific Discovery Agents</h3>
      <p>
        Apply the framework to agents that integrate literature search, data analysis, simulation feedback,
        hypothesis generation, and experiment planning into inspectable discovery trajectories.
      </p>
    </article>
  </div>
  <div class="research-ai4science-path" aria-label="AI4Science research loop">
    <strong>AI4Science research loop</strong>
    <span>Scientific task paradigms</span>
    <span>Discovery behavior and failure boundaries</span>
    <span>Knowledge and reasoning representation analysis</span>
    <span>Mechanism intervention with tools or simulators</span>
    <span>Process monitoring and human-checkable discovery paths</span>
  </div>
</section>
