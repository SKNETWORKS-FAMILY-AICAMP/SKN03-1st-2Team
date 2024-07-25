# 필요한 라이브러리 import
import requests                         # 웹페이지 요청을 위한 것
from bs4 import BeautifulSoup as bs     # html 파싱을 위한 것
import re                               # 정규표현식을 사용하기 위한 것


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

FAQ_list = []
Keyword_list = []

for i, (question, answer) in enumerate(zip(Q, A), start=1):
    # 질문(Q)에서 키워드 추출
    K = question.get_text()
    eng_temp = re.findall(remain_bracket, K)[0]  # 정규표현식으로 대괄호 안의 내용 추출
    Keyword_list.append(eng_temp)

    # 질문과 답변을 FAQ_list에 추가
    FAQ_list.append({
        "Q{i}": question.text.strip(),
        "A{i}": answer.text.strip()
    })

    # 질문과 답변 출력
    print(f"Q{i}: {question.text.strip()}")
    print(f"A{i}: {answer.text.strip()}")
    print(f"Keyword for Q{i}: {eng_temp}\n")

print("Keyword List:", Keyword_list)