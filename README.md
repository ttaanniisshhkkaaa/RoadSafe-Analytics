# RoadSafe Analytics

### Predictive Analysis of Road Collision Severity, Casualty Outcomes and Geospatial Patterns

RoadSafe Analytics is an end-to-end data science and machine learning project that analyzes real-world road collision, vehicle, and casualty records from Great Britain.

The project aims to investigate road collision patterns, classify collision severity, estimate casualty counts, and identify geographical concentrations of reported collisions.

## Project Objectives

- Clean and integrate real-world road safety datasets.
- Perform exploratory data analysis (EDA).
- Investigate environmental, temporal, and road-related collision patterns.
- Develop and compare classification and regression models.
- Apply clustering techniques for geographical and collision-profile analysis.
- Build an interactive dashboard to communicate findings.

## Repository Structure

```text
RoadSafe-Analytics/
├── data/
│   ├── raw/          # Original datasets and official data guide (local only)
│   ├── interim/      # Intermediate datasets
│   └── processed/    # Cleaned Parquet datasets (local only)
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   └── 02_data_cleaning.ipynb
├── src/              # Reserved for reusable Python modules
├── models/           # Trained models and pipelines (future stages)
├── reports/
│   └── figures/      # Visualizations and plots
├── app/              # Interactive dashboard (future stage)
├── tests/            # Optional automated tests
├── .gitignore
├── README.md
└── requirements.txt
```

## Dataset

**Source:** UK Department for Transport (STATS19)  
**Year:** 2025  
**Geographical Coverage:** Great Britain  
**Official Dataset:** https://www.gov.uk/government/statistical-data-sets/road-safety-open-data

The project uses three related datasets:

| Dataset | Records | Original columns |
|---|---:|---:|
| Collisions | 101,525 | 44 |
| Vehicles | 183,948 | 32 |
| Casualties | 127,883 | 24 |

**Total:** 413,356 records across three related tables (not 413,356 independent collisions).

The original CSV files and official Excel data guide are not included in the repository. Download them from the official source and place them in `data/raw/` before running the notebooks.

## Stage 3 — Data Understanding & Quality Assessment

The initial data audit identified:

- Eight conventional missing cells across four geographical columns in the collision dataset.
- Coded unknown, unavailable, deprecated, and historically inapplicable values that are not detected by ordinary null checks.
- `local_authority_district` as deprecated; `age_of_vehicle` contains `-1` in all 2025 vehicle records.
- No exact duplicate rows in any of the three datasets.
- Unique collision identifiers and valid collision/vehicle/casualty reference relationships in the observed data.

The complete inspection and audit are documented in [01_data_understanding.ipynb](notebooks/01_data_understanding.ipynb).

## Stage 4 — Data Cleaning & Preprocessing

The cleaning workflow is documented in [02_data_cleaning.ipynb](notebooks/02_data_cleaning.ipynb). It uses the official STATS19 data guide to examine special codes and performs a documented initial cleaning pass on all three datasets.

### Cleaning performed

- Converted selected documented missing, unknown, or unavailable codes into explicit Pandas missing values, using column-specific decisions.
- Removed `local_authority_district` (deprecated) and `age_of_vehicle` (entirely unavailable in the examined vehicle records) from the working analytical tables.
- Retained historical reporting fields rather than discarding potentially useful information; their suitability for modelling will be reviewed during feature selection.
- Parsed collision dates and checked time formats.
- Screened severity, collision counts, speed limits, ages, and geographical coordinate ranges.
- Verified collision identifier uniqueness, composite-key uniqueness, cross-table references, and preservation of the classification and regression targets.
- Exported cleaned datasets to Parquet and checked that the saved files match the working DataFrames.

### Before-and-after summary

| Dataset | Original rows | Cleaned rows | Original columns | Cleaned columns | Original missing cells | Cleaned missing cells |
|---|---:|---:|---:|---:|---:|---:|
| Collisions | 101,525 | 101,525 | 44 | 43 | 8 | 553,414 |
| Vehicles | 183,948 | 183,948 | 32 | 31 | 0 | 801,266 |
| Casualties | 127,883 | 127,883 | 24 | 24 | 0 | 71,847 |

The increased missing-value counts reflect the conversion of previously coded unavailable information into explicit missing values; they do **not** mean that additional records were lost. All 11 recorded relational-integrity and target-preservation checks passed.

### Cleaned outputs

Running the cleaning notebook generates these local files:

- `data/processed/collisions_clean.parquet`
- `data/processed/vehicles_clean.parquet`
- `data/processed/casualties_clean.parquet`

These generated datasets are excluded from Git tracking. They are not included in the repository and must be regenerated locally.

### Reproducing Stage 4

1. Clone the repository and install the dependencies from `requirements.txt` in a Python virtual environment.
2. Download the three 2025 STATS19 CSV files and the official Excel data guide into `data/raw/`, preserving the filenames expected by the notebook.
3. Open `notebooks/02_data_cleaning.ipynb` in Jupyter or VS Code and select the project Python environment.
4. Restart the kernel and run all cells in order.
5. Check the quality summary, integrity checks, and generated Parquet files in `data/processed/`.

### Cleaning limitations

- Not every special code is equivalent to a missing observation; some represent meaningful unknown or inapplicable categories. The notebook records the initial code-handling choices, which should be revisited if a downstream analysis needs those distinctions.
- Historical and current reporting fields are retained without automatic harmonization.
- Range checks cannot guarantee that every recorded value is factually correct.
- Model-specific imputation, categorical encoding, scaling, and feature selection will be handled in later stages using leakage-safe training pipelines.

## Machine Learning Tasks

### Classification
Predict collision severity across three classes: **Fatal**, **Serious**, and **Slight**.

### Regression
Estimate the number of casualties per reported collision.

### Clustering
- **DBSCAN:** Geographical collision concentration analysis.
- **K-Means:** Collision-profile segmentation.

## Technologies

- Python, Pandas, and NumPy
- Matplotlib, Seaborn, and Plotly
- Scikit-learn and Statsmodels
- Jupyter Notebook
- PyArrow and OpenPyXL
- Streamlit (planned dashboard)
- Git and GitHub

## Project Status

**Current Phase:** Stage 4 — Data Cleaning & Preprocessing (Implemented; documentation and GitHub review in progress)

- [x] Stage 1: Project Planning & Problem Definition
- [x] Stage 2: Environment Setup & GitHub Repository
- [x] Stage 3: Data Acquisition & Understanding
- [x] Stage 4: Data Cleaning & Preprocessing — notebook implementation and local validation
- [ ] Stage 5: Data Integration & Feature Engineering
- [ ] Stage 6: Exploratory Data Analysis
- [ ] Stage 7: Regression Modelling
- [ ] Stage 8: Classification Modelling
- [ ] Stage 9: Clustering Analysis
- [ ] Stage 10: Model Optimization & Interpretability
- [ ] Stage 11: Interactive Dashboard Development
- [ ] Stage 12: Final Documentation & Release

**Next Phase:** Data Integration & Feature Engineering, after Stage 4 is committed and reviewed.

## Limitations

The dataset includes reported personal-injury collisions rather than all road journeys. Predictive models estimate outcomes associated with recorded collisions, not whether a collision will occur.

Geographical collision concentrations do not necessarily represent traffic-adjusted collision risk.

## License and Attribution

Road safety data is sourced from the UK Department for Transport. Dataset attribution and applicable reuse terms will be documented alongside the data acquisition workflow.
