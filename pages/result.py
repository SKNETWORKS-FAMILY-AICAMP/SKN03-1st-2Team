import streamlit as st
import pandas as pd
import warnings
from custom_package import API_module as api

# Streamlit 앱 제목 설정
st.title('차량 데이터 시각화')

if "data" not in st.session_state:
    st.write("선택한 조건이 없습니다. \n Car_index 페이지를 먼저 이용해 주세요")

else:
    customer_data = api.VehicleRegistry()
    session_data = st.session_state.data

    df = customer_data.insert_data(start_date=session_data['start_date'], end_date=session_data['end_date'], district=session_data['district'])
    # # columns
    # # ["date", "address", "city", 'district', 'vehicle_type', 'vehicle_count']

    # ---key sidebar button ----
    st.sidebar.header("Please Filter Here")
    manufacturer = st.sidebar.multiselect(
        "자동차 종류:",
        options=df['vehicle_type'].unique(),
        default=df['vehicle_type'].unique()
    )

    # ---key sidebar radio button ----
    city = st.sidebar.radio(
        "도시 종류:",
        options=df['city'].unique(),
        #default = df['Automation'].unique()
    )

    df_select = df[(df['vehicle_type'].isin(manufacturer))& (df['city'] == city)]

    # ---key sidebar radio button ----
    district = st.sidebar.radio(
        "하위 구역 종류:",
        options=df_select['district'].unique(),
        #default = df['Automation'].unique()
    )

    # sidebar key와 DataFrame 표시 값 연동
    df_select = df_select[df_select['district'] == district]

    # DataFrame에 할당 값이 없을 때 오류 메세지
    if df_select.empty:
        st.warning("No data available based on the current filter settings!")
        st.stop()  ##-- halt streamlit from further execution

    st.subheader("검색 결과")
    st.dataframe(df_select)

    df_aggregated = df_select.groupby(['date', 'vehicle_type'], as_index=False).agg({'vehicle_count': 'sum'})

    # # 꺾은선 그래프 생성
    # st.subheader("Vehicle Count 꺾은선 그래프")
    # st.line_chart(df_select)

    # st.subheader("바 차트")

    # st.bar_chart(x='date', y='vehicle_count', hue='vehicle_type', data=df_aggregated)

    # # 영역 차트
    # st.subheader("영역 차트")
    # st.area_chart(data.set_index('Date'))


but = st.button(label= "버튼")
