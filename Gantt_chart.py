import plotly.express as px
import pandas as pd
df = pd.read_excel("omloop planning.xlsx") #Load the data

colors = {"materiaal rit":"darkorange", "dienst rit":"dodgerblue", "idle":"red", "opladen":"lime"} #Colors for the different boxes in the Gantt chart

y_label = {'omloop nummer':'Circulation number'}
fig = px.timeline(df, x_start="starttijd datum", x_end="eindtijd datum", y="omloop nummer", color = "activiteit",
                  color_discrete_map = colors, labels = y_label, title = "Gantt chart circulation planning bus line 400 and 401") 
fig.update_yaxes(autorange="reversed") # Otherwise tasks are listed from the bottom up
fig.update_layout(xaxis_title = "Period",
                 yaxis = dict(
                 tickmode = 'linear',
                 tick0 = 0,
                 dtick = 1)) #To correct the step size of the y axis
fig.show()