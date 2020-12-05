import pandas as pd

df = pd.read_csv('~/Desktop/database-dsir.csv')
df.head()

mask = df['MAIN PAGE BRANCHES'] == 'Community'
df[mask]

