__Planning check tool__

_Description_
Transdev needs a tool to check whether plannings meet certain criteria for their electric busses, specifically line 400 and 401.
This project has been dedicated to making such tool.

_Table of Contents_
Installation
Usage
File Structure
Features
Requirements
Usage Example
Contributing


_Installation_
For the tool to work properly, it;s necesary to install the following packages/libraries: plotly, streamlit, matplotlib, ...
This can be done by pip install {library}

_Usage_
For a detailed dummy-proof explanation of using the tool, look at the User Manual provided. 

_File Structure_
The code consists of a lot of different single files containing one or more functions. The files of importance to users or developers are the:

main.py:
containing the 'opzet' of the streamlit tool. In main the functions from all 'check' files are used to check the input data.

KPI.py:
Calcultes KPI's energy usage and idle_time of the inputfile and displayes it in a clear manner. 

Gantt_Chart.py:
displaes the inputdata in a Gantt chart, both as given and with the empty time-slots filled as 'idle time'.

Features
List and describe the main features of your project, such as:

Excel file upload
Requirement checks
KPI calculation
Gantt chart visualization
...
_Requirements_
Python 3.7+ (not Python 3.9, because the streamlit library will not work until November 2023)
Streamlit
Pandas
Numpy
Matplotlib
Plotly

_Usage Example_
Provide a usage example, demonstrating how a user can run your tool and get results.

bash
Copy code
streamlit run app.py


_Contributing_
Project by Marilène Bos, Ella Coolen, Annerose de Groot, Teun Voesenek in on the instruction of Fontys university of applied science. If any bugs are found, please contact fontys@engineering.nl .....
