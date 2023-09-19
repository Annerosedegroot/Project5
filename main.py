# import the necessary packages
import math  # For mathematical functions
import pandas as pd  # For working with data frames
import streamlit as st  # For creating a web application
from Format_excel_checks import formatcheck
from buslijn_check import check_buslijn
from activiteit_check import check_activiteit

# Set the title of the web application
st.title("Project 5: Check the planning")

# Planning in app zetten
inputfile = st.file_uploader("Choose an Excel file", type='xlsx')
if inputfile is not None:
    df = pd.read_excel(inputfile)
    formatcheck(df)
    df['buslijn'] = df['buslijn'].astype(float).fillna(0).astype(int)
    check_buslijn(df)  #check buslijn
    check_activiteit(df) #check áctiviteit
# Lay-out app: sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

