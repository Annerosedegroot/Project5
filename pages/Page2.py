import streamlit as st  # For creating a web application
import plotly.express as px
import numpy as np
def Gantt_chart(df):
    """
    Function creates a Gantt chart based on the inputfile.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    ----------
    Gantt chart
    """
    colors = {"materiaal rit":"darkorange", "dienst rit":"dodgerblue", "idle":"red", "opladen":"lime"} #Colors for the different boxes in the Gantt chart

    y_label = {'omloop nummer':'Circulation number'}
    fig = px.timeline(df, x_start="starttijd datum", x_end="eindtijd datum", y="omloop nummer", color = "activiteit", text="buslijn",
                  color_discrete_map = colors, labels = y_label, title = "Gantt chart circulation planning bus line 400 and 401" ) 
    fig.update_yaxes(autorange="reversed") # Otherwise tasks are listed from the bottom up
    fig.update_layout(xaxis_title = "Period",
                 yaxis = dict(
                 tickmode = 'linear',
                 tick0 = 0,
                 dtick = 1)) #To correct the step size of the y axis
    return fig  
def idle_time_fill_up(df):
    """
    Function checks if there is a unfilled time slot, so a time slot that has not been given a categorie such as idle. 
    If a time slot is not given any categorie it will give it the categorie idle with the belonging properties.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    """
    IndexUnfilledIdleTimes = [] 
    for i in range(1, len(df.index)-1):
        if df.iloc[i,3] != df.iloc[i+1,2] and df.iloc[i,8] == df.iloc[i+1,9]: #Checks if there is a empty timeslot in a busline. 
            IndexUnfilledIdleTimes.append(i) #Appends the index of a empty timeslot into a list.

    for i in IndexUnfilledIdleTimes:
        o = i+.5
        df.loc[o] = df.iloc[i,0], df.iloc[i,1], df.iloc[i,3], df.iloc[i+1,3], 'idle', np.NaN, 0.0100, df.iloc[i,9], df.iloc[i+1,8], df.iloc[i,9] #Fills up the empty slot with the categorie idle time including the belonging properties. 
    df = df.sort_index().reset_index(drop=True)
    return df
st.title('This is page 2')

df = st.session_state['df']
st.divider()
df = idle_time_fill_up(df)
fig = Gantt_chart(df)
st.plotly_chart(fig)