# import the necessary packages
import math  # For mathematical functions
import pandas as pd  # For working with data frames
import streamlit as st  # For creating a web application
from Format_excel_checks import formatcheck
from buslijn_check import check_buslijn
from activiteit_check import check_activiteit
from max_omloop_nummer import omloopnummer
from Datum_check import datum_check
from datatype_check import controleer_datatypes
from time_check import check_time_no_difference

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
    omloopnummer(df)
    datum_check(df)
    controleer_datatypes(df)
    check_time_no_difference(df)
# Lay-out app: sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

