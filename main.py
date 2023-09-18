# import the necessary packages
import math  # For mathematical functions
import pandas as pd  # For working with data frames
import streamlit as st  # For creating a web application
from Format_excel_checks import formatcheck

# Set the title of the web application
st.title("Project 5: Check the planning")

# Planning in app zetten
inputfile = st.file_uploader("Choose an Excel file", type='xlsx')
if inputfile is not None:
    df = pd.read_excel(inputfile)
    formatcheck(df)
# Lay-out app: sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

