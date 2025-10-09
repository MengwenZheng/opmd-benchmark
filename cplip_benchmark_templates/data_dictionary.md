# CPLIP Benchmark – Preparing Stage Data Dictionary (v1.0, 2025-10-06)

This folder contains CSV templates for assembling the **minimum viable dataset** and optional extras for your CPLIP OPMD benchmark.

## Core (must-have)

### patients.csv  (one row per patient)
- `patient_id` (string): Unique, de-identified ID.
- `site_id` (string): Recruiting site / hospital.
- `sex` (M/F/Other/Unknown)
- `birth_year` (int) and `age_at_index` (years) – record either or both.
- `smoking_status` (Never/Former/Current/Unknown)
- `alcohol_use` (None/Moderate/High/Unknown) – or free text.
- `comorbidities` (free text or coded list)
- `baseline_lesion_type` (e.g., leukoplakia, erythroplakia, OLP, etc.)
- `baseline_histology_grade` (if **baseline-only** biopsy was done; avoid follow-up grades here)
- `index_date` (YYYY-MM-DD): baseline “time-zero” (first qualifying visit/biopsy).
- `consent_flag` (0/1): if required for governance.

### slides.csv  (one row per WSI)
- `slide_id`: Unique slide identifier.
- `patient_id`, `lesion_id`, `site_id`
- `wsi_path`: File path (or relative path) to the WSI (e.g., .svs, .tif).
- `scanner_vendor`, `scanner_model`, `magnification` (e.g., 20×), `mpp` (microns per pixel).
- `stain` (H&E), `acquisition_date`.

### roi_annotations.csv
- `slide_id`
- `roi_file` (e.g., GeoJSON/JSON/ASAP XML path)
- `roi_format` (geojson/xml/mask_png)
- `annotator_id`, `annotation_date`
- `roi_type` (lesion, epithelium, exclude, etc.)

### outcomes.csv  (patient-level endpoint and censoring)
- `patient_id`
- `transformed_to_oscc` (0/1)
- `transformation_date` (YYYY-MM-DD) – first biopsy-confirmed OSCC.
- `first_oscc_site` (oral subsite), if known.
- `death_date` (YYYY-MM-DD) – for competing risk.
- `death_due_to_oscc` (0/1/Unknown)
- `last_followup_date` (YYYY-MM-DD) – for right-censoring.

### splits.csv  (frozen evaluation protocol)
- `patient_id`, `site_id`, `fold` (1..5), `split` (train/val/test).
Lock once and version-control this file.

## Helpful (nice-to-have)

### visits.csv  (longitudinal context)
- Per-visit record of `visit_date`, `biopsy_performed` (0/1), `histology_grade`, `treatment`.

### tiles_manifest.csv  (engineering cache)
- Where tiles/embeddings live per `slide_id`, plus tiling parameters.

### stain_refs.csv  (stain normalisation)
- Reference tiles per site for Macenko/A/B testing.

## Governance & metadata (store alongside CSVs)
- De-identification key (kept offline), ethics/HREC approvals, data use agreements.
- A short README describing index-date definition, follow-up window, and any inclusion/exclusion rules.
- Site glossary for variable coding (e.g., how smoking/alcohol are coded at each site).

## Notes
- Keep **baseline-only** features in modelling tables to avoid leakage from post-index data.
- Use **patient_id** as the join key between patients/outcomes/slides/splits.
- For survival/competing-risk analyses, dates (`index_date`, `transformation_date`, `death_date`, `last_followup_date`) are essential.
