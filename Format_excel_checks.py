import pandas as pd
import streamlit as st

def formatcheck(df, issues):
    """
    Function checks if the input file is of the correct format/contains the right columns.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    Succes or error-list containing rows with anomalies
    """
    errors = []
    columnlist = ["startlocatie","eindlocatie","starttijd","eindtijd","activiteit","buslijn","energieverbruik","starttijd datum","eindtijd datum","omloop nummer"] #List of all the column titles
    for i in columnlist: #For loop to check if there are any missing columns in the input file
        if i not in df.columns:
            errors.append(i)
        
    if errors:    
        issues.append(1)
        st.error(f'Error: The following columns are missing: {errors}')
    
    for i in columnlist: #For loop to check if the order of the columns is correct.
        if columnlist[columnlist.index(i)] != df.columns[columnlist.index(i)]:
            st.error(f"Order of columns is not as expected.")
            
    
    return issues