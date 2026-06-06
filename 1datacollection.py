import pandas as pd
import requests

# Load CSV
df = pd.read_csv("SampleSuperstore.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Example API Data Collection
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    api_data = response.json()
    api_df = pd.DataFrame(api_data)
    print(api_df.head())