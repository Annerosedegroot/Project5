# Imports
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta


# Function
def row_switch(df):
    """
    Function checks whether the time is in the correct order and if not, changes the data in a copied dataframe.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    """
    time_1 = df['eindtijd']
    time_2 = df['eindtijd'].shift(periods = 2, fill_value = '00:00:00')
    time = pd.merge(time_1, time_2, left_index=True, right_index=True)
    # print(time)
    
    mistake = []
    df_copy = df.copy()
    
    for index, row in time.iterrows():
        
        # Change the string from the excel file into a time Python can read
        t1 = datetime.strptime(row['eindtijd_x'], "%H:%M:%S")
        t2 = datetime.strptime(row['eindtijd_y'], "%H:%M:%S")
        
        # Calculate the difference between the starting time and the ending time
        difference = t2 - t1
        # print(index, difference)
        
        # Make a variable which represents 0 difference in time
        no_difference = timedelta(hours=0, minutes=0, seconds=0)
        
        if difference == no_difference:
            mistake.append(index)
            
    for i in mistake:
        if i > 0:
            df_copy.iloc[i], df_copy.iloc[i-1] = df_copy.iloc[i-1], df_copy.iloc[i]
    # print(df_copy[30:40]) # Even een voorbeeld als check
    # return df_copy



# Test

# df = pd.read_excel("omloop planning.xlsx")
# print(row_switch(df))

