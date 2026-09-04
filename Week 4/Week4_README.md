# Week 4 – Implementation Strategy and Code Architecture

## Project
**AgriGuard AI – Smart Crop Disease and Risk Prediction System**

## Week 4 Task
**Implementation Strategy and Code Architecture Outline**

This folder contains the Week 4 implementation documentation for AgriGuard AI. The objective is to convert the machine-learning model design developed in earlier weeks into a practical, modular and maintainable Python implementation strategy.

## Contents

- `AgriGuard_AI_Week4_Implementation_Strategy.docx` – Complete Week 4 implementation report.
- The DOCX contains the proposed system architecture and end-to-end workflow diagrams.

## Report Coverage

The Week 4 report includes:

1. Step-by-step implementation strategy
2. Concrete dataset evidence and implementation assumptions
3. Hypothesis formulation (H0 and H1)
4. High-level system architecture
5. End-to-end machine-learning workflow
6. Proposed Python project structure
7. Module and function responsibilities
8. Pseudocode for data ingestion, preprocessing, model training, evaluation, disease prediction and risk calculation
9. Accuracy, Precision, Recall, F1-score and confusion matrix
10. Code maintainability, modularity, Git/GitHub and testing practices
11. Generic 7-day implementation timeline
12. Coding and integration risk assessment with mitigation strategies
13. Expected outcome and conclusion
14. References and citations

## Dataset Reference

The implementation plan uses the PlantVillage dataset as a reference benchmark. TensorFlow Datasets documents **54,303 images across 38 categories**.

Proposed experimental split:

- **70% Training:** approximately 38,012 images
- **15% Validation:** approximately 8,145 images
- **15% Testing:** approximately 8,146 images

These figures are an implementation plan, not claimed model results.

## Hypothesis

### H1 – Alternative Hypothesis
A consistent preprocessing pipeline combined with realistic training-data augmentation will improve the generalization performance of the AgriGuard AI disease classifier compared with a baseline without augmentation.

### H0 – Null Hypothesis
Adding preprocessing and augmentation will not produce a meaningful improvement in validation/test performance.

The report proposes a **macro F1-score ≥ 0.90** as an engineering target. This is a target for future experimentation and is not an achieved result.

## Evaluation

The model will be evaluated using overall and class-wise performance. Special attention will be given to macro F1, recall and the confusion matrix so that weak disease classes are not hidden by overall accuracy.

## Risk Management

Key risks covered include:

- Corrupt or incorrectly labelled images
- Class imbalance
- Data leakage
- Overfitting
- Poor generalization to field images
- Dependency/version conflicts
- Limited computing resources
- Training/inference preprocessing mismatch
- Incorrect interpretation of risk scores
- Integration/API errors
- Reproducibility problems

Each risk has a corresponding mitigation strategy in the report.

## Important Note

PlantVillage is primarily a benchmark/reference dataset. Strong performance on this dataset should not automatically be treated as proof of real-world field performance. Future validation with diverse field images and expert-labelled data is recommended before practical deployment.

## References

1. TensorFlow Datasets – PlantVillage: https://www.tensorflow.org/datasets/catalog/plant_village
2. Scikit-learn – Model Evaluation and Scoring: https://scikit-learn.org/stable/modules/model_evaluation.html
3. Ferentinos, K. P. (2018). *Deep learning models for plant disease detection and diagnosis*. Computers and Electronics in Agriculture, 145, 311–318. https://doi.org/10.1016/j.compag.2018.01.009
4. Sladojevic, S. et al. (2016). *Deep Neural Networks Based Recognition of Plant Diseases by Leaf Image Classification*. Computational Intelligence and Neuroscience. https://doi.org/10.1155/2016/3289801
