import pandas as pd
import numpy as np

df = pd.read_csv("../final_results/details.csv")

algorithms = df["algorithm"].unique()

r2_df = pd.DataFrame(columns=["algorithm", "r2_5", "r2_10", "r2_15", "r2_15", "r2_20", "r2_25", "r2_30"])
rmse_df = pd.DataFrame(columns=["algorithm", "rmse_5", "rmse_10", "rmse_15", "rmse_15", "rmse_20", "rmse_25", "rmse_30"])
time_df = pd.DataFrame(columns=["algorithm", "time_5", "time_10", "time_15", "time_15", "time_20", "time_25", "time_30"])

for algorithm in algorithms:
    if algorithm == "All Bands":
        continue
    print(algorithm)
    df2 = df[(df["algorithm"] == algorithm)&(df["dataset"] == "LUCAS")]
    if len(df) == 0:
        continue

    time_strs = []
    r2_strs = []
    rmse_strs = []

    for target_size in [5, 10, 15, 20, 25, 30]:
        df3 = df2[df2["target_size"] == target_size]
        if len(df3) == 0:
            continue

        time_mean = df3["time"].mean()
        r2_mean = df3["metric1"].mean()
        rmse_mean = df3["metric2"].mean()

        time_std = df3["time"].std()
        r2_std = df3["metric1"].std()
        rmse_std = df3["metric2"].std()

        time_str = f"{time_mean:.2f}±{time_std:.2f}"
        r2_str = f"{r2_mean:.2f}±{r2_std:.2f}"
        rmse_str = f"{r2_mean:.2f}±{r2_std:.2f}"


