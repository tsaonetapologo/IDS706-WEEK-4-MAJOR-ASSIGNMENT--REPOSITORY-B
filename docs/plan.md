# AI-Assisted Workflow Plan

## Architect Review

### Project goal
Build a clean, reproducible e-commerce consumer behavior analysis project that loads data, cleans it, summarizes key metrics, computes a correlation coefficient, saves a visualization, and validates the workflow with tests.

### Requirements
- Maintain a project structure that is easy to run from the repository root.
- Keep the data-loading and cleaning workflow reusable.
- Handle currency-formatted purchase amounts correctly.
- Produce actual numeric summary metrics in the terminal.
- Keep correlation values within the valid range of -1 to 1.
- Save a visual output to the reports folder.
- Add automated tests for the core processing functions.
- Keep documentation aligned with the current implementation.

### Proposed changes
1. Keep the `src/ecommerce_analysis.py` module as the reusable data-processing layer.
2. Add a robust `prepare_model_data()` conversion that strips `$` and `,` before numeric conversion.
3. Add explicit summary printing in the analysis script so the terminal displays actual figures rather than a pandas dtype representation.
4. Clamp the final Pearson correlation to the valid range `[-1, 1]`.
5. Save the scatter plot to `reports/age_vs_purchase_amount.png`.
6. Add/retain pytest coverage for loading, cleaning, and modeling data.
7. Add `pytest.ini` to ensure imports work with plain `pytest`.
8. Update the README to reflect the actual commands and results.

### Important files
- `src/ecommerce_analysis.py` — reusable data-cleaning and preparation logic
- `analysis/exploratory_analysis.py` — exploratory analysis output and summary reporting
- `tests/test_ecommerce_analysis.py` — validation for the data-processing pipeline
- `pytest.ini` — import-path configuration for pytest
- `README.md` — user-facing instructions and project explanation
- `requirements.txt` — project dependencies
- `data/Ecommerce_Consumer_Behavior_Analysis_Data.csv` — source dataset

### Risks and design concerns
- Dataset values are stored as strings with currency formatting, which can silently convert to NaN if not normalized.
- Import issues may arise when running tests without setting `PYTHONPATH`.
- Terminal output should stay explicit and readable without hiding the true numeric values behind pandas series output.
- The project should remain simple and reproducible without requiring IDE-specific setup.

### Testing and verification
- Run `pytest -q` from the repository root.
- Run `python -m analysis.exploratory_analysis` to confirm actual values print in the terminal.
- Check that the plot file is generated under `reports/`.
- Verify the mean purchase amount is around `275.063880` and the correlation is within `[-1, 1]`.

### Review and corrections
This plan was reviewed after the initial implementation. The main corrections were to ensure the README and project commands reflect the actual working setup, and to keep the data-cleaning and output logic aligned with the current dataset formatting and terminal output requirements.
