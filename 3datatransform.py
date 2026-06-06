import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_superstore.csv")

# Create new transformed columns
df['Revenue'] = df['Sales']

df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100

df['Discount_Percentage'] = df['Discount'] * 100

df['Total_Value'] = df['Sales'] * df['Quantity']

# Display transformed data
print(df.head())

# Save transformed dataset
df.to_csv("transformed_superstore.csv", index=False)

print("Transformation completed successfully!")