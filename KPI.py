import pandas as pd

def sum_idle(df):
    """
    Function calculated total idle_time in given planning
    
    Arg:
    -------
    Planning, xlsx
    
    Returns:
    ---------
    something
    """
    idle_time= df['activiteit'].value_counts()['idle']
    return print(f'total idle time is: {idle_time}' )

# uploaded = "omloop planning.xlsx" 

# if uploaded is not None:
#     df = pd.read_excel(uploaded)  # Load the Excel file into a DataFrame
#     sum_idle(df)


    