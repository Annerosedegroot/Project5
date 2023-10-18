__Planning check tool__

_Description_
Transdev needs a tool to check whether plannings meet certain criteria for their electric busses, specifically line 400 and 401.
This project has been dedicated to making such tool.

_Table of Contents_
Installation ans requirements
Usage
File Structure
Usage Example
Contributing


_Installation and requirements_
The tool is designed to work with python 3.7 or 3.8.
For the tool to work properly, it's necesary to install the following packages/libraries: plotly, streamlit, matplotlib, pandas and numpy.
This can be done by using pip install {library}

_Usage_
For a detailed explanation on how to use the tool, please take a look at the User Manual provided. 

_File Structure_
The code of the tool consists of mostly single files containing one or more functions. The files of importance to users or developers are:

main.py:
containing the design of the streamlit tool. In 'main' the functions from all 'check' files are used to check the input data.

KPI.py:
Calcultes KPI's energy usage and idle_time of the inputfile and displayes it in a clear manner. 

Gantt_Chart.py:
Displays the inputdata in a Gantt chart, both as given and with the empty time-slots filled as 'idle time'.

_Contributing_
Project by Marilène Bos, Ella Coolen, Annerose de Groot, and Teun Voesenek on the instruction of Fontys university of applied science. If any bugs are found, please contact engineeringeindhoven@fontys.nl. 
