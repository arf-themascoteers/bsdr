import pandas as pd
import matplotlib.pyplot as plt
import os

root = "../temp/4v_500"
datasets = {
    "ghisaconus": 131,
    "indian_pines": 200
}
dataset_names = ["GHISACONUS","Indian Pines"]
res = {
    "ghisaconus": ["0-0","0-8","0-5"],
    "indian_pines": ["0-9","0-9","0-0"],
}

def get_min_max_lims():
    file = f"bsdr-ghisaconus-5-0-0.csv"
    df = pd.read_csv(os.path.join(root, file))
    min_lim = min(df["validation_accuracy"].min(),df["validation_kappa"].min())
    max_lim = min(df["validation_accuracy"].max(),df["validation_kappa"].max())

    file = f"bsdr-indian_pines-5-0-0.csv"
    pd.read_csv(os.path.join(root, file))
    min_lim = min(df["validation_accuracy"].min(),df["validation_kappa"].min(), min_lim)
    max_lim = min(df["validation_accuracy"].max(),df["validation_kappa"].max(), max_lim)

    return min_lim, max_lim

min_lim, max_lim = get_min_max_lims()

fig, ax = plt.subplots(1, 2, figsize=(20, 6))
for ds_index, dataset in enumerate(datasets.keys()):
    file = f"bsdr-{dataset}-5-0-0.csv"
    loc = os.path.join(root, file)
    df = pd.read_csv(loc)
    band_labels = []
    for i in range(1,5+1):
        band_labels.append(f"band_{i}")
    columns = ["epoch","validation_accuracy","validation_kappa"] + band_labels
    df2 = df[columns].copy()
    cols_to_increment = df2.columns.difference(["epoch","validation_accuracy","validation_kappa"])
    df2[cols_to_increment] = df2[cols_to_increment].add(1)

    ax[ds_index].set_xlabel('Epoch', fontsize=22)
    ax[ds_index].set_ylabel('Band Index', fontsize=22)
    ax[ds_index].tick_params(axis='both', which='major', labelsize=20)
    ax[ds_index].set_xlim(0, 500)
    ax[ds_index].set_ylim(1, datasets[dataset]+1)
    for i in range(1,6):
        ax[ds_index].plot(df2["epoch"], df2[f"band_{i}"], label=f"Target Index {i}")
    ax[ds_index].set_title(dataset_names[ds_index], fontsize=25)
    ax[ds_index].grid(True, which='both', linestyle='--', linewidth=0.5)

    if ds_index == 0:
        ax[ds_index].legend(loc='upper right', ncol=5, bbox_to_anchor=(2.5, 1.55), fontsize=20)


# for ax in ax.flat:
#     for spine in ax.spines.values():
#         spine.set_visible(False)

subfolder = os.path.join("../saved_figs", "bands")
if not os.path.exists(subfolder):
    os.mkdir(subfolder)

path = os.path.join(subfolder, f"band_change1.png")
fig.subplots_adjust(wspace=0.5, hspace=0.5)
fig.subplots_adjust(top=0.7)
fig.subplots_adjust(bottom=0.3)
plt.savefig(path)
plt.clf()

