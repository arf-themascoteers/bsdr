import pandas as pd

# for i in ["indian_pines", "ghsi", "lucas_min", "lucas_downsampled", "lucas_full"]:
#     df = pd.read_csv(f"data/{i}.csv")
#     print(i)
#     print("col", len(df.columns)-1)
#     print(len(df))
#     print("")
#     print("")

for i in ["ghsi"]:
    df = pd.read_csv(f"data/{i}.csv")
    print(df["crop"].unique())
