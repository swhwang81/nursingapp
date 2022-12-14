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

css_example = '''                                                                                                                                                     
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                                                                                                                                                                                                                              
<a href ='/' target='_self'><i class="fas fa-home" style='font-size:36px;color:slategray;'></i> </a>                                                                                                                                                                         
'''
st.write(css_example, unsafe_allow_html=True)
st.header("Login")

with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
    
    