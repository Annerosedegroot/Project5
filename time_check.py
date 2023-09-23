# Imports
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
import streamlit as st



# Function
def check_time_no_difference(df):
    """
    Check for zero time difference between start and end times in a DataFrame.

    Parameters:
    df (pd.DataFrame): A DataFrame containing 'starttijd' and 'eindtijd' columns
                       representing the start and end times of events.

    Returns:
    None: The function prints warnings for rows with zero time difference and
          a success message if no such rows are found.

    """
    # Make a dataframe from the starttijd and eindtijd only and call it time
    starting_time = df['starttijd']
    ending_time = df['eindtijd']
    time = pd.merge(starting_time, ending_time, left_index=True, right_index=True)
    
    # Create a list where warnings will be stored if the time difference = 0
    warnings = []
    
    # A forloop per row
    for index, row in time.iterrows():
        
        # Change the string from the excel file into a time Python can read
        t1 = datetime.strptime(row['starttijd'], "%H:%M:%S")
        t2 = datetime.strptime(row['eindtijd'], "%H:%M:%S")
        
        # Calculate the difference between the starting time and the ending time
        difference = t2 - t1
        
        # Make a variable which represents 0 difference in time
        no_difference = timedelta(hours=0, minutes=0, seconds=0)
        
        # Check if the difference between start and end is 0
        if difference == no_difference:
            warnings.append(index+2)
            
    if warnings:
        # If the difference is 0, create a warning
        st.warning(f'In the following rows {warnings}, the time difference is 0, meaning the bus does not drive')
        
    else:
        st.success(f'The data does not contain any busses which have a 0 minute idle time.')
        


# Test
# df = pd.read_excel("omloop planning.xlsx")  # Replace with your Excel file path

# if uploaded is not None:
#     df = uploaded)  # Load the Excel file into a DataFrame
# print(check_time_no_difference(df))