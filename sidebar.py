import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("승수머신 웹", className="display-4"),
        html.Hr(),
        html.P(
            "메뉴", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("승수머신 basic", href="/", active="exact",
                style={'display': 'block','text-decoration-line':'underline','color':'black','font-size':'20px', 'width':'150px','margin':'2px'}),
                dbc.NavLink("똑집 단어구름", href="/word_cloud", active="exact",
                style={'display': 'block','text-decoration-line':'underline','color':'black','font-size':'20px', 'width':'150px','margin':'2px'}),
                dbc.NavLink("???", href="/page-2", active="exact",
                style={'display': 'block','text-decoration-line':'underline','color':'black','font-size':'20px', 'width':'150px','margin':'2px'}),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
