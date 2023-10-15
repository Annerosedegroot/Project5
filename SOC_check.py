import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_excel("omloop planning.xlsx")
df = df.drop(['Unnamed: 0'], axis=1)

def SOC_check(df):
    """
    Function checks if there is a moment wen the State of Charge is violated    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    -----------
    Succes or error-list containing rows with anomalies
    """
        
    original_capacity = 300
    SOH = 0.85 
    SOC = 0.1

    df['accu'] = np.zeros(len(df))
    omloopnummer = []
    accu = original_capacity * SOH
    for i in range(len(df)):
        if df.iloc[i,9] in omloopnummer:
            df.iloc[i,10] = df.iloc[i-1,10] - df.iloc[i,6]  # A new column gets added with the accu capacity for a moment
        else:
            df.iloc[i,10] = accu - df.iloc[i,6]
            omloopnummer.append(i)   

    SOC_warning = []      
    bool_SOC = df.iloc[:,10].lt(accu * SOC).to_list()
    for i in range(len(bool_SOC)):
        if bool_SOC[i] == 1:
            if df.iloc[i, 9] == df.iloc[i+1, 9]: #If statement dat afdwingt dat het om hetzelfde omloop nummer gaat.
                if df.iloc[i,4] == 'dienst rit' and df.iloc[i+1,4] == 'dienst rit':
                    SOC_warning.append(f'Warning: In row {i} the SOC gets violated.') # If a circulation numbers accu is less full than the SOC a warning is put out.

                elif df.iloc[i,4] == 'materiaal rit' and df.iloc[i+1,4] != 'idle' and df.iloc[i+1,4] != 'opladen':
                    SOC_warning.append(f'Warning: In row {i} the SOC gets violated.') #If a circulation numbers accu is less full than the SOC a warning is put out
                    continue

    return SOC_warning