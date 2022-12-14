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
<a href ='/login' target='_self'><i class="fas fa-user-circle" style='font-size:36px;color:slategray; float:right;'></i> </a>  
                                                                                                                                                                      
'''
st.write(css_example, unsafe_allow_html=True)

#st.sidebar.markdown("# Patents Info") 

col1, col2 =st.columns(2)
with col1:
    st.write("# Nursing.")
with col2:
    st.image("medical.png", width= 100)

# text processing and text mining
# chart