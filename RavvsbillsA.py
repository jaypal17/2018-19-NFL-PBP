# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:30:13 2019

@author: JDPallett
"""

import pandas as pd
import numpy as np


df = df[df['GameId'] == 2018090900]
#df = pd.read_csv('pbp-2018.csv')

#series1r = df[(df['SeriesFirstDown'] == 1) & (df['IsRush'] == 1)]
#series1p = df[(df['SeriesFirstDown'] == 1) & (df['IsPass'] == 1)]
#print(series1p ++ series1r)

#1 Sereies Plays
osrplay = df[(df['Down'] == 1) & (df['SeriesFirstDown'] == 1) & (df['IsRush'] == 1)]
ospplay = df[(df['Down'] == 1) & (df['SeriesFirstDown'] == 1) & (df['IsPass'] == 1)]
ostdplay = df[(df['Down'] == 1) & (df['SeriesFirstDown'] == 1) & (df['IsTouchdown'] == 1)]
#2 Series Plays
tsrplay = df[(df['Down'] == 2) & (df['SeriesFirstDown'] == 0) & (df['IsRush'] == 1)]
tspplay = df[(df['Down'] == 2) & (df['SeriesFirstDown'] == 0) & (df['IsPass'] == 1)]
tstdplay= df[(df['Down'] == 1) & (df['SeriesFirstDown'] == 1) & (df['IsTouchdown'] == 1)]
#3 Sereies Plays
thsrplay = df[(df['Down'] == 3) & (df['SeriesFirstDown'] == 0) & (df['IsRush'] == 1)]
thspplay = df[(df['Down'] == 3) & (df['SeriesFirstDown'] == 0) & (df['IsPass'] == 1)]
thstdplay = df[(df['Down'] == 3) & (df['SeriesFirstDown'] == 0) & (df['IsTouchdown'] == 1)]
#4 Sereies Plays 
fsrplay = df[(df['Down'] == 4) & (df['SeriesFirstDown'] == 1) & (df['IsRush'] == 1)]
fspplay = df[(df['Down'] == 4) & (df['SeriesFirstDown'] == 1) & (df['IsPass'] == 1)]
fstdplay = df[(df['Down'] == 4) & (df['SeriesFirstDown'] == 0) & (df['IsTouchdown'] == 1)]

#1 Series print out
print(osrplay, '1 Series Rush Play')
print(ospplay, '1 Series Pass Play')
print(ostdplay, '1 Series Touchdown')
#2 Series print out
print(tsrplay, '2 Series Rush Play')
print(tspplay, '2 Series Pass Play')
print(tstdplay, '2 Series Touchdown')
#3 Series print out
print(thsrplay, '3 Series Rush Plays')
print(thspplay, '3 Series Pass Plays')
print(thstdplay, '3 Series Touchdown Plays')

#4Series print out
print(fsrplay, '4 Sereies Rush Play')
print(fspplay, '4 Sereies Pass Play')
print(fstdplay, '4 Sereies Touchdown Play')





