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


st.markdown("# Home")
#st.sidebar.markdown("# Home")

#st.header("간호 사정 예측 앱")
st.write("this is home.")

st.markdown("""
    <a href ='/Tutorial' target='_self'>click to tutorial </a><br>
    <a href="javascript:alert('Hello World!');" target='_self'>Execute JavaScript</a>
""", unsafe_allow_html=True)

#components.iframe("https://swhwang81-streamlitapp-app-7uz08y.streamlit.app/")

