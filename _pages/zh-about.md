---
layout: research
permalink: /zh/
title: "孙忠祥 (Zhongxiang Sun)"
excerpt: "个人主页"
author_profile: false
lang: zh
lang_switch_url: /
---

<section class="research-profile">
  <div>
    <p class="research-kicker">大模型智能体 | 幻觉 | 机理可解释性 | 搜索</p>
    <h1>孙忠祥 (Zhongxiang Sun)</h1>
    <p>
      我是中国人民大学高瓴人工智能学院博士生，导师是许俊教授。我的研究围绕可信大语言模型与智能体展开，
      目前主要关注幻觉机理、推理与规划、信息检索、可解释性和法律智能。我借鉴认知神经科学的研究方法，
      通过任务设计、行为分析、表征分析、机制干预和过程监控，理解大模型智能体如何工作，又会在什么情况下出错。
    </p>
    <p>
      我预计于 2027 年 6 月毕业，目前正在寻找研究岗位。欢迎与我讨论可信大模型与智能体、
      大模型与信息检索的结合、机理可解释性，以及认知神经科学对人工智能研究的启发。
    </p>
    <div class="research-link-row">
      <a class="research-button" href="mailto:sunzhongxiang@ruc.edu.cn">邮箱</a>
      <a class="research-button research-button--secondary" href="https://scholar.google.com/citations?user=4n5whr0AAAAJ">Google Scholar</a>
      <a class="research-button research-button--secondary" href="https://github.com/Jeryi-Sun">GitHub</a>
    </div>
  </div>
  {% include optimized-image.html src="/images/profile.png" alt="孙忠祥" loading="eager" fetchpriority="high" %}
</section>

<section class="research-section research-impact">
  <h2>研究概览</h2>
  <div class="research-evidence-list">
    <article>
      <span>研究主线</span>
      <strong>可信大模型智能体的系统研究</strong>
      <p>
        我的博士研究从内部认知组织、模块级幻觉机理和长程元认知调控三个层面分析大模型智能体。
      </p>
    </article>
    <article>
      <span>代表成果</span>
      <strong>以第一作者在 ICLR、SIGIR 和 ACL 发表多项工作</strong>
      <p>
        相关项目涉及检索增强生成、大型推理模型、个性化大模型、过程奖励和深度搜索智能体。
      </p>
    </article>
    <article>
      <span>学术认可</span>
      <strong>ICLR Spotlight、SIGIR-AP 最佳论文奖及 Paper Digest 最具影响力论文榜单</strong>
      <p>
        ReDeEP 入选 ICLR Spotlight；生成式检索工作获 SIGIR-AP 最佳论文奖；另有论文入选 Paper Digest 的 SIGIR 与 CIKM 最具影响力论文榜单。
      </p>
    </article>
    <article>
      <span>公开资料</span>
      <strong>项目主页、代码与完整论文列表</strong>
      <p>
        网站整理了 NeuroCogMap 等项目的介绍、论文和代码，并单列完整发表记录，方便集中查阅。
      </p>
    </article>
  </div>
</section>

<section class="research-section">
  <h2>研究</h2>
  <p class="research-section-intro">
    我把大模型智能体视为一种新的人工智能系统。它能理解上下文，围绕目标展开推理，调用工具和记忆，
    与人或其他智能体协作，并在变化的环境中行动。我的工作关心这些能力在模型内部如何组织、故障如何产生，
    以及怎样在执行过程中及时发现并纠正问题。具体方法包括认知任务范式、行为边界测试、表征分析、因果干预和过程级监控。
  </p>
  <div class="research-program-path">
    <article>
      <span class="research-tag">解释</span>
      <div>
        <h3>内部认知组织</h3>
        <p>
          NeuroCogMap 将稀疏特征、功能脑区式分区、能力层级和异常行为定位组织在同一张内部认知图谱中。
        </p>
      </div>
      <a href="/zh/research/cognitive-neuroscience/#internal-organization">了解内部认知组织</a>
    </article>
    <article>
      <span class="research-tag">定位</span>
      <div>
        <h3>智能体模块机理</h3>
        <p>
          ReDeEP、RHD 和 FPPS 分别研究工具证据的使用、推理过程的时间动态，以及个性化记忆引发的事实偏移。
        </p>
      </div>
      <a href="/zh/research/cognitive-neuroscience/#module-mechanisms">查看模块机理研究</a>
    </article>
    <article>
      <span class="research-tag">调控</span>
      <div>
        <h3>元认知调控</h3>
        <p>
          ReARTeR 和 DS-MCM 研究过程奖励、分层监控、反思纠错与经验更新，让智能体在长程任务中及时调整行为。
        </p>
      </div>
      <a href="/zh/research/cognitive-neuroscience/#metacognitive-control">查看元认知调控研究</a>
    </article>
  </div>
