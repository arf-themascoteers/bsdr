import pandas as pd

#df = pd.read_csv(f"d:/downloads/GHISACONUS.csv")

#6988
#print(len(df))

#198
#print(len(df.columns))

df = pd.read_csv(f"../data/ghisa.csv")

print(df["crop"].unique())

#6988
print(len(df))

#198
print(len(df.columns))