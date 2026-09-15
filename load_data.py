import pandas as pd

file_path = "data/raw/locations.csv"

df = pd.read_csv(file_path)

print("Raw data:")
print(df)

print("\nNumber of records:", len(df))
print("Columns:", list(df.columns))