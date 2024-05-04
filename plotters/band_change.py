import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

root = "../saved/0_1"
locs = [os.path.join(root, sub) for sub in os.listdir(root) if sub.startswith("fscrl-lucas_full-5-")]
idx = 10
loc = "../saved/0_1/fscrl-lucas_full-5-1714512143422615.csv"
df = pd.read_csv(loc)
band_labels = []
for i in range(1,6):
    band_labels.append(f"band_{i}")
band_labels = ["epoch"] + band_labels
df = df[band_labels]
limit = 4000
df = df[df["epoch"]<4000]
fig = go.Figure()


for i in range(1,6):
    additional_trace = go.Scatter(x=df["epoch"], y=df[f"band_{i}"], mode='lines', name=f'Band Index {i}')
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
path = os.path.join(subfolder, f"{idx}.png")

fig.write_image(path, scale=5)

