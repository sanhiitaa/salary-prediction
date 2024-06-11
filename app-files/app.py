import streamlit as st
import pickle
import numpy as np
import pandas as pd

# load trained model
pipe=pickle.load(open('app-files/final-pipeline-salary-prediction.pkl', 'rb'))

# app title
st.title('Salary Prediction App')


# getting user input
sex = st.selectbox('Gender', ['F', 'M'])
designation = st.selectbox('Designation', ['Analyst', 'Associate', 'Senior Analyst', 'Manager', 'Senior Manager', 'Director'])
unit = st.selectbox('Unit', ['Marketing', 'Finance', 'Web', 'IT', 'Operations'])
past_exp= st.number_input('Past Experince (in years)', min_value=0, step=1)
years_experience = st.number_input('Experience in current company (in years)', min_value=0, step=1)

# predict button
if st.button('Predict Salary!'):
    input_data = pd.DataFrame({'SEX' : [sex],
                              'DESIGNATION' : [designation],
                              'UNIT' : [unit],
                              'PAST EXP' : [past_exp],
                              'years_experience' : [years_experience]})
    
    
    prediction = pipe.predict(input_data)

    st.write(f'Predicted Salary: ${prediction[0]:.2f}')
