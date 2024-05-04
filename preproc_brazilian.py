import pandas as pd

dest = "data/brazilian.csv"
df = pd.read_csv("data/brazilian/ALL.csv")
cols = list(df.columns)
excluded_cols = ['Amostra', 'Areia', 'Silte', 'Argila', 'pH (H2O)', 'pH (KCl)', 'pH (pH CaCl2)', 'COS (g.kg-1)', 'P (mg dm3)', 'K (mmolc/dm3)', 'Ca (mmolc/dm3)', 'Mg (mmolc/dm3)', 'Al (mmolc/dm3)', 'H (mmolc/dm3)', 'H+Al (mmolc/dm3)', 'SB (mmolc/dm3)', 'CTC (mmolc/dm3)', 'V%', 'Classe V%', 'm%', 's (mg dm3)', 'Na (mg dm3)', 'B (mg dm3)', 'Fe (mg dm3)', 'Cu (mg dm3)', 'Zn (mg dm3)', 'Mn (mg/dm3)']
df.drop(columns=excluded_cols, inplace=True)
df.drop(df.index[247:], inplace=True)
df.to_csv(dest, index=False)
columns_with_nan = df.columns[df.isna().any()]
print(columns_with_nan)