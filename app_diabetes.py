import pickle
with open("model_pickle","rb") as f:
  model= pickle.load(f)

import streamlit as st
st.title('Diabetes Prediction App')
a=st.number_input("Pregnancies")
b=st.number_input("Glucose")
c=st.number_input("BloodPressure")
d=st.number_input("Skin_Thickness")
e=st.number_input("Insulin")
f=st.number_input("BMI")
g=st.number_input("Diabetes_Pedigree_Function")
h=st.number_input("Age")
prediction=model.predict([[a,b,c,d,e,f,g,h]])
button_pressed=st.button("Predict")
if button_pressed:
    if prediction[0]==0:

        st.write("You don't have diabetes")
    else:
        st.write("You have diabetes")