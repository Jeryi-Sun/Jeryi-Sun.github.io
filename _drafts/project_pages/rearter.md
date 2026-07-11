# ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding

## Research Question

How can retrieval-augmented reasoning be supervised as a process rather than judged only by the final answer? ReARTeR studies trustworthy process rewarding for multi-step retrieval-augmented reasoning. The central question is whether an agent can be trained and guided using feedback on intermediate retrieval, reasoning, and evidence-use steps, so that the final answer is supported by a reliable execution process rather than by accidental correctness.

## Motivation

Many retrieval-augmented systems are evaluated at the end of the pipeline: retrieve documents, generate reasoning, produce an answer, and then check whether the answer is correct. This is too coarse for agentic reasoning. A final answer can be correct for unsupported reasons, or wrong because a much earlier sub-query, retrieval decision, or reasoning step failed. Long-horizon agents need feedback inside the process. ReARTeR therefore treats retrieval-augmented reasoning as a sequence of actions that should be monitored, scored, and improved at the step level.

This process view is especially important when retrieval and reasoning are interleaved. A system may retrieve a useful document but use it at the wrong step, or it may decompose a question in a way that makes later evidence irrelevant. Final-answer supervision hides these distinctions. ReARTeR makes the intermediate path an object of supervision, which is closer to how a human researcher would audit a complex reasoning workflow.

## Approach

ReARTeR decomposes complex questions into intermediate retrieval and reasoning steps. It introduces process rewarding to evaluate step quality, evidence use, and reasoning consistency. The framework includes test-time scaling, where process reward signals guide search over reasoning paths, and post-training scaling, where step-level feedback supports warm-up and offline reinforcement learning. The important design choice is to align process evaluation with explanation: a process reward should not only score a step, but also indicate why the step is trustworthy or unreliable.

## Key Findings

The first finding is that trustworthiness must be evaluated inside the reasoning process. Final-answer supervision is not enough for complex retrieval-augmented tasks. The second finding is that process rewards connect explanation with optimization: step-level feedback can diagnose failures and also train better behavior. The third finding is that process rewarding provides a foundation for metacognitive control, because an agent cannot monitor and repair itself if intermediate failures remain invisible.

## Figure Guide

Problem: the RARTPR example shows a complex question that requires decomposition, retrieval, reasoning thought, and process feedback. The figure motivates why a single final-answer check cannot capture the reliability of the whole process.

Method: the test-time scaling figure shows how process-reward training data are collected and how process evaluators guide reasoning search. It also highlights bias-reduction and explanation alignment, which are essential for trustworthy process supervision.

Method: the post-training scaling figure shows how warm-up and step-level offline reinforcement learning improve retrieval-augmented reasoning. This is the bridge from process evaluation to model improvement.

## Research Impact

ReARTeR is the process-rewarding foundation of the metacognitive-control layer in the broader research program. ReDeEP and RHD diagnose particular failure mechanisms; ReARTeR asks how a system can receive reliable feedback during execution. This matters for search agents, research agents, legal reasoning systems, and any setting where intermediate evidence use must be trustworthy. The project makes process-level feedback a practical mechanism for controlling agent behavior.

In the larger Cognitive Neuroscience of AI Agents program, ReARTeR is the bridge from diagnosis to supervision. DS-MCM extends this direction into a self-monitoring loop, while ReARTeR supplies the process signal that such a loop can use. This makes the project a foundation for agents that evaluate the reliability of the steps that produced an answer.

## Resources and Citation

Paper: https://arxiv.org/abs/2501.07861

```bibtex
@inproceedings{sun2025rearter,
  title={ReARTeR: Retrieval-Augmented Reasoning with Trustworthy Process Rewarding},
  author={Sun, Zhongxiang and Wang, Qipeng and Yu, Weijie and Zang, Xiaoxue and Zheng, Kai and Xu, Jun and Zhang, Xiao and Song, Yang and Li, Han},
  booktitle={Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval},
  pages={1251--1261},
  year={2025}
}
```
