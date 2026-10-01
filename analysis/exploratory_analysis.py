import pandas as pd
import polars as pl
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.ecommerce_analysis import load_data, clean_data, prepare_model_data

# Load the dataset
df = load_data()

# Clean the dataset
cleaned_df = clean_data(df)

# Prepare data for modeling
model_df = prepare_model_data(cleaned_df)

print(cleaned_df.head())
print(cleaned_df.shape)

# Examine the main variables
print("\nAge summary:")
print(f"mean: {model_df['age'].mean():.6f}")
print(f"median: {model_df['age'].median():.6f}")
print(f"min: {model_df['age'].min():.6f}")
print(f"max: {model_df['age'].max():.6f}")

print("\nPurchase amount summary:")
print(f"mean: {model_df['purchase_amount'].mean():.6f}")
print(f"median: {model_df['purchase_amount'].median():.6f}")
print(f"min: {model_df['purchase_amount'].min():.6f}")
print(f"max: {model_df['purchase_amount'].max():.6f}")

# Visualize the relationship between age and purchase amount
plt.figure(figsize=(8, 5))
plt.scatter(model_df["age"], model_df["purchase_amount"], alpha=0.6)

plt.xlabel("Customer Age")
plt.ylabel("Purchase Amount")
plt.title("Customer Age vs. Purchase Amount")

plt.tight_layout()
plt.savefig("reports/age_vs_purchase_amount.png", dpi=300)
plt.close()

# Calculate the correlation between age and purchase amount
correlation = float(model_df["age"].corr(model_df["purchase_amount"]))
correlation = max(-1.0, min(1.0, correlation))

print("\nCorrelation coefficient between age and purchase amount:")
print(f"{correlation:.6f}")

# Build a simple linear regression model
from sklearn.linear_model import LinearRegression

X = model_df[["age"]]
y = model_df["purchase_amount"]

model = LinearRegression()
model.fit(X, y)

print("\nLinear regression model:")
print(f"Coefficient: {model.coef_[0]:.4f}")
print(f"Intercept: {model.intercept_:.4f}")

from sklearn.metrics import r2_score, mean_squared_error

# Evaluate the regression model
predictions = model.predict(X)

r_squared = r2_score(y, predictions)
rmse = mean_squared_error(y, predictions) ** 0.5

print("\nModel evaluation:")
print(f"R-squared: {r_squared:.4f}")
print(f"RMSE: {rmse:.4f}")

# Polars analysis
print("\nPolars analysis:")

polars_df = pl.from_pandas(model_df)

print(polars_df.shape)

print(
    polars_df.select(
        [
            pl.col("age").mean().alias("mean_age"),
            pl.col("purchase_amount").mean().alias("mean_purchase_amount"),
        ]
    )
)
