import pandas as pd
import streamlit as st

def check_buslijn(df):
    """
    Function checks whether all variables in column 'buslijn' are either 400, 401 or empty.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    Succes or warning-list containing rows with anomalies
    """
    # Initialize a list to store warning messages and row numbers
    warnings = []
    df['buslijn'] = df['buslijn'].astype(float).fillna(0).astype(int)

    # Iterate through each row
    for index, row in df.iterrows():
        buslijn = str(row['buslijn']).strip()  # Convert to string and remove leading/trailing spaces

        # Check if the buslijn value is not one of the allowed values or is not a NaN value
        if (buslijn not in ('401', '400', '', '0') and 
            not pd.isna(row['buslijn']) and 
            buslijn != 'nan'):
            warnings.append(index)

    # Display warnings in Streamlit these need to go in the list with all other wanring sand errors generated from the data/
    if warnings:
        st.warning(f'Warning: Found unexpected values in the column "buslijn" in the following rows: {warnings}.')

    else:
        st.success(f'No unexpected values found in the column "buslijn".')

# uploaded = "omloop planning.xlsx" 

# if uploaded is not None:
#     df = pd.read_excel(uploaded)  # Load the Excel file into a DataFrame
#     df['buslijn'] = df['buslijn'].astype(float).fillna(0).astype(int)
#     check_buslijn(df)  # Pass the DataFrame to the function
