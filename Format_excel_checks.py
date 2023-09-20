import pandas as pd
import streamlit as st
def formatcheck(df):
    """
    Check if the columns are present.
    Check if the order of the columns is correct. 
    """
    columnlist = ["startlocatie","eindlocatie","starttijd","eindtijd","activiteit","buslijn","energieverbruik","starttijd datum","eindtijd datum","omloop nummer"] #List of all the column titles
    for i in columnlist: #For loop to check if there are any missing columns in the input file
        if i not in df.columns:
            st.error(f"Column {i} is missing.")
    
    for i in columnlist: #For loop to check if the order of the columns is correct.
        if columnlist[columnlist.index(i)] != df.columns[columnlist.index(i)+1]:
            st.error(f"Order of columns is not as expected.")

    