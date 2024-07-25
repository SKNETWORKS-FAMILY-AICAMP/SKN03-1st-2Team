import streamlit as st
from datetime import datetime
import custom_package.customlit as clit
# Streamlit 앱 제목 설정
st.title('탐색조건을 설정해 주세요')
st.write("")

# ************************************** 사용자 입력변수 받는 창 ************************************** #

# 연도, 월 선택
## 시작 연도와 월 선택 위젯
st.subheader('시작 날짜 설정')
start_year = st.selectbox("시작 연도를 선택하세요:", clit.m_date()[0])
start_month = st.selectbox("시작 월을 선택하세요:", clit.m_date()[1])

## 끝 연도와 월 선택 위젯
st.subheader('끝 날짜 설정')
end_year = st.selectbox("끝 연도를 선택하세요:", clit.m_date()[0])
end_month = st.selectbox("끝 월을 선택하세요:", clit.m_date()[1])
try:
    assert (start_year, start_month) <= (end_year, end_month), "시작 날짜는 끝 날짜보다 이전이어야 합니다."
    if (end_year == datetime.now().year) and (end_month > datetime.now().month -1):
        raise ValueError(f"{datetime.now().year}년 { datetime.now().month -1} 이후데이터는 존재하지 않습니다")

except AssertionError as e:
    st.error(f"오류: {e}")
except ValueError as e:
    st.error(f"오류: {e}")

start_date = clit.date_to_int(start_year,start_month)
end_date = clit.date_to_int(end_year,end_month,start_flag=False)


# 지역선택
st.subheader('지역 설정')

customer_area = clit.select_area()
area = customer_area.select_city()


# 유저의 선택결과를 dict에 담아서 전달
st.session_state.data = {"start_date": start_date, "end_date": end_date, "district": area}

st.page_link("./pages/result.py", label="결과", icon="📈")
