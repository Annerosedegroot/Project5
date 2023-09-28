import streamlit as st

from Gantt_chart import Gantt_chart
from main import df


st.set_page_config(page_title="Visualistations", page_icon="📈")
st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
x = Gantt_chart(df)

st.pyplot(x)