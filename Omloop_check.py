import pandas as pd
import streamlit as st


def check_omloop(omloop_df, planning_df):
    """
    Function checks whether 'omloopplanning' meets the required times for the set bus-planning 
    
    args:
    ----------- 
    omloop_df: DataFrame;
    Works with 'omloopplanning' xlsx file,
     
    planning_df: DataFrame;
    Works with 'Connexxion data - ....' xlsx file
    
    Returns:
    -----------
    Succes or error-list containing rows with anomalies
    """
    errors = []
    for index, omloop_row in omloop_df.iterrows():
        vertrektijd1 = omloop_row['vertrektijd']
        buslijn1 = omloop_row['buslijn']
        startlocatie1 = omloop_row['startlocatie']
        
        # Haal alleen het 'HH:MM'-deel op van vertrektijd1
        vertrektijd1_hhmm = vertrektijd1[:5]
        
        # Controleer of er minstens één overeenkomende rij is in planning_df #mogelijk nog veranderen naar precies 1
        overeenkomende_rijen = planning_df[
            (planning_df['starttijd'].str[:5] == vertrektijd1_hhmm) &
            (planning_df['buslijn'] == buslijn1) &
            (planning_df['startlocatie'] == startlocatie1)
        ]
        # print(overeenkomende_rijen)
        if overeenkomende_rijen.empty:
            errors.append(omloop_row)  # Add the row to the errors list
    
    if errors:
        st.error("Omloop-rijen die niet in de planning staan:")
        for error_row in errors:
            st.error(error_row)  # Display each error row
    else:
        st.success('The "omloopplanning" voldoet aan alles')
        

# Roep de functie aan om de controle uit te voeren (test)
# check_omloop(omloop, planning)
