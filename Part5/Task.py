import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Part5/lab_4_part_5.xlsx")
df.to_pickle("cache_table.pkl")