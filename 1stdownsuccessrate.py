# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:15:03 2019

@author: JDPallett
"""

#1 how to determine end of end series
#If Offense team changes then end of series and unsuccessful
#2 how to determine if series is successful
#If yards gained is greater than or equal to yards to go then end of series and 
#successful
#3 Need to caluate the success rate of reach series, success for 1st down on 1st
#down success of 1st down on 2nd down, etc.
#if first down is rush, pass, or pen show amount of 1st down on first, sec, thir
#etc play and convert to %

import pandas as pd
import numpy as np

df = pd.read_csv('reg_pbp_2018_CarMel.csv')
df = df[df['game_id'] == 2018090900]

for index, row in df.iterrows(): 
     if (row['down'] == 3) and (row['first_down_rush']== 1 or row['first_down_pass']== 1 or row['first_down_penalty']== 1):
         print('First Time')
    