---
layout: research
title: "AI 智能体的认知神经科学"
permalink: /zh/research/cognitive-neuroscience/
author_profile: false
lang: zh
lang_switch_url: /research/cognitive-neuroscience/
---

<section class="research-hero research-hero--program">
  <div class="research-hero__heading">
    <p class="research-kicker">研究计划</p>
    <h1>AI 智能体的认知神经科学</h1>
  </div>
  <div class="research-hero__text">
    <p class="research-lede">
      AI 智能体已经能够推理、调用记忆与工具、同人持续交互，并围绕长期目标采取行动。
      我的长期研究关注这些系统的智能、知识、价值和行动结构怎样形成、组织与变化，以及它们如何影响行为。
      现阶段，我从具体故障入手，分析异常怎样沿目标、证据、记忆、工具反馈和行动过程传播，
      再研究智能体能否在执行过程中发现问题并完成纠正。
    </p>
    <div class="research-link-row">
      <a class="research-button research-button--secondary" href="#papers">当前工作</a>
      <a class="research-button" href="#future-plan">未来方向：AI4Science</a>
    </div>
  </div>
  <figure class="research-hero__media research-program-overview">
    {% include optimized-image.html src="/images/research/cognitive-neuroscience-overview-zh.png" alt="从智能体长程状态偏移、故障传播和因果定位走向可信调控的研究路线" loading="eager" fetchpriority="high" %}
    <figcaption>
      从局部机理研究走向长程任务中的可信调控。
    </figcaption>
  </figure>
</section>

<nav class="research-anchor-nav" aria-label="本页目录">
  <span>本页内容</span>
  <a href="#why-this-program">为什么需要这项研究</a>
  <a href="#the-object">研究对象</a>
  <a href="#problem-groups">四类问题</a>
  <a href="#methodological-loop">研究方法</a>
  <a href="#papers">博士阶段工作</a>
  <a href="#future-plan">AI4Science</a>
</nav>

<section class="research-section" id="why-this-program">
  <h2>为什么需要这项研究</h2>
  <p>
    AI 智能体把推理、记忆、工具调用和持续行动组合在同一个系统中。
    这带来了一组具体问题：行为异常由哪些内部状态引起，局部故障怎样沿长程任务传播，系统又能否在执行中及时纠正。
    评测、可解释性和安全研究已经提供了行为测量、机制定位和风险约束方法。我希望把这些方法连起来，追踪智能体从内部组织到持续行动的完整过程。
  </p>
  <div class="research-detail-list">
    <div class="research-detail-list__item">
      <h3>新的研究对象</h3>
      <p>
        智能体把感知、语言、推理、记忆、工具调用、长期目标和多智能体协作组合在一起，
        也开始参与数据生成、评测设计、工具链优化和模型改进。
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>分散的既有解释</h3>
      <p>
        评测描绘行为边界，可解释性追踪内部机理，安全与对齐研究监督和约束。
        我的研究把这些线索放进同一套系统分析中，考察内部组织如何转化为持续行动。
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>反复出现的问题</h3>
      <p>
        推理失真、知识误用、目标漂移和行动失控看似发生在不同模块，背后都涉及能力、知识、
        偏好和行为策略如何形成、更新与失效。
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>需要组合的方法</h3>
      <p>
        认知任务设计、行为分析、表征分析、机理干预和过程监控共同构成实验闭环，
        用来回答“系统何时出错、错误在哪里形成、干预后是否真正改变行为”。
      </p>
    </div>
    <div class="research-detail-list__item">
      <h3>长期社会影响</h3>
      <p>
        当智能体逐渐走向自主化、社会化、具身化和自我改进，我们需要能够检查内部状态、
        引导行为并研究人机长期共存的科学工具。
      </p>
    </div>
  </div>
</section>

