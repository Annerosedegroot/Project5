# Imports
import pandas as pd
import streamlit as st

# WERKT NIET!!


# Function
# def sep_omloop_nr(df):
#     for i in range(len(df['omloop nummer'])-1):
#         if df['omloop nummer'][i] < df['omloop nummer'][i+1]:
#             print('hallo')

def sep_omloop_nr(df):
    separated_dfs = []
    current_omloop_nummer = None
    temp_df = pd.DataFrame(columns=df.columns)

    for index, row in df.iterrows():
        if current_omloop_nummer is None:
            current_omloop_nummer = row['omloop nummer']

        if row['omloop nummer'] != current_omloop_nummer:
            separated_dfs.append(temp_df.copy())
            temp_df = pd.DataFrame(columns=df.columns)
            current_omloop_nummer = row['omloop nummer']

        temp_df = temp_df.append(row, ignore_index=True)

    # Append the last temp_df to the list
    separated_dfs.append(temp_df)

    return separated_dfs

# Usage


# Test

#df = pd.read_excel("omloop planning.xlsx")  # Replace with your Excel file path

#print(sep_omloop_nr(df))