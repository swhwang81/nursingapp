import streamlit as st
import pandas as pd
import numpy as np
import pickle
import streamlit.components.v1 as components  # Import Streamlit

##remove a streamlit default header list########
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
################################################

st.markdown("# Patents Info.")
#st.sidebar.markdown("# Patents Info") 

st.write("this is patents info.")

# input widgets and database usages
st.write("#### 환자 정보를 입력하세요.")

col1,col2 = st.columns(2)

#이름
with col1:
    name = st.text_input('이름: ', '홍길동')
    st.write('이름: ', name)
with col2: #성별
    sex = st.selectbox('성별: ', ['남성', '여성'])
    st.write('성별: ', sex)

col3,col4 = st.columns(2)
with col3:  
    age = st.slider('나이', 0, 110, 25)
    st.write("나이: ", age, ' 세')
with col4:
    period = st.slider('입원기간', 0, 60, 3)
    st.write("입원기간: ", period, ' 일')

col5,col6 =st.columns(2)
with col5:
    option = st.selectbox('HCC 유형: ', ['1', '2','3','4'])
    st.write('HCC 유형: ', option)
with col6:
    yes = st.radio("간경화 여부: ",("yes","no"))
    if yes =='yes':
        st.write("간경화 있음.")
    else:
        st.write("간경화 없음.")

col7,col8 =st.columns(2)
with col7:
    st.write("TACE 차수: ")
    option = st.selectbox('TACE 차수: ', ['1', '2','3','4'])
    st.write('TACE 차수: ', option)
with col8:
    st.write("TACE 유형: ")
    option = st.selectbox('TACE 유형: ', ['1', '2','3','4'])
    st.write('TACE 유형: ', option)

txt = st.text_area('환자의 사정 내용을 입력하세요: ', '''
    예, 오심, 구토 있음, 발열 없음
    ''')
st.write('Sentiment:',str(txt))


if st.button('저장'):
     st.write(name, age, sex, period, option, txt)
else:
    st.write("click button!")
    







    