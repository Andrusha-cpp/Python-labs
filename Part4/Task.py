import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

def main():
    pickle = "Part4/cache_table.pkl"
    df = pd.read_pickle(pickle)

    season(df)
    sale_type(df)

    

def airport(df):
    #*research on airports
    top_dep = df['ORIG_CITY_CODE'].value_counts().head(10)
    print(top_dep)
    top_arr = df['DEST_CITY_CODE'].value_counts().head(10)
    print(top_arr)

    plt.figure(figsize=(10, 7))
    sns.barplot(x=top_dep.index, y=top_dep.values)
    plt.title("Airports by amount of departures")
    plt.xlabel("Airport")
    plt.ylabel("Amount of departures")
    plt.show()
    #TODO same with arrives

def season(df):
   df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])
   df = df.set_index('FLIGHT_DATE_LOC')
   month_sales = df['REVENUE_AMOUNT'].resample('M').count()

   month_names = [calendar.month_name[m.month] for m in month_sales.index]
   plt.figure(figsize=(10, 7))
   sns.barplot(x=month_names, y=month_sales.values)
   plt.show()

def pas_status(df):
    plt.figure(figsize=(10, 7))
    sns.lineplot(df['REVENUE_AMOUNT'].value_counts())
    plt.title("Graphic of people and ticket prices")
    plt.xlabel("Price")
    plt.ylabel("Amount of people")
    plt.show()

def sale_type(df):
    df['FFP_FLAG'] = df['FFP_FLAG'].replace('', 'No').fillna('No')

    plt.figure(figsize=(10,6))
    sns.countplot(x='SALE_TYPE', hue='FFP_FLAG', data=df)
    plt.xlabel('Sale type')
    plt.ylabel('Amount of clients')
    plt.show()

main()
