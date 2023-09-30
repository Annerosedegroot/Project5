import pandas as pd
import streamlit as st

def omloopnummer(df, issues):
    """
    Function checks whether the max 'omloopnummer' is less or equal to 20 (max 20 busses) 
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    Succes or error with the highest 'omloopnummer'
    """
    # Controleer of de maximale waarde in de kolom kleiner dan of gelijk aan 20 is
    max_waarde = df['omloop nummer'].max()
    if max_waarde > 20:
        issues.append(1)
        st.error(f'Error: There are {max_waarde} "omloopnummers". The maximum limit is 20.')
        
    return issues


#st.success(f"De maximale waarde in de kolom omloopnummer is {max_waarde}, wat voldoet aan de voorwaarde.")
#        else:
#            st.warning()
#            f"Er is een fout opgetreden: {e}"