import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


# 데이터베이스 연결 및 쿼리 실행 (예시)
conn = st.connection("dbname", type="sql", autocommit=True)

sql = """
    select
         Keywords
        ,Question
        ,Answer
    from kakao_faq_data
    where 1=1
"""
#데이터 출력 변수
@st.cache_data
def get_data():
    df = conn.query(sql, ttl=3600)
    return df

df = get_data()

st.header("카카오 네비")

# 키워드 버튼 목록
keywords = df['Keywords'].unique()[:]
Question = df['Question'].unique()[:]
Answer = df['Answer'].unique()[:]

# 키워드 버튼을 제목 아래에 추가
selected_keyword = st.selectbox("키워드를 선택해주세요", keywords)
selected_df = df[df['Keywords'] == selected_keyword] #selected_keyword에 들어간 키워드 값을 가져와서 새로운 데이터 프레임을 만든다.

for i in range(selected_df.shape[0]): #selected_df = 키워드 별 데이터 프레임 / shape[0]으로 행의 개수를 구하고 그 길이만큼 반복한다.
    with st.expander(f"{selected_df.iloc[i]["Question"]}"):# 데이터 갯수만큼 상승 된 i값만큼 iloc로 (selected_df)의 인덱스 번호로 접근해서 출력
        st.write(f"{selected_df.iloc[i]["Answer"]}")#해당 iloc변수의 Anwser에 해당하는 데이터를 출력

# 현재 페이지 번호를 세션 상태로 저장
if 'page' not in st.session_state:
    st.session_state.page = 0



