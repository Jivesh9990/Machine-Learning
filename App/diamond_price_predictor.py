import streamlit as st
import os
import pickle
import numpy as np

model = None
model_path = 'models/diamond_price_model.pk'
if os.path.exists(model_path):
    with open(model_path,'rb') as f:
        model = pickle.load(f)
    st.sidebar.success('Diamong Pricing model loaded')

st.header("Diamond price prediction")
paleonium= st.number_input('Paleonium',100)
pressure= st.number_input('Pressure',5000)
btn = st.button("Click to get aprrox pricing of diamonds")

if btn:
    if model:
        inp = np.array([[paleonium,pressure]])
        out = model.predict(inp)[0]
        st.success(f'Diamond approx cost is $ {out:.1f} only')
    else:
        st.error('Model not working')