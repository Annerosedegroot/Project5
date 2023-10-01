import pandas as pd
import streamlit as st


def check_omloop(omloop_df, planning_df, issues2):
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
            errors.append(index)  # Add the row to the errors list
    
    if errors:
        st.error(f'The following "Omloop-rijen" are not in the planning: {index}.')
        issues2.append(1)
        
    return issues2

        # for error_row in errors:
        #     st.error(error_row)  # Display each error row
    # else:
    #     st.success('The "omloopplanning" is correct.')
    
        

# Roep de functie aan om de controle uit te voeren (test)
# check_omloop(omloop, planning)
