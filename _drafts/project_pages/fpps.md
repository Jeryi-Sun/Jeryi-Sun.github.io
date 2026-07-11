# When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs

## Research Question

How can a personalized language model remain useful for user-specific tasks without letting user history distort objective facts? FPPS studies personalization-induced hallucination as a representation-level conflict between long-term user memory and factual knowledge. The paper asks when personalization becomes beneficial, when it becomes factually harmful, where that failure appears inside the model, and whether the representation can be steered without removing personalization altogether.

## Motivation

Personalization is usually presented as a desirable capability. A model that remembers user history can answer user-specific questions, adapt to preferences, and maintain continuity across interactions. But the same memory can become dangerous when the user history conflicts with verifiable facts. A model may overfit to a user's belief, preference, or local context and then provide a factually wrong answer. This is different from retrieval hallucination or single-chain reasoning hallucination because the risk accumulates over a longer timescale. FPPS therefore studies personalization as a memory-modulation problem: user history changes the model's internal state, and that state can bend factual behavior.

## Approach

FPPS first separates personalized-beneficial cases from factual-degraded cases. This distinction matters because the goal is not to suppress personalization everywhere. The method then studies hidden-state geometry, asking whether personalization directions and factual directions become entangled. Based on this diagnosis, FPPS introduces fact-preserving personalized steering. It selects personalization-sensitive layers, trains a probe to detect whether a personalized state is likely to be factually degraded, and applies adaptive steering at inference time. FPPS-H suppresses harmful personalization when the risk is high, while FPPS-S mixes in a fact-oriented correction when the risk is weaker.

## Key Findings

The first finding is that personalization can improve user fit while increasing factual risk. The second finding is that this risk can be described as representation entanglement: personalization and factuality are not always separable in hidden states. The third finding is that targeted inference-time steering can preserve both goals. FPPS does not treat user memory as a problem to remove; it treats it as a useful signal that must be monitored and controlled when it begins to distort facts.

## Figure Guide

Problem: the personalization-induced hallucination figure motivates the central tradeoff. It shows that a personalized model can answer user-specific questions better while also introducing factual hallucination when user history conflicts with objective facts.

Mechanism: the representation-entanglement figure explains the latent-state interpretation. Personalization directions can become non-orthogonal to factual representations, pulling the model toward user-aligned but unreliable answers.

Method: the FPPS framework figure shows layer selection, probing, and adaptive steering. It is the core method figure: select the sensitive layer, detect factual degradation, then decide whether to suppress personalization or add a fact-preserving correction.

Result: the history-length figure tests whether factual reliability degrades as user history becomes longer. It shows why personalization should be treated as a long-timescale memory risk.

Result: the controlled simulation figure isolates the effect of personalized teaching signals and checks whether FPPS-M can mitigate factual degradation in a controlled setting.

## Research Impact

FPPS is the personalized-memory module in the Cognitive Neuroscience of AI Agents program. It studies a failure mode that is not caused by one retrieved document or one reasoning step, but by accumulated user history. This matters for long-term assistants, recommender agents, legal agents, and research agents that maintain memory across sessions. The broader contribution is a control principle: personalization should be monitored at the representation level and steered only when it threatens factual reliability.

## Resources and Citation

Paper: https://arxiv.org/abs/2601.11000

```bibtex
@article{sun2026personalization,
  title={When Personalization Misleads: Understanding and Mitigating Hallucinations in Personalized LLMs},
  author={Sun, Zhongxiang and Zhan, Yi and Shen, Chenglei and Yu, Weijie and Zhang, Xiao and He, Ming and Xu, Jun},
  journal={arXiv preprint arXiv:2601.11000},
  year={2026}
}
```
