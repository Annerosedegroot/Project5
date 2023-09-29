import pandas as pd
import streamlit as st

def check_activiteit(df):
    """
    Function checks if 'activiteit' column solely contains 'idle', 'materiaal rit', 'dienst rit' or 'opladen'.
    
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

    # Define the allowed values for the 'activiteit' column
    allowed_values = ['idle', 'materiaal rit', 'dienst rit', 'opladen']

    # Iterate through each row
    for index, row in df.iterrows():
        activiteit = str(row['activiteit']).strip()  # Convert to string and remove leading/trailing spaces

        # Check if the 'activiteit' value is not one of the allowed values
        if activiteit not in allowed_values:
            warnings.append(index)

    # Display warnings in Streamlit
    if warnings:
        st.warning(f'Warning: The following rows contain unexpected data: {warnings}.')
        
    # else:
    #     st.success(f'No unexpected values found in the column "activiteit".')

# uploaded = "omloop planning.xlsx"  # Replace with your Excel file path

# if uploaded is not None:
# df = pd.read_excel(uploaded)  # Load the Excel file into a DataFrame
# check_activiteit(df)  # Pass the DataFrame to the function
