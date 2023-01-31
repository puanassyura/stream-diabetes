import pickle
import streamlit as st
import base64
import numpy as np


# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# judul web
st.title('PREDIKSI DIABETES')
# bagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Pregnancies')
    Glocouse = st.text_input('Glocouse')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness')
with col2:
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')

    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age')

# code untuk prediksi
diab_diagnosis = ''

# tombol
if st.button("Test Prediksi Diabetes"):
    diab_prediction = diabetes_model.predict(
        [[Pregnancies, Glocouse, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
    st.success(diab_diagnosis)
