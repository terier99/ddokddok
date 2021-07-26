import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_bootstrap_templates import load_figure_template

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from wordcloud import WordCloud
from collections import Counter
from io import BytesIO
import base64

import pickle
from nltk import bigrams, word_tokenize
from nltk.util import ngrams
from nltk import ConditionalFreqDist,ConditionalProbDist,MLEProbDist
import random


from ddok_plot_list import post_word_plot, comment_plot, generation_list, month_list
from sidebar import sidebar
from basic_content import basic_content
from word_cloud import word_cloud,post_word_df,comment_word_df
#from generation import generation_content,generation_content1,generation_content2,generation_content3,generation_content4,generation_content5 name_list, post_token_dict, comment_token_dict, korean_generate_sentence
from generation import *
from home import home_content

import numpy as np


load_figure_template("sketch")
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[r'assets\bootstrap.css'])


server = app.server
app.title = '똑똑집단'

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


content = html.Div(id="page-content", style=CONTENT_STYLE)


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home_content
    elif pathname == "/basic":
        return basic_content
    elif pathname == "/word_cloud":
        return word_cloud
    elif pathname == "/generation":
        return generation_content1
    elif pathname == "/generation1":
        return generation_content2
    elif pathname == "/generation2":
        return generation_content3
    elif pathname == "/generation3":
        return generation_content4
    elif pathname == "/generation4":
        return generation_content5
    # elif pathname == "/generation5":
    #     return generation_content5
    
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
    Output('post-word-plot', 'figure'),
    Input('generation-select', 'value'),
    Input('month-select', 'value'),
)
def update_graph(generation, month):
    fig = post_word_plot(generation, month)
    # clean_chart_format(fig)
    # if len(grpname) > 3:
    fig.update_layout(height=850)
    # else:
    #     fig.update_layout(height=500, width=1250)

    return fig

@app.callback(
    Output('comment-plot', 'figure'),
    Input('generation2-select', 'value'),
    Input('month2-select', 'value')
)
def update_graph(generation, month):
    fig = comment_plot(generation, month)
    # clean_chart_format(fig)
    # if len(grpname) > 3:
    fig.update_layout(height=650)
    # else:
    #     fig.update_layout(height=500, width=1250)

    return fig

@app.callback(
    Output('image-wc', 'src'),
    Input('generation3-select', 'value'),
    Input('month3-select', 'value'),
    Input('name','value')
)
def make_image (generation, month, name):
    tmp_df = post_word_df(generation,  month, name)
    words = ' '.join(list(tmp_df['processed'].apply(lambda x: str(x))))
    words = words.replace('목표','').replace('달성','').replace('일지','').replace('성취도','').replace('이번','').replace('인증','').replace('   ',' ').replace('  ',' ')
    counts = Counter(words.split(' '))
    tags = counts.most_common(40)
    wc = WordCloud(font_path='NanumGothic.ttf', max_font_size=500 , width=1200, background_color='white', height=600)

    img = wc.fit_words(dict(tags)).to_image()

    with BytesIO() as buffer:
        img.save(buffer, format='png')
        img2 = base64.b64encode(buffer.getvalue()).decode()
    return 'data:image/png;base64,{}'.format(img2)

@app.callback(
    Output('image-wc2', 'src'),
    Input('generation4-select', 'value'),
    Input('month4-select', 'value'),
    Input('name2','value')
)
def make_image (generation, month, name):
    tmp_df = comment_word_df(generation,  month, name)
    words = ' '.join(list(tmp_df['processed'].apply(lambda x: str(x))))
    words = words.replace('목표','').replace('달성','').replace('일지','').replace('성취도','').replace('이번','').replace('인증','').replace('   ',' ').replace('  ',' ')
    counts = Counter(words.split(' '))
    tags = counts.most_common(40)
    wc = WordCloud(font_path='NanumGothic.ttf', max_font_size=500 , width=1200, background_color='white', height=600)

    img = wc.fit_words(dict(tags)).to_image()

    with BytesIO() as buffer:
        img.save(buffer, format='png')
        img2 = base64.b64encode(buffer.getvalue()).decode()
    return 'data:image/png;base64,{}'.format(img2)

# for i in range(len(name_list)):
#     @app.callback(
#     Output('post_gen{}'.format(i+1), 'children'),
#     Input('post_gen_buttion{}'.format(i+1), 'n_clicks'),
#     )
#     def update_bot(n_clicks):
#         sentences = post_token_dict[name_list[i]]
#         seed = random.randint(0,1000)
#         gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
#         return html.P(gen)
#     @app.callback(
#     Output('comment_gen{}'.format(i+1), 'children'),
#     Input('comment_gen_buttion{}'.format(i+1), 'n_clicks'),
#     )
#     def update_bot(n_clicks):
#         sentences = comment_token_dict[name_list[i]]
#         seed = random.randint(0,1000)
#         gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
#         return html.P(gen)

@app.callback(
Output('post_gen1', 'children'),
Input('post_gen_buttion1', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = post_token_dict[name_list[0]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('comment_gen1', 'children'),
Input('comment_gen_buttion1', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = comment_token_dict[name_list[0]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('post_gen2', 'children'),
Input('post_gen_buttion2', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = post_token_dict[name_list[0]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('comment_gen2', 'children'),
Input('comment_gen_buttion2', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = comment_token_dict[name_list[0]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('post_gen3', 'children'),
Input('post_gen_buttion3', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = post_token_dict[name_list[1]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('comment_gen3', 'children'),
Input('comment_gen_buttion3', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = comment_token_dict[name_list[1]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('post_gen4', 'children'),
Input('post_gen_buttion4', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = post_token_dict[name_list[2]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('comment_gen4', 'children'),
Input('comment_gen_buttion4', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = comment_token_dict[name_list[2]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('post_gen5', 'children'),
Input('post_gen_buttion5', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = post_token_dict[name_list[3]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('comment_gen5', 'children'),
Input('comment_gen_buttion5', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = comment_token_dict[name_list[3]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('post_gen6', 'children'),
Input('post_gen_buttion6', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = post_token_dict[name_list[4]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)
@app.callback(
Output('comment_gen6', 'children'),
Input('comment_gen_buttion6', 'n_clicks'),
)
def update_bot(n_clicks):
    sentences = comment_token_dict[name_list[4]]
    seed = random.randint(0,1000)
    gen = korean_generate_sentence(sentences = sentences, seed = random.seed(seed))
    return html.P(gen)

if __name__ == '__main__':
    app.run_server(debug=True)
