import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

root = "../saved_results/0_1"
locs = [os.path.join(root, sub) for sub in os.listdir(root) if sub.startswith("bsdr-lucas_full-5-")]
idx = 10
loc = "../saved_results/0_1/fscrl-lucas_full-5-1714510927050816.csv"
df = pd.read_csv(loc)
df = df[["epoch","validation_r2"]]
limit = 8000
df = df[df["epoch"]<limit]
fig = go.Figure()


additional_trace = go.Scatter(x=df["epoch"], y=df[f"validation_r2"], mode='lines', name=f'$R^2')
fig.add_trace(additional_trace)

fig.update_layout({
    'plot_bgcolor': 'white',
    'paper_bgcolor': 'white',
    'title_x': 0.5
})
fig.update_layout(yaxis_title="")
subfolder = os.path.join("../saved_figs", "bands")
if not os.path.exists(subfolder):
    os.mkdir(subfolder)
path = os.path.join(subfolder, f"r2_{idx}.png")

fig.write_image(path, scale=5)

