import streamlit as st
import pandas as pd
import numpy as np
import pickle
import streamlit.components.v1 as components  # Import Streamlit
import mysql.connector

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


st.write("# Nursing.")


# text processing and text mining

@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT title from topic;")

# Print results.
for row in rows:
    #st.write(f"{row[0]} has a :{row[1]}:")
    st.write(f"{row[0]} !")