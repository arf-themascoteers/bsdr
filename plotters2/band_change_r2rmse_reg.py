import pandas as pd
import os
import matplotlib.pyplot as plt

locs = ["../temp/4v_500/bsdr-lucas-5-0-0.csv"]
for index,loc in enumerate(locs):
    df = pd.read_csv(loc)
    df = df[["epoch","validation_r2","validation_rmse"]]

    fig, ax1 = plt.subplots(1, 1, figsize=(7, 5))

    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('$R^2$', color='tab:blue')
    ax1.plot(df["epoch"], df["validation_r2"], color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('RMSE', color='tab:red')
    ax2.plot(df["epoch"], df["validation_rmse"], color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    for spine in ax2.spines.values():
        spine.set_visible(False)

    for spine in ax1.spines.values():
        spine.set_visible(False)

    subfolder = os.path.join("../saved_figs", "bands")
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    path = os.path.join(subfolder, f"LUCAS_r2_rmse.png")


    plt.savefig(path)

