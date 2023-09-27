import pandas as pd

def controleer_datatypes(df):
    """
    Function checks whether the datatype in 'startlocatie', 'eindlocatie' and 'energieverbruik' are 
    respectively 'object', 'object' and 'float64' consistantly.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    
    Returns:
    ----------
    Succes or warning-list containing rows with anomalies
    """
    # Controleer het datatype van de kolom 'startlocatie'
    if df['startlocatie'].dtype != 'object':
        print('Fout: De kolom "startlocatie" bevat ongeldige datatypes.')

    # Controleer het datatype van de kolom 'eindlocatie'
    if df['eindlocatie'].dtype != 'object':
        print('Fout: De kolom "eindlocatie" bevat ongeldige datatypes.')

    # Controleer het datatype van de kolom 'energieverbruik'
    if df['energieverbruik'].dtype != 'float64':
        print('Fout: De kolom "energieverbruik" bevat ongeldige datatypes.')

# Laad het Excel-bestand in een DataFrame
#df = pd.read_excel('omloop planning.xlsx')

# Roep de functie aan om de controle uit te voeren
#controleer_datatypes(df)
