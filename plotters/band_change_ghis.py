import pandas as pd
import matplotlib.pyplot as plt
import os

target_size = 10
file = f"../results/bsdr-ghisaconus-10-0-8.csv"
fig, ax = plt.subplots(1,1, figsize=(7, 5))
df = pd.read_csv(file)
band_labels = []
for i in range(1,target_size+1):
    band_labels.append(f"band_{i}")
columns = ["epoch"] + band_labels
df2 = df[columns].copy()
cols_to_increment = df2.columns.difference(['epoch'])
df2[cols_to_increment] = df2[cols_to_increment].add(1)
for i in range(1,target_size+1):
    ax.plot(df2["epoch"], df2[f"band_{i}"], label=f"Target Index {i}")
ax.set_xlabel('Epoch', fontsize=20)
ax.set_ylabel('Bands Index', fontsize=20)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_xlim(0, 500)
ax.set_ylim(1, 132)

ax.legend(loc='best', bbox_to_anchor=(1.05, 0.91), borderaxespad=0., fontsize=14)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.subplots_adjust(right=0.7)
plt.tight_layout()
plt.savefig("../saved_figs/bands/ghisaconus_10.png")
plt.clf()

