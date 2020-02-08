# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)

# Labeling your data
# You can use the DataFrame attribute dfhits.columns to view and assign new string labels to columns in a pandas DataFrame.
# In this exercise, we have imported pandas as pd and defined a DataFrame dfhits containing top Billboard hits from the 1980s (from Wikipedia).
# Each row has the year, artist, song name and the number of weeks at the top. However, this DataFrame has the column labels a, b, c, d. 
# Your job is to use the df.columns attribute to re-assign descriptive column labels.
# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
dfhits.columns = list_labels
print(dfhits)
