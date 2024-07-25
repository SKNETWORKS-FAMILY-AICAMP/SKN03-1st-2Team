from datetime import datetime
import pandas as pd
import streamlit as st
import json


def m_date(past_year:int=5) -> tuple: 
        """_summary_

        Args:
            past_year (int, optional): _description_. Defaults to 5.

        Returns:
            tuple: (years, months)
        """
        current_year = datetime.now().year
        years = list(range(current_year - past_year, current_year + 1))  # 지난 10년과 현재 연도
        months = list(range(1, 13))  # 1월부터 12월까지
        
        return years, months


def date_to_int(year, month, start_flag = True):
    if start_flag:
        start_date_str = f"{year}-{month:02d}-01"
        int_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        
    else:
        end_date_str = f"{year}-{month:02d}-{pd.Period(f'{year}-{month:02d}').end_time.day:02d}"
        int_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        
    
    result_dt = int(int_date.strftime('%Y%m'))
    return result_dt

class select_area:
    def __init__(self) -> None:
       with open('./custom_package/encode_config.json', 'r', encoding='utf-8') as f:
            self.j_file = json.load(f)
       
    def select_city(self) -> str:
        city = st.selectbox("도시를 골라주세요", list(self.j_file['city'].keys())+['전체'])
        if city == "전체":
            result =  ""
        else:
            result = city + self._select_distict(city)
            
        return result 
            
    def _select_distict(self, city) -> str:
        disticts = self.j_file['city'][city]
        distict = st.selectbox("하위 지역을 골라주세요", disticts + ['전체'])
        if distict == "전체":
            result =  ""
        else:
            result = " " + distict
        
        return result