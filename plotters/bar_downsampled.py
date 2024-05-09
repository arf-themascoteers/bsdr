import os.path
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def plot_bar():
    root = "../saved_figs"
    df_original = pd.read_csv(f"../final_results/regression.csv")
    df = df_original[df_original["algorithm"] != "All Bands"].copy()
    df['time'] = df['time'].apply(lambda x: np.log10(x+10))
    algorithms = ['BSDR', 'BS-Net-FC', 'MCUVE', 'PCAL', 'LASSO', 'SPA']
    df_lucas = df[(df["dataset"] == "LUCAS") & (df["target_size"] == 30)]
    df_short = df[(df["dataset"] == "LUCAS (Downsampled)") & (df["target_size"] == 30)]

    lucas_time = []
    short_time = []

    for a in algorithms:
        rows = df_lucas[df_lucas["algorithm"] == a]
        lucas_time.append(rows.iloc[0]["time"])

        rows = df_short[df_short["algorithm"] == a]
        short_time.append(rows.iloc[0]["time"])

    fig = go.Figure(data=[
        go.Bar(name='LUCAS (Downsampled)', x=algorithms, y=short_time),
        go.Bar(name='LUCAS', x=algorithms, y=lucas_time)
    ])

    fig.update_yaxes(showticklabels=False)

    fig.update_layout(
        barmode='group',
        xaxis_title='Algorithm',
        yaxis_title='Logarithmic execution time',
    )

    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'title_x': 0.5
    })

    subfolder = os.path.join(root, "bars")
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    path = os.path.join(subfolder,f"downsampled.png")
    fig.write_image(path, scale=5)



plot_bar()
