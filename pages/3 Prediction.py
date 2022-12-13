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

st.markdown("""
    <span style ='font-size:34px; font-weight: bold;'> Predict  </span>
""", unsafe_allow_html=True)
st.image('icon01.png', width=150)

st.write("this is prediction.")
st.write("this is to apply a machine learning model. currently this model is for iris classification.")
st.write("But, I'll change a model for my nursing app, soon.")


st.write("## dataset")
data = pd.read_csv("iris.csv")
data

st.write("## model test")

model = pickle.load(open('iri.pkl','rb'))
arr = np.array([[5.9,3.0,5.0,1.8]])
st.write(arr)

pred = model.predict(arr)    


if pred == 0:
    st.write("### predict result: ... Setosa !!",  str(pred))
elif pred == 1:
    st.write("### predict result: ... Versicolor !!", str(pred))
elif pred == 2:
    st.write("### predict result: ... Virginica !!",  str(pred))