import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read from pickle cause it way faster than excel
df = pd.read_pickle("Part5/cache_table.pkl")
print(df.columns)

print(df.dtypes)
#df['Profit'] = df['Unnamed: 8'] - df['Unnamed: 9']
#print(df['Profit'])
