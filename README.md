# 똑똑집단 4기 ~ 9기 데이터 승수머신

## 결과물 :  https://ddokddok.herokuapp.com/ 
- ###각 메뉴 별 첫 로딩에 시간이 걸립니다...

- 동아리 활동중 월별로 네이버 밴드 활동량을 측정해서 상을 시상했는데, 이 과정을 크롤링을 통해 자동화 했었음
- 코로나로 인해 동아리 활동이 끝나게 되면서 이때까지 쌓은 데이터를 이용해 동아리원들에게 추억으로 남겨주고자 함

- 네이버 밴드 api를 이용해 밴드목록, 게시글, 댓글 불러옴
- 불러온 데이터를 시간, 사람 별로 분류
- plotly, dash를 이용해 반응형 시각화
- 단어구름, 확률론적 언어모형을 이용한 게시글, 댓글 자동 생성 봇 생성

- 웹 구성 후에 heroku 플랫폼을 통해 서버에 배포

## 아쉬운점 : 
- 네이버 밴드 api는 현재 대댓글의 크롤링 기능이 없어서 셀레니움으로 웹을 컨트롤해서 크롤링 해야했음. 
- 네이버 밴드 웹 로그인은 단순히 아이디 비밀번호를 입력하는 것이 아니라, 핸드폰으로 인증번호를 보내 인증 과정을 거쳐야 했음
- 이런 문제로 대댓글 크롤링시 로그인을 하는 과정은 자동화 하지는 못함.