<section class="research-section" id="the-object">
  <h2>研究对象：作为复杂智能系统的 AI 智能体</h2>
  <p>
    早期人造智能系统通常有较清楚的任务、能力和行为边界。今天的 AI 智能体通过大规模训练、
    后训练、工具交互、记忆和环境反馈形成能力。它们可以跨任务迁移，拆解长期目标，调用外部工具，
    与其他智能体协作，并对现实环境产生连续影响。
  </p>
  <p>
    因此，我研究的是智能体本身的组织方式：人工系统怎样组织不同能力，怎样存储和调用知识，
    怎样形成目标与偏好，又怎样把模型内部的计算转化为持续行动。这个对象需要系统层面的解释，
    因为一次输出只是行为链条的末端。
  </p>
</section>

<section class="research-section" id="problem-groups">
  <h2>四类相互关联的问题</h2>
  <p>
    我把 AI 智能体的研究整理为智能结构、知识结构、价值结构和行动结构四组问题。
    每一组都对应可观察的行为、需要定位的内部机理，以及可以检验的干预方式。
  </p>
  <div class="research-detail-list">
    <div class="research-detail-list__item">
      <h3>智能结构</h3>
      <p>
        推理、规划、记忆、抽象、工具使用和长程任务组织能力，会在训练与交互中逐步形成。
        我关注这些能力怎样出现和泛化，又为什么会波动或突然失效。
      </p>
      <ul>
        <li>哪些内部结构支持推理、规划与工具使用？</li>
        <li>什么条件会让一种能力保持稳定、变得脆弱或产生误导？</li>
        <li>后训练与环境交互如何改变能力的调用方式？</li>
      </ul>
    </div>
    <div class="research-detail-list__item">
      <h3>知识结构</h3>
      <p>
        智能体内部可能已经形成自然语言提示难以完整调出的知识结构。我研究知识存在哪里、
        如何组织和调用，以及怎样把内部知识转译为人能够检查的证据。
      </p>
      <ul>
        <li>事实知识、程序知识和任务知识分别如何组织？</li>
        <li>外部证据、参数知识与个性化记忆怎样共同影响回答？</li>
        <li>如何检验内部知识的可靠性，并将其转化为可核查的表达？</li>
      </ul>
    </div>
    <div class="research-detail-list__item">
      <h3>价值结构</h3>
      <p>
        智能体的目标、偏好与行为倾向由训练目标、奖励模型、人类反馈、部署环境和社会交互共同塑造。
        我希望测量这类结构的变化，并研究可行的引导方式。
      </p>
      <ul>
        <li>奖励信号与反馈怎样塑造相对稳定的行为倾向？</li>
        <li>价值相关表征如何与任务结构和知识结构相互作用？</li>
        <li>过程监控能否及时发现目标导向行为的偏移？</li>
      </ul>
    </div>
    <div class="research-detail-list__item">
      <h3>行动结构</h3>
      <p>
        工具调用、外部记忆、多智能体协作、具身接口和环境反馈，把模型内部计算接入真实世界。
        我研究行动过程怎样组织，又怎样被监控、纠正和持续更新。
      </p>
      <ul>
        <li>模型能力如何变成外部环境中的连续行动？</li>
        <li>工具接口和记忆系统如何重塑智能体行为？</li>
        <li>智能体能否在执行中监控、反思、纠错并积累经验？</li>
      </ul>
    </div>
  </div>
</section>

