# NeuroCogMap: A Cognitive Map of Internal Organization in Large Language Models

## Research Question

Can large language models be studied as artificial cognitive systems with an internal organization that is more structured than isolated neurons or final outputs? NeuroCogMap asks whether model internals can be organized into an interpretable middle scale: functional parcels, cognitive maps, cognitive capabilities, capability hierarchies, and pathology-localization patterns. The goal is not to claim that language models are biological brains. The goal is to borrow a useful research strategy from cognitive neuroscience: define tasks, observe behavior, analyze internal representations, and build a map that can explain both normal capability and abnormal behavior.

## Motivation

Most evaluation frameworks tell us what a model can do, but they do not explain where a capability lives internally or why the same model fails under slightly different conditions. Classical mechanistic interpretability can identify local features, circuits, or heads, but these units can be too fine-grained to support a program-level account of cognition, hallucination, and intervention. NeuroCogMap fills this gap by asking for a larger explanatory coordinate system. If hallucination is only treated as a wrong final answer, then the analysis starts too late. A model may enter an abnormal internal state before the final response is emitted. NeuroCogMap therefore treats hallucination and related failures as representational pathologies: abnormal activation, misrouted capability use, or disrupted organization inside the model.

## Approach

The project builds a multi-level map from model behavior and internal activations. It starts from cognitive tasks and capability spaces, extracts sparse model features, groups them into functional parcels, and connects those parcels to capability-level maps. The framework then studies how these parcels activate, interact, and organize into broader capability hierarchies. This produces an intermediate representation between raw neurons and benchmark scores. The same map can be used to compare normal and pathological behavior, making it possible to ask whether hallucination, bias, jailbreak, and sycophancy occupy different internal regions or disrupt different capability systems.

## Key Findings

NeuroCogMap provides the explanatory layer for the broader thesis. It shows how hallucination can be studied as an internal organization problem, links normal capability and abnormal behavior in the same representational space, and gives later project pages a shared vocabulary. ReDeEP analyzes evidence-use pathways, RHD analyzes temporal reasoning dynamics, FPPS analyzes personalized-memory drift, ReARTeR analyzes process reward, and DS-MCM analyzes metacognitive monitoring. NeuroCogMap is the coordinate system that lets these module studies be read as one research program.

## Figure Guide

Problem and framework: the first figure explains why a neuroscience-inspired framework is useful for LLM analysis. It connects human cognitive alignment, model neural-level activation, and capability collection, but should be read as a methodological analogy rather than a biological equivalence claim.

Mechanism and structure: the second figure shows how sparse internal signals are organized into functional parcels, cognitive maps, cognitive capabilities, and hierarchy. This is the core contribution: turning unstructured activations into an interpretable system-level map.

Result and pathology localization: the third figure connects the map to abnormal behavior. The important point is that hallucination and other model pathologies can be localized and compared within the same internal organization, which creates a bridge from explanation to intervention.

## Research Impact

NeuroCogMap anchors the Cognitive Neuroscience of AI Agents program. It makes model cognition observable at a level that is useful for faculty readers, mechanism researchers, and agent-safety researchers. Its impact is not a single detector or benchmark improvement; it is an organizing framework for explaining why large-model agents succeed, fail, and become controllable. In the long run, this kind of map can support more systematic diagnosis of internal knowledge, value, and action structures in increasingly autonomous agents.

## Resources and Citation

Project website: https://neurocogmap.site/

Code: https://github.com/Jeryi-Sun/NeuroCogMap
