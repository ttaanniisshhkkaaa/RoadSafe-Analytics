
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

**Current Phase:** Environment Setup

The project is under active development.

## Limitations

The dataset includes reported personal-injury collisions rather than all road journeys. Predictive models estimate outcomes associated with recorded collisions, not whether a collision will occur.

Geographical collision concentrations do not necessarily represent traffic-adjusted collision risk.

## License and Attribution

Road safety data is sourced from the UK Department for Transport. Dataset attribution and applicable reuse terms will be documented alongside the data acquisition workflow.
