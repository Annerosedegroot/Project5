import pandas as pd
from datetime import timedelta, datetime

#input: 2 files: (these are the ones we can test with, eventualy we should change them to 'the sheets that are put into the dropbox in the application')
data_transdev = "Connexxion data - 2023-2024.xlsx" #contains 2 sheets: 'Dienstregeling' and 'Afstand matrix'
omloopplanning = "omloop planning.xlsx" #contains 1 sheet, columns: 'startlocatie', 'eindlocatie', 'starttijd',	'eindtijd',	'activiteit', 
                                         #'buslijn', 'energieverbruik', 'starttijd datum', 'eindtijd datum', 'omloop nummer'

# Input file names, change later to input dropbox
data_transdev = "Connexxion data - 2023-2024.xlsx"
omloopplanning = "omloop planning.xlsx"

# Read Excel file into a DataFrame
df_data = pd.read_excel(omloopplanning)

#add a column 'tijd' with time it takes to get from a to b
times = []
for index, row in df_data.iterrows():
    starttijd_str = row['starttijd']
    eindtijd_str = row['eindtijd']
    
    starttijd = datetime.strptime(starttijd_str, '%H:%M:%S').time()
    eindtijd = datetime.strptime(eindtijd_str, '%H:%M:%S').time()
    
    time_difference = timedelta(
        hours=eindtijd.hour - starttijd.hour,
        minutes=eindtijd.minute - starttijd.minute,
        seconds=eindtijd.second - starttijd.second
    )
    times.append(time_difference)

df_data['tijd'] = times  # Add the calculated time differences to the DataFrame in column 'tijd'

print(df_data)

#variables
