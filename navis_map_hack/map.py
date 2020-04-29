import plotly.graph_objects as go  # or plotly.express as px

import pandas as pd

df = pd.DataFrame(
    {
        "lat": [19.734671, 30.673855, 39.099724, -41.429825],
        "long": [-72.198525, -81.463496, -94.578331, 147.157135],
        "text": [
            "Cap Terminal",
            "Worldwide Terminals Fernandina",
            "Kansas City Southern",
            "TasRail",
        ],
        "cnt": ["purple", "purple", "red", "red"],
    }
)
fig = go.Figure(
    data=go.Scattergeo(
        lon=df["long"],
        lat=df["lat"],
        text=df["text"],
        mode="markers",
        marker_color=df["cnt"],
        marker_size=10,
    )
)
fig.show()  # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )
