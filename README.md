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


# TODO 리스트

     □ 전국 자동차 등록 현황 및 기업 FAQ 조회 시스템

      □ 전국 자동차 등록 현황
  
        □ 데이터 수집

        □ API 를 통한 데이터 수집

        □ streamlit 과의 연동으로 사용자 요구에 해당하는 조건의 데이터 수집

      □ 기능 구현

        □ 사용자 조작으로 조건별 탐색

        □ 차량 대수 출력, 1D 데이터

        □ 그래프를 통한 2D 시각화

        □ 지도 위 3D 그래프 출력 
  
    □ 기업 FAQ 조회 시스템
    
      □ 데이터 수집
        
        □ FAQ 내용 크롤링
      
        □ 이미지 크롤링
      
        □ 크롤링 데이터 DB 저장
    
      □ 기능 구현

        □ 기업별 FAQ 내용 ( 질문, 답변, 키워드 ) 확인

        □ FAQ 검색 시스템

        □ FAQ Keyword Clustering
        
    □ Streamlit

      □ 편리한 UI 구성


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

BeautifulSoup : 정적 페이지(카카오네비, KT원네비, 아틀란) 크롤링

pandas : 해당 데이터들의 DataFrame 형식의 저장

sqlAlchemy : MySQL에 데이터 프레임 전송

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

<img width="400" alt="image" src="https://github.com/user-attachments/assets/b26293ef-9f53-4875-b32e-1ffee4c29e35">


기업별 테이블 관리

# 데이터 흐름도

![image](https://github.com/user-attachments/assets/92f489bb-abaf-4603-a160-b95fe4502661)





# Streamlit 내 데이터 연동

## 전국 자동차 등록 현황


~~



## 기업 FAQ 조회 시스템

sql 구문을 통한 각 기업 데이터 테이블 호출

해당 데이터들의 DataFrame 형식의 저장

DataFrame 의 조작으로 필요 데이터 추출, 출력


![image](https://github.com/user-attachments/assets/5012e987-21cf-4952-97ed-e9d4e57a4bcb)

### streamlit 화면

![image](https://github.com/user-attachments/assets/1677a299-bdb9-4272-99d9-23341395aea8)




  





~~ 각 구현 부분에 대한 설명을 이곳에 추가할까



