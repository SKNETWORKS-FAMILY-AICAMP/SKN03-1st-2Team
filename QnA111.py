import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

response_Q = requests.get("https://navi.kt.com/faqList.html")
response_Q.encoding = 'utf-8'
html_content = response_Q.text
soup = bs(response_Q.text, 'html.parser')
Q = soup.find_all("a",class_="accordion-trigger")
#print("출력 확인")
#print("Q"[0])

############################

response_A = requests.get("https://navi.kt.com/faqList.html")
response_A.encoding = 'utf-8'
html_content = response_A.text
soup = bs(response_A.text, 'html.parser')
A = soup.find_all("div",class_="accordion-contents")
#print("출력 확인")
#print(A[0])


remain_brakcet = r'\[([^\]]+)\]'

Keyword_list = []

for i in Q:
    K = i.get_text()
    eng_temp = re.findall(remain_brakcet, K)[0]

    Keyword_list.append(eng_temp)
############################

FAQ_list = []
for Question, Answer in zip(Q, A):
    FAQ_list.append(
        {"Question":Question.text.strip(), "Answer":Answer.text.strip()}
        )
    
for i, FAQ in enumerate(FAQ_list, start=1):
    print(f"Q{i} : {FAQ['Question']}")
    print(f"A{i} : {FAQ['Answer']}")


My_dict = {{"Question":Question.text.strip(), "Answer":Answer.text.strip()}}
tuple_list = list(My_dict.items())

print(tuple_list)
print(Keyword_list)

#딕 형태니까 key값을 빼와서. 그안에서. []안에 있는 글자만 추출.

