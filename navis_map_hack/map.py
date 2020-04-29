import plotly.graph_objects as go  # or plotly.express as px
from .data import get_data, get_customers, get_products
import pandas as pd


def get_customers_products():
    data = get_data()
    customers = get_customers(data)
    products = get_products(data)
    return customers, products


def get_figure():
    customers, products = get_customers_products()
    df = customers.merge(products, left_on="product", right_on="id", how="left")[
        ["long", "lat", "customer_name", "symbol"]
    ]
    fig = go.Figure(
        data=go.Scattergeo(
            lon=df["long"],
            lat=df["lat"],
            hovertext=df["customer_name"],
            text=df["symbol"],
            mode="text",
        )
    )

    return fig
