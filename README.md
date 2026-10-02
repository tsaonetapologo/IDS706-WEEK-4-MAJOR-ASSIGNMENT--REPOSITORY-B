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

## AI-Assisted Workflow Summary

### Selected option
Option 1: AI-assisted workflow project for Repository B.

### Purpose of the project
This project demonstrates a reproducible, AI-assisted data analysis workflow for an e-commerce dataset. It focuses on data loading, cleaning, exploratory statistics, visualization, and a simple regression analysis.

### Install, run, and test

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m analysis.exploratory_analysis
pytest
```

### Docker build and run

```bash
docker build -t repo-b .
docker run --rm repo-b
```

The container uses the project root as the working directory and runs the exploratory analysis automatically when the image starts.

### Manual smoke test result
The manual smoke test was successful. The documented setup instructions worked, the analysis script executed without errors, the summary figures printed correctly, and the main output file was created in the `reports/` directory.

Observed results:

- mean age: `34.304000`
- mean purchase amount: `275.063880`
- correlation coefficient: `-0.016300`
- automated tests: `4 passed in 0.21s`
- Docker build: successful (`docker build -t repo-b .` completed successfully)

### AI role contributions
- Architect: defined the project goal, requirements, risks, and validation steps.
- Builder: implemented the data-cleaning fix, updated the analysis output, and aligned the project files with the working setup.
- Tester: reviewed the implementation against the plan and confirmed the expected behavior through the test suite.

### AI recommendations accepted
- Accepted the recommendation to strip currency symbols and commas before converting `purchase_amount` to numeric values.
- Accepted the recommendation to clamp the correlation coefficient to the valid range of `[-1, 1]`.

### Recommendations changed or rejected
- Rejected the idea of leaving the raw pandas summary output in the terminal; instead, the script now prints explicit numeric summary values for clarity.
- Adjusted the README to reflect the actual verified commands and results rather than a generic project description.

### Independent verification
The final result was verified independently by running:

```bash
pytest -q
python -m analysis.exploratory_analysis
```

These checks confirm the project runs successfully and the main feature output is produced as expected.

## Reproducibility

The required Python packages are listed in `requirements.txt`.

The project can be reproduced by installing the dependencies, running the analysis module, and running the automated test suite.