<section class="research-section" id="methodological-loop">
  <h2>方法闭环</h2>
  <p>
    认知神经科学提供了一套研究复杂智能系统的实验思路：从行为出发设计任务，观察内部表征，
    再通过干预判断相关线索是否具有因果作用。我把这套思路用于 AI 智能体，形成下面的研究闭环。
  </p>
  <div class="research-flow">
    <div class="research-flow__item">
      <strong>任务范式</strong>
      <p>设计能够显露能力边界、策略变化和错误结构的任务。</p>
    </div>
    <div class="research-flow__item">
      <strong>行为边界</strong>
      <p>测量能力何时稳定、何时迁移，以及在什么条件下失效。</p>
    </div>
    <div class="research-flow__item">
      <strong>表征分析</strong>
      <p>定位功能分区、路径失衡、时间动态和记忆与事实之间的冲突。</p>
    </div>
    <div class="research-flow__item">
      <strong>干预验证</strong>
      <p>通过消融、表征引导、路径评分、奖励塑形和环境改变检验机理。</p>
    </div>
    <div class="research-flow__item">
      <strong>过程调控</strong>
      <p>把诊断结果用于过程监控、反思纠错、过程奖励和经验更新。</p>
    </div>
  </div>
  <div class="research-callout">
    <p>
      我的工作流程是：用任务定义能力，用行为刻画边界，用表征分析定位结构，
      用干预验证机理，再通过过程监控把机理分析接回可靠行动。
    </p>
  </div>
</section>

<section class="research-section" id="papers">
  <h2>博士阶段研究主线</h2>
  <p>
    我的博士研究从幻觉切入。幻觉是一种可见的故障信号，可以追溯到内部功能组织、模块间路径失衡、
    知识调用、记忆干扰、推理动态和长程过程控制。现有工作沿三层路径展开：先解释模型内部的认知坐标系，
    再定位智能体核心模块中的故障，最后用元认知机制调控长程执行。
  </p>
  <div class="research-flow">
    <div class="research-flow__item">
      <strong>解释</strong>
      <p>NeuroCogMap 构建模型认知、能力层级和异常定位的内部坐标系。</p>
    </div>
    <div class="research-flow__item">
      <strong>定位</strong>
      <p>ReDeEP、RHD 和 FPPS 分别定位证据使用、推理时间动态与个性化记忆中的故障。</p>
    </div>
    <div class="research-flow__item">
      <strong>调控</strong>
      <p>ReARTeR 和 DS-MCM 研究过程奖励、分层监控、反思纠错与经验更新。</p>
    </div>
  </div>

  <div class="research-contribution-map">
    <article>
      <span>研究问题</span>
      <strong>智能体故障如何在最终输出之前形成？</strong>
      <p>
        我把幻觉视为内部功能组织、模块路径、推理动态、记忆与事实冲突以及过程控制失效的外部信号。
      </p>
    </article>
    <article>
      <span>方法路线</span>
      <strong>从任务行为走向表征、机理与调控</strong>
      <p>
        每项工作都从一个能显露故障的任务开始，经由行为测量和内部定位检验机理，再据此设计调控方法。
      </p>
    </article>
    <article>
      <span>实证范围</span>
      <strong>证据使用、推理、个性化、过程奖励与深度搜索</strong>
      <p>
        这些工作覆盖多个智能体核心模块，并把局部机理诊断逐步接到长程执行调控上。
      </p>
    </article>
    <article>
      <span>研究定位</span>
      <strong>连接机理可解释性与可信智能体</strong>
      <p>
        这套研究尝试回答故障在哪里形成、怎样传播，以及调控机制应当介入哪个环节。
      </p>
    </article>
  </div>

  <div class="research-paper-group" id="internal-organization">
    <p class="research-kicker">解释：内部认知组织</p>
    {% assign neurocogmap = site.data.research_projects_zh | where: "id", "neurocogmap" | first %}
    <article class="research-publication">
      <a href="{{ neurocogmap.project_url }}">
        {% include optimized-image.html src=neurocogmap.teaser alt="NeuroCogMap 项目预览图" loading="lazy" %}
      </a>
      <div>
        <h3><a href="{{ neurocogmap.project_url }}">{{ neurocogmap.title }}</a></h3>
        <p><strong>{{ neurocogmap.venue }}</strong> | {{ neurocogmap.role }}</p>
        <p>{{ neurocogmap.summary }}</p>
        <div class="research-link-row">
          <a href="{{ neurocogmap.project_url }}">官方项目主页</a>
          {% if neurocogmap.code_url and neurocogmap.code_url != "" %}
            <a href="{{ neurocogmap.code_url }}">代码</a>
          {% endif %}
        </div>
      </div>
    </article>
  </div>

  <div class="research-paper-group" id="module-mechanisms">
    <p class="research-kicker">定位：智能体模块机理</p>
    {% for project in site.data.research_projects_zh %}
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
              <a href="{{ project.paper_url }}">论文</a>
            {% endif %}
            <a href="{{ project.project_url }}">项目主页</a>
          </div>
        </div>
      </article>
      {% endif %}
    {% endfor %}
  </div>

  <div class="research-paper-group" id="metacognitive-control">
    <p class="research-kicker">调控：元认知调控</p>
    {% for project in site.data.research_projects_zh %}
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
              <a href="{{ project.paper_url }}">论文</a>
            {% endif %}
            <a href="{{ project.project_url }}">项目主页</a>
          </div>
        </div>
      </article>
      {% endif %}
    {% endfor %}
  </div>
