import pandas as pd
import matplotlib.pyplot as plt
import os

root = "../temp/4v_500"
datasets = {
    "lucas": 4200
}

for dataset in datasets.keys():
    for target_size in [5, 10, 15, 20, 25, 30]:
        file = f"bsdr-{dataset}-{target_size}-0-0.csv"
        loc = os.path.join(root, file)
        if not os.path.exists(loc):
            continue
        fig, ax = plt.subplots(1,1, figsize=(7, 5))
        df = pd.read_csv(loc)
        band_labels = []
        for i in range(1,target_size+1):
            band_labels.append(f"band_{i}")
        columns = ["epoch"] + band_labels
        df2 = df[columns].copy()
        cols_to_increment = df2.columns.difference(['epoch'])
        df2[cols_to_increment] = df2[cols_to_increment].add(1)
        for i in range(1,target_size+1):
            ax.plot(df2["epoch"], df2[f"band_{i}"], label=f"Band Index {i}")
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Band Index')
        ax.set_xlim(0, 500)
        ax.set_ylim(1, datasets[dataset]+1)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        #pos = ax.get_position()
        #ax.set_position([pos.x0, pos.y0, pos.width * 0.5, pos.height])
        #ax.legend(loc='center right', bbox_to_anchor=(1.65, 0.8))
        ax.legend(loc='upper right')#, bbox_to_anchor=(-0.8, 1), borderaxespad=1.)
        subfolder = os.path.join("../saved_figs", "bands")
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)
        path = os.path.join(subfolder, f"{dataset}_{target_size}.png")
        plt.savefig(path)
        plt.clf()

