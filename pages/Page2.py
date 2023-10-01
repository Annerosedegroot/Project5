import streamlit as st  # For creating a web application
from  Gantt_chart import Gantt_chart
st.title('This is page 2')

df = st.session_state['df']
st.divider()


fig = Gantt_chart(df)
st.pyplot(fig)