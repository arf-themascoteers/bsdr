import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = "../saved_figs"
df_original = pd.read_csv("../final_results/classification.csv")
priority_order = ['MCUVE', 'SPA', 'BS-Net-FC', 'Zhang et al.', 'BSDR', 'All Bands']
display_alg = ['MCUVE [21]', 'SPA [20]', 'BS-Net-FC [28]', 'BS-Net-Classifier [25]', 'BSDR', 'All Bands']
df_original['algorithm'] = pd.Categorical(df_original['algorithm'], categories=priority_order, ordered=True)
df_original = df_original.sort_values('algorithm')
colors = ['#909c86', '#e389b9', '#269658', '#5c1ad6', '#f20a21', '#000000']
markers = ['s', 'P', 'D', '^', 'o', '*', '.']
labels = ["Logarithmic Training Time","OA", "$\kappa$"]

datasets = ["GHISACONUS", "Indian Pines"]

for metric_index,metric in enumerate(["time"]):#, "metric1", "metric2"]):
    for ds_index, dataset in enumerate(datasets):

        dataset_df = df_original[df_original["dataset"] == dataset].copy()
        dataset_df["time"] = np.log10(dataset_df["time"].replace(0, 1))  # To avoid -inf for zero values
        #algorithms = dataset_df["algorithm"].unique()
        for index, algorithm in enumerate(priority_order):
            alg_df = dataset_df[dataset_df["algorithm"] == algorithm]
            alg_df = alg_df.sort_values(by='target_size')
            if algorithm == "All Bands":
                if metric == "time":
                    continue
                else:
                    ax.plot(alg_df['target_size'], alg_df[metric], label=algorithm,
                            linestyle='--', color=colors[index])
            else:
                ax.plot(alg_df['target_size'], alg_df[metric],
                        label=display_alg[index], marker=markers[index], color=colors[index],
                        fillstyle='none', markersize=10, linewidth=2
                        )

        ax.set_xlabel('Target size', fontsize=18)
        ax.set_ylabel(labels[metric_index], fontsize=18)
        ax.tick_params(axis='both', which='major', labelsize=14)
        if ds_index == len(datasets)-1:
            legend = ax.legend(title="Algorithms", loc='upper left', fontsize=18,bbox_to_anchor=(1.05, 1))
            legend.get_title().set_fontsize('18')
            legend.get_title().set_fontweight('bold')

        ax.grid(True, linestyle='--', alpha=0.6)

        fig.set_size_inches(10, 6)

        subfolder = os.path.join(root, "classification", metric)
        os.makedirs(subfolder, exist_ok=True)
        path = os.path.join(subfolder, f"{dataset}.png")
        plt.tight_layout()
        plt.savefig(path, dpi=300)
        plt.close(fig)

