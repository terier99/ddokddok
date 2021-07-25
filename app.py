import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from wordcloud import WordCloud
from collections import Counter
from io import BytesIO
import base64


from ddok_plot_list import post_word_plot, comment_plot, generation_list, month_list
from sidebar import sidebar
from basic_content import basic_content
from word_cloud import word_cloud,post_word_df,comment_word_df

import numpy as np

app = dash.Dash(__name__, suppress_callback_exceptions=True)


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
        return basic_content
    elif pathname == "/word_cloud":
        return word_cloud
    elif pathname == "/page-2":
        return html.P("추후업데이트!")
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
    words = words.replace('목표','').replace('달성','').replace('일지','').replace('성취도','').replace('이번','').replace('인증','')
    counts = Counter(words.split(' '))
    tags = counts.most_common(40)
    wc = WordCloud(font_path=r"NanumGothic.ttf", max_font_size=500 , width=1200, height=600)

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
    words = words.replace('목표','').replace('달성','').replace('일지','').replace('성취도','').replace('이번','').replace('인증','')
    counts = Counter(words.split(' '))
    tags = counts.most_common(40)
    wc = WordCloud(font_path=r"NanumGothic.ttf", max_font_size=500 , width=1200, height=600)

    img = wc.fit_words(dict(tags)).to_image()

    with BytesIO() as buffer:
        img.save(buffer, format='png')
        img2 = base64.b64encode(buffer.getvalue()).decode()
    return 'data:image/png;base64,{}'.format(img2)

if __name__ == '__main__':
    app.run_server(debug=True)
