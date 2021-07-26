import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from ddok_plot_list import generation_list, month_list

basic_content = html.Div([
    html.Div([
        dcc.Markdown(
            """
            ## 기본 승수머신
            그래프를 드래그하면 확대됨 더블 클릭하면 원래대로 돌아옴\n
            모바일에서는 확대될 경우 두번 탭하면 원상복귀됨

            """
        ),
        html.P([html.Small("추가아이디어 있으면 제공 바람!"),
        #html.A(html.Small("twitter"), href="https://twitter.com/_jphwang", title="twitter"),
        html.Small("!")]),
    ]),
    html.Hr(),
    html.Div([
    dcc.Markdown(
    """
    \n\n
    ### 글 데이터
    월 별로 글자 수를 세서 등수를 매겼습니다.
    아래 드롭다운 값을 통해, 월별 기수별로 데이터 확인이 가능합니다.\n
    마우스를 올리면 정확한 수치 확인 가능
    """
    )
    ]),
    
    html.Div([
        html.Label(["기수 : "], style = {'display':'inline-block'}),
        dcc.Dropdown(
            id='generation-select',
            options=[{'label': x, 'value': x} for x in generation_list],
            value='all',
            style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
        ),
        html.Label(["월 : "], style = {'display':'inline-block'}),
        dcc.Dropdown(
            id='month-select',
            options=[{'label': x, 'value': x} for x in month_list],
            value='all',
            style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
        )

    ]),
    dbc.Card([
    dcc.Graph(
        id = 'post-word-plot',
        config={'displayModeBar': False}, style ={'margin':'15px'}
        
    )
    ])
    ,

    html.Hr(),
        html.Div([
        dcc.Markdown(
        """
        ### 댓글 데이터
        월 별로 댓글 개수, 댓글 글자 수를 세서 등수를 매겼습니다.
        아래 드롭다운 값을 통해, 월별 기수별로 데이터 확인이 가능합니다.\n
        마우스를 올리면 정확한 수치 확인 가능
        """
        )
        ]),
        html.Div([
            html.Label(["기수 : "], style = {'display':'inline-block'}),
            dcc.Dropdown(
                id='generation2-select',
                options=[{'label': x, 'value': x} for x in generation_list],
                value='all',
                style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
            ),
            html.Label(["월 : "], style = {'display':'inline-block'}),
            dcc.Dropdown(
                id='month2-select',
                options=[{'label': x, 'value': x} for x in month_list],
                value='all',
                style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
            )

        ]),
        dbc.Card([
        dcc.Graph(
            id = 'comment-plot',
            config={'displayModeBar': False}, style ={'margin':'15px'}
        )
        ])
])
