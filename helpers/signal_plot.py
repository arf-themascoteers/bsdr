import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

fig, axs = plt.subplots(1, 3, figsize=(12, 4))

lucas = pd.read_csv("../data/ghisaconus.csv")
data = lucas.iloc[50,1:].to_numpy()
x = list(range(data.shape[0]))
axs[0].scatter(x, data,s=2)
axs[0].set_title('GHISACONUS', fontsize=18)

lucas = pd.read_csv(r"D:\src\prehyp\data\indian_pines.csv")
data = lucas.iloc[100,0:-1].to_numpy()
x = list(range(data.shape[0]))
axs[1].scatter(x, data,s=2)
axs[1].set_title('Indian Pines', fontsize=18)

lucas = pd.read_csv(r"D:\Data\LUCAS\Lucas-2015\LUCAS2015_Soil_Spectra_EU28\spectra_ MT .csv")
data = lucas.iloc[2,5:].to_numpy()
data = 1/(10**data)
x = list(range(data.shape[0]))
axs[2].scatter(x, data,s=2)
axs[2].set_title('LUCAS', fontsize=18)

for ax in axs:
    ax.set_yticks([])
    ax.set_xlabel('Band Index', fontsize=15)
    ax.set_ylabel('Reflectance', fontsize=15)

plt.tight_layout()
plt.savefig("../saved_figs/fig2.png")



