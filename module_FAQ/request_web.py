import requests
from bs4 import BeautifulSoup as bs
import re

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
        
        keywords_in_FAQ = []
        keywords_texts = []
        seen_keywords = set()  # 중복 확인을 위한 집합

        # 각 keywords 리스트의 요소에서 텍스트만 추출
        for k_lists in keywords:
            for span in k_lists:
                text = span.text.strip()  # .strip()으로 앞뒤 공백 제거
                keywords_in_FAQ.append(text)
                # 텍스트가 이미 본 적이 없는 경우에만 추가
                if text not in seen_keywords:
                    seen_keywords.add(text)  # 텍스트를 집합에 추가
                    keywords_texts.append(text)  # 리스트에 텍스트 추가
        
        question_texts = []
        seen_texts = set()  # 중복 확인을 위한 집합

        # 각 question 리스트의 요소에서 텍스트만 추출
        for q_list in question:
            for span in q_list:
                text = span.text.strip()  # .strip()으로 앞뒤 공백 제거
                
                # 중복제거
                if text not in seen_texts:
                    seen_texts.add(text)  # 텍스트를 집합에 추가
                    question_texts.append(text)  # 리스트에 텍스트 추가

        answer_texts = []
        seen_answer = set()  # 중복 확인을 위한 집합

        # 각 keywords 리스트의 요소에서 텍스트만 추출
        for a_lists in answer:
            for span in a_lists:
                text = span.text.strip()  # .strip()으로 앞뒤 공백 제거

                # 텍스트가 이미 본 적이 없는 경우에만 추가
                if text not in seen_answer:
                    seen_answer.add(text)  # 텍스트를 집합에 추가
                    answer_texts.append(text)  # 리스트에 텍스트 추가
        
        return keywords_in_FAQ, question_texts, answer_texts
    
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
    
    elif p_company == 'kt':
        response_Q = requests.get("https://navi.kt.com/faqList.html")
        response_Q.encoding = 'utf-8'
        html_content = response_Q.text
        soup = bs(response_Q.text, 'html.parser')
        Q = soup.find_all("a", class_="accordion-trigger")

        response_A = requests.get("https://navi.kt.com/faqList.html")
        response_A.encoding = 'utf-8'
        html_content = response_A.text
        soup = bs(response_A.text, 'html.parser')
        A = soup.find_all("div", class_="accordion-contents")

        remain_bracket = r'\[([^\]]+)\]'

        # FAQ_list = []
        Keyword_list = []
        questions = []
        answers = []

        for i, (question, answer) in enumerate(zip(Q, A), start=1):
            # 질문(Q)에서 키워드 추출
            K = question.get_text()
            eng_temp = re.findall(remain_bracket, K)[0]  # 정규표현식으로 대괄호 안의 내용 추출
            Keyword_list.append(eng_temp)
            questions.append(question.text.strip())
            answers.append(answer.text.strip())

        return Keyword_list, questions, answers