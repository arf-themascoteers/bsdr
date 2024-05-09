import os.path
import numpy as np
import pandas as pd
import plotters.utils as utils
import plotly.graph_objects as go

root = "../saved_figs"


df_original = pd.read_csv("../final_results/regression.csv")
priority_order = ['PCA-loading', 'LASSO', 'MCUVE',
                  'SPA',
                  'BS-Net-FC', 'BSDR','All Bands']
df_original['algorithm'] = pd.Categorical(df_original['algorithm'], categories=priority_order, ordered=True)
df_original = df_original.sort_values('algorithm')
colors = ['#636EFA','#19D3F3' , '#00CC96',
          '#AB63FA',
          '#FFA15A', '#EF553B', '#000000']
markers = ['star-open', 'pentagon-open', 'circle-open', 'hash-open', 'triangle-up-open', 'square-open', None]

for metric in ["time","metric1", "metric2"]:
    for dataset in ["LUCAS"]:
        fig = go.Figure()
        dataset_df = df_original[df_original["dataset"] == dataset].copy()
        dataset_df["time"] = dataset_df["time"].apply(lambda x: np.log10(x) if x != 0 else 0)
        algorithms = dataset_df["algorithm"].unique()
        for index, algorithm in enumerate(algorithms):
            alg_df = dataset_df[dataset_df["algorithm"] == algorithm]
            alg_df = alg_df.sort_values(by='target_size')
            line = dict()
            mode = 'lines+markers'
            if algorithm == "All Bands":
                if metric == "time":
                    continue
                else:
                    line["dash"] = "dash"
                    mode = 'lines'
            # elif algorithm == "BSDR":
            #     line["width"] = 3
            fig.add_trace(
                go.Scatter(
                    x=alg_df['target_size'],
                    y=alg_df[metric], mode=mode,
                    name=algorithm, marker=dict(color=colors[index], symbol=markers[index], size=10),
                    line=line
                )
            )

        fig.update_layout({
            'plot_bgcolor': 'white',
            'paper_bgcolor': 'white',
            'title_x':0.5
        })

        fig.update_layout(
            xaxis=dict(
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1
            )
        )

        fig.update_layout(
            #title='Performance Metrics by Algorithm and Dataset',
            xaxis_title="Target size",
            yaxis_title=utils.metric_map[metric][dataset],
            legend_title="Algorithm"
        )

        fig.update_layout(
            font=dict(size=17),
        )
        subfolder = os.path.join(root, "regression")
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)
        subfolder = os.path.join(subfolder, metric)
        if not os.path.exists(subfolder):
            os.mkdir(subfolder)
        path = os.path.join(subfolder, f"{dataset}.png")
        fig.write_image(path, scale=5)




