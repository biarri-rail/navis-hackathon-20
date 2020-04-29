import dash
import dash_core_components as dcc
import dash_html_components as html
from .map import get_figure


def get_app():
    app = dash.Dash()
    app.layout = html.Div([dcc.Graph(figure=get_figure())])
    return app
