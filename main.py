# import the necessary packages
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
from time_check_backwards import time_backwards
from KPI import sum_idle, sum_verbruik

# Set the title of the web application
st.title("Transdev Planning Checker")
st.divider()

#Input file 'planning' and 'Connexxion data', and check if 'planning' meets requirements
st.write('This tool is able to check circulation plannings for buslines 400 and 401 located in Eindhoven, the Netherlands.')
inputfile = st.file_uploader("Choose your completed circulation planning excel file", type='xlsx') # (to check if the format is correct)
issues = []
if inputfile is not None:
    df = pd.read_excel(inputfile)
    df = df.drop(['Unnamed: 0'], axis=1)
    formatcheck(df, issues)
    check_activiteit(df, issues)
    check_buslijn(df, issues) 
    omloopnummer(df, issues)
    datum_check(df)
    controleer_datatypes(df)   # Weet niet hoe ik hier success kan krijgen
    check_time_no_difference(df)
    df = idle_time_fill_up(df)
    time_backwards(df, issues)
    sum_idle(df)
    sum_verbruik(df)
    st.session_state['df'] = df
    if not issues:
        st.success(f'Success: The file is correct.')
    upload2 = st.file_uploader("Choose the excel file which contains the requirements for the planning", type='xlsx')
    issues2 = []
    if upload2 is not None:
        df2 = pd.read_excel(upload2, sheet_name='Dienstregeling')
        #check_omloop(df2, df) 





 