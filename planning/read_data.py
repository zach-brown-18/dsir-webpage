import pandas as pd

df = pd.read_csv('./planning/google-sheet.csv')
df.head()

mask = df['MAIN PAGE BRANCHES'] == 'Community'
df[mask]

df