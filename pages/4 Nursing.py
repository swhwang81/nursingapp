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

st.markdown("# Nursing.")
#st.sidebar.markdown("# Patents Info") 

st.write("this is nursing.")

# text processing and text mining
# chart