</section>

<section class="research-section">
  <div class="research-section-heading">
    <div>
      <h2>代表论文</h2>
      <p>
        这里选取与当前研究主线关系最紧密的工作。其他论文收录在完整列表中。
      </p>
    </div>
    <a class="research-button research-button--secondary" href="/zh/publications/">查看完整论文列表</a>
  </div>
  {% assign homepage_projects = site.data.research_projects_zh | where: "show_on_homepage", true | sort: "homepage_priority" %}
  {% for project in homepage_projects %}
  <article class="research-publication">
    <a href="{{ project.project_url }}">
      {% include optimized-image.html src=project.teaser alt=project.short_title loading="lazy" %}
    </a>
    <div>
      <h3><a href="{{ project.project_url }}">{{ project.title }}</a></h3>
      <p><strong>{{ project.venue }}</strong> | {{ project.role }} | {{ project.layer }}</p>
      <p>{{ project.one_liner }}</p>
      <div class="research-link-row">
        {% if project.paper_url and project.paper_url != "" %}
          <a href="{{ project.paper_url }}">论文</a>
        {% endif %}
        <a href="{{ project.project_url }}">项目主页</a>
        {% if project.code_url and project.code_url != "" %}
          <a href="{{ project.code_url }}">代码</a>
        {% endif %}
      </div>
    </div>
  </article>
  {% endfor %}
</section>

<section class="research-section">
  <h2>教育经历</h2>
  <ul>
    <li><strong>2022.08 至今</strong> 中国人民大学高瓴人工智能学院，博士研究生。</li>
    <li><strong>2018.08–2022.06</strong> 北京交通大学计算机科学与技术专业，本科，专业排名第 1（前 0.4%）。</li>
  </ul>
</section>

<section class="research-section">
  <h2>奖励与荣誉</h2>
  <ul>
    <li>2024 年国家奖学金，并入选全国 100 名研究生国家奖学金获奖学生代表。<a href="https://www.peopleapp.com/column/30048976446-500006240986">报道</a></li>
    <li>2024 年中国科协青年人才托举工程博士生专项计划。</li>
    <li>中国人民大学创新人才项目。</li>
    <li>SIGIR-AP 2024 最佳论文奖。</li>
    <li>首届全国大学生人工智能与智慧治理创新创业竞赛一等奖。</li>
  </ul>
</section>

<section class="research-section">
  <h2>教学经历</h2>
  <ul>
    <li>中国人民大学《大数据分析导论》课程助教，2022 年秋季、2023 年秋季。</li>
    <li>中国人民大学《Python》课程助教，2023 年春季。</li>
  </ul>
</section>

<section class="research-section">
  <h2>学术与研究经历</h2>
  <ul>
    <li><strong>南洋理工大学</strong>，访问学生，2025.09–2026.03，合作导师：刘杨教授。</li>
    <li><strong>快手</strong>，研究实习生，2022.02–2025.06，合作导师：臧小雪、郑凯、宋阳。</li>
    <li><a href="http://cail.cipsc.org.cn/index.html"><strong>CAIL 2022</strong></a>，组委会成员。</li>
    <li><strong>WWW 2024、2025</strong>，审稿人。</li>
    <li><strong>SIGIR 2024、2025</strong>，程序委员会委员。</li>
    <li><strong>TOIS</strong>，审稿人。</li>
    <li><strong>TASLP</strong>，审稿人。</li>
    <li><strong>CIKM 2023、2024</strong>，程序委员会委员。</li>
    <li><strong>NeurIPS 2025</strong>，审稿人。</li>
    <li><strong>ICLR 2026</strong>，审稿人。</li>
  </ul>
</section>

<section class="research-section">
  <h2>报告</h2>
  <ul>
    <li>中国人民大学首届“创新前沿·博士生国际学术研讨会”：精准且可解释的法律案例匹配。<a href="https://drive.google.com/file/d/1TxD8YiEUV4R7nvxL46bRJ_YGata4P8QZ/view?usp=sharing">幻灯片</a></li>
    <li>受邀参加中关村科学城“日新青年说”论坛。<a href="https://mp.weixin.qq.com/s/_31wIQDcXwO5QquX6EUAMw">报道</a></li>
  </ul>
</section>
