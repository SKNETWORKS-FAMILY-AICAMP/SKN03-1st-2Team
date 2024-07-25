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
        with open('./custom_package/encode_config.json', 'r', encoding='utf-8') as file:
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

        customer_data = self._get_request(customer)
        
        
        data = self._fillter_data(datas=customer_data, request_dict=customer)

        df = pd.DataFrame(data, columns=["date", "address", "city", 'district', 'vehicle_type', 'vehicle_count'])
        return df
            
        
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
        
        
    def _fillter_data(self,datas:list,request_dict: dict) -> list[list]:
        
        distirct_code = request_dict['district'].split()
        case_number = len(distirct_code)
        result = []
        #3.10부터 switch-match문으로 switch case 지원
        match case_number:
            case 0:
                #지역 설정 X -> 그럼 car type 만
                for data in datas:
                    if data['시군구'] == "계":
                        continue
                    else:
                        for vehicle in self.car:
                            result.append([data['date'], data['시도명']+" "+data['시군구'], data['시도명'],data['시군구'], vehicle.split(">")[0], data[vehicle]])
                else:
                    return result
            
            case 1:
                #시도명만 설정 
                for data in datas:
                    if data['시도명'] == request_dict['district']: 
                        if data['시군구'] == "계":
                            continue
                        for vehicle in self.car:
                            result.append([data['date'], request_dict['district']+ " "+data['시군구'], request_dict['district'], data['시군구'],vehicle.split(">")[0], data[vehicle]])
                else:
                    return result
            case 2:
                #특정 시군구 설정
                for data in datas:
                    if data['시도명'] == distirct_code[0]: 
                        if data['시군구'] == distirct_code[1]:
                            
                            for vehicle in self.car:
                                result.append([data['date'], request_dict['district'], distirct_code[0],data['시군구'] == distirct_code[1], vehicle.split(">")[0], data[vehicle]])
                                
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    return result
                    
if __name__ == "__main__":
    test_customers = VehicleRegistry()
    result_df = test_customers.insert_data()
    #result_df.to_csv('output.csv')
    