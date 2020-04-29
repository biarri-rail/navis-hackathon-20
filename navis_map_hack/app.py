import dash
import dash_core_components as dcc
import dash_html_components as html
from .map import get_figure

def get_layout():
    return html.Div(
        [
            html.Div(dcc.Graph(figure=get_figure(),responsive=True, style={"height": "100vh"}), style=dict(flex="5 0 auto") ),
            html.Iframe(
                className="airtable-embed",
                src="https://airtable.com/embed/shrDk5hLlMiSU0lqo?backgroundColor=purple",
                style=dict(
                    border="1px solid #ccc",
                    background="background: transparent",
                    maxWidth="20rem",
                ),
                width="100%",
                height="533",
            )
        ],
        style=dict(display="flex"),
    )

def get_app():
    app = dash.Dash()
    app.layout = get_layout
    return app
