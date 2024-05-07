import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

#root = "../saved_results/0_1"
#locs = [os.path.join(root, sub) for sub in os.listdir(root) if sub.startswith("bsdr-lucas_full-5-")]
#idx = 10
locs = ["../saved_results/0_5/fscrl-ghisa-5-171449809410246.csv", "../saved_results/0_5/fscrl-indian_pines-5-1714482682207401.csv"]
for index,loc in enumerate(locs):
    df = pd.read_csv(loc)
    df = df[["epoch","validation_accuracy","validation_kappa"]]
    limit = 8000
    df = df[df["epoch"]<limit]
    fig = go.Figure()


    additional_trace = go.Scatter(x=df["epoch"], y=df[f"validation_accuracy"], mode='lines', name=f'OA')
    fig.add_trace(additional_trace)
    additional_trace = go.Scatter(x=df["epoch"], y=df[f"validation_kappa"], mode='lines', name=f"$\kappa$")
    fig.add_trace(additional_trace)

    fig.update_layout({
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'title_x': 0.5
    })

    fig.update_layout(xaxis_title="Epoch")
    fig.update_layout(
        xaxis=dict(range=[0, 4000]),  # Setting x-axis limits
        yaxis=dict(range=[0, 1])  # Setting y-axis limits
    )

    fig.update_layout(yaxis_title="")
    subfolder = os.path.join("../saved_figs", "bands")
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    path = os.path.join(subfolder, f"classification_r2_rmse_{index}.png")

    fig.write_image(path, scale=5)

