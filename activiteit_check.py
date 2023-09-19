import pandas as pd
import streamlit as st

def check_activiteit(df):
    """
    Function checks if 'activiteit' column only contains 'idle', 'materiaal rit', 'dienst rit' or 'opladen'.
    arg: df
    output: warnings if column contains unwanted value (typo)
    
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
            warnings.append(f"Row {index + 2}: Unexpected value in 'activiteit' column: {activiteit}")

    # Display warnings in Streamlit
    if warnings:
        st.warning("Warning: Found unexpected values in 'activiteit' column:")
        for warning in warnings:
            st.write(warning)
    else:
        st.success("No unexpected values found in 'activiteit' column.")

# uploaded = "omloop_planning.xlsx"  # Replace with your Excel file path

# if uploaded is not None:
#     df = pd.read_excel(uploaded)  # Load the Excel file into a DataFrame
#     check_activiteit(df)  # Pass the DataFrame to the function
