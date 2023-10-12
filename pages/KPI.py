import streamlit as st  # For creating a web application
import pandas as pd
from datetime import datetime, timedelta
import streamlit as st
import numpy as np

def sum_verbruik(df): 
    """
    Function calculates total verbruik in given planning
    
    Arg:
    -------
    df
    
    Returns:
    ---------
    sum of all energyusage in planning
    """
    
    totaal_verbruik = df[df['energieverbruik'] > 0]['energieverbruik'].sum()

    return totaal_verbruik

def sum_idle(df):
    times = []
    for index, row in df.iterrows():
        starttijd_str = row['starttijd']
        eindtijd_str = row['eindtijd']

        starttijd = datetime.strptime(starttijd_str, '%H:%M:%S').time()
        eindtijd = datetime.strptime(eindtijd_str, '%H:%M:%S').time()

        time_difference = timedelta(
            hours=eindtijd.hour - starttijd.hour,
            minutes=eindtijd.minute - starttijd.minute,
            seconds=eindtijd.second - starttijd.second
        )
        times.append(time_difference)

    df['tijd'] = times  # Voeg de berekende tijdsverschillen toe aan de DataFrame in de 'tijd' kolom

    # Converteer de 'tijd' kolom naar het aantal minuten (integer)
    df['tijd'] = df['tijd'].apply(lambda x: x.seconds // 60)

    # Filter rijen waar 'activiteit' gelijk is aan 'idle time'
    idle_rows = df[df['activiteit'] == 'idle']

    # Sommeer de waarden in de 'tijd' kolom om de totale idle time in minuten te krijgen
    total_idle_minutes = idle_rows['tijd'].sum()  # Verschil in minuten

    return total_idle_minutes

def kpis(df):
    """
    Function which contains all the functions for the KPI's

    Arg:
    -------
    df
    
    Returns:
    ---------
    Total energy usage and the total minutes idle time
    """
    total_idle_minutes = sum_idle(df)
    totaal_verbruik = sum_verbruik(df)
    return totaal_verbruik, total_idle_minutes

st.title('KPI metrics')
st.divider()
df = st.session_state['df']
totaal_verbruik, totaal_idle = kpis(df)
col1, col2 = st.columns(2)
col1.metric('Total energy usage in current uploaded planning', totaal_verbruik)
col2.metric('Total idle time in current uploaded planning', totaal_idle)

