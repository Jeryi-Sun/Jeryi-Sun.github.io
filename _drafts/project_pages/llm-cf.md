# LLM-CF: Large Language Models Enhanced Collaborative Filtering

## Research Question

How can a conventional recommender use the world knowledge and reasoning of an LLM together with collaborative signals from other users' interactions? LLM-CF studies this transfer problem with an offline teacher and an online recommendation model. The teacher writes reasoning examples from historical interactions. A retrieval module selects relevant examples, and a small In-context Chain of Thought (ICT) module learns an additional collaborative-filtering feature for the current prediction.

## Motivation

User and item IDs summarize interaction patterns, while language models can interpret product attributes, preferences, and the relationship between a user's history and a candidate item. These sources of information complement one another. A description of one user and one item, however, exposes only a small part of the interaction data. The paper therefore uses retrieved historical interactions as the context in which language-derived information becomes useful to collaborative filtering.

Serving cost also shapes the design. Generating an explanation for every incoming request would place an LLM on the online prediction path. LLM-CF instead builds a reusable collection of reasoning examples offline. Online computation still includes feature encoding, retrieval, the ICT module, and the backbone recommender; the design removes online LLM text generation, not all additional computation.

## Approach

The offline teacher, RecGen-LLaMA, starts from LLaMA2-7B-chat. The paper compares recommendation-only fine-tuning with several alternatives and evaluates both recommendation AUC and MMLU accuracy. Mixing recommendation data with general instruction data from LIMA and alpaca-gpt4 offers a useful balance in these evaluations. This matters because the teacher must still produce informative reasoning after learning recommendation behavior.

RecGen-LLaMA generates a chain of thought for a sampled historical interaction. Its prompt asks for an interpretation of the user's history, the target item's characteristics, their compatibility, and possible interest in diversity. The historical interaction label is provided during this offline generation. Each stored example contains recommendation features, generated reasoning, and the historical label. The reported configuration uses a collection sampled from one tenth of the training data.

For a new query, textual user and item features are embedded and used to retrieve similar examples by cosine similarity. Retrieval excludes interactions from the query's future. The selected context also balances positive and negative historical labels. The current query label is not an input to the prediction process.

ICT turns each retrieved example into three embeddings: recommendation features, reasoning, and its label. These triples precede the current query's feature embedding in a short transformer-decoder sequence. The final query representation becomes the LLM-enhanced collaborative-filtering feature. In the reported setup, four examples yield thirteen sequence positions; the ICT decoder uses two layers and two attention heads.

Training combines the backbone's recommendation loss with a cosine reconstruction objective for the stored reasoning embeddings. The auxiliary task encourages the decoder's feature representations to retain information from the reasoning examples. Ranking models receive the learned feature through concatenation and feature interaction. Retrieval models add it to the user vector; the current target item's information is masked in that setting to avoid exposing the retrieval answer.

## Key Findings

The ranking study evaluates DeepFM, xDeepFM, AutoInt, DCNv1, DCNv2, and DIN on Amazon Sports & Outdoors, Beauty, and Toys & Games. It compares each backbone with no enhancement, knowledge distillation (KD), KAR, and LLM-CF. The comparison uses the same 7B LLaMA2 family and consistent backbone architectures. The dataset split is leave-one-out, and CTR evaluation uses one randomly sampled negative per positive interaction.

Table 3 supports two distinct conclusions. LLM-CF improves the unaugmented backbone's AUC in all eighteen backbone-dataset combinations. Against the other enhancement methods, it has the highest AUC in sixteen of eighteen combinations. KD is higher for DCNv2 on Beauty (0.8057 versus 0.8033) and Toys (0.7827 versus 0.7812). These exceptions belong in the project page because the benefit depends on the backbone.

DeepFM provides an interpretable example of the main improvement. AUC changes from 0.7990 to 0.8137 on Sports, from 0.7853 to 0.8044 on Beauty, and from 0.7681 to 0.7881 on Toys. The corresponding LogLoss values fall from 0.5471 to 0.5306, 0.5545 to 0.5366, and 0.5770 to 0.5581. The page reports direct AUC values rather than relabeling the paper's RelaImpr statistic as an ordinary percentage increase.

Table 4 tests candidate retrieval with SASREC, YoutubeDNN, GRU4REC, and SRGNN. LLM-CF increases HIT@10 in eleven of twelve backbone-dataset combinations. SASREC on Sports improves from 0.0203 to 0.0349. GRU4REC on Toys falls from 0.0411 to 0.0380, with NDCG@10 also falling from 0.0202 to 0.0192. Retrieval gains are broad, with a concrete negative-transfer case.

Table 5 separates reasoning content from other design choices. For DeepFM, removing CoT and its reconstruction loss lowers AUC on all three datasets. Replacing the decoder with mean pooling also lowers these AUC values. Other backbones have exceptions: the full model does not dominate every ablation metric. The page uses the DeepFM rows to explain the controlled comparison and does not generalize them into a universal claim.

## Figure Guide

- Figure 1, `graphs/introduction_graph.pdf`: follow the boundary between offline generation and online recommendation. Stored examples carry language-derived information into a conventional prediction pipeline.
- Figure 3, `graphs/model_graph.pdf`: read generation, top-K retrieval, and ICT as connected stages. The feature, reasoning, and label embeddings explain what enters the decoder; the query representation explains what reaches the backbone.
- Figure 4, `graphs/amazon_Beauty.pdf` and `graphs/amazon_Sports.pdf`: read recommendation AUC and MMLU accuracy jointly. The experiment studies a teacher's measured capability trade-off, rather than establishing preservation of every general ability.
- Figure 5, `graphs/ICL_n_transposed.pdf`: compare context sizes and label-balance settings within each backbone. Four examples are the selected practical configuration; six or eight can help individual cases but are not uniformly stronger.

## Research Impact

LLM-CF is an earlier knowledge-transfer project in my recommendation research. It connects LLM-generated reasoning with interaction-based decision models and makes the serving boundary explicit. It is relevant to my broader interest in how models store and use knowledge, while its experiments concern recommendation quality and transfer. They do not establish an internal cognitive map or a causal explanation of an LLM's reasoning process.

## Resources and Citation

Paper: https://arxiv.org/abs/2403.17688v2

Code: https://github.com/Jeryi-Sun/LLM-CF

```bibtex
@inproceedings{sun2024large,
  title={Large Language Models Enhanced Collaborative Filtering},
  author={Sun, Zhongxiang and Si, Zihua and Zang, Xiaoxue and Zheng, Kai and Song, Yang and Zhang, Xiao and Xu, Jun},
  booktitle={Proceedings of the 33rd ACM International Conference on Information and Knowledge Management},
  doi={10.1145/3627673.3679558},
  year={2024}
}
```
