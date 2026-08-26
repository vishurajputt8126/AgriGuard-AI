# AgriGuard AI — Week 2: Algorithm Exploration and Preliminary Model Design

## Project focus
AgriGuard AI is a proposed machine-learning solution for estimating crop disease risk from field and weather observations. Week 2 focuses on comparing candidate algorithms and designing a practical baseline model.

## Candidate algorithms
1. Logistic Regression — simple, interpretable baseline for binary risk prediction.
2. Decision Tree — easy to explain and useful for non-linear decision rules.
3. Random Forest — combines multiple trees and is more robust to noisy features.
4. Gradient Boosting — sequentially improves weak learners and can model complex relationships.

## Proposed baseline
The initial design uses Random Forest as the primary baseline because it can handle mixed agricultural features, capture non-linear interactions, and provide feature-importance information. Logistic Regression is retained as an interpretable comparison model.

## Example input features
- temperature_c
- humidity_percent
- rainfall_mm
- leaf_wetness_hours
- crop_age_days
- previous_disease_cases

## Output
The model produces a disease-risk class such as Low, Medium, or High. In a real implementation, thresholds would be selected using validation data rather than assumed values.

## Evaluation
Performance will be evaluated using precision, recall, macro F1-score, confusion matrix, and cross-validation. Recall is particularly important for high-risk cases because missing a genuine disease-risk situation can be costly.

## Model flow
Input data -> validation/cleaning -> feature preparation -> train/validation split -> baseline model -> prediction -> evaluation -> risk class.

## Important note
This repository contains a preliminary design for the internship task. No claimed field accuracy is presented until the model is trained and evaluated on a documented dataset.
