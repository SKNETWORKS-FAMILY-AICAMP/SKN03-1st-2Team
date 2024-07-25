# app.py

import streamlit as st

# 페이지 제목 설정
st.title('Private SNS')

# 사용자 인증 기능
username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password', type='password')

# 사용자별 콘텐츠 올리기 기능
if username == 'user1' and password == 'password1':
    st.sidebar.header('User1 Content')
    content_type = st.sidebar.selectbox('Select content type', ['Text', 'Image', 'Video'])
    if content_type == 'Text':
        text_content = st.text_area('Write your text here')
        if st.button('Post Text'):
            st.success(f'User1 posted: {text_content}')
    elif content_type == 'Image':
        image_file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
        if image_file is not None:
            st.image(image_file, caption='Uploaded Image', use_column_width=True)
            if st.button('Post Image'):
                st.success('User1 posted an image')
    elif content_type == 'Video':
        video_file = st.file_uploader('Upload Video', type=['mp4'])
        if video_file is not None:
            st.video(video_file)
            if st.button('Post Video'):
                st.success('User1 posted a video')
elif username == 'user2' and password == 'password2':
    st.sidebar.header('User2 Content')
    content_type = st.sidebar.selectbox('Select content type', ['Text', 'Image', 'Video'])
    if content_type == 'Text':
        text_content = st.text_area('Write your text here')
        if st.button('Post Text'):
            st.success(f'User2 posted: {text_content}')
    elif content_type == 'Image':
        image_file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
        if image_file is not None:
            st.image(image_file, caption='Uploaded Image', use_column_width=True)
            if st.button('Post Image'):
                st.success('User2 posted an image')
    elif content_type == 'Video':
        video_file = st.file_uploader('Upload Video', type=['mp4'])
        if video_file is not None:
            st.video(video_file)
            if st.button('Post Video'):
                st.success('User2 posted a video')
else:
    st.error('Invalid username or password')
    