import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from ddok_plot_list import generation_list, month_list


from nltk import ConditionalFreqDist,ConditionalProbDist,MLEProbDist
import pickle

#name_list = ['','_유리','_창희','_doo','_은석','_은호']
name_list = ['_유리','_창희','_doo','_은석','_은호']
post_token_dict = {}
comment_token_dict = {}
for name in name_list:
    with open('./word_tokens/sentences{}_글.pkl'.format(name),'rb') as f:
        post_token_dict[name] = pickle.load(f)
for name in name_list:
    with open('./word_tokens/sentences{}_댓글.pkl'.format(name),'rb') as f:
        comment_token_dict[name] = pickle.load(f)

def korean_generate_sentence(sentences, seed=None, debug=False):
    cfd = ConditionalFreqDist(sentences)
    cpd = ConditionalProbDist(cfd, MLEProbDist)
    if seed is not None:
        import random
        random.seed(seed)
    c = "SS"
    sentence = []
    while True:
        if c not in cpd:
            break
            
        w = cpd[c].generate()

        if w == "SE":
            break

        w2 = w.split("/")[0]
        pos = w.split("/")[1]

        if c == "SS":
            sentence.append(w2.title())
        elif c in ["`", "\"", "'", "("]:
            sentence.append(w2)
        elif w2 in ["'", ".", ",", ")", ":", ";", "?"]:
            sentence.append(w2)
        elif pos in ["Josa", "Punctuation", "Suffix"]:
            sentence.append(w2)
        elif w in ["임/Noun", "것/Noun", "는걸/Noun", "릴때/Noun",
                   "되다/Verb", "이다/Verb", "하다/Verb", "이다/Adjective"]:
            sentence.append(w2)
        else:
            sentence.append(" " + w2)
        c = w

        if debug:
            print(w)

    return "".join(sentence)

generation_content = html.Div([
    html.Div([
        dcc.Markdown(
            """
            # 자동생성 봇

            목표일지, 댓글 데이터를 이용해 만든 확률론적 언어모델로 문장 생성\n
            일지 생성!, 댓글 생성! 버튼 클릭시 자동으로 새로운 일지, 댓글 생성

            """
        ),
        html.P([html.Small("원하시면 추가해드릴게요 말씀해주세요 ^~^"),
        #html.A(html.Small("twitter"), href="https://twitter.com/_jphwang", title="twitter"),
        html.Small("!")]),
    ]),
    html.Hr(),
    html.Div([
    dcc.Markdown(
    """
    \n\n
    ## 똑집 봇
    똑똑집단 4~9기 전체 데이터 활용해서 만든 봇
    """
    )
    ]),
    html.Div([
        html.H2("일지 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'post_gen1')])])]),
        dbc.Button('일지 생성!','post_gen_buttion1',n_clicks=0, style = {'margin-top': '5px'}),
        html.Hr(),
        html.H2("댓글 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'comment_gen1')])])]),
        dbc.Button('댓글 생성!','comment_gen_buttion1',n_clicks=0, style = {'margin-top': '5px'}),

    ]),
])
generation_content1 = html.Div([
    html.Div([
    dcc.Markdown(
    """
    ## 전유리 봇
    창시자 전유리 데이터 학습
    """
    )
    ]),
    html.Div([
        html.H2("일지 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'post_gen2')])])]),
        dbc.Button('일지 생성!','post_gen_buttion2',n_clicks=0, style = {'margin-top': '5px'}),
        html.Hr(),
        html.H2("댓글 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'comment_gen2')])])]),
        dbc.Button('댓글 생성!','comment_gen_buttion2',n_clicks=0, style = {'margin-top': '5px'}),
        

    ]),
])
generation_content2 = html.Div([
    html.Div([
    dcc.Markdown(
    """
    ## 조창희 봇
    그냥 조창희 데이터 학습
    """
    )
    ]),
    html.Div([
        html.H2("일지 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'post_gen3')])])]),
        dbc.Button('일지 생성!','post_gen_buttion3',n_clicks=0, style = {'margin-top': '5px'}),
        html.Hr(),
        html.H2("댓글 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'comment_gen3')])])]),
        dbc.Button('댓글 생성!','comment_gen_buttion3',n_clicks=0, style = {'margin-top': '5px'}),
  

    ]),
])
generation_content3 = html.Div([
    html.Div([
    dcc.Markdown(
    """
    ## 이두희 봇
    댓글, 일지 데이터 통합 1위 두희,,
    """
    )
    ]),
    html.Div([
        html.H2("일지 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'post_gen4')])])]),
        dbc.Button('일지 생성!','post_gen_buttion4',n_clicks=0, style = {'margin-top': '5px'}),
        html.Hr(),
        html.H2("댓글 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'comment_gen4')])])]),
        dbc.Button('댓글 생성!','comment_gen_buttion4',n_clicks=0, style = {'margin-top': '5px'}),


    ]),
])
generation_content4 = html.Div([
    html.Div([
    dcc.Markdown(
    """
    ## 배은석 봇
    9기 회장 배은석
    """
    )
    ]),
    html.Div([
        html.H2("일지 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'post_gen5')])])]),
        dbc.Button('일지 생성!','post_gen_buttion5',n_clicks=0, style = {'margin-top': '5px'}),
        html.Hr(),
        html.H2("댓글 봇"),
        dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'comment_gen5')])])]),
        dbc.Button('댓글 생성!','comment_gen_buttion5',n_clicks=0, style = {'margin-top': '5px'}),


    ]),
])
# generation_content5 = html.Div([
#     html.Div([
#     dcc.Markdown(
#     """
#     ## 이은호 봇
#     두희 오기 전에 일지 1인자 은호
#     """
#     )
#     ]),
#     html.Div([
#         html.H2("일지 봇"),
#         dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'post_gen6')])])]),
#         dbc.Button('일지 생성!','post_gen_buttion6',n_clicks=0, style = {'margin-top': '5px'}),
#         html.Hr(),
#         html.H2("댓글 봇"),
#         dbc.Card([dbc.Row([dbc.Col([html.Div(id = 'comment_gen6')])])]),
#         dbc.Button('댓글 생성!','comment_gen_buttion6',n_clicks=0, style = {'margin-top': '5px'}),


#     ]),
# ])
