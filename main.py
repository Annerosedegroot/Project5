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
from idle_time_fill_up import idle_time_fill_up
from Omloop_check import check_omloop

# Set the title of the web application
st.title("Project 5: Check the planning")

#Input file 'planning' and 'Connexxion data', and check if 'planning' meets requirements
inputfile = st.file_uploader("Choose an Excel file", type='xlsx')
if inputfile is not None:
    df = pd.read_excel(inputfile)
    formatcheck(df)
    check_activiteit(df)
    check_buslijn(df) 
    omloopnummer(df)
    datum_check(df)
    controleer_datatypes(df)
    check_time_no_difference(df)
    idle_time_fill_up(df)
    upload2 = st.file_uploader("Choose an Excel file 2", type='xlsx')
    if upload2 is not None:
        df2 = pd.read_excel(upload2, sheet_name='Dienstregeling')
        check_omloop(df2, df) 
# Lay-out app: sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


