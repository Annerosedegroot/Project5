# Imports
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
import streamlit as st

def check_time_no_difference(df):
    """
    Function checks for zero time difference between start and end times in a DataFrame.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    Succes or error-list containing rows with anomalies
    """ 
    
    # df2 = df.copy()
    # Make a dataframe from the starttijd and eindtijd only and call it time
    starting_time = df['starttijd']
    ending_time = df['eindtijd']
    time = pd.merge(starting_time, ending_time, left_index=True, right_index=True)
    
    # Create a list where warnings will be stored if the time difference = 0
    warnings = []
    
    # A forloop per row
    for index, row in time.iterrows():
        
        # Change the string from the excel file into a time Python can read
        t1 = datetime.strptime(str(row['starttijd']), "%H:%M:%S")
        t2 = datetime.strptime(str(row['eindtijd']), "%H:%M:%S")
        
        # Calculate the difference between the starting time and the ending time
        difference = t2 - t1
        
        # Make a variable which represents 0 difference in time
        no_difference = timedelta(hours=0, minutes=0, seconds=0)
        
        # Check if the difference between start and end is 0
        if difference == no_difference:
            warnings.append(index)

            

    df = df.drop(warnings)
    df.reset_index(drop=True, inplace=True)

    return df
        



# Test
# df = pd.read_excel("omloop planning.xlsx")  # Replace with your Excel file path

# if uploaded is not None:
#     df = uploaded)  # Load the Excel file into a DataFrame
# print(check_time_no_difference(df))