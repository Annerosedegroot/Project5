# Imports
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
from row_switch_check import row_switch


# Function
def time_overlap_check(df, issues):
    """
    Function checks whether the bus is arriving before leaving for the next 'omloop' route.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    Is there a return here or was this just for testing purposes?
    """     
    
    
    starting_time = df['starttijd']
    ending_time = df['eindtijd'].shift(periods = 1, fill_value = '00:00:00')
    time = pd.merge(starting_time, ending_time, left_index=True, right_index=True)

    
    # Create a list where warnings will be stored if the time difference = 0
    errors = []
    
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
        if difference != no_difference:
            errors.append(index)
            
    if errors:
        issues.append(1)
        st.error(f'Error: The time is incorrect in the following rows: {errors}')
    
    # Make excel file of copied dataframe to check
    # df_copy.to_excel("omloop planning test.xlsx")
    
    return df, issues
        



# Test
df = pd.read_excel("omloop planning.xlsx")  # Replace with your Excel file path

print(time_overlap_check(df))