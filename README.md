# E-Commerce Consumer Behavior Analysis

## Overview

This project analyzes the relationship between customer age and purchase amount in an e-commerce dataset. It includes data loading, cleaning, exploratory analysis, visualization, and simple predictive modeling.

The repository is organized for reproducibility and uses automated testing to validate the core data-processing functions.

## Research Question

Is there a relationship between customer age and purchase amount in the dataset?

## Dataset

The dataset is stored in the `data/` directory and contains customer-level records including age and purchase information.

Key variables used in the analysis:

- `age`
- `purchase_amount`

## Project Structure

```text
IDS706-WEEK-4-MAJOR-ASSIGNMENT--REPOSITORY-B/
├── analysis/
│   └── exploratory_analysis.py
├── data/
│   └── Ecommerce_Consumer_Behavior_Analysis_Data.csv
├── notebooks/
│   └── ...
├── reports/
│   └── age_vs_purchase_amount.png
├── src/
│   ├── __init__.py
│   └── ecommerce_analysis.py
├── tests/
│   └── test_ecommerce_analysis.py
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
└── .pytest_cache/
```

## Setup

Create and activate a virtual environment, then install the required dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Analysis

From the project root, run:

```bash
python -m analysis.exploratory_analysis
```

This script:

- loads the dataset
- cleans it
- prepares modeling data
- prints summary statistics for age and purchase amount
- saves a scatter plot to `reports/age_vs_purchase_amount.png`
- computes the correlation coefficient between age and purchase amount
- fits and evaluates a simple linear regression model

## Run the Tests

The project uses `pytest` for automated validation.

From the project root, run:

```bash
pytest
```

A configuration file is included in `pytest.ini` to ensure the project root is on the Python import path:

```ini
[pytest]
pythonpath = .
```

## Recent Fixes and Notes

- `purchase_amount` values are cleaned by stripping `$` and `,` before conversion to numeric data.
- Invalid or missing values are removed before modeling.
- The correlation coefficient is clamped to the valid range `[-1, 1]`.
- The test suite verifies the data-loading and model-preparation workflow.

## Tools Used

- Python
- pandas
- polars
- matplotlib
- scikit-learn
- pytest

## Workflow Summary

1. Load the raw dataset.
2. Clean and standardize the data.
3. Prepare `age` and `purchase_amount` for modeling.
4. Explore descriptive statistics.
5. Visualize the relationship between the variables.
6. Compute the correlation coefficient.
7. Fit a simple regression model.
8. Validate with automated tests.

## Analysis Results

### Age

- Mean: 34.304 years
- Median: 34.500 years
- Minimum: 18.000 years
- Maximum: 50.000 years

### Purchase Amount

- Mean: 275.063880
- Median: 276.165000
- Minimum: 50.710000
- Maximum: 498.330000

## Correlation

The correlation between customer age and purchase amount is approximately `-0.0163`. This indicates that the linear relationship between age and purchase amount is very weak in this dataset.

## Linear Regression

A simple linear regression model was created using:

- Predictor: `age`
- Response: `purchase_amount`

The model produced:

- Coefficient: `-0.2292`
- Intercept: `282.9270`
- R-squared: `0.0003`
- RMSE: `131.4498`

The very small R-squared indicates that customer age explains very little of the variation in purchase amount in this dataset.

## Pandas and Polars

Pandas was used for the primary data loading, cleaning, transformation, and analysis workflow. Polars was also used to perform an additional analysis and demonstrate an alternative dataframe library.

## Testing

The project uses `pytest` for automated testing. The tests verify that:

- data can be loaded successfully
- data cleaning produces a non-empty dataset
- the modeling dataset contains the required variables
- purchase amount values are present and valid

## Limitations

This analysis uses customer age as the only predictor of purchase amount. Other factors, such as product characteristics, customer preferences, income, or purchasing behavior, may also influence purchase amount.

Therefore, the regression results should not be interpreted as evidence that age causes changes in purchase amount.

## Reproducibility

The required Python packages are listed in `requirements.txt`.

The project can be reproduced by installing the dependencies, running the analysis module, and running the automated test suite.
