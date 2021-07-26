import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

home_content = html.Div([
    html.Div([
        dcc.Markdown(
            """
            ## 똑똑집단 데이터 결산


            """
        ),
        html.Hr(),
        dcc.Markdown(
            """

            - 4~9기 데이터 활용하였습니다.\n
            - 3기 밴드 관리자분 계시면 연락주세요.
            - 주의) 그래프의 경우 마우스로 드래그, 핸드폰에서 터치후 움직일시 확대 되는데, 마우스로 더블클릭 또는 핸드폰에서 두번 탭하면 원래대로 돌아옵니다

            """
        ),
        html.Hr(),
        dcc.Markdown(
            """
            - 승수머신 basic : 우수 게시글, 우수 덧글 작성자 선정시 사용 했던 승수 머신
                - 데이터 범위를 4~9기로 확대하여, 전체 기간, 기수별, 월별로 게시글, 댓글 데이터 확인가능\n

            - 똑집 단어구름 : 기수별, 월별, 동아리원별 게시글, 댓글 단어 구름 생성
                - 단어 크기가 클수록 자주 사용한 단어 (ex) 조창희 게시글 단어 구름에는 술, 물구나무가 있음\n

            - 자동생성봇 : 확률론적 언어모형을 이용해 동아리원이 작성한 게시글, 덧글 바탕으로 자동으로 게시글 덧글 생성하는 모델 개발
                - 게시글 생성, 댓글 생성 버튼을 통해 랜덤으로 생성되는 게시글, 댓글 볼 수 있음
                - 아래 회장들 중심으로 개인화된 모델 생성해 놨음, 실제와 얼마나 비슷한지 보는것도 재미 있을듯
                - 혹시 자기도 생성해 달라 하고 싶으면 요청 해주세용


            """
        ),
        dcc.Markdown(
            """
 

            """
        ),
    ]),
])