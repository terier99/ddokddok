from wordcloud import WordCloud

from collections import Counter

import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


post_df = pd.read_csv('band_writings_list.csv')
comment_df = pd.read_csv('band_comment_list.csv')
generation_list =  ['all'] + list(post_df['기수'].drop_duplicates().sort_values())
month_list = ['all'] + list(post_df['달'].drop_duplicates().sort_values())
name_list = ['all'] + list(post_df['이름'].drop_duplicates())

def post_word_df(generation = 'all', month = 'all', name = ''):
    df =pd.read_csv('band_writings_list.csv')
    df =df.loc[(df['processed'].isna() == False) & (df['processed'] != '')]
    if not generation == 'all':
        df = df.loc[df['기수'] == generation]
    if not month == 'all':
        df = df.loc[df['달'] == month]
    if not name.strip() == '':
        df = df.loc[df['이름'] == name]
    return df

def comment_word_df(generation = 'all', month = 'all', name = ''):
    df = pd.read_csv('band_comment_list.csv')
    df =df.loc[(df['processed'].isna() == False) & (df['processed'] != '')]
    if not generation == 'all':
        df = df.loc[df['기수']== generation]
    if not month == 'all':
        df = df.loc[df['달'] == month]
    if not name.strip() == '':
        df = df.loc[df['댓글작성자'] == name]
    return df
word_cloud = html.Div([
    html.Div([
        dcc.Markdown(
            """
            ## 똑똑집단 단어구름
            과거 돌이켜 보기
            가장 많이 등장한 단어가 가장 크게 표시됩니다. \n
            기수, 월, 사람 별로 많이 사용한 단어 확인 가능

            """
        ),
        html.P([html.Small("다소 오류 많음"),
        #html.A(html.Small("twitter"), href="https://twitter.com/_jphwang", title="twitter"),
        html.Small("!")]),
    ]),
    html.Hr(),
    html.Div([
    dcc.Markdown(
    """
    \n\n
    #### 게시글 단어구름
    아래 드롭다운 값을 통해, 월별 기수별로 데이터 확인이 가능합니다.\n
    이름칸은 비워 놓으면 전체 검색이 가능합니다.
    """
    )
    ]),
    html.Div([
        html.Label(["기수 : "], style = {'display':'inline-block'}),
        dcc.Dropdown(
            id='generation3-select',
            options=[{'label': x, 'value': x} for x in generation_list],
            value='all',
            style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
        ),
        html.Label(["월  : "], style = {'display':'inline-block'}),
        dcc.Dropdown(
            id='month3-select',
            options=[{'label': x, 'value': x} for x in month_list],
            value='all',
            style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
        ),
        html.Label(["이름 : "], style = {'display':'inline-block'}),
        html.Div([
        dcc.Input(
            id='name',
            type="text",
            value = '',
            style={'height': '30px', 'width': '140px','display': 'inline-block','line-height':'34px','border-radius':'4px','border':'1px solid #ccc', 'border-collapse':'separate','position': 'relative','overflow': 'hidden','margin':'0px','padding':'0px'}
        )], style={'width': '140px', 'margin-bottom': '10px'})

    ]),
        dbc.Card([html.Img(id = 'image-wc',style ={'margin':'15px'})])
    ,
    html.Hr(),
    html.Div([
    dcc.Markdown(
    """
    \n\n
    #### 댓글 단어구름
    아래 드롭다운 값을 통해, 월별 기수별로 데이터 확인이 가능합니다.\n
    이름칸은 비워 놓으면 전체 검색이 가능합니다.
    """
    )
    ]),
    html.Div([
        html.Label(["기수 : "], style = {'display':'inline-block'}),
        dcc.Dropdown(
            id='generation4-select',
            options=[{'label': x, 'value': x} for x in generation_list],
            value='all',
            style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
        ),
        html.Label(["월  : "], style = {'display':'inline-block'}),
        dcc.Dropdown(
            id='month4-select',
            options=[{'label': x, 'value': x} for x in month_list],
            value='all',
            style={'height': '30px', 'width': '140px', 'margin-bottom': '10px'}
        ),
        html.Label(["이름 : "], style = {'display':'inline-block'}),
        html.Div([
        dcc.Input(
            id='name2',
            type="text",
            value = '',
            style={'height': '30px', 'width': '140px','display': 'inline-block','line-height':'34px','border-radius':'4px','border':'1px solid #ccc', 'border-collapse':'separate','position': 'relative','overflow': 'hidden','margin':'0px','padding':'0px'}
        )], style={'width': '140px', 'margin-bottom': '10px'})

    ]),
        dbc.Card([html.Img(id = 'image-wc2',style ={'margin':'15px'})])
])
