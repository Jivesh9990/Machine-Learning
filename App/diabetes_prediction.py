import streamlit as st
import os
import pickle
import numpy as np

model = None
model_path = 'models/diabetes_model.pk'
if os.path.exists(model_path):
    with open(model_path,'rb') as f:
        model = pickle.load(f)
    st.sidebar.success('Diabetes model loaded')

st.header("Diabetes Prediction")
BP= st.number_input('BloodPressure',50)
Glucose= st.number_input('Glucose',100)
Insulin=st.number_input('Insulin',0)
btn = st.button("Click here to check")

if btn:
    if model:
        inp = np.array([[BP,Glucose,Insulin]])
        out = model.predict(inp)[0]
        st.success(out)
    else:
        st.error('Model not working')