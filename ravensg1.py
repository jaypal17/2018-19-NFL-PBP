#1. Iterate over the rows (look at each row)
#2. Find when SeriesFirstDown is a 1
#3. print the row where SeriesFirstDown is a 1
#add if statment where series first down is = 1
#for index, row in df.iterrows():
#print


import pandas as pd
import numpy as np

df = pd.read_csv('pbp-2018.csv')
df = df[df['GameId'] == 2018090900]

for index, row in df.iterrows():    
    if (row['SeriesFirstDown'] == 1):
        print(row)
    else:
        print('Nothing')


#print(row['Down'], row['SeriesFirstDown'])

#osrplay = df[(df['Down'] == 1) & (df['SeriesFirstDown'] == 1) & (df['IsRush'] == 1)]




#blah1 = 'dog' + str(1)
#blah2 = 'dog' + str(2)
#blah3 = 'dog' + str(3)
#blah4 = 'dog' + str(4)

#print('1 is', blah1)
#print('2 is', blah2)
#print('3 is', blah3)
#print('4 is', blah4)


#print('')
#print('')
#print('')
# Simple, for loop way

#for i in range(1, 5):
    #blah = 'dog' + str(i)
    #print(str(i) + ' is', blah)

#https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas/16476974#16476974
