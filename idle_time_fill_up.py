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
    #Starting time earlier than ending time - 1
    lst = []
    for j in range(len(df)-1):
        if df.iloc[j+1,7] < df.iloc[j,8] and df.iloc[j,9] == df.iloc[j+1,9]:
            lst.append(j+1)
    df = df.drop(lst)
    lst.clear()
    df = df.reset_index(drop = True)
    
    #Starting time is endingtime
    lst2 = []
    for j in range(len(df)):
        if df.iloc[j, 2] == df.iloc[j,3] :
            lst2.append(j)
    df = df.drop(lst2)
    lst2.clear()
    df = df.reset_index(drop = True)
    
    IndexUnfilledIdleTimes = [] 
    for i in range(1, len(df.index)-1):
        if df.iloc[i,3] != df.iloc[i+1,2] and df.iloc[i,9] == df.iloc[i+1,9]: #Checks if there is a empty timeslot in a busline. 
            IndexUnfilledIdleTimes.append(i) #Appends the index of a empty timeslot into a list.

    for i in IndexUnfilledIdleTimes:
        o = i +.5
        df.loc[o] = df.iloc[i,1], df.iloc[i,1], df.iloc[i,3], df.iloc[i+1,2], 'idle', np.NaN, 0.0100, df.iloc[i,8], df.iloc[i+1,7], df.iloc[i,9] #Fills up the empty slot with the categorie idle time including the belonging properties. 
    df = df.sort_index().reset_index(drop=True)
    return df
