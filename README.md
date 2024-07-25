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


## 기업 FAQ 조회 시스템


### 데이터


<img width="400" alt="image" src="https://github.com/user-attachments/assets/5f9575b8-1eb0-46c0-9a2b-d0531b07333d">


<img width="300" alt="image" src="https://github.com/user-attachments/assets/4e9bd7fa-b9a6-456d-bf32-368f1903f6e3">




FAQ 데이터, 질문과 답변, 해당 질문에 해당하는 카테고리 정보가 있음


### 기능


비슷한 종류의 기업들의 FAQ 들을 모아 표시, 비교 가능


# TODO LIST


     □ 전국 자동차 등록 현황 및 기업 FAQ 조회 시스템

      □ 전국 자동차 등록 현황
  
        □ 데이터 수집

             □ API 를 통한 데이터 수집

             □ streamlit 내 버튼 조작으로 사용자 요구에 해당하는 조건의 데이터 수집

        □ 서비스 기능 구현

             □ 사용자 조작으로 조건별 탐색

             □ 차량 대수 출력, 1D 데이터

             □ 그래프를 통한 2D 시각화

             □ 지도 위 3D 그래프 출력 
  
    □ 기업 FAQ 조회 시스템
    
      □ 데이터 수집
        
             □ FAQ 내용 크롤링
      
             □ 이미지 크롤링
      
             □ 크롤링 데이터 DB 저장
    
      □ 서비스 기능 구현

             □ 기업별 FAQ 내용 ( 질문, 답변, 키워드 ) 확인

             □ FAQ 검색 시스템

             □ FAQ Keyword Clustering
        
    □ Streamlit

             □ 편리한 UI 구성




# 구현

## 전국 자동차 등록 현황

API 를 통해 데이터 호출 

사용자로부터 날짜, 지역의 정보를 입력받아 해당하는 API 데이터 추출


## 데이터 흐름도

![image](https://github.com/user-attachments/assets/f1973ed6-8d8e-494e-8269-c3041eccda30)



## 기업 FAQ 조회 시스템

BeautifulSoup : HTML 파일 파싱 라이브러리, 정적 페이지(카카오네비, KT원네비, 아틀란) 크롤링


pandas : 해당 데이터들의 DataFrame 형식의 저장


sqlAlchemy : MySQL에 데이터 프레임 전송


![image](https://github.com/user-attachments/assets/c59d6171-3412-435f-9a7e-0693ce9fe1a6)


크롬 개발자 도구를 통해 FAQ 데이터들이 정적 수집이 가능한 형태로 존재하는 것을 확인



각 기업별 FAQ 가 저장되어 있는 형태가 다르므로 각기 다른 크롤링 과정 수행

# 기업 선정

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

# 전국 자동차 등록 현황

streamlit 버튼을 통한 사용자 입력으로 API 호출 명령어 생성

호출된 데이터 표현

![image](https://github.com/user-attachments/assets/3c5591d5-6b29-4a2b-9ee8-bbd733d9a3bd)


# streamlit 화면

![image](https://github.com/user-attachments/assets/2c417726-0c87-4341-ae16-551226a42020)

![image](https://github.com/user-attachments/assets/949f062b-4fbe-47e0-b74d-1802f3c8341a)


# 기업 FAQ 조회 시스템

sql 구문으로 각 기업 데이터 테이블 호출

해당 데이터들의 DataFrame 형식 저장

DataFrame 조작으로 필요 데이터 추출, 출력

![image](https://github.com/user-attachments/assets/5012e987-21cf-4952-97ed-e9d4e57a4bcb)

# streamlit 화면

![image](https://github.com/user-attachments/assets/1677a299-bdb9-4272-99d9-23341395aea8)


# 구현

# 발생 이슈들

## DB 생성 및 연동 문제

크롤링 데이터 저장 및 호출 과정에서 DB 와의 연동 문제 발생,

DB 생성, 암호 등의 간단한 문제, DB 연동 전 해당 내용 확인 필요

## 키워드 추출 문제

특정 기업에서 제공하는 FAQ 내 키워드 데이터가 존재하지 않음, 임의의 Keyword 를 추출했어야 했음,

정규 방정식을 사용한 질문 데이터의 전처리를 통해 임의의 Keyword 추출

## 웹 페이지 접근 문제

여러 페이지로 구성되어 있는 FAQ 데이터 수집 시 각 페이지 별 이동 문제

기업별 URL 구조 ( path, parameter ) 분석으로 별도의 하이퍼 링크 크롤링 없이 페이지 이동

## 날짜 데이터 형식 문제

API 호출시 필요한 날짜 데이터의 형식과 streamlit 을 통해 수집한 날짜 데이터의 형식이 맞지 않음,

date_to_int 함수를 통한 형식 변환

## 크롤링 코드 통합 문제

기업별 크롤링을 각각의 팀원들이 분담하여 진행, 변수명부터 url 접근 방식, db 연동까지 다 다른 형식으로 구성되어 있었음

통합 과정에서 반드시 통일해야 하는 부분부터 통합화






# 보완할 점

## Git 활용

git 을 이용한 협업, 코드 관리 공유를 제대로 활용하지 못했음, 

이로 인해 개발 과정에서 발생한 이슈들을 online 상에서 해결하지 못 함 

## 모듈 및 함수 구성

동일한 기능을 모듈 및 함수로 구현하여 사용하지 못함

이로 인해 코드 분석, 통합 과정에 어려움을 겪었고, 모듈 구성의 필요성을 느낌

## 데이터 베이스 활용

향후 다뤄야 할 데이터가 더 크거나 실시간으로 작동되는 서비스의 구현 시

sql 구문을 통한 데이터 저장 및 호출, 검색이 이뤄져야 함을 느낌










