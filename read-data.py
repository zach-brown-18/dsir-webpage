import pandas as pd

df = pd.read_csv('./google-sheet.csv')
df.head()

mask = df['MAIN PAGE BRANCHES'] == 'Community'
df[mask]

