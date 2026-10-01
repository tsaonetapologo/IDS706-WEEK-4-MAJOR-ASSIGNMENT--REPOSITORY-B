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
3. Handle missing values and duplicate records.
4. Explore consumer behavior using descriptive statistics.
5. Create visualizations to identify patterns and relationships.
6. Prepare relevant variables for predictive modeling.
7. Examine the relationship between customer age and purchase amount.
8. Build a simple regression model using customer age to predict purchase amount.
9. Use automated tests to verify key data-processing functions.
10. Organize the project for reproducibility and easy reuse.

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

## Folder and file descriptions

- `data/` — contains the e-commerce consumer behavior dataset.
- `notebooks/` — contains notebooks used for exploratory analysis and development.
- `reports/` — contains analysis outputs and project reports.
- `src/` — contains the reusable Python data-processing functions.
- `tests/` — contains automated tests for the project functions.
- `README.md` — documents the project, workflow, and reproducibility instructions.
- `requirements.txt` — lists the Python packages required to run the project.
- `.gitignore` — specifies files and folders that should not be tracked by Git.

## ## Methods / Workflow

The project follows a structured data analysis workflow:

1. **Load data** — Read the raw e-commerce dataset using Pandas.
2. **Clean data** — Standardize column names, remove completely empty rows, remove duplicate records, and handle data types.
3. **Prepare model data** — Select `age` and `purchase_amount`, convert them to numeric values, and remove invalid or missing observations.
4. **Explore the data** — Use descriptive statistics and exploratory analysis to understand the variables.
5. **Visualize relationships** — Create visualizations to examine patterns between customer age and purchase amount.
6. **Build the model** — Use a simple regression model to examine whether customer age can help predict purchase amount.
7. **Test the code** — Use `pytest` to verify that the main data-processing functions work as expected.
8. **Document and reproduce** — Record the project structure, dependencies, and workflow in the README.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Pytest
- Git and GitHub
- VS Code

## Testing

The project uses `pytest` for automated testing.

The test suite checks the main data-processing functions:

- `load_data()` — verifies that the dataset loads successfully.
- `clean_data()` — verifies that the cleaned dataset is not empty.
- `prepare_model_data()` — verifies that the required modeling variables, `age` and `purchase_amount`, are present.

Run the tests from the project root directory with:

```bash
python -m pytest

### Then add **How to Run**

```markdown
## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd IDS706-WEEK-4-MAJOR-ASSIGNMENT--REPOSITORY-B