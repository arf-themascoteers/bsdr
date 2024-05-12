import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = "../saved_figs"
df_original = pd.read_csv("../final_results/regression.csv")
priority_order = ['MCUVE', 'SPA', 'BS-Net-FC', 'BSDR', 'All Bands']
display_alg = ['MCUVE [21]', 'SPA [20]', 'BS-Net-FC [28]', 'BSDR', 'All Bands']
df_original['algorithm'] = pd.Categorical(df_original['algorithm'], categories=priority_order, ordered=True)
df_original = df_original.sort_values('algorithm')
colors = ['#909c86', '#e389b9', '#269658', '#f20a21', '#000000']
markers = ['s', 'P', 'D', 'o', '*', '.']
labels = ["$R^2$", "RMSE"]
min_r2_lim = df_original["metric1"].min() -0.1
max_r2_lim = df_original["metric1"].max() +0.1
min_rmse_lim = df_original["metric2"].min() -1
max_rmse_lim = df_original["metric2"].max() +1

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
axes[0].set_ylim(min_r2_lim, max_r2_lim)
axes[1].set_ylim(min_rmse_lim, max_rmse_lim)
for metric_index,metric in enumerate(["metric1", "metric2"]):
    dataset_df = df_original[df_original["dataset"] == "LUCAS"].copy()
    for index, algorithm in enumerate(priority_order):
        alg_df = dataset_df[dataset_df["algorithm"] == algorithm]
        alg_df = alg_df.sort_values(by='target_size')
        if algorithm == "All Bands":
            axes[metric_index].plot(alg_df['target_size'], alg_df[metric], label=algorithm,
                    linestyle='--', color=colors[index])
        else:
            axes[metric_index].plot(alg_df['target_size'], alg_df[metric],
                    label=display_alg[index], marker=markers[index], color=colors[index],
                    fillstyle='none', markersize=10, linewidth=2
                    )

    axes[metric_index].set_xlabel('Target size', fontsize=18)
    axes[metric_index].set_ylabel(labels[metric_index], fontsize=18)
    axes[metric_index].tick_params(axis='both', which='major', labelsize=14)
    if metric_index == 1:
        legend = axes[metric_index].legend(title="Algorithms", loc='upper left', fontsize=18,bbox_to_anchor=(1.05, 1))
        legend.get_title().set_fontsize('18')
        legend.get_title().set_fontweight('bold')

    axes[metric_index].grid(True, linestyle='--', alpha=0.6)
    #if metric_index == 0:
        #axes[metric_index].set_title(f"LUCAS dataset", fontsize=22, pad=20)

subfolder = os.path.join(root, "regression")
os.makedirs(subfolder, exist_ok=True)
path = os.path.join(subfolder, f"r2rm.png")
plt.tight_layout()
fig.subplots_adjust(wspace=0.5)
plt.savefig(path)
plt.close(fig)

