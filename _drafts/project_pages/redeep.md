# ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability

## Research Question

Why do retrieval-augmented generation systems still hallucinate when relevant external evidence is available? ReDeEP studies this question mechanistically. It asks whether RAG hallucination is simply a retrieval failure, or whether the model may receive correct evidence while internally relying on parametric knowledge instead. The project frames RAG hallucination as an imbalance between two information sources: the external-context pathway that uses retrieved documents, and the parametric-knowledge pathway that uses stored model knowledge.

## Motivation

Retrieval is often treated as a straightforward solution to hallucination: if the model has access to documents, it should be grounded. In practice, retrieval does not guarantee evidence use. A model may ignore the retrieved document, selectively copy irrelevant content, or override the external evidence with its internal prior. Output-only detectors miss this distinction because they judge the final answer after the model has already resolved the conflict. ReDeEP moves the analysis earlier, into the model's internal computation, where evidence use and knowledge reliance can be separated. This is important for agent research because tool use is one of the first places where an agent must integrate external information with internal knowledge.

## Approach

ReDeEP decomposes RAG generation into evidence-sensitive computation and parametric-knowledge reliance. It analyzes how attention heads, copy behavior, feed-forward pathways, and residual-stream signals contribute to the final response. The method defines signals such as External Context Score and Parametric Knowledge Score to estimate whether generation is being driven by retrieved evidence or by internal knowledge. Instead of training a black-box detector on final outputs, ReDeEP uses this pathway imbalance as a mechanism-level hallucination signal. The same signal can also guide regulation, pushing generation toward evidence-grounded computation when the model's internal state indicates risk.

## Key Findings

The first finding is that evidence availability is not the same as evidence use. A retrieved document can contain the correct answer, yet the model may still produce a response dominated by parametric knowledge. The second finding is that hallucinated generations have internal pathway signatures: they differ in how external context and parametric knowledge are represented and combined. The third finding is that mechanistic signals can support targeted mitigation. By identifying when the model underuses evidence, ReDeEP connects interpretability with intervention rather than stopping at post-hoc explanation.

## Figure Guide

Problem: the RAG conflict figure shows cases where the retrieved document and the model's internal prior disagree. This figure motivates why retrieval alone is insufficient. The key reading point is that the model's failure can occur after successful retrieval.

Mechanism: the causal framing figure separates external-context use from parametric-knowledge use. It clarifies the paper's central hypothesis: hallucination arises from an imbalance between these pathways, not only from missing or noisy documents.

Method: the score-computation figure explains how ReDeEP estimates evidence use and knowledge reliance. It gives the operational bridge from mechanistic interpretation to detection.

Result: the mechanism-evidence figure shows that hallucinated and faithful generations differ in layer-head patterns and score behavior. This is the empirical support for treating RAG hallucination as an internal pathway problem.

## Research Impact

ReDeEP is the tool-evidence module in the Cognitive Neuroscience of AI Agents program. It studies a single-step functional circuit: how an agent sees external evidence, when it fails to use that evidence, and how the failure can be corrected. This matters beyond RAG because agent systems increasingly rely on search, tools, databases, and APIs. A trustworthy agent must not only retrieve information; it must internally use the evidence in a way that can be diagnosed and controlled.

## Resources and Citation

Paper: https://arxiv.org/abs/2410.11414

```bibtex
@inproceedings{sun2025redeep,
  title={{ReDeEP}: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability},
  author={Sun, Zhongxiang and Zang, Xiaoxue and Zheng, Kai and Xu, Jun and Zhang, Xiao and Yu, Weijie and Song, Yang and Li, Han},
  booktitle={International Conference on Learning Representations},
  year={2025}
}
```
