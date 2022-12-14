import streamlit as st
import pandas as pd
import numpy as np
import pickle
import streamlit.components.v1 as components  # Import Streamlit
import datetime

##remove a streamlit default header list########
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
################################################
css_example = '''  
                                                                                                                                                   
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                                                                                                                                                                                                                              
<a href ='/' target='_self'><i class="fas fa-home" style='font-size:36px;color:slategray;'></i> </a>   
<a href ='/login' target='_self'><i class="fas fa-user-circle" style='font-size:36px;color:slategray; float:right;'></i> </a>  
                                                                                                                                                                      
'''
st.write(css_example, unsafe_allow_html=True)
st.markdown("# Patents")
#st.sidebar.markdown("# Patents Info") 


# input widgets and database usages
st.write("1 ~ 3 탭의 환자 정보를 입력하세요.")

tab1, tab2, tab3 = st.tabs(['1.인적사항','2.수술전후 사항','3.그 외'])
with tab1:
   
    #이름 
    name = st.text_input('① 이름: ', '홍길동')
    st.write('이름: ', name)
    #성별
    sex = st.selectbox('② 성별: ', ['남성', '여성'])
    st.write('성별: ', sex)
    #나이
    age = st.slider('③ 나이', 0, 110, 25)
    st.write("나이: ", age, ' 세')
    #입원날짜
    today = datetime.date.today()
    d = st.date_input("④ 입원날짜: ",today)
    st.write("입원날짜: ",d)
    period = abs(today - d)
    st.write("기간: ", period.days)

with tab2:
    #HCC 유형
    option = st.selectbox('⑤ HCC 유형: ', ['1', '2','3','4'])
    st.write('HCC 유형: ', option)
    #간경화 여부
    yes = st.radio("⑥ 간경화 여부: ",("yes","no"))
    if yes =='yes':
        st.write("간경화 있음.")
    else:
        st.write("간경화 없음.")
    #TACE 차수
    st.write("⑦ TACE 차수: ")
    option = st.selectbox('TACE 차수: ', ['1', '2','3','4'])
    st.write('TACE 차수: ', option)
    #TACE 유형
    st.write("⑧ TACE 유형: ")
    option = st.selectbox('TACE 유형: ', ['1', '2','3','4'])
    st.write('TACE 유형: ', option)
    
with tab3:
    #환자 사정
    txt = st.text_area('⑨ 환자의 사정 내용을 입력하세요: ', '''
        예, 오심, 구토 있음, 발열 없음
        ''')
    st.write('Sentiment:',str(txt))

#st.write("⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ㉑ ㉒ ㉓ ㉔")

if st.button('저장'):
     st.write(name, age, sex, period, option, txt)
else:
    st.write("click button!")
    







    