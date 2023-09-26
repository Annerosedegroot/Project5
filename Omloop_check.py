import pandas as pd
import streamlit as st

# Lees het 'Connexxion data - 2023-2024.xlsx' Excel-bestand, dit is de omloopplanning waar de planning aan MOET voldoen
omloop = pd.read_excel('Connexxion data - 2023-2024.xlsx', sheet_name='Dienstregeling')

# Lees het 'omloop planning.xlsx' Excel-bestand (gemaakte planning)
planning = pd.read_excel('omloop planning.xlsx') 


def check_omloop(omloop_df, planning_df):
    """
    checks the mandatory times-buses etc. (deze checks of de gemaakte planning voldoet aan de omloop maar is moeilijk te vertalen)
    
    Arg
    ----------
    omloop_df: xlsx
    Planning waaraan moet worden voldaan
    
    planning_df: xlsx
    Gemaakte planning die gecontroleerd wordt.
    
    Returns:
    -----------
    Either nothing when planning meets requirments
    or the row, time and place of the omloop_df that's not in planning_df
    
    """
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

    if overeenkomende_rijen.empty:
        st.error(f"Omloop-rij die niet in de planning staat:\n{omloop_row}")
    else:
        st.success(f'The "omloopplanning" voldoet aan alles')
        

# Roep de functie aan om de controle uit te voeren (test)
#check_omloop(omloop, planning)
