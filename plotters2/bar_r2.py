import os.path
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def plot_bar():
    root = "../saved_figs"
    df_original = pd.read_csv(f"../final_results/regression.csv")
    df = df_original[df_original["algorithm"] != "All Bands"].copy()
    algorithms = ['BSDR', 'BS-Net-FC', 'MCUVE', 'PCAL', 'LASSO', 'SPA']
    df_lucas = df[(df["dataset"] == "LUCAS") & (df["target_size"] == 5)]
    df_short = df[(df["dataset"] == "LUCAS (Truncated)") & (df["target_size"] == 5)]

    lucas_time = []
    short_time = []

    for a in algorithms:
        rows = df_lucas[df_lucas["algorithm"] == a]
        lucas_time.append(rows.iloc[0]["metric1"])

        rows = df_short[df_short["algorithm"] == a]
        short_time.append(rows.iloc[0]["metric1"])

    fig = go.Figure(data=[
        go.Bar(name='LUCAS (Truncated)', x=algorithms, y=short_time),
        go.Bar(name='LUCAS', x=algorithms, y=lucas_time)
    ])

    #fig.update_yaxes(showticklabels=False)

    fig.update_layout(
        barmode='group',
        xaxis_title='Algorithm',
        yaxis_title='$R^2$',
    )

    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'title_x': 0.5
    })

    subfolder = os.path.join(root, "bars")
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    path = os.path.join(subfolder,f"r2.png")
    fig.write_image(path, scale=5)



plot_bar()
