import pandas as pd
import streamlit as st

def check_buslijn_column(df):
    """
    function checks whether all variables in column 'buslijn' are either 400, 401 or empty  
    arg: dataframe, excel
    output: all warnings if value is not 400, 401 of empty
    """
    # Initialize a list to store warning messages and row numbers
    warnings = []

    # Iterate through each row
    for index, row in df.iterrows():
        buslijn = str(row['buslijn']).strip()  # Convert to string and remove leading/trailing spaces

        # Check if the buslijn value is not one of the allowed values or is not a NaN value
        if (buslijn not in ('401', '400', '', '0') and 
            not pd.isna(row['buslijn']) and 
            buslijn != 'nan'):
            warnings.append(f"Row {index + 1}: Unexpected value in 'buslijn' column: {buslijn}")

    # Display warnings in Streamlit these need to go in the list with all other wanring sand errors generated from the data/
    if warnings:
        st.warning("Warning: Found unexpected values in 'buslijn' column:")
        for warning in warnings:
            st.write(warning)
    else:
        st.success("No unexpected values found in 'buslijn' column.")

uploaded = "omloop planning.xlsx" 

if uploaded is not None:
    df = pd.read_excel(uploaded)  # Load the Excel file into a DataFrame
    df['buslijn'] = df['buslijn'].astype(float).fillna(0).astype(int)
    check_buslijn_column(df)  # Pass the DataFrame to the function
