import streamlit as st 
import pandas as pd
import numpy as np
import pickle 
ohe=pickle.load(open('ohecancer.pkl','rb'))
rfc=pickle.load(open('rfccancer.pkl','rb'))
df=pickle.load(open('Thyroid_Diff.pkl','rb'))
st.title("Thyroid Cancer Recurred Prediction")
st.sidebar.image("th.jpg", caption="Thyroid Cancer", use_column_width=True)
description = """
About 98.5% of people with thyroid cancer will survive for at least 5 years. However, survivors of this disease have an increased risk 
of developing another cancer, and about 20% are at risk of a thyroid cancer recurrence.
Some people have a higher risk
Trusted Source of thyroid cancer recurrence. Factors that can increase the risk of a recurrence include:

*being over 45 years of age at diagnosis
*having had cancer that spread beyond the thyroid
*being male
*having certain tumor genes
"""
st.sidebar.markdown(description)
Age=st.selectbox('Select Age',df['Age'].unique())
Gender=st.selectbox('Select Gender',df['Gender'].unique())
Smoking=st.selectbox("Do you smoke?",df['Smoking'].unique())
Hx_Smoking=st.selectbox("Have you ever smoked in the past?",df['Hx Smoking'].unique())
Hx_Radiothreapy=st.selectbox("Have you ever done Radiotherapy?",df['Hx Radiothreapy'].unique())	
Thyroid_Function=st.selectbox("Thyroid Functioin",df['Thyroid Function'].unique())	
Physical_Examination=st.selectbox("Physical Examination",df['Physical Examination'].unique())
Adenopathy=st.selectbox("Adenopathy",df['Adenopathy'].unique())
Pathology=st.selectbox("Pathology",df['Pathology'].unique())
Focality=st.selectbox("Focality",df['Focality'].unique())
Risk=st.selectbox("Risk",df['Risk'].unique())
T=st.selectbox("T",df['T'].unique())
N=st.selectbox("N",df['N'].unique())
M=st.selectbox("M",df['M'].unique())
Stage=st.selectbox("Which cancer stage you have been at",df['Stage'].unique())
Response=st.selectbox("Response",df['Response'].unique())


if st.button("Predict"):
    new_df=pd.DataFrame([{
    
    'Age':Age,
    'Gender':Gender,
    'Smoking':Smoking,
    'Hx Smoking':Hx_Smoking,
    'Hx Radiothreapy':Hx_Radiothreapy,
    'Thyroid Function':Thyroid_Function,
    'Physical Examination':Physical_Examination,
    'Adenopathy':Adenopathy,
    'Pathology':Pathology,
    'Focality':Focality,
    'Risk':Risk,
    'T':T,
    'N':N,
    'M':M,
    'Stage':Stage,
    'Response':Response}
    
    ])

    encoded_df=ohe.transform(new_df)
    prediction=rfc.predict(encoded_df)
    if prediction[0] ==0:
        st.write("No")
    else:
        st.write("Yes")
        
