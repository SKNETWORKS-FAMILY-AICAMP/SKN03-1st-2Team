import json
import requests
import pandas as pd
from datetime import datetime

class VehicleRegistry:
    
    def __init__(self) -> None:
        """encode_key : str
           city : dict, {시 : [군구,...], }
           car : list
        """
        with open('encode_config.json', 'r', encoding='utf-8') as file:
            # 한국어로 저장되어 있기 때문에 utf-8
            encode = json.load(file)
        self.encode_key = encode["encoded_key"] #개인 API키
        self.city  = encode['city'] #가능한 시 + 군구 목록
        self.car = encode['car_type'] #차량 종류 
    
    
    
    def insert_data(self, start_date:int=202406, end_date:int=202406, district:str="") -> pd.DataFrame:
        customer = {
            "start_date": start_date,
            "end_date" : end_date,
            "district" : district
            
        }
        try:
            customer_data = self._get_request(customer)
            assert type(customer_data) == list, "해당 조건을 만족하는 데이터가 없습니다"
            assert self._int2date(start_date) <= self._int2date(end_date), "시작일은 종료일보다 앞에 있어야합니다"
            
            data = self._fillter_data(datas=customer_data, request_dict=customer)
            assert len(data) > 0 , "해당 조건을 만족하는 데이터가 없습니다"
            
        except AssertionError as e:
            print(e)
        else:
            df = pd.DataFrame(data, columns=["date", "시군구", "시", '하위 지역', '차량 종류', '등록 차량 수'])
            return df
        
    def _int2date(self,date_int):
        date_str = str(date_int)
    
        # 문자열에서 년도와 월 추출
        yyyy = int(date_str[:4])
        mm = int(date_str[4:])
        date_obj = datetime(yyyy, mm, 1)
        return date_obj
    
        
    def _get_request(self, request_dict: dict):
        base_url = "http://stat.molit.go.kr/portal/openapi/service/rest/getList.do"
        params = {
            'key': self.encode_key,
            "form_id" : 5498,
            'style_num': 2,
            'start_dt': request_dict['start_date'],
            'end_dt': request_dict['end_date']
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["result_data"]["formList"]
        else:
            return None
        
        
    def _fillter_data(self,datas:list[dict],request_dict: dict) -> list[list]:
        
        distirct_code = request_dict['district'].split()
        case_number = len(distirct_code)
        result = []
        #3.10부터 switch-match문으로 switch case 지원
        match case_number:
            case 0:
                #지역 설정 X -> 그럼 car type 만
                for data in datas:
                    for vehicle in self.car:
                        result.append([data['date'], data['시도명']+" "+data['시군구'], data['시도명'],data['시군구'], vehicle, data[vehicle]])
                else:
                    return result
            
            case 1:
                #시도명만 설정 
                for data in datas:
                    if data['시도명'] == request_dict['district']: 
                        for dis in  self.city[request_dict['district']] : #군구 출력
                            for vehicle in self.car:
                                result.append([data['date'], request_dict['district']+" "+dis, request_dict['district'],dis, vehicle, data[vehicle]])
                        else:
                            return result
                    else:
                        continue
            case 2:
                #특정 시군구 설정
                for data in datas:
                    if data['시도명'] == distirct_code[0]: 
                        if data['시군구'] == distirct_code[1]:
                            for vehicle in self.car:
                                result.append([data['date'], request_dict['district'], distirct_code[0],data['시군구'] == distirct_code[1], vehicle, data[vehicle]])
                                
                            else:
                                return result
                        else:
                            continue
                    else:
                        continue
                    
if __name__ == "__main__":
    test_customers = VehicleRegistry()
    result_df = test_customers.insert_data()
    #result_df.to_csv('output.csv')
    