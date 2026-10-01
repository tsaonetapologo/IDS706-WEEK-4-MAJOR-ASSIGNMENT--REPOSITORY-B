from pathlib import Path

import pandas as pd

DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / ("Ecommerce_Consumer_Behavior_Analysis_Data.csv")
)


def load_data(path=DATA_PATH):
    """Load the e-commerce consumer behavior dataset."""
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """Clean the dataset for analysis."""
    cleaned = df.copy()

    # Standardize column names
    cleaned.columns = cleaned.columns.str.strip().str.lower().str.replace(" ", "_")

    # Remove completely empty rows
    cleaned = cleaned.dropna(how="all")

    # Remove duplicate records
    cleaned = cleaned.drop_duplicates()

    return cleaned


def prepare_model_data(df):
    """Prepare age and purchase amount for regression analysis."""
    model_df = df[["age", "purchase_amount"]].copy()

    model_df["age"] = pd.to_numeric(model_df["age"], errors="coerce")
    model_df["purchase_amount"] = pd.to_numeric(
        model_df["purchase_amount"], errors="coerce"
    )

    model_df = model_df.dropna()

    return model_df
