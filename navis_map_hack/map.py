import plotly.graph_objects as go  # or plotly.express as px
from .data import get_data
import pandas as pd


def get_figure():
    df = get_data()
    fig = go.Figure(
        data=go.Scattergeo(
            lon=df["long"],
            lat=df["lat"],
            text=df["customer_name"],
            mode="markers",
            marker_size=10,
        )
    )
    return fig
