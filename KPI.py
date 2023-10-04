import pandas as pd
from datetime import datetime, timedelta

def sum_verbruik(df):
    """
    Function calculates total verbruik in given planning
    
    Arg:
    -------
    df
    
    Returns:
    ---------
    sum of all energyusage in planning
    """
    totaal_verbruik = df['energieverbruik'].sum()
    return print(f'total kwh usage is {totaal_verbruik}')

def sum_idle(df):
    """
    Function calculates total idle_time in given planning
    
    Arg:
    -------
    df
    
    Returns:
    ---------
    sum of all energyusage in planning
    """
    # Filter rijen waar 'activiteit' gelijk is aan 'idle time'
    idle_rows = df[df['activiteit'] == 'idle']

    # Sommeer de waarden in de 'tijd' kolom om de totale idle time in minuten te krijgen
    total_idle_time = idle_rows['tijd'].sum()  # Verschil in minuten

    return total_idle_time

uploaded = "omloop planning.xlsx"

if uploaded is not None:
    df = pd.read_excel(uploaded)  # Laad het Excel-bestand in een DataFrame

    # Voeg de 'tijd' kolom toe aan de DataFrame zoals je hebt gedaan
    times = []
    for index, row in df.iterrows():
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

    df['tijd'] = times  # Voeg de berekende tijdsverschillen toe aan de DataFrame in de 'tijd' kolom

    # Converteer de 'tijd' kolom naar het aantal minuten (integer)
    df['tijd'] = df['tijd'].apply(lambda x: x.seconds // 60)

    total_idle_minutes = sum_idle(df)
    print(f'Totaal idle tijd in minuten: {total_idle_minutes} minuten')
    print(sum_verbruik(df))

    