# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:44:00 2019

@author: JDPallett
"""
import pandas as pd

df = pd.read_csv('reg_pbp_2018_CarMel_Master.csv')

# Used penalty_player_id instead of using penalty_player_name, J.Jackson
# Occured the most 
penalized = df['penalty_player_id'].value_counts(dropna=True)

print(penalized)

mmoses = df['penalty_player_id'] == 00-0031330
