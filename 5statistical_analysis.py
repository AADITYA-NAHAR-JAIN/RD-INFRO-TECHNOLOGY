import pandas as pd
from typing import Any

from scipy.stats import (
    ttest_ind
)

df = pd.read_csv(
    "transformed_superstore.csv"
)

print(df.describe())

print("\nAverage Profit by Category\n")

print(
    df.groupby("Category")
      ["Profit"]
      .mean()
)

technology = df[
    df["Category"] == "Technology"
]["Profit"]

furniture = df[
    df["Category"] == "Furniture"
]["Profit"]

result: Any = ttest_ind(
    technology,
    furniture
)

t_stat = float(result[0])
p_value = float(result[1])

print("\nT Statistic:", t_stat)
print("P Value:", p_value)

if p_value < 0.05:
    print(
        "Significant Difference Exists"
    )
else:
    print(
        "No Significant Difference"
    )