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


#st.sidebar.markdown("# Tutorial")
css_example = '''  
                                                                                                                                                   
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                                                                                                                                                                                                                              
<a href ='/' target='_self'><i class="fas fa-home" style='font-size:36px;color:slategray;'></i> </a>   
<a href ='/login' target='_self'><i class="fas fa-user-circle" style='font-size:36px;color:slategray; float:right;'></i> </a>  
                                                                                                                                                                      
'''
st.write(css_example, unsafe_allow_html=True)
st.markdown("# Tutorial")

# for ppt display !
st.markdown("""
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT5FBGDR4azhOdSD_JIGGHIB7o-WNQjjfw_8uAaJeVrixU0cjQdpzhRwBWJ_KEs9bOkjoTA5lyHS0pf/embed?start=false&loop=false&delayms=3000" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true" style="height:500px;width:500px;></iframe>
""",unsafe_allow_html=True)
