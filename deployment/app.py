import streamlit as st
import eda
import prediction

navigation = st.sidebar.selectbox('Move me to this page:', ['Exploratory Data Analysis', 'Model Prediction'])

if navigation == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()