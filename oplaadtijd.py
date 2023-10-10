import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st


def oplaadtijd(df, issues):

    errors = []
    opladen = df[df['activiteit'] == 'opladen']
    
    tijd = opladen[['starttijd', 'eindtijd']]
    # print(tijd)
    
    for index, row in tijd.iterrows():
        t1 = datetime.strptime(row['starttijd'], "%H:%M:%S")
        t2 = datetime.strptime(row['eindtijd'], "%H:%M:%S")
        
        difference = t2 - t1
        min_time = timedelta(hours=0, minutes=15, seconds=0)
        
        if difference < min_time:
            errors.append(index)
            
    if errors:
        st.error(f'The following rows contain a charging time less than 15 minutes: {errors}')
        issues.append(1)
        
    return issues
        
    
    
    
# issues = 0    
# df = pd.read_excel('omloop planning.xlsx')
# print(oplaadtijd(df, issues))