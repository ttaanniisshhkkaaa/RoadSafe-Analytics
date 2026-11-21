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
│   ├── 02_data_cleaning.ipynb
│   ├── 03_data_integration.ipynb
│   └── 09_dbscan.ipynb   # DBSCAN clustering (merged Stage 9 work)
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

## Stage 5 — Data Integration & Feature Engineering

**Status: Completed locally; GitHub integration pending.**

The workflow in [03_data_integration.ipynb](notebooks/03_data_integration.ipynb) joins the cleaned 2025 STATS19 datasets at the **collision level**, preserving one record per collision instead of directly joining individual vehicle and casualty rows.

### Work completed

- Verified the relationships among **101,525 collisions**, **183,948 vehicle records**, and **127,883 casualty records**.
- Aggregated vehicle and casualty counts by `collision_index`; both matched the corresponding collision-level counts with **zero mismatches**.
- Engineered vehicle summaries: mean known driver age, count of known driver ages, and number of distinct vehicle types.
- Engineered casualty summaries for **descriptive analysis only**: mean known casualty age, count of known casualty ages, and number of distinct casualty types.
- Joined the summaries to the collision table using validated one-to-one left joins, preserving all **101,525 unique collision IDs**.
- Created temporal features: `month`, `day_of_week`, `hour`, `is_weekend`, and `time_of_day`.
- Prepared separate classification and regression tables, each with **11 selected predictors** and its respective target.
- Excluded casualty-derived summaries and the other task's target from each predictive table to reduce target leakage.
- Passed **10 final machine-learning dataset validation checks** and verified that all exported Parquet files match the in-memory DataFrames.

### Stage 5 outputs

| Local file in `data/processed/` | Rows | Columns | Intended use |
|---|---:|---:|---|
| `integrated_analytical.parquet` | 101,525 | 53 | Descriptive analysis and EDA; contains post-collision summaries |
| `classification_ready.parquet` | 101,525 | 12 | Collision-severity classification |
| `regression_ready.parquet` | 101,525 | 12 | Casualty-count regression |

The initial shared predictors are `number_of_vehicles`, `speed_limit`, `road_type`, `first_road_class`, `light_conditions`, `weather_conditions`, `road_surface_conditions`, `month`, `day_of_week`, `hour`, and `is_weekend`. The targets are `collision_severity` and `number_of_casualties`, respectively. The derived `time_of_day` category is retained in the integrated analytical dataset, not in the initial modelling tables.

**Reproduce Stage 5:** First run Stage 4 to create `collisions_clean.parquet`, `vehicles_clean.parquet`, and `casualties_clean.parquet`. Then restart the kernel and run every cell in `notebooks/03_data_integration.ipynb`. The notebook exports and reloads the three Stage 5 files to verify them. Generated Parquet files are excluded from Git and must be recreated locally.

**Modelling caveats:** The initial predictor set supports estimating outcomes *conditional on a recorded collision*, not forecasting collision occurrence before it happens. Some attributes (such as the number of involved vehicles) may not be available pre-collision. Missing predictor values remain in the exported tables; train-only imputation, categorical encoding, train/test splitting, and final leakage review belong in the modelling stages. The 10 validation checks verify dataset structure and target preservation, not predictive accuracy.

## Stage 9 — Geospatial Clustering (DBSCAN)

**Status: DBSCAN implementation merged; follow-up improvements tracked separately.**

The DBSCAN work explores geographical concentrations of reported collisions using latitude/longitude, haversine distance, parameter comparisons, and cluster visualizations. The reported configuration uses `eps = 0.50 km` and `min_samples = 10`. The notebook is [09_dbscan.ipynb](notebooks/09_dbscan.ipynb).

Pending review items include verifying the reported 44-column input against the 43-column Stage 4 cleaned collision table, examining the geographical extent of the largest cluster, improving histogram bins, and removing blanket warning suppression. These are follow-up quality tasks; geographical density is not equivalent to traffic-adjusted risk. The wider Stage 9 clustering phase, including K-Means, is not yet marked complete.

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

**Current Phase:** Stage 5 — Data Integration & Feature Engineering (completed locally; pull request pending)

- [x] Stage 1: Project Planning & Problem Definition
- [x] Stage 2: Environment Setup & GitHub Repository
- [x] Stage 3: Data Acquisition & Understanding
- [x] Stage 4: Data Cleaning & Preprocessing — notebook implementation and local validation
- [x] Stage 5: Data Integration & Feature Engineering — notebook, validation, and local exports complete
- [ ] Stage 6: Exploratory Data Analysis
- [ ] Stage 7: Regression Modelling
- [ ] Stage 8: Classification Modelling
- [ ] Stage 9: Clustering Analysis
- [ ] Stage 10: Model Optimization & Interpretability
- [ ] Stage 11: Interactive Dashboard Development
- [ ] Stage 12: Final Documentation & Release

**Next Phase:** Stage 6 — Exploratory Data Analysis, followed by regression and classification modelling. DBSCAN work has been merged separately, with follow-up refinements pending.

## Limitations

The dataset includes reported personal-injury collisions rather than all road journeys. Predictive models estimate outcomes associated with recorded collisions, not whether a collision will occur.

Geographical collision concentrations do not necessarily represent traffic-adjusted collision risk.

## License and Attribution

Road safety data is sourced from the UK Department for Transport. Dataset attribution and applicable reuse terms will be documented alongside the data acquisition workflow.
