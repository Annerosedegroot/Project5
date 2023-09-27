# Imports
import pandas as pd
import streamlit as st
from row_switch_check import row_switch
from datetime import datetime, timedelta



# Function
def time_backwards(df):
    """
    Function checks Check whether bus is arriving before leaving to drive the route according to planning.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    None or error-list containing rows with anomalies
    """
    starting_time = df['starttijd datum']
    ending_time = df['eindtijd datum']
    time = pd.merge(starting_time, ending_time, left_index=True, right_index=True)
    print(time)
    
    # Create a list where warnings will be stored if the time difference = 0
    warnings = []
    
    # A forloop per row
    for index, row in time.iterrows():
        
        # Change the string from the excel file into a time Python can read
        t1 = datetime.strptime(row['starttijd datum'].strftime("%Y/%m/%d %H:%M:%S"), "%Y/%m/%d %H:%M:%S")
        t2 = datetime.strptime(row['eindtijd datum'].strftime("%Y/%m/%d %H:%M:%S"), "%Y/%m/%d %H:%M:%S")
        
        
        # Calculate the difference between the starting time and the ending time
        difference = t2 - t1
        
        # Make a variable which represents 0 difference in time
        no_difference = timedelta(hours=0, minutes=0, seconds=0)
        
        # Check if the difference between start and end is less than 0
        if difference < no_difference:
            warnings.append(index)
            
    # Create error if needed
    if warnings:
        st.error(f'In the following rows, the bus arrives at the destination before it has left the starting point: {warnings}')








# Test

df= pd.read_excel('omloop planning.xlsx')
print(time_backwards(df))




