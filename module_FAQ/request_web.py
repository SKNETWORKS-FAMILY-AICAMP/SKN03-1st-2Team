import requests
from bs4 import BeautifulSoup as bs

# def request_web(p_company):
#     custom_header = {
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
#     }
#     if p_company == '아틀란':
#         # 웹 페이지 요청
#         url = 'https://www.atlan.co.kr/support/faq/list.do?page=1'    #url이라는 변수에 크롤링 할 사이트 url을 담기.
#         response = requests.get(url, headers=custom_header)
#         change_web(response, p_company)

def request_webdata(p_company):

    if p_company == '아틀란':
        question = []
        keywords = []
        answer = []
        custom_header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        # 웹 페이지 변경
        for i in range(13):
            url = 'https://www.atlan.co.kr/support/faq/list.do?page='
            url += str(i+1)
            response = requests.get(url, headers=custom_header)
            soup = bs(response.text, "html.parser")
            question.append(soup.find_all('span', class_='faq_subject'))
            keywords.append(soup.find_all('span', class_='sub_category'))
            answer.append(soup.find_all('div', class_= "faq_answer"))
        return keywords, question, answer
    
    elif p_company == '카카오':
        headers = {
          'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        # 각 버튼이 가리키는 하이퍼 링크와 연결하기 위한 값
        address = "https://cs.kakao.com"

        # 각 데이터의 저장
        keyword_list = []
        question_list = []
        answer_list = []


        for i in range(17):
            url = "https://cs.kakao.com/helps?service=101&locale=ko&isAll=true&page="
            url += str(i+1)

            response = requests.get(url, headers=headers)
            soup = bs(response.text, "html.parser")
            
            # 각 질문으로 이동할 버튼 탐색.
            faq_button = soup.find_all("a", class_="link_content")

            address_list = []

            for faq_link in faq_button:
                address_list.append(address + faq_link.attrs['href'])

            for link in address_list:
                response = requests.get(link, headers=headers)
                soup = bs(response.text, "html.parser")

                # faq 페이지 내에서 keyword 의 획득
                keyword_list.append(soup.find_all("button", class_="btn_cate")[1].get_text())

                # 질문 획득
                question_list.append(soup.find("strong", class_="tit_sub").get_text())

                answer_list.append(soup.find("div", class_="service-help-content desc_content").get_text().replace("\xa0",""))
        return keyword_list, question_list, answer_list