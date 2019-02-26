import pandas as pd

# original dataset
df = pd.read_csv('reg_pbp_2018_mellon_dataset.csv')

# sorted data
df = df.sort_values(['posteam', 'qtr', 'down', 'first_down_rush', 'first_down_pass', 'first_down_penalty'],
                    ascending=[True, False, False, True, True, True])

# Ravens VS Bills to keep it simple
df = df[df['game_id'] == 2018090900]

# sorted data
#df = df.sort_values(['posteam', 'qtr', 'down', 'first_down_rush', 'first_down_pass', 'first_down_penalty'],
    #ascending=[True, False, False, True, True, True])

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



