import pandas as pd

# original dataset
df = pd.read_csv('reg_pbp_2018_mellon_rmv_cols.csv')

# Ravens VS Bills to keep it simple
df = df[df['game_id'] == 2018090900]

# stored all series
all_series_success = []
all_series_fail = []

# variable for iloc
end_of_series = 0


# Go through dataframe by rows
for index, row in df.iterrows():
    # Checking if it is the end of a series no matter success or not
    #here ^^^^
    #if successful series
    if row['first_down_rush'] == 1 or row['first_down_pass'] == 1 or row['first_down_penalty'] == 1:
            #update end of series to index where series stops
            all_series_success.append(df.iloc[end_of_series:index + 1])
            end_of_series = index + 1
    else:
        # add failed series here
        row['play_type'] == punt:
        all_series_fail.append()

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
    if (had a 1st and 10):
        num_success += 1

    # check for all_series fail to count how many fails there were
for series in all_series_fail:
    if (had a 1st and 10):
        num_fail += 1

    # print out success rate
print(str(down) + '&' + str(distance) + ': ', num_success, 'out of', num_success + num_fail)
