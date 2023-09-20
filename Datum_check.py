import pandas as pd
import streamlit as st

def datum_check(df):
    """
    Function checks if the date is in the form %Y:%M:%D and the time in the form %H:%M:%S.
    arg: df
    output: warnings if column contains unwanted value (typo)
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

