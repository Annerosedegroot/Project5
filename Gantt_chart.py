import plotly.express as px
import pandas as pd

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
    fig.show()  