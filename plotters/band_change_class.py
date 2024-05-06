import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

#root = "../saved_results/0_1"
#locs = [os.path.join(root, sub) for sub in os.listdir(root) if sub.startswith("bsdr-lucas_full-5-")]
#idx = 10
locs = ["../saved_results/0_5/fscrl-ghsi-5-171449809410246.csv", "../saved_results/0_5/fscrl-indian_pines-5-1714482682207401.csv"]
bands = [131,200]
for index,loc in enumerate(locs):
    df = pd.read_csv(loc)
    band_labels = []
    for i in range(1,6):
        band_labels.append(f"band_{i}")
    band_labels = ["epoch"] + band_labels
    df = df[band_labels]
    limit = 8000
    df = df[df["epoch"]<limit]
    fig = go.Figure()


    for i in range(1,6):
        additional_trace = go.Scatter(x=df["epoch"], y=df[f"band_{i}"], mode='lines', name=f'Band Index {i}')
        fig.add_trace(additional_trace)

    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'title_x': 0.5,

    })
    fig.update_layout(yaxis_title="Band Index")
    fig.update_layout(xaxis_title="Epoch")
    fig.update_layout(
        xaxis=dict(range=[0, 4000]),  # Setting x-axis limits
        yaxis=dict(range=[0, bands[index]-1])  # Setting y-axis limits
    )
    subfolder = os.path.join("../saved_figs", "bands")
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    path = os.path.join(subfolder, f"classification_{index}.png")

    fig.write_image(path, scale=5)
