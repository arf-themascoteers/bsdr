import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'd:\work10\ghisa2.csv')
# df = df.dropna()
# df.to_csv(r'd:\work10\ghisa2.csv', index=False)
df_aggregated = df.groupby('Crop').mean()
cols = df.columns
cols = [col for col in df.columns if col != "Crop"]
i_cols = [int(s[1:]) for s in cols]

for row in df_aggregated.itertuples():
    val = row[0]
    ref = row[1:]
    plt.plot(i_cols, ref, label=val.replace("_", " ").title())

plt.legend()

plt.xlabel("Wavelength (nm)", fontsize=15)
plt.ylabel("Reflectance (%)", fontsize=15)
plt.legend(fontsize=13)
plt.margins(0.01)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("ghisaconus.png")
