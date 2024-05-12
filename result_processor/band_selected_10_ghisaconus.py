import pandas as pd


def create_latex():
    df = pd.read_csv("../temp/4v_500/details_4v_500.csv")
    df = df[ (df["target_size"] == 10) & (df["dataset"] == "ghisaconus") ]

    for fold in range(10):
        fold_df = df[df["fold"] == fold]

        g_bands = ", ".join(fold_df["selected_features"].values[0].split("-"))

        print(f"{fold+1} & {g_bands}  \\\\")


create_latex()