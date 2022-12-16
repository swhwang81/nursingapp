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
st.write("this is to apply a machine learning model. currently this model is for iris classification.")
st.write("But, I'll change a model for my nursing app, soon.")

tab1, tab2, tab3 = st.tabs(['1.dataset','2.test_data','3.result'])

with tab1:
    st.write("## dataset")
    data = pd.read_csv("iris_data.csv")
    data

with tab2:
    st.write("## model test")

    model = pickle.load(open('iri_rf.pkl','rb'))
    arr = np.array([[5.1,3.5,1.4,0.2]])
    st.write(arr)

with tab3:
    
    pred = model.predict(arr)    


    if pred == 0:
        st.write("### predict result: Setosa !!",  str(pred[0]))
    elif pred == 1:
        st.write("### predict result: Versicolor !!", str(pred[0]))
    elif pred == 2:
        st.write("### predict result: Virginica !!",  str(pred[0]))