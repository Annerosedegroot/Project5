import pandas as pd

def sum_idle(df):
    """
    Function calculates total idle_time in given planning
    
    Arg:
    -------
    df
    
    Returns:
    ---------
    amount of 'idle' in column 'activiteit'
    """
    idle_time= df['activiteit'].value_counts()['idle']
    return print(f'total idle time is: {idle_time}' )

def sum_verbruik(df):
    """
    Function calculates total idle_time in given planning
    
    Arg:
    -------
    df
    
    Returns:
    ---------
    sum of all energyusage in planning
    """
    totaal_verbruik = df['energieverbruik'].sum()
    return print(f'total kwh usage is {totaal_verbruik}')

# uploaded = "omloop planning.xlsx" 

# if uploaded is not None:
#     df = pd.read_excel(uploaded)  # Load the Excel file into a DataFrame
#     sum_idle(df)
#     sum_verbruik(df)


    