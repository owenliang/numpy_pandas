import pandas as pd

data = pd.read_csv('./c15.csv')

df = data.iloc[0:3][['Student ID', 'age','gender']]
df.to_csv('./c15-sub.csv', index=False)
