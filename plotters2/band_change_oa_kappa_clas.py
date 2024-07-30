import pandas as pd
import os
import matplotlib.pyplot as plt

for dataset in ["ghisaconus","indian_pines"]:
    locs = [f"../temp/4v_500/bsdr-{dataset}-5-0-0.csv"]
    for index,loc in enumerate(locs):
        df = pd.read_csv(loc)
        df = df[["epoch","validation_accuracy","validation_kappa"]]

        fig, ax1 = plt.subplots(1, 1, figsize=(10, 6))

        ax1.set_xlabel('Epoch', fontsize=25)
        ax1.set_ylabel('$R^2$', fontsize=25)
        ax1.tick_params(axis='both', which='major', labelsize=20)
        ax1.plot(df["epoch"], df["validation_accuracy"], label="OA")
        ax1.plot(df["epoch"], df["validation_kappa"], label = "$\kappa$")
        ax1.legend(loc='lower right',fontsize=25)
        for spine in ax1.spines.values():
            spine.set_visible(False)

        for spine in ax1.spines.values():
            spine.set_visible(False)

        subfolder = os.path.join("../saved_figs", "bands")
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)
        path = os.path.join(subfolder, f"{dataset}_accuracy_kappa.png")
        plt.tight_layout()

        plt.savefig(path)

