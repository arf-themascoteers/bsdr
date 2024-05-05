import pandas as pd
import plotly.express as px

df = pd.read_csv("b22.csv")

fig = px.scatter(df, x='band1', y='band2',
                    color='score',
                    color_continuous_scale='ylgnbu',
                    labels={"band1": "Band Index 1", "band2": "Band Index 2", "score": "Score"}
                    )

fig.update_layout({
    'plot_bgcolor': 'white',
    'paper_bgcolor': 'white',
    'title_x': 0.5
})

fig.update_layout(
    font=dict(size=22),

)


fig.write_image("fig1.png", scale=5)