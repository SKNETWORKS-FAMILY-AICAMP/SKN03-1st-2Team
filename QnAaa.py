import requests
from bs4 import BeautifulSoup as bs
from fuzzywuzzy import process

# 질문 크롤링
response_Q = requests.get("https://navi.kt.com/faqList.html")
response_Q.encoding = 'utf-8'
soup = bs(response_Q.text, 'html.parser')
Q = soup.find_all("a", class_="accordion-trigger")

# 답변 크롤링
response_A = requests.get("https://navi.kt.com/faqList.html")
response_A.encoding = 'utf-8'
soup = bs(response_A.text, 'html.parser')
A = soup.find_all("div", class_="accordion-contents")

# 질문과 답변을 리스트화
FAQ_list = []
for Question, Answer in zip(Q, A):
    FAQ_list.append(
        {"Question": Question.text.strip(), "Answer": Answer.text.strip()}
    )

# 키워드를 통해 가장 유사한 질문 찾기
def find_most_similar_question(keyword, faq_list):
    questions = [faq['Question'] for faq in faq_list]
    best_match = process.extractOne(keyword, questions)
    return best_match

# 키워드 입력
keyword = "제보하기"  # 검색하고자 하는 키워드를 입력합니다

# 가장 유사한 질문 찾기
most_similar_question = find_most_similar_question(keyword, FAQ_list)

# 출력
if most_similar_question:
    question_text = most_similar_question[0]
    question_index = [faq['Question'] for faq in FAQ_list].index(question_text)
    print(f"가장 유사한 질문: {question_text}")
    print(f"답변: {FAQ_list[question_index]['Answer']}")
else:
    print("유사한 질문을 찾을 수 없습니다.")