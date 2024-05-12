import pandas as pd
import matplotlib.pyplot as plt
import os

root = "../temp/4v_500"


fig, ax = plt.subplots(1, 2, figsize=(18, 10))
file = f"bsdr-lucas-5-0-0.csv"
loc = os.path.join(root, file)
df = pd.read_csv(loc)
band_labels = []
for i in range(1,5+1):
    band_labels.append(f"band_{i}")
columns = ["epoch","validation_r2","validation_rmse"] + band_labels
df2 = df[columns].copy()
cols_to_increment = df2.columns.difference(["epoch","validation_r2","validation_rmse"])
df2[cols_to_increment] = df2[cols_to_increment].add(1)

ax[0].set_xlabel('Epoch', fontsize=30)
ax[0].set_ylabel('Band Index', fontsize=30)
ax[0].tick_params(axis='both', which='major', labelsize=20)
ax[0].set_xlim(0, 500)
ax[0].set_ylim(1, 4201)
for i in range(1,6):
    ax[0].plot(df2["epoch"], df2[f"band_{i}"], label=f"Target Index {i}")
ax[0].legend(loc='upper right', ncol=2, bbox_to_anchor=(0.9, 1.25), fontsize=22)
    
ax[1].set_xlabel('Epoch', fontsize=30)
ax[1].set_ylabel('$R^2$', color='tab:blue', fontsize=30)
ax[1].tick_params(axis='both', which='major', labelsize=20)
ax[1].tick_params(axis='y', labelcolor='tab:blue')
ax[1].set_xlim(0, 500)
ax[1].plot(df["epoch"], df["validation_r2"], color='tab:blue')

ax2 = ax[1].twinx()
ax2.set_xlabel('Epoch', fontsize=30)
ax2.set_ylabel('RMSE', color='tab:red', fontsize=30)
ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_xlim(0, 500)
ax2.plot(df["epoch"], df["validation_rmse"], color='tab:red')

#     ax[0].legend(loc='upper right', ncol=5, bbox_to_anchor=(2.7, 1.3), fontsize=22)
#
#
# for ax in ax.flat:
# for spine in ax.spines.values():
#     spine.set_visible(False)
#
# subfolder = os.path.join("../saved_figs", "bands")
# if not os.path.exists(subfolder):
# os.mkdir(subfolder)
#
# path = os.path.join(subfolder, f"band_change.png")
# fig.subplots_adjust(wspace=0.5, hspace=0.5)
#plt.tight_layout()

for spine in ax[0].spines.values():
    spine.set_visible(False)
for spine in ax[1].spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

plt.tight_layout()
fig.subplots_adjust(wspace=0.4)
#plt.show()

plt.savefig("../saved_figs/bands/bc_reg.png")
plt.clf()

