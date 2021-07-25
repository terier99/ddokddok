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
            ## 똑똑집단 데이터 결산
            4~9기 데이터 활용하였습니다.\n
            3기 밴드 관리자분 계시면 연락주세요.

            """
        ),
        html.P([html.Small("추가아이디어 있으면 제공 바람!"),
        #html.A(html.Small("twitter"), href="https://twitter.com/_jphwang", title="twitter"),
        html.Small("!")]),
    ]),
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
        dcc.Dropdown(
            id='generation-select',
            options=[{'label': x, 'value': x} for x in generation_list],
            value='all',
            style={'width': '140px','display': 'inline-block'}
        ),
        dcc.Dropdown(
            id='month-select',
            options=[{'label': x, 'value': x} for x in month_list],
            value='all',
            style={'width': '140px','display': 'inline-block'}
        )

    ]),
    dcc.Graph(
        id = 'post-word-plot',
        config={'displayModeBar': False}
    ),
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
            dcc.Dropdown(
                id='generation2-select',
                options=[{'label': x, 'value': x} for x in generation_list],
                value='all',
                style={'width': '140px','display': 'inline-block'}
            ),
            dcc.Dropdown(
                id='month2-select',
                options=[{'label': x, 'value': x} for x in month_list],
                value='all',
                style={'width': '140px','display': 'inline-block'}
            )

        ]),
        dcc.Graph(
            id = 'comment-plot',
            config={'displayModeBar': False}
        )
])
