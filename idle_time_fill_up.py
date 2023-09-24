import numpy as np
def idle_time_fill_up(df):
    """Function checks if there is a unfilled time slot, so a time slot that has not been given a categorie such as idle. 
    If a time slot is not given any categorie it will give it the categorie idle with the belonging properties. """
    IndexUnfilledIdleTimes = [] 
    for i in range(1, len(df.index)-1):
        if df.iloc[i,4] != df.iloc[i+1,3] and df.iloc[i,10] == df.iloc[i+1,10]: #Checks if there is a empty timeslot in a busline. 
           IndexUnfilledIdleTimes.append(i) #Appends the index of a empty timeslot into a list.

    for i in IndexUnfilledIdleTimes:
        o = i+.5
        df.loc[o] = i+1, df.iloc[i,2], df.iloc[i,2], df.iloc[i,4], df.iloc[i+1,3], 'idle', np.NaN, 0.0100, df.iloc[i,9], df.iloc[i+1,8], df.iloc[i,10] #Fills up the empty slot with the categorie idle time including the belonging properties. 
    df = df.sort_index().reset_index(drop=True)
