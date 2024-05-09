import pandas as pd
import matplotlib.pyplot as plt
import os

root = "../4v_500"
datasets = {
    "ghisaconus": 131,
    "indian_pines": 200
}

res = {
    "ghisaconus": ["0-0","0-8","0-5"],
    "indian_pines": ["0-0","0-0","0-0"],
}


for dataset in datasets.keys():
    fig, axs = plt.subplots(3, 2, figsize=(10, 12))
    for target_index, target_size in enumerate([5, 10, 15]):
        file = f"bsdr-{dataset}-{target_size}-{res[dataset][target_index]}.csv"
        loc = os.path.join(root, file)
        if not os.path.exists(loc):
            continue

        df = pd.read_csv(loc)
        band_labels = []
        for i in range(1,target_size+1):
            band_labels.append(f"band_{i}")
        columns = ["epoch","validation_accuracy","validation_kappa"] + band_labels
        df2 = df[columns].copy()
        cols_to_increment = df2.columns.difference(['epoch',"validation_accuracy","validation_kappa"])
        df2[cols_to_increment] = df2[cols_to_increment].add(1)
        for i in range(1,target_size+1):
            axs[target_index, 0].plot(df2["epoch"], df2[f"band_{i}"], label=f"Band Index {i}")
            axs[target_index, 0].set_xlim(0, 500)
            axs[target_index, 0].set_ylim(1, datasets[dataset])
            axs[target_index, 0].set_xlabel('Epoch')
            axs[target_index, 0].set_ylabel('Band Index')
            axs[target_index, 0].legend(loc='upper left', bbox_to_anchor=(-0.8, 1), borderaxespad=1.)


        axs[target_index, 1].plot(df2["epoch"], df2[f"validation_accuracy"], label=f"OA")
        axs[target_index, 1].plot(df2["epoch"], df2[f"validation_kappa"], label=f"$\kappa$")
        axs[target_index, 1].set_xlim(0, 500)
        axs[target_index, 1].set_ylim(0,1)
        axs[target_index, 1].set_xlabel('Epoch')
        axs[target_index, 1].legend(loc='lower right')
        #axs[target_index, 1].set_ylabel('Band Index')
        #axs[target_index, 1].legend(loc='upper right', bbox_to_anchor=(-0.8, 0.9), borderaxespad=1.)

    #ax.set_xlabel('Epoch')
    #ax.set_ylabel('Band Index')
    #ax.set_xlim(0, 1000)
    #ax.set_ylim(1, datasets[dataset])
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    for ax in axs.flatten():
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

    #pos = ax.get_position()
    #ax.set_position([pos.x0, pos.y0, pos.width * 0.5, pos.height])
    #ax.legend(loc='center right', bbox_to_anchor=(1.65, 0.8))
    plt.tight_layout()
    subfolder = os.path.join("../saved_figs", "bands")
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    path = os.path.join(subfolder, f"{dataset}.png")
    plt.savefig(path)
    plt.clf()


