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
from oplaadtijd import oplaadtijd

def checks(df, issues):
    """
    Function which contains all the functions to check the circulation planning
    
    Arg:
    -------
    df, issues
    
    Returns:
    ---------
    The errors and warning found if there are mistakes in the circulation planning
    """
    formatcheck(df, issues)
    check_activiteit(df, issues)
    check_buslijn(df, issues)
    omloopnummer(df, issues)
    datum_check(df)
    controleer_datatypes(df)   # Weet niet hoe ik hier success kan krijgen
    check_time_no_difference(df)
    time_backwards(df, issues)
    oplaadtijd(df, issues)
    return issues
    
df = pd.read_excel('omloop planning.xlsx')

# Set the title of the web application
st.title("Transdev Planning Checker")
st.divider()

#Input file 'planning' and 'Connexxion data', and check if 'planning' meets requirements
st.write('This tool is able to check circulation plannings for buslines 400 and 401 located in Eindhoven, the Netherlands.')
inputfile = st.file_uploader("Choose your completed circulation planning excel file", type='xlsx') # (to check if the format is correct)
issues = []
if inputfile is not None:
    df = pd.read_excel(inputfile)
    columnnames = df.columns.to_list()
    if 'Unnamed: 0' in columnnames:
        df = df.drop(['Unnamed: 0'], axis=1)
        st.session_state['df'] = df
        checks(df, issues)
        
    else:
        checks(df, issues)
        st.session_state['df'] = df
    


    #df.to_excel("Test2.xlsx")
    df_new = df.copy()  # A new dataframe such that the old one doesn't get overwritten when it is still needed.
    df_new = idle_time_fill_up(df_new)

    st.session_state['df_new'] = df_new
    
    if not issues:
        st.success(f'Success: The file is correct.')
    upload2 = st.file_uploader("Choose the excel file which contains the requirements for the planning", type='xlsx')
    issues2 = []
    if upload2 is not None:
        df2 = pd.read_excel(upload2, sheet_name='Dienstregeling')
        check_omloop(df2, df, issues2) 
        st.success(f'Success: The file is correct.')


#Reminder Teun Datum checks schrijft alle tijden uit!!!


 