</section>

<section class="research-section" id="impact-horizon">
  <h2>研究进程</h2>
  <p>
    这项研究从当前的幻觉机理逐步扩展到更自主的 AI 智能体。近期分析系统性故障，
    中期研究内部知识的定位和转译，长期则为理解人类与智能体共同生活和工作提供可检验的依据。
  </p>
  <div class="research-timeline">
    <article>
      <span>近期</span>
      <h3>理解系统性故障</h3>
      <p>
        从可观察行为追溯反复出现的错误，定位内部组织、模块机理和过程控制中的具体问题。
      </p>
    </article>
    <article>
      <span>中期</span>
      <h3>定位并转译内部知识</h3>
      <p>
        研究复杂知识在哪里组织、如何调用与重组、是否可靠，以及怎样转化为人可以核查的证据。
      </p>
    </article>
    <article>
      <span>长期</span>
      <h3>支持人类与智能体共存</h3>
      <p>
        为能够形成目标、使用工具并进入社会系统的智能体建立分析与引导方法，使长期行动与人类价值保持联系。
      </p>
    </article>
  </div>
</section>

<section class="research-section" id="future-plan">
  <h2>下一步：从智能体科学走向 AI4Science</h2>
  <p>
    下一阶段有两条相互衔接的工作线。第一条把博士阶段的幻觉机理研究扩展到智能、知识、价值和行动结构；
    第二条把同一套实验闭环用于科学发现智能体。这类智能体需要检索文献，操作分析工具和模拟器，跨尺度推理，
    提出假设并设计实验。我希望把它们的发现过程变成可以检查、可以做因果检验，也可以在出错后纠正的研究对象。
  </p>
  <div class="research-roadmap">
    <article>
      <span>第 1 年</span>
      <h3>智能结构</h3>
      <p>
        描绘推理、规划、记忆、抽象和工具使用如何形成稳定能力，并比较这些能力在不同任务中的失效模式。
      </p>
    </article>
    <article>
      <span>第 1–2 年</span>
      <h3>知识结构</h3>
      <p>
        定位、检验并转译内部知识，让人能够检查仅靠表层提示无法完整调出的知识结构。
      </p>
    </article>
    <article>
      <span>第 2–3 年</span>
      <h3>价值与行动结构</h3>
      <p>
        研究目标、偏好、工具接口、社会反馈和环境交互如何塑造持续行动，并设计相应的监控与调控方法。
      </p>
    </article>
    <article>
      <span>AI4Science</span>
      <h3>科学发现智能体</h3>
      <p>
        构建科学发现智能体，将文献检索、数据分析、模拟反馈、假设生成和实验规划组织成可检查的发现过程。
      </p>
    </article>
  </div>
  <div class="research-ai4science-path" aria-label="AI4Science 研究闭环">
    <strong>AI4Science 研究闭环</strong>
    <span>科学任务范式</span>
    <span>发现行为与失效边界</span>
    <span>知识和推理表征分析</span>
    <span>结合工具或模拟器的机理干预</span>
    <span>过程监控与人可核查的发现路径</span>
  </div>
</section>
