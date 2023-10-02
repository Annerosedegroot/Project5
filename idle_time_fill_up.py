import numpy as np
import pandas as pd
def idle_time_fill_up(df):
    """
    Function checks if there is a unfilled time slot, so a time slot that has not been given a categorie such as idle. 
    If a time slot is not given any categorie it will give it the categorie idle with the belonging properties.
    
    args:
    ----------- 
    df: DataFrame;
    Works with 'omloopplanning' xlsx file 
    """
    IndexUnfilledIdleTimes = [] 
    for i in range(1, len(df.index)-1):
        if df.iloc[i,3] != df.iloc[i+1,2] and df.iloc[i,8] == df.iloc[i+1,9]: #Checks if there is a empty timeslot in a busline. 
            IndexUnfilledIdleTimes.append(i) #Appends the index of a empty timeslot into a list.

    for i in IndexUnfilledIdleTimes:
        o = i+.5
        df.loc[o] = df.iloc[i,0], df.iloc[i,1], df.iloc[i,3], df.iloc[i+1,3], 'idle', np.NaN, 0.0100, df.iloc[i,9], df.iloc[i+1,8], df.iloc[i,9] #Fills up the empty slot with the categorie idle time including the belonging properties. 
    df = df.sort_index().reset_index(drop=True)
    return df
df = pd.read_excel('omloop planning.xlsx')
df = df.drop(['Unnamed: 0'], axis=1)
print(idle_time_fill_up(df))