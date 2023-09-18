# Do it yourself (Github example)
# pip install streamlit
# streamlit hello

# Import necessary packages
from collections import namedtuple  # For creating a named tuple to store points
import altair as alt  # For creating interactive visualizations
import math  # For mathematical functions
import pandas as pd  # For working with data frames
import streamlit as st  # For creating a web application

# Set the title of the web application
st.title("Project 5: Create your own spiral")
st.text("Are you able to adjust the values?")

# Create sliders for input values
total_points = st.slider("Number of points in spiral", 1, 5000, 2000)  # Slider for total points
num_turns = st.slider("Number of turns in spiral", 1, 100, 9)  # Slider for number of turns

# Create an empty list to store data points
Point = namedtuple('Point', 'x y')  # Define a named tuple to represent a point
data = []

# Create the spiral based on input values
points_per_turn = total_points / num_turns  # Calculate how many points per turn

for curr_point_num in range(total_points):
    curr_turn, i = divmod(curr_point_num, points_per_turn)  # Determine the current turn and point within that turn
    angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn  # Calculate the angle based on the current turn and point
    radius = curr_point_num / total_points  # Calculate the radius based on the current point
    x = radius * math.cos(angle)  # Calculate the x-coordinate
    y = radius * math.sin(angle)  # Calculate the y-coordinate
    data.append(Point(x, y))  # Add the point to the data list

if total_points > 3000:
    st.error('Dit is te veel')
elif total_points < 1000:
    st.warning('De punten kunnen beter omhoog')
else:
    st.success('Yeey, feest')

# Display the spiral using Altair and Streamlit
st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    .mark_circle(color='#0068c9', opacity=0.5)  # Create blue circles with transparency
    .encode(x='x:Q', y='y:Q'))  # Encode the x and y coordinates for the chart
