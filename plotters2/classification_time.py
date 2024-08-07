import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = "../saved_figs"
df_original = pd.read_csv("../final_results/classification.csv")
priority_order = ['MCUVE', 'SPA', 'BS-Net-FC', 'Zhang et al.', 'BSDR', 'All Bands']
display_alg = ['MCUVE', 'SPA', 'BS-Net-FC', 'BS-Net-Classifier', 'Proposed Algorithm', 'All Bands']
df_original['algorithm'] = pd.Categorical(df_original['algorithm'], categories=priority_order, ordered=True)
df_original = df_original.sort_values('algorithm')
df_original = df_original[df_original["target_size"]<30]
colors = ['#909c86', '#e389b9', '#269658', '#5c1ad6', '#f20a21', '#000000']
markers = ['s', 'P', 'D', '^', 'o', '*', '.']
labels = ["Logarithmic Training Time","OA", r"$\kappa$"]
# df_original["time"] = np.log10(df_original["time"].replace(0, 1))  # To avoid -inf for zero values
# min_time = df_original["time"].min()-0.1
# max_time = df_original["time"].max()+0.1
datasets = ["GHISACONUS", "Indian Pines"]

for metric_index,metric in enumerate(["time"]):#, "metric1", "metric2"]):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    for ds_index, dataset in enumerate(datasets):
        dataset_df = df_original[df_original["dataset"] == dataset].copy()

        #algorithms = dataset_df["algorithm"].unique()
        for index, algorithm in enumerate(priority_order):
            alg_df = dataset_df[dataset_df["algorithm"] == algorithm]
            alg_df = alg_df.sort_values(by='target_size')

            lw = 3
            if algorithm == "BSDR":
                lw = 5

            if algorithm == "All Bands":
                if metric == "time":
                    continue
                else:
                    axes[ds_index].plot(alg_df['target_size'], alg_df[metric], label=algorithm,
                            linestyle='--', color=colors[index])
            else:
                axes[ds_index].plot(alg_df['target_size'], alg_df[metric],
                        label=display_alg[index], marker=markers[index], color=colors[index],
                        fillstyle='none', markersize=10, linewidth=lw
                        )

        axes[ds_index].set_xlabel('Target size', fontsize=18)
        axes[ds_index].set_ylabel(labels[metric_index], fontsize=18)
#        axes[ds_index].set_ylim(min_time, max_time)
        axes[ds_index].tick_params(axis='both', which='major', labelsize=14)
        axes[ds_index].set_yscale('log')
        if ds_index == len(datasets)-1:
            legend = axes[ds_index].legend(title="Algorithms", loc='upper left', fontsize=18,bbox_to_anchor=(1.05, 1))
            legend.get_title().set_fontsize('18')
            legend.get_title().set_fontweight('bold')

        axes[ds_index].grid(True, linestyle='--', alpha=0.6)
        axes[ds_index].set_title(f"{dataset}", fontsize=22, pad=20)

    subfolder = os.path.join(root, "classification")
    os.makedirs(subfolder, exist_ok=True)
    path = os.path.join(subfolder, f"time.png")
    plt.tight_layout()
    fig.subplots_adjust(wspace=0.5)
    plt.savefig(path)
    plt.close(fig)

