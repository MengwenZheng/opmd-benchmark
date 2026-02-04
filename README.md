# OPMD Risk / CPLIP Benchmark

Benchmark for AI-based risk stratification of oral potentially malignant disorders


Key notes:
- The final stable version will remain archived and citable.


## Quickstart
```bash
conda activate opmd-bench
pip install -r requirements.txt
# or: conda env update -n opmd-bench -f environment.yml
python scripts/check_setup.py

## Maintenance, Versioning, and Feedback Plan

This benchmark is maintained with a focus on stability, transparency, and long-term reproducibility.

### Versioning and release schedule

- **v0.1 (research preview)**  
  Initial public release including dataset structure, baseline models, and evaluation protocols.  
  Minor issues and documentation updates may occur.

- **v0.2 (refinement release)**  
  Bug fixes, clarification of evaluation scripts, and documentation improvements.  
  No changes to labels or data splits.

- **v1.0 (stable release)**  
  Dataset, labels, and evaluation protocols are frozen.  
  This version is intended for long-term comparison and citation.

No backward-incompatible changes will be introduced after v1.0.

### Update communication

All updates will be communicated through:
- GitHub Releases
- A public CHANGELOG.md file

No silent changes will be made to data, labels, or evaluation scripts.

### Feedback and issue reporting

GitHub Issues is the primary channel for:
- Bug reports
- Reproducibility issues
- Documentation questions
- Baseline or feature requests

All discussions are public to ensure transparency.

### Contact and governance

- **Maintainer**: Mengwen Zheng  
- **Supervisory oversight**: Academic supervisors associated with the project

### Retirement and deprecation

The benchmark may be retired or frozen if data governance, ethical, or institutional constraints require it.

## Dataset
Detailed information about the dataset, including intended use,
composition, and limitations, is provided in the
[Dataset Card](DATASET_CARD.md).

> ⚠️ Data are not yet publicly released.
> This repository currently provides benchmark documentation,
> configuration, and evaluation code only.


If retirement occurs, the final stable version will remain archived and citable, but no further updates will be guaranteed.
