import pandas as pd
import pywt

lucas = pd.read_csv("../data/lucas/reflectance.csv")

bands = list(lucas.columns)
bands = bands[13:]
all_columns = ["oc"]+bands
lucas_full = lucas[all_columns]
lucas_full.to_csv("data/lucas_full.csv", index=False)

lucas_full = pd.read_csv("../data/lucas_full.csv")

lucas_min = lucas_full.sample(frac=0.04, random_state=40)
lucas_min.to_csv("data/lucas_min.csv", index=False)

lucas_min = pd.read_csv("data/lucas_min.csv")

reduced_columns = ["oc"] + [str(i) for i in range(66)]
lucas_down = pd.DataFrame(columns=reduced_columns)
for index, row in lucas_full.iterrows():
    signal = row.iloc[1:]
    short_signal, _, _, _, _, _, _ = pywt.wavedec(signal, 'db1', level=6)
    lucas_down.loc[len(lucas_down)] = [row.iloc[0]] + list(short_signal)
lucas_down.to_csv(f"data/lucas_downsampled.csv", index=False)

lucas_down_min = pd.DataFrame(columns=reduced_columns)
for index, row in lucas_min.iterrows():
    signal = row.iloc[1:]
    short_signal, _, _, _, _, _, _ = pywt.wavedec(signal, 'db1', level=6)
    lucas_down_min.loc[len(lucas_down_min)] = [row.iloc[0]] + list(short_signal)
lucas_down_min.to_csv(f"data/lucas_downsampled_min.csv", index=False)

selected_indices = list(range(1,4201,64))
lucas_skipped = pd.DataFrame(columns=reduced_columns)
for index, row in lucas_full.iterrows():
    signal = row.iloc[selected_indices]
    lucas_skipped.loc[len(lucas_skipped)] = [row.iloc[0]] + list(signal)
lucas_skipped.to_csv(f"data/lucas_skipped.csv", index=False)

lucas_skipped_min = pd.DataFrame(columns=reduced_columns)
for index, row in lucas_min.iterrows():
    signal = row.iloc[selected_indices]
    lucas_skipped_min.loc[len(lucas_skipped_min)] = [row.iloc[0]] + list(signal)
lucas_skipped_min.to_csv(f"data/lucas_skipped_min.csv", index=False)

print("Done all")