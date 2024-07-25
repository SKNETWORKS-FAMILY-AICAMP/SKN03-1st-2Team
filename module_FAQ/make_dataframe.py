import pandas as pd

def make_df(p_keywords, p_question, p_answer):
    df = pd.DataFrame({
    'Keywords' : p_keywords,
    'Question' : p_question,
    'Answer' : p_answer
    })

    return df