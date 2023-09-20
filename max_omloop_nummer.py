import pandas as pd
import streamlit as st

def omloopnummer(df):
    try:
        # Controleer of de maximale waarde in de kolom kleiner dan of gelijk aan 20 is
        max_waarde = df['omloopnummer'].max()

        if max_waarde <= 20:
            st.success(f"De maximale waarde in de kolom '{'omloopnummer'}' is {max_waarde}, wat voldoet aan de voorwaarde.")
        else:
            st.warning(f"Fout: De maximale waarde in de kolom '{'omloopnummer'}' is {max_waarde}. Deze waarde overschrijdt de limiet van 20.")
    except Exception as e:
        st.error(f"Er is een fout opgetreden: {e}")
