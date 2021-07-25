import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

post_df = pd.read_csv('band_writings_list.csv')
comment_df = pd.read_csv('band_comment_list.csv')
generation_list =  ['all'] + list(post_df['기수'].drop_duplicates().sort_values())
month_list = ['all'] + list(post_df['달'].drop_duplicates().sort_values())
people_list = ['all'] + list(post_df['이름'].drop_duplicates())

def post_word_df(df, generation = 'all', month = 'all', method = 'sum'):
    if not generation == 'all':
        df = df.loc[df['기수'] == generation]
    if not month == 'all':
        df = df.loc[df['달'] == month]
    if method == 'sum':
        return df.groupby('이름')[['글길이']].sum().sort_values(by = '글길이', ascending = False).reset_index()[:30]
    else:
        return df.groupby('이름')[['글길이']].mean().sort_values(by = '글길이', ascending = False).reset_index()[:30]

def comment_word_df(df, generation = 'all', month = 'all', method = 'sum'):
    if not generation == 'all':
        df = df.loc[df['기수']== generation]
    if not month == 'all':
        df = df.loc[df['달'] == month]
    if method =='sum':
        return df.groupby('댓글작성자')[['댓글길이']].sum().sort_values(by = '댓글길이', ascending = False).reset_index()[:30]
    else:
        return df.groupby('댓글작성자')[['댓글길이']].mean().sort_values(by = '댓글길이', ascending = False).reset_index()[:30]

def comment_num_df(df, generation = 'all', month = 'all'):
    if not generation == 'all':
        df = df.loc[df['기수']== generation]
    if not month == 'all':
        df = df.loc[df['달'] == month]
    return df.groupby('댓글작성자')[['댓글길이']].count().sort_values(by = '댓글길이', ascending = False).reset_index()[:30]


def post_word_plot(generation = 'all', month = 'all'):

    fig = px.bar(post_word_df(post_df, generation = generation, month = month, method = 'sum').sort_values(by ='글길이'), x = '글길이', y = '이름',
                hover_data=['글길이'], color='글길이',orientation='h', title = '글 글자수')
    fig.update_layout(    paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',)
    return fig
    fig.show()

def comment_plot(generation = 'all', month = 'all'):


    temp_df = pd.merge(comment_num_df(comment_df, generation,month).rename(columns ={'댓글길이':'댓글수'}).sort_values(by = '댓글수'),comment_word_df(comment_df, generation,month))

    y_saving = temp_df['댓글수']
    y_net_worth = temp_df['댓글길이']
    x = temp_df['댓글작성자']


    # Creating two subplots
    fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                        shared_yaxes=False, vertical_spacing=0.001)

    fig.append_trace(go.Bar(
        x=y_saving,
        y=x,
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1),
        ),
        name='댓글 개수',
        orientation='h',
    ), 1, 1)

    fig.append_trace(go.Bar(
        x=y_net_worth, y=x,
        marker=dict(
        color='rgb(128, 0, 128, 0.6)',
        line=dict(
            color='rgb(128, 0, 128, 1)',
            width=1),
        ),
    #     mode='lines+markers',
    #     line_color='rgb(128, 0, 128)',
         name='댓글 글자수',
        orientation='h',
    ), 1, 2)

    fig.update_layout(
        title='똑똑집단 댓글 개수, 댓글 글자수',
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.85],
        ),
        yaxis2=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.85],
        ),
    #     yaxis2=dict(
    #         showgrid=False,
    #         showline=True,
    #         showticklabels=False,
    #         linecolor='rgba(102, 102, 102, 0.8)',
    #         linewidth=2,
    #         domain=[0, 0.85],
    #     ),
        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0, 0.42],
        ),
         xaxis2=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0.47, 1],
        ),
    #     xaxis2=dict(
    #         zeroline=False,
    #         showline=False,
    #         showticklabels=True,
    #         showgrid=True,
    #         domain=[0.47, 1],
    #         side='top',
    #         dtick=25000,
    #     ),
        legend=dict(x=0.029, y=1.038, font_size=10),
        margin=dict(l=100, r=20, t=70, b=70),
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
    )

    annotations = []

    y_s = np.round(y_saving, decimals=2)
    y_nw = np.rint(y_net_worth)


    # Source
    annotations.append(dict(xref='paper', yref='paper',
                            x=-0.1, y=-0.109,
                            text= '똑똑집단 댓글 통계',
                            font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)
    return fig
    fig.show()
