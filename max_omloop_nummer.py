import pandas as pd
import streamlit as st

def omloopnummer(df):
    # Controleer of de maximale waarde in de kolom kleiner dan of gelijk aan 20 is
    max_waarde = df['omloop nummer'].max()
    if max_waarde > 20:
        st.error(f"Fout: De maximale waarde in de kolom omloopnummer is {max_waarde}. Deze waarde overschrijdt de limiet van 20.")


#st.success(f"De maximale waarde in de kolom omloopnummer is {max_waarde}, wat voldoet aan de voorwaarde.")
#        else:
#            st.warning()
#            f"Er is een fout opgetreden: {e}"