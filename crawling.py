import requests
import json
import re
import pandas as pd
import numpy as np

#접속 토큰
access_token = 'your_token'

#밴드 리스트 받아오가
band_list_json = requests.get('https://openapi.band.us/v2.1/bands', params = {'access_token': access_token})
print(band_list_json.json())
band_list = band_list_json.json()['result_data']['bands']

#똑똑집단 리스트 받아오기
ddok_list = [x for x in band_list if '똑똑' in x['name']]

#데이터 프레임으로 만들 dic리스트
ddok_df = []

#데이터 원하는 형식으로 크롤링

#게시글
bandkey_dict = {x['name'].split('똑똑집단')[-1].strip() : x['band_key'] for x in ddok_list}
for generation, band_key in bandkey_dict.items():
    writings = requests.get('https://openapi.band.us/v2/band/posts', params = {'access_token':access_token, 'band_key' : band_key}).json()

    writings_list = writings['result_data']['items']

    while writings['result_data']['paging']['next_params']:
        after = writings['result_data']['paging']['next_params']['after']
        writings = requests.get('https://openapi.band.us/v2/band/posts', params = {'after':after,'access_token': access_token, 'band_key':band_key}).json()
        writings_list += writings['result_data']['items']
    for writing in writings_list:
        hashtags = re.findall(r'[#]\w+', writing['content'])
        if hashtags and re.findall(r'\d+', hashtags[0]):
            month = re.findall(r'\d+', hashtags[0])[0]
            name = writing['author']['name']
            text = writing['content'].replace('\n',' ')
            comment_count = writing['comment_count']
            band_key = band_key
            post_key = writing['post_key']
            temp_dict = {'기수' : generation, '달':month, '글작성자':name,'내용':text ,'댓글수':comment_count,'밴드key':band_key, '글key':post_key}
            ddok_df.append(temp_dict)
pd.DataFrame(ddok_df).to_csv('band_writings_list.csv')

#댓글
ddok_comment_list = []
for bwdic in band_writing_dict:
    band_key = bwdic['밴드key']
    post_key = bwdic['글key']
    generation = bwdic['기수']
    response = requests.get('https://openapi.band.us/v2/band/post/comments', params = {'access_token':access_token,'band_key':band_key,'post_key':post_key})
    if response.json()['result_data']['items']:
        comment_list = response.json()['result_data']['items']
        for i in range(len(comment_list)):
            comment = comment_list[i]
            author = comment['author']['name']
            comment_text = comment['content']
            temp_dict = {'기수':generation,'글key':post_key,'댓글작성자':author,'댓글내용':comment_text,'댓글순서':i}
            ddok_comment_list.append(temp_dict)
comment_df = pd.DataFrame(ddok_comment_list)
comment_df['댓글내용'] = pd.DataFrame(ddok_comment_list)['댓글내용'].apply(lambda x : re.sub(r'\<[^)]*\>','',x))
comment_df.to_csv('band_comment_list.csv')
