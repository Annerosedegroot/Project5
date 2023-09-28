import pandas as pd
import streamlit as st

def datum_check(df):
    """
    Function checks if the date in 'starttijd datum' is of format %Y:%M:%D and the time in the form %H:%M:%S.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    Succes or error-list containing rows with anomalies
    """
    try:
        # Check if the starting date and time is in the correct form
        df['starttijd datum'] = pd.to_datetime(df['starttijd datum'], format='%Y/%M/%D /%H/%M/%S', errors='coerce') # 'errors=coerce' ignores incorrect dates

        # Check if there are incorrect dates/times
        if df['starttijd datum'].isnull().any():
            st.warning(f"Fout: There are incorrect dates or times '{'starttijd datum'}'.")
        else:
            st.success("The date and time is correct.")

    except Exception as e:
        st.error(f"There is a mistake: {e}")

