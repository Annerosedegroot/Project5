# import the necessary packages
import math  # For mathematical functions
import pandas as pd  # For working with data frames
import streamlit as st  # For creating a web application

# Set the title of the web application
st.title("Project 5: Check the planning")

# Planning in app zetten
inputfile = st.file_uploader("Choose an Excel file", type='xlsx')
df = pd.read_excel(inputfile)
# Lay-out app: sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)





