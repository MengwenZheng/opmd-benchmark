# Evaluation Protocol

This document defines the fixed evaluation protocol for the OPMD benchmark.
All reported results must follow this protocol exactly.

The protocol is defined prior to data release and model evaluation to ensure
fair comparison and to prevent metric or split selection bias.

---

## Tasks

The benchmark evaluates the following prediction tasks:

- Binary risk stratification:
  - Low-risk vs high-risk OPMD at slide level

Future tasks (e.g. multi-class grading or survival prediction) are out of scope
for the current protocol and will require a protocol update.

---

## Data Splits

All evaluations must use **patient-level splits** to prevent data leakage.

Two evaluation settings are defined:

### 1. Five-fold cross-validation (CV5)

- Stratified at the patient level
- Five non-overlapping folds
- Each patient appears in exactly one fold
- Performance is averaged across the five folds

### 2. Leave-One-Site-Out (LOSO) evaluation

- Each fold holds out all patients from one clinical site
- Training is performed on remaining sites
- Testing is performed only on the held-out site
- Intended to assess cross-site generalization

---

## Metrics

The primary evaluation metric is:

- Area Under the ROC Curve (AUROC)

Secondary metrics include:

- Area Under the Precision–Recall Curve (AUPRC)
- Sensitivity at fixed specificity (when applicable)

Accuracy alone is not considered sufficient due to class imbalance.

---

## Repeats and Random Seeds

- All stochastic models must be evaluated with a fixed random seed
- Default seed: 42
- No hyperparameter tuning is permitted across evaluation folds

If repeated runs are performed, the number of repeats and aggregation method
must be explicitly reported.

---

## Reporting Rules

- All results must be reported as:
  - Mean ± standard deviation across folds
- Fold-wise results must be retained for reproducibility
- No post-hoc metric selection is permitted
- The same protocol must be applied to all baselines and models

Any deviation from this protocol must be explicitly stated and justified.

---

## Intended Use

This evaluation protocol is intended for research benchmarking only.
It must not be used to support clinical decision-making.
