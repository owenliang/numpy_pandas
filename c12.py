import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])

#print(df['A'], df.A)
#print(df[0:3])
#print(df['20130102':'20130104'])

#print(df.loc['20130102':'20130104'])
#print(df.loc[:,['A','B']])
#print(df.iloc[3:5, 1:3])
print(df.A>8)
print(df[df.A>8])
