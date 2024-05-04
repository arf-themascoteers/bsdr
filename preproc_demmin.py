import pandas as pd

dest = "data/demmin.csv"
df = pd.read_csv("data/demmin/demmin.csv")
df.to_csv(dest, index=False)
columns_with_nan = df.columns[df.isna().any()]
print(columns_with_nan)
print(len(df.columns))