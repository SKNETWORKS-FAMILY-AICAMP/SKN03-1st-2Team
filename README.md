# SKN03-1st-2Team
# 전국 자동차 등록 현황 및 기업 FAQ 조회 시스템

전국 자동차 등록 현황, 기업 FAQ 조회 시스템의 두 가지 서비스를 streamlit 을 통해 구현하는 것이 목표

## 전국 자동차 등록 현황

### 데이터

통계시점에 자동차등록원부에 등록하고 운행할 수 있는 자동차(승용, 승합, 화물, 특수)의 대수를 각 세부사항별(차종별, 연료별, 최대적재량별, 규모별 등)로 등록 현황을 제공

![image](https://github.com/user-attachments/assets/76591312-73a7-4cae-ba81-f2c3f99546a3)

### 기능

사용자의 선택으로 해당 조건( 기간, 지역, 차종 )의 차량 대수 조회 가능

<img width="391" alt="image" src="https://github.com/user-attachments/assets/31c77063-65b9-4208-8357-7ae7314842d1">

강동구 지역의 관용-소형 차량 조회 시 23 의 차량 대수의 출력

### 구현

API 를 통해 데이터 호출, 


~ 내용 추가



## 기업 FAQ 조회 시스템

### 데이터

<img width="400" alt="image" src="https://github.com/user-attachments/assets/5f9575b8-1eb0-46c0-9a2b-d0531b07333d">

<img width="300" alt="image" src="https://github.com/user-attachments/assets/4e9bd7fa-b9a6-456d-bf32-368f1903f6e3">



FAQ 데이터, 질문과 답변, 해당 질문에 해당하는 카테고리 정보가 있음

### 기능

비슷한 종류의 기업들의 FAQ 들을 모아 표시, 비교 가능


### 구현

HTML 파일 파싱 라이브러리, BeautifulSoup 의 사용,

![image](https://github.com/user-attachments/assets/c59d6171-3412-435f-9a7e-0693ce9fe1a6)

크롬 개발자 도구를 통해 FAQ 데이터들이 정적 수집이 가능한 형태로 존재하는 것을 확인

각 기업별 FAQ 가 저장되어 있는 형태가 다르므로 각기 다른 크롤링 과정 수행

![image](https://github.com/user-attachments/assets/5fdbba81-e909-4e76-beb4-11f967e82715)

![image](https://github.com/user-attachments/assets/2f188a34-098a-44ed-b3f0-7b9ad092d7d1)

![image](https://github.com/user-attachments/assets/045e04df-1d5d-45cb-ab89-aaefaa82b1ec)


카카오맵, 원네비, 아틀란의 FAQ 데이터 크롤링

FAQ 질문, 답변, 키워드의 크롤링,

Database 내 데이터 저장

![image](https://github.com/user-attachments/assets/06001bb7-51b9-46ca-9e33-b5a00cb3e222)





# Streamlit 내 구현 모습



~~ 각 구현 부분에 대한 설명을 이곳에 추가할까



