# E-Commerce Consumer Behavior Analysis

## Project Overview

This project analyzes e-commerce consumer behavior using a structured consumer
behavior dataset. The project focuses on data cleaning, exploratory data
analysis, visualization, and predictive modeling.

Repository B was rebuilt from the original project with an emphasis on
improved project organization, reusable Python functions, automated testing,
documentation, and reproducibility.

The analysis focuses particularly on the relationship between customer age
and purchase amount.

## Research Question

> Is there a relationship between customer age and purchase amount in the e-commerce consumer behavior dataset?

## Dataset

The project uses an e-commerce consumer behavior dataset containing information
about customers and their purchasing behavior.

The dataset is stored locally in the `data/` directory.

### Main variables used

- `age` — customer age
- `purchase_amount` — amount spent by the customer

Additional variables in the dataset may be used during exploratory analysis.

## Project Objectives

The main objectives of this project are to:

1. Load and inspect the raw dataset.
2. Clean and prepare the data for analysis.
3. Handle missing and duplicate records.
4. Explore consumer behavior using descriptive statistics.
5. Create visualizations to identify patterns and relationships.
6. Prepare relevant variables for predictive modeling.
7. Examine the relationship between customer age and purchase amount.
8. Use automated tests to verify important data-processing functions.
9. Make the analysis reproducible through documented dependencies and
   organized project structure.

## Project Structure

```text
IDS706-WEEK-4-MAJOR-ASSIGNMENT--REPOSITORY-B/
│
├── data/
│   └── Ecommerce_Consumer_Behavior_Analysis_Data.csv
│
├── notebooks/
│   └── ...
│
├── reports/
│   └── ...
│
├── src/
│   ├── __init__.py
│   └── ecommerce_analysis.py
│
├── tests/
│   └── test_ecommerce_analysis.py
│
├── .gitignore
├── README.md
└── requirements.txt