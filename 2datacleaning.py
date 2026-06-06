import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

# Check missing values
print(df.isnull().sum())

# Fill missing values
df.ffill(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Verify
print(df.duplicated().sum())

# Save cleaned data
df.to_csv("cleaned_superstore.csv", index=False)