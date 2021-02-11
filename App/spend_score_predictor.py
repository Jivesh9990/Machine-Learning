import streamlit as st
import os
import pickle
import numpy as np

model = None
model_path = 'models/spend_score_model.pk'
if os.path.exists(model_path):
    with open(model_path,'rb') as f:
        model = pickle.load(f)
    st.sidebar.success('Spend Score model loaded')

income = st.number_input('Annual Income',10000)
age = st.number_input('Age',24)
gender= st.radio('Select the gender',['Male',"Female"])

btn = st.button('Calculate spend score')

if btn:
    if isinstance(model,dict):
        gval = model['gender_encoder'].transform(np.array([gender]))
        x = np.array([[gval[0],age,income]])
        x = model['scaler'].transform(x)
        out = model['model'].predict(x)[0]
        st.header(f'the spend score {out:.2f}')