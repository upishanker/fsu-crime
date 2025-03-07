import pandas as pd

df = pd.read_html("http://police.fsu.edu/crime-log")[0]

# Generate a list of the new columns
new_columns = [chr(x) for x in range(ord('A'), ord('O')+1)]
columns = dict(zip(df.columns, new_columns))
df.rename(columns=columns, inplace=True)
df.to_csv('crime.csv')