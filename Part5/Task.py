import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read from pickle cause it way faster than excel
df = pd.read_pickle("Part5/cache_table.pkl")
print(df.columns)

df['Profit'] = df['Sales'] - df['Cost price']
print(df['Profit'])

