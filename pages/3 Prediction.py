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
# for pickle and model usages

#st.markdown("""
#    <span style ='font-size:34px; font-weight: bold;'> Predict  </span>
#""", unsafe_allow_html=True)

st.write("# Prediction")

st.write("this is prediction.")


st.write("## dataset")
data = pd.read_csv("nurse_selected.csv")
data

st.write("## model test")
model = pickle.load(open('nurse.pkl','rb'))
arr = np.array([[0.41,0.021,-0.29,-0.11,1.5,0.2,0.,1.,0.,1.01,0.14,0.25]])
st.write(arr)
    
pred = model.predict(arr)    

st.write(pred)