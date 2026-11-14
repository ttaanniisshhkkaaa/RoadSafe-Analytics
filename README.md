
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
│   ├── raw/          # Original datasets (not tracked by Git)
│   ├── interim/      # Intermediate datasets
│   └── processed/    # Cleaned, analysis-ready datasets
├── notebooks/        # Jupyter notebooks
├── src/              # Reusable Python modules
├── models/           # Trained models and pipelines
├── reports/
│   └── figures/      # Visualizations and plots
├── app/              # Streamlit dashboard
├── tests/            # Automated tests
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

| Dataset | Records |
|---|---:|
| Collisions | 101,525 |
| Vehicles | 183,948 |
| Casualties | 127,883 |

The original datasets are not included in this repository. They can be obtained from the official source.

## Data Understanding & Quality Assessment

An initial data audit was conducted using the official 2025 STATS19 datasets and the Department for Transport data dictionary.

### Dataset Overview

| Dataset | Records | Columns |
|---|---:|---:|
| Collisions | 101,525 | 44 |
| Vehicles | 183,948 | 32 |
| Casualties | 127,883 | 24 |

**Total:** 413,356 records across three related datasets.

### Key Findings

- **Missing Values:** Eight conventional missing cells were identified across four geographical columns in the collision dataset.
- **Coded Missing Values:** Several variables contain special codes representing unknown, unavailable, deprecated, or historically inapplicable information.
- **Deprecated and Unavailable Features:** local_authority_district is deprecated, while age_of_vehicle contains -1 in all 2025 vehicle records and requires further investigation.
- **Categorical Encoding:** Many categorical attributes are stored as numerical codes and require interpretation using the official data dictionary.
- **Duplicate Records:** No exact duplicate rows were detected in any dataset.
- **Identifier Integrity:** All 101,525 collision identifiers are consistently represented across the three datasets.
- **Composite Keys:** Vehicle and casualty composite identifiers were verified to be unique.
- **Referential Integrity:** No unmatched casualty-to-vehicle references were detected.

### Key Challenges Identified

1. Column-specific handling of coded missing and unknown values.
2. Identification of deprecated and historical variables.
3. Decoding categorical attributes.
4. Handling missing geographical coordinates.
5. Preventing target leakage during predictive modelling.
6. Preserving relational integrity during data integration.

### Notebook

The complete data-understanding process, Python code, inspection results, and documented observations are available in:

[01_data_understanding.ipynb](notebooks/01_data_understanding.ipynb)

**Next Phase:** Data Cleaning & Preprocessing.


## Machine Learning Tasks

### Classification
Predict collision severity:
- Fatal
- Serious
- Slight

### Regression
Estimate the number of casualties per reported collision.

### Clustering
- DBSCAN: Geographical collision concentration analysis.
- K-Means: Collision-profile segmentation.

## Technologies

- Python
- Pandas and NumPy
- Matplotlib, Seaborn and Plotly
- Scikit-learn
- Statsmodels
- Jupyter Notebook
- Streamlit
- Git and GitHub

## Project Status

**Current Phase:** Stage 3 — Data Acquisition & Understanding (Completed)

### Completed Stages

- [x] Stage 1: Project Planning & Problem Definition
- [x] Stage 2: Environment Setup & GitHub Repository
- [x] Stage 3: Data Acquisition & Understanding
- [ ] Stage 4: Data Cleaning & Preprocessing
- [ ] Stage 5: Data Integration & Feature Engineering
- [ ] Stage 6: Exploratory Data Analysis
- [ ] Stage 7: Regression Modelling
- [ ] Stage 8: Classification Modelling
- [ ] Stage 9: Clustering Analysis
- [ ] Stage 10: Model Optimization & Interpretability
- [ ] Stage 11: Interactive Dashboard Development
- [ ] Stage 12: Final Documentation & Release

## Limitations

The dataset includes reported personal-injury collisions rather than all road journeys. Predictive models estimate outcomes associated with recorded collisions, not whether a collision will occur.

Geographical collision concentrations do not necessarily represent traffic-adjusted collision risk.

## License and Attribution

Road safety data is sourced from the UK Department for Transport. Dataset attribution and applicable reuse terms will be documented alongside the data acquisition workflow.
