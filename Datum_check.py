import pandas as pd
import streamlit as st
        
def datum_check(df):
    """
    Function checks if the date is in the form %Y:%M:%D and the time in the form %H:%M:%S.
    
    args: 
    ------
    df
    
    Returns: 
    ------
    warnings if column contains unwanted value (typo)
    """ 
    
    starttijd_datum = pd.to_datetime(df['starttijd datum'], format='%Y/%m/%d %H:%M:%S', exact=True)
    eindtijd_datum = pd.to_datetime(df['eindtijd datum'], format='%Y/%m/%d %H:%M:%S', exact=True)
    
    starttijd = pd.to_datetime(df['starttijd'], format='%H:%M:%S', exact=True)
    eindtijd = pd.to_datetime(df['eindtijd'], format='%H:%M:%S', exact=True)
    
    return starttijd_datum, eindtijd_datum, starttijd, eindtijd

        
# Test
df = pd.read_excel("omloop planning.xlsx")  # Replace with your Excel file path

# if uploaded is not None:
#     df = uploaded)  # Load the Excel file into a DataFrame
datum_check(df)