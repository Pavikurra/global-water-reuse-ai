# Methodology

## 1. Project Objective

This project estimates global greywater production, reuse potential, and water reuse readiness using open-source data, engineered estimates, machine learning, and dashboard visualization.

## 2. Data Sources

The project is designed to use open global datasets such as:

- World Bank population indicators
- wastewater treatment indicators
- municipal water use datasets
- manually curated plumbing and treatment method references

## 3. Greywater Estimation

Greywater production is estimated using population-based assumptions.

```text
estimated_greywater_m3_year = population × estimated_greywater_per_person_per_year
