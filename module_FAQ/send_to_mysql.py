from sqlalchemy import create_engine

def send_2_mysql(p_df, p_company):
    # MySQL 데이터베이스 연결 정보 설정
    user = 'user'
    password = 'user1234'
    host = 'localhost'
    database = 'faq_db'

    # SQLAlchemy 사용
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

    # 데이터프레임을 MySQL 테이블로 저장
    table_name = p_company + '_faq_data'
    p_df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
