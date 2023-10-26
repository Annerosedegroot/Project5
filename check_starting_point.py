import pandas as pd
from time_check import check_time_no_difference
import streamlit as st


def start_vs_end_point(df, issues):
    df = check_time_no_difference(df)
    success = 0
    errors = []
    for i in range(len(df)-1):
        if df.loc[i, 'omloop nummer'] == df.loc[i+1, 'omloop nummer']:
            if df.loc[i, 'eindlocatie'] == df.loc[i+1, 'startlocatie']:
                success += 1
            elif df.loc[i, 'eindlocatie'] != df.loc[i+1, 'startlocatie']:
                errors.append(i)
    
    if errors:
        issues.append(1)
        st.error(f'Error: The bus is leaving a station which is not the destination of the drive before. {errors}')
        
    return df, issues
