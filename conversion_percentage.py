# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:39:50 2019

@author: JDPallett
"""

import pandas as pd

# original dataset
df = pd.read_csv('reg_pbp_2018_CarMel_RMVCOLs.csv',dtype={'game_id':int})

# Ravens VS Bills to keep it simple
df = df[df['game_id'] == 2018090900]

#which columns are we keeping


# stored all series
all_series_success = []
all_series_fail = []

# variable for iloc
end_of_series = 0


# Go through dataframe by rows
for index, row in df.iterrows():
    # Checking if it is the end of a series
    if True:
        if row['first_down_rush'] == 1 or row['first_down_pass'] == 1 or row['first_down_penalty'] == 1:
            all_series_success.append(df.iloc[end_of_series:index + 1])
            pass

# success rate
for down in range(1,5):
    for distance in range(1, 30):
        num_success = 0
        num_fail = 0

# Loop through the all_series_success and count how many success there were
for series in all_series_success:
    #check for combo of down and distance in series, then add to count
    if True:
        if row['down'] >= 1 and row['yards_gained'] > 0:
            pass
    
    #check for all_series fail to count how many fails there were
    if True:
       if row['first_down_rush'] == 0 and row['first_down_pass'] == 0 and row['first_down_penalty'] == 0:
            all_series_fail.append(df.iloc[end_of_series:index + 1]) 
    pass

#print out success rate
print(str(down)+'&' + str(distance)+ ': ', num_success, 'out of', num_success + num_fail)
