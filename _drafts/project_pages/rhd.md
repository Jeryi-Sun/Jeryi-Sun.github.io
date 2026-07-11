# Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models

## Research Question

When a large reasoning model produces a wrong answer, where does the hallucination actually form? RHD asks whether reasoning hallucination should be treated as a final-answer error or as a temporal process that develops across intermediate reasoning steps. The project studies the internal and behavioral dynamics of reasoning trajectories, aiming to identify when a model begins to follow an unreliable path and how process-level constraints can reduce that failure.

## Motivation

Large reasoning models expose longer chains of thought and intermediate computations than standard single-turn language models. This creates an opportunity and a risk. The opportunity is that hallucination can be studied before the final answer appears. The risk is that a model may produce a fluent, self-consistent reasoning trace that still contains shallow pattern matching, early fluctuation, erroneous backtracking, overthinking, or pseudo-verification. Answer-only evaluation cannot distinguish a robust reasoning process from a lucky final answer. RHD therefore treats reasoning hallucination as a temporal neural-dynamics problem.

For a researcher reader, the main shift is methodological. The paper does not ask only whether reasoning models are correct; it asks how the reasoning state changes as the model moves through a trajectory. This makes the work closer to a process-level cognitive experiment than to a conventional benchmark. A hallucinated answer becomes the endpoint of a measurable sequence, not a single opaque failure event.

## Approach

The method tracks reasoning trajectories and constructs trajectory-level probes. It defines Reasoning Score, CV Score, and Attention Score to measure how reasoning depth and attention evolve across steps. These scores allow the paper to compare truthful and hallucinated trajectories, identify misled steps, and characterize the dynamics that precede unreliable answers. The mitigation component, GRPO-R, uses the diagnosis to motivate process-level reward constraints. Rather than waiting for final-answer correction, the method discourages unreliable intermediate states and promotes more faithful reasoning paths.

## Key Findings

The first finding is that reasoning hallucination often forms before the final response. A trajectory can become unstable, follow a false clue, or perform misleading verification long before the answer is emitted. The second finding is that temporal signals reveal failures hidden by answer-only evaluation. Early fluctuation, shallow matching, and pseudo-verification provide a mechanism vocabulary for explaining unreliable reasoning. The third finding is that process reward can target the path itself. By constraining the reasoning process, GRPO-R connects detection with mitigation.

## Figure Guide

Method: the trajectory-scoring figure defines the central measurements. Reasoning Score, CV Score, and Attention Score quantify different aspects of intermediate reasoning behavior, making the trajectory measurable instead of anecdotal.

Problem: the GSM-NoOp trajectory case compares truthful and hallucinated reasoning traces. The key point is that the two traces can differ in step-level dynamics even when the prompt format is similar.

Result: the pattern-validation figure checks whether the proposed scores distinguish misled and non-misled steps. It supports the claim that the method captures real reasoning-state differences.

Result: the consistency and perplexity analysis connects reasoning dynamics with accuracy and uncertainty. This figure makes the behavioral failure more concrete by linking trajectory structure with model-level reliability.

## Research Impact

RHD is the reasoning-planning module in the Cognitive Neuroscience of AI Agents program. It extends hallucination analysis from a single output to a temporal process, which is essential for agent systems that plan, search, and revise over many steps. For researcher readers, the value of RHD is not only that it detects bad answers; it provides a way to ask when reasoning goes wrong, what internal signals accompany that failure, and how a process-level objective can intervene before the final response.

This is also why RHD connects naturally to ReARTeR and DS-MCM. ReARTeR asks how intermediate steps can be rewarded, while DS-MCM asks how long-horizon agents can monitor and correct themselves. RHD supplies the diagnostic layer for reasoning itself: the trajectory must first become observable before it can be rewarded, monitored, or regulated.

## Resources and Citation

Paper: https://arxiv.org/abs/2505.12886

```bibtex
@inproceedings{sun2026mechanistic,
  title={Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models},
  author={Sun, Zhongxiang and Wang, Qipeng and Wang, Haoyu and Zhang, Xiao and Xu, Jun},
  booktitle={The Fourteenth International Conference on Learning Representations},
  year={2026}
}
```
