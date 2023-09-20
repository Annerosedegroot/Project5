# import the necessary packages
import math  # For mathematical functions
import pandas as pd  # For working with data frames
import streamlit as st  # For creating a web application

# Set the title of the web application
st.title("Project 5: Check the planning")

# Planning in app zetten
upload = st.file_uploader("Choose an Excel file", type='xlsx')

if upload is not None:
    df = pd.read_excel(upload, usecols= ['startlocatie', 'eindlocatie', 'starttijd',	'eindtijd',	'activiteit', 'buslijn', 'energieverbruik', 'starttijd datum', 'eindtijd datum', 'omloop nummer'])
    st.table(df)

# Lay-out app: sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


