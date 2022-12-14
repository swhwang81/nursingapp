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
<a href ='/' target='_self'><i class="fas fa-home" style='font-size:36px; color:slategray;'></i> </a>   
<a href ='/login' target='_self'><i class="fas fa-user-circle" style='font-size:36px; color:slategray; float:right;'></i> </a>  
                                                                                                                                                                      
'''
st.write(css_example, unsafe_allow_html=True)
st.write("# Home")


st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">  
    <style>
    ul {
       list-style-type: none;
        margin: 0;
        padding: 0; 
    }
    li.a {
        display: inline-block; 
        width: 80%;
        height: 200px;
        padding: 5px;
        padding-top:50px;
        margin: 10px;
        border: 3px solid slategray; 
        border-radius: 15px;
        font-size: 100px;
        color:slategray;
        text-align: center;
    }
    span.menu {
        display:block;
        font-size:10px;
        color:black;
    }
    </style>
    <center>
    <ul>                                                                                                                                                                                                                                                                                                           
    <a href ='/Tutorial' target='_self'><li class="fas fa-chalkboard a"><span class="menu">Tutorial</span></li> </a><br>
    <a href ='/Patents' target='_self'><li class="fas fa-plus-square a" ><span class="menu">Patents Info.</span></li> </a><br>
    <a href ='/Prediction' target='_self'><li class="far fa-lightbulb a" ><span class="menu">Prediction</span></li> </a><br>
    <a href ='/Nursing' target='_self'><li class="far fa-heart a"><span class="menu">Nursing</span></li> </a><br>
    <a href ='/History' target='_self'><li class="far fa-folder-open a"><span class="menu">Nursing History</span></li> </a><br>
    <a href ='/MyPage' target='_self'><li class="far fas fa-cog a"><span class="menu">My Page</span></li> </a><br>
    <a href ='/Q&A' target='_self'><li class="fas fa-question a"><span class="menu">Q&A</span></li> </a><br>
    <a href="javascript:alert('Hello World!');" target='_self'>Execute JavaScript</a>
    </ul>
    </center>
""", unsafe_allow_html=True)


