import pandas as pd

# original dataset
df = pd.read_csv('reg_pbp_2018_mellon_master.csv')

# Ravens VS Bills to keep it simple
df = df[df['game_id'] == 2018090900]

# stored all series
all_series_success = []
all_series_fail = []

# variable for iloc
index_set = 0


# Go through dataframe by rows
for index, row in df.iterrows():
    # Checking if it is the end of a series no matter success or not
    end_of_series = row ['down'] == 1
    #if successful series
    if row['first_down_rush'] == 1 or row['first_down_pass'] == 1 or row['first_down_penalty'] == 1 or row['touchdown'] == 1:
            #update end of series to index where series stops
            all_series_success.append(df.iloc[index_set:index + 1])
            index_set = index + 1
    else:
        # add failed series here
        row['fourth_down_failed'] == 1 or row['interception'] == 1 or row['safety'] == 1 or row['fumble_lost'] == 1
        all_series_fail.append(df.iloc[index_set:index + 1])
        index_set = index + 1

down = 1
distance = 10

# success rate
#for down in range(1,5):
# for distance in range(1, 30):
num_success = 0
num_fail = 0

# Loop through the all_series_success and count how many success there were
for series in all_series_success:
    # check for combo of down and distance in series, then add to count
    if row ['down'] == 1 and row ['ydstogo'] == 10:
        num_success += 1

    # check for all_series fail to count how many fails there were
for series in all_series_fail:
    if row ['down'] == 1 and row ['ydstogo'] == 10:
        num_fail += 1

    # print out success rate
print(str(down) + '&' + str(distance) + ': ', num_success, 'out of', num_success + num_fail)
