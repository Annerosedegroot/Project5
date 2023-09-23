# Imports
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta


# Function
def time_overlap_check(df):
    starting_time = df['starttijd']
    ending_time = df['eindtijd'].shift(periods = 1, fill_value = '00:00:00')
    time = pd.merge(starting_time, ending_time, left_index=True, right_index=True)
    # time = time['eindtijd'].shift(periods=1, fill_value = 0)
    # time = pd.DataFrame(time)
    print(time)
    
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
        if difference != no_difference:
            warnings.append(index)
            
    print(warnings)
        



# Test
df = pd.read_excel("omloop planning.xlsx")  # Replace with your Excel file path

print(time_overlap_check(df))