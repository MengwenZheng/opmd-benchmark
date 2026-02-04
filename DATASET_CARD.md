# Dataset Card: OPMD-Bench

## 1. Dataset Summary
OPMD-Bench is a histopathology dataset designed for research on the
classification, grading, and risk stratification of Oral Potentially
Malignant Disorders (OPMDs) using whole-slide images (WSIs).

The dataset is intended for benchmarking machine learning and deep
learning models under weakly supervised and clinically realistic
conditions.

---

## 2. Motivation and Background
Oral potentially malignant disorders exhibit substantial histological
heterogeneity and inter-observer variability. Reliable risk
stratification remains challenging, particularly across institutions.

This dataset was created to support transparent, reproducible
evaluation of WSI-based models rather than to maximise performance.

---

## 3. Intended Use

### Appropriate Uses
- Research on OPMD risk stratification (binary or ordinal)
- Weakly supervised learning using WSIs
- Domain generalisation and multi-centre evaluation
- Methodological benchmarking and comparison

### Out-of-Scope Uses
- Clinical diagnosis or treatment decision-making
- Deployment in real-world patient care
- Fully supervised pixel-level segmentation training

---

## 4. Dataset Composition
- Modality: H&E-stained whole-slide images
- Image formats: `.mrxs`, `.tif`, `.svs`
- Labels: Slide-level labels only
- Annotations: Optional ROI annotations (QuPath GeoJSON)
- Patient structure: Multiple slides per patient possible

---

## 5. Label Definitions

### Primary Task
Binary risk stratification:
- Low-risk
- High-risk

### Optional Secondary Task
WHO-style dysplasia grading:
- Low-grade dysplasia
- High-grade dysplasia
- Squamous cell carcinoma (SCC)

Labels are derived from routine pathology reports at the source
institutions.

---

## 6. Data Collection Process
- Retrospective biopsy specimens
- Slides digitised using standard WSI scanners
- Labels assigned by trained pathologists as part of routine diagnosis
- No additional re-annotation or consensus labelling performed

---

## 7. Data Splits and Evaluation
- Strict patient-level splitting
- 5-fold cross-validation (CV5)
- Leave-One-Site-Out (LOSO) evaluation
- No tile-level data leakage permitted

Predefined splits are provided to ensure fair and reproducible
evaluation.

---

## 8. Preprocessing
- Tiling at fixed target magnification (e.g. 20×)
- Fixed tile size across all experiments
- Optional stain normalisation
- Removal of background or blank tiles

Exact preprocessing settings are documented in the benchmark
configuration files.

---

## 9. Dataset Size
Dataset size statistics will be updated as data collection and
curation progress.

---

## 10. Known Limitations
- Limited dataset size relative to modern foundation models
- Class imbalance between risk categories
- Inter-institutional variability in grading practices
- Labels reflect biopsy-level information only
- No longitudinal outcome data included

---

## 11. Ethical Considerations
- All data are de-identified at source
- No direct patient identifiers are included
- Dataset use is governed by institutional ethics approval
- The dataset is intended for research use only

---

## 12. Bias and Fairness
- Geographic and institutional bias may be present
- Demographic metadata are limited
- Models trained on this dataset may not generalise without external
  validation

---

## 13. Access and Licensing
- Access is restricted to approved researchers
- Redistribution is prohibited without permission
- Licensing terms will be finalised prior to public release

---

## 14. Maintenance and Versioning
- Dataset versions follow semantic versioning (v0.1 → v1.0)
- Updates and corrections are documented in a changelog
- Known issues are tracked via the GitHub issue tracker

---

## 15. Contact
Maintainer: Mengwen Zheng  
Affiliation: Dental School, The University of Western Australia  

For questions or issues, please use the repository issue tracker.

