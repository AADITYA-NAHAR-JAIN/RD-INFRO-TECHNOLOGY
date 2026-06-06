import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "transformed_superstore.csv"
)

print(df.describe())

# Sales Distribution

plt.figure(figsize=(8,5))
sns.histplot(
    data=df,
    x="Sales",
    bins=30
)
plt.title("Sales Distribution")
plt.show()

# Profit Distribution

plt.figure(figsize=(8,5))
sns.boxplot(
    data=df,
    x="Profit"
)
plt.title("Profit Distribution")
plt.show()

# Category Sales

plt.figure(figsize=(8,5))

df.groupby("Category")["Sales"] \
  .sum() \
  .sort_values() \
  .plot(kind="bar")

plt.title("Sales by Category")
plt.show()

# Region Profit

plt.figure(figsize=(8,5))

df.groupby("Region")["Profit"] \
  .sum() \
  .plot(kind="bar")

plt.title("Profit by Region")
plt.show()

# Segment Sales

plt.figure(figsize=(7,7))

df.groupby("Segment")["Sales"] \
  .sum() \
  .plot(
      kind="pie",
      autopct="%1.1f%%"
  )

plt.ylabel("")
plt.title("Sales by Segment")
plt.show()

# Top States

plt.figure(figsize=(10,5))

top_states = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(
          ascending=False
      )
      .head(10)
)

top_states.plot(kind="bar")

plt.title("Top 10 States")
plt.show()

# Correlation Heatmap

plt.figure(figsize=(8,6))

sns.heatmap(
    df[
        [
            "Sales",
            "Quantity",
            "Discount",
            "Profit"
        ]
    ].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()